# T3g carrier 3 has no formal content — and I said otherwise an hour ago

**Date:** 2026-08-26 · **Branch:** `claude/8-fold-way-qou-k4e8ch` (PR #5819)
**Bean:** `qou-y7vg`

## The correction, first

The step-1 audit
([`2026-08-26-t3g-step1-name-the-base.md`](2026-08-26-t3g-step1-name-the-base.md))
called `def:categorical-mordell-weil` **"a stronger carrier than the fivefold
remark: a `definition` with a `.lean` sibling, not a `remark."`**

**That was wrong, and it was wrong in the direction that flatters the finding.**
I read the manifest — `kind: definition`, `lean.ref` present — and inferred
formal content from the shape of the metadata without opening the file. The
whole sibling is:

```lean
def CategoricalMordellWeil   :=
  -- Ref: [manuscript] def:categorical-mordell-weil
  trivial
```

`trivial : True`, so the inferred type is `True`. This is `def : True := trivial`
— the **`def-disguised-true`** pattern that AGENTS.md §1a names as a forbidden
audit-dodge. A `.lean` sibling whose body is `trivial` is not stronger evidence
than no sibling at all; it is weaker, because it reads as formalised.

**Both candidate carriers for T3g's existence premise are prose.** The fivefold
block is a `remark` with no Lean; this one is a `definition` whose Lean is a
tautology. Neither supports the gerbe claim formally.

## The three-part defect

Recorded precisely because it is in someone else's block and should be repaired
by whoever owns that chapter, not drive-by.

**1. The sibling is a disguised `True`.** As above.

**2. Its header makes a false locational claim.** The file says:

> The compiled formalisation lives under `QOU/AppendixSurreals/`; this content
> block names the construction.

`QOU/AppendixSurreals/` exists and contains ~200 files. **None of them declares
`CategoricalMordellWeil`.**

**3. The `lean.ref` shadows a real declaration that lives elsewhere.** The
manifest declares `lean: { ref: "qou:QOU.AppendixSurreals.CategoricalMordellWeil",
validation: "not_checked" }`. The real declaration exists — but at
`QOU/QBirchSwinnertonDyer.lean:65`, inside `namespace QOU`, so its full name is
`QOU.CategoricalMordellWeil`:

```lean
def CategoricalMordellWeil (E : C) : Type v :=
  (𝟙_ C) ⟶ E
```

with a companion `theorem descartes_rank_zero`. That is real content. Because
`lean.ref` resolution checks the **sibling first**, the stub wins and the real
declaration is shadowed — the §0a *"🚫 No shadowing stubs"* case, whose
prescribed repair for a mis-named target is to *align the file or the ref so
candidate 2 resolves*, not to paper over it.

Note the repair is not simply "delete the sibling": a `definition` block requires
one at type level. So the fix is to make the sibling carry the real content, or
to re-point the `lean.ref` and give the sibling a genuine body. Which of those is
right depends on where the author wants the declaration to live, so it is not an
agent's call.

## And the real declaration has no gerbe content either

`QBirchSwinnertonDyer.lean` defines the Mordell–Weil group as `Hom(𝟙, E)` and
proves `descartes_rank_zero`. Searching it for `gerbe`, `atlas`, `spectral base`
returns **one** hit, and it is the phrase "fibre functor" inside a docstring
about chord-tangent addition.

So the sentence T3g needs —

> The fibre functor atlas of the QOU forms a `G`-gerbe over the spectral base.

— has **no formal backing anywhere**: not in the stub, which is `trivial`, and
not in the real declaration, which is about Hom-spaces.

## A detector blind spot, measured rather than inferred

The `def-disguised-true` criterion exists precisely for this pattern. It did not
fire here.

Measured by running the audit, not by reading its source: it scanned **3193
`.lean` files** and reported **134 defect candidates across 154 files**.
`categorical-mordell-weil.lean` is **not among them**, while
`proof-no-trivial-true` does fire on other files in the same run (for instance
`e-hartree-categorical-derivation.lean:103`, exempt as a §3b conjecture
placeholder). The criterion is live; it simply does not see this declaration.

The likely reason is that the pattern test keys on the **declared conclusion**,
and `def CategoricalMordellWeil := trivial` **has no type ascription** — there is
no `True` written down to match, only an inferred one. That is an inference about
the cause; the *blindness itself* is the measurement above.

This looks like a new entry for
[`2026-08-15-detector-blindness-taxonomy.md`](2026-08-15-detector-blindness-taxonomy.md),
which already catalogues thirteen detector-blind spellings — four of them found
*by* detectors written to catch the previous blind spot.

**Not fixed here, deliberately.** Widening the criterion to catch un-ascribed
`def x := trivial` touches a checker that runs over 3193 files, and `trivial` is
a legitimate body in contexts this would newly flag. A change like that needs a
measured false-positive count and a selftest before it lands, which is its own
piece of work and not this branch's.

## What it means for T3g

Carrier 3 joins carrier 1: an assertion in prose. `qou-y7vg` should cite it —
it is still the closest thing in the corpus to T3g's own claim, and it names the
spectral base — but it cannot be promoted, and nothing should be built on it as
though it were established.

The base question from the step-1 audit is unchanged and still needs the author.
