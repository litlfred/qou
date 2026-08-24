#!/usr/bin/env python3
"""
d_frame_cyclotomic_exponent_probe.py — the D-frame cyclotomic exponent is
`3A - 1` minus two per neutron, and the `3Z + N - 1` form is a rewriting, not
a count.

WHAT THIS SETTLES.  `qou-cxon` Q2.  The convention-C law gives the exponent of
`(1 + u^2)` as `3A - 1`, derived in `d_u_closed_form_proof.py` as
`n_strands - 1` with `n_strands = 3A`.  The measured convention-D exponent of
`(q^2 + 1)` is `3Z + N - 1`.  The two agree only at `N = 0`, which looked like
a structural contradiction: the number of `z` factors is a property of the
braid word and the Markov recursion, so it cannot depend on what `z` equals.

It is not a contradiction.  Measured here:

    atom      Z N A | m = deg_z  3A-1 | naive actual cancelled  2N
    proton    1 0 1 |         2     2 |     2      2         0   0
    D         1 1 2 |         5     5 |     5      3         2   2
    T         1 2 3 |         8     8 |     8      4         4   4
    3He       2 1 3 |         8     8 |     8      6         2   2

1. **The z-count really is `3A - 1`**, in both frames.  Substituting a FREE
   SYMBOL for `hecke_symbolic.z_markov` makes `tr_M_atomic` polynomial in that
   symbol; its degree is the z-count, and it is convention-independent by
   construction.  The C derivation's counting is correct.
2. Substituting `z_D = q^3/(q^2 + 1)` into a degree-`m` polynomial gives
   `(q^2 + 1)^m` naively -- but exactly **2N** factors **cancel against the
   numerator**, leaving `m - 2N = 3A - 1 - 2N = 3Z + N - 1`.
3. The proton (`N = 0`) is the control: zero cancellation, exponent `= m`.

**So `3Z + N` is NOT a strand count and NOT a peel count.**  The temptation is
to read it as "three strands per proton, one per neutron", which is not a
plausible braid word -- and it is wrong.  The exponent is `3A - 1` reduced by
two per neutron, and `3Z + N - 1` is arithmetic rewriting of that.

**This supersedes the cyclotomic-aliasing hypothesis** recorded in
`docs/audits/2026-08-24-d-frame-prefactor-localised-to-the-interface.md`,
which guessed that each frame's exponent mixed the z-count with additional
sources of its own cyclotomic (`[2]_q` supplying `Phi_8`, `[2]_sqrt(q)`
supplying `Phi_4`).  That guess was flagged as a hypothesis and is now
**refuted**: the mechanism is cancellation in the numerator, not extra
sources.

## The round-trip gate, and why it is an assertion rather than a comment

The free-symbol substitution is only sound if putting `z_D` back reproduces
the unpatched function EXACTLY.  A first attempt at this measurement used
`sp.Symbol("q")` while `hecke_symbolic` uses `sp.Symbol('q', positive=True)`
-- different objects.  The round-trip then built a two-`q` expression, and
every degree read off it was meaningless: it reported the deuteron denominator
as `192*q**25*(q**2+1)**5` against the true `192*q**23*(q**2+1)**3`, and
reported the cancellation as zero.  The z-count it printed happened to be
right, which is worse than being wrong -- a coincidence that would have been
recorded as evidence.

So this probe binds `q = hecke_symbolic.q` and asserts
`round_trip_reproduces_unpatched` FIRST.  If that assertion fails no degree is
reported at all.

Exact symbols throughout; no float is formed anywhere; no anchor enters
(`tr_M_atomic` is exact in symbolic `q`).

Output: `d-frame-cyclotomic-exponent.witness.json`.
"""
from __future__ import annotations

import json
import pathlib
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
for _p in ("computations", "computations/markov", "computations/hecke",
           "computations/substrate"):
    sys.path.insert(0, str(REPO / _p))

import sympy as sp  # noqa: E402
import hecke_symbolic as hs  # noqa: E402

q = hs.q                      # the MODULE's symbol -- see the round-trip note
PHI_D = q ** 2 + 1
Z_D = q ** 3 / PHI_D
ZSYM = sp.Symbol("Zsym")

ATOMS = [("proton", 1, 0), ("D", 1, 1), ("T", 1, 2), ("3He", 2, 1)]


def main() -> int:
    import markov_peel as mkp
    ref = sp.cancel(sp.together(sp.sympify(
        mkp.tr_M_atomic(1, 1, use_fast=False))))

    # patch AFTER computing the reference, then re-import the consumers
    for _m in ("markov_peel", "hecke_symbolic", "markov_trace_canonical",
               "hecke_laurent_fast"):
        sys.modules.pop(_m, None)
    import hecke_symbolic as hs2
    assert hs2.q == q, "module symbol changed across reload"
    hs2.z_markov = ZSYM
    import markov_peel as mkp2

    back = sp.cancel(sp.together(
        sp.sympify(mkp2.tr_M_atomic(1, 1, use_fast=False)).subs(ZSYM, Z_D)))
    round_trip_ok = bool(sp.simplify(sp.cancel(back - ref)) == 0)
    print(f"round-trip reproduces unpatched: {round_trip_ok}", flush=True)

    rows = []
    if round_trip_ok:
        print(f"{'atom':8s} {'Z':>2s}{'N':>2s}{'A':>2s} | {'m=deg_z':>7s} "
              f"{'3A-1':>5s} | {'naive':>5s} {'actual':>6s} "
              f"{'cancelled':>9s} {'2N':>3s}")
        for label, Z, N in ATOMS:
            t0 = time.time()
            A = Z + N
            e = sp.sympify(mkp2.tr_M_atomic(Z, N, use_fast=False))
            n0, d0 = sp.fraction(sp.cancel(sp.together(e)))
            m = max(sp.Poly(sp.expand(x), ZSYM).degree() if x.has(ZSYM) else 0
                    for x in (n0, d0))
            sub = sp.cancel(sp.together(e.subs(ZSYM, Z_D)))
            actual = sum(
                ex for b, ex in sp.factor_list(
                    sp.expand(sp.fraction(sub)[1]))[1]
                if sp.expand(b) == PHI_D)
            rows.append({
                "atom": label, "Z": Z, "N": N, "A": A,
                "z_count_m": int(m),
                "c_law_3A_minus_1": int(3 * A - 1),
                "naive_phi_power": int(m),
                "actual_phi_power": int(actual),
                "cancelled": int(m - actual),
                "two_N": int(2 * N),
                "m_equals_3A_minus_1": bool(m == 3 * A - 1),
                "actual_equals_3Z_plus_N_minus_1": bool(
                    actual == 3 * Z + N - 1),
                "cancelled_equals_2N": bool(m - actual == 2 * N),
                "elapsed_sec": f"{time.time() - t0:.2f}",
            })
            print(f"{label:8s} {Z:2d}{N:2d}{A:2d} | {m:7d} {3*A-1:5d} | "
                  f"{m:5d} {actual:6d} {m-actual:9d} {2*N:3d}   "
                  f"[{time.time() - t0:.1f}s]", flush=True)

    assertions = [
        {"name": "round_trip_reproduces_unpatched",
         "passed": round_trip_ok,
         "note": "GATE: substituting z_D back into the free-symbol expression "
                 "must reproduce tr_M_atomic exactly. A first attempt used a "
                 "bare sp.Symbol('q') against the module's "
                 "sp.Symbol('q', positive=True) and silently measured a "
                 "two-q expression. No degree is reported unless this holds."},
        {"name": "z_count_is_3A_minus_1",
         "passed": bool(rows) and all(r["m_equals_3A_minus_1"] for r in rows),
         "note": "convention-independent by construction (degree in a free "
                 "symbol); confirms the C derivation's n_strands - 1 count"},
        {"name": "d_frame_exponent_is_3Z_plus_N_minus_1",
         "passed": bool(rows) and all(
             r["actual_equals_3Z_plus_N_minus_1"] for r in rows)},
        {"name": "cancellation_is_two_per_neutron",
         "passed": bool(rows) and all(r["cancelled_equals_2N"] for r in rows),
         "note": "the whole of the C-vs-D exponent gap; proton (N=0) is the "
                 "zero-cancellation control"},
    ]

    witness = {
        "computation": "d-frame-cyclotomic-exponent",
        "description": (
            "The convention-D cyclotomic exponent is 3A-1 minus two per "
            "neutron. Substituting a free symbol for hecke_symbolic.z_markov "
            "shows the z-count is 3A-1 in both frames -- convention "
            "independent by construction, and exactly what the convention-C "
            "derivation counts. Substituting z_D = q^3/(q^2+1) then gives "
            "(q^2+1)^(3A-1) naively, of which exactly 2N factors CANCEL "
            "against the numerator, leaving 3A-1-2N = 3Z+N-1. So 3Z+N is "
            "NOT a strand count and NOT a peel count; it is arithmetic "
            "rewriting. This REFUTES the cyclotomic-aliasing hypothesis "
            "recorded in the 2026-08-24 prefactor audit, which guessed at "
            "extra per-frame sources; the mechanism is cancellation. The "
            "round-trip validity gate is asserted first because a first "
            "attempt at this measurement used a mismatched q symbol and "
            "produced a coincidentally-correct z-count from a meaningless "
            "expression. Scope-(a): these four configurations under "
            "bring_color_weighted."
        ),
        "convention": {
            "markov_z": "q**3/(q**2 + 1)   (convention D, canonical per R1)",
            "pn_convention": "bring_color_weighted (canonical per R3)",
            "anchor": (
                "NONE enters the computation: tr_M_atomic is exact in "
                "symbolic q and every number here is a polynomial degree or "
                "a factor multiplicity. The top-level q0Anchor/q0Value are "
                "the ambient WitnessBuilder stamp -- which pin this process "
                "ran under, not an input to any value below."
            ),
        },
        "reference_blocks": ["def:markov-trace",
                             "prop:atomic-braid-decomposition"],
        "atoms": rows,
        "assertions": assertions,
    }
    witness["allPassed"] = all(a["passed"] for a in assertions)

    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(
        witness, script_path=__file__, engine="sympy")
    out = REPO / "computations" / "d-frame-cyclotomic-exponent.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\n  allPassed = {witness['allPassed']}   "
          f"-> {out.relative_to(REPO)}")
    return 0 if witness["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
