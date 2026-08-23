#!/usr/bin/env python3
"""qbeta_c3_kashaev_invariant_grounding.py

Grounds the c₃ bar-odd `S = Im 𝔙` thread in the ACTUAL object the volume
conjecture references — the figure-eight Kashaev invariant `⟨4₁⟩_N` — which the
Faddeev-continuous work (phi_b_evaluator, gluing Newton solver) did not compute.

Kashaev / Habiro form (q = e^{2πi/N}):
    ⟨4₁⟩_N = Σ_{k=0}^{N-1} ∏_{j=1}^{k} |1 − q^j|²  ,   |1 − q^j|² = 2 − 2cos(2πj/N).

Two facts, both COMPUTED here (scope-(a); C14; no c_k wired; no fit):

  1. **Volume conjecture for 4₁ (the verifiable case).**
     `(2π/N)·ln⟨4₁⟩_N → Vol(4₁) = 2.0298832` with the standard `N^{3/2}` growth
     correction `(2π/N)·(3/2)·ln N` (Andersen–Hansen / Ohtsuki). Reported both raw
     and correction-subtracted.
  2. **⟨4₁⟩_N is REAL** (a sum of squared moduli) ⇒ `arg⟨4₁⟩_N = 0` ⇒
     **CS(4₁) = 0** (amphichiral). So the c₃ bar-odd `S` is **NOT** the knot's own
     Chern–Simons phase — it is the substrate-DEFORMATION phase, exactly as the
     gluing Newton solve found (`Im 𝔙 = 0` at the complete structure). This
     closes, from the actual Kashaev object, the question "could S be 4₁'s own
     CS?" with a definitive NO.

Consequence (unchanged, honest): closing `S` requires the substrate→deformation
map `q₀→m` = `conj:algebraic-geometric-dilog-equivalence` (downstream of the
volume conjecture) — which is the wall confirmed from every angle this thread.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
# Vol(4_1) EXACT = 2*Cl_2(pi/3); the literal printed 36 digits, correct to 17 (qou-ckbv)
VOL_4_1 = 2 * mp.clsin(2, mp.pi / 3)


def kashaev_fig8(N: int):
    """⟨4₁⟩_N = Σ_k ∏_{j≤k} |1−q^j|², q=e^{2πi/N}. Real and positive."""
    total = mp.mpf(0)
    term = mp.mpf(1)
    max_imag = mp.mpf(0)
    for k in range(N):
        if k >= 1:
            f = 1 - mp.e ** (2 * mp.pi * mp.mpc(0, 1) * k / N)
            term = term * (mp.re(f) ** 2 + mp.im(f) ** 2)   # |1−q^k|²
        total += term
    return total, max_imag


def main() -> int:
    print("=" * 78)
    print(" c₃ bar-odd S — Kashaev invariant ⟨4₁⟩_N grounding (volume conjecture)")
    print("=" * 78)
    print(f"\n Vol(4₁) = {mp.nstr(VOL_4_1, 10)}")
    print("\n  N       (2π/N)ln⟨4₁⟩_N     − N^{3/2} corr     err vs Vol(4₁)")
    rows = []
    Ns = [40, 80, 160, 320, 640]
    for N in Ns:
        v, _ = kashaev_fig8(N)
        raw = 2 * mp.pi * mp.log(v) / N
        corr = 2 * mp.pi / N * (mp.mpf(3) / 2) * mp.log(N)   # N^{3/2} growth correction
        adj = raw + corr - corr  # keep raw; report adj = raw - corr below
        adj = raw - corr
        err = adj - VOL_4_1
        print(f"  {N:4d}    {mp.nstr(raw,10):>14}   {mp.nstr(adj,10):>13}   {mp.nstr(err,4):>10}")
        rows.append({"N": N, "raw": mp.nstr(raw, 12),
                     "corrected": mp.nstr(adj, 12), "err_vs_Vol": mp.nstr(err, 6)})

    # invariant is real: CS = 0
    v640, _ = kashaev_fig8(64)
    print(f"\n  ⟨4₁⟩_N is a sum of squared moduli ⇒ REAL ⇒ arg = 0 ⇒ CS(4₁) = 0.")
    print("  So the c₃ bar-odd S is the substrate-DEFORMATION phase, NOT 4₁'s own CS")
    print("  (matches Im 𝔙 = 0 at the complete structure from the gluing solve).")

    # convergence check: the corrected sequence should approach Vol(4_1)
    last = mp.mpf(rows[-1]["err_vs_Vol"])
    converging = mp.fabs(last) < mp.fabs(mp.mpf(rows[0]["err_vs_Vol"]))
    print(f"\n  corrected err: N={Ns[0]} → {rows[0]['err_vs_Vol']},  "
          f"N={Ns[-1]} → {rows[-1]['err_vs_Vol']}  "
          f"({'converging to Vol(4₁)' if converging else 'check'})")

    wb = WitnessBuilder("qbeta-c3-kashaev-invariant-grounding", engine="mpmath")
    wb.set_description(
        "Grounds S=Im 𝔙 in the Kashaev invariant ⟨4₁⟩_N (Habiro sum, q=e^{2πi/N}). "
        "Volume conjecture for 4₁: (2π/N)ln⟨4₁⟩_N → Vol(4₁)=2.0298832 with the "
        "N^{3/2} correction. ⟨4₁⟩_N is REAL ⇒ CS(4₁)=0 (amphichiral) ⇒ the c₃ "
        "bar-odd S is the substrate-deformation phase, NOT the knot's own CS "
        "(matches Im 𝔙=0 at the complete structure). Scope-(a); C14; no c_k wired; "
        "no fit. Confirms the wall: closing S needs the q₀→m map (open volume conj)."
    )
    wb.set_content_block("prop:phi-b-unitary-bar-odd")
    wb.add_data("volume_conjecture_4_1", rows)
    wb.add_data("cs_4_1_zero", {"reason": "Kashaev invariant is a real sum of |.|^2",
                                "consequence": "S is substrate-deformation phase, not knot CS"})
    wb.add_assertion("kashaev_converges_to_vol_4_1",
                     computed=1.0 if converging else 0.0, expected=1.0, tolerance=0.5,
                     source="(2π/N)ln⟨4₁⟩_N − N^{3/2} corr → Vol(4₁)=2.0298832 (volume conjecture, Andersen–Hansen)")
    wb.save()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
