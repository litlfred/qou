## Statement

**Proposition (antipode-induced polynomial symmetry).**
*Let $\mathcal{B}_p$ denote the proton braid in $B_3$ used in*
*[`prop:atomic-mass-gb-nf`](#prop:atomic-mass-gb-nf), and let*

$$
  p(q) \;=\; q^{20} + q^{18} + 2 q^{12} - 2 q^{8} - q^{2} - 1
$$

*be the numerator of the closed-form Markov trace*

$$
  \operatorname{tr}_M(\mathcal{B}_p) \;=\; \frac{p(q)}{12 \cdot q^{10}}
$$

*derived in via*
*the symbolic Hoefsmit-Wenzl seminormal reduction. Then $p(q)$ is*
*anti-self-reciprocal of degree $20$:*

$$
  \boxed{\quad q^{20} \cdot p(1/q) \;=\; -p(q). \quad}
$$

*Equivalently, the Markov trace itself satisfies*

$$
  \operatorname{tr}_M(\mathcal{B}_p)\!\bigl(\tfrac{1}{q}\bigr) \;=\; -\operatorname{tr}_M(\mathcal{B}_p)(q).
$$

## Categorical interpretation

The Iwahori-Hecke algebra $H_n(q)$ is a Hopf algebra with antipode
$S(\sigma_i) = \sigma_i^{-1}$. The Hecke quadratic relation
$\sigma_i^2 = (q - q^{-1}) \sigma_i + 1$ implies
$\sigma_i^{-1} = \sigma_i - (q - q^{-1})$, so the antipode acts
linearly on the generators with a $q \leftrightarrow q^{-1}$
component.

The Markov trace $\operatorname{tr}_M$ is the Frobenius integral
on $H_n(q)$ ([`prop:categorical-mass-markov`](#prop:categorical-mass-markov)).
For Frobenius algebras with non-trivial Nakayama automorphism, the
trace satisfies $\operatorname{tr}(S^2(x)) = \operatorname{tr}(x)$.
For the Hecke algebra, $S^2$ acts as $q \leftrightarrow q^{-1}$ on
the structural variable $q$ while preserving the algebra structure.

The minus sign in $\operatorname{tr}_M(\mathcal{B}_p)(1/q) = -\operatorname{tr}_M(\mathcal{B}_p)(q)$
reflects the **odd parity** of the proton word $\mathcal{B}_p$ under the
antipode-induced involution: $S(\mathcal{B}_p)$ is the reversed word with
each $\sigma$ replaced by $\sigma^{-1}$, and the $11$-crossing
(odd) length contributes a parity sign. Specifically, the
proton's word length $\ell(\mathcal{B}_p) = 11$ has odd parity.

## Generalization conjecture

For any closed braid $K \in B_n$ whose Markov trace admits a
closed form
$\operatorname{tr}_M(K) = p_K(q) / (c_K \cdot q^{\mathrm{shift}(K)})$
with $\operatorname{deg}_q p_K = 2 \cdot \mathrm{shift}(K)$, the
polynomial satisfies

$$
  q^{2 \mathrm{shift}(K)} \cdot p_K(1/q) \;=\; (-1)^{\ell(\mathcal{B}_K)} \cdot p_K(q),
$$

where $\ell(\mathcal{B}_K)$ is the word length (or, more precisely, the
parity of crossings under the Hecke-algebra antipode action). The
$\mathrm{shift}(K)$ is the GS-filtration shift exponent
([`docs/audits/-w3-habiro-unblocked.md`](../../docs/audits/-w3-habiro-unblocked.md)),
which equals $18Z + 21N + 1$ for atomic braids per the integer-LP
closure.

This conjecture is testable via 's
$A \geq 2$ extension and via the polynomial structure of the
neutron's closed form
$\operatorname{tr}_M(\mathcal{B}_n) = (\dots) / (12 q^8 \cdot (q^4 + q^2 + 1))$.

## Witness

- `computations/poly_q_proof_probe.py` — sympy-exact verification.
- `computations/poly-q-proof.witness.json` — proof certificate.

## References

- [Wenzl 1988] *Hecke algebras of type $A_n$ and subfactors*, Inventiones Math. **92**, 349–383.
- [Hoefsmit 1974] *Representations of Hecke algebras of finite groups with $BN$-pairs of classical type*, PhD thesis, UBC.
- [Kassel 1995] *Quantum Groups*, Springer GTM 155, Ch. III (Hopf antipode + Frobenius integrals).
- — symbolic closed form for $\operatorname{tr}_M(\mathrm{proton})$.
