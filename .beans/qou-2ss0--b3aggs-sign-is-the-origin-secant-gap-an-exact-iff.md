---
# qou-2ss0
title: 'b3Agg''s sign IS the origin-secant gap: an exact iff replacing two one-way convexity implications, and the fit trap that follows'
status: in-progress
type: task
priority: normal
created_at: 2026-09-13T07:58:29Z
updated_at: 2026-09-13T08:04:25Z
---

## Result (2026-09-13) — the convexity route analysed; convexity is the WRONG invariant

`qou-q8vl` lists "the convexity route, which is unanalysed here" as its one open
sub-item. Analysed. Lean `QOU/MassTheory/B3AggSecantCharacterisation.lean`
(10 decls, lean-direct `-DautoImplicit=false -s 65536` **exit 0**, no warnings;
`#print axioms` on all 8 theorems: **no sorryAx**, only propext / Classical.choice
/ Quot.sound).

### The identity

With `s x = Φ x / x` the origin-secant slope, for `g != 0`

    b3Agg Φ g  =  Φ(3g) − 3 Φ(g)  =  3g · ( s(3g) − s(g) )

exactly (`b3Agg_eq_secant_gap`, by `field_simp`). Hence for `g > 0`

    0 ≤ b3Agg Φ g   ↔   s(g) ≤ s(3g)        (`b3Agg_nonneg_iff_secant_le`)
    0 < b3Agg Φ g   ↔   s(g) < s(3g)        (`b3Agg_pos_iff_secant_lt`)
    b3Agg Φ g = 0   ↔   s(g) = s(3g)        (`b3Agg_eq_zero_iff_secant_eq`)

**These are iffs.** `AggregatorConvexityDichotomy` has three one-way
implications; this replaces them with the condition they were approximating.

### Finding 1 — convexity is sufficient and STRICTLY UNNECESSARY

`convexOn_sufficient_not_necessary` exhibits `Φ x = x³ − x²`: passes through the
origin, **not** `ConvexOn ℝ (Ici 0)` (it is concave near the origin, `Φ'' = 6x−2
< 0` for `x < 1/3`; the witness is that the midpoint of `[0,1/3]` sits strictly
above the chord, `Φ(1/6) = −5/216` against `−8/216`), and yet
`b3Agg Φ 1 = 18 > 0`.

So **a search for `b₃ > 0` restricted to convex aggregators is searching a
strict subset.** Global convexity is a condition at every pair of points; what
`b₃ > 0` requires is that ONE secant slope not drop across ONE fixed scale
ratio. That is a real narrowing of the open search, and it is the opposite of
what the one-line "convexity route" framing suggests.

### Finding 2 — and the route carries a fit trap, now stated as a theorem

Because the characterisation is an **iff**, the aggregator's secant behaviour
across `(g, 3g)` and the sign of `b₃` are the *same proposition*, not two facts
that could corroborate each other (`sign_carries_no_information_beyond_the_secant`).
Choosing `Φ` so that `b₃ > 0` is therefore the assumption rewritten, not evidence
for it. Under §"NO FITTING, EXCEPT CAL-1/2/3" that is **selection against the
target** in the directive's own terms: an *object* is chosen, no continuous
parameter is tuned, and the measured sign is reproduced by construction.

**The convexity route is a derivation route only if the secant condition is
derived from something that does not already know `b₃`.** Otherwise it is the
answer restated. That is the thing to check before anyone spends a tranche on it.

### Scope and what is NOT claimed

Scope (a). No aggregator is proposed, no magnitude is touched, and the
production assembly is undisturbed — `B = −α log(...)` is concave, so `b₃ ≤ 0`
there by the existing `b3Agg_nonpos_of_concaveOn`, unchanged. This narrows and
classifies the search; it derives no replacement. `qou-q8vl`'s OTHER open item —
a third bond family breaking pn-averaging or interface affineness — is untouched.

No `q`, no Markov parameter, no anchor, no CODATA value, no numeral outside the
witness polynomial. Nothing here can go stale under the convention-D migration.
