<!-- FILE_START: q-harmonic-analysis-intro.md -->
The previous section delivered the $q$-deformed
operators in coordinate form on $M$; we now build heat-flow,
Laplace, Fourier, and resolvent calculus on top of them. The
whole package is organised around the $q$-shuffle Hopf algebra
$\mathcal{H}_q$ and its grouplikes $\exp_q, \log_q,
\mathrm{Li}_2^q$ — purely Hopf-algebraic objects whose
archimedean Taylor representations are an additional fact about
the $\mathbb{C}$-realisation, not the defining property.

Definition: $q$-heat equation introduces $\partial_t u = -\Delta_q
u$ along the Reeb flow $\phi_t^q$ on a fixed substrate slice;
Proposition: existence of the $q$-heat equation and Proposition: uniqueness of the $q$-heat equation, with their proofs, fix the
construction. Substituting the three-term expansion of
$\Delta_q$ splits the right-hand side into classical diffusion,
Reeb-spin diffusion, and Coriolis cross-coupling.
Definition: Categorical Laplace transform defines $\mathcal{L}$ as
the monoidal functor pairing against the real grouplike
$\exp_q(-s \cdot) \in G(\mathcal{H}_q)$; existence and uniqueness
propositions (with proofs) follow. Definition: Categorical Fourier transform, with its existence and uniqueness blocks,
pairs against the imaginary-spectral grouplike $\exp_q(i\xi
\cdot)$.

Definition: $q$-resolvent is $R_q(s) = (s +
\widehat{\Delta_q})^{-1}$, characterised as the Laplace
transform of the $q$-heat semigroup and diagonalised over
irreducibles by Peter--Weyl. Existence and uniqueness blocks
(with proofs) deliver $R_q$. Remark: Categorical Wick rotation: real forms of $\exp_q$ identifies $\mathcal{F}[f](\xi) =
\mathcal{L}[f](i\xi)$: the Laplace and Fourier transforms are
the two real slices of a single complex pairing against
$\exp_q$, and the $q$-heat and $q$-Schrödinger equations are
sibling dynamics under $t \mapsto it$. Definition: $q$-exponential, with its existence and uniqueness blocks, is the unique
grouplike of $\mathcal{H}_q$ satisfying $D_q \exp_q = \exp_q$.

Remark: Finite-field obstruction to the $\exp_q$ Taylor series
records that the Hopf-algebraic content of $\exp_q$ survives in
characteristic $p$ even when the Jackson factorials $[n]_q!$
vanish, with the truncated $\exp_q^{(p)}$ and the Witt-vector
lift to $\mathbb{Q}_p, \mathbb{C}_p$ as substitutes;
Remark: $p$-adic realisations gives the convergence radii.
Definition: $q$-logarithm, with its existence and uniqueness
propositions, is the unique primitive of $\mathcal{H}_q$
inverting $\exp_q$ — the Hopf-algebraic shadow of the Lie
exponential. Definition: $q$-dilogarithm, with its existence and
uniqueness propositions, is the unique level-$2$ primitive of
$\mathcal{H}_q$ normalised by the pentagon identity — the
potential whose derivative recovers the universal $R$-matrix. The next section, **Braiding
conventions**, returns to the algebraic origin of the
substrate parameter and pins down the orientation choices
behind $q$, $i$, and the ribbon twist.

_(draft.)_
<!-- FILE_END: q-harmonic-analysis-intro.md -->

<!-- FILE_START: q-heat-equation.md -->
Let $(\mathbf{C}, \varTheta, G, \mathcal{S})$ be a quantum observable
universe with $q$-Laplacian $\Delta_q = d_q\delta_q + \delta_qd_q$
([particle ($q$-harmonic form)](#def:q-harmonic-form)).  The
**$q$-heat equation** is the evolution equation

$$
  \partial_t u \;=\; -\Delta_q u
$$

for a time-dependent section
$u \colon \mathbb{R}_{\ge 0} \times \mathcal{S} \to \mathbf{1}_{\mathbf{C}}$,
where $t$ is the **Reeb-flow parameter** — the affine coordinate of
$\phi_t^q$ on a fixed substrate slice, in units of the Planck step
$t_P(q) = q/(q - 1)$.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: q-heat-equation.md -->

<!-- FILE_START: q-heat-equation-elaboration.md -->
**Two times.**  The Reeb time $t$ must be distinguished from the
substrate parameter $q$, which plays the role of cosmological time
(Big Bang $q \to \infty$ to heat death $q \to 1$).  The $q$-heat
equation ([$q$-heat equation](#def:q-heat-equation)) lives at *fixed*
$q$ and evolves in $t$ along the Reeb flow — it is the dissipative
shadow of the Reeb endofunctor on $\mathbf{Rep}(\mathrm{SU}_q(2))$.

**Categorical formulation.**  The left-hand side $\partial_t$ is
the infinitesimal generator of the Reeb translation
$\phi_t^q \colon \mathcal{S} \to \mathcal{S}$, regarded as an
endomorphism of the identity functor on the slice category
$\mathbf{C}|_{\mathcal{S}}$.  The right-hand side $\Delta_q$ is the
$q$-deformed Hodge Laplacian
([three-term expansion of the $q$-Laplacian](#rem:q-laplacian-expansion)).
The $q$-heat equation asserts the equality of these two
endomorphisms on $u$, which is a purely categorical condition — no
choice of base field is required.

```tex
\begin{equation}\label{eq:q-heat-commutative}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \mathcal{S}
    \ar[r, "u(t)"]
    \ar[d, "\phi_\epsilon^q"']
  & \mathbf{1}_{\mathbf{C}}
    \ar[d, "\mathrm{id} - \epsilon\Delta_q"]
  \\
  \mathcal{S}
    \ar[r, "u(t + \epsilon)"']
  & \mathbf{1}_{\mathbf{C}}
\end{tikzcd}
\end{equation}
```

**Decomposition.**  Substituting the three-term expansion
([$q$-Laplacian expansion](#rem:q-laplacian-expansion)) gives

$$
  \partial_t u  =  -q^{-2}\Delta u
  - q^{-1}(1 - q^{-1})[\text{Coriolis}]u
  - (1 - q^{-1})^2\Delta_\xi u.
$$

The three terms correspond to:

1. **Classical diffusion** ($q^{-2}\Delta$): heat spreads across the
   base manifold.
2. **Reeb-spin diffusion** ($\Delta_\xi$): heat spreads along the
   internal Reeb fibre (the $\mathrm{SU}_q(2)$ direction).
3. **Coriolis cross-coupling**: interference between base-motion and
   Reeb-rotation.

At $q = 1$ only the classical term survives and one recovers the
ordinary heat equation $\partial_t u = \nabla^2 u$ (since
$-\Delta = \nabla^2$ on $0$-forms in the Hodge convention).  As
$q \to \infty$
the classical term is suppressed and diffusion is dominated by pure
Reeb-spin dynamics.

**Base-ring independence.**  Because $\Delta_q$ is a polynomial
operator in $q, q^{-1}$
([base-field independence](#rem:base-field-independence)), the
$q$-heat equation makes sense over any commutative ring in which
$q - 1$ is invertible — including $\mathbb{F}_p$ and $\mathbb{Q}_p$
(after specialising $q$ to a unit $\ne 1$), and the universal ring
$\mathbb{Z}[q, q^{-1}, (q - 1)^{-1}]$.  Convergent series
representations of its solutions (heat kernel, $q$-Gaussian) are
archimedean phenomena and require $\mathrm{char} = 0$.
<!-- FILE_END: q-heat-equation-elaboration.md -->

<!-- FILE_START: q-heat-equation-exists.md -->
Let $(\mathbf{C}, \varTheta, G, \mathcal{S})$ be a
[quantum observable universe](#def:quantum-observable-universe) with
$q$-Laplacian $\Delta_q$ and initial data $u_0 \colon \mathcal{S} \to \mathbf{1}_{\mathbf{C}}$.
Then there exists a formal solution $u(t)$ of the
[$q$-heat equation](#def:q-heat-equation)
$\partial_t u = -\Delta_q u$ with $u(0) = u_0$.
<!-- FILE_END: q-heat-equation-exists.md -->

<!-- FILE_START: q-heat-equation-unique.md -->
Given initial data $u_0$, the solution $u(t)$ of the
[$q$-heat equation](#def:q-heat-equation) is uniquely determined as
the $\exp(-t \Delta_q) u_0$ semigroup orbit.  Two solutions
$u_1, u_2$ with $u_i(0) = u_0$ coincide for every $t$.
<!-- FILE_END: q-heat-equation-unique.md -->

<!-- FILE_START: categorical-laplace-transform.md -->
Fix a quantum observable universe $(\mathbf{C}, \varTheta, G, \mathcal{S})$
with Markov trace
$\mathrm{tr}_M \colon \mathrm{End}_{\mathbf{C}}(A) \to \mathbf{1}_{\mathbf{C}}$
([adjoint trace](#rem:adjoint-trace)).  Let $\mathcal{H}_q$ be the convolution
Hopf algebra of $\mathrm{End}_{\mathbf{C}}(A)$ under the
$q$-deformed convolution $\ast_q$.

**Categorical Laplace transform.**  The **categorical Laplace transform**
is the *:refterm[monoidal functor]{#monoidal-functor}*

$$
  \mathcal{L}\colon \bigl(\mathrm{End}_{\mathbf{C}}(A), \ast_q\bigr)
  \;\longrightarrow\;
  \bigl(\mathrm{End}_{\mathbf{C}}(A), \cdot\bigr)
$$

defined, for each spectral parameter $s \in \mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, A)$,
by the Hopf pairing against the real exponential grouplike
$\exp_q(-s\cdot) \in G(\mathcal{H}_q)$:

$$
  \mathcal{L}[f](s)
  \;=\;
  \mathrm{tr}_M\bigl(\exp_q(-s\cdot)  \cdot  f\bigr)
  \;=\;
  \bigl\langle \exp_q(-s\cdot),  f\bigr\rangle_{\mathrm{tr}_M}.
$$

No integral sign appears: the pairing is the Frobenius pairing
supplied by the rigid monoidal structure
([fibre-functor rigidity](#rem:fibre-functor-rigidity)).

**Defining property (monoidality).**  $\mathcal{L}$ intertwines
$q$-convolution with pointwise product,

$$
  \mathcal{L}[f \ast_q g]  =  \mathcal{L}[f] \cdot \mathcal{L}[g],
  \qquad
  \mathcal{L}[\mathbf{1}_{\ast_q}]  =  \mathbf{1}_{\cdot},
$$

and this property characterises $\mathcal{L}$ up to isomorphism — it
is the *mate* of the comultiplication $\Delta_q$ on $\mathcal{H}_q$.

```tex
\begin{equation}\label{eq:categorical-laplace-square}
\begin{tikzcd}[row sep=2.5em, column sep=4em]
  \mathcal{H}_q \otimes \mathcal{H}_q
    \ar[r, "\ast_q"]
    \ar[d, "\mathcal{L} \otimes \mathcal{L}"']
  & \mathcal{H}_q
    \ar[d, "\mathcal{L}"]
  \\
  \mathcal{H}_q \otimes \mathcal{H}_q
    \ar[r, "\cdot"']
  & \mathcal{H}_q
\end{tikzcd}
\end{equation}
```
<!-- FILE_END: categorical-laplace-transform.md -->

<!-- FILE_START: categorical-laplace-transform-properties.md -->
Because $\exp_q(-s\cdot)$ is defined
abstractly as a grouplike of $\mathcal{H}_q$ — not as a convergent series —
$\mathcal{L}$ makes sense over any base ring $R$ where $\mathcal{H}_q$ has the
grouplike, i.e. anywhere $q \ne 1$ and $s$ is algebraic.  The familiar
integral

$$
  \mathcal{L}[f](s) \;=\; \int_0^\infty e^{-st} f(t)  dt
  \qquad (\mathbb{R}\text{-realisation})
$$

is recovered by evaluating the abstract pairing against the
archimedean realisation of the grouplike ($q \to 1$, $R = \mathbb{C}$,
Haar measure on $\mathbb{R}_{\ge 0}$).  Over $\mathbb{F}_p$ or
$\mathbb{Q}_p$ the integral is replaced by a sum over Frobenius
orbits, but $\mathcal{L}$ itself is unchanged.
<!-- FILE_END: categorical-laplace-transform-properties.md -->

<!-- FILE_START: categorical-laplace-three-contexts.md -->
Paralleling $\exp_q$
([finite-field obstruction](#rem:q-exp-finite-field-obstruction),
[$p$-adic $\exp_q$](#rem:q-exp-p-adic)):

* **$\mathbb{F}_p$.**  $\mathcal{L}$ becomes a finite sum over the
  grouplike spectrum $\mathrm{Spec}_{\mathbb{F}_p}(G(\mathcal{H}_q))$, which is
  finite because $G(\mathcal{H}_q) \otimes \mathbb{F}_p$ is an étale group scheme
  of bounded rank.  This is the Gauss-sum avatar: pairing against
  $\exp_q^{(p)}$ over a finite base gives a finite character sum, and
  monoidality of $\mathcal{L}$ is the product formula for Gauss sums.
* **$\mathbb{Q}_p$.**  $\mathcal{L}$ is a continuous functional on
  locally constant $f \colon p\mathbb{Z}_p \to \mathbb{Q}_p$, computed
  as a $p$-adic integral against the Witt-lifted $\exp_q$.  The monoidal
  property $\mathcal{L}[f \ast_q g] = \mathcal{L}[f] \cdot \mathcal{L}[g]$
  is Amice--Velu theory: the Mellin transform of a $p$-adic measure.
* **$\mathbb{C}_p$.**  $\mathcal{L}$ extends to rigid-analytic $f$ on
  the open disc $v_p(x) > 1/(p-1)$; beyond this disc the pairing is
  purely formal, $\mathcal{L}[f](s) \in \mathbb{C}_p[\![s]\!]$ with no
  evaluation at concrete $s$.  This is the categorical $p$-adic
  Laplace transform.
<!-- FILE_END: categorical-laplace-three-contexts.md -->

<!-- FILE_START: categorical-laplace-q-heat-resolvent.md -->
The $q$-heat equation
([$q$-heat equation](#def:q-heat-equation)) $\partial_t u = -\Delta_q u$
is turned by $\mathcal{L}$ into a spectral equation: differentiation
in $t$ maps to multiplication by $s$ (plus initial data), so

$$
  s  \hat{u}(s) - u_0
  \;=\;
  -\widehat{\Delta_q}  \hat{u}(s),
$$

yielding the *resolvent of the $q$-Laplacian*,
$\hat{u}(s) = (s + \widehat{\Delta_q})^{-1} u_0$
([$q$-resolvent](#def:q-resolvent)).  The heat kernel is
the inverse Laplace of the resolvent, and lives in the archimedean
realisation.
<!-- FILE_END: categorical-laplace-q-heat-resolvent.md -->

<!-- FILE_START: categorical-laplace-transform-exists.md -->
Under the hypotheses of
([existence of $\exp_q$](#prop:q-exponential-exists)), the monoidal
functor

$$
  \mathcal{L} \colon (\mathrm{End}_{\mathbf{C}}(A), \ast_q)
  \longrightarrow (\mathrm{End}_{\mathbf{C}}(A), \cdot)
$$

defined by the
[categorical Laplace transform](#def:categorical-laplace) exists.

Uniqueness is
([uniqueness of categorical Laplace transform](#prop:categorical-laplace-unique)).


**Strategy.** The transform $\mathcal{L}[f](s)$ is constructed using the Markov trace applied to the composite of the assumed $q$-exponential generator and $f$. The functoriality and intertwining properties descend from the coproduct axioms on the $q$-exponential.
<!-- FILE_END: categorical-laplace-transform-exists.md -->

<!-- FILE_START: categorical-laplace-transform-unique.md -->
The [categorical Laplace transform](#def:categorical-laplace) is the
unique :refterm[monoidal functor]{#monoidal-functor}
$(\mathrm{End}_{\mathbf{C}}(A), \ast_q) \to (\mathrm{End}_{\mathbf{C}}(A), \cdot)$
intertwining convolution with product.  It is characterised as the
*mate* of the coproduct $\Delta_q$ on $\mathcal{H}_q$ under the
Frobenius pairing.


**Strategy.** The uniqueness argument follows directly from the uniqueness of the $q$-exponential generator. Any two monoidal functors with the given intertwining property are determined entirely by their evaluation on $\exp_q(-s\cdot)$. By matching these evaluations, we deduce they are isomorphic as Frobenius mates.
<!-- FILE_END: categorical-laplace-transform-unique.md -->

<!-- FILE_START: categorical-fourier-transform.md -->
The Laplace transform ([categorical Laplace transform](#def:categorical-laplace))
pairs against the *real* exponential grouplike $\exp_q(-s\cdot)$.  Its
companion pairs against the *unitary* grouplike $\exp_q(i\xi\cdot)$ — a
second grouplike of the same Hopf algebra $\mathcal{H}_q$, distinguished only by
the sign of the spectral parameter.

**Categorical Fourier transform.**  The **categorical Fourier transform**
is the :refterm[monoidal functor]{#monoidal-functor}

$$
  \mathcal{F}\colon \bigl(\mathrm{End}_{\mathbf{C}}(A), \ast_q\bigr)
  \;\longrightarrow\;
  \bigl(\mathrm{End}_{\mathbf{C}}(A), \cdot\bigr),
  \qquad
  \mathcal{F}[f](\xi) \;=\; \mathrm{tr}_M\bigl(\exp_q(i\xi\cdot)  \cdot  f\bigr),
$$

where $\xi$ ranges over the categorical spectrum
$\mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, A^\vee)$ — the Pontryagin dual
of the Reeb-translation object.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: categorical-fourier-transform.md -->

<!-- FILE_START: categorical-fourier-transform-properties.md -->
This remark collects the reconstruction, Wick-rotation, $q$-heat,
and base-ring realisations of the
[categorical Fourier transform](#def:categorical-fourier).

**Tannakian reconstruction.**  When $G = \mathrm{SU}_q(2)$ and
$\mathbf{C} = \mathbf{Rep}(\mathrm{SU}_q(2))$, the Tannaka--Krein
reconstruction ([Tannaka--Krein reconstruction](#prop:tannaka-krein-reconstruction))
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

**Wick rotation.**  Laplace and Fourier are related by $s = i\xi$, the
categorical version of **Wick rotation**; see
[Laplace--Fourier Wick rotation](#rem:laplace-fourier-wick-rotation).

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
<!-- FILE_END: categorical-fourier-transform-properties.md -->

<!-- FILE_START: categorical-fourier-brings-dft.md -->
When
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
([Lagrange resolvents](#rem:lagrange-resolvents)).  The Briggs--Klein
chart ([Briggs--Klein chart](#def:briggs-klein-chart)) on Bring's
surface ([smoothness of Bring's surface](#rem:brings-smoothness))
is built from these DFT coordinates: even where two colour sheets
$x_i, x_j$ collide (branch points of the projection $\pi$), the
Fourier components $w_k$ remain pairwise distinct because they
live in *different* isotypic blocks.  Smoothness of the
Briggs--Klein chart is thus a direct consequence of the monoidal
property of $\mathcal{F}$: Fourier decomposition separates
spectral components, rendering the position-space collision
invisible on each summand.
<!-- FILE_END: categorical-fourier-brings-dft.md -->

<!-- FILE_START: categorical-fourier-transform-exists.md -->
Under the hypotheses of
([existence of $\exp_q$](#prop:q-exponential-exists)), the monoidal
functor

$$
  \mathcal{F} \colon (\mathrm{End}_{\mathbf{C}}(A), \ast_q)
  \longrightarrow (\mathrm{End}_{\mathbf{C}}(A), \cdot),
  \qquad
  \mathcal{F}[f](\xi) = \mathrm{tr}_M(\exp_q(i\xi\cdot) \cdot f)
$$

defined by the
[categorical Fourier transform](#def:categorical-fourier) exists.

Uniqueness is
([uniqueness of categorical Fourier transform](#prop:categorical-fourier-unique)).
<!-- FILE_END: categorical-fourier-transform-exists.md -->

<!-- FILE_START: categorical-fourier-transform-unique.md -->
The [categorical Fourier transform](#def:categorical-fourier) is the
unique :refterm[monoidal functor]{#monoidal-functor} agreeing with $\mathcal{L}[f](-i\xi)$ (Wick
rotation of the Laplace transform).  In the Tannakian setting with
$G = \mathrm{SU}_q(2)$, it coincides with the Peter--Weyl
decomposition, which is itself unique up to the choice of
irreducible labelling.
<!-- FILE_END: categorical-fourier-transform-unique.md -->

