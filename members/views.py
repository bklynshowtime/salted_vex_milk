import requests
import logging
import time

from django import forms
from django.shortcuts import render
from django.db.utils import IntegrityError

from .forms import MemberForm
from .models import Member
import d2api.utils as api
from d2api.constants import GROUP_ID, D2_HEADERS


"""
Set up logger: for now just print everything to stdout.
"""
logging.basicConfig(level = logging.INFO,  #DEBUG, INFO
                    format = '%(asctime)s - %(levelname)s - %(message)s',
                    datefmt =' %m/%d/%y %H:%M:%S')
logger = logging.getLogger(__name__)



# Create your views here.
def members(request):
    """Home page for salted vex milk"""
    if request.method == 'POST':
        with requests.Session() as session:
            session.headers.update(D2_HEADERS)
            #Functionalize the following you will use it for each end poin
            #time_init_memblist = time.process_time()
            members_url = api.get_members_of_group_url(GROUP_ID)
            logging.info(f"Retreiving group members. URL: {members_url}")
            try:
                members_data = api.destiny2_api_handler(members_url, session)
            except Exception as err:
                logging.exception(f"Error getting clan members for {GROUP_ID}.\nException: {err}.")
            else:
                members = api.extract_member_list(members_data)
                #elapsed_time_memblist = time.process_time() - time_init_memblist
                #logging.info(f"Memberlist construction time: {elapsed_time_memblist}")
                #update or insert member data
                for member in members:
                    time_init_process_member = time.process_time()
                    name = member['name']
                    logging.info(f"Processing {name}.")
#                    #Determine if user has played d2 or not
#                    time_init_profile = time.process_time()
#                    profile_url = api.get_profile_url(member['member_id'], member['membership_type']) #/?components=' + components #200
#                    profile_params = {'components': '200'}
#                    try:
#                        profile_response = api.make_request(profile_url, session, request_params = profile_params)
#                        logging.info(f"ThrottleSeconds: {profile_response.json()['ThrottleSeconds']}")
#
#                        if profile_response.json()['ErrorStatus'] == 'DestinyAccountNotFound':
#                            member['has_played_d2'] = False
#                        else:
#                            member['has_played_d2'] = True
#                    except:
#                        logging.error(f"No profile data for {name}. URL: {profile_url}")
#                    elapsed_time_profile = time.process_time() - time_init_profile
#                    logging.info(f"Check if has played time: {elapsed_time_profile}")

                    #determine if member exists or not, and update/insert accordingly
                    time_init_exists = time.process_time()
                    try:
                        member_instance = Member.objects.get(member_id = member['member_id'],
                                                             membership_type = member['membership_type'])
                    except Member.DoesNotExist:
                        member_form_bound = MemberForm(member)
                    else:
                        logging.debug(f"{name} already exists: updating.")
                        member_form_bound = MemberForm(member, instance = member_instance)
                    elapsed_time_exists = time.process_time() - time_init_exists
                    logging.debug(f"Check if player instance exists: {elapsed_time_exists}")

                    #validate and save form
                    time_init_validate = time.process_time()
                    if member_form_bound.is_valid():
                        try:
                            member_form_bound.save()
                        except IntegrityError as err:
                            logging.error(f"Integrity error: {err}")
                        else:
                            logging.debug(f"{name} successfully saved.")
                    else:
                        logging.error(f"member form not valid. error: {member_form_bound.errors}.\nMember data: {member}")
                        raise forms.ValidationError(f"Member info not valid: {member_form_bound.errors}")
                    elapsed_time_validate = time.process_time() - time_init_validate
                    logging.debug(f"Validation time: {elapsed_time_validate}")

                    elapsed_time_process_member = time.process_time() - time_init_process_member
                    logging.info(f"{name} add time: {elapsed_time_process_member}\n")


    else:
        logging.debug("GET request in members/members.html: just display data.")

    all_members = Member.objects.all().order_by('date_joined')
    context = {'members': all_members}
    return render(request, 'members/members.html', context) # 'index.html', {'update_clan_form': update_clan_form})