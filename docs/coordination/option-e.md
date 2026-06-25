# Δ_λ closure (Option-E) — master ledger

> Single source of truth for the **Δ_λ closure / per-isotope binding**
> goal. Per AGENTS.md L2 Subgoal-1: this is the closure path
> ("per-isotope Borromean-tower extension + operator-valued branching
> combiner") that unlocks the 100× targets above the CAL-2 floor.

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
    sorry-free: `PartitionOf5.deltaSign_mixed` (both ±1 occur) +
    `PartitionOf5.binding_magnitude_eq_dim` (|Δ_λ|² = dim²) in
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
| 2026-06-17 | Claude / `...keystone-lean-mckay-e8-anchors` (PR #2424) | Lean-prove the McKay 2I↔E₈ + A₅-branching anchors | **LANDED (sorry-free).** `binaryIcosahedralIrrepDims` (affine E₈ marks) with Σdim²=120, Σmarks=h(E₈)=30, \|2I\|=4·h, dimE₈=248=8·31; `so3_to_a5_dim_splits`; `s5_to_a5_electron_block_splits` (6=3+3, T₁⊕T₂). Pins the spacetime-face arithmetic behind the chirality split. Verified core-only (exit 0). |
| 2026-06-17 | Claude / `...deuteron-closure-overclaim-fix` | Re-verify the deuteron "closure" claim (row 2026-06-16 above asserted "+0.91% via E₀×q⁻¹ is the correct closure") | **CORRECTION — the deuteron is NOT closed.** No compute reproduces 2.24/+0.91%: stated E₀×q⁻¹ (E₀=4.186)=3.771 (+69.5%); Σ-formula=0.380 (−82.9%); the apparent closure was Σ×**fitted** C_knot=5.852 (the compute itself labels it fitted, gate open). Best parameter-free = interface-knot+T3 = 1.526 (−31%). The 2026-06-16 "Reading" + Status row were themselves wrong (kept E₀×q⁻¹ as "correct closure"); both fixed. No light nucleus honestly closed (Δ_λ blocked, main `1f08f61a`). Audit `2026-06-17-deuteron-closure-overclaim-corrected.md`. |

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
