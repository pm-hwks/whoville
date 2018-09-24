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


class ConstraintTemplateRequest(object):
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
        'description': 'str',
        'cpu': 'float',
        'memory': 'float',
        'disk': 'float',
        'orchestrator_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'cpu': 'cpu',
        'memory': 'memory',
        'disk': 'disk',
        'orchestrator_type': 'orchestratorType'
    }

    def __init__(self, name=None, description=None, cpu=None, memory=None, disk=None, orchestrator_type=None):
        """
        ConstraintTemplateRequest - a model defined in Swagger
        """

        self._name = None
        self._description = None
        self._cpu = None
        self._memory = None
        self._disk = None
        self._orchestrator_type = None

        self.name = name
        if description is not None:
          self.description = description
        self.cpu = cpu
        self.memory = memory
        self.disk = disk
        self.orchestrator_type = orchestrator_type

    @property
    def name(self):
        """
        Gets the name of this ConstraintTemplateRequest.
        name of the resource

        :return: The name of this ConstraintTemplateRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ConstraintTemplateRequest.
        name of the resource

        :param name: The name of this ConstraintTemplateRequest.
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
    def description(self):
        """
        Gets the description of this ConstraintTemplateRequest.
        description of the resource

        :return: The description of this ConstraintTemplateRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ConstraintTemplateRequest.
        description of the resource

        :param description: The description of this ConstraintTemplateRequest.
        :type: str
        """
        if description is not None and len(description) > 1000:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1000`")
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")

        self._description = description

    @property
    def cpu(self):
        """
        Gets the cpu of this ConstraintTemplateRequest.
        number of CPU cores needed for the Ambari node

        :return: The cpu of this ConstraintTemplateRequest.
        :rtype: float
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """
        Sets the cpu of this ConstraintTemplateRequest.
        number of CPU cores needed for the Ambari node

        :param cpu: The cpu of this ConstraintTemplateRequest.
        :type: float
        """
        if cpu is None:
            raise ValueError("Invalid value for `cpu`, must not be `None`")

        self._cpu = cpu

    @property
    def memory(self):
        """
        Gets the memory of this ConstraintTemplateRequest.
        memory needed for the Ambari container (GB)

        :return: The memory of this ConstraintTemplateRequest.
        :rtype: float
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """
        Sets the memory of this ConstraintTemplateRequest.
        memory needed for the Ambari container (GB)

        :param memory: The memory of this ConstraintTemplateRequest.
        :type: float
        """
        if memory is None:
            raise ValueError("Invalid value for `memory`, must not be `None`")

        self._memory = memory

    @property
    def disk(self):
        """
        Gets the disk of this ConstraintTemplateRequest.
        disk size needed for an Ambari node (GB)

        :return: The disk of this ConstraintTemplateRequest.
        :rtype: float
        """
        return self._disk

    @disk.setter
    def disk(self, disk):
        """
        Sets the disk of this ConstraintTemplateRequest.
        disk size needed for an Ambari node (GB)

        :param disk: The disk of this ConstraintTemplateRequest.
        :type: float
        """
        if disk is None:
            raise ValueError("Invalid value for `disk`, must not be `None`")

        self._disk = disk

    @property
    def orchestrator_type(self):
        """
        Gets the orchestrator_type of this ConstraintTemplateRequest.
        type of orchestrator

        :return: The orchestrator_type of this ConstraintTemplateRequest.
        :rtype: str
        """
        return self._orchestrator_type

    @orchestrator_type.setter
    def orchestrator_type(self, orchestrator_type):
        """
        Sets the orchestrator_type of this ConstraintTemplateRequest.
        type of orchestrator

        :param orchestrator_type: The orchestrator_type of this ConstraintTemplateRequest.
        :type: str
        """
        if orchestrator_type is None:
            raise ValueError("Invalid value for `orchestrator_type`, must not be `None`")

        self._orchestrator_type = orchestrator_type

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
        if not isinstance(other, ConstraintTemplateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other