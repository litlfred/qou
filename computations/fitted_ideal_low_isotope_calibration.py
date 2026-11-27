#!/usr/bin/env python3
"""fitted_ideal_low_isotope_calibration.py
==========================================

**The fitted-ideal calibration layer** — the third of the three layers recorded
in [`docs/coordination/calibration-layers.md`](../docs/coordination/calibration-layers.md).

*** PAUSED — OWNER RULING 2026-08-26 ****************************************
The large fitted q0 variation means the MODEL IS NOT YET CORRECT ENOUGH for
this layer to mean anything: A TERM IS MISSING IN BINDING.

The fit demands m_e = 1.9455 MeV against CODATA 0.51100 (3.8x) and moves q
+3.26% off the substrate pin. Two calibration parameters travelling that far
are not exercising calibration freedom - they are ABSORBING MODEL ERROR into
calibration values, which is the signature a missing extensive term in B
produces. The held-out split says it again: light and heavy regimes want
moduli 3.4% apart, so no single three-point choice serves both.

What this does NOT retract: the measurements are correct as recorded and
remain useful as a DIAGNOSTIC - they bound what recalibration alone can buy,
and are independent evidence for the missing additive extensive term.

What it DOES mean: do NOT quote the fitted values as a calibration of the
framework, do not wire them anywhere, do not score any observable against
them. Do NOT open a follow-on that fits harder (more isotopes, more free
parameters, a widened objective) - that makes a mis-specified model fit
better without making it more correct.

Unblocking condition: the missing binding term, not more fitting. Once B
carries the super-pairwise additive extensive object, re-run this producer.
If the fitted calibration then lands near CODATA and the two regimes agree
on q, the layer becomes meaningful. That is a real test - the layer can
currently fail it.
*****************************************************************************

There are **exactly three calibration points in every layer**; the layers differ
only in how the three values are *chosen*:

  math ideal        the canonical triple CAL-1 m_e, CAL-2 P_skew^β, CAL-3 P_avg^π,
                    by definition.
  observational     the same three, taken as MEASURED (CODATA / PDG).
  fitted ideal      the same three, treated as FREE PARAMETERS and chosen to
                    minimise binding-energy error over the low isotopes
                    (²H, ³H, ³He, ⁴He, ⁶Li, ⁷Li, ⁷Be) against AME2020.

This producer computes the fitted-ideal layer and reports it beside the
observational one.

WHY IT IS WORTH COMPUTING
-------------------------
The observational ideal reproduces its three anchors *exactly by construction*,
so those three carry no information about model quality (the same tautology
AGENTS.md §"Precision goals" forbids scoring for m_e / m_p). The fitted ideal
spends the same three degrees of freedom on an OVER-DETERMINED objective —
3 parameters against 7 isotopes — so the residual that survives is a genuine,
falsifiable measure of model error, separated from calibration choice.

THIS IS A FIT AND IS LABELLED ONE
---------------------------------
Per AGENTS.md §"Axiomatization is NOT a Proof" and the Δ_λ anti-fit rule: the
values below are FITTED, not derived. They may be reported and compared. They
may NOT be wired to production as canonical, and nothing derived from them may
be presented as a parameter-free prediction. The canonical layer remains the
math ideal; the production numerical pin remains the proton experimental anchor
(owner directive 2026-08-07, re-affirmed 2026-08-15 R2). Neither is changed
here.

IDENTIFIABILITY — MEASURED, NOT ASSUMED
---------------------------------------
Low-isotope binding enters the chain as

    B(K) = Q_β(n) · ( tr_M(W_free) − tr_M(W_atom) )

(`binding_canonical.py`). Reading the three calibration DOF off that formula:

  CAL-1 (m_e)  — a pure multiplicative MeV scale on every B.  Identifiable
                 only through the overall normalisation.
  CAL-2 (P_skew^β)  — enters BOTH the MeV scale Q_β and the dimensionless trace
                 difference, non-linearly and differently per isotope.
                 Identifiable.
  CAL-3 (P_avg^π)  — DOES NOT APPEAR IN B AT ALL. The low-isotope binding
                 objective is FLAT in CAL-3.

So the fitted ideal has three calibration points but only **two identifiable
directions** under a pure low-isotope-binding objective. This producer fits the
two identifiable ones and reports CAL-3 as held at its observational value —
never as "fitted". A fitted CAL-3 quoted off a flat objective is meaningless.

PARAMETRISATION
---------------
The two identifiable directions are carried as the pair (Q_β, q), i.e. the CAL-2
proxy's MeV value and the substrate modulus. The implied CAL-1 follows by
inverting the CAL-2 relation

    Q_β = m_e · |q² − 2q − 1| · (q + 1) / (2 q³)

so the fit reports an implied m_e to compare against CODATA. Given q, the
optimal scale is analytic (the objective is quadratic in Q_β), so the search is
a 1-D bracket over q with the scale solved in closed form at each trial.

NO LAYER STRADDLE (the defect this producer was built to avoid)
---------------------------------------------------------------
`tr_m_wenzl_bridge_mpfr._load_y_lambda` selects a CACHED y_λ table by matching
q_str against the known anchors, and for an UNRECOGNISED q₀ "keeps the previous
default rather than guessing" — the proton table. Inside a fit loop every trial
q is unrecognised, so calling the bridge naively would pair proton-pinned y_λ
with χ_λ evaluated at the trial q: a systematic instance of the layer straddle
AGENTS.md documents (the μ₃ Fréchet incident, 11.54 ppb — and far worse here,
since the trial q ranges widely rather than sitting 11 ppb away).

This producer therefore takes χ_λ from the bridge's `return_breakdown` (χ
depends only on the word and q, never on the y table) and recombines it with
y_λ(q) computed at the SAME trial q from the live closed form
`schur_principal_mpmath.y_lambda_at_q0_mpmath`. Both factors are then at one q
by construction.

PRECISION
---------
mpmath end to end at 50 dps; no float64 in any arithmetic (AGENTS.md
§"PROBES ARE NOT EXEMPT"). `float()` appears only inside display f-strings.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401,E402
import json
import pathlib
import sys
import time

import mpmath as mp  # noqa: E402

from _precision import (  # noqa: E402
    set_compute_dps, fmt, str_at_true_precision,
)
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from hecke_core import (  # noqa: E402
    _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1,
)
from tr_m_wenzl_bridge_mpfr import tr_M_via_wenzl_bridge_mpfr  # noqa: E402
from schur_principal_mpmath import y_lambda_at_q0_mpmath  # noqa: E402
from closed_form_tau_M import closed_form_tau_M  # noqa: E402
from experimental_constants import Q_NEUTRON_MEV as _Q_BETA_N  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

set_compute_dps()
HERE = pathlib.Path(__file__).resolve().parent

# The isotope target sets. B_AME comes from the VENDORED AME2020 table via
# `ame_2020_binding_energies._binding_mev_exact` (exact Decimal), so the set is
# not limited to whatever the committed sweep witness happens to carry.
SWEEP = "low-isotopes-binding-sweep.witness.json"

# LOW — the owner-specified target set ("low isotopes like 2H, tritium etc").
# This is the set the fitted ideal is DEFINED against; it is what the fit sees.
ISOTOPES_LOW = [
    ("D", 1, 2), ("T", 1, 3), ("3He", 2, 3), ("4He", 2, 4),
    ("6Li", 3, 6), ("7Li", 3, 7), ("7Be", 4, 7),
]

# HELD-OUT — never shown to the fit. Used only to ask whether a calibration
# fitted on the light nuclei GENERALISES. A 3-point calibration that fits its
# own training set and then fails out-of-sample is diagnosing model shape, not
# calibration choice, and that distinction is the whole point of this layer.
ISOTOPES_HELDOUT = [
    ("9Be", 4, 9), ("10B", 5, 10), ("11B", 5, 11), ("12C", 6, 12),
    ("14N", 7, 14), ("16O", 8, 16), ("20Ne", 10, 20), ("24Mg", 12, 24),
    ("28Si", 14, 28), ("40Ca", 20, 40), ("56Fe", 26, 56),
]


def _nucleon_word(g0, g1):
    return [(c, d, 0) for c, d in g0] + [(c, d, 1) for c, d in g1]


_W_P = _nucleon_word(_PROTON_G0, _PROTON_G1)
_W_N = _nucleon_word(_NEUTRON_G0, _NEUTRON_G1)


def tau_H3_at(word, q: mp.mpf) -> mp.mpf:
    """tr_M^3(word) at an ARBITRARY q, with y_λ and χ_λ both at that q.

    See the module docstring, §NO LAYER STRADDLE: χ_λ comes from the bridge
    breakdown (independent of the y table) and y_λ from the live closed form at
    the same q. Never let `_load_y_lambda` choose a table here.
    """
    q_str = mp.nstr(q, mp.mp.dps, strip_zeros=False)
    bd = tr_M_via_wenzl_bridge_mpfr(word, 3, q_str, return_breakdown=True)
    y = y_lambda_at_q0_mpmath(3, q)
    total = mp.mpf(0)
    for entry in bd["by_partition"]:
        lam = tuple(entry["partition"])
        chi = mp.mpf(entry["chi_lambda"])
        total += y[lam] * chi
    return total


def q_beta_from_me(m_e: mp.mpf, q: mp.mpf) -> mp.mpf:
    """CAL-2 relation: Q_β = m_e·|q²−2q−1|·(q+1)/(2q³)."""
    return m_e * abs(q * q - 2 * q - 1) * (q + 1) / (2 * q ** 3)


def me_from_q_beta(q_beta: mp.mpf, q: mp.mpf) -> mp.mpf:
    """Invert the CAL-2 relation for the implied CAL-1."""
    return q_beta * 2 * q ** 3 / (abs(q * q - 2 * q - 1) * (q + 1))


def trace_deficit(Z: int, N: int, q: mp.mpf,
                  tau_p: mp.mpf, tau_n: mp.mpf) -> mp.mpf:
    """The dimensionless (tr_M(W_free) − tr_M(W_atom)) at q."""
    atom = closed_form_tau_M(Z, N, q, tau_p, tau_n)
    vac = tau_p ** Z * tau_n ** N
    return vac - atom


def deficits_at(q: mp.mpf, isotopes) -> dict:
    """Dimensionless trace deficit for every isotope at one q."""
    tau_p = tau_H3_at(_W_P, q)
    tau_n = tau_H3_at(_W_N, q)
    return {row["key"]: trace_deficit(row["Z"], row["N"], q, tau_p, tau_n)
            for row in isotopes}


def rel_rms(scale: mp.mpf, defs: dict, isotopes) -> mp.mpf:
    tot = mp.mpf(0)
    for row in isotopes:
        pred = scale * defs[row["key"]]
        rel = (pred - row["B_AME"]) / row["B_AME"]
        tot += rel ** 2
    return mp.sqrt(tot / len(isotopes))


def optimal_scale(defs: dict, isotopes) -> mp.mpf:
    """Closed-form minimiser of the relative-RMS objective in the scale.

    d/ds Σ ((s·d_i − m_i)/m_i)² = 0  ⇒  s = Σ(d_i/m_i) / Σ(d_i/m_i)².
    """
    num = mp.mpf(0)
    den = mp.mpf(0)
    for row in isotopes:
        r = defs[row["key"]] / row["B_AME"]
        num += r
        den += r * r
    if den == 0:
        raise ZeroDivisionError("degenerate objective: all trace deficits zero")
    return num / den


def objective(q: mp.mpf, isotopes) -> tuple:
    """Best achievable relative-RMS at this q (scale profiled out)."""
    defs = deficits_at(q, isotopes)
    s = optimal_scale(defs, isotopes)
    return rel_rms(s, defs, isotopes), s, defs


def golden_min(f, lo: mp.mpf, hi: mp.mpf, tol: mp.mpf, max_iter: int = 200):
    """Golden-section minimisation of a unimodal f on [lo, hi], all in mpf."""
    inv_phi = (mp.sqrt(5) - 1) / 2
    a, b = lo, hi
    c = b - inv_phi * (b - a)
    d = a + inv_phi * (b - a)
    fc, fd = f(c)[0], f(d)[0]
    it = 0
    while abs(b - a) > tol and it < max_iter:
        if fc < fd:
            b, d, fd = d, c, fc
            c = b - inv_phi * (b - a)
            fc = f(c)[0]
        else:
            a, c, fc = c, d, fd
            d = a + inv_phi * (b - a)
            fd = f(d)[0]
        it += 1
    return (a + b) / 2, it


def build_set(spec):
    """Isotope rows with exact AME2020 binding, as mpf."""
    from ame_2020_binding_energies import _binding_mev_exact
    out = []
    for name, Z, A in spec:
        out.append({
            "key": name, "atom": name, "Z": Z, "N": A - Z, "A": A,
            "B_AME": mp.mpf(str(_binding_mev_exact(Z, A))),
        })
    return out


def committed_sweep_refs():
    """B_pred from the committed sweep witness, keyed by atom (gate reference)."""
    d = json.loads((HERE / SWEEP).read_text())
    rows = d.get("witness", d).get("data", d.get("data", {}))["rows"]
    return {r["atom"]: mp.mpf(r["B_pred_canonical_MeV"]) for r in rows}


def main() -> int:
    t0 = time.monotonic()
    q0 = Q_MP
    qb_obs = mp.mpf(str(_Q_BETA_N))
    isotopes = build_set(ISOTOPES_LOW)
    heldout = build_set(ISOTOPES_HELDOUT)
    refs = committed_sweep_refs()

    # ── GATE: reproduce the committed B_pred at the observational point ──
    # This is the correctness gate for the whole evaluator. If the q-parametric
    # evaluator does not reproduce the committed witness at q₀, every fitted
    # number below would be a laundered artefact of a broken evaluator.
    defs0 = deficits_at(q0, isotopes)
    gate = []
    worst_gate = mp.mpf(0)
    for row in isotopes:
        pred = qb_obs * defs0[row["key"]]
        ref = refs[row["key"]]
        rel = (pred - ref) / ref
        if abs(rel) > abs(worst_gate):
            worst_gate = rel
        gate.append({"atom": row["atom"], "B_pred_recomputed": fmt(pred),
                     "B_pred_committed": fmt(ref), "rel_diff": fmt(rel)})
    GATE_TOL = mp.mpf("1e-6")
    gate_ok = abs(worst_gate) < GATE_TOL

    print(f"GATE  worst |rel diff| vs committed sweep = "
          f"{mp.nstr(abs(worst_gate), 6)}  (tol {mp.nstr(GATE_TOL, 3)})  "
          f"{'PASS' if gate_ok else 'FAIL'}")
    if not gate_ok:
        print("REFUSING to report a fit: the q-parametric evaluator does not "
              "reproduce the committed B_pred at q₀. Fitted numbers computed "
              "from a broken evaluator would be laundered. Fix the evaluator "
              "first.", file=sys.stderr)
        for g in gate:
            print(f"   {g['atom']:>5}  rel={g['rel_diff']}", file=sys.stderr)
        return 1

    # ── Layer 1: OBSERVATIONAL IDEAL (both CAL values measured) ──
    rms_obs = rel_rms(qb_obs, defs0, isotopes)

    # ── Layer 2: FITTED IDEAL, scale-only (CAL-2 modulus held at q₀) ──
    s_scale_only = optimal_scale(defs0, isotopes)
    rms_scale_only = rel_rms(s_scale_only, defs0, isotopes)

    # ── Layer 3: FITTED IDEAL, both identifiable directions (Q_β, q) ──
    # Bracket q well away from the anchor so the search is not seeded on it.
    LO, HI = mp.mpf("1.01"), mp.mpf("1.60")
    print(f"scanning q over [{mp.nstr(LO,4)}, {mp.nstr(HI,4)}] ...")
    # Coarse scan first: the objective need not be unimodal over a wide bracket,
    # so bracket the coarse minimum before the golden refinement.
    n_scan = 40
    best_q, best_val = None, None
    scan = []
    for i in range(n_scan + 1):
        qq = LO + (HI - LO) * mp.mpf(i) / n_scan
        try:
            val, _, _ = objective(qq, isotopes)
        except Exception as exc:                      # noqa: BLE001
            scan.append({"q": fmt(qq), "rms": None, "error": type(exc).__name__})
            continue
        scan.append({"q": fmt(qq), "rms": fmt(val)})
        if best_val is None or val < best_val:
            best_val, best_q = val, qq
        print(f"   q={mp.nstr(qq,8):>12}  rel-RMS={mp.nstr(val*100,6):>10}%")
    if best_q is None:
        print("no evaluable q in the bracket", file=sys.stderr)
        return 1

    step = (HI - LO) / n_scan
    q_fit, iters = golden_min(lambda x: objective(x, isotopes),
                              max(LO, best_q - step), min(HI, best_q + step),
                              mp.mpf("1e-25"))
    rms_fit, s_fit, defs_fit = objective(q_fit, isotopes)
    me_implied = me_from_q_beta(s_fit, q_fit)

    from experimental_constants import M_E_MEV as _M_E
    me_obs = mp.mpf(str(_M_E))

    # ── Held-out test: does a calibration fitted on the light nuclei
    #    GENERALISE?  The held-out set is never shown to the fit.
    #    This is the question a 3-point fit on 7 points can actually answer,
    #    and it separates "the calibration was badly chosen" from "the model's
    #    A-dependence is wrong".
    defs_ho_fit = deficits_at(q_fit, heldout)
    defs_ho_obs = deficits_at(q0, heldout)
    rms_ho_fit = rel_rms(s_fit, defs_ho_fit, heldout)
    rms_ho_obs = rel_rms(qb_obs, defs_ho_obs, heldout)

    # For reference only: the best a refit on the held-out set alone could do.
    # If in-sample fit and held-out refit want very different calibrations, no
    # single 3-point choice serves both, which is a statement about the model.
    rms_ho_refit, s_ho_refit, _ = objective(q_fit, heldout)
    q_ho_refit, _ = golden_min(lambda x: objective(x, heldout),
                               mp.mpf("1.01"), mp.mpf("1.60"), mp.mpf("1e-20"))
    rms_ho_best, s_ho_best, _ = objective(q_ho_refit, heldout)

    heldout_rows = []
    for row in heldout:
        pred = s_fit * defs_ho_fit[row["key"]]
        heldout_rows.append({
            "atom": row["atom"], "Z": row["Z"], "N": row["N"], "A": row["A"],
            "B_AME_MeV": fmt(row["B_AME"]),
            "B_fitted_on_low_MeV": fmt(pred),
            "rel_out_of_sample": fmt((pred - row["B_AME"]) / row["B_AME"]),
        })

    print()
    print("HELD-OUT (never seen by the fit) — calibration fitted on the low set:")
    print(f"{'atom':>5} {'A':>3} {'B_AME':>10} {'B_pred':>11} {'rel':>10}")
    for r in heldout_rows:
        print(f"{r['atom']:>5} {r['A']:>3} "
              f"{float(mp.mpf(r['B_AME_MeV'])):>10.4f} "
              f"{float(mp.mpf(r['B_fitted_on_low_MeV'])):>11.4f} "
              f"{float(mp.mpf(r['rel_out_of_sample']))*100:>9.2f}%")
    print(f"  held-out rel-RMS, observational calibration = "
          f"{mp.nstr(rms_ho_obs*100, 6)}%")
    print(f"  held-out rel-RMS, calibration fitted on low  = "
          f"{mp.nstr(rms_ho_fit*100, 6)}%")
    print(f"  held-out rel-RMS, refitted on held-out       = "
          f"{mp.nstr(rms_ho_best*100, 6)}%  (q={mp.nstr(q_ho_refit,12)})")

    rows_out = []
    for row in isotopes:
        pred = s_fit * defs_fit[row["key"]]
        rows_out.append({
            "atom": row["atom"], "Z": row["Z"], "N": row["N"], "A": row["A"],
            "B_AME_MeV": fmt(row["B_AME"]),
            "B_observational_MeV": fmt(qb_obs * defs0[row["key"]]),
            "rel_observational": fmt((qb_obs * defs0[row["key"]] - row["B_AME"])
                                     / row["B_AME"]),
            "B_fitted_MeV": fmt(pred),
            "rel_fitted": fmt((pred - row["B_AME"]) / row["B_AME"]),
        })

    print()
    print(f"{'atom':>5} {'A':>2} {'B_AME':>10} {'B_obs':>10} {'rel_obs':>9} "
          f"{'B_fit':>10} {'rel_fit':>9}")
    for r, row in zip(rows_out, isotopes):
        print(f"{r['atom']:>5} {r['A']:>2} "
              f"{float(row['B_AME']):>10.5f} "
              f"{float(mp.mpf(r['B_observational_MeV'])):>10.5f} "
              f"{float(mp.mpf(r['rel_observational']))*100:>8.2f}% "
              f"{float(mp.mpf(r['B_fitted_MeV'])):>10.5f} "
              f"{float(mp.mpf(r['rel_fitted']))*100:>8.2f}%")
    print()
    print(f"observational ideal        rel-RMS = {mp.nstr(rms_obs*100, 6)}%")
    print(f"fitted ideal (scale only)  rel-RMS = "
          f"{mp.nstr(rms_scale_only*100, 6)}%")
    print(f"fitted ideal (Q_beta, q)   rel-RMS = {mp.nstr(rms_fit*100, 6)}%")
    print(f"  q_fit    = {mp.nstr(q_fit, 20)}   (q0 = {mp.nstr(q0, 20)})")
    print(f"  Q_beta   = {mp.nstr(s_fit, 12)} MeV  "
          f"(observational {mp.nstr(qb_obs, 12)})")
    print(f"  implied m_e = {mp.nstr(me_implied, 12)} MeV  "
          f"(CODATA {mp.nstr(me_obs, 12)})")
    print(f"  CAL-3 (m_pi): NOT FITTED — objective is flat in it (see docstring)")

    wall = time.monotonic() - t0
    w = WitnessBuilder("fitted-ideal-low-isotope-calibration",
                       start_time=t0)
    w.set_description(
        "Fitted-ideal calibration layer: the three calibration points "
        "chosen to minimise low-isotope binding error vs AME2020, instead "
        "of taken from CODATA/PDG. FITTED, NOT DERIVED — must not be wired "
        "to production as canonical. CAL-3 is not identifiable from this "
        "objective and is held at its observational value.")
    w.add_data("gate_vs_committed_sweep", {
        "tolerance": fmt(GATE_TOL),
        "worst_rel_diff": fmt(worst_gate),
        "passed": gate_ok,
        "rows": gate,
        "note": ("The q-parametric evaluator must reproduce the committed "
                 "B_pred at q0 before any fitted number is reported."),
    })
    w.add_data("layers", {
        "observational_ideal": {
            # Q_β and m_e are CODATA-ORIGIN: they reach mpf from a 53-bit
            # source, so `fmt` at OUTPUT_DPS would emit the binary64 dyadic
            # tail and read as measured precision (the float64-padding
            # defect — caught here by the ratchet as NEW, claiming
            # 0.782333409309999949776... for a value that really carries
            # 0.78233340931). `str_at_true_precision` tests per value
            # whether the mpf holds only 53 bits and shortens exactly those.
            # The FITTED values below keep `fmt`: they are computed at full
            # working precision and shortening them would destroy real digits.
            # m_e keeps `fmt`: it is NOT exactly float64-representable, so the
            # helper falls through to `str()` at compute-dps and emits a
            # 70-digit noise tail — worse than fmt's clean trailing zeros at
            # OUTPUT_DPS. The helper applies per value, not per provenance.
            "q": fmt(q0), "Q_beta_MeV": str_at_true_precision(qb_obs),
            "m_e_MeV": fmt(me_obs),
            "rel_rms": fmt(rms_obs),
            "chosen_by": "measurement (CODATA/PDG)",
        },
        "fitted_ideal_scale_only": {
            "q": fmt(q0), "Q_beta_MeV": fmt(s_scale_only),
            "rel_rms": fmt(rms_scale_only),
            "chosen_by": "minimise low-isotope rel-RMS, CAL-2 modulus held",
        },
        "fitted_ideal_two_direction": {
            "q": fmt(q_fit), "Q_beta_MeV": fmt(s_fit),
            "m_e_implied_MeV": fmt(me_implied),
            "rel_rms": fmt(rms_fit),
            "golden_iterations": iters,
            "chosen_by": "minimise low-isotope rel-RMS over (Q_beta, q)",
        },
    })
    w.add_data("identifiability", {
        "n_calibration_points": 3,
        "n_identifiable_directions": 2,
        "cal1_m_e": "identifiable (overall MeV scale only)",
        "cal2_D_beta": "identifiable (enters Q_beta and the trace difference)",
        "cal3_D_pi": ("NOT identifiable — m_pi does not appear in "
                      "B = Q_beta*(tr_M(W_free) - tr_M(W_atom)); the objective "
                      "is flat in it. Held at its observational value."),
    })
    w.add_data("isotopes", rows_out)
    w.add_data("held_out", {
        "note": ("Never shown to the fit. Tests whether a calibration fitted "
                 "on the light nuclei generalises; separates 'calibration was "
                 "badly chosen' from 'the model's A-dependence is wrong'."),
        "rel_rms_observational_calibration": fmt(rms_ho_obs),
        "rel_rms_calibration_fitted_on_low": fmt(rms_ho_fit),
        "rel_rms_refitted_on_held_out": fmt(rms_ho_best),
        "q_refitted_on_held_out": fmt(q_ho_refit),
        "Q_beta_refitted_on_held_out_MeV": fmt(s_ho_best),
        "rows": heldout_rows,
    })
    w.add_data("q_scan", scan)
    w.add_data("anti_fit_label", {
        "is_a_fit": True,
        "may_be_wired_to_production": False,
        "canonical_layer_unchanged": "math ideal",
        "production_pin_unchanged": "proton experimental anchor",
    })
    w.add_assertion("gate_reproduces_committed_sweep", gate_ok, True)
    w.add_assertion("three_calibration_points", 3, 3)
    w.add_assertion("fitted_not_derived", True, True)
    w.save()
    print(f"\nwall {wall:.1f}s -> fitted-ideal-low-isotope-calibration.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
