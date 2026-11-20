**Hopf link as the simplest knot operator.**
The Hopf link $T_{2,2}$ is the simplest non-trivial 2-component link
in the framework's knot-operator basis:

- Crossing number $2$ (minimum for any non-trivial link).
- Hyperbolic volume $0$ (Seifert-fibered, **not** hyperbolic).
- Complement $S^3 \setminus \mathrm{Hopf} \simeq T^2$ — cohomology
 rank $\leq 2$ in every degree.
- Multivariable Alexander polynomial $\Delta(t_1, t_2) = 1$
 (the standard convention for 2-component links is the
 multivariable form; the single-variable $\Delta(t) = 0$ for the
 Hopf link in the literature should not be confused with this).
 In the QOU framework's reading the Hopf link is the
 *by definition-non-trivial* link — its Alexander structure carries
 no signed information, which is the link-theoretic fact behind
 its $E^{0, *}$-only cohomological location.
- Fundamental group: $\mathbb{Z} \oplus \mathbb{Z}$ — abelian.

**Cohomological location in the framework.**
The Hopf link lives entirely in the $E_\infty^{0, *}$ slot of the
brane-tower spectral sequence
([conj:mass-endomorphism](#conj:mass-endomorphism)) — the
*descended Markov-trace* piece. It contributes only the $E^{0, *}$
component of the SDP optimum
([prop:knot-operator-selection](#prop:knot-operator-selection)).

**Non-magic shells use the Hopf link.**
At non-magic $n$ at substrate $q_0$, the SDP optimum
$T^*(n, q_0)$ is **Hopf-decomposable**, expressible as a tensor
product of Hopf links and trivial ribbons. It lives entirely in
$E_\infty^{0, *}$ (the descended Markov-trace piece per
[Mass endomorphism conjecture](#conj:mass-endomorphism)).

**Magic shells require higher-cohomology operators.**
At magic $n$, the SDP optimum requires non-trivial contribution
from $E_\infty^{p, q \geq 1}$ — operators NOT Hopf-decomposable.
By [Shell binding from the torus knot hierarchy: $T_{2,3} \to T_{2,5} \to T_{2,7} \to T_{2,9}$](#prop:torus-knot-shell-binding),
the active operator at each magic $n$ is one of the six
Bring-embeddable torus knots
$\{T_{2,3}, T_{2,5}, T_{2,7}, T_{2,9}, T_{3,4}, T_{3,5}\}$, none of
which is Hopf-decomposable.

**Operational reading of the magic predicate.**
Selection of the active knot operator at strand count $n$ is a
**topological-class** decision:

| $n$ class | Active knot operator | Cohomological grading |
|---|---|---|
| non-magic | Hopf-decomposable (e.g. $T_{2,2}^{\otimes k}$) | $E_\infty^{0, *}$ |
| magic | non-Hopf Bring torus knot ($T_{p, q}$ with $q \geq 3$, $p \in \{2, 3\}$) | $E_\infty^{p \geq 1, q \geq 1}$ |

This matches the empirical mass-decomposition observation
([conj:mass-endomorphism](#conj:mass-endomorphism)) that descended
$\mathrm{tr}_M$ contributes $\lesssim 0.5\%$ of magic-shell binding;
the rest is brane-tower (= higher-cohomological) contribution.
