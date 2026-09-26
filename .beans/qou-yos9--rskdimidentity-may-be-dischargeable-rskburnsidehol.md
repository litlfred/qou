---
# qou-yos9
title: 'RSKDimIdentity may be dischargeable: rskBurnsideHolds proves it for all n, unverified by print axioms'
status: todo
type: task
priority: normal
created_at: 2026-09-05T18:46:54Z
updated_at: 2026-09-26T11:03:27Z
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

## Resolved 2026-09-05 — checked, and it holds

Step 1 (the check this bean was blocked on). Built the cone —
`scripts/lean-direct-cone.sh QOU.Mathlib.SchenstedRSKBurnside -k -j3`, 48
modules, **46 ok / 2 up-to-date / 0 errors**, 143 s — then ran the measurement:

    'QOU.Mathlib.rskBurnsideHolds'     [propext, Classical.choice, Quot.sound]
    'QOU.Mathlib.card_pairs_eq_sum'    [propext, Classical.choice, Quot.sound]
    'QOU.Mathlib.Schensted.rskEquiv'   [propext, Classical.choice, Quot.sound]

No `sorryAx`, no class binder. The grep was right — but it was right by luck
until this was run, and the instruction not to act on it stands as the correct
call: two of the last five docstrings this arc checked were overstating.

Step 2. `RSKDimIdentity n` is *definitionally* `RSKBurnsideHolds n`
(`seminormalDim = dimSYT`, `heckeDim n = n.factorial`, both definitions), so

    theorem rskDimIdentity (n : ℕ) : RSKDimIdentity n :=
      QOU.Mathlib.rskBurnsideHolds n

typechecks as written. `QOU/HeckeAlgebra/WedderburnUnconditional.lean` carries it
plus `wedderburnEmbedTotal`, `wedderburnEmbedTotal_eq` (proof irrelevance against
the conditional form) and `wedderburnEmbedTotal_injective` — the last discharging
positivity from `seminormalDim_pos'` too, so **nothing is left for a caller to
supply**. All four: `[propext, Classical.choice, Quot.sound]`.

Step 3. `WedderburnConstruction.lean`'s docstring corrected: it said the identity
"is available only conditionally" and pointed solely at the class-binder
declaration. It now records which declaration was wrongly cited, the measurement,
and that the `numSYT` ↔ `dimSYT` bridge it said would be needed
(`SYTEncodingBridge.lean`) is not on this route and was never required.

## Two judgement calls worth recording

**The name was not reclaimed.** `wedderburnEmbed` is free again, and taking it
would have tripped `qbeta_wedderburn_bridge_probe.py`'s guard that no reference
to the retired opaque survives — a gate written one hour earlier in `qou-kp2z`.
The map is `wedderburnEmbedTotal` instead. Keeping a gate sharp is worth more
than a name.

**The guard was still widened, and deliberately.** A plain substring test flags
any identifier starting with those letters, so it would have fired on the
legitimate `wedderburnEmbedOf` / `wedderburnEmbedTotal`. It now matches the
**bare** identifier with a word boundary. Recorded here because widening one's
own gate to fit one's own new code is exactly the move that erodes gates — the
justification is that the gate means "the retired opaque has no consumers", not
"no identifier starts with these letters", and the bare-name form is the one
that actually says that.

## What this does not touch

The shape objection. `wedderburnEmbedTotal` has the same type as before — blocks
in, one matrix out — so the `(2,1)` clause is exactly as open as `qou-v7ms`
leaves it. Discharging a hypothesis changed what the map rests on, not what it
does.

This closes the arc that opened with `opaque wedderburnEmbed`: axiom (`qou-qb7p`)
→ construction with one named hypothesis (`qou-usol`) → opaque deleted
(`qou-kp2z`) → hypothesis discharged (here).
