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

## Next honest step

Formalize Young's seminormal base vector: for a shape `μ` over a char-0 field,
exhibit a nonzero `v ∈ S^μ` that is a simultaneous eigenvector of the JM elements
`X_s` with the prescribed content tuple. Standard route is the superstandard /
row-reading tableau `T₀` and its polytabloid, with the eigenvalue computation
from the JM action on polytabloids. Note the base ring is genuinely
`[Field k] [CharZero k]` — the `[CommRing k]` form is **false** (contents collide
mod `p`, eigenspaces merge), and that is already documented at the decl.

## Caveat for whoever picks this up

**Do not audit sorry-status from restored oleans.** The restored `lake-cache`
tree was missing `SpechtStandardBasisCore.olean` while carrying its own
dependents (built from an older source tree), so `#print axioms` reported a
phantom `sorryAx` that vanished after rebuilding the cone from source. Rebuild
the cone with `-DautoImplicit=false` (matching the lakefile) before believing any
axiom query.
