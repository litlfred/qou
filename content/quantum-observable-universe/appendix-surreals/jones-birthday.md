The Jones polynomial $J_K(q) \in \mathbb{Z}[q^{\pm 1/2}]$ is the Markov trace $\mathrm{tr}_M(\rho_n(\beta))$ of the Hecke representation of any braid word $\beta$ whose closure is the oriented link $K$. The Markov trace sums contributions from every standard tableau $t$ of every two-rowed shape $\lambda \vdash n$.

By [Hoefsmit-is-surreal-construction](#prop:hoefsmit-is-surreal-construction), each tableau $t$ corresponds to a finite-dyadic surreal $\Phi(t) \in \mathbf{No}$ of birthday $\leq n$. This suggests that the Jones polynomial admits a **birthday refinement**: a finer invariant that records contributions stratified by the birthday of the underlying surreal sign sequence.

## Conjecture

There exists a refinement:

$$
  \widetilde{J}_K \in \mathbb{Z}[q^{\pm 1/2}]^{\mathrm{Ord}}
$$

This acts as a function from ordinals to Laurent polynomials in $q^{1/2}$ satisfying:

1. **Recovery of Jones**: The sum $\sum_\alpha \widetilde{J}_K(\alpha) = J_K(q)$ converges to the classical Jones polynomial over all birthdays.
2. **Birthday locality**: $\widetilde{J}_K(\alpha)$ depends only on tableau contributions of YJM depth $\leq \alpha$.
3. **Strict refinement**: There exist knots $K_1, K_2$ with the same Jones polynomial $J_{K_1}(q) = J_{K_2}(q)$ but distinct birthday refinements $\widetilde{J}_{K_1} \neq \widetilde{J}_{K_2}$.

If condition (3) holds, $\widetilde{J}_K$ is a strictly stronger invariant than the Jones polynomial. This contradicts the classical view that the Markov trace collapses all braid-word information.

## Plausibility

The Jones polynomial loses information for two reasons:

1. **Markov-trace averaging**: We add contributions from distinct tableaux $t, t'$ of the same shape $\lambda$. The trace cannot distinguish them.
2. **Tableau-shape averaging**: We weight contributions from distinct shapes by quantum dimensions $\dim_q(\lambda)$.

The birthday refinement preserves the Markov-trace averaging but stratifies by YJM depth. This is a finer invariant than the shape. We separate contributions from "early" symmetric channels ($q$-eigen choices at low YJM steps) from "late" symmetric channels.

Precedent exists. The Khovanov homology and other categorifications of the Jones polynomial act as strictly stronger invariants. The birthday refinement is not a categorification. It produces numbers, not chain complexes. However, both refinements expose previously hidden tableau-level data.

## Criteria for proof or disproof

- **Proof**: Produce two knots with identical Jones polynomials and distinct birthday refinements, computed via Hoefsmit's matrix entries at each YJM step.
- **Disproof**: Show that the YJM-depth filtration of any tableau contributes only via its endpoint (the shape $\lambda$), not its trajectory. This collapses the refinement to the Jones polynomial.

The Conway--Kinoshita pair $(11n34, 11n42)$ provides a classical example of two knots distinguished by Khovanov homology but not by the Jones polynomial. We can test the birthday refinement against this pair.

## Open problem

The conjecture remains open. The Hoefsmit eigenchannel data gives closed formulas. We can compute the refinement. The question is whether it is non-trivial.

## Proof strategy

We pursue a direct computational attack without new theory:

1. **Compute** $\widetilde{J}_K$ for the smallest pair of knots sharing a Jones polynomial. We use Conway's $11n34, 11n42$. Both are eleven-crossing knots. The YJM tableau trees have depth $\leq 11$.
2. **Sum over tableau trajectories**. For each YJM-extension path $\pi$ of length 11 in either knot, we compute the Hoefsmit matrix product along $\pi$. We convert to a sign sequence via `signSequenceOfBraid`. We compute the Gonshor surreal of each path.
3. **Aggregate by birthday**. We group contributions by $b(\mathrm{Gonshor}(\pi))$ and sum coefficients. The result is $\widetilde{J}_K$.
4. **Compare**. If $\widetilde{J}_{11n34} \neq \widetilde{J}_{11n42}$, we establish the conjecture with a single example.

**Required infrastructure**:
- Hoefsmit matrix entries for $H_{11}(q)$ (closed-form).
- The `gonshor` map for finite sign sequences (provided by `QOU.AppendixSurreals.gonshor`).
- A Python/Lean script computing matrix products along YJM paths.

**Falsification path**: Prove that the Hoefsmit-trajectory sum factors through the YJM endpoint (= shape $\lambda$). The birthday refinement then equals the partition-summed Markov trace. This reduces $\widetilde{J}_K$ to $J_K$ identically.

**Provability assessment**: Computational verification is feasible in days. Lean formalization requires only the existing `gonshor` module plus a Hoefsmit-matrix module.odule.
