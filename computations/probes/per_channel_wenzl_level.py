#!/usr/bin/env python3
"""Does the COLOUR channel sit at level 3?  (It does not.)

## Read the prior art first -- most of this table is not new

The per-channel level question is ALREADY ANSWERED, more thoroughly, on the
sibling branch `claude/wenzl-level-family-2026-08-16`
(`docs/audits/2026-08-16-wenzl-level-family.md`,
`computations/probes/wenzl_level_family.py`).  Its finding [N5]:

    mass 2 | binding 2 | borromean-binding-single-pipeline 2 |
    qbeta-decay NONE (formal 2.5995 at q0)
    "every channel that is in the family at all is at r = 2.
     No QOU channel sits at r = 3 or above."

and its [N3] is strictly stronger than any numerical solve: `z_C` is not
`z_r` for ANY `r`, identically in q -- a scope-(b) exclusion resting on two
invariants (field membership, `sqrt(q)` not in QQ(q) by Eisenstein at `q`;
and non-constancy of the formal level `r_C(q)`).  Its [N1] proves
`N_eff == Wenzl level` as maps, not merely at `q0`.  Cite that branch for
all of the above.

## What this probe adds

Exactly two rows the sibling's table does not carry, both about COLOUR --
which is the one channel the eightfold/SU(3) question turns on:

  * `bring_color_weighted`, the PRODUCTION colour convention (canonical per
    the 2026-08-15 ruling R3), and
  * the `N = 3` fibre parameter `z_3 = q^3/[3]_q`, which exists in the
    corpus but only as a probe fixture.

Plus a cross-check that the tower reproduces its own integer levels.

## The tower, and why it has two derivations

    z_r = q^r / [r]_q  =  q^(2r-1)(q^2-1)/(q^(2r)-1)

  * FIBRE DIMENSION.  `z * [N]_q = q^N` for a fibre of quantum dimension
    `dim_q V = [N]_q`, proved division-free in
    `QOU/BraidsAndKnots/FibreDimensionForcesTL.lean`, numerical companion
    `computations/ocneanu_param_from_fibre_dimension.py` (bean `qou-n1dj`).
  * WENZL LEVEL.  `wenzl_level_tower_verify.py` (this PR): Wenzl's
    `z_W = Q^r(1-Q)/(1-Q^r)` at `Q = q^2`, `z_W = q*z`, rearranges over
    QQ(q) to exactly `q^r/[r]_q`, symbolically for general `r`.

Same rational function, so **fibre dimension N = Wenzl level r**.  The
sibling reached that identification independently as [N1]; two routes
agreeing is worth recording, but only one of them is new here.

Pin: PROTON (`qou_substrate.constants.Q`).  No cached witness read.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from mpmath import mp

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "tools" / "qou-substrate" / "python"))

mp.dps = 60


def z_tower(r, q):
    r = mp.mpf(r)
    return q**r / ((q**r - q ** (-r)) / (q - 1 / q))


def level_of(z_target, q, guess=2.0):
    return mp.findroot(lambda r: z_tower(r, q) - z_target, mp.mpf(guess))


def main() -> int:
    from qou_substrate.constants import Q_MP as Q_PROTON

    # Q_MP, not mpf(str(Q)): the f64 constant carries ~16 significant digits,

    # so mpf(str(...)) LAUNDERS it — the value looks 50-digit and is accurate

    # to 16. Read the high-precision name instead.

    q = Q_PROTON

    # Each entry: (channel, production site, literal z as run, callable).
    # Sites confirmed by reading the files, not by trusting the registry --
    # the registry is stale on pyhecke.gram (see the note printed below).
    channels = [
        ("mass",
         "m_p_substrate_identity_50dps.py:124 trM_borromean",
         "no z: Lean closed form in h = q-1/q; value is the D value",
         lambda: q**3 / (q**2 + 1)),
        ("binding",
         "closed_form_tau_M.py:165 markov_z",
         "q**3/(q**2+1)",
         lambda: q**3 / (q**2 + 1)),
        ("binding (symbolic twin)",
         "markov/markov_weights_symbolic.py:99 Z_MARK",
         "Q**3/(Q**2+1)",
         lambda: q**3 / (q**2 + 1)),
        ("borromean-binding-single-pipeline",
         "borromean_binding_recompute.py:111",
         "q**3/(q**2+1)",
         lambda: q**3 / (q**2 + 1)),
        ("qbeta-decay",
         "qbeta/qbeta_utils.py:41 markov_parameter",
         "mpsqrt(q)/(1+q)   [= z_C]",
         lambda: mp.sqrt(q) / (1 + q)),
        ("pyhecke.gram (registry says C)",
         "tools/pyhecke/python/pyhecke/gram.py:175",
         "q0**3/(q0**2+1)   [code is D -- registry STALE]",
         lambda: q**3 / (q**2 + 1)),
        ("colour: bring_color_weighted (PRODUCTION)",
         "closed_form_tau_M.py:307 via markov_z + delta bond shift",
         "q**3/(q**2+1) with a p-n bond perturbation, NOT a new z",
         lambda: q**3 / (q**2 + 1)),
        ("colour: N=3 fibre (PROBE FIXTURE ONLY)",
         "ocneanu_param_from_fibre_dimension.py:189 z_3",
         "q**5/(q**4+q**2+1) = q**3/[3]_q",
         lambda: q**5 / (q**4 + q**2 + 1)),
    ]

    print(f"proton pin q0 = {mp.nstr(q, 20)}\n")
    print(f"{'channel':<44} {'z':<22} {'level r':<22} int?")
    print("-" * 100)

    out = []
    for name, site, expr, fn in channels:
        z = fn()
        guess = 2.5 if abs(z - mp.sqrt(q) / (1 + q)) < mp.mpf("1e-30") else 2.0
        r = level_of(z, q, guess)
        is_int = abs(r - mp.nint(r)) < mp.mpf(10) ** -25
        tag = f"INTEGER ({int(mp.nint(r))})" if is_int else "NOT AN INTEGER"
        print(f"{name:<44} {mp.nstr(z, 12):<22} {mp.nstr(r, 18):<22} {tag}")
        out.append({
            "channel": name, "site": site, "z_expression": expr,
            "z_value": mp.nstr(z, 40), "level_r": mp.nstr(r, 30),
            "integer_level": bool(is_int),
            "level_int": int(mp.nint(r)) if is_int else None,
        })

    print()
    print("Sanity: the tower must reproduce its own integer levels.")
    for r in (1, 2, 3, 4):
        back = level_of(z_tower(r, q), q, guess=r)
        print(f"  r = {r} -> z_r -> solved back to {mp.nstr(back, 20)}")

    print()
    print("VERDICT on the eightfold / SU(3) question")
    print("-" * 100)
    print("  The production colour path (bring_color_weighted, canonical per")
    print("  the 2026-08-15 ruling R3) runs z_D, i.e. LEVEL 2 -- the SU(2)/TL")
    print("  fibre.  Colour enters as a delta-perturbation on the p-n bond")
    print("  factor, not as a change of fibre.  The level-3 parameter")
    print("  z_3 = q^3/[3]_q exists in the corpus only as a positive-control")
    print("  fixture (convention-slip-registry.json R3-trace-N3); there is no")
    print("  registered colour channel, no production consumer, no evaluator")
    print("  entry.  So the strong channel does NOT sit at r = 3.")

    payload = {
        "pin": {"name": "proton", "q0": mp.nstr(q, 50),
                "source": "qou_substrate.constants.Q"},
        "tower": "z_r = q^r/[r]_q",
        "derivations": [
            "fibre dimension: QOU/BraidsAndKnots/FibreDimensionForcesTL.lean"
            " (z*[N]_q = q^N); companion ocneanu_param_from_fibre_dimension.py",
            "Wenzl level: wenzl_level_tower_verify.py (z_W = Q^r(1-Q)/(1-Q^r),"
            " Q = q^2, z_W = q*z) -- same rational function, so N = r",
        ],
        "channels": out,
        "eightfold_verdict": (
            "NO. Production colour (bring_color_weighted) runs z_D = level 2."
            " z_3 exists only as a probe fixture with no production consumer."
        ),
    }
    p = Path(__file__).with_name("per-channel-wenzl-level.json")
    p.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"\nwrote {p.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
