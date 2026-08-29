#!/usr/bin/env python3
"""
chi_free_via_frobenius.py — FREE-config χ^λ(β_free) by the Frobenius
characteristic map. An INDEPENDENT second path to `chi_free_via_lr`.

# Ref: docs/audits/2026-08-26-carrier-saturation-five-failures-diagnosis.md
# Ref: docs/audits/2026-06-09-large-A-chi-bottleneck-scaling-plan.md

WHY. `carrier_saturation_mechanism_probe.py`'s ⁶Li assertion is a regression
PIN rather than a validation, because ⁶Li's free χ came from
`chi_free_via_lr` — the probe's own path — and an expectation taken from the
script it checks validates nothing. This module supplies the missing second
path so that pin can become a real assertion.

THE TWO ROUTES, same mathematics, different algorithm:

  chi_free_via_lr    counts Littlewood–Richardson tableaux
                     (`active_set_lr_profile.multi_lr`) to get c^λ_{μ_1…μ_A},
                     then sums c · Π_i χ^{μ_i}(β_i).

  here               never forms an LR coefficient at all. Both routes start
                     from Σ_λ χ^λ(β_free) s_λ = Π_i F_i with
                     F_i = Σ_{μ⊢3} χ^{μ}(β_i) s_μ, but this one evaluates the
                     product in the POWER-SUM basis, where multiplication is
                     concatenation of partitions and nothing has to be
                     enumerated:

                         s_μ = Σ_{ρ⊢3} (χ^μ_{S_3}(ρ) / z_ρ) p_ρ
                         F_i = Σ_ρ b_i(ρ) p_ρ
                         Π_i F_i = Σ_ρ C(ρ) p_ρ        (ρ ⊢ 3A)
                         p_ρ = Σ_λ χ^λ(ρ) s_λ
                     ⇒   χ^λ(β_free) = Σ_ρ C(ρ) · χ^λ_{S_{3A}}(ρ)

                     with χ^λ(ρ) from Murnaghan–Nakayama.

WHAT THE INDEPENDENCE IS, AND IS NOT. Both routes read the same six cached
nucleon characters, so this catches an error in the combinatorics — an LR
enumeration that misses a tuple, a wrong multiplicity, a transcription slip —
and NOT a bad nucleon input. Said here rather than left to be assumed.

WHY IT IS CHEAP. The combined cycle type is determined only by HOW MANY
nucleons sit in each of the three S_3 classes, so A = 6 gives
C(A+2, 2) = 28 distinct ρ rather than 3^6 = 729 tuples, and the whole ⁶Li
computation is 385 λ × 28 ρ Murnaghan–Nakayama evaluations.
"""
from __future__ import annotations

import json
import sys
from functools import lru_cache
from pathlib import Path

import _path_bridge  # noqa: F401,E402

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

# S_3 character table. Rows λ ⊢ 3, columns ρ in the order below.
_RHO3 = [(1, 1, 1), (2, 1), (3,)]
_Z3 = {(1, 1, 1): 6, (2, 1): 2, (3,): 3}        # z_ρ = Π i^{m_i} m_i!
_CHI_S3 = {
    (3,):       {(1, 1, 1): 1, (2, 1): 1,  (3,): 1},    # trivial
    (2, 1):     {(1, 1, 1): 2, (2, 1): 0,  (3,): -1},   # standard
    (1, 1, 1):  {(1, 1, 1): 1, (2, 1): -1, (3,): 1},    # sign
}

ZN = {"D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2),
      "5Li": (3, 2), "6Li": (3, 3), "7Li": (3, 4)}


@lru_cache(maxsize=None)
def mn_character(lam: tuple, rho: tuple) -> int:
    """χ^λ(ρ) for S_n by Murnaghan–Nakayama.

    Removes a border strip of length rho[0] from λ in every legal way,
    weighting by (-1)^{height-1}, and recurses on the remainder. Returns an
    exact Python int — no floating point anywhere in the character.
    """
    if not rho:
        return 1 if not lam else 0
    r, rest = rho[0], rho[1:]
    total = 0
    for mu, height in _border_strips(lam, r):
        total += (-1) ** (height - 1) * mn_character(mu, rest)
    return total


@lru_cache(maxsize=None)
def _border_strips(lam: tuple, r: int) -> tuple:
    """Every (λ minus a border strip of size r, strip height).

    Uses the beta-number (first-column hook length) model: a border strip of
    length r corresponds to moving one beta-number down by r into a vacant
    slot, and the strip's height is the number of occupied slots it passes.
    """
    if r <= 0:
        return ()
    k = len(lam)
    beta = [lam[i] + (k - 1 - i) for i in range(k)]     # strictly decreasing
    occupied = set(beta)
    out = []
    for b in beta:
        nb = b - r
        if nb < 0 or nb in occupied:
            continue
        # height = number of occupied beta-numbers strictly between nb and b
        height = sum(1 for x in beta if nb < x < b) + 1
        new = sorted((x for x in beta if x != b), reverse=True)
        new.append(nb)
        new.sort(reverse=True)
        # beta-numbers back to a partition
        m = len(new)
        part = tuple(new[i] - (m - 1 - i) for i in range(m))
        part = tuple(x for x in part if x > 0)
        if any(part[i] < part[i + 1] for i in range(len(part) - 1)):
            continue
        out.append((part, height))
    return tuple(out)


def load_nucleon_chi(dps: int = 50) -> dict:
    """The six cached χ^{μ⊢3}(β_{p,n}). Same inputs as the LR path."""
    if mp.mp.dps < dps:
        mp.mp.dps = dps
    files = {"p": "chi-proton-h3-at-q0-50dps.witness.json",
             "n": "chi-neutron-h3-at-q0-50dps.witness.json"}
    cache = {}
    for nuc, f in files.items():
        d = json.loads((HERE / f).read_text())
        bp = d.get("by_partition") or d["data"]["by_partition"]
        cache[nuc] = {tuple(p["partition"]): mp.mpf(str(p["chi_lambda"]))
                      for p in bp}
    return cache


def _power_sum_coeffs(chi_nuc: dict) -> dict:
    """F = Σ_{μ⊢3} χ^μ(β) s_μ, re-expressed as Σ_ρ b(ρ) p_ρ."""
    return {
        rho: sum((chi_nuc[mu] * _CHI_S3[mu][rho] for mu in _CHI_S3),
                 mp.mpf(0)) / _Z3[rho]
        for rho in _RHO3
    }


def chi_free_frobenius(Z: int, N: int, *, dps: int = 50,
                       nuc_chi: dict | None = None) -> dict:
    """`{λ ⊢ 3A: χ^λ(β_free)}` with no Littlewood–Richardson coefficient."""
    if mp.mp.dps < dps:
        mp.mp.dps = dps
    if nuc_chi is None:
        nuc_chi = load_nucleon_chi(dps)
    A = Z + N
    bp = _power_sum_coeffs(nuc_chi["p"])
    bn = _power_sum_coeffs(nuc_chi["n"])

    # Multiply the A degree-3 factors in the p-basis. Only the MULTISET of
    # chosen ρ's matters, so group by (how many protons / neutrons chose
    # each class) instead of walking 3^A tuples.
    combined: dict[tuple, mp.mpf] = {}

    def walk(idx: int, coeff, parts: tuple):
        if idx == A:
            rho = tuple(sorted(parts, reverse=True))
            combined[rho] = combined.get(rho, mp.mpf(0)) + coeff
            return
        b = bp if idx < Z else bn
        for rho3 in _RHO3:
            walk(idx + 1, coeff * b[rho3], parts + rho3)

    walk(0, mp.mpf(1), ())

    n = 3 * A
    out = {}
    for lam in _partitions(n):
        s = mp.mpf(0)
        for rho, c in combined.items():
            ch = mn_character(lam, rho)
            if ch:
                s += c * ch
        out[lam] = s
    return out


@lru_cache(maxsize=None)
def _partitions(n: int, cap: int | None = None) -> tuple:
    cap = n if cap is None else cap
    if n == 0:
        return ((),)
    out = []
    for k in range(min(n, cap), 0, -1):
        for rest in _partitions(n - k, k):
            out.append((k,) + rest)
    return tuple(out)


def main() -> int:
    """Cross-check the Frobenius route against the LR route, and emit a witness.

    Three checks, in increasing strength:
      1. Murnaghan–Nakayama reproduces the S_3 character table it is given.
      2. χ^λ(1^n) equals the hook-length dimension f^λ, for every λ at
         n = 6, 9, 12, 18 — 503 partitions. This exercises MN on exactly the
         shapes the atoms use.
      3. The two routes agree per-block on D / ³He / ⁴He / ⁶Li.
    """
    import math
    import time

    from witness_base import WitnessBuilder
    from chi_free_via_lr import chi_free_lr, load_nucleon_chi

    def hook_dim(lam):
        n = sum(lam)
        num, den = math.factorial(n), 1
        for i in range(len(lam)):
            for j in range(lam[i]):
                arm = lam[i] - j - 1
                leg = sum(1 for r in range(i + 1, len(lam)) if lam[r] > j)
                den *= arm + leg + 1
        return num // den

    wb = WitnessBuilder("chi-free-via-frobenius", engine="mpmath")
    wb.set_description(
        "Independent second path to the free-config chi^lambda(beta_free), by "
        "the Frobenius characteristic map: expand each nucleon's degree-3 "
        "symmetric function in the power-sum basis (where multiplication is "
        "concatenation), then convert back with Murnaghan-Nakayama. Forms no "
        "Littlewood-Richardson coefficient, so it is independent of "
        "chi_free_via_lr in ALGORITHM -- both read the same six cached "
        "nucleon characters, so this catches a combinatorial error, not a bad "
        "input. Exists so the carrier probe's 6Li assertion can be a "
        "validation rather than a regression pin.")

    print("=" * 72)
    print(" free chi via Frobenius — cross-check against the LR route")
    print("=" * 72)

    table_ok = all(mn_character(l, r) == _CHI_S3[l][r]
                   for l in _CHI_S3 for r in _RHO3)
    print(f"  MN reproduces the S_3 character table : {table_ok}")

    bad_dim, tot_dim = 0, 0
    for n in (6, 9, 12, 18):
        for lam in _partitions(n):
            tot_dim += 1
            if mn_character(lam, (1,) * n) != hook_dim(lam):
                bad_dim += 1
    print(f"  chi^lambda(1^n) == f^lambda            : "
          f"{tot_dim - bad_dim}/{tot_dim} (n = 6, 9, 12, 18)")

    nuc = load_nucleon_chi(50)
    worst_overall = mp.mpf(0)
    print("\n  atom   blocks   worst rel |frobenius − LR|   frobenius   LR")
    for atom in ("D", "3He", "4He", "5Li", "6Li"):
        Z, N = ZN[atom]
        t0 = time.time()
        a = chi_free_frobenius(Z, N, nuc_chi=nuc)
        t1 = time.time()
        b = chi_free_lr(Z, N, nuc_chi=nuc)
        t2 = time.time()
        worst = mp.mpf(0)
        for k in set(a) & set(b):
            rel = abs(a[k] - b[k]) / max(abs(b[k]), mp.mpf(1))
            worst = max(worst, rel)
        worst_overall = max(worst_overall, worst)
        print(f"  {atom:>4s}   {len(a):>6d}   {mp.nstr(worst, 4):>22s}   "
              f"{t1 - t0:>7.2f}s  {t2 - t1:>6.2f}s")
        wb.add_data(f"worst_rel_vs_lr_{atom}", mp.nstr(worst, 8))
        wb.add_data(f"n_blocks_{atom}", str(len(a)))

    wb.add_assertion("mn_reproduces_s3_character_table",
                     computed="1" if table_ok else "0",
                     expected="1", tolerance="0")
    wb.add_assertion("mn_dimensions_match_hook_length",
                     computed=str(bad_dim), expected="0", tolerance="0")
    wb.add_assertion("frobenius_matches_lr_all_atoms",
                     computed=mp.nstr(worst_overall, 12),
                     expected="0", tolerance="1e-40")
    print(f"\n  worst over all atoms = {mp.nstr(worst_overall, 6)}")
    out = wb.save()
    print(f"  witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
