# SPDX-FileCopyrightText: 2026 Pedro Sordo Martínez <amurlaniakea@gmail.com>
# SPDX-License-Identifier: AGPL-3.0-or-later

from agent_proving_ground.attacks.library import get_attack_library
from agent_proving_ground.attacks.models import AttackCategory
from agent_proving_ground.scenarios.generator import ScenarioGenerator


def test_library_load():
    library = get_attack_library()
    assert len(library) == 3
    categories = [a.category for a in library]
    assert AttackCategory.JAILBREAK in categories


def test_scenario_generation():
    library = get_attack_library()
    first_attack = library[0]
    gen = ScenarioGenerator()
    scenario = gen.generate_test_scenario("TestAgent", first_attack)
    assert scenario["agent"] == "TestAgent"
    assert scenario["input_prompt"] == first_attack.prompt
