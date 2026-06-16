#!/usr/bin/env python3
"""
Check LP stability of each atom BEFORE molecular bonding.

The gluon derivation showed: the 9-crossing proton FAILS Frobenius
(Gx[γ] < 0), needing 2 gluon crossings to stabilize.

Question: are C(6,6), O(8,8), and H(1,0) atoms in their LP-stable
ground states? If not, the molecular computation starts from the
wrong baseline.

For each atom, check:
1. Does the atom NF satisfy Gx ≥ 0 (Frobenius positivity)?
2. If not, which channels violate?
3. What additional crossings are needed to stabilize?

Also: in chemistry, C-H bond FORMATION releases energy (exothermic).
The bond dissociation energy D₀(C-H) = 4.48 eV is the energy needed
to BREAK the bond.  So the bonded state is LOWER energy than separated.
The LP should find that bonded Φ₁ < unbonded Φ₁ (more negative = more
stable).

Usage:
    cd computations
    python3 atom-stability-check.py
"""

import math
import numpy as np
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent.parent / "substrate"))
from q_parameter import Q as q0, Q_INV as qi0, HA as h, q_int
# z/NF_BASIS/TR_M now owned by pyhecke.gram (M2b inversion). Keep local
# bootstrap for dev mode; the installed-pyhecke path is preferred.
import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parents[2] / "tools" / "pyhecke" / "python"))
from pyhecke.gram import z as _PG_Z, NF_BASIS as _PG_NF_BASIS, TR_M as _PG_TR_M  # noqa: E402


z = _PG_Z  # moved to pyhecke.gram
NF_BASIS = _PG_NF_BASIS  # moved to pyhecke.gram
NF_NAMES = ["γ", "σ₀", "σ₁", "L₊", "L₋", "e⁻"]
TR_M = np.array([1.0, z, z, z**2, z**2, z**3])


def hecke_mul(nf, c, d, gen):
    r = [0.0]*6
    if gen == 0:
        tables = [(0,[(1,c),(0,d)]),(1,[(1,c*h),(0,c),(1,d)]),(2,[(3,c),(2,d)]),(3,[(3,c*h),(2,c),(3,d)]),(4,[(5,c),(4,d)]),(5,[(5,c*h),(4,c),(5,d)])]
    else:
        tables = [(0,[(2,c),(0,d)]),(1,[(4,c),(1,d)]),(2,[(2,c*h),(0,c),(2,d)]),(3,[(5,c),(3,d)]),(4,[(4,c*h),(1,c),(4,d)]),(5,[(5,c*h),(3,c),(5,d)])]
    for si, tgts in tables:
        if abs(nf[si]) < 1e-15: continue
        for ti, co in tgts: r[ti] += nf[si] * co
    return r


# Build Gram matrix
def hecke_mul_dict(t1, t2):
    result = {}
    for w1, c1 in t1.items():
        for w2, c2 in t2.items():
            w = w1 + w2
            result[w] = result.get(w, 0.0) + c1 * c2
    return {w: c for w, c in result.items() if abs(c) > 1e-15}

def reduce_nf_dict(terms):
    changed = True
    while changed:
        changed = False
        new_terms = {}
        for word, coeff in terms.items():
            if abs(coeff) < 1e-15: continue
            done = False
            for pos in range(len(word) - 1):
                if word[pos] == word[pos + 1]:
                    i = word[pos]
                    pre, suf = word[:pos], word[pos + 2:]
                    new_terms[pre + (i,) + suf] = new_terms.get(pre + (i,) + suf, 0.0) + coeff * h
                    new_terms[pre + suf] = new_terms.get(pre + suf, 0.0) + coeff
                    done = changed = True; break
            if done: continue
            for pos in range(len(word) - 2):
                a, b, c = word[pos], word[pos+1], word[pos+2]
                if a == c and abs(a - b) == 1:
                    new_trip = (b, a, b)
                    if new_trip < (a, b, a):
                        nw = word[:pos] + new_trip + word[pos+3:]
                        new_terms[nw] = new_terms.get(nw, 0.0) + coeff
                        done = changed = True; break
            if not done:
                new_terms[word] = new_terms.get(word, 0.0) + coeff
        terms = {w: c for w, c in new_terms.items() if abs(c) > 1e-15}
    return terms

def to_vec(terms):
    return np.array([terms.get(b, 0.0) for b in NF_BASIS])

G = np.zeros((6, 6))
for i in range(6):
    for j in range(6):
        prod = hecke_mul_dict({NF_BASIS[i]: 1.0}, {NF_BASIS[j]: 1.0})
        nf = reduce_nf_dict(prod)
        vec = to_vec(nf)
        G[i, j] = sum(vec[k] * TR_M[k] for k in range(6))


def check_frobenius(nf, label):
    x = np.array(nf)
    Gx = G @ x
    n_viol = sum(1 for v in Gx if v < -1e-10)
    tr = sum(nf[i] * TR_M[i] for i in range(6))
    net = sum(nf)
    print(f"\n  {label}")
    print(f"    NF = [{', '.join(f'{v:+.6f}' for v in nf)}]")
    print(f"    net = {net:+.6f}, tr_M = {tr:.6e}")
    print(f"    Frobenius Gx:")
    for i in range(6):
        status = "✓" if Gx[i] >= -1e-10 else "✗ VIOLATED"
        tight = " (tight)" if abs(Gx[i]) < 1e-6 else ""
        print(f"      [{NF_NAMES[i]}] = {Gx[i]:+.10f}  {status}{tight}")
    print(f"    LP stable: {'YES' if n_viol == 0 else f'NO ({n_viol} violations)'}")
    return n_viol == 0, Gx


# ══════════════════════════════════════════════════════════════
# Build atoms at different stages
# ══════════════════════════════════════════════════════════════

print("=" * 70)
print("ATOM LP STABILITY CHECK")
print("=" * 70)

# ── Proton stages ─────────────────────────────────────────────
print("\n" + "=" * 70)
print("PROTON")
print("=" * 70)

# B₃ only (6 crossings)
nf = [1.0, 0, 0, 0, 0, 0]
for _ in range(3):
    nf = hecke_mul(nf, 1, 0, 0)
    nf = hecke_mul(nf, 1, -h, 1)
check_frobenius(nf, "B₃ only (6 crossings)")

# B₃ + quarks (9 crossings)
nf_9 = nf[:]
nf_9 = hecke_mul(nf_9, 1, 0, 0)       # uu
nf_9 = hecke_mul(nf_9, 1, -h/2, 1)    # ud
nf_9 = hecke_mul(nf_9, 1, -h/2, 0)    # ud
check_frobenius(nf_9, "B₃ + quarks uud (9 crossings)")

# B₃ + quarks + 2 gluon σ₀ (11 crossings)
nf_11 = nf_9[:]
nf_11 = hecke_mul(nf_11, 1, 0, 0)
nf_11 = hecke_mul(nf_11, 1, 0, 0)
check_frobenius(nf_11, "B₃ + quarks + 2 gluon σ₀ (11 crossings)")

# ── Neutron ───────────────────────────────────────────────────
print("\n" + "=" * 70)
print("NEUTRON")
print("=" * 70)

nf_n = [1.0, 0, 0, 0, 0, 0]
for _ in range(3):
    nf_n = hecke_mul(nf_n, 1, 0, 0)
    nf_n = hecke_mul(nf_n, 1, -h, 1)
nf_n = hecke_mul(nf_n, 1, 0, 0)       # ud
nf_n = hecke_mul(nf_n, 1, -h/2, 1)    # dd
nf_n = hecke_mul(nf_n, 1, -h/2, 0)    # ud
check_frobenius(nf_n, "B₃ + quarks udd (9 crossings)")

nf_n13 = nf_n[:]
for _ in range(4):
    nf_n13 = hecke_mul(nf_n13, 1, 0, 0)
check_frobenius(nf_n13, "B₃ + quarks + 4 gluon σ₀ (13 crossings)")

# ── H atom = proton + electron ────────────────────────────────
print("\n" + "=" * 70)
print("HYDROGEN ATOM")
print("=" * 70)

# Without gluon
nf_H_no_gluon = nf_9[:]
nf_H_no_gluon = hecke_mul(nf_H_no_gluon, 1, -h, 1)  # pe
check_frobenius(nf_H_no_gluon, "H (9-cross proton + e⁻, NO gluon)")

# With gluon
nf_H = nf_11[:]
nf_H = hecke_mul(nf_H, 1, -h, 1)  # pe
stable_H, Gx_H = check_frobenius(nf_H, "H (11-cross proton + e⁻, WITH gluon)")

# ── Carbon atom ───────────────────────────────────────────────
print("\n" + "=" * 70)
print("CARBON ATOM C(6,6)")
print("=" * 70)

def build_atom_stages(Z, N, label):
    """Build atom and check stability at each stage."""
    nf = [1.0, 0, 0, 0, 0, 0]
    pc, nc = 0, 0

    for k in range(Z + N):
        is_p = (k % 2 == 0 and pc < Z) or nc >= N
        ntype = "proton" if is_p else "neutron"

        if is_p:
            for _ in range(3):
                nf = hecke_mul(nf, 1, 0, 0)
                nf = hecke_mul(nf, 1, -h, 1)
            nf = hecke_mul(nf, 1, 0, 0)
            nf = hecke_mul(nf, 1, -h/2, 1)
            nf = hecke_mul(nf, 1, -h/2, 0)
            nf = hecke_mul(nf, 1, 0, 0)
            nf = hecke_mul(nf, 1, 0, 0)
            pc += 1
        else:
            for _ in range(3):
                nf = hecke_mul(nf, 1, 0, 0)
                nf = hecke_mul(nf, 1, -h, 1)
            nf = hecke_mul(nf, 1, 0, 0)
            nf = hecke_mul(nf, 1, -h/2, 1)
            nf = hecke_mul(nf, 1, -h/2, 0)
            for _ in range(4):
                nf = hecke_mul(nf, 1, 0, 0)
            nc += 1

    nf_nucleus = nf[:]
    stable_nuc, _ = check_frobenius(nf_nucleus, f"{label} nucleus ({pc}p + {nc}n, no electrons)")

    # Add electrons one at a time
    for e in range(1, Z + 1):
        nf = hecke_mul(nf, 1, -h, 1)  # pe crossing
        stable_e, Gx_e = check_frobenius(nf, f"{label} + {e} electron(s)")

    return nf, stable_e

nf_C, stable_C = build_atom_stages(6, 6, "C(6,6)")

# ── Oxygen atom ───────────────────────────────────────────────
print("\n" + "=" * 70)
print("OXYGEN ATOM O(8,8)")
print("=" * 70)

nf_O, stable_O = build_atom_stages(8, 8, "O(8,8)")

# ══════════════════════════════════════════════════════════════
# Summary
# ══════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"\n  H atom LP stable:  {stable_H}")
print(f"  C atom LP stable:  {stable_C}")
print(f"  O atom LP stable:  {stable_O}")
print()
print("  If any atom is NOT LP stable, it needs additional crossings")
print("  (like the proton gluon) before molecular bonding makes sense.")
print()
print("  Chemistry: C-H bond formation RELEASES energy (exothermic).")
print("  D₀(C-H) = 4.48 eV is the energy to BREAK the bond.")
print("  The bonded state must be LOWER in Φ₁ than separated atoms.")
