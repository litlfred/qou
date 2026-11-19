# Partition-sum Wedderburn decomposition of the Markov trace

$$
  \mathrm{tr}_M^{\mathrm{partition\text{-}sum}}(\mathcal{B}_K)
  \;:=\;
  \sum_{\lambda \vdash 3A} y_\lambda(q) \cdot \mathrm{tr}_{V_\lambda}\!\bigl(\rho_\lambda^q(\mathcal{B}_K)\bigr),
$$

This partition-sum form equals the canonical Markov-axiom reducer $\mathrm{tr}_M(\mathcal{B}_K)$ ([recursive Markov-trace reducer](#prop:markov-trace-recursive-reducer)) to numerical precision at $q = q_0$.

## Significance

The partition-sum form rewrites the Markov trace via the Wedderburn–Artin decomposition $H_n(q) \cong \bigoplus_\lambda M_{f^\lambda}(\mathbb{C})$. The [Hecke branching trace decomposition](hecke-branching-trace-decomposition.md) relies on this decomposition. Downstream consumers (such as binding-energy analysis via $\rho_K$ refinement and force-carrier saturation identities) require a partition-by-partition decomposition of $\mathrm{tr}_M$ that the recursive reducer does not directly expose.

The recursive Markov-axiom ascent and partition-sum Wedderburn formulas must agree. The agreement was previously broken at $q \ne 1$ due to a character convention error. `schur_weyl_symbolic.specht_character_atomic` incorrectly returned the classical Murnaghan–Nakayama character $\chi^\lambda_{\mathrm{MN}}(\pi(\beta))$ at $q = 1$ instead of the $q$-Hecke character $\chi^\lambda_q(\beta)$.

Two layers have to be got right, and each has a natural wrong answer:

1. **Weight layer.** The weight is $y_\lambda(q)$, the Wenzl Schur principal specialisation ([Hecke branching trace decomposition](hecke-branching-trace-decomposition.md)), and what distinguishes it from the naive two-variable Schur function $s_\lambda(q, q^{-1}) / H_q(\lambda)$ is the **normalisation**: $y_\lambda$ divides by $Z = \sum_\mu s_\mu f^\mu$, fixed by $\sum_\lambda y_\lambda f^\lambda = \mathrm{tr}_M(1) = 1$, not by the hook polynomial $H_q(\lambda)$.
2. **Character layer.** The $q = 1$ limit of the Hecke character is not the character required here; the trace must be taken of the $q$-Hecke character $\chi^\lambda_q(\mathcal{B}_K) = \mathrm{tr}\,\rho_\lambda^q(\mathcal{B}_K)$, via Hoefsmit seminormal matrices at $q_0$. The $q$-Murnaghan–Nakayama rule for $\chi^\lambda_q$ is \cite[Thm.~4.1, Cor.~4.2]{jing-liu-2021}, with hook values in closed form \cite[Thm.~2.9]{jing-liu-2021}; those results use $T_i^2 = (q-1)T_i + q$, so their values must be rescaled to the $\sigma_i$ convention here.

### The sum is over at most two rows

Under the production convention $z = q^3/(q^2+1)$ the displayed sum is **not**
over all partitions of $3A$, however it is written. The Wenzl level is fixed by
$Q^{r} = z_W/(1 - Q + z_W)$ with $Q = q^2$, $z_W = qz$, and convention D gives

$$
  1 - q^2 + \frac{q^4}{q^2+1} \;=\; \frac{1}{q^2+1}
  \qquad\Longrightarrow\qquad
  Q^{r} \;=\; q^4 \;=\; Q^2, \qquad r = 2 \ \text{ exactly.}
$$

Wenzl's row cap ($s_{\alpha,r} = 0$ whenever $\ell(\alpha) > r$; Orellana,
*Crelle* **508** (1999) 157–178, p. 5) therefore bites at two rows, so
$y_\lambda(q) = 0$ for every $\lambda$ with three or more rows and
$\mathrm{tr}_M$ factors through the two-row (Temperley–Lieb) quotient:

| | partitions | carry weight under **D** | annihilated |
|---|---|---|---|
| $H_3$ | $(3), (2,1), (1,1,1)$ | $(3), (2,1)$ | $(1,1,1)$ |
| $H_4$ | 5 shapes | $(4), (3,1), (2,2)$ | $(2,1,1), (1,1,1,1)$ |

These are algebraic zeros, not small residuals: the $H_4$ closed forms carry a
literal factor $(A z - q^3)$ with $A = q^2+1$, and $z_D = q^3/A$ is its root
(`h4_markov_weights_closed_form.py`, asserted at run time). Two independent
paths agree exactly — the Wenzl symbolic specialisation $y_\lambda(q)$ and that
closed-form substitution — and both give $w^D_\lambda = s_\lambda(q,q^{-1})/[2]_q^4$
on the surviving shapes with $\sum_\lambda w_\lambda d_\lambda = 1$.

**Convention C did not cap anything.** There $r \approx 2.5995$ — not an integer
— which is why the C-frame weights were non-zero on three-row shapes and why
bullet 1's original contrast read as decisive. That D lands on an *integral*
Wenzl level and C does not is an argument for D from the derivation side.

## Numerical verification

| Atom | $|\mathrm{tr}_M|$ (convention **D**, at $q_0$) |
|---|---:|
| Proton | ${{ qou.computations.atomic-tr-m-mpfr-50dps-proton.results.0.tr_M_at_q0_50dps | precision: 11 }}$ |
| Neutron | ${{ qou.computations.atomic-tr-m-mpfr-50dps-proton.results.1.tr_M_at_q0_50dps | precision: 11 }}$ |
| Deuteron | ${{ qou.computations.atomic-tr-m-mpfr-50dps-proton.results.2.tr_M_at_q0_50dps | precision: 11 }}$ |
| Tritium | ${{ qou.computations.atomic-tr-m-mpfr-50dps-proton.results.3.tr_M_at_q0_50dps | precision: 11 }}$ |
| ${}^3$He | ${{ qou.computations.atomic-tr-m-mpfr-50dps-proton.results.4.tr_M_at_q0_50dps | precision: 11 }}$ |

## Production paths

The values above come from the canonical Hoefsmit + Wenzl bridge under convention **D** at the proton-anchored substrate parameter $q_0$.

Agreement of all three production paths is measured only within convention C. Under convention D the statement this block needs is narrower: the Hoefsmit + Wenzl bridge agrees with the recursive Markov peel wherever both are recorded.

The declaring witness, `q-hecke-seminormal-character-closure-probe`, verifies the
character-closure identity on five **abstract** $B_3$ braids (identity,
$\sigma_1$, the Coxeter element, the figure-8, the full twist) and contains no
nucleon, so it is a structural verifier of the identity — which is
convention-independent — and not the producer of this table.
