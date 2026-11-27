# Pre-Registration: Bring Curve $N_{\mathrm{gen}}=3$ Zero-Mode Branching, $S_3 \subset S_5$ CKM/PMNS Overlap Textures, and Satellite $T(2,7)\text{–}4_1$ Tau Mass Candidates

- **Bean**: `qou-gen3` (`Q-Gap-7`, parent epic `qou-sm8w`; aggregates `qou-x4qm`, `qou-xtcl`, `qou-htk4`, `qou-y0mq`)
- **Branch**: `claude/sm8w-bring-ngen3-ckm-tau-20261123`
- **Date**: 2026-11-23 (committed **before** writing or running the numerical probe)
- **Companion Lean 4 Module**: `folio/quantum-observable-universe/lean/QOU/StandardModel/BringGenerationSplitAndCKMTexture.lean`
- **Companion 80-dps Probe**: `computations/probes/sm8w_bring_ngen3_ckm_tau/sm8w_bring_ngen3_ckm_tau_probe.py`
- **Precision & Anchor**: `mpmath.workdps(80)` (zero `float64`), `q0Anchor = "proton"` (`qou_substrate.constants.q_at(80)`)

---

## 1. Epistemic & Anti-Fit Guardrails (STRICT)

1. **Owner Non-Claim Guardrail on $N_{\mathrm{gen}} = 3$**:
   - Per owner ruling (`docs/audits/2026-10-10-generation-count-two-independent-countings.md`, `sm-open-problems.md:18`), *"Bring's generation count is not established [unconditionally]"*.
   - On Bring's curve $\mathcal{B} \subset \mathbb{P}^4$ of genus $g = 4$ with $\mathrm{Aut}(\mathcal{B}) \cong S_5$, the holomorphic canonical differential space $H^0(\mathcal{B}, K_{\mathcal{B}})$ has dimension $g = 4$ and transforms as the **4-dimensional irreducible standard representation** $V_{(4,1)} = V_{\mathrm{std}} = \{x \in F^5 \mid \sum_{i=0}^4 x_i = 0\}$ of $S_5$.
   - Meanwhile, the four generation-counting candidates in the corpus disagree (`Seifert genus ≤ 4` gives $4$ on $\{3,5,7,9\}$; `Morgan–Voyce continuant divisibility` $b_3 \mid b_9$ gives $3$ on $\{3,5,7\}$; `$S_5$-equivariance` $\mathbb{Z}_s \hookrightarrow S_5$ gives $2$ on $\{3,5\}$; `Bring fibration branch-point conjugate pairs` gives $3$).
   - Therefore, we **never** claim $N_{\mathrm{gen}} = 3$ is unconditionally forced. Instead, we prove the exact algebraic branching $4 \to 3 \oplus 1$ under $S_4 = \mathrm{Stab}_{S_5}(4)$, $3 \to 2 \oplus 1$ under $S_3 = \mathrm{Stab}_{S_5}(3,4)$, and $4 \to 2 \oplus 1 \oplus 1'$ under $S_3 \times S_2 \subset S_5$, prove the four-filter count disagreement (`4 ≠ 3`, `3 ≠ 2`, `4 ≠ 2`), and isolate the equivariant spin/chirality singlet-quotient selection as a **Rule-13a zero-instance `class BringChiralGenerationSelectionHypothesis`**.

2. **Zero Empirical Inputs in Lean & Zero Fitting in Numerics**:
   - `BringGenerationSplitAndCKMTexture.lean` is authored strictly over generic rings/fields (`{R : Type*} [CommRing R]`, `{F : Type*} [Field F]`, and `ℤ` for finite-group character tables) with **zero `ℝ`**, **zero `sorry`**, **standard axioms only**, and **zero empirical literals** (§7c).
   - Every numerical candidate in `sm8w_bring_ngen3_ckm_tau_probe.py` is constructed **exclusively** from the proton-pinned substrate $q_0 = \mathrm{q\_at}(80)$ (`CAL-1` $m_e$, $\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3)$, and proton ratio $m_p/m_e$).
   - Experimental values (PDG-2024 CKM/PMNS mixing parameters and CODATA-2022 $m_\tau/m_e$) are **downstream comparison targets only**, never inputs. All pre-declared candidates—hits and misses alike—are reported with exact signed and absolute relative errors, with `selected = "none"` (scope-(a) exploratory probe).

---

## 2. Pre-Registered Lean 4 Formalization Targets

File: `folio/quantum-observable-universe/lean/QOU/StandardModel/BringGenerationSplitAndCKMTexture.lean`

1. **§1 — Bring Canonical Differential Space $V_{\mathrm{std}}$ Branching ($S_5 \supset S_4 \supset S_3$ and $S_5 \supset S_3 \times S_2$) & Conditional Generation Quotient**:
   - Exact character restriction inner products over `ℤ` (interfacing with `QOU.Brings.S5Char`):
     - $\mathrm{Res}^{S_5}_{S_4} V_{(4,1)} = V_{(3,1)} \oplus V_{(4)}$ ($4 = 3 + 1$),
     - $\mathrm{Res}^{S_5}_{S_3} V_{(4,1)} = V_{(2,1)} \oplus 2\,V_{(3)}$ ($4 = 2 + 1 + 1$, via $3 \to 2 \oplus 1$ on $V_{(3,1)}$),
     - $\mathrm{Res}^{S_5}_{S_3 \times S_2} V_{(4,1)} = (V_{(2,1)} \boxtimes 1) \oplus (1 \boxtimes 1) \oplus (1 \boxtimes \mathrm{sgn})$ ($4 = 2 + 1 + 1'$).
   - Concrete module-level equivariant idempotents over generic `[Field F]` (`(4 : F) ≠ 0`, `(3 : F) ≠ 0`, `(2 : F) ≠ 0`):
     - `permAct : Equiv.Perm (Fin 5) → (Fin 5 → F) → (Fin 5 → F)` preserving `inBringStd x ↔ ∑ i, x i = 0`.
     - Explicit $S_4$-equivariant projectors `projGen3` and `projSing1` on $V_{\mathrm{std}}$ satisfying completeness (`projGen3 x + projSing1 x = x` for $x \in V_{\mathrm{std}}$), idempotency, mutual orthogonality, $S_4$-intertwining (`σ 4 = 4`), and explicit 3-element basis linear independence + span of `V_gen3`.
     - Explicit $S_3$-equivariant refinement `projDoublet2` + `projDem1 = projGen3` (`σ 3 = 3 ∧ σ 4 = 4`), decomposing $3 \to 2 \oplus 1$.
   - Morgan–Voyce composite harmonic identity `mvB h 9 = mvB h 3 * (h^6 + 6*h^4 + 9*h^2 + 1)` vs non-divisibility witness at $h^2 = -1$ (`b_3 = 0` while `b_5 = -1`, `b_7 = -1`), four-filter disagreement (`card {3,5,7,9} = 4`, `card {3,5,7} = 3`, `card {3,5} = 2`), and zero-instance Rule-13a `class BringChiralGenerationSelectionHypothesis` deriving `Module.finrank F (LinearMap.range π) = 3` from rank-nullity on the 4D canonical differential module.

2. **§2 — $S_3 \subset S_5$ Democratic/Tribimaximal Algebra, Cabibbo Perturbation, & Unitary Jarlskog CP Invariant**:
   - Integer TBM eigenmatrix $M_{\mathrm{TBM}} \in M_3(R)$ satisfying $M_{\mathrm{TBM}}^T M_{\mathrm{TBM}} = \mathrm{diag}(6,3,2)$ and $M_{\mathrm{TBM}}^T D_3 M_{\mathrm{TBM}} = \mathrm{diag}(0,9,0)$ over any `[CommRing R]`, plus normalized $U_{\mathrm{TBM}}(s_2, s_3)$ satisfying $U_{\mathrm{TBM}}^T U_{\mathrm{TBM}} = I_3$ over any `[Field F]` with $s_2^2 = 2, s_3^2 = 3$.
   - Exact $2 \times 2$ Cabibbo perturbation identity for a broken democratic doublet block $\begin{pmatrix} 0 & \beta \\ \beta & \alpha \end{pmatrix}$ with $\beta = q - q^{-1}$ and $\alpha = [3]_q = q^2 + 1 + q^{-2}$ (or $\alpha = 1$), proving trace, determinant, discriminant $\alpha^2 + 4\beta^2$, and rational mixing identity $([3]_q^2 + 4(q-q^{-1})^2) \sin^2(2\theta_{12}) = 4(q-q^{-1})^2$ for any $(c,s)$ solving the $2\times 2$ rotation equation.
   - Generic Gaussian ring `QuadI R` (`R × R` with conjugation and `normSq` over any `[CommRing R]`):
     - Unitarity of $V = U_u^\dagger U_d$ from unitarity of $U_u, U_d$;
     - Rephasing invariance of $J(V) = \mathrm{Im}(V_{01} V_{12} V_{02}^* V_{11}^*)$ under unit-norm quark phase redefinitions;
     - Row-orthogonality plaquette antisymmetry $J_{01,12}(V) = -J_{00,12}(V)$;
     - Exact Chau–Keung $3 \times 3$ matrix unitarity ($V^\dagger V = I_3$, $V V^\dagger = I_3$) and exact Jarlskog factorization $J(V) = c_{12} s_{12} c_{23} s_{23} c_{13}^2 s_{13} s_\delta$, vanishing iff an angle factor or $s_\delta$ vanishes (over `[IsDomain R]`), and CP-conjugation sign reversal $J(\overline{V}) = -J(V)$;
     - 3-strand polynomial-framed Burau clasp matrix $\widetilde{C}(t) = t B(\sigma_1 \sigma_2^{-1}) = \begin{pmatrix} t - t^2 & -1 \\ t & -1 \end{pmatrix}$ satisfying $\det(t^2 I_2 - \widetilde{C}(t)^2) = t^2(1 + t + t^2)(-1 + 3t - t^2)$ over any `[CommRing R]`.

3. **§3 — Seifert–Torres $(2,7)$-Cabled Figure-Eight Satellite Alexander & Burau Factorisation**:
   - Framed figure-eight Alexander polynomial $\Delta_{4_1}^{\mathrm{pos}}(t) = -1 + 3t - t^2$ ($\Delta_{4_1}^{\mathrm{pos}}(1) = 1$, $\Delta_{4_1}^{\mathrm{pos}}(-1) = -5$) composed with `QOU.BraidsAndKnots.QIntegerAlexanderTorus.alexanderTorus2` to form $\Delta_{C_{2,2n+1}(4_1)}(t) = \Delta_{4_1}^{\mathrm{pos}}(t^2) \cdot \Delta_{T(2,2n+1)}(t)$ over any `[CommRing R]`.
   - Exact division-free rational identity $(1+t)\Delta_{C_{2,2n+1}(4_1)}(t) = (-1 + 3t^2 - t^4)(1 + t^{2n+1})$ and cabled Burau determinant factorisation $\det(t^4 I_2 - \widetilde{C}(t^2)^2)(1 - (-t)^{2n+1}) = t^4(1+t^2+t^4)(1+t)\Delta_{C_{2,2n+1}(4_1)}(t)$.
   - Specialisation to $n = 3$ ($C_{2,7}(4_1)$): degree-10 explicit expansion, normalization $\Delta_{C_{2,7}(4_1)}(1) = 1$, knot determinant $\Delta_{C_{2,7}(4_1)}(-1) = 7$, bar-palindromicity $t^{10} \Delta_{C_{2,7}(4_1)}(t^{-1}) = \Delta_{C_{2,7}(4_1)}(t)$ (in Laurent-free coefficient-reversal form), and sign-indefiniteness witness ($\Delta_{4_1}^{\mathrm{pos}}(1) = 1 > 0$, $\Delta_{4_1}^{\mathrm{pos}}(3) = -1 < 0$) locating the real node in $(1,3)$ (`\varphi^2 = (3+\sqrt{5})/2 \approx 2.618`).

---

## 3. Pre-Registered 80-dps Numerical Evaluations & Comparison Targets

### Downstream Experimental Reference Targets (Comparison Only — Zero Calibration Input)
- **PDG-2024 CKM**:
  - $|V_{us}| = 0.2243 \pm 0.0008$
  - $|V_{cb}| = 0.0422 \pm 0.0008$
  - $|V_{ub}| = 0.00394 \pm 0.00036$
  - $J_{\mathrm{CKM}} = (3.08 \pm 0.15) \times 10^{-5}$
- **PDG-2024 PMNS (Normal Ordering)**:
  - $\sin^2\theta_{12} = 0.307 \pm 0.013$
  - $\sin^2\theta_{23} = 0.546 \pm 0.021$
  - $\sin^2\theta_{13} = 0.0220 \pm 0.0007$
- **CODATA-2022 Charged-Lepton Mass Ratio**:
  - $m_\tau / m_e = 3477.23 \pm 0.23$ (from `qou_substrate.codata("tau-electron mass ratio")`; we also record the Belle-II/PDG-2024 combination $3477.228 \pm 0.023$ as a secondary comparison figure).

### Closed Pre-Declared Candidate List

With $q_0 = \mathrm{q\_at}(80)$, $h = q_0 - q_0^{-1}$, $\hbar_{q_0} = 1 - q_0^{-1}$, $[2]_{q_0} = q_0 + q_0^{-1}$, $[3]_{q_0} = q_0^2 + 1 + q_0^{-2}$:

#### Part (a): $S_5 \supset S_4 \supset S_3$ Overlap & CKM / PMNS Candidates
1. **Branching & Subgroup Gram Geometry**:
   - Verify exact 80-dps idempotency/orthogonality of $P_{\mathrm{gen},3}, P_{\mathrm{sing},1}, P_{\mathrm{doublet},2}, P_{\mathrm{dem},1}$, conjugate $S_3 \subset S_4$ fixed-line Gram cosine $-\frac{1}{3}$ vs $S_3 \times S_2$ symmetric fixed-line Gram overlaps on $V_{\mathrm{std}}$, overlap singular values against the $\mathbb{Z}_5$ weak $T(3,5)$ Bloch basis on $V_{\mathrm{std}}$, and Hoefsmit $(2,1)$ crossing angle $\cos\theta_H(q_0) = 1/[2]_{q_0}$.
2. **CKM Candidates**:
   - **CKM-C0 (`unperturbed_identity`)**: $V = I_3$ ($|V_{us}|=|V_{cb}|=|V_{ub}|=J=0$).
   - **CKM-C1a (`hecke_hierarchy_z5_phase`)**: Chau–Keung matrix with $\sin\theta_{12} = h$, $\sin\theta_{23} = h^2$, $\sin\theta_{13} = h^3 / [3]_{q_0}$, $\delta = 2\pi/5$ (primitive Bring $\mathbb{Z}_5$ phase).
   - **CKM-C1b (`hecke_hierarchy_s3_phase`)**: Same angles $\sin\theta_{12} = h$, $\sin\theta_{23} = h^2$, $\sin\theta_{13} = h^3 / [3]_{q_0}$, with $\delta = \pi/3$ ($S_3$ Weyl phase).
   - **CKM-C2 (`democratic_yukawa_svd_overlap`)**: Left-unitary overlap $V_{\mathrm{CKM}} = U_u^\dagger U_d$ from explicit Hermitian democratic + Hecke-perturbed Yukawa operators in the Jacobi basis:
     $Y_u = \mathrm{diag}(0, h^2, [3]_{q_0})$ and $Y_d = [3]_{q_0} E_{33} + h E_{22} + h^2(e^{i\cdot 2\pi/5} E_{12} + e^{-i\cdot 2\pi/5} E_{21}) + h^2 [3]_{q_0}(E_{23} + E_{32})$.
   - **CKM-C3 (`cabibbo_two_gen_perturbation_comparison`)**: Compare the two canonical $2\times 2$ Cabibbo formulas $\tan(2\theta_{12}) = 2h/[3]_{q_0}$ vs $\tan\theta_{12} = h$ vs $\sin\theta_{12} = h / \sqrt{[3]_{q_0}}$.
3. **PMNS Candidates**:
   - **PMNS-P0 (`exact_tribimaximal`)**: $U_{\mathrm{TBM}}$ ($\sin^2\theta_{12} = 1/3$, $\sin^2\theta_{23} = 1/2$, $\sin^2\theta_{13} = 0$, $J = 0$).
   - **PMNS-P1a (`hecke_charged_lepton_tbm_maximal_cp`)**: $U_{\mathrm{PMNS}} = R_{12}(\arcsin h, \delta=\pi/2)^\dagger U_{\mathrm{TBM}}$ (yielding $\sin^2\theta_{13} = h^2/2$).
   - **PMNS-P1b (`hecke_charged_lepton_tbm_z5_cp`)**: $U_{\mathrm{PMNS}} = R_{12}(\arcsin h, \delta=2\pi/5)^\dagger U_{\mathrm{TBM}}$.
   - **PMNS-P1c (`hecke_charged_lepton_tbm_real`)**: $U_{\mathrm{PMNS}} = R_{12}(\arcsin h, \delta=0)^T U_{\mathrm{TBM}}$ ($J = 0$).

#### Part (b): Satellite $T(2,7)\text{–}4_1$ vs Bare $5_2$ / $T(2,7)$ $\tau/e$ Mass-Ratio Candidates
1. **TAU-B0 (`bare_T27_volume`)**: $\mathrm{Vol}(T(2,7)) / \hbar_{q_0}^2 = 0$.
2. **TAU-B1 (`bare_5_2_vol_k2`)**: $\mathrm{Vol}(5_2) / \hbar_{q_0}^2$ with $\mathrm{Vol}(5_2) = 3 D(y_1)$ on $X^3 - 2X^2 + 3X - 1 = 0$ at 80 dps.
3. **TAU-B2 (`bare_5_2_vol_k3`)**: $\mathrm{Vol}(5_2) / \hbar_{q_0}^3$.
4. **TAU-S1 (`pure_cable_C27_4_1_jsj_vol_k2`)**: $\mathrm{Vol}_{\mathrm{JSJ}}(C_{2,7}(4_1)) / \hbar_{q_0}^2 = \mathrm{Vol}(4_1) / \hbar_{q_0}^2$ (Seifert cable piece contributes $0$ hyperbolic volume).
5. **TAU-S2a / TAU-S2b (`whitehead_satellite_jsj_vol_k2_k3`)**: $(\mathrm{Vol}(4_1) + 4G) / \hbar_{q_0}^k$ for $k \in \{2, 3\}$, where $4G$ is the Whitehead-pattern hyperbolic volume in $S^1 \times D^2$.
6. **TAU-S3a (`cabled_alexander_q0sq_dressed_k2`)**: $(\mathrm{Vol}(4_1) / \hbar_{q_0}^2) \cdot \Delta_{C_{2,7}(4_1)}(q_0^2)$.
7. **TAU-S3b (`cabled_alexander_ratio_k3`)**: $(\mathrm{Vol}(4_1) / \hbar_{q_0}^3) \cdot \bigl(\Delta_{C_{2,7}(4_1)}(q_0) / \Delta_{C_{2,5}(4_1)}(q_0)\bigr)$, plus evaluation of $\Delta_{C_{2,2k+1}(4_1)}(q_0^{2k+1})$ across $2k+1 \in \{3,5,7\}$ demonstrating the golden-ratio sign node between $w=2$ and $w=3,5$.
8. **TAU-S4a / TAU-S4b (`h6_markov_trace_cabled_4_1_T27`)**: Exact 80-dps Hoefsmit two-row Wedderburn Markov trace $\mathrm{tr}_M(\beta_{C_{2,2k+1}(4_1)})$ in $H_6(q_0)$ for $\beta_{C_{2,2k+1}(4_1)} = \mathrm{cable}_2((\sigma_1\sigma_2^{-1})^2)\,\sigma_1^{2k+1}$ ($2k+1 \in \{3,5,7\}$), testing its three-point `bend` invariant and the two scalings $(\mathrm{Vol}(4_1)/\hbar_{q_0}^3) \cdot |\mathrm{tr}_M(\beta_{C_{2,7}(4_1)})|$ vs $(\mathrm{Vol}(4_1)/\hbar_{q_0}^2) / |\mathrm{tr}_M(\beta_{C_{2,7}(4_1)})|$.
