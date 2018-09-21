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


class NetworkResponse(object):
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
        'description': 'str',
        'subnet_cidr': 'str',
        'cloud_platform': 'str',
        'parameters': 'dict(str, object)',
        'topology_id': 'int',
        'name': 'str',
        'id': 'int',
        'public_in_account': 'bool'
    }

    attribute_map = {
        'description': 'description',
        'subnet_cidr': 'subnetCIDR',
        'cloud_platform': 'cloudPlatform',
        'parameters': 'parameters',
        'topology_id': 'topologyId',
        'name': 'name',
        'id': 'id',
        'public_in_account': 'publicInAccount'
    }

    def __init__(self, description=None, subnet_cidr=None, cloud_platform=None, parameters=None, topology_id=None, name=None, id=None, public_in_account=False):
        """
        NetworkResponse - a model defined in Swagger
        """

        self._description = None
        self._subnet_cidr = None
        self._cloud_platform = None
        self._parameters = None
        self._topology_id = None
        self._name = None
        self._id = None
        self._public_in_account = None

        if description is not None:
          self.description = description
        if subnet_cidr is not None:
          self.subnet_cidr = subnet_cidr
        self.cloud_platform = cloud_platform
        if parameters is not None:
          self.parameters = parameters
        if topology_id is not None:
          self.topology_id = topology_id
        self.name = name
        if id is not None:
          self.id = id
        if public_in_account is not None:
          self.public_in_account = public_in_account

    @property
    def description(self):
        """
        Gets the description of this NetworkResponse.
        description of the resource

        :return: The description of this NetworkResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this NetworkResponse.
        description of the resource

        :param description: The description of this NetworkResponse.
        :type: str
        """
        if description is not None and len(description) > 1000:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1000`")
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")

        self._description = description

    @property
    def subnet_cidr(self):
        """
        Gets the subnet_cidr of this NetworkResponse.
        the subnet definition of the network in CIDR format

        :return: The subnet_cidr of this NetworkResponse.
        :rtype: str
        """
        return self._subnet_cidr

    @subnet_cidr.setter
    def subnet_cidr(self, subnet_cidr):
        """
        Sets the subnet_cidr of this NetworkResponse.
        the subnet definition of the network in CIDR format

        :param subnet_cidr: The subnet_cidr of this NetworkResponse.
        :type: str
        """

        self._subnet_cidr = subnet_cidr

    @property
    def cloud_platform(self):
        """
        Gets the cloud_platform of this NetworkResponse.
        type of cloud provider

        :return: The cloud_platform of this NetworkResponse.
        :rtype: str
        """
        return self._cloud_platform

    @cloud_platform.setter
    def cloud_platform(self, cloud_platform):
        """
        Sets the cloud_platform of this NetworkResponse.
        type of cloud provider

        :param cloud_platform: The cloud_platform of this NetworkResponse.
        :type: str
        """
        if cloud_platform is None:
            raise ValueError("Invalid value for `cloud_platform`, must not be `None`")

        self._cloud_platform = cloud_platform

    @property
    def parameters(self):
        """
        Gets the parameters of this NetworkResponse.
        provider specific parameters of the specified network

        :return: The parameters of this NetworkResponse.
        :rtype: dict(str, object)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this NetworkResponse.
        provider specific parameters of the specified network

        :param parameters: The parameters of this NetworkResponse.
        :type: dict(str, object)
        """

        self._parameters = parameters

    @property
    def topology_id(self):
        """
        Gets the topology_id of this NetworkResponse.
        id of the topology the resource belongs to

        :return: The topology_id of this NetworkResponse.
        :rtype: int
        """
        return self._topology_id

    @topology_id.setter
    def topology_id(self, topology_id):
        """
        Sets the topology_id of this NetworkResponse.
        id of the topology the resource belongs to

        :param topology_id: The topology_id of this NetworkResponse.
        :type: int
        """

        self._topology_id = topology_id

    @property
    def name(self):
        """
        Gets the name of this NetworkResponse.
        name of the resource

        :return: The name of this NetworkResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this NetworkResponse.
        name of the resource

        :param name: The name of this NetworkResponse.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def id(self):
        """
        Gets the id of this NetworkResponse.
        id of the resource

        :return: The id of this NetworkResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this NetworkResponse.
        id of the resource

        :param id: The id of this NetworkResponse.
        :type: int
        """

        self._id = id

    @property
    def public_in_account(self):
        """
        Gets the public_in_account of this NetworkResponse.
        resource is visible in account

        :return: The public_in_account of this NetworkResponse.
        :rtype: bool
        """
        return self._public_in_account

    @public_in_account.setter
    def public_in_account(self, public_in_account):
        """
        Sets the public_in_account of this NetworkResponse.
        resource is visible in account

        :param public_in_account: The public_in_account of this NetworkResponse.
        :type: bool
        """

        self._public_in_account = public_in_account

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
        if not isinstance(other, NetworkResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
