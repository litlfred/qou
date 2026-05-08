Let $\mathcal{H}_q$ be the $q$-shuffle Hopf algebra of a quantum observable
universe with coproduct $\Delta_q$, counit $\epsilon$, antipode $S_q$,
and $q$-Jackson derivative $D_q$.  A *grouplike* of $\mathcal{H}_q$ is an
element $g \in \mathcal{H}_q$ satisfying

$$
  \Delta_q(g) = g \otimes g,
  \qquad
  \epsilon(g) = 1.
$$

Grouplikes form a group $G(\mathcal{H}_q) \subseteq \mathcal{H}_q$ under multiplication:
they are the characters of the coalgebra structure.

**$q$-Exponential.**  The *$q$-exponential* is the unique grouplike
$\exp_q \in G(\mathcal{H}_q)$ satisfying the categorical flow equation

$$
  D_q  \exp_q  =  \exp_q,
  \qquad
  \exp_q(0) = 1.
$$

Equivalently, $\exp_q$ is the unique element of $\mathcal{H}_q$ with
$\mathcal{L}_q^{-1}[(1 - s)_q^{-1}] = \exp_q$, where $\mathcal{L}_q$ is
the categorical Laplace transform
([categorical Laplace transform](#def:categorical-laplace)).

**Universal property.**  $\exp_q$ is the *free grouplike* on one
primitive generator $x$ (the infinitesimal of the Reeb flow
$\phi_t^q$).  Any monoidal functor
$\Phi \colon (\mathrm{End}_{\mathbf{C}}(A), \ast_q) \to (\mathrm{End}_{\mathbf{C}}(A), \cdot)$
that intertwines convolution with product is determined by its value
$\Phi(x)$; the diagonal $\Phi(\exp_q) = \Phi(x) \otimes \Phi(x)$ enforces
grouplike-ness functorially.

```tex
\begin{equation}\label{eq:q-exp-universal}
\begin{tikzcd}[row sep=2.5em, column sep=3.5em]
  x
    \ar[r, "D_q"]
    \ar[d, dashed, "!\,\Phi"']
  & \exp_q
    \ar[r, "\Delta_q"]
    \ar[d, dashed, "!\,\Phi"]
  & \exp_q \otimes \exp_q
    \ar[d, dashed, "!\,\Phi \otimes \Phi"]
  \\
  \Phi(x)
    \ar[r, "D_q"']
  & \Phi(\exp_q)
    \ar[r, "\Delta_q"']
  & \Phi(\exp_q) \otimes \Phi(\exp_q)
\end{tikzcd}
\end{equation}
```

**Base-ring independence.**  Because this definition characterises
$\exp_q$ by a purely Hopf-algebraic universal property — *grouplike* +
*flow-invariant* — it makes sense in any base ring $R$ where $\mathcal{H}_q$
admits a grouplike.  In particular $\exp_q$ exists abstractly over
$\mathbb{F}_p$, $\mathbb{Q}_p$, and $\mathbb{Z}[q, q^{-1}]$ as an
element of the formal Hopf algebra, independently of any convergent
power-series representation
([finite-field obstruction for $\exp_q$](#rem:q-exp-finite-field-obstruction)).

**Native algebraic home: the Habiro ring.**  The Taylor coefficients
of $\exp_q$ are rational functions of $q$ whose denominators are
products of $[n]_q$ — i.e. cyclotomic factors. The partial sums are
therefore coherent modulo the Habiro ideal $((q;q)_m)$, and $\exp_q$
acts as a grouplike in the formal-power-series ring
$\widehat{\mathbb{Z}[q]}[\![x]\!]$ over the Habiro ring
([Habiro ring](#def:habiro-ring)). Evaluation at any root of unity
$\zeta_n$ is the cyclotomic-projection
$\widehat{\mathbb{Z}[q]} \to \mathbb{Z}[q]/\Phi_n(q)$ — purely
algebraic, no analytic continuation required.

**Archimedean realisation.**  Over $\mathbb{C}$ (or any field of
characteristic zero where the Jackson factorials $[n]_q!$ are
invertible), $\exp_q$ is represented by a convergent Taylor series
([Taylor series of $\exp_q$](#prop:q-exponential-taylor)).  This is an
*additional* fact about the $\mathbb{C}$-realisation of the abstract
grouplike — not its defining property.

**Physical meaning.**  $\exp_q$ is the *categorical generator of the
Reeb flow*: the unique Hopf-algebra element whose action on the
substrate coordinate $Z$ produces the $q$-deformed rotation
$\mathcal{L}_\xi Z = J\hbar_q Z$
([substrate radial coordinate](#prop:substrate-radial-coordinate)).
The Planck step $t_P(q) = q/(q-1)$ is one full $\exp_q$-orbit.
