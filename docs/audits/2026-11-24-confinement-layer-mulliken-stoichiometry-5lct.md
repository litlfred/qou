# Five-Layer Confinement Composition, Zero-Fit Layer-3 Mulliken/Hardness Atomic Benchmarks & Unimodular Toric Stoichiometry (`qou-5lct` / `qou-d9iv` / `Q-Gap-0`)

- **Date:** 2026-11-24 (salvaged & re-verified 2026-11-28 against Nov 27–28 base-ring, transcendental-boundary, aether-terminology, and proton-pin ratchets)
- **Beans:** `qou-5lct`, `qou-d9iv` (`Q-Gap-0`: 5-layer `ConfinementLayer` tower, adiabatic confinement ratios $\eta_k$, Layer-3 Fenchel–Legendre Mulliken electronegativity and Parr–Pearson hardness, and Layer-4 toric Diophantine stoichiometry)
- **Authoritative Lean 4 Modules:**
  - Upstream Reservoir foundation (`#9212` / `#9364`): `folio/quantum-observable-universe/lean/ToricConicOpt/ConfinementLayerTower.lean` (`0 sorry`, `0` custom axioms)
  - Canonical chapter-subgraph extension (this tranche): `folio/quantum-observable-universe/lean/QOU/Observations/ConfinementLayerMullikenStoichiometry.lean` (`0 sorry`, `0` custom axioms, `[propext, Classical.choice, Quot.sound]` only; division-free over `[CommRing K]`, `0` `base-ring-audit.py` and `transcendental-boundary-audit.py` flags)
- **80-dps Zero-Fit Probe & Stamped Witness:**
  - `computations/probes/confinement_layer_mulliken_stoichiometry_probe.py` (registered under `physical_proton` in `computations/q0_anchor_manifest.json`)
  - `computations/probes/confinement-layer-mulliken-stoichiometry.witness.json` (`mp.dps = 95` compute / `80` output, zero `float64`, strictly proton-pinned `q0Anchor = "proton"` per 2026-11-28 owner ruling; muon pin on hold until rederivation)

---

## 1. Scope & Non-Duplicative Convergence with `#9212`

Prior commit `86ea08a2ed7` (`PR #9212`, later migrated to the `ToricConicOpt` Reservoir library in `PR #9364`) landed the base record `ConfinementLayer`, single-step `promoteLayer`, adiabatic gap stability, shadow-slope algebra on abstract $E : \mathbb{N} \to K$, and the four 1D binomial kernel equivalences in `ToricConicOpt/ConfinementLayerTower.lean`, alongside `computations/probes/confinement_layer_tower_chem/confinement_layer_tower_chem_probe.py`.

Auditing that surface against the post-`#9360`/`#9366` derived coupling pipeline identified three concrete gaps closed in this tranche without duplicating any existing declaration:

1. **Derived QOU five-layer scales vs empirical inputs:** `confinement_layer_tower_chem_probe.py` evaluated the atomic Rydberg scale from the empirical CODATA fine-structure constant, took nuclear scales solely from AME-2020, and used a fixed `0.20 eV` literal for the hydrogen bond. Here every QOU scale across $\mathcal{L}_0 \to \mathcal{L}_1 \to \mathcal{L}_2 \to \mathcal{L}_3 \to \mathcal{L}_4$ is evaluated from $(m_e, q_0)$ strictly at the physical proton aether parameter pin (`q_at(80)`, `q0Anchor = "proton"`; the muon pin is on hold per the 2026-11-28 owner ruling until rederivation) using the four-topology Form-B coupling $\alpha_{\mathrm{FormB}}(q_0)$ (`PR #9360`, labelled *Conditional* per 2026-11-27 honest-labels ruling), the canonical nuclear scale $2 E_0^{\mathrm{ord0}}(q_0)$, and the $h_q^2 = (q_0 - q_0^{-1})^2$ hydrogen-bond suppression rung (`hbond_categorical_action.py`).
2. **Zero-fit theoretical atomic $(I_1, A_{\mathrm{ea}}, \chi_{\mathrm{M}}, \eta_{\mathrm{PP}})$ benchmarks across $\mathrm{H..Ne}$ ($Z = 1\ldots 10$):** `confinement_layer_tower_chem_probe.py` plugged experimental NIST $(I_1, A_{\mathrm{ea}})$ values into $\chi_{\mathrm{M}}$ and $\eta_{\mathrm{PP}}$, leaving the theoretical atomic ground-state envelope $E_Z(N)$ uncomputed. This probe constructs an 80-dps zero-parameter Roothaan–Slater–Condon variational solver (exact factorial Slater $R^k$ integrals, Russell–Saunders ground-term multiplet coefficients, uniform per-$Z$ split-valence Slater-type orbital basis) scaled solely by $\mathrm{Ry}_{\mathrm{FormB}}(q_0)$ and scores its predictions transparently against NIST.
3. **Division-free multi-step functorial composition, Fenchel–Legendre subgradient characterization, unimodular Smith certificates & Birch Hessian convexity in `QOU/Observations/`:** `ConfinementLayerMullikenStoichiometry.lean` imports `ToricConicOpt.ConfinementLayerTower` directly into the canonical `QOU.Observations` chapter subgraph and proves all theorems division-free over generic commutative rings (`[CommRing K]`) and strict ordered commutative rings (`[CommRing K] [LinearOrder K] [IsStrictOrderedRing K]`) per §7c (`qou-8318`).

---

## 2. Formalized Theorems in `QOU/Observations/ConfinementLayerMullikenStoichiometry.lean`

All declarations compile cleanly with `set_option autoImplicit false`, `0` warnings, `0` `lean-best-practices-lint.py` findings, `0` `base-ring-audit.py` (`field-class` / `field-tactic`) findings, `0` `transcendental-boundary-audit.py` findings, and `#print axioms` restricted to `[propext, Classical.choice, Quot.sound]`:

1. **`compositeMotifs`, `expandMotifs_comp`, `promoteLayer_two_step_charge_and_kernel`:** Proves functorial associativity of motif expansion across consecutive promotions $\mathcal{L}_0 \leadsto \mathcal{L}_1 \leadsto \mathcal{L}_2$ and transitive lifting of conserved charges and integer stoichiometric kernels (`L₂.A *ᵥ v = L₀.A *ᵥ expandMotifs (compositeMotifs motifs₀₁ motifs₁₂) v`). Verified numerically on $\mathcal{L}_1 (p, n) \leadsto \mathcal{L}_2 ({}^{12}\mathrm{C}, {}^1\mathrm{H}, {}^{16}\mathrm{O}) \leadsto \mathcal{L}_4 (\mathrm{C, H_2, O_2, CO, CO_2, H_2O, CH_4})$, certifying $\Delta Z_{\mathrm{tot}} = \Delta N_{\mathrm{nuc,tot}} = 0$ on every reaction generator.
2. **`five_layer_adiabatic_telescoping_product`:** Over any `[CommRing K] [LinearOrder K] [IsStrictOrderedRing K]`, proves the division-free telescoping identity $\Delta_4 = \Delta_0 \cdot (\eta_0 \eta_1 \eta_2 \eta_3)$ where $\Delta_{k+1} = \Delta_k \eta_k$, strict scale ordering $0 < \Delta_4 < \Delta_3 < \Delta_2 < \Delta_1 < \Delta_0$, and $0 < \eta_0 \eta_1 \eta_2 \eta_3 < 1$ whenever $0 < \Delta_0$ and each $\eta_k \in (0, 1)$.
3. **`twoMullikenElectronegativity` & `fenchel_subgradient_interval_iff_mulliken_hardness`:** Characterizes the discrete Fenchel–Legendre subdifferential $\{\mu \in K \mid E(N) + \mu \le E(N+1) \land E(N) - \mu \le E(N-1)\}$ over `[CommRing K] [LinearOrder K] [IsStrictOrderedRing K]` as $[\mu_-(N), \mu_+(N)] = [-I(N), -A_{\mathrm{ea}}(N)]$, proves doubled subgradient nonemptiness if and only if $0 \le \eta_{\mathrm{PP}}(N)$, and proves that $-2\chi_{\mathrm{M}}(N) = -(I(N) + A_{\mathrm{ea}}(N))$ lies at equal distance $\eta_{\mathrm{PP}}(N)$ from $2\mu_-(N)$ and $2\mu_+(N)$.
4. **`twoChargeTransferQuad` & `parr_pearson_charge_transfer_minimizer`:** Completes the square division-free on the doubled two-species quadratic charge-transfer energy $2\Delta E(\delta N) = 2(\chi_A - \chi_B)\,\delta N + (\eta_A + \eta_B)\,\delta N^2$ for $\eta_A + \eta_B > 0$: $(\eta_A + \eta_B)(2\Delta E(\delta N)) + (\chi_A - \chi_B)^2 = ((\eta_A + \eta_B)\delta N + (\chi_A - \chi_B))^2$, giving the unconditional Sanderson–Parr lower bound $-(\chi_A - \chi_B)^2 \le (\eta_A + \eta_B)(2\Delta E(\delta N))$ and global optimality at any stationary $(\eta_A + \eta_B)\delta N^* = \chi_B - \chi_A$.
5. **`two_shell_piecewise_hardness_kink`:** Over any `[CommRing K]`, proves on `twoShellEnergy E_core C₁ ε₁ ε₂` that at exact shell closure $N = C_1$ ($C_1 \ge 1$, modeling $C_1 \in \{2, 10, 18, 36\}$), $\eta_{\mathrm{PP}}(C_1) = \varepsilon_1 - \varepsilon_2$ and $2\chi_{\mathrm{M}}(C_1) = \varepsilon_1 + \varepsilon_2$, whereas strictly inside an unscreened open shell ($N \ge C_1 + 1$), $\eta_{\mathrm{PP}}(N) = 0$ and $2\chi_{\mathrm{M}}(N) = 2\varepsilon_2$.
6. **`cho_smith_normal_form_diag_1_1_2`:** Supplies explicit integer unimodular matrices `choSmithU ∈ GL₃(ℤ)` (with inverse `choSmithUInv`) and `choSmithV ∈ GL₇(ℤ)` (with inverse `choSmithVInv`) certifying $U \cdot A_{\mathrm{CHO}} \cdot V = \mathrm{diag}(1, 1, 2)$, isolating the prime-$2$ hydrogen-parity invariant factor in $\mathrm{coker}_{\mathbb{Z}}(A_{\mathrm{CHO}}) \cong \mathbb{Z}/2\mathbb{Z}$.
7. **`birch_hessian_quad_form_sum_sq_and_pos`:** Proves the exact weighted sum-of-squares identity $\xi^\top (A\,\mathrm{diag}(x)\,A^\top)\,\xi = \sum_{j=1}^M x_j \bigl(\sum_{e=1}^E A_{e,j}\xi_e\bigr)^2$ over any commutative ring and strict positivity $> 0$ for $x > 0$ whenever $A^\top \xi \ne 0$, certifying uniqueness and strict convexity of the finite-temperature Birch toric equilibrium.

---

## 3. 80-dps Numerical Findings (`confinement_layer_mulliken_stoichiometry_probe.py`)

### 3.1 Derived Five-Layer Scale Tower (Physical Proton Pin `q_at(80)`)

| Transition | Derived QOU lower scale $\Delta_k$ | Derived QOU next scale $\Delta_{k+1}$ | Adiabatic ratio $\eta_k$ | Base-$q_0$ depth $\log_{q_0}(\eta_k)$ |
|:-----------|:-----------------------------------|:--------------------------------------|:-------------------------|:--------------------------------------|
| $\mathcal{L}_0 \to \mathcal{L}_1$ | $m_p(q_0)/\alpha_{\mathrm{FormB}}(q_0) = 128.5771\,\mathrm{GeV}$ | $m_p(q_0) = 938.27208943\,\mathrm{MeV}$ | $\alpha_{\mathrm{FormB}}(q_0) = 7.29735256 \times 10^{-3}$ | $-47.1726$ |
| $\mathcal{L}_1 \to \mathcal{L}_2$ | $m_p(q_0) = 938.27208943\,\mathrm{MeV}$ | $2 E_0^{\mathrm{ord0}}(q_0) = 8.37196090\,\mathrm{MeV}$ (`12C/A`: $7.68014\,\mathrm{MeV}$) | $8.92274 \times 10^{-3}$ (`12C/A`: $8.18541 \times 10^{-3}$) | $-45.2498$ |
| $\mathcal{L}_2 \to \mathcal{L}_3$ | $2 E_0^{\mathrm{ord0}}(q_0) = 8.37196090\,\mathrm{MeV}$ | $\mathrm{Ry}_{\mathrm{FormB}}(q_0) = 13.605693129\,\mathrm{eV}$ (`+0.725 ppb` vs CODATA; Form-C `+0.043 ppb`) | $1.62515 \times 10^{-6}$ (`12C/A`: $1.77154 \times 10^{-6}$) | $-127.8012$ |
| $\mathcal{L}_3 \to \mathcal{L}_4$ | $\mathrm{Ry}_{\mathrm{FormB}}(q_0) = 13.605693129\,\mathrm{eV}$ | $2 h_q^2 E_{\mathrm{cov}}(\mathrm{OH}) = 0.4167205\,\mathrm{eV}$ (pure Bohr $\frac{2}{3}h_q^2\,\mathrm{Ry} = 0.3964361\,\mathrm{eV}$) | $3.06284 \times 10^{-2}$ (pure Bohr $2.91375 \times 10^{-2}$) | $-33.4192$ |

### 3.2 Zero-Fit Layer-3 Atomic Benchmarks ($\mathrm{H..Ne}$, $Z = 1\ldots 10$)

- **Exact relativistic reduced-mass protium ionization:** $I_1^{\mathrm{Dirac}}(\mathrm{H}; q_0) = 13.5984682\,\mathrm{eV}$ vs NIST $13.5984346\,\mathrm{eV}$ (**$+2.47\,\mathrm{ppm}$**, zero free parameters).
- **Zero-parameter 80-dps Roothaan–Slater–Condon variational solver (`H..Ne`):** Mean absolute percentage error across $Z = 1\ldots 10$ first ionization potentials is **$\sim 6.5\%$** (pure Hartree–Fock dynamical electron-correlation ceiling, zero empirical screening constants), reproducing every structural periodic invariant without fitting:
  1. Strict Perdew–Parr–Levy–Balduz convexity $\eta_{\mathrm{PP}}(Z) > 0$ for all $Z = 1\ldots 10$;
  2. Towering noble-gas Parr–Pearson hardness maxima at $\mathrm{He}$ ($23.45\,\mathrm{eV}$) and $\mathrm{Ne}$ ($19.63\,\mathrm{eV}$) followed by the $\mathrm{He} \to \mathrm{Li}$ shell-opening drop ($23.45 \to 5.33\,\mathrm{eV}$, $-1.18\%$ vs NIST $5.39\,\mathrm{eV}$);
  3. Both $2s^2 \to 2s^2 2p^1$ penetration ($I_1(\mathrm{Be}) > I_1(\mathrm{B})$) and Hund $2p^3 ({}^4S) \to 2p^4 ({}^3P)$ spin-pairing ($I_1(\mathrm{N}) = 13.98\,\mathrm{eV} > I_1(\mathrm{O}) = 11.83\,\mathrm{eV}$) inversions;
  4. Positive single-determinant electron affinities on open $2p$ acceptors $\mathrm{C}$ and $\mathrm{F}$, with fluorine achieving the maximum open-shell Period-2 Mulliken electronegativity.

### 3.3 Residual Gap Statement (Honest Anti-Fit Accounting)

Single-determinant Hartree–Fock omits opposite-spin Coulomb cusp correlation ($\sim 1.14\,\mathrm{eV}$ per paired shell, accounting for $\mathrm{He}$ $23.45$ vs $24.59\,\mathrm{eV}$, $\mathrm{Ne}$ $19.63$ vs $21.56\,\mathrm{eV}$, and near-degeneracy $2s^2 \leftrightarrow 2p^2$ static correlation in $\mathrm{Be}$ $7.98$ vs $9.32\,\mathrm{eV}$). Closing the remaining $1\text{--}1.9\,\mathrm{eV}$ electron-correlation residual from first principles requires multi-configurational / Hylleraas $r_{12}$-cusp or Hecke-braid pair-correlation operators rather than empirical Slater screening parameters.
