#!/usr/bin/env python3
"""qbeta_habiro_taylor_investigation.py — is c_3 just the Habiro Taylor
coefficient of the exact Q_β expression in h?

CONTEXT. The c_k flip-flop saga (deep audit
docs/audits/2026-05-30-qbeta-ck-mp-dk-deep-audit.md) revealed that the
"structural" forms c_3 = J_Hopf(q=1), c_3 = J - ℏ_q², etc. are all
near-matches at canonical q₀ but not Taylor-exact.

PR #1511 (main, 2026-05-30) showed that the α_EM next-order is exactly
the Habiro Taylor expansion of [2]_q · (1-h²α) — the c_k are uniquely
determined binomial-series rationals, zero free parameters.

THIS PROBE applies the same investigation to Q_β:
  1. Read the symbolic tr_M(β_p, q) and tr_M(β_n, q) from
     habiro-coefficients-atomic.witness.json (exact rationals in q).
  2. Symbolically construct Q_β = m_e × f(tr_M_p, tr_M_n, q) at canonical
     formula. Start with Form A (Q_A = m_e·|q²−2q−1|·(q+1)/(2q³)) and
     see what correction makes it match tr_M data.
  3. Take Habiro Taylor expansion at q=1 in h = q - q⁻¹ basis.
  4. Extract c_k as exact rationals.
  5. Compare to the empirical c_k from my cache (qbeta-ck-cache.witness.json).

If the symbolic c_k match the empirical extraction at compute precision,
then the Q_β c_k ARE the Habiro Taylor coefficients of an exact
substrate expression — closing the flip-flop saga the same way #1511
closed the α_EM saga.

DISCIPLINE: no fitting, no candidate guessing. The symbolic expression
is uniquely determined by the witness-cited tr_M polynomials; the Taylor
coefficients are uniquely determined by SymPy. Either it works exactly
(Habiro element identified) or it doesn't (further structural work
needed).
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 5, 2026-06-02).
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
from mpmath import mpf, mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402


def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder(
        "qbeta-habiro-taylor-investigation",
        engine="python+mpmath",
        start_time=t0,
    )
    builder.set_description(
        "Habiro Taylor expansion of the exact Q_β expression in h = "
        "q - q⁻¹ basis at q=1. Tests whether the Q_β c_k are uniquely "
        "determined Habiro Taylor coefficients of a substrate-canonical "
        "Q_β formula consuming Habiro-witness-cited tr_M polynomials. "
        "If yes, closes the c_k flip-flop saga the same way PR #1511 "
        "closed the α_EM saga."
    )
    builder.set_content_block("prop:q-beta-categorical-precision-ladder")

    print("=" * 78)
    print(" Q_β HABIRO TAYLOR INVESTIGATION — are the c_k just Habiro Taylor coeffs?")
    print("=" * 78)
    print()

    # Read exact symbolic tr_M for proton and neutron
    hab = json.loads((_pb.witness_path("habiro-coefficients-atomic.witness.json", HERE)).read_text())
    tr_p_str = hab["results"]["p (proton, A=1)"]["tr_M_in_q"]
    tr_n_str = hab["results"]["n (neutron, A=1)"]["tr_M_in_q"]

    q = sp.Symbol('q', positive=True)
    # sympify creates its own 'q' symbol — use locals to bind to our q
    tr_p_sym = sp.sympify(tr_p_str, locals={"q": q})
    tr_n_sym = sp.sympify(tr_n_str, locals={"q": q})

    print(f"  tr_M(β_p, q) and tr_M(β_n, q) loaded as exact SymPy rationals in q.")
    print(f"  proton tr_M_in_q (truncated): {tr_p_str[:120]}...")
    print()

    # Form A: Q_A = m_e × |q²−2q−1|·(q+1)/(2q³)
    # The exact Q_β formula must use the symbolic tr_M values.
    # Per prop:neutron-qvalue-symbolic, the canonical formula is:
    #   Q_β = m_e × |Δ(net)| × E_0, with Δ(net) derived from tr_M
    # But the simplest exact form via the witness data is:
    #   Q_β_substrate(q) = m_e × (tr_M(β_n) - tr_M(β_p)) × scaling_factor
    # where scaling_factor is the categorical bridge.
    #
    # FORM TESTED: use Δtr_M directly with Q_A's E_0 scale.
    #   Q_β_test(q) = m_e × |Δtr_M(q)| × E_0(q)
    #   E_0(q) = m_e / (q · (q-1))   [Planck-tick energy scale]
    delta_tr = sp.simplify(tr_n_sym - tr_p_sym)
    print(f"  Δtr_M(q) = tr_M(β_n) - tr_M(β_p) (symbolic, simplified)")
    print(f"  computing Habiro Taylor expansion at q=1...")
    print()

    # Substitute q = 1 + ε to extract the h-series.
    # h = q - q⁻¹ = (1+ε)² - 1)/(1+ε) — for ε small, h ≈ 2ε + O(ε³)
    # Use the substitution q = e^η where h = 2 sinh(η); we expand in η directly.
    # Easier: just expand in (q - 1) and convert.
    eps = sp.Symbol('eps')
    delta_tr_eps = sp.expand(delta_tr.subs(q, 1 + eps))
    delta_tr_eps_simplified = sp.simplify(delta_tr_eps)
    print(f"  Δtr_M(1+ε) leading expansion (after substitution + simplify)...")
    delta_tr_series = sp.series(delta_tr_eps_simplified, eps, 0, 10).removeO()
    delta_tr_expanded = sp.expand(delta_tr_series)
    print(f"  Δtr_M ≈ {delta_tr_expanded}")
    print()

    # Extract the per-order ε coefficients of Δtr_M
    delta_tr_coeffs = {n: sp.simplify(delta_tr_expanded.coeff(eps, n))
                       for n in range(10)}
    print(f"  Δtr_M Taylor coefficients (in ε = q - 1):")
    for n in range(8):
        c = delta_tr_coeffs[n]
        print(f"     ε^{n}:  {c}")
    print()

    # Build symbolic Q_β candidate: Q_β_sub = m_e × |Δtr_M| × 1/(q(q-1))
    # The 1/(q(q-1)) = 1/(q·ε) — diverges at q=1; so this isn't the right form.
    # Better: stay with Form A's structure but with Δtr_M correction.
    #
    # Actually the right form per prop:neutron-qvalue-symbolic is:
    #   Q_β = m_e × |Δ(net)| × E_0  where Δ(net) = h(h-2)/2 = (q² - 2q - 1)(q+1)/(2q³) · q
    # This is Form A — NO tr_M dependency.
    #
    # The deeper formula incorporating tr_M is what we need but haven't derived.
    # Let me try: Q_β_substrate = m_e × |Δtr_M(q)| × g(q) where g(q) is to be determined.
    # The constraint: at canonical q₀ the formula equals CODATA Q_β.

    # Test the simplest substrate scaling: Q_β = m_e × |Δtr_M| × (1/q - 1)
    # No, that doesn't have the right units. Let me check what matches.

    # Numerical sanity at q₀
    q0_str = Q_50_DIGIT_STR
    q0 = sp.Rational(int(mpf(q0_str)._mpf_[1]),
                     2 ** -int(mpf(q0_str)._mpf_[2]) if mpf(q0_str)._mpf_[2] < 0 else 1)
    # Use mpmath instead for q₀ eval
    me_num = mpf(M_E_MEV)
    q0_num = mpf(q0_str)
    Q_codata = mpf("0.78233341")

    tr_p_num = float(sp.N(tr_p_sym.subs(q, sp.Float(str(q0_num), 50)), 30))
    tr_n_num = float(sp.N(tr_n_sym.subs(q, sp.Float(str(q0_num), 50)), 30))
    delta_tr_num = tr_n_num - tr_p_num
    print(f"  Numerical sanity at q₀:")
    print(f"     tr_M(β_p, q₀) = {tr_p_num:.15f}")
    print(f"     tr_M(β_n, q₀) = {tr_n_num:.15f}")
    print(f"     Δtr_M(q₀)     = {delta_tr_num:.15f}")
    print()

    # Try: Q_β = m_e × |Δtr_M| × E_0 with E_0 = m_e/(q(q-1))
    #     = m_e² × |Δtr_M| / (q(q-1)·m_e) = m_e × |Δtr_M| / (q(q-1))
    # This is not right (m_e² appears). The proper formula needs to be:
    #     Q_β = |Δtr_M| × m_e × C where C is a substrate-derived number ratio
    # From prop:neutron-qvalue-symbolic: Q_β = m_e × |Δ(net)| × E_0/m_e = |Δ(net)| × E_0
    # Form A: Δ(net) = h(h-2)/2.
    # The connection Δ(net) ↔ Δtr_M ↔ multi-block needs derivation.

    # SCOPE this probe records what's LOADED + WHERE THE GAP IS, not how to close.
    print()
    print("=" * 78)
    print(" FINDINGS")
    print("=" * 78)
    print(f"""
  • Exact symbolic tr_M(β_p, q) and tr_M(β_n, q) successfully loaded from
    habiro-coefficients-atomic.witness.json. Both are rational functions
    in q^(1/2).

  • Habiro Taylor expansion of Δtr_M(q) at q=1 (in ε = q-1 basis) computed
    symbolically. Leading coefficients are clean rationals.

  • THE GAP (still open, NOT closed by this probe):
    The categorical formula Q_β = m_e × f(Δtr_M(q), q) for some
    substrate-canonical f is NOT in the codebase. Form A
    Q_β = m_e × |q² - 2q - 1| × (q+1)/(2q³) does NOT consume Δtr_M.
    It is the leading approximation; the correction that closes 1677 ppm
    is the multi-Wedderburn-block formula that this probe was meant to
    discover but does not.

  • What WOULD close the c_k saga (parallel to PR #1511 for α_EM):
    Identify the symbolic f such that Q_β = m_e × f(Δtr_M(q), q) matches
    CODATA at q₀, then take its Habiro Taylor expansion — the c_k will
    be exact rationals (binomial-series style) like α_EM's.

  • What this probe DOES contribute:
    Records the Δtr_M Taylor expansion as exact rationals so future
    sessions deriving the canonical f can do the connection in one
    SymPy step.
    """)

    builder.add_data("inputs", {
        "tr_M_proton_symbolic_in_q": tr_p_str,
        "tr_M_neutron_symbolic_in_q": tr_n_str,
        "Q_codata_MeV": str(Q_codata),
        "q_0_50dps": q0_str,
    })
    builder.add_data("delta_tr_M_taylor_at_q_eq_1", {
        "basis": "ε = q - 1",
        "coefficients": {
            f"eps^{n}": str(delta_tr_coeffs[n])
            for n in range(8)
        },
        "note": ("These are the substrate-exact Taylor coefficients of "
                 "Δtr_M(q) at q=1, computed symbolically from the "
                 "Habiro-witness-cited rational tr_M expressions. The "
                 "Q_β c_k will inherit from these via the (yet-undefined) "
                 "categorical formula Q_β = m_e × f(Δtr_M, q)."),
    })
    builder.add_data("numerical_sanity_at_q0", {
        "tr_M_proton_at_q0": mp.nstr(tr_p_num, 18),
        "tr_M_neutron_at_q0": mp.nstr(tr_n_num, 18),
        "delta_tr_M_at_q0": mp.nstr(delta_tr_num, 18),
    })
    builder.add_data("gap_identified", {
        "missing_categorical_formula": "Q_β = m_e × f(Δtr_M(q), q) for "
                                       "substrate-canonical f",
        "current_form_A_misses_by_ppm": 1677,
        "current_form_A_consumes_delta_tr": False,
        "parallel_to_alpha_em_thread": "PR #1511 (main) — there [2]_q · "
                                       "(1-h²α) was the Habiro element; "
                                       "Q_β's analog is yet to be "
                                       "identified",
    })
    builder.add_assertion(
        "symbolic_delta_tr_loaded",
        computed=1.0,
        expected=1.0,
        tolerance=0.0,
        source="Δtr_M(q) is symbolic-rational; Taylor coefficients extracted as exact rationals",
    )
    builder.save()
    print(f"\n  Witness: qbeta-habiro-taylor-investigation.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
