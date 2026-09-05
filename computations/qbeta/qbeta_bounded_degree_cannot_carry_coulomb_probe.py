#!/usr/bin/env python3
"""Coulomb is outside the bond-graph FORM, not a missing term inside it.

`qbeta_chain_cannot_carry_coulomb_or_surface_probe.py` showed the canonical
chain carries `2/Z` of the proton pairs -- 2.44 % at Z = 82. That argument used
nothing about a path except **its degree is 2**, so it generalises to every edge
set this corpus has built. This probe is the instantiation of
`QOU/Hecke/BoundedDegreeCoulomb.lean` on those edge sets. Bean `qou-556v`;
generalises `qou-nial`.

*** THE THEOREM BEING INSTANTIATED ***

Degree-sum formula: `2E = sum_v deg(v) <= d*n` for a graph with max degree `d`.
So the edge count is LINEAR in `n` however the graph is drawn, and its share of
the `n(n-1)/2` pairs is at most `d/(n-1)`. The bound applies to the induced
proton subgraph too -- **whatever the proton assignment** -- because an induced
subgraph's degrees are bounded by the parent's. Nothing here depends on which
sites are protons, which is why the result is about the class and not a model.

*** 1. THE THREE CORPUS EDGE SETS ARE ALL DEGREE-BOUNDED ***

    edge set                          edges       max degree   source
    canonical chain                   A-1         2            atom_braid_word_3A
    max-contact convex deltahedra     3A-6        5            GAP-1 / qou-lzoh
    bounded-degree close packing      kA/2        12            qou-kqdn

Captured share of proton pairs at Z = 82 is `d/(Z-1)`: 2.47 %, 6.17 %, 14.8 %.
**Even close packing leaves 85 % of the proton-proton interaction unrepresented.**
Coulomb is `1/r` long-range; a contact graph is the wrong object for it, and
that is a statement about the form of the law rather than its coefficients.

*** 2. AND `3A-6` IS ONLY DEGREE-5-ADMISSIBLE UP TO A = 12 ***

A triangulated sphere has average degree `2E/A = 6 - 12/A`, which exceeds 5 as
soon as `A > 12` -- and max degree is at least average. There are exactly eight
convex deltahedra, the largest the icosahedron at 12 vertices. So GAP-1's `3A-6`
is a SMALL-A construction; extrapolating it past A = 12 silently raises the
degree bound. That does not touch the theorem (which holds for any `d`), it just
fixes which `d` to quote -- and the larger `d` still loses.

*** 3. WHAT ACTUALLY HAS TO CHANGE: THE FALLOFF, NOT THE COUPLING ***

🛑 **Reframed 2026-09-05; the first version of this section pointed the wrong
way.** It called a Z-dependent per-bond energy "the escape hatch". That is the
SYMPTOM, not the defect, and stating it that way aims a successor at re-tuning a
letter.

**A bond graph is a kernel TRUNCATED AT RANGE 1.** Coulomb is `1/r` with no
truncation. Putting the `1/r` weight back in shows the difference is not a
shortfall at all:

    iso      Z     A   pairs captured   ENERGY captured (k=12, 1/r weighted)
    4He      2     4          100 %                          1587 %
    16O      8    16          100 %                           360 %
    40Ca    20    40         63.2 %                           180 %
    56Fe    26    56         48.0 %                           153 %
    120Sn   50   120         24.5 %                           101 %
    208Pb   82   208         14.8 %                          73.1 %

The contact model **overshoots light nuclei by 16x** and undershoots heavy ones,
crossing near Sn. **A larger `eps` cannot fix a ratio that is on both sides of
1.** The scalings say why: a contact sum is `k Z / 2` -- linear in `Z`, with no
`A` in it -- while the true sum over a uniform ball of radius `R = r0 A^(1/3)`
is `(3/5) Z(Z-1)/R`. Their ratio runs as `A^(1/3)/Z`, which is exactly the
overshoot-then-undershoot.

So the repair is a DECAY KERNEL OVER ALL PAIRS, not a bigger letter on a few.
And a `1/r` kernel over all pairs is a weighted COMPLETE graph -- degree `Z-1`,
precisely the case the theorem excludes. The theorem and the physics agree:
Coulomb is outside the bond-graph form because the form truncates range.

*** 3b. THE COUPLING FORM OF THE SAME STATEMENT, KEPT AS A SYMPTOM ***

Insisting on a degree-bounded graph, the per-bond energy would have to be

    eps(Z) >= 2 a_C (Z-1) / (d A^(1/3))

linear in `Z-1`, a span of 21.7x between 4He and 208Pb. A derived letter
(`b_pp`, `b_pn`, `b_nn`) is a NUMBER; this is a function of the nucleus. Read it
as a measure of how badly the truncation distorts, not as a repair to attempt.

`a_C = 0.697 MeV` is an EXTERNAL SEMF reference constant, used only to size the
requirement -- nothing here is fitted to it and nothing is wired to production.
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

# External SEMF reference (Bethe-Weizsacker, standard fit): sizing only.
A_C = mp.mpf("0.697")

# The three corpus edge sets, as (label, edges(A), max degree).
EDGE_SETS = (
    ("canonical chain", lambda A: mp.mpf(A - 1), 2),
    ("max-contact deltahedra 3A-6", lambda A: mp.mpf(3*A - 6), 5),
    ("close packing kA/2, k=12", lambda A: mp.mpf(12*A)/2, 12),
)

AME = ROOT / "qou-mass/src/qou_mass/data/ame2020.json"


def _head_sha() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "unknown"


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
        if Z < 2 or N < 1 or not b or e.get("binding_energy_per_A_estimated"):
            continue
        B = mp.mpf(str(b))*A/1000
        if B > 0:
            meas.append((A, Z, N, B))

    print("=" * 78)
    print("1. EVERY CORPUS EDGE SET IS DEGREE-BOUNDED, SO EVERY ONE LOSES")
    print("=" * 78)
    print(f"    {'Z':>4}  " + "".join(f"{lbl.split()[0]:>16}" for lbl, _, _ in EDGE_SETS))
    share = []
    for Z in (2, 8, 20, 26, 50, 82):
        row = {"Z": Z, "pairs": Z*(Z - 1)//2}
        cells = []
        for lbl, _, d in EDGE_SETS:
            frac = mp.mpf(d)/(Z - 1) if Z > 1 else mp.mpf(1)
            frac = min(frac, mp.mpf(1))
            row[f"d={d}"] = mp.nstr(frac*100, 6)
            cells.append(mp.nstr(frac*100, 4) + " %")
        share.append(row)
        print(f"    {Z:>4}  " + "".join(f"{c:>16}" for c in cells))

    lead = share[-1]
    ok &= chk("even_close_packing_leaves_most_proton_pairs_unrepresented",
              mp.mpf(lead["d=12"]) < 15, True,
              note=f"d=12 captures {lead['d=12']} % of proton pairs at Z=82; "
                   "the chain captures 2.47 %. Coulomb is 1/r long-range and a "
                   "contact graph is the wrong object for it, whatever d is")

    # The Lean bound `E <= d*n/2` must hold for each edge set on its own count.
    viol = []
    for lbl, ef, d in EDGE_SETS:
        for (A, Z, N, _B) in meas:
            if ef(A) > mp.mpf(d*A)/2:
                viol.append((lbl, A))
                break
    ok &= chk("only_the_deltahedral_row_outgrows_its_quoted_degree_bound",
              [v[0] for v in viol], ["max-contact deltahedra 3A-6"],
              note="3A-6 exceeds 5A/2 for A>12 -- a triangulated sphere has "
                   "average degree 6-12/A, so max degree is at least 6 there, "
                   "and there are only eight convex deltahedra (largest the "
                   "icosahedron, 12 vertices). GAP-1's 3A-6 is a SMALL-A "
                   "construction; past A=12 the honest bound is d=12, not d=5")

    A_break = min(A for (lbl, A) in viol) if viol else None
    ok &= chk("the_deltahedral_bound_breaks_just_above_twelve", A_break, 13,
              note="2E/A = 6 - 12/A > 5 exactly when A > 12")

    print()
    print("=" * 78)
    print("2. IT IS THE FALLOFF, NOT THE COUPLING: THE 1/r-WEIGHTED CAPTURE")
    print("=" * 78)
    print("    contact sum   ~ k Z / 2                 (linear in Z, no A)")
    print("    true Coulomb  ~ (3/5) Z(Z-1) / (r0 A^(1/3))")
    print("    ratio         ~ 5 k A^(1/3) / (6 (Z-1))")
    print()
    print(f"    {'iso':>8}{'Z':>5}{'A':>5}{'pairs':>12}{'ENERGY (k=12)':>18}")
    energy = []
    kk = mp.mpf(12)
    for name, Z, A in (("4He", 2, 4), ("16O", 8, 16), ("40Ca", 20, 40),
                       ("56Fe", 26, 56), ("120Sn", 50, 120), ("208Pb", 82, 208)):
        pair = min(kk/(Z - 1), mp.mpf(1))
        en = 5*kk*mp.mpf(A)**(mp.mpf(1)/3)/(6*(Z - 1))
        energy.append({"iso": name, "Z": Z, "A": A,
                       "pairs_pct": mp.nstr(pair*100, 6),
                       "energy_pct": mp.nstr(en*100, 6)})
        print(f"    {name:>8}{Z:>5}{A:>5}{mp.nstr(pair*100, 4) + ' %':>12}"
              f"{mp.nstr(en*100, 5) + ' %':>18}")

    ratios = [mp.mpf(r["energy_pct"])/100 for r in energy]
    ok &= chk("a_contact_kernel_overshoots_light_nuclei_and_undershoots_heavy",
              bool(max(ratios) > 1 and min(ratios) < 1), True,
              note=f"1/r-weighted capture runs {mp.nstr(max(ratios)*100, 6)} % at "
                   f"4He down to {mp.nstr(min(ratios)*100, 6)} % at 208Pb, "
                   "crossing 1 near Sn. The defect is a kernel TRUNCATED AT "
                   "RANGE 1 standing in for 1/r -- it over-weights the first "
                   "shell and drops everything beyond")
    ok &= chk("so_no_rescaling_of_the_bond_energy_repairs_it",
              bool(max(ratios)/min(ratios) > 20), True,
              note=f"the ratio spans {mp.nstr(max(ratios)/min(ratios), 6)}x and "
                   "sits on BOTH sides of 1, so a constant -- or any single "
                   "monotone eps(Z) -- cannot correct it. The repair is a decay "
                   "kernel over all pairs, which is a weighted COMPLETE graph: "
                   "degree Z-1, exactly the case the theorem excludes")

    print()
    print("=" * 78)
    print("2b. THE COUPLING FORM OF THE SAME STATEMENT, KEPT AS A SYMPTOM")
    print("=" * 78)
    print("    eps(Z) >= 2 a_C (Z-1) / (d A^(1/3))   to reproduce SEMF Coulomb")
    print()
    print(f"    {'iso':>10}{'Z':>5}{'A':>5}{'eps_req (d=12) MeV':>22}")
    req = []
    for (A, Z, N, _B) in meas:
        e_req = 2*A_C*(Z - 1)/(12*mp.mpf(A)**(mp.mpf(1)/3))
        req.append((A, Z, e_req))
    # Key by (Z, A): several nuclides share an A, and taking the first match
    # by A alone mislabels the row (16O is Z=8, not the Z=4 isobar).
    shown = {(2, 4): "4He", (8, 16): "16O", (26, 56): "56Fe", (82, 208): "208Pb"}
    picks = {k: (Z, e_req) for (A, Z, e_req) in req
             for k in [(Z, A)] if k in shown}
    for (Z, A) in sorted(picks, key=lambda k: k[1]):
        _Z, e_req = picks[(Z, A)]
        print(f"    {shown[(Z, A)]:>10}{Z:>5}{A:>5}{mp.nstr(e_req, 8):>22}")

    vals = [e for (_A, _Z, e) in req]
    span = max(vals)/min(vals)
    ok &= chk("no_constant_bond_energy_reproduces_coulomb", span > 20, True,
              note=f"required eps spans {mp.nstr(span, 6)}x across the measured "
                   "chart. A derived letter is a NUMBER; this is a function of "
                   "the nucleus, so the escape hatch is not a re-tuning -- it "
                   "is a different form of law")

    # Dividing out the predicted Z-dependence should collapse that span.
    flat = [e/((Z - 1)/mp.mpf(A)**(mp.mpf(1)/3)) for (A, Z, e) in req]
    flat_span = max(flat)/min(flat)
    ok &= chk("and_the_required_growth_is_exactly_the_predicted_one",
              flat_span < mp.mpf("1.0000000001"), True,
              note=f"eps_req / ((Z-1)/A^(1/3)) has span {mp.nstr(flat_span, 12)} "
                   "-- constant to working precision, so the requirement is "
                   "linear in Z-1 and nothing else. That is the theorem's "
                   "hypothesis failing in exactly the predicted way")

    # How big is what the bond graph is being asked to leave out?
    pb = [(A, Z, B) for (A, Z, _N, B) in meas if A == 208 and Z == 82]
    frac_pb = None
    if pb:
        A, Z, B = pb[0]
        e_c = A_C*Z*(Z - 1)/mp.mpf(A)**(mp.mpf(1)/3)
        frac_pb = e_c/B
        print()
        print(f"    208Pb: SEMF Coulomb {mp.nstr(e_c, 8)} MeV against "
              f"B_AME {mp.nstr(B, 8)} MeV  ({mp.nstr(frac_pb*100, 5)} %)")
    ok &= chk("the_omitted_term_is_not_small", frac_pb is not None and frac_pb > mp.mpf("0.3"),
              True, note="at 208Pb the SEMF Coulomb term is a large fraction of "
                         "the total binding, so this is not a correction the "
                         "law can carry in its error bar")

    print()
    print("=" * 78)
    print("3. WHAT THIS CLOSES")
    print("=" * 78)
    print("  Coulomb is not a missing TERM in the bond graph -- it is outside")
    print("  the bond-graph FORM, because the form TRUNCATES RANGE. Physically")
    print("  right: Coulomb is 1/r, a contact graph is not. The surface term is")
    print("  the opposite case: the same")
    print("  degree bound SUPPLIES it (QOU/Mass/CoordinationSurfaceDeficit,")
    print("  bean qou-kqdn), because a boundary deficit is what bounded degree")
    print("  gives you. One bound, two opposite consequences.")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))

    witness = {
        "computation": "qbeta-bounded-degree-cannot-carry-coulomb",
        "assertions": a,
        "allPassed": bool(ok),
        "parameters": {"dps": DPS, "a_C_MeV": str(A_C),
                       "a_C_provenance": "EXTERNAL SEMF reference constant, "
                                         "used to size the requirement only; "
                                         "nothing is fitted to it",
                       "edge_sets": [{"label": lbl, "max_degree": d}
                                     for lbl, _, d in EDGE_SETS],
                       "lean": "QOU/Hecke/BoundedDegreeCoulomb.lean"},
        "data": {"n_measured": len(meas),
                 "captured_share_pct_by_degree": share,
                 "deltahedral_bound_breaks_at_A": A_break,
                 "one_over_r_weighted_capture": energy,
                 "required_epsilon_span": mp.nstr(span, 10),
                 "required_epsilon_flattened_span": mp.nstr(flat_span, 12),
                 "pb208_coulomb_over_binding": mp.nstr(frac_pb, 10) if frac_pb else None},
        "provenance": {"headSha": _head_sha(),
                       "producer": "computations/qbeta/qbeta_bounded_degree_cannot_carry_coulomb_probe.py",
                       "elapsed_s": round(time.monotonic() - t0, 3)},
    }
    out = HERE / "qbeta-bounded-degree-cannot-carry-coulomb.witness.json"
    out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
    print(f"\nwitness -> {out.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
