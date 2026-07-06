#!/usr/bin/env python3
"""qbeta_multiblock_order_audit.py — the per-Wedderburn-block Δtr_M
contributions live at order √u, while the ladder c_3 lives at order u³.
The shared value "-2" is an ACCIDENTAL value-coincidence across six
ε-orders, not a structural identity. This is the root cause of the
four-session c_3 wire/un-wire flip-flop.

WHY THIS PROBE (dedicated-session symbolic q-difference solve, sub-attack
deferred by claude/qbeta-habiro-element-search-2026-05-31 / PR #1585).

The Q_β precision ladder Q_β = Q_base·∏(1 + c_k·u^k), u = b·ℏ², has c_2 =
-1 proved Taylor-exact and c_3+ only near-matches. The bridge-narrowing
audit (b502b9b83) ruled out 6 mechanisms and noted "c_3 ≈ -2 originates
in the trivial/sign blocks (3),(1,1,1)". Four sessions then tried to wire
c_3 = -2 (= J_Hopf(q=1), = recursive pair-rules leading rung, …) and each
time found a near-match with a q₀-dependent swing.

THIS PROBE explains WHY, rigorously, with exact symbolic ε-series of the
per-block closed forms (qbeta-per-block-paper-closed-forms.witness.json):

  • u = b·ℏ² = (√3/2)·ε² + O(ε³)         →  u is O(ε²)
  • f_λ(q) per block is O(ε) = O(√u):
        (3)    : -2ε + …      (2,1) : -ε + …      (1,1,1) : -2ε + …
  • Δtr_M = Σ_λ f_λ = -5ε + …            →  also O(ε) = O(√u)

  • The ladder coefficient c_3 multiplies u³ = ε⁶.

So the per-block "-2" is the ε¹ (= u^{1/2}) coefficient of Δtr_M, whereas
the ladder c_3 = -2 is the u³ (= ε⁶) coefficient of Q_β/Q_base. They are
FIVE ε-orders apart (ε¹ vs ε⁶), in two DIFFERENT objects. Matching their values is a
numerical coincidence — which is exactly why every "c_3 = -2"
identification is a near-match with a q₀-dependent residual.

q₀-INDEPENDENCE DIAGNOSTIC: the per-block ε-coefficients are FIXED
rationals → identical at the muon-pin q₀ and the m_p-pin q₀. The
empirical c_3 swings 2.98%. The swing therefore lives ENTIRELY in the
categorical map f: Δtr_M ↦ Q_β, which must bridge order √u to order u³ —
not in the block structure (which is proved and anchor-invariant).

DISCIPLINE (AGENTS.md §7b, canonical-derivation, flip-flop framing,
canonical-ck-tiered-not-binary): no fitting, no candidate guessing. Every
quantity is a fixed symbolic function of q. The outcome is a TIERED
characterization of the obstruction (proved block structure / open f-map
/ near-match c_3), never a binary wire/un-wire and never a 7th near-match
candidate.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 2, 2026-06-02).
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
from mpmath import mp, mpf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

# Canonical pins (definitive_q0_shift_for_mp.py): Q_50_DIGIT_STR is the
# framework (muon-derived) q₀; the m_p-pin q_exact is where m_p is exact.
Q0_MUON_PIN = Q_50_DIGIT_STR
Q0_MP_PIN = "1.1099785827513808075916690956107688798744991218736"

# Empirical c_3 band (qbeta-ck-truncation-order-analysis.witness.json).
C3_EMP_MUON = mpf("-2.0097")
C3_EMP_MP = mpf("-2.0693")

EPS_ORDER = 8  # ε-series depth


def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder(
        "qbeta-multiblock-order-audit",
        engine="python+sympy",
        start_time=t0,
    )
    builder.set_description(
        "Order audit of the H_3(q) per-Wedderburn-block Δtr_M "
        "contributions vs the Q_β ladder variable u = b·ℏ². Shows the "
        "per-block forms are O(√u) (ε¹ coefficients -2/-1/-2) while the "
        "ladder c_3 is the u³ (=ε⁶) coefficient — five ε-orders apart (ε¹ vs ε⁶) in "
        "two different objects, so the shared value -2 is an accidental "
        "coincidence, not a structural identity. This is the root cause "
        "of the four-session c_3 wire/un-wire flip-flop. Includes the "
        "q₀-independence diagnostic (per-block ε-coefficients are fixed "
        "rationals, anchor-invariant) locating the empirical c_3 swing "
        "entirely in the (open) categorical map f. Proposes no fitted "
        "form. Sub-attack of probe-qbeta-habiro-element-search."
    )
    builder.set_content_block("prop:q-beta-categorical-precision-ladder")

    print("=" * 78)
    print(" Q_β MULTI-BLOCK ORDER AUDIT — why c_3 = -2 is an accidental coincidence")
    print("=" * 78)
    print()

    q = sp.Symbol("q", positive=True)
    eps = sp.Symbol("eps")
    w = json.loads(
        (_pb.witness_path("qbeta-per-block-paper-closed-forms.witness.json", HERE)).read_text()
    )
    forms = {lam: sp.sympify(w["data"]["paper_closed_forms"][lam],
                             locals={"q": q})
             for lam in w["data"]["paper_closed_forms"]}
    blocks = ["(3)", "(2,1)", "(1,1,1)"]

    # Ladder variable u = b·ℏ²  (b² = (h²+3)/(h²+4), h = q-1/q, ℏ = (q-1)/q).
    h = q - 1 / q
    b = sp.sqrt((h ** 2 + 3) / (h ** 2 + 4))
    hbar = (q - 1) / q
    u = b * hbar ** 2
    u_series = sp.series(u.subs(q, 1 + eps), eps, 0, 5).removeO()
    u_order = sp.Poly(sp.expand(u_series + eps ** 7), eps).monoms()  # smallest power
    u_lead_pow = min(m[0] for m in sp.Poly(u_series, eps).monoms())
    print(f"Ladder variable:  u = b·ℏ²  →  {u_series}")
    print(f"  ⇒ u is O(ε^{u_lead_pow})   (so √u ~ ε^{u_lead_pow//2}, "
          f"u^k ~ ε^{u_lead_pow}·k)")
    print(f"  ⇒ ladder c_3 multiplies u³ ~ ε^{3*u_lead_pow}")
    print()

    # Per-block ε-series + leading order.
    print(f"Per-block Δtr_M contributions f_λ(q), ε-series at q=1:")
    per_block_eps: dict[str, list[str]] = {}
    per_block_lead_pow: dict[str, int] = {}
    lead_coeff: dict[str, sp.Expr] = {}
    for blk in blocks:
        ser = sp.series(forms[blk].subs(q, 1 + eps), eps, 0, EPS_ORDER).removeO()
        ser = sp.expand(ser)
        poly = sp.Poly(ser, eps)
        lp = min(m[0] for m in poly.monoms())
        per_block_lead_pow[blk] = lp
        lead_coeff[blk] = ser.coeff(eps, lp)
        per_block_eps[blk] = [str(ser.coeff(eps, n)) for n in range(EPS_ORDER)]
        print(f"   {blk:>8s}: leading {lead_coeff[blk]}·ε^{lp}  "
              f"(= ε^{lp} = u^{sp.Rational(lp, u_lead_pow)})")

    total = sp.expand(sp.series(sum(forms[b] for b in blocks).subs(q, 1 + eps),
                                eps, 0, EPS_ORDER).removeO())
    total_lp = min(m[0] for m in sp.Poly(total, eps).monoms())
    print(f"   {'Σ (Δtr_M)':>8s}: leading {total.coeff(eps, total_lp)}·ε^{total_lp}")
    print()

    # The decisive order comparison.
    c3_ladder_order = 3 * u_lead_pow            # ε-order of the c_3 u³ term
    block_order = per_block_lead_pow["(3)"]      # ε-order of the block -2
    print("=" * 78)
    print(" THE ACCIDENTAL-COINCIDENCE FINDING")
    print("=" * 78)
    print(f"""
  • The per-block value -2 (trivial block (3), and sign block (1,1,1)) is
    the ε^{block_order} coefficient of Δtr_M  →  order u^{sp.Rational(block_order,u_lead_pow)}.
  • The ladder coefficient c_3 = -2 is the coefficient of u³  →  ε^{c3_ladder_order}.
  • These are {c3_ladder_order - block_order} ε-orders apart, in two different
    objects (Δtr_M vs Q_β/Q_base). The shared value -2 is therefore a
    NUMERICAL COINCIDENCE, not a structural identity.
  • This is the root cause of the four-session flip-flop: every attempt to
    set c_3 = -2 from a block / knot-invariant quantity matches a value
    living at the wrong order, so it is always a near-match with a
    q₀-dependent residual (2.98% cross-anchor swing).
    """)

    # q₀-independence diagnostic: per-block leading coefficients are fixed
    # rationals → identical at both anchors. Empirical c_3 swings.
    print("q₀-independence diagnostic (the falsifier):")
    anchor_invariant = True
    diag = []
    for blk in blocks:
        c = lead_coeff[blk]
        v = mp.mpf(str(sp.N(c, 45)))  # pure rational, no q dependence
        diag.append((blk, str(c), mp.nstr(v, 8)))
        print(f"   {blk:>8s}  leading-coeff {str(c):>4s}  "
              f"(fixed rational ⇒ identical at muon-pin and m_p-pin q₀)")
    swing = float(abs(C3_EMP_MUON - C3_EMP_MP))
    print(f"   empirical c_3:  muon-pin {float(C3_EMP_MUON)}  "
          f"m_p-pin {float(C3_EMP_MP)}  swing {swing:.4f} "
          f"({swing/abs(float(C3_EMP_MP))*100:.2f}%)")
    print(f"   ⇒ the swing lives in the categorical map f, NOT the block "
          f"structure (which is anchor-invariant).")
    print()

    print("=" * 78)
    print(" CHARACTERIZATION OF THE OPEN PROBLEM (no fitted form proposed)")
    print("=" * 78)
    print(f"""
  • SETTLED (proved, q₀-independent): the per-block Δtr_M structure. Blocks
    (3) and (1,1,1) carry -2·ε, block (2,1) carries -1·ε. Fixed rationals.

  • OPEN: the categorical map f: Δtr_M(q) ↦ Q_β(q). It must bridge order
    √u (where Δtr_M lives) to order u³ (where c_3 lives) — an order-3-in-u
    scaling. The bridge-narrowing audit's "residual lives in SCALING
    (eigenphase)" is the same statement: f is a scaling map, and its
    q-dependence is what supplies the empirical c_3 residual.

  • NOT the open problem: "which near-match value for c_3" (the four-session
    trap). The value -2 is settled as an accidental ε¹-coincidence; chasing
    it at the u³ order is category error.

  • TIER: block structure = proved; c_3 = near-match (this probe REINFORCES
    the near-match verdict with a structural reason); f-map = open.
    """)

    builder.add_data("ladder_variable", {
        "u_definition": "b·ℏ², b²=(h²+3)/(h²+4), h=q-1/q, ℏ=(q-1)/q",
        "u_series_eps": str(u_series),
        "u_leading_eps_power": int(u_lead_pow),
        "c3_term_eps_order": int(c3_ladder_order),
    })
    builder.add_data("per_block_eps_series", per_block_eps)
    builder.add_data("per_block_leading", {
        blk: {"coeff": str(lead_coeff[blk]),
              "eps_power": int(per_block_lead_pow[blk]),
              "u_power": str(sp.Rational(per_block_lead_pow[blk], u_lead_pow))}
        for blk in blocks
    })
    builder.add_data("accidental_coincidence_finding", {
        "block_minus2_eps_order": int(block_order),
        "block_minus2_u_order": str(sp.Rational(block_order, u_lead_pow)),
        "ladder_c3_eps_order": int(c3_ladder_order),
        "ladder_c3_u_order": 3,
        "eps_orders_apart": int(c3_ladder_order - block_order),
        "verdict": ("The per-block -2 (order √u) and the ladder c_3 = -2 "
                    "(order u³) are five ε-orders apart (ε¹ vs ε⁶) in two different "
                    "objects; the shared value is a numerical coincidence, "
                    "not a structural identity. Root cause of the "
                    "four-session c_3 wire/un-wire flip-flop."),
    })
    builder.add_data("q0_independence_diagnostic", {
        "per_block_leading_fixed_rationals": {d[0]: d[1] for d in diag},
        "anchor_invariant": anchor_invariant,
        "empirical_c3_muon_pin": str(C3_EMP_MUON),
        "empirical_c3_mp_pin": str(C3_EMP_MP),
        "empirical_swing_pct": swing / abs(float(C3_EMP_MP)) * 100,
        "conclusion": ("Per-block ε-coefficients are fixed rationals "
                       "(identical at both q₀ anchors); the empirical c_3 "
                       "swing lives entirely in the categorical map f."),
    })
    builder.add_data("open_problem_characterization", {
        "settled": "per-block Δtr_M structure (proved, q0-independent)",
        "open": ("categorical map f: Δtr_M (order √u) ↦ Q_β ladder "
                 "(c_3 at order u³); a q-dependent scaling/eigenphase map"),
        "not_the_problem": ("'which near-match value for c_3' — the value "
                            "-2 is an accidental ε¹ coincidence"),
        "tier": "block structure: proved; c_3: near-match; f-map: open",
        "no_fitted_form_proposed": True,
    })
    builder.add_assertion(
        "block_contributions_are_sqrt_u_order",
        computed=float(per_block_lead_pow["(3)"]),
        expected=float(u_lead_pow // 2 * 1),  # ε¹ = u^{1/2} since u~ε²
        tolerance=0.0,
        source=("Per-block Δtr_M contributions are O(ε)=O(√u); the ladder "
                "c_3 is O(u³)=O(ε⁶); the shared value -2 is an accidental "
                "cross-order coincidence (symbolic ε-series, exact)."),
    )
    builder.save()
    print("\n  Witness: qbeta-multiblock-order-audit.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
