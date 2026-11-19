# Construction, verification, and coherence of the QOU $\mathrm{Frob}_p$ instance

This remark records the finite-place coherence checks, the open
status of the global map, the downstream consumers, and the cross-prime coherence of
[the QOU motivic Galois character conjecture](#conj:qou-motivic-galois-instance).

## Construction and verification

- **Compatibility verification.** Two finite-place coherence checks hold on every $(p, \text{atom})$ cell. First, Galois-norm integrality holds: the trace $N(\mathrm{Frob}_p) = \sum_{\sigma \in \mathrm{Gal}(\mathbb{Q}(\zeta_{2p})/\mathbb{Q})} \sigma(\mathrm{Frob}_p)$ yields a rational integer (residual $< 10^{-7}$). Second, Weil purity holds at small primes: at $p \in \{2, 3\}$, the orbit-spread $\max|\sigma(\mathrm{Frob}_p)| - \min|\sigma(\mathrm{Frob}_p)|$ remains below $10^{-10}$ for every atom, and the inferred weight $w = 2 \log_p |\mathrm{Frob}_p|$ takes integer or near-integer values. At larger primes, the spread grows. The QOU motive remains mixed in general, consistent with the brane tower forming a sum across cohomology degrees.

- **Status of the global Frobenius map.** [The motivic Galois character definition](#def:motivic-galois-character) requires a single map assigning a Frobenius element to every prime, and that global map remains open for the QOU aether. The non-triviality condition at almost all primes is kept separate from the character data itself so that constructing a character does not presuppose the perpetual obstruction.

## Downstream consumers

Were the global character in hand, statements that take [the motivic Galois character](#def:motivic-galois-character) as a hypothesis could consume it directly, and the [motivic perpetual obstruction](#thm:motivic-perpetual-obstruction) would become unconditional for the QOU aether. That is the intended payoff rather than a present fact: the character remains conjectural, so those statements still carry the hypothesis.

What *is* unconditional is a narrower result on a different route:
the prime-ideal-collapse invariant
$C = a_0(-1) + 2 a_1(-1)$ establishes the obstruction directly from the trace expansion, without going through a
global motivic Galois character at all.

## Coherence

Cross-prime coherence follows structurally from the Habiro theorem. Any two evaluations $f|_{u = \zeta_{2p}}$ and $f|_{u = \zeta_{2q}}$ extract from the same Habiro element and respect the natural Galois action on $\mathbb{Q}(\mu_\infty)$. The deeper $\ell$-adic archimedean Weil/Deligne behaviour lies outside this construction.
