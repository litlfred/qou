# Construction, verification, and coherence of the QOU $\mathrm{Frob}_p$ instance

This remark records the finite-place coherence checks, the Lean
status, the downstream consumers, and the cross-prime coherence of
the [QOU $\mathrm{MotivicGaloisCharacter}$ instance via Habiro $\to \mathrm{Frob}_p$](#conj:qou-motivic-galois-instance)
construction.

## Construction and verification

- **Compatibility verification.** We perform two finite-place coherence checks on every $(p, \text{atom})$ cell. First, Galois-norm integrality holds: the trace $N(\mathrm{Frob}_p) = \sum_{\sigma \in \mathrm{Gal}(\mathbb{Q}(\zeta_{2p})/\mathbb{Q})} \sigma(\mathrm{Frob}_p)$ yields a rational integer (residual $< 10^{-7}$). Second, Weil purity holds at small primes: at $p \in \{2, 3\}$, the orbit-spread $\max|\sigma(\mathrm{Frob}_p)| - \min|\sigma(\mathrm{Frob}_p)|$ remains below $10^{-10}$ for every atom, and the inferred weight $w = 2 \log_p |\mathrm{Frob}_p|$ takes integer or near-integer values. At larger primes, the spread grows. The QOU motive remains mixed in general, consistent with the brane tower forming a sum across cohomology degrees.

- **Lean status: there is no instance.** `MotivicGaloisCharacter` carries a single field, `frobenius_at`, and nothing in the Lake tree supplies it for the QOU substrate, so [Motivic Galois character $\chi^{\mathrm{mot}}_A$ of the Frobenius--Hopf substrate](#def:motivic-galois-character) is not discharged here. The class once also carried `almost_everywhere_nontrivial`; that field was removed precisely because encoding it as a class field forced every instance either to prove it or to launder the perpetual obstruction through a bare `axiom`.

## Downstream consumers

Were the instance in hand, theorems that carry [Motivic Galois character $\chi^{\mathrm{mot}}_A$ of the Frobenius--Hopf substrate](#def:motivic-galois-character) as an `[instance]` hypothesis could consume it directly, and the [motivic perpetual obstruction](#thm:motivic-perpetual-obstruction) would become unconditional for the QOU substrate. That is the intended payoff, not a present fact: the instance is conjectural, so those theorems still carry the hypothesis.

What *is* unconditional is a narrower result on a different route:
the Lean module `QOU.LiftingDescent.MotivicPerpetualObstructionFromTrace`
derives the obstruction from the prime-ideal-collapse invariant
$C = a_0(-1) + 2 a_1(-1)$, without going through a
`MotivicGaloisCharacter` instance at all.

## Coherence

Cross-prime coherence follows structurally from the Habiro theorem. Any two evaluations $f|_{u = \zeta_{2p}}$ and $f|_{u = \zeta_{2q}}$ extract from the same Habiro element and respect the natural Galois action on $\mathbb{Q}(\mu_\infty)$. The deeper $\ell$-adic archimedean Weil/Deligne behaviour lies outside this construction.
