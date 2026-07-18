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
(validator green): the odd-channel element is transcendental/**resurgent**
(Écalle class) — the low-order (q-)holonomic search class is CLOSED. Do not
re-run holonomic/P-finite hunts on `D(ũ)`; the live routes are (i) the
resurgent/acceleration chain, (ii) KC19's crossing-weight `w(q)` derived from
the Φ_b state integral, (iii) canonical `c₄^even` rungs via H₄ Hoefsmit
(bean `8we6`) since extracted `c_k≥4` are noise (P4 entropy audit). No fit;
no c_k wired; no tier change.


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
shortcut past the resurgent D-ladder exists. Probe
`qbeta_eta_square_functional_g_probe.py` → witness
`qbeta-eta-square-functional-g-probe.witness.json`; audit
[`2026-07-17-eta-square-functional-g-refutation.md`](../audits/2026-07-17-eta-square-functional-g-refutation.md).
No fit; no c_k wired; no tier change.



**2026-07-17 (#3826) — κ̃₅ PREDECLARED TEST: PHASE LAW SURVIVES (residual 9.2e-9);
tower extended to 5 rungs; G3 3d-index tranche: engine certified, assembly
honestly open.** The ξ-frame phase law (#3819, from rungs 1–4 only) predicted
arg κ̃₅ = −5·arctan(t/π) = −0.166002394 IN ADVANCE (prediction committed before
the run); the 11-point ladder (N≤524288, dps 1050, 947d cancellation) measured
−0.166002385 — residual 9.2e-9, LAW SURVIVES. κ̃₅ = 210.675324 − 35.29743·i
[5d/3d]; rungs 1–4 sharpened to 22/17/13/9 digits; #3691 values reproduced.
The perturbative-null for A_ω hardens: κ̃_n/ξⁿ ∈ (−i)ⁿ·ℝ verified through
rung 5. G3 route-1 (owner-uploaded sources now in uploads/): exact-integer
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
dictionary (DGG §4.3 scout of uploads/1112.5179). Validated coefficients now in
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
where the anchor-dependence enters — and the odd-channel D-ladder q-Borel/Écalle
acceleration (sibling #3818) operating on `D(u)` where the swing lives. No c_k;
no fit; scope-(a).

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
alien-calculus / resurgence thread (D-ladder Écalle acceleration, sibling
#3818) — where the swing lives in the transseries of D(u), not in any knot's
geometry. No c_k; no fit; scope-(a).
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
