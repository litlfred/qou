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
| Wenzl/Markov $y_\lambda$ | trace-class coefficients of $\mathrm{tr}_M$ | $1/2,\ 1/4,\ 0$ | $\sum_\lambda y_\lambda d_\lambda = 1$ |

The relationship is conceptual (both express q=1 symmetric-point behaviour of partition-indexed measures) but not equational — and the two q=1 value vectors are different non-uniform patterns.

**Fix:** the `prop:borromean-h4-categorical-derivation` markdown narrates "the symmetric-point Wenzl collapse" as if it inherits from `rem:symmetric-point-resolution-loss`. It does not — the resolution-loss remark covers Plancherel. The fix is to **codify the closed-form Wenzl weights** as a new proposition (Finding 3 below) and re-aim the cross-reference there.

## Finding 3 — the closed-form H_3 Wenzl weights are implicit but not codified

> **Correction (review round, this PR).** The first draft of this
> finding claimed the q=1 Wenzl weights were *uniform*
> ($y_\lambda(1) = 1/2^{n-1}$ for all $\lambda$), via a bar-involution
> argument. **That claim was wrong** — caught by review. The
> bar/transpose symmetry $\lambda \leftrightarrow \lambda^T$ is induced
> by the sign-twist automorphism $\sigma \mapsto -q\,\sigma^{-1}$, and
> the Jones-normalised Markov trace is **not invariant** under it (it
> is chiral). The corrected statement below is *stronger*: exact
> closed forms valid at every $q$, not only at $q = 1$.

The correct facts, codified in this PR as `prop:h3-markov-wenzl-weights`:

$$
  \boxed{\;\;
  y_{(3)}(q) = \frac{[4]_q}{[2]_q^{3}},
  \qquad
  y_{(2,1)}(q) = \frac{1}{[2]_q^{2}},
  \qquad
  y_{(1^3)}(q) = 0 \ \text{(identically)},
  \;\;}
$$

evaluating at $q = 1$ to $(1/2,\ 1/4,\ 0)$ — **not uniform**. Proof
structure: (i) the Jones polynomial factors through Temperley–Lieb,
killing the 3-row partition identically — equivalently the algebraic
identity $[2]_q^3 - 2[2]_q = [4]_q$; (ii) Markov normalisation
$\sum y_\lambda d_\lambda = 1$; (iii) the Borromean closed form pins
$y_{(2,1)}(q) = 1/(h^2+4) = 1/[2]_q^2$ uniquely.

Three independent verifications: Schur orthogonality on the q=1
cycle-counting trace $\mathrm{tr}_M(w) = 2^{c(w)-n}$; the exact
$q$-dependent forms reproduce the Borromean closed form to 30 digits;
and the load-bearing $y_{(2,1)}(1) = 1/4$ matches the T18 h⁴
extraction.

**Impact on the Borromean derivation:** the $(-3) \cdot (1/4) = -3/4$
factorisation is **unchanged and strengthened** — the $1/4$ is now the
exact identity $y_{(2,1)}(q) = 1/[2]_q^2$ evaluated at $q = 1$, and
the $(h^2 + 4)$ denominator of the closed form is recognised as
$1/y_{(2,1)}(q)$ exactly. What is retracted is only the claim that the
*other two* weights share the value $1/4$.

## Finding 4 — per-partition h² budget in `prop:borromean-markov-trace-closed-form` uses a different weight convention (open question)

The merged `prop:borromean-markov-trace-closed-form` `.md` assigns
per-partition h² coefficients $(5/128, -20/128, 15/128)$ to
$y_\lambda \cdot \chi^\lambda$ for $\lambda = (3), (2,1), (1^3)$. Under
the closed-form weights of Finding 3, the corresponding h² split is
$(+16/128, -16/128, 0)$ — both sum to zero (consistent with
$h^2(\mathrm{tr}_M) = 0$) but the per-partition attribution differs.
The merged block therefore uses one of the repo's *other* partition-
weight families ($w_\lambda$ or $\tilde w_\lambda$ per the CLAUDE.md
notation-collision register: "three partition-weight families are
distinct at $q \neq 1$ — never conflate"). **Open question** for a
follow-up: identify which family the h²-budget table uses and label it
explicitly in that block.

## Recommended follow-up commits

| # | Artefact | Action | Status |
|---|---|---|---|
| 1 | `prop:h3-markov-wenzl-weights` (`.ts` + `.md` + `.lean`) | **Codify** the closed-form (non-uniform) Wenzl weights | done in this PR |
| 2 | `prop:borromean-h4-categorical-derivation` (small patch) | Correct the "universal q=1 Wenzl weights" paragraph (false uniformity claim is on `main`); soften `prop:q-heat-kernel-peter-weyl` cross-reference; replace `rem:symmetric-point-resolution-loss` reference with `prop:h3-markov-wenzl-weights` | done in this PR |
| 3 | `gap_a4_T18_markov_normalization_probe.py` | Correct the `check_universal_wenzl_at_q_one` framing to the non-uniform weights + regenerate witness | done in this PR |
| 4 | `prop:borromean-markov-trace-closed-form` | Identify + label the weight family used in the h²-budget table (Finding 4) | open follow-up |
| 5 | `cor:habiro-expansion-atomic` / `markov_pipeline_cross_validator.py` (optional) | Extend the cross-validator to cover $\beta_{\mathrm{Bor}}$ as a non-atomic benchmark | open follow-up |

## Status

The Borromean $h^4 = -3/4$ factorisation $(-3) \cdot (1/4)$ remains
correct — the $1/4$ leg is in fact strengthened to an exact all-$q$
identity. What this audit's review round retracted is the *uniformity*
claim ($y_{(3)} = y_{(1^3)} = 1/4$), which was wrong and briefly
present both in this PR's first draft and in one paragraph of the
merged `prop:borromean-h4-categorical-derivation` (corrected by this
PR). Credit: the error was caught by automated review (Gemini) on this
PR and confirmed by three independent computations before correcting.

The cross-algebra h⁴ obstruction — the original GAP-A-4 question — remains untouched and stays open per the T4–T14 retrospective.
