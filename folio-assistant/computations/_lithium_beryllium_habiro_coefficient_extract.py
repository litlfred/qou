#!/usr/bin/env python3
"""_lithium_beryllium_habiro_coefficient_extract.py — Phase 5q
⁵Li / ⁶Li / ⁷Li / ⁷Be Habiro coefficients via the canonical closed form.

Extends PR #1618's ³He / ⁴He extraction to A=5,6,7 nuclei. The same
Phase 5q closed-form pipeline applies, with the appropriate
canonical-interface-kinds for each (Z, N):

  ⁵Li (Z=3, N=2): kinds = [+, +, +, -]   → z³(z-h)
  ⁶Li (Z=3, N=3): kinds = [+, +, +, -, -]   → z³(z-h)²
  ⁷Li (Z=3, N=4): kinds = [+, +, +, -, -, -]   → z³(z-h)³
  ⁷Be (Z=4, N=3): kinds = [+, +, +, +, -, -]   → z⁴(z-h)²

(per `canonical_interface_kinds` under chi_lambda_braid convention,
production default; verified by direct call in the build prologue.)

CLOSED FORMS:

    tr_M(⁵Li, q) = τ_p(q)³ · τ_n(q)² · z(q)³ · (z(q) - h(q))
    tr_M(⁶Li, q) = τ_p(q)³ · τ_n(q)³ · z(q)³ · (z(q) - h(q))²
    tr_M(⁷Li, q) = τ_p(q)³ · τ_n(q)⁴ · z(q)³ · (z(q) - h(q))³
    tr_M(⁷Be, q) = τ_p(q)⁴ · τ_n(q)³ · z(q)⁴ · (z(q) - h(q))²

where
    z(q) = 1 / (q^{1/2} + q^{-1/2})
    h(q) = q − q^{-1}

TWO MOTIVATIONS:

1. **More data for Habiro recursion** — extending from M=20 (⁴He) to
   M=28+ (⁷Li/⁷Be) gives more empirical Δa_m at higher m for testing
   the Q_β Habiro element ansatz.

2. **Mirror-pair test for Φ_1·Φ_2** — PR #1579 prediction: the (n−p)
   isospin-doublet Habiro element factors as `Φ_1·Φ_2 · …`, so the
   ⁷Be − ⁷Li mirror difference should carry the same `(u²−1)` =
   Φ_1·Φ_2 cyclotomic prefactor. **Falsifiable.**

APPROACH (symbolic-first):
  1. Read τ_p(q), τ_n(q) **as symbolic rationals in q** from the
     existing `habiro-coefficients-atomic.witness.json`.
  2. Multiply by the per-atom z/h power product per the closed forms
     above (and verified at runtime against `canonical_interface_kinds`).
  3. Convert to u-polynomial via `to_u_polynomial` (q = u²).
  4. Run `cyclotomic_expansion` to extract a_m coefficients.
  5. Verify reconstruction is exact + numerical match at q₀.
  6. **Mirror-pair test**: form Δa_m(⁷Be − ⁷Li); reconstruct
     `Σ_m Δa_m · (u;u)_m`; factor over ℤ[u]; check for the
     Φ_1·Φ_2 = (u²-1) prefactor.

OUTPUTS:
  - habiro-coefficients-lithium-5.witness.json
  - habiro-coefficients-lithium-6.witness.json
  - habiro-coefficients-lithium-7.witness.json
  - habiro-coefficients-beryllium-7.witness.json

Per CLAUDE.md long-compute discipline:
    python3 -u _lithium_beryllium_habiro_coefficient_extract.py 2>&1 \
        | tee /tmp/A567_habiro.log

Ref: prop:full-pole-structure-mass-trace
Ref: prop:constit-factor-tau-M-proton-identity
Ref: closed_form_tau_M.py (canonical closed-form module)
Ref: habiro_coefficients_atomic.py (cyclotomic expansion engine)
Ref: _helium_habiro_coefficient_extract.py (template — PR #1618)
"""
from __future__ import annotations

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

# Reuse the canonical extraction primitives.
from habiro_coefficients_atomic import (  # noqa: E402
    to_u_polynomial,
    cyclotomic_expansion,
    reconstruct,
)
from closed_form_tau_M import canonical_interface_kinds  # noqa: E402
from q_parameter import Q as _Q_CANONICAL  # noqa: E402


def _markov_z_q(q: sp.Symbol) -> sp.Expr:
    """z(q) = 1 / (q^{1/2} + q^{-1/2}) as a symbolic expression in q."""
    return 1 / (sp.sqrt(q) + 1 / sp.sqrt(q))


def _hecke_h_q(q: sp.Symbol) -> sp.Expr:
    """h(q) = q − q^{-1}."""
    return q - 1 / q


def _load_p_n_symbolic(habiro_path: Path, q: sp.Symbol):
    """Return (tau_p_in_q, tau_n_in_q) parsed from the existing witness."""
    data = json.loads(habiro_path.read_text())
    p_str = data["results"]["p (proton, A=1)"]["tr_M_in_q"]
    n_str = data["results"]["n (neutron, A=1)"]["tr_M_in_q"]
    tau_p = sp.sympify(p_str, locals={"q": q})
    tau_n = sp.sympify(n_str, locals={"q": q})
    return tau_p, tau_n


def _interface_product_symbolic(Z: int, N: int, q: sp.Symbol) -> sp.Expr:
    """Build the symbolic per-interface product matching
    `canonical_interface_kinds(Z, N)` under chi_lambda_braid.

    + → z   ; − → z − h   ; (no averaged here under chi_lambda_braid)
    """
    z = _markov_z_q(q)
    h = _hecke_h_q(q)
    kinds = canonical_interface_kinds(Z, N)
    expr = sp.Integer(1)
    for kind in kinds:
        if kind == "positive":
            expr = expr * z
        elif kind == "negative":
            expr = expr * (z - h)
        elif kind == "averaged":
            expr = expr * (z - h / 2)
        else:
            raise ValueError(f"Unknown interface kind {kind!r}")
    return expr


def _build_closed_form(Z: int, N: int, tau_p, tau_n, q):
    """tr_M(𝓑_K) = τ_p^Z · τ_n^N · Π interface_factor(kind, q)."""
    return tau_p ** Z * tau_n ** N * _interface_product_symbolic(Z, N, q)


def analyse_atom(label: str, Z: int, N: int, q,
                  tau_p, tau_n, q0_mp,
                  max_m: int = 64) -> dict:
    """Extract Habiro coefficients for the given atom."""
    t0 = time.perf_counter()
    print(f"\n── {label} (Z={Z}, N={N}, A={Z+N}) ──")
    kinds = canonical_interface_kinds(Z, N)
    print(f"  canonical_interface_kinds = {kinds}")

    tr_M_q = _build_closed_form(Z, N, tau_p, tau_n, q)
    print(f"  tr_M closed-form built (free symbols: {tr_M_q.free_symbols})")
    print(f"    elapsed: {time.perf_counter() - t0:.2f} s")

    tr_M_q = sp.together(tr_M_q)
    print(f"  → together-reduced; chars = {len(str(tr_M_q))}")
    print(f"    elapsed: {time.perf_counter() - t0:.2f} s")

    u = sp.Symbol('u', positive=True, real=True)
    p_u, shift, denom = to_u_polynomial(tr_M_q, q, u)
    deg_p = int(sp.Poly(p_u, u).degree()) if p_u != 0 else 0
    print(f"  → p(u) := u^{shift} · denom · tr_M(u²)")
    print(f"     deg p(u) = {deg_p}")
    print(f"     denom (in u) = {denom}")
    print(f"    elapsed: {time.perf_counter() - t0:.2f} s")

    coeffs = cyclotomic_expansion(p_u, u, max_m=max_m)
    print(f"  Habiro coefficients (in u = q^{{1/2}}):")
    for entry in coeffs:
        flag = "✓" if entry["integral"] else "✗"
        a_repr = entry["a_m"]
        if len(a_repr) > 120:
            a_repr = a_repr[:117] + "..."
        print(f"    a_{entry['m']}(u) = {a_repr}    "
              f"deg = {entry['deg_a_m']}, integral: {flag}")
    print(f"    elapsed: {time.perf_counter() - t0:.2f} s")

    recon = reconstruct(coeffs, u)
    diff = sp.expand(recon - p_u)
    recon_matches = (diff == 0)
    if recon_matches:
        print(f"  ✓ reconstruction matches  Σ a_m·(u;u)_m  =  p(u)")
    else:
        print(f"  ✗ reconstruction error:  diff has length {len(str(diff))} chars")
    print(f"    elapsed: {time.perf_counter() - t0:.2f} s")

    # Numerical check at q₀ via mpmath (50 dps).
    mp.mp.dps = 50
    q0 = q0_mp
    u0 = mp.sqrt(q0)
    tr_M_at_q0 = float(mp.mpf(str(sp.N(tr_M_q.subs(q, sp.Rational(str(q0))), 30))))
    p_in_u_at_u0_mpf = mp.mpf(str(sp.N(p_u.subs(u, sp.Rational(str(u0))), 30)))
    denom_expr = sp.sympify(denom, locals={"u": u})
    denom_at_u0_mpf = mp.mpf(str(sp.N(denom_expr.subs(u, sp.Rational(str(u0))), 30)))
    u0_shift = u0 ** shift if shift else mp.mpf(1)
    tr_M_via_u = float(p_in_u_at_u0_mpf / (u0_shift * denom_at_u0_mpf))
    rel_err = (abs(tr_M_at_q0 - tr_M_via_u) / abs(tr_M_at_q0)
               if tr_M_at_q0 != 0 else 0.0)

    print(f"  tr_M({label}) @ q_0 = {tr_M_at_q0:+.12e}")
    print(f"     via u-poly:        {tr_M_via_u:+.12e}")
    print(f"     rel diff:          {rel_err:.3e}")
    print(f"    elapsed: {time.perf_counter() - t0:.2f} s")

    return {
        "Z": Z, "N": N, "A": Z + N,
        "interface_kinds": list(kinds),
        "include_inter": True,
        "tr_M_in_q": str(tr_M_q),
        "shift": int(shift),
        "denom_in_u": denom,
        "p_in_u": str(p_u),
        "deg_p_u": deg_p,
        "habiro_coefficients": coeffs,
        "all_integral": all(c["integral"] for c in coeffs),
        "reconstruction_matches": recon_matches,
        "tr_M_at_q0": tr_M_at_q0,
        "tr_M_at_q0_via_u_poly": tr_M_via_u,
        "tr_M_at_q0_rel_err": rel_err,
    }


def _write_witness(path: Path, key: str, body: dict, q0_float: float,
                   description: str, reference_blocks: list[str]) -> None:
    """Write witness in atomic-witness-compatible format."""
    witness = {
        "computation": f"habiro-coefficients-{key}",
        "description": description,
        "reference_blocks": reference_blocks,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0": q0_float,
            "engine": "sympy Poly + sequential cyclotomic division "
                      "(via closed_form_tau_M closed form)",
            "pn_convention": "chi_lambda_braid (production default)",
            "source": "habiro-coefficients-atomic.witness.json (τ_p, τ_n)",
        },
        # Parent design script reads `habiro_coefficients` flat.
        "habiro_coefficients": body["habiro_coefficients"],
        "Z": body["Z"],
        "N": body["N"],
        "A": body["A"],
        "interface_kinds": body["interface_kinds"],
        "include_inter": body["include_inter"],
        "tr_M_in_q": body["tr_M_in_q"],
        "shift": body["shift"],
        "denom_in_u": body["denom_in_u"],
        "p_in_u": body["p_in_u"],
        "deg_p_u": body["deg_p_u"],
        "all_integral": body["all_integral"],
        "reconstruction_matches": body["reconstruction_matches"],
        "tr_M_at_q0": body["tr_M_at_q0"],
        "tr_M_at_q0_via_u_poly": body["tr_M_at_q0_via_u_poly"],
        "tr_M_at_q0_rel_err": body["tr_M_at_q0_rel_err"],
    }
    path.write_text(json.dumps(witness, indent=2, default=str))
    print(f"  Witness: {path}")


def _coeff_to_sympy(a_m_str: str, u: sp.Symbol) -> sp.Expr:
    """Convert a Habiro coefficient string back to a sympy Expr in u."""
    return sp.sympify(a_m_str, locals={"u": u})


def mirror_pair_test(li7: dict, be7: dict, u: sp.Symbol) -> dict:
    """Form Δa_m(⁷Be − ⁷Li); reconstruct Σ_m Δa_m · (u;u)_m;
    factor over ℤ[u]; check the Φ_1·Φ_2 = (u²-1) prefactor.

    The two atoms must share the same Habiro extraction window;
    coefficients beyond either's terminating m are zero.
    """
    print("\n── Mirror-pair test: ⁷Be − ⁷Li ──")
    print("  Building Δa_m sequence and reconstructing the difference …")

    coeffs_li = li7["habiro_coefficients"]
    coeffs_be = be7["habiro_coefficients"]
    by_m_li = {entry["m"]: entry["a_m"] for entry in coeffs_li}
    by_m_be = {entry["m"]: entry["a_m"] for entry in coeffs_be}
    m_max = max(
        max(by_m_li.keys()) if by_m_li else -1,
        max(by_m_be.keys()) if by_m_be else -1,
    )

    delta_data = []
    delta_coeffs_for_recon = []
    zero_str = "0"
    for m in range(m_max + 1):
        a_li_str = by_m_li.get(m, zero_str)
        a_be_str = by_m_be.get(m, zero_str)
        a_li = _coeff_to_sympy(a_li_str, u)
        a_be = _coeff_to_sympy(a_be_str, u)
        delta = sp.expand(a_be - a_li)
        delta_data.append({
            "m": m,
            "a_m_li7": a_li_str,
            "a_m_be7": a_be_str,
            "delta_a_m": str(delta),
            "delta_is_zero": (delta == 0),
        })
        delta_coeffs_for_recon.append({
            "m": m, "a_m": str(delta), "integral": True, "deg_a_m": 0,
        })

    diff_expr = reconstruct(delta_coeffs_for_recon, u)
    diff_expr = sp.expand(diff_expr)
    print(f"  Σ_m Δa_m · (u;u)_m  has {len(str(diff_expr))} chars")
    if diff_expr == 0:
        print("  WARNING: difference is identically zero — mirrors coincide")
        return {
            "delta_a_m": delta_data,
            "diff_expr": "0",
            "factored": "0",
            "phi_1_phi_2_prefactor": False,
            "factor_orders": [],
            "factor_string": "0",
        }

    # Factor the difference (over ℚ; cyclotomics factor naturally).
    factored = sp.factor(diff_expr)
    factored_str = str(factored)
    if len(factored_str) > 1500:
        factored_str_short = factored_str[:1500] + "..."
    else:
        factored_str_short = factored_str
    print(f"  factored form (truncated): {factored_str_short}")

    # Check for the Φ_1·Φ_2 = u² − 1 prefactor.
    # Equivalently check (u-1) and (u+1) both divide the difference.
    has_u_minus_1 = sp.div(diff_expr, u - 1, u)[1] == 0
    has_u_plus_1 = sp.div(diff_expr, u + 1, u)[1] == 0

    # Compute the multiplicities of (u-1), (u+1), and (u²-1) = Φ_1·Φ_2.
    def _multiplicity(expr, factor):
        m = 0
        residue = expr
        while True:
            quo, rem = sp.div(sp.expand(residue), factor, u)
            if rem != 0:
                break
            residue = quo
            m += 1
        return m

    mult_u_minus_1 = _multiplicity(diff_expr, u - 1) if has_u_minus_1 else 0
    mult_u_plus_1 = _multiplicity(diff_expr, u + 1) if has_u_plus_1 else 0
    mult_phi_1_phi_2 = min(mult_u_minus_1, mult_u_plus_1)

    print(f"  (u-1) multiplicity = {mult_u_minus_1}   (Φ_1)")
    print(f"  (u+1) multiplicity = {mult_u_plus_1}   (Φ_2)")
    print(f"  → Φ_1·Φ_2 = (u²-1) prefactor multiplicity = {mult_phi_1_phi_2}")
    print(f"  → PR #1579 prediction (mirror Φ_1·Φ_2 prefactor): "
          f"{'CONFIRMED' if mult_phi_1_phi_2 >= 1 else 'REFUTED'}")

    return {
        "delta_a_m": delta_data,
        "diff_expr_len": len(str(diff_expr)),
        "factored": factored_str_short,
        "phi_1_multiplicity": mult_u_minus_1,
        "phi_2_multiplicity": mult_u_plus_1,
        "phi_1_phi_2_prefactor": mult_phi_1_phi_2 >= 1,
        "phi_1_phi_2_multiplicity": mult_phi_1_phi_2,
    }


def main() -> int:
    t_overall = time.perf_counter()
    print("=" * 80)
    print("HABIRO COEFFICIENTS — ⁵Li / ⁶Li / ⁷Li / ⁷Be (Phase 5q closed-form)")
    print("=" * 80)

    q0_float = float(_Q_CANONICAL)
    q0_mp = mp.mpf(str(_Q_CANONICAL))
    print(f"q_0 = {q0_float:.16f}")

    habiro_path = HERE / "habiro-coefficients-atomic.witness.json"
    if not habiro_path.exists():
        print(f"  FATAL: {habiro_path} not found")
        return 2

    q = sp.Symbol('q', positive=True, real=True)
    print("  Loading symbolic τ_p, τ_n from atomic witness …")
    tau_p, tau_n = _load_p_n_symbolic(habiro_path, q)
    print(f"     τ_p chars = {len(str(tau_p))}")
    print(f"     τ_n chars = {len(str(tau_n))}")
    print(f"     elapsed: {time.perf_counter() - t_overall:.2f} s")

    plan: list[tuple[str, int, int, int]] = [
        ("⁵Li (lithium-5, A=5)", 3, 2, 80),
        ("⁶Li (lithium-6, A=6)", 3, 3, 96),
        ("⁷Li (lithium-7, A=7)", 3, 4, 112),
        ("⁷Be (beryllium-7, A=7)", 4, 3, 112),
    ]

    results: dict[str, dict] = {}
    for label, Z, N, max_m in plan:
        try:
            results[(Z, N)] = analyse_atom(
                label, Z, N, q, tau_p, tau_n, q0_mp, max_m=max_m,
            )
        except Exception as exc:
            print(f"  {label}: ERROR {type(exc).__name__}: {exc}")
            import traceback
            traceback.print_exc()
            results[(Z, N)] = {"error": f"{type(exc).__name__}: {exc}"}
        print(f"\n>>> elapsed after {label}: "
              f"{time.perf_counter() - t_overall:.2f} s")

    reference_blocks = [
        "def:habiro-ring",
        "prop:full-pole-structure-mass-trace",
        "prop:constit-factor-tau-M-proton-identity",
        "prop:interface-knot-markov-z",
        "thm:knot-mass-formula-unified",
    ]

    out_meta = [
        ((3, 2), "lithium-5", "habiro-coefficients-lithium-5.witness.json",
         "tr_M(⁵Li, q) = τ_p³·τ_n²·z³·(z−h) via Phase 5q closed form."),
        ((3, 3), "lithium-6", "habiro-coefficients-lithium-6.witness.json",
         "tr_M(⁶Li, q) = τ_p³·τ_n³·z³·(z−h)² via Phase 5q closed form."),
        ((3, 4), "lithium-7", "habiro-coefficients-lithium-7.witness.json",
         "tr_M(⁷Li, q) = τ_p³·τ_n⁴·z³·(z−h)³ via Phase 5q closed form."),
        ((4, 3), "beryllium-7", "habiro-coefficients-beryllium-7.witness.json",
         "tr_M(⁷Be, q) = τ_p⁴·τ_n³·z⁴·(z−h)² via Phase 5q closed form."),
    ]

    for key_zn, slug, fname, short_desc in out_meta:
        r = results.get(key_zn, {})
        if "error" in r:
            continue
        _write_witness(
            HERE / fname, slug, r, q0_float,
            description=(
                f"Habiro / cyclotomic expansion tr_M(A={key_zn[0]+key_zn[1]}, q) "
                f"= Σ_m a_m·(u;u)_m (u = q^{{1/2}}) via the Phase 5q closed "
                f"form: {short_desc} Extends the helium-3/helium-4 extraction "
                f"(PR #1618) to higher A; provides additional Δa_m data points "
                f"for Q_β Habiro element fitting and feeds the ⁷Be−⁷Li mirror "
                f"test (PR #1579 Φ_1·Φ_2 falsifiable prediction)."
            ),
            reference_blocks=reference_blocks,
        )

    # Mirror-pair test
    mirror_result = None
    li7 = results.get((3, 4))
    be7 = results.get((4, 3))
    if li7 and be7 and "error" not in li7 and "error" not in be7:
        u = sp.Symbol('u', positive=True, real=True)
        try:
            mirror_result = mirror_pair_test(li7, be7, u)
        except Exception as exc:
            print(f"  mirror-pair test: ERROR {type(exc).__name__}: {exc}")
            import traceback
            traceback.print_exc()
            mirror_result = {"error": f"{type(exc).__name__}: {exc}"}
        # Write mirror witness alongside the per-atom witnesses.
        mirror_witness_path = HERE / "habiro-mirror-pair-li7-be7.witness.json"
        mirror_witness = {
            "computation": "habiro-mirror-pair-li7-be7",
            "description": (
                "Mirror-pair test: ⁷Be − ⁷Li Habiro coefficient difference. "
                "PR #1579 predicts the (n-p) isospin-doublet mirror Habiro "
                "element factors as Φ_1·Φ_2·(…) where Φ_1·Φ_2 = u²−1. This "
                "witness records Δa_m, the reconstructed difference, its "
                "factorization, and the Φ_1, Φ_2 multiplicities."
            ),
            "reference_blocks": reference_blocks + [
                "PR #1579 (Habiro element factorization)",
                "PR #1642 (Q_β Wenzl-Habiro keystone)",
            ],
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "parameters": {
                "q_0": q0_float,
                "engine": "sympy.factor + sequential cyclotomic division "
                          "diff (via _lithium_beryllium_habiro_coefficient_extract)",
                "pn_convention": "chi_lambda_braid (production default)",
            },
            **(mirror_result or {}),
        }
        mirror_witness_path.write_text(
            json.dumps(mirror_witness, indent=2, default=str))
        print(f"  Mirror witness: {mirror_witness_path}")

    # ─── Summary ────────────────────────────────────────────────
    print("\n── Summary ──")
    for key_zn, r in results.items():
        Z, N = key_zn
        name = {(3, 2): '⁵Li', (3, 3): '⁶Li',
                (3, 4): '⁷Li', (4, 3): '⁷Be'}[key_zn]
        if "error" in r:
            print(f"  {name}: ERROR {r['error']}")
            continue
        print(f"  {name}: deg p(u) = {r['deg_p_u']:>3}, "
              f"#Habiro coeffs = {len(r['habiro_coefficients']):>2}, "
              f"all integral: {r['all_integral']}, "
              f"reconstruction: {r['reconstruction_matches']}, "
              f"rel_err @ q_0: {r.get('tr_M_at_q0_rel_err', 'n/a'):.2e}")
    if mirror_result is not None and "error" not in mirror_result:
        verdict = ("CONFIRMED"
                   if mirror_result.get("phi_1_phi_2_prefactor") else "REFUTED")
        print(f"\n  MIRROR (⁷Be−⁷Li) → PR #1579 Φ_1·Φ_2 prefactor: {verdict}")
        print(f"    multiplicity Φ_1 = {mirror_result.get('phi_1_multiplicity')}"
              f", Φ_2 = {mirror_result.get('phi_2_multiplicity')}")

    total = time.perf_counter() - t_overall
    print(f"\n  total elapsed: {total:.1f} s")
    any_err = any("error" in r for r in results.values())
    return 0 if not any_err else 1


if __name__ == "__main__":
    sys.exit(main())
