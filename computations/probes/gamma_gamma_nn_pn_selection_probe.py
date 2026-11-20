#!/usr/bin/env python3
"""gamma_gamma_nn_pn_selection_probe.py -- the gamma-gamma + confinement-SDP bond
selection (owner ruling 2026-09-08, bean qou-ales) run for the nn and pn
two-nucleon systems, as was done for pp in step 3; and the ordering of B_pp,
B_nn, B_pn under the live law.

## What "as was done for pp" means, read from the step-3 probe

Step 3 (`gamma_gamma_h3_psd_selector_probe.py`, bond table) applied reading 3
to the BOND WORD ALONE: candidate G^m = (sigma_2 sigma_3^-1)^m, feasible iff
chi_lambda(G^m) >= 0 on every H_6 block with y_lambda > 0.  The nucleon words
never enter that table -- they enter only the binding functional afterwards.
So that selection is content-blind BY CONSTRUCTION, and run for nn or pn it
returns G^3 identically.  This probe re-runs it per channel anyway (S1) so the
statement is measured rather than asserted, and adds the two things step 3 did
not do:

  S2  the WHOLE-ELEMENT letter scope (the 2026-09-13 (B) ruling, as corrected
      2026-09-14: reading 3, applied to the full word): candidate
      W_l W_r B^m, feasible iff chi_lambda(W_l W_r B^m) >= 0 on every H_6
      block with y_lambda > 0.  Here nucleon content DOES enter.
  P   all four gamma-gamma placements on the single-generator interface
      (step 11): V1 = s2 s3^-1, V2 = s3 s2^-1 (borrow right), V3 = s1 s2^-1,
      V4 = s2 s1^-1 (borrow left).

Channels: pp, nn, pn, np (np = the order-reversal control of pn).

## Binding

B = E_0^full * ln( tr_M(W_free) / tr_M(W_atom) ),  W_free = W_l W_r,
W_atom = W_l W_r B^m, tr_M the convention-D Markov trace on H_6
(y_lambda from y_lambda_su_n(6, q, 2)), E_0^full = m_e c_q^2 hbar_q/(1-hbar_q^2).
B > 0 bound.  AME is quoted ONLY as a labelled comparison after the
selection; nothing is selected by agreement.

## pn: two channels

The words carry quark content and a bond, nothing else: there is no spin or
isospin label in W_l W_r B^m, so neither S1 nor S2 can tell the deuteron
(T=0, 3S1) from the pn singlet (T=1, 1S0).  One number per ordered pn word.

RESULT (proton pin, m <= 10), recorded so the file does not read as an expectation:
  * S1 selects G^3 at all four placements for every channel -- content-blind.
  * S2 at V1, V2 gives the S1 answer {0,3,6,9} for every channel (content-blind,
    measured); at V3, V4 it is channel-dependent and picks m = 1 or 2.
  * In all 8 (placement x scope) cells the pn binding EQUALS a like-pair binding
    (one-body, step 11), so pn is never strictly above, below or between pp and nn
    (Lean QOU.Mass.OneBodyBondOrdering).  Canonical V1, G^3:
    B_nn = B_pn = -2.583 keV > B_pp = B_np = -4.469 keV; all unbound; pp != nn.

PRECISION: mpmath, 60 dps, seeded from Q_50_DIGIT_STR (proton pin). No float.
Machinery reused verbatim from gamma_gamma_h3_psd_selector_probe.
"""
from __future__ import annotations

import os
import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
for _p in ("tools/pyhecke/python", "tools/qou-substrate/python",
           "computations/substrate", "computations/hecke", "computations",
           "computations/probes"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from hoefsmit_mpmath import BlockCacheMP, seminormal_matrices_mp  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from pyhecke.wedderburn import partitions_of  # noqa: E402
from y_lambda_su_n import y_lambda_su_n  # noqa: E402
from gamma_gamma_h3_psd_selector_probe import (  # noqa: E402
    nucleon_block, trace, word_image)

DPS = 60
set_compute_dps(DPS)
TOL = mp.mpf("1e-40")
MMAX = 10
AME_DEUTERON_MEV = "2.224566"   # labelled comparison only (AME2020 B(2H))


def placement(name: str, h):
    one, zero = mp.mpf(1), mp.mpf(0)
    s = lambda g: (one, zero, g)          # noqa: E731
    si = lambda g: (one, -h, g)           # noqa: E731  sigma^-1 = sigma - h
    return {"V1": [s(2), si(3)], "V2": [s(3), si(2)],
            "V3": [s(1), si(2)], "V4": [s(2), si(1)]}[name]


def ordering(b):
    """Descending order with exact ties (|diff| < TOL) grouped by '='."""
    keys = sorted(b, key=lambda c: -b[c])
    out = keys[0]
    for a, c in zip(keys, keys[1:]):
        out += (" = " if abs(b[a] - b[c]) < TOL else " > ") + c
    return out


def main() -> int:
    t0 = time.time()
    if os.environ.get("QOU_Q0_ANCHOR", "").strip().lower() in ("ideal", "muon", "canonical"):
        raise SystemExit("proton-pin producer; refusing a muon override")
    mp.mp.dps = DPS
    q = Q_MP
    qi = 1 / q
    h = q - qi
    cache = BlockCacheMP(q, h)

    parts6 = [tuple(p) for p in partitions_of(6)]
    y6 = {tuple(k): mp.mpf(v) for k, v in y_lambda_su_n(6, q, 2).items()}
    supp = [lam for lam in parts6 if y6[lam] > TOL]
    off = max(abs(y6[lam]) for lam in parts6 if lam not in supp)
    reps = {lam: seminormal_matrices_mp(lam, cache=cache) for lam in parts6}

    def chis(word):
        return {lam: trace(word_image(reps[lam][0], reps[lam][1], word), reps[lam][1])
                for lam in supp}

    def trm(word):
        return mp.fsum(y6[lam] * c for lam, c in chis(word).items())

    from qou_substrate.constants import M_E_MEV  # noqa: PLC0415
    me = mp.mpf(str(M_E_MEV))
    hbar_q = 1 - qi
    E0 = me * (1 / (q - 1)) ** 2 * hbar_q / (1 - hbar_q ** 2)

    print(f"gamma-gamma nn/pn selection -- proton pin, convention D, {DPS} dps")
    print(f"  h = {mp.nstr(h, 15)}; y>0 on {supp}; max |y| off support {mp.nstr(off, 3)}")
    print("  y: " + ", ".join(f"{lam}:{mp.nstr(y6[lam], 10)}" for lam in supp))
    print(f"  E_0^full = {mp.nstr(E0, 12)} MeV")

    channels = {"pp": ("p", "p"), "nn": ("n", "n"), "pn": ("p", "n"), "np": ("n", "p")}
    W = {c: nucleon_block(a, h, 0) + nucleon_block(b, h, 3) for c, (a, b) in channels.items()}

    # ---- S1: bond alone, per placement (content cannot enter) -------------
    s1 = {}
    print("\n  S1  bond-alone reading 3 (step-3 scope): feasible m in 0..10")
    for P in ("V1", "V2", "V3", "V4"):
        rows = []
        for m in range(MMAX + 1):
            c = chis(placement(P, h) * m)
            rows.append({"m": m, "feasible": all(v >= -TOL for v in c.values()),
                         "chi": {str(l): fmt(v) for l, v in c.items()}})
        feas = [r["m"] for r in rows if r["feasible"]]
        nz = min([m for m in feas if m > 0], default=None)
        s1[P] = {"feasible_m": feas, "min_nonzero": nz, "rows": rows}
        print(f"    {P}: feasible {feas}; minimal non-zero survivor m = {nz}")

    # ---- S2: whole element, per placement x channel ------------------------
    s2 = {}
    print("\n  S2  whole-element reading 3 ((B) letter scope): chi_lambda(W_l W_r B^m), y>0 blocks")
    for P in ("V1", "V2", "V3", "V4"):
        s2[P] = {}
        for ch in channels:
            rows = []
            for m in range(MMAX + 1):
                c = chis(W[ch] + placement(P, h) * m)
                bad = [str(l) for l, v in c.items() if v < -TOL]
                rows.append({"m": m, "feasible": not bad, "failing_blocks": bad,
                             "chi": {str(l): fmt(v) for l, v in c.items()}})
            feas = [r["m"] for r in rows if r["feasible"]]
            nz = min([m for m in feas if m > 0], default=None)
            s2[P][ch] = {"feasible_m": feas, "min_nonzero": nz, "rows": rows}
            fails0 = rows[0]["failing_blocks"]
            print(f"    {P} {ch}: feasible {feas}; min non-zero {nz}; "
                  f"free pair (m=0) fails on {fails0}")

    # ---- binding with the S1-selected bond G^3 at every placement ---------
    print("\n  B = E0 ln(tr_free/tr_atom) with the S1-selected bond B^3 [MeV]")
    bind = {}
    for P in ("V1", "V2", "V3", "V4"):
        bind[P] = {}
        for ch in channels:
            tf = trm(W[ch])
            ta = trm(W[ch] + placement(P, h) * 3)
            B = E0 * mp.log(abs(tf) / abs(ta))
            bind[P][ch] = {"tr_free": fmt(tf), "tr_atom": fmt(ta), "ratio": fmt(ta / tf),
                           "B_MeV": fmt(B), "sign_ok": bool(tf > 0 and ta > 0)}
        b = {ch: mp.mpf(bind[P][ch]["B_MeV"]) for ch in channels}
        order = ordering(b)
        print(f"    {P}: " + "  ".join(f"B_{c}={mp.nstr(b[c] * 1000, 8)} keV" for c in channels)
              + f"   order: {order}")
        bind[P]["order_desc"] = order
        bind[P]["charge_independence_pp_eq_nn"] = bool(abs(b["pp"] - b["nn"]) < TOL)
        bind[P]["pp_minus_nn_MeV"] = fmt(b["pp"] - b["nn"])

    # ---- binding with the S2 (whole-element) selected bond ------------------
    print("\n  B with the S2-selected (whole-element, channel-wise) bond B^m* [MeV]")
    bind2 = {}
    for P in ("V1", "V2", "V3", "V4"):
        bind2[P] = {}
        for ch in channels:
            m = s2[P][ch]["min_nonzero"]
            tf = trm(W[ch])
            ta = trm(W[ch] + placement(P, h) * m)
            bind2[P][ch] = {"m": m, "ratio": fmt(ta / tf),
                            "B_MeV": fmt(E0 * mp.log(abs(tf) / abs(ta))),
                            "sign_ok": bool(tf > 0 and ta > 0)}
        b = {ch: mp.mpf(bind2[P][ch]["B_MeV"]) for ch in channels}
        bind2[P]["order_desc"] = ordering(b)
        print(f"    {P}: " + "  ".join(f"B_{c}(m={bind2[P][c]['m']})={mp.nstr(b[c] * 1000, 8)} keV"
                                     for c in channels) + f"   order: {bind2[P]['order_desc']}")

    # template (labelled reference: the production pp->s, nn->s^-1, pn->avg rule)
    tmpl = {"pp": [(mp.mpf(1), mp.mpf(0), 2)], "nn": [(mp.mpf(1), -h, 2)],
            "pn": [(mp.mpf(1), -h / 2, 2)], "np": [(mp.mpf(1), -h / 2, 2)]}
    tB = {ch: fmt(E0 * mp.log(trm(W[ch]) / trm(W[ch] + tmpl[ch]))) for ch in channels}
    print("  template (reference, not selected): " +
          "  ".join(f"B_{c}={mp.nstr(mp.mpf(v), 8)}" for c, v in tB.items()) + " MeV")
    print(f"  AME (labelled comparison only): B(2H, pn T=0) = {AME_DEUTERON_MEV} MeV; pp, nn unbound")

    # ---- assertions --------------------------------------------------------
    s1_same = len({tuple(s1[P]["feasible_m"]) for P in s1}) == 1
    pp_ctrl = mp.mpf(bind["V1"]["pp"]["B_MeV"])
    import json  # noqa: PLC0415
    _w3 = json.loads((_ROOT / "computations/probes/gamma-gamma-h3-psd-selector-probe.witness.json").read_text())
    _w3 = _w3.get("data", _w3)
    step3 = mp.mpf(next(r["B_pp_MeV"] for r in _w3["pp_binding"] if r["bond"] == "G^3"))
    dev_ctrl = abs(pp_ctrl - step3)
    print(f"\n  control: B_pp(V1) vs step-3 witness dev {mp.nstr(dev_ctrl, 3)} MeV")
    print(f"  wall {time.time() - t0:.1f} s")

    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    w = WitnessBuilder("gamma-gamma-nn-pn-selection-probe", engine="python", start_time=t0)
    w.set_description(
        "qou-ales extension to nn/pn: reading-3 (Frobenius positivity) gamma-gamma bond "
        "selection on the H_6 interface for pp/nn/pn/np at four placements, in the bond-alone "
        "(step-3) scope and the whole-element (B) scope; binding under the live log law with "
        "the selected bond. No AME value used in selection.")
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_parameter("convention", "D (z = q^3/(q^2+1))")
    w.add_parameter("dps", DPS)
    w.add_parameter("mmax", MMAX)
    w.add_parameter("E_0_MeV", fmt(E0))
    w.add_data("y_lambda_support", {str(l): fmt(y6[l]) for l in supp})
    w.add_data("S1_bond_alone", s1)
    w.add_data("S2_whole_element", s2)
    w.add_data("binding_with_selected_bond_m3", bind)
    w.add_data("binding_with_S2_selected_bond", bind2)
    w.add_data("template_binding_reference_MeV", tB)
    w.add_data("AME_comparison_label_only", {"B_2H_MeV": AME_DEUTERON_MEV})
    w.add_assertion(name="y_zero_off_two_row", computed=fmt(off), expected="0",
                    tolerance="1e-40", source="convention D two-row truncation")
    w.add_assertion(name="S1_selection_same_at_all_placements", computed=str(int(s1_same)),
                    expected="1", tolerance="0", source="trace_cayleyInverse + parabolic conjugacy")
    w.add_assertion(name="S1_min_nonzero_is_three", computed=str(s1["V1"]["min_nonzero"]),
                    expected="3", tolerance="0", source="GammaGammaH6Interface.interfaceSelected_three")
    ties = 0
    for tab in (bind, bind2):
        for P in ("V1", "V2", "V3", "V4"):
            bp = {c: mp.mpf(tab[P][c]["B_MeV"]) for c in channels}
            ties += int(abs(bp["pn"] - bp["pp"]) < TOL or abs(bp["pn"] - bp["nn"]) < TOL)
    w.add_assertion(name="pn_tied_to_a_like_pair_in_all_8_cells", computed=str(ties),
                    expected="8", tolerance="0",
                    source="Lean OneBodyBondOrdering.pn_eq_like (one-body premise, step 11)")
    blind = int(all(len({tuple(s2[P][c]["feasible_m"]) for c in channels}) == 1 for P in ("V1", "V2")))
    w.add_assertion(name="S2_right_placements_content_blind", computed=str(blind), expected="1",
                    tolerance="0", source="measured, m <= 10")
    w.add_assertion(name="pp_control_matches_step3", computed=fmt(dev_ctrl), expected="0",
                    tolerance="1e-50", source="gamma-gamma-h3-psd-selector-probe.witness.json")
    print(f"  witness -> {w.save()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
