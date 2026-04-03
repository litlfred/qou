For readers more familiar with vector calculus than differential
geometry, we briefly recall how the classical operators appear in the
language of differential forms on a smooth Riemannian manifold
$(M, g)$.

**Forms by degree.** A $0$-form is a scalar field $f \colon M \to \mathbb{R}$ (temperature, electrostatic potential). A $1$-form
$\alpha$ assigns to each tangent vector a number — it is the
geometric version of a vector field (velocity, force, the gradient
of a potential). A $2$-form $\beta$ measures oriented flux through
an infinitesimal parallelogram (magnetic field strength, vorticity).

**The exterior derivative $d$.**
- On a $0$-form: $df$ is the *gradient*. In coordinates,
  $df = \partial_i f\, dx^i$.
- On a $1$-form: $d\alpha$ is the *curl*. If
  $\alpha = P\,dx + Q\,dy + R\,dz$ in $\mathbb{R}^3$, then
  $d\alpha = (\partial_y R - \partial_z Q)\,dy \wedge dz + \cdots$
- The identity $d^2 = 0$ encodes both $\nabla \times (\nabla f) = 0$
  and $\nabla \cdot (\nabla \times \mathbf{F}) = 0$.

**The Hodge star $\star$.**
On an $n$-dimensional manifold, $\star$ maps $k$-forms to
$(n{-}k)$-forms by "complementing" directions:
$\star(dx) = dy \wedge dz$ in $\mathbb{R}^3$. It converts between
the two natural duals of a differential form.

**The codifferential $\delta$ and divergence.**
The codifferential $\delta = (-1)^{nk+n+1}\,\star d\,\star$ is the
formal adjoint of $d$. On $1$-forms in $\mathbb{R}^3$,
$\delta\alpha = -\mathrm{div}(\alpha^{\sharp})$, where
$\alpha^{\sharp}$ is the vector field dual to $\alpha$.

**The Laplacian.**
The Hodge Laplacian is $\Delta = d\delta + \delta d$. On $0$-forms,
$\Delta f = \delta\, df$, which equals $-\nabla^2 f$ (the negative
of the analyst's Laplacian). A function $f$ is *harmonic*
($\Delta f = 0$) precisely when it has no sources or sinks: its
value at each point equals the average over any small sphere
centered there.
