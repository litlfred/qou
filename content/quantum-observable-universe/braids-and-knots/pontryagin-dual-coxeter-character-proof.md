## Proof

We rely on two structural observations:

1. **Self-duality of $\mathbb{Z}/2$.** Every additive homomorphism $\varphi \colon \mathbb{Z}/2 \to \mathbb{Z}/2$ is uniquely determined by $\varphi(1) \in \mathbb{Z}/2$. The two possible values yield the trivial character and the sign character. The bijection $\mathrm{Hom}(\mathbb{Z}/2, \mathbb{Z}/2) \leftrightarrow \mathbb{Z}/2$ given by $\varphi \mapsto \varphi(1)$ establishes canonical self-duality. Embedding $\mathbb{Z}/2 \hookrightarrow \mathbb{C}^\times$ via $k \mapsto (-1)^k$ identifies $\widehat{\mathbb{Z}/2} \cong \mathbb{Z}/2$.

2. **Surjectivity of the sign homomorphism.** For $n \geq 2$, the transposition $\mathrm{swap}(0, 1) \in S_n$ has sign $-1$, witnessing the non-trivial class of $\mathrm{sgn} \colon S_n \to \mathbb{Z}/2$. Consequently, the sign homomorphism is surjective. By Coxeter group theory, the commutator subgroup of $S_n$ is the alternating group $A_n$, so the abelianisation $S_n^{\mathrm{ab}}$ has order 2. Therefore, $S_n^{\mathrm{ab}} \cong \mathbb{Z}/2$.

Composing (1) and (2) yields the canonical isomorphism $\widehat{S_n^{\mathrm{ab}}} \cong \widehat{\mathbb{Z}/2} \cong \mathbb{Z}/2 \cong S_n^{\mathrm{ab}}$. ∎

## Formalisation

The Lean module [`pontryagin_dual_coxeter_character_structural`](pontryagin-dual-coxeter-character.lean) formalises this proof as a sorry-free theorem, conjoining:

- `zmodTwo_pontryagin_self_dual_via_value_at_one` — proves via `fin_cases` that characters $\mathbb{Z}/2 \to \mathbb{Z}/2$ are determined by their value at 1.
- `signHom_surjective_witness` — confirms `Equiv.swap 0 1 ∈ Equiv.Perm (Fin n)` has sign $-1$ for `n ≥ 2`.

For backward compatibility, a `class PontryaginDualCoxeterCharacter` is retained with a default instance backed by the structural theorem. Downstream blocks using it as a §3b-cond hypothesis continue to compile. New downstream code should cite `pontryagin_dual_coxeter_character_structural` directly.
