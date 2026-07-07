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
| `garnir_full_annihilation` | `∑_{σ∈S_{A∪B}} sgn(σ)·(σ·e_t) = 0` |
| `sum_sign_rep_polytabloid_eq_zero_of_family` | rep-level annihilation ⟸ tabloid family |
| `sum_sign_rep_coset_collapse`, `transversal_sum_eq_zero` | `|S_A×S_B|` cancellation over `CharZero` |
| `garnirGSub`/`garnirHSub`, `*_coe`, `garnir_transversal_exists` | subgroups + left transversal (via `Subgroup.exists_left_transversal_of_le`) |
| `sum_over_garnirG_reindex` | Finset reindex `∑_G = ∑_T ∑_H` |
| `garnir_assembly` | isolate a sign-fixing `π₀ ∈ T`, reduce `e_t` to the other reps |

These compose: `garnir_full_annihilation → sum_over_garnirG_reindex → transversal_sum_eq_zero`
gives `∑_{π∈T} sgn(π)·(π·e_t) = 0`, and `garnir_assembly` isolates `e_t`. **The only
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
`e_t = ∑_{π ≠ π₀} c_π · e_{π•t}` with every `e_{π•t}` strictly more dominant. The truth
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
`∃ s, (∀ t' ∈ s, domWeight t < domWeight t') ∧ e_t = ∑_{t'∈s} c_{t'} e_{t'}` then forces
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

## 4.5 Empirical refutation of the naive lex measure (exhaustive, 2026-07-07)

A faithful small-case model of the shuffle-transversal Garnir straightening
(`/tmp/garnir/model2.py`, `exhaustive2.py`) tested the two obvious termination measures
against **every** column-standard tableau and **every** row descent, for shapes up to
`(4,3)` / `(3,3,2)`. Both **fail**:

| candidate measure | requirement (on every non-standard, non-identity term) | result |
|---|---|---|
| `sec = row-inversions` alone | `sec(π•t) < sec(t)` | **FAILS** — `(3,2)`, `(4,2)`, `(3,3)`, … have terms with equal or *higher* row-inversions (e.g. `(4,2)`: 45 failing terms, some `1→2`) |
| lex `(domWeight ▷, row-inversions ↓)` | term strictly `▷ t`, else same-tabloid & `sec ↓` | **FAILS** — `(3,3)`: 104/360 terms; `(4,3)`: 1009/2940. Failing terms are strictly *less* dominant **and** non-standard |

**Worked counterexample (the smallest).** `t = [[1,2,3],[5,4]]` (column-standard, row
descent at `(1,0)`). Garnir set `A = {5}` (col 0, row ≥ 1), `B = {2,4}` (col 1, row ≤ 1).
The shuffle transversal has three reps; besides the identity and the standard term
`[[1,2,3],[4,5]]`, it produces `[[1,4,3],[2,5]]` — which is **column-standard,
non-standard** (row-0 descent `4>3`), **strictly less dominant** than `t`
(`{1,2,3}{4,5} ▷ {1,3,4}{2,5}`), and has the **same** row-inversion count (`1→1`). So
neither `domWeight` nor row-inversions decreases on a term that still needs straightening.

**Scope of this refutation (STRICT — per AGENTS.md "before declaring refuted").** This is a
**scope-limited negative (a)**: the two *specific naive measures above*, in this
combinatorial model, do not monotonically decrease. It is **not** a structural exclusion —
the classical standard-basis theorem is true, so *some* well-founded order works. The
correct order is the **last-letter / column-word dominance** used by James (Thm 8.4) and
Sagan (§2.6.4–5), which compares tableaux (not just row-tabloids) and is genuinely subtler
than any lexicographic combination of `domWeight` + a local inversion count. The lesson:
**model the classical column-word order faithfully in the Python harness and re-run the
exhaustive check *before* writing any Lean, so the formalized measure is one that provably
terminates.**

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

## 5. Concrete next steps (revised 2026-07-07 after §4.5)

0. **Model the classical column-word (last-letter) order in the Python harness** and re-run
   the exhaustive check until a measure passes on every non-standard term for all shapes up
   to ≥ `(4,3)`. Do **not** formalize a measure that has not passed this check — both naive
   candidates looked plausible and failed.
1. Replace `garnir_transversal_exists` (arbitrary transversal) with a **shuffle
   transversal** constructed from order-preserving bijections `A ≃ σ(A)`, `B ≃ σ(B)`.
2. With the *validated* order from step 0, either prove the leading-tabloid unitriangularity
   lemma (Option B, now preferred) or the column-word decrease for shuffle reps.
3. Re-shape `garnir_assembly` to the `(1+κ)·e_t = dominant` form (absorb same-tabloid
   cosets), and rework `straightening_step` / `standardPolytabloid_straightening` onto the
   validated order — **not** the `domBound − domWeight` measure, which §4.5 shows is
   unsound even with a row-inversion tie-breaker.

**Effort estimate.** This is research-grade: Mathlib has no Specht modules, the correct
termination order is the subtle column-word dominance, and steps 1–3 each need fresh
formalization. Realistically multi-day. The 17 sorry-free algebraic lemmas (§1) are the
durable asset and stand regardless of which order closes the induction.

The roadmap comment on `straightening_step_colMax` carries a condensed version of §2–§3
so the next pass does not re-wire the false `hdom`.

## References
- Sagan, *The Symmetric Group*, §2.6 (Garnir relations / straightening).
- James, *The Representation Theory of the Symmetric Groups*, §8 (standard basis).
