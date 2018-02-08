from django.shortcuts import render
import logging
from django_tables2 import RequestConfig

from .models import PveStats
import pvestats.tables as stats_tables


PVESTATS_OPTIONS = ['updated', 'number_activities', 'activities_cleared', 'heroic_public_events', 'adventures',
 'seconds_played', 'longest_single_life', 'average_life', 'kills_pga', 'deaths_pga', 'kd', 'longest_spree',
 'most_precision_kills', 'precision_kills_pga', 'longest_kill', 'favorite_weapon', 'suicides_pga', 'suicides',
 'resurrections_received_pga', 'resurrections_performed_pga', 'orbs_dropped_pga', 'orbs_gathered_pga']


"""
Set up logger: for now just print everything to stdout.
"""
logging.basicConfig(format = '%(asctime)s - %(levelname)s - %(message)s',
                    datefmt =' %m/%d/%y %H:%M:%S')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create your views here.
def pvestats(request, stat = 'kd'):
    """Controlling display of pve stats"""
    all_stats = PveStats.objects.all()
    latest_update = all_stats.latest('updated').updated
    logger.debug(f"stat: {stat}")
    if stat == 'all':
        pvestats_table = stats_tables.PveStatsTable(all_stats, order_by = '-kd')
    else:
        logger.debug(f"Making table for {stat}")
        logger.debug(f"set(pve stats): {set(PVESTATS_OPTIONS)}")
        logger.debug(f"set(stat.split()): {set(stat.split())}")
        to_exclude = tuple(set(PVESTATS_OPTIONS) - set(stat.split()) )
        logger.debug(f"Excluding {to_exclude}.")
        pvestats_table = stats_tables.PveStatsTable(all_stats, order_by = '-'+stat, exclude = to_exclude)
    RequestConfig(request, paginate={'per_page':25}).configure(pvestats_table)
    context = {'pvestats_table': pvestats_table, 'updated': latest_update}
    return render(request, 'pvestats/pvestats.html', context)