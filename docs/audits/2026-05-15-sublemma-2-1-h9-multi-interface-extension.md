# Sub-lemma 2.1 — multi-interface extension to $H_9$ (tritium / ³He)

**Date:** 2026-05-15
**Branch:** `claude/substrate-deriv-A-minus-2-q`
**Status:** **Scaffold + math.** No compute run yet; documents the
extension framework and identifies the substantive next-compute
step (new $H_9$ operator-valued $A^\lambda_{\xi\nu}(I_2)$ extraction).
Pure derivation — no fitting / calibration / numerology.

## Background — single-interface closure (already done)

The **refined Sub-lemma 2.1** (PR #534, audit
[`2026-05-04-sublemma-2-1-refined.md`](2026-05-04-sublemma-2-1-refined.md))
established the operator-valued formula at a **single interface**:

$$
\chi^\lambda(\beta_1 \cdot I \cdot \beta_2)
\;=\;
\sum_{(\mu, \nu)} c^\lambda_{\mu \nu}
\cdot \mathrm{Tr}_{V_\mu \otimes V_\nu}\bigl(
A^\lambda_{\mu \nu}(I) \cdot (\rho_\mu(\beta_1) \otimes \rho_\nu(\beta_2))
\bigr)
$$

with $A^\lambda_{\mu \nu}(I) \in \mathrm{End}(V_\mu \otimes V_\nu)^{\oplus c^\lambda_{\mu \nu}}$
the operator-valued interface coefficient. For the deuteron
$(\beta_1 = \beta_p \in H_3, I = I_{pn} = \sigma_2 - h/2, \beta_2 = \beta_n \in H_3)$
this is **verified at machine ε** (max residual $6.87 \times 10^{-15}$
across all 11 $\lambda \vdash 6$) in
[`sublemma-2-1-A-operator-extract.witness.json`](../../computations/sublemma-2-1-A-operator-extract.witness.json).

The single-interface formula closes the canonical Δ_λ derivation at
the deuteron. The pending extension is to atoms with $\geq 2$
interfaces.

## Multi-interface braid words

For atoms beyond deuteron, the canonical braid word $\beta(Z, N)$
contains $A - 1$ inter-nucleon interfaces (per
[`def:canonical-braid-interface-composition`](../../content/quantum-observable-universe/braids-and-knots/canonical-braid-interface-composition.md)):

| atom | $(Z, N)$ | interfaces | structure |
|---|---|---|---|
| deuteron | $(1, 1)$ | 1 | $\beta_p \cdot I_{pn} \cdot \beta_n$ |
| tritium | $(1, 2)$ | 2 | $\beta_p \cdot I_{pn} \cdot \beta_n \cdot I_{nn} \cdot \beta_n$ |
| ³He | $(2, 1)$ | 2 | $\beta_p \cdot I_{pp} \cdot \beta_p \cdot I_{pn} \cdot \beta_n$ |
| ⁴He | $(2, 2)$ | 3 | $\beta_p \cdot I_{pp} \cdot \beta_p \cdot I_{pn} \cdot \beta_n \cdot I_{nn} \cdot \beta_n$ |

The interfaces are bare Hecke generators in $H_{3A}(q)$:
- $I_{pp} = \sigma_{3k+2}$ (positive, pp)
- $I_{pn} = \sigma_{3k+2} - h/2 \cdot 1$ (averaged, pn)
- $I_{nn} = \sigma_{3k+2} - h \cdot 1$ (negative-equivalent, nn)

## Iterative 2-interface formula

For a 2-interface braid in $H_9 = H_3 \otimes H_3 \otimes H_3$:

$$
\beta_K
\;=\;
\underbrace{(\beta_1 \cdot I_1 \cdot \beta_2)}_{=: W_{\mathrm{inner}} \in H_6}
\;\cdot\; I_2 \;\cdot\; \beta_3
$$

where $W_{\mathrm{inner}}$ is an $H_6$ braid (the "inner deuteron-like
factor") and $I_2 \cdot \beta_3$ adds one interface + 3 more strands.

Apply Sub-lemma 2.1 at $H_9 \downarrow H_6 \times H_3$:

$$
\chi^\lambda(\beta_K)
\;=\;
\sum_{\xi \vdash 6, \, \nu \vdash 3}
c^\lambda_{\xi \nu}
\cdot \mathrm{Tr}_{V_\xi \otimes V_\nu}\bigl(
A^\lambda_{\xi \nu}(I_2)
\cdot (\rho_\xi(W_{\mathrm{inner}}) \otimes \rho_\nu(\beta_3))
\bigr).
$$

The $\rho_\xi(W_{\mathrm{inner}})$ factor is a **full matrix operator
on $V_\xi$** (NOT a scalar) — Sub-lemma 2.1 applied at $H_6 \downarrow
H_3 \times H_3$ gives it as a sum over the $H_3 \times H_3$ branching:

$$
\rho_\xi(\beta_1 \cdot I_1 \cdot \beta_2)\bigl|_{V_\mu \otimes V_{\nu'}}
\;=\;
A^\xi_{\mu \nu'}(I_1) \cdot (\rho_\mu(\beta_1) \otimes \rho_{\nu'}(\beta_2)).
$$

Substituting:

$$
\boxed{\quad
\chi^\lambda(\beta_K)
\;=\;
\sum_{\xi, \nu, \mu, \nu'}
c^\lambda_{\xi \nu} \cdot c^\xi_{\mu \nu'}
\cdot \mathrm{Tr}\bigl[
A^\lambda_{\xi \nu}(I_2)
\cdot \bigl(A^\xi_{\mu \nu'}(I_1) \cdot (\rho_\mu \otimes \rho_{\nu'})\bigr) \otimes \rho_\nu(\beta_3)
\bigr]
\quad}
$$

This is the **iterated 2-interface formula**: products of LR
coefficients times traces of composed operator-valued $A$'s acting
on tensor products of $\rho$ matrices.

## What needs to be extracted (the new compute)

The single-interface $A$ values that exist:

- $A^\lambda_{\mu \nu}(I_{pn})$ at $H_6$ for the deuteron interface
  $I_{pn} = \sigma_2 - h/2$: **verified at machine ε** in
  [`sublemma-2-1-A-operator-extract.witness.json`](../../computations/sublemma-2-1-A-operator-extract.witness.json).

The single-interface $A$ values needed for tritium / ³He:

- $A^\lambda_{\xi \nu}(I_2)$ at $H_9 \downarrow H_6 \times H_3$ where
  $I_2 \in \{I_{nn}, I_{pn}, I_{pp}\}$ — the OUTER interface.
- $A^\xi_{\mu \nu'}(I_1)$ at $H_6 \downarrow H_3 \times H_3$ where
  $I_1 \in \{I_{pn}, I_{pp}, I_{nn}\}$ — the INNER interface,
  but at $H_6$ (already covered for $I_{pn}$; need fresh extraction
  for $I_{pp} = \sigma_2$ and $I_{nn} = \sigma_2 - h$).

So **three new $A$-extractions**:

1. $A^\xi_{\mu \nu'}(I_{pp})$ at $H_6$ (for ³He inner block)
2. $A^\xi_{\mu \nu'}(I_{nn})$ at $H_6$ (for tritium inner block — already if symmetric to $I_{pn}$?)
3. $A^\lambda_{\xi \nu}(I_2)$ at $H_9$ for each of $\{I_{pn}, I_{nn}, I_{pp}\}$

The $H_9$ extraction is the substantive new compute. The existing
`sublemma_2_1_A_operator_extract.py` extracts at $H_6$ via bilinear-
system inversion across $K \sim 12$ test words → $K^2 \sim 144$ chi
evaluations per partition × 11 partitions ≈ 1600 evaluations at
$H_6$.

At $H_9$ the cost scales:
- 30 partitions of 9 (instead of 11)
- $K^2 \sim 144$ test pairs still (same recipe)
- Per evaluation: Hoefsmit at $H_9$ is ~10× slower than $H_6$
- Total: $\sim 30 \times 144 \times 10 = 4.3 \times 10^4$ evaluations,
  ~minutes to hours

The bilinear inversion per partition: support size scales linearly,
inversion polynomial-time in matrix dim.

## Verification strategy

The probe writes itself:

1. Build the canonical tritium braid $\beta_T \in H_9$ via
   `mass_at_3A_proper.atom_braid_word_3A(1, 2)` (already done).
2. **Path A (truth):** compute $\chi^\lambda(\beta_T)$ directly via
   Hoefsmit at $H_9$ for each $\lambda \vdash 9$ (30 partitions).
3. **Path B (derivation):** compute via the iterated 2-interface
   formula above, using:
   - $A^\lambda_{\xi \nu}(I_{nn})$ at $H_9$ (newly extracted)
   - $A^\xi_{\mu \nu'}(I_{pn})$ at $H_6$ (existing)
   - $\rho_\mu(\beta_p), \rho_{\nu'}(\beta_n), \rho_\nu(\beta_n)$ from
     `evaluate_word_matrix` (existing)
4. **Verification:** max relative residual ≤ $10^{-12}$ across all
   30 partitions.

If verification passes: Δ_λ is canonically derived at $H_9$ for
tritium, and the same recipe applies to ³He (different interface
sequence) and ⁴He (3 interfaces, iterated 3-fold).

## Compute scope

| step | atoms | est. time |
|---|---|---|
| 1. $H_6$ extraction for $I_{pp}, I_{nn}$ | (single-interface, reuses existing infra) | ~30 s |
| 2. $H_9$ extraction for $I_{pn}, I_{nn}$ | (new H_9 infra; one-time per interface type) | ~5–30 min |
| 3. Tritium verification | (composes existing + new A's) | ~10 s |
| 4. ³He verification | (reuses A's from #1 + #2) | ~10 s |
| 5. ⁴He verification (3-interface) | requires further $H_{12}$ extraction | (out of scope for v1) |

**Phase 1 deliverable**: H_6 + H_9 A-extractions + tritium/³He
verification. ⁴He is phase 2 (additional H_12 work).

## Categorical content (not fitting)

This is **derivation-verification**, not fitting:

- The LR coefficients $c^\lambda_{\xi\nu}, c^\xi_{\mu\nu'}$ are
  **categorical** (Schur-Weyl, hand-verified or computable from
  `partitions_of` + Pieri's rule).
- The Hoefsmit $\rho_\lambda$ matrices are **categorical**
  (seminormal representation, no fitting).
- The $A^\lambda_{\mu\nu}(I)$ are **extracted by linear-system
  inversion** from independently-computed $\chi^\lambda$ values
  via test words — NOT fit to AME or any experimental data.
- The verification confirms the derivation closes to machine ε
  (numerical proxy for proof; if it didn't close, the iterated
  formula would be wrong).

Per AGENTS.md three-calibration discipline: this probe uses only
$q_0$ (CAL-2) as a calibration input; no $m_e$, $Q_\beta$, or AME
data enters.

## Cross-references

- [`docs/audits/2026-05-04-sublemma-2-1-refined.md`](2026-05-04-sublemma-2-1-refined.md)
  — single-interface operator-valued formula (parent)
- [`docs/audits/2026-05-08-crystal-r-matrix-sublemma-2-1.md`](2026-05-08-crystal-r-matrix-sublemma-2-1.md)
  — q→0 crystal-bases proof (alternative route at $q = 0$)
- [`computations/sublemma_2_1_A_operator_extract.py`](../../computations/sublemma_2_1_A_operator_extract.py)
  — existing $H_6$ extraction infra
- [`computations/v_hat_to_chi_lambda_integrated.py`](../../computations/v_hat_to_chi_lambda_integrated.py)
  — single-interface 1-dim + multi-dim unified at $H_6$
- [`def:canonical-braid-interface-composition`](../../content/quantum-observable-universe/braids-and-knots/canonical-braid-interface-composition.md)
  — interface-type counts $(n_{pp}, n_{pn}, n_{nn})$ per atom
