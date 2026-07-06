> **DEPRECATED on 2026-05-24.** Superseded by [`2026-05-18-1ppb-workplan-v7-100x-experimental.md`](../2026-05-18-1ppb-workplan-v7-100x-experimental.md) (the latest in the 1ppb-workplan chain). Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) §"5-tranche recommendation" T4 for the deprecation rationale.

# 1ppb workplan v1 — refined (post-PR #671 synthesis)

**Date:** 2026-05-17
**Authors:** Claude (this session, post-PR #671)
**Supersedes:** [`2026-05-12-1ppb-implementation-plan.md`](2026-05-12-1ppb-implementation-plan.md) (workplan v0)
**Status:** Awaiting PR #671 merge; will be implemented on a new PR
branched from `main` after that merge.

## Synthesis sources

| Source | Contribution |
|---|---|
| Workplan v0 ([2026-05-12-1ppb-implementation-plan.md](2026-05-12-1ppb-implementation-plan.md)) | Phase 1-4 task structure; M0→M5 milestone ladder |
| **PR #671** (this branch) | Δ_coupling substrate-derivation, F_n closed-form for tr_M(σ_1²), V_(2,2,2) refutation, dual-tr_M correction |
| PR #663 (in flight) | MILP / SDP-PL: `a = z_markov` substrate-clean (i.e. the PL integration limit equals the Markov parameter — no fitting) |
| PR #664 (in flight) | c_3 = -2, c_4 = b²+1/2 categorical claims (status: probes tautological per PR #671 critical review; awaits genuine V_(2,2,2) projection) |
| PR #674 / p4tt-p6 branch | Wenzl LR bridge (Rust + rayon) — fast kernel for n=6,8,12 |
| Sibling main commits | #672 merged (Hoefsmit V_(2,1) matrices); #673 merged (E_0 disentanglement) |

## Goal + hard floor (unchanged from v0)

- **Target:** 1 ppb on $\{m_p, m_n, B(D), B(T), B({}^3\text{He}), B({}^4\text{He})\}$
- **Hard floor:** ~780 ppb from CAL-2 ($q_0$) propagation amplified by $|\partial \ln E_0/\partial \ln q_0| = 11.09$
- **Three calibration anchors only:** $\{m_e, q_0, Q_\beta\}$

## What PR #671 changed about the workplan

**Before PR #671:** workplan v0 framed the m_p chain residual (1571× shortfall: m_p_pred 0.5974 MeV vs CODATA 938.27 MeV) as something to be closed by Phase 1 brane-tower work + Phase 3 Δ_coupling. The dual-tr_M issue was hidden under the misleading `tr_M_symbolic` name; the F_n decomposition was treated as a well-defined ladder.

**After PR #671:**

1. **Production-code correction**: `mass_formula_6term_mpfr_50dps` uses
   canonical Markov via `_bridge_tr_M` (verified). The shipped m_p / m_n /
   m_He predictions on main are using the **correct trace**, not the
   Plancherel mis-named one. No 50-99% drift in mass predictions.

2. **Δ_coupling substrate-derivation** ([`conj:delta-coupling-substrate-form`](https://github.com/litlfred/qou/blob/claude/post-670-story-b-mp-c5-c6/content/quantum-observable-universe/braids-and-knots/delta-coupling-substrate-form.md))
   identifies the leading-form factors:
   - $(A-2)$ ← canonical-atomic-braid excess-strand topology
   - $E_0 = m_e/(q(q-1))$ ← Hecke energy unit
   - $\log(1/h(q_0)) = \log(1/(k_B T_q)) - \log(1+q_0)$ ← thermodynamic + skein
   At $(2,2)$: predicts 13.103 MeV vs extracted +13.20 MeV — **0.71% residual** open.

3. **F_n decomposition is NOT bare-Markov**: the Q_β precision-ladder
   $F_n = 1 + c_n \hbar_q^{2n}$ does NOT come from the Taylor expansion
   of $\text{tr}_M(\sigma_1^2)$ (proven via the closed-form
   [`prop:trm-hopf-sigma1-sq-closed-form`](https://github.com/litlfred/qou/blob/claude/post-670-story-b-mp-c5-c6/content/quantum-observable-universe/braids-and-knots/trm-hopf-sigma1-sq-closed-form.md)).
   Each $F_n$ requires a separate Wedderburn-block projection.

4. **PR #664's V_(2,2,2) channel claim refuted**: direct per-block
   computation shows V_(2,2,2) contributes $+3.79 \times 10^{-3}$ to
   $\text{tr}_M(\sigma_1^2)$ at $q_0$, but the framework F_3 ansatz value
   is $-1.24 \times 10^{-6}$ — opposite sign, off by ~3000×. PR #664's
   c_3 derivation is structurally incomplete.

5. **q-Edgeworth κ_3 refuted** as Δ_coupling source: $\kappa_3 = -0.675$
   at $q_0$ has wrong sign for over-binding.

## Refined milestone ladder

| Milestone | Target | Status (post-PR #671) | Blocker / next concrete task |
|---|---|---|---|
| **M0** (current) | ~22% MAE | shipping on main | — |
| **M1** | ~1% MAE on light isotopes | Phase 1 + P2.A done | Cross-anchor verification of Δ_coupling closed-form on (2,1), (1,2) — pending PR #663 / #664 data; unblocks M1 honest signal |
| **M2** | ~0.1% on light | + closed-form Δ_coupling at multiple anchors | **PR-671-NEW**: Phase 3 systematic Δ_coupling probe on AME data |
| **M3** | ~100 ppm | + V_(2,2,2)-projection-chain genuine F_3 | **NEW**: V_(2,2,2) projector probe (audit doc on PR #671 lays out 6-step scope) |
| **M4** | ~10 ppb | + Wenzl LR bridge fast kernel for n=8,12 (PR #674) | Wenzl LR Rust bridge — PR #674 in flight; await merge |
| **M5** | ~1 ppb | + Lean closure (Phase 4) + N=4 truncation per #639 c(K) ceiling | Phase 4 Lean handover; conditional theorems for the V_(2,2,2)→F_3 chain |
| **Hard floor** | ~780 ppb | CAL-2 propagation; cannot improve without $q_0$ precision | unfixable without sharper CAL-2 |

## v1 phase plan (after PR #671 merges)

### Phase 1' — Cross-anchor verification (was Phase 1 + P3.A)

Take PR #671's $\Delta_{\text{coupling}}$ leading-form
$(A-2) \cdot E_0 \cdot \log(1/h)$ and verify it at the other magic-shell
anchors:

- **P1'.A**: Compute $\Delta_{\text{coupling}}(2, 1)$ for ³He=D+p once
  PR #663's $\Delta_{\text{cat}}$ data for proton lands on main (or
  cherry-pick the witness).
- **P1'.B**: Compute $\Delta_{\text{coupling}}(1, 2)$ for T=D+n same way.
- **P1'.C**: Compute $\Delta_{\text{coupling}}(4, 4)$ for $^8$Be, the
  next doubly-magic-adjacent anchor; verify $(A-2)$ scaling.
- **P1'.D**: Compute $\Delta_{\text{coupling}}$ at the genuine higher
  magic shells $^{16}$O (2,2,2,2 closed), $^{40}$Ca (full shell).

If $(A-2) \cdot E_0 \cdot \log(1/h)$ holds within 1% at all anchors,
promote `conj:delta-coupling-substrate-form` to a proposition.
If gap shape is systematic, derive the corrective ansatz.

**Estimated effort:** 1 PR (~100 lines + 5 witness files).

### Phase 2' — Genuine V_(2,2,2) F_3 derivation

Per audit doc [`2026-05-17-F-n-derivation-analysis.md`](2026-05-17-F-n-derivation-analysis.md)
§"Next-PR scope":

- Compute symbolic projector $P_{(2,2,2)}$ from $y_{(2,2,2)} \cdot \chi^{(2,2,2)}$
  (cached on main via `y-lambda-jones-markov-witness.json`).
- Compute $P_{(2,2,2)} \cdot \sigma_1^2 \cdot P_{(2,2,2)}$ as a Hecke
  element; take Markov trace.
- Expand at $q = 1 + \varepsilon$ to order $\varepsilon^6$; extract leading.
- Compare to F_3 ansatz $-2 \cdot b^3 \cdot \hbar_q^6$.

**Outcomes:**
- If equal: genuine F_3 derivation; promote `conj:hopf-jones-c3-categorical`
  to proposition.
- If unequal: PR #664's chain is structurally wrong; need fresh
  channel identification.

**Estimated effort:** 1 PR (~150 lines + audit doc + witness).

### Phase 3' — m_p chain closure (was Phase 1 items B/C)

Items B and C from PR #671's m_p audit
[`2026-05-17-m-p-chain-closure-gap-analysis.md`](2026-05-17-m-p-chain-closure-gap-analysis.md):

- **P3'.B**: T5 categorical attribution — open R&D. Cite PR #663's
  finding `a = z_markov` (SDP-PL integration limit equals Markov
  parameter) as a possible structural source for T5's
  chirality-BW signature.
- **P3'.C**: Full Habiro residue at A=1 — cheap probe; evaluate the
  Habiro generating-function residue without small-tail truncation.

If T5 + T6 contribute the 1571× factor needed to close m_p_pred from
0.5974 MeV to 938.27 MeV, the m_p chain becomes structurally complete.

**Estimated effort:** 2 PRs (~100 lines each + audit + witness).

### Phase 4' — Wenzl LR bridge integration (post PR #674)

PR #674 / p4tt-p6 branch ships a Rust + rayon Wenzl LR bridge. After
that merges:

- **P4'.A**: Wire it into `mass_formula_6term_mpfr_50dps` for n=8, 12.
- **P4'.B**: Use it to do per-Wedderburn-block traces of compound
  braids (D⊕D, T⊕p, ³He⊕n in H_12) needed for the compositional
  Model B ⁴He approach the workplan v0 mentioned.

**Estimated effort:** 1 PR (~50 lines wiring + tests).

### Phase 5' — Lean closure (was Phase 4)

Delegate to Lean agent per `2026-05-12-lean-handover.md`. Adds:
- Lean proof of `prop:hecke-log-decomposition` (algebraic identity;
  needs Real.log Mathlib machinery)
- Lean proof of `prop:trm-hopf-sigma1-sq-closed-form` (Markov axioms
  + Hecke quadratic relation; needs Hecke-algebra Lean infrastructure)
- Lean class instance for `conj:delta-coupling-substrate-form` once
  Phase 1' promotes it to proposition

## Anti-patterns (reaffirmed from v0)

- ❌ Calibrate $\Delta_{\text{shell}}$ or $\Delta_{\text{coupling}}$ to AME
- ❌ Add ad-hoc per-atom corrections without substrate trace
- ❌ Tune $n_\star$ or $k_\lambda$ per atom without structural justification
- ❌ Hide deuteron-prefactor $\alpha_M$ calibration in Path B Habiro
- ❌ **NEW**: Conflate Plancherel and Markov traces (the dual-tr_M
  audit's lesson). All trace-related work must specify which convention.
- ❌ **NEW**: Claim "c_n categorically derived" without performing
  the explicit per-Wedderburn-block projection. PR #664's pattern
  (textbook value + tautological probe) is not a derivation.

## Cross-PR coordination

| PR | Status | Coordination need |
|---|---|---|
| #671 (this branch) | In review | merge → branch new from main for v1 implementation |
| #663 (isotope-mass) | In review | provide $\Delta_{\text{cat}}$ for {p, n, D, T, ³He} for P1' cross-anchor |
| #664 (c_3 categorical) | In review | resolve by V_(2,2,2) probe (Phase 2') |
| #674 (p4tt-p6 / Wenzl LR) | In review | provides Rust kernel for Phase 4' |

## Recommended next-session sequence

1. **WAIT** for PR #671 to merge.
2. **BRANCH** from main (after #671 lands): `claude/1ppb-phase1-cross-anchor`.
3. **CHERRY-PICK** PR #663's $\Delta_{\text{cat}}$ witness data (with
   coordination on the sibling PR).
4. **EXECUTE** Phase 1' (cross-anchor verification of Δ_coupling).
5. **REPORT** the result; if (A-2)·E_0·log(1/h) holds at all magic-shell
   anchors, the substrate-derivation is structurally complete; if not,
   propose the systematic correction.

Estimated to M1: 1 session, 1 PR. M2 requires Phase 2' (genuine F_3) +
Phase 3' (m_p chain closure), ~3 sessions.

## Open questions for owner

- Q1: Does the H1 form $(A-2) \cdot E_0 \cdot \log(1/h)$ closed-form
  hold at all magic-shell anchors, or just at the doubly-magic (2,2)?
- Q2: For the 0.71% residual at (2,2): accept as next-order substrate
  expansion (open R&D), or close via an explicit Wedderburn-block
  correction inspired by PR #663's `a = z_markov` finding?
- Q3: For PR #664 reconciliation: open a sibling PR specifically for
  the V_(2,2,2) projection chain, or close PR #664 pending the
  genuine derivation?
- Q4: Should the genuine c_3 / F_3 derivation be merged into the
  Phase 1' PR (one substantial PR) or split off as Phase 2'?

---

## v1.1 update (2026-05-17, post-4-negatives synthesis)

PR #671 shipped **4 negative findings** that, taken together, change
the v1 phase plan. The full synthesis is in
[`2026-05-17-structural-diagnosis-operator-valued.md`](2026-05-17-structural-diagnosis-operator-valued.md);
the summary for the workplan is:

| Finding | Tested | Result | Structural lesson |
|---|---|---|---|
| 1 | Refined $\Delta_{\text{coupling}}$ at single-magic anchors | +8.74% (³He), -3.95% (T) — Z↔N asymmetry +0.796 MeV | Symmetric scalar substrate misses |
| 2 | V_(2,2,2) per-block Taylor order | ε^1, not ε^6 — refutes PR #664 c_3 chain | Per-block aggregation is non-trivial |
| 3 | T5 categorical attribution (20 substrate candidates) | None match both anchors AND Z↔N asymmetry (-0.325 MeV) | T5 needs operator-valued structure |
| 4 | Habiro residue at A=1 | Cached `tr_M` IS Habiro-resummed; no separate tail | m_p gap is brane-tower, not residue |

**All 4 ⇒ the next-PR scope is operator-valued per-Wedderburn-block,
exactly the framework PR #681 audits.**

### Re-prioritized phases (v1.1)

| Phase | Was (v1.0) | Is (v1.1) | Rationale |
|---|---|---|---|
| **Phase 1'** | Cross-anchor verification of leading $(A-2)\cdot E_0 \cdot \log(1/h)$ | **Re-derive** $\Delta_{\text{coupling}}$ via operator-valued $A^\lambda_{\mu,\nu}(I)$ at the per-block level using the H_6 deuteron-interface witness | Finding 1 falsifies the symmetric refinement; the per-block route is the next concrete derivation |
| **Phase 2'** | Genuine V_(2,2,2) projection for F_3 | **Per-channel** Wedderburn-block contributions to F_3 — V_(2,2,2) alone is structurally incomplete | Finding 2 refutes V_(2,2,2) as single-block channel |
| **Phase 3'** | m_p chain Items B + C separately | **Combined** operator-valued T5 + brane-tower scaling for $\{m_p, m_n, m_{^4\text{He}}\}$ | Findings 3 + 4 share the operator-valued root cause |
| **Phase 4'** | Wenzl LR bridge (PR #674) | unchanged | PR #674 provides the Rust kernel for per-block traces |
| **Phase 5'** | Lean closure | unchanged — MarkovTraceTower class instance landed on PR #671 | discharges the abstraction; downstream conditional theorems remain |

### Concrete next-session scope (single sibling PR)

1. Cherry-pick / re-use [`canonical_tr_m_via_chi_cache.py`](../../computations/canonical_tr_m_via_chi_cache.py) (PR #671 Step 2 combiner).
2. Compute per-block $\chi^\lambda(\beta_{\text{atom}})$ for $\{T, {}^3\text{He}, {}^4\text{He}\}$ once those chi caches complete (tritium cache running on PR #671 branch; ETA minutes).
3. Apply operator-valued $A^\lambda_{\mu,\nu}(I)$ from [`sublemma-2-1-A-operator-extract.witness.json`](../../computations/sublemma-2-1-A-operator-extract.witness.json) (deuteron interface) to extract per-block corrections.
4. Re-derive $\Delta_{\text{coupling}}$ at $(2,1), (1,2), (2,2)$ and check Z↔N asymmetry +0.796 MeV / T5 asymmetry -0.325 MeV reproduce.
5. If reproduced: promote `conj:delta-coupling-substrate-form` to a conditional proposition (Lean class instance pending the operator-valued $A^\lambda_{\mu,\nu}$ class).

### Coordination touch-points (post-v1.1)

| Sibling | Status now | Need from us |
|---|---|---|
| PR #663 (isotope-mass) | $\Delta_{\text{cat}}$ data for {p, n, D, T, ³He} | Use combiner output to provide per-block $\chi^\lambda$ values |
| PR #664 (c_3 categorical) | refuted at per-block level by Finding 2 | Coordinate on whether to close PR #664 or pivot it to per-channel F_3 |
| PR #674 (Wenzl LR) | provides Rust kernel | Wire into combiner once it merges |
| PR #681 (operator-valued Wenzl audit) | provides theoretical framework | Cite as the canonical reference; offer combiner + chi caches as Step 3 input |

### What is NOT changed by v1.1

- M0–M5 milestone target percentages stay the same
- Three-anchor calibration discipline unchanged
- Hard floor ~780 ppb unchanged
- Anti-patterns list unchanged (and now strengthened: "scalar-substrate
  refinements without Z↔N-asymmetric / operator-valued structure
  are insufficient")
