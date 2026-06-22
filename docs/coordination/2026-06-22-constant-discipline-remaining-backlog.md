# Constant-discipline remaining backlog (2026-06-22)

Coordination ledger for the **tail** of the CODATA/q₀ constant-discipline
cleanup. The value-preserving mechanical scope is **done** (merged PRs
#2542, #2563, #2565, #2581, #2587, #2595, #2602 + the sibling cluster-A q₀
migration `74d93256`). What remains is **owner-sequenced / value-changing**
and is tracked here so the active q₀ sweep and the owner pick it up rather
than racing it on separate branches.

## Item A — q₀ cluster-B (muon anchor) + `Q_MUON` accessor

- **Source:** `docs/audits/2026-06-21-q0-hardcoded-constant-census.md` cluster B
  (6+ files hardcoding the muon-anchor q₀ `1.10997859555418…`).
- **Recipe:** add a `Q_MUON` accessor to `tools/qou-substrate/python/qou_substrate/constants.py`
  (re-exported via `q_parameter`), value = the canonical muon derivation
  `q = 1/(1 − ℏ_q)` with `ℏ_q² = Vol(4₁)/(m_μ/m_e)`; route the cluster-B
  files' bare-decimal q₀ to it. Confirm each is genuinely in the
  canonical-CAL-2 (muon) layer first (two-layer convention).
- **Why deferred:** same package + files as the active cluster-A sweep;
  collision-prone; witness-churning. **Fold into the q₀ sweep.**

## Item B — Class-3a E₀ witness refresh (from PR #2581)

- **Files:** `pn_alpha_lp_dual.py`, `multi_level_jet_sum.py`,
  `probes/adjacent_vs_full_probe.py` (the `crt_markov.py` E₀ anchor has no
  witness). PR #2581 changed `E₀ = m_p / m_proton_tower` to full-precision
  `M_P_MEV_VALIDATION`; the committed witnesses were **not** regenerated.
- **Status (verified 2026-06-22):** regeneration is clean (`pyhecke_native`
  0.9.0 gives the canonical proton-anchor q₀ `1.10997859555733…`); the diff
  is the expected E₀ +9.4e-8 **plus** a q₀ refresh muon-B `…5541805` →
  proton-C `…5573347` (the committed witnesses were on the stale anchor).
- **Why deferred:** that q₀ refresh is exactly the cluster-A/B witness churn
  the sweep owns; regenerating on a side branch conflicts. **Fold into the
  q₀ sweep** (run the 3 scripts, commit refreshed witnesses there).

## Item C — `46ke` hidden-CODATA precision tail (P31 = 21)

Remaining P31 literals are **not** value-preserving routes:

| Literal | ×N | Why not routable value-preservingly |
|---|--:|---|
| `938.27208816` | 8 | dict-string isotope tables (string→number changes JSON), standalone-by-design `meson_mass_from_hecke`, display |
| `206.7682830` | 7 | `# noqa: P31` display lines, source def, standalone |
| `0.78233` | 3 | truncated Q_β (≠ `Q_NEUTRON_MEV` 0.78233341) |
| `0.51099895` | 2 | truncated m_e (≠ `M_E_MEV` 0.51099895069) |
| `939.56542` | 1 | truncated m_n (≠ `M_N_MEV_VALIDATION` 939.56542052) |

- **Recipe (owner precision-call):** for the truncated trio, decide
  per-occurrence: bump to the full-precision registry constant (value
  change ~1e-9–4e-6, refreshes witnesses) **or** leave as an intentional
  display literal with `# noqa: P31`. The dict-string tables need a
  string-keyed registry accessor to route without changing JSON
  serialization.
- **Why deferred:** every option changes values or serialization → owner
  precision-call.

## Item D — `j1hg` genuine 23 (over-count `Z·m_p + N·m_n`)

- **Files:** the 23 GENUINE rows in
  `docs/audits/2026-06-22-overcount-3input-triage.md` (m_n consumed in a
  `Z·m_p + N·m_n` constituent sum or `rho_K` formula).
- **The fork (owner decision):**
  - **Honest fix:** derive `m_n` from the **framework's q₀-derived Q_β**
    (`Q_β = m_e·|q₀²−2q₀−1|(q₀+1)/(2q₀³)`), i.e. `m_n = m_p + Q_β_derived + m_e`.
    This is the true 3-input canonical scheme but **value-changing (~0.17%)**
    — refreshes every dependent witness.
  - **Value-preserving relabel (NOT recommended):** `m_n = m_p +
    Q_NEUTRON_MEV + m_e` with the *experimental* `Q_NEUTRON_MEV`
    (= m_n − m_p − m_e by construction) is exactly value-preserving and
    reclassifies the audit 4-input → 3-input-canonical — **but it is
    circular** (experimental m_n relabeled) and a canonical-watcher would
    flag it as gaming the audit. Do not ship this as "the fix."
- **Why deferred:** the honest fix is value-changing + owner-gated; the
  cheap fix is gaming. **Owner decides.**

## Disposition

Items **A, B** belong to the active q₀ sweep (fold in, don't race).
Items **C, D** are owner precision/discipline decisions. None is clean,
isolated, non-colliding mechanical work — which is why the value-preserving
tranche stopped where it did.
