*Within a QOU $(\mathbf{C}, A, \tau)$.* This block defines a class of classical velocity fields on $\mathbb{R}^3$. It asserts nothing about their existence.

**Definition (discretely self-similar Leray profile).** Fix a point $x_0 \in \mathbb{R}^3$ and a time $T^*$. Leray's similarity variables are
$$
y = \frac{x - x_0}{\sqrt{T^* - t}}, \qquad s = -\log(T^* - t), \qquad t < T^* .
$$
A **Leray profile** is a vector field $V(y, s)$ on $\mathbb{R}^3 \times \mathbb{R}$, and the velocity field it defines is
$$
v(x, t) = (T^* - t)^{-1/2}\, V\bigl(y, s\bigr).
$$
The profile is **:defterm[discretely self-similar]{#discretely-self-similar}** with period $P > 0$ if $V(y, s + P) = V(y, s)$ for all $y$ and $s$. It is **steady** if $V$ does not depend on $s$.

Writing $\lambda = e^{P/2} > 1$, periodicity in $s$ is equivalent to the discrete scaling invariance
$$
v(x, t) = \lambda\, v\bigl(x_0 + \lambda (x - x_0),\; T^* - \lambda^2 (T^* - t)\bigr),
$$
which for $x_0 = 0$, $T^* = 0$ is $v(x, t) = \lambda\, v(\lambda x, \lambda^2 t)$ (Lean `lerayField_discrete_scaling`). A steady profile is discretely self-similar for every period.

The field $v$ solves the Navier--Stokes equation with viscosity $\nu$ if and only if $V$ solves the Leray system
$$
\partial_s V - \nu \Delta_y V + \tfrac{1}{2} V + \tfrac{1}{2} (y \cdot \nabla_y) V + (V \cdot \nabla_y) V + \nabla_y \Pi = 0, \qquad \nabla_y \cdot V = 0 ,
$$
with pressure profile $\Pi(y, s)$. The known constraints on nonzero solutions are collected in [Exclusions for discretely self-similar profiles](#rem:leray-profile-exclusions); finite truncations are discussed in [Truncations of the Leray system](#rem:leray-profile-construction).
