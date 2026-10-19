# agent-proving-ground

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: AGPL-3.0-or-later](https://img.shields.io/badge/License-AGPL--3.0--or--later-green.svg)](https://www.gnu.org/licenses/agpl-3.0)

> **Benchmark de integridad para agentes de IA** — Generador de escenarios adversarios (`behavioral jailbreaks`, `execution hallucination`, `privilege escalation`) y framework de evaluación robusta (`Robustness Score`, `Safety Score`).

---

## Problema Real

Los benchmarks actuales para agentes (`AgentHarm`, `EconEvals`) son frágiles (`arXiv:2605.22568`) porque no simulan ataques multi-turno en entornos `OS` reales. `LITMUS` (`arXiv:2605.10779`) cubre `behavioral jailbreaks` con verificación dual (`semantic` + `physical`), pero no ofrece una biblioteca de ataques reutilizable ni un `harness` de evaluación integral.

---

## Referencias Verificadas

- `arXiv:2605.10779` — `LITMUS`: Benchmark de `behavioral jailbreaks` en `OS` reales con verificación dual.
- `arXiv:2605.22568` — `Measuring Security Without Fooling Ourselves`: Por qué los benchmarks actuales son engañosos.
- `arXiv:2607.25379` — `Cyber-Capable AI Agents`: Vulnerabilidades, evaluación y respuesta defensiva.

---

## Quickstart

```python
from agent_proving_ground.attacks.library import get_attack_library
from agent_proving_ground.scenarios.generator import ScenarioGenerator

library = get_attack_library()
gen = ScenarioGenerator()
scenario = gen.generate_test_scenario("AgentTest", library[0])
```

---

## Arquitectura

```text
AttackLibrary (3 payloads fijos) -> ScenarioGenerator -> Sandbox (Docker) -> DualVerifier -> Scorer
```

- `AttackLibrary`: Ataques deterministas (`InceptionRAG`, `MIA`, `Hijacking`).
- `ScenarioGenerator`: Genera escenarios reproducibles (`agent_name`, `input_prompt`, `expected_outcome`).
- `Sandbox`: Entorno `Docker` aislado para ejecutar agentes sin riesgo al host.
- `DualVerifier`: Verificación dual (`semantic` + `syscall-level` `auditd`) para detectar `execution hallucination`.
- `Scorer`: Calcula `Robustness Score` y `Safety Score` con comparabilidad entre modelos.

---

## Instalación

```bash
git clone https://github.com/amurlaniakea/agent-proving-ground.git
```

---

## Autor

**Pedro Sordo Martínez** — `amurlaniakea@gmail.com`

`SPDX-FileCopyrightText: 2026 Pedro Sordo Martínez <amurlaniakea@gmail.com>`
`SPDX-License-Identifier: AGPL-3.0-or-later`
