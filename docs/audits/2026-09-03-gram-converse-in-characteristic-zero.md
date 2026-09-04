# The Gram criterion's converse holds in characteristic zero — `det(twGram) ≠ 0` at every rank

*2026-09-03, beans `qou-kwoa` / `qou-0y6h`. Lean:
[`QOU/MathlibExt/RegTraceGramNondegenerate.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/RegTraceGramNondegenerate.lean),
[`QOU/MathlibExt/TracePi.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/TracePi.lean),
[`QOU/Hecke/TwGramDetNonzero.lean`](../../content/quantum-observable-universe/lean/QOU/Hecke/TwGramDetNonzero.lean).
PR #6517.*

## Result

```lean
twGram_det_ne_zero {K} [Field K] [CharZero K] (q : K)
    (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) :
  (twGram K (q ^ 2) n).det ≠ 0
```

Sorry-free, `[propext, Classical.choice, Quot.sound]`, at **every** `n`. No determinant is
evaluated anywhere in the proof.

## This does not contradict the 2026-08-30 scope-(b) exclusion — it is its complement

[`2026-08-30-tw-gram-determinant-measured.md`](2026-08-30-tw-gram-determinant-measured.md)
records, correctly, that

    det(twGram) ≠ 0  ⟹  H_n(q) semisimple

is one-directional, with a **characteristic-2** counterexample: at `n = 2` the constant
`2⁴ = 0`, so the determinant vanishes while Dipper–James still gives semisimplicity.

That exclusion stands, unamended. What it excludes is a *characteristic-free* converse. The
same audit says so in its own words — *"any general Lean theorem along this route must carry
a characteristic hypothesis"* — and `twGram_det_ne_zero` carries exactly that, so the audit
predicted this theorem's shape rather than forbidding it.

**But one bullet in that audit is stated unqualified** — *"an agent hoping to get the
converse should stop: it is false"* — and read alone it closes a route that was open. It has
been scoped in place. This is the AGENTS.md over-narrowing failure mode in miniature: the
numerical finding was right, the scope sentence was one clause short, and the clause was the
one a later agent would act on.

### Independent corroboration between the two

The 2026-08-30 audit derives its obstruction as *"for `A = M_d(K)` the regular trace form is
degenerate exactly when `char K ∣ d`"*. The new Lean reaches the same place from the other
side: `regTraceForm_one_one` proves `B(1, 1) = finrank K A`, which for `M_d(K)` is `d²`. For
a prime `p`, `p ∣ d²` iff `p ∣ d` — so the two statements agree, having been obtained by
completely different arguments.

## Why the expensive route was not needed

Both prior audits price the remaining work as Geck–Pfeiffer character theory, and both are
right that **the determinant's VALUE** needs it. They are also right that the obvious
combinatorial shortcut is closed —
[`2026-09-02-tw-regular-trace-not-combinatorial.md`](2026-09-02-tw-regular-trace-not-combinatorial.md)
refutes it with an explicit `S₅` witness, and that refutation is untouched.

What changed is that **non-vanishing does not go through the value.** Semisimplicity of
`H_n(q)` is proved independently, via the Wedderburn decomposition
(`QOU.SchurWeyl.heckeWedderburn`), which owes the Gram determinant nothing. So the Gram
implication can be run backwards:

    semisimple  ⟹  regular trace form nondegenerate  ⟹  det ≠ 0, in every basis

The missing piece was the *converse of the Gram criterion*, which is three short lemmas.
`tr(L_{T_u})` for general `u` is not needed at any point, so the `S₅` witness — which closes
the search for a combinatorial `tr(L_{T_u})` — does not bear on it.

## The argument

1. **The radical is a two-sided ideal.** `regTraceForm_mul_assoc` gives `B(xy, z) = B(x, yz)`
   (both are `trace (L_z)` for the same `z`). Right-closure is immediate; **left**-closure
   needs that together with `regTraceForm_comm`, because the form is associative only in that
   one shape. Packaged as `regTraceRadical : TwoSidedIdeal A`.
2. **On a simple ring the radical is `⊥` or `⊤`**, and `⊤` would put `1` in it, giving
   `B(1,1) = 0`. With `regTraceForm_one_one` (`B(1,1) = finrank K A`, since `L_1 = id`) that
   is excluded in characteristic zero.
3. **A matrix block is simple** for nonempty index (`IsSimpleRing.matrix` over the simple ring
   `K`). Empty index is handled separately: it is the zero ring, which is *not* simple —
   simplicity requires `Nontrivial` — but whose form is nondegenerate because `0` is its only
   element.
4. **A product of matrix algebras is not simple**, so block verdicts are *summed*, not
   transported: `regTraceForm_pi`. That needed `trace_piDiag`, a genuine Mathlib gap —
   Mathlib has only the binary `LinearMap.trace_prodMap'`.
5. **Transport** to the `T_w` basis along `skeinIwahoriEquiv ∘ heckeWedderburn`.

Mathlib's `Algebra.traceForm_nondegenerate` does not apply: it is about separable field
extensions, whereas `regTraceForm x y = trace(L_{xy})` is the regular trace of a
possibly-noncommutative algebra.

## Cross-check at the one rank computed by hand

`twGram_det_ne_zero_rank_one_agrees`. `twGram_det_rank_one` evaluates the four Markov-trace
entries directly and gives `det = (1 + Q)²`; at `Q = q²` its non-vanishing is `q⁴ ≠ 1`, which
is exactly what `NotRootOfUnity q` supplies. Same conclusion, same hypothesis, two entirely
different routes — Wedderburn plus the trace-form radical, versus an explicit `2 × 2`
determinant. Kept in the Lean as a regression.

## What is still open

1. **The determinant's VALUE.** Geck–Pfeiffer 7.2.6, `det(Gram) = ∏_λ (Schur_λ)^{f^λ}`, is
   untouched and remains the book-length development `qou-kwoa` was split out to carry.
   `qou-avt2`'s symbolic characters are still the right material for it, and the `S₅` witness
   still closes the combinatorial shortcut to it. A consumer needing the Schur-element product
   gets nothing from this result.
2. **Small characteristic.** Untouched and, per the 2026-08-30 exclusion, unreachable by this
   route at all — not merely unproved.
3. **The square root.** The statement is at `Q = q²`, the same caveat as
   `isSemisimpleRing_iwahoriHecke_sq` (`qou-j377`) and for the same reason: `skeinIwahoriEquiv`
   relates the skein algebra at `q` to the Iwahori carrier at `q²`, and a general field need
   not contain a root. Removing it needs base change of `IwahoriHecke` along a field
   extension. The *hypothesis* would survive that move for free — `NotRootOfUnity Q ⟹
   NotRootOfUnity q` when `q² = Q`, since `q^m = 1` forces `Q^m = 1` — so only the algebra's
   scalar extension is missing. Over `ℝ` with `Q > 0`, or any field where `Q` is a square,
   `twGram_det_ne_zero_of_sq` already gives the statement at `Q`.

   **The obvious route to that base change is closed, and the closure is structural**
   (measured 2026-09-03, not estimated). It looks like a complete chain —
   `RingQuot.ringQuotEquivIdealQuotient` turns the algebra into an ideal quotient,
   `quotIdealMapEquivTensorQuot` base-changes an ideal quotient, `LinearMap.trace_baseChange`
   base-changes the trace. But `ringQuotEquivIdealQuotient` sits inside `section CommRing`
   with `[CommRing B]` (`Mathlib/Algebra/RingQuot.lean:470`), and `FreeAlgebra K (Fin n)` is
   **noncommutative for `n ≥ 2`** — which is this bean's entire content. The downstream piece
   fails for the same reason: Mathlib's `Ideal B = Submodule B B` is a *left* ideal, so that
   machinery is commutative-only here. Nor is there a free-algebra base change to start from:
   intersecting every file mentioning `FreeAlgebra` with every file mentioning
   `TensorProduct` or `baseChange` yields exactly one hit,
   `Mathlib/LinearAlgebra/TensorAlgebra/Basic.lean`, and that is `FreeAlgebra` being *used to
   define* `TensorAlgebra`, not a scalar-extension lemma.

   **The route that is open** does the base change on `RingQuot` directly via the universal
   property, never touching ideals — and the corpus already holds both halves of that
   property for this algebra: `QOU.SchurWeyl.iwahoriLift` (generators → `AlgHom` out) and
   `iwahori_hom_ext` (two `AlgHom`s agreeing on generators are equal), the same tools
   `skeinIwahoriEquiv` is built from. Four pieces: the tensor as an `L`-algebra whose
   `1 ⊗ σᵢ` satisfy `HeckeRel L Q n`; the two `AlgHom`s and their round trips; basis
   compatibility for `basisTwOfField` (the fiddliest); Gram compatibility, after which `det`
   commutes with a ring hom and `algebraMap` of a field is injective. Scoped in `qou-kwoa`.

## Scope

Semisimplicity and the Gram determinant are **magnitude-axis** facts. Nothing here bears on
the P≠NP wall, as `TwGram.lean` also records.

## Verification, and two harness traps found while doing it

The result was first checked file-by-file with the repo's usual `lean`-direct recipe. It was
then **re-checked against a tree with the stale dependency oleans purged and rebuilt from
source** — all six touched modules `exit 0`, and `#print axioms` on twelve declarations
returns `[propext, Classical.choice, Quot.sound]`. That second pass is the one to trust, and
it exists because the first pass could have been a false green for a reason worth recording.

> **🛑 BOTH TRAPS BELOW WERE ALREADY DOCUMENTED, and I re-derived them because I
> did not read the file that holds them.**
> [`.claude/agent-memory/lean-verifier/verification-harness.md`](../../.claude/agent-memory/lean-verifier/verification-harness.md)
> §1 is the stale-dependency false green, measured 2026-08-30; §2 is the shadowing,
> already naming `QOU/` and the mechanism (`SearchPath.findWithExt`), which is more
> precise than what I worked out. Its §3 also gives a better harness than mine — a
> complete `cp -al` hardlink mirror with `rm -f` before each write, where the `rm -f`
> is load-bearing because a truncate-in-place would corrupt the *shared inode*, i.e.
> the real build tree. I wrote straight into the real tree instead.
>
> The two are kept below as the *measurements this session added* (a fresh instance
> of each, and in the stale-cache case a new sub-shape: the restore itself is stale
> for anything merged after it was seeded, needing no edit of yours). They are not
> discoveries. The only genuinely new entry is the mtime caveat, now §9 of that file.
>
> Recorded because it is the corpus-grep discipline applied to a place I did not
> think of as a corpus: agent memory. The cost was a re-derivation and a discarded
> tool; the fix was one file read.

**Trap 1 — the `LEAN_PATH` shadowing applies to `QOU/`, not just `Mathlib/`.** Lean commits
to the *first* `LEAN_PATH` root containing the module's top-level directory and does not fall
through to later roots. So a scratch build directory works only while the **entire** cone
lives in it: the moment one olean is written there, every dependency still in the package
tree becomes invisible, and the build fails naming a file that exists one directory away.
Reproduced deliberately — after emptying the scratch dir, five of six modules failed on
dependencies that were present in `.lake/build` the whole time.

**Trap 2 — the restored olean cache goes stale, and a "skip if present" builder then verifies
new code against old dependencies.** `lake-cache/qou-<toolchain>` is a snapshot; a module
whose source has since changed has an olean that is present, loadable, and **wrong**. Proved
at the level of content, not timestamps: `QOU/SchurWeyl/HeckeWedderburnGeneral.olean` in the
restored cache contains **zero** occurrences of `NotRootOfUnity`, while the source defines
`heckeWedderburn` with exactly that hypothesis — i.e. the cache still held the pre-#6486
`ℝ`-only signature. A builder that skipped on existence typechecked against it and reported
the new code's own hypotheses as unknown identifiers.

**A caveat on my own measurement of trap 2.** A first pass counted "21 stale oleans" by
comparing mtimes. **Do not quote that number.** `git checkout` sets source mtimes to checkout
time, so an mtime comparison over a fresh clone flags files whose content never changed — and
that same unsoundness is what made an mtime-driven builder walk into Mathlib's whole import
graph. What is established *by content* is a single file, `HeckeWedderburnGeneral`; the rest
of the group is consistent with the general-field tranche having landed after the snapshot,
but it was not verified one by one.

The practical rule, which holds regardless: **after restoring the olean cache, a `lean`-direct
verification is only as current as the dependency oleans it loads.** Rebuild the cone from
source before trusting a green on any module whose dependencies this branch or a recent merge
touched.

> **🛑 THE REVERSE-CONE CHECK BELOW WAS AIMED AT THE WRONG TRANCHE, and eight modules
> went red on `main` because of it (recorded 2026-09-04).** The paragraph that follows is
> correct about what it did and is reported honestly, but it presents as reassurance a
> result that was an artifact: three of this PR's six files were **brand new**, so they had
> zero importers by construction, and "exactly one consumer outside what had been rebuilt"
> measured that fact rather than any safety.
>
> The tranche that actually had consumers was the **earlier** one — #6486's retype of
> `seminormalRep`'s hypothesis `q ^ 2 ≠ 1 → GenericParameter.NotRootOfUnity q` (commit
> `e526464c2d`), which covered nine modules and not their consumers outside the tranche.
> **Eight modules broke on `main`**: `HoefsmitRepGeneral` (2 sites), `SeminormalBlockTrace`
> (4), `SeminormalBlockEquality` (5), `SeminormalCornerTrace` (2), `MarkovAssembly` (1),
> `MarkovTraceInstance` (4), and on a second pass `WenzlMarkovLevelR` (2) and
> `WenzlMarkovTraceInstance` (15). A sibling session found them with a full-cone rebuild and
> fixed them in `794c34897d` and `cbf2202f43`; both are on `main`.
>
> **The rule the incident yields:** run the reverse cone against every declaration whose
> *signature* changed, not against the files you touched. A new file has no consumers by
> construction; a retyped hypothesis on an existing declaration has as many as the corpus
> has callers. Recorded as §13 of the lean-verifier harness memory.
>
> One further correction to this corpus's own wording: the tranche bean recorded
> `HoefsmitRepGeneral ← OFF the general path`. Off-path meant *this change does not need
> it* — not that it does not need this change. It is a consumer of `seminormalRep`, and it
> broke.
>
> A separate alarm raised at the same time — *"`HeckeSemisimpleGeneral` is red on `main`"* —
> was **retracted** by its author: it was measured against their own stale cached
> dependency oleans, the exact trap §1/§11 of that memory records. With the cone rebuilt,
> this PR's files compile clean on `main`.

**And the reverse-import cone, which the first pass here also skipped.** §1 of that memory
prescribes checking the modules that *import* what changed, not only the dependencies it
builds on. Done: of the six files this PR touches, five have importers, and exactly one —
`QOU/SchurWeyl/HeckeSemisimpleReal.lean` — lay outside what had already been rebuilt. It
compiles `exit 0`. The change it consumes is docstring-only (every changed line of
`HeckeSemisimpleGeneral.lean` sits inside the module `/-! -/`), so it could not have broken;
the point is that "could not have broken" was an argument, and the memory asks for a build.
