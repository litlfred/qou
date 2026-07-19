
Per [`.claude/skills/local/canonical-watcher.md`](../../../.claude/skills/local/canonical-watcher.md) §Slot J:

- **GB filtration level**: N/A — the $S$-transform is at the
  parameter level, not the Hecke-element level.
- **Jet order**: all-orders (the modular action acts on the entire
  $q$-expansion of every quantity).
- **Bar-symmetry status**: distinct from bar. $S$-transform composed
  with bar gives a $\mathbb{Z}/2 \times \mathbb{Z}/2$ structure on
  the modular q-parameter space.

## Open R&D

1. **Analytic continuation framework**: verify every framework
   quantity (Hecke generators, Frobenius pairing, Markov trace,
   Wedderburn weights $y_\lambda$) has well-defined modular
   continuation to complex $\tau$.
2. **Numerical check**: at the bar image $q_0^{-1}$ (the convergent
   branch), compute the $S$-transform $\tilde q_0$ and verify the Volume
   Conjecture asymptotic on $\tilde q_0$ matches the framework's bare-volume
   evaluation.
3. **Do not conflate with the named elliptic curves.** The modular
   $\tau$ here is **not** the period $\tau$ of the Descartes/color curve
   $\mathcal{E}_q$ ([`prop:descartes-elliptic-curve`](../predicted-spectra/elliptic-stability-locus.md)):
   the modular nome is $q_0^{-1} \approx 0.90$ (near the cusp) while
   $\mathcal{E}_q$'s period nome is $\approx 0.0029$ (deep in the
   fundamental domain) — a $\sim\!312\times$ mismatch. See
   [`docs/audits/2026-06-17-d14-theta-bar-side-and-nome-conflation.md`](../../../docs/audits/2026-06-17-d14-theta-bar-side-and-nome-conflation.md).
4. **Connect to D16 Bloch-group**: the modular $S$-transform on the
   $K_3(\mathbb{C})$ regulator gives a natural framework-side
   handle on the analytic structure of the Bloch-Wigner
   dilogarithm.
5. **D14 to closed** requires a numerical witness verifying the
   volume-conjecture asymptotic on $\tilde q_0$.

## Cross-references

- [`docs/duality-tracker.md`](../../docs/duality-tracker.md) D14
  + §2 Cluster D (limit dualities) + adjacent to D2 Hermitian *
- D2 sibling: PR [#1127](https://github.com/litlfred/qou/pull/1127)
  blocks `prop:q-zero-complex-extension` +
  `prop:lusztig-vs-hermitian-bar`
- Volume Conjecture: [`conj:kashaev-volume-conjecture`](#conj:kashaev-volume-conjecture)
- D16 Bloch group: [`conj:borromean-bloch-group-element`](borromean-bloch-group-element.md)
- 13-driver menu driver (viii): [`docs/audits/-lambda-scale-canonical-unification.md`](../../docs/audits/-lambda-scale-canonical-unification.md)

**Archimedean specialisation (§7c).** Modular convergence is an archimedean statement: the estimates use $\mathrm{Im}\,\tau$ and $\exp$ over $\mathbb{R}$, so it sits on the archimedean side of the substrate wall.
