from django.shortcuts import render
import logging
from django_tables2 import RequestConfig

from members.models import Member
from .models import PvpStats
import pvpstats.tables as stats_tables
#from .tables import PvpStatsTable

PVPSTATS_OPTIONS = ['greatness', 'seconds_played', 'win_loss_ratio',
               'kills_per_match', 'deaths_per_match', 'kd', 'longest_spree',
               'most_kills', 'favorite_weapon', 'suicide_rate',
               'trials_number_matches', 'trials_kd', 'trials_win_loss_ratio']

"""
Set up logger: for now just print everything to stdout.
"""
logging.basicConfig(format = '%(asctime)s - %(levelname)s - %(message)s',
                    datefmt =' %m/%d/%y %H:%M:%S')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create your views here.
def pvpstats(request, stat = 'kd'):
    """Controlling display of pvp stats"""
    all_stats = PvpStats.objects.all()
    latest_update = all_stats.latest('updated').updated
    logger.debug(f"stat: {stat}")
    if stat == 'all':
        pvpstats_table = stats_tables.PvpStatsTable(all_stats, order_by = '-kd')
    else:
        logger.debug(f"Making table for {stat}")
        logger.debug(f"set(pvp stats): {set(PVPSTATS_OPTIONS)}")
        logger.debug(f"set(stat.split()): {set(stat.split())}")
        to_exclude = tuple(set(PVPSTATS_OPTIONS) - set(stat.split()) )
        logger.debug(f"Excluding {to_exclude}.")
        pvpstats_table = stats_tables.PvpStatsTable(all_stats, order_by = '-'+stat, exclude = to_exclude)
    RequestConfig(request, paginate={'per_page':25}).configure(pvpstats_table)
    context = {'pvpstats_table': pvpstats_table, 'updated': latest_update}
    return render(request, 'pvpstats/pvpstats.html', context)


def memberpvp(request, name = 'cortical_iv'):
    """
    Controls display of individual member pvp stats.
    NOT USED:
    You were going to have al ink on the pvpstats page to show this
    but it is completely redundant if they are clicking on that row
    they already have that data!
    """
    member = Member.objects.get(name=name)
    pvpstats_member = PvpStats.objects.get(member=member.id)
    updated = pvpstats_member.updated
    kd = str(pvpstats_member.kd)
    favorite = pvpstats_member.favorite_weapon
    memberpvp_data = [
            {'stat': 'K/D', 'value': kd},
            {'stat': 'Favorite', 'value': favorite}]
    memberpvp_table = stats_tables.MemberPvpTable(memberpvp_data)
    RequestConfig(request).configure(memberpvp_table)
    context = {'memberpvp_table': memberpvp_table, 'member': member, 'updated': updated}
    return render(request, 'pvpstats/memberpvp.html', context)

