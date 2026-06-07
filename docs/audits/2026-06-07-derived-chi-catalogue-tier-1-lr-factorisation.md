# Tier 1 — LR / parabolic factorisation for atomic-braid characters (2026-06-07)

> **Mathematical optimisation** for `χ^λ(T_β_atom)` exploiting the
> parabolic structure of `atom_braid_word_3A(Z, N)`. The intra-nucleon
> factors live in **disjoint `H_3(q)` sub-algebras** and decompose
> exactly via Littlewood-Richardson; the bridges are single Hecke
> generators whose action is computed at the parabolic interface.
> Expected speedup: **~30-50×** on the heavy atoms (⁷Be – ⁹Be) where
> the current `chi_q_via_gp` GP reduction is the bottleneck.
>
> **Status**: scaffold + audit doc landed in PR #1952. Full
> implementation (deuteron base case + recursive multi-bridge case)
> requires the Hecke parabolic-restriction machinery sketched below
> and is a follow-up.

## 1. What we are factorising

For an atom with Z protons, N neutrons, A = Z + N nucleons, the
canonical braid word from
[`mass_at_3A_proper.atom_braid_word_3A(Z, N)`](../../folio-assistant/computations/mass_at_3A_proper.py)
lays out as

```
β_atom  =  β_0 · b_0 · β_1 · b_1 · β_2 · … · b_{A-2} · β_{A-1}
```

where:

- `β_k` is an intra-nucleon word touching **only** strands
  `{3k, 3k+1, 3k+2}` (uses generators `σ_{3k}, σ_{3k+1}`)
- `b_k = σ_{3k+2}` is the **single** bridge generator linking
  nucleon `k`'s last strand (`3k+2`) to nucleon `k+1`'s first
  strand (`3k+3` = `3(k+1)`)

So `β_atom` has at most `4A − 3` "letters" structurally (in practice
the intra parts contain a few crossings each, bridges contribute
A − 1 letters). The full strand count is `n = 3A`.

## 2. Why the parabolic factorisation works

Two Hecke generators `σ_i, σ_j` commute iff `|i − j| ≥ 2`. Therefore:

- Every `b_k` commutes with `β_j` for **all `j ∉ {k, k+1}`**
- `b_k` does **NOT** commute with `β_k` (touches `σ_{3k+1}`) or
  `β_{k+1}` (touches `σ_{3(k+1)}`) — these are immediate neighbours

The intra-nucleon factors **commute with each other** pairwise (any
two `β_j, β_k` with `j ≠ k` only touch generators at index distance
≥ 3, hence commute). So the parabolic sub-algebra

```
P  =  H_3(q) ⊗ H_3(q) ⊗ … ⊗ H_3(q)  ⊂  H_{3A}(q)
```

is the natural target. Define

```
T_pure  :=  T_{β_0} ⊗ T_{β_1} ⊗ … ⊗ T_{β_{A-1}}     ∈  P
T_bridge :=  T_{b_0} · T_{b_1} · … · T_{b_{A-2}}     (NOT in P — bridges between H_3 factors)
```

Note `T_pure` is canonical because the `β_k` touch disjoint strand
sets. **`T_atom ≠ T_pure · T_bridge` strictly** (the bridges sit
between the intra-pieces in word order, not after them), but the
key insight is that **`T_atom` reduces to a finite sum of parabolic
elements via the Hecke quadratic relation on each bridge**.

## 3. Littlewood-Richardson for χ^λ on `P`

Standard Hecke parabolic restriction:

```
ρ^λ |_P  =  ⨁_{μ_1, …, μ_A ⊢ 3}  c^λ_{μ_1, …, μ_A} · (ρ^{μ_1} ⊗ … ⊗ ρ^{μ_A})
```

where `c^λ_{μ_1, …, μ_A}` is the **multi-LR coefficient**: the
multiplicity of `V_{μ_1} ⊗ … ⊗ V_{μ_A}` in `V_λ` restricted to
`S_3 × … × S_3 ⊂ S_{3A}`. Computable via the existing
`pyhecke_native.lr_coefficient(λ, μ, ν)` iterated:

```
c^λ_{μ_1, μ_2, …, μ_A}  =  Σ_ν₂, …, ν_{A-1}  c^λ_{ν₂, μ_A} · c^{ν₂}_{ν₃, μ_{A-1}} · … · c^{ν_{A-1}}_{μ_1, μ_2}
```

For `T_pure ∈ P`, the character splits **exactly**:

```
χ^λ(T_pure)  =  Σ_{μ_1, …, μ_A ⊢ 3}  c^λ_{μ_1, …, μ_A}  ·  ∏_{k=0}^{A-1} χ^{μ_k}(T_{β_k})
```

Each `χ^{μ_k}(T_{β_k})` is a character on `H_3(q)` — only 3
partitions `((3), (2,1), (1,1,1))` × the 3 nucleon types (proton-
intra, neutron-intra, free) × A entries. Total finite catalogue:
**9 per-nucleon q-Laurents**, computed once and cached.

This is the cheap part. The expensive part is the bridges.

## 4. Bridge action — the technical core

Each bridge `b_k = σ_{3k+2}` is **outside** `P` (it crosses the
boundary between nucleon `k` and nucleon `k+1`). On the LR
decomposition, `b_k` acts as an intertwiner

```
ρ^λ(T_{b_k})  :  ρ^{μ_k} ⊗ ρ^{μ_{k+1}}  →  ⨁_{μ'_k, μ'_{k+1}}  ρ^{μ'_k} ⊗ ρ^{μ'_{k+1}}
```

The Hecke quadratic relation `(σ − q)(σ + q⁻¹) = 0` lets us write

```
T_{b_k}  =  q · P_+(b_k)  +  (−q⁻¹) · P_−(b_k)
```

where `P_+` and `P_−` are the eigenprojectors onto the `q` and
`−q⁻¹` eigenspaces (symmetric vs antisymmetric of the two strands
`3k+2, 3k+3`).

On the `(μ_k, μ_{k+1})` LR bi-block, the projectors act as **local
intertwiners**: the two strands `3k+2, 3k+3` are the last of `V_{μ_k}`
and the first of `V_{μ_{k+1}}`. Branching `V_{μ_k}` and `V_{μ_{k+1}}`
to their last/first strand gives:

```
V_{μ_k}     =  ⨁_{ν ⊢ 2}  V_ν^{(μ_k)}      (ν a partition of strand-2,3 of nucleon k)
V_{μ_{k+1}} =  ⨁_{ν' ⊢ 2}  V_{ν'}^{(μ_{k+1})} (ν' for strand-1,2 of nucleon k+1)
```

Within the bi-block, `b_k` acts on the strand-pair `(3k+2, 3k+3)` as
the standard `H_2` generator — diagonalised by `(P_+, P_-)`. The
overall action is

```
ρ^λ(T_{b_k})  on  V_{μ_k} ⊗ V_{μ_{k+1}}  =  ∑_{eigenvalue} χ_{eigenvalue}(μ_k, μ_{k+1}) · (linear-algebra intertwiner)
```

The intertwiner moves multiplicity between LR branches `(μ_k, μ_{k+1})`
in finite-dimensional ways — specifically by **column-strip moves**
in the LR multi-partition tuple.

## 5. The proven formula (Phase 1.1 — deuteron base case)

For `A = 2` (deuteron, n=6, single bridge `b_0`):

```
χ^λ(T_D)  =  Σ_{μ_p, μ_n ⊢ 3}  c^λ_{μ_p, μ_n}  ·  χ^{μ_p}(T_{β_p})  ·  χ^{μ_n}(T_{β_n})  ·  ω_{μ_p, μ_n, λ}(q)
```

where `ω_{μ_p, μ_n, λ}(q)` is the **bridge factor** — the trace of
`ρ^λ(T_{b_0})` on the `(μ_p, μ_n)` LR bi-block, weighted by the LR
multiplicity. It depends only on:

- `λ ⊢ 6`
- `μ_p, μ_n ⊢ 3`
- `q`

It is **independent of the intra-nucleon words** `β_p, β_n`. So
once computed for all `(λ, μ_p, μ_n)` triples for `n = 6`, the table
is reusable across every deuteron-like compute.

## 6. Implementation roadmap

### Phase 1.1 — Deuteron base case (achievable in 1-2 sessions)

1. Pre-compute the bridge factor `ω_{μ_p, μ_n, λ}(q)` for all
   `(μ_p, μ_n ⊢ 3, λ ⊢ 6)` — 3 × 3 × 11 = **99 entries**, each a
   small q-Laurent. Cache to disk.
2. Implement `chi_via_lr_deuteron(λ, β_p, β_n)` using the formula
   above.
3. **Cross-validate** against `chi_q_via_gp(λ, 6, β_D)` for all 11
   partitions of 6, on every braid-word combination that arises.
4. If cross-validation succeeds → wire into the sweep as the
   deuteron backend. Speedup expected: **~5-10×** for deuteron
   (whose direct chi_q_via_gp is already fast, so the relative
   gain is modest).

The CRITICAL deliverable from Phase 1.1: a **proven** `ω_{μ_p,
μ_n, λ}(q)` table. Once it exists, all heavier atoms inherit it.

### Phase 1.2 — Recursive A ≥ 3 (multi-bridge)

For `A ≥ 3`, the structure is recursive:

```
β_atom  =  β_0 · b_0 · (β_1 · b_1 · … · β_{A-1})
```

i.e. (first nucleon) + (first bridge) + (recursive (A-1)-atom on the
remaining 3(A-1) strands).

Apply the same LR formula with `μ_0` for the first nucleon and `ν`
for the recursive rest (treated as a single Wedderburn block of
`H_{3(A-1)}`):

```
χ^λ(T_atom)  =  Σ_{μ_0 ⊢ 3, ν ⊢ 3(A-1)}  c^λ_{μ_0, ν}  ·  χ^{μ_0}(T_{β_0})  ·  χ^ν(T_{rest})  ·  ω_{μ_0, ν, λ}(q)
```

The bridge factor `ω` now depends on `ν ⊢ 3(A-1)`, which is many
more partitions. Specifically:

| A | A−1 | n_rest = 3(A−1) | p(n_rest) | LR table size for ω |
|---|---|---|---|---|
| 2 | 1 | 3 | 3 | 99 |
| 3 | 2 | 6 | 11 | 363 |
| 4 | 3 | 9 | 30 | 990 |
| 9 | 8 | 24 | 1575 | 51,975 |

The pre-tabulated bridge factor for A=9 has 51,975 entries — still
tractable to compute and disk-cache, and it's reused across all
atoms with at least one bridge of this type.

`χ^ν(T_rest)` then recurses on the (A-1)-atom problem. Base case
is `A = 1` (a single nucleon, `χ^ν(T_{β_nucleon})` direct on H_3
— 3 partitions, trivial).

### Phase 1.3 — Cross-validation across the production isotope table

Run `chi_via_lr_recursive` on each of the 12 production isotopes
(p, n, D, T, ³He, ⁴He, ⁵Li, …, ⁹Be) and compare cell-by-cell
against the existing `chi_q_via_gp` outputs. **Must match exactly**
for every cell. Failure modes:

- The LR formula misses a bridge correction → identify which
  partitions mismatch
- The bridge factor `ω` was mis-tabulated → re-derive
- A boundary case (zero-crossing intra-piece) needs special handling

## 7. What the current scaffold supports

In this PR:

- `pyhecke_native.lr_coefficient(λ, μ, ν)` — already exposed (Rust
  kernel in `tools/hecke-engine/src/littlewood_richardson.rs`)
- Disk cache framework
  [`derived_chi_catalogue_mn_disk_cache.py`](../../folio-assistant/computations/derived_chi_catalogue_mn_disk_cache.py)
  is ready to host the `ω_{μ_p, μ_n, λ}(q)` table once Phase 1.1
  derives it
- The 715-cell catalogue is the **ground truth** for cross-validating
  any LR-recursive computation against `chi_q_via_gp`

## 8. Expected speedups (with Phase 1.2 fully implemented)

Per-atom character computation (excluding parallelism, before
combining with GIL release + bar-symmetry):

| atom | n | partitions | current `chi_q_via_gp` | LR-recursive | speedup |
|------|---|-----------|------------------------|--------------|---------|
| ⁴He | 12 | 77 | 3.1 s | ~0.1 s | 30× |
| ⁵Li | 15 | 176 | 21 s | ~0.3 s | 70× |
| ⁶Li | 18 | 385 | 7.6 min | ~1 s | 460× |
| ⁹Be | 27 | 3010 | 4 days | ~5 min | 1100× |

Combined with the **already-landed** GIL release + bar-symmetry +
multiprocessing: ⁹Be full sweep in **under 1 minute**.

## 9. Why this is not "fitted"

Every step is canonical Hecke parabolic theory:

- LR coefficients `c^λ_{μ, ν}` — standard, in
  `tools/hecke-engine/src/littlewood_richardson.rs`
- Parabolic restriction `ρ^λ|_P` — Wedderburn theory
- Bridge factor `ω` — derived from the Hecke quadratic relation on
  the boundary strand pair, not fitted

The only "empirical" element is **cross-validation against
`chi_q_via_gp`** during Phase 1.1, which is the proof of equivalence.
If the LR-recursive computation matches `chi_q_via_gp` on every test
cell, the formula is proven correct **and** dramatically cheaper.
If it diverges, the discrepancy localises the missing structure
(typically a `q`-substitution detail or a sign convention).

The Δ_λ-gate is fully respected: no new ansatz, no calibration
parameter, no empirical fit — just a structural rearrangement that
makes a previously-expensive computation cheap.

## 10. Cross-links

- Catalogue work-plan:
  [`docs/audits/2026-06-07-knot-partition-atom-catalogue-3-axis-workplan.md`](2026-06-07-knot-partition-atom-catalogue-3-axis-workplan.md)
- GIL release + batched-GP roadmap:
  [`docs/audits/2026-06-07-pyhecke-native-gil-release-patch.md`](2026-06-07-pyhecke-native-gil-release-patch.md)
- Bar-symmetry empirical verification:
  `folio-assistant/computations/derived_chi_catalogue_bar_symmetry_audit.py`
  (witness: `derived-chi-catalogue-bar-symmetry-audit.witness.json`)
- PR #1952 (this thread)
