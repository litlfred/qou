The SDP multiplicity $\rho \in \mathbb{Z}_{>0}$ in the mass formula

$$
  B(\mathfrak{H}) \;=\; m_e \cdot \rho \cdot M(\mathfrak{H})\big|_{q = q_0}
$$

is currently determined case-by-case as a numerical by-product of
the Wedderburn SDP search.  This conjecture proposes a structural rule
for $\rho$ in terms of the categorical data of $\mathfrak{H}$.

## Statement

**Conjecture.**
*Let $\mathfrak{H}$ be a confined particle/atom
([confined particle](#def:confined-particle)) with canonical Hecke
element $T_w \in H_{n_0}(q)$.  The SDP multiplicity is:*

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

## Evidence

The SDP witnesses for all four currently identified particles give:

| Particle | Knot | $n_0$ | Dominant $\lambda^*$ | $\dim_q(\lambda^*)$ at $q_0$ | Obs.\ $\rho$ |
|----------|------|-------|---------------------|------------------------------|--------------|
| Proton/neutron | trefoil $3_1$ | $3$ | $(2,1)$ | $[2]_{q_0} \approx 2.22$ → rounded $\rho = 1$? | $1$ |
| Deuterium $^2$H | $6_2$ | $6$ | $(3,2,1)$ | $[5]_{q_0}/\cdots \approx 1.0$? | $1$ |
| Tritium $^3$H | $8_{11}$ | $6$ | $(3,3)$ | $[2]_{q_0} \approx 2.22$ → $\rho = 2$ | $2$ |
| Helium-3 $^3$He | $L_{6a4}$ | $6$ | $(3,3)$ | $[2]_{q_0} \approx 2.22$ → $\rho = 2$ | $2$ |

The pattern $\rho = \lfloor\dim_q(\lambda^*)\rceil$ (nearest integer
rounding) is consistent with all known cases, but the rule relating
$\lambda^*$ to $(2,1)$ vs.\ $(3,3)$ as the dominant summand has not
been derived from first principles.

## The rounding question

The exact quantum dimension $[2]_{q_0} = q_0 + q_0^{-1} \approx 2.01$
(with $q_0 \approx 1.1097$), so $\dim_q((2,1)) \approx 2.01$.  The
floor gives $\rho = 2$, but the proton/neutron uses $\rho = 1$.  This
suggests the rule may be:

$$
  \rho(\mathfrak{H})
  \;=\;
  \begin{cases}
    1 & \text{if $\lambda^*$ is the hook partition $(n_0-1, 1)$,} \\
    \lfloor\dim_q(\lambda^*)\rceil & \text{otherwise.}
  \end{cases}
$$

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
([`folio-assistant/computations/rho_prefactor_structural_verifier.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/rho_prefactor_structural_verifier.py),
witness [`rho-prefactor-structural-verifier.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/rho-prefactor-structural-verifier.witness.json))
**falsifies** the simple form of the rule "$\rho = \mathrm{round}[\dim_q(\lambda^*)]$" when
$\lambda^*$ is computed from the *braid strand count* alone:

| atom | knot braid | dominant $\lambda^* \vdash 3$ | $\dim_q$ at $q_0$ | obs $\rho$ |
|------|-----------|------------------------------|--------------------|------------|
| proton  | $(\sigma_1 \sigma_2^{-1})^3$  | $(2,1)$ | $2.011$ | $\mathbf{1}$ |
| neutron | $(\sigma_1 \sigma_2^{-1})^3$  | $(2,1)$ | $2.011$ | $\mathbf{1}$ |
| ²H ($6_2$) | $\sigma_1 \sigma_2^{-1} \sigma_1^3 \sigma_2^{-1}$ | $(3)$ | $1.000$ | $\mathbf{1}$ |
| ³He ($L_{6a4}$) | $(\sigma_1^{-1} \sigma_2)^3$ | $(2,1)$ | $2.011$ | $\mathbf{2}$ |

Proton, neutron, and ³He have **identical** $\chi_\lambda$ values across all
three blocks — their braid words are mutual inverses (or trivially equal),
hence Markov-equivalent in $H_3(q_0)$.  No rule of the form
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
together (Hopf link $L_H$ for ²H, an $8_{11}$-class link for ³H,
$L_{6a4}$ for ³He).  The dominant $\lambda^* \vdash 3 \cdot A$ of
$K$ — *not* of the whole-particle braid image at $H_3$ — is what
carries the $\rho$ information.

This is the natural framework for the joint-tower SDP cross-level
consistency constraints (4) of
[`prop:joint-tower-sdp-confinement`](#prop:joint-tower-sdp-confinement),
which already enforce $T_w(\mathfrak{H}) \hookleftarrow T_w(\mathfrak{H}')$
across confinement levels.  Wiring an explicit
"binding-K SDP solver mode" — that finds $K(\mathfrak{H})$ from
substrate data + constituent $T_w$'s alone — is the natural
follow-up deliverable for issue #604 (after the H_{3·A} Hoefsmit
infrastructure lands).  The Lean class
[`conj-rho-prefactor-structural.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/conj-rho-prefactor-structural.lean)
records `A` (not the braid strand count) as its primary parameter and
derives $n_0 = 3 \cdot A$ structurally; per-atom instances must be
constructed at $H_{3 \cdot A}$ to discharge the rule.

## Relationship to GAP-A-4

This conjecture directly addresses GAP-A-4 of the
[derivation audit report](#prose:derivation-audit-report).
