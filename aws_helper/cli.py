import click
import pprint
import boto3

@click.group()
@click.option('--verbose/--no-verbose', default=False)
def cli(verbose):
    click.echo('Verbose mode is on') if verbose else ''

@cli.command()
def stacks():
    click.echo('Stacks!')
    client = boto3.client('cloudformation')
    stacks = client.list_stacks( StackStatusFilter=['CREATE_IN_PROGRESS', 'CREATE_FAILED', 'CREATE_COMPLETE', 'ROLLBACK_IN_PROGRESS', 'ROLLBACK_FAILED', 'ROLLBACK_COMPLETE', 'DELETE_IN_PROGRESS', 'DELETE_FAILED', 'DELETE_COMPLETE', 'UPDATE_IN_PROGRESS', 'UPDATE_COMPLETE_CLEANUP_IN_PROGRESS', 'UPDATE_COMPLETE', 'UPDATE_ROLLBACK_IN_PROGRESS', 'UPDATE_ROLLBACK_FAILED', 'UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS', 'UPDATE_ROLLBACK_COMPLETE' ])
    pprint.pprint(stacks)

@cli.command()
def instances():
    click.echo('Instances!')
    client = boto3.client('ec2')
    instances = client.describe_instances()
    pprint.pprint(instances)

if __name__ == '__main__':
    cli()

