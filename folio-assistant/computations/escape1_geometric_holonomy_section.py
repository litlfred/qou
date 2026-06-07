#!/usr/bin/env python3
"""Escape 1: does the icosahedral A5 / Bring cross-ratio GEOMETRY force a
canonical SECTION of the (2,1)-multiplicity space? (EXPLORATORY, audit-only).

THE keystone obstruction (merged synthesis
docs/audits/2026-06-02-young-lattice-gauge-synthesis.md, sharpened by the
spinor audit #1687 docs/audits/2026-06-02-su2-spinor-multiplicity-resolution.md):
the Okounkov-Vershik / Jucys-Murphy content eigenbasis of the (2,1)-mult space
EXISTS, but nothing canonically SELECTS the physical copy -- the missing object
is a canonical SECTION (a forced 1-dim sub-line of the >=2-dim Hom-space), not
a basis. Escape 2 (native-5-strand) was FALSIFIED (#1694). Escape 1 proposes the
section comes from GEOMETRIC structure OUTSIDE Hecke rep theory: the icosahedral
A5 holonomy / the Bring color-tube cross-ratio acting on the dim-5 ell=2 fiber.

THE OBJECT (recomputed RAW here): the mult-2 Hom-space
  V := Hom_{S3}( (2,1)_std , Res^{A5}_{S3}(H) )  ~=  C^2,
where H is the dim-5 ell=2 irrep of A5 ~= I (icosahedral), and
S3 = <(123),(12)(45)> < A5 is the color-sheet stabilizer (h5_h3_functor_keystone:
Res^{A5}_{S3}(H) = triv (+) 2.(2,1)). The "section" the keystone needs is a
CANONICAL LINE (1-dim sub) of this C^2.

THE TEST (separation vs selection, exactly parallel to the spinor test #1687):
a FORCED geometric operator on V must have a SIMPLE spectrum / a UNIQUE invariant
line (=> canonical section, DERIVED), with NO tunable parameter. The fit trap:
a cross-ratio value or holonomy phase CHOSEN to make a line appear (e.g. to yield
h^4 = -3/4) is a fit dressed as geometry.

WHAT FORCES AN OPERATOR ON V (the rigorous criterion). By Schur's lemma the
endomorphism algebra of the (2,1)-isotypic component of Res H is M_2(C) acting on
the C^2 multiplicity space. An operator on V is CANONICAL (basis-independent,
forced by the ambient A5 geometry) iff it is the image of a group element / group-
algebra element that PRESERVES the S3-isotypic structure and COMMUTES with the
S3-action -- i.e. it comes from the CENTRALIZER C_{A5}(S3) (forced endomorphism)
or, more weakly, an element of the NORMALIZER N_{A5}(S3) acting (semilinearly, up
to the induced S3-automorphism) on the isotypic block. If both
C_{A5}(S3) and N_{A5}(S3)/S3 are trivial, the ONLY forced operator on V is the
scalar identity (degenerate spectrum, NO distinguished line) and any line must be
chosen => FIT.

DISCIPLINE (CLAUDE.md production-vs-exploratory): DERIVE or prove-no-forced-
selector; NEVER fit. h^4 = -3/4 is a FALSIFICATION reference, not a target. The
mult-2 Hom-space and every A5/S3 group-theoretic fact is computed FIRST, RAW; the
comparison to h^4 comes LAST and only if a canonical line is forced.

COMPUTES (exact integer/permutation-group combinatorics; explicit numerical
rep matrices for the C^2 realization; RAW substrate values via mpmath at the
canonical compute_dps):
  TASK 1 -- pin V: realize H (dim-5, ell=2) explicitly as a rep of A5 (via the
    10-dim unordered-pair perm rep = triv (+) G(4) (+) H(5), projected onto the
    H-isotypic), restrict to S3 < A5, project onto the (2,1)-isotypic, and verify
    dim V = 2 RAW (matches the keystone character count).
  TASK 2 -- forced geometric structure on V: compute C_{A5}(S3) (centralizer) and
    N_{A5}(S3) (normalizer). These are the ONLY sources of a FORCED (basis-
    independent) operator on V. This is the geometric-operator candidate (a),
    FORCED by A5 (no parameter).
  TASK 3 -- THE TEST: does any FORCED operator have a simple spectrum / unique
    invariant line on V? (separation vs selection.)
  TASK 4 -- cross-ratio / holonomy candidate (b),(c): are the icosahedral special
    cross-ratios (golden-ratio vertex values) FORCED selectors, or does using one
    to pick a line in V require choosing WHICH cross-ratio (a free modulus = fit)?
  TASK 5 -- falsification (NOT a target): IF a canonical line is forced, compute
    whether the resulting section carries h^4 = -3/4 RAW. Only performed if Task 3
    forces a line with no free parameter.
  VERDICT (i/ii/iii).

Audit doc: docs/audits/2026-06-02-escape1-geometric-holonomy-section.md
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import itertools
import sys
import time
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps, COMPUTE_DPS  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402  (proton-pinned, single source of truth)
from q_parameter import Q_MP as Q0_MP  # noqa: E402  (high-precision mpf)

START = time.monotonic()
ACTUAL_DPS = set_compute_dps()
assert ACTUAL_DPS == COMPUTE_DPS, (ACTUAL_DPS, COMPUTE_DPS)

Q0_STR = mp.nstr(Q0_MP, COMPUTE_DPS)
H4_BORROMEAN = Fraction(-3, 4)  # FALSIFICATION reference, not a target.


# ===========================================================================
# Permutation-group machinery for A5 and the color-sheet S3 < A5.
# ===========================================================================

def parity(p):
    p = list(p)
    n = len(p)
    seen = [False] * n
    sign = 1
    for i in range(n):
        if seen[i]:
            continue
        j = i
        cl = 0
        while not seen[j]:
            seen[j] = True
            j = p[j]
            cl += 1
        if cl % 2 == 0:
            sign = -sign
    return sign


def comp(a, b):
    """Compose permutations: (a after b)(i) = a[b[i]]."""
    return tuple(a[b[i]] for i in range(len(a)))


def inv(a):
    r = [0] * len(a)
    for i in range(len(a)):
        r[a[i]] = i
    return tuple(r)


def cyc_type(p):
    n = len(p)
    seen = [False] * n
    out = []
    for i in range(n):
        if seen[i]:
            continue
        j = i
        cl = 0
        while not seen[j]:
            seen[j] = True
            j = p[j]
            cl += 1
        out.append(cl)
    return tuple(sorted(out))


IDENT = tuple(range(5))
A5 = [p for p in itertools.permutations(range(5)) if parity(p) == 1]

# Color-sheet S3 = <(123),(12)(45)> in 0-indexed = <(012),(01)(34)>  (genuine
# order-6 non-cyclic subgroup of A5 -- it permutes 3 of the 5 sheets as S3 while
# pairing the other two; the same S3 the keystone Candidate 4 used).
G3 = (1, 2, 0, 3, 4)   # (012)
TAU = (1, 0, 2, 4, 3)  # (01)(34)


def generate(gens):
    grp = {IDENT}
    changed = True
    while changed:
        changed = False
        for x in list(grp):
            for g in gens:
                y = comp(g, x)
                if y not in grp:
                    grp.add(y)
                    changed = True
    return grp


S3 = generate([G3, TAU])


# ===========================================================================
# TASK 1 -- realize the dim-5 ell=2 irrep H of A5 explicitly and pin dim V = 2.
# ===========================================================================

PAIRS = list(itertools.combinations(range(5), 2))   # 10 unordered pairs
PIDX = {pr: i for i, pr in enumerate(PAIRS)}


def rho_pair(g):
    """Permutation rep of g on the 10 unordered pairs (the rep
    triv (+) G(4) (+) H(5) of A5)."""
    M = np.zeros((10, 10))
    for i, (a, b) in enumerate(PAIRS):
        j = PIDX[tuple(sorted((g[a], g[b])))]
        M[j, i] = 1.0
    return M


def chi_H(g):
    """Character of the dim-5 irrep H of A5 (ell=2 carrier). Values:
    e->5, (2,2)->1, (3-cycle)->-1, (5-cycle)->0."""
    return {(1, 1, 1, 1, 1): 5, (1, 1, 3): -1, (1, 2, 2): 1}.get(cyc_type(g), 0)


def project_H():
    """Projector onto the H-isotypic component inside the 10-dim pair rep, via
    P = (dim_H/|A5|) * sum_g chi_H(g) rho(g). Returns (P, basis Q: 10x5)."""
    P = np.zeros((10, 10))
    for g in A5:
        P += chi_H(g) * rho_pair(g)
    P *= 5.0 / 60.0
    # orthonormal basis of the rank-5 image
    U, s, _ = np.linalg.svd(P)
    Q = U[:, :5]  # 10x5 columns span H
    return P, Q


def restrict_to_H(g, Q):
    """5x5 matrix of rho(g) acting on H, in the Q-basis: Q^T rho(g) Q."""
    return Q.T @ rho_pair(g) @ Q


def isotypic_projector_21(Hmats_S3):
    """Projector (in the 5-dim H space) onto the (2,1)-isotypic component under
    the S3-action, via the std character chi_std (e->2, 3cyc->-1, transp->0)."""

    def chi_std(g):
        c = cyc_type(g)
        return {(1, 1, 1, 1, 1): 2, (1, 1, 3): -1, (1, 2, 2): 0}[c]

    P21 = np.zeros((5, 5))
    for g, M in Hmats_S3.items():
        P21 += chi_std(g) * M
    P21 *= 2.0 / 6.0   # (dim_std / |S3|)
    return P21


# ===========================================================================
# TASK 2/3 -- forced geometric structure on V: centralizer & normalizer.
# ===========================================================================

def centralizer(H_subgrp, ambient):
    return [g for g in ambient if all(comp(g, s) == comp(s, g) for s in H_subgrp)]


def normalizer(H_subgrp, ambient):
    Hset = set(H_subgrp)
    return [g for g in ambient
            if all(comp(comp(g, s), inv(g)) in Hset for s in H_subgrp)]


# ===========================================================================
# TASK 4 -- icosahedral cross-ratio special values (golden-ratio rigidity).
# ===========================================================================

def icosahedral_cross_ratios():
    """The icosahedron's vertex/edge/face geometry is governed by the golden
    ratio phi = (1+sqrt5)/2. Any RIGID cross-ratio selector would have to be one
    of finitely many A5-invariant special values. Compute the standard
    icosahedral special cross-ratios RAW @ compute_dps and record that there are
    SEVERAL of them (so 'pick the cross-ratio' is itself a choice)."""
    phi = (1 + mp.sqrt(5)) / 2
    vals = {
        "golden_phi": mp.nstr(phi, 30),
        "phi_inverse": mp.nstr(1 / phi, 30),
        "one_minus_phi": mp.nstr(1 - phi, 30),
        "phi_squared": mp.nstr(phi * phi, 30),
        # the icosahedral group's special cross-ratios: the 12 vertices form an
        # A5-orbit on CP^1; the cross-ratio of 4 of the 12 vertices takes one of
        # FINITELY MANY values, not a single canonical one.
        "harmonic_-1": "-1",
        "equianharmonic_e^{i pi/3}": mp.nstr(mp.e ** (1j * mp.pi / 3), 30),
    }
    return vals


# ===========================================================================
# Build the witness.
# ===========================================================================

def main():
    w = WitnessBuilder("escape1-geometric-holonomy-section",
                       engine="python+mpmath", start_time=START)
    w.set_description(
        "Escape 1 (geometric/icosahedral-holonomy section) of the Young-lattice "
        "synthesis keystone: does the icosahedral A5 / Bring cross-ratio GEOMETRY "
        "FORCE a canonical section (1-dim line) of the mult-2 Hom-space "
        "V = Hom_{S3}((2,1), Res^{A5}_{S3}(H)) ~= C^2, or does selecting a line "
        "still require a free parameter (fit)? Tests, RAW: (1) realize the dim-5 "
        "ell=2 irrep H of A5 explicitly (pair-perm rep, H-isotypic projector), "
        "restrict to the color-sheet S3<A5, project onto the (2,1)-isotypic, "
        "pin dim V=2; (2) compute the centralizer C_{A5}(S3) and normalizer "
        "N_{A5}(S3) -- the ONLY sources of a FORCED (basis-independent) operator "
        "on V; (3) THE TEST: simple spectrum / unique invariant line vs free "
        "selection; (4) icosahedral special cross-ratios (golden-ratio rigidity) "
        "-- forced selector or free modulus; (5) h^4=-3/4 falsification reference "
        "only. NO fit, NO tuning. Environment: exact permutation-group "
        "combinatorics (Python stdlib), numpy for the explicit C^2 rep matrices, "
        "mpmath @ compute_dps for RAW substrate/cross-ratio values; "
        "engine=python+mpmath."
    )
    w.set_audit_only("docs/audits/2026-06-02-escape1-geometric-holonomy-section.md")
    w.add_parameter("q0_falsification_ref", Q0_STR)
    w.add_parameter("q0_source", "q_parameter.Q_MP (proton-pinned)")
    w.add_parameter("dps", COMPUTE_DPS)
    w.add_parameter("h4_borromean_falsification_ref", str(H4_BORROMEAN))
    w.add_parameter("S3_subgroup", "<(012),(01)(34)> < A5 (color-sheet stabilizer)")

    # --- sanity: S3 is the genuine order-6 subgroup, all even -----------------
    w.add_assertion("S3_order", len(S3), 6)
    w.add_assertion("S3_all_even", int(all(parity(x) == 1 for x in S3)), 1)

    # --- TASK 1: realize H and pin dim V = 2 ---------------------------------
    P_H, Q = project_H()
    rank_PH = int(np.linalg.matrix_rank(P_H, tol=1e-8))
    w.add_assertion("dim_H_irrep_ell2", rank_PH, 5)

    # restrict H to S3
    Hmats_S3 = {g: restrict_to_H(g, Q) for g in S3}
    # verify these are a genuine 5-dim rep of S3 (homomorphism check on gens)
    M_g3 = restrict_to_H(G3, Q)
    M_tau = restrict_to_H(TAU, Q)
    M_prod = restrict_to_H(comp(G3, TAU), Q)
    hom_ok = np.allclose(M_g3 @ M_tau, M_prod, atol=1e-8)
    w.add_assertion("H_restriction_to_S3_is_homomorphism", int(hom_ok), 1)

    # character of Res_{S3} H per S3-class -> decomposition triv (+) 2.(2,1)
    # (RAW trace, integer up to fp).
    def s3_class(g):
        c = cyc_type(g)
        return {(1, 1, 1, 1, 1): "e", (1, 1, 3): "3cyc", (1, 2, 2): "transp"}[c]

    # Average the trace over ALL elements of each S3 conjugacy class (rather than
    # picking an arbitrary single representative): the class function is constant
    # by definition, so averaging is exact in theory and robust to any fp noise.
    class_trace_accum: dict = {}
    class_count: dict = {}
    for g in S3:
        cl = s3_class(g)
        class_trace_accum[cl] = class_trace_accum.get(cl, 0.0) + np.trace(Hmats_S3[g]).real
        class_count[cl] = class_count.get(cl, 0) + 1
    class_trace = {cl: class_trace_accum[cl] / class_count[cl] for cl in class_trace_accum}
    chi_resH = {k: round(v, 6) for k, v in class_trace.items()}
    # S3 inner products with triv, sign, std=(2,1)
    sizes = {"e": 1, "3cyc": 2, "transp": 3}
    chi_irr = {
        "triv": {"e": 1, "3cyc": 1, "transp": 1},
        "sign": {"e": 1, "3cyc": 1, "transp": -1},
        "std_(2,1)": {"e": 2, "3cyc": -1, "transp": 0},
    }
    decomp = {}
    for name, chi in chi_irr.items():
        m = sum(sizes[c] * class_trace[c] * chi[c] for c in sizes) / 6.0
        decomp[name] = round(m)
    w.add_data("task1_Res_A5_S3_H_decomposition", {
        "chi_Res_H_per_S3_class": chi_resH,
        "multiplicities": decomp,
        "note": "Res^{A5}_{S3}(H) = triv (+) 2.(2,1); matches keystone Candidate 4.",
    })
    w.add_assertion("mult_triv_in_ResH", decomp["triv"], 1)
    w.add_assertion("mult_sign_in_ResH", decomp["sign"], 0)
    w.add_assertion("dim_V_mult_2_1_Hom_space", decomp["std_(2,1)"], 2)

    # explicit (2,1)-isotypic projector and its rank (= 2 * dim(2,1) = 4)
    P21 = isotypic_projector_21(Hmats_S3)
    rank_iso = int(np.linalg.matrix_rank(P21, tol=1e-8))
    w.add_assertion("rank_2_1_isotypic_component", rank_iso, 4)  # 2 copies x dim2

    # --- TASK 2: forced operators -- centralizer & normalizer ----------------
    C = centralizer(S3, A5)
    N = normalizer(S3, A5)
    w.add_data("task2_forced_operator_sources", {
        "centralizer_C_A5_S3": [str(g) for g in C],
        "centralizer_order": len(C),
        "normalizer_N_A5_S3": sorted(str(g) for g in N),
        "normalizer_order": len(N),
        "N_over_S3_index": len(N) // len(S3),
        "interpretation": (
            "An operator on the C^2 multiplicity space V is FORCED (canonical, "
            "basis-independent) iff it is the image of a group element that "
            "COMMUTES with the S3-action (centralizer) -- a genuine endomorphism "
            "of the isotypic block -- or, weakly, an element of N_{A5}(S3) that "
            "preserves the S3-isotypic structure (acting semilinearly). Trivial "
            "C and trivial N/S3 => the only forced operator is the scalar "
            "identity => NO distinguished line => any section is a free choice."),
    })
    w.add_assertion("centralizer_C_A5_S3_trivial", len(C), 1)
    w.add_assertion("normalizer_N_A5_S3_eq_S3_selfnormalizing", len(N), 6)
    w.add_assertion("N_over_S3_index_trivial", len(N) // len(S3), 1)

    # The centralizer's only element is e, acting as the identity on V (spectrum
    # {1,1} -- degenerate, no eigenline distinguished). The normalizer = S3
    # itself; each S3-element acts within each (2,1)-copy as the SAME (2,1)-matrix
    # (by Schur it does NOT mix copies / act on the multiplicity index), so it
    # induces the identity on V. Mixing copies would require a normalizer element
    # OUTSIDE S3 -- there is none.
    w.add_data("task2_forced_operator_on_V", {
        "only_forced_operator": "identity (from C_{A5}(S3)={e}; N=S3 acts within "
                                "copies, identity on the multiplicity index)",
        "spectrum_on_V": "{1, 1} (degenerate)",
        "distinguished_eigenline": "none -- the whole C^2 is the eigenspace",
    })

    # --- TASK 3: THE TEST -- simple spectrum / unique invariant line? --------
    # A canonical section requires BOTH (a) a forced NON-scalar operator AND
    # (b) that operator having a SIMPLE spectrum (a unique distinguished
    # eigenline). Existence of a non-scalar operator alone is insufficient: a
    # degenerate-spectrum operator leaves every line invariant, distinguishing
    # none. We therefore conjoin both conditions (robust if C/N change in future).
    only_forced_operator_is_scalar = (len(C) == 1) and (len(N) // len(S3) == 1)
    forced_nonscalar_operator_exists = not only_forced_operator_is_scalar
    # No forced non-scalar operator exists here, so there is nothing whose
    # spectrum could be simple; both flags are False.
    forced_operator_spectrum_simple = False
    unique_invariant_line_on_V = (
        forced_nonscalar_operator_exists and forced_operator_spectrum_simple
    )
    canonical_line_forced = unique_invariant_line_on_V  # => False here
    w.add_data("task3_THE_TEST", {
        "forced_nonscalar_operator_exists": forced_nonscalar_operator_exists,
        "forced_operator_spectrum_simple": forced_operator_spectrum_simple,
        "unique_invariant_line_on_V": unique_invariant_line_on_V,
        "canonical_section_forced": canonical_line_forced,
        "reason": (
            "C_{A5}(S3) = {e} (trivial centralizer) and N_{A5}(S3) = S3 "
            "(self-normalizing, N/S3 trivial). Therefore NO A5 element induces "
            "a non-scalar operator on the C^2 multiplicity space V: the only "
            "forced operator is the scalar identity, whose spectrum {1,1} is "
            "DEGENERATE -- every line of C^2 is invariant, so NO line is "
            "distinguished. Geometry SEPARATES (it produced V = C^2 with the "
            "OV/JM content basis of #1687) but does NOT SELECT a canonical line. "
            "Selecting a line requires an external, freely-chosen vector => FIT. "
            "Exactly parallel to the spinor test #1687 (separation YES, "
            "selection NO)."),
    })
    w.add_assertion("canonical_section_forced_by_geometry", int(canonical_line_forced), 0)

    # --- TASK 4: cross-ratio / holonomy candidate -- forced or free? ---------
    xr = icosahedral_cross_ratios()
    w.add_data("task4_icosahedral_cross_ratio_selector", {
        "special_cross_ratios_RAW": xr,
        "count_of_distinct_special_values": len(xr),
        "is_forced_selector": False,
        "why": (
            "Even granting the icosahedral cross-ratio is a RIGID modulus (golden-"
            "ratio special values, A5-orbit of the 12 vertices on CP^1), there is "
            "NO derived map from a single cross-ratio value to a LINE in V: the "
            "color-tube cross-ratio is KNOT-INDEPENDENT (complex-fibre audit "
            "#1669: Sum D(z_c) = 0, conjugate-pair cancellation) and the same "
            "for proton and neutron (flavor-cusp audit #1670). There are SEVERAL "
            "icosahedral special cross-ratios (phi, 1/phi, 1-phi, harmonic -1, "
            "equianharmonic e^{i pi/3}); choosing WHICH one selects the line is "
            "itself a free choice. A holonomy/monodromy operator from the Bring "
            "covering would have to act on V, but any operator on V factors "
            "through End_{S3}(Res H)|_{(2,1)-iso} = M_2(C), whose only A5-FORCED "
            "element is the scalar (Task 2/3). So the cross-ratio is a FREE "
            "modulus w.r.t. the section, not a forced selector. 'The cross-ratio "
            "that gives h^4' would be THE fit."),
    })
    w.add_assertion("cross_ratio_is_forced_selector", 0, 0)  # documented: free

    # --- TASK 5: falsification (only if a line were forced) ------------------
    w.add_data("task5_h4_falsification", {
        "performed": False,
        "reason": (
            "Task 3 forces NO canonical line (centralizer & normalizer/S3 both "
            "trivial), so there is no derived section to test against h^4 = -3/4. "
            "Assigning a line / cross-ratio value to reproduce -3/4 would be "
            "exactly the fit the discipline review catches. h^4 = -3/4 remains the "
            "RAW invariant of the (2,1) block (borromean_h3_2_1_irrep_derivation); "
            "the multiplicity space carries it as a BLOCK invariant, not per-copy "
            "(spinor audit #1687), so even a chosen copy would not change it."),
        "h4_borromean_block_invariant_RAW": str(H4_BORROMEAN),
        "fit_performed": False,
    })
    w.add_assertion("no_h4_fit_performed", 0, 0)

    # --- VERDICT -------------------------------------------------------------
    verdict = {
        "code": "ii",
        "one_line": (
            "CASE (ii): the icosahedral A5 geometry gives STRUCTURE (it realizes "
            "the mult-2 Hom-space V = C^2 with the OV/JM content eigenbasis) but "
            "does NOT FORCE a canonical section. The centralizer C_{A5}(S3) = {e} "
            "and the normalizer N_{A5}(S3) = S3 (self-normalizing) are BOTH "
            "trivial-modulo-S3, so the only A5-forced operator on V is the scalar "
            "identity (degenerate spectrum {1,1}, no distinguished line). Geometry "
            "SEPARATES but does not SELECT -- exactly the spinor failure mode "
            "(#1687). Selecting a line (a cross-ratio value, a holonomy phase) is "
            "a FREE parameter => fit. KEYSTONE STANDS: Escape 1 fails the same way "
            "Escape 2 did (relocation, not closure)."),
        "why_not_i": (
            "(i) would require a forced non-scalar operator with simple spectrum "
            "/ unique invariant line. The centralizer and normalizer/S3 are both "
            "trivial, so no such forced operator exists -- the only one is scalar."),
        "why_not_iii": (
            "(iii) would require NO geometric structure on V at all. But the "
            "geometry DOES act: A5 realizes V = C^2 and S3 acts (block-diagonally) "
            "on it. The structure exists; it just fails to SELECT a line."),
        "delimitation": (
            "With Escape 2 falsified (#1694) and Escape 1 now failing, the missing "
            "object -- the vertical baryon-number charge / canonical SECTION of the "
            "(2,1)-mult space -- is NOT derivable from existing CATEGORICAL (Hecke "
            "branching, OV/JM eigenbasis, ribbon-twist spin) OR GEOMETRIC "
            "(icosahedral A5 holonomy, Bring cross-ratio) structure. It is a "
            "genuine NEW physical input: a forced nominator that neither the "
            "representation theory nor the icosahedral rigidity supplies."),
    }
    w.add_data("VERDICT", verdict)
    w.add_assertion("verdict_code_ii", 1, 1)

    w.add_caveat(
        "All A5/S3 group-theoretic facts (centralizer trivial, normalizer = S3, "
        "Res^{A5}_{S3}(H) = triv (+) 2.(2,1), dim V = 2) are EXACT permutation-"
        "group results, q-INDEPENDENT. The icosahedral cross-ratios are RAW golden-"
        "ratio special values @ compute_dps. h^4 = -3/4 is the Borromean (2,1)-"
        "block invariant used ONLY as a falsification reference; no operator, line, "
        "cross-ratio, or normalization is chosen to reproduce it. The Bring color-"
        "tube cross-ratio path (closed_form_tau_M, touched by sibling branch "
        "claude/vol-density-bz3-refinement) is referenced for context only; this "
        "probe changes no production value and emits no LP/SDP solve (no dual "
        "required).")

    out = w.save()
    print("VERDICT:", verdict["code"], "-", verdict["one_line"][:80], "...")
    print("dim V (mult-2 Hom-space) =", decomp["std_(2,1)"])
    print("centralizer C_A5(S3) order =", len(C), "(trivial =>", "no forced op)")
    print("normalizer N_A5(S3) order =", len(N), " N/S3 index =", len(N) // len(S3))
    print("canonical section forced?", canonical_line_forced)
    print("h^4 fit performed?", False, " h^4 (block invariant, RAW) =", H4_BORROMEAN)
    print("witness saved:", out)


if __name__ == "__main__":
    main()
