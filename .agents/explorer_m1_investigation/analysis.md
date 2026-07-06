# Analysis Report: Substrate Parameter and Calibration Violations

This report details the findings from the investigation of the Quantum Observable Universe (QOU) codebase and documentation regarding constraints:
1. **C1_Q_IDENTITY**: $q$ must be treated as a local dynamic physical field/section $q(p)$, not an unobservable background parameter, invisible ether, or rigid global constant.
2. **C2_3_CALIBRATION_POINTS**: Calibrations must be framed as local physical fields derived from topological traces evaluated at local $q(p)$, not as universal rigid constants.
3. **C3_CAL2_VACUUM_LOCK**: The muon-to-electron mass ratio ($m_\mu/m_e$, CAL-2/CAL-1) must anchor the vacuum expectation value $q_0 \approx 1.1097$.

---

## 1. Markdown Documentation Audit (content/)

### 1.1 Calibration Mismatch in `three-calibration-inputs.md`
- **File**: `content/quantum-observable-universe/mass-theory/three-calibration-inputs.md`
- **Lines**: 8–13
- **Observation**: The table at the top of the file contradicts the rest of the text and the definition index by listing decay widths ($\mathfrak{D}_\beta, \mathfrak{D}_\pi$) as calibrations, whereas the text and Wedderburn table below it list $m_e$, $m_\mu/m_e$, and $m_{\pi^\pm}$.
- **Proposed Replacement**:
  Update the table at the top of the file to align with the Wedderburn homological trace mapping (lines 99–103).

  **Target Content (Lines 8-13):**
  ```markdown
  | ID | Observable | Measurement | What it fixes | Jet order |
  |----|-----------|-------------|--------------|-----------|
  | **CAL-1** | $m_\mathfrak{e}$ | electron mass (Penning trap) | leptonic mass scale | $h^0$ |
  | **CAL-2** | $\mathfrak{D}_\beta$ | neutron $\beta$-decay width ($\tau_n$) | substrate $q_0$ via $Q_\beta \to$ substrate identity | $h^2$ |
  | **CAL-3** | $\mathfrak{D}_\pi$ | pion decay width ($\tau_\pi$) | meson mass scale $m_\pi$; independent of $(m_\mathfrak{e}, q_0)$ | $h^3$ |
  ```

  **Proposed Replacement:**
  ```markdown
  | ID | Observable | Measurement | What it fixes | Jet order |
  |----|-----------|-------------|--------------|-----------|
  | **CAL-1** | $m_e$ | electron mass (Penning trap) | leptonic mass scale (std channel) | $h^0$ |
  | **CAL-2** | $m_\mu/m_e$ | muon-to-electron mass ratio | substrate $q_0$ (alt channel) | $h^2$ |
  | **CAL-3** | $m_{\pi^\pm}$ | pion mass | meson mass scale (sym channel) | $h^3$ |
  ```

---

## 2. Codebase Calibration and Anchor Violations

### 2.1 Re-Pinning in `constants.py` (C3_CAL2_VACUUM_LOCK Violation)
- **File**: `tools/qou-substrate/python/qou_substrate/constants.py`
- **Lines**: 8–15, 46–77
- **Observation**: The file describes and executes a re-pinning of $q$ from $m_p/m_e$ (proton mass ratio) instead of $m_\mu/m_e$ (muon mass ratio). This violates **C3_CAL2_VACUUM_LOCK**, which requires the muon-to-electron mass ratio to anchor the vacuum expectation value $q_0$.
- **Proposed Replacement**:
  Revert the anchor to $m_\mu/m_e$ as implemented in the older `q_parameter.py`.

  **Target Content (Lines 46-77):**
  ```python
  def _solve_q_proton_f64(mp_me, vol, iters=80):
      ...
      return q

  Q         = _solve_q_proton_f64(MASS_RATIO_P_E, VOL_FIGURE_EIGHT)
  ```

  **Proposed Replacement:**
  ```python
  # Anchor q_0 directly to the muon-to-electron mass ratio (CAL-2 / CAL-1)
  HBAR_Q_SQ = VOL_FIGURE_EIGHT / MASS_RATIO_MU_E
  HBAR_Q    = math.sqrt(HBAR_Q_SQ)
  Q         = 1.0 / (1.0 - HBAR_Q)
  ```

---

## 3. Hardcoded / Stale Literal Specializations (C1_Q_IDENTITY & C2_3_CALIBRATION_POINTS Violations)

Multiple Python and Rust files hardcode $q_0$ as a fixed float value, violating **C1_Q_IDENTITY** (failing to treat $q$ as a dynamic field section) and **C2_3_CALIBRATION_POINTS** (treating calibrations as universal constants). Furthermore, they exhibit value drift (e.g. `1.1097`, `1.10998`, `1.1097090249`, `1.1099785827513808`, etc.).

### 3.1 Python Files

| File Path | Line(s) | Stale/Hardcoded Literal | Proposed Replacement |
|-----------|---------|------------------------|----------------------|
| `simulations/q_double_slit.py` | 18 | `M_MU_M_E_RATIOS = [1.0, 1.05, 1.1097, 1.2, 1.5]` | Import from `qou_substrate.constants` or define as evaluations of the local field section |
| `computations/e_hartree_mechanism_b_probe.py` | 67 | `q0 = mp.mpf("1.1099785827513808...")` | `from qou_substrate.constants import Q_50_DIGIT_STR` |
| `computations/e_hartree_round19_dressed_scalar_block.py` | 98 | `Q0 = "1.1099785827513808..."` | `from qou_substrate.constants import Q_50_DIGIT_STR` |
| `computations/e_hartree_round20_trace_ratio.py` | 82 | `Q0 = "1.1099785827513808..."` | `from qou_substrate.constants import Q_50_DIGIT_STR` |
| `computations/e_hartree_round22_arch_bridge.py` | 78 | `Q0 = "1.1099785827513808..."` | `from qou_substrate.constants import Q_50_DIGIT_STR` |
| `computations/e_hartree_round23_normalization.py` | 77 | `Q0 = "1.1099785827513808..."` | `from qou_substrate.constants import Q_50_DIGIT_STR` |
| `computations/e_hartree_round24_molecular_reuse.py` | 79 | `Q0 = 1.1099785827513808...` | `from qou_substrate.constants import Q_50_DIGIT_STR` |
| `computations/hbond_categorical_action.py` | 58 | `Q0 = 1.1099780333553254` | `from qou_substrate.constants import Q` |
| `computations/hbond_vdw_energy_ladder.py` | 53 | `Q0 = 1.1099780333553254` | `from qou_substrate.constants import Q` |
| `computations/hbond_vdw_sdp.py` | 62 | `Q0 = 1.1099780333553254` | `from qou_substrate.constants import Q` |
| `computations/homflypt_reference_qa.py` | 86 | `_Q0_STR = "1.1097"` | `from qou_substrate.constants import Q_50_DIGIT_STR` |
| `computations/inter_nucleon_linked_channel.py` | 58 | `Q0_STR = "1.109978595612202..."` | `from qou_substrate.constants import Q_50_DIGIT_STR` |
| `computations/knot_operator_census_group_actions.py` | 34 | `Q0 = mp.mpf("1.10998")` | `from qou_substrate.constants import Q` |
| `computations/option_e_canonical_reeb_v5.py` | 41 | `Q_0 = mpf("1.1097090249")` | `from qou_substrate.constants import Q` |
| `computations/option_e_deuteron_param_free_residual.py` | 33 | `Q_0 = mpf("1.1097090249")` | `from qou_substrate.constants import Q` |
| `computations/option_e_v6_combined_canonical.py` | 41 | `Q_0 = mpf("1.1097090249")` | `from qou_substrate.constants import Q` |
| `computations/option_e_v7_involution_aware.py` | 41 | `Q_0 = mpf("1.1097090249")` | `from qou_substrate.constants import Q` |
| `computations/option_e_v8_hecke_involution_isospin_mirror.py` | 38 | `Q_0 = mpf("1.1097090249")` | `from qou_substrate.constants import Q` |
| `computations/option_e_v9_all_symmetries.py` | 36 | `Q_0 = mpf("1.1097090249")` | `from qou_substrate.constants import Q` |
| `computations/probe_isospin_mirror_v9_generalization.py` | 42 | `Q_0 = D("1.1097090249")` | `from qou_substrate.constants import Q` |
| `computations/rho_w_crystal_vertex_trace.py` | 66 | `Q0_STR = "1.10997858275138..."` | `from qou_substrate.constants import Q_50_DIGIT_STR` |
| `computations/rt_c23_singlet_sign_core.py` | 67 | `Q0 = "1.10997858275138..."` | `from qou_substrate.constants import Q_50_DIGIT_STR` |
| `computations/rt_identity_chain_consolidation.py` | 66 | `Q0 = "1.10997858275138..."` | `from qou_substrate.constants import Q_50_DIGIT_STR` |
| `computations/yekutieli_mi_k3_h6_scaffold.py` | 130 | `q_0 = mpf("1.10970000000")` | `from qou_substrate.constants import Q` |

### 3.2 Rust Files (`tools/hecke-engine/`)

| File Path | Line(s) | Stale/Hardcoded Literal | Proposed Replacement |
|-----------|---------|------------------------|----------------------|
| `tools/hecke-engine/src/gram.rs` | 32 | `pub const Q_0: f64 = 1.1099785955541805;` | Dynamically pass or compute from constants module |
| `tools/hecke-engine/src/bin/joint_tower_sdp.rs` | 38, 563 | `1.1097` | Retrieve value dynamically from standard substrate config |
| `tools/hecke-engine/src/bin/r5_5_diagnose_h5.rs` | 41 | `let q = 1.1097;` | Retrieve value dynamically from standard substrate config |
| `tools/hecke-engine/src/bin/r5_5_minimal_h5.rs` | 37 | `let q = 1.1097;` | Retrieve value dynamically from standard substrate config |
| `tools/hecke-engine/src/bin/r5_5_scale_test.rs` | 14 | `let q = 1.1097;` | Retrieve value dynamically from standard substrate config |
| `tools/hecke-engine/src/bin/r5_6_smoke.rs` | 72 | `let q = 1.1097;` | Retrieve value dynamically from standard substrate config |
| `tools/hecke-engine/src/sdp_per_block.rs` | 605, 651 | `let q = 1.1097;` | Retrieve value dynamically from standard substrate config |
| `tools/hecke-engine/src/sdp_solver_clarabel.rs` | 429, 443 | `let q = 1.1097;` | Retrieve value dynamically from standard substrate config |
