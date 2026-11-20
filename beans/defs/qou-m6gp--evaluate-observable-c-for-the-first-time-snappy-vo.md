---
# qou-m6gp
title: 'Evaluate observable C for the first time: SnapPy volume of the DERIVED braid closures (binding_volume_difference_probe leg C never ran)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-07T18:06:40Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-v2om
---

computations/probes/binding_volume_difference_probe.py reports a 'triple refutation' but leg C (SnapPy hyperbolic volume of the derived braid closures, free vs interface-inclusive) has NEVER executed: _snappy_braid_vols returns (None, None, False) on ImportError, indistinguishable from a genuine non-hyperbolic result, and snappy is absent from every agent container measured. The committed witness therefore records C as refuted on the strength of an import failure. Task: install SnapPy, run leg C, report what it actually says; fix the helper so ImportError is a distinct verdict (unevaluated), never a refutation. Misattributed to qou-26f2 by a sibling; qou-17mq records the reason it does not help the EM-linking front. Scope any negative (a)/(b).



## 2026-09-07 — leg C evaluated for the first time (branch claude/observable-c-snappy-first-run-2026-09-07)

**Premise correction.** SnapPy 3.3.2 was ALREADY present in this container (`pip install snappy` exit 0, all requirements satisfied); the "absent from every agent container" premise does not hold here. Controls: fig-8 2.029883212819, 8_11 8.286316817807, L6a4 7.327724753418, Hopf degenerate/0 — all match `binding-link-volumes.witness.json`. `M.volume(verified=True)` needs Sage (absent); volumes are ManifoldHP quad-double, serialized at 28 digits, UNVERIFIED.

**The old leg was measuring the wrong object.** `_snappy_braid_vols` mapped every Hecke letter to a positive generator (`k+1`), discarding the σ⁻¹ signs and the 2A+1 averaged letters. That all-positive projection is not one of the word's branches; its closure is degenerate (Vol ~1e-4…5e-3). Kept in the witness as `positive_projection_legacy` only.

**Sign-faithful result, live (alternating-core, qou-hu1f) word.** Every per-nucleon 3-strand branch closure is a HYPERBOLIC 2-component link: proton (+,+) L9n10 9.9665118837, (+,−) L11a252 16.1911429640, (−,+) L7a6 4.7494999819, (−,−) L9a21 11.9428724495; neutron (+,+) L11a252, (+,−)/(−,+) L9a21, (−,−) L11n202 8.1957030826 — all "all tetrahedra positively oriented", census-identified. So the 2026-08-25 audit's "monotone ⇒ #T(2,k) ⇒ Vol = 0" (and the same sentence in the `atom_braid_word_3A` docstring) is STALE for the live word — it was true of the grouped word; monotonicity broke on 2026-09-05.

**What survives is the structural half, and it kills leg C harder than "non-hyperbolic" did.** Every inter-nucleon interface is a single letter, so closure(β₁σ_k^±β₂) = closure(β₁) # closure(β₂): `deconnect_sum` on all 800 atom branches (32/128/128/512) gives exactly A summands, 2048/2048 (⁴He) pieces matched to the nucleon table; 0/800 whole closures admit a geometric solution (non-prime). Simplicial volume = sum of hyperbolic JSJ pieces (Gromov/Soma), so Vol(atom) − Vol(free) = 0 on EVERY branch (max over 800: 2e-63, summation rounding at 70 dps). B_C = ρ·0 = 0 for all three derived ρ (m_e, E_0, m_e·8G): residual −100.00 % on ²H, ³H, ³He, ⁴He. Weight-averaged branch volumes: 22.7807 / 34.8488 / 33.4932 / 45.5613.

**Scope: (b) on the DIFFERENCE only**, invariants: single-letter-interface closure identity + JSJ additivity of simplicial volume. NOT excluded: an absolute-volume reading (pieces are hyperbolic, 4.75–16.19 each), a non-additive functional of the pieces, a multi-letter interface. Legs A and B untouched.

**Corpus-grep before writing "refuted":** docs/audits/2026-08-25-atom-word-closures-are-not-hyperbolic.md (grouped word; addendum appended), 2026-07-04-he4-link-volume-braid-closure-refuted.md (different word builder, pre-alternating), computations/atom_word_braid_letter_census_probe.py (branch counts, consistent). 591 files mention snappy across computations/ docs/audits/ .beans/; none evaluated the live word's branch volumes.

**Files:** computations/probes/binding_volume_difference_probe.py (helper replaced by `_snappy_leg_c`, ImportError ⇒ `status: unevaluated`; leg A errors now mpf/fmt, drains 12 raw floats from the ratchet baseline), its witness (regenerated, env mpmath 1.4.1 + clarabel 0.11.1 after installing them), mass_at_3A_proper.py docstring correction, audit addendum. Runtime 1m54s (⁴He 512 branches dominates).
**ROAST 2026-09-07 (qou-pbwj) — verdict: KILL as a research front; keep a ≤10-line chore.** Already answered at scope (b): `docs/audits/2026-08-25-atom-word-closures-are-not-hyperbolic.md` installed SnapPy 3.3.2 and proved every branch closure of `atom_braid_word_3A` is a connected sum of (2,k) torus links, Vol = 0, verified 32/32 against `deconnect_sum` for all A ≤ 24 (invariants: one-run-per-generator normal form; connected sums non-prime; (2,k) torus links Seifert-fibred); `2026-07-04-he4-link-volume-braid-closure-refuted.md` already found the p/n/³H/³He/⁴He closures non-hyperbolic with the wrong component counts. Worse, the code this bean wants to run measures the wrong object: `binding_volume_difference_probe.py:93-111` builds `braid = [k + 1 for (_c, _d, k) in w]`, discarding every crossing sign and averaging weight — an all-positive braid that is none of the 2^(2A+1) branches. Fit exposure: latent selection against the target (choosing a branch/sign resolution to get Vol ≠ 0). L2 relevance: none. Residual value: make ImportError report 'unevaluated' rather than 'refuted' and cross-reference the 08-25 audit from the probe description. Full frame: docs/audits/2026-09-07-takeover-fronts-roast.md §Front 1.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-07 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress Update (Round 90 — lane-cf11)
- Formalized in `folio/quantum-observable-universe/lean/QOU/QBeta/BipartitionTransseriesAndCubicDimensionKernelBrick.lean` with 80-dps probe `computations/probes/bipartition_transseries_and_cubic_dimension_kernel_brick_probe.py` and witness `computations/probes/bipartition-transseries-and-cubic-dimension-kernel-brick.witness.json`.
- PR: https://github.com/litlfred/qou/pull/8339 (`feat/qou-b9cj-m0bv-m6gp-mbz4-mdbh-mssy`, HEAD `8369032c8c6c736ecfb79467000a84fa918a7d04`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8339, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
