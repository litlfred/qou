"""Direction 2 Step 1 (extended) — fractional k_ud + alternative ansatz scan.

EXPLORATORY / AUDIT-ONLY follow-up to the integer k_ud scan in
`probe_k_ud_bring_color_tube_empirical_baseline.py` (PR #1467). That
probe **falsified** the simple multiplicative ansatz:

  m_d / m_u  =  (1 − h_q · q^{10}) / (1 − h_q · q^{10 + k_ud})

— no integer k_ud ∈ {-3..3} closes the PDG residual below 45.9%
(best k = +3 → 1.168 vs PDG 2.16). This probe extends the scan to:

1. **Fractional k_ud** ∈ {-3.0, -2.9, ..., 5.0} — does any non-integer
   value close the residual? If yes, that's a candidate for a Hecke
   partition weight ratio (Wenzl y_{(1,1)}/y_{(2)} type), since
   partition-weight ratios are generically non-integer.

2. **Alternative ansatz forms** beyond the multiplicative one:
   - additive: `m_d/m_u = 1 + Δ`, with Δ = h_q · q^k · constant
   - geometric: `m_d/m_u = (q^10 / q^{10+k})^{some_power}`
   - bar-twisted: `m_d/m_u = (1 − h_q · q^{10}) / (1 + h_q · q^{10+k})`
     (bar-involution sign flip on the (u,d) term)
   - 9-pair weighted ratio: directly from the 9-pair p-n boundary
     decomposition without going through a closed-form m_d/m_u

Per the audit doc
[`docs/workplans/2026-05-30-mass-asymmetric-flavor-split.md`](../../docs/workplans/2026-05-30-mass-asymmetric-flavor-split.md)
Direction 2 Step 1, this probe extends the empirical baseline so
Step 2 (categorical derivation) has a clearer target.

**Discipline guard**: this probe REPORTS which form best matches
PDG, but does NOT credit any match as a derivation. The
`fitted_labelled_canonical_audit.py` rule applies — any match below
the experimental σ requires a categorical-derivation argument
before it can move from `exploratory` to `production`.

References:
- prop:pn-averaging-uniqueness (PR #1445)
- probe_k_ud_bring_color_tube_empirical_baseline.py (PR #1467)
- docs/workplans/2026-05-30-mass-asymmetric-flavor-split.md
"""
from __future__ import annotations
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
from pathlib import Path
import mpmath as mp
from mpmath import mpf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Idempotent. Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

M_D_OVER_M_U_PDG = mpf("2.16")
M_D_OVER_M_U_PDG_ERR = mpf("0.07")
BRING_BASE_EXPONENT = 10


def bring_weight(q: mpf, k: float) -> mpf:
    """1/(1 − h_q · q^{base + k}) — Bring color-tube weight."""
    h_q = (q - 1) / q
    return 1 / (1 - h_q * q ** mpf(BRING_BASE_EXPONENT + k))


def multiplicative_ansatz(q: mpf, k_ud: float) -> mpf:
    """Original (1 − h_q·q^10) / (1 − h_q·q^{10+k}) form — what
    PR #1467's probe falsified at integer k."""
    h_q = (q - 1) / q
    num = 1 - h_q * q ** BRING_BASE_EXPONENT
    den = 1 - h_q * q ** mpf(BRING_BASE_EXPONENT + k_ud)
    return num / den


def additive_ansatz(q: mpf, k_ud: float, c: float = 1.0) -> mpf:
    """m_d/m_u = 1 + c · h_q · q^k — simple additive deviation."""
    h_q = (q - 1) / q
    return 1 + mpf(c) * h_q * q ** mpf(k_ud)


def geometric_ansatz(q: mpf, k_ud: float, p: float = 1.0) -> mpf:
    """(q^10 / q^{10+k})^p = q^{-k·p} — pure power form."""
    return q ** mpf(-k_ud * p)


def bar_twisted_ansatz(q: mpf, k_ud: float) -> mpf:
    """(1 − h_q · q^10) / (1 + h_q · q^{10+k}) — bar-involution sign
    flip on the (u,d) denominator. Tests whether the asymmetry sits
    on the bar-sign rather than the exponent shift."""
    h_q = (q - 1) / q
    num = 1 - h_q * q ** BRING_BASE_EXPONENT
    den = 1 + h_q * q ** mpf(BRING_BASE_EXPONENT + k_ud)
    return num / den


def nine_pair_ratio(q: mpf, k_ud: float) -> mpf:
    """Direct 9-pair weighted ratio: (5·w_k + 4·w_0) / (4·w_k + 5·w_0).
    From p=uud × n=udd with k_ud asymmetry — neutron-heavy pair
    weighting on numerator. This is the structurally most natural
    form per the workplan Direction 2 §1.1."""
    w0 = bring_weight(q, 0)
    wk = bring_weight(q, k_ud)
    return (5 * wk + 4 * w0) / (4 * wk + 5 * w0)


ANSATZ_FORMS = {
    "multiplicative": multiplicative_ansatz,
    "additive (c=1)": lambda q, k: additive_ansatz(q, k, c=1.0),
    "additive (c=10)": lambda q, k: additive_ansatz(q, k, c=10.0),
    "geometric (p=1)": lambda q, k: geometric_ansatz(q, k, p=1.0),
    "geometric (p=10)": lambda q, k: geometric_ansatz(q, k, p=10.0),
    "bar-twisted": bar_twisted_ansatz,
    "9-pair weighted ratio": nine_pair_ratio,
}


def find_root_k(q: mpf, ansatz_fn, target: mpf,
                k_lo: float = -10.0, k_hi: float = 20.0,
                coarse_step: float = 0.01,
                tol: mpf = mpf("1e-30")) -> tuple[float, mpf]:
    """Find k such that ansatz(q, k) ≈ target, within k ∈ [k_lo, k_hi].

    Robust against POLES inside the interval (per Copilot review on
    #1520): Bring color-tube weights can have singularities at
    `q^{10+k} = 1/h_q` which separate same-sign endpoints. Strategy:

    1. Fine-scan the interval at `coarse_step` resolution to identify
       all sign changes of `ansatz_fn - target` (this handles poles
       since the function diverges to ±∞ at each pole, producing
       multiple sign changes per branch).
    2. Within EACH sign-change bracket, bisect to high precision.
    3. Return the bisected root closest to the target — or, if no
       sign change exists anywhere, the coarse-grid global best.

    The bisected `best_k_ud` values reported in the witness are
    therefore actual roots of `ansatz(q, k) - target`, not rounded
    grid points.
    """
    # 1. Fine-scan for sign changes + track values for fallback
    n_steps = int((k_hi - k_lo) / coarse_step) + 1
    samples = []  # (k, value-target) — None where the eval failed
    for i in range(n_steps + 1):
        k_t = k_lo + i * coarse_step
        try:
            v = ansatz_fn(q, k_t)
            samples.append((k_t, v - target))
        except (ZeroDivisionError, ValueError, OverflowError):
            samples.append((k_t, None))

    # 2. Find sign-change brackets (skip None entries)
    brackets = []
    prev_k, prev_f = None, None
    for k_t, f in samples:
        if f is None:
            prev_k, prev_f = None, None
            continue
        if prev_f is not None and float(prev_f) * float(f) < 0:
            brackets.append((prev_k, k_t))
        prev_k, prev_f = k_t, f

    if brackets:
        # 3. Bisect within each bracket; pick the root closest to target
        results = []
        for k_lo_b, k_hi_b in brackets:
            lo, hi = mpf(k_lo_b), mpf(k_hi_b)
            f_lo = ansatz_fn(q, lo) - target
            f_hi = ansatz_fn(q, hi) - target
            for _ in range(200):
                mid = (lo + hi) / 2
                try:
                    f_mid = ansatz_fn(q, mid) - target
                except (ZeroDivisionError, ValueError, OverflowError):
                    break
                if abs(f_mid) < tol:
                    lo = hi = mid
                    break
                if float(f_lo) * float(f_mid) < 0:
                    hi, f_hi = mid, f_mid
                else:
                    lo, f_lo = mid, f_mid
            mid = (lo + hi) / 2
            try:
                v_mid = ansatz_fn(q, mid)
                results.append((float(abs(v_mid - target)), float(mid), v_mid))
            except (ZeroDivisionError, ValueError, OverflowError):
                continue
        if results:
            results.sort()
            return results[0][1], results[0][2]

    # 4. No sign-change bracket found — global best on the fine grid
    valid = [(float(abs(f)), k_t, ansatz_fn(q, k_t))
             for k_t, f in samples if f is not None]
    if not valid:
        return float('nan'), mpf('nan')
    valid.sort()
    return valid[0][1], valid[0][2]


def main():
    _t0 = time.perf_counter()
    set_compute_dps()
    q = Q_MP

    print("=" * 76)
    print("  Direction 2 Step 1 (extended) — fractional k_ud + alt-ansatz scan")
    print("=" * 76)
    print()
    print(f"  q_0           = {mp.nstr(q, 20)}")
    print(f"  PDG target    = {float(M_D_OVER_M_U_PDG):.4f} ± "
          f"{float(M_D_OVER_M_U_PDG_ERR):.4f}")
    print()

    results = []
    print(f"  {'ansatz':<26}  {'k_ud (best)':>14}  "
          f"{'value':>12}  {'PDG residual':>14}")
    print(f"  {'-'*26}  {'-'*14}  {'-'*12}  {'-'*14}")
    for name, fn in ANSATZ_FORMS.items():
        best_k, best_val = find_root_k(q, fn, M_D_OVER_M_U_PDG)
        residual_pct = float(
            (best_val - M_D_OVER_M_U_PDG) / M_D_OVER_M_U_PDG * 100
        ) if not mp.isnan(best_val) else float('nan')
        print(f"  {name:<26}  {best_k:>+14.4f}  {float(best_val):>12.5f}  "
              f"{residual_pct:>+13.4f}%")
        results.append({
            "ansatz": name,
            "best_k_ud": best_k,
            "best_value_at_k": mp.nstr(best_val, 20),
            "pdg_residual_pct": residual_pct,
            "matches_pdg_within_sigma": (
                abs(residual_pct / 100 * float(M_D_OVER_M_U_PDG))
                < float(M_D_OVER_M_U_PDG_ERR)
            ),
        })
    print()

    matches = [r for r in results
               if r["matches_pdg_within_sigma"] and not mp.isnan(mpf(r["best_value_at_k"]))]
    print(f"  Forms matching PDG within 1σ ({float(M_D_OVER_M_U_PDG_ERR):.3f}): "
          f"{len(matches)}")
    for r in matches:
        print(f"    - {r['ansatz']:<26}  k_ud = {r['best_k_ud']:+.4f}  "
              f"residual = {r['pdg_residual_pct']:+.4f}%")
    print()
    print("  DISCIPLINE: any matching form is a SHAPE HINT, not a derivation.")
    print("  Step 2 (categorical derivation, NOT THIS PROBE) must identify")
    print("  the matching k_ud value with a categorical invariant (Hecke")
    print("  partition weight, Lobachevsky-Λ integral, etc.) without fitting.")
    print()
    print("  Provenance forms only counted as derived if Step 2 closes")
    print("  per the fitted_labelled_canonical_audit.py discipline rule.")
    print()

    w = WitnessBuilder("probe-k-ud-fractional-and-alt-ansatz",
                       engine="mpmath", start_time=_t0)
    w.set_description(
        "EXPLORATORY probe extending PR #1467's integer k_ud scan to "
        "fractional values + alternative ansatz forms (additive, "
        "geometric, bar-twisted, 9-pair weighted ratio). Reports "
        "which ansatz forms admit a k_ud that matches PDG m_d/m_u "
        "≈ 2.16 within experimental σ. Shape hints for Direction 2 "
        "Step 2 categorical derivation. Audit-only; never feeds "
        "production. Per fitted_labelled_canonical_audit discipline."
    )
    w.set_audit_only(
        "docs/workplans/2026-05-30-mass-asymmetric-flavor-split.md"
    )
    w.add_data("q_0", mp.nstr(q, 50))
    w.add_data("bring_base_exponent", BRING_BASE_EXPONENT)
    w.add_data("pdg_md_mu_target", str(M_D_OVER_M_U_PDG))
    w.add_data("pdg_md_mu_err", str(M_D_OVER_M_U_PDG_ERR))
    w.add_data("ansatz_forms_scanned", list(ANSATZ_FORMS.keys()))
    w.add_data("scan_results", results)
    w.add_data("matching_within_sigma", [r["ansatz"] for r in matches])
    w.add_assertion(
        "all_ansatz_forms_scanned",
        computed=len(results), expected=len(ANSATZ_FORMS), tolerance=0,
        source="Each of the 7 ansatz forms evaluated; root-bisected for k_ud"
    )
    print(f"  Witness: {w.save()}")


if __name__ == "__main__":
    main()
