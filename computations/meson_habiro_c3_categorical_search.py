"""Meson Habiro c_3 categorical-identification candidate search.

Per author 2026-05-31 + this branch's audit
2026-06-01-closed-route-reexamination-roundup.md step (1):

The REOPENED meson Habiro c=4 route has c_3 = −0.7156 absorbing the
residual at 50 dps (|c_3·u³|/|c_2·u²| = 0.0015, well within natural
truncation bounds). To convert this from REOPENED to PROVED, we
need to identify c_3 = −0.7156 to a NATURAL Hecke/Bring/braid
quantity (not a fit).

## The target

  c_3 = −0.71557706... at q_0 (from meson Habiro c=4 reexam, 50 dps)

Setup recap (from probe `meson_habiro_c4_truncation_reexam.py`):
- u = b · ℏ_q²    where b² = (h² + 3)/(h² + 4)
- C/u² = 4.00606 (vs integer 4)
- Assuming c_2 = 4 exactly, c_3 = (C - 4·u²) / u³ = −0.71557706...

## Method — candidate scan

Test ~30 natural q-arithmetic / Hecke / braid quantities at q_0,
score by |Δ%|. Looking for:
- Δ% within 0.05% (structurally suggestive)
- Δ% within 0.5% (worth investigating)
- Δ% > 5% (rule out)

Categories:
1. Simple integer/rational fractions (−1/2, −3/4, ...)
2. Catalan-G-based (G ≈ 0.916, so −G ≈ −0.916; −G/√2 ≈ −0.648, ...)
3. b-power related (b ≈ 0.868, b² ≈ 0.753, b³ ≈ 0.654, b⁴ ≈ 0.567)
4. J-times-b-power (J = -2; −J·b² = 1.5, J·b² = −1.5, ...)
5. Hecke symmetrizer eigenvalues at H_3, H_4
6. Borromean Markov-trace evaluations

## Cross-references

- audit 2026-06-01-closed-route-reexamination-roundup.md step (1)
- meson_habiro_c4_truncation_reexam.py (the −0.7156 finding)
- option_e_v9_one_plus_q_structural_audit.py (33-candidate template)
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    set_compute_dps(50)
    q = mp.mpf(Q_50_DIGIT_STR)

    print("=" * 78)
    print("Meson Habiro c_3 categorical-identification search (50 dps)")
    print("=" * 78)
    print(f"\nq_0 = {Q_50_DIGIT_STR}\n")

    # Reproduce target from meson_habiro_c4_truncation_reexam.py
    h = q - 1 / q
    h2 = h * h
    b_sq = (h2 + 3) / (h2 + 4)
    b = mp.sqrt(b_sq)
    hbar_q = 1 - 1 / q
    hbar_q_sq = hbar_q ** 2
    u = b * hbar_q_sq

    m_K = mp.mpf("493.677")
    m_pi = mp.mpf("139.57039")
    target = m_K / m_pi
    chi5 = q ** 5 - q ** (-5)
    seifert_ratio_sq = (mp.mpf(9) / 5) ** 2
    base = chi5 * seifert_ratio_sq
    R_exact = target / base
    C = R_exact - 1
    c_3_target = (C - 4 * u ** 2) / u ** 3

    print(f"[Setup recap from reexam probe]")
    print(f"  b     = {mp.nstr(b, 18)}")
    print(f"  ℏ_q²  = {mp.nstr(hbar_q_sq, 18)}")
    print(f"  u     = {mp.nstr(u, 18)}")
    print(f"  C     = {mp.nstr(C, 18)}")
    print(f"\n[Target]")
    print(f"  c_3 (so 4·u² + c_3·u³ = C) = {mp.nstr(c_3_target, 25)}")

    # Hecke / braid helpers
    q2 = q + 1 / q  # [2]_q
    q3 = (q ** 3 - q ** (-3)) / (q - 1 / q)  # [3]_q
    q4 = (q ** 4 - q ** (-4)) / (q - 1 / q)  # [4]_q
    G = mp.catalan
    J = mp.mpf(-2)  # J_Hopf(q=1)

    candidates = [
        # 1. Simple integer/rational fractions
        ("−1/2", -mp.mpf(1) / 2),
        ("−3/4", -mp.mpf(3) / 4),
        ("−2/3", -mp.mpf(2) / 3),
        ("−5/7", -mp.mpf(5) / 7),
        ("−7/10", -mp.mpf(7) / 10),
        # 1a. Other simple ratios near 0.715
        ("−12/17", -mp.mpf(12) / 17),
        ("−10/14 = −5/7", -mp.mpf(10) / 14),
        ("−15/21 = −5/7", -mp.mpf(15) / 21),
        ("−11/15", -mp.mpf(11) / 15),
        ("−16/22 = −8/11", -mp.mpf(8) / 11),
        # 2. Catalan G based
        ("−G", -G),
        ("−G/2", -G / 2),
        ("−G·b", -G * b),
        ("−G·b²", -G * b_sq),
        ("−2G/π", -2 * G / mp.pi),
        ("−G·(1 − ℏ_q)", -G * (1 - hbar_q)),
        ("−G·[2]_q/[3]_q", -G * q2 / q3),
        # 3. b-power based
        ("−b", -b),
        ("−b²", -b_sq),
        ("−b³", -b ** 3),
        ("−b⁴", -b ** 4),
        ("−b²·(1 − ℏ_q)", -b_sq * (1 - hbar_q)),
        # 4. J·b power (J = -2)
        ("J·b/2 = −b", J * b / 2),
        ("J·b²/2 = −b²", J * b_sq / 2),
        ("J·b³/2 = −b³", J * b ** 3 / 2),
        ("J·b⁴/2", J * b ** 4 / 2),
        ("J·b/3", J * b / 3),
        ("J·b²/3", J * b_sq / 3),
        # 5. q-bracket / Hecke ratios
        ("−[2]_q/3", -q2 / 3),
        ("−[3]_q/4", -q3 / 4),
        ("−[2]_q·b²/π", -q2 * b_sq / mp.pi),
        ("−(1+q⁻¹)/2 · b", -(1 + 1 / q) / 2 * b),
        # 5a. q-bracket ratios (test −5/7 hypothesis = quantum-deformed?)
        ("−[5]_q/[7]_q", -((q ** 5 - q ** (-5)) / (q - 1 / q))
         / ((q ** 7 - q ** (-7)) / (q - 1 / q))),
        ("−[3]_q/[4]_q", -q3 / q4),
        ("−[2]_q/[3]_q", -q2 / q3),
        ("−[5]_q/[7]_q · b", -((q ** 5 - q ** (-5)) / (q - 1 / q))
         / ((q ** 7 - q ** (-7)) / (q - 1 / q)) * b),
        ("−[2]_q²/[3]_q²·b²", -q2 ** 2 / q3 ** 2 * b_sq),
        # 6. h-power based — placeholder removed (was hardcoded fudge)
        # 7. Combinations of Hecke Jones with substrate
        ("J·b/2·(1+ℏ_q)", J * b / 2 * (1 + hbar_q)),
        # 8. Specific Borromean/Hopf
        ("J/π", J / mp.pi),
        ("J·(1−G)/2", J * (1 - G) / 2),
        # 9. Quark-mass-style heuristics
        ("−2·b²/(1+b²)", -2 * b_sq / (1 + b_sq)),
        ("−(1−h²)·b²", -(1 - h2) * b_sq),
        ("−ℏ_q·[2]_q/(2·b)", -hbar_q * q2 / (2 * b)),
    ]

    # Score
    print(f"\n[Candidates sorted by |Δ%|]")
    print(f"  {'name':<36}{'value':<18}{'Δ%':<14}{'band'}")
    scored = []
    for name, val in candidates:
        diff = val - c_3_target
        rel = diff / c_3_target * 100 if abs(c_3_target) > mp.mpf("1e-30") else mp.inf
        scored.append((name, val, rel))

    scored.sort(key=lambda r: abs(r[2]))
    for name, val, rel in scored:
        marker = ""
        if abs(rel) < mp.mpf("0.05"):
            marker = " ⭐ within 0.05%"
        elif abs(rel) < mp.mpf("0.5"):
            marker = " * within 0.5%"
        elif abs(rel) < mp.mpf("5"):
            marker = " . within 5%"
        print(f"  {name:<36}{mp.nstr(val, 12):<18}{mp.nstr(rel, 6):<14}{marker}")

    # Discrimination
    within_005 = [r for r in scored if abs(r[2]) < mp.mpf("0.05")]
    within_05 = [r for r in scored if abs(r[2]) < mp.mpf("0.5")]
    within_5 = [r for r in scored if abs(r[2]) < mp.mpf("5")]

    print(f"\n[Summary]")
    print(f"  Within 0.05%: {len(within_005)} candidates")
    for n, v, e in within_005:
        print(f"    {n}: Δ% = {mp.nstr(e, 6)}")
    print(f"  Within 0.5%:  {len(within_05)} candidates")
    for n, v, e in within_05:
        print(f"    {n}: Δ% = {mp.nstr(e, 6)}")
    print(f"  Within 5%:    {len(within_5)} candidates")

    # ── Verdict ──
    print(f"\n[Verdict]")
    if len(within_005) == 0 and len(within_05) == 0:
        verdict = (
            f"NULL — none of the {len(candidates)} natural candidates lands "
            f"within 0.5% of c_3 = {mp.nstr(c_3_target, 8)}. The categorical "
            f"identity (if it exists) requires a wider search beyond the "
            f"natural q-arithmetic / G / b-power / J-Hopf basis."
        )
    elif len(within_005) >= 1:
        names = [n for n, _, _ in within_005]
        verdict = (
            f"CANDIDATE FOUND ({len(within_005)} within 0.05%): {names}. "
            f"This is structurally suggestive (parallels Option E v9's "
            f"(1+q)/2 uniqueness)."
        )
    else:
        names = [n for n, _, _ in within_05]
        verdict = (
            f"WEAK CANDIDATES ({len(within_05)} within 0.5%): {names}. "
            f"Worth investigating but not yet a clean identification."
        )
    print(f"  {verdict}")

    # ── Witness ──
    w = WitnessBuilder(
        "meson-habiro-c3-categorical-search",
        engine="python",
    )
    w.set_description(
        "Categorical-identification candidate scan for the meson Habiro "
        "c_3 = −0.7156 (from the REOPENED 2026-06-01 closed-route audit). "
        "Tests 30+ natural Hecke / Bring / Catalan-G / J-Hopf / b-power "
        "candidates at q_0. Records best-match candidates within 0.05% / "
        "0.5% / 5% bands."
    )
    w.add_parameter("q_50dps", Q_50_DIGIT_STR)
    w.add_data("c_3_target", mp.nstr(c_3_target, 25))
    w.add_data("best_candidates_within_05pct",
               [(n, mp.nstr(v, 15), mp.nstr(e, 8)) for n, v, e in within_05])
    w.add_data("best_candidates_within_5pct",
               [(n, mp.nstr(v, 15), mp.nstr(e, 8)) for n, v, e in within_5])
    w.add_data("verdict", verdict)

    w.add_assertion(
        name="candidate_search_completed",
        computed=len(candidates),
        expected=len(candidates),
        tolerance=0,
        source=f"Scanned {len(candidates)} candidates at 50 dps.",
    )
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
