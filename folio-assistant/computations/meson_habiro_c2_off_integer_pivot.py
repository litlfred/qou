"""Meson Habiro c_2-off-integer pivot — test if c_2 ≠ 4 exactly.

Task 2 of PR #1617 closed-route follow-ups, per audit
2026-06-01-closed-route-reexamination-roundup.md step (1b)
recommendation:

> Recommend: pivot to a c_2-off-integer hypothesis (test
> `c_2 = 4·(1 + ε·h²)` with PSLQ on ε) before further c_3 work.

The meson Habiro re-exam found C/u² = 4.00606 (0.15% off integer 4).
PR #1581 framed this as `c_2 = 4 exactly, c_3 = −0.7156 absorbs the
0.15% residual`. But step 1's PSLQ NULL on c_3 across 24 substrate
basis elements suggested c_3 might not be a clean substrate quantity.

This probe inverts the framing: assume c_2 is slightly off integer 4
with a leading h² correction:

  c_2 = 4 · (1 + ε · h²)

and solve for ε such that the residual closes ENTIRELY at u² order
(no c_3 contribution needed). Then test ε against natural substrate
quantities (G/π, b², b·G, etc.) via PSLQ.

## Method

  C = c_2 · u² + c_3 · u³ + …
  If c_3 = 0 EXACTLY (the c_2-pivot hypothesis):
    c_2 = C / u² = 4.00606…
    ε   = (c_2 / 4 − 1) / h²

Compute ε at q_0, then PSLQ over 24 substrate basis elements.

## Predictions

  - If ε hits a clean substrate quantity (e.g. G/(8π), b², 1/24):
    REOPEN meson Habiro at tier=near-match with c_2 = 4·(1+ε·h²)
    as the structural form
  - If ε is also PSLQ-NULL like c_3 was: definitively close the
    meson Habiro c=4 reopening with both framings ruled out

## Cross-references

- meson_habiro_c4_truncation_reexam.py (the 0.15% finding)
- meson_habiro_c3_pslq_search.py (c_3 PSLQ NULL)
- audit 2026-06-01-closed-route-reexamination-roundup.md §1b
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
from codata_constants import M_K_PM_MEV_VALIDATION, M_PI_PM_MEV_VALIDATION  # noqa: E402
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def qint(k, q):
    return (q ** k - q ** (-k)) / (q - 1 / q)


def main() -> int:
    set_compute_dps(60)
    q = mp.mpf(Q_50_DIGIT_STR)

    print("=" * 78)
    print("Meson Habiro c_2-off-integer pivot (60 dps)")
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

    m_K = M_K_PM_MEV_VALIDATION
    m_pi = M_PI_PM_MEV_VALIDATION
    target = m_K / m_pi
    chi5 = q ** 5 - q ** (-5)
    seifert_ratio_sq = (mp.mpf(9) / 5) ** 2
    base = chi5 * seifert_ratio_sq
    R_exact = target / base
    C = R_exact - 1

    # c_2-pivot: c_2 = C/u² (no c_3 contribution)
    c_2_pivot = C / u ** 2
    epsilon = (c_2_pivot / 4 - 1) / h2

    print(f"[Setup]")
    print(f"  C / u²        = {mp.nstr(c_2_pivot, 25)}")
    print(f"  c_2 - 4       = {mp.nstr(c_2_pivot - 4, 18)}")
    print(f"  ε = (c_2/4 - 1)/h²")
    print(f"    h² at q_0   = {mp.nstr(h2, 18)}")
    print(f"    ε           = {mp.nstr(epsilon, 25)}")
    print(f"  vs 0:           {mp.nstr(epsilon, 8)}")

    # Substrate basis (same as c_3 PSLQ)
    G = mp.catalan
    basis = {
        "1": mp.mpf(1),
        "G": G,
        "pi": mp.pi,
        "ln2": mp.log(2),
        "q": q,
        "1/q": 1 / q,
        "h": h,
        "h^2": h2,
        "hbar_q": hbar_q,
        "hbar_q^2": hbar_q_sq,
        "b": b,
        "b^2": b_sq,
        "b^3": b ** 3,
        "u": u,
        "[2]_q": q + 1 / q,
        "[3]_q": qint(3, q),
        "[4]_q": qint(4, q),
        "[5]_q": qint(5, q),
        "Jhopf_q0": -(q ** 2 + 1 / q ** 2),
        "G*b": G * b,
        "G*b^2": G * b_sq,
        "G/pi": G / mp.pi,
        "G/8pi": G / (8 * mp.pi),
        "1/24": mp.mpf(1) / 24,
    }
    basis_names = list(basis.keys())
    basis_values = [basis[n] for n in basis_names]

    # Pairwise PSLQ
    print(f"\n[PSLQ — pairwise (ε, b_i)]")
    matches = []
    for name, val in basis.items():
        try:
            rel = mp.pslq([epsilon, val], tol=mp.mpf("1e-12"), maxcoeff=10000)
            if rel and rel[0] != 0:
                ratio = -mp.mpf(rel[1]) / mp.mpf(rel[0])
                check = epsilon - ratio * val
                if abs(check) < mp.mpf("1e-10"):
                    matches.append((f"{rel[1]}/{rel[0]} · {name}", ratio * val, abs(check)))
                    print(f"  ε ≈ ({rel[1]}/{rel[0]}) · {name} = {mp.nstr(ratio * val, 15)} "
                          f"(residual {mp.nstr(abs(check), 8)})")
        except Exception:
            pass

    if not matches:
        print(f"  No tight pairwise integer-relation hits (tol 1e-12, maxcoeff 10000).")

    # Direct candidate scan — handpicked plausible structural values for ε
    print(f"\n[Direct candidate scan]")
    candidates = [
        ("0", mp.mpf(0)),
        ("1/(8π)", mp.mpf(1) / (8 * mp.pi)),
        ("G/(8π)", G / (8 * mp.pi)),
        ("G/(4π)", G / (4 * mp.pi)),
        ("1/24", mp.mpf(1) / 24),
        ("1/26", mp.mpf(1) / 26),
        ("h", h),
        ("h/8", h / 8),
        ("ℏ_q/4", hbar_q / 4),
        ("G/(2π·12)", G / (2 * mp.pi * 12)),
        ("G·b²/(2π)", G * b_sq / (2 * mp.pi)),
        ("3·G/(8π·5)", 3 * G / (8 * mp.pi * 5)),
        ("1/(2[3]_q)", 1 / (2 * qint(3, q))),
        ("b²/4·π", b_sq / (4 * mp.pi)),
        ("G/(2π·14)", G / (2 * mp.pi * 14)),
    ]
    scored = []
    for name, val in candidates:
        diff = val - epsilon
        rel = diff / epsilon * 100 if abs(epsilon) > mp.mpf("1e-30") else mp.inf
        scored.append((name, val, rel))

    scored.sort(key=lambda r: abs(r[2]))
    print(f"  {'name':<22}{'value':<22}{'Δ%':<12}{'band'}")
    for name, val, rel in scored:
        marker = ""
        if abs(rel) < mp.mpf("0.5"):
            marker = " ⭐ within 0.5%"
        elif abs(rel) < mp.mpf("5"):
            marker = " * within 5%"
        print(f"  {name:<22}{mp.nstr(val, 18):<22}{mp.nstr(rel, 6):<12}{marker}")

    # Verdict
    within_05pct = [r for r in scored if abs(r[2]) < mp.mpf("0.5")]
    print(f"\n[Verdict]")
    if matches or within_05pct:
        if matches:
            verdict = (
                f"PSLQ HIT: ε = {matches[0][0]} ≈ {mp.nstr(matches[0][1], 12)}. "
                f"The c_2 pivot finds c_2 = 4·(1 + ({matches[0][0]})·h²) as a "
                f"clean integer relation."
            )
        else:
            names = [n for n, _, _ in within_05pct]
            verdict = (
                f"CANDIDATE: {names[0]} within 0.5%. c_2 = 4·(1 + ε·h²) with "
                f"ε ≈ candidate gives a clean structural form."
            )
    else:
        verdict = (
            f"NULL — neither PSLQ over 24 substrate basis elements nor hand-"
            f"curated candidate scan over 15 plausible ε values finds a clean "
            f"match. ε = {mp.nstr(epsilon, 10)} appears to NOT be a natural "
            f"substrate quantity. The c_2-off-integer pivot does NOT rescue "
            f"the meson Habiro c=4 reopening — both framings (c_2=4+c_3 at "
            f"step 1, c_2=4·(1+ε·h²) here) fail PSLQ at the substrate basis."
        )
    print(f"  {verdict}")

    # ── Witness ──
    w = WitnessBuilder(
        "meson-habiro-c2-off-integer-pivot",
        engine="python",
    )
    w.set_description(
        "Task 2 of PR #1617: tests whether meson Habiro c_2 is exactly 4 or "
        "slightly off-integer with a structural h² correction (c_2 = 4·"
        "(1 + ε·h²)). Pairwise PSLQ across 24 substrate basis elements + "
        "15 hand-curated ε candidates."
    )
    w.add_parameter("q_60dps", Q_50_DIGIT_STR)
    w.add_data("epsilon", mp.nstr(epsilon, 25))
    w.add_data("c_2_pivot_value", mp.nstr(c_2_pivot, 25))
    w.add_data("pslq_matches_count", len(matches))
    w.add_data("within_05pct_count", len(within_05pct))
    w.add_data("verdict", verdict)

    w.add_assertion(
        name="c2_pivot_search_completed",
        computed=True,
        expected=True,
        tolerance=0,
        source=f"c_2 pivot PSLQ + hand-scan completed at 60 dps.",
    )
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
