---
# sv8b
title: 'GAP: seminormalVector_base_exists — the last labelling sorry (brick-5 OV)'
status: todo
type: task
priority: high
created_at: 2026-08-07T22:10:00Z
updated_at: 2026-08-07T22:10:00Z
---

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
