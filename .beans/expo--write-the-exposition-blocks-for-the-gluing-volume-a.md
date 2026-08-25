---
# expo
title: 'Write the exposition blocks for the gluing / volume / surreal-transfer arc'
status: in-progress
type: task
priority: high
tags:
    - content
    - exposition
    - hyperbolic-volume
parent: m015
created_at: 2026-08-10T05:00:00Z
updated_at: 2026-08-10T05:00:00Z
---

**The arc has proved results with no paper presence.** That is the opposite of the usual
gap and worth closing deliberately.

Checked 2026-08-10: **no content block cites any of these modules** —
`FiveTwoComplexPentagon`, `KummerRadial`, `KummerUnitCircle`, `KummerDilogHalf`,
`IdealTetLawOfSines`, `RivinConcavity`, `MathlibExt/IdealTriangulation`,
`FiveTwoVolumeConstant`, `FigureEightTriangulation`, `FlatTetrahedra`,
`GeneratedGluing`, `HyperrealLimitTransfer`.

Material wanting exposition, all of it Lean-proved and sorry-free:

- the **5₂ saddle sum rule** (proved; was "verified to 80 dps, unproved")
- **Kummer's identity** for general `z`, and the law of sines for the ideal tetrahedron
- **Rivin concavity** — `Λ″ = −cot`, the Hessian, strict concavity on the line
- the **ideal-triangulation volume functor**, `rotate_angles` / `volume_rotate`
- **27 shape fields** with minimal polynomials and discriminants, and **312 generated
  Lean proofs** of edge gluing equations across 19 manifolds (bean `glnl`)
- the **flat-shape result**: the edge equations do **not** detect hyperbolicity;
  positivity does (bean `m015`, `QOU/Knot/FlatTetrahedra.lean`)
- the **ℝ\* limit transfer** and the two-valued-birthday defect (beans `hypr`, `bday`)

## ⚠ Precedent that shapes how to do this

`content/quantum-observable-universe/mass-theory/thurston-volume-additivity.md` already
asserted *"Flat tetrahedra contribute zero volume"* and *"Torus knots … hyperbolic volume
vanishes identically"* — while its Lean sidecar **axiomatised both**. Prose ran **ahead**
of the formalisation and the sidecar papered over the gap with an `axiom` plus a false
blocker note. Both are now discharged.

So when writing these blocks: **wire `lean.ref` to the real theorem as you write the
prose**, not afterwards. A block whose sidecar axiomatises its own claim is worse than no
block, because `status: "verified"` then means nothing.

## Scope discipline to carry into every block

Say plainly, in each block, that none of this establishes any triangulation is a
triangulation *of* a knot complement (Thurston hyperbolisation + Mostow rigidity, needing
hyperbolic 3-manifolds neither Mathlib nor QOU has), and that no volume conjecture is
touched. Route 75 gate G6 is the wording to reuse.

**And say that the mathematics is not new.** Thurston, Neumann–Zagier, Neumann–Reid,
`snap`, Garoufalidis–Goerner–Zickert — see bean `ptlm`. What is new is the corpus's
formalisation and gating, which is worth exposition on its own terms and must not be
dressed up as a mathematical contribution.

---
**2026-08-10 — first three blocks written, and a trap that would have made them invisible.**

Blocks added to `mass-theory/`, each with `lean.ref` wired to a real, built, sorry-free
theorem **as the prose was written** (the discipline this bean demands):

| block | `lean.ref` |
|---|---|
| `thm:flat-tetrahedron-zero-volume` | `QOU.Knot.FlatTet.BlochWigner_lob_ofReal` |
| `thm:gluing-equations-do-not-detect-hyperbolicity` | `QOU.Knot.FlatTet.edge_equations_do_not_detect_hyperbolicity` |
| `prop:hyperbolic-knot-shape-fields` | `QOU.Knot.GeneratedGluing.K61.edge_0` |

All three refs verified to resolve via `lake env lean` before the blocks were committed.
`validation: "leanok"`.

### ⚠ THE TRAP: dropping files in the directory is not enough

`validateObjects` loads `blockNames ?? discoverManifests(dir)`, and `blockNames` comes
from the **chapter manifest** (`<dir>/<dirname>.ts`). A block file sitting in the
directory but absent from `mass-theory.ts` is **never loaded by any checker** — it looks
present, and is invisible.

I nearly shipped exactly that. Caught by a positive control rather than by reading:
removing the `lean` block from one `.ts` produced **no** warning, when it should have
produced "no Lean declaration yet". After registering the three blocks in
`mass-theory.ts` the same experiment produced

    ⚠ [flat-tetrahedron-zero-volume]: thm:flat-tetrahedron-zero-volume: no Lean declaration yet

and the issue count moved 4 → 5, returning to 4 on revert.

> **A validator reporting "✓ Valid" over your new file proves nothing until you have made
> it fail on purpose.** This is the same failure the sibling detangler bug had — *"a `]`
> inside a manifest comment hid 45 blocks from the checker"* — reached from the other
> direction.

### ⚠ CORRECTION to a claim in merged PR #4891

That PR, and the prepare-merge report, said `content_validate` "could not run … a
cross-repo wiring problem in this container". **That was wrong, and it was my
invocation.** `content/pipeline/validate.ts` uses `resolve(import.meta.dir, "../..")` —
`import.meta.dir` is a **Bun** API, `undefined` under `npx tsx`, which produced exactly
the `TypeError [ERR_INVALID_ARG_TYPE]: paths[0]` I reported as a wiring failure.

Run with `bun run scripts/run-validate.ts` it works, resolves the platform
(`c9ae256`), and passes: **`✓ Valid — 4 issue(s)`**, all four pre-existing and none in
this arc's blocks. The gate was fine; the caller was not. #4891 is merged and cannot be
amended, so the correction lives here.

### Still to write

The 5₂ saddle sum rule; Kummer's identity and the ideal-tetrahedron law of sines; Rivin
concavity; the volume functor and `rotate_angles`/`volume_rotate`; the ℝ* limit transfer
and the two-valued-birthday defect (beans `hypr`, `bday`). Each needs a manifest entry as
well as a file — see the trap above.

---
**2026-08-10 — re-validated against a platform 144 commits newer. Delta still zero, and
several checks I relied on were broken at the old baseline.**

The blocks were first validated against folio-assistant `c9ae256`. The platform was **144
commits behind**, and the gap includes fixes to the very machinery those checks used:

| platform commit | what it fixed |
|---|---|
| `5ebe888` | *"the content validator had never validated anything"* |
| `91c7eb5` | *"The citation check could never fire"* |
| `cbe5fa9` | Zod silently stripping declared fields — **including `lean`** |
| `6c50eca` | 461 blocks invisible to QA |
| `8db9a93` | report manifest fields the schema silently strips |

**`91c7eb5` explains an anomaly recorded earlier in this bean.** A deliberate bogus
citation key produced no error, and that was logged as "either citations aren't checked,
or my block isn't being read". The real answer is now known: the citation check *could
never fire*. On the new platform it is not fixed so much as **disclosed** —

    ℹ [(bibliography)]: no reference registry configured — cites-resolve did not run,
      so cites[] entries were NOT validated against references

which is the right behaviour: a check that did not run now says so instead of passing
silently. `cites[]` in these blocks is still unvalidated, and that is now visible.

**Re-validated on `29b03f7`.** Corpus baseline moved **4 → 40 issues** — entirely from
`8db9a93` newly reporting pre-existing blocks with undeclared fields (`authorNotes`,
`chapter`, `is_mathematics`, `proofOf`, `computation`, `probe`, `consumers`). **None of
the 40 is from this arc's blocks**, and the positive control still fires: removing `lean`
from one block moves 40 → 41 with the expected warning, back to 40 on revert. So the
blocks are genuinely read, and `lean` is not among the stripped fields.

**qou main merged**: +1008 commits since the branch base, clean merge, and of this arc's
files only `mass-theory.ts` was touched upstream — resolved without conflict, all three
block registrations intact. Post-merge baseline 42, delta from this arc still zero.

**Lesson for the remaining blocks.** A validator's issue count is only comparable against
the *same platform SHA*; `run-validate.ts` prints it for exactly this reason (its own
docstring records two agents disagreeing over a baseline that was a function of two
inputs). Quote the platform SHA with any baseline, and re-run the positive control after
a platform bump rather than assuming the previous run still means what it did.

---
**2026-08-15 (later) — two more blocks, for the work this arc produced *after* the original
eight.**

The arc kept going after this bean's first pass, adding ~215 Lean declarations with no
paper presence — the exact gap this bean exists to close. Two blocks, both registered and
both positive-controlled:

| block | chapter | covers |
|---|---|---|
| `diophantine-birthday-trajectory` | `appendix-surreals-archimedean` | the birthday/trajectory separation |
| `gluing-certification-mechanical-reach` | `mass-theory` | degrees 2–14, 2–14 tetrahedra |

**Baseline unchanged at 42 issues** on both, so neither adds a defect; the positive control
moves 42 → 43 for each, naming the block, so both are genuinely read.

### ⚠ The first block was written into the wrong chapter

`conj:diophantine-birthday` lives in **`appendix-surreals-archimedean/`**, not
`appendix-surreals/` where I first put its commentary. Caught by grepping for the label
before wiring `uses[]` — had I trusted the directory name, the block would have sat in a
chapter that never mentions the conjecture it is about, and `uses: ["conj:…"]` would have
pointed across chapters for no reason.

**Related, and not fixed:** `DiophantineBirthday.lean`'s own docstring links to
`../../../quantum-observable-universe/appendix-surreals/diophantine-birthday.md`, which
**does not exist** — the file is in `appendix-surreals-archimedean/`. A dead doc link in
the Lean source, of the same family as the two dead `lean.ref`s this bean caught earlier,
and equally invisible to every checker.

### The untracked-file trap, avoided deliberately this time

This bean already records a positive control run on an **untracked** file, where
`git checkout --` could not revert it and silently left a block without its `lean.ref`.
Both controls here reverted from an explicit `/tmp` backup instead, and the revert was
verified by grepping the restored ref back. Worth stating as the rule: **a positive control
on a new file needs a real backup, because the usual revert is a no-op on something git has
never seen.**

---
**2026-08-16 — a third block, and it changed the Lean it cites.**

`appendix-surreals/birthday-axioms-do-not-pin-the-birthday.{md,ts}`, registered beside
`hyperreal-limit-transfer`. Covers the `BirthdayFaithful` result, which had **no paper
presence**: the six axioms admit a two-valued model, so they bound birthday only from
above; `birthday(n) ≤ n` is already a theorem while the matching `≥` is unobtainable; the
fix is an opt-in mixin rather than a change to the carrier; and the independence is proved
rather than asserted.

**Writing the block improved the theorem.** Wiring `lean.ref` meant reading the cited
statement, which turned out to be weaker than its name — its two conjuncts were not linked
to the same structure (see `qou-bday` for the full account). A stronger
`birthdayFaithful_independent_witnessed` was added and the block cites **that**.

Recording it here because it is an argument for this bean's whole premise: writing the
exposition is not transcription. Citing a result forces someone to read what it actually
says, which is a different act from proving it, and it caught something two prior passes
over that file did not.

Verified as before: ref resolves by `#check`; baseline unchanged at 42; positive control
42 → 43 on removing the `lean` field, reverted from an explicit backup.
