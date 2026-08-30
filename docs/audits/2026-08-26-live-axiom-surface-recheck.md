# The live axiom surface, re-checked against the corpus — and the measurement trap underneath it

**Bean:** `qou-8s7o`. **Date:** 2026-08-26.

Follow-up to `qou-mame`, which discharged `lobachevsky_pi_div_four_eq_half_catalan`
— an axiom classified **External / cited / deep** in
[`2026-06-03-lean-axiom-tractability-triage.md`](2026-06-03-lean-axiom-tractability-triage.md)
— in about twenty lines, using a bridge that had been in this repository for weeks.
That bucket was populated by *reading each axiom's own docstring*. This audit
re-checks it against the corpus instead.

> **How to read the claims below.** They are not all the same kind of thing, and
> putting them side by side flatters the weaker ones. Tiers used throughout:
>
> - **PROVED** — a sorry-free Lean theorem, axioms checked with `#print axioms`.
>   Only §3's Riesz equivalence and the results in `qou-k5jt` are this. They are
>   also the only part of this audit that was not already in the corpus.
> - **MEASURED** — the output of running something: `#print axioms` on a rebuilt
>   cone, a build that exits 0 or 1, a script's count. §1, §2's proof-term
>   comparison, §4's phantom-axiom experiment, §5.
> - **GREPPED** — a pattern count over source text. §2's same-stem search and
>   §3's "eleven of twenty-three" are this, and a grep supports a claim about
>   *what the text says*, never about what is provable. §3 records what happened
>   when that distinction was ignored.
>
> The one claim here that is none of the three is the degeneracy note: that the
> axioms do not *exclude* `tr_M ≡ 0` is proved, but their *consistency* is a
> statement about models and is not established anywhere in this work.

The headline is not the one I expected. Only two of the twenty-three live axioms
have any same-shaped theorem elsewhere in the corpus, and neither is a free win.
What the audit actually turned up is a **defect in the measurement instrument**,
and three ways I mis-measured while finding it.

---

## 1. The bucket no longer maps to the tree: 58 → 23

The triage doc sorts **58** axioms into "External / cited / deep". The
`QOU/` **library** carries **23 axioms** in total, across every bucket
(`scripts/lean-assumption-surface.py`, 2207 files, 0 `sorry` / 0 `sorryAx` /
0 `true_vacuity`, 1 `native_decide`):

| area | axioms |
|---|---|
| HeckeAlgebra | 8 |
| MathlibExt | 5 |
| BraidKnot | 4 |
| Mathlib | 2 |
| AppendixSurreals, Archimedean, Hecke, IwahoriHecke | 1 each |

So most of what that document triages has since been discharged or removed.

> **🛑 SCOPE, corrected 2026-08-26. "23" is the `QOU/` LIBRARY, not the corpus.**
> Content blocks carry sibling `.lean` files outside that library, and they hold
> the large majority of the axioms: measured **22 in the library against 198
> corpus-wide** (3185 files), i.e. 176 live outside the scope every figure in this
> audit uses.
>
> The **comparison in this section is still valid** — the triage doc explicitly
> snapshots "every `axiom` declaration in
> `content/quantum-observable-universe/lean/QOU/`", so 58-vs-23 is scope-matched.
> What was wrong is the phrase "the live tree", which reads as the corpus and is
> off by an order of magnitude. The same applies to `qou-k5jt`'s "surface 23 → 22":
> true of the library, and 198 → 197 of the corpus.
>
> `scripts/lean-assumption-surface.py` now prints its scope and the corpus figure
> on every run, because a tool that silently reports a subtree invites exactly this.
> (Adding that check immediately caught a second error in it: the corpus walk was
> including `.lake/`, reporting 418 axioms over 11198 files — mostly Mathlib's,
> counted as ours.)

 **Do
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

> **These numbers were first obtained by the method §4 condemns, and have since
> been re-measured properly (2026-08-26).** The first run resolved the two
> declarations under `…SDPRealUniqueness.SDPSlaterUniqueness.ofSlater_proven` and
> `…SDPRankEquality.SDPSlaterUniqueness.ofSlater_via_rank_equality`. After
> rebuilding the SDP cone from source those names **do not exist**: the current
> source declares them one namespace higher, without the `SDPSlaterUniqueness`
> segment. So the original measurement read an olean built before that move —
> a third instance of §4, and the first one committed by this audit against its
> own evidence.
>
> Re-measured against a rebuilt SDP cone (6/6), at the correct current names, **the comparison is unchanged**:
> `ofSlater_proven` carries one axiom, `ofSlater_via_rank_equality` and
> `SDPRankUniqueness_proven_via_rank_equality` carry two. The conclusion stands;
> the route to it did not, until now.

`SDPRankEquality`'s own §5 says it "replaces the dependency on `SDPRankUniqueness`".
That is true as stated and easy to read as a reduction; it is a **decomposition**.
It trades one monolithic assumption for two more atomic ones — a reasonable goal,
since atomic assumptions are closer to something Mathlib might one day supply, but
the assumed-mathematics count goes **up, not down**. Nothing outside the two SDP
modules consumes either chain, and **no module imports `SDPRankEquality` at all**.

## 3. Interface vs. deep — and the inference in this section that was wrong

**This section originally concluded that `markovTrace_linear` was "unprovable by
construction". It is now a theorem** (`qou-k5jt`), and both halves of how it got
that wrong are worth keeping, because they are different mistakes.

**The wrong inference.** The argument was: `markovTrace` is `opaque`, an axiom
about an `opaque` symbol cannot be proved, therefore not a Mathlib gap but a
construction gap. The middle step does not follow. What matters is not whether
the *function* is opaque but whether its *argument type* has content.
`HeckeElement n` is not opaque — it abbreviates `EuclideanSpace ℝ (Fin n!)` — so
by Riesz every ℝ-linear functional on it is `⟪w, ·⟫`. Carrying the trace as its
weight vector instead of as an opaque function is the same class of functionals,
and makes linearity provable. Proved both directions, sorry-free:
`QOU.HeckeAlgebra.isLinearMap_iff_exists_weight`.

That the `→` direction had to be *proved* rather than cited is the point. Stated
in prose it licenses the change; only the proof rules out the change having
silently narrowed the admissible traces.

**The wrong citation.** Separately, and more embarrassingly for a section arguing
from specifics: the evidence offered was
`IwahoriHecke/MarkovTrace.lean:77`'s `noncomputable opaque markovTrace`. But
`markovTrace_linear` lives in `HeckeAlgebra/Common.lean` and is about
`HeckeAlgebra.markovTrace`, a *different* declaration in a different namespace.
The claim happened to be true of the intended one — `Common.lean:104` was
`opaque` too — but the line cited to support it was about something else. In a
corpus where "two declarations sharing a glyph" is a named recurring hazard,
citing the wrong one inside the argument that the corpus has too many
`markovTrace`s is its own small demonstration.

**What survives.** `MarkovTrace_cyclic` is the genuine case and is untouched: it
constrains the trace against `heckeMul`, which *is* opaque, so it is not
expressible from the linear-algebra layer and stays an axiom. The reclassification
holds for that one. It does not hold as a blanket claim about the eleven — that
figure is a **co-location count** (axioms declared in a file that also declares
`opaque`), never a per-axiom verdict, and the one member of it examined closely
turned out to go the other way.

There is still a concrete bridge target: `MathlibExt/MarkovTrace.lean:117` defines
`markovTrace` as a real `noncomputable def` over `HeckeRep`/`BraidWord`. The corpus
carries **several `markovTrace`s with nothing connecting them** — the same
unbridged-definitions hazard that held `catalan_G` apart from `Cl_2 (π/2)` until
`qou-mame`, and which the guard's own Catalan comment already names. Bridging them
remains the real question behind the Hecke cluster, and it is corpus-internal.

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

> **🛑 CORRECTION (same day). This section first said `lean-axiom-guard.py`
> "assumes its modules are built; it never checks they are built from the current
> source". That is FALSE, and it is the sharpest error in this audit — an audit
> about not asserting what you have not checked.**
>
> The guard has had a freshness gate since `fed69b1c4d`, before this work started.
> `check_freshness` walks the transitive QOU import cone of every registry module
> and refuses to report on a missing or stale olean. Its docstring even records a
> prior incident of this exact class (2026-08-15: all-match reported against
> 9-day-old oleans while five underlying sorries had been closed upstream).
>
> I did not read the script I was auditing before describing what it does not do.
> The corpus-grep discipline says the source is the authority over any claim
> *about* it; I applied that to the axioms and not to the tool.
>
> **The real gap is narrower and still real.** The gate covers the guard's own
> registry cone. It does not cover an **ad-hoc `#print axioms` probe written by
> hand against some other module** — which has no gate at all. Both stale readings
> below were exactly that: my own probes, outside the registry.

**Direction of harm.** Here the stale cache was *pessimistic* — it over-reported
assumed mathematics, which is the safe direction. The identical mechanism runs the
other way: a cached olean can report `clean` for a declaration whose current source
has regressed, and the gate would stay green.

**Scope, so this is not overstated.** The guard's own 199-module cone is dated
2026-08-25/26, i.e. rebuilt in this container. Tonight's guard runs were *not*
measuring a June cache, and the `qou-mame` verification stands on its own terms —
both changed modules were explicitly rebuilt before being measured. The defect is
that nothing *enforces* that; it held by luck.

**Fix — and it already existed.** I wrote a `lean-rebuild-cone.py` for this and
then found [`scripts/lean-direct-cone.sh`](../../scripts/lean-direct-cone.sh)
(driver [`lean_cone_build.py`](../../scripts/lean_cone_build.py), 374 lines),
which does the same job better: it skips modules already up to date, builds in
parallel with progress and ETA, has `--keep-going` with dependency propagation and
`--all` for a whole-corpus survey, and — as its own docstring predicts — includes
the **root aggregator module** that a naive `QOU/`-directory walk misses. Measured
head to head on the guard's registry: **205 modules against my 199**, and **318 s
against 1572 s**. Mine was deleted. Compose it with the guard:

```sh
scripts/lean-direct-cone.sh $(scripts/lean-axiom-guard.py --print-modules)
```

`scripts/lean-verify-cone.sh` (bean `qou-fjcd`) is the consumer-side form of the
same trap, and its docstring records a 2026-08-08 incident in which a PR claimed
"lean-direct exit 0 on every consumer" against oleans that still held the removed
instances. That is this audit's §4, already found, already tooled.

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
   number is a description of the restore, not of staleness.

   > **Corrected.** This item first concluded "**mtime cannot answer this
   > question** — which is why the fix rebuilds rather than compares." The first
   > half is wrong. Raw mtime cannot, but `lean-axiom-guard.py::_effective_source_time`
   > already answers it: for a clean file it uses the **commit time** of the last
   > commit touching it, which is stable across clones, and falls back to mtime only
   > for a **dirty** file, where a local edit is precisely the case being guarded and
   > no commit can be trusted. Its docstring records the same measurement I
   > re-derived here (2026-08-15: mtime flagged 15 modules stale while `lake build`,
   > which hashes content, replayed all 3285 jobs as up to date).
   >
   > So the artifact is real — mtime alone is useless here — but the conclusion drawn
   > from it was not, and the corpus had already solved it. `lean-rebuild-cone.py`
   > earns its place as the **remediation** tool (the gate detects staleness; it does
   > not fix it, and `lake build` would evict the restored cache), not as a detector.

## Verdict

The bucket was not full of missed `qou-mame`s. One such axiom existed and is
closed. What remains splits into interface axioms over `opaque` symbols (§3,
needing a corpus bridge, not a Mathlib PR), a deliberate SDP decomposition ladder
(§2, where "replaces" means "decomposes"), and a genuinely external residue.

The reusable result is §4, in its corrected form: **a `#print axioms` verdict is
only as current as the olean it was read from.** The guard already knew that and
gates its own registry. What has no gate is a hand-written probe outside it — which
is what produced both stale readings here, including the one this audit used as
evidence for its own §2.

## Cross-refs

- [`2026-06-03-lean-axiom-tractability-triage.md`](2026-06-03-lean-axiom-tractability-triage.md) — the bucket, corrected in place by `qou-mame`
- [`scripts/lean-axiom-guard.py`](../../scripts/lean-axiom-guard.py) — the gate this hardens
- [`scripts/lean-assumption-surface.py`](../../scripts/lean-assumption-surface.py) — the 23-axiom measurement
- [`scripts/lean-direct-cone.sh`](../../scripts/lean-direct-cone.sh) + [`lean_cone_build.py`](../../scripts/lean_cone_build.py) — the remediation tool, which already existed
- [`scripts/lean-verify-cone.sh`](../../scripts/lean-verify-cone.sh) — the consumer-side form (bean `qou-fjcd`)
