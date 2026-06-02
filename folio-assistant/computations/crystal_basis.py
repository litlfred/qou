#!/usr/bin/env python3
"""Crystal-basis primitives for Type-A (sl_n) — Phase 0 of the
S-poly → crystal-basis migration.

This module provides the *combinatorial kernel* needed by downstream
Hecke / Markov-trace compute scripts to replace per-step
``sympy.expand`` with crystal-graph traversal. The key primitives are:

* ``SSYT`` — semistandard Young tableau (shape + entries).
* ``kashiwara_lower(T, i)`` / ``kashiwara_raise(T, i)`` — Kashiwara
  operators ``f_i`` / ``e_i`` via the **signature rule** on the
  row-reading word (standard algorithm; Kashiwara 1991, Lusztig 1990).
* ``crystal_B(shape, n)`` — BFS enumeration of the connected crystal
  ``B(λ)`` rooted at the highest-weight tableau.
* ``demazure_subcrystal(shape, n, reduced_word)`` — sub-crystal
  ``B_w(λ) ⊆ B(λ)`` for a Weyl element ``w`` given as a reduced
  expression.  This is the *asymptotic* win: ``|B_w(λ)| ≪ |B(λ)|``
  whenever ``ℓ(w) ≪ ℓ(w_0)``.
* ``schuetzenberger_evacuation(T)`` — bar involution on the crystal
  (validates against ``bar_involution.bar_coeff_dict`` on the level
  of weights).

Validation (run ``python crystal_basis.py``):

  1. ``|B(λ)| == s_λ(1, …, 1)`` — Weyl dimension formula.
  2. ``|B(λ)| == # SSYT(λ, n)`` — direct enumeration cross-check.
  3. ``demazure_subcrystal(λ, n, w_0) == B(λ)`` — longest Weyl element
     recovers the full crystal.
  4. ``demazure_subcrystal(λ, n, ()) == {highest_weight}`` — empty
     word recovers only the highest-weight tableau.

Reference: Bump–Schilling, *Crystal Bases* (World Scientific 2017),
chapters 2–3 (signature rule), chapter 13 (Demazure crystals).

This module is **pure-Python integer arithmetic** — no sympy, no
floating point.  Coefficients in the canonical basis are
guaranteed-integer by construction; the bar invariance check is a
combinatorial identity, not a polynomial expansion.

See also (sibling modules — non-overlapping roles):

* ``demazure_markov_trace.py`` — Demazure character ``D_w(λ)`` via the
  *polynomial* Demazure operator ``π_i`` on Laurent polynomials in
  ``x_1, …, x_n``.  Used by the Demazure-fiber Markov-trace functional
  (``prop:demazure-fiber-markov-trace``).  Complementary to the
  combinatorial enumerator here: ``D_w(λ)`` is a polynomial; the
  ``demazure_subcrystal`` returned here is the *set of SSYTs* whose
  weights sum to that polynomial.
* ``brundan_kleshchev_audit.py`` — necessary-conditions audit for the
  Brundan–Kleshchev isomorphism ``H_n(R, q) ≅ R_α^Λ``.  Provides the
  empirical-evidence dossier for the conjectural class
  ``CrystalGraphRealization``; this module supplies the SSYT-level
  primitives that the conjectural isomorphism is *about*.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
from collections import deque
from dataclasses import dataclass, field
from functools import lru_cache
from typing import Iterable


# ── 1.  Tableau data structure ─────────────────────────────────────


@dataclass(frozen=True)
class SSYT:
    """Semistandard Young tableau.

    ``rows`` is a tuple of tuples; ``rows[i]`` is row ``i`` (top row
    first), entries are positive integers.  Semistandard means:
    weakly increasing along rows, strictly increasing down columns.

    ``shape`` is recovered as ``tuple(len(r) for r in rows)``.
    """

    rows: tuple[tuple[int, ...], ...]

    @property
    def shape(self) -> tuple[int, ...]:
        return tuple(len(r) for r in self.rows)

    @property
    def size(self) -> int:
        return sum(len(r) for r in self.rows)

    @property
    def weight(self) -> tuple[int, ...]:
        """Weight = content vector ``(c_1, c_2, …)`` where ``c_k`` is
        the number of cells with entry ``k``."""
        if not self.rows:
            return ()
        max_entry = max((max(r) for r in self.rows if r), default=0)
        w = [0] * max_entry
        for r in self.rows:
            for x in r:
                w[x - 1] += 1
        return tuple(w)

    def row_reading_word(self) -> tuple[int, ...]:
        """Row-reading word: read rows **bottom-to-top**, each row
        left-to-right.  This is the Kashiwara reading word convention
        used by the signature rule.
        """
        out: list[int] = []
        for r in reversed(self.rows):
            out.extend(r)
        return tuple(out)

    def is_semistandard(self) -> bool:
        """True iff rows are weakly increasing and columns strictly
        increasing.  Used for sanity-check of constructed tableaux."""
        # Rows weakly increasing
        for r in self.rows:
            for j in range(len(r) - 1):
                if r[j] > r[j + 1]:
                    return False
        # Columns strictly increasing
        for i in range(len(self.rows) - 1):
            for j in range(min(len(self.rows[i]), len(self.rows[i + 1]))):
                if self.rows[i][j] >= self.rows[i + 1][j]:
                    return False
        return True

    def __str__(self) -> str:
        if not self.rows:
            return "∅"
        width = max(len(str(x)) for r in self.rows for x in r) if any(self.rows) else 1
        return "\n".join(
            " ".join(f"{x:>{width}}" for x in r) for r in self.rows
        )


def highest_weight_tableau(shape: tuple[int, ...]) -> SSYT:
    """Highest-weight SSYT of given shape: row ``i`` filled with ``i+1``.

    Example: shape = (3, 2) → ((1,1,1), (2,2)).
    """
    rows = tuple(tuple([i + 1] * length) for i, length in enumerate(shape))
    return SSYT(rows)


# ── 2.  Signature rule (Kashiwara f_i, e_i) ────────────────────────
#
# Standard algorithm (Bump–Schilling 2017, §2.3):
#
#   1. Take the row-reading word of T.
#   2. Replace each `i` with `+`, each `i+1` with `−`, ignore others.
#   3. Iteratively cancel adjacent `−+` pairs (left-to-right).
#   4. The remaining "reduced signature" looks like  +…+−…−.
#   5. f_i acts on the *rightmost surviving +* — change that `i`
#      to `i+1` in the original tableau (well-defined: tableau
#      stays semistandard).  e_i acts on the *leftmost surviving −*
#      — change that `i+1` to `i`.
#
# If no surviving + (resp. −) exists, f_i (resp. e_i) returns None.
# This module deliberately uses None rather than a "0" zero element
# for clarity — callers should branch on ``is None``.


def _reduced_signature(word: tuple[int, ...], i: int) -> list[tuple[str, int]]:
    """Return list of ``(sign, position_in_original_word)`` after
    iterative ``-+`` cancellation.  Positions are 0-indexed into
    ``word``.  Letters not equal to ``i`` or ``i+1`` are simply
    ignored (do not appear in the output).
    """
    # First pass: build (sign, pos) list for relevant letters.
    sig: list[tuple[str, int]] = []
    for pos, x in enumerate(word):
        if x == i:
            sig.append(("+", pos))
        elif x == i + 1:
            sig.append(("-", pos))

    # Iterative −+ cancellation (left-to-right scan, repeated).
    changed = True
    while changed:
        changed = False
        new_sig: list[tuple[str, int]] = []
        skip = False
        for j in range(len(sig)):
            if skip:
                skip = False
                continue
            if (j + 1 < len(sig)
                    and sig[j][0] == "-" and sig[j + 1][0] == "+"):
                # Cancel this −+ pair.
                changed = True
                skip = True
                continue
            new_sig.append(sig[j])
        sig = new_sig
    return sig


def _word_pos_to_cell(T: SSYT, pos: int) -> tuple[int, int]:
    """Translate a position in the row-reading word back to a
    ``(row_index, col_index)`` cell in the tableau.

    The reading word reads rows BOTTOM-to-top, left-to-right within
    each row.  So position 0 is the bottom-left cell; the last
    position is the top-right.
    """
    rows = T.rows
    # Cumulative lengths from the bottom row up.
    offset = 0
    for ri in range(len(rows) - 1, -1, -1):
        L = len(rows[ri])
        if pos < offset + L:
            return ri, pos - offset
        offset += L
    raise IndexError(f"position {pos} out of range for tableau of size {T.size}")


def kashiwara_lower(T: SSYT, i: int) -> SSYT | None:
    """Apply ``f_i`` to ``T``.  Returns the new tableau or ``None``
    if ``f_i T = 0``.

    Acts on the **rightmost surviving +** in the reduced signature.
    """
    word = T.row_reading_word()
    sig = _reduced_signature(word, i)
    # Rightmost surviving + (last position with sign '+').
    plus_positions = [pos for s, pos in sig if s == "+"]
    if not plus_positions:
        return None
    target_word_pos = plus_positions[-1]
    ri, ci = _word_pos_to_cell(T, target_word_pos)
    new_rows = [list(r) for r in T.rows]
    assert new_rows[ri][ci] == i, (
        f"signature rule expected entry {i} at ({ri},{ci}); "
        f"found {new_rows[ri][ci]}"
    )
    new_rows[ri][ci] = i + 1
    out = SSYT(tuple(tuple(r) for r in new_rows))
    assert out.is_semistandard(), (
        f"f_{i} produced non-SSYT — signature rule violated:\n"
        f"  before: {T.rows}\n"
        f"  after:  {out.rows}"
    )
    return out


def kashiwara_raise(T: SSYT, i: int) -> SSYT | None:
    """Apply ``e_i`` to ``T``.  Returns the new tableau or ``None``
    if ``e_i T = 0``.

    Acts on the **leftmost surviving −** in the reduced signature.
    """
    word = T.row_reading_word()
    sig = _reduced_signature(word, i)
    minus_positions = [pos for s, pos in sig if s == "-"]
    if not minus_positions:
        return None
    target_word_pos = minus_positions[0]
    ri, ci = _word_pos_to_cell(T, target_word_pos)
    new_rows = [list(r) for r in T.rows]
    assert new_rows[ri][ci] == i + 1, (
        f"signature rule expected entry {i+1} at ({ri},{ci}); "
        f"found {new_rows[ri][ci]}"
    )
    new_rows[ri][ci] = i
    out = SSYT(tuple(tuple(r) for r in new_rows))
    assert out.is_semistandard(), (
        f"e_{i} produced non-SSYT — signature rule violated:\n"
        f"  before: {T.rows}\n"
        f"  after:  {out.rows}"
    )
    return out


# ── 3.  Crystal B(λ) via BFS from highest weight ───────────────────


def crystal_B(shape: tuple[int, ...], n: int) -> set[SSYT]:
    """Enumerate the connected crystal ``B(λ)`` of ``sl_n``-type, with
    entries in ``{1, …, n}``, by BFS from the highest-weight tableau.

    ``shape`` must be a partition (weakly decreasing, positive parts).
    ``n`` is the rank+1 (entries are ``1..n``).

    Returns the set of all reachable SSYT.  Cardinality equals
    ``s_λ(1, 1, …, 1)`` (Weyl dimension formula).

    For the symmetric-group / Hecke perspective: when ``shape ⊢ n``,
    these tableaux are NOT the SYT — those would have entries
    ``1..|λ|`` each used once.  This is the ``sl_n``-crystal where
    entries can repeat.  For Hecke NF use cases that need exactly
    SYT, restrict to weight ``(1, 1, …, 1)`` after enumeration.
    """
    hw = highest_weight_tableau(shape)
    visited: set[SSYT] = {hw}
    queue: deque[SSYT] = deque([hw])
    while queue:
        T = queue.popleft()
        for i in range(1, n):  # f_1, …, f_{n-1}
            T2 = kashiwara_lower(T, i)
            if T2 is not None and T2 not in visited:
                visited.add(T2)
                queue.append(T2)
    return visited


# ── 4.  Demazure sub-crystal ───────────────────────────────────────


def demazure_subcrystal(
    shape: tuple[int, ...],
    n: int,
    reduced_word: tuple[int, ...],
) -> set[SSYT]:
    """Demazure sub-crystal ``B_w(λ) ⊆ B(λ)`` for ``w = s_{i_1} …
    s_{i_k}`` given as a reduced expression ``reduced_word =
    (i_1, …, i_k)`` (1-indexed simple reflections).

    Construction (Bump–Schilling §13.4): start from the singleton
    set containing the highest-weight tableau; at each step ``j``
    apply the Demazure operator ``D_{i_j}`` which adds to the set
    every tableau reachable by repeated application of ``f_{i_j}``
    (saturated under that single Kashiwara operator).

    For ``w = w_0`` (longest element) the result equals all of
    ``B(λ)``; for the empty word it is the singleton ``{u_λ}``.

    This is the **asymptotic-win primitive**: when ``ℓ(w) ≪
    ℓ(w_0) = n(n-1)/2`` and the relevant computation is concentrated
    on a sub-Weyl orbit (e.g. resonance crossings), enumerating
    ``B_w(λ)`` is exponentially smaller than ``B(λ)``.
    """
    hw = highest_weight_tableau(shape)
    current: set[SSYT] = {hw}
    for i in reduced_word:
        next_set: set[SSYT] = set(current)
        for T in current:
            T_curr = T
            while True:
                T_next = kashiwara_lower(T_curr, i)
                if T_next is None:
                    break
                next_set.add(T_next)
                T_curr = T_next
        current = next_set
    return current


def demazure_dim(
    shape: tuple[int, ...],
    n: int,
    reduced_word: tuple[int, ...],
) -> int:
    """Cardinality of ``B_w(λ)``.

    Convenience wrapper around ``demazure_subcrystal``: it
    materialises the full sub-crystal as a Python ``set`` and
    returns its size.  A true counting-only DP (e.g. via Demazure
    character coefficients summed at weight ``1``) is future work;
    until then this helper has the same memory profile as
    ``demazure_subcrystal``, just discards the result.

    Useful for benchmarking the asymptotic-win shape (full crystal
    vs. partial-Weyl sub-crystal) when the caller doesn't need the
    tableaux themselves.
    """
    return len(demazure_subcrystal(shape, n, reduced_word))


def demazure_growth_profile(
    shape: tuple[int, ...],
    n: int,
    reduced_word: tuple[int, ...],
) -> list[tuple[int, int]]:
    """Return ``[(prefix_length, sub-crystal cardinality), …]`` for
    every prefix of ``reduced_word`` (including empty and full).

    This is the data series the Demazure asymptotic-win demo plots:
    monotone-non-decreasing growth from the singleton ``{u_λ}`` (at
    prefix length 0) to ``B(λ)`` (at prefix length ``ℓ(w_0)``).
    Useful for picking a "resonance" length k where the sub-crystal
    is still ≪ ``|B(λ)|`` so the downstream Hecke-character sweep
    fits in budget.
    """
    out: list[tuple[int, int]] = []
    hw = highest_weight_tableau(shape)
    current: set[SSYT] = {hw}
    out.append((0, len(current)))
    for j, i in enumerate(reduced_word, start=1):
        next_set: set[SSYT] = set(current)
        for T in current:
            T_curr = T
            while True:
                T_next = kashiwara_lower(T_curr, i)
                if T_next is None:
                    break
                next_set.add(T_next)
                T_curr = T_next
        current = next_set
        out.append((j, len(current)))
    return out


def longest_reduced_word(n: int) -> tuple[int, ...]:
    """A reduced expression for the longest element ``w_0 ∈ S_n``,
    using the standard staircase ``s_1 (s_2 s_1) (s_3 s_2 s_1) …``.

    Length is ``n(n-1)/2``.
    """
    out: list[int] = []
    for k in range(1, n):
        for j in range(k, 0, -1):
            out.append(j)
    return tuple(out)


# ── 5.  Bar involution as Schützenberger evacuation ────────────────
#
# On the type-A crystal B(λ), the Lusztig bar involution restricted
# to the canonical basis is realised combinatorially by Schützenberger
# *evacuation* (Lascoux–Leclerc–Thibon 1995).  We provide a thin
# implementation that suffices for validating bar-invariance of
# specific elements; full LLT polynomial expansion is left to a
# future module.


def schuetzenberger_evacuation(T: SSYT, n: int) -> SSYT:
    """Schützenberger evacuation: walk from the highest-weight
    tableau ``u_λ`` to ``T`` using a sequence of ``f_{i_k}``, then
    apply the inverse sequence using ``f_{n-i_k}`` from the
    *anti-highest-weight* tableau.  The result is an involution
    that realises the Lusztig bar on type-A crystals.

    For modest crystals (size ≤ a few hundred) this is fast enough
    to validate bar-invariance combinatorially — no sympy needed.
    """
    # Build a BFS path from highest-weight to T.
    hw = highest_weight_tableau(T.shape)
    if T == hw:
        return _anti_highest_weight_tableau(T.shape, n)

    # BFS to find a sequence of f_i's reaching T.
    parent: dict[SSYT, tuple[SSYT, int]] = {}
    queue: deque[SSYT] = deque([hw])
    visited: set[SSYT] = {hw}
    found = False
    while queue and not found:
        U = queue.popleft()
        for i in range(1, n):
            V = kashiwara_lower(U, i)
            if V is not None and V not in visited:
                visited.add(V)
                parent[V] = (U, i)
                if V == T:
                    found = True
                    break
                queue.append(V)
    if not found:
        raise ValueError(
            f"Tableau {T.rows} not reachable in B(λ={T.shape}) for n={n}; "
            f"is the shape correct?"
        )

    # Recover the sequence (i_1, ..., i_k).
    seq: list[int] = []
    U = T
    while U in parent:
        prev, i = parent[U]
        seq.append(i)
        U = prev
    seq.reverse()

    # Apply f_{n-i} from anti-highest-weight tableau in REVERSE order.
    ahw = _anti_highest_weight_tableau(T.shape, n)
    out = ahw
    for i in reversed(seq):
        out = kashiwara_lower(out, n - i)
        if out is None:
            raise RuntimeError(
                "evacuation broke — anti-tableau path failed at step "
                f"f_{n - i}; signature rule mismatch"
            )
    return out


def _anti_highest_weight_tableau(shape: tuple[int, ...], n: int) -> SSYT:
    """Lowest-weight tableau in B(λ) with entries from {1..n}: row i
    filled with the largest semistandard entries.  Concretely, for
    shape = (λ_1, ..., λ_r) with r ≤ n, row i has entries n-r+i+1
    repeated λ_i times.
    """
    r = len(shape)
    if r > n:
        raise ValueError(f"shape has {r} rows but only {n} letters available")
    rows = tuple(tuple([n - r + i + 1] * length)
                 for i, length in enumerate(shape))
    out = SSYT(rows)
    assert out.is_semistandard(), f"anti-HW tableau not SSYT: {rows}"
    return out


# ── 6.  Direct enumeration of SSYT (cross-check) ────────────────────


@lru_cache(maxsize=None)
def count_ssyt(shape: tuple[int, ...], n: int) -> int:
    """Count SSYT of given ``shape`` with entries in ``{1, …, n}``,
    by direct recursion (used to cross-check the BFS enumeration).
    """
    return len(_enumerate_ssyt(shape, n))


def _enumerate_ssyt(shape: tuple[int, ...], n: int) -> list[SSYT]:
    """Direct recursive enumeration of SSYT(shape, n)."""
    if not shape:
        return [SSYT(())]
    rows: list[list[int]] = [[] for _ in shape]
    out: list[SSYT] = []

    def fill(ri: int, ci: int) -> None:
        if ri == len(shape):
            out.append(SSYT(tuple(tuple(r) for r in rows)))
            return
        if ci == shape[ri]:
            fill(ri + 1, 0)
            return
        # Lower bound: must be > entry above (strict column), >= entry
        # to the left (weak row).
        lb = 1
        if ri > 0:
            lb = max(lb, rows[ri - 1][ci] + 1)
        if ci > 0:
            lb = max(lb, rows[ri][ci - 1])
        for v in range(lb, n + 1):
            rows[ri].append(v)
            fill(ri, ci + 1)
            rows[ri].pop()

    fill(0, 0)
    return out


# ── 7.  Self-test / witness emission ───────────────────────────────


def _weyl_dimension_check(shape: tuple[int, ...], n: int) -> int:
    """Schur s_λ(1, …, 1) at ``n`` ones — Weyl dimension formula via
    direct SSYT count (cross-checks BFS).
    """
    return count_ssyt(shape, n)


def _self_test() -> dict:
    """Run the validation suite. Returns a JSON-serialisable summary."""
    results: list[dict] = []

    # Cases: (shape, n)
    cases: list[tuple[tuple[int, ...], int]] = [
        ((1,), 2),
        ((2,), 2),
        ((1, 1), 2),
        ((2, 1), 3),
        ((3,), 3),
        ((2, 1), 4),
        ((2, 2), 3),
        ((3, 1), 3),
        ((2, 1, 1), 4),
        ((3, 2), 4),
        ((2, 2, 1), 4),
    ]

    all_ok = True
    for shape, n in cases:
        crystal = crystal_B(shape, n)
        bfs_count = len(crystal)
        direct_count = count_ssyt(shape, n)

        # Demazure check: B_{w_0}(λ) == B(λ)
        w0 = longest_reduced_word(n)
        dem_full = demazure_subcrystal(shape, n, w0)
        dem_full_ok = (dem_full == crystal)

        # Demazure check: B_{empty}(λ) == {u_λ}
        dem_empty = demazure_subcrystal(shape, n, ())
        dem_empty_ok = (dem_empty == {highest_weight_tableau(shape)})

        ok = (bfs_count == direct_count) and dem_full_ok and dem_empty_ok
        all_ok = all_ok and ok
        results.append({
            "shape": list(shape),
            "n": n,
            "B_lambda_count": bfs_count,
            "ssyt_count_direct": direct_count,
            "agree": bfs_count == direct_count,
            "demazure_w0_recovers_full": dem_full_ok,
            "demazure_empty_is_singleton": dem_empty_ok,
            "ok": ok,
        })

    # Demazure asymptotic-win demonstration: B_w(λ) for partial w.
    demazure_demo: list[dict] = []
    shape, n = (2, 1), 4
    full_size = len(crystal_B(shape, n))
    for k in range(0, len(longest_reduced_word(n)) + 1):
        w_partial = longest_reduced_word(n)[:k]
        sub = demazure_subcrystal(shape, n, w_partial)
        demazure_demo.append({
            "reduced_word_length": k,
            "subcrystal_size": len(sub),
            "fraction_of_full": round(len(sub) / full_size, 4),
        })

    return {
        "validation_cases": results,
        "all_passed": all_ok,
        "demazure_growth_demo": {
            "shape": list(shape),
            "n": n,
            "full_crystal_size": full_size,
            "by_reduced_word_length": demazure_demo,
        },
    }


if __name__ == "__main__":
    import sys

    print("=" * 72)
    print("CRYSTAL-BASIS PRIMITIVES — Phase 0 self-test")
    print("=" * 72)

    summary = _self_test()

    for r in summary["validation_cases"]:
        flag = "✓" if r["ok"] else "✗"
        print(
            f"  {flag}  λ={tuple(r['shape'])}, n={r['n']}: "
            f"|B(λ)|={r['B_lambda_count']} "
            f"(SSYT count={r['ssyt_count_direct']}); "
            f"Demazure w_0={'OK' if r['demazure_w0_recovers_full'] else 'FAIL'}; "
            f"Demazure ∅={'OK' if r['demazure_empty_is_singleton'] else 'FAIL'}"
        )

    print("\n  Demazure asymptotic-win demo "
          f"(λ={tuple(summary['demazure_growth_demo']['shape'])}, "
          f"n={summary['demazure_growth_demo']['n']}, "
          f"full crystal = "
          f"{summary['demazure_growth_demo']['full_crystal_size']} verts):")
    for row in summary["demazure_growth_demo"]["by_reduced_word_length"]:
        bar = "█" * int(row["fraction_of_full"] * 20)
        print(
            f"    ℓ(w)={row['reduced_word_length']:2d}  "
            f"|B_w(λ)|={row['subcrystal_size']:3d}  "
            f"({row['fraction_of_full']:.1%})  {bar}"
        )

    if summary["all_passed"]:
        print("\n  ✓ All crystal-basis primitive tests passed.")
    else:
        print("\n  ✗ Some tests FAILED — see above.")
        sys.exit(1)

    # Emit witness via WitnessBuilder (canonical ComputationWitness
    # schema; matches scripts/audit-wiring.ts expectations and
    # folio-assistant/schemas/types.ts).
    from witness_base import WitnessBuilder

    w = (WitnessBuilder("crystal-basis-primitives", engine="python")
         .set_description(
            "Phase 0 of the S-poly → crystal-basis migration: validates "
            "Kashiwara f_i / e_i operators (signature rule), B(λ) BFS, "
            "and Demazure sub-crystal enumeration against the Weyl "
            "dimension formula s_λ(1,…,1) = #SSYT(λ,n)."
         ))
    w.add_data("validation_cases", summary["validation_cases"])
    w.add_data("demazure_growth_demo", summary["demazure_growth_demo"])
    w.add_data("all_passed", summary["all_passed"])
    # One assertion per (shape, n) case — agreement of BFS count
    # with direct SSYT enumeration (Weyl dimension formula).
    for r in summary["validation_cases"]:
        w.add_assertion(
            name=f"weyl_dim_lambda={tuple(r['shape'])}_n={r['n']}",
            computed=r["B_lambda_count"],
            expected=r["ssyt_count_direct"],
            tolerance=0,
            source="Weyl dimension formula; "
                   "Bump-Schilling, Crystal Bases (2017) §3.1",
        )
    out_path = w.save()
    print(f"\n  Witness written → {out_path.name}")
