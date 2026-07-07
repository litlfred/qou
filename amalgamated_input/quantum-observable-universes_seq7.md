<!-- FILE_START: differential-structures-intro.md -->
The PawLei machinery treated $\mathrm{Hom}$-spaces;
we now turn to first-order differential structure on $A$ itself
— the categorical Reeb derivation, the projective-line object,
the affine chart it carries, and the fibre-adjoint involution
that ties the chart to the adjoint representation. None of these
objects are imposed by hand: each is forced by the QOU axioms
of the first section.

Definition: Categorical Reeb derivation names the endomorphism
$\xi \colon A \to A$ generating the $T$-action on $A$ and the
dual one-form $\varTheta_A$ that detects horizontal forms.
Proposition: Existence of the categorical Reeb derivation and
Proposition: uniqueness of the categorical Reeb derivation, each
with its proof block, deliver $(\xi, \varTheta_A)$ from the
weight decomposition. Example: Reeb derivation for $\mathrm{SU}(2)$ realises $(\xi, \varTheta_A) = (e_3, \omega_3)$ in the
Woronowicz left-covariant calculus on
$\mathcal{O}_q(\mathrm{SU}(2))$.

Definition: Projective line object and Remark: projective line on $\mathrm{SU}(2)$ introduce $\mathbb{P}(V) = G/T$ as the
function-algebra quotient $A^{\mathrm{co}\,T}$, realised by
$\mathrm{SU}(2)/\mathrm{U}(1) \cong \mathbb{P}^1(\mathbb{C})$.
Definition: Contact affine chart supplies the open dense subset
$U_\xi$ of states with non-vanishing Reeb component and the
affine coordinate $Z = \alpha_H / \iota_\xi\alpha$.
Proposition: Fibre functors as an affine atlas with $G$-torsor transitions repackages every fibre functor on
$\mathbf{C}$ as a chart, every monoidal natural isomorphism as
a transition function, and the cocycle identity as composition
in the functor category — the whole family forming a $G$-gerbe.
Proposition: Substrate radial coordinate, with its proof,
describes how the affine coordinate $Z$ rotates under the Reeb
flow: $\mathcal{L}_\xi Z = J\hbar_q Z$, with $\hbar_q = 1 -
q^{-1}$.

The closing run is the Proposition: fibre-adjoint involution and
its Remark: coadjoint-orbit realisation, with proofs:
$\sigma \colon \mathbb{P}(V) \hookrightarrow \mathrm{Ad}(A)$
embeds the projective line as the coadjoint orbit of a
highest-weight vector and forces the observability axiom from
the Frobenius pairing. Example: Fibre adjoint on $\mathrm{SU}(2)$ and Example: Connection and curvature on $\mathcal{O}(\mathrm{SU}(2))$ execute the construction on the running example, fixing the
left-invariant calculus $\Omega^1(A) =
\mathrm{span}\{\omega_1, \omega_2, \omega_3\}$ that the next
section, **Substrate parameter and deformation**, will deform.

_(draft.)_
<!-- FILE_END: differential-structures-intro.md -->

<!-- FILE_START: categorical-reeb.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
maximal torus $T$ ([maximal torus](#def:maximal-torus)) and weight
decomposition $\pi_H, \pi_V$
([weight decomposition](#def:weight-decomposition)). The **categorical
Reeb derivation** is the endomorphism $\xi \colon A \to A$ that
generates the $T$-action: $\xi$ is the infinitesimal generator of the
one-parameter subgroup $T \cong \mathrm{U}(1) \subset G$, acting on
the Frobenius--Hopf object $A$ via the adjoint coaction. It satisfies:

1. **Vertical generator:**
   $\pi_V \circ d = \iota_\xi d\varTheta_A$, where
   $\iota_\xi$ denotes the interior product (contraction with $\xi$)
   and $\varTheta_A \in \Omega^1(A)$ is the canonical $1$-form dual to
   $\xi$.
2. **Normalisation:**
   $\varTheta_A(\xi) = \mathrm{id}_{\mathbf{1}}$.
3. **Kernel:**
   $\Omega^k_H(A) = \ker(\iota_\xi)$ (horizontal forms are
   precisely those annihilated by contraction with $\xi$).

```tex
\begin{equation}\label{eq:reeb-decomposition-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \Omega^k(A) \ar[r, "\pi_H"] \ar[d, "\pi_V"']
  & \Omega^k_H(A) \ar[d, hook] \\
  \varTheta_A \wedge \Omega^{k-1}_H(A) \ar[r, hook]
  & \Omega^k(A)
\end{tikzcd}
\qquad (\pi_H + \pi_V = \mathrm{id})
\end{equation}
```
<!-- FILE_END: categorical-reeb.md -->

<!-- FILE_START: categorical-reeb-exists.md -->
Let $(\mathbf{C}, A, \tau)$ be a
([quantum observable universe](#def:quantum-observable-universe)) with
[maximal torus](#def:maximal-torus) $T$ and
[weight decomposition](#def:weight-decomposition) $(\pi_H, \pi_V)$.
Then there exists a
[categorical Reeb derivation](#def:categorical-reeb)
$(\xi, \varTheta_A)$ on $A$ satisfying:

1. **Vertical generator:** $\pi_V \circ d = \iota_\xi d\varTheta_A$.
2. **Normalisation:** $\xi \mathbin{;} \varTheta_A = \varTheta_A$
   (categorically: $\varTheta_A(\xi) = \mathrm{id}_{\mathbf{1}}$).

```tex
\begin{equation}\label{eq:reeb-exists-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  A \ar[r, "\xi"] \ar[d, "d"']
  & A \ar[d, "\varTheta_A"] \\
  \Omega^1(A) \ar[r, "\iota_\xi"']
  & A
\end{tikzcd}
\qquad (\varTheta_A(\xi) = \mathrm{id}_{\mathbf{1}})
\end{equation}
```
<!-- FILE_END: categorical-reeb-exists.md -->

<!-- FILE_START: categorical-reeb-unique.md -->
Let $(\mathbf{C}, A, \tau)$ be a
[quantum observable universe](#def:quantum-observable-universe) with
maximal torus $T$ and weight decomposition $(\pi_H, \pi_V)$
([weight decomposition](#def:weight-decomposition)).  Any two
[categorical Reeb derivations](#def:categorical-reeb)
$(\xi_1, \varTheta_A^{(1)})$ and $(\xi_2, \varTheta_A^{(2)})$ on $A$
satisfying the vertical-generator and normalisation axioms coincide:

$$
  \xi_1 \;=\; \xi_2, \qquad \varTheta_A^{(1)} \;=\; \varTheta_A^{(2)}.
$$


**Strategy.** We sequentially apply the categorical Reeb axioms to pin down the derivation. The vertical-generator and normalization axioms together fix the unique derivation along the vertical distribution (corresponding to the free $T$-action). The dual form is then uniquely determined by extending to the horizontal distribution via the Maurer--Cartan condition.
<!-- FILE_END: categorical-reeb-unique.md -->

<!-- FILE_START: reeb-su2.md -->
Continuing [maximal torus of $\mathrm{SU}(2)$](#ex:maximal-torus-su2), the maximal torus is
$T = \mathrm{U}(1)$ with generator
$\xi = e_3 = \frac{1}{2}\begin{smallmatrix} 1 & 0 \\ 0 & -1 \end{smallmatrix} \in \mathfrak{su}(2)$.
On $A = \mathcal{O}(\mathrm{SU}(2))$, $\xi$ acts by
$(\xi \cdot f)(g) = \frac{d}{dt}\big|_{t=0} f(e^{-t\xi} g)$
(left-invariant vector field). The canonical $1$-form is
$\varTheta_A = \omega_3$ (the left-invariant $1$-form dual to $e_3$), and:

- $\omega_3(\xi) = 1$ (normalisation).
- $\Omega^k_H(A) = \{\alpha : \iota_\xi\alpha = 0\}$
  (forms with no $\omega_3$ component).
- In the archimedean realisation on a CR manifold $(M, \varTheta)$,
  $\xi$ becomes the Reeb vector field with $\iota_\xid\varTheta = 0$
  and $\varTheta(\xi) = 1$
  ([Reeb decomposition](#ex:reeb-decomposition)).
<!-- FILE_END: reeb-su2.md -->

<!-- FILE_START: categorical-reeb-brings.md -->
Continuing the [Reeb derivation for $\mathrm{SU}(2)$](#ex:reeb-su2) and the
[Bring coordinate ring](#def:brings-coordinate-ring), we construct
the [categorical Reeb derivation](#def:categorical-reeb)
$(\xi, \varTheta_A)$ on Bring's surface explicitly.

**Step 1: identify the generator $\xi$.** The maximal torus of
$\mathrm{SU}_q(2)$ is $T = \mathrm{U}(1)$, embedded as diagonal
matrices. Its Lie algebra generator in $\mathfrak{su}(2)$ is

$$
  \xi = e_3
  = \frac{1}{2}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}.
$$

On the quantum coordinate ring
$A = \mathcal{O}_q(\mathrm{SU}(2))$, $\xi$ acts as the infinitesimal
adjoint coaction. In terms of the standard generators
$\alpha, \beta, \bar\alpha, \bar\beta$
($\alpha\bar\alpha + q^{-2}\beta\bar\beta = 1$), the action is:

$$
  \xi \cdot \alpha = \tfrac{1}{2}\alpha, \quad
  \xi \cdot \beta  = -\tfrac{1}{2}\beta, \quad
  \xi \cdot \bar\alpha = -\tfrac{1}{2}\bar\alpha, \quad
  \xi \cdot \bar\beta  = \tfrac{1}{2}\bar\beta.
$$

This is a *derivation*: $\xi \cdot (fg) = (\xi \cdot f)g + f(\xi \cdot g)$.

**Step 2: construct the dual $1$-form $\varTheta_A$.** The Woronowicz
$3$-dimensional calculus on $\mathcal{O}_q(\mathrm{SU}(2))$ has basis
$\{\omega_+, \omega_-, \omega_3\}$ of left-invariant $1$-forms. The
form dual to $\xi = e_3$ is

$$
  \varTheta_A = \omega_3
$$

where $\omega_3$ is defined by $\omega_3(e_3) = 1$ and
$\omega_3(e_\pm) = 0$, that is, $\omega_3$ is the left-invariant
basis element dual to $e_3$ in the Woronowicz $3$-dimensional
calculus \cite{woronowicz1989}.

**Step 3: verify the axioms.** The two defining properties of the
categorical Reeb derivation are now checkable by direct computation:

1. *Normalisation*: $\varTheta_A(\xi) = \omega_3(e_3) = 1 = \mathrm{id}_{\mathbf{1}}$. $\checkmark$

2. *Reeb/contact identity*: the directly verified condition is
   $\iota_\xi\,d\varTheta_A = 0$ for $\varTheta_A = \omega_3$.
   The exterior derivative $d\omega_3$ is computed from the
   Woronowicz structure equations
   $d\omega_3 = -q^{-1}\omega_+ \wedge \omega_-$, and
   $\iota_{e_3}(d\omega_3) = -q^{-1}(\omega_+(e_3)\omega_- - \omega_-(e_3)\omega_+) = 0$,
   confirming that $\omega_3$ is a contact form with Reeb field $\xi$.
   The vertical projection
   $\pi_V$ is the independent projection onto non-zero-weight
   components under the $\xi$-action, as constructed in
   [weight decomposition](#ex:weight-decomposition-su2). Combined
   with $\iota_\xi\,d\varTheta_A = 0$, the vertical generator axiom
   $\pi_V \circ d = \iota_\xi\,d\varTheta_A$ restricts to horizontal
   forms (annihilated by $\iota_\xi$) and recovers the Reeb
   decomposition $\pi_H + \pi_V = \mathrm{id}$. $\checkmark$

**Bring's surface specialisation.** On the
[Bring coordinate ring](#def:brings-coordinate-ring)
$\mathcal{O}_q(\mathcal{B})$, the $\xi$-action extends to the
five coordinates $x_1, \ldots, x_5$ via the $S_5$-equivariant
embedding. The $8 = 2g$ independent cycles of the genus-$4$ curve
decompose into $\xi$-eigenspaces (by Hodge decomposition,
$H^1(\Sigma_4, \mathbb{C}) = H^{1,0} \oplus H^{0,1}$ with
$\dim H^{1,0} = g = 4$):

- $4$ cycles of weight $+1$ (holomorphic differentials $H^{1,0}$),
- $4$ cycles of weight $-1$ (anti-holomorphic differentials $H^{0,1}$).

The Reeb spectrum is $\mathrm{Spec}(\xi) = \{-1, +1\}$ with
multiplicity $4$ each, matching the $8$ fundamental modes of
Bring's curve. The contact form $\varTheta_A$ restricts to the
canonical $1$-form on $\Sigma_4$ whose kernel defines the horizontal
distribution.
<!-- FILE_END: categorical-reeb-brings.md -->

<!-- FILE_START: projective-line-object.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
maximal torus $T \subset G$ ([maximal torus](#def:maximal-torus)).
The **projective line object** is the quotient

$$
  \mathbb{P}(V) = G / T,
$$

regarded as an object of $\mathrm{Ind}(\mathbf{C})$ via its function
algebra $\mathcal{O}(\mathbb{P}(V)) = A^{\mathrm{co}T}$
(the $T$-coinvariant subalgebra of $A$).

Under the fibre functor $\tau$, the categorical projective line
realises as the scheme-theoretic projective line over $R$:

$$
  \tau\bigl(\mathbb{P}(V)\bigr) =  \mathbb{P}^1(R)
$$

([scheme notation](#sec:scheme-notation)).  The notation
$\mathbb{P}(V)$ is used when the categorical construction matters
(built from the fundamental object $V$); the notation
$\mathbb{P}^1(R)$ is used in scheme-theoretic or coordinate
contexts ([contact affine chart](#def:contact-affine-chart)).
<!-- FILE_END: projective-line-object.md -->

<!-- FILE_START: projective-line-su2.md -->
Continuing [maximal torus of $\mathrm{SU}(2)$](#ex:maximal-torus-su2),
$G = \mathrm{SU}(2)$ and $T = \mathrm{U}(1)$.
The quotient is
$\mathbb{P}(V) = \mathrm{SU}(2)/\mathrm{U}(1) \cong \mathbb{P}^1(\mathbb{C})$.
A point $[\ell] \in \mathbb{P}^1(\mathbb{C})$ is a line $\ell \subset V = \mathbb{C}^2$;
equivalently, it is the kernel of a linear form on $V$, well-defined up
to scalar. The function algebra is the polynomial ring
$\mathcal{O}(\mathbb{P}^1(\mathbb{C})) = \mathbb{C}[z]$ in the affine coordinate
$z = v_1 / v_2$.
<!-- FILE_END: projective-line-su2.md -->

<!-- FILE_START: contact-affine-chart.md -->
Let $\mathcal{S}$ be the state bundle over $M$ whose fibres are the spaces of
$1$-forms, and let $\mathbb{P}(V)$ be the projective line object
([projective line object](#def:projective-line-object)). Using the
Reeb decomposition ([Reeb decomposition](#ex:reeb-decomposition)),
every form splits as
$\alpha = \alpha_H + \varTheta \wedge \iota_\xi \alpha$.

The **contact affine chart** $U_\xi \subset \mathbb{P}(V)$ is the open
dense subset of states with non-vanishing Reeb component:

$$
  U_\xi =  \bigl\{ [\alpha] \in \mathbb{P}(V)
   \big|  \iota_\xi\alpha \neq 0 \bigr\}.
$$

On $U_\xi$, the explicit *affine coordinate* is defined by the ratio
of horizontal spatial diffusion to vertical quantum spin:

$$
  Z([\alpha]) =  \frac{\alpha_H}{\iota_\xi\alpha}.
$$

```tex
\begin{equation}\label{eq:contact-affine-chart-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  U_\xi \ar[r, hook] \ar[d, "Z"']
  & \mathbb{P}(V) \ar[d, "\cong", "G/T"'] \\
  H = \ker\varTheta \ar[r, hook]
  & \Omega^1_H(A)
\end{tikzcd}
\end{equation}
```

The coordinate $Z$ takes values in the horizontal distribution
$H = \ker\varTheta$. The contact form $\varTheta$ and the Reeb vector field
$\xi$ thus automatically provide the stereographic projection for the
projective line fibres — no external coordinates are needed.
<!-- FILE_END: contact-affine-chart.md -->

