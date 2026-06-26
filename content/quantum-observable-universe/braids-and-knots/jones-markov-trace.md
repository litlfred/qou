**(Jones, 1987, Theorem 5.1 and Corollary 5.3.)**
Let $q \in \mathbb{C}^{\times}$ be not a root of unity, and let
$H_n(R, q) = \mathrm{End}_{B_n}(V^{\otimes n})$ be the Iwahori--Hecke algebra of
type $A_{n-1}$.  Then:

1. **(Existence.)** There exists a unique $\mathbb{C}$-linear functional
   $\mathrm{tr}_M \colon \bigcup_{n \geq 1} H_n(R, q) \to \mathbb{C}$
   satisfying:
   - **(Normalisation)**: $\mathrm{tr}_M(1) = 1$.
   - **(Trace property)**: $\mathrm{tr}_M(ab) = \mathrm{tr}_M(ba)$
     for all $a, b \in H_n(R, q)$.
   - **(Markov property)**: $\mathrm{tr}_M(x \sigma_n^{\pm 1}) = z^{\pm 1}\mathrm{tr}_M(x)$ for all $x \in H_n(R, q)$, viewed in
     $H_{n+1}(q)$ under the standard embedding $H_n(R, q) \hookrightarrow H_{n+1}(q)$, where
     $z = (q - 1)/(q^{1/2} + q^{-1/2})^2$ (determined by $q$).

2. **(Non-degeneracy on irreducibles.)** For each partition
   $\lambda \vdash n$ with at most $r$ parts (where $r = \mathrm{rank}$
   of the quantum group), the restriction of $\mathrm{tr}_M$ to the
   irreducible $H_n(R, q)$-module $S_\lambda$ is a non-zero scalar multiple
   of the character $\chi_\lambda$.  In particular,
   $\mathrm{tr}_M|_{S_\lambda} \neq 0$ for every $\lambda$.

3. **(Link invariance.)** For any braid $\beta \in B_n$, the value
   $\mathrm{tr}_M(\rho_n(\beta))$ depends only on the isotopy class of
   the closure $\hat{\beta}$, and equals the Jones polynomial $J_L(q)$
   of the link $L = \hat{\beta}$ up to a framing factor
   $\alpha^{w(\beta)}$ where $w(\beta)$ is the writhe.

This is the key external result on which knot eigenbasis completeness
([knot eigenbasis completeness](#prop:knot-eigenbasis-complete)) depends.
The proof occupies §3--5 of Jones (1987); we take the result as axiomatic
and encode it as a Lean structure whose fields are the three properties above.
The formal goal is to verify that downstream theorems — the unity of the Markov trace and the detection of all irreducible representations — follow from these axiomatized structure fields. The trace's required properties are isolated as axiomatic structure fields, separating the external existence proof from the internal verification of its consequences in the observable mass spectrum.