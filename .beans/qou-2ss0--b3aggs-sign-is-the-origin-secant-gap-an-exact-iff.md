---
# qou-2ss0
title: 'b3Agg''s sign IS the origin-secant gap: an exact iff replacing two one-way convexity implications, and the fit trap that follows'
status: in-progress
type: task
priority: normal
created_at: 2026-09-13T07:58:29Z
updated_at: 2026-09-13T08:51:09Z
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


## 🛑 CORRECTION 2026-09-13 — I asked the owner for a paper the corpus already HOLDS and already CITES

I told the owner, twice, that Groeneveld (1962) — the alternating-sign theorem
the whole `b₃ < 0` negative rests on — is "**NOT** in `library/`", and asked for
a PDF. **Both halves were wrong**, and the second is worse than the first.

**Held.** Measured on `library/*/sections/`: `Groeneveld` **2 documents**,
`Ursell` **6**, `Mayer` **39**, `Ruelle` **12**, `Penrose` **19**, `lattice gas`
**4**, `fugacity` **10**. `library/s10955-022-02992-6/` is **Jansen & Kolesnikov
(2022), *Cluster Expansions: Necessary and Sufficient Convergence Conditions*,
J. Stat. Phys.**, whose §3.1 states the *"well-known alternating sign property of
the Ursell function"* with the explicit sign
`(−1)^(r + Σ(|Vᵢ|−1)) = (−1)^k` and proves it as Corollary 3.3.

**And cited.** `QOU/MassTheory/UrsellPartitionFunctionB3.lean` line 21 names
`(Jansen–Kolesnikov, library/s10955-022-02992-6/, p. 5)` and line 73 carries
`-- Ref: [jansen2022cluster] https://doi.org/10.1007/s10955-022-02992-6`. The key
is in `content/schema/references.ts`; `BondArcTheorems.lean` cites it too. **The
b₃ Lean is properly sourced and always was.**

### How I got it wrong — it is the documented trap, verbatim

I ran **tier 1 only**. `INDEX.md` returns **0** for `Groeneveld`, `Ursell`,
`Ruelle`, `lattice gas` and `fugacity` while `sections/` returns 2, 6, 12, 4 and
10. AGENTS.md §corpus-grep path 5 says exactly this: *"a clean tier-1 scan is
evidence about the index, not about the library"*, and records that the index
silently went **33 real documents** stale once before. I quoted that rule to the
owner earlier in the same session and then did not apply it.

**Cheapest fix for the next agent: never conclude "not held" from `INDEX.md`.**
Run `grep -rli <topic> library/*/sections/` before saying it. It costs one
command.

## SIXTH name-collision, for `qou-r44k`

`alternating sign` → **alternating sign MATRICES**. Of the four documents
matching it, `1-s20-s009731651830061x-main` (Fischer, *Constant term formulas
for refined enumerations of Gog and Magog trapezoids*) supplies **21** of the
section hits and has nothing to do with Ursell functions; `arxiv-math-9909027v1`
is Jones, *Planar Algebras I*. So a grep for the phrase that names this bean's
own load-bearing theorem lands mostly on combinatorics of ASMs. Same class as
the five already recorded, found inside my own search path.


## 2026-09-13 — the SCALING route, from the owner's upload, and it is the shape a derivation would have

The owner uploaded `arXiv:2311.05446v3` (Aishwarya–Rotem, *New Brunn–Minkowski
and functional inequalities via convexity of entropy*). Its Brunn–Minkowski
results hold for log-concave measures with a **p-homogeneous potential** — and
that hypothesis SHAPE is what matters here, not the inequalities.

`sign_carries_no_information_beyond_the_secant` says the convexity route is a
derivation only if the secant condition comes from something that does not
already know `b₃`. **Scaling is such a something.** A homogeneity degree is
fixed by how the assembly law behaves under rescaling the bond weight; it is not
a curvature picked to fix a sign.

Four new theorems (lean-direct exit 0, all four `#print axioms` clean):

    b3Agg_of_scales                    Φ(3g) = c·Φ(g)  ⇒  b₃ = (c − 3)·Φ(g)
    b3Agg_pos_iff_scale_gt_three       with Φ(g) > 0:   b₃ > 0  ↔  c > 3
    b3Agg_eq_zero_iff_scale_eq_three                     b₃ = 0  ↔  c = 3
    b3Agg_pos_iff_exponent_gt_one      Φ(3g) = 3^p·Φ(g): b₃ > 0  ↔  p > 1

The first three need **no convexity, no differentiability and no hypothesis on
`Φ` anywhere else** — strictly more general than the power law, since `c` is any
scaling factor. Verified in exact `Decimal` at `p = 0.5, 1, 1.5, 2, 3` against
the direct cumulant before the Lean was written; all five agree exactly, signs
`−, 0, +, +, +`.

### Why this is the useful reformulation

**`p = 1` is additive superposition and gives exactly zero** — the affine
boundary `b3Agg_linear_eq_zero` is the linear instance of. **`p < 1`, where a
concave law such as a logarithm sits, gives a negative cumulant.** So the open
question moves from

  *"why should the aggregator curve upward?"*   (a curvature — the fit trap)

to

  *"is the assembly law SUPERLINEAR in the bond count, and why?"*   (a scaling)

That second question is about how the law responds to rescaling, which the
framework can in principle settle **without reference to the measured sign**.
It is the first formulation of this open item that is not circular by
construction.

**NOT claimed:** that the framework's assembly IS superlinear, that `p > 1`, or
any value of `p`. Scope (a). No aggregator is proposed and the magnitude is
untouched. Asserting `p > 1` because it yields `b₃ > 0` would be the same
selection-against-target this file exists to name — the requirement is a derived
scaling degree, not a chosen one.


## 2026-09-13 — `qou-q8vl`'s SECOND escape route is narrower than it was stated

`qou-q8vl` records the open escape for a third bond family as: *"it must break
the AVERAGING of the pn letter, or break AFFINENESS of the interface law."*
**The second half is too weak.** Measured, then proved.

`QOU/MassTheory/InterfaceMonotoneBlocksSignMixed.lean` (12 decls, lean-direct
exit 0, `#print axioms` clean — and the three order-core theorems depend on
**no axioms at all**).

### What actually blocks the pattern

Affineness is not the invariant. **Monotonicity is.** If `f` is monotone in
*either* direction and `c` lies between `a` and `b`, then `f c` cannot strictly
exceed both `f a` and `f b` — no linearity, no continuity, no algebra. The
hypothesis is an order property and each proof is one `lt_of_lt_of_le` against
`lt_irrefl`.

Checked in exact `Fraction` before the Lean, at `a, c, b = 0, 1, 2`:

    affine increasing   3x+5      c strict max?  NO
    affine decreasing  -3x+5      c strict max?  NO
    monotone NON-affine  x³       c strict max?  NO   <-- the point
    antitone NON-affine -x³       c strict max?  NO
    NON-monotone       1-(x-1)²   c strict max?  YES  <-- only escape

`PnBetweennessBlocksSignMixed.pn_not_strict_max` is the `f = (z + ·)` instance
of `pn_not_strict_max_of_monotone`.

### Consequence for the open search — this is the usable part

**A third bond family that merely abandons affineness gains nothing.** A cubic
interface law `d ↦ d³` is as blocked as `d ↦ z + d`. The escape requires a
**non-monotone** law, a strictly stronger demand over a much smaller space.

So the cheap filter, before any number is computed: *is the candidate law
monotone?* If yes, the sign-mixed pattern is already excluded and the
construction is dead. That turns a vague "break affineness" into a
one-line test.

`hump_realises_strict_max` / `nonmonotone_escape_exists` show the narrowing is
**sharp** rather than a disguised impossibility — the downward parabola
`1 − (d−1)²` does put the middle strictly above both endpoints. So monotonicity
is exactly the invariant, not a sufficient condition standing in for something
weaker.

### Scope

Scope (b); the invariant is order-preservation, an identity rather than a
measurement. **NOT claimed:** that a non-monotone interface law exists in the
framework, is derivable, or is physical. Physically it would mean a larger letter
offset *decreasing* the bond factor over some range and increasing it over
another; whether the framework admits that is open and untouched here.
`qou-q8vl`'s *first* escape — breaking the pn averaging — is also untouched.
