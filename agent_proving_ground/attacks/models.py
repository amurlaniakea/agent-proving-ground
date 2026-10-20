# SPDX-FileCopyrightText: 2026 Pedro Sordo Martínez <amurlaniakea@gmail.com>
# SPDX-License-Identifier: AGPL-3.0-or-later

from enum import Enum

from pydantic import BaseModel


class AttackCategory(str, Enum):
    JAILBREAK = "JAILBREAK"
    PRIVILEGE_ESCALATION = "PRIVILEGE_ESCALATION"
    DATA_EXFILTRATION = "DATA_EXFILTRATION"
    EXECUTION_HALLUCINATION = "EXECUTION_HALLUCINATION"


class AttackPayload(BaseModel):
    id: str
    category: AttackCategory
    prompt: str
    expected_behavior: str
