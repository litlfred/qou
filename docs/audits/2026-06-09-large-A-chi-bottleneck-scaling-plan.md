# 2026-06-09 — Large-A χ bottleneck analysis + scaling plan (canonical-tier ruling: no f64)

> **Trigger**: PR #2080 task 3 (⁶Li/⁷Li cached chi witnesses). The
> ⁶Li run via `compute_atom_chi_rust.py` (f64 `chi_q_atomic`) was
> killed after 125 min once the cost model showed it could not
> finish (§2); the owner simultaneously issued the precision ruling
> recorded in §4. This doc is the thorough bottleneck analysis +
> the ranked optimization plan for large A, superseding the
> dimension table in
> [`2026-06-08-matrix-m-optimization-A-8-9-path.md`](2026-06-08-matrix-m-optimization-A-8-9-path.md)
> §1 (whose "max dim V_λ" column is wrong — see §3) while keeping
> its Tier-1/Tier-2 recommendation, which this analysis confirms.

## 1. Algorithm census — what each native χ API actually does

| API (pyhecke_native) | precision | algorithm (source) | per-λ cost | memory |
|---|---|---|---|---|
| `chi_q_atomic(_all_partitions)` | **f64** | per-basis-vector trace over the full Hoefsmit seminormal irrep: for each basis vector `e_i` (i=1..d_λ), apply all L word factors via sparse block application, read back entry i (`seminormal.rs:633-684`) | **O(L·d_λ²)** | O(d_λ) vector + O(d_λ·L) block data |
| `chi_lambda_all_partitions_{f64,mpfr}` | f64 / **MPFR** | same Hoefsmit-matrix class, routed per λ through `chi_lambda_braid(_mpfr)` (`wenzl_lr.rs:280-342`); signed-word input `sign∈{1,−1,0}`, 0 = averaged crossing (direct averaging, no 2^k expansion) | O(L·d_λ²) (×~50-150 per-op for MPFR) | O(d_λ) |
| `chi_q_via_gp` / `chi_lambdas_via_gp` | string-out (internals to verify) | Geck–Pfeiffer **word-level** reduction; the GP reduce depends only on (n, word), shared across all λ in the batched variant | ~independent of d_λ (word-combinatorial) | reduced-element coefficient tables |
| `chi_via_matrix_m_mpfr` | MPFR | μ_p block-restricted trace for parabolic-shaped braids (PR #2015 Tier-2 track) | block-bounded | small |
| `markov_peel.tr_M_atomic` (Python) | **symbolic, exact in q** | GS-reduce + Markov-axiom recursive ascent; produces tr_M directly (not per-λ χ) | word-level | reduced element |

## 2. Why the ⁶Li f64 run could never finish (and ⁴He could)

Per-basis-vector trace summed over **all** λ ⊢ n costs
`L · 2 · Σ_λ d_λ² = L · 2 · n!` sparse f64 ops:

- **n=12 (⁴He)**: 142·2·12! ≈ 1.4e11 → ~28 s observed ✓ (this is why
  the existing 77/77 cached witnesses exist at all).
- **n=18 (⁶Li)**: 71·2·18! ≈ **9.1e17** → at ~8e9 useful sparse
  flops/s (4 cores) ≈ **3.6 years**. The single max-dim partition
  (d=16,336,320) alone is ~55 days; the 6 GB RSS observed at kill
  time was its per-generator block data. Rayon parallelism over
  partitions does not help: the top-k λ dominate (§3) and each is a
  serial d² grind.
- **n=21 (⁷Li)**: d_max = 1.119e9 — one f64 *vector* for the biggest
  λ is 9 GB; Σd² = 21! ≈ 5e19. Dead on arrival for every
  matrix-based path, f64 or MPFR.

**Disposition**: the 125-min ⁶Li `chi_q_atomic` job was killed
(2 h sunk vs a years-long tail), and `compute_atom_chi_rust.py`
must be treated as **A ≤ 4 only** on its current algorithm.

## 3. Exact dimension / cost-concentration profile (hook-length formula)

Computed exactly via SYT hook lengths (this session; supersedes the
June-8 audit's "max dim V_λ" column, which understates d_max by
~4000× at n=18 — its 132/3375 figures appear to be 2-row/3-row
rectangle dims, not the true maxima):

| n | p(n) | d_max | Σd² = n! | k₅₀ | k₉₀ | k₉₉ | dense d_max² (f64) |
|---|---|---|---|---|---|---|---|
| 12 | 77 | 7,700 | 4.8e8 | 8 | 29 | 47 | 0.4 GB |
| 15 | 176 | 292,864 | 1.3e12 | 15 | 53 | 99 | 639 GB |
| 18 | 385 | 16,336,320 | 6.4e15 | 26 | 101 | 187 | 2.0 PB |
| 21 | 792 | 1.12e9 | 5.1e19 | 40 | 176 | 353 | 9.3 EB |
| 24 | 1575 | 1.17e11 | 6.2e23 | 69 | 299 | 630 | — |
| 27 | 3010 | 1.28e13 | 1.1e28 | 106 | 515 | 1078 | — |

`k_x` = number of largest-d λ needed to cover x% of Σd². Read:
**cost is extremely concentrated** (50% of all work in 26 of 385
partitions at n=18), and the concentration *worsens* with n — so
any per-λ matrix algorithm is owned by a handful of giant irreps,
and "skip the tail" saves little. The fix must change the per-λ
scaling, not trim the partition list.

## 4. Precision-tier ruling (owner directive, 2026-06-09 — STRICT)

> **NO float64 on the canonical path. Canonical = symbolic (exact
> in q) always; fall back to mpf/MPFR (≥ 50 dps) for speed. f64 is
> preview / cross-check tier only.**

This was already codified in `chi_lambda_all_partitions_mpfr`'s own
docstring ("this is the production path … the f64 variant exists
for speed-only use cases") but is **violated by the standing cached-χ
pipeline**: `compute_atom_chi_rust.py` (engine: `chi_q_atomic`,
f64) is the producer of the `atom-chi-rust-h{3A}` cached witnesses
consumed by `binding_depth_stratified_lr.py` — i.e. the canonical
default binding tower currently ingests f64 χ inputs.

Consequences (action items):

1. **A ≤ 4 cached-χ regeneration at MPFR** — n ≤ 12 is feasible on
   the existing `chi_lambda_all_partitions_mpfr` (T/³He instant;
   ⁴He ≈ tens of minutes at 50 dps). Follow-up tranche: regenerate
   D/T/³He/⁴He cached χ witnesses at MPFR tier + re-run the
   depth-stratified consumers; mark the f64 versions cross-check.
2. **Combiner gate-lift upgraded in this PR** —
   `canonical_tr_m_via_branching.compute_tr_m_via_branching` (A ≥ 3
   delegation) now calls `chi_lambda_all_partitions_mpfr` at the
   50-dps floor with `Q_50_DIGIT_STR`, replacing the initial f64
   wiring. The (c,d) word maps to the signed-word API by linearity;
   the **color-weighted pn crossing** `σ − h(1/2 − δ/4)·1 =
   [σ − h/2·1] + (h·δ/4)·1` becomes the sign-0 averaged crossing
   plus an identity term whose coefficient is rebuilt at 50 dps
   from `flavor_split_subleading` (the word builder's float `d`
   carries only ~17 digits and would silently cap the precision).
   Validated: D (A=2 branching) unchanged; T = 0.10407107578806…,
   ³He = 0.20657847010037… (0.7-0.8 s each), matching the f64
   cross-check to its 8 printed digits.
3. **Symbolic-tier gap (flagged)**: the exact-in-q paths
   (`markov_peel`, LaurentQ) cannot represent the color-weighted δ
   (numeric function of q₀). A symbolic δ(q) closed form in
   `_li_2_q_util` would lift the canonical color-weighted word into
   the symbolic tier; until then, color-weighted = MPFR tier,
   strict_averaged = symbolic tier.

## 5. Levers, ranked (symmetrize / active-set / iterate / cache)

1. **Iterative LR block decomposition — the structural fix
   (= June-8 Tier 1, (μ_p, μ_n)-blocks).** Replaces per-λ d_λ² by
   bounded blocks (≤ ~40²) — the only lever that changes the
   scaling law. **This session's A=3 closure is its validation**:
   the full-basis H₉ extracts + machine-ε tritium/³He verifies
   prove the iterated Sub-lemma 2.1 layer is exact; the
   "multiplicity-space (intertwiner) parametrization" is the same
   structure applied per level. With it, ⁶Li ≈ minutes (MPFR),
   ⁹Be ≈ minutes; with the Tier-2 Rust port, seconds. **This is the
   large-A plan.** (Also subsumes "reduce to active set": the
   block decomposition skips zero-c_LR pairs structurally,
   ~30-60% of blocks.)
2. **Symmetrize — bar involution λ ↔ λᵀ.** χ^{λᵀ} is derivable from
   χ^λ (conjugate-transpose symmetry; already wired in the derived-χ
   catalogue per PR #1952, ~50% there). NOT yet exploited by
   `chi_q_atomic` / `chi_lambda_*` paths — a ~2× saving that stacks
   with everything, and at n=18 it halves the dominant top-26 set.
3. **Word-level (GP) path for mid-A** — `chi_lambdas_via_gp` shares
   one GP reduction across all λ; cost ~independent of d_λ (⁶Li
   ~1 s/λ ⇒ ~6.5 min/atom, ⁷Li ~10 s/λ ⇒ ~2.2 h). **Bridge option**
   for ⁶Li/⁷Li before Tier 1 lands — pending a precision check of
   its internals (string output; if f64-internal it needs an MPFR
   variant before canonical use).
4. **Cache / precompute** — per-nucleon shifted NFs (markov_peel
   already does, `_shifted_nucleon_nf`), H₃ seminormal blocks
   (June-8 §3b), Rust `atomic_reduce_cache` (exists). Useful
   constants-level savings; do not change the scaling.
5. **Active-set truncation by y_λ weight — exploratory tier ONLY.**
   tr_M consumers weight by y_λ; truncating tiny-|y_λ·χ| terms is an
   *approximation* and is barred from the canonical path; usable
   for previews if labelled. (And §3 shows tail-trimming saves
   little anyway — the giants dominate.)

## 6. Plan for ⁶Li / ⁷Li (task-3 rescope) and A=8,9

| atom | canonical-tier route available today | wall | notes |
|---|---|---|---|
| ⁶Li (n=18) | none ready: matrix-MPFR infeasible (§2); GP needs precision audit; markov_peel symbolic gives tr_M (22 min, strict_averaged) but **not the per-λ χ cache** | — | deliver after Tier-1 (or GP-MPFR check) |
| ⁷Li (n=21) | same; d_max = 1.1e9 kills all matrix paths | — | same |
| ⁸Be/⁹Be | Tier-1 + Tier-2 only (June-8 plan, confirmed) | min/s | — |

Recommended sequence (supersedes "just run the producer" for A ≥ 6):
**(1)** precision-audit `chi_lambdas_via_gp` internals — if
MPFR-capable (or upgradeable cheaply), it delivers ⁶Li in ~minutes
and ⁷Li in ~hours at canonical tier as a bridge; **(2)** implement
June-8 Tier 1 ((μ_p, μ_n)-block extraction) — the structural fix,
now de-risked by this PR's A=3 machine-ε validation; **(3)** Tier-2
Rust port. Do **not** re-run `compute_atom_chi_rust.py` for A ≥ 6
on the current algorithm at any precision.

## 7a. Why ≥6 cannot go MPFR on the current algorithm (it's d_λ, not precision)

A recurring question: "just run ⁶Li/⁷Li at MPFR." It does not help —
**MPFR is strictly worse than f64 here**, because the wall is the irrep
dimension d_λ, not the precision per number:

- `chi_q_atomic` / `chi_lambda_all_partitions_mpfr` are the SAME
  algorithm at different precision: a per-basis-vector trace,
  **O(L·d_λ²) per λ** (loop d_λ basis vectors × apply L factors on the
  d_λ-dim space). MPFR changes only the cost-per-op (50–150× heavier
  bignum vs hardware float); it does nothing to d_λ².
- d_λ explodes: n=18 d_max = 16,336,320 ⇒ ~9e17 f64 ops/atom ≈ 3.6 yr;
  at MPFR that becomes **centuries**. n=21 d_max = 1.1e9 ⇒ one working
  *vector* is 9 GB (f64) / ~70 GB (MPFR) — unallocatable.

So "≥6 at MPFR" on the current algorithm is a non-starter. The fix is
**algorithmic** (§8): the active-set LR rewrite removes d_λ from the
cost entirely (bounded 2^A blocks), and *because the blocks are tiny it
runs at MPFR cheaply* — i.e. the scaling fix and the canonical-tier
(no-f64) fix for ≥6 are the SAME change.

## 8. Active-set / nucleon-cache profile — the scaling fix, quantified

χ^λ(β_atom), λ⊢3A, restricted to the Young subgroup (H_3)^A:

    χ^λ(β_atom) = Σ_{(μ_1,…,μ_A): μ_i ⊢ 3}
                    c^λ_{μ_1…μ_A} · A_op(I_1,…,I_{A-1}) · Π_i χ^{μ_i}(β_{nuc_i})

Two structural facts collapse the cost (multi-LR enumerated this session
via iterated `lr_coefficients.get_lr_table`):

- **Nucleon cache** — χ^{μ}(β_nuc) is needed only for μ ⊢ 3 (3 shapes,
  dims {1,2,1}) and nuc ∈ {p,n}: **6 base numbers, computed ONCE**,
  reused across every λ and every atom. "Don't recalc each time."
- **Active set** — for each λ only the (μ_1,…,μ_A) tuples with
  c^λ_{μ_1…μ_A} > 0 contribute; the rest are exact structural zeros.
  Per-tuple block work is bounded by `(Π dim V_{μ_i})² ≤ (2^A)²` — the
  d_λ² in the per-basis-vector path is **gone**.

| A | n | p(n) | 3^A | Σ\|active\| | max block (2^A) | LR cost Σ(Πdim)² | f64 cost n! | **speedup** |
|---|---|---|---|---|---|---|---|---|
| 2 | 6 | 11 | 9 | 35 | 4 | 188 | 7.2e2 | 3.8× |
| 3 | 9 | 30 | 27 | 406 | 8 | 4,132 | 3.6e5 | 88× |
| 4 | 12 | 77 | 81 | 3,997 | 16 | 74,338 | 4.8e8 | 6.4e3× |
| 5 | 15 | 176 | 243 | 32,070 | 32 | 1.1e6 | 1.3e12 | 1.2e6× |
| 6 | 18 | 385 | 729 | 229,497 | 64 | 1.55e7 | 6.4e15 | **4.1e8×** |
| 7 | 21 | 792 | 2187 | 1.5e6 | 128 | 2.0e8 | 5.1e19 | **2.6e11×** |

Read: **⁶Li LR cost ≈ 1.55e7 ops ⇒ milliseconds** (vs the 3.6-year f64
wall); **⁷Li ≈ 2e8 ⇒ sub-second**. The LR cost grows ~13× per A unit
(extrapolating: A=8 ~2e9, A=9 ~3e10 — still seconds at MPFR). The block
sizes (≤ 2^A) are tiny, so the whole thing runs **at MPFR (canonical
tier) cheaply** — the d_λ² wall never appears.

This is the June-8 (μ_p,μ_n)-block plan generalised to all A nucleons,
now with concrete active-set counts. Its A-operator layer is the same
one validated at machine ε in this PR's A=3 closure (the H_9 extracts +
tritium/³He verifies) — so the structural correctness is already
demonstrated; what remains is the multi-level (A≥4) implementation.

### 8a. Recommended implementation (the actual scaling PR)

1. `nucleon_chi_cache`: the 6 base χ^{μ⊢3}(β_{p,n}) at MPFR (trivial).
2. `active_lr_tuples(λ)`: iterated-LR enumeration of nonzero
   c^λ_{μ_1…μ_A} (this session's profiler — fast integer math, cache
   per (A, λ)).
3. `A_op` per (λ, μ-tuple, interface-pattern): the multi-interface
   operator on the (Π dim μ_i)-dim block — generalise the validated
   single-interface H_9 extract to the A−1 nested interfaces (the
   "multiplicity-space / intertwiner" parametrisation). MPFR.
4. Assemble χ^λ = Σ_active A_op·Π χ^{μ_i}; emit at 50 dps. Drop-in
   replacement for `compute_atom_chi_rust`'s per-λ output, valid for
   all A, canonical tier — unblocking ⁶Li/⁷Li/⁸Be/⁹Be.

## 8b. Free vs atom: the interfaces are the cost (corrected, implemented)

Sharpening §8 after implementing the free path (`chi_free_via_lr.py`,
validated at 50-dps ε vs the chi-*-free witnesses):

- **FREE config — DONE, cheap, validated.** No interfaces ⇒ the
  multiplicity space collapses to a scalar per μ-tuple:
  χ^λ(β_free) = Σ_active c^λ_{μ-tuple} · Π χ^{μ_i}(β_{nuc_i}). Σ|active|
  = 229k at ⁶Li ⇒ **3.8 s** (⁷Li 29 s). 6 cached nucleon χ; no d_λ.

- **ATOM config — the interfaces force the full running multiplicity.**
  The junction σ couples adjacent blocks, so the iterative transfer
  matrix over the running partition ξ⊢3k must carry the running
  multiplicity m_k[ξ] (Bratteli path count), not a scalar. Honest state
  sizes Σ_ξ m_k[ξ] (the "don't recalc / iterative" state):

  | A | n | p(3k) | Σ_ξ m_k[ξ] (transfer state) | max m_k[ξ] |
  |---|---|---|---|---|
  | 4 | 12 | 77 | 28,814 | 1,490 |
  | 6 | 18 | 385 | **90,472,088** | 1,437,930 |
  | 7 | 21 | 792 | 7,237,942,636 | 65,488,896 |

  So the transfer-matrix atom χ is ~**90M ops at ⁶Li (minutes)** — a
  **7e7× win** over the n! = 6.4e15 per-basis-vector wall (years), and
  feasible; ⁷Li (7.2e9) is heavy but tractable. (My earlier Σc²
  full-tuple figure, 1.6e11, was the naive non-iterative cost and is
  superseded by these iterative state sizes.)

- **The remaining implementation piece** is the per-level interface
  operator in the running-multiplicity basis — the Hecke
  Clebsch–Gordan / F-matrix that says how the junction σ acts when
  fusing nucleon k+1 onto the running ξ. Its A=3 instance is the
  validated H_9 extract (this PR). Generalising it to the running
  basis (so it never touches d_λ) is the focused next PR; it is genuine
  Hecke-category machinery, not a one-shot add-on — and should be
  built + validated on its own, not half-landed here.

**Net**: binding's free term scales now (validated); the atom term has a
proven-feasible transfer-matrix path (~minutes at ⁶Li) whose only
missing piece is the running-basis interface operator (F-matrix).

## 9. See also

- [`2026-06-08-matrix-m-optimization-A-8-9-path.md`](2026-06-08-matrix-m-optimization-A-8-9-path.md) — Tier-1/2/3 plan (dim table corrected here, recommendation confirmed)
- [`2026-06-09-binding-canonical-default-depth-stratified.md`](2026-06-09-binding-canonical-default-depth-stratified.md) — §"Path 1 CLOSED at A=3" (the validation that de-risks Tier 1)
- [`2026-05-20-markov-peel-bottleneck-profile.md`](2026-05-20-markov-peel-bottleneck-profile.md) — symbolic-path profile + caching strategies
- `.claude/skills/local/compute-author.md` §1 — numeric-type decision table (this ruling tightens it for χ producers)
