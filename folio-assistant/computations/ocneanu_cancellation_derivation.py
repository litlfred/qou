#!/usr/bin/env python3
"""
ocneanu_cancellation_derivation.py — symbolic-q Ocneanu-weight tracking
through SYT paths to derive the cancellation count first-principles.

For each atom (Z, N) in canonical pppnnn ordering:
  1. Compute χ^λ(β) symbolically in q for each partition λ ⊢ n = 3A
  2. Find the lowest q-power (= pole order) of each χ^λ
  3. Compute tr_M(β) = Σ_λ w_λ · χ^λ(β) / f^λ symbolically
  4. Find the pole of tr_M (cross-partition cancellation)
  5. Compare to DP_max and decompose the cancellation count

Tractable for n ≤ 6 (proton, neutron, deuteron). Higher atoms have
combinatorially large SYT spaces — degrade gracefully.

Output: ocneanu-cancellation-derivation.witness.json
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from hecke_characters import (  # noqa: E402
    partitions_of, build_seminormal_matrices, qfac, dim_q,
    standard_young_tableaux,
)
from canonical_braid_crossings import atom_canonical_crossings as atomic_braid_to_crossings  # noqa: E402

# ──────────────────────────────────────────────────────────────────────
# Symbolic-q Hoefsmit seminormal representation
# ──────────────────────────────────────────────────────────────────────

q = sp.symbols('q', positive=True)
H_SKEIN = q - 1/q  # h = q - q^-1


def hoefsmit_sigma_symbolic(shape: tuple[int, ...]):
    """Build seminormal representation matrices for σ_1, ..., σ_{n-1}
    on V_λ for shape = λ, with entries in sympy.Rational[q, q^-1].

    Uses the recursive Hoefsmit construction.
    """
    syts, cells, contents = standard_young_tableaux(list(shape))
    dim = len(syts)
    n = sum(shape)

    matrices = []
    for k_gen in range(n - 1):
        # σ_{k_gen+1} acts on the SYT basis
        M = sp.zeros(dim, dim)
        for i, syt in enumerate(syts):
            n_lower = k_gen + 1
            n_upper = k_gen + 2
            cell_lower = syt[n_lower]
            cell_upper = syt[n_upper]
            rho_diff = contents[cell_upper] - contents[cell_lower]

            if rho_diff == 1:
                # 1x1 block, eigenvalue q (row swap, no SYT change)
                M[i, i] = q
            elif rho_diff == -1:
                # 1x1 block, eigenvalue -q^-1 (col swap)
                M[i, i] = -1/q
            else:
                # 2x2 block: find swap partner
                swap_map = dict(syt)
                swap_map[n_lower] = cell_upper
                swap_map[n_upper] = cell_lower
                j = None
                for jj, syt_j in enumerate(syts):
                    if syt_j == swap_map:
                        j = jj
                        break
                if j is None:
                    raise ValueError(f"swap partner not found for SYT {i} at gen {k_gen}")

                # Hoefsmit: on the {i, j} basis (assume rho > 0 at i for canonical form)
                # σ matrix is [[1/[d], sqrt(([d]+1)([d]-1))/[d]], [..., -1/[d]]]
                # where [d] = (q^d - q^-d)/(q - q^-1) is the q-deformed axial dist
                d = abs(rho_diff)
                d_q = (q**d - q**(-d)) / (q - 1/q)

                # On {i, j} basis (i = ρ > 0, j = ρ < 0 partner)
                # diagonal entries: 1/[d] and -1/[d]
                M[i, i] = 1 / d_q
                M[j, j] = -1 / d_q
                # off-diagonal: sqrt(([d]+1)([d]-1))/[d]
                # Here ([d]+1)([d]-1) = [d]^2 - 1
                off = sp.sqrt(d_q**2 - 1) / d_q
                # In Hoefsmit convention with rho_diff = +d at i:
                if rho_diff > 0:
                    M[j, i] = off
                    M[i, j] = off
                else:
                    M[j, i] = off
                    M[i, j] = off
        matrices.append(M)
    return matrices, dim


def chi_symbolic(shape: tuple[int, ...], crossings: list) -> sp.Expr:
    """Compute χ^λ(β) symbolically in q for braid word β.

    crossings: list of (k_gen, ctype) where ctype ∈ {sigma, sigma_inv, averaged}.
    """
    sigmas, dim = hoefsmit_sigma_symbolic(shape)
    M = sp.eye(dim)
    for k_gen, ctype in crossings:
        sigma_i = sigmas[k_gen]
        if ctype == 'sigma':
            step = sigma_i
        elif ctype == 'sigma_inv':
            # σ_i^{-1} = σ_i - h
            step = sigma_i - H_SKEIN * sp.eye(dim)
        elif ctype == 'averaged':
            # (σ + σ^{-1})/2 = σ - h/2
            step = sigma_i - (H_SKEIN / 2) * sp.eye(dim)
        else:
            raise ValueError(f"unknown crossing type {ctype}")
        M = sigma_i_mul = step * M
    chi = sp.cancel(M.trace())
    return chi


def lowest_q_power(expr: sp.Expr) -> int:
    """Return the lowest power of q in expr (treating expr as Laurent).

    Computes via the order of `expr` at q=0 in the variable substitution
    expr_in_q = expr * q^N for large N (to make polynomial), then extract
    the lowest exponent.
    """
    if expr == 0:
        return None
    # Substitute q = sympy variable, find min power
    # Use Poly with negative powers via Laurent expansion
    expr = sp.cancel(expr)
    # Get numerator and denominator
    num, den = sp.fraction(expr)
    num_p = sp.Poly(sp.expand(num), q)
    den_p = sp.Poly(sp.expand(den), q)
    # Lowest power of q in num and den
    num_low = min(num_p.monoms(), key=lambda m: m[0])[0] if num_p.monoms() else 0
    den_low = min(den_p.monoms(), key=lambda m: m[0])[0] if den_p.monoms() else 0
    # Expr's lowest power = num_low - den_low
    # But for pole at q=0, we want the lowest exponent if negative
    return num_low - den_low


# ──────────────────────────────────────────────────────────────────────
# Witness scaffold
# ──────────────────────────────────────────────────────────────────────
from witness_base import WitnessBuilder  # noqa: E402

_witness = (
    WitnessBuilder("ocneanu-cancellation-derivation", engine="sympy")
    .set_description(
        "Round-1 SCAFFOLD: symbolic-q Hoefsmit attempt at first-"
        "principles derivation of the cancellation count via Σ_λ w_λ "
        "χ^λ(β) / f^λ. The 2×2-block Hoefsmit construction has known "
        "convention/sign issues (cross-validated against numerical: "
        "χ^(2,1)(proton) sym=2.515 vs num=1.808). High-precision "
        "numerical pole detection in "
        "docs/audits/2026-05-04-ocneanu-cancellation-numerical-verification.md "
        "is the canonical verification path until the symbolic 2×2 "
        "convention is repaired."
    )
    .set_content_block("conj:e-hartree-categorical-derivation")
    .add_caveat(
        "Symbolic 2×2 block has a documented convention bug: the "
        "computed χ^(2,1)(proton) at q_0 is 2.515 vs numerical 1.808. "
        "Treat the symbolic_cross_partition_cancel field as "
        "known-incorrect; the empirical_cross_partition_cancel = 1 "
        "from numerical verification is the correct value."
    )
)
# Compatibility: keep the dict-based WITNESS interface (used through
# the script body) and migrate to WitnessBuilder at save time.
WITNESS = {"data": {}, "assertions": []}

# ──────────────────────────────────────────────────────────────────────
# §1 — Proton standalone (n = 3)
# ──────────────────────────────────────────────────────────────────────
print("=" * 70)
print("§1  Proton standalone (n = 3, 11 generators)")
print("=" * 70)
print()

proton_crosses = atomic_braid_to_crossings(1, 0, include_inter=False)
print(f"  Braid: {len(proton_crosses)} generators")
print(f"  σ count: {sum(1 for _, t in proton_crosses if t == 'sigma')}")
print(f"  σ⁻¹ count: {sum(1 for _, t in proton_crosses if t == 'sigma_inv')}")
print(f"  averaged count: {sum(1 for _, t in proton_crosses if t == 'averaged')}")
print()

# For each partition λ ⊢ 3:
n = 3
partitions = list(partitions_of(n))
print(f"  Partitions of {n}: {partitions}")
print()

per_lambda_chi = {}
per_lambda_pole = {}
print(f"{'λ':<14} {'χ^λ(symbolic)':<60} {'pole':>6}")
print("-" * 80)

for shape in partitions:
    print(f"  Computing χ^λ for λ={shape}...", end=" ", flush=True)
    try:
        chi = chi_symbolic(tuple(shape), proton_crosses)
        per_lambda_chi[tuple(shape)] = chi
        pole = lowest_q_power(chi)
        per_lambda_pole[tuple(shape)] = pole
        chi_str = str(chi)[:55] + ("..." if len(str(chi)) > 55 else "")
        print(f"\r  {str(shape):<12} {chi_str:<60} {pole:>+6}")
    except Exception as e:
        print(f"FAILED: {e}")
        per_lambda_chi[tuple(shape)] = None
        per_lambda_pole[tuple(shape)] = None

print()
# Compute tr_M = Σ w_λ · χ^λ / f^λ symbolically
print("Computing tr_M = Σ_λ w_λ · χ^λ / f^λ ...")
trM = sp.Integer(0)
qfac_n = qfac(n)
for shape in partitions:
    chi = per_lambda_chi.get(tuple(shape))
    if chi is None:
        continue
    f_lam = len(standard_young_tableaux(list(shape)))
    d_q = dim_q(list(shape))
    w_lam_sym = d_q * d_q / qfac_n  # Wedderburn weight (already symbolic in q)
    contribution = sp.cancel(w_lam_sym * chi / f_lam)
    trM = trM + contribution

trM = sp.cancel(trM)
trM_pole = lowest_q_power(trM)
print(f"  tr_M(proton) symbolic pole = {trM_pole}")
DP_MAX_POLE = 11
EMPIRICAL_PROTON_POLE = 10
# lowest_q_power returns -k for a pole of order k (leading term q^{-k}).
# So the symbolic pole order = -trM_pole, and the cancellation from DP-max
# = DP_max_pole - (-trM_pole).  For empirical: DP_max - empirical.
sym_pole_order = -trM_pole if trM_pole is not None else None
sym_cancel = DP_MAX_POLE - sym_pole_order if sym_pole_order is not None else None
emp_cancel = DP_MAX_POLE - EMPIRICAL_PROTON_POLE
print(f"  Empirical proton pole       = {EMPIRICAL_PROTON_POLE} (DP-max {DP_MAX_POLE})")
print(f"  Symbolic pole order         = {sym_pole_order} (from trM_pole={trM_pole})")
print(f"  ⟹ Symbolic cancel = {sym_cancel}, Empirical cancel = {emp_cancel}")

WITNESS["data"]["proton_standalone"] = {
    "n": n,
    "partitions": [list(p) for p in partitions],
    "per_lambda_chi": {str(k): str(v) for k, v in per_lambda_chi.items()},
    "per_lambda_pole_at_q0": {str(k): v for k, v in per_lambda_pole.items()},
    "trM_pole_at_q0": trM_pole,
    "symbolic_pole_order": sym_pole_order,
    "empirical_proton_pole": EMPIRICAL_PROTON_POLE,
    "DP_max_pole": DP_MAX_POLE,
    # symbolic_cross_partition_cancel: 0 when symbolic bug makes pole=DP_max.
    # empirical_cross_partition_cancel: correct count from numerical detection.
    "symbolic_cross_partition_cancel": sym_cancel,
    "empirical_cross_partition_cancel": emp_cancel,
}

# ──────────────────────────────────────────────────────────────────────
# §2 — Save witness via WitnessBuilder + explicit failing assertion
# ──────────────────────────────────────────────────────────────────────
# The 2×2-block Hoefsmit construction has a documented convention bug:
# χ^(2,1)(proton) symbolic = 2.515 vs numerical = 1.808. Add an
# explicit FAILING assertion so the chain auditor sees this as
# verifying-FAIL rather than a silent "verified" witness.
SYMBOLIC_CHI_2_1_AT_Q0 = 2.5154623216489195
NUMERICAL_CHI_2_1_AT_Q0 = 1.807703

for key, value in WITNESS["data"].items():
    _witness.add_data(key, value)
_witness.add_assertion(
    name="symbolic χ^(2,1)(proton) matches numerical hecke_characters",
    computed=SYMBOLIC_CHI_2_1_AT_Q0,
    expected=NUMERICAL_CHI_2_1_AT_Q0,
    tolerance=1e-3,
    source="cross-validation against build_seminormal_matrices",
)
out_path = _witness.save()

print()
print("=" * 70)
print(f"Witness written: {out_path.name}")
print("=" * 70)
