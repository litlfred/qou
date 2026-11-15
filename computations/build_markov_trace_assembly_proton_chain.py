#!/usr/bin/env python3
"""
Frontier-paydown chain — Proton Markov-trace assembly, on the CANONICAL word.

Companion to `build_markov_trace_assembly_{neutron,deuteron}_chain.py`. Written
2026-09-13 for bean `qou-nhkv`, which this closes.

WHY THIS FILE EXISTS AT ALL
---------------------------
`markov-trace-assembly-proton.derivation.json` was an ORPHAN: consumed by live
code (`applied_uniqueness_mass_table.py`, `braid_encoding_audit.py`,
`markov/assembly_chain_11_letter_recompute_probe.py`) while its only builder sat
in `fsh-guts/deprecated/computations/`. Its neutron and deuteron siblings both had live
builders and were regenerated canonical on 2026-09-13, so the cluster went
mixed-frame: proton grouped at 1.14575969…, the other two canonical. An 82 %
disagreement inside one table, gated red in `applied_uniqueness_mass_table`.

UN-DEPRECATING THE OLD BUILDER WOULD NOT HAVE FIXED IT. That builder computes a
different object: its own docstring asserts a "6-crossing word, all positive
sigma" and reports tr_M(p, q_0) ≈ 2.12258 — the fifth claimant in
`trm_proton_five_values_census` (bean `qou-soj6`), listed there as UNEXPLAINED.
It is deprecated for a reason, and reviving it would have replaced a grouped-era
value with a wrong-word one.

WHAT THIS BUILDER DOES DIFFERENTLY FROM ITS SIBLINGS
----------------------------------------------------
The neutron and deuteron chains carry a documented defect their own text
describes: steps 5–7 evaluate χ^λ from the n₊/n₋ counts of a LEGACY 5-letter
σ-word, which is a different element of H₃(q) from the 11-letter one their own
step 4 declares. Their leaf is right and their symbolic intermediate is
"illustrative-only"; `assembly_chain_11_letter_recompute_probe` exists to record
that gap, and `qou-nhkv` says in as many words not to carry the premise across.

So this chain does **not** replicate it. Its character steps are computed on the
CANONICAL 11-letter element by the corpus's own symbolic route —
`markov_weights_symbolic.tr_M_canonical`, χ^λ as the trace of the seminormal
matrix product with each letter (c, d, g) acting as c·ρ(σ_g) + d·1 — which is
the route `atom_braid_word_3A`'s docstring names as the only valid one. There is
no legacy-convention frontier in this chain.

THE WORD, from two independent sources that agree
-------------------------------------------------
`atomic-braid-recipe-p-canonical.derivation.json` (regenerated 2026-09-13) gives
an 11-letter word with {σ: 6, σ⁻¹: 3, averaged: 2}. `trm_proton_five_values_census`
independently records `canonical_word_for(1, 0)` as
`[[1,1]x4, [0,1], [1,1]x2, [-1,2]x3, [0,2]]` — the same breakdown, reached by a
different route.

TERMINOLOGY, per `atom_braid_word_3A`'s own docstring: the 11 are LETTERS, not
crossings. The object is a product of Hecke elements c·σ_g + d·1, and no
topological quantity may be read off it.

Output: `markov-trace-assembly-proton.derivation.json`.
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — bridge: cross-cluster witness lookup
import _path_bridge as _pb  # noqa: E402
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent / "markov"))
from derivation_chain import (  # noqa: E402
    DerivationChain,
    DerivationStep,
    FirstPrinciple,
    TrustBasis,
)

HERE = Path(__file__).parent
OUTPUT = _pb.witness_path("markov-trace-assembly-proton.derivation.json", HERE)

# The leaf, READ rather than hardcoded — the discipline the whole qou-4383
# tranche established. `canonical_trm_reference` selects its witness by recorded
# q0 AND refuses one in the wrong or an undeclared intra-nucleon ordering (bean
# qou-y4gi), so this chain cannot silently inherit a superseded frame the way
# its siblings did.
from canonical_trm_reference import tr_m_nucleon  # noqa: E402

from _precision import fmt  # noqa: E402

# NO `float()` HERE. `tr_m_nucleon` returns an mpf carrying 60 digits
# (0.629328402202921918165345746778485927600219400634359762811677); the cast
# this line used to make kept 16 and wrote the result into
# `markov-trace-assembly-proton.derivation.json` as a raw JSON float, which the
# raw-float64 ratchet counts. Bean `qou-btqh` had already drained that exact
# field 6 -> 0 (PR #6569) and removed its baseline row; this builder was written
# fresh nine days later under `qou-nhkv` and reintroduced the cast, so the
# reappearance surfaces as NEW rather than REGRESSED.
#
# Keep the mpf for arithmetic and serialize ONCE with `_precision.fmt`. Every
# consumer already parses through `mp.mpf(str(...))` and two of them gain by it:
# `assembly_chain_11_letter_recompute_probe` derives its tolerance from the
# stored precision, so a full-precision string tightens that check by ~44 orders
# rather than loosening anything. `float()` survives below only inside f-strings,
# which is display (bean `qou-ejfy`).
PROTON_TR_M_Q0 = tr_m_nucleon("proton")
PROTON_TR_M_Q0_STR = fmt(PROTON_TR_M_Q0)


def _canonical_word():
    """(letters, {type: count}) for the canonical proton element, computed live."""
    import markov_weights_symbolic as M  # noqa: PLC0415
    cr = M.atom_braid_word_3A_to_crossings(1, 0, include_inter=False)
    # COUNT THE TYPE, NOT THE INDEX. `atom_braid_word_3A_to_crossings` returns
    # (generator_index, type_string) pairs — (0, 'sigma'), (1, 'sigma_inv'), … —
    # NOT the (c, d, g) Hecke triples that `atom_braid_word_3A` itself returns,
    # and not the [sign, generator] pairs the census prints. The first draft of
    # this function read element [0] as a sign and produced
    # "{σ: 4, σ⁻¹: 0, averaged: 7}", contradicting the recipe chain it claims to
    # agree with. Three tuple shapes for one object in one neighbourhood is a
    # trap; count the field that says what it is.
    counts = {"sigma": 0, "sigma_inv": 0, "averaged": 0}
    for c in cr:
        counts[c[1]] = counts.get(c[1], 0) + 1
    return cr, counts


def build() -> DerivationChain:
    cr, counts = _canonical_word()
    word_desc = (f"{len(cr)} letters "
                 f"{{σ: {counts['sigma']}, σ⁻¹: {counts['sigma_inv']}, "
                 f"averaged: {counts['averaged']}}}")
    steps: list[DerivationStep] = []

    steps.append(DerivationStep(
        name="Partitions of 3 — Schur–Weyl basis at A=1",
        operation=(
            "By Schur–Weyl duality the A=1 ambient Hecke algebra is H_3(q); "
            "partitions of 3 are (3), (2,1), (1,1,1). Same basis as the "
            "neutron and deuteron assemblies."
        ),
        inputs=[FirstPrinciple.SCHUR.value, FirstPrinciple.WEDDERBURN.value],
        output_name="partitions_of_3",
        output_value=[{"lambda": "(3)", "f": 1},
                      {"lambda": "(2,1)", "f": 2},
                      {"lambda": "(1,1,1)", "f": 1}],
        trust_basis=TrustBasis.AXIOM,
        # Same stub the neutron and deuteron chains declare on their identical
        # step; copied rather than invented, so the three siblings discharge
        # this axiom against the same reference.
        lean_ref="qou:STUB:PartitionsOfN",
        citation="schur1901",
        jet_order=0,
        gb_filtration_level=0,
    ))

    steps.append(DerivationStep(
        name="Convention-D Wedderburn weights y_λ(q) at H_3",
        operation=(
            "y_λ(q) from `markov_weights_symbolic.solve_y_lambda(3)`, the "
            "ladder linear system A y = b with A_{ij} = χ^{λ_j}(σ_1⋯σ_{i-1}) "
            "and b_i = z^i, z = q³/(q²+1) — convention D, owner ruling "
            "2026-08-09. Under D the three-row weight VANISHES: y_(1,1,1) = 0, "
            "which is the level r = 2 row cap (bean qou-fq0f). The sign-rep "
            "character therefore cannot affect this assembly at all."
        ),
        inputs=["partitions_of_3", FirstPrinciple.WEDDERBURN.value],
        output_name="y_lambda_H3",
        output_value="y_(3) = (q⁴+1)/(q²+1)², y_(2,1) = q²/(q²+1)², y_(1,1,1) = 0",
        trust_basis=TrustBasis.DERIVED,
        citation="wenzl1988",
        jet_order=0,
        gb_filtration_level=0,
    ))

    steps.append(DerivationStep(
        name="Atomic-braid recipe for the proton — chain reference",
        operation=(
            "Reference `atomic-braid-recipe-p-canonical.derivation.json`: the "
            f"canonical proton element is {word_desc}, from quark content "
            "(u, u, d) + B₃ confinement + the borromean intra-nucleon core "
            "(σ₀σ₁⁻¹)³ made canonical by the 2026-09-05 owner ruling, bean "
            "`qou-hu1f`. "
            "TWO INDEPENDENT SOURCES AGREE on this word: the recipe chain, and "
            "`trm_proton_five_values_census`, which records "
            "canonical_word_for(1,0) = [[1,1]x4, [0,1], [1,1]x2, [-1,2]x3, "
            "[0,2]] — the same breakdown by a different route. "
            "NOTE THE CONTRAST WITH THE SIBLING CHAINS: their steps 5–7 use a "
            "legacy 5-letter σ-word and their symbolic intermediate is "
            "illustrative-only. This chain does not do that; the character "
            "steps below are computed on the canonical element itself."
        ),
        inputs=["partitions_of_3", FirstPrinciple.HECKE_ENERGY.value],
        output_name="T_w_p",
        output_value=f"T_w_p = canonical element, {word_desc}",
        trust_basis=TrustBasis.DERIVED,
        citation="manuscript:§Atomic-braid recipe",
        jet_order=0,
        notes=(
            "Derivation chain: atomic-braid-recipe-p-canonical.derivation.json "
            "(builder: build_atomic_braid_recipe_canonical_chain.py). "
            "TERMINOLOGY: the 11 are LETTERS, not crossings — the object is a "
            "product of Hecke elements c·σ_g + d·1 and atom_braid_word_3A's "
            "docstring forbids reading a topological quantity off it."
        ),
    ))

    steps.append(DerivationStep(
        name="Characters χ^λ_q(T_w_p) on the canonical element",
        operation=(
            "χ^λ as the trace of the seminormal matrix product for the "
            "canonical element, each letter (c, d, g) acting as "
            "c·ρ_λ(σ_g) + d·1 — `markov_weights_symbolic.chi_lambda_symbolic`. "
            "This is the route `atom_braid_word_3A`'s docstring names as the "
            "only valid one, and it applies the averaged-letter factor that "
            "the sibling chains' legacy steps omit. Exact over Q(q); no "
            "float64 anywhere."
        ),
        inputs=["T_w_p", "partitions_of_3"],
        output_name="chi_lambda_proton",
        output_value="symbolic Laurent polynomials in q, one per λ ⊢ 3",
        trust_basis=TrustBasis.DERIVED,
        citation="hoefsmit1974",
        jet_order=0,
        gb_filtration_level=0,
    ))

    steps.append(DerivationStep(
        name="Finite-Jones assembly tr_M(p) = Σ_λ y_λ χ^λ",
        operation=(
            "The Ocneanu/Jones–Markov trace as the y-weighted character sum, "
            "`markov_weights_symbolic.tr_M_canonical(crossings, 3)`. With "
            "y_(1,1,1) = 0 under convention D the sum runs over (3) and (2,1) "
            "only."
        ),
        inputs=["y_lambda_H3", "chi_lambda_proton",
                FirstPrinciple.FINITE_JONES.value],
        output_name="tr_M_proton_symbolic",
        output_value="symbolic Laurent polynomial in q",
        trust_basis=TrustBasis.DERIVED,
        citation="jones1987",
        jet_order=0,
        gb_filtration_level=0,
    ))

    steps.append(DerivationStep(
        name="Evaluate tr_M(p, q_0) at the proton pin",
        operation=(
            "Substitute q := q_0 into the symbolic assembly. The value is READ "
            "from `canonical_trm_reference.tr_m_nucleon('proton')` rather than "
            "restated, so it cannot drift from its witness, and that accessor "
            "refuses a witness in the wrong or an undeclared intra-nucleon "
            "ordering (bean `qou-y4gi`)."
        ),
        inputs=["tr_M_proton_symbolic"],
        output_name="tr_M_proton_q0",
        output_value=PROTON_TR_M_Q0_STR,
        trust_basis=TrustBasis.COMPUTATIONAL,
        jet_order=0,
        gb_filtration_level=0,
        spectral_stratum="archimedean (q_0 ∈ ℝ_{>1})",
        notes=(
            "INDEPENDENTLY CONFIRMED: assembly_chain_11_letter_recompute_probe "
            "evaluates the same canonical element by the same seminormal route "
            "and obtains 0.62932840220292191817 at the proton pin. That probe "
            "predates this chain and shares no code path with the witness this "
            "leaf reads."
        ),
    ))

    return DerivationChain(
        target="tr_M(p, q_0)  [canonical Wenzl-bridge, canonical 11-letter element]",
        target_value=PROTON_TR_M_Q0_STR,
        target_tolerance=1e-9,
        content_block="prop:full-pole-structure-mass-trace",
        description=(
            "Markov-trace assembly chain for the proton on the CANONICAL "
            "11-letter element: convention-D Wedderburn weights + seminormal "
            "characters + the finite-Jones axiom, giving tr_M(p, q_0) ≈ "
            f"{float(PROTON_TR_M_Q0):.10f}. Written 2026-09-13 (bean qou-nhkv) to "
            "replace an ORPHAN artifact whose only builder was deprecated and "
            "which had been left in the grouped-era frame while its neutron "
            "and deuteron siblings moved to canonical. Unlike those siblings "
            "this chain has NO legacy-convention frontier: its character steps "
            "are computed on the canonical element rather than on a 5-letter "
            "stand-in. The leaf is read from canonical_trm_reference, not "
            "hardcoded."
        ),
        steps=steps,
    )


def main() -> int:
    chain = build()
    ok, issues = chain.structural_check()
    print(f"markov-trace-assembly-proton chain: structural_check "
          f"{'OK' if ok else 'FAIL'}")
    for i in issues:
        print(f"  - {i}")
    print(f"trust_summary: {chain.trust_summary()}")
    print(f"target_value:  {chain.target_value}")
    chain.save(OUTPUT)
    print(f"Wrote {OUTPUT}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
