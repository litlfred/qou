<!-- FILE_START: quantum-universe-frobenius-pairing-unique-intro.md -->
Pinning the Frobenius pairing on the QU fundamental object $A$ is
what makes the $\mathrm{SU}(2)$ realisation canonical: once the
pairing is shown to be unique, its explicit $\mathrm{SU}(2)$ form is
forced, and every downstream construction that consumes the pairing
inherits a single fixed choice rather than a family of options.

The preceding sub-section set up the pairing; this sub-section proves
it unique and exhibits the $\mathrm{SU}(2)$ realisation that pins it.
The arc proceeds through:

1. the uniqueness proof for the pairing on $A$;
2. the explicit $\mathrm{SU}(2)$ pairing realisation;
3. the geometric role the pairing plays in the substrate-flow;
4. the canonical $\mathrm{SU}(2)$ QU explication together with its
   table data;
5. the higher-forms identification (generic plus the
   $\mathrm{SU}(2)$ specialisation) that the next sub-section
   consumes.
<!-- FILE_END: quantum-universe-frobenius-pairing-unique-intro.md -->

<!-- FILE_START: frobenius-pairing-unique.md -->
The Frobenius pairing is canonical up to overall scale.  Let
$(\mathbf{C}, A, \tau)$ be a
[quantum universe](#def:quantum-universe) with $A$ simple.  Any two
non-degenerate Frobenius forms $\int_A^{(1)}, \int_A^{(2)}$ on $A$
differ by an invertible scalar:

$$
  \int_A^{(2)} \;=\; c  \int_A^{(1)}
  \qquad\text{for some } c \in \mathrm{Aut}_{\mathbf{C}}(\mathbf{1}).
$$

Consequently the induced pairings
$\langle \cdot, \cdot \rangle_i = \int_A^{(i)} \circ \mu$, where $\mu$
is the multiplication of $A$, differ by the same scalar, and the
[Frobenius pairing](#def:frobenius-pairing) is unique up to global
normalisation.
<!-- FILE_END: frobenius-pairing-unique.md -->

<!-- FILE_START: frobenius-pairing-su2.md -->
Continuing the SU(2) example
([quantum universe on SU(2)](#ex:quantum-universe-su2)), we make
the Frobenius pairing concrete.

Set $A = \mathcal{O}(\mathrm{SU}(2))$ with pointwise multiplication
$\mu(f \otimes g) = fg$ and Frobenius form
$\int_A f = \int_{\mathrm{SU}(2)} f(x)\,d\mu_{\mathrm{Haar}}(x)$
(the Haar integral).  The Frobenius pairing is the composite

$$
  \langle f, g \rangle_A
  =  \int_A \!\circ \mu(f \otimes g)
  =  \int_{\mathrm{SU}(2)} f(x)g(x)\,d\mu_{\mathrm{Haar}}(x).
$$

This is the $L^2$ inner product on SU(2).

**Non-degeneracy.**  The pairing is non-degenerate because Haar
measure on a compact group has full support: if
$\langle f, \phi \rangle_A = 0$ for all $\phi \in A$, then $f = 0$ a.e.,
hence $f = 0$ in $A$.  Equivalently, the Peter–Weyl theorem gives
an orthonormal basis of matrix coefficients
$\{D^j_{mn}\}_{j \in \frac{1}{2}\mathbb{Z}_{\geq 0}}$ satisfying

$$
  \langle D^j_{mn}, D^{j'}_{m'n'} \rangle_A
  =  \frac{1}{2j+1}\delta_{jj'}\delta_{mm'}\delta_{nn'}.
$$

The isomorphism $A \xrightarrow{\sim} A^{\vee}$ sends each basis
element to its dual functional scaled by $1/(2j+1)$.

**Concrete calculation on $\mathbb{C}^2$.**  The matrix generators
of $\mathcal{O}(\mathrm{SU}(2))$ are
$\alpha, \beta, \bar{\alpha}, \bar{\beta}$ with
$|\alpha|^2 + |\beta|^2 = 1$.  The spin-$\tfrac{1}{2}$
matrix coefficients are $D^{1/2}_{mn} \in \{\alpha, \beta, -\bar{\beta}, \bar{\alpha}\}$.  We compute:

$$
  \langle \alpha, \alpha \rangle_A
  =  \int_{\mathrm{SU}(2)} |\alpha|^2d\mu
  =  \tfrac{1}{2},
  \qquad
  \langle \alpha, \beta \rangle_A
  =  \int_{\mathrm{SU}(2)} \alpha\beta\,d\mu
  =  0.
$$

The factor $\tfrac{1}{2} = 1/(2 \cdot \tfrac{1}{2} + 1)$ confirms
the Peter–Weyl normalisation for spin $j = \tfrac{1}{2}$.

**The snake identity** (non-degeneracy in categorical language):
the coevaluation $\tilde{\eta} \colon \mathbf{1} \to A \otimes A$
sends $1 \mapsto \sum_{j,m,n} (2j+1)D^j_{mn} \otimes \overline{D^j_{mn}}$.  The composite
$A \xrightarrow{\mathrm{id} \otimes \tilde{\eta}} A \otimes A \otimes A \xrightarrow{(\int_A \circ \mu) \otimes \mathrm{id}} A$ acts as

$$
  f  \longmapsto  \sum_{j,m,n} (2j+1)
  \langle f, D^j_{mn} \rangle_A \cdot \overline{D^j_{mn}}
  =  f,
$$

by Peter–Weyl completeness.  This is $\mathrm{id}_A$, confirming
non-degeneracy.
<!-- FILE_END: frobenius-pairing-su2.md -->

<!-- FILE_START: frobenius-geometric-role.md -->
The Frobenius structure on $A$ plays the role of *integration* in
the categorical calculus of the quantum universe. Just as classical
analysis rests on two pillars — differentiation and integration — the
quantum universe pairs:

- **Differentiation**: the Kähler differentials $\Omega^1(A)$, which
  measure infinitesimal change within $A$;

- **Integration**: the Frobenius form
  $\int_A \colon A \to \mathbf{1}$, which assigns to each
  element of $A$ a scalar in $\mathbf{1}$.

The non-degeneracy of the Frobenius pairing
([Frobenius pairing](#def:frobenius-pairing)) is the categorical
analogue of a measure being faithful: $\int_A ab = 0$ for all $b$
implies $a = 0$. Together, differentiation and integration make
$A$ into a self-contained laboratory for the categorical
calculus.  The volume form $\epsilon$
constructed from this pairing in
[Chapter 2](#chap:qou) completes the picture.
<!-- FILE_END: frobenius-geometric-role.md -->

<!-- FILE_START: quantum-universe-su2.md -->
Continuing [rigid monoidal Vect](#ex:rigid-monoidal-vect), we verify each axiom
of [quantum universe](#def:quantum-universe) for $G = \mathrm{SU}(2)$.

**(i) Category.**
$\mathbf{C} = \mathrm{Rep}(\mathrm{SU}(2))$, the category of
finite-dimensional complex representations. Objects are vector spaces
$V$ with a continuous $G$-action $\rho_V \colon G \to \mathrm{GL}(V)$;
morphisms are $G$-equivariant linear maps. This is a
$\mathbb{C}$-linear rigid :refterm[monoidal category]{#monoidal-category}
([rigid monoidal Vect](#ex:rigid-monoidal-vect)). The $G$-action on tensor
products is diagonal: $g \cdot (v \otimes w) = (g \cdot v) \otimes (g \cdot w)$; on duals it is the contragredient:
$(g \cdot f)(v) = f(g^{-1} \cdot v)$.

**(ii) Frobenius--Hopf object.**
$A = \mathcal{O}(\mathrm{SU}(2))$, the coordinate ring of polynomial
functions on the group. Its Hopf structure encodes the group operations:

See [Table 1](#tbl:quantum-universe-su2-table1-data).

The [Frobenius pairing](#def:frobenius-pairing)
$\langle f, g \rangle = \int_A(\mu(f \otimes g)) = \int_G f(x) g(x) d\mu_{\mathrm{Haar}}(x)$
is positive definite (faithfulness of the Haar integral).

**(iii) Fibre functor.**
$\tau \colon \mathrm{Rep}(\mathrm{SU}(2)) \to \mathrm{Vect}_{\mathbb{C}}$ is the forgetful functor: $\tau(V, \rho) = V$ (forget the $G$-action, keep the vector space). It is exact
(short exact sequences of representations split), faithful (a non-zero
equivariant map is non-zero as a linear map), and monoidal
($\tau(V \otimes W) = \tau(V) \otimes \tau(W)$).
By Tannaka--Krein duality, $G$ can be recovered from $\tau$:
$G \cong \mathrm{Aut}^{\otimes}(\tau)$, the group of monoidal natural
automorphisms of the fibre functor.

**(iv) Differential calculus.**
The left-invariant calculus on $\mathrm{SU}(2)$ provides
$\Omega^1(A) = \mathrm{span}\{\omega_1, \omega_2, \omega_3\}$,
the left-invariant $1$-forms dual to the Lie algebra basis
$\{e_1, e_2, e_3\}$ of $\mathfrak{su}(2)$ (with
$[e_a, e_b] = \epsilon_{abc} e_c$;
[SU(2) basis](#def:su2-basis)).
The universal derivation $d \colon A \to \Omega^1(A)$
acts by $df = \sum_i (\partial_i f) \omega_i$, recovering the
Lie derivative along each generator.
<!-- FILE_END: quantum-universe-su2.md -->

<!-- FILE_START: higher-forms.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum universe with differential
calculus $\Omega^1(A)$ ([quantum universe](#def:quantum-universe)). To
assemble a graded differential calculus — the setting in which curvature
and de Rham cohomology are later defined — the first-order forms
$\Omega^1(A)$ must be extended to forms of every degree. The
**higher differential forms** are the graded $A$-bimodule

$$
  \Omega^k(A) =  \bigwedge\nolimits_A^k \Omega^1(A),
  \qquad k = 0, 1, 2, \ldots
$$

(exterior powers of the $A$-bimodule $\Omega^1(A)$ in $\mathbf{C}$),
with $\Omega^0(A) = A$ and $\Omega^1(A)$ the first-order forms already in
hand; the $\mathrm{SU}(2)$ instance is worked out in the
[higher-forms example](#ex:higher-forms-su2). For an object $V$ in $\mathbf{C}$,
$\Lambda^k V$ denotes the $k$-th exterior power of $V$ in the sense
of rigid monoidal categories. The differential
$d \colon \Omega^k(A) \to \Omega^{k+1}(A)$ extends the universal
derivation by the graded Leibniz rule, and satisfies $d^2 = 0$.

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
Continuing [quantum universe on SU(2)](#ex:quantum-universe-su2), the left-invariant
calculus on $A = \mathcal{O}(\mathrm{SU}(2))$ has
$\Omega^1(A) = \mathrm{span}\{\omega_1, \omega_2, \omega_3\}$
(three left-invariant $1$-forms, dual to the Lie algebra
$\mathfrak{su}(2) = \mathrm{span}\{e_1, e_2, e_3\}$). This example
realizes [def:higher-forms](#def:higher-forms) concretely: because the
group is three-dimensional, the exterior tower is finite and truncates
at the top degree $k = 3$. Ascending through it degree by degree, the
higher forms are:

- $\Omega^0(A) = A = \mathcal{O}(\mathrm{SU}(2))$ (functions on the group).
- $\Omega^1(A) = A \otimes \mathrm{span}\{\omega_1, \omega_2, \omega_3\}$
  (left-invariant $1$-forms, dimension $3$ over $A$).
- $\Omega^2(A) = A \otimes \mathrm{span}\{\omega_1 \wedge \omega_2, \omega_1 \wedge \omega_3, \omega_2 \wedge \omega_3\}$
  (dimension $3$ over $A$).
- $\Omega^3(A) = A \otimes \mathrm{span}\{\omega_1 \wedge \omega_2 \wedge \omega_3\}$ (the volume form, dimension $1$ over $A$).
- $\Omega^k(A) = 0$ for $k \geq 4$.

The top degree $\Omega^3(A)$ carries the single invariant volume form,
and the differential $d$ closes the tower: it is determined by
$d\omega_i = -\tfrac{1}{2} \epsilon_{ijk}\omega_j \wedge \omega_k$ (the
Maurer--Cartan equation of $\mathfrak{su}(2)$).
<!-- FILE_END: higher-forms-su2.md -->

<!-- FILE_START: fundamental-object-explication.md -->
We fix two pieces of notation that will appear throughout.

**The fundamental object $V$.**
In a rigid :refterm[monoidal category]{#monoidal-category} $\mathbf{C}$, a volume constraint — a
non-degenerate epimorphism $\epsilon \colon \Lambda^2 V \to \mathbf{1}$,
introduced in [Chapter 2](#chap:qou) — forces
$\mathrm{rank}(V) = 2$.  (If $\mathrm{rank}(V) = 1$ then
$\Lambda^2 V = 0$ and no such epimorphism exists; if
$\mathrm{rank}(V) \geq 3$ then
$\mathrm{rank}(\Lambda^2 V) \geq 3$ and the non-degenerate
epimorphism to the rank-$1$ unit object $\mathbf{1}$ cannot exist.)
In the SU(2) example
([Example](#ex:rigid-monoidal-vect)), the object this singles out is
$V = V_{1/2} \cong \mathbb{C}^2$, the defining
(spin-$\tfrac{1}{2}$) representation. Abstractly, then, the
*fundamental object* $V$ is the unique (up to isomorphism) simple
object of categorical dimension $2$ — a dimension that is not an
independent assumption but a consequence of the constraint. Every
other simple object $V_j$ is an exterior or symmetric power of $V$, so
$V$ generates $\mathbf{C}$ as a tensor category.

**The emergent gauge group $G = \mathrm{Aut}^{\otimes}(\tau)$.**
No group is postulated *a priori*; the gauge group *emerges* from
$(\mathbf{C}, \tau)$. Let $\tau \colon \mathbf{C} \to R\text{-}\mathrm{Mod}$
be the forgetful functor. Concretely, a symmetry is a family of
$R$-module automorphisms
$\{g_X \colon \tau(X) \xrightarrow{\sim} \tau(X)\}_{X \in \mathbf{C}}$
compatible with the tensor product; the *tensor automorphism group*
$G = \mathrm{Aut}^{\otimes}(\tau)$ collects all such families — the
monoidal natural automorphisms of $\tau$. By Tannaka--Krein duality,
$G$ is an affine group scheme over $R$, and $\tau$ establishes a
monoidal equivalence $\mathbf{C} \simeq \mathrm{Rep}(G)$.
<!-- FILE_END: fundamental-object-explication.md -->

<!-- FILE_START: simple-objects-V.md -->
The simple objects are the irreducible building blocks of a rigid
:refterm[monoidal category]{#monoidal-category} $\mathbf{C}$ with a fibre functor
$\tau \colon \mathbf{C} \to R\text{-}\mathrm{Mod}$: every object of
$\mathbf{C}$ admits a filtration whose successive quotients are simple.
Concretely, an object $X$ is
*simple* if every monomorphism into $X$ is either zero or an isomorphism.

Because $\tau$ is faithful and exact, it reflects simplicity: $X$ is
simple in $\mathbf{C}$ if and only if $\tau(X)$ is a simple module.
When $R$ is a field, the simple modules are precisely the irreducible
representations of the emergent gauge group
$G = \mathrm{Aut}^{\otimes}(\tau)$.

The fundamental object $V$ is
distinguished among the simples by two properties:

1. **Categorical dimension $2$**: $\tau(V)$ is a rank-$2$ free
   $R$-module, the smallest non-trivial rank compatible with the
   volume constraint $\epsilon \colon \Lambda^2 V \to \mathbf{1}$.
2. **Tensor generation**: every simple object $V_j$ appears as a
   direct summand of some tensor power $V^{\otimes n}$, so the
   entire category $\mathbf{C}$ is generated by $V$ under tensor
   products and direct sums.

These two properties make $V$ the natural carrier for vectors in the
theory: any "vector-valued" quantity is a morphism into a tensor power
of $V$.
<!-- FILE_END: simple-objects-V.md -->

<!-- FILE_START: unit-simplicity.md -->
Choosing a specific volume form $\epsilon$ amounts to fixing a
fundamental unit of volume for the theory, so what matters is how
much freedom that choice carries. The answer is that $\epsilon$ is
canonical up to a single scalar, and the reason is that the unit
object $\mathbf{1}$ is *simple*.

Concretely, the non-degenerate volume forms
$\mathrm{Hom}(\Lambda^2 V, \mathbf{1})$ occupy a single
one-dimensional line over the base ring $R$. This is a Schur-type
principle: because $\mathbf{1}$ is simple, its endomorphism ring is
the base ring, $\mathrm{End}(\mathbf{1}) \cong R$. This forces the space of
morphisms $\mathrm{Hom}(\Lambda^2 V, \mathbf{1})$ to be
one-dimensional over $R$.

Consequently, if $\epsilon' \colon \Lambda^2 V \twoheadrightarrow \mathbf{1}$ is any other non-degenerate epimorphism, then
$\epsilon' = c\epsilon$ for some unit $c \in R^{\times}$.
Once this baseline scale is chosen, the gauge symmetries
$g \in \mathrm{Aut}^{\otimes}(\tau)$ lock it in place via the
commutativity constraint
([categorical volume constraint](#eq:categorical-volume-constraint)).

This structure anchors the topological invariants directly within
the categorical data $(\mathbf{C}, A, \tau)$: the volume
$\epsilon$ arises not as an external parameter but as a structural
morphism intrinsic to the observable universe.
<!-- FILE_END: unit-simplicity.md -->

