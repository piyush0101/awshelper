import click
import boto


@click.group()
@click.option('--verbose', default=False)
def cli(verbose):
    click.echo('Verbose mode is %s' % ('on' if debug else 'off'))

@cli.command()
def stacks():
    click.echo('Stacks!')

@cli.command()
def instances():
    click.echo('Instances!')

#@click.command()
#def cli():
#    click.echo('Do the cli')

#def main():
#    """AWS command line helpers"""
#    greet = 'Howdy' if as_cowboy else 'Hello'
#    click.echo('{0}, {1}.'.format(greet, name))

#@click.command()
#@click.option('--as-cowboy', '-c', is_flag=True, help='Greet as a cowboy.')
#@click.argument('name', default='world', required=False)

#def main(name, as_cowboy):
#    """AWS command line helpers"""
#    greet = 'Howdy' if as_cowboy else 'Hello'
#    click.echo('{0}, {1}.'.format(greet, name))
