Let $\Sigma_4 = \Gamma\backslash\mathbb{H}$ be [Bring's surface](#def:brings-surface) with its hyperbolic metric of curvature $-1$, where $\Gamma \subset \mathrm{PSL}_2(\mathbb{R})$ is a torsion-free Fuchsian group of genus $4$. Let $M = \mathrm{UT}(\Sigma_4) \cong \Gamma\backslash\mathrm{PSL}_2(\mathbb{R})$ be its unit tangent bundle, the total space of the Reeb bundle of the [Descartes universe](#thm:ns-singularity-descartes). In $\mathfrak{sl}_2(\mathbb{R})$ put

$$
  X = \tfrac{1}{2}H, \qquad Y = \tfrac{1}{2}(E + F), \qquad V = \tfrac{1}{2}(E - F),
$$

so that $[X, Y] = V$, $[X, V] = Y$ and $[Y, V] = -X$. The left-invariant extensions of $X$, $Y$, $V$ descend to $M$, and $V$ generates the rotation of the circle fibres of $M \to \Sigma_4$. For $s > 0$ let $g_s$ be the left-invariant metric whose matrix in the frame $(X, Y, V)$ is $\mathrm{diag}(1, 1, s^2)$. Orient $M$ by $(X, Y, V)$ and define $\mathrm{curl}\,u$ by $(\mathrm{curl}\,u)^\flat = \star\,d u^\flat$. Then:

1. $V$ is a Killing field of $g_s$, with $\mathrm{div}\,V = 0$, $\nabla_V V = 0$ and $\mathrm{curl}\,V = -s\,V$. The unit field $V/s$ satisfies the same Beltrami equation $\mathrm{curl}(V/s) = -s\,(V/s)$.
2. $\mathrm{curl}\,\mathrm{curl}\,V = s^2 V$, $\mathrm{Ric}(V) = \tfrac{s^2}{2} V$ and $\nabla^*\nabla V = \tfrac{s^2}{2} V$.
3. Consider the unforced incompressible Navier--Stokes equations on $(M, g_s)$,

   $$
     \partial_t u + \nabla_u u + \mathrm{grad}\,p = \nu\,L u, \qquad \mathrm{div}\,u = 0, \qquad \nu \geq 0,
   $$

   with one of three viscous operators: the deformation operator $L_{\mathrm{Def}} = -(\Delta_H - 2\,\mathrm{Ric})$, which equals $2\,\mathrm{div}\,\mathrm{Def}$ on divergence-free fields \cite{ebin-marsden1970}; the Hodge operator $L_H = -\Delta_H$; or the Bochner operator $L_B = -\nabla^*\nabla$. Here $\Delta_H$ is the Hodge Laplacian transported to vector fields by $g_s$, which equals $\mathrm{curl}\,\mathrm{curl}$ on divergence-free fields. For every $a \in \mathbb{R}$ and every $\nu \geq 0$, with constant pressure $p$, the field

   $$
     u(t) = a\,V \;\;(L = L_{\mathrm{Def}}), \qquad
     u(t) = a\,e^{-\nu s^2 t}\,V \;\;(L = L_H), \qquad
     u(t) = a\,e^{-\nu s^2 t/2}\,V \;\;(L = L_B)
   $$

   is a smooth solution on $M \times [0, \infty)$. Under $L_{\mathrm{Def}}$ it is steady and extends to $M \times \mathbb{R}$. At $\nu = 0$ all three reduce to the steady Euler solution $u \equiv a\,V$.
