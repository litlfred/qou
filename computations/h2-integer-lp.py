#!/usr/bin/env python3
"""
H₂ binding from integer LP: derive the covalent bond operator.

Same method as derive-crossing-budget.py (gluon derivation):
scan all crossing operators between two H atoms, find which
configuration gives the correct binding energy.

Instead of assuming pe = σ⁻¹ from a crossing table, we let
the LP select from {σ₀, σ₁, σ₀⁻¹, σ₁⁻¹, L₊, L₋, e⁻, id}
at each inter-atomic position.

Usage:
    cd computations
    python3 h2-integer-lp.py
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import math
import itertools
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, Q_INV as qi0, HA as h, q_int
from witness_base import WitnessBuilder
from mpmath import mp  # noqa: F401

z = q0**3 / (q0**2 + 1)

# Wedderburn weights for H₃(q) — from the gluon branch fix
# w_sym = w_alt = q²/(q⁴+4q²+1), w_std = (q²+1)²/(q⁴+4q²+1)
q2 = q0**2
denom = q2**2 + 4*q2 + 1
w_sym = q2 / denom
w_std = (q2 + 1)**2 / denom
w_alt = q2 / denom

TWO_Q = q0 + qi0
from hecke_core import alpha_em, E_HARTREE_EV as E_hartree_eV, E_MOL as E_mol

print("=" * 65)
print("H₂ INTEGER LP: DERIVE THE COVALENT BOND OPERATOR")
print("=" * 65)
print(f"q = {q0:.10f}, h = {h:.10f}, z = {z:.10f}")
print(f"Wedderburn: w_sym={w_sym:.4f}, w_std={w_std:.4f}, w_alt={w_alt:.4f}")
print(f"E_mol = E_hartree/[2]_q² = {E_mol:.4f} eV")
print()

# ══════════════════════════════════════════════════════════════
# §1. Hecke algebra H₃(q) multiplication
# ══════════════════════════════════════════════════════════════
# NF basis: [γ, σ₀, σ₁, L₊, L₋, e⁻]
# where L₊ = σ₀σ₁, L₋ = σ₁σ₀, e⁻ = σ₀σ₁σ₀ = σ₁σ₀σ₁

def hecke_mul(nf, c, d, gen):
    """Apply (c·σ_gen + d·I) to NF vector."""
    r = [0.0]*6
    if gen == 0:
        tables = [
            (0, [(1, c), (0, d)]),
            (1, [(1, c*h), (0, c), (1, d)]),
            (2, [(3, c), (2, d)]),
            (3, [(3, c*h), (2, c), (3, d)]),
            (4, [(5, c), (4, d)]),
            (5, [(5, c*h), (4, c), (5, d)]),
        ]
    else:
        tables = [
            (0, [(2, c), (0, d)]),
            (1, [(4, c), (1, d)]),
            (2, [(2, c*h), (0, c), (2, d)]),
            (3, [(5, c), (3, d)]),
            (4, [(4, c*h), (1, c), (4, d)]),
            (5, [(5, c*h), (3, c), (5, d)]),
        ]
    for src_idx, targets in tables:
        if abs(nf[src_idx]) < 1e-15:
            continue
        for tgt_idx, coeff in targets:
            r[tgt_idx] += nf[src_idx] * coeff
    return r


def nf_markov_trace(nf):
    """Markov trace of NF element: tr_M = γ·1 + σ₀·z + σ₁·z + L₊·z² + L₋·z² + e⁻·z³"""
    return nf[0] + nf[1]*z + nf[2]*z + nf[3]*z**2 + nf[4]*z**2 + nf[5]*z**3


# ══════════════════════════════════════════════════════════════
# §2. Build isolated H atom
# ══════════════════════════════════════════════════════════════
# H = proton (B₃ confined) + 1 electron (trefoil T₂,₃)
# Proton: B₃ = (σ₀σ₁⁻¹)³ in H₃(q) with 3 quark crossings → 9 crossings
# + 2 gluon crossings (from integer LP) → 11 crossings total

# B₃ confinement
nf_B3 = [1.0, 0, 0, 0, 0, 0]
for _ in range(3):
    nf_B3 = hecke_mul(nf_B3, 1, 0, 0)     # σ₀
    nf_B3 = hecke_mul(nf_B3, 1, -h, 1)    # σ₁⁻¹

# Quark Garside for proton (uud): σ₀(uu) σ₁(ud) σ₀(ud)
nf_proton_9 = nf_B3[:]
nf_proton_9 = hecke_mul(nf_proton_9, 1, 0, 0)      # uu → σ₀
nf_proton_9 = hecke_mul(nf_proton_9, 1, -h/2, 1)    # ud → mixed
nf_proton_9 = hecke_mul(nf_proton_9, 1, -h/2, 0)    # ud → mixed

# 2 gluon crossings (σ₀, σ₀)
nf_proton = nf_proton_9[:]
nf_proton = hecke_mul(nf_proton, 1, 0, 0)  # gluon 1
nf_proton = hecke_mul(nf_proton, 1, 0, 0)  # gluon 2

tr_proton = nf_markov_trace(nf_proton)

print("§1. Isolated H atom (proton with 11 crossings)")
print(f"  NF(proton) = [{', '.join(f'{v:+.6f}' for v in nf_proton)}]")
print(f"  tr_M(proton) = {tr_proton:.10f}")
print(f"  |tr_M| = {abs(tr_proton):.10f}")
print()

# Electron trefoil: T₂,₃ = σ₀³ on 2 strands (but lives in H₃ as σ₀³)
nf_electron = [1.0, 0, 0, 0, 0, 0]
nf_electron = hecke_mul(nf_electron, 1, 0, 0)
nf_electron = hecke_mul(nf_electron, 1, 0, 0)
nf_electron = hecke_mul(nf_electron, 1, 0, 0)
tr_electron = nf_markov_trace(nf_electron)

print("§2. Electron trefoil T₂,₃ = σ₀³")
print(f"  NF(e⁻) = [{', '.join(f'{v:+.6f}' for v in nf_electron)}]")
print(f"  tr_M(e⁻) = {tr_electron:.10f}")
print()

# H atom = proton × electron (Hopf link)
# The pe crossing dresses the electron onto the proton
nf_H = nf_proton[:]
# electron Hopf-linked via σ₁⁻¹ (pe attraction)
nf_H = hecke_mul(nf_H, 1, -h, 1)  # pe crossing
tr_H = nf_markov_trace(nf_H)
Phi_H = mp.log(abs(tr_H)) if abs(tr_H) > 1e-300 else float('inf')

print("§3. H atom = proton × pe crossing")
print(f"  NF(H) = [{', '.join(f'{v:+.6f}' for v in nf_H)}]")
print(f"  tr_M(H) = {tr_H:.10f}")
print(f"  Φ₁(H) = ln|tr_M| = {float(Phi_H):.10f}")
Phi_2H = 2 * Phi_H
print(f"  Φ₁(2H separated) = {float(Phi_2H):.10f}")
print()

# ══════════════════════════════════════════════════════════════
# §3. Integer LP: scan inter-atomic operators
# ══════════════════════════════════════════════════════════════
# Two H atoms: H₁ and H₂. The molecular braid is:
#   M(H₂) = H₁ × [inter-atomic operator] × H₂
#
# The inter-atomic operator is a product of Hecke generators
# acting between the two atoms.  We scan:
#   σ₀, σ₁, σ₀⁻¹, σ₁⁻¹
# and combinations thereof (up to 4 crossings).

# Operators: (name, gen, c, d)
OPS = [
    ("σ₀",   0, 1.0, 0.0),
    ("σ₁",   1, 1.0, 0.0),
    ("σ₀⁻¹", 0, 1.0, -h),
    ("σ₁⁻¹", 1, 1.0, -h),
]

print("=" * 65)
print("§4. INTEGER LP: SCAN INTER-ATOMIC OPERATORS (1-4 crossings)")
print("=" * 65)
print()

def compute_H2_binding(ops_sequence):
    """Compute H₂ molecular Markov trace with given inter-atomic operators.

    The molecular NF is: H₁_NF × inter_ops × H₂_NF
    But since both H atoms live in H₃(q), the inter-atomic operator
    acts between them.

    Simplification: the molecular Markov trace is
      tr_M(H₁ · O_inter · H₂) where H₁, H₂ are the H atom NFs
      and O_inter is the inter-atomic operator.

    For the Markov trace: tr_M(A·B) = Σ_{i,j} a_i b_j tr_M(b_i · b_j)
    where b_i are NF basis elements.

    But this requires the full multiplication table. Instead, compute:
      nf_mol = nf_H * O_inter * nf_H  (full Hecke product)
    """
    nf_mol = nf_H[:]  # start with first H atom

    # Apply inter-atomic operators
    for name, gen, c, d in ops_sequence:
        nf_mol = hecke_mul(nf_mol, c, d, gen)

    # Now multiply by second H atom's contribution
    # The second H atom contributes the same crossings as the first.
    # But since we're in the SAME H₃(q), the second atom's crossings
    # are additional multiplications.
    #
    # Actually: the molecular braid is the PRODUCT of all crossings.
    # H₁ crossings, then inter-atomic crossings, then H₂ crossings.
    # H₂ has the same structure as H₁ (11 proton crossings + 1 pe).

    # Proton 2: B₃ + quarks + gluon
    for _ in range(3):
        nf_mol = hecke_mul(nf_mol, 1, 0, 0)
        nf_mol = hecke_mul(nf_mol, 1, -h, 1)
    nf_mol = hecke_mul(nf_mol, 1, 0, 0)      # uu
    nf_mol = hecke_mul(nf_mol, 1, -h/2, 1)   # ud
    nf_mol = hecke_mul(nf_mol, 1, -h/2, 0)   # ud
    nf_mol = hecke_mul(nf_mol, 1, 0, 0)      # gluon 1
    nf_mol = hecke_mul(nf_mol, 1, 0, 0)      # gluon 2
    nf_mol = hecke_mul(nf_mol, 1, -h, 1)     # pe crossing

    tr_mol = nf_markov_trace(nf_mol)
    if abs(tr_mol) < 1e-300:
        return float('inf'), 0.0, nf_mol

    Phi_mol = mp.log(abs(tr_mol))
    binding = Phi_2H - Phi_mol
    return Phi_mol, binding, nf_mol


# ── Single crossing ────────────────────────────────────────────
print("--- 1 inter-atomic crossing ---")
print(f"  {'Op':>8} {'tr_M(H₂)':>14} {'Φ₁(H₂)':>12} {'binding':>10} {'E(eV)':>10}")
print("  " + "-" * 60)

results_1 = []
for name, gen, c, d in OPS:
    Phi, bind, nf = compute_H2_binding([(name, gen, c, d)])
    E = bind * E_mol
    marker = " ←" if bind > 0 else ""
    print(f"  {name:>8} {nf_markov_trace(nf):>14.8f} {float(Phi):>12.6f} {float(bind):>10.6f} {float(E):>10.4f}{marker}")
    results_1.append((name, Phi, bind, E))

# ── Two crossings ─────────────────────────────────────────────
print()
print("--- 2 inter-atomic crossings ---")
print(f"  {'Op1+Op2':>16} {'Φ₁(H₂)':>12} {'binding':>10} {'E(eV)':>10}")
print("  " + "-" * 55)

results_2 = []
for (n1, g1, c1, d1), (n2, g2, c2, d2) in itertools.product(OPS, repeat=2):
    Phi, bind, nf = compute_H2_binding([(n1, g1, c1, d1), (n2, g2, c2, d2)])
    E = bind * E_mol
    label = f"{n1},{n2}"
    results_2.append((label, Phi, bind, E))

results_2.sort(key=lambda r: -r[2])  # sort by binding descending
for label, Phi, bind, E in results_2[:10]:  # top 10
    marker = " ← BEST" if bind == results_2[0][2] else ""
    print(f"  {label:>16} {float(Phi):>12.6f} {float(bind):>10.6f} {float(E):>10.4f}{marker}")
print(f"  ... ({len(results_2)} total combinations)")

# ── Three crossings ────────────────────────────────────────────
print()
print("--- 3 inter-atomic crossings ---")

results_3 = []
for ops in itertools.product(OPS, repeat=3):
    labels = [o[0] for o in ops]
    Phi, bind, nf = compute_H2_binding(list(ops))
    E = bind * E_mol
    results_3.append((",".join(labels), Phi, bind, E))

results_3.sort(key=lambda r: -r[2])
print(f"  {'Ops':>24} {'Φ₁(H₂)':>12} {'binding':>10} {'E(eV)':>10}")
print("  " + "-" * 60)
for label, Phi, bind, E in results_3[:10]:
    print(f"  {label:>24} {float(Phi):>12.6f} {float(bind):>10.6f} {float(E):>10.4f}")
print(f"  ... ({len(results_3)} total)")

# ── Four crossings ─────────────────────────────────────────────
print()
print("--- 4 inter-atomic crossings ---")

results_4 = []
for ops in itertools.product(OPS, repeat=4):
    labels = [o[0] for o in ops]
    Phi, bind, nf = compute_H2_binding(list(ops))
    E = bind * E_mol
    results_4.append((",".join(labels), Phi, bind, E))

results_4.sort(key=lambda r: -r[2])
print(f"  {'Ops':>32} {'Φ₁(H₂)':>12} {'binding':>10} {'E(eV)':>10}")
print("  " + "-" * 68)
for label, Phi, bind, E in results_4[:10]:
    print(f"  {label:>32} {float(Phi):>12.6f} {float(bind):>10.6f} {float(E):>10.4f}")
print(f"  ... ({len(results_4)} total)")

# ══════════════════════════════════════════════════════════════
# §5. Summary: best binding at each crossing count
# ══════════════════════════════════════════════════════════════
print()
print("=" * 65)
print("SUMMARY: BEST BINDING AT EACH CROSSING COUNT")
print("=" * 65)
print()
print(f"  {'n':>3} {'Best operator':>32} {'binding':>10} {'E(eV)':>10} {'vs obs':>8}")
print("  " + "-" * 68)

best_1 = max(results_1, key=lambda r: r[2])
best_2 = max(results_2, key=lambda r: r[2])
best_3 = max(results_3, key=lambda r: r[2])
best_4 = max(results_4, key=lambda r: r[2])

obs = 4.478
for n, best in [(1, best_1), (2, best_2), (3, best_3), (4, best_4)]:
    label, Phi, bind, E = best
    ratio = E / obs if obs > 0 else 0
    print(f"  {n:>3} {label:>32} {float(bind):>10.6f} {float(E):>10.4f} {float(ratio):>7.3f}x")

print()
print(f"  Observed D₀(H₂) = {obs} eV")
print()

# ══════════════════════════════════════════════════════════════
# §6. LP DUAL over strand orderings (prop:h2-lp-dual-binding .md)
# ══════════════════════════════════════════════════════════════
# The block's .md defines the ordering LP:
#   primal:  min_π Φ₁(T_{π0π1}·T_{π1π2}·T_{π2π3})  over orderings π of
#            [p₁, e₁, p₂, e₂], s.t. each strand appears once and the
#            shared electron is Hopf-linked to BOTH protons.
#   dual:    max y_cov  s.t.  y_cov ≤ Φ₁^sep − Φ₁^{H₂}(π)  over the
#            competing orderings;  y_cov* = binding per shared electron.
#
# Per-crossing traced volumes (md "Numerical evaluation"):
#   covalent inter-atomic p–e crossing: eigenvalues (q, −q⁻¹) = σ,
#     traced volume V̂ = z·1 + 0 = z
#   dressed intra-atomic pᵢ–eᵢ crossing: eigenvalues (q⁵, −q⁻⁵) = σ⁵
#     σ⁵ = a₅σ + b₅ with a₅ = (q⁵+q⁻⁵)/(q+q⁻¹), b₅ = q⁵ − a₅q,
#     traced volume V̂ = z·a₅ + b₅
# Feasibility: an ordering is feasible iff strand types alternate
# (p–p / e–e adjacencies have no transfer matrix in the .md, and a
# non-alternating ordering leaves no electron adjacent to both
# protons — the covalent constraint fails).
#
# Routing note: the ordering-min IS expressible in the canonical
# solve_operator_selection_lp(t, G, n_target) form (lp_dual_solver):
# put one occupancy variable x_π per feasible ordering, t_π = Φ₁(π),
# G = I (occupancies ≥ 0 as the "Frobenius positivity" rows) and
# n_target = 1 (exactly one ground state). Then y0* = Φ₁(π*) and the
# y* are the per-ordering reduced costs Φ₁(π) − Φ₁(π*) ≥ 0 — exactly
# the slacks of the .md's dual constraints. The .md-normalised dual
# value is the constant shift  y_cov* = Φ₁^sep − y0*.  (The .md's
# "max over π" is a trivial LP; we still route through the canonical
# entry point per AGENTS.md §LP/SDP duals, and cross-check against
# the direct enumeration.)
import numpy as np
from lp_dual_solver import solve_operator_selection_lp

print()
print("=" * 65)
print("§6. LP DUAL OVER STRAND ORDERINGS (prop:h2-lp-dual-binding)")
print("=" * 65)

a5 = (q0**5 + qi0**5) / (q0 + qi0)
b5 = q0**5 - a5 * q0
V_cov = z                    # tr_M(σ) — covalent inter-atomic crossing
V_dressed = z * a5 + b5      # tr_M(σ⁵) — dressed intra-atomic crossing

# Separated reference, .md literal formula:
#   V^H = −q⁵(q − q⁻¹) + q⁻⁵   (dressed isolated atom)
V_H_md = -(q0**5) * (q0 - qi0) + qi0**5
Phi_H_md = float(mp.log(abs(V_H_md)))
Phi_sep_md = 2 * Phi_H_md
# Markov-consistent alternative: trace the isolated dressed crossing
# with the SAME normalisation as the molecular V̂ᵢ (tr_M(σ⁵)). The .md
# mixes the two conventions; we emit both so the discrepancy is visible.
Phi_sep_markov = 2 * float(mp.log(abs(V_dressed)))

strands = [("p", 1), ("e", 1), ("p", 2), ("e", 2)]

def ordering_phi(perm):
    """Φ₁(π) = Σᵢ ln|V̂ᵢ| over the 3 adjacent transfer matrices,
    or None if the ordering is infeasible (p–p / e–e adjacency)."""
    phi = 0.0
    for (t1, i1), (t2, i2) in zip(perm, perm[1:]):
        if t1 == t2:
            return None  # no p–p / e–e transfer matrix; covalent constraint fails
        phi += float(mp.log(abs(V_dressed if i1 == i2 else V_cov)))
    return phi

orderings = []   # (name, Φ₁(π))
for perm in itertools.permutations(strands):
    phi = ordering_phi(perm)
    if phi is not None:
        name = ",".join(f"{t}{i}" for t, i in perm)
        orderings.append((name, phi))

names = [name for name, _ in orderings]
phis = [phi for _, phi in orderings]
n_ord = len(orderings)

# Canonical LP route (occupancy simplex; see routing note above).
t_vec = np.array(phis, dtype=float)
# Pinned, not `auto`: `auto` picks clarabel-MPFR or scipy-f64 by
# whether the Rust binary happens to be built, so the same script
# yields different numbers on different boxes. QOU_REQUIRE_CLARABEL=1
# makes a missing binary an error rather than a changed answer.
# Bean `qou/ftuv`.
lp = solve_operator_selection_lp(t_vec, np.eye(n_ord), 1.0, backend="clarabel")
assert lp.feasible, "ordering-selection LP infeasible (should never happen)"

DUAL_TOL = 1e-9
y_cov_dual = Phi_sep_md - lp.dual_obj          # dual route (via y0* = Φ₁(π*))
y_cov_primal = Phi_sep_md - min(phis)          # direct-enumeration primal route
slacks = [float(s) for s in lp.y_star]         # Φ₁(π) − Φ₁(π*) ≥ 0
# Tight constraints of the .md's dual = orderings achieving the ground
# state (zero slack). NB the solver's own active_set is the complement
# (indices whose x_π ≥ 0 constraint is pinned with positive price).
active_idx = [i for i, s in enumerate(slacks) if s <= DUAL_TOL]
active_names = [names[i] for i in active_idx]
duality_gap = abs(y_cov_primal - y_cov_dual)
y_cov_markov = Phi_sep_markov - min(phis)

print(f"  feasible orderings: {n_ord} (of {math.factorial(4)} permutations)")
print(f"  V̂_cov = z = {float(V_cov):.10f},  V̂_dressed = z·a₅+b₅ = {float(V_dressed):.10f}")
print(f"  Φ₁^H (md formula)      = {Phi_H_md:.10f}   (md quotes ≈ −1.406)")
print(f"  Φ₁^sep (md formula)    = {Phi_sep_md:.10f}   (md quotes ≈ −2.812)")
print(f"  Φ₁^sep (Markov-consistent) = {Phi_sep_markov:.10f}")
for i, (name, phi) in enumerate(orderings):
    mark = " ← ground state" if i in active_idx else ""
    print(f"    π={name:<14} Φ₁={phi:>12.8f}  slack={slacks[i]:.8f}{mark}")
print(f"  y_cov* (md Φ_sep, dual route)   = {y_cov_dual:.10f}")
print(f"  y_cov* (md Φ_sep, primal route) = {y_cov_primal:.10f}")
print(f"  duality gap                     = {duality_gap:.3e}")
print(f"  y_cov* in eV (×E_mol)           = {y_cov_dual * E_mol:.6f}")
print(f"  y_cov* (Markov-consistent Φ_sep) = {y_cov_markov:.10f}"
      f"  ({y_cov_markov * E_mol:.4f} eV)")

# ══════════════════════════════════════════════════════════════
# §7. Witness
# ══════════════════════════════════════════════════════════════

w = WitnessBuilder("h2-integer-lp", engine="python")
w.set_description(
    "H₂ molecular binding from integer LP. Scans all inter-atomic "
    "crossing operators (σ₀, σ₁, σ₀⁻¹, σ₁⁻¹) up to 4 crossings "
    "to find optimal binding configuration. Zero fitted parameters."
)
w.set_content_block("prop:h2-lp-dual-binding")

w.add_parameter("q", q0)
w.add_parameter("E_mol_eV", E_mol)
w.add_parameter("Phi_H_isolated", float(Phi_H))

w.add_data("best_1_crossing", {"ops": best_1[0], "binding": float(best_1[2]), "E_eV": float(best_1[3])})
w.add_data("best_2_crossings", {"ops": best_2[0], "binding": float(best_2[2]), "E_eV": float(best_2[3])})
w.add_data("best_3_crossings", {"ops": best_3[0], "binding": float(best_3[2]), "E_eV": float(best_3[3])})
w.add_data("best_4_crossings", {"ops": best_4[0], "binding": float(best_4[2]), "E_eV": float(best_4[3])})

# Find which one is closest to observed
all_best = [best_1, best_2, best_3, best_4]
closest = min(all_best, key=lambda b: abs(b[3] - obs))
w.add_data("closest_to_observed", {
    "ops": closest[0], "E_eV": float(closest[3]),
    "error_pct": float((closest[3]/obs - 1)*100),
})

w.add_assertion(
    "Binding is positive for at least one operator",
    computed=any(b[2] > 0 for b in all_best),
    expected=True,
    source="Integer LP scan",
)

# ── LP dual fields (AGENTS.md §"LP / SDP duals — first-class infra") ──
# Canonical six fields at data.<field>, in the .md's dual normalisation:
# y0_star = y_cov* = Φ₁^sep − Φ₁(π*); y_star = per-ordering slacks
# Φ₁(π) − Φ₁(π*) ≥ 0; active_set = tight (ground-state) orderings.
# primal_obj / dual_obj are y_cov* computed via the two independent
# routes (direct enumeration vs the canonical solve_operator_selection_lp
# occupancy LP); strong duality ⇒ duality_gap ≈ 0.
w.add_data("y0_star", float(y_cov_dual))
w.add_data("y_star", slacks)
w.add_data("active_set", active_idx)
w.add_data("primal_obj", float(y_cov_primal))
w.add_data("dual_obj", float(y_cov_dual))
w.add_data("duality_gap", float(duality_gap))
w.add_data("lp_dual_orderings", {
    "orderings": names,
    "phi1": [float(p) for p in phis],
    "active_orderings": active_names,
    "phi_H_md_formula": float(Phi_H_md),
    "phi_sep_md_formula": float(Phi_sep_md),
    "phi_sep_markov_consistent": float(Phi_sep_markov),
    "y_cov_star_md_phi_sep": float(y_cov_dual),
    "y_cov_star_md_phi_sep_eV": float(y_cov_dual * E_mol),
    "y_cov_star_markov_consistent": float(y_cov_markov),
    "y_cov_star_markov_consistent_eV": float(y_cov_markov * E_mol),
    "solver_result": lp.to_dict(),
    "note": (
        "y0_star/primal_obj/dual_obj use the .md's literal Φ₁^sep "
        "formula V^H = -q^5(q-q^-1)+q^-5, which mixes trace "
        "normalisations with the molecular V̂ᵢ = z·aᵢ+bᵢ and yields "
        "y_cov* < 0; the Markov-consistent Φ₁^sep = 2·ln|z·a₅+b₅| "
        "yields y_cov* = -2·ln z > 0. Ordering selection (interleaved "
        "ground state), slacks, active set and the duality gap are "
        "independent of this constant shift."
    ),
})

w.add_assertion(
    "LP dual: all per-ordering slacks nonnegative",
    computed=bool(min(slacks) >= -DUAL_TOL),
    expected=True,
    source="Ordering-selection LP dual (solve_operator_selection_lp)",
)
w.add_assertion(
    "LP dual: strong duality gap ~ 0",
    computed=bool(duality_gap < 1e-9 and lp.duality_gap < 1e-9),
    expected=True,
    source="Direct enumeration vs canonical LP solver",
)
w.add_assertion(
    "LP dual selects the interleaved ordering p1,e2,p2,e1 as ground state",
    computed=bool("p1,e2,p2,e1" in active_names),
    expected=True,
    source="Ordering-selection LP active set",
)

w.save()
print("Done.")
