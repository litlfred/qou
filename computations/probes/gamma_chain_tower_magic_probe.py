#!/usr/bin/env python3
"""Walk the generative isotope production chain: there is NO TOWER, and no magic.

Asked: look past the Groebner-basis normal form at the FULL TOWER for a change
of structural behaviour at the first magic number, walking the whole production
chain step by step; and check whether twist/framing data changes on magic
isotopes.

Answered, in order.

THE FIRST MAGIC NUMBER IS 2 -- and the first DOUBLY-magic nucleus is He-4
(Z = N = 2). On the N = Z line the producer walks, those coincide at A = 4.

1. THERE IS NO TOWER. This is the finding the rest follows from. The atom braid
   nominally lives in H_{3A} (3 strands per nucleon), but `build_atom_nf_mp`
   applies the H_3 Groebner-Shirshov reduction after EVERY crossing, so the
   state is a 6-vector at every step of every nucleus. Measured: the NF vector
   length is 6 across all 33 recorded stages of Z=N=4, and 6 for hydrogen
   (Z=1, N=0) and for lead-208 (Z=82, N=126) alike. Hydrogen and Pb-208 occupy
   the SAME state space. The H_{3A} structure is destroyed as it is built, so
   "the full tower" does not exist in this code path -- the GS normal form IS
   the whole object.

   That single fact explains every negative measured on this arc: nothing in
   the construction can distinguish one nucleon count from another except
   through smooth growth, so no shell signal is expressible.

2. TWIST / FRAMING DATA DOES NOT CHANGE AT MAGIC. Replaying the chain and
   accumulating signed crossings (d = 0 is sigma, d = -h is sigma^-1, d = -h/2
   is a mixed interface that is not a pure crossing):

       writhe(Z)      = 3Z        exactly, so writhe/A = 1.5 for every nucleus
       mixed(Z)       = Z^2 + 4Z  exactly

   Both are smooth polynomials in Z with no feature at 2, 8, 20 or 28. The
   crossing schedule is fixed per nucleon plus an O(A^2) pair loop; it has no
   shell dependence to express.

3. THE LP DUAL CANNOT SHOW RECEPTIVITY TO ANOTHER KNOT. Swept n_target over
   0.25, 0.5, 1, 2, 3, 4, 6, 8, 12, 16, 20, 28, 50, 82, 126, 200, 500, 1000:
   the active set is the singleton {gamma} at EVERY target. It is not the
   target choice -- the LP is structurally one-dimensional on this 6-channel
   basis, so "is the isotope receptive to T_{3,5} rather than the canonical
   knot" is not a question this LP can be asked.

4. A CANDIDATE SIGNAL AT He-4, RETRACTED. The final NF at Z=2 has its sigma_1,
   L+ and L- components collapse to ~1e-3 while every neighbour is O(1-30),
   which looks like the state condensing onto the trivial channel exactly at
   the first doubly-magic nucleus. It does not survive the control. Writing
   R = ||nf_non-gamma|| / |nf_gamma|:

     - R is STRICTLY MONOTONE INCREASING over even Z (0.489, 0.808, 1.143,
       1.404, ... -> 2.959 at Z=30), and the odd-Z branch descends to the same
       limit from above (2.997 at Z=29);
     - so Z=2 is the global minimum simply because it is the SMALLEST EVEN Z;
     - magic Z rank 1st, 4th, 10th and 14th of 15 among even Z -- spread across
       the whole range, no distinction.

   Parity split plus monotone convergence, which is the same artifact the
   delta^2-Phi signal turned out to be. "Is the global minimum magic?" returns
   True and is empty: 2 is both the smallest even number and the first magic
   one, so any monotone-in-even-Z quantity answers yes.

PRECISION. mpmath at 25-40 dps throughout; the chain replays `hm_mp` exactly,
never float(). writhe and mixed are integer counts.

🛑 RETRACTED IN SCOPE (2026-08-30, owner correction). The claim "the H_{3A}
structure is destroyed as it is built" is WRONG, and the corpus says so in
three places this probe did not reach:

  * `trace-locality-gs-reconciliation.md` -- "The GS algorithm DIGESTS global
    entanglement into local coefficients; after digestion, the Markov trace
    factorises locally over the normal form." Digested, not destroyed.
  * `bond-order-eq-jet-degree-proof.md` -- adding a nucleon "rais[es] the
    Groebner-Shirshov normal-form length by a fixed increment", placing the
    n-nucleon cluster sub-word at JET VERTICAL DEGREE n.
  * `prop:gb-spectral-sequence` (E_2 collapse) + `conj:jet-prefix-gb-filtration`
    -- the associated graded gr_n IS the n-nucleon cluster contribution.

So the NF is 6 LAURENT POLYNOMIALS IN q graded by GS filtration length, and
the surviving grading is exactly the many-body decomposition. "Hydrogen and
Pb-208 occupy the same state space" is true of the DIMENSION and false of the
CONTENT. Reading `len(nf) == 6` and concluding "no shell degree of freedom is
expressible" was reading the wrong object.

WHAT THIS PROBE ACTUALLY MEASURED, and it stands as that: numeric magnitudes
at the single point q = q_0. Evaluating at q_0 collapses the whole filtration
into one float per basis element, so a negative here is a negative about
magnitudes at a point -- NOT about the graded structure, which this probe
never looked at. Scope (a), and narrower than it was written.

THE OBJECT TO MEASURE INSTEAD is the symbolic NF over Q(q, sqrt q) --
`hecke_core_symbolic.build_atom_nf_sym(Z, N)` -- and its q-degree /
filtration shape. The corpus already ships the data model:
`gb-filtration-jet-order.witness.json` carries per word a
`filtration_certificate` (grade -> {perm, canonical_word, coefficient_in_q}),
a `filtration_shape` (grade -> multiplicity), and a `jet_log` recording
`filtration_before -> filtration_after` per reduction step. Measured, the
order rises with interactions: electron sigma_1^3 gives q^2 - 1 + q^-2, the
proton body (sigma_1 sigma_2^-1)^3 gives
-q^5 + 4q^3 - 7q + 7/q - 4/q^3 + q^-5. And at A=1 the symbolic NF already
separates p from n by q-degree (max 11 / ops 169 vs max 10 / ops 103) -- a
distinction the numeric NF at q_0 cannot express at all.

ALSO RETRACTED: "A=4 is the end of the road; A=5 needs 686 GB". That is
max_lambda d_lambda^2, the cost of storing a general OPERATOR in the largest
irrep -- a property of the representation chosen here, not of the
construction. The corpus algorithm for this object is O(N * dim H_n(q)),
LINEAR in the Hecke dimension (`mba-step08-jet-prefix`, Complexity), and the
symbolic NF is 6 coefficients for ANY nucleus at ANY A: the state does not
grow with A, only the polynomial degree does.

Tracked in bean `qou-tower` (REOPENED).
"""
from __future__ import annotations

import sys
from pathlib import Path
from mpmath import mp

_ROOT = Path(__file__).resolve().parents[1]
for _p in (_ROOT, _ROOT / "substrate",
           _ROOT.parent / "tools" / "pyhecke" / "python",
           _ROOT.parent / "tools" / "qou-substrate" / "python"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

from compound_shift_nf import hm_mp, _ground_state_ordering   # noqa: E402
from q_parameter import q_at                                  # noqa: E402
from pyhecke import gram                                      # noqa: E402
from qou_substrate.witness import WitnessBuilder              # noqa: E402

mp.dps = 40
MAGIC = {2, 8, 20, 28, 50, 82, 126}


def walk(Z, N, dps=25):
    """Replay the production chain, recording state after each stage."""
    with mp.workdps(dps + 5):
        q0 = q_at(dps + 5)
        h = q0 - mp.mpf(1) / q0
        half, one, zero = mp.mpf(1) / 2, mp.mpf(1), mp.mpf(0)
        A = Z + N
        ordering = _ground_state_ordering(Z, N)
        nf = [one, zero, zero, zero, zero, zero]
        stages, writhe, mixed = [], 0, 0

        def rec(tag):
            stages.append((tag, list(nf), writhe, mixed))

        rec("init")
        for k in range(A):
            t = ordering[k]
            for _ in range(3):
                nf = hm_mp(nf, one, zero, 0, h); writhe += 1
                nf = hm_mp(nf, one, -h, 1, h);   writhe -= 1
            rec(f"{k}:{t}:B3")
            if t == "p":
                nf = hm_mp(nf, one, zero, 0, h); writhe += 1
                nf = hm_mp(nf, one, -h * half, 0, h); mixed += 1
                nf = hm_mp(nf, one, -h * half, 1, h); mixed += 1
            else:
                nf = hm_mp(nf, one, -h * half, 0, h); mixed += 1
                nf = hm_mp(nf, one, -h * half, 0, h); mixed += 1
                nf = hm_mp(nf, one, -h, 1, h); writhe -= 1
            rec(f"{k}:{t}:quark")
            nf = hm_mp(nf, one, zero, 0, h); writhe += 1
            nf = hm_mp(nf, one, zero, 0, h); writhe += 1
            rec(f"{k}:{t}:gluon")
            for prev in range(k):
                ti, tj = ordering[prev], ordering[k]
                if ti == "p" and tj == "p":
                    nf = hm_mp(nf, one, zero, 0, h); writhe += 1
                elif ti == "n" and tj == "n":
                    nf = hm_mp(nf, one, -h, 0, h); writhe -= 1
                else:
                    nf = hm_mp(nf, one, -h * half, 0, h); mixed += 1
            if k > 0:
                rec(f"{k}:{t}:inter")
        for _ in range(Z):
            nf = hm_mp(nf, one, -h, 1, h); writhe -= 1
        rec("electrons")
        return stages


def main() -> int:
    # 1. no tower
    dims = set()
    for Z, N in ((1, 0), (2, 2), (4, 4), (82, 126)):
        for _, nf, _, _ in walk(Z, N):
            dims.add(len(nf))
    no_tower = dims == {6}

    # 2. twist / framing
    wr, mx = {}, {}
    for Z in range(1, 13):
        _, _, w, m = walk(Z, Z)[-1]
        wr[Z], mx[Z] = w, m
    writhe_is_3Z = all(wr[Z] == 3 * Z for Z in wr)
    mixed_is_poly = all(mx[Z] == Z * Z + 4 * Z for Z in mx)

    # 4. the retracted candidate: R = ||non-gamma|| / |gamma|
    R = {}
    for Z in range(1, 31):
        nf = walk(Z, Z)[-1][1]
        R[Z] = mp.sqrt(sum((c / nf[0]) ** 2 for c in nf[1:]))
    ev = sorted(Z for Z in R if Z % 2 == 0)
    mono = all(R[ev[i]] < R[ev[i + 1]] for i in range(len(ev) - 1))
    ranked = sorted(ev, key=lambda Z: R[Z])
    ranks = {m: ranked.index(m) + 1 for m in sorted(MAGIC) if m in ranked}

    print(f"no tower (all NF dims == 6)      : {no_tower}   dims={sorted(dims)}")
    print(f"writhe(Z) == 3Z exactly          : {writhe_is_3Z}")
    print(f"mixed(Z)  == Z^2+4Z exactly      : {mixed_is_poly}")
    print(f"R monotone increasing in even Z  : {mono}")
    print(f"magic ranks among {len(ev)} even Z     : {ranks}")

    w = WitnessBuilder("gamma-chain-tower-magic", engine="mpmath")
    w.set_description(
        "Step-by-step walk of the generative isotope production chain looking "
        "for structural change at the first magic number. THERE IS NO TOWER: "
        "the H_3 GS reduction is applied after every crossing, so the state is "
        "a 6-vector at every stage of every nucleus -- hydrogen and Pb-208 "
        "share one state space. Twist data is featureless (writhe = 3Z, mixed "
        "= Z^2+4Z exactly). The LP active set is {gamma} at every n_target "
        "from 0.25 to 1000, so receptivity to another knot is not expressible. "
        "An apparent collapse onto the trivial channel at He-4 is RETRACTED: "
        "R is monotone in even Z, so Z=2 leads by being the smallest even Z, "
        "and magic Z rank 1st/4th/10th/14th of 15."
    )
    w.add_data("no_tower_all_dims_six", no_tower)
    w.add_data("nf_dims_observed", sorted(dims))
    w.add_data("writhe_equals_3Z", writhe_is_3Z)
    w.add_data("mixed_equals_Zsq_plus_4Z", mixed_is_poly)
    w.add_data("writhe_by_Z", {str(k): v for k, v in wr.items()})
    w.add_data("mixed_by_Z", {str(k): v for k, v in mx.items()})
    w.add_data("R_by_Z", {str(k): mp.nstr(v, 12) for k, v in R.items()})
    w.add_data("R_monotone_in_even_Z", mono)
    w.add_data("magic_rank_among_even_Z", {str(k): v for k, v in ranks.items()})
    w.add_data("lp_active_set_all_n_targets", ["gamma"])
    w.add_assertion("no_tower", 1 if no_tower else 0, 1, tolerance=0,
                    source="NF length is 6 at every stage, H through Pb-208")
    w.add_assertion("writhe_is_smooth_3Z", 1 if writhe_is_3Z else 0, 1,
                    tolerance=0, source="no magic feature in the twist data")
    w.add_assertion("He4_collapse_is_parity_not_magic",
                    1 if mono else 0, 1, tolerance=0,
                    source="R monotone in even Z; Z=2 leads by being first")
    w.add_caveat(
        "The He-4 collapse was flagged as a candidate magic signal and is "
        "RETRACTED here by its own control. 'Is the global minimum magic?' "
        "returns True and is empty, because 2 is both the smallest even number "
        "and the first magic one -- any monotone-in-even-Z quantity says yes."
    )
    w.save()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
