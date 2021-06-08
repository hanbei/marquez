from dbt.adapters.base import AdapterPlugin

from dbt.adapters.openlineage_snowflake.connections import OpenLineageSnowflakeCredentials, OpenLineageSnowflakeConnectionManager
from dbt.adapters.openlineage_snowflake.impl import OpenLineageSnowflakeAdapter
from dbt.include import openlineage_snowflake

__author__ = """Marquez Project"""

Plugin = AdapterPlugin(
    adapter=OpenLineageSnowflakeAdapter,
    credentials=OpenLineageSnowflakeCredentials,
    include_path=openlineage_snowflake.PACKAGE_PATH,
    dependencies=['snowflake'])
