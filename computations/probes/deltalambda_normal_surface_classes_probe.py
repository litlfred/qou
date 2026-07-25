#!/usr/bin/env python3
"""deltalambda_normal_surface_classes_probe.py — exact S3 orbit / stabilizer structure
of the 52 vertex spun-normal surfaces of the Borromean triangulation (idea B3):
which surface classes can carry a (Z,N)-asymmetric collective binding term?

Executes the pn-capability leg of idea B3 of
docs/audits/2026-07-18-uploaded-papers-binding-mass-gap-ideas.md, made concrete by
the W9 census (borromean_angle_structure_lp_probe.py, witness
borromean-angle-structure-lp-probe.witness.json): all 52 vertex spun-normal
surfaces of the SnapPy L6a4 triangulation of B3 with exact (chi, boundary-slope,
cusps-touched) data.

MOTIVATION (attack-map 2026-07-18 s2.1 + s3): the Slater-antisymmetrizer trace is
pn-blind by proved invariant (depends on A = Z + N only), so the collective
(non-additive) magnitude term must come from an object that CAN distinguish (Z,N)
— i.e. that decorates the three cusps (strands) of B3 asymmetrically. The vertex
normal-surface classes carry a per-cusp boundary grading [dS] in H1(dM;Z) = Z^6;
this probe computes EXACTLY which classes distinguish cusps asymmetrically, the
S3 orbit structure, and the stabilizer of every class.

WHAT IS COMPUTED (all exact integer / Fraction arithmetic; no q0, no fit):
  stage 1  re-derive the 52-surface census via the same SnapPy machinery as W9
           (functions imported from the sibling probe; m004 convention re-pin
           included), and assert EXACT agreement with W9's committed witness
           (per-index quad vectors, boundary slopes, chi, all summary counts).
  stage 2  symmetry bookkeeping: 48 isometries realizing the full S3 on cusps
           (SnapPy is_isometric_to return_isometries), the order-8 sign kernel K
           (isometries with trivial cusp permutation), and the 16 combinatorial
           automorphisms of THIS triangulation (only a Z2 of the S3 — so the S3
           statements below are made at the PERIPHERAL level, on boundary-slope
           classes, not on quad vectors; recorded honestly in the witness).
  stage 3  the peripheral action: each isometry acts on H1(dM;Z) = Z^6 by its
           cusp permutation + per-cusp 2x2 cusp maps. The convention (matrix vs
           transpose vs inverse) is pinned EMPIRICALLY by requiring the census
           slope multiset be preserved by all 48 isometries; every passing
           convention is recorded.
  stage 4  class structure: the 52 surfaces project to 46 distinct
           (slope, chi) classes (6 pure-longitude classes are doubled). The
           isometry group acts on the classes; K-orbits ("unsigned peripheral
           classes") are computed; S3 = G/K acts on K-orbits (well-definedness
           machine-verified); S3 orbits + exact stabilizers computed; the
           orbit-stabilizer identity |orbit|*|stab| = 6 asserted for every orbit.
  stage 5  pn-capability tables: cusp-support table (4/4/4, 8/8/8, 16), the
           refined orbit/stabilizer table, the count of asymmetric classes, and
           the H-orbit count for H = the transposition stabilizer of a
           pnn-labeling (the exact DOF count of an H-equivariant weighting —
           the number the audit doc's consequence (b) consumes).
  stage 6  non-additivity data: per-surface tetrahedra-touched counts (a vertex
           surface spans many tetrahedra — not a per-pair bond object) and an
           explicit pairwise-sum extremality check (no census class is the
           quad-vector sum of two census classes).

SCOPE (STRICT): structure-hunt tier; audit-only; scope-(a); NO FIT; nothing
wired to production. No number here is compared to any binding energy, to the
1.22x mirror split, or to any q0 evaluation. Pure integer topology/combinatorics.

Audit doc: docs/audits/2026-07-24-deltalambda-normal-surface-collective-candidate.md
"""
from __future__ import annotations

import json
import sys
import time
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: E402, F401
from witness_base import WitnessBuilder  # noqa: E402

import borromean_angle_structure_lp_probe as w9  # noqa: E402  (sibling probe machinery)

T0 = time.time()


def log(msg: str) -> None:
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


W9_WITNESS = Path(__file__).resolve().parent / \
    "borromean-angle-structure-lp-probe.witness.json"

S3_ELEMENTS = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]


# ---------------------------------------------------------------------------
# Peripheral action of an isometry on a Z^6 slope vector
# ---------------------------------------------------------------------------

def _mat2(m):
    return [[int(m[r, c]) for c in range(2)] for r in range(2)]


def _inv2(m):
    a, b, c, d = m[0][0], m[0][1], m[1][0], m[1][1]
    det = a * d - b * c
    assert det in (1, -1), f"non-unimodular cusp map {m}"
    return [[d // det, -b // det], [-c // det, a // det]]


def _transpose2(m):
    return [[m[0][0], m[1][0]], [m[0][1], m[1][1]]]


def apply_iso(slopes, perm, mats, conv):
    """Map a Z^6 slope vector under (cusp permutation, per-cusp 2x2 maps)."""
    out = [0] * 6
    for h in range(3):
        p, q = slopes[2 * h], slopes[2 * h + 1]
        m = mats[h]
        if conv == "transpose":
            m = _transpose2(m)
        elif conv == "inverse":
            m = _inv2(m)
        elif conv == "inverse-transpose":
            m = _transpose2(_inv2(m))
        # else "matrix": as given
        p2 = m[0][0] * p + m[0][1] * q
        q2 = m[1][0] * p + m[1][1] * q
        out[2 * perm[h]] = p2
        out[2 * perm[h] + 1] = q2
    return tuple(out)


def support_of(slopes):
    return tuple(h for h in range(3)
                 if (slopes[2 * h], slopes[2 * h + 1]) != (0, 0))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    print("=" * 74)
    print(" S3 orbit / stabilizer structure of the 52 vertex spun-normal surfaces")
    print(" of B3 (L6a4) — pn-capability classification for the collective term")
    print(" structure-hunt tier / audit-only / scope-(a) / no fit — see docstring")
    print("=" * 74)

    try:
        import snappy
    except ImportError:
        print("WALL: SnapPy is not importable — cannot re-derive the census from "
              "source; refusing to hand-copy it (anti-guessing rule).")
        return 2

    if not W9_WITNESS.exists():
        print(f"WALL: W9 witness {W9_WITNESS.name} not found — the agreement gate "
              "cannot run.")
        return 2
    w9_data = json.loads(W9_WITNESS.read_text())["data"]
    w9_surf = w9_data["vertex_surfaces"]

    # ---------------- stage 1: re-derive the census, gate on W9 -------------
    log("stage 1: m004 convention re-pin (same machinery as W9)")
    m004 = w9.validate_m004(snappy)
    conv_ok = (m004["conv_ok"] and m004["chi_ok"]
               and tuple(m004["sigma"]) == (1, 2, 0) and m004["eps"] == -1)
    log(f"  re-pinned sigma={m004['sigma']}, eps={m004['eps']} "
        f"(W9 frozen: (1,2,0), -1) -> {'OK' if conv_ok else 'MISMATCH'}")
    if not conv_ok:
        return 1
    SIGMA, EPS = tuple(m004["sigma"]), m004["eps"]

    log("stage 1: L6a4 census re-derivation (SnapPy normal_surfaces + Prop A.3)")
    M, N, r, edge_rows, cusp_rows = w9.gluing(snappy, "L6a4")
    A_eq, b_eq = w9.ga_equalities(N, edge_rows)
    x0, basis, _rank = w9.ga_general_solution(A_eq, b_eq)
    alphas = [w9.random_ga(x0, basis, sd) for sd in range(3)]

    surfs = M.normal_surfaces()
    table = []
    all_indep = True
    for s in surfs:
        qv = [w9.exact_int(v) for v in s.quad_vector()]
        sl = tuple(w9.exact_int(v) for v in s.boundary_slopes())
        vals = {w9.chi_pairing(qv, list(sl), a, N, r, cusp_rows, SIGMA, EPS)
                for a in alphas}
        all_indep &= (len(vals) == 1)
        chi = vals.pop()
        ntets = sum(1 for j in range(N) if any(qv[3 * j + t] for t in range(3)))
        table.append({"index": s._index, "quad_vector": qv,
                      "boundary_slopes": list(sl), "chi": chi,
                      "support": support_of(sl), "n_tets_touched": ntets,
                      "total_quads": sum(qv)})
    n_surf = len(table)
    log(f"  {n_surf} vertex surfaces; Prop A.3 alpha-independent: {all_indep}")

    # exact agreement with the committed W9 witness, per index
    w9_table = w9_surf["table"]
    per_index_ok = (len(w9_table) == n_surf) and all(
        t["quad_vector"] == wt["quad_vector"]
        and t["boundary_slopes"] == wt["boundary_slopes"]
        and str(t["chi"]) == wt["chi"]
        for t, wt in zip(table, w9_table))
    chi_dist = Counter(str(t["chi"]) for t in table)
    quads_dist = Counter(t["total_quads"] for t in table)
    cusp_pattern = Counter(t["support"] for t in table)
    pat_str = {('+'.join(str(c) for c in k) if k else 'none'): v
               for k, v in sorted(cusp_pattern.items())}
    summaries_ok = (
        n_surf == w9_surf["count"]
        and dict(chi_dist) == w9_surf["chi_distribution"]
        and {str(k): v for k, v in sorted(quads_dist.items())}
        == w9_surf["total_quads_distribution"]
        and pat_str == w9_surf["cusps_touched_pattern"])
    log(f"  W9 agreement: per-index table {per_index_ok}, summaries {summaries_ok}")
    log(f"  cusps-touched: {pat_str}; chi: {dict(chi_dist)}")
    support_table_ok = (
        cusp_pattern[(0,)] == cusp_pattern[(1,)] == cusp_pattern[(2,)] == 4
        and cusp_pattern[(0, 1)] == cusp_pattern[(0, 2)]
        == cusp_pattern[(1, 2)] == 8
        and cusp_pattern[(0, 1, 2)] == 16)

    # cross-tab: support size x chi
    supp_chi = Counter((len(t["support"]), int(t["chi"])) for t in table)
    log(f"  (|support|, chi) cross-tab: "
        f"{ {f'{k[0]}-cusp chi={k[1]}': v for k, v in sorted(supp_chi.items())} }")

    # ---------------- stage 2: symmetry bookkeeping -------------------------
    log("stage 2: isometries + combinatorial automorphisms")
    isos = M.is_isometric_to(M, return_isometries=True)
    iso_data = []
    for g in isos:
        perm = tuple(g.cusp_images())
        mats = [_mat2(m) for m in g.cusp_maps()]
        iso_data.append((perm, mats))
    perms_realized = sorted({p for p, _ in iso_data})
    kernel = [(p, m) for p, m in iso_data if p == (0, 1, 2)]
    combi = M.isomorphisms_to(M)
    combi_perms = sorted({tuple(i.cusp_images()) for i in combi})
    sym_ok = (len(isos) == 48 and perms_realized == S3_ELEMENTS
              and len(kernel) == 8)
    combi_ok = (len(combi) == 16 and combi_perms == [(0, 1, 2), (2, 1, 0)])
    log(f"  isometries: {len(isos)}, cusp perms {perms_realized} "
        f"(full S3: {perms_realized == S3_ELEMENTS}); sign kernel |K| = {len(kernel)}")
    log(f"  combinatorial automorphisms: {len(combi)}, cusp perms {combi_perms} "
        f"(only Z2 — hence S3 statements below live on peripheral classes)")

    # ---------------- stage 3: pin the peripheral-action convention ---------
    log("stage 3: peripheral-action convention (empirical pin, all 48 isometries)")
    slope_multiset = Counter(tuple(t["boundary_slopes"]) for t in table)
    passing_convs = []
    for conv in ("matrix", "transpose", "inverse", "inverse-transpose"):
        ok = True
        for perm, mats in iso_data:
            img = Counter(apply_iso(tuple(t["boundary_slopes"]), perm, mats, conv)
                          for t in table)
            if img != slope_multiset:
                ok = False
                break
        if ok:
            passing_convs.append(conv)
    log(f"  conventions preserving the census slope multiset under all 48 "
        f"isometries: {passing_convs}")
    conv_exists = len(passing_convs) >= 1
    if not conv_exists:
        log("  STOP: no convention preserves the census — cannot proceed")
        return 1
    CONV = passing_convs[0]

    # ---------------- stage 4: class structure, orbits, stabilizers ---------
    log(f"stage 4: class action (convention '{CONV}'), K-orbits, S3 orbits")
    classes = sorted({(tuple(t["boundary_slopes"]), int(t["chi"])) for t in table})
    n_classes = len(classes)
    class_index = {c: i for i, c in enumerate(classes)}
    mult = Counter((tuple(t["boundary_slopes"]), int(t["chi"])) for t in table)
    slope_to_chi = {}
    chi_well_defined = True
    for sl, chi in classes:
        if sl in slope_to_chi and slope_to_chi[sl] != chi:
            chi_well_defined = False
        slope_to_chi[sl] = chi
    doubled = sorted([c for c in classes if mult[c] == 2])
    log(f"  {n_classes} distinct (slope, chi) classes; slope determines chi: "
        f"{chi_well_defined}; doubled classes ({len(doubled)}): "
        f"{[c[0] for c in doubled]}")

    # induced permutation of the classes per isometry
    action_ok = True
    perms_on_classes = []  # (cusp_perm, class_perm tuple)
    for perm, mats in iso_data:
        cp = []
        for sl, chi in classes:
            img_sl = apply_iso(sl, perm, mats, CONV)
            key = (img_sl, chi)
            if key not in class_index or mult[key] != mult[(sl, chi)]:
                action_ok = False
                break
            cp.append(class_index[key])
        if not action_ok:
            break
        perms_on_classes.append((perm, tuple(cp)))
    log(f"  class action well-defined (chi + multiplicity preserved): {action_ok}")
    if not action_ok:
        return 1

    # K-orbits (unsigned peripheral classes) via union-find over kernel perms
    parent = list(range(n_classes))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    for perm, cp in perms_on_classes:
        if perm == (0, 1, 2):
            for i in range(n_classes):
                union(i, cp[i])
    korbit_of = [find(i) for i in range(n_classes)]
    korbit_ids = sorted(set(korbit_of))
    korbit_index = {k: i for i, k in enumerate(korbit_ids)}
    n_korbits = len(korbit_ids)
    korbit_members = {i: [] for i in range(n_korbits)}
    for ci in range(n_classes):
        korbit_members[korbit_index[korbit_of[ci]]].append(ci)
    log(f"  K-orbits (unsigned peripheral classes): {n_korbits}")

    # S3 action on K-orbits: verify all isometries with the same cusp perm
    # induce the same map
    s3_maps = {}
    s3_well_defined = True
    for perm, cp in perms_on_classes:
        kmap = {}
        consistent = True
        for ci in range(n_classes):
            src = korbit_index[korbit_of[ci]]
            dst = korbit_index[korbit_of[cp[ci]]]
            if src in kmap and kmap[src] != dst:
                consistent = False
                break
            kmap[src] = dst
        if not consistent:
            s3_well_defined = False
            break
        kt = tuple(kmap[i] for i in range(n_korbits))
        if perm in s3_maps and s3_maps[perm] != kt:
            s3_well_defined = False
            break
        s3_maps[perm] = kt
    s3_well_defined &= (sorted(s3_maps.keys()) == S3_ELEMENTS)
    log(f"  S3 action on K-orbits well-defined: {s3_well_defined}")
    if not s3_well_defined:
        return 1

    # S3 orbits of K-orbits + stabilizers
    seen = set()
    s3_orbits = []
    for k in range(n_korbits):
        if k in seen:
            continue
        orbit = sorted({s3_maps[p][k] for p in S3_ELEMENTS})
        stab = [p for p in S3_ELEMENTS if s3_maps[p][k] == k]
        for o in orbit:
            seen.add(o)
        s3_orbits.append({"korbits": orbit, "stab_order": len(stab),
                          "stabilizer": stab})
    orbit_stab_ok = all(len(o["korbits"]) * o["stab_order"] == 6
                        for o in s3_orbits)
    # conjugacy sanity: every member of an orbit has a conjugate stabilizer
    # (same order) — check orders match across the orbit
    for o in s3_orbits:
        for k in o["korbits"]:
            st = [p for p in S3_ELEMENTS if s3_maps[p][k] == k]
            orbit_stab_ok &= (len(st) == o["stab_order"])
    log(f"  S3 orbits of K-orbits: {len(s3_orbits)}; "
        f"orbit-stabilizer identity |orb|*|stab| = 6 for all: {orbit_stab_ok}")

    # ---------------- stage 5: pn-capability tables -------------------------
    log("stage 5: pn-capability classification")
    orbit_rows = []
    for oi, o in enumerate(s3_orbits):
        rep_k = o["korbits"][0]
        member_classes = korbit_members[rep_k]
        rep_sl, rep_chi = classes[member_classes[0]]
        n_surfaces_orbit = sum(mult[classes[ci]]
                               for k in o["korbits"]
                               for ci in korbit_members[k])
        supp = support_of(rep_sl)
        kind = ("S3-symmetric" if o["stab_order"] == 6 else
                "1-cusp-distinguishing" if o["stab_order"] == 2 else
                "fully-asymmetric")
        orbit_rows.append({
            "orbit": oi,
            "rep_slope": list(rep_sl),
            "chi": rep_chi,
            "support_size": len(supp),
            "rep_support": list(supp),
            "korbit_size_classes": len(member_classes),
            "s3_orbit_size": len(o["korbits"]),
            "n_surfaces": n_surfaces_orbit,
            "stab_order": o["stab_order"],
            "stabilizer": [list(p) for p in o["stabilizer"]],
            "kind": kind,
        })
        log(f"    orbit {oi}: rep slope {rep_sl} chi {rep_chi} "
            f"|supp| {len(supp)} | S3-orbit size {len(o['korbits'])} "
            f"stab {o['stab_order']} | surfaces {n_surfaces_orbit} | {kind}")
    n_sym = sum(1 for row in orbit_rows if row["stab_order"] == 6)
    n_stab2 = sum(1 for row in orbit_rows if row["stab_order"] == 2)
    n_stab1 = sum(1 for row in orbit_rows if row["stab_order"] == 1)
    surf_sym = sum(row["n_surfaces"] for row in orbit_rows
                   if row["stab_order"] == 6)
    surf_asym = n_surf - surf_sym
    log(f"  orbits by stabilizer order: |stab|=6: {n_sym}, |stab|=2: {n_stab2}, "
        f"|stab|=1: {n_stab1}")
    log(f"  surfaces in S3-symmetric orbits: {surf_sym}; in asymmetric "
        f"(pn-capable) orbits: {surf_asym}")

    # H-orbit DOF count: H = stabilizer of a pnn labeling (transposition
    # fixing the distinguished cusp). Computed for each of the 3 choices;
    # they must agree (conjugate subgroups).
    transpositions = {0: (0, 2, 1), 1: (2, 1, 0), 2: (1, 0, 2)}
    h_orbit_counts = {}
    for c0, tr in transpositions.items():
        tmap = s3_maps[tr]
        seenh = set()
        cnt = 0
        for k in range(n_korbits):
            if k in seenh:
                continue
            seenh.add(k)
            seenh.add(tmap[k])
            cnt += 1
        h_orbit_counts[c0] = cnt
    h_dof_consistent = len(set(h_orbit_counts.values())) == 1
    H_DOF = h_orbit_counts[0]
    log(f"  H-orbit counts (H = <transposition fixing cusp c0>): "
        f"{h_orbit_counts} — consistent: {h_dof_consistent}")
    log(f"  => an H-equivariant weighting on unsigned peripheral classes has "
        f"exactly {H_DOF} degrees of freedom (per labeling)")

    # ---------------- stage 6: non-additivity data --------------------------
    log("stage 6: non-additivity data")
    tets_touched = Counter(t["n_tets_touched"] for t in table)
    min_tets = min(t["n_tets_touched"] for t in table)
    log(f"  tetrahedra-touched distribution: {dict(sorted(tets_touched.items()))} "
        f"(min {min_tets} of {N})")
    qv_set = {tuple(t["quad_vector"]) for t in table}
    pairwise_sum_hit = None
    for i in range(n_surf):
        for j in range(i, n_surf):
            ssum = tuple(a + b for a, b in zip(table[i]["quad_vector"],
                                               table[j]["quad_vector"]))
            if ssum in qv_set:
                pairwise_sum_hit = (i, j)
                break
        if pairwise_sum_hit:
            break
    extremality_ok = pairwise_sum_hit is None
    log(f"  no census class is the quad-vector sum of two census classes: "
        f"{extremality_ok}")

    all_core = (conv_ok and all_indep and per_index_ok and summaries_ok
                and support_table_ok and sym_ok and combi_ok and conv_exists
                and chi_well_defined and action_ok and s3_well_defined
                and orbit_stab_ok and h_dof_consistent and extremality_ok)

    # ------------------------------------------------------------------ witness
    wb = WitnessBuilder("deltalambda-normal-surface-classes-probe",
                        engine="python-exact")
    wb.set_description(
        "Exact S3 orbit / stabilizer structure of the 52 vertex spun-normal "
        "surfaces of the Borromean rings complement B3 (SnapPy L6a4, 8 ideal "
        "tetrahedra, 3 cusps), for the idea-B3 pn-capability question: which "
        "surface classes decorate the three cusps asymmetrically and can carry "
        "a (Z,N)-distinguishing collective binding term. The census is "
        "re-derived via the same SnapPy machinery as the W9 angle-LP probe "
        "(m004 convention re-pin sigma=(1,2,0), eps=-1; GHHR 1604.02688 Prop "
        "A.3 pairing) and gated on EXACT per-index agreement with the committed "
        "W9 witness. The 48 isometries (full S3 on cusps; order-8 sign kernel "
        "K) act on the Z^6 peripheral grading via their cusp maps (convention "
        "pinned empirically by census-multiset preservation); the induced "
        "action on the 46 (slope, chi) classes gives K-orbits (unsigned "
        "peripheral classes), the S3 action on K-orbits (well-definedness "
        "machine-verified), S3 orbits, and exact stabilizers. Emits the "
        "cusp-support table, the refined orbit/stabilizer table, the "
        "asymmetric-class counts, the H-orbit DOF count for a "
        "labeling-stabilizer-equivariant weighting, and non-additivity data "
        "(tetrahedra-touched, pairwise-sum extremality). Structure-hunt tier; "
        "audit-only; scope-(a); NO FIT; no q0; no comparison to any binding "
        "observable; nothing wired to production.")
    wb.set_content_block("def:borromean-baryon")
    wb.set_audit_only(
        "docs/audits/2026-07-24-deltalambda-normal-surface-collective-candidate.md")
    wb.add_upstream(W9_WITNESS)

    wb.add_data("manifold", "L6a4 (Borromean rings complement)")
    wb.add_data("census_count", n_surf)
    wb.add_data("chi_distribution", dict(chi_dist))
    wb.add_data("cusps_touched_pattern", pat_str)
    wb.add_data("support_chi_crosstab",
                {f"{k[0]}-cusp,chi={k[1]}": v for k, v in sorted(supp_chi.items())})
    wb.add_data("n_distinct_slope_chi_classes", n_classes)
    wb.add_data("doubled_classes",
                [{"slope": list(sl), "chi": chi, "multiplicity": 2}
                 for sl, chi in doubled])
    wb.add_data("symmetry", {
        "isometry_group_order": len(isos),
        "cusp_permutations_realized": [list(p) for p in perms_realized],
        "sign_kernel_order": len(kernel),
        "combinatorial_automorphisms": len(combi),
        "combinatorial_cusp_permutations": [list(p) for p in combi_perms],
        "note": "only a Z2 of the S3 is realized combinatorially on THIS "
                "triangulation; the S3 orbit structure below is computed on "
                "peripheral (slope, chi) classes via the isometry cusp maps, "
                "not on quad vectors",
    })
    wb.add_data("peripheral_action_conventions_passing", passing_convs)
    wb.add_data("peripheral_action_convention_used", CONV)
    wb.add_data("n_kernel_orbits_unsigned_classes", n_korbits)
    wb.add_data("n_s3_orbits", len(s3_orbits))
    wb.add_data("orbit_table", orbit_rows)
    wb.add_data("orbits_by_stabilizer_order",
                {"6": n_sym, "2": n_stab2, "1": n_stab1})
    wb.add_data("surfaces_in_s3_symmetric_orbits", surf_sym)
    wb.add_data("surfaces_in_asymmetric_orbits", surf_asym)
    wb.add_data("h_orbit_dof_counts_per_distinguished_cusp", h_orbit_counts)
    wb.add_data("h_equivariant_weighting_dof", H_DOF)
    wb.add_data("tets_touched_distribution",
                {str(k): v for k, v in sorted(tets_touched.items())})
    wb.add_data("min_tets_touched", min_tets)
    wb.add_data("pairwise_sum_extremality_holds", extremality_ok)
    wb.add_data("surface_table",
                [{"index": t["index"],
                  "boundary_slopes": t["boundary_slopes"],
                  "chi": str(t["chi"]),
                  "support": list(t["support"]),
                  "n_tets_touched": t["n_tets_touched"],
                  "total_quads": t["total_quads"]} for t in table])

    wb.add_assertion("m004_conventions_repinned", computed=float(conv_ok),
                     expected=1.0, tolerance=0.5,
                     source="sigma=(1,2,0), eps=-1 re-pinned on m004 vs GHHR "
                            "Ex 10.23/A.10, matching the W9 frozen values")
    wb.add_assertion("census_matches_w9_per_index", computed=float(per_index_ok),
                     expected=1.0, tolerance=0.5,
                     source="quad_vector + boundary_slopes + chi equal to the "
                            "committed W9 witness for all 52 indices")
    wb.add_assertion("census_summaries_match_w9", computed=float(summaries_ok),
                     expected=1.0, tolerance=0.5,
                     source="count / chi distribution / quad distribution / "
                            "cusps-touched pattern equal to W9 witness")
    wb.add_assertion("support_table_4_4_4_8_8_8_16",
                     computed=float(support_table_ok), expected=1.0,
                     tolerance=0.5,
                     source="1-cusp: 4 per cusp, 2-cusp: 8 per pair, "
                            "3-cusp: 16")
    wb.add_assertion("isometry_group_order", computed=float(len(isos)),
                     expected=48.0, tolerance=0.5,
                     source="SnapPy is_isometric_to(return_isometries=True)")
    wb.add_assertion("full_s3_realized_on_cusps",
                     computed=float(perms_realized == S3_ELEMENTS),
                     expected=1.0, tolerance=0.5,
                     source="all 6 cusp permutations occur among the 48 "
                            "isometries")
    wb.add_assertion("sign_kernel_order", computed=float(len(kernel)),
                     expected=8.0, tolerance=0.5,
                     source="isometries with trivial cusp permutation")
    wb.add_assertion("combinatorial_automorphisms_z2_only",
                     computed=float(combi_ok), expected=1.0, tolerance=0.5,
                     source="16 combinatorial automorphisms realizing only "
                            "{id, (0 2)} — matches W9")
    wb.add_assertion("peripheral_action_convention_exists",
                     computed=float(conv_exists), expected=1.0, tolerance=0.5,
                     source="at least one cusp-map convention preserves the "
                            "census slope multiset under all 48 isometries")
    wb.add_assertion("class_action_well_defined", computed=float(action_ok),
                     expected=1.0, tolerance=0.5,
                     source="induced map preserves (slope, chi) class set and "
                            "multiplicities for all 48 isometries")
    wb.add_assertion("s3_action_on_kernel_orbits_well_defined",
                     computed=float(s3_well_defined), expected=1.0,
                     tolerance=0.5,
                     source="all isometries with the same cusp permutation "
                            "induce the same map on K-orbits (K normal)")
    wb.add_assertion("orbit_stabilizer_identity",
                     computed=float(orbit_stab_ok), expected=1.0, tolerance=0.5,
                     source="|S3-orbit| * |stabilizer| = 6 for every orbit; "
                            "stabilizer orders constant along each orbit")
    wb.add_assertion("h_dof_count_cusp_independent",
                     computed=float(h_dof_consistent), expected=1.0,
                     tolerance=0.5,
                     source="H-orbit count identical for all 3 choices of "
                            "distinguished cusp (conjugate subgroups)")
    wb.add_assertion("pairwise_sum_extremality",
                     computed=float(extremality_ok), expected=1.0, tolerance=0.5,
                     source="no census quad-vector is the sum of two census "
                            "quad-vectors (vertex/extreme-ray property, "
                            "pairwise check)")
    wb.save()
    log("witness saved")

    print()
    print(f"  classes: {n_classes} (slope, chi); K-orbits {n_korbits}; "
          f"S3 orbits {len(s3_orbits)} "
          f"(stab 6/2/1: {n_sym}/{n_stab2}/{n_stab1})")
    print(f"  pn-capable (asymmetric) surfaces: {surf_asym} of {n_surf}; "
          f"H-equivariant weighting DOF: {H_DOF}")
    print(f"  RESULT: {'ALL OK' if all_core else 'CHECK FAILED'}")
    return 0 if all_core else 1


if __name__ == "__main__":
    raise SystemExit(main())
