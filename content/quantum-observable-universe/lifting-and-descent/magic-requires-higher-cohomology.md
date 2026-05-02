## Statement

**Proposition 8 (magic requires higher-cohomological knot operator).**
*Let $T^*(n, q_0)$ be the canonical SDP optimum at strand count $n$
and substrate $q_0$. In the spectral-sequence decomposition*

$$
  T^*(n, q_0)
  \;=\;
  \sum_{p, q}\, T^*_{p, q}(n, q_0)
  \quad\text{with}\quad
  T^*_{p, q} \in E_\infty^{p, q}(n)
$$

*from [`conj:homological-shell-condensation`](#conj:homological-shell-condensation),
the magic predicate is*

$$
  n \text{ magic at } q_0
  \;\Longleftrightarrow\;
  \exists\, p,\, q \geq 1
  \;\text{such that}\;
  T^*_{p, q}(n, q_0) \neq 0.
$$

*Equivalently:*

$$
  n \text{ non-magic at } q_0
  \;\Longleftrightarrow\;
  T^*(n, q_0) \in E_\infty^{0, *}(n)
  \;\;\text{(purely descended / Markov-trace piece)}.
$$

## Status

**Conjecture** (CLAUDE.md §3b axiom-class). Sharp framework claim:
the cohomological degree of the active SDP operator separates magic
from non-magic.

## Topological reading

The framework's spectral-sequence pages have direct topological
content (per [`conj:mass-endomorphism`](#conj:mass-endomorphism)):

| $E_\infty$ slot | Topological content | Knot class |
|---|---|---|
| $E_\infty^{0, *}$ | descended Markov trace $\lvert\mathrm{tr}_M(\rho(\beta))\rvert$ | **Hopf-decomposable** (Seifert-fibered, simple) |
| $E_\infty^{1, *}$ | brane-tower level 1: $\Phi_q(z_1)$ | non-Hopf, single jet prolongation |
| $E_\infty^{2, *}$ | brane-tower level 2: $\Phi_q(z_2)$ | higher jet, hyperbolic class |

**Hopf link** ($T_{2,2}$) is the simplest non-trivial 2-component
link:

- Crossing number $2$ (minimum for non-trivial).
- Hyperbolic volume $0$ (Seifert-fibered, **not** hyperbolic).
- Complement $S^3 \setminus \mathrm{Hopf} \simeq T^2$ — cohomology
  rank $\leq 2$ throughout.
- Lives entirely in $E_\infty^{0, *}$ (descended trace).

**Bring-embeddable torus knots** ([`prop:torus-knot-shell-binding`](#prop:torus-knot-shell-binding)):

The six knots $\{T_{2,3}, T_{2,5}, T_{2,7}, T_{2,9}, T_{3,4},
T_{3,5}\}$ that embed on Bring's surface
([`def:brings-surface`](#def:brings-surface)) are NON-Hopf — each
has crossing number $\geq 3$, distinguished Alexander polynomial,
and lives in $E_\infty^{p, q \geq 1}$.

The existing `prop:torus-knot-shell-binding` derives the empirical
magic ladder $\{2, 8, 20, 28, 50, 82, 126\}$ as cumulative shell
sizes from these six torus knots. Combined with this proposition:
**the SDP at magic $n$ selects the corresponding Bring torus knot**
(non-Hopf, higher cohomological degree); at non-magic $n$ the SDP
selects a Hopf-decomposable operator.

## Why this unifies the framework

Three previously-separate framework claims now align:

1. **Mass-endomorphism decomposition** ([`conj:mass-endomorphism`](#conj:mass-endomorphism))
   says the descended $\mathrm{tr}_M$ contributes $\lesssim 0.5\%$
   of the magic-shell binding; the rest comes from the brane tower
   ($E^{p, q \geq 1}$ pieces). This proposition explains *why*: at
   magic $n$, the active operator inherently lives in higher
   cohomological degree.

2. **Spectral-sequence collapse** ([`conj:homological-shell-condensation`](#conj:homological-shell-condensation))
   says $E_\infty^{p, >0}(n) = 0$ at magic $n$. This proposition
   refines: the *total* spectral sequence collapses, but the
   *ground-state contribution* $T^*$ is non-zero precisely in
   $E_\infty^{p, q \geq 1}$. The collapse means no further
   obstructions; the surviving piece is in higher cohomology.

3. **Bring-shell-binding** ([`prop:torus-knot-shell-binding`](#prop:torus-knot-shell-binding))
   says the six embeddable torus knots generate the magic ladder.
   This proposition says these knots are EXACTLY the operators that
   live in $E_\infty^{p, q \geq 1}$ (non-Hopf cohomological class).

## Falsification path

For each $n \in \{1, 2, \ldots, 30\}$, run the SDP at $q_0$ and
extract $T^*(n, q_0)$. Decompose $T^*$ in the
$E_r$-page basis and check whether contributions in $E_\infty^{p, q
\geq 1}$ are non-zero. The conjecture predicts: yes at magic $n$,
no at non-magic $n$.

The Bring-torus-knot side of the picture
([`prop:torus-knot-shell-binding`](#prop:torus-knot-shell-binding))
is already empirically established — the shell-size cumulative count
matches. The cohomological-grading side is the new structural
content.

A simplified probe — classify the canonical SDP-active partition
at each $n$ as Hopf-decomposable (purely $E^{0, *}$) or non-Hopf
(has $E^{p, q \geq 1}$ contribution) — is in
[`folio-assistant/computations/cohomology_class_probe.py`](https://github.com/litlfred/qou/blob/claude/qou-algebraic-refactor-1qVFc/folio-assistant/computations/cohomology_class_probe.py).
