---
# msc1
title: 'mis-aimed citations, a phantom attribution, and a weight-family collision in the Phi_q pair'
status: todo
type: task
priority: normal
created_at: 2026-08-10T14:05:00Z
updated_at: 2026-08-15T23:30:00Z
---
Found by the adversarial reader on PR #4921 while adjudicating `prn1` tranche-1
edges. These are **prose defects**, not `uses[]` defects — filed rather than
fixed, because each changes what a block claims.

Verified independently where marked; taken from the reader's report otherwise
and labelled as such.

## 1. Two citations aimed at the proposition when the content is in the proof

**Verified.** `prf:quantum-dilogarithm-stratified` Step 1 cites

> the depth strata are mutually orthogonal under this pairing
> ([Frobenius duality of strata](#prop:spectral-sequence-collapse)
> "§Frobenius duality of strata")

The string *"Frobenius duality of strata"* appears **zero** times in
`spectral-sequence-collapse.md` and at **line 32** of
`spectral-sequence-collapse-proof.md`. The proposition is one sentence
($\mathrm{HH}^k = 0$, $E_\infty^{0,*} = Z(A)$) and does not contain the
orthogonality the proof consumes.

The reader reports the same mis-aim in `prf:phi-q-categorical-truncation`
Step 2, which cites *"[Plancherel-weighted centre projection]
(#prop:spectral-sequence-collapse)"* — content that lives in the same proof
block, under a heading that reads *"q-deformed Wedderburn-weighted"*, not
"Plancherel-weighted". Those are **different weight families** (see §3).

Retargeting these is a prose edit to a load-bearing citation, so it is the
author's call, not a silent fix. Note the `uses[]` consequence already applied:
the edge to `prop:spectral-sequence-collapse` was **rejected** for
`quantum-dilogarithm-stratified` on exactly this ground and **accepted** for
`phi-q-categorical-truncation`, whose Step 1 does use what the proposition
states.

## 2. A load-bearing hook-length claim attributed to a proposition that lacks it

**Verified in part.** `prf:quantum-dilogarithm-stratified` Step 3(b) asserts

> by [curvature-rank stratification](#prop:curvature-rank-gb-stratification)
> Step 3, the GB-depth of $\lambda$ is
> $\mathrm{depth}_{\mathrm{GB}}(\lambda) = \max_{\square \in \lambda} h(\square)$

`curvature-rank-gb-stratification.md` is four lines and contains **zero**
occurrences of "hook", "partition", or $\lambda$. Its content is
$J^{\,r}(q)/J^{\,r+1}(q) = \{T_w : r(T_w) = r\}$ — a statement about *words*,
not partitions. The closing paragraph of the same proof leans on this
identification to claim *"the structural identification is now explicit."*

The reader reports the same attribution in `two-filtration-bridge.md` and
`gb-depth-period-correspondence.md`, and that both blocks additionally
attribute to it the passage from the *algebra* filtration to a *centre* grading
$Z(A) = \bigoplus_k Z^{(k)}(A)$, which is also not in the target.

**Scope note.** What is established is that *the cited proposition does not
contain the claim*. It is **not** established that the claim is unproved
anywhere in the corpus — the grep for it returns hits across several chapters
and they have not been read. Per the "before declaring open" checklist this is
filed as a **mis-citation**, not as a gap. Resolving it means finding where (or
whether) the identification is actually stated.

## 3. Weight-family collision in `prf:phi-q-categorical-truncation`

Reader's finding. Step 2 writes $w_\lambda = \dim_q^2 V_\lambda / [n]_q!$. Per
AGENTS.md §7aa the three families $y_\lambda$ / $w_\lambda$ / $\tilde w_\lambda$
are **distinct at $q \neq 1$** and must never be conflated: $w_\lambda$ is the
classical Plancherel measure $(\dim V_\lambda)^2/n!$, and the quantity written
is $\tilde w_\lambda$.

`prf:quantum-dilogarithm-stratified` gets this right and flags the distinction
explicitly; `prf:spectral-sequence-collapse` and
`prop:unified-curvature-rank-mass-formula` both use $\tilde w_\lambda$. This
block is the only one wrong, and the error propagates into the section name it
cites (§1).

## 4. A squeeze that is described as degenerating when it fails

Reader's finding, arithmetic checked. `rem:yang-mills-surreal-bound`:

> The squeeze $\delta^2 \cdot \varepsilon^{-1} > \varepsilon^3$ holds strictly
> for every standard-real $\delta > 0$ and **degenerates to the marginal
> equality at $\delta = 0$**.

At $\delta = 0$ the left side is $0$ and the right side is $\varepsilon^3 > 0$,
so the inequality **fails strictly** — it does not become an equality. The block
then draws *"Therefore, the only excitation with zero cost is the trivial one"*
from that mis-described limit. The conclusion may well survive a correct
statement of the limit, but as written the step does not support it.

## Item 4 done, and the diagnosis changed — PR (msc1 squeeze branch), 2026-08-15

The arithmetic in the filing is right: at $\delta = 0$ the squeeze fails
strictly rather than degenerating. But the cause is not a mis-described limit.

[`lem:surreal-squeeze`](../content/quantum-observable-universe/appendix-surreals/surreal-squeeze.md)
is stated for *"$\delta > 0$ a **standard real** number"*. That hypothesis is
the whole content — a standard real beats any infinitesimal. The Yang–Mills
block invokes it at **two values that are not standard reals**: $\delta = 0$,
and again in its conclusion, which quantifies over excitations with
$\delta \asymp \varepsilon^3$. This is the
"conditional-proved ≠ premise-established" family, not a wording slip.

Two further facts, both machine-checked
([`yang_mills_squeeze_threshold.py`](../docs/audits/scripts/yang_mills_squeeze_threshold.py)):

- **The marginal-equality case is real and sits at $\delta = \varepsilon^2$**
  (solve $\delta^2/\varepsilon = \varepsilon^3$). The block had true content
  attached to the wrong $\delta$.
- **The threshold is $\varepsilon^2$, the asserted gap is $\varepsilon^3$** —
  smaller by a factor of $\varepsilon$. An excitation at the asserted gap does
  **not** clear the squeeze, so *"every non-trivial excitation has
  $\delta \geq \Delta_q$"* does not follow from it.

Scope-(a). The gap $\Delta_q \asymp \varepsilon^3 > 0$ is established earlier
in the block by a different route and is untouched; nothing here excludes a
squeeze with an $\varepsilon^3$ threshold. What is fixed is the block claiming
this one supplies it.

Still open (author's call): supply the squeeze that does reach $\varepsilon^3$,
or accept the block's weakened phrasing.

## 5. Smaller items

- **`rem:hecke-charge-mass-duality` misstates the mass formula.** It writes
  $\mathfrak{m} = \mathrm{Vol}(K)/\hbar_q^2$ twice, citing
  `prop:hecke-mass-trace` — which states
  $\mathfrak{m} = |\mathrm{tr}_M(\Phi_{\mathrm{mass}}(\beta))|$. Per the
  AGENTS.md canonical banner the shape is
  $m(K) = m_e \cdot \mathrm{Vol}(K) \cdot \rho(K)/\hbar_q^2$; the block drops
  both $m_e$ and $\rho(K)$.
- **`def:hecke-mass-element` is an undeclared prerequisite of the same block.**
  It opens with $\alpha_\varrho = (\int_A \otimes \mathrm{id}) \circ \Delta
  \circ \varrho$, undefined there and verbatim from that target, and cites it
  in prose exactly as it cites the edges that were adjudicated. It was not in
  the candidate set because it was never pruned. The reader rates it a stronger
  accept than either definition edge it rejected.
- **`prf:phi-q-categorical-truncation` has two undeclared "By [X]" steps** —
  `cor:quantum-dilogarithm` (Step 4) and `prop:quantum-dilogarithm-stratified`
  (gap-closure section). Also not in the candidate set for the same reason.
  Reader adds that Step 4 attributes to the corollary a statement it does not
  make.
- **The two blocks may be consolidation candidates.** Both prove
  $\mathrm{tr}_M(\Phi_q(z_i) T_w) = \mathrm{tr}_M(\Phi_q^{[\leq k_\star]}(z_i)
  T_w)$, both close on the same open uniform-bound note, and each cites the
  other's parent. Worth a `proposition-consolidation-audit` look.
