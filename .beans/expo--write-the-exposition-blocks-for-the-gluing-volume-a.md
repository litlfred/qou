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
