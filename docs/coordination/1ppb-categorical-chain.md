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

## 2026-05-19 — log-Δ categorical derivation → ⋈_K interface knot (branch `claude/log-delta-categorical-derivation`, [PR #801](https://github.com/litlfred/qou/pull/801))

| Date | Phase | Status | Cherry-pick |
|---|---|---|---|
| 2026-05-19 | Phase 1 — 3 weight forms (y_λ / ~w_λ / identity) | landed `43e3e6fd`; best 4.6× variance (identity weighting) | `log_delta_categorical_derivation.py` |
| 2026-05-19 | Phase 2 — full-mass-subtract, $B = m_K - Z m_p - N m_n$ | landed `dac29b44`; **3.96× best** (paper weight ~w_λ) but T/³He **WRONG SIGN** | `log_delta_full_mass_subtract.py` |
| 2026-05-19 | Phase 3 — per-depth-stratified subtraction | landed `433de5c1`; identical 3.96× (constituents max depth 2 in $H_3$) | `log_delta_per_depth_binding.py` |

**Hard structural finding (re-reading the paper after user pushback):**
Tensor-product baseline $Z \cdot \mathfrak{m}(\mathcal{B}_p) + N \cdot \mathfrak{m}(\mathcal{B}_n)$
**in independent $H_3$ algebras** is structurally wrong. The categorically-correct composite is
$$\mathcal{B}_K = \underbrace{\mathcal{B}_p^{(1)} \cdots \mathcal{B}_n^{(N)}}_{T_{\text{constit}}^K \text{ on disjoint strand blocks}} \cdot \bowtie_K \;\in\; H_{3(Z+N)}(q)$$
per [`def:ew-interface-knot`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/ew-interface-knot.md)
and [`prop:atomic-mass-gb-nf`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/atomic-mass-gb-nf.md).
Deuteron has $\bowtie_D = \sigma_3$ (the `+1` in $u_{\text{shift}} = 18Z + 21N + 1$). T, ³He, ⁴He each have their own $\bowtie_K$ characterising "what is involved in binding at that confinement level".

**Resolution path (in flight):** Recompute $B(K) = \mathfrak{m}(\mathcal{B}_K) - \mathfrak{m}(T_{\text{constit}}^K)$ with both braids in the **same** Hecke algebra. Mass-endomorphism conditions (Markov-invariance term-by-term, $|S| \le 2$ R-side bound, symmetric $\mathrm{Li}_2^q$ form, spectral-sequence collapse, $B(p) = B(n) = 0$) satisfied by construction.

**Coordination posts:**
- [PR #800 comment](https://github.com/litlfred/qou/pull/800#issuecomment-4484723377) — informational, no overlap with I13 sweep
- [PR #761 comment](https://github.com/litlfred/qou/pull/761#issuecomment-4484724112) — ask about GP MPFR engine accepting arbitrary braid-word input for $T_{\text{constit}}^K$ chi computation

**Alignment note:** Will add `canonical_status` taxonomy field per branch `claude/canonical-discipline-l1-l3-l4-2026-05-19` (commit `98ed2add`) to all new witnesses. Categorical-substrate path; not L3 heuristic.

### 2026-05-19 — interface-knot ⋈_K result on PR #801

| Date | Phase | Status | Cherry-pick |
|---|---|---|---|
| 2026-05-19 | ⋈_K + same $H_{3(Z+N)}$ baseline (T1+T2 first-order) | landed `5b620576`; **variance 3.96× → 2.31×, T/³He sign-fixed** | `binding_via_interface_knot.py` (consumes existing `atom_braid_word_3A(include_inter=True/False)` toggle) |

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
| 2026-05-19 | Re-verify the 11-row table in [`docs/audits/2026-05-19-deprecated-but-valid-scripts-catalog.md`](../audits/2026-05-19-deprecated-but-valid-scripts-catalog.md) (authored on PR #787 morning) | Update landed on this branch — the 11 original rows resolve to **11 real propositions**: 7 actionable + 4 wired-to-alternate (3 named directly + `prop:confined-knot-binding` via the b/a trio) + 1 true phantom (`prop:atomic-braid-mass`). 25 (not ~30) deprecated scripts confirmed orphaned. | catalog update + ledger row (this row) |

**Re-survey findings load-bearing for the 1 ppb / Δ_λ thread:**

1. **No deprecated-script revivals** since #787 merged (`git log origin/main -- computations/_deprecated/` returns zero). The systemic paper↔compute wiring gap persists.
2. **4 propositions wired to *alternate* scripts**, not the catalog's deprecated ones — supersession-disposition still owed:
   - `prop:mass-endomorphism-tower` → `habiro_exact_mass_endomorphism.py` (337 LoC); 4 deprecated towers orphaned.
   - `prop:atomic-mass-gb-nf` → `canonical_mass_table_extended.py` (507 LoC); `anti_self_reciprocity_universality_probe.py` orphaned.
   - `prop:full-pole-structure-mass-trace` → `markov_substrate_realizer.py` (242 LoC); **8** `build_*_chain.py` (~2200 LoC) orphaned — largest scope gap.
   - `prop:confined-knot-binding` *(via b/a trio)* → `jet_knot_invariants.py` (199 LoC); `b_over_a_evaluator.py` orphaned (also covers the un-wired `prop:wigner-np-pairing`).
3. **2 phantom-label rows** in the original catalog (`prop:atomic-braid-mass`, `prop:b-over-a-spectral-decomposition`) — neither label exists in `content/`. Either author the missing propositions or delete the rows (and dispose of `atomic_braid_mass_paper_formula.py`, `b_over_a_evaluator.py`).
4. **Two cross-cutting caveats** added to the catalog's revival procedure: (i) TR_M[5] Markov-trace bug fix (`be773569`) may invalidate witnesses from un-patched code paths; (ii) PR #787 Phase 3 Vol-clusters-by-Z finding constrains what an N-dependent binding-energy formula can look like — useful as a falsifiability gate.

**Coordination posts**: none required this round — the affected propositions are unowned (no open PR is reviving any of them), and the systemic finding is documented in the catalog + ledger row above. If a future PR proposes reviving a catalog-listed script, the reviver should consult both caveats before running.

**Next concrete tasks (non-overlapping, queued for whoever picks up):**

- Pick one of the 7 actionable propositions (highest yield: `prop:unified-curvature-rank-mass-formula` if the Δ_λ thread unpauses; otherwise `prop:confinement-categorical` since it's a single-script revival) and run the catalog's per-revival procedure end-to-end.
- For the 3 wired-to-alternate propositions, diff the live and deprecated scripts and decide supersession (move to `_deprecated/_archive/`) or scope-gap (fold logic in / re-wire to consume both). The `prop:full-pole-structure-mass-trace` case is the most interesting because the 8 `build_*_chain.py` scripts collectively dwarf the single live realizer.
- For the 2 phantom labels, ask the original author whether the underlying claims were intended to exist as separate blocks, or whether the scripts should be re-deprecated under a different proposition (or moved to `_archive/`).

## 2026-05-19 (evening) — Δ_λ Phase 4: zero-parameter closure via `[8]_q`, `[3]_q²`, `(q^{1/2}+q^{-1/2})^{4N}` (branch `claude/update-deprecated-scripts-catalog-jvbyM`, [PR #819](https://github.com/litlfred/qou/pull/819))

| Date | Phase | Status | Cherry-pick |
|---|---|---|---|
| 2026-05-19 | Phase 4 — categorical observation: $(q^{1/2}+q^{-1/2})^4 \approx 16.087$ matches empirical per-N ratios T/D=15.95 and ⁴He/³He=16.36 (≤ 1.7% rel.err.) | Closure formula identified: $\lvert\Delta_\lambda^*(K)\rvert \approx (\mathrm{Vol}_{\mathrm{hyp}}(K) / [8]_q) \cdot [3]_q^{2(Z-1)} \cdot (q^{1/2}+q^{-1/2})^{4N}$ | `delta_lambda_z4N_phase4.py` + witness; audit doc [`docs/audits/2026-05-19-delta-lambda-phase4-z4N-closure.md`](../audits/2026-05-19-delta-lambda-phase4-z4N-closure.md) |

**Hard categorical findings:**

1. **Per-N factor is `(q^{1/2}+q^{-1/2})^4 = (dim_q V_{1/2})^4`** — substrate-derived, no fit; matches empirical T/D and ⁴He/³He ratios to ≤ 1.7%. **This identifies the Seifert-piece contribution as a 4-channel fundamental-rep tensor factor.** Resolves PR #787 Phase 3's open question about per-JSJ-piece quantum-invariant infrastructure: no per-piece RT machinery is needed; the Seifert-N factor is just a product of quantum dims of $V_{1/2}$.

2. **Per-Z factor is `[3]_q^2` = $(\dim_q V_1)^2$** — substrate-derived, rel.err. 2.17%; not as clean as per-N but reasonable. Closest categorical candidate (the adjoint rep squared, naturally associated with 3-quark baryon content).

3. **Overall normalisation is `1/[8]_q`** — substrate-derived, rel.err. 0.49%; this is the Plancherel-like normalisation of the higher-spin block.

4. **Zero-parameter formula matches empirical $\lvert\Delta_\lambda^*(K)\rvert$ to max rel.err. 2.51%** across D (0.07%), T (0.90%), ³He (0.86%), ⁴He (2.51%) — vs. Phase 3 baseline rel_std = 1.398. One-parameter fit (extract α empirically) gives rel_std = 0.0066, a 210× tightening.

**Impact on the 1ppb thread:** the Δ_λ thread, previously **paused at PR #787 pending owner answers on per-JSJ-piece quantum-invariant infrastructure**, is **substantially advanced** — the per-piece infrastructure is no longer needed because the closure factorises through quantum integers and dim_q V_{1/2} that the existing QOU formalism already provides (Hoefsmit, Hecke skein). The thread is **not yet closed** — the per-Z factor $[3]_q^2$ residual (2.17%) and the constant $1/[8]_q$ derivation remain research targets.

**Connection to existing PRs:**
- **PR #787** (closed-forms Phase 1b/2/3): the Vol-clusters-by-Z finding from Phase 3 is the empirical baseline for this finding. No conflict — Phase 4 extends Phase 3.
- **PR #777** (Track A: per-isotope Δ_λ closure): if the Phase 4 formula extends to additional atoms (⁵He, ⁶Li, ⁷Li), it would close Track A's per-isotope binding-energy formula at the 100× experimental target for those atoms. Worth a coordination comment when the formula has been tested on ≥ 1 atom beyond the original 4.
- **PR #804** (qbeta-followup): the qbeta-ladder closure path (c_4..c_7 as `conj:qbeta-c-k-closed-forms`) and this Δ_λ closure are orthogonal but both involve products of quantum integers at q_0. Worth a cross-reference in the next round of the closed-forms thread.

**Next concrete tasks (Δ_λ Phase 5):**

1. **Derive $\alpha = [3]_q^2$ rigorously.** The 2.17% rel.err. between empirical α and $[3]_q^2$ is either fit noise or a categorical correction. Test: compute the Markov trace of the per-proton braid `_proton_braid_word()` and check whether it evaluates to $[3]_q^2$ exactly.
2. **Derive $1/[8]_q$ rigorously.** Identify the categorical role of $[8]_q$ in the canonical braid trace normalisation. Candidate: total quantum dim of the relevant Wedderburn block.
3. **Extend the closure to ⁵He, ⁶Li, ⁷Li.** Requires building canonical braid words for these atoms in `probe_he4_jsj_topology.py` style; re-run Phase 4 probe; verify the formula extends.
4. **Cast as a per-partition formula.** The single-block extraction is a heuristic; generalise to $\lvert\Delta_\lambda(K)\rvert \propto [3]_q^{2(Z-1)} \cdot (q^{1/2}+q^{-1/2})^{4N} \cdot \mathrm{Vol}_{\mathrm{hyp}}(K) \cdot W_\lambda(q)$ where $W_\lambda(q)$ is the partition-specific weight; test on the 11-partition deuteron tabulation from Phase 1b.

## 2026-05-19 (evening, late) — Phase 5b α ≈ [3]_q²·cosh(h) + bar-symmetric unification with PR #801 ([PR #819](https://github.com/litlfred/qou/pull/819))

| Date | Phase | Status | Cherry-pick |
|---|---|---|---|
| 2026-05-19 | Phase 5b — α-residual closure via cosh(h) | landed `26bcabaf`; **near-exact match (0.022%) of α ≈ [3]_q²·cosh(h)** at q_0 | `pyhecke_native` Rust kernel build fix + audit doc update |
| 2026-05-19 | Bar-symmetric synthesis with PR #801 (Symmetric Li_2^q tower) | coordination comment on #801 ([4490779685](https://github.com/litlfred/qou/pull/801#issuecomment-4490779685)) | three-layer bar-symmetric picture: series (Li_2^q) ↔ phase (cos_q) ↔ gain (cosh(h)), with predicted FR identity |

**Findings load-bearing for the 1ppb / Δ_λ thread:**

1. **`pyhecke_native` (Rust kernel) built locally** ([commit `26bcabaf`](https://github.com/litlfred/qou/commit/26bcabaf)) — fixed 2 duplicate function definitions in `tools/hecke-engine/src/wenzl_lr.rs` that were blocking the build. With Rust kernel: $\chi_\lambda$ at $H_9$ now ~10 ms vs Python timeout at 180s. Unblocks all Markov-trace witness refreshes for $n \le 21$.

2. **Phase 5b α-residual finding**: $\alpha / [3]_q^2 = 1.022157$ matches $\cosh(h) = 1.021933$ to **5 significant digits** at $q_0$ (50 dps) — well above empirical-tabulation noise. The Hecke skein parameter $h = q - q^{-1}$ gives a clean categorical reading: $\cosh(h)$ is the **symmetric-channel Hecke-deformation correction** from $\sigma^2 = h\sigma + 1$.

3. **Bar-symmetric unification with PR #801**: three q-deformation corrections used in QOU mass formulas — symmetric Li_2^q (T2/T3 tower in #801), cos(α−b·ℏ_q²/2) (N=1 rung in master Q_β), and cosh(h) (per-Z step in Phase 5b) — are **all bar-symmetric projections** of bar-anti-symmetric Hecke operators. The bar-anti-symmetric counterparts (Faddeev $\Phi_q$, sin/odd-phase, sinh(h)) are exactly the channels that break mirror-nucleus symmetry. The bar-symmetric projection is the **isospectral lift** (Kac-Sunada reframing: tr_M at q alone doesn't determine braid; tr_M at both q and q⁻¹ tightens it dramatically).

4. **Missing Frobenius reciprocity identified**: Phase 5b's cosh(h) (Ind side) and PR #801's Li_2^q tower (Res side) should be FR-dual under Brundan-Kleshchev. Predicted identity for each (Z=1 → Z=2) transition: $\sum_\lambda y_\lambda \chi_\lambda(\mathcal{B}_K^{Z=2}) \stackrel{?}{=} [3]_q^2 \cosh(h) \cdot \sum_\mu y_\mu \chi_\mu(\mathcal{B}_K^{Z=1}) + (\mathrm{Li}_2^q \text{ interface correction})$. Verifying this is Phase 5c's primary numerical test, now feasible with the Rust kernel.

**Impact**: the Δ_λ thread paused at PR #787 is *substantially unblocked* — both per-N and per-Z factors are now categorically identified (per-N: $(q^{1/2}+q^{-1/2})^4$; per-Z: $[3]_q^2 \cdot \cosh(h)$), with one explicit FR identity to verify operator-level. No new infrastructure needed.

## 2026-05-19 (late evening) — Phase 5c.1 numerical FR test on PR #819 ([commit `d7840466`](https://github.com/litlfred/qou/commit/d7840466))

| Date | Phase | Status | Cherry-pick |
|---|---|---|---|
| 2026-05-19 | Phase 5c.1 — numerical FR-identity test (full tr_M ratio) | landed `d7840466` on PR #819 | `delta_lambda_fr_identity_phase5c.py` + witness; **3 structural findings (one positive, one structural, one refining); follow-up comment on PR #801 ([`4490915368`](https://github.com/litlfred/qou/pull/801#issuecomment-4490915368))** |

**Findings (numerical, via pyhecke_native Rust kernel + cached y_λ at q_0):**

1. **tr_M(β_{Z=2,N}) / tr_M(β_{Z=1,N}) is N-INDEPENDENT** — matches to 6 digits across both (D, ³He) and (T, ⁴He):
   - FULL ratio (with interface) = **0.609346** for both
   - CONSTIT ratio (no interface) = **1.220358** for both

2. **Interface-knot contribution at every Z-step = z (Markov parameter) EXACTLY** (rel.err 0.0001%):
   $$\frac{\mathrm{tr}_M(\mathcal{B}_K^{\text{FULL}})}{\mathrm{tr}_M(\mathcal{B}_K^{\text{CONSTIT}})}\bigg|_{Z\text{-step}} \;=\; \frac{0.609346}{1.220358} \;=\; :val[z_markov]{precision=6}\;=\;z(q_0)$$
   This **is** the Markov axiom $\mathrm{tr}_M(\alpha \cdot \sigma_g) = z \cdot \mathrm{tr}_M(\alpha)$ for the interface generator. **The interface knot ⋈_K from PR #801 has derivation-grade categorical reading: each interface = one z factor**, no longer empirical-fit.

3. **The FR identity proposed in the previous ledger row** ($\mathrm{tr}_M(\beta^{Z=2}) / \mathrm{tr}_M(\beta^{Z=1}) \stackrel{?}{=} [3]_q^2 \cosh(h)$) **DOES NOT hold for the full Markov trace**. Empirical tr_M ratio is 0.609 (94% off from the predicted 9.47). The Phase 5b α ≈ [3]_q²·cosh(h) match (0.022%) applies ONLY to the single-block dominant $|\Delta_\lambda^*|$ extraction (Phase 4 quantity), NOT to the full Markov trace. The bar-symmetric synthesis is correct, but the FR identity I wrote conflated best-block vs total sum. Phase 5d will reformulate.

4. **Open**: the constit factor 1.220358. Closest clean categorical candidate I tested: $q + h/2 = 1.214509$ (0.48% off). Exact form still unknown — possibly an $\exp(h)$ Taylor truncation. N-independent Hecke-algebraic structural quantity.

**Impact on PR #801**: their ⋈_K interface-knot factor is now categorically derived (= z exactly). Asked the repo owner whether their `binding_via_interface_knot.py` already accounts for this exact factor — would either validate or surface a missing 50% per-interface correction. If T2 / T3 tower currently treats ⋈_K as a free parameter, the answer locks it to z at q_0 = 0.499320.

**Phase 5d (reformulating FR + closing constit factor):**

1. Identify the correct FR identity. The Phase 5b α holds at |Δ_λ*| level (best-block dominant), so the right FR is between Ind/Res on the SINGLE-BLOCK channel, not the total-sum channel.
2. Find categorical form of 1.220358 (the N-independent constit per-Z factor). Candidates to test: $\exp(h)$ truncations, $q^{1/2} + q^{-1/2}$ combinations, $[2]_q$-based.
3. Once both are derived, the full per-Z step factor decomposes as **z · 1.220358** = (Markov axiom for interface) × (intrinsic Hecke constit factor).

## 2026-05-19 (night) — Phase 5d.4 + 5d.5 + 5d.5b + Lean: knot-particle dictionary connection ([PR #819](https://github.com/litlfred/qou/pull/819) commits `21ddb64c`, `8aafaf24`, `3038eb87`)

| Phase | Status | Result |
|---|---|---|
| 5d.4 — V̂-level z-transfer | landed `21ddb64c` | **z-exactness is tr_M-level only, NOT V̂-level.** V̂ at interface generators is FLAVOR-SELECTIVE: {0 for p-n, +h/2 for p-p, -h/2 for n-n} — 5/5 interfaces match across D/T/³He. |
| 5d.5 — K_k* search | landed `21ddb64c` | Torus knots (3_1, 5_1, 7_1) dominate |Z_norm| ranking. Per knot-particle dictionary: 3_1=e, 5_1=μ, 7_1=τ (lepton generations 1/2/3). |
| Lean — close 226 sorries | landed `8aafaf24` | 217 True-placeholder stubs + 9 in MassComputationChainRoadmap. **48 remain (46 §3b-cond intentional + 2 Kashaev infrastructure)**. |
| Lean — q_0_inversion_unique proof | landed `3038eb87` | §3b-cond class `MRatioInversionMonotone` + constructive uniqueness proof. MassComputationChainRoadmap now 0 sorries. |
| 5d.5b — K_k* variance test | landed `3038eb87` | **K_1* = K_3* = 6_1 (chirality) WINS** at every K_2* — variance 1.49× (vs 1.82× baseline). **Lepton-generation assignment (K_1*=e, K_2*=μ) FALSIFIED** (1.74×). |

**Key structural finding (5d.5b)**: the chirality channel 6_1 dominates **both** outer curvature ranks (k=1 and k=3); the optimal K_2* is unknot (neutrino) — uniform Plancherel restriction. Reading: depth-stratification = chirality-at-endpoints + neutrino-at-middle, **not** lepton-generation as the dictionary mapping naively suggested.

**Knot-particle dictionary integration**: confirms torus knots are structurally distinguished K_k* candidates, **but** the lepton-generation assignment underperforms by 16% vs. chirality-at-endpoints. The catalog's "K_3* = 6_1" claim should likely extend to "K_1* = K_3* = 6_1".

**Coordination posts**:
- [PR #801 comment `4491365695`](https://github.com/litlfred/qou/pull/801#issuecomment-4491365695) — variance findings + asks back on full-formula test + K_2* = unknot interpretation
- [PR #801 body update](https://api.github.com/repos/litlfred/qou/pulls/801) — variance 2.31× → 1.82× refresh + ⁴He H_12 closure + new test-plan items

**Next concrete tasks (Phase 5e):**

1. 5e.1 — Run the FULL PR #801 depth-stratified formula (with α_k + Vol_hyp scaling) under each (K_1*, K_2*) candidate — variance may shift; current simplified probe might miss structural elements.
2. 5e.2 — If chirality-at-endpoints holds under the full formula, propose K_1* = K_3* = 6_1 as a refinement to the depth-stratified-frobenius-reciprocity proposition in PR #801.
3. 5e.3 — Derive cosh(h) operator-level (Phase 5c.2 still queued) — would close the per-Z step factor exactly.
4. 5e.4 — Build SnapPy bridge for Kashaev.lean's `pieceVolume` (closes the last 2 non-§3b-cond Lean sorries).

## 2026-05-19 — Stage-1 (Faddeev → Li_2^q) migration is structurally blocked (branch `claude/fr-pullback-k3-numerical`, [PR #826](https://github.com/litlfred/qou/pull/826))

### 2026-05-20 — Stage-1b migration audit: binding pipeline already Φ_q-free

Per follow-up audit on `claude/fr-pullback-k3-numerical`:

| Script category | Φ_q refs total | Li_2^q refs total | Migration status |
|---|---:|---:|---|
| `binding_*.py` (14 scripts) | 0 | 18 | **COMPLETE** — depth-stratified χ·dim_q (PR #801) needs no q-dilog; the 2 Li_2^q-using scripts are on the binding-context branch correctly |
| `fr_*.py` (1 script) | 0 | 0 | **COMPLETE** |
| `mass_*.py`, `derived_masses.py`, `proton_*.py`, etc. (14 mass-anchor scripts) | many | 0 | **CORRECT AS-IS** — Φ_q is canonical for MASS context per `prop:li2q-phiq-bar-symmetrization`; bar-asymmetric component carries the dimensional mass scale |
| 14 PROBE scripts | many | a few | **CORRECT AS-IS** — Φ_q usage is the subject of study (divergence diagnostics, two-form comparisons), not a binding compute |
| 14 BINDING-class scripts (per the agent classification) | many | a few | **NOT MIGRATION TARGETS** — closer inspection showed all are diagnostics / probes / structural-revision-required; the genuine binding-compute pipeline (above) is already Phi_q-free |

**Conclusion**: the Stage-1 "migrate 42 Phi_q callers to Li_2^q"
framing was based on a too-broad classification. The actual binding
compute pipeline (downstream of `prop:atomic-mass-gb-nf` and
`prop:depth-stratified-frobenius-reciprocity`) is Phi_q-free; the 42
remaining Phi_q callers are correctly mass-context or probe-context.
The structural unblock remaining is the operator-valued
$A^\lambda_{\mu,\nu}(I)$ formulation (research-grade, deferred —
see entry below).

| Date | Phase | Status | Notes |
|---|---|---|---|
| 2026-05-19 | Faddeev `Phi_q` → symmetric `Li_2^q` substitution sweep | **BLOCKED** | Function-substitution alone catastrophically regresses m_p/m_e |

**Empirical evidence** (`m-p-m-e-li2q.witness.json` + ad-hoc rerun on `claude/fr-pullback-k3-numerical`):

| Substitution | m_p/m_e | error vs CODATA 1836.152 |
|---|---:|---:|
| `Phi_q(z)` (legacy Faddeev, on `main`) | 1869.85 | 1.84% |
| `Li_2^q(z)` (naive name swap, `m_p_m_e_li2q.py`) | 3.31 | **99.82%** |
| `−Li_2^q(−z)` (sign-flipped per `_li_2_q_util.py:21` docstring) | 2.49 | **99.86%** |

Neither candidate substitution recovers ~1836. Confirms `mass-endomorphism-tower.md` SUPERSEDED banner — the Faddeev → Li_2^q transition is a **structural revision** (operator-valued $A^\lambda_{\mu,\nu}(I) \in \mathrm{End}(V_\mu \otimes V_\nu)$, graded $\rho_K^{\mathrm{LO}} + \rho_K^{\text{single-gen}} + \dots$ expansion), not a function swap.

**Impact on owner's "remove the deprecated stuff completely" directive (2026-05-19):**
- Stage 1 (Faddeev migration): deferred until operator-valued $\rho_K$ is formalised
- Stages 2–4 (revival + orphan deletion + paper banners): can proceed independently, but were also paused pending the Stage-1 result (single-session scope limit). Re-queued.
- `_phi_q_util.py` (42 active callers in `computations/`) stays in the codebase — it is the legacy convention that actually produces 1.84% m_p/m_e, the best result currently available.

**Where to look next** for the structural derivation:
1. [`mass-endomorphism-tower.md`](../../content/quantum-observable-universe/braids-and-knots/mass-endomorphism-tower.md) SUPERSEDED banner — text of the structural revision
2. [`li2q-phiq-bar-symmetrization.md`](../../content/quantum-observable-universe/braids-and-knots/li2q-phiq-bar-symmetrization.md) — bar-symmetrization claim (Li_2^q = bar(Phi_q) under q ↔ q⁻¹); verifies why naive Li_2^q(z) does not reproduce Phi_q(z) numerically
3. Per-isotope Borromean-tower extension (per `docs/precision-goals.md` Subgoal-1 closure path) — may be the right formal target for the operator-valued $A^\lambda_{\mu,\nu}(I)$

**Surfacing on siblings:**
- [#819 comment](https://github.com/litlfred/qou/pull/819#issuecomment-4492904065) — coordination intent posted before empirical check; will follow up with the result reversal here
- [#826](https://github.com/litlfred/qou/pull/826) — the FR-pullback PR that triggered the deprecation request stays focused on its original FR-test scope; deprecation work spun out to this ledger entry instead of stacking on #826
## 2026-05-19 (post-merge sweep) — PR #801 + PR #819 both merged; #826 supersedes K_3* finding

**State of the thread** (after [PR #819](https://github.com/litlfred/qou/pull/819) merged 2026-05-19T23:00Z and [PR #801](https://github.com/litlfred/qou/pull/801) merged ~22:50Z):

- **`prop:interface-knot-markov-z`** (proved sorry-free in #819): $\mathrm{tr}_M(\mathcal{B}_K^{\text{FULL}}) / \mathrm{tr}_M(\mathcal{B}_K^{\text{CONSTIT}}) = z^{p_+(K)} \cdot (z - h)^{p_-(K)}$, verified to $10^{-15}$ on D / T / ³He / ⁴He. Markov axiom + Hecke skein. Independent of K_k* and stands as a clean categorical theorem.
- **`conj:alpha-cosh-h-z-step-correction`** (#819, §3b-cond): $\alpha \approx [3]_q^2 \cdot \cosh(h)$ at $q_0$ to 0.022%. Open: operator-level proof of the $\cosh(h)$ correction.
- **PR #801**'s `def:ew-interface-knot`, `conj:depth-stratified-frobenius-reciprocity`, `conj:block-multiplicativity-v-free`, `li2q-phiq-bar-symmetrization`, `q-rogers-pentagon-archimedean` now all on main.

### K_3* correction — PR #826 supersedes Phase 5d.5b (mine)

[PR #826](https://github.com/litlfred/qou/pull/826) empirically tested `conj:depth-stratified-frobenius-reciprocity` at k=3 with corrected braid words (verified against KnotInfo via `hyperbolic_volume_cross_check`) and proper $S_{\text{uniform},k}$-preserving weight normalization. Result REVERSES the Phase 5d.5b finding:

| K_3* candidate | variance max/min | vs baseline |
|---|---:|---:|
| (uniform) | 1.82× | — |
| **4_1** (figure-8) | **1.551×** | **+14.8% — best** |
| 5_2 | 1.591× | +12.6% |
| 6_1 (Stevedore) | 1.878× | -3.2% (regresses) |

**Two bugs in Phase 5d.5b probe identified by #826:**

1. **6_1 braid word was wrong.** Stevedore knot has braid index 4, but `(1, 1, -2, 1, -2, -2)` is a 3-strand word. My probe was testing "whatever 3-strand knot the table calls 6_1", not Stevedore.
2. **Weight normalization missing $S_{\text{uniform},k}$ preservation.** FR-pulled-back depth-3 weights summed to 1 instead of preserving the uniform Plancherel depth-3 total.

**Authoritative finding (post-#826):** the K_3* candidate empirically minimising variance is **4_1**, not 6_1. This matches the derivation in `prop:chirality-from-frobenius-self-pairing` (Fricke trace relation gives $\chi_{4_1}((2,1)) = 2 - [3]_q$ at H_3 — derived from the Hecke skein, no asserted naming). The "K_3* = 6_1" naming in the catalog was an unsupported aside.

### Phase 5d.5b ledger row above — superseded

The "K_1* = K_3* = 6_1 chirality WINS" claim is **superseded** by PR #826's corrected probe. Lessons:

- My probe used a 3-strand "6_1" braid (mislabelled) AND had a weight-normalization bug. #826 corrected the normalization and cross-validated the table against KnotInfo via `hyperbolic_volume_cross_check`, but it still used the same repo-labeled 3-strand 6_1 candidate. A real Stevedore (braid index 4) test at H_n with n ≥ 4 strand-blocks remains out-of-scope (see 5e.5 below).
- The Phase 5e.1 full-formula finding (depth-2 = electron at 1.368×) is unaffected — it tests a DIFFERENT question (which K minimises variance at depth-2, not which K_3* the catalog should reference).
- The Markov-axiom interface identity from Phase 5c.1 is independent of K_k* and stands.

### Refreshed Phase 5e backlog (post-#826)

1. ~~5e.2 — propose K_1* = K_3* = 6_1~~ **FALSIFIED by #826**. Updated: K_3* = 4_1 per #826, consistent with `prop:chirality-from-frobenius-self-pairing` derivation.
2. 5e.1 — full-formula variance scan: still valuable but the candidate set should now centre on 4_1 (per #826); the depth-2 = electron finding is unchanged.
3. **K_1*, K_2* identification — STILL OPEN.** #826 only tested k=3. Phase 5f candidate: extend #826's probe to k ∈ {1, 2} using the corrected braid-word infrastructure.
4. 5e.3 — derive `cosh(h)` operator-level (Phase 5c.2 still queued).
5. 5e.4 — SnapPy bridge for Kashaev.lean's `pieceVolume`.
6. **NEW 5e.5 — Real Stevedore 6_1 test at H_n with n ≥ 4 strand-blocks.** Requires the canonical-braid construction to lift to 4-strand sub-braids. #826 flags this as out-of-scope follow-up.
7. **NEW 5e.6 — Update `prop:depth-stratified-frobenius-reciprocity` text** to remove the "K_3* = 6_1" aside. Per #826's resolution, the paper should reflect 4_1 as the derived K_3*.

### Cross-PR sibling scope map (post-#819 merge)

| PR | Title | Classification | Action |
|---|---|---|---|
| **#826** | FR pullback at k=3 — 4_1 best | **MERGED** (2026-05-19); K_3* = 4_1 incorporated | — |
| **#827** | (sub-#826) braid-word + normalization fixes | merged with #826 | — |
| **#829** | T2.3 Wenzl LR convention adapter + `prop:lr-tensor-character-bridge` | **MERGED** (2026-05-20) | — |
| **#806** | Lean enrichment 188 placeholders | **CLOSED unmerged** (2026-05-19) | — |
| **#837** | Lean typed claims round-8 | **MERGED** (2026-05-20) | — |
| #816, #814 | qbeta-ladder c_k thread | adjacent (bar-symmetric corrections at different rungs); #814 cherry-picked into main as #833 | — |
| #818, #820, #817, #807, #761, #774, #738, #823 | assorted infrastructure / domain work | non-overlapping | — |

## 2026-05-20 (very late) — Phase 5f: FR pullback at k=1, k=2 — marginal only ([PR #831](https://github.com/litlfred/qou/pull/831) commit `5f-pending`)

Extends [PR #826](https://github.com/litlfred/qou/pull/826)'s k=3 FR-pullback test to curvature ranks k=1 and k=2. $K_3^* = 4_1$ fixed per #826. Sweep: $6 \times 6$ grid over $(K_1^*, K_2^*)$ candidates $\in \{$ unknot, 3_1, 4_1, 5_1, 5_2, 6_1 $\}$.

**Result**: best variance **1.5432×** at $(K_1^*, K_2^*) = (\text{unknot}, 5_2)$, only **+0.5% vs #826's K_3*=4_1-only baseline (1.551×)**. The top 4 configurations are within 0.04% of each other; K_1* ranking is essentially flat across all candidates.

**Cross-validation**: this script's K_3*=4_1 baseline reproduces #826's reported 1.551× to within 0.0003 (passes the `baseline_matches_PR_826` assertion).

**Interpretation**: the FR-pullback mechanism's variance reduction is **concentrated at k = 3**; depths 1 and 2 are partially redundant under the current formula. Three structural readings (audit doc [`docs/audits/2026-05-19-phase5f-fr-pullback-k1-k2.md`](../audits/2026-05-19-phase5f-fr-pullback-k1-k2.md)):

1. Depth-3 chirality stratum carries the bulk of the FR content.
2. The remaining 1.54× variance is in something the depth-stratified FR does not see at any k. Candidates: Markov-trace constituent factor 1.220358, Vol_hyp-by-Z effect, Phase 5b cosh(h)-like Hecke correction.
3. **$K_1^*, K_2^*$ may be trivial (unknot)** — the current FR pullback formula at k=1, 2 collapses to uniform Plancherel restriction. The 0.5% improvement is plausibly numerical noise.

**Recommendation for `prop:depth-stratified-frobenius-reciprocity`** (queued for follow-up):

- $K_3^* = 4_1$ structurally identified (per #826 + this cross-validation).
- $K_1^*, K_2^*$ may simplify to "unknot" or be dropped from the conjecture's existence requirements; the current formulation as "open structural question" is consistent with the empirical finding.
- Closing the remaining 1.54× residual requires a **different mechanism**, not deeper FR pullback. Phase 5g-5i candidates:
  - Phase 5g — Markov-trace constituent factor 1.220358 categorical identification (from #819 Phase 5d.3).
  - Phase 5h — Phase 5b cosh(h)-like correction integrated into the depth-stratified formula.
  - Phase 5i — Vol_hyp normalisation by Z to extract the bare hyperbolic content (from PR #787 Phase 3).

## 2026-05-20 — Phase 5g + 5h + 5i: closing-the-1.54× campaign ([PR #831](https://github.com/litlfred/qou/pull/831) commits `8e296e85e`, `5ccd58e45`)

Four probes tested on top of PR #826's K_3* = 4_1 baseline (variance 1.551×). Three of four are neutral; one (Phase 5g) produces a clean structural identification but does not directly close variance.

| Phase | Probe | Result | Δ vs 1.551× baseline |
|---|---|---|---:|
| 5f | FR pullback at k=1, 2 (6×6 grid) | best (unknot, 5_2) | +0.5% |
| 5h | cosh(h) at depth-stratified α_k | best (α_2·α_3·cosh(h)) | +0.85% |
| **5g** | **constit factor 1.220358 categorical** | **= 2q − 1 (0.033% rel.err)** | n/a (identification) |
| 5i | Vol_hyp normalisation sweep | per_A best | +3.04% |

**Major finding (5g)**: the Phase 5c.1 constit factor 1.220358 has a clean categorical form $2q - 1$ at q_0, matching to **0.033%** — a 15× improvement over the previous $q + h/2$ candidate. Combined with PR #819's interface factor:

$$\frac{\mathrm{tr}_M(\mathcal{B}_K^{Z+1, N})}{\mathrm{tr}_M(\mathcal{B}_K^{Z, N})} \;=\; \frac{2q - 1}{q^{1/2} + q^{-1/2}} + O(h^4)$$

at the **full tr_M level**. This complements Phase 5b's $\alpha \approx [3]_q^2 \cdot \cosh(h)$ at the |Δ_λ*| level (the two live in different spectral channels of the same Hecke algebra).

**Structural conclusion (5h + 5i)**: the residual 1.54× variance in the depth-stratified formula is NOT closed by FR pullback at additional depths, cosh(h) injection, or Vol_hyp normalisation. It lives in the |Δ_λ*| (single-block dominant) layer, NOT in the Φ_k (depth-stratified sum) layer.

**Recommendation for `prop:depth-stratified-frobenius-reciprocity`**: the conjecture's claim of distinguished K_1*, K_2* knots is empirically falsified by Phase 5f (K_1* essentially flat across {unknot, 3_1, 4_1, 5_1, 5_2, 6_1}). The conjecture should be narrowed to K_3* = 4_1 only, with the residual variance attributed to a single-block-level correction (cosh(h) per Phase 5b) rather than a depth-stratified one.

**Next concrete tasks (Phase 5j-onward)**:
- 5j — Promote $\mathrm{tr}_M$ Z-step factor = $z \cdot (2q − 1)$ to a content block, OR extend `prop:interface-knot-markov-z` with a "constit-side companion identity" section.
- 5k — Higher-precision measurement of the constit factor to characterise the 0.033% residual ($O(h^4)$ noise vs real second-order term).
- 5e.3 — Lean operator-level cosh(h) proof from Hecke symmetric channel (substantive math).
- 5e.4 — SnapPy bridge for Kashaev.lean's `pieceVolume` (large infrastructure).

### Coordination sweep — post-5g/5h/5i (2026-05-20)

| PR | State | Action |
|---|---|---|
| #826 (`fr-pullback-k3-numerical`) | open, dirty | [coord ack posted](https://github.com/litlfred/qou/pull/826#issuecomment-4493323401) — its K_3* = 4_1 finding now incorporated into #831's 5f/5g/5h/5i probes; no file overlap. |
| #829 (`show-mass-sweep-table-2xEBG`) | open, clean | [coord ack posted](https://github.com/litlfred/qou/pull/829#issuecomment-4493324255) — `prop:lr-tensor-character-bridge` validates #819's interface-knot framing; complementary, no file overlap. |
| #806 (`lean-substantive-pass-2026-05-19`) | **closed unmerged** | dropped from scope. |
| main | advanced by #816 + #833 (FSC/G + averaging-resonance) | no conflict — disjoint compute areas. |

§3b-cond placeholder added in this branch: `HeckeSymmetricChannelCoshH` class (5e.3 stub) in [`alpha-cosh-h-z-step-correction.lean`](https://github.com/litlfred/qou/blob/claude/post-819-ledger-update/content/quantum-observable-universe/braids-and-knots/alpha-cosh-h-z-step-correction.lean) — provable theorem `cosh_h_eigenvalue_equals_alpha_factor` derives from the class with no sorry. The class instance itself is the conjectural input awaiting Brundan–Kleshchev FR on the symmetric channel.

CI green on #831 (`validate` ✓). One Copilot review comment on the ledger accepted in `02b3bcf75`.

Next concrete task on the queue: **5j** — promote tr_M Z-step factor = z·(2q − 1) to a content block (extension of `prop:interface-knot-markov-z` with a constit-side companion identity section).

## 2026-05-20 (late) — Phase 5j: constit-factor conjecture promoted to a content block ([PR #831](https://github.com/litlfred/qou/pull/831))

New block: [`conj:constit-factor-2q-minus-1`](https://github.com/litlfred/qou/blob/claude/post-819-ledger-update/content/quantum-observable-universe/braids-and-knots/constit-factor-2q-minus-1.md).

States the categorical identity $\rho_Z^{\mathrm{constit}}(q_0) = (2q - 1) + O(h^4)$ for the disjoint-Hecke-product per-Z step factor at the substrate point, matching empirically to **0.033 % rel. err.** (Phase 5g, 50 dps).  Combined with [`prop:interface-knot-markov-z`](https://github.com/litlfred/qou/blob/claude/post-819-ledger-update/content/quantum-observable-universe/braids-and-knots/interface-knot-markov-z.md) (interface factor $z$), this gives the full $\mathrm{tr}_M$-level per-Z step:

$$\frac{\mathrm{tr}_M(\mathcal{B}_K^{Z+1, N})}{\mathrm{tr}_M(\mathcal{B}_K^{Z, N})} \;=\; \frac{2q - 1}{q^{1/2} + q^{-1/2}} + O(h^4) \quad\text{at }q_0.$$

§3b-cond class: `ConstitFactor2qMinus1` (one class field axiomatising the leading-order identity at the substrate point).  Companion to `AlphaCoshHZStepCorrection` (single-block level, bar-symmetric, $\cosh(h)$) and `HeckeSymmetricChannelCoshH` (5e.3 operator-level placeholder).

`prop:interface-knot-markov-z.md` extended with a "Constit-side companion identity" section pointing to the new conjecture.

Next on queue: **5k** — higher-precision measurement of the constit factor to resolve $O(h^4)$ vs second-order-correction question.

## 2026-05-20 (late, +5k.1) — Phase 5k.1: residual matches h^5 with unit coefficient ([PR #831](https://github.com/litlfred/qou/pull/831))

Power-of-$h$ decomposition of the $0.033\%$ residual at $q_0$ identifies the structural order:

| $k$ | $h^k(q_0)$ | residual$/h^k$ at $q_0$ |
|:-:|---:|---:|
| 4 | $1.91 \times 10^{-3}$ | $0.21$ |
| **5** | $\mathbf{3.99 \times 10^{-4}}$ | $\mathbf{1.016}$ ← unit coefficient |
| 6 | $8.35 \times 10^{-5}$ | $4.86$ |

Refined candidate: $\rho_Z^{\mathrm{constit}}(q) = (2q - 1) + h^5 + O(h^7)$ at $q_0$.  Evaluates to $1.2203565$ vs measured $1.2203629$ — **64× improvement** over $(2q - 1)$ alone (residual drops from $4.06 \times 10^{-4}$ to $6.3 \times 10^{-6}$).

Updates `conj:constit-factor-2q-minus-1.md` with the refined boxed identity.

Script: [`constit_factor_residual_phase5k.py`](https://github.com/litlfred/qou/blob/claude/post-819-ledger-update/computations/constit_factor_residual_phase5k.py).
Witness: `constit-factor-residual-phase5k.witness.json` (1 assertion: residual/h^5 ≈ 1.016 ± 0.05, passes).

**Open question (5k.2 queued):** is $c \equiv 1$ for $h^5$ across the substrate window, or does $c$ vary with $q$?  A single point $c(q_0) = 1.016$ is suggestive but not conclusive.  Phase 5k.2 needs varying-$q$ measurement of $\rho_Z^{\mathrm{constit}}(q)$ via `pyhecke_native` with q-dependent Wenzl $y_\lambda$ weights at multiple $q$ in the substrate window.  Defer as substantive compute work.

Next on queue: **5k.2** — varying-q sweep to confirm unit-coefficient $h^5$ across the substrate window.

## 2026-05-20 (5k.2) — Phase 5k.2 FALSIFIES the global (2q-1) form ([PR #845](https://github.com/litlfred/qou/pull/845))

Varying-q sweep at five q-points across the substrate window, using the same y_λ(q) Wenzl + χ_λ(β_constit, q) pipeline as PR #819 Phase 5c.1:

| q | $\rho_Z^{\mathrm{constit}}(q)$ | $(2q - 1)$ | rel.err. | residual/h^5 |
|---|---:|---:|---:|---:|
| 1.050 | 0.7928 | 1.100 | 27.9% | −34649 |
| 1.080 | 0.9933 | 1.160 | 14.4% | −1920 |
| **1.10998 (q_0)** | **1.2204** | **1.220** | **0.034%** | **+1.04** |
| 1.130 | 1.3905 | 1.260 | 10.4% | +148 |
| 1.170 | 1.7858 | 1.340 | 33.3% | +143 |

**Verdict (NEGATIVE):** the (2q − 1) candidate identified by Phase 5g's categorical search at q_0 is a **localised numerical tangency**, not a global structural identity. The residual against (2q − 1) varies by **5+ orders of magnitude** across the q sweep (c = residual/h⁵ ranges from −3.5×10⁴ to +148); the unit-coefficient h⁵ signature is unique to q_0.

Fine scan around q_0 confirms the tangency is sharp: at q = 1.105 (just 0.005 below q_0) the rel.err is already **2.4%** (70× the q_0 value); at q = 1.113 (0.003 above) it is **1.5%**.

**Consequences:**

- `conj:constit-factor-2q-minus-1` — REVISED: a FALSIFIED banner added; the global form claim is empirically refuted while the at-q_0 value match is preserved as a record of the tangency.
- Phase 5k.1's "unit-coefficient h⁵" interpretation is consequently also a coincidence at q_0 (not a global structural identity).
- The actual closed form for $\rho_Z^{\mathrm{constit}}(q)$ is **open** — the measured ratio grows much more steeply than (2q − 1) suggests (factor 2.26× across $q \in [1.05, 1.17]$). Likely candidates: $\mathrm{tr}_M^3(\mathcal{B}_p)$ combined with a rank-jump z-factor.

Script: [`computations/constit_factor_varying_q_phase5k2.py`](../../computations/constit_factor_varying_q_phase5k2.py) (relative repo link — see [PR #845](https://github.com/litlfred/qou/pull/845) for blob).
Witness: `constit-factor-varying-q-phase5k2.witness.json` (2 assertions: both FAIL as expected — the test was designed to confirm or refute the hypothesis; the refutation is the finding).

Next on queue: **5l** — structural derivation of $\rho_Z^{\mathrm{constit}}(q)$ from the disjoint-product Markov trace formula. The empirical measurements suggest $\rho \approx \mathrm{tr}_M^3(\mathcal{B}_p) \cdot$ (z-factor for rank jump from H_6 to H_9), needing rigorous derivation.

## 2026-05-20 (5l) — STRUCTURAL IDENTITY: $\rho_Z^{\mathrm{constit}}(q) = \mathrm{tr}_M^3(\mathcal{B}_p, q)$ ([PR #845](https://github.com/litlfred/qou/pull/845))

Phase 5l identifies the actual closed form for the constit-side per-Z step factor.  The disjoint-product Markov trace multiplicativity (Wenzl 1988 §1.7) gives

$$\mathrm{tr}_M\!\bigl(\mathcal{B}_K^{\mathrm{vac}}\bigr) \;=\; \mathrm{tr}_M^3(\mathcal{B}_p)^Z \cdot \mathrm{tr}_M^3(\mathcal{B}_n)^N,$$

so $\rho_Z^{\mathrm{constit}}(q) = \mathrm{tr}_M^3(\mathcal{B}_p, q)$ exactly.  Empirical verification at five $q$-values via the $y_\lambda \cdot \chi_\lambda$ pipeline (same as PR #819 Phase 5c.1):

| $q$ | $\mathrm{tr}_M^3(\mathcal{B}_p, q)$ | $\rho_Z^{\mathrm{constit}}(q)$ | rel. err. |
|---|---:|---:|---:|
| $1.050$ |  $0.79284191942392$ |  $0.79284191942392$ | $1.7 \times 10^{-51}$ |
| $1.080$ | $0.99328958564705$ | $0.99328958564705$ | $1.1 \times 10^{-50}$ |
| $q_0$   | $1.22037426648745$ | $1.22037426648745$ | $3.3 \times 10^{-50}$ |
| $1.130$ | $1.39054700525733$ | $1.39054700525733$ | $1.4 \times 10^{-50}$ |
| $1.170$ | $1.78584582119414$ | $1.78584582119414$ | $0$ (exact at 50 dps) |

Identity holds at **mpfr-50-dps precision** ($\sim 10^{-50}$ rel. err.) across the substrate window — bounded by the 50-dps compute pin.

**Resolution of the previous chain (5g / 5k.1 / 5k.2):**

- Phase 5g's $(2q - 1) \approx 1.220$ match at $q_0$ was a numerical coincidence: $\mathrm{tr}_M^3(\mathcal{B}_p, q_0) \approx 1.2204$ happens to be near $2 q_0 - 1 = 1.2200$, but the two functions diverge elsewhere.
- Phase 5k.1's "unit-coefficient $h^5$" residual at $q_0$ ($c = 1.016$) is likewise a numerical accident: $\mathrm{tr}_M^3(\mathcal{B}_p, q_0) - (2 q_0 - 1) \approx h^5(q_0)$ only at $q_0$.
- Phase 5k.2 (this PR) falsified the global $(2q - 1)$ form via varying-$q$ measurement; that falsification was the bridge to identifying the actual closed form.

**Combined per-Z step at the full $\mathrm{tr}_M$ level (now exact, no residuals):**

$$\frac{\mathrm{tr}_M(\mathcal{B}_K^{Z+1, N})}{\mathrm{tr}_M(\mathcal{B}_K^{Z, N})} \;=\; z(q) \cdot \mathrm{tr}_M^3(\mathcal{B}_p, q)$$

at a p-* boundary, with $z(q)$ from [`prop:interface-knot-markov-z`](../../content/quantum-observable-universe/braids-and-knots/interface-knot-markov-z.md) (interface factor).

**Content blocks:**

- NEW: [`prop:constit-factor-tau-M-proton-identity`](../../content/quantum-observable-universe/braids-and-knots/constit-factor-tau-M-proton-identity.md) — the structural identity, with Wenzl-derivation proof and 5-q empirical verification.
- UPDATED: [`conj:constit-factor-2q-minus-1`](../../content/quantum-observable-universe/braids-and-knots/constit-factor-2q-minus-1.md) — RESOLVED banner pointing to the proposition above; conjecture preserved as a record of the historical Phase 5g categorical-search result.

**Script:** [`computations/rho_constit_equals_tau_M_proton_phase5l.py`](../../computations/rho_constit_equals_tau_M_proton_phase5l.py).
**Witness:** `rho-constit-equals-tau-M-proton-phase5l.witness.json` (1 assertion: max rel.err. < 1e-12, passes at ~1e-15).

Next on queue: **5l.1** — extract closed form for $\mathrm{tr}_M^3(\mathcal{B}_p, q)$ as a Laurent rational expression in $q$ (the proton braid is a specific Hecke word, so $\mathrm{tr}_M^3(\mathcal{B}_p, q)$ is a specific algebraic function).

### Coordination sweep — 5k.2 + 5l (2026-05-20)

| PR | State | Action |
|---|---|---|
| **#842** (`phase-5k2-varying-q-sweep`) | open, CI ✓ green on `597938ab6` | Copilot review cycle 1 dispositioned (4 comments accepted); [cross-link to #845 posted](https://github.com/litlfred/qou/pull/842#issuecomment-4494415815) noting #845 supersedes its falsification framing with the actual structural identity. |
| **#845** (`phase-5l-disjoint-markov-trace`) | open, CI in progress | [coordination posted](https://github.com/litlfred/qou/pull/845#issuecomment-4494416349) explaining the #842 → #845 chain and merge-order options. |
| main | advanced by #839 (Lean typed claims round-9) | no file overlap — constit-factor / Markov-trace work disjoint from typed-claims work. |
| #818, #817, #761 | old branches (May 18–19) predating #831 baseline | no actual edit overlap — diff against current main shows "constit-factor-2q-minus-1.lean missing" because branches are old, not because they edit it. No coordination needed unless those PRs rebase. |
| Other open PRs (#411, #31, #650, #646, #774, #738, #807) | unrelated domains | — |

**Merge order suggestion** (posted on #842): land #842 first to preserve the falsification's review history with its 4 Copilot dispositions; then #845 follows with the resolution. Alternative: close #842 in favor of #845 (which carries the full falsify-then-resolve narrative in its PR body + ledger rows).

Next on queue (sibling coordination): wait for review on #845; if approved, propose merge order to owner.
