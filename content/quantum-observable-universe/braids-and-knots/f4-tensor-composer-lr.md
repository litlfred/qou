## Statement

Let $\beta_1, \beta_2$ be braid words on $n_1$ and $n_2$ strands
respectively, with $T_{\beta_i} \in H_{n_i}(q)$ their images in the
Iwahori–Hecke algebra.  Let $\beta_1 \otimes \beta_2$ denote the
braid on $n = n_1 + n_2$ strands obtained by placing $\beta_1$ on
strands $\{1, \ldots, n_1\}$ and $\beta_2$ on strands $\{n_1 + 1,
\ldots, n\}$ (i.e., $\sigma_i$ in $\beta_2$ becomes
$\sigma_{i + n_1}$ in $\beta_1 \otimes \beta_2$).

Then for every partition $\lambda \vdash n$:

$$
  \chi_\lambda(T_{\beta_1 \otimes \beta_2}; q)
  \;=\;
  \sum_{\mu \vdash n_1, \;\nu \vdash n_2}
    c^\lambda_{\mu \nu} \cdot
    \chi_\mu(T_{\beta_1}; q) \cdot \chi_\nu(T_{\beta_2}; q),
$$

where $c^\lambda_{\mu\nu}$ is the Littlewood–Richardson coefficient
of $\lambda$ with respect to the pair $(\mu, \nu)$ — equivalently,
the multiplicity of the Specht module $S^\lambda$ in
$\operatorname{Ind}_{S_{n_1} \times S_{n_2}}^{S_n} (S^\mu \boxtimes S^\nu)$.

For a $k$-fold factorization $\beta = \beta_1 \otimes \cdots \otimes \beta_k$
the formula iterates by associativity of the LR product:

$$
  \chi_\lambda(T_\beta; q)
  \;=\;
  \sum_{\mu_1 \vdash n_1, \ldots, \mu_k \vdash n_k}
    c^\lambda_{\mu_1, \mu_2, \ldots, \mu_k} \cdot
    \prod_{i=1}^{k} \chi_{\mu_i}(T_{\beta_i}; q).
$$

## Proof sketch

The induced representation
$\operatorname{Ind}_{S_{n_1} \times S_{n_2}}^{S_n} (S^\mu \boxtimes S^\nu)$
decomposes into irreducible Specht modules with multiplicities
$c^\lambda_{\mu\nu}$ by the Littlewood–Richardson rule (Stanley EC2
§7.18).  The Hecke algebra $H_n(q)$ is a $q$-deformation of the
group algebra $\mathbb{C}[S_n]$, with the same simple modules
indexed by partitions and the same induction structure for
$H_{n_1} \otimes H_{n_2} \hookrightarrow H_n$.  At any specialization
$q$ the character of $T_{\beta_1 \otimes \beta_2}$ on $S^\lambda$
factors through this decomposition, giving the stated formula.

The associative iteration for $k > 2$ follows from
$c^\lambda_{\mu_1, \mu_2, \mu_3, \ldots} = \sum_\sigma
c^\lambda_{\sigma, \mu_3, \ldots} c^\sigma_{\mu_1 \mu_2}$ (a
specialization of the comultiplication in the Hopf algebra of
symmetric functions).

## Computational realization

Implemented in `folio-assistant/computations/knot_operation_cache.py`
as `chi_via_factorization(lam, factorization, q)`.  Per-factor
characters $\chi_{\mu_i}(T_{\beta_i}; q)$ are evaluated via the
Hoefsmit seminormal kernel
[`pyhecke_native.chi_lambda_braid`](https://github.com/litlfred/qou/blob/claude/f4-sdp-mpfr-content/tools/pyhecke-native/src/lib.rs);
LR coefficients $c^\lambda_{\mu\nu}$ via
[`pyhecke_native.lr_coefficient`](https://github.com/litlfred/qou/blob/claude/f4-sdp-mpfr-content/tools/hecke-engine/src/littlewood_richardson.rs).
The composition is a left-fold maintaining the partial vector
$V_j[\tau] = \chi_\tau(T_{\beta_1 \otimes \cdots \otimes \beta_j})$
over partitions $\tau$ of $n_1 + \cdots + n_j$.

Three precision tiers are exposed:

- `chi_via_factorization(lam, factorization, q)` — `f64`, fastest;
- `chi_via_factorization_mpfr(lam, factorization, q_str, dps=50)` —
  arbitrary-precision MPFR via `chi_lambdas_braid_mpfr`;
- `chi_via_factorization_symbolic(lam, factorization)` — symbolic
  in $q$ (sympy expression), via the Geck–Pfeiffer Hecke-basis
  expansion `chi_q_via_gp` per factor.

Tensor-product factorizations are detected automatically by
[`discover_factorization`](#prop:f4-wedderburn-sdp-shadow-price)
when consecutive generator indices act on disjoint strand subsets;
entangled braids fall through to the shadow-price path.

## Verification

Cross-validated against direct Hoefsmit evaluation on the shifted
concatenation $\beta_1 \cdot \mathrm{shift}(\beta_2, n_1)$ across
46 cases at $q = q_0 \approx 1.10998$ (n = 4, 5, 6, 8 with
symmetric, asymmetric, and three-way factorizations; positive and
inverse generators in per-factor words).  Maximum diff: $4.4 \times 10^{-16}$
(`f64`) and $5 \times 10^{-50}$ (MPFR at 50 dps).  Symbolic variant
matches `f64` at $q = q_0$ and collapses to classical Murnaghan–Nakayama
at $q = 1$.
