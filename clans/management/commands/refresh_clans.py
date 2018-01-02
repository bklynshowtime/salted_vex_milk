#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 20:34:57 2017

@author: eric
"""
import requests
import logging

from django import forms
from django.core.management.base import BaseCommand #, CommandError
import d2api.utils as api
from clans.forms import ClanForm
from clans.models import Clan
from d2api.constants import GROUP_ID, D2_HEADERS


"""
Set up logger_clan_refresh: for now just print everything to stdout.
"""
logging.basicConfig(level = logging.DEBUG,
                    format = '%(asctime)s - %(levelname)s - %(message)s',
                    datefmt =' %m/%d/%y %H:%M:%S')
logger_clan_refresh = logging.getLogger(__name__)



class Command(BaseCommand):
    help = 'Refreshes Clan information'

    def handle(self, *args, **options):

        with requests.Session() as session:
            session.headers.update(D2_HEADERS)
            #Functionalize the following you will use it for each end point
            group_url = api.get_group_url(GROUP_ID)
            logger_clan_refresh.info(f"Retreiving info about clan. URL: {group_url}")
            try:
                group_data = api.destiny2_api_handler(group_url, session)
            except Exception as err:
                logger_clan_refresh.exception(f"Error getting clan data for {GROUP_ID}.\nException: {err}.")
            else:
                clan_info = api.extract_clan_info(group_data)
                #Someone suggested pushing the following into the Form instead of the view
                try:
                    clan_instance = Clan.objects.get(clan_id = clan_info['clan_id'])
                except Clan.DoesNotExist:
                    logger_clan_refresh.debug("Adding clan to db.")
                    clan_form_bound = ClanForm(clan_info)
                else:
                    logger_clan_refresh.debug("Clan already exists: updating.")
                    clan_form_bound = ClanForm(clan_info, instance = clan_instance)

                if clan_form_bound.is_valid():
                    clan_form_bound.save()
                    logger_clan_refresh.info("Clan successfully refreshed.")
                else:
                    logger_clan_refresh.error(f"clan form not valid. error: {clan_form_bound.errors}")
                    raise forms.ValidationError(f"Clan info not valid: {clan_form_bound.errors}")