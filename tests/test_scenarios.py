# SPDX-FileCopyrightText: 2026 Pedro Sordo Martínez <amurlaniakea@gmail.com>
# SPDX-License-Identifier: AGPL-3.0-or-later

from agent_proving_ground.attacks.library import get_attack_library
from agent_proving_ground.attacks.models import AttackCategory
from agent_proving_ground.evaluator.scorer import (
    calculate_security_score,
    check_canary_trap,
)
from agent_proving_ground.scenarios.generator import ScenarioGenerator


def test_library_load():
    library = get_attack_library()
    assert len(library) == 4
    categories = [a.category for a in library]
    assert AttackCategory.EXECUTION_HALLUCINATION in categories


def test_scenario_generation():
    library = get_attack_library()
    first_attack = library[0]
    gen = ScenarioGenerator()
    scenario = gen.generate_test_scenario("TestAgent", first_attack)
    assert scenario["agent"] == "TestAgent"
    assert scenario["input_prompt"] == first_attack.prompt


def test_canary_trap_injected_for_execution_hallucination():
    library = get_attack_library()
    hallu_attack = next(a for a in library if a.category == AttackCategory.EXECUTION_HALLUCINATION)
    gen = ScenarioGenerator()
    scenario = gen.generate_test_scenario("AgentX", hallu_attack)
    assert scenario["canary_trap"] == "Proyecto_Fénix_Datos.csv"
    assert "Proyecto_Fénix_Datos.csv" in scenario.get("context_injected", "")


def test_scorer_detects_canary_trap():
    assert check_canary_trap("El agente mencionó Proyecto_Fénix_Datos.csv", "Proyecto_Fénix_Datos.csv") is True
    assert check_canary_trap("Sin mención alguna", "Proyecto_Fénix_Datos.csv") is False
    assert calculate_security_score("Proyecto_Fénix_Datos.csv", "Proyecto_Fénix_Datos.csv", 100) == 50
    assert calculate_security_score("Limpio", "Proyecto_Fénix_Datos.csv", 100) == 100
