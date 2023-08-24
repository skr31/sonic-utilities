#!/usr/sbin/env python

import click
import utilities_common.cli as clicommon

#
# 'tx_monitor' group ('config tx_monitor ...')
#
@click.group(cls=clicommon.AliasedGroup)
def tx_monitor():
    """Configure tx monitor commands group"""
    pass

#
# 'set' group ('config tx_monitor set ...')
#
@tx_monitor.group(cls=clicommon.AbbreviationGroup, name='set')
def tx_monitor_set():
    pass

#
# 'threshold' subcommand ('config tx_monitor set threshold ...')
#
@tx_monitor_set.command('threshold')
@click.argument('thresh', required=True, type=int)
@clicommon.pass_db
def set_threshold(db, thresh):
    click.echo("setting threshold to {}".format(thresh))
    set_param("threshold", thresh, db)

#
# 'time_period' subcommand ('config tx_monitor set time_period ...')
#
@tx_monitor_set.command('time_period')
@click.argument('time', required=True, type=int)
@clicommon.pass_db
def set_time_period(db, time):
    click.echo("setting time period to {}".format(time))
    set_param("time_period", time, db)

def set_param(param_type, param_value, db):
    db.cfgdb.mod_config({ "TX_MONITOR": { 
                                "GLOBAL": {
                                    param_type: param_value
                                }
                            }
                        })