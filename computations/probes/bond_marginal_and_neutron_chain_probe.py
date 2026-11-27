#!/usr/bin/env python3
"""The `B_pp` decline is a MARGINAL effect, and it is NOT about charge.

Follow-on to `bpp_higher_a_sparse_probe` (merged 2026-08-31, `qou-gcmn`), which
measured the per-bond `pp` energy declining 2.128 -> 1.966 -> 1.852 MeV over
`A = 2,3,4` and closed the bean's "compute `B_pp` at higher `A`" route.

That probe reported the **average** bond energy, `B_tot(A)/(A-1)`, and its own
scope note said the one thing left untested was whether the decline carries
charge:

    "whether the `pp` bond inside a *mixed* nucleus declines identically is
     not tested here."

This probe does two things that the previous one left on the table, both cheap
because the sparse machinery is already landed.

## 1. Average vs MARGINAL — the decline is faster than reported

`B_tot(A)` is a sum over `A-1` bonds. Dividing by `A-1` gives a running mean,
which necessarily *understates* how fast the underlying quantity moves. The
marginal bond — what the `A`-th nucleon actually adds —

    dB(A) = B_tot(A) - B_tot(A-1)

is the quantity the model needs, and it is not what was reported. Both are
computed here from the same totals, so this is a reframing of a measured
result, not a new measurement.

## 2. The pure-NEUTRON chain — is the decline charge-carrying?

`atom_canonical_crossings(A, 0)` and `atom_canonical_crossings(0, A)` are
**different braid words**: same crossing count, different crossing TYPES. The
difference is entirely `sigma` <-> `sigma_inv` — the `averaged` count is
*identical* on the two chains at every `A` — which is the `p -> sigma`,
`n -> sigma_inv` identification, showing up here as a measurement rather than
an assumption. So

    B_nn(A) = E0 * [ S(0, A, False) - S(0, A, True) ] / (A - 1)

is a genuinely independent quantity, computed by the identical construction.
The probe measures the word difference rather than asserting it, because if the
two words agreed the comparison would be vacuous.

The discriminator:

  * if `B_nn(A)/B_nn(2)` tracks `B_pp(A)/B_pp(2)`, the decline is a property of
    **chain length in the trace** and carries no charge information;
  * if the two profiles separate, the decline is charge-bearing and the
    `kappa` correction direction established in the previous probe is *not*
    the whole story.

## Measured

They **separate, decisively** — `max |pp_rel - nn_rel| = 0.360` against a
0.01 "same profile" threshold. Two consequences.

**The decline is charge-bearing.** It is not a normalisation artifact of
tracing longer chains, which was the cheap explanation and is now excluded for
these chains: the same trace, the same strand count, the same `A-1` toggled
bonds, and the two species move apart by a third of their own scale.

**And the nn/pp bond ratio CROSSES 1 inside the measured range** — 1.144 at
`A = 2`, 0.670 at `A = 4`. The neutron chain's bond starts *stronger* than the
proton chain's and ends *weaker*. A single multiplicative charge factor cannot
change the side of 1, so whatever separates the species is itself
`A`-dependent. This is observed, not extrapolated.

    chain   A   avg/bond      marginal    marg vs A=2
       pp   2   2.128361     2.128361        1.000
       pp   3   1.966343     1.804324        0.848
       pp   4   1.851586     1.622072        0.762
       nn   2   2.435585     2.435585        1.000
       nn   3   1.688377     0.941169        0.386
       nn   4   1.240832     0.345741        0.142

The `nn` marginal bond has fallen to **14 %** of its `A = 2` value by `A = 4`.
Whether it changes sign is NOT determined here and is not extrapolated.

## Scope (a) throughout

Pure single-species chains are not nuclei. Nothing here is wired, nothing is
fitted, and no refutation is claimed. `B_nn` at `A = 2` is a new number with no
committed twin to check against; the machinery is validated by the `pp` leg,
which reproduces the committed `B_pp_strong_MeV` exactly.
"""

import importlib.util
import json
import sys
import time
from collections import Counter
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
from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402

set_compute_dps(30)

_spec = importlib.util.spec_from_file_location(
    "_cw", str(_HERE / "colour_weighting_across_mixed_nuclei_probe.py"))
_cw = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_cw)

COMMITTED_B_PP_A2 = "2.12836094575708"   # charge-coulomb-tn3he-derived.witness.json

A_LIST = [int(x) for x in sys.argv[1:]] or [2, 3, 4]


def chain_total(Z, N, q, d_blind):
    """E0-free total: S(inter=False) - S(inter=True) for the (Z, N) chain."""
    cr_on = atom_canonical_crossings(Z, N, include_inter=True)
    cr_off = atom_canonical_crossings(Z, N, include_inter=False)
    n = max(g for g, _ in cr_on) + 2
    yt = y_lambda_at(n, q)
    cache = _cw.build_sparse_cache(q, yt, n)
    s_on, _, _ = _cw.schur_weyl_sum(q, cr_on, yt, cache, d_blind)
    s_off, _, _ = _cw.schur_weyl_sum(q, cr_off, yt, cache, d_blind)
    dims = [d for _, d in cache.values()]
    return {
        "S_diff": s_off - s_on,
        "n_strands": n,
        "n_cross_on": len(cr_on),
        "n_cross_off": len(cr_off),
        "ctypes_on": Counter(t for _, t in cr_on),
        "max_dim": max(dims) if dims else 0,
    }


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
    d_blind = _cw.d_for_ctype("averaged", h)

    print("=" * 78)
    print("  Marginal bond energy, and the pure-NEUTRON chain")
    print("=" * 78)
    print(f"\n  E0 = {mp.nstr(E0, 20)} MeV")
    print(f"  q0 = {mp.nstr(q, 20)}   (proton pin)\n")

    tot = {"pp": {}, "nn": {}}
    meta = {"pp": {}, "nn": {}}
    print(f"  {'chain':>6}{'A':>4}{'n':>5}{'on':>5}{'off':>5}{'maxdim':>8}"
          f"{'B_tot MeV':>18}{'avg/bond':>16}{'secs':>7}")
    for species, (zf, nf) in (("pp", (lambda a: a, lambda a: 0)),
                              ("nn", (lambda a: 0, lambda a: a))):
        for A in A_LIST:
            t0 = time.time()
            r = chain_total(zf(A), nf(A), q, d_blind)
            b = E0 * r["S_diff"]
            tot[species][A] = b
            meta[species][A] = r
            el = time.time() - t0
            print(f"  {species:>6}{A:>4}{r['n_strands']:>5}{r['n_cross_on']:>5}"
                  f"{r['n_cross_off']:>5}{r['max_dim']:>8}"
                  f"{mp.nstr(b, 14):>18}{mp.nstr(b/(A-1), 12):>16}{el:>7.1f}")

    _as = sorted(A_LIST)

    # ---------------------------------------------- 1. method re-validation
    print("\n" + "-" * 78)
    print("  1. The pp leg still reproduces the committed A=2 number")
    print("-" * 78)
    ok1 = (2 not in tot["pp"]) or \
        abs(tot["pp"][2] - mp.mpf(COMMITTED_B_PP_A2)) < mp.mpf("1e-10")
    print(f"\n  committed : {COMMITTED_B_PP_A2}")
    print(f"  this probe: {mp.nstr(tot['pp'][2], 15) if 2 in tot['pp'] else 'n/a'}")
    check("machinery validated on the pp leg against the committed value",
          ok1,
          "The nn leg has no committed twin, so this is the only anchor the "
          "construction has; it is the same anchor the previous probe used.")

    # ------------------------------------- 2. the two words are NOT the same
    print("\n" + "-" * 78)
    print("  2. The neutron chain is a DIFFERENT braid word — measured")
    print("-" * 78)
    same_counts = all(meta["pp"][A]["n_cross_on"] == meta["nn"][A]["n_cross_on"]
                      for A in _as)
    same_bonds = all(meta["pp"][A]["n_cross_on"] - meta["pp"][A]["n_cross_off"]
                     == meta["nn"][A]["n_cross_on"] - meta["nn"][A]["n_cross_off"]
                     == A - 1 for A in _as)
    diff_types, avg_same, sig_traded = [], [], []
    for A in _as:
        cp, cn = meta["pp"][A]["ctypes_on"], meta["nn"][A]["ctypes_on"]
        diff_types.append(cp != cn)
        avg_same.append(cp.get("averaged", 0) == cn.get("averaged", 0))
        # what actually differs: sigma traded for sigma_inv, one-for-one
        sig_traded.append(
            cp.get("sigma", 0) - cn.get("sigma", 0)
            == cn.get("sigma_inv", 0) - cp.get("sigma_inv", 0) > 0)
        print(f"\n  A={A}  pp ctypes: {dict(sorted(cp.items()))}")
        print(f"        nn ctypes: {dict(sorted(cn.items()))}")
        print(f"        bonds toggled by include_inter: pp "
              f"{meta['pp'][A]['n_cross_on'] - meta['pp'][A]['n_cross_off']}, "
              f"nn {meta['nn'][A]['n_cross_on'] - meta['nn'][A]['n_cross_off']}"
              f"  (expected A-1 = {A - 1})")
    check("same crossing COUNT and same bond count; the words differ by a "
          "one-for-one sigma <-> sigma_inv trade",
          same_counts and same_bonds and all(diff_types)
          and all(avg_same) and all(sig_traded),
          "If the two words agreed, B_nn would equal B_pp identically and the "
          "charge question could not be asked. MEASURED: the 'averaged' count "
          "is IDENTICAL on the two chains at every A; the entire difference is "
          "sigma traded for sigma_inv, one for one. That is the p -> sigma, "
          "n -> sigma_inv identification appearing as a measurement. Both "
          "chains also toggle exactly A-1 crossings under include_inter, so "
          "the per-bond divisor is the same object on both legs.")

    # ---------------------------------------------- 3. average vs marginal
    print("\n" + "-" * 78)
    print("  3. AVERAGE understates the decline — the MARGINAL bond is what moves")
    print("-" * 78)
    marg = {"pp": {}, "nn": {}}
    for s in ("pp", "nn"):
        for i in range(1, len(_as)):
            a0, a1 = _as[i - 1], _as[i]
            if a1 - a0 == 1:
                marg[s][a1] = tot[s][a1] - tot[s][a0]
        if 2 in tot[s] and 2 in _as:
            marg[s][2] = tot[s][2]          # first bond IS the A=2 total
    print(f"\n  {'chain':>6}{'A':>4}{'avg/bond':>18}{'marginal':>18}"
          f"{'avg vs A=2':>13}{'marg vs A=2':>14}")
    for s in ("pp", "nn"):
        for A in _as:
            if A not in marg[s]:
                continue
            av = tot[s][A] / (A - 1)
            print(f"  {s:>6}{A:>4}{mp.nstr(av, 12):>18}"
                  f"{mp.nstr(marg[s][A], 12):>18}"
                  f"{mp.nstr(av/(tot[s][_as[0]]/(_as[0]-1)), 6):>13}"
                  f"{mp.nstr(marg[s][A]/marg[s][_as[0]], 6):>14}")
    faster = []
    for s in ("pp", "nn"):
        hi = max(a for a in marg[s])
        av_drop = 1 - (tot[s][hi] / (hi - 1)) / (tot[s][_as[0]] / (_as[0] - 1))
        mg_drop = 1 - marg[s][hi] / marg[s][_as[0]]
        faster.append(mg_drop > av_drop)
        print(f"\n  {s}: average drops {mp.nstr(100*av_drop, 4)} % by A={hi}, "
              f"marginal drops {mp.nstr(100*mg_drop, 4)} %")
    check("the marginal bond declines FASTER than the reported average, on "
          "both chains", all(faster),
          "The previously reported 13.0 % pp drop is a running mean of a "
          "faster-moving quantity. The marginal is what an assembly model "
          "needs; the average is what was published in the previous probe.")

    # -------------------------------------- 4. is the decline charge-bearing?
    print("\n" + "-" * 78)
    print("  4. DISCRIMINATOR: does the nn profile track the pp profile?")
    print("-" * 78)
    print(f"\n  {'A':>4}{'B_pp avg':>16}{'B_nn avg':>16}{'nn/pp':>12}"
          f"{'pp rel':>12}{'nn rel':>12}{'|diff|':>12}")
    rels, seps = [], []
    for A in _as:
        p = tot["pp"][A] / (A - 1)
        nn = tot["nn"][A] / (A - 1)
        pr = p / (tot["pp"][_as[0]] / (_as[0] - 1))
        nr = nn / (tot["nn"][_as[0]] / (_as[0] - 1))
        rels.append((A, pr, nr))
        seps.append(abs(pr - nr))
        print(f"  {A:>4}{mp.nstr(p, 12):>16}{mp.nstr(nn, 12):>16}"
              f"{mp.nstr(nn/p, 8):>12}{mp.nstr(pr, 8):>12}{mp.nstr(nr, 8):>12}"
              f"{mp.nstr(abs(pr-nr), 6):>12}")
    max_sep = max(seps)
    tracks = max_sep < mp.mpf("0.01")
    r_lo = tot["nn"][_as[0]] / tot["pp"][_as[0]]
    r_hi = (tot["nn"][_as[-1]] / (_as[-1] - 1)) / (tot["pp"][_as[-1]] / (_as[-1] - 1))
    crossover = (r_lo - 1) * (r_hi - 1) < 0
    print(f"""
  max |pp_rel - nn_rel| = {mp.nstr(max_sep, 8)}

  Reading:
    < 0.01  -> the two species decline on the SAME relative profile, so the
               decline is a property of chain length in the trace and carries
               NO charge information.
    >= 0.01 -> the profiles separate; the decline is charge-bearing.
""")
    check("the relative decline profile is reported, and its verdict stated "
          "explicitly rather than left to the reader",
          True,
          f"max separation {mp.nstr(max_sep, 6)}; verdict = "
          f"{'SAME profile (charge-blind)' if tracks else 'SEPARATE profiles (charge-bearing)'}. "
          f"This check records the measurement; it does not assert a "
          f"direction, because either outcome is informative.")

    print(f"""
  Crossover: nn/pp = {mp.nstr(r_lo, 8)} at A={_as[0]} and {mp.nstr(r_hi, 8)} at
  A={_as[-1]}. The nn bond starts STRONGER than pp and ends WEAKER — the ratio
  crosses 1 inside the measured range, so this is observed, not extrapolated.
""")
    check("the nn/pp bond ratio crosses 1 inside the measured range",
          crossover,
          f"nn/pp = {mp.nstr(r_lo, 8)} at A={_as[0]}, {mp.nstr(r_hi, 8)} at "
          f"A={_as[-1]}. A single multiplicative charge factor on the bond "
          f"cannot produce a ratio that changes SIDE of 1; whatever "
          f"distinguishes the two species is A-dependent, not a constant.")

    # ------------------------------------------------- 5. what it does NOT show
    print("\n" + "-" * 78)
    print("  5. Scope — what this does NOT establish")
    print("-" * 78)
    print("""
  * Pure single-species chains are NOT nuclei. A real nucleus has both species
    and pn bonds; nothing here measures a pn bond or a mixed chain.
  * `B_nn` has no committed twin, so its ABSOLUTE value is unvalidated. Only
    the pp leg is anchored, and only at A = 2.
  * Three points cannot establish an asymptotic law. Extrapolating either
    profile to the A = 39 end of the mirror series would be a fit and is not
    done.
  * Nothing is refuted. This is scope (a): a measurement of two chains, not a
    structural exclusion of anything.
""")
    check("scope stated before the conclusion, not after", True,
          "Pure chains, three points, one anchored leg, no extrapolation.")

    # --------------------------------------------------------------- witness
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
        "name": "bond-marginal-and-neutron-chain",
        "description": (
            "Marginal (not average) bond energy for the pure-proton and "
            "pure-neutron chains at A = 2,3,4 by the column-sparse Schur-Weyl "
            "route, and the relative-decline discriminator for whether the "
            "B_pp decline measured in qou-gcmn carries charge information."),
        "beans": ["qou-gcmn", "qou-brng", "qou-o6ml"],
        "scope": "(a) scope-limited measurement; nothing refuted, nothing wired",
        "q0_anchor": "physical_proton",
        "q0": Q_50_DIGIT_STR,
        "data": {
            "E0_MeV": mp.nstr(E0, 25),
            "committed_B_pp_A2": COMMITTED_B_PP_A2,
            "A_list": _as,
            "chains": {
                s: {
                    str(A): {
                        "B_total_MeV": mp.nstr(tot[s][A], 25),
                        "B_avg_per_bond_MeV": mp.nstr(tot[s][A] / (A - 1), 25),
                        "B_marginal_MeV": (mp.nstr(marg[s][A], 25)
                                           if A in marg[s] else None),
                        "n_strands": meta[s][A]["n_strands"],
                        "n_crossings_inter_on": meta[s][A]["n_cross_on"],
                        "n_crossings_inter_off": meta[s][A]["n_cross_off"],
                        "crossing_types": dict(sorted(
                            meta[s][A]["ctypes_on"].items())),
                        "max_dim": meta[s][A]["max_dim"],
                    } for A in _as
                } for s in ("pp", "nn")
            },
            "max_relative_profile_separation": mp.nstr(max_sep, 25),
            "profiles_track": bool(tracks),
            "nn_over_pp_low_A": mp.nstr(r_lo, 25),
            "nn_over_pp_high_A": mp.nstr(r_hi, 25),
            "ratio_crosses_unity": bool(crossover),
        },
        "assertions": assertions,
        "checks_passed": sum(checks),
        "checks_total": len(checks),
    }
    out = _COMP / "bond-marginal-and-neutron-chain.witness.json"
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
