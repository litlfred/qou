<!-- FILE_START: color-tube-coords-intro.md -->
The braid-group action on the resolvents leaves three
$S_5$-invariants that the previous section already named in
passing. We now make those invariants the working coordinate system.
Definition: Color tube coordinates introduces the variables
$c_r, c_g, c_b$ together with their aggregates, and Remark: Aggregate color quantities records the named combinations
($\hat c$, total charge, etc.) used throughout the chapter.
Remark: Constraint equations in color tube coordinates rewrites
the Bring quadric and cubic as identities among these aggregates,
which is what makes the change of coordinates useful.

Remark: Interpretation of the color tube is the structural payoff:
the three tubes correspond to the three color charges, and pure-color
loci correspond to confinement. Remark: $C_5$ action in color tube coordinates records the residual cyclic symmetry that
survives after the $S_5$ quotient, and Remark: Intrinsic color cubic: pairing structure extracts the pairing that the next section
on color fibration and elliptic curves treats as the defining datum
of the elliptic structure $\mathcal{E}_q$.

_(draft.)_
<!-- FILE_END: color-tube-coords-intro.md -->

<!-- FILE_START: color-tube-coordinates.md -->
Let $z = x_0/x_1 \in \mathbb{P}^1(\mathbb{C})$ be the spacetime ratio
([braid group action](#rem:braid-group-action)(i)) and let $w_k$,
$k \in \{0,\dots,4\}$, be the Lagrange resolvents of Bring's surface
([Lagrange resolvents](#rem:lagrange-resolvents)).  The **color tube coordinates**
are the shifted spectral coordinates

```tex
\begin{equation}\label{eq:color-tube-coords}
  c_r = w_2 - z, \quad c_g = w_3 - z, \quad c_b = w_4 - z,
\end{equation}
```

together with the space-like shift $\sigma = w_1 - z$.  The
*color vector* is $c = (c_r, c_g, c_b)$.
<!-- FILE_END: color-tube-coordinates.md -->

<!-- FILE_START: aggregate-color-quantities.md -->
Define the following $C_5$-equivariant quantities in color tube
coordinates, with $\zeta = e^{2\pi i/5}$:

```tex
\begin{align}
  p_1(c) &=  \sigma + c_r + c_g + c_b
    &&\text{(first power sum),}
    \label{eq:agg-p1}\\[4pt]
  h_2(c) &=  \sigma c_b + c_r c_g
    &&\text{(Hermitian quadric),}
    \label{eq:agg-h2}\\[4pt]
  \chi_\zeta(c) &=  \zeta^{-1}\sigma + \zeta^{-2}c_r + \zeta^{-3}c_g + \zeta^{-4}c_b
    &&\text{($C_5$ character),}
    \label{eq:agg-chi}\\[4pt]
  h_3(c) &=  \sigma^2 c_g + c_b^2 c_r + c_r^2\sigma + c_g^2 c_b
    &&\text{(Hermitian cubic).}
    \label{eq:agg-h3}
\end{align}
```

The subscript on $h_k$ denotes the degree of the $C_5$-equivariant
invariant: $h_2$ pairs conjugate resolvents ($w_k$ with $w_{5-k}$)
and $h_3$ pairs squared resolvents in the skip-one pattern.  The
character $\chi_\zeta$ is the $\zeta$-weighted sum --- the Fourier
dual of $p_1$.

These are related to the unshifted resolvent invariants
$S = \sum_{k=1}^{4}w_k$ and $D = \sum_{k=1}^{4}\zeta^{-k}w_k$ by

```tex
\begin{equation}\label{eq:aggregate-shift}
  S =  p_1(c) + 4z, \qquad D =  \chi_\zeta(c) - z,
\end{equation}
```

where the second identity uses $\sum_{k=1}^{4}\zeta^{-k} = -1$.
The inverse Lagrange resolvent transform
([Lagrange resolvents](#rem:lagrange-resolvents)) gives

```tex
\begin{equation}\label{eq:z-from-SD}
  z =  \frac{x_0}{x_1} =  \frac{S}{D}.
\end{equation}
```
<!-- FILE_END: aggregate-color-quantities.md -->

<!-- FILE_START: color-tube-constraints.md -->
The Bring's surface constraints take the following form in color tube coordinates.

**Spacetime recovery.**
Substituting into $z = S/D$
(equation [$z = S/D$](#eq:z-from-SD)) yields $z(\chi_\zeta(c) - z) = p_1(c) + 4z$,
which rearranges to

```tex
\begin{equation}\label{eq:spacetime-recovery}
  z^2 - (\chi_\zeta(c) - 4)z + p_1(c) =  0.
\end{equation}
```

Thus the spacetime coordinate $z$ is determined implicitly by the
shifted data $(p_1(c), \chi_\zeta(c))$.

**Shifted quadric.**
Substituting $w_k = c_k + z$ into the quadric gives

```tex
\begin{equation}\label{eq:shifted-quadric}
  h_2(c) + zp_1(c) + 2z^2 =  0,
\end{equation}
```

or equivalently $\sigma b + rg = -z(\sigma + r + g + b) - 2z^2$.

**Shifted cubic.**
Substituting $w_k = c_k + z$ into the cubic gives

```tex
\begin{equation}\label{eq:shifted-cubic}
  h_3(c) + z(p_1(c)^2 - 2h_2(c))
  + 3z^2p_1(c) + 4z^3 =  0.
\end{equation}
```

Eliminating $h_2(c)$ via the shifted quadric yields the
*reduced cubic*:

```tex
\begin{equation}\label{eq:reduced-cubic}
  h_3(c) + zp_1(c)^2 + 5z^2p_1(c) + 8z^3 =  0.
\end{equation}
```

All three equations are polynomial over $\mathbb{Z}$ in $z, r, g, b, \sigma$;
they therefore define affine varieties over $\mathbb{Z}$ and descend
to $\mathbb{F}_\mathfrak{p}$ for every prime $\mathfrak{p} \ne 5$.

**Commutative-limit specialisation.**  Under the weight
identification of
[prop:x5-bring-weight-identification](#prop:x5-bring-weight-identification),
the weight-$(-1)$ Lagrange resolvent $w_1$ on Bring's surface
corresponds canonically to the affine coordinate $x$ on the
hyperelliptic quintic $\mathcal{X}_5 \colon y^2 = x^5 - 1$.
Restricting the full $S_5$-symmetric color-tube system above to
its cyclic $\mathbb{Z}_5 \subset S_5$ residue selects this single
weight channel: the three color coordinates $r, g, b$ and the
shift $z$ collapse to observables on the single $\mathrm{U}(1)$
phase tube of
[rem:u1-phase-tube](#rem:u1-phase-tube).  The shifted quadric
and cubic, evaluated along $w_2 = w_3 = w_4 = 0$, reduce to the
single-variable identity $x^5 - 1 = y^2$ that defines
$\mathcal{X}_5$.
<!-- FILE_END: color-tube-constraints.md -->

<!-- FILE_START: color-tube-interpretation.md -->
The terminology *color tube* reflects two features of the geometry.

**Color.**
The coordinates $r, g, b$ label the three color degrees of freedom
that correspond, via the $S_3$ subgroups of $S_5$
([braid group action](#rem:braid-group-action)(iii)), to the three
colour charges of quantum chromodynamics.  The color coordinates
$x_2, x_3, x_4$ of the QOU $4$-tuple
([Bring's QOU 4-tuple](#rem:brings-qou-4tuple)) descend to $c_r = w_2 - z$,
$c_g = w_3 - z$, $c_b = w_4 - z$ after shifting by the spacetime ratio $z$.

**Tube.**
For fixed $z \in \mathbb{P}^1(\mathbb{C})$, the color vector $c = (c_r, c_g, c_b)$
is constrained by the shifted quadric and
cubic to lie on a curve inside the
three-dimensional color space $\mathbb{A}^3$.  As $z$ varies over the
spacetime base, this curve sweeps out a tube --- the total space of
the color fibration over $\mathbb{P}^1(\mathbb{C})$.

**Space-like coordinate.**
The shift $\sigma = w_1 - z$ is distinguished: it measures the deviation
of the $C_5$-fundamental resolvent $w_1$ from the spacetime base,
anchoring the $U(1)$ longitudinal backbone
([spectral dynamics](#rem:spectral-dynamics)) in the shifted frame.
<!-- FILE_END: color-tube-interpretation.md -->

<!-- FILE_START: c5-color-tube.md -->
The cyclic symmetry $w_k \mapsto \zeta^{-k} w_k$
([Lagrange resolvents](#rem:lagrange-resolvents)) becomes, in color tube coordinates:

```tex
\begin{align}
  \sigma & \longmapsto  \zeta^{-1}\sigma + (\zeta^{-1}-1)z,
    \label{eq:c5-sigma}\\[4pt]
  r & \longmapsto  \zeta^{-2}r + (\zeta^{-2}-1)z,
    \label{eq:c5-r}\\[4pt]
  g & \longmapsto  \zeta^{-3}g + (\zeta^{-3}-1)z,
    \label{eq:c5-g}\\[4pt]
  b & \longmapsto  \zeta^{-4}b + (\zeta^{-4}-1)z.
    \label{eq:c5-b}
\end{align}
```

The $C_5$ action is no longer diagonal: each coordinate acquires an
additive correction proportional to $z$, reflecting the cost of
breaking projective homogeneity by subtracting the affine
quantity $z$ from each resolvent.
<!-- FILE_END: c5-color-tube.md -->

<!-- FILE_START: intrinsic-color-cubic-pairing.md -->
The intrinsic color cubic $h_3(c)$ admits a natural decomposition into space-like and color sectors:

```tex
\begin{equation}\label{eq:color-cubic-decomp}
  h_3(c)
  = 
  \underbrace{\sigma(\sigma g + r^2)}_{\text{space--colour coupling}}
  + 
  \underbrace{b(br + g^2)}_{\text{pure colour}}.
\end{equation}
```

The four terms pair the resolvent indices as $(1,3)$, $(2,1)$, $(4,2)$,
$(3,4)$: each index is squared and contracted with the index two steps
ahead in the cyclic order $1 \to 3 \to 4 \to 2 \to 1$.  This
skip-one pairing respects the conjugation $w_k \leftrightarrow w_{5-k}$
that pairs $(w_1, w_4)$ and $(w_2, w_3)$.
<!-- FILE_END: intrinsic-color-cubic-pairing.md -->

