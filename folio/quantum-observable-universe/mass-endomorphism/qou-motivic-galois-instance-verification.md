# Construction, verification, and coherence of the QOU $\mathrm{Frob}_p$ instance

This remark records the finite-place coherence checks, the status of
the instance, the downstream consumers, and the cross-prime coherence of
the [QOU $\mathrm{MotivicGaloisCharacter}$ instance via Habiro $\to \mathrm{Frob}_p$](#conj:qou-motivic-galois-instance)
construction.

## Construction and verification

- **Compatibility verification.** We perform two finite-place coherence checks on every $(p, \text{atom})$ cell. First, Galois-norm integrality holds: the trace $N(\mathrm{Frob}_p) = \sum_{\sigma \in \mathrm{Gal}(\mathbb{Q}(\zeta_{2p})/\mathbb{Q})} \sigma(\mathrm{Frob}_p)$ yields a rational integer (residual $< 10^{-7}$). Second, Weil purity holds at small primes: at $p \in \{2, 3\}$, the orbit-spread $\max|\sigma(\mathrm{Frob}_p)| - \min|\sigma(\mathrm{Frob}_p)|$ remains below $10^{-10}$ for every atom, and the inferred weight $w = 2 \log_p |\mathrm{Frob}_p|$ takes integer or near-integer values. At larger primes, the spread grows. The QOU motive remains mixed in general, consistent with the brane tower forming a sum across cohomology degrees.

- **Status: there is no instance.** The motivic Galois character consists of a single datum, the Frobenius assignment $\mathrm{frobenius\_at}$, and nothing supplies it for the QOU substrate, so [Motivic Galois character $\chi^{\mathrm{mot}}_A$ of the Frobenius--Hopf substrate](#def:motivic-galois-character) is not discharged here.

## Downstream consumers

Were the instance in hand, theorems that carry [Motivic Galois character $\chi^{\mathrm{mot}}_A$ of the Frobenius--Hopf substrate](#def:motivic-galois-character) as a hypothesis could consume it directly, and the [motivic perpetual obstruction](#thm:motivic-perpetual-obstruction) would become unconditional for the QOU substrate. That is the intended payoff, not a present fact: the instance is conjectural, so those theorems still carry the hypothesis.

What *is* unconditional is a narrower result on a different route:
the obstruction is derived directly from the prime-ideal-collapse
invariant $C = a_0(-1) + 2 a_1(-1)$, without going through a motivic
Galois character at all.

## Coherence

Cross-prime coherence follows structurally from the Habiro theorem. Any two evaluations $f|_{u = \zeta_{2p}}$ and $f|_{u = \zeta_{2q}}$ extract from the same Habiro element and respect the natural Galois action on $\mathbb{Q}(\mu_\infty)$. The deeper $\ell$-adic archimedean Weil/Deligne behaviour lies outside this construction.
