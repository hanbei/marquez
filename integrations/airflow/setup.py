#!/usr/bin/env python
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()


package_name = "marquez-airflow"
package_version = "0.15.0"
description = """Marquez integration with Airflow"""


requirements = [
    "attrs>=19.3",
    "requests>=2.24.0",
    "sqlparse>=0.3.1",
    f"marquez-common>={package_version}",
]

extras_require = {
    "tests": [
        "pytest",
        "pytest-cov",
        "flake8",
        "SQLAlchemy==1.3.18",       # must be set to 1.3.* for airflow tests compatibility
        "pandas-gbq==0.13.2",       # must be set to 0.14.* for airflow tests compatibility
        "apache-airflow==1.10.12",
        "apache-airflow[gcp_api]==1.10.12",
        "apache-airflow[google]==1.10.12",
        "apache-airflow[postgres]==1.10.12",
        "snowflake-connector-python==2.2.9",
        "airflow-provider-great-expectations==0.0.6",
    ],
}
extras_require["dev"] = set(sum(extras_require.values(), []))

setup(
    name=package_name,
    version=package_version,
    description=description,
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Marquez Project",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    extras_require=extras_require,
    python_requires=">=3.6",
    zip_safe=False,
    keywords="marquez",
)
