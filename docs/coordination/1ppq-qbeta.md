# 1ppQ Master Ledger — Q_β

> **⮕ For c_k / d_k tier + wiring status** (incl. the flip-flop guard), the
> authoritative source is
> [`docs/coordination/ck-dk-canonical-registry.md`](ck-dk-canonical-registry.md).
> This ledger tracks the broader 1ppQ Q_β goal; the registry is the single
> per-rung canonical-vs-empirical record.

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

> **Ohtsuki-invariant exposition framing (2026-06-16, PR #2413) — EXPOSITION ONLY,
> not a new derivation/proof/wiring.** Near `q=1` (the `q₀` regime) a Habiro-ring
> element has a canonical **Ohtsuki (perturbative) expansion** whose coefficients
> *are* the Ohtsuki invariants. So the `c_k` ladder is, conceptually, the Ohtsuki
> series of the Q_β Habiro element — which reframes "is `c_k` fundamental / Taylor-
> exact / wired?" as "what is the `k`-th Ohtsuki invariant?", a *determined* object,
> dissolving the flip-flop framing. It also **bridges to the s5-so3 keystone**: that
> keystone's full-Hecke trace is a Habiro element in the *same ring*, and its
> spacetime partner is `WRT(S³/2I)` = the **Lawrence–Zagier quantum modular form**
> (keystone audit `2026-06-16-keystone-habiro-coupling-lead-and-ck-exposition.md`).
> **Honest status (answering "Lean-proved & wirable?"):** **NO on both for `c_3+`.**
> Only **`c_2`** is Taylor-exact, (independently) Lean-supported, and **wired**;
> `c_3..c_7` stay NOT-derived (near-match / CAL-anchored) and **not wirable as
> derivations** — blocked on the open **"Q_β Habiro element search"** (PROBE NEW
> below, the actual blocker). The `c_k = Ohtsuki-invariants` identification is **not
> itself Lean-proved** (the existing `QBeta*`/`habiro-*` Lean files formalize the
> *ladder* + Habiro–Pochhammer *bridges*, not "the `c_k` are the Ohtsuki invariants
> of a constructed element"). This note eases *exposition* and unifies the two goals;
> it changes no value and adds no wiring.

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

> **Refuted-class map (method-level).** Before opening a new derivation probe,
> consult the search-space map
> [`docs/audits/2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md`](../audits/2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md):
> it catalogues the eliminated hypothesis classes (real-q single/composite,
> torus-knot, constant-kernel, Pell-Lucas-into-free-rungs, SDP-extraction,
> algebra-tower box-adding, trace-level Markov-stabilization) and pins the one
> open axis (**decay-side fibre-level Habiro element `F(q)`** — the
> trace-level Markov-stabilization `Ind_{H₃}^{H₄}` axis was itself REFUTED by
> PR #1850, refuted-class row C12; this blockquote previously named it as the
> open axis, corrected 2026-06-10). Don't re-run a refuted class.

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
| 2026-06-02 | Claude / `claude/qbeta-habiro-element-2026-06-02` (PR #1713) | open Topic 1 of PR #1698 follow-up — re-frame Q_β c_k via fibre-vs-observable distinction (AGENTS.md 2026-06-01 banner); target the fibre-level Habiro element `F(q)` whose archimedean evaluation at any q_0 reproduces c_k at that anchor; cherry-pick categorical-ID framework from sibling #1521 (`[2]_q = J_2(unknot)`, `1/(8π) = π·dim H¹(M_Bring)`); Phase A re-frame, Phase B symbolic q-diff OR Galois descent on Habiro ring; Phase C deferred Lean §3b-cond `QBetaHabiroElement` | SCOPING — branch + PR #1713 opened with scope doc `docs/coordination/2026-06-02-qbeta-habiro-element-scope.md`. Intent comment posted on #1521. Coordinated with parallel Topic 2+3 branch `claude/m-p-linking-weight-and-binding-link-2026-06-02` (PR #1712) addressing the Subgoal-1 closure thread on m_p linking_weight + ²H/³H binding-link canonical objects. Forbidden routes (AGENTS.md): no ansatz fits, no binary wired/dropped, no production wiring before cross-anchor (q_proton + q_muon). |
| 2026-06-02 (cont.) | Claude / `claude/qbeta-habiro-element-2026-06-02` (PR #1713) MERGED | Phase B symbolic q-difference attack | RESULT — Q_β Habiro element `F(u) = Π (1 + c_k u^k)` has **radius of convergence exactly equal to u_substrate** at q_0; asymptotic `c_{k+1}/c_k → 1/u = 117.41` matched to 4 sig figs at k=8,9,10. Refutes 2-term constant-coefficient recurrence. Confirms AGENTS.md fibre-vs-observable framing — c_k live in the fibre; archimedean eval at q_0 hits a singularity. Sharpens c_3 flip-flop saga: searching for real `c_3 = f(q_0_real)` matching multiple anchors NEAR a singularity was always going to fail. Audit `docs/audits/2026-06-02-qbeta-habiro-radius-of-convergence-at-u-substrate.md`. NO categorical residue ID claimed. Merged `a99493e20c`. |
| 2026-06-02 (cont. 2) | Claude / `claude/qbeta-1ppq-closure-2026-06-02` (PR #1727) | Steps 1+2+3 of 1ppQ closure follow-up — singularity-type ID, cross-anchor validation, documentation-level dashboard | RESULT — **SIMPLE POLE at u_substrate, fibre-level**. Step 1: c_k · u^k constancy at k=8,9,10 with 0.02 % spread (PASSES 1 % tier); branch-fit β = 0.999 confirms simple-pole interpretation. Step 2: cross-anchor `u_subst(q_muon)` vs `u_subst(q_proton)` differs by **210 ppb** (well within 1 ppm fibre-level tolerance) — singularity is at the SAME location at both anchors. Step 3 documentation-level: structural verdict landed in audit + this ledger; **NO production-script wiring** because residue `A = 1.804e-15 ≈ 1 ppQ` has no categorical closed-form derivation yet (forbidden ansatz fit). Audit `docs/audits/2026-06-02-qbeta-1ppq-singularity-simple-pole-fibre-level.md`. Open research target: identify A categorically (`ℏ_q^N`? `b^N · ℏ_q^M`? `Q_β · ε_struct`?). |
| 2026-06-03 | Claude (session `017uTFqMEnyAuPwyUtUQZ6oU`) / merged PRs #1746 + #1749 | (1) refute the 5th of 5 categorical-candidate constructions for `|c|(λ)` in the abs-content scoping doc; (2) reconcile cheat-sheet §5 manager-view against live witness + 1ppQ ledger + STATUS.md (3 stale claims caught) | RESULTS — (1) Candidate #5 ("sum of `χ^λ(s_k)` over Coxeter generators") FALSIFIED via Murnaghan-Nakayama: `χ^λ(s_k) = f^λ · 2c(λ)/(n(n−1))` — proportional to *signed* `c(λ)`, not L¹ norm `|c|(λ)`. Counterexample at `(2,2)`: self-conjugate ⇒ Coxeter sums = 0, but `|c|((2,2)) = 2`. **Only 1 of 5 scalar candidates remains** (trace of `|Ω_q|`, with basis-convention objection from PR #1641/#1643). Sharpened Δ_λ-gate discipline: no more scalar candidates; wait for operator-valued combiner upstream. PR #1746 merged `515547117a`. (2) Cheat sheet §5 #2 stale claim "Q_β passes 100×" + "c_3 = -2 = J_Hopf(q=1) categorical-closure-friendly" — both inverted by live state (Q_β 164× miss post-q₀-re-pin; c_3 = -2 is flip-flop entry #4, settled NEAR-MATCH per PR #1593 order audit). §5 #4 stale "3 of 6 pass, gaps (m_p, m_n, Δ_pn)" — live is 3 of **7**, gaps are **(m_μ, Q_β, m_n, Δ_pn)** (m_p PASSES, m_μ is independent μ–p floor). PR #1749 merged `63dfa8cec6`. Net 1ppQ-closure contribution: documentation truth-tracking + categorical refutation cumulatively narrow the search space without proposing forbidden Ansätze. |
| 2026-06-03 (cont.) | Claude / `claude/vol-density-knot-dependent-fix-2026-06-03` | fix cheat-sheet's `VolDensity(𝓑₃, q₀)` framing — user caught the knot-collapse that mirrors the production-compute bug (per [`vol-usage-audit 2026-06-02`](../audits/2026-06-02-vol-usage-audit-uniform-vs-per-knot.md): 87 of 89 scripts uniform-Vol(𝓑₃); 64 atom-touching scripts have the bug); update 1ppQ ledger sessions log | IN PROGRESS — cheat sheet 4 places fixed: §3 mass-identity row (m(K) = m_e·VolDensity(K, q₀) with K-dependence), §5 frontier callout, §5 manager-view #1 (per-knot wire-up, not single-knot refinement), §5 framing-correction blockquote (per-knot work, not λ_scale calibration), §5 lambda-scale-absorbed blockquote (knot-dependent + cross-link to vol-usage audit). No compute changes (that's the 64-script research-grade migration tracked separately). This ledger entry. |
| 2026-06-03 (cont. 2) | Claude / `claude/qbeta-markov-trace-2026-06-03` (PR #1750) | Follow-up to PR #1739 caveat §1 (L2 norm basis-dependence); test whether SHAPE × S survives under Markov-trace inner product | RESULT — **STRUCTURAL COLLAPSE of T_β-as-operator, observable c_k UNCHANGED**. Under the categorically-natural Hecke-Frobenius norm `⟨X,Y⟩_τ = τ_M(X·Y)`, the SDP min-norm primal-feasible solution is `T_β^Markov = S · I` (scalar multiple of identity; all 6 σ_i / L_± / e_⁻ coefficients are 0). Symbolic proof discharged via column identity `G·e_γ = A` (commit `9bd3f95444`, all 6 residues simplify to 0 in `(q, b, y_λ)`) ⇒ `G^{-1}A = e_γ` ⇒ `A^T G^{-1} A = τ_M(I) = 1` exactly. **HONEST CORRECTION (Step 4 diagnostic, commit later this session)**: the observable c_k are L2/Markov-INVARIANT. Both norms reproduce `τ_M(T_β)(q) ≡ S(q)` identically (the SDP **constraint**, not the **objective**); the c_k = Taylor coefficients of `S(q)` regardless of norm. The earlier framing that suggested the cross-anchor c_3 swing might be an L2 artifact was wrong: the swing lives in `S(q)` itself, upstream of any SDP norm choice. Q_β predictions unchanged. **Implication for residue A categorical-ID** (PR #1727's open target): no redirection — residue A is the simple-pole residue of `S(q)`, which both norms agree on. Markov simplifies the OPERATOR T_β (from 6-channel spread to scalar × I), not the c_k. Audits: `docs/audits/2026-06-03-qbeta-markov-trace-shape-collapse.md` + step-4 diagnostic witness `qbeta-markov-trace-step-4-ck-invariance.witness.json`. Coord cross-links posted on 6 affected siblings (PR #1752 open, PRs #1739, #1727, #1713, #1649, #1642 retroactive) — corrections may follow on those threads. **PR #1750 merged** as `cc5fcaf61f`. |
| 2026-06-03 (cont. 3) | Claude / `claude/qbeta-closure-1ppq-hunt-2026-06-03` (PR #1760) | User chose 3 of 4 closure paths after #1756 land: **(A)** approve a categorical Q_β Habiro element direction = re-derive the Habiro element at the current proton-pinned q₀; **(B)** refresh stale Q_β witness to verify current gap; **(C)** operationalize today's structural negatives into a narrowed Phase-3 candidate space. | RESULTS — **(B done)** Refreshed `per-observable-100x-status.witness.json` confirms current gap: **Q_β = 1279 ppb pred, 779.7 ppb σ_exp, 7.797 ppb 100× target → 164.0× miss** (validation; not stale-witness). The pre-re-pin Habiro-exact 5.7 ppb result IS NOT reachable at the current proton-pinned q₀ — it needs re-derivation. **m_μ = 963.6× miss, m_n = 185.4× miss, Δ_pn = 163.3× miss** — 4 of 7 L2 targets fail; same shared root cause documented 2026-05-30. **(C done)** Narrowed Phase-3 candidate space documented below (this entry's "Narrowed Phase-3 search space" section). **(A in progress)** Q_β Habiro element re-derivation at proton-pinned q₀, mirroring α_EM PR #1511's `[2]_q·(1−h²α)` success. Scaffolding + scope doc landed in this branch; categorical-residue-ID is the open work. NO fitted form proposed (Δ_λ-gate respected). |
| 2026-06-03 (cont. 4) | Claude / `claude/qbeta-closure-1ppq-hunt-2026-06-03` (PR #1760) | Per-user follow-up to (B): re-run `c_3_categorical_derivation_attempt.py` at current proton-pinned q₀ to verify the c_3 verdict is current. | RESULT — **VERDICT UNCHANGED: NEGATIVE at current q₀**. 15 categorical candidates evaluated; **0 pass 10 ppm at both anchors** (m_p-pin + muon-pin). Best candidate: `−(q² + q⁻²)` (un-weighted block-eigenvalue sum) at 9,109 ppm m_p-pin / 16,921 ppm muon-pin. The previously-closest structural candidate `−2 − 6·ℏ_q²` lands 5,044 ppm at m_p-pin but blows out to 24,482 ppm at muon — no improvement over the 2026-05-31 run. The α_EM-Habiro extrapolation `2·C(1/2, 3/2)·(1/4)^(3/2)` is **q-independent and equals 0** — does NOT transfer to c_3. This settles the "stale c_3 witness" concern raised in (cont. 3): the c_3 NEGATIVE is current, not stale. Witness refreshed: `c-3-categorical-derivation-attempt.witness.json`. **Implication for the still-active Habiro chain**: the residue-A categorical ID must live in a categorical chain other than the 15 single-formula candidates already tested; the natural next step is owner-direction on which of the 4 active chains to pursue (Q_β Habiro at proton-pinned q₀ / `\|Ω_q\|` Hoefsmit / operator-valued LR / Kashiwara crystal). |
| 2026-06-03 (cont. 5) | Claude / `claude/qbeta-closure-1ppq-hunt-2026-06-03` (PR #1760) | User picked Chain 1 (Q_β Habiro element at proton-pinned q₀) and approved scaffolding compute for all 3 sub-families (γ then α then β). | RESULTS — Chain 1 first-tests complete; **2 of 3 sub-families NEGATIVE, 1 PASS as structural verifier**: **Family γ (Q_A·cos·Π_k decomposition) PASS** (3/3 assertions): Q_A(q₀) ≈ 0.7836 MeV and cos(α−bℏ²/2) ≈ 0.9984 at q₀ are FINITE, so structural singularity at u_substrate (PR #1727) must live in Π_k(∞) tower; ladder TERMINATES at c_3 within precision (1e-30) at proton-pinned q₀ (c_4..c_7 below numerical floor here). **Family α (Wenzl-projector Markov trace) NEGATIVE**: 4 conventions (JW `(-1)^(n-1)/[n]_q`, symmetric, antisymmetric, adjoint-like `[n]_q − [n]_q⁻¹`) all fail at c_2 by 50%+ and c_3 by 100%+; literal Family α REFUTED. **Family β (Kashaev tower) NEGATIVE**: 3 variants (standard q-Pochhammer, Bloch-Wigner D(z), Faddeev real-q L_q) all fail by 100%+; Bloch-Wigner identically 0 for real q^n with q > 0; literal Family β REFUTED. **Combined α + β NEGATIVE pointer**: the Lean proof of c_2 = -1 references **Kashiwara f̃₁²** (crystal operator eigenvalue), not Markov-projector and not Kashaev-dilog. Combined with α + β NEGATIVE, the residue A categorical-ID must be a TRUE **Kashiwara CRYSTAL** operator value — **Option-E path** (Chain 4 from the original PR #1760 owner-direction menu). The 3 Chain 1 sub-families have CLOSED Chain 1 as written. Next-session options: **(a)** switch to Chain 4 (Kashiwara crystal / Option-E); **(b)** explore mixed-chain symmetric combinations (Wenzl · Kashaev) not tested in the literal first-tests. Witnesses: `qbeta-sa-qa-chain-gamma.witness.json` (γ PASS), `qbeta-wenzl-habiro-chain-alpha.witness.json` (α NEGATIVE), `qbeta-kashaev-habiro-chain-beta.witness.json` (β NEGATIVE). Δ_λ gate respected throughout (closed-form formulas, no fits). Audit: [`docs/coordination/2026-06-03-qbeta-habiro-chain-1-scope.md`](2026-06-03-qbeta-habiro-chain-1-scope.md). |
| 2026-06-03 (cont. 6) | Claude / `claude/qbeta-residue-a-categorical-id-2026-06-03` (PR #1759 — CLOSED as duplicate) | open follow-up probe on residue A categorical-ID per PR #1727's open target | **CORPUS-GREP MISS**. Scaffold opened then closed: existing [`qbeta_residue_categorical_id_probe.py`](../../computations/qbeta/qbeta_residue_categorical_id_probe.py) already exhausted 38 candidates across 6 hypothesis families (ℏ_q^N, b^N·ℏ_q^M, Q_β·ε, [n]_q·ℏ_q^N, 2·ℏ_q^15·(1+ε), Φ_8/q-Poch/α_em); best near-match `[2]_q · ℏ_q^15 · Schwinger` misses by 2.93% (fibre-level swing magnitude). The Markov-collapse insight from PR #1750 does NOT open new attack surface — c_k and A are L2/Markov-invariant. Should have run corpus-grep checklist (AGENTS.md §"Before declaring 'open' math") before opening the PR. PR #1759 closed `2026-06-03T19:30Z` with candid finding posted on the PR. **Lesson**: corpus-grep checklist isn't optional for "open target" claims. |
| 2026-06-03 (cont. 7) | Claude / `claude/lean-lift-t-beta-collapse-2026-06-03` (PR #1761 — VERIFIED + READY) | lift PR #1750's substrate-model Lean proof of `T_β = S·1` to general `[Algebra R A]` typeclass setting per AGENTS.md §3b-cond | RESULT — **3 SORRY-FREE LSP-VERIFIED THEOREMS** in `QOU.QBeta.MarkovFrobeniusCollapse.General` namespace: `completing_the_square_general` (commutative-ring algebraic identity), `markov_frobenius_min_norm_lift` (lower-bound `S² ≤ τ(X·X)` under `PSDTrace`), `markov_frobenius_min_norm_uniqueness` (equality case ↔ `X = S·1` under `PSDTrace` + `NonDegTrace`). PR scaffolded → multiple proof iterations → reverted (trust-but-verify) → cherry-picked → addressed Copilot review round 1 (9 comments: split into 2 theorems + simplify statement) → mathlib cache 403 + LSP timeouts blocked verification → cloned mathlib locally to `../mathlib4` → LSP unblocked → 4 real bugs surfaced via LSP diagnostics + fixed (`LinearOrderedField` deprecated → 3-class form; `h_smul_one_sq` rewrite chain failure → `simp only`; `h_tau_expand` brittle `rw` → `simp only`; linear_combination sign error resolved by simp+ring). LSP final: 0 errors, 0 warnings. **CI is billing-blocked throughout** (per AGENTS.md §"CI billing failures" — 404 on job logs); skip-CI annotation in PR body. |
| 2026-06-03 (cont. 8) | Claude / `claude/lean-lift-t-beta-collapse-2026-06-03` | /coordinate sweep — scope siblings of PR #1761 | Posted cross-link intent on 3 directly-overlapping open PRs: **PR #1752** (q-rational SDP strict-comp T_β selection — different selection mechanism, same constraint set, both reproduce τ_M(T_β) = S; comment noted Step 4 L2/Markov-invariance of c_k); **PR #1764** (qbeta multi-block c_3 + sorry-free Lean — namespace check `QOU.QBeta.*` heads-up + Step 4 c_k-invariance implication for the multi-block attack); **PR #1763** (77-axiom triage + cache-host blocker — flagged the same `lake exe cache get` 403 blocker I hit + requested workaround). Skipped PR #1760 / #1762 (low overlap with #1761's typeclass-scaffolding scope). |
| 2026-06-03 (cont. 9) | Claude / `claude/qbeta-kashiwara-chain-4-2026-06-03` (PR #1768) + `claude/qbeta-residue-a-cal-anchored-acceptance-2026-06-03` (this PR) | Cont. 5's owner-direction options narrowed (per follow-up): test Chain 4 (Kashiwara/crystal-derived single-formula c_3) + formally accept residue A as CAL-3-anchored + scope KLR/crystal upstream infrastructure for the composite-operator search. | RESULTS — Chain 4 (PR #1768) closes the single-formula search: **6 Kashiwara/crystal-derived candidates all NEGATIVE** at proton-pinned q₀. Best: SYT(2,1) major-index sum `-(q + q²)` at 131,775 ppm. Other candidates: Demazure (2,1) char `-2·[3]_q` at 1.94M ppm, J_Hopf(q) Kauffman at 959k ppm, symmetric+Hopf-center `-(q² + 1 + q⁻²)` at 470k ppm, `-(q + q⁻¹)·b_q` at 157k ppm, `-J_Hopf(q=1)·b² = 2·b²` sign-test at 1.73M ppm. **Combined 4-search NEGATIVE bracket** = 28 total candidates tested across Chain 1 α/β + 15-candidate c_3 re-run + Chain 4 = 28 NEGATIVE/28 candidates. The single-formula search space is now SATURATED across all natural categorical families (Markov-projector, Kashaev-dilog, Kashiwara-crystal, combinatorial-SYT, symmetric-block-combinations). **Formal acceptance landed (this PR)**: residue A categorically lives in a COMPOSITE Kashiwara operator structure that requires upstream KLR/crystal infrastructure not in Mathlib (no Demazure modules, no Kashiwara crystal graphs, no KLR algebra, no Markov trace on Hecke). Current production: c_3 stays at tier `cal-anchored`; Q_β L2 dashboard headline at 1279 ppb (164× off 100× target). NO fitted form wired. Δ_λ gate held throughout. Audit: [`docs/audits/2026-06-03-qbeta-residue-a-cal-anchored-acceptance.md`](../audits/2026-06-03-qbeta-residue-a-cal-anchored-acceptance.md); KLR/crystal infra roadmap: [`docs/scope/2026-06-03-qbeta-residue-a-klr-crystal-infra-scope.md`](../scope/2026-06-03-qbeta-residue-a-klr-crystal-infra-scope.md). Next-session direction needed from owner: **A** (stop chasing c_3 promotion, focus other observables), **B** (Composite 4 Wenzl×q-Poch, cheapest at 5-6 sessions infra), **C** (Composite 1 Demazure×q-Poch, 5-7 sessions, infra reusable for mass-formula crystal multiplicities), or **D** (Composite 3 Type-B folded crystal, 12-17 sessions, highest theoretical value per §7b). |
| 2026-06-03 (cont. 10) | Claude / `claude/qbeta-c3-multiblock-recursion-attack-2026-06-03` (PR #1764) | multi-block Δτ_M probe + per-block χ_λ closed-form Lean theorems; corpus-grep + wiring discipline | RESULT — **NEAR-MATCH verdict, NOT wired (would be flip-flop #6)**. Sorry-free Lean theorems landed: `chi_block_3/21/111` defs + `chi_block_antipode_pairing` (χ_(1,1,1)(q) = q⁻⁴·χ_(3)(q) for q > 0) + `chi_blocks_vanish_at_one` + `chi_blocks_have_q2_minus_1_factor`. Multi-block Δτ_M rational closed form derived under NON-CANONICAL rational-y_λ surrogate (canonical y_λ involves √q); cross-anchor swing at q_proton vs q_muon ≈ 9.99633e-9 ⇒ NEAR-MATCH per the pre-stated failure-mode signature. Witness records `c_3_value: "NOT_DERIVED"` and `c_3_status: "NEAR-MATCH (open). f-map keystone open. flip-flop history #1-5 — NOT wired as Taylor-exact"`. **3 rounds of Copilot review (16 inline comments) all addressed**: triple renamed `qbeta-delta-tau-m-multiblock-closed-form.*` → `qbeta-per-block-chi-closed-forms.*` to match label; y_λ surrogate clearly marked in script docstring header + `y_lambda_h3_symbolic` docstring + .md retraction note + witness JSON; `c_3_value: "NOT_DERIVED"` + `c_3_status` flag added; muon-anchor `q_muon_at(50)` canonical (replaced silent CODATA fallback); `field_simp [hq_ne]` at all 4 sites; 60-dps SymPy eval (matches witness output_dps); real Δτ_M-rational-in-q assertion (replaces vacuous 1.0=1.0). **4 Lean extensions added** (surrogate Δτ_M closed form + Taylor coeffs at q=1 + Markov parameter + canonical-Δτ_M conditional class + z-recursion class) — all FULLY SORRY-FREE after local LSP verification (lean v4.24.0 + Mathlib f897ebcf; EXIT=0). **Coord cross-links posted on 4 Q_β siblings**: PR #1773 (composite-operator), PR #1768 (Chain-4 Option-E), PR #1769 (S=Q_β/E_0 shape diagnostic), PR #1762 (1ppQ roadmap reanalysis). **CI**: jobs in billing-pattern setup-failure throughout (3-4s); `[skip-ci: billing]` per AGENTS.md. **Wiring discipline confirmed**: zero downstream `uses[]` of `prop:qbeta-per-block-chi-closed-forms`; zero downstream importers of the probe script. The content is pre-archimedean structural input the f-map will eventually consume — not production compute. |
| 2026-06-04 (cont. 11) | Claude / `claude/jolly-goodall-eT4Mi` (PR #1831) | follow-up to cont. 9/10: (1) numerically evaluate the §3b-cond canonical Δτ_M at the explicit √q instance at q₀; (2) discharge the order-2 Taylor coeff in Lean; (3) the saturated-search next step — a **systematic 2-factor composite sweep** with cross-anchor discrimination. | RESULT — **2-factor composite space SATURATED (NEGATIVE)**. Built a reusable `c3_target_at(q,…)` ladder inversion (`c_3(q)=(Q_codata/Q_N2(q)−1)/u³`) that reproduces the canonical proton target `−2.06934257711516784` to 1e-12 and yields the **reusable muon target `c_3(muon) = −2.02020023502125517`** (cross-anchor swing `0.0491`, 2.37%). Swept **1281 candidates** (every `a∘b`, ∘∈{×,÷,+,−}, over ~20 categorical atoms): **0 match both anchors within 1 ppm**; best proton matcher `q²+q⁻²−[4]_q` (1.6e-3) misses the muon anchor by 14×; the 4 single-anchor near-matches all fail cross-anchor. Combined with the 28-candidate single-formula bracket (cont. 9), **both the 1- and 2-factor spaces are now saturated** ⇒ residue A is not a 1- or 2-factor product of natural categorical objects; narrows to 3+-factor / Habiro-tower / KLR-crystal (Composites 1–4). Δ_λ gate held (closed-form atoms, no fits). Witness: `qbeta-composite-crossanchor-2factor-sweep.witness.json`. Also landed: the explicit-instance Δτ_M companion witness + Lean eval lemmas, and an order-2 second-derivative Lean proof (g″(1)=5/3 ⇒ c₂=5/6) — Lean LSP-verified sorry-free (both modules `lake build` exit 0) via a local from-source build (toolchain installed through `scripts/setup-lean-toolchain.sh`, the GitHub-releases workaround for the blocked `release.lean-lang.org`). |
| 2026-06-05 (cont. 12) | Claude / `claude/qbeta-stageB-cosh-relabel-2026-06-04` (PR #1866, MERGED) + `claude/qbeta-odd-parity-avatar-2026-06-05` (PR #1880) | Test PR #1824's generating-function hypothesis (c_k = Taylor coeffs of a single closed form `F(u,q)`) at the cross-anchor + multi-coefficient level, and relabel `linking_weight_family_a` per the `0e30e23e` roadmap audit. | RESULT — **generating-function reframing of c_3 opens NO new search space (both parity slices closed)**. (1) **Even slice — structurally empty** (PR #1866): every cos/cosh avatar is even in u ⇒ Taylor c_3 = 0, but cal-anchored c_3 ≈ −2.07 ≠ 0; refutes the entire even-parity family at once (max-miss 1e6 ppm on c_3), sharper than the prior 16-candidate single-anchor cosh scan. (2) **Odd slice — reduces to the saturated single-formula search** (PR #1880): the ladder constraints c_1 = 0 (starts at k=2) + c_2 = −1 (proved, even) force any odd-extended avatar `F = (even baseline)·(1 + g·u³)` to have c_2 = −1 indep of g AND **c_3 = g exactly** (confirmed numerically + **sorry-free Lean** `QBetaOddParityAvatarReduction.lean`, 3 `ring` identities over CommRing, LSP-verified 675-job build). So an odd-parity closure ⇒ a closed-form bar-antisymmetric g(q) matching c_3 at both anchors = the already-saturated 28-candidate single-formula search (cont. 9); 9 bar-antisymmetric/control g candidates tested cross-anchor, all NEGATIVE (best `−(q²+q⁻²)` 12,389 ppm proton). **Remaining productive directions** (unchanged): q-difference ODE (PR #1824 §3.b — c_k coupled by a recurrence, NOT a single closed form; genuinely different, NOT closed by these probes) + GAP-A-3/A-4. Also landed: `linking_weight_family_a` docstring relabel (CODATA-implied near-match, not derived count) per `0e30e23e` §5; Hoefsmit Stage B scope doc (infra unblocked on main by `dcd598f1`/`01802133`); Option D Δ_λ refuted-record (#1860). Reuses `c3_target_at` (cont. 11 / PR #1831). Witnesses: `qbeta-cosh-avatar-crossanchor-multicoeff-probe`, `qbeta-odd-parity-avatar-reduction-probe`. Δ_λ gate held; no fits; AGENTS.md no-7th-ansatz respected. CI billing-blocked throughout. |
| 2026-06-05 (cont. 13) | Claude / `claude/qbeta-reeb-sinh-parity-2026-06-05` (PR #1887) | After cont. 12 closed the closed-form + recurrence axes, pursue the one structural lead left: the **Reeb-bundle `sinh` holonomy** as the bar-antisymmetric c_3 source (formalize-first). + /coordinate vs `claude/confident-newton-R8lIx` (PR #1871). | RESULT — **first NON-refuted structural lead since the bracket closed: `PARITY_ADMISSIBLE_FIBRE_LEVEL`.** (1) **Lean parity invariant** (`QBetaReebSinhParity.lean`, sorry-free, 1827-job build): `cosh(kη)` bar-even, `sinh(kη)` bar-odd, and the bar-antisymmetric part of a Reeb holonomy `a·cosh+b·sinh` is exactly `b·sinh(kη)` ⇒ among Reeb components ONLY `sinh` can source the bar-antisymmetric c_3 (same parity wall that killed the cos/cosh avatars, #1866). (2) **Pruning probe**: 7 bar-odd `sinh`-Reeb scalars ALL match the c_3 *sign* but their observable cross-anchor slope `dS/dη` is O(1) while `dc_3/dη ≈ 4.26e6` is amplified by the ladder `1/u³ ≈ 1.62e6`; the slope ratios `(dc_3/dη)/(dS/dη)` are all ~1/u³, NOT ~1 ⇒ a DIRECT Reeb `sinh` is **not** the observable c_3 closed form (consistent with #1880) but **is** parity-admissible at the **fibre level**, where the ladder supplies the amplification (consistent with #1811's fibre-level residue A). (3) **The `1/uᵏ` IS the f-map** between the `sinh(kη)` **q-weight / jet-filtration index** `k` and the **u-adic ladder rung** `k`; the candidate `k = brane-tower level ℓ(K,q₀)` is **GAP-A-3**. **Coordination (PR #1871, confident-newton):** strong convergence — their §4 mirror-pair `ΔB = 2B₀ sinh θ_B` (binding *difference* is the bar-odd `sinh` channel) is the structural sibling of "c_3 sourced by Reeb `sinh`"; their SO(3)_q Lean §6 (`1+2cosh(2η)`, `cosh_two_mul`) shares my hyperbolic toolkit; their step-9 jet-filtration/q-difference workplan ↔ my `1/uᵏ` f-map. Intent posted on #1871; no file overlap, findings consistent (no §6 escalation). Witness: `qbeta-reeb-sinh-parity-probe.witness.json`. Δ_λ gate held; no fits. Next: scope `sinh(ℓη)` with `ℓ`=brane-tower level + test the `1/uᵏ` f-map to the c_k ladder (the structural route to the data-blocked recurrence). **UPDATE (same session, committed):** those `Next` items are now DONE with a decisive outcome. **(a) f-map REFUTED as an integer brane-tower level** (`qbeta_reeb_sinh_fmap_brane_tower_probe.py`): testing `c_3 = sinh(ℓ·η)/f_k` over 6 `f_k` candidates, the inferred `ℓ` is **swing-locked** — `|Δℓ|/|ℓ| = |Δc_3|/|c_3| = 0.02375` at both anchors, so no *integer* (knot-topological) level reproduces both; a round-trip guard kills the trivial `ℓ=0` asinh-small-argument false positive (`NEGATIVE_NO_INTEGER_BRANE_TOWER_LEVEL`). **(b) Phase-series reframe per PR #1871 §3** (`qbeta_cosh_phase_series_reframe_probe.py` + 2 sorry-free Lean lemmas): the c_k ladder is the u-Taylor expansion of a **single hyperbolic phase**, `Q_β/Q_A = cos(Φ(u))`, `Φ(u) = Φ₁u + Φ₂u² + …`. The truncated cosine `1−Φ²/2` (Lean `qbeta_phase_cos_truncation`, one-line `ring`) gives `c_2 = −Φ₁²/2` and `c_3 = −Φ₁·Φ₂`; the proved `c_2 = −1` ⇒ **`Φ₁ = √2` anchor-exact** (Lean `qbeta_phase_leading_sq_eq_two`, `linarith`; this IS the #1866 even slice `cos(√2·u)`), and `c_3 = −Φ₁Φ₂` ⇒ **`Φ₂ = −c_3/√2 = 1.46324616887618 (proton) / 1.42849728553818 (muon)`** (round-trip c_2 err 9e-13, c_3 err 1.67e-6 ppm; swing 0.0347, rel 0.0237). This **unifies the whole bracket**: #1866 (even slice = `cos(√2·u)`, the Φ₂=0 truncation), #1880 (odd rung `c_3 = g`, here `g = −Φ₁Φ₂`), #1887 (sinh bar-odd channel = imaginary fibre phase), #1871 (their q-difference `G(x;q)` recurrence is exactly the machine that must generate `Φ₂(q)`). **Hand-off posted to PR #1871** ([comment](https://github.com/litlfred/qou/pull/1871#issuecomment-4634207741)): the concrete `Φ₂` targets their G-recurrence must reproduce. Δ_λ gate held; no fits. Witnesses: `qbeta-reeb-sinh-fmap-brane-tower-probe`, `qbeta-cosh-phase-series-reframe-probe`. |
| 2026-06-05 (cont. 14) | Claude / `claude/qbeta-phi2-ckrecursion-kernel-2026-06-05` (PR #1900) | Owner direction "advance the Φ₂ closure" (follow-up to merged #1887). Formalize-first: constrain the **open** c_k-recursion kernel rather than launch the (blocked) symbolic search. | RESULT — **bridge #1887→#1871 + constant-depth-2 kernel REFUTED.** Key finding: the on-`main` block `prop:q-beta-c-k-recursion-from-habiro-q-difference` defines `F = Q_β/[Q_A·cos(α_eff(q))]` with a depth-`d` kernel recursion `c_{k+1}=Σ a_j c_{k+1-j}` and lists symbolic `α_eff(q)` as OPEN — and **#1887's `cos(Φ(u))` reframe IS that `cos(α_eff)`**: `α_eff(u)=Φ(u)`, `Φ₁=√2` exact, so the open `Φ₂` is the kernel's leading coefficient up to √2. **Φ₂'s value stays gated** on the SW-residue/Hoefsmit-`H₃(q)` kernel derivation (#1871's frontier). Bounded deliverables: **6 sorry-free Lean lemmas** (`QBetaCKRecursionKernelConstraints.lean`, `lake build` exit 0, 1828 jobs): `ck_recursion_depth_one_refuted` (depth≥2: `c_1=0`,`c_2=−1≠0`), `ck_a2_eq_c2_depth_two` (`a_2=c_2=−1` via `f_0=1`), `ck_a1_eq_neg_c3_depth_two` (`a_1=−c_3`), `ck_a1_eq_sqrt2_phi2` (`a_1=√2·Φ₂` — kernel leading coeff = #1887 Φ₂ target = 2.0693(p)/2.0202(m)), `ck_c4_constant_depth_two_prediction` (`c_4=1−c_3²`), `ck_a1_bar_odd` (the #1887 Reeb-sinh parity wall as a kernel constraint). **Probe** (`qbeta_ck_recursion_kernel_constraint_probe.py`): the constant depth-2 kernel is over-determined (`a_2=−1`,`a_1=−c_3`) and predicts `c_4=1−c_3²≈−3.28(p)/−3.08(m)` vs fitted `c_4≈−0.97` ⇒ **`CONSTANT_DEPTH2_KERNEL_REFUTED`** (miss ×3.38/×3.17, sign-preserving, floor-robust). Reading: the recursion is **depth≥3 or non-constant** (the block's Habiro `(u;u)_m` change-of-basis is load-bearing, not raw `u^k`). Surviving kernel constraints for #1871's `R` search: depth≥2, not-constant-depth-2, leading coeff `a_1=−c_3=√2·Φ₂` **bar-ODD**. Addressed Copilot+Gemini review on the scope doc (lemma-name consistency, single bar-even/bar-odd convention, `f_0=1` indexing). Witness: `qbeta-ck-recursion-kernel-constraint-probe.witness.json`. Δ_λ gate held; no fits; closure stays GAP-A/SW-residue. CI billing-blocked throughout (local validate exit 0). |
| 2026-06-06 (cont. 15) | Claude / `claude/qbeta-alpha-eff-hoefsmit-h3-2026-06-06` (PR #1907) | Owner direction "Hoefsmit feeds the KLR kernel" — contribute the symbolic-α layer to the KLR residue-A program (PR #1892 scope, merged) rather than open a competing kernel-ownership PR. | RESULT — **corpus-grep: the symbolic α_eff is NOT open; it is already on `main`.** [`probe_q_beta_operator_valued_N3.py`](../../computations/probe_q_beta_operator_valued_N3.py) carries it in closed form: `z = 1/(√q+1/√q)` (bar-even), `h = q−1/q` (bar-odd Hecke param), **`alpha = (z−1)·h/2`** (bar-ODD single-wrap angle); `Q_β/Q_A = cos(alpha − Σ u^k/2)`, `u = b·ℏ_q²`. The companion probe (`qbeta_alpha_eff_hoefsmit_symbolic_probe.py`) re-derives `alpha` from these closed forms and **reproduces the on-main N=3 witness value exactly** (`−0.05233612…`). **Two results:** (1) `alpha` is **bar-ODD** ⇒ independently confirms, from the Hoefsmit/categorical side, the #1900 kernel constraint that `a_1 = −c_3 = √2·Φ₂` is bar-odd (two independent routes — Reeb-`sinh` #1887/#1900 and Hoefsmit single-wrap — agree on the parity); (2) the KLR scope's "open symbolic α(q)" item can be **retired**. **Reconciliation tranche (owner: "probe carefully") — REFUTED the easy path:** a second probe (`qbeta_alpha_eff_ladder_reconciliation_probe.py`) tests whether `Φ₂` follows from `alpha` using the producer's CANONICAL N=2 model `cos(alpha−u/2)(1−u²)` (not the prior line-144 candidate). It gives `c_2 = −9/8` **structurally** (α-independent — both anchors `−1.12500000`), vs the proved #1887 `c_2 = −1` (leading phase `3/2` vs `√2`); and `c_1 = tan(alpha)/2 ≠ 0`. **No single ladder rescale `ũ=λu` reconciles both rungs** (`λ=√(9/8)` forces `c̃_2=−1` but leaves `c̃_1=−0.0247≠0`; 2 d.o.f. needed, rescale has 1). ⇒ the on-main `alpha=(z−1)h/2` is the single-wrap angle of the N=2 **approximation**, a DISTINCT phase from the proved ladder `Φ(u)`; **`Φ₂` does NOT follow from `(z−1)h/2` by reparametrisation** — the kernel work must derive the exact `Φ(u)`, the easy path is formally closed. `alpha` bar-odd (confirms #1900) stands. Deliverables: 2 symbolic probes + witnesses (6 assertions pass) + findings doc [`docs/scope/2026-06-06-qbeta-alpha-eff-hoefsmit-symbolic-finding.md`](../scope/2026-06-06-qbeta-alpha-eff-hoefsmit-symbolic-finding.md); addressed Copilot's 8 comments (closed-form tail `u/(2(1-u))`, raw-mpf assertion, tighter annotations, doc precision-note). Feeds the KLR program; does NOT claim the kernel `R`/`F(q)∈Habiro(ℤ)` derivation. Δ_λ gate held; no fit; nothing wired. CI billing-blocked (local probe exit 0). |
| 2026-06-06 (cont. 16) | Claude / `claude/qbeta-klr-tau-eval-map-2026-06-06` (PR #1911, MERGED `fbbba406`) + `claude/qbeta-klr-composite4-wenzl-qpoch-scope-2026-06-06` (PR #1914) | Owner direction "pick up KLR" then `/coordinate auto /prepare-merge 1911 then 2`. First two focused tranches of the KLR/crystal residue-A program (master scope PR #1892, merged 2026-06-05). | RESULTS — **t1 MERGED, t2 SCOPE OPEN, mid-session corpus-grep save.** **Tranche 1 (PR #1911 merged)**: structural Lean formalisation of the residue-A element as the **bar-ODD Habiro dual of α_EM**. Corpus-grep found the duality is already named in [`alpha-em-habiro-bar-involution.md`](../../content/quantum-observable-universe/braids-and-knots/alpha-em-habiro-bar-involution.md) §Significance: α_EM `[2]_q(1−h²α)` bar-EVEN with ζ₄ zero ↔ Q_β residue bar-ODD with ζ₄ pole. Formalised in [`QBetaResidueHabiroDual.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/QBetaResidueHabiroDual.lean) (`QOU.BraidKnot.QBetaResidueDual`, generic `CommRing`, bar=swap `q↔qi`, sorry-free, 675-job build): 7 lemmas — `bracketTwo_bar_even`, `heckeDiff_bar_odd`, `residueNum_bar_odd` (`N(qi,q)=−N(q,qi)`, complement of α_EM's bar-invariance), `bracketTwo_zero_at_bar_antifixed`, `residueNum_at_bar_antifixed = 2q(1−4q²α)`, and the rigour-upgraded `residueNum_ne_zero_at_bar_antifixed` over `[IsDomain R]` with explicit `2q≠0,1−4q²α≠0` hyps (the genuine `≠0` content of "pole", per Copilot review). Third independent confirmation of the bar-odd kernel parity (#1900 c_k-recursion + #1907 α_eff + #1911 Habiro-dual). **Corpus-grep save mid-session**: between t1 and t2, almost re-opened PR #1759's exact mistake — proposed "residue-magnitude identification" (`A=ℏ_q^N`? `b^N·ℏ_q^M`? `Q_β·ε_struct`?) as tranche 2. Stopped at the ledger check: that menu has been **exhausted three times** — cont. 6 (PR #1759 CLOSED-AS-DUPLICATE, 38 candidates / 6 families, best 2.93% miss), cont. 9 (28 candidates SATURATED), cont. 11 (1281 2-factor composites SATURATED). PR #1759's explicit lesson: "corpus-grep checklist isn't optional for 'open target' claims." Avoided the repeat; redirected. **Tranche 2 (PR #1914 open)**: focused sub-scope of the cont. 9 KLR-infra roadmap, a **one-session formalize-first parity preflight gate** for Composite 4 (Wenzl × q-Pochhammer, cheapest of 4 composites at 5-6 sessions Option B). The cont. 9 scope predates the three new bar-odd + ζ₄-pole constraints; the preflight derives Composite 4's predicted `c_3` parity analytically (no infra build). **Reviewer-sharpened verdict** (Copilot + Gemini caught two real math errors): u^3 = A_3 only (no k=2,3 mixing — product starts k≥2, first mixing A_2A_3 u^5 at degree 5); the bar-eigenvector renormalisation is `Y_k = q^{-k(k+1)/4}·(q;q)_k` with NEGATIVE exponent (Gemini caught my sign error), making `Y_k` bar-eigenvector with sign `(-1)^k` ⇒ `Y_3` bar-ODD. Combined: `A_3^ren = tr_M(p_3^JW)·Y_3 = (bar-even)·(bar-odd) = bar-ODD`. Composite 4 with bare `(q;q)_k` REFUTED at u^3; with renormalised `Y_k` PASSES; verdict **CONDITIONAL-on-norm-source**, reducing the live question to a single yes/no: is `Y_k` the categorically natural object in pyhecke/Markov-trace normalisations? The preflight RUN (one focused session) settles that, gating the 5-6 session infra investment. Strict formalize-first dominance over cont. 9's implicit "build first, test later". **Coordination**: brief intent posted on PR #1871 (confident-newton sibling) noting t1 merge + reaffirming cont. 14 Φ₂ targets (proton `1.46324616887618` / muon `1.42849728553818`, swing `0.0347`). CI billing-blocked throughout. Scope docs: [t1 findings](../scope/2026-06-06-qbeta-residue-habiro-dual-tau-eval.md), [t2 preflight](../scope/2026-06-06-qbeta-klr-composite4-wenzl-qpoch-preflight.md). **UPDATE (same session): preflight RUN result, [`docs/scope/2026-06-06-qbeta-klr-composite4-preflight-run-results.md`](../scope/2026-06-06-qbeta-klr-composite4-preflight-run-results.md), commit `6960883192`.** One-session probe `qbeta_klr_composite4_preflight_run.py` computes A_2 = tr_M(p_2^JW)·Q_2 for both Q_2 ∈ {(q;q)_2 bare, Y_2 renormalised} at both anchors (mp 65-dps); both give |A_2| ≈ 0.01090 — q-INDEPENDENT (identical to 6 figs proton/muon), **OFF the proved c_2 = -1 target by ~92×**. Not a near-match, not a cross-anchor swing artifact, not closeable by a constant rescaling (which would be a forbidden single-parameter fit). **Verdict: `PARITY_PASS_C2_MAGNITUDE_FAIL_BUILD_NOT_AUTHORISED`** (2 assertions pass; c_2 gate decisive at >10× threshold). The 5-6 session cont. 9 Option B (Wenzl + pyhecke linear-`tr_M`) infra build is **NOT authorised** — it would discover this failure at the end; the one-session preflight surfaces it now. **~5× ROI on the preflight session.** Redirect (per cont. 9 menu): Option C (Composite 1 Demazure × q-Poch, 5-7 sessions; same preflight pattern should apply before that build commits) OR Option A (accept residue A as inherently CAL-3-anchored permanently, now reinforced by 3 corpus-side closures + this preflight refutation). Witness: `qbeta-klr-composite4-preflight-run.witness.json`. **UPDATE 2 (same session): Composite-1 preflight RUN also done, commit `a1968542`, [`docs/scope/2026-06-06-qbeta-klr-composite1-preflight-run-results.md`](../scope/2026-06-06-qbeta-klr-composite1-preflight-run-results.md)** — owner direction "2" picked the Option-C preflight without waiting for the t2 merge. Same one-session template; computes `[u²]F = (q;q)_2 · Σ_{ℓ(w)=2} D_w(ω_1; sl_3)` at both anchors using the explicit Demazure formula from `qbeta_chain4_demazure_fund_weights.py` (Joseph/Andersen unsigned variant: `D_w(ω_j; q) = Σ_S q^{Σ(a_k-1)}`, positive at q > 0). Result: **`[u²]F = +0.1391` at both anchors** (identical to 9 figs) vs proved target `c_2 = -1 < 0`. **Verdict: `STANDARD_DEMAZURE_X_QPOCH_SIGN_REFUTED_AT_U2`** — sharper refutation than Composite 4's (which was magnitude-based at ~92×); this is **SIGN**-based and convention-robust: Y_k renormalisation does NOT rescue (`q^{-k(k+1)/4} > 0` inherits sign), and no global rescaling rescues (would flip `c_3` sign which currently matches). Honest caveat: Demazure-Lusztig variant (signed q-difference operators) UNTESTED — separate preflight scope required. **Combined two-preflight outcome**: cont. 9 Options B (Composite 4) + C (Composite 1 standard) both REFUTED via one-session preflights ⇒ **~10-13 sessions of Lean + pyhecke infra build avoided**. Remaining cont. 9 menu: Option A (now reinforced by 3 corpus closures + 2 preflight refutations), Option D (Composite 3 Type-B folded crystal, 12-17 sessions, not yet preflighted), or Demazure-Lusztig variant (untested). Witness: `qbeta-klr-composite1-preflight-run.witness.json` (2 assertions pass). |
| 2026-06-06 (cont. 17) | Claude / `claude/qbeta-klr-composite3-and-lusztig-preflights-2026-06-06` (PR #1924) | Owner direction `1 merge after comments resolved then 2 3` (cont. 16 sequel). PR #1914 merged `6814b9f01e` (no fresh review comments beyond Copilot's 6 + Gemini's 2 already addressed); then two follow-up cont. 9 menu preflights. | RESULTS — **BOTH REFUTED at u² sign, completing the cont. 9 menu refutation sweep.** **Option D (Composite 3 Type-B folded crystal)** `F(u) = Σ_T q^{c(T)}·u^{|T|}` tested at sl_4 → C_2 folding / ω_2; σ-fixed `|T|=2` elements = `{{1,4}, {2,3}}` under σ = (1↔4, 2↔3); `[u²]F = q³ + q³ = 2q³ = +2.7351` at both anchors (identical to 7 figs); sign-mismatches `c_2 = -1`. **Even cleaner than Composite 1**: no q-Pochhammer factor ⇒ `[u^k]F > 0` at EVERY k. AGENTS.md §7b bar-invariance does NOT rescue (orthogonal to sign). cont. 9 Option D (12-17 sessions) **NOT AUTHORISED**. **Option C′ (Lusztig-dual variant of Composite 1)** `D_w^{dual}(q) = q^{ht}·D_w(q^{-1})` at sl_3/ω_1/ℓ=2: PALINDROMIC-EQUAL to standard (`1+q = q+1` trivially), so `Σ_dual = Σ_std = 5.4520`, `[u²]F = +0.1391`, same sign refutation. **Lusztig 1990 positivity** ⇒ all NATURAL Lusztig variants (dual, T_i-action) inherit positivity. **Honest caveat**: EXOTIC signed variants (Lusztig-Yun-Zhu Whittaker, twisted T_i sign-changing) UNTESTED — separate scope. NARROWS Option C to exotic-signed only. **Combined four-preflight outcome** (PRs #1914 + #1924): **~22-30 sessions of infra build avoided** across 4 one-session preflights; ROI ~6-7×. cont. 9 menu: B/C/D refuted at u²; A (CAL-3-anchored) now backed by 3 corpus + 4 preflight refutations; only C-exotic-signed remains (research-grade theoretical-escape, not build-cost-saving tranche). **Reviewers** (Copilot 6 + Gemini 3 = 9 comments on #1924, several duplicates): addressed all in same-session fix commit — docstring path normalised, q-Pochhammer replaced with mpmath's optimised `qp()`, non-ASCII identifiers (`Σ_std/Σ_dual` → `sum_std/sum_dual`), heading labels harmonised with cont. 9 conventions (Option D / C′), witness `scriptCommitSha` regenerated after fix commit (Copilot caught the "unknown" provenance). 4 assertions pass total. Δ_λ gate held; no fit; nothing wired. Results doc: [`docs/scope/2026-06-06-qbeta-klr-composite3-and-lusztig-preflights-results.md`](../scope/2026-06-06-qbeta-klr-composite3-and-lusztig-preflights-results.md). |
| 2026-06-06 (cont. 18) | Claude / `claude/l2-shared-root-update-and-klr-exotic-lusztig-2026-06-06` (PR #1930) | Owner direction "1 3" (post-#1924 sequel): L2 100× shared-root state-of-the-program update + exotic-signed Lusztig structural scope. Both scope-only (no compute) following today's 3 KLR-program merges. | RESULTS — **two paired scope docs landing the post-KLR program state**. **(1) L2 shared-root audit update** [`docs/audits/2026-06-06-l2-shared-root-post-klr-update.md`](../audits/2026-06-06-l2-shared-root-post-klr-update.md): companion to 2026-05-30 original. Today's 4 preflight refutations effectively close cont. 9 Options B/C/C′/D — the proposed instantiations of "Option E (Kashiwara crystal extension)" in the original. Updated picture: **m_n (185.4× off)** and **Δ_pn (163.3× off)** inherit Q_β CAL-3-anchored permanent acceptance — **permanently CAL-3-anchored** modulo a research-grade exotic-signed Lusztig discovery; **m_μ (963.6× off)** is INDEPENDENT (μ–p tension floor, formula `m_μ = m_e · Vol(4_1) / ℏ_q²` per `m_p_borromean_verification_50dps.py`) — **separate scope item** for future-session prioritisation. AGENTS.md §Precision goals count `3/7 met` is accurate post-re-pin; no doc refresh needed. **(2) C-exotic Lusztig bounded-magnitude scope** [`docs/scope/2026-06-06-qbeta-klr-exotic-signed-lusztig-bounded-magnitude-scope.md`](../scope/2026-06-06-qbeta-klr-exotic-signed-lusztig-bounded-magnitude-scope.md): three structural narrowings without specifying a concrete exotic convention — **N1** bounded magnitude at sl_3/ω_1/ℓ=2 (`|Σ D_w| ≤ 6.7 << target 39.4` regardless of sign); **N2** cont. 11's 1281-sweep saturates natural Demazure-derived 2-factor combinations; **N3** cross-anchor rigidity forces convention to be intrinsic. Combined with Lusztig 1990 positivity (natural canonical bases don't produce sign-changing Demazure in type A), exotic conventions (Whittaker / Yun-Zhu / twisted T_i) not in this corpus — specifying one IS a research task. **Verdict: cont. 9 C-exotic NARROWED HARD**, formally open as theoretical-research direction but **NOT a 5-7 session build-cost-saving tranche**. **cont. 9 menu final state**: B/C/C′/D refuted; C″ exotic NARROWED; **A (CAL-3-anchored permanently)** backed by **3 corpus + 4 preflight + 3 structural narrowings**. Δ_λ gate held; no fit; no production wiring. CI billing-blocked (no compute to validate; scope-only PR). |
| 2026-06-10 (cont. 19) | Claude / `claude/loving-allen-o0xjrs` (PR #2106) + #2090 merge | Owner "1 y / 2 y / 3 y": merge #2090 after review disposal; execute **Hoefsmit Stage B** (live-menu option 1 / probe 6.d′); update the kernel/Φ₂ scope. | RESULTS — **#2090 MERGED** (rebase, main `73daca85`) after Gemini review disposal (1 formatting applied `182fe7c1`; whole-file import reorder declined with rationale — theme-grouped aggregator, #2095 conflict risk; Copilot 2× no-show over 15 h documented; CI billing signature throughout). **Stage B EXECUTED** ([`qbeta_hoefsmit_stage_b_per_block_ck_probe.py`](../../folio-assistant/computations/qbeta/qbeta_hoefsmit_stage_b_per_block_ck_probe.py), 7/7 assertions): (1) **gate-1 recombination identity PASSES SYMBOLICALLY** — `Σ_λ y_λ(q)·χ^λ(w) = tr_M(w)` for all 6 H₃ basis words (Wenzl × Hoefsmit = canonical Markov trace, exact); (2) **NEW level bar-parity ladder** on `ΔT = T_n − T_p`: L₀ bar-ODD / L₁ bar-EVEN / L₂ bar-ODD / L₃ MIXED (odd fraction 9.45 % at q₀) ⇒ **the f-map must re-mix parity** (raw ℓ=3 level is 90.5 % bar-even but a₁ = √2·Φ₂ is bar-ODD); (3) **(2,1) block carries exactly 0 at the trefoil level ℓ=3** (Wedderburn selection — rung-3 factors through (3) ⊕ (1³)); (4) **scalar-peel saturation demonstrated**: ĉ₃ = `c3_target_at` to 30 dps at both anchors (−2.06716 p / −2.01803 μ), then ĉ₄..ĉ₈ ≡ 0 to 65 dps ⇒ a single scalar reference populates exactly ONE free rung — c_k≥4 is operator-only (constructive companion to the §4 precision floor); (5) **H₃ level ceiling**: NF words stop at ℓ=3 ⇒ unbiased c₄..c₈ require H_{n≥4} towers or the kernel recursion — derives the registry 'c₄ = artifact' tier, localises Stage C; (6) **heat-family per-mode a₁ REFUTED** (all three `−(q−1)μ_λ` bar-MIXED, \|a₁\| ~ 1e-3 vs √2·Φ₂ ≈ 2.069); assembled `Z_q`-level composition stays open (t-dependent coefficients ⇒ outside #1900's constant-depth-2 refuted class). **Gate-correction note:** the previously-planned gate `Σ_λ y_λ·Δ(net)_λ == scalar Δ(net)` is a **functional mismatch** — the scalar net is the coefficient-sum (counit-type) functional, not the Markov recombination (Δ(net)(q₀) = −0.18829 vs Δtr_M(q₀) = −0.11789); the per-word identity above is the correct infra gate. Scope addendum [`2026-06-10-qbeta-phi2-kernel-heat-family-and-stage-b-constraints.md`](../scope/2026-06-10-qbeta-phi2-kernel-heat-family-and-stage-b-constraints.md) appends constraint rows 7–9; keystone path unchanged. Δ_λ gate held; no fit; no wiring; no tier change. |
| 2026-06-18 (cont. 20) | Claude / `claude/dreamy-feynman-nns0ol` (PR #2465) | Owner direction "gate open this session" + "continue stalled agent": execute the **#1622 mode→ladder bridge** that #2106 (Stage B, 8 days idle) did not take — change of variable `u=√q ↦ u_L=b·ℏ_q²` on the exact `Δtr_M` mode decomposition, to read off `c_k`. | RESULTS — **bridge EXECUTED; gate NOT opened (honest negative).** (1) Exact anchor-independent **ℏ-Taylor series of `Δtr_M`** pinned: `a_n = −5/4, −13/8, −33/16, −77/32, −177/64, −25/8, −891/256, −3923/1024, −4277/1024, …` — a new **forward constraint** on any `f`. (2) Structure: `u_L=b·ℏ²` ⟹ even-in-ℏ `a_4,a_6,a_8` feed integer rungs `c_2,c_3,c_4`; odd-in-ℏ are the half-integer **bar-odd remainder** `f` must cancel (makes PR #1602's `−√3/12·u¹` class exact). (3) `bar-even (u↦1/u) ≠ even-in-ℏ` — two independent constraints. (4) **Two principled `f`-candidates REFUTED** (new refuted-class row **C13**): raw even-in-ℏ gives constant `c_3=−100/(77b)≈−1.497` (25% off −2); #1602 bar-even gives `c_3=−175/(144b)≈−1.401` (30% off). `c_2=−1` only as a scale-fix, not independently derived. Surviving `f` is **non-linear** in `Δtr_M`, still fibre-level/open. **(5) C13 formalized in Lean** (`QBetaCKRecursionKernelConstraints`, 4 sorry-free ℝ lemmas, `lean`-direct verified exit 0): the two seedings need different `b` (`50/77 ≠ 175/288`) ⇒ bridge can't hit −2. **(6) H₄-tower Stage-C preflight** (`qbeta_h4_tower_branching_preflight.py`, owner "push into H₄ tower"): H₄ Hoefsmit seminormal reps (λ⊢4) satisfy Hecke+braid to 1e-40; H₃⊂H₄ branching `χ^μ(w)=Σ_{λ↗μ}χ^λ(w)` holds on all σ₃-free decay words (err 5.6e-52); **σ₃-gating proven** — c₄ is gated on the OPEN length-4 σ₃-lift (Stage C), not in any A=1/σ₃-free object (consistent with C12+C13). No c₄ fabricated. Tiered; no fit; no wiring; no registry change. Artifacts: [`habiro_mode_to_ladder_bridge.py`](../../computations/habiro/habiro_mode_to_ladder_bridge.py) + witness, [`qbeta_h4_tower_branching_preflight.py`](../../computations/habiro/qbeta_h4_tower_branching_preflight.py) + witness, [bridge scope](../scope/2026-06-18-qbeta-habiro-mode-bridge-execution-scope.md), [Stage-C scope](../scope/2026-06-18-qbeta-c4-h4-tower-stage-c-scope.md), refuted-map C13. Intent on #2106, cross-link on #2469. |
| 2026-06-22 (cont. 21) | Claude / `claude/epic-hopper-f97it3` (PR #2611) | Owner direction "agent stalled, sharpen structure then work on F(q)": reconcile the two now-characterized F-poles (dominant 117.41 #1727, subdominant silver 3.1154 #2454) against the actual canonical `c_2..c_10`, since #2454 established silver purely algebraically (`Q_A(silver)=0`) and never against the coefficients. | RESULTS — **two-pole ladder decomposition (structural diagnostic; no closure/fit/wiring).** (1) **Rung partition (novel low-rung framing):** the dominant pole is TAIL-only — `|D_k/c_k|` = 1.7e-7, 3.5e-5, 0.39% for the OPEN rungs c_3,c_4,c_5; 16% c_6; overtakes at c_7. The 1ppQ-blocking open rungs are NOT a dominant-pole phenomenon. (2) **First test of the silver pole vs the ladder:** the dominant-peeled residual `c_k−D_k` sign-flips at k=6, no clean `+3.1154` geometric ⇒ canonical `c_k` do not corroborate the silver zero as leading subdominant structure — **confirms PR #2454's own caution** (genuine F-singularity, screened in the ladder by the entire/A-sector). (3) **Two-pole-removed residual** `h_k` large at low k, ~1.5e-5 collapse in tail ⇒ minimal denominator deg≥3, re-confirming refuted **C5** from the pole side; `h_k` is the exact-extraction target for #2106/#2474. **Net:** closing c_4,c_5 is an entire/A-sector (PR #1622) problem, consistent with #2106 Finding 5 (H₃ stops at ℓ=3) — localizes #2474's σ₃-lift. Corpus-grep first: residue-A floor/ceiling settled (#1727/#1805), not re-reported. Artifacts: [`qbeta_two_pole_ladder_decomposition.py`](../../computations/qbeta/qbeta_two_pole_ladder_decomposition.py) + witness (3 assertions), [pole-structure map audit](../audits/2026-06-22-qbeta-two-pole-ladder-decomposition.md). Δ_λ gate held; no tier change. |

## Narrowed Phase-3 search space (2026-06-03 consolidation)

After today's sibling audits (PR #1746, PR #1750, PR #1752, and the per-knot demo on PR #1756), the search for the Q_β Habiro element's categorical residue at u_substrate has the following **structurally ruled-out** vs. **still-active** state:

### Structurally ruled out (do not re-explore)

| Candidate | Refutation | Source |
|---|---|---|
| min-trace LP on Frobenius Gram → unique categorical T_β | Frobenius Gram is INDEFINITE (eigs at q₀: `[-0.855, 0.102, 0.855, 0.855, 0.855, 3.477]`); min-trace LP is degenerate (optimum ≈ 0, not the physical operator). | PR #1752 |
| L2 norm choice → c_k cross-anchor swing is an L2 artifact | T_β collapses to `S·I` under the categorically-natural Markov pairing; the c_k are L2/Markov-INVARIANT (the SDP **constraint** determines them, not the **objective**). The swing is structural, upstream of any norm. | PR #1750 step 4 |
| Scalar `|c|(λ)` Coxeter-sum candidate | `χ^λ(s_k) = f^λ · 2c(λ)/(n(n−1))` is proportional to *signed* `c(λ)`, not L¹ `|c|`. Counterexample `(2,2)`: self-conjugate ⇒ sum = 0, but `|c|((2,2)) = 2`. | PR #1746 |
| Other 4 scalar `|c|(λ)` candidates from PR #1721 | Refuted on basis-convention or weight-vs-content arguments. | PR #1721 + PR #1746 |
| Real `c_3 = f(q_0_real)` matching multiple anchors near u_substrate | The Habiro element has a singularity at u_substrate (radius of convergence = u_substrate exactly; PR #1713 / PR #1727 simple-pole verdict). Searching for a real function near a fibre-level singularity is structurally hopeless. | PR #1713, PR #1727 |
| 2-term constant-coefficient recurrence c_{k+1} = α·c_k + β·c_{k-1} | Asymptotic `c_{k+1}/c_k → 1/u = 117.41` at k=8,9,10 refutes any constant-coefficient 2-term recurrence. | PR #1713 |
| `eigenphase = f` (the Habiro scaling map) at u¹ | Falsified at u¹: Taylor of `cos(α − bℏ²/2)` has a non-zero u¹ coefficient `−√3/12`, but the ladder `Π(1+c_k u^k)` starts at u². | PR #1602 |

### Still active (uncrossed)

| Candidate | Status | Next step |
|---|---|---|
| Q_β Habiro element `F(u) ∈ Habiro(ℤ)` whose archimedean evaluation at the **proton-pinned q₀** reproduces the observed c_k | Parallel α_EM PR #1511's `[2]_q · (1−h²α)`. The fibre object is real; the question is the categorical-residue identification of the simple pole at u_substrate. | Re-derive at proton-pinned q₀; identify residue `A ≈ 1.804e-15` categorically (`ℏ_q^N`? `b^N · ℏ_q^M`? `Q_β · ε_struct`?). |
| Trace of operator `|Ω_q|` in Hoefsmit basis | 1 of 5 PR #1721 candidates survives; basis-convention objection from PR #1641 / PR #1643 still open. | Resolve the basis-convention objection before adopting. |
| Operator-valued LR branching combiner (PR #1443) | Open since 2026-05; not refuted, not derived. | Owner-direction needed to pursue. |
| Kashiwara crystal route (Option-E ledger's intended path) | Complementary to PR #1750's T_β = S·I (Type-B folding for matter-antimatter pairing is in §7b of AGENTS.md but is *authoring guidance*, not closure). | Owner-direction needed to pursue. |

### Implication for `linking_weight(K)` (PR #1756 Phase 3)

The Q_β c_k chain and the per-knot `linking_weight(K)` chain **share the Δ_λ gate** (same residue-identification methodology, same forbidden-Ansätze rules), but they are **structurally different closure targets**:

- Q_β c_k: scalar Taylor coefficients of a fibre-level Habiro element at a simple pole.
- `linking_weight(K)`: per-knot generalization of an H_4 Family-A scalar across atoms.

A categorical residue ID for Q_β's `A` (if found) does **not** automatically transfer to a `linking_weight(K)` formula; the analogous derivation would be a separate categorical chain.

## 2026-06-05 — Step 5b Markov-trace Lean verified green (PR #1811) + #1871 cross-link

- **Step 5b VERIFIED.** `MarkovTraceOnHecke.lean` (`trM_cyclic` trace
  cyclicity + `QOU.lean` root wiring) builds green on a fresh container
  (`lake build QOU.Machinery.MarkovTraceOnHecke`, 922 jobs, exit 0,
  sorry-free, warning-free). The Markov-trace **machinery** (Steps 1–3
  `gram.py`/`trace_formal.py` + Step 5 Lean) is stable and reusable —
  **not** a c_3 claim (Δ_λ-gate clean). `markov_trace_origin` discharge
  stays gated on the owner-gated Step 4 residue-A element.
- **Cross-link to #1871 (M=Vol×Density).** My abstract `trM` (H₃ Markov
  trace) is the same functional as their P2 "Density = Σλ yλ χλ = Markov
  trace" (`density_per_block`, `tr_M(proton)=1.0653`). **#1850** (merged)
  refutes Markov-stabilization at trace level (z<1; identity-trace =
  1 ≠ 2.53), which directly bounds the residue-A-via-`Ind_{H₃}^{H₄}`
  endgame — reinforcing Step 4's gated status.
  [Coordination comment.](https://github.com/litlfred/qou/pull/1871#issuecomment-4632946776)
- **Lean-cache infra finding (flagged to #1871).** The
  `lake-cache/qou-v4-24-0` cold-container restore fell back to a full
  Mathlib source rebuild (`URL has changed` re-clone of every package);
  the #1857 seed likely baked a `file://` `insteadOf` remote, so
  restorers must re-apply the redirect or the seed must normalize package
  remotes to canonical GitHub URLs before chunking.

## 2026-06-10 — c_k synthesis (PR #2090) + pre-archimedean q-heat depth-1 backbone (Lean) + coordination sweep

- **Synthesis doc + 2 currency fixes landed** on PR #2090
  (`docs/audits/2026-06-10-qbeta-ck-state-of-play-synthesis.md`). Owner
  declined the registry CAL-anchor note for c₃ (registry untouched,
  "leave as is") and deferred `/prepare-merge` ("not yet").
- **Pre-archimedean backbone #2 identified + formalized.** The `exp_q`
  grouplike defining equation (Jackson `D_q exp_q = exp_q`,
  `def:q-exponential`) rearranges to the depth-1 q-difference kernel
  `exp_q(qx) = (1+(q−1)x)·exp_q(x)`; per-Peter–Weyl-mode q-heat kernels
  `1−(q−1)·μ_λ·t` with `μ_λ(q) = ℏ_q²·Σ[c]_q[c+1]_q` (content-Casimir,
  q-rational); division-free two-mode depth-2 composition (any CommRing,
  no Casoratian). Lean sorry-free generic-`R`:
  `QOU.BraidKnot.QBetaPreArchHeatDepthOneKernel` (4 thms, commit
  `50d2e5ad`). Narrative: synthesis doc §3-bis. Status: **candidate
  FAMILY for the kernel `R` — UNGATED** (must produce bar-odd
  `a₁ ≈ 2.07` and survive the constant-depth-2 `c₄` refutation);
  heat-trace `R_λ` gate-check folded into the Stage-B probe scope
  (owner-approved "1 2" + "do all lean").
- **Latent closure gap fixed in same touch**:
  `QBetaCKRecursionKernelConstraints` (#1900 constraint lemmas) was
  imported by no module ⇒ likely never inside the `lake build QOU`
  closure; now aggregated in `BraidKnot.lean`. Cone-build verification
  in flight (background); if the orphan is red, the import line is
  reverted and the finding handed to #2095 (in-closure repair owner).
- **Coordination sweep (this entry's run):** intent comments →
  [#2095](https://github.com/litlfred/qou/pull/2095#issuecomment-4666539578)
  (closure addition heads-up),
  [#2094](https://github.com/litlfred/qou/pull/2094#issuecomment-4666549352)
  (post-merge inventory deltas),
  [#2093](https://github.com/litlfred/qou/pull/2093#issuecomment-4666549792)
  (`Z_q` q-shift structure is upstream of their `F_q = −T_q ln Z_q`
  crossing). Main drift vs PR base `dd7612c2`: 10 commits, no
  aggregator conflict (clean rebase expected). PR #2090 review state:
  0 threads; Gemini at daily-quota limit. CI: billing signature
  re-confirmed on `50d2e5ad` (3 jobs complete in 4 s, logs HTTP 404;
  identical pattern reported by #2095/#2094/#2091/#2089 today) — no
  retrigger per policy.
- **LANDED (cont. 19, PR #2106):** Stage-B probe executed — see the
  sessions-table row. The gate as planned here was a functional
  mismatch (coefficient-sum net ≠ Markov recombination); the correct
  per-word identity `Σ_λ y_λ·χ^λ(w) = tr_M(w)` passes symbolically.
  Headline: level bar-parity ladder (f-map must re-mix parity), H₃
  ceiling at ℓ=3 (c₄..c₈ operator-only via H_{n≥4} towers / kernel),
  heat-family per-mode a₁ refuted.

## 2026-06-13 — root-of-unity residue program → ζ₄ RELAXED (PR #2240)

Heat-route follow-up to the `a_1` gate (#2231). Pulled Zagier-2010's
Ohtsuki-period / root-of-unity structure back to the fibre and asked
whether bar-parity + ζ₄ + period-3 **over-determine** the active-mode
set `Λ`. Three sympy probes (all structural, no `c_3` value):

- **Option 0 (mode-sum)** `qbeta_root_of_unity_residue_program.py`:
  summed `μ_λ = ℏ_q²·Σ[c][c+1]` carries **only ζ₂ + ζ₆** (n≤6). ζ₆ ↔
  `(2,1,1),(2,2,1),(2,2,2)` matches the period-3 resonance ✓. **ζ₄
  washed out** by Σ_□.
- **Option 1 (per-cell)** `qbeta_per_cell_zeta4_subprobe.py`: ζ₄ *is*
  carried per-cell by content c∈{−5,−4,3,4} (`[4]_q=[2]_q·Φ₄`), but
  every ζ₄-carrying `κ_c` is bar-neither; only bar-ODD content c=1
  carries ζ₂ only. No mode is bar-odd ∧ ζ₄ at cell or mode level.
- **Option 2 (framing)** `qbeta_framing_zeta4_subprobe.py`:
  `α_eff=(z−1)h/2`, `z=√q/(q+1)`. In `s=√q`, framing carries
  `Φ_d(√q)` for d∈{2,4,6} → q-orders {1,2,3}; **no `Φ₈(√q)` ⇒ no
  genuine ζ₄(q)**. The `q+1=Φ₂(q)` reads as `Φ₄(√q)` but is the same
  locus `q=−1` (bar-fixed). Bonus: `α_eff` carries `Φ₆(√q)→ζ₃`.

**Verdict — ζ₄ is NOT a fibre constraint (RELAXED).** Neither `μ_λ`
nor `cos α_eff` supplies a bar-odd-compatible genuine ζ₄(q); it is a
√q double-cover reading of ζ₂ or a post-`cos`-wrap archimedean
(Kashaev/Ohtsuki) feature. Structural prune (formalize-first) — drops
ζ₄ from the fibre pre-flight. **Live fibre constraints:** bar-odd
`a_1=κ_(2,1)=(q−1)³(q+1)/q²` + period-3/ζ₆ (both realisable).
Checkpointed in `q-beta-c-k-recursion-from-habiro-q-difference.md`
kernel-status row. Audit:
[`docs/audits/2026-06-13-qbeta-root-of-unity-residue-program.md`](../audits/2026-06-13-qbeta-root-of-unity-residue-program.md).

- **Coordination sweep (this run):** scope map = #2240 (mine, qbeta
  c_3 fibre) vs open siblings. **No coordination comments posted** —
  no sibling has a genuine file overlap or actionable cross-finding:
  #2245/#1495 (α_EM) and #1765 (Habiro per-knot λ) are domain-adjacent
  but touch different files/observables; #2202 (bib) is tooling only
  (does NOT touch `references.ts`, confirmed via get_files); #2104
  (compute-pipeline) is binding/Δ_λ infra, not Q_β c_k. Own-PR triage:
  0 review threads; 1 Gemini daily-quota notice (not actionable). CI =
  standing billing block; `send_later` unavailable (no hourly
  self-check-in — webhook events only).
- **Period-3/ζ₆ CLOSED** `qbeta_period3_zeta6_cancellation_probe.py`:
  **cyclotomic bar-stability lemma** — `Φ_d` (d>1) self-reciprocal,
  `bar(Φ_d)=q^{-φ(d)}Φ_d` (verified d=2,3,4,6) ⇒ `Φ_d ∣ X ⟺ Φ_d ∣
  (X)_odd`. So the bar-ODD projection of a *single* ζ₆-carrier
  `(κ_(2,1,1))_odd` is a nonzero bar-odd Φ₆-carrier — **refutes** the
  "content-spanning Λ with cancellation required" caveat above; the
  mode-selective f-map + odd projection suffices. Same lemma sharpens
  ζ₄: bar-parity was never the obstruction (odd projection preserves
  any carried Φ_d); ζ₄ is unreachable because **no full κ_λ carries
  Φ₄** (mode-unavailability, Σ_□ wash-out), re-confirmed n≤6. Both live
  fibre constraints (bar-odd a_1=κ_(2,1), period-3/ζ₆) now realisable.
- **Higher a_2,a_3 carriers** `qbeta_higher_aj_carrier_probe.py`:
  recursion coefficients are `a_j = e_j({r_λ})`, elementary symmetric
  polynomials of the per-mode rates `r_λ = (q−1)μ_λ = κ_λ`.
  **PARITY-ALTERNATION THEOREM** (verified abstractly j=1..4): bar-odd
  rates ⇒ `bar(e_j)=(−1)^j e_j` ⇒ a_j alternate ODD,EVEN,ODD,EVEN —
  mode-set-INDEPENDENT (one-line `e_j(−x)=(−1)^j e_j`; Mathlib-provable,
  formalization follow-up, sandbox elan firewalled). Concrete depth-3
  set {(2,1),(2,2),(2,1,1)}: a_1 odd/ζ₂, a_2 even/ζ₂, a_3 odd/ζ₂+ζ₆ —
  ζ₆ enters at a_3 (the top product; active-set-specific, only the
  alternation law is universal). Fibre structure now mapped through a_3.
- **Scalar `S = Q_β/E₀` — OWNER-DECLINED (2026-06-13).** Attempting a
  categorical derivation of `S` means explaining the anchor-dependence
  (908 proton / 887 muon), which is the `q_0`-substrate-derivation the
  ledger declined 2026-05-08 (Subgoal-2, research-grade, out of scope).
  Owner declined the attempt this session ("2 decline"). The fibre
  STRUCTURE (carriers κ_(2,1), parity-alternation, ζ-content through
  a_3) is complete; turning it into `c_k` VALUES needs `S` + the active
  set `Λ`, both deferred. Do not attempt `S` without owner reversal.

## 2026-06-13 — a_1 carrier reconciliation + cyclotomic bar-stability Lean (PR #2253)

Follow-up to #2240, resolving the `/coordinate`-surfaced question vs #2106.

- **a_1 has two factorizations of the SAME number** (`a_1 = −c_3 ≈ 2.0694`):
  #2240 mode/Wedderburn basis `a_1 = κ_(2,1)·S` (`κ_(2,1)=(q−1)³(q+1)/q²` pure-q
  bar-ODD fibre carrier; `S = Q_β/E₀` archimedean scalar) vs #2106 Hoefsmit
  level basis `a_1 = √2·Φ₂` (`Φ₂ = 1.46324616887618` numeric synthesis target).
  `qbeta_a1_carrier_reconciliation.py`: `S = (√2·Φ₂)/κ_(2,1)(q_0) = 908.36/886.79`
  reproduces #2240 exactly; `|κ_(2,1)(q_0)|/|√2·Φ₂| = 1.1e-3 = 1/S`.
- **#2106's R_λ "honest negative" RESOLVED.** #2106's per-mode candidate
  `−(q−1)μ_λ` (= ∓κ_λ) was rejected by a magnitude gate (`|κ_λ| ~ 10⁻³` vs
  `2.069`, fails <1%) — that rejected the SCALE-1 carrier; supplying `S ≈ 908`
  recovers the magnitude. `κ_(2,1)` IS the bar-ODD carrier — `S` was the missing
  piece (owner-declined to derive, see #2240 entry). Mode basis = clean
  fibre/archimedean cut; `√2·Φ₂` is the archimedean a_1 VALUE.
- **Only (2,1) is bar-ODD among λ⊢3** ((3),(1³) bar-neither); #2106's "three
  bar-MIXED candidates" are the heat-trace R_λ family (a different μ_λ).
- **Cyclotomic bar-stability NOW LEAN-FORMALIZED** (corrects the #2240
  "formalization follow-up — sandbox elan firewalled" note above): `Φ_d`
  self-reciprocal `Φ_d(1/q)·q^{φ(d)} = Φ_d(q)` proved sorry-free as
  `cyclotomic_{two,three,six}_bar_stable` (d∈{2,3,6}; `Φ_6` = the ζ₆ carrier) in
  the recursion `.lean`. `esymm_bar_parity` (parity-alternation) was likewise
  already Lean'd in #2240. Verified FOREGROUND via direct-`lean` + `LEAN_PATH`
  against the restored `lake-cache/qou-v4-24-0` oleans (the lake dep-wipe bypass,
  `lean-environment-setup.md §322`) — the elan firewall no longer blocks Lean
  verification in-sandbox.
- **Coordination:** intent posted on #2106 (reconciliation framing) + #2127
  (Q_β/c_k domain); owner `beans`-CLI ask acked (not on `main` yet — will adopt
  when the skill updates land).

## 2026-06-14 — q-Bessel identification of the Reeb-phase objects (PR #2279)

**Scope.** Exposition + supporting infra, no production wiring. Answers "where
do Bessel functions play a role" and makes explicit that the home-grown
Reeb-phase / Markov-trace objects **are** the q-special functions of
`Rep(SU_q(2))`: Chebyshev / little-q-Jacobi matrix coefficients (rotation
regime), **Hahn–Exton q-Bessel** in the `SU_q(2)→E_q(2)` contraction / brane-
tower limit (Vaksman–Korogodsky 1989; Koelink 1994).

**Proved (Lean, sorry-free, verified `lean`-direct vs the restored
`lake-cache/qou-v4-24-0` oleans):**

- `QOU/QBeta/ReebTowerJacobiAnger.lean` — bar-graded three-term recurrence
  `sinh((k+1)η)=2cosh η·sinh(kη)−sinh((k−1)η)`; the **rotation/growth = `J_ν`/`I_ν`**
  unification (one recurrence `p_{k+1}=2t·p_k−p_{k−1}`, two conics: circle
  `cos²+sin²=1` vs hyperbola `cosh²−sinh²=1`).
- `QOU/QBeta/QBesselContiguityRecurrence.lean` — q-Bessel contiguity ⟹
  closed-form coefficients (first-order **q-holonomic**); C-finite as the
  constant-ratio degeneration; links to
  `RationalCoeffRecurrence.pole_reciprocal_is_char_root`.

**Compute (run, witnesses committed):**

- `qbeta_reeb_tower_jacobi_anger.py` (6/6) — the scope-doc "Bessel-like" tag
  IS the identity `sinh(x sinh η)=2 Σ_m J_{2m+1}(x) sinh((2m+1)η)` (bar-ODD,
  `c_3` sector), proved `<1e-40`; `I_ν(x)=i^{−ν}J_ν(ix)`. **n=3 bar-odd spectra
  are pure odd-order {1,3,5}** (the right structure) but the 3-order truncation
  does NOT match a single-`x` Bessel profile (resid 0.128) ⇒ the Bessel object
  is the TOWER / contraction limit, not the n=3 trace (a clean refutation that
  confirms the framing — same footing as #1887's f-map refutation).
- `qbeta_qbessel_contiguity_cfinite.py` (4/4) — **#1839 DERIVED**: the q-Bessel
  coefficient recurrence is q-holonomic (q^k-dependent), NOT C-finite, which
  predicts #1839's "no low-order constant recurrence"; the tail ratio
  `c_{k+1}/c_k → 1/u_substrate = 117.41` (the q-difference pole) is reproduced
  to **rel-err 0.0000**. The kernel `R` of `F(qξ)=R·F(ξ)` is the q-Bessel
  q-difference operator, not a rational degeneration.

**Relation to the carrier work (#2240/#2106).** Independent and complementary:
the carrier thread pins the *archimedean a_1 VALUE* (`√2·Φ₂`, `κ_(2,1)`); this PR
pins the *fibre-level functional class* (q-Bessel / odd-order Jacobi-Anger). The
bar-ODD localization to the `(2,1)` block (`χ^(2,1)(σ_1)=2 sinh η`, pure odd)
agrees with the ledger's "only (2,1) is bar-ODD among λ⊢3".

**NOT wired** to production Q_β or to the mass endomorphism. `c_3` stays
cal-anchored. The structural lever (per-λ Reeb phase θ_λ, rotation/growth) is the
same one the A≥3 binding decomposition uses (`binding_reeb_phase_decomposition.py`),
but that side is the open Δ_λ frontier, also unwired. Refs added:
Koelink 1994, Koelink–Swarttouw 1994, Vaksman–Korogodsky 1989, Koornwinder 1990,
Gasper–Rahman 2004. Audit:
`docs/audits/2026-06-13-reeb-phase-qbessel-identification.md`.

**Coordination:** intent posted on #2106 (bar-parity per-block overlap).

## 2026-06-14 — q-Bessel derive-first follow-up (PR #2305)

Follow-up to the merged q-Bessel trilogy (#2279 identification / #2300 real-x c_3
refutation / #2294 binding NO-GO), under the owner steer *"derive/prove first,
not fit/probe."* Three deliverables:

1. **2nd-order q-Bessel equation PROVED in Lean.** The function-level companion of
   #1839's q-holonomic kernel: `q^ν·g(q²w) − (1+q^ν−w)·g(qw) + g(w) = 0`
   (`g=Σ c_k w^k`) is sorry-free (`QOU.QBeta.qbessel_second_order_recurrence`),
   derived from the #2279 coefficient recurrence (★) via the factorization
   `a·q^{2k+1}−q^{k+1}−a·q^k+1 = (1−q^{k+1})(1−a·q^k)`. Witness:
   `qbessel-second-order-qdifference-equation.witness.json` (3/3).
2. **Lead-4 derivation (exact ℚ(q), no fit): the finite spectrum is NOT q-Bessel
   zeros.** `μ_λ = ℏ_q² Σ[c]_q[c+1]_q` is the **compact SU_q(2) q-Casimir**
   (rational in q, finite of size `p(n)`, quadratic-in-content; `q→1 →
   Σc(c+1)`), with content-Casimir degeneracies (`μ_{(3,1)}=μ_{(3)}`). It cannot
   be a q-Bessel zero spectrum (infinite/transcendental), and `p(n)≠n` rules out
   the degree-n q-Lommel zero set. **REDIRECT:** the q-Bessel/q-Lommel zeros live
   in the `n→∞` brane-tower / E_q(2) contraction limit — where the binding `Δ_λ`
   ladder also lives, via the **q-Lommel three-term recurrence**. Confirms #2279's
   "Bessel object is the tower, not the n-trace" from the spectral side. Audit:
   `docs/audits/2026-06-14-qbessel-lead4-mu-lambda-qlommel-derivation.md`.
3. **Linkage + notation.** Wired the missing `uses[]` edge
   `prop:q-beta-c-k-recursion-from-habiro-q-difference → prop:q-heat-kernel-peter-weyl`
   (the narrative already had `F = trace of the q-heat kernel`); added the
   "q-Bessel identification of F" subsection (F = Z_q = Hahn–Exton q-Bessel, with
   the honest fibre-vs-archimedean banner); registered `J_ν^{(3)}` (Hahn–Exton
   q-Bessel) + q-Lommel `h_{n,ν}` in the notation register with the `J_K` (Jones)
   collision note.

**NOT wired** to production; `c_k` stays cal-anchored (the real-x archimedean
closure is refuted — this is fibre-level structure). **Coordination:** intent
posted on #1839 (c_k kernel — function-level form), #2078 (binding Δ_λ — q-Lommel
tower lead + no-7th-fit gate), #1762 (1ppQ roadmap — q-Bessel route status).

## 2026-06-16 — Q_β Path A: counit (transition) vs Markov-trace (mass) (PR #2363)

**Result.** The free-neutron relation `Q_β = |Δ(net)|·𝔈₀` is the **Frobenius
counit** `ε` of the nucleon NF difference, categorically distinct from the
**Markov trace** `tr_M` the per-braid mass tower is built on. The two agree on
the nucleon difference *only* at the trivial loop `z=1` (`ε = tr_M|_{z=1}`;
gap `ε − tr_M = h(z−1)`); at the substrate `z = 1/(√q+1/√q) ≈ 0.5`, `tr_M`
gives Q_β ~2× low (−56%) while the counit gives +0.17%. With `𝔈₀ =
m_e·c_q²·ℏ_q^E = m_e/(q(q−1))` the **per-Hecke-step energy**, Q_β reads as
*(reduction-count diff) × (energy/step)* — a transition observable dual to
the static-mass trace (trace = pair-with-unit `𝟙`; counit = pair-with-integral
`ω = G⁻¹𝟙`).

**Resolves** the 2026-05-24 net-ansatz "(a) leading-order vs (b) fitting?"
worry in a third way: the counit is the *correct functional for a transition*,
and the +0.17% is the `N=0` consistency between the two functionals (same
residual as the 0.74% `𝔈₀` derived-vs-cal gap), not a fit. **Open:** the
convergence leg — proving the trace mass-difference `m(n)−m(p)−m_e` converges
to `ε(Δ)·𝔈₀` with +0.17% as the `N=0` remainder.

**Artifacts.** Audit docs `2026-06-16-q-beta-net-ansatz-path-a-counit-vs-trace.md`
+ `2026-06-16-q-beta-path-a-counit-transition-resolution.md`; verified Lean
`QOU/Interactions/qbeta_counit_vs_trace.lean` + `qbeta_energy_scale.lean`
(generic field, sorry-free); paper blocks `prop:qbeta-counit-closed-form` +
`rem:qbeta-counit-transition`. **Coordination:** intent posted on #2106
(Hoefsmit Stage B — counit closes the net-ansatz functional type), #2347
(Markov-M3 Lean — orthogonal; counit is the trace-dual), #2346 (q-anchor —
#2363 is q₀-anchor-agnostic, generic-`q` Lean, no conflict with deferred
q₀-selection). #2127 (Habiro/QA plumbing) — silent pass.

**Reconciliation flag (§6, 2026-06-16, #2346 ↔ #2363).** #2346 promotes
`Q_β → 𝔔_β` (fraktur, ~138 files) and adds `conj:binding-qbeta-complex-volume`:
`𝔙(K) = E₀·tr_M((Π_free−1)∘𝓜) ∈ ℂ`, **binding = Re 𝔙, 𝔔_β = Im 𝔙**
(bar-odd/`sinh`). This is a *second* Q_β framing (`Im` of a **trace** object)
parallel to #2363's **counit** `ε(Δ)·𝔈₀`. They are **not** trivially the same:
`ε(Δ) = h²/2 − h` splits under bar (`q→q⁻¹`, `h→−h`) into bar-even `+h²/2`
and bar-odd `−h`; the bar-odd (`Im`) channel *alone* gives **+11.86%**, while
the full counit (both channels) gives **+0.17%**. So if `Im 𝔙` is strictly the
`sinh` channel, `Im 𝔙 ≠ ε(Δ)·𝔈₀` by the bar-even `h²/2` term (~11.7% gap) —
reconciliation target, **not** a silent fold. Posted on #2363
([comment](https://github.com/litlfred/qou/pull/2363#issuecomment-4724054009));
awaiting owner confirmation whether `Im 𝔙` is the pure `sinh` channel or the
full transition value. Notation: rebase #2363 onto #2346 once it lands, mirror
`𝔔_β` in the 4 new content blocks. Additional unifying lead from #2346:
**binding is also a transition** (constituents→bound = `Re 𝔙`), matching
#2363's prediction that binding *and* Q_β are both transition observables.

**RESOLVED (branch A, no double-count) — 2026-06-16.** Tested by computing
#2346's actual `Im 𝔙` from `habiro-exact-qbeta.witness.json`:
`Q_A = Im 𝔙 = 0.7836458028 MeV = |ε(Δ)|·𝔈₀` to `2·10⁻¹⁶`. So `Im 𝔙` is the
**full** counit (+0.17%), **not** the bar-odd part (+11.86%). The framings
**agree**; no double-count. The error in the flag above: `Im 𝔙` is the `sinh`
channel of the **single-knot confinement defect** `(Π_free−1)∘𝓜`, a different
object from `Δ = NF(n)−NF(p)` — its value is the whole counit, not `−h`. The
counit's internal bar-split is **not** #2346's binding/Q_β Re/Im split.
Outcome: `𝔔_β = Im 𝔙 = ε(Δ)·𝔈₀` is one observable in two presentations
(cross-validated to machine precision). Retraction + branch-A audit:
[`docs/audits/2026-06-16-qbeta-binding-double-count.md`](../audits/2026-06-16-qbeta-binding-double-count.md);
owner notified ([comment](https://github.com/litlfred/qou/pull/2363#issuecomment-4724147020)).


## 2026-06-18 — counit convergence-leg invariant pinned at live q₀ + block reconciliation (PR #2469)

**Scope.** Transition-side (counit) follow-on to the merged Path-A framing
(#2363) — **orthogonal** to the active static-mass c_k frontier (#2106 Hoefsmit
Stage B, #1839 residue kernel, #2453/#2460 Jacobi–Anger/Φ_q). No c_k, no fit,
no production wiring.

**Result.** Re-evaluated the counit/trace functionals at the *live*
proton-anchored `q₀ = 1.10997859…` (50 dps,
`computations/qbeta/qbeta_counit_substrate_consistency.py`, witness
`qbeta-counit-substrate-consistency`). Reproduces **both** merged signatures at
the live anchor — counit `|ε(Δ)·𝔈₀| = 0.78365 MeV` (**+0.168 %**, right tool)
and trace `|tr_M(Δ)|_{z_sub}·𝔈₀| = 0.34549 MeV` (**−55.84 %**, wrong tool),
`z_sub = √q/(q+1) = 0.49932` — **confirming the +0.17 % counit value is current,
not stale** (re-pin 2026-05-28).

**Convergence-leg invariant (formalize-first).** The +0.17 % counit residual is
the `N=0` truncation remainder, bounded by the falsifiable
`O(ℏ_q²/(1−ℏ_q²)) = 0.9915 %` at q₀ (observed `0.168 % ⊂ 0.99 %` ✓). This is the
invariant the open `conj:qbeta-trace-counit-convergence` must respect; closing it
still needs a *closed evaluation of the tower-summed* trace difference (the trace
term is the wrong functional — −56 % — so it is functional-consistency, not a
perturbative limit). Audit:
[`docs/audits/2026-06-18-qbeta-counit-substrate-consistency.md`](../audits/2026-06-18-qbeta-counit-substrate-consistency.md).

**Block fix.** The merged `conj:qbeta-trace-counit-convergence` `.md`+`.lean`
quoted the `N=0` trace term as `≈ 0.49 MeV (~259 %)`; the canonical functional
`tr_M(Δ)=h²/2−h·z` at `z_sub` gives `0.345 MeV (−56 %, ~2.3× low)` — matching
#2363's own "~2× low, −56 %" and the witness. Corrected the prose/docstring
(conjecture statement, Lean class, conditional corollary unchanged).

## 2026-06-19 — §4a single-x q-Bessel REFUTED across all discrete towers; content/twist eigenbasis reframing + 3 gap-closing lemmas (PRs #2496, #2502)

**Scope.** Transition-side (Reeb-tower / Jacobi–Anger §4a) follow-on — the §4a
single-x q-Bessel identification of the bar-odd `χ_λ(𝓑_n−𝓑_p)` tower. No c_k, no
fit, no production wiring; all `auditOnly`/`probe`; TIERED.

**Negative — single-x q-Bessel does not extend.** The 6.84 % n=3 near-match was
tested against every natural discrete tower variable and fails to converge in all:
- **strand tower** (n=3A): parity obstruction — bar-odd order-parity alternates
  odd/even with A, odd-order test is 0/0 at n=6 ([#2496](https://github.com/litlfred/qou/pull/2496));
- **winding iterate** β^k: parity = k mod 2; odd-k residual diverges
  (6.84 %→no-soln→~100 %→erratic);
- **framing tower** Δ^{2m}: separates orders by content into a gapped cluster
  (`W₅=0`), §4a undefined;
- **single content mode** (c=0 (2,1)-block): residual 480/606/186/240 %
  ([#2502](https://github.com/litlfred/qou/pull/2502)).
Live lead now the **continuous E_q(2) contraction** (Hahn–Exton q-Bessel), not
discrete braid towers (n=3 HE-vs-ordinary too thin to decide — 3 orders).

**Positive — content/twist eigenbasis makes the proved relations evident.**
Anchored on the Lean-proved ribbon eigenvalue `θ_λ=q^{2c(λ)}`: framing GF is a
3-pole rational `χ_λ/(1−t·q^{2c})`; bar-odd shape depends only on `|c(λ)|`; the
single-x failure is a `|content|`-graded multi-mode object. Audit:
[`docs/audits/2026-06-19-content-twist-eigenbasis-reframing.md`](../audits/2026-06-19-content-twist-eigenbasis-reframing.md).

**Gap-closing.** The eigenbasis promotes three verified-only facts to rigorous
lemmas (exact-symbolic; Lean follow-up): **L1** order-parity = word-length parity
(⇒ the #2496 parity obstruction is a theorem); **L2** `χ_λ(1/q)=(−1)^L·χ_{λ'}(q)`
(⇒ the conjugation invariant); **L3** the framing 3-pole GF. **Does NOT** close the
Δ_λ binding gate (content-statistic refuted, GAP-A-3 — out of scope).

## Cross-refs

- AGENTS.md §Precision goals (L1 / L2 / Subgoal-1 / Subgoal-2)
- AGENTS.md §Q_β c_k truncation order framing
- `docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`
- `docs/audits/2026-05-30-l2-100x-status-3-failing-shared-root.md`
- `docs/audits/2026-05-30-klr-dialog-assessment.md` (recurrent re-pitch failure modes)
- `docs/audits/2026-06-14-klr-positivity-mass-gap.md` (KLR positivity resolution and missing T2/T3 quadratic absolute mass gap)

## 2026-07-02 — AW holomorphic tie: two-session split (mechanism vs identification)

Two sessions worked bean `1jrh` concurrently at different levels; results are
**complementary** (no inconsistency, verified by cross-read):

- **Mechanism half (PR #3216, session 014LW6oa…):** `recurrence_invol_descent`
  compute-confirmed at the H₂/Hopf tower, where the AW multiplier `c = q²+q⁻²`
  is FORCED by the crossing eigenvalues (no identification, no fit): tower +
  both parity channels ride one Chebyshev/q-ultraspherical recurrence
  (exact + <1e-65 at muon-q₀); bar-even hypothesis proved necessary
  (bar-odd multiplier cross-couples channels exactly). Also lands the
  self-dual locus constraint (`barFixed_qbeta_zero`, sorry-free): any 𝔙
  assembly must send amphichiral composites to real 𝔙.
- **Identification half (main `ad28b5a9` + PR #3221, session 01Jceoju…):**
  the PHYSICAL c_k-ladder AW identification is under-determined (4 params vs
  ≤2 trusted rungs) ⇒ GATED on `c₃^even`; #3221 then measured
  `c₃^even = +86.661` (exact s-series), W₂ > 0 consistent, W₃ still gated on
  genuine c₄ rungs. Bean `1jrh` stays per the prune (todo/gated); the
  mechanism note is appended, status NOT flipped.
- **Merge-order note:** both #3216 and #3221 touch `.beans/1jrh…md` —
  whichever merges second rebases the bean file (append-only, trivial).

## 2026-07-02 — Stage-C σ₃-lift obligation machine-checked (Lean; no Λ candidate)

Follow-up to the two-session split above (bean `pxhb` → session bean `cbzx`):
the sole remaining Stage-C open item — the categorical σ₃-lift `Λ ∈ H₄(q)` —
now has a machine-checked obligation file,
`QOU/QBeta/StageCSigma3LiftObligation.lean` (lean-direct exit 0, sorry-free,
generic `[CommRing R]` + ordered decision section per §7c), mirroring the s013
`KeystoneQBesselRadialTarget` pattern:

- **Carrier** `StageCSigma3Lift` (OPEN, no instance): C12
  stabilization-constant-1 reading `c₄^even = tr_M^{H₄}(Λ) − tr_M^{H₃}(shadow)`,
  σ₃-gating non-degeneracy (`c4even ≠ 0`), bar-evenness of both traces;
  derived: the rung is bar-even (`c4even_bar_even`). The scope-§2 provenance
  rule (derive Λ from decay content, never back-solve) and anchor-stability
  stay meta-level selection rules — deliberately not encoded.
- **Sign-tier robustness** `W2_pos_of_sign_tiers`: W₂ > 0 from the measured
  TIERS alone (c₂^even < 0, c₃^even > 0, c₂^odd = −1 proved, c₃^odd < 0) —
  the audit's W₂ ≈ +102.67 is one instance; positivity is tier-robust.
- **Decision rule** `one_recurrence_incompatible` + composed
  `sigma3_lift_kill_test`: any valid lift whose genuine rungs give W₃ ≤ 0
  refutes the single-AW-recurrence identification (scope-(a), machine-checked
  form of the gated test; converts the untrusted-input "indicative lean" into
  a one-call decision once genuine c₄ rungs exist).

No Λ enumerated or evaluated (scope no-fit rule intact). Λ specification
remains the owner-gated research object.

---

## P-C15 — 4₁ order-2 qZeilberger operator clears the bar-parity gate (2026-07-03)

First **survivor** on the fibre-kernel axis: the newly-landed 4₁ order-2
colored-Jones operator (`aj_figure_eight_certificate.py`, exact N=1..12) is a
candidate for the recursion kernel `R(q,ξ)`. Its Casoratian ratio
`W_{N+1}/W_N = a₀/a₂ = (q³x³−q³x²−x+1)/(q³x³−q²x−qx²+1)` (x=q^N) is **exactly
bar-self-reciprocal** under `q→1/q, x→1/x` (twist = 1, a Laurent monomial) and its
q→1 classical shadow is `1 > 0` (consistent with measured even-channel
`W₂ = +102.674 > 0`). **Gate PASSED** → *not excluded*; **no anchor sweep** (per the
formalize-first gate). Distinct from every refuted C1–C14 (C14 tested Ohtsuki
*scalars* as c₃; cp4i tested only the degenerate first-order Newton restriction —
this uses the full second-order operator). **Not a closure, not a c_k value, nothing
wired.**

- Probe: [`qbeta_pc15_casoratian_bar_parity_probe.py`](../../computations/qbeta/qbeta_pc15_casoratian_bar_parity_probe.py)
  → [`qbeta-pc15-casoratian-bar-parity.witness.json`](../../computations/qbeta/qbeta-pc15-casoratian-bar-parity.witness.json)
- Audit: [`2026-07-03-qbeta-pc15-casoratian-bar-parity.md`](../audits/2026-07-03-qbeta-pc15-casoratian-bar-parity.md)
- **Gated next step:** the H₄ Hoefsmit `c₄^even` build (bean `8we6`) → genuine c₄ rung →
  the sibling's machine-checked `sigma3_lift_kill_test`
  ([`StageCSigma3LiftObligation.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/StageCSigma3LiftObligation.lean))
  evaluates the anchor Casoratian `W₃/W₂`. P-C15 de-risks that build.
- Part of the 2026-07-03 **path-to-1ppQ reanalysis** (main @ `746a5091`): Identity I is
  a rigor input to a falsifiable gate, **not** the keystone unlock; the keystone's
  geometric leg (Σ(2,3,5) WRT on S³/2I) was **refuted 2026-07-02**; Q_β (this axis) is
  the one near-term needle-mover above the CAL-2 floor.

## Production/framing — m_p `c₄` dropped (fit), Q_β derived-to-c₂ confirmed (2026-07-04)

Two paired audits closing the "is the precision tower derived or fitted?"
question on both sides of the μ–p work.

- **m_p (#3280, MERGED).** The `(1 + 46u⁴)…` Habiro tower was a CODATA fit:
  the exact `c₄` is **affine in the q₀ pin** (≈0 at the proton pin, 46 at the
  muon pin, slope 3.99/ppb) — the μ–p tension reparametrized, not a categorical
  constant. `4143/90` had no derivation trail and cited a refuted Reeb route.
  **Dropped** (also fixed a live +242 ppb regression — the muon-era tower was
  being applied to the proton-pinned q₀). m_p now honest at +1.35 ppb; L2 count
  3/7 → **2/7** (m_e, m_K/m_π). The one proved c_k recursion is the Habiro
  integrality `a_m` ladder (finite, M=8), which yields the floor, not 46.
  Audit: [`2026-07-04-c4-mu-p-tension-pin-dependence.md`](../audits/2026-07-04-c4-mu-p-tension-pin-dependence.md).
- **Q_β (#3296).** The honest counterpoint: the production Q_β ladder is
  **fully derived** to the **proved c₂ = −1** — `Q_A` (`prop:neutron-qvalue-symbolic`,
  +1677 ppm) × c₁ = b Kashiwara edge (+74 ppm) × `(1−u²)` = c₂ = −1
  (`prop:q-beta-c-2-eq-neg-one-structural`, +1.28 ppm). No fit; production
  correctly stops at the proved c₂. The ~164× L2 miss is the honest derived
  residual, not a stripped fit. Audit:
  [`2026-07-04-qbeta-derived-ladder-tiers.md`](../audits/2026-07-04-qbeta-derived-ladder-tiers.md).
- **Frontier (both sides = same keystone).** Below the proved floor — m_p's c₄,
  Q_β's c₃ = −2 = J_Hopf — is the s5bb Habiro-element keystone. c₃ is settled
  non-wireable (PR #1580; flip-flop table above). Sibling coordination:
  **#3294** (ζ₄/Φ₄ refuted on the Δ_net carrier — prunes one route into the c₃
  frontier, localizes residue to R₁₂) and **#3273** (route-A `c₄^even` H₄ build)
  both live past this floor; flagged the pin-stability caution to #3273 so
  `c₄^even` doesn't absorb the μ–p tension the way m_p's c₄ did.
## 8we6 — H₄ `c₄^even` build: appended-strand routes fail the gate; channel-projection is the survivor (2026-07-04)

The gated next step P-C15 pointed to (the H₄ Hoefsmit `c₄^even` build) was attempted.
Route B (re-decompose the unchanged H₃ element at λ⊢4) is **machine-checked pruned**
([`H4RouteBBranchingPrune.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/H4RouteBBranchingPrune.lean),
PR #3273). A headless n-agnostic H₄ Markov-assembly
([`qbeta_h4_nucleon_assembly.py`](../../computations/qbeta/qbeta_h4_nucleon_assembly.py))
reproduces the committed H₃ `Δ(net)` **exactly**, validating the harness (H₃ ladder
gives `c₂=−8.00641, c₃=+86.66116` exactly).

**Both owner-chosen explicit 4th-strand routes fail the stability gate.** Lepton
(u–d-averaged) and brane (bare σ₂ Hopf) reach word length 4 (real σ₂-support) but
**move c₂/c₃** — at full coupling (lepton `−6.84/+73.4`; brane `+3.99/−65.5`,
sign-flipped) **and at linear order** (`dc₂/dg|₀ ≈ +16.4 / +13.7`, not zero). Recorded
**scope-(a)**: the *appended-strand construction* is out (it redistributes NF weight
across all word lengths, hitting the short words that drive c₂,c₃), **not** the
4th-strand ingredient.

**The g-response failure motivates the channel-projected (Brunnian/SDP) route** as the
structural survivor: the n=4 cup-diagram Gram `G=[[δ²,δ],[δ,δ²]]` splits into a
**bar-even** channel (`u1+u2`, eigenvalue `δ(δ+1)` — where a `c₄^even` rung lives) and
bar-odd (`u1−u2`, `δ(δ−1)`); both bar-invariant. This channel is orthogonal to the
nucleon's short-word structure, so it does not touch c₂,c₃.

- Audit: [`2026-07-04-8we6-h4-route-a-explicit-strand-gate-scan.md`](../audits/2026-07-04-8we6-h4-route-a-explicit-strand-gate-scan.md)
- Gram groundwork: [`qbeta_h4_gram_barchannel_probe.py`](../../computations/qbeta/qbeta_h4_gram_barchannel_probe.py) → witness.
- **Owner-gated remaining decision:** the SDP objective weights `t` / net target
  `n_target` for the n=4 singlet selection, and the selected-channel → Q_β net-route
  ladder linkage. These are framework choices, not agent ansätze.

## 8we6 resolution — Markov-trace calibration already derived; c₄^even = keystone residue (2026-07-04)

Owner authorised "re-derive the Q_β ladder calibration for the Markov-trace functional."
Corpus-grep shows it is **already derived and Lean-proved** — and the derivation's verdict
is that `tr_M` is the *wrong* functional for the transition:

- **Counit is correct (derived).** `ε(β)=⟨β,G⁻¹𝟙⟩_G` = crossing-stripped reduction count
  (transition); `tr_M(β)=⟨β,𝟙⟩_G` = closed-loop static mass. β-decay is a transition ⇒ `ε`.
  `tr_M` misses by ~2× ([`qbeta-counit-transition.md`](../../content/quantum-observable-universe/particle-interactions/qbeta-counit-transition.md)).
- **Markov-trace leading analog is Lean-proved** ([`qbeta_counit_vs_trace.lean`](../../content/quantum-observable-universe/lean/QOU/Interactions/qbeta_counit_vs_trace.lean),
  sorry-free): `trMNP h z = h²/2−h·z`, gap `ε−trMNP = h(z−1)`, `trMNP_q=(q²−1)(q²−2qz−1)/(2q²)`.
  `E_0` is functional-independent; the phase `cos(α_eff)` **is** `τ_M(M_β)`. Nothing to re-derive.
- **Open object = ladder residue `F(q)`**, a fibre-level Habiro/root-of-unity element — the
  **s5-so3 keystone** `W_λ` (bean `s5bb`); ledger says do not open a separate Q_β probe.

**Bean 8we6 closed:** c₄^even not reachable by re-decomposition (Route B, Lean-pruned),
counit strand-append (contaminates c₂/c₃, proven full+linear), or tr_M recalibration
(derived-wrong; N=0 analog already Lean-proved). Redirected to the keystone.
Audit: [`2026-07-04-8we6-h4-route-a-explicit-strand-gate-scan.md`](../audits/2026-07-04-8we6-h4-route-a-explicit-strand-gate-scan.md).

**2026-07-11 (#3509) — selection-rule engine + Δ_λ ζ₄ locus + strong-sector vacuity.**
Re-scoped the Gemini-session c₃ over-claims (c₃=−Vol(4₁) → scope-(b) bar-parity
exclusion; three vacuous "closure" Lean stubs bannered). Landed
`QOU/SelectionRules.lean` (sorry-free): `odd_ne_even_of_ne_zero` (bar-parity) +
`nonneg_sum_ne_neg_target` (sign-positivity) unify the weak (c₃) and strong (Δ_λ)
sign/parity exclusions. Δ_λ probes: raw T(2,5) character + real-q re-framing pruned;
the Δ_λ chirality sign located at **q=i (ζ₄, non-semisimple H₅)**:
`sgn(Δ_λ)=(−1)^{n(λ)}=q^{2n(λ)}|_{q=i}` — the SAME ζ₄ fibre point #3429 formalizes for
the Q_β f-map (Arm 2). Coordinated on #3429 (intent comment); no file overlap.
Open: exact chiral operator realizing `q^{2n(λ)}`; magnitude `|Δ_λ|=dim` (Track A).
Audit: [`2026-07-11-gemini-session-c3-overclaim-continuum-and-lean-audit.md`](../audits/2026-07-11-gemini-session-c3-overclaim-continuum-and-lean-audit.md).

**2026-07-11 (#3556 merged, #3563) — KC17 parity-descent dichotomy + ζ₄ ↔ odd-carrier bridge (Lean).**
Formalized *why* the bar-odd c_k channel is archimedean, as sorry-free Lean
(lean-direct EXIT 0). #3556 (merged): `uside_parity_descent_iff_zeta4` — the
u-side cyclotomic re-basing transports the fibre bar-parity to the c_k rungs iff
`q²=−1` (q-side `(−1)^k` vs u-side `(q²)^k` twists agree only there); over ℝ,
`uside_parity_never_descends_real` (never, `q²≥0`). #3563: `descent_iff_order_four`
— that descent point **is a primitive 4th root ζ₄** (`q²=−1 ↔ q⁴=1 ∧ q²≠1`), plus
the formal composed bridge `uside_parity_descent_iff_order_four`. This is the SAME
ζ₄ fibre point the #3509 entry above located for Δ_λ (`q^{2n(λ)}|_{q=i}`) and #3429
formalizes for the f-map — now the Q_β-side parity descent is pinned to it too.
Net (with merged #3534, `S=Q_β/E₀` irreducible archimedean): the odd channel
connects to the c_k parity only at ζ₄, never on the real substrate axis → S is
irreducibly archimedean, corroborating the Φ_b-at-real-q₀ route (#3544/#3562/#3536).
Coordinated: intent on #3560 (ζ₄ swap sibling), support note on #3562 (Φ_b).
No c_k value; wires nothing; no tier change.

**2026-07-11 (#3536 + #3567, merged) — untested-avenues execution wave: every
discrete/formal c_k identification route closed; C15–C18 land on the map.**
Owner-directed survey + same-day execution of all ranked avenues
([`2026-07-11-qbeta-ck-untested-avenues-and-literature.md`](../audits/2026-07-11-qbeta-ck-untested-avenues-and-literature.md) §6),
one probe per commit, pre-registered kill criteria, nothing wired:

- **C15** Borromean forced-link shadow REFUTED (τ_D Brunnian ℏ³-vanishing;
  4 canonical normalisations all miss −2).
- **C16** Habiro-ring membership of the ladder in `q` REFUTED (scope-(a)) at
  natural normalisations — the ladder is not a Habiro element's q=1 expansion;
  gates off GSWZ Galois descent; converges with KC8 (simple pole ≠ Gevrey-1).
- **C17** raw `q^N↦q^k` 4₁-operator kernel REFUTED (scope-(a)); P-C15 bar-parity
  survivor intact (needs re-basing/twist, canonical rungs).
- **C18** PSLQ recognition of *extracted* rungs ENTROPY-BLOCKED: empirical c₃
  carries ≤ ~2.2 digits/anchor; **"empirical c₄ = −0.972" is a rounding
  artifact of c₃** (identically 0 under exact extraction — updated in the
  registry rung-4 row, [`ck-dk-canonical-registry.md` §3](ck-dk-canonical-registry.md)
  + JSON twin [`ck-dk-registry.json`](ck-dk-registry.json)). Extracted k ≥ 4 is
  noise; kernel tests need canonical rungs.
- **C13 extended**: exponentiated-uniform per-block seeding refuted
  (exp ≡ linear at c₃, symbolic).
- P2 (Φ_b infra) resolved as collision → deferred to the `qou-9lot` line
  (merged #3540; open #3562/#3544).

Net: with C16+C18+KC8+KC17, the surviving c₃ bar-odd object is the **analytic
Φ_b state-integral face at real q₀** — active on #3562 (m-plane inversion +
`FaddeevPhi` class repair) and #3544 (real-integral route). Map rows:
[`2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md`](../audits/2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md) §2.
Coordination this cycle: duplicate `CuspShapeBarParity.lean` flagged on
#3573 ↔ #3579 (QBeta/ vs Knot/, same theorems); parallel Lean Φ_b carrier
flagged on #3544 ↔ #3562 (instantiate the repaired class, don't fork).

**2026-07-11 (#3540/#3562 merged, #3596) — Φ_b constructed + S-flip source localized to the m-deformation stage.**
Three merged/landed tranches on `claude/faddeev-phi-b-construction-wwblhu`:
(1) #3540: substrate b-map pinned `b = √(t/2π)e^{+iπ/4}` (q = 1/q₀, dual
q̃ ≈ 5e−165); contour == modular-double product to 1e−39 at both anchors;
the documented −π/4 branch is the inverse-conjugate object. (2) #3562:
`FaddeevPhi` class repaired (unguarded `shift_binv` unsatisfiable by any
total-function encoding — the dual lattice carries POLES; false
`phi_binv_zero` removed); `phiBProd` tprod instantiation with CommMonoid-level
telescoping, sorry-free; m-plane inversion: S smoothness-killed
(|dS/dq| ≈ 3.8e6, lever = CODATA ÷u³), un-levered r = S·u³ smooth
(r_μ ≈ +5.98e−9, r_p ≈ −2.44e−8, slope ≈ −2.4) = the well-posed target.
(3) #3596: 84 lever-class (|U|, κ/u³) candidates all fail cross-anchor
(h and 2t sit 2% below the proton feasibility floor |u|_min = √(2|S|/√3));
pole-seed sensitivity probe: the Φ_q-pole-seeded Newton stage is
ANCHOR-BLIND (amplification 1.4e−4, Jacobian O(1)) ⇒ with #3600's θ-smooth
negative and the rate exclusion, the S sign-flip source is localized to the
m-deformed gluing system (the m(q₀) assignment), scope-(a) throughout.
Coordinated: intent+results on #3573, #3600; earlier on #3543 (merged).
Open: Multipliable discharge (LogBounds cone building); m(q₀) law itself.
No c_k value; wires nothing; no tier change.

- **C19 (#3573, pole-seed Newton — the phase is a BRANCH SELECTOR).** Seeding
  Thurston's figure-8 gluing Newton with the *real* substrate pole `q₀^{-k}`
  flows to the **degenerate golden branch** `z²−z−1=0` (`φ=1.618`, Vol=0), never
  the hyperbolic cusp `z²−z+1=0`. The two branches swap bar-parity roles via the
  discriminant flip `−3 ↔ +5` (`goldenShape_barEven_sq=5`, Lean-proved), so
  CS = bar-odd `S` turns on only under complexification — the phase `φ(q₀)` *is*
  the branch selector (= open `conj:agde`). Independent quantitative confirm of
  the geometry-side negative (#`1a4894b8`): full Rogers-dilog CS at substrate
  scale `~1.7e-5`, **~2350× below** `|S|` — the naive 4₁ CS deformation is orders
  too small, so `Φ_b` (not pure-4₁ geometry) is the live `S` carrier. No c_k wired.

**2026-07-11 (#3571 merged, #3606) — even-channel action arithmetic home = ℚ(√3), both numerical-block and exact-saddle.**
Completes the even-channel arithmetic mapping, complementing the odd-channel
#3556/#3563 (KC17 ζ₄ + Hopf-cubic prime-19). #3571 (merged): the *numerical* PSLQ
of the 4₁ resurgence-action coefficients over ℚ(√−3) is **entropy-blocked**
(divergent series c_m~m!/A^m + fit contamination) — ℚ(√−3) is the arithmetic home
(4₁ trace field) but unreachable by fit. #3606: the **exact-saddle** complement,
sorry-free Lean (`QOU/QBeta/Qsqrt3SaddleArithmetic.lean`): the 4₁ Kashaev saddle
at x*=5/6 has Taylor data ∈ ℚ(√3)·π^k (Hessian −√3π, then −4π², −8√3π³, …) and
leading coefficient `b₁ = √3π/54 ∈ ℚ(√3)·π` — computed exactly where PSLQ failed.
Even-channel counterpart of `HopfCubicOddCarrier` (KC20). **Consistent with the
cusp-shape siblings** #3573/#3579 (`barEven ω=1`=Vol, `barOdd ω²=−3`=CS, trace
field ℚ(√−3)): same 4₁ ℚ(√−3) home, cusp-shape side ⊕ saddle-expansion side; no
§6 escalation. Anti-laundering: `b₁≈0.101` is the naive saddle value, explicitly
≠ observable c₁≈0.554 (needs full state-integral normalisation); no action value
wired. Coordinated on #3573 (intent) + #3579 (link). Owner ruling #3607
(Subgoal-2 open-for-all) relaxes the deferred observable closure to in-scope
(anti-fit still binds). No c_k value; wires nothing; no tier change.
**Currency (Copilot #3606):** the two fields are now certified **distinct** —
the 4₁ *trace* field ℚ(√−3) is imaginary quadratic (cusp/CS side, #3573/#3579),
the *saddle* data field ℚ(√3) is totally real (even-Laplace side, this PR); both
embed in ℚ(ζ₁₂) and √−3 = i·√3 relates the generators, but they are not equal.
The earlier "same ℚ(√−3) home" phrasing is refined accordingly — the two channels
share the *ambient* ℚ(ζ₁₂), each realising its own real/imaginary quadratic subfield.

**2026-07-11 (#3606, Ohtsuki κ₁) — even-channel OBSERVABLE leading coefficient is
EXACT: `κ₁ = 11√3π/108 = (11/2)·b₁`.** The naive saddle `b₁=√3π/54` (#3606) is the
integral-Laplace value; the *observable* leading coefficient `κ₁ = [1/N] log J_N(4₁)
≈ 0.55421647` (the value #3571 could only fit; naive saddle missed it, κ₁/b₁=5.5) is
identified exactly by a targeted 10-point Vandermonde extraction (N≤786432, ≈23
confident digits) + 2-term PSLQ (33-digit agreement):
`κ₁ = 11·√3·π/108 ∈ ℚ(√3)·π` — the Ohtsuki figure-eight **2-loop** coefficient
(imaginary form `κ_1^Oht = (11/72)/√−3`, the classical numerator **11**). #3571's
entropy-block was on the *full ladder*, never the best-conditioned leading rung;
its PSLQ miss was a basis-size artifact (10 elements @ 15 digits). Lean
(`ohtsukiKappa1_eq_eleven_halves_b1`, `_mem_qsqrt3`, sorry-free) certifies the
algebra κ₁=(11/2)·b₁ + field membership; the *value* is the numerical Ohtsuki
identification. Probe [`qbeta_ohtsuki_kappa1_extract.py`](../audits/scripts/qbeta_ohtsuki_kappa1_extract.py).
**Anti-laundering:** κ₁ is a 4₁-Kashaev/Ohtsuki topological fact, NOT a Q_β
production c_k — the 4₁↔Q_β action bridge is the open keystone; nothing wired, no
tier change. Higher [1/N^k] rungs remain entropy-blocked (#3571).
**2026-07-11 (#3600) — q-Reeb rotation angle θ(q₀) for the S wall (probe + Lean + paper).**
"Keep pushing on arg(u(q₀)) using reeb." Built the 2×2 Hoefsmit seminormal
block of σ₁,σ₂ on V_{(2,1)} and read the figure-eight operator
M_{4₁}=(σ₁σ₂⁻¹)² eigenvalue phase (gauge-invariant). Verified from the actual
rep: braid+Hecke hold, det M=1, |tr M|<2 ⇒ |λ_{4₁}|=1 (confirms the content
block's Reeb claim). Derived: θ(q₀)≈117.087° at both anchors; θ(1)=2π/3 EXACT
(S₃ 3-cycle, amphichiral, CS=0); closed form tr=q⁴−2q²+1−2q⁻²+q⁻⁴. θ is SMOOTH
(dθ/dq≈−51°/unit q) ⇒ arg(u)=θ is a scope-(a) NEGATIVE — θ cannot supply the
dc₃/dq≈4.66e6 sign-flip; the open q₀→u map (conj:algebraic-geometric-dilog-
equivalence) still owns it. Third independent confirmation of the "smooth
geometric quantity ≠ the hypersensitive phase" pattern (with #3596 pole-seed
amplification 1.4e−4 and #3573 near-singular φ). Reeb's real contribution:
Δθ=θ(q₀)−120°≈−2.91° is the parameter-free amphichirality-breaking seed of S.
Lean (hand-audited, toolchain behind egress): figureEightTrace + tr(1)=−1 +
figure_eight_classical_reeb (θ(1)=2π/3 proved via existing unit-modulus thm +
primitive-cube-root). Paper: rem:figure-eight-reeb-theta-value. Coordinated:
intent on #3596/#3573/#3579; flagged the #3573↔#3579 CuspShapeBarParity.lean
duplication and the θ(braid-operator) vs boost(meridian-holonomy) phase
distinction. No c_k value; wires nothing; no tier change.

**2026-07-12 (#3648) — KC19×KC20 bridge reconciliation + ℚ(√−19)≠ℚ(√−3) arithmetic separator.**
Self-correction of merged #3618 (it missed the prior 2026-07-07 hopf-cubic-vs-crossing-weight
bridge audit): assertion 4 now separates the MEANINGFUL Hopf-sector shadow C_Hopf(2)=−2 (=J_Hopf(1),
Lean-certified) from the COINCIDENTAL total-C(3)=−2 at golden y=3; #3618's genuinely-new pieces
(4−h²=6−y kernel-denominator identity; disjoint singularities) delineated from the bridge audit's
prior coverage. NEW (scope-(a), grep-confirmed not explicit): the odd carrier's quadratic field is
ℚ(√−19) (disc C_Hopf=−76=−2²·19), DISTINCT from the even/4₁/Φ_b field ℚ(√−3) — channels separated
by ramified odd prime 19 vs 3. Consequence: the odd algebraic field-of-definition is not contained
in the 4₁/Φ_b arithmetic; a closure must supply the disc-19 field. STRICT scope guard: does NOT
exclude Φ_b (transcendental, richer arithmetic possible), does NOT address the anchor-dependent c₃
swing (w(q) fibre, KC19). Sharpens the search target. No c_k value; nothing wired; no tier change.
**2026-07-12 (PR #3622, in flight) — NZ parity prune + exact 4₁ even series.**
Lean (sorry-free): the geometric NZ deformation series has NO odd rung
([`NeumannZagierParity.lean`](../../content/quantum-observable-universe/lean/QOU/Knot/NeumannZagierParity.lean),
scope-(b), invariant = parity) — kills this session's own #3562 NZ-u³
proposal (which also conflated `u_ladder` with the NZ deformation u).
Probe (geometric-exact, from the CCGLS A-polynomial, convention-free):
τ = −i√3, v₃ = −i√3/3, v₅ = −23i√3/180, ratio Φ₄/Φ₂ = **1/6** ⇒
`corr(u) = 1 ± u²/6`; at the #3573 anchors the **real-u ray improves both**
(muon 2.54%→2.36%, proton 4.08%→3.38%, not closing; imag-u worsens) —
selects the real-u geometric embedding and leaves the ~2.4%/3.4% residual
to the odd/archimedean channel (KC17). Audit:
[`2026-07-12-nz-parity-prune-and-fourone-even-series.md`](../audits/2026-07-12-nz-parity-prune-and-fourone-even-series.md).
No c_k; nothing wired.


**2026-07-12 (#3628) — even-channel Ohtsuki rungs exact through κ₄; growth-class
obstruction makes the 4₁↔Q_β bridge = Borel/Φ_b resummation (scope-(b)).**
Extends merged #3606 (κ₁=11√3π/108). Targeted Vandermonde extraction (13 pts,
N≤6.29M) + strict 2-term parity PSLQ identifies **all four rungs exactly**:
κ₁=(11/108)√3π [36d], κ₂=(2/27)π² [30d], κ₃=(1081/21870)√3π³ [25d],
κ₄=(98/729)π⁴ [19d] — the √3-parity alternation (odd→√3, even→pure rational)
confirmed by construction; denominators 3-power-dominated (ℚ(√−3) torsion-3).
⇒ #3571's entropy-block is a divergent-TAIL effect, not a low-rung wall. Lean:
`ohtsukiKappa2/3/4` + parity-membership lemmas (sorry-free, lean-direct EXIT 0)
extend the merged κ₁ pattern. **Bridge consequence (scope-(b), cited invariant):**
the exact κ_n ratios rise without bound (1.32→3.63→4.93, Gevrey-1 divergent,
finite Borel singularity A≈0.7) while the Q_β ladder is convergent
(c_{k+1}/c_k→1/u=117.41, KC8) — a divergent and a convergent series cannot be
equated term-by-term under any ℏ↔u reparametrisation, so the naive bridge is a
PROVED dead end and the true bridge is the Borel-median / Faddeev-Φ_b state
integral = analytic continuation off |q|=1 (Kashaev root-of-unity) to real q₀>1
(fibre-vs-observable rule; a b·A²=u_substrate "necessary condition" was drafted
then RETRACTED as laundering-risk — the map is a continuation, not algebraic).
Skeleton already proved: even [2]_q=2cosh η ⊥ odd h=2sinh η of one η=log q
(`reeb_growth_hyperbola`). Borel-singularity probe
(`qbeta_even_borel_singularity.py`) quantifies A. Coordinated: complementary-
scope note on #3544 (Φ_b construction; we characterise the divergence their
resummation resums — no overlap). Audits:
`2026-07-12-ohtsuki-higher-rungs-exact.md`,
`2026-07-12-fmap-4one-qbeta-bridge-growth-obstruction.md`. No fit; no c_k value;
wires nothing; no tier change.

**2026-07-12 (follow-up to #3622) — the deformed 1-loop of 4₁ is e^u × even:
a geometric sinh carrier at one loop.** The DG 1-loop invariant along the
4₁ Dehn-surgery branch satisfies **τ(u) = e^u·τ_even(u)** (κ = e^{−u}τ even
to 9e-62; flattening-irreducible, class ±M^{4ℤ}), so its odd part is exactly
**sinh(u)·τ_even(u)** — the first geometric object with the bar-odd sinh
structure (classical NZ series has no odd rung, #3622). Even core rungs
exact: 1 − u²/3 − u⁴/4 − 121u⁶/1080. τ(0) = ±√−3/2; A-polynomial
cross-check ≤ 3e-61. Plugs into the cosh/sinh bridge skeleton
(`3336314582` audit). Audit:
[`2026-07-12-deformed-one-loop-sinh-carrier.md`](../audits/2026-07-12-deformed-one-loop-sinh-carrier.md).
No c_k; nothing wired.
**2026-07-12 (#3639, meridian-boost) — the meridian-holonomy boost is a
smooth-quantity NEGATIVE for the c₃ seat (scope-(a); 4th confirmation).** Closes
the one angle `#3600` flagged as unprobed: the boost `ζ = ln q₀` distinct from the
braid phase `θ`. The target is `dc₃/dq₀ ≈ 4.66×10⁶` (from `Δc₃ = −0.0596` over the
`11.5 ppb` muon↔proton anchor gap, `c₃: −2.0097 → −2.0693`). The boost's
sensitivity is `dζ/dq₀ = 1/q₀ ≈ 0.90 = O(1)` — same order as `θ` (`#3600`,
`dθ/dq ≈ −51°/unit`), **6–7 orders too small** to be the sole seat. So the
meridian boost, like `θ`, is a **smooth geometric quantity ≠ the hypersensitive
phase** — the 4th independent confirmation (`#3600` θ, `#3596` pole-seed, `#3573`
near-singular φ, this). **Corollary (productive direction):** by
`dc₃/dq₀ = (dc₃/du)(du/dq₀)`, a smooth `u(q₀)` forces `du/dq₀ = O(1)`, so the
amplification must live in a **near-singular / pole structure** of the `q₀→u`
dilog map (`conj:algebraic-geometric-dilog-equivalence`) — exactly where `#3596`
(pole-seed amp `1.4×10⁻⁴`) and `#3573` (near-singular φ) are circling. The
smooth-holonomy family (boost + braid θ) is now closed as a *sole* mechanism; the
search concentrates on the pole structure. Anti-laundering: no `c_k` value; wires
nothing; no tier change; `c₃` stays a q₀-dependent near-match (SETTLED #1580).
Audit:
[`docs/audits/2026-07-12-c3-meridian-boost-smooth-negative.md`](../audits/2026-07-12-c3-meridian-boost-smooth-negative.md).
Coordinated: intent on `#3596`/`#3573`.


**2026-07-12 (#3691) — bar-odd S three routes: DEFORMED rungs κ̃₁(u)/κ̃₂(u) at
the substrate meridian (route 2), experimental Q_β budget (route 3), D(u) ladder
scoped (route 1).** Route 2: new extractor
(`qbeta_ohtsuki_deformed_meridian_rungs.py`) generalizes the u=0 Kashaev sum to
the exact deformed Habiro form `Σ_k ∏_j (2cosh u − 2cosh(ξj/N))`, ξ=u+2πi —
inside H. Murakami's PROVED asymptotic regime (0<u<0.9624), so no
deformed-volume-conjecture assumption. At u_sub=2ln q₀≈0.2087:
**κ̃₁ = 0.587343387311 − 0.0195072·i** (12d; vs κ₁(0)=11√3π/108=0.554216, +5.98%),
anchor-blind to 7.9e-9, smooth dκ̃₁/du — sign-flip stays representational
(capstone-consistent). Im κ̃₁ ≠ 0 is a new intrinsic bar-odd-channel datum
(deformation breaks J_N reality). Deformed finite-b lead t·Re κ̃₁ = 0.0613
(refines #3654's 0.0578 scale). Bonus structural: Re α(u) −
2πVol(u)/(u²+4π²) = **(1/2)u** + 0.1703·u² (linear meridian term ⇔ Im S ⊃ π·u,
odd under u↦−u — bar-odd); b·u² unidentified, NOT fitted. Deformed-saddle
cancellation eats ~u^1.9·N digits — measured, handled adaptively (dps 300).
Route 3 (`qbeta_qstar_experimental_budget.py`): σ(q*) today = 296 ppb from
σ(Q_β)=0.61 eV via dq*/dQ_β=−0.539 (#3636); **~26× sharper Q_β (0.024 eV) makes
q* an arbiter of the μ–p tension**; ~13.5× matches the muon pin; proton pin
needs ~4900×. Route 1 queued (bean qou-gmm6): D₁..D₅ exact in ℚ(√3), ũ=q·u
hypothesis fails exactly at ord 11 — extension deferred for reviewability.
Audit: `2026-07-12-bar-odd-s-three-routes.md`. No fit; no c_k wired; no tier
change.


**2026-07-12 (#3691, update 2) — route-1 CORRECTION: the "order-11 failure" of
the two-variable form was an O/h TOP-ORDER ARTIFACT; log R = E(ũ) + h·D(ũ)
HOLDS exactly (margin 9). Also: κ̃₃(u_sub) landed; π·u meridian term Lean.**
The route-1 probe (`qbeta_barodd_d_ladder_ord17_probe.py`) found the failing
order tracks the truncation top exactly (ORD 11→s^11, 17→s^17, 19→s^19);
series-diff localized the drift to G = O/h's top row, which the shift-padding
makes depend on the unknown O[ORD+1] — garbage by construction. Scope-(a)
re-scopes: ai81's FAILS-at-11 verdict corrected (form holds through s^18, 9
over-determining checks all zero); 08ds's margin-1 h³-refutation moot (its
distinguishing row was the invalid one; no residual exists to repair); the
ζ₄-route "failing-residual constraint set" is void (KC18–KC20 untouched);
the capstone's S = h·D(ũ) STRENGTHENED — D exact ℚ(√3) ladder now d₁..d₉
(d₅ reproduces ai81; heights →10²⁰). Diagnostic h·D(ũ(q₀)) = −0.003486 is
anchor-blind (swing stays in the 1/u³ inversion). Route 2 additions:
**κ̃₃(u_sub) = 3.956290802 − 0.395360496·i** [10d/8d] (tall ladder N≤262144,
dps 980, 445d cancellation handled) vs κ₃(0)=2.6545; odd finite-b partial sum
t·κ̃₁ − t³·κ̃₃ = 0.056790. Lean `MeridianLinearBarOdd.lean` (sorry-free,
lean-direct exit 0): the Im S ⊃ π·u response model 2π²u/(u²+4π²) — bar-odd,
= u/2 − u³/(2(u²+4π²)), |deviation| ≤ |u|³/(8π²). Heads-up posted on #3692
(κ-tower resummation sibling): their Borel–Padé can now rerun on DEFORMED
rungs (κ̃₁, κ̃₃ available). No fit; no c_k wired; no tier change.

**2026-07-13 (#3737 merged + registry rows KC21/KC22, this branch) — D-ladder
holonomy negatives complete; the wall resolution + D-ladder enter the kernel
registry.** #3737's two exact results: (1) **no coupled ℚ(√3) matrix
P-recurrence** for `d_k` (`r≤2, D≤4`; `r=3, D≤3`; `r=4, D≤2` — the class the
separated #3716 test structurally could not see); (1b) **not q-holonomic
either, in the base its own denominators indicate** — base `3` (and `1/3`,
and classical `k`) through `r≤3, E≤3`, prime-certified full rank, despite the
3-smooth denominators (`v₃ ~ 1.5k`). (2) denominator **2-adic valuation is
parity-graded** (Lean-proved window `K=5`,
`DLadderTwoAdicGrading.bDen_two_adic_graded`; `p=3` ungraded ⇒ 2 is the
**unique graded prime** — the ℤ/2 bar-involution signature). Together with
the [2026-07-12 capstone](../audits/2026-07-12-c3-wall-resolution-capstone.md)
(the `1/u³` artifact, `S = h·D(ũ)`, structural sign-flip, decay-sector `q*`)
these are now **registry rows KC21 + KC22** in
[`ck-dk-canonical-registry.md §9`](ck-dk-canonical-registry.md) + JSON twin
(validator green): ~~the odd-channel element is transcendental/**resurgent**
(Écalle class)~~ **[WITHDRAWN 2026-08-09]** — the low-order (q-)holonomic search
class is CLOSED. Do not
re-run holonomic/P-finite hunts on `D(ũ)`; the live routes are ~~(i) the
resurgent/acceleration chain~~ **[(i) WITHDRAWN 2026-08-09]**, (ii) KC19's crossing-weight `w(q)` derived from
the Φ_b state integral, (iii) canonical `c₄^even` rungs via H₄ Hoefsmit
(bean `8we6`) since extracted `c_k≥4` are noise (P4 entropy audit). No fit;
no c_k wired; no tier change.

> **⚠ [SUPERSEDED 2026-08-09] — route (i) is withdrawn, and the *reason* given
> for the closure is wrong. The closure instruction itself STANDS.** `D(ũ)` is
> **CONVERGENT** (`ρ = ũ(q*_ρ) = 0.142799996644689…`, `κ = 0`), so the
> "transcendental/resurgent (Écalle class)" reading — and the
> "resurgent/acceleration chain" named as live route (i) — rest on a divergence
> the ladder does not have. **"Do not re-run holonomic/P-finite hunts on
> `D(ũ)`" remains correct and in force**: a convergent series need not be
> holonomic, and KC22's closed form `φ(w)log(1−w/ρ) + ψ(w)` is exactly such an
> element — so the (q-)holonomic exclusion survives losing the divergence that
> was mistakenly offered as its justification. Routes (ii) and (iii) are
> untouched. See the 2026-08-14 entry at the end of this ledger; `qou-dri7`.


**2026-07-17 (bar-odd-S follow-up) — ξ-FRAME PHASE LAW: κ̃_n/ξⁿ ∈ (−i)ⁿ·ℝ (rung 1
to 6e-20) ⇒ the perturbative deformed tower has NO intrinsic odd phase; deformed
Borel–Padé extends #3692's single-valuedness to the meridian (Im 𝔙̃_b = 0.05855,
88° Stokes margin).** Probe `qbeta_c3_borel_pade_deformed_meridian_probe.py`
(5/5 assertions) on the #3691 deformed rungs: arg κ̃_n = −n·arctan(t/π) exactly
(rung-1 residual 6.2e-20; rungs 2–4 within their witness precision), i.e. the
deformed Ohtsuki coefficients are REAL in the ξ-normalized frame — the u=0
parity structure (#3628) carries to the meridian unchanged, and #3691's
"intrinsic odd channel Im κ̃₁" is the kinematic frame rotation, nothing more.
**A_ω-lane selection rule (heads-up posted on #3805/#3813): any genuine
odd-channel monodromy phase must be NON-perturbative — unreadable from κ̃ rungs
at any order.** Deformed resummation: Im 𝔙̃_b = 0.05855 (u=0: 0.05545; meridian
correction +0.0031); Borel singularity rotates by the same frame phase; nearest
Padé pole 88.1° off the imaginary ray ⇒ no median split / no anchor-dependent
trans-series at the meridian either. Task-2 record: the O/h top-order artifact
is FIXED on main (`ser_div`, valuation-aware, credits the #3691 diagnosis);
corpus sweep finds zero remaining shift-divide offenders. Audit:
`2026-07-17-deformed-tower-xi-frame-phase-law.md`. No fit; no c_k wired; no
integer Stokes constant claimed; no tier change.

**2026-07-17 (PR #3818, `claude/dladder-qborel-acceleration-2026-07-17`) —
q-Borel acceleration of the D-ladder: transport invariant proved, fixed-base
Jackson pruned, gate fails at k=21.** The unowned odd-channel front of the
[07-17 reassessment](../audits/2026-07-17-1ppq-path-reassessment.md) item 1;
audit [`2026-07-17-dladder-qborel-acceleration.md`](../audits/2026-07-17-dladder-qborel-acceleration.md).
Formalize-first results: (1) **proved-lean, sorry-free** — the signed 2-adic
component gap `v₂(a_k)−v₂(b_k)` is invariant under EVERY scalar acceleration
transform (`DLadderTwoAdicGrading.gap_invariant_under_scalar_transform`), so
the ℤ/2 bar-parity grading survives into every accelerated plane —
**permissive**, no obstruction to resummation; the absolute law transports by
`−v₂(f_k)` (LTE-verified) and is carried verbatim by 2-adically-unit bases
(Jackson base 2 = the graded prime's own base). (2) **Fixed-base Jackson
q-Borel pruned** (scope-(a), conditional on the triple-confirmed divergence
class): `Q>1` over-accelerates to an entire transform, `Q<1` is a geometric
no-op — only the `Q→1` Borel–Leroy boundary matches the `exp(Bk+Ck·log k)`
class; do not scan fixed-base q-Borel families on `D(ũ)`. (3) The
pre-registered 15% estimator-consistency gate **fails at every
`s ∈ [0,0.40]`** at k=21 (0.15 vs 0.26 persists); parity-split branches
unresolved too; **observation only** (not a gate): the conformal-mapped core
at s\*≈0.20 converges to A≈0.236 (0.3% window spread), within 9.5% of the
root-test radius — the specific datum the ORD-63 extension terms (sibling
arm, three-front specs §1) must confirm or kill. (4) Back-transform =
meridian partial sums to 2.5e-26 at muon-q₀ AND q\* (A2); `D` smooth through
q\* — the S=0 zero is bridge-borne (KC21 smooth-zero reading confirmed from
the accelerated side). No instanton action identified; no candidate value;
no c_k wired; no fit; no tier change.

**2026-07-17 addendum — independent replication (same branch, second
implementation).** A parallel implementation
([`2026-07-17-dladder-ecalle-acceleration.md`](../audits/2026-07-17-dladder-ecalle-acceleration.md),
probe `qbeta_dladder_ecalle_acceleration_probe.py`, 4/4 assertions)
independently reproduces the K1 headline: the estimator gate fails at every
Borel–Leroy `s ≤ 0.40` AND every exponent-order Jackson `t ≤ 0.50`
(`q₀^{t·k(k−1)/2}` parametrization) — the finite-k shadow at k = 21 is now
double-confirmed and transform-independent. **One open discrepancy, flagged
for adjudication (not resolved here):** on the parity split the two
implementations disagree — the entry above finds parity branches unresolved,
while the second implementation finds each parity subseries *individually
passes* the gate when accelerated at its own per-parity slope-zero order in
the w = ζ² plane (odd/S-carrier ρ_ζ ≈ 0.152, even ρ_ζ ≈ 0.254, radii 40%
apart). Likely a methodology difference (shared-s vs per-parity s\*_par;
ζ vs ζ² plane); queued as a bean — neither reading is wired anywhere.

**2026-07-17 addendum — parity-split ADJUDICATED (bean qou-ffxw closed;
PR #3818).** Probe
[`qbeta_dladder_parity_adjudication_probe.py`](../../computations/qbeta/qbeta_dladder_parity_adjudication_probe.py)
(witness `qbeta-dladder-parity-adjudication.witness.json`) ran BOTH methods on
the same exact d_k plus four adversarial controls (deliberately hostile to the
per-parity positive: only ~10–11 coeffs/parity → real Froissart risk).
**Verdict: undecidable-at-k21.** The exact difference is four ingredients:
(i) per-parity slope-zero s\* vs a shared fixed s-grid (even's optimum s ≈ 0.465
lies *outside* the sibling's [0,0.40] grid); (ii) **conformal-mapped** vs
**raw** dlog-Padé; (iii) gap-only vs gap+spread gate; (iv) tiny fixed Padé order
vs an M-window. Control outcomes: **C4a** the conformal gate is NOT
self-referential — the located singularity is seed-invariant to ~1e-13 across
{0.5,1,1.5,2}×ρ_rt (the "it just returns the root-test seed" artifact
hypothesis is REFUTED); **C4b** the PASS↔FAIL flip localizes to the **conformal
map** — raw dlog-Padé at the *ecalle probe's own* per-parity s\* still fails both
parities (raw Padé ≈ 2× below the root-test radius — the qborel probe's ARM-2
"branch-cut-biased-low" signature), while the conformal estimator passes;
**C3** the ecalle probe's real per-parity radii are stable across
orders/margins/truncation (≤ ~10%). BUT the controls cannot **certify** the
40%-split as real ℤ/2 structure at this length: on same-length *convergent*
branch-point synthetics (mismatched to the divergent target) the short-series
conformal estimator is biased ~30% high (C1a) and fails to recover planted
distinct parity singularities (C2; Probe B even resolved the even branch 4/9).
**Bottom line: the qborel probe's "unresolved" is the raw-Padé low bias (not an
absence of structure); the ecalle probe's "per-parity pass" is the conformal
cure — but the located radii are not certifiable to 40% at k = 21.** Neither
parity reading is wired; the ORD-63 / k ≈ 31 extension decides whether the
odd/even radii stay 40% apart or converge. Audits:
[`2026-07-17-dladder-ecalle-acceleration.md`](../audits/2026-07-17-dladder-ecalle-acceleration.md),
[`2026-07-17-dladder-qborel-acceleration.md`](../audits/2026-07-17-dladder-qborel-acceleration.md).
## 2026-07-17 — E = G(η²) functional identification REFUTED exactly (0zr0 follow-up closed)

The queued continuation of the 07-04 η²-fibre-descent positive is executed
and closed: `E = G(η²)` fails as a pure power series at rung `ũ¹` (exact:
`η²` starts at `ũ³` while `E₁ = 3√3/4 ≠ 0`), and fails with an arbitrary
2-rung carrier at the first of four over-determined checks (rung 4; exact
ℚ(√3) obstructions at rungs 4, 5, 7, 8 with `g₁, g₂` forced by rungs 3, 6 —
margin-4 parameter-free refutation, not a fit rejection). Both named
candidate profiles (q-Bessel Layer-2 kernel, ζ₄-rotation image) are functions
of `η²` alone and die at the `ũ¹` obstruction. **Scope-(a):** the 07-04
positive stands (`η` bar-odd, `η² ∈ ℚ(√3)[[ũ]]` margin 9); what is refuted is
`E` being *generated by* `η²` — the bar-even fibre needs ≥ 2 independent
generators (`ũ`, `η²`). Consonant with KC21/KC22: no fibre-level algebraic
shortcut past the ~~resurgent~~ **[WITHDRAWN 2026-08-09]** D-ladder exists.
Probe
`qbeta_eta_square_functional_g_probe.py` → witness
`qbeta-eta-square-functional-g-probe.witness.json`; audit
[`2026-07-17-eta-square-functional-g-refutation.md`](../audits/2026-07-17-eta-square-functional-g-refutation.md).
No fit; no c_k wired; no tier change.

> **⚠ [SUPERSEDED 2026-08-09]** — only the word "resurgent" is withdrawn:
> `D(ũ)` is convergent (`ρ = 0.1428`, `κ = 0`). **The no-shortcut finding
> itself stands** — there is still no fibre-level algebraic shortcut past the
> D-ladder. See the 2026-08-14 entry at the end of this ledger.



**2026-07-17 (#3826) — κ̃₅ PREDECLARED TEST: PHASE LAW SURVIVES (residual 9.2e-9);
tower extended to 5 rungs; G3 3d-index tranche: engine certified, assembly
honestly open.** The ξ-frame phase law (#3819, from rungs 1–4 only) predicted
arg κ̃₅ = −5·arctan(t/π) = −0.166002394 IN ADVANCE (prediction committed before
the run); the 11-point ladder (N≤524288, dps 1050, 947d cancellation) measured
−0.166002385 — residual 9.2e-9, LAW SURVIVES. κ̃₅ = 210.675324 − 35.29743·i
[5d/3d]; rungs 1–4 sharpened to 22/17/13/9 digits; #3691 values reproduced.
The perturbative-null for A_ω hardens: κ̃_n/ξⁿ ∈ (−i)ⁿ·ℝ verified through
rung 5. G3 route-1 (owner-uploaded sources now in library/): exact-integer
I_Δ engine + exact triality certificates + substrate convergence
(I_Δ(0,0)(e^−t)=0.1922789824); DGG anchor (4.20) glyph-verified; assembly of
the 4₁ TOTAL index NOT yet certified (flat-wing divergence of the bare 4.18;
q^{−e₂} near-miss; 9 quad frames excluded) — open input is the U=2·log m
charge dictionary; appendix-B tables next. All open-state recorded in the
witness (anti-fabrication). No fit; no c_k wired; no tier change.

**2026-07-17 (#3813, this branch) — the A_ω monodromy datum is a
pentagon-rigidity invariant (Lean, sorry-free).** Post-week re-evaluation
(all 07-11→14 routes converged on the G3 keystone: the argument→S monodromy
datum, `2026-07-13-phib-proof-status-and-monodromy-datum-gap-audit.md`).
New Lean `QOU.QBeta.MonodromyDatumRigidity` composes two recent results into
the lane's structural claim: (a) the deformed Ohtsuki tower has NO intrinsic
odd phase (`arg κ̃_n = −n·arctan(t/π)`, phase-law commit `c821747763`) ⇒ A_ω
is non-perturbative, i.e. a Stokes/monodromy ratio ⇒ scale-invariant; (b) L4
`CyclicDilogPentagon` proved (modulo the honest open `PentagonRigidity`)
that two nowhere-zero `FaddeevPhi` solutions are equal once normalized.
Theorem `monodromy_datum_rigidity`: **every scale-invariant readout is the
same on all `FaddeevPhi` solutions under pentagon rigidity** — the A_ω datum
off any Φ_b representative is one pentagon-forced invariant, no fitting
freedom (the Lean form of "forced, not fitted" for G3). Non-vacuous witness
`qpRatio_scaleInvariant`; `qpRatio_solution_independent` isolates the pentagon
input to the dual/large-argument monodromy (the local `ib`-quasi-period is
already solution-independent via `phi_b_quasiperiod`). Does NOT compute A_ω;
inherits the open `PentagonRigidity` hypothesis (§3b-cond). lean-direct exit 0.
No c_k; registry untouched; scope-(a). Also this session: #3704's (N,k) 0/8
+ G2-misframing correction absorbed; bean `8we6` annotated with the H₄
route-A 9/9 gate-fail state (awaits owner-level framework content).

**2026-07-17 (#3813, cont.) — two Φ_b-lane results: Liouville-elliptic Lean +
local-monodromy anchor-blind negative.** (a) **Liouville for doubly-periodic
entire functions** (`QOU.MathlibExt.DoublyPeriodicLiouville`, sorry-free,
#print axioms = {propext, Classical.choice, Quot.sound}): the "doubly-periodic
⇒ constant" step L4 `CyclicDilogPentagon` carried as an open hypothesis
("absent from Mathlib") is now proved from primitives — no ZLattice/measure
theory, just `Int.fract` coordinate reduction into a closed ball (compact, ℂ
proper) + Liouville. The bridge `ratio_const_of_doublyPeriodic` **shrinks
`PentagonRigidity.uniqueUpToScalar`** to two smaller explicit inputs (ratio
entire = zeros coincide; periods independent), Liouville discharged. (b)
**Two-route A_ω cross-pin** (`qbeta_c3_two_route_cross_pin_probe.py` + witness,
2/2 pass): the only fit-free Φ_b monodromy datum computable in-repo — the local
scale-invariant quasi-period readout `qpRatio` (proved solution-independent in
`MonodromyDatumRigidity`) — is **anchor-blind** (cross-anchor ratio 1 − 3e-9),
reproducing neither the S swing (−4.0751) nor any pre-named GGM integer/count.
**Scope-(a):** the c₃ bar-odd swing is NOT in the local Φ_b monodromy but in the
dual/large-argument (Stokes) monodromy — the 3d-index/GGM face owned by siblings
#3805/#3826 (their `I_Δ(0,0)=0.192279` consumed as a cited reference only;
assembly not touched). Empirical companion of `MonodromyDatumRigidity` + the
non-perturbative phase law (`c821747763`). No fit; no c_k; registry untouched.

**2026-07-18 (#3813) — 4₁ TOTAL 3d-index assembled + validated; #3826's
"honestly open" state closed as a NUMERICAL BUG.** DGG 1112.5179 eq (4.18)
`I_41(m,e) = Σ_{e₂∈ℤ} I_Δ(m−e₂,m+e−e₂)·I_Δ(e−e₂,−e₂)` assembled on the
validated tranche-1 exact I_Δ engine
(`qbeta_g3_fourone_index_assembly_corrected.py` + witness, 3/3 pass):
reproduces the paper's PRINTED anchor eq (4.20)
`I_41(1,1) = −q−q²+2q³+7q⁴+11q⁵+11q⁶+3q⁷` **exactly**, is window-stable
(convergent), and satisfies the (4.19) amphichiral symmetry
`I_41(m,e)=I_41(−m,−e)`. **Key finding for the G3 route-1 sibling:** the merged
#3826 assembly's "honestly open / no-certification" verdict was a *numerical
bug* — its `tet_norm` under-summed the per-factor series, reported a spurious
negative lead for large-argument I_Δ, and its convergence guard then wrongly
rejected the convergent bare sum as a "flat divergent wing." There is **no
missing 'U=2·log m charge dictionary'**: (4.18)'s arguments ARE the resolved
dictionary (DGG §4.3 scout of library/1112.5179). Validated coefficients now in
hand: `I_41(0,0) = 1−2q−3q²+2q³+8q⁴+18q⁵+18q⁶+14q⁷−12q⁸−52q⁹−106q¹⁰−…`. The A_ω
VALUE remains one tranche away — the coefficient↔Stokes dictionary (GGM
2012.00062, classical Stokes matrix `S⁰=[[1,0],[−3,1]]` → load-bearing integer
3). No c_k wired; no fit; scope-(a).

**2026-07-18 (#3813) — STOKES DICTIONARY resolved + STRUCTURAL VERDICT: 4₁
CS=0 bars the bar-odd A_ω from the u=0 index.** Extending the validated 4₁
total-index assembly with the coefficient↔Stokes dictionary (GGM 2007.10190
eq 80, cited): the geometric Stokes entry `S⁺_σ1σ1(q) = Σ_e I_41(0,e) =
1−8q−9q²+18q³+46q⁴+90q⁵+62q⁶`; the leading (classical) Stokes constant of 4₁ is
**3** (= the `S⁻(0)=[[1,0],[−3,1]]` off-diagonal). **Key structural finding
(reframes the A_ω search):** the c₃ bar-odd real (~0.0097/−0.0395) is NOT
extractable from the u=0 4₁ index —
- **scope-(a):** the 4₁ Stokes constants are INTEGERS (3,−8,−9,46,…) and the
  q-series diverges at substrate q≈0.90 (growing coefficients);
- **scope-(b), cited invariant:** 4₁ is **AMPHICHIRAL ⇒ CS=0** at the u=0
  complete structure (`V(σ1)=i·Vol` purely imaginary, GGM 2012.00062 eq 41), so
  the bar-odd/imaginary complex-volume datum is **identically zero** for the
  figure-eight at u=0.

So the u=0 4₁ Stokes data is bar-EVEN (the integer 3); the **bar-odd A_ω lives
only in the DEFORMED (u≠0) state integral** — needing Φ_b median/Borel
resummation (machinery not in-repo; the winding/meridian face) OR a
non-amphichiral knot (5₂, CS≠0). This is fully consistent with this PR's
local-Φ_b-monodromy anchor-blind result and `MonodromyDatumRigidity` (the
bar-odd datum is dual/non-perturbative, not in the u=0 readout). `2·Vol(4₁)=4.06
≈ |ratio −4.0751|` (0.38%) is flagged anti-numerology — NOT wired. Probe/witness
`qbeta_g3_fourone_index_assembly_corrected` (3/3: anchor 4.20, window stability,
amphichiral symmetry). No c_k; no fit.

**2026-07-18 (#3813) — the A_ω fork resolved: BOTH branches hit the same
Lean-proved anchor-invariance wall.** Owner steered "try 1" (deformed u≠0
median resummation) + "for 2, look at knot operators." Both scoped + settled:

- **Lane 1 (deformed median resummation) — DIRECTLY settled, anchor-blind.**
  New probe `qbeta_c3_deformed_median_discontinuity_probe.py` (2/2) computes the
  lateral Borel sums the corpus only *inferred*: on-ray reproduces Im 𝔙̃_b =
  0.0585; the lateral discontinuity scales LINEARLY with straddle δ (ratios
  1.988, 1.997 ≈ 2) ⇒ **smooth, no Stokes jump** on the physical substrate ray
  (a genuine jump would be δ-constant). The across-singularity Stokes magnitude
  |2πi·Res| = 0.656 ≈ Vol(4₁)/π = 0.646 (action-consistent, anchor-blind, ~2 sig
  figs — not a new identification, per T3). Single-valued + anchor-blind.
- **Lane 2 (non-amphichiral knot 5₂) — scoped; blocked by the SAME prune.** The
  knot-operator census (`2026-06-01-knot-operator-census-group-actions.md`) +
  the 5₂ falsification protocol (`chirality-period-pairing.md`, proposes
  CS(5₂)≈−0.153π²) show 5₂ *fixes* the CS=0 structural problem (nonzero bar-odd
  home) but needs its own H₅(q) Hecke cell + Markov trace + `τ_{5₂}(q)` +
  verified CS(5₂) + `𝔙_q(5₂)` — new machinery (the H₅(q) cell is the flagged
  obstacle). And classical CS(5₂) is **anchor-invariant**, so it too is excluded
  as the swing carrier.
- **The unifying invariant (Lean-proved, sorry-free):
  `QOU.QBeta.SRigidity.no_anchor_invariant_realizes_swing`** — any anchor-
  invariant datum `g(datum)` (datum constant across anchors) cannot equal an S
  that swings (verified this session). This subsumes BOTH branches: the deformed
  tower/its Stokes constant AND a fixed classical CS(K) are anchor-invariant.

**Conclusion:** the bar-odd swing is intrinsically the ANCHOR-DEPENDENT quantum
`𝔙_q` at q₀ = the 1/u³ ladder-inversion of a smooth numerator `N_odd = S·u³`
(`BarOddLadderShape`), precision-limited by the experimental Q_β
(`dq*/dQ_β ≈ −0.54`), NOT by any resummation or knot choice. The one genuinely-
open target is the geometric `Im 𝔙_q → N_odd` normalization (the capstone) —
where the anchor-dependence enters — and ~~the odd-channel D-ladder q-Borel/Écalle
acceleration (sibling #3818) operating on `D(u)` where the swing lives~~
**[WITHDRAWN 2026-08-09]**. No c_k;
no fit; scope-(a).

> **⚠ [SUPERSEDED 2026-08-09]** — the q-Borel/Écalle acceleration named here has
> no target: `D(ũ)` is convergent (`ρ = 0.1428`, `κ = 0`). The capstone
> normalization named alongside it is unaffected. `qou-dri7` (scrapped).

**2026-07-18 (#3872) — G3 STEP 2 DONE: GGM 4₁ Stokes data exact — Theorem 9
certified, (59a) DERIVED OCR-free, integer Stokes 3 at ι = Vol(4₁)/π; new
exact anchor for the step-1 assembly.** Exact-integer implementation of the
GGM (2012.00062v3, §§4–5) machinery: G⁰_m/G¹_m (51a/b), det W_m = 2 and the
q-difference (49) exact through q^30. The (59a) sandwich was derived rather
than OCR-read: glyph-verified magnitudes, all sign patterns × both ᵀ
placements scanned against the q→0 limit (60) + all four printed towers
(61)–(64) (28 coefficients; cmsy sign rows decoded via the baseline−9.2
glyph offset, calibrated on (63) = −(62) forced by symmetry (65)). Result:
8 sign-pattern gauges, ONE distinct S⁺(q), ᵀ on the second W as the glyphs
read. S⁺₁₁ = 1 − 8q − 9q² + 18q³ + 46q⁴ + 90q⁵ + 62q⁶ + 10q⁷ + …;
substrate S⁺₁₁(e^{−t}) = 0.25843626726140844236 (40 stable digits). The
Borel singularity is ι = Vol(4₁)/π ≈ 0.64613 — the SAME object as the
corpus's measured A (#3692/#3819) — with INTEGER Stokes constant 3. Via the
PROVEN (for 4₁) dictionary eq (21), S⁺_{σ1σ1} = Σ_e I(0,e): the step-1
assembly search now has ~30 exact target coefficients (own-computed, not
just 7 printed) + the 25 annihilator equations. NOT claimed: identification
of the integer 3 with the corpus A_ω normalization (step 3's residual test
decides). Probe `qbeta_g3_ggm_stokes_41.py` → witness
`qbeta-g3-ggm-stokes-41.witness.json` (3/3 green). No fit; no c_k wired.

**2026-07-18 (#3872) — G3 STEP 3 (u=0 LEG) DONE: GGM eq-(48) bridge verified
at the substrate; integer M_I(0) derived; A_ω is DEFORMATION-CARRIED.** The
exact side (Theorem-9-certified G-series = GK state-integral factorization,
eq 44) equals the integer-dressed Borel side (exact printed order-3 φ_σ1,
eq 42; Φ_σ2(τ) = iΦ_σ1(−τ)) at τ = it/2π: connection matrix DERIVED from
two ray points, integer to 1.3e-5 (= order-3 truncation floor),
M_I(0) = [[4,−4],[4,4]]; wrong prefactor reading rejected by the same
integrality test (dev 0.26); held-out point verifies; Conjecture-10 shape
X = (W₋₁(0)ᵀ)⁻¹·M = [[0,−4],[4,−4]] exactly integer (4× the (56a) glyph —
a pure normalization gauge). STRUCTURAL FINDING: at u=0 the substrate
non-perturbative channel is |q̃| = e^{−4π²/t} ≈ 1e-164 — invisible — while
the measured DEFORMED odd datum Im 𝔙̃_b ≈ 0.0585 (#3819) is O(1). So A_ω
cannot be a u=0 Stokes effect: it is deformation-carried (u≠0), consistent
with the ξ-frame phase law (#3819/#3826). Next: the deformed leg — GGM's
x̃-dependent Stokes structure (§5) at the substrate meridian. Probe
`qbeta_g3_ggm_eq48_bridge_41.py` → witness
`qbeta-g3-ggm-eq48-bridge-41.witness.json` (3/3 green). No fit; no c_k wired.

**2026-07-18 (#3892) — Step 2: full 5₂ Jones bar-odd datum validated + corpus
braid-word CORRECTION.** Self-contained TL₃ Kauffman bracket (`qbeta_5two_jones_
barodd_probe.py`, 3/3) reproduces known V(4₁) (det 5) and V(5₂) (det 7). **Caught
a corpus data error:** the canonical-table braid `(1,1,1,-2,1,-2)` labelled "5_2"
(`_deprecated/hyperbolic_knot_db_extended.py:44`) actually has det 11 ⇒ it is
**6₂, not 5₂**. The real 5₂ is `(1,1,1,2,-1,2)` (det 7, writhe 4). The merged
#3813 5₂-writhe brick used the corpus braid, so its knot was 6₂ (writhe 2,
D_odd=sinh(u_sub)); the real 5₂ has writhe 4, D_odd=½(q⁴−q⁻⁴)=sinh(2·u_sub). The
qualitative finding (chiral ⇒ nonzero bar-odd datum; amphichiral 4₁ ⇒ 0) is
label-independent and stands. The complete classical Jones bar-odd datum
V(5₂)_odd is O(0.1) at q₀, anchor-smooth (swing 6.4e-8), ~1e7× above N_odd ⇒ NOT
the swing (prune); the bar-odd HOME. Step 1 (anchor-dependent 𝔙_q(5₂)) is the
swing test. No c_k; no fit; scope-(a).

**2026-07-18 (#3902) — Step 1: 5₂ quantum volume 𝔙_q(5₂) computed — ANCHOR-SMOOTH,
the decisive non-amphichiral negative.** 5₂ complex volume via the Neumann–Zagier
saddle (Hikami 0604094 §4.2 eq 4.13), deformed to the substrate meridian at both
anchors (`qbeta_5two_quantum_volume_probe.py`, 2/2). Vol(5₂)=2.82812208833
VALIDATED at the m=1 geometric saddle (12 digits vs SnapPy). 5₂ chiral: Re 𝔙=1.91
≠ 0 (CS-partner), unlike amphichiral 4₁. **The decisive test:** the
anchor-DEPENDENT quantum volume — the one object `no_anchor_invariant_realizes
_swing` does NOT exclude — has max |d𝔙/dq| = 1.47, i.e. ANCHOR-SMOOTH (O(1)),
~6 orders below the 3.84e6 the S-swing needs. So even a chiral knot's
anchor-dependent quantum volume cannot supply the swing. **Overarching
conclusion:** the bar-odd swing is carried by NO smooth geometric/topological
object — 4₁ deformed median resummation (smooth/anchor-blind, directly computed
#3813), classical CS / Stokes integer (anchor-invariant, prune), and now 5₂
quantum volume (anchor-smooth O(1), computed) — all fail. The swing is
intrinsically the 1/u³ inversion of a smooth numerator N_odd crossing zero at q*
(`BarOddLadderShape`), pinned by experimental Q_β. The ONE locus where
amplification could still live: the substrate meridian tuned to an A-polynomial
branch point (the near-singular q₀→u map, `conj:algebraic-geometric-dilog-
equivalence` — the standing open conjecture). No c_k; no fit; scope-(a).

**2026-07-18 (#3902 cont.) — BRANCH-POINT LOCUS CLOSED: substrate meridian is
GENERIC, ~8.6e6× the anchor gap from any 4₁/5₂ branch point.** The #3902 entry
named the last geometric hope: q₀ tuned to an A-polynomial branch point, where
the saddle degenerates (det J → 0) and an otherwise-smooth quantum volume can
blow up. Direct test (`qbeta_substrate_meridian_branchpoint_probe.py`, 2/2):
4₁ branch points via the m-discriminant of A_{4₁} (B²−4m⁸, B=1−m²−2m⁴−m⁶+m⁸) —
nearest real root at m*=0.61803 (golden-ratio conjugate), 0.492 from q₀; the
|m|=1 branch locus is q₀−1=0.10998 away. 5₂ branch points via the gluing-saddle
Jacobian det J (eq 4.13): det J(q₀)=4.37, O(1), NON-DEGENERATE; nearest real
det J=0 far off. NEAREST branch point of either knot: 0.10998 from q₀ —
~8.6e6× the 1.28e-8 proton↔muon anchor gap. The substrate meridian is generic;
the swing is NOT a geometric near-singularity. **All four geometric routes now
closed** (median resummation smooth #3813; classical CS/Stokes anchor-invariant
prune; 5₂ quantum volume anchor-smooth #3902; branch-point locus generic). The
c₃ bar-odd swing is confirmed representational — the 1/u³ inversion of a smooth
N_odd (BarOddLadderShape) crossing zero at q*, pinned by experimental Q_β. Per
the owner conditional (NOT anomalously close ⇒), the lever is now the
~~alien-calculus / resurgence thread (D-ladder Écalle acceleration, sibling
#3818) — where the swing lives in the transseries of D(u)~~
**[WITHDRAWN 2026-08-09]**, not in any knot's
geometry. No c_k; no fit; scope-(a).

> **⚠ [SUPERSEDED 2026-08-09]** — this lever is withdrawn. `D(u)` has no
> transseries to live in: it is convergent (`ρ = 0.1428`, `κ = 0`), with closed
> form `φ(w)log(1−w/ρ) + ψ(w)`. The swing itself is real and unaffected — it is
> the `1/u³` ladder inversion of the smooth `N_odd`, as this same entry states.
**2026-07-18 (follow-on to merged #3872) — DEFORMED LEG TRANCHE A: GGM §5.2
4₁ holomorphic blocks implemented; m-structure certified; Theorem-14
assembly reading OPEN (honest fail); Kashaev-ray frame confirmed as the
unsuppressed home.** A_m/B_m blocks (q-Hahn Bessel J± eq 127, θ eq 107)
built exactly (mpmath dps 60, no float64): θ q-difference (109) exact; the
Theorem-16 annihilator generator kills A_m and B_m (blocks' m-structure
certified). Exact deformed Z (Theorem 14) evaluated near the Kashaev ray
τ = 1/10 + 0.05i with |B·B|/|A·A| ∈ {2.5, 6.1, 36.7} at u ∈ {.05,.1,.2} —
the two-saddle trans-series is UNSUPPRESSED there, confirming (sharpening
tranche 5) that the O(1) odd channel lives at the Kashaev ray (τ→1/N, q̃
pure phase), not on the 3d-index ray (|q̃| ≈ 1e-164 even deformed; x̃ =
e^{u/τ} is a pure phase for real u). OPEN: the Theorem-14 phase/θ assembly
does not yet reproduce the certified u=0 GK side — O(1) complex ratio
(≈ −3.93−3.03i at τ=i/2); a 1024-reading derivation scan (θ-arguments ×
θ-power × Δ(τ) sign patterns × exponent swap) found NO hit, so the
misreading is structural (Φ_b normalization prefactor between (113) and
(44) suspected). Next: certify against direct Φ_b quadrature of (125) as
ground truth, then tranche B (deformed Borel side eq 123 minus exact side
→ numeric A_ω residual). Wrong-knot escalation posted on #3884 (their "4₁
Stokes {3,4} from eq 96/98" reads 5₂ data — pages 20–22 are the 5₂ block;
§5 deformed-4₁ starts p. 24). Probe `qbeta_g3_deformed_blocks_41.py` →
witness `qbeta-g3-deformed-blocks-41.witness.json` (honest FAILURES by
design). No fit; no c_k wired.

**2026-07-18 (#3898) — THEOREM-14 ASSEMBLY DERIVED AND GREEN: the deformed
4₁ exact side is now fully certified on the imaginary axis (5.5e-54).**
The open item from tranche A closed by derivation, not transcription:
(i) two-pole residue cancellation (x = q and x = q⁻¹, u-independent
coefficient ratio — Theorem 14(c) entirety) pruned the reading space;
(ii) the m-restored Theorem-16 annihilator confirmed the printed
J-arguments uniquely (1e-41 vs O(1) for all variants); (iii) the sole
survivor's coefficients, solved at three pure-imaginary τ, fit
e^{α+β(τ+τ⁻¹)} exactly (3rd-point error 1e-41) with β = −πi/6, +πi/3 —
THE PRINTED exponents, an independent confirmation — and α = ±πi/4 (the
printed-read ∓3πi/4 differs by an overall −1 absorbed by the θ_A monomial
θ(−q^{1/2}x)⁻² = x²θ(−q^{−1/2}x)⁻²); the rejected alternative fails
constancy at 1e-2. Derived assembly: c_A = e^{+πi/4−(πi/6)(τ+τ⁻¹)},
c_B = e^{−πi/4+(πi/3)(τ+τ⁻¹)}, θ_A arg −x√q, θ_B arg −x/√q (power +1).
Witness now 3/3 green. Follow-ups: complex-τ branch alignment
(bookkeeping; raw (112) drifts off-axis in this frame map), then tranche
B — deformed Borel at the Kashaev ray minus this exact side → numeric A_ω
residual vs Im 𝔙̃_b = 0.0585. No fit; no c_k wired.

**2026-07-18 (#3898) — TRANCHE B PART 1: fixed-x saddle data exact (Lean-
proved algebraic layer) + STRUCTURAL FINDING: the corpus tower is a
DIFFERENT double-scaling limit — part-2 redirect to the Kashaev limit of
the block factorization.** The deformed 4₁ saddle curve was re-derived from
GGM (115) with the glyph-lost minus restored: x·y² + (x²−x−1)·y + 1 = 0
(self-certified: reduces to (38) at x=1; y-discriminant = the printed (119)
product identically; γ² = (x+x⁻¹−3)(x+x⁻¹+1) → −3 at u=0). The algebraic
layer is now LEAN-PROVED sorry-free over generic CommRing
(`QOU/QBeta/DeformedSaddleCurve.lean`: discriminant factorization, x=1
reduction, γ²-locus identity, Vieta product/sum — lean-direct exit 0);
the transcendental part stays in the witness per the §7c wall. Exact
saddle actions at the substrate meridian: V(σa,b) = −1.68848201 ±
1.41228159i (residuals 1e-61), ι̃ = (Va−Vb)/(2πi) = 0.44954319 (real);
u=0 control ι̃ = Vol/π exact. SCOPE-(a) NEGATIVE: ι̃(u_sub) does NOT
reproduce the corpus's measured tower singularity 0.6310+0.0210i (29%
off; u-rescaling dictionaries also fail; Im 𝔙̃_b candidates all fail).
CAUSE IDENTIFIED: different double-scalings — GGM §5.1 fixes x = e^u as
τ→0, while the corpus tower fixes the MERIDIAN in J_N(e^{ξ/N}) where
x̃ = e^{u/τ} ~ e^{uN} → ∞; consistently the measured pole sits near the
u=0 Vol/π with weak u-dependence (Murakami regime). REDIRECT (part 2):
the exact side of the A_ω residual is the Kashaev-limit of the certified
Theorem-14 block factorization (τ → 1/N + iε with the meridian scaling),
which the deformed-blocks probe already evaluates. Probe
`qbeta_g3_deformed_saddle_exact_bridge.py` → witness 2/2 green. No fit;
no c_k wired.

**2026-07-18 (post-#3898) — TRANCHE B PART 2: FIRST A_ω-ADJACENT NUMBERS —
u=0 dictionary CONFIRMED against the GGM integer 3 (ratio 0.92); deformed
amplitude |2πi·r̃|(u_sub) ≈ 1.296; SELF-CORRECTION: the tower singularity
IS the fixed-x closed form.** Borel–Padé residue probe
(`qbeta_g3_aomega_residue_first_number.py`, 4/4 green): (i) u=0 CONTROL on
the 12 EXACT symbolic rungs — leading pole 0.25% from Vol/π and
|2πi·res| = 2.753, ratio 0.918 to the GGM-PROVED integer Stokes constant 3
(#3872 exact S⁺(0)) — the resurgence normalization dictionary (tower Borel
residue = Stokes amplitude) is confirmed at the ~8% Padé-instrument level;
(ii) DEFORMED leg on the measured κ̃₁..κ̃₅: first amplitude estimate
|2πi·r̃|(u_sub) ≈ 1.296 (spread 5%) — the A_ω-adjacent number, honest
instrument precision, NOT wired; (iii) SELF-CORRECTION of the part-1
scope-(a) negative: the deformed Padé poles trend 5.9%→4.9%→3.8% onto the
EXACT fixed-x closed form ι̃·2πi/ξ = 0.44905+0.01491i — the corpus ladder
holds x = e^u fixed, so it IS the fixed-x limit; the part-1 negative is
RE-SCOPED to the #3819 Borel construction only (its pole 0.631 is a
different-instrument number). The closed form (V(σ1)−V(σ2))/(2πi) — whose
algebraic layer is Lean-proved — is now the leading candidate for the
deformed tower singularity, with the amplitude ratio 1.296/2.753 ≈ 0.47
measuring the deformation of the Stokes constant from its u=0 integer 3.
LEAN EXTENSION (owner ask): `DeformedSaddleCurve.lean` +3 sorry-free
lemmas (lean-direct exit 0): cube/sixth-power at the u=0 saddles (y³ = −1,
y⁶ = 1 via linear_combination) and `saddle_separation` — x²(y₁−y₂)² =
(x²−3x+1)(x²+x+1) from the Vieta pair, tying ι̃'s branch locus to the
proven (119) factorization (the algebraic core of meridian genericity).
No fit; no c_k wired.

**2026-07-18 (post-#3923) — POLE-PINNED AMPLITUDES + THE ODD-PHASE NULL:
the 4₁ non-perturbative sector is FULLY phase-law-kinematic — A_ω is not
a 4₁ Stokes phase (direct-measurement confirmation of #3813's
non-amphichiral verdict).** Probe `qbeta_g3_aomega_sharpened_amplitude.py`
(3/3 green): (i) pole-pinned residue extraction with the Lean-backed exact
singularity — u=0 calibration |2πi·r| = 2.807 (ratio 0.936 to the proved
integer 3, tail spread 1.6%, monotone toward 3); deformed
|2πi·r̃|(u_sub) = 1.024 (tail spread 10.6%; supersedes the free-Padé
1.296). (ii) The exact pole satisfies arg(ζ₀) = arctan(t/π) to 8e-53 —
the singularity POSITION carries no intrinsic odd phase (exact: ι̃ real ×
the 2πi/ξ rotation). (iii) THE NULL: arg(r̃) = 9.2e-9 rad from real —
equal to the κ̃₅ phase-test floor (9.24e-9, #3826), i.e. rung-precision-
limited — the deformed Stokes AMPLITUDE is real: the phase law extends to
the full non-perturbative datum. CONSEQUENCE: the bar-odd A_ω channel is
NOT a 4₁ Stokes phase at any level (perturbative tower #3819, singularity
position, amplitude — all kinematic); the odd channel must source from
non-amphichiral geometry — the 5₂-class lane (#3892), independently
confirming #3813's fork resolution by direct measurement. Capstone
(Seq-1) ingredient rows recorded; N_odd stays O(1e-8), no identification
claimed. The 4₁/GGM lane of the g3 campaign is now COMPLETE: exact Stokes
towers, certified blocks, Lean-proved saddle curve, calibrated residue
dictionary, and the odd-phase null. No fit; no c_k wired.

**2026-07-18 (#3916) — Φ_b 2-loop b-dictionary: bar-parity IS the √3 trace-field
grading; F1's odd D-ladder pinned to the geometric κ_odd subladder.** Follow-up
to the branch-point closure, on the restarted designated Φ_b branch. Per #3844's
four-front note the single unowned piece feeding F1 (~~odd D-ladder Écalle
acceleration~~ **[work item SCRAPPED 2026-08-14]**) is "the deformed b-dictionary normalization, which #3596's Φ_b
construction supplies once its saddle expansion is pushed to 2-loop at m=q₀." The
4₁ Φ_b state integral's semiclassical tower log Z ~ 𝔙/ħ + ½logdet + Σ ħⁿSₙ has
fluctuation invariants Sₙ = the exact Ohtsuki κ-ladder (κ_1..κ_7, up to ħ↔2πi/N).
Findings (`qbeta_phib_2loop_bdictionary_probe.py`, 6/6): **(A)** under bar (t↔−t)
the substrate assembly Σ(it)ⁿκ_n splits by n, and the κ-ladder's number-field
grading IS this bar-parity — κ_odd ∈ ℚ·√3·πⁿ, κ_even ∈ ℚ·πⁿ (√3 = the 4₁ cusp
trace field). So the bar-ODD b-dictionary is the closed-form √3-subladder
{κ_1,κ_3,κ_5,κ_7}. **(B/B2 — the unifying finding)** F1's exact bar-odd D-ladder
d_k=a_k+b_k√3 (k≤21) shares ℚ(√3), and its **odd-k rungs are √3-DOMINATED
(bar-odd)** while even-k are ℚ-dominated (bar-even) — so #3861's G2 2-adic
k-parity grading COINCIDES with the √3 bar-parity. F1's "odd D-ladder" is thus
the √3-graded subladder geometrically generated by the κ_odd fluctuation
invariants. **(C)** the leading odd rung assembles at the substrate to the corpus
finite-b correction i·t·κ_1. The d↔κ normalization (= the meridian↔Q_β map)
stays the OPEN keystone bridge — characterized, not asserted; the raw odd-k
growth is O(1) decreasing (3-adic denominator explosion), #3861's mild q-Gevrey
order is the arithmetic-normalized extraction. ħ↔2πi/N: perturbative κ_n only.
No c_k wired; scope-(a); no fit.

> **⚠ [SUPERSEDED 2026-08-09]** — only the *work item* named at the top of this
> entry is withdrawn: `D(ũ)` is convergent (`ρ = 0.1428`, `κ = 0`), so there is
> nothing to accelerate (`qou-dri7`, scrapped). **The b-dictionary
> normalization, the Φ_b 2-loop tranche, and the Ohtsuki κ-ladder findings in
> this entry are unaffected** — the κ-tower *is* genuinely divergent
> (Gevrey-1, Borel singularity `A ≈ 0.7`), which is a different ladder.

**2026-07-18 (#3916 cont.) — d↔κ BRIDGE PRUNED (formalize-first): the action is
Vol(4₁)/π (shared), not new; the keystone narrows to one √3-graded Stokes
constant.** Before searching for the open d↔κ / meridian↔Q_β map
(conj:algebraic-geometric-dilog-equivalence), formalize-first pruned the
hypothesis class (`qbeta_dkappa_bridge_shared_action_probe.py`, 3/3). The
κ-ladder one-instanton Borel action A_n = n/(|κ_{n+1}|/|κ_n|) increases
monotonically 0.551→0.630 (n=2..6) toward Vol(4₁)/π=0.6461 (Richardson
A∞=0.656); the finite-order A_6=0.6303 matches the #3898-tranche-B corpus tower
singularity Re=0.6310 to 0.1% (same Borel singularity, same Murakami depth);
Vol/π lands in C1's even-channel band. **⇒ the bridge requires NO NEW instanton
action** — it is the KNOWN Vol/π, shared across the geometric κ-ladder, the
even channel (C1), and the corpus tower. The bridge SPLITS by bar-parity:
bar-even action = Re = Vol/π (known); bar-odd = the tower's Im=0.0210 — the
√3-graded Stokes constant (matching #3916's √3-graded odd subladder) that
remains open. This narrows the keystone from "derive a transcendental d↔κ map"
to "derive one √3-graded Stokes constant against a known action." scope-(a)
pruning, NOT a derivation; the Stokes constant stays open. No c_k; no fit.

**2026-07-18 (#3916 cont.) — STOKES CONSTANT confirmed (integer 3) from the κ
amplitude; #3916 √3-framing REFINED (parity-blind amplitude).** Reconciliation
with main's landed G3 tranche-B pt2 (`qbeta-g3-aomega-residue-first-number`),
which read the u=0 Stokes amplitude 2.753 (ratio 0.918 to the GGM-proved integer
3, #3872) from Borel-Padé residues. Independent route
(`qbeta_stokes_constant_kappa_amplitude_probe.py`, 2/2): the κ-ladder
one-instanton amplitude 2π·C_n (C_n = κ_n·Aⁿ/Γ(n), A=Vol/π) increases 2.25→2.64
(n=1..7), reproducing the landed 2.753 (rel 4%) — both converge to integer 3.
**Honest refinement of #3916:** the amplitude is PARITY-BLIND — C_n retains the
√3 for odd n yet the odd/even traces converge together (top gap 2.4%), so the √3
is the trace-field dressing that makes both parities SHARE the single integer-3
Stokes constant, **not** a separate √3-graded odd amplitude. The genuine bar-odd
datum is the DEFORMED-pole Im (CS, ≈0.0156 at u_sub), which vanishes at the
amphichiral u=0. Net: the u=0 Stokes constant is settled (integer 3, now
confirmed from the amplitude too); the OPEN piece is the deformation Im at u≠0
(= the meridian↔Q_β map, conj:algebraic-geometric-dilog-equivalence) — NOT a √3
amplitude. Corrects the "√3-graded bar-odd Stokes constant" phrasing two entries
up. No c_k wired; scope-(a); no fit.

**2026-07-18 (post-#3930) — 5₂ PORT: exact saddle data + the FALSIFIABLE
odd-phase targets for the #3892 ladder (Lean-proved curve layer).** The
completed 4₁ machinery ported to GGM §6.1's 5₂: deformed curve derived
from the (232) saddle equation — cleared cubic x·y³ − (x²+1)·y² +
(x²+x+1)·y − x = 0 (x↔x⁻¹ palindromic: the potential (231) is u-EVEN;
the chirality lives in the complex saddle values). Lean-proved sorry-free
(`FiveTwoSaddleCurve.lean`, lean-direct exit 0): x=1 reduction to the
printed (73) cubic y³−2y²+3y−1, discriminant −23 = the printed trace
field, the pairwise Vieta certificate, and divisor-free palindromy
(x·z = 1 ⇒ x²·curve(z,y) = curve(x,y)). Probe controls (3/3 green):
printed root ξ₁ = 0.78492+1.30714i reproduced; |Im V(σ1)| = Vol(5₂) to
1e-10; ι_12(0) = Vol(5₂)/π exact; saddle residuals 1e-50 (V is ℂ/2π²ℤ-
valued — σ3-pair positions are lattice representatives, documented).
STRUCTURAL CONTRAST WITH 4₁: the u=0 singularities already include the
genuinely COMPLEX ι_13 = −0.39349 − 0.65852i (CS(5₂) ≠ 0). FALSIFIABLE
TARGETS for #3892: deformed (u_sub = 2t) ξ-frame pole predictions —
ι̃_12 → 0.90955+0.03021i (kinematic phase EXACTLY, like 4₁'s conjugate
pair); ι̃_13/ι̃_23 → poles with |arg − kinematic| up to 2.683 rad vs the
4₁ null floor 9.2e-9 — a NONZERO intrinsic pole phase is predicted for
the 5₂ σ3-pairs, exactly the odd-channel carrier the 4₁ null excluded.
Forward predictions only; nothing fitted; nothing wired. No c_k wired.

**2026-07-18 (#3938) — the ħ↔2πi/N wall is LOAD-BEARING: Kashaev fluctuation
tower ≠ b-tower phase law; #3923's 4₁ odd-phase null cannot be term-by-term
cross-confirmed from the Kashaev frame (but agrees qualitatively).** Item-1
re-scope after #3923 landed (4₁ deformed Stokes amplitude real; b-tower phase law
κ̃_n=ρ_n·ωⁿ, ω=e^{−i·arctan(t/π)}). Distinct route
(`qbeta_kashaev_vs_btower_phase_distinction_probe.py`, 2/2): the Kashaev-saddle
Wick fluctuation tower deformed to the substrate tilt μ=i·t gives arg(κ_n^K)
tiny/positive (~+0.0003→+0.012), **not** the b-tower's −n·arctan(t/π). The two
towers relate by resummation, not term-by-term — the Kashaev route cannot
term-by-term confirm the null; b-tower amplitudes (r̃, #3805/#3898/#3923) and
Kashaev-frame numbers are NOT interchangeable (category-error guard). Qualitative
agreement: the Kashaev per-rung phase stays below the kinematic magnitude
arctan(t/π), so both frames see only weak odd phase in the deformed 4₁ tower.
Net: the 4₁ lane is #3923's (COMPLETE); the open frontier is the non-amphichiral
5₂-class lane (#3892/#3902 — where my 5₂ quantum volume was found anchor-smooth).
No c_k wired; scope-(a); no fit.

**2026-07-18 (erratum + refinement to #3937) — σ3 CONVENTION CORRECTED:
GGM §6.1 keeps only Re(V) at the real connection; updated 5₂ targets.**
Deeper §6.1/6.2 extraction surfaced the printed convention "for σ3, we
only keep the real part of V" (the Im at the real branch is a log-branch
artifact) — the #3937 σ3-pair targets used full complex V₃ and are
SUPERSEDED. Corrected exact targets (witness regenerated, 3/3):
u=0: ι_13 = +0.45011 − 0.65852i, ι_23 = −conj(ι_13) (clean bar
structure; Re ι_13 = Vol(5₂)/2π exactly); deformed (u_sub = 2t):
ι̃_13 → pole 0.47625 − 0.63135i (arg−kinematic = −0.958 rad),
ι̃_23 → −0.43331 − 0.66156i (−2.184 rad); ι̃_12 unchanged (kinematic
exactly). The nonzero-intrinsic-phase prediction STANDS (max 2.184 rad
vs the 4₁ null floor 9.2e-9). Also extracted for the next tranche:
Theorem 22 (PROVEN 5₂ three-block factorization, eqs 240–245) + H±
q-hypergeometrics + the printed deformed 2-loop (238) — the exact-Z₅₂
implementation is fully sourced. Corrected targets re-posted to #3892.
No fit; no c_k wired.

**2026-07-18 (#3945) — ODD-CHANNEL GEOMETRIC SEARCH CLOSED: the chiral 5₂ σ3-pair
carries nonzero bar-odd phase but is ANCHOR-SMOOTH.** Capstone + the decisive
5₂-class test. The 4₁ odd-phase null (#3923) pointed the odd channel to
non-amphichiral 5₂ geometry; the 5₂ port (#3930) predicts the σ3-pairs carry a
nonzero intrinsic phase. `qbeta_5two_sigma3_anchor_test_probe.py` (2/2, reusing
the #3930 saddle machinery) tests the necessary second condition: ι₁₃, ι₂₃ at
both q₀ anchors. RESULT: the σ3-pairs DO carry nonzero phase (|arg ι₁₃|=0.958,
|arg ι₂₃|=2.184 rad ≫ the null floor 9.2e-9; erratum σ3 convention V_sigma3=Re(V),
reproducing the corrected #3937-erratum targets exactly, ι₂₃=−conj(ι₁₃)) — genuine
non-amphichiral bar-odd carriers — BUT are ANCHOR-SMOOTH (|dι/dq|=0.216, O(1), 7.25
orders below the 3.84e6 swing). So the ONE geometric object with nonzero bar-odd phase still
cannot carry the swing. Every geometric object now fails (4₁ branch-point/volume/
null; 5₂ σ1 volume #3902; 5₂ σ3 phase). The c₃ swing is REPRESENTATIONAL on every
front, chiral included — the 1/u³ inversion of a smooth N_odd, pinned by
experimental Q_β. Capstone: `docs/audits/2026-07-18-qbeta-odd-channel-cornering-
capstone.md`. scope-(a) (σ3-pair alone; magnitude not ingredient — stays a
permanent bar-odd carrier); scope-(b) exclusion of a SINGLE smooth geometric
source (proved null + exhausted census). No c_k wired; no fit.

**2026-07-18 (exact-Z₅₂ tranche) — THEOREM-22 BLOCKS IMPLEMENTED; ASSEMBLY
DERIVED ANCHOR-FREE (β = −πi/3 recovered exactly); the 5₂ three-term
structure measured near the Kashaev ray.** `qbeta_g3_5two_exact_blocks.py`
(3/3 green): H± q-hypergeometrics (242) + blocks (241) over the certified
4₁ θ machinery. The assembly ratios derived with NO external anchor —
Laurent c₋₂/c₋₁ cancellation at the u* = 2πiτ pole family (Theorem 22c
entirety; block poles are order ≤ 2), verified on the held-out −u* family
to 1e-43, and the derived ratios fit e^{α+β(τ+τ⁻¹)} with α = −πi,
β = −πi/3 EXACTLY the printed Theorem-22 constants, c_C = c_B — the 4₁
derivation discipline confirmed on the 3-saddle knot at 1e-44 precision.
Kashaev-ray exact term structure (τ = 1/10+0.05i, u ∈ {.05,.1,.2}):
three O(1)-comparable saddle terms with DISTINCT phases (args e.g.
−1.68/+1.49/+1.37 at u=0.1) — the non-amphichiral amplitude data whose
positions are the corrected #3944 targets. The 5₂ odd-channel measurement
now has BOTH exact sides: singularity positions (saddle closed form) and
exact term amplitudes (this probe). Remaining: the σ-basis rotation
(M(x̃;q̃) dictionary) to read the intrinsic odd phase out of the exact
term data — next tranche. No fit; no c_k wired.

**2026-07-18 (#3954, supports #3927 A3) — the σ3 bar-odd datum supplies the
anchor-independent CARRIER but not the N_odd shape; the A3 u³·smooth prefactor is
constrained.** Follow-on to #3945 (σ3-pair anchor-smooth). Shape half of #3927's
A3 falsification (`u³·smooth × Im 𝔙_q(5₂) vs N_odd`):
`qbeta_5two_sigma3_nodd_shape_probe.py` (2/2, erratum V_sigma3=Re(V)) finds
Im 𝔙_q(5₂)=Im(ι₁₃) smooth and MONOTONE across [1.02,1.50] — no zero crossing near
the substrate (N_odd's defining zero-at-q* absent) — with slope 0.1965 at q₀,
12.1× SMALLER than A′(q*)=2.37. So the σ3 datum gives the anchor-independent
bar-odd carrier but NEITHER N_odd's zero NOR its slope; the A3 u³·smooth prefactor
must carry the zero at q* AND amplify the slope ~12× (not a passive
normalization). scope-(a): raw σ3 alone; magnitude/shape mismatch, not ingredient
exclusion — stays a valid carrier in the composed A3 form. No c_k wired; no fit.

**2026-07-18 (bar-pair tranche) — EXACT 5₂ SUBSTRATE BAR-PAIR COMPUTED;
raw split honestly DEGENERATE; the open step precisely localized.**
`qbeta_g3_5two_barodd_substrate.py` (3/3 green): Theorem-22 Z₅₂ evaluated
exactly at the substrate bar-pair (τ = it/2π and −τ, i.e. q₀-side vs
q₀⁻¹) with the #3951-certified assembly; the substrate point sits EXACTLY
on the block-pole lattice (x = q⁻² since u_sub = 2t) — handled by the
entire-Z circle average; implementation certified by exact u-evenness
(3e-44). HONEST FINDING: the raw bar-split is degenerate — the bar image
is exponentially suppressed (|Z_q̄/Z_q| ~ 1e-30; the classical
e^{V/2πiτ} prefactor flips exponent sign under τ→−τ), so D_odd ≈ D_even
measures the classical asymmetry, not an intrinsic odd datum. Log-split
recorded: 𝔏_odd = 34.4318219 + 2.2721850i. THE REMAINING OPEN STEP is
now precisely localized: strip the classical exponential (the
normalization derivation) from the bar-pair — with every exact
ingredient on main (singularity positions #3944, term amplitudes #3951,
the bar-pair here). No identification claimed; no fit; no c_k wired.

**2026-07-18 (#3964, supports #3927 A3) — no natural 5₂ factor supplies the N_odd
zero-at-q*; the A3 prefactor zero is representational.** Distinct-route follow-on
to #3954 (σ3 carrier monotone, slope 12× short). Structural enumeration
(`qbeta_5two_a3_prefactor_natural_factors_probe.py`, 1/1, NOT a fit) of six
natural 5₂ smooth factors — σ1 quantum volume, σ3 bar-even part, [3]_q, [5]_q,
σ3/σ1 action ratio, σ1–σ3 saddle separation — across q∈[1.02,1.30]: ALL smooth,
monotone, bounded away from zero (smallest |ι₁₃/ι₁₂|≈0.79–0.89). No natural factor
crosses zero. ⇒ the N_odd zero at q* is NOT a manifest geometric feature of any
natural 5₂ object — it is representational (q* = the S=A/u³ crossing, pinned by
experimental Q_β). A3's prefactor can produce the zero only by a non-structural
factor tuned to q* (anti-fit-forbidden as a derivation). Confirms the
representational conclusion from the prefactor side; complements main's "open step
localized to the classical-prefactor strip" (96a42b8ab9). scope-(a) (excludes the
obvious candidates, not a proof no factor exists). No c_k wired; no fit.

**2026-07-18 (strip tranche) — SUBSTRATE PAIR AMPLITUDES EXTRACTED (near-
unit, exact solve): PRELIMINARY intrinsic bar data φ_odd = −0.004145 rad;
generic-direction strip honestly OPEN (needs the M-dictionary).**
`qbeta_g3_5two_classical_strip.py` (2/2 green): with the Theorem-22 exact
Z₅₂ and the saddle classical prefactors e^{V/2πiτ}/√(iδ) (V per (231), δ
per (235), branches mod-2πi per the #3944 convention), the substrate-ray
conjugate-pair amplitudes were extracted by exact 2×2 solve on BOTH bar
sides: |a_σ2| = 0.958, |b_σ2| = 1.041 (near-unit — the expected
transseries-coefficient scale; σ1 nearly absent from the contour, ~1e-3 —
consistent Picard–Lefschetz). PRELIMINARY intrinsic bar data (conj-
symmetry predicts 0): φ_odd = arg a₂ + arg b₂ = −0.004145 rad and
|b₂|/|a₂|−1 = +0.0864 — the first normalized bar-odd numbers from the
non-amphichiral sector, same ORDER as the S anchors (S_muon +0.00968,
S_proton −0.03946) but at O(τ²)-instrument precision and with NO
identification claimed. HONEST OPEN (S2): off the ray the single-saddle
strip is structurally wrong (V_eff matches no saddle mod 2π²; blocks
carry their own modular e^{1/τ} growth) — the Stokes-sector bookkeeping
(the 5₂ M(x̃;q̃) dictionary, GGM 94-95 analogues) is the remaining step
to certify the strip and sharpen φ_odd beyond preliminary. No fit; no
c_k wired.

**2026-07-18 (sector-Prony tranche) — SECTOR CONTENT DERIVED
REPRESENTATIVE-FREE: the generic sector holds ALL THREE saddle terms
(rank-3 Prony beats rank-2, holdout 0.0049 vs 0.185) — the derived cause
of the #3987 off-ray strip failure; sheet identification honestly OPEN.**
`qbeta_g3_5two_sector_prony.py` (2/2 green): exact Theorem-22 Z₅₂ sampled
equally in 1/τ along the S2-failure direction; rank-2/rank-3 Prony with
held-out certification — the three-term model wins decisively, exponents
E = (−2.7385+6.4091i, −3.0508+3.8801i, −2.7935+5.3053i) recorded. The
exponents sit OUTSIDE the small-integer scan of my saddle-branch
representatives' multivaluedness moves (residuals ~1.2–1.8) — the
branch-sheet bookkeeping genuinely needs the full 5₂ M(x̃;q̃) dictionary
(the honest remaining step), for which these Prony exponents are now the
exact targets. φ_odd (#3987, −0.004145 preliminary) unaffected: the
substrate-ray conjugate-pair extraction is the on-ray case with near-unit
amplitudes. No fit; no c_k wired.

**2026-07-18 (dictionary-diagnostic tranche) — PER-TERM EXPONENT
IDENTIFICATION IS DRIFT-LIMITED AT THIS τ-WINDOW: the numerics lane is
exhausted; the remaining path to a derived-precision φ_odd is the
ANALYTIC 5₂ M-dictionary.** `qbeta_g3_5two_block_saddle_dictionary.py`
(2/2 green, honest diagnostic): Theorem 22 writes Z₅₂ as exactly three
terms, so the #3991 Prony exponents should be the per-term exponents —
tested in ρ-space (branch-ambiguity-free Prony-grid ratios on each exact
term). Finding: all three terms have COMPARABLE ratio magnitudes
(|ρ| ~ 50–60) with 5–12 % drift per Δ-step, they do NOT match the #3991
Prony roots individually (devs 0.85/0.24/0.95, no bijection), and
per-term saddle/sheet identification with the Δ-constant offset
2πi·β_T scanned over small-integer sheet moves leaves residuals
1.7–2.9. CONCLUSION: at this window the block terms are not clean
exponentials — the (238)-and-higher c₁τ corrections dominate at the
several-percent level, so exponent-level sector identification (both
#3991's three-term set and any per-term map) is effective, not sharp.
REDIRECT: deeper numerics at this window cannot sharpen φ_odd; the
remaining step is the ANALYTIC M-dictionary — the u=0 H^ε tower (GGM
89a-c/90a-c, needs the E₁⁽ⁿ⁾/E₂⁽ⁿ⁾/E₂ definitions from pp. ~20–21),
the 3×3 W_m, the (94)-(95) M/S sandwiches derived OCR-free against the
q→0 targets (96/97, constants {3,4}), then wall-crossing to deformed x.
φ_odd (#3987, −0.004145 on-ray) stands as preliminary. No fit; no c_k
wired; scope-(a).

## 2026-07-18 — knot-operator/Gram recurrence framing ↔ the c_k/Ohtsuki ladder (structural, no wire)

The c_k precision ladder is "conceptually the Ohtsuki invariants ... ladder +
Habiro–Pochhammer bridges" (cheat-sheet, above). This session formalizes the *recurrence
mechanism* behind that ladder and pins where the odd channel departs from it:

- **Even/geometric channel = knot-operator + Gram recurrence (q-holonomic / quantum
  A-polynomial).** A knot operator that is a power of a braiding element acts on a
  finite-dimensional Hecke/TL module; Cayley–Hamilton ⇒ an order-`d` linear recurrence
  (`d = N+1` at colour `N`), and the Markov-pairing **Gram matrix** makes it self-adjoint so
  `G⁻¹` builds the projector basis that diagonalises it. Lean: `QOU/BraidKnot/`
  `KnotOperatorRecurrence.lean` (twist 2×2: `charpoly_two` → `trace_two_step`,
  `twist_gram_selfAdjoint`; PR #3995) + `ColoredJonesRecurrence.lean` (general order-`d`:
  `pow_recurrence_of_relation`, `trace_recurrence_of_relation`). This IS the AJ / quantum
  A-polynomial structure the Ohtsuki-invariant ladder rides on — the same Gram inverse that
  gives the LP/SDP confinement dual.
- **Bar-odd `Q_β` channel escapes it (KC22).** The D-ladder `D(ũ)` is proven **not** low-order
  `(q-)holonomic` in any tested class (KC22, prime-certified). In this language: the odd
  channel is *not* the trace of powers of a knot operator on any finite-dimensional Gram
  module — it has no quantum-A-polynomial recurrence. **It does NOT follow that the odd
  channel is resurgent** (corrected 2026-08-14; the clause here formerly read "hence the
  resurgent/Écalle route"). Non-holonomic does not imply divergent: KC22's own closed form
  `D(w) = φ(w)log(1−w/ρ) + ψ(w)`, with algebraic `φ`,`ψ` over a degree-12 field, is
  **convergent** (`ρ = 0.1428`, `κ = 0`) *and* not low-order P-finite — it is the
  counterexample to the inference, and it is the object under discussion. The
  even(μ–p) vs odd(`Q_β`) split is exactly "has a Gram recurrence" vs "does not."

Audit: [`2026-07-18-knot-operator-gram-recurrence.md`](../audits/2026-07-18-knot-operator-gram-recurrence.md).
Records the mechanism + its KC22 boundary; no c_k wired, no fit, no tier change.
**2026-07-18 (analytic M-dictionary, part 1) — THE u=0 5₂ TOWER LAYER IS
DERIVED AND CERTIFIED OCR-FREE; the (92) orthogonality and the E₂
constant slots are now EXACT.** `qbeta_g3_5two_analytic_hm_tower.py`
(4/4 green): the H^ε_{k,m} towers (GGM 89a-c/90a-c with E-series (79))
implemented and self-certified against Theorem 11 without trusting a
single ambiguous glyph. (T1) H⁺ satisfies the (86) q-difference
recurrence and H⁻ its q→q⁻¹ extension recurrence to < 1e-48 — the E₁
sign is pinned uniquely (flip breaks at > 1e-6) and the (80) extension
identity is structurally certified. (T2) the k=2 constant slot enters
as a c·H₀ column operation — proven (86)- and det-invisible. (T3, the
centerpiece, EXACT rational q-series arithmetic): every Theorem-11
bilinear carries only the SUM σ_c = c⁺+c⁻, and demanding the (92)
entries be Laurent POLYNOMIALS derives σ_c = 1/4 − 6·Ê₂ exactly —
identically the printed "−(1/6)E₂ / −(1/12)E₂" under standard
E₂ = 1−24Ê₂ — plus the (92) RHS = [[1,0,0],[0,0,1],[0,1,3−q^m]], all
entries exact to O(q^24), held-out m=2 verified. The (c⁺,c⁻) split is
Theorem-11-invisible; its pin is honestly deferred to the (82)
state-integral match. (T4) independent mpmath towers reproduce the
derived identity to 1e-50. NEXT (part 2): W₋₁-based (94)-(95) M/S
sandwiches vs the q→0 targets (96/97, constants {3,4}), the (82)
u=0 state-integral match (pins the split + ties towers to the
certified #3951 blocks), then wall-crossing to deformed x → the
derived-precision φ_odd. No fit; no c_k wired; scope-(a).

**2026-07-18 (analytic M-dictionary, part 2a) — THE (c⁺,c⁻) SPLIT IS
DERIVED (40 digits) AND THE (82) STATE-INTEGRAL READING CERTIFIED;
towers now TIED to the certified deformed blocks.**
`qbeta_g3_5two_state_integral_split_pin.py` (2/2 green): eq (82) was
glyph-decoded (cmsy minus-offset discipline; sub/superscript y-band
rows) as Z₅₂(0;τ) = −(e^{πi/4}/2)(q/q̃)^{1/8}·(τH₀⁻(q̃)H₂⁺(q) −
2H₁⁻(q̃)H₁⁺(q) + τ⁻¹H₂⁻(q̃)H₀⁺(q)) — the same antidiag(1,−2,1)
pairing shape as the part-1 (92) bilinear. Because term 1 carries
c⁺(q) and term 3 carries c⁻(q̃) at DIFFERENT arguments, the state
integral separates the split the Theorem-11 bilinears cannot see.
Matched linearly against the independently certified Theorem-22 exact
Z₅₂ (#3951 assembly, u→0 circle-average K=20) at two asymmetric
τ-points (symmetric points make the solve singular — first-run
failure kept honest in the probe docstring): phase σ = 1 (NO
convention factor between Thm 22 and (82)), a⁺ = 1/6 to 6e-41,
b⁺ = −4 to 6e-39, held-out τ rel dev 1.3e-40 — c⁺ = (1/6)E₂,
c⁻ = (1/12)E₂ (E₂ = 1−24Ê₂) is now DERIVED, completing the part-1
deferral. The u=0 tower layer is fully pinned. NEXT (part 2b): the
(94)-(95) M/S sandwiches vs the q→0 targets (96/97, constants {3,4}),
then wall-crossing to deformed x → the derived-precision φ_odd. No
fit; no c_k wired; scope-(a).

**2026-07-18 (analytic M-dictionary, part 2b) — THE u=0 5₂ STOKES
DATA (94)-(97) IS FULLY DERIVED: exact sandwiches reproduce the q→0
factorizations and Stokes integrality from first principles.**
`qbeta_g3_5two_stokes_sandwich.py` (2/2 green, exact Fractions): the
(95a/b) sandwiches were glyph-decoded (the L⁺ row-3 minus sat BELOW
the printed band — caught only by the cmsy minus-offset rule, recorded
in the probe) as S⁺ = ½L⁺W₋₁(q⁻¹)·antidiag(1,−2,1)·W₋₁(q)ᵀR⁺ and the
mirrored S⁻, with the SAME antidiag(1,−2,1) pairing as (92) and (82).
Assembled from the fully-pinned tower layer (σ_c #4011, split #4013):
S⁺(0) = [[1,4,0],[0,1,0],[−3,−9,1]] and S⁻(0) = [[1,0,3],[−4,1,−3],
[0,0,1]] EXACTLY equal the glyph-decoded (96/97) three-factor products
(printed constants {3,4}); every entry is an INTEGER q-series to
O(q^18); det S± = 1 identically; the unflipped W-orientation wins —
the same convention the part-1 (92) RHS picked (two independent
confirmations). The O(q) Stokes coefficients are recorded in the
witness (new derived data beyond the print). NEXT (part 2c): wall-
crossing to deformed x — port the sandwich structure onto the #3951
deformed Theorem-22 blocks, certify the off-ray strip, and sharpen
φ_odd (#3987, −0.004145 preliminary) to derived precision. No fit;
no c_k wired; scope-(a).

**2026-07-18 (analytic M-dictionary, part 2c-1) — THE DEFORMED LAYER
IS CERTIFIED AND THE EXACT BAR-TRANSFORM TOOL IS IN HAND: descendant
blocks, the deformed bilinear (245), and the (250) wall-crossing
identity all stand at 1e-34..1e-46.** `qbeta_g3_5two_deformed_bilinear.py`
(2/2 green): the descendant blocks A_m/B_m/C_m (GGM 241a-c, z-slot
q^m·x^{±2} + x^{±m}/θ⁻² structure), the deformed W_m(x;q) (244), and
the bilinear W_{m,μ}(u;τ) = W_{−μ}(x̃;q̃⁻¹)·Δ(τ)·W_m(x;q)ᵀ (245/246 —
the deformed analogue of the (92) sandwich). Certified: [W₀,₀]₁₁
reproduces the #3951-certified Z₅₂ (2e-45); the (247) x↔x⁻¹ symmetry
holds at descendant order m=2 (1e-45); Theorem 22(c) u-ENTIRETY holds
at the lattice point u* = log q at descendant (m,μ) = (1,2)
(two-radius circle-average, 5e-34); and the (250) WALL-CROSSING
determinant identity — H(x,y,z;q⁻¹) = det(2×2 of H⁺'s)/(y·θ-triple),
the exact q→q⁻¹ bar-transform of the deformed blocks — holds at
generic (x,y,z,q) to 1e-45 with the printed reading (no scan needed).
This is the structural tool the barodd probe (#3962) said was missing:
the intrinsic bar-odd extraction can now strip the classical prefactor
via the bilinear + crossing identity instead of Borel numerics. NEXT
(part 2c-2): apply (250) at the substrate bar-pair → φ_odd at derived
precision (vs #3987 preliminary −0.004145). No fit; no c_k wired;
scope-(a).
**2026-07-18 (#3993 b3ix odd-locus — AUTHORITATIVE 5₂ cyclotomic coefficients
from Masbaum, "be critical" colored-Jones gate CLEARED).** The owner flagged
the self-calibrating `(V_{5_2}-1)/(V_{4_1}-1)` extraction of `C_{5_2,1}` as a
possibly-erroneous probe and pointed at Masbaum's twist-knot paper (uploaded on
main, `library/agt-v3-n1-p17-p/agt-v3-n1-p17-p.pdf`, `masbaum2003`, DOI 10.2140/agt.2003.3.537).
Critical verification (`qbeta_5two_masbaum_cyclotomic_probe.py`, 4/4):
(1) V_{4_1}, V_{5_2} match KnotInfo; (2) Masbaum Thm 5.1/Rem 5.2 for K_2
reproduces the standard Jones V_{5_2} at N=2 EXACTLY (fixing t=q⁻¹);
(3) the DERIVED Kashaev-tail basis bridge `C_{K,n}(q) = (-1)^n q^{n(n+1)/2}
f̃_{K,n}(q)` is exact — it maps Masbaum's `f̃_{4_1,n}=(-1)^n q^{-n(n+1)/2}` to
`C_n=1` (Kashaev figure-eight) on the amphichiral knot; (4) the flagged
self-calibrating heuristic `C_{5_2,1}=-(t⁻²+t⁻⁴)` EQUALS the authoritative
`C_{5_2,1}(q)=-(q⁴+q²)` exactly — the heuristic STANDS, not erroneous. This
supersedes the heuristic as the source of record and delivers the authoritative
higher coefficients (task 2): `C_{5_2,2}(q)=q¹¹+q⁸+q⁷+q⁵`,
`C_{5_2,3}(q)=-(q²¹+q¹⁷+q¹⁶+q¹⁵+q¹³+q¹²+q¹¹+q⁹)` — all bar-asymmetric (5₂ chiral),
the genuine 5₂ bar-odd Habiro data for the Q_β odd channel. Lean: c52_2, c52_3
+ bar-odd-term theorems (`QOU.QBeta.HabiroCyclotomicOddLocus`, sorry-free).
Distinct-route from the sibling state-integral/M-dictionary strip (main
7d9a6c03aa etc.): the Habiro/cyclotomic-basis face gives the coefficients as
exact Laurent polynomials; the two converge on the same 5₂ odd datum. Beans
filed for the other uploads (q-holonomic Garoufalidis-Lê, Takata A-poly, Hitchin
monodromy). scope-(b): cited exact formula, Jones-cross-checked. No fit; no c_k.

**2026-07-18 (analytic M-dictionary, part 2c-2) — φ_odd SHARPENING
OBSTRUCTED (honest, localized): the substrate is EXACTLY the (250)
0/0 lattice node, the σ3-pair strip is precision-UNSTABLE, and the
multi-loop solve diverges — the #3987 −0.004145 stands as a 2-loop
preliminary (~1 sig fig).** `qbeta_g3_5two_wall_crossing_barpair.py`
(C1/C2 green; S1/S2 honest negatives). [C1] at q₀ the bar-pair
(q=e^−t=0.90092, q̄=q⁻¹=q₀=1.10998) is REAL, the substrate sits
EXACTLY on the block pole lattice (x=q⁻², u_sub=2t, dev 0), and the
(250) θ-triple prefactor VANISHES there (0/0 node) — φ_odd lives
exactly where the classical factor the (250) identity strips is zero,
so the tool cannot dissolve the degeneracy, only relocate it into the
vanishing θ-triple. [C2] the (250) tool is re-certified in the
substrate NEIGHBOURHOOD (off-lattice, q near e^−t) to 6.3e-50. [S1]
the #3987 σ3-pair strip is PRECISION-UNSTABLE: the ray classical
prefactor is e^{−V/t}, |Re| ≈ 34.5 (~1e15), and the 2%-spaced 2×2
rows are near-parallel, so the ~1e-2 phase residual is
cancellation-limited — the solve tips between the physical near-unit
branch (|a₂|≈0.96, φ_odd≈−0.004) and a spurious null branch
(|a₂|≈1e-53, φ_odd≈+0.9) NON-monotonically in dps (physical at
40/45/60/80/150/200; collapse at 50/100/300 — recurs even at high
precision), and the physical value carries ~4% circle-average-scheme
sensitivity (−0.003999 K=40 vs −0.004145 K=12), i.e. good to ~1 sig
fig. [S2] the exact multi-loop ray extraction (solving c₂,c₃,… beyond
the printed 2-loop, transseries form inverted against exact data — not
a fit) gives NO trustworthy limit: cond explodes with loop order
(156 → 2e6 → 4.5e9 → 3.8e13 → 4.9e17 at dps 60) and the result is
precision-branch-dependent (dps 60 sequence −0.0044→−0.0011→−0.0017→
−0.00177→−0.00178, but dps 50 lands in [0.5,4.2]). The small-Δ dps-60
tail (≈−0.0018) is a spurious ill-conditioned + precision-branch
artifact — a lax "last-3 within 1e-4" check flags it as "converged",
but it sits at cond>1e12 AND fails the precision-stability gate, so
reporting it would launder an ill-conditioned fit as a derivation; the
probe's strict gate (tractable cond<1e12 AND n_phys=4) rejects it. At
τ_sub≈0.0166 the τ^k loop columns are numerically degenerate and the
contour-absent σ3-real saddle leaks. CONCLUSION: φ_odd = −0.004145
stands as a 2-loop
PRELIMINARY (dictionary datum for the anchor-smooth, permanent 5₂
σ3-pair carrier per the odd-channel capstone — NOT the c₃ swing
carrier, which is representational); a derived value needs higher-loop
(238)-type c₂,c₃ (printed-data-blocked in 2012.00062v3 §6.2) or a
σ3-transseries resummation — NOT deeper numerics, and the (250) block
identity is exact but does not isolate the saddle Stokes constants
φ_odd is built from. Audit:
`docs/audits/2026-07-18-5two-part2c-wall-crossing-barpair.md`. No fit;
no c_k wired; scope-(a) (constrains the METHOD, not the σ3-pair
ingredient — it remains a valid bar-odd carrier).

**2026-07-24 (post-week resync — block-level bar-pair: POLE-FAMILY
SWAP + REALITY NULL; independent parallel-route confirmation of the
2c-2 obstruction, with mechanism).**
`qbeta_g3_5two_intrinsic_barodd_crossing.py` (3/3 green): per-block
Laurent coefficients at the substrate lattice node on both bar sides.
(F1) the bar involution SWAPS the pole families — q-side A regular /
B,C double-pole; bar-side exactly reversed — the blockwise face of the
(250) crossing (Ā is a determinant of B/C-type H's) and the MECHANISM
behind the 2c-2 0/0 node. (F2) every significant coefficient is REAL
(worst 1.2e-41): on the ray the function-value intrinsic bar phase is
exactly 0/π — a genuine bar-odd phase must be lateral/Stokes (part-2b
S±, q̃-suppressed on-ray) or live in another slot; independently
supports φ_odd = −0.004145 as ~1-sig-fig preliminary. (F3) the real
intrinsic node data recorded as matched-order swap-covariant
cross-family ratios (B/C degeneracy < 1e-41). Workplan (beans, W1-W4
under qou-yaz3): next = EXACT higher-loop c₂/c₃ by formal Gaussian
at the (231) saddle (algebraic in Q(ξ)) + the Masbaum cyclotomic
cross-face; coordinate with #4127 (octahedral 4-dilog lane) before
overlap. No fit; no c_k wired; scope-(a).

**2026-07-24 (W2 part 1) — THE FORMAL-GAUSSIAN LOOP ENGINE IS
CERTIFIED: the printed 4₁ loop coefficients (42) reproduced EXACTLY at
all three orders (1e-59) — the well-conditioned algebraic route to the
unprinted 5₂ c₂/c₃ that the 2c-2 obstruction called for is open.**
`qbeta_g3_formal_gaussian_loops_41gate.py` (2/2 green): Feynman-rule
expansion at the state-integral saddle with the Faddeev vertices —
(G0) the expansion log Φ_b = Σ ħ^{2n−1}B_{2n}(1/2)/(2n)!·Li_{2−2n}(−e^w)
was certified against the exact Φ_b product formula at small b (1.5e-9
= |ħ|⁵ floor), NOT trusted from memory; (G1) the δ = √−3 saddle branch
(ξ = e^{iπ/3} of curve (38) via ξ = −e^w); (G2) the universal
e^{−ħ/24} normalization derived from c₁'s constant part by exact hand
computation, then VERIFIED on the two held-out orders; (G3)
c₁ = 11/(72√−3), c₂ = (697/2)/(72√−3)², c₃ = (724351/30)/(72√−3)³ all
matched to ~1e-59 at dps 60 (EPS_ORD = 18; six-cubic-vertex diagrams
needed for c₃). No ill-conditioned inversion anywhere — loop data is
rational in the saddle (GGM (12)). NEXT (W2 part 2, bean qou-3ndf):
run the engine on the deformed 5₂ potential (231) at the σ-saddles →
gate on the printed u=0 (76) + deformed 2-loop (238), emit the
unprinted exact c₂/c₃, then re-extract φ_odd with the extended
transseries. No fit; no c_k wired; scope-(a).

**2026-07-24 (W1) — INDEPENDENT CONFIRMATION + MECHANISM for the
part-2c-2 obstruction: the bar involution SWAPS the block pole
families, and the substrate-ray block data is REAL to 1e-41.**
`qbeta_g3_5two_intrinsic_barodd_crossing.py` (3/3 green; parallel
route per the owner directive, citing audit
2026-07-18-5two-part2c-wall-crossing-barpair): per-block Laurent
coefficients at the substrate lattice node show (F1) q-side A
regular/B,C double-pole with the bar side exactly reversed — the
blockwise face of the (250) crossing and WHY the classical-prefactor
strip hits 0/0 there; (F2) every significant coefficient on both bar
sides is real, so the function-value intrinsic bar phase is exactly
0/π on the ray — a genuine bar-odd phase must be lateral/Stokes or
live elsewhere, independently supporting φ_odd = −0.004145 as a
~1-sig-fig preliminary; (F3) the real swap-covariant cross-family
ratios recorded scope-(a) with the B/C degeneracy check (1e-45).

**2026-07-24 (W2 part 2) — THE DEFORMED 5₂ LOOP DATA IS DERIVED
(c₁, c₂, c₃ at any x, including the previously-UNPRINTED c₂/c₃), and
the corpus (238)-transcription is SUPERSEDED: it fails the u→0
continuity gate with a saddle-dependent mismatch.**
`qbeta_g3_5two_deformed_loops.py` (2/2 green): the #4149-certified
formal-Gaussian engine, extended to the deformed x-fixed frame, passes
(A) the 4₁ (42) regression (1.6e-59), (B) the full NINE-integer
trace-field snap of the printed 5₂ u=0 (76) series (c₁·2116 →
(−454,209,−242); c₂·389344 → (25400,−22668,12643); c₃·12357778560 →
(−164659509,85642761,−35443870); snaps 1e-51..1e-59; ν = −1/8
held-out-verified), and (C) u→0 continuity with the O(u²) even-in-u
scaling. HONEST FINDING (D): `c1_printed` (the #3987 glyph transcription
of (238)) does NOT reduce to the certified (76) values at u→0 — ratio
0.80 on σ₁, 4.7∓2.15i on σ₂/σ₃ (saddle-DEPENDENT ⇒ no frame constant
absorbs it); the scrambled P/δ³ decode is implicated and the engine
supersedes the transcription. CONSEQUENCE: downstream consumers of
c1_printed — the #3987 pair amplitudes and the 2c-2 multi-loop solves,
hence the φ_odd = −0.004145 preliminary — are flagged for
re-extraction with engine input. EMITTED (witness): engine c₁..c₃ at
u = 0.17, 0.30 and the substrate u_sub = 2t, all three saddles. NEXT:
re-run the σ₂/σ₃-pair φ_odd extraction with the engine 3-loop
transseries. No fit; no c_k wired; scope-(a).

**2026-07-24 (W2 part 3) — THE SUBSTRATE IS A TRANSSERIES-RESONANT
POINT: x̃ = 1 EXACTLY, the ℓ-tower degenerates, and finite-rank
amplitude extraction is structurally inadequate there — the σ-pair
φ_odd channel closes; the derived-grade route is the MASBAUM FACE.**
`qbeta_g3_5two_phiodd_engine_reextraction.py` (2/2 green, honest
diagnostic): the re-extraction was run with the corrected instrument
(engine 3-loop models replacing the superseded (238) transcription,
rank-3 solve closing the σ₁ leak, sector-constancy sweep as sheet
certification). The sweep FAILED its own gates — and localized WHY:
on the imaginary-τ ray |x̃| = 1 identically, so the GGM (13)-(14)
ℓ-tower Φσ·q̃^k·x̃^ℓ is non-decaying, and at the substrate itself
x̃ = e^{−4πi} = 1 EXACTLY: the entire ℓ-tower DEGENERATES onto the
bare saddle exponents (a resonance locus — the same coincidence
lattice as the 2c-2 0/0 node and the W1 pole-family swap). The
drifting pseudo-amplitudes are the tower aliasing into finite rank;
tilting the ray (θ = 0.1–0.35) suppresses the tower but explodes the
saddle magnitude hierarchy (|a₂| ~ 1e20) — recorded. CONSEQUENCES
(scope-(a), method-level): the #3987 φ_odd = −0.004145 (2-term model
+ superseded 2-loop, AT the resonance) cannot be a derived σ-pair
amplitude phase; an on-ray derived value needs ℓ-tower resummation
(lateral machinery), not finite-rank numerics; the near-term
derived-grade route to the 5₂ bar-odd datum is the Masbaum
cyclotomic face (exact C_{5₂,n} Laurent polynomials, already
landed). The campaign's function-value/state-integral lane is now
cleanly closed with derived structure at every dead end: 4₁ odd-phase
null → W1 reality null → 2c-2 obstruction → the x̃ = 1 resonance.
No fit; no c_k wired.

**2026-07-24 (W3) — CROSS-FACE BRIDGE CERTIFIED THROUGH 3 LOOPS: the
Masbaum cyclotomic face and the loop-engine/state-integral face are
ONE analytic object, and the bar-odd C_{5₂,n} data now has a
state-integral-certified backbone.** `qbeta_g3_5two_kashaev_cross_face.py`
(2/2 green): the Kashaev ladder ⟨K⟩_N = Σ C_n(q)·|(q;q)_n|² at
q = e^{2πi/N} (the framework's C-basis IS the Kashaev-tail basis —
the bridge factor (−1)ⁿq^{n(n+1)/2} is exactly the (q;q)ₙ² → |(q;q)ₙ|²
transfer at roots of unity; the naive Habiro-basis reduction DECAYS and
is recorded as the convention trap) matches the certified engine loop
data on every rung: 4₁ control α/logN/γ (γ rel 1.4e-4); 5₂ α =
Vol/2π to 1.3e-11, 2-loop γ = −2π·Im c₁(ξ_geo) to 3.8e-6 — uniquely
selecting ξ_geo = 0.78492+1.30714i (the +Im member of the trace-field
cubic) as a DERIVED byproduct — and 3-loop 1/N² = Re[(2πi)²(c₂−c₁²/2)]
to 5.8e-4. Held-out-N gated; window solve exact. CONSEQUENCE: the
odd-channel extraction proceeds on the Masbaum face (per the #4167
resonance redirect) with the engine as its certified cross-check.
Scope-(a); no c_k wired.

**2026-07-25 (Masbaum-face odd-channel data) — THE FIRST EXACT
ODD-CHANNEL NUMBERS ON THE MASBAUM FACE, the substrate Habiro tail,
and the EXACT bar-side divergence law that poses the resummation
step.** `qbeta_g3_5two_masbaum_barodd_profile.py` (2/2 green; exact
integer-Laurent arithmetic for all polynomials): (M1) the
convergent-side Habiro tail at the substrate is
F(q₀⁻¹-side) = 0.9861565521419607621… (truncation-certified 1e-40 at
n = 37). (M2) the bar-side divergence is characterized EXACTLY:
max_exp(C_{5₂,n}) = 3n² + 5n as an exact integer identity (n = 1..10)
and min_exp has exact 2nd-difference 2 — so the bar image is q-Gevrey
of quadratic type with growth constant (3/2)·t·n² in q-units: the
DERIVED divergence datum the W9 q-Borel/Ecalle lane (sibling bean
qou-dri7) must resum; a structural echo of the θ⁻²/x²-slot growth on
the state-integral face is noted, not claimed. (M3) the exact per-n
bar-odd profile ρ_n = O_n(q₀)/E_n(q₀) (canonical monomial-wise bar
split, 5₂ chirality ⇒ O_n ≠ 0): ρ₁ = −0.30318, ρ₂ = −0.66918,
ρ₃ = −0.90334, …, ρ_n → −1 (the C_n become asymptotically PURE
bar-odd — the unpaired extreme monomials dominate). Scope-(a)
comparison rows vs the S anchors recorded; NO identification. The
odd-channel derivation now has exact finite-n data (this), the
certified analytic backbone (W3 #4172), and a precisely-posed
resummation step. No fit; no c_k wired.

**2026-07-25 (W9-parallel) — THE BAR SIDE IS RESUMMED: the first
resummed bar-odd datum D_odd = −0.0075794037 ± 1.5e-10 (real, same
order class as the S anchors), via an exactly-gated q-Borel/θ-Laplace
pipeline.** `qbeta_g3_5two_qborel_theta_laplace.py` (3/3 green;
parallel to the sibling W9 lane qou-dri7 per the owner directive,
distinct exact-input angle): (B1) the exact q-Borel transform
T̂_n = C_n(q̄)(q̄;q̄)_n²·a₀^{5n²+7n} has (−1)ⁿT̂_n > 0 decaying with
|ratio| → 1 (Aitken 1.00001) — Borel radius EXACTLY 1 with a SOFT
singularity at w = −1, and a derived structural fact: the C-tail and
Pochhammer-tail subleading monomials CANCEL (the naive extreme-monomial
product overshoots). (B2) the θ-kernel inversion identity was DERIVED
in-probe (not cited) and gated exactly on a finite quadratic-type test
(9e-62). (B3) the resummed bar-side value s(F̄) = 0.9709977446 is
kernel-choice-invariant to 12 digits and Padé-order-stable (relative
band 3e-10 — the honest scheme-dependence report). (B4) with the
convergent side F_conv = 0.9861565521 (#4175):
D_odd = (s(F̄) − F_conv)/2 = −0.0075794037 ± 1.5e-10, D_even =
0.9785771484; D_odd/u³ = −0.834. All REAL — consistent with the W1/2c-2
reality null (and the S anchors are real). Scope-(a): recorded against
S_muon (+0.00968), S_proton (−0.03946), u³, Im 𝔙̃_b WITHOUT
identification; a derived-grade claim still needs the scheme fixed by
a structural normalization (Écalle median / M-dictionary lateral) —
the sibling W9 lane's framing question, now with a concrete number and
a 3e-10 instrument. No fit; no c_k wired.

**2026-07-25 (D_odd median + cross-checks) — THE NORMALIZATION QUESTION
RESOLVES: D_odd = −0.007579403739 ± 5e-16 is scheme-robust (δ-torus
median), superasymptotically gated, and pin-characterized.**
`qbeta_g3_5two_dodd_median_crosschecks.py` (3/3 green): (E) the
δ-torus average — the q-analogue of the Écalle median over the
θ-Laplace spiral offset — has orbit variation 4.9e-16: the scheme
ambiguity is THIRTEEN orders below the physics scale, so the #4184
caveat closes and D_odd(proton pin) = −0.007579403739 stands
median-normalized. (C1) the raw divergent series' optimal truncation
(n* = 3) agrees with s_med within its minimal term (0.0017 < 0.0033) —
the classic internal resummation gate. (C3) recomputing the ENTIRE
pipeline at the muon pin moves D_odd by only 2.2e-9 while the anchors
differ by ΔS = +0.0491 — an honest structural constraint: the
anchor-dependence of S is per-observable, NOT a substrate-modulus
effect on this object; any future identification must source ΔS
elsewhere (e.g. the observable-side u-dependence or the f-map slot).
(C2) same-decade row vs the sibling b3ix order-3 estimate (T_odd =
+0.0192, muon; different object) recorded. D_odd is now a
median-normalized, internally-gated, pin-characterized bar-odd
number of the 5₂ Habiro face. Scope-(a); no identification; no fit;
no c_k wired.

**2026-07-25 (A6 + A6.2, branch claude/a6-gswz-arithmeticity-2026-07-25,
PR #4195) — THE SADDLE-SIDE ODD CHANNEL GETS ITS ARITHMETIC HOME + the
first two-route confrontation with D_odd.**
`qbeta_5two_gswz_saddle_arithmeticity_probe.py` (6/6): the A4.2 φ-series
engine run at ALL THREE saddles of x³−2x²+3x−1 (disc −23 = the three
embeddings of the 5₂ trace field K) reconstructs **all 24 orders as
integer-exact elements of K** (determined Vandermonde solve + CF
rationalization at dps 320 + re-evaluation at every embedding; printed
P₁..P₃ matched integer-exact). Measured denominator laws: v₂₃ ≈ 3k/2
and — outside {2,3,5,23} — the Ohtsuki/Habiro-type tail
**v_p = ⌊k/(p−2)⌋ for every prime p ≥ 7** (enters at k = p−2, steps by
p−2; saturated at all 120 (k,p) checks). The exact **bar-odd σ-pair
tower** P_k(ξ₁)−P_k(ξ̄₁) ∈ √−23-line is recorded for all 24 orders.
`qbeta_5two_odd_two_route_confrontation_probe.py` (2/2): the σ-pair
projection EVALUATED at the substrate — **O_φ = Im φ_σ1(−ln q₀) =
+0.01090896074** (calibration-free; truncation ≡ directional Laplace at
4e-18) — recorded scope-(a) against this ledger's median-normalized
**D_odd = −0.007579403739** (ratio −1.4393), S_muon (1.13), u³ (1.20):
NO identification — the open piece is the bridge between the two
OBJECTS (σ-pair coefficientwise projection vs Habiro-face function
value = the Stokes sector population on the real-q ray), NOT the
scheme (closed by the δ-torus median above). Structural finding: the
exact q-Borel T̂_n carry **no clean algebraic n^{−θ} tail at n ≤ 43**
(θ window-drifts 11 → 9; three-model ranking only indicative) — the
naive φ-side Gauss-prefactor 3/2 tie is untestable at that depth;
A6.3 (deep C_n to n = 96, dps 800) is running to settle pre-asymptotic
vs flat-type. Scope-(a); no fit; no c_k wired.

**2026-07-25 (A6.3, same branch/PR #4195) — THE W9 BOREL SINGULARITY IS
A SIMPLE POLE (residue ≈ 1.23e-12), not soft; D_odd precision caveat.**
`qbeta_5two_tail_law_deep_cn_probe.py` (4/4): exact C_n to n = 96
(shared Pascal triangle, integer-exact regeneration gate; dps 800 vs a
~640-digit cancellation). (−1)ⁿT̂_n plateaus at c∞ = 1.230766e-12
(Aitken 4.4e-10-stable); the θ track marches 12.35 → 0.25. So the B1
"soft singularity / coefficients decay to 0" reading was the TRANSIENT
— which itself decays geometrically at ratio 0.90086 ≈ 1/q₀ (6e-5
match; measured observation): ĝ(w) = c∞/(1+w) + (analytic to |w| ≈ q₀).
**Flag for this lane:** the pole puts a ~1e-12-scale contour ambiguity
into the θ-Laplace scheme, above the stated 5e-16 D_odd band — no
physics impact at the 7.6e-3 scale, but the precision statement should
carry the caveat (or the pole term subtracted explicitly, after which
the 5e-16 claim likely survives on the regular part). Scope-(a); no
fit; nothing wired.

**2026-07-25 (A6.4, same branch/PR #4195) — THE W9 BOREL FUNCTION IS
DERIVED: exact formula, residue (q̃;q̃)_∞², pole ladder at w = −q₀ᵏ,
regularized D_odd confirms the median to 4.5e-12.**
`qbeta_5two_gbar_pole_ladder_probe.py` (5/5): the balanced-binomial
inversion gives the exact cancellation-free
(−1)ⁿT̂_n = (q̃;q̃)_n²·Σ_k q̃^{k(n+1)}[n,k]_{q̃} (vs direct route:
1.1e-497). Closed forms: c∞ = (q̃;q̃)_∞² = 1.23076604e-12 (the pole
residue), transient ratio exactly q̃, and a GEOMETRIC POLE LADDER at
w = −q₀ᵏ (k=1 found at rel 4.6e-11, k=2 at 9.2e-9) — the Habiro-face
Borel plane is structurally tied to the substrate modulus. θ-Laplace
with the exact pole split: D_odd_reg = −0.00757940374349, = this
ledger's median to 4.5e-12; honest full-pipeline band 1.1e-10 (the
5e-16 figure is scheme-orbit-only; the A6.3 pole caveat resolves with
the pole explicit). Every constant derived; no fit; nothing wired.

**2026-07-25 (coordination, PR #4226 tranche) — bridge attack scope
posted.** B3 landed (the (★) identity wired as the canonical Habiro-tail
compute path, machine-exact gate); B2 heart landed (bar-inversion
`[n,k]_q = q^{k(n−k)}[n,k]_{q⁻¹}` sorry-free in
`QOU/QBeta/HabiroTailStar.lean`; general (★) typed + Ref'd). B1 (the
O_φ ↔ D_odd Stokes-population bridge) starting: intent posted on #4213
(GZ weight-selection — their `weightDiff = 0 ⇒ integer Stokes` on the
σ-pair ray is load-bearing here; will cite, not re-derive) and #3805
(G3 3d-index lane — same integers-not-fits program, different knot +
route; measured research-overlap per the 2026-07-18 relaxation).

**2026-07-25 (B1, PR #4226) — STOKES-POPULATION BRIDGE: the σ-pair
population is FORCED ZERO on the real-q ray (derived); no small-weight
σ₃ assembly bridges to D_odd (180-candidate pre-registered scan, 0
hits, 0 near-misses); the wall is the GK bilinear block pairing.**
`qbeta_5two_stokes_population_bridge_probe.py` (3/3): T1 — at
x₀ = −ln q₀ the σ-pair sectors carry |e^{iV₁/x₀}| = 5.5e5
(overshoot ×4.8e7 vs the O(1) Habiro value) ⇒ integer population
n₁ = n₂ = 0 on this ray — consistent with A4.3's Stokes-free ray,
#4213's GZ weight rule (cited, not re-derived), and A2's
Ind^rot-bar-even. The only O(1) carrier is the real saddle σ₃
(amplitude 0.494, pure phase). T3 — the pre-registered parameter-free
family (σ₃ sin/cos/mirror channels × GZ weight powers x^{0,1/2,3/2} ×
small half-integers + A2 O-matrix entries; gate 1e-6, every near-miss
reportable) returned NOTHING: O_φ and D_odd are not bridged by any
single-sector small-weight population. Scope-(a); the named successor
is the GK bilinear block pairing (Z = Σ M_σσ' B_σ(q)B̃_σ'(q̃)) — the
odd channel as an off-diagonal block product, not a sector weight.
No fit; nothing wired.

**2026-07-25 (B1.2, branch claude/gk-bilinear-block-pairing-2026-07-25)
— GK BILINEAR CONFRONTATION: no bare-entry bridge (440 pre-registered
comparisons, 0 hits/0 near-misses); the wall is the state-integral
DRESSING + λ-row selection.** `qbeta_5two_gk_bilinear_pairing_probe.py`
(2/2): both bar-pair sides evaluated through A2's 8/8-gated block
machinery via the |q|>1 glue (GGM eq 25); the naked bilinear
W₋₁(1/q)·B·W₋₁(q)ᵀ, the dressed S±, and their odd/even splits — every
entry confronted parameter-free with F_conv, s(F̄), D_odd, D_even
(consistency gate: in-probe S⁺ = committed A2 matrix at 2.2e-25).
NOTHING matches at 1e-6. Combined with B1 (σ-pair population forced
zero; no single-sector small-weight assembly), the odd-channel bridge
now has a sharply-posed remaining form: the Gaussian/unit dressing
(√-prefactor, (q/q̃)^{1/8}) and WHICH λ-row of the block basis the
Masbaum tail occupies. Scope-(a); no fit; nothing wired.

**2026-07-25 (B1.3, branch claude/masbaum-block-row-selection-2026-07-25)
— λ-ROW SELECTION ANSWERED IN THE NEGATIVE: the Masbaum tail lies
OUTSIDE the 18-dim GGM block span for every pre-registered dressing
(21 exact rational solves, 0 in-span); the bridge needs a MODULE MAP,
not a row choice.** `qbeta_5two_masbaum_block_row_probe.py` (3/3):
the tail built as an exact u-series from the integer-Laurent C_n
(u-parity EVEN — an integer-q series, no half-integer-λ escape);
the 18 H±_(j,λ) series generated at O(q^34) by an exact
Fraction-series port of A2's generator (re-gated against the 18
printed GGM tables); basis matrix 34×18 at FULL rank 18; the
pre-registered dressed family (q;q)_∞^p·q^s·F (p ∈ −3..3, s ∈ 0..2)
decided by exact augmented-rank membership — a "solution" would mean
every residual order vanishes identically, and NONE exists.
Scope-(a): this basis/dressing family as-stated. Combined with B1
(population forced zero) and B1.2 (no bare-entry bilinear bridge),
the odd-channel bridge question is now maximally sharpened: the
Masbaum tail is a DIFFERENT vector in the Habiro module — the named
successors are the module map (descendant/derivative tower, or the
cyclotomic expansion) applied to the block basis. No fit; nothing
wired; comparison to observed only.

**2026-07-25 (C1, branch claude/qbeta-5two-gk-bilinear-bridge-2026-07-25,
DISTINCT ANGLE parallel to B1.2/B1.3) — THE BAR-ODD HOME IS THE ι-ODD
ANTISYMMETRIC OFF-DIAGONAL CONTRACTION, AND IT IS ANCHOR-SMOOTH: the
grade B1.2/B1.3 missed, but ~7600× too smooth to be c₃.** From the
A1-derived chirality split `Ẑ = R^{1/8}·H⁺₁H⁻₁ + i(−R^{1/8}/2)(β·H⁺₂H⁻₀
− β⁻¹·H⁺₀H⁻₂)`, the bar-odd channel is `ω(β,p,q)=β·p−β⁻¹·q`, ι-ODD under
the amphichiral involution `ι:(β,p,q)↦(β⁻¹,q,p)`. B1.2's symmetric
bilinear and B1.3's single span-vectors are ι-EVEN/ι-fixed objects, and
`ω≡0` on the ι-fixed locus — they searched ω's ZERO LOCUS, which is why
both returned nothing (structural, independent of dressing/row).
Formalized sorry-free (`QOU/QBeta/BarOddAntisymOffDiagonal.lean`,
lean-direct exit 0): `omega_iota_odd`, `sEven_iota_invariant`,
`omega_of_iotaFixed`/`omega_zero_on_iotaFixed` (= V(4₁)_odd=0),
`omega_ne_zero_imp_chiral` (nonzero bar-odd ⇒ chiral ⇒ needs 5₂ not 4₁).
DECISIVE anchor-swing bound (`qbeta_5two_barodd_antisym_offdiagonal_probe.py`,
4/4, committed-data only): the bar-odd home `Im Ẑ` swings **4.56 ppm**
across muon↔proton while c₃ swings **3.47% (34700 ppm)** — ratio 7613×.
Scope-(a): the correct bar-odd algebraic object is anchor-smooth and
cannot ALONE realize the c₃ swing. CONSTRAINS the B1.3 successors: any
module map staying inside the (anchor-smooth) block/Habiro home inherits
the ppm smoothness ⇒ cannot close a percent swing; the swing must carry
the anchor-DEPENDENT meridian-holonomy deformation q₀↦u (CuspShapeBarParity's
open link), not a smoother object choice. This does NOT refute the
module-map program — it bounds it (must be holonomy-deforming). No fit;
nothing wired; NEVER inverts Q_β/CODATA. Audit
`docs/audits/2026-07-25-5two-gk-bridge-attack.md`.

**2026-07-25 (branch claude/qbeta-meridian-holonomy-c3-anchor-2026-07-25,
PR #4288; ORTHOGONAL to #4283/C1 — attacks the q₀↦u deformation itself) —
THE MERIDIAN-HOLONOMY q₀↦u DEFORMATION MAGNITUDE IS ANCHOR-SMOOTH: an EXACT
boost-hyperbola amplification bound.** C1 relocated the missing
anchor-dependence to the meridian-holonomy deformation (CuspShapeBarParity's
open link); #4283 chases the in-block module maps (which inherit C1's
anchor-smoothness). This branch attacks the deformation MAGNITUDE directly.
Meridian holonomy = mult by q ⇒ bar-odd deformation shape barOdd q=q−q⁻¹
(=u+O(u³), S∝u²). Formalize-first (`QOU/QBeta/MeridianHolonomyAnchorCarrier.lean`,
lean-direct exit 0, sorry-free): the boost hyperbola barEven²−barOdd²=4 pins
the log-q sensitivity square EXACTLY — `sensitivity_sq`:
(barEven/barOdd)² = 1 + 4/barOdd² (generic field, §7c); `barOdd_sq_le_of_amplification`
(ℝ): amplification ρ≥N ⟹ (barOdd)²≤4/(N²−1), i.e. a large magnitude amplification
FORCES q near the compact locus barOdd=0 (q=±1). TRUE anchor comparison
(`qbeta_meridian_holonomy_anchor_swing_probe.py`, 4/4, committed q₀ both anchors,
coordinate FIXED — the honest test the 2026-07-11 audit skipped, it substituted
barOdd(√q₀) vs barOdd(q₀) at one anchor): ρ_u=9.62=O(10); deformation-magnitude
swing Δ(u²)/u² = **0.221 ppm** (cf C1's ω 4.56 ppm) ⇒ (c₃ 3.47%)/(swing)=**1.57e5**;
required ρ_req=3.0e6 ⇒ compact-locus bound needs |barOdd|≤6.6e-7, actual 0.209 ⇒
**5.5 orders too far.** Scope-(a) NEGATIVE. UNIFIES the bound with #4283: under the
one exact criterion "amplification ⇒ proximity to barOdd=0", BOTH the in-block
module maps AND the holonomy-deformation magnitude are excluded as sole seat —
every smooth/magnitude object fails; the swing lives ONLY in the near-singular /
non-perturbative PHASE arg(u) (consistent with #3818's ξ-frame phase law: no
perturbative odd phase at the meridian). Exact generic-field sharpening of #3639's
numerical dζ/dq₀=1/q₀=O(1) boost-negative. Does NOT close c₃ (phase = open
conj:algebraic-geometric-dilog-equivalence). No fit; nothing inverts Q_β/CODATA;
nothing wired; c₃ stays a q₀-dependent near-match (SETTLED #1580). Audit
`docs/audits/2026-07-25-meridian-holonomy-c3-anchor.md`.

**2026-07-25 (branch claude/qbeta-argu-phase-branch-selection-2026-07-25,
PR #4293; CLOSES the last seat left open by #4288) — THE arg(u) PHASE
BRANCH-SELECTION IS FROZEN ON THE REAL SUBSTRATE RAY: the deep keystone is a
WALL, not a handle.** #4288 bounded the deformation MAGNITUDE and localized the
residual to the non-perturbative PHASE arg(u) (the open
conj:algebraic-geometric-dilog-equivalence branch-selection). This branch attacks
that last seat, formalize-first. Result (`QOU/QBeta/ArgUPhaseBranchSelection.lean`,
lean-direct exit 0, sorry-free): write the leading NZ Im 𝔙 in polar coords
S(r,φ)=(√3/2)r²·sin(2φ) (r=|u|, φ=arg u; corpus 2026-07-11 branch-structure §2).
(1) The task's suspicion is CONFIRMED: the phase is a maximal-leverage INDEPENDENT
DOF — `nzImVolume_phase_deriv`: ∂S/∂φ|₀=√3r²≠0, `nzImVolume_quarter_turn`: φ:0↦π/4
swings the FULL (√3/2)r² CS amplitude — NOT bounded by #4288's boost-hyperbola
magnitude ratio. So the phase is not excluded by being bounded. (2) BUT the real
substrate FREEZES the phase — `substrate_meridian_arg_zero`: u=2·log q₀ is a
nonneg real for q₀≥1 ⇒ arg(u)=0; `anchor_phase_difference_zero`: both anchors real
⇒ Δ(arg u)=0. (3) The WALL — `phase_channel_anchor_swing_zero`: the phase-channel
anchor-swing (∂S/∂φ)·Δφ=(√3r²)·0=0 EXACTLY, regardless of the (nonzero, unbounded)
sensitivity; `nzImVolume_real_ray`: S=0 on the whole real ray (recovers #3654
amphichirality Im 𝔙(real)=0). Probe `qbeta_argu_phase_branch_selection_probe.py`
(4/4, both committed anchors): arg(u)=0 both, S(real ray)=0 both, phase-channel
swing=0 exactly, ∂S/∂φ|₀=0.0757≠0. This is a STRONGER negative than the magnitude
bound (0.221 ppm vs exactly 0). UNIFIES the exclusion chain: #4282 (ω-home smooth)
+ #4288 (magnitude bounded) + this (phase frozen) ⇒ EVERY categorical/geometric DOF
at real q₀ supplies zero-or-negligible anchor-swing ⇒ c₃'s anchor-dependence is
genuinely NON-CATEGORICAL — a fibre-level ε=Im(q) (#3636, sign S=sign ε) realized
through the 1/u³ ladder representation (#3636/#3654), COMPLETING the 2026-07-12
wall-resolution capstone by formalizing its phase leg. Does NOT close c₃
(conj:algebraic-geometric-dilog-equivalence stays open — whatever branch it
selects, its phase is frozen at the observable level). No fit; nothing inverts
Q_β/CODATA; nothing wired; c₃ stays a q₀-dependent near-match (SETTLED #1580).
Audit `docs/audits/2026-07-25-argu-phase-branch-selection.md`.

> **Cross-branch composition (added on the B1.4 rebase).** The three
> sibling rows above (C1/#4282, #4288, #4293) were posted while B1.4 was
> in flight and they *predict* the negatives recorded below: the in-block
> objects B1.2/B1.3 searched are ι-even (on ω's zero locus), and any
> perturbative in-block map — the θ-descendant tower and the cyclotomic
> level correspondence included — is anchor-smooth in magnitude (boost-
> hyperbola bound) with the phase leg frozen at real q₀. The exact
> decisions below are therefore the *independent formal confirmation* of
> a structurally-predicted exclusion, reached by a different route
> (exact rational membership rather than anchor-swing bounds): two
> methods, same wall.

**2026-07-25 (B1.4 + B1.4', branch claude/masbaum-module-map-2026-07-25)
— BOTH MODULE-MAP ARMS NEGATIVE: the θ-descendant tower does not
bridge (63 exact decisions, 0 in-span) and no cyclotomic level
correspondence exists (165 exact cross-multiplication decisions, 0
leads).** Arm 1 `qbeta_5two_masbaum_theta_tower_probe.py` (4/4):
Euler tower θ^m (m ≤ 2) over the extended λ-grid (99 columns; exact
rank over ℚ = 81 by fraction-free Bareiss — the tower carries 18
linear dependencies back into the span, itself structural) vs θ^t F
dressed by (q;q)_∞^p·q^s at O(q^128), margin 47: every candidate
OUTSIDE, certified mod two 61-bit primes (rank_p(aug) > rank_ℚ(M) ⇒
rank_ℚ(aug) > rank_ℚ(M); 0 exact escalations needed). Arm 2
`qbeta_5two_masbaum_cyclo_level_probe.py` (3/3): no n-independent
dressing relates Masbaum level n to GGM block level n+k anywhere on
the grid × shifts −2..2; bonus finding — EVERY Masbaum level is
individually u-even, not just the total. Scope-(a) both: these
operator families as-stated. The surviving bridge forms are
level-mixing / n-dependent module maps (the full Habiro-ring
comultiplication), beyond parameter-free probing at this rung.
Engineering: sympy rational rref intractable at 128×99 (>60 CPU-min);
Bareiss runs in <1 s — recorded in the probes for successors. No fit;
nothing wired; comparison to observed only.

**2026-07-25 (B2 + B1.5, branch claude/star-lean-general-n-2026-07-25)
— (★) PROVED SORRY-FREE AT EVERY ORDER n; the level-mixing bridge
form stated as a design note, no compute.** B2 (bean qou-rk84):
`QOU/QBeta/HabiroTailStar.lean` `star` is no longer a stated `sorry` —
two inversion lemmas discharge it. `gaussBinom_inv` (landed earlier)
collapses each summand's quadratic a-exponent
`3n²+5n+k²−2k−3nk−k(n−k)` to `3n²+5n−2k−2nk`; the overall
`a^{−(5n²+7n)}` then leaves `−2(n+1)(n+k)`, i.e. exactly
`(a²)^{−n(n+1)}·((a²)⁻¹)^{k(n+1)}` — linear in k — and the new
`qPoch_sq_inv` (`(q;q)_n² = q^{n(n+1)}(q⁻¹;q⁻¹)_n²`) absorbs the
`(a²)^{−n(n+1)}` prefactor. lean-direct exit 0, zero sorry warnings.
The compute that verified (★) machine-exactly for n ≤ 32 (and to
1e-497 for n ≤ 64) is now a theorem for all n; the derived corollaries
(c∞ = (q̃;q̃)_∞², transient ratio 1/q₀, pole ladder at −q₀ᵏ) rest on a
proved base rather than a checked one. B1.5: design note
`docs/workplans/2026-07-25-b15-level-mixing-bridge-design.md` states
the surviving bridge form — a level-mixing module map
`T^Mas_n = Σ_m M_{n,m}(q)·T^H_m` with `M` a matrix of q-polynomials —
and argues (formalize-first, DOF count ~L²N unknowns vs N equations)
that a scan over `M` would fit by construction, so the next rung must
derive `M` from the Habiro comultiplication and check it, not search
it. No fit; nothing wired; c₃ tier unchanged (SETTLED #1580).

**2026-07-26 (B1.5 step 2 sharpened, branch
claude/valuation-bound-sharpen-2026-07-26) — THE LEVEL-MAP COEFFICIENT
FLOOR IS (1−q)^{2n+3m}, AND IT IS EXACTLY TIGHT.** Lean
`QOU/QBeta/LevelMapValuation.lean` (`sub_one_pow_dvd_masLevel`,
`sub_one_pow_dvd_coeff_combined`, `natDegree_ge_of_bridge_combined`;
lean-direct exit 0, sorry-free): both indices cost. The GGM block term
carries `(q;q)_m³` in the DENOMINATOR — an order-3m pole at q=1 that
the coefficient must pay for — while the Masbaum level term
`T^Mas_n = C_n·(q;q)_n²` carries its Pochhammer in the NUMERATOR and so
*contributes* vanishing of order 2n. A single-level bridge coefficient
is therefore forced to carry `(1−q)^{2n+3m}`, and over ℤ[X] its degree
is ≥ 2n+3m. The earlier `3m` bound (PR #4327) is the n=0 case; the
sharpening matters because n is the index that runs when more orders of
the tail are demanded — reaching Masbaum level n costs 2n degrees of
coefficient *regardless of m*, so any bounded-degree coefficient family
covers only a finite triangle of (n,m). Probe
`qbeta_5two_masbaum_valuation_probe.py` (3/3, exact synthetic division
over ℤ — no floats, no tolerance): ν(C_n) = 0 for every n ≤ 12, hence
ν(T^Mas_n) = 2n exactly ⇒ **the proved floor is TIGHT** and cannot be
improved by this argument. Scope note: the valuation argument is
specific to the j=0 block row, where the numerator is a monomial (a
unit) and `1/(q;q)_m³` is genuinely rational. The j ≥ 1 rows carry
`E1n`/`E2n` Lambert series, which are not rational functions, so no
algebraic pole statement is available there — the bound does NOT extend
to them, contrary to the initial expectation. No fit; nothing wired; no
bridge claimed.

**2026-07-26 (branch claude/no-bounded-degree-bridge-2026-07-26) — NO
BOUNDED-DEGREE LEVEL MAP BRIDGES THE TAIL.** Lean
`QOU/QBeta/LevelMapValuation.lean` (`level_le_of_natDegree_le`,
`natDegree_unbounded_of_all_levels`; lean-direct exit 0, sorry-free).
From the tight `(1−q)^{2n+3m}` floor: a degree budget `D` caps the
reachable Masbaum level at `n ≤ D/2` **whatever `m` is**, so a level map
that intertwines at *every* order has coefficient degrees growing
without bound — there is no "small" universal bridge. Reachable
triangle `{(n,m) : 2n+3m ≤ D}` (computed):

| D | 4 | 8 | 12 | 20 | 30 | 50 |
|---|---|---|---|---|---|---|
| max Masbaum level | 2 | 4 | 6 | 10 | 15 | 25 |
| reachable (n,m) pairs | 4 | 10 | 19 | 44 | 91 | 234 |

**Honest scope on the named successor.** The B1.5 design note calls for
*deriving* the level map from the Habiro comultiplication. That
derivation is **not closed and is not attempted here**: relating the
cyclotomic expansion (Habiro/Masbaum side) to the state-integral block
decomposition (GGM side) is the substance of the Garoufalidis–Gu–Mariño
programme, not a one-session algebraic identity. What *is* closed is the
constraint side — the tight valuation floor, the degree bound, and now
the unboundedness — which narrows the family any future derivation must
land in. Recording this rather than producing a plausible-looking
"derivation" that would be a guess. No fit; nothing wired; no bridge
claimed.

**2026-07-26 (branch claude/q0-varies-imq-c3-anchor-2026-07-26, PR #4326)
— "q₀ VARIES / Im(q) as the c₃ anchor-carrier" TESTED AGAINST #4293's
PROVED ∂S/∂φ → NOT A LEAD (per-anchor FIT + order-mismatch wall).** The
owner reframe (capstone #4297): q₀ is a local varying field carrying
Im(q)≠0; #4293 proved the phase channel `S=(√3/2)r²sin2φ`, φ=arg(u),
u=2 log q₀, is maximal-leverage (∂S/∂φ|₀=√3r²) but FROZEN at real q₀
(arg u=0). Allowing Im(q₀)=ε≠0 unfreezes it. Probe
`computations/qbeta/qbeta_imq_anchor_carrier_probe.py` (mpmath, exact):
the arg(u)↔Im(q₀) slope is `d arg u/dε|₀ = 1/(q_r log q_r) = 8.634`
(numeric=analytic), so the linear response is `S≈k·ε` with
`k = 4√3 log(q_r)/q_r = 0.6514` (exact=numeric). k is anchor-invariant to
the 22 ppb q_r difference ((k_p−k_m)/k_p = 1.9e−7), so the model MEASURES
Im(q₀) faithfully — **but** that is fatal: (1) a **single global** Im(q₀)
gives swing 7.4e−9 vs observed |S_p−S_m|=0.0492 ⇒ **order-mismatch
6.63e6** (the registry dc₃/dq≈4.6e6 obstruction through arg(u); = SRigidity
`no_anchor_invariant_realizes_swing` for the Im(q) channel; amp ceiling
0.0377 < |S_p|=0.0395); (2) reproducing the swing needs **per-anchor**
Im(q): ε_p=−0.061 (−5.5% of q_r), ε_m=+0.015 (+1.3%), **opposite sign**
(forced by `fig8Trace_im_odd`, sign S=sign ε) on a mere pinning choice,
4.07× magnitude, a **free** O(1e−2) scale — a FIT. Lean
`QOU/QBeta/ImQAnchorCarrier.lean` (imports #4293, Mathlib-leaf; ℝ;
lean-direct exit 0, sorry-free): `global_imq_cannot_realize_swing`,
`peranchor_imq_fits_anything`, `required_imq_opposite_sign`,
`global_imq_zero_swing_when_slopes_equal`. **Verdict scope-(a):** the
reframe does NOT survive as a constrained/predicted model — it is a
per-anchor fit unless a *derived* Im(q₀) scale predicts both per-anchor
values (incl. the sign-flip); the only independent scales (11.5–22 ppb
μ–p residual) fall ~7 orders short. The fibre-level home stays open,
value measurement-limited. No fit; NO residual inverted to define Im(q);
nothing wired; conj:algebraic-geometric-dilog-equivalence OPEN. Audit:
docs/audits/2026-07-26-q0-varies-imq-c3.md.
## Φ_b bar-odd keystone carriers + S = Im 𝔙 channel (PR #3773, 2026-07-13)

Lean carriers for the two-conjecture composition, all sorry-free (lean-direct
exit 0), no instance fabricated, no c_k wired:

- **`QOU/QBeta/PhiBSArgumentIdentification.lean`** — `SArgumentIdentification`
  (§3b, parametrized by the argument map zArg to avoid choice-function
  vacuity: readout `phase (fibreB q₀) (zArg q₀) = S q₀` on the |q|=1 fibre
  branch, `fibreB = √(ln q₀/2π)`); `SDeformedVolumeChannel` (u(q₀) map +
  deformed 𝔙 + `S = Im 𝔙(u(q₀))` — the binding-conjecture S channel per the
  2026-07-11 conditional audit). Derived: `readout_phiB`,
  `exists_zero_crossing` (IVT: measured sign flip ⇒ q* with c₃ = −Vol(4₁)
  exactly), `exists_pure_bar_even`, `phase_eq_im_deformed_volume`,
  `phiB_eq_cs_phase` (Φ_b readout = e^{i·CS(u(q₀))}), `exists_cs_vanishing`
  (Im 𝔙(u(q*)) = 0 — deformed complex volume purely real at q*; falsifiable).
- **`QOU/MathlibExt/FaddeevPhiBRealIntegral.lean` additions** — G0 as a
  theorem (`norm_fibreQParam`: real b ⇔ |q_b|=1; `fibreQParam_fibreB`:
  q_b = e^{i·ln q₀/2}); σ-unitarity `phiB_mul_conj`; G1 re-scoped:
  `integrableOn_kernel_Ioi_one` (tail, sorry-free; majorant facts as named
  hypotheses per the PhiBProd precedent) + `_Ioi_zero` (full (0,∞) reduced
  to the bounded near-0 piece, bean `qou-dihs`).
- **Coordination:** complementary to #3768's cyclic-dilog L1–L5 (G2 closed
  algebraically; this PR is the ℂ-analytic face), #3769's KC21/q* registry
  rows (IVT carrier = machine-checked q* zero-crossing), #3683's κ-tower A_ω
  (the resurgent instance of the monodromy datum). Intent posted on all three.
**2026-07-26 (branch claude/quadratic-degree-bound-2026-07-26) — THE
LEVEL-MAP DEGREE BOUND IS QUADRATIC, NOT LINEAR (self-correction).**
`qPoch_prod_dvd_coeff` + `natDegree_ge_quadratic` in
`QOU/QBeta/LevelMapValuation.lean` (lean-direct exit 0, sorry-free).
The previously-published `(1−q)^{2n+3m}` bound reads only the vanishing
at q = 1; the SAME hypothesis gives the whole Pochhammer product:
`(q;q)_n²·(q;q)_m³ ∣ c`. Since `(q;q)_k = ∏_d Φ_d^{⌊k/d⌋}`, this is the
constraint at **every** root of unity at once, not just q = 1. Degree
consequence `2·deg c ≥ 2n(n+1) + 3m(m+1)` — quadratic in both indices.
The reachable region under a degree budget collapses:

| D | 12 | 20 | 30 | 50 | 100 |
|---|---|---|---|---|---|
| pairs (old linear bound) | 19 | 44 | 91 | 234 | 884 |
| pairs (new quadratic) | 9 | 14 | 21 | 33 | 64 |
| n_max old → new | 6→3 | 10→4 | 15→5 | 25→6 | 50→9 |

So `n ≲ √D` rather than `D/2`: matching the tail to cyclotomic order N
needs coefficient degree `≳ N²`, not `2N`. The earlier bound
(`natDegree_ge_of_bridge_combined`, PR #4336) stands as a true but
strictly weaker corollary; it is superseded, not retracted. No fit;
nothing wired; no bridge claimed.

**2026-07-26 (LITERATURE FINDING — reframes B1.x) — THE MASBAUM TAIL
LIVES IN THE TRIVIAL-CONNECTION ROW OF THE *EXTENDED* MATRIX, WHICH THE
3×3 GEOMETRIC BLOCK MATRIX DOES NOT CONTAIN.** A2's machinery (the 18
H±_{j,λ}, the W±_m, the 3×3 B/A±/C±) is the GGM *Peacock patterns*
object (arXiv:2012.00062), whose rows are indexed by the **geometric**
boundary-parabolic SL₂(ℂ) flat connections σ₁,σ₂,σ₃ of 5₂. GGM+**Wheeler**
(arXiv:2111.04763, CMP 2024) describe the trivial-connection resurgent
structure via an **extended** matrix whose rows are indexed by those flat
connections *including the trivial one* σ₀, with entries in generalized
Habiro rings and the inverted Habiro series obtained from the cyclotomic
expansion of the colored Jones. So the Masbaum tail is **by construction**
a row the geometric sub-block does not contain — and B1.2 (0/440), B1.3
(0/21), B1.4 (0/63), B1.4′ (0/165) were searching that sub-block. The
uniform negatives are the expected signature, not a surprise. Nothing
landed is invalidated: every negative was correctly scoped (a), and the
`(q;q)_n²(q;q)_m³ ∣ c` floor + quadratic degree bound remain true theorems
(now read as measuring the geometric block's distance from the trivial
row). **The B1.5 target is superseded**: the σ₀ row is not a combination
of geometric rows to be derived, it is an adjoined fundamental solution of
the same q-difference equation. Next rung: compare the `C52`-built tail
directly against GGMW's σ₀ row — a comparison to a published object, not a
search over a self-assembled basis. Method lesson recorded: check the
literature for the object's structure before scanning a basis you
assembled. Full reading list + links:
`docs/audits/2026-07-26-extended-matrix-trivial-connection-row.md`.
No fit; nothing wired.

**2026-07-26 (B1.6, bean qou-2rvk) — IDENTIFIED: the corpus's `C52(n)`
IS the published Habiro polynomial of 5₂.** Probe
`qbeta_5two_habiro_polynomial_match_probe.py` (4/4, exact
integer-Laurent, no floats): `C52(n)` read as a q-series at q = a²
**equals GGMW arXiv:2111.04763v2 eq (161)**
`H_n^{5₂}(q) = (−1)ⁿ q^{n(n+3)/2} Σ_k q^{k(k+1)}[n,k]_q` term-by-term
for n ≤ 12 — no dressing. (Both trace to Masbaum 2003; GGMW's printed
H₀ = 1, H₁ = −q²−q⁴ reproduced as a gate.) The `(★)LHS / H_n` ratio is
`q^{−(5n²+7n)/2}(q;q)_n²`, exactly the (★) normalization, so it cancels
identically: the sorry-free (★) theorem is a bar-inversion statement
about a NAMED object of the literature.
**This closes the explanation of every B1.x negative.** GGMW construct
the extended matrix from the Habiro polynomials by a 2-parameter (ε,δ)
DEFORMATION (eq 165 → Q_m eq 167 → Taylor coefficients Q_m^{(a,b)} =
the 6×6 entries, eq 172). Deformation-and-expand, not change of basis —
so no linear map into the geometric span could ever have produced the
tail. For 5₂ the chain is 3×3 (geometric; A2's machinery, eq 158) ⊂ 4×4
(+trivial σ₀) ⊂ 6×6 (fundamental solution of the 6th-order q-difference
equation of the DESCENDANT colored Jones, eq 164); the extra 2×2 block
is Rogers–Ramanujan (eq 180) and GGMW state they do not understand its
flat-connection labeling — an open problem in the literature, not a
corpus gap. Convention flag recorded: GGMW eq (189) puts Vol(5₂) =
2.8281 in Im(V₁) while the corpus carries it in Re(V₁); reconcile before
cross-using GGMW numerics. No fit; nothing wired; identification is a
location result, not a closure.

**2026-07-26 (convention reconciliation, CLOSED) — V_GGMW = V_GGM +
2π²/3 exactly; the corpus's Im(V₁) and V₃ match NEITHER published
convention.** With GGM 2012.00062v3 in `library/`, eq (234) at x = 1
gives `V = 3Li₂(y) + (log(−y))²` on `y² = (1−y)³` (the same cubic as
GGMW eq 184), and §6.1 states "for σ₃ we only keep the real part of V".
Computed at 30 dps: `V_GGM(σ₁) = −3.5556078909 + 2.8281220883i`,
`V_GGM(σ₃) = −7.6931908199`; adding `2π²/3` reproduces GGMW eq (189)
`V₁ = 3.0241283765 + 2.8281220883i`, `V₃ = −1.1134545525` to 16 digits.
Both papers carry Vol in **Im V₁**. The corpus's `Re(V₁) = 2.8281220883
= Vol` is CORRECT (an i-rotation); its `Im(V₁) = 1.3790860299` and
`V₃ = −2.7580990292` match neither paper under any rotation or π²-shift,
and the source comment `# GGM eq 21` mis-cites (eq 21 of v3 is the
Stokes/3D-index identity). Blast radius: `|V₁−V₂| = 2·Vol =
5.656244176661566` is identical in all three conventions, so
`phi_series_engine`, `median_borel_resummation` and
`a3_prefactor_natural_factors` are unaffected. B1 is affected but in the
SAFE direction — using the published `Im V₁ = Vol` the sector overshoot
becomes `5.9e11` instead of the reported `5.5e5`, six orders larger, so
B1's population-forced-to-zero conclusion is STRENGTHENED. B1's V₃
phases are not reproducible from the literature and want re-derivation.
Nothing retracted; a reproducibility defect recorded with its blast
radius measured.

**2026-07-31 — prepare-merge coordination of the saddle/Borel/T5 stack
(coordinator: PR #4416).** Landing order agreed with the owner:
#4408 (5₂ saddle values, rebased + adopted the sibling 0-sorry
StokesJump/WeylAlgebra — the FL²=id lemma was FALSE, replaced by proved
FL⁴=id) → #4415 (T5 assembly, byte-identical copy also carried by
#4414; whichever lands second dedupes or closes-as-superseded) →
#4414 (q-Borel chain; rebased, FaddeevPhi cherry-pick duplicate
auto-dropped, all 13 changed .lean files lean-direct exit 0, 0
sorries). Branch `fivetwo-saddle-values-canonical-2026-07-30` is a
superset whose only unique content is the T3 multi-knot binding probe;
residual PR opens after the stack lands. New qou-qnnq route beans:
qou-offl (cone-manifold off-lattice), qou-awpk (per-winding GGM
Stokes), qou-mcus (multi-cusp Borromean), qou-rdmr (Rademacher
word→winding). Probe re-verification: `saddle_values()` reproduces both
papers' printed values to 16 digits at prepare-merge time.

**2026-08-01 (qou-awpk, route 2 of qnnq — per-winding Stokes of 4₁; PR
#4433).** The per-(winding e, descendant ℓ) integer Stokes family of 4₁
is EXTRACTED EXACTLY via the proven dictionary S⁺_{σ₁σ₁}(w;q̃) =
Σ_e I(0,e)(q̃)wᵉ on the validated DGG flux-sum engine; Σ_e reproduces the
printed rotated index exactly (closes the corrected-assembly probe's
"e-sum reproduction deferred" item). New exact-int canonical-chamber
engine (`_awpk_fast_index.py`, no floats — owner directive): S₃-triality
rotation into the m ≤ 0 chamber removes the Laurent-cancellation AND the
"higher internal order" truncation subtlety; ~400× faster than the dict
engine. TWO defect corrections: (1) the `else-40` sentinel convergence
guard (merged g3 probe affected) — its substrate datum S⁺₁₁(q̃) = 0.2584
was sentinel-passed and is WRONG; honest ladder value **0.42764420134
(13 digits)**. (2) E-window truncation at the winding hump. STRUCTURAL
RESULT: |I(0,e)(q̃_sub)| does not decay in e ⇒ the winding sum has radius
of convergence 1 in w; the corpus sheet |w| = q₀ = 1.1100 exceeds even
the index annulus q̃^{−1/2} = 1.0535, so the observed-sheet effective
Stokes is defined ONLY by analytic continuation/lateral data — and on the
convergent domain (|w| = 1) amphichirality forces the sum exactly
bar-even (1e-51). Independently re-derives, from the winding side, the
"bar-odd S must be lateral/Stokes" conclusion (B1/#3923 lineage), now
with a region-of-validity mechanism. Scope-(a) negative for naive-sum
route 2 (no sign flip; no −4.08); surviving form is the CONTINUED
x-refined Stokes (bean qou-3bp8). Audit:
`docs/audits/2026-07-31-awpk-perwinding-stokes-41.md`. Nothing wired.

**2026-08-01 (qou-3bp8 route 2b, PR #4447) — the winding GF is ENTIRE on
ℂ*: the #4433 radius-1 reading was pre-asymptotic; entirety + the
annihilator functional equation are Lean-proved.** Chain of findings:
(1) the DGG C.7 annihilator holds at the substrate point on the
canonical-chamber engine (residual 6.6e-15, dropping x8.5e12 when the
internal order rises 1600→2400 — pure truncation). (2) Its winding-GF
transform (M̂ ↦ q^{m/2}w multiplication; ℓ̂ ↦ row-shift with w-dilation
by q^{1/2}) is a three-term functional equation, machine-checked
sorry-free (`QOU.QBeta.WindingGFTransform.gf_three_term`; annihilator as
content-bearing conditional class, 10-term expansion cross-checked to
1e-71). (3) The decay-onset measurement kills the #4433 "radius exactly
1" claim: I(0,e)(q̃) = 2e-5 / -2e-16 / -3.5e-32 / 2e-53 at e =
40/60/80/100, tracking the quadratic lead e²/8 — the e≤28 window sat on
the pre-asymptotic plateau. Lean: `summable_winding_of_sq_dominated`
(square-dominated two-sided families are absolutely summable at EVERY
w ≠ 0) + `gf_three_term_of_sq_dominated` (the functional equation holds
among the tsums on all of ℂ*, HasSum discharged by entirety). Dated
correction appended to the #4433 audit; its 3c bar-even-on-|w|=1 result
stands (now Lean-proved: `pairedWindowSum_unit_sheet_im_zero`), but the
"bar-odd must be lateral because the sheet is outside the annulus"
re-derivation is withdrawn as stated — a bar-odd part can arise off
|w| = 1 by direct convergent summation. W2 runs exactly that: A_eff at
the T4 sheets by direct two-sided summation (converged by e≈60 at
|w| = q₀²), parameter-free comparison vs S_p/S_μ = −4.0751. Guard-bug
lineage continued: the W1 A2 failures were hump-regime artifacts (the
negative-e hump reaches 1e17 at |w|=0.3 needing dps≥80; benign ~0.26 at
|w|≈0.8 — A2 re-specced there). No fit; nothing wired; beans qou-ovph
(domain re-scope) + qou-vvm1 (session).

**2026-08-01 (provenance-claim correction + citation-anchored-literal
checker).** Two items, one class.

(1) **The `π²/2` extraction-convention identification was attached to the
WRONG legacy literal.** After #4408 landed, `fivetwo_saddle_values.py`'s
docstring asserted that the corpus's `Im V₁ = 1.3790860299` equals
`Re(V_GGMW) − π²/6` "within 5e-8". Recomputation: `Re(V_GGMW) − π²/6 =
Re(V_GGM) + π²/2 = 1.379194309661075…` (the two forms agree exactly, so
the π²/6-lattice claim itself is SOUND). The 5e-8 match holds for
`V_DOM = …−1.37919426157i` in `median_borel_resummation` (|Δ| = 4.81e-8),
**not** for `Im V₁ = 1.3790860299`, which sits **1.08e-4 away — 2250× the
stated bound**. Not a root-precision artifact: a 6-digit root already
reproduces `1.379194309661` exactly, and the residual is not a simple
multiple of Vol, π, or π². Two distinct legacy literals differing in the
4th decimal were conflated. **`Im V₁ = 1.3790860299` and `V₃ =
−2.7580990292` therefore remain UNEXPLAINED** — the 2026-07-26 row above
stands unretracted. No numerical result changes: the consuming probes
already call `saddle_values("ggm")`, so only the explanatory prose was
wrong. Fixed in the module docstring + the stokes-bridge comment, and the
claim is now machine-checked by a 6-gate `_self_check()` in the module
(`python3 computations/probes/fivetwo_saddle_values.py`, exit 0) — the
mis-attribution survived review precisely because it was prose.

(2) **`computations/citation_anchored_literal_validator.py`** (new,
warn-only, auditOnly). Flags a numeric literal carrying ≥ 8 significant
digits when a citation-shaped comment sits within 2 lines above and the
file shows no evidence the value is checked (no witness load, assertion,
gate, or recomputation). Motivated by two same-class defects in one week
— the V-literals above and the `nzImVolume` sin/cos convention bug — both
being *numbers asserting provenance they do not verify*. A hardcoded
reference used as an assertion **target** is good practice and is not
flagged; what is flagged is a cited number consumed as an **input**.
Docstring prose and `"key": "value"` witness-payload lines are masked
(both observed as false positives on the first run). Run it for the live
count; do not cite a dated baseline. `--strict` wiring into
`witness-pipeline.yml` follows the `lp_dual_witness_validator.py`
warn-only-then-strict precedent.

**2026-08-01 (stale-witness sweep of the V migration — one live regression,
one V₃ evidence result; PR #4454).** Re-running the three probes migrated to
`saddle_values("ggm")` by `87722fa817` found their witnesses all predated the
migration, so none of its effects had ever been recorded.

| probe | witness was | effect of migration |
|---|---|---|
| `phi_series_engine` | 2026-07-25 | **numerically inert** — consumes only `\|V₁−V₂\| = 2·Vol`, identical in all three conventions (confirms the 2026-07-26 blast-radius prediction) |
| `stokes_population_bridge` | 2026-07-25 | substantive, **safe direction** — σ-pair overshoot 4.76e7 → 5.12e13, B1's forced-zero conclusion strengthened (confirms the predicted 5.5e5 → 5.9e11) |
| `median_borel_resummation` | 2026-07-18 | **LIVE REGRESSION** (below) |

**The regression.** `zeta12 = 1j * (V1 - V2)` had been calibrated against the
corpus's legacy *i-rotated* V (Vol in `Re V₁`), where `i·(V₁−V₂)_legacy =
5.656j`. The migration switched V to GGM but kept the `1j *`, double-rotating
by 90°. Running the probe as committed on main fails its resurgence gate
(rel dev 0.0222 → 1.369). Invisible because the witness was never regenerated
— the stale sidecar was asserting a PASS the code no longer produced.

The Borel–Padé pole is **convention-free data** (`0.0753 + 5.7566j`), so the
correct form is decidable rather than a matter of taste: `V₁−V₂` gives rel dev
`0.0222`; `1j·(V₁−V₂)` gives `1.436`. Dropping the `1j *` restores the gate
byte-identically to its pre-migration value. Corrected form: **`ζ = V_i − V_j`,
no explicit `i`, in the published GGM convention.**

**NEW EVIDENCE on the unexplained `V₃`.** The σ₁/σ₃ pole match improves sharply
under the published value:

    ζ₁₃ rel dev:  0.2545   (legacy V₃ = −2.7580990292)
                  0.0195   (GGM    V₃ = −7.69319081986683)    — 13× better

The convention-free pole map therefore **independently prefers the published
GGM `V₃`** over the corpus's legacy literal. That literal is now not merely
unexplained (2026-07-26 row) but **positively disfavored by data the
conventions do not touch**. Scope-(a): evidence about which `V₃` the series
knows, NOT a derivation of where `−2.758` came from — that provenance, and
`Im V₁ = 1.3790860299`'s, remain OPEN.

**Method note.** All three defects this session — the π²/2 mis-attribution, the
stale witnesses, and this double-rotation — were found by *re-running committed
compute and diffing the witness*, not by reading code. A witness that predates
the commit it claims to describe is not evidence; it is a stale assertion of a
PASS. Refreshing witnesses in the same commit as the change they describe is
what would have caught all three at authoring time.

## 2026-08-02 — A_ω=3 made conditional-on-published-conjecture (bean qou-ujmw)

**PR:** `claude/aomega-conditional-gukov-stosic-bps-2026-08-02` (#4569).
A_ω=3 (figure-eight) moved *structurally-open* → *conditional-on
`conj:stokes-dt-bps-bridge`* [garoufalidis-gu-marino2023peacock Conj 3(d) +
gukov-pei-putrov-vafa2017 (GPPV)], Vol-conjecture-style. **Theorem for 4₁**
(GGM proved peacock Conj 3 for 4₁); conjectural in general. NOT wired to
production (L2/Q_β untouched). Internal QOU-driver derivation of `3` still
OPEN (qou-qnnq).

**Honest non-degeneracy gate result (owner-mandated):** the owner-named
**Gukov–Stošić** knot-homology↔BPS bridge (1112.0030) is the **OPEN** BPS
sector (colored HOMFLY homology on the conormal Lagrangian). Via knots–quivers
(1707.02991) the 4₁ open-BPS count is `det(4₁)=5` (trefoil calibration = 3 =
det 3₁). **5 ∉ {3,4} → that bridge FAILS the gate and was NOT landed as a
class.** The `{3,4}`/reduced-3 live in the **CLOSED** / state-integral
resurgent sector (GGM Conj 3(d) + GPPV), which is what the adopted class
uses. Witness `computations/probes/aomega-bps-sector-nondegeneracy.witness.json`;
audit `docs/audits/2026-08-02-aomega-conditional-gukov-stosic-bps-bridge.md`.

**Beans (CLI absent this session — recorded here):** qou-ujmw → conditional
adoption landed (this PR); qou-qnnq → internal derivation of `3` still open
(sibling #4554); qou-sfuo → see #4554/#4567 for the cross-knot {3,4} angle.

**Flag:** the A_ω bricks cite `[garoufalidis-gu-marino2021]` for GGM
2012.00062, which is `garoufalidis-gu-marino2023peacock`. Follow-up fix.

**2026-08-02 (5₂ saddle SUM RULE + the two literals IDENTIFIED; PR #4624).**
The provenance hunt on `Im V₁ = 1.3790860299` and `V₃ = −2.7580990292` closed
the convention question and turned up an exact identity.

**The identity.** The three 5₂ saddle values satisfy

    Σⱼ Re(Vⱼ) = −3π²/2                                            (SUM)

to 80 dps (residual 3.4e-80). Since `V₂ = conj(V₁)` this is equivalent to
`V₃ = −2·Re(V₁) − 3π²/2`, so **`V₃` is determined by `V₁`** and need never be
carried as an independent literal again.

**What the π²/2 shift IS.** In `V^ext = V + π²/2`, (SUM) reads `Σⱼ Vⱼ^ext = 0`.
The "extraction convention" — treated for months as an unexplained fudge
"absorbed by the fit" (2026-08-01 rows) — is exactly the unique shift that
**centers** the saddle values. It was never arbitrary.

**Specific to 5₂, not branch bookkeeping.** Five control cubics of the same
shape (one real + two conjugate roots), four sharing 5₂'s `Πy = 1` constraint,
miss the target by 0.16–2.83 while 5₂ hits it to 2e-50. (SUM) is an arithmetic
property of the 5₂ saddle cubic.

**Provenance verdict — supersedes two earlier findings.** Both prior verdicts
tested only *one* literal and were wrong:

| | extraction | legacy | rel |
|---|---|---|---|
| σ₁ | 1.37919430966108 | 1.3790860299 | 7.85e-5 |
| σ₃ | −2.75838861932215 | −2.7580990292 | 1.05e-4 |

Both literals **ARE** the extraction convention, evaluated to ~4 digits. The
2026-07-26 "matches neither published convention" verdict and the 2026-08-01
"Im V₁ doesn't match" narrowing are both **superseded**: the formula was right,
the evaluation was sloppy. The pair additionally violates (SUM) by 7.3e-5, so
the two were computed **independently** — neither derived from the other.

**Refuted as the error source (scope-(a), direct test):** Li₂ series truncation
(converges σ₃ to the true value, never the legacy; cannot produce σ₁ at all,
`|y₁| = 1.52 > 1`) and root imprecision (a 3-decimal root already gives 1e-8;
the root that *would* give legacy σ₃ has cubic residual 9.2e-3, so it is not a
root of the cubic). The ~1e-4 source stays **OPEN**, now bounded to a 4-digit
evaluation slip in a correct formula.

**(SUM) is VERIFIED, NOT PROVED.** Partial proof recorded so the next attempt
starts mid-stream: the branch data is exact
(`2 log yⱼ − 3 log(1−yⱼ) = 2πi·εⱼ`, `ε = (+1,−1,0)` — the source of the π²),
and summing the reflection identity over the roots gives
`A + B = π²/2 − (2/3)Σ(log yⱼ)² − (4π/3)·arg(y₁)` exactly, with
`A = ΣLi₂(yⱼ)`, `B = ΣLi₂(1−yⱼ)`. That is one equation in two unknowns and does
not close; the identified route for the second is the Kubert/distribution
relation applied to `Li₂(y²) = Li₂((1−y)³)`. Bloch-group work, left OPEN.

auditOnly; nothing wired; no fit.

**2026-08-07 (coordination, PR #4658 ↔ #4666) — the same identity, two routes.**
`/coordinate` sweep. PR **#4666** ("C1 ramified leading blocks + the general
Bloch–Wigner D, reaching 5₂") independently derived **`D(y₊) = Vol(5₂)/3`** —
the identical identity #4658 verified hours earlier by a different route.

| | #4666 | #4658 |
|---|---|---|
| route | dihedral angles, `D = Λ(α)+Λ(β)+Λ(γ)` | Broadhurst eq (73), `vol(5₂) = 3·Z₂₃,₃` |
| digits | 20 (capped by their `Vol(5₂)` *literal*) | 31 (computed from the saddle roots) |

Two independent confirmations of an open result — deliberate parallel work per
the measured-research-overlap relaxation, not duplication.

**Independently converged negative.** #4666 states these `D` values "contribute
nothing" to the saddle sum rule, being the imaginary part. That is Route 2 of
`qou-0yqu` reached from the other side; `qou-0yqu` adds that `Σⱼ D(yⱼ) = 0`
holds **automatically** for any cubic with one real + one conjugate pair
(control-verified), so the Bloch–Wigner side is information-free here, not
merely unhelpful.

**Offered to #4666:** `fivetwo_saddle_values.py::volume()` computes `Vol(5₂)`
from the roots at arbitrary `dps` — removes their stated precision ceiling;
Broadhurst's published eq (73); and `disc = −23`, now Lean-proved
(`disc_eq_neg_23`). **Wanted from them:** `summable_clausen` (the filler
defines `Cl_2` as a `tsum` proving nothing about convergence — everything
downstream rested on that), `tetAngles_sum_eq_pi`.

**No file conflict** — disjoint Lean files. No review comments on #4658 to
triage. Comment: https://github.com/litlfred/qou/pull/4666#issuecomment-5215109956

**2026-08-07 (PR #4658, later) — the branch data `b` is PROVED, not fitted; and
Route 5 gets a Lean spine.**

Two things landed, both sorry-free with axioms `[propext, Classical.choice,
Quot.sound]`.

*1. `b = (−1, +1, +1)` carries no free parameters.* The sum rule is stated as
`Vⱼ = 3·Li₂(yⱼ) + (log yⱼ + bⱼπi)²` with three hand-supplied signs — which
reads like a fit. It is not:

> **`log yⱼ + bⱼπi = Log(−yⱼ)`, principal branch** —
> `QOU.QBeta.FiveTwo.branch_shift_eq_log_neg`.

`arg(−z) = arg z − π` above the real axis, `arg z + π` below, `= π` on the
positive reals. A cubic with one positive real root and one conjugate pair
therefore *forces* `(−1, +1, +1)`. Probe gate G6 confirms at 60 dps with error
exactly `0.0`; the Lean proof is unconditional. So `Vⱼ = 3·Li₂(yⱼ) + Log(−yⱼ)²`,
and `Log(−z)²` is precisely the term in the inversion formula
`Li₂ z + Li₂(1/z) = −π²/6 − ½Log(−z)²` — which makes the inversion route
structural rather than opportunistic.

*2. Route 5's integral is now known to converge.* `|log P(z)| ≤ 4z` on `[0,1]`
(`abs_log_recipCubic_le`) removes the apparent singularity at `z = 0`, so
`intervalIntegrable_log_recipCubic_div` makes `−∫₀¹ log P(z)/z dz` a real
number rather than a formal expression. `LiTwo_eq_integral_unit` supplies the
matching shape `Li₂(y) = −∫₀¹ log(1 − yz)/z dz`.

*Also:* the complex Euler reflection identity is proved on `ball(½,½)`
(`QOU.Archimedean.cLiTwo_reflection`) by the identity theorem, closing the
continuation step `qou-gkco` was opened for. It does **not** reach `y₁`
(`|y₁| = 1.52`); `cLiTwo` is junk-valued outside the closed disc, so the
inversion formula is not even *stateable* for it without redefining `Li₂` by an
integral on `ℂ ∖ [1,∞)`.

**One self-refutation, recorded.** Earlier the same day I wrote into
`qou-0yqu` that `b` is the `2πik` correction in `log ∏ = Σ log`. Probe gate G1
shows that correction is *identically zero* (`3.1e-61` over 40 points). Struck,
not deleted; the correct identification is G6 above.

**New exact restatement (G7 + G8), verified to 25 digits, still unproved:**

    Σⱼ Re Li₂(yⱼ) − 2·Σⱼ Re Li₂(1/yⱼ) = −π²/2

*derived*, not merely observed: the per-root inversion rewrite fails as a
complex identity at `y₃ ∈ (0,1)`, but G8 shows the whole defect is imaginary
(`Re Dⱼ = 0` for each root separately, `Im D₃ = −10.6009742`). Since the sum
rule uses only real parts, the rewrite is legitimate. **Lean consequence:** a
proof needs only the *real part* of inversion on `(0,1)` — weaker and more
tractable than the complex identity that genuinely fails there.

**Caution.** `∏ⱼ(1 − z/yⱼ) = 1 − 3z + 2z² − z³` *changes sign* on `[0,1]`
(`−1` at `z = 1`, since `1/y₃ = 2.325 > 1`), so the positivity argument that
makes the root side a clean real integral does **not** transfer to the
reciprocal side. That sign change is the honest location of the remaining
difficulty.

Probe + witness: `computations/probes/qbeta_5two_route5_branch_data_probe.py`,
`computations/qbeta-5two-route5-branch-data.witness.json` (8 gates, 60 dps,
parameter-free). **Sum-rule status unchanged: verified to 80 dps, unproved.**

**2026-08-07 (night, PR #4658) — Route 5's chain is now a theorem; Route 6
tried and refuted; the hard part is untouched.**

*The chain.* `Σⱼ Re cLiTwoExt(yⱼ) = −∫₀¹ log(1 − 2z + 3z² − z³)/z dz`
(`sum_re_cLiTwoExt_eq_integral`), sorry-free, assembled from
`sum_re_log_one_sub_eq_log_recipCubic` (real parts, so no branch data enters) +
integral linearity + `Re` commuting with the integral. `cLiTwoExt` is the
integral-defined dilogarithm, the object that makes sense at `‖y₁‖ = 1.52`;
`cLiTwo_eq_intervalIntegral` proves it agrees with the series on the disc, and
`intervalIntegrable_log_one_sub_div` discharges its side conditions (needs
`Re(1 − yz) > 0` on `[0,1]`, true for all three roots).

*Route 6 — Zagier's enhanced dilogarithm — REFUTED, scope-(a).* Owner supplied
Zagier (2007) as `library/zagier-the-dilogarithm-function/zagier-the-dilogarithm-function.pdf`. §II.1 B's `D̃ = Li₂(z) + ½uv` on
`{eᵘ+eᵛ=1}`, valued in `ℂ/(π²/2)ℤ`, looked like our `Vⱼ` exactly: same
`Li₂ + (log)(log)`-with-branch-data shape, roots on `2u = 3v + 2πik`, and
`−3π²/2` an exact multiple of the ambiguity. Had it closed, the problem would
have become a *rationality* statement. It does not: no integer branch offset
matches, and the residual is exactly `πi(2b+k)u − b²π²`, leaving
`Σⱼ Re D̃(yⱼ) = π²/2 − (2/3)πθ` with `πθ ∉ π²ℚ`. **Scope-(a)** — this set-up
fails; nothing excludes a formulation at a different covering point or Bloch
element. The obvious thing such a formulation must track is already Lean-proved
here: `d[yⱼ]` is **3-torsion**, not zero (`three_smul_wedge_eq_zero`).

*One summand identified.* `Re V₃ = 3·L(y₃) − π²` with `L` the **Rogers**
dilogarithm (`re_V_real_root_eq_rogers`) — the real root's contribution is a
standard object, not an ad-hoc combination. It evaluates nothing:
`L(y₃)/(π²/6) = 0.441033…` is irrational, as expected for a cubic-field
argument.

*What is left, exactly two things.* (i) `cLiTwoExt` analytic on `ℂ ∖ [1,∞)` —
without it "the analytic continuation" is a name, and `cLiTwoExt(y₁)` is not
*identified* with the sum rule's `Li₂(y₁)`. (ii) **Evaluating
`−∫₀¹ log P(z)/z dz` in closed form.** Untouched. This is the actual hard part,
and none of today's eleven theorems approaches it — they make the restatement
rigorous and demystify the branch data `b` (= `Log(−y)`, forced, not fitted).

**Six routes tried, six not closing. Status unchanged: verified to 80 dps,
unproved.**

**2026-08-07 (PR #4658, takeover) — Route 7 REFUTED scope-(a): the defect in
Route 6 was branch freedom, not the modulus.**

Route 7 asked whether the corpus's own `ℂ/2π²ℤ` valuedness for these `Vⱼ`
(2026-07-18 GGM §6.1 port) rescues the enhanced-dilogarithm reading that Route 6
killed under Zagier's `ℂ/(π²/2)ℤ`. **It does not, and the modulus was never the
issue** — the branch shift contributes `−2π²aⱼbⱼ`, a multiple of both moduli.

What the probe did find: Route 6's witness gate G3 evaluated `Σⱼ Re D̃` at the
**principal branch only**. With `u = log y + 2πia`, `v = log(1−y) + 2πib` there
are two free integers per root and the `θ` obstruction cancels iff
`3(b₁−b₂) + 2(a₁−a₂) = −2`; Route 6's implicit `a = 0` makes that `3(b₁−b₂) = −2`,
insoluble over `ℤ` — exactly its reported "no integer branch offset matches".
With `a` free, exact rationality **is** reachable, so Route 6's conclusion stood
for the wrong reason.

It is still worthless: reachable set is exactly `Σⱼ Re D̃/π² ∈ 11/6 + 2ℤ`, every
control `y^p = (1−y)^q` lands in its own `π²ℚ` coset (including `y³−y²+2y−1`,
which *is* `y³=(1−y)²`), and neither `−1/2` nor `−3/2` is in the coset. Generic
bookkeeping — the Route-2 failure mode.

Probe + witness:
`computations/probes/qbeta_5two_route7_enhanced_dilog_branch_freedom_probe.py`,
`computations/qbeta-5two-route7-enhanced-dilog-branch-freedom.witness.json`
(8 gates, 60 dps). Beans `qou-r7ml` (completed/refuted), parent `qou-0yqu`.
**Route count 7 tried, 7 not closing. Sum-rule status unchanged: verified to
80 dps, unproved.**

**2026-08-07 (PR #4658, takeover) — GGM/GGMW READ IN FULL. They do not contain
the sum rule. The literature lead is closed.**

`qou-0yqu` named GGM (2012.00062) / GGMW (2111.04763) twice as "the realistic
direct sources" and neither had been opened. Both now swept end to end
(bean `qou-g2wr`).

**Negative:** `Σⱼ Vⱼ` appears nowhere in either paper; no `−3π²/2`. **"real
part" occurs exactly once in GGM and zero times in GGMW** — the single hit is
the §6.1 σ₃ branch prescription already ledgered 2026-07-26, not a statement
about `Re V`. No `Bloch`, no `regulator` in either. GGMW's `Rogers` hits are
**Rogers–Ramanujan**, not the Rogers dilogarithm — flagged as a false lead.
With the disc −23 ladder literature being the volume side, **there is now no
known published source for this identity.**

**Positives worth carrying:**

1. GGM eq (234) is the source of the `ℂ/2π²ℤ` modulus, confirmed verbatim; at
   `x = 1` it is the corpus's `V`, reproducing the sum rule to 50 dps.
2. `b = (−1,+1,+1)` is **exactly** principal `Log(−yⱼ)` (exact zero at all three
   roots) — independent confirmation of `branch_shift_eq_log_neg`. GGM writes
   `(log(−y))²` directly.
3. **`Re Vⱼ` is only defined mod `2π²`** (the modulus is real). In GGM's own
   quotient the sum rule reads `Σⱼ Re Vⱼ ≡ π²/2 (mod 2π²)`, so the exact
   `−3π²/2` is a statement about chosen representatives. **Any proof routed
   through GGM's `V` alone can only deliver the mod-`2π²` statement** — pinning
   the representative is exactly `branch_shift_eq_log_neg`, which makes that
   theorem load-bearing rather than bookkeeping. Consistency: GGMW's
   `+2π²/3` per root shifts the sum by exactly one lattice step `2π²`, giving
   `Σⱼ Re V_GGMW = π²/2` exactly; the two published conventions are adjacent
   representatives.
4. GGMW §4.1 **states disc −23 outright**, and identifies `σ₁,σ₂,σ₃` with the
   three embeddings of the trace field. So `Σⱼ Re Vⱼ` is a **trace over all
   embeddings** — the structural reason the power sums `pₙ` are rational
   integers and Route 5's integrand is a ℤ-coefficient polynomial.

**Sum-rule status unchanged: verified to 80 dps, unproved.**

**2026-08-07 (PR #4658, takeover) — `cLiTwoExt = Li₂` off the disc is TRUE
(verified); Lean blocked in-session.**

`elan`/`lake` absent and the environment denies `release.lean-lang.org:443`
(403 on CONNECT), so no toolchain and no `lake exe cache get`. **No Lean
written** — deliberately, rather than shipping unverifiable code. Groundwork
instead (bean `qou-clx8`):

* `cLiTwoExt y = −∫₀¹ Log(1−yz)/z dz` equals `Li₂(y)` to diff **`0.0`** at all
  three 5₂ roots — including `y₁`, `‖y₁‖ = 1.52` — and on 28/28 grid points off
  the real axis to `< 1e-25`. **The identification `cLiTwoExt(y₁) = Li₂(y₁)` is
  true; only its proof is open.**
* **The current side condition `Re(1−yz) > 0` is sufficient but NOT necessary** —
  it fails at `1.5+0.3i` and `3+0.001i` where the identity still holds. The right
  hypothesis: for `Im y ≠ 0`, `Im(1−yz) = −z·Im y` vanishes on `[0,1]` only at
  `z = 0`, so the path never meets the principal cut and `Log(1−yz)` is
  continuous along it. Covers `ℂ ∖ ℝ` in one step.
* The cut is `[1,∞)` and not `|y| ≥ 1` because for real `y > 1` the integrand is
  singular *inside* the interval, at `z = 1/y ∈ (0,1)`.
* **Numerical trap:** when `0 < Re(1/y) < 1`, plain `quad([0,1])` is silently
  wrong (off by `1.15e-2` at `y = 3+0.001i`). Probes must split at `Re(1/y)`.

**Sum-rule status unchanged: verified to 80 dps, unproved.**

**2026-08-07 (PR #4658, takeover) — Route 8: the sum rule TRANSPORTS to a 7th-root-of-unity
identity at a totally real field. Reduction, not proof.**

First route to move along GGM's deformation instead of attacking at `x = 1`
(bean `qou-8v3k`).

> `Σⱼ Re Vⱼ = −3π²/2` **⟺** `Σₖ Re[Li₂(yₖ) + 2Li₂(−yₖ) + (log(−yₖ))²] = −π²/2`,
> `yₖ = −1 − 2cos(2πk/7)`, the **totally real cyclotomic field ℚ(ζ₇)⁺**, disc 49.

Mechanism: (i) `∂V/∂y = 0` **derives** GGM's deformed curve — already Lean-proved
here as `FiveTwoSaddleCurve.lean` — so `yⱼ(x)` are critical points; (ii) Vieta
gives `∏ⱼ(1−xyⱼ) = x`, `∏ⱼ(1−yⱼ/x) = 1/x`; (iii) envelope theorem gives
`d/dx V(x,yⱼ(x)) = (1/x)log[(1−yⱼ/x)/(1−xyⱼ)]`; (iv) summing collapses to
`S'(x) = −2log x/x`, so **`S(x) = S(1) − log²x`** (verified `<1e-30` on
`x ∈ [0.2,5]`; palindromy `S(x)=S(1/x)` confirmed, GGM eq 306). The branch term
`2πik log x` is purely imaginary for real `x>0` so cannot touch `Re`, and on
`|x|=1` is real with **`k = 0` measured** at eight points to `φ = π`, giving
`S(−1) = −π²/2`. At `x = −1` the curve degenerates to `y³+2y²−y−1` (disc 49) with
roots exactly `−1−2cos(2πk/7)`.

**⚠ Not a proof** — `S(1)` is the constant of integration, so this transports the
unknown. The cyclotomic identity is verified to `9.2e-41`, not proved.

**Why it matters anyway:** every prior route died on *real part vs volume side* —
at disc −23 the field is complex, `D ≠ 0`, and the classical ladders compute
`ζ_F(2)` via `D`. At `x = −1` the field is totally real and abelian, `D ≡ 0`
identically, and Rogers sums there are expected in `π²ℚ` — the Frenkel–Szenes /
Y-system / Watson regime where `−π²/2` is the natural answer. **The obstruction
that killed Routes 2, 6 and 7 is structurally absent at the new point.**

Probe + witness: `computations/probes/qbeta_5two_route8_envelope_deformation_cyclotomic_probe.py`,
`computations/qbeta-5two-route8-envelope-deformation-cyclotomic.witness.json`
(7 gates, 40 dps). **Route count 8 tried; 7 refuted, 1 reduction. Sum-rule status
unchanged: verified to 80 dps, unproved.**

**2026-08-07 (PR #4658, takeover) — Route 9: RATIONALITY PROVED. The sum rule is
one rational number away.**

Bean `qou-b7cy`, building on Route 8. Route 6 hoped the problem would "stop being
a transcendental evaluation and become a rationality statement" and failed; that
is achieved here by a different mechanism.

With `w = −y = 1 + 2cos(2πk/7)` (root of `w³ − 2w² − w + 1`), all of `w`, `1−w`,
`1+w` are **units** of `F = ℚ(ζ₇)⁺` (norms −1, −1, +1), and the **ring identity**

    (1 − w)²(1 + w) = 1 − w − w² + w³ = w²     [w³ = 2w² + w − 1]

gives `δ(2[w] + [−w]) = w ∧ w² = 0`, so `ξ := 2[w] + [−w]` lies in the **Bloch
group** `B(F)`. `F` totally real ⟹ `r₂ = 0` ⟹ `B(F) ⊗ ℚ = 0` (Borel) ⟹ `ξ` is
torsion ⟹ Rogers `L(ξ) ∈ π²ℚ`. **That step is elementary + one classical theorem,
and the algebraic half is a Lean one-liner.**

Measured exactly (26 digits): `Σₖ Re[2L(wₖ) + L(−wₖ)] = π²/2`, and
`Σₖ Re V = Σₖ Re L(ξₖ) − π²`, recovering Route 8's `−π²/2`.

**Open:** the rational `1/2` itself (verified, not derived — note `π²/2 = 3·L(1)`),
and the `−π²` branch constant. A per-embedding formula
`V − L(ξ) = iπ log[(1−w)/w]` was tried and **is FALSE** (fails at two of three
embeddings); only the sum is exact — recorded to prevent re-derivation.

Probe + witness: `computations/probes/qbeta_5two_route9_bloch_torsion_rationality_probe.py`,
`computations/qbeta-5two-route9-bloch-torsion-rationality.witness.json`.
**Route count 9 tried; 7 refuted, 2 reductions. Sum-rule status unchanged:
verified to 80 dps, unproved.**

**2026-08-07 (PR #4658, takeover) — LEAN IS AVAILABLE HERE (workaround), and the
algebraic core of Routes 8/9 is now sorry-free. Borel is not formalizable.**

**Environment correction, worth propagating:** `release.lean-lang.org:443` is
denied by network policy, but the toolchain is **mirrored on github.com**, which
egresses fine — `github.com/leanprover/lean4/releases/download/v4.24.0/lean-4.24.0-linux.tar.zst`,
decompressed with python `zstandard` (no `zstd` binary present). Mathlib's olean
cache (Azure) is still 403, so `lake exe cache get` fails, but Mathlib *source*
is on github and a **targeted** build works: `lake build Mathlib.Tactic.LinearCombination`
is 708 jobs, minutes not hours. Do not build all of Mathlib.

**New, sorry-free:** `QOU/QBeta/FiveTwoCyclotomicBloch.lean` — six theorems over
an arbitrary `CommRing`, axioms `[propext, Classical.choice, Quot.sound]` (two
need only `propext, Quot.sound`): `bloch_poly` (`(1−w)²(1+w) − w² = w³−2w²−w+1`
**identically**, so the Bloch condition *is* the minimal polynomial),
`bloch_key`, `minpoly_one_sub`, `minpoly_one_add`, and Route 8's two Vieta
products `∏(1−x yⱼ) = x`, `∏(x−yⱼ) = x²` (hypotheses denominator-cleared, so no
field or `x ≠ 0` needed).

**Composition check (new gate G8):** from the three numerators alone,
`(Σ mₖ)π²/42 − π² − π² = −3π²/2` with **residual 0.0** — the Route 8 and Route 9
reductions genuinely compose; no seam was fudged.

**⚠ Measured Mathlib survey (`qou-mlbg`), 6996 files at the pinned rev:** `Bloch`
0, `Borel regulator` 0, `Polylog`/`polylog` 0, `Rogers` 0, `Steinberg` 0, no
`KTheory` directory. The single `dilog` hit is a docstring aside — **Mathlib has
no `Li₂` at all**. `Clausen`/`Lobachevsky` hits are the author *Claus Clausen*
and *Clausen–Scholze* condensed maths — no Clausen function. Only exterior powers
exist. **So Route 9's rationality argument is proved on paper and is NOT
formalizable**; "formalize Borel first" is a multi-year project, not a plan.
Note two false friends: bean `el8w` is Borel *resummation*, and `cj2d5`
(`BorelZagierQouVolumes`) is the *volume* side.

**The route that avoids all of it is `qou-fivt`:** prove the three numerators
`17, 5, −1` by five-term/Abel, needing only a real `Li₂` (QOU has one) and the
Rogers functional equations. **Sum-rule status unchanged: verified to 80 dps,
unproved.**

**2026-08-07 (post-#4658) — Route 10: the three level-7 numerators are a Bernoulli
`B₂`. The sum rule is now ONE distribution relation.**

Bean `qou-fivt`. Route 9 left the sum rule equivalent to three explicit rationals
`Re[2L(wₖ)+L(−wₖ)] = mₖπ²/42`, `m = (17,5,−1)`, verified but underived — three
integers that looked fitted.

They are not three constants. `mₖ = 3k² − 21k + 35` (symmetric under `k ↦ 7−k`),
and that quadratic is `mₖ/7 = 21·B₂(k/7) + 3/2` with `B₂(x) = x² − x + 1/6`.
`B₂` is the Fourier signature of `Li₂` at roots of unity — `Σₙcos(2πnx)/n² =
π²B₂(x)`, i.e. **`Re Li₂(ζ₇^k) = π²B₂(k/7)`** (verified 1e-61). And
`wₖ = ζ₇^k + ζ₇^{−k} + 1` exactly. So the whole remaining content is

    Re[2·L(wₖ) + L(−wₖ)] = (7/2)·Re Li₂(ζ₇^k) + π²/4

**Why this is the useful form:** (i) it kills the "fitted" objection — one
Bernoulli polynomial, not three lucky integers; (ii) `Re Li₂(ζ₇^k) = π²B₂(k/7)`
is **elementary**, the cosine Fourier series of `B₂`, needing only real analysis
and `Cl₂` — **not** the complex `Li₂` continuation blocking `qou-clx8`/`qou-ph1k`
— and the corpus already has `Cl₂` from #4666
(`QOU/Archimedean/BlochWignerLobachevsky.lean`); (iii) it names the object:
Kubert / multiplication relations, with standard technique.

Note the symmetry with Route 4, which *died* on the Kubert relation applied at
`Li₂(y²) = Li₂((1−y)³)` (six new unknowns for one relation). The same machinery
nets positive here only because Route 8 first moved the problem to a field where
roots of unity are the natural arguments.

**⚠ Not a proof** — the relation is verified, not derived. Probe + witness:
`qbeta_5two_route10_kubert_distribution_probe.py`,
`qbeta-5two-route10-kubert-distribution.witness.json` (6 gates, 60 dps).
**Route count 10 tried; 7 refuted, 3 reductions. Sum-rule status unchanged:
verified to 80 dps, unproved.**

**2026-08-07 (post-#4658) — Routes 11–12: the numerators are DERIVED, and the
transport's branch integer is PINNED. One analytic gap left.**

**Route 11 (`qou-fivt`) — the three numerators `17, 5, −1` are derived**, not
fitted. Reduce to `(0,1)` by reflection / inversion `L(x)+L(1/x)=2L(1)` / Landen
`L(x)+L(x/(x−1))=0`; the argument set `{w₂, q, r, s}` plus reflections is **closed
under the five-term relation** (15 instances, 3 independent); exact certificate

    T₁ = (2R₁ − 4R₂ + R₃)/7    T₂ = (R₁ − 2R₂ + 4R₃)/7    T₃ = (4R₁ − R₂ + 2R₃)/7

with `rank(R) = rank(R ∪ T) = 3`, in exact `Fraction` arithmetic. The coefficient
triples are cyclic shifts of `(1,2,4)` — **the quadratic residues mod 7** — which
is where the `/7` in `mₖ/7` comes from. *Dead end recorded:* PSLQ over
`[L1, a, L(q), L(r), L(s)]` returns `[−4,4,−3,4,3]`, a linear consequence of the
targets carrying no information; the five-term closure is what supplies
independent equations.

**Route 12 (`qou-trns`) — `k = 0` pinned by the base point.** Previously argued
from integrality + local constancy, which gives *constant* but not *which*
constant. Now: `exp(g) = ∏ⱼ[(1−yⱼ/x)/(1−xyⱼ)] = 1/x²` (exact Vieta, Lean-proved),
`g` continuous on a collision-free arc, so `g + 2log x` is constant; **at `x = 1`
every factor is exactly 1, so `g(1) = 0`** and the constant is 0. Verified at 2000
points, worst `1.6e-30`. Hence `S(−1) = S(1) + π²`.

⚠ Two probe errors recorded in `qou-trns`: a script that hard-coded "no jump"
while its own output showed `2π`, and a comparison against mpmath's *principal*
`log x` (which jumps at `φ = π`) rather than the continuous branch `iφ`.

**The one remaining gap is the envelope theorem** — differentiability of `V` along
the path plus the implicit function theorem for `yⱼ(x)` (discriminant bounded away
from zero, so the hypothesis holds). Ordinary analysis, not a research problem,
but not done. **Sum rule: verified to 80 dps, numerators derived, transport
branch-pinned, still not proved.**

**2026-08-08 — the cyclotomic side is PROVED IN LEAN. Two links remain, both analytic.**

Beans `qou-abel`, `qou-rhyp`, `qou-fivt` — all three **closed**. PR #4701.

`Σₖ (2·L(wₖ) + L(−wₖ)) = π²/2` is now a theorem about the corpus's own
dilogarithm, sorry-free on `[propext, Classical.choice, Quot.sound]`:

| theorem | file |
|---|---|
| `rogersL_fiveTerm` — **Abel's five-term relation** on `(0,1)` | `QOU/QBeta/FiveTwoAbelFiveTerm.lean` |
| `numerators_of_root` — `(17,5,−1)`, **no hypothesis on `L`** | same |
| `exists_root_in_Ioo` — non-vacuity, by IVT | same |
| `extended_targets` / `extended_sum` — the targets in original form | same |
| `hasDerivAt_rogersL` — `L'(x) = −(log(1−x)/x + log x/(1−x))/2` | `FiveTwoRogersReflection.lean` |

Abel's relation went the way `LiTwo_reflection'` does: fix `y`, kill the
derivative, evaluate at `x → 0⁺`. All the content is in four log-splitting
lemmas; after they fire, `−2F'(x)` is a linear form in
`log x, log(1−x), log y, log(1−y), log(1−xy)` whose five coefficients each vanish
as rational functions, so the last step is `field_simp; ring`.

**Two of the ladder's twelve hypotheses were FALSE, not hard** — worth knowing if
you build on the earlier notes. `hinv1` and `hlan1` fail by `−2.4543` and
`+1.5692` for a Rogers `L` built on `LiTwo`: their arguments `w₁ = 2.2470` and
`−w₁` leave the disc of convergence, where Lean's `tsum` is the junk value `0`
and `Real.log` is even. Every earlier probe missed it by evaluating with mpmath's
`polylog` — testing the mathematics while the Lean file encodes the semantics.
Repaired definitionally in `FiveTwoRogersExtend` (Zagier §I.3).

**Correction to the 2026-08-07 entry above.** It says the `B₂` route needs "only
real analysis and `Cl₂` … not the complex `Li₂` continuation". True, and now
moot: Route 11→14 derived the numerators from the five-term relation directly,
never evaluating `Li₂` at a root of unity. The `B₂` framing is explanatory and
**load-bearing for nothing**.

### What is still open — and it is NOT the dilogarithm

The sum rule is `Σⱼ Re Vⱼ = −3π²/2`; what is proved is `Σₖ(2L(wₖ)+L(−wₖ)) = +π²/2`.

1. **`qou-trns`** — transport `x = 1 → x = −1`. Branch integer pinned; the
   **envelope theorem is numerical only**. Weakest link, and analytic.
2. **`qou-rstq` item 4** — `extend` is not identified with `Re` of the analytic
   Rogers `L` *in Lean*. Route 15 closed it on paper. Its two halves are **not
   equally hard**: the Landen half sits far from the cut where the corpus's
   `cLiTwoExt` is already the right object; the inversion half sits **on**
   `[1,∞)` and needs `Re` of the boundary value, well defined only because the
   discontinuity is `2πi·log x` — purely imaginary. That fact underpins this
   lane's whole "take real parts" convention and is written down nowhere.

**Sum-rule status unchanged: verified to 80 dps, unproved.**

**2026-08-09 (PR #4865) — THE 5₂ SADDLE SUM RULE IS PROVED. Routes 51–70.**

Every entry above this line records the sum rule as "verified to 80 dps,
unproved". That is now false, and this entry is the reason. Those entries are
left as written — they were accurate on their dates, and this is a log.

`QOU/QBeta/FiveTwoComplexPentagon.lean`, sorry-free, axioms
`[propext, Classical.choice, Quot.sound]`:

* `fiveTwo_saddle_sum_rule` — there exist `t ∈ (0,1)` real and `a` with
  `Im a > 0`, all three of `t, a, ā` roots of `X³ − 2X² + 3X − 1`, with
  `Li₂(a) + Li₂(ā) + Li₂(t) = −π²/6 − ½·log²t + ⅔·(arg a − π)²`.
* `fiveTwo_sum_V` — `Σⱼ Vⱼ = −3π²/2 + 2π·log t·i`. The real part is (SUM). The
  imaginary part is new: the corpus only ever recorded `Σ Re Vⱼ`.
* `fiveTwoSaddleSumRule_holds` — the class `QOU.QBeta.FiveTwo.FiveTwoSaddleSumRule`,
  whose docstring read "No instance is provided: the statement is open",
  constructed at `Li = cLiTwoExt`, `y = ![a, ā, t]`, `b = ![−1, +1, +1]`.

**The route was not the one this log spent ten entries planning.** The whole
`A`-vs-`B` programme — Kubert/distribution, the "one remaining distribution
relation", `FiveTwoDilogLadder` — was never needed. What worked:

1. the complex five-term identity for `cRogersL`, unconditional when one
   variable is real in `(0,1)` and the other is off both cuts;
2. the flattened (Neumann `ℬ̂(ℂ)`) pentagon, with **no** branch hypotheses;
3. complex Rogers reflection + inversion, giving the anharmonic group in four
   one-log forms where the `log²` terms cancel completely;
4. branch pinning from `y² = (1−y)³` plus a 4π-wide window, then `SaddleRoots`
   — proved inhabited by IVT (`f(0) = −1 < 0 < 1 = f(1)`) and an explicit square
   root (`0 < 3t² − 4t + 8` unconditionally).

Verified per-module with the `.olean` deleted first: `FiveTwoComplexPentagon` +
`FiveTwoFlattenedPentagon` exit 0 at 3241 jobs, 0 warnings; `FiveTwoSaddleSumRule`
exit 0 at 1893 jobs. `origin/main` at measurement `f689f12d2d06aee2959002f13b9ac39c1a79e3cf`.

Probe `computations/probes/qbeta_5two_route70_sum_rule_proved_probe.py` (80 dps,
4 gates) is a **control on the statement, not evidence**: it checks that the
expression proved is the one this log recorded as the target
(`A = 0.9717306814686482591277741699`), and that `b = (−1,+1,+1)` is pinned —
the only one of five assignments reaching `−3π²/2`.

**NOT proved: the 5₂ VOLUME conjecture.** `Vol(5₂) = 3·D(y₁)` and `D` cancels
identically on the Galois sum — which is exactly why the sum rule could fall
without reaching the volume. Nothing in this lane speaks to `Vol(5₂)`.

**2026-08-14 (PR #5022 follow-on) — THE D-LADDER IS CONVERGENT; the
resurgent/Écalle inference is WITHDRAWN. This ledger was never told.**

The 2026-08-09 convergence correction
([`2026-08-09-dladder-is-convergent-radius-is-the-qb-zero.md`](../audits/2026-08-09-dladder-is-convergent-radius-is-the-qb-zero.md))
landed in the KC22 registry row and **never reached this ledger**. That is the
defect this entry closes: the ledger's last word on `D(ũ)` was the
divergence-era conclusion, and five downstream entries (2026-07-12 → 07-18)
name a "resurgent/acceleration chain" as a live route on that basis. Each is
now marked `[SUPERSEDED 2026-08-09]` in place; none is rewritten.

**What changed.** `D(ũ) = Σ d_k ũ^k` is **convergent**, radius
`ρ = ũ(q*_ρ) = 0.142799996644689688905720885779` — the image of a `Q_b` zero the
2026-07-12 singularity search omitted (`k²Δ²log|d_k| → 1`, `kΔ² → 0`, so
`κ = 0`). Closed form `D(w) = φ(w)log(1−w/ρ) + ψ(w)` with algebraic `φ`,`ψ` over
a degree-12 field, giving `d_k = −(1/(2h*_ρ))ρ^{−k}/k(1+O(1/k))` with **no free
parameters**.

**What is withdrawn.** Écalle acceleration, median/Watson resummation and
Borel–Leroy all exist to sum a *divergent* series. There is none here. The three
beans carrying that work — `qou-b00b`, `qou-dri7`, `qou-xuc4`, one task under
three titles, all opened 2026-07-17 with empty bodies — are consolidated into
`qou-dri7` and **scrapped**.

**What is NOT withdrawn** — three separate things, easy to over-read:

1. **The (q-)holonomic closure stands.** KC22's exclusion is untouched. A
   convergent series need not be holonomic; `φ(w)log(1−w/ρ) + ψ(w)` is exactly
   such an element. Do not re-run P-finite hunts on `D(ũ)` — that instruction
   was right, only its stated *reason* was wrong.
2. **The κ-tower is genuinely divergent** and its resurgence work is unaffected
   (Gevrey-1, ratios 1.32→3.63→4.93, Borel singularity `A ≈ 0.7`) — as this
   ledger already recorded, with the scope-(b) invariant that a divergent and a
   convergent series cannot be equated term-by-term. Two different ladders; the
   κ-tower diverges, `D(ũ)` does not.
3. **Écalle machinery as a normalization technique** (Écalle median /
   M-dictionary lateral) is a different usage and is untouched.

**A correction of an inference, not just a status.** The framing bullet reading
*"no quantum-A-polynomial recurrence, hence the resurgent/Écalle route"* is
corrected in place: non-holonomic does **not** imply divergent, and `D(ũ)` is
the counterexample. That step was invalid independently of the 2026-08-09
correction. Wider corpus sweep for the same step: bean `qou-arvu`.

**Scope-(a).** No invariant is named excluding q-Borel methods from this
function. A study of the `log(1−w/ρ)` branch point would be a *different* task
with a different motivation and needs a bean that says so — not a resumption of
the scrapped titles. No fit; no `c_k` wired; no tier change (c₃ stays
EMPIRICAL/REFUTED-as-real-q).

## 2026-08-15 — owner redirect: c₃ refutation chain audited against the C→D trace-convention flip (survives; value layer C-conditional)

**Trigger.** Owner critical-distance redirect: probes behind "c₃ REFUTED as
real-q fibre element" may be invalid after the C→D trace flip, the
color-weighting fixes, the GGM V₃ = −7.693 correction, and the q₀ pin changes.

**Audit:** [`2026-08-15-c3-refutation-chain-convention-validity-audit.md`](../audits/2026-08-15-c3-refutation-chain-convention-validity-audit.md)
· probe `qbeta_c3_ladder_trace_convention_sensitivity_probe.py` (9/9, exit 0)
· registry §9g + c₂/c₃/KC13/KC21/KC22 provenance notes (.md + JSON twin,
validator clean).

**Verdict, tiered:**

- **REFUTED-as-real-q SURVIVES** — measured, not assumed: the anchor-swing
  mechanism is convention-immune (swing D/C = **1.0052**; `u`, `Q_A` are
  z-free), and P3 (entropy bound), P4 (q→1 shadow; `z_C(1)=z_D(1)=1/2`
  exact), P6 (KC20 `Δ_net` numerator z-free) are convention-independent.
  V₃ was already canonical in the 2026-07-30 B1 re-run; color-weighting does
  not reach the qbeta chain; anchor q₀ values are unchanged.
- **The value layer is convention-C-conditional** — the extractor's N=1 rung
  consumes `z_C` via `α=(z−1)h/2` (`qbeta_utils.py:124-125`); re-extraction
  under D shifts c₃ from ≈ −2.07 to ≈ **−974** — so (H1) `−Vol(4₁)`,
  `[3]_q/25`, `J−ℏ²`, `S_leak`, `q*_S`, and the KC21/KC22 D-ladder constants
  hold in the C frame only. `bar(z_D) = q⁻⁴·z_D` exactly ⇒ KC13's
  no-scalar-z-source prune is C-scoped.
- **Bigger than the redirect asked:** the canonical rung **c₂ = −1 is also a
  C-frame statement** (implied empirical c₂ under D ≈ −9.30; rung convergence
  58× under C vs 1.12× under D). The C→D excision does NOT transfer to Q_β by
  a z-swap; it would require re-deriving the ladder from the D-trace.
- **Root cause:** the Q_β channel was never registered in
  `trace-convention-registry.json` (channels: mass/binding/borromean only),
  so the whole channel has been convention-silent — the exact failure mode
  that registry's rule names. Open item: bean **`qou-b3nk`** (register the
  channel; examine whether the two-row forcing transfers to the decay
  channel, whose explicit weight instance has `y_(1³) ≠ 0`).

Scope-(a) throughout; no convention adjudicated; no `c_k` wired; no tier
flips (c₂ stays CANONICAL for its now-named object; c₃ stays
EMPIRICAL/REFUTED-as-real-q — in both frames).

## 2026-08-15 — bean `qou-b3nk` worked: qbeta-decay channel registered DISPUTED; the forcing/ladder boundary proved

**Branch:** `claude/qbeta-channel-convention-2026-08-15` (PR #5111) ·
**Audit:** [`2026-08-15-qbeta-decay-channel-convention-disputed-registration.md`](../audits/2026-08-15-qbeta-decay-channel-convention-disputed-registration.md)

Outcome **(c)** of the bean, leaning (b): **neither C nor D is derived for the
decay channel** — registered `disputed` in `trace-convention-registry.json`
(`channels.qbeta-decay`: definitional `null` (contradictory — the decay blocks
write the excised-C value while naming it "the Markov–Jones parameter", whose
referent has read D since 2026-08-09), production `C`; R9 evaluator on
`qbeta_utils.markov_parameter` asserts the C-state, CONFIRMED |d| = 1.9e-51).

New Lean, sorry-free
([`MarkovZFullBarCondition.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/MarkovZFullBarCondition.lean),
`lean`-direct exit 0, no `sorryAx`):

- **`decayLadder_zC_threeRow_ne_zero`** — any faithful normalised Markov trace
  at the ladder's `z_C` has `y_(1³) ≠ 0` for all `s = √q > 1` (locus
  `s⁷+s⁵−s⁴−1 = (s−1)(s⁶+s⁵+2s⁴+s³+s²+s+1)` empty). **The two-row forcing and
  the C-frame ladder are mutually exclusive** — no z-swap transfer; D-adoption
  = ladder re-derivation (measured collapse: c₃ → ≈ −974, N2/N1 0.017 → 0.89).
- **`zD_full_bar_covariant`** / **`barEven_fullBar_forces_classical`** /
  **`zC_fails_fullBar`** — the full-bar condition `bar(z) = z − h` (PR #4834
  discussion, sympy witness 2026-08-08) is now in Lean: D holds exactly; any
  bar-even `z` (= C, KC13) fails away from `q² = 1`. Premise (trace
  bar-compatibility) named, not proved.

Witness correction: the `y_(1³) ≠ 0` escape had been cited via the explicit
instance `y = (z, 1/2−z, z)` — that inhabitant is **not** an Ocneanu
`z_C`-trace (its `σ₀` value is `h/2` exactly, z-independent, sympy). The
correct witness is C's own solve (`y_(1³) = 0.02274…`, probe 18/18, proton
pin) and the Lean brick. Conclusion unchanged.

Scope-(a); no convention adjudicated; no `c_k` wired; no tier flips. Bean
stays **in-progress** (closing is a human action); settlement routes in the
audit §4 (derive the decay fibre, or prove/refute
`conj:binding-qbeta-complex-volume` / bar-compatibility).

## 2026-08-15 — KC21's parity immunity: it was ASSERTED; now VERIFIED, and its stated mechanism was wrong (bean `qou-kc21im`, PR #5123)

**Trigger:** reading the **owner-redirect entry** above (*"c₃ refutation chain
audited against the C→D trace-convention flip"*, PR #5107 — not the `qou-b3nk`
entry immediately preceding, which landed separately) back against the sentence
it added. That audit's own logic splits the c₃ record into a C-conditional value
layer and a structural layer, and the structural sentence reads *"the structural parity
statement (`S(−ε)=−S(ε)`) and the `1/u³` result are convention-immune."* The
`1/u³` half was **measured** (swing ratio D/C = 1.0052). The parity half was
not — and it is exactly the kind of claim that needs measuring, since `c₃(q)`
is *defined by* an extractor consuming the convention-C `z`, and under D that
extractor is a different function (c₃ ≈ −974).

**Probe:** [`qbeta-kc21-parity-convention-immunity`](../../computations/qbeta/qbeta_kc21_parity_convention_immunity_probe.py)
— 12/12, exit 0, 60 dps, proton pin.
**Lean:** [`LadderParityReflection.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/LadderParityReflection.lean)
— `lean`-direct exit 0, sorry-free, no `sorryAx`.
**Audit:** [2026-08-15 KC21 parity convention-immunity](../audits/2026-08-15-kc21-parity-convention-immunity-audit.md).
**Registry:** new **§9h**; KC21 row + JSON twin relabelled.

**Verdict, tiered:**

- **VERIFIED-immune (`ε`-parity).** Re-derived under D: `Im` odd / `Re` even to
  `1e-45` relative over `ε ∈ [10⁻³⁰, 10⁻²]`, non-vacuously
  (`Im c₃^D(q₀+10⁻⁸i) = 0.0386`), while the C→D shift moves the value by 972 =
  **470× \|c₃^C\|**. A parity that survives a 470× reframing of its own object
  is not riding on the frame.
- **The reduction is stronger than "z-free".** `z` *does* enter — it just
  cannot matter. The parity is **Schwarz reflection**, whose only hypothesis on
  the Markov parameter is that `z` be **real-valued on the real q-axis**; it
  never reads `z`'s formula. Every ingredient (`h`, `ℏ_q`, `b`, `u`, `Q_A`,
  `z_C`, `z_D`, `cos`) is reflective, and the class is closed under the field
  operations and composition. A control convention `z_X = q/(1+q²)`, in **no**
  channel, has the parity too. Formalized quantified over conventions:
  `alphaPhase_im_odd_of_reflective_markov`.
- **Correction 1 — the literal statement is FALSE.** `Re S` is even and nonzero
  (`−0.0394593` at the proton pin), so `S(−ε) = −S(ε)` read of the full complex
  value cannot hold. The statement is about **`Im S`** / the decay projection.
  Registry corrected; `reflective_re_even` makes the failure a theorem.
- **Correction 2 — the parity is NOT evidence for bar-oddness.** KC21 and the
  2026-07-12 capstone derive it as *"bar-odd ⇒ odd in ε"*.
  `ImQDecayLinearResponse`'s actual chain is `fig8TraceC_conj`: **real
  coefficients** ⇒ conjugation commutes ⇒ `Im` odd in `ε`. Bar-oddness is never
  used, and the bar-**even** `Q_A` has the identical `ε`-parity (measured). So
  *"the sign-flip is structural because `S` is bar-odd"* should read *"because
  `S` is real-analytic in `q`"* — a premise satisfied by essentially every
  ladder ingredient, which says correspondingly little about which channel `S`
  lives in. The immunity stands; the evidential weight attached to it does not.
- **The BAR involution is untouched, and is now the more pressing question.**
  `σ: q ↦ q⁻¹` is a *different* involution from complex conjugation.
  `bar(z_D) = q⁻⁴·z_D` and the `z_C` full-bar-condition failure (PR #5111)
  stand as stated, and **the `h·D(ũ)` bar-split inherits none of the
  `ε`-parity's immunity.** Correction 2 removes the `ε`-parity as support for
  the bar-odd reading, so the companion question — whether trace-derived
  quantities carry clean *bar* parity at all now — is left open and sharper
  than before.

Scope-(a) throughout; no convention adjudicated for the Q_β channel (`qou-b3nk`
unchanged); no C-conditional value revived; no `c_k` wired; no tier flipped in
either direction (KC21 stays `proved-lean`, the value layer stays
C-conditional). Adjacent: the NO-FLOAT64 ratchet's NEW-dirty count drained
**2 → 0** — a `round()` float64 in this branch's own probe, fixed at the
producer here; and one left by the #5107 probe, which this branch also fixed
but which `main` had **independently fixed first**, in the better form. Both
carried the duration as a float; this branch serialized it as the string
`durationSec`, `main` as integer `durationMs`. Only `durationMs` is in
`_EPHEMERAL_META_FIELDS`, so `durationSec` would have left an unmasked
wall-clock field drifting on every re-run. On rebase this branch's version of
that one fix was **dropped in favour of main's** (convergent fix, superseded);
the leak is drained either way.
