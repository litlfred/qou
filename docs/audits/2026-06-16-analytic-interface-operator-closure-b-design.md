# Analytic interface operator `A^λ_{ξν}(I)` — closure path (b) design + prototype

**Date:** 2026-06-16
**Branch:** `claude/analytic-interface-operator-closure-b-2026-06-16`
**Track:** B (recursive ρ_ξ / operator-valued branching combiner for per-isotope binding)
**Status:** design + structural finding + runnable preflight scaffold. The full
`A≥3` closure is a multi-phase implementation; this document fixes the
mathematics and the verification plan, and ships the first preflight increment.
**Trigger:** follow-up to
[`2026-06-16-hyperbolic-hurdle-dialog-assessment.md`](2026-06-16-hyperbolic-hurdle-dialog-assessment.md)
§"Going deeper on ③" — closure path (b) of
[`2026-05-18-recursive-rho-xi-blocked-by-underdetermined-extracts.md`](2026-05-18-recursive-rho-xi-blocked-by-underdetermined-extracts.md).

## The structural finding (formalize-first)

The operator-valued Wenzl branching combiner
([`canonical_tr_m_via_branching.py`](../../computations/canonical_tr_m_via_branching.py))
peels one nucleon at a time via

$$
\chi^\lambda\!\left(W_{\text{inner}}\cdot I\cdot \beta_{\text{block}}\right)
  = \sum_{\substack{\xi\,\vdash\,n-3\\ \nu\,\vdash\,3}}
      \operatorname{Tr}_{V_\xi\otimes V_\nu}\!\Big(
        A^{\lambda}_{\xi\nu}(I)\cdot
        \big(\rho_\xi(W_{\text{inner}})\otimes\rho_\nu(\beta_{\text{block}})\big)
      \Big),
$$

where $I = c\,\sigma_{n-4} + d\,\mathbb{1}$ is the interface (the **bridge
generator** $\sigma_{n-4}$ that lies between the Young subalgebra factors
$\mathbf H_{n-3}\times\mathbf H_3$, deformed by the flavour coefficients
$(c,d)$ — $pp{=}(1,0)$, $nn{=}(1,-h)$, $pn{=}(1,-h/2)$).

The current extractor
([`a_operator/A_operator_extract_at_level.py`](../../computations/a_operator/A_operator_extract_at_level.py))
**fits** $A^\lambda_{\xi\nu}(I)$ by least-squares over a small $\mathbf H_3$
test-word family. This is rank-deficient for $n\ge9$ (e.g. $\lambda=[4,3,1,1]$
at $\mathbf H_9$ has $n_{\text{unknowns}}=3390$, rank $66$), so the fitted $A$
reproduces $\chi^\lambda$ on the $\mathbf H_3$ test set it was fit on but
predicts the wrong $\chi^\lambda$ when the inner braid is a 2-nucleon deuteron
at $\mathbf H_6$ — the $21$–$42\%$ error on T and ³He.

**The finding: $A^\lambda_{\xi\nu}(I)$ is not a quantity to fit. It is the
$(\xi,\nu)$-isotypic diagonal block of the seminormal interface-generator
matrix $\rho_\lambda(I)$, expressed in the branching-adapted basis** — a known
generator-matrix block, **universal by construction**.

### Why this is the right object

In the Young/Hoefsmit seminormal representation of $\mathbf H_n(q)$ on $V_\lambda$:

1. **The inner factor acts block-diagonally.** $W_{\text{inner}}\in\mathbf
   H_{n-3}=\langle\sigma_0,\dots,\sigma_{n-5}\rangle$ acts only on entries
   $\{1,\dots,n-3\}$. In the seminormal basis (adapted to the chain
   $1\subset2\subset\cdots\subset n$), the sub-shape $\xi$ formed by entries
   $\{1,\dots,n-3\}$ is well-defined per basis vector, and $\rho_\lambda(W)$
   restricted to the $\xi$-block is exactly $\rho_\xi(W)\otimes\mathbb1$.
2. **The block factor acts block-diagonally.** $\beta_{\text{block}}\in\mathbf
   H_3=\langle\sigma_{n-3},\sigma_{n-2}\rangle$ acts only on entries
   $\{n-2,n-1,n\}$, as $\mathbb1\otimes\rho_\nu(\beta_{\text{block}})$ within
   the $(\xi,\nu)$-isotypic sector.
3. **Only the bridge generator mixes the centers.** $\rho_\lambda(\sigma_{n-4})$
   is the *one* operator that couples entry $n-3$ (last of the inner factor) to
   entry $n-2$ (first of the block). It is the genuine "two-center coupling."

Because $W$ acts within $\xi$-blocks and $\beta_{\text{block}}$ within
$\nu$-blocks (no mixing) and the trace is cyclic, **only the diagonal
$(\xi,\nu)\to(\xi,\nu)$ isotypic block of $\rho_\lambda(I)$ survives the trace**.
Off-diagonal blocks $(\xi,\nu)\to(\xi',\nu')$ would carry $\rho_{\xi'}(W)\otimes
\rho_{\nu'}(\beta)$ between *different* irreps and vanish under the closed trace.
Hence

$$
\boxed{\;A^\lambda_{\xi\nu}(I)\;=\;\Pi_{\xi\nu}\,\rho_\lambda(I)\,\Pi_{\xi\nu}\;}
$$

the compression of $\rho_\lambda(I)=c\,\rho_\lambda(\sigma_{n-4})+d\,\mathbb1$
to the $(\xi,\nu)$-isotypic subspace, transported into the $V_\xi\otimes V_\nu$
coordinates by the branching embedding $V_\xi\otimes V_\nu\hookrightarrow
\operatorname{Res}V_\lambda$.

### The `I = identity` sanity anchor (already in the corpus)

When the bridge generator is absent ($c=0,\,d=1$, i.e. a **disjoint** tensor
braid), the compression is the scalar projection and

$$
A^\lambda_{\xi\nu}(\mathbb1)=c^\lambda_{\xi\nu}\,\mathbb1_{d_\xi d_\nu},
\qquad
\chi^\lambda(\beta_1\otimes\beta_2)
  =\sum_{\xi,\nu}c^\lambda_{\xi\nu}\,\chi^\xi(\beta_1)\,\chi^\nu(\beta_2),
$$

which is **exactly the existing character-level Wenzl LR bridge**
[`tools/hecke-engine/src/wenzl_lr.rs`](../../tools/hecke-engine/src/wenzl_lr.rs)
`chi_via_lr_2way`. So the interface operator is the **bridge-generator
deformation of the LR scalar $c^\lambda_{\xi\nu}\mathbb1$** — and the
`I=identity` reduction is a free, runnable cross-check against existing
production infra. The prototype scaffold implements this first.

## Why this closes `A≥3`

The fitted $A$ failed at $A\ge3$ because least-squares cannot recover a
$(d_\xi d_\nu)^2$-entry generator block from $\mathcal O(\text{tens})$ of
$\mathbf H_3$ test-word equations. The analytic $A$ has **no test-word
dependence** — it is a fixed compression of a fixed generator matrix, identical
for any inner family (single nucleon, deuteron, triton, …). Constructing it once
per $(\lambda,\xi,\nu)$ makes the combiner correct at every $A$, subject only to
the cost of the seminormal generator matrix at $\mathbf H_n$ (the same cost the
fit already paid to generate $\chi^\lambda$ test data).

## Construction algorithm (build on existing infra — do not reinvent)

| Step | Object | Existing primitive |
|------|--------|--------------------|
| 1 | seminormal matrices $\rho_\lambda(\sigma_i)$ at $\mathbf H_n$ | `char_fast._compiled_sigmas`; `tools/hecke-engine/src/seminormal.rs` / `seminormal_mpfr.rs` |
| 2 | LR multiplicities $c^\lambda_{\xi\nu}$ | `substrate/lr_coefficients.get_lr_table`; `tools/hecke-engine/src/littlewood_richardson.rs` |
| 3 | restriction $\operatorname{Res}^{\,\mathbf H_n}_{\mathbf H_{n-3}\times\mathbf H_3}V_\lambda=\bigoplus c^\lambda_{\xi\nu}V_\xi\boxtimes V_\nu$ | `tools/hecke-engine/src/cross_level_embedding.rs` `multi_lr` / `verify_edge`; `pyhecke.skew_syt` |
| 4 | $\xi$-grouping of the seminormal basis (entries $\{1..n-3\}$ shape) | automatic in the seminormal basis (chain-adapted) |
| 5 | $\nu$-isotypic projection within each $\xi$-block (the skew rep $\lambda/\xi$ under $\langle\sigma_{n-3},\sigma_{n-2}\rangle$) | $\mathbf H_3$ central idempotents; `pyhecke.skew_syt.skew_syt_count` for dimension checks |
| 6 | $V_\xi\otimes V_\nu$ embedding (the **crux**, ~the 500 LOC) | `wenzl_lr.rs` (character form, to be lifted to operator form) + Wenzl 1988 explicit branching matrices |
| 7 | compress $\rho_\lambda(I)$ to the $(\xi,\nu)$ block in $V_\xi\otimes V_\nu$ coords | new — this module |

Step 6 is the genuinely new representation-theory work: the existing
`wenzl_lr.rs` realizes the LR bridge at the **character (trace) level**; the
operator-valued $A$ needs the **operator-level** embedding so the bridge
generator can be compressed into $V_\xi\otimes V_\nu$ coordinates rather than
traced away.

## Verification plan (§3 algebraic preflight — smallest non-trivial first)

The deuteron is the full-rank anchor: its $\mathbf H_6$ fitted extract is
verified end-to-end against `markov_peel` at $7\times10^{-15}$, so it is the
ground truth for the analytic construction.

1. **`I=identity` reduction** (this PR's scaffold): analytic
   $A^\lambda_{\xi\nu}(\mathbb1)$ equals $c^\lambda_{\xi\nu}\mathbb1$ for every
   $\lambda\vdash6$, cross-checked against `get_lr_table` and against
   `wenzl_lr.chi_via_lr_2way`. **Runnable now**, no operator embedding needed.
2. **Deuteron analytic $A$** (next): construct $A^\lambda_{\xi\nu}(I_{pn})$ from
   the seminormal $\sigma_2$ block; require it to (a) match the full-rank
   $\mathbf H_6$ fitted extract entrywise (modulo the $V_\xi\otimes V_\nu$ basis
   gauge) and (b) reconstruct $\operatorname{tr}_M(D)$ matching the transfer-
   matrix / `markov_peel` reference at $\mathbf{1e\text{-}25}$ (50 dps — **not**
   the f64 `1e-6` the fitter tolerates; cf. compute-author §1.1).
3. **$\mathbf H_9$ universality** (the payoff): construct $A^\lambda_{\xi\nu}$ at
   $\mathbf H_9$ analytically and reconstruct $\operatorname{tr}_M$(T), (³He)
   matching the transfer-matrix reference at $1e\text{-}25$ — the case the fitted
   extract misses by $21$–$42\%$.

A precision note carried from compute-author §1: the existing fitter runs in
**numpy f64**. The analytic construction must be carried in **mpmath /
exact rational** to meet the L1 floor; f64 is acceptable only for the scaffold's
`I=identity` integer cross-check (where $A=c\,\mathbb1$ has integer entries).

## Scope of this PR

- This design document (the structural finding + algorithm + verification plan).
- A runnable scaffold [`computations/a_operator/a_operator_analytic.py`](../../computations/a_operator/a_operator_analytic.py)
  implementing **preflight step 1** (the `I=identity` reduction to
  $c^\lambda_{\xi\nu}\mathbb1$, cross-checked against the LR table) with a
  witness emission. Steps 2–3 are scaffolded with explicit `TODO(closure-b)`
  markers and the precise object each must produce.

This is a **prototype / first increment**, not the closure. It does not change
any production path (`canonical_tr_m_via_branching.py` still routes $A\ge3$
through the lossless fine-Bratteli transfer matrix). It fixes the mathematics so
the remaining work is implementation against a verified spec, not search.

## What this PR does NOT do / claim

- Does **not** claim `A≥3` is closed — only that the object is identified and
  the smallest preflight passes.
- Does **not** introduce a fit, a fourth calibration, or a new constant — the
  LR coefficients and seminormal generator matrices are existing categorical
  objects.
- Does **not** touch the hyperbolic-volume compute (per the sibling audit's
  critical-distance flag).

## Cross-references

- [`docs/audits/2026-06-16-hyperbolic-hurdle-dialog-assessment.md`](2026-06-16-hyperbolic-hurdle-dialog-assessment.md) — §"Going deeper on ③" (the parent finding).
- [`docs/audits/2026-05-18-recursive-rho-xi-blocked-by-underdetermined-extracts.md`](2026-05-18-recursive-rho-xi-blocked-by-underdetermined-extracts.md) — closure paths (a)/(b)/(c)/(d); this is (b).
- [`computations/canonical_tr_m_via_branching.py`](../../computations/canonical_tr_m_via_branching.py) — the combiner (consumer).
- [`computations/a_operator/A_operator_extract_at_level.py`](../../computations/a_operator/A_operator_extract_at_level.py) — the fitted extractor this replaces.
- [`tools/hecke-engine/src/wenzl_lr.rs`](../../tools/hecke-engine/src/wenzl_lr.rs) — character-level LR bridge (the `I=identity` case).
- [`tools/hecke-engine/src/cross_level_embedding.rs`](../../tools/hecke-engine/src/cross_level_embedding.rs) — restriction multiplicities `multi_lr`.
- [`tools/hecke-engine/src/seminormal.rs`](../../tools/hecke-engine/src/seminormal.rs) / [`seminormal_mpfr.rs`](../../tools/hecke-engine/src/seminormal_mpfr.rs) — seminormal generator matrices.
- [`tools/pyhecke/python/pyhecke/skew_syt.py`](../../tools/pyhecke/python/pyhecke/skew_syt.py) — skew-SYT counts for the $\lambda/\xi$ dimension checks.
