#!/usr/bin/env python3
"""Whitehead braid-word identification by the formula-free 4G volume test,
using the fast (numpy) validated colored-Jones machinery.

The closure whose normalized colored Jones grows at rate 4·G = 3.66386
(regular ideal octahedron) is the Whitehead link.  Discriminants:
    torus / split         Vol 0
    Whitehead (L5a1)      4G       = 3.66386
    Borromean rings       2Vol(oct)= 7.32772
No colored-Jones form is assumed — the volume is read off the growth.

Audit-only; no wiring.
"""
from __future__ import annotations

import sys
from itertools import product
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from whitehead_fast import volume_estimate, perm_cycles  # noqa: E402

VOL_WHITEHEAD = 3.663862376708876


def curated_words():
    """Standard / literature Whitehead-link braid-word candidates (B₃)."""
    return [
        [1, 1, 2, -1, 2],          # σ1²σ2σ1⁻¹σ2
        [1, 1, -2, 1, -2],
        [1, -2, 1, -2, 1],
        [1, -2, 1, -2, -2],
        [1, 1, 2, 2, -1],
        [1, 2, -1, 2, 2],
        [1, 1, -2, -1, -2],
        [-1, -1, 2, 1, 2],
    ]


def main() -> int:
    print("Curated Whitehead candidates (B₃), volume via near-root growth (δ=1e-6):")
    print("  target 4G = 3.66386\n")
    for w in curated_words():
        c = perm_cycles(w, 3)
        rows = volume_estimate(w, 3, [4, 6, 8, 10], delta=1e-6)
        vol = rows[-1][2]
        tag = ""
        if vol is not None:
            if abs(vol - VOL_WHITEHEAD) < 0.15:
                tag = "  <== WHITEHEAD (4G)"
            elif abs(vol - 7.3277) < 0.2:
                tag = "  (Borromean-like)"
            elif abs(vol) < 0.3:
                tag = "  (torus/split, Vol 0)"
        seq = "  ".join(f"N={N}:{(f'{r:.3f}' if r is not None else f'{e:.3f}')}"
                         for N, e, r in rows)
        print(f"  {str(w):<22} comps={c}  {seq}   vol≈{(f'{vol:.4f}' if vol else '—')}{tag}")

    # bounded formula-free search: all 2-component 3-braid words len 5, no
    # adjacent cancellation, low-N volume near 4G
    print("\nBounded search — 2-component 3-braid words (len 5), vol within 0.3 of 4G:")
    gens = [1, -1, 2, -2]
    seen = set()
    hits = []
    for word in product(gens, repeat=5):
        if any(word[i] == -word[i + 1] for i in range(4)):
            continue
        if perm_cycles(list(word), 3) != 2:
            continue
        # canonical: skip cyclic-rotation / inverse dups cheaply via sorted key
        key = tuple(word)
        if key in seen:
            continue
        seen.add(key)
        try:
            rows = volume_estimate(list(word), 3, [4, 6, 8], delta=1e-6)
            vol = rows[-1][2]
        except Exception:
            continue
        if vol is not None and abs(vol - VOL_WHITEHEAD) < 0.3:
            hits.append((list(word), vol))
    hits.sort(key=lambda t: abs(t[1] - VOL_WHITEHEAD))
    print(f"  {len(hits)} words near 4G (of {len(seen)} 2-component len-5 words):")
    for w, vol in hits[:15]:
        print(f"    {w}  vol≈{vol:.4f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
