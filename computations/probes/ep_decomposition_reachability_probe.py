#!/usr/bin/env python3
"""
Reachability of the Epstein–Penner route across the live nuclide knot dictionary.

Bean `qou-eptr`, issue #6941. The owner brought a proposal to source the binding
gap's one open piece — the irreducibly many-body term, measured `b₃ = +1.4262`
MeV against a model value of exactly `0` — from the canonical (Epstein–Penner)
ideal decomposition of a knot complement. A cell decomposition is attractive for
that piece because it is extensive (a sum over cells), 4-body per cell (so not
pair-local, and `CrossingModelPairLocality.b3_eq_zero_of_pairLocal` proves
pair-locality is exactly what forces the model's zero), canonical (so no
selection against the target), and bounded-degree.

An Epstein–Penner decomposition exists only for a COMPLETE FINITE-VOLUME
HYPERBOLIC manifold. Before any construction is built on the route, this probe
measures whether it reaches anything: for every atom in the live per-atom knot
dictionary, is the assigned complement hyperbolic, and — the question that
actually decides the route — HOW MANY DISTINCT MANIFOLDS does the dictionary
use?

The second question is decisive because an Epstein–Penner decomposition is a
function of the MANIFOLD. Every quantity derived from it — the cell count, the
volume, the cusp shape, the Pachner distance to any other triangulation, the
3d-index — takes the same value on every atom assigned the same complement. If
the dictionary maps many atoms with different binding energies onto one
manifold, then no function of the Epstein–Penner decomposition alone can
separate them, whatever that function is.

WHAT THIS PROBE DOES NOT CLAIM. The exclusion it measures is about the knot the
DICTIONARY assigns, not about the route in general. `classify_nuclear_knot` is a
four-branch dispatch on the mass number `A` alone which discards the braid word
entirely, and it has exactly one consumer in the tree. The live binding law
attaches to the braid word (a `tr_M` ratio), a strictly finer object. So the
honest reading is conditional: Epstein–Penner-of-the-dictionary-knot is
excluded; Epstein–Penner-of-the-actual-per-atom-closure is UNTESTED, and testing
it would first require identifying that closure, which the corpus does not
currently do.

The deuteron is handled separately and does not depend on the dictionary being
right. The dictionary calls it a SATELLITE knot. Thurston's trichotomy says a
knot is exactly one of torus, satellite, or hyperbolic, so a satellite complement
admits no complete hyperbolic structure and has no Epstein–Penner decomposition —
derived from the classification, not guessed, and independent of the 2026-08-29
owner ruling that puts the deuteron on a `Vol = 0` braid closure. The two agree.

Precision: every binding energy is carried as `mpmath.mpf` from its string form;
counts and set cardinalities are exact integers. No float64 arithmetic, no fit,
no `q`, no Markov parameter, no anchor (`q0Anchor: independent`).

-- Ref: [manuscript] docs/audits/2026-09-05-binding-gap-groupoids-derived-categories-full-tower.md §1.2
-- Ref: [manuscript] docs/audits/2026-08-29-deuteron-knot-owner-decision.md
-- Ref: [thurston1982] https://doi.org/10.1090/S0273-0979-1982-15003-0
--      (the geometrisation trichotomy: torus | satellite | hyperbolic)
-- Ref: [epstein1988] https://doi.org/10.4310/jdg/1214441650
--      (Euclidean decompositions of noncompact hyperbolic manifolds)
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

# --- path bootstrap MUST precede `import _path_bridge` (AGENTS.md: a script in a
# --- cluster subdir has sys.path[0] set to its own directory, so the bridge is
# --- unresolvable until computations/ is on the path).
_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

import knot_volumes as kv  # noqa: E402
import sw_hyperbolicity_gate as gate  # noqa: E402
from _precision import COMPUTE_DPS  # noqa: E402

# The dictionary's coarse labels -> canonical names in the hyperbolicity registry.
# 'satellite' is deliberately absent: it is resolved by the trichotomy below,
# not by a registry lookup, because the registry refuses to guess and a satellite
# knot is not a named canonical knot.
LABEL_TO_CANONICAL = {
    "trivial": "unknot",
    "figure-eight": "4_1",
    "Borromean": "L6a4",
}

# Thurston's trichotomy: a knot is exactly one of torus, satellite, hyperbolic.
# So a satellite complement carries no complete hyperbolic structure, hence no
# Epstein-Penner decomposition. This is derived, not a registry entry.
NON_HYPERBOLIC_BY_TRICHOTOMY = {"satellite"}


def load_atoms() -> list[dict]:
    """Per-atom rows of the live knot dictionary.

    Read from `hadron-knot-table.witness.json`. That witness is known to carry
    the RETIRED muon q0 pin in its `q0Value` field (AGENTS.md records it as the
    one such file left on main); every field this probe reads — `knot_type`,
    `Z`, `N`, `A`, `B_MeV` — is produced by `classify_nuclear_knot` and the
    binding computation and is not a function of that field's staleness for the
    purposes of the count below, which is over labels and set cardinalities.
    """
    path = _COMP / "hadron-knot-table.witness.json"
    if not path.exists():
        raise FileNotFoundError(f"missing knot dictionary witness: {path}")
    return json.loads(path.read_text())["data"]["atoms"]


def classify_is_function_of_A_only() -> bool:
    """Verify the dictionary's classifier depends on Z and N only through A.

    Run it over a grid and check every (Z, N) with the same sum agrees. This is
    what makes the constancy argument below a statement about the dictionary
    rather than about one witness run.
    """
    from hecke_core_legacy import classify_nuclear_knot

    by_A: dict[int, set] = {}
    for Z in range(0, 30):
        for N in range(0, 34):
            A = Z + N
            _alpha, name, hyp = classify_nuclear_knot(Z, N)
            by_A.setdefault(A, set()).add((name, hyp))
    return all(len(v) == 1 for v in by_A.values())


def main() -> int:
    mp.mp.dps = COMPUTE_DPS

    atoms = load_atoms()
    rows = []
    for a in atoms:
        label = str(a["knot_type"])
        if label in NON_HYPERBOLIC_BY_TRICHOTOMY:
            canonical, hyp, why = None, False, "Thurston trichotomy: satellite is not hyperbolic"
        else:
            canonical = LABEL_TO_CANONICAL[label]
            hyp = gate.is_hyperbolic(canonical)
            why = "sw_hyperbolicity_gate registry"
        rows.append({
            "name": a["name"], "Z": a["Z"], "N": a["N"], "A": a["A"],
            "label": label, "canonical": canonical, "hyperbolic": hyp,
            "basis": why, "B_MeV": mp.mpf(str(a["B_MeV"])),
        })

    hyp_rows = [r for r in rows if r["hyperbolic"]]
    distinct_manifolds = sorted({r["canonical"] for r in hyp_rows})

    # Per-class binding spread. The decisive statistic: an Epstein-Penner
    # invariant is CONSTANT on a class (it is a function of the manifold), so a
    # class whose binding energies differ cannot be separated by one.
    classes: dict[str, list] = {}
    for r in hyp_rows:
        classes.setdefault(r["canonical"], []).append(r)

    class_stats = {}
    for cname, members in classes.items():
        bs = [m["B_MeV"] for m in members if m["B_MeV"] != 0]
        stat = {"n_atoms": len(members),
                "atoms": [m["name"] for m in members],
                "n_nonzero_B": len(bs)}
        if bs:
            bmin, bmax = min(bs), max(bs)
            stat["B_min_MeV"] = mp.nstr(bmin, 12)
            stat["B_max_MeV"] = mp.nstr(bmax, 12)
            stat["B_ratio_max_over_min"] = mp.nstr(bmax / bmin, 12)
            stat["_ratio"] = bmax / bmin
        class_stats[cname] = stat

    borro = class_stats.get("L6a4", {})
    borro_ratio = borro.get("_ratio", mp.mpf(0))

    deuteron = next((r for r in rows if r["A"] == 2), None)
    n_nonzero_B = sum(1 for r in rows if r["B_MeV"] != 0)
    n_nonzero_B_hyp = sum(1 for r in rows if r["B_MeV"] != 0 and r["hyperbolic"])

    tol = mp.mpf(10) ** (-(COMPUTE_DPS - 5))
    checks = [
        ("deuteron_is_satellite_hence_no_EP",
         deuteron is not None and deuteron["label"] == "satellite"
         and not deuteron["hyperbolic"],
         "A=2 is labelled satellite; Thurston's trichotomy makes it "
         "non-hyperbolic, so no Epstein-Penner decomposition exists for it"),
        ("all_A_ge_3_are_hyperbolic",
         all(r["hyperbolic"] for r in rows if r["A"] >= 3),
         "every atom with A>=3 in the dictionary has a hyperbolic complement, "
         "so the route is not blocked above the deuteron"),
        ("distinct_hyperbolic_manifolds_is_two",
         len(distinct_manifolds) == 2,
         "the whole dictionary uses exactly two hyperbolic manifolds (4_1, L6a4)"),
        ("borromean_class_holds_13_atoms",
         class_stats.get("L6a4", {}).get("n_atoms") == 13,
         "13 of 19 atoms are assigned the SAME complement L6a4"),
        ("borromean_class_binding_spread_exceeds_1e6",
         borro_ratio > mp.mpf(10) ** 6,
         "binding varies by more than a factor 1e6 inside the single class on "
         "which every Epstein-Penner invariant is constant"),
        ("classifier_depends_on_A_only",
         classify_is_function_of_A_only(),
         "classify_nuclear_knot(Z,N) factors through A=Z+N over a 30x34 grid, "
         "so the dictionary discards the braid word"),
        ("vol_L6a4_eq_8_catalan",
         abs(gate.vol_component("L6a4") - 8 * kv.CATALAN_G_MPF) < tol,
         "registry sanity: Vol(L6a4) = 8*Catalan"),
        ("vol_4_1_eq_2_cl2_pi_over_3",
         abs(gate.vol_component("4_1")
             - 2 * mp.clsin(2, mp.pi / 3)) < tol,
         "registry sanity: Vol(4_1) = 2*Cl_2(pi/3) "
         "(NOT twice Catalan; Cl_2(pi/2) is a different number)"),
        ("catalan_is_not_cl2_pi_over_3",
         abs(kv.CATALAN_G_MPF - mp.clsin(2, mp.pi / 3)) > mp.mpf("0.05"),
         "guard on the Lambda-vs-Cl_2 confusion the dialog made: Catalan's "
         "constant Cl_2(pi/2) and Cl_2(pi/3) differ by ~0.099"),
    ]

    print(f"{'atom':10} {'A':>3}  {'label':13} {'manifold':9} {'hyp':>5}  B_MeV")
    for r in rows:
        print(f"{r['name']:10} {r['A']:>3}  {r['label']:13} "
              f"{str(r['canonical']):9} {str(r['hyperbolic']):>5}  "
              f"{mp.nstr(r['B_MeV'], 10)}")
    print()
    print(f"atoms                        : {len(rows)}")
    print(f"with non-zero binding        : {n_nonzero_B}")
    print(f"  of those, hyperbolic       : {n_nonzero_B_hyp}")
    print(f"distinct hyperbolic manifolds: {len(distinct_manifolds)} {distinct_manifolds}")
    for cname, st in class_stats.items():
        print(f"  {cname}: {st['n_atoms']} atoms, "
              f"B in [{st.get('B_min_MeV', '-')}, {st.get('B_max_MeV', '-')}], "
              f"ratio {st.get('B_ratio_max_over_min', '-')}")
    print()

    ok = 0
    for name, cond, desc in checks:
        print(f"[{'PASS' if cond else 'FAIL'}] {name}: {desc}")
        ok += 1 if cond else 0
    print(f"\n{ok}/{len(checks)} assertions")

    try:
        from qou_substrate.witness import WitnessBuilder
    except Exception as e:  # noqa: BLE001
        print(f"(witness not emitted: {e!r})")
        return 0 if ok == len(checks) else 1

    wb = WitnessBuilder("ep-decomposition-reachability", engine="mpmath",
                        _script_path=__file__)
    for name, cond, desc in checks:
        wb.add_assertion(name, computed="1" if cond else "0", expected="1",
                         tolerance="0.5", source=desc)
    wb.add_data("atoms", [
        {k: (mp.nstr(v, 12) if isinstance(v, mp.mpf) else v)
         for k, v in r.items()} for r in rows])
    wb.add_data("distinct_hyperbolic_manifolds", distinct_manifolds)
    wb.add_data("class_stats", {
        c: {k: v for k, v in st.items() if not k.startswith("_")}
        for c, st in class_stats.items()})
    wb.add_data("n_atoms", len(rows))
    wb.add_data("n_atoms_nonzero_binding", n_nonzero_B)
    wb.add_data("n_atoms_nonzero_binding_hyperbolic", n_nonzero_B_hyp)
    wb.add_data("classifier_consumers_in_tree",
                ["computations/hadron_knot_table.py"])
    wb.add_data("scope",
                "Excludes an Epstein-Penner invariant of the DICTIONARY-assigned "
                "knot as a source of the A-dependent shape residual, because "
                "such an invariant is constant on a class whose binding spans "
                "more than 1e6. Does NOT exclude an Epstein-Penner invariant of "
                "the actual per-atom braid closure, which is untested and would "
                "first require identifying that closure.")
    wb.save({"q0Anchor": "independent",
             "q0AnchorReason": "pure topology: no q, no Markov parameter, no anchor"})
    print("witness written")
    return 0 if ok == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
