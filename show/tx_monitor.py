#!/usr/sbin/env python

import click
import utilities_common.cli as clicommon

#
# 'tx-monitor' subcommand ('show tx_monitor ...')
#
@click.command('tx-monitor')
@clicommon.pass_db
def tx_monitor(db):
    tx_mon_cfg = db.get_data("TX_MONITOR", "GLOBAL")
    click.echo("threshold: {}".format(tx_mon_cfg["threshold"]))
    click.echo("time_period: {}".format(tx_mon_cfg["time_period"]))
