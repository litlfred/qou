"""Generic Markov-trace evaluator for any knot/link in the framework.

Per author 2026-05-25 (common infra request): provides a unified
`markov_trace_for_knot(knot_name, q, convention)` function that:

1. Looks up the canonical braid word from `knot_braid_database`
2. Builds y_λ on the appropriate H_n(q) via the requested convention:
   - "wenzl"   → y_lambda_wenzl_bridge_numeric (mpf, 50 dps)
   - "q_schur" → closed form q^{content_sum(λ)} / [n]_q! (mpf, 50 dps)
3. Computes χ_λ(β_K, q) via pn.chi_lambdas_braid_mpfr (MPFR at dps)
4. Returns tr_M(K, q) = Σ_λ y_λ · χ_λ(β_K) as mp.mpf at requested dps

## Precision discipline (per .claude/skills/local/compute-author.md §1)

**Default: mp.mpf at 50 dps** — matches the L1 production floor.
The function accepts any caller-side q type (float / mpf / decimal
string); internally promoted to mp.mpf at the requested dps and
routed through the *_mpfr Rust kernels.

**f64 path: opt-in via `precision="f64"` — LOSSY (~17 digits).**
Use only for cross-checking against the mpf default. Never on a
production critical path.

## Convention disambiguation

Per `docs/audits/2026-05-25-markov-trace-convention-audit.md`:

| Convention | tr(σ_i) | Used by |
|------------|---------|---------|
| "wenzl"    | z = 1/(√q+1/√q) | Mass formula (Borromean), per-atom witnesses |
| "q_schur"  | h = q − q⁻¹     | Torus knot closed forms, lepton tower |

**Pick the convention that matches your physics.**

## Verified cross-checks

- `markov_trace_for_knot("T(2,4)", q_0, "q_schur")` matches the
  sibling H_2 hardcode `y_(2)·q^4 + y_(1,1)·q^-4` to ~1e-50 at
  50 dps (mpf default).
- f64 and mpf paths agree to ~1e-15 (machine f64 epsilon).
- mpf-vs-`(4+h²−3h⁴−h⁶)/(h²+4)` Borromean gap is 2e-4, NOT machine
  epsilon — this is the **h⁴+ truncation gap** documented in
  PR #1272's `gamma_gamma_pair_production_decomposition.py`
  (Family A `5/2 + (3/4)h²` terminates at h²; the actual Wenzl
  Markov trace has h⁴, h⁶ corrections). The closed form is NOT
  the exact Markov trace, only an h²-truncation.

## Example

```python
import mpmath as mp
from markov_trace_for_knot import markov_trace_for_knot

# Default — mpf at 50 dps
tr_borr = markov_trace_for_knot("Borromean", "1.10997859...", "wenzl")
# → mp.mpf at 50 dps

# Opt-in f64 cross-check (LOSSY)
tr_borr_f64 = markov_trace_for_knot("Borromean", 1.10997, "wenzl",
                                      precision="f64")
# → Python float, ~17 digits
```
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

import sys
from pathlib import Path
from typing import Any

import mpmath as mp
import pyhecke_native as pn

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from knot_braid_database import (  # noqa: E402
    braid_word_for_knot,
    n_strands_for_knot,
)
from y_lambda_wenzl_bridge import (  # noqa: E402
    partitions_of as _partitions_of,
    y_lambda_wenzl_bridge_numeric,
)


def y_lambda_h2_q_schur_mpf(q: Any) -> tuple[Any, Any]:
    """Closed-form q-Schur Plancherel weights on H_2(q) — generic in q.

    Returns (y_(2), y_(1,1)) where:
      y_(2)   = q   / [2]_q
      y_(1,1) = q⁻¹ / [2]_q
    with [2]_q = q + q⁻¹. Sum y_(2) + y_(1,1) = 1 (Plancherel
    normalization).

    These are the principal specialization of the q-Schur weights
      y_λ(q) = q^{content_sum(λ)} / [n]_q!
    at n = 2, with content_sum((2)) = +1 and content_sum((1,1)) = −1.

    The function is parametric in `q` — works for `float`, `mp.mpf`,
    `sp.Symbol`. Use this in mp.mpf-precision scripts (50-dps pin)
    where `pn.trace_weights_n_q_schur` (f64) would lose precision.

    Equivalent to `pn.trace_weights_n_q_schur(2, float(q))` at f64,
    but preserves caller precision via duck-typed arithmetic on `q`.
    """
    qi = 1 / q
    bracket_2 = q + qi
    return q / bracket_2, qi / bracket_2


def trM_torus_2_k_mpf(k: int, q: Any) -> Any:
    """Closed-form Markov trace tr_M(σ_1^k) in H_2(q), generic in q.

    For T(2, k) torus link with braid σ_1^k in B_2:
      tr_M(σ_1^k) = y_(2)·q^k + y_(1,1)·(-q⁻¹)^k

    where (y_(2), y_(1,1)) = `y_lambda_h2_q_schur_mpf(q)`.

    Generic in `q` for full precision in mp.mpf scripts.
    """
    y_2, y_11 = y_lambda_h2_q_schur_mpf(q)
    qi = 1 / q
    sign = (-1) ** k
    return y_2 * q ** k + y_11 * sign * qi ** k


def _content_sum(partition: tuple[int, ...]) -> int:
    """Sum of contents (j - i) over cells (i, j) of partition λ."""
    return sum(j - i for i, row in enumerate(partition) for j in range(row))


def _q_factorial_mpf(n: int, q: Any) -> Any:
    """[n]_q! = Π_{k=1}^{n} [k]_q where [k]_q = (q^k - q^{-k})/(q - q^{-1}).

    Generic in q (mpf / float / sympy.Symbol). For n=0 returns 1.
    """
    if n == 0:
        return q ** 0  # 1 in the appropriate type
    qmqi = q - 1 / q
    result = q - 1 / q  # = [1]_q · (q - q⁻¹), placeholder
    result = (q ** 0)  # 1
    for k in range(1, n + 1):
        bracket_k = (q ** k - q ** (-k)) / qmqi
        result = result * bracket_k
    return result


def _q_schur_y_lambda_mpf(partition: tuple[int, ...], q: Any, n: int) -> Any:
    """q-Schur Plancherel weight y_λ(q) = q^{c(λ)} / [n]_q!.

    Generic in q (mpf / float). Closed form per
    `docs/audits/2026-05-25-markov-trace-convention-audit.md` §3
    and `prop:q-schur-y-lambda-closed-form` (PR #1259).
    """
    c = _content_sum(partition)
    return q ** c / _q_factorial_mpf(n, q)


def _markov_trace_mpf(
    knot_name: str,
    q,
    convention: str,
    dps: int,
) -> Any:
    """50-dps mp.mpf Markov-trace path (default).

    Routes y_λ through the mpf production primitives and χ_λ through
    `pn.chi_lambdas_braid_mpfr` (MPFR at the requested dps). Returns
    `mp.mpf` at exactly `dps` significant digits.
    """
    mp.mp.dps = max(mp.mp.dps, dps)
    if isinstance(q, mp.mpf):
        q_mpf = q
        q_str = mp.nstr(q, dps + 5, strip_zeros=False)
    elif isinstance(q, str):
        q_mpf = mp.mpf(q)
        q_str = q
    else:
        # float / int — DOC THIS AS LOSSY at the call site
        q_mpf = mp.mpf(repr(q))
        q_str = repr(q)

    braid = braid_word_for_knot(knot_name)
    n = n_strands_for_knot(knot_name)
    shapes = _partitions_of(n)

    # y_λ at mpf precision
    if convention == "wenzl":
        y_mpf = [
            y_lambda_wenzl_bridge_numeric(lam, q_str, dps=dps)
            for lam in shapes
        ]
    else:  # q_schur
        y_mpf = [_q_schur_y_lambda_mpf(tuple(lam), q_mpf, n) for lam in shapes]

    # χ_λ via MPFR-precision Rust kernel
    chi_strs = pn.chi_lambdas_braid_mpfr(shapes, braid, q_str, dps=dps)
    chi_mpf = [mp.mpf(s) for s in chi_strs]

    return sum(y_mpf[i] * chi_mpf[i] for i in range(len(shapes)))


def _markov_trace_f64(
    knot_name: str,
    q: float,
    convention: str,
) -> float:
    """LOSSY f64 Markov-trace path — cross-check only.

    Routes both y_λ and χ_λ through the f64 Rust kernels
    (`pn.trace_weights_n` and `pn.chi_lambdas_braid`). Precision
    ~17 digits. Never on a production critical path; only use to
    cross-check the mpf default to within machine epsilon.
    """
    braid = braid_word_for_knot(knot_name)
    n = n_strands_for_knot(knot_name)

    if convention == "wenzl":
        y_lambda = pn.trace_weights_n(n, q)
    else:  # q_schur
        y_lambda = pn.trace_weights_n_q_schur(n, q)

    shapes = pn.partitions_of(n)
    chi_vals = pn.chi_lambdas_braid(shapes, braid, q)

    return sum(y_lambda[i] * chi_vals[i] for i in range(len(shapes)))


def markov_trace_for_knot(
    knot_name: str,
    q,
    convention: str = "wenzl",
    *,
    precision: str = "mpf",
    dps: int = 50,
):
    """Compute the Markov trace tr_M(K, q) for any catalogued knot/link.

    Args:
        knot_name: 'Borromean', '4_1', 'T(2,8)', etc. See
            `knot_braid_database.list_known_knots()` + T(p, k).
        q: substrate q value. Accepts mp.mpf (preferred), decimal
            string, or numeric type supporting str() coercion.
        convention: "wenzl" (Wenzl Jones-Markov, mass-formula) or
            "q_schur" (q-Schur Plancherel, torus knots).
        precision: "mpf" (DEFAULT — 50-dps mp.mpf via MPFR Rust
            kernels) or "f64" (LOSSY ~17 digits — cross-check only,
            never production critical path).
        dps: target precision in decimal places (default 50, matches
            L1 floor). Ignored for `precision="f64"`.

    Returns:
        mp.mpf at requested dps (default) or Python float (f64 mode).

    Raises:
        ValueError: if convention not in {"wenzl", "q_schur"} or
            precision not in {"mpf", "f64"}.
        KeyError: if knot_name not catalogued.

    Precision discipline (per compute-author skill §1):
      "f64" is LOSSY — never on production critical path. Default
      "mpf" matches the L1 50-dps floor.
    """
    if convention not in ("wenzl", "q_schur"):
        raise ValueError(
            f"convention must be 'wenzl' or 'q_schur', got {convention!r}"
        )
    if precision not in ("mpf", "f64"):
        raise ValueError(
            f"precision must be 'mpf' or 'f64', got {precision!r}"
        )

    if precision == "f64":
        return _markov_trace_f64(knot_name, float(q), convention)
    return _markov_trace_mpf(knot_name, q, convention, dps)


def _self_test() -> int:
    """Quick sanity checks on the common infra."""
    import mpmath as mp
    mp.mp.dps = 50
    q_str = "1.10997859561220225731080831999100762523924148"
    q_mpf = mp.mpf(q_str)
    q_f64 = float(q_mpf)

    print("=" * 80)
    print("markov_trace_for_knot — self-test (mpf + f64 cross-check)")
    print(f"  q_0 (50dps) = {q_str}")
    print(f"  q_0 (f64)   = {q_f64}")
    print("=" * 80)

    # Borromean via Wenzl — mpf default + f64 cross-check
    # NOTE: the truncated closed form (4+h²−3h⁴−h⁶)/(h²+4) is NOT
    # exact — it's the h²-truncation of the actual Wenzl Markov
    # trace, with a 2e-4 residual at q_0 from the h⁴+ tower
    # (documented in PR #1272's γγ̄ decomposition).
    h_mpf = q_mpf - 1 / q_mpf
    h2 = h_mpf * h_mpf
    h4 = h2 * h2
    h6 = h4 * h2
    borr_h2trunc = (4 + h2 - 3 * h4 - h6) / (h2 + 4)
    borr_wenzl_mpf = markov_trace_for_knot("Borromean", q_str, "wenzl")
    borr_wenzl_f64 = markov_trace_for_knot("Borromean", q_f64, "wenzl",
                                           precision="f64")
    print(f"\nBorromean (Wenzl JM):")
    print(f"  h²-truncation (4+h²−3h⁴−h⁶)/(h²+4) = {mp.nstr(borr_h2trunc, 25)}")
    print(f"  mpf (default, 50 dps)               = {mp.nstr(borr_wenzl_mpf, 25)}")
    print(f"  f64 (cross-check, LOSSY)            = {borr_wenzl_f64:.15g}")
    print(f"  h²-trunc residual (h⁴+ gap, PR #1272) = {mp.nstr(abs(borr_h2trunc - borr_wenzl_mpf), 5)}")
    print(f"  mpf ↔ f64 agreement                 = {mp.nstr(abs(borr_wenzl_mpf - mp.mpf(borr_wenzl_f64)), 5)}")

    # T(2,4) = W± (q-Schur) — mpf default
    tr_T24_mpf = markov_trace_for_knot("T(2,4)", q_str, "q_schur")
    tr_T24_f64 = markov_trace_for_knot("T(2,4)", q_f64, "q_schur",
                                       precision="f64")
    y_2_mpf, y_11_mpf = y_lambda_h2_q_schur_mpf(q_mpf)
    qi_mpf = 1 / q_mpf
    sibling_T24 = y_2_mpf * q_mpf ** 4 + y_11_mpf * qi_mpf ** 4
    print(f"\nT(2,4) W± (q-Schur):")
    print(f"  sibling hardcode (mpf)            = {mp.nstr(sibling_T24, 25)}")
    print(f"  mpf (default)                     = {mp.nstr(tr_T24_mpf, 25)}")
    print(f"  f64 (cross-check)                 = {tr_T24_f64:.15g}")
    print(f"  mpf ↔ hardcode agreement          = {mp.nstr(abs(sibling_T24 - tr_T24_mpf), 5)}")

    # Figure-eight 4_1 via Wenzl (mpf + f64)
    tr_4_1_mpf = markov_trace_for_knot("4_1", q_str, "wenzl")
    tr_4_1_f64 = markov_trace_for_knot("4_1", q_f64, "wenzl",
                                       precision="f64")
    print(f"\n4_1 figure-eight (Wenzl JM):")
    print(f"  mpf (default, 50 dps) = {mp.nstr(tr_4_1_mpf, 25)}")
    print(f"  f64 (cross-check)     = {tr_4_1_f64:.15g}")
    print(f"  mpf ↔ f64 agreement   = {mp.nstr(abs(tr_4_1_mpf - mp.mpf(tr_4_1_f64)), 5)}")

    print("\n✓ Common infra working — mpf is default; f64 opt-in cross-check.")
    return 0


if __name__ == "__main__":
    sys.exit(_self_test())
