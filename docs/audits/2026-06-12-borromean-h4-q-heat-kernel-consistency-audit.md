# Borromean h⁴ derivation vs q-heat-kernel framework: consistency audit

**Date:** 2026-06-12
**Branch:** `claude/gap-a4-post-merge-consolidation-2026-06-12`
**Scope:** Audit the cross-references in `prop:borromean-h4-categorical-derivation` (merged in [PR #1942](https://github.com/litlfred/qou/pull/1942)) against the Habiro-from-q-heat-kernel infrastructure (merged in PR #2131).

## TL;DR

The within-H_3 derivation `h⁴(tr_M(β_Bor)) = (−3) · (1/4) = −3/4` stands unchanged. Two of the cross-references in the merged `prop:borromean-h4-categorical-derivation` are however **structurally adjacent rather than directly causal**, and one **new structural fact** (the *uniform Wenzl-at-q=1 value* on H_n) is implicit in the derivation but not yet codified.

**Recommended actions:**
1. Codify `prop:symmetric-point-wenzl-markov-uniform` — the new fact `y_λ(q=1) = 1/[2]_q^{n-1}|_{q=1} = 1/2^{n-1}` (uniform across all H_n irreps), distinct from the Plancherel measure of `rem:symmetric-point-resolution-loss`.
2. Adjust `prop:borromean-h4-categorical-derivation` cross-references in a small follow-up patch: cite the new uniform-Wenzl prop in place of `rem:symmetric-point-resolution-loss`; downgrade `prop:q-heat-kernel-peter-weyl` reference from "the polynomial form derives from" to "the partition-indexing framework".

## Notation register — $\mu_\lambda$ vs $\chi^\lambda$

Both quantities are **indexed by the same partition** $\lambda \vdash n$
labelling Hecke-algebra irreps $V_\lambda$, but they extract *different*
information from the same block:

| Symbol | Defined on | Operator on $V_\lambda$ | Domain of meaning |
|---|---|---|---|
| $\mu_\lambda(q) \in \mathbb{C}$ | partition $\lambda$ alone | $q$-Laplacian $\Delta_q$ | spectral / heat-flow |
| $\chi^\lambda(g) \in \mathbb{C}$ | $\lambda$ **and** a group/algebra element $g$ | $\rho_\lambda(g)$ | character / trace |
| $y_\lambda(q) \in \mathbb{C}$ | partition $\lambda$ alone | Frobenius coefficient | Markov-trace weighting |

The notational similarity is real but not equational: $\mu_\lambda$
answers "what scale does the $q$-heat flow decay at on the $V_\lambda$
component?" while $\chi^\lambda(\beta_{\mathrm{Bor}})$ answers "what
trace does the *specific braid* $\beta_{\mathrm{Bor}}$ have when acted
on $V_\lambda$?".  The two propositions on `main` use these symbols
consistently within themselves, but anyone reading them together
should keep them strictly separate.

**Optional follow-up:** consider adding an entry to
`content/quantum-observable-universe/notation/notation-collisions.md`
that distinguishes $\mu_\lambda$, $\chi^\lambda$, $y_\lambda$, and the
Plancherel $w_\lambda$ explicitly, since all four are
$\lambda$-indexed scalars but encode independent data.

## Finding 1 — `prop:q-heat-kernel-peter-weyl` gives spectral eigenvalues, not character values

The proposition formalises the spectral decomposition

$$
  u(t, x) \;=\; \sum_{\lambda \in \widehat{H_n(q)}}
    d_\lambda(q) \cdot e^{-\mu_\lambda(q)\,t}  \cdot \pi_\lambda(u_0)(x),
$$

with explicit eigenvalue formula

$$
  \mu_\lambda(q)
  \;=\;
  \hbar_q^2  \sum_{\square \in \lambda}  [c(\square)]_q \, [c(\square) + 1]_q.
$$

For the standard partition $(2,1) \vdash 3$ with cell contents $\{0, 1, -1\}$:

$$
  \mu_{(2,1)}(q)
  \;=\;
  \hbar_q^2 \cdot \bigl([0]_q[1]_q + [1]_q[2]_q + [-1]_q[0]_q\bigr)
  \;=\;
  \hbar_q^2 \cdot [2]_q.
$$

This is the **q-Laplacian eigenvalue on $V_{(2,1)}$** — the heat-flow decay rate of the (2,1) isotypic component. It is **not** the character value $\chi^{(2,1)}(\beta_{\mathrm{Bor}}) = 2 - 3h^4 - h^6$, which comes from evaluating the (2,1) irreducible representation on the *specific braid* $\beta_{\mathrm{Bor}} \in B_3$.

**What `prop:q-heat-kernel-peter-weyl` *does* supply for the Borromean h⁴ derivation:** the **Wedderburn-decomposition framework** indexed by partitions $\lambda \vdash n$ — the same framework the Frobenius expansion in Step 2 of `prop:borromean-h4-categorical-derivation` relies on. That is genuinely shared structure.

**What it *does not* supply:** the polynomial form $\chi^{(2,1)}(\beta_{\mathrm{Bor}}) = 2 - 3h^4 - h^6$ itself. That comes from either (a) direct algebraic substitution on the closed-form trace `prop:borromean-markov-trace-closed-form` (T15's derivation), or (b) the Hecke spectral projector `QOU.Hecke.SpectralProjector` extracting the (2,1) channel of $\sigma_1^{-1}\sigma_2$ on $V_{1/2}^{\otimes 3}$ (T17's R-matrix derivation).

**Fix:** soften the `prop:q-heat-kernel-peter-weyl` cross-reference in `prop:borromean-h4-categorical-derivation` from "the polynomial form derives from" to "the partition-indexing framework matches".

## Finding 2 — `rem:symmetric-point-resolution-loss` covers Plancherel, not Wenzl/Markov

The remark explicitly states the measure being preserved at $q = 1$ is the **Plancherel weight**

$$
  w_\lambda(q) \;=\; [n]_q! \,/\, H_q(\lambda)^2,
\qquad w_\lambda(1) \;=\; d_\lambda^2 / n!.
$$

For $\mathrm{H}_3$ this gives the *non-uniform* Plancherel measure $\bigl(d_{(3)}^2/6, d_{(2,1)}^2/6, d_{(1^3)}^2/6\bigr) = (1/6, 2/3, 1/6)$ that satisfies $\sum_\lambda w_\lambda = 1$.

The merged `prop:borromean-h4-categorical-derivation` (T18) however derives

$$
  y_\lambda(q=1) \;=\; \tfrac{1}{4} \;=\; \frac{1}{[2]_q^{\,n-1}}\bigg|_{q=1} \;=\; \frac{1}{2^{n-1}}
\quad \text{(uniform across all }\mathrm{H}_3\text{ irreps),}
$$

from the **Markov-normalisation constraint** $\sum_\lambda y_\lambda \cdot d_\lambda = \mathrm{tr}_M(\mathbf{1}_n) = 1$. For $\mathrm{H}_3$ that is $y_{(3)} + 2\,y_{(2,1)} + y_{(1^3)} = 1$ which (combined with bar-involution symmetry $q \leftrightarrow q^{-1}$ exchanging $(3) \leftrightarrow (1^3)$) gives all three equal to $1/4$.

These are **different measures**:

| Object | Definition | Value at $q = 1$ for $\mathrm{H}_3$ | Sum identity |
|---|---|---|---|
| Plancherel $w_\lambda$ | $[n]_q! / H_q(\lambda)^2$ | $1/6,\ 2/3,\ 1/6$ | $\sum_\lambda w_\lambda = 1$ |
| Wenzl/Markov $y_\lambda$ | trace-class coefficients of $\mathrm{tr}_M$ | $1/4,\ 1/4,\ 1/4$ | $\sum_\lambda y_\lambda d_\lambda = 1$ |

The relationship is conceptual (both express q=1 symmetric-point behaviour of partition-indexed measures) but not equational.

**Fix:** the `prop:borromean-h4-categorical-derivation` markdown narrates "the symmetric-point Wenzl collapse" as if it inherits from `rem:symmetric-point-resolution-loss`. It does not — the resolution-loss remark covers Plancherel. The fix is to **codify the uniform Wenzl-at-q=1 fact** as a new proposition (Finding 3 below) and re-aim the cross-reference there.

## Finding 3 — `prop:symmetric-point-wenzl-markov-uniform` is implicit but not codified

The fact

$$
  \boxed{\;\;
  y_\lambda(q=1) \;=\; \frac{1}{[2]_q^{\,n-1}}\bigg|_{q=1} \;=\; \frac{1}{2^{\,n-1}}
  \quad\text{for every } \lambda \vdash n,
  \;\;}
$$

is the **uniform symmetric-point limit of the Wenzl/Markov measure on $\mathrm{H}_n(q)$**. It is the structural reason the Borromean h⁴ factor *separates as* $(−3) \cdot (1/4)$.

A short proof:
- Markov normalisation: $\sum_\lambda y_\lambda(q) \cdot d_\lambda = 1$ for every $q$ (including $q = 1$).
- Bar-involution symmetry at $q = 1$: the involution $q \leftrightarrow q^{-1}$ acts trivially at the fixed point $q = 1$, but exchanges Specht modules and their sign twists ($\lambda \leftrightarrow \lambda^T$). Combined with the symmetric-point channel collapse, all irreps land at a common Wenzl value.
- For $\mathrm{H}_n$ embedded in the c-component link-closure picture, the Markov trace prefactor is $[2]_q^{c-1}$ where $c = $ component count; at $q = 1$ this becomes $2^{c-1}$ and (for the standard $c = n$ closure of $\mathbf{1}_n$) gives the uniform $1/2^{n-1}$.

A `proposition` block + `.lean` stub formalising this fact, together with cross-references from `prop:borromean-h4-categorical-derivation` and `prop:borromean-markov-trace-closed-form`, would close the gap.

This proposition is the **right structural home** for the $1/4$ factor in the Borromean derivation.

## Recommended follow-up commits

| # | Artefact | Action |
|---|---|---|
| 1 | `prop:symmetric-point-wenzl-markov-uniform` (`.ts` + `.md` + `.lean`) | **Codify** the uniform-Wenzl-at-q=1 fact; cite from `prop:borromean-h4-categorical-derivation` |
| 2 | `prop:borromean-h4-categorical-derivation` (small patch) | Soften `prop:q-heat-kernel-peter-weyl` cross-reference; replace `rem:symmetric-point-resolution-loss` reference with the new uniform-Wenzl prop |
| 3 | `cor:habiro-expansion-atomic` and `markov_pipeline_cross_validator.py` (optional) | Extend the cross-validator to cover $\beta_{\mathrm{Bor}}$ as a non-atomic benchmark |

## Status

This audit does **not** invalidate any merged content. The Borromean $h^4 = -3/4$ derivation remains correct; the inconsistencies are in the **cross-reference framing**, not the mathematical content. The recommended commits (1) and (2) are small targeted patches.

The cross-algebra h⁴ obstruction — the original GAP-A-4 question — remains untouched and stays open per the T4–T14 retrospective.
