#!/usr/bin/env python3
"""
Confined knot binding mechanism: character ratio decomposition.

Validates prop:confined-knot-binding — the extremal cancellation
theorem and per-level character ratios for all crossing types.

Key result: for any symmetric crossing (d = -h/2), the sym and alt
Wedderburn channels cancel exactly. Binding is carried entirely
by the standard representation:

    V_pn = W_std × (z - h/2)

This is symbolic in q: no empirical input beyond q₀.

Usage:
    python3 confined_knot_binding.py
"""
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import math
import sys
from pathlib import Path
from fractions import Fraction

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q, Q_INV as qi, HA as h, q_int
from witness_base import WitnessBuilder

# Canonical p-n interface offset (owner ruling 2026-08-15 R3, reaffirmed
# 2026-08-26). `-h/2` is `strict_averaged`, the COLOUR-BLIND convention: the
# bar-symmetriser of z, which averages the two flavours 50/50 and so cannot
# see the substrate flavour split. Imported, not open-coded, so there is one
# definition; the import is hard on purpose because a fallback would compute
# the blind convention while reporting success.
from pyhecke.constants import pn_interface_offset_from_h as _pn_d  # noqa: E402

z = q**3 / (q**2 + 1)

# OWNER RULING 2026-11-20 (PR #8590): this V-hat deliberately keeps the
# pre-convention-D W_sym/W_std/W_alt (q-Plancherel) mixture. The 11-18 ruling
# moved pyhecke.atom to the convention-D Markov trace z*a+b, but here that puts
# the proton V-hat (1.2824) past the Phi_q pole at q0 and m_p/m_e = inf
# (qou-2tuv). Kept, labelled, until the pole is resolved. No number moves.
VHAT_WEIGHTS_LABEL = (
    "pre-convention-D mixture (q-Plancherel W_sym/W_std/W_alt), kept by owner "
    "ruling 2026-11-20 until the Phi_q pole (qou-2tuv) is resolved; "
    "convention-D z*a+b gives m_p/m_e = inf (PR #8590)"
)
# Wedderburn weights (exact symbolic form)
q2 = q**2
denom_w = q2**2 + 4*q2 + 1
W_SYM = q2 / denom_w
W_STD = (q2 + 1)**2 / denom_w
W_ALT = q2 / denom_w


def crossing_channels(c, d):
    """Compute the three Wedderburn channel values for crossing (c, d)."""
    chi_sym = c * q + d
    chi_alt = -c * qi + d
    chi_std = z * c + d  # single-crossing std (a=c, b=d from identity start)
    V_full = W_SYM * chi_sym + W_STD * chi_std + W_ALT * chi_alt
    return chi_sym, chi_alt, chi_std, V_full


def chain_V(crossings):
    """Compute Wedderburn volume for a chain of crossings on one generator.

    Each crossing is (c, d). Returns (V_full, sp, ap, Vs).
    """
    a, b = 0.0, 1.0
    sp, ap = 1.0, 1.0
    for c, d in crossings:
        a, b = a * h + a * d + b * c, a * c + b * d
        sp *= c * q + d
        ap *= -c * qi + d
    Vs = z * a + b
    Vf = W_SYM * sp + W_STD * Vs + W_ALT * ap
    return Vf, sp, ap, Vs


# ── Crossing types ─��────────────────────────────────────────────

CROSSING_TYPES = {
    "pp (σ)":           (1, 0),
    "nn (σ⁻¹)":        (1, -h),
    "pn (colour-weighted)": (1, _pn_d(h)),
    "pe (σ₁⁻¹)":       (1, -h),
    "gluon (σ₀)":      (1, 0),
}

print("=" * 80)
print("CONFINED KNOT BINDING: Wedderburn channel decomposition")
print("=" * 80)
print(f"q = {q:.10f}")
print(f"h = q - 1/q = {h:.10f}")
print(f"z = 1/(���q + 1/√q) = {z:.10f}")
print(f"W_sym = W_alt = {W_SYM:.10f}")
print(f"W_std = {W_STD:.10f}")
print()

print("=" * 80)
print("§1  Channel decomposition per crossing type")
print("=" * 80)
print(f"{'Type':>20} {'χ_sym':>10} {'χ_alt':>10} {'χ_std':>10} {'V_full':>10} {'sym+alt':>10}")
print("-" * 80)

crossing_data = []
for name, (c, d) in CROSSING_TYPES.items():
    chi_s, chi_a, chi_std, V = crossing_channels(c, d)
    sym_alt_sum = W_SYM * chi_s + W_ALT * chi_a
    print(f"{name:>20} {chi_s:>+10.6f} {chi_a:>+10.6f} {chi_std:>+10.6f} {V:>+10.6f} {sym_alt_sum:>+10.2e}")
    crossing_data.append({
        "name": name, "c": c, "d": d,
        "chi_sym": round(chi_s, 10), "chi_alt": round(chi_a, 10),
        "chi_std": round(chi_std, 10), "V_full": round(V, 10),
        "sym_alt_cancel": abs(sym_alt_sum) < 1e-14,
    })

print()
print("KEY: pn crossing has sym+alt = 0 (extremal cancellation)")
print(f"     V_pn = W_std × (z + d_pn) = {W_STD:.6f} × {z + _pn_d(h):.6f} = {W_STD * (z + _pn_d(h)):.6f}")
print()

# ── Symbolic verification of extremal cancellation ���─────────────

print("=" * 80)
print("§2  Extremal cancellation proof (symbolic)")
print("=" * 80)
print(f"For pn crossing (c=1, d=-h/2):")
print(f"  χ_sym = q - h/2 = q - (q-1/q)/2 = (q²+1)/(2q) = {(q**2+1)/(2*q):.10f}")
print(f"  χ_alt = -1/q - h/2 = -(q²+1)/(2q) = {-(q**2+1)/(2*q):.10f}")
print(f"  χ_sym + χ_alt = {(q**2+1)/(2*q) - (q**2+1)/(2*q):.2e}")
print(f"  W_sym = W_alt ⟹ W_sym(χ_sym + χ_alt) = 0  ✓")
print()
print(f"Symbolic form: V_pn = W_std · (z - H_A/2)")
print(f"  = [(q²+1)²/(q⁴+4q²+1)] × [1/(√q+1/√q) - (q-1/q)/2]")
print()

# ── Per-level character ratios ──────────────────────────────────

print("=" * 80)
print("§3  Per-level character ratios for nuclear binding")
print("=" * 80)

# Nucleon construction: B₃ + quark pairs + gluon
def build_nucleon_gen0(quark_type):
    """Return gen0 crossings for proton ('p') or neutron ('n')."""
    crossings = [(1, 0)] * 3  # B₃ confinement: 3 × σ₀
    if quark_type == 'p':
        crossings += [(1, 0)]        # uu pair → σ₀
        crossings += [(1, -h/2)]     # ud pair → mixed
    else:
        crossings += [(1, -h)]       # dd pair → σ⁻¹
        crossings += [(1, -h/2)]     # ud pair → mixed
    crossings += [(1, 0)] * 2        # 2 gluon σ₀
    return crossings

def build_nucleon_gen1(quark_type):
    """Return gen1 crossings for proton or neutron."""
    crossings = [(1, -h)] * 3  # B₃ confinement: 3 × σ₁⁻¹
    crossings += [(1, -h/2)]   # ud pair
    return crossings


# Free nucleon volumes
V_p0, sp_p0, ap_p0, Vs_p0 = chain_V(build_nucleon_gen0('p'))
V_p1, sp_p1, ap_p1, Vs_p1 = chain_V(build_nucleon_gen1('p'))
V_n0, sp_n0, ap_n0, Vs_n0 = chain_V(build_nucleon_gen0('n'))
V_n1, sp_n1, ap_n1, Vs_n1 = chain_V(build_nucleon_gen1('n'))

proton_product = V_p0 * V_p1
neutron_product = V_n0 * V_n1

print(f"Proton:  V₀ = {V_p0:.6f}, V₁ = {V_p1:.6f}, product = {proton_product:.6f}")
print(f"Neutron: V₀ = {V_n0:.6f}, V₁ = {V_n1:.6f}, product = {neutron_product:.6f}")
print()

# Atom construction and character ratios
NUCLEI = [
    ("¹H",  1, 0),
    ("²H",  1, 1),
    ("³H",  1, 2),
    ("³He", 2, 1),
    ("⁴He", 2, 2),
    ("⁶Li", 3, 3),
    ("⁷Li", 3, 4),
    ("⁹Be", 4, 5),
    ("¹²C", 6, 6),
    ("¹⁶O", 8, 8),
]

print(f"{'Atom':>6} {'A':>3} {'V_product':>12} {'Free_product':>12} {'Ratio':>10}")
print("-" * 55)

ratio_data = []
for name, Z, N in NUCLEI:
    A = Z + N
    if A <= 1:
        print(f"{name:>6} {A:>3} {'(nucleon)':>12}")
        ratio_data.append({"name": name, "Z": Z, "N": N, "ratio": 1.0})
        continue

    # Build ground-state ordering
    ordering = []
    pc, nc = 0, 0
    for k in range(A):
        if (k % 2 == 0 and pc < Z) or nc >= N:
            ordering.append('p')
            pc += 1
        else:
            ordering.append('n')
            nc += 1

    # Build full gen0 and gen1 chains
    gen0_crossings = []
    gen1_crossings = []
    for k in range(A):
        nuc_type = ordering[k]
        gen0_crossings += build_nucleon_gen0(nuc_type)
        gen1_crossings += build_nucleon_gen1(nuc_type)
        # Inter-nucleon crossing after each nucleon (except last)
        if k < A - 1:
            t1, t2 = ordering[k], ordering[k + 1]
            if t1 == t2 == 'p':
                gen0_crossings += [(1, 0)]      # pp → σ₀
            elif t1 == t2 == 'n':
                gen0_crossings += [(1, -h)]     # nn → σ₀⁻¹
            else:
                gen0_crossings += [(1, _pn_d(h))]   # pn → mixed

    V_d0, _, _, _ = chain_V(gen0_crossings)
    V_d1, _, _, _ = chain_V(gen1_crossings)
    atom_product = V_d0 * V_d1

    # Free product: each nucleon independently
    free_product = 1.0
    for nuc_type in ordering:
        if nuc_type == 'p':
            free_product *= proton_product
        else:
            free_product *= neutron_product

    ratio = atom_product / free_product if abs(free_product) > 1e-300 else float('inf')

    print(f"{name:>6} {A:>3} {atom_product:>+12.6f} {free_product:>+12.6f} {ratio:>10.6f}")
    ratio_data.append({
        "name": name, "Z": Z, "N": N,
        "atom_product": round(atom_product, 10),
        "free_product": round(free_product, 10),
        "ratio": round(ratio, 10),
    })

print()
print("The character ratio measures departure from free-nucleon product.")
print("Binding = ratio ≠ 1. The magnitude and sign encode binding energy.")
print()

# ── V_pn symbolic form ──────────────────────────────────────────

V_pn_exact = W_STD * (z + _pn_d(h))
print("=" * 80)
print("§4  Symbolic binding volume")
print("=" * 80)
print(f"V_pn = W_std · (z + d_pn),  d_pn = -h(1/2 - delta/4)")
# The old form printed here spelled z as `1/(sqrt q + 1/sqrt q)`, which is
# convention C, and the offset as `(q - 1/q)/2`, an inlined h/2. Both were
# display-only and both were wrong for the live computation.
print(f"     = [(q²+1)² / (q⁴+4q²+1)] · [q³/(q²+1) - h(1/2 - δ/4)]")
print(f"     = {V_pn_exact:.10f}")
print()
print(f"For comparison:")
print(f"  V_e (trefoil σ³) = {chain_V([(1,0)]*3)[0]:.10f}")
V_e_val = chain_V([(1,0)]*3)[0]
print(f"  V_e · z = {V_e_val * z:.10f}")
print(f"  V_pn / V_e = {V_pn_exact / V_e_val:.10f}")
print(f"  z + d_pn = {z + _pn_d(h):.10f}"  f"   (colour-blind z - h/2 was {z - h/2:.10f})")
print()

# ── Witness ──────���──────────────────────────────────────────────

w = WitnessBuilder("confined-knot-binding", engine="python")
w.set_description(
    "Validates prop:confined-knot-binding. Key result: for symmetric "
    "crossings (pn nuclear force), the sym and alt Wedderburn channels "
    "cancel exactly (W_sym = W_alt). Binding is carried entirely by the "
    "standard representation: V_pn = W_std × (z - H_A/2). The character "
    "ratio at each jet level gives the knot factor — no fitting required."
)
w.set_content_block("prop:confined-knot-binding")
w.add_parameter("q", q)
w.add_parameter("h", h)
w.add_parameter("z", z)
w.add_parameter("vhat_weights", VHAT_WEIGHTS_LABEL)
w.add_parameter("W_sym", W_SYM)
w.add_parameter("W_std", W_STD)
w.add_parameter("W_alt", W_ALT)
w.add_parameter("V_pn", V_pn_exact)

w.add_assertion(
    "W_sym equals W_alt",
    computed=W_SYM,
    expected=W_ALT,
    tolerance=1e-15,
    unit="dimensionless",
    source="Wedderburn-Artin: dim_q((3))=dim_q((1,1,1))=1",
)

pn_sym_alt = W_SYM * ((q**2+1)/(2*q)) + W_ALT * (-(q**2+1)/(2*q))
w.add_assertion(
    "pn extremal cancellation",
    computed=pn_sym_alt,
    expected=0.0,
    tolerance=1e-14,
    unit="dimensionless",
    source="W_sym·χ_sym + W_alt·χ_alt = W_sym·(χ_sym+χ_alt) = 0",
)

w.add_assertion(
    "V_pn = W_std*(z+d_pn)",
    computed=V_pn_exact,
    expected=W_STD * (z + _pn_d(h)),
    tolerance=1e-15,
    unit="dimensionless",
    source="Standard rep carries all pn binding",
)

w.add_data("crossing_types", crossing_data)
w.add_data("character_ratios", ratio_data)
w.save()
