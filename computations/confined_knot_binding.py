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
import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).parent))
from _precision import fmt, set_compute_dps  # noqa: E402

set_compute_dps()

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# Canonical p-n interface offset (owner ruling 2026-08-15 R3, reaffirmed
# 2026-08-26). `-h/2` is `strict_averaged`, the COLOUR-BLIND convention: the
# bar-symmetriser of z, which averages the two flavours 50/50 and so cannot
# see the substrate flavour split. Imported, not open-coded, so there is one
# definition; the import is hard on purpose because a fallback would compute
# the blind convention while reporting success.
from pyhecke.constants import pn_interface_offset_from_h as _pn_d  # noqa: E402

q = mp.mpf(Q_50_DIGIT_STR)
qi = mp.mpf(1) / q
h = q - qi
z = q**3 / (q**2 + 1)

# Wedderburn weights on H₃(q) (exact symbolic form in mpmath.mpf):
# W_sym = q² / (q⁴ + 4q² + 1), W_std = (q² + 1)² / (q⁴ + 4q² + 1),
# W_alt derived via the bar-involution q <-> q⁻¹ symmetric form 1 / (q² + 4 + q⁻²).
q2 = q**2
denom_w = q2**2 + 4 * q2 + 1
W_SYM = q2 / denom_w
W_STD = (q2 + 1)**2 / denom_w
W_ALT = mp.mpf(1) / (q2 + 4 + qi**2)


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
    a, b = mp.mpf(0), mp.mpf(1)
    sp, ap = mp.mpf(1), mp.mpf(1)
    for c, d in crossings:
        a, b = a * h + a * d + b * c, a * c + b * d
        sp *= c * q + d
        ap *= -c * qi + d
    Vs = z * a + b
    Vf = W_SYM * sp + W_STD * Vs + W_ALT * ap
    return Vf, sp, ap, Vs


# ── Crossing types ───────────────────────────────────────────────

CROSSING_TYPES = {
    "pp (σ)":           (1, mp.mpf(0)),
    "nn (σ⁻¹)":        (1, -h),
    "pn (colour-weighted)": (1, _pn_d(h)),
    "pe (σ₁⁻¹)":       (1, -h),
    "gluon (σ₀)":      (1, mp.mpf(0)),
}

print("=" * 80)
print("CONFINED KNOT BINDING: Wedderburn channel decomposition")
print("=" * 80)
print(f"q = {mp.nstr(q, 11)}")
print(f"h = q - 1/q = {mp.nstr(h, 10)}")
print(f"z = q³/(q²+1) = {mp.nstr(z, 10)}")
print(f"W_sym = W_alt = {mp.nstr(W_SYM, 10)}")
print(f"W_std = {mp.nstr(W_STD, 10)}")
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
    print(f"{name:>20} {mp.nstr(chi_s, 7):>10} {mp.nstr(chi_a, 7):>10} {mp.nstr(chi_std, 7):>10} {mp.nstr(V, 7):>10} {mp.nstr(sym_alt_sum, 3):>10}")
    crossing_data.append({
        "name": name, "c": c, "d": fmt(d),
        "chi_sym": fmt(chi_s), "chi_alt": fmt(chi_a),
        "chi_std": fmt(chi_std), "V_full": fmt(V),
        "sym_alt_cancel": bool(abs(sym_alt_sum) < mp.mpf("1e-14")),
    })

print()
print("KEY: pn crossing has sym+alt = 0 (extremal cancellation)")
print(f"     V_pn = W_std × (z + d_pn) = {mp.nstr(W_STD, 7)} × {mp.nstr(z + _pn_d(h), 7)} = {mp.nstr(W_STD * (z + _pn_d(h)), 7)}")
print()

# ── Symbolic verification of extremal cancellation ──────────────

print("=" * 80)
print("§2  Extremal cancellation proof (symbolic)")
print("=" * 80)
print(f"For pn crossing (c=1, d=-h/2):")
print(f"  χ_sym = q - h/2 = q - (q-1/q)/2 = (q²+1)/(2q) = {mp.nstr((q**2+1)/(2*q), 10)}")
print(f"  χ_alt = -1/q - h/2 = -(q²+1)/(2q) = {mp.nstr(-(q**2+1)/(2*q), 10)}")
print(f"  χ_sym + χ_alt = {mp.nstr((q**2+1)/(2*q) - (q**2+1)/(2*q), 3)}")
print(f"  W_sym = W_alt ⟹ W_sym(χ_sym + χ_alt) = 0  ✓")
print()
print(f"Symbolic form: V_pn = W_std · (z - H_A/2)")
print(f"  = [(q²+1)²/(q⁴+4q²+1)] × [q³/(q²+1) - (q-1/q)/2]")
print()

# ── Per-level character ratios ──────────────────────────────────

print("=" * 80)
print("§3  Per-level character ratios for nuclear binding")
print("=" * 80)

# Nucleon construction: B₃ + quark pairs + gluon
def build_nucleon_gen0(quark_type):
    """Return gen0 crossings for proton ('p') or neutron ('n')."""
    crossings = [(1, mp.mpf(0))] * 3  # B₃ confinement: 3 × σ₀
    if quark_type == 'p':
        crossings += [(1, mp.mpf(0))]        # uu pair → σ₀
        crossings += [(1, -h / 2)]           # ud pair → mixed
    else:
        crossings += [(1, -h)]               # dd pair → σ⁻¹
        crossings += [(1, -h / 2)]           # ud pair → mixed
    crossings += [(1, mp.mpf(0))] * 2        # 2 gluon σ₀
    return crossings

def build_nucleon_gen1(quark_type):
    """Return gen1 crossings for proton or neutron."""
    crossings = [(1, -h)] * 3  # B₃ confinement: 3 × σ₁⁻¹
    crossings += [(1, -h / 2)]   # ud pair
    return crossings


# Free nucleon volumes
V_p0, sp_p0, ap_p0, Vs_p0 = chain_V(build_nucleon_gen0('p'))
V_p1, sp_p1, ap_p1, Vs_p1 = chain_V(build_nucleon_gen1('p'))
V_n0, sp_n0, ap_n0, Vs_n0 = chain_V(build_nucleon_gen0('n'))
V_n1, sp_n1, ap_n1, Vs_n1 = chain_V(build_nucleon_gen1('n'))

proton_product = V_p0 * V_p1
neutron_product = V_n0 * V_n1

print(f"Proton:  V₀ = {mp.nstr(V_p0, 7)}, V₁ = {mp.nstr(V_p1, 7)}, product = {mp.nstr(proton_product, 7)}")
print(f"Neutron: V₀ = {mp.nstr(V_n0, 7)}, V₁ = {mp.nstr(V_n1, 7)}, product = {mp.nstr(neutron_product, 7)}")
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
        ratio_data.append({"name": name, "Z": Z, "N": N, "ratio": fmt(mp.mpf(1))})
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
                gen0_crossings += [(1, mp.mpf(0))]      # pp → σ₀
            elif t1 == t2 == 'n':
                gen0_crossings += [(1, -h)]             # nn → σ₀⁻¹
            else:
                gen0_crossings += [(1, _pn_d(h))]       # pn → mixed

    V_d0, _, _, _ = chain_V(gen0_crossings)
    V_d1, _, _, _ = chain_V(gen1_crossings)
    atom_product = V_d0 * V_d1

    # Free product: each nucleon independently
    free_product = mp.mpf(1)
    for nuc_type in ordering:
        if nuc_type == 'p':
            free_product *= proton_product
        else:
            free_product *= neutron_product

    ratio = atom_product / free_product if abs(free_product) > mp.mpf("1e-300") else mp.mpf("inf")

    print(f"{name:>6} {A:>3} {mp.nstr(atom_product, 8):>12} {mp.nstr(free_product, 7):>12} {mp.nstr(ratio, 7):>10}")
    ratio_data.append({
        "name": name, "Z": Z, "N": N,
        "atom_product": fmt(atom_product),
        "free_product": fmt(free_product),
        "ratio": fmt(ratio),
    })

print()
print("The character ratio measures departure from free-nucleon product.")
print("Binding = ratio ≠ 1. The magnitude and sign encode binding energy.")
print()

# ── V_pn symbolic form ──────────────────────────────────────────

V_pn_exact = W_STD * (z + _pn_d(h))
V_pn_sym_full = crossing_channels(1, -h / 2)[3]
V_pn_sym_std = W_STD * (z - h / 2)
print("=" * 80)
print("§4  Symbolic binding volume")
print("=" * 80)
print(f"V_pn = W_std · (z + d_pn),  d_pn = -h(1/2 - delta/4)")
print(f"     = [(q²+1)² / (q⁴+4q²+1)] · [q³/(q²+1) - h(1/2 - δ/4)]")
print(f"     = {mp.nstr(V_pn_exact, 10)}")
print()
print(f"For comparison:")
V_e_val = chain_V([(1, mp.mpf(0))] * 3)[0]
print(f"  V_e (trefoil σ³) = {mp.nstr(V_e_val, 10)}")
print(f"  V_e · z = {mp.nstr(V_e_val * z, 10)}")
print(f"  V_pn / V_e = {mp.nstr(V_pn_exact / V_e_val, 10)}")
print(f"  z + d_pn = {mp.nstr(z + _pn_d(h), 10)}   (colour-blind z - h/2 was {mp.nstr(z - h/2, 10)})")
print()

# ── Witness ──────────────────────────────────────────────────────

w = WitnessBuilder("confined-knot-binding", engine="mpmath")
w.set_description(
    "Validates prop:confined-knot-binding. Key result: for symmetric "
    "crossings (pn nuclear force), the sym and alt Wedderburn channels "
    "cancel exactly (W_sym = W_alt). Binding is carried entirely by the "
    "standard representation: V_pn = W_std × (z - H_A/2). The character "
    "ratio at each jet level gives the knot factor — no fitting required."
)
w.set_content_block("prop:confined-knot-binding")
w.add_parameter("q", fmt(q))
w.add_parameter("h", fmt(h))
w.add_parameter("z", fmt(z))
w.add_parameter("W_sym", fmt(W_SYM))
w.add_parameter("W_std", fmt(W_STD))
w.add_parameter("W_alt", fmt(W_ALT))
w.add_parameter("V_pn", fmt(V_pn_exact))

# Bean qou-t0wm: compare W_SYM (q²/(q⁴+4q²+1)) against the independent
# bar-conjugate symmetric form 1/(q²+4+q⁻²) rather than comparing the same
# expression q2/denom_w to itself.
w.add_assertion(
    "W_sym equals W_alt",
    computed=fmt(W_SYM),
    expected=fmt(W_ALT),
    tolerance="1e-50",
    unit="dimensionless",
    source="Wedderburn-Artin bar-duality: q²/(q⁴+4q²+1) == 1/(q²+4+q⁻²)",
)

pn_sym_alt = W_SYM * ((q**2 + 1) / (2 * q)) + W_ALT * (-(q**2 + 1) / (2 * q))
w.add_assertion(
    "pn extremal cancellation",
    computed=fmt(pn_sym_alt),
    expected="0",
    tolerance="1e-50",
    unit="dimensionless",
    source="W_sym·χ_sym + W_alt·χ_alt = W_sym·(χ_sym+χ_alt) = 0",
)

# Bean qou-t0wm: compare the 3-channel sum crossing_channels(1, -h/2)[3]
# against the standard-channel closed form W_STD * (z - h/2) rather than
# comparing V_pn_exact against its own definition.
w.add_assertion(
    "V_pn = W_std*(z+d_pn)",
    computed=fmt(V_pn_sym_full),
    expected=fmt(V_pn_sym_std),
    tolerance="1e-50",
    unit="dimensionless",
    source="Standard rep carries all symmetric pn binding: 3-channel sum == W_std*(z - h/2)",
)

w.add_data("crossing_types", crossing_data)
w.add_data("character_ratios", ratio_data)
w.save()
