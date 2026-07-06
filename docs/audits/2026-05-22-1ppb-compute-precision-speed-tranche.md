# 1 ppb compute-precision + speed-optimization tranche — 2026-05-22

> **Scope.** User-requested 5-item tranche post-PR #879 merge:
> (1) block-graph hygiene, (2) Bring-Bloch tier-search status,
> (3) (Z+N) extension audit, (4) L1 dashboard scan, (5) PR #761
> follow-up — plus (6) compute speed/bottleneck analysis. Reframed
> as **L1 (compute) precision, not L2 (experimental)** per owner
> direction. Companion to existing
> [`docs/audits/2026-05-20-compute-wiring-audit-pr-852.md`](2026-05-20-compute-wiring-audit-pr-852.md).

## TL;DR

| Item | Outcome |
|---|---|
| L1 1 ppb gate | **GREEN.** `onepb-status-dashboard.witness.json` reports max delta 0.0 across all 3 assertions (LP duality gap, Markov-trace cross-check, witness inventory). |
| Block-graph hygiene | **Landed (commit `558056b25`).** 15 `.ts` files migrated `uses[]`/`interprets:` from `prop:mass-endomorphism-tower` (SUPERSEDED) → `prop:mass-tower-operator-valued`. Validation clean. |
| Bring-Bloch λ_scale | **6-tier consistent negative.** All 52 hyperbolic-knot Bloch-Wigner volumes searched (Tier 0..5, maxcoeff 10^5–10^8, PSLQ at 80–100 dps); zero relations. Decisive structural signal. CAL-4 in `λ_scale` remains open. |
| (Z+N) extension | **H_12 A-operator extraction is the next concrete blocker** (2–3 day compute task; unblocks 14 of 20 SUPERSEDED-importer scripts). Rank-deficiency risk noted; mitigation via `markov_peel.tr_M_atomic(2,2)` direct call. |
| PR #761 status | **887 commits behind main.** Past prepare-merge §8c stop threshold; owner attention required. |
| Speed/bottleneck | **Rust LR convention adapter (PR #829) is the highest-ROI unwired speedup**: ~500× at ⁴He H_12, ~10⁶× at ¹⁰B. Per cheat-sheet §5 Migration Backlog #3: not yet wired in `atomic_tr_m_helium4.py`, `atomic_tr_m_mpfr_50dps.py`, +6 mass scripts. |

## 1. Block-graph hygiene — landed

Commit [`558056b25`](https://github.com/litlfred/qou/blob/claude/1ppb-compute-precision-speed-2026-05-22/) migrates 15 `.ts` files. The `mass-endomorphism-tower` block stays in place (it carries the SUPERSEDED banner pointing to `mass-tower-operator-valued`), so in-prose `.md` links and Lean `Ref:` lines that intentionally cite the SUPERSEDED block continue to resolve. Only the structural dependency graph (`uses[]`, `interprets:`) is updated.

Files migrated:

| File | Field |
|---|---|
| `alpha-cosh-h-z-step-correction.ts` | `uses[]` |
| `alpha-k-categorical-closure.ts` | `uses[]` |
| `block-multiplicativity-v-free.ts` | `uses[]` |
| `interface-knot-markov-z.ts` | `uses[]` |
| `mass-endomorphism-jet-tower.ts` | `uses[]` + `interprets:` |
| `per-braid-mass-tower.ts` | `uses[]` |
| `phi-q-resums-trace-series.ts` | `uses[]` + `interprets:` |
| `phi-q-tower-algebraic-stratification.ts` | `uses[]` |
| `phi-q-tower-jsj-bridge.ts` | `uses[]` |
| `quantum-dilogarithm-disambiguation.ts` | `uses[]` |
| `six-term-per-derivation-weights.ts` | `uses[]` |
| `stable-atom.ts` | `uses[]` |
| `bw-empirical-misses.ts` | `uses[]` |
| `three-calibration-discipline.ts` | `uses[]` |
| `tower-binding-energy.ts` | `uses[]` |

`bun run validate quantum-observable-universe` passes (1 pre-existing warning unrelated to this change, in `lr-tensor-character-bridge` cross-refs).

## 2. Bring-Bloch tier-search — 6-tier negative is structural

Per [`prop:lambda-scale-bring-bloch-identity`](../../content/quantum-observable-universe/braids-and-knots/lambda-scale-bring-bloch-identity.md), `λ_scale = (1/8G) · D(Σ_i n_i^(p) [Z_K_i])` for some integer multiset `n_i^(p)` of hyperbolic-knot Bring-decomposition classes. The five tier scripts search for the multiset via PSLQ against the CODATA target `λ_p = 2.4599527843613...`:

| Tier | Basis | Knots added | PSLQ result |
|---|---:|---|---|
| 0 | 8 | Atlas-named {4_1, 5_2, 6_1, 6_2, 6_3, 7_4, B_3, L_6a4} + whitehead | NULL |
| 1 | 11 | Birman–Hilden 3-braid hyperbolic (≤ 8 crossings) | NULL |
| 2 | 16 | + bridge-3 hyperbolic (4-braid, ≤ 8 crossings) | NULL |
| 3 | 33 | + prime 9-crossing hyperbolic (17 knots) | NULL |
| 4 | 40 | + 10-crossing primes (vol range 6.8–17.6) | NULL |
| 5 | 52 | + 11-crossing primes (vol range 7.7–20.6, bracketing target 18.026) | NULL |

All at PSLQ tolerance 1e-10 to 1e-15, maxcoeff 10^5–10^8. The six-tier consistent negative is **structurally informative**: the proton's Bring-decomposition is not a ℤ-linear combination of prime hyperbolic-knot volumes ≤ 11 crossings.

**Forward options** (per `bring_bloch_tier5_search_m_p.py:200–208` and `prop:lambda-scale-bring-bloch-identity §Open work`):

1. **Tier 6+** — 12-crossing primes, composite/satellite knots. Cost grows combinatorially; no convergence guarantee.
2. **Direct knot-operator-LP/SDP derivation** of `n_i^(p)` from the canonical proton Hecke element `𝓑_p` (replaces empirical PSLQ search).
3. **q-dilog tower direct parametrisation** — bypass hyperbolic volumes; derive `λ_scale` from the bar-anti-symmetric `Li_2^q` tower at the substrate point. Listed as §7 #4 open frontier in [`2026-05-20-compute-wiring-audit-pr-852.md`](2026-05-20-compute-wiring-audit-pr-852.md).

**Discipline note.** The paper's `prop:lambda-scale-bring-bloch-identity` states the identity sorry-free conditional on the existence of the integer multiset `n_i^(p)`. With six tiers exhausted, the conditional is currently empty — `λ_scale` remains a hardcoded literal `LAMBDA_PROTON_DOC = 2.4599527869` in [`m_p_borromean_verification_50dps.py:100`](../../computations/m_p_borromean_verification_50dps.py). The "CAL-4 in disguise" status documented in [`docs/audits/2026-05-18-210x-scale-gap-root-cause-v2.md`](2026-05-18-210x-scale-gap-root-cause-v2.md) (PR #879, merged) **stands**.

## 3. (Z+N) extension audit — H_12 is the gate

`mass_tower_operator_valued.py` currently verifies the operator-trace identity only at **A=2 (deuteron, H_6)**. Extension to A=4 (⁴He, H_12) is the next concrete task because it unblocks 14 of the 20 SUPERSEDED-importer scripts. Concrete blocker per [`sublemma_2_1_h12_helium_4_framework.py`](../../computations/sublemma_2_1_h12_helium_4_framework.py):

The 3-interface ⁴He formula needs three extracted A-operator matrices:

| Operator | Source | Status |
|---|---|---|
| `A^η_{μν}(I_pp)` at H_6 | `sublemma-2-1-A-operator-extract.witness.json` | ✅ on disk |
| `A^ξ_{ην'}(I_pn)` at H_9 | `sublemma-2-1-A-operator-extract-h9-nn.witness.json` | ✅ on disk |
| `A^λ_{ξν''}(I_nn)` at H_12 | — | **❌ MISSING** |

H_12 requires 77 partitions with max dimension 462 (`λ=[4,4,4]`). Estimated compute: 30–60 min for the Hoefsmit build at MPFR 50 dps; 24–48 h parallelisable for the bilinear extraction over 3,500+ test words per λ.

**Rank-deficiency risk.** Per [`docs/audits/2026-05-18-recursive-rho-xi-blocked-by-underdetermined-extracts.md`](2026-05-18-recursive-rho-xi-blocked-by-underdetermined-extracts.md), H_9 extraction showed 42% error on tritium due to rank-deficient bilinear systems. The H_12 scale-up may amplify this; the fix is to lattice-span the test-word basis rather than restrict to the canonical-form basis.

**Migration tiers per the 20 SUPERSEDED-importer scripts:**

| Tier | Effort | Scripts |
|---|---|---|
| **A. Today** (2-factor only) | 4–8 hrs | Single-nucleon refactors of any script that only needs χ_λ for A=1 (no interface): `murnaghan_nakayama.py` and similar. |
| **B. After H_12 extract** | 2–3 days compute + 1–2 days validation | `build_proton_mass_50dps_chain.py`, `mass_formula_6term.py`, `mass_at_3A_proper.py`, `paper_six_term_isotope_sweep.py`, `atom_level_wedderburn_tower.py` (5 scripts). |
| **C. General (Z+N)** | 1–2 weeks R&D | Extend iterated 3-interface formula to k-factor; handle rank-deficiency via lattice-spanning. Remaining ~9 scripts. |

**Mitigation if rank-deficiency blocks (B).** Fall back to `markov_peel.tr_M_atomic(2,2)` direct call inside the affected scripts; loses structural transparency but ships migration capability immediately.

## 4. L1 dashboard — GREEN

[`computations/onepb-status-dashboard.witness.json`](../../computations/onepb-status-dashboard.witness.json) (computed 2026-05-20):

| assertion | computed | expected | tolerance | passed |
|---|---:|---:|---:|:---:|
| `all_witnesses_present` | 10 | 10 | 0 | ✅ |
| `lp_max_duality_gap` | 0 | 0.0 | 1e-09 | ✅ |
| `markov_trace_max_rel_delta` | 0.0 | 0.0 | 1e-09 | ✅ |

L1 1-ppb cross-method agreement is **trivially met** per AGENTS.md §Precision goals: the production stack runs at 50 dps compute / 40 dps output (`_precision.py`). The dashboard confirms this empirically across all 10 indexed witnesses, with zero LP duality gap and zero relative delta between the Hoefsmit and `markov_peel` paths for the Markov trace cross-check.

**No L1 regressions to chase.** The next compute-precision work is structural (closing CAL-4) and speed (Rust wiring), not raw precision.

## 5. PR #761 — owner attention required

PR #761 (combined 10-PR consolidation, 21 commits, 2022 additions, 11 files) is **887 commits behind main** as of this audit. Per [`.claude/commands/prepare-merge.md §8c`](../../.claude/commands/prepare-merge.md) decision matrix:

> **Delta > 10** → stop: announce to the user. Long-discharge sessions risk substantial divergence; offer prepare-merge rebase OR continue + flag.

887 is far beyond the threshold. The Rust files (`geck_pfeiffer.rs`, `laurent_poly_q.rs`, `wenzl_lr.rs`) likely conflict with subsequent landed work. The 5 audit `.md` docs likely land cleanly.

**Recommendation.** Owner decides between (a) cherry-pick the still-relevant subset onto a fresh branch, (b) abandon the consolidation and re-land each piece individually as needed, or (c) attempt the full 887-commit rebase (risky). Do not attempt option (c) without owner explicit go-ahead.

## 6. Speed/bottleneck queue — 10 opportunities, ROI-ranked 5

Per direct scan of production scripts, the 10 largest opportunities (with current per-script Rust-wiring status):

| Script | Status | Bottleneck | Proposed fix |
|---|---|---|---|
| `atomic_tr_m_helium4.py:166` | Python-only (mpmath, slowest) | `markov_trace_recursive` on H_12 (44–47 crossings, 480s timeout) | Wire Rust hecke-engine LR convention adapter — ~500× at H_12 |
| `atomic_tr_m_mpfr_50dps.py:106` | Python with `sympy.simplify` (slowest tier) | Wenzl-bridge p(12)=77 partitions × 47 crossings × 50dps; ~2×10¹³ ops/partition | Rust rayon parallel + block-sparse MPFR; currently intractable at H_12 |
| `atomic_chirality_residue.py:101` | Rust-wired via `pyhecke_native` ✅ | Python fallback when `_RUST_AVAILABLE=False`; multiprocessing pool overhead | Ensure Rust kernel always available — already ~50× faster at n ≥ 9 |
| `atom_level_wedderburn_tower.py:58–59` | Python-only (mpmath) | `build_seminormal_matrices_cached` initialised per-partition; BlockCache cold | Pre-warm BlockCache at module init |
| `binding_canonical.py:186` | Python with sympy (mitigated) | `sympy.simplify` on 5–12 k-op trace (skipped with `simplify=False` per the line comment) | Already skipped; move reduction step to Rust symbolic backend for next win |
| `binding_depth_stratified.py:125` | Python-only (mpmath) | `markov_trace_3A` over full p(3A) sum; partition loop per depth stratum | Vectorise partition loop; Rust `chi_lambda_braid` batch evaluation |
| `mass_at_3A_proper.py:58–200` | Python-only (mpmath) | `_cached_seminormal` disk I/O + NPZ deserialize per shape; pickle RCE-risk patch (P14) | Memory-map precompiled seminormal; eliminate per-shape disk latency |
| `mass_formula_6term.py:94–150` | Python-only (mpmath) | `term_23_brane_tower` over generator pairs; Φ_q convergence near pole (|V̂_i| ≈ 0.95) | Vectorise pair-sum; Φ_q LUT for [0.9, 1.05) |
| `build_proton_mass_50dps_chain.py:101–113` | Python with mpmath | `LAMBDA_SCALE_SUBSTRATE_FORM` (5/2 − h²·G) recomputed per call | Module-level cached constant; one-time at import |
| `binding_depth_stratified_rust.py:95–135` | Conditional Rust | Reads `atom-chi-rust-*.witness.json`; missing files trigger manual recompute | Auto-generate missing Rust witnesses on first import |

### Priority queue (ROI-ranked, top 5)

| Rank | Speedup | Script | Fix |
|---|---|---|---|
| 1 | ~500–1000× | `atomic_tr_m_helium4.py:166` | Wire `direct_h12_recursion` to Rust hecke-engine LR convention adapter; eliminates 480 s timeout budget. |
| 2 | ~100–1000× | `atomic_tr_m_mpfr_50dps.py:106` | Parallelise Wenzl-bridge partition sum via Rust rayon + block-sparse MPFR; unblocks ⁴He routine sweep. |
| 3 | ~10–50× | `mass_at_3A_proper.py:166–200` | Memory-map precompiled seminormal matrices; eliminate per-shape disk I/O in `_cached_seminormal`. |
| 4 | ~5–10× | `binding_depth_stratified.py:103–126` | Vectorise partition loop over depths; use Rust `chi_lambda_braid` batch eval. |
| 5 | ~2–5× | `mass_formula_6term.py:99–150` | Precompute Φ_q LUT for near-pole domain; skip adaptive convergence checks in loop body. |

**Top recommendation: action #1** is the highest-ROI single change. The Rust kernel is already on `main`; only the Python wrapper in `atomic_tr_m_helium4.py:166` needs to import it. Expected: ⁴He compute drops from minutes to fractional-second; ⁶Li and beyond become tractable for routine sweeps.

**Companion guidance** from existing audit infra:
- `compute-audit-scan.witness.json` queue items track `sympy.simplify → LaurentQ` migration (mechanical; partial).
- AGENTS.md `compute-author` mandates MPFR ≥ 50 dps; float64 should be near-zero in production.
- Cheat-sheet §5 Migration Backlog #3+#4 (Rust LR adapter wire-up + closed-form `tr_M(𝓑_K)` refactor) overlap with priorities 1–4 above.

## Action queue (priority order)

1. **Land action #1** (Rust LR convention adapter wiring) — biggest speed win.
2. **Land action #2** (closed-form `tr_M(𝓑_K)`) — eliminates O(N×partition) recomputes.
3. **Owner decision on PR #761** (cherry-pick vs abandon vs full-rebase).
4. **H_12 A-operator extraction** — unblocks 14 of 20 SUPERSEDED scripts; gating dependency for Migration Backlog #2.
5. **q-dilog tower direct parametrisation of λ_scale** — alternative path after 6-tier Bring-Bloch negative (open frontier #4).

Items 1–2 are mechanical and additive (no math content changes). Items 3–5 require either owner decision or research-level work.

## Cross-references

- [`docs/audits/2026-05-18-210x-scale-gap-root-cause-v2.md`](2026-05-18-210x-scale-gap-root-cause-v2.md) — PR #879 (merged) — identifies `λ_scale` as CAL-4 in disguise.
- [`docs/audits/2026-05-20-compute-wiring-audit-pr-852.md`](2026-05-20-compute-wiring-audit-pr-852.md) — 72-hr compute-wiring scan; this audit's companion.
- [`docs/canonical-derivation-cheat-sheet.md §5`](../canonical-derivation-cheat-sheet.md) — Migration backlog (master).
- [`computations/onepb-status-dashboard.witness.json`](../../computations/onepb-status-dashboard.witness.json) — L1 dashboard.
- [`computations/sublemma_2_1_h12_helium_4_framework.py`](../../computations/sublemma_2_1_h12_helium_4_framework.py) — (Z+N) extension framework.
- [`computations/bring_bloch_tier{1..5}_search_m_p.py`](../../computations/) — Bring-Bloch tier searches.
- [`docs/audits/2026-05-18-recursive-rho-xi-blocked-by-underdetermined-extracts.md`](2026-05-18-recursive-rho-xi-blocked-by-underdetermined-extracts.md) — H_9 rank-deficiency precedent for H_12 risk.

## Provenance

This audit consolidates findings from:
- Sub-agent A (Bring-Bloch tier survey — all 6 tiers NULL)
- Sub-agent B ((Z+N) extension audit — H_12 extraction concrete blocker)
- Direct read of L1 dashboard witness JSON
- Mechanical block-graph migration script
- Existing `docs/audits/2026-05-20-compute-wiring-audit-pr-852.md` for §5 / §7 cross-checks
