#!/usr/bin/env python3
"""
Cross-check the pure-Python KL Betti sums (kl_betti_cell_dependence_probe.py)
against the canonical Rust engine `pyhecke_native.kl_betti_sum_rust`, over
EVERY left cell of S_6.

Requires the `pyhecke_native` wheel (build from tools/pyhecke-native; the
default build already exposes `kl_betti_sum_rust`, no `clarabel-lp` needed).

Result (2026-06-25): 76/76 cells match, zero mismatches; the per-shape Betti
*ranges* agree exactly between both engines — e.g. (3,3): 6..23, (3,2,1):
22..54, (4,1,1): 10..26 in BOTH. This confirms, against the canonical engine,
that B_λ is cell-dependent (the kl-betti-cell-dependence finding). The Rust
function sums P_{identity,w}(1) over the *given* cell, so it agrees per-cell and
cannot itself resolve the cell-ambiguity.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from collections import defaultdict
import kazhdan_lusztig as KL  # noqa: E402
import pyhecke_native  # noqa: E402

def rsk_PQ(w):
    P=[]; Q=[]
    for i,x in enumerate(w):
        r=0
        while r < len(P):
            idx=-1
            for c in range(len(P[r])):
                if P[r][c] > x: idx=c; break
            if idx==-1:
                P[r].append(x); Q[r].append(i+1); break
            else:
                x, P[r][idx] = P[r][idx], x; r+=1
        if r==len(P):
            P.append([x]); Q.append([i+1])
    return P, Q

n = 6
perms = KL.permutations_S_n(n)
ident = tuple(range(1, n+1))
_c = {}
def P1(w):
    if w in _c: return _c[w]
    pol = KL.kl_polynomial(ident, w)
    v = int(pol.subs({s: 1 for s in pol.free_symbols})); _c[w]=v; return v

cells = defaultdict(list)
for w in perms:
    _, Q = rsk_PQ(w)
    cells[tuple(tuple(r) for r in Q)].append(w)

print(f"checking {len(cells)} left cells of S_{n} (pure-Python KL vs Rust kl_betti_sum_rust)...")
mismatches = 0; checked = 0
byshape = defaultdict(list)
for Q, ws in cells.items():
    shape = tuple(len(r) for r in Q)
    py   = sum(P1(tuple(w)) for w in ws)
    rust = pyhecke_native.kl_betti_sum_rust(n, [list(w) for w in ws])
    checked += 1
    if py != rust:
        mismatches += 1
        print(f"  MISMATCH shape={shape} py={py} rust={rust}")
    byshape[shape].append((py, rust))

print(f"\ncells checked = {checked}, mismatches = {mismatches}\n")
print(f"{'shape':16s} {'py range':>12s} {'rust range':>12s} {'agree?':>7s}")
print("-"*52)
allmatch = True
for shape in sorted(byshape, key=lambda k: sum(k), reverse=True):
    pys  = sorted(p for p,_ in byshape[shape])
    rusts= sorted(r for _,r in byshape[shape])
    agree = (pys == rusts)
    allmatch &= agree
    print(f"{str(shape):16s} {f'{min(pys)}..{max(pys)}':>12s} {f'{min(rusts)}..{max(rusts)}':>12s} {str(agree):>7s}")
print("-"*52)
ok = (mismatches == 0 and allmatch)
print(f"\nRUST PARITY: {'CONFIRMED — every cell matches' if ok else 'FAILED'}")
sys.exit(0 if ok else 1)
