# Canonical $(q^2 - 1)$ factor of the Markov trace difference

Assume given canonical Wenzl–Markov weights $y_{(3)}(q)$, $y_{(2,1)}(q)$, and $y_{(1,1,1)}(q)$ satisfying the dimension-normalisation axiom $y_{(3)}(q) + 2 \, y_{(2,1)}(q) + y_{(1,1,1)}(q) = 1$ for $q > 0$. 

Define the canonical trace difference $\Delta\mathrm{tr}_M^{\text{can}}(q)$ as the weighted sum:

$$
  \Delta\mathrm{tr}_M^{\text{can}}(q) =
  y_{(3)}(q) \chi_{(3)}(q)
  + y_{(2,1)}(q) \chi_{(2,1)}(q)
  + y_{(1,1,1)}(q) \chi_{(1,1,1)}(q).
$$

For $q > 0$, the trace difference factors as:

$$
  \Delta\mathrm{tr}_M^{\text{can}}(q) = (q^2 - 1) P^{\text{can}}(q),
$$

where

$$
  P^{\text{can}}(q) = y_{(3)}(q) P_{(3)}(q) + y_{(2,1)}(q) P_{(2,1)}(q) + y_{(1,1,1)}(q) P_{(1,1,1)}(q).
$$

Here $P_\lambda(q)$ are the per-block cofactors, $\chi_\lambda(q) = (q^2 - 1) P_\lambda(q)$. In particular, $\Delta\mathrm{tr}_M^{\text{can}}(1) = 0$.

## Cross-references

- Parent block: [Per-block character closed forms for $\chi_\lambda(\Delta_{T_\beta})(q)$ over $H_3(q)$, antipode pairing, and vanishing at $q = 1$](qbeta-per-block-chi-closed-forms.md) (establishes the per-block $\chi_\lambda$ closed forms and introduces the canonical weights).
- Sibling: [$S(q) = \mathfrak{Q}_\beta(q)/E_0(q)$ vanishes at the classical point $q = 1$ — the SDP-constraint scalar is not the $c_k$ ladder normalization](../mass-theory/q-beta-over-e0-classical-vanishing.md) (shows the classical-point vanishing of the upstream object $S(q) = \mathfrak{Q}_\beta/E_0$).

**Archimedean specialisation.** What follows sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs, physical observables, and numerical evaluation at the substrate parameter $q_0$. Generic categorical or $q$-deformation identities remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
