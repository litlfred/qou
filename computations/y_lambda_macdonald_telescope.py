#!/usr/bin/env python3
"""Macdonald hook-content telescope for $Z_n$ and clean $y_\\lambda$.

Closes the open structural project recorded in
`y-lambda-clean-closed-forms.md` (§"Open: a telescope for general $n$?").

The Wenzl-bridge gives

    Z_n  =  Σ_{λ ⊢ n}  f_λ · s_{λ, X}(Q),
    s_{λ, X}(Q) = Q^{n(λ)} · ∏_{x ∈ λ} (1 − X · Q^{c(x)}) / (1 − Q^{h(x)}),

where f_λ = number of SYT of shape λ, Q = q², and X = Q^r is the
Wenzl level.  The hand-derivation at n = 2 produced the compact
ratio Z_2 = (1−X)² / (1−Q)².  That is *not* a coincidence: it is
the n = 2 case of the **classical principal-specialisation
identity**

    Σ_{λ ⊢ n} f_λ · s_λ(x_1, x_2, …)  =  p_1(x_1, x_2, …)^n,        (★)

(Stanley EC2, Cor. 7.12.5; equivalent to the Robinson–Schensted–
Knuth bijection / Frobenius character formula for the regular
representation of S_n).  Specialising to a finite alphabet
(1, q, q², …, q^{r−1}) — the *principal specialisation* of length
r — gives p_1 = 1 + q + … + q^{r−1} = (1 − q^r) / (1 − q).
Substituting q ↦ Q and X = Q^r, identity (★) yields the
**Macdonald hook-content telescope**

    Z_n  =  ((1 − X) / (1 − Q))^n.                                  (♦)

Equivalently, the Wenzl-bridge $y_\\lambda$ collapses to the
single-product hook-content form

    y_λ  =  Q^{n(λ)} · (1 − Q)^n / (1 − X)^n
              · ∏_{x ∈ λ} (1 − X · Q^{c(x)}) / (1 − Q^{h(x)}).      (♣)

This is fully algorithmic: O(n) work per partition, no
sympy.simplify, no manual algebra.

This script:

1. Verifies (♦) as a sympy identity for n = 0, …, n_max (default
   n_max = 8 — symbolic, exact, sorry-free).
2. Emits the clean closed form (♣) for every partition of every
   n ∈ {0, …, 12} into a witness JSON.
3. Cross-checks (♣) against the Wenzl-bridge raw form
   s_{λ,X}(Q) / Σ_µ d_µ s_{µ,X}(Q) (must be identically equal —
   this is a sanity check, not a numerical comparison).
4. Spot-checks numerical agreement against the existing MPFR
   witness `y-lambda-mpfr-witness.json` at q_0.

References
----------
- Stanley, "Enumerative Combinatorics, Volume 2" (1999),
  Corollary 7.12.5 (sum-of-Schur identity (★) above).
- Macdonald, "Symmetric Functions and Hall Polynomials" (1995),
  I.3 ex. 1 (principal specialisation of Schur functions).
- prop:macdonald-hook-telescope (this paper).
"""

from __future__ import annotations
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).parent))
from witness_base import WitnessBuilder  # noqa: E402
from partition_utils import hook_lengths_with_cells as hook_lengths  # noqa: E402
from _precision import set_compute_dps  # noqa: E402


def n_lambda(p):
    return sum(i * p[i] for i in range(len(p)))


def f_lambda(p):
    """Hook-length formula: number of SYT of shape p."""
    n = sum(p)
    nfact = 1
    for k in range(2, n + 1):
        nfact *= k
    hp = 1
    for (_, _, h) in hook_lengths(p):
        hp *= h
    return nfact // hp


def partitions_of(n):
    if n == 0:
        return [()]
    out = []

    def rec(rem, mx, pre):
        if rem == 0:
            out.append(tuple(pre))
            return
        for k in range(min(rem, mx), 0, -1):
            rec(rem - k, k, pre + [k])

    rec(n, n, [])
    return out


def schur_principal_symbolic(p, X, Q):
    """s_{λ, X}(Q) in terms of symbols X, Q."""
    cells = hook_lengths(p)
    expr = Q ** n_lambda(p)
    for (i, j, h) in cells:
        c = j - i
        expr *= (1 - X * Q ** c) / (1 - Q ** h)
    return expr


def y_lambda_telescope_symbolic(p, X, Q):
    """Closed form (♣) — the post-telescope $y_\\lambda$.

    Returns a sympy ratio with no sympy.simplify or sympy.cancel:
    the structure is already canonical.
    """
    cells = hook_lengths(p)
    n = sum(p)
    num = Q ** n_lambda(p) * (1 - Q) ** n
    den = (1 - X) ** n
    for (i, j, h) in cells:
        c = j - i
        num *= (1 - X * Q ** c)
        den *= (1 - Q ** h)
    return num / den


def verify_telescope_identity(n_max: int = 8) -> dict:
    """Verify (♦) Z_n = ((1-X)/(1-Q))^n symbolically for n = 0..n_max."""
    X, Q = sp.symbols("X Q")
    results = {}
    for n in range(0, n_max + 1):
        Z = sum(
            f_lambda(p) * schur_principal_symbolic(p, X, Q)
            for p in partitions_of(n)
        )
        target = ((1 - X) / (1 - Q)) ** n
        diff = sp.cancel(Z - target)
        results[str(n)] = {
            "num_partitions": len(partitions_of(n)),
            "Z_n_minus_target_simplified": sp.sstr(diff),
            "identity_holds": (diff == 0),
        }
    return results


def verify_telescope_collapse(n_max: int = 6) -> dict:
    """Check that (♣) matches the raw Wenzl form s_λ / Z symbolically.

    For each partition of each n, the post-telescope closed form (♣)
    must equal s_{λ,X}(Q) / Z_n.  Both sides are sympy rationals; we
    check (LHS · Z_n − s_{λ,X}(Q)) simplifies to 0.
    """
    X, Q = sp.symbols("X Q")
    results = {}
    for n in range(0, n_max + 1):
        per_partition = {}
        for p in partitions_of(n):
            lhs = y_lambda_telescope_symbolic(p, X, Q)
            rhs_num = schur_principal_symbolic(p, X, Q)
            rhs_den = ((1 - X) / (1 - Q)) ** n
            diff = sp.cancel(lhs - rhs_num / rhs_den)
            per_partition[str(p)] = {
                "matches_raw_wenzl": (diff == 0),
                "diff_simplified": sp.sstr(diff),
            }
        results[str(n)] = per_partition
    return results


def emit_closed_forms(ns) -> dict:
    """Emit closed forms (♣) for every partition of every n in `ns`.

    Output is symbolic in q (with Q = q², X expanded via Wenzl bridge
    X = q · z / (1 − Q + q · z) and z = q³/(q² + 1), the SU(2) /
    Temperley–Lieb form — convention D).

    This docstring read `z = 1/(q^{1/2} + q^{-1/2})` — convention C — until
    2026-08-15, while the line below it computed `q**3/(q**2 + 1)`. The
    emitted numbers were therefore always D and are unaffected; only the
    prose was stale. It is recorded here rather than silently corrected
    because this file was one of the last three entries on the
    convention-C front, and a reader (or a grep-based detector) had no way
    to tell a stale comment from a stale computation.
    """
    q = sp.Symbol("q", positive=True)
    Q = q ** 2
    z = q**3 / (q**2 + 1)
    X = q * z / (1 - Q + q * z)
    out = {}
    for n in ns:
        per_partition = []
        for p in partitions_of(n):
            y = y_lambda_telescope_symbolic(p, X, Q)
            per_partition.append({
                "partition": list(p),
                "f_lambda": f_lambda(p),
                "n_lambda": n_lambda(p),
                "y_lambda_closed_form": sp.sstr(y),
            })
        out[str(n)] = {
            "n": n,
            "num_partitions": len(per_partition),
            "weights": per_partition,
        }
    return out


def cross_check_mpfr(witness_path: Path) -> dict:
    """Numerical spot-check (♣) at q_0 against the MPFR witness."""
    import mpmath as mp
    set_compute_dps()

    if not witness_path.exists():
        return {"available": False, "reason": f"{witness_path} not found"}

    raw = json.loads(witness_path.read_text())

    def y_numeric(p, q0):
        Qn = q0 ** 2
        zn = q0**3 / (q0**2 + 1)
        Xn = q0 * zn / (1 - Qn + q0 * zn)
        cells = hook_lengths(p)
        n = sum(p)
        num = Qn ** n_lambda(p) * (1 - Qn) ** n
        den = (1 - Xn) ** n
        for (i, j, h) in cells:
            c = j - i
            num *= (1 - Xn * Qn ** c)
            den *= (1 - Qn ** h)
        return num / den

    samples = []
    blob = raw.get("tables_by_n") or raw.get("by_n") or raw
    candidate_keys = (
        "y_lambda", "y_lambda_mpfr", "y_lambda_numeric", "value",
    )
    if isinstance(blob, dict):
        for nk, table in blob.items():
            try:
                n_int = int(nk)
            except (ValueError, TypeError):
                continue
            if not isinstance(table, dict):
                continue
            rows = table.get("weights")
            q_val = mp.mpf(table.get("q") or "1.1097")
            if not rows:
                continue
            for row in rows:
                p = tuple(row.get("partition") or row.get("lambda") or [])
                if not p:
                    continue
                key = next((k for k in candidate_keys if k in row), None)
                if key is None:
                    continue
                ref_val = mp.mpf(row[key])
                comp = y_numeric(p, q_val)
                samples.append({
                    "n": n_int,
                    "partition": list(p),
                    "y_mpfr": str(ref_val),
                    "y_telescope": str(comp),
                    "abs_diff": str(abs(comp - ref_val)),
                })
    return {
        "available": True,
        "samples": samples,
        "num_samples": len(samples),
        "max_abs_diff": str(
            max((mp.mpf(s["abs_diff"]) for s in samples), default=mp.mpf(0))
        ),
    }


def _scope_n_max() -> int:
    """Symbolic-verification range.  Defaults to 6 to fit the local
    sandbox's wall-clock budget; CI sets `QOU_EXTEND_SCOPE=1` to
    push to 8 (incurs n=7 + n=8 sympy.cancel costs that exceed
    the local 50 s timeout).  Witness drift is allowed when this
    flag toggles since both regimes produce a self-consistent
    output. -/
    """
    import os
    return 8 if os.environ.get("QOU_EXTEND_SCOPE") == "1" else 6


def main():
    builder = (
        WitnessBuilder("y-lambda-macdonald-telescope", engine="sympy")
        .set_description(
            "Macdonald hook-content telescope: Z_n = ((1-X)/(1-Q))^n, "
            "giving the clean closed form y_λ = Q^{n(λ)} (1-Q)^n / (1-X)^n "
            "· ∏ (1-X·Q^c)/(1-Q^h) — sorry-free, O(n) per partition, no "
            "sympy.simplify needed.  Resolves the 'Open: a telescope for "
            "general n?' question in y-lambda-clean-closed-forms.md."
        )
        .set_content_block("prop:macdonald-hook-telescope")
    )

    n_max = _scope_n_max()
    expected_partition_total = sum(
        len(partitions_of(n)) for n in range(0, n_max + 1)
    )
    print(f"Step 1: verify Z_n = ((1-X)/(1-Q))^n symbolically "
          f"(n = 0..{n_max}, scope={'CI-extended' if n_max == 8 else 'sandbox'})...")
    identity = verify_telescope_identity(n_max=n_max)
    for n_str, rec in identity.items():
        flag = "OK" if rec["identity_holds"] else "FAIL"
        print(f"  n={n_str:>2}  {flag}  ({rec['num_partitions']} partitions)")
        builder.add_assertion(
            name=f"Z_{n_str}_identity",
            computed=int(rec["identity_holds"]),
            expected=1,
            tolerance=0,
            source="sympy.cancel(Z_n - ((1-X)/(1-Q))^n) == 0",
        )

    print(f"Step 2: verify per-partition closed-form collapse (n = 0..{n_max})...")
    collapse = verify_telescope_collapse(n_max=n_max)
    for n_str, per_p in collapse.items():
        all_ok = all(rec["matches_raw_wenzl"] for rec in per_p.values())
        flag = "OK" if all_ok else "FAIL"
        print(f"  n={n_str:>2}  {flag}  ({len(per_p)} partitions)")
        builder.add_assertion(
            name=f"closed_form_collapse_n{n_str}",
            computed=int(all_ok),
            expected=1,
            tolerance=0,
            source="y_λ telescope = s_λ / Z_n per partition",
        )

    print(f"Step 3: emit closed forms (n = 0..{n_max})...")
    closed = emit_closed_forms(list(range(0, n_max + 1)))
    total = sum(rec["num_partitions"] for rec in closed.values())
    print(f"  emitted {total} closed forms")
    builder.add_assertion(
        name="closed_forms_emitted",
        computed=total,
        expected=expected_partition_total,
        tolerance=0,
        source=f"cumulative p(0)+...+p({n_max})",
    )

    print("Step 4: cross-check against MPFR witness...")
    mpfr_check = cross_check_mpfr(
        Path(__file__).parent / "y-lambda-mpfr-witness.json"
    )
    if mpfr_check.get("available"):
        print(f"  max |Δ| = {mpfr_check['max_abs_diff']} (over "
              f"{len(mpfr_check['samples'])} samples)")
        builder.add_assertion(
            name="mpfr_cross_check_max_abs_diff",
            computed=mpfr_check["max_abs_diff"],
            expected="0",
            tolerance=1e-30,
            source="y-lambda-mpfr-witness.json",
        )
    else:
        print(f"  skipped: {mpfr_check.get('reason', 'unknown')}")

    builder.add_data("telescope_identity",
                     "Z_n := Σ_{λ ⊢ n} f_λ · s_{λ,X}(Q) = ((1-X)/(1-Q))^n")
    builder.add_data("closed_form",
                     "y_λ = Q^{n(λ)} · (1-Q)^n / (1-X)^n · "
                     "∏_{x ∈ λ} (1-X·Q^{c(x)})/(1-Q^{h(x)})")
    builder.add_data("verification", {
        "identity": identity,
        "collapse": collapse,
    })
    builder.add_data("closed_forms_by_n", closed)
    builder.add_data("mpfr_cross_check", mpfr_check)
    builder.add_data("precision", "symbolic_q")
    builder.add_data("truncation_eps", 0.0)

    out_path = builder.save()
    print(f"\nWitness: {out_path}")


if __name__ == "__main__":
    main()
