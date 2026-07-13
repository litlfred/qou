<!-- FILE_START: surreal-speculative-intro.md -->
Speculative extensions: surreal-valued knot invariants, transfinite braid groups, and connections to set-theoretic independence phenomena.
<!-- FILE_END: surreal-speculative-intro.md -->

<!-- FILE_START: local-infinitesimal-field.md -->
The appendix so far treats the substrate parameter $q = 1 +
\varepsilon$ as a **single global element** of the valuation ring
$\mathcal{O} \subset \mathbf{No}$. This conjecture proposes a
richer structure: $\varepsilon$ is a **sheaf** of infinitesimals
across a scheme $X$, with $q(x) = 1 + \varepsilon(x)$ varying
locally from patch to patch.

## Setup

Let $X$ be the scheme of quantum observable universes (underlying
the categorical substrate of this paper). Following the
points-and-topology framework already in the paper, treat $X$ as a
functor $\mathrm{CRing} \to \mathrm{Set}$.

Evaluate $X$ at the valuation ring
([valuation ring of finite surreals](#rem:valuation-ring-finite-surreals)):

$$
  X(\mathcal{O})
   := \mathrm{Hom}_{\mathrm{CRing}}(\mathcal{O}_X, \mathcal{O}).
$$

An element of $X(\mathcal{O})$ is a "surreal-valued point" — an
assignment of a finite surreal to each coordinate of $X$. The
standard-part functor $\mathrm{st} : \mathcal{O} \to \mathbb{R}$
induces

$$
  X(\mathrm{st}) \;:\; X(\mathcal{O}) \twoheadrightarrow X(\mathbb{R}),
$$

sending each surreal-valued point to its classical real shadow
by stripping infinitesimal fluctuations.

## Conjecture

The substrate parameter is not a global constant $q \in \mathbb{R}$
but a **section of the structure sheaf** valued in $\mathcal{O}$:

$$
  \varepsilon \;\in\; \Gamma(X, \mathfrak{m}_X),
$$

where $\mathfrak{m}_X \subset \mathcal{O}_X$ is the sheaf of
infinitesimals on $X(\mathcal{O})$. Writing $\varepsilon(x)$ for
the stalk at a point $x \in X$:

1. **Local variation**: $\varepsilon(x)$ may differ from
 $\varepsilon(y)$ for distinct $x, y \in X$ — the substrate
 parameter *fluctuates* across the scheme.

2. **Standard-part global constant**: $\mathrm{st}(\varepsilon(x)) = 0$
 for all $x$, so the classical substrate is $q_{\mathrm{classical}} = 1$
 everywhere — matching the archimedean limit to a trivial
 constant.

3. **Birthday-uniform at archimedean scale**: the *leading
 surreal coefficient* of $\varepsilon(x)$ (i.e., the coefficient
 of $\omega^{-1}$ in the Conway normal form) *is* globally
 constant, and equals the paper's archimedean substrate deviation
 $q_0 - 1 \approx 0.11$.

Equivalently, $q(x) = 1 + (q_0 - 1) + \delta(x)$ where $\delta(x)$
is a strictly-infinitesimal local fluctuation with zero mean and
birthday-ordered magnitude distribution.

## Significance

1. **Halo structure**: every classical real point of $X$ is
 surrounded by a *halo* (monad) of infinitesimally-fluctuated
 surreal points. Under the functor $X(\mathrm{st})$ all halo
 points collapse to the classical point — but within the halo,
 distinct surreal fluctuations are resolved.

2. **Non-global symmetries**: a symmetry of this paper's QOU
 that is global in the archimedean sense may be broken at the
 infinitesimal scale *locally* (at specific points $x$), without
 affecting the classical image. This is analogous to approximate
 isospin / chiral symmetries in particle physics.

3. **Singularity detection**: a "singularity" of this paper's
 QOU is a point $x_0$ where some quantity diverges. In the
 surreal lift, the divergence has a specific normal-form order
 $\ordw(\cdot)$ — which, by locality, can vary in a neighbourhood
 of $x_0$.

## Relation to existing conjectures

This conjecture refines Hahn-series
substrate: instead of $q$ being a single
Hahn series, it is a *sheaf* of Hahn series. The base $\mathbb{R}$-
shadow agrees with the paper in both cases.

It also specialises [archimedean-stpart](#conj:archimedean-stpart)
to the sheaf-theoretic setting: the archimedean QOU is the
standard-part *sheaf-morphism* of the surreal QOU, not a
single-point morphism.

## Proof strategy

**Mathematical layer (existence of local sheaf structure)**:

1. Show that $\mathcal{O}$ is a valid coefficient ring for the
 scheme $X$: it is a local ring, hence satisfies all standard
 sheaf-construction axioms (easy).

2. Define $\mathfrak{m}_X$ as the kernel sheaf of the structure-
 sheaf morphism $\mathcal{O}_X \to (\mathcal{O}/\mathfrak{m})_X
   = \mathbb{R}_X$. This is the standard construction of an ideal
 sheaf.

3. Verify that global sections of $\mathfrak{m}_X$ exist
 (non-vacuously): the constant section $\varepsilon \mapsto
   \varepsilon$ witnesses this.

4. Characterise which global sections give consistent QOU
 structure — i.e., which $\varepsilon$-valued $q$ deformations
 preserve the rigid monoidal axioms up to the
 $\varepsilon$-relaxations of
 [infinitesimal-frobenius](#conj:infinitesimal-frobenius) etc.

**Physical layer (uniqueness of the fluctuation distribution)**:

5. Assume the fluctuation distribution $\delta(x)$ has some
 explicit form (e.g., zero-mean Gaussian on the classical
 spectrum of $X$).

6. Show that the classical observables (particle masses,
 $\mathcal{Q}$-values, spectral gaps) are *unchanged* under
 standard-part — equivalent to the sheaf being $\mathrm{st}$-
 compatible.

7. Show that there are *no* non-trivial fluctuation distributions
 at leading order beyond the global one — equivalent to
 rigidity of this paper QOU.

**Falsification path**: produce two distinct sheaf sections
$\varepsilon_1, \varepsilon_2$ on $X$ both producing the same
archimedean QOU under $X(\mathrm{st})$ but *differing* in some
surreal observable (e.g., the second-order coefficient of a
particle mass). Such non-uniqueness would show that the surreal
lift is strictly richer than the archimedean, and the extra
information is physical.

**Provability assessment**: mathematical layer provable once
`QOU.AppendixSurreals.ValuationRing` is developed (currently
pending). Physical layer speculative — depends on
interpretation.
<!-- FILE_END: local-infinitesimal-field.md -->

<!-- FILE_START: spectral-normal-form.md -->
Under the surreal lift $q = 1 + \varepsilon$
(Hahn substrate), every spectral operator
$O_q$ of this paper (Hecke generators, transfer matrices, $q$-
Hamiltonians, Feynman integrals, vortex operators) has eigenvalues
$\lambda_i(q)$ that are rational in $\varepsilon$, hence elements
of the valuation ring $\mathcal{O}$.

This conjecture asserts that **spectral gaps and singularities as
$q \to 1$ are read directly off the leading exponent $\ordw(\cdot)$**
of the eigenvalues, without analytic limits.

## Conjecture

Let $O_q : V \to V$ be a linear operator on a finite-dimensional
$\mathbf{No}$-vector space, whose matrix entries are rational
functions of $q$. At $q = 1 + \varepsilon$, let

$$
  \lambda_1(\varepsilon) \leq \lambda_2(\varepsilon) \leq \cdots
   \leq \lambda_N(\varepsilon)
$$

be the eigenvalues ordered by $\mathbf{No}$-magnitude. Define the
**spectral gap** $\Delta := \lambda_2(\varepsilon) -
\lambda_1(\varepsilon)$.

1. **Algebraic closure at $q = 1$**: the gap $\Delta$ closes in
   the classical limit iff $\ordw(\Delta) < 0$ (i.e., $\Delta$ is
   infinitesimal).

2. **Closure rate from leading exponent**: the rate of closure is
   $\ordw(\Delta) \in \mathbf{No}$. Specifically:
   - $\ordw(\Delta) = 0$: gap stays open in the classical limit
     (no closure).
   - $\ordw(\Delta) = -1$: gap closes linearly, $\Delta \sim
     c\,\varepsilon$ — generic first-order closure.
   - $\ordw(\Delta) = -n$ for $n \in \mathbb{N}$: gap closes
     polynomially of order $n$.
   - $\ordw(\Delta) \in (-\omega\cdot 2,\, -\omega)$: gap closes
     *faster than any polynomial but slower than any exponential*
     — signals transcendental quantum-dilogarithm behaviour.

3. **Singularity formation**: a divergence (eigenvalue blowing up)
   has $\ordw(\lambda_i) > 0$ in the surreal lift. The exponent
   $\ordw(\lambda_i)$ classifies the divergence type:
   - $\ordw(\lambda_i) = 1$: simple pole, $\lambda_i \sim
     C/\varepsilon = C\omega$.
   - $\ordw(\lambda_i) = n$: $n$-th order pole, $\lambda_i \sim
     C\omega^n$.
   - $\ordw(\lambda_i) \in (1, 2)$: fractional-order divergence,
     signalling root-of-unity or Weierstrass behaviour.

4. **Algebraic vs transcendental singularities**: if
   $\ordw(\lambda_i)$ is a **rational** surreal (in the
   Hahn-series rationals $\mathbb{Q} \subset \mathbf{No}$), the
   singularity is algebraic. If $\ordw(\lambda_i)$ is transfinite
   (involves $\omega$ or logarithms), the singularity is
   transcendental.

## Application to QOU

Specialise to two main-paper operators:

**Categorical transfer matrix $T(c, d)$** (braiding eigenvalues):
- Eigenvalues are $q$ and $-q^{-1}$ at every Hecke-level step.
- At $q = 1 + \varepsilon$: leading terms $1 + \varepsilon$ and
  $-(1 - \varepsilon + \varepsilon^2 - \cdots) = -1 + \varepsilon
  - \varepsilon^2 + \cdots$.
- Gap $\Delta = q - (-q^{-1}) = q + q^{-1}$, which equals $2 + O(\varepsilon^2)$
  at $q = 1 + \varepsilon$. $\ordw(\Delta - 2) = -2$, so no
  closure; the classical limit preserves the binary splitting.

**$q$-Hamiltonian $\hat{H}_q$** (from this paper):
- At $q = 1 + \varepsilon$, each eigenvalue is rational in
  $\varepsilon$.
- Classical-limit $q \to 1$ eigenvalues are the
  standard-parts.
- Quantum corrections are the subleading coefficients —
  accessible by inverting the $\ordw$ filtration.

**Möbius energy $E_q$**:
- $E_q = \frac{1}{4} E_{\mathrm{classical}} + \mathrm{const}$ at
  $q \to 1$.
- Surreal-lifted: $\ordw(E_q - \frac{1}{4}E_{\mathrm{classical}}) \geq 0$,
  with the leading surreal constant fixed.

## Contrast with classical spectral theory

Classical spectral analysis of $q$-deformed operators requires:
- $\varepsilon$--$\delta$ bounds on eigenvalues as $q \to 1$;
- careful treatment of multiplicity crossings;
- perturbation theory with analytic convergence radii.

Under the surreal lift, all of this is replaced by:
- *algebraic* evaluation of eigenvalues at $q = 1 + \varepsilon$
  (a rational arithmetic in $\varepsilon$);
- *ordinal-valued* leading exponents of spectral differences
  classifying gap closure;
- *no convergence requirement* — everything is formal power series
  with infinite-birthday exponents.

This is a substantive conceptual simplification; whether it
corresponds to a practical *proof* technique (replacing current
spectral-gap proofs in the paper with surreal evaluations)
depends on computability of the normal forms.

## Proof strategy

**Algebraic case (provable now, modulo conjecture
Hahn-substrate)**:

1. Assume $O_q$ has matrix entries in $\mathbb{Q}(q)$ or, more
   generally, in the Hahn-series substrate.

2. Eigenvalues are rational functions of $q$ by standard
   linear algebra; hence rational in $\varepsilon$ at
   $q = 1 + \varepsilon$.

3. Compute $\ordw(\Delta)$ directly from the rational-function
   expression.

4. Verify against this paper's spectral-gap statements
   (e.g., for the Hecke generators where the gap is known
   classically).

**Transcendental case (speculative)**:

5. For operators whose entries involve the quantum dilogarithm
   or other transcendentals, appeal to
   Berarducci–Mantova exponential/log on $\mathbf{No}$
   [@berarducci-mantova2018].

6. Compute the normal-form expansion of each eigenvalue, reading
   off the leading transfinite exponent.

7. Match against known asymptotic-volume formulas (Kashaev,
   etc.).

**Required infrastructure**:
- Rational-function arithmetic in Lean at $q = 1 + \varepsilon$
  (partial; via specialising `Polynomial (R_q)` at surreal values).
- Hahn-series substrate (pending).
- Normal-form computation for eigenvalues (pending).

**Falsification path**: find an operator $O_q$ with classically
well-defined spectral gap closure *not* matching the leading
exponent $\ordw(\Delta)$. Such a mismatch would refute the
surreal-normal-form interpretation, likely indicating a subtle
multi-scale behaviour that the surreal lift does not capture.

**Provability assessment**: algebraic case mostly tractable with
current Lean + surreal infrastructure. Transcendental case
requires Berarducci–Mantova in Lean. The overall conjecture is
a *dictionary*, more testable than deep-research-open.

## Open problem

The conjecture is open. Its importance depends on whether the
QOU paper's spectral-gap and singularity-formation claims can be
rewritten as leading-exponent computations. If so, the
classical-limit discussions simplify substantially; if not, the
surreal lift is a curiosity.
<!-- FILE_END: spectral-normal-form.md -->

<!-- FILE_START: kashaev-surreal.md -->
The Kashaev volume conjecture [@kashaev1997] (proved for various
classes of knots by Murakami--Murakami [@murakami-murakami2001] and
others, but open in full generality) states:

$$
  \mathrm{Vol}(S^3 \setminus K)
   \;=\; 2 \pi \cdot \lim_{n \to \infty}
    \frac{\log |J_K(\zeta_n, n)|}{n},
$$

where $J_K(q, n)$ is the $n$-th coloured Jones polynomial,
$\zeta_n = e^{2 \pi i / n}$, and $\mathrm{Vol}$ is the hyperbolic
volume.

The conjecture has two awkward features when viewed through QOU:

1. The **left-hand side** is hyperbolic volume — pure analytic
 geometry, broken under surreal replacement (see
 [analytic obstructions](#rem:analytic-obstructions)).
2. The **right-hand side** uses an asymptotic-$n$ limit at a root
 of unity — a *singular* limit in $\mathbb{C}$.

Under the surreal lift, both sides admit cleaner reformulations,
and the gap between them sharpens.

## Reformulation

Set $n = \omega \in \mathbf{No}$ (the first infinite ordinal as a
surreal). Then $\zeta_\omega = e^{2 \pi i / \omega}$ is a
specific element of $\mathbf{No}[i]$ (interpreting the exponential
via Berarducci--Mantova's transseries [@berarducci-mantova2018]).
The coloured Jones polynomial $J_K(q, n)$ is rational in $q$ and
*polynomial in $n$* for fixed $K$, so $J_K(\zeta_\omega, \omega)$
is well-defined as an element of $\mathbf{No}[i]$.

The **surreal Kashaev statement** is:

$$
  \mathrm{Vol}(S^3 \setminus K)
   \;\stackrel{?}{=}\;
   \mathrm{st}\!\left(
     2 \pi \cdot \frac{\log |J_K(\zeta_\omega, \omega)|}{\omega}
   \right),
$$

where $\mathrm{st}$ is the standard-part map applied to a finite
surreal.

## The trade-off

The reformulation **does not solve** the volume conjecture. It
trades:

- (classical) an analytic limit $\lim_{n \to \infty}$ of complex
 numbers, plus a hyperbolic-volume identity in $\mathbb{R}$;

for:

- (surreal) an evaluation of a polynomial-in-$n$ at $n = \omega$,
 plus the *standard-part* identity that the result agrees with
 hyperbolic volume.

The right-hand side of the surreal version is *manifestly*
well-defined (rational arithmetic in $\mathbf{No}$), so the
question reduces to whether the **standard-part** matches. The
asymptotic-limit content of Kashaev becomes the standard-part
content of the surreal version.

## Location of the algebra-vs-analysis split

The reformulation makes the algebraic and analytic content of
Kashaev separable:

| Side | Algebra-vs-analysis content |
|---|---|
| RHS, before $\mathrm{st}$ | Pure algebra: rational in $\omega$ at root of unity |
| $\mathrm{st}$ application | Asymptotic transseries reduction |
| Identification with $\mathrm{Vol}$ | Genuine hyperbolic geometry |

The first row uses no analysis. The second row uses a *single*
transseries reduction (Berarducci--Mantova). The third row is
where hyperbolic geometry enters — and it enters *only* on the
LHS.

This is the appendix's sharpest expression of "trade analytic
for surreal": Kashaev becomes one transseries reduction
plus one $\mathrm{Vol}$-identity, instead of an analytic
limit plus a $\mathrm{Vol}$-identity.

## Potential utility and its limits

**Might help:** the algebraic side $J_K(\zeta_\omega, \omega)$
is exactly computable for any specific knot (it is a rational
function evaluated at named surreals). If a *general* formula
exists for $\mathrm{st}(\log |J_K(\zeta_\omega, \omega)|/\omega)$
in terms of knot data, we have a path to a proof of Kashaev.

**Might not help:** the standard-part identity is *itself* an
analytic statement (it asserts an asymptotic relationship
between the algebraic and the geometric). The surreal lift may
just relocate the difficulty rather than dissolve it.

## Discussion

**Open** — the conjecture is a reformulation, not a proof. Its
value is in *separating* the algebraic content (which is
computable) from the geometric content (which is the actual
Kashaev). The Murakami--Murakami proof for the figure-eight
knot [@murakami-murakami2001] should be re-derivable in the surreal form
as a sanity check.

## Connection to QOU

This paper uses the Kashaev volume conjecture as a *cross-
check* on its categorical mass formula
([Kashaev volume--density](#rem:kashaev-volume-density)). The
mass formula computes a particle mass via Hoefsmit/Markov-trace
data; the cross-check identifies this with a Jones-polynomial
evaluation, which Kashaev relates to hyperbolic volume.

Under the surreal lift:

- Hoefsmit/Markov-trace side lifts to $\mathbf{No}$ exactly
 (algebraic — see [algebraic core survives](#rem:algebraic-core-survives)).
- Jones polynomial at $q = q_0 \in \mathbb{R}$ lifts by definition
 ($q_0 \in \mathbb{R} \subset \mathbf{No}$).
- Hyperbolic volume side stays in $\mathbb{R}$ (external anchor).
- Kashaev's identity, recast as a surreal standard-part
 identity, bridges the two.

If the surreal Kashaev conjecture is proved (or even just
proved for the knot class relevant to QOU), the QOU mass formula
acquires an algebraic foundation independent of hyperbolic
geometry.

## Proof strategy

**Reformulation reducibility (provable now)**:

1. Show: the classical Kashaev statement (limit form) and the
 surreal Kashaev statement (standard-part form) are
 *equivalent* — one holds iff the other does.

2. Forward direction: if $\lim_{n \to \infty} 2\pi \log
   |J_K(\zeta_n, n)|/n = \mathrm{Vol}(S^3 \setminus K)$, then by
 the transfer principle the standard-part of the surreal
 evaluation matches.

3. Backward direction: if $\mathrm{st}(\cdots) =
   \mathrm{Vol}(\cdots)$, then by definition of $\mathrm{st}$
 the asymptotic limit converges to $\mathrm{Vol}$.

**Verification on known cases (provable now)**:

4. The figure-eight knot $4_1$ (Murakami–Murakami 2001
 [@murakami-murakami2001]) and the trefoil $3_1$ have the volume
 conjecture proved. Compute $J_K(\zeta_\omega, \omega)$
 directly, take $\mathrm{st}$, and verify equality with the
 known volume.

5. Use `QOU.AppendixSurreals.gonshorIn` and
 `omegaSurreal` to express the surreal evaluations.

**General case (open)**:

6. The general Kashaev conjecture for hyperbolic knots is open
 classically. The surreal reformulation does not provide a new
 line of attack, but it *separates* the algebraic content
 (rational-in-$\omega$ evaluations of $J_K$) from the geometric
 content (the volume identity).

**Required infrastructure**:
- Coloured Jones polynomial in Lean (does not exist in mathlib).
- Berarducci–Mantova exponential/logarithm on $\mathbf{No}$
 (partial in mathlib).
- Hyperbolic-volume formalisation (does not exist in mathlib).

**Falsification path**: identical to the classical Kashaev
conjecture; if the limit form fails for some knot, the
surreal form fails as well (and conversely).

**Provability assessment**: the *equivalence* of the two
formulations is provable in Lean (transfer principle). The
underlying conjecture is a long-standing open problem; the
reformulation does not by itself solve it but reorganises the
problem productively.
<!-- FILE_END: kashaev-surreal.md -->

<!-- FILE_START: perpetual-obstruction-depth-omega.md -->
The [motivic perpetual obstruction](#conj:motivic-perpetual-obstruction)
asserts that the Yekutieli obstruction $\kappa_n$ is non-trivial at
*every* finite tower level $n$. Under the surreal lift, this infinite
family of non-vanishing statements is the shadow of a single graded
coefficient.

Recall the substrate identification $\varepsilon = q - 1
\leftrightarrow 1/\omega$ ([surreal blow-up
calculus](#def:surreal-blowup-calculus)), under which the level-$n$
contribution sits at $\varepsilon$-order $n$. The element

$$
  \varepsilon^{\omega} \;=\; \omega^{-\omega},
  \qquad
  0 \;<\; \varepsilon^{\omega} \;<\; \varepsilon^{n}
  \quad\text{for every finite } n,
$$

is the unique grade lying beneath the entire finite tower — the
**depth-$\omega$** slot of the [Conway normal
form](#rem:conway-normal-form). It exists in $\mathbf{No}$ precisely
because $\mathbf{No}$ admits Hahn expansions with *surreal* exponents,
and has no counterpart in the archimedean Hahn line
$\mathbb{R}((\varepsilon^{\mathbb{Q}}))$, whose exponents are finite.

**Interpretation.** Perpetuity of the obstruction is equivalent to the
surreal-lifted obstruction $\widehat{\kappa}$ carrying a non-zero
component at the depth-$\omega$ grade:

$$
  \kappa_n \neq 0 \ \ (\forall\, n \in \mathbb{N})
  \qquad\Longleftrightarrow\qquad
  [\varepsilon^{\omega}]\,\widehat{\kappa} \;\neq\; 0 .
$$

The universally-quantified family collapses to one non-vanishing
graded coefficient. This is the cleanest service the surreal field
renders the framework: an obstruction *beyond every finite order* —
a non-perturbative datum invisible to each $\varepsilon^{n}$
truncation, in the manner of a transseries beyond-all-orders term —
acquires an explicit home as a single element of the value group.

**Scope.** The equivalence is a re-grading, not a new theorem. By
Mostow rigidity the volume series $\mathrm{Vol} = \sum_n \Phi_n$
converges in $\mathbb{R}$ ([Chern–Simons evaluation
faithfulness](#prop:cs-evaluation-faithfulness)), so the archimedean
value is recovered by the standard part and no surreal arithmetic is
needed to evaluate it. The depth-$\omega$ statement is a single graded
witness for perpetuity — the narrowing — not an archimedean
obligation.
<!-- FILE_END: perpetual-obstruction-depth-omega.md -->

