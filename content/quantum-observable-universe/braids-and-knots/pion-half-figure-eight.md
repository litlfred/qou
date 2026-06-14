**Proposition (pion = half-figure-eight on $V_{(2,1)}$).**
*The pion braid $\mathfrak{M}_+ = (\sigma_1\sigma_2)^2\sigma_2\sigma_1$
and the half-figure-eight braid $\sigma_1\sigma_2^{-1}$ have
identical eigenvalue phases when acting on the standard
representation $V_{(2,1)}$ of $H_3(q)$:*

$$
  \mathrm{arg}\bigl(\lambda(\mathfrak{M}_+)\bigr)
  = \mathrm{arg}\bigl(\lambda(\sigma_1\sigma_2^{-1})\bigr).
$$

*The figure-eight knot operator $(\sigma_1\sigma_2^{-1})^2$ is the
square of the pion-type rotation.*

**Mathematical Novelty.** While the proof itself is a straightforward characteristic-polynomial comparison for $2 \times 2$ matrices with equal trace and determinant, the mathematical novelty is structurally mapping the meson's topological state to a specific "half-knot" Reeb rotation, directly formalising the relationship between meson decay energies and the lepton mass ratio (figure-eight volume) via the algebraic squaring relation $4_1 = (\sigma_1\sigma_2^{-1})^2$.

**Formalization Goal Plausibility.** The formalization intentionally focuses on the algebraic reduction—verifying that identical traces and determinants force identical characteristic polynomials and eigenvalues in the $2 \times 2$ module. The specific trace identity $\chi^{(2,1)}(\mathfrak{M}_+) = -(h^2+1)$ is introduced as an assumed hypothesis rather than calculated from scratch; this is a routine computational fact in representation theory, not a disguised gap. By factoring out the topological character computation, the goal of verifying the spectral consequences becomes highly plausible and sharply targeted.

**Proof.** Both $\mathfrak{M}_+$ and $\sigma_1\sigma_2^{-1}$ have
determinant $+1$ on $V_{(2,1)}$ (even number of Hecke generators,
each with $\det = -1$; the product of an even number of $(-1)$
factors is $+1$).  Both have real trace on $V_{(2,1)}$:

$$
  \chi^{(2,1)}(\mathfrak{M}_+) = -(h^2 + 1),
  \qquad
  \chi^{(2,1)}(\sigma_1\sigma_2^{-1}) = -(h^2 + 1).
$$

Since both are $2 \times 2$ matrices with $\det = 1$ and identical
trace, they have the **same characteristic polynomial**:

$$
  \lambda^2 + (h^2 + 1)\lambda + 1 = 0.
$$

The eigenvalues are therefore identical:
$\lambda = \tfrac{-(h^2+1) \pm \sqrt{(h^2+1)^2 - 4}}{2}$,
giving complex conjugates on the unit circle with the same
phase $\theta = \arccos\bigl(-(h^2+1)/2\bigr)$.  $\square$

## The half-rotation interpretation

The figure-eight knot $4_1 = (\sigma_1\sigma_2^{-1})^2$ is the
**composition of two pion-type rotations**.  Each pion rotation
advances the Reeb phase by $\theta$; two such advances give the
figure-eight's eigenvalue phase $2\theta \pmod{2\pi}$.

The muon-anchor identity
$m_\mu / m_\mathfrak{e} = \mathrm{Vol}(4_1) / \hbar_q^2$
uses the volume of the figure-eight — the asymptotic value of
twice the pion rotation angle.  The pion is the **generator**
of the Reeb rotation tower; the figure-eight is its square.

## Connection to pion decay

The pion decay $\pi \to \mu + \nu$
([`prop:hoefsmit-binding-amplitude`](hoefsmit-binding-amplitude.md))
de-entangles $V_{(2,1)}$ into $V_{(2)} \oplus V_{(1,1)}$.  This
is the **inverse** of a half-Reeb-rotation: the pion's eigenvalue
phase $\theta$ is the energy that was stored in the entanglement,
and the decay releases it by undoing the rotation.

Two such decays (two pions) would undo a full figure-eight
rotation — connecting the meson decay energy to the lepton
mass ratio through the composition $4_1 = (\text{half-rotation})^2$.
