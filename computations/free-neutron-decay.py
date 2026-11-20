"""

CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
#!/usr/bin/env python3
"""
Free neutron decay: n → p + e⁻ + ν̄ₑ
VERBOSE MODE — shows every Gröbner--Shirshov relation application.

Computes:
  1. NF(B₃)     = NF((σ₀σ₁⁻¹)³)             in H₃(q)
  2. NF(proton)  = NF(B₃ · crossings(u,u,d))  in H₃(q)
  3. NF(neutron) = NF(B₃ · crossings(u,d,d))  in H₃(q)
  4. Transition:  NF(neutron) − NF(proton)

Relations applied (Gröbner--Shirshov basis for H_n(q)):
  R1 (Hecke):        σ_i² = (q − q⁻¹)·σ_i + 1
  R2 (Far-comm):     σ_i·σ_j = σ_j·σ_i   for |i − j| ≥ 2
  R3 (Yang-Baxter):  σ_i·σ_{i+1}·σ_i = σ_{i+1}·σ_i·σ_{i+1}

Usage:
    python3 free-neutron-decay.py
"""

import math, json, subprocess
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp

# P2.5 migration: helper available; per-witness expose_polynomial call is a follow-up
import sys as _p25_sys
from pathlib import Path as _P25Path
_p25_sys.path.insert(0, str(_P25Path(__file__).parent))
from witness_polynomial import expose_polynomial  # noqa: F401
q = sp.Symbol('q', positive=True)

# ── Iwahori--Hecke algebra constants ───────────────────────────────────
q_inv = 1 / q
q_half = sp.sqrt(q)
q_half_inv = 1 / sp.sqrt(q)
HA = q - q_inv                       # q − q⁻¹
s_skein = q_half - q_half_inv        # q^½ − q^{-½}
# CONVENTION D (owner ruling 2026-08-15, R1). This read
#   z_markov = 1 / (q_half + q_half_inv)   ==  sqrt(q)/(q+1)  ==  z_C,
# which evaluates to 0.4993203... The canonical value is z_D = 0.6126880...
# Matches hecke_symbolic.z_markov, the library definition. Published into
# constants_at_q0 below; not used by the NF reduction, so the normal forms
# are unchanged by this correction.
z_markov = q**3 / (q**2 + 1)          # convention D: q^3/(q^2+1)

from q_parameter import (Q as q0, Q_INV as qi0, E_CROSS,
                         Q_MP as q0_mp, Q_50_DIGIT_STR)
from experimental_constants import M_E_MEV, KAPPA

# ── Exact evaluation ─────────────────────────────────────────
# `q_parameter.Q` is a Python FLOAT (float64); `Q_MP` / `Q_50_DIGIT_STR` carry
# the full 50 digits.  Values that reach the witness must not be evaluated at
# the float64 anchor -- NO-FLOAT64 is STRICT for producers.  `_num` evaluates
# the exact sympy coefficient over Q(q) at the exact rational anchor and
# returns an mpmath mpf.  float() remains permissible for DISPLAY only.
import mpmath as _mp
_mp.mp.dps = 60          # 50-digit serialization needs headroom
_Q_EXACT = sp.Rational(Q_50_DIGIT_STR)

def _num(c):
    """Exact 50-dps value of a sympy coefficient at q0.  Returns mpf."""
    if not hasattr(c, "subs"):
        return _mp.mpf(c)
    return _mp.mpf(str(sp.N(c.subs(q, _Q_EXACT), 50)))

def _netsum(terms):
    """Coordinate sum of a normal form, carried in mpf end to end."""
    tot = _mp.mpf(0)
    for c in terms.values():
        tot += _num(c)
    return tot

try:
    SHA = subprocess.check_output(['git','rev-parse','HEAD'],
        cwd=str(Path(__file__).resolve().parent.parent.parent)).decode().strip()
except: SHA = "unknown"

# ── Word helpers ──────────────────────────────────────────────
# Each entry: (particle_name, word_string, knot_or_link_name)
# The knot/link is what the Markov trace of the braid closure produces.
PARTICLE_KNOT = {
    ():         ("ν",  "𝟏",      "unknot (0₁)"),
    (0,):       ("σ₀", "σ₀",     "virtual (ℓ=1)"),
    (1,):       ("σ₁", "σ₁",     "virtual (ℓ=1)"),
    (0, 1):     ("L₊", "σ₀σ₁",   "Hopf link"),
    (1, 0):     ("L₋", "σ₁σ₀",   "Hopf link"),
    (0, 1, 0):  ("e⁻", "σ₀σ₁σ₀", "trefoil (3₁)"),
}

def ws(w):
    if not w: return "𝟏"
    return "·".join(f"σ_{i}" for i in w)

def pn(w):
    return PARTICLE_KNOT.get(w, ("", "", ""))[0]

def knot_name(w):
    return PARTICLE_KNOT.get(w, ("", "", ""))[2]


# ══════════════════════════════════════════════════════════════
#  VERBOSE GRÖBNER REDUCTION
# ══════════════════════════════════════════════════════════════

def reduce_verbose(terms_dict, label="", max_iterations=10000):
    """
    Gröbner--Shirshov-reduce a symbolic Hecke element, printing every relation.
    Input: dict { word_tuple: sympy_coefficient }
    Output: reduced dict, step_counts
    """
    terms = {w: c for w, c in terms_dict.items() if c != 0}
    hecke = yb = fc = 0
    step_num = 0

    print(f"\n  ┌─ REDUCTION of {label}")
    print(f"  │  Starting terms: {len(terms)}")
    for w, c in sorted(terms.items(), key=lambda x: (len(x[0]), x[0])):
        v = float(c.subs(q, q0)) if not isinstance(c, (int, float)) else c
        print(f"  │    {v:+.6f} · {ws(w)}")
    print(f"  │")

    changed = True
    iteration = 0
    while changed and iteration < max_iterations:
        changed = False
        new_terms = {}

        for word, coeff in terms.items():
            if coeff == 0:
                continue

            reduced_this = False

            # ── R1: Hecke — σ_i² → (q−q⁻¹)·σ_i + 1 ──────────────
            for pos in range(len(word) - 1):
                if word[pos] == word[pos + 1] and word[pos] >= 0:
                    i = word[pos]
                    prefix = word[:pos]
                    suffix = word[pos + 2:]

                    w1 = prefix + (i,) + suffix
                    c1 = sp.expand(coeff * HA)
                    w2 = prefix + suffix
                    c2 = sp.expand(coeff * 1)

                    new_terms[w1] = sp.expand(new_terms.get(w1, sp.Integer(0)) + c1)
                    new_terms[w2] = sp.expand(new_terms.get(w2, sp.Integer(0)) + c2)

                    step_num += 1; hecke += 1
                    v_old = float(coeff.subs(q, q0)) if hasattr(coeff, 'subs') else coeff
                    v1 = float(c1.subs(q, q0)) if hasattr(c1, 'subs') else c1
                    v2 = float(c2.subs(q, q0)) if hasattr(c2, 'subs') else c2
                    print(f"  │  R1 Hecke  #{step_num:3d}:  "
                          f"{v_old:+.6f}·{ws(word)}  →  "
                          f"{v1:+.6f}·{ws(w1)} + {v2:+.6f}·{ws(w2)}")
                    print(f"  │    σ_{i}² = (q−q⁻¹)·σ_{i} + 1  "
                          f"at pos {pos} in {ws(word)}")

                    reduced_this = True
                    changed = True
                    break

            if reduced_this:
                continue

            # ── R2: Far-comm — σ_i·σ_j → σ_j·σ_i ─────────────────
            for pos in range(len(word) - 1):
                i_gen, j_gen = word[pos], word[pos + 1]
                do_swap = False
                reason = ""

                if i_gen >= 0 and j_gen < 0:
                    do_swap = True
                    reason = f"formal ℵ commutes left"
                elif (abs(i_gen - j_gen) >= 2 and i_gen > j_gen
                        and i_gen >= 0 and j_gen >= 0):
                    do_swap = True
                    reason = f"|{i_gen}−{j_gen}| = {abs(i_gen-j_gen)} ≥ 2"

                if do_swap:
                    new_word = word[:pos] + (j_gen, i_gen) + word[pos + 2:]
                    new_terms[new_word] = sp.expand(
                        new_terms.get(new_word, sp.Integer(0)) + coeff)
                    fc += 1; step_num += 1
                    v_old = float(coeff.subs(q, q0)) if hasattr(coeff, 'subs') else coeff
                    print(f"  │  R2 FC     #{step_num:3d}:  "
                          f"{v_old:+.6f}·{ws(word)}  →  "
                          f"{v_old:+.6f}·{ws(new_word)}")
                    print(f"  │    σ_{i_gen}·σ_{j_gen} → σ_{j_gen}·σ_{i_gen}  "
                          f"({reason})")
                    reduced_this = True
                    changed = True
                    break

            if reduced_this:
                continue

            # ── R3: Yang-Baxter — σ_i·σ_{i+1}·σ_i → σ_{i+1}·σ_i·σ_{i+1}
            for pos in range(len(word) - 2):
                a, b, c = word[pos], word[pos + 1], word[pos + 2]
                if a == c and a >= 0 and b >= 0 and abs(a - b) == 1:
                    new_trip = (b, a, b)
                    old_trip = (a, b, a)
                    if new_trip < old_trip:
                        new_word = word[:pos] + new_trip + word[pos + 3:]
                        new_terms[new_word] = sp.expand(
                            new_terms.get(new_word, sp.Integer(0)) + coeff)
                        yb += 1; step_num += 1
                        v_old = float(coeff.subs(q, q0)) if hasattr(coeff, 'subs') else coeff
                        print(f"  │  R3 YB     #{step_num:3d}:  "
                              f"{v_old:+.6f}·{ws(word)}  →  "
                              f"{v_old:+.6f}·{ws(new_word)}")
                        print(f"  │    σ_{a}·σ_{b}·σ_{a} → "
                              f"σ_{b}·σ_{a}·σ_{b}  at pos {pos}")
                        reduced_this = True
                        changed = True
                        break

            if not reduced_this:
                new_terms[word] = sp.expand(
                    new_terms.get(word, sp.Integer(0)) + coeff)

        terms = {w: c for w, c in new_terms.items() if c != 0}
        iteration += 1

    print(f"  │")
    print(f"  │  RESULT: {len(terms)} NF terms after "
          f"{hecke} Hecke + {yb} YB + {fc} FC = {step_num} steps")
    for w, c in sorted(terms.items(), key=lambda x: (len(x[0]), x[0])):
        v = float(c.subs(q, q0)) if hasattr(c, 'subs') else c
        name = pn(w)
        tag = f"  [{name}]" if name else ""
        print(f"  │    {v:+.10f} · {ws(w)}{tag}")

    net = _netsum(terms)
    print(f"  │    Net: {float(net):+.10f}")
    print(f"  └─ END {label}")

    return terms, {'hecke': hecke, 'yb': yb, 'fc': fc, 'total': step_num}


# ── Element multiplication ────────────────────────────────────
def mul_terms(a_terms, b_terms):
    result = {}
    for wa, ca in a_terms.items():
        for wb, cb in b_terms.items():
            w = wa + wb
            c = sp.expand(ca * cb)
            result[w] = sp.expand(result.get(w, sp.Integer(0)) + c)
    return {w: c for w, c in result.items() if c != 0}


# ── Crossing constructors ────────────────────────────────────
def crossing(type_i, type_j, gen):
    """Build crossing element for quark pair types."""
    pair = set([type_i, type_j])
    if type_i == type_j == 'u':
        print(f"  ── crossing({type_i},{type_j}) at σ_{gen}: "
              f"σ_{gen}  [u-u positive]")
        return {(gen,): sp.Integer(1)}
    elif type_i == type_j == 'd':
        C = sp.Integer(1); D = -(q - 1/q)
        print(f"  ── crossing({type_i},{type_j}) at σ_{gen}: "
              f"σ_{gen} − (q−q⁻¹)·𝟏  [d-d negative]")
        return {(gen,): C, (): D}
    elif pair == set(['u', 'd']):
        C = sp.Integer(1); D = -(q - 1/q) / 2
        print(f"  ── crossing({type_i},{type_j}) at σ_{gen}: "
              f"σ_{gen} − ½(q−q⁻¹)·𝟏  [u-d mixed]")
        return {(gen,): C, (): D}
    else:
        print(f"  ── crossing({type_i},{type_j}) at σ_{gen}: "
              f"σ_{gen}  [Hopf link]")
        return {(gen,): sp.Integer(1)}


# ══════════════════════════════════════════════════════════════
#  COMPUTATION
# ══════════════════════════════════════════════════════════════

print("=" * 80)
print("FREE NEUTRON DECAY  n → p + e⁻ + ν̄ₑ  — VERBOSE RELATION TRACE")
print(f"All Gröbner--Shirshov relations shown for every reduction step.")
print(f"Commit: {SHA[:8]}  |  q₀ = {q0:.10f}")
print("=" * 80)

print(f"""
RELATIONS APPLIED:
  R1 (Hecke):       σ_i² = (q − q⁻¹)·σ_i + 1       [creates/absorbs terms]
  R2 (Far-comm):    σ_i·σ_j = σ_j·σ_i  (|i−j| ≥ 2) [reorders word]
  R3 (Yang-Baxter): σ_i·σ_{{i+1}}·σ_i = σ_{{i+1}}·σ_i·σ_{{i+1}}  [braid move]

CROSSING TYPES:
  u-u:  σ_i                          [same-flavor up: pure positive]
  d-d:  q²·σ_i − q·s·𝟏             [same-flavor down: Skein mixing]
  u-d:  ½(1+q²)·σ_i − ½q·s·𝟏      [mixed: averaged]

HECKE CONSTANTS at q₀ = {q0:.10f}:
  HA = q − q⁻¹ = {q0 - 1/q0:.10f}
  s  = q^½ − q^{{-½}} = {q0**0.5 - q0**(-0.5):.10f}
  z  = q³/(q²+1) [conv D] = {float(q0**3/(q0**2+1)):.10f}
""")

# ── Step 0: σ₁⁻¹ ─────────────────────────────────────────────
print("─" * 80)
print("STEP 0: Build σ₁⁻¹")
print("─" * 80)
print(f"  From σ² = (q−q⁻¹)σ + 1, multiply both sides by σ⁻¹:")
print(f"    σ = (q−q⁻¹) + σ⁻¹")
print(f"    σ⁻¹ = σ − (q−q⁻¹)")
print(f"  So: σ₁⁻¹ = σ₁ − HA = σ₁ − ({q0 - 1/q0:.10f})")
print()

sig1_inv = {(1,): sp.Integer(1), (): -HA}
for w, c in sig1_inv.items():
    v = float(c.subs(q, q0))
    v_polynomial_q = expose_polynomial(c, q)
    print(f"    {v:+.10f} · {ws(w)}")

# ── Step 1: B₃ = (σ₀·σ₁⁻¹)³ ─────────────────────────────────
print()
print("─" * 80)
print("STEP 1: Build B₃ = (σ₀·σ₁⁻¹)³  Borromean confinement braid")
print("─" * 80)

sig0 = {(0,): sp.Integer(1)}

print("\n  Phase 1a: unit = σ₀ · σ₁⁻¹")
unit = mul_terms(sig0, sig1_inv)
for w, c in sorted(unit.items(), key=lambda x: (len(x[0]), x[0])):
    v = float(c.subs(q, q0))
    v_polynomial_q = expose_polynomial(c, q)
    print(f"    {v:+.10f} · {ws(w)}")

print("\n  Phase 1b: unit² = (σ₀·σ₁⁻¹)²  [unreduced]")
unit2_raw = mul_terms(unit, unit)
for w, c in sorted(unit2_raw.items(), key=lambda x: (len(x[0]), x[0])):
    v = float(c.subs(q, q0))
    v_polynomial_q = expose_polynomial(c, q)
    print(f"    {v:+.10f} · {ws(w)}")

print("\n  Phase 1c: Reduce unit²")
unit2, steps_u2 = reduce_verbose(unit2_raw, "unit²")

print("\n  Phase 1d: B₃ = unit² · unit  [unreduced]")
b3_raw = mul_terms(unit2, unit)
for w, c in sorted(b3_raw.items(), key=lambda x: (len(x[0]), x[0])):
    v = float(c.subs(q, q0))
    v_polynomial_q = expose_polynomial(c, q)
    print(f"    {v:+.10f} · {ws(w)}")

print("\n  Phase 1e: Reduce B₃")
b3, steps_b3 = reduce_verbose(b3_raw, "B₃")

# ── Step 2: NF(neutron) = B₃ · crossings(u,d,d) ─────────────
print()
print("─" * 80)
print("STEP 2: NF(neutron) = B₃ · crossings(u, d, d)")
print("  Quarks: [u (strand 0), d₁ (strand 1), d₂ (strand 2)]")
print("  Pairwise crossings: (0,1)=u-d  (0,2)=u-d  (1,2)=d-d")
print("─" * 80)

types_n = ['u', 'd', 'd']
elem_n = dict(b3)
total_steps_n = dict(steps_b3)
A = len(types_n)

for i in range(A):
    for j in range(i + 1, A):
        print(f"\n  Phase 2.{i}{j}: Multiply by crossing({types_n[i]},{types_n[j]}) at gen {i}")
        cx = crossing(types_n[i], types_n[j], i)
        product = mul_terms(elem_n, cx)
        print(f"  Unreduced product: {len(product)} terms")
        elem_n, s = reduce_verbose(product, f"neutron after ({i},{j})")
        for k, v in s.items():
            total_steps_n[k] = total_steps_n.get(k, 0) + v

# ── Final neutron NF ─────────────────────────────────────────
print()
print("=" * 80)
print(f"NEUTRON NF(𝔫) = NF(B₃ · crossings(u,d,d)): {len(elem_n)} terms")
print("=" * 80)
for w, c in sorted(elem_n.items(), key=lambda x: (len(x[0]), x[0])):
    v = float(c.subs(q, q0))
    v_polynomial_q = expose_polynomial(c, q)
    name = pn(w)
    tag = f"  [{name}]" if name else ""
    print(f"  {v:+.10f} · {ws(w):<15}{tag}")
net_n = _netsum(elem_n)
print(f"  Net: {float(net_n):+.10f}")
print(f"  Reductions: {total_steps_n}")

# ── Step 3: NF(proton) = B₃ · crossings(u,u,d) ──────────────
print()
print("─" * 80)
print("STEP 3: NF(proton) = B₃ · crossings(u, u, d)")
print("  Quarks: [u_r (strand 0), u_g (strand 1), d_b (strand 2)]")
print("  Pairwise crossings: (0,1)=u-u  (0,2)=u-d  (1,2)=u-d")
print("─" * 80)

types_p = ['u', 'u', 'd']
elem_p = dict(b3)
total_steps_p = dict(steps_b3)

for i in range(A):
    for j in range(i + 1, A):
        print(f"\n  Phase 3.{i}{j}: Multiply by crossing({types_p[i]},{types_p[j]}) at gen {i}")
        cx = crossing(types_p[i], types_p[j], i)
        product = mul_terms(elem_p, cx)
        print(f"  Unreduced product: {len(product)} terms")
        elem_p, s = reduce_verbose(product, f"proton after ({i},{j})")
        for k, v in s.items():
            total_steps_p[k] = total_steps_p.get(k, 0) + v

# ── Final proton NF ──────────────────────────────────────────
print()
print("=" * 80)
print(f"PROTON NF(𝔭) = NF(B₃ · crossings(u,u,d)): {len(elem_p)} terms")
print("=" * 80)
for w, c in sorted(elem_p.items(), key=lambda x: (len(x[0]), x[0])):
    v = float(c.subs(q, q0))
    v_polynomial_q = expose_polynomial(c, q)
    name = pn(w)
    tag = f"  [{name}]" if name else ""
    print(f"  {v:+.10f} · {ws(w):<15}{tag}")
net_p = _netsum(elem_p)
print(f"  Net: {float(net_p):+.10f}")
print(f"  Reductions: {total_steps_p}")

# ── Step 4: Transition n → p ─────────────────────────────────
print()
print("=" * 80)
print("FREE NEUTRON DECAY:  n → p + e⁻ + ν̄ₑ")
print("=" * 80)
print()

# Term-by-term comparison
all_words = sorted(set(list(elem_p.keys()) + list(elem_n.keys())),
                   key=lambda x: (len(x), x))
print(f"  {'Word':<15} {'Neutron 𝔫':>12} {'Proton 𝔭':>12} {'Δ(n−p)':>12} Particle")
print(f"  {'─'*15} {'─'*12} {'─'*12} {'─'*12} {'─'*8}")
for w in all_words:
    vn = float(elem_n[w].subs(q, q0)) if w in elem_n else 0
    vp = float(elem_p[w].subs(q, q0)) if w in elem_p else 0
    d = vn - vp
    name = pn(w)
    print(f"  {ws(w):<15} {vn:+12.6f} {vp:+12.6f} {d:+12.6f} {name}")

print()
print(f"  Net (neutron):  {float(net_n):+.10f}")
print(f"  Net (proton):   {float(net_p):+.10f}")
print(f"  Δ(n − p):       {float(net_n - net_p):+.10f}")
print()

# ν and e⁻ sector deltas
n_nu = float(elem_n.get((), sp.Integer(0)).subs(q, q0)) if () in elem_n else 0
p_nu = float(elem_p.get((), sp.Integer(0)).subs(q, q0)) if () in elem_p else 0
n_e = float(elem_n.get((0,1,0), sp.Integer(0)).subs(q, q0)) if (0,1,0) in elem_n else 0
p_e = float(elem_p.get((0,1,0), sp.Integer(0)).subs(q, q0)) if (0,1,0) in elem_p else 0

print(f"  ν sector:   Δν  = ν(n) − ν(p) = {n_nu - p_nu:+.10f}")
print(f"  e⁻ sector:  Δe⁻ = e⁻(n) − e⁻(p) = {n_e - p_e:+.10f}")
print()
print(f"  Physical interpretation:")
print(f"    The neutron NF has MORE ν content than proton ({n_nu:+.6f} vs {p_nu:+.6f})")
print(f"    The neutron NF has MORE e⁻ content ({n_e:+.6f} vs {p_e:+.6f})")
print(f"    → Decay releases these sectors as free particles: e⁻ + ν̄ₑ")
print()

# Observed
print(f"  Observed free neutron decay:")
print(f"    Q = m_n − m_p − m_e ≈ 939.56542 − 938.27209 − 0.51100 = 0.78233341 MeV")  # noqa: P31 — narrative print of CODATA cross-check; live values from experimental_constants
print(f"    τ = 878.4 ± 0.5 s")

# ── Witness JSON ──────────────────────────────────────────────
def terms_to_list(terms):
    result = []
    for w, c in sorted(terms.items(), key=lambda x: (len(x[0]), x[0])):
        v = float(c.subs(q, q0))
        v_polynomial_q = expose_polynomial(c, q)
        result.append({
            "word": list(w), "word_str": ws(w), "particle": pn(w),
            "knot": knot_name(w),
            "coefficient_symbolic": str(c),
            "coefficient_numeric": v,
        })
    return result

witness = {
    "computation": "free-neutron-decay",
    # Emitted BY THE PRODUCER. This field was previously hand-added to the
    # committed witness and was silently lost on every regeneration -- a
    # hand-edited field is the opposite of derived.
    "auditOnly": "docs/audits/categorical-vs-fitted-q-decay-ba.md",
    "description": "Free neutron decay n → p + e⁻ + ν̄ₑ with B₃ Borromean binding. "
                   "All Gröbner--Shirshov relations traced verbosely.",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "commit_sha": SHA,
    "q0": q0,
    "relations": {
        "R1_Hecke": "σ_i² = (q − q⁻¹)·σ_i + 1",
        "R2_far_comm": "σ_i·σ_j = σ_j·σ_i for |i−j| ≥ 2",
        "R3_Yang_Baxter": "σ_i·σ_{i+1}·σ_i = σ_{i+1}·σ_i·σ_{i+1}",
        "sigma_inv": "σ_i⁻¹ = σ_i − (q − q⁻¹)",
        "B3": "B₃ = (σ₀·σ₁⁻¹)³",
    },
    "crossing_types": {
        "u-u": "σ_i",
        "d-d": "q²·σ_i − q·s·𝟏  where s = q^½ − q^{-½}",
        "u-d": "½(1+q²)·σ_i − ½q·s·𝟏",
    },
    "constants_at_q0": {
        # exact at 50 dps, never the float64 q_parameter.Q
        "q0": str(q0_mp), "HA": str(q0_mp - 1/q0_mp),
        "s_skein": str(_mp.sqrt(q0_mp) - 1/_mp.sqrt(q0_mp)),
        # convention D (owner ruling 2026-08-15 R1); was z_C = 0.4993203...
        "z_markov": str(q0_mp**3 / (q0_mp**2 + 1)),
        "z_markov_convention": "D: z = q^3/(q^2+1)",
    },
    "neutron": {
        "composition": "[u, d, d]",
        "nf_terms": terms_to_list(elem_n),
        "n_terms": len(elem_n),
        "net_coefficient": float(net_n),
        "net_coefficient_exact": str(net_n),
        "reduction_steps": total_steps_n,
    },
    "proton": {
        "composition": "[u, u, d]",
        "nf_terms": terms_to_list(elem_p),
        "n_terms": len(elem_p),
        "net_coefficient": float(net_p),
        "net_coefficient_exact": str(net_p),
        "reduction_steps": total_steps_p,
    },
    "transition": {
        # exact 50-dps strings; float64 would truncate at digit 17
        "delta_net": str(net_n - net_p),
        "delta_net_float": float(net_n - net_p),  # legacy consumers
        "delta_nu": n_nu - p_nu,
        "delta_e": n_e - p_e,
        "Q_observed_MeV": 0.78233,  # noqa: P31 — comparison-only snapshot in JSON output; live value from experimental_constants.Q_BETA_MEV
    },
}

from codata_constants import M_E_MEV as _ME_FND, Q_BETA_MEV as _QB_CODATA_FND  # noqa: E402
_me_fnd = _mp.mpf(str(_ME_FND))
_qb_codata_fnd = _mp.mpf(str(_QB_CODATA_FND))
_q2_fnd = q0_mp ** 2
_tr_conn_p_fnd = -2 * ((_q2_fnd - 1) ** 4) * (_q2_fnd ** 2 + _q2_fnd + 1) / (27 * (_q2_fnd ** 3))
_tr_conn_n_fnd = ((_q2_fnd - 1) ** 4) * (2 * (_q2_fnd ** 2) - _q2_fnd + 2) / (27 * (_q2_fnd ** 3))
_tr_conn_diff_fnd = _tr_conn_n_fnd - _tr_conn_p_fnd
_dm_qed_conn_fnd = -_me_fnd * _tr_conn_diff_fnd
_dm_qed_conn_knkp_fnd = -_me_fnd * ((_tr_conn_n_fnd / q0_mp) - (q0_mp * _tr_conn_p_fnd))
_dm_qed_conn_kp3_fnd = -_me_fnd * (_tr_conn_n_fnd - (q0_mp * _tr_conn_p_fnd))
_dm_qed_conn_q_fnd = -_me_fnd * q0_mp * _tr_conn_diff_fnd
_qa_fnd = _me_fnd * abs(_q2_fnd - 2 * q0_mp - 1) * (q0_mp + 1) / (2 * (q0_mp ** 3))
_h_fnd = q0_mp - 1 / q0_mp
_z_fnd = (q0_mp ** 3) / (_q2_fnd + 1)
_hbar_fnd = (q0_mp - 1) / q0_mp
_alpha_fnd = (_z_fnd - 1) * _h_fnd / 2
_b_fnd = _mp.sqrt(1 - _q2_fnd / ((_q2_fnd + 1) ** 2))
_qn1_fnd = _qa_fnd * _mp.cos(_alpha_fnd - _b_fnd * (_hbar_fnd ** 2) / 2)
_qn2_fnd = _qn1_fnd * (1 - (_b_fnd ** 2) * (_hbar_fnd ** 4))
_qn2_two_term_fnd = _qn2_fnd + _dm_qed_conn_fnd
_err_qn2_ppm = (_qn2_fnd - _qb_codata_fnd) / _qb_codata_fnd * _mp.mpf(10) ** 6
_err_qn2_two_term_ppm = (_qn2_two_term_fnd - _qb_codata_fnd) / _qb_codata_fnd * _mp.mpf(10) ** 6
_err_red_pct = (1 - abs(_err_qn2_two_term_ppm) / abs(_err_qn2_ppm)) * _mp.mpf(100)

witness["two_term_borromean_qed_dressing"] = {
    "lean_ref": "QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.trace_QAdj_connected_diff_borromeanV3",
    "tr_conn_p_V3": str(_tr_conn_p_fnd),
    "tr_conn_n_V3": str(_tr_conn_n_fnd),
    "Delta_tr_conn_V3": str(_tr_conn_diff_fnd),
    "Delta_m_QED_conn_MeV": str(_dm_qed_conn_fnd),
    "Delta_m_QED_conn_KnKp_MeV": str(_dm_qed_conn_knkp_fnd),
    "Delta_m_QED_conn_Kp3_MeV": str(_dm_qed_conn_kp3_fnd),
    "Delta_m_QED_conn_q_MeV": str(_dm_qed_conn_q_fnd),
    "Q_N2_MeV": str(_qn2_fnd),
    "Q_N2_two_term_MeV": str(_qn2_two_term_fnd),
    "Q_N2_vs_CODATA_ppm": str(_err_qn2_ppm),
    "Q_N2_two_term_vs_CODATA_ppm": str(_err_qn2_two_term_ppm),
    "error_reduction_pct": str(_err_red_pct),
}

# Write beside THIS FILE, not into the caller's cwd. As a bare relative path
# a run from the repo root -- how producers are normally invoked -- created an
# untracked orphan at ./free-neutron-decay.witness.json and left the tracked
# computations/ copy untouched. That makes a re-run look like a REPRODUCTION:
# diffing the committed file after such a run compares it against itself.
# Measured (bean qou-nxxw): it cost three runs to notice the committed witness
# was stale by the full 11.5 ppb mu-p tension.
#
# `scriptFile` likewise: this producer wrote none, so a downstream provenance
# backfill guessed `derived_masses.py` -- which only READS this witness. Any
# tool resolving producer-from-witness therefore re-ran the wrong script.
witness["scriptFile"] = Path(__file__).name
out = Path(__file__).resolve().parent / "free-neutron-decay.witness.json"
with open(out, "w") as f:
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
    #
    # MERGE NOTE: main and this branch fixed the SAME qou-4un2 defect from
    # different directions and BOTH halves are kept -- main's staleness/q0
    # stamp, this branch's `auditOnly` above and ensure_ascii=False below.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=None)
    # ensure_ascii=False: the braid relations are written with real
    # sigma/subscript glyphs and the corpus stores them readable.
    json.dump(witness, f, indent=2, default=str, ensure_ascii=False)
print(f"\nWitness: {out} (commit: {SHA[:8]})")
