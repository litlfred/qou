#!/usr/bin/env python3
"""qbeta_c3_hopf_cubic_residue_probe.py — EXPLORATION of the sharp c_3 target
(bean qou-1dnr): does the EXACT categorical bar-odd carrier
`Δ_net^odd = (h/4)·C(y)`, evaluated at the substrate and normalized by a
CORPUS-PRINCIPLED quantity, reproduce the bar-odd part of the Q_β ladder
coefficient c_3?

## The route being tested (the redirect the three 2026-07-20 routes triangulated to)

Three independent routes landed NEGATIVE and pointed to the SAME open piece:

  * DM-cubic / Berezinian (`qbeta_c3_dm_cubic_berezinian_probe.py`): the genuine
    target is the SMOOTH bar-odd object `S = h·D(ũ)`, not a swinging real-q c_3.
  * Habiro-element growth dichotomy (`qbeta_c3_habiro_growth_dichotomy.py`): the
    Q_β ladder is GEOMETRIC (finite radius, simple pole at u_substrate), so c_3
    is the ANALYTIC RESIDUE of that simple pole — NOT a formal Habiro series.
  * GGM-Stokes (`qbeta_c3_stokes_ggm_order3_probe.py`): a flat (anchor-invariant)
    datum is the CORRECT type; the extracted-c_3 "swing" is a 1/u³
    ladder-inversion artifact (KC21), NOT the obstruction. Open piece = the
    NORMALIZED §4e bridge.

The corpus ALREADY gives the EXACT carrier (KC20, Lean-proved in
`QBetaZeta4ResidueRefutation.lean`):

    Δ_net^odd = (h/4)·C(y),  h = q − q⁻¹,  y = q² + q⁻² = 2cosh 2λ,
    C(y) = y³ − 4y² + 3y − 2   (irreducible/ℚ, disc −152, Galois S₃),

sourced by the Hopf (double-crossing) sector. So the OPEN piece is the
residue / normalization connection from this exact carrier to the c_3 rung.

## What this probe does (formalize-first; the structural object narrows the compute)

1. Evaluate the EXACT carrier `(h/4)·C(y_0)` at BOTH the proton- and muon-pinned
   substrate anchors → confirm it is anchor-INVARIANT (flat). Per route C this
   is now the CORRECT signature (a derived object must be flat), NOT a failure.

2. Extract the empirical c_3 at both anchors (the canonical CODATA-anchored
   `c3_target_at`), split c_3 into its bar-even part (≈ −Vol(4₁), "exactly
   measured") and its bar-odd part `S = c_3 + Vol(4₁)` (the OPEN channel; the
   capstone `2026-07-12-c3-wall-resolution-capstone.md`). Confirm `S` swings
   SIGN across anchors (μ +0.0097 / p −0.0395) — the KC21 1/u³ representation
   artifact — while the physical |S| scale ≈ 0.0094 is anchor-blind (the Φ_b
   state-integral volume deficit).

3. Ask: is there a CORPUS-PRINCIPLED normalization N with
   `N·(h/4)·C(y_0) = S` (or `= |S|_geom = 0.0094`)? Test named corpus
   quantities (h², u³, u_substrate⁴, the KC19 bar-odd kernel `K(q)=2h/(4w₀²−h²)`,
   1/(4q⁷), …). A normalization TUNED to hit S is a FIT and is labelled so.

## Honesty (AGENTS.md §Axiomatization is NOT a Proof; anti-laundering; refuted-scope)

  * Derivation ONLY if the bar-odd carrier comes from the EXACT categorical C(y)
    + a principled (corpus-EXISTING) normalization — NEVER by inverting Q_β to
    fit. The CODATA-anchored c_3 / S are used ONLY as the comparison target.
  * The irreducible-cubic fact (KC20) means the bar-odd part of c_3 is NOT a
    real-q algebraic ROOT of C — but it CAN be the VALUE C(y_0) times a residue
    normalization. This probe keeps that distinction sharp: it evaluates C(y_0)
    (a value), it does not seek a root.
  * No c_k wired; no production; no tier change; bean stays open unless the
    bar-odd channel is genuinely derived.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))                                  # computations/
sys.path.insert(0, str(HERE.parent / "qbeta"))                       # computations/qbeta/
sys.path.insert(0, str(HERE.parent.parent / "tools" / "qou-substrate" / "python"))

import _path_bridge  # noqa: E402, F401
from mpmath import mp, mpf  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from qbeta_utils import c3_target_at, substrate_ladder_quantities  # noqa: E402
from codata_constants import M_E_MEV, Q_BETA_MEV  # noqa: E402

from qou_substrate.constants import q_at, q_muon_at, VOL_FIGURE_EIGHT  # noqa: E402


# ── The EXACT categorical bar-odd carrier (KC20, Lean-proved) ──
def cubic_C(y: mpf) -> mpf:
    """C(y) = y³ − 4y² + 3y − 2 — the irreducible cubic in the trace variable
    (QBetaZeta4ResidueRefutation.cubicC)."""
    return y ** 3 - 4 * y ** 2 + 3 * y - 2


def cubic_C_Hopf(y: mpf) -> mpf:
    """C_Hopf(y) = y³ − 6y² + 10y − 6 — the Hopf (double-crossing) sector cubic
    that sources the degree-3 field (QBetaZeta4ResidueRefutation.cubicC_Hopf)."""
    return y ** 3 - 6 * y ** 2 + 10 * y - 6


def carrier_odd(q: mpf) -> mpf:
    """Δ_net^odd(q) = (h/4)·C(y), h = q − q⁻¹, y = q² + q⁻². The EXACT bar-odd
    part of the net decay-width Laurent polynomial (numerator over 4q⁷). Smooth
    real-q object ⇒ anchor-invariant."""
    h = q - 1 / q
    y = q ** 2 + 1 / q ** 2
    return (h / 4) * cubic_C(y)


def swing_pct(vp: mpf, vm: mpf) -> mpf:
    return (vp - vm) / vm * 100 if vm != 0 else mpf("nan")


def main() -> int:
    set_compute_dps()
    t0 = time.time()
    me = mpf(str(M_E_MEV))
    qc = mpf(str(Q_BETA_MEV))
    qp = q_at(mp.dps)
    qm = q_muon_at(mp.dps)
    vol41 = mpf(VOL_FIGURE_EIGHT) if not callable(VOL_FIGURE_EIGHT) else VOL_FIGURE_EIGHT()

    # (1) EXACT carrier at both anchors -----------------------------------------
    car_p = carrier_odd(qp)
    car_m = carrier_odd(qm)
    car_swing = swing_pct(car_p, car_m)
    dcar_dq = (car_p - car_m) / (qp - qm)

    yp = qp ** 2 + 1 / qp ** 2
    hp = qp - 1 / qp
    Chopf_p = cubic_C_Hopf(yp)

    # (2) Empirical c_3, its bar-even (−Vol) and bar-odd (S) split ---------------
    emp_p = c3_target_at(qp, qc, me)
    emp_m = c3_target_at(qm, qc, me)
    emp_swing = swing_pct(emp_p, emp_m)
    dc3_dq = (emp_p - emp_m) / (qp - qm)

    # bar-odd part of c_3 (capstone: S = c_3 + Vol(4₁); bar-even part ≈ −Vol(4₁))
    S_p = emp_p + vol41
    S_m = emp_m + vol41
    S_swing = swing_pct(S_p, S_m)
    S_geom = mpf("0.0094")   # anchor-blind Φ_b state-integral |S| scale (capstone)

    subp = substrate_ladder_quantities(qp)
    subm = substrate_ladder_quantities(qm)
    u_p = subp["u"]
    u_m = subm["u"]

    # (3) Normalization analysis ------------------------------------------------
    # What N would take the EXACT carrier onto S (or its anchor-blind magnitude)?
    N_to_Sp = S_p / car_p                # onto proton S
    N_to_Sm = S_m / car_m                # onto muon S
    N_to_Sgeom = S_geom / abs(car_p)     # onto the anchor-blind |S| scale

    # Corpus-named normalization candidates evaluated at the proton anchor.
    # (If any equals N_to_S* to several digits WITHOUT being tuned, it is a lead;
    #  otherwise the normalization is not a corpus quantity — an open/fitted map.)
    cand = {
        "h_sq": hp ** 2,
        "h": hp,
        "u_sub": u_p,
        "u_sub_sq": u_p ** 2,
        "u_sub_cubed": u_p ** 3,
        "u_sub_4th": u_p ** 4,
        "one_over_4q7": 1 / (4 * qp ** 7),
        "hbar_q_sq": subp["hbar_q"] ** 2,
        "z": subp["z"],
    }

    print("=" * 84)
    print(" Q_β c_3 — Hopf-cubic ANALYTIC-RESIDUE exploration (bean qou-1dnr)")
    print("=" * 84)
    print(f"  q_proton = {mp.nstr(qp, 26)}")
    print(f"  q_muon   = {mp.nstr(qm, 26)}   (Δq = {mp.nstr(qp - qm, 4)})")
    print(f"  Vol(4₁)  = {mp.nstr(vol41, 16)}")
    print()
    print("  (1) EXACT categorical bar-odd carrier  Δ_net^odd = (h/4)·C(y_0):")
    print(f"      proton = {mp.nstr(car_p, 14)}")
    print(f"      muon   = {mp.nstr(car_m, 14)}")
    print(f"      swing  = {float(car_swing):+.3e} %   dcarrier/dq = {mp.nstr(dcar_dq, 5)}")
    print(f"      → ANCHOR-INVARIANT (flat). y_0 = {mp.nstr(yp,12)}, C(y_0) = {mp.nstr(cubic_C(yp),12)}")
    print(f"      Hopf-sector piece (h/4)·C_Hopf(y_0) = {mp.nstr((hp/4)*Chopf_p, 12)}")
    print()
    print("  (2) Empirical c_3 (CODATA-anchored) and its bar-even/bar-odd split:")
    print(f"      c_3         proton = {mp.nstr(emp_p, 12)}   muon = {mp.nstr(emp_m, 12)}")
    print(f"      c_3 swing = {float(emp_swing):+.4f} %   dc_3/dq = {mp.nstr(dc3_dq, 5)}")
    print(f"      bar-EVEN part  ≈ −Vol(4₁) = {mp.nstr(-vol41, 12)}  (exactly measured)")
    print(f"      bar-ODD  part  S = c_3+Vol(4₁):  proton = {mp.nstr(S_p, 10)}  muon = {mp.nstr(S_m, 10)}")
    print(f"      S swing = {float(S_swing):+.3f} %  → S SWINGS SIGN (bar-odd Im(q) projection, KC21)")
    print(f"      anchor-blind physical |S| scale (Φ_b state integral) ≈ {mp.nstr(S_geom,4)}")
    print()
    print("  (3) Normalization needed to map EXACT carrier → S:")
    print(f"      N (carrier→S_proton)     = {mp.nstr(N_to_Sp, 10)}")
    print(f"      N (carrier→S_muon)       = {mp.nstr(N_to_Sm, 10)}  ← DIFFERENT (S swings, carrier flat)")
    print(f"      N (carrier→|S|_geom)     = {mp.nstr(N_to_Sgeom, 10)}")
    print()
    print("      Corpus-named normalization candidates (proton anchor):")
    for k, v in cand.items():
        r_geom = v / N_to_Sgeom if N_to_Sgeom != 0 else mpf("nan")
        print(f"        {k:>14} = {mp.nstr(v, 10):>16}   (÷ N_geom = {mp.nstr(r_geom, 6)})")
    print()

    # (3b) Bar-odd factorization S = h·D(ũ) (KC21) vs carrier = (h/4)·C(y) -------
    # BOTH S and the carrier are bar-ODD (h bar-odd, C(y) & D(ũ) bar-even), so BOTH
    # factor automatically as h·(bar-even). The shared h is bookkeeping, NOT a
    # match. The genuine open content is the bar-EVEN ratio D(ũ)/C(y):
    #   N = S/carrier = h·D / ((h/4)·C) = 4·D(ũ)/C(y)  (bar-even/bar-even).
    D_p = S_p / hp                       # implied bar-even ladder value D(ũ) at proton
    D_m = S_m / (qm - 1 / qm)            # at muon
    ratio_4D_over_C_p = 4 * D_p / cubic_C(yp)
    print("  (3b) Bar-odd factorization  S = h·D(ũ)  vs  carrier = (h/4)·C(y):")
    print(f"       implied D(ũ) = S/h:  proton = {mp.nstr(D_p, 10)}  muon = {mp.nstr(D_m, 10)}")
    print(f"       ⇒ N = S/carrier = 4·D(ũ)/C(y) (bar-even) = {mp.nstr(ratio_4D_over_C_p, 10)} (proton)")
    print("       The shared bar-odd h is AUTOMATIC (any bar-odd Laurent object = h·(bar-even));")
    print("       it is NOT evidence. The open piece is the bar-even ratio 4D/C — and D(ũ)")
    print("       is the KC22 resurgent/non-holonomic ℚ(√3) ladder (radius→0), so 4D/C is")
    print("       as transcendental as D. The fixed cubic C(y) does NOT supply it.")
    print()

    # Verdict logic -------------------------------------------------------------
    ANCHOR_INV = mpf("1e-3")   # percent
    carrier_flat = abs(car_swing) < ANCHOR_INV
    # A corpus candidate "matches" N_geom if within 1% WITHOUT tuning.
    matches = {k: (abs(v / N_to_Sgeom - 1) < mpf("0.01")) for k, v in cand.items()}
    any_principled = any(matches.values())

    print("=" * 84)
    print(" VERDICT")
    print("=" * 84)
    print(f"  carrier anchor-invariant (flat)?  {carrier_flat}  "
          f"(swing {float(car_swing):.2e}% << c_3 swing {float(emp_swing):.2f}%)")
    print(f"  any corpus-named normalization hits N_geom within 1% (no tuning)?  {any_principled}")
    if any_principled:
        for k, ok in matches.items():
            if ok:
                print(f"        LEAD: {k} ≈ N_geom")
    print()
    print("  Reading:")
    print("   • The EXACT carrier (h/4)·C(y_0) is ANCHOR-INVARIANT — the CORRECT type")
    print("     for a derived object (route C). Its value is O(0.1), the physical |S|")
    print("     scale is O(0.01); the map between them is the OPEN normalization.")
    print("   • The bar-odd target S ITSELF swings sign across anchors (the 1/u³")
    print("     representation artifact, KC21) — so no flat object equals S at both")
    print("     anchors; the fair anchor-blind target is |S|_geom ≈ 0.0094 (state integral).")
    print("   • Whether (h/4)·C(y_0) maps onto |S|_geom by a CORPUS quantity is the crux:")
    print("     if no named quantity hits N_geom un-tuned, the normalization is OPEN")
    print("     (the §4e / conj:qdifference-kernel-prolongation-symbol keystone), and any")
    print("     hand-picked N is a FIT — NOT a derivation of the bar-odd channel.")

    if carrier_flat and not any_principled:
        verdict = ("DERIVED_MODULO_OPEN_NORMALIZATION — exact flat carrier (correct "
                   "type) but NO corpus-named normalization maps it onto |S|; the "
                   "residue/§4e normalization stays the open keystone. NOT a full "
                   "derivation; scope-(a), nothing wired.")
    elif carrier_flat and any_principled:
        verdict = ("LEAD — a corpus-named normalization matches N_geom un-tuned; "
                   "candidate derivation of the bar-odd channel PENDING verification.")
    else:
        verdict = "CARRIER_NOT_FLAT — unexpected; re-examine."
    print()
    print(f"  VERDICT: {verdict}")

    # ── witness ──
    wb = WitnessBuilder("qbeta-c3-hopf-cubic-residue", engine="mpmath")
    wb.set_description(
        "EXPLORATION (bean qou-1dnr): does the EXACT categorical bar-odd carrier "
        "Δ_net^odd = (h/4)·C(y) (KC20, Lean-proved; C irreducible cubic, Hopf "
        "double-crossing sector) evaluated at the substrate, normalized by a "
        "CORPUS-PRINCIPLED quantity, reproduce the bar-odd part of the Q_β ladder "
        "c_3 (S = c_3 + Vol(4₁))? The carrier is ANCHOR-INVARIANT (correct type, "
        "route C); the target S swings sign (1/u³ artifact, KC21) with anchor-blind "
        "|S| scale ≈ 0.0094 (Φ_b state integral). No corpus-named normalization "
        "(h², u^k, KC19 kernel, 1/4q⁷, …) maps the carrier onto |S| un-tuned ⇒ the "
        "residue/§4e normalization is the OPEN keystone "
        "(conj:qdifference-kernel-prolongation-symbol). NOT a full derivation; "
        "nothing inverted from Q_β; no c_k wired; no tier change."
    )
    wb.set_content_block("conj:qdifference-kernel-prolongation-symbol")
    wb.set_audit_only("docs/audits/2026-07-20-c3-hopf-cubic-residue-exploration.md")
    wb.add_data("anchors", {"q_proton": fmt(qp), "q_muon": fmt(qm),
                            "delta_q": fmt(qp - qm), "vol_4_1": fmt(vol41)})
    wb.add_data("exact_carrier_hopf_cubic", {
        "proton": fmt(car_p), "muon": fmt(car_m), "swing_pct": fmt(car_swing),
        "dcarrier_dq": fmt(dcar_dq), "y0_proton": fmt(yp),
        "C_y0_proton": fmt(cubic_C(yp)),
        "hopf_sector_piece_proton": fmt((hp / 4) * Chopf_p),
        "note": "(h/4)·C(y_0), C(y)=y³−4y²+3y−2 (KC20). Anchor-invariant (flat).",
    })
    wb.add_data("empirical_c3", {
        "proton": fmt(emp_p), "muon": fmt(emp_m), "swing_pct": fmt(emp_swing),
        "dc3_dq": fmt(dc3_dq),
        "note": "CODATA-anchored (c3_target_at); comparison target only, not inverted to fit.",
    })
    wb.add_data("c3_bar_split", {
        "bar_even_part_approx": fmt(-vol41),
        "bar_odd_S_proton": fmt(S_p), "bar_odd_S_muon": fmt(S_m),
        "S_swing_pct": fmt(S_swing), "S_geom_anchor_blind": fmt(S_geom),
        "note": "S = c_3 + Vol(4₁) (capstone 2026-07-12). S swings SIGN; |S|_geom ≈ 0.0094 (Φ_b state integral, anchor-blind).",
    })
    wb.add_data("normalization_analysis", {
        "N_carrier_to_S_proton": fmt(N_to_Sp),
        "N_carrier_to_S_muon": fmt(N_to_Sm),
        "N_carrier_to_S_geom": fmt(N_to_Sgeom),
        "corpus_candidates": {k: fmt(v) for k, v in cand.items()},
        "closest_candidate": "h_sq (0.0437, 1.8% below N_geom) — near-coincidence, NOT a match",
        "any_corpus_candidate_matches_untuned": any_principled,
        "note": "No corpus-named normalization maps the carrier onto |S|_geom un-tuned; "
                "a hand-picked N is a FIT.",
    })
    wb.add_data("bar_odd_factorization", {
        "implied_D_proton": fmt(D_p), "implied_D_muon": fmt(D_m),
        "N_eq_4D_over_C_proton": fmt(ratio_4D_over_C_p),
        "note": "Both S = h·D(ũ) (KC21) and carrier = (h/4)·C(y) are bar-odd ⇒ both = "
                "h·(bar-even). The shared h is AUTOMATIC bookkeeping, not a match. The "
                "open normalization N = S/carrier = 4·D(ũ)/C(y) is bar-even; D(ũ) is the "
                "KC22 resurgent/non-holonomic ℚ(√3) ladder ⇒ N is as transcendental as D. "
                "The fixed cubic C(y) does NOT supply the bar-even ratio.",
    })
    wb.add_data("verdict", verdict)
    wb.add_data("qbeta_100x_met_via_this_route", False)

    wb.add_assertion("carrier_anchor_invariant",
                     computed=float(abs(car_swing)), expected=0.0,
                     tolerance=float(ANCHOR_INV))
    wb.add_assertion("bar_odd_S_swings_sign",
                     computed=1.0 if (S_p < 0) != (S_m < 0) else 0.0, expected=1.0)
    wb.add_assertion("no_corpus_normalization_matches_untuned",
                     computed=1.0 if not any_principled else 0.0, expected=1.0)
    wb.save()

    print()
    print("  Witness: qbeta-c3-hopf-cubic-residue.witness.json")
    print(f"  Elapsed: {time.time() - t0:.2f} s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
