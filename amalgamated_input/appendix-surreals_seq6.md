<!-- FILE_START: standard-part-classical-limits-intro.md -->
The standard-part functor projects surreal-valued observables to their real shadows, recovering classical limits.
<!-- FILE_END: standard-part-classical-limits-intro.md -->

<!-- FILE_START: valuation-ring-finite-surreals.md -->
The [standard-part functor](#def:standard-part-functor)
$\mathrm{st} : \mathbf{No}_{\mathrm{fin}} \to \mathbb{R}$ admits a
clean ring-theoretic reading: **it is the quotient map of a
valuation ring.**

## Valuation ring structure

The **finite surreals** form a convex subring of $\mathbf{No}$:

$$
  \mathcal{O}
   := \{ x \in \mathbf{No} : \exists n \in \mathbb{N},\,
         -n < x < n \}
   = \{ x \in \mathbf{No} : \mathrm{IsFinite}(x) \}.
$$

The **infinitesimals** form its unique maximal ideal:

$$
  \mathfrak{m}
   := \{ x \in \mathcal{O} : \mathrm{IsInfinitesimal}(x) \}.
$$

The quotient

$$
  \mathcal{O} / \mathfrak{m} \;\xrightarrow{\sim}\; \mathbb{R}
$$

is canonically isomorphic to the real numbers, and the projection
$\mathcal{O} \twoheadrightarrow \mathcal{O}/\mathfrak{m}$ is exactly
$\mathrm{st}$.

## Significance of this framing

The appendix's functorial constructions (point-evaluation of
schemes, categorical enrichments, surreal-coefficient sheaves)
all need a **set-sized** coefficient ring to avoid proper-class
pathologies. The valuation ring $\mathcal{O}$ is set-sized; the
ambient $\mathbf{No}$ is a proper class. By restricting to
$\mathcal{O}$ before any point-evaluation, we stay inside
standard set-theoretic foundations.

The infinite surreals $\mathbf{No} \setminus \mathcal{O}$ are **not
in the domain of $\mathrm{st}$**. Any arithmetic involving
$\omega, \omega^2, \omega^\omega$ must be restricted to
$\mathcal{O}$ before projecting. This is not a loss: it is
exactly the archimedean-observability boundary already implicit
in the main paper's treatment of physical observables.

## Connection to points-and-topology framework

The main paper develops the points-and-topology framework for
QOU in its categorical-foundations chapters. This remark
specialises that framework to the surreal setting:

- Main paper: points of a categorical structure live in an
  $R$-algebra for some coefficient ring $R$.
- Surreal appendix: the natural choice is $R = \mathcal{O}$
  (finite surreals), with the archimedean quotient recovering
  $R = \mathbb{R}$.

No new framework is introduced here; this remark records that
the Robinson standard-part construction fits the same
categorical framework already in use.
<!-- FILE_END: valuation-ring-finite-surreals.md -->

<!-- FILE_START: classical-limit-stpart.md -->
**Placement in the paper.** Three blocks in this paper address the
$q \to 1$ classical limit:

| Block                                                                    | Scope                                                                                                 | Status                                                                                          |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| [classical limit functor](#def:classical-limit-functor)                 | Topological definition $\mathcal{L} : \mathbf{C}_q \to \mathbf{C}_1$                                  | Definition (with obstruction)                                                                   |
| **This block**                                                           | Single-functor surreal replacement: $\mathcal{L} \cong \mathrm{St} \circ \mathrm{ev}_{1+\varepsilon}$ | Conjecture (open)                                                                               |
| [archimedean QOU is standard-part of surreal](#conj:archimedean-stpart) | Whole-tuple surreal replacement on $(\mathbf{C}, \varTheta, G, \mathcal{S})$                          | Conjecture (open); strategy in [archimedean-stpart strategy](#rem:archimedean-stpart-strategy) |

The current block is the *single-functor* version; the
whole-tuple version is the appendix companion. Both are likely
equivalent modulo functoriality.

The [classical limit functor](#def:classical-limit-functor)
$\mathrm{cl} : \mathbf{C}_q \to \mathbf{C}_{q=1}$ takes the
$q \to 1$ limit of categorical structures parametrised by the
substrate parameter $q$. Classically, this requires either a
topological notion of limit on the parameter space (which fails
for surreal-valued $q$) or a careful Hochschild-cohomology
construction
([classical limit obstruction](#def:classical-limit-obstruction)).

This conjecture proposes a clean replacement: the classical-limit
functor is the **standard-part of evaluation at $q = 1 +
\varepsilon$**.

## Conjecture

Let $\mathbf{C}_q$ be a $K$-linear :refterm[monoidal category]{#monoidal-category} whose
structure constants are rational functions of $q \in K$, and let
$\mathrm{cl}_{\mathrm{top}} : \mathbf{C}_q \to \mathbf{C}_{q=1}$
be the topological classical-limit functor (defined when it
exists). Set $K = \mathbf{No}$, fix an infinitesimal
$\varepsilon \in \mathbf{No}$, and let
$\mathrm{ev}_{1 + \varepsilon} : \mathbf{C}_q \to
\mathbf{C}_{\mathbf{No}}$ be evaluation at $q = 1 + \varepsilon$.

Then there is a natural isomorphism of functors

$$
  \mathrm{cl}_{\mathrm{top}}
   \;\cong\;
  \mathrm{St} \circ \mathrm{ev}_{1 + \varepsilon},
$$

whenever the left-hand side is defined. The right-hand side is
defined more generally — wherever the structure constants make
sense as rational expressions in $\varepsilon$.

## Discussion

The conjecture is a *natural-isomorphism* statement: both sides
should agree on objects (since the standard-part of an
infinitesimal-shifted object recovers the archimedean object) and
on morphisms (the standard-part of a Jackson derivative is the
classical derivative; the standard-part of a $q$-shifted matrix
entry is its $q = 1$ value).

The novelty is that the right-hand side **always exists** as long
as the structure constants are rational in $\varepsilon$ — even in
cases where the left-hand side has obstructions. The
classical-limit obstruction
([classical limit obstruction](#def:classical-limit-obstruction))
$\mathrm{HH}^2(\mathcal{U}_q, \mathrm{Ad})$ becomes, on the
The right-hand side, a *non-zero finite surreal* in
$\mathbf{No}_{\mathrm{fin}}$ whose standard-part vanishes only
when the obstruction itself vanishes.

This gives a refined picture: the obstruction is *always*
detected in the surreal lift (as a non-trivial first-order
$\varepsilon$-term), but it is "felt by the classical observer"
only when the standard-part is non-zero.

## Discussion

**Open.** The conjecture is partly motivated by Berarducci--
Mantova's derivation construction
\[@berarducci-mantova2018]: their derivation $D : \mathbf{No} \to
\mathbf{No}$ extends $d/dx$ on $\mathbb{R}$, so the standard-
part of $D(f(1 + \varepsilon))$ recovers $f'(1)$ when $f$ is
analytic. Promoting this from a single function to a functor on
$\mathbf{C}_q$ requires functoriality of the standard-part — known
classically \[@robinson1966] in the model-theoretic setting but
not (yet) in the categorical setting.

A first step would be to prove the conjecture for
$\mathbf{C}_q = \mathrm{Rep}(\mathrm{SU}_q(2))$ — the case of
direct interest for QOU.

## Significance

The paper treats the $q \to 1$ classical limit
*archimedean-topologically*: as a limit of real numbers in a
topology on the parameter space. Under the surreal lift, the
limit becomes a *literal evaluation at a specific surreal* — no
topology required. Whether the two formulations give the same
answer is the conjecture above.

If true, the conjecture would let the entire classical-limit
discussion in the paper (Möbius energy comparison; experimental
benchmarks; $\hbar_q \to 0$ etc.) be re-stated as
standard-part identities, eliminating one source of analytic
machinery.

## Proof strategy

The conjecture splits into a single-morphism case and a
naturality case:

**Single morphism case (single-element ground field)**:

1. **Specialise** to the simplest non-trivial example:
   $\mathbf{C} = \mathrm{Vect}_{\mathbb{Q}(q)}$ and a morphism
   $f : V \to V$ given by a single rational function
   $f_q(x) = p(q, x) / r(q, x)$ in $\mathbb{Q}(q, x)$.

2. **Show**: $\lim_{q \to 1} f_q$ (in the topological sense, where
   defined) equals $\mathrm{st}(f_{1+\varepsilon})$. Concretely:
   write $f_{1+\varepsilon} = f_1 + \varepsilon \cdot g + O(\varepsilon^2)$
   by Taylor expansion in the second variable; the standard-part
   recovers $f_1 = \lim_{q \to 1} f_q$.

3. **Lemma needed**: standard-part commutes with rational arithmetic
   on finite surreals. Provided by
   `QOU.AppendixSurreals.standardPart_add` and
   `standardPart_mul`.

**Naturality case** (functorial promotion):

4. Generalise from a single morphism to a functor
   $\mathrm{cl}_{\mathrm{top}} : \mathbf{C}_q \to \mathbf{C}_{q=1}$.
   This requires functoriality of $\mathrm{St}$ on the
   $K$-linear category $\mathbf{C}_K$, which is straightforward
   from the ring-hom property of $\mathrm{St}$ on the finite
   subring (provided $\mathbf{C}$ is enriched over
   $K$-modules).

**Required infrastructure**:

* `QOU.AppendixSurreals.standardPart_add`, `_mul` (proved up to
  the `IsFinite_decomposition` axiom).
* A decision procedure for "rational in $\varepsilon$" in Lean
  (could specialise to `Polynomial K`).

**Falsification path**: produce a categorical structure
$\mathbf{C}_q$ where some morphism's $q \to 1$ limit exists in
the classical (topological) sense but not as a standard-part of
evaluation at $1 + \varepsilon$. Such a structure would have to
involve a discontinuous-but-classically-limit-existing function,
which (for rational structure constants) is impossible.

**Provability assessment**: the single-morphism case is a Lean
exercise once the `IsFinite_decomposition` axiom is discharged.
The functorial case requires more `CategoryTheory` machinery but
is structural.
<!-- FILE_END: classical-limit-stpart.md -->

<!-- FILE_START: archimedean-stpart.md -->
A QOU is an archimedean tuple
$(\mathbf{C}, \varTheta, G, \mathcal{S})$
([quantum observable universe](#def:quantum-observable-universe))
in the main paper: the categorical algebra $\mathbf{C}$ is
$K$-linear with $K = \mathbb{R}$ implicit, the gauge group $G$ is
a real Lie group, and $\mathcal{S}$ is a real vector bundle.

A **surreal QOU** is the same data with $K = \mathbf{No}$ — but
with all axioms relaxed to hold up to an infinitesimal:

| Axiom | Archimedean | Surreal |
|---|---|---|
| Frobenius pairing | $\int_A \circ \mu = \mathrm{id}$ | $= \mathrm{id} + O(\varepsilon)$ |
| Observability | $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ | $\leq \varepsilon$ |
| Volume | $g_{\mathbf{1}} = \mathrm{id}$ | $= (1 + \varepsilon) \mathrm{id}$ |
| Vacuum | $\mathrm{Geom}(\unicode{9737}) = 0$ | $= \varepsilon$ |

Each relaxation is via the named infinitesimal $\varepsilon \in
\mathbf{No}$ from
[surreal blow-up calculus](#def:surreal-blowup-calculus).

## Conjecture

The standard-part functor $\mathrm{St}$
([standard-part functor](#def:standard-part-functor)) sends every
surreal QOU to an archimedean QOU. More precisely:

There is a functor

$$
  \mathrm{St}_{\mathrm{QOU}} :
   \mathbf{QOU}_{\mathbf{No}}^{\varepsilon}
   \longrightarrow
   \mathbf{QOU}_{\mathbb{R}},
$$

from the category of surreal QOUs (with $\varepsilon$-relaxed
axioms) to archimedean QOUs (with strict axioms), defined by
applying $\mathrm{St}$ to all hom-spaces. The functor is
**essentially surjective** — every archimedean QOU lifts to a
surreal QOU — and the composition
$\mathrm{St}_{\mathrm{QOU}} \circ \iota$ (where $\iota$ is the
inclusion of archimedean QOUs as the "$\varepsilon = 0$" surreal
QOUs) is the identity.

## Strength

If the conjecture holds, the surreal lift carries strictly more
information than the archimedean theory: each archimedean QOU has
a *fibre* of surreal QOUs above it, parametrised by the
infinitesimal-correction data $\{\varepsilon, \varepsilon^2,
\ldots\}$ allowed by the relaxed axioms. Two non-isomorphic
surreal QOUs may have the same standard-part image, in which case
the additional information is *infinitesimal physics*: first-order
quantum corrections to the Frobenius pairing, observability
cohomology, volume normalisation, and vacuum.

Whether such infinitesimal corrections are *physical* (i.e.
distinguish observable predictions) or only *mathematical*
(distinguished only by the surreal structure) is itself open.

## Relation to the classical-limit conjecture

This conjecture is the **categorical** counterpart of
[classical limit as standard-part](#conj:classical-limit-stpart):

- Classical-limit-stpart says: the $q \to 1$ classical-limit
 functor on $\mathbf{C}_q$ is $\mathrm{St} \circ \mathrm{ev}_{1
  + \varepsilon}$ (single-category statement).
- Archimedean-stpart says: the entire QOU framework
 $(\mathbf{C}, \varTheta, G, \mathcal{S})$ is the
 standard-part of an $\varepsilon$-relaxed surreal QOU
 (whole-tuple statement).

The two conjectures are likely equivalent modulo functoriality,
but a precise reduction is open.

## Consequences of the lift

If true, the appendix's $\varepsilon$-relaxation is a *strict*
generalisation of the main paper:

1. The main paper's QOU axioms are recovered as
 $\mathrm{St}_{\mathrm{QOU}}$ applied to the surreal axioms.
2. Every theorem proved in the main paper has a surreal
 counterpart; the surreal counterpart may have additional
 non-trivial first-order corrections that vanish under
 $\mathrm{St}$.
3. Future work can investigate whether these corrections have
 physical significance (e.g., explain corrections to the QOU
 mass formula's $4\%$ MAE on $\mathcal{Q}$-values).
## Proof strategy

The conjecture is the *category-level* counterpart of
[classical-limit-stpart](#conj:classical-limit-stpart). Reduce
to that conjecture via:

1. **Functorial reduction**. Show
 $\mathrm{St}_{\mathrm{QOU}} = (\mathrm{St}, \mathrm{St}, \mathrm{St},
   \mathrm{St})$ — the standard-part applied to each component of the
 QOU tuple $(\mathbf{C}, \varTheta, G, \mathcal{S})$.

2. **Reduce each component**:
 - $\mathbf{C} = \mathrm{Rep}_{\mathbf{No}}(\mathrm{SU}_q(2))$ at
 $q = 1 + \varepsilon$: $\mathrm{St}$ recovers
 $\mathrm{Rep}_{\mathbb{R}}(\mathrm{SU}(2))$ by
 [classical-limit-stpart](#conj:classical-limit-stpart).
 - $\varTheta : \mathbf{1} \to A$: just an element of a hom-space;
 $\mathrm{St}$ acts entry-wise.
 - $G = \mathrm{Aut}(A)$: a functorial gauge group; standard-part
 of an algebraic group object.
 - $\mathcal{S}$: state bundle; standard-part of fibre.

3. **Verify axioms**: each $\varepsilon$-relaxed axiom (Frobenius,
 observability, volume, vacuum) becomes the strict axiom under
 $\mathrm{St}$ — content of conjectures
 [infinitesimal-frobenius](#conj:infinitesimal-frobenius),
 [infinitesimal-observability](#conj:infinitesimal-observability),
 [vacuum-epsilon](#conj:vacuum-epsilon).

4. **Essential surjectivity**: every archimedean QOU lifts (set
 $\varepsilon = 0$ by definition). This direction is automatic.

**Required infrastructure**:
- The five sub-conjectures above (or worked examples).
- A `Functor` instance from `QOU_No^ε` to `QOU_ℝ` in Lean.
- `CategoryTheory.MonoidalFunctor` interaction with $\mathrm{St}$.

**Falsification path**: exhibit an $\varepsilon$-relaxed surreal
QOU whose standard-part image violates a strict QOU axiom
(e.g., the Frobenius pairing of the standard-part has positive
nullity). This would require an infinitesimal that becomes
non-infinitesimal under standard-part — impossible by the
definition of $\mathrm{st}$.

**Provability assessment**: structurally clean once the
sub-conjectures are settled. Mainly bookkeeping over the four
QOU components.
<!-- FILE_END: archimedean-stpart.md -->

<!-- FILE_START: archimedean-stpart-strategy.md -->
Proof strategy for
[archimedean QOU is the standard-part of surreal QOU](#conj:archimedean-stpart).
This remark records *how* one would attempt the proof, not the proof
itself; the conjecture remains open.

The conjecture is the *category-level* counterpart of
[classical-limit-stpart](#conj:classical-limit-stpart). Reduce
to that conjecture via:

1. **Functorial reduction.** Show
 $\mathrm{St}_{\mathrm{QOU}} = (\mathrm{St}, \mathrm{St}, \mathrm{St},
   \mathrm{St})$ — the standard-part applied to each component of the
 QOU tuple $(\mathbf{C}, \varTheta, G, \mathcal{S})$.

2. **Reduce each component**:
 - $\mathbf{C} = \mathrm{Rep}_{\mathbf{No}}(\mathrm{SU}_q(2))$ at
 $q = 1 + \varepsilon$: $\mathrm{St}$ recovers
 $\mathrm{Rep}_{\mathbb{R}}(\mathrm{SU}(2))$ by
 [classical-limit-stpart](#conj:classical-limit-stpart).
 - $\varTheta : \mathbf{1} \to A$: just an element of a hom-space;
 $\mathrm{St}$ acts entry-wise.
 - $G = \mathrm{Aut}(A)$: a functorial gauge group; standard-part
 of an algebraic group object. This is the categorical
 counterpart of the archimedean realization $\tau$ of
 [fibre functor rigidity](#rem:fibre-functor-rigidity) — the
 image of the rigid monoidal embedding into $\mathbb{R}$-linear
 endomorphisms.
 - $\mathcal{S}$: state bundle; standard-part of fibre.

3. **Verify axioms.** Each $\varepsilon$-relaxed axiom (Frobenius,
 observability, volume, vacuum) becomes the strict axiom under
 $\mathrm{St}$ — content of conjectures
 [infinitesimal-frobenius](#conj:infinitesimal-frobenius),
 [infinitesimal-observability](#conj:infinitesimal-observability),
 [vacuum-epsilon](#conj:vacuum-epsilon).

4. **Essential surjectivity.** Every archimedean QOU lifts (set
 $\varepsilon = 0$ by definition). This direction is automatic.

**Required infrastructure**:

- The five sub-conjectures above (or worked examples).
- A `Functor` instance from `QOU_𝐍𝐨^ε` to `QOU_ℝ` in Lean.
- `CategoryTheory.MonoidalFunctor` interaction with $\mathrm{St}$.

**Falsification path.** Exhibit an $\varepsilon$-relaxed surreal
QOU whose standard-part image violates a strict QOU axiom (e.g.
the Frobenius pairing of the standard-part has positive nullity).
This would require an infinitesimal that becomes non-infinitesimal
under standard-part — impossible by the definition of $\mathrm{st}$.

**Provability assessment.** Structurally clean once the
sub-conjectures are settled. Mainly bookkeeping over the four
QOU components.
<!-- FILE_END: archimedean-stpart-strategy.md -->

