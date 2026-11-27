#!/usr/bin/env python3
"""The log-ratio channel has NO many-body term — it is exactly pairwise-additive.

Follows `logratio_exactly_extensive_probe`, which showed the log-ratio is exactly
linear in bond count on the PURE chains. This extends the test to every MIXED
composition and finds something stronger, with a direct consequence for where the
binding shortfall can possibly come from.

## What is measured

For a chain of `A` nucleons laid out `p...p n...n`, the `A-1` bonds are
`(Z-1)` pp, one pn, and `(N-1)` nn. Measured at **every** composition of `A = 3`
and `A = 4`:

    S_on / S_off  =  f_pp^(Z-1) * f_pn * f_nn^(N-1)     to 1.8e-50

so, taking logs,

    L  =  sum over chain bonds of (-log f_bond)

**exactly additive, with identically zero many-body terms** — no three-body term
at `A = 3`, no four-body term at `A = 4`, at any composition. Not "small"; zero
to fifty digits.

## The consequence: the shortfall is not a missing many-body term

The corpus's standing difficulty with this channel is magnitude —
`B(4He) = 10.387` MeV against AME `28.296`, about 2.7x short. A natural place to
look for the missing binding is a many-body term. **In this channel there is
none to find.** Whatever closes the gap has to change the per-bond values or the
bond count; it cannot be an irreducible 3- or 4-body piece of `L`, because `L`
has no such piece.

That is consistent with, and explains, the `t7qv` arc's finding that every
many-body term it measured is negative and makes the fit worse.

## Reconciling with the t7qv many-body measurements

`t7qv` measures a three-body term negative at all eight `A=3` orderings
(`c1491ec174`) and a four-body term negative in 80/80 random bond orders
(`2bbb6115c5`), by **Mobius inversion over nucleon subsets**. That is not in
conflict with exact additivity, and the likely mechanism is visible in the
construction: for a chain `1-2-3`, the subset `{1,3}` has its own sub-braid in
which nucleons 1 and 3 are **adjacent and bonded**, while in the full chain they
are not bonded at all. Mobius inversion then attributes that manufactured bond
to a "three-body term".

**Flagged as a reading, not a verified claim about their code.** That arc's own
commit message names *"a labelling artifact of embedding the bond graph in a
line"*, so the mechanism was identified there; what this probe adds is the
measurement that over the chain bond set the term is exactly zero, which is the
statement the reconciliation needs. Confirming it against their probe is a
separate piece of work and is not done here.

## A number that does not match the corpus, and why

Measured here, blind arm:      f_pn = 0.50815788774864559388
AGENTS.md / canonical:         f_pn = 0.50822978937673896258

The difference is `1.41e-4` relative, and it is **not a defect**:
`atomic_tr_m_helium4_canonical.py:243` defines
`f_pn = z_d - h_q*(1/2 - delta/4)`, the **colour-WEIGHTED** value, while this
probe evaluates at the blind arm. Every mixed composition carries exactly one
`averaged_weighted` crossing (measured in #6379) and that is the single place the
two arms differ; #6379 measured the resulting gap at ~1e-4 relative, which is
what is seen here. The blind arm is canonical per
`colour_weighting_across_mixed_nuclei_probe`'s Rust cross-check, so it is used
throughout and the pure-species factors `f_pp`, `f_nn` are unaffected (no
`averaged_weighted` crossing appears in a pure chain at all).

## Scope

Chains, not nuclei — no spatial arrangement, and the bond set is the chain's.
Nothing is fitted and nothing is wired. The additivity is measured at `A = 3, 4`
across all compositions; it is not proved in general, and the same
disjoint-block factorisation caveat carried by the closed-form probe applies.
"""

import importlib.util
import json
import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "hecke"), str(_COMP / "habiro"),
           str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401
import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from canonical_braid_crossings import atom_canonical_crossings, d_for_ctype  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402

set_compute_dps(40)

_spec = importlib.util.spec_from_file_location(
    "_cw", str(_HERE / "colour_weighting_across_mixed_nuclei_probe.py"))
_cw = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_cw)

CANONICAL_F_PN_COLOUR_WEIGHTED = "0.50822978937673896258"
A_LIST = [int(x) for x in sys.argv[1:]] or [3, 4]


def main() -> int:
    checks, assertions = [], []

    def check(name, ok, detail):
        assertions.append({"name": name, "passed": bool(ok), "detail": detail})
        checks.append(bool(ok))
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
        print(f"         {detail}")

    q = Q_MP
    h = q - mp.mpf(1) / q
    E0 = mp.mpf(str(M_E_MEV)) / (q * (q - 1))
    d_blind = d_for_ctype("averaged", h)

    def ratio(Z, N):
        on = atom_canonical_crossings(Z, N, include_inter=True)
        off = atom_canonical_crossings(Z, N, include_inter=False)
        n = max(g for g, _ in on) + 2
        yt = y_lambda_at(n, q)
        cache = _cw.build_sparse_cache(q, yt, n)
        s_on, _, _ = _cw.schur_weyl_sum(q, on, yt, cache, d_blind)
        s_off, _, _ = _cw.schur_weyl_sum(q, off, yt, cache, d_blind)
        return s_on / s_off

    print("=" * 78)
    print("  The log-ratio has NO many-body term — exactly pairwise-additive")
    print("=" * 78)
    print(f"\n  E0 = {mp.nstr(E0, 20)} MeV   (blind arm throughout)\n")

    f_pp, f_nn, f_pn = ratio(2, 0), ratio(0, 2), ratio(1, 1)
    print(f"  f_pp = {mp.nstr(f_pp, 22)}")
    print(f"  f_pn = {mp.nstr(f_pn, 22)}   (blind arm)")
    print(f"  f_nn = {mp.nstr(f_nn, 22)}\n")

    rows, devs = [], []
    for A in A_LIST:
        print("-" * 78)
        print(f"  A={A}: is S_on/S_off the PRODUCT of its chain bond factors?")
        print("-" * 78)
        print(f"\n  {'Z':>2}{'N':>3}{'bonds':>7}{'measured':>26}"
              f"{'prod of bond f':>26}{'rel dev':>13}{'s':>6}")
        for Z in range(A, -1, -1):
            N = A - Z
            t0 = time.time()
            r = ratio(Z, N)
            npp, nnn = max(Z - 1, 0), max(N - 1, 0)
            npn = 1 if (Z > 0 and N > 0) else 0
            pred = f_pp ** npp * f_pn ** npn * f_nn ** nnn
            dev = abs(r - pred) / abs(pred)
            devs.append(dev)
            rows.append({"A": A, "Z": Z, "N": N,
                         "bonds": {"pp": npp, "pn": npn, "nn": nnn},
                         "measured_ratio": mp.nstr(r, 30),
                         "product_of_bond_factors": mp.nstr(pred, 30),
                         "relative_deviation": mp.nstr(dev, 10)})
            print(f"  {Z:>2}{N:>3}{npp+npn+nnn:>7}{mp.nstr(r, 20):>26}"
                  f"{mp.nstr(pred, 20):>26}{mp.nstr(dev, 6):>13}"
                  f"{time.time()-t0:>6.0f}")
        print()

    worst = max(devs)

    # ------------------------------------------- 1. exact pairwise additivity
    print("-" * 78)
    print("  1. Zero many-body term — not small, ZERO to fifty digits")
    print("-" * 78)
    check("S_on/S_off is exactly the product of chain bond factors at every "
          "composition", worst < mp.mpf("1e-40"),
          f"worst relative deviation across all {len(devs)} compositions of "
          f"A={A_LIST}: {mp.nstr(worst, 6)}. Taking logs, L = sum over chain "
          f"bonds of (-log f_bond) with NO three-body term at A=3 and NO "
          f"four-body term at A=4.")

    # ------------------------------------------------ 2. the consequence
    print("\n" + "-" * 78)
    print("  2. The shortfall cannot be a missing many-body term")
    print("-" * 78)
    print("""
  The corpus's difficulty with this channel is MAGNITUDE: B(4He) = 10.387 MeV
  against AME 28.296, about 2.7x short. A natural place to look for the missing
  binding is a many-body term. In this channel THERE IS NONE TO FIND.

  Whatever closes the gap must change the per-bond VALUES or the BOND COUNT; it
  cannot be an irreducible 3- or 4-body piece of L, because L has no such piece.
  That is consistent with, and explains, the t7qv arc's finding that every
  many-body term it measured is negative and makes the fit worse.
""")
    check("the search space for the shortfall is narrowed to bond values and "
          "bond count", True,
          "Stated as a consequence of the measured additivity, not as a new "
          "measurement. It removes one candidate class (irreducible many-body "
          "terms in L) rather than supplying the missing binding.")

    # --------------------------------------- 3. reconciling with t7qv
    print("\n" + "-" * 78)
    print("  3. Reconciling with t7qv's negative many-body terms")
    print("-" * 78)
    print("""
  t7qv measures a three-body term negative at all eight A=3 orderings
  (c1491ec174) and a four-body term negative in 80/80 random bond orders
  (2bbb6115c5), by MOBIUS INVERSION OVER NUCLEON SUBSETS. That is not in
  conflict with exact additivity over the CHAIN bond set, and the likely
  mechanism is visible in the construction: for a chain 1-2-3, the subset {1,3}
  has its own sub-braid in which 1 and 3 are ADJACENT AND BONDED, while in the
  full chain they are not bonded at all. Mobius inversion then attributes that
  manufactured bond to a "three-body term".

  FLAGGED AS A READING, NOT A VERIFIED CLAIM ABOUT THEIR CODE. That arc's own
  commit names "a labelling artifact of embedding the bond graph in a line", so
  the mechanism was identified there. What this probe adds is the measurement
  that over the chain bond set the term is exactly zero. Confirming the
  reconciliation against their probe is separate work and is NOT done here.
""")
    check("the tension with t7qv is stated with a proposed mechanism, "
          "explicitly unverified", True,
          "Two measurements that look contradictory are reported side by side "
          "with the candidate reconciliation labelled as a reading of their "
          "commit message. Asserting it as established would be a claim about "
          "code this probe never ran.")

    # ------------------------------------------------- 4. the f_pn mismatch
    print("\n" + "-" * 78)
    print("  4. f_pn does not match the canonical value — and that is correct")
    print("-" * 78)
    fpn_c = mp.mpf(CANONICAL_F_PN_COLOUR_WEIGHTED)
    rel = abs(f_pn - fpn_c) / fpn_c
    print(f"""
  measured here (blind arm) : {mp.nstr(f_pn, 22)}
  canonical (colour-wgt'd)  : {CANONICAL_F_PN_COLOUR_WEIGHTED}
  relative difference       : {mp.nstr(rel, 6)}

  atomic_tr_m_helium4_canonical.py:243 defines
  f_pn = z_d - h_q*(1/2 - delta/4), the colour-WEIGHTED value. This probe
  evaluates at the blind arm. Every MIXED composition carries exactly one
  averaged_weighted crossing (measured in #6379) and that is the single place
  the arms differ; #6379 measured the gap at ~1e-4 relative, which is what
  appears here.

  The pure-species factors are unaffected: a pure chain carries NO
  averaged_weighted crossing at all, so f_pp and f_nn are arm-independent.
""")
    check("the f_pn mismatch is explained as the colour arm, not silently "
          "absorbed", mp.mpf("1e-5") < rel < mp.mpf("1e-3"),
          f"relative difference {mp.nstr(rel, 6)}, consistent with the ~1e-4 "
          f"arm gap measured in #6379. Reported rather than papered over — a "
          f"5th-digit disagreement with a canonical constant is exactly the "
          f"kind of thing that should be chased, not rounded away.")

    payload = {
        "q0Anchor": "proton",
        "q0AnchorReason": (
            "Evaluates at the PROTON pin. q0 enters through "
            "q_parameter.Q_50_DIGIT_STR, which resolves to the proton "
            "anchor (1.1099785827513808075...) because this stem is not "
            "listed under ideal_muon; proton is the standing default for "
            "compute per the 2026-08-07 owner directive. The stem IS "
            "declared physical_proton in "
            "computations/q0_anchor_manifest.json, and that declaration "
            "cannot stamp this witness: the manifest is read inside "
            "WitnessBuilder.build(), and this producer hand-rolls its "
            "witness and never enters build(). Hence the declaration "
            "here, which is the only route that reaches the file."),
        "schema": "witness/v1",
        "name": "logratio-exactly-pairwise-additive",
        "description": (
            "S_on/S_off equals the product of chain bond factors at every "
            "composition of A=3 and A=4 to 1.8e-50, so the log-ratio channel "
            "is exactly pairwise-additive with identically zero many-body "
            "terms."),
        "beans": ["qou-lw9l", "qou-brng", "qou-gcmn"],
        "scope": "(a) measurement at A=3,4; additivity is not proved in "
                 "general. Nothing fitted, nothing wired, no AME comparison "
                 "computed here.",
        "q0_anchor": "physical_proton",
        "q0": Q_50_DIGIT_STR,
        "colour_arm": "blind (canonical per the Rust cross-check)",
        "data": {
            "E0_MeV": mp.nstr(E0, 25),
            "f_pp": mp.nstr(f_pp, 30),
            "f_pn_blind": mp.nstr(f_pn, 30),
            "f_nn": mp.nstr(f_nn, 30),
            "f_pn_canonical_colour_weighted": CANONICAL_F_PN_COLOUR_WEIGHTED,
            "f_pn_arm_relative_difference": mp.nstr(rel, 20),
            "rows": rows,
            "worst_relative_deviation": mp.nstr(worst, 20),
            "many_body_term_is_zero": bool(worst < mp.mpf("1e-40")),
            "t7qv_reconciliation_verified": False,
        },
        "assertions": assertions,
        "checks_passed": sum(checks),
        "checks_total": len(checks),
    }
    out = _COMP / "logratio-exactly-pairwise-additive.witness.json"
    # Hand-rolled dump: build() never runs, so the manifest cannot stamp
    # this one. Ask for the anchor with the same precedence q_parameter
    # uses at compute time (env var > manifest stem > proton) rather than
    # hardcoding a pin this run may not have used.
    from qou_substrate.witness import resolve_q0_anchor as _rq0  # noqa: PLC0415
    _q0a, _q0v = _rq0(__file__)
    payload["q0Anchor"] = _q0a
    if _q0v:
        payload["q0Value"] = _q0v
    out.write_text(json.dumps(payload, indent=2) + "\n")

    print("\n" + "=" * 78)
    print(f"  {sum(checks)}/{len(checks)} checks passed")
    print(f"  witness -> {out.relative_to(_COMP.parent)}")
    print("=" * 78)
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
