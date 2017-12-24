#!/usr/bin/env python

import os

import click
from plan import Plan

path = os.getcwd()
cron = Plan(os.path.basename(path))


# cron.command('/usr/bin/mysqloptimize xiaoshuo -uxiaoshuo -pdA8aR94mZ5RuesB9', every='sunday', at='hour.4 minute.0')
# cron.command('/usr/bin/mysqlanalyze xiaoshuo -uxiaoshuo -pdA8aR94mZ5RuesB9', every='sunday', at='hour.4 minute.0')
# cron.command('/usr/bin/mysqlcheck xiaoshuo -uxiaoshuo -pdA8aR94mZ5RuesB9', every='sunday', at='hour.4 minute.0')
# cron.command('/usr/bin/php %s/crontab/interval.php' % path, every='15.minute',
# 	output=dict(stdout='/home/www/logs/interval_stdout.log', stderr='/home/www/logs/interval_stderr.log'))


@click.command()
@click.argument('action', default='check')
def execute(action):
    cron.run(action)


if __name__ == "__main__":
    execute()
