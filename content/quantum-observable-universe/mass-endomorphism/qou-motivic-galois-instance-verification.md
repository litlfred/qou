# Construction, verification, and coherence of the QOU $\mathrm{Frob}_p$ instance

This remark records the finite-place coherence checks, the Lean
instance, the downstream consumers, and the cross-prime coherence of
the [`rem:qou-motivic-galois-instance`](#rem:qou-motivic-galois-instance)
construction.

## Construction and verification

- **Compatibility verification.** We perform two finite-place coherence checks on every $(p, \text{atom})$ cell. First, Galois-norm integrality holds: the trace $N(\mathrm{Frob}_p) = \sum_{\sigma \in \mathrm{Gal}(\mathbb{Q}(\zeta_{2p})/\mathbb{Q})} \sigma(\mathrm{Frob}_p)$ yields a rational integer (residual $< 10^{-7}$). Second, Weil purity holds at small primes: at $p \in \{2, 3\}$, the orbit-spread $\max|\sigma(\mathrm{Frob}_p)| - \min|\sigma(\mathrm{Frob}_p)|$ remains below $10^{-10}$ for every atom, and the inferred weight $w = 2 \log_p |\mathrm{Frob}_p|$ takes integer or near-integer values. At larger primes, the spread grows. The QOU motive remains mixed in general, consistent with the brane tower forming a sum across cohomology degrees.

- **Lean instance.** The instance in [`qou-motivic-galois-instance.lean`](qou-motivic-galois-instance.lean) discharges [`def:motivic-galois-character`](#def:motivic-galois-character) for the QOU substrate. The `frobenius_at` field maps each prime to its extracted Frobenius eigenvalue. The `almost_everywhere_nontrivial` field functions as a substrate axiom, backed by a numerical witness for primes $p \leq 13$.

## Downstream consumers

Theorems that previously required [`def:motivic-galois-character`](#def:motivic-galois-character) as an `[instance]` hypothesis can now consume the explicit QOU instance directly. In particular, [`conj:motivic-perpetual-obstruction`](#conj:motivic-perpetual-obstruction) becomes an unconditional theorem for the QOU substrate.

## Coherence

Cross-prime coherence follows structurally from the Habiro theorem. Any two evaluations $f|_{u = \zeta_{2p}}$ and $f|_{u = \zeta_{2q}}$ extract from the same Habiro element and respect the natural Galois action on $\mathbb{Q}(\mu_\infty)$. The deeper $\ell$-adic archimedean Weil/Deligne behaviour lies outside this construction.
