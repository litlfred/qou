#!/usr/bin/env python3
"""LR-fusion self-conjugacy test for the magic-shell rank-collapse
conjecture (conj:sdp-rank-collapse-magic-shell).

For each canonical self-conjugate partition lambda of n in {magic,
non-magic}, computes the dominant LR-fusion product
  V_lambda (x) V_lambda
and reports whether the dominant nu (max c^nu_{lambda, lambda}) is
itself self-conjugate. The conjecture predicts: yes at magic n,
no at non-magic n.

Implementation: Yamanouchi (LR) skew-tableau enumeration.
Brute-force; tractable for n <= ~15 (giving lambda otimes lambda of
size <= 30).

Run as:
    python3 lr_fusion_self_conj_test.py [n ...]

If no n is supplied, runs on small magic + non-magic.
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
from typing import List, Tuple, Iterator, Optional

sys.path.insert(0, ".")
from enumerate_self_conjugate_partitions import (  # noqa: E402
    canonical_self_conjugate,
    conjugate_partition,
    content_sum,
)


def partitions_of(n: int, max_first: Optional[int] = None) -> List[List[int]]:
    """All partitions of n in decreasing order, optionally bounded
    by max_first."""
    if max_first is None:
        max_first = n
    out = []

    def go(remaining: int, max_part: int, current: List[int]) -> None:
        if remaining == 0:
            out.append(list(current))
            return
        start = min(max_part, remaining)
        for k in range(start, 0, -1):
            current.append(k)
            go(remaining - k, k, current)
            current.pop()

    go(n, max_first, [])
    return out


def skew_cells(nu: List[int], lam: List[int]) -> List[Tuple[int, int]]:
    """Cells (i, j) in nu but not in lam, 1-indexed."""
    cells = []
    for i, length in enumerate(nu, start=1):
        lam_i = lam[i - 1] if i - 1 < len(lam) else 0
        for j in range(lam_i + 1, length + 1):
            cells.append((i, j))
    return cells


def is_subdiagram(lam: List[int], nu: List[int]) -> bool:
    """Is lam contained in nu (cell-wise)?"""
    if len(lam) > len(nu):
        return False
    return all(lam[i] <= nu[i] for i in range(len(lam)))


def count_lr_tableaux(nu: List[int], lam: List[int], mu: List[int]) -> int:
    """Count Littlewood-Richardson tableaux of shape nu/lam and
    weight mu. Yamanouchi condition: reading right-to-left top-to-
    bottom, every prefix has #i >= #(i+1) for all i.
    """
    if not is_subdiagram(lam, nu):
        return 0
    cells = skew_cells(nu, lam)
    if len(cells) != sum(mu):
        return 0
    # Reading order: top-to-bottom, right-to-left within each row.
    cells_sorted = sorted(cells, key=lambda c: (c[0], -c[1]))
    n_letters = len(mu)

    # Backtracking
    count = [0]

    def backtrack(idx: int, filling: dict, used_per_letter: List[int]) -> None:
        if idx == len(cells_sorted):
            # Verify weight matches mu
            if used_per_letter == list(mu):
                count[0] += 1
            return
        i, j = cells_sorted[idx]
        for letter in range(1, n_letters + 1):
            # Weight constraint: at most mu[letter-1]
            if used_per_letter[letter - 1] >= mu[letter - 1]:
                continue
            # Row weakly increasing: cell to left must have <= letter
            if j > 1 and filling.get((i, j - 1), 0) > letter:
                # Note: filling.get returns 0 for empty/uninserted cells;
                # but cell (i, j-1) is in the skew shape only if it's not
                # in lam. If j-1 <= lam_{i-1} then cell is in lam and we
                # don't constrain.
                pass
            lam_i = lam[i - 1] if i - 1 < len(lam) else 0
            if j > lam_i + 1:
                left_letter = filling.get((i, j - 1))
                if left_letter is not None and left_letter > letter:
                    continue
            # Column strictly increasing: cell above must have < letter
            if i > 1:
                above_letter = filling.get((i - 1, j))
                if above_letter is not None and above_letter >= letter:
                    continue
            # Yamanouchi: every prefix must have #k >= #(k+1).
            # Since we fill cells in reading order, used_per_letter
            # already tracks prefix counts. Adding `letter` would
            # bring its count to used_per_letter[letter-1] + 1; that
            # must not exceed used_per_letter[letter-2] (the count
            # of the preceding letter in the alphabet). For
            # letter == 1 the constraint is vacuous.
            if letter > 1 and used_per_letter[letter - 1] + 1 > used_per_letter[letter - 2]:
                continue
            # Recurse
            filling[(i, j)] = letter
            used_per_letter[letter - 1] += 1
            backtrack(idx + 1, filling, used_per_letter)
            del filling[(i, j)]
            used_per_letter[letter - 1] -= 1

    backtrack(0, {}, [0] * n_letters)
    return count[0]


def lr_decomposition(lam: List[int], mu: List[int],
                      max_partitions: int = 200
                     ) -> List[Tuple[List[int], int]]:
    """All (nu, c) with c = c^nu_{lam, mu} > 0.
    Returns list sorted by c descending."""
    n = sum(lam) + sum(mu)
    out = []
    parts = partitions_of(n, max_first=lam[0] + mu[0] if lam and mu else n)
    if len(parts) > max_partitions:
        # Trim to nu's that contain lam (most lr coeffs are zero anyway)
        parts = [p for p in parts if is_subdiagram(lam, p)]
        parts = parts[:max_partitions]
    for nu in parts:
        c = count_lr_tableaux(nu, lam, mu)
        if c > 0:
            out.append((nu, c))
    out.sort(key=lambda x: -x[1])
    return out


def test_self_conjugacy_at_magic_shell(
    targets: Optional[List[int]] = None,
    timeout_per_n: float = 60.0,
) -> dict:
    """For each n in targets, take the canonical self-conjugate
    lambda |- n, compute the LR self-fusion lambda (x) lambda, and
    check whether the dominant nu is also self-conjugate."""
    magic = [8, 20, 28]  # bigger magic n are intractable here
    nonmagic = [12, 16]

    if targets is None:
        targets = sorted(magic + nonmagic)

    report = {}
    for n in targets:
        canonical, count = canonical_self_conjugate(n)
        if not canonical:
            report[n] = {
                "n": n,
                "canonical": None,
                "skipped": "no self-conjugate (degenerate)",
            }
            print(f"n={n}: degenerate (no self-conjugate)")
            continue

        is_magic = n in magic
        print(f"n={n} (magic={is_magic}): canonical lambda = {canonical}")
        print(f"  Computing LR decomposition lambda (x) lambda ...")
        t0 = time.time()
        try:
            decomp = lr_decomposition(canonical, canonical, max_partitions=500)
            elapsed = time.time() - t0
        except Exception as e:
            report[n] = {
                "n": n,
                "canonical": canonical,
                "error": str(e),
            }
            print(f"  ERROR: {e}")
            continue

        if elapsed > timeout_per_n:
            print(f"  WARNING: took {elapsed:.1f}s")

        if not decomp:
            report[n] = {
                "n": n,
                "canonical": canonical,
                "decomposition": [],
                "error": "empty decomposition",
            }
            print(f"  empty decomposition!")
            continue

        dominant_nu, dominant_c = decomp[0]
        is_dom_self_conj = dominant_nu == conjugate_partition(dominant_nu)
        print(
            f"  dominant nu = {dominant_nu} (c = {dominant_c},"
            f" self-conj = {is_dom_self_conj}), {elapsed:.2f}s"
        )
        # Top 5 components for context
        for nu, c in decomp[:5]:
            sc = nu == conjugate_partition(nu)
            print(f"    {nu}: c={c}{' [self-conj]' if sc else ''}")

        report[n] = {
            "n": n,
            "magic": is_magic,
            "canonical": canonical,
            "dominant_nu": dominant_nu,
            "dominant_c": dominant_c,
            "dominant_is_self_conjugate": is_dom_self_conj,
            "top_5": [
                {
                    "nu": nu,
                    "c": c,
                    "is_self_conj": nu == conjugate_partition(nu),
                }
                for nu, c in decomp[:5]
            ],
            "elapsed_sec": elapsed,
        }

    print()
    print("Summary:")
    for n, r in report.items():
        if "dominant_is_self_conjugate" in r:
            print(
                f"  n={n} ({'magic' if r['magic'] else 'non-magic'}):"
                f" dominant nu self-conj = {r['dominant_is_self_conjugate']}"
            )

    # Pattern check
    magic_results = [
        r["dominant_is_self_conjugate"]
        for r in report.values()
        if r.get("magic") and "dominant_is_self_conjugate" in r
    ]
    nonmagic_results = [
        r["dominant_is_self_conjugate"]
        for r in report.values()
        if r.get("magic") is False and "dominant_is_self_conjugate" in r
    ]
    print()
    print(f"Magic n with self-conj dominant: {sum(magic_results)}/{len(magic_results)}")
    print(
        f"Non-magic n with self-conj dominant: "
        f"{sum(nonmagic_results)}/{len(nonmagic_results)}"
    )
    if all(magic_results) and not any(nonmagic_results):
        print("=> Hypothesis SUPPORTED: self-conj dominance is magic-exclusive.")
    else:
        print("=> Hypothesis NOT supported (check non-trivial counter-examples).")

    return report


if __name__ == "__main__":
    targets = [int(a) for a in sys.argv[1:]] if len(sys.argv) > 1 else None
    report = test_self_conjugacy_at_magic_shell(targets)

    # ── Witness emission ─────────────────────────────────────────
    from witness_base import WitnessBuilder  # noqa: E402

    w = WitnessBuilder("lr-fusion-self-conj-test", engine="python")
    w.set_description(
        "LR-fusion self-conjugacy test for the magic-shell "
        "rank-collapse conjecture: at magic n, the dominant ν in "
        "V_λ ⊗ V_λ (canonical self-conjugate λ ⊢ n) is itself "
        "self-conjugate; predicted to fail at non-magic n."
    )
    w.set_content_block("conj:diagrammatic-double-magic-lr-fusion")

    magic_total = sum(
        1 for r in report.values()
        if r.get("magic") and "dominant_is_self_conjugate" in r
    )
    magic_self = sum(
        1 for r in report.values()
        if r.get("magic") and r.get("dominant_is_self_conjugate")
    )
    nonmagic_total = sum(
        1 for r in report.values()
        if r.get("magic") is False and "dominant_is_self_conjugate" in r
    )
    nonmagic_self = sum(
        1 for r in report.values()
        if r.get("magic") is False and r.get("dominant_is_self_conjugate")
    )

    w.add_parameter("targets", targets if targets else "default")
    w.add_parameter("magic_count", magic_total)
    w.add_parameter("nonmagic_count", nonmagic_total)
    w.add_data(
        "per_n",
        {
            str(n): {
                "magic": r.get("magic"),
                "canonical": r.get("canonical"),
                "dominant_nu": r.get("dominant_nu"),
                "dominant_c": r.get("dominant_c"),
                "dominant_is_self_conjugate":
                    r.get("dominant_is_self_conjugate"),
            }
            for n, r in report.items()
        },
    )
    w.add_data(
        "summary",
        {
            "magic_self_conj_dominant": magic_self,
            "magic_total_tested": magic_total,
            "nonmagic_self_conj_dominant": nonmagic_self,
            "nonmagic_total_tested": nonmagic_total,
            "hypothesis_supported": (
                magic_total > 0
                and magic_self == magic_total
                and nonmagic_self == 0
            ),
        },
    )
    # Sanity-only assertion: every entry produced a result OR was
    # explicitly skipped.
    accounted = sum(
        1 for r in report.values()
        if "dominant_is_self_conjugate" in r or "skipped" in r
    )
    w.add_assertion(
        "All targets accounted for (computed or skipped)",
        computed=accounted,
        expected=len(report),
        tolerance=0,
    )
    w.save()
