**Proposition ($Q_\beta$ Form A at $N = 1$, geometric-series lift).**

*Let $q = q_0$, $h = q - q^{-1}$, $\hbar_q = (q-1)/q$, and let
$E_{0,N=0} := m_e / (q(q-1))$ be the single-tick brane-tower energy
scale of
[rem:energy-scale-planck](#rem:energy-scale-planck). Define the
**depth-$N$ geometric-series lift** of $E_0$ as the truncated
geometric series*

$$
  E_{0,N} \;:=\; E_{0,N=0} \cdot \sum_{k=0}^{N} \hbar_q^{2k}
        \;=\; E_{0,N=0} \cdot \frac{1 - \hbar_q^{2(N+1)}}{1 - \hbar_q^{2}}.
$$

*At $N = 1$ the multiplicative factor simplifies algebraically:*

$$
  1 + \hbar_q^2 \;=\; 1 + \frac{(q-1)^2}{q^2} \;=\; \frac{2q^2 - 2q + 1}{q^2},
$$

*and the Form A prediction reads*

$$
  \boxed{\;
  Q_\beta^{A, N = 1}(q)
  \;=\;
  \frac{m_e \cdot (q + 1) \cdot \lvert q^2 - 2q - 1 \rvert
       \cdot (2q^2 - 2q + 1)}
      {2\,q^5}.\;}
$$

*This is the closed symbolic form for Form A at depth-1 brane-tower
truncation under the geometric-series lift.*

## Numerical evaluation (50 dps)

See [Table](#tbl:q-beta-form-a-n1-symbolic-table-data).

## Negative finding: the geometric-series lift is the wrong lift

The depth-$N$ geometric series above is the **simplest possible
algebraic lift** of $E_0$: it sums the q-Pochhammer expansion of
$1/(1 - \hbar_q^2)$ truncated at depth $N+1$. Numerically it
**overshoots the per-braid-mass-tower ceiling by $\sim 120\times$**
($1.15\%$ observed vs $97$ ppm ceiling) and **makes the residual
worse than $N=0$** by a factor of $\sim 6.9$ in absolute terms.

This is consistent with prior handoff documentation: five
candidate naive $N=1$ lifts all overshot by factors of
$42$–$134\times$. The geometric-series lift is
qualitatively the same failure mode: a uniform multiplicative
correction to $E_0$ that doesn't respect the per-partition
Wedderburn-block structure of the brane-tower truncation.

The correct $N \geq 1$ lift formula remains the open structural
piece flagged by
[conj:brane-tower-z-habiro](#conj:brane-tower-z-habiro): per
[rem:per-partition-k-lambda-rule](#rem:per-partition-k-lambda-rule),
the per-partition $k_\lambda$ rule (non-uniform Wedderburn-block
truncation) is the surviving open form. The simple geometric
series tried here is, in $k_\lambda$ language, the **uniform-$k$
lift with $k = N + 1$ on every partition** — exactly the form
PR #638 refuted across multi-strand binding.

## What this rules in / out

**Rules out**: any uniform-$k$ algebraic lift of $E_0$ (geometric,
arithmetic, or other) as the correct $N \geq 1$ closure.

**Rules in**: the symbolic closed form itself is the **correct
shape** for a uniform-$k$ lift; what's wrong is the uniform-$k$
assumption, not the algebraic derivation. The same Taylor structure
applies under non-uniform $k_\lambda$, with the multiplicative
factor $(1 + \hbar_q^2)$ replaced by a partition-dependent
correction $\bigl(1 + \hbar_q^{2(k_\lambda)}\bigr)$ summed against
the Wedderburn weights $y_\lambda(q_0)$.

## Provenance

Witness: [`q_beta_form_a_n1_extension.py`](https://github.com/litlfred/qou/blob/main/computations/q_beta_form_a_n1_extension.py)
$\to$ [`q-beta-form-a-n1-extension.witness.json`](https://github.com/litlfred/qou/blob/main/computations/q-beta-form-a-n1-extension.witness.json)
on PR #639. Three assertions pass:
1. Geometric-$N{=}1$ lift overshoots the per-braid ceiling.
2. The factor identity $1 + \hbar_q^2 = (2q^2 - 2q + 1)/q^2$ holds
   exactly at 50 dps.
3. Geometric-$N{=}1$ residual is worse than $N=0$ in absolute
   value.

Substrate-only (CAL-1 $m_e$ + CAL-2 $q_0$); CAL-3 $Q_\beta$ used
as comparator only (Class C per
`docs/audits/2026-05-11-three-calibration-discipline-violations.md`
on PR #640).
