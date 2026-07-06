# Reading-A linking-weight — conditional formula (conjecture)

**Conjecture (conditional on a categorical principle not yet
identified).** *The Borromean linking-weight is*

$$
\mathrm{linkingWeight}_A(q) = \tfrac{5}{2} + (-G)\, h^2
\quad \text{where}\quad h = q - q^{-1}\ \text{and}\ G\ \text{is Catalan's constant}.
$$

## Motivation

At the substrate parameter, the formula $\tfrac{5}{2} + (-G) h^2$
matches the $m_p$-anchored target $m_p^{\mathrm{exp}} / (m_e \cdot
\mathrm{Vol}(\mathcal{B}_3) / \hbar_q^2)$ to high precision in
linking-weight units. (Specific substrate-parameter value, residual,
and equivalent proton-mass precision figures live in the archimedean
witness audit ledger, not here — this block carries only the
categorical conjecture and its algebraic consequences.)

The empirical match is striking — far closer than any known
substrate-derived formula. This file states the conjecture
*conditionally* and proves its algebraic consequences in Lean
without claiming the conjecture itself.

## Status (read this carefully)

This is **NOT a proof** that Reading-A is the actual linking-weight.
Reading-A's $h^2$ coefficient $-G$ directly contradicts the
[**proved Family A theorem**](lambda-scale-substrate-form.md)

$$
\lambda_A(q) := \tfrac{1}{4}\sum_{\lambda \vdash 4} \dim_q V_\lambda
              = \tfrac{5}{2} + \tfrac{3}{4} h^2,
$$

so Reading-A can only be valid if $\mathrm{linkingWeight} \neq
\lambda_A$, i.e. *the Borromean linking-weight is not the $H_4$
Wedderburn sum*. The required new categorical principle has not
yet been identified.

**Three independent audit results foreclose obvious paths:**

1. [****](https://github.com/litlfred/qou/pull/701) —
   falsified the Wedderburn-sum incarnation of $\tfrac{5}{2} - G h^2$
   across 5 structural routes (Wedderburn / Frobenius / Demazure
   / LP-Plancherel / LP-Frobenius).
2. [**Audit**](../../../docs/audits/-yekutieli-bijection-natural-reading-negative.md) —
   the natural half-symmetric projection at $H_4$ gives $+0.5$, not
   $-G$. The Yekutieli per-cell bijection conjecture (Reading-B)
   is also NEGATIVE under the natural reading.
3. [**Path C1 probe**](../../../computations/probes/higher_n_wedderburn_h2_drift_probe.py)
   (this branch) — the higher-N Wedderburn limit
   $(1/N)\sum_{\lambda \vdash N} \dim_q V_\lambda$ has $h^2$
   coefficient growing roughly factorially with $N$ (0.75, 4.0,
   20.0, 92.5, 430.5 at $N = 4, 5, 6, 7, 8$); it diverges away
   from $-G$, not toward it.

## What the Lean file provides

`reading-a-conditional-linking-weight.lean` (sibling) provides:

| Declaration | Kind | Status |
|-------------|------|--------|
| `linkingWeightReadingA` | `def` | algebraic, no claim |
| `ReadingAValidAtH2` | `class` | the SOLE sorry — the conjecture itself |
| `readingA_h2_coefficient` | `theorem` | trivial algebraic (verified) |
| `readingA_eq_familyA_plus_correction` | `theorem` | $\Delta = (-G - 3/4) h^2$ (verified) |
| `readingA_h0_eq_family_a_h0` | `theorem` | $h^0$ unchanged (verified) |
| `m_p_pred_reading_a` | `def` | conditional prediction formula |
| `m_p_pred_reading_a_factored` | `theorem` | factored closed form (verified) |

Per AGENTS.md §3b-cond, the conditional-class pattern lets the
downstream `m_p` prediction be **fully Lean-verified** modulo the
single class-axiomatised assumption `ReadingAValidAtH2`.

## Key Lean-derived identity

The m_p prediction under Reading-A factors cleanly:

$$
m_p^{\mathrm{pred}} = m_e \cdot \mathrm{Vol}(\mathcal{B}_3)
  \cdot \left( \frac{5/2}{\hbar_q^2} + (-G)(q+1)^2 \right)
$$

The second term $(-G)(q+1)^2$ is a *polynomial* in $q$ (no
inverse powers), exposing the Reading-A correction as a clean
polynomial contribution rather than a Laurent expression. The
algebraic identity behind this factorisation is

$$
\frac{h}{\hbar_q} = \frac{q - q^{-1}}{1 - q^{-1}} = q + 1,
$$

proved in `m_p_pred_reading_a_factored`.

## What "proving Reading-A" would require

To upgrade `ReadingAValidAtH2` from a conjecture (`sorry`) to a
theorem (proved), one would need to:

1. **Identify the categorical structure.** Some categorical object
   whose categorically-natural evaluation at $q_0$ on $\mathcal{B}_3$
   yields $-G$ at $h^2$.
2. **Build the bridge to physics.** Show that this object IS the
   linking-weight in the mass formula, not just numerically close.
3. **Formalise in Lean.** Define the structure, prove the
   evaluation, derive the $-G$ coefficient.

The audit
[ Path C](../../../docs/audits/-path-c-categorical-principle-hunt.md)
enumerates 7 candidate categorical principles; **C3 (KLR /
Kashiwara crystal $h^2$ correction)** is the highest-value remaining
direction but is multi-session research.

## What this content block does NOT do

- Does **not** change any production formula (Family A remains the
  proved Lean theorem and the production linking-weight).
- Does **not** propose Reading-A for production adoption — it
  formalises the empirical-match coincidence basin (numerical
  residual recorded in the archimedean witness ledger) as a
  *conditional* Lean statement.
- Does **not** claim the conjecture is true; the `class
  ReadingAValidAtH2` carries the only `sorry` in the chain.

## References

- [Family A theorem](lambda-scale-substrate-form.md) — proved $h^2$ = +3/4
- — Reading-A residual probes
- [Path C audit](../../../docs/audits/-path-c-categorical-principle-hunt.md)
- [Yekutieli per-cell](../../../docs/audits/-yekutieli-percell-conjecture-formalized.md)
- [Yekutieli bijection negative](../../../docs/audits/-yekutieli-bijection-natural-reading-negative.md)
