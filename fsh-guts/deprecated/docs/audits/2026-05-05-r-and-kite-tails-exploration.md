> **DEPRECATED on 2026-05-24.** Workplan / status snapshot / investigation result / closure-attempt that has been integrated into main or superseded by a later resolution. Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) for the tranche rationale.

# Notation exploration: `r = q^{1/2}` and kite tails

**Status.** Exploration / brainstorm. Not committed to a notation choice.
**Branch.** `claude/hoefsmit-2x2-fix` (PR #546).

## Part 1 — Implications of `r := q^{1/2}`

### Defining relation and physical interpretation

Set $r := q^{1/2}$, so $r^2 = q$ and $r > 0$ at $q_0$ (canonical
substrate point gives $r_0 \approx 1.0535$). The user-suggested
reading: $r$ is the **information-transfer rate along a purely
linear braid** — one strand, no surface area, no branching.

| Quantity | $q$-form | $r$-form |
|---|---|---|
| Markov parameter | $z = 1/(\sqrt q + 1/\sqrt q)$ | $z = 1/(r + r^{-1})$ |
| Hecke skein | $h = q - q^{-1}$ | $h = r^2 - r^{-2}$ |
| Substrate $\hbar_q$ | $(q-1)/q$ | $1 - r^{-2}$ |
| Substrate $c_q$ | $1/(q-1)$ | $1/((r-1)(r+1))$ |
| Hoefsmit eigenvalues | $\pm q, \mp q^{-1}$ on $V \otimes V$ | $\pm r^2, \mp r^{-2}$ |
| Half-twist eigenvalue | $\pm \sqrt q$ on spin-½ | $\pm r$ |

The clean interpretation: **$r$ is the eigenvalue of one elementary
half-twist on the spin-½ fundamental rep**. Each strand "carries"
information at rate $r$ per half-twist. A full crossing $\sigma_i$
multiplies by $r^2 = q$ (full twist) on the symmetric channel; the
half-twist building block is exactly $r$.

This is also the natural unit for the **R-matrix universal
specialisation**: $R = q^{H \otimes H/2}\,(\ldots)$ involves
$q^{1/2}$ in the Cartan half, so $r$ is the universal Cartan unit.

### What "linear chain, no surface area" means precisely

A braid word on $n$ strands is a **graph with surface area** when
it has crossings between non-adjacent strands (creating bigons,
triangles, etc. in the link diagram). A **purely linear chain**
is a word using **only one generator** — say $\sigma_1^k$ for some
$k$ — which lives in $H_2(q)$ and has trivial closure topology
(unknot, trefoil, etc., depending on $k$).

For such a linear chain:

- the closure has a single 2-bridge component;
- the Markov trace reduces to a polynomial in $r$ via
  $\sigma_1^k = (h\sigma_1 + 1)^{k/2 \text{ish}}$ recursion;
- there is no mixing between irreps beyond the 2 partitions of 2;
- the "rate per step" is exactly $r$.

Examples:
- Unknot ($\sigma_1^0$): $\mathrm{tr}_M(1) = 1$.
- Hopf link ($\sigma_1^2$): $\mathrm{tr}_M = h r^{-1} + r^{-2}$ etc.
- Trefoil ($\sigma_1^3$): closed-form derived in
  [`2026-05-05-categorical-chain-gamma-to-six-term.md`](2026-05-05-categorical-chain-gamma-to-six-term.md),
  $\approx 0.7302$ at $q_0$.

For ANY of these, the result is a polynomial in $r$ with integer
coefficients (no √ residual). $r$ is the right primary variable.

### Notation conflict — "r" already in use for Wenzl level

The Wenzl Schur principal-specialisation formula
$y_\lambda \propto s_\lambda(1, Q, Q^2, \ldots, Q^{r_W - 1})$ uses
**`r_W`** (the principal-spec length). The user-proposed
re-purposing of `r` for $q^{1/2}$ would clash unless we rename:

- `r_W` → `ℓ_W` (Wenzl length), or
- `r_W` → `n_W` (level), or
- keep `r_W` and use `r` for $q^{1/2}$ only — context would resolve
  but reading is harder.

Cleanest approach: **rename `r_W → ℓ`** (since it IS a length —
the count of points in the principal specialisation $1, Q, \ldots,
Q^{\ell-1}$). Then `r := q^{1/2}` is the fundamental rate variable
throughout.

### Substrate-physics interpretation of `r`

If $r$ is a "rate", what does it physically encode?

**Information per Planck tick on a single strand.** Each braid
step is $r$; the substrate processes one $r$-quantum of "spinor
phase" per elementary tick along a single thread. At $q_0$,
$r_0 \approx 1.0535$ — slightly above unity, the "barely faster
than classical" regime. This is a structural interpretation, not
a numerical match: $r$ is the unit of measurement, not a
dimensionless ratio.

**Categorical content.** $r$ is the eigenvalue of the elementary
half-twist on the spin-½ fundamental rep — the smallest non-trivial
quantum step. Without $r$ (i.e. only working with $r^2 = q$) you
can compute the **bracket polynomial** (writhe-blind invariants);
with $r$ you get the **Jones polynomial** (writhe-tracking, frame-
aware). The substrate's information rate $r$ is precisely the unit
that distinguishes oriented-vs-unoriented topology.

**Connections to mass ratios — open.** Lepton mass ratios
($m_\mu/m_e$, $m_\tau/m_e$) and the fine-structure constant
$\alpha_{\text{em}}^{-1}$ are dimensionless and might admit
$r$-polynomial categorical expressions; this requires a derivation
of "muon = electron + $k$ half-twists" (or similar) and is **out
of scope** here. We do **not** claim numerical $r^k$ matches
without a categorical derivation — that would be numerology.

## Part 2 — Yekutieli kite tails

### What I can verify

Amnon Yekutieli's work on derived completions, MC-elements, and
continuous Hochschild cohomology uses tail-structured objects in
several places, but **I cannot confirm the specific term "kite
tail" without access to the literature in this session**. The
candidates I'm aware of from his published work:

- "Nonabelian deformations and Maurer-Cartan equations" (Yekutieli,
  2012) — uses **MC tails** (the formal-power-series tail of the
  MC element after truncation at order $N$) for the descent of
  twisted deformations.
- "Derived categories" (Yekutieli book, 2020) — has **completion
  tails** in adic-derived completions.
- "Smooth formal embeddings" — uses **kite-shaped graphs** for
  cohomological filtration in some operad-theoretic constructions
  (this might be where "kite" enters; I'm less certain).

Without verifying I won't claim a specific Yekutieli result
matches our setting. But the **structure** the user is pointing at
is real and present in QOU:

### Kite-tail structure in our braid algebra

A braid word can be decomposed into:

- **tail**: a maximal linear sub-chain $\sigma_i^{k_i}$ on a single
  generator;
- **kite**: a triangle $\sigma_i \sigma_j \sigma_i$ for $|i - j| = 1$
  (Yang-Baxter-tied, planar);
- **junction**: a place where two tails meet at a kite or a
  Reidemeister-III move.

The **tail** carries pure-$r$ information (linear chain). The
**kite** is the first place where 2D surface area enters — a
triangle of three strands closing back.

For the canonical atomic braid words (proton, neutron, deuteron):

- Proton word (11 crossings): mostly tail-structured. The 3 × $\sigma_0$
  $B_3$-confinement crossings + 3 × $\sigma_1^{-1}$ are pure tails;
  the pair couplings (uu, ud, ud) introduce kite junctions.
- Deuteron word (23 crossings): 11 + 11 tails + 1 inter-nucleon kite
  junction.

This decomposition is consistent with the
$D(u) = 2^{2A+1} \cdot u^{\text{shift}} \cdot (1 + u^2)^{3A-1}$
factorisation in PR #545:

- $u^{\text{shift}}$ comes from the tail count (each elementary
  half-twist contributes $u = r$);
- $(1 + u^2)^{3A-1}$ comes from the cyclotomic/kite structure
  (each pair of strands contributes a $1 + r^2 = 1 + q$
  cyclotomic factor);
- $2^{2A+1}$ is the average-crossing prefactor (kite junctions
  contribute halving).

### Tentative "kite tails" interpretation

If we adopt the dictionary:

- **tail** = pure $r$-power (linear chain)
- **kite** = $(1 + r^2)$ factor (junction)
- **prefactor** = $2^{2A+1}$ (averaging/coboundary)

then the closed-form $D(u)$ is **literally a kite-tail
factorisation**, exactly the kind of structural decomposition
Yekutieli-style derived completion would produce. Whether this is
*the* construction Yekutieli calls "kite tails" needs literature
verification.

### Path to confirming the connection

To verify or refute the Yekutieli connection, one would need:

1. **Direct citation check** — search Yekutieli's papers (2010–2024)
   for the term "kite" or "kite tail". My best guess: it's in
   "Smooth formal embeddings and the residue complex" or one of
   the formal-infinitesimal calculus papers.
2. **Structural comparison** — extract the precise algebra Yekutieli
   uses and see if it matches our braid kite-tail decomposition.
3. **Functorial bridge** — if both are using the same combinatorial
   structure, build the equivalence (probably via the Connes-Kreimer
   Hopf algebra of rooted trees, since both kite and tail are
   tree-like).

This is a 1-3 day research effort. **Not in scope for PR #546**, but
worth queuing as a follow-up.

### Verification result (2026-05-06 follow-up)

The kite-tail conjecture in its naive form is **falsified** by direct
verification. [`computations/kite_tail_verification.py`](../../computations/kite_tail_verification.py)
runs the closed-form symbolic $\mathrm{tr}_M$ for proton, neutron,
and deuteron (with bridge-numeric $y_\lambda$ at $n=6$ for tractability)
and extracts the factorisation:

| Atom | Predicted (PR #545 D(u)) | Observed (canonical tr_M denominator) |
|---|---|---|
| Proton (A=1) | $2^3 \cdot r^{19} \cdot (1+r^2)^2$ | $2^2 \cdot r^{19} \cdot (1+r^2)^1$ |
| Neutron (A=1) | $2^3 \cdot r^{22} \cdot (1+r^2)^2$ | $2^2 \cdot r^{19} \cdot (1+r^2)^1$ |

**What matches:** the tail exponent ($\text{shift} = 18Z + 21N + 1$) is
correct: 19 for proton, 22 for neutron. ✓

**What doesn't match:** the kite power and the $2^k$ prefactor.
Observed (1, $2^2$) vs predicted ($3A-1=2$, $2^{2A+1}=2^3$). At $A=1$
the discrepancy is by exactly a factor of 2 in each.

### Reconciliation (open)

PR #545's $D(u)$ is computing a **different quantity** than the
canonical Wedderburn $\mathrm{tr}_M$. Possibilities:

1. **$D(u)$ is the polynomial after stripping a different
   normalisation**, e.g. multiplying by an extra $z = u/(1+u^2)$
   or $u/(r+r^{-1})$ factor that absorbs one $(1+r^2)$ and one $2$.
2. **$D(u)$ uses a different braid encoding** (with vs without
   gluon dressing — the `proton_cross` vs `nucleon_gen_chains`
   distinction we hit in PR #546 round-1).
3. **$D(u)$ is the cleared-NUMERATOR**, and the $(1+r^2)^{3A-1}$
   exponent is the NUMERATOR-side cyclotomic factor, not the
   denominator-side. (Need to redo the extraction on the numerator
   to test.)

This is open work. The kite-tail **dictionary** (tail = pure $r$-power,
kite = cyclotomic junction, averaging = $2^k$) remains structurally
correct; only the precise exponents in PR #545's $D(u)$ closed form
need reconciliation with the canonical Wedderburn $\mathrm{tr}_M$.

The Yekutieli connection — if it exists — would naturally arise
from the correct refined kite-tail form, not the naive one.

## Recommendation

For **immediate notation** (PR #546 close-out):

1. **Keep `q^{1/2}` lowercase explicit** in audit doc text and use
   `q12` or `t = q^{1/2}` only as a temporary script-local symbol.
2. **Adopt `r` as the canonical fundamental rate** in a SEPARATE
   follow-up branch, after the `r_W → ℓ` rename is done globally.
3. **Cite Yekutieli kite tails as conjectural** in this audit doc;
   open a research issue to verify.

This keeps PR #546 narrowly scoped to the actual closed-form
derivations, and the notation refactor + Yekutieli investigation
become their own work items.

## Summary table — pros/cons of `r`

| Aspect | Pro | Con |
|---|---|---|
| Physical meaning | Rate per half-twist (clear) | Slightly abstract |
| Existing usage | None (after `r_W → ℓ` rename) | `r_W` rename is non-trivial |
| Mathematical convention | Common for "rate" / "rapidity" | Conflicts with radius / generic var |
| Substrate fit | Natural unit for spinor information rate | Mass-ratio expressions in $r^k$ require categorical derivation, not numerical match |
| Yekutieli compat | If kite-tail bridge holds, $r$ is the tail unit | Requires verification |
| Lit precedent | Wenzl Schur uses $Q^r$; PR #545 uses $u$ | Both established |

## Note on rejected alternatives

- **`t`** — clashes with the standard knot-polynomial variable
  ($V_K(t)$) and with time. **Rejected.**
- **`ι` (iota)** — clashes with involution / inclusion / unit-map
  notation in category theory. **Rejected** (per user feedback).
- **`u`** — already used in PR #545's $D(u)$ work for the same
  quantity ($u = q^{1/2}$). Pragmatic choice if cross-PR alignment
  is the priority.
- **`κ`** — Kauffman-bracket variable A satisfies $A^2 = q^{\pm 1/2}$;
  $\kappa$ would be one square root deeper. Visually OK but not
  clearly tied to physical meaning.
- **`r`** — fits the "rate" interpretation cleanly; conflict with
  Wenzl level $r_W$ resolvable via rename to $\ell$. **Strong
  candidate.**

## Open questions

1. Is the apparent $r$-polynomial structure of lepton mass ratios
   a categorical identity, or just dimensional analysis?
2. Does Yekutieli's "kite tail" (if it exists in the literature)
   match our braid tail/kite decomposition?
3. Should the choice be `r` (paper-wide) or `u` (matching PR #545)?
   `r` has cleaner semantics; `u` minimises rename-cost.
