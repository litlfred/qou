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
[`neutron-gap-probes-round3.witness.json`](../../computations/neutron-gap-probes-round3.witness.json):
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

1. [`computations/substrate/codata_constants.py`](../../computations/substrate/codata_constants.py)
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
2. [`computations/codata-2022-validation-masses.witness.json`](../../computations/codata-2022-validation-masses.witness.json)
   created — source-of-truth for nucleon + light-nucleus CODATA masses.
3. [`computations/cal-3-q-beta.witness.json`](../../computations/cal-3-q-beta.witness.json)
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
   tautological pipeline reports $m_p = :val[m_p_MeV]{precision=6}$ MeV and the deuteron
   binding $\Delta = +2.225$ MeV at $0.119\%$ relative error. After
   rewire, $m_p$ becomes a genuine prediction with a ~$1.8\%$ residual
   from the $\Phi_q$-tower truncation
   ([`mass_endomorphism.py:5,26`](../../computations/mass_endomorphism.py)),
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
5. **Use the unified knot mass formula, not a single-term `|tr_M|·E_0`
   shortcut.** (Correction applied 2026-05-10 after owner pointed
   out an earlier draft of this doc had the wrong formula.) The
   canonical chain is
   [`prop:atom-knot-mass-derivation`](../../content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md):

   $$M(\mathfrak{H}) = \rho \cdot \bigl[\,|\mathrm{tr}_M(T_w)| + \mathrm{tower}(T_w) + \mathrm{tr}_M(C_{\dim_q})\,\bigr]$$

   $$B(\mathfrak{H}) = m_e \cdot M(\mathfrak{H})\big|_{q = q_0}$$

   with three components:

   - $|\mathrm{tr}_M(T_w)|$ — descended Markov trace via Wenzl bridge
     $\sum_\lambda y_\lambda(q)\,\chi_\lambda(T_w)$.
   - $\mathrm{tower}(T_w) = \sum_i \Phi_q(|\hat{V}_i|) + z^2 \sum_{i<j} \Phi_q(|\hat{V}_i \hat{V}_j|)$
     — brane tower from per-generator additive-Wedderburn volumes
     (see [`prop:mass-endomorphism-tower`](../../content/quantum-observable-universe/braids-and-knots/mass-endomorphism-tower.md)).
   - $\mathrm{tr}_M(C_{\dim_q}) = \sum_{\lambda \vdash n_0} 1/\dim_q(\lambda)$
     — Frobenius co-Casimir trace
     ([`thm:frobenius-codim-universal`](../../content/quantum-observable-universe/braids-and-knots/frobenius-codim-universal.md)).

   The canonical Hecke element $T_w$ is built by
   [`mass_at_3A_proper.atom_braid_word_3A(Z, N)`](../../computations/mass_at_3A_proper.py)
   — the **β-decay-operator-unfolded** 3A-strand word. For the
   proton ($Z = 1$, $N = 0$): an 11-letter word in $H_3(q)$, since
   the β-decay operator $T_\beta = \sigma_0 \sigma_1^{-1}$ lives in
   $H_3(q)$ and the nucleon level satisfies the
   [`prop:level-sufficiency`](../../content/quantum-observable-universe/braids-and-knots/level-sufficiency.md)
   bound $k_{\max}(P, q) \le 3$ (deeper unfolding is superfluous
   for trace-class invariants).

   The earlier draft of this section claimed
   `m_p = |tr_M(p, q_0)| · E_0` with $E_0 = Q_\beta$ as the
   "categorical chain" — that's wrong. That single-term form is
   shorthand and is structurally inadequate (verified empirically
   in `probe-sdp-canonical-paper-formula.witness.json`: 87–100 %
   error on $D, T, {}^3$He). The proper $m_p$ derivation uses the
   unified formula above with all three components plus the $m_e$
   conversion factor; **no CAL-3 entry, no $E_0$ scaling, no CODATA
   m_p back-fit**.

   **Caveat — the deprecated `atomic_braid_mass_table.py`.** That
   script (lines 5–22 of
   [`atomic_braid_mass_table.py`](../../computations/atomic_braid_mass_table.py)
   carry their own deprecation banner) contains a literal
   `E_0 = (M_p_CODATA − t6) / total_hecke[p]` back-fit at line 441.
   That **is** a 4th-calibration violation, but it lives in a script
   already marked obsolete; the canonical replacement
   `atomic_mass_via_rho_k.py` does not back-fit $E_0$ — it consumes
   `M_P_MEV` and `M_N_MEV` directly via $\rho_K^{\mathrm{LO}}$,
   which is the discipline violation Phase 0b is fixing. So the
   right fix is **not** to derive $E_0$ from $Q_\beta / |\Delta(\mathrm{net})|$
   (a different chain in the paper, used for Q-value spectral
   decomposition per
   [`spectral-decomposition-qvalue.md`](../../content/quantum-observable-universe/descartes-universe/spectral-decomposition-qvalue.md))
   — the right fix is to drop $E_0$ from the proton-mass derivation
   entirely and replace it with the unified knot mass formula above.

   **Resolution path** (Phase 0b.2 prerequisite):
   1. Confirm the brane-tower component
      ([`prop:mass-endomorphism-tower`](../../content/quantum-observable-universe/braids-and-knots/mass-endomorphism-tower.md))
      is callable from
      [`mass_endomorphism.py`](../../computations/mass_endomorphism.py).
      Document the current ~1.8 % systematic residual (Φ_q
      truncation) and note it as Workplan 2's Phase 2 target.
   2. Add a Frobenius co-Casimir helper that returns
      $\sum_{\lambda \vdash n_0} 1/\dim_q(\lambda)$ at $q_0$, given
      $n_0$. Trivial for the proton ($n_0 = 3$); reusable for
      neutron + light nuclei.
   3. Wire `derived_masses.proton_mass_mev()` to call into the
      multi-term assembly with $T_w = \texttt{atom\_braid\_word\_3A}(1, 0)$
      and multiply by $m_e$. Drop the `NotImplementedError`.
   4. Same for `neutron_mass_mev()` with $T_w = \texttt{atom\_braid\_word\_3A}(0, 1)$.
   5. Cross-check $m_n - m_p \approx Q_\beta + m_e$ within the
      Φ_q-tower truncation residual. If it agrees, CAL-3 is
      overdetermined (consistency check); if it disagrees beyond
      the truncation, that's a real falsifier — escalate.
   6. Light nuclei: derive $\rho_K^{\mathrm{LO}}$ purely from the
      derived $m_p$ and $m_n$ (NOT from CODATA literals), then
      proceed with the binding pipeline as before.

## Migration plan for the sibling agent

### Phase 0b.1 — Inventory (1–2 days)

Run the full audit:
```bash
grep -rn -E 'from codata_constants import.*M_[PN]_MEV|M_[DT]_MEV|M_HE[34]_MEV|c\.M_[PN]_MEV' \
  computations/ --include='*.py' \
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

Create `computations/derived_masses.py` that exposes:
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
- [ ] Read [`neutron-gap-probes-round3.witness.json`](../../computations/neutron-gap-probes-round3.witness.json)
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

- All `*.py` scripts under `computations/` import
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
