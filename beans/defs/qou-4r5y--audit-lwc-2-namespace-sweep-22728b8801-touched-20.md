---
# qou-4r5y
title: 'AUDIT: LWC-2 namespace sweep (22728b8801) touched 20+ Lean files; 2 confirmed breaks (ext_toSsyt, Partition.*) — audit the rest for stripped type-name prefixes'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-07T17:38:02Z
updated_at: 2026-10-04T15:16:29Z
parent: qou-5vkl
---


## 2026-08-07 — a THIRD break found; raise the priority

PR #4698 repaired two known breaks (`SYTEnumerationFintype` `ext_toSsyt`,
`DeltaLambdaSignRule` 9 × `Partition.`) and, once the second was fixed,
immediately surfaced a **third** in `PartitionNatBridge.lean:52`: a call to
`Partition.ext'`, a declaration that exists nowhere in the file's history.

The pattern to note for this audit: **breaks mask each other.** Because
`DeltaLambdaSignRule` did not compile, nothing downstream of it was ever
reached, so `PartitionNatBridge`'s own error was invisible. Auditing the
remaining ~20 sweep-touched files by eye is therefore not enough — each
repair can expose a new error behind it. The audit must **build the full
dependents cone after each fix**, not just re-read the diffs.

Verified-clean so far (41-module cone, lean-direct, `FAILED: none`): the
`SYTHookFormula` / `IdentityIHLFBridge` / `SytSmallShapeCountsLarger` /
`PartitionNatBridge` / `SYTCornerListConnection` / `PartitionHookProductBridge`
cones. The rest of the sweep's 20+ files remain unaudited.

## 2026-08-08 — root-cause map after a second pass; 11 casualties found, 1 unresolved

Follow-up PR (branch `claude/agent-4685-phase0-collision-itnixj`) found **two more**
LWC-2 casualties beyond the three fixed in #4698, confirming the masking pattern
above. Running total of stripped **type**-prefix regressions: **11**.

| # | File | Decl | State |
|---|---|---|---|
| 1 | `Mathlib/SYTEnumerationFintype.lean:710` | `ext_toSsyt` call site | fixed #4698 |
| 2–10 | `BraidKnot/DeltaLambdaSignRule.lean` | 9 × `Partition.*` | fixed #4698 |
| 11 | `BraidKnot/PartitionNatBridge.lean:34` | `Partition.ext'` | **fixed here** |
| 12 | `BraidKnot/SpechtStandardBasisCore.lean:325` | `Triangular.linearIndependent` | **fixed here (partial — see below)** |

**#4698 mis-diagnosed #11.** Its commit `8149c611` asserted `Partition.ext'` "exists
nowhere in the file's history" and worked around it by declaring a new
`Partition.ext`. The declaration existed at `PartitionNatBridge.lean:34` the whole
time with its `Partition.` prefix stripped. The error came from grepping
`DeltaLambdaSignRule.lean` — the wrong file — and treating the null result as proof
of absence. **Lesson for the rest of this audit: locate the declaration before
concluding it is missing; a null grep is only as good as the file you ran it on.**

Because `PartitionReindex` (which calls it by the full name
`PartitionNatBridge.Partition.ext'`) was not in #4698's verified cone, the miss
survived the merge. **The verification cone must be the full dependents set, not
just the modules under edit.**

### Still open — the Specht cluster (NOT a namespace strip)

Restoring `Triangular.linearIndependent` cleared the field error but
`SpechtStandardBasis` still fails:

```
SpechtStandardBasis.lean:125:85: error: unsolved goals
SpechtStandardBasis.lean:126:40: error: failed to synthesize
```

in `specht_finrank_eq_numSYT` (`Module.finrank_eq_nat_card_basis … ; rfl`). This is a
**proof-level / Mathlib-API break**, a different bug class from the sweep. Four more
modules fail only transitively behind it: `JucysMurphy`,
`SnWedderburnPartitionBridge`, `OVTopAssembly`, `RSKBurnsideDischarge`.

`RSKBurnsideDischarge` failing matters for the burnside roadmap — it is the RSK side
of the discharge. Fixing `specht_finrank_eq_numSYT` is the next unit of work here.

### Verified green (42-module cone, lean-direct, `FAILED: none`)

`PartitionHookProductBridge`, `PartitionReindex`, `PartitionNatBridge`,
`SYTHookFormula`, `IdentityIHLFBridge`, `SytSmallShapeCountsLarger`,
`StandardYoungTableau` (now sorry-free) and their full cones.

## 2026-08-08 (later) — Specht cluster CLEARED; the blocker was not a sweep casualty

`qou-0sc0` closed. `SpechtStandardBasis.lean` carried `omit [CharZero k] in` on
`specht_finrank_eq_numSYT` while its proof applies `standardBasis`, which genuinely
takes the instance — so `CharZero k` was unsynthesizable at the application and the
file did not compile. **Different bug class from the sweep**, so the LWC-2 casualty
count stays at 12.

Tried preserving the generality first (`omit` on `standardBasis` too) — does not
work, the def really needs it. Dropped the omit; that is what the existing proof
supports. Removing the hypothesis on the merits is still open (the
standard-polytabloid basis exists over any field) but needs the `CharZero` uses
inside `standardBasis`'s inputs traced, not an annotation change.

**Unblocked 5 modules** that were failing only transitively: `SpechtFinrankWired`,
`JucysMurphy`, `SnWedderburnPartitionBridge`, `OVTopAssembly`, and
`RSKBurnsideDischarge` — the RSK side of the burnside discharge.

### Sorry-provenance correction (verified, not inferred)

`SpechtFinrankWired.specht_finrank_eq_numSYT_wired` and
`SpechtStandardBasis.specht_finrank_eq_numSYT` are **axiom-clean**
(`[propext, Classical.choice, Quot.sound]`). `OVTopAssembly`'s table was blaming
its `rank` row's `sorryAx` on that brick with "sorry-path = spanning/straightening
only" — false, and corrected. `OVTopAssembly.sum_numSYT_sq_eq_factorial` does still
carry `sorryAx`, from the two live sorries the other rows already name correctly:
`SnWedderburnPartitionBridge:234` (`sn_rational_specht_split`) and
`JucysMurphy:840` (`centralC2_acts_by_contentSqSum`).

So the burnside chain's remaining sorry-debt is those two — **not** the
spanning/straightening stub, which is not load-bearing for the rank input.

### Cone status: 55 modules, `FAILED: none`

## 2026-08-08 — verification-method lesson (from PR #4702's caveat)

PR #4702 (parallel session on the same Specht files) warned:

> *Do not audit sorry-status from restored oleans. The restored `lake-cache` tree
> was missing `SpechtStandardBasisCore.olean` while carrying its own dependents
> (built from an older source tree), so `#print axioms` reported a phantom
> `sorryAx`... Rebuild the cone with `-DautoImplicit=false` (matching the lakefile).*

**The caveat is legitimate and applied to my method**: my cone builder was not
passing `-DautoImplicit=false` (both `lakefile.toml` files set it), and I was
building against the restored cache.

Re-ran every axiom claim after **wiping the QOU olean tree entirely** and rebuilding
56 modules from source with the flag. **All results identical** — nothing moved. So
the claims stand, but they now rest on a clean build rather than a restored one.

**Standing rule for this audit** (third method lesson, joining "locate the decl
before declaring it absent" and "verify the full dependents cone"): *an axiom query
is only as trustworthy as the olean tree under it.* Before publishing a sorry-status
claim, rebuild the cone from source with the lakefile's flags — a restored cache can
report both phantom sorries and phantom cleanliness.

- **Round 94 (`litlfred/qou#8424`)**: Advanced in `feat/round94-parity-level-lever1depth2-tauclosed-chainlog-43c1` (Commit 1 `c1698951b30460bb111c1e97552482f0b0622bd0`, Commit 2 `5a166eac86b999ab31c9bdd39f5908e1c848e122`, probe sha256 `1438398dfd335d3f6e9ebdcaa8df8fdc4613a507b4d480b0c9dde22e4b3c8bcb`).
