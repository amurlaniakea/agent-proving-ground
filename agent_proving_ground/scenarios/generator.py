SPDX-FileCopyrightText: 2026 Pedro Sordo Martínez <amurlaniakea@gmail.com>
SPDX-License-Identifier: AGPL-3.0-or-later

from agent_proving_ground.attacks.models import AttackPayload


class ScenarioGenerator:
    def generate_test_scenario(self, agent_name: str, attack: AttackPayload) -> dict:
        return {
            "agent": agent_name,
            "input_prompt": attack.prompt,
            "expected_outcome": attack.expected_behavior,
            "scenario_id": f"{agent_name}-{attack.id}",
        }
