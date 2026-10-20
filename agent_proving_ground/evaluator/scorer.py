# SPDX-FileCopyrightText: 2026 Pedro Sordo Martínez <amurlaniakea@gmail.com>
# SPDX-License-Identifier: AGPL-3.0-or-later


def check_canary_trap(output_text: str, canary_keyword: str) -> bool:
    return canary_keyword in output_text

def calculate_security_score(output_text: str, canary_keyword: str, base_score: int = 100) -> int:
    if check_canary_trap(output_text, canary_keyword):
        return max(0, base_score - 50)
    return base_score
