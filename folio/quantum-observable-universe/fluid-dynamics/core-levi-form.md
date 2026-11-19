**Proposition ("Core Levi form").**

Let $D$ be the three-dimensional flow domain, $\mathbb{R}^3$ or $\mathbb{T}^3$ with the Euclidean metric. This is a statement on $D$, not on the [state bundle](#ex:c-quantum-observable-universe) $\mathcal{S}$: the chapter also uses $\mathcal{S}$ as a surface, where a contact structure cannot exist. Let $u$ be a smooth velocity field on $D$ with vorticity $\omega = \mathrm{curl}\,u$, and on the open set $D_\omega = \{\omega \neq 0\}$ let $\xi = \omega/|\omega|$ be the vorticity direction. For a smooth scalar $f > 0$ on $D_\omega$ set

$$
  \varTheta := f\,\xi^\flat ,
$$

where $\xi^\flat$ is the metric dual of $\xi$. Then on $D_\omega$:

*(a)* The plane field is the orthogonal complement of the vorticity line: $\ker \varTheta = \xi^\perp$.

*(b)* $\varTheta \wedge d\varTheta = f^2\,(\xi\cdot\mathrm{curl}\,\xi)\,\mathrm{vol}$. Hence $\ker\varTheta$ is a contact structure at $x$ if and only if $(\xi\cdot\mathrm{curl}\,\xi)(x) \neq 0$, independently of $f$.

*(c)* The [Levi datum](#def:levi-form-defect) of $\ker\varTheta$ is one scalar. For $v, w \in \xi^\perp$,

$$
  d\varTheta(v, w) = f\,(\xi\cdot\mathrm{curl}\,\xi)\;\xi\cdot(v\times w),
$$

so the restriction of $d\varTheta$ to $\ker\varTheta$ is $f\,(\xi\cdot\mathrm{curl}\,\xi)$ times the area form of the plane. There is no pair of Levi eigenvalues and no Levi condition number in dimension $3$.

*(d)* $\omega\cdot\mathrm{curl}\,\omega = |\omega|^2\,(\xi\cdot\mathrm{curl}\,\xi)$. The contact locus of $\ker\varTheta$ is therefore $\{\omega\cdot\mathrm{curl}\,\omega \neq 0\}$.

**Proof.** Part (a) is the definition, since $f > 0$.

For (b), $d\varTheta = df\wedge\xi^\flat + f\,d\xi^\flat$. The first term wedges to zero against $\varTheta$ because $\xi^\flat\wedge\xi^\flat = 0$. The identity $\xi^\flat\wedge d\xi^\flat = (\xi\cdot\mathrm{curl}\,\xi)\,\mathrm{vol}$ then gives the formula, and $f^2 > 0$ gives the criterion.

For (c), $df\wedge\xi^\flat$ vanishes on $\xi^\perp$, and $d\xi^\flat(v,w) = \mathrm{curl}\,\xi\cdot(v\times w)$. For $v, w \perp \xi$ the vector $v\times w$ is parallel to the unit vector $\xi$, so $\mathrm{curl}\,\xi\cdot(v\times w) = (\xi\cdot\mathrm{curl}\,\xi)\,\xi\cdot(v\times w)$.

For (d), write $\omega = |\omega|\,\xi$. Then $\mathrm{curl}\,\omega = |\omega|\,\mathrm{curl}\,\xi + \nabla|\omega|\times\xi$, and $\xi\cdot(\nabla|\omega|\times\xi) = 0$. $\square$

**Examples.** For the Beltrami flow $u = e^{-\nu t}(\sin z, \cos z, 0)$ on $\mathbb{T}^3$, $\xi\cdot\mathrm{curl}\,\xi = 1$ everywhere, so $\ker\varTheta$ is contact on all of $\mathbb{T}^3$. For a straight anti-parallel vortex pair, $\xi = \pm e_z$ is constant on each core, so $\xi\cdot\mathrm{curl}\,\xi = 0$ there and $\ker\varTheta$ is integrable. This holds whatever the cross-sectional shape of the cores, so the core aspect ratio carries no Levi information.

**Relation to the regularity criteria.** The Constantin–Fefferman condition \cite{constantin1993} and its $\tfrac{1}{2}$-Hölder improvement by Beirão da Veiga and Berselli \cite{beiraodaveiga2002} bound the variation of the line field $[\xi]$ on the high-vorticity set. Such a bound controls all of $\nabla\xi$, and so gives an *upper* bound on $|\xi\cdot\mathrm{curl}\,\xi|$. The Levi scalar is one component of $\nabla\xi$. Neither its vanishing nor its non-vanishing implies either criterion. What the criteria do give is stated in the [Levi degeneracy conjecture](#conj:levi-degeneracy).
