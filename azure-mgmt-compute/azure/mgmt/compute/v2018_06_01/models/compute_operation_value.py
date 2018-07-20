# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComputeOperationValue(Model):
    """Describes the properties of a Compute Operation value.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar origin: The origin of the compute operation.
    :vartype origin: str
    :ivar name: The name of the compute operation.
    :vartype name: str
    :ivar operation: The display name of the compute operation.
    :vartype operation: str
    :ivar resource: The display name of the resource the operation applies to.
    :vartype resource: str
    :ivar description: The description of the operation.
    :vartype description: str
    :ivar provider: The resource provider for the operation.
    :vartype provider: str
    """

    _validation = {
        'origin': {'readonly': True},
        'name': {'readonly': True},
        'operation': {'readonly': True},
        'resource': {'readonly': True},
        'description': {'readonly': True},
        'provider': {'readonly': True},
    }

    _attribute_map = {
        'origin': {'key': 'origin', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'operation': {'key': 'display.operation', 'type': 'str'},
        'resource': {'key': 'display.resource', 'type': 'str'},
        'description': {'key': 'display.description', 'type': 'str'},
        'provider': {'key': 'display.provider', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ComputeOperationValue, self).__init__(**kwargs)
        self.origin = None
        self.name = None
        self.operation = None
        self.resource = None
        self.description = None
        self.provider = None
