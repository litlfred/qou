The infinite geometric torsion $T$ and the six topological defects on the
$\mathbb{P}^1(\mathbb{C})$ base $z=x_0/x_1$ are strictly artefacts of
dimensional projection. The total space, when lifted into the
complete coordinate framework, is a globally smooth complex manifold.

**1. The blow-up and the exceptional divisor.**
Near a spacetime defect $z_c$ where chiral sheets (e.g. $x_2$ and
$x_3$) merge, the singularity is resolved by blowing up the point into
an exceptional divisor parameterised by the local coordinate
$\delta=x_2-x_3$. The local geometry satisfies

$$
  z-z_c \sim \delta^2,
$$

proving that the spacetime base "bounces" at the defect: the chiral
coordinate continuously glides through the exceptional divisor and
transitions between sheets without encountering a singularity
(cf. [Bring's surface smoothness](#rem:brings-smoothness)).

In the spectral domain, the Jacobian determinant of the DFT
([Lagrange resolvents](#rem:lagrange-resolvents)) is a constant
$\lvert\det(J)\rvert=1$, so the global volume form never collapses:

```tex
\begin{equation}\label{eq:spectral-volume-form}
  \Omega =  dw_1\wedge dw_2\wedge dw_3\wedge dw_4
  =  \det(J)dx_0\wedge\cdots\wedge dx_4\Big|_{w_0=0}.
\end{equation}
```

This is the *spectral volume constraint*: the top-degree analogue
of the categorical volume constraint
([quantum observable universe](#def:quantum-observable-universe), item (iii)). The categorical
constraint provides a non-degenerate pairing
$\epsilon \colon \Lambda^2 V \to \mathbf{1}$ on the rank-$2$ fundamental
object; the spectral volume constraint
extends this to the full chiral fibre, ensuring that the $4$-form $\Omega$
is everywhere non-degenerate. Both enforce $\det = 1$: the categorical
form forces $g_V \in \mathrm{SL}(V)$, while the spectral form forces
$\det(J) \in \mathrm{U}(1)$.

The link is made explicit by the symplectic form. On the categorical
side, the alternating pairing on $V \cong \mathbb{C}^2$ is
([volume from rigidity](#lem:volume-from-rigidity))

$$
  \epsilon(v \wedge w)
  =  v_1 w_2 - v_2 w_1,
  \qquad v, w \in V.
$$

On the Brings surface, the spectral coordinates split into conjugate
pairs $(w_1, w_4)$ and $(w_2, w_3)$ with
$\overline{w_k} = w_{5-k}$. The quadric
constraint is
$w_1 w_4 + w_2 w_3 = 0$,
which is the Plucker relation $\Lambda^2 V \hookrightarrow V \otimes V$. The induced symplectic $2$-form on the chiral fibre is

```tex
\begin{equation}\label{eq:chiral-symplectic-form}
  \omega_{\mathrm{ch}}
  =  dw_1 \wedge dw_4 + dw_2 \wedge dw_3,
\end{equation}
```

and $\Omega = \tfrac{1}{2}\omega_{\mathrm{ch}} \wedge \omega_{\mathrm{ch}}$, so the non-degeneracy of $\Omega$
(i.e. $\det(J) \neq 0$) is equivalent to the non-degeneracy of
$\omega_{\mathrm{ch}}$, which is exactly the fibre-functor image of the
categorical volume form $\epsilon$.

The geometric torsion $T$ is thereby localised not as a point
singularity but as a trapped, finite magnetic flux integrated over
the surface of the exceptional $\mathbb{P}^1(\mathbb{C})$ sphere.

**2. The Seiberg--Witten differential.**
With the singularities geometrically resolved, the dynamics of the chiral
space are completely parameterised by a meromorphic $1$-form embedded in
the cotangent bundle $T^{*}\mathbb{P}^1(\mathbb{C})$, the *Seiberg--Witten
differential*:

```tex
\begin{equation}\label{eq:seiberg-witten-differential}
  \lambda_{\mathrm{SW}} =  Xdz,
\end{equation}
```

where $X\in\{x_2,x_3,x_4\}$ is the internal momentum (Higgs-field
eigenvalue) defining the spectral curve
([color bundles](#rem:color-bundles)), and $z$ is the spacetime position.
The exact physical properties of the topological defects---specifically
the mass/energy spectrum generating the torsion---are rigorously
determined by integrating this differential along the fundamental
non-contractible loops ($A$ and $B$ cycles) of the resolved chiral
torus:

```tex
\begin{equation}\label{eq:seiberg-witten-periods}
  a =  \oint_{A}\lambda_{\mathrm{SW}},
  \qquad
  a_D =  \oint_{B}\lambda_{\mathrm{SW}}.
\end{equation}
```

By lifting the Bring's surface into the full spatial and spectral
coordinate spaces, the degenerate branch points resolve completely into
smooth exceptional divisors. The infinite local torsion is geometrically
captured as trapped flux, revealing that the discrete braid-group
($B_3$) holonomy ([holonomy of trefoil](#rem:holonomy-trefoil)) is the
continuous Kodaira monodromy of a globally smooth Seiberg--Witten gauge
theory.
