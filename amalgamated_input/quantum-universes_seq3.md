<!-- FILE_START: quantum-universe-frobenius-pairing-unique-intro.md -->
Pinning the Frobenius pairing on the fundamental object $A$ makes the $\mathrm{SU}(2)$ realisation canonical. The pairing is unique, forcing its explicit $\mathrm{SU}(2)$ form. Every downstream construction inherits this fixed choice.

This sub-section proves the pairing unique and exhibits the $\mathrm{SU}(2)$ realisation. The arc proceeds through:

1. The uniqueness proof for the pairing on $A$.
2. The explicit $\mathrm{SU}(2)$ pairing realisation.
3. The geometric role of the pairing in the substrate-flow.
4. The canonical $\mathrm{SU}(2)$ explication and table data.
5. The higher-forms identification.
<!-- FILE_END: quantum-universe-frobenius-pairing-unique-intro.md -->

<!-- FILE_START: frobenius-pairing-unique.md -->
The Frobenius pairing is canonical up to overall scale. Let $(\mathbf{C}, A, \tau)$ be a [quantum universe](#def:quantum-universe) with $A$ simple. Any two non-degenerate Frobenius forms $\int_A^{(1)}, \int_A^{(2)}$ differ by an invertible scalar:

$$
  \int_A^{(2)} \;=\; c  \int_A^{(1)}
  \qquad\text{for some } c \in \mathrm{Aut}_{\mathbf{C}}(\mathbf{1}).
$$

The induced pairings $\langle \cdot, \cdot \rangle_i = \int_A^{(i)} \circ \mu$ differ by the same scalar. The [Frobenius pairing](#def:frobenius-pairing) is unique up to global normalisation.
<!-- FILE_END: frobenius-pairing-unique.md -->

<!-- FILE_START: frobenius-pairing-su2.md -->
We make the Frobenius pairing concrete on [SU(2)](#ex:quantum-universe-su2).

Set $A = \mathcal{O}(\mathrm{SU}(2))$ with pointwise multiplication $\mu(f \otimes g) = fg$ and Haar integral $\int_A f = \int_{\mathrm{SU}(2)} f(x)\,d\mu_{\mathrm{Haar}}(x)$. The Frobenius pairing is the $L^2$ inner product:

$$
  \langle f, g \rangle_A
  =  \int_{\mathrm{SU}(2)} f(x)g(x)\,d\mu_{\mathrm{Haar}}(x).
$$

**Non-degeneracy.** Haar measure has full support. If $\langle f, \phi \rangle_A = 0$ for all $\phi \in A$, then $f = 0$ a.e., hence $f = 0$. The Peter–Weyl theorem provides an orthonormal basis of matrix coefficients $\{D^j_{mn}\}$ satisfying:

$$
  \langle D^j_{mn}, D^{j'}_{m'n'} \rangle_A
  =  \frac{1}{2j+1}\delta_{jj'}\delta_{mm'}\delta_{nn'}.
$$

The isomorphism $A \xrightarrow{\sim} A^{\vee}$ sends each basis element to its dual functional scaled by $1/(2j+1)$.

**Concrete calculation on $\mathbb{C}^2$.** The matrix generators of $\mathcal{O}(\mathrm{SU}(2))$ are $\alpha, \beta, \bar{\alpha}, \bar{\beta}$ with $|\alpha|^2 + |\beta|^2 = 1$. The spin-$\tfrac{1}{2}$ coefficients are $D^{1/2}_{mn} \in \{\alpha, \beta, -\bar{\beta}, \bar{\alpha}\}$. We compute:

$$
  \langle \alpha, \alpha \rangle_A = \tfrac{1}{2}, \qquad \langle \alpha, \beta \rangle_A = 0.
$$

The factor $\tfrac{1}{2}$ confirms the normalisation for spin $j = \tfrac{1}{2}$.

**The snake identity.** The coevaluation $\tilde{\eta} \colon \mathbf{1} \to A \otimes A$ sends $1 \mapsto \sum_{j,m,n} (2j+1)D^j_{mn} \otimes \overline{D^j_{mn}}$. The composite $A \xrightarrow{\mathrm{id} \otimes \tilde{\eta}} A \otimes A \otimes A \xrightarrow{(\int_A \circ \mu) \otimes \mathrm{id}} A$ acts as:

$$
  f  \longmapsto  \sum_{j,m,n} (2j+1)
  \langle f, D^j_{mn} \rangle_A \cdot \overline{D^j_{mn}} = f.
$$

This is $\mathrm{id}_A$, confirming non-degeneracy.
<!-- FILE_END: frobenius-pairing-su2.md -->

<!-- FILE_START: frobenius-geometric-role.md -->
The Frobenius structure on $A$ provides *integration* in the categorical calculus. The quantum universe pairs:

- **Differentiation**: the Kähler differentials $\Omega^1(A)$ measure infinitesimal change within $A$.
- **Integration**: the Frobenius form $\int_A \colon A \to \mathbf{1}$ assigns a scalar to each element of $A$.

Non-degeneracy of the [Frobenius pairing](#def:frobenius-pairing) means the measure is faithful: $\int_A ab = 0$ for all $b$ implies $a = 0$. Differentiation and integration make $A$ a self-contained laboratory for the categorical calculus.
<!-- FILE_END: frobenius-geometric-role.md -->

<!-- FILE_START: quantum-universe-su2.md -->
Continuing [rigid monoidal Vect](#ex:rigid-monoidal-vect), we verify the [quantum universe](#def:quantum-universe) axioms for $G = \mathrm{SU}(2)$.

**(i) Category.** $\mathbf{C} = \mathrm{Rep}(\mathrm{SU}(2))$ is the category of finite-dimensional complex representations. This is a $\mathbb{C}$-linear rigid :refterm[monoidal category]{#monoidal-category}. The $G$-action on tensor products is diagonal; on duals it is the contragredient.

**(ii) Frobenius--Hopf object.** $A = \mathcal{O}(\mathrm{SU}(2))$ is the coordinate ring. Its Hopf structure encodes the group operations (see [Table 1](#tbl:quantum-universe-su2-table1-data)). The [Frobenius pairing](#def:frobenius-pairing) is positive definite.

**(iii) Fibre functor.** $\tau \colon \mathrm{Rep}(\mathrm{SU}(2)) \to \mathrm{Vect}_{\mathbb{C}}$ is the forgetful functor. It is exact, faithful, and monoidal. By Tannaka--Krein duality, $G \cong \mathrm{Aut}^{\otimes}(\tau)$.

**(iv) Differential calculus.** The left-invariant calculus on $\mathrm{SU}(2)$ provides $\Omega^1(A) = \mathrm{span}\{\omega_1, \omega_2, \omega_3\}$. The universal derivation $d \colon A \to \Omega^1(A)$ acts by $df = \sum_i (\partial_i f) \omega_i$.
<!-- FILE_END: quantum-universe-su2.md -->

<!-- FILE_START: higher-forms.md -->
Let $(\mathbf{C}, A, \tau)$ be a [quantum universe](#def:quantum-universe) with differential calculus $\Omega^1(A)$. The **higher differential forms** are the graded $A$-bimodule:

$$
  \Omega^k(A) =  \bigwedge\nolimits_A^k \Omega^1(A), \qquad k = 0, 1, 2, \ldots
$$

Here $\Omega^0(A) = A$. For an object $V$, $\Lambda^k V$ denotes its $k$-th exterior power. The differential $d \colon \Omega^k(A) \to \Omega^{k+1}(A)$ extends the universal derivation by the graded Leibniz rule and satisfies $d^2 = 0$:

```tex
\begin{equation}\label{eq:de-rham-complex}
\begin{tikzcd}[column sep=2.5em]
  A = \Omega^0(A) \ar[r, "d"]
  & \Omega^1(A) \ar[r, "d"]
  & \Omega^2(A) \ar[r, "d"]
  & \cdots
\end{tikzcd}
\qquad (d^2 = 0)
\end{equation}
```
<!-- FILE_END: higher-forms.md -->

<!-- FILE_START: higher-forms-su2.md -->
On $A = \mathcal{O}(\mathrm{SU}(2))$, the left-invariant calculus has $\Omega^1(A) = \mathrm{span}\{\omega_1, \omega_2, \omega_3\}$. The group is three-dimensional, so the exterior tower truncates at $k = 3$:

- $\Omega^0(A) = A$
- $\Omega^1(A) = A \otimes \mathrm{span}\{\omega_1, \omega_2, \omega_3\}$
- $\Omega^2(A) = A \otimes \mathrm{span}\{\omega_1 \wedge \omega_2, \omega_1 \wedge \omega_3, \omega_2 \wedge \omega_3\}$
- $\Omega^3(A) = A \otimes \mathrm{span}\{\omega_1 \wedge \omega_2 \wedge \omega_3\}$
- $\Omega^k(A) = 0$ for $k \geq 4$.

The differential $d$ is determined by $d\omega_i = -\tfrac{1}{2} \epsilon_{ijk}\omega_j \wedge \omega_k$.
<!-- FILE_END: higher-forms-su2.md -->

<!-- FILE_START: fundamental-object-explication.md -->
We fix two pieces of notation, defined below: the [fundamental object](#def:fundamental-object) $V$ — the self-dual simple object of categorical dimension $2$ that tensor-generates $\mathbf{C}$ — and the [Tannaka dual](#def:tannaka-dual) $G = \mathrm{Aut}^{\otimes}(\tau)$, the gauge group emergent from the fibre functor $\tau$.
<!-- FILE_END: fundamental-object-explication.md -->

<!-- FILE_START: fundamental-object.md -->
Let $\mathbf{C}$ be an $R$-linear rigid :refterm[monoidal category]{#monoidal-category}. A **fundamental object** is an object $V \in \mathbf{C}$ equipped with a volume form
$$
  \epsilon \colon V \otimes V \longrightarrow \mathbf{1}
$$
— the categorical determinant $\Lambda^2 V \to \mathbf{1}$ — together with an adjoint coform $\eta \colon \mathbf{1} \to V \otimes V$ satisfying the two snake identities. Thus $\epsilon$ exhibits $V$ as its own dual: a *symplectic self-dual object*, the datum that distinguishes $\mathrm{SL}_2 / \mathrm{SU}(2)$ from $\mathrm{GL}_2$ \cite{deligne1990}.

Under a fibre functor the volume constraint forces $\mathrm{rank}(V) = 2$, so $V$ is simple of categorical dimension $2$: in $\mathrm{SU}(2)$ it is $V = V_{1/2} \cong \mathbb{C}^2$, every other simple object is an exterior or symmetric power of $V$, and $V$ tensor-generates $\mathbf{C}$ (see the [role of $V$](#rem:simple-objects-V)).
<!-- FILE_END: fundamental-object.md -->

<!-- FILE_START: tannaka-dual.md -->
The gauge group emerges from the pair $(\mathbf{C}, \tau)$. Let $\tau \colon \mathbf{C} \to R\text{-}\mathrm{Mod}$ be the fibre functor. A symmetry is a family of $R$-module automorphisms compatible with the tensor product — a monoidal natural automorphism of $\tau$. The **Tannaka dual**, or emergent gauge group,
$$
  G \;=\; \mathrm{Aut}^{\otimes}(\tau)
$$
collects these families. When $(\mathbf{C}, \tau)$ is neutral Tannakian in the sense of Deligne, $G$ is an affine group scheme over $R$ and the reconstruction $\mathbf{C} \simeq \mathrm{Rep}(G)$ holds \cite{deligne1990}.
<!-- FILE_END: tannaka-dual.md -->

<!-- FILE_START: simple-objects-V.md -->
Simple objects are the irreducible building blocks of a rigid :refterm[monoidal category]{#monoidal-category} $\mathbf{C}$. An object $X$ is simple if every monomorphism into $X$ is zero or an isomorphism.

The faithful, exact functor $\tau$ reflects simplicity: $X$ is simple if and only if $\tau(X)$ is a simple module. The fundamental object $V$ is distinguished by two properties:

1. **Categorical dimension $2$**: $\tau(V)$ is a rank-$2$ free module.
2. **Tensor generation**: Every simple object appears as a direct summand of some tensor power $V^{\otimes n}$.

These properties make $V$ the natural carrier for vectors.
<!-- FILE_END: simple-objects-V.md -->

<!-- FILE_START: unit-simplicity.md -->
Choosing a specific volume form $\epsilon$ fixes a fundamental unit of volume. The volume form is canonical up to a scalar because the unit object $\mathbf{1}$ is simple.

The space of non-degenerate volume forms $\mathrm{Hom}(\Lambda^2 V, \mathbf{1})$ is one-dimensional over $R$. This follows because $\mathrm{End}(\mathbf{1}) \cong R$. Thus, any other non-degenerate epimorphism $\epsilon'$ satisfies $\epsilon' = c\epsilon$ for some unit $c \in R^{\times}$.

Once chosen, the gauge symmetries lock it in place. The volume $\epsilon$ is a structural morphism intrinsic to the observable universe.
<!-- FILE_END: unit-simplicity.md -->

