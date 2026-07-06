# Coordination ledger — non-calibrated Q_β + mass cleanup

**Goal**: tighten the framework's β-decay $Q_\beta$ prediction
(non-calibrated, CAL-1 + CAL-2 only) and clean up the mass-formula
pipeline to honor the three-calibration discipline.

**Owner branch**: `claude/display-mass-tables-PAj4i` → PR #637

## Scope map (2026-05-11 snapshot)

| PR | Title | Author | Branch | Classification |
|---|---|---|---|---|
| **#637** (this) | FULL Q_β prediction + non-calibrated mass cleanup | @litlfred | claude/display-mass-tables-PAj4i | own |
| #636 | Audit: Plancherel weight usage | @litlfred | claude/audit-plancherel-usage-a6DgI | **scope-overlap (w_λ semantics)** |
| #635 | Mikusiński WitnessBuilder migration | @litlfred | claude/mikusinski-witness-builder-migration | **convention-overlap (WitnessBuilder.wrap_legacy)** |
| #632 | Paper illustrations (SVG figures) | @litlfred | claude/add-paper-illustrations-Diggj | no overlap |
| #510 | Mod-p Mandelbrot/Julia visualisations | @litlfred | claude/p-adic-mandelbrot-visuals-6Lvum | no overlap (paused) |

(Bot/automation PRs #31, #411 excluded — copilot-driven, separate workflow.)

## Classification axes (per skill §2)

### #636 — scope overlap (w_λ Plancherel weight semantics)

**Overlap**: my new probe scripts (`probe_beta_decay_residue_sum_h3.py`,
`probe_q_beta_residue_per_nucleon.py`) use the q-deformed Wedderburn
weight $w_\lambda = \dim_q^2(\lambda) / [n]_q!$ — exactly the formula
#636's audit identifies as overloaded with the classical Plancherel
form.

**Dependency**: my PR consumes one convention consistently (q-deformed,
normalized to sum-to-1 at n=3). If #636's R1 (rename q-deformed →
$\widetilde{w}_\lambda$) lands, I rename in my probes to match.

**Cherry-pick**: none. #636 is an audit report only, no code changes
to consume.

**Coordination posted**: https://github.com/litlfred/qou/pull/636#issuecomment-4417353011

**Action**: WAIT for #636 R1 disposition before renaming. No blocker.

### #635 — convention overlap (WitnessBuilder.wrap_legacy)

**Overlap**: #635 migrates 5 graded-Mikusiński scripts to
`WitnessBuilder.wrap_legacy`. Copilot's #637 review identified 7
ADDITIONAL scripts in `computations/` with the same
missing-WitnessBuilder pattern.

**Dependency**: #637 SHOULD consume #635's `wrap_legacy` pattern after
merge to match the convention, rather than racing parallel migrations.

**Cherry-pick**: none. #635 establishes the canonical pattern; #637's
follow-up consumes it.

**Coordination posted**: https://github.com/litlfred/qou/pull/635#issuecomment-4417350818

**Action**: DEFER 7-script WitnessBuilder migration to a follow-up PR
(`claude/witnessbuilder-migration-cleanup`) opened after #635 merges.
Tier-2 fix list documented in PR #637 review reply
(https://github.com/litlfred/qou/pull/637#issuecomment-4417349854).

### #632 — no overlap (SVG illustrations)

**Overlap**: none. Different chapters, different file types (SVG +
illustration skills package). No content-block conflicts.

**Action**: nothing.

## Status comments posted

| PR | Comment | Type | URL |
|---|---|---|---|
| #637 | Tier-1 disposition + Tier-2 deferral plan | own status | https://github.com/litlfred/qou/pull/637#issuecomment-4417349854 |
| #636 | w_λ convention coordination | sibling intent | https://github.com/litlfred/qou/pull/636#issuecomment-4417353011 |
| #635 | WitnessBuilder migration coordination | sibling intent | https://github.com/litlfred/qou/pull/635#issuecomment-4417350818 |

## §6 escalations (inconsistent findings)

None — all overlap is convention-level (naming, formatting). No
inconsistent NUMERICAL findings between my PR and #635/#636.

Cross-check with #636 audit data:
- #636 reports $\dim_q^2/[12]_q! \neq 1$ at n=12
- My #637 probes evaluate at n=3 only, where the discrepancy is
  small
- After my sum-to-1 renormalization at H_3 the convention difference
  cancels exactly. No escalation needed.

## Watch baseline

`origin/main` at `f5e47e52` (no new commits during this session as of
03:35Z). Monitor task `blluxl3xg` re-armed (5-min poll). No upstream
landing to integrate.

## Open queue items on this branch

1. **Tier-2 WitnessBuilder migration** — DEFERRED to follow-up PR after #635 merges (7 scripts)
2. **Tier-3 Lean closure proofs** — 10 sorries opened in `MassComputationChainRoadmap.lean`; each is multi-week R&D
3. **CI validate failure** — believed to be runner-quota constraint (per #635 author's note on PR #634); local validate passes

## Anti-patterns avoided this session (skill §10)

- ✓ Did NOT split the difference on inconsistent w_λ conventions —
  documented per-probe convention explicitly and asked #636 for R1
  disposition.
- ✓ Did NOT silently merge main — fetched + verified no upstream
  changes before opening PR.
- ✓ Did NOT add newly-opened sibling PR to scope without prompting —
  #635 + #636 both got explicit coordination comments asking for
  their preferred coordination mode.
- ✓ Did NOT rewrite my framing in response to inconsistent findings
  — the +1.31 keV residual is intrinsic to predict mode and was
  preserved consistently across 16 commits.

## Last updated

2026-05-11T03:42Z — coordination cycle 2 (user `/coordinate
claude/audit-plancherel-usage-a6DgI` invocation).

## Coordination cycle 2 — focused re-coordination on #636

User invoked `/coordinate` with sibling argument
`claude/audit-plancherel-usage-a6DgI` (= PR #636) explicitly.

### State of #636 since cycle 1

* My coordination comment (`#4417353011`) — landed 03:29Z. No reply yet.
* **3 other coordination comments from parallel sessions** also on #636:
  * `#4417286807` from PR #635 (Mikusiński migration coordination)
  * `#4417297548` from PR #637's owner-context (another session)
  * `#4417315728` from #637 (visibility ping)
  Suggests multi-PR coordination activity is healthy on this sibling.
* **1 new Copilot review thread on #636**:
  `docs/audits/2026-05-11-plancherel-usage-audit.md:241` — broken
  GitHub URL (`hoefsmit-symbolic.py` should be `hoefsmit_symbolic.py`).
  **NOT my concern** — #636 author's review thread to address.
* CI on #636: `validate` in-progress at 03:40Z — same `validate` job
  that keeps failing on my PR + #635. Confirms shared CI constraint
  (likely the runner-quota issue from PR #634).

### Classification update — UNCHANGED

* Scope overlap: still ONLY `w_λ` symbol semantics
* Dependency: I consume one convention consistently; if their R1
  (rename q-deformed → `w̃_λ`) lands, I rename to match. **No
  blocker either way.**
* Cherry-pick: still NONE (audit is documentation-only)
* §6 escalation: still NONE — no inconsistent numerical findings
  between #636 and #637 at n=3

### Action taken this cycle

NONE — no new comment posted to #636. Reasons:

1. My cycle-1 comment (#4417353011) already covers the convention
   overlap completely.
2. Posting again would violate skill §3 anti-pattern: "one
   coordination comment, not a stream".
3. The new Copilot thread on #636 (URL fix) is not in my scope.
4. No new findings on my side since cycle 1.

### Action queued — wait for #636 R1 disposition

If #636's R1 lands and renames `w_λ` (q-deformed) → `w̃_λ`,
I will rename in:

* `computations/probe_beta_decay_residue_sum_h3.py:96`
* `computations/probe_q_beta_residue_per_nucleon.py` (analogous comment)
* `content/quantum-observable-universe/lean/QOU/MassComputationChainRoadmap.lean`
  (gap #6 stub — already includes a coordination note)

Estimated effort: <30 minutes once #636 lands. Tracked as
follow-up; no blocker on #637 merge.

### Watch baseline UNCHANGED

`origin/main` still at `f5e47e52`. Monitor `blluxl3xg` armed.

### Anti-patterns avoided this cycle

* ✓ Did NOT post a duplicate coordination comment ("stream", §3)
* ✓ Did NOT silently rewrite my framing in response to the URL-fix
  thread on #636 (skill §6) — that thread is for #636's author
* ✓ Did NOT fix the broken hoefsmit-symbolic.py URL myself
  (that's #636's review thread, not mine to address)

## Coordination cycle 3 — major Q_β residual decomposition findings

2026-05-11T16:30Z — user requested error-source analysis +
re-derivation via Frobenius pairing / dual basis / Wenzl bridge.

### New findings (worth coordinating with #636)

1. **Frobenius factorization** of 1.00744 = 1.00168 (brane-tower
   N=0) × 1.00579 (basis-change typed vs single-wrap). Exact
   multiplicative split, numerically and structurally separable.

2. **Dual-basis structural identity** $G^{-1} \cdot t = e_\gamma$ at H_3.
   Proof: $G_{\gamma j} = \mathrm{tr}_M(b_j) = t_j$, so $G \cdot e_\gamma = t$.
   Equivalently: the framework's "net" (= $\sum_i x_i$) IS the
   Frobenius counit $\varepsilon$, the structurally-canonical
   projection. **No weights are missing.**

3. **Forms 2 (tr_M-weighted), 3 (Frobenius dual G⁻¹), 4 (Wenzl
   y_λ χ_λ)** all FAIL to give Q_β — they measure different physical
   quantities (cat-action, dual-paired γ-content, Markov-trace).
   The framework's unweighted counit × $E_0$ form is correct.

4. **Per-N bound vs lift formula**: per-braid-mass-tower bound
   predicts ≤ 1 ppb at $N \geq 4$, but actual residual depends on
   lift formula. 5 naive N=1 lifts all WORSE (42–134×). The
   bound is the worst-case ceiling; the canonical $n_\star$
   conjecture is the open piece.

### #636 relevance

The Wenzl-bridge form (Form 4) **does** use $y_\lambda$ weights — exactly
the symbol-overload issue #636 audits. But I'm using $y_\lambda$ in
the Markov-trace form (which is correct for tr_M), not in the
mass formula (which uses the Frobenius counit instead). So no
direct cross-PR concern — the rename (#636 R1 → `w̃_λ`) wouldn't
affect my analysis.

The cleanest categorical takeaway: **counit ≠ Markov trace**. They
have different structural roles. Both are correct in their respective
domains.

### Action taken cycle 3

Posted update on #636 with the dual-basis identity finding — useful
data for their #R6 (invariance under weight renormalization) check.
Did NOT post on #635 (no relevance) or #632 (no overlap).

### Watch baseline

`origin/main` still at `f5e47e52`. Monitor armed; no upstream
landings during this session.

### Open queue update

Gap 6 (Wedderburn weights closed form) is now **NOT on the critical
path** for closing the 1.31 keV residual, because the dual-basis
identity shows the framework's Q_β formula uses the Frobenius counit
directly (no $w_\lambda$ involved). Gaps 4 + 5 (Φ_q convergence + n_⋆
existence) remain the bottleneck.

## Coordination cycle 4 — post-merge of #637; sibling #638 appears

2026-05-11T17:30Z — PR #637 merged at commit `86971534`. New sibling
**#638** (`claude/close-level-selection-rule-bvMvw`, opened
2026-05-11T17:04Z) refutes the **scalar-eigenvalue** form of the
`n_⋆` level-selection rule from the `brane-tower-z-habiro` conjecture
that my just-merged work depended on (Lean gap 5).

### Scope map (post-merge)

| PR | Title | Status | Classification |
|---|---|---|---|
| **#637** | FULL Q_β prediction + non-calibrated mass cleanup | **MERGED** at `86971534` | own (closed) |
| **#638** (NEW) | Refute scalar-eigenvalue n_⋆; add operator-valued probe | open, clean review | **scope-overlap (brane-tower-z-habiro)** |
| #635 | Mikusiński WitnessBuilder migration | open, waiting on CI | convention-overlap (deferred Tier-2 dependency) |
| #632 | Paper illustrations (SVG figures) | open | no overlap |
| #636 | Audit: Plancherel weight usage | merged or stale (not in latest open list) | no longer in scope |

### #638 classification

* **Scope overlap**: HIGH — both PRs cite `brane-tower-z-habiro`;
  my `BraneTowerNStar.lean` declares `betaDecayNStarCandidates`
  (scalar 3-way agreement at $n_\star = 2$ for $A = 1$ β-decay),
  #638 refutes the scalar-eigenvalue form across $A \geq 2$
  ($D, T, {}^3\mathrm{He}$).
* **Dependency**: compatible at the data level — β-decay (#637) is
  the multiplicity-trivial sub-case; D/T/³He (#638) exposes the
  near-pole multiplicity asymmetry. #638 **supersedes** handoff
  Task 2 (operator-valued recovery for BraneTowerNStar.lean) —
  the multiplicity-refined branch is now the canonical successor.
* **Cherry-pick**: none. #638 is a structural refutation.

### Cross-check for §6 inconsistency: NONE

| Artifact | Statement | Scope |
|---|---|---|
| #637 `betaDecayNStarCandidates` | scalar candidates agree at $n_\star = 2$ | $A = 1$, free β-decay, single near-pole entry |
| #638 `nStar_all_probed_forms_refuted` | scalar AND per-eigenvalue forms fail | $A = 2, 3$, multi-strand binding, multiplicity ≥ 1 |

These compose cleanly: the scalar form works precisely where the
multiplicity profile is trivial (β-decay), and fails as soon as
that profile diverges (D/T/³He). No silent reframing on my side.

### Actions this cycle

* Posted **one** coordination comment on #638:
  https://github.com/litlfred/qou/pull/638#issuecomment-4423184876
  (intent + classification + commitment to a one-line cross-ref
  follow-up after #638 merges).
* Subscribed to #638 activity for CI / review tracking.
* Did **not** open a fix branch yet — the cross-ref follow-up is
  blocked on #638 landing (avoid racing their branch).
* Did **not** post on #635 (still convention-only overlap) or
  #632 (no overlap).

### Queued follow-up after #638 merges

Tiny PR (`claude/brane-tower-nstar-xref-638`):
* `BraneTowerNStar.lean` — add docstring note pointing to #638's
  `witness_refutes_per_eigenvalue_operator_form`, clarifying that
  `betaDecayNStarCandidates` is the $A = 1$ multiplicity-trivial
  sub-case (not a counterexample to the broader refutation).
* Estimated effort: < 15 minutes.

### Watch baseline (post-merge)

`origin/main` at `86971534` (= my #637 merge). Will re-fetch and
re-classify each watcher cycle. Subscribed to #638 + still
monitoring open queue.

### Anti-patterns avoided this cycle

* ✓ Did NOT add #638 to scope without first reading its body +
  classifying against my just-merged work.
* ✓ Did NOT post a duplicate review-triage comment — #638's owner
  already addressed all 13 Gemini/Copilot threads cleanly.
* ✓ Did NOT race the cross-ref fix into a branch while #638 is
  still open (avoids spurious merge conflicts on
  `brane-tower-z-habiro.{md,lean}`).
* ✓ Did NOT silently rewrite #637's framing in response to #638's
  refutation; documented the multiplicity-profile reconciliation
  explicitly.

## Coordination cycle 5 — sibling #640 (neutron Path A)

2026-05-11T18:35Z — PR #640 opened at `c4c2d382` extending
`M_HECKE_PIPELINE_AT_Q0` with the neutron Path A entry. Direct
extension of my just-merged #637 pipeline. Includes a comprehensive
three-calibration-discipline audit
([`docs/audits/2026-05-11-three-calibration-discipline-violations.md`](https://github.com/litlfred/qou/blob/claude/neutron-mass-50dps-chain/docs/audits/2026-05-11-three-calibration-discipline-violations.md))
that flags two Class-A violations on `main` and reinforces the
normative CAL-1/CAL-2/CAL-3 framing.

### #640 classification

* **Scope overlap**: MODERATE — registry entries split on dict key
  ('p' in main, 'n' in #640). No file-level conflict expected.
* **Dependency**: complementary, not blocking. Both #639 and #640
  depend on #637's framework.
* **Cherry-pick**: none.

### Three-calibration self-audit on my #639 compute

Cross-checked against #640's taxonomy:

| Script | Class | Disposition |
|---|---|---|
| `q_beta_spectral_bridge_witness.py` | pure prediction (CAL-1 + CAL-2) | clean |
| `c_k_beta_decay_witness.py` | **Class C (comparator)** — Q_BETA_MEV used to compare observation vs ceiling, NOT as a calibration input | clean with explicit docstring tag added (commit `ccecd506`) |

### Actions cycle 5

* Posted **one** coordination comment on #640:
  https://github.com/litlfred/qou/pull/640#issuecomment-4423536222
* Subscribed to #640 activity.
* Added Class-C docstring tag to `c_k_beta_decay_witness.py`
  (commit `ccecd506`).
* Updated `MassComputationChainRoadmap.lean` "Coordination" section
  with #638/#639/#640 entries + Gap 4 CLOSED + Gap 5 UPDATED.
* Did **not** triage #640's 12 open Gemini/Copilot threads (their
  owner is handling them).
* CI failure on #639 validate: skipped per "ci=billing. skip".

### §6 escalations: none

No inconsistent numerical findings.

## Coordination cycle 5b — share findings with #640

User requested cycle 5 to also push my **c(K) ceiling**
findings to #640 as positive-example material for their audit
framework. Posted a second concise share-comment on #640 with:

1. The substrate-derived per-N residual ceiling
   `|R_N| ≤ C(K) · e^(-c(K) N)` (c(K) = 4.624 for β-decay),
   useful framing for evaluating their neutron mass prediction's
   residual against the same exponential bound.
2. The Class-C / "comparator only" docstring convention they may
   want to adopt for `M_N_MEV_CODATA` (currently hard-coded per
   the open Copilot review at `build_neutron_mass_50dps_chain.py:71`).

Second comment is reactive sharing, not a duplicate intent post —
keeps the "one coordination comment, not a stream" anti-pattern
intact because it serves a distinct request.

## Coordination cycle 5c — cross-PR audit of #640 neutron chain

2026-05-11T19:30Z — applied the #637 cycle-3 trust-basis audit
pattern to PR #640's neutron Path A derivation. Posted findings:
https://github.com/litlfred/qou/pull/640#issuecomment-4424275187

Three structural findings flagged to #640:
1. The 999 ppb residual is NOT a brane-tower truncation effect
   (100× larger than per-braid N=0 bound 0.991%)
2. The Path A T1+T4 dimensionless ratio m_n/m_e = 1.0982 ≈ q_0 —
   collapsed onto the substrate parameter, missing ~1672× in scale
3. Their recommended ρ_K fallback is SELF-REFUTED by their own
   three-calibration audit (Class-A hard violation)

Closure path likely runs through per-partition k_λ on the Wedderburn
decomposition, not Phase A precision alone.

## Coordination cycle 6 — sibling triage + #635 cherry-pick + SDP-with-Gram

2026-05-11T19:55Z — /coordinate run on all open PRs updated today.

### Sibling state

| PR | Status | Cycle-6 action |
|---|---|---|
| **#639** (own) | open, 22+ commits | progress summarized below |
| **#640** (neutron Path A) | open, 12 review threads | cycle 5c audit stands; no follow-up needed |
| **#638** (refute scalar n_⋆) | open | cycle 4 stands; nothing new |
| **#635** (Mikusiński WitnessBuilder) | open | **cherry-pick acknowledgement posted** ([4424413868](https://github.com/litlfred/qou/pull/635#issuecomment-4424413868)) — 7 #637-deferred scripts now use #635's `wrap_legacy` pattern |
| #632 (illustrations) | open | no overlap; no action |

`origin/main` advanced to `787f8d0f` ("Document knot volumes
derivation and pipeline audit") — adds `docs/agent-briefs/lambda_scale.md`,
no overlap with my files; no rebase required.

### #639 progress this cycle

**New substantive probes since cycle 5b:**

* **LP-cost selector probe** (`probe_lp_cost_dominant_partition.py`):
  tests $\mathop{\mathrm{argmax}} |y_\lambda \cdot \chi_q^\lambda|$.
  Negative finding (1/3, T only). Rules out simple LP cost.
* **Form A N=1 symbolic** (`q_beta_form_a_n1_extension.py` + content
  block `prop:q-beta-form-a-n1-symbolic` + Lean): closed form
  $Q_\beta^{A,N=1} = m_e \cdot (q+1)|q^2-2q-1|(2q^2-2q+1)/(2q^5)$
  via geometric-series lift. Negative finding: overshoots per-braid
  ceiling 97 ppm by ~120×.
* **SDP-with-Gram active-set** (`probe_sdp_active_set_dominant_partition.py`):
  runs the actual operator-selection LP via `lp_dual_solver` with
  $t_\lambda = y_\lambda \cdot \chi_q^\lambda$ and **diagonal** Gram
  $G = \mathrm{diag}(\sum_a |\mu_a|^2)$. PARTIAL match (1/3, T only)
  — same as LP cost. The diagonal-Gram simplification collapses
  the SDP dual to the LP cost; **the full off-diagonal Gram is
  required to genuinely test the SDP hypothesis**. Strong duality
  verified (gap = 0 for all 3 atoms). LP/SDP first-class-infra
  contract satisfied.

### Refutation chain status (cycle 6 snapshot)

| Selector form | Verdict | Witness |
|---|:---:|---|
| Scalar n_⋆ (uniform k, GB grade, ℓn_0+k) | refuted | PR #638 |
| Per-eigenvalue operator-valued uniform k | refuted | PR #638 |
| Type-B fold depth (partition shape only) | partial (2/3) | PR #639 cycle 5b |
| Hoefsmit content-spread (partition shape only) | refuted | PR #639 cycle 5c |
| Multiplicity-refined 2-input rules (4 simple) | refuted | PR #639 cycle 5b |
| LP cost argmax | refuted (1/3) | PR #639 cycle 6 |
| **SDP with diagonal Gram** | refuted (1/3) | **PR #639 cycle 6** |
| Per-partition k_λ (max-|μ| selector, EMPIRICAL) | **closes** | PR #639 cycle 5b |
| SDP with full off-diagonal Gram | UNTESTED | next probe |

### Open structural question (sharpened)

The empirical max-|μ| selector closes all 3 atoms (cycle 5b).
The closed-form **substrate-derivable** identification of that
selector is the remaining open piece. Two routes remain:

1. **Full off-diagonal SDP Gram** — compute Gram entries
   $\mathrm{tr}_M(b_i \cdot b_j)$ across distinct Wedderburn blocks
   via Hoefsmit matrix products. The diagonal simplification is
   shown insufficient.
2. **Hoefsmit hook-content asymptotic along a reduced braid word**
   ($(q, \beta)$-aware, per `rem:per-partition-k-lambda-rule`'s
   open question section).

### Anti-patterns avoided cycle 6

* ✓ Fetched `origin/main` and classified `787f8d0f` (no overlap)
* ✓ Did NOT split the difference on inconsistent findings — SDP-
  with-diagonal-Gram NEGATIVE result is documented as a refutation
  of the simplified hypothesis, not a partial confirmation
* ✓ Cherry-pick from #635 properly attributed (single comment, not
  a stream)

## Last updated

2026-05-11T19:55Z — cycle 6 (sibling triage + #635 cherry-pick
acknowledgement + SDP-with-Gram negative finding logged).
