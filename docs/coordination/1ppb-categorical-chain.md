# Coordination ledger: 1 ppb categorical-chain frontier

Tracking PRs working toward the 1 ppb $Q_\beta$ / mass-table goal.

## Scope map (2026-05-17)

| PR | Branch | Author | Role |
|---|---|---|---|
| [#665](https://github.com/litlfred/qou/pull/665) | `claude/knot-volumes-review-Pgt8o` | claude (this session) | N=4 + σ_1 + n-strand foundation + scaffolds |
| [#672](https://github.com/litlfred/qou/pull/672) | `claude/post-665-open-rd-hoefsmit-matrices` | claude (this session) | R&D inventory + YB d_1↔d_2 finding |
| [#664](https://github.com/litlfred/qou/pull/664) | `claude/post-662-c3-chain-anti-staleness` | claude (other session) | `prop:hopf-jones-c3-categorical` (alternate c_3 = −2 proof) |
| [#671](https://github.com/litlfred/qou/pull/671) | `claude/post-670-story-b-mp-c5-c6` | claude (other session) | Story B forced audit + m_p chain closure gap |
| [#663](https://github.com/litlfred/qou/pull/663) | `claude/isotope-mass-witness-data-x5lCh` | claude (other session) | isotope-mass-table + anti-staleness infra |

## Classification

| pair | overlap | dependency | cherry-pick |
|---|---|---|---|
| #665 ↔ #672 | HIGH (#672 follows #665) | #672 depends on #665 | — |
| #665 ↔ #664 | HIGH (same c_3 = −2, different proof paths) | independent | none planned; cross-ref both after merge |
| #665 ↔ #671 | MEDIUM (same Story B framing) | independent | none |
| #665 ↔ #663 | LOW (different files, different topic) | #663 consumes substrate Q_β; could swap to N=4 once #665 lands | none |
| #672 ↔ #664 | MEDIUM (#672 documents YB anomaly; #664 may implicitly need YB) | independent | none |

## Coordination comments posted

- [#664 — coordination from #665+#672](https://github.com/litlfred/qou/pull/664#issuecomment-4469105688)
- [#671 — coordination from #665+#672](https://github.com/litlfred/qou/pull/671#issuecomment-4469149330)
- [#663 — Q_β substrate swap opportunity](https://github.com/litlfred/qou/pull/663#issuecomment-4468003754) (earlier)

## Cross-PR findings affecting siblings

### YB cubic d_1↔d_2 anomaly (PR #672)

Symbolic computation shows the chapter `hoefsmit_sigma1` matrices
fail YB cubic with `σ_0 = diag(q, −q⁻¹)`. Analytical fix: swap
`hoefsmit_d1` and `hoefsmit_d2` in
`hoefsmit-V21-cos-symmetrization.lean`. Zero downstream regressions
(basis-permutation preserves all scalar invariants).

**Implications for siblings**:
- #664: Step 2 ("Frobenius selection picks V_(2,2,2) at order h⁶")
  may or may not depend on YB-compatible σ_1 conventions. Coordination
  comment posted asking; awaiting response.
- #665: cross-PR fix commit `df5621609` removes the vacuous
  `yangBaxter_H3 := ⟨0, rfl⟩` instance to avoid asserting a falsehood
  under current conventions.

## Open questions for the author

1. **Q_β substrate swap on #663**: ship #663 as-is with `form_a_cos`
   (residual +306 ppm), or wait for #665 to land then swap to the
   N=4 ladder (residual ~7e-6 ppm)?
2. **c_3 cross-references**: after #665 and #664 both land, should
   `prop:q-beta-c3-hopf-three-fold-markov` (#665) cite
   `prop:hopf-jones-c3-categorical` (#664) as upstream, or vice-versa?

## Next concrete task (non-overlapping)

Await Gemini/Copilot review responses on #665 and #672; address as
they come in. R&D items 1-5 (from #672's inventory) are queued for
follow-up branches; none touch sibling PR scopes.

## 2026-05-19 — Δ_λ categorical closure (branch `claude/closed-forms-first-principles`, no PR)

| Date | Branch / PR | Phase | Status | Cherry-pick |
|---|---|---|---|---|
| 2026-05-19 | `claude/closed-forms-first-principles` (no PR) | Phase 1a — conjecture block | landed `66c655ed` | `conj:delta-lambda-categorical-closure` content triple |
| 2026-05-19 | same | Phase 1b — verification on deuteron | landed `8da9ca67`; **NEGATIVE** — naive form misses by 33× | `delta_lambda_categorical_verification.py` + witness |
| 2026-05-19 | same | Δ_λ exploration | landed `7f82b0c9` | 3 Galois orbits via reciprocal cubic $16w^3+24w^2-13w+2=0$; $k=2$-residue-zero anomaly; per-knot factor required (T/³He degeneracy falsifies universal-c) |

**Findings load-bearing for the 1ppb / 1ppm thread:**

1. **Δ_λ depends on knot K beyond χ^λ.** Cross-atom test: T (c=20.7) vs ³He (c=7.14) at same n=9. Universal-c hypothesis falsified. Δ_λ closure requires a per-knot factor (likely JSJ volume).

2. **Discriminant 3-orbit structure** (palindromic Δ(z) → reciprocal cubic) is the categorical refinement of PR #779's "principal pair". 3 orbits available for per-block selection.

3. **$k=2$ residue vanishes** identically across all 3 orbits. Constrains the k(λ) mapping to $\{0, 1, 3\}$.

**Proposed Phase 2 closure form:**

$$\Delta_\lambda(K) = \mathrm{Vol}_{\mathrm{hyp}}^{(\lambda)}(K) \cdot \tau_q\!\Bigl(\sum_{p \in \mathcal{O}^{(\lambda)}} \mathrm{Res}^{\mathrm{alg}}_p (\lambda^{(k(\lambda))}_{\mathrm{SW}})\Bigr)$$

**Coordination posts:**
- [PR #777 comment](https://github.com/litlfred/qou/pull/777) — intent + 2 asks
- [PR #781 comment](https://github.com/litlfred/qou/pull/781) — light-touch downstream-consumer notice

**Holding** Phase 2 until PR #777's owner confirms (i) the closure is outside the 6 banned fit ansätze and (ii) PR #708's `Vol_hyp^(λ)(K)` machinery is accessible.

## 2026-05-19 — Δ_λ Phase 2 + Phase 3 (branch `claude/closed-forms-first-principles`, [PR #787](https://github.com/litlfred/qou/pull/787))

| Date | Phase | Status | Cherry-pick |
|---|---|---|---|
| 2026-05-19 | Phase 2 (two-factor V(K)·c_λ) | landed `b4e196e2`; **FALSIFIED** on 8 V(K) candidates | `delta_lambda_two_factor_phase2.py` + falsification doc |
| 2026-05-19 | Phase 3 (JSJ Vol via SnapPy) | landed `b7b11519`; **FALSIFIED** (rel_std 1.4) but reveals **Vol(canonical(K)) clusters by Z** | `delta_lambda_jsj_phase3.py` + Vol_hyp(D)=Vol(T)=12.776; Vol(³He)=Vol(⁴He)=12.554 |
| 2026-05-19 | Coord on #777 | comment posted (this round) | asks #1 (f64-vs-mpmath knot-vol audit) and #2 (per-JSJ-piece quantum-invariant infrastructure) |

**Hard categorical finding (Phase 3):** Vol_hyp of the canonical atomic braid closure is **invariant under adding nucleons at fixed Z**. The N-direction is Seifert-fibered (Vol contribution = 0). Per-N binding-energy structure must live in Seifert-piece quantum invariants, not in the hyperbolic core.

This **constrains** PR #781's Kashaev mass-table formula (ρ_F · Vol_hyp) — same-Z isotopes should use the same Vol per my Phase 3 measurement; if PR #781 assigns different Vol to D vs T (same Z=1), that's a discrepancy worth surfacing.

**Status**: Δ_λ thread **paused** at PR #787 pending owner answers on the per-JSJ-piece-quantum-invariant infrastructure (ask #2). If no such infrastructure, the branch lands as a diagnostic package (3 phases of productive negatives + Z-clustering structural finding) and the thread pivots to another closed-form option.

## 2026-05-19 — log-Δ categorical derivation → Δ_I^K interface knot (branch `claude/log-delta-categorical-derivation`, [PR #801](https://github.com/litlfred/qou/pull/801))

| Date | Phase | Status | Cherry-pick |
|---|---|---|---|
| 2026-05-19 | Phase 1 — 3 weight forms (y_λ / ~w_λ / identity) | landed `43e3e6fd`; best 4.6× variance (identity weighting) | `log_delta_categorical_derivation.py` |
| 2026-05-19 | Phase 2 — full-mass-subtract, $B = m_K - Z m_p - N m_n$ | landed `dac29b44`; **3.96× best** (paper weight ~w_λ) but T/³He **WRONG SIGN** | `log_delta_full_mass_subtract.py` |
| 2026-05-19 | Phase 3 — per-depth-stratified subtraction | landed `433de5c1`; identical 3.96× (constituents max depth 2 in $H_3$) | `log_delta_per_depth_binding.py` |

**Hard structural finding (re-reading the paper after user pushback):**
Tensor-product baseline $Z \cdot \mathfrak{m}(\beta_p) + N \cdot \mathfrak{m}(\beta_n)$
**in independent $H_3$ algebras** is structurally wrong. The categorically-correct composite is
$$\beta_K = \underbrace{\beta_p^{(1)} \cdots \beta_n^{(N)}}_{T_{\text{constit}}^K \text{ on disjoint strand blocks}} \cdot \Delta_I^K \;\in\; H_{3(Z+N)}(q)$$
per [`def:ew-interface-knot`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/ew-interface-knot.md)
and [`prop:atomic-mass-gb-nf`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/atomic-mass-gb-nf.md).
Deuteron has $\Delta_I^D = \sigma_3$ (the `+1` in $u_{\text{shift}} = 18Z + 21N + 1$). T, ³He, ⁴He each have their own $\Delta_I^K$ characterising "what is involved in binding at that confinement level".

**Resolution path (in flight):** Recompute $B(K) = \mathfrak{m}(\beta_K) - \mathfrak{m}(T_{\text{constit}}^K)$ with both braids in the **same** Hecke algebra. Mass-endomorphism conditions (Markov-invariance term-by-term, $|S| \le 2$ R-side bound, symmetric $\mathrm{Li}_2^q$ form, spectral-sequence collapse, $B(p) = B(n) = 0$) satisfied by construction.

**Coordination posts:**
- [PR #800 comment](https://github.com/litlfred/qou/pull/800#issuecomment-4484723377) — informational, no overlap with I13 sweep
- [PR #761 comment](https://github.com/litlfred/qou/pull/761#issuecomment-4484724112) — ask about GP MPFR engine accepting arbitrary braid-word input for $T_{\text{constit}}^K$ chi computation

**Alignment note:** Will add `canonical_status` taxonomy field per branch `claude/canonical-discipline-l1-l3-l4-2026-05-19` (commit `98ed2add`) to all new witnesses. Categorical-substrate path; not L3 heuristic.

### 2026-05-19 — interface-knot Δ_I^K result on PR #801

| Date | Phase | Status | Cherry-pick |
|---|---|---|---|
| 2026-05-19 | Δ_I^K + same $H_{3(Z+N)}$ baseline (T1+T2 first-order) | landed `5b620576`; **variance 3.96× → 2.31×, T/³He sign-fixed** | `binding_via_interface_knot.py` (consumes existing `atom_braid_word_3A(include_inter=True/False)` toggle) |

**Hard improvement vs tensor-product baseline:**
- D: B_pred = 1.566 MeV (AME 2.225, ratio 0.704)
- T: B_pred = 2.582 MeV (AME 8.482, ratio 0.304)
- ³He: B_pred = 2.618 MeV (AME 7.718, ratio 0.339)
- max/min = 2.31× (was 3.96× tensor)
- ALL signs positive (was T/³He wrong sign under tensor)

**Deferred to next iteration:**
- ⁴He H_12 character sum requires > 12 GB RAM on this host. Witness records `atoms_deferred: ["4He"]` with `INCLUDE_4HE=1` env-flag override.
- T3 (pair) closure pending: for some pairs in H_{3A>3}, |V̂_i V̂_j| > q_0 ≈ 1.1097 exceeds Li_2^q convergence radius. Three structural options identified in PR body.

**Canonical_status taxonomy alignment:** all 4 witnesses on this branch (3 phase scripts + interface-knot) now carry `canonical_status: canonical-with-empirical-assignment` per the new taxonomy from `claude/canonical-discipline-l1-l3-l4-2026-05-19` commit `98ed2add`.

### 2026-05-19 — Block-multiplicativity scaling on PR #801 (followups)

| Date | Phase | Status | Cherry-pick |
|---|---|---|---|
| 2026-05-19 | Block-multiplicativity scaling (16 atoms D → ⁵⁶Fe) | landed `f43da415`; **variance 5.47× T1+T2, 1.65× medium A=6..14, 10.99× all 16 (T3 over-counts A²)** | `binding_block_multiplicative.py` + `conj:block-multiplicativity-v-free` content triple |
| 2026-05-19 | T3 closure via interface-pair structural cancellation | landed `65a3985e` + `f00ae129`; finite even though T3_free / T3_atom individually diverge | structural cancellation rule (non-interface pairs cancel) |
| 2026-05-19 | Coord on PR #814 (silver-ratio Q_β null / Pell-Lucas c_k) | comment posted | ask on involution/Leibniz origin of c_5 generalising to α_{k≥4} damping |

**Structural finding (verified empirically at A=2,3 exact to 4 digits):** per-generator V̂ values at H_{3A} are A-INDEPENDENT for the disjoint Hecke product. Block factors v_p = 0.7084, v_n = 0.6005, |V^pp/nn_inter| = 0.1045, |V^pn_inter| = 0. Scales B(K) prediction to ALL atoms in microseconds — no H_{3A} character sum beyond H_6 / H_9 calibration. Conjecture content block + Lean class committed (`conj:block-multiplicativity-v-free`).

**Open structural target (heavy-atom variance):** T3 pair-blowup grows as A² (number of interface-involving pairs ≈ 5A(A-1)/2). AME binding grows linearly in A. The mismatch may be resolved by switching from the mass-endomorphism blow-up tower (T1+T2+T3) to the **depth-stratified α_k · Φ_k formulation** for k ≥ 4 — where α_{k≥4} = m_e · 8G provides built-in damping at high curvature rank ([`prop:plancherel-term-7-formulation`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/plancherel-term-7-formulation.md)). Cross-reference to PR #814's involution/Leibniz analysis of c_5's 1/2 fingerprint — same averaged-crossing mechanism plausibly drives the α_{k≥4} damping universal at depth k ≥ 4.
## 2026-05-19 (evening) — Deprecated-but-valid catalog re-verification (branch `claude/update-deprecated-scripts-catalog-jvbyM`)

| Date | Phase | Status | Cherry-pick |
|---|---|---|---|
| 2026-05-19 | Re-verify the 11-row table in [`docs/audits/2026-05-19-deprecated-but-valid-scripts-catalog.md`](../audits/2026-05-19-deprecated-but-valid-scripts-catalog.md) (authored on PR #787 morning) | Update landed on this branch — 7 propositions still actionable, 2 phantom labels removed, 3 wired-to-alternate need supersession check, 25 (not ~30) deprecated scripts confirmed orphaned | catalog update + ledger row (this row) |

**Re-survey findings load-bearing for the 1 ppb / Δ_λ thread:**

1. **No deprecated-script revivals** since #787 merged (`git log origin/main -- folio-assistant/computations/_deprecated/` returns zero). The systemic paper↔compute wiring gap persists.
2. **3 propositions wired to *alternate* scripts**, not the catalog's deprecated ones — supersession-disposition still owed:
   - `prop:mass-endomorphism-tower` → `habiro_exact_mass_endomorphism.py` (337 LoC); 4 deprecated towers orphaned.
   - `prop:atomic-mass-gb-nf` → `canonical_mass_table_extended.py` (507 LoC); `anti_self_reciprocity_universality_probe.py` orphaned.
   - `prop:full-pole-structure-mass-trace` → `markov_substrate_realizer.py` (242 LoC); **8** `build_*_chain.py` (~2200 LoC) orphaned — largest scope gap.
3. **2 phantom-label rows** in the original catalog (`prop:atomic-braid-mass`, `prop:b-over-a-spectral-decomposition`) — neither label exists in `content/`. Either author the missing propositions or delete the rows (and dispose of `atomic_braid_mass_paper_formula.py`, `b_over_a_evaluator.py`).
4. **Two cross-cutting caveats** added to the catalog's revival procedure: (i) TR_M[5] Markov-trace bug fix (`be773569`) may invalidate witnesses from un-patched code paths; (ii) PR #787 Phase 3 Vol-clusters-by-Z finding constrains what an N-dependent binding-energy formula can look like — useful as a falsifiability gate.

**Coordination posts**: none required this round — the affected propositions are unowned (no open PR is reviving any of them), and the systemic finding is documented in the catalog + ledger row above. If a future PR proposes reviving a catalog-listed script, the reviver should consult both caveats before running.

**Next concrete tasks (non-overlapping, queued for whoever picks up):**

- Pick one of the 7 actionable propositions (highest yield: `prop:unified-curvature-rank-mass-formula` if the Δ_λ thread unpauses; otherwise `prop:confinement-categorical` since it's a single-script revival) and run the catalog's per-revival procedure end-to-end.
- For the 3 wired-to-alternate propositions, diff the live and deprecated scripts and decide supersession (move to `_deprecated/_archive/`) or scope-gap (fold logic in / re-wire to consume both). The `prop:full-pole-structure-mass-trace` case is the most interesting because the 8 `build_*_chain.py` scripts collectively dwarf the single live realizer.
- For the 2 phantom labels, ask the original author whether the underlying claims were intended to exist as separate blocks, or whether the scripts should be re-deprecated under a different proposition (or moved to `_archive/`).
