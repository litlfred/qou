#!/usr/bin/env python3
"""bring_polarized_q_dictionary_endpoint_blindness_probe.py

FORMALIZE-FIRST result for the α_EM magnitude leg's q-deformation route:
**endpoint-anchored q-dictionaries are polarization-blind.**

Context. Two corpus results meet here:

1. `alpha_em_period_qdeformation_probe.py` (bean qou-tq20 tranche 5) proved the
   formalize-first prune: matching two monotone one-parameter families under a
   FREE reparameterization t(q) is VACUOUS — the dictionary-independent content
   of the period-side q-deformation lives ONLY in the asymptotic ENDPOINT
   observables (t→0, t→∞).
2. `bring_genus4_polarized_epstein_detprime_probe.py` (merged #4043) computed
   the genus-4 boson measures: principally polarized τ₀·M → 1.38758 (O(1));
   product period τ₀·diag(5,5,5,1) → 1.4724e12 — a ~12-orders separation
   carried ENTIRELY by the integer-lattice theta-factor (covolume and metric
   spectrum are polarization-independent: det = 125, spec {1,5,5,5}).

CLAIM (symbolic-exact, numerically confirmed below): the two endpoint
observables are IDENTICAL for the polarized and product periods —

  * t→0:  Jacobi inversion θ_H(t) = t^{−n/2} det(H)^{−1/2} θ_{H⁻¹}(1/t) gives
          θ(t) ~ t^{−4}/√det H, and det is polarization-independent (both
          Grams have det = Im(τ₀)⁸·125²... identical), so the t→0 asymptote
          is EQUAL for the two periods — exactly, not approximately;
  * t→∞:  θ_H(t) → 1 for every positive-definite H — trivially equal.

CONSEQUENCE (scope-(a)): any q-dictionary anchored only at the endpoints — the
only non-vacuous kind, per the tranche-5 prune — assigns the polarized and the
product period the SAME q-image. But #4043 showed the polarization theta-factor
is a ~12-orders effect for the determinant. Hence the period-side q-deformation
program cannot see the polarization data at all: **the magnitude leg's
q-deformation route carries no dictionary-independent content beyond the
product form, and the leg collapses onto the τ-functor (categorical) wall** —
converging, from the geometry side, with #4030's "irreducibly categorical"
verdict for the per-loop leg. The interior region where polarization lives is
exactly the dictionary-gated region where matching is vacuous.

Scope guard (STRICT): scope-(a) — this constrains the METHOD CLASS
(endpoint-anchored period-side dictionaries), not any categorical ingredient;
the τ-functor route is untouched and remains THE open wall. No q₀-dictionary
is fitted; no 8π; nothing wired; no tier change.

Self-contained (numpy + mpmath); reuses the merged #4043 FP machinery.
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

import mpmath as mp
import numpy as np

_here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _here)
from bring_genus4_polarized_epstein_detprime_probe import (  # noqa: E402
    _gram, fp_norms, _theta_m1,
)
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


def theta(qnorms, t):
    """θ_H(t) = 1 + Σ_{m≠0} e^{−π t mᵀHm} from precomputed FP norms."""
    return 1.0 + _theta_m1(qnorms, t)


def theta_small_t(qnorms_inv, detH, n, t):
    """θ_H(t) via Jacobi inversion — exact for t ≪ 1 where direct sums fail."""
    return t ** (-n / 2) * detH ** -0.5 * theta(qnorms_inv, 1.0 / t)


def main():
    t0 = complex(-0.5, 0.186676)
    M = np.array([[4, 1, -1, 1], [1, 4, 1, -1], [-1, 1, 4, 1], [1, -1, 1, 4]], float)
    D = np.diag([5.0, 5.0, 5.0, 1.0])
    G_pol = _gram(t0 * M)
    G_diag = _gram(np.array(t0 * D, complex))
    n = 8
    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    # 0. the exact precondition: covolume is polarization-independent
    dpol, ddiag = np.linalg.det(G_pol), np.linalg.det(G_diag)
    check("covolume_polarization_independent",
          abs(dpol / ddiag - 1) < 1e-12,
          f"det G_pol = {dpol:.12e} = det G_diag = {ddiag:.12e}")

    qpol = fp_norms(G_pol, 14)
    qdiag = fp_norms(G_diag, 14)
    qpol_i = fp_norms(np.linalg.inv(G_pol), 14)
    qdiag_i = fp_norms(np.linalg.inv(G_diag), 14)

    # 1. t→0 endpoint: Jacobi asymptote θ ~ t^{-4}/√det G — EQUAL exactly
    #    (verified numerically: the ratio θ_pol/θ_diag → 1 as t → 0)
    ratios0 = {}
    for t in (0.2, 0.1, 0.05):
        tp = theta_small_t(qpol_i, dpol, n, t)
        td = theta_small_t(qdiag_i, ddiag, n, t)
        ratios0[t] = tp / td
    monotone_to_1 = (abs(ratios0[0.05] - 1) < abs(ratios0[0.1] - 1) < abs(ratios0[0.2] - 1))
    check("endpoint_t_to_0_identical",
          abs(ratios0[0.05] - 1) < 1e-8 and monotone_to_1,
          f"θ_pol/θ_diag at t=0.2,0.1,0.05: {ratios0[0.2]:.10f}, {ratios0[0.1]:.10f}, "
          f"{ratios0[0.05]:.10f} → 1 (Jacobi: both ~ t⁻⁴/√det, det equal ⇒ EXACT)")

    # 2. t→∞ endpoint: θ → 1 for both — trivially equal. Convergence is slow
    #    (the thin τ₀ block's shortest Gram vector ≈ 0.139 ⇒ rate e^{−0.437t}),
    #    so evaluate deep in the tail: t = 10, 20, 40.
    ratios_inf = {t: theta(qpol, t) / theta(qdiag, t) for t in (10.0, 20.0, 40.0)}
    monotone_inf = (abs(ratios_inf[40.0] - 1) < abs(ratios_inf[20.0] - 1)
                    < abs(ratios_inf[10.0] - 1))
    check("endpoint_t_to_inf_identical",
          abs(ratios_inf[40.0] - 1) < 1e-6 and monotone_inf,
          f"θ_pol/θ_diag at t=10,20,40: {ratios_inf[10.0]:.8f}, {ratios_inf[20.0]:.8f}, "
          f"{ratios_inf[40.0]:.10f} → 1 monotonically (both θ → 1; deviation decays at "
          "the shortest-vector rate e^{−π·0.139·t})")

    # 3. the interior is where ALL the polarization lives (dictionary-gated zone)
    r1 = theta(qpol, 1.0) / theta(qdiag, 1.0)
    check("interior_carries_polarization",
          abs(r1 - 1) > 0.05,
          f"θ_pol/θ_diag at t=1: {r1:.6f} ≠ 1 — the interior differs while both "
          "endpoints agree; integrated over the heat kernel this is the ~12-orders "
          "determinant separation of #4043 (1.38758 vs 1.4724e12)")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "ENDPOINT-ANCHORED q-DICTIONARIES ARE POLARIZATION-BLIND (scope-(a), method-class "
        "constraint): both dictionary-content endpoints of the period-side q-deformation — "
        "the t→0 Jacobi asymptote θ~t⁻⁴/√det (det polarization-independent, so EXACTLY "
        "equal) and the trivial t→∞ limit θ→1 — coincide for the principally polarized "
        "period τ₀·M and the product period τ₀·diag(5,5,5,1), while the ~12-orders "
        "determinant separation (#4043: 1.38758 vs 1.4724e12) lives entirely in the "
        "dictionary-gated interior where matching is vacuous (tranche-5 prune). The "
        "magnitude leg's period-side q-deformation route therefore carries no "
        "dictionary-independent polarization content: the route collapses onto the "
        "τ-functor (categorical) wall — independent geometric convergence with #4030's "
        "'irreducibly categorical'. Constrains the METHOD, not any ingredient; the "
        "τ-functor route is untouched. No dictionary fitted; no 8π; nothing wired."
        if all_passed else
        "INCONCLUSIVE — an assertion failed; re-derive before citing."
    )
    print("\nVERDICT:", verdict)

    def _sha():
        s = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=_here, text=True).strip()
        if not s:
            raise RuntimeError("empty commitSha")
        return s

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(__file__, "rb") as _f:
        src = _f.read()
    witness = {
        "computation": "bring-polarized-q-dictionary-endpoint-blindness",
        "description": "Formalize-first method-class constraint for the α_EM magnitude leg: "
                       "the two non-vacuous (endpoint) observables of any period-side "
                       "q-deformation dictionary are identical for the polarized (τ₀·M) and "
                       "product (τ₀·diag) periods — t→0 exactly (Jacobi + det equality), "
                       "t→∞ trivially — while the ~12-orders polarization effect (#4043) is "
                       "confined to the dictionary-gated interior. The q-route collapses "
                       "onto the τ-functor wall (independent convergence with #4030). "
                       "Scope-(a); no dictionary fitted; no 8π; nothing wired.",
        "auditOnly": "docs/audits/2026-07-19-bring-polarized-q-dictionary-endpoint-blindness.md",
        "tier": "symbolic-exact (t→0 equality via Jacobi inversion + det identity; t→∞ trivial) "
                "+ numeric confirmation; scope-(a) method-class constraint",
        "computedAt": now, "commitSha": _sha(),
        "engine": "numpy+mpmath", "engineVersion": np.__version__ + "/" + mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions, "allPassed": all_passed,
        "result": {
            "theta_ratio_t_0p05": ratios0[0.05], "theta_ratio_t_1": r1,
            "theta_ratio_t_40": ratios_inf[40.0],
            "measure_polarized_4043": 1.38757991, "measure_diagonal_4043": 1.472396e12,
            "verdict": verdict,
        },
        "context": {
            "builds_on": "#4043 (polarized/diagonal genus-4 measures + FP machinery); "
                         "alpha_em_period_qdeformation_probe (tranche-5 endpoint-only prune); "
                         "#4030 + TauFunctorTargetSpec (per-loop leg irreducibly categorical)",
            "scope_guard": "scope-(a) method-class constraint; τ-functor route untouched; "
                           "no dictionary fitted; no 8π; nothing wired; no tier change",
        },
    }
    out = os.path.join(_here, "bring-polarized-q-dictionary-endpoint-blindness.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
