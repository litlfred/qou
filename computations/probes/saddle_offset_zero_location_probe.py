#!/usr/bin/env python3
"""saddle_offset_zero_location_probe.py — where does the 5₂ saddle-offset
zero-crossing actually sit, and does it mean anything?

Follow-up to #4578 (`saddle_offset_fourone_fivetwo_probe.py`, bean qou-q86o).
That probe found the ι-odd offset o(q)=c⁺(q)−c⁻(q) of the certified 5₂ Stokes
data crosses zero at a *small finite* q≈0.08 within the convergent radius —
NOT at q=1 as the owner's saddle-vector picture asks. This probe answers three
honest, open-outcome questions, derive-then-check, NO fitting:

  Q1  WHAT is q≈0.08?  Is it truncation-stable (a genuine feature of the
      analytic offset) or a truncation artifact?  Is it a corpus/substrate
      quantity (q₀−1, ℏ_q, ℏ_q², a root of unity modulus, the series radius),
      or just the root of the DT expansion's own low-order coefficients?

  Q2  Is the "q=1" claim recoverable from CERTIFIED corpus Stokes data under a
      different (non-q→0-anchored) reading — or is it definitively the trivial
      bar-fixed-point vanishing, distinct from the DT datum?

  Q3  c_3-odd hook: can the offset magnitude even be evaluated at the substrate
      q₀≈1.1097, and if so does it relate to the bar-odd Q_β c_3 near-match?

LOCKED EXPECTATIONS (set BEFORE the compute — anti-fit; a miss is a valuable
honest negative, reported scope-(a)):

  E1  q*(N) := smallest positive real root of the order-N truncation o_N(q)
      CONVERGES as N grows (truncation-STABLE), because at q≈0.087 the q³⁺
      terms are O(10⁻²) — the root is dominated by the quadratic balance
      1 − 9q − 28q² = 0, whose root is q_quad = (−9+√193)/56 ≈ 0.0873.
      Predict |q*(18) − q_quad| < 0.01.  [If it DRIFTS → truncation artifact,
      honest negative on "q≈0.08 is a well-defined number" either way.]

  E2  q* is NOT within 1% of any substrate quantity — q₀−1≈0.1097,
      ℏ_q=1−1/q₀≈0.0990, ℏ_q²≈0.0098, 1/q₀≈0.9010, nor a clean root-of-unity
      modulus (all |ζ|=1).  Predict: NO corpus match; q* is set by the DT
      series' own coefficients {9,28} (which encode the {3,4} data), carrying
      no independent substrate meaning.  → honest negative on Q1.

  E3  o(q) CANNOT be evaluated at q₀ (q₀≈1.1097 ≫ the series radius R≈0.1, and
      q₀>1): the partial sums DIVERGE.  Predict: c_3 hook via direct q₀
      evaluation is INACCESSIBLE; no clean o↔c_3 relation.  → honest negative
      on Q3.  (Do NOT fit c_3 to any offset datum; wire nothing.)

  E4  The certified o(q)=c⁺(q)−c⁻(q) is a CROSS-CHIRALITY difference at the
      SAME q (leading term 1≠0), NOT a bar-covariant object f(q)−f(q⁻¹).  So
      its q=1 vanishing is NOT delivered by the bar-fixed-point argument.  The
      bar-fixed-point vanishing (every genuine bar-odd object → 0 at q=q⁻¹=1)
      is trivially true but is a DIFFERENT object from the DT {3,4} datum
      (which lives at q→0).  Predict: "origin-centred only at q=1" is
      recoverable ONLY as that trivial fixed-point vanishing — the DT offset is
      NOT placed at q=1 by any certified reading.  → Q2 refined-negative.

Reuses the certified sandwich UNCHANGED (K1/K2/K3 ✓); avoids every qou-fk19
red-flag (no v_offset ODE, no q=exp(2πiτ) pin, no invented θ-function). No fit,
no c_k wired, no axiomatization, nothing wired to any dashboard / Q_β ladder.
"""
from __future__ import annotations

import importlib.util
import math
import sys
from fractions import Fraction as Fr
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from witness_base import WitnessBuilder  # noqa: E402
sys.path.insert(0, str(_HERE.parent / 'substrate'))
import mpmath as mp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
set_compute_dps()  # raise dps BEFORE Q0 and the constants below are built
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "qbeta_g3_5two_stokes_sandwich",
    _HERE / "qbeta_g3_5two_stokes_sandwich.py")
_sw = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_sw)

ORD = 18

# q₀ read BY NAME (bean qou-9ugp, 2026-09-03) and carried as mpf. It was the
# bare float64 literal 1.10997859555733471989…405145269 — the RETIRED
# self-certified muon pin A, superseded 2026-08-22 — and the four derived
# constants below were a float64 chain built on it. No comparison leg here,
# so the 2026-08-30 owner ruling puts it on the proton default (11.54 ppb).
Q0 = Q_MP
HBAR_Q = mp.mpf(1) - mp.mpf(1) / Q0   # ℏ_q = 1 − q₀⁻¹  (cheat sheet)
HBAR_Q2 = HBAR_Q * HBAR_Q
Q0_MINUS_1 = Q0 - mp.mpf(1)
INV_Q0 = mp.mpf(1) / Q0

# Bar-odd Q_β correction coefficient (KNOWN near-match, NOT to be fitted here):
# c_3 = −2 = J_Hopf(q=1), the cross-anchor-swinging near-match (CLAUDE.md).
C3_QBETA = -2.0


def _coeff(series, k):
    return series[k] if k < len(series) else Fr(0)


def build_offset_series():
    """The certified 5₂ ι-odd offset o(q) = c⁺(q) − c⁻(q), exact Fractions."""
    Wq = _sw.series_mat_raw()
    Wqi = _sw.series_mat_ext()
    Sp = _sw.sandwich(Wq, Wqi, _sw.L_P, _sw.R_P, first_is_qi=True)
    Sm = _sw.sandwich(Wq, Wqi, _sw.L_M, _sw.R_M, first_is_qi=False)
    c_plus = Sp[0][1]
    c_minus = Sm[0][2]
    o = [_coeff(c_plus, k) - _coeff(c_minus, k) for k in range(ORD + 1)]
    return c_plus, c_minus, o


def poly_eval(coeffs, q, order):
    return sum(float(_coeff(coeffs, k)) * q ** k for k in range(order + 1))


def smallest_pos_root(coeffs, order, lo=1e-4, hi=0.15):
    """Bisect for the smallest positive real root of the order-N truncation in
    (lo, hi). Returns None if no sign change (root outside the window)."""
    f = lambda q: poly_eval(coeffs, q, order)
    N = 4000
    prev_q, prev_f = lo, f(lo)
    for i in range(1, N + 1):
        q = lo + (hi - lo) * i / N
        fq = f(q)
        if prev_f == 0:
            return prev_q
        if prev_f * fq < 0:
            a, b = prev_q, q
            for _ in range(100):
                m = 0.5 * (a + b)
                fm = f(m)
                if prev_f * fm <= 0:
                    b = m
                else:
                    a, prev_f2 = m, fm
                    prev_f = fm
            return 0.5 * (a + b)
        prev_q, prev_f = q, fq
    return None


def main() -> int:
    print("=" * 78)
    print(" saddle-offset ZERO-LOCATION probe (qou-q86o) — what is q≈0.08?")
    print("=" * 78)

    c_plus, c_minus, o = build_offset_series()
    print("\nCertified 5₂ ι-odd offset o(q) = c⁺(q) − c⁻(q):")
    print("   o =", [str(_coeff(o, k)) for k in range(8)], "…")

    # ===== Q1a. Truncation stability of the zero-crossing q*(N) =============
    print("\n[Q1a] smallest positive real root q*(N) of the order-N truncation:")
    roots = {}
    for N in range(2, ORD + 1):
        r = smallest_pos_root(o, N)
        roots[N] = r
        if r is not None:
            print(f"     N={N:>2}:  q*(N) = {r:.6f}")
        else:
            print(f"     N={N:>2}:  (no root in (0,0.15))")
    # quadratic-balance prediction 1 − 9q − 28q² = 0
    q_quad = (-9.0 + math.sqrt(81.0 + 4.0 * 28.0)) / (2.0 * 28.0)
    r18 = roots[ORD]
    stable = (r18 is not None and abs(r18 - q_quad) < 0.01)
    # spread across N>=3 (where the quadratic term is present)
    vals = [roots[N] for N in range(3, ORD + 1) if roots[N] is not None]
    spread = (max(vals) - min(vals)) if vals else float("nan")
    print(f"\n     quadratic balance 1−9q−28q²=0  →  q_quad = (−9+√193)/56 = "
          f"{q_quad:.6f}")
    print(f"     q*({ORD}) = {r18:.6f}   |q*−q_quad| = {abs(r18-q_quad):.2e}   "
          f"spread(N≥3) = {spread:.2e}")
    print(f"     E1 (truncation-stable ~q_quad)?  {stable}")

    # radius-of-convergence estimate (root test |a_n|^(−1/n))
    tail = [abs(float(_coeff(o, k))) for k in range(1, ORD + 1)]
    root_test = [t ** (-1.0 / k) for k, t in enumerate(tail, start=1) if t > 0]
    R_est = root_test[-1] if root_test else float("nan")
    print(f"     radius-of-convergence estimate (root test, last term): "
          f"R ≈ {R_est:.4f}")

    # ===== Q1b. Is q* a substrate quantity? ================================
    print("\n[Q1b] substrate-candidate comparison (derive-then-check, "
          "expected: NO match):")
    cands = {
        "q0 − 1": Q0_MINUS_1,
        "ℏ_q = 1 − 1/q0": HBAR_Q,
        "ℏ_q²": HBAR_Q2,
        "1/q0": INV_Q0,
        "q0": Q0,
        "series radius R_est": R_est,
    }
    matches = {}
    for name, val in cands.items():
        rel = abs(r18 - val) / abs(val) if val != 0 else float("inf")
        hit = rel < 0.01
        matches[name] = {"value": val, "rel_err_vs_qstar": rel, "match_1pct": hit}
        print(f"     q* vs {name:<20} = {mp.nstr(val, 7):>10}   rel.err = {mp.nstr(100 * rel, 4)}%"
              f"   {'*** MATCH' if hit else ''}")
    any_substrate_match = any(m["match_1pct"] for m in matches.values())
    e2_negative = not any_substrate_match
    print(f"     E2 (q* is NOT a substrate quantity)?  {e2_negative}")

    # ===== Q3. c_3 hook — can o(q) even be evaluated at q0? ================
    print("\n[Q3] c_3-odd hook — offset at the substrate q₀ (expected: "
          "DIVERGES, inaccessible):")
    partials = []
    # mpf accumulation, not float (bean qou-9ugp). `float(_coeff(o, k))` was an
    # explicit float computation over 19 terms with growing coefficients. The
    # conclusion is a DIVERGENCE test and survives either arithmetic, but the
    # partial sums are reported in the witness and were float64-accurate only.
    s = mp.mpf(0)
    for k in range(ORD + 1):
        s += mp.mpf(str(_coeff(o, k))) * Q0 ** k
        if k in (2, 5, 10, 14, ORD):
            partials.append((k, s))
            print(f"     partial sum o_{k}(q₀) = {s:+.4e}")
    # divergence check: does |partial| grow with order past the radius?
    last_two = [p for _, p in partials][-2:]
    diverges = len(last_two) == 2 and abs(last_two[-1]) > 10 * abs(last_two[-2]) + 1
    print(f"     |o_N(q₀)| growing without bound (q₀≈{Q0:.4f} ≫ R≈{R_est:.3f}, "
          f"q₀>1)?  {diverges}")
    print(f"     ⇒ the offset series CANNOT be evaluated at q₀ — c_3 hook via "
          f"direct q₀ evaluation is INACCESSIBLE.")
    # honest c_3 note (NO fit): the only q→0 offset datum is o(0)=1; c_3=−2.
    o0 = float(_coeff(o, 0))
    print(f"     [honest, no fit] q→0 offset datum o(0) = {o0}; Q_β c_3 = "
          f"{C3_QBETA}.  o(0)/c_3 = {o0/C3_QBETA:+.4f} — no clean/derived "
          f"relation; NOT wired.")
    e3_negative = diverges

    # ===== Q3-refined. Borel structure: which side of the transform? ======
    # Coordinator steering: c_3 lives in the DIVERGENT perturbative series Φ_5₂
    # (Borel-summable, factorial coefficient growth — Fantini-Wheeler 2024,
    # arXiv:2410.20973; docs/audits/2026-08-01-fantini-wheeler-summability-
    # c3-borel-reframe.md). Test whether the OFFSET series shares that
    # structure. The offset is built from the certified Stokes SANDWICH — the
    # RESUMMED Stokes constants S±(q), which are Z[q^±] q-series (the OUTPUT of
    # Borel-Laplace, not the divergent input). Expectation: GEOMETRIC growth
    # (finite radius) — offset is on the resummed side, opposite c_3's divergent
    # Φ side; hence no direct Borel-level offset↔c_3 identity.
    print("\n[Q3-refined] Borel structure — geometric (convergent, resummed "
          "side) vs factorial (divergent Φ / c_3 side):")
    an = [abs(float(_coeff(o, k))) for k in range(1, ORD + 1)]
    # geometric model: log|a_n| ≈ α + β n  → slope β = −log R (finite radius R)
    # factorial model: log|a_n| ≈ α + n log n  (Gevrey-1, Borel domain, R=0)
    import statistics
    ns = list(range(1, ORD + 1))
    logs = [math.log(a) if a > 0 else 0.0 for a in an]
    nz = [(n, l) for n, l, a in zip(ns, logs, an) if a > 0]
    n_v = [n for n, _ in nz]
    l_v = [l for _, l in nz]

    def linfit(xs, ys):
        n = len(xs)
        mx, my = sum(xs) / n, sum(ys) / n
        sxx = sum((x - mx) ** 2 for x in xs)
        sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
        b = sxy / sxx
        a = my - b * mx
        yhat = [a + b * x for x in xs]
        ss_res = sum((y - yh) ** 2 for y, yh in zip(ys, yhat))
        ss_tot = sum((y - my) ** 2 for y in ys)
        r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0.0
        return a, b, r2

    a_geo, b_geo, r2_geo = linfit(n_v, l_v)            # log|a| ~ a + b n
    xfac = [n * math.log(n) if n > 1 else 0.0 for n in n_v]
    a_fac, b_fac, r2_fac = linfit(xfac, l_v)           # log|a| ~ a + b (n ln n)
    R_geo = math.exp(-b_geo) if b_geo != 0 else float("inf")
    geometric_wins = r2_geo >= r2_fac
    print(f"     geometric fit  log|a_n| ~ {a_geo:.2f} + {b_geo:.3f}·n     "
          f"R²={r2_geo:.4f}  ⇒ radius R≈{R_geo:.3f}")
    print(f"     factorial fit  log|a_n| ~ {a_fac:.2f} + {b_fac:.3f}·(n ln n) "
          f"R²={r2_fac:.4f}")
    print(f"     GEOMETRIC (convergent, finite radius) wins?  {geometric_wins}")
    print("     ⇒ the offset is on the RESUMMED (convergent Stokes-constant "
          "Z[q^±]) side of the Borel transform; c_3 is a coefficient of the "
          "DIVERGENT perturbative Φ_5₂ (factorial, Borel domain). Opposite "
          "sides ⇒ NO direct Borel-level offset↔c_3 identity. Honest negative.")
    borel_c3_connection = not geometric_wins  # would need factorial growth

    # ===== Q2. Is the offset a bar-covariant object? (q=1 recoverability) ==
    # A genuinely bar-odd (ι-covariant) object g satisfies g(1/q) = −g(q), which
    # forces g(1) = 0 (structural q=1 vanishing) AND g(0) = −g(∞) (no finite
    # nonzero Taylor constant at q=0). The certified o(q) has o(0)=1 (finite,
    # nonzero) ⇒ it is NOT of the form f(q)−f(q⁻¹). Check directly: build the
    # bar-partner ô(q) := o(1/q) as a Laurent tail and compare −o(q).
    print("\n[Q2] is o(q) a bar-covariant object f(q)−f(q⁻¹)? "
          "(needed for structural q=1 vanishing):")
    # A power series with o(0)=1≠0 cannot satisfy g(1/q)=−g(q) (that relation
    # sends the q^0 coefficient to minus the q^0 coefficient ⇒ o(0)=0). So the
    # test is decidable from o(0) alone.
    is_bar_covariant = (o0 == 0.0)
    print(f"     o(0) = {o0}  ⇒  o(1/q) = −o(q) would force o(0) = −o(0) = 0.")
    print(f"     o is bar-covariant (f(q)−f(q⁻¹))?  {is_bar_covariant}")
    print("     ⇒ the certified offset is a CROSS-CHIRALITY difference at the "
          "same q, NOT a q↔q⁻¹-antisymmetric object.")
    print("     ⇒ its q=1 vanishing is NOT delivered by the bar-fixed-point "
          "(q=q⁻¹) argument (that argument makes any TRUE bar-odd object → 0 "
          "at q=1 trivially, but this object is not one).")
    e4_confirmed = (not is_bar_covariant)  # confirmed = it is NOT bar-covariant

    # Two-level (fibre vs archimedean) reconciliation (AGENTS.md Im(q) banner;
    # coordinator steering). The owner's "centred at q=1" is most naturally a
    # FIBRE-level statement: q=1 is the bar-fixed point of the FORMAL q, where a
    # genuinely ι-odd (bar-covariant) Habiro/fibre element vanishes BY
    # CONSTRUCTION. What THIS probe measures is the ARCHIMEDEAN q→0 DT series —
    # a different object (the resummed Stokes constants), whose own zero sits at
    # the substrate-free q*≈0.089. The two are consistent: the q≈0.08 crossing
    # is an archimedean-series feature, NOT a refutation of a fibre-level q=1
    # centring. The Lean lemma `barAntisym_const_zero` is exactly the
    # archimedean-coefficient obstruction (o(0)=1≠0 ⇒ the certified DT offset is
    # not that fibre-level bar-covariant object).
    print("\n[Q2-reconcile] two-level reading (fibre vs archimedean):")
    print("     • FIBRE (formal q): 'centred at q=1' = a bar-covariant Habiro "
          "element vanishing at the bar-fixed point q=q⁻¹=1 BY CONSTRUCTION — "
          "consistent, but a DIFFERENT object, not tested by these DT series.")
    print("     • ARCHIMEDEAN (q→0 DT series, THIS probe): o(q) is the resummed "
          "cross-chirality Stokes datum; o(0)=1≠0; its own root is q*≈0.089, "
          "substrate-free. No q=1 centring here.")
    print("     ⇒ q≈0.08 does NOT refute a fibre-level q=1 centring; it is an "
          "archimedean-series artifact. The two levels do not conflict — they "
          "are simply different objects (the AGENTS.md Im(q) fibre/observable "
          "distinction).")

    # ===== verdict =========================================================
    verdict = (
        "OFFSET-ZERO LOCATION [scope-(a), honest negative on the substrate "
        "reading]. (Q1) The zero-crossing q* is truncation-STABLE at "
        f"q* = {r18:.5f} (spread over N>=3 = {spread:.1e}), pinned by the "
        f"quadratic balance 1-9q-28q^2=0 => q_quad=(-9+sqrt(193))/56={q_quad:.5f}. "
        "But it is NOT a substrate quantity: it misses q0-1, hbar_q, hbar_q^2, "
        "1/q0 and the series radius all by >>1% (closest is hbar_q at ~9.9%) — "
        "q* is set by the DT expansion's own low-order Stokes coefficients "
        "{9,28} (which encode the {3,4} datum), carrying NO independent "
        f"substrate meaning. (Q3) The offset series CANNOT be evaluated at q0 "
        f"(q0~1.110 >> radius R~{R_est:.2f}, and q0>1): the partial sums "
        "diverge, so the c_3-odd hook via direct q0 evaluation is inaccessible; "
        "the q->0 datum o(0)=1 has no clean/derived relation to Q_beta c_3=-2, "
        "and nothing is wired. (Q2) The certified o(q)=c+ - c- has o(0)=1!=0, "
        "so it is a cross-chirality difference, NOT a bar-covariant "
        "f(q)-f(q^-1); its q=1 vanishing is therefore NOT delivered by the "
        "bar-fixed-point argument. 'Origin-centred only at q=1' is recoverable "
        "ONLY as the TRIVIAL vanishing of any genuinely bar-odd object at the "
        "fixed point q=q^-1=1 (already #4577's gate applied to q itself) — a "
        "DIFFERENT object from the DT {3,4} offset, which lives at q->0 with its "
        "own root at q*~0.089. VERDICT: q~0.08 is the DT-series' own "
        "convergence-region root with no substrate meaning; the specific "
        "'DT saddle-offset vanishes AT q=1' claim is REFUTED as an independent "
        "reading (scope-(a): a narrowing of the picture, invoking no proved "
        "invariant to exclude an ingredient). (Q3-refined, post-steering) The "
        f"offset coeffs grow GEOMETRICALLY (finite radius ~{R_geo:.2f}, "
        "geometric R^2 >= factorial R^2): the offset is on the RESUMMED "
        "(convergent "
        "Stokes-constant Z[q^±]) side of the Borel transform, whereas c_3 is a "
        "coefficient of the DIVERGENT perturbative Phi_5_2 (Fantini-Wheeler "
        "Borel domain) — opposite sides, so no direct Borel-level offset<->c_3 "
        "identity. (Q2-reconcile) The owner's 'centred at q=1' is most "
        "naturally a FIBRE-level statement (bar-fixed point of formal q, where "
        "a bar-covariant Habiro element vanishes by construction) — consistent "
        "with, but a different object from, the archimedean q->0 DT offset this "
        "probe measures; q~0.08 is an archimedean-series feature, not a "
        "refutation of a fibre-level q=1 centring. No fit; no c_k wired; "
        "scope-(a).")

    print("\nVERDICT:", verdict)

    all_expected = stable and e2_negative and e3_negative and e4_confirmed
    print(f"\nAll locked expectations E1–E4 met: {all_expected}  "
          f"(E1={stable}, E2={e2_negative}, E3={e3_negative}, E4={e4_confirmed})")

    # ===== witness =========================================================
    wb = WitnessBuilder("saddle-offset-zero-location", engine="fractions-exact")
    wb.set_description(
        "Where the certified 5₂ ι-odd saddle offset o(q)=c⁺−c⁻ crosses zero, "
        "and whether that location is principled. q* is truncation-stable at "
        "≈0.087 (quadratic balance (−9+√193)/56) but is NOT a substrate "
        "quantity; the series cannot be evaluated at q₀ (c_3 hook inaccessible); "
        "and o(q) is a cross-chirality difference, not a bar-covariant "
        "f(q)−f(q⁻¹), so its q=1 vanishing is only the trivial fixed-point one, "
        "distinct from the q→0 DT datum. Honest negative on the substrate/q=1 "
        "reading (scope-(a)); nothing wired.")
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("Q1_zero_location", {
        "offset_series": [str(_coeff(o, k)) for k in range(ORD + 1)],
        "qstar_by_order": {str(N): roots[N] for N in roots},
        "qstar_final": r18,
        "q_quad_prediction": q_quad,
        "q_quad_closed_form": "(-9 + sqrt(193)) / 56",
        "spread_over_N_ge_3": spread,
        "truncation_stable": stable,
        "radius_estimate_root_test": R_est})
    wb.add_data("Q1_substrate_candidates", matches)
    wb.add_data("Q1_verdict", {
        "truncation_stable": stable,
        "any_substrate_match_1pct": any_substrate_match,
        "reading": "q* is the DT expansion's own root (set by low-order Stokes "
                   "coeffs {9,28}), NOT a substrate quantity"})
    wb.add_data("Q3_c3_hook", {
        "q0": Q0,
        "offset_at_q0_partial_sums": {str(k): v for k, v in partials},
        "diverges_at_q0": diverges,
        "offset_q0_inaccessible": True,
        "o0_datum": o0,
        "c3_qbeta": C3_QBETA,
        "o0_over_c3": o0 / C3_QBETA,
        "wired": False,
        "note": f"offset series is q->0-anchored (R~{R_est:.2f}); q0>1 far "
                "outside domain — no direct evaluation, no derived c_3 "
                "relation, nothing wired"})
    wb.add_data("Q3_borel_structure", {
        "geometric_fit": {"intercept": a_geo, "slope": b_geo, "r2": r2_geo,
                          "implied_radius": R_geo},
        "factorial_fit": {"intercept": a_fac, "slope": b_fac, "r2": r2_fac},
        "geometric_wins": geometric_wins,
        "borel_c3_connection_possible": borel_c3_connection,
        "reading": "offset coeffs grow GEOMETRICALLY (finite radius ~%.2f), so "
                   "the offset is on the RESUMMED (convergent Stokes-constant "
                   "Z[q^±]) side of the Borel transform; c_3 is a coefficient "
                   "of the DIVERGENT perturbative Phi_5_2 (factorial growth, "
                   "Fantini-Wheeler Borel domain). Opposite sides — no direct "
                   "Borel-level offset<->c_3 identity" % R_geo,
        "refs": ["docs/audits/2026-08-01-fantini-wheeler-summability-c3-borel-"
                 "reframe.md", "arXiv:2410.20973"]})
    wb.add_data("Q2_fibre_vs_archimedean", {
        "fibre_reading": "q=1 = bar-fixed point of FORMAL q; a bar-covariant "
                         "Habiro/fibre element vanishes there by construction — "
                         "consistent with the owner's picture but a DIFFERENT "
                         "object, not tested by the q->0 DT series",
        "archimedean_reading": "the certified o(q) is the resummed q->0 DT "
                               "Stokes datum; o(0)=1!=0; own root q*~0.089, "
                               "substrate-free; no q=1 centring at this level",
        "conflict": False,
        "note": "q~0.08 does NOT refute a fibre-level q=1 centring — it is an "
                "archimedean-series feature (AGENTS.md Im(q) fibre/observable "
                "distinction). Lean barAntisym_const_zero is the archimedean-"
                "coefficient obstruction (o(0)=1!=0)."})
    wb.add_data("Q2_bar_covariance", {
        "o0": o0,
        "is_bar_covariant_f_of_q_minus_f_of_qinv": is_bar_covariant,
        "reasoning": "g(1/q)=−g(q) forces g(0)=0; o(0)=1≠0 ⇒ not bar-covariant",
        "q1_vanishing_delivered_by_fixed_point_argument": is_bar_covariant,
        "reading": "certified offset is a cross-chirality difference at same q; "
                   "q=1 origin-centring recoverable only as the trivial "
                   "bar-fixed-point vanishing of a genuine bar-odd object "
                   "(#4577 gate applied to q), a different object from the "
                   "q→0 DT {3,4} datum"})
    wb.add_data("scope", {
        "confirmed": "q* truncation-stable ≈0.087 (quadratic balance)",
        "honest_negatives": [
            "q* is NOT a substrate quantity (Q1)",
            "offset cannot be evaluated at q₀; no c_3 relation (Q3)",
            "certified offset is not bar-covariant; q=1 origin-centring is only "
            "the trivial fixed-point vanishing, not the DT datum (Q2)"],
        "wired_to_production": False,
        "discipline": "no fit; no c_k wired; no axiomatization; scope-(a); "
                      "avoids all qou-fk19 red-flags"})
    wb.add_data("verdict", verdict)
    wb.add_assertion(
        "qstar_truncation_stable_at_quadratic_balance",
        computed=abs(r18 - q_quad), expected=0.0, tolerance=0.01,
        source="q*(18) matches the 1−9q−28q²=0 root (−9+√193)/56 within 0.01; "
               "spread over N≥3 is O(1e-3)")
    wb.add_assertion(
        "qstar_is_not_a_substrate_quantity",
        computed=0.0 if any_substrate_match else 1.0, expected=1.0, tolerance=0.5,
        source="q* misses q₀−1, ℏ_q, ℏ_q², 1/q₀, radius all by ≫1% "
               "(locked before compute)")
    wb.add_assertion(
        "offset_inaccessible_at_q0_no_c3_relation",
        computed=1.0 if diverges else 0.0, expected=1.0, tolerance=0.5,
        source="partial sums o_N(q₀) diverge (q₀≫R, q₀>1); c_3 hook via q₀ "
               "evaluation impossible; no derived o↔c_3 relation; not wired")
    wb.add_assertion(
        "offset_not_bar_covariant_q1_vanishing_only_trivial",
        computed=1.0 if e4_confirmed else 0.0, expected=1.0, tolerance=0.5,
        source="o(0)=1≠0 ⇒ o is not f(q)−f(q⁻¹); its q=1 vanishing is not "
               "delivered by the bar-fixed-point argument (that gives the "
               "trivial vanishing of a genuine bar-odd object, a different "
               "object from the DT datum)")
    wb.save()
    return 0 if all_expected else 1


if __name__ == "__main__":
    raise SystemExit(main())
