*Lean sibling: archimedean specialisation over $\mathbb{R}$ (CLAUDE.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**3-fold Markov closure $\to$ Hopf-link substructure $\to$ $c_3 = -2$.**

This proposition formalizes the Track C direction: **proving** the
categorical identification $c_3 = J_{\text{Hopf}}(q=1) = -2$ in the
$Q_\beta$ precision ladder, not just observing it empirically.

## Structural claim

For typed-$B_3$ braids of the form arising in the QOU β-decay
single-wrap construction (proton uud / neutron udd, both 11
typed crossings), the **third-order coefficient $c_3$ in the τ_M
asymptotic expansion** equals the **classical-limit Jones polynomial
of the Hopf link**:

$$
\boxed{
  c_3 \;=\; J_{\text{Hopf}}(q=1) \;=\; -2 .
}
$$

The reason is **not** that the Markov closure of the full typed braid
is the Hopf link — it isn't. Rather, the third-order coefficient
in the perturbative expansion of $\tau_M$ around $q = 1$ (in powers
of $\hbar_q^2$) **factors** through the contribution of **2-strand
sub-braid windings**, whose Markov closure is the Hopf link.

## Per-step categorical chain

The factorization arises from four structural facts:

### Fact 1 — Hecke quadratic at each crossing

Per the Iwahori-Hecke relation, $\sigma_i^2 = h \sigma_i + 1$ in
$H_n(q)$. Repeated application generates a Laurent polynomial in
$q$ at each crossing, with leading $q$-derivative entering at order
$h \sim \hbar_q$.

### Fact 2 — Markov cyclicity at $k$-fold closure

The Markov closure $\widehat{\beta} \in S^3$ of a braid $\beta \in B_n$
respects cyclicity: $\tau_M(xy) = \tau_M(yx)$. At the $k$-th order
in the perturbative expansion of $\tau_M(\beta)$ around $q = 1$, the
combinatorial contribution gathers cyclic permutations of $k$
crossings — equivalently, $k$-fold cyclic substructures of the
underlying braid graph.

### Fact 3 — 2-strand sub-braid extraction at order 3

At order $\hbar_q^6$ (the third perturbative order), the dominant
contribution to $\tau_M(\mathcal{B}_p) - \tau_M(\mathcal{B}_n)$ comes from
**all $\binom{n}{2}$ choices of 2-strand sub-braids** of $\beta$.
For each such 2-strand sub-braid, the Markov closure is the **Hopf
link** (or the unknot, for trivial sub-braids).

The Hopf-link contribution survives at the classical limit; the
unknot contribution is trivial.

### Fact 4 — KL decategorification at $q = 1$

Per CLAUDE.md §7b's Kazhdan-Lusztig decategorification principle, the
mass observable lives in the classical limit. At $q = 1$ the Jones
polynomial of the Hopf link evaluates to:

$$
  J_{\text{Hopf}}(q) \;=\; -q^2 (1 + q^2),
  \qquad
  J_{\text{Hopf}}(q=1) \;=\; -2 .
$$

Combining Facts 1–4: the third-order $\hbar_q^6$ coefficient in
$\tau_M(\mathcal{B}_p) - \tau_M(\mathcal{B}_n)$ factors as

$$
  c_3 \cdot b^3 \cdot \hbar_q^6
   \;=\;
   J_{\text{Hopf}}(q=1) \cdot (\text{Hoefsmit substrate factor}) \cdot \hbar_q^6
   \;=\;
   (-2) \cdot b^3 \cdot \hbar_q^6,
$$

giving $c_3 = -2$ as a **structural prediction**, not an empirical fit.

## Empirical confirmation

Per [`probe_q_beta_gamma_gamma_derivation.py`](../../folio-assistant/computations/probe_q_beta_gamma_gamma_derivation.py),
the prediction is empirically observable:

- N=2 (Kashiwara $b^2$ alone): residual $+1.25$ ppm (above CODATA's
  $0.4$ ppm floor)
- N=3 (+ structural $c_3 = -2$): residual $+0.011$ ppm (within floor)
- **112$\times$ tightening** at N=3 from the structural identification.

This 112$\times$ residual reduction is **observable above CODATA noise**,
empirically validating the categorical-chain prediction.

## Open formalization steps

The Lean stub
[`q-beta-c3-hopf-three-fold-markov.lean`](q-beta-c3-hopf-three-fold-markov.lean)
encodes the chain at three levels:

1. **Axiomatic input class** `ThreeFoldMarkovHopfExtraction` capturing
   Fact 3 (2-strand sub-braid extraction at order 3). This is the
   substantive combinatorial input requiring further development.
2. **Classical-limit identity** $J_{\text{Hopf}}(1) = -2$ as a
   pure-arithmetic theorem (closed by `ring` / `norm_num`).
3. **Top-level export** $c_3 = -2$ conditional on (1) and (2).

The class-axiomatization pattern follows CLAUDE.md §3b's conditional-
class rule for results downstream of an unproved structural input.
