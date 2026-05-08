#!/usr/bin/env python3
"""
Meson and nucleon construction via Hecke algebra normal forms.

STEP 1: Meson = quark + antiquark
  Proposed:  M₊ = T_01 · H_L · T_10   (quark · binding · antiquark)
             M₋ = T_10 · H_L · T_01   (antiquark · binding · quark)
  Where:
    T_01 = σ₀σ₁  (positive crossing pair = L₊ = Hopf link)
    T_10 = σ₁σ₀  (reversed crossing pair = L₋ = Hopf link)
    H_L  = σ₀σ₁  (Hopf link binding)

STEP 2: Quark definition options
  Option A: B₃(T_01, T_01, T_10)  — using Borromean braid
  Option B: T₂₉(T_01, T_01, T_10) — using T(2,9) torus knot
  Where B₃ = (σ₀σ₁⁻¹)³ and T₂₉ = (σ₀σ₁)⁹/² (half-turn torus knot)

STEP 3: Nucleon from meson + quark
  Path A: Meson · H_L · T_01    (or T_10)
  Path B: Meson · T₂₉ · T_01   (or T_10)
  Path C: Meson · B₃            (Borromean confinement)

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

from q_parameter import Q as q0, Q_INV as qi0, HA as HA0
from experimental_constants import M_P_MEV, M_N_MEV, M_E_MEV

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

# ── Iwahori--Hecke algebra ────────────────────────────────────
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
#  GRÖBNER--SHIRSHOV REDUCTION (same as breit-wheeler-nucleon-nf)
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
            continue
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


def nf_summary(nf_terms, label):
    """Return dict summary of NF for witness."""
    return {
        "label": label,
        "n_terms": len(nf_terms),
        "net": sum(eval_q0(c) for c in nf_terms.values()),
        "terms": {
            ws(w): eval_q0(c)
            for w, c in sorted(nf_terms.items(), key=lambda x: (len(x[0]), x[0]))
        },
        "particle_content": {
            pn(w): eval_q0(c)
            for w, c in sorted(nf_terms.items(), key=lambda x: (len(x[0]), x[0]))
            if pn(w) != "?"
        },
    }


# ══════════════════════════════════════════════════════════════
#  MAIN ANALYSIS
# ══════════════════════════════════════════════════════════════

print("=" * 72)
print("  MESON & NUCLEON CONSTRUCTION NF ANALYSIS")
print("=" * 72)
print(f"  q₀  = {q0:.10f}")
print(f"  HA  = q−q⁻¹ = {HA_num:.10f}")
print(f"  E₀  = {E0:.6f} MeV")

results = {}

# ── Building blocks ──────────────────────────────────────────

sig0 = {(0,): sp.Integer(1)}
sig1 = {(1,): sp.Integer(1)}
sig1_inv = {(1,): sp.Integer(1), (): -HA_sym}
sig0_inv = {(0,): sp.Integer(1), (): -HA_sym}

# T_01 = σ₀σ₁ (= L₊, Hopf link positive)
T_01 = mul_terms(sig0, sig1)
# T_10 = σ₁σ₀ (= L₋, Hopf link negative)
T_10 = mul_terms(sig1, sig0)
# H_L = Hopf link = σ₀σ₁ (same as T_01)
H_L = dict(T_01)

print("\n  Building blocks:")
print(f"    T_01 = σ₀σ₁ = L₊")
print(f"    T_10 = σ₁σ₀ = L₋")
print(f"    H_L  = σ₀σ₁ (Hopf link binding)")


# ══════════════════════════════════════════════════════════════
#  STEP 1: MESON NORMAL FORMS
# ══════════════════════════════════════════════════════════════

print("\n\n" + "=" * 72)
print("  STEP 1: MESON NORMAL FORMS")
print("  Meson = quark · binding · antiquark")
print("=" * 72)

# 1a: M₊ = T_01 · H_L · T_10 = σ₀σ₁ · σ₀σ₁ · σ₁σ₀
print("\n─── 1a: M₊ = T_01 · H_L · T_10 = σ₀σ₁ · σ₀σ₁ · σ₁σ₀ ───")
meson_plus_raw = mul_terms(mul_terms(T_01, H_L), T_10)
nf_meson_plus, net_meson_plus, steps_mp = reduce_nf(
    meson_plus_raw, "M₊ = T_01·H_L·T_10 = (σ₀σ₁)²·σ₁σ₀"
)

# 1b: M₋ = T_10 · H_L · T_01 = σ₁σ₀ · σ₀σ₁ · σ₀σ₁
print("\n─── 1b: M₋ = T_10 · H_L · T_01 = σ₁σ₀ · σ₀σ₁ · σ₀σ₁ ───")
meson_minus_raw = mul_terms(mul_terms(T_10, H_L), T_01)
nf_meson_minus, net_meson_minus, steps_mm = reduce_nf(
    meson_minus_raw, "M₋ = T_10·H_L·T_01 = σ₁σ₀·(σ₀σ₁)²"
)

# 1c: Alternative — H_L as separate binding: T_01 · T_10 (no binding)
print("\n─── 1c: T_01 · T_10 = σ₀σ₁ · σ₁σ₀ (no binding, check) ───")
bare_pair = mul_terms(T_01, T_10)
nf_bare, net_bare, _ = reduce_nf(bare_pair, "σ₀σ₁·σ₁σ₀ (bare pair)")

# 1d: T_10 · T_01 = σ₁σ₀ · σ₀σ₁
print("\n─── 1d: T_10 · T_01 = σ₁σ₀ · σ₀σ₁ ───")
bare_pair_rev = mul_terms(T_10, T_01)
nf_bare_rev, net_bare_rev, _ = reduce_nf(bare_pair_rev, "σ₁σ₀·σ₀σ₁ (reversed)")

results["step1"] = {
    "meson_plus": nf_summary(nf_meson_plus, "M₊ = T_01·H_L·T_10"),
    "meson_minus": nf_summary(nf_meson_minus, "M₋ = T_10·H_L·T_01"),
    "bare_pair": nf_summary(nf_bare, "T_01·T_10 (no binding)"),
    "bare_pair_rev": nf_summary(nf_bare_rev, "T_10·T_01 (reversed)"),
}

print("\n  ── MESON SUMMARY ──")
print(f"  M₊ = T_01·H_L·T_10: net = {net_meson_plus:+.10f}, {len(nf_meson_plus)} terms")
print(f"  M₋ = T_10·H_L·T_01: net = {net_meson_minus:+.10f}, {len(nf_meson_minus)} terms")
print(f"  bare T_01·T_10:      net = {net_bare:+.10f}, {len(nf_bare)} terms")
print(f"  bare T_10·T_01:      net = {net_bare_rev:+.10f}, {len(nf_bare_rev)} terms")


# ══════════════════════════════════════════════════════════════
#  STEP 2: QUARK COMPOSITION OPTIONS — B₃ vs T(2,9)
# ══════════════════════════════════════════════════════════════

print("\n\n" + "=" * 72)
print("  STEP 2: QUARK COMPOSITION OPTIONS")
print("  B₃(T_01, T_01, T_10) vs T₂₉(T_01, T_01, T_10)")
print("=" * 72)

# 2a: Borromean B₃ = (σ₀σ₁⁻¹)³
print("\n─── 2a: B₃ = (σ₀σ₁⁻¹)³ ───")
unit = mul_terms(sig0, sig1_inv)
unit2_raw = mul_terms(unit, unit)
nf_unit2, _, _ = reduce_nf(unit2_raw, "unit² = (σ₀σ₁⁻¹)²")
b3_raw = mul_terms(nf_unit2, unit)
nf_b3, net_b3, steps_b3 = reduce_nf(b3_raw, "B₃ = (σ₀σ₁⁻¹)³")

# B₃ braid word (unreduced): σ₀σ₁⁻¹σ₀σ₁⁻¹σ₀σ₁⁻¹
print(f"\n  B₃ braid word: (σ₀σ₁⁻¹)³ = σ₀·σ₁⁻¹·σ₀·σ₁⁻¹·σ₀·σ₁⁻¹")
print(f"  B₃ net = {net_b3:+.10f}")

# 2b: T(2,9) torus knot — braid word is (σ₀σ₁)⁴·σ₀ (for T(2,9) on 2 strands)
# Actually T(2,n) on braid group B_2 is σ₁^n. On B_3 with two generators:
# T(2,9) as alternating: (σ₀σ₁)⁴·σ₀ = σ₀σ₁σ₀σ₁σ₀σ₁σ₀σ₁σ₀
print("\n─── 2b: T(2,9) torus knot = (σ₀σ₁)⁴·σ₀ = alternating 9 crossings ───")
t29_word = (0, 1, 0, 1, 0, 1, 0, 1, 0)  # 9 alternating generators
t29_raw = {t29_word: sp.Integer(1)}
nf_t29, net_t29, steps_t29 = reduce_nf(t29_raw, "T(2,9) = (σ₀σ₁)⁴σ₀")

print(f"\n  T(2,9) braid word: σ₀σ₁σ₀σ₁σ₀σ₁σ₀σ₁σ₀ (9 crossings)")
print(f"  T(2,9) net = {net_t29:+.10f}")

# 2c: T(2,3) torus knot (trefoil) for reference
print("\n─── 2c: T(2,3) trefoil = σ₀σ₁σ₀ (3 crossings, for reference) ───")
t23_raw = {(0, 1, 0): sp.Integer(1)}
nf_t23, net_t23, _ = reduce_nf(t23_raw, "T(2,3) = σ₀σ₁σ₀")

# 2d: Compare the "quark compositions"
# Option A: B₃(uud) = B₃ · T_01 · T_01 · T_10 (concatenation)
print("\n─── 2d: Option A — B₃ · T_01 · T_01 · T_10 ───")
optA_raw = mul_terms(mul_terms(mul_terms(nf_b3, T_01), T_01), T_10)
nf_optA, net_optA, _ = reduce_nf(optA_raw, "B₃·T_01·T_01·T_10")

# Option B: T₂₉ · T_01 · T_01 · T_10
print("\n─── 2e: Option B — T₂₉ · T_01 · T_01 · T_10 ───")
optB_raw = mul_terms(mul_terms(mul_terms(nf_t29, T_01), T_01), T_10)
nf_optB, net_optB, _ = reduce_nf(optB_raw, "T₂₉·T_01·T_01·T_10")

# Mirror versions for neutron-like (ddu)
print("\n─── 2f: Option A (mirror) — B₃ · T_10 · T_10 · T_01 ───")
optA_mirror_raw = mul_terms(mul_terms(mul_terms(nf_b3, T_10), T_10), T_01)
nf_optA_m, net_optA_m, _ = reduce_nf(optA_mirror_raw, "B₃·T_10·T_10·T_01")

print("\n─── 2g: Option B (mirror) — T₂₉ · T_10 · T_10 · T_01 ───")
optB_mirror_raw = mul_terms(mul_terms(mul_terms(nf_t29, T_10), T_10), T_01)
nf_optB_m, net_optB_m, _ = reduce_nf(optB_mirror_raw, "T₂₉·T_10·T_10·T_01")

results["step2"] = {
    "B3": nf_summary(nf_b3, "B₃ = (σ₀σ₁⁻¹)³"),
    "T29": nf_summary(nf_t29, "T(2,9) = (σ₀σ₁)⁴σ₀"),
    "T23": nf_summary(nf_t23, "T(2,3) = σ₀σ₁σ₀"),
    "option_A_uud": nf_summary(nf_optA, "B₃·T_01·T_01·T_10 (proton-like)"),
    "option_B_uud": nf_summary(nf_optB, "T₂₉·T_01·T_01·T_10 (proton-like)"),
    "option_A_ddu": nf_summary(nf_optA_m, "B₃·T_10·T_10·T_01 (neutron-like)"),
    "option_B_ddu": nf_summary(nf_optB_m, "T₂₉·T_10·T_10·T_01 (neutron-like)"),
}

print("\n  ── QUARK COMPOSITION SUMMARY ──")
print(f"  B₃ alone:                  net = {net_b3:+.10f}")
print(f"  T(2,9) alone:              net = {net_t29:+.10f}")
print(f"  T(2,3) trefoil:            net = {net_t23:+.10f}")
print(f"  B₃·T_01·T_01·T_10 (uud):  net = {net_optA:+.10f}")
print(f"  T₂₉·T_01·T_01·T_10 (uud): net = {net_optB:+.10f}")
print(f"  B₃·T_10·T_10·T_01 (ddu):  net = {net_optA_m:+.10f}")
print(f"  T₂₉·T_10·T_10·T_01 (ddu): net = {net_optB_m:+.10f}")

# Compare to known nucleon nets from beta-decay-energy-scale
print(f"\n  Reference (from beta-decay-energy-scale):")
print(f"    net(proton)  = +0.9991251252")
print(f"    net(neutron) = +0.8108345052")
print(f"    Δnet         = -0.1882906200")


# ══════════════════════════════════════════════════════════════
#  STEP 3: NUCLEON FROM MESON + QUARK
# ══════════════════════════════════════════════════════════════

print("\n\n" + "=" * 72)
print("  STEP 3: NUCLEON FROM MESON + QUARK")
print("  Using M₊ = T_01·H_L·T_10 as the meson")
print("=" * 72)

# 3a: Meson · H_L · T_01 (proton-like: meson + up quark via Hopf binding)
print("\n─── 3a: M₊ · H_L · T_01 (meson + up via Hopf) ───")
n3a_raw = mul_terms(mul_terms(nf_meson_plus, H_L), T_01)
nf_3a, net_3a, _ = reduce_nf(n3a_raw, "M₊·H_L·T_01")

# 3b: Meson · H_L · T_10 (meson + down quark via Hopf binding)
print("\n─── 3b: M₊ · H_L · T_10 (meson + down via Hopf) ───")
n3b_raw = mul_terms(mul_terms(nf_meson_plus, H_L), T_10)
nf_3b, net_3b, _ = reduce_nf(n3b_raw, "M₊·H_L·T_10")

# 3c: Meson · T₂₉ · T_01 (meson + up via T(2,9) binding)
print("\n─── 3c: M₊ · T₂₉ · T_01 (meson + up via T(2,9)) ───")
n3c_raw = mul_terms(mul_terms(nf_meson_plus, nf_t29), T_01)
nf_3c, net_3c, _ = reduce_nf(n3c_raw, "M₊·T₂₉·T_01")

# 3d: Meson · T₂₉ · T_10 (meson + down via T(2,9) binding)
print("\n─── 3d: M₊ · T₂₉ · T_10 (meson + down via T(2,9)) ───")
n3d_raw = mul_terms(mul_terms(nf_meson_plus, nf_t29), T_10)
nf_3d, net_3d, _ = reduce_nf(n3d_raw, "M₊·T₂₉·T_10")

# 3e: Meson · B₃ (Borromean confinement of meson)
print("\n─── 3e: M₊ · B₃ (meson + Borromean confinement) ───")
n3e_raw = mul_terms(nf_meson_plus, nf_b3)
nf_3e, net_3e, _ = reduce_nf(n3e_raw, "M₊·B₃")

# 3f: B₃ · Meson (Borromean first, then meson content)
print("\n─── 3f: B₃ · M₊ (Borromean first, then meson) ───")
n3f_raw = mul_terms(nf_b3, nf_meson_plus)
nf_3f, net_3f, _ = reduce_nf(n3f_raw, "B₃·M₊")

results["step3"] = {
    "meson_HL_up": nf_summary(nf_3a, "M₊·H_L·T_01"),
    "meson_HL_down": nf_summary(nf_3b, "M₊·H_L·T_10"),
    "meson_T29_up": nf_summary(nf_3c, "M₊·T₂₉·T_01"),
    "meson_T29_down": nf_summary(nf_3d, "M₊·T₂₉·T_10"),
    "meson_B3": nf_summary(nf_3e, "M₊·B₃"),
    "B3_meson": nf_summary(nf_3f, "B₃·M₊"),
}

print("\n  ── NUCLEON CONSTRUCTION SUMMARY ──")
print(f"  M₊·H_L·T_01  (meson + u via Hopf):    net = {net_3a:+.10f}")
print(f"  M₊·H_L·T_10  (meson + d via Hopf):    net = {net_3b:+.10f}")
print(f"  M₊·T₂₉·T_01  (meson + u via T(2,9)):  net = {net_3c:+.10f}")
print(f"  M₊·T₂₉·T_10  (meson + d via T(2,9)):  net = {net_3d:+.10f}")
print(f"  M₊·B₃         (meson + Borromean):     net = {net_3e:+.10f}")
print(f"  B₃·M₊         (Borromean + meson):     net = {net_3f:+.10f}")
print(f"\n  Reference targets:")
print(f"    net(proton)  = +0.9991251252")
print(f"    net(neutron) = +0.8108345052")

# ── Closeness analysis ──
print("\n  ── CLOSENESS TO CODATA NUCLEON NETS ──")
target_p = 0.9991251252
target_n = 0.8108345052
candidates = [
    ("M₊·H_L·T_01", net_3a),
    ("M₊·H_L·T_10", net_3b),
    ("M₊·T₂₉·T_01", net_3c),
    ("M₊·T₂₉·T_10", net_3d),
    ("M₊·B₃", net_3e),
    ("B₃·M₊", net_3f),
    ("B₃·T_01·T_01·T_10 (opt A)", net_optA),
    ("T₂₉·T_01·T_01·T_10 (opt B)", net_optB),
    ("B₃·T_10·T_10·T_01 (opt A mirror)", net_optA_m),
    ("T₂₉·T_10·T_10·T_01 (opt B mirror)", net_optB_m),
]

print(f"\n  {'Construction':<42s}  {'net':>12s}  {'Δ(proton)':>12s}  {'Δ(neutron)':>12s}")
print(f"  {'-'*42}  {'-'*12}  {'-'*12}  {'-'*12}")
for name, net_val in candidates:
    dp = net_val - target_p
    dn = net_val - target_n
    print(f"  {name:<42s}  {net_val:+12.8f}  {dp:+12.8f}  {dn:+12.8f}")


# ══════════════════════════════════════════════════════════════
#  WRITE WITNESS
# ══════════════════════════════════════════════════════════════

witness = {
    "computation": "meson-nucleon-nf",
    "description": "Meson and nucleon construction via Hecke algebra normal forms",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "git_sha": SHA,
    "parameters": {
        "q": q0,
        "HA": HA_num,
        "E0_MeV": E0,
    },
    "building_blocks": {
        "T_01": "σ₀σ₁ (= L₊, Hopf link positive)",
        "T_10": "σ₁σ₀ (= L₋, Hopf link negative)",
        "H_L": "σ₀σ₁ (Hopf link binding, same as T_01)",
        "B3": "(σ₀σ₁⁻¹)³ (Borromean braid)",
        "T29": "(σ₀σ₁)⁴σ₀ (torus knot T(2,9), 9 crossings)",
    },
    "step1_meson": results["step1"],
    "step2_quark_composition": results["step2"],
    "step3_nucleon_construction": results["step3"],
    "reference_nets": {
        "proton": target_p,
        "neutron": target_n,
        "delta_net": target_n - target_p,
    },
}

witness_path = Path(__file__).parent / "meson-nucleon-nf.witness.json"
with witness_path.open("w") as f:
    json.dump(witness, f, indent=2, default=str)
print(f"\n  Witness written to {witness_path.name}")

print("\n" + "=" * 72)
print("  ANALYSIS COMPLETE")
print("=" * 72)
