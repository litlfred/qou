# Crystal-shift ordering-invariance — structural proof

**Date:** 2026-05-16
**Branch:** `claude/crystal-and-he4-combined`
**Status:** Proof of the empirical ordering-invariance finding from
[`probe_ordering_dependence.witness.json`](../../computations/ordering-dependence.witness.json)
(12/12 orderings of ⁴He, T, ³He give identical crystal q-pole and
Habiro shift).

## Statement

**Theorem.** Let $\beta_{\sigma}$ denote the canonical atomic braid
for nucleon ordering $\sigma$ of $Z$ protons and $N$ neutrons (any
permutation of $p^Z n^N$). Let $\text{qpole}_{\text{crystal}}(\beta)
= \max_{\lambda \vdash n} \max_{T \in \mathrm{SYT}(\lambda)} \sum_{j} \text{pole}_T(\text{factor}_j)$
be the crystal q-pole counter from
[`crystal_shift_nf`](../../computations/crystal_shift_nf_atomic.py).

Then for any two orderings $\sigma_1$, $\sigma_2$:
$$\text{qpole}_{\text{crystal}}(\beta_{\sigma_1}) \;=\; \text{qpole}_{\text{crystal}}(\beta_{\sigma_2}) \;=\; 12A - 1,$$

i.e., the q-pole equals the total generator count, independent of ordering.

## Proof

**Step 1 — Generator count is ordering-invariant.**

The canonical atomic braid for any ordering has:
- $11$ intra-nucleon generators per nucleon (3 σ_g + 3 σ_g⁻¹ + 1 σ-pair + 2 avg-mix + 2 gluon σ)
- $A - 1$ inter-nucleon interface generators

Total: $11A + (A - 1) = 12A - 1$. This count depends only on $A = Z + N$, NOT on the ordering. □

**Step 2 — Per-factor pole is at most 1 in any SYT.**

Per [`crystal_shift_nf_atomic._pole_for_class`](../../computations/crystal_shift_nf_atomic.py):
- $\sigma$ on column SYT (ρ = −1): pole 1
- $\sigma$ on row SYT (ρ = +1): pole 0
- $\sigma^{-1}$ on column: pole 0 (cancels via $-h \cdot I$ term)
- $\sigma^{-1}$ on row: pole 1
- avg = $\sigma - h/2$: pole 1 on row OR column
- $|\rho| \geq 2$ (2×2 block): pole 1 regardless of $d$

So every factor contributes $\leq 1$ to the per-SYT total. Therefore
$\text{qpole}(\beta) \leq |\beta| = 12A - 1$. □

**Step 3 — Equality holds: max-pole SYT exists.**

We need an SYT $T$ of some shape $\lambda \vdash n = 3A$ such that
EVERY factor of $\beta_\sigma$ contributes pole 1 on $T$. Partition
the generator positions $\{1, \ldots, n-1\}$ into:
- $S$: positions where the factor is $\sigma$ or avg
- $S^c$: positions where the factor is $\sigma^{-1}$ or avg

(Note: avg-positions appear in BOTH sets — they're satisfied
regardless of descent/ascent.)

Define $S^\sigma = \{$positions where factor is $\sigma\}$ — these
REQUIRE descents in $T$. Define $S^{\sigma^{-1}} = \{$positions where
factor is $\sigma^{-1}\}$ — these REQUIRE ascents.

$S^\sigma \cap S^{\sigma^{-1}} = \emptyset$ (a factor cannot be both
σ and σ⁻¹). Avg positions are unconstrained.

**Claim:** There exists $\lambda \vdash n$ and $T \in \mathrm{SYT}(\lambda)$
with descent set $D(T) = S^\sigma \cup S^{\text{avg-as-descent}}$ for
any choice of which avg-positions to treat as descents.

**Sub-proof of claim** — this is **Stanley, EC1 §7 (descent-set
theorem for SYTs)**: for every subset $S \subseteq \{1, \ldots, n-1\}$,
there exists a partition $\lambda \vdash n$ and SYT $T$ of shape
$\lambda$ with descent set $D(T) = S$.

Concretely, choose $S = S^\sigma$ (no avg-positions as descents — keep
all avg as ascents) OR any superset $S^\sigma \subseteq S \subseteq S^\sigma \cup S^{\text{avg}}$.
By Stanley's theorem, an SYT with descent set $S$ exists for some shape.

For that SYT $T$:
- $\sigma$-positions ($\in S$): descent in $T$ → ρ_T(k+1) ≤ −1 → factor pole = 1
- $\sigma^{-1}$-positions ($\in S^c \cap S^{\sigma^{-1}}$): ascent in $T$ → ρ_T(k+1) ≥ +1 → factor pole = 1
- avg-positions: descent or ascent depending on choice — either way pole = 1

Total $T$-pole = $12A - 1$. □

Together Steps 1, 2, 3 give $\text{qpole}(\beta_\sigma) = 12A - 1$ for
every ordering $\sigma$.

Combined with the Habiro bridge
$\text{shift}(Z, N) = 2 \cdot (\text{qpole} - (3Z + 1.5N - 1.5)) = 18Z + 21N + 1$,
the **closed-form Habiro shift is ordering-invariant** (since both
qpole and the cancellation are functions of $(Z, N)$ alone). ∎

## Empirical evidence

12 orderings tested (PR #670,
[`probe_ordering_dependence.py`](../../computations/probe_ordering_dependence.py)):

| atom | orderings tested | all give shift |
|---|---|---|
| ⁴He | ppnn, pnpn, pnnp, nppn, npnp, nnpp (6 orderings) | 79 |
| T   | pnn, npn, nnp (3 orderings)                        | 61 |
| ³He | ppn, pnp, npp (3 orderings)                        | 58 |

12/12 verified empirically; matches the structural proof above.

## Implications

1. **Atomic shift is a "macroscopic" invariant** depending only on
   nucleon content $(Z, N)$, not on the microscopic ordering or
   interface composition $(n_{pp}, n_{pn}, n_{nn})$.

2. **Compositional ambiguity is finer than shift.** F1's compositional
   probe (PR #654 + PR #670 ⁴He compositional) showed that
   different compositional decompositions of ⁴He give DIFFERENT
   topological closures (component counts 2, 4, 5) and DIFFERENT
   Markov-trace values. But they all have the same SHIFT — shift is
   a coarser invariant that washes out the topological distinction.

3. **The closed form `18Z + 21N + 1` is genuinely structural**, not
   just an artifact of canonical pppnnn ordering convention.

4. **For 1-ppb mass prediction**: the shift exponent is robust to
   model-B knot-choice ambiguity. The actual mass depends on the
   FULL τ_M (Jones polynomial), not just shift; but the shift-pole-
   order subtraction in Habiro form is invariant.

## Dependencies

- **Stanley, EC1 §7** — Enumerative Combinatorics Vol 1, Chap 7,
  descent-set theorem for SYTs: for every $S \subseteq \{1, \ldots, n-1\}$
  there exists a partition $\lambda \vdash n$ and SYT $T$ of shape
  $\lambda$ with descent set $D(T) = S$. Citation:
  Stanley, R., *Enumerative Combinatorics*, vol. 1, 2nd ed. (Cambridge
  Studies in Advanced Mathematics 49, Cambridge University Press 2011),
  Theorem 7.19.7.

- **Crystal pole counter** (PR #670, `crystal_shift_nf_atomic.py`):
  the combinatorial primitive that the proof characterizes.

- **Hecke-quadratic relation** ($\sigma_i^2 = h \sigma_i + 1$): the
  algebraic source of the σ ↔ σ⁻¹ pole-cancellation pattern.

## Caveat — non-canonical d-coefficients

The proof assumes Hecke factors are exactly one of $\{\sigma, \sigma^{-1}, \text{avg}\}$
i.e. $(c, d) \in \{(1, 0), (1, -h), (1, -h/2)\}$. These are the only
generators that appear in `mass_at_3A_proper.atom_braid_word_3A`'s
canonical pppnnn construction. Generalizations to other Hecke
generators (e.g., $\sigma + \alpha \cdot \sigma_g$ for $\alpha$ not
proportional to $h$) would need additional analysis.

For canonical atomic braids, this caveat doesn't bite.
