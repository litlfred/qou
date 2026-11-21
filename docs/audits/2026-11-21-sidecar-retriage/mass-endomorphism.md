# Sidecar re-triage: mass-endomorphism (2026-11-21)

Umbrella issue #8766. Criteria: `proof-narrative-lean-equiv` (statement vs Lean) and `da-non-sequitur` (proof vs statement). 28 entries: 27 stale, 1 never reviewed.

## Re-stamped (wording-only diffs; earlier verdict kept)

17 blocks. The diffs change voice ("we" to "one"), replace label references with titles, and replace Lean names with prose. No step of the mathematics or the Lean changed:
mass-identity-C, mass-identity-unique, mass-identity-exists, categorical-mass-markov (+ proof), hecke-branching-trace-decomposition (+ proof), markov-trace-antipode-polynomial-symmetry (+ proof), markov-trace-axiomatic-closed-form (+ proof), hecke-baer-star-generic-proof, qbeta-delta-tau-canonical-conditional-q2-minus-1-factor (+ proof), tau-M-asymptotic-rep-theory-proof, qbeta-per-block-chi-closed-forms-proof, qbeta-canonical-markov-weights-explicit-instance-proof.

## Full reviews (maths or Lean changed)

| block | criterion | was | now | finding |
|---|---|---|---|---|
| topological-mass-eigenspace-decomp | stmt | warn | **warn** | Now a correct bound, with the multiplicative-integral split as a hypothesis, and it matches the sibling Lean `tm_eigenspace_decomp_norm_le`. The closing remark applies vector-sum facts (strict triangle inequality, common ray) to a group product. |
| topological-mass-eigenspace-decomp-proof | proof | fail | **warn** | The final step is now valid. The proof still presents the multiplicative-integral factorisation as derived, though the statement assumes it. It also still calls the involution an "idempotent". |
| topological-mass-proof | proof | fail | **warn** | Proves the archimedean upper bound correctly, given the lemmas. It does not state the factorisation hypothesis, drops the norm on Φ_q in its last line, and its title still says "decomposition". |
| topological-mass-categorical-proof | proof | fail | **warn** | Valid bound by linearity and the triangle inequality. The title still names the conjectured equality. |
| topological-mass-upper-bound | stmt | — | **warn** (first) | The Lean proves the norm step from an assumed split; the scope is disclosed. |
| topological-mass-conjecture | stmt | fail | **fail** | The md now says the decomposition is conjectural. The Lean is still a self-assuming class, and its docstring still calls thm:topological-mass "proved". Kind is still `proposition`. |
| atomic-mass-gb-nf | stmt | fail | **fail** | **Regression.** The honest "fixes nothing, ρ_K is free" note was replaced by "acquires predictive content via prop:rho-k-graded-expansion". That block is circular: it is derived from this identity, its next piece is fitted against the mass table, and its pair piece is open. |
| quantum-dilogarithm | stmt | fail | **fail** | The claim is now explicit in the md. The ref is still a class field, and the Faddeev-vs-series Φ_q collision remains. |
| hecke-baer-star-generic | stmt | fail | **fail** | New sorry-free `baerStarRing_matrix_rclike` (M_n over RCLike with conjugate transpose). But the ref still points at the M_2(F_2) refutation. The bar involution moves q, so it is not an involution of H_n(q) over R, and it is not positive. |
| markov-trace-recursive-reducer | stmt | fail | **fail** | The sibling Lean is honestly repaired (Hecke relations, ascending-run product law, the general law left open). But the ref still resolves to the self-assuming library class. The md keeps the old z-factor argument above the note that refutes it. A docstring cites a `markovTrace_disjointProduct` that does not exist. |
| categorical-chain-convergence-mechanisms | stmt | fail | **fail** | Conditional banner added, but the conjecture is not in uses[] and has no Lean class hypothesis (§3b-cond). The Mechanism 2 `z^k` contradiction is unchanged. |

## Ruling check (docs/coordination/owner-rulings.md)

No block in this batch states a photon, electron or Lagrangian-trace form, so none conflicts with the rulings. The no-fitting ruling bears on atomic-mass-gb-nf. Its new scope note leans on a fitted prefactor (α chosen against the mass table) for "predictive content".

Census after this batch: `proof-narrative-lean-equiv` 19 fresh / 0 stale; `da-non-sequitur` 23 fresh / 0 stale.
