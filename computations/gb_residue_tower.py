"""

CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
from codata_constants import M_P_MEV_VALIDATION  # noqa: E402 — full-precision m_p per-nucleon scale
#!/usr/bin/env python3
# polynomial_q_not_applicable: mpmath/numerical-only output; sympy use is intermediate or absent.
"""
GB residue tower: Mittag-Leffler residue sum at roots of unity.

⚠ DEPRECATED / SUPERSEDED — kept for historical reference.  The
numerical contour approach has structural issues that make it
unsuitable for sub-1% binding precision.  Use instead:

    schur_weyl_symbolic.py       (exact global H_{3A} sum, sympy)
    habiro_residue_symbolic.py   (exact residues via Φ_n, sympy)

See prop:full-pole-structure-mass-trace
(content/braids-and-knots/full-pole-structure-mass-trace.md) for
the algebraic picture.  This script's truncation to the closest
pole ζ_1 loses the higher-order ζ_n interference regime.

Numerical issues (from the superseding propositions):

  1. ε-accuracy ceiling.  Res[f;ζ] ≈ (ε/N) Σ f(ζ+ε·e^{iθ_k})·e^{iθ_k}
     has O(ε²) error.  Sub-% binding forces ε < 10⁻³; hook-poles
     force ε < 1/(3A) — explodes per atom.
  2. Dense roots of unity near q₀ = 1.11: infinitely many ζ_n;
     single contour cannot separate them.
  3. mpmath.mpc halves precision vs mpf per multiply.
  4. Catastrophic cancellation across alternating-sign residues.
  5. Φ_q branch cuts crossed by any contour around ζ_n.

Original description retained below for historical context.

─────────────────────────────────────────────────────────────────────

Implements a FIRST-PASS numerical spectral sum from
prop:gb-residue-spectral-sum:

    𝔪(K, q₀) = |tr_M(T_w, q₀)|
             + Σ_{ℓ=1..k_max} Res[Φ_q · tr_{M,ℓ}(T_w); q=ζ_ℓ]
                               / (q₀ - ζ_ℓ)

Numerical strategy:
  - For each filtration level ℓ ∈ {1..k_max}, pick the closest
    root of unity ζ_ℓ to q₀ on the unit circle.
  - Compute the residue of the level-ℓ graded trace weighted by
    Φ_q at ζ_ℓ using a small-circle contour integral (average
    over N points on a circle of radius ε around ζ_ℓ).
  - Transport to q₀ via the Cauchy kernel 1/(q₀ - ζ_ℓ).
  - Start with ⁴He (A=4) and ¹²C (A=12) — the two atoms where
    the additive-Wedderburn baseline gives ~5% binding error.

Witness output: gb-residue-tower.witness.json
"""
import sys
import json
from pathlib import Path
from datetime import datetime, timezone

import mpmath

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as _Q_CANONICAL
from crt_markov import (
    markov_trace_symbolic_eval,
    _build_crossings,
    _Phi_q_mp,
)


def markov_trace_three_channels(Z, N, include_inter, m_pp, m_pn, m_nn,
                                  q_val, precision=50):
    """Compatibility wrapper: returns `{"full": markov_trace_symbolic_eval(...)}`.

    The legacy multi-channel return shape (`{"full", "pp", "pn", "nn"}`) was
    removed when `crt_markov` migrated to the canonical Jones-Markov y_λ via
    `markov_trace_symbolic_eval` (single-value descended trace).  Call sites
    in this script only use the `"full"` field, so a single-key dict
    suffices.  pp/pn/nn channel breakdown was experimental and is not
    needed by the residue spectral sum.
    """
    val = markov_trace_symbolic_eval(
        Z, N, include_inter, m_pp, m_pn, m_nn, q_val, precision=precision,
    )
    return {"full": val}


def primitive_root_of_unity(n, precision=50):
    """Return the primitive n-th root of unity ζ_n = exp(2πi/n) as mpc.

    For n=1 this is the classical limit q=1. For n=2 it's q=-1.
    Higher n give finer Hecke degeneration loci.
    """
    mpmath.mp.dps = precision
    return mpmath.expjpi(mpmath.mpf(2) / mpmath.mpf(n))


def residue_at_root(Z, N, include_inter, m_pp, m_pn, m_nn,
                    root_n, q0_val, precision=50,
                    epsilon=mpmath.mpf('0.01'), n_contour=32,
                    channel="full"):
    """Compute Res_{q=ζ_n}[Φ_q · tr_M(T_w)] via small-circle contour integral.

    The residue is approximated as the average of the integrand
    over N equally-spaced points on a circle of radius ε around ζ_n:

        Res[f; ζ] ≈ (ε / N) · Σ_{k=0..N-1} f(ζ + ε·e^{2πik/N}) · e^{2πik/N}

    This uses the trapezoidal rule applied to Cauchy's residue formula
    Res[f; ζ] = (1/2πi) ∮ f(w) dw around ζ. For small ε and sufficient N
    this converges to the true residue at rate O(ε²) for simple poles.

    Returns mpmath complex value of the residue.
    """
    mpmath.mp.dps = precision
    zeta = primitive_root_of_unity(root_n, precision)

    residue_sum = mpmath.mpc(0)
    for k in range(n_contour):
        theta = mpmath.mpf(2) * mpmath.pi * k / n_contour
        w = zeta + epsilon * mpmath.exp(mpmath.mpc(0, theta))
        # Evaluate Φ_q · tr_M at w. tr_M takes real input historically;
        # for a complex contour we need complex arithmetic. Here we take
        # the real-part approximation (Hecke algebra is defined over ℂ
        # but our transfer matrices are real for real q — for complex q
        # near a root of unity, we use |w| as a stand-in for the
        # magnitude of the relevant q-integer factors).
        w_real = mpmath.fabs(w)
        try:
            # `channel` arg of the outer function is accepted for API
            # stability but the current `markov_trace_symbolic_eval` returns
            # the canonical Jones-Markov full-channel value (no per-channel
            # split); keeping the outer param for caller compatibility.
            tr_w = markov_trace_symbolic_eval(
                Z, N, include_inter, m_pp, m_pn, m_nn, w_real,
                precision=precision)
            qi = 1 / w_real
            # Use tr_M itself as the "Φ_q-weighted graded trace" surrogate;
            # the true Φ_q(tr_M) is finite wherever |tr_M| < w_real.
            if abs(tr_w) < w_real:
                phi = _Phi_q_mp(abs(tr_w), w_real, qi)
                if mpmath.isinf(phi):
                    return mpmath.inf
                f_w = phi * tr_w
            else:
                # Graded stratum is trivial at this root — no residue.
                f_w = mpmath.mpf(0)
        except (ZeroDivisionError, ValueError):
            f_w = mpmath.mpf(0)
        # Cauchy contour weight: e^{iθ} * (εi)
        weight = mpmath.exp(mpmath.mpc(0, theta))
        residue_sum += f_w * weight
    residue = epsilon * residue_sum / n_contour
    return residue


def spectral_sum_mass(Z, N, include_inter, m_pp, m_pn, m_nn,
                      q0_val, k_max=3, precision=50):
    """Compute mass via GB residue spectral sum.

    𝔪(K, q₀) = |tr_M(T_w, q₀)| + Σ_{ℓ=1..k_max} Res[ζ_ℓ] / (q₀ - ζ_ℓ)

    Uses the H_3-full channel for the descended term and for each
    residue. k_max = 3 samples levels 1 (ζ=1), 2 (ζ=-1), 3 (ζ=e^{2πi/3}).

    Returns dict with descended, residues[], total.
    """
    mpmath.mp.dps = precision
    q0 = mpmath.mpf(str(q0_val))

    # Descended (E⁰) term: |tr_full(T_w)|
    ch = markov_trace_three_channels(Z, N, include_inter, m_pp, m_pn, m_nn,
                                      q0, precision)
    desc = ch["full"]

    # Residue contributions at ζ_1, ζ_2, ..., ζ_{k_max}
    residue_contribs = []
    residue_total = mpmath.mpc(0)
    for level in range(1, k_max + 1):
        zeta = primitive_root_of_unity(level, precision)
        res = residue_at_root(Z, N, include_inter, m_pp, m_pn, m_nn,
                               level, q0, precision)
        kernel = 1 / (q0 - zeta)
        transported = res * kernel
        residue_contribs.append({
            "level": level,
            "zeta_n": level,
            "distance_to_q0": str(abs(q0 - zeta)),
            "residue_raw": str(res),
            "kernel": str(kernel),
            "transported": str(transported),
            "|transported|": str(abs(transported)),
        })
        residue_total += transported

    total = desc + abs(residue_total)
    return {
        "descended": desc,
        "residue_contribs": residue_contribs,
        "residue_sum_abs": abs(residue_total),
        "total": total,
    }


if __name__ == "__main__":
    print("GB RESIDUE SPECTRAL SUM — Mittag-Leffler mass formula")
    print("=" * 80)
    mpmath.mp.dps = 50
    q0 = mpmath.mpf(repr(_Q_CANONICAL))
    print(f"q_0 = {q0}")
    print(f"Per prop:gb-residue-spectral-sum "
          f"(content/braids-and-knots/gb-residue-spectral-sum.md).\n")

    # Target atoms: the two where the current Wedderburn baseline gives
    # ~5% binding error (see mass-table-best.witness.json on 1ppb branch).
    TARGET_ATOMS = [
        ("D",   1,  1,   2.22),
        ("T",   1,  2,   8.48),
        ("3He", 2,  1,   7.72),
        ("4He", 2,  2,  28.30),
        ("6Li", 3,  3,  32.00),
        ("12C", 6,  6,  92.16),
        ("16O", 8,  8, 127.62),
    ]

    # β-decay calibration (same as crt_markov.py __main__).
    tr_p = markov_trace_three_channels(1, 0, False, 1, 1, 1, q0, 50)
    tr_n = markov_trace_three_channels(0, 1, False, 1, 1, 1, q0, 50)
    Q_cat = tr_n["full"] - tr_p["full"]
    from experimental_constants import Q_NEUTRON_MEV
    E_0_cat = (mpmath.mpf(str(Q_NEUTRON_MEV)) / abs(Q_cat)
               if abs(Q_cat) > 0 else mpmath.mpf(0))
    print(f"Calibration (β-decay, H_3-full channel):")
    print(f"  |tr_full(p)| = {float(tr_p['full']):.6e}")
    print(f"  |tr_full(n)| = {float(tr_n['full']):.6e}")
    print(f"  Q_cat        = {float(Q_cat):.6e}")
    print(f"  E_0          = {float(E_0_cat):.6e} MeV/cat.unit\n")

    print(f"  {'Atom':>6} {'A':>3} {'desc(free)':>14} {'desc(atom)':>14} "
          f"{'|res_sum|':>14} {'B_pred':>10} {'B_AME':>8} {'|Δm/m|%':>9}")
    print("  " + "-" * 92)
    results = []
    for atom, Z, N, B_AME in TARGET_ATOMS:
        free = spectral_sum_mass(Z, N, False, 1, 1, 1, q0, k_max=3)
        at = spectral_sum_mass(Z, N, True, 1, 1, 1, q0, k_max=3)
        B_cat = at["total"] - free["total"]
        B_MeV = float(E_0_cat * abs(B_cat))
        M_total = (Z + N) * float(M_P_MEV_VALIDATION)
        dm = abs(B_MeV - B_AME) / M_total * 100
        print(f"  {atom:>6} {Z+N:>3d} "
              f"{float(free['descended']):>14.4e} "
              f"{float(at['descended']):>14.4e} "
              f"{float(at['residue_sum_abs']):>14.4e} "
              f"{B_MeV:>10.4f} {B_AME:>8.2f} {dm:>8.4f}%")
        results.append({
            "atom": atom, "Z": Z, "N": N, "A": Z + N,
            "free_descended": str(free["descended"]),
            "free_residue_sum_abs": str(free["residue_sum_abs"]),
            "atom_descended": str(at["descended"]),
            "atom_residue_sum_abs": str(at["residue_sum_abs"]),
            "atom_residues_by_level": at["residue_contribs"],
            "B_pred_MeV": B_MeV,
            "B_AME_MeV": B_AME,
            "delta_m_over_m_pct": dm,
        })

    witness = {
        "computation": "gb-residue-tower",
        "description": (
            "GB residue spectral sum: Mittag-Leffler mass formula at q_0. "
            "Sums residues of Φ_q · tr_M at primitive n-th roots of unity "
            "(n=1,2,3) via small-circle contour integrals, weighted by "
            "the Cauchy kernel 1/(q_0 - ζ_n). Implements "
            "prop:gb-residue-spectral-sum."
        ),
        "reference_block": "prop:gb-residue-spectral-sum",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0": str(q0),
            "E_0_cat_MeV": str(E_0_cat),
            "k_max_filtration_levels": 3,
            "contour_epsilon": "0.01",
            "contour_n_points": 32,
            "mpmath_dps": 50,
        },
        "results": results,
    }
    out = Path(__file__).parent / "gb-residue-tower.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
    print("\nNote: this is a first-pass numerical implementation; residues")
    print("are computed at real |w| along a small circle around each root")
    print("of unity. A complex-analytic upgrade (full ℂ-valued Hecke)")
    print("is the natural next step for sub-1% binding precision.")
