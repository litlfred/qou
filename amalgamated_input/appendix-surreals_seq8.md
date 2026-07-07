<!-- FILE_START: surreal-blowup-calculus.md -->
## Named surreals

Fix an infinitesimal $\varepsilon = 1/\omega \in \mathbf{No}$. Equivalently, $\omega = 1/\varepsilon$ is the first infinite ordinal regarded as a surreal. Then:

See [Table](#tbl:surreal-blowup-calculus-table-data).

These are specific elements of $\mathbf{No}$. Every name above corresponds to a unique element under Conway's recursive construction.

## The blow-up calculus

A **blow-up of a divergent expression** evaluates the expression at a named infinite surreal, then takes the standard part of a renormalised version. Schematically:

1. Write the divergent expression $X$ as a function of a parameter that becomes a named surreal: $X = X(\Lambda)$ with $\Lambda \to \omega$.
2. Identify a **counterterm** $C(\Lambda)$ (typically a polynomial in $\Lambda$) such that $X(\Lambda) - C(\Lambda)$ is a finite surreal.
3. Define the renormalised value:
   $X_{\mathrm{ren}} := \mathrm{st}(X(\omega) - C(\omega)) \in \mathbb{R}$.

The field $\mathbf{No}$ makes every step literal. The cutoff $\Lambda$ is a specific element. The counterterm is a specific surreal-valued function. The standard part is a specific real number.
<!-- FILE_END: surreal-blowup-calculus.md -->

<!-- FILE_START: surreal-blowup-examples.md -->
Physics frequently uses an unspecified $\infty$ to denote an unrenormalised divergence: $\Lambda \to \infty$, $1/\varepsilon$, $\delta(0)$, etc. These require a specific element in an extended number system. The surreal numbers $\mathbf{No}$ provide one. The blow-up calculus ([surreal blow-up calculus](#def:surreal-blowup-calculus)) makes each device literal.

## Examples

### Möbius energy diagonal

The diagonal-regularised Möbius energy ([Möbius energy proof](#prf:mobius-energy)) computes

$$
  E(\varrho) = \iint_{S^1 \times S^1}
    \!\!\left(\frac{1}{|\varrho(s) - \varrho(t)|^2}
    - \frac{1}{D(\varrho(s), \varrho(t))^2}\right) \!ds\, dt.
$$

In the surreal lift, the inner integrand at $s = t$ evaluates to $1/0^2 = \omega^2$. The arc-length subtraction $1/D^2$ matches this $\omega^2$ at $s = t$. The difference is a finite surreal. Its standard part is the renormalised energy.

### $c_q$ at $q = 1$

The speed of light $c_q = 1/(q-1)$ at $q = 1 + \varepsilon$ is exactly $\omega \in \mathbf{No}$. The classical-limit divergence "$c_q \to \infty$ as $q \to 1$" becomes the literal identity $c_q\big|_{q = 1 + \varepsilon} = \omega$.

### Vacuum normalisation

The empty-link Markov trace evaluates to $\mathrm{tr}_M(1) = z = 1/(\sqrt{q} + 1/\sqrt{q})$. At $q = 1 + \varepsilon$ this is $1/2 + O(\varepsilon)$. This is finite. In the unnormalised convention $\mathrm{tr}_M(1) = 1$, which becomes $1/0$ in normalisation factors. The named-surreal calculus makes these distinctions explicit.

## Cohomological aspect

The blow-up calculus respects the birthday grading. The counterterm $C(\omega)$ has the same birthday as $X(\omega)$. Their difference lives at a strictly lower birthday. The standard part collapses it to $\mathbb{R}$. This gives a birthday-graded refinement of the BPHZ subtraction algorithm. Each subtraction reduces the birthday by a controlled ordinal amount.

## Significance for QOU

The QOU mass formula contains no divergences. Hoefsmit seminormal form and the Markov trace produce finite rational expressions in $q$. The blow-up calculus is not needed for the main computation. It serves three secondary purposes:

1. **Möbius energy comparison**. We turn the informal classical $\infty$ into a named $\omega^2$.
2. **Classical-limit $q \to 1$**. We make "$c_q \to \infty$" literal: $c_q|_{q = 1+\varepsilon} = \omega$.
3. **Future renormalisation work**. We provide a setting for Yang--Mills or Sobolev-completion arguments that require regularisation (see [outlook](#sec:surreal-appendix-conclusion)).
<!-- FILE_END: surreal-blowup-examples.md -->

<!-- FILE_START: mobius-surreal-renormalization.md -->
The [Möbius energy](#prop:mobius-energy) (O'Hara \cite{ohara1991};
Freedman–He–Wang \cite{freedman1994}) is a *renormalized* quadratic
interaction: $\iint |\varrho(s)-\varrho(t)|^{-2}$ and $\iint D(s,t)^{-2}$ each
diverge on the diagonal and the divergences cancel. Under the surreal lift this
renormalization is **surreal arithmetic** — a difference of two infinite
surreals.

**Remark.** Excise a diagonal band of width $\varepsilon = 1/\omega$
([surreal blow-up calculus](#def:surreal-blowup-calculus)) and set

$$
  I_1 = \iint_{|s-t|>1/\omega}\!\frac{|\varrho'(s)|\,|\varrho'(t)|}{|\varrho(s)-\varrho(t)|^2},
  \qquad
  I_2 = \iint_{|s-t|>1/\omega}\!\frac{|\varrho'(s)|\,|\varrho'(t)|}{D(s,t)^2}.
$$

Both are **infinite surreals of $\operatorname{ord}_\omega = +1$**
([Conway normal form](#rem:conway-normal-form)): each diverges like $c\,\omega$
as the cutoff shrinks. Because $|\varrho(s)-\varrho(t)| = D(s,t) + O(|s-t|^3)$
near the diagonal, $I_1$ and $I_2$ share the **same leading coefficient** $c$,
consequently the $\omega^{+1}$ parts cancel, $I_1 - I_2$ is **appreciable** (finite), and

$$
  E(\varrho) \;=\; \operatorname{std}\!\bigl(I_1 - I_2\bigr).
$$

The analytic Hadamard finite part becomes *"subtract two infinite surreals of
equal leading $\omega$-order, take the standard part"*, and the **finiteness
bound** — the hard analytic content — reduces to an **algebraic
leading-coefficient match** $[\omega^{+1}]I_1 = [\omega^{+1}]I_2$ (the
near-diagonal expansion above).

**General principle — dimension as a surreal order.** The same move runs the
Frostman/Riesz $s$-energy $I_s = \iint |x-y|^{-s}$: infinite below the dimension,
appreciable above. The **Hausdorff dimension is the $\operatorname{ord}_\omega$
boundary** at which $I_s$ flips from infinite to appreciable — a single valuation
statement, not the analytic $\sup\{s : I_s < \infty\}$. (In-repo instance: the
Julia-set dimension $d_H(q) = (2q-1)^2/q^3$.)

**Scope.** This is the surreal *language* for a renormalization also expressible
classically (the Hadamard finite part over $\mathbb{R}$); its value is turning
the divergent quadratic interaction's finiteness bound into an algebraic
leading-coefficient check. It adds no archimedean obligation: $E(\varrho)$ is the
same real number either way. The contrast with the *measure-value* side is
sharp — $\mathbf{No}$ carries no Lebesgue measure, but Hausdorff *dimension*
(an exponent) and renormalized *energies* (a difference of infinite surreals)
are surreal-native.
<!-- FILE_END: mobius-surreal-renormalization.md -->

<!-- FILE_START: bigbang-heatdeath.md -->
The QOU framework is parameter-time-symmetric: the substrate
$q \in \mathbb{R}_{>0}$ controls all dimensionful constants (speed
of light $c_q = 1/(q-1)$, Planck constant $\hbar_q = (q-1)/q$,
etc.) but does not itself evolve in any preferred direction. A
cosmological reading would identify $q$-flow with cosmic time
$t$, with two natural endpoints:

- **Big Bang**: $q \to 1^+$ (where $c_q, c_q^2 \to \infty$, "speed
  of light diverges, all states causally connected, no time
  separation");
- **Heat death**: $q \to \infty$ (where $\hbar_q \to 1$, "quantum
  scale of action saturates classical scale of action, no further
  quantum dynamics distinguishable").

Both endpoints are *singular limits* in the archimedean sense:
the QOU structure constants diverge or saturate. Standard physics
treats these as unattainable boundary conditions.

## Conjecture

The Big Bang and heat-death "endpoints" are not unattainable:
they are the **standard-part of evaluation at specific named
surreals**.

For each $\varepsilon \in \mathbf{No}$ with $\varepsilon > 0$,
let $\mathbf{QOU}_{1 + \varepsilon}$ be the surreal QOU at $q = 1
+ \varepsilon$, and let

$$
  \mathbf{BigBang}_{1 + \varepsilon}
   := \mathrm{St}_{\mathrm{QOU}}(\mathbf{QOU}_{1 + \varepsilon}).
$$

This is a functor from the *infinitesimals* (an ordered
sub-monoid of $\mathbf{No}$) to archimedean QOUs. The
conjecture is:

1. **Big Bang as named-surreal evaluation**: there is a
   well-defined "Big Bang functor" $\mathbf{BigBang} :=
   \mathbf{BigBang}_{1 + \varepsilon}\big|_{\varepsilon \to 0^+}$.
   This is not a topological limit but a *named-surreal
   evaluation*: $\varepsilon \to 0^+$ in $\mathbf{No}$ is reached
   by replacing $\varepsilon$ with smaller and smaller infinitesimals
   $\varepsilon^2, \varepsilon^3, \ldots, \varepsilon^\omega$. The
   final functor is the evaluation at a specific transfinite surreal
   $\varepsilon^\omega$ (or whatever name is chosen for the
   limit), composed with $\mathrm{St}$.

2. **Heat death as evaluation at $q = \omega$**: similarly,
   $\mathbf{HeatDeath} := \mathrm{St}_{\mathrm{QOU}}(\mathbf{QOU}_{q = \omega})$,
   the standard-part of QOU evaluated at the named infinite surreal
   $\omega$.

3. **Both functors are well-defined.** The QOU mass formula and
   $\mathcal{Q}$-value derivations are rational in $q$, so they
   evaluate at any non-zero, non-pole element of $\mathbf{No}$,
   including the named endpoints. The functors land in
   well-defined (if degenerate) archimedean QOUs:
   - $\mathbf{BigBang}$: $c \to \infty$, $\hbar \to 0$, all
     particles massless, all knots equivalent (no eigenchannel
     distinction);
   - $\mathbf{HeatDeath}$: $c \to $ finite, $\hbar \to 1$,
     classical/quantum identification, no further quantum
     evolution.

4. **Approximation by intermediate $\varepsilon$**: the standard-
   part of $\mathbf{QOU}_{1 + \varepsilon}$ for "small but
   archimedean" $\varepsilon \in \mathbb{R}_{>0}$ approximates
   $\mathbf{BigBang}$ to leading order in $\varepsilon$. This is
   the classical "early-universe perturbation theory" reading:
   each $\mathbf{BigBang}_{1 + \varepsilon}$ at finite real
   $\varepsilon$ is a quantitative deviation from the singular
   $\mathbf{BigBang}$ functor.

## Consequences of the conjecture

If the conjecture holds, the cosmological endpoints become
*objects* in the category of archimedean QOUs rather than
unattained limits. Three immediate uses:

1. **Singularity resolution**: the Big Bang singularity is not a
   "place where physics breaks down"; it is the standard-part of a
   well-defined surreal QOU.

2. **Approximation framework**: physical observables near either
   endpoint are computed by perturbation in $\varepsilon$ around
   the named-surreal evaluation. This is just nonstandard analysis
   recast cosmologically.

3. **Functorial cosmology**: the cosmological-time evolution
   $t \mapsto \mathbf{QOU}_{q(t)}$ becomes a functor from surreal
   times to archimedean QOUs, with named endpoints as honest
   objects.
## Proof strategy

The mathematical kernel is well-defined; the question is one of
*interpretation*.

**Mathematical kernel** (provable now in Lean):

1. Show $\mathrm{QOU}_q$ is rational in $q$ (each structure
   constant is in $\mathbb{Q}(q)$).

2. Show evaluation at any non-pole $q \in \mathbf{No}$ is
   well-defined. Use `QOU.AppendixSurreals.omegaSurreal`,
   `epsilonSurreal`.

3. Show $\mathrm{St}_{\mathrm{QOU}} \circ \mathrm{ev}_{q = \omega}$
   and $\mathrm{St}_{\mathrm{QOU}} \circ \mathrm{ev}_{q = 1 +
   \varepsilon^\omega}$ both produce well-defined archimedean QOUs
   (modulo
   [archimedean-stpart](#conj:archimedean-stpart)).

**Provable in Lean today**:
- `c_q_eq_omega_at_one_plus_epsilon` already proved in
  `QOU.AppendixSurreals.Conjectures`: $c_q = (q-1)^{-1}$ at
  $q = 1 + \varepsilon$ equals $\omega$.

**Required infrastructure** (interpretation):
- A definition of "cosmological time" as an ordering on the
  parameter $q \in \mathbf{No}$.
- A categorical-cosmology framework distinguishing "moment"
  (= a specific $q$) from "evolution" (= a path in $\mathbf{No}$).
- Such a framework is **not** developed in the main paper.

**Falsification path** (mathematical): show that the QOU
structure constants have *poles* at $q = \omega$ or
$q = 1$ in $\mathbf{No}$ that prevent evaluation. This is false
for the rational-in-$q$ formulas, so the evaluation is well-
defined.

**Falsification path** (interpretive): show that the
"cosmological time" reading is incompatible with QOU's
parameter-time symmetry (the substrate $q$ does not evolve in
the main paper). This is the most natural objection, and the
appendix's caveat already concedes it.

**Provability assessment**: the mathematical kernel is
provable in Lean modulo the sub-conjectures. The cosmological
interpretation is a separate matter, deliberately bracketed.
<!-- FILE_END: bigbang-heatdeath.md -->

<!-- FILE_START: cosmological-cone-visualization.md -->
**Visualization aid.**  Picture the substrate-parameter axis
$q \in \mathbb{R}_{>0}$ ([substrate parameter](#def:substrate-parameter))
as the radial coordinate of a schematic cone with two named
endpoints from
[Big Bang / heat death](#conj:bigbang-heatdeath):

| endpoint | $q$ | structure constants | geometric reading |
|---|---|---|---|
| Big Bang | $q \to 1^+$ | $c_q = 1/(q-1) \to \infty$, $\hbar_q = (q-1)/q \to 0$ | "apex": all states causally connected, no time separation |
| heat death | $q \to \infty$ | $c_q \to 0$, $\hbar_q \to 1$ | "asymptotic base": classical and quantum scales of action saturate |

At every interior $q$, each cross-section of the cone carries a
copy of the Reeb bundle $\mathcal{R}_p \cong S^3$ over the
exceptional divisor $\mathcal{S}_p$
([exceptional divisor](#def:exceptional-divisor)) at brane point
$p$, with the three color sectors
$\mathfrak{r}, \mathfrak{g}, \mathfrak{b}$
([color-sector coordinates](#def:color-sector-coords)) threaded
along the cone under the color twist $q\phi$.  As $q$ varies the
embedding $(O, R, T_1, T_2, N)$ deforms continuously, sweeping the
sectors through their $q$-deformed positions while the underlying
$\mathcal{S}_p$-topology is preserved.

**Direction mnemonic.**  *Light speed $c_q$ diverges at the Big
Bang*, i.e.\ at $q \to 1^+$, and $\hbar_q$ saturates to $1$ at
heat death, i.e.\ at $q \to \infty$.  The direction is recorded
in [Big Bang / heat death](#conj:bigbang-heatdeath); we restate
it here because the two endpoints are easy to swap.

**Scope and limitations.**  The cone is a schematic mnemonic for
the $q$-parameter family of QOUs.  It does *not*

- introduce a metric on the parameter axis (no claim that
  $r = \sqrt{t}$ or any specific cone angle is physical);
- commit the paper to a cosmological-time reading of $q$
  (parameter-time symmetry is preserved);
- promote [Big Bang / heat death](#conj:bigbang-heatdeath) from
  conjecture to theorem — the endpoint functors remain
  speculative, as that block's caveat records.

The visualization is included only to give a reader picking up the
paper from Chapter 7 onward a unifying picture for how the
substrate parameter, the exceptional divisor, the Reeb bundle, and
the color sectors fit on a single axis.
<!-- FILE_END: cosmological-cone-visualization.md -->

