#!/usr/bin/env python3
"""dt_d1b_gabriel_route_void_source_verified_probe.py — qou-q9ih D1-b.

**THIS PROBE VOIDS ITS OWN SIBLING'S PREMISE, not merely its answer.**

`dt_d1b_arrow_count_forced_by_gabriel_probe.py` has now given two answers to the
arrow question — "forced to 0 or 1", then "in {0,1,2} with V unpinned". Both
presuppose that the corpus's `(4,3)` datum counts **indecomposable objects of a
finite-representation-type quiver**. That presupposition was never checked
against the source. It is checked here, and it is **false**.

═══ THE SOURCE, QUOTED ═══

The datum is GGM `arXiv:2012.00062v3` eq (98), held in this repo at
`library/arxiv-2012.00062v3/sections/sec-007-2-borel-resummation-and-stokes-
automorphisms.md`. Immediately under eq (96)/(97) the paper says, verbatim:

    "where the non-vanishing off-diagonal entry of S_{σi,σj} is the Stokes
     constant associated to the Borel singularity ι_{i,j}. Assembling these
     off-diagonal entries in a matrix, we obtain the matrix [eq 98]"

So each entry is **one Stokes constant at one Borel singularity** — a
multiplicity at a single charge. `Ω(ι_{1,2}) = 4` is a degeneracy of four at one
ray, NOT four distinct objects at four distinct charges.

═══ WHY THAT VOIDS GABRIEL ═══

Gabriel: for an acyclic quiver with `W = 0`, finite representation type <=> ADE,
and then the indecomposables are in bijection with the **positive roots**, each
occurring with multiplicity **exactly one**. So for any finite-type quiver

    max_d Ω_d = 1.

The datum has `max |Ω| = 4`. **A finite-type quiver cannot carry it**, at any
rank, with any arrow count. Gabriel's theorem is not underdetermined here — it is
inapplicable, and every arrow count either sibling probe reported is void.

This is a scope-(b) **structural exclusion** in the sense of AGENTS.md: the
invariant cited is Gabriel's bijection itself (multiplicity one per positive
root), not a failed numerical search.

═══ WHAT THE SOURCE GIVES BACK — a real constraint, not a fit ═══

Two structural facts, both mechanical consequences of the source's own eq (96)
and eq (97), neither previously recorded anywhere in this corpus (six-path
grep: 0 hits for the ray-orientation fact, 0 for eq (100)):

  (F1) The index set is **three** σ-indexed perturbative series, so the Stokes
       matrices are 3x3 and the singularities ι_{i,j} run over ORDERED PAIRS —
       six of them, not three.

  (F2) S+ uses {(3,1),(3,2),(1,2)} and S- uses {(1,3),(2,3),(2,1)}. These are
       **exactly the two opposite orientations of the same three unordered
       pairs** {12,13,23}. The bar-conjugate "ray pair" the corpus is looking
       for is therefore not two arbitrary stability rays — it is the two
       orientations of a 3-node complete graph.

  (F3) eq (100): `S^(k)_{σi,σj} = -S^(k)_{σφ(i),σφ(j)}` for `i≠j`, with
       `φ = (1 2)`. Stated in the source for the q-series coefficients; this
       probe CHECKS whether it also holds on the eq-(98) constants (it could
       fail — that is a real control, not a restatement).

       φ is **sign-reversing**, hence count-breaking, which is exactly what
       `QuiverMirrorAutomorphismExcluded` requires of any mirror implementation
       reading (4,3): `Ω(σd) ≠ Ω(d)`. The source's own symmetry and the corpus's
       Lean exclusion agree. That agreement is a cross-check, not an input.

═══ WHAT IS **NOT** CLAIMED ═══

F2 makes "V = 3, arrows = the three unordered pairs" the obvious guess. It is
recorded below as a **labelled HYPOTHESIS with its disconfirmation test**, and
it is NOT a result. The reason is precise and is the same reason the sibling
probe went wrong twice: in the KS quiver description the arrows are given by the
**Dirac pairing on the charges**, not by which Borel singularities happen to be
populated. F2 says which singularities are populated. That is evidence about the
arrow set; it is not the arrow set.

Predicted before measuring, and recorded either way:
  P1: eq (100) holds on the eq-(98) constants.          -> checked in C4
  P2: the two ray sets are exact orientation-reverses.  -> checked in C2
  P3: max |Ω| over eq (98) is 4, hence > 1.             -> checked in C3

Exact integer arithmetic throughout; no floats anywhere. Self-contained apart
from the witness builder.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402

# ---------------------------------------------------------------------------
# The single certified input: GGM 2012.00062v3 eq (98), 0-indexed.
# ---------------------------------------------------------------------------
DT = [
    [0, 4, 3],
    [-4, 0, -3],
    [-3, 3, 0],
]

# eq (96) / eq (97): the ordered pairs (i,j) whose elementary factor appears.
SPLUS_FACTORS = [(2, 0), (2, 1), (0, 1)]
SMINUS_FACTORS = [(0, 2), (1, 2), (1, 0)]

SOURCE_QUOTE = (
    "where the non-vanishing off-diagonal entry of S_{sigma_i,sigma_j} is the "
    "Stokes constant associated to the Borel singularity iota_{i,j}. Assembling "
    "these off-diagonal entries in a matrix, we obtain the matrix (98)"
)
SOURCE_PATH = ("library/arxiv-2012.00062v3/sections/"
               "sec-007-2-borel-resummation-and-stokes-automorphisms.md")


def _elem(i, j):
    M = [[1 if a == b else 0 for b in range(3)] for a in range(3)]
    M[i][j] += DT[i][j]
    return M


def _mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)]
            for i in range(3)]


def _splus():
    return _mul(_mul(_elem(2, 0), _elem(2, 1)), _elem(0, 1))


def _sminus():
    return _mul(_mul(_elem(0, 2), _elem(1, 2)), _elem(1, 0))


def main() -> int:
    print("=" * 78)
    print(" D1-b — the Gabriel route is VOID (source-verified against eq 98)")
    print("=" * 78)

    checks = []

    # -- C1 (control): reproduce the source's typed matrices and eq (17). ----
    Sp, Sm = _splus(), _sminus()
    Sp_typed = [[1, 4, 0], [0, 1, 0], [-3, -9, 1]]
    Sm_typed = [[1, 0, 3], [-4, 1, -3], [0, 0, 1]]
    SpT = [[Sp[j][i] for j in range(3)] for i in range(3)]
    I3 = [[1 if a == b else 0 for b in range(3)] for a in range(3)]
    c1 = (Sp == Sp_typed and Sm == Sm_typed and _mul(SpT, Sm) == I3)
    print("\n  ── C1 control: reconstruct S±(0) from eq (98) ──")
    print(f"     S+(0) = {Sp}")
    print(f"     S-(0) = {Sm}")
    print(f"     eq-(17)  S+(0)^T · S-(0) = I  : {_mul(SpT, Sm) == I3}")
    checks.append((c1, "C1_source_matrices_reproduce",
                   "eq (96),(97) rebuilt from the eq-(98) entries reproduce the "
                   "typed S±(0) and satisfy the eq-(17) inversion relation. This "
                   "is the control on the arithmetic below -- if it failed, "
                   "nothing else in this probe would be about the source"))

    # -- C2 (F2): the two ray sets are orientation-reverses. -----------------
    plus_set = set(SPLUS_FACTORS)
    minus_set = set(SMINUS_FACTORS)
    reversed_plus = {(j, i) for (i, j) in SPLUS_FACTORS}
    unordered_plus = {frozenset(p) for p in SPLUS_FACTORS}
    unordered_minus = {frozenset(p) for p in SMINUS_FACTORS}
    all_unordered = {frozenset(p) for p in [(0, 1), (0, 2), (1, 2)]}
    c2 = (reversed_plus == minus_set
          and unordered_plus == unordered_minus == all_unordered
          and plus_set.isdisjoint(minus_set))
    print("\n  ── C2 (F2): are the two rays the two ORIENTATIONS of one graph? ──")
    print(f"     S+ rays (0-indexed) : {sorted(plus_set)}")
    print(f"     S- rays (0-indexed) : {sorted(minus_set)}")
    print(f"     reverse(S+) == S-   : {reversed_plus == minus_set}")
    print(f"     both cover all three unordered pairs : "
          f"{unordered_plus == unordered_minus == all_unordered}")
    print(f"     ordered sets disjoint : {plus_set.isdisjoint(minus_set)}")
    checks.append((c2, "C2_ray_pair_is_the_two_orientations_of_K3",
                   "P2 CONFIRMED. S+ and S- populate exactly the two opposite "
                   "orientations of the SAME three unordered pairs {12,13,23}. "
                   "The bar-conjugate ray pair is not two arbitrary stability "
                   "rays -- it is the two orientations of a 3-node complete "
                   "graph. Not previously recorded in this corpus"))

    # -- C3 (the result): max |Ω| = 4 > 1 excludes finite type. --------------
    omegas = {(i, j): DT[i][j] for i in range(3) for j in range(3) if i != j}
    max_abs = max(abs(v) for v in omegas.values())
    c3 = (max_abs == 4 and max_abs > 1)
    print("\n  ── C3 (THE RESULT): Gabriel needs max Ω = 1; the datum has 4 ──")
    for (i, j), v in sorted(omegas.items()):
        print(f"     Ω(ι_{i+1},{j+1}) = {v:>3}")
    print(f"     max |Ω| = {max_abs}")
    print("     Gabriel: indecomposables <-> positive roots, multiplicity ONE")
    print("              => any finite-type quiver has max Ω = 1")
    print(f"     {max_abs} > 1  ⇒  NO finite-type quiver carries this datum,")
    print("                     at any rank, with any arrow count.")
    checks.append((c3, "C3_finite_type_EXCLUDED_max_omega_is_4",
                   "P3 CONFIRMED, and this is the result. The source says each "
                   "eq-(98) entry is ONE Stokes constant at ONE Borel "
                   "singularity iota_{i,j} -- a multiplicity at a single "
                   "charge, not a count of distinct objects. Gabriel's "
                   "bijection gives every positive root multiplicity exactly "
                   "one, so a finite-type quiver has max Omega = 1. The datum "
                   "has max |Omega| = 4. Scope-(b) structural exclusion: the "
                   "cited invariant is Gabriel's bijection itself"))

    # -- C4 (F3): does eq (100) hold on the eq-(98) constants? ---------------
    phi = {0: 1, 1: 0, 2: 2}   # φ = (1 2) in the paper's 1-indexing
    eq100_rows = []
    eq100_ok = True
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            lhs = DT[i][j]
            rhs = -DT[phi[i]][phi[j]]
            eq100_rows.append(((i + 1, j + 1), lhs, rhs, lhs == rhs))
            eq100_ok = eq100_ok and (lhs == rhs)
    print("\n  ── C4 (F3): eq (100)  S_{ij} = −S_{φ(i)φ(j)},  φ = (1 2) ──")
    for (pair, lhs, rhs, ok) in eq100_rows:
        print(f"     (i,j)={pair}:  {lhs:>3}  vs  −S_φ = {rhs:>3}   "
              f"{'ok' if ok else 'MISMATCH'}")
    print(f"     holds on the eq-(98) constants: {eq100_ok}")
    print("     φ is SIGN-REVERSING ⇒ count-breaking ⇒ agrees with the corpus's")
    print("     QuiverMirrorAutomorphismExcluded (any mirror reading (4,3) must")
    print("     have Ω(σd) ≠ Ω(d)). Independent agreement, not an input.")
    checks.append((eq100_ok, "C4_eq100_mirror_holds_and_is_count_breaking",
                   "P1 CONFIRMED. The source states eq (100) for the q-series "
                   "coefficients S^(k); it is checked here on the eq-(98) "
                   "constants and holds. phi = (1 2) is sign-reversing, hence "
                   "count-breaking -- exactly what the Lean "
                   "QuiverMirrorAutomorphismExcluded requires of any mirror "
                   "implementation that reads (4,3). The source's own symmetry "
                   "and the corpus's proved exclusion agree independently"))

    # -- C5: what this does to the sibling probe's two answers. --------------
    voided = {
        "first_version": "arrows forced to 0 or 1",
        "corrected_version": "arrows in {0,1,2}, V unpinned",
    }
    c5 = True
    print("\n  ── C5: both sibling answers are VOID, for the SAME reason ──")
    for k, v in voided.items():
        print(f"     {k:<20} '{v}'  → void")
    print("     Neither is arithmetically wrong. Both apply Gabriel to a datum")
    print("     Gabriel cannot describe. Patching the answer a third time would")
    print("     have kept the defect; the premise is what had to be tested.")
    checks.append((c5, "C5_both_sibling_answers_are_void_same_reason",
                   "Neither sibling answer is arithmetically wrong; both apply "
                   "Gabriel's theorem to a datum outside its hypotheses. The "
                   "error was never in the enumeration -- it was in never "
                   "checking the premise against the source, which is one grep "
                   "of a paper this repo already holds"))

    # -- C6: the hypothesis, LABELLED, with its disconfirmation test. --------
    c6 = True
    print("\n  ── C6: HYPOTHESIS (labelled, NOT a result) ──")
    print("     H: V = 3 (the three σ), arrows = the three unordered pairs = 3,")
    print("        the two rays being the two orientations.")
    print("     Why it is only a hypothesis: in the KS description the arrows")
    print("        are the DIRAC PAIRING on the charges, not the set of")
    print("        populated Borel singularities. F2 says which singularities")
    print("        are populated. That is evidence about the arrow set, not the")
    print("        arrow set.")
    print("     DISCONFIRMATION TEST: compute the Dirac pairing ⟨γ_i,γ_j⟩ on the")
    print("        charge lattice of the 5₂ spectral curve and compare with the")
    print("        eq-(98) support. If the pairing is not supported on exactly")
    print("        {12,13,23}, H is dead. That test needs charge-lattice data")
    print("        this probe does not have, and is the honest next rung.")
    checks.append((c6, "C6_hypothesis_is_labelled_not_claimed",
                   "H: V=3 with 3 arrows (the three unordered pairs), rays = "
                   "the two orientations. Recorded as a CANDIDATE with its "
                   "disconfirmation test (compute the Dirac pairing on the 5_2 "
                   "charge lattice; if it is not supported on {12,13,23}, H is "
                   "dead). Not claimed, not wired, not a derivation"))

    # -- C7: antisymmetry discriminates NOTHING (the next trap, pre-empted). --
    antisym = all(DT[i][j] == -DT[j][i] for i in range(3) for j in range(3))
    # How many antisymmetric 3x3 integer matrices with entries in [-4,4] are
    # there? Three free upper-triangular entries, 9 choices each.
    population = 9 ** 3
    c7 = (antisym and population > 1)
    print("\n  ── C7: the antisymmetry of eq (98) is NOT evidence for H ──")
    print(f"     eq (98) is antisymmetric: {antisym}")
    print("     TWO readings both ENTAIL antisymmetry, so observing it")
    print("     discriminates neither:")
    print("       R_source  Ω(ι_ij) = −Ω(ι_ji) — the CPT / particle-antiparticle")
    print("                 sign on Stokes constants.  This is what the paper says.")
    print("       R_pairing B_ij = −B_ji — an exchange matrix, by definition.")
    print("     And they give DIFFERENT arrow counts off the same matrix:")
    print("       R_pairing reads arrows straight off |B|: 4 + 3 + 3 = 10 on 3 nodes")
    print("       H (from F2, populated singularities):    3 on 3 nodes")
    print(f"     Antisymmetric 3x3 integer matrices with entries in [-4,4]: "
          f"{population}.")
    print("     eq (98) is one of them and is not distinguished by being one, so")
    print("     'it looks like an exchange matrix' has no evidential weight at all.")
    checks.append((c7, "C7_antisymmetry_discriminates_nothing",
                   "Pre-empting the next available misreading, which is the same "
                   "shape as the two already made. eq (98) IS antisymmetric, and "
                   "an antisymmetric integer matrix indexed by three objects "
                   "looks exactly like a quiver exchange matrix -- reading it as "
                   "one gives arrows 4+3+3 = 10 on 3 nodes, a DIFFERENT answer "
                   "from H's 3. But BOTH readings entail antisymmetry (CPT sign "
                   "on Stokes constants vs B_ij = -B_ji by definition), so "
                   f"observing it separates them not at all; there are {population} "
                   "antisymmetric 3x3 integer matrices with entries in [-4,4] and "
                   "eq (98) is not distinguished by being one of them. The source "
                   "says Stokes constants; that is the only thing deciding it here"))

    # ---------------- witness ------------------------------------------------
    wb = WitnessBuilder("dt-d1b-gabriel-route-void-source-verified",
                        engine="exact-integer-source-verification")
    wb.set_description(
        "qou-q9ih D1-b. This probe VOIDS THE PREMISE of its sibling "
        "dt_d1b_arrow_count_forced_by_gabriel_probe, which has now given two "
        "different arrow counts ('forced to 0 or 1', then 'in {0,1,2}'). Both "
        "presuppose the corpus's (4,3) datum counts INDECOMPOSABLES of a "
        "finite-representation-type quiver. Checked against the source for the "
        "first time: GGM arXiv:2012.00062v3, held in this repo, says under eq "
        "(96)/(97) that each eq-(98) entry is 'the Stokes constant associated "
        "to the Borel singularity iota_{i,j}' -- a MULTIPLICITY AT ONE CHARGE. "
        "Gabriel's bijection gives every positive root multiplicity exactly "
        "one, so any finite-type quiver has max Omega = 1; the datum has max "
        "|Omega| = 4. NO finite-type quiver carries it at any rank with any "
        "arrow count, so both sibling answers are void -- scope-(b), the cited "
        "invariant being Gabriel's bijection itself. What the source gives "
        "back: the index set is THREE sigma-series so the singularities run "
        "over SIX ordered pairs, and S+ and S- populate exactly the two "
        "OPPOSITE ORIENTATIONS of the same three unordered pairs {12,13,23} -- "
        "the bar-conjugate ray pair is the two orientations of a 3-node "
        "complete graph, not two arbitrary stability rays. Neither that fact "
        "nor eq (100) was previously recorded in this corpus. eq (100)'s "
        "mirror phi = (1 2) is SIGN-REVERSING, hence count-breaking, agreeing "
        "independently with the Lean QuiverMirrorAutomorphismExcluded. The "
        "obvious reading V=3 with 3 arrows is recorded as a LABELLED "
        "HYPOTHESIS with its disconfirmation test, NOT as a result: KS arrows "
        "are the Dirac pairing on charges, not the populated singularities.")
    wb.add_data("source", {
        "paper": "Garoufalidis-Gu-Marino, arXiv:2012.00062v3, "
                 "'Peacock patterns and resurgence in complex Chern-Simons "
                 "theory'",
        "held_at": SOURCE_PATH,
        "quote_under_eq_96_97": SOURCE_QUOTE,
        "reading_established": "each eq-(98) entry is ONE Stokes constant at "
                               "ONE Borel singularity: a multiplicity at a "
                               "single charge, not a count of distinct objects",
    })
    wb.add_data("eq98_matrix", DT)
    wb.add_data("ray_structure", {
        "n_sigma": 3,
        "n_ordered_pairs": 6,
        "splus_rays_1indexed": [[i + 1, j + 1] for (i, j) in SPLUS_FACTORS],
        "sminus_rays_1indexed": [[i + 1, j + 1] for (i, j) in SMINUS_FACTORS],
        "reverse_of_splus_equals_sminus": reversed_plus == minus_set,
        "common_unordered_support": [[1, 2], [1, 3], [2, 3]],
    })
    wb.add_data("gabriel_exclusion", {
        "max_abs_omega": max_abs,
        "finite_type_max_omega": 1,
        "verdict": "finite representation type EXCLUDED",
        "scope": "(b) structural -- invariant cited is Gabriel's bijection "
                 "(positive roots <-> indecomposables, multiplicity one)",
    })
    wb.add_data("voided_sibling_answers", voided)
    wb.add_data("hypothesis_H", {
        "statement": "V = 3 (the three sigma), arrows = the three unordered "
                     "pairs = 3, the two rays being the two orientations",
        "tier": "labelled CANDIDATE -- not claimed, not wired",
        "why_not_a_result": "KS arrows are the Dirac pairing on the charge "
                            "lattice, not the set of populated Borel "
                            "singularities",
        "disconfirmation_test": "compute <gamma_i,gamma_j> on the 5_2 spectral-"
                                "curve charge lattice; if it is not supported "
                                "on exactly {12,13,23}, H is dead",
    })
    wb.add_data("predictions_recorded_before_measuring", {
        "P1_eq100_holds_on_eq98": eq100_ok,
        "P2_rays_are_orientation_reverses": reversed_plus == minus_set,
        "P3_max_omega_exceeds_one": max_abs > 1,
    })
    wb.add_data("wall_crossing_scaffolding_is_orphaned", {
        "module": "folio/quantum-observable-universe/lean/QOU/Mathlib/"
                  "WallCrossing.lean",
        "carries": "ChargeLattice (antisymmetric integral Euler pairing), "
                   "CentralCharge, BPSState, BPSSpectrum, Wall, KSWallCrossing",
        "instances_of_ChargeLattice": 0,
        "instances_of_KSWallCrossing": 0,
        "importers": 0,
        "mentions_anywhere_else_in_the_paper_tree": 0,
        "importers_is_NOT_the_interesting_number": "CORRECTED 2026-09-04 in "
            "the same session it was written. '0 importers' was reported as "
            "though it were a finding; it is not. Measured over the QOU tree: "
            "866 of 2566 modules (33.8%) are never imported anywhere, and this "
            "is a long-tracked class with its own detector "
            "(folio/pipeline/lean-orphan-audit.ts, beans qou-orph / "
            "qou-kljb). Being unimported makes this module ORDINARY. The "
            "library is glob-declared so it still compiles",
        "what_is_actually_specific": "ZERO INSTANCES of ChargeLattice and "
            "KSWallCrossing anywhere in the tree. That is a different and "
            "stronger statement than unimported -- an imported module can have "
            "no instances, and an unimported one can have instances inside "
            "itself -- and it is the fact that blocks the D1-b Dirac-pairing "
            "test. Quote the instance count, not the importer count",
        "qou_modules_total": 2566,
        "qou_modules_never_imported": 866,
        "note": "measured 2026-09-04 by grep over content/quantum-observable-"
                "universe/ excluding .lake/. Deliberately NOT instantiated "
                "here: giving it eq (98) as its euler field would assert that "
                "eq (98) IS the Dirac pairing, which is precisely hypothesis H "
                "and would launder it into Lean",
    })
    wb.add_data("scope", {
        "tier": "scope-(b) exclusion + source-verified structural facts",
        "method": "exact integer algebra on the source's own eq (96)-(98); "
                  "no search, no fit, no tuning",
        "arithmetic": "exact integers throughout; no floats",
        "derives_A_omega": False, "wired": False, "fit": False,
    })

    for ok, name, detail in checks:
        wb.add_assertion(name, computed="PASS" if ok else "FAIL",
                         expected="PASS", tolerance="exact", source=detail)
    wb.save()

    n_ok = sum(1 for ok, _, _ in checks if ok)
    print(f"\n  {n_ok}/{len(checks)} checks passed")
    return 0 if n_ok == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
