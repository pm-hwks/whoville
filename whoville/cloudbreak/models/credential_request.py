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


class CredentialRequest(object):
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
        'cloud_platform': 'str',
        'parameters': 'dict(str, object)',
        'description': 'str',
        'topology_id': 'int'
    }

    attribute_map = {
        'name': 'name',
        'cloud_platform': 'cloudPlatform',
        'parameters': 'parameters',
        'description': 'description',
        'topology_id': 'topologyId'
    }

    def __init__(self, name=None, cloud_platform=None, parameters=None, description=None, topology_id=None):
        """
        CredentialRequest - a model defined in Swagger
        """

        self._name = None
        self._cloud_platform = None
        self._parameters = None
        self._description = None
        self._topology_id = None

        self.name = name
        self.cloud_platform = cloud_platform
        if parameters is not None:
          self.parameters = parameters
        if description is not None:
          self.description = description
        if topology_id is not None:
          self.topology_id = topology_id

    @property
    def name(self):
        """
        Gets the name of this CredentialRequest.
        name of the resource

        :return: The name of this CredentialRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CredentialRequest.
        name of the resource

        :param name: The name of this CredentialRequest.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if name is not None and len(name) > 100:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")
        if name is not None and len(name) < 5:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `5`")
        if name is not None and not re.search('(^[a-z][-a-z0-9]*[a-z0-9]$)', name):
            raise ValueError("Invalid value for `name`, must be a follow pattern or equal to `/(^[a-z][-a-z0-9]*[a-z0-9]$)/`")

        self._name = name

    @property
    def cloud_platform(self):
        """
        Gets the cloud_platform of this CredentialRequest.
        type of cloud provider

        :return: The cloud_platform of this CredentialRequest.
        :rtype: str
        """
        return self._cloud_platform

    @cloud_platform.setter
    def cloud_platform(self, cloud_platform):
        """
        Sets the cloud_platform of this CredentialRequest.
        type of cloud provider

        :param cloud_platform: The cloud_platform of this CredentialRequest.
        :type: str
        """
        if cloud_platform is None:
            raise ValueError("Invalid value for `cloud_platform`, must not be `None`")

        self._cloud_platform = cloud_platform

    @property
    def parameters(self):
        """
        Gets the parameters of this CredentialRequest.
        cloud specific parameters for credential

        :return: The parameters of this CredentialRequest.
        :rtype: dict(str, object)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this CredentialRequest.
        cloud specific parameters for credential

        :param parameters: The parameters of this CredentialRequest.
        :type: dict(str, object)
        """

        self._parameters = parameters

    @property
    def description(self):
        """
        Gets the description of this CredentialRequest.
        description of the resource

        :return: The description of this CredentialRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CredentialRequest.
        description of the resource

        :param description: The description of this CredentialRequest.
        :type: str
        """
        if description is not None and len(description) > 1000:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1000`")
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")

        self._description = description

    @property
    def topology_id(self):
        """
        Gets the topology_id of this CredentialRequest.
        id of the topology the resource belongs to

        :return: The topology_id of this CredentialRequest.
        :rtype: int
        """
        return self._topology_id

    @topology_id.setter
    def topology_id(self, topology_id):
        """
        Sets the topology_id of this CredentialRequest.
        id of the topology the resource belongs to

        :param topology_id: The topology_id of this CredentialRequest.
        :type: int
        """

        self._topology_id = topology_id

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
        if not isinstance(other, CredentialRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
