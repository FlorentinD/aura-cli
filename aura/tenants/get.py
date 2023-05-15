import click
from aura.api_command import api_command
from aura.repository import make_api_call

@api_command
@click.option('--tenant_id', '-tid', prompt=True)
def get(tenant_id):
    path = f"/tenants/{tenant_id}"

    return make_api_call("GET", path)