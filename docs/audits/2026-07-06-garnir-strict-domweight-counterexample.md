# Garnir straightening: the strict-`domWeight` dominance is FALSE — counterexample and reformulation sketch

**Date:** 2026-07-06
**Scope:** `content/quantum-observable-universe/lean/QOU/BraidKnot/SpechtStandardBasisCore.lean`
— piece 2 (the Garnir coset-sum that closes `straightening_step_colMax`).
**Verdict:** the coset-sum *machinery* is proved sorry-free; but the final *dominance*
step is not merely hard — **the theorem `straightening_step_colMax` is false as stated**
(§3.5, definitive, exact-arithmetic disproof, 2026-07-07). Its goal demands the Garnir
terms be *strictly `domWeight`-greater*; the real standard-basis expansion produces terms
that are dominance-`⊴ {t}` (equal-or-lower `domWeight`). Because the framework's
`domWeight` is **maximized** by the small-labels-on-top arrangement, a column-maximal
non-standard `t` can already sit at the `domWeight` maximum, leaving *no* strictly-greater
term to expand into. The whole `domBound − domWeight` **increasing** induction is
mis-directed. This doc records the disproof and the reformulation required.

> **Headline for the next agent.** Do **not** try to close the `straightening_step_colMax`
> sorry — the statement is unsatisfiable. The framework needs restatement (terms
> dominance-`⊴`, standard tableaux as the induction *minima*, or the classical column-word
> order). The 17 sorry-free algebraic lemmas (§1) stand and are reusable.

## 1. What is proved (sorry-free, `lean`-direct exit 0)

The entire algebraic + annihilation + reindexing half of the Garnir relation:

| lemma | content |
|---|---|
| `card_col_labels`, `card_col_labels_row_lt_of_le` | column label counts |
| `garnir_row_collision` | the pigeonhole (`|A|+|B| = colLen j + 1`) → same-row `(a∈A,b∈B)` collision |
| `garnir_full_annihilation` | `Σ_{σ∈S_{A∪B}} sgn(σ)·(σ·e_t) = 0` |
| `sum_sign_rep_polytabloid_eq_zero_of_family` | rep-level annihilation ⟸ tabloid family |
| `sum_sign_rep_coset_collapse`, `transversal_sum_eq_zero` | `|S_A×S_B|` cancellation over `CharZero` |
| `garnirGSub`/`garnirHSub`, `*_coe`, `garnir_transversal_exists` | subgroups + left transversal (via `Subgroup.exists_left_transversal_of_le`) |
| `sum_over_garnirG_reindex` | Finset reindex `Σ_G = Σ_T Σ_H` |
| `garnir_assembly` | isolate a sign-fixing `π₀ ∈ T`, reduce `e_t` to the other reps |

These compose: `garnir_full_annihilation → sum_over_garnirG_reindex → transversal_sum_eq_zero`
gives `Σ_{π∈T} sgn(π)·(π·e_t) = 0`, and `garnir_assembly` isolates `e_t`. **The only
missing input is the dominance hypothesis `hdom`** — and that hypothesis is false.

## 2. The counterexample (verified)

`garnir_assembly` requires: for every non-identity transversal rep `π`,
`domWeight t < domWeight (π•t)` (strict). Take the Garnir set at the row descent
`(i,j),(i,j+1) ∈ μ` with `labelAt t (i,j+1) ≤ labelAt t (i,j)`:

- `A = {labels in col j, row ≥ i}`, `B = {labels in col j+1, row ≤ i}`.
- The **row-`i` overlap is essential**: it is exactly what makes
  `|A| + |B| = (colLen j − i) + (i+1) = colLen j + 1 > colLen j`, the strict inequality
  the pigeonhole (`garnir_row_collision`) needs.
- But then `a := labelAt t (i,j)` and `b := labelAt t (i,j+1)` are **both in row `i`**,
  and `π := Equiv.swap a b` satisfies:
  - `π ∈ garnirG` (fixes everything outside `A ∪ B`; `a∈A`, `b∈B`);
  - `π ∉ colStab t` (it moves `a` to column `j+1` and `b` to column `j`), so `π ∉ H`
    (`= garnirG ∩ colStab`) — a **non-identity coset element**;
  - `rowPattern (π•t) = rowPattern t` (both labels stay in row `i`), so
    **`domWeight (π•t) = domWeight t`** — not `>`;
  - `{π•t} = {t}` (same tabloid), so **no representative of that coset strictly
    dominates** `t`.

Hence `hdom` is unsatisfiable for *any* transversal, and the same-tabloid coset feeds
the coefficient of `e_t` **itself** (its leading tabloid is `{t}`, like `e_t`'s).

## 3. Why `garnir_assembly`'s shape is wrong

`garnir_assembly` assumes the Garnir relation has the form
`e_t = Σ_{π ≠ π₀} c_π · e_{π•t}` with every `e_{π•t}` strictly more dominant. The truth
is `(1 + κ)·e_t = (strictly-dominant terms)` where `κ` collects the same-tabloid cosets:
the correct straightening solves for `e_t` after absorbing those, using the **partial
dominance order + sign cancellation**, not a strict linear measure. `domWeight` (a strict
linear extension) cannot see the tie, so `domWeight`-strict induction cannot drive it.

This is not specific to `garnir_assembly`: the pre-existing `straightening_step` /
`standardPolytabloid_straightening` also carry the strict-`domWeight` shape (induction on
`domBound μ − domWeight t`), which the counterexample suggests needs the same rework.

## 3.5 Definitive disproof (exact arithmetic, 2026-07-07)

§2–§3 showed a *coset* whose reps tie `domWeight`. This section proves the stronger claim
that `straightening_step_colMax` is **false as a proposition**, using the exact
standard-basis coordinates (`/tmp/garnir/solve.py`, `Fraction` Gaussian elimination — the
standard polytabloids are a basis, so coordinates are unique).

**Witness.** Shape `μ = (3,2)`, `t = [[1,2,3],[5,4]]`.

- `t` is **column-standard** (`col 0 = (1,5)`, `col 1 = (2,4)`, `col 2 = (3)` all increasing),
  hence **column-maximal**: every `σ ∈ colStab t` moves a smaller label down a column, so
  `domWeight (σ•t) ≤ domWeight t`. ⟹ hypothesis `hmax` holds.
- The unique standard-basis expansion is
  `e_t = e_{[[1,2,3],[4,5]]} − e_{[[1,3,4],[2,5]]} + e_{[[1,3,5],[2,4]]}` — a genuine
  3-term combination, so `e_t` is **not** a single standard polytabloid. ⟹ hypothesis `h`
  (`polytabloid t ∉ range standardPolytabloid`) holds. Also `e_t ≠ 0`.

**The invariant that forbids the conclusion.** The framework's `domWeight`
(`domCount' f i m = #{l : l < m ∧ f l ≤ i}`, summed over `i,m`) counts *small labels in
top rows*, so it is **maximized** by `{1,2,3}{4,5}` — which is exactly `{t}`. Therefore
`{t' : domWeight t' > domWeight t}` is **empty** (nothing exceeds the maximum). The goal
`∃ s, (∀ t' ∈ s, domWeight t < domWeight t') ∧ e_t = Σ_{t'∈s} c_{t'} e_{t'}` then forces
`s = ∅`, i.e. `e_t = 0` — contradicting `e_t ≠ 0`. ∎

The three standard terms of `e_t` sit at dominance `=`, `<`, `<` relative to `{t}`
(never `>`): straightening moves **down** the order, not up. This is a structural
exclusion **(b)** with a cited invariant (`{t}` maximal ⇒ no strictly-greater tabloid),
per AGENTS.md's refuted-claim rule — not a scope-limited numerical miss.

**Consequence for the framework.** `straightening_step` (the parent) routes every
column-maximal non-standard `t` into `straightening_step_colMax` and claims the *same*
strictly-`domWeight`-greater goal shape, so it inherits the falsity. The
`standardPolytabloid_straightening` / `_span` chain built on `domBound − domWeight`
strong induction is therefore mis-directed at the root: it tries to *increase* a measure
whose maximum is a **non-standard** tableau. A correct straightening decreases toward
standard tableaux (the classical column-word / last-letter order, in which standard
tableaux are minimal).

## 4. Reformulation sketch (options)

**Option A — lexicographic measure `(domWeight, secondary)`.**
Add a secondary tie-breaker `sec t` (e.g. a count of within-row inversions of the
column-word) and induct on `(domBound − domWeight t, sec t)` lexicographically. Each
Garnir term then either (i) strictly raises `domWeight` (the genuinely-dominant cosets),
or (ii) ties `domWeight` and strictly lowers `sec` (the same-tabloid cosets, which fix a
local row-descent). *Cost:* one must pick the transversal so that the same-tabloid reps
provably lower `sec` — i.e. the classical **shuffle transversal** (reps increasing on `A`
and on `B`), not Mathlib's arbitrary `exists_left_transversal_of_le` output, plus a proof
that shuffle reps decrease the lex measure. This is the genuine combinatorial crux.

**Option B — James's route (avoid straightening-by-domWeight entirely).**
Prove the standard basis theorem via unitriangularity: (a) standard polytabloids are
linearly independent because `e_s` has *leading tabloid* `{s}` in the dominance order and
distinct standard `s` have distinct `{s}`; (b) they span by a dimension/counting argument
against `numSYT`, using the Garnir relations only to bound, not to strictly decrease. The
module docstring already gestures at this ("independence via the dominance/last-letter
order"). This sidesteps the strict-`domWeight` induction but needs the leading-term
machinery.

**Recommendation (SUPERSEDED — see §4.5).** Option A *looked* closest to the existing
scaffolding, but the empirical check in §4.5 shows its specific lex measure
`(domWeight, row-inversions)` **does not terminate**. Option B (leading-tabloid
unitriangularity) is now the preferred route. Either way the residual is the **shuffle
transversal + a correct well-founded order** — the part Mathlib does not provide (no
Specht modules in Mathlib at all).

## 4.5 domWeight (tabloid dominance) is insufficient — but the COLUMN-WORD order works (exhaustive, validated 2026-07-07)

> **Retraction note.** An earlier revision of this section reported "exhaustive
> refutation" failure *counts* for `row-inversions` and lex `(domWeight, row-inversions)`
> from a small-case model (`model2.py`/`exhaustive2.py`). That model had a **sign bug** —
> it dropped the coset rep's `sgn(π)` factor, so its "Garnir terms" did **not** satisfy the
> Garnir relation `Σ sgn·e = 0` (checked: **all** (t,descent) pairs violated it). Those
> specific counts are withdrawn. The corrected model (`/tmp/garnir/vo2.py`) satisfies
> `Σ sgn·e = 0` on every (t,descent) pair for shapes up to `(4,2)` and is the basis for the
> validated result below. The §3.5 disproof is **unaffected** — it used the exact
> standard-basis expansion (direct `poly_vec` + rational solve), not the shuffle model.

With the **corrected, relation-validated** shuffle-transversal model, tableau-level
termination measures were tested for strict decrease on **every non-standard, non-identity**
single-step Garnir term, over all column-standard tableaux and all row descents, shapes up
to `(3,3,2)` (3967 non-standard terms):

| candidate measure | strict-decrease failures |
|---|---|
| `domWeight` descending (tabloid dominance, ℕ linear ext.) | **FAILS** — e.g. `(3,3)`: 216; `(4,3)`: 1805 |
| `domWeight` ascending | **FAILS** — `(4,3)`: 2012 |
| row-reading word, lex | **FAILS** — `(4,3)`: 201 |
| **column-reading word, lex `<`** (col-major, first entry most significant) | **0 failures** — every shape, incl. `(4,3)`=2814, `(3,3,2)`=3967 |
| ℕ-encoded column word `Σ_k w_k·(n+1)^{…}` (Lean-ready) | **0 failures** — same |

**Why `domWeight` cannot work:** Garnir produces terms whose *tabloids are
dominance-incomparable* to `{t}` (e.g. `(2,2,2)`: `t=[[1,2],[5,3],[6,4]]` →
`[[1,3],[2,4],[6,5]]`, `INCOMP`). No linear extension of tabloid dominance orders those
consistently. The **column-reading word** (a tableau-level, not tabloid-level, statistic)
does — this is the classical straightening order (James Thm 8.4, Sagan §2.6.4–5).

**The validated measure (keystone for the restatement).** Read `t` column-major
(left-to-right, top-to-bottom): `colWord t = [t(0,0), t(1,0), …, t(0,1), t(1,1), …]`.
Encode as `colWordNum t = Σ_k colWord(t)[k]·(n+1)^{(n-1-k)}` (first column entry most
significant; entries `< n+1` so base `n+1` is faithful). **Every non-standard Garnir term
`t'` satisfies `colWordNum t' < colWordNum t`.** Standard tableaux are the lex-minima
within a column class, so the strong induction on `colWordNum` (descending) terminates at
standard polytabloids. This is the drop-in replacement for `domWeight`.

## 4.6 LSP / elan toolchain — the fetch blocker is fixed (2026-07-07)

The lean-lsp-mcp server had been unusable all session: every call died with an elan
`install_from_dist → fetch_url` backtrace (the toolchain server `release.lean-lang.org` is
firewalled). Root cause: the project's `lean-toolchain` pins `leanprover/lean4:v4.24.0`,
but the only installed toolchain was hand-named `lean-v4.24.0` (symlink to
`/tmp/lean-v4.24.0`). elan mangles the file spec to the directory name
`leanprover--lean4---v4.24.0` (`/`→`--`, `:`→`---`), didn't find it, and tried to fetch.

**Fix (persistent, no network):**
```bash
ln -sfn /tmp/lean-v4.24.0 ~/.elan/toolchains/'leanprover--lean4---v4.24.0'
elan default lean-v4.24.0
```
After this, `elan run 'leanprover/lean4:v4.24.0' lean --version` resolves offline and the
LSP **initializes** (returns real diagnostics, no timeout). Residual, softer wall: lake
considers the out-of-band-restored oleans stale ("Imports are out of date and must be
rebuilt"), so the LSP still cannot serve *live goal state* on a Mathlib-importing file
without a `lake build` that risks the Mathlib re-clone/wipe. `lean`-direct (LEAN_PATH →
restored oleans) therefore remains the verification path. The elan alias should be added to
the sandbox Lean-setup so future sessions get a working LSP handshake.

## 5. Concrete next steps (revised 2026-07-07 — column-word order validated)

The keystone (which measure) is now settled empirically (§4.5): the **column-word measure
`colWordNum`**. The restatement is:

1. **Define `colWordNum t : ℕ`** (column-major reading word, base-`(n+1)` positional
   encoding, first column entry most significant) alongside the existing `colPattern`.
   A fixed ceiling `colWordBound μ` (= `(n+1)^n`, or the sum bound) plays `domBound`'s role.
2. **Restate `straightening_step`** — replace the false goal `∀ t'∈s, domWeight t < domWeight t'`
   with:
   `∀ t'∈s, e_{t'} ∈ range standardPolytabloid ∨ colWordNum t' < colWordNum t`
   (each Garnir term is already standard **or** strictly column-word-smaller). The identity
   coset contributes coefficient `1` (t column-standard ⇒ colsort sign `+1`), so
   `e_t = −Σ_{non-id} c·e_{t'}` with **no** `CharZero` division needed.
3. **Prove the column-word-decrease lemma** for the shuffle transversal: every non-identity
   shuffle rep's column-sorted image has strictly smaller `colWordNum`. This is the new
   combinatorial core (replaces the false dominance claim); validated exhaustively to
   `(3,3,2)`.
4. **Rework `standardPolytabloid_straightening`** to strong-induct on `colWordNum t`
   (descending) instead of `domBound − domWeight t`. The `standardPolytabloid_span_eq_specht`
   / `_span` corollaries then follow unchanged (they only consume the `_straightening`
   conclusion, which keeps the same *type*).

The column-antisymmetry branch of `straightening_step` (the `∃ σ ∈ C_t` raising case) also
needs re-expressing: a column-sort toward the standard column order **lowers** `colWordNum`
(the sorted column word is lex-smallest), consistent with the descending induction.

**What is reusable as-is:** the 17 sorry-free algebraic/annihilation/reindex lemmas (§1) —
they establish the Garnir relation `Σ sgn·e = 0` and the coset reindexing, which are
measure-independent. Only the *dominance conclusion* (`garnir_assembly`'s strict-`domWeight`
premise, `straightening_step*`'s goal shape, and the induction measure) changes.

### 5.1 Progress (2026-07-07) — 6 sorry-free bricks + a cleaner path

Landed sorry-free on the branch (`lean`-direct exit 0; file stays at ONE sorry, colMax):
`colWordNum`/`cmajSig` (measure), `cmajSig_lt_of_col_row`, **`colWordNum_swap_lt`** (a
within-column descent swap strictly lowers `colWordNum` — the analogue of
`domWeight_swap_lt`), `colStandard_of_colWordMin`, `exists_row_descent_of_colWordMin`
(roadmap step 1), and **`garnir_assembly_gen`** (the measure-generic assembly, parametric
over `P : Tableau → Prop`).

**The shuffle transversal is NOT needed — use the full group.** A relation-validated model
(`/tmp/garnir/vo2.py`) shows: aggregate `sgn(σ)` over **all** of `S_{A∪B}` (the already-proved
`garnir_full_annihilation`, `Σ_{σ∈garnirG} sgn(σ)·(σ·e_t) = 0`) and group the resulting
polytabloids by their **column-sorted** tableau. Then **every** column-sorted tableau with
*nonzero* aggregated coefficient (other than `t`) has strictly smaller `colWordNum` —
0 failures over shapes to `(3,2,1)`. The non-decreasing terms **cancel to zero
coefficient**. So the plan is:

1. `garnir_full_annihilation` (proved) ⇒ `|H|·e_t = −Σ_{σ∈garnirG\H} sgn(σ)·e_{σ·t}`
   (the `σ∈H⊆colStab` part collapses to `|H|·e_t` via column antisymmetry; needs `CharZero`
   for the `1/|H|`).
2. Rewrite each `e_{σ·t} = sgn(colsort σ)·e_{colsort(σ·t)}` and group by the column-sorted
   tableau `t'`.
3. **The remaining core:** show the aggregated coefficient `c_{t'} = 0` for every `t'` with
   `colWordNum t' ≥ colWordNum t` (the cancellation), leaving only `colWordNum`-smaller
   terms — then `garnir_assembly_gen` (or a full-group variant) closes colMax. Empirically
   the fibre of `t'` is a single `H`-coset, so this is the coset-sign-collapse
   (`sum_sign_rep_coset_collapse`, proved) combined with the row-collision cancellation
   (`garnir_row_collision`, proved) — the genuine hard combinatorial content, but now
   framed without any explicit shuffle-transversal object.

**Effort estimate.** Research-grade but now well-scoped: Mathlib has no Specht modules, but
the termination order is settled and Lean-ready. Steps 1–4 are a focused restatement +
one new combinatorial lemma (step 3), not open-ended research.

The roadmap comment on `straightening_step_colMax` carries a condensed version of §2–§3
so the next pass does not re-wire the false `hdom`.

## References
- Sagan, *The Symmetric Group*, §2.6 (Garnir relations / straightening).
- James, *The Representation Theory of the Symmetric Groups*, §8 (standard basis).
