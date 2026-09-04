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

## Update 2026-09-04 — 38 → 11, and the cause table needs a second half

**Standing: 27 of the 38 are at 0 errors and 0 warnings; 11 remain.**
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

### The 11 that remain

| errors | file |
|---|---|
| 22 | `mass-theory/spin-involution-lp-dual-invariance` (bean `qou-0xrn`) |
| 7 | `fluid-dynamics/townsend-biot-savart-strain` (real-analysis proof drift) |
| 4 | `climax-volume-mass/vertex-algebra-jet-relations` |
| 3 | `mass-theory/categorical-transfer-matrix` (bean `qou-xdwp`), `mass-theory/gb-depth-period-correspondence`, `quantum-observable-universes/categorical-q-ext-deriv-unique` |
| 2 | `lifting-and-descent/descent-cocycle-deviation` (`GroupWithZero M`), `braids-and-knots/braid-action-tensor` (bean `qou-8qby`), `braids-and-knots/lagrange-resolvent-transform` |
| 1 | `mass-theory/vertex-operator` (bean `qou-xdwp`), `mass-endomorphism/chi-v21-hoefsmit-matrix-derivation` (unknown `hoefsmit_v21_b_sq_rational` + a `whnf` heartbeat timeout) |

**Correction, same day.** This section first said "38 → 12 / 26 fixed", and
several commit messages on this branch carry a running `Sweep N -> M` tally
built on that. **The correct figure is 38 → 11, i.e. 27 fixed**, re-measured
after merging `origin/main` (151 commits) into the branch. The error was an
off-by-one in a hand-counted intermediate list — a 15-entry list read as 16 —
which then propagated through every subsequent subtraction. The per-file table
above was always right; only the count above it was wrong. The `Sweep N -> M`
lines in the commit history are left as written rather than rewritten; read
them as approximate, and this table as authoritative.

The merge changed 33 library `.lean` files. None is in the import cone of any
file repaired here (`QOU/KnotTheory`, `QOU/BraidKnot/TwoRowStratum`,
`QOU/BraidKnot/KnotFactorSpectralDerivation`,
`QOU/MassEndomorphism/DeltaMaxUniformBound`,
`QOU/QuantumBloch/pentagon_uv_commutation` are all untouched by it), and every
one of the 40 originally-failing paths was re-run lean-direct after the merge —
which is where the 11 above comes from.


---

## Update 2026-09-04, later — 38 → 8

**30 of the 38 are at 0 errors; 8 remain.** Re-measured by re-running all 40
originally-failing paths lean-direct after merging `origin/main`.

Four more repaired, adding two cause classes and one honest non-repair:

| file | cause |
|---|---|
| `lifting-and-descent/descent-cocycle-deviation` | **A structure parameter was dropped.** `TwistedTwoCocycle` sits under `variable (R : Type*) [GroupWithZero R]`, so its real arity is `TwistedTwoCocycle R M`. The sibling passed one argument, putting the base manifold in the coefficient ring's slot, and so demanded `GroupWithZero M`. (Also: `twisted_cocycle_unobstructed` takes `R` **explicitly**, inherited from the `variable` form.) |
| `braids-and-knots/lagrange-resolvent-transform` | **A genuinely unfinished proof**, not a stale reference — see below. |
| `mass-endomorphism/chi-v21-hoefsmit-matrix-derivation` | **A forward reference, then a proof that could not be seen to fail** — see below. Ends at `sorry` + `-- Ref:`, bean `qou-18b6`. |

### `lagrange-resolvent-transform`: a comment true about the wrong quantity

`lagrange_resolvent_diagonal_action` (the DFT diagonalises the C₅ action on
Bring's surface, `σ(w_k) = ζ^{-k} w_k`) failed on the `k = 4` case. Seven
hand-enumerated reduction lemmas covered `ζ^5 … ζ^16`, justified as *"the
products k·j for k,j ∈ {0,…,4} range over {0,…,16}"* — correct about the
products, and irrelevant to what the proof sees: `ring_nf` multiplies in the
`ζ^4` standing for `ζ⁻¹`, so exponents reach `4·4 + 4·4 = 32`. The surviving
goal wanted `ζ^20, ζ^24, ζ^28, ζ^32`.

Replaced with one conditional simp lemma, `ζ_pow_reduce (n) (h : 5 ≤ n) :
ζ^n = ζ^(n-5)`, which terminates (exponent strictly decreases; side condition
fails below 5) and reduces any concrete power. **This is a completed proof, not
a repaired reference** — the theorem now holds for all five `k`, where before it
held for four and the file did not compile.

Generalisable: an enumerated reduction table is sized against the *inputs*; what
needs covering is what the *normaliser* produces from them.

### `chi-v21-hoefsmit`: raise the heartbeat budget before believing a timeout

Two defects, the second hidden by the first.

`hoefsmit_v21_b_sq_rational` was declared at the end of the file and consumed at
line 247 → `Unknown identifier`. **A forward reference and a missing declaration
are indistinguishable from that error text.**

With that fixed the error was `(deterministic) timeout at whnf, maximum number
of heartbeats (200000)`. That reads as "proof present, machine too slow". It is
not: at 4 000 000 heartbeats the declaration elaborates in **28 s** and reports
the real failure — `rw [h_sqrt]` finds no `√(hoefsmit_v21_b_sq q) ^ 2`, because
`ring_nf` had already normalised the square away. The tactic script never proved
the theorem.

Disposition: `sorry` + `-- Ref:` (§Zero-sorry default, state-and-queue), with
the partial progress recorded in the docstring and bean `qou-18b6` — the goal
reduces to a polynomial identity in `q, b` modulo `b² = (q⁴+q²+1)/(q²+1)²`, and
the tractable route is the Tier-2 `sigma1_v21_gen` restatement the file's own
`@[deprecated]` notice already names.

### Recurring across the whole sweep: the unused instance binder

Three files carried a hypothesis their proof never consumed
(`dominant_subbraid_consistency`, `sigma1_v21_param_sq_trace`, and the
now-`sorry`'d one's neighbours). This is not a lint nit — an unused hypothesis
**overstates the dependency**, making an unconditional fact read as conditional.
It is the mirror of the §3b-cond violations elsewhere in this sweep, and neither
direction is visible to `#print axioms`.

### The 8 that remain

| errors | file |
|---|---|
| 22 | `mass-theory/spin-involution-lp-dual-invariance` (bean `qou-0xrn`) |
| 7 | `fluid-dynamics/townsend-biot-savart-strain` (real-analysis proof drift) |
| 4 | `climax-volume-mass/vertex-algebra-jet-relations` |
| 3 | `mass-theory/categorical-transfer-matrix` (bean `qou-xdwp`), `mass-theory/gb-depth-period-correspondence`, `quantum-observable-universes/categorical-q-ext-deriv-unique` |
| 2 | `braids-and-knots/braid-action-tensor` (bean `qou-8qby`) |
| 1 | `mass-theory/vertex-operator` (bean `qou-xdwp`) |


## Update 2026-09-04, third pass — 38 → 6

**32 of the 38 at 0 errors.** Two more, both cases where the compile error was
again not the whole story:

`mass-theory/vertex-operator` — `Function expected at ReebBundle`. Unreachable
(sibling cannot import sibling) **and type-wrong**: `def:reeb-bundle` is
`structure ReebBundle (q : ℝ)` — archimedean, `q > 1`, `Real.exp` holonomy, its
own header saying "NOT part of the formal proof chain" — while this file is over
`R_q = ℤ[q, q⁻¹]`. Applying an ℝ-indexed structure to a Laurent polynomial is
the §7c straddle, and `autoImplicit` turned it into a metavariable rather than a
type error. `VertexOperator`/`OPE` now take the base space as a type parameter
`B`; an archimedean consumer instantiates `B := ReebBundle q₀` after τ.

The same file carried `axiom ope_is_skein`, whose `q` was auto-bound because the
real binder had been commented out. Now a theorem — and its proof is
`⟨⟨Y₁, Y₂, q, -q_inv_param⟩, rfl, rfl, rfl, rfl⟩`, **because `OPE` carries the
eigenvalues as fields**. So the axiom was simultaneously heavyweight in
`#print axioms` for every downstream statement and empty in content. What it
establishes is that such an OPE exists; what it does not is that the Hecke pair
is *forced* — that needs `OPE` to carry the generator's action and derive the
eigenvalues, and until then `q` and `-q⁻¹` are put in by hand.

`braids-and-knots/braid-action-tensor` — both errors were
`rewrite failed: Did not find an occurrence of the pattern` on patterns that
**are** present, just not as syntactic subterms: `≫` is right-associated, so
`α ≫ (V◁β ≫ (V◁β⁻¹ ≫ α⁻¹))` has no adjacent whisker pair, and `hex`'s RHS is the
first three factors of a goal that parses as `X ≫ (Y ≫ (Z ≫ α⁻¹))`.
`slice_lhs 2 3` and `slice_lhs 1 3` re-bracket first — the tool §5's tactic
table already names for diagram work. `yang_baxter_braiding`, which the file
exists for, now typechecks. Bean `qou-8qby` closed.

**Same error text, opposite diagnosis, worth keeping straight:** in
`chi-v21-hoefsmit` the missing pattern was genuinely gone (`ring_nf` had
normalised it away) and the proof was unfinishable as written; here it is
present and only mis-bracketed. Check whether the subterm exists modulo
associativity before concluding a proof is wrong.

### The 6 that remain

| errors | file |
|---|---|
| 22 | `mass-theory/spin-involution-lp-dual-invariance` (bean `qou-0xrn`) |
| 7 | `fluid-dynamics/townsend-biot-savart-strain` |
| 4 | `climax-volume-mass/vertex-algebra-jet-relations` |
| 3 | `mass-theory/categorical-transfer-matrix` (bean `qou-xdwp`), `mass-theory/gb-depth-period-correspondence`, `quantum-observable-universes/categorical-q-ext-deriv-unique` |

---

## Update 2026-09-04, fourth pass — 38 → 4, and a cost of this sweep I had not measured

**34 of the 38 at 0 errors.** Two more repaired (`categorical-q-ext-deriv-unique`,
`gb-depth-period-correspondence`); re-verified after a second `origin/main` merge
(49 commits, no conflict), and none of the 34 regressed.

### CORRECTION — "a stranded sibling is often a pure duplicate" was a rate claim I did not measure

The 2026-09-04 update above says that, and "often" asserts a rate over a
population. I repaired three that way and generalised from three.

A sibling session measured the adjacent population and landed it on `main` as
`02483c5457` while this branch was working. Its numbers:

- declarations whose **type** is `sorry`: **exactly 1** corpus-wide — the
  `delta-max-uniform-bound` stub deleted here. Singular, not a class.
- siblings **degenerate on a name the library also declares**: also **exactly 1**,
  the same file.

So the shape is real and the rate is not "often". `pentagon-uv-commutation` does
not appear in either count because it declared a *different* name
(`_mass_theory` suffix), and `bloch-group-quotient-construction` was trivial
instances rather than a name collision — three repairs, three different shapes.
Read the earlier paragraph as describing those three, not a population.

### I should have found the pre-existing script, and did not

[`scripts/lean-sibling-library-divergence-audit.py`](../../scripts/lean-sibling-library-divergence-audit.py)
was written **2026-09-03 13:11**, before this sweep began, and detects exactly
the phenomenon this audit reports from the other direction: a sibling and a
library file declaring the same fully-qualified name with different statements.
Its motivating incident is worse than any found here — `conj:b1-hyperbolic-rows-theorem`
was repaired in the library on 2026-08-08, the sibling kept the pre-repair
version, and a `False` was still derivable from the sibling on 2026-09-03.

That is a corpus-grep miss: the sweep's core finding was already tooled.

### The cost: a repair turns a VISIBLY broken sibling into a SILENTLY divergent one

`lean.ref` resolves **sibling-first by file** (§0a candidate 1). A sibling that
does not compile is visibly broken — a reader following the ref hits errors. A
sibling that compiles while declaring the same name as a library declaration,
with a different statement, looks fine and is not.

Making these files compile does not create the divergence (the script compares
declaration text, not compilation, so it flagged them before too). It changes
the failure mode from loud to quiet.

**Measured on the 38 sibling files this branch touched: 6 appear in the script's
195 divergences, and hand-verification says 4 are real.**

| name | library | verdict |
|---|---|---|
| `QOU.planck_classical_limit` | `QuantumObservableUniverse/Propositions.lean` | **REAL** — sibling proves it of `quantumPlanckConstantSibling`, library of `quantumPlanckConstant` |
| `QOU.qExtDeriv_classical` | same | **REAL** |
| `QOU.qLieBracket_classical` | same | **REAL** |
| `QOU.FlavorDressing.flavor_mass_splitting_bound` | `FlavorDressing/FlavorMassSplittingBound.lean` | **REAL** |
| `QOU.BraidKnot.ConfinementPhaseStratification` | `BraidKnot/ConfinementLevel.lean` | **FALSE POSITIVE** — that file declares no such name |
| `QOU.LiftingDescent.descent_cocycle_deviation` | `LiftingDescent/ccg_crossed_module_structure.lean` | **FALSE POSITIVE** — that file declares only `CrossedModuleContext` and `ccg_crossed_module_structure` |

The two false positives are the script's own documented defect: it builds a
fully-qualified name by concatenating **every** `namespace` line in a file, which
is wrong for a file opening and closing several in sequence. Its header says so,
and says 6.1 % of sibling and 8.5 % of library files have more than one. **So
verify a reported pair against both files before acting on it** — the
`descent_cocycle_deviation` row nearly cost a retraction of a correct repair
here, on the strength of a tool another agent wrote and I had not checked.

The four real ones are **pre-existing and not repaired here**: deciding whether
the sibling or the library declaration is canonical is a per-block judgement
about which statement the `.md` means, not a compile fix. Tracked in
bean `qou-e7xv`.

### The 4 that remain

| errors | file |
|---|---|
| 22 | `mass-theory/spin-involution-lp-dual-invariance` (bean `qou-0xrn`) |
| 7 | `fluid-dynamics/townsend-biot-savart-strain` |
| 4 | `climax-volume-mass/vertex-algebra-jet-relations` |
| 3 | `mass-theory/categorical-transfer-matrix` (bean `qou-xdwp`) |

---

## Update 2026-09-04, final pass — 38 → 1

**37 of the 38 at 0 errors.** The one remaining is
`mass-theory/spin-involution-lp-dual-invariance` (22 errors, bean `qou-0xrn`) —
a judgement call already put to the author and deliberately not patched.

Three more repaired, and each turned up something larger than its compile
error. Together with `vertex-operator` they make a family worth naming.

### FOUR bare axioms in the sweep, and each was wrong in a different way

| declaration | what it actually was |
|---|---|
| `QOU.ope_is_skein` (`vertex-operator`) | **Empty.** Provable by `⟨⟨Y₁, Y₂, q, -q_inv_param⟩, rfl, rfl, rfl, rfl⟩` — `OPE` carries the eigenvalues as *fields*, so exhibiting one is record construction. Heavyweight in `#print axioms`, and bought nothing. |
| `QOU.transfer_matrix_level_independence` (`categorical-transfer-matrix`) | **False.** Asserted `T₁.base = T₂.base → T₁.vertex_volume = T₂.vertex_volume` with `vertex_volume` a free field. `level_independence_false_as_stated` proves the refutation. A false axiom is available to prove anything downstream. |
| `markov_level_compatible` (`vertex-algebra-jet-relations`) | **Provable by `rfl`, and its docstring described a different claim.** Statement: `levelHecke hp n level = levelHecke hp n (level+1)`, where `levelHecke` discards its level. The docstring claimed `tr_M^{(n+1)}(ℓ_n(w)) = tr_M^{(n)}(w)` — neither `tr_M` nor `ℓ_n` appears, and the bound `w` was never used. |
| `kappa_squared_tends_to_zero_axiom` (`townsend-biot-savart-strain`) | **Not an axiom at all.** Already a `theorem`, with a real filter proof in its body, under a docstring announcing it as "auto-extracted … pending Mathlib infrastructure". A reader auditing axioms would have counted it as one on the name; a reader trusting the docstring would not have tried to fix it. |

The through-line: **`#print axioms` sees none of this.** It reports what a proof
term *depends on*, and says nothing about whether the statement is empty, false,
mismatched with its docstring, or already proved under a misleading name. Only
reading the statement against the `.md` catches any of the four.

### And a fifth shape: the block's `lean.ref` pointing at the wrong thing

- `categorical-transfer-matrix` referenced
  `qou:QOU.Torsion.CategoricalTransferMatrix` — **live library code**, a
  spectral mass-gap object (`eigenvalues : ℕ → ℝ`, `gapValue`) with consumers in
  `MassGapKeystone` and `MassGapFrontier`. This block's `.md` describes an
  equivalence class of braiding operations, i.e. the *sibling's*
  `QOU.CategoricalTransferMatrix`. Two different objects sharing a base name
  across namespaces; the ref picked the one that does not match the prose.
- `vertex-algebra-jet-relations` referenced `euler_level_stable`, which was
  `theorem euler_level_stable (_n : ℕ) : (2 : ℤ) - 2 * 4 = -6 := by norm_num`.
  That arithmetic identity *was* the block's formalisation. Now stated over a
  named `eulerChar` so it is false if `eulerChar` is wrong or level-sensitive.

### `townsend-biot-savart-strain`: 7 errors, all Mathlib API drift

Worth recording because the docstring said the opposite ("pending Mathlib
infrastructure"). The four mismatches: `Tendsto.pow` landing in `𝓝 (0^2)`;
`tendsto_log_mul_rpow_nhdsGT_zero` stated with an **rpow** while the proof tried
`rw [Real.rpow_natCast]` inside a `filter_upwards` where the exponent was
already a natural power; `Tendsto.div` producing `Pi.div` rather than a
pointwise lambda; and `Metric.tendsto_nhdsWithin_nhds` leaving `τ` **implicit**
in its conclusion. Plus a `field_simp` that closes its goal, making the
following `ring` report `No goals to be solved` — the fourth instance of that
shape in this sweep.

### `vertex-algebra-jet-relations`: the migration boundary INSIDE one file

`levelHecke` is defined at the top of the same file and gained `(hs : 0 < strands)`
when `UGB.GrobnerShirshov.heckeRewritingSystem` gained `(hn : 0 < n)`. Its three
call sites, fifty lines below, were not updated. The usual stranding, with no
cross-file boundary to make it visible.

### Final standing

| errors | file |
|---|---|
| 22 | `mass-theory/spin-involution-lp-dual-invariance` (bean `qou-0xrn` — author's call) |

Everything else compiles. Note the caveat recorded in the previous section
stands: 4 of the 38 repaired files carry **real** sibling/library name
collisions that repairing has made silent rather than loud, and choosing which
declaration is canonical is a per-block judgement, not a compile fix.

---

## Precedent check, 2026-09-04 — the axiom family is NOT a new finding

Before opening a bean for the proposed "corpus-wide statement-vs-`.md` pass", the
`.beans/` corpus-grep (checklist path 6). It should have been run before calling
the four-axiom table "the single most useful thing this sweep found". Two beans
already name the class:

**`qou-k4ul` — "operator_selection_lp is false as stated, not merely unproved"**
(completed, 2026-08-16). Machine-verified: `False` is derivable from
`operator_selection_lp`, because `OperatorSelectionLpContext` carries **only data
and no hypotheses**, while the theorem concludes a relation among that data for
*every* instance. Instantiate with `d = 1, n_target = 1, x_star = 0` and the
first conjunct says `0 = 1`.

That is **the same mechanism** as `transfer_matrix_level_independence` here —
free fields, a conclusion relating them, refutable by instantiating degenerately
— found a month earlier on a different declaration. So this sweep's "false axiom"
is the *second* instance of a diagnosed class, not a discovery.

**`bday` — "Audit what the birthday axioms actually establish"** (in-progress).
Same family from the other side: `flatBirthday x := if x = 0 then 0 else 1`
satisfies **all six** birthday axioms, so any theorem proved from those axioms
alone is true in the two-valued model too. Its method is the generalisation this
sweep was groping toward:

> instantiate it at the degenerate model. If it degenerates to something trivial,
> the theorem carries no content, whatever its statement looks like.

That is strictly sharper than "read the statement against the `.md`" — it is
*mechanical*, and it decides the question rather than raising it. `ope_is_skein`
would have fallen to it immediately (`OPE` carries the eigenvalues as fields, so
the degenerate instance discharges it); so would the `norm_num` statements, whose
degenerate model is "any two numbers with that product".

### What this changes

- **The sweep's contribution is instances, not the class.** Four more members,
  two of them in shapes the earlier beans had not seen (`markov_level_compatible`,
  provable by `rfl` *and* docstring-mismatched; `kappa_squared_tends_to_zero_axiom`,
  not an axiom at all). Recorded as such.
- **No new bean was opened.** The right home is `bday`, which is in-progress and
  already carries the method; a fresh bean would have fragmented it.
- **The proposed corpus-wide pass should be scoped as extending `bday`'s
  degenerate-model test**, not as a new statement-vs-`.md` idea. `bday` names 11
  modules for the surreals case; the generalisation is: for every `structure` or
  `class` whose fields are pure data, construct the degenerate instance and see
  what survives.

The PR body's §3 calls the four-axiom table "the single most useful thing this
sweep found". That stands as written — it was, *for this sweep* — but it should
not be read as novelty. This section is the correction of record.

---

## Update 2026-09-04 — fourth `origin/main` merge, re-verified

`origin/main` `7297f2f6d5 → d0d473550a`, **21 commits**, merged as `bf4f787890`.
This is the **fourth** merge into the branch (after 151, 49, 26); everywhere
this document says "three merges", read four.

**All 37 repaired siblings re-verified: `lean`-direct exit 0, zero errors, on
every one.** None regressed. The one file the merge deleted from the check list
(`mass-theory/pentagon-uv-commutation.lean`) is the pure duplicate this sweep
`git rm`'d, so its absence is the expected state and not a miss.

Two notes on the merge itself, both worth keeping because each is a shape that
recurs.

**The one conflict was provenance-only, and checking that is a two-line job.**
`computations/witness-raw-float64-audit.witness.json` conflicted on exactly
three lines — `commitSha` and `computedAt` — with the payload auto-merged. Both
sides' payloads hash **identically** with `commitSha` / `computedAt` /
`durationMs` masked, so the later run was taken. Masking the volatile keys and
hashing is what turns "a witness conflicted" into "nothing computed differently";
without it the honest report would have had to be "a witness conflicted and I
picked one".

**One library file main touched is inside this branch's cone.**
`QOU/Mathlib/LPDuality.lean` gained 61 lines from a sibling
(`duality_gap_decomposition`, `duality_gap_le_of_residual_bounds`). Pure
addition, no deletions — but "pure addition" is an argument, not a check, so it
was compiled: `lean`-direct **exit 0** post-merge. No other `.lean` in the 21
commits overlaps this branch.
