#!/usr/bin/env python3
"""threerow_extensive_cumulant_forward_probe.py — the q₀-free ≥3-row extensive
cumulant, built FORWARD from the proved Δ_λ, tested ratio-only against AME.

LEAD 1, bean qou-prjo.  Forward, q₀-free companion to the q₀-dependent
`deltalambda_kappa_interface_residual_simplex_probe.py` / `AdditiveResidualSimplex`.

CONSTRUCTION (free_parameters = 0, NO q₀, NO AME inversion)
----------------------------------------------------------
The proved per-partition binding value is
    Δ_λ = (−1)^{n(λ)}·dim V_λ = (−1)^{n(λ)}·f^λ          (signed Springer dim;
`QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional`, sorry-free general-n).
Restrict it to the ≥3-ROW stratum ℓ(λ) ≥ 3 — the stratum PR #4664 measured to
DOMINATE the binding sum (26%→100% of B as A: 2→4) — and sum over partitions of
each cluster size k:
    s_k = Σ_{λ⊢k, ℓ(λ)≥3} (−1)^{n(λ)}·f^λ.
Then form the additive/extensive cluster functional over the derived C(A,k)
coordination-simplex basis (a single Markov trace over A strands is intensive and
saturates — 2026-06-02-binding-intensive-vs-extensive-derivation.md — so binding
must be an additive subset sum):
    B_ext(A) = Σ_{k≥3} C(A,k)·s_k     (Reading Y, extensive cluster sum)
    S(A)     = s_A                    (Reading X, single A-body algebra)
Everything is exact integer arithmetic (SYT counts via hook lengths; n(λ) exact).
NO float64 anywhere; AME enters ONLY as fixed ratio targets, never inverted.

ANTI-FIT (STRICT).  This is the 7th-ansatz danger zone.  If the object matches only
by choosing between Reading X / Reading Y (or by tuning a weight), that is a FIT and
the result is scope-(a).  The two readings are reported side by side and NOT
interpolated.

RESULT (see verdict): scope-(a).  ν₂ = 0 reproduces the derived μ₂ = 0 (0-fit,
combinatorial), but the forward cumulants are (ν₃,ν₄)=(−1,+2) — opposite sign order
to the derived (+,−) window — and |ν₄/ν₃|=2 vs derived ~9.75; the extensive AME
ratio B_ext(4)/B_ext(3)=6.0 vs AME 3.336.  Nothing wired.
"""
from __future__ import annotations
import json
import hashlib
import datetime
from fractions import Fraction
from math import comb, factorial
from pathlib import Path

# --------------------------------------------------------------------------- #
# Exact partition combinatorics (no floats)
# --------------------------------------------------------------------------- #

def partitions(n: int, mx: int | None = None):
    if mx is None:
        mx = n
    if n == 0:
        yield []
        return
    for k in range(min(n, mx), 0, -1):
        for rest in partitions(n - k, k):
            yield [k] + rest

def conjugate(lam: list[int]) -> list[int]:
    if not lam:
        return []
    m = max(lam)
    return [sum(1 for x in lam if x >= j) for j in range(1, m + 1)]

def syt_count(lam: list[int]) -> int:
    """f^λ = dim V_λ via the hook-length formula (exact integer)."""
    lp = conjugate(lam)
    n = sum(lam)
    denom = 1
    for i, row in enumerate(lam):
        for j in range(row):
            arm = row - (j + 1)
            leg = lp[j] - (i + 1)
            denom *= (arm + leg + 1)
    return factorial(n) // denom

def n_of_lambda(lam: list[int]) -> int:
    """n(λ) = Σ (i−1)·λ_i  (1-based i)  = Σ i·λ_i for 0-based enumeration."""
    return sum(i * li for i, li in enumerate(lam))

def s_row3(k: int) -> int:
    """s_k = Σ_{λ⊢k, ℓ(λ)≥3} (−1)^{n(λ)}·f^λ  (exact integer, q₀-free)."""
    total = 0
    for lam in partitions(k):
        if len(lam) >= 3:
            total += ((-1) ** n_of_lambda(lam)) * syt_count(lam)
    return total

def s_row3_detail(k: int):
    rows = []
    for lam in partitions(k):
        if len(lam) >= 3:
            f = syt_count(lam)
            nl = n_of_lambda(lam)
            rows.append({"lambda": tuple(lam), "rows": len(lam), "f_lambda": f,
                         "n_lambda": nl, "delta": ((-1) ** nl) * f})
    return rows

# --------------------------------------------------------------------------- #
# Cluster functionals (exact)
# --------------------------------------------------------------------------- #

def Bext(A: int) -> int:
    """Reading Y — extensive cluster sum Σ_{k≥3} C(A,k)·s_k."""
    return sum(comb(A, k) * s_row3(k) for k in range(3, A + 1))

def Salg(A: int) -> int:
    """Reading X — single A-body algebra S(A)=s_A."""
    return s_row3(A)

# Forward cumulants: Mayer inversion of S(A) over the C(A,k) basis (edge/triangle/
# tetrahedron), the SAME basis AdditiveResidualSimplex uses for the q₀ residual.
def forward_cumulants():
    nu2 = Salg(2)
    nu3 = Salg(3) - 3 * nu2
    nu4 = Salg(4) - 6 * nu2 - 4 * nu3
    return nu2, nu3, nu4

# --------------------------------------------------------------------------- #
# AME2020 total binding energies (MeV) — TARGETS ONLY, never inverted
# --------------------------------------------------------------------------- #
AME_MeV = {"D": Fraction(222456, 100000), "T": Fraction(848180, 100000),
           "He3": Fraction(771805, 100000), "He4": Fraction(2829567, 100000)}

# Derived q₀ residual cumulants (from AdditiveResidualSimplex / the residual-simplex
# witness) — quoted here only for the comparison, NOT used as inputs.
DERIVED_MU = {"mu2": "0", "mu3": "+0.4708", "mu4": "-4.591",
              "abs_mu4_over_mu3": "9.751"}


def main() -> dict:
    sk = {k: s_row3(k) for k in range(1, 6)}
    detail = {k: s_row3_detail(k) for k in range(1, 6)}
    nu2, nu3, nu4 = forward_cumulants()

    # exact ratios
    bext = {A: Bext(A) for A in (2, 3, 4)}
    salg = {A: Salg(A) for A in (2, 3, 4)}
    ame_ratio_43 = AME_MeV["He4"] / AME_MeV["T"]          # ≈ 3.336
    y_ratio_43 = Fraction(abs(bext[4]), abs(bext[3]))      # 6
    x_ratio_43 = Fraction(abs(salg[4]), abs(salg[3]))      # 2

    result = {
        "free_parameters": 0,
        "q0_free": True,
        "no_float64": True,
        "s_k": {str(k): sk[k] for k in sk},
        "s_k_detail": {str(k): detail[k] for k in detail},
        "reading_Y_extensive_cluster": {str(A): bext[A] for A in bext},
        "reading_X_single_algebra": {str(A): salg[A] for A in salg},
        "forward_cumulants": {"nu2": nu2, "nu3": nu3, "nu4": nu4,
                              "abs_nu4_over_nu3": str(Fraction(abs(nu4), abs(nu3)))},
        "zero_fit_match": {
            "nu2": nu2, "derived_mu2": DERIVED_MU["mu2"],
            "match": (nu2 == 0),
            "note": "ν₂=0 re-derives the derived μ₂=0 combinatorially (s₁=s₂=0), "
                    "q₀-free and independent of the graded-ladder self-reference.",
        },
        "sign_window": {
            "forward_nu3_nu4_signs": [("+" if nu3 > 0 else "-"),
                                      ("+" if nu4 > 0 else "-")],
            "derived_mu3_mu4_signs": ["+", "-"],
            "opposite_order": True,
            "note": "forward parity gives (−,+); the derived #4316 window is (+,−). "
                    "The Δ_λ chirality parity does NOT supply the many-body "
                    "sign-change.",
        },
        "magnitude_ratio": {
            "forward_abs_nu4_over_nu3": str(x_ratio_43),  # = 2
            "derived_abs_mu4_over_mu3": DERIVED_MU["abs_mu4_over_mu3"],  # ≈ 9.75
            "miss_factor": str(Fraction(9751, 1000) / x_ratio_43),
        },
        "ame_ratio_test_He4_over_T": {
            "AME": f"{float(ame_ratio_43):.4f}",
            "reading_Y_extensive": f"{float(y_ratio_43):.4f}",
            "reading_X_single": f"{float(x_ratio_43):.4f}",
            "verdict": "brackets AME (Y +80%, X −40%); no q₀-free convention lands "
                       "on it; interpolating is the forbidden fit.",
        },
        "verdict": "scope-(a): the q₀-free ≥3-row signed-Springer-dimension content, "
                   "ALONE, reproduces the derived μ₂=0 (0-fit) but not the 3-body "
                   "sign, the (+,−) sign-change window, or the |μ₄/μ₃|≈9.75 "
                   "magnitude. The many-body binding sign+magnitude live in the "
                   "q₀-dependent y_λ·χ^λ trace weighting, not in the combinatorial "
                   "Δ_λ. Nothing wired.",
    }

    # assertions (exact)
    assertions = [
        ("s1_s2_zero", sk[1] == 0 and sk[2] == 0, True),
        ("s3_is_minus_one", sk[3] == -1, True),
        ("s4_is_minus_two", sk[4] == -2, True),
        ("Bext_deuteron_zero", bext[2] == 0, True),
        ("Bext_ratio_four_three_is_six", bext[4] == 6 * bext[3], True),
        ("forward_nu2_zero_matches_derived_mu2", nu2 == 0, True),
        ("forward_sign_window_opposite", (nu3 < 0 and nu4 > 0), True),
        ("forward_ratio_two_not_derived_9p75", nu4 == -2 * nu3, True),
    ]
    return result, assertions


if __name__ == "__main__":
    result, assertions = main()
    script_path = Path(__file__)
    script_hash = hashlib.sha256(script_path.read_bytes()).hexdigest()[:12]
    witness = {
        "engine": "python-stdlib-exact",
        "engineVersion": "fractions + math (exact integers, no float64)",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "assertions": [{"name": n, "computed": str(c), "expected": str(e),
                        "passed": (c == e)} for (n, c, e) in assertions],
        "allPassed": all(c == e for (_, c, e) in assertions),
        "computation": "threerow-extensive-cumulant-forward",
        "scriptFile": script_path.name,
        "scriptHash": script_hash,
        "q0_anchor": "none (q₀-free construction; ratio-only test)",
        "description": (
            "LEAD 1 (bean qou-prjo): the q₀-free ≥3-row extensive cumulant built "
            "FORWARD from the proved Δ_λ=(−1)^{n(λ)}f^λ restricted to ℓ(λ)≥3, fed "
            "into the derived C(A,k) cluster basis. free_parameters=0, no q₀, no "
            "AME inversion. Re-derives μ₂=0 combinatorially (0-fit) but gives the "
            "(−,+) sign order vs the derived (+,−) window and |ν₄/ν₃|=2 vs ~9.75; "
            "extensive AME ratio B_ext(4)/B_ext(3)=6.0 vs AME 3.336. scope-(a); "
            "nothing wired. Forward, q₀-free twin of "
            "deltalambda_kappa_interface_residual_simplex_probe.py."),
        "contentBlock": "rem:ohtsuki-tower-bar-parity",
        "audit_only": True,
        "tier": "structural (proved Δ_λ + exact cluster arithmetic; AME targets only)",
        "result": result,
    }
    out = script_path.with_name("threerow-extensive-cumulant-forward.witness.json")
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=False)
    out.write_text(json.dumps(witness, indent=2, ensure_ascii=False))
    print(f"s_k = {result['s_k']}")
    print(f"Reading Y (extensive): {result['reading_Y_extensive_cluster']}")
    print(f"Reading X (single):    {result['reading_X_single_algebra']}")
    print(f"forward cumulants: {result['forward_cumulants']}")
    print(f"AME ratio test: {result['ame_ratio_test_He4_over_T']}")
    print(f"allPassed={witness['allPassed']}")
    print(f"wrote {out.name}")
