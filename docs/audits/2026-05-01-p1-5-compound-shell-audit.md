# P1.5 audit — compound-shell / atlas / light-isotopes — result

**Pair**: [`2026-05-01-math-framework-workplan.md`](2026-05-01-math-framework-workplan.md) §P1.5
**Branch**: `claude/audit-math-framework-FXlp2`
**Conclusion**: 🟢 **No new calibration leak found.** The three
suspect blocks all derive their numerical content from the three
declared calibrations of
[`prop:three-calibration-discipline`](../../content/quantum-observable-universe/observations/three-calibration-discipline.md)
($H^0 = m_e$, $H^1 = m_\mu/m_e \to q_0$, $H^2 = Q_\beta$).

## Per-block findings

### `compound-beta-shell-calibration.md`

**Suspicion**: filename contains "calibration".

**Verdict**: 🟢 The "calibration" in the name is the $H^2$
calibration $Q_\beta$ (free-neutron β-decay Q-value, 0.782 MeV)
— exactly the third entry in the three-calibration discipline.
The block does **not** introduce a fourth fit:

- $E_0 = Q_\beta$ is the declared $H^2$ input.
- Magic-shell binding is *derived* from the chain Q-value of
  β-decays through the magic anchor, minus the level-3 shadow
  prices for non-magic intermediate steps. No free coefficients.
- The block explicitly says: "shell $y_{\text{target}}$ values are
  not independently calibrated; they follow from β-decay Q-values
  and level-3 shadow prices".

**Action taken**: minor language alignment — "the single
archimedean calibration constant at level 2" → "the **$H^2$
calibration** of the three-calibration discipline"; the
"single-calibration" claim in §Consequences updated to reference
the three-calibration discipline.

### `recursive-atom-knot-atlas.md`

**Suspicion**: a recursive composition could propagate base-case fits.

**Verdict**: 🟢 The atlas already carries a strict
**Methodology classification** (lines 15–37 of the source) with
six tags:

- `principled-derivation` — closure of explicit σ-braid words.
- `principled-gb-nf` — trivial-NF entries (single strand).
- `manual-historical-volume-match` — flagged: GB-NF derivation not
  yet computed, but identification well-established.
- `magic-A-formula` — closed-form $A \cdot 8G$ (Catalan).
- `recursive-on-⁴He` — composite from ⁴He + binding.
- `deprecated-volume-match` — **explicitly quarantined; do not cite as principled**; reverse-engineers AME data.

The atlas is exemplary: it self-quarantines volume-match results,
splits the table into principled and provisional sections, and
links the deprecation witness JSON. **No action needed.**

### `derived-mass-formula-light-isotopes.md`

**Suspicion**: an "empirical scorecard" might be hiding a
post-hoc coefficient choice.

**Verdict**: 🟢 Every term in the formula is declared derived:

- $\alpha = m_e \cdot 8G$ — Catalan × $H^0$ calibration.
- $\Phi_1, \Phi_2, \Phi_3$ — per-generator transfer-matrix chains
  on inter-nucleon generators (deterministic, structural choice
  of generator positions $3k+2$).
- $\Delta_W$ — Wigner $T=0$ pn pairing, derived from $H_q((2,2))$.
- $\Delta_{T=1}$ — natural $T=1$ extension using the same
  self-conjugate partition.

The "empirical scorecard" (table at line 30) is a *test*, not a
fit: predicted vs CODATA values are reported as residuals (0.04%
to 0.6%), with no parameters tuned to match. **No action needed.**

## Net status

P1.5 closes with the conclusion that the suspected
calibration-leak blocks are **all structurally clean** under the
three-calibration discipline. The audit's residual concern (the
"compound-shell calibration self-reports as a calibration" flag of
[deep audit §2·G](2026-05-01-math-framework-deep-audit.md#2g--compound-shell--shell-closure-calibration))
is resolved: it is the $H^2$ calibration, not a fourth fit.

The deep-audit `SHELL-1` flag is downgraded from 🟠 to 🟢 in the
companion update.
