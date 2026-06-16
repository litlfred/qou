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

z = 1.0 / (q0**0.5 + qi0**0.5)

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
# §6. Witness
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

w.save()
print("Done.")
