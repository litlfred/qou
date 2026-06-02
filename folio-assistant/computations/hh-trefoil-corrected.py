#!/usr/bin/env python3
"""
H × trefoil × H with CORRECTED formulas from gluon branch.

Corrections from claude/docs-handover-knot-operator-k3XxB:
  1. Proton: B₃ + uu(σ₀) + ud(σ₁ mixed) + 2×σ₀(gluon) + ud(σ₀ mixed)
  2. Neutron: B₃ + ud(σ₀ mixed) + dd(σ₁⁻¹) + L₊L₋(σ₀σ₁σ₁σ₀) + ud(σ₀ mixed)
  3. Wedderburn: dim_std = [2]_q (not [3]_q)
  4. tr_M(e⁻) = z³
  5. 3-channel vertex volumes: w_sym·λ_sym + w_std·V̂_std + w_alt·λ_alt

Usage:
    cd folio-assistant/computations
    python3 hh-trefoil-corrected.py
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import math, sys
from pathlib import Path
from mpmath import mp
sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, Q_INV as qi0, HA as h, q_int
from witness_base import WitnessBuilder

z = 1.0/(q0**0.5+qi0**0.5)

# Corrected Wedderburn weights (from gluon branch fix)
def qint(k):
    return (q0**k - qi0**k) / h

def qfact(n):
    r = 1.0
    for k in range(1, n+1):
        r *= qint(k)
    return r

nf3 = qfact(3)
dim_std = qint(2)  # [2]_q, NOT [3]_q
w_sym_raw = 1.0 / nf3
w_std_raw = dim_std**2 / nf3
w_alt_raw = 1.0 / nf3
w_total = w_sym_raw + w_std_raw + w_alt_raw
w_sym = w_sym_raw / w_total
w_std = w_std_raw / w_total
w_alt = w_alt_raw / w_total

TWO_Q = q0 + qi0
from hecke_core import alpha_em, E_MOL as E_mol

NF_NAMES = ["gamma", "s0", "s1", "L+", "L-", "e-"]
TR_M = [1.0, z, z, z**2, z**2, z**3]

print("=" * 70)
print("H x TREFOIL x H (CORRECTED from gluon branch)")
print("=" * 70)
print("Corrections applied:")
print("  1. Proton: B3 + uu(s0) + ud(s1) + 2*s0(gluon) + ud(s0)")
print("  2. Neutron: B3 + ud(s0) + dd(s1inv) + L+L-(s0s1s1s0) + ud(s0)")
print("  3. dim_std = [2]_q = {:.6f}".format(dim_std))
print("  4. Weights: w_sym={:.4f}, w_std={:.4f}, w_alt={:.4f}".format(w_sym, w_std, w_alt))
print("  5. E_mol = E_hartree/[2]_q^2 = {:.4f} eV".format(E_mol))
print()

def hm(nf, c, d, g):
    r = [0.0]*6
    if g == 0:
        t = [(0,[(1,c),(0,d)]),(1,[(1,c*h),(0,c),(1,d)]),(2,[(3,c),(2,d)]),(3,[(3,c*h),(2,c),(3,d)]),(4,[(5,c),(4,d)]),(5,[(5,c*h),(4,c),(5,d)])]
    else:
        t = [(0,[(2,c),(0,d)]),(1,[(4,c),(1,d)]),(2,[(2,c*h),(0,c),(2,d)]),(3,[(5,c),(3,d)]),(4,[(4,c*h),(1,c),(4,d)]),(5,[(5,c*h),(3,c),(5,d)])]
    for si, tgts in t:
        if abs(nf[si]) < 1e-15: continue
        for ti, co in tgts: r[ti] += nf[si] * co
    return r

def nf_tr(nf): return sum(nf[i]*TR_M[i] for i in range(6))

def show(label, nf):
    t = nf_tr(nf)
    Phi = mp.log(abs(t)) if abs(t) > 1e-300 else float('inf')
    nf_str = ", ".join("{:+.6f}".format(v) for v in nf)
    print("  " + label)
    print("    NF = [" + nf_str + "]")
    print("    net={:.6f}, tr_M={:.6e}, Phi_1={:.6f}".format(sum(nf), t, float(Phi)))
    return t, Phi

# ── Build corrected proton ────────────────────────────────────
def build_proton():
    """Proton: B3 + uu(σ₀) + ud(σ₁ mixed) + 2×σ₀(gluon) + ud(σ₀ mixed)"""
    nf = [1.0, 0, 0, 0, 0, 0]
    # B₃ = (σ₀σ₁⁻¹)³
    for _ in range(3):
        nf = hm(nf, 1, 0, 0)      # σ₀
        nf = hm(nf, 1, -h, 1)     # σ₁⁻¹
    # Quarks + gluon (from symbolic-atom-builder.py)
    nf = hm(nf, 1, 0, 0)          # uu → σ₀
    nf = hm(nf, 1, -h/2, 1)       # ud → mixed on gen 1
    nf = hm(nf, 1, 0, 0)          # gluon σ₀ #1
    nf = hm(nf, 1, 0, 0)          # gluon σ₀ #2
    nf = hm(nf, 1, -h/2, 0)       # ud → mixed on gen 0
    return nf

# ── Build corrected neutron ───────────────────────────────────
def build_neutron():
    """Neutron: B3 + ud(σ₀ mixed) + dd(σ₁⁻¹) + L₊L₋(σ₀σ₁σ₁σ₀) + ud(σ₀ mixed)"""
    nf = [1.0, 0, 0, 0, 0, 0]
    for _ in range(3):
        nf = hm(nf, 1, 0, 0)
        nf = hm(nf, 1, -h, 1)
    nf = hm(nf, 1, -h/2, 0)       # ud → mixed on gen 0
    nf = hm(nf, 1, -h, 1)         # dd → σ₁⁻¹
    # L₊L₋ gluon = σ₀σ₁·σ₁σ₀
    nf = hm(nf, 1, 0, 0)          # σ₀ (L₊ part 1)
    nf = hm(nf, 1, 0, 1)          # σ₁ (L₊ part 2)
    nf = hm(nf, 1, 0, 1)          # σ₁ (L₋ part 1)
    nf = hm(nf, 1, 0, 0)          # σ₀ (L₋ part 2)
    nf = hm(nf, 1, -h/2, 0)       # ud → mixed on gen 0
    return nf

# ── H atom = proton + pe crossing ─────────────────────────────
def build_H():
    nf = build_proton()
    nf = hm(nf, 1, -h, 1)         # pe crossing (σ₁⁻¹)
    return nf

def apply_H(nf):
    """Apply H atom crossings to existing NF."""
    # Proton crossings
    for _ in range(3):
        nf = hm(nf, 1, 0, 0)
        nf = hm(nf, 1, -h, 1)
    nf = hm(nf, 1, 0, 0)
    nf = hm(nf, 1, -h/2, 1)
    nf = hm(nf, 1, 0, 0)
    nf = hm(nf, 1, 0, 0)
    nf = hm(nf, 1, -h/2, 0)
    # Electron
    nf = hm(nf, 1, -h, 1)
    return nf

# ══════════════════════════════════════════════════════════════
# Compute
# ══════════════════════════════════════════════════════════════

nf_H = build_H()
tr_H, Phi_H = show("H atom", nf_H)
print()

nf_ub = apply_H(list(nf_H))
tr_ub, Phi_ub = show("H x H (unbonded)", nf_ub)
print()

# ── Trefoil operators ─────────────────────────────────────────

operators = [
    ("Inverse trefoil s0i.s1i.s0i (w=-3)", [(0,1,-h),(1,1,-h),(0,1,-h)]),
    ("Inverse trefoil s1i.s0i.s1i (w=-3)", [(1,1,-h),(0,1,-h),(1,1,-h)]),
    ("Positive trefoil s0.s1.s0 (w=+3)",   [(0,1,0),(1,1,0),(0,1,0)]),
    ("(s1i)^2 Hopf link (w=-2)",            [(1,1,-h),(1,1,-h)]),
    ("(s1i)^3 (w=-3, NOT trefoil)",         [(1,1,-h),(1,1,-h),(1,1,-h)]),
    # Figure-8 knot 4_1 = s0.s1i.s0.s1i (w=0)
    ("Figure-8: s0.s1i.s0.s1i (w=0)",      [(0,1,0),(1,1,-h),(0,1,0),(1,1,-h)]),
    # T(2,5) = (s0.s1)^2.s0 (w=+5, torus knot)
    ("T(2,5) = s0.s1.s0.s1.s0 (w=+5)",     [(0,1,0),(1,1,0),(0,1,0),(1,1,0),(0,1,0)]),
    # Inverse T(2,5) (w=-5)
    ("T(2,5)^-1 (w=-5)",                    [(0,1,-h),(1,1,-h),(0,1,-h),(1,1,-h),(0,1,-h)]),
]

print("=" * 70)
print("KNOT OPERATORS BETWEEN TWO H ATOMS")
print("=" * 70)
print()

results = []
for label, ops in operators:
    nf = list(nf_H)
    for gen, c, d in ops:
        nf = hm(nf, c, d, gen)
    nf = apply_H(nf)

    t = nf_tr(nf)
    Phi = mp.log(abs(t)) if abs(t) > 1e-300 else float('inf')
    bind = Phi_ub - Phi
    E = bind * E_mol
    writhe = sum(-1 if d < 0 else +1 for _, _, d in ops)

    show(label, nf)
    print("    writhe={:+d}, binding={:.6f}, E={:.4f} eV".format(writhe, float(bind), float(E)))
    print()
    results.append((label, writhe, bind, E))

# ══════════════════════════════════════════════════════════════
# Summary
# ══════════════════════════════════════════════════════════════

print("=" * 70)
print("SUMMARY")
print("=" * 70)
print()
print("  {:>40s} {:>6s} {:>10s} {:>10s}".format("Operator", "w", "binding", "E(eV)"))
print("  " + "-" * 70)
print("  {:>40s} {:>6s} {:>10s} {:>10s}".format("unbonded", "0", "0", "0"))
for label, w, bind, E in results:
    marker = " <--" if 3.5 < E < 5.5 else ""
    print("  {:>40s} {:>+6d} {:>10.6f} {:>10.4f}{}".format(
        label[:40], w, float(bind), float(E), marker))

print()
print("  Observed D_0(H2) = 4.478 eV")
print()

# ── Witness ───────────────────────────────────────────────────
w = WitnessBuilder("hh-trefoil-corrected", engine="python")
w.set_description(
    "H x trefoil x H with corrected formulas from gluon branch. "
    "Proton: corrected quark order + 2 sigma_0 gluon. "
    "Neutron: L+L- gluon. dim_std = [2]_q."
)
w.set_content_block("def:h2-molecular-braid")
w.add_parameter("q", q0)
w.add_parameter("w_sym", w_sym)
w.add_parameter("w_std", w_std)
w.add_parameter("w_alt", w_alt)
w.add_parameter("E_mol_eV", E_mol)

for label, wr, bind, E in results:
    w.add_data(label[:30], {"writhe": wr, "binding": float(bind), "E_eV": float(E)})

w.save()
print("Done.")
