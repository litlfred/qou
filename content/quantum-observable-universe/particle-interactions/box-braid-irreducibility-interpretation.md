**The box braid: crossing-by-crossing.**

The process $\gamma\gamma \to \nu\nu^{\sigma}$ has no tree-level realisation because photons ($K = \mathbf{1}_{B_4}$ 4-strand id; see [confined-particle](#def:confined-particle), [photon](#ex:photon-wavefront)) carry no braid strands, and neutrinos ($K_{0_1}$, [neutrino](#def:neutrino-knot)) have zero crossing chirality $Q(\nu) = 0$. The minimal topology is a box with four vertices and four internal propagators, all at brane tower level $A_1$ ([virtual particles](#rem:virtual-particles-exceptional-divisor)):

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

- **EM vertices** ($\gamma \leftrightarrow e^-e^+$): The photon's $\dagger$-involution couples to the trefoil's antisymmetric crossing energy ([force–knot identification](#rem:force-knot-identification), §I). This creates virtual $e^-e^+$ pairs at the exceptional divisor $\mathcal{S}_p$. Each pair is a trefoil + mirror trefoil ($T_{2,3} \sqcup T_{2,3}^{\sigma}$) at brane level $A_1$.
- **Weak vertices** ($e \to \nu$ via $T_{3,5}$): The Skein relation mediated by $T_{3,5}$ ([force–knot identification](#rem:force-knot-identification), §III) converts the charged trefoil to the neutral unknot.

**Corollary: neutrino stability.**

The neutrino ($K_{0_1}$, mass $m_\nu \sim \mu_0(q-1)$, [neutrino](#def:neutrino-knot)) is strictly stable. It cannot decay via any process.

1. **No beta decay.** The neutrino is an elementary knot (unknot) with no internal constituents, no crossing orientation partition, and no substructure to rearrange ([electron immortality](#rem:electron-immortality) applies *a fortiori*: the unknot is simpler than the trefoil).
2. **No scattering decay.** Any decay channel $\nu \to \gamma + \cdots$ or $\nu \to \nu' + \cdots$ must pass through the $T_{3,5}$ topology (or a higher-genus equivalent). The $T_{3,5}$ mediator is an element of length $10$ in the Artin generators. Each crossing operation incurs an energy penalty proportional to $(q - q^{-1})\mu_0$. The total topological obstruction barrier scales strictly with the invariant crossing number:

   $$
     E_{\mathrm{box}}  \geq 
     c(T_{3,5}) \cdot (q - q^{-1}) \cdot \mu_0
     = 
     10 \cdot (q - q^{-1}) \cdot \mu_0
     \gg
     m_\nu =  \mu_0(q - 1).
   $$

   Since $E_{\mathrm{box}}$ is structurally disjoint from the unknot mass scale $m_\nu = \mu_0(q - 1)$, the decay channel is strongly suppressed.
3. **No simpler process.** $T_{3,5}$ is the unique cross-family mediator on the Bring's surface. Its crossing number $10$ is a topological invariant. No isotopy or alternative mediator reduces the barrier.

The neutrino is therefore strictly stable in the Descartes universe. It has no decay channels at any energy below the $T_{3,5}$ crossing threshold. Unlike the electron, which is stable by topological invariance of the trefoil, the neutrino is stable by the energetic inaccessibility of its only interaction channel. The structural requirement of the full box machinery renders these interactions both topologically irreducible and energetically suppressed.
