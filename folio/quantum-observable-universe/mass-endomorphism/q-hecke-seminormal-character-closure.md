# Partition-sum Wedderburn decomposition of the Markov trace

$$
  \mathrm{tr}_M^{\mathrm{partition\text{-}sum}}(\mathcal{B}_K)
  \;:=\;
  \sum_{\lambda \vdash 3A} y_\lambda(q) \cdot \mathrm{tr}_{V_\lambda}\!\bigl(\rho_\lambda^q(\mathcal{B}_K)\bigr),
$$

This partition-sum form equals the canonical Markov-axiom reducer $\mathrm{tr}_M(\mathcal{B}_K)$ ([Existence of a recursive symbolic Markov-trace reducer for $H_n(q)$ with disjoint-product property](#prop:markov-trace-recursive-reducer)) to numerical precision at $q = q_0$.

## Significance

The partition-sum form rewrites the Markov trace via the Wedderburn–Artin decomposition $H_n(q) \cong \bigoplus_\lambda M_{f^\lambda}(\mathbb{C})$. The [Hecke branching trace decomposition](#prop:hecke-branching-trace-decomposition) relies on this decomposition. Downstream consumers (such as binding-energy analysis via $\rho_K$ refinement and force-carrier saturation identities) require a partition-by-partition decomposition of $\mathrm{tr}_M$ that the recursive reducer does not directly expose.

For the recursive Markov-axiom ascent and the partition-sum Wedderburn formula to agree away from $q = 1$, each summand must evaluate the $q$-deformed Hecke character $\chi^\lambda_q(\beta)$ rather than the classical $q = 1$ Murnaghan–Nakayama character $\chi^\lambda_{\mathrm{MN}}(\pi(\beta))$.

Two layers have to be got right, and each has a natural wrong answer:

1. **Weight layer.** The weight is $y_\lambda(q)$, the Wenzl Schur principal specialisation ([Hecke branching trace decomposition](#prop:hecke-branching-trace-decomposition)), and what distinguishes it from the naive two-variable Schur function $s_\lambda(q, q^{-1}) / H_q(\lambda)$ is the **normalisation**: $y_\lambda$ divides by $Z = \sum_\mu s_\mu f^\mu$, fixed by $\sum_\lambda y_\lambda f^\lambda = \mathrm{tr}_M(1) = 1$, not by the hook polynomial $H_q(\lambda)$.
2. **Character layer.** The $q = 1$ limit of the Hecke character is not the character required here; the trace must be taken of the $q$-Hecke character $\chi^\lambda_q(\mathcal{B}_K) = \mathrm{tr}\,\rho_\lambda^q(\mathcal{B}_K)$, via Hoefsmit seminormal matrices at $q_0$. The $q$-Murnaghan–Nakayama rule for $\chi^\lambda_q$ is \cite[Thm. 4.1, Cor. 4.2]{jing-liu-2021}, with hook values in closed form \cite[Thm. 2.9]{jing-liu-2021}; those results use $T_i^2 = (q-1)T_i + q$, so their values must be rescaled to the $\sigma_i$ convention here.

### The sum is over at most two rows

At the Markov parameter $z = q^3/(q^2+1)$ the displayed sum restricts to
partitions of at most two rows. The Wenzl level is fixed by
$Q^{r} = z_W/(1 - Q + z_W)$ with $Q = q^2$, $z_W = qz$, which gives

$$
  1 - q^2 + \frac{q^4}{q^2+1} \;=\; \frac{1}{q^2+1}
  \qquad\Longrightarrow\qquad
  Q^{r} \;=\; q^4 \;=\; Q^2, \qquad r = 2 \ \text{ exactly.}
$$

Wenzl's row cap ($s_{\alpha,r} = 0$ whenever $\ell(\alpha) > r$; Orellana,
*Crelle* **508** (1999) 157–178, p. 5) therefore bites at two rows, so
$y_\lambda(q) = 0$ for every $\lambda$ with three or more rows and
$\mathrm{tr}_M$ factors through the two-row (Temperley–Lieb) quotient:

| | partitions | carry nonzero weight at $z = q^3/(q^2+1)$ | annihilated |
|---|---|---|---|
| $H_3$ | $(3), (2,1), (1,1,1)$ | $(3), (2,1)$ | $(1,1,1)$ |
| $H_4$ | 5 shapes | $(4), (3,1), (2,2)$ | $(2,1,1), (1,1,1,1)$ |

These are algebraic zeros, not small residuals: the $H_4$ closed forms carry a
literal factor $(A z - q^3)$ with $A = q^2+1$, and $z = q^3/A$ is its root
(checked by exact symbolic computation). Two independent
paths agree — the Wenzl specialisation and that
closed-form substitution — and both give $y_\lambda = s_\lambda(q,q^{-1})/[2]_q^4$
on the surviving shapes with $\sum_\lambda y_\lambda d_\lambda = 1$.

## Numerical verification

| Atom | $|\mathrm{tr}_M|$ ($z = q^3/(q^2+1)$, proton-anchored $q_0$) |
|---|---:|
| Proton | ${{ qou.computations.atomic-tr-m-mpfr-50dps-proton.results.0.tr_M_at_q0_50dps | precision: 11 }}$ |
| Neutron | ${{ qou.computations.atomic-tr-m-mpfr-50dps-proton.results.1.tr_M_at_q0_50dps | precision: 11 }}$ |
| Deuteron | ${{ qou.computations.atomic-tr-m-mpfr-50dps-proton.results.2.tr_M_at_q0_50dps | precision: 11 }}$ |
| Tritium | ${{ qou.computations.atomic-tr-m-mpfr-50dps-proton.results.3.tr_M_at_q0_50dps | precision: 11 }}$ |
| ${}^3$He | ${{ qou.computations.atomic-tr-m-mpfr-50dps-proton.results.4.tr_M_at_q0_50dps | precision: 11 }}$ |

## Evaluation paths

The values above come from the Hoefsmit seminormal + Wenzl bridge at $z = q^3/(q^2+1)$ and the proton-anchored $q_0$, where the Hoefsmit + Wenzl partition sum agrees with the recursive Markov peel across all recorded isotopes. Independently, the character-closure identity holds across abstract $B_3$ braids (identity, $\sigma_1$, the Coxeter element, the figure-eight word, and the full twist) for arbitrary $z$.
