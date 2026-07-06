**Conjecture (D18 3d–3d correspondence closure).**

*The Dimofte–Gaiotto–Gukov 3d–3d correspondence maps a hyperbolic 3-manifold $M^3$ to a 3d $\mathcal{N}{=}2$ gauge theory $T[M^3]$. The partition function $Z_{T[M^3]}(q)$ on a squashed 3-sphere $S^3_b$ equals the state-integral invariant of $M^3$ constructed from the quantum dilogarithm $\Phi_q$. Applied to the Borromean rings complement $\mathbf{S}^3 \setminus \mathcal{B}_3$, the 3d–3d theory $T[\mathbf{S}^3 \setminus \mathcal{B}_3]$ yields a partition function whose $h^4$ coefficient matches the framework's Markov-trace coefficient $h^4 = -3/4$.*

## Significance

The 3d–3d correspondence provides a gauge-theory realisation for every hyperbolic-3-manifold mass formula.

| Framework side | 3d gauge theory side |
|----------------|----------------------|
| $\mathcal{B}_3$ (Borromean rings complement) | $T[\mathcal{B}_3]$ — a 3d $\mathcal{N}{=}2$ theory |
| $m_p = m_e \cdot \mathrm{VolDensity}(\mathcal{B}_3, q_0)$ | partition function $Z_{T[\mathcal{B}_3]}(q_0)$ on $S^3_b$ |
| $h^4 = -3/4$ Markov-trace coefficient | 4-loop perturbative contribution to $Z_{T[\mathcal{B}_3]}$ |

This manifests mirror symmetry: the framework's mass formula corresponds to a quantum-field-theory partition function on a curved spacetime. Both compute the same hyperbolic invariant.

## Diagnostics

Per [`.claude/skills/local/canonical-watcher.md`](../../../.claude/skills/local/canonical-watcher.md) §Slot J:

- **GB filtration**: N/A (the duality operates at the partition-function / observable level, not at a specific Hecke-element level).
- **Jet order**: All-orders (the partition function possesses a full $q$-perturbative expansion; the $h^4$ coefficient corresponds to a specific perturbative order in the gauge theory).
- **Bar-symmetry**: Dependent on the gauge theory side. For $\mathcal{N}{=}2$ theories with a real-mass parameter, bar-symmetry corresponds to the parity-reversal of the squashed 3-sphere $S^3_b \to S^3_{1/b}$.

## Open R&D

1. Identify the 3d $\mathcal{N}{=}2$ theory $T[\mathcal{B}_3]$ explicitly via the Dimofte–Gaiotto–Gukov 2014 construction.
2. Cross-check the $h^4 = -3/4$ coefficient against the 4-loop contribution in the $T[\mathcal{B}_3]$ partition function.
3. Closing D18 remains a long-horizon task requiring significant QFT-side Lean infrastructure.

## Cross-references

- [`docs/duality-tracker.md`](../../docs/duality-tracker.md) D18 + §2 Cluster C (Pentagon validation)
- D16 [`conj:borromean-bloch-group-element`](borromean-bloch-group-element.md) — K-theoretic regulator parallel
- [`conj:kashaev-volume-conjecture`](kashaev-volume-conjecture.md) — Volume Conjecture as the leading-order 3d–3d statement
- [Dimofte–Gaiotto–Gukov 2014; Terashima–Yamazaki 2011]
