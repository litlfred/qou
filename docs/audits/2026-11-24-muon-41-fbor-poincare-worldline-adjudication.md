# Muon $4_1$ Markov Trace, Chiral $F_{\mathrm{Bor}}$ Poincaré Weight, Asymmetric Seifert Determinant, and 80-dps Worldline Loop Adjudication

Date: 2026-11-24. Branch `claude/muon-41-fbor-poincare-seifert-lean-probe-20261124`.
Beans: `qou-1ozb`, `qou-6gf9`, `qou-24w9`, `qou-gbsa`.

Every numerical statement below is computed at 80 decimal digits (`mp.mp.dps = 80`, zero `float64`, zero fitted parameters) by
[`computations/probes/muon_fbor_poincare_and_worldline_loop_probe.py`](../../computations/probes/muon_fbor_poincare_and_worldline_loop_probe.py)
and recorded in
[`computations/probes/muon-fbor-poincare-and-worldline-loop.witness.json`](../../computations/probes/muon-fbor-poincare-and-worldline-loop.witness.json)
(`10/10` assertions passed, cross-anchor `q0_comparison` at both the proton mass-ratio pin $q_p$ and the live muon mass-ratio pin $q_\mu$, with all experimental inputs read directly from `qou_substrate.codata` CODATA-2022).

The exact algebraic identities over an arbitrary field `{K : Type*} [Field K]` (`0 sorry`, zero archimedean `ℝ` imports) are proved unconditionally in
[`folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/MuonFigureEightFBorPoincareIdentities.lean`](../../folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/MuonFigureEightFBorPoincareIdentities.lean),
alongside a comment-only cleanup of two stale pole-inverse parentheticals in
[`folio/quantum-observable-universe/lean/QOU/Nuclear/ProtonBorromeanAssembly.lean`](../../folio/quantum-observable-universe/lean/QOU/Nuclear/ProtonBorromeanAssembly.lean).

---

## 1. Executive Adjudication Summary

At the one-term Borromean proton pin
$$q_p = 1.1099785827513808075916690956107689\dots,$$
the bare figure-eight muon-electron mass ratio $\mathcal{M}_\mu(q_p) = \operatorname{Vol}(4_1)/\hbar_q^2$ (`\hbar_q = 1 - q^{-1}`) evaluates to `206.7683263706716...`, overshooting CODATA-2022 $(m_\mu / m_e)_{\mathrm{exp}} = 206.7682827(46)$ (`\sigma_\mu = 22.247 ppb`) by **`+211.20586 ppb`** (`+9.494 \sigma_\mu`; historical witness reference `+211.16 ppb`). Because $\sigma_\mu / \delta_* = 22.247 / 211.206 = 10.53\%$ (`~10.3%` nominal), the residual is only a **`0.98`-significant-digit datum**: any post-hoc rational or algebraic coefficient selected to match `211 ppb` would fail the anti-fitting entropy gate.

This adjudication establishes four crisp results:

1. **Coupled-vs-Uncoupled Re-Pinning Theorem (§2):** Any universal multiplicative dressing $\mathcal{M}_\mu(q) \mapsto \mathcal{M}_\mu(q)(1 - \delta)$ shared equally by the free muon and the proton's $2\,\mathcal{M}_\mu(q) F_{\mathrm{Bor}}(q) - 12$ constituent shifts $q_p$ by **`-10.12 ppb`**, re-absorbing **`87.18%`** (`~92%` against a nominal `200 ppb` shift) of $\delta$ back into $q_p$, leaving $m_\mu / m_e$ at **`+184.12 ppb`** while pulling Form-B $\alpha_{\mathrm{EM}}^{-1}$ by **`-69.19 ppb`**. A viable mechanism **must** therefore distinguish the open single-fermion muon worldline from the closed colour-singlet Borromean nucleon constituent.
2. **Complete Exclusion of Topological Torsion, Instanton, and Proton Counterterm Routes (§3):**
   - **Track 2 (`[murakami-h2011]` real-$u$ $4_1$ Reidemeister torsion $1 - \sqrt{3 - 2\cosh u}$):** spans **`4.82 \times 10^4\text{ ppb}`** ($u = \hbar_q^2$) to **`5.46 \times 10^6\text{ ppb}`** ($u = \ln q_p$) — two to four orders of magnitude too large.
   - **Track 4 ($4_1$ and $\Sigma(2,3,5)$ instantons):** $4_1$ hyperbolic instantons $\exp(-\operatorname{Vol}(4_1)/u)$ sit at **`1.27 .. 3.68 ppb`** (`6.07 \times 10^4\text{ ppb}` with saddle prefactor), while the $\Sigma(2,3,5)$ Chern–Simons minimal instanton $\exp(-\pi^2 / (60 \hbar_q))$ sits at **`1.90 \times 10^8\text{ ppb}`** (`0.190`).
   - **All 5 canonical proton counterterms on $V_p^3 = (A_1 A_2^{-1})^3$:** covariant all-pairs `QPairP = 0` vanishes identically; diagonal `QSelfP = I_3` is absorbed; the unprojected adjacent-crossing electromagnetic trace $E_0(q_p)(1 - q_p^{-1})\operatorname{tr}((Q_{12}^{(p)} + Q_{23}^{(p)}) V_p^3) = \mathbf{-0.53588\text{ keV}}$ has the **opposite sign** to the **`+0.22881 keV`** (`+0.22729 keV` frozen / `+0.22877 keV` linearized) proton shift required to move $q_p \to q_\mu$, worsening $\mu\text{–}p$ to **`+705.86 ppb`** (`+706 ppb`); the $e_{(2,1)}$-projected trace gives **`-25.56 keV`**; and the non-covariant modulus-flipped two-term pin $+\lvert\operatorname{tr}_{\mathrm{conn}}(p, V^3)\rvert$ pulls Form-B $\alpha_{\mathrm{EM}}^{-1}$ to **`+75.97 ppb`** (`495\sigma_\alpha`).
3. **4D Worldline QED 1-Loop Self-Energy & Surviving Unwired Candidates (§4):** Direct 80-dps quadrature of the intrinsic-clock proper-time integral confirms to $1.38 \times 10^{-28} < 10^{-25}$ at $u_\ell = 10^{-30}$:
   $$\frac{\delta m_\ell^{\mathrm{WL}}(u_\ell)}{m_\ell} = \frac{\alpha_{\mathrm{EM}}}{2\pi}\left[\frac{3}{2}\bigl(\ln(1/u_\ell) - \gamma_E\bigr) + \left(1 - \frac{3}{2}\ln 2\right) + O(u_\ell \ln u_\ell)\right],$$
   with single-clock massless-subtracted finite part $+\frac{5}{4}\frac{\alpha_{\mathrm{EM}}}{\pi}$ and exact cancellation in $m_\mu / m_e$ for a universal intrinsic Compton clock $u_e = u_\mu$. Naive 1-vertex and 2-vertex Hecke photon-projector $e_i^{(-)} = (q - \sigma_i)/[2]_q$ insertions on $4_1 = (\sigma_1 \sigma_2^{-1})^2$ carry $O(w^0)$ and $O(w^1)$ terms (`(3\alpha_{\mathrm{EM}}/(4\pi)) w = +18,983.59 ppb`, `90x` too large). The two surviving bar-even candidates (`w = q + q^{-1} - 2 = q\hbar_q^2`, `h = q - q^{-1}`, $H(q) = [2]_q / (8\pi)$) —
   - **2-loop Bring–Schwinger:** $-\alpha_{\mathrm{EM}}^2 H(q) h^2 = \mathbf{-186.22\text{ ppb}}$ (post-residual **`+24.99 ppb = +1.12\sigma_\mu`**, or `+24.95 ppb` vs `+211.16 ppb`), and
   - **1-loop double-commutator:** $-\frac{3\alpha_{\mathrm{EM}}}{4\pi} w^2 = \mathbf{-206.86\text{ ppb}}$ (post-residual **`+4.34 ppb = +0.20\sigma_\mu`**, or `+4.30 ppb` vs `+211.16 ppb`) —
   are recorded strictly as **UNWIRED WORKING-ASSUMPTION PROBES** (zero production rewire of $m_\mu / m_e$).
4. **Unconditional `[Field K]` Lean 4 Formalization (§5):** `MuonFigureEightFBorPoincareIdentities.lean` proves with `0 sorry` the exact $N=2$ Wenzl Markov trace of $4_1$ and $\Delta_3$ on the `(2,1)` weight space (including its exact ratio $\frac{2q^3}{(q^2+1)(q^4+1)}$ to the bar-symmetrized 2-strand $T(2,5)$ trace), the chiral horizontal-Dirac Poincaré identity $[3]_q! / q^3 = P_{\mathfrak{S}_3}(q^{-2}) = 1 + 2q^{-2} + 2q^{-4} + q^{-6}$, and the asymmetric Seifert / balanced Alexander factorization connecting $(t^2 - t + 1)(t^6 - t^3 + 1)\Phi_{15}(t)\big|_{t = q^{-1}}$ to $q^{-8}\Delta_{T(2,9)}(q)\Delta_{T(3,5)}(q)$.

---

## 2. Coupled-vs-Uncoupled Re-Pinning Theorem (80 dps)

Suppose a universal dressing $\mathcal{M}_\mu(q) \mapsto \mathcal{M}_\mu(q)(1 - \delta_*)$ with $\delta_* = 1 - (m_\mu/m_e)_{\mathrm{exp}} / \mathcal{M}_\mu(q_p) = 211.20582 \times 10^{-9}$ enters **both** the free muon observable and the Borromean proton equation
$$2\,\mathcal{M}_\mu(q)(1 - \delta_*)\,F_{\mathrm{Bor}}(q) - 12 = \left(\frac{m_p}{m_e}\right)_{\mathrm{exp}}.$$
Because $\frac{d\ln \mathcal{M}_\mu}{d\ln q}\big|_{q_p} = -18.18580$ and $\frac{d\ln F_{\mathrm{Bor}}}{d\ln q}\big|_{q_p} = -2.67536$, the proton solve absorbs
$$\frac{d\ln \mathcal{M}_\mu / d\ln q}{d\ln \mathcal{M}_\mu / d\ln q + d\ln F_{\mathrm{Bor}} / d\ln q} = 87.1754\%$$
of $\delta_*$ back into $q_p$:

| Quantity | Uncoupled ($q_p$) | Coupled Re-Pinned ($q_{p,\mathrm{coupled}}$) | Shift |
|---|---:|---:|---:|
| Pin $q$ | `1.109978582751380808...` | `1.109978571513288227...` | **`-10.12460 ppb`** |
| Predicted $m_\mu / m_e$ residual vs CODATA-2022 | `+211.20586 ppb` (bare) / `0.00 ppb` (uncoupled) | **`+184.11957 ppb`** (`+8.28 \sigma_\mu`) | `87.18%` re-absorbed |
| Form-B $\alpha_{\mathrm{EM}}^{-1}$ | `137.0359991269509` (`-0.365 ppb`) | `137.0359896460661` (`-69.551 ppb`) | **`-69.18536 ppb`** |

Consequently, no rescaling of the abstract $4_1$ geometric carrier $\operatorname{Vol}(4_1)/\hbar_q^2$ shared by the bound proton constituent can close the $\mu\text{–}p$ offset without simultaneously failing by `+184.12 ppb` on $m_\mu / m_e$ and `-69.19 ppb` (`-452\sigma_\alpha`) on $\alpha_{\mathrm{EM}}^{-1}$.

---

## 3. Exclusion of Tracks 2 & 4 and All Five Proton Counterterms

### 3.1 Track 2 (`[murakami-h2011]` Deformed $4_1$ Torsion) & Track 4 (Instantons)

| Candidate Mechanism | Substrate Evaluation | Fractional Effect (`ppb`) | Adjudication |
|---|---|---:|---|
| Track 2: $1 - \sqrt{3 - 2\cosh u}$ at $u = \hbar_q^2$ | `u = 0.00981719` | **`+4.819 \times 10^4`** | Excluded (`228x` too large, wrong sign) |
| Track 2: $1 - \sqrt{3 - 2\cosh u}$ at $u = w = [2]_q - 2$ | `u = 0.01089687` | **`+5.937 \times 10^4`** | Excluded (`281x` too large, wrong sign) |
| Track 2: $1 - \sqrt{3 - 2\cosh u}$ at $u = \hbar_q$ | `u = 0.09908172` | **`+4.925 \times 10^6`** | Excluded (`2.33 \times 10^4\text{x}` too large) |
| Track 2: $1 - \sqrt{3 - 2\cosh u}$ at $u = \ln q_p$ | `u = 0.10434072` | **`+5.463 \times 10^6`** | Excluded (`2.59 \times 10^4\text{x}` too large) |
| Track 4: $4_1$ instanton $\exp(-\operatorname{Vol}(4_1)/\hbar_q)$ | `Vol(4_1) = 2.0298832` | **`1.267`** | Excluded (`167x` too small) |
| Track 4: $4_1$ instanton $\exp(-\operatorname{Vol}(4_1)/\ln q_p)$ | `ln q_p = 0.1043407` | **`3.557`** | Excluded (`59x` too small) |
| Track 4: $4_1$ instanton $\exp(-2\operatorname{Vol}(4_1)/(q_p - q_p^{-1}))$ | `h_q / 2 = 0.1045301` | **`3.685`** | Excluded (`57x` too small) |
| Track 4: $\Sigma(2,3,5)$ instanton $\exp(-\pi^2 / (60 \hbar_q))$ | `pi^2 / (60 hbar_q) = 1.66017` | **`1.901 \times 10^8`** | Excluded (`9.0 \times 10^5\text{x}` too large; Ohtsuki floor `0.544`) |

### 3.2 Five Canonical Proton Counterterms on $V_p^3 = (A_1 A_2^{-1})^3$

Aligning $q_p$ onto $q_\mu$ from the proton side requires adding **`+0.22881 keV`** (`+0.00044776 m_e` at live $q_\mu$; `+0.22729 keV` at frozen $q_\mu$) to the proton model at $q_\mu$. All five canonical operators formalized in `QOU/BraidsAndKnots/NucleonWeightSpaceTwoTerm.lean` fail:

1. **Covariant all-pairs Coulomb `QPairP = Q12p + Q23p + Q13p`:** identically zero on the `(2,1)` proton weight space (`0.00000 keV`).
2. **Diagonal self-energy `QSelfP = Q_1^2 + Q_2^2 + Q_3^2`:** acts as `1 * I_3`, contributing zero differential shift beyond the bare trace.
3. **Unprojected adjacent-crossing EM trace $E_0(q_p)(1 - q_p^{-1})\operatorname{tr}((Q_{12}^{(p)} + Q_{23}^{(p)}) V_p^3)$:** evaluates to **`-0.53588 keV`** (opposite sign!), pushing $q_p$ downward and **worsening** $\mu\text{–}p$ from `+211.21 ppb` to **`+705.86 ppb`**.
4. **$e_{(2,1)}$-projected adjacent-crossing EM trace $E_0(q_p)(1 - q_p^{-1})\operatorname{tr}(e_{(2,1)}^{(p)}(Q_{12}^{(p)} + Q_{23}^{(p)}) V_p^3)$:** evaluates to **`-25.5612 keV`** (`O((q-1)^2)` rather than `O((q-1)^4)`, opposite sign and `112x` too large).
5. **Non-covariant modulus-flipped two-term pin $+\lvert\operatorname{tr}_{\mathrm{conn}}(p, V^3)\rvert$:** moves $q_p$ by **`+11.1709 ppb`**, degrading Form-B $\alpha_{\mathrm{EM}}^{-1}$ from `-0.365 ppb` to **`+75.970 ppb`** (`+495.7\sigma_\alpha`).

---

## 4. 4D Worldline QED 1-Loop Asymptotic and Unwired Working-Assumption Candidates

### 4.1 Exact 4D Worldline QED 1-Loop Fermion Self-Energy (`|quad - symbolic| < 1e-25`)

For an open spin-$1/2$ worldline of mass $m_\ell$ in 4D Euclidean Feynman gauge with intrinsic proper-time cutoffs $s_1 = m_\ell^2 t_1 \ge u_\ell$ and $s_2 = m_\ell^2 t_2 \ge u_\ell$,
$$\frac{\delta m_\ell^{\mathrm{WL}}(u_\ell)}{m_\ell} = \frac{\alpha_{\mathrm{EM}}}{2\pi}\int_{u_\ell}^\infty ds_1 \int_{u_\ell}^\infty ds_2\,\frac{2 s_1 + s_2}{(s_1 + s_2)^3}\exp\!\left(-\frac{s_1^2}{s_1 + s_2}\right) = \frac{\alpha_{\mathrm{EM}}}{2\pi}\left[\frac{3}{2}\bigl(\ln(1/u_\ell) - \gamma_E\bigr) + \left(1 - \frac{3}{2}\ln 2\right) + O(u_\ell \ln u_\ell)\right].$$
At $u_\ell = 10^{-30}$, 80-dps Gauss–Legendre quadrature gives `102.710784916539838525773999143623...` versus the closed symbolic asymptotic `102.710784916539838525773999143486...`, agreeing to **`1.377 \times 10^{-28} < 10^{-25}`**. Subtracting the single-clock massless UV reference $\frac{\alpha_{\mathrm{EM}}}{2\pi}\int_0^1 (1+y) E_1(u_\ell)\,dy$ yields the finite part $\frac{\alpha_{\mathrm{EM}}}{2\pi}\int_0^1 -(1+y)\ln(y^2)\,dy = +\frac{5}{4}\frac{\alpha_{\mathrm{EM}}}{\pi}$. Because an intrinsic Compton clock sets $u_e = u_\mu$, this continuum 1-loop factor is lepton-universal and cancels identically (`0`) in $m_\mu / m_e$ unless coupled to the nontrivial braid geometry of $4_1$ (absent on the unknotted electron worldline).

### 4.2 Hecke Photon-Projector Correlators on $4_1$ vs Surviving Bar-Even Working Assumptions

Inserting the Hecke antisymmetrizer $e_i^{(-)} = (q - \sigma_i)/[2]_q$ onto $4_1 = (\sigma_1 \sigma_2^{-1})^2$ inside the $B_3$ Markov trace gives non-vanishing $O(w^0)$ and $O(w^1)$ pieces ($\langle e_1^{(-)}\rangle_{4_1} = -0.54762$, $\langle e_1^{(-)} \sigma_1 \sigma_2^{-1} e_1^{(-)} \sigma_1 \sigma_2^{-1}\rangle_{4_1} = +0.11671$, $\langle [e_1^{(-)}, \sigma_2^{-1}]^2\rangle_{4_1} = +0.60499$ at $q_p$). Even after renormalising the $q \to 1$ ($O(w^0)$) limit, an $O(w^1)$ 1-loop QED term has scale $\frac{3\alpha_{\mathrm{EM}}}{4\pi} w = \mathbf{+18{,}983.59\text{ ppb}}$ (`89.9x` larger than `211.21 ppb`).

Only two parameter-free bar-even open-worldline structures land in the `~200 ppb` window (evaluated at both $q_p$ and $q_\mu$ in the witness):

| Unwired Working-Assumption Candidate | Formula (bar-even under $q \leftrightarrow q^{-1}$) | Shift at $q_p$ (`ppb`) | Post-Shift Residual at $q_p$ | Status |
|---|---|---:|---:|---|
| 2-loop Bring–Schwinger open-worldline dressing | $-\alpha_{\mathrm{EM}}^2 H(q) h^2$, $H(q)=\frac{[2]_q}{8\pi}$, $h = q - q^{-1}$ | **`-186.21889`** | `+24.99 ppb` (`+1.12\sigma_\mu`; `+24.95 ppb` vs `+211.16 ppb`) | **UNWIRED WORKING ASSUMPTION** |
| 1-loop double-commutator open-worldline dressing | $-\frac{3\alpha_{\mathrm{EM}}}{4\pi} w^2$, $w = q + q^{-1} - 2 = q\hbar_q^2$ | **`-206.86166`** | `+4.34 ppb` (`+0.20\sigma_\mu`; `+4.30 ppb` vs `+211.16 ppb`) | **UNWIRED WORKING ASSUMPTION** |

Note that on the electromagnetic coupling side, `EmFermionLoopFourTopology` (`#9360`) proves unconditionally that summing all four signed chiral 2-vertex topologies $(\epsilon_1, \epsilon_2) \in \{+,-\}^2$ on $U_q(\mathfrak{sl}_2)$ cancels the $\pm h\,m(\sigma_2)$ chiral tadpoles identically to $-1 \cdot h^2$, deriving Form B's $(1 - h^2 \alpha)$ loop factor; whether an open figure-eight fermion worldline inherits the corresponding 2-loop $-\alpha_{\mathrm{EM}}^2 H(q) h^2$ or 1-loop $-\frac{3\alpha_{\mathrm{EM}}}{4\pi} w^2$ suppression without $O(w^1)$ leakage remains open.

> **Anti-Fitting & Entropy Guardrail:** Because CODATA-2022 resolves the `211.21 ppb` gap to only `10.53%` (`~1` significant digit), neither candidate is wired into production `m_mu/m_e`. Wiring requires a first-principles 4D $\to$ 1D worldline-to-Hecke reduction proving both the absence of $O(w^1)$ leakage on $4_1$ and decoupling from the colour-singlet Borromean constituent.

---

## 5. `[Field K]` `0-sorry` Lean 4 Identities (`MuonFigureEightFBorPoincareIdentities.lean`)

Over an arbitrary field `{K : Type*} [Field K]` with zero archimedean imports, `MuonFigureEightFBorPoincareIdentities.lean` proves unconditionally:

1. **Wenzl $N=2$ Markov Trace of $\Delta_3$ and $4_1$ (`qou-1ozb`, `qou-6gf9`):** With $y_{(3)}(q) = \frac{q^4 + 1}{(q^2 + 1)^2}$ and $y_{(2,1)}(q) = \frac{q^2}{(q^2 + 1)^2}$ satisfying $y_{(3)}(q) + 2 y_{(2,1)}(q) = 1$:
   - $\chi_{(2,1)}(\Delta_3) = \operatorname{tr}(A_1 A_2 A_1) - q^3 = 0$;
   - $\chi_{(2,1)}(4_1) = \operatorname{tr}\bigl((A_1 A_2^{-1})^2\bigr) - 1 = \frac{q^8 - 2q^6 + q^4 - 2q^2 + 1}{q^4}$;
   - $\operatorname{tr}_M(4_1) = y_{(3)}(q)\cdot 1 + y_{(2,1)}(q)\cdot\chi_{(2,1)}(4_1) = \frac{q^8 - q^6 + q^4 - q^2 + 1}{q^2(q^2 + 1)^2} = \frac{q^5 + q^{-5}}{(q + q^{-1})^3}$;
   - Relative to the bar-symmetrized 2-strand $T(2,5)$ trace $\overline{\operatorname{tr}}_M^{(B_2)}(T(2,5)) = \frac{(q^2 + q^{-2})(q^5 + q^{-5})}{2(q + q^{-1})^2}$, $\operatorname{tr}_M(4_1) = \frac{2q^3}{(q^2 + 1)(q^4 + 1)} \cdot \overline{\operatorname{tr}}_M^{(B_2)}(T(2,5))$.
2. **Chiral Horizontal-Dirac Poincaré Identity for $F_{\mathrm{Bor}}$'s `/q^3` (`qou-24w9`):** Under $T = q^{-1}\sigma$ ($q \ne 0$), the chiral quadratic Hecke relation $(T - 1)(T + q^{-2}) = 0$ is equivalent to the balanced skein relation $(\sigma - q)(\sigma + q^{-1}) = 0$, and the quantum factorial weight in $F_{\mathrm{Bor}}(q)$ equals the $\mathfrak{S}_3$ Poincaré polynomial in $q^{-2}$:
   $$\frac{(q^2 + 1 + q^{-2})(q + q^{-1})}{q^3} = (1 + q^{-2})(1 + q^{-2} + q^{-4}) = 1 + 2q^{-2} + 2q^{-4} + q^{-6}.$$
3. **Asymmetric Seifert Determinant / Balanced Alexander Identity (`qou-gbsa`, `#9359`):** Both in cleared polynomial form over any commutative ring and in rational balanced-Alexander form over `[Field K]` ($q \ne 0, q - 1 \ne 0, q^2 - 1 \ne 0, q^9 - 1 \ne 0, q^3 - 1 \ne 0, q^5 - 1 \ne 0$), at $t = q^{-1}$:
   $$(t^2 - t + 1)(t^6 - t^3 + 1)(t^8 - t^7 + t^5 - t^4 + t^3 - t + 1) = q^{-8}\,\Delta_{T(2,9)}(q)\,\Delta_{T(3,5)}(q) = \kappa_{\mathrm{Seifert}}(q)^{-1},$$
   where $\Delta_{T(m,n)}(q) = q^{-(m-1)(n-1)/2}\frac{(q^{mn} - 1)(q - 1)}{(q^m - 1)(q^n - 1)}$ and $\kappa_{\mathrm{Seifert}}(q_p) = q_p^{b_1(\Sigma_4)} / \bigl(\Delta_{T(2,9)}(q_p)\Delta_{T(3,5)}(q_p)\bigr) = 1.905155328\dots$ (`b_1(\Sigma_4) = 8`).
