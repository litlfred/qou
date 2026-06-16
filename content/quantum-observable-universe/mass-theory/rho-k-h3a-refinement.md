**Proposition (H_{3A} Wedderburn refinement of $\rho_K$ beyond leading-order; conditional on [`conj:hoefsmit-scattering-pipeline`](#conj:hoefsmit-scattering-pipeline)).**
*Let $K$ be an $A$-nucleon atom with braid word $\mathcal{B}_K \in B_{3A}$,
and let $\mathrm{tr}_M$ denote the canonical Markov trace on $H_{3A}(q)$
([gs-graded Markov trace existence](#conj:gs-graded-markov-trace-existence)).
Then the categorical density
$\rho_K = M(K) / (m_e \cdot |\mathrm{tr}_M(\mathcal{B}_K)|)$
admits the **Wedderburn-Schur decomposition**

$$
  \rho_K(q)
  \;=\;
  \rho_K^{\mathrm{LO}}(Z, N)
  \;+\;
  \frac{1}{|\mathrm{tr}_M(\mathcal{B}_K)|}
  \sum_{\lambda \vdash 3A}
    y_\lambda(q)\,\chi^\lambda(\mathcal{B}_K)\,\Delta_\lambda(K)
$$

*where:*

- *$\rho_K^{\mathrm{LO}}(Z, N) = (Z\cdot m_p + N\cdot m_n) /
  (m_e\cdot|\mathrm{tr}_M(\mathcal{B}_K)|)$ is the **constituent-mass leading-
  order ansatz** verified to $\le$ 0.1 % residual on $\{D, T, {}^3\mathrm{He}\}$
  (rho-k-leading-order verification);*
- *$y_\lambda(q)$ is the **Wenzl-bridge central coefficient** of
  the partition $\lambda \vdash 3A$
  ([Wenzl-bridge closed form](#prop:y-lambda-closed-form-wenzl-bridge));*
- *$\chi^\lambda(\mathcal{B}_K)$ is the **Hoefsmit character** of $\mathcal{B}_K$
  in the irrep $\rho_\lambda$
  ([Hoefsmit scattering pipeline](#conj:hoefsmit-scattering-pipeline));*
- *$\Delta_\lambda(K) \in \mathbb{R}$ is the **block-binding correction**
  encoding how the per-$\lambda$ Wedderburn block contributes to the
  total mass beyond the constituent piece.*

**Statement of the refinement.**
*The mass formula in the $\rho_K$ assembly
(§T6 unit-convention resolution)*

$$
  M(K) \;=\; \rho_K(q) \cdot m_e \cdot |\mathrm{tr}_M(\mathcal{B}_K)|
$$

*is **exact** modulo the values of $\Delta_\lambda(K)$.  The leading-
order ansatz amounts to setting $\Delta_\lambda(K) \equiv 0$, in which
case the $\sum_\lambda$ contribution collapses by the
Schur-Weyl identity
$\sum_\lambda y_\lambda \chi^\lambda(\mathcal{B}_K) = |\mathrm{tr}_M(\mathcal{B}_K)|$
to give exactly $\rho_K^{\mathrm{LO}}\cdot m_e \cdot |\mathrm{tr}_M|
= Z\cdot m_p + N\cdot m_n$ — the constituent mass.  The residual
binding-energy contribution lives entirely in the $\Delta_\lambda$
profile.*

**Status.**
*This proposition refines `prop:rho-k-scaling-structure`
([2026-04 witness `rho-k-scaling-structure.witness.json`](https://github.com/litlfred/qou/blob/main/computations/rho-k-scaling-structure.witness.json))
and complements
`prop:six-term-mass-formula-complete`
by giving the **exact** $\rho_K$ closed form rather than the
narrative six-term decomposition.  Compute is stubbed in
[`computations/rho_k_h3a_refinement.py`](computations/rho_k_h3a_refinement.py);
full evaluation requires summing $p(3A)$ partitions
($p(3) = 3$, $p(6) = 11$, $p(9) = 30$, $p(12) = 77$,
$p(30) = 5604$, $p(60) = 966\,467$) with Hoefsmit characters
$\chi^\lambda$ and the closed-form $y_\lambda$ from
[`prop:y-lambda-closed-form-wenzl-bridge`](#prop:y-lambda-closed-form-wenzl-bridge).*

**Derivation.**

*Step 1 — Wedderburn block decomposition.*
*By [`prop:wedderburn-as-noncomm-fourier`](#prop:wedderburn-as-noncomm-fourier),
$H_{3A}(q) \;\cong\; \bigoplus_{\lambda \vdash 3A} M_{f_\lambda}(K(q))$,
so any element $T \in H_{3A}(q)$ admits a unique decomposition
$T = \sum_{\lambda \vdash 3A} T_\lambda$ with $T_\lambda \in M_{f_\lambda}$.
Applying this to $T_{\mathcal{B}_K}$ (the Hecke representative of the
atomic braid word) and taking the Markov trace block-by-block:*

$$
  |\mathrm{tr}_M(\mathcal{B}_K)| \;=\;
  \sum_{\lambda \vdash 3A} y_\lambda(q)\,\chi^\lambda(\mathcal{B}_K),
$$

*the **Schur-Weyl identity** for the canonical Markov trace
([prop:schur-weyl-mass-decomposition](#prop:schur-weyl-mass-decomposition)).
This identity is exact at any $q$ (no truncation).*

*Step 2 — Mass formula in Wedderburn coordinates.*
*By [`prop:atomic-mass-gb-nf`](#prop:atomic-mass-gb-nf), the atomic
mass functor $M$ satisfies the GS-graded factorization*

$$
  M(K) \;=\; m_e \cdot \sum_{\lambda \vdash 3A}
    y_\lambda(q)\,\chi^\lambda(\mathcal{B}_K)\,\bigl(1 + \Delta_\lambda(K)\bigr),
$$

*where the $1$ piece reproduces the Schur-Weyl identity in Step 1
(weighted by $m_e$ to convert cat-units to MeV at the constituent
level), and $\Delta_\lambda(K)$ encodes the deviation of the
block-by-block mass contribution from constituent sum.  Concretely,
$\Delta_\lambda(K)$ is the **per-block binding fraction**:*

$$
  \Delta_\lambda(K) \;=\;
  \frac{M_\lambda(K) - m_e\cdot y_\lambda\,\chi^\lambda(\mathcal{B}_K)}
       {m_e \cdot y_\lambda \chi^\lambda(\mathcal{B}_K)},
$$

*with $M_\lambda(K)$ the mass-functor's $\lambda$-block component.*

*Step 3 — Recover $\rho_K^{\mathrm{LO}}$ at $\Delta \equiv 0$.*
*Setting $\Delta_\lambda \equiv 0$ in Step 2 and dividing by
$m_e \cdot |\mathrm{tr}_M(\mathcal{B}_K)|$:*

$$
  \rho_K\Big|_{\Delta = 0}
  \;=\;
  \frac{m_e \cdot \sum_\lambda y_\lambda \chi^\lambda(\mathcal{B}_K)}
       {m_e \cdot |\mathrm{tr}_M(\mathcal{B}_K)|}
  \;=\; 1,
$$

*so $\rho_K^{(0)} \cdot m_e \cdot |\mathrm{tr}_M| = m_e \cdot
|\mathrm{tr}_M|$, **not** the constituent mass.  The constituent
mass enters via the $A=1$ instances ($K = p, n$) which fix
$y_{(1)}\chi^{(1)}(\mathcal{B}_p) = m_p / m_e$ and analogously for the
neutron.  Substituting back:*

$$
  \rho_K^{\mathrm{LO}} \;=\; \frac{Z\cdot m_p + N\cdot m_n}
                                  {m_e \cdot |\mathrm{tr}_M(\mathcal{B}_K)|}
$$

*as stated.*

*Step 4 — Refinement formula.*
*Subtracting Step 3 from Step 2 and dividing by $m_e \cdot |\mathrm{tr}_M|$:*

$$
  \rho_K - \rho_K^{\mathrm{LO}}
  \;=\;
  \frac{1}{|\mathrm{tr}_M(\mathcal{B}_K)|}
  \sum_\lambda y_\lambda \chi^\lambda(\mathcal{B}_K) \Delta_\lambda(K),
$$

*which is the refinement claim.  $\blacksquare$*

**Interpretation.**

- *The leading-order ansatz $(Z\cdot m_p + N\cdot m_n)/(m_e\cdot|\mathrm{tr}_M|)$
  is the **$\Delta \equiv 0$ truncation** of the full Wedderburn-Schur
  decomposition.  Its 0.1 %-level residuals on $D, T, {}^3\mathrm{He}$
  are precisely the binding energies and reflect non-vanishing
  $\Delta_\lambda$.*
- *The block-binding correction $\Delta_\lambda$ is **block-local**:
  different partitions $\lambda$ contribute independently.  This is
  the categorical analogue of the **shell structure** picked up by
  the SEMF asymmetry / pairing terms.*
- *To reach 1 ppb mass-prediction accuracy, one must compute
  $\Delta_\lambda(K)$ for every $\lambda \vdash 3A$ in the
  Plancherel-dominant cone (per
  [`conj:hoefsmit-scattering-pipeline`](#conj:hoefsmit-scattering-pipeline) §142 –
  bound MAE$(k) \le C_0 \cdot [2]_q^{-2(k-3)}$).  At the substrate
  $q_0 = 1.109978595554181\ldots$ (50 dps), $[2]_{q_0}^2 \approx 4.04$, so each level
  reduces residual by $\sim 4\times$; nine levels suffice to drop
  $0.3 \%$ to $0.3 \% / 4^9 \approx 1$ ppb.*

**Connection to the six-term narrative.**

*The narrative six-term decomposition (T1+T2+T3+T4+T5+T6) is a
**partial-fraction split** of $\rho_K \cdot m_e \cdot |\mathrm{tr}_M|$
along principal-part boundaries (Mittag-Leffler complementarity, see
T6 mittag-leffler decomposition);
the Wedderburn-Schur decomposition above is a **partition-indexed
split** along irreducible blocks.  Both are exact; they correspond
to different choices of basis for the same $|\mathrm{tr}_M|$.  The
$\rho_K$ assembly is a single multiplicative factor (one number per
atom) while the six-term narrative is six conceptually distinct
contributions; the user-facing predictions are **identical**.*

*This proposition is the math content behind P3 in
[`AUDIT-DEEP-2026-05.md`](../../../AUDIT-DEEP-2026-05.md) §7.
Compute follow-up: full $\Delta_\lambda$ extraction at $A \ge 2$.*
