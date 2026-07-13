<!-- FILE_START: color-fibration-elliptic-intro.md -->
The intrinsic color cubic supplies the data to identify an elliptic curve over the color parameter. We establish this in the proposition that the generic color fibre carries the Weierstrass structure $\mathcal{E}_q$. The color elliptic curve exhibits self-duality, possessing a $T$-duality that pairs $q \leftrightarrow q^{-1}$. We translate the elliptic data back into the tube coordinates and demonstrate how the $T$-duality acts on the tubes themselves.

The closing blocks isolate the confinement geometry. We identify the discriminant locus where the elliptic fibre degenerates. We extract the explicit constraint a pure-color state must satisfy. This structure underpins the bundle smoothness analysis on $\mathbb{P}^1$ in the next section.
<!-- FILE_END: color-fibration-elliptic-intro.md -->

<!-- FILE_START: color-elliptic.md -->
Let $z=x_0/x_1\in\mathbb{P}^1(\mathbb{C})$ be the projective spacetime ratio ([braid group action](#rem:braid-group-action)(i)). We substitute the constraint $x_0+x_1=C$ and eliminate $x_0,x_1$ in favour of $z$. The quadratic and cubic power-sum conditions on the color variable $X=(x_2,x_3,x_4)$ reduce at each fixed $z$ to the cubic

```tex
\begin{equation}\label{eq:color-elliptic}
  X^3+(z+1)X^2+(z^2+z+1)X+(z^3+z^2+z+1)=0.
\end{equation}
```

The variable $X$ is so named because the geometry of the fibre is a weave of colorful twisted tubes with fractal boundary structure, capturing color, chirality, and rigidity. For generic $z$, this cubic defines an elliptic curve $\mathcal{E}_z$ in the color fibre. Its $j$-invariant varies as a rational function of $z$. The monodromy of $\mathcal{E}_z$ around the singular fibres (where the discriminant of the cubic vanishes) recovers the holonomy generators $H_1,H_2$ of [holonomy of trefoil](#rem:holonomy-trefoil).
<!-- FILE_END: color-elliptic.md -->

<!-- FILE_START: t-duality-elliptic.md -->
The cubic is symmetric under the exchange $X\leftrightarrow z$. Writing

$$
  F(X,z)= X^3+(z+1)X^2+(z^2+z+1)X+(z^3+z^2+z+1),
$$

we verify $F(X,z)=F(z,X)$ term by term. This involution $\iota\colon(X,z)\mapsto(z,X)$ is a *T-duality*. It identifies every color fibre $\mathcal{E}_z$ with its dual spacetime wrapping $\mathcal{E}_X$. The internal and external degrees of freedom of Bring's surface are thus algebraically indistinguishable.

**Quotient space.**
Passing to the symmetric coordinates $u=X+z$, $v=Xz$, the curve becomes

```tex
\begin{equation}\label{eq:symmetric-quotient}
  v =  \frac{(u+1)(u^2+1)}{2u+1}.
\end{equation}
```

This is rational in $u$. Hence the quotient is $\mathcal{E}_z/\langle\iota\rangle\cong\mathbb{P}^1(\mathbb{C})$. Folding the torus along its $X=z$ diagonal collapses it to a genus-$0$ Riemann sphere.

**Weierstrass normal form.**
Depressing the cubic via $X=t-\tfrac{z+1}{3}$ eliminates the quadratic term:

```tex
\begin{equation}\label{eq:weierstrass-depressed}
  t^{3}+p(z)t+q(z)=0,\qquad
  p=\frac{2z^2+z+2}{3},\quad
  q=\frac{5(4z^3+3z^2+3z+4)}{27}.
\end{equation}
```

The discriminant $\Delta(z)=-4p(z)^3-27q(z)^2$ is a polynomial in $z$. Its roots determine the singular fibres of the elliptic fibration $\mathcal{S}\to\mathbb{P}^1(\mathbb{C})$. At those roots, the $j$-invariant $j(\mathcal{E}_z)=-1728\cdot 64p(z)^3/\Delta(z)$ degenerates.
<!-- FILE_END: t-duality-elliptic.md -->

<!-- FILE_START: color-tube-cubic.md -->
At a fixed $z \in \mathbb{P}^1(\mathbb{C})$, the three color roots of the elliptic cubic ([color elliptic curve](#prop:color-elliptic)) each satisfy the cubic in the color tube coordinate $\mathbf{c} \in \{\mathbf{r}_z, \mathbf{g}_z, \mathbf{b}_z\}$, obtained by substituting $X = \mathbf{c} + z$ into the color elliptic equation. Expanding this yields the *color tube cubic*:

```tex
\begin{equation}\label{eq:color-tube-cubic}
  \mathbf{c}^3 + (4z+1)\mathbf{c}^2 + (6z^2+3z+1)\mathbf{c}
  + (4z^3+3z^2+2z+1) =  0.
\end{equation}
```

This polynomial lies in $\mathbb{Z}[z][\mathbf{c}]$ and defines a variety over $\mathbb{Z}$. The leading $z$-coefficients $4, 6, 4$ equal $\binom{4}{1}$, $\binom{4}{2}$, $\binom{4}{3}$. The constant term satisfies

$$
  4z^3 + 3z^2 + 2z + 1 =  \frac{d}{dz}(z^4 + z^3 + z^2 + z).
$$

Vieta's formulas for the three roots give:

```tex
\begin{align}
  \mathbf{r}_z + \mathbf{g}_z + \mathbf{b}_z
    &=  -(4z+1),
    \label{eq:vieta-sum}\\[4pt]
  \mathbf{r}_z\mathbf{g}_z + \mathbf{r}_z\mathbf{b}_z
    + \mathbf{g}_z\mathbf{b}_z
    &=  6z^2+3z+1,
    \label{eq:vieta-pairs}\\[4pt]
  \mathbf{r}_z\mathbf{g}_z\mathbf{b}_z
    &=  -(4z^3+3z^2+2z+1).
    \label{eq:vieta-product}
\end{align}
```
<!-- FILE_END: color-tube-cubic.md -->

<!-- FILE_START: color-tube-fibers.md -->
Let $z \in \mathbb{P}^1(\mathbb{C})$. The **color tube** at $z$ is the affine curve defined over $\mathbb{Z}[z]$ by the color tube cubic. We denote it $R_z$, $G_z$, or $B_z$ according to which color tube coordinate $\mathbf{r}_z$, $\mathbf{g}_z$, or $\mathbf{b}_z$ is used:

```tex
\begin{equation}\label{eq:color-tube-fiber-def}
  R_z  := 
  \bigl\{\mathbf{r}_z \in \mathbb{A}^1 :
    \mathbf{r}_z^{3} + (4z+1)\mathbf{r}_z^{2}
    + (6z^2+3z+1)\mathbf{r}_z
    + (4z^3+3z^2+2z+1) = 0\bigr\}.
\end{equation}
```

The curves $G_z$ and $B_z$ are defined by the same equation with coordinates $\mathbf{g}_z$ and $\mathbf{b}_z$, respectively. The coordinates relate to the Lagrange resolvents by

$$
  \mathbf{r}_z = w_2 - z, \qquad \mathbf{g}_z = w_3 - z, \qquad
  \mathbf{b}_z = w_4 - z.
$$

As varieties, $R_z \cong G_z \cong B_z$ is isomorphic to the color elliptic fiber $\mathcal{E}_z$ of [color elliptic curve](#prop:color-elliptic) via the shift $X = \mathbf{c} + z$.
<!-- FILE_END: color-tube-fibers.md -->

<!-- FILE_START: t-duality-color-tube.md -->
The T-duality involution $\iota \colon (X, z) \mapsto (z, X)$ ([T-duality on elliptic fibres](#rem:t-duality-elliptic)) acts on color tube coordinates as follows. Writing $c = X - z$, the dual point has base coordinate $z' = X = c + z$ and color coordinate $X' = z$, yielding the dual color tube coordinate $c' = z - X = -c$. Hence

```tex
\begin{equation}\label{eq:t-duality-color-tube}
  \iota \colon (c, z)  \longmapsto  (-c, c + z).
\end{equation}
```

The symmetry $F(X,z) = F(z,X)$ ([T-duality on elliptic fibres](#rem:t-duality-elliptic)) translates to covariance of the color tube cubic. The involution $\iota$ carries the cubic at parameter $z$ with root $c$ to the cubic at parameter $c + z$ with root $-c$. We verify this directly from $F(c+z, z) = F(z, c+z)$, as $F(z, c+z)$ is the color tube cubic at parameter $c+z$ evaluated at $-c$.
<!-- FILE_END: t-duality-color-tube.md -->

<!-- FILE_START: color-tube-subloci.md -->
**Vanishing of the intrinsic color cubic.**
If $h_3(c) = 0$, the reduced cubic factors as

```tex
\begin{equation}\label{eq:reduced-cubic-factored}
  z\bigl(p_1(c)^2 + 5zp_1(c) + 8z^2\bigr) =  0.
\end{equation}
```

Either $z = 0$ (the spacetime origin), or $p_1(c)$ satisfies the quadratic $p_1(c)^2 + 5zp_1(c) + 8z^2 = 0$. The discriminant of this quadratic (in $p_1(c)$) is $25z^2 - 32z^2 = -7z^2$, which is negative for real $z \ne 0$. Over $\mathbb{C}$, the two solutions are

$$
  p_1(c) =  z\frac{-5 \pm \sqrt{-7}}{2}.
$$

These are non-real for $z \ne 0$. The locus $h_3(c) = 0$ meets the real locus only at $z = 0$. Over $\mathbb{F}_\mathfrak{p}$, the existence of a solution depends on whether $-7$ is a quadratic residue mod $\mathfrak{p}$.
<!-- FILE_END: color-tube-subloci.md -->

<!-- FILE_START: pure-colour-sublocus.md -->
**Pure colour sublocus.**
The pure colour term $b(br + g^2)$ vanishes on

$$
  \{b = 0\} \cup \{br + g^2 = 0\}.
$$

The condition $b = 0$ means $w_4 = z$. The fourth resolvent coincides with the spacetime ratio, collapsing one color degree of freedom onto the base. The condition $br + g^2 = 0$, or $(w_4 - z)(w_2 - z) + (w_3 - z)^2 = 0$, is a quadratic relation among the color resolvents and $z$. Either condition constitutes a *colour-confinement* constraint. One color mode freezes in register with the spacetime coordinate, and the remaining two couple by a Hermitian-quadric relation in the shifted frame.
<!-- FILE_END: pure-colour-sublocus.md -->

