**Remark (Yekutieli license: PL is the archimedean shadow of non-abelian
Stokes).**
*The Picard–Lefschetz thimble decomposition
([Picard–Lefschetz thimble](#def:picard-lefschetz-thimble))
acquires its categorical license from the non-abelian Stokes
theorem.  Without that license, PL on $\mathcal{E}_q$ would be
ordinary complex analysis with no formal connection to the
categorical machinery of $H_n(R, q)$ and the GB spectral sequence.*

*The licensing chain has three links:*

**1. Categorical ($R$-side): MI-integral over a categorical surface.**
*By
([Yekutieli–Stokes remark](#rem:yekutieli-stokes)) and
([topological mass holonomy](#prop:topological-mass-formula)),
the categorical mass of a vortex $\varrho$ admits an MI-integral
representation*

$$
  \mathfrak{m}(\varrho)
  \;=\;
  \mathrm{MI}\!\!\int_{\Sigma}\, F_{\nabla_A}
  \;\in\; R
$$

*with $\partial \Sigma = \varrho$, where $F_{\nabla_A}$ is the
curvature of the categorical connection.  This statement is fully
on the $R$-side: $\Sigma$ is a categorical surface in $\mathbf{C}$,
and $\mathrm{MI}\!\!\int$ is the multiplicative integral defined in
$\mathbf{C}$
([yekutieli2015]).*

**2. Bridge ($\tau$): non-abelian Stokes commutes with $\tau$.**
*Apply the archimedean fibre functor
$\tau \colon R \hookrightarrow \mathbb{C}$.  Because $\tau$ is a
monoidal functor, it commutes with the multiplicative integral:*

$$
  \tau\Bigl(\mathrm{MI}\!\!\int_{\Sigma}\, F_{\nabla_A}\Bigr)
  \;=\;
  \mathrm{MI}\!\!\int_{\tau(\Sigma)}\, \tau(F_{\nabla_A})
  \;\in\; \mathbb{C}.
$$

*The right-hand side is now a $\mathbb{C}$-valued surface integral on
the archimedean realisation of $\Sigma$, with the categorical
curvature replaced by the SW field strength $F_{\nabla_A} \mapsto
d\lambda^{(1)}_{\mathrm{SW}}$.*

**3. Archimedean ($\mathbb{C}$-side): contour collapse to thimble residues.**
*On the $\mathbb{C}$-side, the surface $\tau(\Sigma)$ may be deformed
without changing the value of the MI-integral, provided the
deformation does not cross the discriminant locus
$\{z : \Delta(z) = 0\}$.  Deforming $\tau(\Sigma)$ to a "thimble cap"
— a finite union of steepest-descent disks $\{D_\sigma\}$ each
attached to a critical point $z_\sigma$ of $S$ — collapses the
surface integral to a finite sum of point residues:*

$$
  \mathrm{MI}\!\!\int_{\tau(\Sigma)}\, d\lambda^{(1)}_{\mathrm{SW}}
  \;=\;
  \sum_{\sigma}
    n_\sigma \cdot \mathrm{Res}_{z = z_\sigma}\, \lambda^{(1)}_{\mathrm{SW}}
  \;=\;
  \sum_{\sigma}
    n_\sigma \oint_{\mathcal{J}_\sigma}\, \lambda^{(1)}_{\mathrm{SW}}\, dz
  \;=\;
  \Pi^{(1)},
$$

*which is the Picard–Lefschetz period
([SW-period thimble equivalence](#prop:sw-period-thimble-equivalence)).
The intersection numbers $n_\sigma$ are determined by how the original
contour $\partial(\tau(\Sigma))$ wraps around each $z_\sigma$.*

**Summary diagram.**

$$
  \begin{tikzcd}[column sep=large]
    \displaystyle\mathrm{MI}\!\!\int_{\Sigma}\, F_{\nabla_A}
    \arrow[r, "\tau"] \arrow[d, equal, "\text{Yekutieli, $R$-side}"']
    & \displaystyle\mathrm{MI}\!\!\int_{\tau(\Sigma)}\, d\lambda^{(1)}_{\mathrm{SW}}
    \arrow[d, equal, "\text{contour collapse, archimedean}"] \\
    \mathfrak{m}(\varrho)
    \arrow[r, "\tau"]
    & \displaystyle\sum_\sigma n_\sigma\, \Pi^{(1)}_\sigma
  \end{tikzcd}
$$

*The diagram commutes: the $R$-side categorical mass and the
$\mathbb{C}$-side PL period are two facets of the same
non-abelian-Stokes datum, related by $\tau$.*

**Why this remark exists.**

*Without
([Yekutieli–Stokes remark](#rem:yekutieli-stokes)) and
([topological mass holonomy](#prop:topological-mass-formula)),
the steepest-descent integral on $\mathcal{E}_q$ would be a free-
floating complex-analytic computation, disconnected from the
categorical formalism that defines what "mass" means in the QOU.
This remark records the formal bridge: PL is **not an alternative**
to the Yekutieli surface integral; it is its **archimedean
realisation**, accessible only after $\tau$.*

**Strict archimedean split.**

*The diagram's two rows live on opposite sides of $\tau$:*

- *Top row: categorical surfaces, MI-integrals, curvature 2-forms in
  $\mathbf{C}$.  All $R$-valued.*
- *Bottom row: $\mathbb{C}$-contours, residues, Picard–Lefschetz
  thimbles.  All $\mathbb{C}$-valued.*

*The vertical arrows are $\tau$ itself.  The horizontal equalities
within each row are intrinsic to that side and do not require $\tau$.
The commutativity of the diagram (i.e. $\tau$-commutation with the
two collapse operations) is the proposition's content.*
