**Conjecture (staircase EW-residual).**
*Let $\rho_k = (k, k-1, \ldots, 1)$ be the
[staircase partition](#def:staircase-partition), let
$V_{\rho_k}$ be the Specht module of $H_{n_k}(q)$ at this shape
(realised in
[Hoefsmit seminormal form](#prop:hoefsmit-seminormal-form)),
and let
$\beta_{\mathrm{EW}}\,\bowtie_K^{\mathrm{minimal}} \in H_{n_k}(q)$
be the canonical electroweak braid word.  Then for every
$k \geq 2$, the matrix image*

$$
  \rho_{\rho_k}\!\bigl(\beta_{\mathrm{EW}}\,
                       \bowtie_K^{\mathrm{minimal}}\bigr)
  \;\in\;
  \mathrm{Mat}_{f^{\rho_k} \times f^{\rho_k}}\!\bigl(\mathbb Q(q)\bigr)
$$

*has two nonzero eigenvalues whose pairwise ratio equals*

$$
  q^{1 / h_{\mathrm{corner}}(\rho_k)}
  \;=\; q^{1 / (2k - 1)},
$$

*where the corner-hook identification
$h_{\mathrm{corner}}(\rho_k) = 2k - 1$ is
[Lemma `lem:staircase-corner-hook`](#lem:staircase-corner-hook).*

**Empirical content.**

* $k = 3$ (dim $f^{\rho_3} = 16$): the residual factor $q^{1/5}$
  closes the $2.19\%$ cot $\theta_W$ discrepancy from the bare
  $\max^{+}/\!\operatorname{2nd-max}^{+}$ reading down to
  $0.13\%$ — see
  [`close_321_weinberg_gap.py`](https://github.com/litlfred/qou/blob/main/computations/close_321_weinberg_gap.py),
  witness
  [`close-321-weinberg-gap.witness.json`](https://github.com/litlfred/qou/blob/main/computations/close-321-weinberg-gap.witness.json),
  audit
  [`docs/audits/-close-321-weinberg-gap.md`](https://github.com/litlfred/qou/blob/main/docs/audits/-close-321-weinberg-gap.md).
* $k = 4$ (dim $f^{\rho_4} = 768$): the top eigenvalue is
  *degenerate* (multiplicity $\geq 2$, ratio $1.0$) because every
  Hecke generator has $\det \rho_{\rho_4}(\sigma_i) = +1$ on the
  pure-$\mathrm{SL}$ stratum; the conjecture is verified instead
  via a **pairwise** ratio
  $e[254]/e[188] = 1.01357 \approx q^{1/7} = 1.01502$
  (relative error $0.14\%$) — see
  [`staircase_ew_residual_conjecture.py`](https://github.com/litlfred/qou/blob/main/computations/staircase_ew_residual_conjecture.py),
  audit
  [`docs/audits/-staircase-ew-residual-conjecture.md`](https://github.com/litlfred/qou/blob/main/docs/audits/-staircase-ew-residual-conjecture.md).
* $k = 2$ (dim $f^{\rho_2} = 2$): currently untestable — the
  $\beta_{\mathrm{EW}}$ word at $n = 3$ collapses to a length-$0$
  word under the construction, leaving no matrix multiplication
  to inspect.

**Lean status (per
[`AGENTS.md` §3b-cond](https://github.com/litlfred/qou/blob/main/AGENTS.md)).**
The conjecture is axiomatised as a **hypothesis-only** Lean `class`
`QOU.StaircaseCornerHook.StaircaseEWResidual` (no global instance —
per §3b-cond, supplying one would require a `sorry`; the conjecture
*is* the existence of an instance
`StaircaseEWResidual q (canonicalScale q)`).  The predicate
`StaircaseEWSpectralContent q (scale k) k` is stated explicitly
in terms of
`HoefsmitRepresentation.HasEigenvalueRatio` applied to
`HoefsmitRepresentation.wordImage (betaEWWord (staircaseStrands k))`,
so downstream Lean theorems may take
`[StaircaseEWResidual q scale]` as an instance hypothesis and
remain rigorous-conditional results: their Lean proofs are fully
verified modulo this one named conjectural input.
