**Where this fits.** Three blocks in this paper address the
$q \to 1$ classical limit:

| Block                                                                    | Scope                                                                                                 | Status                                                                                          |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| [classical limit functor](#def\:classical-limit-functor)                 | Topological definition $\mathcal{L} : \mathbf{C}_q \to \mathbf{C}_1$                                  | Definition (with obstruction)                                                                   |
| **This block**                                                           | Single-functor surreal replacement: $\mathcal{L} \cong \mathrm{St} \circ \mathrm{ev}_{1+\varepsilon}$ | Conjecture (open)                                                                               |
| [archimedean QOU is standard-part of surreal](#conj\:archimedean-stpart) | Whole-tuple surreal replacement on $(\mathbf{C}, \varTheta, G, \mathcal{S})$                          | Conjecture (open); strategy in [archimedean-stpart strategy](#rem\:archimedean-stpart-strategy) |

The current block is the *single-functor* version; the
whole-tuple version is the appendix companion. Both are likely
equivalent modulo functoriality.

The [classical limit functor](#def\:classical-limit-functor)
$\mathrm{cl} : \mathbf{C}_q \to \mathbf{C}_{q=1}$ takes the
$q \to 1$ limit of categorical structures parametrised by the
substrate parameter $q$. Classically, this requires either a
topological notion of limit on the parameter space (which fails
for surreal-valued $q$) or a careful Hochschild-cohomology
construction
([classical limit obstruction](#def\:classical-limit-obstruction)).

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
([classical limit obstruction](#def\:classical-limit-obstruction))
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

## Why this matters

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
