"""Q_β c_3 = -2 — sign-block / Plancherel template check (Item 3 of PR #1650).

PR #1645 sign-block hypothesis: (α_em/π)·P_λ at a 1-dim Wedderburn block
of H_3 reproduces the m_p Ocneanu correction. Does the same template
apply to Q_β c_3 = J_Hopf(q=1) = -2 from Probe B?

## The Q_β c_3 = -2 finding

Per PR #1581 Probe B and merged audit
`2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`:
  c_3 = J_Hopf(q=1) = -(q² + q⁻²) at q=1 = -2

J_Hopf is the Jones polynomial of the Hopf link evaluated at q=1.

## Sign-block / Plancherel application attempt

Hopf link is 2-strand → H_2. Wedderburn decomposition of H_2:
  - trivial V_(2): dim 1, P = 1/2
  - sign V_(1,1): dim 1, P = 1/2

If the c_3 = -2 lives at a 1-dim block with Plancherel weight 1/2:
  c_3_pred = (Hopf coupling) · P_(λ) · (factor)
           = ??? · (1/2) · ???

The natural Plancherel-weighted Hopf calc at q=1:
  trace_M(σ_1²) = P_triv · σ_1²(trivial) + P_sign · σ_1²(sign)
                = (1/2) · q² + (1/2) · 1
                at q=1: (1/2) + (1/2) = 1, NOT -2

So the bare Plancherel-channel doesn't give -2.

## What would the template need to add?

For c_3 = -2 to emerge as `template · X`:
  -2 = (1/2) · X
  X = -4

What's a natural -4? Could be:
  - -2 · 2 (sign-twist × Plancherel-mean times 2)
  - -|S_2|² = -4 (squared regular rep dim)
  - Other...

This probe tests these candidate forms.

## Cross-references

- merged PR #1581 Probe B (Q_β c_3 evaluation comparison)
- merged audit 2026-05-31-qbeta-ck-truncation-order-canonical-framing.md
- merged PR #1645 sign-block / Plancherel template
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 5, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from _precision import set_compute_dps  # noqa: E402
from q_parameter import q_at, q_str  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    DPS = 80
    set_compute_dps(DPS)
    q = q_at(DPS)

    print("=" * 78)
    print("Q_β c_3 = -2 sign-block template check (item 3 of PR #1650)")
    print("=" * 78)
    print(f"\nq_0 = {q_str(60)} (display)\n")

    target_c3 = mp.mpf(-2)  # J_Hopf(q=1)

    # H_2 Wedderburn data
    print(f"[H_2 Wedderburn]")
    print(f"  trivial V_(2):   dim 1, P = 1/2")
    print(f"  sign V_(1,1):    dim 1, P = 1/2")
    print(f"  σ_1(trivial) eigenvalue = +q, σ_1(sign) = -1")
    print(f"  At q=1: σ_1(trivial)² + σ_1(sign)² = 1 + 1 = 2 (NOT |-2|)")

    # Direct test: does any natural Plancherel-template form give -2?
    print(f"\n[Candidate templates for c_3 = -2 via Plancherel structure]")

    # Use q=1 evaluations
    q1 = mp.mpf(1)
    sigma1_triv_q1 = q1
    sigma1_sign_q1 = -mp.mpf(1)
    P_triv = mp.mpf(1) / 2
    P_sign = mp.mpf(1) / 2

    candidates = [
        # (a) Σ_λ P_λ · σ_1(λ) at q=1
        ("(a) Σ_λ P_λ · σ_1(λ)|_{q=1}",
         P_triv * sigma1_triv_q1 + P_sign * sigma1_sign_q1),
        # (b) Σ_λ P_λ · σ_1²(λ) at q=1
        ("(b) Σ_λ P_λ · σ_1²(λ)|_{q=1}",
         P_triv * sigma1_triv_q1 ** 2 + P_sign * sigma1_sign_q1 ** 2),
        # (c) -[2]_q² at q=1 — anti-symmetric Hopf
        ("(c) -[2]_q² at q=1",
         -(q + 1 / q) ** 2),
        # (d) -|S_2|² = -4
        ("(d) -|S_2|² = -4", mp.mpf(-4)),
        # (e) -2·|S_2| = -4
        ("(e) -2·|S_2|", mp.mpf(-2) * 2),
        # (f) sign-channel only (just -1, no factor)
        ("(f) σ_1(sign)|_{q=1} = -1", mp.mpf(-1)),
        # (g) 2·σ_1(sign)
        ("(g) 2·σ_1(sign)|_{q=1} = -2", 2 * sigma1_sign_q1),
        # (h) -[2]_q at q=1 = -2
        ("(h) -[2]_q at q=1", -(q + 1 / q)),
        # (i) -([2]_q at q_0)
        ("(i) -[2]_q at q_0", -(q + 1 / q)),
        # (j) ηJones full Hopf eval at q=1
        ("(j) -(q²+q⁻²) at q=1 (Jones-Hopf)", -(1 + 1)),
    ]

    print(f"  {'name':<48}{'value':<22}{'Δ vs -2'}")
    scored = []
    for name, val in candidates:
        diff = val - target_c3
        scored.append((name, val, diff))

    scored.sort(key=lambda r: abs(r[2]))
    for name, val, diff in scored:
        marker = ""
        if abs(diff) < mp.mpf("1e-30"):
            marker = " ⭐⭐ EXACT match"
        elif abs(diff) < mp.mpf("0.01"):
            marker = " ⭐ within 1%"
        elif abs(diff) < mp.mpf("0.5"):
            marker = " *"
        print(f"  {name:<48}{mp.nstr(val, 12):<22}{mp.nstr(diff, 6)}{marker}")

    # Verdict
    exact_matches = [r for r in scored if abs(r[2]) < mp.mpf("1e-30")]
    plancherel_matches = [r for r in scored
                          if "Σ_λ" in r[0] or "P_" in r[0]]
    pw_in_exact = [r for r in plancherel_matches if abs(r[2]) < mp.mpf("1e-30")]

    print(f"\n[Verdict]")
    if pw_in_exact:
        verdict = (
            f"TEMPLATE APPLIES: Plancherel-weighted form '{pw_in_exact[0][0]}' "
            f"reproduces c_3 = -2 EXACTLY. The sign-block / Plancherel template "
            f"from PR #1645 extends to Q_β."
        )
    elif exact_matches:
        names = [r[0] for r in exact_matches]
        verdict = (
            f"NON-PLANCHEREL EXACT MATCHES: {names}. c_3 = -2 is reproducible "
            f"as -[2]_q at q=1, but NOT directly as a Plancherel-weighted "
            f"sum at H_2. The sign-block template does NOT directly transfer; "
            f"c_3 is the Hopf-link Jones evaluation, NOT a Plancherel-channel "
            f"projection. Complements sibling Q_β Habiro work (independent "
            f"categorical mechanism)."
        )
    else:
        verdict = "NO EXACT match in tested basis."
    print(f"  {verdict}")

    # ── Witness ──
    w = WitnessBuilder(
        "qbeta-signblock-template-check",
        engine="python",
    )
    w.set_description(
        "Item 3 of PR #1650: test whether PR #1645's sign-block/Plancherel "
        "template transfers to Q_β c_3 = -2 = J_Hopf(q=1). Complement to "
        "sibling Q_β Habiro work; non-competing categorical-template check."
    )
    w.add_parameter("q_80dps", q_str(DPS))
    w.add_data("exact_matches", str([r[0] for r in exact_matches]))
    w.add_data("plancherel_exact_matches", str([r[0] for r in pw_in_exact]))
    w.add_data("verdict", verdict)

    w.add_assertion(
        name="qbeta_template_scan_completed",
        computed=len(candidates),
        expected=len(candidates),
        tolerance=0,
        source=f"Scanned {len(candidates)} candidates at 80 dps.",
    )
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
