# Refocused 1-ppb workplan v4 — post Wenzl LR bridge

> **Date:** 2026-05-17
> **Predecessor:** [`2026-05-09-refocused-1ppb-workplan-v3.md`](2026-05-09-refocused-1ppb-workplan-v3.md)
> **Coordination ledger:** [`docs/coordination/1ppb.md`](../coordination/1ppb.md)

## 1. Status snapshot

Since v3 (2026-05-09), main has advanced substantially. Of the
**v3 open items**, the following have landed:

| v3 Item | State on main | Landing PR |
|---------|---------------|------------|
| P4″ ρ_K assembly path | **landed** | #564 (200× improvement, mean 0.23% MAE) |
| P3 Markov-trace y_λ at H_n | **landed** | #572 (`wedderburn_jones_markov.py`) |
| Tier-2 PSLQ extension | **landed** | #580 (third negative; K-theoretic ID outside H_3 + bridge-3) |
| Cl_2 boundary checks | **landed** | #587 |
| MarkovTraceCyclic + FarCommutes | **landed** | #589 |
| Linking predicate upgrades | **landed** | #597 |
| literal_0_782 doc-string cleanup | **landed** | #596 |
| V_(2,1), V_(3), V_(1,1,1) closed forms | **landed** | #672 (matches PR #655's c_3 / c_4 empirical values exactly — Story A falsified) |
| c_3 = J_Hopf(q=1) categorical proof | **landed** | #672 contributors via #664 (open) |
| E_0 disentanglement | **landed** | #673 |
| **Wenzl LR bridge** (producer side) | **in-flight on #674** | this PR's stacked-target |

What changed structurally:

1. **Story A falsified.** PR #672's V_(λ) closed forms match the
   empirical c_3, c_4 values exactly. The categorical chain
   produces those coefficients with no free parameter; PR #657's
   "c_k = 0 beyond c_2" reading is inadmissible, not deprioritised.
2. **m_p chain gap surfaced** (PR #671 docs-only). The
   `build_proton_mass_50dps_chain.py` reports `m_p/m_e ≈ 1.169`
   vs CODATA 1836.15, identifying three open R&D items
   (Item A: T2+T3 at A=1 KeyError; Item B: T5 categorical
   attribution; Item C: full Habiro residue).
3. **¹H "derived" was tautology** (PR #663). Restored honesty:
   all 23 isotope rows now `derivation_pending`, with
   `witness_dependency_drift.py` anti-staleness infra newly
   available.
4. **Wenzl LR producer landed** (PR #674, in flight). Rust+rayon
   module + canonical-crossing-aware binary + Python wrapper.
   ⁴He at H_12 in 173 ms (was >30 min Hoefsmit timeout).

## 2. Two distinct precision targets (clarified 2026-05-17)

**1 ppb = compute-precision target** (internal cross-method
agreement at substrate q_0). Distinct from the
**~780 ppb experimental-floor target** (CODATA Q_β uncertainty
on absolute mass predictions).

| Target | Layer | Gate |
|--------|-------|------|
| **1 ppb compute** | independent compute paths agree at q_0 to 1e-9 relative | `cross_check_trM_1ppb.py` (Hoefsmit ↔ markov_peel; in CI --strict) + `cross_check_trM_wenzl_lr_1ppb.py` (Wenzl LR ↔ both; PR #679) |
| ~780 ppb experimental | absolute mass prediction vs CODATA | `atomic_mass_via_rho_k.py` side-by-side comparison + downstream consumers |

Q_β substrate-derivation declined explicitly; experimental floor
stands. The compute-precision target is **achievable independently**
and is the gate of choice for cross-validating new methods like the
Wenzl LR bridge.

## 2a. Wenzl LR consumer bug (2026-05-17)

`cross_check_trM_wenzl_lr_1ppb.py` flagged ~80 % relative
divergence between Wenzl LR and Hoefsmit/markov_peel for D, T,
³He |tr_M| values. Root cause: the LR identity
`χ^λ(β_1 ⊗ β_2) = Σ_{μν} c^λ_{μν} · χ^μ(β_1) · χ^ν(β_2)` applies
to **tensor-product** braids only; the canonical atomic braid is
**not** a tensor product (inter-nucleon arc crossings break
tensor structure).

PR #679's `atomic_mass_via_rho_k.py` LR-overlay layer was
**disabled** after this finding. The producer
(`rho_k_full_via_wenzl_lr.py` + `hecke-tr-m-wenzl-lr` Rust binary)
remains in place as a tensor-product χ^λ primitive — building
block for a future canonical consumer that handles non-tensor
inter-nucleon braiding per
`hecke-branching-trace-decomposition.md`. Bug surfaced *by* the
new 1 ppb cross-check, which is the intended QA mechanism.

PR #663 wired a candidate substrate `Q_β = 0.7825728 MeV` (residual
vs CODATA: +306 ppm) via `form_a_cos` with c_2 = b² Kashiwara
correction — this is a *prediction*, not a calibration, per the
three-cal discipline. Promoting it to a CAL-3 = output (rather than
input) is an open governance question for the author.

## 3. What's closeable now

Ordered by yield × tractability:

1. **ρ_K consumer wiring for the Wenzl LR producer (this branch).**
   The Wenzl LR bridge from #674 produces per-partition χ^λ values
   for any atomic braid. The ρ_K refinement chain currently uses
   the *leading-order ansatz* `ρ_K^LO = (Z m_p + N m_n) / (m_e |tr_M|)`
   (PR #564's tautology). Wiring the LR-derived `Σ_λ y_λ · χ^λ`
   into a `ρ_K^full` consumer is the next substantive step toward
   the 780 ppb floor — it removes the LO tautology by providing
   per-block χ^λ data the simple ratio can't carry.
   - Dependency: PR #674 must merge first (Rust binary).
   - Scope: new script `rho_k_full_via_wenzl_lr.py` calls the
     binary, divides by `averaging_denominator`, combines with
     `y_lambda_at(n=3A, Q_0)`, emits witness with per-atom
     |tr_M(canonical β)|.
   - **Half-day** once PR #674 lands.

2. **`witness_dependency_drift.py` adoption (cherry-pick from #663).**
   The Wenzl LR witness has upstream dependencies on
   `atom_canonical_crossings` (which depends on
   `mass_at_3A_proper.atom_braid_word_3A`). Adding
   `upstream_witness_hashes` to the new witness catches silent
   staleness when the canonical decomposition changes.
   - Dependency: PR #663 must merge first.
   - **Hour-long** after #663 lands.

3. **m_p chain Items A/B/C** (open R&D from PR #671 docs).
   - Item A: T2+T3 at A=1 KeyError (cheap probe — should be the
     first attempt).
   - Item C: full Habiro residue at A=1 (cheap probe).
   - Item B: T5 categorical attribution (open R&D, no known ansatz).
   - **Days** for A/C; weeks for B.

4. **`atomic_braid_mass_table.py` deprecation completion**
   (mass-prediction consumer migration). PR #674 found this
   already had zero scope — no real consumers; only docstring
   updates remain. **Done as part of #674.**

5. **Tier-3 PSLQ extension** (`BringHyperbolicDecomposition`).
   Compute-bound, isolated from the m_p / ρ_K chain. Worth
   running if the goal is to either find the elusive relation or
   pin a fourth negative.

## 4. Not closeable without infrastructure

| Item | Blocker |
|------|---------|
| `BlochSuslinUniqueness` instance | Mathlib `Real.dilog` + Suslin map upstream |
| `ArchimedeanLimit x ∈ (0,1)` instance | Faddeev–Kashaev uniform Tauberian |
| Hoefsmit seminormal at n ≥ 5 in Python mpmath | Replaced by Wenzl LR (#674) at the |tr_M| level |
| Q_β substrate derivation | Explicitly declined |

## 5. Critical-path graph (v4)

```
                  ┌──────── ρ_K^LO tautology ───────┐
                  │   M(K) = ρ_K · m_e · |tr_M(K)|  │
                  │   landed PR #564                │
                  └────────────────┬────────────────┘
                                   │
        ┌──────────────────────────┼──────────────────────────┐
        │                          │                          │
        ▼                          ▼                          ▼
  Wenzl LR producer       Markov y_λ at H_n        m_p chain Items A/B/C
  (PR #674)              (PR #572)                 (open R&D, PR #671)
        │                          │                          │
        └─────────┬────────────────┘                          │
                  │ (this branch)                              │
                  ▼                                            │
        rho_k_full_via_wenzl_lr.py                            │
                  │                                            │
                  ▼                                            ▼
              ρ_K^full                                  m_p closure
                  │                                            │
                  └────────────────────┬───────────────────────┘
                                       ▼
                              780 ppb floor closure
                                  (per-atom)
```

## 6. Sibling-PR scope map (2026-05-17)

| PR | Layer | Status | Relevance to this workplan |
|----|-------|--------|----------------------------|
| #663 | anti-staleness infra | open, dirty | cherry-pick `witness_dependency_drift.py` after merge |
| #664 | c_3 = J_Hopf(q=1) categorical | open | precision-ladder, orthogonal |
| #671 | m_p chain gap (docs) | open | identifies Items A/B/C — bumps these into scope |
| #674 | Wenzl LR producer | in-flight | direct dependency for this branch |

## 7. Open governance questions

(carrying forward from v3 + new)

| # | Question |
|---|----------|
| Q1 | Promote substrate `Q_β = 0.7825728 MeV` (PR #663) to CAL-3 = output? Currently CAL-3 = CODATA Q_β input; flipping it would change the calibration semantics. |
| Q2 | When Items A/B/C close the m_p chain (PR #671), should the `M_P_DERIVED_MAX_REL_DIFF` threshold tighten from 1% → 1 ppm immediately, or stage at intermediate values? |
| Q3 | Tier-3 PSLQ scope: pursue if α_EM closure is still in scope, or defer until the m_p / ρ_K chain reaches the 780 ppb floor? |
