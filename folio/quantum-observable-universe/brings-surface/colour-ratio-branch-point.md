Write $P(\mathbf{c}, z)$ for the left side of the [colour tube cubic](#rem:color-tube-cubic). Its discriminant in $\mathbf{c}$ is

$$
\operatorname{Disc}_{\mathbf{c}} P = -\left(16z^6 + 24z^5 + 35z^4 + 50z^3 + 35z^2 + 24z + 16\right),
$$

and the sextic is irreducible over $\mathbb{Q}$. So the colour roots collide at exactly six branch points $z_c$, which are Galois conjugate.

**Local splitting.** Fix a branch point $z_c$ and label the roots so that $\mathbf{r}_{z_c} = \mathbf{g}_{z_c} = \rho$ is the double root and $\mathbf{b}_{z_c}$ is the simple one. By the sum formula, $\mathbf{b}_{z_c} = -(4z_c+1) - 2\rho$, and

$$
\tfrac{1}{2}\,\partial_{\mathbf{c}}^2 P(\rho, z_c) = 3\rho + 4z_c + 1 = \rho - \mathbf{b}_{z_c}.
$$

Since $\rho$ is a double root, it is fixed by the Galois group of $\overline{\mathbb{Q}}/\mathbb{Q}(z_c)$, so $\rho \in \mathbb{Q}(z_c)$. Moreover $\rho \neq 0$, because the resultant of the constant term $4z^3 + 3z^2 + 2z + 1$ and the linear coefficient $6z^2 + 3z + 1$ is $100$. Write $z = z_c + t^2$ for a local parameter $t$. The double root splits as

$$
\mathbf{r}_z = \rho + Ct + O(t^2), \qquad \mathbf{g}_z = \rho - Ct + O(t^2), \qquad C^2 = -\frac{\partial_z P(\rho, z_c)}{\rho - \mathbf{b}_{z_c}},
$$

where $\partial_z P = 4\mathbf{c}^2 + (12z+3)\mathbf{c} + 12z^2 + 6z + 2$.

**The Möbius matrix.** Put $\varpi = \rho / C$. The ratio of the linear truncations is

$$
\frac{\rho + Ct}{\rho - Ct} = \frac{t + \varpi}{-t + \varpi} = \mu_\varpi(t),
$$

the Möbius map of the matrix $M_\varpi$ of the [colour-ratio Möbius matrix lemma](#lem:colour-ratio-mobius-matrix). Hence the colour ratio satisfies $\mathbf{r}_z / \mathbf{g}_z = \mu_\varpi(t) + O(t^2)$. This identification holds to first order in $t$ only; the ratio is not exactly a Möbius function of $t$. Under it, $t = -\varpi$ is the zero of the linear truncation of $\mathbf{r}_z$, $t = 0$ is the branch point itself, where the ratio is $1$, and $t = \varpi$ is the zero of the linear truncation of $\mathbf{g}_z$.

**Field of definition.** Since $\rho$ and $C^2$ lie in $\mathbb{Q}(z_c)$, so does $\varpi^2 = \rho^2 / C^2$. Hence $[\mathbb{Q}(z_c, \varpi) : \mathbb{Q}] \leq 12$.

**Conjugacy class.** By item 4 of the lemma, $M_\varpi$ is parabolic exactly when $\varpi^2 - 6\varpi + 1 = 0$, that is, $\varpi = 3 \pm 2\sqrt{2}$. The normalised squared trace $(\operatorname{tr} M_\varpi)^2 / \det M_\varpi = (\varpi + 2 + \varpi^{-1})/2$ is real only when $\varpi$ is real or $|\varpi| = 1$. Evaluating the algebraic numbers $\varpi^2$ at the six branch points to $30$ digits gives

$$
\varpi^2 \approx 1.54517 \pm 0.07255\,i, \qquad \pm 0.73878\,i, \qquad -1.54517 \pm 0.07255\,i,
$$

each value occurring at a conjugate pair of branch points. None of these is real, so $\varpi$ is never real, and none has modulus $1$, so $|\varpi| \neq 1$. Therefore $M_\varpi$ is loxodromic at every branch point, and the parabolic values $3 \pm 2\sqrt{2}$ are not attained. This last paragraph rests on a numerical evaluation of algebraic numbers, not on a proof.
