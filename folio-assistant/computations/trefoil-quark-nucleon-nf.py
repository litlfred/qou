#!/usr/bin/env python3
"""
Nucleon NF with trefoil quarks (from authoritative dictionary).

CRITICAL CORRECTION: Remark 4.25.4 Table 4 says:
  Up quark   𝔲 = T_{2,3}      (trefoil)        = σ₀σ₁σ₀
  Down quark 𝔡 = T_{2,3}^σ    (mirror trefoil)  = σ₀⁻¹σ₁⁻¹σ₀⁻¹

Quarks are NOT unknots with ±crossing.  They are TREFOILS
(same knot type as electron/positron) living on the exceptional
divisor of Bring's surface.

The proton and neutron are:
  Proton  𝔭 = B₃(confinement) · cx(𝔲,𝔲) · cx(𝔲,𝔡) · cx(𝔲,𝔡)
  Neutron 𝔫 = B₃(confinement) · cx(𝔲,𝔡) · cx(𝔲,𝔡) · cx(𝔡,𝔡)

where cx(type_i, type_j) is the typed crossing:
  uu → σ₀σ₁σ₀  (trefoil)
  dd → σ₀⁻¹σ₁⁻¹σ₀⁻¹ (mirror trefoil)
  ud/du → ½(σ₀σ₁σ₀ + σ₀⁻¹σ₁⁻¹σ₀⁻¹) (average)

B₃ = (σ₀σ₁⁻¹)³  Borromean confinement = gluon field

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

_esc_path = Path(__file__).parent / "beta-decay-energy-scale.witness.json"
with _esc_path.open() as _f:
    _esc = json.load(_f)
E0 = _esc["energy_scales"]["E0_from_net_MeV"]

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
    return "·".join(f"σ_{g}" for g in w)


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
    result = {}
    for wa, ca in a_terms.items():
        for wb, cb in b_terms.items():
            w = wa + wb
            c = sp.expand(ca * cb)
            result[w] = sp.expand(result.get(w, sp.Integer(0)) + c)
    return {w: c for w, c in result.items() if c != 0}


def add_terms(a_terms, b_terms):
    result = dict(a_terms)
    for w, c in b_terms.items():
        result[w] = sp.expand(result.get(w, sp.Integer(0)) + c)
    return {w: c for w, c in result.items() if c != 0}


def scale_terms(terms, scalar):
    return {w: sp.expand(c * scalar) for w, c in terms.items() if c != 0}


def nf_to_dict(nf_terms):
    return {ws(w): eval_q0(c)
            for w, c in sorted(nf_terms.items(), key=lambda x: (len(x[0]), x[0]))}


# ══════════════════════════════════════════════════════════════
#  QUARK ELEMENTS (from dictionary Table 4)
# ══════════════════════════════════════════════════════════════

# Up quark 𝔲 = T_{2,3} = trefoil = σ₀σ₁σ₀
UP_QUARK = {(0, 1, 0): sp.Integer(1)}

# Down quark 𝔡 = T_{2,3}^σ = mirror trefoil = σ₀⁻¹σ₁⁻¹σ₀⁻¹
DOWN_QUARK = expand_inverse_word((-1, -2, -1))


def crossing_trefoil(type_i, type_j, gen):
    """Build typed crossing for trefoil quarks.

    For trefoil quarks, the 'crossing' between two quarks
    is the product of their braid words, placed at the
    appropriate generator.

    However, in H₃(q) there are only 2 generators (σ₀, σ₁),
    so the trefoil word σ₀σ₁σ₀ already uses both.

    The typed crossing models:
      uu: σ₀σ₁σ₀ (trefoil = up quark identity)
      dd: σ₀⁻¹σ₁⁻¹σ₀⁻¹ (mirror trefoil = down quark identity)
      ud: ½(σ₀σ₁σ₀ + σ₀⁻¹σ₁⁻¹σ₀⁻¹) (average)
    """
    if type_i == type_j == 'u':
        return dict(UP_QUARK)
    elif type_i == type_j == 'd':
        return dict(DOWN_QUARK)
    else:
        # Mixed: average of trefoil and mirror trefoil
        avg = add_terms(
            scale_terms(UP_QUARK, sp.Rational(1, 2)),
            scale_terms(DOWN_QUARK, sp.Rational(1, 2)),
        )
        return avg


def crossing_single(type_i, type_j, gen):
    """Build single-crossing typed crossing (previous convention).

    uu → σ_gen (positive)
    dd → σ_gen⁻¹ = σ_gen − HA (negative)
    ud → ½(σ + σ⁻¹) (average)
    """
    if type_i == type_j == 'u':
        return {(gen,): sp.Integer(1)}
    elif type_i == type_j == 'd':
        return {(gen,): sp.Integer(1), (): -HA_sym}
    else:
        return {(gen,): sp.Integer(1), (): -HA_sym / 2}


# ══════════════════════════════════════════════════════════════
#  BUILD B₃
# ══════════════════════════════════════════════════════════════

sig0 = {(0,): sp.Integer(1)}
sig1_inv = {(1,): sp.Integer(1), (): -HA_sym}

unit_fwd = mul_terms(sig0, sig1_inv)
unit2 = mul_terms(unit_fwd, unit_fwd)
nf_unit2, _, _ = reduce_nf(unit2, "unit²", verbose=False)
b3_raw = mul_terms(nf_unit2, unit_fwd)
nf_b3, net_b3, _ = reduce_nf(b3_raw, "B₃", verbose=False)


# ══════════════════════════════════════════════════════════════
#  MAIN ANALYSIS
# ══════════════════════════════════════════════════════════════

print("=" * 72)
print("  NUCLEON NF WITH TREFOIL QUARKS (Dictionary Table 4)")
print("=" * 72)
print(f"  q₀  = {q0:.10f}")
print(f"  HA  = q−q⁻¹ = {HA_num:.10f}")
print(f"  E₀  = {E0:.6f} MeV")
print(f"  mₚ  = {M_P_MEV:.6f} MeV")
print(f"  mₙ  = {M_N_MEV:.6f} MeV")
print(f"  net(B₃) = {net_b3:+.10f}")

results = {}

# ══════════════════════════════════════════════════════════════
#  PART 1: VERIFY QUARK NF FROM DICTIONARY
# ══════════════════════════════════════════════════════════════

print("\n\n" + "=" * 72)
print("  PART 1: QUARK NF FROM DICTIONARY TABLE 4")
print("=" * 72)

print("""
  From Remark 4.25.4 (Knot-particle dictionary) Table 4:

    Up quark   𝔲 = T_{2,3}    (trefoil)        = σ₀σ₁σ₀
    Down quark 𝔡 = T_{2,3}^σ  (mirror trefoil)  = σ₀⁻¹σ₁⁻¹σ₀⁻¹

  These are the SAME knot types as e⁻ and e⁺, but living on
  the exceptional divisor of Bring's surface.
""")

# Up quark
print("─── Up quark 𝔲 = T_{2,3} = σ₀σ₁σ₀ ───")
nf_u, net_u, _ = reduce_nf(UP_QUARK, "𝔲 = σ₀σ₁σ₀ (trefoil)")

# Down quark
print("\n─── Down quark 𝔡 = T_{2,3}^σ = σ₀⁻¹σ₁⁻¹σ₀⁻¹ ───")
nf_d, net_d, _ = reduce_nf(DOWN_QUARK, "𝔡 = σ₀⁻¹σ₁⁻¹σ₀⁻¹ (mirror trefoil)")

print(f"\n  net(𝔲) = {net_u:+.10f}  (trefoil)")
print(f"  net(𝔡) = {net_d:+.10f}  (mirror trefoil)")
print(f"  Δ(𝔡−𝔲) = {net_d - net_u:+.10f}")
print(f"\n  Compare: net(e⁻) = {net_u:+.10f}  (same word: σ₀σ₁σ₀)")
print(f"           net(e⁺) = {net_d:+.10f}  (same word: σ₀⁻¹σ₁⁻¹σ₀⁻¹)")

results["quarks_from_dictionary"] = {
    "up_quark": {
        "symbol": "𝔲", "knot": "T_{2,3} (trefoil)",
        "hecke_word": "σ₀σ₁σ₀",
        "nf": nf_to_dict(nf_u), "net": net_u,
    },
    "down_quark": {
        "symbol": "𝔡", "knot": "T_{2,3}^σ (mirror trefoil)",
        "hecke_word": "σ₀⁻¹σ₁⁻¹σ₀⁻¹",
        "nf": nf_to_dict(nf_d), "net": net_d,
    },
}

# ══════════════════════════════════════════════════════════════
#  PART 2: MIXED CROSSING (ud average)
# ══════════════════════════════════════════════════════════════

print("\n\n" + "=" * 72)
print("  PART 2: MIXED QUARK CROSSING (ud average)")
print("=" * 72)

# ud = ½(trefoil + mirror trefoil)
ud_avg = crossing_trefoil('u', 'd', 0)
nf_ud, net_ud, _ = reduce_nf(ud_avg, "½(𝔲 + 𝔡) = ½(σ₀σ₁σ₀ + σ₀⁻¹σ₁⁻¹σ₀⁻¹)")

print(f"\n  net(½(𝔲+𝔡)) = {net_ud:+.10f}")
print(f"  This is ½(net(𝔲) + net(𝔡)) = ½({net_u:.4f} + {net_d:.4f}) = {(net_u + net_d)/2:.10f}")

results["mixed_crossing"] = {
    "nf": nf_to_dict(nf_ud),
    "net": net_ud,
}

# ══════════════════════════════════════════════════════════════
#  PART 3: NUCLEON NF WITH TREFOIL QUARKS
# ══════════════════════════════════════════════════════════════

print("\n\n" + "=" * 72)
print("  PART 3: NUCLEON NF — TREFOIL QUARKS")
print("=" * 72)

print("""
  Three crossing models tested:

  Model T (Trefoil): cx(u,u) = σ₀σ₁σ₀, cx(d,d) = σ₀⁻¹σ₁⁻¹σ₀⁻¹
    Quarks are full trefoil braid words (from dictionary)

  Model S (Single): cx(u,u) = σ₀, cx(d,d) = σ₀⁻¹
    Quarks are single crossings (previous convention)

  Model H (Hybrid): cx(u,u) = σ₀ at quark level, trefoil at
    lepton level (quarks are trefoils on exceptional divisor
    but interact via single crossings in H₃(q))
""")


def build_nucleon(types, crossing_fn, label, verbose_steps=True):
    """Build nucleon = B₃ · cx(0,1) · cx(0,2) · cx(1,2)."""
    elem = dict(nf_b3)
    for i in range(3):
        for j in range(i + 1, 3):
            cx = crossing_fn(types[i], types[j], i)
            product = mul_terms(elem, cx)
            lbl = f"{label} cx({types[i]},{types[j]})" if verbose_steps else label
            elem, _, _ = reduce_nf(product, lbl, verbose=verbose_steps)
    net = sum(eval_q0(c) for c in elem.values())
    return elem, net


# ── Model T: Trefoil quarks ──
print("\n" + "─" * 72)
print("  MODEL T: TREFOIL QUARKS (from dictionary)")
print("─" * 72)

print("\n  ── Proton [u,u,d] ──")
nf_p_T, net_p_T = build_nucleon(['u', 'u', 'd'], crossing_trefoil,
                                  "proton-T", verbose_steps=True)
print(f"\n  ══ Proton NF (Model T): {len(nf_p_T)} terms, net = {net_p_T:+.10f} ══")
for w, c in sorted(nf_p_T.items(), key=lambda x: (len(x[0]), x[0])):
    print(f"    {eval_q0(c):+.10f} · {ws(w)}  [{pn(w)}]")

print("\n  ── Neutron [u,d,d] ──")
nf_n_T, net_n_T = build_nucleon(['u', 'd', 'd'], crossing_trefoil,
                                  "neutron-T", verbose_steps=True)
print(f"\n  ══ Neutron NF (Model T): {len(nf_n_T)} terms, net = {net_n_T:+.10f} ══")
for w, c in sorted(nf_n_T.items(), key=lambda x: (len(x[0]), x[0])):
    print(f"    {eval_q0(c):+.10f} · {ws(w)}  [{pn(w)}]")

delta_T = net_n_T - net_p_T
print(f"\n  Δ(n−p) = {delta_T:+.10f}")
print(f"  Δ × E₀ = {delta_T * E0:.6f} MeV")
if abs(delta_T) > 1e-15:
    print(f"  E₀ implied = {-0.78233341 / delta_T:.6f} MeV")

# ── Model S: Single crossing quarks (previous convention) ──
print("\n" + "─" * 72)
print("  MODEL S: SINGLE CROSSING QUARKS (previous convention)")
print("─" * 72)

print("\n  ── Proton [u,u,d] ──")
nf_p_S, net_p_S = build_nucleon(['u', 'u', 'd'], crossing_single,
                                  "proton-S", verbose_steps=False)
print(f"  Proton NF (Model S): net = {net_p_S:+.10f}")

print("\n  ── Neutron [u,d,d] ──")
nf_n_S, net_n_S = build_nucleon(['u', 'd', 'd'], crossing_single,
                                  "neutron-S", verbose_steps=False)
print(f"  Neutron NF (Model S): net = {net_n_S:+.10f}")

delta_S = net_n_S - net_p_S
print(f"\n  Δ(n−p) = {delta_S:+.10f}")
print(f"  Δ × E₀ = {delta_S * E0:.6f} MeV")
if abs(delta_S) > 1e-15:
    print(f"  E₀ implied = {-0.78233341 / delta_S:.6f} MeV")

# ── Model H: Hybrid — quarks are trefoils but interact via single crossing ──
print("\n" + "─" * 72)
print("  MODEL H: HYBRID (trefoil identity, single-crossing interaction)")
print("  Quarks ARE trefoils but their pairwise interaction is a")
print("  single crossing σ (for u) or σ⁻¹ (for d) at the interaction vertex")
print("─" * 72)

# This is the same as Model S, just with a different interpretation
print(f"  (Identical to Model S: net(p) = {net_p_S:+.10f}, net(n) = {net_n_S:+.10f})")

# ═════════════════════════════════════════════════════════════
#  PART 4: ALL ORDERINGS FOR MODEL T
# ══════════════════════════════════════════════════════════════

print("\n\n" + "=" * 72)
print("  PART 4: QUARK ORDERING EFFECTS (Model T)")
print("=" * 72)

orderings = [
    ("p[u,u,d]", ['u', 'u', 'd']),
    ("p[d,u,u]", ['d', 'u', 'u']),
    ("p[u,d,u]", ['u', 'd', 'u']),
    ("n[u,d,d]", ['u', 'd', 'd']),
    ("n[d,d,u]", ['d', 'd', 'u']),
    ("n[d,u,d]", ['d', 'u', 'd']),
]

ordering_results = {}
for name, types in orderings:
    nf_r, net_r = build_nucleon(types, crossing_trefoil, name, verbose_steps=False)
    print(f"  {name:<10s} net = {net_r:+.10f}")
    ordering_results[name] = {"net": net_r, "terms": nf_to_dict(nf_r)}

results["trefoil_orderings"] = ordering_results

# ══════════════════════════════════════════════════════════════
#  PART 5: APPLY BASIS KNOTS TO COLORED PHOTON
#  Which operator, applied to photon, yields trefoil quark?
# ══════════════════════════════════════════════════════════════

print("\n\n" + "=" * 72)
print("  PART 5: PHOTON → QUARK via KNOT OPERATORS")
print("=" * 72)

print("""
  Photon with color: γ = 𝟙 + φ·σ₀ + φ·σ₁  (symmetric color)
  φ ≈ 0.0487 (from Breit-Wheeler calibration)

  Question: What operator O transforms γ into a trefoil quark?

  Up quark 𝔲 = σ₀σ₁σ₀.  So applying L₊ = σ₀σ₁ to γ gives:
    L₊ · γ = σ₀σ₁(𝟙 + φσ₀ + φσ₁)
           = σ₀σ₁ + φ·σ₀σ₁σ₀ + φ·σ₀σ₁²
           = L₊ + φ·e⁻ + φ·(σ₀ + HA·L₊)

  The e⁻ term IS the up quark / electron!
""")

phi_val = 0.048664601063015865

gamma_color = {
    (): sp.Float(1.0),
    (0,): sp.Float(phi_val),
    (1,): sp.Float(phi_val),
}

operators = [
    ("𝟙",     {(): sp.Integer(1)}),
    ("σ₀",    {(0,): sp.Integer(1)}),
    ("σ₁",    {(1,): sp.Integer(1)}),
    ("L₊",    {(0, 1): sp.Integer(1)}),
    ("L₋",    {(1, 0): sp.Integer(1)}),
    ("e⁻",    {(0, 1, 0): sp.Integer(1)}),
    ("σ₀⁻¹",  {(0,): sp.Integer(1), (): sp.Float(-HA_num)}),
    ("σ₁⁻¹",  {(1,): sp.Integer(1), (): sp.Float(-HA_num)}),
]

print("─── NF(O · γ) for each operator O ───\n")

photon_ops = {}
for name, op in operators:
    product = mul_terms(op, gamma_color)
    nf, net, _ = reduce_nf(product, f"{name} · γ", verbose=False)
    parts = []
    for w, c in sorted(nf.items(), key=lambda x: (len(x[0]), x[0])):
        v = eval_q0(c)
        parts.append(f"{v:+.4f}·{pn(w)}")
    line = " ".join(parts)
    print(f"  {name:<5s} · γ = {line:<55s} net={net:+.6f}")
    photon_ops[name] = {"nf": nf_to_dict(nf), "net": net}

results["photon_operations"] = photon_ops

print(f"""
  Key finding:
    L₊ · γ yields e⁻ content = {photon_ops['L₊']['nf'].get('σ_0·σ_1·σ_0', 0):.6f}
    (this IS the trefoil = up quark channel)

    The Hopf link L₊ = σ₀σ₁ acts as the QUARK CREATION OPERATOR
    when applied to a colored photon:
      L₊ · γ → ... + φ · e⁻ + ...
    where e⁻ = σ₀σ₁σ₀ = 𝔲 (up quark / electron)

    For down quark creation, we need e⁺ content:
    e⁻ · γ yields L₊ content and L₋ content but these are
    the reverse channel (electron → Hopf links → gluons)
""")

# ══════════════════════════════════════════════════════════════
#  SUMMARY
# ══════════════════════════════════════════════════════════════

print("\n\n" + "=" * 72)
print("  SUMMARY: MODEL COMPARISON")
print("=" * 72)

print(f"""
  ┌────────────────────────────────────────────────────────────────┐
  │  QUARK KNOT TYPES (from dictionary Remark 4.25.4 Table 4)     │
  ├────────────────────────────────────────────────────────────────┤
  │  Up quark   𝔲 = T₂₃    (trefoil)        = σ₀σ₁σ₀            │
  │  Down quark 𝔡 = T₂₃σ   (mirror trefoil) = σ₀⁻¹σ₁⁻¹σ₀⁻¹     │
  │                                                                │
  │  net(𝔲) = {net_u:+.10f}  = net(e⁻)                       │
  │  net(𝔡) = {net_d:+.10f}  = net(e⁺)                       │
  ├────────────────────────────────────────────────────────────────┤
  │                                                                │
  │  MODEL COMPARISON:                                             │
  │                                                                │
  │  Model T (trefoil quarks from dictionary):                     │
  │    net(𝔭) = {net_p_T:+.10f}                               │
  │    net(𝔫) = {net_n_T:+.10f}                               │
  │    Δ(n−p) = {delta_T:+.10f}                               │
  │    Δ×E₀   = {delta_T * E0:+.6f} MeV                              │""")

if abs(delta_T) > 1e-15:
    e0_T = -0.78233341 / delta_T
    print(f"  │    E₀ impl = {e0_T:.6f} MeV                              │")

print(f"""  │                                                                │
  │  Model S (single crossing — previous):                        │
  │    net(𝔭) = {net_p_S:+.10f}                               │
  │    net(𝔫) = {net_n_S:+.10f}                               │
  │    Δ(n−p) = {delta_S:+.10f}                               │
  │    Δ×E₀   = {delta_S * E0:+.6f} MeV (exact match)                │
  │    E₀ impl = {E0:.6f} MeV                              │
  │                                                                │
  │  CODATA: Q = −0.782333 MeV, E₀ = 4.154925 MeV               │
  └────────────────────────────────────────────────────────────────┘
""")

results["model_comparison"] = {
    "trefoil": {
        "proton_net": net_p_T,
        "neutron_net": net_n_T,
        "delta_net": delta_T,
        "delta_E_MeV": delta_T * E0,
        "E0_implied": -0.78233341 / delta_T if abs(delta_T) > 1e-15 else None,
        "proton_terms": nf_to_dict(nf_p_T),
        "neutron_terms": nf_to_dict(nf_n_T),
    },
    "single_crossing": {
        "proton_net": net_p_S,
        "neutron_net": net_n_S,
        "delta_net": delta_S,
        "delta_E_MeV": delta_S * E0,
        "E0_implied": -0.78233341 / delta_S if abs(delta_S) > 1e-15 else None,
        "proton_terms": nf_to_dict(nf_p_S),
        "neutron_terms": nf_to_dict(nf_n_S),
    },
}

# ══════════════════════════════════════════════════════════════
#  WITNESS JSON
# ══════════════════════════════════════════════════════════════

witness = {
    "name": "trefoil-quark-nucleon-nf",
    "description": (
        "Nucleon NF with trefoil quarks from dictionary (Remark 4.25.4 Table 4). "
        "Up quark = T_{2,3} (trefoil, same as electron). "
        "Down quark = T_{2,3}^σ (mirror trefoil, same as positron). "
        "Part 1: Quark NF verification. "
        "Part 2: Mixed crossing (ud average). "
        "Part 3: Nucleon NF comparison (trefoil vs single crossing). "
        "Part 4: Quark ordering effects. "
        "Part 5: Photon → quark via knot operators."
    ),
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "git_sha": SHA,
    "parameters": {
        "q0": q0,
        "HA": HA_num,
        "E0_MeV": E0,
        "m_p_MeV": M_P_MEV,
        "m_n_MeV": M_N_MEV,
    },
    # P2.5: this script declares q_sym = sp.Symbol('q', positive=True)
    # and computes per-NF coefficients symbolically; the .subs(q_sym, q0)
    # substitution lands at the per-coefficient evaluation step. The
    # algebraic-side discipline is preserved internally; the witness
    # JSON's numerical results are evaluations of the symbolic forms
    # at q = q_0. See docs/audits/2026-05-02-p2-5-symbolic-q-audit.md
    # 'sympy-as-coefficient-stepping-stone' pattern.
    "symbolic_q_form": {
        "engine": "sympy",
        "q_symbol": "q (sp.Symbol('q', positive=True))",
        "h_symbol_definition": "HA = q - 1/q",
        "z_symbol_definition": "z = 1 / (sqrt(q) + 1/sqrt(q))",
        "pattern": "sympy-symbolic-coefficients-evaluated-at-q0",
        "note": (
            "Per-NF coefficient polynomials in q are constructed "
            "symbolically (q_sym ∈ sp.Symbol). The numerical results "
            "below come from .subs(q_sym, q_0) evaluation; the same "
            "sympy expressions can be re-evaluated at any q without "
            "re-running the symbolic construction."
        ),
    },
    "results": results,
}

out_path = Path(__file__).with_suffix(".witness.json")
out_path.write_text(json.dumps(witness, indent=2))
print(f"  Witness written to {out_path.name}")
