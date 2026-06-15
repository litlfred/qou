#!/usr/bin/env python3
"""
Nucleon NF with explicit Hopf-link gluons.

MOTIVATION: The previous computation (breit-wheeler-nucleon-nf.py) used
  nucleon = B₃ · crossings(quarks)
where B₃ = (σ₀σ₁⁻¹)³ is the Borromean confinement braid.

However, this omitted the GLUON FIELD.  From the knot-particle dictionary:
  Gluon = Hopf link T(2,2) = σᵢ² (closure of two parallel crossings)

In H₃(q), σᵢ² = HA·σᵢ + 𝟙 (Hecke relation), so a Hopf link gluon
between quarks on strands i and i+1 is the element (HA·σᵢ + 𝟙).

For 3 quarks on 3 strands (generators σ₀, σ₁):
  - Pair (0,1): gluon at σ₀ → σ₀² = HA·σ₀ + 𝟙
  - Pair (0,2): via σ₀ (adjacency approx) → σ₀² = HA·σ₀ + 𝟙
  - Pair (1,2): gluon at σ₁ → σ₁² = HA·σ₁ + 𝟙

MODELS TESTED:
  Model A: nucleon = B₃ · crossings  (no gluons — previous)
  Model B: nucleon = B₃ · [σᵢ²·cx]  per pair (Hopf gluon per pair)
  Model C: nucleon = B₃ · σ₀²·σ₁² · crossings  (global Hopf dressing)
  Model D: nucleon = B₃ · L₊ · crossings  (single Hopf link L₊=σ₀σ₁)
  Model E: nucleon = B₃ · L₊·L₋ · crossings  (Hopf pair)

Also computes basic particle NFs for the appendix witness table.

Depends on: q_parameter.py, experimental_constants.py
"""

import math
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp

# P2.5 migration: helper available; per-witness expose_polynomial call is a follow-up
import sys as _p25_sys
from pathlib import Path as _P25Path
_p25_sys.path.insert(0, str(_P25Path(__file__).parent))
from witness_polynomial import expose_polynomial  # noqa: F401

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

# ── Energy scale ──────────────────────────────────────────────
_esc_path = Path(__file__).parent / "beta-decay-energy-scale.witness.json"
with _esc_path.open() as _f:
    _esc = json.load(_f)
E0 = _esc["energy_scales"]["E0_from_net_MeV"]

# ── Symbols ───────────────────────────────────────────────────
HA_sym = q_sym - 1 / q_sym
HA_num = HA0

PARTICLE_KNOT = {
    ():        ("ν",  "𝟏",      "unknot (0₁)"),
    (0,):      ("σ₀", "σ₀",     "virtual (ℓ=1)"),
    (1,):      ("σ₁", "σ₁",     "virtual (ℓ=1)"),
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
#  GRÖBNER--SHIRSHOV REDUCTION
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
                    step += 1; hecke += 1
                    done = changed = True
                    break

            if done:
                continue

            for pos in range(len(word) - 1):
                i_gen, j_gen = word[pos], word[pos + 1]
                if (i_gen >= 0 and j_gen >= 0 and abs(i_gen - j_gen) >= 2
                        and i_gen > j_gen):
                    nw = word[:pos] + (j_gen, i_gen) + word[pos + 2:]
                    new_terms[nw] = sp.expand(new_terms.get(nw, 0) + coeff)
                    step += 1; fc += 1
                    done = changed = True
                    break

            if done:
                continue

            for pos in range(len(word) - 2):
                a, b, c_g = word[pos], word[pos + 1], word[pos + 2]
                if (a == c_g and a >= 0 and b >= 0 and abs(a - b) == 1):
                    new_trip = (b, a, b)
                    old_trip = (a, b, a)
                    if new_trip < old_trip:
                        nw = word[:pos] + new_trip + word[pos + 3:]
                        new_terms[nw] = sp.expand(new_terms.get(nw, 0) + coeff)
                        step += 1; yb += 1
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
    else:
        return {(gen,): sp.Integer(1), (): -(q_sym - 1 / q_sym) / 2}


def hopf_gluon(gen):
    """Build Hopf-link gluon element σᵢ² = HA·σᵢ + 𝟙."""
    return {(gen,): HA_sym, (): sp.Integer(1)}


def format_nf(nf_terms):
    """Format NF terms as a compact string."""
    parts = []
    for w, c in sorted(nf_terms.items(), key=lambda x: (len(x[0]), x[0])):
        v = eval_q0(c)
        name = pn(w)
        parts.append(f"{v:+.6f}·{name}")
    return " ".join(parts)


def nf_to_dict(nf_terms):
    """Convert NF terms to a serializable dict."""
    return {ws(w): eval_q0(c)
            for w, c in sorted(nf_terms.items(), key=lambda x: (len(x[0]), x[0]))}


# ══════════════════════════════════════════════════════════════
#  BUILD B₃
# ══════════════════════════════════════════════════════════════

sig0 = {(0,): sp.Integer(1)}
sig1 = {(1,): sp.Integer(1)}
sig1_inv = {(1,): sp.Integer(1), (): -HA_sym}
sig0_inv = {(0,): sp.Integer(1), (): -HA_sym}

unit_fwd = mul_terms(sig0, sig1_inv)
unit2_fwd = mul_terms(unit_fwd, unit_fwd)
nf_unit2_fwd, _, _ = reduce_nf(unit2_fwd, "unit²", verbose=False)
b3_raw = mul_terms(nf_unit2_fwd, unit_fwd)
nf_b3, net_b3, _ = reduce_nf(b3_raw, "B₃", verbose=False)

# ══════════════════════════════════════════════════════════════
#  MAIN ANALYSIS
# ══════════════════════════════════════════════════════════════

print("=" * 72)
print("  NUCLEON NF WITH EXPLICIT HOPF-LINK GLUONS")
print("=" * 72)
print(f"  q₀  = {q0:.10f}")
print(f"  HA  = q−q⁻¹ = {HA_num:.10f}")
print(f"  E₀  = {E0:.6f} MeV")
print(f"  mₚ  = {M_P_MEV:.6f} MeV")
print(f"  mₙ  = {M_N_MEV:.6f} MeV")
print(f"  net(B₃) = {net_b3:+.10f}")

results = {}

# ══════════════════════════════════════════════════════════════
#  PART 1: BASIC PARTICLE NF TABLE
# ══════════════════════════════════════════════════════════════

print("\n\n" + "=" * 72)
print("  PART 1: BASIC PARTICLE NF TABLE")
print("  (For appendix: NF of all fundamental particles)")
print("=" * 72)

basic_particles = {}

# ── Neutrino ν = 𝟙 ──
print("\n─── Neutrino ν = 𝟙 (identity/unknot) ───")
nf_nu = {(): sp.Integer(1)}
net_nu = 1.0
print(f"  NF(ν) = +1.0000000000 · 𝟏")
print(f"  net(ν) = +1.0000000000")
basic_particles["neutrino"] = {
    "symbol": "ν", "knot": "T₁₀ (unknot 0₁)",
    "hecke_word": "𝟙", "nf": {"𝟏": 1.0}, "net": 1.0,
}

# ── Photon γ = 𝟙 (same as ν topologically, distinguished by context) ──
print("\n─── Photon γ = 𝟙 (identity/point) ───")
basic_particles["photon"] = {
    "symbol": "γ", "knot": "∅ (point)",
    "hecke_word": "𝟙", "nf": {"𝟏": 1.0}, "net": 1.0,
    "note": "Same as ν in H₃(q); distinguished by bundle context",
}

# ── Hopf crossings σ₀ = σ₀, σ₁ = σ₁ ──
print("\n─── Hopf crossing σ₀ = σ₀ ───")
nf_h0, net_h0, _ = reduce_nf({(0,): sp.Integer(1)}, "σ₀ = σ₀")
basic_particles["hopf0"] = {
    "symbol": "σ₀", "knot": "virtual (ℓ=1)",
    "hecke_word": "σ₀", "nf": nf_to_dict(nf_h0), "net": net_h0,
}

print("\n─── Hopf crossing σ₁ = σ₁ ───")
nf_h1, net_h1, _ = reduce_nf({(1,): sp.Integer(1)}, "σ₁ = σ₁")
basic_particles["hopf1"] = {
    "symbol": "σ₁", "knot": "virtual (ℓ=1)",
    "hecke_word": "σ₁", "nf": nf_to_dict(nf_h1), "net": net_h1,
}

# ── Hopf links L₊ = σ₀σ₁, L₋ = σ₁σ₀ (GLUON) ──
print("\n─── Gluon L₊ = σ₀σ₁ (Hopf link) ───")
nf_lp, net_lp, _ = reduce_nf({(0, 1): sp.Integer(1)}, "L₊ = σ₀σ₁ (gluon)")
basic_particles["hopf_link_plus"] = {
    "symbol": "L₊ (gluon)", "knot": "Hopf link T(2,2)",
    "hecke_word": "σ₀σ₁", "nf": nf_to_dict(nf_lp), "net": net_lp,
}

print("\n─── Gluon L₋ = σ₁σ₀ (Hopf link) ───")
nf_lm, net_lm, _ = reduce_nf({(1, 0): sp.Integer(1)}, "L₋ = σ₁σ₀ (gluon)")
basic_particles["hopf_link_minus"] = {
    "symbol": "L₋ (gluon)", "knot": "Hopf link T(2,2)",
    "hecke_word": "σ₁σ₀", "nf": nf_to_dict(nf_lm), "net": net_lm,
}

# ── Hopf-squared σᵢ² = HA·σᵢ + 𝟙 ──
print("\n─── σ₀² = HA·σ₀ + 𝟙 (Hopf self-link) ───")
nf_s0sq, net_s0sq, _ = reduce_nf({(0, 0): sp.Integer(1)}, "σ₀²")
basic_particles["sigma0_sq"] = {
    "symbol": "σ₀²", "knot": "Hopf self-link (closure = Hopf link)",
    "hecke_word": "σ₀²", "nf": nf_to_dict(nf_s0sq), "net": net_s0sq,
    "expansion": "HA·σ₀ + 𝟙",
}

# ── Electron e⁻ = σ₀σ₁σ₀ (trefoil) ──
print("\n─── Electron e⁻ = σ₀σ₁σ₀ (trefoil 3₁) ───")
nf_em, net_em, _ = reduce_nf({(0, 1, 0): sp.Integer(1)}, "e⁻ = σ₀σ₁σ₀")
basic_particles["electron"] = {
    "symbol": "e⁻", "knot": "trefoil T₂₃ (3₁)",
    "hecke_word": "σ₀σ₁σ₀", "nf": nf_to_dict(nf_em), "net": net_em,
}

# ── Positron e⁺ = σ₀⁻¹σ₁⁻¹σ₀⁻¹ (mirror trefoil) ──
print("\n─── Positron e⁺ = σ₀⁻¹σ₁⁻¹σ₀⁻¹ (mirror trefoil) ───")
ep_expanded = expand_inverse_word((-1, -2, -1))
nf_ep, net_ep, _ = reduce_nf(ep_expanded, "e⁺ = σ₀⁻¹σ₁⁻¹σ₀⁻¹")
basic_particles["positron"] = {
    "symbol": "e⁺", "knot": "mirror trefoil T₂₃σ",
    "hecke_word": "σ₀⁻¹σ₁⁻¹σ₀⁻¹", "nf": nf_to_dict(nf_ep), "net": net_ep,
}

# ── Up quark 𝔲 = σ₀ (positive crossing in B₃) ──
print("\n─── Up quark 𝔲 = σ₀ (positive crossing orientation) ───")
nf_uq, net_uq, _ = reduce_nf({(0,): sp.Integer(1)}, "𝔲 = σ₀")
basic_particles["up_quark"] = {
    "symbol": "𝔲", "knot": "unknot T₁₀ (positive orientation in B₃)",
    "hecke_word": "σ₀", "nf": nf_to_dict(nf_uq), "net": net_uq,
    "crossing": "positive",
}

# ── Down quark 𝔡 = σ₀⁻¹ (negative crossing in B₃) ──
print("\n─── Down quark 𝔡 = σ₀⁻¹ (negative crossing orientation) ───")
d_expanded = expand_inverse_word((-1,))
nf_dq, net_dq, _ = reduce_nf(d_expanded, "𝔡 = σ₀⁻¹")
basic_particles["down_quark"] = {
    "symbol": "𝔡", "knot": "unknot T₁₀ (negative orientation in B₃)",
    "hecke_word": "σ₀⁻¹ = σ₀ − HA·𝟙", "nf": nf_to_dict(nf_dq), "net": net_dq,
    "crossing": "negative",
}

# ── B₃ = (σ₀σ₁⁻¹)³ gluon field ──
print("\n─── B₃ = (σ₀σ₁⁻¹)³ (Borromean confinement / gluon field) ───")
nf_b3_show, net_b3_show, _ = reduce_nf(b3_raw, "B₃ = (σ₀σ₁⁻¹)³")
basic_particles["B3_gluon_field"] = {
    "symbol": "B₃", "knot": "Borromean link B₃",
    "hecke_word": "(σ₀σ₁⁻¹)³",
    "nf": nf_to_dict(nf_b3_show), "net": net_b3_show,
    "role": "gluon field / color confinement",
}

results["basic_particles"] = basic_particles

# ══════════════════════════════════════════════════════════════
#  PART 2: NUCLEON NF WITH GLUON MODELS
# ══════════════════════════════════════════════════════════════

print("\n\n" + "=" * 72)
print("  PART 2: NUCLEON NF WITH MULTIPLE GLUON MODELS")
print("=" * 72)

print("""
  Gluon = Hopf link T(2,2).
  In H₃(q), σᵢ² = HA·σᵢ + 𝟙 is the Hopf self-link (closure = Hopf link).
  L₊ = σ₀σ₁ and L₋ = σ₁σ₀ are the Hopf link elements.

  Model A: nucleon = B₃ · crossings (NO gluons)
  Model B: nucleon = B₃ · [σᵢ² · cx(i,j)] per pair (Hopf gluon per pair)
  Model C: nucleon = B₃ · σ₀²·σ₁² · crossings (global Hopf dressing, 2 gluons)
  Model D: nucleon = B₃ · L₊ · crossings (single Hopf link element)
  Model E: nucleon = B₃ · L₊ · L₋ · crossings (Hopf pair, both orientations)
""")


def build_nucleon_model_A(types, label):
    """Model A: B₃ · crossings (no gluons)."""
    elem = dict(nf_b3)
    for i in range(3):
        for j in range(i + 1, 3):
            cx = crossing(types[i], types[j], i)
            product = mul_terms(elem, cx)
            elem, _, _ = reduce_nf(product, f"{label} cx({types[i]},{types[j]})",
                                   verbose=False)
    net = sum(eval_q0(c) for c in elem.values())
    return elem, net


def build_nucleon_model_B(types, label):
    """Model B: B₃ · [σᵢ²·cx(i,j)] per pair (Hopf gluon per pair)."""
    elem = dict(nf_b3)
    for i in range(3):
        for j in range(i + 1, 3):
            gen = i
            # Apply Hopf gluon σ_gen² = HA·σ_gen + 𝟙
            gluon = hopf_gluon(gen)
            product = mul_terms(elem, gluon)
            elem, _, _ = reduce_nf(product, f"{label} gluon({i},{j})",
                                   verbose=False)
            # Then apply flavor crossing
            cx = crossing(types[i], types[j], gen)
            product = mul_terms(elem, cx)
            elem, _, _ = reduce_nf(product, f"{label} cx({types[i]},{types[j]})",
                                   verbose=False)
    net = sum(eval_q0(c) for c in elem.values())
    return elem, net


def build_nucleon_model_C(types, label):
    """Model C: B₃ · σ₀²·σ₁² · crossings (global Hopf dressing)."""
    elem = dict(nf_b3)
    # Apply σ₀² = HA·σ₀ + 𝟙
    g0 = hopf_gluon(0)
    product = mul_terms(elem, g0)
    elem, _, _ = reduce_nf(product, f"{label} σ₀²", verbose=False)
    # Apply σ₁² = HA·σ₁ + 𝟙
    g1 = hopf_gluon(1)
    product = mul_terms(elem, g1)
    elem, _, _ = reduce_nf(product, f"{label} σ₁²", verbose=False)
    # Then crossings
    for i in range(3):
        for j in range(i + 1, 3):
            cx = crossing(types[i], types[j], i)
            product = mul_terms(elem, cx)
            elem, _, _ = reduce_nf(product, f"{label} cx({types[i]},{types[j]})",
                                   verbose=False)
    net = sum(eval_q0(c) for c in elem.values())
    return elem, net


def build_nucleon_model_D(types, label):
    """Model D: B₃ · L₊ · crossings (single Hopf link element)."""
    elem = dict(nf_b3)
    # Apply L₊ = σ₀σ₁
    lp = {(0, 1): sp.Integer(1)}
    product = mul_terms(elem, lp)
    elem, _, _ = reduce_nf(product, f"{label} L₊", verbose=False)
    # Then crossings
    for i in range(3):
        for j in range(i + 1, 3):
            cx = crossing(types[i], types[j], i)
            product = mul_terms(elem, cx)
            elem, _, _ = reduce_nf(product, f"{label} cx({types[i]},{types[j]})",
                                   verbose=False)
    net = sum(eval_q0(c) for c in elem.values())
    return elem, net


def build_nucleon_model_E(types, label):
    """Model E: B₃ · L₊ · L₋ · crossings (Hopf pair)."""
    elem = dict(nf_b3)
    # Apply L₊ = σ₀σ₁
    lp = {(0, 1): sp.Integer(1)}
    product = mul_terms(elem, lp)
    elem, _, _ = reduce_nf(product, f"{label} L₊", verbose=False)
    # Apply L₋ = σ₁σ₀
    lm = {(1, 0): sp.Integer(1)}
    product = mul_terms(elem, lm)
    elem, _, _ = reduce_nf(product, f"{label} L₋", verbose=False)
    # Then crossings
    for i in range(3):
        for j in range(i + 1, 3):
            cx = crossing(types[i], types[j], i)
            product = mul_terms(elem, cx)
            elem, _, _ = reduce_nf(product, f"{label} cx({types[i]},{types[j]})",
                                   verbose=False)
    net = sum(eval_q0(c) for c in elem.values())
    return elem, net


# Build all models for both proton and neutron
models = {
    "A (B₃ only)": build_nucleon_model_A,
    "B (Hopf/pair)": build_nucleon_model_B,
    "C (global σ²)": build_nucleon_model_C,
    "D (single L₊)": build_nucleon_model_D,
    "E (L₊·L₋)": build_nucleon_model_E,
}

model_results = {}

for model_name, build_fn in models.items():
    print(f"\n{'─' * 72}")
    print(f"  MODEL {model_name}")
    print(f"{'─' * 72}")

    nf_p, net_p = build_fn(['u', 'u', 'd'], f"proton {model_name}")
    nf_n, net_n = build_fn(['u', 'd', 'd'], f"neutron {model_name}")
    delta = net_n - net_p

    print(f"\n  Proton  [u,u,d]: net = {net_p:+.10f}")
    for w, c in sorted(nf_p.items(), key=lambda x: (len(x[0]), x[0])):
        v = eval_q0(c)
        print(f"    {v:+.10f} · {ws(w)}  [{pn(w)}]")

    print(f"\n  Neutron [u,d,d]: net = {net_n:+.10f}")
    for w, c in sorted(nf_n.items(), key=lambda x: (len(x[0]), x[0])):
        v = eval_q0(c)
        print(f"    {v:+.10f} · {ws(w)}  [{pn(w)}]")

    print(f"\n  Δ(n−p) = {delta:+.10f}")
    print(f"  Δ × E₀ = {delta * E0:.6f} MeV")
    print(f"  Q(CODATA) = −0.782333 MeV")
    if abs(delta) > 1e-15:
        print(f"  E₀ from this model = {-0.78233341 / delta:.6f} MeV")
    print()

    model_results[model_name] = {
        "proton": {
            "net": net_p,
            "n_terms": len(nf_p),
            "terms": nf_to_dict(nf_p),
        },
        "neutron": {
            "net": net_n,
            "n_terms": len(nf_n),
            "terms": nf_to_dict(nf_n),
        },
        "delta_net": delta,
        "delta_E_MeV": delta * E0,
        "E0_implied_MeV": -0.78233341 / delta if abs(delta) > 1e-15 else None,
    }

results["gluon_models"] = model_results

# ══════════════════════════════════════════════════════════════
#  PART 3: B₃ with duu vs uud (quark ordering effect)
# ══════════════════════════════════════════════════════════════

print("\n\n" + "=" * 72)
print("  PART 3: QUARK ORDERING EFFECT")
print("  B₃·[d,u,u] vs B₃·[u,u,d] and B₃#·[u,d,d] vs B₃·[u,d,d]")
print("=" * 72)

orderings = [
    ("B₃·[u,u,d]", ['u', 'u', 'd'], False, "proton (standard)"),
    ("B₃·[d,u,u]", ['d', 'u', 'u'], False, "proton (rotated)"),
    ("B₃·[u,d,u]", ['u', 'd', 'u'], False, "proton (mixed)"),
    ("B₃·[u,d,d]", ['u', 'd', 'd'], False, "neutron (standard)"),
    ("B₃·[d,d,u]", ['d', 'd', 'u'], False, "neutron (rotated)"),
    ("B₃·[d,u,d]", ['d', 'u', 'd'], False, "neutron (mixed)"),
]

# Also with gluons (Model B — per-pair Hopf gluon)
orderings_with_gluons = [
    ("B₃+g·[u,u,d]", ['u', 'u', 'd'], "proton+gluon"),
    ("B₃+g·[d,u,u]", ['d', 'u', 'u'], "proton+gluon (rotated)"),
    ("B₃+g·[u,d,d]", ['u', 'd', 'd'], "neutron+gluon"),
    ("B₃+g·[d,d,u]", ['d', 'd', 'u'], "neutron+gluon (rotated)"),
]

ordering_results = {}

for name, types, use_mirror, desc in orderings:
    nf_r, net_r = build_nucleon_model_A(types, name)
    print(f"  {name:<16s} ({desc}):  net = {net_r:+.10f}")
    ordering_results[name] = {"net": net_r, "terms": nf_to_dict(nf_r)}

print()
for name, types, desc in orderings_with_gluons:
    nf_r, net_r = build_nucleon_model_B(types, name)
    print(f"  {name:<18s} ({desc}):  net = {net_r:+.10f}")
    ordering_results[name] = {"net": net_r, "terms": nf_to_dict(nf_r)}

results["quark_orderings"] = ordering_results

# ══════════════════════════════════════════════════════════════
#  PART 4: KNOT OPERATION ACTIONS TABLE
# ══════════════════════════════════════════════════════════════

print("\n\n" + "=" * 72)
print("  PART 4: KNOT OPERATION ACTIONS TABLE")
print("  (Appendix: dictionary of all Hecke algebra operations)")
print("=" * 72)

operation_entries = []

# All basis products
basis = [
    ("𝟙", ()),
    ("σ₀", (0,)),
    ("σ₁", (1,)),
    ("σ₀σ₁ (L₊)", (0, 1)),
    ("σ₁σ₀ (L₋)", (1, 0)),
    ("σ₀σ₁σ₀ (e⁻)", (0, 1, 0)),
]

# Squared operations (Hecke relation)
squares = [
    ("σ₀²", (0, 0), "HA·σ₀ + 𝟙 (Hecke relation)"),
    ("σ₁²", (1, 1), "HA·σ₁ + 𝟙 (Hecke relation)"),
]

# Yang-Baxter
yb_ops = [
    ("σ₀σ₁σ₀ = σ₁σ₀σ₁", (0, 1, 0), "Yang-Baxter braid relation"),
]

# Inverse operations
inverses = [
    ("σ₀⁻¹", (-1,), "σ₀ − HA·𝟙 (Hecke inverse)"),
    ("σ₁⁻¹", (-2,), "σ₁ − HA·𝟙 (Hecke inverse)"),
]

# Borromean units
borromean = [
    ("σ₀σ₁⁻¹ (gluon unit)", None, "σ₀σ₁ − HA·σ₀ (one gluon exchange)"),
    ("(σ₀σ₁⁻¹)² (unit²)", None, "Intermediate Borromean"),
    ("(σ₀σ₁⁻¹)³ = B₃", None, "Borromean confinement"),
]

print("\n  ┌────────────────────────────────────────────────────────────────────┐")
print("  │  HECKE ALGEBRA H₃(q) OPERATION DICTIONARY                         │")
print("  ├────────────────────────────────────────────────────────────────────┤")
print(f"  │  q₀ = {q0:.10f},  HA = q−q⁻¹ = {HA_num:.10f}              │")
print("  ├────────────────────────────────────────────────────────────────────┤")

# Hecke relation
print("  │                                                                    │")
print("  │  FUNDAMENTAL RELATIONS:                                            │")
print(f"  │    σᵢ² = HA·σᵢ + 𝟙     (HA = {HA_num:.6f})                    │")
print("  │    σ₀σ₁σ₀ = σ₁σ₀σ₁     (Yang-Baxter)                            │")
print("  │    σᵢ⁻¹ = σᵢ − HA·𝟙    (Hecke inverse)                          │")
print("  │                                                                    │")
print("  ├────────────────────────────────────────────────────────────────────┤")
print("  │  PARTICLE ↔ KNOT ↔ HECKE WORD                                     │")
print("  ├──────────┬────────────┬───────────┬──────────┬─────────────────────┤")
print("  │ Particle │ Knot       │ Word      │ net(q₀)  │ Role               │")
print("  ├──────────┼────────────┼───────────┼──────────┼─────────────────────┤")

particle_rows = [
    ("ν", "unknot 0₁", "𝟙", 1.0, "Neutrino"),
    ("γ", "point ∅", "𝟙", 1.0, "Photon (= ν in H₃)"),
    ("σ₀", "virtual", "σ₀", net_h0, "Hopf crossing"),
    ("σ₁", "virtual", "σ₁", net_h1, "Hopf crossing"),
    ("L₊", "Hopf T(2,2)", "σ₀σ₁", net_lp, "Gluon (+)"),
    ("L₋", "Hopf T(2,2)", "σ₁σ₀", net_lm, "Gluon (−)"),
    ("e⁻", "trefoil 3₁", "σ₀σ₁σ₀", net_em, "Electron"),
    ("e⁺", "mirror 3₁", "σ₀⁻¹σ₁⁻¹σ₀⁻¹", net_ep, "Positron"),
    ("𝔲", "unknot (+)", "σ₀", net_uq, "Up quark"),
    ("𝔡", "unknot (−)", "σ₀⁻¹", net_dq, "Down quark"),
]

for sym, knot, word, net, role in particle_rows:
    print(f"  │ {sym:<8s} │ {knot:<10s} │ {word:<9s} │ {net:+.6f} │ {role:<19s} │")

print("  ├──────────┴────────────┴───────────┴──────────┴─────────────────────┤")
print("  │                                                                    │")
print("  │  COMPOSITE OPERATIONS:                                             │")
print("  ├────────────────────────────────────────────────────────────────────┤")

composite_ops = [
    ("σ₀²", (0, 0)),
    ("σ₁²", (1, 1)),
    ("σ₀σ₁²", (0, 1, 1)),
    ("σ₁σ₀²", (1, 0, 0)),
    ("σ₀²σ₁", (0, 0, 1)),
    ("σ₀σ₁σ₀σ₁", (0, 1, 0, 1)),
    ("σ₁σ₀σ₁σ₀", (1, 0, 1, 0)),
]

action_dict = {}
for label, word in composite_ops:
    nf, net, _ = reduce_nf({word: sp.Integer(1)}, label, verbose=False)
    parts = []
    for w, c in sorted(nf.items(), key=lambda x: (len(x[0]), x[0])):
        v = eval_q0(c)
        parts.append(f"{v:+.4f}·{pn(w)}")
    line = " ".join(parts)
    print(f"  │  {label:<14s} = {line:<50s} │")
    action_dict[label] = {"nf": nf_to_dict(nf), "net": net}

# Add inverse operations
for label, word in [("σ₀⁻¹", (-1,)), ("σ₁⁻¹", (-2,)),
                    ("σ₀⁻¹σ₁⁻¹", (-1, -2)), ("σ₁⁻¹σ₀⁻¹", (-2, -1)),
                    ("σ₀⁻¹σ₁⁻¹σ₀⁻¹", (-1, -2, -1))]:
    expanded = expand_inverse_word(word)
    nf, net, _ = reduce_nf(expanded, label, verbose=False)
    parts = []
    for w, c in sorted(nf.items(), key=lambda x: (len(x[0]), x[0])):
        v = eval_q0(c)
        parts.append(f"{v:+.4f}·{pn(w)}")
    line = " ".join(parts)
    print(f"  │  {label:<14s} = {line:<50s} │")
    action_dict[label] = {"nf": nf_to_dict(nf), "net": net}

print("  └────────────────────────────────────────────────────────────────────┘")

results["operation_dictionary"] = action_dict

# ══════════════════════════════════════════════════════════════
#  SUMMARY
# ══════════════════════════════════════════════════════════════

print("\n\n" + "=" * 72)
print("  SUMMARY: GLUON MODEL COMPARISON")
print("=" * 72)

print(f"\n  {'Model':<20s} {'net(p)':>12s} {'net(n)':>12s} {'Δ(n−p)':>12s} {'Δ×E₀ (MeV)':>12s} {'E₀ impl.':>10s}")
print("  " + "─" * 80)
for model_name, data in model_results.items():
    net_p = data["proton"]["net"]
    net_n = data["neutron"]["net"]
    delta = data["delta_net"]
    e0_impl = data["E0_implied_MeV"]
    e0_str = f"{e0_impl:.3f}" if e0_impl else "N/A"
    print(f"  {model_name:<20s} {net_p:+.10f} {net_n:+.10f} {delta:+.10f} {delta*E0:+.6f}  {e0_str:>10s}")

print(f"\n  CODATA reference: Q = −0.782333 MeV")
print(f"  E₀ (from beta-decay): {E0:.6f} MeV")

# Which model gives the best delta?
best_model = None
best_err = float('inf')
q_codata = -0.78233341
for name, data in model_results.items():
    delta_e = data["delta_net"] * E0
    err = abs(delta_e - q_codata)
    if err < best_err:
        best_err = err
        best_model = name

print(f"\n  Best match to CODATA Q-value: Model {best_model}")
print(f"  (residual = {best_err:.6f} MeV)")

# ══════════════════════════════════════════════════════════════
#  WITNESS JSON
# ══════════════════════════════════════════════════════════════

witness = {
    "name": "nucleon-with-gluons-nf",
    "description": (
        "Nucleon NF with explicit Hopf-link gluons. "
        "Part 1: Basic particle NF table (ν, γ, σ₀, σ₁, L₊, L₋, e⁻, e⁺, 𝔲, 𝔡, B₃). "
        "Part 2: Five gluon models compared (A: B₃ only, B: Hopf/pair, "
        "C: global σ², D: single L₊, E: L₊·L₋). "
        "Part 3: Quark ordering effects. "
        "Part 4: Knot operation actions dictionary."
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
    },
    # P2.5: see docs/audits/2026-05-02-p2-5-symbolic-q-audit.md
    "symbolic_q_form": {
        "engine": "sympy",
        "q_symbol": "q (sp.Symbol('q', positive=True))",
        "h_symbol_definition": "HA = q - 1/q",
        "z_symbol_definition": "z = 1 / (sqrt(q) + 1/sqrt(q))",
        "pattern": "sympy-symbolic-coefficients-evaluated-at-q0",
        "note": (
            "Per-NF coefficient polynomials in q are constructed "
            "symbolically; the numerical results below come from "
            ".subs(q_sym, q_0) evaluation."
        ),
    },
    "results": results,
}

out_path = Path(__file__).with_suffix(".witness.json")
out_path.write_text(json.dumps(witness, indent=2))
print(f"\n  Witness written to {out_path.name}")
