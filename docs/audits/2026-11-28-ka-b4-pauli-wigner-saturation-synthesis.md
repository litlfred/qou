# Exploratory Macroscopic Cluster-Model Comparison (`§3b-cond`, Unwired) Alongside the Ruled `T3` Valence Bound: Intra-Shell Pauli–Wigner Wenzl Cells ($b_2, b_3$), $\mathrm{SU}(4)$ Hankel Quartet Closure ($b_4$), FCC `(111)` Face Contacts & 3D Pauli Fermi Valley Across `2,542` AME2020 Nuclides (`qou-v2om`, `qou-gpb5`, `qou-sbn9`, `qou-d9iv`)

- **Date:** 2026-11-28 (salvaged & re-scoped from uncommitted 2026-11-24 `ws12-pr9180` worktree under `qou-d9iv` / `qou-s028`)
- **Branch:** `claude/ka-b4-pauli-wigner-saturation-probe-20261128`
- **Ruled Production Bond-Valence Reference (`PR #9710`):** [`folio/quantum-observable-universe/lean/QOU/MassTheory/NucleusBondValence.lean`](../../folio/quantum-observable-universe/lean/QOU/MassTheory/NucleusBondValence.lean) & [`docs/audits/2026-11-27-nucleus-bond-valence.md`](2026-11-27-nucleus-bond-valence.md)
- **Lean 4 Exploratory Cluster Formalization (`0 sorry`):** [`folio/quantum-observable-universe/lean/QOU/Nuclear/AlphaQuartetPauliWignerSaturation.lean`](../../folio/quantum-observable-universe/lean/QOU/Nuclear/AlphaQuartetPauliWignerSaturation.lean) (`0 sorry`, `0` custom axioms, division-free over generic `[CommRing R]` + `q : Rˣ` with `0` `base-ring-audit.py` and `transcendental-boundary-audit.py` flags)
- **Proton-Pinned 80-dps Exploratory Probe & Stamped Witness:** [`computations/probes/ka_b4_pauli_wigner_saturation_probe.py`](../../computations/probes/ka_b4_pauli_wigner_saturation_probe.py) $\to$ [`computations/probes/ka-b4-pauli-wigner-saturation.witness.json`](../../computations/probes/ka-b4-pauli-wigner-saturation.witness.json) (`OUTPUT_DPS = 80`, `COMPUTE_DPS = 125`, zero `float64`, zero fitted parameters, registered under `physical_proton` with `q0Anchor = "proton"`; muon pin on hold per 2026-11-28 owner ruling until rederivation)

---

## 0. Critical Applicability Gate: 2026-11-27 `T3` Colour-Valence Ruling (`PR #9710`)

> [!IMPORTANT]
> **Standing Owner Ruling (2026-11-27, `docs/coordination/owner-rulings.md` row 22; `QOU.MassTheory.NucleusBondValence`, `PR #9710`):**
> *"The nucleus bond count (gap G5) is fixed by the colour valence cap T3: each quark strand carries at most one inter-nucleon bond, and bonds carry one colour label, distinct at each nucleon (`3⌊A/2⌋` bonds, 1.5 per nucleon); V6 is not to be adopted without a corpus derivation."*

1. **Exact algebraic relation proved in `AlphaQuartetPauliWignerSaturation.lean`:**
   - At $A = 4m$ ($m$ disjoint $(2p, 2n)$ $K_4$ $\alpha$-quartets), `t3_valence_cap_eq_disjoint_quartet_internal_bonds` and `card_le_six_mul_of_t3_proper_colouring` prove directly from `QOU.MassTheory.NucleusBondValence.card_le_of_proper_colouring` that the ruled `T3` bound $3\lfloor 4m / 2 \rfloor = 6m$ coincides identically with the $6m$ internal edges of the $m$ disjoint $K_4$ tetrahedra (`6` internal bonds per quartet = `1.5` per nucleon, yielding `0.47` ($\alpha$) / `0.53` ($E_0$) of measured heavy-nucleus binding in `PR #9710`).
   - Thus, once nucleons close into internal $K_4$ $\alpha$-quartets, **all `T3` quark-strand colour valences are already saturated intra-quartet**. Subtracting twice those $(3/2)A$ internal edges from twice the $6A$ edges of a macroscopic `12`-coordinated FCC cluster lattice (`two_mul_fcc_sub_k4_external_bonds_eq`: $12A - 3A = 9A = 3 \cdot (3A)$) isolates the remaining $(9/2)A$ external inter-quartet nucleon-pair bridges (`3` bridges across each of $(3/2)A$ `(111)` faces).
2. **Strict `§3b-cond` Exploratory Framing (Unwired):**
   - Because additional inter-quartet `(111)` face contacts exceed the pairwise `T3` colour-valence cap unless derived from a higher-body / residual multipole mechanism on the full $3A$-strand Hecke word, the welded FCC `(111)` face-saturation models `S3..S5` below are recorded **strictly as an exploratory macroscopic cluster-model comparison (`§3b-cond`, unwired)** alongside the ruled `T3` baseline (`T3_ruled_valence_cap_pair`). Nothing here replaces the ruled `T3` bond count or touches any fenced production pipeline file (`ACCURACY.md`, `mass_table_comprehensive.py`, `per_observable_100x_status.py`).

---

## 1. Zero-Parameter Ingredients Evaluated Alongside Ruled `T3`

Every ingredient below is a zero-parameter function of $(m_e, q_0, m_{\pi^\pm})$ evaluated strictly at the physical proton aether parameter pin `q_at(190)` (`q0Anchor = "proton"`; the muon pin is on hold per the 2026-11-28 owner ruling until rederivation), using QOU's own model proton mass $m_p^{\mathrm{pred}}(q_0, m_e)$ and 4-topology Form-B $\alpha_{\mathrm{EM}}(q_0)$ (*Conditional*) in natural units $\hbar = c = 1$:

1. **Sub-Quartet Pauli–Wigner Wenzl Cells (`QOU.MassTheory.B3ExtensiveCellSumCarrier`, `#9373`):**
   On $A \in \{2, 3\}$, $\phi_1^{\mathrm{Wenzl}} = E_0^{\mathrm{twr}} / [2]_{q_0} = 2.102288\;\mathrm{MeV}$ (${}^2\mathrm{H}$, `-5.50%`) and $\phi_2^{\mathrm{Wenzl}} = \bigl(1 + \frac{q_0^2}{q_0^4 + q_0^2 + 1}\bigr) E_0^{\mathrm{twr}} = 5.616410\;\mathrm{MeV}$, giving $b_3^{\mathrm{Wenzl}} = \phi_2^{\mathrm{Wenzl}} - 2\phi_1^{\mathrm{Wenzl}} = +1.411835\;\mathrm{MeV}$ (`-1.01%` vs symmetric AME2020 `+1.426220 MeV`).
2. **Completed `(2p, 2n)` Quartet Closure (`QOU.Nuclear.SU4FourRowHankelNormalization`, `#9377`):**
   Closing four spin-isospin columns into $(3,3,3,3) \vdash 12$ under the $4 \times 4$ Cauchy–Binet Hankel $q$-Plancherel partition function $Z_{12}^{(4)}(q_0)$ gives single-quartet surprisal $B_4^{\mathrm{Hankel}}(q_p) = -E_0^{\mathrm{twr}}(q_p)\ln P_{(3,3,3,3)}^{(4)}(q_p) = \mathbf{27.954400\;\mathrm{MeV}}$ (`-1.206%` vs AME2020 `28.29566 MeV`), and Coulomb-restored strong quartet closure $B_4^{\mathrm{strong}} = B_4^{\mathrm{Hankel}} + E_C(2, 4) = \mathbf{28.883145\;\mathrm{MeV}}$.
3. **Exploratory Macroscopic FCC `(111)` Face Contacts vs Ruled `T3` Cap:**
   - Under the **ruled `T3` valence bound** (`T3_ruled_valence_cap_pair`), $3\lfloor A/2 \rfloor$ pair bonds saturate at $\frac{3}{2} b_2^{\log,\gamma\gamma} = \mathbf{4.292775\;\mathrm{MeV}/A}$ (`52.3%` of heavy-nucleus $B/A$, matching `PR #9710`'s `0.53` $E_0$ figure; or $\frac{1}{4} B_4^{\mathrm{Hankel}} = 6.9886\;\mathrm{MeV}/A$ in `S1` before Coulomb), leaving the post-`T3` macroscopic gap quantified in `PR #9710`.
   - Under the **exploratory `§3b-cond` cluster comparison** (`AlphaQuartetPauliWignerSaturationHypothesis`), assigning each surface-corrected inter-quartet `(111)` face $M_{\mathrm{face}}(A) = \max\bigl(0, \frac{3}{2}A - 3 A^{2/3}\bigr)$ (which vanishes identically for $A \le 8$) the 3-nucleon Wenzl triangle weight $\phi_2^{\mathrm{Wenzl}}$ yields $a_V^{\mathrm{strong}} = B_4^{\mathrm{strong}}/4 + \frac{3}{2}\phi_2^{\mathrm{Wenzl}} = \mathbf{15.645401\;\mathrm{MeV}}$ and $a_S^{\mathrm{Wenzl}} = 3\phi_2^{\mathrm{Wenzl}} = \mathbf{16.849229\;\mathrm{MeV}}$.
4. **Continuous Wigner Parabola + 3D Pauli Fermi Asymmetry + Nilsson–Strutinsky Shells (`#9367`, `92497ed7b76`):**
   Projecting onto $w_{\mathrm{iso}}(Z, N) = 4ZN/A^2 = 1 - ((N - Z)/A)^2$, subtracting the 3D Fermi-gas Pauli kinetic asymmetry $\Delta T_{\mathrm{Pauli}}(Z, N)$ ($\varepsilon_F / 3 = \mathbf{11.682291\;\mathrm{MeV}}$), adding deuteron-scale pairing $\pm \phi_1^{\mathrm{Wenzl}} / \sqrt{A/4}$, and subtracting FCC Coulomb $E_C(Z, A)$ (`S4`, plus `#9367` order-4 Hermite–Strutinsky shell stabilization in `S5`) tests whether the missing post-`T3` bulk binding in heavy nuclei matches the `(111)` inter-quartet triangle + Pauli Fermi scale.

---

## 2. Division-Free `[CommRing R]` Theorems (`QOU.Nuclear.AlphaQuartetPauliWignerSaturation`)

All declarations compile with `set_option autoImplicit false`, `0 sorry`, `0` custom axioms (`[propext, Classical.choice, Quot.sound]` only), `0` `lean-best-practices-lint.py` warnings, and **`0` `base-ring-audit.py` / `transcendental-boundary-audit.py` flags**:

1. **Sub-Quartet Preservation, $\alpha$-Extensivity & Isobaric Sawtooth (`[CommRing R]`):**
   `quartetClosed_deuteron_eq`, `quartetClosed_triton_eq`, `quartetClosed_he3_eq`, `quartetClosed_he4_eq`, `quartetClosed_b3_eq`, `quartetClosed_b4_eq`, `quartetClosed_b4_jump`, `quartetClosed_alpha_plus_excessPairs`, `quartetClosed_alpha_mul`, `quartetClosed_isobar_odd_to_even_jump`.
2. **Ruled `T3` Valence Bound vs Exploratory FCC `(111)` Coordination (`[CommRing R]` & `q : Rˣ`):**
   `t3_valence_cap_eq_disjoint_quartet_internal_bonds`, `card_le_six_mul_of_t3_proper_colouring` (invoking `QOU.MassTheory.NucleusBondValence.card_le_of_proper_colouring`), `two_mul_fcc_sub_k4_external_bonds_eq`, `qIntUnit_three_mul_sq`, `qSimplex_two_clearing_eq`, `twoInterQuartetFaceCountCube_factored`, `twoInterQuartetFaceCountCube_at_two`, `twoInterQuartetFaceCountCube_pos_of_gt_two`.
3. **Division-Free `A²`-Cleared Wigner Isospin & Isobaric Valley Concavity (`[CommRing R]`):**
   `wignerIsoNumerator_eq_sum_sq_sub_asym_sq`, `wignerIsoNumerator_le_sum_sq`, `isobaric_binding_second_diff_eq`, `isobaric_binding_second_diff_neg`, `isobaric_beta_step_eq`, `isobaric_beta_exothermic_iff`.
4. **Exploratory `§3b-cond` Hypothesis Class & Consistency Witness (`[CommRing R]`):**
   `AlphaQuartetPauliWignerSaturationHypothesis`, `trivialModel` (Pattern 3.3 `def`, non-instance), `composite_nuclear_saturation_identity`, and `alpha_decay_qValue_shell_jump`.

---

## 3. Proton-Pinned 80-dps Scale Map (`q_at(190)`, `q0Anchor = "proton"`)

*(Muon pin is on hold per the 2026-11-28 owner ruling until rederivation.)*

| Quantity | Closed-Form Expression | Physical Proton Pin ($q_p$) | Role / Epistemic Scope |
|---|---|---:|---|
| Aether parameter $q_0$ | `q_at(190)` (`physical_proton`) | `1.109978582751381` | Physical proton pin (`Q0_OK`) |
| Form-B $\alpha_{\mathrm{EM}}^{-1}(q_0)$ | 4-topology Schwinger cubic (`#9360`) | `137.0359991269509` | Conditional (`#9443`) |
| Model proton mass $m_p^{\mathrm{pred}}(q_0)$ | $2 m_\mu(q_0) F_{\mathrm{Bor}}(q_0) - 12 m_e$ | `938.2720894273239 MeV` | Zero CODATA $m_p$ input |
| Tower scale $E_0^{\mathrm{twr}}(q_0)$ | $m_e / (q_0(q_0 - 1)(1 - \hbar_q^2))$ | `4.227483355629031 MeV` | Ruled tower scale (`#9424`) |
| Ruled `T3` asymptotic pair cap | $\frac{3}{2} E_0^{\mathrm{twr}} \ln(1 / z_{\gamma\gamma})$ (`PR #9710`) | `4.292775210830215 MeV/A` | **Ruled `G5` valence cap (`3⌊A/2⌋` bonds)** |
| Sub-quartet pair $\phi_1^{\mathrm{Wenzl}}$ | $E_0^{\mathrm{twr}} / [2]_{q_0}$ | `2.102287504456460 MeV` | ${}^2\mathrm{H}$ cell (`-5.50%` vs `2.2246 MeV`) |
| Sub-quartet triangle $\phi_2^{\mathrm{Wenzl}}$ | $\bigl(1 + \frac{q_0^2}{q_0^4+q_0^2+1}\bigr) E_0^{\mathrm{twr}}$ | `5.616409574519008 MeV` | 3-nucleon Wenzl weight |
| 3-body cumulant $b_3^{\mathrm{Wenzl}}$ | $\phi_2^{\mathrm{Wenzl}} - 2\phi_1^{\mathrm{Wenzl}}$ | `+1.411834565606088 MeV` | `-1.01%` vs AME `+1.426220 MeV` |
| Hankel quartet $B_4^{\mathrm{Hankel}}$ | $-E_0^{\mathrm{twr}} \ln P_{(3,3,3,3)}^{(4)}(q_0)$ (`#9377`) | `27.95440002447971 MeV` | Net ${}^4\mathrm{He}$ (`-1.206%` vs `28.2957 MeV`) |
| Strong quartet $B_4^{\mathrm{strong}}$ | $B_4^{\mathrm{Hankel}} + E_C(2,4)$ | `28.88314500671300 MeV` | Bare strong $[1^4]$ quartet closure |
| Exploratory volume $a_V^{\mathrm{strong}}$ | $B_4^{\mathrm{strong}}/4 + \frac{3}{2}\phi_2^{\mathrm{Wenzl}}$ | `15.64540061345676 MeV` | Exploratory `(111)` cluster comparison (`§3b-cond`) |
| Exploratory surface $a_S^{\mathrm{Wenzl}}$ | $3\phi_2^{\mathrm{Wenzl}}$ | `16.84922872355702 MeV` | Exploratory `(111)` cluster comparison (`§3b-cond`) |
| FCC Coulomb constant $c_{\mathrm{coul}}$ | $\frac{2}{5}(4\pi\sqrt{2}/3)^{1/3}\alpha_{\mathrm{EM}} m_{\pi^\pm}$ | `0.737145380903657 MeV` | Pion-Compton FCC spacing |
| 3D Pauli Fermi $\varepsilon_F / 3$ | $\frac{2}{27}(9\pi^4/2)^{1/3} m_{\pi^\pm}^2 / m_p^{\mathrm{pred}}$ | `11.68229098273183 MeV` | Kinetic symmetry coefficient |
| ${}^{208}\mathrm{Pb}$ Strutinsky $\Delta B_{\mathrm{Strut}}$ | $(\delta B_{82} + \delta B_{126})\hbar\omega_0(208)$ | `+13.8695746383050 MeV` | `#9367` Dirac Nilsson shell closure |

---

## 4. Ruled `T3` Baseline Alongside Exploratory Cluster Comparison (`2,542` AME2020 Nuclides, Proton Pin)

| Model | Epistemic Status | `2,542` Nuclides MAE ($B/A$) | `2,542` Nuclides Med $|\Delta B|/B$ | `1,009` $\beta^-$ Exo (`scored` / `Leg` / `CODATA`) | `1,009` $\beta^-$ Med Err (`Leg`) | `1,051` $\alpha$ Exo | `1,051` $\alpha$ Med Err |
|---|---|---:|---:|---:|---:|---:|---:|
| `ACCURACY.md` 1D chain | Production (`A - 1` bonds) | `~5.16 MeV/A` | `68.93%` | `0 / — / —` | `142.4%` (`scored`) | `1,049 / 1,051` | `320.3%` |
| **`T3_ruled_valence_cap_pair` (`PR #9710`)** | **Ruled `G5` cap (`3⌊A/2⌋` bonds)** | `3.805 MeV/A` | `47.73%` | `1009 / 1009 / 1009` (no $E_C$/$T_z$) | `85.45%` | `35 / 1,051` | `100.0%` |
| `S0_wenzl_intra_only` (`#9373` `M4`) | Disjoint intra-shell | `4.306 MeV/A` | `53.43%` | `1009 / 1009 / 1009` | `82.37%` | `15 / 1,051` | `100.0%` |
| `S1_discrete_quartet_closed_coulomb` | Disjoint `K_4` (= `T3` at $A=4m$) + $E_C$ | `5.303 MeV/A` | `67.99%` | `521 / 540 / 543` | `143.3%` | `1,051 / 1,051` | `615.8%` |
| `S2_su4_pauli_triangle_3tree` (`#9377`) | Exploratory 3-tree + $E_C$ | `1.960 MeV/A` | `26.08%` | `174 / 189 / 192` | `214.5%` | `1,051 / 1,051` | `154.0%` |
| `S3_welded_hankel_strong_fcc_fermi_pair` | Exploratory `§3b-cond` (unwired) | `0.2263 MeV/A` | `2.961%` | `895 / 928 / 930` | `26.46%` | `1,029 / 1,051` | `21.68%` |
| `S4_welded_hankel_net_fcc_fermi_pair` | Exploratory `§3b-cond` (unwired) | `0.0881 MeV/A` | `0.8116%` | `907 / 938 / 941` | `25.73%` | `1,029 / 1,051` | `21.12%` |
| `S5_welded_hankel_net_nilsson_strutinsky` | Exploratory `§3b-cond` + `#9367` shells | `0.0996 MeV/A` | `0.9776%` | `890 / 922 / 927` | `34.02%` | `979 / 1,051` | `45.27%` |

---

## 5. Honest Scope Boundaries, Limitations & Bean Disposition

1. **Relationship to Ruled `T3` (`QOU.MassTheory.NucleusBondValence`, `PR #9710`):**
   Comparing `S1` (disjoint $K_4$ quartets, whose $6(A/4)$ internal bonds saturate the ruled `T3` valence cap at $A = 4m$, giving `MAE = 5.303 MeV/A` after Coulomb) against `S4` (`MAE = 0.0881 MeV/A`, `0.8116%` median across `2,542` nuclides) isolates quantitatively that closing the remaining $\sim 53\%$ heavy-nucleus binding gap (`G5`) within the ruled `T3` framework requires deriving an effective inter-quartet / multi-body residual operator from the $3A$-strand Hecke algebra rather than asserting ad-hoc higher strand valence (`V6`).
2. **Spherical Strutinsky Over-Modulation on Deformed Actinide $Q_\alpha$ (`S5` vs `S4`):**
   Spherical Nilsson–Strutinsky shell stabilization (`S5`) improves mid-shell binding (`0.0458 MeV/A`, `0.44%` median on $A = 57\ldots 150$; ${}^{56}\mathrm{Fe}$ `-0.24%`, ${}^{62}\mathrm{Ni}$ `+0.18%`, ${}^{120}\mathrm{Sn}$ `+0.016%`, ${}^{208}\mathrm{Pb}$ `-0.85%`) and reproduces the $N = 128 \to 126$ magic jump (`+4.22 MeV` from ${}^{210}\mathrm{Po}$ to ${}^{212}\mathrm{Po}$ vs AME `+3.55 MeV`), while over-modulating open-shell prolate actinides ($\beta_2 \approx 0.20\text{--}0.28$).
3. **Bean Disposition:**
   - `Refs qou-d9iv`, `Refs qou-v2om`, `Refs qou-gpb5`, `Refs qou-sbn9`: salvages the division-free `[CommRing R]` Lean module and proton-pinned 80-dps exploratory comparison probe cleanly onto `origin/main`; open research beans remain open per Rule 13a pending a $3A$-strand derivation compatible with the ruled `T3` valence cap.
