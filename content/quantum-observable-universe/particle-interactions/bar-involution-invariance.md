**Proposition (conditional).**
Let $\bar\cdot$ be the bar-involution sending $q \mapsto q^{-1}$. Then:

1. (**Plancherel-weight invariance**) The Plancherel weight satisfies $\overline{w_\lambda(q)} = w_\lambda(q)$.
2. (**Transpose-pair equality**) $w_\lambda(q) = w_{\lambda^T}(q)$.
3. (**Type-B-folded normal forms**) Any Hecke normal form produced by the pair-production engine is bar-invariant: $\overline{T_w} = T_w$.

## Significance: a witness against hand-rolled CPT violations

These conditions are necessary consequences of Type-B folding. Any normal form, mass formula, or LP cost vector must satisfy them. Failure signals a chirality bias incompatible with the symmetric-crystal substrate. This block packages the invariance lemmas as a regression-test witness.

## Proofs

**(1) Plancherel-weight invariance.** The $q$-integer $[k]_q$ is bar-invariant. The entire Plancherel weight is a quotient of bar-invariants, hence bar-invariant. $\square$

**(2) Transpose-pair equality.** Hook lengths are unchanged by transpose. This yields identical $w_\lambda$. $\square$

**(3) Type-B-folded normal forms.** The folded operator pair produces two descendants whose normal forms are bar-conjugates. Their sum is bar-invariant.

## Worked example: $n = 3$

Transpose pairing yields identical hook products, matching part 2. Bar-invariance follows from $[k]_{q^{-1}} = [k]_q$ on every factor.

## Lean formalisation

The Lean formalisation defines the bar-involution, $q$-integer, and Plancherel weight, and proves the relevant invariance lemmas.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall.
