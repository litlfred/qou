#!/usr/bin/env python3
"""Empirically extract per-edge Bratteli ratios y_λ^(n+1)/(z·y_μ^(n))
from the Jones-Markov witness file, and test candidate closed forms.

Companion script for prop:wedderburn-bratteli-recursion.
"""
from __future__ import annotations
import json
from pathlib import Path
import mpmath as mp

mp.mp.dps = 30

import sys
sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0_FLOAT

with open(Path(__file__).parent / "y-lambda-jones-markov-witness.json") as f:
    W = json.load(f)

# Build (n, λ_tuple) → y_λ lookup
yl: dict = {}
for n_str, t in W["tables_by_n"].items():
    for ww in t["weights"]:
        yl[(int(n_str), tuple(ww["partition"]))] = mp.mpf(str(ww["y_lambda"]))

q = mp.mpf(repr(Q0_FLOAT))
z = 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))


def qint(k: int) -> mp.mpf:
    if k == 0:
        return mp.mpf(0)
    return (q ** k - q ** (-k)) / (q - 1 / q)


def removable_corners(lam: tuple) -> list:
    """Return list of (mu, content, row) triples for each removable corner."""
    L = list(lam)
    out = []
    for i in range(len(L)):
        if i == len(L) - 1 or L[i] > L[i + 1]:
            mu = list(L)
            mu[i] -= 1
            if mu[i] == 0:
                mu = mu[:i]
            content = (L[i] - 1) - i
            out.append((tuple(mu), content, i))
    return out


def per_edge_ratios():
    """Print per-edge ratio y_λ/(z·y_μ) for every Bratteli edge in witness."""
    print(f"{'n+1':>3} {'λ':>14} {'μ':>14} {'c':>3} {'y_λ/(z·y_μ)':>16}")
    for n in range(2, 12):
        if str(n + 1) not in W["tables_by_n"]:
            continue
        for ww in W["tables_by_n"][str(n + 1)]["weights"]:
            lam = tuple(ww["partition"])
            for mu, c, _row in removable_corners(lam):
                if (n, mu) not in yl or (n + 1, lam) not in yl:
                    continue
                y_lam = yl[(n + 1, lam)]
                y_mu = yl[(n, mu)]
                if y_mu == 0:
                    continue
                ratio = y_lam / (z * y_mu)
                print(f"{n+1:>3} {str(lam):>14} {str(mu):>14} {c:>+3} {float(ratio):>+16.10f}")


def plancherel_check():
    """Verify Σ y_λ · d_λ = 1 at every level."""
    from math import factorial as F

    def hook_dim(p):
        n = sum(p)
        pt = [sum(1 for r in p if r > c) for c in range(p[0])]
        prod = 1
        for i, ri in enumerate(p):
            for j in range(ri):
                h = (ri - j) + (pt[j] - i) - 1
                prod *= h
        return F(n) // prod

    print("\nPlancherel completeness Σ y_λ d_λ:")
    print(f"{'n':>3} {'Σ y_λ d_λ':>20}")
    for n_str in sorted(W["tables_by_n"], key=int):
        s = mp.mpf(0)
        for ww in W["tables_by_n"][n_str]["weights"]:
            d = hook_dim(ww["partition"])
            s += mp.mpf(str(ww["y_lambda"])) * d
        print(f"{n_str:>3} {float(s):>20.16f}")


if __name__ == "__main__":
    per_edge_ratios()
    plancherel_check()
