#!/usr/bin/env python3
"""borromean_3d_index_graded.py — per-cusp graded 3D-index table of the Borromean
rings complement (advances idea B6's grading leg; W1 of the 2026-07-24 workplan).

Follow-on to computations/probes/borromean_3d_index.py (validated machinery; audit
docs/audits/2026-07-18-borromean-3d-index.md).  This probe:

  1. computes I_B3(b) EXACTLY to q^6 for every peripheral class b in Z^6 with
     |b|_inf <= 1 (3^6 = 729 classes; b = (p1,q1,p2,q2,p3,q3) in the SnapPy
     (mu_h, lam_h) cusp-row basis of L6a4), reusing the GHRS/GHHR machinery of
     borromean_3d_index.IndexTriangulation verbatim for charges/J_D/min-degree,
     with one performance addition: a SHARED shell enumeration across classes
     (the lattice box and the b-independent charge part k @ E are computed once
     per l-infinity shell and reused for all classes; the per-summand min-degree
     bound D(k,b) = 2*sum(k) + sum_j nu_j(k,b) is evaluated per class with the
     elementary-symmetric identity nu = e2(shifted charges) - min, which equals
     the sorted-product form of borromean_3d_index.nu_Q exactly because the
     min-shifted triple always contains a zero);
  2. verifies S_3 cusp-permutation equivariance of the FULL table (every class
     vs every permutation of the three (p_h, q_h) blocks), and RECORDS (does not
     interpret) which further candidate lattice symmetries preserve the table
     (global negation b -> -b, per-cusp negation, global and per-cusp
     meridian<->longitude swap, global longitude negation);
  3. computes the meridian TOTAL index
         I^tot_B3(q) := sum_{e in Z^3} I_B3(e1*mu1 + e2*mu2 + e3*mu3)(q)
     to q^6 — the direct 3-cusp analogue of GHRS arXiv:1303.5278 Rmk 1.13 eq (2)
     (stated there for KNOT complements; the link-complement version used here is
     a DEFINITION, flagged as such, with per-order finiteness checked by the
     exact min-degree bound: meridian e-shells are enumerated until two
     consecutive shells contribute nothing to q^6);
  4. records count-level Wedderburn-side data (partitions of 3, block dims,
     writhe-0 one-dimensional characters, the Lean-proved tr_M(beta_Bor) closed
     form and F_Bor(q_0)) NEXT TO the index-side counts, comparison-only.

VALIDATION GATES (all must pass before the sweep results are trusted):
  A. committed-value gate — I_B3(0), I_B3(mu_1), I_B3(mu_1+lam_1) from this
     probe's shared-shell machinery must equal the committed witness values of
     borromean-3d-index.witness.json (exact integers to q^6);
  B. independent-machinery gate — for three sample classes the shared-shell
     enumeration + evaluation must equal borromean_3d_index.IndexTriangulation
     .index() (the original, per-class itertools enumeration) exactly;
  C. structural self-tests — no negative q-powers anywhere (GHHR Cor 10.21),
     I_B3(0) constant term 1, S_3 equivariance of the full 729-class table.

SCOPE (STRICT). Audit-only; scope-(a); comparison-only; NO FIT; nothing wired to
production.  No coefficient of any index series is compared numerically to
F_Bor / tr_M / rho(B3) / masses — the bridge-invariant list lives in
docs/audits/2026-07-24-borromean-index-bridge-invariant.md and this probe only
supplies the graded data + count-level structure that any *derived* bridge must
consume equivariantly.  (AGENTS.md anti-laundering + formalize-first.)

SOURCES: as in borromean_3d_index.py ([GHHR] arXiv:1604.02688 Section 4;
[GHRS] arXiv:1303.5278 Sections 4.5-4.6, Thm 1.1/1.2/1.5, Rmk 1.10, Rmk 1.13),
plus [DGG] arXiv:1112.5179 Section 4.6 eq (4.54)-(4.57) for the volume
asymptotics statement recorded in the audit doc (not computed here).
"""
from __future__ import annotations

import itertools
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: E402, F401
from witness_base import WitnessBuilder  # noqa: E402

import borromean_3d_index as bor  # noqa: E402  (validated machinery, reused)
from _precision import set_compute_dps  # noqa: E402

T0 = time.time()
QMAX = 6              # q-order of the graded sweep (Q-degree cap = 12)
HI = 2 * QMAX
EMPTY_SHELLS_TO_STOP = 3
RMAX = 40
CHUNK = 400_000       # rows per numpy chunk in the shared shell sweep

# Committed reference values (gate A) — exact integers from
# computations/probes/borromean-3d-index.witness.json /
# docs/audits/2026-07-18-borromean-3d-index.md (q^0..q^6).
REF_I0_Q6 = [1, 0, 13, -16, -97, 16, 586]
REF_MU_Q6 = [0, 0, 8, -16, -64, 48, 464]
REF_MULAM_Q6 = [0, 0, 0, -8, 8, 64, 96]


def log(msg: str) -> None:
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


# ---------------------------------------------------------------------------
# Shared-shell graded sweep
# ---------------------------------------------------------------------------

class GradedSweep:
    """Multi-class admissible-lattice sweep sharing shell enumeration.

    Semantics per class are identical to IndexTriangulation.admissible_lattice
    (same min-degree bound, same 3-consecutive-empty-shell stopping rule);
    only the enumeration is shared across classes for speed.
    """

    def __init__(self, tri: bor.IndexTriangulation):
        self.tri = tri
        self.n = tri.n
        self.Eb = np.array([tri.edge_rows[i] for i in tri.basic_edges],
                           dtype=np.int64)                      # dim x 3n
        self.cusp = np.array(tri.cusp_rows, dtype=np.int64)     # 2r x 3n
        self.dim = len(tri.basic_edges)

    def _shell_rows(self, R: int):
        """Yield (box_chunk, ) numpy int64 arrays covering the l-inf shell R."""
        if R == 0:
            yield np.zeros((1, self.dim), dtype=np.int64)
            return
        w = 2 * R + 1
        # inner grid over the last dim-1 coordinates, built once per R
        inner = np.indices((w,) * (self.dim - 1), dtype=np.int64)
        inner = inner.reshape(self.dim - 1, -1).T - R            # M x (dim-1)
        cheb = np.abs(inner).max(axis=1)
        interior_rows = inner[cheb < R]
        for k0 in range(-R, R + 1):
            rows = inner if abs(k0) == R else inner[cheb == R]
            if not len(rows):
                continue
            box = np.empty((len(rows), self.dim), dtype=np.int64)
            box[:, 0] = k0
            box[:, 1:] = rows
            # chunk if very large
            for s in range(0, len(box), CHUNK):
                yield box[s:s + CHUNK]
        del interior_rows  # (unused beyond clarity)

    def sweep(self, classes, hi: int):
        """Admissible k-vectors (full length-n, zeros at excluded edges) per class.

        Returns dict class-index -> list of full k-vectors.
        """
        C = len(classes)
        PB = np.array(classes, dtype=np.int64) @ self.cusp       # C x 3n
        adm = {i: [] for i in range(C)}
        empty_run = [0] * C
        active = set(range(C))
        R = 0
        while active and R <= RMAX:
            found = [False] * C
            nrows = 0
            for box in self._shell_rows(R):
                nrows += len(box)
                S = box @ self.Eb                                # M x 3n
                k2 = 2 * box.sum(axis=1)                         # M
                for ci in list(active):
                    C3 = (S + PB[ci]).reshape(len(box), self.n, 3)
                    m = C3.min(axis=2)                           # M x n
                    sh = C3 - m[:, :, None]
                    t = sh.sum(axis=2)
                    sq = (sh * sh).sum(axis=2)
                    e2 = (t * t - sq) // 2                       # = s1*s2 (s0=0)
                    D = k2 + (e2 - m).sum(axis=1)
                    good = box[D <= hi]
                    if len(good):
                        found[ci] = True
                        for kk in good:
                            kvec = [0] * self.n
                            for pos, ki in zip(self.tri.basic_edges, kk):
                                kvec[pos] = int(ki)
                            adm[ci].append(kvec)
            for ci in list(active):
                empty_run[ci] = 0 if found[ci] else empty_run[ci] + 1
                if empty_run[ci] >= EMPTY_SHELLS_TO_STOP:
                    active.remove(ci)
            log(f"  shell R={R}: {nrows} rows, {len(active)} classes active")
            R += 1
        if active:
            raise RuntimeError(f"sweep hit RMAX={RMAX} with active classes")
        return adm

    def evaluate(self, kvecs, b, hi: int):
        """Exact Q-dict of sum over kvecs of q^{sum k} prod_j J_D(charges).

        Same evaluation loop as IndexTriangulation.index() (borromean_3d_index),
        applied to a precomputed admissible list.
        """
        tri = self.tri
        tot = {}
        for kvec in kvecs:
            charges = tri._charges(kvec, b)
            shift = 2 * sum(kvec)
            cap = hi - shift
            nus = [bor.nu_Q(*t) for t in charges]
            rest = sum(nus)
            done = 0
            prod = {0: 1}
            for t, nu in zip(charges, nus):
                rest -= nu
                fac = bor.J_D(*t, cap - rest - done)
                prod = bor._mul(prod, fac, cap - rest)
                done += nu
                if not prod:
                    break
            for p, cc in prod.items():
                pp = p + shift
                if pp <= hi:
                    tot[pp] = tot.get(pp, 0) + cc
        return {p: c for p, c in tot.items() if c}


# ---------------------------------------------------------------------------
# Symmetry maps on peripheral classes b = (p1,q1,p2,q2,p3,q3)
# ---------------------------------------------------------------------------

def perm_cusps(b, pi):
    """Permute the three (p_h, q_h) blocks by permutation pi of {0,1,2}."""
    out = [0] * 6
    for h in range(3):
        out[2 * pi[h]], out[2 * pi[h] + 1] = b[2 * h], b[2 * h + 1]
    return tuple(out)


SYMMETRY_MENU = {
    "global_negation": lambda b: tuple(-x for x in b),
    "negate_cusp_1": lambda b: (-b[0], -b[1]) + b[2:],
    "swap_mu_lam_all": lambda b: (b[1], b[0], b[3], b[2], b[5], b[4]),
    "swap_mu_lam_cusp_1": lambda b: (b[1], b[0]) + b[2:],
    "negate_lam_all": lambda b: (b[0], -b[1], b[2], -b[3], b[4], -b[5]),
    "negate_mu_all": lambda b: (-b[0], b[1], -b[2], b[3], -b[4], b[5]),
    "negate_lam_cusp_1": lambda b: (b[0], -b[1]) + b[2:],
    "negate_mu_cusp_1": lambda b: (-b[0], b[1]) + b[2:],
}


# ---------------------------------------------------------------------------
def qcoeffs(d, nq):
    return [d.get(2 * j, 0) for j in range(nq)]


def series_pairs(d):
    """Exact (Q-power, coeff) pairs, sorted (Q = q^{1/2})."""
    return sorted(d.items())


def main() -> int:
    print("=" * 74)
    print(" Graded 3D-index table of the Borromean rings complement (L6a4)")
    print(" audit-only / scope-(a) / comparison-only / no fit — see docstring")
    print("=" * 74)

    try:
        import snappy
    except ImportError:
        print("WALL: SnapPy is not importable — refusing to hand-guess gluing "
              "data (anti-guessing rule). Install snappy and re-run.")
        return 2

    log("preflight: kernel identities (reused from borromean_3d_index)")
    if not bor.preflight():
        log("  preflight FAILED")
        return 1
    log("  preflight OK")

    M = snappy.Manifold("L6a4")
    tri = bor.IndexTriangulation(M)
    pos_oriented = M.solution_type() == "all tetrahedra positively oriented"
    log(f"L6a4: n={tri.n}, r={tri.r}, basic edges {tri.basic_edges}, "
        f"solution '{M.solution_type()}', volume {float(M.volume()):.9f}")

    sweeper = GradedSweep(tri)

    # ---------------- stage 1: |b|_inf <= 1 graded sweep --------------------
    classes = [tuple(b) for b in itertools.product((-1, 0, 1), repeat=6)]
    log(f"stage 1: shared-shell sweep of {len(classes)} classes to q^{QMAX}")
    adm = sweeper.sweep(classes, HI)
    n_adm = sum(len(v) for v in adm.values())
    log(f"  admissible vectors total: {n_adm} "
        f"(max per class {max(len(v) for v in adm.values())})")

    log("stage 2: evaluating series per class")
    table = {}
    for ci, b in enumerate(classes):
        table[b] = sweeper.evaluate(adm[ci], b, HI)
        if ci % 100 == 99:
            el = time.time() - T0
            log(f"  evaluated {ci + 1}/{len(classes)} "
                f"(elapsed {el:.0f}s, ETA +{el / (ci + 1) * (len(classes) - ci - 1):.0f}s)")

    zero_b = tuple([0] * 6)
    c0 = qcoeffs(table[zero_b], QMAX + 1)
    log(f"  I_B3(0) to q^{QMAX}: {c0}")

    # ---------------- gate A: committed values ------------------------------
    gA = (c0 == REF_I0_Q6
          and qcoeffs(table[(1, 0, 0, 0, 0, 0)], QMAX + 1) == REF_MU_Q6
          and qcoeffs(table[(1, 1, 0, 0, 0, 0)], QMAX + 1) == REF_MULAM_Q6)
    log(f"gate A (committed witness values, 3 classes): {'PASS' if gA else 'FAIL'}")

    # ---------------- gate B: independent machinery -------------------------
    gB = True
    for b in [zero_b, (1, 0, 0, 0, 0, 0), (0, 0, 1, 1, 0, 0), (1, 0, -1, 0, 0, 1)]:
        ref = tri.index(b, QMAX, progress_every=0)
        gB &= (ref == table[b])
    log(f"gate B (original per-class machinery, 4 classes): {'PASS' if gB else 'FAIL'}")

    # ---------------- gate C: structural self-tests -------------------------
    neg_ok = all(min(d) >= 0 for d in table.values() if d)
    const_ok = table[zero_b].get(0, 0) == 1
    odd_terms = {b: [(p, c) for p, c in sorted(d.items()) if p % 2]
                 for b, d in table.items() if any(p % 2 for p in d)}
    log(f"gate C: power series everywhere: {neg_ok}; const term 1: {const_ok}; "
        f"classes with half-integer q-powers: {len(odd_terms)}")

    # S_3 equivariance over the full table
    perms = list(itertools.permutations(range(3)))
    s3_ok = True
    for b in classes:
        for pi in perms:
            if table[perm_cusps(b, pi)] != table[b]:
                s3_ok = False
                log(f"  S_3 BROKEN: b={b} pi={pi}")
    log(f"  S_3 cusp-permutation equivariance over all {len(classes)} classes: "
        f"{'PASS' if s3_ok else 'FAIL'}")

    # further symmetry menu (recorded-not-interpreted)
    sym_results = {}
    for name, f in SYMMETRY_MENU.items():
        ok = all(table[f(b)] == table[b] for b in classes)
        sym_results[name] = ok
        log(f"  symmetry menu — {name}: {'preserves table' if ok else 'does NOT preserve table'}")

    # ---------------- orbit decomposition (under S_3) -----------------------
    seen = set()
    orbits = []  # (representative, orbit_size, series)
    for b in classes:
        if b in seen:
            continue
        orb = {perm_cusps(b, pi) for pi in perms}
        seen |= orb
        orbits.append((min(orb), len(orb), table[b]))
    nonzero_orbits = [(r, s, d) for (r, s, d) in orbits if d]
    log(f"  S_3 orbits: {len(orbits)} total, {len(nonzero_orbits)} with nonzero "
        f"series to q^{QMAX}; nonzero classes "
        f"{sum(s for _, s, d in orbits if d)}/{len(classes)}")

    # coarse orbits under the FULL verified lattice symmetry group: the group
    # generated by every symmetry-menu map that preserved the table, plus the
    # S_3 permutations (recorded-not-interpreted; orbit closure by BFS)
    verified_maps = [f for name, f in SYMMETRY_MENU.items() if sym_results[name]]
    verified_maps += [(lambda pi: (lambda b: perm_cusps(b, pi)))(pi) for pi in perms]

    def orbit_closure(b):
        orb, todo = {b}, [b]
        while todo:
            x = todo.pop()
            for f in verified_maps:
                y = f(x)
                if y not in orb:
                    orb.add(y)
                    todo.append(y)
        return orb

    seen2 = set()
    coarse = []
    for b in classes:
        if b in seen2:
            continue
        orb = orbit_closure(b)
        seen2 |= orb
        series = {tuple(sorted(table[x].items())) for x in orb}
        assert len(series) == 1, f"verified maps break on orbit of {b}"
        coarse.append((min(orb), len(orb), table[b]))
    distinct_series = {tuple(sorted(d.items())) for _, _, d in coarse}
    log(f"  coarse orbits under the verified symmetry group: {len(coarse)}; "
        f"distinct series among them: {len(distinct_series)} "
        f"(coincidences beyond the group are recorded, not interpreted)")

    # ---------------- stage 3: meridian total index -------------------------
    log("stage 3: meridian total index I^tot (3-cusp analogue of GHRS Rmk 1.13 "
        "eq (2) — link version is a DEFINITION here, not the knot theorem)")
    tot = {}
    contributing = []
    E = 0
    empty_e_shells = 0
    while empty_e_shells < 2 and E <= 12:
        shell_classes = [e for e in itertools.product(range(-E, E + 1), repeat=3)
                         if max(abs(x) for x in e) == E]
        found = False
        # reuse the |b|<=1 table where possible
        need = []
        for e in shell_classes:
            b = (e[0], 0, e[1], 0, e[2], 0)
            if max(abs(x) for x in b) <= 1:
                d = table[b]
                if d:
                    found = True
                    contributing.append((e, d))
            else:
                need.append((e, b))
        if need:
            adm_e = sweeper.sweep([b for _, b in need], HI)
            for i, (e, b) in enumerate(need):
                d = sweeper.evaluate(adm_e[i], b, HI)
                if d:
                    found = True
                    contributing.append((e, d))
        empty_e_shells = 0 if found else empty_e_shells + 1
        log(f"  e-shell |e|={E}: {len(shell_classes)} classes, "
            f"{'contributes' if found else 'empty'}")
        E += 1
    for _, d in contributing:
        for p, c in d.items():
            tot[p] = tot.get(p, 0) + c
    tot = {p: c for p, c in tot.items() if c}
    tot_coeffs = qcoeffs(tot, QMAX + 1)
    log(f"  I^tot_B3 to q^{QMAX}: {tot_coeffs}  "
        f"({len(contributing)} contributing meridian classes, stop |e| = {E - 1})")

    # ---------------- stage 4: count-level Wedderburn-side record -----------
    # (comparison-only, recorded-not-interpreted; no numeric coefficient match)
    wedderburn = {
        "H3_partitions": ["[3]", "[2,1]", "[1,1,1]"],
        "H3_block_dims": [1, 2, 1],
        "beta_Bor": "(sigma_1 sigma_2^{-1})^3, writhe 0",
        "one_dim_characters_at_beta_Bor": {"[3]": 1, "[1,1,1]": 1},
        "trM_closed_form": "(4 + h^2 - 3h^4 - h^6)/(h^2 + 4), h = q - 1/q "
                           "(BorromeanMarkovTrace.lean; even in h, bar-even)",
        "F_Bor_def": "|tr_M(beta_Bor)| * [3]_q! / q^3 "
                     "(m_p_substrate_identity_50dps.py)",
    }
    try:
        from m_p_substrate_identity_50dps import F_Bor
        from q_parameter import Q_50_DIGIT_STR
        from mpmath import mp, mpf
        set_compute_dps()
        wedderburn["F_Bor_at_q0"] = mp.nstr(F_Bor(mpf(Q_50_DIGIT_STR)), 30)
    except Exception as exc:  # record, don't fail the topology probe
        wedderburn["F_Bor_at_q0"] = f"unavailable ({exc})"
    log(f"  Wedderburn-side record: 3 blocks, dims (1,2,1); "
        f"F_Bor(q0) = {wedderburn['F_Bor_at_q0']}")

    all_ok = (gA and gB and neg_ok and const_ok and s3_ok and pos_oriented)

    # ---------------- witness ----------------------------------------------
    wb = WitnessBuilder("borromean-3d-index-graded", engine="python-exact")
    wb.set_description(
        "Per-cusp graded 3D-index table of the Borromean rings complement B3 "
        "(SnapPy L6a4): I_B3(b) exact to q^6 for all 729 peripheral classes "
        "|b|_inf <= 1, S_3 cusp-permutation equivariance verified on the full "
        "table, extra lattice symmetries recorded, and the meridian total index "
        "I^tot = sum_{e in Z^3} I(sum e_h mu_h) (3-cusp analogue of GHRS "
        "1303.5278 Rmk 1.13 eq (2); link version is a definition, per-order "
        "finiteness certified by the exact min-degree bound). Machinery: "
        "borromean_3d_index.py (validated 2026-07-18) with a shared-shell "
        "enumeration; gated against the committed witness AND the original "
        "per-class machinery. Audit-only; scope-(a); comparison-only; NO FIT; "
        "no coefficient is compared numerically to F_Bor/tr_M/rho/masses — "
        "count-level Wedderburn-side structure recorded next to index-side "
        "counts only. Bridge-invariant list: "
        "docs/audits/2026-07-24-borromean-index-bridge-invariant.md.")
    wb.set_content_block("def:borromean-baryon")
    wb.set_audit_only("docs/audits/2026-07-24-borromean-index-bridge-invariant.md")
    wb.add_data("manifold", "L6a4 (Borromean rings complement)")
    wb.add_data("qmax", QMAX)
    wb.add_data("n_classes", len(classes))
    wb.add_data("n_classes_nonzero_to_q6", sum(1 for d in table.values() if d))
    wb.add_data("n_S3_orbits", len(orbits))
    wb.add_data("n_S3_orbits_nonzero", len(nonzero_orbits))
    wb.add_data("orbit_size_multiset_nonzero",
                sorted(s for _, s, d in nonzero_orbits))
    wb.add_data(
        "graded_table_nonzero",
        {" ".join(map(str, r)): {"orbit_size": s,
                                 "Q_pairs": series_pairs(d),
                                 "q_coeffs": qcoeffs(d, QMAX + 1)}
         for r, s, d in nonzero_orbits})
    wb.add_data("half_integer_power_classes",
                {" ".join(map(str, b)): pairs for b, pairs in odd_terms.items()})
    wb.add_data("symmetry_menu_results", sym_results)
    wb.add_data("coarse_orbits_verified_group_count", len(coarse))
    wb.add_data("coarse_distinct_series_count", len(distinct_series))
    wb.add_data(
        "coarse_orbit_table",
        {" ".join(map(str, r)): {"orbit_size": s,
                                 "q_coeffs": qcoeffs(d, QMAX + 1)}
         for r, s, d in coarse})
    wb.add_data("I_tot_meridian_q0_q6", tot_coeffs)
    wb.add_data("I_tot_meridian_Q_pairs", series_pairs(tot))
    wb.add_data("I_tot_contributing_meridian_classes",
                [" ".join(map(str, e)) for e, _ in contributing])
    wb.add_data("I_tot_stop_radius_linf", E - 1)
    wb.add_data("I_tot_definition_caveat",
                "GHRS Rmk 1.13 eq (2) states I^tot for KNOT complements; the "
                "3-cusp sum used here is a definition (per-order finiteness "
                "machine-certified via the exact min-degree bound), not the "
                "cited theorem.")
    wb.add_data("wedderburn_side_record", wedderburn)
    wb.add_assertion("gate_A_committed_witness_values", computed=float(gA),
                     expected=1.0, tolerance=0.5,
                     source="I(0), I(mu_1), I(mu_1+lam_1) equal "
                            "borromean-3d-index.witness.json to q^6")
    wb.add_assertion("gate_B_independent_machinery", computed=float(gB),
                     expected=1.0, tolerance=0.5,
                     source="shared-shell sweep equals IndexTriangulation.index() "
                            "on 4 classes exactly")
    wb.add_assertion("index_is_power_series_all_classes", computed=float(neg_ok),
                     expected=1.0, tolerance=0.5,
                     source="no negative q-powers on any of 729 classes "
                            "(GHHR Cor 10.21)")
    wb.add_assertion("constant_term_is_one", computed=float(const_ok),
                     expected=1.0, tolerance=0.5, source="I_B3(0)(0) = 1")
    wb.add_assertion("s3_equivariance_full_table", computed=float(s3_ok),
                     expected=1.0, tolerance=0.5,
                     source="I(pi.b) = I(b) for all 729 classes x 6 permutations")
    wb.save()
    log("witness saved")

    print()
    print(f"  I_B3(0)  = {c0}")
    print(f"  I^tot    = {tot_coeffs}")
    print(f"  nonzero classes: {sum(1 for d in table.values() if d)}/729 in "
          f"{len(nonzero_orbits)} S_3 orbits")
    print(f"  RESULT: {'ALL OK' if all_ok else 'CHECK FAILED'}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
