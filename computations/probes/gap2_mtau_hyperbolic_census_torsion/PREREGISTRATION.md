# Pre-Registration: Complete $\le 7$-Crossing 3-Braid Hyperbolic Census, Neumann–Zagier Complex Volume, and `#9213` 1-Loop Reidemeister-Torsion Tau Mass Maps (Open Gap 2, Option 2A + `qou-r0dn`)

- **Workstream / Gap**: Closing Open Gap 2 (Option 2A Primary) + Bean `qou-r0dn` (`Vol(6_2)` literal fix in `m_tau_knot_prediction.py`)
- **Branch**: `claude/gap2-mtau-hyperbolic-census-torsion-20261123`
- **Date**: 2026-11-23 (authored, committed, and pushed **before** computing any `m_tau / m_e` candidate evaluations)
- **Companion Lean 4 Module**: `folio/quantum-observable-universe/lean/QOU/StandardModel/LowCrossingThreeBraidTauSelection.lean`
- **Companion 80-dps Probe**: `computations/probes/gap2_mtau_hyperbolic_census_torsion/gap2_mtau_hyperbolic_census_torsion_probe.py`
- **Companion `qou-r0dn` Fix**: `computations/m_tau_knot_prediction.py` + `computations/m-tau-knot-prediction.witness.json`
- **Precision & Anchor**: `mpmath.workdps(80)` (`OUT_DIGITS = 50`, zero `float64`), `q0Anchor = "proton"` (`qou_substrate.constants.q_at(80)`)

---

## 1. Anti-Fit, Precision, and Epistemic Guardrails (`STRICT`)

1. **`NO FITTING, EXCEPT CAL-1/2/3`**:
   - Every substrate evaluation uses the proton-pinned parameter $q_0 = \mathrm{q\_at}(80)$ and $\hbar_{q_0} = 1 - q_0^{-1}$, derived solely from `CAL-1` ($m_e$), the figure-eight motivic period $\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3)$, and CODATA $m_p / m_e$.
   - Experimental tau-to-electron mass ratios enter **strictly** as downstream comparison targets:
     - Belle-II / PDG / CODATA-2022 high-precision benchmark: $m_\tau / m_e = 3477.228 \pm 0.023$,
     - In-repo `qou_substrate.codata.codata("tau-electron mass ratio")`: $3477.23 \pm 0.23$.
   - Zero continuous or discrete parameters are tuned, swept, or post-hoc adjusted against $m_\tau / m_e$.

2. **Zero `float64` and Zero Hardcoded Decimal Geometry Literals**:
   - Every hyperbolic volume $\mathrm{Vol}(K)$, Neumann–Zagier–Zickert Chern–Simons invariant $\mathrm{CS}(K)$, Euclidean cusp modulus $\tau_{\mathrm{cusp}}(K)$, and Dubois–Porti / Murakami 1-loop adjoint Reidemeister torsion $\tau_{\mathrm{Ad}}(K; m)$ is computed at `mp.dps = 80` by solving exact univariate integer polynomials $P_K(x) \in \mathbb{Z}[x]$ (from parabolic $SL(2, \mathbb{C})$ spinor Gröbner bases and Riley $2$-bridge polynomials) via 80-dps Newton polishing, followed by Bloch–Wigner dilogarithm $D(z) = \mathrm{Im}\,\mathrm{Li}_2(z) + \arg(1 - z)\ln|z|$, Zickert's extended Rogers dilogarithm $L(z; p, q)$ on barycentrically-ordered crossing octahedra, and Fox-calculus adjoint cohomology determinants.
   - Bean `qou-r0dn` (`Vol(6_2)` and sibling decimal string literals in `computations/m_tau_knot_prediction.py`) is remediated using the same exact $\overline{\mathbb{Q}}$ polynomial + 80-dps `mpmath` Newton/Bloch–Wigner solver (zero hardcoded decimal float strings).

3. **Zero Empirical Literals in Lean 4 (`§7c`) & Rule 13a**:
   - `LowCrossingThreeBraidTauSelection.lean` is formalized strictly over generic `[CommRing R]` / `[Field K]` and `ℤ`/`ℕ` combinatorics (`0 sorry`, `0` custom `axiom`s, zero `ℝ`, zero empirical literals).
   - **Pre-Registered Selection Criterion**: A candidate $(K, \text{Map})$ is selected **only if** $K$ belongs to the $\le 7$-crossing hyperbolic 3-braid set $\{5_2^-, 6_2^-, 6_3, 7_3^-, 7_5^-\}$, is **uniquely** singled out by its topological selection gate, and achieves $< 1\%$ relative error against CODATA-2022 $m_\tau / m_e$. Otherwise, the probe records `selected = "none"` and the Lean module isolates the unresolved carrier/dressing hypothesis as a zero-instance `class` under **Rule 13a**.

---

## 2. Pre-Registered Topological Selection Filter & Exact Braid-Index Census ($\le 8$ Crossings)

### 2.1 Filter Predicates on Prime Knots $K = \widehat{b}$

1. **Predicate F1 — 3-Strand Braid Closure & Hyperbolicity ($\beta(K) = 3$, $\mathrm{Vol}(K) > 0$)**:
   - $K$ is the closure of a 3-strand braid $b \in B_3$ with exact braid index $\beta(K) = 3$.
   - Prime knots with $\beta(K) = 2$ ($3_1 = T(2,3)$, $5_1 = T(2,5)$, $7_1 = T(2,7)$, stabilized in $B_3$ as $\sigma_0^{2m+1}\sigma_1^{\pm 1}$) and the $\beta = 3$ torus knot $8_{19} = T(3,4) = \widehat{(\sigma_0\sigma_1)^4}$ are Seifert-fibered with $\mathrm{Vol}(K) = 0$; by `InhomogeneousLeptonLoopResolvent.singPart_eq_zero_of_vol_zero` (`#9213`), their hyperbolic saddle branch vanishes identically.
   - Prime knots with Franks–Williams–Morton HOMFLY-PT bound $\beta_{\mathrm{FWM}}(K) = \frac{1}{2}(\max\deg_v P_K - \min\deg_v P_K) + 1 \ge 4$ satisfy $\beta(K) \ge 4$ and **cannot** be closed from any $b \in B_3$:
     - Excluded at $\le 7$ crossings ($\beta(K) = 4$): **$6_1$** (stevedore), **$7_2$**, **$7_4$**, **$7_6$**, **$7_7$**.
     - Excluded at $8$ crossings: $\beta(K) = 4$ (**$8_4, 8_6, 8_8, 8_{11}, 8_{13}, 8_{14}, 8_{15}$**) and $\beta(K) = 5$ (**$8_1, 8_3, 8_{12}$**).
   - Composite 3-braids $T(2, 2a+1) \# T(2, \pm(2b+1))$ ($\beta(K_1 \# K_2) = \beta(K_1) + \beta(K_2) - 1 = 3$ by Birman–Menasco) have $\mathrm{Vol} = 0$ and are non-prime.
   - The 4-crossing 3-braid $4_1 = \widehat{(\sigma_0\sigma_1^{-1})^2}$ is already assigned to the 2nd-generation muon $\mu^-$ at pole order $k = 2$ (`CAL-2`).

2. **Predicate F2 — Single-Component Knot ($|K| = 1$)**:
   - The underlying permutation $\pi(b) \in S_3$ has a single cycle ($\pi(b) \in \{(0\,1\,2), (0\,2\,1)\}$), which forces even word length $L(b) \in 2\mathbb{N}$ (`ElectronWordCandidates.numCycles_permOf_of_odd`) and even braid writhe $w(b) \in 2\mathbb{Z}$.

3. **Predicate F3 — Seifert / Bring Genus Bound ($g(K) \le 4$)**:
   - $g(K) \le 4$ (matching Bring's curve genus $g(\mathcal{B}) = 4$). Every prime 3-braid with $c(K) \le 8$ satisfies $g(K) \in \{1, 2, 3\} \le 4$.

4. **Predicate F4 — Electric Charge $Q = -1$ Writhe / Framing Gate Matching $e^-, \mu^-$**:
   Because $\beta_e = \sigma_0\sigma_1\sigma_0 \in B_3$ closes to the 2-component Hopf link ($|L|=2$, odd length $3$, constant strand framing $t_e = (-1,-1,-1)$) while $\beta_\mu = (\sigma_0\sigma_1^{-1})^2 \in B_3$ closes to $4_1$ ($|K|=1$, even length $4$, intrinsic writhe $w(\beta_\mu) = 0$, self-linking $sl(\beta_\mu) = w - 3 = -3$), we pre-register all three canonical QOU integer predicates on $b \in B_3$:
   - **Gate G1 (Component-framing gate, `ComponentFraming.lean`)**: $|K|=1$ forces every component framing $t : \mathrm{Fin}\,3 \to \mathbb{Z}$ (`t ∘ π(b) = t`) to be constant; setting $t = (-1,-1,-1)$ gives $Q = \frac{1}{3}\sum_{i=0}^2 t_i = -1$ on every 1-component 3-braid knot (fixing chiral representatives to $w(b) \le 0$): passes **$\{5_2^-, 6_2^-, 6_3, 7_3^-, 7_5^-\}$**.
   - **Gate G2 (Halved-writhe Coulomb gate, `def:coulomb-charge` $Q = w(b)/2 = -1 \iff w(b) = -2$)**: Among $\le 7$-crossing hyperbolic 3-braids, selects **uniquely $6_2^-$** ($b = \sigma_0^{-3}\sigma_1\sigma_0^{-1}\sigma_1$, $w = -2$; note $w(\beta_\mu) = 0$ fails $w/2 = -1$).
   - **Gate G3 (Muon writhe-zero / Bennequin $sl(b)/3 = -1$ gate, $w(b) = w(\beta_\mu) = 0$)**: Matches $\mu^- = 4_1$ and among non-$4_1$ $\le 7$-crossing hyperbolic 3-braids selects **uniquely $6_3$** ($b = \sigma_0^2\sigma_1^{-1}\sigma_0\sigma_1^{-2}$, $w = 0$).

### 2.2 Complete Pre-Registered Primary Candidate Set ($\le 7$-Crossing Hyperbolic 3-Braids)

| Knot $K$ | $c(K)$ | $\beta(K)$ | $g(K)$ | Minimal $B_3$ Word ($w \le 0$ branch) | $w(b)$ | Exact Parabolic Spinor Polynomial $P_K(x) \in \mathbb{Z}[x]$ |
|---|---:|---:|---:|---|---:|---|
| $4_1$ ($\mu^-$ ref) | 4 | 3 | 1 | $(\sigma_0\sigma_1^{-1})^2$ | $0$ | $x^2 + x + 1$ ($z = -x$: $z^2 - z + 1$) |
| $5_2^-$ | 5 | 3 | 1 | $\sigma_0^{-3}\sigma_1^{-1}\sigma_0\sigma_1^{-1}$ | $-4$ | $x^3 - x^2 + 1$ |
| $6_2^-$ | 6 | 3 | 2 | $\sigma_0^{-3}\sigma_1\sigma_0^{-1}\sigma_1$ | $-2$ | $x^5 - x^4 - 2x^3 + x^2 + x + 1$ |
| $6_3$ | 6 | 3 | 2 | $\sigma_0^2\sigma_1^{-1}\sigma_0\sigma_1^{-2}$ | $0$ | $x^6 - x^5 - x^4 + 2x^3 - x + 1$ |
| $7_3^-$ | 7 | 3 | 2 | $\sigma_0^{-4}\sigma_1^{-2}\sigma_0^{-1}\sigma_1$ | $-6$ | $x^6 - x^5 + 3x^4 - 2x^3 + 2x^2 - x - 1$ |
| $7_5^-$ | 7 | 3 | 2 | $\sigma_0^{-3}\sigma_1^{-2}\sigma_0^{-2}\sigma_1$ | $-6$ | $x^8 + x^7 - x^6 - 2x^5 + x^4 + 2x^3 - 2x - 1$ |

**Out-of-Filter Diagnostic Controls (reported for completeness; ineligible for primary $\le 7$-crossing 3-braid selection)**:
- **Control Set C-Beta4 ($\le 7$ crossings, excluded by $\beta(K) = 4 > 3$)**: $\{6_1, 7_2, 7_4, 7_6, 7_7\}$ (with `6_1` Riley/gluing cubic $z^3 + z^2 - 2z + 1$ / $y^3 - y^2 + 2y - 1$ verified over $\mathbb{Z}[z]$).
- **Control Set C-8x ($c(K) = 8$, $\beta(K) = 3$, excluded by $c(K) \le 7$)**: the 10 hyperbolic 8-crossing 3-braid knots $\{8_2, 8_5, 8_7, 8_9, 8_{10}, 8_{16}, 8_{17}, 8_{18}, 8_{20}, 8_{21}\}$.

---

## 3. Pre-Registered Parameter-Free Mass Maps (Pole Order $k = 3$ at $q_0 = \mathrm{q\_at}(80)$)

Let $q_0 = \mathrm{q\_at}(80)$ and $\hbar_{q_0} = 1 - q_0^{-1}$. Every candidate $K$ in the primary $\le 7$-crossing 3-braid set $\{5_2^-, 6_2^-, 6_3, 7_3^-, 7_5^-\}$ is evaluated under all three parameter-free maps:

1. **`Map A` (Bare Hyperbolic Volume)**:
   $$R_{\mathrm{A}}(K) := \frac{\mathrm{Vol}(K)}{\hbar_{q_0}^3}.$$

2. **`Map B` (Complex Volume Modulus with $\mathrm{CS}$ Normalized $\bmod\;2\pi^2$)**:
   $$R_{\mathrm{B}}(K) := \frac{\bigl|\mathrm{Vol}(K) + i\,\mathrm{CS}_{2\pi^2}(K)\bigr|}{\hbar_{q_0}^3} = \frac{\sqrt{\mathrm{Vol}(K)^2 + \mathrm{CS}_{2\pi^2}(K)^2}}{\hbar_{q_0}^3},$$
   where $\mathrm{CS}_{2\pi^2}(K) \in (-\pi^2, \pi^2]$ is the exact Neumann–Zagier–Zickert $SL(2,\mathbb{C})$ Chern–Simons invariant in the canonical meridional $\mathrm{tr}\,\rho(\mu) = +2$ spin lift. As a convention cross-check, we also report `Map B_PSL2` using Meyerhoff's $PSL(2,\mathbb{C})$ principal value $\mathrm{CS}_{\pi^2}(K) \in (-\pi^2/2, \pi^2/2]$ ($\bmod\;\pi^2$).

3. **`Map C` (`#9213` 1-Loop Reidemeister-Torsion / Inhomogeneous Loop-Resolvent Dressing of $\mathrm{Vol}(K)/\hbar_{q_0}^3$)**:
   Instantiating `QOU.Observations.InhomogeneousLeptonLoopResolvent` (`#9213`) with exact Dubois–Porti adjoint Reidemeister torsion $\mathbb{T}_{\mathrm{Ad}}(K; \mu) = 2\tau_{\mathrm{Ad}}(K; \mu)$ ($|\mathbb{T}_{\mathrm{Ad}}(4_1; \mu)| = \sqrt{3}$), Murakami's $m$-deformed torsion $T_{\mathrm{Reid}}(K; m) = 1 / \tau_{\mathrm{Ad}}(K; m)$ along $\mathrm{tr}\,\rho_m(\mu) = m + m^{-1}$ at $m = q_0$, and the $H_3(q_0)$ Convention-D regular contact ratio $\widehat{W}_{\mathrm{alg}}(K; q_0) = \tau_D(b_K; q_0) / \tau_e(q_0)$:
   - **`Map C1` (1-loop saddle free-energy log-torsion shift relative to `CAL-2` $4_1$)**:
     $$R_{\mathrm{C1}}(K) := \frac{\mathrm{Vol}(K)}{\hbar_{q_0}^3}\left(1 - \frac{\hbar_{q_0}}{2\,\mathrm{Vol}(K)}\ln\left|\frac{\mathbb{T}_{\mathrm{Ad}}(K; \mu)}{\mathbb{T}_{\mathrm{Ad}}(4_1; \mu)}\right|\right)$$
     (together with un-subtracted `Map C1u`: $\bigl(\mathrm{Vol}(K) - \frac{1}{2}\hbar_{q_0}\ln|\mathbb{T}_{\mathrm{Ad}}(K; \mu)|\bigr) / \hbar_{q_0}^3$).
   - **`Map C2a` (`#9213` inhomogeneous contact branch + $m = q_0$ Murakami cone-torsion ratio)**:
     $$R_{\mathrm{C2a}}(K) := \frac{\tau_D(b_K; q_0)}{\tau_e(q_0)} + \frac{\mathrm{Vol}(K)}{\hbar_{q_0}^3}\left|\frac{T_{\mathrm{Reid}}(K; q_0)}{T_{\mathrm{Reid}}(K; 1)}\right|.$$
   - **`Map C2b` (Direct 1-loop Murakami torsion amplitude ratio relative to $4_1$)**:
     $$R_{\mathrm{C2b}}(K) := \frac{\mathrm{Vol}(K)}{\hbar_{q_0}^3} \cdot \left|\frac{T_{\mathrm{Reid}}(K; 1)}{T_{\mathrm{Reid}}(4_1; 1)}\right| = \frac{\mathrm{Vol}(K)}{\hbar_{q_0}^3} \cdot \frac{\sqrt{3}}{|\mathbb{T}_{\mathrm{Ad}}(K; \mu)|}.$$

---

## 4. Pre-Registered Lean 4 Formalization Targets

File: `folio/quantum-observable-universe/lean/QOU/StandardModel/LowCrossingThreeBraidTauSelection.lean`

1. **Exact 3-Braid Word & Braid-Index Census Classification ($\le 8$ Crossings) over `ℤ` / `Fin 3`**:
   - Exact $S_3$ permutation cycle count, word-length parity, and writhe parity (`|K| = 1 → L(b) % 2 = 0 ∧ writhe(b) % 2 = 0`), plus Franks–Williams–Morton HOMFLY-PT degree-span inequality certificate proving $\beta(K) \ge 4$ for $\{6_1, 7_2, 7_4, 7_6, 7_7\}$ (and $\beta(K) \ge 4$ for the 10 non-3-braid 8-crossing knots), leaving **exactly six** prime $\beta = 3$ hyperbolic knots up to $7$ crossings: $\{4_1, 5_2, 6_2, 6_3, 7_3, 7_5\}$.
   - Proof of the three $Q = -1$ writhe/framing gate selections on $\{5_2^-, 6_2^-, 6_3, 7_3^-, 7_5^-\}$: G1 admits all 5; G2 ($w = -2$) uniquely selects $6_2^-$; G3 ($w = 0$) uniquely selects $6_3$.
2. **Exact Riley / Spinor / Gluing Shape Polynomials over `[CommRing R]` (`ℤ[X]`)**:
   - Exact polynomial identities, reciprocal/amphichiral symmetries ($x \mapsto x^{-1}$ or $-x^{-1}$ on $4_1, 6_3$), and discriminant / non-root-at-$\{0, \pm 1\}$ certificates for $4_1$ ($z^2 - z + 1$), $5_2$ ($z^3 - z^2 + 1$ and tetrahedral $y^3 - 2y^2 + 3y - 1$ isomorphism $y = 1/(1 - z)$), $6_1$ ($z^3 + z^2 - 2z + 1$), $6_2$ ($x^5 - x^4 - 2x^3 + x^2 + x + 1$), $6_3$ ($x^6 - x^5 - x^4 + 2x^3 - x + 1$), $7_3$, and $7_5$.
3. **Generation-3 (`k = 3`) Inhomogeneous Loop-Resolvent Pole Identities & Rule-13a Open Carrier Class**:
   - Over generic `[Field K]`, exact `ℏ_q⁻³` pole factorization and CAL-2 ratio identity `R_tau / R_mu = (Vol(K_tau) / Vol(4_1)) · ℏ_q⁻¹ · (1 + O(ℏ_q))`, plus zero-instance `class TauHyperbolicThreeBraidCarrierHypothesis` under Rule 13a if no $\le 7$-crossing 3-braid passes uniquely at $< 1\%$.
