# Plancherel usage audit — QOU

**Date:** 2026-05-11
**Branch:** `claude/audit-plancherel-usage-a6DgI`
**PR:** #636
**Trigger:** "audit compute — are Plancherel being used? correctly?"
**Pattern:** P2 (Markov vs Plancherel vs partition-sum normalisation
confusion) per `.claude/skills/local/compute-audit.md`.

**Status (2026-05-11, post-fix commit):** All four findings
addressed in-branch via the **narrow fix**: restrict the
Wenzl-bridge claim to the self-conjugate stratum (where the only
witness verifies it), rename the q-deformed Wedderburn weight
`$\tilde w_\lambda$` distinct from the classical Plancherel
measure `$w_\lambda$`, drop the falsified q-Plancherel identity
claim in Term 7, and rename Python `plancherel_sum*` →
`markov_m3_sum*` to disambiguate the Markov-axiom M3 check from
the Plancherel identity. See *Implemented fixes* at the bottom of
this document.

## Executive summary

**Verdict: NOT correctly. Symbol `w_λ` is overloaded between two
non-equivalent formulas in the same chapter, the canonical Plancherel
boundedness proof does not justify the corollary it is invoked for, a
key Lean theorem is a tautology that begs the question, and the
canonical-weight block's `y_λ = (−1)^κ w_λ` claim is empirically
falsified by an in-repo witness.**

The audit anchor is the three-family contract: Markov $y_\lambda$ →
$|\mathrm{tr}_M|$; Plancherel $w_\lambda$ → tower; quantum dim
$\dim_q(\lambda)$ → Frobenius co-Casimir. The paper's
`wedderburn-weight-canonical.md` collapses these three into a single
canonical $w_\lambda = \dim_q^2/[n]_q!$ with three "named scalings,"
but the Python witnesses and one Python author's own warnings show
they are genuinely distinct at $q \neq 1$.

Four substantive findings (A–D) below. Each cites file:line and a
specific contradiction.

---

## Audit anchor

The framework's three weight families, per user clarification:

| Family | Symbol | Used in (term) | Defining identity |
|--------|--------|----------------|-------------------|
| Markov | $y_\lambda$ | $\lvert\mathrm{tr}_M\rvert$ (term 1) | $\sum_\lambda d_\lambda y_\lambda = 1$ (Markov axiom M3) |
| Plancherel | $w_\lambda$ | tower (term 2) | $\sum_\lambda w_\lambda = 1$ (probability measure) |
| Quantum dim | $\dim_q(\lambda)$ | Frobenius co-Casimir (term 3) | $\sum_\lambda \dim_q^2/[n]_q! \neq 1$ at $q \neq 1$ |

These three agree only at $q = 1$. At $q_0 \approx 1.1097$ they
disagree by factors as large as 2.5× per the witness
[`probe-wedderburn-weight-scheme.witness.json`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/probe-wedderburn-weight-scheme.witness.json).

---

## Finding A — Symbol `w_λ` is overloaded in the same chapter

Two non-equivalent formulas share the same symbol $w_\lambda$ in
`braids-and-knots`. The boundedness proof applies only to one; the
mass-formula uses the other.

| Block | File:line | Formula for $w_\lambda$ | Sums to (per the same chapter) |
|-------|-----------|--------------------------|--------------------------------|
| Plancherel boundedness | [`plancherel-weight-boundedness.md:6`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/content/quantum-observable-universe/braids-and-knots/plancherel-weight-boundedness.md) | $(\dim V_\lambda)^2 / n!$ (classical) | $1$ exactly in $\mathbb{Q}$ |
| Mass-tower coefficient stratification | [`mass-tower-coefficient-stratification.md:61`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/content/quantum-observable-universe/braids-and-knots/mass-tower-coefficient-stratification.md) | $(\dim V_\lambda)^2 / n!$ (classical) | $1$ |
| Plancherel Term 7 formulation | [`plancherel-term-7-formulation.md:8`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/content/quantum-observable-universe/braids-and-knots/plancherel-term-7-formulation.md) | $\dim_q^2 V_\lambda / [n]_q!$ (q-deformed) | $\approx 1.51$ at $q_0$, $n=12$ |
| Unified curvature-rank mass formula | [`unified-curvature-rank-mass-formula.md:22`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/content/quantum-observable-universe/braids-and-knots/unified-curvature-rank-mass-formula.md) | $\dim_q^2 V_\lambda / [n]_q!$ (q-deformed) | claimed $1$, actually $\approx 1.51$ |
| Wedderburn weight canonical | [`wedderburn-weight-canonical.md:10`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/content/quantum-observable-universe/braids-and-knots/wedderburn-weight-canonical.md) | $\dim_q^2(\lambda) / [n]_q!$ (q-deformed) | not stated; called "Plancherel weight" |

`plancherel-weight-boundedness.md:42-44` is explicit that the
q-deformed alternative $\tilde w_\lambda := \dim_q^2/[n]_q!$ is **not**
a probability measure (sums to $\sim 1.51$ at $q_0$). Yet three other
blocks in the same chapter use the symbol $w_\lambda$ (unmarked, no
tilde) for that very $\tilde w_\lambda$.

This is precisely pattern P2.

---

## Finding B — The boundedness corollary doesn't apply to where it's invoked

[`plancherel-weight-boundedness.md:51–69`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/content/quantum-observable-universe/braids-and-knots/plancherel-weight-boundedness.md)
states the **Corollary (convergence of curvature-rank functionals)**
and concludes:

> The total mass functional
> $\mathfrak{m}_{q,\mathcal{K}}(\mathcal{T}) = \sum_k \alpha_k
> \mathfrak{m}^{(k)}_{q,\mathcal{K}}(\mathcal{T})$ is therefore
> absolutely convergent for any bounded $|\alpha_k|$, with no
> super-exponential divergence at large $n$.

But the same chapter's
[`unified-curvature-rank-mass-formula.md:13–22`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/content/quantum-observable-universe/braids-and-knots/unified-curvature-rank-mass-formula.md)
defines $\mathfrak{m}^{(k)}$ using the **q-deformed** $w_\lambda =
\dim_q^2/[n]_q!$. The boundedness proof in
`plancherel-weight-boundedness.md:21–36` uses the classical
$(\dim V_\lambda)^2/n!$. The classical sum-to-1 identity does **not**
transfer to the q-deformed sum, and the same chapter empirically
records a $\sim 51\%$ overshoot at $q_0$, $n=12$.

The corollary therefore proves boundedness for a quantity the paper
does not actually compute, and leaves the q-deformed
$\mathfrak{m}^{(k)}$ unbounded by any cited result.

**Math note.** The "$q$-Plancherel identity" $\sum_\lambda \dim_q^2 V_\lambda = [n]_q!$
cited in [`plancherel-term-7-formulation.md:43`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/content/quantum-observable-universe/braids-and-knots/plancherel-term-7-formulation.md)
is **not** an identity in $H_n(R, q)$ at generic $q$. The Hecke
algebra is a flat deformation, so $\dim_{\mathbb{Q}(q)} H_n(q) = n!$
(not $[n]_q!$) and the Wedderburn-Artin decomposition gives
$\sum_\lambda (\dim V_\lambda)^2 = n!$ with classical dimensions. The
q-deformed identity holds in the **fusion-category** / **TL at root
of unity** setting (where $[n]_q!$ is the categorical dimension), not
in the algebra-theoretic semisimple Hecke setting that the
boundedness proof relies on. Citing it as an identity in
`H_n(R, q)` is what produces the contradiction in Finding A.

---

## Finding C — `wedderburn-weight-canonical.md`'s `y_λ = (−1)^κ w_λ` claim is empirically falsified

[`wedderburn-weight-canonical.md:43`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/content/quantum-observable-universe/braids-and-knots/wedderburn-weight-canonical.md)
asserts:

> **Wenzl-bridge:** $y_\lambda = (-1)^{\kappa_\lambda} w_\lambda$,
> $\kappa_\lambda := \sum_{x \in \lambda} c(x)$
>
> *For self-conjugate partitions ($\kappa_\lambda = 0$), the
> Wenzl-bridge form reduces to $y_\lambda = w_\lambda$.*

In particular $|y_\lambda| = |w_\lambda|$ everywhere.

The in-repo audit witness
[`probe-wedderburn-weight-scheme.witness.json`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/probe-wedderburn-weight-scheme.witness.json)
computes both at $q_0 \approx 1.1097$ and shows them genuinely
distinct:

| $n$ | $\lambda$ | scheme_A (Plancherel $w_\lambda$) | scheme_B (Wenzl $y_\lambda$) | $\|B/A\|$ |
|-----|-----------|-----------------------------------|------------------------------|---------|
| 2 | $(2)$ | 0.4973 | 0.6963 | 1.40 |
| 2 | $(1,1)$ | 0.4973 | 0.3037 | 0.61 |
| 3 | $(3)$ | 0.1634 | 0.4154 | 2.54 |
| 3 | $(2,1)$ | 0.6607 | 0.2809 | 0.43 |
| 3 | $(1^3)$ | 0.1634 | 0.0227 | 0.14 |

These ratios are not signs. $|y_\lambda| \neq |w_\lambda|$.

The probe script's own description
([`probe_wedderburn_weight_scheme.py:1–35`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/probe_wedderburn_weight_scheme.py))
states this is exactly the suspected "hidden fitting" question:

> The codebase uses TWO different Wedderburn weight schemes
> [...] If they disagree on $\chi_\lambda(T_w)$ for non-trivial $T_w$,
> one (or both) is wrong, and the +1.84% $m_p/m_e$ residual may live
> in the WEIGHT CHOICE.

Another Python author independently flags the same conflict in
[`hecke_3a_weights.py:146–162`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/hecke/hecke_3a_weights.py),
explicitly warning:

> This is the **symmetric Plancherel weight** [...], NOT the
> Jones-Markov weight $y_\lambda(q)$ needed for Markov-trace
> assembly at $q \neq 1$. The two coincide only at the classical
> Plancherel point $q = 1$. [...] using this symmetric-Plancherel
> weight in a Markov-trace context [...] for D overstates $\Sigma$ by
> $\sim 3.5×$; for $^4\mathrm{He}$ by $\sim 8×$.

The Python code is more honest than the markdown. The
`wedderburn-weight-canonical.md` "unification" of $y_\lambda$, $w_\lambda$,
$\beta_\lambda$, $C_\lambda$ as scalings of one canonical $w_\lambda$
is the P2 confusion in pure form.

---

## Finding D — "Plancherel completeness" is being used for the Markov-axiom M3 check

Multiple Python scripts label

$$\sum_\lambda d_\lambda \cdot y_\lambda = 1$$

as "Plancherel completeness":

- [`alpha_k_macdonald_closed_form.py:35,135,173,179`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/alpha/alpha_k_macdonald_closed_form.py) — function `plancherel_sum`, assertion `plancherel_completeness_n{n}`. The docstring at line 136 is internally correct ("must equal 1 by Markov-axiom (M3) `tr_M(1)=1`") but the public name is "plancherel".
- [`y_lambda_symbolic_validate.py:13,151,338`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/y_lambda_symbolic_validate.py) — function `test_2_plancherel`.
- [`y_lambda_wenzl_bridge.py:441`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/y_lambda_wenzl_bridge.py) — function `plancherel_sum_numeric`.
- [`codata_reconciliation.py:226`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/codata_reconciliation.py) — comment "Plancherel completeness $\sum d_\lambda y_\lambda = 1$".

This identity is the **Markov axiom (M3)** $\mathrm{tr}_M(1) = 1$
applied to the Wedderburn decomposition $\mathrm{tr}_M = \sum_\lambda
y_\lambda \chi_\lambda$, which sends $1 \mapsto \sum_\lambda y_\lambda
d_\lambda$. It is *not* the Plancherel identity $\sum_\lambda
d_\lambda^2 / n! = 1$, which is a statement about probability measure
$w_\lambda$ on $\hat{S}_n$.

Both sums equal $1$, but for different reasons; conflating them
under one label is what gets the canonical-weight block to claim
$y_\lambda = w_\lambda$ up to sign (Finding C).

---

## Per-site inventory and verdicts

### Content blocks (`.md`)

| Block | Verdict | Note |
|-------|---------|------|
| [`plancherel-weight-boundedness.md`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/content/quantum-observable-universe/braids-and-knots/plancherel-weight-boundedness.md) | **Correct (classical)** | Uses $(\dim V_\lambda)^2/n!$; explicitly warns q-deformed alternative is not a measure. Corollary (lines 51–69) overreaches — see Finding B. |
| [`mass-tower-coefficient-stratification.md`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/content/quantum-observable-universe/braids-and-knots/mass-tower-coefficient-stratification.md) | **Correct (classical)** | Distinguishes $w_\lambda = d_\lambda^2/n!$ from $\tilde w_\lambda = \dim_q^2/[n]_q!$ at lines 61–64. |
| [`plancherel-term-7-formulation.md`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/content/quantum-observable-universe/braids-and-knots/plancherel-term-7-formulation.md) | **Incorrect (q-deformed claimed sum-to-1)** | Uses $\dim_q^2/[n]_q!$, cites a "q-Plancherel identity" that is false in $H_n(q)$ (Finding B). |
| [`unified-curvature-rank-mass-formula.md`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/content/quantum-observable-universe/braids-and-knots/unified-curvature-rank-mass-formula.md) | **Incorrect (q-deformed claimed sum-to-1)** | Same as above. |
| [`wedderburn-weight-canonical.md`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/content/quantum-observable-universe/braids-and-knots/wedderburn-weight-canonical.md) | **Incorrect (collapses three families)** | $y_\lambda = (-1)^\kappa w_\lambda$ falsified by in-repo witness (Finding C). |
| [`partition-sum-proton-residual.md`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/content/quantum-observable-universe/braids-and-knots/partition-sum-proton-residual.md) | **Distinct usage** | "Inverse-Plancherel" $\sum [n]_q! / (\dim_q^2 d_\lambda) \cdot e_\lambda$. Belongs to Frobenius co-Casimir term, not Plancherel-measure family. |

### Lean (`.lean`)

| File | Verdict | Note |
|------|---------|------|
| [`plancherel-weight-boundedness.lean`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/content/quantum-observable-universe/braids-and-knots/plancherel-weight-boundedness.lean) | **Correct, abstract** | `PlancherelDistribution` structure axiomatises `weight_sum_one`; theorems hold under that hypothesis. No `sorry`. Whether the hypothesis applies depends on which concrete $w_\lambda$ is plugged in. |
| [`plancherel-term-7-formulation.lean`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/content/quantum-observable-universe/braids-and-knots/plancherel-term-7-formulation.lean) | **Tautological** | `plancherel_sum_eq_one` (line 58) takes `h_pl : sum = 1` and returns the same. The contested q-Plancherel identity is the hypothesis, never proved. Header comment (line 15) asserts "$w_\lambda = \dim_q^2/[n]_q!$ (bounded; sum=1)" — bound = 1 is the un-proved hypothesis. |
| [`wedderburn-as-noncomm-fourier.lean`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/content/quantum-observable-universe/braids-and-knots/wedderburn-as-noncomm-fourier.lean) | **Conceptual** | Identifies Plancherel measure with non-commutative Fourier weight. No formula commitment. |

The Lean files do **not** prove the disputed q-Plancherel sum
identity; they assume it and proceed. The Lean side is therefore
silent on the conflict between the markdown blocks and the
in-repo numerical witness.

### Python (`.py`) — substantive sites

Active call sites that compute or rely on a Plancherel-labelled weight:

| Script | Formula used | Verdict |
|--------|--------------|---------|
| [`canonical_tower.py:147,490`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/canonical_tower.py) | $w_\lambda = \dim_q^2 / [n]_q!$ | Tower computation — per audit anchor should use classical Plancherel. Uses q-deformed; sums to $\neq 1$. |
| [`canonical_plus_multibrane.py:88,103`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/canonical_plus_multibrane.py) | $w_\lambda = \dim_q^2 / [n]_q!$ | Same issue as above. |
| [`chirality_avg_content.py:121`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/chirality_avg_content.py), [`chirality_avg_content_atomic.py:211,235,269`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/chirality_avg_content_atomic.py), [`chirality_avg_content_chiral.py:179`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/chirality_avg_content_chiral.py) | $\dim_q^2 / [n]_q!$ | Apply q-deformed weight inside an averaging ratio; check whether the ratio is invariant under the renormalisation that fixes $\sum = 1$. If not, the chirality average is biased by $\sim 1.51$ factor at $q_0, n=12$. |
| [`close_321_weinberg_gap.py:255`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/close_321_weinberg_gap.py) | $d_q^2 / [n]_q!$ | Mass-formula evaluation at $(3,2,1)$ stratum; same issue. |
| [`build_term7_s_crystal_4he_chain.py:127–139`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/build_term7_s_crystal_4he_chain.py) | $w_\lambda = f_\lambda^2 / n!$ (**classical**) | **Correct** for Plancherel. Aligns with `plancherel-weight-boundedness.md`. |
| [`hecke_3a_weights.py:145–167`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/hecke/hecke_3a_weights.py) | $d_q^2 / [n]_q!$ | Returns the q-deformed weight but **docstring explicitly warns this is not Markov $y_\lambda$**. Honest. |
| [`hecke_wedderburn.py:144`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/hecke/hecke_wedderburn.py), [`hoefsmit_symbolic.py:134`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/hoefsmit_symbolic.py), [`jet_knot_invariants.py:138`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/jet_knot_invariants.py) | $d_q^2 / [n]_q!$ | Same q-deformed weight; no normalisation guard. |
| [`probe_wedderburn_weight_scheme.py`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/probe_wedderburn_weight_scheme.py) | Scheme A ($w$) vs Scheme B ($y$) | **Audit probe** that explicitly tests the conflict and produces the witness used in Finding C. |
| [`probe_proton_with_wenzl_weights.py`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/probe_proton_with_wenzl_weights.py) | Wenzl $y_\lambda$ | Uses the right Markov family for the proton. |
| [`alpha_k_macdonald_closed_form.py`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/alpha/alpha_k_macdonald_closed_form.py), [`y_lambda_symbolic_validate.py`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/y_lambda_symbolic_validate.py), [`y_lambda_wenzl_bridge.py`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/y_lambda_wenzl_bridge.py) | $\sum y_\lambda d_\lambda = 1$ called "Plancherel completeness" | **Misnamed but numerically valid**. Identity is Markov axiom M3 (Finding D). |
| [`mass_at_3A_proper.py:115,303,405`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/mass_at_3A_proper.py) | `normalized_plancherel_weights_3A` rescales $d_q^2/[n]_q!$ to force $\sum = 1$ | **Marked DEPRECATED** — patch around the non-normalised q-deformed weight. The fact that a renormalisation was needed is itself the witness that q-deformed $\neq$ Plancherel. |
| [`hecke_core.py:2622,2948,3063`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/substrate/hecke_core.py) | "LEGACY Plancherel-weighted form" | Multiple deprecated paths. |
| [`light_isotope_sweep.py:97–177`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/sweeps/light_isotope_sweep.py) | `convention="plancherel"` (LEGACY) vs `"wenzl-schur"` | Explicitly exposes both conventions as a switch — already implements the distinction the canonical-weight block denies. |

---

## Recommendations (ordered)

The work below is **not implemented in this session** — this audit
report is the deliverable. Each recommendation cites a specific
narrative fix; no scripts have been edited.

### R1. (Highest priority.) Resolve symbol collision in `braids-and-knots`

Pick one convention and rewrite the three q-deformed blocks
(`plancherel-term-7-formulation.md`,
`unified-curvature-rank-mass-formula.md`,
`wedderburn-weight-canonical.md`) to use a separate symbol — e.g.
$\tilde w_\lambda$ or $w^{(q)}_\lambda$ — for the q-deformed quantity.
Reserve $w_\lambda$ unsubscripted for the classical Plancherel measure
$(\dim V_\lambda)^2/n!$ as defined in
`plancherel-weight-boundedness.md`.

This is the smallest change that fixes Finding A. It costs nothing
in formal content; it just removes the overload.

### R2. Repair `wedderburn-weight-canonical.md`

The `y_\lambda = (-1)^\kappa w_\lambda` claim (line 43) is empirically
falsified for $n \geq 2$ at $q_0$ by
`probe-wedderburn-weight-scheme.witness.json`. Three options:

1. **Drop the unification.** Restate Markov $y_\lambda$, Plancherel
   $w_\lambda$, and quantum dim $\dim_q$ as distinct families, with
   the relation $y_\lambda \to (-1)^\kappa d_\lambda^2/n!$ holding
   only at $q = 1$.
2. **Find the missing factor.** If a $q$-correction factor turns
   $(-1)^\kappa w_\lambda$ into $y_\lambda$, write it and verify
   against the witness. Best-case this is a $q$-hook ratio; worst
   case the claim is structurally wrong.
3. **Demote to remark.** If the unification is only suggestive,
   move it to a `remark` with `interprets:
   prop:plancherel-weight-boundedness` and a note that the
   identification holds at $q = 1$ only.

Option 1 is consistent with the user's three-family contract and
the in-repo witness. Option 2 is open research.

### R3. Either prove the q-Plancherel sum identity or weaken Term 7's boundedness claim

[`plancherel-term-7-formulation.md:42–46`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/content/quantum-observable-universe/braids-and-knots/plancherel-term-7-formulation.md)
cites "the q-Plancherel identity for the semisimple Hecke algebra,
$\sum_\lambda \dim_q^2 V_\lambda = [n]_q!$" — but this identity is
not in standard references on $H_n(R, q)$ at generic $q$, and the
same chapter's witness records the sum as $\sim 1.51 \cdot [n]_q!$
at $q_0, n=12$. Either provide a proof (with a citation in
`references.ts`) or replace the q-deformed weight with the classical
one whose sum-to-1 is proved in the boundedness proposition.

### R4. Rename "Plancherel completeness" check in the four Python scripts

In `alpha_k_macdonald_closed_form.py`, `y_lambda_symbolic_validate.py`,
`y_lambda_wenzl_bridge.py`, and the `codata_reconciliation.py`
comment, rename the `plancherel_*` symbol that computes
$\sum y_\lambda d_\lambda$ to `markov_axiom_m3_*` (or similar). The
identity is Markov axiom M3, not the Plancherel identity. The current
naming is a footgun that fed Finding C.

### R5. Update the affected Lean theorems

In [`plancherel-term-7-formulation.lean:58`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/content/quantum-observable-universe/braids-and-knots/plancherel-term-7-formulation.lean),
`plancherel_sum_eq_one` is a tautology over its own hypothesis.
Either:

1. Strengthen the theorem to **prove** $\sum_\lambda \dim_q^2 V_\lambda
   / [n]_q! = 1$ in `H_n(R, q)` (R3 must succeed first), or
2. Replace the q-deformed `weight` instance with the classical one
   and prove the classical Plancherel identity (matches the abstract
   `PlancherelDistribution` structure already in
   `plancherel-weight-boundedness.lean`).

Either way the tautology should go.

### R6. Audit downstream callers for ratio invariance

The four chirality scripts ([`chirality_avg_content*.py`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/)) compute
ratios $\sum w_\lambda \chi_\lambda c_\lambda / \sum w_\lambda
\chi_\lambda$. Such ratios are invariant under the renormalisation
$w_\lambda \to w_\lambda / Z$ that fixes the sum-to-1, so they may
be insensitive to the Finding A bug. Verify this explicitly for each
script and label the conclusion in the witness JSON.

For the **non-ratio** sites (`canonical_tower.py`,
`canonical_plus_multibrane.py`, `close_321_weinberg_gap.py`,
`jet_knot_invariants.py`), a re-run with the renormalised weight is
needed to estimate the perturbation to downstream observables.

---

## Cross-references

- Pattern catalogue: [`.claude/skills/local/compute-audit.md`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/.claude/skills/local/compute-audit.md) §P2.
- In-repo audit witness: [`probe-wedderburn-weight-scheme.witness.json`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/probe-wedderburn-weight-scheme.witness.json).
- Honest in-script flag: [`hecke_3a_weights.py:146`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/hecke/hecke_3a_weights.py).
- Convention switch already implemented: [`light_isotope_sweep.py:176`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/sweeps/light_isotope_sweep.py).

---

## Out-of-scope but worth noting

- `partition-sum-proton-residual.md` uses an **inverse-Plancherel**
  element $C_\mathrm{Frob} = \sum_\lambda [n]_q!/(\dim_q^2 d_\lambda)
  \cdot e_\lambda$. This belongs to the **Frobenius co-Casimir** term
  (third weight family) and is not in conflict with Findings A–D. If
  R2 demotes the Wenzl-bridge unification, the Frobenius co-Casimir
  block becomes the canonical home for $\dim_q$-weighted statements.
- The `chirality_avg_content_*` family is the most numerous user of
  q-deformed Plancherel weights inside ratios; R6 may show those
  results are unaffected.
- 58 Python files mention Plancherel; ~12 are substantive call sites
  per the inventory pass. The non-substantive references are
  narrative comments and witness-JSON output and are not
  individually scored.

---

## Implemented fixes (2026-05-11, in-branch, PR #636)

The audit's findings were closed by the **narrow fix** rather than
the larger restructure (R3 / R6 deferred). Specifically:

### Narrative content blocks

- [`wedderburn-weight-canonical.md`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/content/quantum-observable-universe/braids-and-knots/wedderburn-weight-canonical.md):
  - Proposition title relabelled "canonical q-deformed
    Wedderburn-block weight … BW and LP for all $\lambda$;
    Wenzl-bridge on the self-conjugate stratum".
  - Wenzl-bridge identity table row restricted to
    self-conjugate $\lambda$ (`$y_\lambda = w_\lambda$` when
    `$\kappa_\lambda = 0$`). Cited the in-repo witness
    `probe-wedderburn-weight-scheme.witness.json` for the
    non-self-conjugate falsification.
  - "Why $w_\lambda$ is canonical" rewritten to state Markov
    `$\mathrm{tr}_M = \sum y_\lambda \chi_\lambda$` (not
    `$w_\lambda$`) and call out that `$y_\lambda$` and `$w_\lambda$`
    coincide only on the self-conjugate stratum.
  - Section "Wenzl-bridge: $y_\lambda = (-1)^{\kappa_\lambda}
    w_\lambda$" retitled "Wenzl-bridge on the self-conjugate
    stratum: $y_\lambda = w_\lambda$ when $\kappa_\lambda = 0$".
- [`plancherel-term-7-formulation.md`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/content/quantum-observable-universe/braids-and-knots/plancherel-term-7-formulation.md):
  - The q-deformed weight is now written `$\tilde w_\lambda$`
    everywhere; the symbol `$w_\lambda$` is reserved for the
    classical Plancherel measure.
  - The falsified "q-Plancherel identity $\sum \dim_q^2 V_\lambda
    = [n]_q!$" claim is removed from the proof. Replaced with a
    finite-but-not-unit boundedness statement citing
    `prop:plancherel-weight-boundedness` and the witness number
    ($\sim 1.51$ at $q_0, n=12$).
  - A new **Naming note** documents the disambiguation and points
    to the legacy script.
- [`unified-curvature-rank-mass-formula.md`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/content/quantum-observable-universe/braids-and-knots/unified-curvature-rank-mass-formula.md):
  - $\Phi_k$ now uses `$\tilde w_\lambda$`. Classical Plancherel
    measure `$w_\lambda$` cross-referenced.

### Lean siblings

- [`wedderburn-weight-canonical.lean`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/content/quantum-observable-universe/braids-and-knots/wedderburn-weight-canonical.lean):
  - Class `WedderburnWeightCanonical` field `y_eq : ∀ λ, y λ =
    (-1)^κ_λ · w λ` replaced with `y_eq_self_conjugate : ∀ λ,
    kappa λ = 0 → y λ = w λ`. The `y_self_conjugate` theorem now
    discharges to that hypothesis directly. Doc-string rewritten
    to state the BW/LP scalings hold for all $\lambda$ and the
    Wenzl-bridge identity is restricted to the self-conjugate
    stratum.

### TS manifests

- [`wedderburn-weight-canonical.ts`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/content/quantum-observable-universe/braids-and-knots/wedderburn-weight-canonical.ts):
  - Title updated. `computation.script` path corrected from
    `computations/bw_wenzl_shadow_equivalence.py`
    to `…/computations/_deprecated/bw_wenzl_shadow_equivalence.py`
    (the script was already silently moved). `uses[]` now
    includes `prop:plancherel-weight-boundedness`. Tag
    `self-conjugate` added.

### Python scripts (Finding D — naming)

Pure rename plus backward-compat alias:

- [`alpha_k_macdonald_closed_form.py`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/alpha/alpha_k_macdonald_closed_form.py): `plancherel_sum` → `markov_m3_sum`; assertion name `plancherel_completeness_n{n}` → `markov_m3_completeness_n{n}`; module docstring updated.
- [`y_lambda_wenzl_bridge.py`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/y_lambda_wenzl_bridge.py): `plancherel_sum_numeric` → `markov_m3_sum_numeric`.
- [`y_lambda_symbolic_validate.py`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/y_lambda_symbolic_validate.py): `test_2_plancherel` → `test_2_markov_m3`; `DPS_PLANCHEREL` → `DPS_MARKOV_M3`; `TOL_PLANCHEREL` → `TOL_MARKOV_M3`; tolerance-table key `"plancherel"` → `"markov_m3"`; docstring updated.
- [`codata_reconciliation.py`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/codata_reconciliation.py): assertion-name prefix accepts both old (`plancherel_completeness_n*`) and new (`markov_m3_completeness_n*`) during transition.

Backward-compat aliases keep pre-rename callers working until the
next witness regeneration; mark for removal after the next CI run
refreshes the witness JSON.

### Notation register

- [`content/quantum-observable-universe/notation/notation-register.md`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/content/quantum-observable-universe/notation/notation-register.md): three new entries in the Braids-and-Knots register — `$w_\lambda$` (classical Plancherel), `$\tilde w_\lambda$` (q-deformed Wedderburn-block), `$\dim_q(\lambda)$` (quantum dimension). Jones–Markov entry strengthened to flag the three-family distinction.
- [`content/quantum-observable-universe/notation/notation-collisions.md`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/content/quantum-observable-universe/notation/notation-collisions.md): new bullet codifying the three-family rule, the Wenzl-bridge self-conjugate restriction, and the bare-vs-tilde $w$ convention.
- [`CLAUDE.md §7aa`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/CLAUDE.md): summary table mirrors the register; collisions bullet added.

### Recommendations status

| Rec | Status | Note |
|-----|--------|------|
| R1 | done | $w_\lambda$ → $\tilde w_\lambda$ across three blocks |
| R2 | done | Wenzl-bridge restricted to self-conjugate stratum |
| R3 | done | False q-Plancherel identity removed; boundedness restated honestly |
| R4 | done | Python `plancherel_*` → `markov_m3_*` in four scripts |
| R5 | done | Lean class field rewritten; tautological theorem replaced |
| R6 | done | Chirality scripts are ratio-form, renormalisation-invariant (see below) |

### R6 closure — chirality scripts are ratio-invariant

All three chirality scripts —
[`chirality_avg_content.py:142–143`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/chirality_avg_content.py),
[`chirality_avg_content_chiral.py:189–190`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/chirality_avg_content_chiral.py),
[`chirality_avg_content_atomic.py:213–214, 235, 269–273`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/chirality_avg_content_atomic.py)
— compute the chirality average as a **ratio**

$$
  \langle c \rangle_\lambda
  \;=\;
  \frac{\sum_\lambda \tilde w_\lambda \cdot \chi_\lambda(\beta) \cdot c(\lambda)}
       {\sum_\lambda \tilde w_\lambda \cdot \chi_\lambda(\beta)}
$$

with $\tilde w_\lambda$ entering linearly in both numerator and
denominator. Any $\lambda$-independent rescaling $\tilde w_\lambda
\mapsto Z \cdot \tilde w_\lambda$ — including the renormalisation
$Z = 1 / \sum_\lambda \tilde w_\lambda$ that turns $\tilde w$ into
a probability measure — cancels exactly, leaving the ratio
unchanged. Therefore the $w_\lambda \to \tilde w_\lambda$ rename in
these scripts is purely **cosmetic**: zero numerical impact on
their witness values. The committed witnesses
(`chirality-avg-content*.witness.json`) remain valid as-is.

### Remaining follow-ups

- **Witness regeneration** (still partial): `alpha_k_macdonald_closed_form.py`
  witness regenerated with `markov_m3_completeness_n*` assertion
  names (this branch). `y_lambda_symbolic_validate.py` witness *not*
  regenerated — local mpmath produced a 5e-17 precision drift on the
  pre-existing `test_1_cross_q` (unrelated to the rename), which
  would introduce a real test_1 failure if pushed. The in-script
  backward-compat alias (`test_2_plancherel = test_2_markov_m3`)
  keeps existing tooling working. Author can refresh under a
  reproducible environment.
- **Title of Term 7 block** updated in
  [`plancherel-term-7-formulation.ts`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/content/quantum-observable-universe/braids-and-knots/plancherel-term-7-formulation.ts)
  to "q-deformed Wedderburn-weighted log functional"; label
  `prop:plancherel-term-7-formulation` preserved to avoid breaking
  cross-references.

### Post-merge cherry-pick onto PR #637

After PR #636 merges, the q-deformed Wedderburn weight symbol in
two blocks on `claude/display-mass-tables-PAj4i` needs the same
rename. The fixup is a single sed-style pass:

```sed
# tower-binding-energy.md lines 46-105
s/\bw_\\lambda\b/\\tilde w_\\lambda/g
# confined-knot-binding.md line 155
s/\bw_\\lambda\b/\\tilde w_\\lambda/g
```

…with one accompanying narrative note on each block clarifying that
$\tilde w_\lambda := \dim_q^2/[n]_q!$ is the q-deformed Wedderburn
weight (not the classical Plancherel measure
[`prop:plancherel-weight-boundedness`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/content/quantum-observable-universe/braids-and-knots/plancherel-weight-boundedness.md)).

Posted as a coordination comment on PR #637:
[#637 comment 4417561229](https://github.com/litlfred/qou/pull/637#issuecomment-4417561229).
This audit branch does **not** touch #637's files (per the
session-start branch-discipline rule).
