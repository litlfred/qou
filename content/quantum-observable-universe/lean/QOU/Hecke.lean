import QOU.Hecke.Generators
import QOU.Hecke.Algebra
import QOU.Hecke.MarkovTrace
import QOU.Hecke.MarkovTraceProduct
import QOU.Hecke.MarkovPairZ2
import QOU.Hecke.Wedderburn
import QOU.Hecke.Hoefsmit
import QOU.Hecke.PauliChannelBinding

/-!
# Hecke algebra infrastructure — module index

Axiomatic / structural Lean formalization of the Iwahori–Hecke
algebra `H_n(q)` over a base ring `R` with parameter `q ∈ R`.
Provides:

- `HeckeGenerator i` — formal generator σ_i (1 ≤ i ≤ n-1).
- `HeckeAlgebra n q` — the algebra modulo Hecke + braid relations.
- `MarkovTrace` — class for tr_M : HeckeAlgebra → R with Markov
  axiom and normalisation.
- `WedderburnDecomp` — Wedderburn-Artin decomposition by partitions
  λ ⊢ n into matrix algebras.
- `HoefsmitRepresentation` — explicit seminormal-form matrix
  representation `ρ_λ : H_n(q) → Mat_{f^λ}(R)` per partition `λ`,
  word-sensitive (distinguishes braids whose permutation cycle
  types coincide).

Status: structural framework laid out as classes (per AGENTS.md §3b
axiom-class pattern). Substantive proofs are left as `sorry` with
`Ref` citations to the relevant references / .md content; downstream
QOU theorems can take these as `[instance]` hypotheses.

## References

- [thm:jones-markov-trace] — Markov trace existence/uniqueness.
- [prop:braiding-eigenvalue-extraction] — q from R-matrix.
- [thm:wedderburn-mass-formula] — Wedderburn decomposition.
- Kassel (1995), Quantum Groups, Chapter XII.
- Mathas (1999), Iwahori–Hecke Algebras and Schur Algebras.
-/
