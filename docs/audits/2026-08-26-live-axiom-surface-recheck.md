# The live axiom surface, re-checked against the corpus — and the measurement trap underneath it

**Bean:** `qou-8s7o`. **Date:** 2026-08-26.

Follow-up to `qou-mame`, which discharged `lobachevsky_pi_div_four_eq_half_catalan`
— an axiom classified **External / cited / deep** in
[`2026-06-03-lean-axiom-tractability-triage.md`](2026-06-03-lean-axiom-tractability-triage.md)
— in about twenty lines, using a bridge that had been in this repository for weeks.
That bucket was populated by *reading each axiom's own docstring*. This audit
re-checks it against the corpus instead.

The headline is not the one I expected. Only two of the twenty-three live axioms
have any same-shaped theorem elsewhere in the corpus, and neither is a free win.
What the audit actually turned up is a **defect in the measurement instrument**,
and three ways I mis-measured while finding it.

---

## 1. The bucket no longer maps to the tree: 58 → 23

The triage doc sorts **58** axioms into "External / cited / deep". The live tree
carries **23 axioms** in total, across every bucket
(`scripts/lean-assumption-surface.py`, 2207 files, 0 `sorry` / 0 `sorryAx` /
0 `true_vacuity`, 1 `native_decide`):

| area | axioms |
|---|---|
| HeckeAlgebra | 8 |
| MathlibExt | 5 |
| BraidKnot | 4 |
| Mathlib | 2 |
| AppendixSurreals, Archimedean, Hecke, IwahoriHecke | 1 each |

So most of what that document triages has since been discharged or removed. **Do
not quote its bucket sizes as a description of the current tree** — including the
"57 remaining" figure in my own bean `qou-8s7o`, which inherited the error.

## 2. Corpus-grep of all 23: two hits, both in the SDP ladder, neither free

Every axiom's name-stem was greped across the whole QOU tree for a `theorem` or
`lemma` of the same stem, excluding its own file. Twenty-one have none. Two do,
and both are **deliberate refinement layers**, not forgotten discharges:

- `SDPRankUniqueness` (`SDPRealUniqueness.lean:586`) is shadowed by
  `SDPRankUniqueness_proven_via_rank_equality` (`SDPRankEquality.lean:720`),
  which has an identical signature and is proved.
- `strict_complementarity_unique_axiom` (`SDP.lean:286`) is shadowed by four
  proved `real_strict_complementarity_unique*` theorems in `SDPRealUniqueness.lean`.

In both cases the proved version lives **downstream** of the axiom
(`SDPRankEquality` imports `SDPRealUniqueness` imports `SDP`), so it cannot
replace it in place without a cycle.

**And swapping would not reduce anything.** Measured by proof term:

```
ofSlater_proven            -> [propext, Classical.choice, Quot.sound,
                               SDPRankUniqueness]                          1 axiom
ofSlater_via_rank_equality -> [propext, Classical.choice, Quot.sound,
                               affine_slater_rigidity,
                               strict_complementarity_kernel_disjoint]     2 axioms
```

`SDPRankEquality`'s own §5 says it "replaces the dependency on `SDPRankUniqueness`".
That is true as stated and easy to read as a reduction; it is a **decomposition**.
It trades one monolithic assumption for two more atomic ones — a reasonable goal,
since atomic assumptions are closer to something Mathlib might one day supply, but
the assumed-mathematics count goes **up, not down**. Nothing outside the two SDP
modules consumes either chain, and **no module imports `SDPRankEquality` at all**.

## 3. Reclassification: much of the surface is interface, not deep mathematics

Eleven of the twenty-three sit in a file that also declares `opaque`. That is a
co-location proxy rather than a per-axiom proof, but the pattern is clear where
it was checked directly: `IwahoriHecke/MarkovTrace.lean:77` declares
`noncomputable opaque markovTrace`, and `HeckeAlgebra/MarkovTrace.lean` declares
`opaque heckeStab`. `MarkovTrace_cyclic` and `markovTrace_linear` assert
cyclicity and linearity **of an opaque symbol**.

Such an axiom is not blocked on Mathlib and is not deep — it is **unprovable by
construction**, and will stay so until the opaque symbol is bridged to something
with content. Filing it as "External / cited / deep" invites exactly the search I
ran, which cannot succeed.

There is a concrete bridge target: `MathlibExt/MarkovTrace.lean:117` defines
`markovTrace` as a real `noncomputable def` over `HeckeRep`/`BraidWord`. So the
corpus carries **two `markovTrace`s, one opaque and one concrete, with nothing
connecting them** — the same unbridged-definitions hazard that held `catalan_G`
apart from `Cl_2 (π/2)` until `qou-mame`, and the guard's own Catalan comment
already names that shape as a live hazard. Bridging them is the real question
behind the Hecke cluster, and it is a corpus-internal one.

## 4. The measurement instrument was unsound: `#print axioms` over a mixed-vintage cache

While measuring §2, both SDP cones reported a fourth axiom,
`PosSemidefDiagZero.entry_sq_le_diag_mul_axiom` — **which does not exist in the
source.** `grep` finds no such declaration anywhere in `content/`;
`PosSemidefDiagZero.lean:140` proves `Matrix.PosSemidef.entry_sq_le_diag_mul` as
a **theorem**.

The olean was built **2026-06-09**, when the same result was an axiom. Rebuilding
that single module from source removed the phantom from both cones — the direct
experiment, not an inference.

`#print axioms` reads the loaded environment, which comes from `.olean` files. In
a restored container those are a **mixed-vintage cache**: QOU olean build dates on
this tree span **2026-06-09 to 2026-08-26**, with 556 from 2026-07-02 alone.
`scripts/lean-axiom-guard.py` assumes its modules are *built*; it never checks
they are built **from the current source**.

**Direction of harm.** Here the stale cache was *pessimistic* — it over-reported
assumed mathematics, which is the safe direction. The identical mechanism runs the
other way: a cached olean can report `clean` for a declaration whose current source
has regressed, and the gate would stay green.

**Scope, so this is not overstated.** The guard's own 199-module cone is dated
2026-08-25/26, i.e. rebuilt in this container. Tonight's guard runs were *not*
measuring a June cache, and the `qou-mame` verification stands on its own terms —
both changed modules were explicitly rebuilt before being measured. The defect is
that nothing *enforces* that; it held by luck.

**Fix:** [`scripts/lean-rebuild-cone.py`](../../scripts/lean-rebuild-cone.py)
rebuilds a set of modules and their transitive QOU cone in topological order via
`lean`-direct, so verdicts are about the source. `--from-guard` takes the axiom
guard's registry as roots (15 roots → 199 modules). It uses `lean -o` rather than
`lake build`, which would evict the restored oleans (bean `qou-r13s`).

## 5. Three artifacts I hit while measuring this — all in one investigation

Recorded because each looked like a finding and each was an artifact of the
environment, and because the corpus already warns about the first one in a
different context.

1. **Shallow clone.** `git log --name-only` reported that all 2207 QOU `.lean`
   files changed since the cache seed. The clone has **17 shallow grafts**;
   `fed69b1c4d` sits on the boundary, so `git rev-list --parents` shows it as a
   root and its whole tree as "new files" — while `git cat-file -p` shows it has
   two parents. AGENTS.md already flags this exact trap for
   `witness.scriptCommitSha` ("a sha can be missing merely because the history was
   never fetched"); it applies to file-change measurement too.
2. **Merge-commit inflation.** `--name-only` on a merge prints the combined diff.
   And `--no-merges` did **not** exclude the offender, because rebase-merge
   flattens a branch's merge commit into a single-parent commit that keeps the
   words "Merge pull request" in its subject.
3. **Clone-time mtime.** 845 of 1046 QOU oleans are "older than their source".
   That is exactly the set restored from the tarball: a checkout stamps every
   source with the clone time while tar preserves the oleans' build times. The
   number is a description of the restore, not of staleness. **mtime cannot
   answer this question** — which is why the fix rebuilds rather than compares.

## Verdict

The bucket was not full of missed `qou-mame`s. One such axiom existed and is
closed. What remains splits into interface axioms over `opaque` symbols (§3,
needing a corpus bridge, not a Mathlib PR), a deliberate SDP decomposition ladder
(§2, where "replaces" means "decomposes"), and a genuinely external residue.

The reusable result is §4: **a `#print axioms` verdict is only as current as the
olean it was read from**, and until now nothing in the pipeline said so.

## Cross-refs

- [`2026-06-03-lean-axiom-tractability-triage.md`](2026-06-03-lean-axiom-tractability-triage.md) — the bucket, corrected in place by `qou-mame`
- [`scripts/lean-axiom-guard.py`](../../scripts/lean-axiom-guard.py) — the gate this hardens
- [`scripts/lean-assumption-surface.py`](../../scripts/lean-assumption-surface.py) — the 23-axiom measurement
- [`scripts/lean-rebuild-cone.py`](../../scripts/lean-rebuild-cone.py) — the fix
