# `BlowupYekutieli` cannot be transcribed because there is nothing to transcribe from

**Date:** 2026-08-30 · **Bean:** `qou-88nf` (parent `qou-rq9n`)
**Companion:** [`2026-08-30-qns-carriers-are-refutable.lean`](2026-08-30-qns-carriers-are-refutable.lean)

---

## The question

Four of the five q-NS conjecture carriers in
[`lean/QOU/AlgebraicSubstrate/ConditionalClasses.lean`](../../content/quantum-observable-universe/lean/QOU/AlgebraicSubstrate/ConditionalClasses.lean)
were re-encoded on 2026-08-30 by **transcribing the claim each docstring
already made**. `BlowupYekutieli` was left vacuous, on the stated grounds that
its docstring names *"an explicit constant determined by the substrate scale"*
and never says which.

The obvious next step is to go and find that constant. This audit is the result,
and the answer is not "I could not find it".

## The finding

**The corpus's "Yekutieli" is Amnon Yekutieli, *Central Extensions of Gerbes*
(Adv. Math. 225(1), 2010) — a pure-algebra paper. He has no blow-up rate, and
neither does this corpus.**

What the name denotes here, counted over live `content/` (`.md`/`.ts`/`.lean`):

| phrase | occurrences |
|---|---|
| Yekutieli lifting | 92 |
| `YekutieliTriple` | 44 + 42 |
| Yekutieli obstruction | 25 + 20 |
| Yekutieli Stokes | 21 + 8 |
| Yekutieli tower | 6 |
| Yekutieli volume | 2 |
| **Yekutieli blow-up rate / exponent** | **0** |

Every one is the gerbe-lifting/obstruction framework (`κ_n ∈ H²(𝒮, ℬ)`) or the
non-abelian Stokes theorem in the canonical derivation chain. **None is a
fluid-dynamics blow-up rate.**

Corpus-grep, all six paths:

| path | result |
|---|---|
| `docs/audits/` | no rate; hits are this carrier's own audit trail |
| `content/` | `blow-up exponent` appears **once**, in the carrier's own docstring |
| `computations/` | `yekutieli-volume-join.witness.json` (volume, not a rate); the rest `_deprecated/` |
| `docs/coordination/` | one hit, and it is explicit: *"Not the q-NS PDE solve (blowup exponent) — survey research target"* — i.e. recorded as **not done** |
| `library/` (ingested sources) | 3 documents mention Yekutieli; **none** pairs him with blow-up |
| `.beans/` | hits are this bean and its parent |

## Why this makes the carrier different in kind from its four siblings

The other four are backed by a content block that states the claim:

| carrier | conjecture block |
|---|---|
| `QAubinLions` | `fluid-dynamics/q-aubin-lions.ts` |
| `NSCounterexample` | `fluid-dynamics/p5-counterexample.ts` |
| `CriticalExponent` | `fluid-dynamics/p2-critical-exponent.ts` |
| `RegularityBreakdown` | `fluid-dynamics/regularity-breakdown.ts` |
| **`BlowupYekutieli`** | **none — 0 `.ts` blocks declare `conj:blowup-yekutieli`** |

The Lean carries `-- Ref: [manuscript] conj:blowup-yekutieli`, and that label is
declared by no content block in the corpus. The four transcriptions were
possible because there was an upstream statement to transcribe; here the
citation resolves to nothing.

> **🛑 CORRECTED 2026-08-30, later the same day (bean `qou-4670`). The
> paragraph below said the `p3-blowup-yekutieli` block is gone. It is not — it
> MOVED, and it is live.**
>
> I asserted: *"A `p3-blowup-yekutieli` block did once exist — under
> `ch10-fluid-dynamics/` and `ch6-descartes-universe/`, plus a
> `fluid-dynamics/p3-blowup-yekutieli.lean`, none of which is on disk now."*
> I had searched the chapter directories the block used to sit in, found
> nothing, and stopped. It is at
> [`lifting-and-descent/p3-blowup-yekutieli.ts`](../../content/quantum-observable-universe/lifting-and-descent/p3-blowup-yekutieli.ts),
> with its `.md`, its `.lean` and a `.qa.json` sidecar — a full live block.
>
> **The table above is literally true and its inference is not.** Zero `.ts`
> blocks declare `conj:blowup-yekutieli`, because the live block's label is
> **`prop:blowup-yekutieli`** — a *proposition*, not a conjecture. Ten other
> blocks `interprets` or `uses` it. So the sentence *"the citation resolves to
> nothing"* is right about the citation and wrong about the corpus: the Lean's
> `-- Ref: conj:blowup-yekutieli` points at a label nobody declares, while the
> statement it is named for is one directory over under a different kind.
>
> **What that block actually carries**, in `QOU.FluidDynamics.BlowupYekutieli`:
> a `smooth : Prop`, an `obstruction : ℕ → ℕ`, and the definitional field
> `smooth ↔ ∀ n, obstruction n = 0` — with a *derived*, sorry-free theorem
> `blowup_yekutieli` getting the blow-up direction by contraposition. That is a
> §3b-cond non-degenerate carrier, and it is nothing like the local class of
> the same name, whose entire content is `∃ r, 0 ≤ r ∧ r ≤ 1 + T`.
>
> **What survives unchanged.** The finding this audit is titled for stands:
> there is no Yekutieli blow-up *rate* in the corpus, the six-path grep is
> unaffected, and no bound can be transcribed. What changes is the disposition
> — see the correction under §Disposition below, where option 2 was resting on
> this error.

Superseded text follows. **A `p3-blowup-yekutieli` block did once exist** —
under `ch10-fluid-dynamics/` and `ch6-descartes-universe/`, plus a
`fluid-dynamics/p3-blowup-yekutieli.lean`, none of which is on disk now.
Recovering the last committed `.md` does **not** supply the missing rate: its
content is the *regularity-breakdown* argument — smoothness as lifting through
the brane tower, `v` smooth ⟺ `κ_n(v) = 0` — with no blow-up exponent in it.

(That last sentence was correct about the *content*, and is in fact the whole
point: the block states the lifting-obstruction claim and no rate.)

## What this is, in the corpus's own taxonomy

This is the **borrowed-name** defect that sibling bean `qou-0avp` targets: a
declaration named after an external theory whose statement is entirely local.
The name `BlowupYekutieli` suggests an external result bounding a blow-up rate.
Amnon Yekutieli's paper is about central extensions of gerbes and says nothing
about fluid blow-up; the corpus's own Yekutieli material is lifting and Stokes;
and the encoded bound `1 + T` involves no substrate scale and is satisfied by
`r = 0` — by **no blow-up**, the negation of the claim the carrier is named for.

## Scope of this negative — (a), not (b)

Per AGENTS.md §"Before declaring refuted / ruled out", this is a
**scope-limited negative**: *this corpus, as of 2026-08-30, contains no
Yekutieli blow-up rate, and the conjecture label the carrier cites is declared
by no content block.* Six grep paths, listed above.

It is **not** a structural exclusion. It does not say no such rate exists or
could be derived — only that it is not here to be transcribed, which is what
the encoding needed.

## Disposition — authorial, and the choice is now a real one

Deliberately **not** done here: no bound was written. Choosing an `f(q₀)` would
produce something that looks exactly like the four sibling fixes and is a fitted
value wearing their clothes — the anti-laundering rule this whole arc is about.

> **🛑 The three options below were written believing the `p3` block was
> deleted. It is live (see the correction above), and that collapses the choice
> — option 2 is no longer a speculative rename, it is a transcription with a
> named source.**
>
> **Recommended, and this is my judgement rather than a finding: option 2.**
> The local class should be re-encoded against
> `QOU.FluidDynamics.BlowupYekutieli` — `smooth ↔ ∀ n, obstruction n = 0` —
> exactly as the other four were transcribed from their upstreams, and its
> `-- Ref:` corrected from the non-existent `conj:blowup-yekutieli` to the live
> `prop:blowup-yekutieli`. That needs no new mathematics, no rate, and no
> number chosen by an agent: the statement exists, is proved-from in
> `blowup_yekutieli`, and is refutable (an `obstruction` that vanishes
> everywhere while `smooth` is `False` falsifies it).
>
> **The rename question is separate and stays open.** Whether the *name*
> `BlowupYekutieli` should survive is the borrowed-name issue below (`qou-0avp`)
> and is genuinely authorial; transcribing the upstream content does not settle
> it, and can be done under either name.
>
> Option 1 stays available and stays the more ambitious one: if the framework
> does claim a blow-up *rate*, that is a conjecture block nobody has written,
> and this audit's six-path grep says so. Option 3 is unaffected.

Superseded text follows. Three options, none of which is mine to take:

1. **Write the missing conjecture block.** Someone states the q-NS blow-up rate
   as an explicit function of the substrate modulus, `conj:blowup-yekutieli`
   gets a content block like its four siblings, and the carrier is then
   transcribed exactly as they were.
2. **Rename the carrier.** If the intended content is the *lifting obstruction*
   (which is what the corpus's Yekutieli material actually is, and what the
   deleted `p3` block contained), the name is wrong and the fix is a rename plus
   an encoding against `κ_n`, not a blow-up bound.
3. **Retire it.** If the blow-up leg is not a claim the framework makes, the
   carrier and its `[BlowupYekutieli]` binders come out. Note it currently has
   **one** live consumer leg — the fourth conjunct of
   `qNS_cone_full_composition`, which is the one conjunct still satisfied by
   zero.

Until one of those, the carrier stays as it is, flagged at the declaration and
adjudicated `genuine` in the vacuity ledger.
