#!/usr/bin/env python3
"""qbeta_alpha_entropy_bound_probe.py — how many reliable digits does the
REQUIRED ladder phase carry, and is that enough to identify a closed form?

Bean `qou-cds1`. The open item is that `alpha` is ASSERTED in both Markov
conventions -- `alpha = (z-1)h/2`, a literal at
`probe_q_beta_operator_valued_N3.py:70` -- and derived in neither. The
tempting next move is to invert the ladder for the phase it REQUIRES, then
look for a closed form matching it.

FORMALIZE-FIRST SAYS PRUNE BEFORE SEARCHING (compute-author §3.3). PROBE 4
already established the shape of the answer for `c_3`: the extraction chain
divides by `u^k`, which amplifies sigma(Q_beta) until the target carries fewer
reliable digits than any closed-form identification needs, and "running PSLQ
on noise is forbidden". The same question has never been asked of `alpha`.

WHAT THIS MEASURES

    cos(alpha_eff_req) = Q_codata / (Q_A * (1 - u^2))
    alpha_eff_req      = arccos(...)

so d(alpha_eff)/d(Q) carries a 1/sin(alpha_eff) factor, and

    sigma(alpha_eff) = cot(alpha_eff) * sigma_rel(Q_beta)

The cotangent is the amplifier here, and it is large precisely because
alpha_eff is small -- the same structural reason the ladder is delicate. This
probe computes the resulting effective digit count D_eff(alpha) and compares
it against the PSLQ entropy floor n*log10(2H) for the arithmetic bases that
would actually be tried.

sigma_rel(Q_beta) is taken at BOTH readings the corpus carries -- 7.8e-7
(the experimental sigma, docs/precision-goals.md §L2) and the more optimistic
7.8e-9 -- because a prune must survive the friendliest input, not the
harshest.

WHAT THIS DOES NOT DO. It does not derive alpha, propose a phase, or run any
search. If the digits are insufficient it forbids one ROUTE (identify alpha by
matching alpha_required) and says nothing against deriving alpha structurally
-- which remains the open item either way.

Anchors: proton (default) and muon.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import M_E_MEV, Q_BETA_MEV  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps()

#: sigma_rel(Q_beta) readings. 7.8e-7 is the experimental sigma; 7.8e-9 is a
#: deliberately over-optimistic stand-in so the prune is tested against the
#: friendliest input rather than the harshest.
SIGMA_READINGS = [("experimental_7.8e-7", mp.mpf("7.8e-7")),
                  ("optimistic_7.8e-9", mp.mpf("7.8e-9"))]

#: Bases a closed-form identification of a phase would plausibly try, as
#: (label, n_terms, integer_height). The floor is n*log10(2H) (PR #1805).
BASES = [("minimal {1, sqrt3, pi} H<=10", 3, 10),
         ("standard {1, sqrt3, pi^2, Vol(4_1)} H<=100", 4, 100),
         ("wide 6-term H<=100", 6, 100)]


def substrate(q):
    q = mp.mpf(q)
    hbar = (q - 1) / q
    d1 = q ** 3 / (q ** 2 + 1)
    d2 = -1 / (q * (q ** 2 + 1))
    b = mp.sqrt(d1 * d2 + 1)
    u = b * hbar ** 2
    Q_A = mp.mpf(M_E_MEV) * (2 * q + 1 - q ** 2) * (q + 1) / (2 * q ** 3)
    return {"q": q, "hbar": hbar, "b": b, "u": u, "Q_A": Q_A}


def main() -> int:
    Qc = mp.mpf(str(Q_BETA_MEV))
    print("=" * 78)
    print(" Entropy bound on the REQUIRED ladder phase")
    print("=" * 78)

    rows = []
    for label, q in (("proton", q_at()), ("muon", q_muon_at())):
        s = substrate(q)
        cos_req = Qc / (s["Q_A"] * (1 - s["u"] ** 2))
        a_eff = mp.acos(cos_req)
        # sigma(alpha_eff) = |d alpha/d Q| * sigma(Q) = cot(alpha_eff) * sigma_rel
        cot = mp.cos(a_eff) / mp.sin(a_eff)
        print(f"\n  {label}:  alpha_eff_req = {mp.nstr(a_eff, 16)}")
        print(f"          cos = {mp.nstr(cos_req, 16)}   cot = {mp.nstr(cot, 8)}")
        for sname, srel in SIGMA_READINGS:
            sig_a = cot * srel
            d_eff = -mp.log10(sig_a / abs(a_eff))
            print(f"          sigma_rel(Q)={sname:<22} "
                  f"sigma(alpha)={mp.nstr(sig_a, 5):>12}  D_eff={mp.nstr(d_eff, 5)}")
            rows.append({"anchor": label, "sigma_reading": sname,
                         "alpha_eff_required": fmt(a_eff),
                         "cot_amplifier": fmt(cot),
                         "sigma_alpha_abs": fmt(sig_a),
                         "D_eff_digits": fmt(d_eff)})

    best = max(mp.mpf(r["D_eff_digits"]) for r in rows)
    print(f"\n  best-case D_eff(alpha) over all anchors and sigma readings = "
          f"{mp.nstr(best, 6)}")
    # Column is labelled best-case explicitly: judging by `best` alone (the
    # OPTIMISTIC sigma) would read as an all-clear the experimental sigma does
    # not support. The per-sigma grid in the Reading block below is the answer.
    print(f"\n  {'basis':<44}{'floor':>8}{'best-case':>12}")
    print("  " + "-" * 64)
    floors = []
    for bl, n, H in BASES:
        floor = n * mp.log10(2 * H)
        ok = best > floor
        floors.append({"basis": bl, "n_terms": n, "height": H,
                       "floor_digits": fmt(floor), "supported": bool(ok)})
        print(f"  {bl:<44}{mp.nstr(floor, 4):>8}{('OK' if ok else 'BLOCKED'):>12}")

    min_floor = min(mp.mpf(f["floor_digits"]) for f in floors)
    # NOTE: my first version asserted `best < min_floor` -- a blanket block --
    # and it FAILED. best-case D_eff (5.61, under the OVER-OPTIMISTIC sigma)
    # exceeds the cheapest floor (3.90). The honest statement is a per-(sigma,
    # basis) grid: the phase sits right AT the boundary for the smallest
    # conceivable basis and is decisively blocked for anything realistic.
    d_exp = max(mp.mpf(r["D_eff_digits"]) for r in rows
                if r["sigma_reading"].startswith("experimental"))
    d_opt = max(mp.mpf(r["D_eff_digits"]) for r in rows
                if r["sigma_reading"].startswith("optimistic"))
    # blocked for every basis beyond the minimal one, at BOTH sigma readings
    non_minimal = [mp.mpf(f["floor_digits"]) for f in floors
                   if f["n_terms"] >= 4]
    blocked_realistic = all(d_opt < fl for fl in non_minimal)
    # and at the honest experimental sigma even the minimal basis fails
    blocked_minimal_at_exp = d_exp < min_floor
    deficit = min_floor - d_exp

    print(f"""
{'=' * 78}
 Reading
{'=' * 78}

  The amplifier on the phase is cot(alpha_eff) = {mp.nstr(mp.mpf(rows[0]['cot_amplifier']), 6)}, large for a
  STRUCTURAL reason: alpha_eff is small, so the ladder reads the phase through
  the FLAT part of the cosine, where a relative error in Q_beta becomes a
  cot-times-larger error in alpha.

  Note this is a DIFFERENT amplifier from the rung's. c_3 is amplified by
  1/u^3 = 1.6e6 (proved exactly: QOU.QBeta.c3Of_sub_mul_u_cubed); the phase is
  amplified by cot ~ 17.6. Conflating them would misattribute the noise budget.

  D_eff(alpha) at the experimental sigma(Q) = 7.8e-7 : {mp.nstr(d_exp, 6)} digits
  D_eff(alpha) at an over-optimistic  7.8e-9 : {mp.nstr(d_opt, 6)} digits

  basis floor n*log10(2H), and what each sigma supports:

    minimal  n=3 H<=10   floor {mp.nstr(mp.mpf(floors[0]['floor_digits']), 4):>6}   experimental {'NO ' if d_exp < mp.mpf(floors[0]['floor_digits']) else 'yes'}   optimistic {'NO ' if d_opt < mp.mpf(floors[0]['floor_digits']) else 'yes'}
    standard n=4 H<=100  floor {mp.nstr(mp.mpf(floors[1]['floor_digits']), 4):>6}   experimental {'NO ' if d_exp < mp.mpf(floors[1]['floor_digits']) else 'yes'}   optimistic {'NO ' if d_opt < mp.mpf(floors[1]['floor_digits']) else 'yes'}
    wide     n=6 H<=100  floor {mp.nstr(mp.mpf(floors[2]['floor_digits']), 4):>6}   experimental {'NO ' if d_exp < mp.mpf(floors[2]['floor_digits']) else 'yes'}   optimistic {'NO ' if d_opt < mp.mpf(floors[2]['floor_digits']) else 'yes'}

  ** MY HYPOTHESIS WAS WRONG. ** I expected a blanket entropy block and
  asserted best-case D_eff < cheapest floor. It failed: 5.61 > 3.90. The phase
  is NOT as noise-starved as c_3.

  What is true, and is the usable prune:

    1. Every realistic basis (n >= 4) is BLOCKED at both sigma readings --
       deficit {mp.nstr(mp.mpf(floors[1]['floor_digits']) - d_opt, 4)} digits even under the over-optimistic sigma.
    2. At the HONEST experimental sigma, even the minimal 3-term H<=10 basis
       fails, by {mp.nstr(deficit, 4)} digits. It clears only under a sigma nobody claims.

  So a closed-form identification of alpha from alpha_required is permitted by
  entropy ONLY for a 3-term, height<=10 basis AND only under an optimistic
  error reading. Anything broader is guaranteed-spurious. That is a narrow
  licence, not a green light -- and it is narrow enough to be worth stating
  before someone runs a wide search.

  WHAT THIS DOES NOT SAY. It does not argue against deriving alpha; it bounds
  one route -- fitting the anchor. The open item is unchanged: alpha is
  asserted in both conventions and derived in neither, and a categorical
  derivation is not limited by sigma(Q_beta) at all.

  Corollary: alpha_required's apparent anchor-stability (0.0005 % drift) is
  NOT evidence of structure. With ~{mp.nstr(d_exp, 3)} honest digits there is not enough
  resolution for the two anchors to disagree -- and indeed D_eff comes out
  identical at both.
""")

    wb = WitnessBuilder("qbeta-alpha-entropy-bound", engine="mpmath")
    wb.set_description(
        "Bean qou-cds1, formalize-first prune. Asks of the ladder PHASE the "
        "question PROBE 4 asked of c_3: how many reliable digits does the "
        "inverted target carry, and does that clear the PSLQ entropy floor "
        "n*log10(2H)? cos(alpha_eff_req) = Q_codata/(Q_A(1-u^2)) means "
        "sigma(alpha_eff) = cot(alpha_eff)*sigma_rel(Q_beta), and cot is large "
        "because alpha_eff is small — the ladder reads the phase through the "
        "flat part of the cosine. Evaluated at both anchors and at BOTH "
        "sigma(Q_beta) readings in the corpus (7.8e-7 experimental and an "
        "over-optimistic 7.8e-9) so the prune survives the friendliest input. "
        "Also explains the apparent anchor-stability of alpha_required: a "
        "quantity with this few digits cannot resolve a cross-anchor "
        "difference. Derives nothing and forbids only that one route; deriving "
        "alpha categorically is untouched and remains open."
    )
    wb.add_data("ladder_frame", "u")
    wb.add_data("rows", rows)
    wb.add_data("bases", floors)
    wb.add_data("D_eff_experimental_sigma", fmt(d_exp))
    wb.add_data("D_eff_optimistic_sigma", fmt(d_opt))
    wb.add_data("cheapest_floor_digits", fmt(min_floor))
    wb.add_data("minimal_basis_deficit_at_experimental_sigma", fmt(deficit))

    wb.add_assertion(
        name="every_realistic_basis_is_entropy_blocked_at_both_sigma_readings",
        computed=str(int(bool(blocked_realistic))), expected="1", tolerance=0,
        source=f"D_eff(alpha) = {mp.nstr(d_opt, 6)} digits even under the "
               f"OVER-OPTIMISTIC sigma(Q) = 7.8e-9, against floors of "
               f"{mp.nstr(mp.mpf(floors[1]['floor_digits']), 5)} (n=4, H<=100) and "
               f"{mp.nstr(mp.mpf(floors[2]['floor_digits']), 5)} (n=6, H<=100). Any "
               "closed form matched to alpha_required over a basis of 4+ terms is "
               "guaranteed-spurious, by the PR #1805 bound that already forbade "
               "the c_3 PSLQ route.",
    )
    wb.add_assertion(
        name="even_the_minimal_basis_fails_at_the_honest_experimental_sigma",
        computed=str(int(bool(blocked_minimal_at_exp))), expected="1", tolerance=0,
        source=f"at sigma(Q) = 7.8e-7 (the experimental value) D_eff(alpha) = "
               f"{mp.nstr(d_exp, 6)} digits against the cheapest floor "
               f"{mp.nstr(min_floor, 6)} (n=3, H<=10) — short by "
               f"{mp.nstr(deficit, 4)}. The minimal basis clears only under the "
               "optimistic sigma, which nobody claims. NOTE: this probe first "
               "asserted a BLANKET block (best-case D_eff < cheapest floor) and "
               "that FAILED — 5.61 > 3.90. The phase is not as noise-starved as "
               "c_3; the licence is narrow, not absent.",
    )
    wb.add_assertion(
        name="the_amplifier_on_the_phase_is_cotangent_not_one_over_u_cubed",
        computed=str(int(mp.mpf(rows[0]["cot_amplifier"]) > 5)), expected="1",
        tolerance=0,
        source=f"cot(alpha_eff_req) = {mp.nstr(mp.mpf(rows[0]['cot_amplifier']), 8)} "
               "at the proton anchor. The phase is NOT amplified by 1/u^3 (that is "
               "the c_3 rung's amplifier, proved exactly in "
               "QOU.QBeta.c3Of_sub_mul_u_cubed); it is amplified by cot, because "
               "the ladder reads it through the flat part of the cosine. Two "
               "different amplifiers, and conflating them would misattribute the "
               "phase's noise budget.",
    )
    out = wb.save({"q0Anchor": "ambiguous"})
    print(f"Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
