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

Let $\mathbf{C}_q$ be a $K$-linear monoidal category whose
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
right-hand side, a *non-zero finite surreal* in
$\mathbf{No}_{\mathrm{fin}}$ whose standard-part vanishes only
when the obstruction itself vanishes.

This gives a refined picture: the obstruction is *always*
detected in the surreal lift (as a non-trivial first-order
$\varepsilon$-term), but it is "felt by the classical observer"
only when the standard-part is non-zero.

## Status

**Open.** The conjecture is partly motivated by Berarducci--
Mantova's derivation construction
[@berarducci-mantova2018]: their derivation $D : \mathbf{No} \to
\mathbf{No}$ extends $d/dx$ on $\mathbb{R}$, so the standard-
part of $D(f(1 + \varepsilon))$ recovers $f'(1)$ when $f$ is
analytic. Promoting this from a single function to a functor on
$\mathbf{C}_q$ requires functoriality of the standard-part — known
classically [@robinson1966] in the model-theoretic setting but
not (yet) in the categorical setting.

A first step would be to prove the conjecture for
$\mathbf{C}_q = \mathrm{Rep}(\mathrm{SU}_q(2))$ — the case of
direct interest for QOU.

## Why this matters

The QOU paper currently treats the $q \to 1$ classical limit
*archimedean-topologically*: as a limit of real numbers in a
topology on the parameter space. Under the surreal lift, the
limit becomes a *literal evaluation at a specific surreal* — no
topology required. Whether the two formulations give the same
answer is the conjecture above.

If true, the conjecture would let the entire classical-limit
discussion in the paper (Möbius energy comparison; CODATA
benchmarks; $\hbar_q \to 0$ etc.) be re-stated as
standard-part identities, eliminating one source of analytic
machinery.
