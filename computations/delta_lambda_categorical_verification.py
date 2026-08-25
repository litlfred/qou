"""
delta_lambda_categorical_verification.py — Phase 1b of the
closed-forms-first-principles workplan.

Tests the per-partition Δ_λ categorical closure form
(conj:delta-lambda-categorical-closure) on the deuteron:

    Δ_λ(K) := τ_q( Σ_{p ∈ O_prin^(λ)} Res^alg_p (λ^(k(λ))_{SW,λ}) )

vs the empirical AME 2020 deuteron binding energy
B(D) = 2.22456 MeV via the master formula

    B(K) = m_e · Σ_λ y_λ(q_0) · χ^λ(β_K) · Δ_λ(K).

Strategy:
  1. Load per-partition (y_λ, χ^λ(β_D), dim) from
     chi-deuteron-h6-at-q0-50dps.witness.json.
  2. Identify the per-λ "jet prolongation order" k(λ) from the
     partition shape (several candidate mappings tested).
  3. Compute the principal-Galois-orbit residue of λ^(k)_SW for
     k ∈ {0, 1, 2, 3} as the per-k "base residue" c_k.
  4. For each k(λ) mapping, evaluate B(D) = m_e · Σ_λ y_λ χ^λ · c_{k(λ)}.
  5. Compare to AME 2020. The mapping (if any) that reproduces
     B(D) at ≤ 1 ppm identifies the categorical k(λ) bijection.

Outcomes interpretation:
  - **Match at ≤ 1 ppm on some mapping:** Δ_λ closure substantiated;
    the categorical bijection k(λ) is identified empirically;
    Phase 2 extends to T, ³He, ⁴He.
  - **Best mapping matches at 1–10% level:** closure is qualitatively
    right, quantitatively needs refinement (per-λ discriminant
    factorization, higher jet prolongation, or block-specific
    residue convention).
  - **No mapping comes close:** the closure form does not match
    empirical — R1 (per-λ discriminant doesn't factor) or R2 (the
    formula needs another categorical ingredient) fires.

Ref: [manuscript] conj:delta-lambda-categorical-closure
Ref: [manuscript] docs/audits/2026-05-19-closed-forms-first-principles-workplan.md
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
from _precision import set_compute_dps, str_at_true_precision  # noqa: E402 — dps must rise before module constants
import ast
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp
import numpy as np

from witness_base import WitnessBuilder, record_upstream
# Canonical constants — avoid re-typed CODATA / q_0 literals (Copilot PR #787 review).

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []
from codata_constants import M_E_MEV
from q_parameter import Q as Q0

# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

B_D_AME_MEV = mp.mpf("2.22456607")  # AME 2020 deuteron binding energy


def load_chi_deuteron() -> tuple[mp.mpf, list[dict]]:
    """Load Hecke characters for the deuteron at q_0, 50 dps."""
    path = _pb.witness_path("chi-deuteron-h6-at-q0-50dps.witness.json", HERE)
    w = record_upstream(path, _UPSTREAM_RECORDS)
    by_part = w["by_partition"]
    parsed = []
    for p in by_part:
        # The witness can carry `partition` either as a JSON list or as
        # its string repr ("[6]" etc.). Use ast.literal_eval — never
        # bare eval (Copilot PR #787 review).
        raw = p["partition"]
        lam = raw if isinstance(raw, list) else ast.literal_eval(raw)
        parsed.append({
            "partition": str(lam),
            "lam": lam,
            "dim": int(p["dim"]),
            "y": mp.mpf(p["y_lambda"]),
            "chi": mp.mpf(p["chi_lambda"]),
        })
    tr_M = mp.mpf(w["tr_M_at_q0"])
    return tr_M, parsed


# ── Color-tube cubic + algebraic residue (per PR #779/#780 framework) ──

def cubic_roots(z: complex) -> np.ndarray:
    coeffs = [1.0 + 0.0j, 4 * z + 1, 6 * z**2 + 3 * z + 1,
              4 * z**3 + 3 * z**2 + 2 * z + 1]
    return np.roots(coeffs)


def dF_dc(z: complex, c: complex) -> complex:
    return 3 * c**2 + 2 * (4 * z + 1) * c + (6 * z**2 + 3 * z + 1)


def dF_dz(z: complex, c: complex) -> complex:
    return 4 * c**2 + (12 * z + 3) * c + (12 * z**2 + 6 * z + 2)


def dc_dz_at(z: complex, c: complex) -> complex:
    denom = dF_dc(z, c)
    if abs(denom) < 1e-14:
        return complex("inf")
    return -dF_dz(z, c) / denom


def lambda_SW_k(z: complex, k: int) -> complex:
    """The k-th jet prolongation of the SW differential, evaluated at z.

    k = 0: electron channel (c_0 + z) where c_0 is the principal real root
    k = 1: muon channel (dc_0/dz on the principal sheet)
    k = 2: pair channel (Σ over color-sheet pairs)
    k = 3: baryon channel (∏_k dc_k/dz)
    """
    if k == 0:
        cs = cubic_roots(z)
        c0 = cs[np.argmin(np.abs(cs.imag))]
        return c0 + z
    elif k == 1:
        cs = cubic_roots(z)
        c0 = cs[np.argmin(np.abs(cs.imag))]
        return dc_dz_at(z, c0)
    elif k == 2:
        cs = cubic_roots(z)
        # Sum of pairwise products of dc_k/dz
        ds = [dc_dz_at(z, c) for c in cs]
        return ds[0] * ds[1] + ds[0] * ds[2] + ds[1] * ds[2]
    elif k == 3:
        cs = cubic_roots(z)
        p = 1.0 + 0.0j
        for c in cs:
            p *= dc_dz_at(z, c)
        return p
    else:
        raise ValueError(f"k = {k} not implemented")


def find_principal_pair() -> list[complex]:
    """Innermost conjugate pair of the color-tube discriminant."""
    coeffs = [16, 24, 35, 50, 35, 24, 16]
    roots = np.roots(coeffs)
    sorted_by_modulus = sorted(roots, key=lambda z: abs(z))
    return [complex(sorted_by_modulus[0]), complex(sorted_by_modulus[1])]


def residue_via_circle(f, z_c: complex, eps: float = 1e-3, n: int = 400) -> complex:
    thetas = np.linspace(0.0, 2.0 * np.pi, n, endpoint=False)
    dtheta = 2.0 * np.pi / n
    integral = 0.0 + 0.0j
    for theta in thetas:
        z = z_c + eps * np.exp(1j * theta)
        dz = 1j * eps * np.exp(1j * theta) * dtheta
        integral += f(z) * dz
    return integral / (2j * np.pi)


def base_residue_sum_at_k(k: int) -> complex:
    """Σ_{p ∈ O_prin} Res^alg_p (λ^(k)_SW), the per-k "base residue".

    ⚠ Numerical precision caveat (Copilot PR #787 review): this contour
    integral is computed in numpy float64 (~ 17 decimal digits), NOT at
    the script's mpmath 50-dps target. For ε = 1e-3 and 400 sample
    points, the noise floor on the residue magnitude is approximately
    ε · float64_eps ≈ 1e-16 — well above values like the k=0 / k=1
    base residues (5e-6 / 1e-5 range). The "k=2 residue identically
    zero" finding in the audit doc is therefore consistent with
    float64-precision cancellation; an mpmath-quadrature reimplementation
    would resolve whether k=2 is truly zero or merely smaller than 1e-6.
    For Phase 1b diagnostic purposes, float64 suffices; Phase 2 should
    re-run at mpmath precision before claiming the per-k structure is
    categorically true."""
    principal = find_principal_pair()
    res = sum(residue_via_circle(lambda z, kk=k: lambda_SW_k(z, kk), zc)
              for zc in principal)
    return res


# ── Per-λ k mapping candidates ────────────────────────────────────────

def k_by_rows(lam: list[int]) -> int:
    """k = number of rows of λ minus 1."""
    return min(3, len(lam) - 1)


def k_by_first_row(lam: list[int]) -> int:
    """k = first row length minus 1 (clamped to 3)."""
    return min(3, lam[0] - 1)


def k_by_distinct_rows(lam: list[int]) -> int:
    """k = number of distinct row lengths minus 1."""
    return min(3, len(set(lam)) - 1)


def k_by_sign(lam: list[int]) -> int:
    """k matches the channel structure: trivial → 0, standard → 1,
       hook → 2, alternating → 3."""
    n = sum(lam)
    if lam == [n]:
        return 0
    elif lam == [n - 1, 1]:
        return 1
    elif lam == [1] * n:
        return 3
    else:
        return 2


def k_by_hook(lam: list[int]) -> int:
    """k = hook length at (1,1) - 1, the principal hook."""
    if not lam:
        return 0
    # principal hook = row 1 length + col 1 length - 1
    row1 = lam[0]
    col1 = len(lam)
    return min(3, row1 + col1 - 2)


K_MAPS = {
    "by_rows": k_by_rows,
    "by_first_row": k_by_first_row,
    "by_distinct_rows": k_by_distinct_rows,
    "by_sign": k_by_sign,
    "by_hook": k_by_hook,
}


# ── Verification ──────────────────────────────────────────────────────

def main() -> int:
    builder = WitnessBuilder("delta-lambda-categorical-verification")
    builder.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    builder.set_description(
        "Phase 1b numerical test of conj:delta-lambda-categorical-closure "
        "on the deuteron (n=6, 11 partitions). Computes B(D) under each "
        "candidate k(λ) mapping and compares to AME 2020 B(D) = 2.22456 MeV."
    )

    # 1. Load empirical χ^λ data
    tr_M, partitions = load_chi_deuteron()
    builder.add_parameter("q0", str(Q0))
    builder.add_parameter("n_partitions", str(len(partitions)))
    builder.add_parameter("tr_M_at_q0_empirical", str(tr_M))
    builder.add_parameter("m_e_MeV", str(M_E_MEV))
    builder.add_parameter("B_D_AME_MeV", str(B_D_AME_MEV))

    # 2. Compute base residues at k = 0, 1, 2, 3
    base_res = {k: base_residue_sum_at_k(k) for k in (0, 1, 2, 3)}
    builder.add_data("base_residues_by_k", {
        str(k): {"re": float(v.real), "im": float(v.imag),
                 "abs": float(abs(v))}
        for k, v in base_res.items()
    })

    # 3. For each k(λ) mapping, evaluate B(D)
    results = {}
    for map_name, k_fn in K_MAPS.items():
        # Δ_λ := τ_q(base_res[k(λ)]) — interpret as the absolute value
        # (the categorical Δ_λ has magnitude; sign tracking is a separate
        # refinement)
        B_D_pred = mp.mpf(0)
        per_lambda = []
        for p in partitions:
            k_lambda = k_fn(p["lam"])
            delta_l = mp.mpf(abs(base_res[k_lambda]))
            term = p["y"] * p["chi"] * delta_l
            B_D_pred += term
            per_lambda.append({
                "partition": p["partition"],
                "k_lambda": k_lambda,
                # str_at_true_precision, not str: delta_l is mp.mpf(<float>) —
                # 53 bits promoted — and str() renders it at the live mp.dps,
                # emitting 50 digits of binary64 tail that read as measured.
                # A no-op on the values that DID carry more than 53 bits, since
                # the short form is then exact.
                "y_lambda": str_at_true_precision(p["y"]),
                "chi_lambda": str_at_true_precision(p["chi"]),
                "delta_lambda": str_at_true_precision(delta_l),
                "contribution": str_at_true_precision(term),
            })
        B_D_pred *= M_E_MEV
        err_abs = abs(B_D_pred - B_D_AME_MEV)
        err_rel = err_abs / B_D_AME_MEV
        results[map_name] = {
            "B_D_predicted_MeV": str(B_D_pred),
            "B_D_AME_MeV": str(B_D_AME_MEV),
            "error_abs_MeV": str(err_abs),
            "error_relative": float(err_rel),
            "error_ppm": float(err_rel * 1e6),
            "per_lambda": per_lambda,
        }
    builder.add_data("verification_per_mapping", results)

    # 4. Identify best-fit mapping
    best_map = min(results.keys(), key=lambda m: results[m]["error_relative"])
    builder.add_data("best_fit_mapping", best_map)
    builder.add_data("best_fit_error_ppm",
                     results[best_map]["error_ppm"])

    # 5. Verdict
    best_err = results[best_map]["error_relative"]
    if best_err < 1e-6:
        verdict = "PASS (≤ 1 ppm)"
    elif best_err < 1e-2:
        verdict = "QUALITATIVE (1 ppm – 1%, refinement needed)"
    else:
        verdict = "MISS (> 1%, R1 or R2 fires)"
    builder.add_data("verdict", verdict)

    # Sanity assertion: tr_M from χ^λ contributions matches the witness
    tr_M_check = sum(p["y"] * p["chi"] for p in partitions)
    builder.add_assertion(
        "tr_M_reconstruction_from_chi",
        computed=float(tr_M_check),
        expected=float(tr_M),
        tolerance=1e-10,
        unit="trace value",
        source="chi-deuteron-h6-at-q0-50dps.witness.json",
    )

    # Closure-form assertion at the quantitative target: ≤ 1% relative
    # error (the band the closure form actually claims to meet).
    # Per Copilot PR #787 review: this asserts the QUANTITATIVE target,
    # so a failure here truthfully reflects the closure form's
    # current quantitative MISS (the verdict field above records the
    # qualitative band). Tightening from "factor of 2" to "≤ 1% relative"
    # makes allPassed: false consistent with the negative diagnostic.
    builder.add_assertion(
        "best_mapping_B_D_pred_within_1_percent",
        computed=float(mp.mpf(results[best_map]["B_D_predicted_MeV"])),
        expected=float(B_D_AME_MEV),
        tolerance=float(B_D_AME_MEV) * 0.01,  # ≤ 1% relative
        unit="MeV",
        source=(
            f"closure form Δ_λ = |base_residue[k({best_map}(λ))]| "
            f"applied to deuteron (Phase 1b naive form; Phase 2 "
            f"two-factor closure with JSJ Vol^(λ) addresses the miss)"
        ),
    )

    # Lean SDP-uniqueness cross-reference (post-#1537 wiring).

    builder.add_data("lean_uniqueness_ref", {

        "generic": "qou:QOU.BraidKnot.@nucleus_uniqueness_closed (3*A)",

        "framework_doc":

            "content/quantum-observable-universe/lean/QOU/BraidKnot/NucleusEmptySDPUniqueness.lean",

        "note": "Certifies T_w uniqueness at the abstract empty-constraint SDP level (PR #1537 parameterised module). Workplan: docs/workplans/2026-05-31-witness-lean-uniqueness-ref-wiring.md.",

    })


    builder.save()

    # Console summary
    print("=" * 72)
    print("  Δ_λ categorical closure — Phase 1b verification on deuteron")
    print("=" * 72)
    print(f"  q_0      = {Q0}")
    print(f"  m_e      = {M_E_MEV} MeV (CODATA 2022)")
    print(f"  B(D) AME = {B_D_AME_MEV} MeV")
    print()
    print("  Base residues |Σ_{z_c^±} Res^alg_z_c (λ^(k)_SW)|:")
    for k, r in base_res.items():
        print(f"    k = {k}: |{r:.6f}| = {abs(r):.6f}")
    print()
    print(f"  {'mapping':<22}  {'B_D pred (MeV)':>18}  {'error (rel)':>14}  {'error (ppm)':>16}")
    for map_name, r in results.items():
        marker = "  ←" if map_name == best_map else ""
        print(f"  {map_name:<22}  {r['B_D_predicted_MeV'][:18]:>18}  "
              f"{r['error_relative']:>14.6f}  {r['error_ppm']:>16.3f}{marker}")
    print()
    print(f"  Verdict: {verdict}")
    print(f"  Best-fit mapping: {best_map} (relative err = {best_err})")
    print()
    print("  See witness JSON for per-λ contributions under each mapping.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
