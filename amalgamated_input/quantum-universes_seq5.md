<!-- FILE_START: qu-structures-intro.md -->
With the QU axioms and their immediate consequences settled, we assemble the differential-geometric vocabulary the next chapter will build on: this is precisely the data that *Quantum Observable Universes* equips with observability and measurability, and on which the volume constraint forcing $\mathrm{SU}_2(R)$ as the gauge group acts. Getting there takes four movements — a connection with its curvature, the jet object that packages its first-order data, a Hodge star, and an internal Poisson structure. The connection comes first because everything else refines it. Definition: Categorical connection and curvature introduces a connection as a morphism $\nabla \colon A \to A \otimes \Omega^1(A)$ satisfying the Leibniz rule, with curvature $F_\nabla = \nabla^2 \colon A \to A \otimes \Omega^2(A)$. Proposition: Existence of categorical connections and Proposition: Uniqueness of categorical connections (up to gauge) then guarantee that every QU admits such a $\nabla$ and pin down the space of connections as an affine space over $\Omega^1(A) \otimes \mathrm{Ad}(A)$, and Example: Categorical connection as Maurer--Cartan form on $\mathrm{SU}(2)$ makes the abstract object concrete as the flat left-invariant connection $\varTheta = g^{-1} dg$. With the connection in hand, its first-order data wants a home: Definition: Categorical jet object provides one, packaging $J^1(A) = A \otimes_{\mathbf{C}} \Omega^1(A)$ as the middle term of the universal extension $0 \to A \otimes \Omega^1(A) \to J^1(A) \to A \to 0$.

The Hodge half of the section runs in parallel, and the classical picture is the one to keep in view. On the three-dimensional left-invariant calculus of $\mathrm{SU}(2)$ the Hodge star sends a $1$-form to a $2$-form by $\star\omega_i = \tfrac12 \epsilon_{ijk} \omega_j \wedge \omega_k$; the categorical operator below is the abstraction that must reproduce exactly this correspondence. Definition: Categorical Hodge star defines $\star \colon \Omega^k(A) \to \Omega^{n-k}(A)$ by the identity $\alpha \wedge \star \beta = \int_A(\alpha^* \cdot \beta) \mathrm{vol}$, using the Frobenius form, the antipode-conjugate, and a normalised volume form. Proposition: Existence of the categorical Hodge star and Proposition: Uniqueness of the categorical Hodge star show that $\star$ is well-defined and satisfies $\star^2 = \mathrm{id}$, the uniqueness conditional on a fixed Frobenius form and a fixed volume. Example: Hodge star on $\mathcal{O}(\mathrm{SU}(2))$ then computes $\star$ on that $3$-dimensional calculus and recovers exactly the classical correspondence above.

The section closes with the Poisson structure that links the differential calculus to deformation theory. Definition: Internal Poisson object defines a Poisson bivector as a morphism $\pi \colon \mathbf{1} \to \Lambda^2(\Omega^1(A)^{\vee})$ subject to the Schouten--Nijenhuis Jacobi condition $[\pi, \pi]_{\mathrm{SN}} = 0$ and a biderivation Leibniz rule, with the bracket $\{f, g\} = \langle \pi, df \wedge dg \rangle$ recovered through the Frobenius self-duality $A \cong A^{\vee}$. Remark: Relation to HKR and skew-Poisson integration identifies $\pi$ as the image of the Hochschild--Kostant--Rosenberg map applied to the first-order Hopf deformation $\phi_1 \in HH^2(\mathcal{U}_q, \mathrm{Ad})$, and matches the internal Poisson bracket against the skew-Poisson structure of the formal-group integration theorem — the bridge to the deformation-theoretic reading the next chapter takes up.
<!-- FILE_END: qu-structures-intro.md -->

<!-- FILE_START: categorical-connection.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum universe over $R$ with
differential forms $\Omega^k(A)$ ([higher forms](#def:higher-forms)).

A connection is the categorical device that lets one differentiate
sections and transport structure along $A$; it generalizes the
classical de Rham connection $d$ on differential forms, and the
$\mathrm{SU}(2)$ instance in [Example](#ex:categorical-connection-su2)
gives the reader's first concrete grip on it.

A **connection** on $A$ is a morphism
$\nabla \colon A \to A \otimes \Omega^1(A)$ in $\mathbf{C}$ satisfying
the Leibniz rule: $\nabla(\mu(a \otimes b)) = \nabla(a) \cdot b + a \cdot \nabla(b)$, expressed by the commutativity
of the *Leibniz triangle*:

```tex
\begin{equation}\label{eq:leibniz-triangle}
\begin{tikzcd}[row sep=2.5em, column sep=3.5em]
  A \otimes A
    \ar[r, "\mu"]
    \ar[dr, "{\nabla \otimes 1 + 1 \otimes \nabla}"']
  & A \ar[d, "\nabla"]
  \\
  & A \otimes \Omega^1(A)
\end{tikzcd}
\end{equation}
```

The **curvature** of $\nabla$ is the composition

```tex
\begin{equation}\label{eq:curvature-composition}
\begin{tikzcd}[column sep=3em]
  A \ar[r, "\nabla"]
  & A \otimes \Omega^1(A) \ar[r, "\nabla"]
  & A \otimes \Omega^2(A)
\end{tikzcd}
\end{equation}
```

denoted $F_\nabla = \nabla^2$, which is $A$-linear (a standard
consequence of the Leibniz rule).
<!-- FILE_END: categorical-connection.md -->

<!-- FILE_START: categorical-connection-exists.md -->
A categorical connection is the substrate analogue of a gauge or
differential connection: it equips the observable algebra $A$ with a
covariant-derivative structure, so that the abstract triple carries the
same differential geometry as a bundle with connection. Here
$\Omega^1(A)$ plays the role of the one-forms on $A$, and $\nabla$ sends
an observable to its differential. The content of the result is that
this structure always exists.

Every [quantum universe](#def:quantum-universe) $(\mathbf{C}, A, \tau)$
admits a [categorical connection](#def:categorical-connection) — i.e.
a morphism $\nabla \colon A \to \Omega^1(A)$ satisfying the Leibniz
rule.

Uniqueness up to gauge is
([uniqueness of categorical connections](#prop:categorical-connection-unique)).
<!-- FILE_END: categorical-connection-exists.md -->

<!-- FILE_START: categorical-connection-unique.md -->
Two [categorical connections](#def:categorical-connection)
$\nabla_1, \nabla_2$ on the same QU differ by a
$\mathrm{Ad}(A)$-valued $1$-form:

$$
  \nabla_2 - \nabla_1 \;\in\; \Omega^1(A) \otimes \mathrm{Ad}(A).
$$

This difference is a categorical gauge potential.  The space of
connections is an affine space over
$\Omega^1(A) \otimes \mathrm{Ad}(A)$, so uniqueness holds up to
gauge.
<!-- FILE_END: categorical-connection-unique.md -->

<!-- FILE_START: categorical-connection-su2.md -->
We instantiate the [categorical connection](#def:categorical-connection)
concretely on $\mathrm{SU}(2)$, continuing the running example from
[SU(2) as a quantum universe](#ex:quantum-universe-su2).

**Classical setup.** A connection on a Lie group $G$ is a
$\mathfrak{g}$-valued 1-form on $G$. The canonical choice is the
**Maurer--Cartan form** $\varTheta = g^{-1}  dg$, a left-invariant
$\mathfrak{su}(2)$-valued 1-form.

**Explicit matrix form.** For $g \in \mathrm{SU}(2)$ written as

$$
g = \begin{pmatrix} \alpha & -\bar{\beta} \\ \beta & \bar{\alpha} \end{pmatrix},
\qquad |\alpha|^2 + |\beta|^2 = 1,
$$

the inverse is $g^{-1} = g^\dagger = \bigl(\begin{smallmatrix} \bar{\alpha} & \bar{\beta} \\ -\beta & \alpha \end{smallmatrix}\bigr)$.
The Maurer--Cartan form evaluates to:

$$
\varTheta = g^{-1} dg
= \begin{pmatrix}
\bar{\alpha}  d\alpha + \bar{\beta}  d\beta &
\bar{\alpha}  d(-\bar{\beta}) + \bar{\beta}  d\bar{\alpha} \\
-\beta  d\alpha + \alpha  d\beta &
-\beta  d(-\bar{\beta}) + \alpha  d\bar{\alpha}
\end{pmatrix}.
$$

Using the constraint $\alpha  d\bar{\alpha} + \bar{\alpha}  d\alpha + \beta  d\bar{\beta} + \bar{\beta}  d\beta = 0$ (differentiation of
$|\alpha|^2 + |\beta|^2 = 1$), one verifies that $\varTheta$ is
traceless and skew-Hermitian: $\varTheta \in \Omega^1(G; \mathfrak{su}(2))$.

**Flatness.** The curvature of the Maurer--Cartan form is

$$
F = d\varTheta + \varTheta \wedge \varTheta.
$$

The **Maurer--Cartan equation** states that $F = 0$ identically.
This follows from $d(g^{-1}) = -g^{-1} (dg)  g^{-1}$:

$$
d\varTheta = d(g^{-1} dg) = d(g^{-1}) \wedge dg
= -g^{-1} dg \wedge g^{-1} dg = -\varTheta \wedge \varTheta,
$$

so $F = d\varTheta + \varTheta \wedge \varTheta = 0$. The Maurer--Cartan form
is a **flat** connection — its curvature vanishes.

**Categorical interpretation.** In the language of the
[categorical connection](#def:categorical-connection), $\varTheta$
corresponds to the natural transformation implementing parallel
transport in $\mathbf{Rep}(\mathrm{SU}(2))$. Flatness ($F = 0$)
means that parallel transport around any contractible loop is trivial
— equivalently, the monodromy depends only on the homotopy class of
the path. Since $\mathrm{SU}(2) \cong S^3$ is connected,
*all* monodromy is trivial: the Maurer--Cartan connection has trivial
holonomy.

Non-flat connections arise when we pass to quotients
(e.g. $\mathrm{SO}(3) = \mathrm{SU}(2)/\mathbb{Z}_2$) or when an
external gauge field is switched on — these are treated in Chapter 2.
<!-- FILE_END: categorical-connection-su2.md -->

<!-- FILE_START: categorical-jet.md -->
Just as a jet of a section of a bundle records the section together
with its first-order variation, the jet object packages an element of
$A$ together with its infinitesimal (first-order) variation along the
connection. Let $(\mathbf{C}, A, \tau)$ be a
([quantum universe](#def:quantum-universe)) with connection $\nabla$
([categorical connection](#def:categorical-connection)). The **jet
object** is

$$
  J^1(A) := A \otimes_{\mathbf{C}} \Omega^1(A),
$$

where $\Omega^1(A) = \ker(\mu \colon A \otimes A \to A)$ is the
bimodule of K\"ahler differentials. The jet object fits into the
universal extension

```tex
\begin{equation}\label{eq:jet-ses}
\begin{tikzcd}[column sep=2.5em]
  0 \ar[r]
  & A \otimes \Omega^1(A) \ar[r]
  & J^1(A) \ar[r, "j^1"]
  & A \ar[r]
  & 0
\end{tikzcd}
\end{equation}
```

where $j^1 \colon J^1(A) \to A$ is the jet evaluation (the counit of
the tensor--hom adjunction).
<!-- FILE_END: categorical-jet.md -->

<!-- FILE_START: categorical-hodge-star.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum universe over $R$
([quantum universe](#def:quantum-universe)) with higher differential forms
$\Omega^k(A)$ ([higher forms](#def:higher-forms)). The
**categorical Hodge star** is the involution
$\star \colon \Omega^k(A) \to \Omega^{n-k}(A)$ defined by

$$
  \alpha \wedge \star \beta
  = \int_A\!\bigl(\alpha^* \cdot \beta\bigr) \mathrm{vol},
$$

```tex
\begin{equation}\label{eq:categorical-hodge-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \Omega^k(A) \ar[r, "\star"] \ar[d, "\star"']
  & \Omega^{n-k}(A) \ar[d, "\star"] \\
  \Omega^{n-k}(A) \ar[r, equal]
  & \Omega^{n-k}(A)
\end{tikzcd}
\qquad (\star^2 = \mathrm{id})
\end{equation}
```

where $\int_A \colon A \to \mathbf{1}$ is the Frobenius form,
$\alpha^* = S(\alpha)$ is the antipode-conjugate, and
$\mathrm{vol} \in \Omega^n(A)$ is the volume form
(the unique $G$-invariant top form normalised by
$\int_A(\mathrm{vol}) = 1$).
That $\star^2 = \mathrm{id}$ (i.e. $\star$ is an involution)
follows from the non-degeneracy of $\int_A$ and the involutivity of
the antipode. More precisely: $S^2 = \mathrm{id}$ holds on $A$
because a commutative Hopf algebra has involutive antipode (and our
Frobenius--Hopf axioms imply commutativity of $A$ via the faithfulness
of $\tau$ into $R\text{-}\mathrm{Mod}$). The extension to
$\Omega^k(A)$ follows from the graded Leibniz rule for $S$ on the
differential graded algebra.
<!-- FILE_END: categorical-hodge-star.md -->

<!-- FILE_START: categorical-hodge-star-exists.md -->
Let $(\mathbf{C}, A, \tau)$ be a
[quantum universe](#def:quantum-universe) of dimension $n$ with
volume form $\mathrm{vol} \in \Omega^n(A)$.  Then the
[categorical Hodge star](#def:categorical-hodge-star)
$\star \colon \Omega^k(A) \to \Omega^{n-k}(A)$ exists as a morphism
in $\mathbf{C}$ and satisfies $\star^2 = \mathrm{id}$.

Uniqueness is
([uniqueness of categorical Hodge star](#prop:categorical-hodge-star-unique)).
<!-- FILE_END: categorical-hodge-star-exists.md -->

<!-- FILE_START: categorical-hodge-star-unique.md -->
The [existence proposition](#prop:categorical-hodge-star-exists)
constructs a categorical Hodge star but leaves open whether it is
canonical; this proposition closes that gap. Given a fixed Frobenius
form $\int_A$ and volume form $\mathrm{vol}$, the
[categorical Hodge star](#def:categorical-hodge-star) $\star$ is
uniquely determined: the defining Frobenius pairing is what pins it
down, so any other involution $\star'$ satisfying
$\alpha \wedge \star' \beta = \int_A(\alpha^* \cdot \beta) \mathrm{vol}$
for all $\alpha$ coincides with $\star$.
<!-- FILE_END: categorical-hodge-star-unique.md -->

<!-- FILE_START: hodge-su2.md -->
Continuing [higher forms on SU(2)](#ex:higher-forms-su2), the Hodge star on
$A = \mathcal{O}(\mathrm{SU}(2))$ identifies $\Omega^k(A)$ with
$\Omega^{n-k}(A)$ using the Frobenius form as the inner product — the
categorical version of "rotating a form into its complement". On the
$3D$-calculus $\Omega^{\bullet}(A)$ it acts as follows. The volume form is
$\mathrm{vol} = \omega_1 \wedge \omega_2 \wedge \omega_3$
(normalised by $\int_A(\mathrm{vol}) = 1$). Then:

- $\star 1 = \mathrm{vol}$,
  $\star\mathrm{vol} = 1$.
- On $1$-forms: $\star\omega_i = \tfrac{1}{2}\epsilon_{ijk} \omega_j \wedge \omega_k$ (each basis form maps to its
  complementary $2$-form).
- On $2$-forms: $\star(\omega_i \wedge \omega_j) = \epsilon_{ijk}\omega_k$ (each basis $2$-form maps to its
  complementary $1$-form).

The self-dual
$2$-forms $\Omega^+(A)$ are the $+1$-eigenspace of $\star$; in
$3$ dimensions, $\star$ on $\Omega^2(A)$ maps to $\Omega^1(A)$, so
the self-dual/anti-self-dual decomposition is trivial. The
non-trivial decomposition arises when $\dim H = 4$ (the archimedean
case, [self-dual curvature](#ex:self-dual-curvature)).
<!-- FILE_END: hodge-su2.md -->

<!-- FILE_START: poisson-object.md -->
Let $(\mathbf{C}, A, \tau)$ be a
[quantum universe](#def:quantum-universe) with
[Frobenius pairing](#def:frobenius-pairing)
$\int_A \circ \mu \colon A \otimes A \to \mathbf{1}$ and
[higher forms](#def:higher-forms) $\Omega^k(A)$.

We now equip the quantum universe with an internal Poisson
structure: a datum that endows $A$ with a bracket $\{-, -\}$, the
categorical counterpart of the phase-space bracket of classical
mechanics and the first-order datum of a deformation quantisation.

An **internal Poisson object** on $A$ is a morphism

$$
\pi \colon \mathbf{1} \longrightarrow \Lambda^2\bigl(\Omega^1(A)^{\vee}\bigr)
$$

in $\mathbf{C}$ (a *bivector*), subject to the conditions below.
Concretely, $\pi$ contracts a pair of differentials to a scalar,
so that it defines the bracket
$\{f, g\} := \langle \pi, df \wedge dg \rangle$ on points
$f, g \colon \mathbf{1} \to A$; the remainder of this block makes
the contraction $\langle \pi, {-} \rangle$ precise.

**Construction via pullback.**
The Frobenius self-duality $A \xrightarrow{ \sim } A^{\vee}$
induces an identification $\Omega^1(A)^{\vee} \cong \Omega^1(A)$
(dualising the bimodule of Kähler differentials through the
non-degenerate pairing).  Composing with the exterior square gives
the *Poisson bivector object*

$$
\Pi  :=  \Lambda^2\bigl(\Omega^1(A)^{\vee}\bigr)
 \cong  \Lambda^2\bigl(\Omega^1(A)\bigr)
=  \Omega^2(A).
$$

A global section $\pi \colon \mathbf{1} \to \Pi$ then defines a
*Poisson bracket* on $A$ by the composite

```tex
\begin{equation}\label{eq:poisson-bracket-pullback}
\begin{tikzcd}[row sep=1.5em, column sep=2.2em]
  A \otimes A
    \ar[r, "d \otimes d"]
  & \Omega^1(A) \otimes \Omega^1(A)
    \ar[r, "\wedge"]
  & \Omega^2(A)
    \ar[r, "\langle \pi{,} {-} \rangle"]
  & A
\end{tikzcd}
\end{equation}
```

where $d$ is the universal derivation, $\wedge$ the exterior product,
and the contraction $\langle \pi, {-} \rangle$ is the pullback of
$\pi$ through the Frobenius isomorphism.  Explicitly,
$\{f, g\} := \langle \pi, df \wedge dg \rangle$ for
$f, g \colon \mathbf{1} \to A$.

**Axioms.** The morphism $\pi$ must satisfy:

1. **Jacobi identity.** The Jacobiator
   $\{f, \{g, h\}\} + \{g, \{h, f\}\} + \{h, \{f, g\}\} = 0$
   vanishes, equivalently the Schouten--Nijenhuis condition
   $[\pi, \pi]_{\mathrm{SN}} = 0$ on the bivector.

2. **Leibniz rule.** $\{f, gh\} = \{f, g\}h + g\{f, h\}$,
   ensuring the bracket is a biderivation with respect to the
   multiplication $\mu$ on $A$.

Anti-symmetry $\{f, g\} = -\{g, f\}$ is automatic: since $\pi$
factors through $\Lambda^2(\Omega^1(A)^{\vee})$ (the exterior
square, not the full tensor square), the bracket inherits the
anti-symmetry of the wedge product.

The triple $(A, \mu, \pi)$ is then a *Poisson algebra object* in
$\mathbf{C}$.
<!-- FILE_END: poisson-object.md -->

<!-- FILE_START: poisson-hkr-connection.md -->
The [internal Poisson object](#def:poisson-object) makes explicit a
structure that is already implicit in the paper's deformation theory.
Concretely, over $\mathbf{C} = \mathrm{Mod}(\mathbb{F}_p)$ with
$A = \mathcal{O}(H)$ that object is the $p$-truncated skew-Poisson
biderivation $\pi_<$ of
[skew-Poisson integration](#prop:skew-poisson-integration) — the image
under the fibre functor $\tau$ of the bivector $\pi$ constructed below.
The remainder of this block builds that bivector from the Hochschild
picture and recovers $\pi_<$ as its shadow.

**From Hochschild to bivectors.**
The first-order deformation $\phi_1 \in HH^2(\mathcal{U}_q, \mathrm{Ad})$
of the Frobenius--Hopf algebra
([classical limit obstruction](#def:classical-limit-obstruction))
maps under the Hochschild--Kostant--Rosenberg isomorphism to a
bivector field:

$$
\mathrm{HKR} \colon HH^2(A, A)
\xrightarrow{ \sim }
\Gamma\!\bigl(\Lambda^2 T_A\bigr)
= 
\mathrm{Hom}_{\mathbf{C}}\!\bigl(\mathbf{1},
  \Lambda^2(\Omega^1(A)^{\vee})\bigr).
$$

The image $\pi := \mathrm{HKR}(\phi_1)$ is precisely a global section
of the bivector object $\Pi$ from the
[Poisson object definition](#def:poisson-object).  The Jacobi identity
on $\pi$ corresponds to the Maurer--Cartan equation
$[\phi_1, \phi_1] = 0$ in the Hochschild complex.

**Internal vs.\ external.**
The classical approach defines the Poisson bracket on $A$ by
passing through $\tau$ to the vector-space level and invoking HKR
there.  The internal definition avoids this detour: the bivector
$\pi \colon \mathbf{1} \to \Pi$ into the bivector object $\Pi$ and the
contraction
$\langle \pi, {-} \rangle$ live entirely inside $\mathbf{C}$, using
only the Frobenius self-duality $A \cong A^{\vee}$ and the
differential calculus $\Omega^{\bullet}(A)$.

**Model: skew-Poisson integration.**
When $\mathbf{C} = \mathrm{Mod}(\mathbb{F}_p)$ and $A = \mathcal{O}(H)$
for a commutative formal group $H$, the internal Poisson object
specialises to the skewed-Poisson structure $\pi_<$ of
[skew-Poisson integration](#prop:skew-poisson-integration): the
biderivation $\pi_<$ is the image of $\pi$ under $\tau$, and the
$p$-truncated Jacobi condition is the shadow of the internal Jacobi
identity modulo $p$-th powers.  The integration theorem then lifts
$(H, \pi_<)$ to a non-commutative formal group $G / \mathbb{Z}_p$
whose distribution algebra deforms $\mathrm{Dist}(H)$ while
preserving the Frobenius relation.
<!-- FILE_END: poisson-hkr-connection.md -->

<!-- FILE_START: outro-quantum-universes.md -->
The concrete payoff of this chapter is an internal Poisson bracket on
the Frobenius–Hopf object $A$, fixed without recourse to any fibre
functor.  Assembling it required the full categorical setup for a
Quantum Universe: a rigid braided monoidal category $\mathbf{C}$
carrying such an object $A$, together with a categorical connection,
jet, Hodge star, and internal Poisson object on $A$.  The
Hochschild–Kostant–Rosenberg map identifies the first-order
deformation class with a global section of $\Lambda^2 (\Omega^1)^\vee$,
fixing the bracket internally before any fibre functor is invoked.

The next chapter promotes this static categorical data to a *Quantum
Observable Universe* by adjoining the substrate parameter $q$ and the
Reeb derivation $\xi$ that controls one-parameter flow.  Every
construction in this chapter — connection, jet, Hodge star, Poisson
bracket — receives a $q$-deformation when the substrate parameter
moves, and the chapters that follow trace the consequences of that
deformation through the categorical-braiding, knot-theoretic, and
physical-observation layers.
<!-- FILE_END: outro-quantum-universes.md -->

