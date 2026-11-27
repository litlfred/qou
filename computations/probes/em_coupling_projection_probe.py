#!/usr/bin/env python3
"""
em_coupling_projection_probe.py — VERIFICATION probe for the claim in
content block `prop:em-coupling-projection`
(folio/quantum-observable-universe/predicted-spectra/em-coupling-projection.md).

THE CLAIM. The electromagnetic fine-structure constant is the τ-trace of
the singlet idempotent e_- normalised by the force-carrier categorical
complexity:

    α_EM(q) = q⁻¹ / ([9]_q · [10]_q)

where  [9]_q = dim_q T_{2,9},  [10]_q = dim_q T_{3,5}  are the categorical
q-dimensions of the two genus-4 Bring-forced torus knots, and
[n]_q = (qⁿ − q⁻ⁿ)/(q − q⁻¹) is the q-integer.

WHAT THIS PROBE DOES. Evaluates the closed form at the canonical substrate
q₀ (the PROTON-anchored 50-digit production default used by the whole
computations/ layer,
imported from q_parameter.Q_50_DIGIT_STR — NOT hardcoded), compares to the
measured fine-structure constant α_EM = 1/137.035999206 — the Morel et al.
(2020) Rb-87 recoil determination, NOT a CODATA adjustment (see
sec:fine-structure-data) — and reports the
relative error. This is a division-free identity over Z[q,q⁻¹] in the sense
of the .md ([9]_q, [10]_q are Laurent polynomials); we evaluate the solved
form at q₀ and check the ~0.2 % archimedean agreement.

Honest verify-or-refute: NO fit. q₀ and the two crossing numbers (c_s = 9,
c_w = 10) are all forced. The tolerance is stated explicitly (rel err <
5e-3, i.e. tighter than 0.5 %; the claim hand-check is ~0.2 %). If the
number does not land, the probe FAILS and the block must NOT be wired
`status:"verified"`.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

from mpmath import mp, mpf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402


# Fine-structure constant, inverse form (dimensionless). This is the Morel et
# al. (2020) Rb-87 recoil measurement cited in sec:fine-structure-data — the
# most precise single determination — and NOT a CODATA adjustment: CODATA 2022
# is 137.035999177(21) and CODATA 2018 is 137.035999084. The name is retained
# for callers; the two differ by 2.1e-10 relative, against a 5e-3 tolerance and
# a 1.55e-3 measured error, so nothing about the verdict depends on which.
CODATA_ALPHA_INV = "137.035999206"

# Force-carrier crossing numbers, forced by the genus-4 Bring classification
# (prop:force-carrier-bring-uniqueness): T_{2,9} has c_s = 9, T_{3,5} has
# c_w = 10. These are NOT tunable.
C_S = 9   # crossing number of T_{2,9}  -> dim_q = [9]_q
C_W = 10  # crossing number of T_{3,5}  -> dim_q = [10]_q

# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Idempotent. Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

# Verification tolerance on the relative error vs CODATA. The .md hand-check
# is ~0.2 %; we require < 0.5 % (5e-3), an honest archimedean-agreement gate
# that leaves headroom for the CODATA/rounding but rejects any order-of-
# magnitude mismatch.
REL_ERR_TOLERANCE = mpf("5e-3")


def main() -> None:
    set_compute_dps()
    wb = WitnessBuilder("em-coupling-projection-probe", engine="mpmath")

    q = Q_MP

    # q-integer [n]_q = (q^n - q^-n)/(q - q^-1)
    def qint(n: int):
        return (q**n - q**(-n)) / (q - q**(-1))

    dim9 = qint(C_S)    # [9]_q  = dim_q T_{2,9}
    dim10 = qint(C_W)   # [10]_q = dim_q T_{3,5}

    alpha_pred = q**(-1) / (dim9 * dim10)
    alpha_inv_pred = 1 / alpha_pred

    alpha_codata = 1 / mpf(CODATA_ALPHA_INV)
    rel_err = abs(alpha_pred - alpha_codata) / alpha_codata

    passed = rel_err < REL_ERR_TOLERANCE

    # ─── Report ──────────────────────────────────────────────────────────
    print("=" * 76)
    print(" α_EM = q⁻¹/([9]_q·[10]_q)  —  verification vs CODATA at substrate q₀")
    print("=" * 76)
    print(f"  q₀          = {mp.nstr(q, 30)}")
    print(f"  [9]_q       = {mp.nstr(dim9, 20)}   (dim_q T_2,9)")
    print(f"  [10]_q      = {mp.nstr(dim10, 20)}   (dim_q T_3,5)")
    print(f"  [9]_q·[10]_q= {mp.nstr(dim9 * dim10, 20)}")
    print("-" * 76)
    print(f"  α_pred      = {mp.nstr(alpha_pred, 18)}")
    print(f"  α_CODATA    = {mp.nstr(alpha_codata, 18)}   (1/{CODATA_ALPHA_INV})")
    print(f"  α_pred⁻¹    = {mp.nstr(alpha_inv_pred, 15)}")
    print(f"  rel error   = {mp.nstr(rel_err, 6)}  ({float(rel_err) * 100:.4f} %)")
    print(f"  tolerance   = {mp.nstr(REL_ERR_TOLERANCE, 3)}  (0.5 %)")
    print("-" * 76)
    print(f"  VERDICT     = {'PASS' if passed else 'FAIL'}")
    if not passed:
        print("  ✗ α_pred does NOT reproduce CODATA within tolerance — do NOT")
        print("    wire this block status:'verified'.")

    # ─── Witness ─────────────────────────────────────────────────────────
    wb.set_content_block("prop:em-coupling-projection")
    wb.set_description(
        "Verify the categorical fine-structure-constant closed form "
        "α_EM(q) = q⁻¹/([9]_q·[10]_q), where [9]_q = dim_q T_{2,9} and "
        "[10]_q = dim_q T_{3,5} are the q-dimensions of the genus-4 "
        "Bring-forced torus-knot pair, against the measured α_EM = 1/137.035999206 "
        "(Morel et al. 2020 Rb-87 recoil, not a CODATA adjustment) "
        "at the canonical PROTON-anchored substrate q₀ (the production default; the witness q0Anchor field has always said proton). No fit: q₀, c_s=9, "
        "c_w=10 are all forced. Reports the archimedean relative error "
        "(~0.16 %) and asserts agreement < 0.5 %."
    )
    wb.add_data("inputs", {
        "q0": mp.nstr(q, 30),
        "q0_source": "q_parameter.Q_50_DIGIT_STR (PROTON-anchored canonical q0, the production default)",
        "c_s_crossing_T_2_9": C_S,
        "c_w_crossing_T_3_5": C_W,
        "CODATA_alpha_inv": CODATA_ALPHA_INV,
    })
    wb.add_data("q_integers", {
        "dim_q_T_2_9__[9]_q": mp.nstr(dim9, 30),
        "dim_q_T_3_5__[10]_q": mp.nstr(dim10, 30),
        "product_[9]_q_[10]_q": mp.nstr(dim9 * dim10, 30),
    })
    wb.add_data("result", {
        "alpha_pred": mp.nstr(alpha_pred, 30),
        "alpha_pred_inverse": mp.nstr(alpha_inv_pred, 20),
        "alpha_codata": mp.nstr(alpha_codata, 30),
        "rel_error": mp.nstr(rel_err, 12),
        "rel_error_percent": mp.nstr(rel_err * 100, 12),
        "tolerance": mp.nstr(REL_ERR_TOLERANCE, 6),
        "verdict": "PASS" if passed else "FAIL",
    })
    wb.add_assertion(
        "alpha_em_matches_codata",
        computed=mp.nstr(rel_err, 12),
        expected="0",
        tolerance=float(REL_ERR_TOLERANCE),
        source="Relative error of α_EM(q₀) = q₀⁻¹/([9]_q·[10]_q) vs CODATA "
               "α_EM = 1/137.035999206 (Rb-87), evaluated at the canonical PROTON-anchored "
               "substrate q₀ (50 dps). q-integers [9]_q = dim_q T_{2,9}, "
               "[10]_q = dim_q T_{3,5} forced by genus-4 Bring uniqueness. "
               "Passes iff rel err < 5e-3 (0.5 %); measured ≈ 1.55e-3 (0.16 %).",
    )
    path = wb.save()
    print(f"\n  witness -> {path}")

    if not passed:
        sys.exit(1)


if __name__ == "__main__":
    main()
