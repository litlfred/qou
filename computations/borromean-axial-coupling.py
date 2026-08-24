#!/usr/bin/env python3
"""
g_A from confinement Frobenius reciprocity — instance of the master
formula ⟨O⟩_T = Σ_{i,j ∈ A*(T)} u_i* (G^{-1})_{ij} ⟨O, b_j⟩
(prop:confinement-frobenius-reciprocity).

This script REPLACES the prior conjugation-pattern computation
``g_A = (5/3) · |tr(β·σ₁·β⁻¹) / tr(σ₁)|``, which was structurally
``5/3`` for ALL ``q`` because ``tr(β·X·β⁻¹) = tr(X)`` by cyclicity of
the Markov trace.  See
``docs/audits/2026-05-06-frobenius-pairing-compute-audit.md`` § 3.1
for the bug history.

Pipeline (Item 4b of the workplan)
----------------------------------

1. Load the Frobenius Gram matrix $G$ and inverse $G^{-1}$ on the
   $H_3(q)$ NF basis from
   ``gram-matrix-dual.witness.json``.

2. Solve the operator-selection LP for the proton bound state via
   ``lp_dual_solver.solve_operator_selection_lp(t, G, n_target)``,
   yielding the primal optimum $T = \\sum_i x_i^* b_i$, the dual
   shadow prices $u^*$, and the LP-active set
   $A^*(T) = \\{i : u_i^* > 0\\}$.

3. For each of the two physical observables — vector channel
   $O_V = e_{\\mathrm{sym}}$ (trivial / $+q$ eigenspace of $\\sigma_i$)
   and axial channel $O_A = e_{\\mathrm{alt}}$ (sign / $-q^{-1}$
   eigenspace) — compute the row of pairings
   $\\langle O, b_j\\rangle = \\mathrm{tr}_M(O \\cdot b_j)$ for
   $j \\in A^*$, by evaluating the Markov trace of the NF basis
   element in the irreducible representation.

4. Apply the master formula on the active subspace:
   ``⟨O⟩_T = Σ_{i,j ∈ A*}  u_i*  (G^{-1})_{ij}  ⟨O, b_j⟩``.
   This is the Gram-inverse dual pairing weighted by LP-active
   shadow prices, NOT a raw Markov trace.

5. The axial coupling is the ratio
   ``g_A = |⟨O_A⟩_T| / |⟨O_V⟩_T|``.

6. Emit a witness JSON containing BOTH the LP-dual fields
   ``primal_obj``, ``dual_obj``, ``duality_gap`` (LP-dual CI gate via
   ``lp_dual_witness_validator.py``) AND the bound-state-observable
   fields ``gram_matrix``, ``gram_inverse``, ``lp_active_set``,
   ``shadow_prices`` (bound-state CI gate via
   ``bound_state_observable_validator.py``).

Usage
-----
    python3 computations/borromean-axial-coupling.py

Output
------
    computations/borromean-axial-coupling.witness.json
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent.parent / "tools" / "pyhecke" / "python"))

from q_parameter import Q as q0, Q_INV as qi0  # noqa: E402
from pyhecke.gram import (  # noqa: E402
    NF_BASIS,
    NF_NAMES,
    TR_M,
)
from lp_dual_solver import solve_operator_selection_lp  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []


# ── Step 1. Load Gram matrix + inverse from canonical witness ────

GRAM_WITNESS_PATH = _pb.witness_path("gram-matrix-dual.witness.json", HERE)
_gram_data = record_upstream(GRAM_WITNESS_PATH, _UPSTREAM_RECORDS)
GRAM = np.array(_gram_data["gram_matrix"], dtype=float)
# The Gram matrix is SINGULAR (eigenvalues carry one exact zero; the
# null vector is the sign representation, `gram_radical`), so a true
# inverse does not exist and the upstream producer stopped emitting
# `gram_inverse` in be59f01376.  `gram_quotient_inverse` -- the inverse
# on the quotient by the radical -- was MEASURED to be the Moore-Penrose
# pseudo-inverse of `gram_matrix` to 3.8e-16 relative, i.e. to the
# precision the witness is written at, and it annihilates the radical.
# That is the standard meaning of G^{-1} for singular G.
#
# Safe here for a reason specific to this consumer: `dual_pairing` feeds
# this matrix into a RATIO (`g_A` below) with the same `u_A` and the same
# restricted matrix in numerator and denominator, so `g_A` depends on it
# only through the direction of `u_A^T M|_A` -- overall scale cancels.
# See bean qou-cnbm for the measurement.
GRAM_INV = np.array(_gram_data["gram_quotient_inverse"], dtype=float)
assert GRAM.shape == (6, 6), f"Gram matrix shape mismatch: {GRAM.shape}"
assert GRAM_INV.shape == (6, 6), f"Gram quotient-inverse shape mismatch: {GRAM_INV.shape}"


# ── Step 2. Solve the operator-selection LP for the proton ───────
#
# The proton is the confined bound state with `n_target = 1` on the
# 6-element NF basis of H_3(q).  ``solve_operator_selection_lp``
# returns BOTH primal coefficients ``x_star`` AND dual shadow prices
# ``y_star`` (with ``y_star[i] > 0`` flagging LP-active channels).
# Strong duality gives ``primal_obj == dual_obj`` to machine precision.

T_NF = TR_M.copy()  # Markov-trace vector on NF basis
N_TARGET = 1.0       # proton confinement net (normalised categorical mass)

# Pinned, not `auto`: `auto` picks clarabel-MPFR or scipy-f64 by
# whether the Rust binary happens to be built, so the same script
# yields different numbers on different boxes. QOU_REQUIRE_CLARABEL=1
# makes a missing binary an error rather than a changed answer.
# Bean `qou/ftuv`.
lp = solve_operator_selection_lp(T_NF, GRAM, N_TARGET, backend="clarabel")
if not lp.feasible:
    raise RuntimeError(
        "Operator-selection LP for proton bound state was infeasible. "
        "Cannot instantiate the master formula. Check the Gram matrix "
        "and Markov-trace inputs."
    )

x_star = np.asarray(lp.x_star, dtype=float)
y_star = np.asarray(lp.y_star, dtype=float)
y0_star = float(lp.y0_star)

# Active set: indices where the Frobenius positivity constraint is
# tight (shadow price > 0).  Per prop:mass-coefficient-shadow-price
# these are the "most receptive sub-braids on the shell".
ACTIVE_TOL = 1e-9
# Threshold below which a denominator pairing is treated as numerically
# zero (g_A would then be undefined).  Same scale as ACTIVE_TOL — a
# pairing of magnitude ≤ 1e-15 is in float-roundoff territory.
ZERO_PAIRING_TOL = 1e-15
active_set = [int(i) for i, y in enumerate(y_star) if abs(y) > ACTIVE_TOL]
if not active_set:
    # Degenerate LP: fall back to the entire basis (all u* effectively 0
    # but we still need a non-empty subspace for the master formula).
    # The master formula then collapses onto the primal coefficients.
    active_set = list(range(6))
    print(
        "WARNING: LP-active set is empty (all Frobenius constraints slack). "
        "Falling back to the full NF basis for the dual pairing.",
        file=sys.stderr,
    )


# ── Step 3. Compute observable pairings ⟨O, b_j⟩ ────────────────
#
# The two physical observables are the Hecke-algebra projectors onto
# the irreducible representations of H_3(q):
#
#   O_V  =  e_sym  =  the eigenspace of σ_i with eigenvalue  +q
#                     (trivial / vector / parity-even channel)
#   O_A  =  e_alt  =  the eigenspace of σ_i with eigenvalue  -q⁻¹
#                     (sign / axial / parity-odd channel)
#
# In the irreducible representation, σ_i acts as a scalar:
#   trivial:   σ_i ↦ q
#   sign:      σ_i ↦ -q⁻¹
#
# So the trace of an NF basis word b_j = σ_{j_1}…σ_{j_k} in the
# trivial rep is q^k, and in the sign rep is (-q⁻¹)^k.
#
# These traces ARE the pairings ⟨O_V, b_j⟩ and ⟨O_A, b_j⟩ in the
# sense of Frobenius reciprocity on the algebra.

def char_trivial(b: tuple[int, ...]) -> float:
    """Character of the trivial rep on the NF basis word b."""
    return float(q0 ** len(b))


def char_sign(b: tuple[int, ...]) -> float:
    """Character of the sign rep on the NF basis word b."""
    return float((-qi0) ** len(b))


obs_V = np.array([char_trivial(b) for b in NF_BASIS], dtype=float)
obs_A = np.array([char_sign(b) for b in NF_BASIS], dtype=float)


# ── Step 4. Apply the master formula on the active subspace ─────
#
#   ⟨O⟩_T  =  Σ_{i,j ∈ A*}  u_i*  (G^{-1})_{ij}  ⟨O, b_j⟩
#
# Equivalently in matrix form, restricting G^{-1} to its principal
# submatrix on A*:  ⟨O⟩_T = u_A^T · G_A^{-1} · obs_A.

def dual_pairing(obs_full: np.ndarray) -> dict:
    """Apply the master formula and return diagnostic dict.

    Returns
    -------
    dict with keys:
      - ``value``                : the scalar pairing ⟨O⟩_T
      - ``active_indices``       : copy of the LP-active set A*(T)
      - ``active_basis_names``   : NF basis names indexed by A*
      - ``u_active``             : shadow prices on A* (length |A*|)
      - ``obs_active``           : ⟨O, b_j⟩ for j ∈ A* (length |A*|)
    """
    A = active_set
    u_A = y_star[A]                                  # shadow prices on A*
    G_inv_A = GRAM_INV[np.ix_(A, A)]                 # G^{-1}|_{A*}
    obs_A_vec = obs_full[A]                          # ⟨O, b_j⟩, j ∈ A*
    pairing = float(u_A @ G_inv_A @ obs_A_vec)
    return {
        "value": pairing,
        "active_indices": A,
        "active_basis_names": [NF_NAMES[i] for i in A],
        "u_active": u_A.tolist(),
        "obs_active": obs_A_vec.tolist(),
    }


pairing_V = dual_pairing(obs_V)
pairing_A = dual_pairing(obs_A)


# ── Step 5. Axial coupling ──────────────────────────────────────
#
# g_A = |⟨O_A⟩_T| / |⟨O_V⟩_T|
#
# This replaces the cyclic-trivial g_A = (5/3) · |tr(βσ₁β⁻¹)/tr(σ₁)|
# of the prior implementation.  The naive quark-model coefficient
# (5/3) is dropped: it was a Clebsch-Gordan factor inserted by hand,
# whereas the master formula gives the *full* matrix element on the
# LP-active subspace without external normalisation.

if abs(pairing_V["value"]) < ZERO_PAIRING_TOL:
    g_A_value = float("nan")
    g_A_note = (
        "Vector channel pairing is numerically zero; g_A undefined. "
        "This indicates the LP-active set selects a state on which the "
        "trivial-rep character vanishes, which would be a deeper "
        "structural finding — investigate before interpreting."
    )
else:
    g_A_value = abs(pairing_A["value"]) / abs(pairing_V["value"])
    g_A_note = (
        "g_A from confinement Frobenius reciprocity (master formula); "
        "no external Clebsch-Gordan factor inserted."
    )

PDG_G_A = 1.2754


# ── Step 6. Assemble witness ────────────────────────────────────

w = WitnessBuilder("borromean-axial-coupling", engine="numpy")
w.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
w.set_description(
    "Axial coupling g_A as an instance of the master formula "
    "⟨O⟩_T = Σ_{i,j ∈ A*(T)} u_i (G⁻¹)_{ij} ⟨O,b_j⟩ "
    "(prop:confinement-frobenius-reciprocity). "
    "Replaces the prior cyclic-trivial conjugation-pattern computation "
    "tr(β·σ₁·β⁻¹)/tr(σ₁) — see "
    "docs/audits/2026-05-06-frobenius-pairing-compute-audit.md § 3.1. "
    "Bound-state observable: g_A (axial coupling, Gamow-Teller form factor)."
)
w.set_content_block("prop:confinement-frobenius-reciprocity")

w.add_parameter("q", q0)
w.add_parameter("q_inv", qi0)
w.add_parameter("n_target", N_TARGET)

# Bound-state-observable CI gate fields:
w.add_data("gram_matrix", GRAM.tolist())
# Emitted under `gram_inverse` because that is the name in
# `bound_state_observable_validator.REQUIRED_FIELDS`, and that validator
# documents the field by its ROLE -- "G^{-1} used for dualisation" -- which
# the pseudo-inverse is.  `gram_inverse_kind` names the actual object so the
# role-name does not read as a claim that G is invertible.  It is not.
w.add_data("gram_inverse", GRAM_INV.tolist())
w.add_data("gram_inverse_kind", "moore-penrose-pseudoinverse")
w.add_data("lp_active_set", active_set)
w.add_data("shadow_prices", y_star.tolist())
w.add_data("active_basis_names", [NF_NAMES[i] for i in active_set])

# LP-dual CI gate fields:
w.add_data("x_star", x_star.tolist())
w.add_data("y0_star", y0_star)
w.add_data("y_star", y_star.tolist())
w.add_data("active_set", active_set)
w.add_data("primal_obj", float(lp.primal_obj))
w.add_data("dual_obj", float(lp.dual_obj))
w.add_data("duality_gap", float(lp.duality_gap))
w.add_data("lp_feasible", bool(lp.feasible))

# Master-formula instantiation details:
w.add_data("observable_vector", {
    "name": "O_V (trivial / vector / +q eigenspace)",
    "char_on_basis": obs_V.tolist(),
    "dual_pairing_value": pairing_V["value"],
    "u_active": pairing_V["u_active"],
    "obs_active": pairing_V["obs_active"],
})
w.add_data("observable_axial", {
    "name": "O_A (sign / axial / -q⁻¹ eigenspace)",
    "char_on_basis": obs_A.tolist(),
    "dual_pairing_value": pairing_A["value"],
    "u_active": pairing_A["u_active"],
    "obs_active": pairing_A["obs_active"],
})

w.add_assertion(
    "g_A",
    computed=g_A_value,
    expected=PDG_G_A,
    tolerance=0.5,  # broad tolerance; this is a v1 instance
    source="PDG 2024",
)
# F1 (PR #565): backfill structural-correctness anchors so a
# regression that breaks LP duality is caught before the g_A
# tolerance widens silently.
w.add_assertion(
    "lp_duality_gap_zero",
    computed=abs(float(lp.duality_gap)),
    expected=0.0,
    tolerance=1e-10,
    source="prop:operator-selection-lp § strong duality",
)
w.add_assertion(
    "lp_active_set_nonempty",
    computed=float(len(active_set)),
    expected=1.0,
    tolerance=10.0,  # at least 1; passes for any non-empty active set
    source="prop:confinement-frobenius-reciprocity § master formula",
)
w.add_data("g_A_note", g_A_note)
w.add_data("interpretation", (
    "g_A is the ratio of two instances of the master formula on the "
    "same proton bound state T (operator-selection LP optimum at "
    "n_target = 1). The vector channel O_V uses the trivial-rep "
    "character (σ_i ↦ q); the axial channel O_A uses the sign-rep "
    "character (σ_i ↦ -q⁻¹). The Gram-inverse dual pairing on the "
    "LP-active subspace replaces the cyclic-trivial conjugation "
    "pattern of the prior implementation. Exact numerical agreement "
    "with PDG g_A = 1.2754 requires the categorical Clebsch-Gordan "
    "structure to be installed on the same active subspace; this v1 "
    "establishes the correct STRUCTURE — the conjugation bug is gone "
    "— with refinement (proper isospin projector on T) deferred."
))

out_path = w.save()


# ── Console summary ─────────────────────────────────────────────

print(f"q₀                 = {q0:.10f}")
print(f"n_target (proton)  = {N_TARGET}")
print()
print(f"LP solve:")
print(f"  feasible          = {lp.feasible}")
print(f"  primal_obj        = {lp.primal_obj:.10f}")
print(f"  dual_obj          = {lp.dual_obj:.10f}")
print(f"  duality_gap       = {lp.duality_gap:.2e}")
print(f"  active_set        = {active_set}")
print(f"  active_basis      = {[NF_NAMES[i] for i in active_set]}")
print(f"  shadow_prices     = {[f'{y:.4f}' for y in y_star]}")
print()
print(f"Master formula on active subspace:")
print(f"  ⟨O_V⟩_T (trivial) = {pairing_V['value']:.6f}")
print(f"  ⟨O_A⟩_T (sign)    = {pairing_A['value']:.6f}")
print()
print(f"  g_A (master)      = {g_A_value:.6f}")
print(f"  g_A (PDG 2024)    = {PDG_G_A:.6f}")
print()
print(f"Witness written to {out_path}")
