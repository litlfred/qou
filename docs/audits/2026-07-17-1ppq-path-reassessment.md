# 1ppQ path reassessment — after the 2026-07-12→14 landing wave

**Date:** 2026-07-17 · **Axis:** program-level (L1/L2 + the c_k keystone) ·
**Tier:** assessment (no new results; no fit; no c_k wired; no tier change).
Owner request: *"reevaluate path to close 1ppq based on new work on main and
active siblings in last week."* Window surveyed: origin/main 07-12→07-14
(571 commits; nothing landed 07-15..17) + 11 active sibling PRs.

## Headline state changes

1. **L1 is CLOSED.** ⁴He certification completed 07-13 (in-sandbox Rust kernel,
   H₁₂ χ-cache 77/77): **6/6 production atoms 1ppQ-certified**, χ-engine
   closed-form anchor worst |Δ| = 5.6e-50
   ([`2026-07-13-l1-4he-certification-complete.md`](2026-07-13-l1-4he-certification-complete.md)).
   The `precision-goals.md` TL;DR row ("NOT certified, 2026-06-17") lags this
   audit and needs a currency edit. **L1 requires no further math.**

2. **The Q_β odd channel has collapsed to a single well-posed problem.** KC22
   closes the *entire* (q-)holonomic search class for the bar-odd D-ladder
   (separated ℚ, coupled ℚ(√3) matrix, base-3/⅓/k q-holonomic, and log-closure
   — all refuted, prime-certified). Meanwhile the Watson/Nevanlinna–Sokal
   **uniqueness half is proved sorry-free end-to-end** (el8w:
   `watson_uniqueness_sector` on the >π sector), and the surreal appendix gives
   median resummation a formal home (`rem:st-is-median-resummation`). Net: a
   genuine c₃ closure, if any, is **transcendental/resurgent** — the one route
   left is **Jackson q-Borel / Écalle acceleration of the D-ladder** (equivalently
   the Φ_b state-integral odd carrier), with two exact structural anchors now in
   hand: the **2-adic bar-parity grading** (v₂(den b_k)=0 ⟺ k odd; 2 the unique
   graded prime — Lean-anchored) and **q\*** (the S=0 point, a third decay-sector
   determination of q₀). The D-ladder is q-Gevrey (no single Gevrey index —
   that's the 07-13 finding, not a failure), so the machinery is q-Borel, NOT
   plain Borel.

3. **Vol(4₁)/π is back in play as the even-channel Borel action** — my 07-12
   "Vol/π REFUTED (17%)" from raw-ratio Richardson is **superseded**: the
   conformal-mapped Borel plane (C1) gives A ≈ 0.646–0.657 vs Vol/π = 0.6461
   (1.7%), and the modular-resurgence probe has it consistent within spread
   (5.2%). Status: *consistent, not identified*. The raw Δr_n Richardson was the
   wrong extrapolator (subleading Borel structure); the C6 transseries now
   **derives** the κ-ladder. The route to a *derived* Stokes datum is the **GGM
   3d-index integer counts (G3)** — under active attack on **#3805**.

4. **Two adjacent legs are now single named computations.**
   - **α_EM:** four of six ingredients derived; the single wall is the photon
     1-loop determinant normalization `1/(πb₁) = 1/(8π)` on the genus-4 Bring
     **Jacobian** (proved-exact falsification: it is NOT the zero-mode measure
     1/(12π) — that fails at 1-loop by 9500σ). The θ-graph 2-loop candidate
     `−[3]_q/(8π)²` sits at **1.3σ parameter-free**, waiting on that one
     derivation, which would certify every loop order at once.
   - **W_λ keystone (McKay 2I↔Ê₈):** value map `d_q(λ) = [mark]_q` EXACT
     (marks, not exponents) + **framing-is-phase proved** (`|S_{0λ}θ_λ^f|² = W_λ`
     for all blocks). One open piece: the **colored Lawrence–Rozansky modulus
     identification** `|S_{0λ}^{Σ(2,3,5)}(ζ)| = d_ζ(λ)/D(ζ)`.

5. **Binding purged two wrong readings** (pre-registered falsifications): the
   "resonance at k=A_light" reading is dead — d/t/n-ladders ALL peak at k=3, a
   fixed 3-α Brunnian onset; and the deuteron transseries resummation undershoots
   B_D 37× at every coupling. L2 effort is now correctly aimed; count unchanged.

## The reassessed path to close L2 (still 2/7)

The five misses reduce to **two root causes and two adjacent single-computation
walls**:

| L2 miss | root cause | the (now-)named closing problem | owner/live |
|---|---|---|---|
| Q_β ~160×, m_n ~416×, Δ_pn ~159× | c₃ exact value | **q-Borel/Écalle acceleration of the D-ladder** (+ GGM Stokes integer as the monodromy datum) | G3 on #3805; **the q-Borel acceleration itself is unowned** |
| m_p ~437×, m_μ ~964× | μ–p pin tension (substrate q₀) | Subgoal-2 substrate derivation; the **W_λ / McKay route** is the live geometric approach — one piece left (Lawrence–Rozansky modulus) | McKay route landed on main; modulus ID **unowned** |
| (α_EM, headline per #3612) | loop measure | **Bring-Jacobian photon determinant** `1/(8π)` (one computation, all loop orders) | scoped on #3807's audits; **unowned** |
| (L1) | — | **CLOSED** (6/6 atoms) | done |

Strategic reading: a week ago each of these was a search over open-ended
hypothesis classes; today each is a *single named computation or resummation*
with the surrounding negative space proved closed (KC22, framing-is-phase, the
measure-falsification). That is the direct payoff of the formalize-first/
refute-honestly discipline: the searches shrank to points.

## Non-duplicative next-work options (vs the 11 active siblings)

1. **The D-ladder Jackson q-Borel / Écalle acceleration** — the single named
   odd-channel problem; #3683 owns the *even* κ-tower resurgence and #3805 owns
   the GGM Stokes integer, but the q-Borel acceleration of the *odd* D-ladder is
   unowned. Anchors: 2-adic grading + q\*. Highest L2 leverage (3 observables).
2. **The Lawrence–Rozansky modulus identification** — the W_λ keystone's last
   open piece (m_p/m_μ root cause; Subgoal-2, open for all).
3. **The Bring-Jacobian photon determinant** — α_EM's single wall; honest
   multi-week estimate.
4. **Support #3805's G3** (Stokes-integer derivation) rather than open a new
   front.

## Cross-references

- Master week docs: [`2026-07-13-alien-calculus-surreal-integration-review.md`](2026-07-13-alien-calculus-surreal-integration-review.md), [`2026-07-13-dladder-coupled-recurrence-and-2adic-parity-grading.md`](2026-07-13-dladder-coupled-recurrence-and-2adic-parity-grading.md), [`2026-07-14-alpha-em-2loop-derivability-map.md`](2026-07-14-alpha-em-2loop-derivability-map.md), [`2026-07-12-keystone-wlambda-derivation-mckay-e8-route.md`](2026-07-12-keystone-wlambda-derivation-mckay-e8-route.md), [`2026-07-13-l1-4he-certification-complete.md`](2026-07-13-l1-4he-certification-complete.md)
- Registry: [`ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md) (KC21/KC22)
- Superseded-by-this-note: the 07-12 raw-ratio "Vol/π refuted" reading in [`2026-07-12-ohtsuki-symbolic-derivation-borel-phib.md`](2026-07-12-ohtsuki-symbolic-derivation-borel-phib.md) §2 (extrapolator artifact; conformal-Padé supersedes)
