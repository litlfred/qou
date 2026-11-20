*Proof.*
The group $\Gamma$ acts on $\mathrm{PSL}_2(\mathbb{R})$ on the left, so left-invariant vector fields, forms and metrics on $\mathrm{PSL}_2(\mathbb{R})$ descend to $M$. The Levi-Civita connection of a left-invariant metric maps pairs of left-invariant fields to left-invariant fields, so every quantity in items 1 and 2 is computed on the Lie algebra. The field $V$ generates the fibre rotation because $\exp(\theta V)$ rotates unit tangent vectors by the angle $\theta$.

Items 1 and 2 are computations in the basis $(X, Y, V)$. The Koszul formula determines $\nabla$ on left-invariant fields. The operator $\mathrm{ad}_V$ is skew for $g_s$, so $V$ is Killing and $\mathrm{div}\,V = 0$. The remaining values follow from the Koszul connection, from the curvature $R(u,v)w = \nabla_u\nabla_v w - \nabla_v\nabla_u w - \nabla_{[u,v]} w$ traced over the orthonormal frame $(X, Y, V/s)$, and from the definition of $\mathrm{curl}$. The values satisfy the Weitzenböck identity $\nabla^*\nabla V + \mathrm{Ric}(V) = \Delta_H V$ and agree with Milnor's Ricci formula $\mathrm{Ric}(X) = -(1 + s^2/2)\,X$.

For item 3 write $u(t) = a(t)\,V$. Then $\mathrm{div}\,u = 0$ and $\nabla_u u = a^2\,\nabla_V V = 0$ by item 1, so with constant $p$ the equations reduce to $a'(t)\,V = \nu\,a(t)\,L V$. By items 1 and 2, $L_{\mathrm{Def}} V = -(s^2 - s^2)\,V = 0$, $L_H V = -s^2 V$ and $L_B V = -\tfrac{s^2}{2} V$. This gives $a' = 0$, $a' = -\nu s^2 a$ and $a' = -\tfrac{\nu s^2}{2} a$ respectively, with the stated solutions. Each $u(t)$ is a smooth multiple of the smooth field $V$ for all $t$. $\square$

**Formal verification.** The Lie-algebra computations are proved in Lean, sorry-free, in `QOU/FluidDynamics/BeltramiSteadyEuler.lean`, namespace `QOU.FluidDynamics.BeltramiSteadyEuler`:

- `sl2_brackets` and `L3.toMat_br` for the brackets, checked as $2 \times 2$ matrix commutators;
- `L3.nab_torsion_free` and `L3.nab_metric`, which identify the Koszul connection used with the Levi-Civita connection on left-invariant fields;
- `L3.V_killing`, with the non-vacuity check `L3.X_not_killing`;
- `L3.nab_VV`, `L3.curl_V`, `L3.curl_curl_V`, `L3.ric_V`, `L3.ric_X`, `L3.rough_V` and `L3.weitzenbock_V`;
- `L3.deformation_V`, the identity $(\Delta_H - 2\,\mathrm{Ric})\,V = 0$.

The same file proves the flat analogue end to end with Mathlib derivatives: a Beltrami eigenfield yields an exact Navier--Stokes solution, and the ABC field gives the solution $e^{-\nu t} u_{\mathrm{ABC}}$ on the three-torus.

Two standard steps are not formalised: the descent of left-invariant data from $\mathrm{PSL}_2(\mathbb{R})$ to $\Gamma\backslash\mathrm{PSL}_2(\mathbb{R})$, and the identification of the manifold operators $\nabla$, $\mathrm{Ric}$, $\nabla^*\nabla$ and $\Delta_H$ on left-invariant fields with the Lie-algebra formulas above. The reduction of the equations to the scalar equation for $a(t)$ in item 3 is carried out by hand.
