<!-- FILE_START: qu-structures-intro.md -->
We now assemble the differential-geometric vocabulary that *Quantum Observable Universes* equips with observability and measurability. A connection with its curvature, the jet object packaging its first-order data, a Hodge star, and an internal Poisson structure comprise this vocabulary.

The connection comes first because everything else refines it. A connection is a morphism $\nabla \colon A \to A \otimes \Omega^1(A)$ satisfying the Leibniz rule, with curvature $F_\nabla = \nabla^2 \colon A \to A \otimes \Omega^2(A)$. Every QU admits such a $\nabla$. The space of connections is an affine space over $\Omega^1(A) \otimes \mathrm{Ad}(A)$. On $\mathrm{SU}(2)$, the flat left-invariant connection $\varTheta = g^{-1} dg$ makes the abstract object concrete. The first-order data of the connection packages into the jet object $J^1(A) = A \otimes_{\mathbf{C}} \Omega^1(A)$, the middle term of the universal extension $0 \to A \otimes \Omega^1(A) \to J^1(A) \to A \to 0$.

The Hodge half runs in parallel. The categorical Hodge star $\star \colon \Omega^k(A) \to \Omega^{n-k}(A)$ is defined by $\alpha \wedge \star \beta = \int_A(\alpha^* \cdot \beta) \mathrm{vol}$. It uses the Frobenius form, the antipode-conjugate, and a normalised volume form. The operator is well-defined and satisfies $\star^2 = \mathrm{id}$. On the three-dimensional left-invariant calculus of $\mathrm{SU}(2)$, it sends a $1$-form to a $2$-form by $\star\omega_i = \tfrac12 \epsilon_{ijk} \omega_j \wedge \omega_k$, recovering the classical correspondence.

An internal Poisson structure links the differential calculus to deformation theory. The internal Poisson object defines a Poisson bivector as a morphism $\pi \colon \mathbf{1} \to \Lambda^2(\Omega^1(A)^{\vee})$ subject to the Schouten--Nijenhuis Jacobi condition $[\pi, \pi]_{\mathrm{SN}} = 0$ and a biderivation Leibniz rule. The bracket is $\{f, g\} = \langle \pi, df \wedge dg \rangle$. This bivector $\pi$ is the image of the Hochschild--Kostant--Rosenberg map applied to the first-order Hopf deformation. It matches the internal Poisson bracket against the skew-Poisson structure of formal-group integration.
<!-- FILE_END: qu-structures-intro.md -->

<!-- FILE_START: categorical-connection.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum universe over $R$ with differential forms $\Omega^k(A)$ ([higher forms](#def:higher-forms)).

A connection differentiates sections and transports structure along $A$. It generalizes the classical de Rham connection $d$. The $\mathrm{SU}(2)$ instance in [Example](#ex:categorical-connection-su2) provides a concrete picture.

A **connection** on $A$ is a morphism $\nabla \colon A \to A \otimes \Omega^1(A)$ in $\mathbf{C}$ satisfying the Leibniz rule $\nabla(\mu(a \otimes b)) = \nabla(a) \cdot b + a \cdot \nabla(b)$. This is expressed by the commutativity of the *Leibniz triangle*:

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

The **curvature** of $\nabla$ is the composition:

```tex
\begin{equation}\label{eq:curvature-composition}
\begin{tikzcd}[column sep=3em]
  A \ar[r, "\nabla"]
  & A \otimes \Omega^1(A) \ar[r, "\nabla"]
  & A \otimes \Omega^2(A)
\end{tikzcd}
\end{equation}
```

This composition is denoted $F_\nabla = \nabla^2$. It is $A$-linear, a standard consequence of the Leibniz rule.
<!-- FILE_END: categorical-connection.md -->

<!-- FILE_START: categorical-connection-exists.md -->
A categorical connection equips the observable algebra $A$ with a covariant-derivative structure. The abstract triple carries the same differential geometry as a bundle with connection. Here $\Omega^1(A)$ plays the role of one-forms, and $\nabla$ sends an observable to its differential.

Every [quantum universe](#def:quantum-universe) $(\mathbf{C}, A, \tau)$ admits a [categorical connection](#def:categorical-connection), which is a morphism $\nabla \colon A \to \Omega^1(A)$ satisfying the Leibniz rule. Uniqueness up to gauge is shown in [uniqueness of categorical connections](#prop:categorical-connection-unique).
<!-- FILE_END: categorical-connection-exists.md -->

<!-- FILE_START: categorical-connection-unique.md -->
Two [categorical connections](#def:categorical-connection) $\nabla_1, \nabla_2$ on the same QU differ by a $\mathrm{Ad}(A)$-valued $1$-form:

$$
  \nabla_2 - \nabla_1 \;\in\; \Omega^1(A) \otimes \mathrm{Ad}(A).
$$

This difference is a categorical gauge potential. The space of connections is an affine space over $\Omega^1(A) \otimes \mathrm{Ad}(A)$, making uniqueness hold up to gauge.
<!-- FILE_END: categorical-connection-unique.md -->

<!-- FILE_START: categorical-connection-su2.md -->
We instantiate the [categorical connection](#def:categorical-connection) concretely on [SU(2)](#ex:quantum-universe-su2).

**Classical setup.** A connection on a Lie group $G$ is a $\mathfrak{g}$-valued 1-form on $G$. The canonical choice is the **Maurer--Cartan form** $\varTheta = g^{-1}  dg$, a left-invariant $\mathfrak{su}(2)$-valued 1-form.

**Explicit matrix form.** For $g \in \mathrm{SU}(2)$ written as

$$
g = \begin{pmatrix} \alpha & -\bar{\beta} \\ \beta & \bar{\alpha} \end{pmatrix}, \qquad |\alpha|^2 + |\beta|^2 = 1,
$$

the inverse is $g^{-1} = g^\dagger = \bigl(\begin{smallmatrix} \bar{\alpha} & \bar{\beta} \\ -\beta & \alpha \end{smallmatrix}\bigr)$. The Maurer--Cartan form evaluates to:

$$
\varTheta = g^{-1} dg
= \begin{pmatrix}
\bar{\alpha}  d\alpha + \bar{\beta}  d\beta &
\bar{\alpha}  d(-\bar{\beta}) + \bar{\beta}  d\bar{\alpha} \\
-\beta  d\alpha + \alpha  d\beta &
-\beta  d(-\bar{\beta}) + \alpha  d\bar{\alpha}
\end{pmatrix}.
$$

Using the constraint $\alpha  d\bar{\alpha} + \bar{\alpha}  d\alpha + \beta  d\bar{\beta} + \bar{\beta}  d\beta = 0$, one verifies that $\varTheta$ is traceless and skew-Hermitian: $\varTheta \in \Omega^1(G; \mathfrak{su}(2))$.

**Flatness.** The curvature of the Maurer--Cartan form is $F = d\varTheta + \varTheta \wedge \varTheta$. The **Maurer--Cartan equation** states that $F = 0$ identically. This follows from $d(g^{-1}) = -g^{-1} (dg)  g^{-1}$:

$$
d\varTheta = d(g^{-1} dg) = d(g^{-1}) \wedge dg
= -g^{-1} dg \wedge g^{-1} dg = -\varTheta \wedge \varTheta,
$$

so $F = d\varTheta + \varTheta \wedge \varTheta = 0$. The Maurer--Cartan form is a **flat** connection.

**Categorical interpretation.** The connection $\varTheta$ corresponds to the natural transformation implementing parallel transport in $\mathbf{Rep}(\mathrm{SU}(2))$. Flatness ($F = 0$) means parallel transport around any contractible loop is trivial. Since $\mathrm{SU}(2) \cong S^3$ is connected, all monodromy is trivial. The Maurer--Cartan connection has trivial holonomy.
<!-- FILE_END: categorical-connection-su2.md -->

<!-- FILE_START: categorical-jet.md -->
A jet object packages an element of $A$ together with its infinitesimal variation along the connection. Let $(\mathbf{C}, A, \tau)$ be a [quantum universe](#def:quantum-universe) with connection $\nabla$ ([categorical connection](#def:categorical-connection)). The **jet object** is

$$
  J^1(A) := A \otimes_{\mathbf{C}} \Omega^1(A),
$$

where $\Omega^1(A) = \ker(\mu \colon A \otimes A \to A)$ is the bimodule of K\"ahler differentials. The jet object fits into the universal extension

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

where $j^1 \colon J^1(A) \to A$ is the jet evaluation.
<!-- FILE_END: categorical-jet.md -->

<!-- FILE_START: categorical-hodge-star.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum universe over $R$ with higher differential forms $\Omega^k(A)$ ([higher forms](#def:higher-forms)). The **categorical Hodge star** is the involution $\star \colon \Omega^k(A) \to \Omega^{n-k}(A)$ defined by

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

where $\int_A \colon A \to \mathbf{1}$ is the Frobenius form, $\alpha^* = S(\alpha)$ is the antipode-conjugate, and $\mathrm{vol} \in \Omega^n(A)$ is the volume form (the unique invariant top form normalised by $\int_A(\mathrm{vol}) = 1$). That $\star^2 = \mathrm{id}$ follows from the non-degeneracy of $\int_A$ and the involutivity of the antipode. The extension to $\Omega^k(A)$ follows from the graded Leibniz rule for $S$.
<!-- FILE_END: categorical-hodge-star.md -->

<!-- FILE_START: categorical-hodge-star-exists.md -->
Let $(\mathbf{C}, A, \tau)$ be a [quantum universe](#def:quantum-universe) of dimension $n$ with volume form $\mathrm{vol} \in \Omega^n(A)$. The [categorical Hodge star](#def:categorical-hodge-star) $\star \colon \Omega^k(A) \to \Omega^{n-k}(A)$ exists as a morphism in $\mathbf{C}$ and satisfies $\star^2 = \mathrm{id}$. Uniqueness is shown in [uniqueness of categorical Hodge star](#prop:categorical-hodge-star-unique).
<!-- FILE_END: categorical-hodge-star-exists.md -->

<!-- FILE_START: categorical-hodge-star-unique.md -->
Given a fixed Frobenius form $\int_A$ and volume form $\mathrm{vol}$, the [categorical Hodge star](#def:categorical-hodge-star) $\star$ is uniquely determined. The defining Frobenius pairing pins it down. Any other involution $\star'$ satisfying $\alpha \wedge \star' \beta = \int_A(\alpha^* \cdot \beta) \mathrm{vol}$ coincides with $\star$.
<!-- FILE_END: categorical-hodge-star-unique.md -->

<!-- FILE_START: hodge-su2.md -->
Continuing [higher forms on SU(2)](#ex:higher-forms-su2), the Hodge star on $A = \mathcal{O}(\mathrm{SU}(2))$ identifies $\Omega^k(A)$ with $\Omega^{n-k}(A)$ using the Frobenius form. On the $3D$-calculus $\Omega^{\bullet}(A)$, the volume form is $\mathrm{vol} = \omega_1 \wedge \omega_2 \wedge \omega_3$ (normalised by $\int_A(\mathrm{vol}) = 1$). Then:

- $\star 1 = \mathrm{vol}$, $\star\mathrm{vol} = 1$.
- On $1$-forms: $\star\omega_i = \tfrac{1}{2}\epsilon_{ijk} \omega_j \wedge \omega_k$.
- On $2$-forms: $\star(\omega_i \wedge \omega_j) = \epsilon_{ijk}\omega_k$.

The self-dual $2$-forms $\Omega^+(A)$ are the $+1$-eigenspace of $\star$. In $3$ dimensions, $\star$ maps $\Omega^2(A)$ to $\Omega^1(A)$, so the self-dual decomposition is trivial. The non-trivial decomposition arises when $\dim H = 4$.
<!-- FILE_END: hodge-su2.md -->

<!-- FILE_START: poisson-object.md -->
Let $(\mathbf{C}, A, \tau)$ be a [quantum universe](#def:quantum-universe) with [Frobenius pairing](#def:frobenius-pairing) $\int_A \circ \mu \colon A \otimes A \to \mathbf{1}$ and [higher forms](#def:higher-forms) $\Omega^k(A)$. We equip the quantum universe with an internal Poisson structure. 

An **internal Poisson object** on $A$ is a morphism

$$
\pi \colon \mathbf{1} \longrightarrow \Lambda^2\bigl(\Omega^1(A)^{\vee}\bigr)
$$

in $\mathbf{C}$ (a *bivector*). It contracts a pair of differentials to a scalar, defining the bracket $\{f, g\} := \langle \pi, df \wedge dg \rangle$ for $f, g \colon \mathbf{1} \to A$.

**Construction via pullback.** The Frobenius self-duality $A \xrightarrow{ \sim } A^{\vee}$ induces an identification $\Omega^1(A)^{\vee} \cong \Omega^1(A)$. Composing with the exterior square gives the *Poisson bivector object*

$$
\Pi  :=  \Lambda^2\bigl(\Omega^1(A)^{\vee}\bigr)
 \cong  \Lambda^2\bigl(\Omega^1(A)\bigr)
=  \Omega^2(A).
$$

A global section $\pi \colon \mathbf{1} \to \Pi$ defines a *Poisson bracket* on $A$ by the composite:

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

**Axioms.** The morphism $\pi$ must satisfy:

1. **Jacobi identity.** The Jacobiator vanishes: $\{f, \{g, h\}\} + \{g, \{h, f\}\} + \{h, \{f, g\}\} = 0$, equivalently $[\pi, \pi]_{\mathrm{SN}} = 0$.
2. **Leibniz rule.** $\{f, gh\} = \{f, g\}h + g\{f, h\}$, ensuring the bracket is a biderivation.

Anti-symmetry $\{f, g\} = -\{g, f\}$ is automatic because $\pi$ factors through the exterior square. The triple $(A, \mu, \pi)$ is a *Poisson algebra object* in $\mathbf{C}$.
<!-- FILE_END: poisson-object.md -->

<!-- FILE_START: poisson-hkr-connection.md -->
The [internal Poisson object](#def:poisson-object) makes explicit a structure implicit in the deformation theory. Over $\mathbf{C} = \mathrm{Mod}(\mathbb{F}_p)$ with $A = \mathcal{O}(H)$, this object is the $p$-truncated skew-Poisson biderivation $\pi_<$ of [skew-Poisson integration](#prop:skew-poisson-integration).

**From Hochschild to bivectors.** The first-order deformation $\phi_1 \in HH^2(\mathcal{U}_q, \mathrm{Ad})$ of the Frobenius--Hopf algebra maps under the Hochschild--Kostant--Rosenberg isomorphism to a bivector field:

$$
\mathrm{HKR} \colon HH^2(A, A)
\xrightarrow{ \sim }
\Gamma\!\bigl(\Lambda^2 T_A\bigr)
= 
\mathrm{Hom}_{\mathbf{C}}\!\bigl(\mathbf{1},
  \Lambda^2(\Omega^1(A)^{\vee})\bigr).
$$

The image $\pi := \mathrm{HKR}(\phi_1)$ is a global section of the bivector object $\Pi$. The Jacobi identity on $\pi$ corresponds to the Maurer--Cartan equation $[\phi_1, \phi_1] = 0$.

**Internal vs. external.** The classical approach defines the Poisson bracket by passing through $\tau$ to the vector-space level and invoking HKR. The internal definition avoids this detour. The bivector $\pi \colon \mathbf{1} \to \Pi$ and the contraction live entirely inside $\mathbf{C}$.

**Model: skew-Poisson integration.** When $\mathbf{C} = \mathrm{Mod}(\mathbb{F}_p)$ and $A = \mathcal{O}(H)$, the internal Poisson object specialises to the skewed-Poisson structure $\pi_<$ of [skew-Poisson integration](#prop:skew-poisson-integration). The $p$-truncated Jacobi condition is the shadow of the internal Jacobi identity modulo $p$-th powers. The integration theorem lifts $(H, \pi_<)$ to a non-commutative formal group $G / \mathbb{Z}_p$.
<!-- FILE_END: poisson-hkr-connection.md -->

<!-- FILE_START: outro-quantum-universes.md -->
The concrete payoff of this chapter is an internal Poisson bracket on the Frobenius–Hopf object $A$, fixed without recourse to any fibre functor. Assembling it required a rigid braided monoidal category $\mathbf{C}$ carrying $A$, together with a categorical connection, jet, Hodge star, and internal Poisson object on $A$. The Hochschild–Kostant–Rosenberg map identifies the first-order deformation class with a global section of $\Lambda^2 (\Omega^1)^\vee$.

The next chapter promotes this static categorical data to a *Quantum Observable Universe* by adjoining the substrate parameter $q$ and the Reeb derivation $\xi$ controlling one-parameter flow. Every construction receives a $q$-deformation when the substrate parameter moves. The following chapters trace the consequences of that deformation.
<!-- FILE_END: outro-quantum-universes.md -->

