#!/usr/bin/env python3
"""
Quark-photon knot operations: complete NF analysis.

QUESTIONS ADDRESSED:
  1. Which basis knot, applied to a colored photon, yields the up quark
     (T₁₀ positive crossing) vs the down quark (T₁₀ negative crossing)?
  2. Complete NF for B₃ · crossings(d,u,u) — proton with explicit ordering
  3. Complete NF for B₃# · crossings(u,d,d) — neutron with mirror B₃
  4. Comprehensive knot operation dictionary: what happens when each
     basis element (𝟙, σ₀, σ₁, σ₀σ₁, σ₁σ₀, σ₀σ₁σ₀) acts on
     a colored photon?

CONVENTIONS:
  - Hecke relation: σᵢ² = HA·σᵢ + 𝟙  where HA = q − q⁻¹
  - Inverse: σᵢ⁻¹ = σᵢ − HA
  - B₃ = (σ₀σ₁⁻¹)³  Borromean confinement = gluon field
  - B₃# = (σ₁σ₀⁻¹)³  mirror Borromean
  - Proton = B₃ · crossings(u,u,d)  quarks = [u,u,d]
  - Neutron = B₃ · crossings(u,d,d) quarks = [u,d,d]
  - Up quark: unknot with positive crossing orientation → σ (positive)
  - Down quark: unknot with negative crossing orientation → σ⁻¹ (negative)
  - Typed crossings: uu → σ, dd → σ⁻¹, ud/du → ½(σ + σ⁻¹)

Depends on: q_parameter.py, experimental_constants.py
"""

import math
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp

q_sym = sp.Symbol('q', positive=True)

from q_parameter import Q as q0, Q_INV as qi0, HA as HA0, E_CROSS, HBAR_Q
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV

try:
    SHA = subprocess.check_output(
        ['git', 'rev-parse', 'HEAD'],
        cwd=str(Path(__file__).resolve().parent.parent.parent)
    ).decode().strip()
except Exception:
    SHA = "unknown"

# ── Energy scale from beta-decay calibration ──────────────────
_esc_path = Path(__file__).parent / "beta-decay-energy-scale.witness.json"
with _esc_path.open() as _f:
    _esc = json.load(_f)
E0 = _esc["energy_scales"]["E0_from_net_MeV"]

# ── Iwahori--Hecke algebra symbols ────────────────────────────
HA_sym = q_sym - 1 / q_sym
HA_num = HA0

PARTICLE_KNOT = {
    ():        ("ν",  "𝟏",      "unknot (0₁)"),
    (0,):      ("H⁰", "σ₀",     "virtual (ℓ=1)"),
    (1,):      ("H¹", "σ₁",     "virtual (ℓ=1)"),
    (0, 1):    ("L₊", "σ₀σ₁",   "Hopf link"),
    (1, 0):    ("L₋", "σ₁σ₀",   "Hopf link"),
    (0, 1, 0): ("e⁻", "σ₀σ₁σ₀", "trefoil (3₁)"),
}


def ws(w):
    if not w:
        return "𝟏"
    parts = []
    for g in w:
        if g >= 0:
            parts.append(f"σ_{g}")
        else:
            parts.append(f"σ_{-g-1}⁻¹")
    return "·".join(parts)


def pn(w):
    return PARTICLE_KNOT.get(w, ("?", "?", "?"))[0]


def eval_q0(c):
    if isinstance(c, (int, float)):
        return float(c)
    return float(c.subs(q_sym, q0))


# ══════════════════════════════════════════════════════════════
#  GRÖBNER--SHIRSHOV REDUCTION  (reused from breit-wheeler)
# ══════════════════════════════════════════════════════════════

def reduce_nf(terms_dict, label="", verbose=True):
    """Reduce a Hecke element. Returns (reduced_terms, net, steps)."""
    terms = {w: sp.expand(c) for w, c in terms_dict.items() if c != 0}
    hecke = yb = fc = 0
    step = 0

    if verbose:
        print(f"\n  ┌─ REDUCTION of {label}")
        print(f"  │  Input: {len(terms)} terms")

    changed = True
    while changed:
        changed = False
        new_terms = {}

        for word, coeff in terms.items():
            if coeff == 0:
                continue
            done = False

            # R1: Hecke σᵢ² → (q−q⁻¹)σᵢ + 1
            for pos in range(len(word) - 1):
                if word[pos] == word[pos + 1] and word[pos] >= 0:
                    i = word[pos]
                    pre, suf = word[:pos], word[pos + 2:]
                    w1 = pre + (i,) + suf
                    w2 = pre + suf
                    c1 = sp.expand(coeff * HA_sym)
                    c2 = sp.expand(coeff)
                    new_terms[w1] = sp.expand(new_terms.get(w1, 0) + c1)
                    new_terms[w2] = sp.expand(new_terms.get(w2, 0) + c2)
                    step += 1
                    hecke += 1
                    done = changed = True
                    break

            if done:
                continue

            # R2: Far-comm σᵢσⱼ → σⱼσᵢ for |i-j| ≥ 2, i > j
            for pos in range(len(word) - 1):
                i_gen, j_gen = word[pos], word[pos + 1]
                if (i_gen >= 0 and j_gen >= 0 and abs(i_gen - j_gen) >= 2
                        and i_gen > j_gen):
                    nw = word[:pos] + (j_gen, i_gen) + word[pos + 2:]
                    new_terms[nw] = sp.expand(new_terms.get(nw, 0) + coeff)
                    step += 1
                    fc += 1
                    done = changed = True
                    break

            if done:
                continue

            # R3: Yang-Baxter σᵢσᵢ₊₁σᵢ → σᵢ₊₁σᵢσᵢ₊₁
            for pos in range(len(word) - 2):
                a, b, c_g = word[pos], word[pos + 1], word[pos + 2]
                if (a == c_g and a >= 0 and b >= 0 and abs(a - b) == 1):
                    new_trip = (b, a, b)
                    old_trip = (a, b, a)
                    if new_trip < old_trip:
                        nw = word[:pos] + new_trip + word[pos + 3:]
                        new_terms[nw] = sp.expand(new_terms.get(nw, 0) + coeff)
                        step += 1
                        yb += 1
                        done = changed = True
                        break

            if not done:
                new_terms[word] = sp.expand(new_terms.get(word, 0) + coeff)

        terms = {w: sp.expand(c) for w, c in new_terms.items() if c != 0}

    net = sum(eval_q0(c) for c in terms.values())

    if verbose:
        print(f"  │  NF ({hecke} Hecke + {yb} YB + {fc} FC = {step} steps):")
        for w, c in sorted(terms.items(), key=lambda x: (len(x[0]), x[0])):
            v = eval_q0(c)
            name = pn(w)
            tag = f"  [{name}]" if name != "?" else ""
            print(f"  │    {v:+.10f} · {ws(w)}{tag}")
        print(f"  │  net = {net:+.10f}")
        print("  └─")

    return terms, net, {"hecke": hecke, "yb": yb, "fc": fc, "total": step}


def expand_inverse_word(word):
    """Expand σᵢ⁻¹ → σᵢ − (q−q⁻¹) in a word."""
    terms = {(): sp.Integer(1)}
    for g in word:
        new_terms = {}
        if g >= 0:
            for w, c in terms.items():
                nw = w + (g,)
                new_terms[nw] = sp.expand(new_terms.get(nw, 0) + c)
        else:
            i = -g - 1
            for w, c in terms.items():
                nw1 = w + (i,)
                new_terms[nw1] = sp.expand(new_terms.get(nw1, 0) + c)
                nw2 = w
                new_terms[nw2] = sp.expand(new_terms.get(nw2, 0) - c * HA_sym)
        terms = {w: sp.expand(c) for w, c in new_terms.items() if c != 0}
    return terms


def mul_terms(a_terms, b_terms):
    """Multiply two Hecke elements (concatenation)."""
    result = {}
    for wa, ca in a_terms.items():
        for wb, cb in b_terms.items():
            w = wa + wb
            c = sp.expand(ca * cb)
            result[w] = sp.expand(result.get(w, sp.Integer(0)) + c)
    return {w: c for w, c in result.items() if c != 0}


def crossing(type_i, type_j, gen):
    """Build typed crossing element for quark pair."""
    if type_i == type_j == 'u':
        return {(gen,): sp.Integer(1)}
    elif type_i == type_j == 'd':
        return {(gen,): sp.Integer(1), (): -(q_sym - 1 / q_sym)}
    else:  # mixed u-d or d-u
        return {(gen,): sp.Integer(1), (): -(q_sym - 1 / q_sym) / 2}


# ══════════════════════════════════════════════════════════════
#  MAIN ANALYSIS
# ══════════════════════════════════════════════════════════════

print("=" * 72)
print("  QUARK-PHOTON KNOT OPERATIONS ANALYSIS")
print("=" * 72)
print(f"  q₀  = {q0:.10f}")
print(f"  HA  = q−q⁻¹ = {HA_num:.10f}")
print(f"  E₀  = {E0:.6f} MeV")
print(f"  mₑ  = {M_E_MEV:.6f} MeV")
print(f"  mₚ  = {M_P_MEV:.6f} MeV")
print(f"  mₙ  = {M_N_MEV:.6f} MeV")

results = {}

# ══════════════════════════════════════════════════════════════
#  SECTION 1: KNOT OPERATION DICTIONARY
#  What does each basis element do when applied to various inputs?
# ══════════════════════════════════════════════════════════════

print("\n\n" + "=" * 72)
print("  SECTION 1: KNOT OPERATION DICTIONARY")
print("  Action of basis elements on identity and on each other")
print("=" * 72)

# The basis of H₃(q) in normal form (Gröbner-reduced) is:
#   {𝟙, σ₀, σ₁, σ₀σ₁, σ₁σ₀, σ₀σ₁σ₀}
# These correspond to:
#   {ν, H⁰, H¹, L₊, L₋, e⁻}

basis_words = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
basis_names = ["𝟙 (ν)", "σ₀ (H⁰)", "σ₁ (H¹)", "σ₀σ₁ (L₊)", "σ₁σ₀ (L₋)", "σ₀σ₁σ₀ (e⁻)"]

print("\n─── Left-multiplication table: X · Y ───")
print("  Each entry shows NF(X · Y) as a vector in the basis {𝟙, σ₀, σ₁, L₊, L₋, e⁻}")
print()

op_table = {}

for i, (wi, ni) in enumerate(zip(basis_words, basis_names)):
    for j, (wj, nj) in enumerate(zip(basis_words, basis_names)):
        product = {wi + wj: sp.Integer(1)}
        nf, net, _ = reduce_nf(product, f"{ni} · {nj}", verbose=False)
        key = f"{ni} · {nj}"
        entry = {}
        for w, c in sorted(nf.items(), key=lambda x: (len(x[0]), x[0])):
            v = eval_q0(c)
            entry[ws(w)] = v
        op_table[key] = {"terms": entry, "net": net}

# Print as a formatted table
print(f"  {'X · Y':<20s}", end="")
for bn in ["𝟙", "σ₀", "σ₁", "L₊", "L₋", "e⁻"]:
    print(f" {bn:>9s}", end="")
print(f" {'net':>10s}")
print("  " + "─" * 85)

for i, (wi, ni) in enumerate(zip(basis_words, basis_names)):
    for j, (wj, nj) in enumerate(zip(basis_words, basis_names)):
        key = f"{ni} · {nj}"
        entry = op_table[key]
        if j == 0:
            label = ni
        else:
            label = f"  · {nj}"
        if j == 0:
            print(f"\n  {ni:<20s}", end="")
        # Print coefficient for each basis element in row
        if j == 0:
            pass  # header line already started
    # Actually let's do a proper matrix print
    pass

# Let's reformat: show each product as a single line
print("\n  ── Detailed products ──\n")

for i, (wi, ni) in enumerate(zip(basis_words, basis_names)):
    for j, (wj, nj) in enumerate(zip(basis_words, basis_names)):
        product = {wi + wj: sp.Integer(1)}
        nf, net, _ = reduce_nf(product, f"{ni} · {nj}", verbose=False)
        parts = []
        for w, c in sorted(nf.items(), key=lambda x: (len(x[0]), x[0])):
            v = eval_q0(c)
            name = pn(w)
            parts.append(f"{v:+.4f}·{name}")
        line = " ".join(parts)
        print(f"    {ni:<14s} · {nj:<14s} = {line:<50s} net={net:+.6f}")
    print()

results["operation_dictionary"] = op_table

# ══════════════════════════════════════════════════════════════
#  SECTION 2: PHOTON WITH COLOR → QUARK IDENTIFICATION
#  Apply basis knots to a colored photon to see which produce
#  an element whose NF is dominated by the quark channel
# ══════════════════════════════════════════════════════════════

print("\n\n" + "=" * 72)
print("  SECTION 2: PHOTON → QUARK via KNOT OPERATORS")
print("  Which operator, applied to a photon, yields up vs down quark?")
print("=" * 72)

print("""
  A photon with color is: γ = 𝟙 + φ·σ₀ + φ·σ₁  (symmetric color)
  where φ ≈ 0.0487 (from Breit-Wheeler calibration)

  Question: What operator O transforms the photon γ into
  something with the quark crossing character?

  Up quark   = unknot with positive crossing → σ dominates
  Down quark = unknot with negative crossing → σ⁻¹ = σ − HA dominates

  We test: NF(O · γ) for each basis O ∈ {𝟙, σ₀, σ₁, L₊, L₋, e⁻}
  and also σ₀⁻¹, σ₁⁻¹.
""")

phi_val = 0.048664601063015865  # from BW calibration

# Build colored photon
gamma_color = {
    (): sp.Float(1.0),
    (0,): sp.Float(phi_val),
    (1,): sp.Float(phi_val),
}

# Test each operator
operators = [
    ("𝟙",      {(): sp.Integer(1)}),
    ("σ₀",     {(0,): sp.Integer(1)}),
    ("σ₁",     {(1,): sp.Integer(1)}),
    ("σ₀⁻¹",   {(0,): sp.Integer(1), (): -HA_sym}),
    ("σ₁⁻¹",   {(1,): sp.Integer(1), (): -HA_sym}),
    ("L₊",     {(0, 1): sp.Integer(1)}),
    ("L₋",     {(1, 0): sp.Integer(1)}),
    ("e⁻",     {(0, 1, 0): sp.Integer(1)}),
]

print("─── NF(O · γ_colored) for each operator O ───\n")

photon_ops = {}
for name, op in operators:
    product = mul_terms(op, gamma_color)
    nf, net, _ = reduce_nf(product, f"{name} · γ", verbose=False)
    parts = []
    for w, c in sorted(nf.items(), key=lambda x: (len(x[0]), x[0])):
        v = eval_q0(c)
        parts.append(f"{v:+.6f}·{pn(w)}")
    line = " ".join(parts)
    print(f"  {name:<6s} · γ  =  {line}")
    print(f"  {'':6s}        net = {net:+.10f}")
    print()
    photon_ops[name] = {
        "terms": {ws(w): eval_q0(c)
                  for w, c in sorted(nf.items(), key=lambda x: (len(x[0]), x[0]))},
        "net": net,
    }

results["photon_operations"] = photon_ops

# ══════════════════════════════════════════════════════════════
#  SECTION 3: QUARK NF — INDIVIDUAL QUARKS
#  Up quark as σ and down quark as σ⁻¹ in isolation
# ══════════════════════════════════════════════════════════════

print("\n\n" + "=" * 72)
print("  SECTION 3: INDIVIDUAL QUARK NF")
print("=" * 72)

print("""
  Convention from paper:
    Up quark   u = positive crossing orientation = σ
    Down quark d = negative crossing orientation = σ⁻¹ = σ − HA

  In H₃(q), quark on strand 0:
    u = σ₀     → NF = σ₀,  net = 1
    d = σ₀⁻¹   → NF = σ₀ − HA·𝟙, net = 1 − HA
""")

# Up quark
nf_u, net_u, _ = reduce_nf({(0,): sp.Integer(1)}, "u = σ₀ (up quark)")

# Down quark
d_expanded = expand_inverse_word((-1,))
nf_d, net_d, _ = reduce_nf(d_expanded, "d = σ₀⁻¹ (down quark)")

print(f"\n  net(u) = {net_u:+.10f}")
print(f"  net(d) = {net_d:+.10f}")
print(f"  Δ(d−u) = {net_d - net_u:+.10f}")

results["individual_quarks"] = {
    "up": {"net": net_u, "word": "σ₀"},
    "down": {"net": net_d, "word": "σ₀⁻¹ = σ₀ − HA·𝟙"},
}

# ══════════════════════════════════════════════════════════════
#  SECTION 4: COMPLETE B₃ AND B₃# (mirror)
# ══════════════════════════════════════════════════════════════

print("\n\n" + "=" * 72)
print("  SECTION 4: B₃ vs B₃# (MIRROR BORROMEAN)")
print("=" * 72)

# B₃ = (σ₀σ₁⁻¹)³
sig0 = {(0,): sp.Integer(1)}
sig1_inv = {(1,): sp.Integer(1), (): -HA_sym}

unit_fwd = mul_terms(sig0, sig1_inv)
print("\n─── B₃ = (σ₀σ₁⁻¹)³ ───")
unit2_fwd = mul_terms(unit_fwd, unit_fwd)
nf_unit2_fwd, _, _ = reduce_nf(unit2_fwd, "unit²")
b3_raw = mul_terms(nf_unit2_fwd, unit_fwd)
nf_b3, net_b3, _ = reduce_nf(b3_raw, "B₃ = (σ₀σ₁⁻¹)³")

# B₃# = (σ₁σ₀⁻¹)³ — mirror
sig1 = {(1,): sp.Integer(1)}
sig0_inv = {(0,): sp.Integer(1), (): -HA_sym}

unit_mirror = mul_terms(sig1, sig0_inv)
print("\n─── B₃# = (σ₁σ₀⁻¹)³ (mirror Borromean) ───")
unit2_mirror = mul_terms(unit_mirror, unit_mirror)
nf_unit2_mirror, _, _ = reduce_nf(unit2_mirror, "mirror unit²")
b3_mirror_raw = mul_terms(nf_unit2_mirror, unit_mirror)
nf_b3_mirror, net_b3_mirror, _ = reduce_nf(b3_mirror_raw, "B₃# = (σ₁σ₀⁻¹)³")

print(f"\n  net(B₃)  = {net_b3:+.10f}")
print(f"  net(B₃#) = {net_b3_mirror:+.10f}")

results["borromean"] = {
    "B3": {
        "net": net_b3,
        "terms": {ws(w): eval_q0(c) for w, c in sorted(nf_b3.items(),
                  key=lambda x: (len(x[0]), x[0]))},
    },
    "B3_mirror": {
        "net": net_b3_mirror,
        "terms": {ws(w): eval_q0(c) for w, c in sorted(nf_b3_mirror.items(),
                  key=lambda x: (len(x[0]), x[0]))},
    },
}

# ══════════════════════════════════════════════════════════════
#  SECTION 5: COMPLETE NF FOR ALL QUARK ORDERINGS
#  B₃·(duu), B₃·(uud), B₃#·(udd), B₃#·(ddu)
# ══════════════════════════════════════════════════════════════

print("\n\n" + "=" * 72)
print("  SECTION 5: COMPLETE NUCLEON NF FOR ALL ORDERINGS")
print("=" * 72)

configs = [
    # (name, quark_types, use_mirror_B3)
    ("Proton (B₃·[u,u,d])",   ['u', 'u', 'd'], False),
    ("Proton (B₃·[d,u,u])",   ['d', 'u', 'u'], False),
    ("Proton (B₃·[u,d,u])",   ['u', 'd', 'u'], False),
    ("Neutron (B₃·[u,d,d])",  ['u', 'd', 'd'], False),
    ("Neutron (B₃·[d,d,u])",  ['d', 'd', 'u'], False),
    ("Neutron (B₃·[d,u,d])",  ['d', 'u', 'd'], False),
    ("Proton (B₃#·[u,u,d])",  ['u', 'u', 'd'], True),
    ("Neutron (B₃#·[u,d,d])", ['u', 'd', 'd'], True),
]

nucleon_results = {}

for config_name, types, use_mirror in configs:
    print(f"\n{'─' * 72}")
    print(f"  {config_name}")
    pairs_desc = []
    for i in range(3):
        for j in range(i + 1, 3):
            pairs_desc.append(f"({i},{j})={types[i]}-{types[j]}")
    print(f"  Pairwise crossings: {', '.join(pairs_desc)}")
    print("─" * 72)

    if use_mirror:
        elem = dict(nf_b3_mirror)
    else:
        elem = dict(nf_b3)

    for i in range(3):
        for j in range(i + 1, 3):
            cx = crossing(types[i], types[j], i)
            product = mul_terms(elem, cx)
            elem, _, s = reduce_nf(product,
                f"{config_name} after ({types[i]},{types[j]})")

    net_val = sum(eval_q0(c) for c in elem.values())
    print(f"\n  ══ {config_name} NF: {len(elem)} terms, net = {net_val:+.10f} ══")
    for w, c in sorted(elem.items(), key=lambda x: (len(x[0]), x[0])):
        v = eval_q0(c)
        name = pn(w)
        tag = f"  [{name}]" if name != "?" else ""
        print(f"    {v:+.10f} · {ws(w)}{tag}")

    nucleon_results[config_name] = {
        "quarks": types,
        "mirror_B3": use_mirror,
        "net": net_val,
        "n_terms": len(elem),
        "terms": {ws(w): eval_q0(c)
                  for w, c in sorted(elem.items(), key=lambda x: (len(x[0]), x[0]))},
    }

results["nucleon_orderings"] = nucleon_results

# ══════════════════════════════════════════════════════════════
#  SECTION 6: PROTON AND NEUTRON DEFINITIONS (with gluon = B₃)
# ══════════════════════════════════════════════════════════════

print("\n\n" + "=" * 72)
print("  SECTION 6: CORRECTED PROTON/NEUTRON DEFINITIONS")
print("  nucleon = B₃(gluon) · crossings(quarks)")
print("=" * 72)

# Standard ordering
p_net = nucleon_results["Proton (B₃·[u,u,d])"]["net"]
n_net = nucleon_results["Neutron (B₃·[u,d,d])"]["net"]
delta = n_net - p_net

print(f"""
  ┌──────────────────────────────────────────────────────────┐
  │  PROTON 𝔭 = B₃ · crossing(u,u) · crossing(u,d) · crossing(u,d)  │
  │  B₃ = (σ₀σ₁⁻¹)³ = GLUON FIELD (Hypothesis C)          │
  │  quarks = [𝔲, 𝔲, 𝔡]                                    │
  │  net(𝔭) = {p_net:+.10f}                               │
  ├──────────────────────────────────────────────────────────┤
  │  NEUTRON 𝔫 = B₃ · crossing(u,d) · crossing(u,d) · crossing(d,d) │
  │  B₃ = (σ₀σ₁⁻¹)³ = GLUON FIELD                         │
  │  quarks = [𝔲, 𝔡, 𝔡]                                    │
  │  net(𝔫) = {n_net:+.10f}                               │
  ├──────────────────────────────────────────────────────────┤
  │  Δ(𝔫−𝔭)     = {delta:+.10f}                               │
  │  Δ × E₀     = {delta * E0:.6f} MeV                              │
  │  Q(CODATA)   = −0.78233341 MeV                          │
  └──────────────────────────────────────────────────────────┘
""")

# ── Also show without B₃ for comparison ──
print("─── Without B₃ (quarks only, no gluon field) ───")
for cfg_name, types in [("proton (quarks only)", ['u', 'u', 'd']),
                         ("neutron (quarks only)", ['u', 'd', 'd'])]:
    elem_bare = {(): sp.Integer(1)}
    for i in range(3):
        for j in range(i + 1, 3):
            cx = crossing(types[i], types[j], i)
            elem_bare = mul_terms(elem_bare, cx)
    nf_bare, net_bare, _ = reduce_nf(elem_bare, cfg_name)
    print(f"  net({cfg_name}) = {net_bare:+.10f}")

# ── Show B₃ decomposition ──
print(f"\n─── B₃ = gluon field decomposition ───")
print(f"  B₃ = (σ₀σ₁⁻¹)³")
print(f"  Each gluon unit (σ₀σ₁⁻¹) = one gluon exchange")
print(f"  The cube creates Borromean topology → confinement")
print(f"  net(B₃) = {net_b3:+.10f}  (≈1, near-unity gluon self-energy)")

results["corrected_definitions"] = {
    "proton": {
        "formula": "B₃ · crossing(u,u) · crossing(u,d) · crossing(u,d)",
        "components": "gluon_field(B₃) + flavor_crossings(u,u,d)",
        "net": p_net,
    },
    "neutron": {
        "formula": "B₃ · crossing(u,d) · crossing(u,d) · crossing(d,d)",
        "components": "gluon_field(B₃) + flavor_crossings(u,d,d)",
        "net": n_net,
    },
    "delta_net": delta,
    "delta_E_MeV": delta * E0,
}

# ══════════════════════════════════════════════════════════════
#  SECTION 7: COMPREHENSIVE KNOT OPERATION ACTIONS TABLE
#  (for appendix)
# ══════════════════════════════════════════════════════════════

print("\n\n" + "=" * 72)
print("  SECTION 7: KNOT OPERATION ACTIONS TABLE")
print("  (For appendix: what each knot does when applied)")
print("=" * 72)

print("""
  Legend:
    Each entry shows what particle content emerges when
    a row-knot is applied to a column-knot in H₃(q).
    The result is the Gröbner normal form.

  Operations:
    σ₀²  = HA·σ₀ + 𝟙       (Hecke relation)
    σ₁²  = HA·σ₁ + 𝟙       (Hecke relation)
    σ₀σ₁σ₀ = σ₁σ₀σ₁       (Yang-Baxter / braid relation)
    σ₀⁻¹ = σ₀ − HA·𝟙      (Hecke inverse)
""")

# Build the concise action table
action_table = {}

print("  ┌─────────────┬─────────────────────────────────────────────────────────┐")
print("  │ Operation   │ Normal form expansion                                   │")
print("  ├─────────────┼─────────────────────────────────────────────────────────┤")

action_entries = [
    ("σ₀²",          (0, 0)),
    ("σ₁²",          (1, 1)),
    ("σ₀σ₁",         (0, 1)),
    ("σ₁σ₀",         (1, 0)),
    ("σ₀σ₁σ₀",       (0, 1, 0)),
    ("σ₁σ₀σ₁",       (1, 0, 1)),
    ("σ₀σ₁σ₀σ₁",     (0, 1, 0, 1)),
    ("σ₁σ₀σ₁σ₀",     (1, 0, 1, 0)),
    ("σ₀σ₁²",        (0, 1, 1)),
    ("σ₁σ₀²",        (1, 0, 0)),
    ("σ₀²σ₁",        (0, 0, 1)),
    ("σ₁²σ₀",        (1, 1, 0)),
]

for label, word in action_entries:
    product = {word: sp.Integer(1)}
    nf, net, _ = reduce_nf(product, label, verbose=False)
    parts = []
    for w, c in sorted(nf.items(), key=lambda x: (len(x[0]), x[0])):
        v = eval_q0(c)
        name = pn(w)
        if abs(v - 1.0) < 1e-10:
            coeff_str = ""
        elif abs(v + 1.0) < 1e-10:
            coeff_str = "−"
        elif abs(v - round(v)) < 1e-10:
            coeff_str = f"{int(round(v))}·"
        else:
            coeff_str = f"{v:.4f}·"
        sign = "+" if v > 0 else ""
        parts.append(f"{coeff_str}{name}")
    line = " + ".join(parts).replace("+ −", "− ")
    print(f"  │ {label:<11s} │ {line:<55s} │")
    action_table[label] = {
        "word": ws(word),
        "nf_terms": {ws(w): eval_q0(c)
                     for w, c in sorted(nf.items(), key=lambda x: (len(x[0]), x[0]))},
        "net": net,
    }

# Now add inverse operations
inverse_entries = [
    ("σ₀⁻¹",        (-1,)),
    ("σ₁⁻¹",        (-2,)),
    ("σ₀⁻¹σ₁⁻¹",    (-1, -2)),
    ("σ₁⁻¹σ₀⁻¹",    (-2, -1)),
    ("σ₀⁻¹σ₁⁻¹σ₀⁻¹", (-1, -2, -1)),
]

for label, word in inverse_entries:
    expanded = expand_inverse_word(word)
    nf, net, _ = reduce_nf(expanded, label, verbose=False)
    parts = []
    for w, c in sorted(nf.items(), key=lambda x: (len(x[0]), x[0])):
        v = eval_q0(c)
        name = pn(w)
        if abs(v - 1.0) < 1e-10:
            coeff_str = ""
        elif abs(v + 1.0) < 1e-10:
            coeff_str = "−"
        else:
            coeff_str = f"{v:.4f}·"
        parts.append(f"{coeff_str}{name}")
    line = " + ".join(parts).replace("+ −", "− ")
    print(f"  │ {label:<11s} │ {line:<55s} │")
    action_table[label] = {
        "word": label,
        "nf_terms": {ws(w): eval_q0(c)
                     for w, c in sorted(nf.items(), key=lambda x: (len(x[0]), x[0]))},
        "net": net,
    }

print("  └─────────────┴─────────────────────────────────────────────────────────┘")

results["action_table"] = action_table

# ══════════════════════════════════════════════════════════════
#  SECTION 8: PHOTON → QUARK-ANTIQUARK PAIR PRODUCTION
#  γ → q + q̄  near strong field
# ══════════════════════════════════════════════════════════════

print("\n\n" + "=" * 72)
print("  SECTION 8: PHOTON → QUARK-ANTIQUARK PAIR PRODUCTION")
print("  γ(colored) near nucleus → u + ū  or  d + d̄")
print("=" * 72)

print("""
  In standard QCD, photon pair production near an atomic nucleus
  can produce quark-antiquark pairs when the photon energy exceeds
  the pair production threshold.

  In our framework:
    Photon = 𝟙 (identity in H₃(q))
    Up quark = σ₀ (positive crossing)
    Down quark = σ₀⁻¹ = σ₀ − HA (negative crossing)
    Antiquark = mirror of quark

  The question is: which knot operation (representing the
  nuclear field) converts a photon into a quark pair?

  If the field applies σ₀ to a photon:
    σ₀ · 𝟙 = σ₀  → this IS the up quark!

  If the field applies σ₀⁻¹ to a photon:
    σ₀⁻¹ · 𝟙 = σ₀ − HA·𝟏  → this IS the down quark!

  So the nuclear field operator IS the quark itself:
    - Positive crossing (σ₀) = up quark creation operator
    - Negative crossing (σ₀⁻¹) = down quark creation operator
""")

# Verify: σ₀ applied to photon
print("─── σ₀ · 𝟙 (up quark creation) ───")
nf_u_from_photon, net_u_from_photon, _ = reduce_nf(
    {(0,): sp.Integer(1)}, "σ₀ · 𝟙 → up quark")

print("\n─── σ₀⁻¹ · 𝟙 (down quark creation) ───")
d_from_photon = expand_inverse_word((-1,))
nf_d_from_photon, net_d_from_photon, _ = reduce_nf(
    d_from_photon, "σ₀⁻¹ · 𝟙 → down quark")

# Now with colored photon
print("\n─── σ₀ · γ(colored) ───")
product_u = mul_terms({(0,): sp.Integer(1)}, gamma_color)
nf_u_colored, net_u_colored, _ = reduce_nf(product_u, "σ₀ · γ(colored)")

print("\n─── σ₀⁻¹ · γ(colored) ───")
sig0_inv_terms = {(0,): sp.Integer(1), (): sp.Float(-HA_num)}
product_d = mul_terms(sig0_inv_terms, gamma_color)
nf_d_colored, net_d_colored, _ = reduce_nf(product_d, "σ₀⁻¹ · γ(colored)")

print(f"""
  Results:
    σ₀ · γ:    net = {net_u_colored:+.10f}  (up quark channel)
    σ₀⁻¹ · γ:  net = {net_d_colored:+.10f}  (down quark channel)
    Δ(d−u):         = {net_d_colored - net_u_colored:+.10f}

  The crossing orientation determines the quark flavor:
    σ₀   → up   (positive crossing, charge +2/3)
    σ₀⁻¹ → down (negative crossing, charge −1/3)
""")

results["quark_creation"] = {
    "up_from_photon": {
        "operator": "σ₀",
        "net": net_u_colored,
    },
    "down_from_photon": {
        "operator": "σ₀⁻¹",
        "net": net_d_colored,
    },
}

# ══════════════════════════════════════════════════════════════
#  SUMMARY
# ══════════════════════════════════════════════════════════════

print("\n\n" + "=" * 72)
print("  SUMMARY OF KEY RESULTS")
print("=" * 72)

print(f"""
  1. QUARK IDENTIFICATION:
     Up quark   = σ₀ (positive crossing)   net = {net_u:+.10f}
     Down quark = σ₀⁻¹ (negative crossing) net = {net_d:+.10f}
     Both are unknots (T₁₀) distinguished by orientation.

  2. B₃ = GLUON FIELD:
     B₃ = (σ₀σ₁⁻¹)³  Borromean confinement
     net(B₃)  = {net_b3:+.10f}
     net(B₃#) = {net_b3_mirror:+.10f}

  3. NUCLEON NF (corrected: B₃ + quarks):
     net(proton  = B₃·[u,u,d]) = {p_net:+.10f}
     net(neutron = B₃·[u,d,d]) = {n_net:+.10f}
     Δ(n−p) = {delta:+.10f}
     Δ × E₀ = {delta * E0:.6f} MeV  (CODATA: −0.782333 MeV)

  4. QUARK ORDERINGS:
""")

for name, data in nucleon_results.items():
    print(f"     {name:<30s} net = {data['net']:+.10f}")

print(f"""
  5. PHOTON → QUARK:
     σ₀ · γ(colored)   = up quark channel:   net = {net_u_colored:+.10f}
     σ₀⁻¹ · γ(colored) = down quark channel: net = {net_d_colored:+.10f}

  6. KNOT OPERATION DICTIONARY:
     {len(action_table)} entries computed (see appendix table)
""")

# ══════════════════════════════════════════════════════════════
#  WITNESS JSON
# ══════════════════════════════════════════════════════════════

witness = {
    "name": "quark-photon-operations",
    "description": (
        "Comprehensive quark-photon knot operations analysis. "
        "Section 1: Knot operation dictionary (basis element products). "
        "Section 2: Photon → quark via knot operators. "
        "Section 3: Individual quark NF (up = σ, down = σ⁻¹). "
        "Section 4: B₃ vs B₃# (mirror Borromean). "
        "Section 5: Complete nucleon NF for all quark orderings. "
        "Section 6: Corrected proton/neutron definitions (B₃ = gluon field). "
        "Section 7: Comprehensive knot operation actions table. "
        "Section 8: Photon → quark-antiquark pair production."
    ),
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "git_sha": SHA,
    "parameters": {
        "q0": q0,
        "HA": HA_num,
        "E0_MeV": E0,
        "m_e_MeV": M_E_MEV,
        "m_p_MeV": M_P_MEV,
        "m_n_MeV": M_N_MEV,
        "phi_color": phi_val,
    },
    "results": results,
}

out_path = Path(__file__).with_suffix(".witness.json")
out_path.write_text(json.dumps(witness, indent=2))
print(f"  Witness written to {out_path.name}")
