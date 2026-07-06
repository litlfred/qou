# M1 mass table — V2 production-wired snapshot

**Date:** 2026-05-15 (session end)
**Branch:** `claude/review-1ppb-prs-EC0ay`
**Builds on:** [`2026-05-12-m1-mass-table.md`](2026-05-12-m1-mass-table.md), [`2026-05-15-three-pr-integration.md`](2026-05-15-three-pr-integration.md)

Snapshot after the V2 mirror-chirality production-wire (`term5_v2_chirality.aK_v2`
default in both `paper_six_term_mass` and `mass_formula_6term_mpfr_50dps.term_5_chirality_bw_mp`)
and after re-running the canonical isotope sweep. The substrate calibration
gap is **unchanged** from the M1 baseline; V2 affects only the chirality
factor `a_K` per atom.

## 1  Source

- Witness: [`computations/sweeps/paper-six-term-isotope-sweep.witness.json`](../../computations/sweeps/paper-six-term-isotope-sweep.witness.json)
- Generator: [`paper_six_term_isotope_sweep.py`](../../computations/sweeps/paper_six_term_isotope_sweep.py) (commit `f25a90e3` + cherry-picks)
- Default `chirality_source = "v2"` (substrate-derived `τ(β · β_mirror⁻¹)` per
  [`prop:he4-two-row-dominance`](../../content/quantum-observable-universe/braids-and-knots/he4-two-row-dominance.md)
  conjecture context; library `term5_v2_chirality.aK_v2`).
- Default `e0_mode = "substrate"` (no calibration leak).

## 2  Current mass table (V2 default, `li2q` tower) — light isotopes

`err_pct = (M_pred − M_codata) / M_codata × 100`; sign is signed.

| Atom | A | $M_{\mathrm{codata}}$ (MeV) | $M_{\mathrm{pred}}$ (MeV) | err_pct | $a_K$ (V2) | Source |
|------|--:|---------------------------:|--------------------------:|--------:|----------:|--------|
| p    | 1 |   938.272 |  28.866 | −96.923 % |  2.4237 | v2 |
| n    | 1 |   939.565 |  25.821 | −97.252 % |  2.1336 | v2 |
| D    | 2 |  1876.124 |  39.597 | −97.889 % |  5.2279 | v2 |
| T    | 3 |  2809.432 |  46.366 | −98.350 % | 10.4775 | v2 |
| ³He  | 3 |  2809.413 | 107.141 | −96.186 % | 13.9937 | v2 |
| ⁴He  | 4 |  3728.401 |  73.362 | −98.032 % | 28.0456 | v2 |

**MAE on {p, n, D, T, ³He, ⁴He}**: $97.439\,\%$. Substantially the same
as the M0/M1 baseline ($98.027\,\%$ under `li2q` per the prior table);
the V2 chirality factor changes the per-atom $a_K$ contribution but the
~50× scale gap is dominated by the unresolved substrate $E_0 \cdot
(T1 + T2 + T3 + T4)$ vs nucleon mass scale.

## 3  Heavy isotopes (A ≥ 5) — T1 witness gap

| Atom | A | Status |
|------|--:|--------|
| ⁵Li  | 5 | T1 witness missing (`atomic-tr-m-mpfr-50dps.witness.json` does not cover A ≥ 5) |
| ⁶Li  | 6 | T1 witness missing |
| ⁷Li  | 7 | T1 witness missing |
| ⁷Be  | 7 | T1 witness missing |
| ⁸Be  | 8 | T1 witness missing |
| ⁹Be  | 9 | T1 witness missing |

The sweep gracefully captures the `KeyError` per atom and reports
`"error": "KeyError: \"no canonical T1 for 'NLi'; …\""` in the
witness row (handler at `paper_six_term_isotope_sweep.py:846`).
The fix is to compute T1 = `tr_M(β_atomic(Z, N))` for A = 5..9 via
the per-irrep Hoefsmit numeric path (same machinery as the
`F1-braid` ⁴He probe). Partition counts grow rapidly:
n=15 → 176, n=18 → 385, n=21 → 792, n=24 → 1575, n=27 → 3010.
For n=12 (⁴He) the compute took 221 s with the new y_λ witness
fast-path; A=5..9 will take ~10 min to ~6 h per atom. Deferred to
a separate compute round.

## 4  V2 chirality — values vs prior production heuristic

| Atom | $a_K$ (old heuristic) | $a_K$ (V2) | ratio |
|------|--------------------:|----------:|------:|
| p    |   1.000 |  2.4237 | 2.42× |
| n    |   1.000 |  2.1336 | 2.13× |
| D    |   1.1097 |  5.2279 | 4.71× |
| T    |   1.000 | 10.4775 | 10.48× |
| ³He  |   1.000 | 13.9937 | 13.99× |
| ⁴He  | unknown  | 28.0456 | — |

The old heuristic `chirality_signs_for_isotope(iso)` returned
$\prod (1 + \mathrm{sign} \cdot h)$ over a hand-coded sign list, giving
$a_K \approx 1$ for all atoms with amphichiral cancellation, and
$a_K \approx 1.11$ for the deuteron. V2 is the canonical
substrate-derived $\tau(\beta \cdot \beta_{\mathrm{mirror}}^{-1})$
per [`prop:he4-channel-active-set`](../../content/quantum-observable-universe/braids-and-knots/he4-channel-active-set.md)
and the Gram-matrix conjecture, and the values scale with the
geometric mass parameter (heavier atoms have more crossings and
hence larger `a_K`).

## 5  Closure path — quantitative gates (cherry-picked from #655)

The 1 ppb closure path has two structurally-linked precision gates,
both quantified by the cherry-picked
[`audit_delta_S_chain.py`](../../computations/audit_delta_S_chain.py)
+ [`delta-S-chain-audit.witness.json`](../../computations/delta-S-chain-audit.witness.json)
finding:

- **$\varepsilon_{\Delta S} = (Q_\beta / (Q_\beta + m_e)) \cdot \varepsilon_Q
  \approx 0.605 \cdot \varepsilon_Q$** at 50 dps (chain match
  residual $2.6 \times 10^{-48}$).
- For 1 ppb on $\Delta S_{\mathrm{derived}}$
  ($\varepsilon_{\Delta S} \to 10^{-3}$ ppm), $Q_\beta$ closed form
  must tighten to $\varepsilon_Q \approx 0.0017$ ppm —
  **1700× tighter than current $+1677.54$ ppm**.

[`probe_q_beta_tightening_landscape.py`](../../computations/probe_q_beta_tightening_landscape.py)
+ [`q-beta-tightening-landscape.witness.json`](../../computations/q-beta-tightening-landscape.witness.json)
report a **5.49× tightening** by composing $Q_\beta$ with
$\cos((z-1) \cdot h/2)$: residual drops from $+1677.5$ ppm to
$+305.4$ ppm. This is the first positive structural identification
of a missing correction term in the closed form; remaining gap to 1
ppb is ~300×, candidates: per-irrep Hecke character corrections at
depth $N \geq 1$, multi-wrap NF contributions, crystal-graph parity
corrections.

## 6  Magic-shell coupling — substrate hypothesis (cherry-picked from #656)

[`probe_a_minus_2_q_substrate.py`](../../computations/probe_a_minus_2_q_substrate.py)
+ [`a-minus-2-q-substrate-probe.witness.json`](../../computations/a-minus-2-q-substrate-probe.witness.json)
+ [`docs/audits/2026-05-15-a-minus-2-q-substrate-derivation.md`](2026-05-15-a-minus-2-q-substrate-derivation.md)
extend this branch's F2 (H7a refuted at A=3) with three substrate-
derivation candidates and their cross-anchor test:

| Candidate | Mechanism | Status |
|---|---|---|
| D-1 KLR/BK graded character | $A-2$ interior interface slots | Falsified by single-magic gaps |
| D-2 q-Catalan multiplicity | $\mathrm{Cat}_q(A-1, 1) = [A-1]_q [A-2]_q / ([2]_q [A]_q)$ with Z/N-dependent SYT corrections | **Survives** |
| D-3 KLR-trace identity | Mathas/BK trace formula | Falsified (predicts universality) |

The follow-on
[`probe_interface_type_resolved_coupling.py`](../../computations/probe_interface_type_resolved_coupling.py)
localises the ³He proton-heavy anomaly to **pp-vs-nn interface
asymmetry** (asymmetric hook eigenline products through the
dominant antisymmetric column). The fit is exact at the three A=3
data points but not yet predictive; extension to {⁵Li, ⁶Li, ⁶He,
⁶Be} would give ≥ 4 independent $(n_{pp}, n_{nn})$ probes to test
whether the fit parameters have clean q-rational form.

The substrate candidate D-2 is the load-bearing piece for closing
the H7a Z↔N asymmetry that this branch's F2 refuted. Combined with
the F1 fingerprint result (two-row stratum carries 86.6 % of
$\mathrm{tr}_M(\beta_{^4\mathrm{He}})$ + D⊕D channel has the highest
LP shadow price), the structural account of doubly-magic ⁴He has
three independent confirmations:

1. **Two-row Wedderburn block dominance** ([`prop:he4-two-row-dominance`](../../content/quantum-observable-universe/braids-and-knots/he4-two-row-dominance.md))
2. **D⊕D channel LP shadow-price dominance** ([`prop:he4-channel-active-set`](../../content/quantum-observable-universe/braids-and-knots/he4-channel-active-set.md))
3. **q-Catalan multiplicity Cat_q(A-1, 1) at A=4** (cherry-picked D-2 candidate)

## 7  Recommended next steps

In priority order:

1. **Cherry-pick PR #655 / #656 closures** — after merge, the cherry-
   picked files here become canonical paths rather than local copies.
2. **Compute T1 witness for A ∈ {5, 6, 7, 8, 9}** via the per-irrep
   Hoefsmit numeric path. Unblocks the sweep for ⁵Li..⁹Be.
3. **Compose V2 chirality + cos$((z-1)h/2)$ Q_β tightening** —
   substrate-derived $a_K$ + structurally-identified Q_β correction
   should reduce the 1 ppb gap to ~300× from current 1700×.
4. **Wire D-2 q-Catalan candidate** into the magic-shell coupling
   formula and re-run F2 cross-anchor test at A=3.
5. **Compose F1 + D-2** — the two-row stratum dominance + q-Catalan
   multiplicity prediction should give a closed-form prediction for
   the doubly-magic Δ_coupling(2, 2) value, not just an anchor fit.
