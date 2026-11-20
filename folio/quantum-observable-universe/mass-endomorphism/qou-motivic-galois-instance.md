# **QOU MotivicGaloisCharacter instance** via Habiro evaluation

**Conjecture.** The QOU brane-tower substrate carries a concrete instance of [Motivic Galois character $\chi^{\mathrm{mot}}_A$ of the Frobenius--Hopf substrate](#def:motivic-galois-character) constructed by the Habiro evaluation map:

$$
  \mathrm{Frob}_p \;=\; f(u) \big|_{u = \zeta_{2p}}
  \;\in\; \mathbb{Z}[\zeta_{2p}].
$$

Here $f(u) = \sum_{m \geq 0} a_m(u) (u; u)_m$ represents the Habiro cyclotomic expansion of the atomic Markov trace $\mathrm{tr}_M(T_w, q)$ and $u = q^{1/2}$. The cyclotomic Pochhammer $(u; u)_m$ vanishes for $m \geq 2p$. This forces the sum to terminate after a finite number of terms.

The finite-place compatibility checks, the
downstream consumers, and cross-prime coherence are recorded in
[the follow-on remark](#rem:qou-motivic-galois-instance-verification);
the per-cell $\mathrm{Frob}_p$ data appears in
[the accompanying example](#ex:qou-motivic-galois-instance-per-cell).

**Why this is stated as a conjecture.** The formula above
specifies $\mathrm{Frob}_p$ in $\mathbb{Z}[\zeta_{2p}]$, one prime at a
time. What [Motivic Galois character $\chi^{\mathrm{mot}}_A$ of the Frobenius--Hopf substrate](#def:motivic-galois-character)
asks for is a single $\mathrm{frobenius\_at} \colon \mathrm{Primes} \to
\widehat{M}$, so the content of the claim is that these per-prime
evaluations *cohere* into one $\widehat{M}$-valued function. The
follow-on remark argues that coherence structurally from the Habiro
theorem; it is neither proved nor formalised. Calling this a definition
would assert the construction was already in hand.

**Lean status.** There is no Lean formalization of this instance. The
module `QOU.LiftingDescent.MotivicPerpetualObstructionFromTrace`
(prime-ideal collapse, $C = a_0(-1) + 2 a_1(-1)$) proves statements
about the perpetual obstruction and constructs no
`MotivicGaloisCharacter`; it is a different result.
