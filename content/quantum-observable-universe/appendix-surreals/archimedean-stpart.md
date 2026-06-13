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

## What this would unlock

If true, the appendix's $\varepsilon$-relaxation is a *strict*
generalisation of the main paper:

1. The main paper's QOU axioms are recovered as
 $\mathrm{St}_{\mathrm{QOU}}$ applied to the surreal axioms.
2. Every theorem proved in the main paper has a surreal
 counterpart; the surreal counterpart may have additional
 non-trivial first-order corrections that vanish under
 $\mathrm{St}$.
3. Future work can investigate whether these corrections are
 physically meaningful (e.g., explain corrections to the QOU
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
