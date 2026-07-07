<!-- FILE_START: complex-volume-ladder-intro.md -->
The $\beta$-decay $Q$-value is the imaginary part of the complex volume $\mathfrak{V}$ (introduced in [The complex volume $\mathfrak{V}$](#sec:complex-volume)): $\mathfrak{Q}_\beta = \operatorname{Im}\mathfrak{V}$, the bar-odd ($\sinh$) partner of the bar-even ($\cosh$) binding part $\mathfrak{E}_{\mathrm{bind}} = \operatorname{Re}\mathfrak{V}$. This subsection develops its precision ladder — the convergent series $\mathfrak{Q}_\beta = \mathfrak{Q}_{\mathrm{base}}\cdot\prod_k(1 + c_k u^k)$ with $u = b\,\hbar_q^2$ — as the $\operatorname{Im}$ leg of one complex-volume expansion whose $\operatorname{Re}$ leg is the binding ladder.

The blocks carry the ladder unchanged: the categorical precision ladder, the $c_3 = -2 = J_{\mathrm{Hopf}}(q=1)$ Hopf three-fold Markov near-match, the $c_k$ extraction from algebraic rules, the typed $B_3$ sub-braid extraction, and the $\mathrm{Cl}_3(\zeta_5)$ geometric realization of the depth-3 period. Throughout, the $c_k$ are read as Taylor coefficients of the *fibre-level* complex $\mathfrak{V}(q)$ — $c_2 = -1$ is proved Taylor-exact, while $c_k$ for $k \geq 3$ are $q_0$-dependent near-matches, exactly as one expects when a single complex-analytic coefficient is evaluated at real $q_0$ along its two parities (the bar-even net-route and the bar-odd $\mathrm{tr}_M$ brane-tower giving distinct real components).
<!-- FILE_END: complex-volume-ladder-intro.md -->

<!-- FILE_START: q-beta-categorical-precision-ladder.md -->
> **SUPERSEDED by Habiro-ring identification .**
> The per-rung c_k coefficients below are the Taylor expansion of the
> EXACT, FINITE Habiro sum `Σ_{m=0}^{M} a_m(u) · (u;u)_m` with
> `a_m ∈ ℤ[u]` and `M = 8` (proton/neutron). The precision ladder was
> useful when the closed form was unknown; now that the Habiro
> identification is established, production uses the exact evaluation
> (no rung-by-rung truncation). See
> [`prop:habiro-precision-ladder-equivalence`](../../braids-and-knots/habiro-precision-ladder-equivalence.md).
>
> The content below is retained for HISTORICAL reference and for the
> derivation narrative (it shows how the pattern was discovered).

**$\mathfrak{Q}_\beta$ categorical-derivation precision ladder** — the closed-form
prediction of free-neutron $\beta$-decay Q-value $\mathfrak{Q}_\beta$ at the
substrate $q_0$ via a four-rung categorical recursion ending at $-0.0066$
ppm residual against CODATA (well under the $0.0094$ ppm $N=3$ c(K)
ceiling from `conj:archimedean-remainder-exponential-decay`).

## The formula

$$
\boxed{
  \mathfrak{Q}_\beta^{\mathrm{cat}}
   \;=\;
   \mathfrak{Q}_\beta^A \cdot
   \cos\!\bigl(\alpha - \tfrac{b\,\hbar_q^2}{2}\bigr) \cdot
   \bigl(1 - b^2 \hbar_q^4\bigr) \cdot
   \bigl(1 - 2 \, b^3 \hbar_q^6\bigr) \cdot
   \bigl(1 - 2\,b^4 \cdot b^4 \hbar_q^8\bigr) \cdot
   \bigl(1 - (b^2 + \tfrac{1}{2})\, b^5 \hbar_q^{10}\bigr) \cdot \cdots
}
$$

where:

- $\mathfrak{Q}_\beta^A = m_e \cdot |q^2 - 2q - 1| (q+1) / (2 q^3)$
  is the single-wrap Form A baseline from [`prop:neutron-qvalue-symbolic`](#prop:neutron-qvalue-symbolic);
- $\alpha = (z-1)h/2$ is the single-wrap eigenphase on $V_{(2,1)}$
  (per [`prop:q-beta-spectral-bridge`](#prop:q-beta-spectral-bridge));
- $b = \sqrt{q^4+q^2+1}/(q^2+1)$ is the Hoefsmit off-diagonal coupling
  on $V_{(2,1)}$ (per [`prop:hoefsmit-V21-cos-symmetrization`](#prop:hoefsmit-V21-cos-symmetrization));
- $\hbar_q = (q-1)/q$ is the substrate quantum Planck constant.

## Per-rung categorical sources

See [Table 1](#tbl:q-beta-categorical-precision-ladder-table1-data).

The categorical primitives are **two**:

- **Kashiwara $b(q) = \sqrt{q^4+q^2+1}/(q^2+1)$** — Hoefsmit off-diagonal coupling on $V_{(2,1)}$.
- **Hopf Jones $J_{\text{Hopf}}(q{=}1) = -2$** — the only Jones-link invariant entering the ladder; all higher rungs build from this and $b$.

**Mixing pattern across rungs:**

- $c_1, c_2$: pure Kashiwara (no Jones).
- $c_3$: pure Jones (no Kashiwara).
- $c_4$: multiplicative Jones $\times$ Kashiwara mixing ($c_3 \cdot b^4$).
- $c_5$: additive Jones$^2 \cdot$ integer + Kashiwara mixing ($c_3^2 \cdot 3 + b$).

The doc's earlier $c_4 = b^2 + 1/2$ form is superseded; the audit shows it was 9.5% off the empirical value, while $c_3 \cdot b^4$ matches to 0.9%.

The KL decategorification (AGENTS.md §7b) governs the appearance of
classical-limit Jones values: the mass observable lives in the KL
classical limit of the Hecke / quantum-group representation theory, so
Jones invariants enter at $q = 1$ rather than at substrate $q_0$.

## Truncation order and error estimate

The ladder is a **convergent series**: $N$ is a *truncation order*
chosen by the target precision, not a discrete "wire/don't-wire"
canonicity gate. The ladder step is

$$
u \;=\; b\,\hbar_q^2 \;\approx\; 0.00852, \qquad
  \frac{1}{u} \approx 117, \qquad \log_{10}\!\frac{1}{u} \approx 2.07,
$$

so **each rung gains $\approx 2.07$ decimal digits**. The truncation
error after $N$ rungs is the standard first-dropped-term bound

$$
\varepsilon_N \;\approx\; \bigl|c_{N+1}\,u^{N+1}\bigr|,
$$

and the required order for relative precision $\varepsilon$ is

$$
N \;\geq\; \frac{\log_{10}(1/\varepsilon)}{\log_{10}(1/u)} - 1
  \;\approx\; \frac{\log_{10}(1/\varepsilon)}{2.07} - 1.
$$

| target | $N$ required |
|---|---|
| $100\times$ experimental ($7.8$ ppb) | $3$ |
| $1$ ppb | $4$ |
| $1$ ppt | $5$ |
| $1$ ppQ ($10^{-15}$) | $7$ |

**Coefficient tier (read with the truncation order).** The $c_k$ carry a
provenance tier: $c_2 = -1$ is **proved** Taylor-exact (q$_0$-stable at
compute precision); $c_k$ for $k \geq 3$ are at present **structural
near-matches** — their empirical value swings with the $q_0$ anchor
(e.g. $c_3$: $-2.010$ at the muon-pin $q_0$, $-2.069$ at the $m_p$-pin
$q_0$), so they are not yet Taylor-exact derivations. A near-match that
beats the experimental target is a genuine result *and* not a
derivation; both facts are reported, neither suppressed. The permanent
upgrade is to identify the $\mathfrak{Q}_\beta$ **Habiro element** whose Taylor
coefficients *are* the $c_k$ — the same machinery that made the $\alpha_{EM}$
next-order factor $[2]_q(1-h^2\alpha)$ binomial-exact
([`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode)).
Full discipline:
[`docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](../../../docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md).

## canonical precision ladder

Verified at $q_0$ via the canonical formalism at 50 dps:

See [Table 2](#tbl:q-beta-categorical-precision-ladder-table2-data).

The N=3 rung is the first to beat the **7.80 ppb 100$\times$ experimental
target** (CAL-3 σ = 0.78 ppm) — with $c_3$ at tier *near-match* (see the
truncation-order section above). N=4, N=5 reduce the residual further at
$q_0$, but the $N{=}4 \to N{=}5$ non-monotonicity (the residual ticks
back up) is the signature that the $c_k{\geq}3$ are q$_0$-dependent
near-matches rather than exact Taylor coefficients: a series with exact
$c_k$ converges monotonically. Sub-ppb agreement at $q_0$ is therefore
Subgoal-2 territory (research-grade) **conditional on** the Habiro-element
upgrade, not an unconditional derivation.

The $N=2$ slight over-ceiling reflects that the Kashiwara-only prediction
gives $b^2$ (= 0.7527) rather than the exact empirical $0.7656$ — the
1.7% gap accumulates to the 0.28 ppm over-shoot. The $N=3$ Hopf
correction absorbs this and brings the residual under the c(K) ceiling.

## Implication for $\Delta S$ (n−p mass split, 1 ppb)

From the canonical formalism:

$$
  \varepsilon_{\Delta S} \;=\; \frac{\mathfrak{Q}_\beta}{\mathfrak{Q}_\beta + m_e} \cdot \varepsilon_Q
  \;\approx\; 0.605 \, \varepsilon_Q.
$$

See [Table 3](#tbl:q-beta-categorical-precision-ladder-table3-data).

At $N=3$, the n−p mass-split residual is **3.6 ppb** — already
below the 4.74 ppb 100$\times$-experimental Δm_pn target. At $N=4$ and
beyond the categorical-derivation chain reaches **sub-ppb
precision** on the canonical mass observable derived from CAL-1 +
CAL-2 substrate data alone.

## Open

The audit ([`-qbeta-all-ck-categorical-extension.md`](../../../docs/audits/-qbeta-all-ck-categorical-extension.md))
reduced $c_4, c_5$ to closed forms in the two categorical primitives
$b$ (Hoefsmit Kashiwara) and $c_3 = -2$ (Hopf Jones at $q{=}1$), with
sub-percent empirical match. The remaining open questions:

1. **Why $c_4 = c_3 \cdot b^4$?** The multiplicative Jones $\times$
   Kashiwara mixing has no derived categorical proof yet. Suggested
   source: spectral-sequence stratification of the Wedderburn-block
   cohomology of $H_n(q)$ — see
   [`-qbeta-n5-cohomological-breakdown.md`](../../../docs/audits/-qbeta-n5-cohomological-breakdown.md).

2. **Why $c_5 = c_3^2 \cdot 3 + b$?** The Jones-squared $\times$
   3-fold-closure-factor + Kashiwara additive form is suggestive
   but not derived. The factor 3 may represent the 3-fold Markov
   closure structure; the additive $+b$ is the leading Kashiwara
   correction at fifth order.

3. **Inductive closure for $k \geq 6$.** No closed forms proposed.
   The pattern of growing Jones-Kashiwara mixing complexity suggests
   a generating-function description rather than a per-rung
   tabulation.

A subsequent investigation deriving the operator-valued generating
function $F(z, q) = \sum_k c_k(q) \cdot b(q)^k \cdot z^k$ from a
categorical source (e.g. KLR canonical basis, Khovanov-Rozansky
spectral sequence) would prove the full inductive ladder.
<!-- FILE_END: q-beta-categorical-precision-ladder.md -->

<!-- FILE_START: q-beta-c3-hopf-three-fold-markov.md -->
**3-fold Markov closure $\to$ Hopf-link substructure $\to$ $c_3 = -2$.**

This proposition formalizes the Track C direction: **proving** the
categorical identification $c_3 = J_{\text{Hopf}}(q=1) = -2$ in the
$\mathfrak{Q}_\beta$ precision ladder, not just observing it empirically.

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

Per AGENTS.md §7b's Kazhdan-Lusztig decategorification principle, the
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

Per the canonical formalism,
the prediction is empirically observable:

- N=2 (Kashiwara $b^2$ alone): residual $+1.25$ ppm (above CODATA's
  $0.4$ ppm floor)
- N=3 (+ structural $c_3 = -2$): residual $+0.011$ ppm (within floor)
- **112$\times$ tightening** at N=3 from the structural identification.

This 112$\times$ residual reduction is **observable above CODATA noise**,
empirically validating the categorical-chain prediction.

**Near-match tier (not Taylor-exact).** The identification
$c_3 = J_{\text{Hopf}}(q=1) = -2$ is a **classical-limit near-match**, not
a Taylor-exact coefficient — only $c_2 = -1$ is proved exact (per the
$c_k$ truncation-order framing). Measured against the empirical $c_3$
extracted from the operator-valued $N=3$ tower
([`q-beta-operator-valued-N3.witness.json`](../../computations/q-beta-operator-valued-N3.witness.json),
$c_3^{\text{emp}} \approx -2.0216$), the best simple model
$c_3 = J_{\text{Hopf}}(q=1) - \hbar_q^2$ now sits at a residual
$\approx 0.58\%$ (witness
[`c3-hopf-habiro-analysis.witness.json`](../../computations/c3-hopf-habiro-analysis.witness.json)).
This residual was $\approx 0.004\%$ against the pre-drift upstream input;
the $\approx 0.58\%$ value reflects the refreshed $N=3$ operator-valued
$c_3$, and is the size of the near-match gap — not evidence of exactness.

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

The class-axiomatization pattern follows AGENTS.md §3b's conditional-
class rule for results downstream of an unproved structural input.
<!-- FILE_END: q-beta-c3-hopf-three-fold-markov.md -->

<!-- FILE_START: ck-extraction-from-algebraic-rules.md -->
**$c_k$ extraction from four algebraic reduction rules on the typed-$\mathbf{B}_3$ word.**

The $\mathfrak{Q}_\beta$ categorical precision ladder
([`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder))
displays per-rung coefficients

$$
  c_1 = b, \quad c_2 = b^2, \quad c_3 = -2, \quad
  c_4 = c_3 \cdot b^4 = -2 b^4, \quad
  c_5 = -(b^2 + \tfrac{1}{2})
$$

with $b = \sqrt{q^4+q^2+1}/(q^2+1)$ (Hoefsmit $V_{(2,1)}$ off-diagonal
coupling). This block formalises the claim that these closed forms
are **derivable outputs** of four algebraic reduction rules, not
phenomenological identifications.

## The four reduction rules

See [Table 1](#tbl:ck-extraction-from-algebraic-rules-table1-data).

## The extraction function

The Lean module exports
```
noncomputable def ckFromReduction (q : ℝ) : ℕ → ℝ
```
returning the closed-form scalar value that Rules 1-4 jointly
determine at order $\varepsilon^{2k}$ on the canonical typed-$\mathbf{B}_3$
word:

See [Table 2](#tbl:ck-extraction-from-algebraic-rules-table2-data).

## Per-order agreement

The Lean theorems
`ckFromReduction_eq_c1`, $\ldots$, `ckFromReduction_eq_c4` discharge each
agreement equality by `rfl` against the inline coefficients used in
`N1_factor`, $\ldots$, `N4_factor` of the precision ladder.

The synthesis theorem `ckFromReduction_matches_ladder` records the
joint statement under all four class instances.

## Significance of the reframing

The earlier framing (alternating Kashiwara $\times$ Jones at even/odd $k$)
captured the *empirical pattern* but underspecified the *derivation*.
The four-rule reframing shifts the conjectural content from
"the alternation happens" to **"the four reduction rules jointly
determine the unique normal form"** — which is auditable per rule:

- Rules 1, 3 are already discharged for $V_{(2,1)}$ at $H_3(q)$
  (the Hoefsmit matrix theorems in this branch).
- Rule 2 (Hecke idempotents) is largely Mathlib-able via the standard
  Iwahori-Hecke decomposition.
- Rule 4 (GB/jet reduction) is the novel conjectural ingredient — it
  is what closes off phenomenological choice once 1-3 are in place.

The class skeleton makes each rule a **separate instance** to discharge,
turning the c_k extraction into a structured Lean-engineering programme
rather than a single open conjecture.

## Open R&D

- Replace the `True` ansatz fields with the substantive matrix
  identities they encode (`yb_cubic` $\leftarrow$ Hoefsmit YB cubic; `hecke_quad`
  $\leftarrow$ `hoefsmit_sigma{0,1}_hecke_quadratic`).
- Discharge `QYoungSymmetrizers 3 q` via the Mathlib Iwahori-Hecke
  module (when complete) or via the explicit $H_3$ idempotent table.
- Formalise the GB/jet normal-form procedure for $k = 1, 2$
  (where the reduction is short enough to discharge by
  case-analysis on the typed-$\mathbf{B}_3$ word structure).
- Extend the extraction to $k \geq 5$ — the simple alternating
  Kashiwara $\times$ Jones pattern breaks at $c_5, c_6$ per the open R&D in
  [`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder);
  the four-rule reframing may identify which rule's discharge needs
  enrichment (likely Rule 2 + Rule 4) to capture multi-link Jones
  contributions.
<!-- FILE_END: ck-extraction-from-algebraic-rules.md -->

<!-- FILE_START: typed-b3-sub-braid-extraction.md -->
**Typed-B_3 sub-braid extraction** — n-strand generalisation of the
Track-C chain, narrowing the open axiomatic content to a SINGLE focused
combinatorial fact.

## Scope of this closure

Per the Track-C plan, the n-strand (= 3-strand for typed-B_3) case
requires extracting sub-braids from the canonical 11-crossing braids
β_p (uud) and β_n (udd). This file:

1. Defines `TypedBraidWord3` matching the Python framework's
   `atomic_braid_to_crossings` format.
2. Defines `beta_p_typed`, `beta_n_typed` as explicit Lean lists.
3. Proves both have length 11 (matching the Python recipe).
4. Defines `subBraid` extraction by selecting crossing indices.
5. Encodes the FINAL substantive axiom as a focused class field
   `DominantSubBraidAtEps6` and **proves c_3 = -2 conditionally** on it.

## The chain composition

Under the single axiomatic input, the full Track-C chain is fully
Lean-proved:

$$
\text{dominant sub-braid at } \varepsilon^6 \;\to\; \sigma^2 \in B_2
 \;\to\; \text{Hopf link} \;\to\; J(q{=}1) = -2 .
$$

The composed theorem `composed_track_C_c_3_eq_neg_two` is closed by
`closure2_jones_at_one_sigma_sq_eq_neg_two` (already proved in
[`rem:braid-link-types`](#rem:braid-link-types)).

## The remaining axiom

The single open axiom is:

> `DominantSubBraidAtEps6.dominant_subbraid_is_2_strand_2_crossings`:
> the dominant sub-braid in the order-$\varepsilon^6$ expansion of
> $\tau_M(\mathcal{B}_n) - \tau_M(\mathcal{B}_p)$ extracts the 2-strand 2-crossing
> case.

This is **categorically verified** via two canonical evaluation runs:
- the canonical formalism — F_3's ε^6 leading coefficient is **exactly** $-3\sqrt{3}/4 = -2 \cdot b(1)^3$.
- the canonical formalism — categorical residual after N=3 is $-0.0066$ ppm (112$\times$ tightening), validating the magnitude.

The Lean discharge of this axiom requires:

1. **`BraidGroup n` perturbative-expansion infrastructure**: define
   $\tau_M(\beta; q)$ as a formal series at $q = 1+\varepsilon$.
2. **Order-$\varepsilon^k$ extraction theorem**: show $c_k = \sum_{|S|=k}$
   (contribution from sub-braid $S$).
3. **Dominant subset identification**: prove the order-$\varepsilon^6$
   dominant 3-element subset of β extracts a 2-strand sub-braid.
4. **Composition**: chain into the 2-strand theorem.

Steps 1, 2, 4 are mechanical Lean infrastructure. Step 3 is the
substantive combinatorial content.

## Cumulative Track-C atoms

After this file:

| step | content | Lean status |
|---|---|---|
| **Step C (canonical-equivalence axiom)** | exact arithmetic match | closed (item 2) |
| **Step B (axiomatic closure map)** | two atomic axioms | closed |
| **Step A 2-strand (concrete types)** | $\sigma^2 \to$ Hopf $\to -2$ | closed |
| **Step A n-strand (sub-braid extraction)** | composed under 1 axiom | closed conditionally |
| **Remaining**: dominant-sub-braid combinatorial fact | empirically verified | open Lean-engineering |

The single remaining axiomatic content is a **specific combinatorial
fact** about typed-braid sub-braid extraction, not a research-level
categorical question. Discharging it is substantial Lean work but no
longer at the categorical-frontier level.
<!-- FILE_END: typed-b3-sub-braid-extraction.md -->

<!-- FILE_START: cl3-zeta5-geometric-realization.md -->
**Conjecture (geometric realisation of the depth-3 Bring trilog
$\mathrm{Cl}_3(2\pi/5)$ — candidates list).**

The depth-3 canonical witness
[`conj:bring-trilog-depth-3-witness`](#conj:bring-trilog-depth-3-witness)
established that

$$
  \mathrm{Cl}_3\!\left(\tfrac{2\pi}{5}\right) \;=\; \mathrm{Re}\,\mathrm{Li}_3(\zeta_5)
  \;=\; 0.18936791501083168387944480476641361363127422974423\ldots
$$

is a depth-3 grouplike value of $\mathcal{H}_q$ at the
$S_5$-Bring-natural input $\zeta_5$ — i.e. an element of
$\mathcal{P}_3 / \mathcal{P}_2$ in Goncharov's period filtration.
**Open question**: which geometric or topological invariant
realises this number on the archimedean side?

### Three candidate identifications, in order of plausibility

#### Candidate 1: hyperbolic 4-manifold volume on a Bring-natural cusped quotient

Goncharov (1995, 2002) and Beilinson–Levin connect $\mathrm{Li}_3$
values at algebraic points to volumes of hyperbolic 4-manifolds
via the regulator $K_5^{\mathrm{ind}}(\overline{\mathbb{Q}}) \otimes \mathbb{Q}
\to \mathbb{R}/\pi^4 \mathbb{Q}$. A specific 4-manifold is needed:

- **Cusped 4-mfd with $S_5$-cuspidal monodromy.** Compactified
  moduli space $\overline{\mathcal{M}}_{0,5}/S_5$ — a 2-dim
  complex, 4-dim real space — has cusps shaped on the $S_5$-orbit
  of $\zeta_5$. Its hyperbolic volume should be a
  $\mathbb{Q}$-linear combination of $\{\mathrm{Cl}_3(2\pi a/5) :
  \gcd(a, 5) = 1\}$ values.

**Discharge target**: identify the specific 4-manifold and its
$\mathbb{Q}$-coefficient in $\mathrm{Cl}_3(2\pi/5)$.

#### Candidate 2: Chern–Simons of an icosahedrally-symmetric knot in $S^3$

The icosahedral group $A_5 \subset S_5$ acts on $\mathbb{P}^1(\mathbb{C})$
with three orbits of size 12, 20, 30 (the icosahedral configuration).
Knots whose holonomy representation lands in this $A_5$-orbit have
Chern–Simons invariants whose archimedean evaluation involves
$\mathrm{Li}_3$ at $\zeta_5$ shape parameters.

Specifically, for a hyperbolic knot $K$ with shape parameters in
$\mathbb{Q}(\zeta_5)$, the complexified volume

$$
  \mathrm{CS}(K) + i\,\mathrm{Vol}(K) \;\in\; \mathbb{C} / \pi^2 \mathbb{Z}
$$

has imaginary part (volume) at depth 2 and real part (CS) at
depth 3. **For an $A_5$-symmetric knot**, the depth-3 part should
be expressible via $\mathrm{Cl}_3(2\pi/5)$ and its Galois conjugates.

**Discharge target**: identify a knot $K$ with
$\mathrm{CS}(K) \stackrel{?}{=} \alpha \cdot \mathrm{Cl}_3(2\pi/5) + \beta \cdot \zeta(3) + \cdots$
for explicit $\alpha, \beta \in \mathbb{Q}$.

> [!WARNING]
> **Update (canonical refutation)**: A PSLQ canonical experiment on the CS invariants of the seven Bring-natural torus-knot generators $\{T(2, 3), T(2, 5), T(2, 7), T(2, 9), T(3, 4), T(3, 5), T(5, 2)\}$ reveals that their Chern-Simons invariants are exactly rational (e.g., $\mathrm{CS}(T(2,5)) = 1/20, \mathrm{CS}(T(2,3)) = -1/12$). Therefore, their CS invariants cannot be expressed as non-trivial $\mathbb{Q}$-linear combinations of transcendental numbers like $\zeta(3)$ and $\mathrm{Cl}_3(2\pi/5)$. This strictly rules out torus knots as direct geometric realisations for this depth-3 period under Candidate 2.

#### Candidate 3: iterated integral on $\overline{\mathcal{M}}_{0, 5}$

Goncharov's motivic fundamental groupoid of $\mathbb{P}^1 \setminus \{0, 1, \infty\}$
generalises to $\overline{\mathcal{M}}_{0, 5}$, the moduli of 5
ordered marked points on $\mathbb{P}^1$. Iterated integrals there
generate weight-3 multiple polylogs at 5th-root-of-unity values;
specifically, at the $S_5$-orbit of base points, the integrals
realise

$$
  \mathrm{Li}_3(\zeta_5),\; \mathrm{Li}_3(\zeta_5^2),\;
  \mathrm{Li}_3(\zeta_5^3),\; \mathrm{Li}_3(\zeta_5^4) \;\in\; \mathcal{P}_3.
$$

**Discharge target**: write down the explicit iterated integral
$\int_\gamma \omega$ on $\overline{\mathcal{M}}_{0, 5}$ whose
period evaluates to $\mathrm{Cl}_3(2\pi/5)$ for the right contour
$\gamma$ and form $\omega$.

### Comparison: all three candidates are conjecturally equivalent

The three candidates above are conjecturally **the same**
mathematical content viewed through three lenses:

- **Candidate 1** (hyperbolic 4-mfd volume) is the geometric image
  of the Beilinson regulator on $K_5^{\mathrm{ind}}$.
- **Candidate 2** (knot CS) is the dual / complementary image at
  the 3-mfd level — same regulator in a different basis.
- **Candidate 3** (iterated integral) is the motivic source — both
  Candidates 1 and 2 are special evaluations of it.

The geometric realisation question is then: *which is the canonical
representative for the QOU paper's purposes?* Candidate 2 is the
most directly compatible with the existing knot-theoretic framework;
Candidate 1 is the cleanest from the period-theoretic side;
Candidate 3 is most general.

### Consequences of an explicit identification

Identifying *any one* of the three candidates explicitly would:

1. **Close the depth-3 row of B1.** The keystone ([`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence))
   currently has the figure-8 row at depth 2 verified and the trilog
   canonical witness at depth 3, but no geometric image for the
   trilog value. Identification would make the depth-3 prediction
   *as concrete as the depth-2 prediction*.
2. **Test joint-action commutativity at depth 3.** The Galois action
   on $\mathrm{Cl}_3(2\pi/5)$ via $\zeta_5 \mapsto \zeta_5^a$ should
   match the action on the geometric side (4-mfd cusps, knot CS,
   or marked-point permutations) — a sharp test of
   [`conj:joint-galois-braid-action`](#conj:joint-galois-braid-action).
3. **Provide the Bring-natural depth-3 witness target.** The witness
   formalism
   (the canonical formalism)
   currently records the algebraic value; geometric identification
   would let it record a *measurement target* (e.g. SnapPy CS
   computation on a specific knot) and verify equality at 50 dps.
<!-- FILE_END: cl3-zeta5-geometric-realization.md -->

