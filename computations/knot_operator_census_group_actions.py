#!/usr/bin/env python3
"""Knot-operator census + group-action map (EXPLORATORY, audit-only).

Maps the distinct knot/link operators that appear in the QOU framework for
color tubes / nucleons / channels and the group action(s) attached to each.

Computes, RAW (no tuning to any observable):
  - the writhe w(beta) of each canonical braid word (the U(1)_framing datum);
  - the Markov-trace stabilization scaling tr_M(beta . sigma_n^{+-1}) = z^{+-1} tr_M(beta)
    (z = 1/(q^{1/2}+q^{-1/2})) at the substrate q0, the canonical
    strand-count-changing map B_n -> B_{n+1};
  - the n-independence of tr_M(sigma_1^2) (the Hopf, witness sanity);
  - which operators have nonzero writhe (live U(1)) vs zero (Borromean),
    reported WITH the level n each writhe is taken at (see below);
  - the level-independent companion (w - n) mod 2 of each (w, n) pair.

LEVEL OF DEFINITION (framing; no number in this census changes)
---------------------------------------------------------------
The writhe is a property of the BRAID WORD, not of its closure. It is invariant
under Markov I (conjugation) but Markov II -- stabilization
beta in B_n |-> beta.sigma_n^{+-1} in B_{n+1} -- shifts it by +-1 while
presenting the SAME link. The operators censused here do not share a level:
the Hopf and the torus knots T(2,k) sit in B_2, the Borromean baryon and the
figure-eight in B_3, the unknot in B_1. So "nonzero writhe vs zero writhe" is a
statement about words at three different levels, and the raw comparison is a
cross-level one.

Two things make it well-posed rather than broken:

  (a) Under the owner ruling -- states are Groebner-Shirshov normal forms, and
      the observable is the trace at the LOWEST level of the substrate tower
      (the braid index) -- these canonical words ARE the states. The census
      compares states, not two presentations of one state. Every writhe below
      is therefore reported together with its level n, and the U(1)_framing
      verdict is stated per level rather than across levels.

  (b) Markov II acts on the pair (w, n) as (w +- 1, n + 1), whose complete
      invariant is (w - n) mod 2 -- proved in
      QOU/StandardModel/WritheLevelParity.lean (markovPair_parity soundness,
      markovPair_of_even completeness), and equal to the COMPONENT PARITY of
      the closure. It is emitted per row below, computed from the stored
      (writhe, strands_B_n) pair. It carries exactly ONE BIT: it can never
      substitute for a magnitude, for Q = w/2, or for I_3, and the physical
      (fermion/boson) reading of it is refuted -- see the audit. Its only
      legitimate use is as a consistency check on level-crossing claims.

Ref: docs/audits/2026-08-10-writhe-level-of-definition.md (sections 4, 5d, 6).

NO FIT. Every numeric is a falsification reference reported raw.
Audit doc: docs/audits/2026-06-01-knot-operator-census-group-actions.md
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from witness_base import WitnessBuilder  # noqa: E402

START = time.time()
mp.mp.dps = 60

# Substrate q0 (proton-anchored). Reference value only -- not tuned here.
Q0 = mp.mpf("1.10998")


def writhe_from_word(word):
    """Writhe = sum of crossing signs. word is a list of signed generators
    (+i = sigma_i, -i = sigma_i^{-1})."""
    return sum(1 if g > 0 else -1 for g in word)


def z_factor(q):
    """Markov stabilization factor z = q^3/(q^2 + 1) (convention D)."""
    return q**3 / (q**2 + 1)


def trM_sigma1_sq(q):
    """Closed form tr_M(sigma_1^2) = h*z + 1, h = q - q^-1 (n-independent).

    Delegates to the canonical definition. It was 1 + (q-1)/q^{1/2} -- this
    same identity at z_C, correct arithmetic and permanently wrong the moment
    z moved -- then a local `h*z+1`, which was right but still a COPY. A local
    copy of a library value is the defect class this whole arc is about, so it
    is now the library's, gated once by R11 as
    `closed_form_tau_M.trM_sigma1_sq`.
    """
    from closed_form_tau_M import trM_sigma1_sq as _canonical
    return _canonical(q)


# --- Census of canonical braid words (operator -> (B_n strand count, word)) ---
# word entries: +i = sigma_i (L+), -i = sigma_i^{-1} (L-)
OPERATORS = {
    # name: (strands n in B_n, braid word as signed-generator list, note)
    "unknot_T(1,0)": (1, [], "identity / vacuum; genus 0"),
    "Hopf_T(2,2)=sigma1^2": (2, [1, 1], "positive Hopf link; diquark; writhe +2"),
    "trefoil_T(2,3)=sigma1^3": (2, [1, 1, 1], "electron e^-; lepton gen 1"),
    "cinquefoil_T(2,5)=sigma1^5": (2, [1, 1, 1, 1, 1], "muon; lepton gen 2"),
    "septafoil_T(2,7)=sigma1^7": (2, [1] * 7, "tau; lepton gen 3 (sym-broken)"),
    "T(2,9)=sigma1^9": (2, [1] * 9, "genus-4 saturation; sym-broken"),
    "T(3,4)=(s1 s2)^4": (3, [1, 2] * 4, "Hopf^2 color binding; H^{0,1}"),
    "T(3,5)=(s1 s2)^5": (3, [1, 2] * 5, "weak mediator; alpha_EM index"),
    "borromean=(s1^-1 s2)^3": (3, [-1, 2, -1, 2, -1, 2], "nucleon/baryon; writhe 0"),
    "figure8_4_1": (3, [1, -2, 1, -2], "Higgs/pion-half; hyperbolic; writhe 0"),
}


def main() -> int:
    """Run the producer and write its witness.

    This body used to sit at MODULE LEVEL, so `import knot_operator_census_group_actions`
    ran the whole computation and rewrote the witness as a side effect of
    the import. Any tool that imports the module -- a validator, a doc
    generator, a test collector -- would silently regenerate a witness.
    That also made the module impossible to gate numerically: R11 in the
    trace-convention registry has to import what it checks.

    Only the side-effecting tail moved. The constants and pure functions
    above stay at module level, so they remain importable, which is what
    the gate needs.
    """
    w = WitnessBuilder("knot-operator-census-group-actions", engine="mpmath", start_time=START)
    w.set_description(
        "EXPLORATORY census of QOU knot/link operators: writhe (U(1)_framing), "
        "Markov-stabilization scaling (B_n->B_{n+1} bridge), Hopf n-independence. "
        "All RAW @ 60 dps; no tuning to any observable."
    )
    w.set_audit_only("docs/audits/2026-06-01-knot-operator-census-group-actions.md")
    w.add_parameter("q0", str(Q0))
    w.add_parameter("dps", mp.mp.dps)

    # --- 1. Writhe per operator (the U(1)_framing datum), WITH its level ---
    # Each row carries the level n it is defined at (strands_B_n) plus the
    # level-independent companion (w - n) mod 2, computed from that stored pair --
    # the complete invariant of the Markov-II action (w, n) -> (w +- 1, n + 1)
    # (WritheLevelParity.lean). Nothing is hardcoded: the parity is derived from the
    # same (writhe, strands_B_n) already recorded. One bit only -- see the module
    # docstring for what it cannot be used for.
    writhes = {}
    for name, (n, word, note) in OPERATORS.items():
        wr = writhe_from_word(word)
        writhes[name] = {"strands_B_n": n, "writhe": wr, "note": note,
                         "u1_framing_nontrivial": wr != 0,
                         "writhe_minus_level_parity": (wr - n) % 2}
    w.add_data("writhe_per_operator", writhes)

    # T(2,2m) writhe = +2m closed form (all positive crossings)
    t22m = {}
    for m in range(1, 6):
        word = [1] * (2 * m)  # sigma_1^{2m}
        t22m[f"T(2,{2*m})"] = {"writhe": writhe_from_word(word), "formula_2m": 2 * m}
    w.add_data("torus_T2_2m_writhe", t22m)
    # assertion: T(2,2m) writhe equals 2m (derived, structural)
    for m in range(1, 6):
        w.add_assertion(f"writhe_T(2,{2*m})_eq_2m", t22m[f"T(2,{2*m})"]["writhe"], 2 * m)
    # assertion: Borromean writhe = 0 (the U(1) is trivial on the baryon)
    w.add_assertion("writhe_borromean_eq_0", writhes["borromean=(s1^-1 s2)^3"]["writhe"], 0)

    # --- 2. Markov stabilization factor z at q0 (the strand-count bridge) ---
    z = z_factor(Q0)
    w.add_data("markov_stabilization_factor_z_at_q0", str(z))
    # Stabilization: tr_M(beta . sigma_n^{+-1}) = z^{+-1} tr_M(beta) when the new
    # strand is DISJOINT. This is the canonical B_n -> B_{n+1} map (vertical alpha_V
    # of markov-moves-brane-tower.md). Report z, z^-1 RAW.
    w.add_data("z_inverse_at_q0", str(1 / z))

    # --- 3. Hopf tr_M(sigma_1^2) n-independence (sanity; the disjoint-strand case) ---
    trhopf = trM_sigma1_sq(Q0)
    w.add_data("trM_sigma1_sq_at_q0", str(trhopf))
    # Verify the closed form 1+(q-1)/sqrt(q) equals the Hecke-derived value
    # tr_M(sigma_1^2) = (q-q^-1)*z + 1 with z = 1/(q^{1/2}+q^{-1/2}).
    hecke_val = (Q0 - 1 / Q0) * z_factor(Q0) + 1
    w.add_assertion("trM_sigma1sq_closedform_eq_hecke", str(trhopf), str(hecke_val),
                    tolerance=1e-50)

    # --- 4. Strand-count summary: which group acts on which n ---
    # Borromean baryon lives in H_3 (3 strands); the S5/SO(3) fiber lives on
    # 5 strands (partitions of 5). The torus knots T(2,n) live in B_2 (2 strands);
    # T(3,n) in B_3 (3 strands). Markov stabilization is the ONLY structural map
    # changing strand count. Record the strand-count of every operator for the map.
    strand_map = {name: n for name, (n, _, _) in OPERATORS.items()}
    w.add_data("operator_strand_counts", strand_map)
    w.add_data("fiber_action_strand_count", 5)  # S5/A5 lives on partitions of 5
    w.add_data("borromean_trace_strand_count", 3)  # H_3

    # --- 5. The bridge probe: does Markov (de)stabilization connect 5 <-> 3? ---
    # To go from H_5 (fiber level) to H_3 (Borromean trace) requires TWO
    # de-stabilizations (remove sigma_4, then sigma_3), each contributing z^{-1}
    # IF the removed strand is disjoint. RAW factor for two de-stabs:
    two_destab = (1 / z) ** 2
    w.add_data("two_destabilization_factor_z_inv_sq_at_q0", str(two_destab))
    w.add_caveat(
        "Markov de-stabilization H_5 -> H_3 is only valid when the removed strands "
        "are DISJOINT from the closure (Markov axiom 3). The Borromean braid "
        "(s1^-1 s2)^3 uses BOTH generators of B_3 non-trivially and is Brunnian "
        "(every 2-sublink is trivial) -- so a strand cannot be removed without "
        "changing the link type. Therefore plain Markov de-stabilization does NOT "
        "give a derived H_5(fiber) -> H_3(Borromean) functor. The 5-strand fiber "
        "object and the 3-strand trace remain in different rep rings. The bridge "
        "is OPEN: a derived map requires either (a) a cabling/satellite operation "
        "(2-cabling a 3-strand pattern -> 6 strands, NOT 5), or (b) an explicit "
        "branching functor Res^{H_5}_{H_3} composed with the fiber decoration -- "
        "neither is supplied by the current framework. No fit attempted."
    )
    w.add_caveat(
        "U(1)_framing, STATED PER LEVEL (the writhe is a property of the braid word, "
        "not of its closure: Markov-I invariant, but Markov-II stabilization shifts "
        "it by +-1 while presenting the same link, so a level must be named). "
        "AT LEVEL n=2 (B_2): writhe is nonzero (+2m) for the torus knots T(2,2m), "
        "including the Hopf sigma_1^2 (w=+2), and for every T(2,odd) lepton carrier. "
        "AT LEVEL n=3 (B_3): writhe is ZERO for the Borromean baryon and for the "
        "figure-eight, and nonzero for T(3,4) (w=+8) and T(3,5) (w=+10). So a "
        "nonzero-writhe operator (e.g. a T(2,2m) color-tube operator) WOULD carry a "
        "nontrivial U(1)_framing phase q^{w.c} AT ITS OWN LEVEL. This is a RAW "
        "structural observation; mapping writhe -> hypercharge Y is NOT derived and "
        "is NOT attempted. The production nucleon uses the writhe-0 Borromean at "
        "n=3, so the framing U(1) is trivial there -- consistent with the s5-so3 "
        "audit. Under the owner ruling (states are Groebner-Shirshov normal forms; "
        "the observable is the trace at the lowest level of the tower, the braid "
        "index) these canonical words ARE the states, so the census compares states "
        "and the per-level readings above stand as written."
    )
    w.add_caveat(
        "LEVEL-INDEPENDENT COMPANION: writhe_minus_level_parity = (w - n) mod 2 is "
        "emitted per row, computed from the stored (writhe, strands_B_n) pair. It is "
        "the COMPLETE invariant of the Markov-II action (w, n) -> (w +- 1, n + 1) "
        "(QOU/StandardModel/WritheLevelParity.lean: markovPair_parity soundness, "
        "markovPair_of_even completeness) and equals the component parity of the "
        "closure. In this census only the Hopf link comes out EVEN (0): it is the "
        "one 2-component closure; every other operator here is odd (1). It carries "
        "exactly ONE BIT and therefore cannot substitute for a magnitude, for "
        "Q = w/2, or for I_3; its fermion/boson reading is separately REFUTED (the "
        "gluon unit sigma_1 sigma_2^{-1} closes to a single component, hence odd, "
        "yet is a boson). Use it ONLY as a consistency check on level-crossing "
        "claims. NOT wired. Ref: docs/audits/2026-08-10-writhe-level-of-definition.md."
    )

    path = w.save()
    elapsed = time.time() - START
    print(f"[knot-operator-census] wrote {path} in {elapsed:.2f}s")
    print(f"  z(q0) = {z}")
    print(f"  tr_M(sigma_1^2)(q0) = {trhopf}")
    print(f"  T(2,2m) writhe = 2m: {[t22m[f'T(2,{2*m})']['writhe'] for m in range(1,6)]}")
    print(f"  Borromean writhe = {writhes['borromean=(s1^-1 s2)^3']['writhe']} "
          f"(at level n={writhes['borromean=(s1^-1 s2)^3']['strands_B_n']})")
    print("  (w-n) mod 2 per operator [level-independent, 1 bit, NOT wired]:")
    for _nm, _r in writhes.items():
        print(f"    {_nm:<26} n={_r['strands_B_n']}  w={_r['writhe']:+d}  "
              f"(w-n)%2={_r['writhe_minus_level_parity']}")


if __name__ == "__main__":
    raise SystemExit(main())
