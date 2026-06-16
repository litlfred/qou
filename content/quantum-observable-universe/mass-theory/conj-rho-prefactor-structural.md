The SDP multiplicity $\rho \in \mathbb{Z}_{>0}$ in the mass formula

$$
  B(\mathfrak{H}) \;=\; m_e \cdot \rho \cdot M(\mathfrak{H})\big|_{q = q_0}
$$

is currently determined case-by-case as a numerical by-product of
the Wedderburn SDP search. This conjecture proposes a structural rule
for $\rho$ in terms of the categorical data of $\mathfrak{H}$.

## Statement

**Conjecture.**
*Let $\mathfrak{H}$ be a confined particle/atom
([confined particle](#def:confined-particle)) with canonical Hecke
element $T_w \in H_{n_0}(q)$. The SDP multiplicity is:*

$$
  \rho(\mathfrak{H})
  \;=\;
  \dim_q\!\bigl(\lambda^*(T_w)\bigr),
$$

*where $\lambda^*(T_w)$ is the **dominant Young diagram** in the
Wedderburn decomposition of $T_w$: the partition $\lambda \vdash n_0$
maximizing $|y_\lambda(q_0) \cdot \chi_\lambda(T_w)|$
([Markov trace expansion](#prop:wedderburn-trace-identity),
[Wenzl-bridge weights](#prop:alpha-k-derivation-procedure)).*

*The quantum dimension $\dim_q(\lambda) = [d_\lambda]_q$ where
$d_\lambda$ is the number of standard Young tableaux of shape
$\lambda$ (hook-length formula).*

## Evidence (heuristic, pre-binding-K refinement)

The SDP witnesses for all four currently identified particles give the
following heuristic table. **Caveat (issue #604, deliverable 4):** the
"Dominant $\lambda^*$" entries here are *conjectural* and were
populated before the $H_{3 \cdot A}$ binding-K analysis below; they are kept
for historical reference and reconciliation with the older narrative.
The numerically verified rule (see "Critical structural finding" below)
must be evaluated at the atomic strand count $n_0 = 3 \cdot A$:

| Particle | Knot | $n_0 = 3\cdot A$ | Conjectural dominant $\lambda^*$ | $\dim_q(\lambda^*)$ at $q_0$ | Obs.\ $\rho$ |
|----------|------|------------------|----------------------------------|------------------------------|--------------|
| Proton/neutron | trefoil $3_1$ | $3$ ($A=1$) | $(2,1)$ | $[2]_{q_0} \approx 2.01$ $\to$ $\rho = 1$ (hook special case) | $1$ |
| Deuterium $^2$H | $6_2$ | $6$ ($A=2$) | $(3,2,1)$ | $\approx 1.0$ | $1$ |
| Tritium $^3$H | $8_{11}$ | $9$ ($A=3$) | $(3,3,3)$ (conjectural) | $\approx 2.0$ $\to$ $\rho = 2$ | $2$ |
| Helium-3 $^3$He | $L_{6a4}$ | $9$ ($A=3$) | $(3,3,3)$ (conjectural) | $\approx 2.0$ $\to$ $\rho = 2$ | $2$ |

The earlier draft of this table (pre-deliverable-4) listed
$n_0 = 6$ for ${}^{3}$H/${}^{3}$He, which conflicted with the joint-tower SDP
convention $n_0 = 3 \cdot A$ used in
[`prop:joint-tower-sdp-confinement`](#prop:joint-tower-sdp-confinement)
and in
[`joint-tower-sdp-h6-h9.witness.json`](https://github.com/litlfred/qou/blob/main/computations/joint-tower-sdp-h6-h9.witness.json)
(`atomic_n_0 = 9` for ${}^{3}$H, ${}^{3}$He). This table is now reconciled to
$n_0 = 3 \cdot A$. The conjectural $\lambda^* \vdash 9$ entries
remain to be verified once Hoefsmit at $H_9$ is implemented (deferred
— see "Critical structural finding" below).

The pattern $\rho = \mathrm{round}[\dim_q(\lambda^*)]$ (nearest-integer
rounding) is consistent with the four known cases under the
hook-special-case caveat; the rule relating $\lambda^*$ to specific
shapes has not been derived from first principles.

## The rounding question

The exact quantum dimension $[2]_{q_0} = q_0 + q_0^{-1} \approx 2.01$
(with $q_0 = 1.109978595554181\ldots$ (50 dps)), so $\dim_q((2,1)) \approx 2.01$. The
nearest-integer round gives $\rho = 2$, but the proton/neutron uses
$\rho = 1$. This suggests the rule may be:

$$
  \rho(\mathfrak{H})
  \;=\;
  \begin{cases}
    1 & \text{if $\lambda^*$ is the hook partition $(n_0-1, 1)$,} \\
    \mathrm{round}[\dim_q(\lambda^*)] & \text{otherwise.}
  \end{cases}
$$

(The symbol $\lfloor \cdot \rceil$ in earlier drafts denotes
*round-to-nearest*, not floor. The Lean class
[`conj-rho-prefactor-structural.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/conj-rho-prefactor-structural.lean)
encodes this as the inequality
$|\rho - \dim_q(\lambda^*)| \leq 1/2$.)

Alternatively, the correct $\rho$ may count the number of
**orthogonal Wedderburn copies** that fit inside the SDP feasible
region of the mass formula, which would give $\rho = 1$ for single-copy
and $\rho = 2$ for double-cover nuclei.

## Proof obligations

1. Identify the dominant $\lambda^*$ for each particle from the
 Markov-weight data and show it is $\lambda^* = (2,1)$ for proton
 and $(3,3)$ for $^3$H/$^3$He.

2. Show the multiplicity rule (exact quantum dimension, rounded, or
 orthogonal-copy count) reproduces the known $\rho$ values.

3. Provide a categorical interpretation of $\rho$: it should count
 a natural structural quantity of the confinement-SDP solution space
 (orthogonal copies, Wedderburn summand multiplicity, etc.).

4. Extend the rule to heavier nuclei $A \leq 60$ in the recursive
 atom-knot atlas and verify no per-atom re-tuning is needed.

## Critical structural finding (issue #604, deliverable 4)

The B_3-level numerical evaluation
([`computations/rho_prefactor_structural_verifier.py`](https://github.com/litlfred/qou/blob/main/computations/rho_prefactor_structural_verifier.py),
witness [`rho-prefactor-structural-verifier.witness.json`](https://github.com/litlfred/qou/blob/main/computations/rho-prefactor-structural-verifier.witness.json))
**falsifies** the simple form of the rule "$\rho = \mathrm{round}[\dim_q(\lambda^*)]$" when
$\lambda^*$ is computed from the *braid strand count* alone:

| atom | knot braid | dominant $\lambda^* \vdash 3$ | $\dim_q$ at $q_0$ | obs $\rho$ |
|------|-----------|------------------------------|--------------------|------------|
| proton | $(\sigma_1 \sigma_2^{-1})^3$ | $(2,1)$ | $2.011$ | $\mathbf{1}$ |
| neutron | $(\sigma_1 \sigma_2^{-1})^3$ | $(2,1)$ | $2.011$ | $\mathbf{1}$ |
| ${}^2$H ($6_2$) | $\sigma_1 \sigma_2^{-1} \sigma_1^3 \sigma_2^{-1}$ | $(3)$ | $1.000$ | $\mathbf{1}$ |
| ${}^{3}$He ($L_{6a4}$) | $(\sigma_1^{-1} \sigma_2)^3$ | $(2,1)$ | $2.011$ | $\mathbf{2}$ |

Proton, neutron, and ${}^{3}$He have **identical** $\chi_\lambda$ values across all
three blocks — their braid words are mutual inverses (or by definition equal),
hence Markov-equivalent in $H_3(q_0)$. No rule of the form
"$\rho = f(\chi_\lambda, y_\lambda)$ at the braid strand count" can
distinguish $\rho_{\mathrm{p}} = 1$ from $\rho_{^3\mathrm{He}} = 2$.

### Required structural refinement: atomic strand count $n_0 = 3 \cdot A$

The conjecture must be evaluated at the **atomic** strand count
$n_0 = 3 \cdot A$, embedding the braid into $H_{3 \cdot A}(q_0)$
**through the binding operator**:

$$
T_w(\mathfrak{H})
\;=\;
\underbrace{K(\mathfrak{H})}_{\text{binding link} \,\in\, H_{3A}(q_0)}
\,\cdot\,
\underbrace{\bigotimes_{i=1}^{A} T_w(\text{nucleon}_i)}_{\text{constituents at } H_3(q_0)^{\otimes A}}.
$$

The binding operator $K(\mathfrak{H})$ links the $A$ nucleon-trefoils
together (Hopf link $L_H$ for ${}^2$H, an $8_{11}$-class link for ${}^3$H,
$L_{6a4}$ for ${}^{3}$He). The dominant $\lambda^* \vdash 3 \cdot A$ of
$K$ — *not* of the whole-particle braid image at $H_3$ — is what
carries the $\rho$ information.

This is the natural framework for the joint-tower SDP cross-level
consistency constraints (4) of
[`prop:joint-tower-sdp-confinement`](#prop:joint-tower-sdp-confinement),
which already enforce $T_w(\mathfrak{H}) \hookleftarrow T_w(\mathfrak{H}')$
across confinement levels. Wiring an explicit
"binding-K SDP solver mode" — that finds $K(\mathfrak{H})$ from
substrate data + constituent $T_w$'s alone — is the natural
follow-up deliverable for issue #604 (after the $H_{3 \cdot A}$ Hoefsmit
infrastructure lands). The Lean class
[`conj-rho-prefactor-structural.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/conj-rho-prefactor-structural.lean)
records `A` (not the braid strand count) as its primary parameter and
derives $n_0 = 3 \cdot A$ structurally; per-atom instances must be
constructed at $H_{3 \cdot A}$ to discharge the rule.

## Closure path via the canonical-knot-id

GAP-A-4 closes *as a corollary* of GAP-A-1 (canonical knot
identification): once the canonical $T_w$ for a nucleus is uniquely
fixed by the R5-full SDP, the dominant Wedderburn summand
$\lambda^*(T_w)$ is uniquely determined, and $\rho = [d_{\lambda^*}]_q$
follows from the Wedderburn trace identity.

The Lean side is now stated as
[`rho_eq_qdim_via_canonical_knot`](conj-rho-prefactor-structural.lean)
in `conj-rho-prefactor-structural.lean`. 's R5-full witness
records $\rho_\star$ per atom directly:

| Atom | Witness $\rho_\star$ | Notes |
|------|----------------------|-------|
| $^3\mathrm{He}$ | $3$ | At canonical $T_w = L_{6a4}$ |
| $^2\mathrm{H}$ | $3$ | At prototype's L=8 winner $\sigma_2 \sigma_1^6 \sigma_2^{-1}$ — **not** the historical $\rho = 1$ |

The deuterium discrepancy is because the prototype's single-term
cost function does not select $6_2$ at first principle (
"${}^2$H needs multi-term wiring"). Once T2--T6 of
[`thm:knot-mass-formula-unified`](#thm:knot-mass-formula-unified)
land in `cost_for_candidate`, the historical $\rho = 1$ at $6_2$
should be recovered.

For $^3\mathrm{He}$ the $\rho_\star = 3$ value is consistent with
the dominant-$\lambda^*$ rule once the orthogonal-copies
interpretation is invoked (the historical assignment $\rho = 2$
referred to the double-cover hadronic factor; the SDP's
$\rho_\star$ counts a different structural quantity).
Reconciling the two interpretations is the residual open piece
of obligation 3.

## Relationship to GAP-A-4

This conjecture directly addresses GAP-A-4 of the
[derivation audit report](#prose:derivation-audit-report).
