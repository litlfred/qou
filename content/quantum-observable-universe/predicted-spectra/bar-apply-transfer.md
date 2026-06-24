**Proposition (Bar-transfer principle).**
Let $P \colon \mathbb{R}_{>0} \to \mathrm{Prop}$ be a property of the
substrate parameter that is **bar-invariant**:

$$
  \forall\,q > 0,\quad P(q) \iff P(q^{-1}).
$$

Then for every $a > 0$:

1. **Lower bound transfer.**
   $\bigl(\forall q > a,\; P(q)\bigr) \iff
    \bigl(\forall q < a^{-1},\, q > 0 \Rightarrow P(q)\bigr).$

2. **Two-sided extension.**
   If $a < 1$ and $\bigl(\forall q \in (a, a^{-1}),\, P(q)\bigr)$, then
   $\bigl(\forall q \in \mathbb{R}_{>0} \setminus \{a, a^{-1}\},\,
    P(q)\bigr)$
   does **not** follow in general — but if $P$ is also continuous on
   $\mathbb{R}_{>0}$, the bar-invariance forces $P$ to extend symmetrically
   across both endpoints.

3. **Negation transfer.**
   $\bigl(\exists q < a,\, q > 0 \land \neg P(q)\bigr) \iff
    \bigl(\exists q > a^{-1},\, \neg P(q)\bigr)$.

**Reuse pattern (refactoring).**

The bar-transfer principle says: **any proof of a one-sided
substrate bound for a bar-invariant property automatically yields
the bar-conjugate bound, with no additional argument**.

Concretely, if a previous block proves

$$
  q_0 > 1/\varphi^2 \quad\Rightarrow\quad
  \mathcal{E}_{q_0}\text{ is non-degenerate}
$$

then bar-applying yields, for free,

$$
  q_0 < \varphi^2 \quad\Rightarrow\quad
  \mathcal{E}_{1/q_0}\text{ is non-degenerate}
$$

— i.e., the same property holds on the super-classical wing
$(1, \varphi^2)$ as the proof established on the sub-classical
wing $(1/\varphi^2, 1)$, **without re-running the proof**.

Both derivations may then be folded into a single statement on the
bar-self-dual band $\mathcal{B} = (1/\varphi^2, \varphi^2)$
([bar-self-dual confinement band](#prop:bar-self-dual-confinement-band)).

**Application: stability-margin halving.**

Every two-sided stability statement of the form

$$
  q \in (a, a^{-1}) \Longleftrightarrow \text{stable}
$$

with bar-invariant "stable" is established by proving **only one**
inequality (e.g. $q > a \Rightarrow$ stable). The companion
inequality $q < a^{-1} \Rightarrow$ stable is automatic. This
**halves the proof obligations** for every bar-invariant predicate
in the paper.

Eligible predicates (bar-invariant by construction):

- $\Delta(\mathcal{E}_q) < 0$ (single real component) — bar-invariant
  via [bar T-duality](#prop:bar-t-duality-substrate).
- Slater-strict feasibility of the confinement SDP, when the SDP
  is formulated $\iota$-equivariantly in $q$.
- Markov-trace positivity on the Hecke algebra (bar-invariant by
  $\sigma_i \leftrightarrow \sigma_i^{-1}$).
- $j$-invariant finiteness of the Descartes elliptic curve.

For each predicate, any existing one-sided proof now generates the
bar-companion bound by composition with $\iota$.
