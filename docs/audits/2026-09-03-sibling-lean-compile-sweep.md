# 38 content-block sibling `.lean` files do not compile, and nothing was checking them

**Date:** 2026-09-03 · **Bean:** `qou-e7xv` · **Method:** `lean`-direct on every
sibling, then every failure re-verified under a widened `LEAN_PATH`

## What was measured

Every `.lean` under `content/quantum-observable-universe/` that is **not** in
`lean/` — i.e. every content-block sibling — compiled with `lean`-direct.
908 files, 6 workers.

    raw failures                                       41
      harness: QOU-only LEAN_PATH, file imports UGB    -1
      harness: `import Mathlib` (aggregator olean absent) -2
    REAL                                               38   (4.2 % of 908)
      fixed on this branch                            -11
    REMAINING                                          27

**Both harness classes were confirmed by re-running, not by inspection.**
`vertex-algebra-relations.lean` gives `unknown module prefix 'UGB'` under a
QOU-only path and **exit 0** with all three paper packages on it — same file,
same commit. And `Mathlib.olean` (the whole-library aggregator) is genuinely
absent from the restored cache, so two files that `import Mathlib` wholesale
fail for a reason a real `lake build` would not have. Harness §6(a): check
`ls` on the named olean before diagnosing.

## Why nothing caught these

Content-block siblings live **outside the Lake globs** — `globs = ["QOU",
"QOU.+"]` with `srcDir = "."` pointing at the `lean/` directory — so
`lake build QOU` never sees them. CI here is `workflow_dispatch`-only under
the 2026-06-30 Actions-billing directive. And `lean-content-siblings.yml`
gates *content-block* siblings, not these. So a sibling can be broken
indefinitely with nothing reporting it: `n-v-bring-action.lean` was, at 8
parse errors, because `Σ` is Lean 4 notation for `Sigma` and cannot be a
binder name.

## The list

| errors | file | first error |
|---:|---|---|
| 24 | `mass-theory/spin-involution-lp-dual-invariance.lean` | : Function expected at |
| 13 | `mass-theory/categorical-transfer-matrix.lean` | : unexpected token 'section'; expected 'lemma' |
| 9 | `fluid-dynamics/townsend-biot-savart-strain.lean` | (lean.unknownIdentifier): Unknown constant `Real.tendsto_log_mul_rpow_nhdsGT_zero` |
| 8 | `mass-theory/flavor-mass-splitting-bound.lean` | (lean.unknownIdentifier): Unknown identifier `R` |
| 8 | `quantum-observable-universes/substrate-parameter-exists.lean` | : `field_pos` is not a field of structure `SubstrateParameter` |
| 7 | `mass-theory/vertex-operator.lean` | : unexpected token 'section'; expected 'lemma' |
| 6 | `information-theory/quantum-volume.lean` | : failed to synthesize |
| 5 | `mass-theory/knot-factor-shell-closed.lean` | : Application type mismatch: The argument |
| 5 | `predicted-spectra/bloch-group-quotient-construction.lean` | : `pentagon_subgroup_exists` is not a field of structure `HasPentagonRelation` |
| 5 | `quantum-observable-universes/quantum-planck-constant.lean` | : failed to synthesize |
| 4 | `climax-volume-mass/vertex-algebra-jet-relations.lean` | : Application type mismatch: The argument |
| 4 | `mass-theory/residue-at-root.lean` | (lean.unknownIdentifier): Unknown constant `QOU.BraidKnot.ResidueAtRoot.residue` |
| 3 | `mass-theory/gb-depth-period-correspondence.lean` | : failed to synthesize |
| 3 | `quantum-observable-universes/categorical-q-ext-deriv-unique.lean` | : Tactic `rfl` failed: The left-hand side |
| 3 | `quantum-observable-universes/q-ext-deriv.lean` | : failed to synthesize |
| 3 | `quantum-observable-universes/q-lie-bracket.lean` | : failed to synthesize |
| 2 | `braids-and-knots/braid-action-tensor.lean` | : Tactic `rewrite` failed: Did not find an occurrence of the pattern |
| 2 | `braids-and-knots/lagrange-resolvent-transform.lean` | : `simp` made no progress |
| 2 | `lifting-and-descent/descent-cocycle-deviation.lean` | : failed to synthesize |
| 2 | `lifting-and-descent/euler-char-stability.lean` | (lean.inferBinderTypeFailed): Failed to infer type of binder `n` |
| 2 | `mass-endomorphism/chi-v21-hoefsmit-matrix-derivation.lean` | (lean.unknownIdentifier): Unknown identifier `hoefsmit_v21_b_sq_rational` |
| 2 | `mass-endomorphism/u-coordinate-discharges.lean` | : No goals to be solved |
| 2 | `mass-theory/gram-determinant-plancherel-ratio.lean` | : unexpected token '=>'; expected '[', '{', '\|', '⦃' or term |
| 2 | `mass-theory/he4-channel-active-set.lean` | : unknown tactic |
| 2 | `mass-theory/he4-two-row-dominance.lean` | : unknown tactic |
| 2 | `nuclear-interactions/hyperelliptic-z5-classification.lean` | : unknown tactic |
| 2 | `quantum-observable-universes/q-connection.lean` | : failed to synthesize |
| 1 | `fluid-dynamics/bn-mtc-action.lean` | : invalid binder annotation, type is not a class instance |
| 1 | `knots-particles-confinement/confinement-level-exists.lean` | (lean.unknownIdentifier): Unknown constant `QOU.BraidKnot.ConfinementLevel.exists` |
| 1 | `knots-particles-confinement/confinement-phase-stratification.lean` | : unexpected token '/--'; expected 'lemma' |
| 1 | `lifting-and-descent/localized-knot.lean` | : Invalid field `writhe`: The environment does not contain `QOU.KnotTheory.BraidWord.writh |
| 1 | `mass-endomorphism/explicit-central-idempotent.lean` | : failed to synthesize |
| 1 | `mass-theory/delta-max-uniform-bound.lean` | : object file '/home/user/qou/content/quantum-observable-universe/lean/.lake/build/lib/lea |
| 1 | `mass-theory/pentagon-uv-commutation.lean` | : Application type mismatch: The argument |
| 1 | `mass-theory/qz-bicompletion.lean` | (lean.unknownIdentifier): Unknown identifier `zPochhammer` |
| 1 | `mass-theory/typed-b3-sub-braid-extraction.lean` | : No goals to be solved |
| 1 | `observations/n-v-tower-depth-ninety.lean` | : typeclass instance problem is stuck, it is often due to metavariables |
| 1 | `stochastic-mechanics/classical-limit-functor.lean` | (lean.unknownIdentifier): Unknown identifier `MonoidalFunctor` |

## Notable causes

- **`delta-max-uniform-bound.lean` imports a module that does not exist.**
  `import QOU.MassEndomorphism.JetTower` — no `JetTower.lean` anywhere in the
  source tree (the closest are `QOU/BraidKnot/JetTowerUniformDeltaMax` and
  `QOU/QBeta/JetTowerBlindToDecay`). Its second import,
  `QOU.BraidsAndKnots.MarkovTrace`, uses a namespace spelling
  (`BraidsAndKnots`) the tree writes as `BraidKnot`. Distinguished from a
  harness gap by checking the SOURCE tree, not just the olean: absent olean +
  absent source = real.
- **`Inv GroundRing.R_q` cannot be synthesised — 5 files. 🛑 And the obvious
  fix is the WRONG one.** This audit first called it *"one missing instance on
  the corpus's own ground ring"* and named it the highest-leverage single fix.
  That diagnosis is **retracted**: adding an `Inv` instance is precisely what
  must not happen.

  `lean/QOU/GroundRingCore.lean` is explicit — `R_q = ℤ[q, q⁻¹]` is *"an
  un-ordered commutative ring"*, and `q_inv_param` exists as its own
  declaration with the reason stated in its docstring: *"`R_q` is a ring, not
  a field, so it has no `Inv` instance and `q⁻¹` cannot be written."* The
  absence is deliberate. An `Inv` instance on a non-field would make `x⁻¹`
  elaborate to a junk value for every non-unit, turning five compile errors
  into five silently wrong formulas — strictly worse.

  🛑 **And that second diagnosis was wrong too.** It said the sites needed
  `q_inv_param` or an explicit `q * q_inv = 1` field, "a per-site mathematical
  decision". They needed neither. The actual cause is one level further up and
  is stated in the library's own docstring: `SubstrateParameter` was split
  across the §7c wall (bean `qou-6ome`) into

      SubstrateParameter M         categorical: field : M → R_q
      ArchimedeanSubstrateField M  the former structure, renamed: M → ℝ

  and these files are archimedean — they return `ℝ`, take `⁻¹`, use positivity
  — but still named the *categorical* structure, so `sp.field p` came back as
  `R_q`. The `Inv` error was three levels downstream of the fault.

  **RESOLVED**: all five, plus `substrate-parameter-exists.lean` (the
  `field_pos` case), migrated to `ArchimedeanSubstrateField`. Each now
  compiles with zero errors and zero warnings. Sweep total **38 → 32**.

  The same library file explains why no gate caught it, and it generalises:

  > `check-wall-side` and `check-base-ring` both **PASS** on a file that is
  > *wholly* archimedean, because they fire on files that *mix* regimes.
  > Passing the wall gate means "not mixed", not "on the right side of the
  > wall".

  Three diagnoses of one symptom, each confident, the first two wrong and one
  of them actively harmful. Recorded at length because the leverage framing —
  *five files, one root cause* — is what made the wrong fix attractive, and
  because the right answer was in a docstring the whole time.
- **4 parse errors**, i.e. files that never got past the parser.
- **Mathlib drift**: `Real.tendsto_log_mul_rpow_nhdsGT_zero`,
  `MonoidalCategory.whiskerRight_comp` (renamed `comp_whiskerRight`) and
  friends.

## The dominant cause, once the files are opened: MIGRATIONS STOP AT THE SIBLING BOUNDARY

Not Mathlib drift, and not bad mathematics. Repeatedly, a library object
changed shape, every consumer *inside* the Lake globs was updated because
`lake build` forces it, and the content-block siblings were left behind
because nothing builds them:

| library change | siblings stranded |
|---|---|
| `SubstrateParameter` split into categorical (`→ R_q`) and `ArchimedeanSubstrateField` (`→ ℝ`) | **6** |
| a theorem specialised from generic `Field R` to `ℝ`, one ascription left as `(q : R)` | 1 |
| `HeckeExpansion` gained `(R : Type*) [Field R]` before `n` | 1 |
| `HasPentagonRelation` / `HasBlochGroup` given real fields in place of `True`-ish ones | 1 |

That is **9 of the 11 files repaired so far**. The remaining two were a
Lean-notation token used as a binder name and a pair of orphaned docstrings.

The consequence is worth stating plainly: **a mechanically-enforced migration
is not enforced here.** `lake build QOU` cannot see these files
(`globs = ["QOU", "QOU.+"]`, `srcDir = "."` → the `lean/` directory), and CI
is `workflow_dispatch`-only, so the compiler never asks the sibling to keep
up. Anyone changing a library signature should grep
`content/<paper>/**/*.lean` outside `lean/` as a separate step.

The Bloch-group case is the sharpest, because there the stranded sibling was
*wrong* rather than merely stale: it carried an instance with every field
`:= trivial`, and the library's strengthening is exactly what stopped it
typechecking. The compile error was the guard working.

## Scope — what this does NOT say

A sibling that fails to compile is not automatically a *false* claim: most of
these are stale references and missing instances, not wrong mathematics. What
it does mean is that the block's `lean.ref` points into a file that does not
typecheck, so the formalisation cannot be relied on as stated. Triage per
file; do not treat the 38 as 38 refuted propositions.

Two are already partly repaired on this branch: `n-v-bring-action.lean`
(now exit 0, zero warnings) and `braid-action-tensor.lean` (5 errors → 2,
still failing, bean `qou-8qby`).

---

## Update 2026-09-04 — 38 → 12, and the cause table needs a second half

**Standing: 26 of the 38 are at 0 errors and 0 warnings; 12 remain.**
Re-measured by re-running every one of the 40 originally-failing paths
lean-direct with all three paper packages on `LEAN_PATH`.

The migration-boundary table above still holds, and it grew: three more
stranded siblings, in a shape the first pass did not name.

### The shape that shape has: a stranded shadow is often a pure DUPLICATE

Three of the repairs were `git rm`, not a patch. In each case the block's
`.ts` `ref` already named a **complete, sorry-free library declaration**,
and the sibling was a copy of it that had gone stale:

| sibling | what it was |
|---|---|
| `mass-theory/delta-max-uniform-bound.lean` | `theorem … : sorry := sorry` — `sorry` in the TYPE, so it asserted nothing — shadowing a proved `QOU.MassEndomorphism.delta_max_uniform_bound`. Both its imports were dead too: `QOU.MassEndomorphism.JetTower` has no source anywhere in the tree. |
| `mass-theory/pentagon-uv-commutation.lean` | a verbatim copy under an unreferenced `_mass_theory` suffix, stale in one conjunct because `claim_iii_eigenvalue_specialisation` had been migrated from a bare `: Prop` to a real equation. |
| `predicted-spectra/bloch-group-quotient-construction.lean` | (earlier in this sweep) instances with every field `:= trivial`. |

This matters for triage order: **find the library declaration the `ref`
names and verify THAT first.** If it compiles and the sibling adds
nothing, the sibling is the defect. Sibling-first resolution is by
**file**, so a sibling wins even when it declares a different name than
the ref — which is how the `bn-mtc-action.ts` ref stayed wrong
(`qou:QOU.ObservableMTC.bnAction` for a declaration actually named
`QOU.bnAction`) with nothing to catch it.

### A second cause class, unrelated to migrations: missing imports

Four files failed for reasons that have nothing to do with the library:

- **Missing tactic import (3 files).** `unknown tactic` at `ring`,
  `linarith`, `interval_cases` respectively — plus an `unsolved goals`
  dump of the untouched goal, which reads as a broken proof and is not.
  One import line each; all three to 0/0 with no proof step changed.
- **`import Mathlib`, the monolithic aggregator (2 files).** Not
  verifiable here at all (the restored olean cache has no
  `Mathlib.olean`, and `lake build` evicts the restore), and a §8
  hygiene defect independently. Measured: these were the **only two**
  authored files doing it — the other 21 hits of `^import Mathlib$` are
  inside vendored `MathlibTest/`. Narrowed to the cones actually used.

### Three failures were hiding a content defect, not just a compile defect

The compile error is sometimes the smaller half. Recorded because in each
case fixing only the error would have left the worse problem in place:

1. **`bn-mtc-action`** concluded `∃ V, (β_ V V).hom ≫ (β_ V V).hom ≠ 𝟙 …`
   and proved it by `MTC.braiding_nonsymmetric` — projecting out a field
   of the definition it depends on (§3b-cond item 5), and not the `.md`
   claim, which is non-factoring through `B_n ↠ S_n`. Rewritten to derive
   that, via a general group lemma (`not_factorsThrough_of_sq_ne_one`).
2. **`explicit-central-idempotent`** stated the `(2,2)` case
   *unconditionally* while proving it from a theorem carrying
   `[ExplicitCentralIdempotentConjecture q]`. Lean refused it — the
   elaborator catching exactly the hypothesis-smuggling §3b-cond forbids.
   This surfaced a larger gap: **§3b-cond item 4 is unsatisfiable for
   that block**, because the class has no `conj:` content block anywhere,
   so `conjectural-propagation-audit.ts` sees an empty conjectural cone.
   Bean `qou-1bua`.
3. **`borromean-h4-categorical-derivation`** proved
   `(-3 : ℝ) * (1/4 : ℝ) = -3/4` by `norm_num` under three paragraphs of
   docstring about the Borromean h⁴ chain — a statement that mentions
   nothing in the framework and would hold if both factors came from
   somewhere else. Restated over named objects (`chiTwoOneBorromean`,
   `yTwoOne`) so it is false if either input is wrong. `#print axioms`
   cannot see this class: the proof is clean, the STATEMENT is empty.

And one in the reverse direction: `typed-b3-sub-braid-extraction`'s
`dominant_subbraid_consistency` carried an unused
`[hd : DominantSubBraidAtEps6]`. An unused instance binder is not a lint
nit — it **overstates the dependency**, making an unconditional closure
fact read as conditional on a perturbative-expansion axiom.

### The 12 that remain

| errors | file |
|---|---|
| 22 | `mass-theory/spin-involution-lp-dual-invariance` (bean `qou-0xrn`) |
| 7 | `fluid-dynamics/townsend-biot-savart-strain` (real-analysis proof drift) |
| 4 | `climax-volume-mass/vertex-algebra-jet-relations` |
| 3 | `mass-theory/categorical-transfer-matrix` (bean `qou-xdwp`), `mass-theory/gb-depth-period-correspondence`, `quantum-observable-universes/categorical-q-ext-deriv-unique` |
| 2 | `lifting-and-descent/descent-cocycle-deviation` (`GroupWithZero M`), `braids-and-knots/braid-action-tensor` (bean `qou-8qby`), `braids-and-knots/lagrange-resolvent-transform` |
| 1 | `mass-theory/vertex-operator` (bean `qou-xdwp`), `mass-endomorphism/chi-v21-hoefsmit-matrix-derivation` (unknown `hoefsmit_v21_b_sq_rational` + a `whnf` heartbeat timeout) |
