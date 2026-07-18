#!/usr/bin/env python3
"""qbeta_dladder_fibre_branch_stokes_ambiguity_probe.py

The c3 D-ladder Écalle thread's ONE non-duplicative compute gap (survey 2026-07-18):
EVERY prior acceleration probe evaluates the D-ladder at the SUBSTRATE MERIDIAN
(real u~0.0095), where the least-term Stokes ambiguity is provably suppressed and
anchor-blind (the #3818 Phi_b "M4" negative: least term sits at the k=KMAX edge,
optimal truncation k*~1e13, jump exp(-A/u) ~ 1e-27). The Phi_b resummation verdict
names the FIBRE branch (|q|=1, u~O(1)) as the place the UNSUPPRESSED Stokes datum
A_omega would live -- and states it is "NOT produced here."

This probe LEAVES the substrate meridian. It evaluates the exact Q(sqrt3) D-ladder
along the fibre q = e^{i th} (th: small -> pi), where the generating-function
variable u~(th) = q * b * hbar_q^2 is COMPLEX and |u~| grows from ~0.0095 to O(1).
It measures, as a function of |u~|:

  * delta_np(th) = min_k |d_k * u~^k|   -- the optimal-truncation least-term
    ambiguity = the Stokes-jump magnitude;
  * N*(th) = argmin_k |d_k u~^k|, and whether it has LEFT the k=KMAX edge
    (edge => ambiguity still suppressed; interior => genuine divergence);
  * D_opt(th) = optimal-truncation partial sum, and S_pred = h * D_opt
    (h = q - 1/q, the #3654 bridge) -- does |Im S_pred| reach the S/N_odd scale?

Formalize-first structural prediction: the least term leaves the edge when
|u~| exceeds the last-ratio radius r* = |d_{KMAX-1} / d_{KMAX}| (beyond which
|d_k u~^k| increases at the top of the ladder). This is the "unsuppression
threshold" -- computed exactly and checked against the measured crossing.

QUESTION (scope-(a) MEASUREMENT, not a closure): does the D-ladder Stokes ambiguity
become O(1)/unsuppressed on the fibre, as the Phi_b verdict predicts, and does
|Im(h.D)| cross the S scale (~0.01-0.04) anywhere? DISCIPLINE: no fit (nothing tuned
to CODATA), no c_k wired, nothing to production, no tier change. Reuses the exact d_k
(build_d_ladder) + canonical substrate quantities.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from qbeta_utils import substrate_ladder_quantities  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402

# generating-function module reads ORD from sys.argv at import time
ORD = int(sys.argv[1]) if len(sys.argv) > 1 else 63
sys.argv = [sys.argv[0], str(ORD)]
import qbeta_dladder_generating_function_structure_probe as dlad  # noqa: E402

mp.mp.dps = 50
S_SCALE = mp.mpf("0.0097")          # |S(muon)| reference magnitude (the swing scale)


def to_mpf(v):
    return mp.mpf(str(sp.N(v, 46)))


def main() -> int:
    print("building exact D-ladder at ORD=%d ..." % ORD, flush=True)
    dk_sym, KMAX, valid_top, odd_ok = dlad.build_d_ladder()
    dk = {k: to_mpf(dk_sym[k]) for k in dk_sym if k >= 1}
    KMAX = max(dk)
    print(f"  KMAX={KMAX}  valid_top={valid_top}  odd_ok={odd_ok}", flush=True)

    # canonical substrate reference: b from u_sub = b * hbar_q^2, hbar_q = 1 - 1/q0
    q0 = q_at(50)
    u_sub = substrate_ladder_quantities(q0)["u"]
    hbar0 = 1 - 1 / q0
    b = u_sub / hbar0 ** 2
    u_mer_sub = q0 * u_sub                       # the real substrate meridian u~
    print(f"  q0={mp.nstr(q0,12)}  u_sub={mp.nstr(u_sub,8)}  b={mp.nstr(b,10)}  "
          f"u~_substrate={mp.nstr(u_mer_sub,8)}", flush=True)

    def stokes_at(u_tilde):
        """optimal-truncation least-term data at a (possibly complex) u~."""
        terms = {k: dk[k] * u_tilde ** k for k in dk}
        Nstar = min(terms, key=lambda k: abs(terms[k]))
        delta = abs(terms[Nstar])
        edge = (Nstar == KMAX)
        Dopt = mp.fsum(terms[k] for k in dk if k <= Nstar)
        return Nstar, delta, edge, Dopt

    # --- structural prediction: unsuppression threshold r* = |d_{KMAX-1}/d_{KMAX}|
    r_star = abs(dk[KMAX - 1] / dk[KMAX])
    print(f"\n  structural unsuppression threshold r* = |d_{KMAX-1}/d_{KMAX}| "
          f"= {mp.nstr(r_star,8)}", flush=True)

    # --- substrate reference (real q0): confirm the M4 edge/suppressed picture
    Ns_sub, d_sub, edge_sub, D_sub = stokes_at(u_mer_sub)
    print(f"\n  SUBSTRATE (real q0):  |u~|={mp.nstr(abs(u_mer_sub),8)}  N*={Ns_sub}"
          f"{'(edge)' if edge_sub else ''}  delta_np={mp.nstr(d_sub,6)}", flush=True)

    # --- FIBRE sweep: q = e^{i th}, th from just above 0 to pi ------------------
    print("\n  FIBRE branch  q=e^{i th}:  |u~|, N*, delta_np(=Stokes ambiguity), "
          "|Im(h.D)|", flush=True)
    rows = []
    left_edge_at = None
    max_abs_imS = mp.mpf(0)
    crossed_S_scale = False
    thetas = [mp.pi * mp.mpf(j) / 40 for j in range(1, 41)]   # (0, pi]
    for th in thetas:
        q = mp.e ** (1j * th)
        hbar = 1 - 1 / q
        u_tilde = q * b * hbar ** 2                  # complex on the fibre
        h = q - 1 / q                                # bridge factor = 2 i sin(th)
        Nstar, delta, edge, Dopt = stokes_at(u_tilde)
        S_pred = h * Dopt
        imS = abs(mp.im(S_pred))
        au = abs(u_tilde)
        rows.append({"theta": mp.nstr(th, 6), "abs_u": mp.nstr(au, 8),
                     "Nstar": Nstar, "edge": bool(edge),
                     "delta_np": mp.nstr(delta, 8), "abs_D": mp.nstr(abs(Dopt), 8),
                     "abs_imS": mp.nstr(imS, 8)})
        if (not edge) and left_edge_at is None:
            left_edge_at = au
        if imS > max_abs_imS:
            max_abs_imS = imS
        if imS >= S_SCALE:
            crossed_S_scale = True
        if th <= mp.pi * mp.mpf("0.5") or (float(th) * 40 / float(mp.pi)) % 4 < 1:
            print(f"    th={float(th):.3f}  |u~|={mp.nstr(au,6):>10}  N*={Nstar:>2}"
                  f"{' edge' if edge else '     '}  d_np={mp.nstr(delta,5):>11}  "
                  f"|ImS|={mp.nstr(imS,5):>11}", flush=True)

    # --- summary + verdict ------------------------------------------------------
    fibre_unsuppressed = (left_edge_at is not None)
    print(f"\n  least term LEAVES the k={KMAX} edge at |u~| = "
          f"{mp.nstr(left_edge_at,8) if left_edge_at else 'never (<= pi)'}  "
          f"(structural r*={mp.nstr(r_star,6)})", flush=True)
    print(f"  max |Im(h.D)| over the fibre = {mp.nstr(max_abs_imS,8)}  "
          f"(S scale ~ {mp.nstr(S_SCALE,4)})", flush=True)

    # kill criteria: exact ladder; substrate edge reproduced; threshold matches r*
    substrate_suppressed = bool(edge_sub)
    threshold_matches_rstar = (left_edge_at is not None and
                               abs(left_edge_at / r_star - 1) < mp.mpf("0.5"))

    verdict = (
        f"FIBRE-BRANCH STOKES AMBIGUITY MEASURED (scope-(a); leaves the substrate "
        f"meridian for the first time). On the substrate (real q0) the least term is "
        f"{'at the k=%d edge (suppressed/anchor-blind, reproduces #3818 M4)' % KMAX if substrate_suppressed else 'INTERIOR (unexpected)'}. "
        f"On the fibre q=e^{{i th}}, the ambiguity delta_np "
        f"{'BECOMES UNSUPPRESSED: the least term leaves the edge at |u~|=%s (structural threshold r*=|d_{KMAX-1}/d_KMAX|=%s%s), so the Stokes jump is O(1) at |u~|~O(1) -- CONFIRMING the Phi_b prediction that A_omega lives on the fibre, NOT the substrate meridian. This NARROWS the c3/A_omega search to the fibre-branch accelero-summation.' % (mp.nstr(left_edge_at,6), mp.nstr(r_star,6), ', matches' if threshold_matches_rstar else ', order-of-mag') if fibre_unsuppressed else 'stays edge-suppressed even to th=pi -- the fibre does NOT unsuppress the ambiguity in this window (negative).'} "
        f"Max |Im(h.D)| over the fibre = {mp.nstr(max_abs_imS,6)} ("
        f"{'REACHES the |S|~%s swing scale at some th -- a location, NOT an identification (no fit; the anchor-dependent value still requires the accelero-summation, not this optimal-truncation floor)' % mp.nstr(S_SCALE,3) if crossed_S_scale else 'does not reach the |S|~%s scale via optimal truncation alone' % mp.nstr(S_SCALE,3)}). "
        f"SCOPE: measures WHERE the ambiguity is unsuppressed; derives no c3 value, "
        f"wires nothing, no tier change. The genuine non-commutative Écalle accelerator "
        f"(two critical times) is still required to produce the value -- this probe only "
        f"establishes the branch it must be run on."
    )
    print("\nVERDICT:", verdict, flush=True)

    wb = WitnessBuilder("qbeta-dladder-fibre-branch-stokes-ambiguity", engine="mpmath")
    wb.set_description(
        "Leave the substrate meridian: measure the D-ladder optimal-truncation Stokes "
        "ambiguity delta_np=min_k|d_k u~^k| along the fibre q=e^{i th} where u~ is "
        "complex and |u~| grows to O(1). Tests the Phi_b prediction that the ambiguity "
        "is unsuppressed on the fibre (A_omega home), suppressed on the substrate.")
    wb.set_audit_only("docs/audits/2026-07-18-dladder-fibre-branch-stokes-ambiguity.md")
    wb.add_assertion("d_ladder_exact_odd_ok", str(bool(odd_ok)), "True")
    wb.add_assertion("substrate_least_term_edge_suppressed", str(substrate_suppressed), "True")
    wb.add_assertion("fibre_ambiguity_unsuppressed", str(fibre_unsuppressed), "True")
    wb.add_data("KMAX", KMAX)
    wb.add_data("r_star_unsuppression_threshold", mp.nstr(r_star, 12))
    wb.add_data("u_tilde_substrate_abs", mp.nstr(abs(u_mer_sub), 12))
    wb.add_data("least_term_leaves_edge_at_abs_u", mp.nstr(left_edge_at, 12) if left_edge_at else "never")
    wb.add_data("threshold_matches_rstar", bool(threshold_matches_rstar))
    wb.add_data("max_abs_im_S_over_fibre", mp.nstr(max_abs_imS, 12))
    wb.add_data("crossed_S_scale", bool(crossed_S_scale))
    wb.add_data("fibre_rows", rows)
    wb.add_data("verdict", verdict)
    wb.save()
    return 0 if (odd_ok and substrate_suppressed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
