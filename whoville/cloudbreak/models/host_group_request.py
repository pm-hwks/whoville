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


class HostGroupRequest(object):
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
        'constraint': 'Constraint',
        'recipe_ids': 'list[int]',
        'recovery_mode': 'str',
        'recipes': 'list[RecipeRequest]',
        'recipe_names': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'constraint': 'constraint',
        'recipe_ids': 'recipeIds',
        'recovery_mode': 'recoveryMode',
        'recipes': 'recipes',
        'recipe_names': 'recipeNames'
    }

    def __init__(self, name=None, constraint=None, recipe_ids=None, recovery_mode=None, recipes=None, recipe_names=None):
        """
        HostGroupRequest - a model defined in Swagger
        """

        self._name = None
        self._constraint = None
        self._recipe_ids = None
        self._recovery_mode = None
        self._recipes = None
        self._recipe_names = None

        self.name = name
        self.constraint = constraint
        if recipe_ids is not None:
          self.recipe_ids = recipe_ids
        if recovery_mode is not None:
          self.recovery_mode = recovery_mode
        if recipes is not None:
          self.recipes = recipes
        if recipe_names is not None:
          self.recipe_names = recipe_names

    @property
    def name(self):
        """
        Gets the name of this HostGroupRequest.
        name of the resource

        :return: The name of this HostGroupRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this HostGroupRequest.
        name of the resource

        :param name: The name of this HostGroupRequest.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def constraint(self):
        """
        Gets the constraint of this HostGroupRequest.
        instance group or resource constraint for a hostgroup

        :return: The constraint of this HostGroupRequest.
        :rtype: Constraint
        """
        return self._constraint

    @constraint.setter
    def constraint(self, constraint):
        """
        Sets the constraint of this HostGroupRequest.
        instance group or resource constraint for a hostgroup

        :param constraint: The constraint of this HostGroupRequest.
        :type: Constraint
        """
        if constraint is None:
            raise ValueError("Invalid value for `constraint`, must not be `None`")

        self._constraint = constraint

    @property
    def recipe_ids(self):
        """
        Gets the recipe_ids of this HostGroupRequest.
        referenced recipe ids

        :return: The recipe_ids of this HostGroupRequest.
        :rtype: list[int]
        """
        return self._recipe_ids

    @recipe_ids.setter
    def recipe_ids(self, recipe_ids):
        """
        Sets the recipe_ids of this HostGroupRequest.
        referenced recipe ids

        :param recipe_ids: The recipe_ids of this HostGroupRequest.
        :type: list[int]
        """

        self._recipe_ids = recipe_ids

    @property
    def recovery_mode(self):
        """
        Gets the recovery_mode of this HostGroupRequest.
        recovery mode of the hostgroup's nodes

        :return: The recovery_mode of this HostGroupRequest.
        :rtype: str
        """
        return self._recovery_mode

    @recovery_mode.setter
    def recovery_mode(self, recovery_mode):
        """
        Sets the recovery_mode of this HostGroupRequest.
        recovery mode of the hostgroup's nodes

        :param recovery_mode: The recovery_mode of this HostGroupRequest.
        :type: str
        """
        allowed_values = ["MANUAL", "AUTO"]
        if recovery_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `recovery_mode` ({0}), must be one of {1}"
                .format(recovery_mode, allowed_values)
            )

        self._recovery_mode = recovery_mode

    @property
    def recipes(self):
        """
        Gets the recipes of this HostGroupRequest.
        referenced recipes

        :return: The recipes of this HostGroupRequest.
        :rtype: list[RecipeRequest]
        """
        return self._recipes

    @recipes.setter
    def recipes(self, recipes):
        """
        Sets the recipes of this HostGroupRequest.
        referenced recipes

        :param recipes: The recipes of this HostGroupRequest.
        :type: list[RecipeRequest]
        """

        self._recipes = recipes

    @property
    def recipe_names(self):
        """
        Gets the recipe_names of this HostGroupRequest.
        referenced recipe names

        :return: The recipe_names of this HostGroupRequest.
        :rtype: list[str]
        """
        return self._recipe_names

    @recipe_names.setter
    def recipe_names(self, recipe_names):
        """
        Sets the recipe_names of this HostGroupRequest.
        referenced recipe names

        :param recipe_names: The recipe_names of this HostGroupRequest.
        :type: list[str]
        """

        self._recipe_names = recipe_names

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
        if not isinstance(other, HostGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other