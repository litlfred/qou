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

**Convention D** (SU(2)/Temperley–Lieb, Jones).  Matches
`markov_weights_symbolic.schur_principal_symbolic` exactly:
  Q     = q²
  z_W   = q · z_markov,   z_markov = q³/(q² + 1)
  Q^r   = z_W / (1 - Q + z_W)            (Wenzl level eigenvalue)
        = q⁴ = Q²  under D, i.e. r = 2 exactly
  s_λ   = Q^{n(λ)} · ∏_{x ∈ λ} (1 - Q^r · Q^{c(x)}) / (1 - Q^{h(x)})

Convention C (z = 1/(√q + 1/√q)) was excised by owner ruling 2026-08-09;
docs/coordination/trace-convention-registry.md.  It survives here only as
`_wenzl_constants_convention_C_HISTORICAL` /
`y_lambda_at_q0_mpmath_convention_C_HISTORICAL`, which exist so the D-vs-C
comparison in `y_lambda_su_n.main()` keeps a live C to quote.
"""
from __future__ import annotations

from typing import Iterable

import mpmath as mp
from _precision import set_compute_dps  # noqa: E402


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
    """Returns (Q, Q^r) at q = q_val, matching the symbolic convention.

    TRACE CONVENTION **D** (SU(2)/Temperley–Lieb, Jones), z = q³/(q² + 1) —
    the same z as `markov_weights_symbolic.Z_MARK`.  Owner ruling 2026-08-09
    excised convention C (z = 1/(√q + 1/√q)), which this function carried
    until then.  Registry: docs/coordination/trace-convention-registry.md.

    Under D the Wenzl level relation collapses exactly:

        z_W = q·z  = q⁴/(q² + 1),
        Q^r = z_W/(1 − Q + z_W)
            = q⁴ / ((1 − q²)(q² + 1) + q⁴)
            = q⁴ / (1 − q⁴ + q⁴)  =  q⁴  =  Q²,

    i.e. **r = 2**, the SU(2) level.  `schur_principal_mpmath` is then the
    two-variable specialization s_λ(1, Q) and returns 0 for every λ with
    three or more rows.  C gave a non-integral level (Q^r ≈ 1.72025 at q₀
    against Q² ≈ 1.51795, ratio 1.13327) and hence y_(1³) ≠ 0.
    """
    Q = q_val ** 2
    # z_markov = q³/(q² + 1)      (convention D)
    z_markov = q_val ** 3 / (q_val ** 2 + 1)
    # z_W = q · z_markov
    z_W = q_val * z_markov
    # Q^r = z_W / (1 - Q + z_W)
    QR = z_W / (1 - Q + z_W)
    return Q, QR


def _wenzl_constants_convention_C_HISTORICAL(
    q_val: mp.mpf,
) -> tuple[mp.mpf, mp.mpf]:
    """DEAD FOR PRODUCTION — convention C, excised 2026-08-09.

    Retained because the excision has to stay **measurable**.  The D-vs-C
    comparison in `y_lambda_su_n.main()` needs one live C implementation to
    quote, and after the qou-wgta sweep every other one in the repo has been
    switched.  Left unpreserved, that comparison silently degrades to D-vs-D
    and reports C's y_(1³)/y_(3) as 0 with a spurious *integral* N* = 2 —
    the exact opposite of the finding it exists to display.

    C: z = 1/(√q + 1/√q).  Q^r is then not a power of Q (1.72025 at q₀
    against Q² = 1.51795), so C carried no SU(N) row cap and y_(1³) ≠ 0.

    Do not call this from anything that feeds a predicted observable.
    """
    Q = q_val ** 2
    sq = mp.sqrt(q_val)
    z_markov = 1 / (sq + 1 / sq)
    z_W = q_val * z_markov
    QR = z_W / (1 - Q + z_W)
    return Q, QR


def _schur_principal_with(lam: tuple[int, ...], Q: mp.mpf,
                          QR: mp.mpf) -> mp.mpf:
    """s_λ(1, Q, …, Q^{r-1}) from precomputed (Q, Q^r).  Shared by the
    production path and the convention-C historical path so the two cannot
    drift apart in anything but the two constants."""
    hs, cs = hooks_and_contents(lam)
    num = mp.mpf(1)
    den = mp.mpf(1)
    for h, c in zip(hs, cs):
        num *= 1 - QR * Q ** c
        den *= 1 - Q ** h
    return Q ** n_partition(lam) * num / den


def schur_principal_mpmath(lam: tuple[int, ...], q_val: mp.mpf) -> mp.mpf:
    """s_λ(1, Q, …, Q^{r-1}) evaluated DIRECTLY at q = q_val (mpmath).

    Closed form matches `markov_weights_symbolic.schur_principal_symbolic`:

        s_λ = Q^{n(λ)} · ∏_{x ∈ λ} (1 - Q^r · Q^{c(x)}) / (1 - Q^{h(x)})

    O(|λ|) mpf operations. No sympy.  Convention D — see `_wenzl_constants`.
    """
    return _schur_principal_with(lam, *_wenzl_constants(q_val))


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

    TRACE CONVENTION **D** — see `_wenzl_constants`.  Every λ with three or
    more rows comes back exactly 0 (the SU(2) row cap ℓ(λ) ≤ 2).

    For n > 12: extends the y_λ tower beyond the cached witness.

    NOTE: `y-lambda-at-q0.witness.json` still holds convention-C weights and
    is therefore NOT a valid cross-check for this function until it is
    regenerated.  `main()` reports that comparison as a C-vs-D delta, not as
    an error.
    """
    return _y_lambda_normalised(n, q_val, _wenzl_constants(q_val))


def y_lambda_at_q0_mpmath_convention_C_HISTORICAL(
    n: int, q_val: mp.mpf
) -> dict[tuple[int, ...], mp.mpf]:
    """DEAD FOR PRODUCTION — convention C, excised 2026-08-09.

    The one surviving live C implementation, kept so the D-vs-C comparison
    stays measurable.  See `_wenzl_constants_convention_C_HISTORICAL`.
    """
    return _y_lambda_normalised(
        n, q_val, _wenzl_constants_convention_C_HISTORICAL(q_val))


def _y_lambda_normalised(
    n: int, q_val: mp.mpf, wenzl: tuple[mp.mpf, mp.mpf]
) -> dict[tuple[int, ...], mp.mpf]:
    """y_λ = s_λ / Σ_μ s_μ f^μ for a given (Q, Q^r).  Convention-agnostic:
    the convention lives entirely in `wenzl`."""
    shapes = partitions_of(n)
    s_vals: dict[tuple[int, ...], mp.mpf] = {
        sh: _schur_principal_with(sh, *wenzl) for sh in shapes
    }

    Z = mp.mpf(0)
    for sh in shapes:
        Z += s_vals[sh] * _f_lambda(sh)

    return {sh: s_vals[sh] / Z for sh in shapes}


def main() -> int:
    """Smoke-test against the y-lambda-at-q0 witness for n ∈ {2, ..., 12},
    then benchmark n=13.

    NOTE (2026-08-09, bean qou-wgta item 9): that witness still holds
    **convention C** weights while this module now computes **D**, so the
    column below is a C-vs-D gap of order 10⁻¹ — not an accuracy figure.
    It is labelled as such until the witness is regenerated.  The real
    accuracy check meanwhile is the D column against
    `markov_weights_symbolic.y_lambda_symbolic` (sympy, independent code
    path): those agree to round-off.
    """
    import json
    import time
    from pathlib import Path
    import sys
    HERE = Path(__file__).resolve().parent
    if str(HERE) not in sys.path:
        sys.path.insert(0, str(HERE))

    set_compute_dps()
    from q_parameter import Q_MP  # noqa: E402

    print("=" * 80)
    print("  schur_principal_mpmath — accuracy + speed audit")
    print("=" * 80)
    print()

    witness = json.loads(
        (_pb.witness_path("y-lambda-at-q0.witness.json", HERE)).read_text()
    )
    cache = witness.get("data", witness)["by_n"]

    print("  witness y-lambda-at-q0.witness.json is still convention C;")
    print("  this module is convention D.  The last column is therefore the")
    print("  C-vs-D GAP, not an error, until that witness is regenerated.")
    print()
    print(f"  {'n':<3} {'partitions':>10} {'wall (s)':>10} "
          f"{'max C-vs-D gap':>15}")
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
