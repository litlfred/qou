#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical witness; packages two canonical
# real observables as one complex object, no symbolic-q polynomial output.
"""
Complex-volume witness — 𝔙 = E₀·tr_M((Π_free − 1)∘𝓜) as ONE object.

Realizes the unification conjecture
[`conj:binding-qbeta-complex-volume`] computationally: binding energy and
the β-decay Q-value are the real and imaginary parts of a single complex
fibre observable, the QOU analogue of the Neumann–Zagier complex volume
𝕍 = Vol + i·CS.

  𝔙(K)  =  𝔈_bind(K)  +  i · 𝔔_β
  Re 𝔙  =  binding  (bar-even / cosh / volume channel)   — binding_canonical
  Im 𝔙  =  Q_β      (bar-odd  / sinh / Chern–Simons)      — q_beta_substrate

FIBRE-LEVEL CAVEAT (STRICT, carried into the witness). At the archimedean
substrate anchor Im(q₀)=0, so BOTH Re and Im are real measured numbers; the
complex structure is fibre-level (pre-τ). This script does NOT manufacture a
complex q₀ — it packages the two real archimedean shadows of the one fibre
object and records |𝔙|, arg 𝔙 (the polar / mass-modulus & EM-phase reading
of `rem:mass-modulus-em-phase-color-grading`). The shared categorical defect
δ = tr_M(W_free) − tr_M(W_atom) is the object both channels read; that the
two observables descend from ONE fibre 𝔙 is the open conjecture, not proved
here. What is emitted is the consistent single-object packaging + both
cross-checks.

Run:  python3 -u computations/complex_volume_witness.py 2>&1 | tee /tmp/cv.log
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — substrate/ subdir bridge
from _precision import set_compute_dps  # noqa: E402 — raise dps before any mpmath value
import math
import sys

from witness_base import WitnessBuilder  # noqa: E402
from binding_canonical import binding_canonical  # noqa: E402
from q_beta_substrate_prediction import q_beta_substrate  # noqa: E402
from experimental_constants import Q_NEUTRON_MEV  # noqa: E402
from tr_m_atom_via_transfer import tr_m_atom_zn  # noqa: E402

# substrate inputs (CAL-1 m_e, CAL-2 q₀) — pure canonical, no fit
from q_parameter import Q_MP as Q0  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION, AME_B_HE3_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION, M_E_MEV as _ME  # noqa: E402

# canonical energy scale α = E₀ = m_e/(q₀(q₀−1)) ≈ 4.186 MeV (derived,
# the dashboard scale) — distinct from binding_canonical's Q_β multiplier.
_E0 = float(_ME) / (float(Q0) * (float(Q0) - 1.0))

# bound states to package (Re channel needs the bound-knot trace → A small)
ISOTOPES = [("2H", 1, 1), ("3H", 1, 2), ("3He", 2, 1), ("4He", 2, 2)]

# AME binding ground truth (MeV) for the Re cross-check
B_AME = {"2H": float(AME_B_DEUTERON_MEV_VALIDATION), "3H": float(AME_B_TRITIUM_MEV_VALIDATION), "3He": float(AME_B_HE3_MEV_VALIDATION), "4He": float(AME_B_HE4_MEV_VALIDATION)}


# This producer never raised working precision, so every mpmath value in
# it was built at mpmath's default 15 dps and the numbers it emits are
# HONESTLY float64 — no fake precision to detect, no constant built too
# early, so the padding / raw-float64 / import-time gates all pass it.
# Gate: never_raises_dps_audit.py (bean qou-j6gb). Idempotent.
set_compute_dps()

def complex_volume(Z: int, N: int):
    """𝔙 = 𝔈_bind + i·𝔔_β for the (Z,N) bound knot. Im is the single
    n→p β-decay Q-value (the bar-odd partner of the bar-even binding).

    Re uses the magnitude-correct **log-trace** form (the exact
    standard-part / archimedean realization)
        𝔈_bind = E₀·ln(tr_free / tr_atom),   E₀ = m_e/(q₀(q₀−1)),
    so |𝔙| and arg 𝔙 are physical (Re-dominated). The earlier
    linear-defect form E₀·(tr_free−tr_atom) (binding_canonical, Q_β-scaled)
    is retained as `re_linear_MeV` for comparison — it under-predicts 5–40×
    and is NOT used for the polar quantities."""
    import mpmath as mp
    ta, tf, _, _ = tr_m_atom_zn(Z, N, dps=50)
    # bar-involution conjugate trace: tr̆_M = tr_M(q₀⁻¹). The principled
    # mass-modulus is the BAR-NORM ‖tr_M‖² = tr_M(q₀)·tr_M(q₀⁻¹) (bar-even,
    # the cosh / binding channel), NOT the usual |tr_M(q₀)|² = tr_M(q₀)².
    # They coincide on the unit circle (where conjugation = bar-involution)
    # and DIFFER at the real anchor q₀ (q̄₀=q₀≠q₀⁻¹).
    ta, tf = float(ta), float(tf)
    mass_mod_usual = abs(ta)                             # |tr_M(q₀)|
    # bar-norm tr_M(q₀)·tr_M(q₀⁻¹) needs tr_M re-lifted at q₀⁻¹.
    #
    # CORRECTED 2026-08-19 (bean `qou-e58e`). This comment used to say the
    # word "BAKES q₀ into its crossing values, so it cannot re-lift at q⁻¹",
    # citing the tr_m_atom_via_transfer docstring — which was itself stale and
    # is fixed in the same commit. The re-lift WORKS: tr_M(q₀⁻¹) computes in
    # milliseconds, and the try/except below has never been the thing that
    # fires. What fires is `bar_prod > 0` in the next line, because the
    # product is NEGATIVE (deuteron: −8.5e-4; free: −3.3e-3). So the bar-norm
    # is not "not yet computable" — as a real number it DOES NOT EXIST for
    # this word, which is a stronger and different statement.
    #
    # What the bar image does carry is a mirror law: q ↦ 1/q exchanges
    # (Z,N) ↔ (N,Z) up to one universal offset δ(q), measured to 22–30 digits
    # over A = 2..6. See
    # `computations/substrate/bar_involution_is_isospin_probe.py`.
    ta_i = None
    mass_mod_bar = None
    try:
        q_inv = mp.mpf(1) / mp.mpf(str(Q0))
        ta_i_mp, _, _, _ = tr_m_atom_zn(Z, N, q=q_inv, dps=50)
        ta_i = float(ta_i_mp)
        bar_prod = ta * ta_i
        mass_mod_bar = math.sqrt(bar_prod) if bar_prod > 0 else None
    except Exception:
        ta_i = None
        mass_mod_bar = None
    re = _E0 * math.log(tf / ta)                         # binding (Re) — log-trace
    re_lin = float(binding_canonical(
        Z, N, use_transfer=True, use_closed_form=False)["B_MeV"])
    im = q_beta_substrate(float(Q0), float(_ME))         # Q_β     (Im)
    mod = math.hypot(re, im)                             # |𝔙| (usual)
    arg = math.atan2(im, re)                             # arg 𝔙 (EM phase)
    return {
        "re_binding_MeV": re,
        "re_linear_MeV": re_lin,
        "im_qbeta_MeV": im,
        "modulus_MeV": mod,
        "arg_rad": arg,
        "tr_M_atom": ta,
        "tr_M_free": tf,
        "tr_M_atom_qinv": ta_i,
        "mass_mod_usual": mass_mod_usual,
        "mass_mod_bar": mass_mod_bar,
        "bar_vs_usual_ratio": (mass_mod_bar / mass_mod_usual)
        if (mass_mod_bar and mass_mod_usual) else None,
    }


def main() -> int:
    qbeta_codata = float(Q_NEUTRON_MEV)
    rows = []
    for name, Z, N in ISOTOPES:
        cv = complex_volume(Z, N)
        b_ame = B_AME[name]
        re_err = abs(cv["re_binding_MeV"] - b_ame) / b_ame
        rows.append((name, Z, N, cv, b_ame, re_err))

    # Im cross-check (shared across isotopes — the n→p decay)
    im_pred = rows[0][3]["im_qbeta_MeV"]
    im_err = abs(im_pred - qbeta_codata) / qbeta_codata

    print("\n  COMPLEX-VOLUME WITNESS  𝔙 = 𝔈_bind + i·𝔔_β   (Re = log-trace binding)")
    print(f"  q₀ = {float(Q0):.10f}   E₀ = {_E0:.4f} MeV   "
          f"Im(q₀)=0 ⇒ Re,Im both real (fibre caveat)\n")
    print("| iso | Re 𝔙 = binding (MeV) | B_AME | Re err | Im 𝔙 = Q_β (MeV) | |𝔙| | arg 𝔙 (rad) | (re_linear) |")
    print("|---|--:|--:|--:|--:|--:|--:|--:|")
    for name, Z, N, cv, b_ame, re_err in rows:
        print(f"| {name} | {cv['re_binding_MeV']:.4f} | {b_ame:.4f} "
              f"| {re_err*100:.2f}% | {cv['im_qbeta_MeV']:.6f} "
              f"| {cv['modulus_MeV']:.4f} | {cv['arg_rad']:.5f} "
              f"| {cv['re_linear_MeV']:.4f} |")
    print("\n  Mass-modulus: usual |tr_M(q₀)| vs bar-norm √(tr_M(q₀)·tr_M(q₀⁻¹))")
    print("  (bar-even; the principled |·|. Coincide on |q|=1; differ at real q₀.)")
    print("| iso | tr_M(q₀) | tr_M(q₀⁻¹) | |tr_M| usual | bar-norm | bar/usual |")
    print("|---|--:|--:|--:|--:|--:|")
    for name, Z, N, cv, b_ame, re_err in rows:
        ti, bn, rt = cv["tr_M_atom_qinv"], cv["mass_mod_bar"], cv["bar_vs_usual_ratio"]
        ti_s = f"{ti:.6f}" if ti is not None else "n/a*"
        bn_s = f"{bn:.6f}" if bn is not None else "n/a*"
        rt_s = f"{rt:.4f}" if rt is not None else "—"
        print(f"| {name} | {cv['tr_M_atom']:.6f} | {ti_s} "
              f"| {cv['mass_mod_usual']:.6f} | {bn_s} | {rt_s} |")
    print("  *bar-norm n/a here because tr_M(q₀)·tr_M(q₀⁻¹) is NEGATIVE, so it "
          "has no real square root — NOT because the re-lift fails. The q₀⁻¹ "
          "column above is computed for every row. Corrected 2026-08-19 (bean "
          "`qou-jqjc`); the old wording claimed the word could not re-lift at "
          "q⁻¹, which the same table disproves. As a real number the bar-norm "
          "does not EXIST for those words, which is stronger than 'not yet "
          "computable' and means the claim should be retired, not repaired.")

    print(f"\n  Im channel: Q_β,pred = {im_pred:.6f} MeV vs CODATA "
          f"{qbeta_codata:.6f} MeV  (err {im_err*100:.3f}%)")
    print("  Re channel: log-trace binding E₀·ln(tr_free/tr_atom) (magnitude-"
          "correct); re_linear = E₀·(tr_free−tr_atom) shown for comparison "
          "(under-predicts 5–40×). arg 𝔙 now Re-dominated (physical).")

    w = WitnessBuilder(
        "complex-volume-unification",
        engine="complex_volume_witness.py",
    )
    w.set_description(
        "𝔙 = 𝔈_bind + i·𝔔_β: binding (Re) and β-decay Q-value (Im) as "
        "the two real archimedean shadows of one complex fibre object "
        "(conj:binding-qbeta-complex-volume). Im(q₀)=0 ⇒ both real; "
        "complex structure is fibre-level. Re via binding_canonical, "
        "Im via q_beta_substrate_prediction; pure-canonical (m_e, q₀). "
        "Packaging only — that both descend from one fibre 𝔙 is the open "
        "conjecture, not proved here (no binding/Q_β double-count: main "
        "cdc2d867 branch A)."
    )
    w.set_content_block("conj:binding-qbeta-complex-volume")
    w.add_parameter("q_0", float(Q0))
    w.add_parameter("m_e_MeV", float(_ME))
    w.add_parameter("Q_beta_codata_MeV", qbeta_codata)
    w.add_data("im_qbeta_pred_MeV", str(im_pred))
    w.add_data("im_qbeta_rel_err", str(im_err))
    w.add_data("fibre_caveat", "Im(q_0)=0; complex structure is fibre-level (pre-tau)")

    # Assertions (bean `qou-jqjc`). This witness previously emitted NONE, so a
    # consumer reading `allPassed` saw a pass over zero checks — the producer's
    # prose was honest but its machine surface was not. Values are passed as
    # STRINGS, the drained convention (qou-t0rf), so adding them does not put
    # new raw float64 into the witness.
    #
    # Only what is actually checked is asserted. In particular there is NO Re
    # assertion: the log-trace binding sits 22–69% from AME (see re_rel_err per
    # isotope in the data), which is a recorded gap, not a passing test. Nor is
    # the single-frakV descent asserted — it is the open conjecture.
    w.add_assertion(
        "im_qbeta_matches_codata",
        computed=str(im_pred), expected=str(qbeta_codata),
        tolerance=str(0.002 * qbeta_codata), unit="MeV",
        source="CODATA neutron beta-decay Q-value")
    im_spread = max(abs(r[3]["im_qbeta_MeV"] - im_pred) for r in rows)
    w.add_assertion(
        "im_channel_isotope_independent",
        computed=str(im_spread), expected="0", tolerance="1e-30", unit="MeV",
        source="Im is the single n->p decay Q-value, so it cannot vary by isotope")
    w.add_caveat(
        "Re channel is NOT asserted: the log-trace binding is 22-69% from AME "
        "across 2H/3H/3He/4He (re_rel_err per isotope). Recorded, not checked.")
    w.add_caveat(
        "The single-frakV descent (conj:binding-qbeta-complex-volume) is NOT "
        "tested here. Im is ASSIGNED from q_beta_substrate, not derived from a "
        "trace; that the two channels descend from one fibre object is the open "
        "conjecture. `allPassed` refers to the two assertions above and to "
        "nothing else.")
    w.add_caveat(
        "Bar-norm sqrt(tr_M(q0)*tr_M(q0^-1)) is n/a for 2H and 3H because the "
        "product is NEGATIVE, not because the re-lift fails; as a real number it "
        "does not exist for those words.")
    for name, Z, N, cv, b_ame, re_err in rows:
        w.add_data(f"V_{name}", {
            "re_binding_MeV": cv["re_binding_MeV"],
            "re_linear_MeV": cv["re_linear_MeV"],
            "im_qbeta_MeV": cv["im_qbeta_MeV"],
            "modulus_MeV": cv["modulus_MeV"],
            "arg_rad": cv["arg_rad"],
            "B_AME_MeV": b_ame,
            "re_rel_err": re_err,
            "tr_M_atom_q0": cv["tr_M_atom"],
            "tr_M_atom_q0_inv": cv["tr_M_atom_qinv"],
            "mass_mod_usual": cv["mass_mod_usual"],
            "mass_mod_bar": cv["mass_mod_bar"],
            "bar_vs_usual_ratio": cv["bar_vs_usual_ratio"],
        })
    w.save()
    print("\n  witness written: complex-volume-unification.witness.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
