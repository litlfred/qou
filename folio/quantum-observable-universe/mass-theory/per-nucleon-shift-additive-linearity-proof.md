### Proof

The per-new-nucleon increment is invariant in 6 transitions
($A : 2 \to 3$, $A : 3 \to 4$, etc.) for both proton and neutron
additions, regardless of starting atom (witness §1). This linearity
identifies the closed form by induction:

- *Base case:* $\mathrm{shift}(D) = 40 = 18 \cdot 1 + 21 \cdot 1 + 1$.
- *Step (+proton):*
  $\mathrm{shift}(Z+1, N) = \mathrm{shift}(Z, N) + 18 = 18(Z+1) + 21N + 1$.
- *Step (+neutron):*
  $\mathrm{shift}(Z, N+1) = \mathrm{shift}(Z, N) + 21 = 18Z + 21(N+1) + 1$.

The base-case $+1$ originates from the **single mixed (p, n)
interface** in pppnnn ordering, contributing
$\alpha((\sigma+\sigma^{-1})/2) = 1$ from the compound-shift theorem.
This matches
[Pole order at $q=0$ of the torus-knot character: $\alpha_{\mathrm{shift}}(T_{p,k}) = k(p-1)$ on $V_{(1^p)}$](#prop:alpha-shift-torus-knot)'s
simplest interface case $\alpha = 1$ for the Hecke-symmetric
average. $\square$

### Generator-decomposition reading of (18, 21)

Each new generator's DP-max contribution to the q=0 pole is 1
(the canonical formalism),
so DP-max increment per new nucleon is $12$. The actual pole
increments are:
- **per-new-proton:** pole $+9$ (cancellation $= 12 - 9 = 3$),
  shift $= 2 \cdot 9 = 18$.
- **per-new-neutron:** pole $+10.5$ (cancellation $= 1.5$,
  half-integer), shift $= 2 \cdot 10.5 = 21$.

#### Categorical verification (proton + deuteron)

Both the per-proton coefficient $18$ and the multi-nucleon
combination $18 + 21 + 1 = 40$ are verified by direct symbolic
Hoefsmit pole-order analysis:

- **Proton ($A = 1$, $H_3$):**
  the canonical formalism
  (witness:
  [proton $H_3$ pole record](../../../computations/per-irrep-pole-proton-h3.witness.json))
  computes $\chi^\lambda_q(\mathcal{B}_p)$ for each $\lambda \vdash 3$
  via the Hoefsmit seminormal, sums
  $\mathrm{tr}_M(\mathcal{B}_p) = \sum_\lambda y_\lambda(q) \chi^\lambda_q(\mathcal{B}_p)$
  with the canonical Wenzl Jones-Markov weights, substitutes $q = u^2$
  (per the $D(u)$ convention from
  the canonical formalism)
  and reports $\mathrm{ord}_{u=0}(\mathrm{tr}_M(\mathcal{B}_p)) = 19$,
  matching $18 \cdot 1 + 21 \cdot 0 + 1$ exactly.
- **Deuteron ($A = 2$, $H_6$):**
  the canonical formalism
  (witness:
  [deuteron $H_6$ pole record](../../../computations/per-irrep-pole-deuteron-h6.witness.json))
  uses three optimisations to make the symbolic $H_6$ analysis
  tractable: (a) cached symbolic $y_\lambda(q)$ from
  the symbolic Wenzl-bridge weights (skipping the >5 min
  symbolic solve at $n = 6$), (b) cached symbolic
  $\chi^\lambda_q(\beta_D)$ in
  [the deuteron $H_6$ character record](../../../computations/chi-deuteron-h6.witness.json)
  (first-run ~131 s, then <1 s), (c) per-term
  $\mathrm{ord}_{u=0}(y_\lambda \cdot \chi^\lambda)$ analysis. The
  per-term maximum is **uniquely $40$ at $\lambda = (4, 1, 1)$**
  (next-highest $39$ at $(4, 2)$); since the maximum is unique,
  lower-order terms cannot cancel it, so
  $\mathrm{ord}_{u=0}(\mathrm{tr}_M(\beta_D)) = 40 = 18 \cdot 1 + 21 \cdot 1 + 1$
  rigorously.

**Reading note.** The per-irrep maximum $\mathrm{ord}_{q=0}^{(-)}\chi^\lambda_q(\mathcal{B}_p) = 11$
(at $\lambda = (2, 1)$); the "$18$" in the formula is the
per-proton additive coefficient of the **full summed** $u$-pole
order of $\mathrm{tr}_M$, NOT the q-pole order of any single per-irrep
$\chi^\lambda_q$.

The cancellation count enumerates the $\sigma^2$-relation reductions
($\sigma^2 = h\sigma + 1$ in the Hecke quadratic) in the new
nucleon's intrinsic $\sigma^{\pm 1}$-adjacencies plus its incoming interface contribution.
