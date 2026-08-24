#!/usr/bin/env python3
"""qbeta_c3_barodd_binding_sdp_dual_probe.py

The decay=binding route (owner insight): read the c₃ bar-odd S as a binding
shadow price on the ghost channel of β(4₁). This probe runs the CANONICAL
operator-selection LP (mirroring aK_via_lp_dual_hecke_basis.py: t=TR_M,
G=Gram, n_target=|tr_M|) with FULL primal+dual emission, and reports the honest
structural finding it produces.

FINDING (all computed; scope-(a); C14; no c_k wired):

  1. The operator-selection LP on β(4₁) gives a TRIVIAL dual: active set = {γ}
     (identity), shadow price 0 on the L₊/L₋/e⁻ (binding) channels.
  2. Reason — the decay/ghost mode ½(L₊−L₋) is TRACELESS: tr_M(L₊)=tr_M(L₋)
     ⇒ tr_M(½(L₊−L₋))=0. A traceless mode is INVISIBLE to any linear
     trace-target LP.
  3. But it has NEGATIVE Gram norm (⟨½(L₊−L₋)⟩²_G = −0.4275 < 0). So binding
     is a QUADRATIC (Gram / SDP) quantity, not a linear (trace / LP) shadow
     price: mass = linear tr_M (rest energy), binding = quadratic Gram
     (the mass DEFECT, second order) — physically correct.

CONCLUSION: S is NOT a linear LP shadow price (the binding channel is traceless,
LP-trivial). It is the QUADRATIC negative-norm (SDP) binding form on the ghost.
Its VALUE still needs the archimedean deformation/phase z(q₀) (the open gap) to
realize the quadratic form. This does NOT refute the decay=binding identity (the
Gram-signature split stands); it correctly locates binding in the SDP/quadratic
layer. No SDP setup is tuned to reproduce S (that would be a fit).

Companion: docs/audits/2026-07-11-qbeta-c3-barodd-nz-deformation-gap.md.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from pyhecke.gram import G as GRAM, TR_M, NF_NAMES, nf_of_word  # noqa: E402
from lp_dual_solver import provenance, solve_operator_selection_lp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

FLIP = [0, 2, 1, 4, 3, 5]


def main() -> int:
    print("=" * 78)
    print(" c₃ bar-odd S — decay=binding via operator-selection dual (H₃(q))")
    print("=" * 78)

    G = np.array(GRAM, dtype=float)
    t = np.asarray([float(x) for x in TR_M], dtype=float)
    beta = np.asarray([float(x) for x in nf_of_word([0, -2, 0, -2])], dtype=float)
    decay = (beta - beta[FLIP]) / 2.0
    n_target = abs(float(beta @ t))

    # ---- 1. canonical operator-selection LP (full primal+dual) ----
    # Pin clarabel-MPFR (50 dps). This was `backend="scipy"`, pinned for
    # byte-determinism. Measured 2026-08-23: clarabel-MPFR is byte-deterministic
    # too (6 identical solves, 1 output hash), so that reason never distinguished
    # the two. The real concern was `backend="auto"` choosing silently by whether
    # the Rust binary happened to be built; pinning `clarabel` answers it, and
    # QOU_REQUIRE_CLARABEL=1 makes a missing binary an error rather than a
    # changed answer. Bean `qou/ftuv`.
    r = solve_operator_selection_lp(t, G, n_target, backend="clarabel")
    d = r.to_dict() if hasattr(r, "to_dict") else vars(r)
    active = list(d.get("active_set", []))
    y_star = [float(x) for x in d.get("y_star", [])]
    y0 = float(d.get("y0_star", 0.0))
    print(f"\n[1] operator-selection LP (t=TR_M, n_target=|tr_M(4₁)|={n_target:.6f}):")
    print(f"    active_set = {active} => {[NF_NAMES[i] for i in active]}")
    print(f"    y_star = {[round(v,5) for v in y_star]}   y0_star = {y0:.5f}")
    print(f"    primal={float(d.get('primal_obj',0)):.5f} dual={float(d.get('dual_obj',0)):.5f} "
          f"gap={float(d.get('duality_gap',0)):.2e}")
    binding_shadow = sum(y_star[i] for i in (3, 4, 5))  # L₊,L₋,e⁻ channels
    print(f"    binding-channel shadow price (L₊+L₋+e⁻) = {binding_shadow:.6f}  (≈0 ⇒ NOT activated)")

    # ---- 2. why: the ghost is traceless ----
    tr_decay = float(decay @ t)
    print(f"\n[2] decay ghost ½(L₊−L₋): tr_M = {tr_decay:.8f}  (TRACELESS: tr_M(L₊)=tr_M(L₋)={t[3]:.6f})")
    print("    ⇒ invisible to any LINEAR trace-target LP (hence [1]'s trivial dual).")

    # ---- 3. binding is quadratic (Gram / SDP) ----
    gnorm2 = float(decay @ G @ decay)
    print(f"\n[3] Gram-norm²(decay) = {gnorm2:.6f}  (<0 ⇒ binding is QUADRATIC/SDP, negative norm)")
    print("    mass = linear tr_M (rest energy); binding = quadratic Gram (mass defect).")

    print("\n[4] VERDICT (honest): S is NOT a linear LP shadow price — the binding")
    print("    channel is traceless / LP-trivial. It is the QUADRATIC negative-norm")
    print("    (SDP) binding form on the ghost; its VALUE needs z(q₀) (open). The")
    print("    decay=binding Gram-signature identity stands; no SDP tuned to S (C14).")

    ok = (len(active) <= 2 and abs(binding_shadow) < 1e-6
          and abs(tr_decay) < 1e-9 and gnorm2 < 0)

    wb = WitnessBuilder("qbeta-c3-barodd-binding-sdp-dual", engine="pyhecke+scipy")
    wb.set_description(
        "decay=binding route for c₃ bar-odd S. Canonical operator-selection LP "
        "(t=TR_M,G=Gram,n_target=|tr_M(4₁)|) gives a TRIVIAL dual (active={γ}, "
        "binding shadow 0) because the decay ghost ½(L₊−L₋) is TRACELESS "
        "(tr_M=0) — invisible to a linear trace-target LP. It has negative Gram "
        "norm (−0.4275), so binding is a QUADRATIC (SDP) quantity: mass=linear "
        "tr_M, binding=quadratic Gram (mass defect). S is the SDP negative-norm "
        "binding form on the ghost; value needs z(q₀). Scope-(a); C14; no c_k "
        "wired; no SDP tuned to S."
    )
    wb.set_content_block("prop:phi-b-unitary-bar-odd")
    # Required LP/SDP dual fields (AGENTS.md §LP/SDP first-class infra)
    wb.add_data("operator_selection_lp", {
        "t": [float(x) for x in t], "n_target": n_target,
        "active_set": active, "active_channels": [NF_NAMES[i] for i in active],
        "y0_star": y0, "y_star": y_star,
        "primal_obj": float(d.get("primal_obj", 0.0)),
        "dual_obj": float(d.get("dual_obj", 0.0)),
        "duality_gap": float(d.get("duality_gap", 0.0)),
        "binding_channel_shadow_price": binding_shadow,
        # Solver, precision, and full-precision decimals behind the f64 above.
        **provenance(r)})
    wb.add_data("why_lp_trivial", {
        "decay_ghost_tr_M": tr_decay, "tr_M_Lplus": float(t[3]), "tr_M_Lminus": float(t[4]),
        "note": "traceless decay mode invisible to linear trace-target LP"})
    wb.add_data("binding_is_quadratic", {
        "decay_gram_norm2": gnorm2,
        "conclusion": "binding = quadratic Gram/SDP negative-norm form; mass=linear tr_M; value needs z(q0)"})
    wb.add_assertion("lp_dual_trivial_binding_not_activated",
                     computed=abs(binding_shadow), expected=0.0, tolerance=1e-6,
                     source="operator-selection LP dual: binding channels have zero shadow price")
    wb.add_assertion("decay_ghost_traceless", computed=abs(tr_decay), expected=0.0,
                     tolerance=1e-9, source="tr_M(½(L₊−L₋))=0 (tr_M L₊ = tr_M L₋)")
    wb.add_assertion("binding_quadratic_negative_norm",
                     computed=1.0 if gnorm2 < 0 else 0.0, expected=1.0, tolerance=0.5,
                     source="decay ghost has negative Gram norm ⇒ binding is quadratic (SDP)")
    wb.save()

    print(f"\n  RESULT: {'ALL OK' if ok else 'CHECK'}  (binding located in SDP/quadratic layer; value open)")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
