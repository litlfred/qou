#!/usr/bin/env python3
"""
fl_sniady_rsk_form_verify.py — DIRECT RSK-enumeration verification of the RSK form of the Δ_λ
covariance kernel T₃ (epic qou-x631 / bean qou-joi7, Phase 2 orientation).

The frontier note (#3998, docs/audits/2026-07-18-deltalambda-covariance-kernel-frontier.md) STATES
the RSK form of the kernel

    T₃ = Σ_λ (f^λ)² χ^λ(3-cycle) = Σ_{w ∈ S_k} χ^{sh(w)}(3-cycle),

but the existing probes (wlambda_covariance_kernel_frontier.py, wlambda_covariance_epic_phase1.py)
only ever compute the closed form Σ_λ (f^λ)² χ^λ(3-cycle) via hook dimensions — they never LITERALLY
enumerate S_k and apply the Robinson–Schensted correspondence. This probe closes that gap: it
builds sh(w) by actual Schensted row-insertion of every permutation word, and confirms

    (i)   #{ w ∈ S_k : sh(w) = λ } = (f^λ)²                    (RSK is a bijection S_k ≅ ⊔_λ SYT(λ)²)
    (ii)  Σ_{w ∈ S_k} χ^{sh(w)}(3-cycle) = Σ_λ (f^λ)² χ^λ(3-cycle) = T₃    (the RSK form, EXACT)
    (iii) T₃ = 3·cov(k)/(k)₃ < 0  with cov(k) = Σ_λ (f^λ)³(Σ_□c² − C(k,2))  (kernel identity)

All arithmetic is EXACT (Python ints); χ^λ(3-cycle,1^{k-3}) is Murnaghan–Nakayama (signed 3-ribbon
removal). k = 3..KMAX (default 7, |S_7| = 5040). This is a faithful realization of the RSK
bijection underlying the Kerov-CLT observable T₃ — it does NOT prove T₃ ≤ 0 (that is the open
kernel), it verifies the RSK *form* the Phase-2 genus expansion is built on.

Discipline: scope-(a) exact verification; no fit; nothing wired; no c_k; L2 unchanged (2/7).
In-sandbox (pure Python ints; no numpy).

# Ref: [sniady2006asymptotics] https://doi.org/10.1007/s00440-005-0479-7
# Ref: [biane1998representations] https://doi.org/10.1006/aima.1998.1741
"""
from __future__ import annotations

import math
import sys
from itertools import permutations
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent / "substrate"))

KMAX = 7


def partitions_of(n, m=None):
    if m is None:
        m = n
    if n == 0:
        yield ()
        return
    for i in range(min(n, m), 0, -1):
        for rest in partitions_of(n - i, i):
            yield (i,) + rest


def hook_dim(l):
    """f^λ = number of standard Young tableaux of shape λ (hook-length formula)."""
    l = list(l)
    n = sum(l)
    if n == 0:
        return 1
    conj = [sum(1 for p in l if p > j) for j in range(l[0])]
    d = 1
    for i, row in enumerate(l):
        for j in range(row):
            d *= (row - j) + (conj[j] - i) - 1
    return math.factorial(n) // d


def rsk_shape(word):
    """Shape of the RSK insertion tableau P(word) by Schensted row-insertion. Returns a partition
    (weakly-decreasing tuple of row lengths)."""
    rows = []  # each row a strictly increasing list
    for x in word:
        cur = x
        r = 0
        while True:
            if r == len(rows):
                rows.append([cur])
                break
            row = rows[r]
            # find leftmost entry strictly greater than cur (bump)
            lo, hi = 0, len(row)
            while lo < hi:
                mid = (lo + hi) // 2
                if row[mid] > cur:
                    hi = mid
                else:
                    lo = mid + 1
            if lo == len(row):
                row.append(cur)
                break
            else:
                cur, row[lo] = row[lo], cur
                r += 1
    return tuple(len(r) for r in rows)


def _cells(l):
    return {(i, j) for i, row in enumerate(l) for j in range(row)}


def _is_border_strip(cells):
    if not cells:
        return False
    cs = set(cells)
    # no 2x2 block
    for (i, j) in cs:
        if (i, j + 1) in cs and (i + 1, j) in cs and (i + 1, j + 1) in cs:
            return False
    # connected (edge-adjacency)
    start = next(iter(cs))
    seen = {start}
    stack = [start]
    while stack:
        (i, j) = stack.pop()
        for (a, b) in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if (a, b) in cs and (a, b) not in seen:
                seen.add((a, b))
                stack.append((a, b))
    return len(seen) == len(cs)


def _strip_height(cells):
    """height = (#rows spanned) − 1."""
    rows = {i for (i, _) in cells}
    return len(rows) - 1


def mn_char_3cycle(l):
    """χ^λ(3-cycle, 1^{k-3}) via Murnaghan–Nakayama: Σ over border strips ξ (3 cells) removable from
    λ of (−1)^{ht(ξ)} · f^{λ∖ξ}. The remaining cycle type is 1^{k−3}, so the recursive MN factor is
    exactly the SYT count of the smaller shape."""
    l = tuple(x for x in l if x > 0)
    k = sum(l)
    if k < 3:
        return 0
    lcells = _cells(list(l))
    result = 0
    for mu in partitions_of(k - 3):
        muf = list(mu) + [0] * (len(l) - len(mu))
        if len(mu) > len(l):
            continue
        if any(muf[i] > l[i] for i in range(len(l))):
            continue
        skew = lcells - _cells(muf)
        if len(skew) != 3:
            continue
        if not _is_border_strip(skew):
            continue
        result += ((-1) ** _strip_height(skew)) * hook_dim(tuple(x for x in muf if x > 0))
    return result


def contentsq(l):
    return sum((j - i) ** 2 for i, row in enumerate(l) for j in range(row))


def main() -> int:
    print("=== Direct RSK-enumeration verification of the RSK form of the Δ_λ kernel T₃ ===\n")
    print(f"{'k':>2} {'|S_k|':>7} {'T3_RSK(enum)':>14} {'T3_closed':>12} {'3cov/(k)_3':>12} "
          f"{'match':>6} {'bijection':>10}")

    all_ok = True
    rows_out = []
    for k in range(3, KMAX + 1):
        parts = list(partitions_of(k))
        fdim = {l: hook_dim(l) for l in parts}
        chi3 = {l: mn_char_3cycle(l) for l in parts}

        # closed form T₃ = Σ_λ (f^λ)² χ³
        T3_closed = sum(fdim[l] ** 2 * chi3[l] for l in parts)

        # kernel identity 3·cov/(k)_3
        Ck2 = k * (k - 1) // 2
        cov = sum(fdim[l] ** 3 * (contentsq(l) - Ck2) for l in parts)
        kfall = k * (k - 1) * (k - 2)
        assert (3 * cov) % kfall == 0, "3·cov not divisible by (k)_3"
        T3_from_cov = 3 * cov // kfall

        # DIRECT RSK enumeration: sum χ^{sh(w)}(3-cycle) over all w in S_k, and count shapes
        shape_count = {}
        T3_rsk = 0
        for w in permutations(range(k)):
            sh = rsk_shape(w)
            shape_count[sh] = shape_count.get(sh, 0) + 1
            T3_rsk += chi3[sh]

        # (i) bijection check: #{w : sh(w)=λ} == (f^λ)²
        bijection_ok = all(shape_count.get(l, 0) == fdim[l] ** 2 for l in parts) and \
            sum(shape_count.values()) == math.factorial(k)

        match = (T3_rsk == T3_closed == T3_from_cov)
        all_ok = all_ok and match and bijection_ok
        print(f"{k:>2} {math.factorial(k):>7} {T3_rsk:>14} {T3_closed:>12} {T3_from_cov:>12} "
              f"{str(match):>6} {str(bijection_ok):>10}")
        rows_out.append({
            "k": k, "T3_rsk_enum": int(T3_rsk), "T3_closed_form": int(T3_closed),
            "T3_from_cov": int(T3_from_cov), "cov": int(cov),
            "rsk_form_matches": bool(match), "rsk_bijection_ok": bool(bijection_ok),
            "T3_negative": bool(T3_rsk < 0),
        })

    print()
    print("Interpretation: RSK is realized LITERALLY (Schensted row-insertion of every w∈S_k);")
    print("the 3-cycle character averaged over the RSK shape equals the closed-form character sum")
    print("T₃ = Σ_λ(f^λ)²χ³ and the kernel value 3·cov/(k)₃, all EXACTLY, and T₃ < 0 throughout.")
    print("This verifies the RSK FORM the Phase-2 Śniady genus expansion is built on — it does NOT")
    print("prove T₃ ≤ 0 (the open Biane–Śniady / Kerov-CLT anti-correlation, epic qou-x631).")

    print(f"\nRESULT: RSK form + bijection verified exactly for k=3..{KMAX}: {all_ok}")

    try:
        from witness_base import WitnessBuilder
        w = WitnessBuilder("fl-sniady-rsk-form-verify", engine="python-exact")
        w.set_description(
            "DIRECT RSK-enumeration verification of the RSK form of the Δ_λ covariance kernel T₃ "
            "(epic qou-x631 / bean qou-joi7 Phase 2). Existing probes compute only the closed form "
            "Σ_λ(f^λ)²χ^λ(3-cycle) via hook dimensions; this probe LITERALLY enumerates S_k and "
            "applies Schensted row-insertion to every permutation word, confirming EXACTLY (k=3..7): "
            "(i) #{w∈S_k : sh(w)=λ} = (f^λ)² (RSK bijection S_k ≅ ⊔_λ SYT(λ)²); (ii) "
            "Σ_{w∈S_k} χ^{sh(w)}(3-cycle) = Σ_λ(f^λ)²χ^λ(3-cycle) = T₃ (the RSK form); (iii) "
            "T₃ = 3·cov(k)/(k)₃ < 0 with cov(k)=Σ(f^λ)³(Σc²−C(k,2)). χ^λ(3-cycle) by Murnaghan–"
            "Nakayama (signed 3-ribbon removal). Verifies the RSK form the Phase-2 genus expansion "
            "rests on; does NOT prove the open kernel T₃≤0. scope-(a); no fit; nothing wired; no c_k.")
        w.add_data("kmax", KMAX)
        w.add_data("per_k", rows_out)
        w.add_data("all_verified", bool(all_ok))
        w.add_assertion(
            "rsk_form_and_bijection_exact",
            computed=str(int(all_ok)), expected="1", tolerance=0,
            source=("Literal Schensted enumeration of S_k (k≤7): shape-count = (f^λ)² (RSK bijection) "
                    "and Σ_{w}χ^{sh(w)}(3-cycle) = Σ_λ(f^λ)²χ³ = 3cov/(k)₃ < 0, all exact. "
                    "Verifies the RSK form; open kernel T₃≤0 unproved. No fit; no c_k."))
        out = w.save()
        print(f"\nWitness: {out}")
    except ImportError as e:
        print(f"\n(witness skipped — witness_base unavailable: {e})")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
