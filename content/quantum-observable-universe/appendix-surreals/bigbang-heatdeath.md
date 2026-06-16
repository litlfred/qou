## Status

**Highly speculative** and outside the appendix's main thrust.
It is included to record an evident application of named-surreal
calculus (Big Bang $\sim$ $1 + \varepsilon^\omega$;
heat death $\sim$ $\omega$) without claiming any of the
physics-of-cosmology details. The QOU paper does not commit to
any particular cosmological reading, and this conjecture should
not be read as such.

The mathematical content — that the QOU functors evaluate at
named infinite/infinitesimal surreals — is correct (rational
expressions in $q$ make sense at any non-pole element of
$\mathbf{No}$). The interpretive content — that these are *the*
Big Bang and heat death — is metaphor, pending a separate
discussion of cosmological time in QOU.

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

## What this would buy

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
