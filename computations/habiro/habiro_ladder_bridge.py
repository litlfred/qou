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

DISCIPLINE (AGENTS.md §7b, ck-tiered-not-binary): exact symbolic; no fit;
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

# NOTE: this module deliberately holds NO q₀ literal. The pin is read from the
# upstream witness at the evaluation site below; see the block comment there.


def q_pochhammer(U: sp.Symbol, m: int) -> sp.Expr:
    r = sp.Integer(1)
    for k in range(1, m + 1):
        r *= (1 - U ** k)
    return r


def habiro_trM(atom: dict, U: sp.Symbol) -> sp.Expr:
    # SYMBOL BINDING, fixed 2026-08-30 (bean qou-0ndb). This bound
    # `locals={"check_q": U}`, which was stale: since
    # `fix(qou-0ndb): serialize Habiro polynomials in ONE canonical symbol`
    # (2026-08-10) the upstream serialises in `u`, and it was regenerated in
    # `u` on 2026-08-26. So sympify mints a fresh Symbol('u'), the a_m/denom
    # never bind to `U`, and the expression comes out a {u, U} MIXTURE — the
    # exact silent failure habiro_coefficients_atomic.py:222-231 warns about.
    # `.subs(U, sqrt(q))` then left `u` symbolic and `float(dtrM_at_1)` raised
    # with "Cannot convert expression to float", so THIS PRODUCER COULD NOT RUN
    # AT ALL and its witness could not be regenerated. Reproduced directly
    # before fixing. Confirmed against the committed upstream, whose
    # `denom_in_u` reads `4*u**26 + 8*u**22 + 4*u**18` — serialised in `u`.
    D = sp.sympify(atom["denom_in_u"], locals={"u": U})
    total = sp.Integer(0)
    for c in atom["habiro_coefficients"]:
        total += sp.sympify(c["a_m"], locals={"u": U}) \
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

    wit = builder.add_upstream(_pb.witness_path("habiro-coefficients-atomic.witness.json", HERE))
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

    # ── numeric value at q₀ (sanity) ─────────────────────────────────
    # q₀ MIGRATED off pin A to the proton pin, 2026-08-30. VALUES MOVE, so the
    # witness must be regenerated (bean qou-jjge) — but see the BLOCKER at
    # `habiro_trM` first: this producer cannot currently run at all.
    #
    # Until now this read a hardcoded
    #     Q0_MP_PIN = "1.1099785955573347198997632204832250266562084087802"
    # under the label "m_p-pin". Measured, that literal is 11.5371 ppb from the
    # proton pin and 0.0769 ppb from the current muon pin C — label and value
    # disagreed. It is the value that is the artefact here: the constant was
    # named `Q0_MP_PIN` because when this probe was written
    # (docs/audits/2026-06-01-habiro-ladder-bridge.md) the corpus believed that
    # literal WAS the m_p pin — see 2026-06-21-q0-clusterA-migration-plan.md,
    # which calls it "the canonical proton anchor". 2026-06-24-q0-layer-
    # migration-scope.md then showed it reaches m_p only via the FITTED
    # habiro_ratio (1+46u⁴)(1+4u⁵)(1−29u⁶), and the owner ruling 2026-07-03
    # stripped that tower (q_parameter.py:33-44), after which the tower-free
    # proton solve is 1.1099785827513808…. The label kept its meaning; the
    # value did not follow.
    #
    # COMPETING PRECEDENT — considered, and a DIFFERENT SHAPE.
    # `probes/qbeta_habiro_cyclotomic_probe.py:270` and
    # `substrate/z2bn_tau_gauss_manin_sage_probe.py:88` carry this same literal
    # under a "proton" label and were resolved the other way on 2026-08-29 —
    # label corrected, value kept (bean qou-fd0e). Both keep it because there
    # the value has an independent job: the cyclotomic probe evaluates the MUON
    # arm of a deliberate proton↔muon residual (its own text reports the 2.88%
    # proton↔muon swing, and 2026-06-21-q0-clusterA-migration-plan.md had
    # already REVERTED that file from a mechanical sweep for exactly that
    # reason), and the z2bn probe takes q₀ from the 50-dps pinning witness, the
    # muon feed. That pass also did not rule on intent — qou-fd0e records it as
    # "the label is corrected, the intent is not ruled on".
    #
    # This file has neither: no second anchor, no cross-anchor comparison, no
    # read of the pinning witness, and exactly one upstream — habiro-
    # coefficients-atomic, which is manifest-declared `physical_proton` AND
    # carries the proton pin in its PAYLOAD (`parameters.q_0 =
    # 1.1099785827513808`), not merely in a `q0Anchor` stamp (a stamp on an
    # undeclared stem is only a runtime default — this stem IS declared, and
    # the payload is the real evidence either way). The nearest precedent is
    # one file over in this cluster on this same upstream:
    # `habiro_interpolate_cross_validator.py:143` (bean qou-0hnz, 2026-08-30)
    # dropped its own pin-A default for the same reason and now reads the pin
    # from the upstream payload, raising rather than guessing.
    #
    # DECIDING EVIDENCE is arithmetic, not a label. Δtr_M is built ENTIRELY
    # from that upstream's coefficients, so a "sanity" check is only sane at
    # the pin those coefficients were computed at. Against the upstream's own
    # recorded traces (n − p = −0.158016004341491285…):
    #     at the proton pin   |diff| = 1.3e-17  (agrees to its precision)
    #     at pin A            |diff| = 2.1e-8   (six orders worse)
    #
    # So the pin is taken from the upstream and never hardcoded: a resolved pin
    # cannot go stale, a literal can (qou-0hnz).
    _params = wit.get("parameters") or {}
    q0_payload = _params.get("q_0")
    if q0_payload is None:
        raise SystemExit(
            "habiro_ladder_bridge: habiro-coefficients-atomic carries no "
            "parameters.q_0. Refusing to fall back to a hardcoded pin from "
            "the other anchor layer (bean qou-0hnz).")
    q0_str = str(q0_payload)
    # The stamp is higher precision, but a stamp alone is not evidence — use it
    # only when the payload (which is) agrees with it.
    q0_stamp = wit.get("q0Value")
    if q0_stamp is not None:
        _payload, _stamp = mp.mpf(q0_str), mp.mpf(str(q0_stamp))
        if abs(_stamp - _payload) > mp.mpf("1e-15") * abs(_payload):
            raise SystemExit(
                f"habiro_ladder_bridge: upstream q0Value {q0_stamp!r} "
                f"disagrees with its own parameters.q_0 {q0_payload!r}. "
                "Refusing to pick one (bean qou-fd0e).")
        q0_str = str(q0_stamp)
    q0_anchor = wit.get("q0Anchor", "unstamped")
    dq_num = complex(sp.N(dq.subs(q, sp.Float(q0_str, 50)), 30)).real
    print(f"  Δtr_M(q₀) = {dq_num:.12f}  (numeric sanity at the upstream's "
          f"{q0_anchor} pin q₀)")
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
    # NO FLOAT64 (owner directive): assertion values pass as STRINGS, the
    # drained convention (qou-t0rf). WitnessBuilder.add_assertion coerces
    # with float() when evaluating `passed`, so exact-zero tolerance still
    # behaves identically; only the RECORDED value stays out of float64.
    builder.add_assertion(
        "delta_trM_vanishes_at_classical_point",
        computed=str(dtrM_at_1),
        expected="0",
        tolerance="0",
        source=("Δtr_M(q=1) = 0 exactly — proton & neutron Markov traces "
                "coincide at the classical point q=1 (the q-space form of "
                "the #1622 d=2 bar-mode vanishing)."),
    )
    builder.add_assertion(
        "delta_trM_is_sqrt_u_ladder_order",
        # DECIMAL string, not str(Rational): str(Rational(1,2)) is "1/2",
        # which add_assertion's float() coercion cannot parse — it records
        # passed=False on a ratio that is exactly right. The drained-
        # convention string must stay float()-parseable.
        computed=str(sp.N(sp.Rational(dtrM_lead, u_lad_lead), 20)),
        expected="0.5",
        tolerance="0",
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
