#!/usr/bin/env python3
"""habiro_ladder_bridge.py — the change-of-variable bridge from the
exact Habiro mode decomposition (u = √q = \check{q}, the spinor
rate) to the Q_β ladder variable (u_ladder = b·ℏ²), reading off
what the ladder c_k must satisfy.

WHY THIS PROBE (1ppQ-Q_β keystone — the final bridge step).

PR #1622 solved the q-difference structure of Δtr_M mode-by-mode (exact
partial fraction in u = √q). The one remaining open step is the change
of variable u = √q ↦ u_ladder = b·ℏ², to connect the now-exact modes to
the ladder coefficients c_k. This probe performs that bridge and reports
the (consistent) structural picture that emerges.

THE TWO VARIABLES (both expansions around q = 1):
  • Habiro  u        = q^{1/2}   → 1   as q→1  (u = 1 + ε/2 − …, ε = q−1)
  • Ladder  u_ladder = b·ℏ²      → 0   as q→1  (u_ladder = (√3/2)ε² − …)
So u_ladder is O(ε²) while the Habiro u is O(1); the two organise the
SAME function Δtr_M(q) around q=1 in different gradings.

THE CONSISTENT PICTURE (this probe verifies it end-to-end):
  1. Δtr_M(q=1) = 0 exactly — the proton/neutron traces coincide at the
     classical point (the d=2 bar-mode vanishing of PR #1622, in q-space).
  2. Δtr_M is O(ε¹) = O(√u_ladder) — the trace difference lives at order
     √u_ladder, exactly the per-block order of PR #1593's order audit.
  3. The ladder c_k multiply u_ladder^k (k≥2). So Δtr_M does NOT directly
     supply the c_k: a candidate scaling map f: Δtr_M ↦ Q_β must lift
     order √u_ladder to order u_ladder² (PR #1602's u¹-cancellation /
     bar-even constraint), then the c_k are read from f(Δtr_M).

This probe records Δtr_M(q) in closed form, both variable expansions, and
the order-matching that ties #1593 (order audit), #1602 (eigenphase ≠ f),
and #1622 (mode solve) into ONE consistent structural statement. It does
NOT fabricate a c_k value — the f-lift is still the open object; this
probe pins down exactly what f must do.

DISCIPLINE (CLAUDE.md §7b, ck-tiered-not-binary): exact symbolic; no fit;
no c_k value claimed; tiered. NOTE on u: Habiro u = q^{1/2} vs ladder
u_ladder = b·ℏ² (notation-collisions.md §u, PR #1622) — kept distinct.
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
import mpmath as mp  # noqa: E402
mp.mp.dps = 70

from witness_base import WitnessBuilder  # noqa: E402

Q0_MP_PIN = "1.1099785827513808075916690956107688798744991218736"


def q_pochhammer(U: sp.Symbol, m: int) -> sp.Expr:
    r = sp.Integer(1)
    for k in range(1, m + 1):
        r *= (1 - U ** k)
    return r


def habiro_trM(atom: dict, U: sp.Symbol) -> sp.Expr:
    D = sp.sympify(atom["denom_in_u"], locals={"check_q": U})
    total = sp.Integer(0)
    for c in atom["habiro_coefficients"]:
        total += sp.sympify(c["a_m"], locals={"check_q": U}) \
            * q_pochhammer(U, int(c["m"]))
    return sp.cancel(total / D)


def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder(
        "habiro-ladder-bridge",
        engine="python+sympy",
        start_time=t0,
    )
    builder.set_description(
        "Change-of-variable bridge from the exact Habiro mode "
        "decomposition (u = q^{1/2}) to the Q_β ladder variable "
        "u_ladder = b·ℏ². Records Δtr_M(q) in closed form, both variable "
        "expansions around q=1, and the order-matching that unifies the "
        "order audit (#1593: Δtr_M is O(√u_ladder)), eigenphase≠f (#1602: "
        "f must lift √u to u² / bar-even), and the mode solve (#1622) "
        "into one consistent structural statement: Δtr_M(1)=0 exactly, "
        "Δtr_M is O(√u_ladder), so the c_k come from the scaling map "
        "f(Δtr_M), not Δtr_M directly. Exact symbolic; no fitted c_k."
    )
    builder.set_content_block("prop:q-beta-categorical-precision-ladder")

    print("=" * 78)
    print(" HABIRO → LADDER BRIDGE — change of variable u=√q ↦ u_ladder=b·ℏ²")
    print("=" * 78)
    print()

    q = sp.Symbol("q", positive=True)
    eps = sp.Symbol("eps")
    U = sp.Symbol("U")  # Habiro u = √q

    wit = json.loads(
        (_pb.witness_path("habiro-coefficients-atomic.witness.json", HERE)).read_text())
    dU = sp.cancel(habiro_trM(wit["results"]["n (neutron, A=1)"], U)
                   - habiro_trM(wit["results"]["p (proton, A=1)"], U))
    # substitute U = √q → Δtr_M as a function of q
    dq = sp.simplify(dU.subs(U, sp.sqrt(q)))
    print(f"  Δtr_M(q) = {dq}")
    print()

    # the two variables
    hbar = (q - 1) / q
    b = sp.sqrt(q ** 4 + q ** 2 + 1) / (q ** 2 + 1)
    u_ladder = b * hbar ** 2
    u_habiro = sp.sqrt(q)

    u_hab_ser = sp.series(u_habiro.subs(q, 1 + eps), eps, 0, 4)
    u_lad_ser = sp.series(u_ladder.subs(q, 1 + eps), eps, 0, 4)
    dq_ser = sp.series(dq.subs(q, 1 + eps), eps, 0, 5)
    print("  VARIABLE EXPANSIONS around q = 1 (ε = q−1):")
    print(f"    Habiro  u = √q       = {u_hab_ser}")
    print(f"    Ladder  u_ladder=b·ℏ²= {u_lad_ser}")
    print(f"    Δtr_M(q)             = {dq_ser}")
    print()

    # the consistent picture. Use SymPy's leadterm for a robust leading
    # order (Gemini review #1622: the manual coeff loop is fragile).
    dtrM_at_1 = sp.limit(dq, q, 1)
    _, dtrM_lead_pow = dq.subs(q, 1 + eps).leadterm(eps)
    dtrM_lead = int(dtrM_lead_pow)
    u_lad_lead = 2  # u_ladder = O(ε²)
    print("  ORDER-MATCHING (the unifying statement):")
    print(f"    Δtr_M(q=1) = {dtrM_at_1}  (exact — p/n traces coincide "
          f"classically)")
    print(f"    Δtr_M leading order: ε^{dtrM_lead}  →  "
          f"u_ladder^{sp.Rational(dtrM_lead, u_lad_lead)} "
          f"(= √u_ladder, matching #1593 order audit)")
    print(f"    ladder c_k multiply u_ladder^k, k≥2")
    print(f"    ⇒ Δtr_M (order √u_ladder) does NOT directly supply c_k;")
    print(f"      the scaling map f must lift √u_ladder → u_ladder² "
          f"(#1602).")
    print()

    # numeric value at q0 (sanity)
    q0 = mp.mpf(Q0_MP_PIN)
    dq_num = complex(sp.N(dq.subs(q, sp.Float(str(q0), 50)), 30)).real
    print(f"  Δtr_M(q₀) = {dq_num:.12f}  (numeric sanity at m_p-pin q₀)")
    print()

    print("=" * 78)
    print(" FINDING (bridge — exact, consistent, no fabricated c_k)")
    print("=" * 78)
    print(f"""
  • Δtr_M(q) closed form bridges the Habiro modes (u=√q) to the ladder
    (u_ladder=b·ℏ²). Both are expansions of the SAME Δtr_M(q) around q=1,
    in different gradings (u=√q is O(1), u_ladder is O(ε²)).

  • CONSISTENT PICTURE (three prior probes unified):
    – Δtr_M(q=1) = 0 exactly (p/n coincide classically; = #1622's d=2
      bar-mode vanishing, in q-space).
    – Δtr_M is O(ε¹) = O(√u_ladder) — exactly #1593's order-audit result.
    – c_k multiply u_ladder^k (k≥2); so Δtr_M alone cannot supply the
      c_k. The scaling map f must lift order √u_ladder to u_ladder², the
      u¹-cancellation / bar-even constraint of #1602.

  • This pins f's job EXACTLY: a bar-even map lifting the O(√u_ladder)
    trace difference to the O(u_ladder²) ladder, reproducing the #1622
    modular data (ζ_4 residue ∓i/2, bar-even content 1/2). No c_k value
    is fabricated — f remains the open object, now fully constrained.
    """)

    builder.add_data("delta_trM_closed_form", {
        "in_q": str(dq),
        "value_at_q_eq_1": str(dtrM_at_1),
        "value_at_q0": mp.nstr(mp.mpf(str(dq_num)), 15),
    })
    builder.add_data("variable_expansions", {
        "u_habiro_sqrt_q": str(u_hab_ser),
        "u_ladder_b_hbar2": str(u_lad_ser),
        "delta_trM": str(dq_ser),
    })
    builder.add_data("order_matching", {
        "delta_trM_at_q1": str(dtrM_at_1),
        "delta_trM_leading_eps_order": int(dtrM_lead),
        "u_ladder_leading_eps_order": u_lad_lead,
        "delta_trM_in_u_ladder_order": str(sp.Rational(dtrM_lead, u_lad_lead)),
        "statement": ("Δtr_M is O(√u_ladder); c_k multiply u_ladder^k "
                      "(k≥2); the scaling map f lifts √u_ladder→u_ladder², "
                      "unifying #1593/#1602/#1622."),
    })
    builder.add_data("f_constraint", {
        "f_must": ("bar-even map lifting O(√u_ladder) Δtr_M to "
                   "O(u_ladder²) ladder, reproducing ζ_4 residue ∓i/2 "
                   "and bar-even content 1/2 (#1622)"),
        "status": "open object, now fully constrained",
        "no_fitted_form_proposed": True,
    })
    builder.add_assertion(
        "delta_trM_vanishes_at_classical_point",
        computed=float(dtrM_at_1),
        expected=0.0,
        tolerance=0.0,
        source=("Δtr_M(q=1) = 0 exactly — proton & neutron Markov traces "
                "coincide at the classical point q=1 (the q-space form of "
                "the #1622 d=2 bar-mode vanishing)."),
    )
    builder.add_assertion(
        "delta_trM_is_sqrt_u_ladder_order",
        computed=float(sp.Rational(dtrM_lead, u_lad_lead)),
        expected=0.5,
        tolerance=0.0,
        source=("Δtr_M leads at ε¹ while u_ladder is O(ε²), so Δtr_M is "
                "O(√u_ladder) — exactly the per-block order of the #1593 "
                "order audit. Confirms the c_k come from f(Δtr_M), not "
                "Δtr_M directly."),
    )
    builder.save()
    print("\n  Witness: habiro-ladder-bridge.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
