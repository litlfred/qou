# Handoff Report: Substrate Parameter and Calibration Violations Audit

## 1. Observation
We conducted a comprehensive read-only search across the repository.
- **Inconsistent Calibration definitions**:
  - `content/quantum-observable-universe/mass-theory/three-calibration-inputs.md` lines 8-13 lists:
    ```markdown
    | **CAL-1** | $m_\mathfrak{e}$ | electron mass (Penning trap) | leptonic mass scale | $h^0$ |
    | **CAL-2** | $\mathfrak{D}_\beta$ | neutron $\beta$-decay width ($\tau_n$) | substrate $q_0$ via $Q_\beta \to$ substrate identity | $h^2$ |
    | **CAL-3** | $\mathfrak{D}_\pi$ | pion decay width ($\tau_\pi$) | meson mass scale $m_\pi$; independent of $(m_\mathfrak{e}, q_0)$ | $h^3$ |
    ```
    This table contradicts the rest of the file itself. Specifically, the Wedderburn trace mapping table (lines 99-103) lists:
    - `alt`: `CAL-2: m_mu/m_e \mapsto q_0`
    - `std`: `CAL-1: m_e`
    - `sym`: `CAL-3: m_{\pi^{\pm}}`
    The top table uses neutron decay width and pion decay width, which is mismatched.

- **Substrate Anchor Re-Pinning (C3_CAL2_VACUUM_LOCK Violation)**:
  - `tools/qou-substrate/python/qou_substrate/constants.py` contains a Newton solver `_solve_q_proton_f64(...)` (lines 46-77) that anchors the value of `q` based on the proton mass ratio `MASS_RATIO_P_E` ($m_p/m_e$).
  - This contradicts the older implementation `q_parameter.py` (which correctly computes `q` from the muon mass ratio `MASS_RATIO_MU_E` ($m_\mu/m_e$) via the closed-form relation $\hbar_q^2 = \mathrm{Vol}(4_1) / (m_\mu/m_e)$), violating **C3_CAL2_VACUUM_LOCK** which locks $q_0 \approx 1.1097$ to the muon mass ratio.

- **Hardcoded/Stale Substrate Literal Value Drift**:
  - Multiple Python and Rust source code files define hardcoded literals for $q_0$ rather than importing the canonical value or evaluating symbolically before specialization:
    - `simulations/q_double_slit.py` line 18 uses: `M_MU_M_E_RATIOS = [1.0, 1.05, 1.1097, 1.2, 1.5]`
    - `computations/option_e_v9_all_symmetries.py` line 36 uses: `Q_0 = mpf("1.1097090249")` (stale muon literal)
    - `computations/e_hartree_mechanism_b_probe.py` line 67 uses: `q0 = mp.mpf("1.1099785827513808075916690956107688798744991218736")` (proton pin literal)
    - `tools/hecke-engine/src/bin/joint_tower_sdp.rs` line 38 uses: `default_value_t = 1.1097`
    - `tools/hecke-engine/src/gram.rs` line 32 uses: `pub const Q_0: f64 = 1.1099785955541805;`
    These hardcoded values drift across scripts, violating the principles of **C1_Q_IDENTITY** (failing to treat $q$ as a dynamic field section) and **C2_3_CALIBRATION_POINTS** (treating calibrations as universal rigid constants).

## 2. Logic Chain
- **Table Inconsistency**: The table on lines 8-13 of `three-calibration-inputs.md` explicitly lists decay widths as calibrations. This contradicts the description at lines 99-103 (which maps Wedderburn blocks to $m_\mu/m_e$ and $m_{\pi^\pm}$) and definition indices. Correcting this table to reflect the true calibrations ($m_e$, $m_\mu/m_e$, $m_{\pi^\pm}$) restores consistency.
- **Anchor Violation**: C3_CAL2_VACUUM_LOCK requires the ratio CAL 2 / CAL 1 ($m_\mu/m_e$) to anchor $q_0 \approx 1.1097$. The implementation in `constants.py` re-pins $q$ to the proton mass ratio ($m_p/m_e$), violating this constraint. Reverting this module to use the muon-to-electron mass ratio as the anchor fixes the violation.
- **Constant Specialization Violations**: C1_Q_IDENTITY and C2_3_CALIBRATION_POINTS require $q$ and calibrations to be framed as local fields evaluated at local $q(p)$, rather than universal constants. Hardcoding specific floats (like `1.1097` or `1.10998`) directly inside the computation scripts violates these constraints. Replacing them with configuration imports or symbolic evaluations removes hardcoding and fixes drift.

## 3. Caveats
- The codebase was not executed dynamically to test structural effects after applying the proposed changes.
- It is assumed that the Wedderburn block mapping ($m_e$, $m_\mu/m_e$, $m_{\pi^\pm}$) defined in the text is the intended model.

## 4. Conclusion
The QOU codebase and documentation contain structural inconsistencies in calibration definitions, a violation of the $q$-anchoring rule (re-pinning to the proton mass ratio), and hardcoded/stale literals for $q_0$ that drift across files. Actionable modifications are documented in `analysis.md`.

## 5. Verification Method
- **Code verification**: Run grep command to ensure no hardcoded float literals of $q$ remain in Python/Rust source files (e.g. `grep -rn "1.1097"`).
- **Test execution**: Run `cargo test` in `tools/hecke-engine/` and Python unit tests to ensure that the modifications do not break compilation or analytical calculations.
