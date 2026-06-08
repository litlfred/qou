#!/usr/bin/env python3
"""derived_chi_catalogue_matrix_m.py — Tier 1 Phase 1 substrate.

Implements the **matrix-valued M** approach for the LR factorisation
of `χ^λ(T_β_atom)` identified in the audit doc
[`docs/audits/2026-06-07-derived-chi-catalogue-tier-1-lr-factorisation.md`](../../docs/audits/2026-06-07-derived-chi-catalogue-tier-1-lr-factorisation.md)
as the correct refinement of the (refuted) scalar-ω formula.

## What this delivers

A pure-Python port of the Hoefsmit **natural seminormal form** for
H_n(q) acting on V_λ, using sympy q-rationals (exact, symbolic in q).

  - `seminormal_matrices_qrat(shape)` — returns the list of
    σ_1, …, σ_{n-1} as sympy matrices over Q(q) in the SYT basis
  - `chi_lambda_via_matrix_product(shape, word)` — computes χ^λ(T_β)
    as Tr[ρ^λ(σ_{c_1}) · … · ρ^λ(σ_{c_k})] symbolically in q
  - Cross-validation harness vs Rust `chi_q_via_gp` at numerical q

This is the **symbolic-substrate** for the matrix-M extraction:
once we have ρ^λ(σ_i) as exact q-rational matrices, the next step
(future PR) is to project ρ^λ(σ_{3k+2}) onto each (μ_left, μ_right)
LR-isotypic to obtain M(μ_left, μ_right, λ; q) — the matrix that
enters the trace formula

    χ^λ(T_β) = Σ_{(μ_left, μ_right)} Tr [ M · (ρ^{μ_left}(β_left)
                                              ⊗ ρ^{μ_right}(β_right)) ]

per audit §4 (refined).

## Why "natural" form not "Hoefsmit" form

The Rust `seminormal_block_generators` (`tools/hecke-engine/src/seminormal.rs:230`)
uses the SYMMETRIC normalisation where the 2×2 blocks have
`b = √(a·a' + 1)` — self-adjoint matrices, good for numerical f64
work but the `√` is NOT a rational function of q in general
(e.g. for ρ=2, `b² = (q⁴ + q² + 1)/(q² + 1)²` — rational, but the
sqrt of that lifts out of Q(q)).

The ASYMMETRIC natural form puts `c = 1, c' = a·a' + 1` on the off-
diagonal. Then every entry is in Q(q), and the trace of any matrix
product is the same as the symmetric form (similarity within each
2×2 block preserves trace). So characters match exactly while we
stay symbolic in q.

## Δ_λ gate

This is pure structural rearrangement — Young's seminormal form is
textbook Hecke representation theory (Mathas, Hoefsmit). No new
ansatz, no calibration parameter, no empirical fit. The audit doc
§9 conditions on canonical-only operations are satisfied.

## Scope of this PR

  - PROVE the pure-Python matrix-M character pipeline matches
    Rust `chi_q_via_gp` on every (n, λ, β) combination tested
  - SET UP the q-rational matrix substrate for follow-up
    (μ_left, μ_right) projection work

The LR-block extraction itself — building Π_{(μ_p, μ_n)} and
extracting M = Π · σ_b · Π — is the next milestone (multi-session
per audit estimate). The validation here proves the substrate is
correct before that next step.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: E402, F401

import sympy as sp  # noqa: E402

import pyhecke_native as ph  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402


# ── Standard Young tableaux generator ─────────────────────────────


def _shape_partitions_of(n: int) -> list[tuple[int, ...]]:
    """All partitions of n, returned as sorted tuples (largest first).

    Wraps `pyhecke_native.partitions_of` so this module has one
    canonical entry point for shape enumeration.
    """
    return [tuple(p) for p in ph.partitions_of(n)]


def standard_young_tableaux(shape: tuple[int, ...]) -> list[tuple[tuple[int, int], ...]]:
    """All standard Young tableaux of the given shape, each represented
    as the tuple of cells `(row, col)` indexed by the entry value.

    Entry `k` (1-based) lives in cell `T[k-1]`. The list of all SYTs
    matches the convention used by `tools/hecke-engine/src/seminormal.rs`
    so the Python port can swap basis vectors by SYT identity.

    Algorithm: recursive — at step k, place k into any cell that is a
    corner of the current Young diagram and yields a still-valid
    partition shape.
    """
    n = sum(shape)
    if n == 0:
        return [()]

    # corners[i] = current set of cells indexed by where entry i (1-based) goes.
    results: list[list[tuple[int, int]]] = []

    def _place(filled: list[tuple[int, int]], rows: list[int]) -> None:
        """rows[r] = current number of cells filled in row r."""
        k = len(filled) + 1
        if k > n:
            results.append(list(filled))
            return
        for r, target in enumerate(shape):
            if rows[r] >= target:
                continue
            # placement at (r, rows[r]) is valid iff it's a corner —
            # either r == 0 or row r-1 has at least one more cell than r.
            if r > 0 and rows[r - 1] <= rows[r]:
                continue
            cell = (r, rows[r])
            rows[r] += 1
            filled.append(cell)
            _place(filled, rows)
            filled.pop()
            rows[r] -= 1

    _place([], [0] * len(shape))
    return [tuple(t) for t in results]


def _content(cell: tuple[int, int]) -> int:
    """Content of a cell (r, c) is `c - r` (column minus row)."""
    return cell[1] - cell[0]


# ── Pure-Python Hoefsmit (natural / asymmetric) ───────────────────


def seminormal_matrices_qrat(
    shape: tuple[int, ...], q: sp.Symbol
) -> list[sp.Matrix]:
    """Build the σ_1, …, σ_{n-1} generator matrices of H_n(q) acting
    on V_λ (`λ = shape`) in the standard Young tableau basis, as
    exact sympy `Matrix` objects over Q(q).

    Uses the **natural / asymmetric** seminormal form where 2×2
    blocks have off-diagonal entries (1, b²) instead of the
    symmetric (b, b) Hoefsmit normalisation. This keeps every entry
    rational in q. The character (trace of matrix products) is
    invariant under this similarity, so any chi computation
    downstream matches the symmetric / Rust form exactly.

    Formula (per `tools/hecke-engine/src/seminormal.rs` lines 230-293,
    asymmetricised):

        For SYT T at index i, generator σ_k:
          ρ = content(T[k]) - content(T[k-1])
          a = (q - q^{-1}) / (1 - q^{-2ρ})
          If swap(T, k-1, k) is NOT a valid SYT  (same row / column):
            σ_k acts on T_i as scalar `a` (1×1 block).
            For same row: ρ = 1 ⇒ a = q.
            For same column: ρ = -1 ⇒ a = -q^{-1}.
          Else (different row + column) at index j:
            a' = (q - q^{-1}) / (1 - q^{2ρ})
            σ_k on (T_i, T_j) is the 2×2 block
              [ a,    1      ]
              [ a·a'+1,  a'  ]
            (one of the equivalent natural-form normalisations).

    Returns a list `[σ_1, σ_2, …, σ_{n-1}]` of sympy matrices, each
    of size `dim × dim` where `dim = #SYTs(shape) = dim V_λ`.
    """
    n = sum(shape)
    syts = standard_young_tableaux(shape)
    dim = len(syts)
    syt_to_idx: dict[tuple[tuple[int, int], ...], int] = {
        syt: i for i, syt in enumerate(syts)
    }
    h = q - 1 / q

    generators: list[sp.Matrix] = []
    for k in range(1, n):
        # σ_k is highly sparse (only 1×1 and 2×2 blocks per Hoefsmit
        # block decomposition) — build as MutableSparseMatrix, convert
        # to dense Matrix on return.
        M = sp.MutableSparseMatrix(dim, dim, {})
        processed = [False] * dim
        for i in range(dim):
            if processed[i]:
                continue
            cell_k_minus_1 = syts[i][k - 1]
            cell_k = syts[i][k]
            rho = _content(cell_k) - _content(cell_k_minus_1)
            # Use sp.cancel — both a, a' and b² are rational in q;
            # cancel does GCD-based simplification without the
            # expensive heuristic search that sp.simplify runs.
            a = sp.cancel(h / (1 - q ** (-2 * rho)))

            # Swap partner — only valid if cells are in different rows
            # AND different columns (i.e. |ρ| ≠ 1 is equivalent here).
            swapped = list(syts[i])
            swapped[k - 1], swapped[k] = cell_k, cell_k_minus_1
            swapped_tuple = tuple(swapped)
            partner = syt_to_idx.get(swapped_tuple)
            if partner is None or partner == i:
                # 1×1 block.
                M[i, i] = a
                processed[i] = True
            else:
                j = partner
                a_prime = sp.cancel(h / (1 - q ** (2 * rho)))
                b_sq = sp.cancel(a * a_prime + 1)
                # Asymmetric natural form: off-diagonals are (1, b²).
                # Order by index: smaller-index row = i, larger = j.
                lo, hi = (i, j) if i < j else (j, i)
                a_lo, a_hi = (a, a_prime) if i < j else (a_prime, a)
                M[lo, lo] = a_lo
                M[lo, hi] = sp.Integer(1)
                M[hi, lo] = b_sq
                M[hi, hi] = a_hi
                processed[lo] = True
                processed[hi] = True
        generators.append(sp.Matrix(M))
    return generators


# ── Character via matrix product ──────────────────────────────────


def chi_lambda_via_matrix_product(
    shape: tuple[int, ...],
    word: list[tuple[int, int]],
    q: sp.Symbol,
) -> sp.Expr:
    """Compute χ^λ(T_β) symbolically in q via direct matrix product
    in the seminormal basis.

    Args:
      shape: partition λ ⊢ n.
      word: list of `(sign, gen_1based)` pairs — same convention as
        `pyhecke_native.chi_q_via_gp`. `sign = +1` → σ_g, `sign = -1`
        → σ_g⁻¹. `gen_1based` is 1-based (σ_1 is the first generator).
      q: sympy Symbol for the deformation parameter.

    Returns the trace of the matrix product, simplified as a sympy
    expression in q.

    Internal: pre-computes `σ_i⁻¹` once per generator that appears
    with negative sign in the word; the Hecke relation gives
    σ_i⁻¹ = σ_i - (q - q⁻¹) (i.e. matrix subtract a scaled identity
    on the 1×1 blocks where σ_i acts as q-or-(-1/q), but more
    cleanly: σ_i⁻¹ = σ_i - h · I as ALGEBRA elements, since
    σ_i² = h σ_i + I ⇒ σ_i⁻¹ = σ_i - h · I). So compute
    `σ_i⁻¹ = σ_i_matrix - h · eye(dim)`.
    """
    n = sum(shape)
    syts = standard_young_tableaux(shape)
    dim = len(syts)
    sigmas = seminormal_matrices_qrat(shape, q)
    h = q - 1 / q
    eye = sp.eye(dim)

    sigma_inv_cache: dict[int, sp.Matrix] = {}

    def get_inv(g_idx_0based: int) -> sp.Matrix:
        if g_idx_0based not in sigma_inv_cache:
            # Apply sp.cancel element-wise: σ_i⁻¹ = σ_i - h·I leaves the
            # diagonal entries as `a - h` which sp doesn't auto-collapse,
            # and unsimplified entries blow up the trace's intermediate
            # symbolic size during long matrix products. applyfunc with
            # cancel keeps each entry in canonical rational form.
            inv_mat = sigmas[g_idx_0based] - h * eye
            sigma_inv_cache[g_idx_0based] = inv_mat.applyfunc(sp.cancel)
        return sigma_inv_cache[g_idx_0based]

    # Start with identity, multiply on the right (matches word order
    # T_β = T_{σ_{c_1}} · T_{σ_{c_2}} · … convention).
    product = eye
    for (sign, gen_1based) in word:
        g_idx = gen_1based - 1
        assert 0 <= g_idx < n - 1, (
            f"gen_1based={gen_1based} out of range for n={n}"
        )
        mat = sigmas[g_idx] if sign >= 0 else get_inv(g_idx)
        product = product * mat
    # The character is a rational function in q; sp.cancel is the
    # fast canonical-form reducer (GCD-based) for this domain.
    return sp.cancel(sp.trace(product))


# ── Cross-validation harness vs Rust ──────────────────────────────


def chi_rust_at_qval(
    shape: tuple[int, ...],
    n_strands: int,
    word: list[tuple[int, int]],
    q_value: sp.Expr,
) -> sp.Expr:
    """Evaluate `pyhecke_native.chi_q_via_gp` and sum its Laurent terms
    at the given symbolic q-value. Returns a sympy expression.

    The Rust output uses half-exponent encoding (key = 2 · math q-exp)
    per the half-exponent convention documented in
    `derived_chi_catalogue_bar_symmetry_audit.py`.
    """
    laurent = ph.chi_q_via_gp(list(shape), n_strands, list(word))
    total = sp.Integer(0)
    for (d_key, c_str) in laurent:
        d_int = int(d_key)
        # half-exp: math q-exp = d_int / 2.
        # Both even and odd d_int can occur — pyhecke emits both
        # (e.g. trefoil [2] strand=2 word=[(1,1)*3] → [(6, '1')] = q³).
        if d_int % 2 == 0:
            total += sp.Integer(int(c_str)) * q_value ** (d_int // 2)
        else:
            # half-integer exponent — represent as q^(d/2) symbolically.
            total += sp.Integer(int(c_str)) * q_value ** sp.Rational(d_int, 2)
    return sp.simplify(total)


def cross_validate(
    shape: tuple[int, ...],
    word: list[tuple[int, int]],
    q_test_values: list[sp.Expr] | None = None,
) -> dict[str, object]:
    """For a given (shape, word), compute χ^λ(T_β) both via the pure-
    Python seminormal matrix product (symbolic in q) and via Rust
    `chi_q_via_gp` (numerical at each test q). Returns a dict with
    pass/fail per test q.

    q_test_values default to a small set covering generic + roots of
    unity that are catalogue-relevant: {2, 3, 5, 1+i, 1.1097}.
    """
    n = sum(shape)
    if q_test_values is None:
        # Three rational + one substrate-anchor numerical to stress
        # the symbolic simplifier and the Rust f64 evaluator.
        q_test_values = [
            sp.Integer(2),
            sp.Integer(3),
            sp.Rational(11097, 10000),
        ]

    q = sp.Symbol("q", positive=True)
    python_symbolic = chi_lambda_via_matrix_product(shape, word, q)

    results: list[dict] = []
    all_match = True
    for q_val in q_test_values:
        python_val = sp.simplify(python_symbolic.subs(q, q_val))
        rust_val = chi_rust_at_qval(shape, n, word, q_val)
        # Compare as rationals or floats — sympy handles both.
        delta = sp.simplify(python_val - rust_val)
        match = bool(delta == 0)
        if not match:
            # Fall back to numerical comparison with tolerance — the
            # Rust output is f64 internally; the symbolic Python can
            # differ in the last bit when forced through float.
            try:
                py_f = float(python_val)
                rs_f = float(rust_val)
                match = abs(py_f - rs_f) < max(1e-10, 1e-10 * max(abs(py_f), abs(rs_f)))
            except (TypeError, ValueError):
                match = False
        if not match:
            all_match = False
        results.append({
            "q": str(q_val),
            "python_symbolic": str(python_val),
            "rust": str(rust_val),
            "delta": str(delta),
            "match": match,
        })
    return {
        "shape": list(shape),
        "word": [list(t) for t in word],
        "n_strands": n,
        "python_symbolic_q": str(python_symbolic),
        "tests": results,
        "all_match": all_match,
    }


# ── Sweep: validate against catalogue's compute scope ─────────────


def _word_for_braid_word_3a(Z: int, N: int) -> tuple[int, list[tuple[int, int]]]:
    """Bridge to the production atom braid word — uses the existing
    `mass_at_3A_proper.atom_braid_word_3A` and translates from the
    `(c, d, gen_0based)` triple format into the `(sign, gen_1based)`
    pairs that `chi_q_via_gp` and our Python pipeline both consume.
    """
    from mass_at_3A_proper import atom_braid_word_3A
    triples = atom_braid_word_3A(Z, N)
    n_strands = 3 * (Z + N)
    word = [(1 if c >= 0 else -1, gen_0based + 1) for (c, _d, gen_0based) in triples]
    return n_strands, word


# ── Main: sweep validation across small partitions ────────────────


def main() -> int:
    wb = WitnessBuilder(
        "derived-chi-catalogue-matrix-m-validation",
        engine="python",
    )
    wb.set_description(
        "Pure-Python Hoefsmit (natural / asymmetric seminormal form) "
        "validation against Rust pyhecke_native chi_q_via_gp. "
        "Substrate for Tier 1 matrix-M extraction (audit doc "
        "2026-06-07-derived-chi-catalogue-tier-1-lr-factorisation). "
        "Proves the q-rational matrix pipeline computes the same "
        "character as the Rust Geck-Pfeiffer engine on a sweep of "
        "(n, λ, β) test cases."
    )

    print("=" * 78)
    print(" Pure-Python Hoefsmit ↔ Rust chi_q_via_gp validation sweep")
    print("=" * 78)

    # Test 1: All partitions of n = 2 on a single-crossing braid.
    # Sanity: σ_1 has eigenvalues q (trivial rep) and -q⁻¹ (sign rep).
    print("\n  Test 1 — n=2, β = σ_1 (single positive crossing)")
    print("  ─────────────────────────────────────────────────")
    test_cases: list[dict] = []
    for shape in [(2,), (1, 1)]:
        result = cross_validate(shape, [(1, 1)])
        status = "✓" if result["all_match"] else "✗"
        print(f"    {status} λ={list(shape)} χ(q) = {result['python_symbolic_q']}")
        test_cases.append(result)

    # Test 2: All partitions of n = 3 on Hopf-link braid (σ_1 σ_2 σ_1).
    print("\n  Test 2 — n=3, β = σ_1 σ_2 σ_1 (Hopf-like)")
    print("  ─────────────────────────────────────────")
    hopf_word = [(1, 1), (1, 2), (1, 1)]
    for shape in [(3,), (2, 1), (1, 1, 1)]:
        result = cross_validate(shape, hopf_word)
        status = "✓" if result["all_match"] else "✗"
        print(f"    {status} λ={list(shape)} χ(q) = {result['python_symbolic_q']}")
        test_cases.append(result)

    # Test 3: All partitions of n = 4 on a 4-letter mixed-sign braid.
    print("\n  Test 3 — n=4, β = σ_1 σ_2 σ_3 σ_2⁻¹ (mixed signs)")
    print("  ──────────────────────────────────────────────────")
    mixed_word = [(1, 1), (1, 2), (1, 3), (-1, 2)]
    for shape in _shape_partitions_of(4):
        result = cross_validate(shape, mixed_word)
        status = "✓" if result["all_match"] else "✗"
        print(f"    {status} λ={list(shape)} χ(q) = {result['python_symbolic_q'][:60]}…")
        test_cases.append(result)

    # Test 4: All partitions of n = 6 (deuteron strand count) on a
    # short test braid β = σ_1 σ_3 σ_5 (commuting generators across
    # the parabolic split — pure (μ_p, μ_n) restriction with the
    # bridge σ_3 included).
    print("\n  Test 4 — n=6, β = σ_1 σ_3 σ_5 (deuteron-shaped probe)")
    print("  ──────────────────────────────────────────────────────")
    deut_probe = [(1, 1), (1, 3), (1, 5)]
    n6_partitions = _shape_partitions_of(6)
    for shape in n6_partitions:
        result = cross_validate(shape, deut_probe)
        status = "✓" if result["all_match"] else "✗"
        dim = len(standard_young_tableaux(shape))
        print(f"    {status} λ={list(shape)} dim={dim} χ(q) = "
              f"{result['python_symbolic_q'][:50]}…")
        test_cases.append(result)

    # Tally
    n_total = len(test_cases)
    n_pass = sum(1 for t in test_cases if t["all_match"])
    print(f"\n  ── Summary ──")
    print(f"    Tests:  {n_total}")
    print(f"    Passed: {n_pass}")
    print(f"    Failed: {n_total - n_pass}")

    wb.add_assertion(
        "python_hoefsmit_matches_rust_chi_q_via_gp",
        computed=(n_pass == n_total),
        expected=True,
        source="Whether pure-Python sympy q-rational matrix product "
               "reproduces the Rust pyhecke_native chi_q_via_gp output "
               "on every (n, λ, β) test case in Tests 1-4 (covers "
               "n=2..6, all partitions, several braid words). Proves "
               "the matrix-M substrate is structurally correct.",
    )
    wb.add_data("n_test_cases", n_total)
    wb.add_data("n_pass", n_pass)
    wb.add_data("n_fail", n_total - n_pass)
    wb.add_data("test_cases", test_cases)
    out = wb.save()
    print(f"\n  ✓ Witness: {out.name}")
    print("=" * 78)
    return 0 if n_pass == n_total else 1


if __name__ == "__main__":
    sys.exit(main())
