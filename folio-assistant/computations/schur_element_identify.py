#!/usr/bin/env python3
"""
Schur-element formula identification (NEGATIVE RESULT).

Tests several literature candidates for the Markov-trace Schur
elements y_λ on H_n(R, q) with parameter z = 1/(√q + 1/√q),
matching against the verified numerical witness at n=2,3,4.

Status: NONE of the 10 candidates implemented here match the witness
to better than ~10% relative error.  Either the convention used in
the paper differs from the candidate forms, or there is an additional
normalisation factor not captured by the formulas as written.  A
careful Geck–Pfeiffer / Lambropoulou reference lookup is needed to
pin down the correct convention.

This file documents the candidates as attempted; future work can
extend with additional formulas or correct a convention.

Convention check:
- σ_i^2 = (q - q^{-1}) σ_i + 1   (v-form of Hecke relation;
  σ has eigenvalues +q^{1/2} and -q^{-1/2})
- z = 1/(q^{1/2} + q^{-1/2}) (Birman-Wenzl Markov parameter)
- tr_M(1) = 1, tr_M(σ_i) = z

Cell content c(i,j) = j - i; hook h_λ(i,j) = (last col of row i) -
j + (last row of col j) - i + 1 (1-indexed).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp
mp.mp.dps = 50

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP


Q = Q_MP  # was f64 roundtrip
QI = 1 / Q
SQRTQ = mp.sqrt(Q)
ISQRTQ = 1 / SQRTQ
Z = 1 / (SQRTQ + ISQRTQ)
H = Q - QI


def q_int(k: int):
    """[k]_q = (q^k - q^{-k})/(q - q^{-1})."""
    if k == 0:
        return mp.mpf(0)
    return (Q ** k - Q ** (-k)) / H


def hook_lengths(partition):
    """Compute hook length of every cell (i, j) ∈ λ."""
    rows = len(partition)
    cols = max(partition) if rows else 0
    transpose = [
        sum(1 for r in range(rows) if partition[r] > c)
        for c in range(cols)
    ]
    return {
        (i, j): (partition[i] - j - 1) + (transpose[j] - i - 1) + 1
        for i in range(rows)
        for j in range(partition[i])
    }


def content(i: int, j: int) -> int:
    return j - i


def candidate_A(partition):
    """A: y_λ = ∏ (q^c - z^{-1}) / [h]_q."""
    hooks = hook_lengths(partition)
    prod = mp.mpf(1)
    for (i, j), h in hooks.items():
        c = content(i, j)
        prod *= (Q ** c - 1 / Z) / q_int(h)
    return prod


def candidate_B(partition):
    """B: y_λ = ∏ (z q^c - 1) / (z [h]_q)."""
    hooks = hook_lengths(partition)
    prod = mp.mpf(1)
    for (i, j), h in hooks.items():
        c = content(i, j)
        prod *= (Z * Q ** c - 1) / (Z * q_int(h))
    return prod


def candidate_C(partition):
    """C: y_λ = ∏ (q^c - z) / (z [h]_q)  (Lambropoulou 1994 form)."""
    hooks = hook_lengths(partition)
    prod = mp.mpf(1)
    for (i, j), h in hooks.items():
        c = content(i, j)
        prod *= (Q ** c - Z) / (Z * q_int(h))
    return prod


def candidate_D(partition):
    """D: y_λ = ∏ (z - q^{-c-1}) / [h]_q."""
    hooks = hook_lengths(partition)
    prod = mp.mpf(1)
    for (i, j), h in hooks.items():
        c = content(i, j)
        prod *= (Z - Q ** (-c - 1)) / q_int(h)
    return prod


def candidate_E(partition):
    """E: y_λ = ∏ (q^{c+1} (1-z) - q^c + z) / [h]_q  (Geck-Pfeiffer-style)."""
    hooks = hook_lengths(partition)
    prod = mp.mpf(1)
    for (i, j), h in hooks.items():
        c = content(i, j)
        num = Q ** (c + 1) * (1 - Z) - Q ** c + Z
        prod *= num / q_int(h)
    return prod


def candidate_F(partition):
    """F: y_λ = z^n · ∏ (q^c - z^{-1}) / [h]_q  (with z^n prefactor)."""
    n = sum(partition)
    hooks = hook_lengths(partition)
    prod = Z ** n
    for (i, j), h in hooks.items():
        c = content(i, j)
        prod *= (Q ** c - 1 / Z) / q_int(h)
    return prod


def candidate_G(partition):
    """G: y_λ = ∏ (q^{c} z + q^{-c} z) / ([h]_q · (z + 1/z))^? — wild guess."""
    hooks = hook_lengths(partition)
    prod = mp.mpf(1)
    for (i, j), h in hooks.items():
        c = content(i, j)
        prod *= (Q ** c * Z + Q ** (-c) * Z) / q_int(h)
    return prod


def candidate_H(partition):
    """H: y_λ = ∏ (1 - z q^c) (1 - z q^{-c}) / [h]_q^2."""
    hooks = hook_lengths(partition)
    prod = mp.mpf(1)
    for (i, j), h in hooks.items():
        c = content(i, j)
        num = (1 - Z * Q ** c) * (1 - Z * Q ** (-c))
        prod *= num / q_int(h) ** 2
    return prod


def candidate_I(partition):
    """I: Geck-Pfeiffer 9.4.1 form for type A:
       y_λ = ∏ (q^{c} z^{-1/n}? ... no, try:
       y_λ = q^{n(λ)} z^n ∏ (1 - z q^{c}) / [h]_q where n(λ) = Σ (i)·partition[i]."""
    n = sum(partition)
    hooks = hook_lengths(partition)
    n_lambda = sum(i * partition[i] for i in range(len(partition)))
    prod = Q ** n_lambda * Z ** n
    for (i, j), h in hooks.items():
        c = content(i, j)
        prod *= (1 - Z * Q ** c) / q_int(h)
    return prod


def candidate_J(partition):
    """J: y_λ = (z (q-1))^n / ∏(1 - q^{c+1} z + ?)
       Try: y_λ = ∏ ((1-z)q^c + z q^{c+1}) / [h]_q^2 — exotic form."""
    hooks = hook_lengths(partition)
    prod = mp.mpf(1)
    for (i, j), h in hooks.items():
        c = content(i, j)
        num = (1 - Z) * Q ** c + Z * Q ** (c + 1)
        prod *= num / q_int(h) ** 2
    return prod


CANDIDATES = {
    "A: ∏(q^c - z⁻¹)/[h]_q": candidate_A,
    "B: ∏(zq^c - 1)/(z[h]_q)": candidate_B,
    "C: ∏(q^c - z)/(z[h]_q)": candidate_C,
    "D: ∏(z - q^{-c-1})/[h]_q": candidate_D,
    "E: ∏(q^{c+1}(1-z) - q^c + z)/[h]_q": candidate_E,
    "F: z^n · ∏(q^c - z⁻¹)/[h]_q": candidate_F,
    "G: ∏(zq^c + zq^{-c})/[h]_q": candidate_G,
    "H: ∏(1-zq^c)(1-zq^{-c})/[h]_q²": candidate_H,
    "I: q^{n(λ)} z^n · ∏(1-zq^c)/[h]_q": candidate_I,
    "J: ∏((1-z)q^c + zq^{c+1})/[h]_q²": candidate_J,
}


GROUND_TRUTH = {
    (2,):           mp.mpf("0.6963254203"),
    (1, 1):         mp.mpf("0.3036745797"),
    (3,):           mp.mpf("0.4153957863"),
    (2, 1):         mp.mpf("0.2809296340"),
    (1, 1, 1):      mp.mpf("0.0227449457"),
    (4,):           mp.mpf("0.2275269302"),
    (3, 1):         mp.mpf("0.1878688561"),
    (2, 2):         mp.mpf("0.0694733046"),
    (2, 1, 1):      mp.mpf("0.0235874732"),
    (1, 1, 1, 1):   mp.mpf("-0.0008425275"),
}


def main():
    print(f"q_0 = {float(Q):.16f}, z = {float(Z):.10f}")
    print(f"Testing {len(CANDIDATES)} candidate Schur-element formulas\n")

    print(f"{'partition':<14} ", end="")
    for name in CANDIDATES:
        print(f"{name[:25]:<27}", end="")
    print()
    print(f"{'(truth)':<14} ", end="")
    for _ in CANDIDATES:
        print(f"{'|diff|':<27}", end="")
    print()
    print("-" * (14 + 27 * len(CANDIDATES)))

    matches = {name: 0 for name in CANDIDATES}
    for partition, truth in GROUND_TRUTH.items():
        print(f"{str(partition):<14} ", end="")
        for name, formula in CANDIDATES.items():
            val = formula(list(partition))
            diff = abs(val - truth)
            relative = abs(diff / truth) if truth != 0 else diff
            print(f"  {float(diff):.2e} (r={float(relative):.1e})", end="  ")
            if relative < mp.mpf("1e-10"):
                matches[name] += 1
        print()

    print()
    print("Match counts (out of {}): ".format(len(GROUND_TRUTH)))
    for name, count in sorted(matches.items(), key=lambda kv: -kv[1]):
        marker = " ← MATCH" if count == len(GROUND_TRUTH) else ""
        print(f"  {name:<40}: {count}{marker}")


if __name__ == "__main__":
    main()
