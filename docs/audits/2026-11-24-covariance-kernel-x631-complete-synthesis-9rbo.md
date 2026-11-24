# Covariance-Kernel Epic (`qou-x631`) — Complete Cold-Reader Synthesis (`qou-9rbo`)

**Date:** 2026-11-24 · **Branch:** `claude/editorial-audit-0sq1-20d3-9rbo-73y1-20261124` · **Closes:** `qou-9rbo` (updating and completing [`2026-07-25-covariance-kernel-epic-synthesis.md`](2026-07-25-covariance-kernel-epic-synthesis.md) across all July–November 2026 developments through `PR #9320`) · **Epic:** `qou-x631` · **Cluster:** `qou-x631`, `qou-k5r5`, `qou-o6ov`, `qou-za3q`, `qou-omr7`.

This document is a self-contained handoff written for a reader with zero context from prior sessions. Every bean identifier, Lean module, witness, and algebraic symbol is defined on first use.

---

## 1. Exact Mathematical Statement and Downstream Role (`GAP-A-3`)

For an integer $k \ge 3$ and a Young diagram (integer partition) $\lambda \vdash k$, write:
- $f^\lambda = \dim V^\lambda = \frac{k!}{\prod_{\square \in \lambda} h(\square)}$ for the standard Young tableau (SYT) hook-length dimension, where $h(\square)$ is the hook length of cell $\square = (i, j) \in \lambda$;
- $c(\square) = j - i$ for the cell content, and $C_2(\lambda) := \sum_{\square \in \lambda} c(\square)^2$ for the total squared content;
- $\omega_3(\lambda) := C_2(\lambda) - \binom{k}{2} = \sum_{\square \in \lambda} h(\square)^2 - k^2 - \binom{k}{2}$ for the centred content-spread observable;
- $\mathbb{P}_{\mathrm{Planch}}(\lambda) := \frac{(f^\lambda)^2}{k!}$ for the Plancherel probability measure on $\{\lambda \vdash k\}$.

By the Frobenius–Jucys–Murphy identity $\sum_{\square \in \lambda} c(\square)^2 - \binom{k}{2} = \frac{k(k-1)(k-2)\,\chi^\lambda((123))}{3\,f^\lambda}$ and the Kerov–Olshanski free-cumulant relation $\widehat{\Sigma}_3(\lambda) = R_4(\lambda) + R_2(\lambda) = 3\,\omega_3(\lambda)$ (with $R_2(\lambda) = k$ deterministic at level $k$, so $R_4(\lambda) = 3\,\omega_3(\lambda) - k$), the following four inequalities are **algebraically equivalent**:

$$
\begin{aligned}
  \mathrm{cov}(k) := \sum_{\lambda \vdash k} (f^\lambda)^3\,\omega_3(\lambda) \le 0
  &\iff T_3(k) := \sum_{\lambda \vdash k} (f^\lambda)^2\,\chi^\lambda((123)) \le 0 \\
  &\iff \mathrm{Cov}_{\mathrm{Planch}}\bigl(f^\lambda,\, \omega_3(\lambda)\bigr) \le 0 \\
  &\iff \mathrm{Cov}_{\mathrm{Planch}}\bigl(f^\lambda,\, R_4(\lambda)\bigr) \le 0.
\end{aligned}
$$

Here $\mathbb{E}_{\mathrm{Planch}}[\omega_3] = 0$ identically for all $k \ge 0$ (proved unconditionally in Lean in `QOU.BraidsAndKnots.SecondMomentKernelVanishes.tiltedMean_zero`).

### Why this inequality is load-bearing
1. **Formal reduction chain (sorry-free in Lean):**
   - `folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/DeltaLambdaDReduction.lean` (`D_of_T3_nonpos`) reduces hypothesis `(D)` of the $\Delta_\lambda$ tower weight bound to $T_3(k) \le 0$.
   - `folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/WstdSuperExpBound.lean` derives the super-exponential growth lower bound on the standard Wedderburn tower weight, which forces the nuclear confinement truncation scale $k(A) = O(\log A)$ (`GAP-A-3`).
   - `folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/YoungDiagramKernel.lean` carries the open all-$k$ statement honestly as `covariance_kernel_conjecture` (`kernelValue k ≤ 0`), with `kernelValue_nonpos_of_le_seven` `decide`-proved for $3 \le k \le 7$ (`cov(3..7) = -4, -16, -320, -10400, -163520`).
2. **Numerical certification:**
   - Exact rational/integer enumeration confirms $\mathrm{cov}(k) < 0$ (and $T_3(k) < 0$) for every $3 \le k \le 44$ (`computations/deltalambda/wlambda_covariance_kernel_frontier.py`, `computations/deltalambda/fl_sniady_genus_biased_measure.py`), plus an independent zero-shared-code Murnaghan–Nakayama $\beta$-number cross-check for $3 \le k \le 22$ (`qou-x631`, 2026-08-15) and literal Schensted RSK permutation enumeration $\sum_{w \in S_k} \chi^{\mathrm{sh}(w)}((123)) = T_3(k)$ for $3 \le k \le 7$ (`computations/deltalambda/fl_sniady_rsk_form_verify.py`).
3. **2026-11-22 applicability check:**
   - Verified unaffected by all November 2026 framework rulings ($\gamma\gamma$ bond rule, Nakayama-twisted trace conventions, Hopf-link electron word, jet-prolongation Frobenius drop): the statement depends purely on $S_k$ Plancherel weights $(f^\lambda)^2/k!$, cell contents, and $\chi^\lambda((123))$, with no $q_0$ anchor, no Markov parameter $z$, and no braid word.

---

## 2. Structural Diagnosis: The $\dim^2 \to \dim^3$ Non-Holonomicity Threshold

Weighting $\omega_3(\lambda)$ by $(f^\lambda)^t$ exposes why elementary symmetric-group identities stop just below the kernel:

| Exponent $t$ | Weighted sum $\sum_{\lambda \vdash k} (f^\lambda)^t \omega_3(\lambda)$ | Status and mechanism |
|---:|---|---|
| $t = 2$ | $0$ **identically** ($\forall k$) | **PROVED** (`SecondMomentKernelVanishes.tiltedMean_zero`): column orthogonality of $\chi_{\mathrm{reg}}$ / Ivanov–Olshanski Proposition 5.1 ($\mathbb{E}_{\mathrm{Planch}}[p^\#_\rho] = k^{\downarrow r}\delta_{\rho,(1^r)}$). |
| $t = 3$ | $\mathrm{cov}(k) < 0$ ($k \ge 3$) | **OPEN CONJECTURE**: one surplus factor of $f^\lambda = \chi^\lambda(e)$ beyond Plancherel measure; $f^\lambda$ is **not** a polynomial/shifted-symmetric diagram functional, breaking holonomicity and finite-genus character expansions. |

Under the $(f^\lambda)^3$-tilted probability measure $P_3(\lambda) = (f^\lambda)^3 / Z_3$, the normalized deficit $\Delta(k) := \mathbb{E}_{P_3}[C_2] - \binom{k}{2} = \mathrm{cov}(k)/Z_3$ scales empirically as $-\Delta(k) \sim c\,k^p$ with $p \approx 1.63$ ($20 \le k \le 44$), i.e. at the **Kerov-CLT fluctuation scale** $\mathrm{Std}_{\mathrm{Planch}}(C_2) \sim k^{3/2}$ rather than the leading $O(k^2)$ limit-shape scale.

---

## 3. Complete Catalog of Eliminated Proof Routes (16 Routes & Sub-Certificates)

Every negative below is a **method elimination** ("this proof mechanism fails on an explicit obstruction"), never an evidence claim against $\mathrm{cov}(k) \le 0$.

| # | Candidate Proof Route | Exact Obstruction / Counterexample | Source Audit / Witness |
|---:|---|---|---|
| 1 | **Holonomic / P-recursive recurrence** for $\mathrm{cov}(k)$ or $T_3(k)$ | No constant- or polynomial-coefficient recurrence fits exact sequence through $k \le 28$; both $|T_3(k)|$ and $|\mathrm{cov}(k)|$ absent from OEIS ($k \le 18$). | `2026-07-18-covariance-kernel-proof-epic-phase1.md` |
| 2 | **Global $\beta$-ensemble monotonicity** of $\mathbb{E}_\beta[C_2]$ under $P_\beta(\lambda) \propto (f^\lambda)^\beta$ | Not monotone in $\beta$: while $\mathbb{E}_3[C_2] < \mathbb{E}_2[C_2]$, $\mathbb{E}_\beta[C_2]$ increases from $\beta = 4$ to $\beta = 5$. | `2026-07-18-covariance-kernel-proof-epic-phase1.md` |
| 3 | **Restricted sub-family sign-definiteness** | Two-row partial sum $\sum_{\ell(\lambda) \le 2} (f^\lambda)^3 \omega_3$ flips **positive at $k = 6$**; hook partial sum flips **positive at $k = 4$**. Sign requires bulk-vs-extreme cancellation. | `2026-07-24-covariance-kernel-proof-epic-phase2.md` |
| 4 | **Murnaghan–Nakayama 3-ribbon peeling** $B(\nu) = \sum_{\lambda/\nu = \mathrm{BS}_3} (-1)^{\mathrm{ht}(\lambda/\nu)} (f^\lambda)^2 \le 0$ | Pointwise peeling sign fails first at $k = 9$ on the self-conjugate staircase core $\nu = (3, 2, 1)$, where $B((3,2,1)) > 0$. | `2026-07-24-covariance-kernel-proof-epic-phase2.md` |
| 5 | **Closed-form shifted-symmetric character evaluation** (`A1`) | Extra $f^\lambda$ factor is non-shifted-symmetric; even the unweighted cube sum $\sum_{\lambda \vdash k} (f^\lambda)^3$ has no hypergeometric closed form. | `2026-07-25-covariance-kernel-A1-eliminated-dim-threshold.md` |
| 6 | **FKG / Harris inequality on the Young-diagram dominance lattice** | Log-supermodularity of Plancherel weight fails at $k = 8$ for $\lambda = (4,2,1,1)$ and $\mu = (3,3,2)$ ($3780 > 3136$); furthermore $\omega_3(\lambda) = \omega_3(\lambda')$ and $\ln f^\lambda = \ln f^{\lambda'}$ are **U-shaped** (transpose-symmetric), not dominance-monotone. | `2026-07-24-covariance-kernel-interval-fkg-reframing.md` |
| 7 | **Chebyshev / comonotone rearrangement** | Pairwise discordance holds on only $\approx 77\%$ of partition pairs; fails explicitly between $(m, 2)$ and $(m, 1, 1)$. | `2026-07-25-covariance-kernel-epic-synthesis.md` §4 |
| 8 | **Per-edge Dirichlet form on the dominance Hasse diagram** | Edge increments $\Delta_e f^\lambda \cdot \Delta_e \omega_3$ have mixed signs across covering edges. | `2026-07-25-covariance-kernel-epic-synthesis.md` §4 |
| 9 | **Negative quadrant dependence (NQD) / Hoeffding kernel** | Joint cumulative distribution difference is not sign-definite across the diagram ordering. | `2026-07-25-covariance-kernel-epic-synthesis.md` §4 |
| 10 | **Direct Stein exchangeable-pair eigenfunction method on $\omega_3$** | Under Fulman's Plancherel up-down Markov chain, $\omega_3$ is not a conditional-drift eigenfunction; two-step marginal transfer bound loses the sign in remainder slack. | `2026-07-24-covariance-kernel-route1-exchangeable-pair.md`, `...-effective-stein-step2-transfer-bound.md` |
| 11 | **Bernstein / complete monotonicity (CM)** of tilted Laplace transform (`A3-CM`) | Alternating derivative signs hold at low order, but Hankel / Stieltjes positive-semidefiniteness determinants go negative, refuting genuine Bernstein representability. | `2026-07-25-covariance-kernel-complete-monotonicity-target.md` |
| 12 | **Śniady genus filtration (`[sniady2006asymptotics]` Prop. 3.4)** on $f^\lambda$ (`A5`) and on $\sum_\square h(\square)$ (`M1`) | $\deg \Sigma_\pi = n - 2\,\mathrm{genus}_\pi$ grades the Kerov–Olshanski polynomial-function algebra $\mathcal{A}$. While $\omega_3, R_4 \in \mathcal{A}$ (degree 4), neither $f^\lambda$ (`qou-20d3`, `rem:sniady-genus-grading-dimension-obstruction`) nor $\sum_\square h(\square)$ belongs to $\mathcal{A}$. | `2026-07-25-covariance-kernel-A5-genus-eliminated-A4-lean.md`, `2026-08-28-...-sigmah-not-in-free-cumulant-algebra.md` |
| 13 | **Pointwise Laplace / Frullani integrand nonpositivity** $\mathrm{Cov}_{\mathrm{Planch}}(H_s, \omega_3) \le 0\;\forall s > 0$ ($\iff R(x) \ge 0$ on $(0,1)$) | **FALSE for $n \ge 29$**: first exact counterexample at $n = 29$ ($\max_{s>0}\mathrm{Cov}(H_s, \omega_3) = +0.056$; quotient polynomial $R(x) = P(x)/[x(x-1)]$ gains a root in $(0,1)$ at $n = 30$). Sub-certificates also false: $\nu_v$ has 5–9 sign changes ($n \le 30$, defeating pure Laguerre/Descartes zero-counting), cumulative $S_v \le 0$ and $R$-coeff nonnegativity fail at $n = 6$, and $\mathrm{Cov}(N_v, N_w)$ is not an M-matrix. | `2026-07-25-covariance-kernel-A2-pointwise-reduction-falsified.md`, `2026-07-26-covariance-kernel-A2-nu-sign-structure.md` |
| 14 | **Unconditioned $\theta$-poissonized Maya/discrete-Bessel DPP** (Borodin–Okounkov–Olshanski) | Both $N_v = \sum_a (1-m_a)m_{a+v}$ and $\omega_3$ are quadratic in Maya occupations $m_a$, but without fixed-$|\lambda|=n$ conditioning, size fluctuations force $\mathrm{Cov}_\theta(N_v, \sum h^2) > 0\;\forall v$; Gaussian linear-response depoissonization misses signs. | `2026-07-25-covariance-kernel-A1b-dpp-maya-representation.md` |
| 15 | **Debye kink-cancellation (`c_{1/2}=0`) & coupled $\rho_P$–$\sigma$-ratio cancellation** in `M₁` | Transpose reflection is automatic and does not kill the $n^{-1/2}$ / Airy-edge exponent (retracted PR `#5939`); conversely, bounding $\rho_P$ and $V_D/V_A$ separately wastes only $1.137\times$ ($40.48\times$ headroom), refuting the claim that $\rho_P$ and $\sqrt{V_D/V_A}$ must be bounded jointly (retracted PR `#6528`). | `2026-08-29-covariance-kernel-M1-machinery-inventory-and-route.md`, `2026-09-04-covariance-kernel-M1-k5r5-ratio-route-is-the-target.md` |
| 16 | **One-step Young-lattice branching recursion** (`2026-11-22`) | Splitting $(f^\Lambda)^3$ via $f^\Lambda = \sum_{\lambda \nearrow \Lambda} f^\lambda$ and transition probabilities $p_\lambda(\square) = f^{\lambda+\square}/[(k+1)f^\lambda]$ gives $D(k+1) = (k+1)^2 \sum_{\lambda \vdash k} (f^\lambda)^3 [s(\lambda)X(\lambda) + Q(\lambda)]$, which collapses via the co-transition identity $\sum_{\lambda \nearrow \Lambda} f^\lambda X(\lambda) = \frac{m-3}{m} f^\Lambda X(\Lambda)$ to $D(k+1) = \frac{(k+1)^3}{3}\sum_{\lambda \vdash k} (f^\lambda)^3 Q(\lambda)$ with $Q(\lambda) = \mathrm{Cov}_{p_\lambda}(p_\square, c_\square^2)$. Pointwise $Q(\lambda) \le 0$ fails at $\lambda = (2,1)$ ($k=3$) and staircase-like shapes $(3,2,1), (4,3,2,1), \dots$ ($k \ge 6$), and $\mathbb{E}_3[Q]/(\mathbb{E}_3[s]\cdot k) = O(k^{-1/2})$ is again fluctuation-order. | `qou-x631` execution ledger (`2026-11-22`) |

---

## 4. Live Reductions and Machine-Checked Lean State (Through `PR #9320`, 2026-11-24)

Two active, rigorously formalized analytic reductions survive all 16 eliminations above.

### Track A — Tilt-Interpolation Pincer & Hook-Length Moment Family (`qou-ogrk` / `A2` + `A3`)

Tilting the Plancherel numerator $(f^\lambda)^2$ by $\exp(\theta \ln f^\lambda)$ defines $g(\theta) := \mathbb{E}_{2+\theta}[\omega_3]$, with $g(0) = 0$ and $\operatorname{sgn} g(1) = \operatorname{sgn} \mathrm{cov}(k)$.

1. **Pincer scaffold (`QOU.BraidsAndKnots.YoungDiagramKernelPincer`, sorry-free):**
   - `pincer_arith` / `KernelPincerLegs k`: if $g(0) = 0$, $\mathrm{covLnF}(k) = \mathrm{Cov}_{\mathrm{Planch}}(\ln f^\lambda, \omega_3) \le 0$ (`[A2]`), and $|g(1) - \mathrm{covLnF}(k)| \le -\mathrm{covLnF}(k)$ (`[A3]`), then `kernelValue k ≤ 0`.
   - `SecondMomentKernelVanishes.tiltedMean_zero`: discharges $g(0) = 0$ **unconditionally for every $k \in \mathbb{N}$**.
   - `YoungDiagramKernelDimPos.sytDim_pos_of_mem_partsOf` & `PlancherelNormalisation`: discharge $f^\lambda > 0$ on all enumerated partitions and $\sum_{\lambda \vdash k} (f^\lambda)^2 = k!$ unconditionally.
2. **Fractional Moment Positivity (`FMP`) & `(TAIL)` Carrier Program:**
   - Writing $\nu_v(n) := \mathrm{Cov}_{\mathrm{Planch}}(N_v, \omega_3)$ where $N_v(\lambda) = \#\{\square \in \lambda : h(\square) = v\}$, one has $\mathrm{Cov}_{\mathrm{Planch}}(\ln f^\lambda, \omega_3) = -\sum_{v=1}^n (\ln v)\,\nu_v(n)$ (`A2`), and `covLnF_nonpos_of_FMP` reduces `[A2]` to positivity of the exponential sum $M_\alpha(n) := \sum_{v=1}^n \nu_v(n)\,v^\alpha > 0$ for $\alpha > 0$.
   - **Even hook-power moments (`YoungDiagramKernelA2MomentSkeleton.lean`):** $M_{2r}(n) > 0$ is polynomial in $n$ (by Ivanov–Olshanski shifted-symmetric degree) and proved positive at $2r = 2$ ($M_2(n) = \frac{n(n-1)(n-2)}{3}$).
   - **Depth-0 extreme hook (`v = n`, `YoungDiagramTailFirstInstance.lean`, sorry-free):**
     $$
       \nu_n(n) = \frac{n(n-2)(n-3)\,\binom{2n-4}{n-2}}{3\,n!},
     $$
     vanishing at $n = 3$ and strictly positive for all $n \ge 4$ (onset $n_0 = 4$).
   - **Depth-1 sub-extreme hook (`v = n - 1`, `DepthOneHookClassification.lean` + `YoungDiagramTailSecondInstance.lean`, landed 2026-11-24 in `PR #9320`, sorry-free):**
     Unconditional closed form `nuV_depthOne_closed_form` for every $n \ge 4$:
     $$
       \nu_{n-1}(n) = \frac{(n - 1)(n - 4)(n^3 - 11n^2 + 32n - 30)\,\binom{2n - 6}{n - 3}}{3\,n!},
     $$
     with machine-checked exact onset theorems (`nuV_depthOne_eq_zero_iff`, `nuV_depthOne_neg_iff`, `nuV_depthOne_pos_iff`):
     - $\nu_{n-1}(4) = 0$,
     - $\nu_{n-1}(n) < 0$ for $n \in \{5, 6, 7\}$ (`-4/3, -5/3, -1/6`),
     - $\nu_{n-1}(n) > 0$ **for every $n \ge 8$** (`119/60` at $n=8$, `88/27` at $n=9$, pinning sign onset $n_1 = 8$ unconditionally).
     This confirms that per-depth tail positivity $\nu_{n-j}(n) > 0$ holds past an explicit computable onset $n_j$ rather than with a depth-independent constant $n/2 + O(1)$.

### Track B — First Odd Hook Moment $M_1(n) = \mathrm{Cov}_{\mathrm{Planch}}(\sum_\square h(\square), \omega_3) > 0$ (`qou-k5r5`, `qou-h315`)

At $\alpha = 1$ in $M_\alpha(n)$, $M_1(n) = \mathrm{Cov}_{\mathrm{Planch}}(\sum_\square h, \omega_3) = \mathrm{Cov}_{\mathrm{Planch}}(\sum_i \lambda_i^2, \sum_\square c^2)$ is the lowest non-polynomial odd hook moment (`qou-k5r5`).

1. **Exhaustive finite window (`n ≤ 78`):**
   - `computations/deltalambda/wlambda_covariance_epic_B1_kappa_window_extension.py` (`b1-kappa-window-extension.witness.json`, exact `Fraction` Plancherel summation, 0 `float64`) certifies $M_1(n)/n^{5/2} \ge \kappa_\infty = \frac{128}{225\pi^2} \approx 0.0576405 > 0$ for every $3 \le n \le 78$ (paired with `YoungDiagramKernel.m1_pos_of_le_eight` in Lean).
2. **Cauchy–Schwarz algebraic reduction (`QOU.BraidsAndKnots.YoungDiagramKernelCSMargin`, sorry-free):**
   - Using $\sum_{\square \in \lambda} h(\square) = \sum_{\square \in \lambda} |c(\square)| + \sum_a D_a^2$ (Fulman's decomposition into absolute content plus diagonal arm/leg discrepancy), write $M_1(n) = P(n) - N(n)$ where $P = \mathrm{Cov}(\sum |c|, \omega_3) = \rho_P \sigma_A \sigma_W$ and $N = -\mathrm{Cov}(\sum D^2, \omega_3) \le \sigma_D \sigma_W$.
   - `m1_pos_all_of_cs_inputs` proves over any strict ordered commutative ring that `base` ($M_1(n) > 0$ for $n < N_0$) plus the **Cauchy–Schwarz margin** $\sigma_D(n) < \rho_P(n)\,\sigma_A(n)$ for $n \ge N_0$ implies $M_1(n) > 0$ for all $n$.
3. **Sharpest analytic target (`2026-09-04-covariance-kernel-M1-k5r5-ratio-route-is-the-target.md`):**
   - Leading asymptotic margin is $m_\infty = \rho_{P,\infty} - \sqrt{V_{D,\infty}/V_{A,\infty}} \approx 0.300186 > 0$; `wlambda_covariance_epic_M1_VD_ceiling_rigorous.py` rigorously certifies $V_{D,\infty} < \frac{64}{75\pi^2}$ via interval arithmetic plus an analytic Fourier tail majorant.
   - At $N_0 = 79$ and the $n^{-1/2}$ convergence rate (`M1DescentDPPConvergence.lean`), closing `hCS` requires a finite-$n$ envelope constant $C \le m_\infty \sqrt{79} = 2.66812$.
   - Bounding **two** objects — $\rho_P(n)$ and the **ratio** $V_D(n)/V_A(n)$ — achieves empirical envelope $C_\rho + C_{\mathrm{ratio}} = 0.01226 + 0.05365 = 0.06591$, retaining **$40.48\times$ headroom** below $2.66812$ (only $1.137\times$ above $C_{\mathrm{true}} = 0.05797$), making a rigorous finite-$n$ error bound on $\rho_P$ and $V_D/V_A$ via `QOU.MathlibExt.CompositeEulerMaclaurin` + `GaussianTailBound` (`qou-h315`) the single remaining analytic step for $M_1 > 0$.

---

## 5. Five-Bean Coordination Map (`qou-x631` Shared Ledger)

Per the `2026-09-08` and `2026-09-11` cross-bean coordination notes, five open research beans share this mathematical neighborhood and must cross-cite any landing result:

| Bean ID | Exact Scope | Current Status (2026-11-24) |
|---|---|---|
| `qou-x631` | Full covariance kernel $\mathrm{cov}(k) = \sum_{\lambda \vdash k} (f^\lambda)^3 \omega_3(\lambda) \le 0$ ($\iff T_3(k) \le 0$) feeding `WstdSuperExpBound` (`GAP-A-3`) | **OPEN conjecture**; verified $k \le 44$; 16 routes eliminated; pincer + depth-0/depth-1 `(TAIL)` closed forms sorry-free in Lean (`PR #9320`). |
| `qou-k5r5` | All-$n$ proof of first odd hook moment $M_1(n) = \mathrm{Cov}_{\mathrm{Planch}}(\sum_\square h, \omega_3) > 0$ | **OPEN for $n \ge 79$**; certified $n \le 78$; `m1_pos_all_of_cs_inputs` sorry-free; narrowed to finite-$n$ bound on $\rho_P$ and $V_D/V_A$ (`qou-h315`, $40.5\times$ headroom). |
| `qou-o6ov` | Decay of normalized second Magnus trace $|\mathrm{tr}(\rho_\lambda \Omega_2)| / \dim V_\lambda$ in $b$ along two-row partitions $(a, b)$ | **OPEN mathematics** (rescoped `PR #6822`). |
| `qou-za3q` | Support mismatch in Magnus-$\Omega_2$ probes weighting all $H_{3A}$ shapes by classical Plancherel $y_\lambda$ while $\mathrm{tr}_M$ at two-strand $SU(2)$ level annihilates $> 2$-row shapes | **Measured $A = 2, 3, 4$ sign map (`2026-09-11`):** $H_{12}$ ($77/77$ partitions, max $\dim 7700$) gives $P_{\mathrm{total}}(A=4) = +34.1260\dots$ (`sign = +1`), so $(A=2, A=3, A=4) = (-1, +1, +1)$ — the single sign flip occurs between $A=2$ and $A=3$ ($+2.4702$), **not** between $A=3$ and $A=4$ (`qou-rfhj`). |
| `qou-omr7` | Inverted $q$-hook product vs quantum dimension weight $d_q(\lambda)$ in four historical Magnus probes | **Fixed in those 4 probes (`PR #6442`)**; tracked as part of the shared `qou-x631` audit trail. |

---

## 6. Key File Index for Future Agents

- **Paper prose:** [`sniady-genus-grading-dimension-obstruction.md`](../../folio/quantum-observable-universe/braids-and-knots/sniady-genus-grading-dimension-obstruction.md) (`rem:sniady-genus-grading-dimension-obstruction`, citing `[sniady2006asymptotics]`)
- **Core Lean modules (`folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/`):**
  - `DeltaLambdaDReduction.lean`, `WstdSuperExpBound.lean` (downstream `GAP-A-3` reduction)
  - `YoungDiagramKernel.lean`, `SecondMomentKernelVanishes.lean`, `YoungDiagramKernelDimPos.lean`
  - `YoungDiagramKernelPincer.lean`, `YoungDiagramKernelA2MomentSkeleton.lean`
  - `YoungDiagramTailFirstInstance.lean` ($\nu_n$, onset $n_0 = 4$), `DepthOneHookClassification.lean`, `YoungDiagramTailSecondInstance.lean` ($\nu_{n-1}$, onset $n_1 = 8$)
  - `YoungDiagramKernelCSMargin.lean`, `M1DescentDPPConvergence.lean` ($M_1 > 0$ Cauchy–Schwarz + DPP reduction)
- **Primary witnesses (`computations/deltalambda/`):**
  - `wlambda-covariance-kernel-frontier.witness.json`
  - `fl-sniady-rsk-form-verify.witness.json`, `fl-sniady-genus-biased-measure.witness.json`
  - `wlambda-covariance-epic-A2-nu-sign-structure.witness.json`
  - `wlambda-covariance-epic-A2-tail-first-instance.witness.json`, `wlambda-covariance-epic-A2-tail-second-instance.witness.json`
  - `b1-kappa-window-extension.witness.json` ($M_1(n) > 0$ for $3 \le n \le 78$)
