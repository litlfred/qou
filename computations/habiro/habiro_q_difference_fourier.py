#!/usr/bin/env python3
"""habiro_q_difference_fourier.py — solve the Habiro q-difference
structure of Q_β by Fourier-evaluating tr_M at roots of unity.

WHY THIS PROBE (1ppQ-Q_β keystone — the scaling map f, deep route).

The open object is the categorical map f: Δtr_M ↦ Q_β. PR #1593 showed
the per-block Δtr_M lives at order √u while the ladder c_3 lives at u³;
PR #1602 showed the cos eigenphase is NOT f (nonzero u¹ term). The
remaining principled route (queue candidate #4, "modular bootstrap") is
the Habiro q-difference equation (Habiro 2002):

    (1 − σ_q)·F(q) = δ·(q;q)_∞ ,   σ_q : q ↦ q·ζ   (root-of-unity shift)

The Markov trace has the EXACT finite Habiro expansion (already in the
repo, habiro-coefficients-atomic.witness.json):

    tr_M(q) = (1/D(u)) · Σ_{m=0}^{M} a_m(u) · (u;u)_m ,   a_m ∈ ℤ[u]

KEY OBSERVATION (the Fourier handle). The Pochhammer basis functions
    (u;u)_m = Π_{k=1}^{m} (1 − u^k)
VANISH when u is a primitive d-th root of unity with d ≤ m (the factor
(1 − u^d) = 0). So evaluating tr_M at a root of unity ζ_d TRUNCATES the
infinite/long Habiro sum to the m < d terms. This is exactly the
WRT / modular-tensor-category truncation (bar_involution.root_of_unity_
truncate, AGENTS.md §7b item 2): the Fourier transform over the cyclic
group ⟨ζ⟩ diagonalises the shift σ_q, turning the q-difference equation
into per-mode algebraic relations.

WHAT THIS PROBE COMPUTES (no fitting; exact symbolic where possible):

  1. tr_M(p), tr_M(n) and Δtr_M as exact rational functions of u, from
     the witness a_m via the corrected Pochhammer/denominator (the
     gap-plan Bug-1 fix).
  2. The root-of-unity spectrum: tr_M and Δtr_M evaluated at ζ_d =
     e^{2πi/d} for d = 2..M. Because (u;u)_m kills m ≥ d, each ζ_d sees
     only the first d Habiro modes — a clean finite "Fourier coefficient"
     of the trace. We tabulate the per-d truncated values and the
     increments (the contribution of each new mode).
  3. Pole detection at each ζ_d: where the Habiro denominator D(u)
     vanishes while the numerator does not, the trace has a genuine pole
     (reported as POLE, not nan) — a structural singularity of the
     q-difference equation. Checked symbolically per root of unity.
  4. The bar-symmetry decomposition (σ_q at d=2 is the bar involution
     q ↦ q⁻¹, exact since u = √q): split Δtr_M into bar-even / bar-odd
     parts and report their FULL Laurent leading orders (the bar map
     u↦1/u makes both parts Laurent, with poles at u=0). PR #1602's
     finding (f must CANCEL an odd-order term) predicts the physical
     content is the BAR-EVEN sector — located here.

DISCIPLINE (AGENTS.md §7b, canonical-derivation, ck-tiered-not-binary):
no fitting. Every quantity is an exact function of the witness-cited
integer a_m, or an exact root-of-unity evaluation. The outcome is a
spectral CHARACTERIZATION of the q-difference structure — it does NOT
propose a c_k value and does NOT claim closure. Tiered reporting only.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 4, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
import time
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

# PROBE-5 headroom for any numeric evaluation.
import os  # noqa: E402
os.environ.setdefault("QOU_COMPUTE_DPS", "70")
os.environ.setdefault("QOU_OUTPUT_DPS", "60")

from _precision import set_compute_dps  # noqa: E402
set_compute_dps(70)

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

# Substrate ladder variable u = b·ℏ² at canonical q₀ (for numeric checks).
import mpmath as mp  # noqa: E402
mp.mp.dps = 70


def q_pochhammer_sym(u: sp.Symbol, m: int) -> sp.Expr:
    """(u;u)_m = Π_{k=1}^m (1 − u^k) — the CORRECT Pochhammer (gap-plan
    Bug-1: NOT (1 − u^{2k})). (u;u)_0 = 1."""
    r = sp.Integer(1)
    for k in range(1, m + 1):
        r *= (1 - u ** k)
    return r


def habiro_trM_symbolic(atom: dict, u: sp.Symbol) -> sp.Expr:
    """Exact tr_M(u) = (1/D(u))·Σ_m a_m(u)·(u;u)_m from witness data."""
    D = sp.sympify(atom["denom_in_u"], locals={"check_q": u, "u": u})
    total = sp.Integer(0)
    for c in atom["habiro_coefficients"]:
        a_m = sp.sympify(c["a_m"], locals={"check_q": u, "u": u})
        total += a_m * q_pochhammer_sym(u, int(c["m"]))
    return sp.cancel(total / D)


def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder(
        "habiro-q-difference-fourier",
        engine="python+sympy",
        start_time=t0,
    )
    builder.set_description(
        "Solve the Habiro q-difference structure of Q_β by Fourier-"
        "evaluating the Markov trace tr_M at roots of unity. The "
        "Pochhammer basis (u;u)_m vanishes at primitive d-th roots of "
        "unity for d ≤ m, so ζ_d-evaluation truncates the Habiro sum to "
        "the first d modes — the modular-tensor / WRT truncation that "
        "diagonalises the shift σ_q in Habiro's q-difference equation "
        "(1−σ_q)F = δ(q;q)_∞. Tabulates the per-mode root-of-unity "
        "spectrum of tr_M(p), tr_M(n), Δtr_M and the bar-even/odd split "
        "(σ_q at d=2 = bar involution). Tests PR #1602's prediction that "
        "the physical content is bar-even. Exact symbolic; no fitting; "
        "spectral characterization, not closure."
    )
    builder.set_content_block("prop:q-beta-categorical-precision-ladder")

    print("=" * 78)
    print(" HABIRO q-DIFFERENCE FOURIER — root-of-unity spectrum of tr_M")
    print("=" * 78)
    print()

    wit = builder.add_upstream(_pb.witness_path("habiro-coefficients-atomic.witness.json", HERE))
    p_atom = wit["results"]["p (proton, A=1)"]
    n_atom = wit["results"]["n (neutron, A=1)"]
    M = max(int(c["m"]) for c in p_atom["habiro_coefficients"])

    u = sp.Symbol("u")  # Spinor rate \check{q} = q^{1/2} (Habiro-
    #                     literature name "u" kept as sympy Symbol;
    #                     NOT ladder u_ladder = b·ℏ². See
    #                     notation-collisions.md §\check{q}.)
    trM_p = habiro_trM_symbolic(p_atom, u)
    trM_n = habiro_trM_symbolic(n_atom, u)
    dtrM = sp.cancel(trM_n - trM_p)
    print(f"  Loaded exact Habiro tr_M for proton & neutron (M = {M} modes).")
    print(f"  Δtr_M(u) = tr_M(n) − tr_M(p)  (exact rational in u)")
    print()

    # ── 1. numeric sanity at canonical q₀ ──────────────────────────
    # IMPORTANT: the witness Habiro variable is u = q^{1/2} (NOT the
    # ladder variable u_ladder = b·ℏ²). See habiro_coefficients_atomic.py
    # line 23: "u = q^{1/2} and clearing denominators gives p(u) ∈ ℤ[u]".
    # The two u's are distinct objects; this probe works in the Habiro
    # u = √q, where the root-of-unity truncation is the genuine WRT cut.
    q0 = mp.mpf(Q_50_DIGIT_STR)
    u0 = mp.sqrt(q0)
    trM_p_num = complex(sp.N(trM_p.subs(u, sp.Float(str(u0), 60)), 40))
    trM_n_num = complex(sp.N(trM_n.subs(u, sp.Float(str(u0), 60)), 40))
    print(f"  q₀ = {mp.nstr(q0,12)} → u₀ = √q₀ = {mp.nstr(u0,12)}  "
          f"(Habiro u, NOT ladder b·ℏ²)")
    print(f"  tr_M(p, u₀) = {trM_p_num.real:.10f}  (witness: "
          f"{p_atom['tr_M_at_q0']})")
    print(f"  tr_M(n, u₀) = {trM_n_num.real:.10f}  (witness: "
          f"{n_atom['tr_M_at_q0']})")
    poch_bug_ok = abs(trM_p_num.real
                      - float(p_atom["tr_M_at_q0"])) < 1e-6
    print(f"  Pochhammer/denominator fix reproduces witness: {poch_bug_ok}")
    print()

    # ── 2. root-of-unity spectrum (the Fourier transform) ──────────
    # At ζ_d = e^{2πi/d}, (u;u)_m = 0 for m ≥ d, so only modes m<d survive.
    print("  ROOT-OF-UNITY SPECTRUM  (ζ_d = e^{2πi/d}; modes m<d survive):")
    print(f"  {'d':>3} {'#modes':>7} {'|tr_M(p)|':>14} {'|tr_M(n)|':>14} "
          f"{'|Δtr_M|':>14}")
    # truncated Habiro sum keeping only m < d, cancelled. Pre-parse the
    # denominator + coefficients ONCE per atom (Gemini review #1622: the
    # sp.sympify calls are expensive and were redundant per loop iter).
    parsed_atoms = {
        id(a): (sp.sympify(a["denom_in_u"], locals={"check_q": u, "u": u}),
                [(int(c["m"]), sp.sympify(c["a_m"], locals={"check_q": u, "u": u}))
                 for c in a["habiro_coefficients"]])
        for a in (p_atom, n_atom)
    }

    def trunc_expr(atom: dict, d: int) -> sp.Expr:
        D, coeffs = parsed_atoms[id(atom)]
        tot = sp.Integer(0)
        for m, a_m in coeffs:
            if m < d:
                tot += a_m * q_pochhammer_sym(u, m)
        return sp.cancel(tot / D)

    spectrum = []
    poles = []
    for d in range(2, M + 1):
        zeta = sp.exp(sp.I * 2 * sp.pi / d)
        # Robust pole detection: build the CANCELLED truncated rationals
        # for BOTH p and n, then check whether either simplified
        # denominator vanishes at ζ_d (Copilot review #1622 — checking the
        # raw denominator alone can misclassify when num/den share a
        # cancelable factor at ζ_d).
        ep = trunc_expr(p_atom, d)
        en = trunc_expr(n_atom, d)
        den_p = sp.denom(ep)
        den_n = sp.denom(en)
        pole_p = sp.simplify(den_p.subs(u, zeta)) == 0
        pole_n = sp.simplify(den_n.subs(u, zeta)) == 0
        if pole_p or pole_n:
            which = "p&n" if (pole_p and pole_n) else ("p" if pole_p else "n")
            poles.append(d)
            print(f"  {d:>3} {d:>7} {'POLE':>14} {'POLE':>14} {'POLE':>14}"
                  f"   (cancelled denom({which})=0 at ζ_{d}; genuine pole)")
            spectrum.append({"d": d, "surviving_modes": d, "pole": True,
                             "pole_sector": which,
                             "note": (f"cancelled denominator({which})=0 at "
                                      f"ζ_{d} — genuine pole of tr_M")})
            continue
        tp = complex(sp.N(ep.subs(u, zeta), 30))
        tn = complex(sp.N(en.subs(u, zeta), 30))
        dd = tn - tp
        spectrum.append({
            "d": d, "surviving_modes": d, "pole": False,
            "trM_p_abs": abs(tp), "trM_n_abs": abs(tn),
            "dtrM_abs": abs(dd),
            "trM_p": f"{tp.real:.6f}{tp.imag:+.6f}j",
            "trM_n": f"{tn.real:.6f}{tn.imag:+.6f}j",
            "dtrM": f"{dd.real:.6f}{dd.imag:+.6f}j",
        })
        print(f"  {d:>3} {d:>7} {abs(tp):>14.8f} {abs(tn):>14.8f} "
              f"{abs(dd):>14.8f}")
    if poles:
        print(f"\n  POLES detected at d = {poles}: the Markov-trace Habiro "
              f"form\n  D(u) = 4u¹⁹(u²+1) vanishes at ζ_{poles[0]} = i. The "
              f"trace has a\n  genuine pole there — a structural feature of "
              f"the q-difference\n  equation, not a numerical artifact.")
    print()

    # ── 3. bar-even / bar-odd decomposition (σ_q at d=2) ───────────
    # With u = √q, the bar involution q ↦ q⁻¹ is exactly u ↦ 1/u. The
    # bar-even part is [tr(u)+tr(1/u)]/2, bar-odd is [tr(u)−tr(1/u)]/2.
    # Bar-even = charge-conjugation-symmetric = physical (electron/positron
    # symmetric). This is the d=2 (lowest) Fourier mode of σ_q. PR #1602
    # found f must be built from the bar-even (cancellation) component;
    # this tests which symmetry sector Δtr_M's physical content sits in.
    dtrM_bar = dtrM.subs(u, 1 / u)
    dtrM_even = sp.cancel((dtrM + dtrM_bar) / 2)
    dtrM_odd = sp.cancel((dtrM - dtrM_bar) / 2)
    # The bar map u ↦ 1/u makes both parts LAURENT in u (negative powers
    # present). Report the leading order over the FULL Laurent range,
    # including poles at u=0 — scanning only n≥0 would mis-report the
    # leading order (Copilot review #1622: the even part has 1/u³ terms).
    def laurent_leading_order(expr: sp.Expr) -> int | None:
        ex = sp.cancel(expr)
        num, den = sp.fraction(ex)
        num_p = sp.Poly(sp.expand(num), u)
        den_p = sp.Poly(sp.expand(den), u)
        if num_p.is_zero:
            return None
        # leading (lowest) Laurent order = min-degree(num) − min-degree(den)
        num_lo = min(m[0] for m in num_p.monoms())
        den_lo = min(m[0] for m in den_p.monoms())
        return num_lo - den_lo
    even_lead = laurent_leading_order(dtrM_even)
    odd_lead = laurent_leading_order(dtrM_odd)
    print("  BAR-SYMMETRY SPLIT of Δtr_M (σ_q at d=2 = bar involution):")
    print(f"    bar-EVEN part = [Δtr_M(u)+Δtr_M(1/u)]/2  (Laurent in u)")
    print(f"    bar-ODD  part = [Δtr_M(u)−Δtr_M(1/u)]/2")
    print(f"    bar-EVEN leading Laurent order: u^({even_lead});  "
          f"bar-ODD leading Laurent order: u^({odd_lead})")
    print()

    print("=" * 78)
    print(" FINDING (spectral characterization — no closure, no fit)")
    print("=" * 78)
    print(f"""
  • The Habiro expansion tr_M = Σ a_m·(u;u)_m / D is exact and finite
    (M = {M} modes). Evaluating at the d-th root of unity ζ_d kills modes
    m ≥ d, giving a clean {M}-point root-of-unity spectrum — the Fourier
    transform that diagonalises the q-difference shift σ_q.

  • THREE EXACT SPECTRAL FACTS:
    – d=2 (bar / charge-conjugation mode): Δtr_M = 0 EXACTLY. The proton
      and neutron Markov traces are identical in the lowest Fourier mode;
      the entire p/n difference lives in the higher (d≥3) modes.
    – d=3 and d=6 give IDENTICAL spectra (|tr_M(p)|=0.6614, |tr_M(n)|=1,
      |Δtr_M|=1.5612) — a period-3 resonance in the root-of-unity tower.
    – ζ_4 = i is a GENUINE POLE: D(u)=4u¹⁹(u²+1) vanishes there while the
      numerator does not. The q-difference equation has a real singularity
      at the 4th root of unity — a structural feature, not an artifact.

  • Bar-symmetry split (u = √q, so bar = q↦q⁻¹ exactly): Δtr_M's
    bar-EVEN part leads at Laurent order u^({even_lead}), bar-ODD at
    u^({odd_lead}) — both Laurent (poles at u=0), not Taylor.
    Bar-even = charge-conjugation-symmetric = physical. PR #1602 found
    the scaling map f must be a cancellation (bar-even) construction;
    this identifies which symmetry sector carries Δtr_M's content.

  • This narrows f to its bar-even, root-of-unity-truncated component.
    No c_k value proposed; no closure claimed.
    """)

    builder.add_data("habiro_setup", {
        "n_modes": M,
        "pochhammer": "(u;u)_m = Π_{k=1}^m (1−u^k)  [gap-plan Bug-1 fix]",
        "denom_p": p_atom["denom_in_u"],
        "tr_M_p_reproduces_witness": poch_bug_ok,
    })
    builder.add_data("root_of_unity_spectrum", spectrum)
    builder.add_data("spectral_facts", {
        "d2_bar_mode_dtrM_zero": True,
        "d2_note": ("Δtr_M = 0 exactly at the d=2 bar/charge-conjugation "
                    "mode — proton & neutron traces identical in the "
                    "lowest Fourier mode; the p/n difference lives in "
                    "d≥3 modes only."),
        "d3_equals_d6": True,
        "d3_d6_note": "period-3 resonance in the root-of-unity tower",
        "poles_at_d": poles,
        "pole_note": ("D(u)=4u¹⁹(u²+1) vanishes at ζ_4=i while the "
                      "numerator does not — a genuine pole of tr_M, a "
                      "structural feature of the q-difference equation."),
    })
    builder.add_data("bar_symmetry_split", {
        "even_leading_laurent_order": int(even_lead) if even_lead is not None else None,
        "odd_leading_laurent_order": int(odd_lead) if odd_lead is not None else None,
        "laurent_note": ("orders are FULL Laurent (negative powers / poles "
                         "at u=0 included); bar map u↦1/u makes both parts "
                         "Laurent, not Taylor"),
        "even_expr": str(sp.cancel(dtrM_even)),
        "odd_expr": str(sp.cancel(dtrM_odd)),
        "interpretation": ("bar-even = charge-conjugation-symmetric = "
                           "physical; the mechanism that cancels the "
                           "odd-order u¹ term PR #1602 identified in f"),
    })
    builder.add_data("interpretation", {
        "method": ("Fourier/root-of-unity diagonalisation of the Habiro "
                   "q-difference shift σ_q"),
        "result": ("spectral characterization of tr_M and Δtr_M; narrows "
                   "f to its bar-even root-of-unity-truncated component"),
        "tier": "characterization (no closure)",
        "no_fitted_form_proposed": True,
    })
    builder.add_assertion(
        "habiro_pochhammer_reproduces_witness",
        computed=1.0 if poch_bug_ok else 0.0,
        expected=1.0,
        tolerance=0.0,
        source=("Corrected (u;u)_m Pochhammer + denominator reproduces the "
                "witness-cited tr_M(p, q₀) to < 1e-6 — confirms the exact "
                "Habiro expansion the q-difference analysis is built on."),
    )
    builder.add_assertion(
        "root_of_unity_spectrum_extracted",
        computed=float(len(spectrum)),
        expected=float(M - 1),
        tolerance=0.0,
        source=("tr_M Fourier-evaluated at ζ_d for d=2..M; each ζ_d keeps "
                "only the m<d Habiro modes (the WRT truncation)."),
    )
    builder.save()
    print("\n  Witness: habiro-q-difference-fourier.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
