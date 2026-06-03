# 1ppQ Master Ledger — Q_β

> Single source of truth for the **1 ppQ (10⁻¹⁵) Q_β** goal.
>
> Per `STATUS.md`: this is the achievable arm of the 1ppQ target;
> absolute m_p / m_n / m_⁴He at 1ppQ remain Subgoal-2 territory
> (substrate-derivation of q_0 required, declined 2026-05-08).

## Why this ledger exists

The Q_β c_k Taylor coefficients have flip-flopped four times across
sessions. Each flip wasted ~1 session and produced contradictory
prose in the dashboard. This ledger:

1. **Pins the canonical status of each c_k** so the next session
   doesn't re-derive a "discovery" that was already retracted.
2. **Catalogues the retraction history** so the failure modes are
   visible (typically: conflating "near-match" with "Taylor-exact").
3. **Lists open probes** so multiple agents can fork distinct
   threads without stepping on each other.
4. **Logs session intent + results** so an interrupted thread can
   be picked up by another agent.

## c_k status (as of 2026-06-03)

**Update 2026-06-03**: structural narrowing landed across this session's
PRs (#1746 refutes |c|(λ) candidate #5 — only 1 of 5 scalar candidates
remains, with basis-convention objection; #1727 verdict from earlier
this week: SIMPLE POLE at u_substrate, fibre-level — `c_k · u^k`
constancy at k=8,9,10 PASSES 1% tier). c_k status table itself
unchanged below — keystone remains the Habiro element identification
(scaling map `f: Δtr_M(√u) ↦ Q_β(c_3 at u³)`; live work in sibling
PR #1739 pre-archimedean recursion + bridge instance).

| Coefficient | Status | Evidence | Open question |
|-------------|--------|----------|---------------|
| **c_2** | **Taylor-exact (derived)** ✓ | `f4930df95` ("honest c_k bar — only Taylor-exact c_2 wired") | none |
| **c_3** | **NOT derived** — near-match (J_Hopf(q=1)=-2), 2.98% cross-anchor swing >> 10⁻⁵⁰ compute precision | `b3c92844d`, `6ace8153e`, [verdict 2026-05-31](../audits/2026-05-31-qbeta-c3-q0-stability-verdict.md); **structural reason** [order audit 2026-05-31](../audits/2026-05-31-qbeta-c3-order-audit-accidental-coincidence.md) (PR #1593) | **SETTLED** as near-match. The block `-2` is at order √u (ε¹); ladder c_3 is at u³ (ε⁶) — accidental coincidence. Resolution path = the scaling map f (Habiro element), not a c_3 value. |
| **c_4** | **NOT derived** — CAL-anchored tier | `453918755` ("CAL-anchored, honestly labeled") | derive canonically via Habiro recursion |
| **c_5** | **NOT derived** | — | extend Habiro recursion |
| **c_6** | **NOT derived** | — | extend Habiro recursion |
| **c_7** | **NOT derived** — target for 1ppQ | per `6ace8153e` truncation analysis: N=7 → 1ppQ | extend Habiro recursion |

**Reading:** the 1ppQ truncation analysis (`6ace8153e`) says N=7 is required.
The Habiro q-difference equation (`d6b6e0483`) gives a recursive
generator for c_k. If c_3 can be settled canonically, the same recursion
extends to c_4–c_7 with relative ease. **c_3 is the keystone.**

## Truncation-order math (reference, from `6ace8153e`)

Q_β = Q_base · Π_{k≥2} (1 + c_k · u^k)  where u = b · ℏ_q² ≈ 0.00852

- Each rung buys log₁₀(1/u) ≈ **2.07 digits**.
- N(ε) ≥ log₁₀(1/ε)/2.07 − 1.
- 100× exp target (≈ 8 ppb) → N=3
- 1 ppb → N=4
- 1 ppt → N=5
- **1 ppQ → N=7**

## Open probes (current queue)

- [x] **PROBE 1 — c_3 q_0-stability** (DONE this session, 2026-05-31): verdict NEAR-MATCH. The 2.98% cross-anchor swing exceeds 10⁻⁵⁰ compute precision by 48 orders of magnitude — c_3 = -2 is NOT Taylor-exact at the value level, and J_Hopf(q) − ℏ_q²(q) is not the right q-dependent function either. Audit: [`docs/audits/2026-05-31-qbeta-c3-q0-stability-verdict.md`](../audits/2026-05-31-qbeta-c3-q0-stability-verdict.md).
- [ ] **PROBE NEW — Q_β Habiro element search** (the actual blocker — parallel α_EM PR #1511). High priority; this is the keystone for all c_k≥3.
  - **Sub-attack result (symbolic q-difference solve, PR #1593, 2026-05-31):** ORDER AUDIT — the per-block `Δtr_M` contributions are O(√u) (ε¹, leading −2/−1/−2) while ladder c_3 is O(u³) (ε⁶). The shared `−2` is an **accidental cross-order coincidence (5 ε-orders apart)**, not a structural identity — the root cause of the flip-flop. Sharpens the target: the Habiro element is the **scaling/eigenphase map f: Δtr_M(√u) ↦ Q_β(c_3 at u³)**, NOT a value for c_3. q₀-independence confirmed (per-block coeffs fixed rationals). Audit: [`docs/audits/2026-05-31-qbeta-c3-order-audit-accidental-coincidence.md`](../audits/2026-05-31-qbeta-c3-order-audit-accidental-coincidence.md). No fitted form proposed.
- [ ] **PROBE 2 — c_4 coefficients** from the Habiro element (renamed from c_4 Habiro recursion). Blocked on the search.
- [ ] **PROBE 3 — c_5 / c_6 / c_7 coefficients** from the Habiro element. Blocked on c_4.
- [ ] **PROBE 4 — Lean §3b-cond classes for each c_k** mirroring `QbetaC3StructuralFormClass` (`441c291fc`).
- [ ] **PROBE 5 — _precision.py headroom bump** to 70 dps compute / 60 dps output (for safe 10⁻¹⁵ arithmetic).

## Active PRs

| PR | Scope | Relation to 1ppQ-Q_β |
|----|-------|----------------------|
| #1577 | canonical-watcher: automate Q_β c_k flip-flop prevention | **direct overlap** — infrastructure to prevent the bug this ledger documents |
| #1521 | Habiro element [2]_q·(1-h²α) categorical 1-loop | **direct upstream** — the canonical c_k source |
| #1543 | ⁴He magic-A binding | adjacent (binding side) |
| #1580 | coord infrastructure + 1ppQ kickoff | sets up this ledger + STATUS.md + queue file + /session-intent + /pending-show + SessionStart hook |
| #1579 | CAL-3 = m_π corroboration + parallel c_3 derivation attempt | **parallel arrival** — independent c_3 single-coefficient derivation attempt landed NEGATIVE simultaneously; corroborates the SETTLED verdict via a different methodology (15 candidate categorical formulas at both q₀ anchors). See [`docs/audits/2026-05-31-c-3-categorical-derivation-attempt.md`](../audits/2026-05-31-c-3-categorical-derivation-attempt.md) and [`docs/coordination/2026-05-31-cal-3-m-pi-hunt.md`](2026-05-31-cal-3-m-pi-hunt.md) |

## Flip-flop history (DO NOT REPEAT)

| # | Date | Commit | What flipped | Why (failure mode) |
|---|------|--------|--------------|---------------------|
| 1 | 2026-05-26 | `b2f908731` | c_3 = J − ℏ_q² "0.004% sub-leading" | over-claimed near-match as Taylor-exact |
| 2 | 2026-05-29 | `41b8d4a4c` | wire(Q_β) restore derived c_3 = J(q=1) = −2 | same conflation, different prose |
| 3 | 2026-05-30 | `f4930df95` | wire(Q_β) honest c_k bar — revert c_3 | corrected |
| 4 | 2026-05-30 | `c1f7487df` → `b3c92844d` | deep-audit re-wired c_3, then "stale-q₀ artifact" | conflated FACT A (N=3 beats 100×) with FACT B (c_3 = −2 is NOT Taylor-exact) |
| **5 (settled)** | 2026-05-31 | this PR #1580 | **probe-c3-q0-stability verdict: NEAR-MATCH, not Taylor-exact. Habiro element identification is the resolution path.** | (no flip — settled) |
| **6 (ruled out, not a flip)** | 2026-05-31 | claude/phi-q-spectral-combiner-2026-05-31 (PR #1609) | Li_2^q × spectral combiner — μ_λ := Li_2^q(−abs χ_λ) / Σ Li_2^q(−abs χ_λ'); c_3 candidate = Σ μ_λ · c_3^(λ); Σ μ_λ = 1 by construction (cures mech #6 defect). Single-anchor result at q_proton: c_3 cand = −1.797 vs empirical −2.07 → **REFUTED by 13%**. Cross-anchor q_muon deferred (Hoefsmit χ_λ(q) evaluator not yet wired). | new mechanism #7 added to b502b9b83 list — not a flip-flop, never claimed as derivation |

**Failure mode pattern:** every flip used a fresh canonical-looking formula
(`J − ℏ_q²`, `J_Hopf(q=1)`) and matched it numerically near the substrate
q_0. The "match" became "derivation" became "wired". On re-pinning q_0
(`c1f7487df` → `b3c92844d`) the "match" moved and revealed the original
formula was q_0-dependent — i.e. not Taylor-exact, just a near-match at
one anchor.

**Anti-pattern signature:** if a c_k "derivation" reports < 1% match at
muon-pin AND at proton-pin AND at any other q_0 cross-anchor — and the
match is < the difference between those anchors — it's likely
Taylor-exact. Otherwise, it's a near-match.

## Sessions log

| Date | Agent / branch | Intent | Results |
|------|----------------|--------|---------|
| 2026-05-31 | Claude / `claude/coord-infra-1ppq-2026-05-31` | (1) create this ledger + STATUS.md, (2) coord with #1577, (3) ask user about queue-schema formalization, (4) probe c_3 q_0-stability if scope permits | (1) ✓ STATUS.md + 1ppq-qbeta.md committed; PR #1580 MERGED. (2) ✓ intent comment on #1577 (subsequently merged independently). (3) ✓ user chose: TodoItem JSON, no explicit claim, intent at branch-open, pre-work main sweep, new skills `/session-intent` + `/pending-show` + SessionStart hook. (4) ✓ **probe-c3-q0-stability SETTLED** — verdict: NEAR-MATCH, not Taylor-exact. 2.98% cross-anchor swing >> 10⁻⁵⁰ compute precision; J_Hopf(q=1)=-2 nominal mismatches empirical c_3 at both anchors by 0.48% (muon) / 3.46% (m_p). Q_β Habiro element search added as new keystone probe. Audit doc: [`docs/audits/2026-05-31-qbeta-c3-q0-stability-verdict.md`](../audits/2026-05-31-qbeta-c3-q0-stability-verdict.md). Also addressed 4 Gemini review comments on PR #1580. |
| 2026-05-31 (cont.) | Claude / `claude/qbeta-habiro-element-search-2026-05-31` | claim `probe-qbeta-habiro-element-search` after #1580 merge; structural attack on Q_β Habiro element | PARTIAL — consolidation only. Synthesized state from b502b9b83 (6 mechanisms ruled out, 1 left), d6b6e0483 (recursive pair-rules same near-match gap), qbeta_habiro_taylor_investigation (categorical f missing), qbeta_habiro_tower_1ppq (form-fitting iterative peel). Added 5 untested-but-not-falsified attack candidates to queue with pre-stated failure-mode signatures (non-uniform multi-block PRODUCT decomp, exponentiated per-block, symbolic q-diff solve, modular bootstrap, Galois descent). Queue status: in_progress (awaiting next session/sibling agent for symbolic attack). NO 7th near-match candidate proposed (avoiding flip-flop trap). PR #1585 MERGED. |
| 2026-05-31 (cont. 2) | Claude / `claude/qbeta-ck-lean-3bcond-classes-2026-05-31` | claim `probe-ck-lean-3bcond-classes`; add Lean §3b-cond classes for c_4–c_7 mirroring c_3 pattern | IN PROGRESS — added classes + axioms + Q_beta_nk_categorical + q_beta_nk_structural_form for k=4,5,6,7 to content/quantum-observable-universe/mass-theory/q-beta-categorical-precision-ladder.lean (~188 lines added). Closed forms taken verbatim from existing canonical instance; no instances of new classes provided (matching c_3 discipline). PR #1587 opened. Lean LSP couldn't start locally (toolchain install blocked); CI verification pending. |
| 2026-05-31 (cont. 3) | Claude / `claude/qbeta-habiro-symbolic-solve-2026-05-31` | pick up the **symbolic q-difference solve** sub-attack deferred by #1585 (cont.) | CHARACTERIZATION (no closure) — ORDER AUDIT via exact symbolic ε-series of the per-block `Δtr_M` closed forms vs the ladder variable u=b·ℏ². Found: per-block forms are O(√u) (ε¹, leading −2/−1/−2) while ladder c_3 is O(u³) (ε⁶) — the shared `−2` is an **accidental cross-order coincidence (5 ε-orders apart)**, not a structural identity, which is the **root cause of the 4-session flip-flop**. q₀-independence diagnostic: per-block coeffs are fixed rationals (anchor-invariant) ⇒ the empirical c_3 swing lives entirely in the open categorical map f. Sharpens the open problem: the Habiro element is the **scaling/eigenphase map f: Δtr_M(√u) ↦ Q_β(c_3 at u³)**, NOT a c_3 value. No fitted form proposed. Probe `qbeta_multiblock_order_audit.py`; audit `docs/audits/2026-05-31-qbeta-c3-order-audit-accidental-coincidence.md`; PR #1593. |
| 2026-06-01 | Claude / `claude/qbeta-1ppq-narrowing-2026-06-01` | (1) derive scaling map f directly; (2) precision headroom (PROBE 5); (3) Lean §3b-cond audit (PROBE 4); (4) L2 dashboard refresh | (1) CHARACTERIZATION — Taylor-expanded the N=1 cos eigenphase `cos(α−bℏ²/2)` in u=b·ℏ² (dual symbolic+numeric, cross-checked): a_0=1, a_1=**−√3/12**, a_2=−11/32−√3/12. **KEY: a_1 ≠ 0** ⇒ the eigenphase has a u¹ term but the ladder `Π(1+c_k u^k)` starts at u² (no c_1) ⇒ **"eigenphase = f" FALSIFIED at u¹**. New constraint on f: must cancel the u¹ term + supply c_2=−1 exactly (points at a paired/bar-symmetric construction). Probe `qbeta_eigenphase_taylor_in_u.py`; audit `docs/audits/2026-06-01-qbeta-eigenphase-not-f-falsified-at-u1.md`. (2) PROBE 5: ran at 70 dps via local `set_compute_dps(70)` (opt-in, no global bump). (3) PROBE 4 audit: all 5 §3b-cond classes (c_3–c_7) confirmed **instance-free**, conditional theorems sorry-free, no stray instances anywhere — discipline holds. Added 6 sorry-free Lean base-point anchors (`hbarQ_one`…`N1_factor_one`, `hoefsmitB_one=√3/2`); CI-verify pending (no local lake). (4) L2 doc refresh: m_μ flipped ✓→✗ post re-pin (209.8 ppb, independent of Q_β chain). PR #1602. No fitted form. |
| 2026-06-01 (cont.) | Claude / `claude/phi-q-modulus-audit-and-reframe-2026-06-01` + sister `claude/qbeta-signed-vs-abs-tower-2026-06-01` | per user: (a) `Φ_q(signed)` vs `Φ_q(|...|)` sensitivity diagnostic; (b) full paper `|...|` audit in non-archimedean sections; (c) tier-2 refactor representative; (d) compute implications | (a) PR #1641 — at v=±0.142 (Δtr_M scale), `Φ_q(+v)/Φ_q(-v)` ratio = **13.3** (92% per-term divergence); `|...|` is structural CHOICE, not convergence requirement. (b) PR #1643 — 212 sites scanned, **34 NON-ARCH-MISUSE** (mass-theory 24, mass-endomorphism 4, braids-and-knots 3, others 3); Tier 1 (`conj:im-q-physical-role`) reclassified as audit FALSE POSITIVE (correctly discusses archimedean projection). (c) Representative refactor on `atom-knot-mass-derivation.md` lines 66, 76 — `\|tr_M(T_w)\|` → `tr_M(T_w)`, `\|V̂_i\|` → `V̂_i` in the explicitly-stated pre-archimedean formula. (d) Compute implications doc: production single-nucleon V̂ all positive ⇒ `\|...\|` no-op there; higher-level jets could change ≤92% per term. Q_β = m_n − m_p insensitive if correlated, unverified. Coord posts on #1642 ζ_8-Habiro keystone, #1636 α_EM bar-involution, #1622 q-diff Fourier ladder, #1640 sister audit tool. ESCALATED to author: 32 remaining tier-2 sites need per-site author review (regex audit imprecise per Tier 1 false positive). |
| 2026-06-02 | Claude / `claude/qbeta-habiro-element-2026-06-02` (PR #1713) | open Topic 1 of PR #1698 follow-up — re-frame Q_β c_k via fibre-vs-observable distinction (CLAUDE.md 2026-06-01 banner); target the fibre-level Habiro element `F(q)` whose archimedean evaluation at any q_0 reproduces c_k at that anchor; cherry-pick categorical-ID framework from sibling #1521 (`[2]_q = J_2(unknot)`, `1/(8π) = π·dim H¹(M_Bring)`); Phase A re-frame, Phase B symbolic q-diff OR Galois descent on Habiro ring; Phase C deferred Lean §3b-cond `QBetaHabiroElement` | SCOPING — branch + PR #1713 opened with scope doc `docs/coordination/2026-06-02-qbeta-habiro-element-scope.md`. Intent comment posted on #1521. Coordinated with parallel Topic 2+3 branch `claude/m-p-linking-weight-and-binding-link-2026-06-02` (PR #1712) addressing the Subgoal-1 closure thread on m_p linking_weight + ²H/³H binding-link canonical objects. Forbidden routes (CLAUDE.md): no ansatz fits, no binary wired/dropped, no production wiring before cross-anchor (q_proton + q_muon). |
| 2026-06-02 (cont.) | Claude / `claude/qbeta-habiro-element-2026-06-02` (PR #1713) MERGED | Phase B symbolic q-difference attack | RESULT — Q_β Habiro element `F(u) = Π (1 + c_k u^k)` has **radius of convergence exactly equal to u_substrate** at q_0; asymptotic `c_{k+1}/c_k → 1/u = 117.41` matched to 4 sig figs at k=8,9,10. Refutes 2-term constant-coefficient recurrence. Confirms CLAUDE.md fibre-vs-observable framing — c_k live in the fibre; archimedean eval at q_0 hits a singularity. Sharpens c_3 flip-flop saga: searching for real `c_3 = f(q_0_real)` matching multiple anchors NEAR a singularity was always going to fail. Audit `docs/audits/2026-06-02-qbeta-habiro-radius-of-convergence-at-u-substrate.md`. NO categorical residue ID claimed. Merged `a99493e20c`. |
| 2026-06-02 (cont. 2) | Claude / `claude/qbeta-1ppq-closure-2026-06-02` (PR #1727) | Steps 1+2+3 of 1ppQ closure follow-up — singularity-type ID, cross-anchor validation, documentation-level dashboard | RESULT — **SIMPLE POLE at u_substrate, fibre-level**. Step 1: c_k · u^k constancy at k=8,9,10 with 0.02 % spread (PASSES 1 % tier); branch-fit β = 0.999 confirms simple-pole interpretation. Step 2: cross-anchor `u_subst(q_muon)` vs `u_subst(q_proton)` differs by **210 ppb** (well within 1 ppm fibre-level tolerance) — singularity is at the SAME location at both anchors. Step 3 documentation-level: structural verdict landed in audit + this ledger; **NO production-script wiring** because residue `A = 1.804e-15 ≈ 1 ppQ` has no categorical closed-form derivation yet (forbidden ansatz fit). Audit `docs/audits/2026-06-02-qbeta-1ppq-singularity-simple-pole-fibre-level.md`. Open research target: identify A categorically (`ℏ_q^N`? `b^N · ℏ_q^M`? `Q_β · ε_struct`?). |
| 2026-06-03 | Claude (session `017uTFqMEnyAuPwyUtUQZ6oU`) / merged PRs #1746 + #1749 | (1) refute the 5th of 5 categorical-candidate constructions for `|c|(λ)` in the abs-content scoping doc; (2) reconcile cheat-sheet §5 manager-view against live witness + 1ppQ ledger + STATUS.md (3 stale claims caught) | RESULTS — (1) Candidate #5 ("sum of `χ^λ(s_k)` over Coxeter generators") FALSIFIED via Murnaghan-Nakayama: `χ^λ(s_k) = f^λ · 2c(λ)/(n(n−1))` — proportional to *signed* `c(λ)`, not L¹ norm `|c|(λ)`. Counterexample at `(2,2)`: self-conjugate ⇒ Coxeter sums = 0, but `|c|((2,2)) = 2`. **Only 1 of 5 scalar candidates remains** (trace of `|Ω_q|`, with basis-convention objection from PR #1641/#1643). Sharpened Δ_λ-gate discipline: no more scalar candidates; wait for operator-valued combiner upstream. PR #1746 merged `515547117a`. (2) Cheat sheet §5 #2 stale claim "Q_β passes 100×" + "c_3 = -2 = J_Hopf(q=1) categorical-closure-friendly" — both inverted by live state (Q_β 164× miss post-q₀-re-pin; c_3 = -2 is flip-flop entry #4, settled NEAR-MATCH per PR #1593 order audit). §5 #4 stale "3 of 6 pass, gaps (m_p, m_n, Δ_pn)" — live is 3 of **7**, gaps are **(m_μ, Q_β, m_n, Δ_pn)** (m_p PASSES, m_μ is independent μ–p floor). PR #1749 merged `63dfa8cec6`. Net 1ppQ-closure contribution: documentation truth-tracking + categorical refutation cumulatively narrow the search space without proposing forbidden Ansätze. |
| 2026-06-03 (cont.) | Claude / `claude/geom-full-knot-dependent-fix-2026-06-03` | fix cheat-sheet's `Geom_full(𝓑₃, q₀)` framing — user caught the knot-collapse that mirrors the production-compute bug (per [`vol-usage-audit 2026-06-02`](../audits/2026-06-02-vol-usage-audit-uniform-vs-per-knot.md): 87 of 89 scripts uniform-Vol(𝓑₃); 64 atom-touching scripts have the bug); update 1ppQ ledger sessions log | IN PROGRESS — cheat sheet 4 places fixed: §3 mass-identity row (m(K) = m_e·Geom_full(K, q₀) with K-dependence), §5 frontier callout, §5 manager-view #1 (per-knot wire-up, not single-knot refinement), §5 framing-correction blockquote (per-knot work, not λ_scale calibration), §5 lambda-scale-absorbed blockquote (knot-dependent + cross-link to vol-usage audit). No compute changes (that's the 64-script research-grade migration tracked separately). This ledger entry. |
| 2026-06-03 (cont. 2) | Claude / `claude/qbeta-markov-trace-2026-06-03` (PR #1750) | Follow-up to PR #1739 caveat §1 (L2 norm basis-dependence); test whether SHAPE × S survives under Markov-trace inner product | RESULT — **STRUCTURAL COLLAPSE**. Under the categorically-natural Hecke-Frobenius norm `⟨X,Y⟩_τ = τ_M(X·Y)`, the SDP min-norm primal-feasible solution is `T_β^Markov = S · I` (scalar multiple of identity; all 6 σ_i / L_± / e_⁻ coefficients are 0). One-line proof: `G_{γ,i} = τ_M(I·b_i) = A_i` ⇒ `G·e_γ = A` ⇒ `G^{-1}A = e_γ` ⇒ `A^T G^{-1} A = τ_M(I) = 1` exactly (12-digit numerical verification at q₀). The 6-channel L2 SHAPE × S from PR #1739 is **basis-dependence of the Euclidean coordinate norm**, not categorical structure. Q_β predictions unchanged (both norms satisfy `τ_M(T_β) = S` by construction; difference is which `T_β ∈ H_3(q)` is canonical). **Implication for c_3 flip-flop saga**: the cross-anchor c_3 swing was extracted from L2-projection Taylor coefficients; under Markov, the c_k come from the Taylor of `S(q) = Q_β(q)/E_0(q)` itself — single q-rational scalar. Whether the swing pattern simplifies is a runnable Step-4 probe, NOT a 7th-mechanism speculative claim. **Implication for residue A categorical-ID** (PR #1727's open target): under Markov, the entire Q_β q-dependence flows through the scalar S(q); residue A is the simple-pole residue of S(q) directly. Audit `docs/audits/2026-06-03-qbeta-markov-trace-shape-collapse.md`. Coord cross-links posted on 6 affected siblings (PR #1752 open, PRs #1739, #1727, #1713, #1649, #1642 retroactive). |

## Cross-refs

- CLAUDE.md §Precision goals (L1 / L2 / Subgoal-1 / Subgoal-2)
- CLAUDE.md §Q_β c_k truncation order framing
- `docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`
- `docs/audits/2026-05-30-l2-100x-status-3-failing-shared-root.md`
- `docs/audits/2026-05-30-klr-dialog-assessment.md` (recurrent re-pitch failure modes)
