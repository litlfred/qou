#!/usr/bin/env python3
"""qbeta_habiro_pochhammer_convention_probe.py — the Lean qPochhammer in
`habiro-precision-ladder-equivalence` was the WRONG Pochhammer for the
expansion it formalizes: 507 % off, and the .md carried the same error.

Bean `qou-cds1`.  Scope-(b) for the discrepancy (an exact arithmetic
mismatch against a stored witness, not a modelling judgement); scope-(a) for
the claim that `(1-u^k)` is the intended convention.

## What was wrong

`prop:habiro-precision-ladder-equivalence` formalizes

    tr_M = sum_{m=0}^{M} a_m(u) * (u;u)_m ,   u = q^{1/2}

Its Lean defined

    qPochhammer u (m+1) = qPochhammer u m * (1 - u^(2*(m+1)))       <- (u^2;u^2)_m

and its .md said `(u;u)_m = prod (1-u^{2k})`.  At `u = sqrt(q)` that product is
`(q;q)_m`, which is a DIFFERENT object from `(u;u)_m` and — decisively — a
different object from the one the corpus's stored coefficients are computed
against.  `habiro-coefficients-atomic.witness.json` states its own convention
in its `description`:

    "tr_M(T_w, q) = sum_m a_m * (check_q;check_q)_m  (check_q = q^{1/2})"

i.e. `prod (1 - u^k)` at `u = sqrt(q)`.

## Measured, at 60 dps against the stored a_m

                              proton tr_M            rel. error
    witness tr_M_at_q0        1.145759692457300816   --
    (1-u^k)   [correct]       1.145759692457300870   4.65e-17
    (1-u^2k)  [was in Lean]   6.960179408595493080   5.07   (507 %)

and for the neutron 0.987743688115809531 vs 4.564900350080829572 (362 %).

## It was also a notation error on its own terms

`(u;u)_m` DENOTES `prod (1-u^k)`.  The product `prod (1-u^{2k})` is
`(u^2;u^2)_m`.  So the definition disagreed with the name it was given,
independently of which expansion one wants — the same name-vs-body class as the
`markovZ` / `markovZC` / `markovZc` defects (#5972, #6015).

## The odd one out among three same-named definitions

Three `QOU.BraidKnot.qPochhammer` definitions live in `mass-theory/`:

    habiro-expansion-atomic.lean         (1 - u^(m+1))     <- (u;u)_m
    full-pole-structure-mass-trace.lean  (1 - q^(k+1))     <- (q;q)_m
    habiro-precision-ladder-equivalence  (1 - u^(2(m+1)))  <- THE ODD ONE OUT

Two of three already used `(1-u^k)`; only the equivalence file disagreed, and it
is the one whose .md quotes the atomic expansion whose coefficients the witness
stores.

## Blast radius of the fix: zero external consumers

`qPochhammer` in that file is used only by `HabiroExpansion.eval` in the SAME
file (line 61), and NO other Lean file imports the module.  So the correction
cannot move any other declaration.  Verified `lean`-direct with the lakefile's
own flags (`-DautoImplicit=false -s 65536`): exit 0, 0 errors.

## What this does NOT claim

It does not claim any published number was wrong.  The compute layer
(`habiro_exact_qbeta.py`, and the witness producer) already used `(1-u^k)`; the
defect was confined to the Lean + .md statement of the proposition, which had no
consumers.  So this is a FORMALIZATION-vs-COMPUTE divergence, corrected on the
formalization side.

## A separate live defect, reported not fixed here

`computations/habiro/habiro_exact_qbeta.py::eval_a_m_at_u` does `u = float(u_val)`
— float64 — while a comment 25 lines below in the same file says "NOT float() —
would silently truncate the 50-dps u_val to ~17 digits".  That producer emits
`habiro-exact-qbeta.witness.json`.  Left for its own change so this one stays
reviewable; recorded in bean `qou-cds1`.

## Precision

mpmath at 60 dps; the `a_m` and denominators evaluated through sympy exact
rationals, NOT through the producer's float64 path.  No `float(` outside
display, no `statistics`, no `math.`.
"""
from __future__ import annotations

import json
import pathlib as _pl
import sys as _sys

_HERE = _pl.Path(__file__).resolve()
_COMP = _HERE.parent.parent
for _p in (_COMP, _COMP / "substrate", _COMP / "qbeta"):
    _sys.path.insert(0, str(_p))

import mpmath as mpm                                            # noqa: E402
import sympy as sp                                              # noqa: E402
from mpmath import mp                                           # noqa: E402

from q_parameter import q_at                                    # noqa: E402
from witness_base import WitnessBuilder                          # noqa: E402

mp.dps = 60
RESULTS: list[dict] = []


def record(name: str, passed: bool, detail: str) -> None:
    RESULTS.append({"name": name, "passed": bool(passed), "detail": detail})
    print(f"[{'PASS' if passed else 'FAIL'}] {name}\n    {detail}\n")


q0 = q_at(60)
u0 = mpm.sqrt(q0)
WP = _COMP / "habiro" / "habiro-coefficients-atomic.witness.json"
W = json.load(open(WP))

u = sp.symbols("u")


def _ev(expr_str):
    e = sp.sympify(str(expr_str).replace("check_q", "u"))
    return mp.mpf(str(sp.N(e.subs(u, sp.Float(str(u0), 60)), 60)))


def reconstruct(d, exponent):
    total = mp.mpf(0)
    for c in d["habiro_coefficients"]:
        p = mp.mpf(1)
        for k in range(1, c["m"] + 1):
            p *= (1 - u0 ** (exponent * k))
        total += _ev(c["a_m"]) * p
    return total / _ev(d["denom_in_u"])


table = {}
ok_correct, ok_wrong = True, True
for atom in ("p (proton, A=1)", "n (neutron, A=1)"):
    d = W["results"][atom]
    tgt = mp.mpf(d["tr_M_at_q0"])
    a, b = reconstruct(d, 1), reconstruct(d, 2)
    ra, rb = abs(a - tgt) / abs(tgt), abs(b - tgt) / abs(tgt)
    table[atom] = {
        "witness_tr_M_at_q0": mpm.nstr(tgt, 22),
        "pochhammer_1_minus_u_k": mpm.nstr(a, 22),
        "rel_err_1_minus_u_k": mpm.nstr(ra, 4),
        "pochhammer_1_minus_u_2k": mpm.nstr(b, 22),
        "rel_err_1_minus_u_2k": mpm.nstr(rb, 4),
    }
    ok_correct &= ra < mp.mpf(10) ** (-15)
    ok_wrong &= rb > mp.mpf(1)

record(
    "witness_declares_the_1_minus_u_k_convention",
    "check_q;check_q" in W["description"] and "q^{1/2}" in W["description"],
    "habiro-coefficients-atomic.witness.json description: "
    f"{W['description'][:120]!r} — i.e. the expansion is against "
    "(check_q;check_q)_m with check_q = q^{1/2}, which is prod(1-u^k) at "
    "u = sqrt(q). The convention is stated by the data itself, not inferred.",
)

record(
    "1_minus_u_k_reproduces_the_stored_trM",
    ok_correct,
    "; ".join(f"{k}: {v['rel_err_1_minus_u_k']}" for k, v in table.items())
    + " — both atoms reconstruct to better than 1e-15 at 60 dps, evaluating "
    "the a_m through sympy exact rationals rather than the producer's float64 "
    "path.",
)

record(
    "1_minus_u_2k_is_off_by_hundreds_of_percent",
    ok_wrong,
    "; ".join(f"{k}: rel {v['rel_err_1_minus_u_2k']} "
              f"({v['pochhammer_1_minus_u_2k']} vs {v['witness_tr_M_at_q0']})"
              for k, v in table.items())
    + " — this is what the Lean definition and the .md both specified. Not a "
    "rounding question: 507 % and 362 %.",
)

record(
    "it_was_also_a_notation_error_independently",
    True,
    "(u;u)_m DENOTES prod(1-u^k); prod(1-u^{2k}) is (u^2;u^2)_m. So the "
    "definition disagreed with the name it was given whichever expansion one "
    "wants — the same name-vs-body class as markovZ / markovZC / markovZc "
    "(#5972, #6015). Two of the three QOU.BraidKnot.qPochhammer definitions in "
    "mass-theory/ (habiro-expansion-atomic, full-pole-structure-mass-trace) "
    "already used (1-u^k); the equivalence file was the only one that did not.",
)

out = {
    "probe": _HERE.stem,
    "bean": "qou-cds1",
    "question": "does the Lean qPochhammer in habiro-precision-ladder-equivalence "
                "match the expansion it formalizes?",
    "answer": "No. It used prod(1-u^{2k}) = (u^2;u^2)_m where the corpus's stored "
              "Habiro coefficients are computed against (u;u)_m = prod(1-u^k) at "
              "u = sqrt(q). Reconstructing tr_M with the Lean's convention gives "
              "6.9602 instead of 1.1458 (507 %). Corrected in the Lean and the .md.",
    "scope": "(b) for the discrepancy — an exact arithmetic mismatch against a "
             "stored witness, with the convention declared by the witness itself. "
             "(a) for the fix direction. Confined to the FORMALIZATION: the compute "
             "layer already used (1-u^k), so no published number was wrong, and the "
             "corrected declaration has zero external consumers.",
    "reconstruction": table,
    "lean_verification": "lean -DautoImplicit=false -s 65536 -> exit 0, 0 errors "
                         "(never lake build; restored olean cache intact)",
    "separate_defect_reported_not_fixed": "computations/habiro/habiro_exact_qbeta.py"
        "::eval_a_m_at_u does u = float(u_val) — float64 — contradicting a comment "
        "25 lines below in the same file; it emits habiro-exact-qbeta.witness.json.",
    "q0": mpm.nstr(q0, 20),
    "q0_pin": "proton (q_at)",
    "dps": mp.dps,
    "assertions": RESULTS,
    "allPassed": all(r["passed"] for r in RESULTS),
}
# Stamp provenance through WitnessBuilder rather than a raw json.dump — a bare
# write lands the witness PROV_MISSING (no engine/scriptFile/commitSha), which
# `scripts/check-sidecars.sh` flags as P30.
WitnessBuilder.stamp_staleness_metadata(
    out, script_path=__file__, engine="python+sympy+mpmath",
    # Bare token in q0_anchor, prose in q0_anchor_reason. "physical_proton" is
    # not one of the recognised tokens, so q0_anchor_consistency_audit could not
    # map it to a pin and reported this witness Q0_ANCHOR_UNRECOGNISED — i.e.
    # never checked at all. Surfaced by the helper's own warning while fixing
    # the missing scriptFile on this same witness (bean qou-4383).
    q0_anchor="proton",
    q0_anchor_reason="the physical proton pin",
    q0_value=mpm.nstr(q0, 50),
)
wpath = _HERE.parent / "qbeta-habiro-pochhammer-convention.witness.json"
wpath.write_text(json.dumps(out, indent=2) + "\n")
print(f"witness -> {wpath}")
print(f"allPassed: {out['allPassed']}")
_sys.exit(0 if out["allPassed"] else 1)
