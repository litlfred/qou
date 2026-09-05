---
# qou-yos9
title: 'RSKDimIdentity may be dischargeable: rskBurnsideHolds proves it for all n, unverified by print axioms'
status: in-progress
type: task
created_at: 2026-09-05T18:46:54Z
updated_at: 2026-09-05T18:46:54Z
---


`QOU/HeckeAlgebra/WedderburnConstruction.lean` (bean `qou-usol`, PR #6848)
isolates the Robinson–Schensted–Knuth dimension identity as an explicit
hypothesis:

    def RSKDimIdentity (n : ℕ) : Prop :=
      ∑ lam : Nat.Partition n, seminormalDim lam ^ 2 = heckeDim n

and its docstring says the identity "is available only conditionally", citing
`lean-axiom-guard.py`'s warning that the corpus's
`OVTopAssembly.sum_numSYT_sq_eq_factorial` reached `clean` "by moving its
obligation into a class binder, which is the §3b-cond pattern".

**That may be the wrong declaration to have cited.** There is a second, apparently
independent route, found 2026-09-05 while chasing an unrelated gap:

    QOU/Mathlib/RSKBurnsideTarget.lean:
      def RSKBurnsideHolds (n : ℕ) : Prop :=
        ∑ p : Nat.Partition n, (dimSYT p) ^ 2 = n.factorial

    QOU/Mathlib/SchenstedRSKBurnside.lean:56:
      theorem rskBurnsideHolds (n : ℕ) : RSKBurnsideHolds n

**universally quantified**, four lines long, proved from `Schensted.rskEquiv`
over a ~40-file in-repo Schensted development (`QOU/Mathlib/Schensted*.lean`).

The two statements look definitionally identical:

- `seminormalDim lam = QOU.Mathlib.dimSYT lam` — `Hoefsmit.lean:88`, by definition.
- `heckeDim n = n.factorial` — `Common.lean:53`, by definition.

So `RSKDimIdentity n` and `RSKBurnsideHolds n` should be the same proposition up
to unfolding, and `wedderburnEmbedOf` would become **unconditional** — dropping
the one hypothesis PR #6848 was careful to isolate.

## What is NOT established

**`#print axioms QOU.Mathlib.rskBurnsideHolds` HAS NOT BEEN RUN.** Its olean does
not exist — `QOU.Mathlib.SchenstedRSKBurnside` is one of the 1712 never-built
modules measured in `qou-pdgc`, and building its cone would race the whole-corpus
survey currently writing that olean tree.

The only evidence so far is static and weak:

- no `axiom` declaration in any `QOU/Mathlib/Schensted*.lean`;
- the three files matching `sorry` match it only in prose — each says
  "sorry-free" in its own module docstring.

A grep is not `#print axioms`, and this arc has repeatedly found docstrings
overstating exactly this kind of claim (`wedderburnEmbed_posSemidef` advertised
but absent; `wenzlBridge` advertised at the wrong strength; three of my own PR
claims corrected). `RSKBurnsideTarget.lean`'s own docstring says the identity is
"**no longer open**" and "Nothing is waiting on upstream" — which is precisely
the sort of sentence that needs checking rather than quoting.

## Next step, in order

1. Once the `qou-pdgc` survey has built `QOU.Mathlib.SchenstedRSKBurnside`, run
   `#print axioms QOU.Mathlib.rskBurnsideHolds`. Anything beyond
   `[propext, Classical.choice, Quot.sound]` — in particular `sorryAx` — settles
   it negatively and this bean closes as "checked, still conditional".
2. If clean, prove `RSKDimIdentity n` from it (should be `rfl`-adjacent) and make
   `wedderburnEmbedOf` unconditional, retiring the hypothesis from the signature.
3. Either way, correct `WedderburnConstruction.lean`'s docstring, which currently
   points only at the class-binder declaration and does not mention this one.

Do **not** perform step 2 on the strength of the grep.
