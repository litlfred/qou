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
