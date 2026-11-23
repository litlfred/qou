#!/usr/bin/env python3
"""The normaliser convention is PINNED by the algebra: `delta = [2]_q`, exactly,
at every `q`. The 1.33x family freedom collapses to one member.

`qou-59j5` measured a five-member normaliser family spanning **1.33x** in
MeV/nucleon and observed — correctly — that this is *the same size as the
deficit it would explain*, "which is exactly the condition that makes choosing a
member a fit". `qou-78pt` reverted to "unfalsifiable as written" on that basis,
with the standing verdict: **pinning the convention from the axioms is the actual
work.**

The bond factors already pin it, and by an identity rather than a comparison.

*** THE IDENTITY ***

Two of the three interface letters are PURE crossings — `b_pp` is `sigma` and
`b_nn` is `sigma^-1`. Their product collapses:

    b_pp . b_nn  =  q^3/(q^2+1) . 1/(q^3+q)  =  q^2/(q^2+1)^2  =  1/[2]_q^2

so the GEOMETRIC MEAN of the two pure-crossing bonds is **exactly the inverse
loop value**, and each bond is a `q^(+/-2)` twist of it:

    sqrt(b_pp . b_nn) = 1/[2]_q         b_pp = q^2/[2]_q        b_nn = q^-2/[2]_q

Hence the per-strand coefficient of the additive binding law is exactly the log
of the loop value:

    (L_pp + L_nn)/2  =  ln [2]_q        (L = -ln b)

*** WHY THIS IS A PINNING AND NOT A CHOICE ***

The identity holds **identically in `q`**, and among `qou-59j5`'s family only
`[2]_q` satisfies it. The other three agree with `sqrt(b_pp b_nn) = q/(q^2+1)`
only at `q = 1` — the classical point, where every factor in this arc collapses
to `z = 1/2` anyway:

    [2]_q     = q + 1/q            IDENTICAL
    [2]_Q     = 1 + q^2            agrees only at q = 1
    q^1/2 + q^-1/2  (Kauffman)     agrees only at q = 1
    1 + q^4   (over-shoot control) agrees only at q = 1

A fit would land at `q0` and nowhere else. This holds on the whole parameter
line, so it is an algebraic fact about the letters, not a selection among
candidates.

Independent corroboration from the corpus: `1/[2]_q = 0.4972905456049155...` is
exactly the `1/delta = 0.497290545` that bean `qou-98g5` records the corpus
already carrying.

*** THE HONEST CAVEAT ***

`[2]_q` is ALSO the closest-landing member — `3 . E_0 . ln[2]_q = 8.77274`
MeV/nucleon against a measured peak `B/A = 8.79456`, 0.25 %, where the next best
(Kauffman) is 0.83 % away. Those are two independent facts and the coincidence
means the ENERGY comparison has little discriminating power here. **The pinning
does not rest on it.** The identity is checked symbolically and holds with no
reference to any energy, any anchor, or any measured binding value.

*** WHAT THIS CLOSES, AND WHAT IT DOES NOT ***

**Closes:** the condition `qou-59j5` and `qou-78pt` flagged. The family span was
1.33x, comparable to the deficit, so a residual could always be absorbed by a
convention choice. It cannot any more — after this a residual is a residual.

**Does not close:** `E_0` is still CAL-1, a calibration and not a derivation, so
the absolute scale is still unpinned. And the factor-of-3 gap stands: the colour
tube that would supply it is unrealisable in this construction family
(`qbeta_layout_conflict_probe.py`, `QOU/Hecke/LayoutConflict.lean`).

**And the averaged letter is NOT of this form.** `b_pn . [2]_q = 1.021998`, not a
power of `q0` — as expected, since `b_pn` is a weight-1 average of the two
crossings rather than a crossing. The identity is a statement about the two PURE
letters, and it is stated that way.
"""
from __future__ import annotations

import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590) order-zero E_0 routed + labelled, owner ruling 2026-11-20
import json
import subprocess
import time
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent

DPS = 40
mp.mp.dps = DPS
Q0_STR = "1.1099785827513808075916690956107688798744991218736"
Q0 = mp.mpf(Q0_STR)
M_E = mp.mpf("0.51099895069")
E0 = _qbeta_e0.order_zero_scaled(M_E, Q0)
STRANDS_PER_NUCLEON = 3
PEAK_B_OVER_A = mp.mpf("8.794555")          # measured, A = 62; see qbeta_strand_multiplicity


def _head_sha() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "unknown"


def _symbols():
    q = sp.symbols("q", positive=True)
    return q, {
        "b_pp": q**3/(q**2 + 1),                      # sigma      (pure crossing)
        "b_nn": 1/(q**3 + q),                         # sigma^-1   (pure crossing)
        "b_pn": (q**10 - 2*q**9 + 7*q**8 - 2*q**6 + 4*q**5 + 4*q**4
                 + q**2 - 2*q + 1)/(12*q**5*(q**2 + 1)),   # AVERAGED, not a crossing
    }


def _family(q):
    return {
        "[2]_q = q + 1/q (unframed Jones/TL loop)": q + 1/q,
        "[2]_Q = 1 + q^2 (corpus partition function)": 1 + q**2,
        "q^(1/2) + q^(-1/2) (Kauffman variable)": sp.sqrt(q) + 1/sp.sqrt(q),
        "1 + q^4 (over-shoot control)": 1 + q**4,
    }


def main() -> int:
    t0 = time.monotonic()
    a = []

    def chk(name, computed, expected, note=""):
        ok = computed == expected
        a.append({"name": name, "computed": computed, "expected": expected,
                  "passed": bool(ok), **({"note": note} if note else {})})
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {computed!r}")
        return ok

    ok = True
    q, B = _symbols()
    two_q = q + 1/q

    print("=" * 78)
    print("1. THE IDENTITY — symbolic, in q, with no numbers in it")
    print("=" * 78)
    prod = sp.simplify(B["b_pp"] * B["b_nn"])
    print(f"    b_pp . b_nn          = {prod}")
    print(f"    1/[2]_q^2            = {sp.simplify(1/two_q**2)}")
    ok &= chk("product_of_the_two_pure_crossing_bonds_is_the_inverse_loop_squared",
              sp.simplify(prod - 1/two_q**2) == 0, True,
              "b_pp is sigma and b_nn is sigma^-1; their product collapses to "
              "q^2/(q^2+1)^2 = 1/[2]_q^2 with no cancellation assumed")
    ok &= chk("each_pure_bond_is_a_q_squared_twist_of_the_inverse_loop",
              sp.simplify(B["b_pp"] - q**2/two_q) == 0
              and sp.simplify(B["b_nn"] - q**-2/two_q) == 0, True,
              "b_pp = q^2/[2]_q and b_nn = q^-2/[2]_q")
    geo = sp.sqrt(prod)
    print(f"    sqrt(b_pp . b_nn)    = {sp.simplify(geo)}   = 1/[2]_q")
    mean_L = sp.simplify((-sp.log(B["b_pp"]) - sp.log(B["b_nn"]))/2)
    ok &= chk("per_strand_coefficient_is_exactly_the_log_of_the_loop_value",
              sp.simplify(mean_L - sp.log(two_q)) == 0, True,
              "(L_pp + L_nn)/2 = ln[2]_q, identically in q")

    print("\n" + "=" * 78)
    print("2. IT DISCRIMINATES — only one family member satisfies it, at every q")
    print("=" * 78)
    fam_rows = []
    for nm, d in _family(q).items():
        identical = sp.simplify(geo - 1/d) == 0
        where = "IDENTICAL in q" if identical else "agrees only at q = 1"
        fam_rows.append({"member": nm, "identical": bool(identical)})
        print(f"    {nm:<44} {where}")
    ok &= chk("exactly_one_family_member_matches_identically",
              sum(1 for r in fam_rows if r["identical"]) == 1, True,
              "a fit would land at q0 and nowhere else; this holds on the whole "
              "parameter line, so it is an algebraic fact about the letters")

    inv = mp.mpf(1)/(Q0 + 1/Q0)
    print(f"\n    1/[2]_q at q0 = {mp.nstr(inv, 20)}")
    ok &= chk("matches_the_corpus_delta_recorded_in_qou_98g5",
              abs(inv - mp.mpf("0.497290545")) < mp.mpf("1e-9"), True,
              "bean qou-98g5 records the corpus carrying 1/delta = 0.497290545; "
              "that is this number, independently")

    print("\n" + "=" * 78)
    print("3. THE ENERGY COMPARISON — reported, and NOT what the pinning rests on")
    print("=" * 78)
    print(f"    {'member':<44}{'MeV/nucleon':>13}{'vs peak':>10}")
    energies = []
    for nm, d in _family(q).items():
        dv = mp.mpf(str(sp.N(d.subs(q, sp.Float(Q0_STR, DPS + 5)), DPS + 5)))
        per_nuc = STRANDS_PER_NUCLEON * E0 * mp.log(dv)
        energies.append({"member": nm, "MeV_per_nucleon": mp.nstr(per_nuc, 10),
                         "over_peak": mp.nstr(per_nuc/PEAK_B_OVER_A, 8)})
        print(f"    {nm:<44}{mp.nstr(per_nuc, 8):>13}{mp.nstr(per_nuc/PEAK_B_OVER_A, 6):>10}")
    span = (max(mp.mpf(e["MeV_per_nucleon"]) for e in energies)
            / min(mp.mpf(e["MeV_per_nucleon"]) for e in energies))
    print(f"    family span = {mp.nstr(span, 6)}x   (qou-59j5's 1.33x, reproduced)")
    ok &= chk("the_family_span_reproduces_qou_59j5s_1_33x",
              abs(span - mp.mpf("1.33")) < mp.mpf("0.02"), True,
              "so this is the same family, and it is that span the identity "
              "collapses to a single member")
    best = min(energies, key=lambda e: abs(mp.mpf(e["over_peak"]) - 1))
    ok &= chk("the_pinned_member_is_ALSO_the_closest_landing_one",
              best["member"].startswith("[2]_q"), True,
              "stated because it CUTS AGAINST the argument: the coincidence "
              "means the energy comparison has little discriminating power here. "
              "The pinning is §1-§2 and refers to no energy at all")

    print("\n    b_pn is NOT of this form — it is an AVERAGE, not a crossing:")
    bpn = mp.mpf(str(sp.N(B["b_pn"].subs(q, sp.Float(Q0_STR, DPS + 5)), DPS + 5)))
    print(f"      b_pn . [2]_q = {mp.nstr(bpn*(Q0 + 1/Q0), 12)}  (not a power of q0)")

    print("\n  ✅ delta = [2]_q, pinned by an identity in q. qou-59j5's condition")
    print("     — family span comparable to the deficit — is GONE.")
    print("  🛑 E_0 is still CAL-1, and the factor-3 layout conflict still stands.")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))

    witness = {
        "computation": "qbeta-loop-value-pinned",
        "q0Anchor": "proton",
        "assertions": a,
        "allPassed": bool(ok),
        "parameters": {"q0": Q0_STR, "dps": DPS, "E_0_MeV": mp.nstr(E0, 20),
                       "E_0_expression": "m_e/(q0*(q0-1))  [CAL-1, still a calibration]",
                       "strands_per_nucleon": STRANDS_PER_NUCLEON,
                       "peak_B_over_A_MeV": str(PEAK_B_OVER_A)},
        "data": {
            "identity": {
                "b_pp_times_b_nn": str(prod),
                "equals": "1/[2]_q^2",
                "geometric_mean": str(sp.simplify(geo)),
                "b_pp_closed": "q^2/[2]_q", "b_nn_closed": "q^-2/[2]_q",
                "per_strand_coefficient": "ln [2]_q",
            },
            "family_discrimination": fam_rows,
            "inverse_loop_at_q0": mp.nstr(inv, 20),
            "family_energies": energies,
            "family_span": mp.nstr(span, 10),
            "b_pn_times_two_q": mp.nstr(bpn*(Q0 + 1/Q0), 15),
        },
        "provenance": {"headSha": _head_sha(),
                       "producer": "computations/qbeta/qbeta_loop_value_pinned_probe.py",
                       "elapsed_s": round(time.monotonic() - t0, 3)},
    }
    out = HERE / "qbeta-loop-value-pinned.witness.json"
    out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
    print(f"\nwitness -> {out.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
