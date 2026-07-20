# The q-difference kernel's confluent limit is over-determined: R(1,x) = 1 is forced and the bounded-depth OGF form fails at first order

**Date:** 2026-07-20
**Branch:** `claude/jets-alien-calc-q-mobius-yrp563` (PR #4122)
**Bean:** `qou-d8as` (keystone narrowing, milestone `qou-nxl8`)
**Status:** AUDIT — a derived structural narrowing of
[`conj:qdifference-kernel-prolongation-symbol`](../../content/quantum-observable-universe/mass-theory/qdifference-kernel-prolongation-symbol.md).
Nothing wired; the Lean bricks are queued, not landed. Scope classification
per the §Before-declaring-refuted discipline is given explicitly in §4.

## 0. Summary

Working the `q → 1` confluent limit of the conditional q-difference form
([`prop:binding-genfun-qdifference`](../../content/quantum-observable-universe/mass-theory/binding-genfun-qdifference.md))

$$G(qx;q) = R(q,x)\,G(x;q), \qquad R \in \mathbb{Q}(q)[x,x^{-1}] \text{ of bounded depth } d,$$

against the **proved** classical shadow — `B_n(1) = I(n)/n` with `I` the
involution numbers (`prop:sw-classical-jet-exactness` chain;
Gevrey-1/2 sandwich `QOU.Mass.BindingGevreyHalf`) — gives, by pure
coefficient algebra:

1. **Zeroth order is rigid:** `R(1,x) = 1` identically (§2). The kernel is
   necessarily a deformation of the identity, `R = 1 + (q−1)S(q,x)`.
2. **First order is fully pinned by classical data:** the `∂_q B_n` terms
   cancel identically, leaving `n·B_n(1) = Σ_j s_j·B_{n−j}(1)` with
   `s_j = [x^j]S(1,x)` (§3). No q-side freedom survives at this order.
3. **The pinned relation is unsatisfiable at bounded depth** (§4): the
   left side grows like `n·B_n`, the right side like `B_{n−1}`, and
   `n·B_n/B_{n−1} → ∞` (super-geometric growth). Hence the **literal
   bounded-depth OGF form of the kernel hypothesis cannot hold as stated**.
4. **The survivor is the Gevrey-normalized (q-Borel) form** (§5): divide
   the coefficients by a Gevrey-1/2 normalizer before asking for a
   bounded-depth kernel. This relocates the conjectured q-difference
   connection to the **Borel plane — exactly where the alien-calculus
   `Δ_ω` data already lives** (PR #4122's interaction audit), and is
   consistent with the GGM state-integral route.

This is a **narrowing, not a demolition**: the prolongation-symbol
*identification* (the conjecture's content) survives; what fails is one
normalization choice in its stated carrier equation.

## 1. Setup and the two proved inputs

Notation as in the conjecture block: `G(x;q) = Σ_{n≥0} B_n(q) xⁿ` (ordinary
generating function), kernel relation `G(qx;q) = R(q,x)G(x;q)` with
`R = Σ_{j=−d₋}^{d₊} r_j(q) x^j`, coefficient form

$$q^n B_n(q) \;=\; \sum_j r_j(q)\,B_{n-j}(q) \qquad (\ast)$$

Proved inputs (both corpus-carried):

- **(P1) Classical shadow.** `B_n(1) = I(n)/n` — the classical binding
  period `a_D^{(n)} = lw(n−1) = I(n)/n`
  ([`sw-classical-jet-exactness-proof.md`](../../content/quantum-observable-universe/brings-surface/sw-classical-jet-exactness-proof.md),
  Lean `involutionNumber_pos` and the E-chain).
- **(P2) Super-geometric growth.** `I(n)² ≍ n!` up to exponential factors
  (`QOU.Mass.BindingGevreyHalf.gevrey_half_sandwich`, sorry-free), and the
  successive-ratio divergence `I(n)/I(n−1) → ∞`: from
  `r_n := I(n)/I(n−1) = 1 + (n−1)/r_{n−1}` (the involution recurrence) a
  two-line two-sided induction gives `r_n ≍ √n`. Numerically (sanity, exact
  integer recurrence to n = 60): `B_{n−1}/B_n = 0.213, 0.151, 0.124` at
  `n = 20, 40, 60`; `n·B_n/B_{n−1} = 93.9, 265.3, 485.4` — both monotone in
  the asserted directions.

## 2. Zeroth order: R(1,x) = 1 is forced

Evaluate `(∗)` at `q = 1`: `B_n = Σ_j r_j(1) B_{n−j}` for all large `n`,
i.e. `0 = Σ_j c_j B_{n−j}` with `c_0 = r_0(1) − 1`, `c_j = r_j(1)` (j ≠ 0),
finitely many terms. Order the indices by growth: `B_{n+d₋} ≫ … ≫ B_{n−d₊}`
(P2: each successive ratio → ∞). Divide by the fastest-growing term present
and take `n → ∞`: its coefficient must vanish. Induct downward:
**every `c_j = 0`**. Hence `r_0(1) = 1`, `r_j(1) = 0` for `j ≠ 0`:

$$R(1,x) = 1, \qquad R(q,x) = 1 + (q-1)\,S(q,x), \quad S \in \mathbb{Q}(q)[x,x^{-1}].$$

(Uses only positivity + successive-ratio divergence — both at (P2)'s tier.
No archimedean input beyond ordering; a Lean brick would live wall-side (ℝ)
by §7c since it takes limits.)

## 3. First order: the ∂_q terms cancel and classical data pins S(1,x)

Differentiate `(∗)` at `q = 1` (write `B_n' = ∂_q B_n|_{q=1}`,
`s_j = [x^j]S(1,x)`; use §2):

$$n\,B_n(1) + B_n' \;=\; B_n' + \sum_j s_j\,B_{n-j}(1)$$

The **`B_n'` terms cancel identically** — the first-order constraint knows
nothing about the q-deformation of the coefficients:

$$n\,B_n(1) \;=\; \sum_j s_j\,B_{n-j}(1) \qquad (\ast\ast)$$

This is the confluent statement "the fibre q-shift becomes a derivation"
(the block's consequence 2) made exact at the coefficient level: `x∂_x`'s
eigenvalue `n` must be reproduced by the finite Laurent convolution `S(1,·)`.

## 4. The obstruction, and its honest scope classification

`(∗∗)` compares `n·B_n(1)` (left) against a finite combination of
`B_{n−j}(1)`, dominated by `B_{n−1}(1)` (or `B_{n+d₋}(1)` if `S` has
negative depth — the same elimination as §2 first kills all negative-`j`
coefficients). By (P2):

$$\frac{n\,B_n(1)}{B_{n-1}(1)} \;=\; \frac{n\,(n-1)}{n}\cdot\frac{I(n)}{I(n-1)} \;\sim\; n^{3/2} \;\to\; \infty,$$

so no bounded Laurent `S(1,x)` satisfies `(∗∗)`. Conclusion:

> **Scope-(b) structural exclusion (with the invariant named):** the
> hypothesis "`G(x;q) = Σ B_n xⁿ` (OGF, `B_n(1) = I(n)/n`) satisfies
> `G(qx) = R·G(x)` with `R ∈ ℚ(q)[x,x⁻¹]` of bounded depth" is
> **incompatible** with the proved Gevrey-1/2 growth (P2). The excluding
> invariant is growth (P2) + the exact first-order identity `(∗∗)`; both
> steps are displayed above and the argument is elementary.

Per the discipline this exclusion is **narrow by construction**: it rules
out one *carrier normalization* (bounded-depth kernel on the raw OGF), not
the prolongation-symbol identification, not a depth-unbounded `R`, and not
any renormalized carrier (§5). `prop:binding-genfun-qdifference` is
conditional ("Suppose G satisfies…") and its block already flags existence
of `R` as the open part — this audit sharpens *why* existence fails in the
raw normalization. Pending independent verification + the Lean bricks, the
conjecture block should gain an `authorNotes` caveat (queued as follow-up,
not edited here — render-QA gates).

## 5. The survivor: the kernel lives on the (q-)Borel side

The failure mode is precisely Gevrey growth — the same `√(n!)` factor that
`BindingGevreyHalf` proves and that the alien-calculus chain resums. Divide
it out: with a Gevrey-1/2 normalizer `γ_n` (`γ_n = Γ(n/2+1)` or the q-analog
`[n]_q!^{1/2}`-graded variant), the **Borel-normalized** series
`Ĝ(ξ;q) = Σ (B_n/γ_n) ξⁿ` has geometric-growth coefficients, and `(∗∗)`'s
analogue becomes satisfiable (the `n` on the left is absorbed by
`γ_n/γ_{n−1} ~ √n` two steps at a time — matching the **depth-2** shape of
the involution recurrence `I(n) = I(n−1) + (n−1)I(n−2)`).

Consequences:

1. **Sharpened keystone target.** Restate the conjecture's carrier as: the
   *q-Borel transform* of the binding OGF satisfies a bounded-depth
   q-difference equation whose kernel is the prolongation symbol. The
   Borel-plane singularity structure of `Ĝ` is then *the same object* as
   the `Δ_ω` alien data of the interaction audit
   ([`2026-07-19-jets-alien-qmobius-bring-interaction.md`](2026-07-19-jets-alien-qmobius-bring-interaction.md))
   — the two chains meet instead of running in parallel.
2. **Depth prediction.** The classical recurrence's rank (2, with the
   `(n−1)` coefficient) predicts **depth d = 2** for the normalized kernel
   — a concrete, falsifiable pin replacing "bounded depth d".
3. **Quaternionic/hyperkähler route (owner question).** The
   twistorial/hyperkähler construction of SW-type connections (GMN:
   Stokes data = BPS/DT integers on the twistor line) is the natural
   *derivation* route for the normalized kernel's Stokes data, and is the
   same DT-integer structure as the GGM route already carried for G3. The
   corpus has no hyperkähler carrier block yet; #4129's landed
   "quaternionic monodromy" scaffold is the first step — its cross-check
   against this audit's obstruction is tracked in §6.

## 6. Cross-check against the #4129 landing (merged as `68736287`)

PR #4129 ("Formalize local quaternionic monodromy for the keystone
R(q,x)") landed Lean scaffolding around the same conjecture
(`ReebAlienFiltration`, prolonged-periods, kernel-symbol files) while this
audit was in progress. The critical question is whether any landed
statement *encodes the raw bounded-depth OGF form* that §4 excludes — if
so, that statement's hypothesis class is empty and it holds vacuously; if
it is normalization-agnostic, it composes with §5 unchanged. This
cross-check is running as a separate adversarial review; its findings land
as a follow-up commit to this doc rather than being pre-judged here.

## 7. Discipline

- **Corpus-grep:** the four paths were walked for prior statements of the
  confluent obstruction (`grep -ri "confluent" content/ docs/audits/`,
  `R(1,x)`, involution-recurrence-vs-kernel comparisons in
  `docs/coordination/`): the block's own consequence 2 states the
  confluent *limit* but no prior artifact runs it at coefficient level or
  records the obstruction. No prior closure found.
- **Anti-fit:** nothing here is fitted — both inputs are proved corpus
  facts; the derivation is two lines of coefficient algebra shown in full.
- **Formalize-first:** this audit *is* the formalize-first step for any
  future kernel search — it prunes the raw-OGF hypothesis class to zero
  and fixes the normalized target (depth-2, q-Borel side) before anyone
  scans for kernels. Lean bricks queued (bean `qou-d8as`): (i) §2/§4 as a
  wall-side (ℝ) growth lemma; (ii) the `(∗∗)` cancellation as a generic-R
  formal-power-series identity.
