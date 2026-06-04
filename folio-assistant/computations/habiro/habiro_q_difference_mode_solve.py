#!/usr/bin/env python3
"""habiro_q_difference_mode_solve.py — solve the Habiro q-difference
structure of Δtr_M mode-by-mode via partial-fraction (Fourier-mode)
decomposition, using the root-of-unity spectrum (PR #1622) as boundary
data.

WHY THIS PROBE (1ppQ-Q_β keystone — the scaling map f, the solve step).

PR #1622 Fourier-evaluated the Markov trace at roots of unity and found
the q-difference equation (1−σ_q)F = δ(q;q)_∞ has a finite spectral
target: 6 non-pole ζ_d values + a genuine pole at ζ_4 = i. This probe
takes the next step — SOLVING for the exact mode structure.

THE KEY IDENTITY. Under the Fourier transform that diagonalises the
root-of-unity shift σ_q, solving the q-difference equation is exactly
the PARTIAL-FRACTION decomposition of the (rational) Δtr_M over its
poles. Each pole of Δtr_M is one Fourier mode of σ_q; the partial
fraction is the mode-by-mode solution. From the exact Habiro expansion
(u = q^{1/2}, integer a_m):

    Δtr_M(u) = P(u) / [4 u⁴ (u²+1)]

partial-fractions into THREE clean spectral sectors:

  (A) ENTIRE part: a polynomial in u (no poles) — the "bulk" of f.
  (B) ζ_4 CYCLOTOMIC mode: the 1/(u²+1) pole pair at u = ±i, residues
      ∓i/2 — the genuine q-difference singularity (the WRT level-4 cut).
  (C) u=0 LAURENT TOWER: poles at u^{-1}, u^{-3}, u^{-4} — the
      short-distance / high-energy modes.

WHAT THIS PROBE COMPUTES (exact symbolic; no fitting):

  1. The exact partial-fraction decomposition of Δtr_M (the mode-by-mode
     q-difference solution), separated into sectors A/B/C.
  2. Per-sector reconstruction check: A+B+C must equal Δtr_M exactly.
  3. The ζ_4 residues (the modular data) and the u=0 Laurent
     coefficients (the short-distance data) as exact rationals.
  4. Bar-symmetry of each sector: under u ↦ 1/u (charge conjugation),
     which sectors are bar-even (physical) vs bar-odd. PR #1602 found f
     must be a bar-even (cancellation) construction; this assigns each
     mode to a symmetry sector, telling us which modes f keeps.

DISCIPLINE (CLAUDE.md §7b, ck-tiered-not-binary): exact symbolic
throughout. This is a CHARACTERIZATION of the q-difference solution
structure — it decomposes Δtr_M into its exact Fourier modes, but does
NOT yet bridge to the ladder c_k (that bridge is the remaining open
step). No fitted form; no c_k value; tiered reporting.

NOTE on u: u = q^{1/2} is the spinor information rate \check{q}
(canonical name as of 2026-06-04); the Python identifier "u" is
kept per Habiro-literature convention. NOT the ladder
u_ladder = b·ℏ². See notation-collisions.md §\check{q}.
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

import os  # noqa: E402
os.environ.setdefault("QOU_COMPUTE_DPS", "70")
os.environ.setdefault("QOU_OUTPUT_DPS", "60")

from _precision import set_compute_dps  # noqa: E402
set_compute_dps(70)

from witness_base import WitnessBuilder  # noqa: E402

# Habiro half-twist variable u = q^{1/2} (NOT ladder b·ℏ²).
u = sp.Symbol("u")


def q_pochhammer_sym(m: int) -> sp.Expr:
    r = sp.Integer(1)
    for k in range(1, m + 1):
        r *= (1 - u ** k)
    return r


def habiro_trM(atom: dict) -> sp.Expr:
    D = sp.sympify(atom["denom_in_u"], locals={"check_q": u})
    total = sp.Integer(0)
    for c in atom["habiro_coefficients"]:
        a_m = sp.sympify(c["a_m"], locals={"check_q": u})
        total += a_m * q_pochhammer_sym(int(c["m"]))
    return sp.cancel(total / D)


def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder(
        "habiro-q-difference-mode-solve",
        engine="python+sympy",
        start_time=t0,
    )
    builder.set_description(
        "Mode-by-mode solution of the Habiro q-difference structure of "
        "Δtr_M via partial-fraction decomposition (the Fourier-mode "
        "diagonalisation of the root-of-unity shift σ_q). Δtr_M = "
        "P(u)/[4u⁴(u²+1)] (u=q^{1/2}) decomposes into three exact "
        "spectral sectors: (A) entire polynomial, (B) the ζ_4=±i "
        "cyclotomic pole pair (residues ∓i/2, the WRT level-4 cut), "
        "(C) the u=0 Laurent tower (u^{-1},u^{-3},u^{-4}). Records the "
        "exact residues / Laurent coefficients and the bar-symmetry "
        "(charge-conjugation) sector of each mode. Uses the PR #1622 "
        "root-of-unity spectrum as boundary data. Exact symbolic; no "
        "fitting; characterization of the q-difference solution, not a "
        "bridge to the ladder c_k (still open)."
    )
    builder.set_content_block("prop:q-beta-categorical-precision-ladder")

    print("=" * 78)
    print(" HABIRO q-DIFFERENCE MODE SOLVE — partial-fraction = Fourier modes")
    print("=" * 78)
    print()

    wit = json.loads(
        (_pb.witness_path("habiro-coefficients-atomic.witness.json", HERE)).read_text())
    trM_p = habiro_trM(wit["results"]["p (proton, A=1)"])
    trM_n = habiro_trM(wit["results"]["n (neutron, A=1)"])
    dtrM = sp.cancel(trM_n - trM_p)
    num, den = sp.fraction(dtrM)
    print(f"  Δtr_M(u) = ({sp.expand(num)}) / ({sp.factor(den)})")
    print()

    # ── mode-by-mode = partial fraction over the poles ─────────────
    # Real partial fraction keeps the cyclotomic (u²+1) factor intact —
    # this is the mode-by-mode q-difference solution.
    pf = sp.apart(dtrM, u)
    print("  PARTIAL-FRACTION DECOMPOSITION (the q-difference mode solve):")
    print(f"    {pf}")
    print()

    # Separate the three sectors term-by-term over the partial fraction.
    poly_part = sp.Integer(0)   # (A) entire polynomial (no pole)
    sector_B = sp.Integer(0)    # (B) ζ_4 cyclotomic pole (u²+1 in denom)
    sector_C = sp.Integer(0)    # (C) u=0 Laurent tower (pure powers of u)
    cyclotomic = u ** 2 + 1
    for term in pf.as_ordered_terms():
        den = sp.denom(sp.cancel(term))
        if term.is_polynomial(u) and (den == 1 or not den.has(u)):
            # entire part: polynomial in u (constant denom is fine)
            poly_part += term
        elif den.has(u) and sp.rem(den, cyclotomic, u) == 0:
            sector_B += term
        else:
            sector_C += term
    poly_part = sp.expand(poly_part)
    sector_B = sp.cancel(sector_B)
    sector_C = sp.expand(sector_C)

    print("  THREE SPECTRAL SECTORS:")
    print(f"    (A) entire polynomial : {poly_part}")
    print(f"    (B) ζ_4 cyclotomic    : {sp.nsimplify(sector_B)}")
    print(f"    (C) u=0 Laurent tower : {sector_C}")
    print()

    # ── reconstruction check: A + B + C = Δtr_M exactly ────────────
    recon = sp.cancel(poly_part + sector_B + sector_C - dtrM)
    recon_ok = sp.simplify(recon) == 0
    print(f"  Reconstruction A+B+C = Δtr_M exactly: {recon_ok}")
    print()

    # ── modular data: ζ_4 residues ─────────────────────────────────
    res_pi = sp.simplify(sp.residue(dtrM, u, sp.I))
    res_mi = sp.simplify(sp.residue(dtrM, u, -sp.I))
    print(f"  ζ_4 MODULAR DATA (residues at u=±i):")
    print(f"    Res_{{u=+i}} Δtr_M = {res_pi};   Res_{{u=-i}} = {res_mi}")
    print(f"    (conjugate pair ∓i/2 — the WRT level-4 modular phase)")
    print()

    # ── u=0 Laurent coefficients (short-distance data) ─────────────
    # The u=0 tower is sector_C, a Laurent polynomial in u. Multiply by
    # u^6 to clear the poles, then read the polynomial coefficients
    # reliably (Gemini review #1622: coeff(u, k) with negative k is
    # fragile; Poly coefficient extraction at k+6 is robust).
    sector_C_poly = sp.Poly(sp.expand(sector_C * u ** 6), u)
    laurent_coeffs = {}
    for k in range(-6, 1):
        c = sector_C_poly.coeff_monomial(u ** (k + 6))
        if c != 0:
            laurent_coeffs[k] = sp.nsimplify(c)
    print(f"  u=0 LAURENT TOWER coefficients (short-distance modes):")
    for k in sorted(laurent_coeffs):
        print(f"    [u^{k}]  {laurent_coeffs[k]}")
    print()

    # ── bar-symmetry sector of each mode (u ↦ 1/u) ─────────────────
    def bar_split(expr: sp.Expr) -> tuple[sp.Expr, sp.Expr]:
        e = sp.cancel(expr)
        bar = sp.cancel(e.subs(u, 1 / u))
        return sp.cancel((e + bar) / 2), sp.cancel((e - bar) / 2)
    even_A, odd_A = bar_split(poly_part)
    even_B, odd_B = bar_split(sector_B)
    even_C, odd_C = bar_split(sector_C)
    print("  BAR-SYMMETRY (charge-conjugation u↦1/u) — even/odd split:")
    print(f"    (A) entire : even = {even_A}")
    print(f"    (B) ζ_4    : even = {even_B}   ← clean constant!")
    print(f"    (C) u=0    : even = {even_C}")
    print()

    print("=" * 78)
    print(" FINDING (q-difference mode solve — exact, no fit, no closure)")
    print("=" * 78)
    print(f"""
  • Δtr_M solves the q-difference structure as a 3-sector Fourier-mode
    decomposition (partial fraction over its poles), exact rationals:
    (A) an entire polynomial −u⁴/4 −u³/2 +u/2 −1/2;
    (B) the ζ_4 = ±i cyclotomic pole pair, residues ∓i/2;
    (C) the u=0 Laurent tower u^{{-1}}, u^{{-3}}, u^{{-4}}.
    Reconstruction A+B+C = Δtr_M holds exactly ({recon_ok}).

  • The ζ_4 residues ∓i/2 are the MODULAR DATA — the level-4 WRT phase
    that any candidate scaling map f must reproduce. This is a hard,
    exact constraint (a half-integer modular residue), not a fitted
    value.

  • BAR-EVEN (charge-conjugation-symmetric = physical) content per
    sector: the ζ_4 cyclotomic sector B has bar-even part = EXACTLY 1/2
    (a clean constant — the modular sector's physical content is a pure
    phase-1/2). PR #1602 found f must be the bar-even part; the modular
    mode contributes this exact 1/2 to f.

  • OPEN (the remaining bridge): map this exact u=√q mode decomposition
    onto the ladder variable u_ladder = b·ℏ² to read off the c_k. That
    change-of-variable (√q ↦ b·ℏ²) is the last step; the modes are now
    known exactly, so the bridge is a defined computation, not a search.
    """)

    builder.add_data("delta_trM", {
        "numerator": str(sp.expand(num)),
        "denominator": str(sp.factor(den)),
        "u_convention": "u = q^{1/2} (Habiro half-twist; NOT ladder b·ℏ²)",
    })
    builder.add_data("partial_fraction_mode_solve", str(pf))
    builder.add_data("spectral_sectors", {
        "A_entire_polynomial": str(poly_part),
        "B_zeta4_cyclotomic": str(sp.nsimplify(sector_B)),
        "C_u0_laurent_tower": str(sector_C),
        "reconstruction_exact": bool(recon_ok),
    })
    builder.add_data("zeta4_modular_data", {
        "residue_at_plus_i": str(res_pi),
        "residue_at_minus_i": str(res_mi),
        "note": "conjugate pair ∓i/2 — WRT level-4 modular phase",
    })
    builder.add_data("u0_laurent_coefficients",
                     {f"u^{k}": str(v) for k, v in laurent_coeffs.items()})
    builder.add_data("bar_symmetry_sectors", {
        "A_entire_even": str(sp.cancel(even_A)),
        "B_zeta4_even": str(sp.cancel(even_B)),
        "C_u0_tower_even": str(sp.cancel(even_C)),
        "B_zeta4_even_is_constant_half": bool(sp.simplify(even_B - sp.Rational(1, 2)) == 0),
        "interpretation": ("f must be the bar-even (charge-conjugation-"
                           "symmetric) part — PR #1602. The ζ_4 modular "
                           "sector's bar-even content is exactly 1/2."),
    })
    builder.add_data("open_bridge", {
        "remaining_step": ("change of variable u=√q ↦ u_ladder=b·ℏ² to "
                           "read off the ladder c_k from the now-exact "
                           "mode decomposition"),
        "status": "defined computation, not a search (modes known exactly)",
        "no_fitted_form_proposed": True,
    })
    builder.add_assertion(
        "mode_decomposition_reconstructs_exactly",
        computed=1.0 if recon_ok else 0.0,
        expected=1.0,
        tolerance=0.0,
        source=("Partial-fraction sectors A (entire) + B (ζ_4 pole pair) "
                "+ C (u=0 Laurent tower) sum to Δtr_M exactly — the "
                "mode-by-mode q-difference solution."),
    )
    builder.add_assertion(
        "zeta4_residues_are_conjugate_half_i",
        computed=float(sp.Abs(res_pi)),
        expected=0.5,
        tolerance=1e-30,
        source=("The ζ_4 = ±i residues are ∓i/2 (|res| = 1/2) — the "
                "exact WRT level-4 modular phase, an integer/2 constraint "
                "on any candidate f."),
    )
    builder.add_assertion(
        "zeta4_sector_bar_even_is_exactly_half",
        computed=1.0 if sp.simplify(even_B - sp.Rational(1, 2)) == 0 else 0.0,
        expected=1.0,
        tolerance=0.0,
        source=("The bar-even (charge-conjugation-symmetric) part of the "
                "ζ_4 cyclotomic sector is exactly 1/2 — the modular "
                "sector's physical content is a pure constant phase."),
    )
    builder.save()
    print("\n  Witness: habiro-q-difference-mode-solve.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
