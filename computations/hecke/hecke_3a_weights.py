#!/usr/bin/env python3
"""
H_{3A} Wedderburn weights — full partition sum λ ⊢ 3A.

The atom braid has 3A strands (A = Z + N nucleons × 3 quarks each), so the
ambient Iwahori–Hecke algebra is H_{3A}(q), not H_3(q) per generator.

The biggest binding-accuracy win (per handover notes) is replacing the
per-generator V_full (built from H_3 weights) with the full sum over
λ ⊢ 3A partitions, weighted by w_λ(q) = d_q(λ)² / [3A]_q! at H_{3A}.
The DEFAULT path is exhaustive enumeration — no Plancherel truncation.

A Plancherel-bounded enumerator is retained as an OPTIONAL tool
(``shape_cap`` / ``plancherel_topn``) for performance audits only; it is
NOT used by default.  For heavy atoms the full enumeration is delegated
to upstream callers that have access to symbolic-in-q / CRT machinery.

Public API
----------
partitions_of_n(n)                   → list of all partitions λ ⊢ n
wedderburn_weights_3a(A)             → list of (λ, w_λ, d_λ) for H_{3A}
                                       (full enumeration, default)
plancherel_topn(n, top_n, shape_cap) → OPTIONAL truncated enumerator
                                       (top-N dominant partitions only —
                                       not canonical, use for diagnostics)
normalization_3a(A)                  → Σ w_λ over all λ ⊢ 3A
dominant_shape(n)                    → partition with maximal w_λ

Caching on disk (.cache/) keyed by (n, top_n, shape_cap).
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 4, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import math
import json
import sys
import hashlib
from pathlib import Path
from typing import Iterable

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0, Q_INV as QI, HA as HA_VAL  # noqa: F401
from partition_utils import hook_lengths  # noqa: E402


# ── Partition generation ──────────────────────────────────────────────

def partitions_of_n(n: int) -> list[tuple[int, ...]]:
    """All partitions of n (descending), deterministic order."""
    if n == 0:
        return [()]
    out: list[tuple[int, ...]] = []

    def rec(rem: int, mx: int, cur: list[int]) -> None:
        if rem == 0:
            out.append(tuple(cur))
            return
        for p in range(min(rem, mx), 0, -1):
            rec(rem - p, p, cur + [p])

    rec(n, n, [])
    return out


def partitions_bounded(n: int, max_part: int, max_length: int):
    """Partitions of n with λ₁ ≤ max_part and length ≤ max_length.

    Enables Plancherel-neighbourhood enumeration for large n: the
    Plancherel measure concentrates near λ₁ ∼ 2√n (Vershik–Kerov /
    Logan–Shepp limit shape), so bounding both λ₁ and length by a
    small multiple of √n captures the dominant contribution.
    """
    if n == 0:
        yield ()
        return

    def rec(rem: int, mx: int, depth: int, cur: list[int]):
        if depth > max_length:
            return
        if rem == 0:
            yield tuple(cur)
            return
        top = min(rem, mx, max_part)
        for p in range(top, 0, -1):
            yield from rec(rem - p, p, depth + 1, cur + [p])

    yield from rec(n, max_part, 0, [])


# ── q-arithmetic (floats; mpmath not needed for top-N sorting) ────────

def q_int(k: int) -> float:
    """q-integer [k]_q at the pinned q₀."""
    if k == 0:
        return 0.0
    return (Q0 ** k - QI ** k) / (Q0 - QI)


_QFAC_CACHE: dict[int, float] = {0: 1.0}


def q_fact(n: int) -> float:
    if n in _QFAC_CACHE:
        return _QFAC_CACHE[n]
    r = q_fact(n - 1) * q_int(n)
    _QFAC_CACHE[n] = r
    return r


def classical_dim(shape: tuple[int, ...]) -> int:
    """d_λ = n!/∏ h_λ via hook-length formula."""
    n = sum(shape)
    if n == 0:
        return 1
    hks = hook_lengths(shape)
    num = math.factorial(n)
    den = 1
    for h in hks:
        den *= h
    return num // den


def q_dim(shape: tuple[int, ...]) -> float:
    """d_q(λ) = [n]_q! / ∏ [h]_q."""
    n = sum(shape)
    if n == 0:
        return 1.0
    hks = hook_lengths(shape)
    num = q_fact(n)
    den = 1.0
    for h in hks:
        den *= q_int(h)
    return num / den if abs(den) > 0 else 0.0


def wedderburn_weight(shape: tuple[int, ...]) -> float:
    """w_λ = d_q(λ)² / [n]_q!  (**symmetric Plancherel weight, not Markov-trace**).

    .. warning::
        This is the **symmetric Plancherel weight** (Hecke generalisation
        of f^λ / n!), NOT the Jones-Markov weight y_λ(q) needed for
        Markov-trace assembly at q ≠ 1.  The two coincide only at the
        classical Plancherel point q = 1.

        For Markov-trace contexts (the QOU paper's tr_M = Σ y_λ χ^λ
        at q = q_0), use `markov_weights_symbolic.solve_y_lambda(n)` or
        `wedderburn_jones_markov.y_lambda_at(n, q_val=q_0)` (numerical-
        q-from-start, ~3.8s at n=6, ~63s at n=9).

        Per docs/audits/2026-05-08-p3-h-3a-divergence.md, using this
        symmetric-Plancherel weight in a Markov-trace context produces
        the WRONG sum — for D it overstates Σ by ~3.5×; for ⁴He by ~8×.
    """
    n = sum(shape)
    if n == 0:
        return 1.0
    dq = q_dim(shape)
    return (dq * dq) / q_fact(n)


# ── Plancherel truncation ─────────────────────────────────────────────

def _plancherel_bound(n: int) -> int:
    """Shape-cap ≈ 2⌈√n⌉ + 2 (covers Plancherel limit shape + buffer)."""
    if n <= 0:
        return 1
    return max(3, 2 * int(math.isqrt(n)) + 2)


def plancherel_topn(n: int, top_n: int | None = None,
                     shape_cap: int | None = None,
                     full_below: int = 25):
    """Top-N partitions of n ordered by w_λ (descending).

    Strategy:
      - For n ≤ full_below: enumerate all p(n) partitions.
      - For n > full_below: enumerate λ with λ₁ ≤ shape_cap AND
        length ≤ shape_cap (default shape_cap = 2⌈√n⌉+2).  Captures
        the Plancherel-concentrated regime.

    Returns a list of dicts: [{"partition": λ, "w": w_λ, "d_cl": d_λ,
    "d_q": d_q(λ)}].  If top_n is given, truncates to that many.
    """
    if n < 0:
        return []
    if n <= full_below or shape_cap is None and n <= full_below:
        parts_iter: Iterable[tuple[int, ...]] = partitions_of_n(n)
    else:
        cap = shape_cap if shape_cap is not None else _plancherel_bound(n)
        parts_iter = partitions_bounded(n, cap, cap)

    entries: list[dict] = []
    for p in parts_iter:
        d_cl = classical_dim(p)
        if d_cl == 0:
            continue
        dq = q_dim(p)
        w = (dq * dq) / q_fact(n)
        entries.append({
            "partition": p,
            "d_cl": d_cl,
            "d_q": dq,
            "w": w,
        })
    # Descending by w (Plancherel dominant first)
    entries.sort(key=lambda e: -e["w"])
    if top_n is not None and top_n > 0:
        entries = entries[:top_n]
    return entries


def wedderburn_weights_3a(A: int, top_n: int | None = None,
                            shape_cap: int | None = None,
                            full_below: int = 10**9):
    """Wedderburn weights at H_{3A}(q): full enumeration λ ⊢ 3A.

    By default: exhaustive enumeration of all p(3A) partitions
    (no Plancherel truncation).  ``top_n`` and ``shape_cap`` are
    exposed only for optional performance audits, and should
    normally be left None.
    """
    return plancherel_topn(3 * A, top_n=top_n, shape_cap=shape_cap,
                             full_below=full_below)


def normalization_3a(A: int, top_n: int | None = None) -> float:
    """Σ w_λ over all λ ⊢ 3A (no truncation by default).

    Note: at q ≠ 1 this is NOT identically 1 — the Markov-trace
    normalization for Iwahori–Hecke uses a different normalization
    of w_λ.  This function simply reports Σ d_q(λ)² / [3A]_q!.
    """
    return sum(e["w"] for e in wedderburn_weights_3a(A, top_n=top_n))


def dominant_shape(n: int) -> tuple[int, ...]:
    """Partition of n with maximal w_λ (Plancherel mode)."""
    top = plancherel_topn(n, top_n=1)
    return top[0]["partition"] if top else ()


# ── Disk cache ───────────────────────────────────────────────────────

_CACHE_DIR = Path(__file__).parent / ".cache" / "hecke_3a_weights"


def _cache_key(n: int, top_n: int | None, shape_cap: int | None) -> str:
    raw = f"{Q0:.10f}|{n}|{top_n}|{shape_cap}".encode()
    return hashlib.sha1(raw).hexdigest()[:16]


def cached_weights_3a(A: int, top_n: int | None = 64,
                        shape_cap: int | None = None):
    """Disk-cached version of wedderburn_weights_3a."""
    _CACHE_DIR.mkdir(parents=True, exist_ok=True)
    key = _cache_key(3 * A, top_n, shape_cap)
    f = _CACHE_DIR / f"3A-{3 * A}-{key}.json"
    if f.exists():
        data = json.loads(f.read_text())
        # Re-hydrate tuples (JSON only has lists)
        for e in data:
            e["partition"] = tuple(e["partition"])
        return data
    data = wedderburn_weights_3a(A, top_n=top_n, shape_cap=shape_cap)
    # JSON-safe: convert tuples to lists
    payload = [
        {"partition": list(e["partition"]), "d_cl": e["d_cl"],
         "d_q": e["d_q"], "w": e["w"]}
        for e in data
    ]
    f.write_text(json.dumps(payload, indent=2))
    return data


# ── CLI ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser(
        description="H_{3A} Wedderburn weights — full enumeration")
    ap.add_argument("--A", type=int, default=4,
                    help="Nucleon count A = Z+N (so 3A partitions)")
    ap.add_argument("--top-n", type=int, default=None,
                    help="(optional audit) keep top-N by w_λ")
    ap.add_argument("--full-below", type=int, default=10**9,
                    help="(audit) Plancherel-bound path when 3A > this")
    args = ap.parse_args()

    n = 3 * args.A
    print(f"H_{{{n}}}(q) at q₀ = {Q0:.6f}")
    print(f"Plancherel bound: λ₁, len(λ) ≤ {_plancherel_bound(n)}")
    entries = wedderburn_weights_3a(args.A, top_n=args.top_n,
                                       full_below=args.full_below)
    total_w = sum(e["w"] for e in entries)
    print(f"top-{len(entries)} partitions of {n}:")
    print(f"  {'λ':<28} {'d_λ':>10} {'w_λ':>14}")
    for e in entries[:32]:
        print(f"  {str(e['partition']):<28} {e['d_cl']:>10d} "
              f"{e['w']:>14.6e}")
    print(f"  Σ w_λ (top-{len(entries)}) = {total_w:.6f}")
    if total_w < 0.99:
        miss = 1.0 - total_w
        print(f"  WARNING: top-N captures {total_w*100:.2f}%; "
              f"truncation error ~{miss:.2e}")
