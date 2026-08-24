# **QOU MotivicGaloisCharacter instance** via Habiro evaluation

**Conjecture.** The QOU brane-tower substrate carries a concrete instance of [`def:motivic-galois-character`](#def:motivic-galois-character) constructed by the Habiro evaluation map:

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

**Why this is stated as a conjecture (2026-08-23).** The formula above
specifies $\mathrm{Frob}_p$ in $\mathbb{Z}[\zeta_{2p}]$, one prime at a
time. What [`def:motivic-galois-character`](#def:motivic-galois-character)
asks for is a single $\mathrm{frobenius\_at} \colon \mathrm{Primes} \to
\widehat{M}$, so the content of the claim is that these per-prime
evaluations *cohere* into one $\widehat{M}$-valued function. The
follow-on remark argues that coherence structurally from the Habiro
theorem; it is neither proved nor formalised. Calling this a definition
asserted the construction was already in hand.

**Lean status (2026-08-23).** There is no Lean formalization of this
instance. The co-located `.lean` file — which contained a bare `axiom`
laundering the perpetual obstruction into the `MotivicGaloisCharacter`
class — was deleted on 2026-08-12 and has no replacement. The
`lean.ref` this block carried until today,
`QOU.LiftingDescent.QOUInstance.qouMotivicGaloisChar`, named a module
and a declaration that exist nowhere in the Lake tree.

What does exist is
`lean/QOU/LiftingDescent/MotivicPerpetualObstructionFromTrace.lean`
(Route A: prime-ideal-collapse, $C = a_0(-1) + 2 a_1(-1)$, sorry-free),
and it is a *different* result: it proves statements about the
obstruction, and constructs no `MotivicGaloisCharacter`. The 2026-08-12
note here read as though it were the replacement.
