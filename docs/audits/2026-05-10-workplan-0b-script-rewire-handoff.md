# Workplan 0b — Script rewire handoff (RISKY, sibling-PR coordination required)

**Date opened**: 2026-05-10
**Originating branch**: `claude/display-mass-tables-PAj4i`
**Status**: HANDOFF — not yet started
**Estimated effort**: 1–2 weeks (multi-PR coordination, regression-testing of ~30 scripts, witness regen)
**Risk class**: HIGH — this rewires the foundation that Workplans 1–5 build on.

## Background — the discipline violation

The QOU paper's
[`prop:three-calibration-inputs`](../../content/quantum-observable-universe/braids-and-knots/three-calibration-inputs.md)
admits **exactly three** external calibration inputs: CAL-1 = $m_e$,
CAL-2 = $m_\mu/m_e$, CAL-3 = $Q_\beta(n)$. Repeated independently in
[`calibration-inputs.md`](../../content/quantum-observable-universe/braids-and-knots/calibration-inputs.md),
[`three-calibration-discipline.md`](../../content/quantum-observable-universe/observations/three-calibration-discipline.md),
[`mass-formula-validation.md`](../../content/quantum-observable-universe/observations/mass-formula-validation.md),
[`derivation-audit-report.md`](../../content/quantum-observable-universe/braids-and-knots/derivation-audit-report.md),
[`pre-archimedean-derivation-chain.md`](../../content/quantum-observable-universe/braids-and-knots/pre-archimedean-derivation-chain.md).

The compute pipeline silently violates the discipline by injecting
$m_p$, $m_n$ (and the light-nucleus masses $m_D$, $m_T$, $m_{^3\mathrm{He}}$,
$m_{^4\mathrm{He}}$) as **CODATA inputs** rather than deriving them. This
inflates the calibration count from 3 → 9 in practice. The diagnostic
self-recommendation already exists in
[`neutron-gap-probes-round3.witness.json`](../../folio-assistant/computations/neutron-gap-probes-round3.witness.json):
> "the canonical 3-input Skein-pair scheme (m_μ/m_e, m_e, Q_β(n)) is
> the theoretically-correct form of the n/p split: the Hecke trace
> alone does NOT distinguish neutron from proton, so any framework
> that omits Q_β as a structural input will show residuals at the
> $m_n − m_p \approx 0.14\%$ scale (or larger). Sprint A v5's naïve
> assembly should be revised to use the 3-input convention: predict
> $m_p$ from $|\mathrm{tr}_M(p)| \cdot E_0$; predict
> $m_n = m_p + Q_\beta + m_e$ (NOT from $|\mathrm{tr}_M(n)|$)."

## What's already done (Workplan 0a, this branch)

Surgical, non-destructive infrastructure cleanup. Backwards-compatible.

1. [`folio-assistant/computations/codata_constants.py`](../../folio-assistant/computations/codata_constants.py)
   refactored:
   - Adds DISCIPLINE banner (CAL-1/2/3 table).
   - Renames `M_P_MEV`, `M_N_MEV`, `M_D_MEV`, `M_T_MEV`, `M_HE3_MEV`,
     `M_HE4_MEV` → `*_VALIDATION` suffix.
   - `Q_BETA_MEV` promoted from derived to primary CAL-3 input.
   - Module-level `__getattr__` exposes the old names as
     **deprecated aliases** that resolve correctly but emit
     `DeprecationWarning` on every access. **No script breaks.**
   - Adds CAL-3 ↔ (m_n − m_p − m_e) consistency check (assertion
     warning if combined CODATA σ disagrees).
   - All values except $m_e$ now loaded from witness JSONs.
2. [`folio-assistant/computations/codata-2022-validation-masses.witness.json`](../../folio-assistant/computations/codata-2022-validation-masses.witness.json)
   created — source-of-truth for nucleon + light-nucleus CODATA masses.
3. [`folio-assistant/computations/cal-3-q-beta.witness.json`](../../folio-assistant/computations/cal-3-q-beta.witness.json)
   created — CAL-3 input with provenance.
4. [`recomputed-low-isotope-mass-table.md`](../../content/quantum-observable-universe/braids-and-knots/recomputed-low-isotope-mass-table.md)
   line 79: corrected the misstatement ("3 CAL inputs are $m_e, m_p, m_n$").
5. [`mass-comparison-table.md`](../../content/quantum-observable-universe/observations/mass-comparison-table.md)
   proton / neutron / n−p rows: marked † as **tautological under the
   current pipeline**, with explanation pointing to this handoff.

## What's still risky (Workplan 0b — this doc)

The **script-side migration** to derive $m_p$, $m_n$, $m_D$, $m_T$,
$m_{^3\mathrm{He}}$, $m_{^4\mathrm{He}}$ from $\{m_e, q_0, Q_\beta\}$.
Why risky:

1. **Predicted values will shift substantially.** The current
   tautological pipeline reports $m_p = 938.272$ MeV and the deuteron
   binding $\Delta = +2.225$ MeV at $0.119\%$ relative error. After
   rewire, $m_p$ becomes a genuine prediction with a ~$1.8\%$ residual
   from the $\Phi_q$-tower truncation
   ([`mass_endomorphism.py:5,26`](../../folio-assistant/computations/mass_endomorphism.py)),
   so the deuteron-binding number will move correspondingly.
2. **~30 scripts touch the deprecated names.** Each one needs case-by-case
   review:
   - Is it consuming $m_p$ as a *prediction input* (needs rewire) or as a
     *validation comparator* (just rename to `_VALIDATION`)?
   - Many are not always obvious — some use $m_p$ as a unit-bridge
     (e.g. ratio expressions) where the right answer is "use the
     predicted $m_p$".
3. **Sibling PR coordination.** The 1ppb workplan
   ([`docs/audits/2026-05-10-1ppb-workplan-update.md`](2026-05-10-1ppb-workplan-update.md))
   mentions in-flight PRs #623, #622, #614, #617 (and others #600, #602,
   #603, #612, #613, #618). Several of these touch the same scripts
   `binding_K_direct.py`, `applied_uniqueness_mass_table.py`,
   `derivation_chain.py`, `atomic_braid_mass_table.py`. The rewire must
   be sequenced after they land OR coordinated with each PR's owner.
4. **The categorical chain has its own gaps.** $m_p = |\mathrm{tr}_M(p)| \cdot E_0$
   currently uses a placeholder $m_e^{\mathrm{Hecke}}$ literal in
   `applied-uniqueness-mass-table.witness.json` (per its own
   `phase_2_note`). Workplan 2 (Path A 50-dps $m_e^{\mathrm{Hecke}}$)
   must land first — otherwise the rewired predictions will look
   ~25% off when the real signal is the placeholder, not the
   discipline fix. **Workplan 0b depends on Workplan 2.**
5. **$E_0$ provenance — second discipline violation discovered
   2026-05-10 during Phase 0b.2.** The framework defines
   $E_0 = Q_\beta(n) / |\Delta(\mathrm{net})|$ with
   $\Delta(\mathrm{net}) = h(h-2)/2$ from the symbolic NF
   difference between neutron and proton. The compute infra
   currently has **three different conventions in flight**, none
   of which match the symbolic formula:

   - [`hecke_core.E_0_CALIBRATION_MEV`](../../folio-assistant/computations/hecke_core.py)
     line 2922: `E_0 = Q_β(n) ≈ 0.782` MeV/cat-unit (i.e. it sets
     $|\Delta(\mathrm{net})| = 1$, skipping the symbolic step).
   - [`canonical-mass-table.witness.json`](../../folio-assistant/computations/canonical-mass-table.witness.json)
     parameters block: `E_0_MeV: 0.782` (truncated 4 sig figs of
     the same convention).
   - [`atomic_braid_mass_table.py`](../../folio-assistant/computations/atomic_braid_mass_table.py)
     "Strategy-3" (per
     [`derivation_chain.py:90`](../../folio-assistant/computations/derivation_chain.py)):
     `E_0 ≈ 199.86 MeV/cat-unit` — **back-fitted** from
     `total_hecke[p] · E_0 = 938.272 MeV` (proton CODATA). This
     is a 4th-calibration violation **parallel to** the
     `M_P_MEV` / `M_N_MEV` one this handoff is meant to fix.

   **Demonstration of the inconsistency.** The newly-added
   [`derived_masses.derivation_summary()`](../../folio-assistant/computations/derived_masses.py)
   shows the naive single-term `m_p = |tr_M(p, q_0)| · E_0` with
   $E_0 = Q_\beta$ gives `1.065 × 0.782 ≈ 0.83` MeV — off by 3
   orders of magnitude vs CODATA `m_p = 938.272` MeV. The
   "Strategy-3" pipeline gets the right number only because
   `total_hecke[p] = T1+T2+T3+T4 ≈ 4.6912` cat-units (from the
   Wenzl-bridge multi-term sum in
   [`atomic_braid_mass_terms.py`](../../folio-assistant/computations/atomic_braid_mass_terms.py))
   *and* $E_0$ is back-fitted to make the product hit CODATA. The
   `total_hecke[p]` cat-unit sum is genuine framework output
   (categorical, no fit); the $E_0$ back-fit is a hidden calibration.

   **Resolution path** (Phase 0b.2 prerequisite):
   1. Find or write the script that computes
      $\Delta(\mathrm{net}) = h(h-2)/2$ symbolically from the
      neutron / proton braid NF difference. Sibling agent: search
      for `Delta_net`, `h*(h-2)/2`, `symbolic_q_value`,
      `Q_value_symbolic`, `nucleon_mass_splitting` in
      `folio-assistant/computations/` and `content/`.
   2. Compute $|\Delta(\mathrm{net})|$ at $q_0$.
   3. Compute $E_0 = Q_\beta / |\Delta(\mathrm{net})|$. Verify this
      matches `atomic_braid_mass_table.py`'s back-fitted 199.86
      MeV/cat-unit (within $\Phi_q$-tower truncation residual). If
      it does NOT match, that's a real falsifier — the framework's
      $E_0$ formula needs revisiting.
   4. Replace `E_0_CALIBRATION_MEV` in `hecke_core.py` with the
      derived value, and remove the back-fit from
      `atomic_braid_mass_table.py`.
   5. Drop the `NotImplementedError` stubs from
      [`derived_masses.py`](../../folio-assistant/computations/derived_masses.py)
      and wire in the categorical predictions.

## Migration plan for the sibling agent

### Phase 0b.1 — Inventory (1–2 days)

Run the full audit:
```bash
grep -rn -E 'from codata_constants import.*M_[PN]_MEV|M_[DT]_MEV|M_HE[34]_MEV|c\.M_[PN]_MEV' \
  folio-assistant/computations/ --include='*.py' \
  | tee /tmp/codata-deprecation-call-sites.txt
```

For each call site, classify:
- **A. Validation comparator** (e.g. `err = pred - M_P_MEV`) →
  trivial rename to `*_VALIDATION`.
- **B. Prediction input** (e.g. `M_pred = (Z * M_P_MEV + N * M_N_MEV) + Binding`) →
  needs rewire to derived chain.
- **C. Unit bridge / ratio** (e.g. `m_e_natural = M_E_MEV / mass_endomorphism(...)`) —
  case-by-case judgment.

Expected counts (from agent #2's analysis):
- Class A: ~15 scripts (the `probe_*` and `*_diagnostic.py` files)
- Class B: ~10 scripts (the prediction tables)
- Class C: ~5 scripts (helpers + the 50-dps chains)

### Phase 0b.2 — Build the derived-mass module (2–3 days)

Create `folio-assistant/computations/derived_masses.py` that exposes:
```python
from derived_masses import M_P_DERIVED, M_N_DERIVED, M_D_DERIVED, ...
```
Each derived value is computed lazily on first access (cached) from:
- `derivation_chain.TR_M_AT_Q0[atom]` for $|\mathrm{tr}_M|$
- `Q_BETA_MEV` for CAL-3
- `M_E_MEV` for CAL-1
- $E_0 = Q_\beta / |\Delta(\mathrm{net})|$ — needs the symbolic
  $\Delta(\mathrm{net})$ source identified.

Each accessor must emit a witness `*-derived-mass-<atom>.witness.json`
recording the input chain (provenance) and the predicted value at the
build's commit SHA — so reviewers can audit the derivation.

### Phase 0b.3 — Migrate Class A call sites (1 day)

Mechanical rename. Each script tested in isolation by importing it
under `python -W error::DeprecationWarning` to force any leftover
deprecated alias to surface.

### Phase 0b.4 — Migrate Class B call sites (3–5 days)

Per-script PR. Coordinate with sibling-PR owners:
- `binding_K_direct.py` — owner: PR #602 / #603 (Δ_λ derivation race).
- `applied_uniqueness_mass_table.py` — owner: PR #617 (Phase 2 $m_e^{\mathrm{Hecke}}$).
- `atomic_braid_mass_table.py` — currently has TODO marker on
  `a_ZN, delta_n2` placeholder (line 123-125 per agent #3 audit);
  coordinate with that owner.
- `derivation_chain.py` — registry; coordinate with PR #612 owner.

For each migrated script, regenerate the witness and **commit BOTH the
script change AND the new witness** so reviewers can diff predictions
cleanly. Expect ~5–10 % swing on first-pass numbers; that swing IS the
fix (it surfaces the previously-tautological residuals).

### Phase 0b.5 — Migrate Class C call sites (1–2 days)

Case-by-case judgment. The 50-dps chains
(`build_proton_mass_50dps_chain.py`, etc.) are the hardest because
they may legitimately want both `M_P_MEV_VALIDATION` (target) and
`M_P_DERIVED` (prediction) in scope.

### Phase 0b.6 — Remove deprecated aliases (after one release cycle)

Once `grep -rn 'from codata_constants import M_P_MEV' folio-assistant/`
returns empty and CI runs clean for one full week with `-W error`,
delete the `__getattr__` block from `codata_constants.py`.

## Coordination checklist for sibling agent

- [ ] Read this doc start-to-finish.
- [ ] Read [`neutron-gap-probes-round3.witness.json`](../../folio-assistant/computations/neutron-gap-probes-round3.witness.json)
      `recommendation` field for the canonical 3-input form.
- [ ] Confirm Workplan 2 (Phase 2 $m_e^{\mathrm{Hecke}}$) is **landed**
      before Phase 0b.4 begins. If not, queue 0b.4 behind it.
- [ ] Identify the script that computes $E_0 = Q_\beta / |\Delta(\mathrm{net})|$
      symbolically. If none exists, write it (Phase 0b.2 prerequisite).
- [ ] Coordinate with owners of in-flight PRs #602, #603, #612, #617,
      #618, #622, #623 before touching their scripts. Use the
      `local/coordinate` skill for the cross-PR ledger.
- [ ] After migration, regenerate the three "live" mass-table
      witnesses (`canonical-mass-table.witness.json`,
      `applied-uniqueness-mass-table.witness.json`,
      `atomic-braid-mass-table.witness.json`) and update the three
      narrative `.md` files in
      `content/quantum-observable-universe/{braids-and-knots,observations,particle-interactions}/`
      to remove the "tautological" † footnotes added in 0a.

## Acceptance criteria

- All `*.py` scripts under `folio-assistant/computations/` import
  cleanly under `python -W error::DeprecationWarning`.
- All `*.witness.json` files for mass / binding predictions are
  regenerated; their numerical values may differ from the current
  by up to ~10% (this is expected — the swing IS the fix).
- The proton / neutron rows in `mass-comparison-table.md` no longer
  carry the † tautology footnote and now report a non-trivial
  residual (the $\Phi_q$-tower truncation, ~1.8%).
- The CAL-3 consistency check in `codata_constants.py` continues to
  pass (no warning emitted on import).
- All five tightening workplans (1–5 in the
  [1ppb workplan update](2026-05-10-1ppb-workplan-update.md))
  can resume against the cleaned-up foundation.
