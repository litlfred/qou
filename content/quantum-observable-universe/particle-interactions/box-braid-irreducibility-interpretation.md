**The box braid: crossing-by-crossing.**

The process $\gamma\gamma \to \nu\nu^{\sigma}$ has no tree-level
realisation because photons ($K = \mathbf{1}_{B_4}$ 4-strand id;
see [confined-particle](#def:confined-particle),
[photon](#ex:photon-wavefront)) carry no braid strands and
neutrinos ($K_{0_1}$, [neutrino](#def:neutrino-knot)) have zero
crossing chirality $Q(\nu) = 0$.  The minimal topology is a box
with four vertices and four internal propagators, all at brane
tower level $A_1$
([virtual particles](#rem:virtual-particles-exceptional-divisor)):

```tex
\[
\begin{tikzcd}[row sep=3em, column sep=4em]
  \gamma_1 \ar[r, "\text{EM}" {above}, "\dagger\text{-coupling}" {below}]
  & e^-_{\mathrm{virt}} \ar[d, "\text{Skein}_{T_{3,5}}" {right}]
  \\
  \gamma_2 \ar[u, "\text{EM}" {left}, "\dagger\text{-coupling}" {right}]
  & \nu\nu^{\sigma} \ar[l, phantom, "\text{output}" {below}]
\end{tikzcd}
\]
```

**Vertex structure.**

At each vertex, a specific braid operation occurs:

- **EM vertices** ($\gamma \leftrightarrow e^-e^+$): the
  photon's $\dagger$-involution couples to the trefoil's
  antisymmetric crossing energy
  ([force–knot identification](#rem:force-knot-identification),
  §I), creating virtual $e^-e^+$ pairs at the exceptional
  divisor $\mathcal{S}_p$.  Each pair is a trefoil + mirror trefoil
  ($T_{2,3} \sqcup T_{2,3}^{\sigma}$) at brane level $A_1$.

- **Weak vertices** ($e \to \nu$ via $T_{3,5}$): the Skein
  relation mediated by $T_{3,5}$
  ([force–knot identification](#rem:force-knot-identification),
  §III) converts the charged trefoil to the neutral unknot.

**Corollary: neutrino stability.**

The neutrino ($K_{0_1}$, mass $m_\nu \sim \mu_0(q-1)$,
[neutrino](#def:neutrino-knot)) is **stable** — it cannot decay
via any process.

1. **No beta decay.** The neutrino is an elementary knot (unknot)
   with no internal constituents, no crossing orientation partition,
   and no substructure to rearrange
   ([electron immortality](#rem:electron-immortality) applies
   *a fortiori*: the unknot is even simpler than the trefoil).

2. **No scattering decay.** Any decay channel
   $\nu \to \gamma + \cdots$ or $\nu \to \nu' + \cdots$ must
   pass through the $T_{3,5}$ topology (or something at least as
   complex).  The $T_{3,5}$ mediator requires $10$ $R$-matrix
   applications — $10$ Planck steps of braid computation.  Each
   application costs crossing energy $(q - q^{-1}) \cdot \mu_0$.
   The total energy barrier:

   $$
     E_{\mathrm{box}}  \geq 
     c(T_{3,5}) \cdot (q - q^{-1}) \cdot \mu_0
     = 
     10 \cdot (q - q^{-1}) \cdot \mu_0
     \gg
     m_\nu =  \mu_0(q - 1).
   $$

   The ratio $E_{\mathrm{box}} / m_\nu \geq 10 \cdot (q + 1) / q \approx 19$ at the substrate parameter $q$: the box
   energy barrier is $\sim 19$ times the neutrino mass.

3. **No simpler process.** $T_{3,5}$ is the unique cross-family
   mediator on the Bring's surface, and its crossing number $10$
   is a topological invariant.  No isotopy or alternative mediator
   reduces the barrier.

The neutrino is therefore the **most stable** particle in the
Descartes universe: it has no decay channels at any energy below
the $T_{3,5}$ crossing threshold.  Unlike the electron (which is
stable by topological invariance of the trefoil — it *could*
interact but cannot *decay*), the neutrino is stable by
**energetic inaccessibility of its only interaction channel**.
This is why neutrinos pass through matter virtually unimpeded:
every interaction requires the full box machinery, which is both
topologically irreducible and energetically suppressed.
