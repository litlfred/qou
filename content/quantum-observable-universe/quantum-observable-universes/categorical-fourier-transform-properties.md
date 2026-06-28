This remark collects the reconstruction, Wick-rotation, $q$-heat,
abelian-instance, and base-ring realisations of the
[categorical Fourier transform](#def\:categorical-fourier).

**Tannakian reconstruction.**  When $G = \mathrm{SU}_q(2)$ and
$\mathbf{C} = \mathbf{Rep}(\mathrm{SU}_q(2))$, the Tannaka--Krein
reconstruction ([Tannaka--Krein reconstruction](#prop\:tannaka-krein-reconstruction))
identifies $\mathcal{F}$ with the *Peter--Weyl decomposition*:

$$
  \mathcal{F}\colon L^2(G, \mathrm{Haar}_q)
  \;\xrightarrow{\;\sim\;}\;
  \bigoplus_{j \in \widehat{G}} V_j \otimes V_j^\vee,
  \qquad
  f \mapsto \bigl(\pi_j(f)\bigr)_{j \in \widehat{G}}.
$$

The Fourier coefficients $\pi_j(f)$ are the matrix elements of $f$ in
the irreducible representation $V_j$, and the monoidal property
$\mathcal{F}[f \ast_q g] = \mathcal{F}[f] \cdot \mathcal{F}[g]$ becomes
the statement that convolution of class functions diagonalises over
irreducible characters.

```tex
\begin{equation}\label{eq:categorical-fourier-peter-weyl}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \mathcal{H}_q
    \ar[r, "\mathcal{F}"]
    \ar[d, "\ast_q"']
  & \displaystyle\bigoplus_{j} V_j \otimes V_j^\vee
    \ar[d, "{\otimes_j\,\pi_j}"]
  \\
  \mathcal{H}_q
    \ar[r, "\mathcal{F}"']
  & \displaystyle\bigoplus_{j} V_j \otimes V_j^\vee
\end{tikzcd}
\end{equation}
```

**Wick rotation.**  Because $\exp_q(-s\cdot)$ and $\exp_q(i\xi\cdot)$ are
the *same* abstract grouplike evaluated at real versus imaginary
spectral parameter, Laplace and Fourier are related by
$s = i\xi$:

$$
  \mathcal{F}[f](\xi) \;=\; \mathcal{L}[f](i\xi).
$$

This is the categorical version of **Wick rotation** — the heat
equation (Laplace side) and the Schrödinger equation (Fourier side)
are the two real forms of a single complex spectral equation, differing
only in which character of the Reeb-translation object one pairs
against.

**Role in the $q$-heat story.**  Applying $\mathcal{F}$ to both sides
of the $q$-heat equation $\partial_t u = -\Delta_q u$ diagonalises the
$q$-Laplacian on each Peter--Weyl summand:

$$
  \partial_t \pi_j(u) \;=\; -\lambda_j(q) \cdot \pi_j(u),
  \qquad
  \pi_j(u)(t) \;=\; e^{-\lambda_j(q)t}  \pi_j(u_0),
$$

where $\lambda_j(q) = [j]_q[j+1]_q (1 - q^{-1})^2$ is the eigenvalue
of $\Delta_\xi$ on the $j$-th irrep (plus the classical $q^{-2}\Delta$
eigenvalue on the base).  Reassembling over irreducibles gives the
**Peter--Weyl heat kernel**, which is the archimedean realisation of
the inverse Fourier of the resolvent.

**Abelian instance: the Bring's-surface DFT.**  When
$G = C_5$ (cyclic of order $5$) and $q = 1$, the quantum-group
Fourier transform degenerates to the **classical discrete Fourier
transform** on $\mathbb{Z}/5$.  The five irreducible characters
$\chi_k(j) = \zeta^{kj}$ (where $\zeta = e^{2\pi i/5}$) are the
grouplikes $\exp_1(2\pi i k \cdot / 5)$, and the Peter--Weyl
projection becomes

$$
  \mathcal{F}[x](k) \;=\; \sum_{j=0}^{4} \zeta^{kj}  x_j \;=\; w_k,
$$

the $k$-th Lagrange resolvent
([Lagrange resolvents](#rem\:lagrange-resolvents)).  The Briggs--Klein
chart ([Briggs--Klein chart](#def\:briggs-klein-chart)) on Bring's
surface ([smoothness of Bring's surface](#rem\:brings-smoothness))
is built from these DFT coordinates: even where two colour sheets
$x_i, x_j$ collide (branch points of the projection $\pi$), the
Fourier components $w_k$ remain pairwise distinct because they
live in *different* isotypic blocks.  Smoothness of the
Briggs--Klein chart is thus a direct consequence of the monoidal
property of $\mathcal{F}$: Fourier decomposition separates
spectral components, rendering the position-space collision
invisible on each summand.

**Base-ring independence.**  The Peter--Weyl decomposition of
$\mathbf{Rep}(\mathrm{SU}_q(2))$ as a direct sum of $V_j$'s is a
purely categorical statement — it holds whenever the category has a
set of simple objects indexed by $\widehat{G}$, regardless of base
ring.  The *integral* realisation of $\mathcal{F}$ as
$\int_G f(g) e^{i\xi g} dg$ requires a Haar measure (archimedean), but
the **algebraic** Fourier transform as Peter--Weyl projection works
over $\mathbb{F}_p$, $\mathbb{Q}_p$, and $\mathbb{Z}[q, q^{-1}]$.

**Three-context behaviour.**

* **$\mathbb{F}_p$.**  Peter--Weyl over $\mathbb{F}_p$ is valid
  whenever $p \nmid |\widehat{G}|$ and $p \nmid [n]_q!$ for small $n$
  (Maschke semisimplicity for quantum groups).  Under these conditions
  $\mathcal{F}$ is a *finite* Fourier transform — the Peter--Weyl
  matrix is invertible, and the heat-equation diagonalisation holds
  termwise.  The archimedean Gauss sum $\sum_j e^{i\xi j}$ becomes a
  character sum over $\mathbb{F}_p^\times$.
* **$\mathbb{Q}_p$.**  $\mathcal{F}$ sends locally constant $f$ to its
  $p$-adic Mellin transform, convergent on the same disc as
  $\exp_q(i\xi\cdot)$.  When $G = \mathrm{SU}_q(2)$ with
  $q \in 1 + p\mathbb{Z}_p$, the Peter--Weyl sum $\sum_j \pi_j(f)$
  converges in $\mathbb{Q}_p$ because the irrep dimensions $[2j+1]_q$
  have bounded $p$-adic valuation.
* **$\mathbb{C}_p$.**  Peter--Weyl holds identically; the Wick rotation
  $\mathcal{F}[f](\xi) = \mathcal{L}[f](i\xi)$ is a *formal* identity
  in $\mathbb{C}_p[\![\xi]\!]$ because both sides are now series in
  grouplike coefficients.  No analytic continuation is required — the
  categorical Fourier transform is an identity of Hopf-algebra mates.
