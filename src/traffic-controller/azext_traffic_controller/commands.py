# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: disable=too-many-lines
# pylint: disable=too-many-statements


def load_command_table(self, _):  # pylint: disable=unused-argument
    from .custom import FrontendCreate
    self.command_table["service-networking traffic-controller frontend create"] = FrontendCreate(loader=self)

    from .custom import AssociationCreate
    self.command_table["service-networking traffic-controller association create"] = AssociationCreate(loader=self)
