**Proposition (Hecke disjoint-product character via Littlewood-Richardson).**

*Let $T_{\text{constit}}^K = \beta_p^{(1)} \cdot \beta_p^{(2)} \cdots
\beta_n^{(N)} \in H_{3A}(q)$ be the disjoint Hecke product of $Z$
proton braids and $N$ neutron braids on disjoint 3-strand blocks
(the constituent-vacuum baseline of
[`def:ew-interface-knot`](#def:ew-interface-knot)). For each partition
$\lambda \vdash 3A$, the Hecke character factorises via iterated
Littlewood–Richardson:*

$$
  \chi^\lambda(T_{\text{constit}}^K)
   =
  \sum_{\mu_1, \mu_2, \ldots, \mu_A \vdash 3}
    c^{\lambda}_{\mu_1, \mu_2, \ldots, \mu_A}
    \cdot
    \prod_{k=1}^{A} \chi^{\mu_k}\!\bigl(\beta_{x_k}\bigr),
$$

*where $x_k \in \{p, n\}$ is the flavor of the $k$-th nucleon block,
$\chi^{\mu_k}(\beta_{x_k})$ is the H_3 Hecke character of the proton or
neutron braid in the $\mu_k$-irrep, and $c^{\lambda}_{\mu_1, \ldots,
\mu_A}$ is the iterated Littlewood–Richardson coefficient
$\sum_{\nu} c^{\nu}_{\mu_1, \mu_2} \cdots c^{\lambda}_{\nu, \mu_A}$.*

### Proof sketch

Each $\beta_{x_k}$ acts trivially on strands outside the $k$-th block,
so the disjoint product factors through the Hecke subalgebra
$H_3 \times H_3 \times \cdots \times H_3 \hookrightarrow H_{3A}$ as a
direct-summand inclusion. The character of an element in the induced
representation $\mathrm{Ind}_{H_3^A}^{H_{3A}}(\chi^{\mu_1} \boxtimes
\cdots \boxtimes \chi^{\mu_A})$ factorises by Frobenius reciprocity,
and the Littlewood–Richardson rule expresses the induced character
multiplicity into $\chi^\lambda$:

$$
  [\mathrm{Ind}_{H_3^A}^{H_{3A}}(\chi^{\mu_1} \boxtimes \cdots
  \boxtimes \chi^{\mu_A})\!:\!\chi^\lambda]
   =
  c^\lambda_{\mu_1, \ldots, \mu_A}.
$$

Summing over all $(\mu_1, \ldots, \mu_A)$ yields the claimed formula.
At $q = 1$ this is the classical S_n representation-theoretic
identity ([macdonald1995, I.7]); the q-deformation preserves it
because LR coefficients are integer combinatorial invariants
independent of $q$ — the q-deformation enters only through the
$\chi^{\mu_k}(\beta_{x_k})$ Hecke characters at H_3.

### Computational realisation

The iterated LR sum is computable from H_3 chi values via the
precomputed LR tables in
[`folio-assistant/computations/lr_coefficients.py`](https://github.com/litlfred/qou/blob/claude/log-delta-categorical-derivation/folio-assistant/computations/lr_coefficients.py)
(LR_TABLE_3_3_TO_6, 3_6_TO_9, 6_6_TO_12). For each (Z, N) the H_3
chi values for proton and neutron are read from
`chi-proton-h3-at-q0-50dps.witness.json` and the analogous neutron
witness; the LR composition reproduces $\chi^\lambda(T_{\text{constit}}^K)$
at $H_{3A}$ to full mpmath precision.

### Verification

For atoms $K \in \{D, T, {}^3\mathrm{He}\}$, the LR-decomposed
$\chi^\lambda(T_{\text{constit}}^K)$ has been cross-validated against
direct H_{3A}-Wedderburn-weighted character sums from
[`markov_trace_3A(Z, N, include_inter=False)`](https://github.com/litlfred/qou/blob/claude/log-delta-categorical-derivation/folio-assistant/computations/mass_at_3A_proper.py#L314)
— **byte-identical** chi values at all 11 + 30 + 30 partitions
combined (consistent to >40 dps).  For ⁴He at $H_{12}$, cross-validation
uses the cached 24-partition partial witness; all match.

### Significance

This proposition is the structural foundation for SCALING the
depth-stratified binding-energy compute to large atoms without
performing H_{3A}-character sums at high A:

- **At free-side**: $\chi^\lambda(T_{\text{constit}}^K)$ is
  computable in $O(p(3A))$ via LR-decomposition from $H_3$ chi
  values — no $H_{3A}$-seminormal matrices required.
- **At atom-side**: $\chi^\lambda(\beta_K) = \chi^\lambda(T_{\text{constit}}^K
  \cdot \Delta_I^K)$ does NOT factorise via LR (the interface knot
  $\Delta_I^K$ is a non-disjoint Hecke element), and requires
  direct character computation (e.g. via the Rust kernel
  [`pyhecke_native.chi_q_atomic`](https://github.com/litlfred/qou/blob/claude/log-delta-categorical-derivation/tools/pyhecke-native/src/lib.rs)
  cherry-picked from PR #761).

The CONVOLUTION structure $\beta_K = T_{\text{constit}}^K *_q \Delta_I^K$
([`def:ew-interface-knot`](#def:ew-interface-knot)) is preserved
throughout — this is **NOT** a tensor-product reduction; the LR
coefficients encode the Wedderburn-character branching from the
disjoint-Hecke-product structure inside the single H_{3A} algebra.
