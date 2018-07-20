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


class RegionalReplicationStatus(Model):
    """This is the regional replication status.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar region: The region where the gallery image version is published to.
    :vartype region: str
    :ivar state: This is the regional replication state. Possible values
     include: 'Unknown', 'Replicating', 'Completed', 'Failed'
    :vartype state: str or
     ~azure.mgmt.compute.v2018_06_01.models.ReplicationState
    :ivar details: The details of the replication status.
    :vartype details: str
    :ivar progress: It indicates progress of the replication job.
    :vartype progress: int
    """

    _validation = {
        'region': {'readonly': True},
        'state': {'readonly': True},
        'details': {'readonly': True},
        'progress': {'readonly': True},
    }

    _attribute_map = {
        'region': {'key': 'region', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'details': {'key': 'details', 'type': 'str'},
        'progress': {'key': 'progress', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(RegionalReplicationStatus, self).__init__(**kwargs)
        self.region = None
        self.state = None
        self.details = None
        self.progress = None
