*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Post-PR-#665 open R&D inventory.**

PR #665's prepare-merge cycle identified six open research items
that remain after the categorical-chain Lean infrastructure shipped.
This block records them with **initial findings** from investigation.

## The six items

| # | Item | Status |
|---:|---|---|
| 1 | $\sigma_1$ off-diagonal substantive discharge | partial (chapter has $\sigma_1$ Hecke quadratic; full matrix-level discharge pending) |
| 2 | Full Hecke algebra type at $H_n(q)$ | open (Mathlib lift) |
| 3 | Per-Wedderburn-block Python probe at $\varepsilon^{10}, \varepsilon^{12}$ | open |
| 4 | Inductive-limit Markov-trace operator construction | open (scaffold present) |
| 5 | Full perturbative-expansion infrastructure on typed-$B_3$ words | open |
| 6 | **Matrix-level Yang-Baxter cubic on $V_{(2,1)}$ Hoefsmit matrices** | **NEGATIVE FINDING** — chapter conventions fail YB |

## Finding 6.A — chapter Hoefsmit $\sigma_1$ fails the YB cubic

Direct symbolic computation of the Yang-Baxter cubic identity

$$
  \sigma_0\,\sigma_1\,\sigma_0 \;=\; \sigma_1\,\sigma_0\,\sigma_1
$$

on the chapter file [`prop:hoefsmit-V21-cos-symmetrization`](#prop:hoefsmit-V21-cos-symmetrization)'s
explicit matrices

  - $\sigma_0 = \begin{pmatrix} q & 0 \\ 0 & -q^{-1} \end{pmatrix}$
  - $\sigma_1 = \begin{pmatrix} d_1 & b \\ b & d_2 \end{pmatrix}$
  - $d_1 = q^3/(q^2 + 1)$, $d_2 = -q^{-1}/(q^2 + 1)$,
    $b^2 = d_1 d_2 + 1 = (q^4+q^2+1)/(q^2+1)^2$

yields a $(0,0)$-entry constraint

$$
  q^2 \cdot d_1
  \;\stackrel{?}{=}\;
  q \cdot d_1^2 \;-\; q^{-1} \cdot b^2
  \;\;\Leftrightarrow\;\;
  b^2 \;\stackrel{?}{=}\; q^2 \cdot d_1 \cdot (d_1 - q)
  \;\;\Leftrightarrow\;\;
  b^2 \;\stackrel{?}{=}\; -\frac{q^6}{(q^2+1)^2}
$$

since $d_1 - q = -q/(q^2+1)$. But the chapter's $b^2$ is **strictly
positive**, so the YB-required value is **impossible**.

## Implications

The chapter $\sigma_1$ satisfies:

  - Hecke quadratic $\sigma_1^2 = (q - q^{-1})\sigma_1 + 1$  (proved)
  - trace $= q - q^{-1}$  (proved)
  - det $= -1$  (proved)

but is **not** part of an $H_3$ representation with
$\sigma_0 = \mathrm{diag}(q, -q^{-1})$.

## The fix: swap $d_1$ and $d_2$

Solving the YB cubic constraint analytically: with
$\sigma_0 = \mathrm{diag}(q, -q^{-1})$ and the trace
$d_1 + d_2 = q - q^{-1}$ plus the (0,1)-entry YB constraint
$q d_1 - q^{-1} d_2 = -1$, we get **uniquely**
$d_1 = -q^{-1}/(q^2 + 1)$, hence $d_2 = q^3/(q^2 + 1)$ — literally
the chapter's $d_2$ and $d_1$ **swapped**. With the swap,
$b^2 = (q^4 + q^2 + 1)/(q^2 + 1)^2$ holds (positive, matching the
chapter's value).

**The fix is a 1-line edit**: swap the definitions of
`hoefsmit_d1` and `hoefsmit_d2`.

### Zero downstream regressions from the swap

The swap is a basis-permutation, so:

  - `hoefsmit_b_sq = d_1 * d_2 + 1` is symmetric $\to$ unchanged
  - Hecke quadratic still holds (constraints at (0,0) and (1,1) swap, both true)
  - All scalar invariants (trace, det, eigenvalues, `hoefsmitB`, Markov trace $\tau_M$) are basis-permutation-invariant
  - `N_k_factor` formulae in the precision ladder use only `hoefsmitB q` (= $b$) $\to$ unaffected
  - `ckFromReduction q k` uses only `hoefsmitB_local q` $\to$ unaffected
  - τ_M numerical predictions at $q_0$ are unchanged (all use traces / Wedderburn dimensions)

## What this means for the c_k chain

The numerical residual at $q = 2$ is recorded in
`yb_residual_00_at_two_ne_zero` (closed by `norm_num`). At
substrate $q_0 \approx 1.11$ the residual is also non-zero.

**Does this break the c_k chain?** Not necessarily — the chapter's
$\sigma_1$ may be a non-standard parameterisation that still gives
the correct $\tau_M$ values empirically. But the SIBLING of
[`rem:ck-extraction-from-algebraic-rules`](#rem:ck-extraction-from-algebraic-rules)
that asserts "Rule 1 (Yang-Baxter cubic) is discharged at H_3 on
V_(2,1) by the Hoefsmit matrices" needs a correction or a basis
change to be substantively true.

This is the **first concrete substantive R&D finding** post-PR-#665,
recorded here for future investigation. The fix is mechanical
(swap $d_1 = q/(q^2+1)$ in place of $q^3/(q^2+1)$, then re-verify
all downstream theorems) but requires care to not break the existing
Hecke quadratic / cos-symmetrisation chain.

## Status

**Negative finding, recorded.** Items 1-5 remain open per the table
above. The YB anomaly (item 6) is a concrete substantive issue
identified in this branch's R&D phase and is the recommended
**first follow-up** after PR #665 lands.
