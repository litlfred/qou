# 4-C is mis-framed: no third flavour grade is missing

**Status:** CORRECTION to a standing reference and a live `todo` bean. No new
compute; the resolving theorem is already on `main`, sorry-free, and this audit
only reads it. Beans `qou-dnm1` (todo), `qou-mesont3`, `qou-qpj9`.

## The claim as it currently stands

[`sm-eightfold-derivation-cheat-sheet.md` §4-C](../sm-eightfold-derivation-cheat-sheet.md)
names the second of the framework's three gating objects **"A third flavour
grade (strangeness / charm Cartan)"**, ranks it **2** in the near-term table,
and states:

> *"`(n, T₃)` separates all six quarks (§3.2, sorry-free), but **still
> collides** `D̄⁰{c̄,u}` with `K⁰{d̄,s}` (same multiset).
> `mass_from_graded_content_cannot_separate` is proved: the mass is **not** a
> function of `(n, T₃)`. The missing grade is the **flavour** `SU(3)` Cartan …
> So 4-C reduces into 4-A."*

Bean `qou-dnm1` (`todo`) carries the same framing and four attack options:
extend GMN to `Y_f = B + S + C`; find *"a third knot grading orthogonal to
`(n, T₃)`"*; build a *"flavour `SU(3)` weight lattice from Bring/icosahedral
geometry"*; or a `q`-graded flavour index.

## Why it is wrong

**The corpus already resolves the collision, sorry-free, and says so.**
[`MesonOperatorSelectionT3.lean`](../../content/quantum-observable-universe/lean/QOU/ParticleInteractions/MesonOperatorSelectionT3.lean)
defines two content maps:

```lean
def gradedContent  (m : Meson) : Multiset ℤ :=          -- symmetric
  {- signedWrithe (constituents m).1, signedWrithe (constituents m).2}

def orderedContent (m : Meson) : ℤ × ℤ :=               -- keeps the bar
  (- signedWrithe (constituents m).1, signedWrithe (constituents m).2)
```

and proves both of:

| theorem | content |
|---|---|
| `graded_D_K0_collide` | `gradedContent D̄⁰ = gradedContent K⁰` — the multisets collide |
| `orderedContent_injective` | `Function.Injective orderedContent` — **`by decide`, sorry-free** |

`D̄⁰` is `(−5, +3)` and `K⁰` is `(+3, −5)`. **These collide only as multisets.**
The ordered pairs are different, and the ordering is not a tiebreaker bolted on
for the purpose — it is the quark/antiquark strand orientation, the same
`signedWrithe` datum that produces `T₃`. The theorem's own docstring says so:

> *"Keeping the quark/antiquark orientation (the "bar" — itself topological
> strand-orientation data, not a fit) separates `D̄⁰ (−5,+3)` from `K⁰ (+3,−5)`.
> The residual collision is an artefact of the **symmetric-multiset** content
> model of #4614, not of the physics; the bar resolves it."*

**So there is no missing grade, and the four attack options in `qou-dnm1` are
searching for an object that is not absent.**

## The arity conflation that produced it

`mass_from_graded_content_cannot_separate` is real and is correctly proved. Read
its type:

```lean
theorem mass_from_graded_content_cannot_separate (f : Multiset ℤ → ℚ) :
    (fun m => f (gradedContent m)) .Dmeson = (fun m => f (gradedContent m)) .K0
```

It quantifies over `f : Multiset ℤ → ℚ` — **symmetric** functions of the
multiset. It says: *no symmetric function of the unordered content separates
these two.* It does **not** say the content cannot carry the mass, which is the
stronger claim the cheat sheet and `qou-dnm1` both read off it. The complement
is `orderedContent`, and that one is injective.

This is the `da-arity-conflation` class in
[`local/devils-advocate-watcher`](../../.claude/skills/local/devils-advocate-watcher.md)
— a quantifier read one binder too wide — and it is the fourth instance of that
class recorded in this corpus.

**How it propagated is worth recording**, because the file contains both the
error and its correction *adjacent*. The docstring on `graded_D_K0_collide`
ends: *"a further flavour grading (charm number vs strangeness) is the
remaining missing datum."* The **very next theorem** in the same file refutes
that sentence. A reader who stopped at the collision docstring — which is where
the section heading `### The honest remainder — residual content collision
(needs a 3rd grade)` invites you to stop — carried the stale half downstream
into the ledger, the bean and the cheat sheet.

A prior agent caught this on `qou-mesont3` and wrote it up correctly
(*"Obstruction A is purely geometric, not a missing grade … do not chase a
third flavour grade"*). That note never reached the cheat sheet or `qou-dnm1`,
both of which still direct effort at the non-problem. Re-verified here at
source rather than taken from the bean.

## What this does and does not establish

**Removed:** the claimed information-theoretic obstruction at the content
level. No third flavour grade is missing; `qou-dnm1`'s premise is void as
stated.

**NOT established — and the distinction is the whole point:** that the D-meson
mass is derived, or derivable. Injectivity guarantees a factorisation *exists*
(an injection admits a left inverse on its image); it says nothing about
whether the factorising map is canonical, parameter-free, or derivable. Fitting
a function through five injectively-labelled points is precisely the per-state
fit the J/ψ attack already recorded as worthless. `sorry-free ≠ derived`
applies here in its usual form.

**What actually remains** is `qou-qpj9`'s Obstruction A: a canonical,
parameter-free map from the ordered content to a hyperbolic braid word at
`H₃(q)`. The `(n, T₃)` content is `Vol = 0` torus-carrier data
(`MesonFluxTubeReduction.twoStrand_winding_bijective`), and nothing yet derives
the braid whose volume the mass law reads. That is **geometric**, and it is a
far better-posed target than "find a missing invariant".

## The consequence that matters for the ranking

**4-C does not reduce into 4-A.** The cheat sheet's *"So 4-C reduces into 4-A,
but with a much more concrete target"* is the load-bearing error: it places the
rank-2 near-term object behind **4-A**, the `N = 3` problem — the framework's
hardest open question, with seven excluded routes and one surviving lead.

If no flavour grade is missing, that dependency is not there. 4-C gates on a
geometric construction that needs no `SU(3)`, flavour or colour. This moves the
rank-2 target from *blocked behind the hardest open problem* to *blocked on a
well-posed construction* — without making it any more solved.

## Scope

**(a) scope-limited negative on a FRAMING**, not on a result. Nothing proved is
withdrawn: `mass_from_graded_content_cannot_separate`, `graded_D_K0_collide`
and `gradedContentExt_not_injective` all stand exactly as proved. What is
corrected is the inference drawn from them, at three sites.

## Sites corrected

- `docs/sm-eightfold-derivation-cheat-sheet.md` §4-C and the §8 rank-2 row.
- `docs/coordination/sm-26-parameter-chip-away.md` — the D-meson "gates on
  exactly TWO objects" entry, whose object 1 is the void one.
- Bean `qou-dnm1` — body appended; **status left alone** (closing is the
  author's call), with a recommendation to re-scope onto `qou-qpj9` rather
  than continue the four attack options.
- `MesonOperatorSelectionT3.lean` — the `graded_D_K0_collide` docstring and the
  section heading that invite stopping before the resolution. Left as a
  follow-up: the theorems are correct and I would rather not touch proved Lean
  to fix prose in the same pass as an audit.
