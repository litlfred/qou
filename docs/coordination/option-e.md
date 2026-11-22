# Δ_λ closure (Option-E) — master ledger

> Single source of truth for the **Δ_λ closure / per-isotope binding**
> goal. Per AGENTS.md L2 Subgoal-1: this is the closure path
> ("per-isotope Borromean-tower extension + operator-valued branching
> combiner") that unlocks the 100× targets above the CAL-2 floor.

> **🟩 Value/magnitude split (2026-08-02, PR #4590).** The per-partition
> **VALUE** `Δ_λ = (-1)^{n(λ)}·dim V_λ` is now **PROVED** sorry-free,
> general-n (`dtEuler_eq_deltaLambda_unconditional`, PR #4580) and wired to
> `delta-lambda-witness.json` (value_only). The "six ansätze failed" story
> below is about the **many-body MAGNITUDE** `r* ≈ 1.585`, *not* the value —
> the ansätze failed trying to force the magnitude into a per-block Δ_λ, which
> is structurally impossible (intensive→extensive). The pairwise log-det
> extensive candidate is proved-**capped** `ρ_A ≤ C(A,2)` (< strong ρ_4≈13),
> landing the missing term firmly at **super-pairwise**
> (`QOU.MassTheory.exchangeDet_pow_two_le_four`). **New route this session**
> (distinct from the trace/determinant magnitude attacks): the **Bloch-Wigner
> torus-operator composition** angle — free torus knots (incl. charm T(2,7))
> are Vol=0, but composed `b_i·β(T_{m,n})·b_j` closures hyperbolize and carry
> Bloch-Wigner volume = binding; probe whether inter-nucleon closures supply
> the `∝A` magnitude (bean `qou-uclw`). Full framing:
> [`2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md`](../audits/2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md).

## Why this ledger exists

Six prior Δ_λ ansätze failed (Frobenius co-Casimir, Demazure-fibre,
LP-Plancherel, LP-Frobenius, crystal-graph, augmented Markov). AGENTS.md
§Precision goals records that any 7th fit-based ansatz "will be caught
by the three-calibration discipline review". The productive direction
is **Option-E** (Kashiwara crystal) — the §L2 Δ_λ-gate context doc
explicitly endorses it as a non-fit-based attack.

Like the c_k flip-flop saga (`docs/coordination/1ppq-qbeta.md`),
Option-E has cycled through versions v1..v9 with progressively-closer
near-matches. v9 hit 0.11% on the A=3 mirror pair via a `(1+q)/2`
correction factor selected from substrate candidates — concerningly
similar to the "search for a clean-looking formula" pattern that
flip-flopped c_3 four times.

This ledger pins the current state so the next session doesn't
re-discover already-tried directions.

## Status (as of 2026-05-31)

| Sub-goal | Status | Evidence | Open question |
|----------|--------|----------|---------------|
| **Deuteron Δ_λ closure** | **NOT closed** (corrected 2026-06-17) — "+0.91% via E₀×q⁻¹" unsubstantiated: E₀×q⁻¹=3.771 (+69.5%), bare Σ=0.380 (−82.9%), apparent closure was Σ×fitted C_knot=5.852; best parameter-free = interface-knot+T3, −31% | `2026-06-17-deuteron-closure-overclaim-corrected.md` | the Δ_λ assembly gate (main `1f08f61a`: both directions blocked) |
| **Per-nucleon binding (T, ³He, ⁴He, ⁶Li+)** | NOT derived | retraction PR #1386 documents the backhanded-fit attempt | structural derivation required |
| **A=3 mirror pair (T − ³He)** | NEAR-MATCH at 0.11% | v9 commit `30c5393b7` | is `(1+q)/2` correction Taylor-exact / structurally-derived, or another near-match? |
| **A=4 (⁴He)** | NOT derived | various probes 2026-05-25 thread | requires multi-nucleon extension of the v9 mirror-pair formula |
| **A ≥ 5 (⁶Li, etc.)** | NOT derived | — | depends on lower-A closures |

**Reading (corrected 2026-06-17 — the deuteron is NOT closed):** the prior
"closed by `E₀×q⁻¹` (+0.91%)" reading was itself wrong. Re-verified, no compute
reproduces the claimed 2.24 / +0.91%: the *stated* `E₀×q⁻¹` (E₀=4.186) gives
**3.771 MeV, +69.5%**; the per-block **Δ_λ Σ-formula**
`B = m_e × |Σ_λ y_λ · χ^λ(β_D) · sgn(w_0^{S_{λ'}}) · f^λ|` (f^λ=dim(V_λ)) gives
`B(D)=0.380 MeV`, **−82.9%**; and the apparent "closure" was that Σ value × a
**fitted single-isotope constant C_knot=5.852** back-solved to AME
(`binding_energy_categorical_deuteron.py:99` itself labels C_knot "FITTED …
not a derived layer; Δ_λ gate remains open"). Best **parameter-free** deuteron
prediction = interface-knot+T3 = **1.526 MeV (−31%)**. So the deuteron is NOT
honestly closed, and no light nucleus is (Δ_λ directions blocked, main
`1f08f61a`). Cross-checks:
`docs/audits/2026-06-17-deuteron-closure-overclaim-corrected.md`,
`docs/audits/2026-06-16-deuteron-closure-crosscheck-and-correction.md`.
The A=3 mirror pair is
near-matched but not closed. **Critical:** the v9 (1+q)/2 factor was
selected from a substrate-candidate list, NOT derived. Treat as
near-match per AGENTS.md "Don't propose a seventh fit-based ansatz"
discipline.

## v1..v9 progression (DO NOT REPEAT failed paths)

| v | Approach | Best residual | Verdict |
|---|----------|---------------|---------|
| v1 | simple stats | 65.6% (D-only) | refuted |
| v2 | BK content sum | 17.4% (D-only) | refuted (coincidence) |
| v3 | multi-isotope content | 70-87% | refuted |
| v4 | naive q-Reeb | ~95% (all) | refuted |
| v5 | canonical free-vs-atom | ~99% (growth missing) | refuted |
| v6 | mirror-pair + μ₀ | 81% | refuted |
| v7 | transpose + m_π | 58% | refuted |
| v8 | transpose + Z↔N + m_π·ℏ_q | 6.15% | partial — within 10% |
| **v9** | **+ (1+q)/2 correction** | **0.11% (stale) → +0.12% (canonical q₀, PR #1707)** | **NEAR-MATCH (fit) — PROBE 1 tested; structural derivation REFUTED; A=3 closure OPEN** |

Each version's witness lives at
`computations/option-e-v{N}-*.witness.json`.
The witness commitSha pins which session produced the value.

## v9 canonical closure formula (NEAR-MATCH, not yet derived)

```
B_T − B_³He = m_π · ℏ_q · (1+q)/2 · Σ_λ y_λ · (χ^λ(β_T) + χ^{λᵀ}(β_³He))/2
```

| Component | Source | Status |
|-----------|--------|--------|
| `m_π` | CAL-3 pion mass | derived (input) |
| `ℏ_q = (q-1)/q` | substrate q₀ | derived |
| `(1+q)/2` | **NEAR-MATCH** | selected from substrate candidates; 0.11% off the required closure factor 1.05605 |
| `y_λ · χ^λ(β_T)` | Markov weights × Hoefsmit characters | computed (on disk) |
| `(χ^λ(β_T) + χ^{λᵀ}(β_³He))/2` | bar-symmetric (transpose-pair) | structural — partition transpose is the right family |

**Failure-mode signature for v10+**: if a new "substrate candidate"
matches the closure factor at the proton-pin q₀ but moves on re-pinning
to muon-pin q₀ (see `q_muon_at()` cross-check in
`tools/qou-substrate/python/qou_substrate/constants.py`), it's another
near-match. Do NOT wire as a derivation.

## Open probes

- [x] **PROBE 1 — Derive `(1+q)/2` structurally** from the categorical
  action. **TESTED → NEAR-MATCH (fit)** (PR #1707, audit
  `2026-06-02-option-e-derive-1plusq-over-2.md`). Verdict: `(1+q)/2` is
  NOT structurally forced. All four hypotheses fail: the σ_1 standard-rep
  trace (= h, −80%), its half (h/2, −90%), the Hoefsmit seminormal
  diagonal `1/[2]_q` (−53%) and off-diagonal `√([3][1])/[2]` (−18%), and
  the (2,1)-block symmetric-channel projector `q/[2]_q` (−48%) all land
  18–90% away. The only "matches" are `[2]_q/2` (unbalanced) and
  `(q+1)/2` — tautologies (literally `(1+q)/2` renamed), not independent
  derivations. The DECISIVE test: the required closure factor
  `R = target/(m_π·ℏ_q·S) = 1.05372` ≠ `(1+q)/2 = 1.05499` by **+0.12%**
  at the SAME pin — not an algebraic identity. Staleness: the published
  0.11% used the stale muon-anchor literal `1.1097090249`; at canonical
  proton q₀ the residual is **+0.12%, sign-flipped**. Corroborates the
  prior PARTIAL record (#1579 chirality-odd narrative; #1581 33-candidate
  scan). `(1+q)/2` stays un-wired; A=3 closure OPEN. No v10 ansatz.

- [ ] **PROBE 2 — A=4 extension** of the v9 mirror-pair formula. The
  mirror-pair symmetry collapses at A=4 (no canonical mirror partner
  for ⁴He). Need a different categorical operation. Per audit
  `2026-05-26-delta-lambda-binding-formula-closure.md`: ⁴He requires
  the multi-nucleon interface operator, not just the mirror.

- [ ] **PROBE 3 — Lean §3b-cond class for the v9 closure** if it
  becomes Taylor-exact. Pattern: `class OptionEV9MirrorPairClass : Prop`
  with field axiomatising the formula. NO instance until PROBE 1 closes.

- [ ] **PROBE 4 — `Δ_λ` from Kashiwara crystal** (the original
  Option-E motivation). The v9 substrate-search may have empirically
  hit the crystal weight without deriving it. Worth tracing
  `(1+q)/2` against known Kashiwara-crystal coefficients (Lecouvey,
  Brundan-Kleshchev).
  - **(2026-06-02, upstream main: `rho_w_crystal_vertex_trace.py`)
    Regular-multiplicity sum REFUTED.** Σ_w ρ_w(K) = χ^λ(β_K) by
    trace identity (n^w_λ = 1); `closure_status: does_not_close`.
    Design doc: `docs/audits/2026-05-31-rho-w-crystal-vertex-trace-design.md`.
  - **(2026-06-02, PR #1516) Cheap pass DONE — four ad-hoc closed-
    form candidates REFUTED.** Orthogonal to the regular-multiplicity
    sum above: tests χ^λ(w_0), \|χ^λ(w_0)\|, sgn(χ^λ(w_0))·dim_λ,
    peak \|ρ_λ(w_0) diag\|. All miss ≥ 66 % on the deuteron target.
    Symmetric to #1709 geometric Vol_λ refutation. Combined verdict
    (this + upstream): no single-vertex / trivial-multiplicity
    shortcut closes Δ_λ. Remaining in-Option-E path: full
    `n^w_λ` multiplicity sum (non-trivial KL polynomials) across
    multiple vertices `w` — requires extending `kazhdan_lusztig.py`
    past its n ≤ 4 cap. Witness:
    `probe-option-e-phase2-crystal-vertex-candidates.witness.json`.
    Note: the (1+q)/2 framing in this bullet is stale post-PROBE 1
    (#1707 refuted (1+q)/2 separately); PROBE 4 is now framed as
    Δ_λ closure via crystal-vertex weights rather than as a
    cross-check on (1+q)/2.
  - **(2026-06-16) KL-POSITIVITY PRUNE — full n^w_λ sum DE-PRIORITISED.**
    The target Δ_λ = sgn(w_0^{S_{λ'}})·dim is **mixed-sign** (n=3: 1+/2−;
    n=6: 6+/5−), but KL multiplicities n^w_λ are **non-negative** (KL
    positivity). So Σ_w n^w_λ·X_w supplies at most the *magnitude*
    |Δ_λ|=dim (already the deuteron f^λ); the chirality *sign* must come
    exogenously, as the closed formula already does. ⇒ extending
    `kazhdan_lusztig.py` to S_6 to run the full sum would hit a positivity
    wall — PROBE 4 is not a new closure mechanism. Honest frontier is
    PROBE 2 (A=4 interface operator), the sibling A≥3 cluster's scope
    (#2369/#2371/#2372). Audit:
    `docs/audits/2026-06-16-option-e-probe4-kl-positivity-prune.md`.
  - **(2026-06-17, PR #2416) PRUNE PREMISE NOW LEAN-PROVED.** The
    mixed-sign premise behind the positivity prune is machine-checked
    sorry-free: `QOU.BraidsAndKnots.deltaSign_mixed` (both ±1 occur) +
    `QOU.BraidsAndKnots.binding_magnitude_eq_dim` (|Δ_λ|² = dim²) in
    `QOU/BraidsAndKnots/S5SO3FiberAction.lean`. So the prune now rests on a
    Lean fact, not just a Python check: a non-negative (KL) weight sum can
    supply the magnitude |Δ_λ|=dim but never the mixed chirality sign. The
    McKay 2I↔E₈ + A₅-branching anchors behind the chirality pairing are
    likewise Lean-proved (PR #2424). No new closure mechanism — theory-ledger
    tightening only.
  - **(2026-06-25, this PR) MAGNITUDE LEG CLOSED — `B_λ` (KL left-cell Betti
    sum) is NOT cell-invariant, so it cannot supply `|Δ_λ|` either.** The
    2026-06-16/-17 prune closes the *sign*; this closes the *magnitude* leg it
    explicitly left open (cf. `2026-06-16-delta-lambda-sign-is-icosahedral-chirality.md`:
    "positive KL data could in principle contribute on the magnitude side").
    Direct S_6 enumeration of **all** left cells (literature-validated pure-Python
    KL, `kazhdan_lusztig._self_test` green): distinct cells of the *same* shape
    give *different* `B_λ = Σ_{w∈Γ_λ} P_{e,w}(1)` — (3,3): 6..23; (3,2,1): 22..54;
    (4,2): 9..20; **even hooks vary** ((4,1,1): 10..26). Only the three trivial
    shapes (6,),(5,1),(1^6) are invariant. ⇒ `B_λ` is not a function of λ; it has
    no canonical value without an arbitrary cell-selection rule. Resolves the
    prior on-main disagreement (`kl_betti_extrapolation.py` first-cell vs
    `probe_option_e_probe4_kl_batch.py` `canonical_Q` — each silently picks *a*
    cell; the batch-results doc's "hooks match f^λ" was a `canonical_Q` artifact,
    now corrected in that doc). Deuteron: the f^λ→B_λ swing is
    `B_pred ∈ 0.457..0.817 MeV` (×1.20..×2.15), none reaching 2.2245 (needs ×5.85).
    **(a)-scope** negative (this construction alone), **not** a structural
    exclusion of KL data from every closure. Probe:
    `kl_betti_cell_dependence_probe.py`; witness: `kl-betti-cell-dependence.witness.json`.
    Cross-checked against the canonical Rust engine: 76/76 S_6 left cells match
    `pyhecke_native.kl_betti_sum_rust` (zero mismatches; per-shape ranges agree
    exactly) — `kl_betti_rust_parity_crosscheck.py`.

## Anti-patterns (DO NOT repeat)

- ❌ Q-factorial ratio (`q⁻^A · δ_tr · A(A-1)/2`) — RETRACTED per PR #1386 as backhanded fit. The actual `Δtr(⁴He)/Δtr(D) = 0.67`, not the 12.7 the q-factorial implied.
- ❌ Single-nucleon Δ_λ derivation (audit `2026-05-26-...`): misses the multi-nucleon interface operator.
- ❌ q-dependent algebraic Δ_λ at the Cat layer (audit ibid): mixes Cat and Alg layers. The Cat-layer Δ_λ is q-independent (sign × dim).
- ❌ Seventh fit-based ansatz (AGENTS.md §L2 explicit ban). The v9
  `(1+q)/2` factor is borderline — it's clean enough to look canonical
  but was SEARCHED for, not derived. Treat as near-match.

## Active PRs

| PR | Scope | Status |
|----|-------|--------|
| #1516 | Option-E Phase 2 entry-point probe + Phase 1 doc update (pivoted to H_n generalisation) | open |
| #1697 | **Option-E Phase 1 H_n generalisation** — per-block Hoefsmit-seminormal ρ_λ(σ_k) and ρ_λ(w_0) at H_3 + H_6 (deuteron); 11 partition blocks; 4 assertions pass | open |
| #1698 | Subgoal-1 m_avg operator-valued combiner (Wenzl branching) — touches `BraidKnot/OperatorValuedCombiner.lean`; no file overlap with #1697 but shares Markov-trace path | open |
| #1707 | **Option-E PROBE 1** — derive `(1+q)/2` structurally or falsify as near-match; just opened, stub-only audit doc | open |
| (this PR) | Option-E master ledger backfill | open |

## Sessions log

| Date | Agent / branch | Intent | Results |
|------|----------------|--------|---------|
| 2026-05-31 (cont. 3) | Claude / `claude/coord-ledgers-option-e-followup-2026-05-31` | (1) backfill this ledger from v1..v9 commits + existing audits, (2) document v9 near-match status honestly with failure signature for v10 | landed (1) + (2); did NOT propose v10 to avoid 7th-ansatz trap; PROBE 1 (derive (1+q)/2 structurally) is the next-session keystone. |
| 2026-06-02 | Claude / `claude/option-e-derive-1plusq-over-2-2026-06-02` (PR #1707) | PROBE 1: DERIVE-OR-FALSIFY the v9 (1+q)/2 — refresh at canonical q₀, test 4 structural hypotheses, proton-vs-muon discriminator | **VERDICT NEAR-MATCH (fit)**. (1+q)/2 NOT forced: 4 independent hypotheses 18–90% off; only tautological [2]_q/2 / (q+1)/2 "match". Required factor R=1.05372 ≠ (1+q)/2=1.05499 by +0.12% same-pin. Published 0.11% was stale (muon literal); canonical-q₀ residual +0.12%, sign-flipped. No v10. (1+q)/2 stays un-wired; A=3 closure OPEN. |
| 2026-06-02 | Claude / `claude/option-e-phase1-gram-h6-2026-06-02` | Phase 1 H_n Gram-matrix generalisation at H_6 (deuteron) — deliver the per-block Hoefsmit-seminormal infrastructure that #1516's doc update identified as missing. Pure-Python, no pyhecke_native dep. | landed (PR #1697); 11 H_6 partition blocks with σ_k matrices + ρ_λ(w_0) at q_0; 4 assertions pass (χ_λ cross-check residual 2.22e-16 at H_6, Σ dim_λ² = n! at both n=3,6). Witness `option-e-phase1-gram-h6.witness.json` carries the data needed to test **PROBE 1** ("`(1+q)/2` = half-trace of σ_1 in standard rep") on the (5,1) standard rep of H_6 — not run in this PR (scope = infrastructure). |
| 2026-06-02 | Claude / `claude/option-e-derive-1plusq-over-2-2026-06-02` | Open **PROBE 1** — derive `(1+q)/2` structurally or falsify as near-match. Per ledger §"Open probes" line 85. | in flight (PR #1707, stub-only commit; coord posts cross-published on #1697 and #1707; canonical q_0 confirmed not stale; can consume #1697's `option-e-phase1-gram-h6.witness.json::data.h6.blocks["5_1"]` data for the half-trace hypothesis test). |
| 2026-06-02 | Claude / `claude/option-e-phase2-gram-probe-2026-05-30` (PR #1516) | **PROBE 4 (cheap pass)** — test single-vertex KL candidate rules for Δ_λ closure at H_6/deuteron, mirroring PR #1709's "cheap proxy first" strategy. Also extends Phase 2 entry-point probe H_3 → H_6 consuming #1697's just-merged Gram. | **VERDICT: ALL FOUR SINGLE-VERTEX CANDIDATES REFUTED** (miss ≥ 66%): A χ^λ(w_0) 99.83%, B \|χ^λ(w_0)\| 120.73%, C sgn·dim_λ 66.47%, D peak \|ρ_λ(w_0) diag\| 117.46%. Symmetric to #1709's geometric Vol_λ refutation. Remaining in-Option-E direction: full `n^w_λ` enumeration across multiple vertices (extend `kazhdan_lusztig.py` past n ≤ 4 cap to S_6). Otherwise: pivot to GAP-A-3/A-4. Witness: `probe-option-e-phase2-crystal-vertex-candidates.witness.json`. |

| 2026-06-16 | Claude / `claude/option-e-probe4-kl-positivity-prune-2026-06-16` | Formalize-first prune of PROBE 4 (the remaining in-Option-E path) before committing to the S_6 KL extension | **PRUNED.** Target Δ_λ=sgn·dim is mixed-sign (verified n=3,6); KL multiplicities are non-negative (KL positivity) ⇒ a Σ_w n^w_λ·X_w sum supplies at most \|Δ_λ\|=dim (already f^λ), never the chirality sign. PROBE 4 not a new closure mechanism; de-prioritise the S_6 KL extension. Frontier = PROBE 2 (A=4 interface), sibling cluster #2369/#2371/#2372. No fit. Audit `2026-06-16-option-e-probe4-kl-positivity-prune.md`. |
| 2026-06-16 | Claude / `...probe4-kl-engine-validation` (PR #2381) | Engine-verify the PROBE-4 prune on real KL data | Located the KL engine at `computations/kazhdan_lusztig.py`; KL positivity at S_4 confirmed (all 576 P_{x,w} coeffs ≥0; 6 non-trivial = q+1) → prune now engine-verified, not theorem-cited. |
| 2026-06-16 | Claude / `...delta-lambda-sign-chirality` (PR #2386) | Decompose the Δ_λ per-block factor | Δ_λ = sgn(w₀^{S_λ'})·dim = **magnitude (Wedderburn dim, chirality-invariant) × chirality sign** (= transpose = sign-twist = keystone's T₁↔T₂ parity; self-conj (3,1,1) ↔ A₅-split). Explains the PROBE-4 prune (sign exogenous). **NOTE (corrected #2388-era):** this is the Δ_λ *factor* structure, NOT a deuteron closure — see next row. |
| 2026-06-16 | Claude / `...deuteron-closure-crosscheck` (this PR) | Run the canonical deuteron compute; reconcile closure framing | **CORRECTION.** `binding_energy_categorical_deuteron.py` → B(D)=0.380 MeV, **−82.9%** off: the Δ_λ Σ-formula does NOT close the deuteron. The closure is **E₀×q⁻¹ (+0.91%)** (PR #1367), a separate object. Corrected #2386 (banner) + the §Status "Reading" prose (above) which had conflated the two. No math retracted — the chirality decomposition + PROBE-4 prune stand. Audit `2026-06-16-deuteron-closure-crosscheck-and-correction.md`. |
| 2026-06-16 | Claude / (infra) | doc-currency | Compute path `folio-assistant/computations/` → `computations/` swept (3675 files, PR #2388); the canonical compute is qou-top-level `computations/`. |
| 2026-06-17 | Claude / `...keystone-lean-delta-lambda-chirality` (PR #2416) | Lean-prove the Δ_λ magnitude×chirality split | **LANDED (sorry-free).** `S5SO3FiberAction.lean`: `deltaSign`/`deltaLambda`, `deltaSign_sq_one`, `binding_magnitude_eq_dim` (|Δ_λ|=dim), `deltaSign_mixed` (the PROBE-4 prune premise), `electron_block`. Verified core-only (lean v4.24.0, exit 0); Mathlib build CI-deferred. The PROBE-4 KL-positivity prune now rests on a machine-checked mixed-sign fact. No fit, no compute rewire. |
| 2026-06-24 | Claude / `claude/brave-hawking-tjdu2p` | Owner Q: "KL not sufficient ≠ wrong — can it be *contributive* to the magnitude?" Measure on the deuteron oracle (S₆, exact). | **CONTRIBUTIVE, NOT CLOSING (×2.0).** With the canonical y_λ·χ^λ·sgn primitives, swapping f^λ→ KL left-cell Betti B_λ gives Σ: −0.7439 (f^λ, reproduces canonical) → −1.4894 (Betti); B(D): 0.380 (−82.9%) → **0.761 MeV (−65.8%)**. Needs ×5.85 to close, KL-Betti delivers ×2.0 (lift all from bulk; dominant (5,1) is a hook, unchanged). **Refines** the prune's incidental "KL at most re-derives \|Δ_λ\|=dim": Betti ≠ dim on bulk and *does* move the number — PROBE-4 is **(a) scope-limited**, not (b) excluded. The *sign* prune (deltaSign_mixed) still stands; **not** a production rewire (non-closing ansatz swap). Witness `option-e-kl-betti-contributive-deuteron`; audit `2026-06-24-kl-betti-deuteron-contributive-measurement.md`. |
| 2026-06-28 | Claude / `claude/option-e-a4-reconcile-2026-06-28` | Reconcile #2839's A=4 "closure" empirically + record durably (anti-rechase). | **A=4 Option-E closure UNSUBSTANTIATED.** Only runnable A=4 script `a4_option_e_color_tube_closure.py` = **−79.1%** (5.91 MeV via the ×10³ color-tube numerology, not Betti). No full Σ_λ exists: `chi-helium-4-h12` is **17/77** (`partial`; Rust-gated producer — bean **b0vf**, no non-Rust route: `pyhecke_native` absent + pure-Python matrix-M "infeasible for n=12") and only `B_{(10,2)}` of 77 `B_λ` computed (#2839 Rust). So "B_{(10,2)}=584 closes A=4" is a **single-partition scalar, not a full sum**. Both computable fronts (A=2 ×2.0; A=4 −79%) = contributive/insufficient, **not closing**. Don't re-chase until b0vf (χ complete) + 77 `B_λ` land, then run the deuteron harness. Audit `…2026-06-24…` §A=4. (t6ba verified resolved on main.) |
| 2026-06-28 | Claude / `claude/option-e-a4-computed-2026-06-28` | Built `pyhecke_native` (owner direction) → compute the REAL A=4 binding; correct the prior "χ 17/77 / can't compute". | **A=4 f^λ COMPUTED — does NOT close.** Full 77-partition signed sum (the complete χ was already on main in the `…-matrix-m` witness; the 17/77 was a stale sibling file = b0vf): Σ_f=−10.867 → **B(⁴He)_f = 5.55 MeV (−80.4%)**, needs ×5.10. Full **Betti** sum infeasible even with pyhecke (`kl_betti_sum_rust`: (10,2)~100s; column shapes = w₀ over all S₁₂) — which is why #2839 has only B_(10,2). Verdict: A=4 not closing (deuteron Betti uplift is only ×2.0 → ~11 MeV ceiling). **#2839's "584 closes A=4" refuted.** Script `option_e_a4_full_reconciliation.py` + witness `option-e-a4-full-reconciliation`; audit §A=4 Update. |
| 2026-06-17 | Claude / `...keystone-lean-mckay-e8-anchors` (PR #2424) | Lean-prove the McKay 2I↔E₈ + A₅-branching anchors | **LANDED (sorry-free).** `binaryIcosahedralIrrepDims` (affine E₈ marks) with Σdim²=120, Σmarks=h(E₈)=30, \|2I\|=4·h, dimE₈=248=8·31; `so3_to_a5_dim_splits`; `s5_to_a5_electron_block_splits` (6=3+3, T₁⊕T₂). Pins the spacetime-face arithmetic behind the chirality split. Verified core-only (exit 0). |
| 2026-06-17 | Claude / `...deuteron-closure-overclaim-fix` | Re-verify the deuteron "closure" claim (row 2026-06-16 above asserted "+0.91% via E₀×q⁻¹ is the correct closure") | **CORRECTION — the deuteron is NOT closed.** No compute reproduces 2.24/+0.91%: stated E₀×q⁻¹ (E₀=4.186)=3.771 (+69.5%); Σ-formula=0.380 (−82.9%); the apparent closure was Σ×**fitted** C_knot=5.852 (the compute itself labels it fitted, gate open). Best parameter-free = interface-knot+T3 = 1.526 (−31%). The 2026-06-16 "Reading" + Status row were themselves wrong (kept E₀×q⁻¹ as "correct closure"); both fixed. No light nucleus honestly closed (Δ_λ blocked, main `1f08f61a`). Audit `2026-06-17-deuteron-closure-overclaim-corrected.md`. |
| 2026-06-28 | Claude / `claude/delta-lambda-l1-ceiling-prune-2026-06-28` | Formalize-first attempt at the Δ_λ closure: characterize the residual structure of the proven `sgn·dim` form rather than fit a 7th ansatz | **NEW PRUNE — sign-only fixes structurally excluded (b, invariant cited).** For the Σ-formula with proven Δ_λ=sgn(w₀^{S_λ'})·dim, the triangle inequality bounds **any** sign/chirality reassignment by ‖c‖₁=Σ\|y_λ χ^λ dim_λ\|. Measured ‖c‖₁/\|target\| = {D 0.52, T 0.36, ³He 0.59, ⁴He 0.41} — **< 1 for all four** ⟹ no sign-only re-derivation closes the deficit; a *magnitude-adding* ingredient is necessary (re-derived \|Δ_λ\|, re-weighted y_λ, or a new term T2–T6 / A=4). **Magnitude-side mirror of the PROBE-4 KL prune** (PROBE-4: signs can't supply magnitude-of-dim → never the sign; this: the sign structure → never the magnitude). Does NOT exclude magnitude-side levers z2bn/w5tg/thb7/PROBE-2 (all add ℓ¹ mass). thb7 note: ceiling ratios non-constant (0.36–0.59) ⇒ universal scalar on the summed vector can't hit all four (consistent with C_knot 2.8× spread) — informative, not a refutation. Witness `delta-lambda-l1-ceiling-sign-prune.witness.json`; audit `2026-06-28-delta-lambda-l1-ceiling-sign-only-prune.md`. No fit, no compute rewire. |
| 2026-06-28 (cont.) | Claude / `claude/delta-lambda-l1-ceiling-prune-2026-06-28` | Machine-check the prune core + profile the deficit + probe route (i) | **(1) Lean** `DeltaLambdaL1Ceiling.lean` sorry-free (`abs_weighted_sum_le_l1` / `weighted_sum_below_target` / `chirality_sum_below_target`; generic `[Field R][LinearOrder R][IsStrictOrderedRing R]`; lean-direct exit 0; wired to QOU.lean). **(2) Deficit profile** `delta-lambda-magnitude-deficit-profile.witness.json`: irreducible shortfall `|target|−‖c‖₁` = 40–64% of target; ℓ¹ mass concentrates in few-row near-rectangular blocks ([5,1]/[4,2]/[3,3] for D). **(3) Route-(i) q-dim probe** (scope (a)) `delta-lambda-qdim-route-probe.witness.json`: tested 3 q-dim conventions — ceiling `‖c_q‖₁/|target|` is **wildly convention-dependent** (⁴He spans **0.41→5.62**: balanced 0.80, unbalanced 2.54, fake-degree 5.62). ⟹ route (i) **escapes the sign-only prune** and is **under-constrained** — the q-dim convention is a **hidden DOF** (Rule 14); magnitude-matching via q-dim is NOT a derivation. Real discriminators: an independent principle fixing the convention + the sign/cancellation structure (net −82.9% vs fake-degree ℓ¹ +462% on ⁴He ⟹ near-total cancellation required). Caution for z2bn/thb7/PROBE-2. No fit. |
| 2026-06-28 (cont.2) | Claude / `claude/delta-lambda-l1-ceiling-prune-2026-06-28` | Cancellation / A-scaling probe — the SIGNED net (closure ⇒ +1) under classic + 3 q-dim conventions | **No flat q-dim convention reproduces binding's A-scaling.** `delta-lambda-cancellation-ascaling-probe.witness.json`: as the convention grows the net grows **non-uniformly in A** — heavy isotopes overshoot (³He 1.27, ⁴He 1.31 at fake-degree) while light undershoot (D 0.28, T 0.91); no single convention lands all four near +1 (isotope spread 2.2–4.7×, *widens* with the convention). ⟹ the closure object must be **A-/λ-structured** (route (ii)/(iii) or a structured kernel whose effective dim_q bends the A-scaling — directly the z2bn S(m)=Σ_λ dim_q q-Gaussian/Habiro EGF, #2899). Sharpens the hidden-DOF finding: it's not just ℓ¹ freedom — the signed family fails the A-scaling test for every flat convention. Scope (a). No fit. |

## Cross-refs

- `docs/audits/2026-05-26-delta-lambda-binding-formula-closure.md` — deuteron closure (PR #1305 + #1367)
- `docs/audits/2026-05-18-delta-lambda-gating-context.md` — the §L2 Δ_λ-gate context (Track A blocker)
- `docs/audits/2026-05-25-option-e-crystal-weight-delta-lambda.md` — original Option-E motivation (Kashiwara crystal)
- `docs/audits/2026-05-19-delta-lambda-phase4-z4N-closure.md` — early Z⊕N closure attempts
- `docs/audits/2026-05-19-delta-lambda-thread-closure.md` — six-ansatz failure record
- `computations/option-e-v9-all-symmetries.witness.json` — v9 witness
- `computations/option_e_v9_all_symmetries.py` — v9 source
- AGENTS.md §Precision goals (L2 Δ_λ gate; Track A blocker; Subgoal-1 closure path)
- `docs/coordination/1ppq-qbeta.md` — parallel flip-flop saga (c_k near-matches)

## 2026-06-28 — z2bn fibre-kernel structure ↔ #2925 ℓ¹-ceiling (coordination)

PR #2925 (Δ_λ ℓ¹-ceiling) proves sign-only Δ_λ re-derivation is capped at
`‖c‖₁/|target| = 36–59 %` for D/T/³He/⁴He (scope (b), triangle inequality), so a
**magnitude-adding** ingredient is necessary — and lists **z2bn (fibre R(q,x))**
as an active magnitude-side lever that escapes the ceiling. PR #2899 (z2bn) pins
the structure of that magnitude object: the binding period `S(m)=Σ_λ dim_q(λ)`
has an exact q-Gaussian generating function
`Ŝ(z)=Σ S(m)z^m/[m]_q! = exp(z + L₂(q)z² + Σ_{m≥3} L_m z^m)`, with a `(q−1)²·Φ_d`
cyclotomic (Habiro) correction tower (sorry-free Lean
`QOU.Mass.BindingQGaussianHabiro`), not q-holonomic of order ≤3 (held-out
falsified). **Honest scope (a):** right *kind* of object (magnitude-side
generating function, exact data), structure pinned; does **not** yet show it
adds the 41–64 % ℓ¹ mass to close the deficit — closure is downstream. The
ℓ¹-ceiling sets the bar the kernel's mass contribution must clear.
Audit: `docs/audits/2026-06-27-lever1-qinvolution-cyclotomic-kernel.md`.

## 2026-07-05 — PROBE-2 (A=4 interface operator) class-D gate landed + s5-so3 coordination

The A=4 interface-operator lever (PROBE 2 / GAP-A-4 class D) got its
**formalize-first gate + a confirmed locality prediction** (PRs #3375 scoping,
#3385 gate+probe; the I-1/I-6/I-2 gate trio landed earlier via #3351/#3366):

- **Scoping map** `docs/scope/2026-07-05-gap-a4-interface-operator-attack-scoping.md`
  synthesizes the ~40-probe graveyard (T2–T18 + interface/a_operator). The ×5.10
  ⁴He gap is pinned as a **missing higher-order term** — not a weight (bond
  factors Lean-exact, `deltaSign_mixed`) and not sign-fixable (the ℓ¹-ceiling
  0.41 < 1, row 2026-06-28 above). It is **≥4-body and ⁴He-LOCAL**.
- **Gate (sorry-free)** `QOU/MassTheory/SU4SupermultipletGate.lean`: the Wigner
  SU(4) [1^A] supermultiplet has dim `C(4,A)`, **zero iff A>4** — the α (A=4) is
  the top closed shell. The degree/orbit-count vanishing that *predicts* the
  ⁴He-locality.
- **Narrow probe (scope-(a))** `su4-supermultiplet-locality.witness.json`: the
  **measured super-pairwise excess peaks at ⁴He (2.093×) and returns to ~pairwise
  by ⁶Li (0.944×) where `C(4,6)=0`** — a clean LOCALITY MATCH. Not ∝ `C(4,A)`
  (that peaks at A=2); peaks at the unique maximally-bound α singlet. **Magnitude
  leg (2.093× ↔ the [1^4] connected-operator value) is the multi-session
  follow-on** — this is locality-consistency, not a magnitude closure.

**Coordination:** posted intent on #2503 (the class-C geometric `W_λ` route) —
the two ⁴He-magnitude attacks (class-C geometric vs class-D interface operator)
now share a proved A=4-local / A>4-vanishing signature any candidate index can be
cross-checked against, alongside the existing defect-cubic / `f_pn`-bracket gates.
Earlier same-day: I-6 trace-convention unblock posted on #3205 (per-knot axis).

## 2026-07-06 — [1⁴] value-leg writhe derivation + Wigner phys-lit (coordination)

The ⁴He magnitude value leg narrowed to a single object across ~10 PRs
(#3395 I-par … #3420 Perron–Frobenius … #3422 antisym-Hecke): `b₄` = the
connected 4-body cumulant (9.243 MeV, exact) of a nucleon-flavor `Λ⁴(4)`
operator (gate-verified), Lean-proved orthogonal to existing forms, functional
form `−ln det(I+G)` (sign-unique), `G` a **sign-carrying (bar-odd) exchange**
(Perron–Frobenius excludes the positive binding factors). PR #3423 adds the
**lit anchor** (the α binding IS the Wigner SU(4) supermultiplet closed-shell
energy — nuclear physics *fits* it; `b₄` derives it), a phys-lit **remark**
(`rem:alpha-wigner-supermultiplet-context` on `conj:wigner-su4-from-spin-isospin`),
and the **§4a structural finding** (the committed atom word is a linear CHAIN,
not the [1⁴] complete graph — why `B_sym` under-binds ⁴He). The one open object
is the **per-pair writhe sign** `sgn(w_{ij})` of the six [1⁴] block crossings,
read from the [1⁴] link-diagram framing (never fitted).

**Coordination posted:**
- **#3417** (Elliott SU(3) + q-deformed nuclear) — overlaps on
  `wigner-su4-from-spin-isospin`; flagged the new phys-lit remark so bean 1ict
  builds on it rather than duplicating (Wigner SU(4) ⊃ Elliott SU(3), complementary).
- **#3407** (Reeb-flow `Lk_R^{(k)}` categorical linking operation) — possible
  **dependency**: their bar-odd-A₋ linking operation may supply the `w_{ij}`
  linking numbers my writhe leg reads as open. Both independently land in the
  bar-odd sector. Watching #3407; will consume `Lk_R^{(k)}` if it closes.

### 2026-07-06 (later) — [1⁴] writhe signs read off; the open sharpens to sign **+** magnitude (#3426)

Built the [1⁴] complete-graph exchange matrix explicitly
([`b4_1four_complete_graph_writhe_signs.py`](../../computations/probes/b4_1four_complete_graph_writhe_signs.py),
PR #3426). **Two of the three pair-signs are DERIVED** off the framework's own
crossing convention (`atom_braid_word_3A`): **pp → σ = +1**, **nn → σ⁻¹ = −1**
(nn = bar-mirror of pp — the p↔n bar-odd asymmetry). Only the **pn** sign is
open. Enumerating `w_pn ∈ {−1,0,+1}` at the derived bond-factor magnitude
`z ≈ 0.499`: pn=±1 give det<0 (unphysical), pn=0 gives 2.40 MeV (0.26×) **and**
block-diagonally decouples the pn-dominated shell (excluded). **Decisive bound
(not a fit):** the read-off sign pattern's most-negative eigenvalue is exactly
**−√5**, capping the physical per-pair magnitude at `g < 1/√5 ≈ 0.447`; the naive
`z ≈ 0.499` exceeds it by ~12% (why the mixed-sign det went negative). Since
`−ln det → +∞` at the ceiling, the value **form** `b₄ = −ln det(I+G)` is **not
refuted (scope-(a))** — the failure is the *naive uniform magnitude z*, not the
form. **Open object sharpened:** the [1⁴] framing must supply the pn sign **and**
a sub-`1/√5` per-pair magnitude. Posted the exact spec on **#3407**
([comment](https://github.com/litlfred/qou/pull/3407#issuecomment-4892386760)):
their `Lk_R^{(k)}` must land the pn linking amplitude below `1/√5`, mixed-sign,
in the bar-odd A₋ sector — supplying both open inputs at once.

### 2026-07-11 — binding w_n = the Δ_λ/W_λ gate; kernel basis = q-Hermite (#3534)

The jet-filtration residue-weight kernel derive-or-refute (#3534, bean t7qv)
lands the **binding-side** view of the same Δ_λ/W_λ gate the sign capstone
(`164153f40d`, merged) and the magnitude reduction (#3537) work from the
partition side. Three-part result:

1. **Ad-hoc constant-ratio kernels REFUTED (scope-(a)).** Coulomb-corrected AME
   → universal `w_2,w_3,w_4 = 4.353, 9.331, 15.919` (ratios 2.143, 1.706); no
   parameter-free geometric/[n]_q/a_D-self/linear kernel closes to 5% (`[n]_q²`
   lone 6.9% near-miss, echoing the √C_λ near-miss of merged #3518).
2. **Kernel basis DERIVED = q-Hermite / Rogers–Szegő.** The na-Stokes kernel
   `a_D^(n)=S(n)/n`, `S(n)=Σ_{λ⊢n} dim_q V_λ` (q-involution number), obeys a
   three-term recurrence `S(n)=S(n−1)+c_n·S(n−2)` with **`c_3=[2]_q` exact** and
   `c_n/[n−1]_q` rising — the q-oscillator / q-hyperbolic orthogonal basis
   (`QOU.Mass.RogersSzegoInhabited`). Owner steer 2026-07-11.
3. **w_n is NOT q-Hermite-clean → the gated W_λ content.** w_n neither obeys the
   `a_D` recurrence (42% off) nor matches any Rogers–Szegő ratio-shape (closest
   13.2%); it **decelerates** (2.14→1.71, sub-geometric) vs the near-geometric
   q-Hermite. So the q-dim structure lives in the **kernel**, the magnitude in
   the **multiplier** — the exact split #3537 finds ("magnitude = classical q=1
   `dim(λ)`, not substrate q-dim"). Complementary, no §6 escalation.

**New falsifiable constraint on the gated W_λ:** the trace `tr(g_ρ)` (or any
W_λ realisation) must, summed per body-order, reproduce w_n's **sub-geometric
deceleration** (2.14→1.71). Posted as the one ask on
[#3537](https://github.com/litlfred/qou/pull/3537#issuecomment-4945856508).
Un-refuted forward route stays option #1 (hyperbolic link-volume `w_n`).
Cherry-pick pointer: [`binding_wn_kernel_derive_refute.py`](../../computations/binding_wn_kernel_derive_refute.py) §5–6.

## 2026-07-18 — Δ_λ two-front session (magnitude structure + sign-morphism) (coordination)

Two clean, disciplined results this session (gate open for all; no fit; nothing
wired; honest negatives where they fell).

**Front (ii) — many-body magnitude structure DERIVED (#3924, merged).** The
missing ≥4-body `[1⁴]` term's structure is now parameter-free:
- **⁴He-locality is structural:** the SU(4) `[1⁴]` antisymmetrizer trace
  `(1/A!)Σ_{σ∈S_A} sgn(σ)·4^{c(σ)} = C(4,A)`, rank `{1,4,6,4,1,0,0,0}` ⇒
  `b₄(A>4)=0`, and **A=4 is the unique rank-1 `[1⁴]` singlet** (Wigner closed
  shell) — a structural reason the residual peaks at doubly-magic ⁴He.
- **Exchange sign + ceiling fixed:** the `[1⁴]` complete-graph exchange matrix
  spectrum is exactly `{±√5,±1}` ⇒ `det(I+G)=(1−5m²)(1−m²)`; the attractive
  `−ln det` branch is realised and physicality `det>0 ⇔ m<1/√5` **reproduces the
  derived writhe cap** parameter-free.
- **Residual = one gated scalar:** the per-pair bond magnitude (`E_unit`) — this
  *is* the standing Δ_λ gate (six ansätze failed; 7th fit forbidden). The `−ln det`
  form's locality/sign/ceiling are derived; its magnitude remains the gate,
  unwired. Coordinated on the binding-frontier #3808 (R11 additive-split owner).
  Probe `b4_slater_antisymmetrizer_exchange_sign.py` (7/7).

**Front (i) — sign-morphism Angle A REFUTED (#3931, open).** Tested whether the
sign carrier `g_ρ` (the principal **row** grading `q^{2ρ}`, `n(λ)=Σ row`) is the
**Nakayama automorphism** of a natural graded Frobenius algebra — a route to
replace the cited fake-degree theorem with a self-contained categorical morphism.
**Verdict: NO** (12/12, proved): coinvariant `R_n` commutative⇒symmetric⇒`ν=id`
(+1, INV-1); `V_λ`-carriers (ℂS_n, generic `H_n(q)`) semisimple⇒`ν=id` (+1,
INV-2); non-symmetric candidates (0-Hecke, nilCoxeter, `gr H_n(q)`) index the
wrong simples; the one pivotal "Nakayama-like" twist `θ_λ=q^{2(n(λ′)−n(λ))}` is
the **content** grading (+1 at ζ₄, already pruned #3529). Saves the
`nakayama_eq_principalGrading` Lean effort (false) — problem (i) stays open, the
correct home remains the GS/jet-order fake-degree valuation (#3537-line). Probe
`deltalambda_grho_nakayama_probe.py` (12/12); hand-audited Lean
`NakayamaGradingObstruction.lean` (NOT machine-verified — sandbox 403).

**Net Δ_λ state:** sign fully derived (`g_ρ` jet-order valuation; Nakayama route
now excluded as an alternative construction); single-trace magnitude = `dim(λ)`;
the whole remaining wall is the **≥4-body per-pair bond magnitude scalar** — its
locality/sign/ceiling derived, its value the standing gate. No §6 escalation.

**2026-07-26 — the #4316 frustration weight κ is WALLED at the deuteron; the
residual is derived to be pure ≥3-body (μ₂=0).** (PR #4320,
`claude/deltalambda-interface-operator-kappa-2026-07-26`.) The #4316 additive
term `M(A)=s·(edges − κ·triangles)`, s>0, is **refuted at A=2**: the graded ladder
`ρ_grad(A)=[A]_q!/[2]_q!` gives `ρ_grad(2)=1` and the deuteron self-reference gives
`ρ_strong(2)=1`, so `M(2)=0` (DERIVED, AME-independent) — but the model predicts
`M(2)=s>0`. So κ=t/s is ill-posed (edge coefficient forced to 0); the fitted
κ=2.385 was an A=3,4-only artefact. The exact 0-parameter simplex (Mayer)
decomposition over the derived C(A,k) basis (points A=2,3,4): **μ₂(edge)=0,
μ₃(triangle)=+0.4708, μ₄(tetra)=−4.591** — a pure ≥3-body residual, tetrahedron-
dominant-negative, matching the derived ρ_F full-binding **b₄/b₂=4.16** ([1⁴]
supermultiplet). This **re-confirms this ledger's "≥4-body per-pair bond magnitude
scalar" as the standing gate**: the derivation target is μ₄, reachable via the ρ_F
cluster integrals (`pyhecke_native` present) but requiring the residual
(graded-subtracted) cluster-integral compute — infra-scoped, not a κ fit. Lean
`AdditiveResidualSimplex.lean` sorry-free (deuteron refutation + μ₂=0 + exact
0-param solve). Audit `2026-07-26-deltalambda-interface-operator-kappa.md`. No fit,
nothing wired.

**2026-07-26 — the μ₄ redirect (ρ_F cluster integrals) WALLS on the 3-body sign;
4-body sign-consistent but not derived.** (PR #4354,
`claude/deltalambda-mu4-rhoF-cluster-2026-07-26`.) Followed the #4320 redirect:
compute the DERIVED (0-fit, q₀-only) ρ_F cluster integrals and test against
μ₃=+0.4708, μ₄=−4.591. **Infra NOT gated** (`pyhecke_native` 0.9.0 functional; the
connected 3-body cluster is cached 0-fit at `three-body-joint-trace-a3.witness.json`).
Key decomposition: **μ_k = s_k − g_k** with `g_k` the DERIVED graded simplex coeffs
(g₂=1, g₃=0.342, **g₄=+8.371**) and `s_k` the AME target — so **μ₄<0 is dominated by
the derived g₄ subtraction, NOT an ρ_F cluster**. Derived ρ_F 3-body cluster
**c₃<0** (⟨T,³He⟩=−1.59 MeV, H₉ joint trace); derived 4-body beyond-pairwise **c₄<0**.
**Sign gate (normalization-free):** μ₃>0 ≠ c₃<0 → **WALL**; μ₄<0 sign-consistent with
c₄<0. A single N>0 cannot map same-sign (c₃,c₄) to opposite-sign (μ₃,μ₄); no
0–1-param derivation lands both. **Lean-proved scope-(b):** `productModel_3body_nonpos`
+ `markovParam_le_half` (z≤½<1 ∀q>0) ⇒ NO pairwise interface product gives a positive
3-body cluster. So the multiplicative ρ_F cluster route **cannot** supply μ₃ — the
standing open door is a **non-multiplicative / enhancing (f>1) cluster operator** (the
3-body cluster *sign*, not its ~1.5 MeV scale, is the open question). Lean
`Mu4RhoFCluster.lean` (hand-audited; lean-direct blocked by pruned lake-cache +
disk ENOSPC). Audit `2026-07-26-deltalambda-mu4-rhoF-cluster.md`. No fit, nothing
wired.

**2026-07-26 — the Borromean irreducible operator supplies the forbidden μ₃ `+`
sign: a derived positive-sign LEAD (scope-(a)), NOT a closure.** (PR #4360,
`claude/deltalambda-borromean-3body-cluster-2026-07-26`.) Followed #4354's open
door — a **non-multiplicative, enhancing** 3-body operator. The distinct QOU
candidate: the **Borromean/Brunnian** irreducible operator — three components,
every 2-sub-link *trivial*, yet genuinely 3-body linked, so the pairwise
(multiplicative) part vanishes *by construction* and the whole content is the
irreducible 3-body cluster (it is *the* `Vol(𝓑₃)·ρ` object, GAP-A-4 closed form,
**0 free params**). The connected 3-body cluster against the unlink `τ_free=τ(0)=1`
is `c₃^Borr = E₀·(1−τ_Borr)` with the **closed form** `1−τ_Borr = h⁴(3+h²)/(h²+4)
≥ 0` ∀ real h (strict for q≠1). **Sign gate (normalization-free):** `c₃^Borr>0`
**matches** `μ₃=+0.4708>0` — the sign the pairwise multiplicative route provably
CANNOT give (#4354). This positivity is **unconstrained by `markovParam z≤½`** (that
bounds *multiplicative* products; the Borromean object is irreducible). **Lean
`BorromeanThreeBodyCluster.lean` machine-checked sorry-free** (lean-direct exit 0,
restored cache): `one_sub_tauBorromean`, `tauBorromean_le_one`/`_lt_one`,
`borromean_cluster_nonneg`/`_pos`, `mu3_sign_compatible_with_borromean_cluster` —
the **forward complement** of `Mu4RhoFCluster.pairwise_3body_content_nonpos` (≤0);
the `μ₃>0` sign **selects** the Brunnian operator. **NOT a closure:** bare-`H₃`
magnitude ~0.006 MeV is ~78× below +0.4708 (~264× below the ρ_F ~1.5 MeV scale);
any level-lift tuned to the target = a **FIT** (not made, not wired). Δ_λ remains
open (per-λ, 2 anchors, sign≠magnitude); magnitude is the next derive-or-refute
(a *derived* H₉/g-channel lift or s5-so3 `W_λ`, never a fit). Probe
`borromean_3body_cluster_sign_probe.py` + witness. Audit
`2026-07-26-deltalambda-borromean-3body-cluster.md`. `μ₃`'s value enters no proof.

**2026-07-26 — the Borromean MAGNITUDE lifts ~49× at the H₉ joint-trace level to
0.63× μ₃: a scope-(a) NEAR-MISS LEAD (0-fit), NOT a closure and NOT a fit.** (PR
#4364, `claude/deltalambda-borromean-magnitude-lift-2026-07-26`.) Closed the one
honest gap #4360 left — the Borromean 3-body **magnitude**. #4360 derived the
**sign** but at bare `H₃` (c₃≈+0.006 MeV, ~78× short). This session lifts the
Borromean cluster to the **same H₉ perblock level ρ_F used** (`g=Σ_{λ⊢9}
y_λ|χ_λ(word)|·E₀`, same E₀ + normalization as `three_body_joint_trace_a3`), with
the **faithful cabled linking** `(Δ_A·Δ_B⁻¹)³` (each nucleon a width-3 cable, 54
crossings). **Level FIXED (H₉, 3 cables) ⇒ 0 free params.** Result: **derived H₉
⟨T,³He⟩ c₃ = +0.297 MeV = 0.63× μ₃** (~1.6× short), same **+ sign**, a **~49× lift**
over bare-`H₃` — right order of magnitude, 0 fit. **Key honesty check: MEASURED
leading `h`-exponent = 4.098 ⇒ `O(h⁴)` CONFIRMED** — cabling PRESERVES the Brunnian
order-suppression; the ~49× lift is a **derived coefficient enhancement** (3
width-3 cables ⇒ ~49× more `h⁴` strand-pairs), NOT an order change or fit (channels:
`(Δ_A)³=−0.125`, `(Δ_B⁻¹)³=+0.973` non-Brunnian, but `(Δ_A·Δ_B⁻¹)³=+0.049` is the
small `O(h⁴)` value — pairwise cancellation confirmed). **Lean
`BorromeanMagnitudeLift.lean` sorry-free (lean-direct exit 0):**
`lift_is_coefficient_ratio` (level lift = κ₁/κ₂, the h⁴ cancels ⇒ never an order
change), `not_closed_at_H9` (0.297≠0.4708), `borromean_H9_near_miss`. **VERDICT:
scope-(a) NEAR-MISS LEAD** — sign derived (#4360) + magnitude order recovered 0-fit
(0.63× μ₃); the exact coefficient identity `E₀·κ·h⁴=μ₃` is **OPEN**. NOT a closure,
NOT a fit (μ₃ never inverted, no width/multiplicity tuned), NOT a hard wall. Residual
1.6× is a **coefficient** question (cable width / tower / s5-so3 `W_λ`), never a fit.
Probe `borromean_h9_magnitude_lift_probe.py` + witness. Audit
`2026-07-26-deltalambda-borromean-magnitude-lift.md`. Nothing wired; μ₃'s value
enters no proof.

**2026-07-26 — the Δ_λ residual is a TWO-operator (binding − saturation) object:
capstone formalization of the three cluster-sign walls (0-fit, sign-only).** (PR
#4379, `claude/deltalambda-two-operator-split-2026-07-26`.) Reads #4360 (Brunnian
deficit ≥0), #4354 (multiplicative cluster ≤0) and #4376 (A=4 residual μ₄<0,
`sign_swap_a3_a4`) together as a **decomposition**: the residual moment sequence
`{μₖ}` (`μ₂=0`, `μ₃=+0.4708`, `μ₄=−4.591`) is realized as a signed sum
`μₖ = Bₖ − Sₖ` of a non-negative **binding** operator `B` (Brunnian/Borromean
trace deficit) and a non-negative **saturation** magnitude `S` (= minus the ≤0
multiplicative cluster). The **sign of `μₖ` selects the dominant operator**:
`μ₃>0 ⟺ B₃>S₃` (binding-dominated), `μ₄<0 ⟺ S₄>B₄` (saturation-dominated); and —
the structural payoff — **two operators of opposite sign are necessary**: a
binding-only model (`S=0`) is ≥0 everywhere so can never equal `μ₄<0`, a
saturation-only model (`B=0`) is ≤0 everywhere so can never equal `μ₃>0`. **Lean
`TwoOperatorResidualSplit.lean` sorry-free (lean-direct exit 0):** `residual_pos_iff`
/ `residual_neg_iff` (sign ⟺ domination), `pure_binding_nonneg` /
`pure_saturation_nonpos`, `binding_alone_ne_mu4` / `saturation_alone_ne_mu3`
(two-operator necessity), `borromeanMinusSaturation` (concrete split, both signs
reused from `borromean_cluster_nonneg` + `pairwise_3body_content_nonpos`),
`residual_is_two_operator` (packaged capstone). **Genuinely REUSES the merged sign
lemmas — does not reprove them.** **Scope: SIGN structure fully derived; the
per-λ MAGNITUDE closure (that the concrete operator magnitudes sum to the exact
`μₖ`) is the OPEN Δ_λ gate and is NOT claimed** — `μ = B − S` enters the domination
theorems as a modeling hypothesis, `signed_split_exists` records only the trivial
weak form. 0 free params, no `μₖ` inverted, nothing wired. Audit
`2026-07-26-deltalambda-two-operator-split.md`.

**2026-07-26 — the A=4 Route-3 sign wall's antecedent is REFUTED: the genuine
4-component Brunnian deficit is NEGATIVE (τ_L₄ > 1), sign-COMPATIBLE with μ₄<0.** (PR
#4378, `claude/deltalambda-a4-h12-brunnian-measure-2026-07-26`.) Measured the open
companion input of the #4376 scope-(b) **conditional** wall
`mu4_ne_brunnian4Cluster` (conditional on `τ_L₄ ≤ 1`). Built a **genuine** Brunnian
4-braid — the iterated left-normed commutator of pure-braid band generators
`w₄=[[A₀₁,A₁₂],A₂₃]` — and verified Brunnian-ness **exactly** via the strand-forgetting
map `d_k` (deleting any strand → identity braid; all 4 proper sub-links machine-zero).
Unlike the earlier block-chain probe (never verified Brunnian), this is a true
Brunnian object. **Measured:** `τ_L₄ = 1.000146 > 1` (base n=4), `1.0139 > 1` (H₁₂
width-3 cable, 77 λ, 126.5 s/trace); deficit **NEGATIVE** both levels, leading Milnor
order **O(h⁶)=2·(4−1)** confirmed (n≈6.06). Robust across 3 Brunnian representatives
and the `|χ|`-vs-signed convention; cabling preserves + amplifies the sign. **So the
antecedent `τ_L₄ ≤ 1` is FALSE**: `c₄ = E₀·(1−τ_L₄) < 0` has the **same sign** as
`μ₄=−4.591<0` — the sign OBSTRUCTION is removed and the A=4 recipe **reopens on sign**.
A **Milnor-parity sign flip** vs A=3 (Borromean length-3 → +, O(h⁴); Brunnian length-4
→ −, O(h⁶)). **scope-(a)** measured negative on the antecedent — NOT a structural
exclusion, NOT a μ₄ derivation (magnitude test now live: base |c₄|≈6e-4, H₁₂ ≈6e-2
MeV, both ≪ 4.591 — NOT fitted). **Lean `HeliumBrunnianDeficitMeasured.lean` sorry-free
(lean-direct exit 0):** `measured_antecedent_fails`, `brunnian4Cluster_neg_of_tau_gt_one`,
`mu4_sign_compatible_measured_brunnian`, `brunnian_deficit_sign_flip_a3_a4` — records
the measured value WITHOUT assuming the antecedent or touching the merged conditional
wall. Probe `a4_h12_brunnian_deficit_measure_probe.py` + witness. Audit
`2026-07-26-deltalambda-a4-h12-brunnian-measure.md`. Nothing wired; μ₄'s value enters
no proof. `free_parameters = 0`.

**2026-07-27 — the A=3 (+) and A=4 (−) results consolidated into an A-indexed
Milnor-parity sign law, with the proved-vs-measured split made VISIBLE in the Lean
types.** (PR #4389, `claude/deltalambda-milnor-parity-sign-law-2026-07-27`.) Formalizes
the observed pattern `sign(1−τ_A) = (−1)^(A−1)` (A=3→+, A=4→−) and leading Milnor
order `2(A−1)` across the two known orders, WITHOUT overclaiming a general proof.
**Lean `MilnorParitySignLaw.lean` sorry-free (lean-direct exit 0, v4.24.0):**
`borromean_deficit_order` (A=3 order law `h^(2(3−1))·r(h)`, `r(0)=3/4≠0`, PROVED from
#4360 closed form) + `tauBorromean_lt_one` (A=3 sign `+`, PROVED); `tauL4Measured`,
`tauL4MeasuredOrder := 6.06` recorded as **measured `def`s** cited to the #4378
witness (NOT theorems); `paritySign_of_odd`/`paritySign_of_even` (the `(−1)^(A−1)`
convention); **`sign_law_of_crossing`** (the star CONDITIONAL theorem — IF the parity
crossing pattern `τ_A<1` odd / `τ_A>1` even holds THEN sign `= (−1)^(A−1)`, crossing
as explicit §3b-cond hypothesis); `sign_law_A3` (hypothesis discharged by PROVED
`τ_Borr<1`), `sign_law_A4_measured` (discharged by MEASURED `τ_L₄>1`, cited);
`MilnorParitySignConjecture` (content-bearing primary conjecture class, **NO
instance** = honest open state for the general law) + `sign_law_general` (§3b-cond
conditional result modulo it). **Honesty:** the general sign law is NOT asserted
proved — the A=4 sign is a measurement, so it enters only via the discharged
hypothesis of the conditional theorem; the all-A law is an instance-less conjecture.
No `μₖ` in any statement or proof; SIGN only, no Δ_λ magnitude closure; nothing wired.
Audit `2026-07-27-deltalambda-milnor-parity-sign-law.md`. `free_parameters = 0`.

**2026-07-27 — Route 1 (geometric W_λ) re-run with the CORRECT normalizer `d_q²/D²`:
still WALL(scope-a); the sibling's `d_q²/[n]_q!` was un-normalized.** (PR #4392,
`claude/deltalambda-s5so3-geometric-wlambda-2026-07-27`.) The sibling Route-1
(`S5So3WLambdaLift.lean` #4376) re-weighted the H₉ cabled-Borromean cluster with
`W^{raw}_λ = d_q²/[n]_q!` → `r_raw = 52.62` (33× overshoot). But at q₀>1 that proxy
sums to `Σ = D²/[n]_q! = 1.1109 ≠ 1` — **not** a probability measure. The corpus's own
`WLambdaMTCLocalizationObligation.lean` fixes the genuine Beasley–Witten / WRT(S³/2I)
localization weight as `W^{geom}_λ = d_q²/D²`, `D² = Σd_q²`, `Σ=1` (C1). Forward-
evaluated on the **identical** #4364 word/E₀/|χ_λ| (0 fit): `c₃(geom) = +14.07 MeV =
29.9× μ₃`, **`r_geom = r_raw/S = 47.37`** vs needed `r*≈1.585`. The correct normalizer
shifts the number 11 % but **not** the verdict: **WALL(scope-a)**, ~30× overshoot.
**No other geometric W_λ to try** — self-duality `S⁴=1` (2026-07-17) + framing collapse
(2026-07-12, `KeystoneModularTwist`) ⇒ `d_q²/D²` **is** the geometric measure; the route
converges on this wall. **Declined fit-trap:** both-Σ=1 comparison gives `r_geom·Σy_λ =
1.504` (5.1 % short, and a normalization convention `ρ_F` does not use); exact closure
needs a μ₃-inverted rescale = FIT. Lean `S5So3GeometricWLambda.lean` sorry-free
(lean-direct exit 0): `geom_ratio_eq_raw_ratio_div_sum`, `geom_measure_normalized`,
`geom_route_walls`, `geom_cluster_overshoots`, `route_closes_with_rescale_iff`. Probe +
witness `s5so3-geometric-wlambda-borromean-lift.witness.json`. Audit
`2026-07-27-deltalambda-s5so3-geometric-wlambda.md`. Nothing wired; μ₃ never inverted;
`free_parameters = 0`.

**2026-08-01 — Milnor ORDER law: all-A lower bound `order(D_A) ≥ 2(A−1)` PROVED from
the h-adic filtration.** (PR #4471, `claude/deltalambda-milnor-order-law-proof-2026-08-01`.)
Predecessor #4389 (`MilnorParitySignLaw`) proved the leading Milnor order `2(A−1)` of the
A-component Brunnian trace deficit `D_A = 1−τ_A` **only at A=3** and recorded A=4 as a
measured `def` — two data points, no theorem. This turns them into a genuine **all-A
theorem**: the length-A iterated commutator of pure-braid band generators `A_{ij}` (each
`A_{ij}−1` divisible by `h`, the derivable ker(B_n↠S_n) fact underlying #4378's
strand-forgetting Brunnian check) accumulates one `h²` per commutator level. Formalized as
an h-adic filtration `HasOrder h k x := ∃c, x = am(h^k)·c` with proved `mul`/`commutator`
(orders add) + R-linear `trace` transfer; the left-normed tower `V(n+1)=[c(n+1),V n]` gets
`HasOrder(2(n+1))` **by induction** → **`brunnian_deficit_order_lower_bound`**: `τ(w_A)`
divisible by `h^{2(A−1)}` for **every** A ≥ 2. Tier: **bound + honest partial**. Exact `=`
re-derived at A=3 (`borromean_tight_slice`, cofactor(0)=3/4≠0 ⇒ tight); A=4 measured
(cited #4378); exact-all-A (leading coeff ≠ 0 = length-A Milnor μ̄ nonvanishing) left as a
content-bearing **conjecture class with NO instance** (`MilnorExactOrderConjecture`) —
NOT asserted proved. Lean `QOU/MassTheory/MilnorOrderLawGeneral.lean` sorry-free
(lean-direct exit 0, v4.24.0); generic `[CommRing R]/[Algebra R A]` per §7c, `ℝ` only for
the A=3 anchor. Complements #4389 (sign law); distinct angle from #4463/#4404 (μ₃
magnitude = the leading-coefficient *value* the conjecture leaves open). Audit
`2026-08-01-deltalambda-milnor-order-law-proof.md`. Nothing wired; no exact-law overclaim;
`free_parameters = 0`.

**2026-08-01 — GAP-A-4 coordination-EDGE route (the last un-excluded A=3 magnitude
reading): WALL(scope-a) — the third bond breaks Brunnian O(h⁴).** (PR #4472,
`claude/deltalambda-gap-a4-brane-tower-level-2026-08-01`.) #4364's H₉ word
`(Δ_A·Δ_B⁻¹)³` uses only 2 of 3 cable-pairs = the path `P₃` (2 edges); the physical
triton is `K₃` (3 edges, braid linear-order obstruction). Forward-derived, 0-fit edge
ratio `|E(K₃)|/|E(P₃)| = 3/2 = 1.5` (converges with #4392's fit-trap `1.504`, ~5% short
of `r*=1.585`). Probe `brane_tower_level_coordination_edge_probe.py` adds the third bond
`Δ_C=(1 2)(0 1)(1 2)` and MEASURES: path stays `O(h⁴)` (order 4.098, reproduces #4364 bare
deficit 0.049); triangle `(Δ_A·Δ_B⁻¹·Δ_C)³` **breaks Brunnian** (order 4.098→1.776=`O(h²)`,
overshoots ~400×, sign flip — the `{0,2}` sub-link goes non-trivial); cyclic bar-balanced
**cancels to 0** (~1e-14). So the `3/2` edge count has **no Brunnian-order-preserving braid
realization** — `lift_is_coefficient_ratio`'s shared-`h⁴` premise is destroyed. **WALL(scope-a)**,
NOT a (b) exclusion of the edge-count ingredient (the graph fact + conditional arithmetic
stand; only the braid realization of the premise is refuted). With the three prior walls
(2026-07-26) + geometric `W_λ` (#4392) this **brackets the A=3 magnitude source completely**:
neither a derived LEVEL, nor a geometric `W_λ`, nor a coordination-EDGE factor supplies the
`1.585×`. Lean `BraneTowerLevelAmplitude.lean` sorry-free (lean-direct exit 0):
`edge_ratio_A3`, `braid_order_gap_A3`, §3b-cond `CoordinationEdgeAmplitude` +
`fullCoordAmplitude_eq` (conditional; premise probe-refuted), `edge_scaling_near_miss`,
`edge_reweight_requires_brunnian` (measured order `1.776 ≠ 4`). Audit
`2026-08-01-deltalambda-gap-a4-brane-tower-level.md`. Nothing wired; μ₃ never inverted;
`free_parameters = 0`.
## 2026-08-01 — the partition-conjugation parity thread (GAP-1 exclusion + weight-class narrowing + the three-parity clarification)

Three merged PRs (#4387, #4399, #4481) working the Δ_λ **weight-class** structure via the
partition-conjugation parity of the deuteron H₆ Wedderburn sum. No fit; nothing wired;
`free_parameters = 0`.

- **Signed conjugation parity (#4387, merged).** The deuteron binding `B = m_e Σ_{λ⊢6} T_λ Δ_λ`
  (`T_λ = w_λ χ^λ`) transforms under the physical bar as `T_λ(q⁻¹) = (−1)^{n-1} T_{λ'}(q)`
  (`sgn = (−1)^{n-1}`, `= −1` for `n=6`); three exact identities (`w_λ=w_{λ'}`, `χ^{λ'}(q)=χ^λ(q⁻¹)`,
  `w_λ(q⁻¹)=(−1)^{n-1}w_λ(q)`). Consequence: the self-conjugate `(3,2,1)` is **bar-ODD** ⇒ feeds `t`,
  never `g₂`; `g₂ ← conjugate-pair asymmetries Δ_λ − Δ_{λ'}`, `t ← symmetric parts + (3,2,1)`. Lean
  `ConjugationParitySplit.lean` (sorry-free). Audit `2026-07-26-deuteron-conjugation-parity-categorical.md`.

- **GAP-1 exclusion (#4399, merged).** Any **conjugation-symmetric** dressing `Δ_λ = Δ_{λ'}` gives
  `g₂ = 0` (for even A, `sgn = −1`) — scope-(b), proved invariant. So the Markov weight `w_λ`,
  classical `dim(λ)²`, and hook-form q-dimension are **excluded**; the conjugation-**covariant Wenzl
  principal specialization survives** — independently selecting the corpus's production weight `y_λ`.
  This is the *complement* to the geometric-W_λ wall above: the symmetric q-Plancherel-type weights
  are excluded on parity grounds for even-A, consistent with the `d_q²/D²` overshoot. Lean
  `ConjugationSymmetricDeltaExcluded.lean` (sorry-free). Audit
  `2026-08-01-deltalambda-parity-exclusion-and-frontier-ties.md`.

- **Milnor-sign convergence is NOT a derivation (#4481, merged).** The `(−1)^{A−1}` match between the
  weight bar-sign `(−1)^{n-1}` (`n=3A`) and the Milnor-parity cluster-deficit sign (#4389) is a
  **convergence via distinct mechanisms, not a derivation**: the proved Borromean deficit
  `h⁴(3+h²)/(h²+4)` has leading order `h⁴ = h^{2(A−1)}` with the weight prefactor `h⁸ = h^{n−1}`
  **absent** (τ_A is a normalized ratio ⇒ the Ocneanu weight cancels), and the weight order
  `3A−1 > 2(A−1)` is subleading. Lean `MilnorWeightParityConvergence.lean` (sorry-free). Audit
  `2026-08-01-milnor-sign-weight-parity-convergence.md`.

**Three-parity clarification (for siblings).** The corpus now holds **three distinct parity
sign-readings**, and none derives another: (i) Milnor deficit sign `(−1)^{A−1}` (#4389, cluster deficit;
A=3 proved, A=4 measured); (ii) winding-parity `N(φⁿ)=(−1)ⁿ` (#4401, the **decay/`Im𝔙` S-channel**
sign, explicitly self-scoped "conjectural mechanism, not a derivation"); (iii) the Ocneanu-weight
bar-parity `(−1)^{n-1}` (#4387/#4399, the **binding weight class**). (i) and (iii) share the value
`(−1)^{A−1}` but arise from distinct-order objects (#4481); (ii) is a different observable. **Do not
join them into a single "meeting-point" derivation** — that would manufacture a spurious link across
observables.

**Net for the magnitude gate:** the parity thread **narrows the weight class** (symmetric excluded ⇒
principal specialization) but does **not** touch the standing magnitude gate — the A=3 `~1.6×`
coefficient (`c₃ = 0.63×μ₃`, `μ₃ = +0.4708`). This orthogonality is now made explicit (scope-(a)
negative, #4486, probe `a3_magnitude_parity_orthogonal_probe.py`, audit
`2026-08-01-a3-magnitude-parity-orthogonal.md`): at `n=9` (`sgn=+1`) parity is a **relabeling not a
rescaling** (R1) and the `c₃` gap lives at the **bare single-trace level**, not the `Δ_λ`-dressing
level where parity acts (R2). So parity cannot supply the `~1.6×`; that coefficient remains the open
Track-A gate. **Do not re-try parity for the magnitude.**

**2026-08-01 — Milnor EXACT-order coefficient: Route B proved trace-cyclicity
sub-wall; Route C extends to A=5/A=6 (4 data points); μ̄_A ratio is −2, NOT the
1.585× magnitude bridge.** (PR #4480,
`claude/deltalambda-milnor-exact-coefficient-2026-08-01`; continues #4471.)
Attacked #4471's open exact order law `order(D_A) = 2(A−1)` (= leading
coefficient μ̄_A ≠ 0). **Route B (PROVED NEGATIVE):** #4471's order engine is the
*Lie* iterated-commutator tower `iterCommTower`; a genuine *cyclic* Markov trace
annihilates every ring commutator, so `cyclic_trace_kills_iterCommTower` — the
trace of the whole top level is 0, and #4471's `HasOrder.trace` witness is `s=0`
(`leading_coefficient_witness_is_uninformative`). The leading coefficient is
therefore provably NOT extractable from the Lie tower via the trace; it lives in
the *group*-commutator / finite-type (Milnor/Vassiliev) structure — Route A,
Mathlib-inaccessible, CITED not axiomatised. **Route C (compute):** measured the
Brunnian deficit orders + leading coefficients (both conventions coincide): orders
`4,6,8,10` → exactly `2(A−1)` (A=5/A=6 NEW, turns #4471's 2 data points into 4);
μ̄_A = `(3/4)(−2)^{A−3}` = {3/4,−3/2,3,−6}, ratio **exactly −2**, sign `(−1)^{A−1}`
(matches #4389). **Bridge check:** the μ̄_A ratio is −2, and no combination lands
near the `r*≈1.585` magnitude factor this ledger's geometric-W_λ rows need — so the
exact-order leading coefficient is a clean object that does **NOT** encode the A=3
magnitude anomaly; the missing `1.585×` structure lives elsewhere. Lean
`MilnorExactCoefficient.lean` sorry-free (lean-direct exit 0), no
`MilnorExactOrderConjecture` instance fabricated; measured A=5/A=6 recorded as
`def`s. Probe/witness `milnor-exact-coefficient.witness.json`; audit
`2026-08-01-deltalambda-milnor-exact-coefficient.md`. Nothing wired; μ̄ extracted
never fit; `free_parameters = 0`.

**2026-08-01 — Milnor exact-order coefficient: POSITIVE Magnus realization —
`μ̄(12…A) = ±1 ≠ 0` PROVED via the faithful nilpotent (elementary-matrix)
representation; the surviving coefficient is off-diagonal / trace-invisible (the
positive counterpart of #4480 Route B).** (Branch
`claude/milnor-exact-order-coefficient-proof-2026-08-01`; continues #4471/#4480,
complements DD-1 `MilnorVassilievGrading`.) Attacked the honest sub-target
"length-A Milnor leading coefficient ≠ 0". **PROVED (sorry-free, 0 free params,
`MilnorMagnusCoefficient.lean`):** evaluating #4471's *Lie* iterated-commutator
tower `iterCommTower` on the **Magnus generators** `c_i = E_{i,i+1}` (elementary
matrices in `Mₙ(R)`, the faithful strictly-upper-triangular / free-2-step rep)
telescopes to a single off-diagonal elementary matrix:
`iterCommTower_magnusGen : iterCommTower magnusGen n = (−1)ⁿ • E_{0,n+1}`, hence
the tower is NONZERO (`iterCommTower_magnusGen_ne_zero`) and its `(0,n+1)` Magnus
coordinate — Milnor's `μ̄(12…(n+2))` — equals `(−1)ⁿ = ±1`
(`milnorMagnusCoeff_eq`, `milnorMagnusCoeff_ne_zero`). This is Milnor's classical
`μ̄(12…A)=±1≠0`, **derived** (matrix computation), not fitted, at the natural
Vassiliev degree `A−1` (matching DD-1's `milnorVassilievDegree`). **Positive
counterpart to Route B:** the surviving coefficient sits in the off-diagonal
`(0,A)` entry — a NON-cyclic coordinate functional — whose cyclic *trace* is `0`
(`trace_magnusGen_realization_eq_zero`, off-diagonal), in exact agreement with
#4480's `cyclic_trace_kills_iterCommTower`. Sharpens the wall: the leading
coefficient EXISTS and is nonzero *as an algebra element*; it is the cyclic trace
that annihilates it, NOT the coefficient that vanishes. **Does NOT close
`MilnorExactOrderConjecture`** (the QOU *Markov-trace* deficit `D_A`'s leading
coefficient ≠ 0): identifying the off-diagonal Magnus coefficient `±1` with the
Markov-trace deficit coefficient is the Bar-Natan / Habegger–Masbaum
Milnor = leading-Vassiliev bridge (`BrunnianVassilievBridge`, instance-less),
Mathlib-inaccessible — CITED, not axiomatised. No conjecture instance fabricated;
the trace-normalised `μ̄_A = (3/4)(−2)^{A−3}` (#4480) stays MEASURED. lean-direct
exit 0. `free_parameters = 0`. Open follow-up: bean `qou-v7ro` (bridge Magnus coeff → Markov-trace deficit coeff).

**2026-08-01 — A=3 beyond-Hecke MAGNITUDE via the Vassiliev WEIGHT: leading-weight ≤ Hecke
bound REFUTES the `1.585×` (scope-b of the bare-weight claim).** (PR pending,
`claude/deltalambda-beyond-hecke-vassiliev-magnitude-2026-08-01`.) **Distinct angle:** the A=3
3-body **magnitude** (`r* = μ₃/c₃ ≈ 1.585`), tested against a Kontsevich/Vassiliev
weight-system correction of the proved Borromean deficit — *not* the exact-order μ̄_A
coefficient (#4480 owns that; ratio −2) and *not* the A=4 magnitude (#4472 owns that);
Vassiliev-scaffold overlap (#4479) is permitted. **Object:** the proved deficit
`1−τ_Borr = h⁴(3+h²)/(h²+4)`; its leading finite-type (Vassiliev degree `2(A−1)=4`) weight is
the `h→0` symbol `(3/4)h⁴`. **Decisive bound (exact, all h):**
`(3+h²)/(h²+4) − 3/4 = (h²/4)/(h²+4) ≥ 0`, so the leading weight is the *smallest* term of a
positive convergent series ⇒ **weight/Hecke ≤ 1 < 3/2 < r*** (Lean
`leadingWeight_le_borrDeficit`, `vassiliev_weight_cannot_supply_magnitude`). Numerically at the
muon q₀: weight/Hecke = 0.9964, the **whole** finite-type correction is +0.36 %, not the +58.5 %
needed. **Mechanism:** the finite-type filtration *re-expands the same Markov trace the Hecke
level already sums*; the near-miss `c₃ = 0.297` IS the full finite-type sum, so no truncation
exceeds it — the `1.585×` lives OUTSIDE the finite-type filtration of the single Borromean
deficit. **Length-A Milnor reading (`A−1=2`):** μ̄(123) is an INTEGER Vassiliev invariant `±1`
(#4479 `BrunnianVassilievBridge.muBar_realized`, `val:K→ℤ`), measured ratio `−2`; no integer =
`r* ∈ (3/2,2)` (`no_integer_weight_eq_rStar`). **Numerology dismissed:** `r* ≈ log₂3` is an
irrational coincidence (`two_pow_ne_three_pow`: `2^a` even ≠ `3^b` odd). **Verdict
REFUTE(scope-b)** of the bare-weight-as-magnitude claim (cites two proved invariants: the ≤-bound
+ integrality); explicitly NOT a general exclusion of the Vassiliev ingredient from a larger
multi-channel closure (untested). This closes the finite-type route too — the four prior walls
(LEVEL / geometric `W_λ` / EDGE / exact-order μ̄_A) plus this bracket the A=3 magnitude source
completely at the Hecke *and* finite-type levels; the `1.585×` needs structure outside the
single-deficit filtration (e.g. an operator-valued cross-channel combiner). Lean
`VassilievMagnitudeA3.lean` sorry-free (lean-direct exit 0); probe/witness
`vassiliev-magnitude-a3.witness.json`; audit
`2026-08-01-deltalambda-a3-beyond-hecke-vassiliev-magnitude.md`. Nothing wired;
`free_parameters = 0`.

**2026-08-01 — PROBE 2 (A=4 interface operator + s5-so3 geometric W_λ on ⁴He): the
reweighting BRACKETS both AME targets but hits neither, and is NOT excluded — WALL(scope-(a)).**
(PR TBD, `claude/deltalambda-a4-helium-interface-operator-2026-08-01`.) With the A=4 SIGN
settled (#4378: `τ_L₄>1` ⇒ `c₄<0` compatible with `μ₄<0`), the MAGNITUDE became live. The
s5-so3 fiber action (`conj:s5-so3-fiber-action`) supplies a **normalized** color-tube weight
(`Σ W_λ=1`); its genuine geometric measure is the SAME Beasley–Witten `W_geom=d_q²/D²` #4392
used at A=3. Forward-evaluated 0-fit on the canonical b0vf ⁴He `H₁₂` per-block table
(`chi-helium-4-h12-at-q0-50dps`, 77 λ⊢12), `E₀=4.18598`: production `E₀·Σy_λ|χ_λ|=0.243 MeV`
(**undershoots** B(⁴He)=28.30 by 117×), geometric `E₀·ΣW_geom|χ_λ|=60.33 MeV`
(**overshoots** by 2.13×; `r_geom=248.5` vs A=3's 47.4 — `d_q²` concentrates even harder at
n=12). The two 0-fit endpoints **bracket** both targets (`0.243 < 4.591 < 60.33` and
`0.243 < 28.30 < 60.33`) but **neither lands**. Crucially the normalized-measure bound
`E₀·max_λ|χ_λ|=266 MeV` (`max|χ|=63.6` at λ=(6,3,3)) is **above** both targets ⇒ the target
is **reachable in principle** by some normalized `W` — **NOT a scope-(b) exclusion**; an exact
hit needs a tuned intermediate weight = **FIT**, declined. (The pre-existing
`a4_option_e_color_tube_closure.py`'s ad-hoc `10³` "color-tube scale" IS such a fit; NOT used.)
So the s5-so3 interface operator does **not** supply the A=4 magnitude as-is — **WALL(scope-(a))**,
mirroring the fully-bracketed A=3. Lean `GeometricWLambdaA4Helium.lean` sorry-free (lean-direct
exit 0, v4.24.0): the reusable invariant `normalized_reweight_abs_le_bound` (`ΣW=1,W≥0,|x|≤B ⇒
|ΣWx|≤B`), `bracket_B4He`/`bracket_absMu4`, `geom_ne_targets`, `targets_within_bound`, capstone
`a4_magnitude_bracketed_not_closed_not_excluded`. Probe/witness
`s5so3-geometric-wlambda-a4-helium.witness.json`; audit
`2026-08-01-deltalambda-a4-helium-interface-operator.md`. GAP bean filed. Nothing wired;
B(⁴He)/μ₄ never inverted; `free_parameters = 0`.

**2026-08-01 — ROUTE 1 (A=3 operator-valued branching combiner): the trace-based
combiner = the scalar Markov trace EXACTLY — supplies ZERO magnitude —
REFUTE(scope-(b)).** (Branch `claude/a3-magnitude-operator-branching-combiner-2026-08-01`,
bean `qou-jv64`.) Tests the `qou-tnvz` surviving hypothesis that keeping the
operator (matrix) structure through the `H₉→H₆→H₃` Wenzl branching, instead of
collapsing to a scalar `Σ_λ y_λ χ_λ` trace at each level, retains cross-channel
information the single trace loses — and thereby supplies the `r* = μ₃/c₃ ≈ 1.585`
(μ₃=+0.4708, c₃=0.297). **Formalize-first verdict: the premise is FALSE at the
observable level.** The observable is a cyclic additive trace `τ` of the assembled
operator sliced by the branching's isotypic projectors `{P i}`; the governing
invariant is the **partition-of-unity trace collapse** `τ X = Σ_i τ(P_i·X·P_i)`
(off-diagonal blocks vanish under the closed trace; per-block weight identically
`1`). So the block-resolved operator-combiner readout **equals the scalar Markov
trace exactly** — keeping the operator structure multiplies by a factor of
**exactly `1.0`** (0 % of the needed `+58.5 %`; gap `≡0`), reproducing `c₃=0.297`
never `μ₃=0.4708`. **Numerical shadow (independent):** `canonical_tr_m_via_branching.py`
already records branching ≡ transfer trace to `4.7e-15` for A≥3. **The "by how much":**
`weightedReadout_sub_trace` proves the only way a block decomposition yields a value
`≠ τ X` is a **non-uniform per-block weight `w_i ≠ 1`** — precisely a `Δ_λ`-type
per-partition weight, a *different functional* than the trace, which the combiner
does NOT retain. **Verdict REFUTE(scope-(b))** of ROUTE 1 as stated (cites the
proved partition-of-unity trace-collapse invariant); explicitly **NOT** an
exclusion of a non-uniform `w_i`/`Δ_λ` route — that stays open (the A=4 PROBE-2
geometric-`W_λ` bracket is the live instance). Lean
`QOU/BraidKnot/A3OperatorCombinerMagnitude.lean` sorry-free (lean-direct exit 0,
v4.24.0): `trace_partition_collapse`, `operatorCombiner_eq_scalarTrace`,
`weightedReadout_sub_trace`, `weightedReadout_eq_of_uniform`,
`magnitude_change_forces_nonuniform_weight`. Audit
`2026-08-01-a3-magnitude-operator-branching-combiner.md`. Nothing wired; `μ₃`
never inverted; `free_parameters = 0`.

## 2026-08-01 — A=3 magnitude ROUTE 3: multi-sub-link channel sum — WALL(scope-b), Brunnian triviality

The A=3 magnitude program asks what supplies the residual factor `r* = μ₃/c₃ ≈ 1.585`
(the near-miss `c₃ = 0.297 = 0.63× μ₃`, #4364 — complete finite-type sum of the ONE
Borromean deficit), bracketed out of every SINGLE-Markov-trace re-weighting
(three-walls audit `2026-07-26-deltalambda-a3-magnitude-source-three-walls.md`).

**ROUTE 3 (the channel-sum reading):** the triton = 3 nucleons = three 2-body sub-links
PLUS the 3-body Borromean. Test whether summing the **distinct** sub-link trace objects
(`Σ = f₁₂+f₁₃+f₂₃+f₁₂₃`, or the multiplicative `1−∏(1−fᵢ)`) supplies `r*` — structurally
different from every bracketed probe (a sum of distinct traces, not a re-weighting of one).

**VERDICT: WALL(scope-b) — Brunnian sub-link triviality kills it.** The Borromean rings are
the archetype Brunnian link: every proper 2-sub-link is the UNLINK. Verified exactly
(`borromean_sublink_channel_sum_probe.py`): strand-forgetting on `w₃=[A₀₁,A₁₂]` collapses
each pairwise sub-word to the **empty word** (a commutator with one argument deleted), so
through the corpus χ_λ/y_λ pipeline every pairwise deficit `fᵢ = 0` **exactly**. Both
closures then collapse to the single 3-body deficit — the multiplicative closure's cross
terms all vanish (each `1−fᵢ=1`) — so the channel decomposition supplies magnitude factor
**exactly 1**. `r* ≈ 1.585 ≠ 1` is NOT supplied. This is the AGENTS.md "compositional/trace
object is already many-body" caveat *turned decisive*: the caveat protects cross terms only
when the pairwise deficits are nonzero; here they are **provably zero**, so the cross terms
vanish and the route adds nothing.

- **(b) not (a):** invariant cited = Brunnian sub-link triviality (proper 2-sub-links of 𝓑₃
  are unlinks ⇒ deficit identically 0). Scoped to the canonical Borromean triton model; a
  non-Brunnian link with linked pairs would give nonzero channels but is a different,
  non-canonical choice (and tuning one to hit 1.585 is a FIT — not made).
- **Lean:** `QOU.MassTheory.BorromeanSubLinkChannelSum` (sorry-free, lean-direct exit 0):
  `brunnian_channelClosureMul_eq_triple` (decisive collapse), `brunnian_channel_no_magnitude`
  `[IsDomain]`, `borromean_channelClosure_eq_c3` / `borromean_channel_ne_r_star` (ℝ). Generic
  `[CommRing R]` per §7c.
- **Probe/witness:** `computations/deltalambda/borromean_sublink_channel_sum_probe.py` /
  `borromean-sublink-channel-sum.witness.json` (`closes=false`, `free_parameters=0`).
- **Audit:** `docs/audits/2026-08-01-a3-magnitude-sublink-channel-sum-brunnian-wall.md`.
- **Bean:** `qou-dka4`. Nothing wired; μ₃/c₃ never inverted.

Sharpens the frontier: the A=3 magnitude source cannot be any *sub-link-additive* or
*-multiplicative* object over the Borromean model — it must be an *irreducible* enhancement
of the single 3-body trace itself (the three-walls "strictly larger h⁴-coefficient no
substrate rule supplies"). Complements sibling ROUTE 1 (operator-branching) / ROUTE 2
(super-Berezinian).

**2026-08-01 — A=3 magnitude ROUTE 2 (super-Berezinian even/odd cross-sector mixing): the
`r*≈1.585` is a FREE parameter of the cross-term — scope-(a) underdetermination, NOT a
closure and NOT an exclusion.** (Branch
`claude/a3-magnitude-super-berezinian-cross-sector-2026-08-01`, bean `qou-6r6d`; feeds
`qCubicGradedSplit` / `qou-jqof` / PR #4140.) With every SINGLE-trace ingredient bracketed at
`c₃=0.63·μ₃` (LEVEL/geometric-`W_λ`/EDGE/`μ̄_A`/Vassiliev), tested the only genuinely
cross-**sector** candidate — the Berezinian off-diagonal `t=B·D⁻¹·C` coupling the bar-even
(cosh/mass/C1) and bar-odd (sinh/decay/GGM) faces. **Distinct angle from the on-main parity
bricks** (`OddDecayWeightParity` #4140-adjacent, `BerezinianSelfAdjointCrossTerm` 2026-07-31):
those settle the cross-term SIGN (bar-odd ⇒ needs non-self-adjoint independent off-blocks);
this attacks the MAGNITUDE. **Decisive invariant (Lean `SuperBerezinianA3Magnitude.lean`,
sorry-free, lean-direct exit 0, generic `[Field R]`):** the even-face correction `(A−t)/A` is
**surjective** in the off-block `B` (`crossTerm_magnitude_surjective`, witness `B=A(1−r)DC⁻¹`),
while block-diagonal/single-trace data gives correction `≡1` (`evenFaceCorrection_no_mixing` —
*why* single-trace is bracketed: `t=0` can't move the coefficient). So `r*` is reachable **only**
by pinning `B` to the target = a **FIT**; the off-block magnitude is a **hidden DOF (Rule 14)**.
Empirical companion `a3_magnitude_berezinian_crossterm_probe.py` (0 fit): `r*=1.5852≈log₂3`
(flagged coincidence); **0/13** natural parameter-free substrate readings of `ρ=t/A`
(`ℏ_q,h,h²,(1+q)/2,±sector-ratio,±1,±2`) land `r*` (scatter `0.0..3.0`); fit witness
`B*=−0.585` hits `r*` exactly. **VERDICT scope-(a):** the cross-term does NOT derive `r*` — it
**relocates** the wall from "which single trace" to "**derive the off-blocks `B,C`**" (the DM
q-cubic period datum = `qou-jqof`, open). **First A=3-magnitude route NOT excluded** (unlike the
single-trace family it CAN reach `O(1)`), but not a closure. `A3CrossTermMagnitudeClosed`
(§3b-tax dependent, NO instance) is the honest open carrier. Audit
`2026-08-01-a3-magnitude-super-berezinian-cross-sector.md`; witness
`a3-magnitude-berezinian-crossterm.witness.json`. Nothing wired; `μ₃`/`c₃` never inverted;
`free_parameters = 0`.

**2026-08-01 — A=3 magnitude ROUTE 4: a Habiro-ring FIBRE element does NOT supply `r* ≈ 1.585`
— two-part honest negative REFUTE(scope-b) + WALL(scope-a).** (Branch
`claude/a3-magnitude-habiro-fibre-element-2026-08-01`, bean `qou-2ybf`.) **Distinct angle:** the
last candidate named by the Vassiliev audit ("structure OUTSIDE the finite-type filtration") — a
fibre-level cyclotomic-completion element `F(q) = Σ_n a_n(q)(q;q)_n`, parallel to the proved α_EM
`[2]_q(1−h²α)` (#1511) and the Q_β Habiro element. **Decisive obstruction — the substrate anchor
is `q₀ > 1`:** the Habiro ring `ℤ[q]^ = lim ℤ[q]/((q;q)_n)` evaluates canonically at roots of
unity / inside `|q|<1`, but `q₀ ≈ 1.10998 > 1` is OUTSIDE both. For real `q>1` the cyclotomic
basis magnitude `|(q;q)_n| = ∏(q^k−1)` is **UNBOUNDED** (`|(q;q)_40|≈1.8·10³¹`; Lean
`pochAbs_unbounded` via geometric doubling once `q^{n+1}−1≥2`), so an integer-coefficient
completion series has non-vanishing terms and **diverges** there (`habiro_terms_not_tendsto_zero`)
— a genuine infinite Habiro element has NO canonical archimedean value at the substrate ⇒
**REFUTE(scope-b)**, cited invariant `pochAbs_unbounded`. **Finite sub-case:** the only Habiro-
shape elements evaluable at `q₀>1` are FINITE (Laurent), i.e. the α_EM shape `[k]_q(1−h²X)` — a
genuine Laurent object (the α_EM/Q_β elements ARE finite Laurent, not infinite tails). Those are
bracketed: `r*∈(3/2,2)` lies STRICTLY between `[1]_q=1` and `[2]_q=q₀+q₀⁻¹≈2.011`
(`rStar_strictly_between_q1_q2`); the `(1−h²X)` correction is negligible (`h²X≈6·10⁻⁵`); no
derived (0-fit) integer `k` or categorical `X` lands on `r*` (best fit-scan `[6]_q/[4]_q=1.554`,
−1.9%, is a scan match not a forced value) ⇒ **WALL(scope-a)**. **Net:** no DERIVED Habiro
element reproduces `r*` — the genuinely-new infinite completion diverges at `q₀>1`, the
well-defined finite part is the already-bracketed quantum integer. Consistent with the fibre-vs-
observable framing (the c_k / magnitude coefficients live in the fibre; a REAL `f(q₀)` was already
refuted, #1821). The `1.585×` needs structure genuinely outside the single-deficit filtration AND
representable as a finite / resummed object at `q₀>1` — an operator-valued cross-channel combiner,
not a bare cyclotomic-completion tail. Lean `HabiroMagnitudeA3.lean` sorry-free (lean-direct exit
0, no trivial-true/native_decide/axiom); probe/witness `habiro-magnitude-a3.witness.json`; audit
`2026-08-01-deltalambda-a3-magnitude-habiro-fibre-element.md`. Nothing wired; `μ₃/c₃`/AME/CODATA/
`q₀` never inverted; `free_parameters = 0`.

## 2026-08-02 · A=3 magnitude ROUTE 6 (frame/units audit) — headline CONCEDED to ROUTE 5

PR #4491 (`claude/mu3-target-frame-robustness-2026-08-01`) audited μ₃'s well-posedness from a
frame/units angle. Its **headline over-claimed** and is **conceded to ROUTE 5** (`a9c2ee94`): the
subtracted ladder `ρ_grad = [A]_q!/[2]_q!` is *pinned* to the coinvariant graded dimension (Poincaré
series, #4300), so the "1.73× baseline-class spread" (balanced-quantum / classical alternatives) is
**illegitimate** — μ₃ is well-posed at ~10% (isospin ±8%, `r* ∈ [1.50,1.71]`, cond-#≈8), not an
artifact. Score derived `c₃` by **sign + `r* ∈ [1.50,1.71]`**, not 1.585 to 3 sig figs. **Survivors**
(independent of the retracted headline): the A=3/A=4 **order-separation** prune (higher-cluster-order
route cannot close the gap — bounded `|aₖ|≤2` tail ≤0.7% ≪ miss; needs a new leading-order Δ_λ
channel); the cond-#≈8 "report on the physical ratio" discipline (= ROUTE 5); and a **units-labelling
flag** (borromean probe:188 compares `c₃` MeV to `μ₃` dimensionless, "read as MeV"). Lean
`Mu3BaselineFragility` / `A3PrecisionOrderSeparation` / `A4PrecisionOrderSeparation` /
`A3UnitsConsistency` (sorry-free). The **C_knot / Δ_λ magnitude** remains open (bean `qou-3q7t`); the
**binding weight is pinned to the Markov `y_λ`** (W_λ excluded, conjugation symmetry — PR #4543,
`BindingWeightMarkovPinning`). Nothing wired; `μ₃/c₃`/AME/CODATA/`q₀` never inverted.

## 2026-08-02 · A=3 magnitude ROUTE 2-b (off-block DERIVATION) — the branching Schur complement is a REDUCTION, r*>1 lift UNREACHABLE (scope-(b))

(Branch `claude/a3-offblock-derivation-2026-08-02`.) Attacks the wall ROUTE 2 (#4544,
`SuperBerezinianA3Magnitude`) relocated: **derive the off-blocks `B,C`** instead of leaving `B`
free. **Derivation (categorical, 0 fit):** the bar-self-adjoint `H₃(q)` mass endomorphism
`diag(a,c,b)` (`a=m₍₃₎`, `b=m₍₁,₁,₁₎`, `c=m₍₂,₁₎`), rotated into the **transpose-involution
eigenbasis** (the super-sector grading — `q↔q⁻¹` = transpose swaps `(3)↔(1,1,1)`, fixes self-conj
`(2,1)`), **PINS** the off-blocks with no residual freedom: `B=C=(a−b)/2`, `D=(a+b)/2`. The equal
Borromean characters `χ₍₃₎(β)=χ₍₁,₁,₁₎(β)=1` (proved, `(σ₁σ₂⁻¹)³`) make `B` a pure Markov-weight
difference. **Result — scope-(b) structural exclusion (invariant `sq_nonneg`):** the derived
even-face factor is `magnitudeFactor = 1 − ((a−b)/(a+b))² ≤ 1` for all real `a,b` with
`a+b ≠ 0` (`D` invertible; the Schur complement's `D⁻¹` requires it)
(`magnitudeFactor_le_one`) — the self-adjoint branching Schur complement is a **REDUCTION**, never
a lift, so the observed `r* = μ₃/c₃ ≈ 1.585 > 1` (and the whole ROUTE-5 band `[1.50,1.71]`) is
**structurally unreachable** (`observed_lift_unreachable`). **Sharpens ROUTE 2:** the branching is
not merely *silent* on `B` (ROUTE 2's surjectivity = fit), it *positively* supplies the wrong-sign
(`≤1`) self-adjoint off-block; the lift must come from an **anti-self-adjoint** (`C≠−σB`, two
independent amplitudes) GGM/Stokes off-block the branching leaves FREE — the DM q-cubic wall
`conj:qdifference-kernel-prolongation-symbol` / `qou-jqof`. Recorded as §3b dependent class
`A3LiftFromDerivedOffBlock` (content-bearing, **NO instance**). Parity certificate: the branching
assembly is graded self-adjoint (`branching_graded_selfadjoint`: `B=C` + `σB=−B` ⇒ `C=−σB`), so
`BerezinianSelfAdjointCrossTerm` ⇒ bar-EVEN cross-term = the correct parity for the bar-even ratio
`r*`, but bounded `≤1`. Lean `QOU/QBeta/A3OffBlockDerivation.lean` sorry-free (lean-direct exit 0,
0 real sorries, no native_decide/trivial-true/axiom), wired into `QOU.lean`. Nothing fitted,
nothing wired; `μ₃/c₃`/AME/CODATA/`q₀` never inverted; `free_parameters = 0`.

## 2026-08-02 · A=3 magnitude ROUTE 2-c (anti-self-adjoint amplitude) — the single open door is ONE free amplitude E; scope-(a), lift carried by exactly one real DOF

(Branch `claude/a3-antiselfadjoint-lift-2026-08-02`, bean `qou-jqof`.) Attacks the single door
ROUTE 2-b (`A3OffBlockDerivation`) named: the **anti-self-adjoint** off-block (`C≠−σB`) the
self-adjoint branching leaves free. **Distinct angle:** rather than re-derive the branching
off-blocks, decompose the *actual* off-block into its graded-self-adjoint value plus an
anti-self-adjoint amplitude, `C = −(σB) + E` (`E := C + σB`), and study the E-dependence.
**Decisive algebra (Lean `A3AntiSelfAdjointLift.lean`, sorry-free, lean-direct exit 0, generic
`[Field R]`):** the even-face Berezinian factor is **AFFINE** in the amplitude
`E` — `factor = factor_sa − B·D⁻¹·E/A` (`factor_affine_in_amplitude`), with `factor_sa ≤ 1` the
ROUTE 2-b self-adjoint reduction. Three consequences localise the wall to ONE scalar: (i) a genuine
lift `>1` **FORCES** `E ≠ 0` (`lift_forces_nonzero_amplitude` / `amplitude_nonzero`) — the lift is
impossible without an anti-self-adjoint amplitude; (ii) that `E` is **free** — `E ↦ factor` is
surjective onto `R`, witness `E* = (factor_sa−r)·A·D·B⁻¹` (`amplitude_surjective`), so the
anti-self-adjoint route is **NOT scope-(b) excluded** (it CAN reach `r*≈1.585`, contrast the
self-adjoint route); (iii) that `E` is **unique** (`amplitude_injective`) ⇒ `E ↦ factor` is a
**bijection**. **VERDICT scope-(a):** the A=3 lift is carried by **exactly ONE real degree of
freedom** — the anti-self-adjoint amplitude `E` — and it is free/unique, so pinning it to hit `r*`
is a **FIT** (`E*` anchor-inverted); the route does NOT close `r*`, it **isolates the wall to one
scalar** and proves that scalar is necessarily nonzero, free, and unique for any lift. Deriving `E`
from the DM q-cubic / Yekutieli-Stokes prolongation symbol (`conj:qdifference-kernel-prolongation-symbol`)
IS the open keystone, recorded as §3b dependent class `DerivedAmplitudeGivesLift` (content-bearing,
**NO instance**). A **scope-(b)** upgrade would need a *proved* amplitude bound (`|E| ≤ …` from a
writhe cap / Stokes-constant bound) — precisely what deriving the prolongation symbol would supply,
and it is open. Also addressed Copilot review on ROUTE 2-b: `A3LiftFromDerivedOffBlock` now
quantifies a bar map `σ : R →+* R` with `C_geom ≠ −(σ B_geom)` (was a free `σB : R`); the
`magnitudeFactor_le_one` ledger phrasing above corrected to `a+b ≠ 0` (D invertible). Lean
`QOU/QBeta/A3AntiSelfAdjointLift.lean` sorry-free (lean-direct exit 0, 0 real sorries, no
native_decide/trivial-true/axiom), wired into `QOU.lean`. Nothing fitted, nothing wired;
`μ₃/c₃`/AME/CODATA/`q₀` never inverted; `free_parameters = 0`.

## 2026-08-08 · A=3 amplitude ROUTE 2-c-STOKES — the LOCAL Stokes/resurgence route CANNOT supply `E`; a WALL (scope-(a) + scope-(b) sub-exclusion)

(Branch `claude/deltalambda-stokes-amplitude-e-2026-08-08`, bean `qou-jqof`.) Attacks
`E` (the single free DOF ROUTE 2-c isolated) via the **local Stokes-constant / resurgence /
Écalle-Borel** angle — distinct from the DT-index route. **Verdict: WALL, not closure** —
extends PR #4790's retraction (C1's `∞` pure isoclinic ⇒ RSZ isoformal dim 0 ⇒ no local
Stokes data) to `E`. **The bridge (CITED MODEL, RSZ Thm 5.5.7 unipotency, not a fit):** the
amplitude a *local* q-Stokes datum supplies is the strictly-off-block part of the unipotent
q-Stokes matrix, a coordinate sum `∑_{i<d} coeffᵢvᵢ` (`stokesAmplitude`) over the `d =
rszIsoformalDim k r μ = Σ_{i<j}rᵢrⱼ(μⱼ−μᵢ)` slope-pairing moduli (RSZ Thm 3.3.5). **Two
branches, both wall the route (Lean `StokesAmplitudeE.lean`, sorry-free, lean-direct exit 0,
`#print axioms` = the 3 standard axioms, no `sorryAx`):** (i) **single-slope carrier**
(`k=1`, exactly C1's `∞`): `rszIsoformalDim_one = 0` ⇒ amplitude forced `0`
(`stokesAmplitude_eq_zero_of_dim_zero`) ⇒ composed with ROUTE 2-c's `amplitude_nonzero`, the
local Stokes data **cannot lift** (`pureIsoclinic_local_stokes_cannot_lift`, **scope-(b)**,
cited invariant = RSZ empty slope-pairing at `k=1`); (ii) **multi-slope carrier**: a local
lift *forces* ≥2 slopes (`local_stokes_lift_forces_positive_dim`), but then the amplitude is
**surjective onto `R`** (`stokesAmplitude_surjective_of_dim_pos`) ⇒ local Stokes data leaves
`E` **free**; its value lives in the **GLOBAL** (`0↔∞`) Birkhoff connection matrix
(theta-valued, un-started — #4790's W2 successor,
`2026-08-01-branch-selection-birkhoff-connection-matrix.md`), NOT any local Stokes constant.
So C1 (Fuchsian at 0, pure isoclinic at ∞) has **empty local Stokes data at every local
point** — the local route is walled either way. **Unifies the sibling Stokes negatives** at
the amplitude level (large-order `2πP≈1` not GGM `3`; bar-odd ladder anchor-blind/`Im=0` on
the real meridian; ±i phase not the Δ_λ sign): the carrier's *local* Stokes moduli is simply
too small to be `E`. Open successor = §3b dependent class `GlobalBirkhoffSuppliesAmplitude`
(content-bearing, **NO instance**; distinct from ROUTE 2-c's `DerivedAmplitudeGivesLift` — it
names the **global** Birkhoff datum, not the DM q-cubic). Audit
[`docs/audits/2026-08-08-stokes-amplitude-e-local-wall.md`](../audits/2026-08-08-stokes-amplitude-e-local-wall.md).
Nothing fitted, nothing wired; `μ₃/c₃`/AME/`q₀` never inverted; `q₀`-derivation not routed
through; `free_parameters = 0`.

**2026-08-02 — PROBE 2 (A=4 interface operator): the ≥4-body magnitude wall is a ONE-SCALAR
gate — the derived `−ln det(I+G)` form is SURJECTIVE onto (0,∞); naive uniform `z` scope-(b)
excluded — WALL(scope-(a)), sharpened from #4526.** (Branch
`claude/a4-interface-magnitude-2026-08-02`.) Consolidates the two A=4 magnitude framings and
proves they collapse to the SAME single under-determined categorical scalar. The merged #3924
`[1⁴]` exchange spectrum `{±√5,±1}` gives (derived, not asserted — `detG_eq_spectral_product`)
`det(I+G) = (1+m√5)(1−m√5)(1+m)(1−m) = (1−5m²)(1−m²)`, so `b₄(m) = −ln det(I+G)`, one free
per-pair magnitude `m`, derived ceiling `m<1/√5` (writhe cap). **MAIN
(`magnitude_form_surjective`):** for EVERY `t>0` there is `m∈(0,1/√5)` with `b₄(m)=t`, via the
closed-form root `m*(t)=√((6−√(16+20·e^{−t}))/10)` (algebraic, no IVT; `det(I+G)(m*)=e^{−t}`
exactly). So the derived form reaches the ENTIRE positive axis in its one scalar — every AME
target (`b₄≈9.243`, `|μ₄|≈4.591`, `B(⁴He)≈28.30`) is reachable (`documented_targets_all_reachable`)
⇒ **NOT scope-(b) excluded**; but the reaching `m` is a function of the target (anchor-inversion =
**FIT**) ⇒ **NOT closed**. This SHARPENS #4526: the obstruction is not the reweight-bracket width
but that the single scalar `m` is free (`b4_strictMono_on`: strictly increasing ⇒ exactly one
scalar, unique `m*`). **Scope-(b) exclusion (`naive_z_unphysical`):** the framework's naive
uniform per-pair magnitude `z≈0.499` has `5z²>1` ⇒ `det(I+G)(z)<0`, unphysical — cited invariant =
the exchange spectrum `{±√5,±1}` (⇒ most-negative scaled eigenvalue `−m√5` ⇒ the det form). Direct
analog of the #4526 geometric OVERSHOOT ⇒ **surviving mechanism = a categorical principle fixing
`m∈(0,1/√5)` strictly BELOW the naive `z`** (equiv. a normalized `W` strictly below `d_q²/D²`).
Distinct object from the A=3 binding weight #4543 pins to Markov `y_λ` (that's the per-partition
character weight; this is the `[1⁴]` exchange determinant ≥4-body term). Lean
`QOU/MassTheory/A4InterfaceMagnitude.lean` sorry-free (lean-direct exit 0, v4.24.0; no
trivial-true / native_decide / axiom): `detG_eq_spectral_product`, `detG_neg_of_above_ceiling`,
`naive_z_unphysical`, `b4_strictMono_on`, `magnitude_form_surjective`,
`documented_targets_all_reachable`, capstone `a4_magnitude_one_scalar_gate`. Probe/witness
`a4-interface-magnitude-one-scalar-gate.witness.json`; audit
`2026-08-02-a4-interface-magnitude-one-scalar-gate.md`. GAP bean filed. Nothing wired;
`μ₄`/`B(⁴He)`/`b₄` never inverted; `free_parameters = 0`.

## Shared bar-parity invariant with the μ-p route (2026-08-01)

The Δ_λ chirality sign `deltaSign λ = (-1)^(principal grading λ)`
(`QOU.BraidKnot.PrincipalGradingJetOrder.deltaSign`,
`QOU.BraidsAndKnots.PartitionOf5.deltaSign`) is the **bar-involution parity**
`q ↔ q⁻¹` of the principal-grading degree: each grading-1 generator is the
bar-odd `ℏ = q − q⁻¹`, so a degree-`d` monomial has bar-parity `(-1)^d`. This is
proved sorry-free in
[`QOU.BraidKnot.BarParityInvariant`](../../folio/quantum-observable-universe/lean/QOU/BraidKnot/BarParityInvariant.lean)
(`barEven_barOdd_pow_even` / `barOdd_barOdd_pow_odd`).

**Consequence for coordination:** the same `ℤ/2` bar-involution grading that
forces the μ-correction **bar-even** (#2584 refuted the bar-mixed projector shift)
*is* the Δ_λ mixed-sign chirality structure. Both open routes (GAP-A-4 muon,
GAP-A-3 / Δ_λ binding) go through the shared s5-so3 `W_λ` object and are gated by
this one invariant plus the heat-kernel-defect coefficient
(`WLambdaDefectClosedForm.n144C_closed_form`). A Δ_λ or μ-correction closure must
respect the bar-parity of its principal grading — a candidate whose bar-parity
mismatches its target sign is structurally excluded (`barEven_barOdd_forces_zero`),
independent of magnitude. Formalize-first record for bean `qou-ph2a`:
[`docs/audits/2026-08-01-mu-p-tension-attack-recon-floor-verdict.md`](../audits/2026-08-01-mu-p-tension-attack-recon-floor-verdict.md).

## 2026-08-08 · A=3 magnitude ROUTE 2-c (amplitude E) — the DT-index / 3d-index / graded-Euler route is BAR-PARITY EXCLUDED from supplying E (scope-(b))

(Branch `claude/deltalambda-dt-index-amplitude-e-2026-08-08`, beans `qou-3dya`/`qou-jqof`.) Attacks
the open keystone `qou-jqof` (derive the anti-self-adjoint amplitude `E` of ROUTE 2-c) via the
**DT-invariant / 3d-index / graded-Euler** substrate route — a **distinct angle** from the resurgent
Stokes route a sibling is on. **Verdict: scope-(b) route-scoped exclusion (proved invariant:
bar-parity).** The DT-index / 3d-index / graded-Euler datum is by definition an **integer** (a
Behrend-weighted virtual point count = alternating dimension sum `χ = Σ_k(−1)^k dim(G)_k ∈ ℤ`); a
ring-hom bar involution fixes `ℤ ↪ R`, so every DT value is **bar-EVEN** (`dtIndex_barEven`,
`map_intCast`). The amplitude `E = C + σB` is **bar-ODD** — *derived*, not assumed: the physical
mass/C1 face has a bar-even cross-term `B·D⁻¹·C` (parity of `r*=μ₃/c₃`), which with `B` bar-odd, `D`
bar-even forces `C` bar-odd (`crossTermBarEven_imp_C_barOdd`), hence `E` bar-odd (`amplitude_barOdd`).
Bar-even ∧ bar-odd ⇒ 0 (`barEven_barOdd_eq_zero`, invariant `char R ≠ 2`), so the nonzero `E` a lift
forces (`A3AntiSelfAdjointLift.amplitude_nonzero`) is **NOT** any DT-index value
(`dtIndex_cannot_supply_amplitude`). The DT route lives in the bar-EVEN (self-adjoint, `≤ 1`) sector
(`A3OffBlockDerivation.magnitudeFactor_le_one`); the lift lives in the bar-ODD sector. **This removes
the DT-index route from the ROUTE 2-c menu and hands `E` back to the bar-ODD resurgent-Stokes / DM
q-cubic sector** (`conj:qdifference-kernel-prolongation-symbol`) — the correct parity (±i / π/2),
converging with the Stokes-route sibling from a different direction. Consistent with
`amplitude_surjective` (some real bar-odd `E` hits `r*`, never a DT integer) and with Horn-1 (#4540:
the DT/Behrend sign is a real π-phase, bar-even). **Element-level analog of the established corpus
`QOU.BraidKnot.BarParityInvariant`** (`barEven_barOdd_forces_zero`, bean `qou-ph2a`/`s5bb`) — same
bar-parity filter, new step is `dtIndex_barEven` (DT integers are bar-even) + the DT↔`E` connection.
Lean `QOU/QBeta/DTIndexAmplitudeE.lean` sorry-free (lean-direct exit 0, 0 real sorries, no
native_decide/trivial-true/axiom), wired into `QOU.lean`. Nothing fitted, nothing wired;
`r*`/`μ₃`/`c₃`/AME/CODATA/`q₀` never inverted; `free_parameters = 0`. Audit:
[`docs/audits/2026-08-08-dtindex-amplitude-e-bar-parity-exclusion.md`](../audits/2026-08-08-dtindex-amplitude-e-bar-parity-exclusion.md).

## 2026-08-08 · A=3 magnitude ROUTE 2-c (amplitude E) — WELL-POSEDNESS: E is the gauge-invariant CROSS-RATIO of the Birkhoff matrix, NOT a single (frame-dependent) entry

(Branch `claude/deltalambda-birkhoff-wellposed-2026-08-08`, bean `qou-wiub`/`qou-jqof`.) Red-team /
well-posedness mirror of the μ₃-target-robustness audits, complementary to the sibling constructing
the connection matrix explicitly (they own `BirkhoffAmplitudeE.lean`; this owns
`BirkhoffAmplitudeWellPosed.lean`). Two merged results (`DTIndexAmplitudeE` #4810, `StokesAmplitudeE`
#4811) pinned the anti-self-adjoint amplitude `E := C+σB` to the GLOBAL `0↔∞` Birkhoff connection
matrix `P=(X^∞)⁻¹X^0` of C1. **Before a value is extracted: is `E` a single entry of `P`, or a
gauge-dependent combination requiring the full monodromy?** By `QCharacter.IsQChar.ratio_qInvariant`,
the local solution bases are unique only up to a `q`-invariant (elliptic) normalisation, so `P` carries
a residual gauge `P ↦ D_∞⁻¹ P D_0`, entrywise `P_{ij} ↦ (d_∞,i)⁻¹ P_{ij} (d_0,j)`. **Verdict — MIXED,
both branches proved sorry-free: (a)** the cross-ratio `crossRatio P := P₀₁·P₁₀/(P₀₀·P₁₁)` is
gauge-invariant (`crossRatio_gauge_invariant` — the four gauge units cancel) and is the UNIQUE invariant
(`gauge_fixes_all_iff`: the gauge stabiliser of a generic 2×2 `P` is the 1-parameter global scale, so
`4−3=1` invariant); **(b)** a single entry is NOT invariant — it carries a full elliptic-unit gauge
freedom (`entry_gauge_orbit_surjective`: any `u·P₀₁` reachable; `entry_not_gauge_invariant`: a nontrivial
gauge moves it), so reading `E` off one entry is **ill-posed**, needing an extra normalisation datum.
**Consequence:** `E` is a frame-free physical amplitude (`A3AntiSelfAdjointLift.amplitude_injective`), so
it must equal the gauge-invariant cross-ratio, not a matrix element — **the sibling should target
`crossRatio(P)`.** Recorded as the OPEN §3b carrier `AmplitudeIsGaugeInvariantCrossRatio`
(`E = crossRatio P ∧ E ≠ 0`), NO instance; choosing the cross-ratio to hit `r*` (`amplitude_surjective`)
would be the forbidden fit and is not done. Bar-oddness of `crossRatio(P)`
(`DTIndexAmplitudeE.amplitude_barOdd`) is a consistency check the concrete `P` must satisfy — noted,
not proved (no concrete `σ` on `P` yet). Lean `QOU/QBeta/BirkhoffAmplitudeWellPosed.lean` sorry-free
(lean-direct exit 0, no native_decide/trivial-true/axiom). Nothing fitted, nothing wired;
`r*`/`μ₃`/`c₃`/AME/CODATA/`q₀` never inverted; `q₀`-derivation not routed through. Audit:
[`docs/audits/2026-08-08-birkhoff-amplitude-e-well-posedness.md`](../audits/2026-08-08-birkhoff-amplitude-e-well-posedness.md).

## 2026-08-08 · A=3 amplitude ROUTE 2-c-BIRKHOFF — CONSTRUCTING the C1 cross-ratio: `E = χ(P)` (frame-free), the WALL is its VALUE; scope-(a), converges with the well-posedness sibling

**Branch** `claude/deltalambda-birkhoff-amplitude-e-2026-08-08` · **bean `qou-wiub`** ·
**Lean** `QOU/QBeta/BirkhoffAmplitudeE.lean` (sorry-free, lean-direct exit 0, axioms
`[propext, Classical.choice, Quot.sound]` — no `sorryAx`; 0 native_decide / 0 trivial-true /
0 axiom).

Assigned the **connection-matrix CONSTRUCTION** angle on the open keystone `E` (the single
free DOF ROUTE 2-c isolated; LOCAL Stokes walled #4811, DT-index bar-excluded #4810 — both
hand `E` to the GLOBAL `0↔∞` Birkhoff matrix `P = (X^{(∞)})⁻¹ X^{(0)}` of C1). Built `P`'s
structural content from the q-character infra (`QCharacter.IsQChar`) and located the precise
next wall.

**Convergence (not contradiction) with the well-posedness sibling
`BirkhoffAmplitudeWellPosed.lean`.** Mid-task the sibling proved (sorry-free) that `E`, being
frame-free (`A3AntiSelfAdjointLift.amplitude_injective`), **must be the gauge-invariant
CROSS-RATIO `χ(P) = P₀₁P₁₀/(P₀₀P₁₁)`, not a single matrix entry** (a bare entry moves under
the elliptic diagonal normalization gauge → ill-posed; 4 entries − 3 gauge dims = 1
invariant). This file **independently confirms** it — `crossRatio_gauge_invariant` (the
cross-ratio is gauge-invariant) + `entry_gauge_movable` (a bare entry is movable to any
nonzero value under a χ-preserving gauge) + `distinct_entries_share_crossRatio` — and takes
the construction angle on the corrected object.

**Genuinely new construction result — `crossRatio_conn_qInvariant`.** Straight from
`IsQChar`: the cross-ratio of the four connection entries is σ_q-invariant (elliptic)
**because the exponent multipliers cancel exactly** — each entry `P_{ij}` has multiplier
`c_{0,j}/c_{∞,i}`, and `(c₀₁/c∞₀)(c₀₀/c∞₁) = (c₀₀/c∞₀)(c₀₁/c∞₁)` (`connMultiplier_balance`).
This *constructs* the frame-free object's ellipticity from the q-character algebra — the
abstract reason `χ(P)` is theta-valued and `C1ConnectionPoles.connRatio_elliptic` holds —
and singles out `χ(P)` (not any entry) as the well-posed `E`-carrier. Bridge to A3
(`lift_injective_in_crossRatio` + `lift_reachable_by_crossRatio`): since `E = χ(P)` is
frame-free and `E ↦ factor` is a bijection, **deriving `χ(P)` DOES pin the A=3 lift** — no
gauge ambiguity remains; only the cross-ratio's *value* is open.

**Net verdict — WALL (scope-(a)), sharpened + well-posed.** The wall is no longer "which
functional of `P` is `E`" (answered: the cross-ratio) but the **VALUE of `χ(P)`**: its
closed form is the open bean `qou-wgnx` (`χ = closed form` proved-elliptic but unproved),
and its `∞`-input is C1's slope-`½` wild normalization (open bean `qou-vkg5`; the 0-side
Fuchsian exponent IS determined, `C1FuchsianExponents`). Open successor recorded as §3b
dependent class `BirkhoffCrossRatioSuppliesAmplitude` (content-bearing: 0-exponent
determined + ∞-exponent open + `E = χ(P)` + bar-odd consistency + lift; **NO instance**),
correcting `StokesAmplitudeE.GlobalBirkhoffSuppliesAmplitude` (whose `multislope` condition
is C1-inapplicable — C1's ∞ is single-slope, `rszIsoformalDim = 0`) and aligned with the
sibling's `AmplitudeIsGaugeInvariantCrossRatio`. Nothing fitted, nothing wired;
`r*`/`μ₃`/`c₃`/AME/`q₀` never inverted; `q₀`-derivation not routed through. Audit
[`docs/audits/2026-08-08-birkhoff-amplitude-e-crossratio-construction.md`](../audits/2026-08-08-birkhoff-amplitude-e-crossratio-construction.md).

### 2026-08-08 — χ(P)|q₀ EVALUATED vs r* — the cross-ratio is a UNIT PHASE, not 1.585 (scope-(a))

The decisive check the E=χ(P) rows above left open: **evaluate the closed-form χ(P) at the
substrate and compare to r* = μ₃/c₃ ≈ 1.585.** Done (proton q₀, no tuning; witness
[`c1-chi-magnitude-vs-r-star.witness.json`](../../computations/qbeta/c1-chi-magnitude-vs-r-star.witness.json),
audit [`2026-08-08-chi-p-magnitude-vs-r-star-evaluation.md`](../audits/2026-08-08-chi-p-magnitude-vs-r-star-evaluation.md)).

**Result.** χ(P) on the real axis is a **pure unit-modulus phase**: `|χ| = 1` EXACTLY (dev
0.0; closed form = direct connection matrix to 1e-5), a `z`-dependent elliptic function
(`arg χ = −0.488/−1.921/+1.310/+3.052` at `z = 0.30/0.45/0.60/0.75`); `|α| = q^{3/4} =
1.0814…` exactly. `r* ≈ 1.585` is a real magnitude `> 1`. A unit phase cannot equal it:
`||χ|−r*| = 0.585` uniformly. **So the naive identity `χ(P) = r*` does NOT close the A=3
magnitude** — same pattern as every other trace/cross-ratio object here (modulus 1, r*≠1).

**Sharpening, not refutation.** This does NOT refute `E = χ(P)` (the gauge-invariance
argument never claimed χ(P) = the *magnitude*). It relocates the wall: the A=3 lift is
*affine* in `E` (`factor_sa − (B·D⁻¹/A)·E`, `factor_sa ≤ 1`), so `r*` is a real functional
of `E`, not `E` itself. The cross-ratio's numeric VALUE is **no longer open** (it is a
computed unit phase); what remains open is the phase→real-amplitude→lift bridge — including
a genuine type tension (`A3AntiSelfAdjointLift` wants a real `E`; χ(P) is a unit-modulus
complex phase). Nothing fitted, nothing wired; `r*`/`μ₃`/`c₃` never inverted;
`q₀`-derivation not routed through. Bean `qou-wgnx`/`qou-wiub`.
