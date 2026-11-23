The proof splits into two short verifiable observations:

1. **Self-duality of $\mathbb{Z}/2$.** Every additive homomorphism
   $\varphi \colon \mathbb{Z}/2 \to \mathbb{Z}/2$ is determined by
   its value $\varphi(1) \in \mathbb{Z}/2$. There are exactly two
   such values, giving the trivial character and the identity (sign)
   character. The bijection
   $\mathrm{Hom}(\mathbb{Z}/2, \mathbb{Z}/2) \leftrightarrow \mathbb{Z}/2$,
   $\varphi \mapsto \varphi(1)$, is the canonical self-duality.
   Composing with the standard embedding $\mathbb{Z}/2 \hookrightarrow
   \mathbb{C}^\times$, $k \mapsto (-1)^k$, identifies
   $\widehat{\mathbb{Z}/2} \cong \mathbb{Z}/2$.

2. **Surjectivity of the sign homomorphism** $\mathrm{sgn} \colon
   S_n \to \mathbb{Z}/2$ for $n \geq 2$. The transposition
   $\mathrm{swap}(0, 1) \in S_n$ has sign $-1$, witnessing the
   non-trivial sign class. Combined with the identity (trivial
   class), this realises both elements of $\mathbb{Z}/2$, so the
   sign homomorphism is surjective. By the universal property of
   abelianisation and the fact that $S_n$ for $n \geq 2$ has
   abelianisation of order 2 (Coxeter group theory; equivalently,
   the commutator subgroup is the alternating group $A_n$),
   $S_n^{\mathrm{ab}} \cong \mathbb{Z}/2$.

Composing (1) and (2): $\widehat{S_n^{\mathrm{ab}}} \cong
\widehat{\mathbb{Z}/2} \cong \mathbb{Z}/2 \cong S_n^{\mathrm{ab}}$,
canonically. ∎
