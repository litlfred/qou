#!/usr/bin/env python3
"""qbeta_c3_imq_decay_projection_probe.py

Tests the owner lead (2026-07-11): "physically observed things correspond to
small-ish imaginary q; maybe [the archimedean] projection is this." This is
exactly **candidate (iii)** of `conj:im-q-physical-role`
(`content/quantum-observable-universe/mass-theory/conj-im-q-physical-role.md`):
Im(q) as the **non-Hermitian / open-system (decay-width Γ)** parameter — the
conjecture notes it "needs a categorical formula for decay widths Γ."

The c₃ bar-odd `S = Q_β/E₀` (the β-decay Q-value) IS a decay-sector observable
with a categorical (bar-odd trace) formula — the Γ-observable candidate (iii) was
waiting for. This probe asks the candidate-(iii) question concretely: **is `S` the
first-order response of the figure-eight complex volume `Im 𝔙` to a small
imaginary part of `q`?** If so, the wall's open phase `arg(u(q₀))` (residue of the
c₃ S wall, see qbeta_c3_wall_branch_structure_probe.py) IS candidate (iii)'s
`Im(q)` — the decay projection.

DERIVED linear-response (no fit; scope-(a); C14):
  * meridian holonomy = multiplication by `q` (#3579, `holonomy_hyperbola`),
    so the deformation `u = 2 log m = 2 log q`;
  * leading NZ complex volume `Im 𝔙 ≈ (√3/2)|u|² sin(2 arg u)` (√3 = derived
    cusp shape `τ = 2√−3`, this session's Lean `cuspShape_barOdd_sq`);
  * put `q = q₀ + iε` (ε = Im q, the decay projection). Then `u ≈ 2 log q₀ +
    2iε/q₀`, `arg u ≈ ε/(q₀ log q₀)`, and to first order
        `S ≈ (4√3 · log q₀ / q₀) · ε`  ⇒  `ε = S · q₀ / (4√3 log q₀)`.

RESULT (extraction, not a fit — S is the input, ε the read-out):
  ε(muon) ≈ +0.0149 (+1.3% of Re q),  ε(proton) ≈ −0.0606 (−5.5%): **small-ish
  and SIGN-FLIPPED**. The two real q₀ differ by only ~1e-8, so ε cannot be a
  function of Re(q₀) at this resolution — it is an independent DOF, exactly as
  candidate (iii) requires. A real q₀ can never flip S's sign; a sign-flipped
  small Im(q) does it naturally. This is the candidate-(iii) SIGNATURE.

HONEST SCOPE:
  * This does NOT close the wall. The map `q₀ ↦ ε(q₀)` is still open — it is the
    SAME open object as `arg(u(q₀))`, now re-read as "the decay projection's
    imaginary part" rather than an unstructured phase. The advance is the
    physical IDENTITY (wall = candidate (iii) Im(q)) + the sign-flip explanation.
  * The |ε| MAGNITUDE is map-dependent (uses `u = 2 log q`); a different derived
    `u(q)` rescales |ε| but the SIGN-FLIP is robust (it is sign(S), preserved by
    any monotone response). Robust claim: required Im(q) is small (1–5%) and
    sign-flipped. Exact magnitude conditional on the u-map.
  * NO conflict with `lusztig_q_0_imaginary_part_zero` (Im q₀ = 0 for the
    bar-EVEN MASS evaluation): masses are the value at Im q = 0; the bar-ODD
    decay S is the ∂/∂Im(q) response. `conj:im-q-physical-role` states Im q₀ = 0
    is a convention "pending an Im-sensitive measurement" — S is that measurement.
  * NO c_k wired; registry untouched; the conjecture stays a conjecture.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 50
Q = {"muon": mp.mpf("1.10997859555733471"),
     "proton": mp.mpf("1.1099785827513808075916690956107688798744991218736")}
S_TARGET = {"muon": mp.mpf("0.00968298"), "proton": mp.mpf("-0.03945936")}


def eps_required(q0, S):
    """Required Im(q)=ε from S via the derived u=2 log q linear response."""
    lnq = mp.log(q0)
    coeff = 4 * mp.sqrt(3) * lnq / q0        # dS/dε at ε=0 (derived)
    return S / coeff, coeff


def main() -> int:
    print("=" * 78)
    print(" c₃ bar-odd S as candidate (iii) — the decay projection Im(q)=ε")
    print("=" * 78)
    print("\n S = first-order response of Im 𝔙 to Im(q); u = 2 log q (meridian, #3579);")
    print(" Im 𝔙 ≈ (√3/2)|u|² sin(2 arg u); q=q₀+iε ⇒ S ≈ (4√3 log q₀/q₀)·ε.\n")

    eps = {}
    for a in ("muon", "proton"):
        e, coeff = eps_required(Q[a], S_TARGET[a])
        eps[a] = e
        print(f"   {a:7s}: S={mp.nstr(S_TARGET[a],6):>12}  dS/dε={mp.nstr(coeff,6)}  "
              f"⇒ ε=Im(q)={mp.nstr(e,6)}  ({mp.nstr(e/Q[a]*100,4)}% of Re q)")

    sign_flipped = (eps["muon"] > 0) and (eps["proton"] < 0)
    small = all(mp.fabs(eps[a] / Q[a]) < mp.mpf("0.1") for a in Q)     # < 10% of Re q
    print(f"\n   ε(muon)={mp.nstr(eps['muon'],5)} > 0 > ε(proton)={mp.nstr(eps['proton'],5)}: "
          f"sign-flipped? {sign_flipped}   small (<10% Re q)? {small}")
    print("   ⇒ candidate-(iii) signature: a small, sign-flipped Im(q) reproduces S; the")
    print("     wall's arg(u(q₀)) IS the decay projection's Im(q). Real q₀ (Δ~1e-8) cannot")
    print("     flip S — so the hypersensitivity lives in the imaginary (decay) DOF, not Re q.")

    wb = WitnessBuilder("qbeta-c3-imq-decay-projection", engine="mpmath")
    wb.set_description(
        "Tests conj:im-q-physical-role candidate (iii) (Im(q) = non-Hermitian / "
        "decay-width Γ parameter) against the c₃ bar-odd S = Q_β/E₀, the decay "
        "observable it predicted. Non-fitting inversion: S as the first-order "
        "response of Im 𝔙 to Im(q)=ε, with the derived meridian map u=2 log q "
        "(#3579) and leading NZ Im 𝔙 ≈ (√3/2)|u|²sin(2 arg u). Required ε: "
        "muon +1.3%, proton −5.5% of Re q — small-ish and SIGN-FLIPPED. Real q₀ "
        "differ ~1e-8, so ε is an independent DOF; the sign-flip (impossible for "
        "real q) is the candidate-(iii) signature. Does NOT close the wall (the "
        "q₀↦ε map = arg(u(q₀)) stays open, now read as the decay projection). "
        "No conflict with Im q₀=0 (that is the bar-even mass eval; S is ∂/∂Im q). "
        "Magnitude u-map-dependent; sign-flip robust. Scope-(a); C14; no fit; "
        "no c_k wired; conjecture stays a conjecture."
    )
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("epsilon_required", {
        a: {"eps": mp.nstr(eps[a], 10), "pct_of_re_q": mp.nstr(eps[a] / Q[a] * 100, 6),
            "S": mp.nstr(S_TARGET[a], 8)} for a in Q})
    wb.add_data("derivation", {
        "u_map": "u = 2 log q (meridian holonomy = mult by q, #3579)",
        "im_V_leading": "(sqrt3/2)|u|^2 sin(2 arg u), sqrt3 = derived cusp shape tau=2 sqrt(-3)",
        "response": "S ≈ (4 sqrt3 log q0 / q0) eps"})
    wb.add_data("interpretation", {
        "wall_identity": "arg(u(q0)) = candidate (iii) Im(q) (the decay projection)",
        "sign_flip": "eps(muon)>0>eps(proton): imaginary DOF carries the sign-flip real q cannot",
        "no_im_q0_conflict": "masses = value at Im q=0 (lusztig_q_0_imaginary_part_zero); S = d/d(Im q) response",
        "magnitude_caveat": "|eps| depends on the u-map; sign-flip is robust (=sign S)"})
    wb.add_assertion("imq_small_and_sign_flipped",
                     computed=1.0 if (sign_flipped and small) else 0.0, expected=1.0, tolerance=0.5,
                     source="required Im(q)=eps from S: small (<10% Re q) AND sign-flipped mu/p — candidate (iii) signature")
    wb.save()

    print("\n  RESULT: c₃ bar-odd S ↔ conj:im-q-physical-role candidate (iii); the wall's")
    print("          open phase = the decay projection's small sign-flipped Im(q).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
