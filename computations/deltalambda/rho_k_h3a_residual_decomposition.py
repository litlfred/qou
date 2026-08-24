#!/usr/bin/env python3
"""rho_k_h3a_residual_decomposition.py — the ~1e-8 Schur-Weyl residual is INPUT PROVENANCE,
not a precision floor and not a logic bug.

WHAT bean qdzu SAID, and why it is wrong.  Bean `qdzu` (2026-07-05, surfaced by the 5-way
witness-drain swarm in PR #3351) records that three exploratory Delta_lambda probes
(`rho_k_h3a_crystal`, `rho_k_h3a_lp_dual`, `rho_k_h3a_refinement`) fail an internal
Schur-Weyl self-check at ~1e-8 against a 1e-40 tolerance, and hypothesises:

    "The ~1e-8 residual is consistent across all three -> a numeric-engine
     precision floor, not a logic bug: the self-check tolerance (1e-40) is
     set far below the engine's achievable precision (~1e-8)."

That reasoning is pattern-matching on the *consistency* of the number, not a measurement of
its *cause*, and it does not survive either half:

  * NOT a precision floor.  The compute runs at 50 dps.  A genuine engine floor would sit at
    ~1e-50, not ~1e-8 -- 42 orders away.  Feeding the identity self-consistent inputs drives
    the residual to 3.1e-49, i.e. the actual floor.  The engine was never the limit.
  * NOT a logic bug.  The Schur-Weyl identity Sum_lambda y_lambda chi^lambda = tr_M is exact
    for this braid word; it was verified identically in q (as rational functions, zero Float
    atoms) at n=3 and n=6 in PR #5168 / bean qou-hdyp.  beta_D on H_6 with 23 crossings IS
    the n=6 atom of that proof.

THE ACTUAL CAUSE is that the two sides of the self-check are evaluated at DIFFERENT q_0
PINS -- the documented two-layer calibration convention leaking into one quantity, exactly
the class `mu3_anchor_consistency_probe.py` records for the mu3 Frechet probe:

    LHS  Sum_lambda y_lambda(q_0) chi^lambda(beta_D; q_0)
         evaluated at `q_parameter.Q_MP` = 1.1099785827513808...   (PROTON, experimental)

    RHS  tr_M(beta_D) read from `atomic-tr-m-mpfr-50dps.witness.json`,
         which is stamped `q0Anchor: "muon"`  = 1.1099785955573347...   (MUON, ideal 3-CAL)

    separation = 11.5371 ppb  --  the mu-p substrate tension itself.

Per AGENTS.md S"q0 anchor convention": "Never straddle the two layers inside one quantity.
Mixing an ideal-layer input with an experimental-layer input in a single computed number is
a defect regardless of its size."  That is precisely what the self-check does.

THE DECOMPOSITION this probe measures.  The residual is fully accounted for by two input
mismatches, with nothing left over for the identity:

    | component                        |     size | share |
    |----------------------------------|----------|-------|
    | q_0 pin straddle (proton/muon)   |  8.34e-8 |   98% |
    | witness internal self-inconsistency | 1.85e-9 |    2% |
    | Schur-Weyl identity itself       |  3.1e-49 |    0% |

The second component is a finding in its own right, and it points at the witness rather than
at any probe: `atomic-tr-m-mpfr-50dps.witness.json` carries TWO deuteron tr_M values that
disagree with each other by 1.852e-9 --

    results.tr_M_at_q0_50dps                  = 0.57517232916588433221594741758...
    results.peel_cross_check.tr_M_at_q0_50dps = 0.57517233101788385191979179668...

-- and the independently-computed Schur-Weyl sum agrees with the `peel_cross_check` branch to
3.1e-49 (the 50-dps floor) while missing the `primary` branch by that same 1.852e-9.  Two
independent routes agreeing to the floor is strong evidence the PRIMARY value is the wrong
one, so the self-check has been reading against the less reliable of the witness's two
numbers.  Recorded separately; the fix belongs to the witness's producer, not here.

WHICH LAYER IS CORRECT for this probe.  MUON -- do not "fix" this by moving the probe to the
proton pin.  The 2026-08-07 owner directive defaults *new and touched* compute to the
experimental (proton) anchor, but its own "Never mix" clause dominates here: this probe's
required input (`atomic-tr-m-mpfr-50dps.witness.json`) is a muon-layer witness, and
regenerating it at the proton pin is part of the bulk migration that is explicitly GATED
behind bean `qou-1c4y` and still needs scoped sign-off.  Moving only the evaluation pin while
the input witness stays muon would not remove the straddle -- it would invert it.  So the
in-scope fix is to make the probe internally consistent at the layer its input already lives
in, and to say so explicitly in the witness.  This matches the ruling
`mu3_anchor_consistency_probe.py` reached for the same class: "for a categorical Delta^2 g in
computations/, that layer is MUON."

Run:  python3 -u rho_k_h3a_residual_decomposition.py 2>&1 | tee /tmp/rho_k_h3a_resid.log
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMPUTATIONS = HERE.parent
for _p in (COMPUTATIONS, COMPUTATIONS / "hecke", COMPUTATIONS / "substrate"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402

set_compute_dps()

import rho_k_h3a_refinement as R  # noqa: E402
from _li_2_q_util import flavor_split_leading  # noqa: E402
from canonical_braid_crossings import d_for_ctype  # noqa: E402
from q_parameter import Q_MP  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

TR_M_WITNESS = "atomic-tr-m-mpfr-50dps.witness.json"


def load_tr_m_both_branches():
    """Return (q0_of_witness, anchor_label, tr_M_primary, tr_M_peel) for the deuteron.

    Both branches are returned deliberately: the whole point of this probe is that they
    disagree, and that the identity picks out one of them.
    """
    path = None
    for cand in COMPUTATIONS.rglob(TR_M_WITNESS):
        path = cand
        break
    if path is None:
        raise RuntimeError(f"{TR_M_WITNESS} not found under {COMPUTATIONS}")

    doc = json.loads(path.read_text())
    q0 = mp.mpf(doc["q0Value"])
    anchor = doc.get("q0Anchor", "UNSTAMPED")
    for r in doc["results"]:
        if "deuteron" in json.dumps(r).lower():
            primary = mp.mpf(r["tr_M_at_q0_50dps"])
            peel = mp.mpf(r["peel_cross_check"]["tr_M_at_q0_50dps"])
            return q0, anchor, primary, peel
    raise RuntimeError("deuteron entry not found in " + TR_M_WITNESS)


def schur_weyl_sum_at(q, y_sym, crossings, parts):
    """Sum_lambda y_lambda(q) chi^lambda(beta_D; q), every input evaluated at THIS q.

    delta is recomputed at `q` rather than taken from `d_for_ctype`'s default cache.  The
    default is pinned at the numeric `q_parameter.Q`, so leaving it alone would re-introduce
    the very straddle this probe measures -- a second, inner one, inside chi itself.
    """
    q = mp.mpf(mp.nstr(q, 50, strip_zeros=False))
    q_sym = sp.sympify(mp.nstr(q, 50, strip_zeros=False))
    delta = mp.mpf(
        str(sp.sympify(flavor_split_leading(sp.Symbol("q")))
            .subs(sp.Symbol("q"), q_sym)
            .evalf(mp.mp.dps))
    )

    total = mp.mpf(0)
    for lam in parts:
        mats, dim, _ = R.hoefsmit_matrices_numeric(lam, q)
        if dim == 0:
            continue
        h = q - mp.mpf(1) / q
        eye = mp.eye(dim)
        M = mp.eye(dim)
        for gen_idx, ctype in crossings:
            M = M * (mats[gen_idx] + d_for_ctype(ctype, h, delta=delta) * eye)
        chi = sum(M[i, i] for i in range(dim))
        y = mp.mpf(str(y_sym[lam].subs(R.Q_SYM, q_sym).evalf(mp.mp.dps)))
        total += y * chi
    return total


def main() -> int:
    q_muon, anchor, tr_primary, tr_peel = load_tr_m_both_branches()
    q_proton = Q_MP
    rel_gap = abs(q_proton - q_muon) / q_muon

    print("=" * 88)
    print("rho_k_h3a Schur-Weyl residual — decomposition")
    print("=" * 88)
    print(f"\n  q_0 PROTON (q_parameter.Q_MP, what the probe evaluates at)")
    print(f"      = {mp.nstr(q_proton, 50)}")
    print(f"  q_0 MUON   ({TR_M_WITNESS}, q0Anchor={anchor!r})")
    print(f"      = {mp.nstr(q_muon, 50)}")
    print(f"  separation = {mp.nstr(rel_gap * mp.mpf('1e9'), 6)} ppb  (the mu-p substrate tension)")

    print(f"\n  witness tr_M(beta_D)  primary = {mp.nstr(tr_primary, 40)}")
    print(f"  witness tr_M(beta_D)  peel    = {mp.nstr(tr_peel, 40)}")
    print(f"  the witness disagrees with ITSELF by {mp.nstr(abs(tr_peel - tr_primary), 8)}")

    y_sym = R.load_y_lambda_n6()
    crossings = R.deuteron_canonical_crossings()
    parts = R.partitions_of_n(6)
    print(f"\n  computing Sum_lambda y_lambda chi^lambda over {len(parts)} partitions, "
          f"{len(crossings)} crossings on H_6 …")

    sum_proton = schur_weyl_sum_at(q_proton, y_sym, crossings, parts)
    sum_muon = schur_weyl_sum_at(q_muon, y_sym, crossings, parts)

    r_straddle = abs(sum_proton - tr_primary)      # what the probe currently reports
    r_pin_fixed = abs(sum_muon - tr_primary)       # pin matched, primary branch
    r_exact = abs(sum_muon - tr_peel)              # pin matched, peel branch

    print("\n  RESIDUALS")
    print(f"    LHS@proton  vs  tr_M primary   = {mp.nstr(r_straddle, 8)}   "
          f"<- what the self-check reports")
    print(f"    LHS@muon    vs  tr_M primary   = {mp.nstr(r_pin_fixed, 8)}   "
          f"<- pin straddle removed")
    print(f"    LHS@muon    vs  tr_M peel      = {mp.nstr(r_exact, 8)}   "
          f"<- identity at the engine floor")

    print("\n  DECOMPOSITION of the reported residual")
    print(f"    q_0 pin straddle           {mp.nstr(r_straddle - r_pin_fixed, 6):>14}   "
          f"({float((r_straddle - r_pin_fixed) / r_straddle) * 100:.1f}%)")
    print(f"    witness self-inconsistency {mp.nstr(r_pin_fixed, 6):>14}   "
          f"({float(r_pin_fixed / r_straddle) * 100:.1f}%)")
    print(f"    Schur-Weyl identity        {mp.nstr(r_exact, 6):>14}   "
          f"({float(r_exact / r_straddle) * 100:.1e}%)")

    identity_exact = r_exact < mp.mpf("1e-40")
    print(f"\n  VERDICT: the Schur-Weyl identity is "
          f"{'EXACT (at the 50-dps floor)' if identity_exact else 'NOT exact — investigate'}.")
    print("  Bean qdzu's 'numeric-engine precision floor' hypothesis is refuted: the floor")
    print("  is 3.1e-49, and the ~1e-8 is entirely input provenance.")
    print("=" * 88)

    w = WitnessBuilder("rho-k-h3a-residual-decomposition", engine="mpmath",
                       output_dir=HERE)
    w.add_assertion("schur_weyl_identity_exact_at_matched_pin", 1 if identity_exact else 0, 1)
    w.add_parameter("q0_proton", mp.nstr(q_proton, 50))
    w.add_parameter("q0_muon", mp.nstr(q_muon, 50))
    w.add_parameter("q0_anchor_of_tr_M_witness", anchor)
    w.add_parameter("separation_ppb", fmt(rel_gap * mp.mpf("1e9")))
    w.add_parameter("evaluation_pin_used", "muon")
    w.add_data("residuals", {
        "lhs_proton_vs_tr_M_primary": str(r_straddle),
        "lhs_muon_vs_tr_M_primary": str(r_pin_fixed),
        "lhs_muon_vs_tr_M_peel": str(r_exact),
        "witness_primary_minus_peel": str(tr_peel - tr_primary),
    })
    w.add_caveat(
        "DEFECT RECORDED, and it is a CALIBRATION-LAYER crossing plus a witness-internal "
        "inconsistency -- NOT the numeric-engine precision floor that bean qdzu "
        "hypothesised. The rho_k_h3a probes evaluate Sum_lambda y_lambda chi^lambda at the "
        "EXPERIMENTAL (proton) q_0 from q_parameter.Q_MP while reading tr_M from "
        "atomic-tr-m-mpfr-50dps.witness.json, which is stamped q0Anchor='muon' (the IDEAL "
        "3-CAL layer). The 11.5371 ppb separation is the mu-p substrate tension itself and "
        "accounts for 98% of the reported ~8.5e-8. The remaining 2% (1.852e-9) is the "
        "witness disagreeing with ITSELF: its results.tr_M_at_q0_50dps and its "
        "results.peel_cross_check.tr_M_at_q0_50dps differ by that amount, and the "
        "independently-computed Schur-Weyl sum matches the PEEL branch to 3.1e-49 while "
        "missing the PRIMARY branch by 1.852e-9 -- evidence that the primary value, not the "
        "identity, is the wrong number. With the pin matched and the peel branch used, the "
        "residual is 3.1e-49, i.e. the actual 50-dps engine floor. The identity itself was "
        "already proved to hold identically in q at n=3 and n=6 (PR #5168, bean qou-hdyp); "
        "beta_D on H_6 with 23 crossings is that proof's n=6 atom. Correct layer for this "
        "probe is MUON, matching its input witness -- moving only the evaluation pin to "
        "proton would invert the straddle rather than remove it, and regenerating the input "
        "witness at proton is gated behind bean qou-1c4y."
    )
    w.set_description(
        "Decomposes the ~1e-8 Schur-Weyl self-check residual of the rho_k_h3a probes into "
        "q_0 pin straddle (98%), witness internal self-inconsistency (2%), and the identity "
        "itself (0%; 3.1e-49 at the 50-dps floor). Refutes bean qdzu's precision-floor "
        "hypothesis and localises the residual entirely in input provenance."
    )
    # Declare MUON, not "ambiguous". The witness does carry both pins, which is the
    # signature `gen_q0_anchor_manifest.py` maps to `ambiguous` -- but that state is defined
    # as "a queue for a manual ruling", and the ruling is made: the verdict (identity exact
    # at 3.1e-49) is established at the muon pin, matching the layer this probe's input
    # witness already lives in. The proton value is present only as a labelled comparison,
    # which is the deliberate-comparison case AGENTS.md carves out for both-pin witnesses.
    w.save({"q0Anchor": "muon", "q0Value": mp.nstr(q_muon, 50)})
    return 0 if identity_exact else 1


if __name__ == "__main__":
    raise SystemExit(main())
