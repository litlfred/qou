---
# sv8b
title: 'GAP: seminormalVector_base_exists — the last labelling sorry (brick-5 OV)'
status: completed
type: task
priority: high
created_at: 2026-08-07T22:10:00Z
updated_at: 2026-08-25T11:12:14Z
---

## Priority escalation (2026-08-08) — this blocks BOTH PlancherelSnData axioms

Originally filed as the blocker on axiom (ii) (the `ω = Σ c²` labelling). #4710
(merged, `b10c689e`) landed `BurnsideDischarge.lean`, deriving `Σ_λ (f^λ)² = n!`
from the roadmap bridges and replacing the `BurnsideContext` self-assuming
projection with a real instance. Its `burnside_proved` carries a residual
`sorryAx` tracing to exactly two lemmas: `SnWedderburnPartitionBridge:234` and
**`JucysMurphy:840` — this one**.

So axiom (i) `Σ_λ dim² = n!` lands on this lemma too, once the labelling bridges
are in place. **This is now the single highest-value open lemma in the Identity-I
chain**, not merely the `ω`-side blocker.

## Inputs that landed since this bean was filed

- **The column-superstandard tableau now exists** (#4716, 10 decls, sorry-free) —
  the sub-task this bean flagged as missing (`grep colSuperstandard` was empty).
  It is `Finset.orderIsoOfFin` for the column-then-row lex order, since
  `Specht.Tableau μ` is definitionally `Fin (nOf μ) ≃ μ.cells`.
  - **Trap recorded there:** applying `orderIsoOfFin` under a bespoke
    `LinearOrder (ℕ × ℕ)` *appears* to elaborate, but `ℕ × ℕ` already carries
    Mathlib's componentwise `Prod.instLE_mathlib`, so type-annotated downstream
    lemmas resolve `LE` to the ambient instance and mismatch. Instance-level —
    `show`/`unfold` do not fix it. Route through `ℕ ×ₗ ℕ` and transport back.
- **`sameColumn_count`** — for the column-superstandard tableau,
  `#{j < s : (j s) ∈ colStab T₀} = row index of s`. So the first summand of
  `jm_polytabloid_split` is exactly `−i · e_{T₀}`: **the `−i` of
  `content (i,j) = j − i` is settled.**
- **`swap_mem_colStab_iff`** — the converse of `colStab_swap_mem` (which gave only
  same-column ⟹ in `colStab`). This is what turned the count into an exact equality.

Division of labour (agreed on PR #4702, per the measured-research-overlap rule):
the sibling took the tableau construction and the `−i` half and is deliberately
staying off steps 2–5 below; **steps 2–5 are this bean's**.

## The gap

`QOU.BraidKnot.JucysMurphy.seminormalVector_base_exists`
([`JucysMurphy.lean:850`](../content/quantum-observable-universe/lean/QOU/BraidKnot/JucysMurphy.lean))
is an honest, cited `sorry` — `-- Ref: [vershik-kerov1977]` (Young's seminormal
form, existence of the explicit seminormal **base** vector in `S^λ`).

After PR #4702 this is the **single remaining live `sorry` in the whole
partition-labelling chain**. Everything above it is assembled from it:

- `seminormalVector_data_exists` (JucysMurphy.lean:1218) — consumes it directly
  (`obtain ⟨T₀, hbase⟩ := seminormalVector_base_exists`).
- `exists_indep_seminormal_family` (JucysMurphy.lean:1606) — `choose`s from
  `seminormalVector_data_exists`.
- `OVTopAssembly.identityB_general` / `sum_numSYT_sq_eq_factorial` — the
  "unconditional modulo the assembled OV bricks" results.

## Why it matters (the precise consumer)

The s5-so3 ledger (2026-07-02, #3193/#3220) records that after
`identityB_via_wedderburn_unconditional`, the residual content of the two
`PlancherelSnData` axioms is **exactly the partition labelling** of the abstract
Wedderburn blocks (blocks ↔ `λ⊢n`, `d = #SYT`, `ω = Σc²`) — i.e. the brick-5 OV
cores, *not* the trace/block/center machinery.

Of that labelling:

- **`d = #SYT` side: CLOSED.** `specht_finrank_eq_numSYT` (`dim_k S^μ = #SYT(μ)`)
  verifies sorry-free after PR #4702 — the Garnir straightening core
  `straightening_step_colMax` and the spanning half `standardPolytabloid_span`
  were already proved in source; the file merely did not elaborate, and its
  status tables were stale.
- **`ω = Σc²` side: THIS BEAN.** The OV seminormal eigenbasis is what attaches the
  JM content-square eigenvalue to the partition-indexed block.

So this one lemma is what stands between the current state and axiom (ii) of
`PlancherelSnData` at general `n`. It does **not** by itself give Identity I
general-`n` — axiom (i) `Σ_λ dim² = n!` needs its own discharge — but it is the
named blocker on the `ω` side.

## What was attempted

Nothing on the proof itself this session. The gap was *localised*, not attacked:
the session's Lean work went into repairing `SpechtStandardBasis` (PR #4702),
which is what made it possible to see that brick-4 was already done and that
brick-5 reduces to this single lemma.

## Next honest step — now reduced to ONE identity

Two findings sharpen this considerably.

**(a) The stated blocker was stale.** The decl's docstring said the construction
"needs the polytabloid straightening machinery not yet built here". False:
`JucysMurphy.lean` imports `QOU.BraidKnot.SpechtStandardBasis`, and after #4702
that machinery (`standardPolytabloid_straightening`, `standardPolytabloid_span`,
Garnir core `straightening_step_colMax`) is **proved sorry-free**. Docstring
corrected. What remains is the eigen-computation, not missing infrastructure.

**(b) The reduction is already built and sorry-free.**
[`OVBaseSeminormalVector.lean`](../content/quantum-observable-universe/lean/QOU/BraidKnot/OVBaseSeminormalVector.lean)
(0 sorries; imports `JucysMurphy`, so the residual must land there or in a leaf —
the same import-direction constraint that forced #4692's `HookProductHLF` layout).
Its `jm_polytabloid_split` gives, for any tableau `t`:

    X_s · e_t = #{j < s : (j s) ∈ colStab t} · (−e_t)
                + Σ_{j < s, (j s) ∉ colStab t} e_{(j s)·t}

For the column-superstandard `T₀` with `s` at cell `(i, j)`, the same-column count
is `i`, giving `−i · e_{T₀}`; since `content(i,j) = j − i`, the **sole remaining
obligation** is the off-column (Garnir) collapse:

    Σ_{j' < s, (j' s) ∉ colStab T₀} e_{(j' s)·T₀} = j · e_{T₀}

i.e. the off-column sum contributes exactly the count of cells strictly left of
`s` in its row. Numerically confirmed for the column-superstandard choice in
[`2026-07-19-ov-base-vector-column-superstandard-verification.md`](../docs/audits/2026-07-19-ov-base-vector-column-superstandard-verification.md).

That single identity is the whole gap. It is real Garnir combinatorics — not a
wiring exercise — so it should be attacked as a proof, with the existing bricks
(`starSum_rep_polytabloid`, `colGarnir_fullgroup_sum`,
`colGarnir_single_column_of_annihilation`, `sameColumn_sum_polytabloid`) as input.

## The collision, decomposed (worked out; step 1 landed)

Per the 2026-07-19 audit's second pass, the single-column relation reduces to the
**full-group annihilation** `∑_{σ ∈ S_{C∪{s}}} sgn σ · σ·e_t = 0`
(`colGarnir_single_column_of_annihilation` then divides by `|C|! ≠ 0`). Via
`sum_sign_rep_polytabloid_eq_zero_of_family` + `mtab_sum_sign_smul_of_eq_zero`
that is exactly a **row collision**: for every `ρ ∈ colStab t`, two distinct labels
of `C ∪ {s}` share a row in `ρ • t`.

**The argument is generic in `t`** — it needs only `c < c_s`, *not*
column-superstandardness. That matters: it can be proved before the
column-superstandard tableau is constructed.

1. `ρ ∈ colStab t` ⟹ `colPattern (ρ • t) = colPattern t`, so the column-`c`
   labels of `ρ • t` are still exactly `C`. — **DONE, sorry-free**:
   `OVBaseSeminormalVector.colPattern_smul_of_mem_colStab` +
   `colLabels_smul_of_mem_colStab`.
2–4. **DONE, sorry-free — and the plan below was more than the argument needs.**
   `OVBaseSeminormalVector.exists_sameRow_earlier_col` /
   `exists_collision_earlier_col`. A tableau is an **`Equiv`** onto `μ.cells`, so the
   colliding label is produced by exhibiting its *cell* and pulling back through
   `t.symm`. There is no need to show the column-`c` labels occupy rows
   `0 … colLen c − 1`, no counting, and `|C| = colLen c` is never required. With
   `r = row s`: `(r,c') ∈ μ` ⟹ `r < colLen c'`; `colLen_anti` ⟹ `colLen c' ≤ colLen c`;
   so `(r,c) ∈ μ`; take `x = t.symm ⟨(r,c), _⟩`. Strict `c < c'` additionally gives
   `x ≠ s`. Generic in `t`.

   *Superseded plan (kept for the record):* (2) the column-`c` labels fill column `c`,
   occupying rows `0 … colLen c − 1`; (3) `s` at row `< colLen c_s`; (4) the `colLen`
   comparison. Steps 2 and 3 were never needed as separate facts.
   The Mathlib ingredient used is
   `YoungDiagram.colLen_anti : ∀ μ j1 j2, j1 ≤ j2 → μ.colLen j2 ≤ μ.colLen j1`
   (present in the pinned v4.24.0).

5. Combine: the column-`c` label at row `r` collides with `s`; distinct since their
   columns differ. Feed as `hfam`. — *open* (assembly).

Then (iv) sum the single-column relations over `c < c_s` and combine with brick 3a
(`sameColumn_sum_polytabloid`, giving the `−row(s)` term) to get the eigen-equation;
(v) discharge the two side conjuncts (`polytabloid_mem_specht`, `≠ 0` from standard
-basis independence) and close `seminormalVector_base_exists`.

**Also still needed:** the **column-superstandard tableau itself** does not exist in
the tree (`grep colSuperstandard` is empty; only `SytRowSuperstandard` exists, and the
audit shows the *row*-superstandard polytabloid is **not** an eigenvector — building
toward it would be proving a false statement). Constructing it and proving it standard
is its own sub-task.

Base ring is genuinely `[Field k] [CharZero k]` — the `[CommRing k]` form is
**false** (contents collide mod `p`, eigenspaces merge); already documented at the
decl, do not "generalize" it.

## Caveat for whoever picks this up

**Do not audit sorry-status from restored oleans.** The restored `lake-cache`
tree was missing `SpechtStandardBasisCore.olean` while carrying its own
dependents (built from an older source tree), so `#print axioms` reported a
phantom `sorryAx` that vanished after rebuilding the cone from source. Rebuild
the cone with `-DautoImplicit=false` (matching the lakefile) before believing any
axiom query.


---

## CLOSED 2026-08-25 — the gap no longer exists. Measured, not read.

`seminormalVector_base_exists` is **proved**, sorry-free. Found by attempting to work this
bean, not by auditing it.

Verified per this bean's own caveat — the root Mathlib cache here is restored
(`oleans=6990 traces=0`), so the whole transitive `QOU.*` cone was **rebuilt from source**
with `lean -o` in topological order before printing anything:

    CONE_REBUILD_DONE  files=115  failures=0
    EXTRA_DONE         files=4    failures=0

`#print axioms` against that fresh cone — all `[propext, Classical.choice, Quot.sound]`,
**no `sorryAx`**:

    SeminormalBaseExists.seminormalVector_base_exists'
    JucysMurphy.seminormalVector_base_exists
    SnIsotypicSpechtSplitInstance.instSnIsotypicSpechtSplit
    OVTopAssembly.identityB_general
    PlancherelSnDataGeneral.plancherelSnDataGeneral
    PlancherelSnDataGeneral.two_sum_dim_sq_hooks_general
    PlancherelSnDataGeneral.twoM_eq_plancherel_hook_sum_general

### Why a grep for `sorry` in JucysMurphy.lean disagrees with this bean

It cannot be discharged in place. The proof runs through
`ColSuperstandardEigen.jm_eigen_colSuperstandard'`, which is DOWNSTREAM of the statement, so
`SeminormalBaseExists.lean` restates and proves it there and the upstream declaration
delegates. The five files that did the work — `ColSuperstandardTableau`, `ColSuperstandardSYT`,
`ColSuperstandardEigen`, `SeminormalBaseExists`, `JucysMurphyOV` — did not exist when this bean
was written.

### What else closed with it

- **The §3b-cond carrier is inhabited.** `SnIsotypicSpechtSplit` has an instance for every
  char-0 field, so everything carrying `[SnIsotypicSpechtSplit ℚ]` is unconditional.
- **Identity I holds at every `n` with NO hypothesis.** `PlancherelSnDataGeneral`. The per-`n`
  `decide` instances (2…12) stay registered and stay the resolvable ones in range;
  `plancherelSnDataGeneral` is deliberately a `def`, since `PlancherelSnData` carries data and a
  competing general instance would make `h.parts` / `h.dim` resolution-dependent.

### Corrected as durable artifacts

- `docs/coordination/s5-so3-keystone.md` — "only the general-`n` discharge remains open" struck
  and replaced with the measurement.
- `docs/coordination/2026-06-29-ov-standard-basis-brick4.md` — its `identityB_general` axiom
  record (`sorryAx` present) annotated as accurate-when-written but superseded.
- `docs/audits/2026-08-25-ov-general-n-chain-is-closed.md` — the measurement.

**The lesson:** a HIGH-priority bean pointing at closed work costs the next agent a session.
This one nearly did. Beans go stale exactly as source-file `## Status` notes do, and the same
rule applies — the corpus is the source of truth, and the corpus means a source-rebuilt
`#print axioms`, not a docstring and not a bean. This bean's own caveat warned about this class
of error, about its own file.
