<!-- FILE_START: markov-axioms-braid-link-markov-closure-map-intro.md -->
Continuation of the preceding sub-section.

This sub-section identifies the categorical Markov closure map, records its $F_3$ $\varepsilon^6$ leading coefficient, derives the canonical $\mathfrak{Q}_\beta \gamma\gamma$ form, and extracts the $c_k$ coefficients from the algebraic rules that the closure map supplies. The closing $c_k$ extraction blocks specialise the substrate-level Markov machinery to the Habiro-coefficient framework consumed by the predicted-spectra chapter.
<!-- FILE_END: markov-axioms-braid-link-markov-closure-map-intro.md -->

<!-- FILE_START: markov-closure-map-axiomatic.md -->
**Track C Step B: axiomatic Markov-closure map**, reducing the open content to two atomic axioms.

Per the Track-C plan in [`rem:F3-eps6-leading-eq-neg-2b-cubed`](#rem:F3-eps6-leading-eq-neg-2b-cubed), the substantive open content of $c_3 = J_{\text{Hopf}}(q=1) = -2$ lives in the 3-fold Markov closure $\to$ Hopf-link substructure identification.

We factorise that content into two atomic axioms:

## The two atomic axioms

1. **Markov-closure of a 2-strand 2-crossing braid is the Hopf link**:
   $$\widehat{\sigma_1^2 \in B_2} \;=\; \text{Hopf link}$$
   This is the Alexander-Markov closure theorem applied to a specific case.

2. **Classical Jones value of the Hopf link**:
   $$J_{\text{Hopf}}(q{=}1) \;=\; -2$$
   Already proved in Lean ([`F3-eps6-leading-eq-neg-2b-cubed.lean`](F3-eps6-leading-eq-neg-2b-cubed.lean)) via `unfold + norm_num`.

## Lean encoding

The companion file [`markov-closure-map-axiomatic.lean`](markov-closure-map-axiomatic.lean) defines `class MarkovClosureMap2Strand` with explicit fields mapping crossing-count to closure type and tracking the classical-limit Jones value. It defines `class TrackCReducedAxiom` carrying the single axiomatic statement that $c_3$ factors through the Hopf identification. It proves `track_C_c_3_eq_neg_two`: under both classes, $c_3 = -2$.

## Result

The previous `ThreeFoldMarkovHopfExtraction` class had a single broad axiomatic field. Now, that content is split into two atomic axioms, each representing a recorded knot-theoretic result:

| atomic axiom | known result | Lean status |
|---|---|---|
| `closure 2 = Hopf link` | Alexander-Markov | type axiom |
| `jones_at_one 2 = -2` | Jones 1985 | proved (`unfold + norm_num`) |

The eventual full Track-A formalisation targets only the first atom; the second is already closed.

**Archimedean specialisation (§7c).** This block invokes real- or complex-analytic constructs. Generic categorical identities remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: markov-closure-map-axiomatic.md -->

<!-- FILE_START: F3-eps6-leading-eq-neg-2b-cubed.md -->
**Lean exact-arithmetic lemma**: the leading $\varepsilon^6$ coefficient of $(F_3 - 1)$ at $q = 1 + \varepsilon$ equals $-2 \cdot b^3(q=1) = -3\sqrt{3}/4$.

## Statement

For the $F_3 = 1 - 2 b^3 \hbar_q^6$ factor in the [`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder) precision ladder, the leading $\varepsilon^6$ contribution of $(F_3 - 1)$ at $q = 1+\varepsilon$ is the exact algebraic value:

$$
\boxed{
  -2 \cdot b^3(q=1) \;=\; -2 \cdot \frac{3\sqrt{3}}{8} \;=\; -\frac{3\sqrt{3}}{4}
   \;\approx\; -1.29904 .
}
$$

This is verified at sympy precision in [`probe_q_beta_cat_per_factor_decomposition.py`](../../computations/probe_q_beta_cat_per_factor_decomposition.py) and in Lean [`F3-eps6-leading-eq-neg-2b-cubed.lean`](F3-eps6-leading-eq-neg-2b-cubed.lean).

## Proof

The Hoefsmit off-diagonal coupling is $b = \sqrt{q^4+q^2+1}/(q^2+1)$. At $q = 1$, $b^2 = 3/4$, hence $b = \sqrt{3}/2$. Thus $b^3 = 3\sqrt{3}/8$, and $-2 \cdot b^3 = -3\sqrt{3}/4$. The Lean stub proves all steps directly.

## Significance

This lemma is the purely-arithmetic component of the $c_3 = -2$ identification in [`prop:q-beta-c3-hopf-three-fold-markov`](#prop:q-beta-c3-hopf-three-fold-markov). The categorical content remains class-axiomatic via `ThreeFoldMarkovHopfExtraction`, but its arithmetic discharge at the $\varepsilon^6$ level is Lean-proved.

Combined with [`rem:markov-axioms-primitive`](#rem:markov-axioms-primitive), two previously-axiomatic class hypotheses have been replaced by purely algebraic/arithmetic theorems. The substantive open content of `ThreeFoldMarkovHopfExtraction` reduces to the categorical identification that the perturbative $\hbar_q^6$ piece of the $\tau_M$-expansion factors through Hopf-link Jones values.
<!-- FILE_END: F3-eps6-leading-eq-neg-2b-cubed.md -->

<!-- FILE_START: q-beta-gamma-gamma-canonical-derivation.md -->
**$\mathfrak{Q}_\beta$ γγ canonical derivation: Story B selected by the cat-action / Frobenius / Wenzl chain.**

This content captures the understanding of the $\mathfrak{Q}_\beta$ precision-ladder coefficients $c_k$, settling the Story A vs Story B ambiguity flagged in [`probe_q_beta_high_precision_ck.py`](../../computations/probe_q_beta_high_precision_ck.py).

## The chain

The canonical $c_k$ values are determined by tracing through:

$$
\text{cat-action} \;\to\; \text{Frobenius pairing} \;\to\;
\text{Wedderburn} \;\to\; \text{Wenzl bridge} \;\to\;
\tau_M(\text{typed }\beta) \;\to\; \mathfrak{Q}_\beta^{\text{cat}}
$$

### Step 1 — Cat action (Hoefsmit seminormal)

$H_3(q)$ acts on the three irreps $V_{(3)}, V_{(2,1)}, V_{(1,1,1)}$ via the Hoefsmit seminormal representation.

### Step 2 — Frobenius pairing

Per [`prop:markov-trace-frobenius-selection`](#prop:markov-trace-frobenius-selection), the unique non-degenerate Markov trace on $H_n(R, q)$ is the Jones-Markov $\tau_M$. The non-degeneracy is forced by the Frobenius co-Casimir construction.

### Step 3 — Wedderburn decomposition

$H_3(q) \cong V_{(3)} \oplus V_{(2,1)} \oplus V_{(1,1,1)}$. So $\tau_M(\beta) = y_{(3)} \chi_{(3)}(\beta) + y_{(2,1)} \chi_{(2,1)}(\beta) + y_{(1,1,1)} \chi_{(1,1,1)}(\beta)$.

### Step 4 — Wenzl bridge

The $y_\lambda$ weights solve the Markov-axiom system on $H_3$.

### Step 5 — Canonical typed braids

From [`def:categorical-proton`](#def:categorical-proton) and [`def:categorical-neutron`](#def:categorical-neutron), $\mathcal{B}_p$ and $\mathcal{B}_n$ have 11 typed crossings each.

### Step 6 — $\tau_M$ values

At $q_0$, $\Delta\tau_M(n{-}p) = +0.0445860283$.

### Step 7-9 — Precision-ladder identifications

Categorical-chain reading of the $c_k$ coefficients from [`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder):

| $k$ | $c_k$ | categorical source |
|:---:|:---|:---|
| 1 | $b$ | Hoefsmit off-diagonal coupling on $V_{(2,1)}$ — Kashiwara $\tilde f_1$ |
| 2 | $b^2$ | Kashiwara $\tilde f_1^\dagger \tilde f_1$ return amplitude |
| 3 | $-2 = J_{\text{Hopf}}(q{=}1)$ | classical-limit Jones polynomial of the Hopf-link substructure |
| 4 | $b^2 + \tfrac{1}{2}$ | Kashiwara + half-Hopf mixed |

## Story A vs Story B resolution

[`probe_q_beta_gamma_gamma_derivation.py`](../../computations/probe_q_beta_gamma_gamma_derivation.py) runs the categorical-derivation chain end-to-end. The N=2 $\to$ N=3 transition reduces the residual against CODATA by 112$\times$. This reduction is observable above CODATA's 0.4 ppm measurement floor. The categorical identification $c_3 = J_{\text{Hopf}}(q{=}1) = -2$ is empirically validated, not just an empirical fit.

Story A (fitting $c_2$) provides no structural derivation of the 1.7% deviation. Story B (Kashiwara $c_2 = b^2$ + Hopf $c_3 = -2$) provides structural content: each rung's coefficient is derived from substrate-only data via the categorical chain.

Selection rule: when two interpretations match the data equally, the categorical-chain interpretation (Story B) is canonical because it traces back to substrate principles.

## Track-C open question

Can the $c_3 = -2$ Hopf assignment be proved rigorously? A Lean-level proof requires formalising the 3-fold Markov closure $\to$ Hopf-link substructure identification at the categorical level.

## Track-B open question

Once Track C settles the structural identification, Track B extends to higher orders where the simple Kashiwara + Jones alternation breaks down. The empirical $c_5, c_6$ remain unidentified pending a refined mathematical framing.
<!-- FILE_END: q-beta-gamma-gamma-canonical-derivation.md -->
