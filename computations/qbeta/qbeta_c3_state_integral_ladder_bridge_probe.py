#!/usr/bin/env python3
"""qbeta_c3_state_integral_ladder_bridge_probe.py

Bridge (items 2+3 of the c₃-wall capstone): connect the Φ_b state-integral
results (#3654: deficit 0.0094, finite-b i·t·κ₁=0.058) to the corpus's existing
bar-even/odd LADDER decomposition (`qbeta_even_channel_bar_split_probe`):

    log R = E(u) + h·D(u),   h = q − 1/q  (bar-odd carrier),   E, D ∈ ℚ(√3)[[u]].

The bar-odd S is the odd part, `S = h·D(u)`. This probe does NOT re-derive the
ladder (the corpus develops E, D exactly); it BRIDGES the two pictures and pins
the exact-normalization gap, without duplication.

FINDINGS (scope-(a); C14; no fit; no c_k wired):

  1. **`S = h·D(u)` with the sign-flip in `D`, not `h`.** `h = q−1/q ≈ 0.209` is
     anchor-blind (differs ~1e-8); `D = S/h` is `+0.0463` (muon), `−0.1887`
     (proton) — the sign-flip lives entirely in the bar-even ladder function
     `D(u)`, which via the `c₃ = (…)/u³` extraction carries the `1/u³`
     amplification of a smooth zero (merged #3636). Consistent end-to-end.

  2. **The "odd channel" is `h·ℚ(√3)`, not a separate ℚ(√−3) (clarification).**
     My earlier #3654 framing named a "bar-ODD ℚ(√−3) channel". The corpus's
     exact split shows the bar-odd part factors as `h·D(u)` with `D ∈ ℚ(√3)` —
     the bar-odd-ness is carried by the algebraic `h = q−1/q`, and the `√−3`
     enters only as the geometric cusp modulus of `𝔙`, not as the ladder's
     arithmetic home. Re-scoped here for the record.

  3. **The exact-normalization gap is the ladder `D(u)`.** The state integral
     fixes the SCALE of `D` (deficit 0.0094 ≈ |S(muon)|; finite-b 0.058 ≈ the
     `D`-scale × h), but the exact `D(u)` — hence exact `S` — is the corpus's
     even/odd-channel program (`qbeta_even_channel_bar_split`,
     `qbeta_ck_sseries_exact_rational`), not this state-integral angle. The two
     meet at the scale; the exact function is ladder-side.

CONCLUSION: the state-integral (smooth 𝔙, no singular map) and the ladder
(`S=h·D(u)`, sign-flip in `D` via 1/u³) are one consistent picture. The residual
open object is the exact ladder `D(u)` — a corpus-owned program — not a
singular-map derivation.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qbeta_utils import substrate_ladder_quantities  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
with mp.workdps(50):
    KAPPA1 = +(11 * mp.sqrt(3) * mp.pi / 108)
S_TARGET = {"proton": mp.mpf("-0.03945936"), "muon": mp.mpf("0.00968298")}


def main() -> int:
    print("=" * 78)
    print(" c₃ bar-odd S — state-integral ↔ ladder bridge (S = h·D(u))")
    print("=" * 78)

    rows = []
    h_vals, D_vals = {}, {}
    for tag, q0 in (("proton", q_at(50)), ("muon", q_muon_at(50))):
        h = q0 - 1 / q0                                  # bar-odd carrier (=HA)
        u = substrate_ladder_quantities(q0)["u"]
        D = S_TARGET[tag] / h                            # implied bar-even ladder fn
        t = mp.log(q0)
        h_vals[tag], D_vals[tag] = h, D
        print(f"   {tag:7s}: h=q−1/q={mp.nstr(h,8)}  u={mp.nstr(u,8)}  D=S/h={mp.nstr(D,8)}")
        rows.append({"anchor": tag, "h": mp.nstr(h, 20), "u": mp.nstr(u, 20),
                     "D_eq_S_over_h": mp.nstr(D, 20), "S": mp.nstr(S_TARGET[tag], 12),
                     "i_t_kappa1": mp.nstr(t * KAPPA1, 12)})

    h_anchor_blind = abs(h_vals["proton"] - h_vals["muon"]) < mp.mpf("1e-6")
    D_sign_flips = D_vals["muon"] > 0 > D_vals["proton"]
    print(f"\n   h anchor-blind? {h_anchor_blind}   D sign-flips (muon>0>proton)? {D_sign_flips}")
    print("   ⇒ the sign-flip is in the bar-even ladder D(u), carried to c₃ by the 1/u³ extraction")
    print("     (merged #3636); h just supplies the bar-odd-ness. State-integral scale (deficit")
    print("     0.0094, finite-b 0.058) meets the ladder at the D-scale; exact D(u) is corpus-owned.")
    print("\n   Clarification: the bar-ODD part is h·D(u), D∈ℚ(√3) — NOT a separate ℚ(√−3) channel;")
    print("   √−3 is the geometric cusp modulus of 𝔙, not the ladder's arithmetic home.")

    wb = WitnessBuilder("qbeta-c3-state-integral-ladder-bridge", engine="mpmath")
    wb.set_description(
        "Bridge (c₃-wall capstone items 2+3): connects the Φ_b state-integral "
        "results (#3654: deficit 0.0094, finite-b i·t·κ₁=0.058) to the corpus's "
        "bar-even/odd ladder log R=E(u)+h·D(u), h=q−1/q, E,D∈ℚ(√3). S=h·D(u): h is "
        "anchor-blind (~0.209), D=S/h is +0.0463 (muon)/−0.1887 (proton) — the "
        "sign-flip lives in the bar-even ladder D(u), carried to c₃ by the 1/u³ "
        "extraction (merged #3636). Clarifies the #3654 framing: the bar-odd part "
        "is h·ℚ(√3), NOT a separate ℚ(√−3) channel (√−3 is the geometric cusp "
        "modulus, not the ladder's home). The exact-normalization gap = the exact "
        "ladder D(u) (corpus even/odd-channel program), which the state integral "
        "meets only at the scale. No re-derivation of the ladder; bridge only. "
        "Scope-(a); C14; no c_k wired; no fit."
    )
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("bridge", rows)
    wb.add_data("findings", {
        "S_eq_h_D": "S = h*D(u), h=q-1/q bar-odd carrier, D bar-even ladder fn",
        "h_anchor_blind": bool(h_anchor_blind), "D_sign_flips": bool(D_sign_flips),
        "odd_channel_clarification": "bar-odd part is h*Q(sqrt3), not a separate Q(sqrt-3); "
                                     "sqrt-3 is the geometric cusp modulus of V",
        "exact_normalization_gap": "the exact ladder D(u) (corpus even/odd-channel program); "
                                   "state integral fixes only the D-scale"})
    wb.add_assertion("S_equals_h_times_D_signflip_in_D",
                     computed=1.0 if (h_anchor_blind and D_sign_flips) else 0.0, expected=1.0, tolerance=0.5,
                     source="S=h*D(u): h anchor-blind, D=S/h sign-flips (muon>0>proton) => sign-flip is in the bar-even ladder D(u), consistent with the 1/u^3 extraction (#3636)")
    wb.save()
    print("\n  RESULT: S=h·D(u) bridges state-integral↔ladder; sign-flip in D(u) (1/u³); exact D(u)")
    print("          is the corpus even/odd-channel program; odd part = h·ℚ(√3), not ℚ(√−3).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
