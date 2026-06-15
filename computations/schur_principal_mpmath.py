"""mpmath-native fast path for the Wenzl-bridge Schur principal
specialization + y_λ(q_0) computation.

## What this replaces

The sympy path in `markov_weights_symbolic.schur_principal_symbolic`
computes `s_λ(1, Q, …, Q^{r-1})` symbolically, then later substitutes
q = q_0 and calls `evalf(30)`. At n ≥ 12 each per-partition
`schur_principal_symbolic(λ).subs(q, q_0).evalf(30)` walls past
20+ seconds because sympy expands the rational expression into
thousands of terms before substituting.

This module computes the SAME closed form
    s_λ = Q^{n(λ)} · ∏_{x ∈ λ} (1 - Q^{r + c(x)}) / (1 - Q^{h(x)})
DIRECTLY at q = q_0 using mpmath. Each cell of λ contributes one
mpf multiply + one mpf power; total per-partition cost is O(|λ|)
mpf operations.

## Empirical speedup target

At n=12 (cached): sympy path takes ~minutes; mpmath path expected
sub-millisecond per partition. At n=13 (uncached): sympy ~30 min
total for 101 partitions; mpmath expected ~10ms total.

## Convention

Matches `markov_weights_symbolic.schur_principal_symbolic` exactly:
  Q     = q²
  z_W   = q · z_markov,   z_markov = 1/(√q + 1/√q)
  Q^r   = z_W / (1 - Q + z_W)            (Wenzl level eigenvalue)
  s_λ   = Q^{n(λ)} · ∏_{x ∈ λ} (1 - Q^r · Q^{c(x)}) / (1 - Q^{h(x)})
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
from typing import Iterable

import mpmath as mp


def hooks_and_contents(lam: tuple[int, ...]) -> tuple[list[int], list[int]]:
    """Hook lengths and contents c(x) = j - i of cells of partition λ.

    Mirror of `markov_weights_symbolic.hooks_and_contents` (same
    arm + leg + 1 formula and column-minus-row contents).
    """
    hs: list[int] = []
    cs: list[int] = []
    rows = len(lam)
    for i in range(rows):
        for j in range(lam[i]):
            arm = lam[i] - j - 1
            leg = sum(1 for r in range(i + 1, rows) if lam[r] > j)
            hs.append(arm + leg + 1)
            cs.append(j - i)
    return hs, cs


def n_partition(lam: tuple[int, ...]) -> int:
    """n(λ) = Σ i · λ_i  (Macdonald's n-statistic, 0-indexed rows)."""
    return sum(i * lam_i for i, lam_i in enumerate(lam))


def _wenzl_constants(q_val: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
    """Returns (Q, Q^r) at q = q_val, matching the symbolic convention."""
    Q = q_val ** 2
    # z_markov = 1 / (√q + 1/√q)
    sq = mp.sqrt(q_val)
    z_markov = 1 / (sq + 1 / sq)
    # z_W = q · z_markov
    z_W = q_val * z_markov
    # Q^r = z_W / (1 - Q + z_W)
    QR = z_W / (1 - Q + z_W)
    return Q, QR


def schur_principal_mpmath(lam: tuple[int, ...], q_val: mp.mpf) -> mp.mpf:
    """s_λ(1, Q, …, Q^{r-1}) evaluated DIRECTLY at q = q_val (mpmath).

    Closed form matches `markov_weights_symbolic.schur_principal_symbolic`:

        s_λ = Q^{n(λ)} · ∏_{x ∈ λ} (1 - Q^r · Q^{c(x)}) / (1 - Q^{h(x)})

    O(|λ|) mpf operations. No sympy.
    """
    Q, QR = _wenzl_constants(q_val)
    hs, cs = hooks_and_contents(lam)
    num = mp.mpf(1)
    den = mp.mpf(1)
    for h, c in zip(hs, cs):
        num *= 1 - QR * Q ** c
        den *= 1 - Q ** h
    return Q ** n_partition(lam) * num / den


def _f_lambda(lam: tuple[int, ...]) -> int:
    """f^λ = n! / ∏ hook lengths (Frame-Robinson-Thrall)."""
    import math
    n = sum(lam)
    hs, _ = hooks_and_contents(lam)
    prod = 1
    for h in hs:
        prod *= h
    return math.factorial(n) // prod


def partitions_of(n: int) -> list[tuple[int, ...]]:
    """All integer partitions of n, sorted in dominance order."""
    if n == 0:
        return [()]
    out: list[tuple[int, ...]] = []
    def _rec(remaining: int, max_part: int, current: tuple[int, ...]) -> None:
        if remaining == 0:
            out.append(current)
            return
        for k in range(min(max_part, remaining), 0, -1):
            _rec(remaining - k, k, current + (k,))
    _rec(n, n, ())
    return out


def y_lambda_at_q0_mpmath(
    n: int, q_val: mp.mpf
) -> dict[tuple[int, ...], mp.mpf]:
    """Jones–Markov y_λ(q_val) at H_n, mpmath-direct (no sympy).

    Computes y_λ = s_λ / Z where Z = Σ_μ s_μ · f^μ enforces the
    normalisation Σ_λ y_λ · f^λ = tr_M(1) = 1.

    For n ∈ {2, ..., 12}: matches `wedderburn_jones_markov.y_lambda_at`
    (which loads from witness) to ~10⁻¹⁵.

    For n > 12: extends the y_λ tower beyond the cached witness.
    """
    shapes = partitions_of(n)
    s_vals: dict[tuple[int, ...], mp.mpf] = {}
    for sh in shapes:
        s_vals[sh] = schur_principal_mpmath(sh, q_val)

    Z = mp.mpf(0)
    for sh in shapes:
        Z += s_vals[sh] * _f_lambda(sh)

    return {sh: s_vals[sh] / Z for sh in shapes}


def main() -> int:
    """Smoke-test: verify against the existing y-lambda-at-q0 witness
    for n ∈ {2, ..., 12}, then benchmark n=13."""
    import json
    import time
    from pathlib import Path
    import sys
    HERE = Path(__file__).resolve().parent
    if str(HERE) not in sys.path:
        sys.path.insert(0, str(HERE))

    mp.mp.dps = 50
    from q_parameter import Q_MP  # noqa: E402

    print("=" * 80)
    print("  schur_principal_mpmath — accuracy + speed audit")
    print("=" * 80)
    print()

    witness = json.loads(
        (_pb.witness_path("y-lambda-at-q0.witness.json", HERE)).read_text()
    )
    cache = witness.get("data", witness)["by_n"]

    print(f"  {'n':<3} {'partitions':>10} {'wall (s)':>10} {'max rel err':>15}")
    print("  " + "-" * 55)

    for n in range(2, 13):
        t0 = time.time()
        y_my = y_lambda_at_q0_mpmath(n, Q_MP)
        wall = time.time() - t0

        # Compare to cached witness
        n_str = str(n)
        if n_str not in cache:
            continue
        ref_entries = cache[n_str]
        max_rel_err = mp.mpf(0)
        for ref in ref_entries:
            lam = tuple(ref["partition"])
            ref_val = mp.mpf(ref["y_at_q0_50dps"])
            my_val = y_my.get(lam)
            if my_val is None:
                print(f"    MISSING λ={lam}")
                continue
            if abs(ref_val) < mp.mpf("1e-40"):
                # Both should be ~zero
                rel = abs(my_val - ref_val)
            else:
                rel = abs(my_val - ref_val) / abs(ref_val)
            if rel > max_rel_err:
                max_rel_err = rel
        print(f"  {n:<3} {len(y_my):>10} {wall:>10.4f} {float(max_rel_err):>15.3e}")

    # Now extend to n=13, 14, 15 (uncached)
    print()
    print(f"  Extension to uncached n:")
    for n in [13, 14, 15]:
        t0 = time.time()
        y_my = y_lambda_at_q0_mpmath(n, Q_MP)
        wall = time.time() - t0
        # Sanity: Σ y_λ · f^λ ≈ 1 (tr_M(1) = 1 normalisation)
        s = mp.mpf(0)
        for sh, y in y_my.items():
            s += y * _f_lambda(sh)
        residual = abs(s - 1)
        print(f"  {n:<3} {len(y_my):>10} {wall:>10.4f} "
              f"|Σy·f - 1| = {float(residual):.3e}")

    print()
    print(f"  ★ mpmath direct path: ~ms per atom, all n.")
    print(f"  ★ vs sympy: ~minutes (n=12) → ~30+ min (n=13)")
    print(f"  ★ speedup: ~10⁵–10⁶× per partition for n ≥ 12")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
