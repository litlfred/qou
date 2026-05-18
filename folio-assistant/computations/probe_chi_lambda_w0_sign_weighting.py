"""Sign-character verification probe for `prop:chi-lambda-w0-sign-weighting`.

Verifies the long-element-character weighting

    S_k^(w_0) = Σ_{λ ⊢ 3} χ_λ(w_0) · c_k^(λ)
              = c_k^(3) · 1 + c_k^(2,1) · 0 + c_k^(1,1,1) · (-1)
              = c_k^(3) - c_k^(1,1,1)

reproduces the SIGN of the empirical c_k coefficient at k = 5, 6.
This is the SIGN-only verification — the magnitude ratios
(|empirical/S_k^(w_0)| ≈ 1.49 at k=5, ≈ 95.3 at k=6) are
explicitly open per the prop's `.md`.

The S_3 character values χ_λ(w_0) are the standard table values:

| λ ⊢ 3      | irrep         | χ_λ(w_0)  |
|------------|---------------|-----------|
| (3)        | trivial       |  +1       |
| (2,1)      | standard      |   0       |
| (1,1,1)    | sign          |  -1       |

The per-irrep c_k^(λ) values come from `per-wedderburn-block-ck.witness.json`
(empirical Wedderburn-block coefficients at H_3, ε-expansion to ε^12).
The empirical c_k reference values are
- c_5 = -395.41
- c_6 = -45485

per the same upstream witness.

Reference: `prop:chi-lambda-w0-sign-weighting` (PR #672 follow-up
636c7dda, 2026-05-13).
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402

UPSTREAM = HERE / "per-wedderburn-block-ck.witness.json"


def _load_upstream() -> dict:
    """Load the per-Wedderburn-block c_k upstream witness."""
    if not UPSTREAM.exists():
        raise FileNotFoundError(
            f"missing upstream witness: {UPSTREAM}\n"
            "  Run the per-wedderburn-block-ck producer first."
        )
    return json.loads(UPSTREAM.read_text())


def main() -> int:
    mp.mp.dps = 50

    upstream = _load_upstream()
    results = upstream.get("results", upstream.get("data", {}))

    per_lambda = results["per_lambda"]
    emp_c5 = mp.mpf(str(results["empirical_c5_reference"]))
    emp_c6 = mp.mpf(str(results["empirical_c6_reference"]))

    # Per-irrep coefficients at ε^10 (= c_5 in the prop's notation) and
    # ε^12 (= c_6).  Prefer the symbolic ("c10_diff_symbolic") field when
    # the upstream provides it; fall back to the f64 ("c10_diff_float")
    # otherwise.  The symbolic field stores Sympy `Rational` strings
    # like "1/4", "65/4", "533/2" — `mp.mpf(str(...))` cannot parse
    # fraction strings (raises `ValueError`), so we go through
    # `sympy.Rational` first and lift to mpmath via the `(p, q)`
    # constructor.  This is the actual I8 fix (per Copilot #693
    # follow-up): the previous `mp.mpf(str(sym))` would have crashed
    # on next clean run; values happened to look correct because the
    # currently-stored rationals are dyadic and the f64 cast was exact.
    import sympy as sp  # noqa: E402

    def _coeff(v: dict, sym_key: str, f64_key: str) -> mp.mpf:
        sym = v.get(sym_key)
        if sym is not None:
            rat = sp.Rational(sym)
            return mp.mpf(int(rat.p)) / mp.mpf(int(rat.q))
        return mp.mpf(str(v[f64_key]))

    c5_per_lambda = {
        lam: _coeff(v, "c10_diff_symbolic", "c10_diff_float")
        for lam, v in per_lambda.items()
    }
    c6_per_lambda = {
        lam: _coeff(v, "c12_diff_symbolic", "c12_diff_float")
        for lam, v in per_lambda.items()
    }

    # S_3 long-element character values
    chi_w0 = {
        "(3,)": mp.mpf(1),
        "(2, 1)": mp.mpf(0),
        "(1, 1, 1)": mp.mpf(-1),
    }

    # Long-element-weighted sums
    s5_w0 = sum(chi_w0[lam] * c5_per_lambda[lam] for lam in chi_w0)
    s6_w0 = sum(chi_w0[lam] * c6_per_lambda[lam] for lam in chi_w0)

    # Sign agreement check.  Treats (0, 0) as a sign match (signs
    # trivially agree at the zero ⇒ zero edge case per Copilot #693
    # follow-up); strict-sign disagreement requires opposite non-zero
    # signs.  Returns False on `nan` inputs (defensive — `mp.sign` is
    # undefined there).
    def _same_sign(a: mp.mpf, b: mp.mpf) -> bool:
        if mp.isnan(a) or mp.isnan(b):
            return False
        return mp.sign(a) == mp.sign(b)

    s5_sign_ok = _same_sign(s5_w0, emp_c5)
    s6_sign_ok = _same_sign(s6_w0, emp_c6)

    # Magnitude ratios — informational only (magnitude closure is open
    # per the prop's `.md` § "Open: magnitude closure").
    ratio_c5 = abs(emp_c5) / abs(s5_w0) if s5_w0 != 0 else mp.inf
    ratio_c6 = abs(emp_c6) / abs(s6_w0) if s6_w0 != 0 else mp.inf

    print("=" * 80)
    print("  chi_lambda(w_0)-weighted sign verification  (prop:chi-lambda-w0-...)")
    print("=" * 80)
    print()
    print("  S_3 long-element character values χ_λ(w_0):")
    for lam, v in chi_w0.items():
        print(f"    χ_{lam}(w_0) = {int(v):+d}")
    print()
    print("  Per-irrep c_5 (ε^10) coefficients:")
    for lam, v in c5_per_lambda.items():
        print(f"    c_5^{lam} = {mp.nstr(v, 8)}")
    print(f"  S_5^(w_0) = c_5^(3) - c_5^(1,1,1) = {mp.nstr(s5_w0, 8)}")
    print(f"  empirical c_5                       = {mp.nstr(emp_c5, 8)}")
    print(f"  sign agreement: {'✓' if s5_sign_ok else '✗'}")
    print(f"  magnitude ratio |empirical/S_5|     = {mp.nstr(ratio_c5, 4)}  (closure open)")
    print()
    print("  Per-irrep c_6 (ε^12) coefficients:")
    for lam, v in c6_per_lambda.items():
        print(f"    c_6^{lam} = {mp.nstr(v, 8)}")
    print(f"  S_6^(w_0) = c_6^(3) - c_6^(1,1,1) = {mp.nstr(s6_w0, 8)}")
    print(f"  empirical c_6                       = {mp.nstr(emp_c6, 8)}")
    print(f"  sign agreement: {'✓' if s6_sign_ok else '✗'}")
    print(f"  magnitude ratio |empirical/S_6|     = {mp.nstr(ratio_c6, 4)}  (closure open)")
    print()

    builder = (
        WitnessBuilder(
            "chi-lambda-w0-sign-weighting", engine="mpmath",
        )
        .set_description(
            "Long-element (w_0 ∈ S_3) character-weighted sum "
            "S_k^(w_0) = Σ_λ χ_λ(w_0) · c_k^(λ) reproduces the SIGN of "
            "the empirical c_k at k = 5, 6 (ε^10 / ε^12 coefficients of "
            "χ_λ(β_n;q) − χ_λ(β_p;q) at q = 1+ε).  Magnitude closure "
            "remains open (ratios ≈ 1.49 at k=5, ≈ 95.3 at k=6) per "
            "the prop's `.md` § 'Open: magnitude closure'."
        )
        .set_content_block("prop:chi-lambda-w0-sign-weighting")
        .add_parameter("w_0_one_line", "[3,2,1]")
        .add_parameter("w_0_reduced_word", "s_1 s_2 s_1")
        .add_parameter("w_0_cycle", "(1 3)")
        .add_parameter(
            "chi_w0_values",
            "{(3): +1, (2,1): 0, (1,1,1): -1}",
        )
        .add_data("c5_per_lambda", {
            lam: mp.nstr(v, 50) for lam, v in c5_per_lambda.items()
        })
        .add_data("c6_per_lambda", {
            lam: mp.nstr(v, 50) for lam, v in c6_per_lambda.items()
        })
        .add_data("s5_w0_weighted", mp.nstr(s5_w0, 50))
        .add_data("s6_w0_weighted", mp.nstr(s6_w0, 50))
        .add_data("empirical_c5", mp.nstr(emp_c5, 50))
        .add_data("empirical_c6", mp.nstr(emp_c6, 50))
        .add_data("magnitude_ratio_c5", mp.nstr(ratio_c5, 50))
        .add_data("magnitude_ratio_c6", mp.nstr(ratio_c6, 50))
        .add_data("magnitude_closure", "OPEN — see prop:chi-lambda-w0-sign-weighting §'Open: magnitude closure'")
    )
    # add_upstream returns the loaded body, not the builder — call separately.
    builder.add_upstream("per-wedderburn-block-ck.witness.json")
    builder = (
        builder
        .add_assertion(
            name="c5_sign_agreement_with_empirical",
            computed=1.0 if s5_sign_ok else 0.0,
            expected=1.0,
            tolerance=0.0,
            unit="boolean (1.0 = signs agree)",
            source="prop:chi-lambda-w0-sign-weighting Step 4 — sign matches at k=5",
        )
        .add_assertion(
            name="c6_sign_agreement_with_empirical",
            computed=1.0 if s6_sign_ok else 0.0,
            expected=1.0,
            tolerance=0.0,
            unit="boolean (1.0 = signs agree)",
            source="prop:chi-lambda-w0-sign-weighting Step 4 — sign matches at k=6",
        )
        # Removed: the previous `chi_2_1_w0_eq_zero` assertion compared
        # the hardcoded chi_w0["(2, 1)"] = mp.mpf(0) against 0.0 and was
        # therefore tautological by construction.  The character value
        # χ_(2,1)(w_0) = 0 is a standard S_3 character-table fact (the
        # trace of a reflection in the 2-d standard rep is 0) but a
        # non-tautological check would require deriving it from the
        # Hoefsmit seminormal matrices, which is out of scope for this
        # probe.  Captured in the prop's `.md` § "Step 1 — character
        # values at w_0" and the `chi_w0_values` parameter above.
    )
    out = builder.save()
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
