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
import math
import sys

from witness_base import WitnessBuilder  # noqa: E402
from binding_canonical import binding_canonical  # noqa: E402
from q_beta_substrate_prediction import q_beta_substrate  # noqa: E402
from experimental_constants import Q_NEUTRON_MEV  # noqa: E402

# substrate inputs (CAL-1 m_e, CAL-2 q₀) — pure canonical, no fit
from q_parameter import Q as Q0  # noqa: E402
from codata_constants import M_E_MEV as _ME  # noqa: E402

# bound states to package (Re channel needs the bound-knot trace → A small)
ISOTOPES = [("2H", 1, 1), ("3H", 1, 2), ("3He", 2, 1), ("4He", 2, 2)]

# AME binding ground truth (MeV) for the Re cross-check
B_AME = {"2H": 2.224566, "3H": 8.481821, "3He": 7.718058, "4He": 28.295673}


def complex_volume(Z: int, N: int):
    """𝔙 = 𝔈_bind + i·𝔔_β for the (Z,N) bound knot. Im is the single
    n→p β-decay Q-value (the bar-odd partner of the bar-even binding)."""
    bc = binding_canonical(Z, N, use_transfer=True, use_closed_form=False)
    re = float(bc["B_MeV"])                              # binding  (Re)
    im = q_beta_substrate(float(Q0), float(_ME))         # Q_β       (Im)
    mod = math.hypot(re, im)                             # |𝔙| (mass-modulus)
    arg = math.atan2(im, re)                             # arg 𝔙 (EM phase)
    return {
        "re_binding_MeV": re,
        "im_qbeta_MeV": im,
        "modulus_MeV": mod,
        "arg_rad": arg,
        "tr_M_atom": bc.get("tr_M_atom"),
        "tr_M_free": bc.get("tr_M_free"),
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

    print("\n  COMPLEX-VOLUME WITNESS  𝔙 = 𝔈_bind + i·𝔔_β")
    print(f"  q₀ = {float(Q0):.10f}   Im(q₀)=0 ⇒ Re,Im both real (fibre caveat)\n")
    print("| iso | Re 𝔙 = binding (MeV) | B_AME | Re err | Im 𝔙 = Q_β (MeV) | |𝔙| | arg 𝔙 (rad) |")
    print("|---|--:|--:|--:|--:|--:|--:|")
    for name, Z, N, cv, b_ame, re_err in rows:
        print(f"| {name} | {cv['re_binding_MeV']:.4f} | {b_ame:.4f} "
              f"| {re_err*100:.2f}% | {cv['im_qbeta_MeV']:.6f} "
              f"| {cv['modulus_MeV']:.4f} | {cv['arg_rad']:.5f} |")
    print(f"\n  Im channel: Q_β,pred = {im_pred:.6f} MeV vs CODATA "
          f"{qbeta_codata:.6f} MeV  (err {im_err*100:.3f}%)")
    print("  Re channel: canonical binding defect E₀·(tr_free − tr_atom), "
          "binding_canonical.")

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
    for name, Z, N, cv, b_ame, re_err in rows:
        w.add_data(f"V_{name}", {
            "re_binding_MeV": cv["re_binding_MeV"],
            "im_qbeta_MeV": cv["im_qbeta_MeV"],
            "modulus_MeV": cv["modulus_MeV"],
            "arg_rad": cv["arg_rad"],
            "B_AME_MeV": b_ame,
            "re_rel_err": re_err,
        })
    w.save()
    print("\n  witness written: complex-volume-unification.witness.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
