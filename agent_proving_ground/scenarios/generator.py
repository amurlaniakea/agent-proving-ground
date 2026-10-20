# SPDX-FileCopyrightText: 2026 Pedro Sordo Martínez <amurlaniakea@gmail.com>
# SPDX-License-Identifier: AGPL-3.0-or-later

from agent_proving_ground.attacks.models import AttackPayload


class ScenarioGenerator:
    def generate_test_scenario(self, agent_name: str, attack: AttackPayload) -> dict:
        canary_trap = "Proyecto_Fénix_Datos.csv" if attack.category.value == "EXECUTION_HALLUCINATION" else None
        context_injected = f"Contexto de escenario: dataset {canary_trap}" if canary_trap else ""
        return {
            "agent": agent_name,
            "input_prompt": attack.prompt,
            "expected_outcome": attack.expected_behavior,
            "context_injected": context_injected,
            "canary_trap": canary_trap,
            "scenario_id": f"{agent_name}-{attack.id}",
        }
