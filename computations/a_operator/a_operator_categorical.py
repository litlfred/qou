"""Categorical interface operator A^λ_{ξν}(I) — closure path (b), prototype.

Replaces the least-squares *fitted* A^λ_{ξν}(I) of
`A_operator_extract_at_level.py` with an *categorical* construction that is
universal by construction (no test-word dependence), so the operator-valued
Wenzl branching combiner closes for A ≥ 3.

## Structural finding (see design doc)

The combiner peels one nucleon:

    χ^λ(W_inner · I · β_block)
      = Σ_{ξ⊢n-3, ν⊢3} Tr_{V_ξ⊗V_ν}( A^λ_{ξν}(I) · (ρ_ξ(W_inner) ⊗ ρ_ν(β_block)) )

with I = c·σ_{n-4} + d·1 the *bridge generator* between the Young-subalgebra
factors H_{n-3} × H_3, deformed by the flavour coefficients
(pp=(1,0), nn=(1,-h), pn=(1,-h/2)).

A^λ_{ξν}(I) is NOT a quantity to fit. It is the (ξ,ν)-isotypic diagonal block
of the seminormal interface-generator matrix ρ_λ(I), transported into the
V_ξ⊗V_ν coordinates by the branching embedding V_ξ⊗V_ν ↪ Res V_λ:

    A^λ_{ξν}(I) = Π_{ξν} ρ_λ(I) Π_{ξν}          (in V_ξ⊗V_ν coords).

At I = identity (c=0, d=1, i.e. a disjoint tensor braid with no bridge):

    A^λ_{ξν}(1) = c^λ_{ξν} · 1_{d_ξ d_ν},
    χ^λ(β_1 ⊗ β_2) = Σ_{ξ,ν} c^λ_{ξν} χ^ξ(β_1) χ^ν(β_2),

which is exactly the existing character-level Wenzl LR bridge
(tools/hecke-engine/src/wenzl_lr.rs :: chi_via_lr_2way). The interface operator
is the *bridge-generator deformation* of that LR scalar.

## Status (prototype / first increment)

  - PREFLIGHT STEP 1 — `verify_chi_disjoint_reduction` (this file): the
    I=identity reduction χ^λ(disjoint) = Σ c^λ_{ξν} χ^ξ χ^ν, cross-checked
    against the seminormal ground truth `chi_lambda_fast_mp`. RUNNABLE. LOSSY:
    `chi_lambda_fast_mp` is f64-limited at the source, so this validates the
    STRUCTURAL identity at ~1e-14; the exact 1e-25 verification is step 2.
  - PREFLIGHT STEP 1b — `verify_dimension_identity`: d_λ = Σ c^λ_{ξν} d_ξ d_ν.
    RUNNABLE.
  - STEP 2 — `categorical_A_interface` (deuteron, bridge ≠ 1): TODO(closure-b).
  - STEP 3 — H_9 universality: TODO(closure-b).

This file changes NO production path — the combiner still routes A≥3 through the
lossless fine-Bratteli transfer matrix. It establishes the verified spec the
remaining closure-b work implements against.

Design: docs/audits/2026-06-16-categorical-interface-operator-closure-b-design.md
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 5/6, 2026-06-02): keeps
# flat-namespace imports working from the a_operator/ subdirectory.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import argparse
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from char_fast import chi_lambda_fast_mp  # noqa: E402
from lr_coefficients import get_lr_table, partitions_of  # noqa: E402

try:
    import pyhecke_native as _pyn  # exact MPFR seminormal characters
    _HAVE_NATIVE = True
except ImportError:  # pragma: no cover
    _pyn = None
    _HAVE_NATIVE = False

# Exact cross-check bar at 50 dps (compute-author §1.1: 1e-25 minimum). Reachable
# only via the native MPFR character path (`pyhecke_native.chi_lambda_braid_mpfr`),
# which evaluates the Hoefsmit seminormal form at arbitrary precision — unlike
# `char_fast.chi_lambda_fast_mp`, whose seminormal source entries are f64.
EXACT_TOL = mp.mpf("1e-25")

# LOSSY cross-check bar (f64-limited). `char_fast.chi_lambda_fast_mp` lambdifies
# the seminormal generator matrices from f64-precision source entries
# (`_cached_seminormal` is numpy/f64), so its effective precision is ~1e-14
# despite the mpmath arithmetic. This preflight therefore validates the
# STRUCTURAL identity at f64; the exact 50-dps / 1e-25 verification (compute-
# author §1.1) needs an exact-rational seminormal path and is part of closure-b
# step 2 (see design doc). The pass test is combined abs-OR-rel so a near-zero
# character (tiny |χ| inflating the relative metric) is judged on its absolute
# residual.
PREFLIGHT_TOL_ABS = mp.mpf("1e-11")
PREFLIGHT_TOL_REL = mp.mpf("1e-11")

# Interface (bridge-generator) flavour coefficients (c, d) for I = c·σ + d·1.
# Matches A_operator_extract_at_level.INTERFACE_COEFS.
INTERFACE_COEFS: dict[str, tuple[str, str]] = {
    # d-coefficient is "0", "-h", or "-h/2" — resolved against h at q_0.
    "pp": ("1", "0"),
    "nn": ("1", "-h"),
    "pn": ("1", "-h/2"),
}


def q0_mp(dps: int = 50) -> mp.mpf:
    """Substrate q_0 as a 50-dps mpmath.mpf (arbitrary-precision findroot)."""
    mp.mp.dps = max(mp.mp.dps, dps + 10)
    from q_parameter import q_at
    return q_at(dps)


# Dimension of the seminormal/Specht module V_λ (= # SYT of shape λ), via the
# hook-length formula. Centralised in `partition_utils` (single source of truth;
# Gemini review #2353) — aliased here so existing `partition_dim` callers (incl.
# a_operator_gauge_align) keep working.
from partition_utils import dim_lambda as partition_dim  # noqa: E402


def verify_dimension_identity(n_inner: int, n_block: int) -> dict:
    """Preflight 1b: d_λ = Σ_{ξ,ν} c^λ_{ξν} d_ξ d_ν for every λ ⊢ n_inner+n_block.

    This is the operator-level shadow of the restriction
    Res^{H_n}_{H_{n_inner}×H_{n_block}} V_λ = ⊕ c^λ_{ξν} V_ξ ⊠ V_ν
    (cf. tools/hecke-engine/src/cross_level_embedding.rs :: verify_edge).
    """
    n = n_inner + n_block
    lr = get_lr_table(n_inner, n_block)
    parts_outer = partitions_of(n)
    parts_inner = partitions_of(n_inner)
    parts_block = partitions_of(n_block)
    dims_inner = {xi: partition_dim(xi) for xi in parts_inner}
    dims_block = {nu: partition_dim(nu) for nu in parts_block}

    failures = []
    for lam in parts_outer:
        lhs = partition_dim(lam)
        rhs = 0
        for xi in parts_inner:
            for nu in parts_block:
                c = lr.get((xi, nu, lam), 0)
                if c:
                    rhs += c * dims_inner[xi] * dims_block[nu]
        if lhs != rhs:
            failures.append({"lambda": list(lam), "d_lambda": lhs, "sum": rhs})
    return {
        "n_inner": n_inner, "n_block": n_block, "n": n,
        "n_partitions": len(parts_outer),
        "all_passed": not failures,
        "failures": failures,
    }


def disjoint_word(inner_word: list[tuple], block_word: list[tuple],
                  n_inner: int) -> list[tuple]:
    """Build the H_{n_inner+n_block} word W_inner · β_block with NO bridge
    generator (I = identity): block gens shift by n_inner so the two factors
    act on disjoint strand sets {0..n_inner-1} and {n_inner..n-1}."""
    out = list(inner_word)
    out += [(c, d, g + n_inner) for (c, d, g) in block_word]
    return out


def _test_words(n: int, h: mp.mpf) -> list[list[tuple]]:
    """A small diverse H_n test-word family exercising the +1 (σ) and
    -h / -h/2 (Hecke-negative / averaged) channels."""
    gens = list(range(n - 1))
    words: list[list[tuple]] = [[]]
    for g in gens:
        words.append([(mp.mpf(1), mp.mpf(0), g)])           # σ_g
    for g in gens[:-1]:
        words.append([(mp.mpf(1), mp.mpf(0), g),
                      (mp.mpf(1), mp.mpf(0), g + 1)])        # σ_g σ_{g+1}
    for g in gens[:2]:
        words.append([(mp.mpf(1), -h, g)])                  # σ_g^{-1}-type
        words.append([(mp.mpf(1), -h / 2, g)])              # averaged
    if n >= 3:
        words.append([(mp.mpf(1), mp.mpf(0), 0),
                      (mp.mpf(1), mp.mpf(0), 1),
                      (mp.mpf(1), mp.mpf(0), 0)])            # trefoil-like
    return words


def verify_chi_disjoint_reduction(n_inner: int, n_block: int,
                                  dps: int = 50) -> dict:
    """Preflight 1: the I=identity branching identity

        χ^λ(W_inner · β_block)  ==  Σ_{ξ,ν} c^λ_{ξν} χ^ξ(W_inner) χ^ν(β_block)

    cross-checked against the seminormal ground truth `chi_lambda_fast_mp`
    (which evaluates χ^λ directly at H_{n_inner+n_block}). This is
    `A^λ_{ξν}(1) = c^λ_{ξν}·1` — the LR-scalar limit of the categorical interface
    operator — verified end-to-end. LOSSY: `chi_lambda_fast_mp` is f64-limited
    at the source (see PREFLIGHT_TOL_ABS note), so this validates the STRUCTURAL
    identity at ~1e-14, not at the 1e-25 L1 floor.
    """
    mp.mp.dps = dps + 10
    q = q0_mp(dps)
    h = q - 1 / q
    n = n_inner + n_block
    lr = get_lr_table(n_inner, n_block)
    parts_outer = partitions_of(n)
    parts_inner = partitions_of(n_inner)
    parts_block = partitions_of(n_block)

    inner_words = _test_words(n_inner, h)
    block_words = _test_words(n_block, h)

    max_abs = mp.mpf(0)          # worst absolute residual (all checks)
    max_rel_wc = mp.mpf(0)       # worst relative residual on well-conditioned χ
    n_checks = 0
    n_fail = 0
    worst = None
    for wi in inner_words:
        # Pre-cache χ^ξ(W_inner) for all ξ.
        chi_xi = {xi: chi_lambda_fast_mp(xi, wi, q) for xi in parts_inner}
        for wb in block_words:
            chi_nu = {nu: chi_lambda_fast_mp(nu, wb, q) for nu in parts_block}
            full = disjoint_word(wi, wb, n_inner)
            for lam in parts_outer:
                lhs = chi_lambda_fast_mp(lam, full, q)            # ground truth
                rhs = mp.mpc(0)
                for xi in parts_inner:
                    for nu in parts_block:
                        c = lr.get((xi, nu, lam), 0)
                        if c:
                            rhs += c * chi_xi[xi] * chi_nu[nu]    # I=identity sum
                ad = abs(lhs - rhs)
                rel = ad / max(abs(lhs), abs(rhs), mp.mpf("1e-30"))
                # Combined abs-OR-rel test (near-zero χ judged on absolute).
                ok = (ad < PREFLIGHT_TOL_ABS) or (rel < PREFLIGHT_TOL_REL)
                if ad > max_abs:
                    max_abs = ad
                if abs(lhs) > mp.mpf("1e-3") and rel > max_rel_wc:
                    max_rel_wc = rel
                if not ok:
                    n_fail += 1
                    if worst is None:
                        worst = {"lambda": list(lam), "inner_len": len(wi),
                                 "block_len": len(wb),
                                 "abs_residual": mp.nstr(ad, 6),
                                 "rel_residual": mp.nstr(rel, 6)}
                n_checks += 1
    return {
        "n_inner": n_inner, "n_block": n_block, "n": n, "dps": dps,
        "precision_note": "LOSSY f64 (~1e-14) — chi_lambda_fast_mp is "
                          "f64-limited at the seminormal source",
        "n_checks": n_checks, "n_fail": n_fail,
        "max_absolute_residual": mp.nstr(max_abs, 8),
        "max_relative_residual_wellcond": mp.nstr(max_rel_wc, 8),
        "tolerance_abs": mp.nstr(PREFLIGHT_TOL_ABS, 4),
        "tolerance_rel": mp.nstr(PREFLIGHT_TOL_REL, 4),
        "all_passed": n_fail == 0,
        "worst_failure": worst,
    }


# ──────────────────────────────────────────────────────────────────────
# Exact (1e-25) path — native MPFR seminormal characters.
# ──────────────────────────────────────────────────────────────────────

def _native_chi(lam: tuple[int, ...], braid: list[tuple[int, int]],
                q_str: str, dps: int) -> mp.mpf:
    """Exact χ^λ(braid) via pyhecke_native at `dps` digits.

    `braid` is a list of (sign, gen0) with sign ∈ {+1,-1} (σ or σ⁻¹) and gen0
    a 0-based generator index; the native API uses 1-based indices, so we add 1.
    """
    nat = [(int(s), int(g) + 1) for (s, g) in braid]
    return mp.mpf(_pyn.chi_lambda_braid_mpfr(list(lam), nat, q_str, dps))


def _braid_test_words(n: int) -> list[list[tuple[int, int]]]:
    """Diverse *pure-braid* H_n test words (σ_g, σ_g⁻¹ and products only — no
    averaged/Hecke factor, so the exact native braid-character path applies)."""
    gens = list(range(n - 1))
    words: list[list[tuple[int, int]]] = [[]]
    for g in gens:
        words.append([(1, g)])                 # σ_g
        words.append([(-1, g)])                # σ_g⁻¹
    for g in gens[:-1]:
        words.append([(1, g), (1, g + 1)])     # σ_g σ_{g+1}
        words.append([(1, g), (-1, g + 1)])    # σ_g σ_{g+1}⁻¹
    if n >= 3:
        words.append([(1, 0), (1, 1), (1, 0)])   # trefoil-like
        words.append([(-1, 0), (1, 1), (-1, 0)])
    return words


def disjoint_braid(inner: list[tuple[int, int]], block: list[tuple[int, int]],
                   n_inner: int) -> list[tuple[int, int]]:
    """Disjoint product (I=identity): block gens shift by n_inner (0-based)."""
    return list(inner) + [(s, g + n_inner) for (s, g) in block]


def verify_chi_disjoint_reduction_exact(n_inner: int, n_block: int,
                                        dps: int = 50) -> dict:
    """Preflight step 1, EXACT (1e-25): the I=identity branching identity

        χ^λ(W·β) == Σ_{ξ,ν} c^λ_{ξν} χ^ξ(W) χ^ν(β)

    with every character evaluated by the native MPFR Hoefsmit kernel at `dps`
    digits. Upgrades `verify_chi_disjoint_reduction` (f64) to the L1 floor.
    """
    if not _HAVE_NATIVE:
        return {"skipped": True,
                "reason": "pyhecke_native unavailable — build via "
                          "`pip install ./tools/pyhecke-native` (compute-author §0.1)"}
    mp.mp.dps = dps + 10
    q = q0_mp(dps)
    q_str = mp.nstr(q, dps)
    n = n_inner + n_block
    lr = get_lr_table(n_inner, n_block)
    parts_outer = partitions_of(n)
    parts_inner = partitions_of(n_inner)
    parts_block = partitions_of(n_block)

    inner_words = _braid_test_words(n_inner)
    block_words = _braid_test_words(n_block)

    max_abs = mp.mpf(0)
    max_rel_wc = mp.mpf(0)
    n_checks = 0
    n_fail = 0
    worst = None
    for wi in inner_words:
        chi_xi = {xi: _native_chi(xi, wi, q_str, dps) for xi in parts_inner}
        for wb in block_words:
            chi_nu = {nu: _native_chi(nu, wb, q_str, dps) for nu in parts_block}
            full = disjoint_braid(wi, wb, n_inner)
            for lam in parts_outer:
                lhs = _native_chi(lam, full, q_str, dps)
                rhs = mp.mpf(0)
                for xi in parts_inner:
                    for nu in parts_block:
                        c = lr.get((xi, nu, lam), 0)
                        if c:
                            rhs += c * chi_xi[xi] * chi_nu[nu]
                ad = abs(lhs - rhs)
                rel = ad / max(abs(lhs), abs(rhs), mp.mpf("1e-40"))
                ok = (ad < EXACT_TOL) or (rel < EXACT_TOL)
                if ad > max_abs:
                    max_abs = ad
                if abs(lhs) > mp.mpf("1e-3") and rel > max_rel_wc:
                    max_rel_wc = rel
                if not ok:
                    n_fail += 1
                    if worst is None:
                        worst = {"lambda": list(lam), "abs_residual": mp.nstr(ad, 6)}
                n_checks += 1
    return {
        "n_inner": n_inner, "n_block": n_block, "n": n, "dps": dps,
        "engine": "pyhecke_native MPFR (exact)",
        "n_checks": n_checks, "n_fail": n_fail,
        "max_absolute_residual": mp.nstr(max_abs, 8),
        "max_relative_residual_wellcond": mp.nstr(max_rel_wc, 8),
        "tolerance": mp.nstr(EXACT_TOL, 4),
        "all_passed": n_fail == 0,
        "worst_failure": worst,
    }


# ──────────────────────────────────────────────────────────────────────
# STEP 2 — operator-level A^λ_{ξν}(I) via exact seminormal matrices.
#
# A^λ_{ξν}(I) = Π_{ξν} ρ_λ(I) Π_{ξν}, the (ξ,ν)-isotypic block of the
# seminormal interface-generator matrix. The isotypic projectors Π_{ξν}
# = P^{(in)}_ξ · P^{(bl)}_ν are built from the central class-sums of the
# two commuting H_3 factors (Lagrange spectral projectors — exact, no
# eigensolve). Because the inner word W and block word β both commute
# with Π_{ξν}, the decomposition
#
#   χ^λ(W·I·β) = Σ_{ξν} Tr[ ρ_λ(W)·(Π_{ξν} ρ_λ(I) Π_{ξν})·ρ_λ(β) ]
#
# is verifiable in the seminormal basis directly (no ρ_ξ⊗ρ_ν gauge
# alignment needed for verification; that alignment is a downstream
# basis-change to feed the combiner / match the fitted extract).
# ──────────────────────────────────────────────────────────────────────

def exact_seminormal_matrices(lam: tuple[int, ...], q_str: str,
                              dps: int) -> tuple[list, int]:
    """Exact mpmath seminormal matrices [ρ_λ(σ_1), …, ρ_λ(σ_{n-1})] (1-indexed
    generators) and the dimension, via the native MPFR binding."""
    sp = _pyn.seminormal_matrices_mpfr(list(lam), q_str, dps)  # per-gen sparse
    if not sp:
        return [], 0
    dim = len(sp[0])
    mats = []
    for gen_rows in sp:
        M = mp.zeros(dim, dim)
        for i, row in enumerate(gen_rows):
            for (j, s) in row:
                M[i, j] = mp.mpf(s)
        mats.append(M)
    return mats, dim


def _class_sum_C2(mats: list, a: int, b: int) -> "mp.matrix":
    """Central class-sum C₂ = σ_a + σ_b + σ_a σ_b σ_a of the H_3 factor on
    generators (a, b) (0-based indices into `mats`)."""
    sa, sb = mats[a], mats[b]
    return sa + sb + sa * sb * sa


def _h3_class_sum_eigenvalues(q_str: str, dps: int) -> dict:
    """Eigenvalue of the H_3 class-sum C₂ on each irrep ν ⊢ 3 (the scalar by
    which the central C₂ acts), via e_ν = χ^ν(C₂)/d_ν using native characters.
    C₂ = σ_1 + σ_2 + σ_1σ_2σ_1 (1-based gens → native words)."""
    words = {"s1": [(1, 1)], "s2": [(1, 2)], "s1s2s1": [(1, 1), (1, 2), (1, 1)]}
    ev = {}
    for nu in partitions_of(3):
        chi_sum = sum(mp.mpf(_pyn.chi_lambda_braid_mpfr(list(nu), w, q_str, dps))
                      for w in words.values())
        ev[nu] = chi_sum / partition_dim(nu)
    return ev


def _lagrange_projectors(C: "mp.matrix", eigenvalues: dict, dim: int) -> dict:
    """Spectral projectors of the central matrix C with known distinct
    eigenvalues {label: e}, via Lagrange interpolation
    P_a = Π_{b≠a} (C - e_b I)/(e_a - e_b). Exact, no eigensolve."""
    I = mp.eye(dim)
    labels = list(eigenvalues)
    projs = {}
    for a in labels:
        ea = eigenvalues[a]
        P = mp.eye(dim)
        for b in labels:
            if b == a:
                continue
            eb = eigenvalues[b]
            P = P * (C - eb * I) * (mp.mpf(1) / (ea - eb))
        projs[a] = P
    return projs


def _trace(M: "mp.matrix") -> "mp.mpf":
    return sum(M[i, i] for i in range(M.rows))


def verify_operator_decomposition_exact(dps: int = 50) -> dict:
    """Step 2 (deuteron, exact 1e-25): verify A^λ_{ξν}(I) = Π_{ξν} ρ_λ(I) Π_{ξν}
    reconstructs χ^λ(W · I · β) for the pn interface, via

      χ^λ(W·I·β) = Σ_{ξν} Tr[ ρ_λ(W) · (Π_{ξν} ρ_λ(I) Π_{ξν}) · ρ_λ(β) ].

    H_6: inner gens σ_1,σ_2 (0-idx 0,1); bridge σ_3 (0-idx 2); block σ_4,σ_5
    (0-idx 3,4). I_pn = σ_3 - (h/2)·1.
    """
    if not _HAVE_NATIVE:
        return {"skipped": True, "reason": "pyhecke_native unavailable"}
    mp.mp.dps = dps + 10
    q = q0_mp(dps)
    q_str = mp.nstr(q, dps)
    h = q - 1 / q
    n = 6
    parts6 = partitions_of(n)

    # H_3 class-sum eigenvalues (same for inner + block factors).
    ev = _h3_class_sum_eigenvalues(q_str, dps)
    evs = list(ev.values())
    min_gap = min(abs(evs[i] - evs[j]) for i in range(len(evs))
                  for j in range(i + 1, len(evs)))

    # Test words: braid words on the inner H_3 (gens 0,1) and block H_3
    # (gens 0,1 → applied at block offset). Use (sign, gen0) pure-braid form.
    def braid_to_factors(braid, h):
        out = []
        for (s, g) in braid:
            out.append((mp.mpf(1), mp.mpf(0) if s > 0 else -h, g))
        return out

    inner_braids = _braid_test_words(3)
    block_braids = _braid_test_words(3)

    def word_matrix(mats, factors):
        dim = mats[0].rows
        M = mp.eye(dim)
        for (c, d, g) in factors:
            M = M * (c * mats[g] + d * mp.eye(dim))
        return M

    max_abs = mp.mpf(0)
    max_rel_wc = mp.mpf(0)
    n_checks = 0
    n_fail = 0
    worst = None
    rank_ok = True

    for lam in parts6:
        mats, dim = exact_seminormal_matrices(lam, q_str, dps)
        if dim == 0:
            continue
        # Isotypic projectors from class-sums (inner gens 0,1; block gens 3,4).
        C_in = _class_sum_C2(mats, 0, 1)
        C_bl = _class_sum_C2(mats, 3, 4)
        P_in = _lagrange_projectors(C_in, ev, dim)   # keyed by ξ ⊢ 3
        P_bl = _lagrange_projectors(C_bl, ev, dim)   # keyed by ν ⊢ 3
        # Bridge interface I_pn = σ_3 (0-idx 2) with d = -h/2.
        I_iface = mats[2] - (h / 2) * mp.eye(dim)
        # Π_{ξν} = P_in[ξ] · P_bl[ν]
        Pi = {(xi, nu): P_in[xi] * P_bl[nu]
              for xi in ev for nu in ev}
        # Rank check: Σ tr(Π_{ξν}) = dim (partition of unity).
        sum_tr = sum(_trace(Pi[k]) for k in Pi)
        if abs(sum_tr - dim) > mp.mpf("1e-20"):
            rank_ok = False

        # A^λ_ξν(I) = Π_ξν ρ_λ(I) Π_ξν is independent of the words W, β —
        # precompute once per λ rather than per (W, β) pair (Gemini review
        # #2353: lifts the projected-interface multiplications out of the
        # nested word loop).
        A_blocks = {k: Pi[k] * I_iface * Pi[k] for k in Pi}

        for wi in inner_braids:
            fi = braid_to_factors(wi, h)
            W = word_matrix(mats, fi)
            for wb in block_braids:
                # block gens shift by 3 (0-idx): block gen g → g+3.
                fb = [(c, d, g + 3) for (c, d, g) in braid_to_factors(wb, h)]
                B = word_matrix(mats, fb)
                # Ground truth χ^λ(W · I · β):
                full = W * I_iface * B
                lhs = _trace(full)
                # Operator decomposition Σ_{ξν} Tr[ W · (Π I Π) · β ]:
                rhs = mp.mpf(0)
                for k in Pi:
                    rhs += _trace(W * A_blocks[k] * B)
                ad = abs(lhs - rhs)
                rel = ad / max(abs(lhs), abs(rhs), mp.mpf("1e-40"))
                ok = (ad < EXACT_TOL) or (rel < EXACT_TOL)
                if ad > max_abs:
                    max_abs = ad
                if abs(lhs) > mp.mpf("1e-3") and rel > max_rel_wc:
                    max_rel_wc = rel
                if not ok:
                    n_fail += 1
                    if worst is None:
                        worst = {"lambda": list(lam),
                                 "abs_residual": mp.nstr(ad, 6)}
                n_checks += 1
    return {
        "n": n, "dps": dps, "interface": "pn",
        "construction": "A^λ_ξν(I) = Π_ξν ρ_λ(I) Π_ξν (class-sum projectors)",
        "h3_classsum_min_eigen_gap": mp.nstr(min_gap, 6),
        "partition_of_unity_ok": rank_ok,
        "n_checks": n_checks, "n_fail": n_fail,
        "max_absolute_residual": mp.nstr(max_abs, 8),
        "max_relative_residual_wellcond": mp.nstr(max_rel_wc, 8),
        "tolerance": mp.nstr(EXACT_TOL, 4),
        "all_passed": (n_fail == 0) and rank_ok,
        "worst_failure": worst,
    }


# ──────────────────────────────────────────────────────────────────────
# STEP 2-gauge / STEP 3 — ρ_ξ⊗ρ_ν alignment + H_9 universality.
# ──────────────────────────────────────────────────────────────────────

def categorical_A_interface(lam: tuple[int, ...], xi: tuple[int, ...],
                            nu: tuple[int, ...], interface: str,
                            n_inner: int, dps: int = 50):
    """TODO(closure-b): the categorical interface operator A^λ_{ξν}(I), I ≠ 1.

    Spec (what this MUST return): the (d_ξ·d_ν)×(d_ξ·d_ν) matrix

        A^λ_{ξν}(I) = Π_{ξν} ρ_λ(I) Π_{ξν}        (in V_ξ⊗V_ν coordinates)

    where ρ_λ(I) = c·ρ_λ(σ_{n_inner-1}) + d·1 is the seminormal
    interface-generator matrix at H_{n_inner+3} (available from
    char_fast._compiled_sigmas), and Π_{ξν} is the orthogonal projector onto
    the (ξ,ν)-isotypic subspace of Res^{H_n}_{H_{n_inner}×H_3} V_λ, followed by
    the branching isomorphism into V_ξ⊗V_ν coordinates.

    Construction (build on existing infra — see design doc §"Construction"):
      1. ρ_λ(σ_{n_inner-1}) at H_n         — char_fast._compiled_sigmas / seminormal.rs
      2. ξ-grouping of the seminormal basis — automatic (chain-adapted)
      3. ν-isotypic projection on each ξ-block via H_3 central idempotents
      4. V_ξ⊗V_ν embedding (the crux ~500 LOC) — operator lift of wenzl_lr.rs
      5. compress ρ_λ(I) into V_ξ⊗V_ν coords

    Verification: must reduce to c^λ_{ξν}·1 at interface=identity (preflight 1,
    already passing), match the full-rank H_6 deuteron extract entrywise (modulo
    the V_ξ⊗V_ν basis gauge), and reconstruct tr_M(D) at 1e-25.
    """
    raise NotImplementedError(
        "closure-b step 2: bridge-generator deformation not yet implemented; "
        "preflight 1 (I=identity reduction) passes — see "
        "docs/audits/2026-06-16-categorical-interface-operator-closure-b-design.md"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n-inner", type=int, default=3,
                        help="inner Young-subalgebra strand count (default 3 = deuteron inner)")
    parser.add_argument("--n-block", type=int, default=3,
                        help="block strand count (default 3 = one nucleon)")
    parser.add_argument("--dps", type=int, default=50)
    parser.add_argument("--emit-witness", action="store_true")
    args = parser.parse_args()

    print("=" * 84)
    print("  Categorical interface operator A^λ_{ξν}(I) — closure-b preflight")
    print("=" * 84)
    print(f"  H_{args.n_inner} × H_{args.n_block} → H_{args.n_inner + args.n_block}"
          f"   (abs tol={mp.nstr(PREFLIGHT_TOL_ABS, 4)}, "
          f"rel tol={mp.nstr(PREFLIGHT_TOL_REL, 4)})")
    print()

    dim_res = verify_dimension_identity(args.n_inner, args.n_block)
    print(f"  [1b] dimension identity d_λ = Σ c^λ_ξν d_ξ d_ν : "
          f"{'PASS' if dim_res['all_passed'] else 'FAIL'} "
          f"({dim_res['n_partitions']} partitions)")
    if not dim_res["all_passed"]:
        for f in dim_res["failures"][:5]:
            print(f"       FAIL λ={f['lambda']}: d_λ={f['d_lambda']} ≠ Σ={f['sum']}")

    print(f"  [1 ] χ^λ disjoint (I=identity) reduction (f64-limited, ~1e-14) ...")
    chi_res = verify_chi_disjoint_reduction(args.n_inner, args.n_block, args.dps)
    print(f"       {'PASS' if chi_res['all_passed'] else 'FAIL'} — "
          f"{chi_res['n_checks']} checks ({chi_res['n_fail']} fail), "
          f"max abs residual = {chi_res['max_absolute_residual']}, "
          f"max rel (well-cond) = {chi_res['max_relative_residual_wellcond']}")
    if not chi_res["all_passed"]:
        print(f"       worst failure: {chi_res['worst_failure']}")

    print(f"  [1x] χ^λ disjoint (I=identity) reduction EXACT (1e-25, native MPFR) ...")
    exact_res = verify_chi_disjoint_reduction_exact(args.n_inner, args.n_block, args.dps)
    if exact_res.get("skipped"):
        print(f"       SKIP — {exact_res['reason']}")
    else:
        print(f"       {'PASS' if exact_res['all_passed'] else 'FAIL'} — "
              f"{exact_res['n_checks']} checks ({exact_res['n_fail']} fail), "
              f"max abs residual = {exact_res['max_absolute_residual']}, "
              f"max rel (well-cond) = {exact_res['max_relative_residual_wellcond']}")
        if not exact_res["all_passed"]:
            print(f"       worst failure: {exact_res['worst_failure']}")
    print()
    print(f"  [2 ] operator A^λ_ξν(I_pn) = Π_ξν ρ_λ(I) Π_ξν, exact decomposition ...")
    op_res = verify_operator_decomposition_exact(args.dps)
    if op_res.get("skipped"):
        print(f"       SKIP — {op_res['reason']}")
    else:
        print(f"       {'PASS' if op_res['all_passed'] else 'FAIL'} — "
              f"{op_res['n_checks']} checks ({op_res['n_fail']} fail), "
              f"partition-of-unity={op_res['partition_of_unity_ok']}, "
              f"max abs residual = {op_res['max_absolute_residual']}")
        if not op_res["all_passed"]:
            print(f"       worst failure: {op_res['worst_failure']}")
    print("  [2g] ρ_ξ⊗ρ_ν gauge alignment (feed combiner)  : TODO(closure-b)")
    print("  [3 ] H_9 universality                        : TODO(closure-b)")
    print()

    exact_ok = exact_res.get("skipped") or exact_res["all_passed"]
    op_ok = op_res.get("skipped") or op_res["all_passed"]
    all_passed = (dim_res["all_passed"] and chi_res["all_passed"]
                  and exact_ok and op_ok)
    print(f"  Preflight verdict: {'ALL PASS' if all_passed else 'FAILURES PRESENT'}")

    if args.emit_witness:
        from witness_base import WitnessBuilder
        b = (WitnessBuilder("a-operator-categorical-preflight", engine="mpmath")
             .set_description(
                 "Closure-b preflight for the categorical interface operator "
                 "A^λ_{ξν}(I): the I=identity reduction A^λ_{ξν}(1)=c^λ_{ξν}·1 "
                 "(Wenzl LR-scalar limit) cross-checked at 50 dps against the "
                 "seminormal ground truth, plus the restriction-dimension "
                 "identity. Steps 2-3 (bridge deformation, H_9 universality) "
                 "are scaffolded TODO(closure-b).")
             .add_parameter("n_inner", args.n_inner)
             .add_parameter("n_block", args.n_block)
             .add_parameter("dps", args.dps)
             .add_data("dimension_identity", dim_res)
             .add_data("chi_disjoint_reduction_f64", chi_res)
             .add_data("chi_disjoint_reduction_exact", exact_res)
             .add_data("operator_decomposition_exact", op_res)
             .set_audit_only(
                 "docs/audits/2026-06-16-categorical-interface-operator-closure-b-design.md"))
        b.add_assertion(
            name="dimension_identity_holds",
            computed=dim_res["all_passed"], expected=True, tolerance=0,
            source="restriction d_λ = Σ c^λ_ξν d_ξ d_ν")
        b.add_assertion(
            name="chi_identity_reduction_f64",
            computed=chi_res["all_passed"], expected=True, tolerance=0,
            source="χ^λ(disjoint) = Σ c^λ_ξν χ^ξ χ^ν vs chi_lambda_fast_mp "
                   "(f64-limited ~1e-14)")
        if not exact_res.get("skipped"):
            b.add_assertion(
                name="chi_identity_reduction_exact_1e-25",
                computed=exact_res["all_passed"], expected=True, tolerance=0,
                source="χ^λ(disjoint) = Σ c^λ_ξν χ^ξ χ^ν via pyhecke_native "
                       "MPFR seminormal characters at 50 dps (tol 1e-25)")
        if not op_res.get("skipped"):
            b.add_assertion(
                name="operator_interface_decomposition_exact_1e-25",
                computed=op_res["all_passed"], expected=True, tolerance=0,
                source="χ^λ(W·I_pn·β) = Σ_ξν Tr[ρ_λ(W)·Π_ξν ρ_λ(I) Π_ξν·ρ_λ(β)] "
                       "via exact MPFR seminormal matrices + class-sum projectors "
                       "(tol 1e-25) — proves A^λ_ξν(I)=Π_ξν ρ_λ(I) Π_ξν")
        out = b.save()
        print(f"  Witness: {out.name}")

    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
