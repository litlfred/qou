Let $U \subset M_0$ be an affine chart carrying a bundle initial
condition $\mathcal{S}_0 = \sum_i (p_i, H_i)$
([bundle initial conditions](#def:bundle-initial-conditions)).

A **big bang state** is a bundle initial condition in which the
degree-$0$ algebra is trivial:

$$
  \mathcal{S}_0 \text{ is a big bang state}
  \quad\Longleftrightarrow\quad
  \Gamma\!\bigl(U,\, A_0|_{\mathcal{S}_0}\bigr) = 0.
$$

Equivalently, every constituent satisfies $H_i = \varnothing$
(photon with zero fibre data) and the section $s_0 \in \Gamma(U, A_0)$
encoding their identity vanishes: there are **no degree-$0$
observables** at $\mathcal{S}_0$.  What remains is the higher-jet
data: sections of $A_1/A_0$ (linear transport) and $A_2/A_0$
(curvature), which provide the seed for the forward light cone
$\mathcal{S}_1, \mathcal{S}_2, \ldots$

**Relation to the jet horizon.**
A big bang state is algebraically identical to the data on one
side of a jet horizon
([jet horizon](#def:jet-horizon)): both are characterised by the
vanishing of $A_0$.  The difference is contextual:

| Concept | Algebraic condition | Role |
|:--------|:---:|:---|
| Jet horizon | $A_0\vert_{\mathcal{H}} = 0$ | Boundary within an affine chart |
| Big bang state | $A_0\vert_{\mathcal{S}_0} = 0$ | Reference configuration of an affine chart |

A jet horizon is a **boundary**; a big bang state is an
**initial condition**.  The same vanishing ideal $\mathfrak{h}$
describes both.

**Existence is not assumed.**
Whether any affine chart in the descended universe admits a big
bang state is a dynamical question, not an axiom.  It is
consistent with the framework that:
- every affine chart has a big bang state (global initial singularity),
- some charts do and others do not,
- no chart does (the backward light cone extends indefinitely).
