# Sidecar re-triage: quantum-universes chapter (2026-11-21)

Umbrella issue #8766. 9 stale items. After the writes the census shows all 8 Lean-backed statements and all 9 proofs in this chapter fresh.

## Re-stamped (wording only, earlier verdict kept)

- quantum-universe-exists (pass)
- positive-definite-dagger proof (fail)
- frobenius-pairing-exists, statement and proof (warn)
- categorical-connection-exists (fail)
- categorical-connection-unique proof (fail)
- categorical-hodge-star-exists (fail)
- quantum-universe-exists proof (warn)

## Full review

**frobenius-pairing-unique proof: pass → fail, major.** The earlier pass had no evidence. The new proof text has three problems:

1. It uses the false identity Hom(A^∨, 1) ≅ Hom(1, A) ⊗ Hom(1, A^∨).
2. It uses A^∨, which does not exist in a non-rigid quantum universe.
3. It reads "simple" ambiguously. As a simple object with a simple unit, the form is an isomorphism, so A ≅ 1. As a simple algebra, the claim is false. Counterexample: on M₂(k), tr and tr(diag(1,2)·) are not scalar multiples.

The block's lean.ref points at the wrapper around the open axiom, not at the proved `frobeniusForm_unique_of_schur`.

## Ruling check

No block in this chapter uses the photon form, the electron strand or the two-term trace.
