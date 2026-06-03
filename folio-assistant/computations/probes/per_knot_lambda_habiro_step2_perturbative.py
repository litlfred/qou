"""Per-knot λ(K) via Habiro — STEP 2: extract the perturbative series.

Follow-up to `per_knot_lambda_habiro_probe.py` (step 1) and §6.8 of
[`docs/audits/2026-06-03-1ppq-roadmap-reanalysis-and-geom-full-bridge-gap.md`].

Step 1 found the figure-eight (= muon, linking_weight = 1) Habiro element

    J(4_1; q) = Σ_{n≥0} (q;q)_n (q⁻¹;q⁻¹)_n
              = Σ_{n≥0} (-1)^n 4^n [∏_{j=1}^n sinh(jℏ/2)]²    (q = e^ℏ)

is an ASYMPTOTIC series at real q₀, with optimal (least-term) truncation
giving S* = 0.98954 — only −1.05 % from the muon's exact lw = 1.

STEP 2 (this script, no external dependency) extracts the perturbative
series

    S*(ℏ)  =  a_0 + a_1 ℏ + a_2 ℏ² + …

by computing the optimal-truncation value across a ladder of small real
ℏ and fitting.  The decisive question: **is a_0 = 1 exactly?**  If so,
the figure-eight Habiro element's ℏ→0 limit IS the muon's linking_weight,
and the −1.05 % at q₀ is just the leading O(ℏ²) correction — i.e. the
Geom_full bridge for the muon is DERIVED (the lw = 1 for a knot is the
ℏ→0 Habiro limit), not a convention.

Optimal-truncation extracts the asymptotic power series modulo a
non-perturbative ambiguity of order the least term (~exp(−c/ℏ),
exponentially small), which is far below the a_k we read off — so the
power-series coefficients are well-defined.

Saddle structure (verified): the least-term index solves
4 sinh²((n+1)ℏ/2) = 1 ⟹ sinh((n+1)ℏ/2) = 1/2 ⟹ (n+1)ℏ/2 = arcsinh(1/2)
= ln φ (φ = golden ratio).  So n* = 2 ln φ / ℏ − 1.  The REAL-q saddle
sits at the golden ratio — distinct from the complex Q(√−3) hyperbolic
saddle (the real-vs-root-of-unity distinction the G-S-W-Z framework
makes precise).

ZERO fit to physics.  EXPLORATORY.  No production path.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import _path_bridge  # noqa: F401, E402

from q_parameter import Q_50_DIGIT_STR  # noqa: E402


def habiro_4_1_optimal(hbar: mp.mpf, n_cap: int = 400) -> tuple[mp.mpf, int, mp.mpf]:
    """Optimal (least-term) truncation of J(4_1; e^ℏ).

    Returns (S_opt, n_opt, min_term_magnitude).
    """
    q = mp.e ** hbar
    terms = [mp.mpf(1)]
    sums = [mp.mpf(1)]
    term = mp.mpf(1)
    total = mp.mpf(1)
    for n in range(1, n_cap + 1):
        factor = (1 - q**n) * (1 - q**(-n))
        term *= factor
        total += term
        terms.append(term)
        sums.append(total)
        # stop once we are clearly past the minimum (terms growing again)
        if n > 5 and abs(terms[n]) > abs(terms[n - 1]) > abs(terms[n - 2]) \
                and abs(terms[n]) > mp.mpf("1e6"):
            break
    abs_terms = [abs(t) for t in terms]
    n_opt = min(range(1, len(abs_terms)), key=lambda i: abs_terms[i])
    return sums[n_opt], n_opt, abs_terms[n_opt]


def fit_power_series(hbars: list[mp.mpf], svals: list[mp.mpf],
                     degree: int) -> list[mp.mpf]:
    """Least-squares polynomial fit S(ℏ) = Σ a_k ℏ^k (Vandermonde solve
    at high precision via mpmath)."""
    # Build Vandermonde and solve normal equations at mp precision.
    m = len(hbars)
    A = mp.matrix(m, degree + 1)
    for i in range(m):
        for k in range(degree + 1):
            A[i, k] = hbars[i] ** k
    b = mp.matrix(svals)
    # Solve via QR (mpmath lstsq through normal equations AtA x = At b)
    At = A.T
    AtA = At * A
    Atb = At * b
    coeffs = mp.lu_solve(AtA, Atb)
    return [coeffs[k] for k in range(degree + 1)]


def main() -> int:
    mp.mp.dps = 80
    t0 = time.time()
    print("=" * 72)
    print(" Habiro per-knot λ(K) STEP 2 — figure-eight perturbative series")
    print("=" * 72)

    # Ladder of small real ℏ.  Smaller ℏ → larger n_opt → smaller min
    # term → more digits, but also more compute.  Range chosen so the
    # min term stays > 1e-25 (well-resolved at 80 dps).
    hbars = [mp.mpf(h) / 1000 for h in
             (40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140)]
    rows = []
    svals = []
    for hb in hbars:
        S, n_opt, mt = habiro_4_1_optimal(hb)
        svals.append(S)
        rows.append((hb, S, n_opt, mt))
        print(f"  ℏ={float(hb):.3f}  n_opt={n_opt:>3}  "
              f"min|term|={mp.nstr(mt, 4):>12}  S*={mp.nstr(S, 18)}")

    # Fit S*(ℏ) as a polynomial.  Try degree 4 and 6; report a_0..a_3.
    print("\n── polynomial fits S*(ℏ) = Σ a_k ℏ^k ──")
    fits = {}
    for deg in (4, 6):
        coeffs = fit_power_series(hbars, svals, deg)
        fits[deg] = [mp.nstr(c, 12) for c in coeffs]
        print(f"  degree {deg}:")
        for k, c in enumerate(coeffs[:5]):
            print(f"    a_{k} = {mp.nstr(c, 14)}")

    # Decisive readout: a_0 vs muon linking_weight = 1
    a0_d4 = fit_power_series(hbars, svals, 4)[0]
    a0_d6 = fit_power_series(hbars, svals, 6)[0]
    print("\n── DECISIVE: a_0 vs muon linking_weight = 1 ──")
    print(f"  a_0 (deg4 fit) = {mp.nstr(a0_d4, 16)}  "
          f"(rel to 1: {mp.nstr((a0_d4 - 1) * 100, 4)} %)")
    print(f"  a_0 (deg6 fit) = {mp.nstr(a0_d6, 16)}  "
          f"(rel to 1: {mp.nstr((a0_d6 - 1) * 100, 4)} %)")

    # Also report value at q0 for continuity with step 1
    q0 = mp.mpf(Q_50_DIGIT_STR)
    hb0 = mp.log(q0)
    S0, n0, mt0 = habiro_4_1_optimal(hb0)
    print(f"\n  at q₀ (ℏ={mp.nstr(hb0,8)}): S*={mp.nstr(S0,16)} "
          f"(step-1 cross-check: 0.98953878)")

    a0_is_one = abs(a0_d6 - 1) < mp.mpf("1e-4")
    verdict = ("a_0 = 1 to fit precision → figure-eight Habiro ℏ→0 limit "
               "IS the muon linking_weight; −1.05% at q₀ is the O(ℏ²) "
               "correction. Geom_full bridge DERIVED for the muon."
               if a0_is_one else
               "a_0 ≠ 1 at fit precision → the figure-eight Habiro element "
               "does NOT limit to lw=1; the −1.05% is not purely O(ℏ²). "
               "Needs the canonical normalization (background G-Z lookup).")
    print(f"\n  VERDICT: {verdict}")

    out = {
        "computation": "per-knot-lambda-habiro-step2-perturbative",
        "description": (
            "Extracts the figure-eight Habiro perturbative series S*(ℏ) "
            "via optimal-truncation across an ℏ-ladder + polynomial fit. "
            "Decisive question: is a_0 = 1 (= muon linking_weight)? "
            "EXPLORATORY, no production path, no physics fit."),
        "saddle_structure": "n* = 2 ln(φ)/ℏ − 1 (golden-ratio real-q saddle)",
        "ladder": [
            {"hbar": mp.nstr(hb, 8), "S_opt": mp.nstr(S, 20),
             "n_opt": no, "min_term": mp.nstr(mt, 6)}
            for (hb, S, no, mt) in rows
        ],
        "fits": fits,
        "a0_deg4": mp.nstr(a0_d4, 20),
        "a0_deg6": mp.nstr(a0_d6, 20),
        "a0_rel_to_lw1_pct_deg6": mp.nstr((a0_d6 - 1) * 100, 8),
        "S_at_q0": mp.nstr(S0, 20),
        "a0_equals_one_to_1e4": bool(a0_is_one),
        "verdict": verdict,
        "compute_time_sec": round(time.time() - t0, 2),
    }
    out_path = HERE.parent / "per-knot-lambda-habiro-step2.witness.json"
    out_path.write_text(json.dumps(out, indent=2))
    print(f"\nWitness: {out_path.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
