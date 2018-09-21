# coding: utf-8

"""
    Cloudbreak API

    Cloudbreak is a powerful left surf that breaks over a coral reef, a mile off southwest the island of Tavarua, Fiji. Cloudbreak is a cloud agnostic Hadoop as a Service API. Abstracts the provisioning and ease management and monitoring of on-demand clusters. SequenceIQ's Cloudbreak is a RESTful application development platform with the goal of helping developers to build solutions for deploying Hadoop YARN clusters in different environments. Once it is deployed in your favourite servlet container it exposes a REST API allowing to span up Hadoop clusters of arbitary sizes and cloud providers. Provisioning Hadoop has never been easier. Cloudbreak is built on the foundation of cloud providers API (Amazon AWS, Microsoft Azure, Google Cloud Platform, Openstack), Apache Ambari, Docker lightweight containers, Swarm and Consul. For further product documentation follow the link: <a href=\"http://hortonworks.com/apache/cloudbreak/\">http://hortonworks.com/apache/cloudbreak/</a>

    OpenAPI spec version: 2.7.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class RDSConfigResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'connection_url': 'str',
        'type': 'str',
        'connector_jar_url': 'str',
        'id': 'int',
        'creation_date': 'int',
        'public_in_account': 'bool',
        'cluster_names': 'list[str]',
        'stack_version': 'str',
        'database_engine': 'str',
        'connection_driver': 'str',
        'database_engine_display_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'connection_url': 'connectionURL',
        'type': 'type',
        'connector_jar_url': 'connectorJarUrl',
        'id': 'id',
        'creation_date': 'creationDate',
        'public_in_account': 'publicInAccount',
        'cluster_names': 'clusterNames',
        'stack_version': 'stackVersion',
        'database_engine': 'databaseEngine',
        'connection_driver': 'connectionDriver',
        'database_engine_display_name': 'databaseEngineDisplayName'
    }

    def __init__(self, name=None, connection_url=None, type=None, connector_jar_url=None, id=None, creation_date=None, public_in_account=False, cluster_names=None, stack_version=None, database_engine=None, connection_driver=None, database_engine_display_name=None):
        """
        RDSConfigResponse - a model defined in Swagger
        """

        self._name = None
        self._connection_url = None
        self._type = None
        self._connector_jar_url = None
        self._id = None
        self._creation_date = None
        self._public_in_account = None
        self._cluster_names = None
        self._stack_version = None
        self._database_engine = None
        self._connection_driver = None
        self._database_engine_display_name = None

        self.name = name
        self.connection_url = connection_url
        self.type = type
        if connector_jar_url is not None:
          self.connector_jar_url = connector_jar_url
        if id is not None:
          self.id = id
        if creation_date is not None:
          self.creation_date = creation_date
        if public_in_account is not None:
          self.public_in_account = public_in_account
        if cluster_names is not None:
          self.cluster_names = cluster_names
        if stack_version is not None:
          self.stack_version = stack_version
        self.database_engine = database_engine
        self.connection_driver = connection_driver
        self.database_engine_display_name = database_engine_display_name

    @property
    def name(self):
        """
        Gets the name of this RDSConfigResponse.
        Name of the RDS configuration resource

        :return: The name of this RDSConfigResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this RDSConfigResponse.
        Name of the RDS configuration resource

        :param name: The name of this RDSConfigResponse.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def connection_url(self):
        """
        Gets the connection_url of this RDSConfigResponse.
        JDBC connection URL in the form of jdbc:<db-type>://<address>:<port>/<db>

        :return: The connection_url of this RDSConfigResponse.
        :rtype: str
        """
        return self._connection_url

    @connection_url.setter
    def connection_url(self, connection_url):
        """
        Sets the connection_url of this RDSConfigResponse.
        JDBC connection URL in the form of jdbc:<db-type>://<address>:<port>/<db>

        :param connection_url: The connection_url of this RDSConfigResponse.
        :type: str
        """
        if connection_url is None:
            raise ValueError("Invalid value for `connection_url`, must not be `None`")

        self._connection_url = connection_url

    @property
    def type(self):
        """
        Gets the type of this RDSConfigResponse.
        Type of RDS, aka the service name that will use the RDS like HIVE, DRUID, SUPERSET, RANGER, etc.

        :return: The type of this RDSConfigResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this RDSConfigResponse.
        Type of RDS, aka the service name that will use the RDS like HIVE, DRUID, SUPERSET, RANGER, etc.

        :param type: The type of this RDSConfigResponse.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def connector_jar_url(self):
        """
        Gets the connector_jar_url of this RDSConfigResponse.
        URL that points to the jar of the connection driver(connector)

        :return: The connector_jar_url of this RDSConfigResponse.
        :rtype: str
        """
        return self._connector_jar_url

    @connector_jar_url.setter
    def connector_jar_url(self, connector_jar_url):
        """
        Sets the connector_jar_url of this RDSConfigResponse.
        URL that points to the jar of the connection driver(connector)

        :param connector_jar_url: The connector_jar_url of this RDSConfigResponse.
        :type: str
        """

        self._connector_jar_url = connector_jar_url

    @property
    def id(self):
        """
        Gets the id of this RDSConfigResponse.
        id of the resource

        :return: The id of this RDSConfigResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RDSConfigResponse.
        id of the resource

        :param id: The id of this RDSConfigResponse.
        :type: int
        """

        self._id = id

    @property
    def creation_date(self):
        """
        Gets the creation_date of this RDSConfigResponse.
        creation time of the resource in long

        :return: The creation_date of this RDSConfigResponse.
        :rtype: int
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """
        Sets the creation_date of this RDSConfigResponse.
        creation time of the resource in long

        :param creation_date: The creation_date of this RDSConfigResponse.
        :type: int
        """

        self._creation_date = creation_date

    @property
    def public_in_account(self):
        """
        Gets the public_in_account of this RDSConfigResponse.
        resource is visible in account

        :return: The public_in_account of this RDSConfigResponse.
        :rtype: bool
        """
        return self._public_in_account

    @public_in_account.setter
    def public_in_account(self, public_in_account):
        """
        Sets the public_in_account of this RDSConfigResponse.
        resource is visible in account

        :param public_in_account: The public_in_account of this RDSConfigResponse.
        :type: bool
        """

        self._public_in_account = public_in_account

    @property
    def cluster_names(self):
        """
        Gets the cluster_names of this RDSConfigResponse.
        list of clusters which use config

        :return: The cluster_names of this RDSConfigResponse.
        :rtype: list[str]
        """
        return self._cluster_names

    @cluster_names.setter
    def cluster_names(self, cluster_names):
        """
        Sets the cluster_names of this RDSConfigResponse.
        list of clusters which use config

        :param cluster_names: The cluster_names of this RDSConfigResponse.
        :type: list[str]
        """

        self._cluster_names = cluster_names

    @property
    def stack_version(self):
        """
        Gets the stack_version of this RDSConfigResponse.
        (HDP, HDF)Stack version for the RDS configuration

        :return: The stack_version of this RDSConfigResponse.
        :rtype: str
        """
        return self._stack_version

    @stack_version.setter
    def stack_version(self, stack_version):
        """
        Sets the stack_version of this RDSConfigResponse.
        (HDP, HDF)Stack version for the RDS configuration

        :param stack_version: The stack_version of this RDSConfigResponse.
        :type: str
        """

        self._stack_version = stack_version

    @property
    def database_engine(self):
        """
        Gets the database_engine of this RDSConfigResponse.
        Name of the external database engine (MYSQL, POSTGRES...)

        :return: The database_engine of this RDSConfigResponse.
        :rtype: str
        """
        return self._database_engine

    @database_engine.setter
    def database_engine(self, database_engine):
        """
        Sets the database_engine of this RDSConfigResponse.
        Name of the external database engine (MYSQL, POSTGRES...)

        :param database_engine: The database_engine of this RDSConfigResponse.
        :type: str
        """
        if database_engine is None:
            raise ValueError("Invalid value for `database_engine`, must not be `None`")

        self._database_engine = database_engine

    @property
    def connection_driver(self):
        """
        Gets the connection_driver of this RDSConfigResponse.
        Name of the JDBC connection driver (for example: 'org.postgresql.Driver')

        :return: The connection_driver of this RDSConfigResponse.
        :rtype: str
        """
        return self._connection_driver

    @connection_driver.setter
    def connection_driver(self, connection_driver):
        """
        Sets the connection_driver of this RDSConfigResponse.
        Name of the JDBC connection driver (for example: 'org.postgresql.Driver')

        :param connection_driver: The connection_driver of this RDSConfigResponse.
        :type: str
        """
        if connection_driver is None:
            raise ValueError("Invalid value for `connection_driver`, must not be `None`")

        self._connection_driver = connection_driver

    @property
    def database_engine_display_name(self):
        """
        Gets the database_engine_display_name of this RDSConfigResponse.
        Display name of the external database engine (Mysql, PostgreSQL...)

        :return: The database_engine_display_name of this RDSConfigResponse.
        :rtype: str
        """
        return self._database_engine_display_name

    @database_engine_display_name.setter
    def database_engine_display_name(self, database_engine_display_name):
        """
        Sets the database_engine_display_name of this RDSConfigResponse.
        Display name of the external database engine (Mysql, PostgreSQL...)

        :param database_engine_display_name: The database_engine_display_name of this RDSConfigResponse.
        :type: str
        """
        if database_engine_display_name is None:
            raise ValueError("Invalid value for `database_engine_display_name`, must not be `None`")

        self._database_engine_display_name = database_engine_display_name

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, RDSConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
