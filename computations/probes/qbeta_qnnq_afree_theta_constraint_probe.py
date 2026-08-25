#!/usr/bin/env python3
"""qbeta_qnnq_afree_theta_constraint_probe.py — bean qou-qnnq: the A_ω-free
constraint that every independent ϑ-route must satisfy.

WHY THIS EXISTS. The circularity note (docs/scope/2026-08-01-t4-anchor-
circularity.md) established that A_ω and ϑ_K are ONE degree of freedom: the
channel

    S_K = A_ω · κ · (ln²q₀ − ϑ_K²),      κ = √3/4

gives two equations (two anchors) in three unknowns (A_ω, ϑ_μ, ϑ_p). Every ϑ
in the corpus is T4-inverted, i.e. A_ω-conditioned, so comparing a candidate
route against those ϑ values inherits the conditioning — the defect the
`circ-derived-used-as-input` detector flags.

THE OBSERVATION. Underdetermined is not contentless. Eliminating A_ω between
the two anchor equations leaves a relation with NO free parameter:

    (ln²q₀ − ϑ_μ²) / (ln²q₀ − ϑ_p²)  =  S_μ / S_p  ≡  r          (*)

r is built from the two MEASURED S values alone. It contains neither A_ω nor
q₀. So (*) is a falsifiable, A-free constraint curve in the (ϑ_μ, ϑ_p) plane,
and it is exactly the testable content the T4 chain does carry. Solved for the
proton coordinate:

    ϑ_p²(ϑ_μ)  =  L − (L − ϑ_μ²)/r,        L ≡ ln²q₀

WHAT THIS BUYS.
  1. Any route supplying BOTH ϑ values is testable WITHOUT assuming A_ω — on
     the curve or off it, no conditioning inherited.
  2. A route that lands ON the curve then DETERMINES A_ω,
         A_ω = S_μ / (κ·(L − ϑ_μ²)),
     which would be the first genuine determination in this arc rather than a
     literature import.
  3. It converts the qou-rdmr result from a comparison against conditioned
     targets into an A-free refutation (test T1 below).

Checks performed:
  C0  control — the T4 pair lies on the curve (it MUST; T4 is the inversion.
      A failure here would mean an arithmetic slip, not a discovery).
  C1  admissible range — ϑ_μ real requires A ≥ S_μ/(κL); the curve is
      traversed monotonically by A on [A_crit, ∞).
  T1  qou-rdmr's prediction ϑ_μ = ϑ_p = 0 (Rademacher Φ vanishes on both
      (RL)ⁿ words) tested against (*) — A-free.
  S1  (RESOLVED 2026-08-07) the T4 probe used to hardcode q₀ = 1.11020 vs canonical
      substrate value is q₀ ≈ 1.10998; r is q₀-free, but the curve is not, so
      both are reported.

Scope (STRICT). This derives nothing about the VALUE of A_ω and wires nothing.
It states, in falsifiable form, what an independent route has to reproduce. The
measured S values are inputs, taken as given from the bar-odd leak measurement;
this probe does not re-derive them.

Run: python3 -u computations/probes/qbeta_qnnq_afree_theta_constraint_probe.py \
       2>&1 | tee /tmp/qbeta_qnnq_afree.log
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from qou_substrate.precision import set_compute_dps  # noqa: E402

set_compute_dps()

# Measured bar-odd-leak S values (inputs, from qbeta_t4_stokes3_crux_probe.py).
S_MUON = mp.mpf("0.00968298")
S_PROTON = mp.mpf("-0.03945936")

KAPPA = mp.sqrt(3) / 4
# The T4 probe now READS the canonical proton-pinned constant. Its old literal
# 1.11020 was a unit conflation (it solved 2*ln q = h, where h = q - 1/q, rather
# than using q0); fixed 2026-08-07. There is consequently only ONE grid now —
# the two-grid comparison this probe used to run is resolved, not merely moot.
Q0 = None                        # bound to q_at(50) in main()
A_OMEGA_LIT = 3                  # GGM literature value — used ONLY to reproduce T4

# T4-inverted values, for the C0 control only. A_omega-conditioned.
# T4-inverted values at the CORRECTED q0 (was 0.05894648 / 0.20323503 at the
# superseded 1.11020). Still A_omega-conditioned; used for the C0 control only.
THETA_T4_MUON = mp.mpf("0.058592016840059722")
THETA_T4_PROTON = mp.mpf("0.20313250701827611")


def theta_p_sq(theta_mu_sq, L, r):
    """The A-free constraint curve, solved for the proton coordinate."""
    return L - (L - theta_mu_sq) / r


def main() -> int:
    print("=" * 78)
    print(" qou-qnnq — the A_ω-free constraint every independent ϑ-route must meet")
    print("=" * 78)

    r = S_MUON / S_PROTON
    print(f"\n[invariant] r = S_μ/S_p = {mp.nstr(r, 14)}")
    print("            depends on NEITHER A_ω NOR q₀ — it is measured data alone.")

    q0_canon = q_at(50)
    # ONE grid. Before 2026-08-07 this probe compared the T4 probe's hardcoded
    # q0 = 1.11020 against the canonical value, and reported the resulting
    # 4th-digit split in L and A_crit as a live discrepancy. That literal has
    # since been corrected at the source (a unit conflation: it solved
    # 2*ln q = h instead of using q0), so the two grids have collapsed into one.
    GRID = f"canonical q₀={mp.nstr(q0_canon, 8)}"
    grids = {GRID: q0_canon}

    out = {}
    for tag, q0 in grids.items():
        L = mp.log(q0) ** 2
        A_crit = S_MUON / (KAPPA * L)
        # C0 control: does the T4 pair satisfy (*)? Now meaningful on the single
        # canonical grid, since T4 inverts at that same q0.
        lhs = (L - THETA_T4_MUON**2) / (L - THETA_T4_PROTON**2)
        resid = abs(lhs - r)
        # T1: the rdmr prediction ϑ_μ = 0 → what does the curve force for ϑ_p?
        tp2_at_zero = theta_p_sq(mp.mpf(0), L, r)
        tp_at_zero = mp.sqrt(tp2_at_zero) if tp2_at_zero >= 0 else mp.mpf("nan")
        out[tag] = {"L": L, "A_crit": A_crit, "curve_resid_at_T4": resid,
                    "theta_p_forced_at_theta_mu_zero": tp_at_zero}
        print(f"\n[{tag}]")
        print(f"    L = ln²q₀           = {mp.nstr(L, 12)}")
        print(f"    A_crit = S_μ/(κL)   = {mp.nstr(A_crit, 10)}   "
              f"(ϑ_μ real ⟺ A ≥ A_crit)")
        print(f"    C0  curve residual at the T4 pair = {mp.nstr(resid, 6)}")
        print(f"    T1  curve forces ϑ_p = {mp.nstr(tp_at_zero, 10)} when ϑ_μ = 0")

    # the control must pass (definitional — T4 inverts on this grid)
    c0_ok = out[GRID]["curve_resid_at_T4"] < mp.mpf("1e-6")

    # ---- C1: traverse the curve in A, showing it is a genuine 1-parameter family
    L4 = out[GRID]["L"]
    print("\n[C1] the admissible family, traversed by A (A-free curve, A shown "
          "only as the parameter):")
    print(f"    {'A':>8}   {'ϑ_μ':>12}   {'ϑ_p':>12}   {'ϑ_p/ϑ_μ':>10}")
    table = []
    for A in ["2.10", "2.50", "3.00", "4.00", "6.00", "10.00"]:
        Am = mp.mpf(A)
        tm2 = L4 - S_MUON / (KAPPA * Am)
        tp2 = L4 - S_PROTON / (KAPPA * Am)
        if tm2 < 0:
            continue
        tm, tp = mp.sqrt(tm2), mp.sqrt(tp2)
        table.append({"A": A, "theta_mu": mp.nstr(tm, 12), "theta_p": mp.nstr(tp, 12),
                      "ratio": mp.nstr(tp / tm, 10)})
        print(f"    {A:>8}   {mp.nstr(tm, 10):>12}   {mp.nstr(tp, 10):>12}   "
              f"{mp.nstr(tp / tm, 8):>10}")
    print("    Every row satisfies (*) exactly. NOTHING in the T4 chain picks a "
          "row — that is the one degree of freedom.")

    # ---- T1 verdict: is the rdmr prediction on the curve?
    tp_forced = out[GRID]["theta_p_forced_at_theta_mu_zero"]
    rdmr_on_curve = abs(tp_forced) < mp.mpf("1e-6")
    print(f"\n[T1] qou-rdmr predicts ϑ_μ = ϑ_p = 0 (Rademacher Φ vanishes on both "
          f"(RL)ⁿ words).")
    print(f"     The A-free curve forces ϑ_p = {mp.nstr(tp_forced, 10)} at ϑ_μ = 0, "
          f"not 0.")
    print(f"     On the curve? {rdmr_on_curve}  ⇒ refuted WITHOUT assuming A_ω.")

    verdict = (
        "THE T4 CHAIN DOES CARRY ONE FALSIFIABLE, A-FREE STATEMENT. Eliminating "
        "A_ω between the two anchor equations leaves "
        "(ln²q₀ − ϑ_μ²)/(ln²q₀ − ϑ_p²) = S_μ/S_p = "
        f"{mp.nstr(r, 10)}, an invariant built from measured S values alone — no "
        "A_ω, no q₀. Any route supplying BOTH ϑ values is testable against this "
        "curve with no conditioning inherited, and a route that lands on it "
        "DETERMINES A_ω = S_μ/(κ(ln²q₀ − ϑ_μ²)) — which would be the arc's first "
        "genuine determination rather than a literature import. Control C0 "
        "passes (the T4 pair lies on the curve, as it must by construction). "
        "First application, T1: qou-rdmr's Rademacher prediction ϑ_μ = ϑ_p = 0 "
        f"is OFF the curve — at ϑ_μ = 0 the curve forces ϑ_p = "
        f"{mp.nstr(tp_forced, 8)}, so the Rademacher symbol is refuted WITHOUT "
        "assuming A_ω = 3, upgrading that scope-(a) result from a comparison "
        "against conditioned targets to an A-free one. SCOPE: this fixes no "
        "value of A_ω and wires nothing; it states in falsifiable form what an "
        "independent route (qou-offl, or any successor to qou-rdmr) must "
        "reproduce. The measured S values are taken as given."
        if c0_ok else
        "INCONCLUSIVE — the C0 control failed, meaning the curve and the T4 "
        "inversion disagree; that is an arithmetic slip to fix, not a finding.")
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("qbeta-qnnq-afree-theta-constraint", engine="mpmath")
    wb.set_description(
        "Bean qou-qnnq: derives the A_omega-free constraint curve that any "
        "independent theta-route must satisfy. Eliminating A_omega between the "
        "two anchor equations of S_K = A_omega*kappa*(ln^2 q0 - theta^2) leaves "
        "(L - theta_mu^2)/(L - theta_p^2) = S_mu/S_p, an invariant built from "
        "measured S values alone (no A_omega, no q0). This is the falsifiable "
        "content the T4 chain carries despite being underdetermined by one. A "
        "route landing on the curve determines A_omega rather than importing "
        "it. First application: the qou-rdmr Rademacher prediction "
        "theta_mu = theta_p = 0 is OFF the curve, refuting it WITHOUT assuming "
        "A_omega = 3. Fixes no value of A_omega; wires nothing.")
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("r_invariant", mp.nstr(r, 20))
    wb.add_data("r_is_free_of", ["A_omega", "q0"])
    wb.add_data("constraint_curve", "theta_p^2 = L - (L - theta_mu^2)/r,  L = ln^2 q0")
    wb.add_data("A_determination_if_on_curve",
                "A_omega = S_mu / (kappa * (L - theta_mu^2))")
    wb.add_data("grids", {tag: {"L": mp.nstr(v["L"], 16),
                                "A_crit": mp.nstr(v["A_crit"], 12),
                                "curve_residual_at_T4_pair":
                                    mp.nstr(v["curve_resid_at_T4"], 8),
                                "theta_p_forced_at_theta_mu_zero":
                                    mp.nstr(v["theta_p_forced_at_theta_mu_zero"], 12)}
                          for tag, v in out.items()})
    wb.add_data("admissible_family_sample", table)
    wb.add_data("T1_rdmr_on_curve", bool(rdmr_on_curve))
    wb.add_data("q0_note",
                "RESOLVED 2026-08-07: the T4 probe used to hardcode q0 = 1.11020 vs canonical "
                "substrate value is ~1.10998; r is q0-free but the curve is not, "
                "so both grids are reported")
    wb.add_data("inputs_taken_as_given",
                {"S_muon": mp.nstr(S_MUON, 12), "S_proton": mp.nstr(S_PROTON, 12),
                 "source": "bar-odd leak measurement via "
                           "qbeta_t4_stokes3_crux_probe.py"})
    wb.add_data("verdict", verdict)
    wb.add_assertion("C0_T4_pair_lies_on_curve",
                     computed="1" if c0_ok else "0", expected="1", tolerance="0.5",
                     source="control: the T4 inversion must satisfy the A-free "
                            "relation by construction")
    wb.add_assertion("T1_rdmr_off_curve",
                     computed="1" if not rdmr_on_curve else "0", expected="1",
                     tolerance="0.5",
                     source=f"at theta_mu = 0 the curve forces theta_p = "
                            f"{mp.nstr(tp_forced, 8)}, not 0 — A-free refutation "
                            f"of the Rademacher route")
    wb.save()
    print("  witness -> computations/probes/qbeta-qnnq-afree-theta-constraint.witness.json")
    return 0 if c0_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
