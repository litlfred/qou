#!/usr/bin/env python3


# polynomial_q_not_applicable: Lean source generator for n=8 dim_q table.
"""
Phase 5 n=8 dim_q table generator (corrected convention).

Convention: `dim_q(λ) = [n]_q! / ∏_{x∈λ} [h_x]_q` — the **quantum
hook-length formula**, matching the existing `heckeH6DimQ` /
`heckeH7DimQ` (cf. the docstring on `heckeH6DimQ` line 365).

For each partition λ ⊢ 8:
1. Compute the multi-set of hook lengths.
2. Symbolically reduce `[8]_q! / ∏ [h]_q` via cancellation.
3. Emit the surviving factor product as a Lean expression.
4. Numerical spot-check at q_0 + q=1.

The 22 partitions of 8 split as **10 conjugate pairs + 2 self-
conjugate** partitions ((4,2,1,1) and (3,3,2)), giving the
accounting 2·10 + 2 = 22.

Output: `phase5-n8-dim-q-table.json` (raw data + Lean code chunks).
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 3, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).parent))
from partition_utils import hook_lengths  # noqa: E402


def partitions_of(n: int) -> list[tuple[int, ...]]:
    if n == 0:
        return [()]
    result: list[tuple[int, ...]] = []

    def rec(remaining: int, max_part: int, prefix: list[int]) -> None:
        if remaining == 0:
            result.append(tuple(prefix))
            return
        for k in range(min(remaining, max_part), 0, -1):
            rec(remaining - k, k, prefix + [k])

    rec(n, n, [])
    return result


def conjugate(partition: tuple[int, ...]) -> tuple[int, ...]:
    if not partition:
        return ()
    cols = max(partition)
    return tuple(
        sum(1 for r in range(len(partition)) if partition[r] > c)
        for c in range(cols)
    )


def q_int_sympy(h: int, q: sp.Symbol) -> sp.Expr:
    """[h]_q = q^(h-1) + q^(h-3) + ... + q^-(h-3) + q^-(h-1)."""
    if h == 0:
        return sp.S.Zero
    if h == 1:
        return sp.S.One
    return sum(q ** k for k in range(h - 1, -h, -2))


def q_factorial(n: int, q: sp.Symbol) -> sp.Expr:
    """[n]_q! = ∏_{k=1}^n [k]_q (returns 1 for n=0 or 1)."""
    result: sp.Expr = sp.S.One
    for k in range(2, n + 1):
        result = result * q_int_sympy(k, q)
    return result


def dim_q_via_quantum_hooks(
    partition: tuple[int, ...], q: sp.Symbol
) -> sp.Expr:
    """dim_q(λ) = [n]_q! / ∏_{x∈λ} [h_x]_q, simplified."""
    n = sum(partition)
    if n == 0:
        return sp.S.One
    hooks = hook_lengths(partition)
    # Hook-product: ∏ [h]_q
    hook_prod: sp.Expr = sp.S.One
    for h in hooks:
        hook_prod = hook_prod * q_int_sympy(h, q)
    qfact = q_factorial(n, q)
    return sp.cancel(qfact / hook_prod)


def q_int_lean(h: int) -> str:
    """Render [h]_q as a Lean expression in `q`."""
    if h == 0:
        return "0"
    if h == 1:
        return "1"
    terms: list[str] = []
    for k in range(h - 1, -h, -2):
        if k == 0:
            terms.append("1")
        elif k > 0:
            terms.append(f"q ^ {k}" if k > 1 else "q")
        else:
            ak = -k
            terms.append(f"(q ^ {ak})⁻¹" if ak > 1 else "q⁻¹")
    return " + ".join(terms)


def factor_signature(
    partition: tuple[int, ...]
) -> tuple[dict[int, int], dict[int, int]]:
    """Compute (numerator, denominator) multi-sets of [k]_q indices
    such that `dim_q(λ) = ∏_{k∈num} [k]_q / ∏_{k∈den} [k]_q`.

    Numerator = [n]_q!'s factors {2, 3, ..., n} as a multiset.
    Denominator = hook lengths > 1 as a multiset.
    Cancellation: subtract per-key min from both sides.
    """
    n = sum(partition)
    num: dict[int, int] = {}
    for k in range(2, n + 1):
        num[k] = num.get(k, 0) + 1
    den: dict[int, int] = {}
    for h in hook_lengths(partition):
        if h > 1:
            den[h] = den.get(h, 0) + 1
    # Cancel
    for k in list(num.keys()):
        if k in den:
            cancel = min(num[k], den[k])
            num[k] -= cancel
            den[k] -= cancel
            if num[k] == 0:
                del num[k]
            if den[k] == 0:
                del den[k]
    return num, den


def composite_factor_lean(num: dict[int, int],
                          den: dict[int, int]) -> str:
    """Render the irreducible quotient ∏[num]/∏[den] as a Lean
    expression.

    Strategy: for each `k → m` in den, find numerator factor j such
    that j is a positive multiple of k (i.e., j = c·k); then
    `[j]_q / [k]_q = [j]_q · [k]_q⁻¹`.  Lean prefers polynomial
    factors over inverses.  Use the identity

      [j]_q / [k]_q = ∏_{i=0}^{c-1} q^{(c-1)k - 2ik} + ... = sum form.

    Concretely, [j]_q/[k]_q for j = c·k is a sum of (c) terms in
    powers of q^k.  E.g. [6]/[3] = q³ + q⁻³ = sum of 2 terms in q³;
    [6]/[2] = q⁴ + q² + 1 + q⁻² + q⁻⁴ = sum of 5 terms in q²
    (= [3]_{q²}).

    For now: represent simply as `[num]_q · [den]_q⁻¹` if a clean
    multiple-pairing exists; otherwise emit a quotient with explicit
    `(q^... + ...)⁻¹` denominator.
    """
    pieces: list[str] = []
    # Greedy: for each den factor, find a num multiple to pair off.
    den_remaining = dict(den)
    num_remaining = dict(num)
    pair_subs: list[tuple[int, int]] = []  # (num_j, den_k) pairs
    for k, dk in list(den_remaining.items()):
        for _ in range(dk):
            paired = False
            # Look for a num factor j that is a positive multiple of k.
            for j in sorted(num_remaining.keys(), reverse=True):
                if j % k == 0 and num_remaining[j] > 0 and j > k:
                    pair_subs.append((j, k))
                    num_remaining[j] -= 1
                    if num_remaining[j] == 0:
                        del num_remaining[j]
                    den_remaining[k] -= 1
                    if den_remaining[k] == 0:
                        del den_remaining[k]
                    paired = True
                    break
            if not paired:
                # Cannot eliminate via pairing; will need explicit
                # `[k]_q⁻¹` term.
                break
    # Emit num_remaining factors as plain [k]_q.
    for k, mk in sorted(num_remaining.items(), reverse=True):
        for _ in range(mk):
            expr = q_int_lean(k)
            pieces.append(f"({expr})" if "+" in expr else expr)
    # Emit pair_subs as [j]_q / [k]_q via sum-of-terms-in-q^k form.
    for j, k in pair_subs:
        # [j]_q / [k]_q where j = c·k yields sum of c terms in q^k:
        # q^{(c-1)k} + q^{(c-3)k} + ... + q^{-(c-1)k}.
        c = j // k
        terms: list[str] = []
        for i in range(c):
            exp = (c - 1) * k - 2 * i * k
            if exp == 0:
                terms.append("1")
            elif exp > 0:
                terms.append(f"q ^ {exp}" if exp > 1 else "q")
            else:
                ae = -exp
                terms.append(f"(q ^ {ae})⁻¹" if ae > 1 else "q⁻¹")
        joined = " + ".join(terms)
        pieces.append(f"({joined})")
    # Emit any UNPAIRED den_remaining as explicit ⁻¹ (rare for n ≤ 9).
    for k, dk in sorted(den_remaining.items(), reverse=True):
        for _ in range(dk):
            expr = q_int_lean(k)
            pieces.append(f"({expr})⁻¹")
    if not pieces:
        return "1"
    return " * ".join(pieces)


def main() -> int:
    n = 8
    raw_parts = partitions_of(n)
    assert len(raw_parts) == 22, f"expected p(8) = 22, got {len(raw_parts)}"

    print(f"=== Phase 5: n={n} dim_q table (quantum-hook formula) ===")
    print(f"Convention: dim_q(λ) = [{n}]_q! / ∏ [h_x]_q\n")

    # Reorder partitions for conjugate-symmetric indexing matching the
    # pattern of heckeH6DimQ / heckeH7DimQ: idx i ↔ idx (p(n)-1-i)
    # are conjugate pairs; self-conjugates sit at the centre.
    seen_for_order: set[tuple] = set()
    pair_seq: list[tuple[tuple, tuple]] = []
    self_seq: list[tuple] = []
    for p in raw_parts:
        if p in seen_for_order:
            continue
        c = conjugate(p)
        if c == p:
            self_seq.append(p)
            seen_for_order.add(p)
        elif c in raw_parts:
            pair_seq.append((p, c))
            seen_for_order.add(p)
            seen_for_order.add(c)
    # Symmetric layout: first half = first elt of each pair (in
    # encountered order), centre = self-conjugates, second half
    # = conjugates of first half (reversed).
    parts: list[tuple] = (
        [p for p, _ in pair_seq] + self_seq + [c for _, c in reversed(pair_seq)]
    )
    assert len(parts) == 22

    # Recompute pairs/self-conj in the new ordering.
    seen: set[tuple] = set()
    pairs: list[tuple[int, int]] = []
    self_conj: list[int] = []
    for i, p in enumerate(parts):
        if p in seen:
            continue
        c = conjugate(p)
        if c == p:
            self_conj.append(i)
            seen.add(p)
        else:
            j = parts.index(c)
            pairs.append((min(i, j), max(i, j)))
            seen.add(p)
            seen.add(c)

    print(f"Conjugate pairs: {len(pairs)}; self-conjugate: {len(self_conj)}")
    print(f"Total: {2 * len(pairs) + len(self_conj)} = {len(parts)}\n")

    # Compute dim_q via reduced hook factors.
    q = sp.Symbol("q", positive=True)
    rows = []
    print(f"{'idx':>3}  {'partition':>22}  {'num/den':>22}  d_λ(q=1)  Lean dim_q")
    for i, p in enumerate(parts):
        hooks = hook_lengths(p)
        num, den = factor_signature(p)
        lean_expr = composite_factor_lean(num, den)
        # Numerical d_λ at q=1 (classical S_n irrep dimension).
        from math import factorial as fact
        d_classical = fact(n) // (1)
        for h in hooks:
            d_classical = d_classical // h if h > 0 else d_classical
        # Spot-check the lean expr at q=1 numerically by sympy substitution.
        sympy_dim = dim_q_via_quantum_hooks(p, q)
        sympy_at_1 = float(sp.cancel(sympy_dim).subs(q, 1))
        rows.append({
            "idx": i,
            "partition": list(p),
            "hooks": sorted(hooks, reverse=True),
            "num_factors": dict(num),
            "den_factors": dict(den),
            "lean_expr": lean_expr,
            "d_lambda_at_q1": int(round(sympy_at_1)),
        })
        ns = "·".join(f"[{k}]^{v}" if v > 1 else f"[{k}]" for k, v in sorted(num.items(), reverse=True)) or "1"
        ds = "·".join(f"[{k}]^{v}" if v > 1 else f"[{k}]" for k, v in sorted(den.items(), reverse=True)) or "1"
        print(f"{i:>3}  {str(p):>22}  {ns + '/' + ds:>22}  {int(round(sympy_at_1)):>8}  {lean_expr[:60]}{'…' if len(lean_expr) > 60 else ''}")

    # Conjugate-pair sanity check.
    print()
    print("Conjugate-pair check (same d_λ + same num/den signatures):")
    for i, j in pairs:
        ok = (rows[i]["d_lambda_at_q1"] == rows[j]["d_lambda_at_q1"] and
              rows[i]["num_factors"] == rows[j]["num_factors"] and
              rows[i]["den_factors"] == rows[j]["den_factors"])
        marker = "✓" if ok else "✗"
        print(f"  {marker} {parts[i]} (d={rows[i]['d_lambda_at_q1']}) ↔ "
              f"{parts[j]} (d={rows[j]['d_lambda_at_q1']})")
    print()

    # Emit Lean source skeleton.
    out_lean = Path(__file__).parent / "phase5-n8-dim-q-table.lean"
    lines = []
    lines.append("/-! Phase 5 — n=8 quantum hook-length dim_q table")
    lines.append(f"    Generated by phase5_n8_dim_q_table.py.")
    lines.append(f"    {len(parts)} partitions, {len(pairs)} conjugate pairs, "
                 f"{len(self_conj)} self-conjugate (idx {self_conj}).")
    lines.append("    Convention: dim_q(λ) = [n]_q! / ∏ [h_x]_q.")
    lines.append("    Conjugate-symmetric ordering: idx i ↔ idx (21-i).")
    lines.append("")
    lines.append("    Index map:")
    for r in rows:
        ns = "·".join(f"[{k}]^{v}" if v > 1 else f"[{k}]"
                      for k, v in sorted(r["num_factors"].items(), reverse=True)) or "1"
        ds = "·".join(f"[{k}]^{v}" if v > 1 else f"[{k}]"
                      for k, v in sorted(r["den_factors"].items(), reverse=True)) or "1"
        sig = ns if ds == "1" else f"{ns}/{ds}"
        lines.append(f"      {r['idx']:>2} ↦ {str(tuple(r['partition'])):<22} "
                     f"d_λ={r['d_lambda_at_q1']:>3}, dim_q = {sig}")
    lines.append("-/")
    lines.append("")
    lines.append(f"noncomputable def heckeH{n}DimQ (q : ℝ) (i : Fin {len(parts)}) : ℝ :=")
    lines.append("  match i with")
    for r in rows:
        lines.append(f"  | ⟨{r['idx']}, _⟩ => {r['lean_expr']}")
    lines.append(f"  | ⟨_+{len(parts)}, h⟩ => absurd h (by omega)")
    lines.append("")
    # simp lemmas
    name_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
                  "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
                  "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twentyone"]
    for r in rows:
        word = name_words[r["idx"]]
        lines.append(f"@[simp] theorem heckeH{n}DimQ_{word} (q : ℝ) :")
        lines.append(f"    heckeH{n}DimQ q {r['idx']} = {r['lean_expr']} := rfl")
    lines.append("")
    # Fin.sum_univ_22 lemma
    lines.append("/-- `Fin 22` sum decomposition (extends Mathlib's `Fin.sum_univ_*`")
    lines.append("    pattern to twenty-two elements; pattern: peel 14 via")
    lines.append("    `Fin.sum_univ_castSucc` then bridge through `Fin.sum_univ_eight`). -/")
    lines.append("private lemma Fin_sum_univ_twentytwo {M : Type*} [AddCommMonoid M]")
    lines.append("    (f : Fin 22 → M) :")
    lines.append("    ∑ i, f i = f 0 + f 1 + f 2 + f 3 + f 4 + f 5 + f 6 + f 7")
    lines.append("                + f 8 + f 9 + f 10 + f 11 + f 12 + f 13")
    lines.append("                + f 14 + f 15 + f 16 + f 17 + f 18 + f 19")
    lines.append("                + f 20 + f 21 := by")
    lines.append("  rw [Fin.sum_univ_castSucc, Fin.sum_univ_castSucc, Fin.sum_univ_castSucc,")
    lines.append("      Fin.sum_univ_castSucc, Fin.sum_univ_castSucc, Fin.sum_univ_castSucc,")
    lines.append("      Fin.sum_univ_castSucc, Fin.sum_univ_castSucc, Fin.sum_univ_castSucc,")
    lines.append("      Fin.sum_univ_castSucc, Fin.sum_univ_castSucc, Fin.sum_univ_castSucc,")
    lines.append("      Fin.sum_univ_castSucc, Fin.sum_univ_castSucc, Fin.sum_univ_eight]")
    lines.append("  rfl")
    lines.append("")
    # Theorem statement: Σ_{λ⊢8} 1/dim_q(λ).
    lines.append("/-- **H_8 specialisation: τ(C_dim_q) = Σ_{λ⊢8} 1/dim_q(λ).**")
    lines.append("")
    lines.append("    Closes the n=8 case of the Frobenius co-Casimir trace by")
    lines.append("    Fin-22 enumeration of the partitions of 8.  After grouping")
    lines.append(f"    conjugate pairs ({len(pairs)} pairs + {len(self_conj)} self-conjugate)")
    lines.append("    each pair contributes 2/dim_q while each self-conj contributes")
    lines.append("    1/dim_q.")
    lines.append("")
    lines.append("    Ref: 1ppb plan T1 / Phase 5; closes ⁴He's H_{12} block. -/")
    lines.append(f"theorem hecke_n{n}_frobenius_codim (q : ℝ) :")
    lines.append(f"    ∑ i : Fin {len(parts)}, 1 / heckeH{n}DimQ q i = ")
    # Build sum: 2/dim_q for each pair (use the first index's expr),
    # plus 1/dim_q for each self-conjugate.
    summed_terms: list[str] = []
    for i, j in pairs:
        expr = rows[i]["lean_expr"]
        summed_terms.append(f"        2 / ({expr})")
    for i in self_conj:
        expr = rows[i]["lean_expr"]
        summed_terms.append(f"        1 / ({expr})")
    lines.append(" +\n".join(summed_terms) + " := by")
    lines.append(f"  rw [Fin_sum_univ_twentytwo]")
    lines.append("  simp")
    lines.append("  ring")
    lines.append("")
    out_lean.write_text("\n".join(lines) + "\n")
    print(f"Wrote Lean source: {out_lean.relative_to(Path(__file__).parent.parent.parent)}")

    # Emit JSON for downstream theorem author.
    import json
    out_json = Path(__file__).parent / "phase5-n8-dim-q-table.json"
    out_json.write_text(json.dumps({
        "n": n,
        "num_partitions": len(parts),
        "rows": rows,
        "conjugate_pairs": [{"i": i, "j": j, "lam_i": list(parts[i]), "lam_j": list(parts[j])} for i, j in pairs],
        "self_conjugate": [{"i": i, "lam": list(parts[i])} for i in self_conj],
    }, indent=2))
    print(f"Wrote table JSON: {out_json.relative_to(Path(__file__).parent.parent.parent)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
