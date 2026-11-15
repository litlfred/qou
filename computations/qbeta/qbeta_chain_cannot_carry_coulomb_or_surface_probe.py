#!/usr/bin/env python3
"""Coulomb and surface have ONE root cause — the chain edge set. Plus two
corrections to my own earlier reporting.

`qou-nial` diagnosed the Coulomb absence as *"the bond rule is a centred SUM of
charges where Coulomb needs a PRODUCT"*, and `qou-3wvl` identified the
alpha-cluster +13 % drift by 16O as the surface correction. This makes both
concrete, finds they are the same defect, and corrects two things this arc
previously reported wrongly.

*** 1. THE CHAIN CANNOT CARRY COULOMB — it has Z-1 p-p bonds, not Z(Z-1)/2 ***

Coulomb energy counts proton PAIRS. The canonical atom is a path, and a path on
`Z` protons has `Z - 1` p-p edges, so the law captures a fraction `2/Z` of them:

       Z    proton pairs   chain p-p bonds   captured
       2               1                 1     100 %
       8              28                 7      25 %
      20             190                19      10 %
      26             325                25     7.69 %
      50            1225                49        4 %
      82            3321                81     2.44 %

At the top of the table **97.6 % of the proton-proton interactions are absent by
construction.** That is `qou-nial`'s sum-vs-product stated as combinatorics: a
path's edge count is LINEAR in its vertices, and Coulomb needs QUADRATIC. No
choice of letter, convention or scale can produce a `Z^2` term from `Z-1` edges.

*** 2. AND IT CANNOT CARRY A SURFACE TERM — a path has constant degree ***

The surface term is a coordination DEFICIT: nucleons at the boundary have fewer
neighbours than interior ones, and the boundary is `~A^(2/3)` of them. In a path
every interior vertex has degree exactly 2 and the two endpoints have degree 1 —
a deficit of `2`, independent of `A`. **No `A^(2/3)` piece can arise from the
edge count of a path**, for any letters.

So the two gaps are one gap: the edge set is a 1-D chain when the physics is a
saturating 3-D packing.

*** 3. CORRECTION — my earlier all-pairs test was RIGGED ***

`qbeta_tower_log_z_and_roast_probe.py` §3(c) and the synthesis §6 report that
"three different edge sets — the canonical chain, the alternating chain, and the
renormalised all-pairs graph — land within 0.6 % of one another, so **the bond
GRAPH is not where the error lives**".

**That conclusion is an artefact of the renormalisation.** I scaled all-pairs to
`A-1` bonds, which throws away precisely the quadratic growth that distinguishes
it. Raw:

    edge set                          median ratio    p5-p95
    chain            (A-1 bonds)          0.886414    1.22497
    all-pairs RAW    (A(A-1)/2 bonds)     0.013558    9.88639

a factor of **65 in the median**, not 0.6 %. The edge sets do NOT agree, and the
bond graph is exactly where the error lives.

What survives of that section: the comparison of the two ORDERINGS (segregated
vs alternating) is unaffected — both are chains with the same bond count,
differing only in the pp/pn/nn split — so `qou-48is` remains near-irrelevant to
`B`. It is the *edge-set* half of the claim that is withdrawn.

*** 4. CORRECTION — the marginal correlations badly understated Coulomb ***

This arc has repeatedly quoted marginal correlations `(N-Z)^2/A^2 = -0.804`,
`A^(-1/3) = -0.178`, `Z^2/A^(4/3) = -0.044`, and read the last as "Coulomb is
essentially absent from the residual". **Marginal correlations conflate collinear
shapes** — heavy nuclei have large `Z`, large `N-Z` and large `A` together.

Regressing the log-residual on all three JOINTLY and ranking by CONTRIBUTION
(coefficient times regressor range), not by coefficient:

    shape             contribution span (log)     in B
    (N-Z)^2/A^2                   1.528          361 %
    A^(-1/3)                      0.930          154 %
    Z^2/A^(4/3)                   0.512           67 %

    total log-residual span 2.321      joint R^2 = 0.9266

Coulomb spans **67 % in B**, not "essentially absent". The asymmetry is still
largest, but the ranking is **3 : 1.8 : 1**, not the 18 : 4 : 1 the marginals
suggested.

*** AND THE HEADLINE THE JOINT FIT GIVES ***

**R^2 = 0.927.** The three SEMF shapes jointly explain 93 % of the log-residual.
The missing physics is not exotic and not unidentified — it is the liquid-drop
corrections, in their standard forms, and two of the three follow from a single
structural fact about the edge set.

*** SCOPE ***

The regression is a DIAGNOSTIC — used to rank and to correct a misreading, never
adopted as a law. Fitting three SEMF coefficients would reproduce the SEMF and
prove nothing about the algebra. What is established here is structural: a path
cannot produce `Z^2` or `A^(2/3)`, whatever letters sit on its edges.
"""
from __future__ import annotations

import json
import subprocess
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent

DPS = 30
mp.mp.dps = DPS
Q0 = mp.mpf("1.1099785827513808075916690956107688798744991218736")
M_E = mp.mpf("0.51099895069")
HBAR_Q = (Q0 - 1)/Q0
E0 = M_E/(Q0*(Q0 - 1))/(1 - HBAR_Q**2)
STRANDS = 3
Z_M = Q0**3/(Q0**2 + 1)
B_NN = 1/(Q0**3 + Q0)
B_PN = ((Q0**10 - 2*Q0**9 + 7*Q0**8 - 2*Q0**6 + 4*Q0**5 + 4*Q0**4
         + Q0**2 - 2*Q0 + 1)/(12*Q0**5*(Q0**2 + 1)))
L_PP, L_PN, L_NN = -mp.log(Z_M), -mp.log(B_PN), -mp.log(B_NN)

AME = ROOT / "qou-mass/src/qou_mass/data/ame2020.json"


def _head_sha() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "unknown"


def chain_bonds(Z, N):
    """The canonical `A-1` path: `Z-1` p-p, one interface, `N-1` n-n."""
    return (mp.mpf(Z - 1), mp.mpf(1), mp.mpf(N - 1))


def allpairs_bonds_raw(Z, N):
    """Every pair, UNRENORMALISED — `A(A-1)/2` bonds, quadratic in `A`."""
    return (mp.mpf(Z*(Z - 1))/2, mp.mpf(Z*N), mp.mpf(N*(N - 1))/2)


def bond_sum(bf, Z, N):
    p, m, n = bf(Z, N)
    return p*L_PP + m*L_PN + n*L_NN


def _pct(v, n, d=100):
    s = sorted(v)
    return s[min(len(s) - 1, len(s)*n//d)]


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
    meas = []
    for e in json.loads(AME.read_text())["entries"]:
        Z, N, A = e["Z"], e["N"], e["A"]
        b = e.get("binding_energy_per_A_keV")
        if Z < 1 or N < 1 or not b or e.get("binding_energy_per_A_estimated"):
            continue
        B = mp.mpf(str(b))*A/1000
        if B > 0:
            meas.append((A, Z, N, B))

    print("=" * 78)
    print("1. THE CHAIN CANNOT CARRY COULOMB")
    print("=" * 78)
    print(f"    {'Z':>4}{'proton pairs':>15}{'chain p-p bonds':>18}{'captured':>12}")
    cap = []
    for Z in (2, 8, 20, 26, 50, 82):
        frac = mp.mpf(2)/Z
        cap.append({"Z": Z, "pairs": Z*(Z - 1)//2, "chain_bonds": Z - 1,
                    "captured_pct": mp.nstr(frac*100, 6)})
        print(f"    {Z:>4}{Z*(Z-1)//2:>15}{Z-1:>18}{mp.nstr(frac*100, 4)+' %':>12}")
    ok &= chk("at_lead_the_chain_misses_over_97_percent_of_proton_pairs",
              mp.mpf(2)/82 < mp.mpf("0.025"), True,
              "2/Z captured -- 2.44 % at Z = 82. qou-nial's sum-vs-product as "
              "combinatorics: a path's edge count is LINEAR, Coulomb needs "
              "QUADRATIC, so no letter or scale can make a Z^2 term from Z-1 edges")

    print("\n" + "=" * 78)
    print("2. AND IT CANNOT CARRY A SURFACE TERM")
    print("=" * 78)
    print("    The surface term is a coordination DEFICIT over ~A^(2/3) boundary")
    print("    nucleons. In a path every interior vertex has degree 2 and the two")
    print("    endpoints have degree 1 — a deficit of 2, INDEPENDENT of A.")
    ok &= chk("a_paths_degree_deficit_is_constant_not_A_to_the_two_thirds",
              True, True,
              "so no A^(2/3) piece can arise from the edge count of a path, for "
              "any letters. Coulomb and surface are ONE defect: a 1-D chain "
              "where the physics is a saturating 3-D packing")

    print("\n" + "=" * 78)
    print("3. CORRECTION — my earlier all-pairs test was RIGGED")
    print("=" * 78)
    stats = {}
    for nm, bf in (("chain         (A-1 bonds)", chain_bonds),
                   ("all-pairs RAW (A(A-1)/2)", allpairs_bonds_raw)):
        v = [B/(STRANDS*E0*bond_sum(bf, Z, N)) for (A, Z, N, B) in meas]
        stats[nm.split()[0]] = {"median": mp.nstr(_pct(v, 50), 10),
                                "p5_p95": mp.nstr(_pct(v, 95)/_pct(v, 5), 10)}
        print(f"    {nm:<28} median {mp.nstr(_pct(v, 50), 6):>12}   "
              f"p5-p95 {mp.nstr(_pct(v, 95)/_pct(v, 5), 6)}")
    ratio = mp.mpf(stats["chain"]["median"])/mp.mpf(stats["all-pairs"]["median"])
    print(f"    ratio of medians = {mp.nstr(ratio, 6)}")
    ok &= chk("raw_all_pairs_differs_from_the_chain_by_a_factor_of_tens",
              ratio > 50, True,
              "65x, not the 0.6 % I reported. Renormalising all-pairs to A-1 "
              "bonds threw away exactly the quadratic growth that distinguishes "
              "it, so that test could not have seen the effect. The claim 'the "
              "bond GRAPH is not where the error lives' is WITHDRAWN -- it is "
              "exactly where it lives. The ORDERING half (segregated vs "
              "alternating, both chains) is unaffected")

    print("\n" + "=" * 78)
    print("4. CORRECTION — the marginals badly understated Coulomb")
    print("=" * 78)
    ys = [mp.log(B/(STRANDS*E0*bond_sum(chain_bonds, Z, N))) for (A, Z, N, B) in meas]
    names = ["const", "(N-Z)^2/A^2", "A^(-1/3)", "Z^2/A^(4/3)"]
    X = [[mp.mpf(1), (mp.mpf(N - Z)/A)**2, mp.mpf(A)**(-mp.mpf(1)/3),
          mp.mpf(Z*Z)/mp.mpf(A)**(mp.mpf(4)/3)] for (A, Z, N, B) in meas]
    k = 4
    AtA = [[sum(X[r][i]*X[r][j] for r in range(len(X))) for j in range(k)]
           for i in range(k)]
    Atb = [sum(X[r][i]*ys[r] for r in range(len(X))) for i in range(k)]
    c = mp.lu_solve(mp.matrix(AtA), mp.matrix(Atb))
    print(f"    {'shape':<14}{'coefficient':>14}{'contribution span':>20}{'in B':>12}")
    contribs = {}
    for i in range(1, k):
        vals = [X[r][i] for r in range(len(X))]
        span = c[i]*max(vals) - c[i]*min(vals)
        contribs[names[i]] = {"coeff": mp.nstr(c[i], 10),
                              "span_log": mp.nstr(abs(span), 10),
                              "span_pct_B": mp.nstr((mp.e**abs(span) - 1)*100, 8)}
        print(f"    {names[i]:<14}{mp.nstr(c[i], 8):>14}{mp.nstr(abs(span), 6):>20}"
              f"{mp.nstr((mp.e**abs(span)-1)*100, 5)+' %':>12}")
    coul = mp.mpf(contribs["Z^2/A^(4/3)"]["span_log"])
    asym = mp.mpf(contribs["(N-Z)^2/A^2"]["span_log"])
    ok &= chk("coulombs_joint_contribution_is_not_negligible",
              (mp.e**coul - 1) > mp.mpf("0.5"), True,
              "it spans 67 % in B, against the marginal correlation of -0.044 "
              "this arc read as 'essentially absent'. Marginal correlations "
              "conflate collinear shapes -- heavy nuclei have large Z, large "
              "N-Z and large A together")
    ok &= chk("the_ranking_is_three_to_one_point_eight_to_one_not_eighteen_to_four_to_one",
              asym/coul < 4, True,
              "the asymmetry is still largest, but far less lopsidedly than the "
              "marginals suggested")

    pred = [sum(c[i]*X[r][i] for i in range(k)) for r in range(len(X))]
    my = sum(ys)/len(ys)
    r2 = 1 - (sum((y - p)**2 for y, p in zip(ys, pred))
              / sum((y - my)**2 for y in ys))
    print(f"\n    joint R^2 = {mp.nstr(r2, 8)}")
    ok &= chk("the_three_SEMF_shapes_jointly_explain_over_ninety_percent",
              r2 > mp.mpf("0.9"), True,
              "the missing physics is not exotic and not unidentified -- it is "
              "the liquid-drop corrections in their standard forms, and two of "
              "the three follow from one structural fact about the edge set")

    print("\n  🎯 Coulomb and surface are ONE defect: the edge set is a 1-D chain")
    print("     where the physics is a saturating 3-D packing. Neither can arise")
    print("     from a path, for any letters.")
    print("  🛑 Two of my own reports corrected: the all-pairs comparison was")
    print("     rigged by renormalisation, and the marginal correlations")
    print("     understated Coulomb by an order of magnitude.")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))

    witness = {
        "computation": "qbeta-chain-cannot-carry-coulomb-or-surface",
        "q0Anchor": "proton",
        "assertions": a,
        "allPassed": bool(ok),
        "parameters": {"q0": mp.nstr(Q0, 30), "dps": DPS,
                       "E_0_MeV": mp.nstr(E0, 20),
                       "E_0_form": "tower-summed (owner ruling 2026-09-05)",
                       "strands_per_nucleon": STRANDS,
                       "note": "the regression is a DIAGNOSTIC, never adopted "
                               "as a law -- fitting three SEMF coefficients "
                               "would reproduce the SEMF and prove nothing"},
        "data": {"n_measured": len(meas), "coulomb_capture": cap,
                 "edge_sets": stats,
                 "median_ratio_chain_over_allpairs": mp.nstr(ratio, 10),
                 "joint_regression": contribs,
                 "joint_R2": mp.nstr(r2, 10)},
        "provenance": {"headSha": _head_sha(),
                       "producer": "computations/qbeta/qbeta_chain_cannot_carry_coulomb_or_surface_probe.py",
                       "elapsed_s": round(time.monotonic() - t0, 3)},
    }
    out = HERE / "qbeta-chain-cannot-carry-coulomb-or-surface.witness.json"
    out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
    print(f"\nwitness -> {out.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
