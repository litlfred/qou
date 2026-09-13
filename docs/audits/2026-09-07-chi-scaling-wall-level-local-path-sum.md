# The χ^λ scaling wall: the Rust GP minimal-length reduction is the cost, and a dim-free seminormal path-sum removes it

**Bean:** `qou-s7ld` (the coordinator's `qou-zunl` does not exist on `main`; this is its carrier).
**Related:** `qou-d9wf` (cost model refuted, on #7083), `qou-sv7h` (binding compute cannot scale), `qou-92u9` / `qou-hu1f` (borromean intra-nucleon ordering ruling, 2026-09-05).
**Producer:** [`computations/chi_path_sum_seminormal.py`](../../computations/chi_path_sum_seminormal.py) (new) wired into [`computations/chi_via_rust_lossless.py`](../../computations/chi_via_rust_lossless.py) as the default backend.
**Owner ask (verbatim):** *"Investigate why slow — can we optimize / get rid of bottlenecks / use symmetry / use symbolic forms?"*

---

## 1. Claim

1. **The wall is not dim V_λ and not the T_w-basis expansion; it is `reduce_basis_to_minimal_length_complete`** — the Hecke conjugation of every basis element toward a minimal-length conjugacy-class representative inside `pyhecke_native.chi_q_via_gp` (`tools/hecke-engine/src/geck_pfeiffer.rs`).
2. **A symmetry of the atom word removes the wall entirely.** `atom_braid_word_3A` touches every seminormal level in exactly one contiguous factor, so `χ^λ(T_β) = Σ_{T∈SYT(λ)} Π_j ⟨T|F_j|T⟩` — a transfer-matrix contraction over shapes that never sees dim V_λ. All 176 partitions of ⁵Li in **2.5 s**; all 385 of ⁶Li in **8.5 s**; the Rust route took **5.6 s for a single λ at n = 12** and did not finish 40 of ⁵Li's 176 partitions in 3 h 35 m.
3. **The ⁵Li/⁶Li caches are regenerated on the borromean word.** So are D, T and ³He — which were, like ⁵Li/⁶Li, still on the pre-2026-09-05 *grouped* word while ⁴He alone was borromean (§4).

## 2. Evidence

### 2.1 Where the time goes (measured 2026-09-07, this container, `pyhecke_native` system wheel)

Support of the T_w-basis expansion of the atom word, counted by simulating `braid_to_hecke` on permutation sets only (`scratchpad/support_count.py`):

| n | A | word length | support of T_β | 6^A | n! |
|---|---|---|---|---|---|
| 6 | 2 | 23 | **36** | 36 | 7.2e2 |
| 9 | 3 | 35 | **216** | 216 | 3.6e5 |
| 12 | 4 | 47 | **1296** | 1296 | 4.8e8 |
| 15 | 5 | 59 | **7776** | 7776 | 1.3e12 |
| 18 | 6 | 71 | **46656** | 46656 | 6.4e15 |

The support is exactly 6^A: each nucleon block is a word in the parabolic `H_3` on its own three strands (6 basis elements), joined by one bond letter, and the product of reduced words across blocks stays reduced. So the hypothesis "cost = number of basis terms → n!" is **refuted**: the expansion is tiny.

Per-call timing of the three Rust entry points on the same word (`/tmp/chi-scaling-4-timing.log`, f64 kernels so only the *ratio* is load-bearing):

| n | λ | expansion + Hoefsmit per T_w (no reduction) | direct seminormal | `chi_q_via_gp` (expansion + minimal-length reduction + q-MN) |
|---|---|---|---|---|
| 6 | [6] | 1.0 ms | <0.1 ms | 1.5 ms |
| 9 | [9] | 7.7 ms | <0.1 ms | 30.8 ms |
| 12 | [12] | 62 ms | <0.1 ms | **7385 ms** |
| 12 | [11,1] | 88 ms | 2.7 ms | **7633 ms** |

Same expansion, same word: the route *without* the reduction is 62 ms, the route *with* it is 7.4 s. > 99 % of `chi_q_via_gp`'s cost at n = 12 is the reduction. Mechanism (read from the source, not instrumented): `hecke_conjugate_by_s` produces `T_{sws}` plus lower terms, which leave the 6^A chain and spread toward S_n; each outer iteration rescans `current` from the start (`find_map` with `perm_cycle_type` + `length()`, O(|support|·n²)); stalled elements trigger a BFS over the equal-length cyclic-shift class capped at 10⁶ nodes.

### 2.2 The identity, and its cross-checks

In Young's seminormal basis `ρ(σ_i)` maps a tableau `T` into span{`T`, `s_i T`}; `s_i T` differs from `T` only at level `i` of the shape path `∅ ⊂ λ^{(1)} ⊂ … ⊂ λ`. The atom word is `F_1 F_2 ⋯ F_m` with `F_j` supported on pairwise-disjoint level sets ({3k+1,3k+2} for nucleon k, {3k+3} for the bond). For such a product every intermediate tableau in `⟨T|F_1⋯F_m|T⟩` is forced back to `T` — no later factor can undo a change at a level it does not touch — so the diagonal entry factorises, and the trace is a sum over SYT(λ) of products of *local* diagonal entries. Each local entry depends only on the boxes of the ≤ 3 entries the factor touches (contents → Hoefsmit axial distances; row/column adjacency → which swaps are standard), so the SYT sum is a DP over (shape, last box) with orbits of size ≤ 6. Cost is polynomial in n; dim V_λ never appears.

`python3 computations/chi_path_sum_seminormal.py` (`/tmp/chi-scaling-6-selftest.log`), all `mpmath` at 70 dps, q from `Q_50_DIGIT_STR` (proton pin):

| check | result |
|---|---|
| all 11 λ ⊢ 6 vs Rust `chi_lambdas_braid_mpfr` (independent seminormal kernel) | worst rel **1.2e-49** |
| all 30 λ ⊢ 9 vs Rust `chi_lambdas_braid_mpfr` | worst rel **6.9e-50** |
| same, with a mixed σ / σ⁻¹ / averaged (shift h/2) word | worst rel **9.1e-50** |
| all 77 λ ⊢ 12 vs the committed ⁴He borromean cache | worst rel **4.7e-50** |
| D / T / ³He / ⁵Li / ⁶Li caches on `main` (grouped word) | 1.1e-49 / 3.1e-50 / 3.1e-50 / 3.1e-42 / 2.0e-41 |
| `χ_[15] = q^59`, `χ_[18] = q^71` (trivial rep = writhe) | pass |
| first four partitions of D and T vs `chi_q_via_gp` on the current word | agree to 20 shown digits |

The 1e-42 / 1e-41 on the Li caches are the recorded 50-dps strings under cancellation in χ of magnitude ~10²–10³; the D/T/³He/⁴He agreement is at the floor of the recorded precision.

### 2.3 New-route timing, all partitions, this container

| atom | n | p(n) | path-sum (all λ) | Rust `chi_q_via_gp` (measured) |
|---|---|---|---|---|
| D | 6 | 11 | 17 ms | 1.2 ms/λ |
| T / ³He | 9 | 30 | 131 ms | 26 ms/λ |
| ⁴He | 12 | 77 | 0.66 s | 5.6 s/λ → ~430 s (#7083 measured 800 s batched) |
| ⁵Li | 15 | 176 | **2.5 s** | > 5.4 min/λ (40/176 not finished in 3 h 35 m) |
| ⁶Li | 18 | 385 | **8.5 s** | not attempted; extrapolation ~months |

## 3. The assessed alternatives (owner's list)

| route | verdict | cost model / measurement |
|---|---|---|
| (a) direct seminormal product along the word | works but is O(L·dim²): Σ_λ dim² = n! (1.3e12 at n=15) — a wall of the same height, just reached later. The Rust `chi_lambda_braid_mpfr` is this route. **Superseded by the path-sum**, which is the same seminormal arithmetic re-bracketed so the dim-sum collapses. |
| (b) bar-invariance / λ ↔ λ' halving | not needed once (2) is in place; the sign-only word is not bar-invariant anyway (all letters +σ). Not implemented. |
| (c) Murnaghan–Nakayama / GP class-representative route | **this is `chi_q_via_gp`, and its reduction step is the wall** (§2.1). The character table is cheap; getting T_β into class representatives at q ≠ 1 is not. |
| (d) exact Laurent polynomial once, evaluate later | `chi_q_via_gp` already returns the exact Laurent polynomial; that is not where the time is. The path-sum could run over ℚ(q) but there is no consumer asking for it; at 70 dps the mpf route is the cheaper exact-enough form. Not implemented. |
| (e) re-base Li consumers on the per-bond closed forms | The four consumers (`delta_lambda_empirical_tabulation.py`, `deltalambda/carrier_table_convention_d_rederivation.py`, `deltalambda/li6_h18_amplification_discriminator_probe.py`, `deltalambda/carrier_saturation_mechanism_probe.py`) read **per-λ χ**, not tr_M, so the bond factorisation of the Markov trace does not replace the cache. Moot now that the cache costs seconds. |

## 4. Second finding: five of six matrix-m caches on `main` were on the superseded word

`mass_at_3A_proper.atom_braid_word_3A(..., intra_order="borromean")` is the default since the 2026-09-05 ruling; `intra_order="grouped"` reproduces the earlier word. Measured (`scratchpad/cache_grouped.py`), worst relative disagreement of each committed cache against the path-sum on each word:

| cache | vs borromean | vs grouped | verdict |
|---|---|---|---|
| `chi-deuteron-h6-…-matrix-m` | 1.28 | **1.1e-49** | grouped (stale) |
| `chi-tritium-h9-…` | 2.14 | **3.1e-50** | grouped (stale) |
| `chi-helium-3-h9-…` | 2.14 | **3.1e-50** | grouped (stale) |
| `chi-helium-4-h12-…` | **4.7e-50** | 125 | borromean (#7083 regenerated it) |
| `chi-lithium-5-h15-…` | 10.1 | **3.1e-42** | grouped (stale) |
| `chi-lithium-6-h18-…` | 7.21 | **2.0e-41** | grouped (stale) |

So the family straddled two words. This also explains the 69 s the ⁵Li cache recorded in August: on the grouped word every segment is a *single* generator (segment sizes `[1,1,1,…]`), so the T_w expansion is already minimal-length and the GP reduction has nothing to do; the borromean word interleaves two generators per block (`[2,1,2,1,…]`) and the reduction explodes. **The Rust route was never "20 ms/λ independent of dim" — it was fast on a word that happened not to exercise its expensive step.**

All five are regenerated here on the borromean word (D/T/³He as a separate, revertible commit). The absolute per-λ χ and tr_M move (D: `tr_M` 2.1754 → 1.4547); `mass_at_3A_proper`'s own docstring records that the *ratio* `tr_M(W_atom)/tr_M(W_free)` is ordering-invariant to ~1e-60, which is the quantity the binding consumers use. Consumers reading per-λ χ directly (the four named in §3(e)) see moved numbers and should be re-run; I did not re-run them (they are `deltalambda/` probes owned by other arcs).

## 5. Implications

- **⁵Li and ⁶Li are no longer long-compute.** The `chi-lithium-{5,6}` caches are regenerable in ~13 s total; the "days-to-weeks" in `qou-d9wf` and the "Li regeneration is infeasible" conclusion on #7083 are superseded — for this word family. The Rust `chi_q_via_gp` route remains available via `--backend gp` and remains correct; it is simply the wrong tool for a level-local word.
- **The identity is general, not atom-specific.** Any word whose generators partition into contiguous segments with disjoint generator sets is level-local; the module detects the condition (`segments_of`) and raises `NotLevelLocal` otherwise rather than returning a wrong number. It also handles σ⁻¹ and averaged / colour-weighted crossings (`σ − d·I`, per-position shifts), so the **binding (averaged) trace** can use the same route.
- **`qou-sv7h` is not closed by this.** That bean is about `hecke_core_legacy.unified_iterative_correction`'s O(dim³) matmuls in the *binding* producer, a different code path. The path-sum is a candidate replacement for its χ evaluations if that producer's words are level-local — not measured here.
- **Cost model in the producer docstring corrected** (it claimed 4 s for ⁵Li via Rust); `chi_via_rust_lossless.py` now records `chi_backend` and `braid_word_intra_order` in every witness so a future reader can tell a grouped-word cache from a borromean one without recomputing.

## 6. What is NOT established

- Whether `reduce_basis_to_minimal_length_complete` is O(n!) or merely super-polynomial on this word class: three timing points and an uninstrumented Rust. The *attribution* (reduction vs expansion) is measured; the complexity class is not.
- Whether the four `deltalambda/` consumers' conclusions move under the regenerated caches. Not re-run.
- Whether the binding producer's words (`unified_iterative_correction`) are level-local. Not checked.

## 7. Options (recommendation marked as judgement)

1. **Merge as is** — path-sum default, Li + D/T/³He caches on the borromean word. Cost: nothing further. Risk: the four `deltalambda/` consumers now read moved per-λ values; their own witnesses become stale until re-run. Commits to: the borromean word as the cache convention (already the owner's ruling).
2. **Merge the route, drop the D/T/³He regeneration commit** — keeps those three on the grouped word. Cost: one `git revert`. Risk: keeps the family straddling two words (⁴He and Li borromean, D/T/³He grouped), which is the straddle this bean was opened on.
3. **Do nothing** — Li caches stay grouped-word and inconsistent with ⁴He; the Rust cost model stays refuted with no replacement.

My judgement: **option 1**. The regeneration is derived from the corpus (the owner's ordering ruling plus the producer's own default), verified against an independent kernel at 1e-49, and the straddle is worse than the churn.

## 8. Verification run

- `python3 computations/chi_path_sum_seminormal.py` → `ALL PASSED` (`/tmp/chi-scaling-6-selftest.log`).
- `python3 -u computations/chi_via_rust_lossless.py --fresh 5Li 6Li D T 3He 2>&1 | tee /tmp/chi-scaling-8-regen.log` → 5 nuclides in 13.4 s, environment block matching the committed record (mpmath 1.4.1, clarabel present).
- `scripts/precision-gates.sh --changed` (`/tmp/chi-scaling-9-gates.log`): RED on pre-existing tree-wide baseline drift only; no line names any file changed here. The 10 tree-measuring audit witnesses it rewrote were reverted per its own instruction.
