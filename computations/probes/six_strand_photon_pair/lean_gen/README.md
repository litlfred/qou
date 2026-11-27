# Generator for `QOU/MassTheory/PhotonPairNoFactor.lean`

Exact sympy only (no floats). Run from the repo root, with `OUT` a scratch directory:

    python3 computations/probes/six_strand_photon_pair/lean_gen/step1_entries.py $OUT/entries2.json
    python3 computations/probes/six_strand_photon_pair/lean_gen/step2_expressions.py $OUT
    python3 computations/probes/six_strand_photon_pair/lean_gen/step3_emit_lean.py $OUT 1000 \
        folio/quantum-observable-universe/lean/QOU/MassTheory/PhotonPairNoFactor.lean

Step 1 picks, for each γγ word and photon placement, a matrix entry of the word (one-marked-strand
sector) outside the reach of the two photons. Step 2 recomputes that entry with the Lean
definitions of `sig`/`sigInv`, asserts it matches the probe's representation, and finds the
cofactor for `linear_combination`. Step 3 writes the Lean file.

Step 4 handles the 25 cells step 1 cannot block with one entry (needs the `singular` apt package):

    python3 computations/probes/six_strand_photon_pair/lean_gen/step4_sector_certificates.py \
        $OUT/entries2.json folio/quantum-observable-universe/lean/QOU/MassTheory/PhotonPairNoFactorSector.lean

19 of them have no solution on the one-marked-strand sector; the script emits a Lean proof for each
from an exact Nullstellensatz certificate. The other 6 are two-photon products; they are proved as
Hecke-algebra identities in `PhotonPairIdleFactor.lean` (hand-written, not generated).

Correction (2026-11-22). Steps 1-3 used 88 words; the probe's own two-photon search (`P2_*`) used
68 of them (3-vertex matches and 5-vertex matches with no idle strand). The earlier note that the
probe excludes the 25 leftover cells by Groebner was wrong: those cells were never in its search,
and 6 of them factorise.
