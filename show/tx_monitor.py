#!/usr/sbin/env python

import click
import utilities_common.cli as clicommon

#
# 'tx-monitor' subcommand ('show tx_monitor ...')
#
@click.command('tx-monitor')
@click.option('--interfaces', '-i', required=False, type=str)
@clicommon.pass_db
def tx_monitor(db, interfaces):
    tx_monitor_keys = sorted(db.db.keys(db.db.STATE_DB, "TX_MONITOR_TABLE|*"))
    if interfaces:
        interfaces = interfaces.split(",")

    if tx_monitor_keys is not None:
        click.echo("  Interface         |   Status")
        click.echo("---------------------------------------")
        for key in tx_monitor_keys:
            _,eth_name = key.split('|')
            if not interfaces or eth_name in interfaces:
                data = db.db.get_all(db.db.STATE_DB, key)
                click.echo("{}              {}".format(eth_name, data["status"]))
