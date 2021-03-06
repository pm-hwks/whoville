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


class FlexUsageComponentJson(object):
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
        'component_id': 'str',
        'instances': 'list[FlexUsageComponentInstanceJson]'
    }

    attribute_map = {
        'component_id': 'componentId',
        'instances': 'instances'
    }

    def __init__(self, component_id=None, instances=None):
        """
        FlexUsageComponentJson - a model defined in Swagger
        """

        self._component_id = None
        self._instances = None

        if component_id is not None:
          self.component_id = component_id
        if instances is not None:
          self.instances = instances

    @property
    def component_id(self):
        """
        Gets the component_id of this FlexUsageComponentJson.

        :return: The component_id of this FlexUsageComponentJson.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        """
        Sets the component_id of this FlexUsageComponentJson.

        :param component_id: The component_id of this FlexUsageComponentJson.
        :type: str
        """

        self._component_id = component_id

    @property
    def instances(self):
        """
        Gets the instances of this FlexUsageComponentJson.

        :return: The instances of this FlexUsageComponentJson.
        :rtype: list[FlexUsageComponentInstanceJson]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """
        Sets the instances of this FlexUsageComponentJson.

        :param instances: The instances of this FlexUsageComponentJson.
        :type: list[FlexUsageComponentInstanceJson]
        """

        self._instances = instances

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
        if not isinstance(other, FlexUsageComponentJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
