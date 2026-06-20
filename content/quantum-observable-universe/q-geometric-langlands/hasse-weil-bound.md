*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

The 8 fundamental eigenvalues of the Frobenius endomorphism satisfy
the Hasse--Weil bound:

$$
|\alpha_i| = q^{1/2} \qquad \text{for all } i = 1, \ldots, 8
$$

**Proof sketch.** The argument proceeds via the Castelnuovo--Severi
inequality on the self-product $\mathcal{B} \times \mathcal{B}$. The
diagonal $\Delta \subset \mathcal{B} \times \mathcal{B}$ defines a
correspondence whose intersection number with the graph of
$\mathrm{Fr}_q^n$ counts $|\mathcal{B}(\mathbb{F}_{q^n})|$. The Hodge
index theorem on the surface $\mathcal{B} \times \mathcal{B}$ implies
the Castelnuovo--Severi inequality:

$$
\bigl(D \cdot D\bigr) \le 2g \cdot \bigl(D \cdot H\bigr)
$$

for any correspondence $D$ and ample divisor $H$. Applied to
$D = \mathrm{graph}(\mathrm{Fr}_q^n) - q^n \cdot \Delta$, this yields
$|\alpha_i|^2 \le q$ for all $i$. The functional equation
$P(t) = q^g t^{2g} P(1/qt)$ then forces $|\alpha_i|^2 = q$,
completing the proof.

This is the **Riemann hypothesis for Bring's curve over
$\mathbb{F}_q$** — an unconditional theorem, not a conjecture,
established by Weil's foundational work on algebraic geometry over
finite fields.
