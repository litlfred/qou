# Can the `TL_n` route discharge the Wenzl 1988 dependency?

**Verdict: NO. The route does not close, and its stated justification has
lapsed.** Two independent reasons, either sufficient on its own. A weaker but
genuine result *is* reachable, and is proved here.

Lean: [`QOU/QBeta/VanishingSetUnderdetermines.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/VanishingSetUnderdetermines.lean)
(new, 207 lines, sorry-free)
· prior scoping [`2026-08-16-ocneanu-weight-axiomatisation.md`](2026-08-16-ocneanu-weight-axiomatisation.md)
· prior result [`2026-08-16-tl-all-n-weight-vanishing.md`](2026-08-16-tl-all-n-weight-vanishing.md)

## The dependency

[`WenzlWeightVanishing.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/WenzlWeightVanishing.lean)
proves `schurPrincipal r Q μ / Z = 0 ⟺ ℓ(λ) > r` **unconditionally** — about an
explicit named expression. Reading that expression as the mass channel's
*actual Ocneanu weight* is Wenzl (1988), axiomatised in
[#5230](https://github.com/litlfred/qou/pull/5230) as
`IsOcneanuWeightSystem Q z r y` and threaded via `_of_wenzl`. Its two fields,
read verbatim from the current file:

```lean
markovParameter_eq : z * (1 - Q ^ r) = Q ^ r * (1 - Q)
weight_eq_schurPrincipal :
  ∃ Z : R, Z ≠ 0 ∧ ∀ μ : YoungDiagram, y μ = schurPrincipal r Q μ / Z
```

The first is pure algebra in `(Q, z, r)` and is not the external input. The
second is Wenzl. `#print axioms` cannot see it (bean `qou-fpjy`): the three
`_of_wenzl` rows are byte-identical to the unconditional ones.

## The candidate route

[`2026-08-16-ocneanu-weight-axiomatisation.md`](2026-08-16-ocneanu-weight-axiomatisation.md)
§"Is there a cheaper route?" costed one candidate:

> prove only the **vanishing set** via `TL_n` … which **skips items 5 and 6
> entirely**, i.e. the whole symmetric-function and hook-content stack.

resting on a stated premise:

> What the corpus actually consumes downstream is not the *values* `y_λ` but
> the *vanishing set*.

## Reason 1 — the premise is false as of today

[PR #5353](https://github.com/litlfred/qou/pull/5353) (`qou-q2oa`, open,
head `5613d15704`) is deriving the Q_β ladder phase as

```
α_D = (h/4)·( y₍₃₎·[2]_q + h − 2 )
```

from `y₍₃₎ = (q⁴+1)/(q²+1)²` — a weight **value**. The vanishing set supplies
only `y₍₁³₎ = 0`; it says nothing whatever about `y₍₃₎`. So a live sibling is
consuming exactly what the route proposes to stop proving. The premise was
defensible when written on 2026-08-16 and is not defensible now.

This is not a scheduling accident. `y₍₃₎` and `y₍₂,₁₎` are the surviving
two-row blocks — the ones the level-2 cap *keeps* — and the cap is what makes
them the whole story. A route justified by "only the vanishing set matters"
is in tension with the cap's own consequence, which is that the surviving
values now carry all the content.

## Reason 2 — the saving is orthogonal to the blocker

The prior audit listed seven build items and noted the route "still needs
items 1–4." That is correct but understates it. Sorting the seven by
difficulty against the corpus as it actually stands:

| Item | Route | Corpus status |
|---|---|---|
| 1. `S_n` as a Coxeter group of type A | still needed | absent |
| 2. `H_n(q)` and its `T_w` basis (Matsumoto) | still needed | **absent — the sharp gap** |
| 3. Generic semisimplicity | still needed | hypothesis-carrying only (below) |
| 4. Irreps indexed by partitions | still needed | absent |
| 5. Trace decomposition `tr = Σ y_λ χ_λ` | **skipped** | class *field*, not a theorem |
| 6. Schur principal specialisation | **skipped** | **already proved, twice** |
| 7. Wenzl's theorem | the target | — |

The two items the route saves are the two the corpus has *already done* or does
not need done:

- **Item 6 is done twice over, unconditionally and sorry-free.**
  `WenzlWeightVanishing.schurPrincipal_eq_zero_iff` (generic `[Field R]`, all
  `r`, all `λ`) and
  [`MathlibExt/TLContentStratification.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/TLContentStratification.lean)
  `schurElement_tl_eq_zero_iff_numCols_gt` (over `ℝ`, 12 theorems, 0 classes)
  are two independent formula-side vanishing theorems. Note the second is the
  **conjugate** statement (columns, not rows) — its own header flags this,
  arising from the opposite sign convention `X = Q^{-N}`, and it was
  adjudicated separately as bean `qou-25k5` (completed). Neither mentions an
  algebra.
- **Item 5 is not a theorem to be saved.** `Hecke/Wedderburn.trace_decomposition`
  is `exact WD.trace_decomp x` — a projection of a class field (bean
  `qou-luq7`, confirmed by reading the file). Skipping it saves nothing,
  because nothing was spent.

Meanwhile items 2 and 4 — the entire difficulty — are untouched by the route.
So the trade is: pay the whole cost, save the part already paid.

**And the route does not escape item 4, contrary to first appearance.** `TL_n`'s
cell modules are indexed by through-strand count (Catalan-many), not by
partitions. To phrase the conclusion in the corpus's indexing — `y : YoungDiagram
→ R` — you must map TL block labels back to `≤ 2`-row partitions, which *is* the
partition-indexing of `H_n` irreps restricted to the quotient. The prior audit's
own words for item 4 apply unchanged: *"the indexing set … has no home in Lean
without it. The statement cannot be written down."*

## What the algebra side actually contains (measured)

Because the route's cost turns on it, the algebra-side inventory was measured
rather than assumed. The sibling `infra-ledger` is building the general
proved-vs-axiomatised ledger; this is only the slice bearing on Wenzl.

- **`Hecke/Wedderburn.WedderburnDecomp` has no instance anywhere.**
  `grep -rnE '(instance|example|def)[^:]*:\s*WedderburnDecomp\b'` over
  `content/**/lean/QOU` returns empty. Its `y_lambda : Partition n → R` — the
  corpus's only algebra-attached Ocneanu weight — is therefore an unconstructed
  class field.
- **Concrete `HeckeAlgebra` carriers do exist** (`instHeckeAlgebraH2`,
  `instHeckeAlgebraH3A`, `instHeckeAlgebraH4A`), so item 2 is not at zero at
  small `n`. It is at zero *in general*, which is what the route needs.
- **`HeckeGenericSemisimple.lean` is hypothesis-carrying, by design.** Both its
  theorems take the Gram–factorial identity `hgram` as an explicit argument; its
  own header calls that "the one thing the concrete Iwahori–Hecke construction
  must still supply." Item 3 is staged, not done.

### A collision worth fixing separately

Three distinct objects share one name, which is the AGENTS.md registry §2
hazard ("attributes do not transfer across overloaded symbols"):

| Name | Where | What it is |
|---|---|---|
| `Hecke.WedderburnDecomp` | `Hecke/Wedderburn.lean:72` | content-bearing class, **no instance** |
| `Mathlib.WedderburnDecomposition` | `Mathlib/HeckeAlgebra.lean:118` | class with `Prop`-**variable** fields |
| `HeckeAlgebra.WedderburnDecomposition` | `HeckeAlgebra/Wedderburn.lean:68` | an `abbrev` for a **Type** |

The middle one deserves a flag on its own. Its fields are
`blocks_sum_to_one : Prop` plus `blocks_sum_holds : blocks_sum_to_one` — a Prop
*variable*, not the proposition it names — and `instance triv_wedderburn`
discharges it globally with `True` over `carrier := PUnit`. So it asserts
nothing and is found by typeclass search. That is the `proof-claims-unencoded`
/ `true-class-field` pattern of AGENTS.md §3b-tax, and it is the precise
failure `IsOcneanuWeightSystem` was designed to avoid — its docstring says the
satisfiability witness is "deliberately **not** registered as an `instance`, so
typeclass search can never silently discharge the hypothesis." Filed as
`qou-h56b`; not fixed here, since it is not on the Wenzl path.

## The weaker genuine result, proved

The route would replace `weight_eq_schurPrincipal` by a vanishing-set field.
That trade is now measured rather than estimated.

| Declaration | Statement |
|---|---|
| `schurPrincipal_bot` | `s_⊥ = 1` — the normalisation point |
| `ocneanuWeight_bot_ne_zero` | `y ⊥ ≠ 0`, from the class fields (no genericity hypothesis) |
| **`ocneanuWeight_eq_bot_smul_schurPrincipal`** | **rigidity: `y μ = y ⊥ · s_μ`** |
| `ocneanuWeight_unique_of_bot_eq` | two systems agreeing at `⊥` are equal |
| `rescaleAt`, `rescaleAt_self`, `rescaleAt_of_ne` | one-point rescaling |
| `rescaleAt_eq_zero_iff` | rescaling preserves the vanishing set exactly |
| **`vanishingSet_not_determines_weights`** | **the vanishing set does not determine `y`** |
| `rescaled_two_one_not_weight_system` | the gap concretely, at `Q = 2` over `ℚ` |

**Rigidity** says `IsOcneanuWeightSystem` pins `y` completely up to the single
scalar `y ⊥`: the normaliser `Z` is not free once `y ⊥` is known, it is
`1 / y ⊥`. **The refutation** says the vanishing set pins nothing of the sort —
given any genuine weight system, rescaling its value at one surviving diagram
by `c ∉ {0,1}` preserves the vanishing set *exactly* and destroys the class.

So the vanishing-set hypothesis is **strictly** weaker, and a consumer of
weight values — #5353 — is not served by it. That closes the loop with Reason 1:
the route's saving and the route's justification fail for the same underlying
reason, that the surviving values carry content the vanishing set does not.

The concrete case uses the two blocks #5185 measured: doubling `y₍₂,₁₎` at
`Q = 2` over `ℚ` still kills `(1³)`, still spares `(2,1)`, and is not a weight
system at any Markov parameter.

### Not a discharge, and not a step toward one

These are measurements of a proposed weaker hypothesis, not progress on Wenzl.
Nothing here constructs `H_n(q)`, and no declaration in `WenzlWeightVanishing`
becomes unconditional. The three `_of_wenzl` statements remain conditional and
must still be cited as *"proved conditional on Wenzl 1988"*.

In particular **no new class was introduced.** Discharging a class by adding
another that assumes the same content is the anti-laundering failure
(AGENTS.md §"Axiomatization is NOT a Proof"); the file adds only theorems and
one `noncomputable def`.

### Non-degeneracy

`vanishingSet_not_determines_weights` carries three side conditions on top of
the class (`μ₀ ≠ ⊥`, `y μ₀ ≠ 0`, `c ∉ {0,1}`), so it would prove nothing if
those were never jointly satisfiable. `rescaled_two_one_not_weight_system`
meets all three concretely, reusing the file's own
`isOcneanuWeightSystem_schurPrincipal` and `discriminates_at_n_three`.

The load-bearing lemma is `ocneanuWeight_eq_bot_smul_schurPrincipal`: delete it
and the argument does not go through, because nothing else forces the value at
`μ₀`. It is derived from `weight_eq_schurPrincipal`, not projected out of it —
the class has no field mentioning `y ⊥`, and no field mentioning vanishing.

## Verification

`lean`-direct against the real import cone, **exit 0, no warnings**. Not via
`lake build`: this tree's oleans are the main checkout's, used read-only, and
`lake build` would evict them (bean `qou-r13s`). Toolchain `lean 4.24.0`
(`797c613eb9b6d4ec95db23e3e00af9ac6657f24b`); mathlib olean count **6990**
before and after.

```
'…schurPrincipal_bot'                          [propext, Classical.choice, Quot.sound]
'…ocneanuWeight_bot_ne_zero'                   [propext, Classical.choice, Quot.sound]
'…ocneanuWeight_eq_bot_smul_schurPrincipal'    [propext, Classical.choice, Quot.sound]
'…ocneanuWeight_unique_of_bot_eq'              [propext, Classical.choice, Quot.sound]
'…rescaleAt'                                   [propext, Classical.choice, Quot.sound]
'…rescaleAt_self'                              [propext, Classical.choice, Quot.sound]
'…rescaleAt_of_ne'                             [propext, Classical.choice, Quot.sound]
'…rescaleAt_eq_zero_iff'                       [propext, Classical.choice, Quot.sound]
'…vanishingSet_not_determines_weights'         [propext, Classical.choice, Quot.sound]
'…rescaled_two_one_not_weight_system'          [propext, Classical.choice, Quot.sound]
```

No `sorryAx`. Grep for `sorry|native_decide|axiom|: True|:= trivial` returns
nothing. Generic `{R : Type*} [Field R]` throughout — no ordering, no `ℝ`, no
archimedean construct (§7c); the one `ℚ` instantiation is the concrete
non-example, which nothing above it consumes.

This is a standalone library file with no `.qa.json` sidecar, so nothing but
this check covers it (AGENTS.md §"QA is agent-owned").

## Recommendation

1. **Do not walk the `TL_n` route.** It saves the two items already done and
   pays the two that were never started, and its justification is falsified.
2. **Do not re-scope `IsOcneanuWeightSystem` around the vanishing set.** That
   would weaken a hypothesis a live PR depends on for values. Recorded as the
   negative it is — scope **(a)**, a scope-limited negative about *this route*,
   not a structural exclusion of `TL_n` from any future argument. No invariant
   forbids a `TL_n` ingredient; what is refuted is this route's economics.
3. **The full route stands as the prior audit scoped it** — Mathlib-contribution
   scale, items 1–4 first. Item 1 (`A_n` presents `S_n`) remains the smallest
   independently-worthwhile piece.
4. **Fix the `WedderburnDecomp*` collision separately** (`qou-h56b`), in
   particular the `Prop`-variable class with a global trivial instance.
