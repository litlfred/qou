# Six-term mass-formula compute pipeline — script audit

**Goal**: map every paper formula (`knot-mass-formula-unified.md`,
six-term + jet) to its compute implementation; flag deprecation
chains; identify the canonical substrate-only predictor.

**Branch**: `claude/neutron-mass-50dps-chain`
**Date**: 2026-05-11

## Paper-side derivations (per [`knot-mass-formula-unified.md`](../../content/quantum-observable-universe/braids-and-knots/knot-mass-formula-unified.md))

| Term | Paper formula | Block | Status |
|------|---------------|-------|--------|
| **T1** | $\lvert\mathrm{tr}_M(T_w)\rvert$ | [`prop:categorical-mass-markov`](../../content/quantum-observable-universe/braids-and-knots/categorical-mass-markov.md) | derived |
| **T2** | brane tower, single gen | [`prop:mass-endomorphism-tower`](../../content/quantum-observable-universe/braids-and-knots/mass-endomorphism-tower.md) | **derived** (3 paths, see below) |
| **T3** | brane tower, gen-pair | same | **derived** (3 paths) |
| **T4** | $m_e \cdot \mathrm{tr}_M(C_{\dim_q}^{H_n(R, q)})$ | [`thm:frobenius-codim-universal`](../../content/quantum-observable-universe/braids-and-knots/frobenius-codim-universal.md) | derived (per-$3A$ form) |
| **T5** | $a_K \cdot \mathcal{C}_K$ chirality | [`prop:six-term-mass-formula-complete`](../../content/quantum-observable-universe/braids-and-knots/six-term-mass-formula-complete.md) | derived (for D, T, ⁴He) |
| **T6** | jet-prefix Habiro residue tail | (`pure_hecke_binding.py`) | **open R&D** |

### T2 + T3 has three derivation paths in the paper

The boxed Kashaev form is flagged "Markov-invariance-broken at $q_0$" producing $\sim 10^5$ MeV pathologies. The paper lists three reformulation paths, all derived but with different numerical behaviour:

| Path | T2 form | T3 form | Markov-invariant? | Convergent at $q_0$? |
|------|---------|---------|-------------------|----------------------|
| **Kashaev (boxed)** | $-\sum_i \mathrm{Li}_2^q(-\lvert\hat V_i\rvert)$ | $-z^2 \sum_{i<j} \mathrm{Li}_2^q(-\lvert\hat V_i \hat V_j\rvert)$ | NO | catastrophic ($\Phi_q(0.99) \approx 6.7\times 10^5$) |
| **Path 1 R-side algebraic** | $(n-1) \cdot z^2$ | $\binom{n-1}{2} \cdot z^4$ | YES (Markov axiom, `prop:markov-pair-z2`) | YES |
| **Path 2 Wedderburn-Heine** | $\sum_n c_n \mathrm{tr}_M(\sigma_i^n)$ converging to $\Phi_q(z)$ | similar | YES | YES (`brane-tower-plancherel-scaffold.witness.json`) |
| **Path 3 Habiro single-trace** | absorbs T2+T3+T6 into one cyclotomic expansion | — | YES | YES, sub-1% errors on $\{p, n, D, T, ^3\mathrm{He}\}$ (`path-b-habiro-mass-probe.witness.json`) |

## Compute-side implementations

### Canonical substrate-only predictor

[`paper_six_term_isotope_sweep.py`](../../computations/sweeps/paper_six_term_isotope_sweep.py) — **the working entry point**. Implements T1+T2+T3+T4+T5(+T6 if witness present) with 5 selectable `tower_mode`s:

| Mode | T2+T3 path | Mean \|err\| | Max \|err\| | Status |
|------|-----------|-------------:|------------:|--------|
| `brane-legacy` | Kashaev $\Phi_q$ | 22% | 56% | deprecated (Markov-broken) |
| `drop` | $T_2 = T_3 = 0$ | 57% | 84% | diagnostic baseline |
| `q1-base` | classical-limit $(1/2)^{2A-1}$ | 60% | 86% | diagnostic |
| `r-side-bare` | **Path 1 (paper preferred)** | **36%** | **48%** | canonical for now |
| `li2q` | corrected Kashaev (Li_2^q) | 22% | 31% | best empirical |

Output: [`paper-six-term-isotope-sweep.witness.json`](../../computations/sweeps/paper-six-term-isotope-sweep.witness.json).

### Five-mode side-by-side at $q_0$ (mean \|err\| vs CODATA, post-calibration)

| iso | A | brane | drop | q1-base | **r-side** | **li2q** |
|----:|--:|------:|-----:|--------:|-----------:|---------:|
|   p | 1 | 0.0% | 0.0% | 0.0% | **0.0%** | **0.0%** |
|   n | 1 | -56.2% | -4.1% | -3.6% | **-3.6%** | **-4.9%** |
|   D | 2 | -21.0% | -48.5% | -53.3% | **-32.8%** | **-21.7%** |
|   T | 3 | -25.7% | -75.2% | -78.0% | **-48.3%** | **-31.5%** |
| ³He | 3 | +0.6% | -74.3% | -77.2% | **-47.5%** | **-26.6%** |
| ⁴He | 4 | -4.4% | -83.7% | -85.7% | **-48.3%** | **-25.0%** |

The T − ³He isospin defect under `brane-legacy` is −737 MeV vs CODATA +19 keV (38 000× wrong); `r-side-bare` and `li2q` give −22 MeV and −136 MeV respectively, still 1000–7000× wrong. None of the modes close the isospin defect to even 1%.

### Deprecated / scattered implementations

| Script | Status | Disposition |
|--------|--------|-------------|
| [`atomic_braid_mass_table.py`](../../computations/atomic_braid_mass_table.py) | **⚠️ DEPRECATED 2026-05-08** (wrong multiplicative T1) | retained for witness compat; do not extend |
| [`atomic_braid_mass_table_modes_sweep.py`](../../computations/atomic_braid_mass_table_modes_sweep.py) | downstream of above | deprecate |
| [`mass_formula_6term_mpfr_50dps.py`](../../computations/mass_formula_6term_mpfr_50dps.py) | Phase A 50-dps; consumes registry $\tau_M$ | keep as 50-dps backend |
| [`atomic_mass_via_rho_k.py`](../../computations/atomic_mass_via_rho_k.py) | **CANONICAL GOING-FORWARD** per its own header, BUT it's single-term + $\rho_K$ post-calibration consuming CODATA $m_p$, $m_n$ | ⚠️ violates three-calibration discipline; rename or relabel as "post-calibration only" |
| [`probe_sdp_canonical_paper_formula.py`](../../computations/probe_sdp_canonical_paper_formula.py) | Single-term T1 only, on Model B SDP-canonical braids | keep as Model B T1 reference |

### Pieces wired but not yet plugged in

- **T6 Habiro residue tail**: `term6_residues_at_roots.py` exists but `term6-habiro-residue-mpfr-50dps.witness.json` not on this branch — current sweep silently sets T6 = 0 MeV (warning emitted).
- **Path 2 Wedderburn-Heine**: `brane-tower-plancherel-scaffold.witness.json` exists but `paper_six_term_isotope_sweep.py` has no `tower_mode="path-2"` option.
- **Path 3 Habiro single-trace**: `path-b-habiro-mass-probe.witness.json` claims sub-1% errors; no entry-point script for production use — buried in `_deprecated/` or older PR branches.

## Model A vs Model B T1 input

`paper_six_term_isotope_sweep.py` consumes T1 from
`derivation_chain.TR_M_AT_Q0` (Model A; production
`atomic_braid_word_3A` values via `markov_peel.tr_M_atomic`). To get a Model
B variant, substitute Model B's SDP-canonical $\lvert\tau_M\rvert$ values:

| Atom | Model A T1 ($3A$-strand) | Model B T1 (canonical knot, Wenzl-Schur) |
|------|-------------------------:|----------------------------------------:|
| D | $0.388286$ | $0.288326$ |
| T | $0.104052$ | $0.012889$ |
| ³He | $0.206540$ | $0.998367$ |

These don't bridge — the ratios $0.388/0.288 = 1.35$, $0.104/0.0129 = 8.07$, $0.207/0.998 = 0.21$ have no common factor (per [`2026-05-11-model-b-mass-table.md`](../audits/2026-05-11-model-b-mass-table.md)).

## Migration plan (next session)

1. **Add `--t1-source=model-b` option** to `paper_six_term_isotope_sweep.py`, reading SDP-canonical $\tau_M$ from `probe-sdp-canonical-paper-formula.witness.json`. Re-run; compare to Model A column.
2. **Run `term6_residues_at_roots.py`** to generate the missing T6 witness; re-run sweep with non-zero T6.
3. **Add `tower_mode="path-2"`** (Path 2 Wedderburn-Heine) per
   [`brane-tower-plancherel-scaffold.witness.json`](../../computations/brane-tower-plancherel-scaffold.witness.json).
4. **Add `tower_mode="habiro-single-trace"`** (Path 3) per [`path-b-habiro-mass-probe.witness.json`](../../computations/probes/path-b-habiro-mass-probe.witness.json) — claims sub-1% error.
5. **Relabel `atomic_mass_via_rho_k.py`** with explicit "post-calibration only" docstring (currently misleadingly tagged "canonical going-forward").
6. **Deprecate** `atomic_braid_mass_table_modes_sweep.py` (already-flagged downstream of broken script).
