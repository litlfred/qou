**Proposition (figure-eight knot operator is unitary on $V_{(2,1)}$).**
*The knot operator $M_{4_1} = (\sigma_1\sigma_2^{-1})^2$ of the
figure-eight knot, acting on the standard representation $V_{(2,1)}$
of $H_3(q)$, has eigenvalues of unit modulus:*

$$
  \lambda_{4_1} = e^{\pm i\theta},
  \qquad |\lambda_{4_1}| = 1.
$$

*The eigenvalue phase $\theta$ is the accumulated
$q$-Reeb rotation angle of the alternating braid
$\sigma_1\sigma_2^{-1}\sigma_1\sigma_2^{-1}$.*

*

## Connection to the $q$-Reeb flow

The $q$-Reeb flow
([`ex:q-reeb-flow`](../climax-volume-mass/q-reeb-flow-on-coral-coords.md))
advances the coral-sector angular coordinate by $q \cdot t$
per crossing on the active strands.  For an alternating braid
$\sigma_a\sigma_b^{-1}$, the positive crossing $\sigma_a$
advances by $+q\pi$ and the negative crossing $\sigma_b^{-1}$
advances by $-q^{-1}\pi$.  The net Reeb advance per alternating
pair is $(q - q^{-1})\pi = h\pi$.

The figure-eight braid has TWO such pairs, giving total Reeb
advance $2h\pi$ on the pair of active strands.  Restricted to
$V_{(2,1)}$, this advance manifests as the eigenvalue phase
$\theta = \mathrm{arg}(\lambda_{4_1})$.

The q-Reeb flow rotates between the two lepton channels
$V_{(2)}$ and $V_{(1,1)}$ that constitute $V_{(2,1)}$ under
Frobenius restriction
([`prop:frobenius-lepton-meson-bridge`](frobenius-lepton-meson-bridge.md)).
The rotation angle $\theta$ is the **accumulated Reeb phase** of
the figure-eight's alternating crossings — the same geometric
quantity that, in the Kashaev $N \to \infty$ limit, yields the
hyperbolic volume $\mathrm{Vol}(4_1)$.

## Why $4_1$ sets the mass scale

The $q$-Reeb rotation mixes the lepton channels
$V_{(2)} \leftrightarrow V_{(1,1)}$ inside $V_{(2,1)}$.  The
rotation angle $\theta$ is the natural invariant of this mixing.
The muon-anchor identity
$m_\mu / m_\mathfrak{e} = \mathrm{Vol}(4_1) / \hbar_q^2$
uses the **asymptotic volume** (Kashaev limit of $\theta$).
The finite-$q$ phase $\theta(q_0)$ and the asymptotic volume
$\mathrm{Vol}(4_1)$ are related by the Volume Conjecture; the
mass formula uses the asymptotic form because the lepton sector
lives at $H_2$ where the Kashaev limit is the natural evaluation.

The figure-eight knot $4_1$ appears in the mass formula because
it is the **simplest alternating braid** at $H_3$ — the
minimal-crossing braid that implements a full Reeb rotation on
$V_{(2,1)}$.  Its volume is the rotation angle, and the rotation
is the mechanism that connects the two lepton generations.

## Lean realisation (archimedean specialisation, §7c)

The unitarity statement is realised on the **archimedean side**. The
structural inputs — $\det(M_{4_1}) = 1$ (a product of generator
determinants $q\cdot(-q^{-1}) = -1$, an exact identity over the formal
field $\mathbb{Q}(q^{1/2})$) and the reality of the trace — are
substrate/categorical and base-ring-agnostic. The *conclusion*
$|\lambda_{4_1}| = 1$, however, is an archimedean assertion: it says the
eigenvalues lie on the unit circle of $\mathbb{C}$. The Lean
`QOU.BraidsAndKnots.figure_eight_unitary_on_standard` proves it over
$\mathbb{R}$ via the complex norm $\lVert\cdot\rVert$ /
`Complex.normSq` and the ordering hypothesis $t^2 < 4$ (forcing a
non-real root), discharged by `nlinarith`. The complex modulus, the
unit circle, and the real trace bound $t^2 < 4$ are the archimedean
constructs that pin this formalisation to $\mathbb{R}$; the determinant
identity itself stays on the substrate side (`figure_eight_det_one` for
the $\mathbb{R}$ specialisation used here, with the generic
Hecke-generator determinant lemma belonging in the algebraic layer).

**Mathematical Novelty:** The q-Reeb-rotation-phase reading of the figure-eight eigenvalue on $V_{2,1}$, which connects to $\mathrm{Vol}(4_1)$ and the muon anchor, is a genuinely framework-specific and novel conceptual idea. (Note that this connection is asserted conceptually rather than fully established in the formalization).
