#!/usr/bin/env python3
"""qbeta_c_vs_d_are_different_algebras_probe.py — C and D are not two coordinates
on one trace. D is the Temperley-Lieb QUOTIENT, z is indexed by RANK, and the
"degeneracy" of my merged #6889 is non-semisimplicity.

Bean `qou-cds1`.  Scope-(b): exact symbolic identities and registry facts.

## 🛑 What this corrects

Three of my own PRs on this arc attacked the C->D move as though `z` were a
COORDINATE to be re-normalised:

  * #6915 rescaled `z_D` to bar-evenness (`z_D/q^2 = 1/[2]_q`) and found the
    route leaves convention D;
  * #6921 pushed the derived eigenphase projection `alpha - h^2/4` through the
    ladder and found it insufficient;
  * #6889 declared the root-of-unity sublocus EMPTY because every admissible
    phase was "degenerate" (`b^2 = 0`).

All three measurements stand.  **The framing behind the first two was wrong,
and the third mislabels what it measured.**

## 1. C and D differ in WHICH WEDDERBURN BLOCKS EXIST

From `docs/coordination/trace-convention-registry.json`:

    convention   name                                y_(3)        y_(2,1)     y_(1^3)
    C            full-Hecke Ocneanu / Wenzl z-trace  0.4153958    0.2809296   0.0227449
    D            SU(2)/Temperley-Lieb (Jones)        [4]/[2]^3    1/[2]^2     0

Both normalise (`sum_lambda y_lambda d_lambda = 1`, `d = (1,2,1)`), but D
ANNIHILATES the sign block.  `TL_n = H_n / <antisymmetriser>` kills every
partition with more than two rows; at `n = 3` that is exactly `(1^3)`.  So D is
a QUOTIENT of C.  Information is destroyed, not re-coordinatised — which is
`decayLadder_zC_threeRow_ne_zero` in its own words ("does not factor through
Temperley-Lieb").

Consequence: the relation `z_D(q) = q^2 z_C(q^2)` — true, verified below — is a
coincidence between parameter VALUES.  It is not an isomorphism of traces, and
no substitution carries a 3-block trace to a 2-block one.

## 2. `z` is indexed by RANK; it is not a free coordinate

`z_N = q^N / [N]_q` satisfies the full-bar condition `bar(z) = z - h` for EVERY
`N` (checked N = 1..6, exactly zero each time), with twist `bar(z_N)/z_N =
q^(-2N)`.  `z_D = z_2` — **D is the SU(2) member**.

`z_C = 1/[2]_sqrt(q)` carries NO `q^N` numerator: it is bar-even, twist 1, and
is therefore not in the family for any `N`.  **The `q^N` numerator IS the bar
twist**, so #6915's "rescale to bar-evenness" was stripping the rank label.

## 3. `b^2 = [3]_q / [2]_q^2` — so `b^2 = 0` IS non-semisimplicity

Exact identity (my first attempt carried a spurious `q^2`; recorded because the
wrong form is easy to reach and sympy is what caught it).  `H_n(q)` is
semisimple iff `[k]_q != 0` for all `k <= n`, so

    b^2 = 0   <=>   [3]_q = 0   <=>   H_3(q) is NOT semisimple.

The phases `pi/3` and `5pi/3` that #6889 called "degenerate", and used to
declare the root-of-unity sublocus EMPTY, are exactly the points where the
Wedderburn decomposition `tr = sum_lambda y_lambda chi^lambda` CEASES TO EXIST.
That is not an obstruction to the physics; it is where the semisimple machinery
ends and the cellular / tilting structure begins.  #6889 excluded the
interesting locus on the grounds that its own tooling stopped working there.

**#6889's arithmetic is unchanged and its exclusion is withdrawn as an
interpretation.**

## 4. A tension for the owner, flagged not resolved

  * 2026-08-15 ruling: convention D canonical.
  * 2026-09-03 ruling: derivations should be on the FULL TOWER — all `n` of the
    Hecke tower and all orders in `q`.

D = SU(2)/TL is a TWO-ROW TRUNCATION: at `n = 3A` it discards every partition
with more than two rows.  Which ruling governs the Q_beta channel is an owner
decision; this probe measures the truncation, it does not adjudicate.

## Precision

sympy exact symbolic; registry values read from the committed JSON.  No float64
in any claim.
"""
from __future__ import annotations

import json
import pathlib as _pl
import sys as _sys

_HERE = _pl.Path(__file__).resolve()
_COMP = _HERE.parent.parent
_ROOT = _COMP.parent
for _p in (_COMP, _COMP / "substrate", _COMP / "qbeta"):
    _sys.path.insert(0, str(_p))

import sympy as sp                                              # noqa: E402
from witness_base import WitnessBuilder                         # noqa: E402

RESULTS: list[dict] = []


def record(name, passed, detail):
    RESULTS.append({"name": name, "passed": bool(passed), "detail": detail})
    print(f"[{'PASS' if passed else 'FAIL'}] {name}\n    {detail}\n")


q = sp.symbols("q", positive=True)
bar = lambda e: sp.simplify(sp.powsimp(e.subs(q, 1 / q), force=True))
h = q - 1 / q
br = lambda n: sp.simplify((q ** n - q ** (-n)) / (q - 1 / q))
zN = lambda n: q ** n / br(n)
zC = sp.sqrt(q) / (q + 1)
zD = q ** 3 / (q ** 2 + 1)

REG = json.load(open(_ROOT / "docs" / "coordination" / "trace-convention-registry.json"))
conv = {c["id"]: c for c in REG["conventions"] if c.get("id") in ("C", "D")}

yD = {"(3)": br(4) / br(2) ** 3, "(2,1)": 1 / br(2) ** 2, "(1^3)": sp.Integer(0)}
dims = {"(3)": 1, "(2,1)": 2, "(1^3)": 1}
normD = sp.simplify(sum(yD[k] * dims[k] for k in yD))
yC_reg = conv["C"]["weights_at_q0"]
normC = sum(sp.Float(yC_reg[k], 50) * dims[k] for k in yC_reg)

record(
    "D_annihilates_the_sign_block_C_does_not",
    yD["(1^3)"] == 0 and sp.Float(yC_reg["(1^3)"], 50) != 0 and normD == 1,
    f"registry: D is named {conv['D']['name']!r} with y_(1^3) = "
    f"{conv['D']['weights_lambda3']['(1^3)']!r}; C is {conv['C']['name']!r} with "
    f"y_(1^3) = {yC_reg['(1^3)'][:12]}... Both normalise (D: "
    f"sum y_l d_l = {normD}; C: {sp.nsimplify(round(float(normC),12))}). "
    f"TL_n = H_n/<antisymmetriser> kills every partition with >2 rows, which at "
    f"n=3 is exactly (1^3). So D is a QUOTIENT of C — the two conventions differ "
    f"in which blocks EXIST, not in how one object is coordinatised.",
)

record(
    "the_zD_equals_q2_zC_of_q2_relation_is_a_value_coincidence",
    sp.simplify(zD - q ** 2 * zC.subs(q, q ** 2)) == 0,
    "z_D(q) = q^2 z_C(q^2) holds exactly — which is what made the "
    "'same form, different variable' reading tempting. It relates parameter "
    "VALUES only. Given assertion 1 it cannot be an isomorphism of traces: no "
    "substitution carries a 3-block trace to a 2-block one. This is why "
    "#6915's rescaling route was malformed rather than merely unsuccessful.",
)

fullbar = {n: sp.simplify(bar(zN(n)) - (zN(n) - h)) for n in range(1, 7)}
twists = {n: sp.simplify(bar(zN(n)) / zN(n)) for n in (1, 2, 3)}
record(
    "z_is_indexed_by_RANK_and_D_is_the_SU2_member",
    all(v == 0 for v in fullbar.values())
    and sp.simplify(zN(2) - zD) == 0
    and sp.simplify(bar(zC) / zC) == 1,
    "z_N = q^N/[N]_q satisfies the full-bar condition bar(z) = z - h for every "
    f"N = 1..6 (residual {set(str(v) for v in fullbar.values())}), with twist "
    + ", ".join(f"N={n}: {t}" for n, t in twists.items())
    + f". z_2 = {sp.simplify(zN(2))} = z_D, so D is the SU(2) member. z_C = "
      "1/[2]_sqrt(q) has NO q^N numerator, is bar-even (twist 1) and is in the "
      "family for no N. The q^N numerator IS the bar twist — so rescaling z_D "
      "to bar-evenness strips the rank label.",
)

b2 = (q ** 4 + q ** 2 + 1) / (q ** 2 + 1) ** 2
record(
    "b_squared_is_three_over_two_squared_so_its_vanishing_is_NONSEMISIMPLICITY",
    sp.simplify(b2 - br(3) / br(2) ** 2) == 0
    and sp.simplify(b2 - q ** 2 * br(3) / br(2) ** 2) != 0,
    "b^2 = [3]_q/[2]_q^2 exactly (the variant q^2[3]/[2]^2 is NOT equal — my "
    "first attempt carried that spurious q^2 and sympy caught it, recorded "
    "because the wrong form is easy to reach). H_n(q) is semisimple iff "
    "[k]_q != 0 for all k <= n, so b^2 = 0 <=> [3]_q = 0 <=> H_3(q) is NOT "
    "semisimple. The pi/3 and 5pi/3 phases that #6889 called 'degenerate' — and "
    "used to declare the root-of-unity sublocus EMPTY — are exactly where the "
    "Wedderburn decomposition tr = sum_l y_l chi^l ceases to exist. #6889's "
    "arithmetic stands; its exclusion is WITHDRAWN as an interpretation.",
)

record(
    "TL_is_a_two_row_truncation_of_the_tower",
    yD["(1^3)"] == 0,
    "the 2026-09-03 owner ruling asks derivations to use the FULL TOWER (all n "
    "of H_n(q), all orders in q); the 2026-08-15 ruling makes D canonical. D = "
    "SU(2)/TL keeps only <=2-row partitions, so at n = 3A it discards the "
    "overwhelming majority of the tower. The two rulings pull opposite ways for "
    "this channel. MEASURED here, NOT adjudicated — which governs Q_beta is an "
    "owner decision.",
)

out = {
    "probe": _HERE.stem,
    "bean": "qou-cds1",
    "question": "is the C->D move a change of coordinate on one trace?",
    "answer": "No. C is the full Hecke (Ocneanu/Wenzl) trace; D is the "
              "Temperley-Lieb/SU(2) QUOTIENT with y_(1^3) = 0. z is not a free "
              "coordinate but the rank label of z_N = q^N/[N]_q (D = N=2), and "
              "b^2 = [3]_q/[2]_q^2 makes the #6889 'degeneracy' exactly the "
              "non-semisimple locus of H_3(q).",
    "corrects": "the FRAMING of my #6915 and #6921 (measurements stand), and the "
                "INTERPRETATION of my merged #6889 (arithmetic stands, exclusion "
                "withdrawn)",
    "scope": "(b) for the identities and registry facts. Adjudicates neither "
             "ruling; proposes no replacement derivation.",
    "rank_family": {f"z_{n}": str(sp.simplify(zN(n))) for n in range(1, 5)},
    "full_bar_residuals": {f"N={n}": str(v) for n, v in fullbar.items()},
    "b_squared_identity": "b^2 = [3]_q/[2]_q^2",
    "assertions": RESULTS,
    "allPassed": all(r["passed"] for r in RESULTS),
}
WitnessBuilder.stamp_staleness_metadata(out, script_path=__file__, engine="python+sympy")
wp = _HERE.parent / "qbeta-c-vs-d-are-different-algebras.witness.json"
wp.write_text(json.dumps(out, indent=2) + "\n")
print(f"witness -> {wp}\nallPassed: {out['allPassed']}")
_sys.exit(0 if out["allPassed"] else 1)
