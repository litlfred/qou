<!-- FILE_START: braiding-conventions-intro.md -->
The substrate parameter $q$, the imaginary unit $i$,
and the ribbon twist $v = q^{1/2}$ are bound by sign and
orientation choices that are entirely separable from the
content-bearing axioms of the QOU. We collect them in one place
so that the rest of the chapter can refer to a single convention.

Remark: Inside-unit-circle labelling of the braiding eigenvalue records the convention that fixes $q := \lambda_+$ (the
$S^2 V$ eigenvalue), justified by the positivity axiom and
compatibility with the standard Kauffman orientation.
Remark: $\sqrt q$ as ribbon datum places the formal square
root $v = q^{1/2}$ in $\mathbb{Q}(q^{1/2})$ and reads the
ribbon twist $\varTheta_V = q^{1/2}\,\mathrm{id}_V$ on the
defining representation. Remark: The binary sign of $\sqrt q$ as spin structure records that the choice $v$ vs $-v$,
once $q$ is fixed to a numerical value, is the spin structure
on the resulting worldline.

Remark: The imaginary unit $i$ as braiding-orientation datum
collects the three faces of $i$ — Wick rotation, CR complex
structure $J$, and arrow-of-time orientation under $\prec_c$ —
and identifies them as a single $\mathbb{Z}_2$ choice on the
braiding $c_{V,V}$ versus $c_{V,V}^{-1}$.
Remark: Affine-chart origin of $i$ and $q$ traces both
coordinates to the chart-transition data of $\mathbb{P}(V)$:
$q$ appears as the chart-transition coefficient $zw = q^{-1}$
in the deformed case, $i$ as the square root of the chart-swap
involution in the commutative case.
Proposition: The categorical-coordinate ring $R[i, q^{\pm 1}]$ of chart-transition data, with its proof, packages this
as the smallest $R$-algebra extension in which both data are
universally available — characterised by a chart-transition
universal property and the semidirect-product factorisation
$\langle q \rangle \rtimes \langle \iota \rangle$ of the
chart-transition automorphism group. The next section,
**Elaboration: categorical context**, opens the elaboration
material and treats TQFT, Levi-form generalisations, and the
$j^1$ local-state machinery.

_(draft.)_
<!-- FILE_END: braiding-conventions-intro.md -->

<!-- FILE_START: braiding-unit-circle-convention.md -->
Proposition~[braiding-eigenvalue-extraction](#prop:braiding-eigenvalue-extraction)
extracts $q$ from the eigenvalues of $c_{V,V}$ and assigns
$q := \lambda_+$ (the eigenvalue on the symmetric summand $S^2 V$).
This labelling is a **convention**: one could equally define
$q := \lambda_- = -q^{-1}$. The present choice is the
**inside-unit-circle convention**.

**Choice of $\lambda_+$ over $\lambda_-$.** The
[substrate parameter existence](#thm:substrate-parameter-exists)
proof requires $q > 1$ over $\mathbb{R}$ (the `field_ge_one`
positivity axiom). Under the Hecke relation
$(T - q)(T + q^{-1}) = 0$, the eigenvalue $\lambda_+= q$ lies
*outside* the unit circle when $q > 1$, while $\lambda_- = -q^{-1}$
lies inside. Defining $q := \lambda_+$ is therefore equivalent to
choosing the eigenvalue of larger absolute value — the one that
controls the asymptotic growth of the braiding representation.

**Effect on the Hecke relation.** The two eigenvalues satisfy
$\lambda_+ \cdot \lambda_- = -1$ (determinant condition), so
swapping them replaces $q$ by $-q^{-1}$. The Hecke relation
$(T-q)(T+q^{-1}) = 0$ is manifestly asymmetric in $\lambda_+$
and $\lambda_-$; the choice $q := \lambda_+$ is the one that
makes the symmetric summand eigenvalue positive (for real $q > 1$)
and compatible with the standard orientation of the Kauffman bracket.

**No mathematical content changes.** This is a naming convention:
the braiding endomorphism $c_{V,V}$ and the Hecke relation are fixed
by the category. Choosing $q := \lambda_+$ fixes which of the
two eigenvalues receives the name ``$q$'', consistently with the
[substrate parameter](#def:substrate-parameter) and the physical
positivity axiom.
<!-- FILE_END: braiding-unit-circle-convention.md -->

<!-- FILE_START: sqrt-q-ribbon-structure.md -->
The braiding eigenvalues
([braiding-eigenvalue-extraction](#prop:braiding-eigenvalue-extraction))
are $q$ and $-q^{-1}$; neither involves $q^{1/2}$.  The element
$v := q^{1/2}$ is *post-Archimedean naming*: pre-Archimedean it is a
formal adjoined square root in the splitting field $\mathbb{Q}(q^{1/2})$
and carries no geometric content; post-Archimedean (after the
realization functor at $q_0$) it becomes the real number $q_0^{1/2}$,
and the binary sign choice is the spin structure on the realized
worldline (see [sign-as-spin-structure](#rem:sign-as-spin-structure)).

A *ribbon structure* on $\mathbf{C}$ is a natural twist
$\varTheta_V \colon V \xrightarrow{\sim} V$ satisfying
$\varTheta_{V \otimes W} = (c_{W,V} \circ c_{V,W}) \circ (\varTheta_V \otimes \varTheta_W)$
and $\varTheta_{V^\vee} = (\varTheta_V)^\vee$.  By Schur, on a simple
object the twist is a scalar; combining the twist axiom with the Hecke
eigenvalues $(q, -q^{-1})$ forces this scalar to $\pm q^{1/2}$, so on
the defining $\mathrm{SU}_q(2)$ representation
$\varTheta_V = q^{1/2}\,\mathrm{id}_V$.

The ribbon datum is post-Archimedean: it is needed exactly when the
realization target carries a framing — e.g.\ for the Reshetikhin--Turaev
functor ([tqft-context](#rem:tqft-context)) or for an MTC structure on
$\mathrm{Rep}(\mathbf{C})$ — and so it does not enter the QOU core
axioms ([quantum-observable-universe](#def:quantum-observable-universe)).
<!-- FILE_END: sqrt-q-ribbon-structure.md -->

<!-- FILE_START: sign-as-spin-structure.md -->
Once a ribbon structure is fixed
([sqrt-q-ribbon-structure](#rem:sqrt-q-ribbon-structure)), the relation
$v^2 = q$ determines $v = q^{1/2}$ only up to sign.  Post-Archimedean
(after the realization functor at $q_0$), this binary sign is the
spin structure on the realized worldline.  This datum is independent
of the braiding-orientation convention
([braiding-unit-circle-convention](#rem:braiding-unit-circle-convention));
the two choices index the framing and the orientation respectively.
<!-- FILE_END: sign-as-spin-structure.md -->

<!-- FILE_START: i-as-braiding-orientation.md -->
The imaginary unit $i$ appears in three distinct but related contexts
in the QOU framework.  Each appearance is, in reality, the same
underlying datum: the **orientation of the braiding**
$c_{V,V}$ versus $c_{V,V}^{-1}$.

**Algebraic face (Wick rotation).**
The [Wick-rotation remark](#rem:laplace-fourier-wick-rotation)
identifies $i$ in the Fourier grouplike pairing
$\exp_q(i\xi\,\cdot)$ with the complex-time rotation
$t \mapsto it$ that converts the Laplace half-plane into the Fourier
half-plane.  This rotation is **orientation-dependent**: replacing
$i$ with $-i$ swaps the two half-planes (Laplace $\leftrightarrow$
Fourier), reversing the direction of complex-time evolution.

**Geometric face (CR complex structure).**
The [linearisation convention](#sec:linearisation-convention) identifies
$i$ with the CR complex structure operator
$J \colon H \to H$ ($J^2 = -\mathrm{Id}$) on the Levi distribution.
The operator $J$ is determined by the contact form up to an overall
sign: choosing $+J$ or $-J$ is a choice of **CR orientation**.  This
sign choice is identical to the braiding-orientation choice encoded in
[braiding-induced ordering](#prop:braiding-induced-ordering):
$c_{V,V}$ (positive crossing, forward time) versus
$c_{V,V}^{-1}$ (negative crossing, reverse time).

**Combinatorial face (arrow of time).**
[Proposition~braiding-induced-ordering](#prop:braiding-induced-ordering)
establishes that $c_{V,V}$ (positive crossing) defines "forward time"
in the Hecke basis ordering $\prec_c$, while $c_{V,V}^{-1}$ reverses
this ordering.  Negating $i$ in either of the above faces
($i \mapsto -i$ in the Wick rotation, $J \mapsto -J$ in the CR
structure) is equivalent to flipping crossing orientation
($c_{V,V} \leftrightarrow c_{V,V}^{-1}$), which is time reversal
(the T component of CPT symmetry).

**Summary.**  The three faces — algebraic, geometric, combinatorial —
are three manifestations of a single binary choice: the orientation of
$c_{V,V}$.  Fixing $i$ (rather than $-i$) as the Wick-rotation factor
is the same convention as fixing $c_{V,V}$ (rather than $c_{V,V}^{-1}$)
as the positive crossing — the arrow of time for the QOU.
<!-- FILE_END: i-as-braiding-orientation.md -->

<!-- FILE_START: affine-chart-origin-of-i-and-q.md -->
**Remark (affine-chart origin of $i$ and $q$).**
Both categorical coordinates of [$\mathbb{P}(V)$](#def:projective-line-object)
arise from a single piece of data — the **transition between two
affine charts** — but in two distinct regimes of the deformation
family.  The Reeb chart of [contact affine chart](#def:contact-affine-chart)
is one of two natural affine charts; the other is the antipodal chart
swapped by the polar involution.  Writing $z$ for the affine
coordinate on $U_0$ and $w$ for the antipodal chart $U_1$, the
transition on $U_0 \cap U_1$ is

$$
  z \cdot w  =  \kappa,
$$

with the *categorical coordinate* $\kappa$ recording the chart-glue
data.

**Quantum case: $\kappa = q^{-1}$.**  For
$\mathbb{P}_q(V) = G_q/T_q$ ([quantum gauge group](#def:quantum-gauge-group))
the fibre-functor image $\mathcal{O}_q(\mathbb{P}^1)$ has generators
$x, y$ satisfying the quantum-plane relation $yx = q\,xy$.  The
two affine charts are

$$
  z  =  y x^{-1}\;\text{on}\; U_0, \qquad
  w  =  x y^{-1}\;\text{on}\; U_1,
$$

and the chart-transition coefficient is

$$
  z\,w  =  y x^{-1} \cdot x y^{-1}  =  q^{-1},
$$

so $q$ is *literally the chart-transition coefficient* on
$\mathbb{P}_q(V)$, in agreement with the eigenvalue extraction of
[braiding-eigenvalue-extraction](#prop:braiding-eigenvalue-extraction)
under the convention
[$q := \lambda_+$](#rem:braiding-unit-circle-convention).

**Commutative case: $\kappa = 1$ collapses, $i$ from chart-swap.**  At
$q = 1$ ([commutative QOU](#def:commutative-qou)) the chart-transition
$z w = 1$ becomes the classical inversion, and the categorical
coordinate degenerates: $\kappa - \kappa^{-1} = 0$.  The chart-swap
involution

$$
  \iota \colon  z  \longmapsto  z^{-1}, \qquad \iota^2 = \mathrm{id},
$$

generates a $\mathbb{Z}_2$ in $\mathrm{Aut}(\mathbb{P}(V))$.  Its
linearisation on $T_p\mathbb{P}(V)$ at any fixed point ($z = \pm 1$)
acts by $-1$.  Recovering a continuous categorical coordinate requires
a *square root of $\iota$*: a one-parameter family
$\rho_\varTheta\colon z \mapsto e^{i\varTheta} z$ with $\rho_\pi = \iota$
and $\rho_{\pi/2}$ the *quarter-turn between the two charts*.  The
quarter-turn generator is

$$
  \rho_{\pi/2}  =  i \cdot \mathrm{id}_V \in \mathrm{End}_{R[i]}(V),
$$

and this is the categorical coordinate $i = \sqrt{\lambda_-}$.  The
square root resides in $R[i]$ rather than $R$ for exactly the same
reason that $z w = q^{-1}$ does not collapse to $z w = 1$ in the
quantum case: a non-trivial chart-transition is the carrier of the
categorical coordinate.

**Same construction, two regimes.**

| Object | Chart transition | Categorical coordinate |
|--------|------------------|-----------------------|
| $\mathbb{P}_q(V)$ | $z\,w = q^{-1}$ (continuous deformation) | $q \in \mathrm{End}_R(\mathbf{1})$ |
| $\mathbb{P}(V)$ at $q=1$ | $z\,w = 1$, $\iota: z \mapsto z^{-1}$ ($\mathbb{Z}_2$) | $i = \sqrt{\iota|_{T_p}} \in \mathrm{End}_{R[i]}(\mathbf{1})$ |
| $\mathbb{P}(V)$ over $R[i]$ | $z\,w = 1$, $\rho_\varTheta: z \mapsto e^{i\varTheta} z$ ($\mathrm{U}(1)$) | $i$ as quarter-turn generator |

The hierarchy of the categorical-coordinate group is therefore an
expansion of chart-transition automorphisms,

$$
  \underbrace{\mathbb{Z}_2}_{\iota,\;\text{chart-swap}}
  \;\hookrightarrow\;
  \underbrace{\mathbb{Z}_4}_{\iota,\;\pm i}
  \;\hookrightarrow\;
  \underbrace{\mathrm{U}(1)}_{\rho_\varTheta,\;\text{rotation}}
  \;\hookrightarrow\;
  \underbrace{\mathrm{U}_q(1)}_{q\text{-deformation}},
$$

with each inclusion adding one more layer of chart-transition
automorphism.

**Choice up to sign.**  The two square roots $\pm i$ of $\iota$
correspond to the two ways of orienting the quarter-turn;
$\mathbb{P}(V)$ determines the unordered pair $\{+i, -i\}$ but not
the element.  The Galois action $\mathrm{Gal}(R[i]/R) = \mathbb{Z}_2$
exchanging $\pm i$ is the same $\mathbb{Z}_2$ as the braiding
orientation choice $c_{V,V} \leftrightarrow c_{V,V}^{-1}$ of
[i as braiding orientation](#rem:i-as-braiding-orientation): the
sign ambiguity in the chart-transition square root *is* the
arrow-of-time choice.
<!-- FILE_END: affine-chart-origin-of-i-and-q.md -->

<!-- FILE_START: reeb-u1-chart-swap.md -->
**Proposition (chart-swap $U(1)$ equals the Reeb $U(1)$).**
Let $(\mathbf{C}, A, \tau)$ be a
[quantum observable universe](#def:quantum-observable-universe)
with maximal torus $T_q = U_q(1) \subset G_q = \mathrm{SU}_q(2)$
acting on the fundamental object $V$ via the standard weight
decomposition, let $\mathbb{P}(V)$ be the
[projective line object](#def:projective-line-object), and let
$\xi \in \mathrm{Der}(A)$ be the
[categorical Reeb derivation](#thm:categorical-reeb-exists).
Then as subgroups of $\mathrm{Aut}_{\mathbf{C}}(\mathbb{P}(V))$:

$$
  \underbrace{\langle \rho_\varTheta : \varTheta \in U(1) \rangle}_{\text{chart-swap}}
  \;=\;
  \underbrace{\langle \phi_t : t \in \mathbb{R} \rangle}_{\text{Reeb flow}}
  \;=\;
  T_q,
$$

(The chart-swap one-parameter subgroup originates in
[`rem:affine-chart-origin-of-i-and-q`](#rem:affine-chart-origin-of-i-and-q);
the Reeb flow subgroup originates in
[`thm:categorical-reeb-exists`](#thm:categorical-reeb-exists).)

i.e. both one-parameter families of automorphisms are the image of
the maximal torus $T_q$ under the standard $T_q$-action on
$\mathbb{P}(V) = G_q / T_q$.
<!-- FILE_END: reeb-u1-chart-swap.md -->

<!-- FILE_START: reeb-u1-five-roles.md -->
## Consequences (five roles, one $U(1)$)

The proposition fixes which $U(1)$ plays which role: the
categorical framework does not need to invent a separate $U(1)$ for
the Wick rotation, for the imaginary unit $i$, for the chart-swap,
or for the framing of knot operators. All five roles inherit from
the maximal torus $T_q$ of the substrate $G_q$:

| Role | Action on $Z$ | Subgroup / regime |
|------|---------------|-------------------|
| Antipodal involution ($\rho_\pi$ — linearisation of chart-swap $\iota : z \mapsto z^{-1}$ at the fixed point, per [`rem:affine-chart-origin-of-i-and-q`](#rem:affine-chart-origin-of-i-and-q)) | $\rho_\pi : Z \mapsto -Z$ | $\mathbb{Z}_2$ at $\varTheta = \pi$ |
| Imaginary unit $i$ | $\rho_{\pi/2}$ (quarter-turn) | $\mathbb{Z}_4$ |
| Wick rotation | $\rho_\varTheta$, $\varTheta \in [0, \pi/2]$ | full $U(1)$, continuous |
| Reeb flow $\phi_t$ | $Z \mapsto e^{-t} Z$ | generated by $\xi$ |
| $q$-deformation | $\rho_\varTheta$ off the unit circle | $U_q(1)$ |

The $\mathbb{Z}_2 \hookrightarrow \mathbb{Z}_4 \hookrightarrow U(1)
\hookrightarrow U_q(1)$ hierarchy of
[affine-chart origin of $i$ and $q$](#rem:affine-chart-origin-of-i-and-q)
is therefore the same Reeb $U(1)$ viewed at successively finer
chart-transition resolution. Three consequences:

- **The continuous Wick rotation** is the analytic continuation
  $t \mapsto t e^{i\varTheta}$ of the Reeb-flow parameter, with the
  Euclidean ($\varTheta = 0$) and Minkowski ($\varTheta = \pi/2$)
  metrics as endpoints
  ([affine-chart origin of $i$ and $q$](#rem:affine-chart-origin-of-i-and-q)).
- **Knot operators** are Reeb-$U(1)$ Wilson loops on the contact
  bundle: a torus knot $T_{m,n}$ embeds as the $(m, n)$-cable of a
  Reeb fibre, with framings = integer ambiguity in the $T_q$-lift to
  the gauge bundle. The categorical mass evaluation
  $|\mathrm{tr}_M(\mathcal{B}_K)|$ is the
  [Frobenius pairing](#def:frobenius-hopf-substrate) of the
  Reeb-$U(1)$ holonomy.
- **The OS reflection** $\theta_{\mathrm{OS}}$ is the antipodal
  $\mathbb{Z}_2 \subset T_q$ subgroup; the positivity of the
  [Frobenius pairing under it](#conj:os-reflection-positivity-from-reeb)
  is the categorical datum that becomes OS reflection positivity
  in the archimedean realisation.
<!-- FILE_END: reeb-u1-five-roles.md -->

<!-- FILE_START: categorical-coordinate-ring.md -->
**Proposition.**
Let $R$ be the categorical ground ring, $V$ the fundamental object,
and $\mathbb{P}(V)$ the projective line object
([projective line object](#def:projective-line-object)) with two
affine charts $U_0, U_1$ and intersection $U_0 \cap U_1 \cong \mathbb{G}_m$.
Let $\iota \in \mathrm{Aut}_R(U_0 \cap U_1)$ be the chart-swap
involution $z \mapsto z^{-1}$ ($\iota^2 = \mathrm{id}$), and let $T_p$
denote the tangent space at a fixed point $p$ of $\iota$.

The **categorical-coordinate ring** of the chart-transition data of
the deformation family $(\mathbb{P}_q(V))_{q \in R^\times}$ is

$$
  R[i, q^{\pm 1}]
   \;=\;
  R[q, q^{-1}][i] / (i^2 + 1),
$$

characterised by the universal property:
$R[i, q^{\pm 1}]$ is the smallest $R$-algebra extension $S \supseteq R$
such that

1. $q \in S^\times$ (the chart-transition coefficient $z\,w = q^{-1}$
   is a unit in $S$);
2. The tangent representation $\rho_p(\iota) = -1 \in \mathrm{End}_R(T_p)$
   admits a square root in $S$:  there exists $i \in S$ with $i^2 = -1$.

Under this identification, the chart-transition automorphism group
factors as the semidirect product

$$
  \mathrm{Aut}_{R[i, q^{\pm 1}]}(U_0 \cap U_1, \mathbb{P}_q(V))
   \;\cong\;
   \langle q \rangle  \rtimes  \langle \iota \rangle,
$$

with $\mathbb{Z}_2 = \langle \iota \rangle$ acting on the cyclic
subgroup $\langle q \rangle \subset R^\times$ by inversion
$q \mapsto q^{-1}$.

**Mathematical Novelty.** While the construction of $R[q, q^{-1}][i]/(i^2+1)$ is routine commutative algebra, its mathematical novelty here is that this specific elementary ring is proven to universally parameterise the chart-transition data of the quantum projective line. Instead of taking the deformation parameter $q$ and the imaginary unit $i$ as externally posited constants, this algebraic derivation strictly recovers them as the unavoidable geometric consequences of requiring chart-transition invertibility and chart-swap reflection within the non-commutative coordinate algebra.
<!-- FILE_END: categorical-coordinate-ring.md -->

