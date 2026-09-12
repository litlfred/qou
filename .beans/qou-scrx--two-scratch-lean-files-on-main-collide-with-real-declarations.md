---
# qou-scrx
title: Two scratch_*.lean files on main duplicate real declarations — 6 collisions, 0 importers
status: completed
type: task
priority: medium
created_at: 2026-08-30T08:00:00Z
updated_at: 2026-09-12T07:18:15Z
---

Found while running the `/prepare-merge` §4a duplicate-declaration gate on the
q-RH branch. **Not that branch's regression** — measured on `origin/main`
itself, and recorded here rather than fixed there because it is a different
domain.

## What

Two files in the **library** tree are scratch debris:

- `content/quantum-observable-universe/lean/QOU/scratch_pmass.lean` (20 lines)
- `content/quantum-observable-universe/lean/QOU/scratch_skein.lean` (29 lines)

Both were added in the **same** commit, `b4a0dc7138` (2026-08-29,
*"fix(coulomb-charge): Q is the STRONG coefficient"*), which is not about
either subject — the shape of a scratch file left behind rather than authored.

## Why it matters

Lean's environment is flat, so two modules declaring the same fully-qualified
name **cannot both be imported by anything**. These duplicate three real
declarations, six collisions in total:

| FQN | real home | scratch copy |
|---|---|---|
| `QOU.Substrate.ProtonMassSubstrateIdentity.proton_mass_substrate_match` | `QOU/Substrate/ProtonMassSubstrateIdentity.lean:41` | `scratch_pmass.lean:15` |
| `QOU.Torsion.SkeinGenerationContext` | `QOU/Torsion/skein_generation.lean:32` | `scratch_skein.lean:13` |
| `QOU.Torsion.skein_generation` | `QOU/Torsion/skein_generation.lean:48` | `scratch_skein.lean:21` |

`scratch_pmass.lean` also carries an `opaque F_Bor (q : ℝ) : ℝ` and a hardcoded
`m_e_codata : ℝ := 0.51099895069` — an opaque stand-in for a derived quantity
plus a bare CODATA literal, both of which the corpus's own disciplines are
against.

## Measured, so the disposition is cheap

- **Importers: 0.** Nothing in `content/` references either module by name
  outside the files themselves.
- **The gate is red on `main`, not on the branch that found it.** Run against
  `origin/main` and against the q-RH branch, `check-duplicate-decls --package
  qou` reports **63** duplicated FQNs on **both** — the branch adds zero. The
  skill's `--baseline 57` is therefore stale relative to main by 6, and all 6
  are these.

## Disposition

Delete both files. They have no importers, they are not cited by any content
block, and their declarations already exist in their proper modules. Then lower
`--baseline` from 57 toward 57 − 6 = 51 in
`.claude/skills/local/prepare-merge-auto.md` §4a, per the ratchet rule.

**Do not simply raise the baseline to 63** — that banks the collisions as
permanent and is the loosening the ratchet exists to prevent.

**Verify before deleting**, cheaply: write a two-line module importing both
`QOU.Torsion.skein_generation` and `QOU.scratch_skein` and confirm it fails with
`environment already contains`. The skill notes that two earlier counts of this
population were wrong while the compile never was.

---

## CORRECTION 2026-08-30 — only ONE of the two is a duplicate. I filed this wrong.

The entry above says both files "duplicate real declarations" and proposes
deleting both. **That is wrong for `scratch_skein.lean`, and I wrote it without
diffing the pairs** — from the collision report alone, which tells you two
modules declare the same name and nothing about whether they say the same thing.
That is precisely the mirror-drift lesson (`QOU.CRManifoldData`: each side
carrying an anti-vacuity condition the other lacks) applied to myself.

Diffed:

**`scratch_pmass.lean` IS a true duplicate.** Same `opaque F_Bor`, same three
CODATA defs, same `m_p_predicted`, same theorem with the same `norm_num` proof.
The canonical `QOU/Substrate/ProtonMassSubstrateIdentity.lean` differs only by
docstrings, which it has and the scratch does not. Safe to delete: 0 importers,
nothing lost.

**`scratch_skein.lean` is NOT a duplicate — it states a different proposition,
and arguably the more faithful one.**

| | canonical `QOU/Torsion/skein_generation.lean` | `scratch_skein.lean` |
|---|---|---|
| class field | `generation_top : Algebra.adjoin R (…) = ⊤` | `Hadron : Skein → Prop` + `hadron_is_polynomial : ∀ h, Hadron h → h ∈ adjoin (…)` |
| theorem | `∀ (h : Skein), h ∈ adjoin (…)` | `∀ h, ctx.Hadron h → h ∈ adjoin (…)` |
| proof | `rw [ctx.generation_top]; exact Algebra.mem_top` | `ctx.hadron_is_polynomial h h_hadron` |

The canonical one concludes membership for **every** element of the Skein
module; the scratch one restricts to **hadrons**, which is what the narrative
says (*"Every hadron admits a terminal Skein resolution"*).

**So deleting `scratch_skein.lean` would remove the copy closer to the prose.**
Do not do it as a cleanup. The right sequence is: fix the canonical module
first (below), then delete the scratch, then lower the baseline.

## Revised disposition

1. **Delete `scratch_pmass.lean`** — true duplicate, 0 importers. Removes 1 of
   the 6 collisions; baseline 57 → 56.
2. **Do not touch `scratch_skein.lean`** until `qou-skgn` (filed separately) is
   resolved, because the canonical module it collides with has its own defect.
3. The "lower the baseline toward 51" figure above assumed six safe deletions.
   Only one is safe today. **51 is not reachable yet.**

Still true and unchanged: 0 importers on both; both added in the same unrelated
commit `b4a0dc7138`; the gate is red at 63 on `origin/main` itself, so no branch
that merely rebases is responsible for it.

---

## SECOND CORRECTION 2026-08-30 — it is 8 colliding FQNs, not 3, and both my errors were the same mistake

**Compile-verified**, as this bean's own closing paragraph demanded. Two-line
modules importing each real module alongside its scratch twin:

```
import QOU.Substrate.ProtonMassSubstrateIdentity + import QOU.scratch_pmass
  → error: environment already contains
    'QOU.Substrate.ProtonMassSubstrateIdentity.F_Bor'
import QOU.Torsion.skein_generation + import QOU.scratch_skein
  → error: environment already contains 'QOU.Torsion.SkeinGenerationContext'
```

The collisions are real. But the **first** name Lean rejects is `F_Bor`, which
my table did not list — so I counted again, and the count is **8**:

| FQN | from |
|---|---|
| `…ProtonMassSubstrateIdentity.F_Bor` | `scratch_pmass` |
| `…ProtonMassSubstrateIdentity.m_e_codata` | `scratch_pmass` |
| `…ProtonMassSubstrateIdentity.m_mu_codata` | `scratch_pmass` |
| `…ProtonMassSubstrateIdentity.m_p_codata` | `scratch_pmass` |
| `…ProtonMassSubstrateIdentity.m_p_predicted` | `scratch_pmass` |
| `…ProtonMassSubstrateIdentity.proton_mass_substrate_match` | `scratch_pmass` |
| `QOU.Torsion.SkeinGenerationContext` | `scratch_skein` |
| `QOU.Torsion.skein_generation` | `scratch_skein` |

**The checker was right and my reading of it was wrong.** It reports all eight;
I built the original three-row table from `tail -10` of its output, which shows
only the last three FQNs. Nothing was wrong with the tool.

**Both of my errors on this bean are the same mistake — reading a fragment of a
tool's output as the whole of it.** The first was diffing nothing and taking the
collision list as evidence the files were duplicates; the second was taking the
tail of that list as the list. In a session that spent its length insisting on
measuring before quoting, this is the failure mode arriving through the one door
left open: *the measurement was run, and then only partly read.*

## What this changes about the disposition

The arithmetic in both earlier entries is void. Live figures:

- duplicate-decls total on `main`: **63**, baseline **57** → 6 over.
- these two files account for **8** of the 63.
- deleting **`scratch_pmass` alone** drains 6 → **57**, exactly the baseline.
- deleting **both** drains 8 → **55**, two *under* it, at which point the
  baseline should be lowered to 55 and not left at 57.

So the earlier "only 1 of 6 is safe today, 51 is not reachable" was wrong in
both directions: the safe deletion is worth **6**, not 1, and the reachable
floor is **55**, not 51.

**Unchanged, and still the reason not to delete `scratch_skein` yet:** it states
a *different* proposition from its twin (hadron-restricted, closer to the
narrative), and the canonical module it collides with has its own defect —
`qou-skgn`. Deleting `scratch_pmass` is safe now; `scratch_skein` waits on that
bean.


--------

## 2026-09-02 — RESOLVED, and this bean's count was stale by 4

### The "6 collisions" is wrong; it is 2

Measured directly (FQN → declaring files, over every `.lean` under `QOU/`):
**62 duplicated FQNs corpus-wide, of which exactly 2 involve a scratch file**,
both from `scratch_skein.lean`:

* `QOU.Torsion.SkeinGenerationContext`
* `QOU.Torsion.skein_generation`

**`scratch_pmass.lean` no longer collides at all.** It was namespaced one level
deeper — `QOU.Substrate.ProtonMassSubstrateIdentity.Scratch` — by the `qou-kfcl`
fix, and its own header comment records why. So this bean's collision table is
stale by 4: three FQNs × 2 files became one FQN pair.

That changes the *justification* for deleting `scratch_pmass.lean`, not the
conclusion. It is still debris and still goes — a hardcoded
`m_e_codata : ℝ := 0.51099895069`, an `opaque F_Bor`, and a "theorem" whose
`h_F : F_Bor q_0 = 4.469…` hypothesis hands it the very number it checks. But
deleting it is **hygiene, not a gate fix**, and should not be reported as
recovering collisions.

### The conflict with `qou-skgn`, resolved by doing the work rather than choosing

This bean said *"Delete both files."* `qou-skgn` said **do not** delete
`scratch_skein.lean` — it was the corpus's only hadron-restricted statement of
the claim.

Both are now satisfied, because `scratch_skein.lean`'s content was **preserved
and upgraded** before deletion. On inspection its `hadron_is_polynomial` field
*was* the conclusion and `skein_generation` merely projected it — the same
self-assuming defect `qou-skgn` is about, only hadron-restricted. The one thing
worth keeping was the `Hadron : Skein → Prop` quantifier.

So `QOU/Torsion/skein_generation.lean` now carries `HadronSkeinResolution` —
hadron-relative `base` and `resolve` (the resolution must *produce* hadrons, or
the induction could leave the class) — and derives `skein_generation_hadron`,
the narrative's actual sentence: *"every **hadron** admits a terminal Skein
resolution into a finite polynomial"*. Derived, not projected.

That is route (3)'s hadron half from `qou-skgn`, and it makes the scratch file
strictly redundant.

### Result

* duplicated FQNs **62 → 60**; scratch-related **2 → 0**.
* importers of either file, re-checked immediately before deletion: **0** and **0**.
* five theorems in `skein_generation.lean`, `lean`-direct exit 0, all
  `#print axioms`-clean, **0 `sorryAx`**.

### Still open

The `ℤ[q^{±1}]` coefficient ring — `R` is still an arbitrary `CommRing`. That
is the remaining half of `qou-skgn` route (3), recorded in the module docstring.


---

## RE-MEASURED 2026-09-12 — the subject is DONE; the ratchet half rests on a wrong premise and is unreachable here. CLOSING.

**Part 1 (delete both files): done, verified two independent ways.**

* Neither `QOU/scratch_pmass.lean` nor `QOU/scratch_skein.lean` is on
  `origin/main` (`git ls-tree -r origin/main`). Deleted by `9684dbd281c`
  (2026-09-03).
* An independent FQN scanner (namespace-stack walk over all 42,271 declarations
  under `QOU/`) reports **0 duplicated FQNs involving a scratch file**. That is
  the instrument-independent half of the finding and it agrees.

**The hadron restriction was PRESERVED, not lost.** This bean and `qou-skgn`
conflicted — one said delete, the other said keep `scratch_skein.lean` as the
corpus's only hadron-restricted statement. The fix resolved it by doing the
work: `HadronSkeinResolution` + `hadron_mem_adjoin_of_complexity_eq` now live in
`QOU/Torsion/skein_generation.lean`, derived rather than projected.

**Part 2 (lower `--baseline` 57 → 51) is NOT actionable, for three separate
reasons — recording them rather than silently dropping it:**

1. **Wrong file.** The bean says
   `.claude/skills/local/prepare-merge-auto.md §4a`. That file contains no
   `baseline` string and no §4a. The live gate is
   `.claude/commands/prepare-merge.md:558`.
2. **The arithmetic 57 − 6 is wrong.** It assumed 6 scratch collisions. The fix
   commit measured **2** (both from `scratch_skein.lean`; `scratch_pmass.lean`
   had already been namespaced one level deeper by the `qou-kfcl` fix and no
   longer collided). Its own message says "THE COUNT IN qou-scrx IS STALE BY 4".
3. **The gate's instrument is not in this checkout.**
   `scripts/check-duplicate-decls.ts` is PIN-HIDDEN — it lives in
   `folio-assistant` and was added *after* `.folio-assistant-pin`, which
   `scripts/bean-dangling-path-audit.py` cause 6 names explicitly. So the
   baseline cannot be re-measured here at all.

**And my own scanner is NOT a substitute.** It reports **131** duplicated FQNs
against the gate's baseline of 57 and the fix commit's 62 — a different
instrument, so its number must not be used to re-calibrate a threshold
belonging to a tool I cannot run. Proposing a `--baseline` edit off it would be
the detector-blindness trap, not a fix.

**What would settle it:** run
`bun run <folio-assistant>/scripts/check-duplicate-decls.ts --package qou` after
`scripts/setup-folio-assistant.sh`, and lower the baseline to whatever it
reports — from the gate's own instrument, never from a hand-rolled scan. Left
unfiled as a separate bean because it is one command on a pin advance, not a
tranche.
