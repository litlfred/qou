**Axiomatic Markov-closure map**, reducing the open content to two atomic axioms.

As set out in [`rem:F3-eps6-leading-eq-neg-2b-cubed`](#rem:F3-eps6-leading-eq-neg-2b-cubed), the substantive open content of $c_3 = J_{\text{Hopf}}(q=1) = -2$ lives in the 3-fold Markov closure $\to$ Hopf-link substructure identification.

We factorise that content into two atomic axioms:

## The two atomic axioms

1. **Markov-closure of a 2-strand 2-crossing braid is the Hopf link**:
   $$\widehat{\sigma_1^2 \in B_2} \;=\; \text{Hopf link}$$
   This is the Alexander-Markov closure theorem applied to a specific case.

2. **Classical Jones value of the Hopf link**:
   $$J_{\text{Hopf}}(q{=}1) \;=\; -2$$
   Already proved in Lean ([`F3-eps6-leading-eq-neg-2b-cubed.lean`](F3-eps6-leading-eq-neg-2b-cubed.lean)) via `unfold + norm_num`.

## Result

The previous `ThreeFoldMarkovHopfExtraction` class had a single broad axiomatic field. Now, that content is split into two atomic axioms, each representing a recorded knot-theoretic result:

| atomic axiom | known result | Lean status |
|---|---|---|
| `closure 2 = Hopf link` | Alexander-Markov | type axiom |
| `jones_at_one 2 = -2` | Jones 1985 | proved (`unfold + norm_num`) |

A full formalisation therefore targets only the first atom; the second is already closed.

**Archimedean specialisation.** What follows invokes real- or complex-analytic constructs. Generic categorical identities remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
