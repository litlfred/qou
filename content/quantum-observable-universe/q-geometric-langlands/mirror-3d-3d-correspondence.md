**Conjecture (D18 3d–3d correspondence closure, research-grade,
long horizon).**
*The Dimofte–Gaiotto–Gukov 3d–3d correspondence maps a hyperbolic
3-manifold $M^3$ to a 3d $\mathcal{N}{=}2$ gauge theory $T[M^3]$
such that the partition function $Z_{T[M^3]}(q)$ on a squashed
3-sphere $S^3_b$ equals the state-integral invariant of $M^3$
constructed from the quantum dilogarithm $\Phi_q$.  Applied to the
Borromean rings complement $\mathbf{S}^3 \setminus \mathcal{B}_3$,
the 3d–3d theory $T[\mathbf{S}^3 \setminus \mathcal{B}_3]$ has a
partition function whose $h^4$ coefficient is the QOU framework's
$h^4 = -3/4$.*

## Why this matters

The 3d–3d correspondence gives the framework a **gauge-theory
realisation** of every hyperbolic-3-manifold mass formula:

| Framework side | 3d gauge theory side |
|----------------|----------------------|
| $\mathcal{B}_3$ (Borromean rings complement) | $T[\mathcal{B}_3]$ — a 3d $\mathcal{N}{=}2$ theory |
| $m_p = m_e \cdot \mathrm{VolDensity}(\mathcal{B}_3, q_0)$ | partition function $Z_{T[\mathcal{B}_3]}(q_0)$ on $S^3_b$ |
| $h^4 = -3/4$ Markov-trace coefficient | 4-loop perturbative contribution to $Z_{T[\mathcal{B}_3]}$ |

This is **mirror symmetry** in the sense that the framework's mass
formula corresponds to a quantum-field-theory partition function on
a curved spacetime; both sides compute the same hyperbolic invariant.

## Diagnostics

Per [`.claude/skills/local/canonical-watcher.md`](../../../.claude/skills/local/canonical-watcher.md) §Slot J:

- **GB filtration**: N/A (the duality is at the partition-function
  / observable level, not at a specific Hecke-element level).
- **Jet order**: all-orders (partition function has full $q$ /
  perturbative expansion; the $h^4$ coefficient corresponds to a
  specific perturbative order in the gauge theory).
- **Bar-symmetry**: depends on the gauge theory side; for
  $\mathcal{N}{=}2$ theories with a real-mass parameter, the
  bar-symmetry corresponds to the parity-reversal of the squashed
  3-sphere $S^3_b \to S^3_{1/b}$.

## Open R&D

1. Identify the 3d $\mathcal{N}{=}2$ theory $T[\mathcal{B}_3]$
   explicitly (Dimofte–Gaiotto–Gukov 2014 provides the construction).
2. Cross-check the $h^4 = -3/4$ coefficient as a 4-loop contribution
   in $T[\mathcal{B}_3]$ partition function.
3. D18 to closed is a very long horizon — requires significant
   QFT-side Lean infrastructure (none exists in Mathlib).

## Cross-references

- [`docs/duality-tracker.md`](../../docs/duality-tracker.md) D18
  + §2 Cluster C (Pentagon validation)
- D16 [`conj:borromean-bloch-group-element`](borromean-bloch-group-element.md)
  — K-theoretic regulator parallel
- [`conj:kashaev-volume-conjecture`](kashaev-volume-conjecture.md)
  — Volume Conjecture is the leading-order 3d–3d statement
- [Dimofte–Gaiotto–Gukov 2014; Terashima–Yamazaki 2011]
