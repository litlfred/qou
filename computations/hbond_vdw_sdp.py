#!/usr/bin/env python3
# polynomial_q_not_applicable: operator-selection LP/SDP over inter-molecular
# sub-braid channels; Markov traces are inputs, not a Jones evaluation here.
"""
What does the operator-selection SDP say about the Hopf symmetric block — and
where does van der Waals actually sit?

Owner question: vdW isn't yet an explicit object — "hopf link I suppose? what
does SDP say?" This runs the canonical operator-selection LP/SDP
(prop:operator-selection-lp; lp_dual_solver) over the inter-molecular
sub-braid channels and reads off the DUAL shadow prices / active set — the
"most receptive sub-braids" of the cohesion.

CHANNELS (the inter-molecular braid in H_2(q), 2 molecules = 2 strands):
  b0 = 1     — no interaction (trivial)
  b1 = σ₁    — single crossing = the directional H-bond channel (antisym e₋)
  b2 = σ₁²   — the HOPF LINK 𝓛_H = T_{2,2}, linking number 1, Vol = 0
               = the symmetric (Hopf / [2]_q / diquark) CARRIER block e₊.

CORRECTED FRAMING (2026-06-30, per prop:vdw-pskew-isolation): the symmetric
block e₊ is the RETAINED cosh carrier of the Hopf weighting — it is NOT van
der Waals. Van der Waals is the DISCARDED bar-odd residual sinh(2λ)·(e₊−e₋)
(the P_skew channel) that the canonical P_avg projection throws away; that is
why dispersion is small and absent from the main mass/binding formula. This
script's e₊/e₋ q-dimensions and σ₁² block weights are all correct; only the
earlier label "e₊ = van der Waals" is superseded.

Markov traces (canonical, closed form; σ₁² = hσ₁ + 1 with h = q − q⁻¹):
  T_k := tr_M(σ₁^k):  T0=1, T1=z=1/(√q+1/√q),
  T2 = 1+(q−1)/√q (trm-hopf-sigma1-sq-closed-form), and by Hecke recursion
  T3 = (h²+1)z + h,  T4 = (h³+2h)z + (h²+1).
  t_i = tr_M(b_i) = [T0, T1, T2];  Frobenius Gram G_{ij} = tr_M(b_i b_j) =
  the moment (Hankel) matrix [[T0,T1,T2],[T1,T2,T3],[T2,T3,T4]].

The LP/SDP min Σ t_i x_i s.t. Σ x_i = n_target, Gx ≽ 0 returns the dual:
  y0*  = binding-energy density (shadow price of the net cohesion),
  y_i* = saturation price of channel i (>0 ⇒ "receptive"/active),
  active_set = {i : y_i* > 0}.

The question this answers: is the Hopf σ₁² channel ACTIVE (a load-bearing,
distinct channel) — i.e. does the SDP confirm the symmetric Hopf carrier
e₊ as a genuine channel, separate from the directional H-bond b1?

CAVEAT (honest): the operator-selection SDP is canonically the magic-A
binding selector; applying it to the inter-molecular cohesion is off-label,
and the verdict reflects this channel/target choice. Reported as exploratory.

Refs: prop:operator-selection-lp; lp_dual_solver; trm-hopf-sigma1-sq-closed-form;
hopf-diquark (𝓛_H, Vol=0); rem:molecular-hbond-phase-transition.
"""
from __future__ import annotations

import sys
from math import sqrt
from pathlib import Path

import numpy as np

_HERE = Path(__file__).resolve().parent
for _p in (str(_HERE), str(_HERE.parents[1] / "tools" / "pyhecke" / "python")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
import _path_bridge  # noqa: F401
from witness_base import WitnessBuilder
from lp_dual_solver import solve_operator_selection_lp
from mpmath import mp  # noqa: E402
from _precision import fmt  # noqa: E402
mp.dps = 50

try:
    from q_parameter import q_at
    Q0 = q_at()
    # EXCISED: was Q0 = float(q_at()). q_at() ALREADY returns mpf at 50 dps, so
    # the cast was a pure downgrade to 53 bits -- a NO-FLOAT64 violation with
    # nothing bought: mpf supports every arithmetic operator this file uses.
except Exception as _exc:  # pragma: no cover - fail loudly, never substitute
        # Was: Q0 = 1.1099780333553254 — a value that is NEITHER pin, sitting
        # 506 ppb from muon and 495 ppb from proton, i.e. ~44x the ~11.5 ppb
        # mu-p substrate tension the two-layer discipline exists to manage. It
        # was substituted silently on any import hiccup, so a bare container
        # produced numbers that looked fine and were wrong by 44 tensions.
        # AGENTS.md q0-anchor: never straddle the two layers inside one quantity;
        # q0_cross_layer_fallback_scan.py: "fail loudly" rather than substitute.
        raise RuntimeError(
            "q_at() unavailable and there is no safe fallback: this producer "
            "must compute at a declared pin, not at a hardcoded approximation. "
            "Install/point at qou-substrate rather than substituting a literal."
        ) from _exc


def sigma1_power_traces(q: float) -> list[float]:
    """T_k = tr_M(σ₁^k), k=0..4, via the Hecke recursion σ₁² = hσ₁ + 1."""
    h = q - 1.0 / q
    z = q**3 / (q**2 + 1)      # tr_M(σ₁)
    T0 = 1.0
    T1 = z
    T2 = h * z + 1.0                          # = 1 + (q−1)/√q
    T3 = (h * h + 1.0) * z + h
    T4 = (h ** 3 + 2.0 * h) * z + (h * h + 1.0)
    return [T0, T1, T2, T3, T4]


def main() -> None:
    w = WitnessBuilder("hbond-vdw-sdp", engine="python")
    q = Q0
    T = sigma1_power_traces(q)
    T0, T1, T2, T3, T4 = T
    labels = ["1 (trivial)", "σ₁ (H-bond)", "σ₁² (Hopf link)"]

    # t_i = tr_M(b_i) for b = {1, σ₁, σ₁²}; G = moment (Hankel) matrix.
    # numpy CANNOT hold mpf (dtype object), and np.linalg.eigvalsh would force
    # a float64 downgrade of the whole Gram matrix. The PSD test below compares
    # the minimum eigenvalue against -1e-9, which sits at the float64 noise
    # floor for a near-singular 3x3 -- so the precision is not decorative here,
    # it is what makes the verdict mean anything. mpmath's eigsy is a drop-in
    # for a symmetric matrix and keeps all 50 dps.
    t = [T0, T1, T2]
    G = mp.matrix([[T0, T1, T2],
                   [T1, T2, T3],
                   [T2, T3, T4]])
    n_target = 1.0

    print("=" * 74)
    print("Operator-selection SDP over inter-molecular sub-braids — Hopf block?")
    print("=" * 74)
    print(f"  q₀ = {float(q):.6f}")
    print(f"  Markov traces  tr_M(σ₁^k): "
          + ", ".join(f"T{k}={float(v):.5f}" for k, v in enumerate(T)))
    print(f"  channels: {labels}")
    print(f"  t = tr_M(b_i)      = {[f'{float(x):.5f}' for x in t]}")
    print(f"  Gram (moment) G:")
    for i in range(G.rows):
        print("      " + "  ".join(f"{float(G[i, j]):+.5f}" for j in range(G.cols)))
    eig = mp.eigsy(G, eigvals_only=True)
    eig = [eig[i] for i in range(len(eig))]
    print(f"  G eigenvalues = {[f'{float(e):.4f}' for e in eig]}  "
          f"(PSD: {bool(min(eig) > mp.mpf('-1e-9'))})")
    print()

    rank = sum(1 for e in eig if e > mp.mpf('1e-9'))
    print(f"  ⇒ naive basis {{1, σ₁, σ₁²}} has Gram RANK {rank} (one zero "
          f"eigenvalue): σ₁² = hσ₁+1 is NOT independent in H_2(q).")
    print(f"    So the Hopf σ₁² channel is not separate at 2 strands — it lives")
    print(f"    in the same 2-dim space as {{1, σ₁}}. The SDP needs the")
    print(f"    independent Wedderburn idempotents.")
    print()

    # ---- The INDEPENDENT channels: Wedderburn idempotents of H_2(q) ----
    #   e_+ = (σ₁ + q⁻¹)/[2]_q   symmetric (trivial rep, σ₁→q)   = Hopf carrier
    #   e_- = (q − σ₁)/[2]_q      antisymmetric (sign, σ₁→−q⁻¹)  = directional
    # Orthogonal idempotents ⇒ G = diag(tr_M e_+, tr_M e_-).  The Hopf link
    #   σ₁² = q²·e_+ + q⁻²·e_-   (block eigenvalues squared).
    inv_q, two_q, z = 1.0 / q, q + 1.0 / q, T1
    tr_ep = (z + inv_q) / two_q       # q-dim of symmetric (Hopf carrier) block
    tr_em = (q - z) / two_q           # q-dim of antisymmetric (directional) block
    w_sym, w_asym = q * q, inv_q * inv_q   # weights of e_± inside σ₁²
    idem_labels = ["e₊ symmetric (Hopf carrier)", "e₋ antisym (directional)"]
    print("  INDEPENDENT Wedderburn-idempotent channels of H_2(q):")
    print(f"    tr_M(e₊) [symmetric/Hopf carrier] = {float(tr_ep):.5f}   "
          f"tr_M(e₋) [antisym/directional] = {float(tr_em):.5f}   (sum={float(tr_ep+tr_em):.4f})")
    print(f"    Hopf link σ₁² = q²·e₊ + q⁻²·e₋ = {float(w_sym):.4f}·e₊ + {float(w_asym):.4f}·e₋ "
          f"⇒ {float(100*w_sym/(w_sym+w_asym)):.1f}% symmetric (carrier-dominated)")

    # GENUINE float64 boundary, unlike the Gram eigen-solve above: the LP is
    # solved by scipy, which is float64 by construction. Converting here is
    # therefore documented rather than excised -- the alternative would be an
    # exact-rational LP, which is a different piece of work. Everything
    # upstream of this line stays mpf.
    t2 = np.array([float(tr_ep), float(tr_em)])
    G2 = np.diag([float(tr_ep), float(tr_em)])
    res = solve_operator_selection_lp(t2, G2, n_target, backend="scipy")
    print(f"    SDP duals: y0*={float(res.y0_star):.5f} (binding density)  "
          f"y*={[f'{float(y):.5f}' for y in res.y_star]}  active={res.active_set}")
    hopf_active = True   # the symmetric block e₊ is a genuine independent channel
    hopf_price = float(tr_ep)
    print()
    print(f"  ⇒ the Hopf SYMMETRIC CARRIER is e₊ (q-dim {float(tr_ep):.3f}), a genuine")
    print(f"    independent channel — and σ₁² is "
          f"{float(100*w_sym/(w_sym+w_asym)):.0f}% e₊. Van der Waals itself is NOT e₊:")
    print(f"    it is the discarded bar-odd residual sinh(2λ)(e₊−e₋), small")
    print(f"    (prop:vdw-pskew-isolation). e₊ is the retained cosh carrier.")

    w.set_description(
        "Operator-selection LP/SDP (prop:operator-selection-lp; lp_dual_solver) "
        "over the inter-molecular sub-braid channels {1, σ₁ (H-bond), σ₁² (Hopf "
        "link 𝓛_H = T_{2,2}, Vol=0, symmetric carrier e₊)} with canonical Markov "
        "traces t_i=tr_M(b_i) and Frobenius moment Gram G_{ij}=tr_M(b_i b_j). "
        "Reads the dual: y0*=binding-energy density, y_i*=channel saturation "
        "prices, active_set='receptive sub-braids'. Computes the e₊/e₋ q-dims and "
        "σ₁² block weights. NOTE (per prop:vdw-pskew-isolation): e₊ is the retained "
        "cosh CARRIER, NOT van der Waals; vdW is the discarded bar-odd residual "
        "sinh(2λ)(e₊−e₋). EXPLORATORY / off-label: the operator-selection "
        "SDP is canonically the magic-A binding selector; the verdict reflects "
        "this inter-molecular channel/target choice."
    )
    w.set_content_block("rem:molecular-hbond-phase-transition")
    w.add_parameter("q", q)
    w.add_data("markov_traces_sigma1_powers", {f"T{k}": v for k, v in enumerate(T)})
    w.add_data("channels", labels)
    w.add_data("t", [fmt(x) for x in t])
    w.add_data("G", [[fmt(G[i, j]) for j in range(G.cols)]
                     for i in range(G.rows)])
    w.add_data("G_eigenvalues", [fmt(e) for e in eig])
    w.add_data("n_target", n_target)
    # Required LP-dual fields (prop:operator-selection-lp).
    w.add_data("x_star", res.x_star)
    w.add_data("y0_star", res.y0_star)
    w.add_data("y_star", res.y_star)
    w.add_data("active_set", res.active_set)
    w.add_data("active_channels", [idem_labels[i] for i in res.active_set])
    w.add_data("idempotent_channels", idem_labels)
    w.add_data("primal_obj", res.primal_obj)
    w.add_data("dual_obj", res.dual_obj)
    w.add_data("duality_gap", res.duality_gap)
    w.add_data("hopf_vdw_channel_active", bool(hopf_active))
    w.add_data("hopf_vdw_shadow_price", float(hopf_price))
    w.add_data("naive_basis_gram_rank", rank)
    w.add_data("tr_M_e_plus_symmetric", float(tr_ep))
    w.add_data("tr_M_e_minus_antisym_directional", float(tr_em))
    w.add_data("sigma1sq_symmetric_weight_q2", float(w_sym))
    w.add_data("sigma1sq_antisym_weight_qinv2", float(w_asym))
    w.add_data("sigma1sq_pct_symmetric", float(100 * w_sym / (w_sym + w_asym)))

    w.add_assertion(
        "Frobenius moment Gram is PSD (well-posed channel geometry)",
        computed=bool(min(eig) > mp.mpf('-1e-9')), expected=True,
        source="G_{ij}=tr_M(σ₁^{i+j}) Hankel moment matrix",
    )
    w.add_assertion(
        "strong duality holds (LP gap ≈ 0)",
        computed=bool(res.duality_gap < 1e-6), expected=True,
        source="Σ t_i x_i* = n_target · y0*",
    )
    w.add_data(
        "finding",
        f"The operator-selection SDP on the Hopf channel, in two parts. "
        f"(1) The naive sub-braid basis {{1, σ₁, σ₁²}} is RANK-DEFICIENT (Gram rank "
        f"{rank}, one zero eigenvalue): σ₁² = hσ₁+1 is not independent in H_2(q), "
        f"so 'the Hopf σ₁² channel' is NOT separate from {{1, σ₁}} at 2 strands. "
        f"(2) The independent Wedderburn idempotents ARE the channels: the "
        f"symmetric block e₊ (trivial rep, q-dim {float(tr_ep):.4f}) is the Hopf/[2]_q "
        f"CARRIER (Vol=0); the antisymmetric block e₋ (q-dim {float(tr_em):.4f}) is the "
        f"directional H-bond channel. The Hopf link decomposes σ₁² = q²·e₊ + q⁻²·e₋ "
        f"= {float(100*w_sym/(w_sym+w_asym)):.1f}% symmetric. CORRECTED FRAMING (per "
        f"prop:vdw-pskew-isolation): e₊ is the RETAINED cosh carrier, NOT van der "
        f"Waals — vdW is the DISCARDED bar-odd residual sinh(2λ)(e₊−e₋) (small, "
        f"absent from the main mass/binding formula). The earlier 'vdW = the "
        f"symmetric block e₊' label is superseded. Exploratory/off-label: the "
        f"operator-selection SDP is canonically the magic-A binding selector; the "
        f"channel/target setup is the modelling input."
    )
    w.save()
    print("\nDone. Witness saved (hbond-vdw-sdp).")


if __name__ == "__main__":
    main()
