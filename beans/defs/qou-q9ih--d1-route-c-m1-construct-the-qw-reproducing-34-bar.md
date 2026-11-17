---
# qou-q9ih
title: 'D1: Route C M1 — construct the (Q,W) reproducing {3,4} + bar split (7,1); fitted quiver = candidate only (parent qou-rtec)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-15T02:49:30Z
updated_at: 2026-11-15T17:10:00Z
parent: qou-v2om
---


## 2026-08-15 first rung — implementation class pruned (Lean-proved)

`QOU/QBeta/QuiverMirrorAutomorphismExcluded.lean` (sorry-free, axioms
[propext, Quot.sound]): any COUNT-INVARIANT mirror implementation — a
quiver automorphism, the op-duality Q ↦ Q^op, or any DT-preserving
equivalence — forces every readable pair amphichiral, so the (4,3)
datum is unreachable (`count_invariant_excludes_five_two`), and
conversely reading (4,3) forces Ω(σd) ≠ Ω(d)
(`five_two_forces_count_breaking`).

CONSEQUENCE for the search: the M1 object is (quiver, potential, TWO
stability rays) with the mirror acting on the RAY, never (quiver +
automorphism). Consistent with M2's distinct-Borel-rays finding
(RouteCM3CategoryIdentification). Extends Driver14's no-scalar theorem
one level up (no count-preserving symmetry implementation either).

REMAINING (the big rung, still open): actually construct a (Q,W) + ray
pair whose DT counts are (4,3) with bar split (7,1), FROM Hecke/Bring
data. A fitted quiver stays a labeled CANDIDATE only (anti-laundering).


## Attack-options ledger — construction rung (2026-08-15, dispatched-agent research)

Target object (post-pruning): **(Q, W, ray+, ray-)** — quiver with potential
plus TWO stability rays, ray-wise DT counts (4,3), bar split (7,1).
Constraints Lean-proved: no count-preserving mirror implementation
(QuiverMirrorAutomorphismExcluded); abelian spectrum at distinct Borel rays
(AomegaM2BPSCohomology / RouteCM3); datum is set-valued (Driver14 no-scalar).
Standing negative respected: driver-14 NOT constructible from scalar drivers.
Any quiver whose only credential is matching the datum = labeled CANDIDATE.

### D1-a — KS/Reineke small-quiver two-ray DT scan (CANDIDATE generator)
Enumerate <=3-4-vertex quivers, DT counts on ray pairs, filter (4,3)+(7,1).
Session-scale. Either outcome is progress: no hit -> bounded negative
(">= N vertices required"); many hits -> datum underdetermines (Q,W),
sharpening why only derivation counts. Expect many hits (2-integer target is
weak — the #4534 two-knot-linear-fit guard); say so in the docstring.
No dependencies; parallel-safe.

### D1-b — Jacobi algebra from certified character-variety / spectral data
Nodes per connection (3 / 4 incl. abelian, certified in
dt_crossknot_connection_count_certified_probe.py), arrows/potential from the
NZ-gluing datum (DGG closed-sector). Multi-session; the NZ->(Q,W) dictionary
must be assembled from KS/DGG lit. CANDIDATE-plus tier: certified GEOMETRIC
imports (allowed — the audit says the missing input IS geometric), not
Hecke-derived. Do NOT resurrect the refuted KRSS open-sector route (det(K)=5).

### D1-c — Hecke/Bring-side extraction (the derivation-tier target = M3)
Vertices from Wedderburn blocks of H3(q) (both knots are 3-braids), bar-graded
per DTChiralityBarInvolutionLink; rays from the bar involution on stability.
First step is a cheap disconfirmable shape test: does ANY natural pairing on
the 5_2 braid blocks give a 2-ray abelian spectrum summing to 7?
Research-programme; heavy prior against (driver-14 negative), but a quiver is
not a scalar so not formally excluded. Only route whose success = derivation.
Open-outcome — sibling overlap encouraged with distinct angle.

### D1-d — Exponential-network import (literature frontier)
BPS counts of the A-polynomial curve at two conjugate phases (BLR style).
Multi-session+; no network infra in corpus. Even reproducing 4_1's count 3
locally would upgrade the DT import tier. Import-tier, clearly labeled.
Lowest priority per unit cost.

### D1-e — Formalize-first: Lean constraints on the (Q,W,ray,ray) shape
Before any scan: prove what abelian + two rays + the datum force —
(i) >=4 / >=3 stable classes per ray (vertex lower bounds); (ii) rays not
exchangeable by arrow-preserving relabeling (import of the landed exclusion);
(iii) the M2 dimBPSplus = sAtOne+1 anchor as a ray-count tie. Session-scale,
sorry-free-achievable. Each theorem must delete a concrete slice of the D1-a
enumeration. DO D1-e BEFORE OR WITH D1-a.

### D1-f — Wait-on-lit watch (named unblockers)
(1) published closed-sector BPS quiver for T[5_2] -> unblocks D1-b;
(2) exponential-network counts for 5_2 -> validates (4,3) independent of GGM;
(3) a 6_1 (or 3_1) DT spectrum -> the third-knot falsification target;
(4) any categorification of the 3d-index from Hecke/Soergel data -> reopens
D1-c. Passive; not a substitute for D1-a/e.

### Sequencing
1. D1-e (formalize-first, prunes downstream) 2. D1-a (candidate generator)
3. D1-b (main multi-session thrust) 4. D1-c (parallel sibling, distinct angle)
5. D1-d/D1-f passive. Nothing derives A_omega; datum stays certified-imported;
q0-derivation untouched (forever-gated).

## 2026-08-19 Arc review — two sibling tools now feed D1, and M3 has an owner

**Nobody has touched the M1 construction rung.** D1-a…D1-f stand as written.
Two landings feed it, both verified sorry-free and read directly:

1. **`QOU/QBeta/LadderPhaseMirrorCovariance.lean`** (`fa03077a7`, generic
   `CommRing`/field): `phaseTwice_bar_odd_iff_z_bar_fixed`, `zC_bar_fixed`,
   `phaseTwiceD_bar_anomaly`, and — the D1-relevant one — under convention D
   **bar EXCHANGES the two Markov loop values**, which is what a mirror must do
   since mirroring exchanges positive and negative crossings.
   **Why this matters here:** `QuiverMirrorAutomorphismExcluded` proved the
   mirror must act on the STABILITY RAY, never as a count-preserving symmetry,
   but supplied no candidate for what that action IS. The D-frame loop-value
   exchange is the first concrete candidate. Feeds D1-a (the two-ray scan) and
   D1-e (further Lean constraints) directly.

2. **`QOU/QBeta/AdjointIndexSetM3.lean`** —
   `knot_independent_core_forces_unit_remainder (core : Int) (extra : KKnot → Int)`
   with hypotheses `core + extra 4₁ = 3`, `core + extra 5₂ = 4`. Stated over the
   SAME `KKnot`/`fourOne`/`fiveTwo` vocabulary as my
   `Driver14CharacterVarietyDTMenu`, so it composes without translation. Usable
   in D1-a as a filter on candidate (Q,W) spectra: any knot-independent core
   forces a remainder of exactly 1.

**Coordination (do this before D1-b or D1-c).** Bean `qou-m3ad` (sibling,
in-progress, high, `parent: qou-rtec` — inside my own parent programme)
reframed the M3 target from "build a CoHA" to "derive the index set Ω", on M2's
abelian finding, and pins the (3,3)-vs-(3,4) remainder with two adversarial
checks recorded. Per the survey it does NOT conflict with
`no_scalar_matches_chirality_split_datum`: its Part 2 addresses that explicitly
(R1 = dtMax, H_Ad core = dtMin, and the PAIR reconstructs {3,4}) — i.e. it
routes around my no-scalar theorem rather than contradicting it. **Unverified
by me**: I read the theorem statement, not that Part-2 argument. Verify before
building on it.

Sequencing unchanged (D1-e → D1-a → D1-b, D1-c as a sibling's parallel angle),
but D1-a is now cheaper: two proved filters instead of an unconstrained scan.

── Assessment 2026-08-22 (branch n24484): no bounded high-value move; O4 stands ──
Read the arc-status (qou-arc1, COMPLETED): the A_ω/Route-C arc RESOLVED to O4
(pivot away) on 2026-08-15 — O2 refuted, physics connection ESTABLISHED ABSENT,
recommendation = bank standing results and stop investing; M1/M3 remain 'pure-math,
no physics payoff'. Assessed each bounded D1 entry against that:
• D1-a (small-quiver two-ray DT scan): its predicted outcome — 'datum underdetermines
  (Q,W)' — is ALREADY anticipated by the corpus ('2-integer target is weak, #4534
  two-knot-linear-fit guard'). Running it reproduces a known negative; low marginal value.
• D1-e (formalize-first vertex bound): given the imported M2 abelian premise (stable
  classes = vertex simples, #simples = V) the vertex lower bound V≥4 from ray-count 4 is
  near-trivial pigeonhole; thin, and the premise carries all the weight.
• D1-c (Hecke/Bring derivation-tier, the ONLY route whose success = derivation): the cheap
  shape test 'does a natural pairing on 5₂'s H₃(q) blocks give a 2-ray abelian spectrum
  summing to 7' is the right entry, BUT the exact (7,1) bar-split target + the
  blocks→spectrum 'natural pairing' dictionary are under-specified in the corpus; assembling
  them is the multi-session D1-b/c thrust, not a session.
Certified inputs confirmed: DT connection counts 4₁→3 (2 irred + 1 abelian), 5₂→4 (3+1),
so {3,4} sum 7 (dt_crossknot_connection_count_certified_probe). Nothing here is a fit.
VERDICT: no bounded, rigorous, high-value in-session move exists that isn't corpus-
anticipated (D1-a), near-trivial (D1-e), or a multi-session assembly (D1-c). O4 stands:
this periphery has no physics payoff. Not pursuing further absent an explicit pure-math
directive. (Coordination: my gap-3 commit touched LadderPhaseMirrorCovariance.lean, which
feeds D1-a/e — phaseTwice_eq_counit_sub_trace added there, no overlap with M1 construction.)

── 2026-08-31: D1-f item (3) is DONE — the third-knot test was never blocked ──

Owner directive to work this programme (the explicit pure-math directive the
2026-08-22 assessment named as its own gate — that gate is now satisfied).

`computations/qbeta/dt_third_knot_trefoil_count_probe.py`, **7/7**.

**The blocker was true of 6₁ only.** The certified probe's docstring and witness
both record the third-knot test as needing "the ptolemy DB or magma". But
D1-f names **"a 6_1 (or 3_1) DT spectrum"** as the target, and
`3_1__sl2_c0` / `3_1__sl2_c1` are bundled in the very directory the certified
probe already reads. No DB, no Magma, no network.

    knot   c1 orbits / degrees / field          irred + abelian = TOTAL
    3_1      1 / [1] / Q                          1      1        2     NEW
    4_1      1 / [2] / x^2 - x + 1                2      1        3     control
    5_2      1 / [3] / x^3 + 2*x^2 + 3*x + 1      3      1        4     control

Both controls reproduce the committed certified witness exactly, so the method
is the corpus's own, not a new one.

**It does not separate the three readings that were on the list.** All three
predict 2 for the trefoil: `crossing − 1` (3−1), `deg(trace field) + 1` (1+1,
the field is ℚ), and the corpus's R1 `full A-polynomial L-degree` (2). Saying
"the third-knot test passed" without that would be the over-read the
`#4534 two-knot-linear-fit guard` warns of.

**🛑 CORRECTION to my own first write-up: it DOES discriminate, against a fourth
reading I had not listed — and that is the load-bearing half.** The adversarial
alternative to the whole R1 identification is that the count tracks the
COMPUTATION's presentation rather than the knot, i.e. the **triangulation**:

    knot   tets   crossings   MEASURED   crossing-1   tets+1
    3_1      2        3           2          2         3   <-- FAILS by 1
    4_1      2        4           3          3         3       fits
    5_2      3        5           4          4         4       fits

`tets + 1` is **not a strawman**: SnapPy triangulates 4₁ with 2 tetrahedra and
5₂ with 3, so on the corpus's own two knots it is **indistinguishable** from
`crossing − 1`. The trefoil separates them because 3₁ has the **same**
tetrahedron count as 4₁ and one fewer crossing. This matters more than the three
readings above, because the triangulation is **not canonical** — had the count
tracked it, R1 would have been an artifact of how the manifold was handed to
Magma rather than a fact about the knot.

**What it does buy.** The datum moves from TWO points to THREE: totals (2,3,4)
at crossings (3,4,5), irreducibles (1,2,3) equal to the trace-field degrees.
`AdjointIndexSetM3.knot_independent_core_forces_unit_remainder` fits two points
by construction; a third collinear point is **one genuine spare constraint, and
it passed**. Weak evidence — and more than none. It also changes the M1
construction target: the DT counts to reproduce are now a 3-element family with
a linear pattern, not the 2-element pair (4,3) the bean is written around.

**What would discriminate, both blocked and neither guessed at.**
`crossing − 2` and `trace-field degree` agree on all three and must diverge
somewhere. Separating them needs (a) trace-field degrees for further knots —
`M.trace_field_gens()` raises `SageNotAvailable` (SnapPy outside Sage here), or
(b) ptolemy data for a fourth **knot** — not bundled; 6₁ = m032 has no fixture.

**Inspected and EXCLUDED so it is not taken for a fourth point.**
`DT_mcbbiceaibjklmdfgh__sl2_c0..c7` is also bundled and tempting, but it is
**L13a5175** — a 3-component LINK, 3 cusps. Its abelian count is not 1 and its
26 irreducible points (c4 degree 15, c5 degree 11) are not comparable. The other
bundled fixtures (m019, m135, s000, t00000, v0000) are census manifolds that
`identify()` returns only themselves for — not knot complements.

**Scope caveat, stated because it is easy to miss:** 3₁ is a TORUS knot, volume
0, not hyperbolic. The ptolemy variety and A-polynomial are defined regardless
so the count and the R1 reading are meaningful, but the geometric-component
reasoning motivating the hyperbolic cases does not apply, and its single orbit
is rational rather than a genuine trace field. Scope-(a), nothing wired, no fit.

**Two of my own errors this session, recorded because both were near-misses.**
(1) I read a truncated `tail -30` of a 35-entry listing, concluded `3_1` was
absent, and "corrected" a correct earlier claim into a wrong one — the sorted
list puts `3_1__*` first, exactly where the truncation cut. (2) A bare
`except: pass` around `find_field` turned `SageNotAvailable` into a printed
`None`, i.e. a tool refusal reported as a measured absence. Same shape as the
detector-blindness class this corpus catalogues.

── 2026-09-03: D1-a RUN. The datum underdetermines, and the trefoil cuts NOTHING ──

`computations/qbeta/dt_d1a_small_quiver_two_ray_scan_probe.py`, **6/6**.

### Result 0 (formalize-first, and it is the D1-e deliverable — a DELETION)

D1-a's filter reads "(4,3) **+ bar split (7,1)**", i.e. four constraints. **It is
two.** `AomegaM2BPSCohomology` defines

    barEven := dimBPSplus + dimBPSminus     (4 + 3 = 7)
    barOdd  := dimBPSplus - dimBPSminus     (4 - 3 = 1)

so `(7,1)` is the sum and difference of `(4,3)` — **zero independent
information**, and `bar_split_seven_one` is `by decide` on those definitions.
Filtering on `(7,1)` after `(4,3)` is a **no-op**. D1-e asked that each theorem
"delete a concrete slice of the D1-a enumeration"; this deletes half the
apparent target before the scan runs. The 2026-08-22 assessment's "2-integer
target is weak" was right, and the target is weaker than the bean's own phrasing.

### Result 1 — the scan

74 acyclic quivers, V ∈ {2,3,4}, arrow multiplicities 0..1; real roots (Tits
form `q(d)=1`) in a box; slope-graded King stability with exact `Fraction`
slopes; a RAY is a slope value, so one `θ` offers several rays.

    filter A  admits a ray pair with counts (4,3)      64 of 74
    filter B  admits a ray triple with (2,3,4)         64 of 74
    cut by the trefoil's third point                    0  (exactly zero)

**64 of 74 hit. The datum underdetermines `(Q,W)`** — the bean's own prediction,
now measured rather than expected.

### 🛑 Result 2 — this REFUTES my own claim, and that is the useful part

On merging PR #6391 I wrote that D1-a was "now better posed — a 3-element linear
family rather than two integers, which is a materially stronger filter". **It is
not stronger. It is exactly as strong: the cut is 0.** Every quiver reaching
`{3,4}` also reaches `{2,3,4}`, because count 2 is available at some ray of
nearly any quiver.

The reason is structural and the probe asserts it: **all 10 misses are quivers
too small to reach 4 stables at any ray.** So the filter is a **SIZE** condition
— "has ≥ 4 stable objects at some ray" — not a structural one. A size condition
cannot discriminate `(Q,W)`, and adding more integers of the same kind never
will. So the third knot's value is where PR #6391 put it (killing the
triangulation reading of R1), **not** in strengthening this scan.

### 🛑 An artifact of mine that nearly read as a strong negative

The first version required `θ·d = 0` for every counted root — King's numerical
condition at slope **zero**. That forces every counted object onto ONE slope, so
a per-ray count can essentially never exceed 1, and the scan returned **0 hits
for both filters**. "No small quiver reproduces the datum" would have been a
publishable bounded negative; it was an instrument error. Caught only because
the bean **predicts many hits**, and a result contradicting the corpus's own
expectation is a reason to audit the instrument before believing it. Recorded in
the probe docstring.

### Scope

Scope-(a). `W = 0` throughout (a potential can only cut further, so a miss here
does not exclude a quiver once `W` is added); real roots only (imaginary roots
carry moduli); stability is a numerical proxy for King in both directions, so
the counts are **not certified DT invariants**. Both filters use the *same*
counting function, which is what makes the **cut** meaningful even where the
absolute counts are not. No `(Q,W)` proposed, nothing wired, no fit — hits are
labeled CANDIDATES only, per this bean's anti-laundering instruction.

### Where this leaves D1-a

**Done, and negative in the way the assessment predicted.** The remaining D1
entries are unaffected: D1-c is still the only route whose success would be a
derivation, and it is still under-specified. Nothing here derives `A_ω`.

── 2026-09-03 (2): D1-c's stated VERTEX ASSIGNMENT is excluded ──

`computations/qbeta/dt_d1c_hecke_block_vertex_bound_probe.py`, **6/6**.

D1-c is the only D1 route whose success would be a **derivation**, and the
2026-08-22 assessment called its two inputs under-specified: the exact `(7,1)`
bar-split target, and the blocks→spectrum "natural pairing" dictionary.

**Half that blocker was already gone.** The D1-a probe's Result 0 shows `(7,1)`
is `(plus+minus, plus−minus)` — arithmetic on `(4,3)`. There is no separate
bar-split target to specify; D1-c must hit `(4,3)`, full stop.

**The other half does not need specifying either, because the vertex assignment
is excluded before any dictionary is chosen.**

### The measured bound

Over every acyclic quiver on `V` vertices, the largest number of stable objects
sharing ONE ray (slope) is exactly `V`, never more:

    V   quivers   max per-ray   exceeds V?
    2      3           2          no
    3     27           3          no
    4    729           4          no

and for `V = 3` it is **not** a box artifact — growing the enumeration box grows
the root system without lifting the cap:

    DMAX  TMAX   max #roots   max per-ray
      3     3        18            3
      4     4        24            3
      5     4        30            3

Likely mechanism, offered as the reason and **not proved here**: at a fixed
slope the θ-semistables form an abelian category whose simples are the
θ-stables, and its rank is bounded by the rank of K-theory, which is `V`.

### The consequence

`H₃(q)` has exactly **three** Wedderburn blocks — `(3)` dim 1, `(2,1)` dim 2,
`(1³)` dim 1 — so one vertex per block gives `V = 3`, ceiling 3, while the datum
needs a ray carrying **4** (5₂). **Under that reading D1-c cannot produce
`(4,3)` whatever the blocks→spectrum dictionary turns out to be.**

**🛑 But which reading?** The bean does not say, and the two differ:

    one vertex per block   V = 3   (blocks (3), (2,1), (1³))    EXCLUDED
    dimension-weighted     V = 4   (dims 1 + 2 + 1)             clears it

"Vertices from Wedderburn blocks" reads most naturally as one per block, which
is excluded — but `H₃` has total dimension 4, so the weighted reading survives.
**The exclusion is of the natural reading, not of every reading**, and the probe
reports both counts rather than picking one. Worth noting that **both** escapes
land on `V = 4`: the dimension-weighted reading, and the blocks-plus-abelian
repair below. Suggestive; not evidence.

This is the same bound D1-e anticipated ("`V ≥ 4` … near-trivial pigeonhole").
**What is new is not the bound but where it lands**: the bean lists D1-e and
D1-c as separate entries, so nobody had pointed the one at the other. D1-c's own
vertex count violates it.

### A structurally-motivated repair — PROPOSED here, TESTED below, and it FAILS

> **Superseded by the 2026-09-03 (3) entry at the end of this bean.** The
> repair clears the vertex bound and then fails D1-c's *own* bar-ray
> stipulation. Do not re-run this test; read that entry.

The corpus's own decomposition is `total = irreducible + abelian` with
abelian = 1: 4₁ = 2+1, 5₂ = 3+1, 3₁ = 1+1. So the natural vertex set is not the
three blocks alone but **the three blocks together with the abelian
connection** — `V = 4`, clearing the bound exactly. That reconciliation comes
from the corpus's arithmetic rather than from choosing 4 to fit, which is why it
is worth recording. Nothing here tests whether such a quiver reproduces `(4,3)`
at two rays, and one that did would still be a labeled CANDIDATE.

### Scope, and what is NOT closed

Only the stated **vertex assignment** is excluded — not D1-c the route. `W = 0`
throughout (a potential can only cut further). The bound is **measured**, not
proved, over the stated ranges with the numerical King proxy. A `V = 5`
extension was attempted and **timed out** (exit 124); it was not load-bearing —
`V = 2,3,4` carry the result. Nothing derives `A_ω`.

── 2026-09-03 (3): the V=4 repair CLEARS the bound and FAILS the bar-ray stipulation ──

`computations/qbeta/dt_d1c_v4_blocks_plus_abelian_bar_ray_probe.py`, **6/6**.

The previous entry proposed the repair — vertices = the three `H₃` blocks
**together with the abelian connection**, `V = 4`, from the corpus's own
`total = irreducible + abelian`. Tested.

**Not the vacuous version.** "Does some V=4 quiver hit (4,3)" is already YES
(D1-a: 64/74). The content is D1-c's own structure, stipulated in two places:
vertices are `H₃` blocks, so **bar acts on them as partition conjugation**
`(3) ↔ (1³)` fixing `(2,1)` and the abelian vertex — `σ = (0 2)`, and *not a
free choice*, since `bar χ^(3)(Δ) = χ^(1³)(Δ)` is exact and convention-free
(entry 15 of `qou-cds1`, on main) — and "**rays from the bar involution on
stability**", so the two rays are `θ` and `σ·θ`.

### The dichotomy

    bar-symmetric quivers on the 4 vertices                        128
      admit (4,3) on SIGMA-RELATED rays (theta, sigma.theta)         0
      admit (4,3) on ARBITRARY two rays                            128
      achievable per-ray counts overall                      [1,2,3,4]

**Every one of the 128 reaches the target somewhere; not one reaches it on a
bar-related ray pair.** `σ` is a symmetry of the quiver, so it carries the
stable spectrum at `θ` onto the spectrum at `σ·θ` and the counts are forced
**equal** — while the datum needs `4 ≠ 3`.

So the repair **clears the counting bound and fails the structure**. Reaching
`(4,3)` requires giving up either (a) bar-symmetry of the quiver — but then `σ`
is not an automorphism and "the bar involution on stability" has no compatible
action to be — or (b) bar-relatedness of the rays, which is D1-c's own wording.

### This is the MEASURED form of a theorem the bean already has

`QuiverMirrorAutomorphismExcluded` (sorry-free) proves any count-invariant
mirror implementation forces amphichirality, so `(4,3)` is unreachable. **What
is new is not the statement but that it is checked on the specific vertex set
the repair proposes** — the repair was designed to clear a *different* bound
(the vertex count) and does, so it was not obvious the same obstruction would
survive. It does.

### A second structural fact, measured in passing

Only **25 of 128** bar-symmetric quivers are acyclic, and **none of those 25**
carries an arrow between the two conjugate blocks. Reason, immediate once seen:
`σ`-invariance sends `0 → 2` to `2 → 0`, a 2-cycle. **Bar-symmetry forbids
arrows between conjugate Wedderburn blocks in any acyclic quiver** — a
bar-symmetric acyclic model can never couple `(3)` to `(1³)` directly.

### Scope

Scope-(a). `W = 0` (a potential can only cut further). What is closed is the
**blocks-plus-abelian repair under D1-c's own bar-ray stipulation** — not D1-c
the route, and not every `(Q,W)`. The per-ray equality is **measured** here; the
cited Lean theorem proves the general statement. Nothing derives `A_ω`.

── 2026-09-03 (4): ledger status after the D1 tranche — no LIVE route is derivation-tier ──

The three entries above (D1-a, the D1-c vertex bound, the V=4 repair) settle
enough of the 2026-08-15 attack-options ledger that it should be read with
outcomes attached. Restating it so the next agent does not re-run a finished
scan or re-enter a blocked route:

| entry | tier | status after this tranche |
|---|---|---|
| **D1-e** formalize-first | prunes | **delivered, and it was a deletion.** `(7,1)` is `plus±minus` on `(4,3)`, so the target is 2 constraints, not 4. Filtering on it is a no-op. |
| **D1-a** small-quiver scan | candidate generator | **done. Predicted outcome confirmed:** 64/74 quivers meet the target — the datum underdetermines `(Q,W)`. The trefoil's third point cuts **exactly 0**. Do not re-run for more integers of the same kind. |
| **D1-c** Hecke/Bring extraction | **the only derivation-tier route** | **blocked at its own entry test, both readings.** `V=3` (one vertex per block) is under the measured per-ray ceiling `V`; `V=4` (blocks + abelian) clears the ceiling and then fails the bar-ray stipulation, because a `σ` that is a quiver automorphism forces the two ray counts **equal** while the datum needs `4 ≠ 3`. |
| **D1-b** Jacobi from character-variety / NZ | candidate-plus (import) | **untouched. Now the highest-value live route** by default, not by result. |
| **D1-d** exponential networks | import | untouched. Still lowest priority per unit cost. |
| **D1-f** wait-on-lit | passive | untouched — and item **(4)** ("a categorification of the 3d-index from Hecke/Soergel data") is now the *named* unblocker for D1-c rather than a nice-to-have. |

**The consequence, stated plainly: after this tranche no live D1 route is
derivation-tier.** D1-b and D1-d both terminate in a labeled CANDIDATE or a
certified import; the ledger itself says D1-c was the only one whose success
would be a derivation. So M3 does not have a live path, and the arc should say
so rather than presenting D1-b's progress as progress toward a derivation.

### What would reopen D1-c — and what would NOT

D1-c is **blocked, not refuted**. The block is scope-(a) plus one mechanism:

- **Scope-(a) part.** The per-ray ceiling `V` is *measured* over `V ∈ {2,3,4}`
  with `W = 0`, real roots, and a numerical King proxy. A potential can only
  cut further, so this never excludes a `(Q,W)` once `W` is added.
- **Mechanism part.** The `V=4` failure is *not* an enumeration artifact and
  does not depend on the arrow-multiplicity cap the scan used: if `σ` is an
  automorphism of the quiver it carries the `θ`-stable spectrum bijectively
  onto the `σ·θ` spectrum, so the counts are equal for **any** multiplicity and
  any `W` that is itself `σ`-invariant. That is the landed
  `QuiverMirrorAutomorphismExcluded`, measured here on the specific vertex set.

So the following would **not** reopen it, and should not be attempted as though
they might: a larger arrow multiplicity at `V=4`; a `V=5` blocks-plus-abelian
variant; a different `θ` with the same `σ`-symmetric quiver. All three leave the
automorphism argument intact.

What **would** reopen it is exactly one thing: **the mirror acting as something
other than a quiver automorphism or a ray relation** — e.g. a `σ` realised as a
derived autoequivalence that is not induced by a vertex permutation, or a
non-`σ`-invariant `W` breaking the symmetry the counts inherit. Nothing in the
corpus supplies either, which is why D1-f (4) is the live dependency.

### Scope of this entry

This is bookkeeping over the three entries above; it measures nothing new. No
route is declared refuted, nothing is wired, and `A_ω` remains underived. The
"no live derivation-tier route" statement is a claim about **this ledger's**
entries, not about the framework.

── 2026-09-03 (5): D1-b entry test — the NZ datum's SNF is a function of N alone ──

`computations/qbeta/dt_d1b_nz_gluing_invariant_entry_probe.py`, **10/10**
(PR #6509). Formalize-first, run BEFORE the multi-session NZ → Q dictionary
assembly the ledger calls for, and it asks the prior question: **can that
datum carry the information at all?**

### The measurement

The natural first-order invariant of an integer gluing datum is the Smith
normal form of `A | B` — its class under integral row/column equivalence
`GL(ℤ) × GL(ℤ)`. Across 16 knots spanning `N = 2..13` tetrahedra:

    SNF(A|B) = (1)^N + (2) + (0)      for EVERY knot.

| N | knots | distinct SNFs |
|---|---|---|
| 2 | 3₁, 4₁ | 1 |
| 3 | 5₁, 5₂, 8₁₉ | 1 |
| 4 | 6₁, 7₁, 7₂ | 1 |
| 5 | 6₂, 7₃, 8₂₀, 9₄₂, 10₁₃₉ | 1 |
| 6 | 6₃, 7₄ | 1 |
| 13 | 8₁₈ | 1 |

A function of the tetrahedron count alone. The invariant carries **no
knot-theoretic information**.

### The consequence for D1-b

D1-b's node count must separate 4₁ (3 connections) from 5₂ (4). The SNF
separates nothing beyond `N`, so **no `GL(ℤ)×GL(ℤ)`-invariant function of the
NZ gluing matrix can supply it.** The dictionary must read the matrix in a
**fixed polarization** — its actual entries — not any basis-independent
invariant of it.

### It does NOT rest on the non-hyperbolic 3₁

The tempting instance is the `N = 2` collision: 3₁ and 4₁ share an SNF but
have certified `C = 2` and `3`. **3₁ is not hyperbolic** (`contains flat
tetrahedra`), so a geometric dictionary may legitimately be undefined there —
that instance *corroborates* and is reported with the caveat attached. What
*establishes* the claim is the `N = 5` group: five **pairwise non-isometric
hyperbolic** knots, one SNF, distinctness by `is_isometric_to` rather than by
comparing volumes.

### Neither input was re-derived

Both already existed and the corpus-grep found them first:

- node counts ← `dt_crossknot_connection_count_certified_probe.py`;
- the NZ datum ← **cross-checked against** `one_loop_torsion.py::nz_pair`,
  the corpus's own extractor, rather than replacing it. SnapPy's rectangular
  form and `nz_pair` agree **exactly** as `(A,B) = (a,−b)` on every row of
  every knot up to `N = 13`, and the SNF is invariant under that convention
  flip (both are controls C5/C6).

### Two re-scopings of D1-b the grep surfaced, recorded so they are not redone

- **`W` is NOT needed.** The M2 plethystic-log result
  (`aomega_m2_bps_cohomology.py` / `AomegaM2BPSCohomology`, lean-direct exit
  0) gives `dim BPS_d = |Ω_d|`, so a potential-free abelianized quiver already
  realizes `{3,4}`. **D1-b as written asks for "arrows AND potential" — the
  potential half asks for an object the corpus records as unnecessary.**
  Scope-(a), conditional on the imported eq-(98) datum.
- **The `(7,1)` half of D1-b's target is a no-op** on `(4,3)` — the 2026-09-03
  (1) Result 0 applies to D1-b exactly as it did to D1-a.

And the live constraint carries over unchanged: `QuiverMirrorAutomorphismExcluded`
(sorry-free) — the mirror must act on the stability **ray**, never as a quiver
automorphism.

### Literature gap to plan around

**ACCERV, *BPS quivers and spectra*** — the triangulation-to-BPS-quiver
precedent — is **NOT held** in `library/`; it appears only in other papers'
reference lists. DGG (`arxiv-1108.4389`, `arxiv-1112.5179`), KS
(`arxiv-0811.2435`) and Davison–Meinhardt (`arxiv-1601.02479`) **are** held.
So the dictionary assembly needs an outbound fetch, not a corpus read.

### A methodology finding from running the checklist (PR #6510)

Path 5's tier 1 — `library/INDEX.md` — was **missing 33 real documents**, and
AGENTS.md explained the directories-minus-rows gap by the duplicate copies, so
the shortfall read as accounted for. Among the 33: the volume conjecture, the
oriented skein category, affine-Hecke Plancherel, knot polynomials on braid
closures, and q-deformed Plancherel growth. Regenerated with
`scripts/summarize-library.py --apply`; AGENTS.md corrected with the
arithmetic check that detects it. **A clean tier-1 scan is evidence about the
index, not about the library.**

### Scope

Scope-(a). DGG acts by `Sp(2N,ℤ)`, a strictly finer equivalence than
`GL × GL`, so a polarization-dependent construction is **NOT** excluded —
**D1-b is constrained at its entry, not refuted.** Certified `C` exists only
for 3₁, 4₁, 5₂ (the snappy wheel's Magma fixtures; the ptolemy DB is
firewalled). Exact integer arithmetic throughout; volumes printed for
orientation and never computed with. Nothing is wired, nothing is fitted, and
`A_ω` remains underived.

── 2026-09-03 (6): D1-b part 2 — the pincer closes, and the needle is threadable ──

`computations/qbeta/dt_d1b_nz_triangulation_invariance_pincer_probe.py`,
**7/7** (same PR #6509). Part 1 concluded the dictionary must be
polarization-dependent and deliberately left that open. This closes it.

### The bracket

| | |
|---|---|
| **too coarse** | the basis-independent invariant (part 1) is constant across all knots at fixed `N` |
| **too fine** | the RAW polarization datum is not a manifold invariant at all — retriangulating ONE manifold moves `(N, SNF(P), det P, rank P)` for `P = A_edge·B_edgeᵀ` |

The node count **is** a manifold invariant, so the dictionary must be
**strictly finer than the Smith normal form, yet triangulation-invariant.**

### The constructive half — that class is non-empty

The corpus already holds a verified member: the **Dimofte–Garoufalidis 1-loop
invariant `τ`** (`computations/one_loop_torsion.py`). Measured here it is
triangulation-invariant (spread `0.0` / `1.4e-40` at 40 dps) and it
**separates all five N=5 knots the SNF collided**, smallest pairwise gap
`0.555`:

    6_2  2.2165899308911189066      9_42    8.9879137538564859187
    7_3  2.7717413902489047800      10_139  6.7715656780558894839
    8_20 5.9288297060394782874

**So D1-b is LOCATED, not excluded** — the dictionary lives among the
triangulation-invariant functionals of the NZ datum.

### 🛑 Why NO `τ → C` map is proposed — a hard data limit, not caution

`τ` is a complex number, not an integer count; separating is not counting.
Sharper: **this corpus cannot test any such map.** Certified `C` exists for
exactly three knots (the snappy wheel's Magma fixtures; the ptolemy DB is
firewalled) and `τ` is **undefined on 3₁** because it is not hyperbolic. That
leaves **two** usable `(τ, C)` points, and any two-parameter family fits two
points exactly — a map fitted here would be **unfalsifiable by construction**.

**What would unblock the search is DATA, not cleverness:** more certified
connection counts, i.e. the ptolemy database or magma. That is now the
concrete dependency for D1-b, and it belongs beside D1-f's watch items.

### One thing I got wrong and fixed before it landed

The part-2 docstring first said "**eleven** distinct values" for 6₂.
`randomize()` walks a random move sequence, and the next run gave **nine**. A
stochastic count written as a fixed one is exactly the staleness pattern this
corpus keeps paying for. The docstring now says the count is stochastic,
points at the witness for the run's own figures, and notes that only the
qualitative fact — that it moves at all — is load-bearing; the assertion tests
`> 1`.

### Scope

Scope-(a). DGG acts by `Sp(2N,ℤ)`, strictly finer than `GL × GL`. Three
controls, including one (`C3′`) that exists because the invariance claim would
otherwise be vacuous — an invariance test passes trivially when nothing was
varied — and one (`C1′`) checking `τ(4₁) = √3/2` against DG's own worked
example, because the module records that **three** 1-loop implementations
existed here and disagreed. mpmath at 40 dps; no float64. Nothing wired,
nothing fitted, `A_ω` underived.

── 2026-09-03 (7): 🛑 CORRECTING entry (6) — six usable points offline, not two ──

Entry (6) above stated D1-b's blocker as *"DATA, not cleverness — the ptolemy
database or magma"*, on the ground that only **two** usable `(τ, C)` points
exist. **That is wrong and the error was mine.** It is corrected in the probe
(`dt_d1b_nz_triangulation_invariance_pincer_probe.py`, now **9/9**), and entry
(6)'s blocker sentence should be read as superseded by this one.

**How the error happened**, because the mechanism generalises: I inherited
*"the ptolemy DB is firewalled; only 4₁/5₂/3₁ ship fixtures"* from the corpus
and **never enumerated the directory**. Half of it was true and half was not,
and I carried both.

- **True, and re-verified this session:** `ptolemy.unhyperbolic.org` returns
  **403 on CONNECT** — by `curl` and by snappy's own `retrieve_solutions()`
  for 6₁.
- **False:** the wheel ships sl2 Magma fixtures for **seven** manifolds, not
  three. **Six** are 1-cusped, hyperbolic, and carry both a defined `τ` and a
  certified irreducible count:

| manifold | N | irreducible | \|τ\| |
|---|---|---|---|
| 4₁ | 2 | 2 | 0.86602540378443864676 |
| 5₂ | 3 | 3 | 1.1611627381339100731 |
| m135 | 4 | 8 | 11.31370849898476039 |
| s000 | 6 | 6 | 14.276474167114481671 |
| t00000 | 8 | 8 | 29.22901156226534965 |
| v0000 | 7 | 8 | 20.893884161273003105 |

Six points against a two-parameter family leaves **four degrees of freedom**,
so a candidate relation **is** testable offline. The blocker was overstated 3×.

### What does NOT change

**Still no `τ → C` map is proposed.** Six points make a candidate *testable*;
they do not make *fishing* legitimate. Searching a functional form across six
points and reporting the winner is the numerology this repo forbids. So the
corrected statement of D1-b's need is **a hypothesis stated before looking**,
not more data — and the probe's closing assertion now says that instead of
naming the ptolemy DB.

### Three caveats, recorded rather than papered over

1. `m135`, `s000`, `t00000`, `v0000` are **census manifolds, not knots in
   S³**. Valid for testing whether a relation exists; **not** automatically
   valid as D1-b nodes, since D1-b's setup is about knots (both 3-braids).
2. The **abelian `(L−1)` convention** is established for knots in S³ and does
   **not** carry over to a census manifold, so the common currency across all
   six is the **irreducible** count, which is what the table reports.
3. **`irreducible = N` fails.** It holds for four of six and breaks at `m135`
   (4, 8) and `v0000` (7, 8) — worth stating because it is exactly what one
   would assume from the 4₁/5₂ pair alone, where the two coincide.

### 🛑 A trap found while excluding 3₁

**`one_loop` does not guard against non-hyperbolic input.** Called on 3₁ it
returns `0.5` **without raising**, although `solution_type()` is
`contains flat tetrahedra` and DG's `τ` needs a genuine hyperbolic structure.
**A returned value is not evidence of hyperbolicity.** The probe therefore
excludes by an explicit `solution_type()` test, never by trusting an
exception — and any other consumer of `one_loop` should do the same.

── 2026-09-03 (8): the node count is ARITHMETIC — a single trace-field degree — and my prediction was WRONG ──

`computations/qbeta/dt_d1b_connection_count_galois_orbit_hypothesis_probe.py`,
**7/7**. Entry (7) concluded D1-b needs **a hypothesis stated before looking**,
not more data. This is that hypothesis, stated in the docstring before the
measurement, with a prediction recorded so it could be refuted.

### The hypothesis

> **H.** The irreducible boundary-parabolic PSL(2,ℂ) representations of a
> 1-cusped hyperbolic manifold form a **single Galois orbit** — the conjugates
> of the geometric representation — so `C_irr = [trace field : ℚ]`.

It came from noticing where the certified counts actually originate: the
certified probe sums **Galois-orbit degrees**, and those degrees are degrees of
the number fields the representations are defined over.

### H HOLDS, 6/6

| manifold | inhabited classes | orbits | degree | `C_irr` |
|---|---|---|---|---|
| 4₁ | 1 | 1 | 2 | 2 |
| 5₂ | 1 | 1 | 3 | 3 |
| m135 | 1 (of 8) | 1 | 8 | 8 |
| s000 | 1 (of 2) | 1 | 6 | 6 |
| t00000 | 1 (of 2) | 1 | 8 | 8 |
| v0000 | 1 (of 4) | 1 | 8 | 8 |

4₁ and 5₂ are **not** independent evidence — they are what suggested H. The
four census manifolds are, and all four are single-orbit.

### 🛑 My prediction was WRONG, and the way it was wrong is the useful part

I predicted **H fails at m135**, reasoning that m135 carries **eight
obstruction classes**, that an obstruction class is an `H²(M,∂M;ℤ/2)` invariant
the Galois action cannot move a rep across, and that eight inhabited classes
therefore cannot be one orbit.

The reasoning about Galois and obstruction classes is fine. **The premise was
not: m135 has eight classes and only ONE is inhabited — seven are empty.** I
read "8 classes" as "8 classes with solutions in them". Same wrong-denominator
error as three others today.

It was caught by control **C3**, which exists precisely to stop "one orbit"
being an artifact of dropping empty classes — and which therefore had to
*count* the empties: `{m135: 7, v0000: 3, rest: 1}`. A probe without that
control would have reported H holds and left the reason invisible.

### The consequence for D1-b — this REDIRECTS the route

**The node count does not come from the NZ gluing datum at all.** It is a field
degree. So the two earlier D1-b probes bracketed the wrong object: entry (5)
showed the NZ SNF is too coarse and entry (6) that the raw polarization datum
is too fine, and both are correct — but the count they were bracketing toward
is supplied by **arithmetic that does not involve the gluing datum**.

That **closes D1-b's node question positively** and leaves the **arrow**
question open. A dictionary still has to produce arrows and (if wanted) a
potential; nothing here touches that.

### Scope, and what would break H

Scope-(a). Six fixtures, four census manifolds not knots in S³ — valid for
testing H, **not** automatically valid as D1-b nodes. Irreducible counts only;
the abelian `(L−1)` convention does not carry to a census manifold. The
ptolemy DB stays firewalled, so this sample **cannot be enlarged offline**.

**H is almost certainly classical** in some form — the corpus-grep found
nothing, but that is a statement about this corpus, not the literature. And H
should be expected to **fail** for a manifold whose character variety carries
extra components beyond the geometric one; this sample is small and uniformly
well-behaved. Do not treat 6/6 as a theorem.

Nothing wired, nothing fitted, `A_ω` underived.

── 2026-09-03 (9): the bar grading of the node set, and a wrong consequence I caught by reading the Lean ──

`computations/qbeta/dt_d1b_trace_field_bar_grading_probe.py`, **8/8**, same PR
as entry (8). Entry (8) closed the **node** question and left the **arrow**
question open. Arrows in a bar-graded quiver need the bar grading *of the node
set*, and the single-orbit result says exactly where to read it: the nodes are
the embeddings of the trace field, complex conjugation acts on them, and a
representation is self-conjugate **iff its embedding is real**.

| manifold | deg | `r₁` fixed | `r₂` pairs |
|---|---|---|---|
| 4₁ | 2 | **0** | 1 |
| 5₂ | 3 | **1** | 1 |
| m135 | 8 | 0 | 4 |
| s000 | 6 | 0 | 3 |
| t00000 | 8 | 0 | 4 |
| v0000 | 8 | 0 | 4 |

**Five of six trace fields are totally imaginary.** 5₂ is the only one with a
real embedding — and it **cannot avoid one**: its trace field has **odd
degree**, and no involution acts freely on a set of odd size. So a mirror-fixed
node is *forced* for 5₂ and absent for 4₁, by parity rather than by any
property of the particular polynomial.

### 🛑 The consequence I nearly drew, and why it is wrong

I read this as an **escape** from `QuiverMirrorAutomorphismExcluded` — the
theory being that the theorem excludes a *freely acting* mirror, so a mirror
with a fixed point is a different object and 5₂ slips past it.

**I read the theorem before writing that down, and it does not say that.** Its
hypothesis is

```
hσ : ∀ e, Ω (σ e) = Ω e
```

— **count-invariance**, which says nothing about freeness. A `σ` with fixed
points can satisfy it perfectly well and is excluded on identical terms. **The
parity fact survives; the consequence does not.** Recorded rather than dropped
because it reads plausible and would have propagated into the arrow work.

### What this actually is

An **input** to the arrow question: the measured `(r₁, r₂)` is the bar grading
any bar-graded quiver on these nodes has to reproduce. It does not produce
arrows, a potential, or `A_ω`, and no construction is proposed.

### Scope

Scope-(a). Exact throughout — Sturm real-root **counting** on rational minimal
polynomials, no root-finding and no floats. Four of six are census manifolds,
valid for reading the grading and **not** automatically valid as D1-b nodes.
The ptolemy DB stays firewalled, so six is the offline maximum. Two independent
routes now give the same six numbers (orbit degrees in entry (8), polynomial
degree here), so neither is a parsing artifact.

── 2026-09-04 (10): 🛑 SUPERSEDED BY (11) — "the arrow count is FORCED" answered the wrong question ──

> **Read entry (11) first.** The Gabriel lever below is sound; the `(rank,
> spectrum)` pairs it was fed were not. Kept unedited as the record of the
> error.

── 2026-09-04 (10, as written): the ARROW count is FORCED — 0 or 1, by Gabriel, not by a fit ──

`computations/qbeta/dt_d1b_arrow_count_forced_by_gabriel_probe.py`, **8/8**.
Entry (8) closed the node question; entries (8)–(9) left the arrows open and I
reported having no lead. The lead was a counting argument, not a search.

### The lever

For an **acyclic** quiver with `W = 0`, **Gabriel's theorem**: finite
representation type ⟺ the underlying graph is a disjoint union of **simply-laced
Dynkin** diagrams, and then `#indecomposables = #positive roots`. Every ADE
diagram is a **tree**, so a rank-`V` union with `k` components has exactly
`V − k` edges.

**So the arrow count is a function of the Dynkin type, and the type is a
function of `(rank, #positive roots)`.** The rank is the node count — arithmetic,
from entry (8). The spectrum size the corpus supplies. The pair pins everything.

### The answer

| reading | 4₁ | 5₂ | arrows |
|---|---|---|---|
| abelian **is** a node | `V=3, spec 3` → **A₁+A₁+A₁** | `V=4, spec 4` → **A₁⁴** | **0** |
| abelian is **not** a node | `V=2, spec 3` → **A₂** | `V=3, spec 4` → **A₁+A₂** | **1** |

**All four are UNIQUE** — exactly one ADE type hits each `(rank, spectrum)`
pair. The arrow count is not chosen, it is read off. And each reading is
internally consistent across both knots, rather than one knot working and the
other not.

**The zero-arrow branch independently re-derives M2.** `A₁^V` is precisely the
potential-free **abelianized** quiver that `AomegaM2BPSCohomology` said already
realizes the target — reached here from Gabriel rather than from the
Davison–Meinhardt plethystic log. Two routes, same object.

### What this leaves open — a much smaller question

Not "what are the arrows" but **"is the abelian connection a node?"** — a
question about a convention the corpus already has an opinion about, not new
mathematics.

### 🛑 The assumption chain, because the result is conditional on it

- **(A1) `W = 0`** — the corpus's own M2 finding.
- **(A2) acyclic** — assumed; Gabriel requires it.
- **(A3) FINITE spectrum** — **load-bearing.** Infinite ⇒ non-Dynkin ⇒ nothing
  forced.
- **(A4) simply-laced** — B/C/F/G need valued quivers and are excluded, not
  overlooked.
- **(A5) the recorded DT count is the INDECOMPOSABLE count.** If the corpus's
  `(4,3)` are instead per-ray counts of **one** quiver, the total is ≥ 7 and
  rank-4 `A₁+A₃` (7 roots, **2 arrows**) becomes the candidate. **That reading
  is not tested here** and is the first thing to check before building on this.

### Method note

No search against the target. The ADE enumeration is exhaustive per rank
(2→2 types, 3→3, 4→6, 5→9), exact integer arithmetic, and a target is hit by
exactly one type or by none — there is nothing to tune. Controls: positive-root
counts reproduce the ten known values; every generated union has the requested
rank (so `edges = rank − components` applies); the enumeration is verified
complete at each rank.

Scope-(a). Nothing wired, nothing fitted, `A_ω` underived.

── 2026-09-04 (11): 🛑 CORRECTING entry (10) — the arrow count is NOT forced ──

Same probe, corrected in place before merge (`8/8`). Entry (10) concluded *"the
arrow count is FORCED to 0 or 1"*. **It answered a question the corpus did not
ask.**

### What was wrong

Entry (10) read the target `(4,3)` as **two knots' total spectra** — 4₁ with 3,
5₂ with 4 — and set `rank = C_irr` per knot from the merged Galois-orbit result.
**This bean says otherwise, in as many words, at line 36:**

> Target object (post-pruning): **(Q, W, ray+, ray−)** — quiver with potential
> plus **TWO stability rays, ray-wise DT counts (4,3)**, bar split (7,1).

So `(4,3)` are **ray-wise counts of ONE quiver** — its bar-conjugate ray pair.
The numerical coincidence that `C(4₁) = 3` and `C(5₂) = 4` is what made the
misreading available, and I took it.

### Two things break, and the second is the substantive one

1. A stable object has a **definite slope**, so the two rays' stable sets are
   **disjoint** and the total is `≥ 4 + 3 = 7`, not 3 or 4.
2. **`rank` is no longer the per-knot node count at all.** The target is ONE
   quiver spanning the pair, so the merged `C_irr = [trace field : ℚ]` result —
   which is **per knot** — **does not pin its `V`**. The chain *"rank = node
   count"* was broken from the start under this reading. That is the real
   error; the arithmetic was fine.

### The corrected result — a constraint table, not a resolution

`V ≥ 4` (a ray carrying 4 needs it, from the merged per-ray ceiling) and
total `≥ 7`. If the spectrum is exactly the two rays:

| rank | type | arrows |
|---|---|---|
| 4 | `A₁+A₃` | **2** |
| 5 | `A₁+A₂+A₂` | **2** |
| 6 | `A₁⁴+A₂` | **1** |
| 7 | `A₁×7` | **0** |

**The arrow count is `{0,1,2}` depending on `V`, and nothing in the corpus pins
`V`.** So the arrow question is **still open** — better constrained than before,
but not resolved.

### How the error happened

Entry (10) listed **(A5)** *"the recorded DT count is the indecomposable
count"* as an assumption **and named it the first thing to check before building
on the result.** It was wrong, and checking it took **one grep of this bean**.

**Flagging a weak assumption is not the same as testing it.** The flag made the
overclaim feel safe to publish; it did not make it true. Where a probe's own
author can name the assumption most likely to be wrong, that is the assumption
to spend ten minutes on before writing the headline, not after.

Scope-(a). Gabriel lever unchanged and sound; exact integers; nothing wired; no
fit; `A_ω` underived.


## 2026-09-04 (12) — entries (10) and (11) are BOTH void: the Gabriel route does not apply

Entry (10) said the arrow count was forced to 0 or 1. Entry (11) corrected that
to `{0,1,2}` with `V` unpinned. **Both are void, and for a reason neither of them
touched:** they apply Gabriel's theorem to a datum Gabriel's theorem cannot
describe. `dt_d1b_gabriel_route_void_source_verified_probe.py` (6/6).

**The source, read for the first time.** GGM `arXiv:2012.00062v3` is held in
this repo (`library/arxiv-2012.00062v3/`). Immediately under eq (96)/(97) it
says, verbatim:

> "where the non-vanishing off-diagonal entry of `S_{σi,σj}` is the Stokes
> constant associated to the Borel singularity `ι_{i,j}`. Assembling these
> off-diagonal entries in a matrix, we obtain the matrix (98)"

So each eq-(98) entry is **one Stokes constant at one Borel singularity** — a
multiplicity at a single charge. `Ω(ι_{1,2}) = 4` is a degeneracy of four at one
ray, **not** four distinct objects at four distinct charges. Every arrow-count
argument in (10) and (11) read it the second way.

**Why that is fatal.** Gabriel's bijection sends positive roots to
indecomposables with multiplicity **exactly one**, so any finite-representation-
type quiver has `max_d Ω_d = 1`. The datum has `max |Ω| = 4`. **No finite-type
quiver carries it, at any rank, with any arrow count.** Scope-**(b)** structural
exclusion in the AGENTS.md sense — the invariant cited is Gabriel's bijection
itself, not a failed search.

**What the source gives back (both new — six-path grep returned 0 hits for
either).**

* **F1.** The index set is **three** σ-indexed perturbative series, so the
  singularities `ι_{i,j}` run over **six ordered pairs**, not three.
* **F2.** `S⁺` populates `{(3,1),(3,2),(1,2)}` and `S⁻` populates
  `{(1,3),(2,3),(2,1)}` — **exactly the two opposite orientations of the same
  three unordered pairs** `{12,13,23}`. The bar-conjugate ray pair the whole D1
  programme is chasing is not two arbitrary stability rays: it is the two
  orientations of a 3-node complete graph. Verified mechanically (C2).
* **F3.** eq (100), `S^(k)_{σi,σj} = −S^(k)_{σφ(i),σφ(j)}` with `φ = (1 2)`, is
  stated in the source for the q-series coefficients; it is checked here on the
  eq-(98) **constants** and holds (C4). `φ` is **sign-reversing**, hence
  count-breaking — independently agreeing with `QuiverMirrorAutomorphismExcluded`,
  which requires `Ω(σd) ≠ Ω(d)` of any mirror reading (4,3). Two different
  routes to the same constraint; the Lean was not an input to this check.

**HYPOTHESIS, labelled, not a result.** `V = 3` (the three σ) with **3 arrows**
(the three unordered pairs), the two rays being the two orientations. It is only
a hypothesis because in the KS description the arrows are the **Dirac pairing on
the charges**, not the set of populated Borel singularities — F2 says which
singularities are populated, which is evidence about the arrow set, not the
arrow set. **Disconfirmation test:** compute `⟨γ_i,γ_j⟩` on the 5₂ spectral-curve
charge lattice; if it is not supported on exactly `{12,13,23}`, H is dead. That
needs charge-lattice data this probe does not have, and is the honest next rung.

**The lesson, and it is the third of this kind on this object.** (10) was wrong
about the arithmetic's inputs and I caught it by grepping the bean. (11) was
wrong about the *premise* and the bean could not catch it — only the source
could, and the source has been sitting in `library/` the whole time. Corpus-grep
path 5 exists precisely for this, and I ran paths 0/2/3/6 twice on this object
without ever running path 5 on the paper the datum is quoted from. **When a
probe's input is a quoted equation, read the equation.**

**Addendum to (12), same session — the next rung is blocked on DATA, measured.**

The disconfirmation test above wants the Dirac pairing on the 5₂ charge lattice.
The corpus turns out to carry exactly the right scaffolding and it is **dead**:
`QOU/Mathlib/WallCrossing.lean` declares `ChargeLattice` (with an antisymmetric
integral Euler pairing), `CentralCharge`, `BPSState`, `BPSSpectrum`, `Wall` and
`KSWallCrossing` — and has **0 instances, 0 importers, and 0 mentions anywhere
else in `folio/quantum-observable-universe/`** (grep 2026-09-04, excluding
`.lake/`). It compiles only because the QOU library is glob-declared. So the
test is blocked on *data*, not on infrastructure, and that is now a measurement
rather than my assertion.

**Deliberately NOT instantiated.** Handing `ChargeLattice` the eq-(98) matrix as
its `euler` field would assert that eq (98) *is* the Dirac pairing — which is
precisely hypothesis H, and would launder it into Lean. §"Axiomatization is NOT
a Proof" forbids exactly this move.

**C7 — the next trap, pre-empted, because it is the same shape as the two
already sprung.** eq (98) is antisymmetric, and an antisymmetric integer matrix
indexed by three objects looks exactly like a quiver exchange matrix. Reading it
as one gives arrows straight off `|B|`: **4 + 3 + 3 = 10 arrows on 3 nodes** — a
*different* answer from H's 3, and just as immediately available. But **both
readings entail antisymmetry** (the source's CPT / particle-antiparticle sign on
Stokes constants; `B_ij = −B_ji` by definition), so observing it separates them
not at all. There are **729** antisymmetric 3×3 integer matrices with entries in
`[−4,4]`; eq (98) is not distinguished by being one of them. Only the source
decides, and the source says Stokes constants.

That is now **three** distinct "obvious" readings of one 3×3 matrix, giving
arrow counts 0/1, `{0,1,2}`, 3 and 10. The object is not underdetermined by
accident — a small integer matrix admits many structural readings, and the only
thing that has ever discriminated between them in this arc is the sentence
printed under the equation in the paper.

**🛑 CORRECTION to the addendum, same session, ~20 minutes later. "0 importers"
was not a finding and I let it read as one.**

The addendum above reports `WallCrossing.lean` as having "0 instances, 0
importers, 0 mentions" and lets all three carry equal weight. **The importer
count is unremarkable.** Measured over the QOU tree on 2026-09-04:

    total QOU modules                 2566
    never imported anywhere            866   (33.8 %)

A third of the library is unimported. It is a long-tracked class with its own
detector — [`content/pipeline/lean-orphan-audit.ts`](content/pipeline/lean-orphan-audit.ts),
beans `qou-orph` / `qou-kljb`, which measured 761 of 1598 (47.6 %) on
2026-08-07 — and the module compiles regardless, because the QOU library is
glob-declared (`globs = ["QOU", "QOU.+"]`). Being unimported makes
`WallCrossing.lean` **ordinary**, not notable, and quoting it alongside the
other two numbers implied a discovery that a five-minute check deflates.

**What is actually specific, and is the load-bearing half: ZERO INSTANCES of
`ChargeLattice` and `KSWallCrossing` anywhere in the tree.** That is a different
and stronger statement — an imported module can have no instances, and an
unimported one can have instances inside itself — and it is the fact that
blocks the Dirac-pairing test. Quote the instance count; drop the importer
count.

Nothing else in (12) or the addendum moves: the Gabriel exclusion, F2, F3 and
C7 are untouched, and the test is still blocked on data.

## 2026-09-04 (13) — (12) merged as #6597; the lattice rung is `qou-rutm`, and H is UNSTATED

The Gabriel-void result merged to `main` (`a46ddb84a7`, rebase). PR #6566 was
recreated as **#6597** via the all-REST route — GitHub's GraphQL draft toggle
was rate-limited ~40 min while REST stayed live, the split recorded in
`merge-coordinator` memory; recreating beat waiting it out, 1st try.

**The lattice rung is opened as `qou-rutm` and its first pass closes three
routes.** The short version, because it changes what "blocked" means here:

* **R1.** GGM `arXiv:2012.00062v3` — the paper that produced the datum — contains
  **0** `"charge lattice"` and **0** `"Dirac pairing"`. Its 2 `"symplectic"` are
  both §7, both naming Neumann–Zagier. H's test has no referent in its own source.
* **R2.** The NZ datum is **Lagrangian on the edge block** (`A·Bᵀ` symmetric — the
  NZ symplectic theorem — so the antisymmetrization is exactly zero), and its
  entire antisymmetric content is the **rank-2 cusp block** `(μ,λ)` at `±2`.
  Both 4₁ and 5₂, so structural. eq (98) is rank 3 ⇒ NZ cannot carry it at any
  index set. **Scope-(b).**
* **R3.** KRSS quivers are **symmetric** by the paper's own definition; eq (98) is
  antisymmetric ⇒ not a KRSS quiver matrix. **Kept separate** from this bean's
  standing *"refuted KRSS open-sector route (det(K)=5)"* — different claim,
  different construction, neither is evidence for the other.

**So H is UNSTATED, not unconfirmed.** "The Dirac pairing on the charges" does
not yet denote anything: the missing object is a map `{σ₁,σ₂,σ₃} ⟶ Γ` with `Γ`
carrying an antisymmetric integral pairing, which would come from the 3d-3d
flavour lattice of `T[5₂]` — not held in `library/`, not computable here. The
next step is **acquiring a source**, not another probe against what is held.

Detail and the 6/6 probe: `qou-rutm`, PR #6599.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-22 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-15 — re-scoped by the γγ rule

The owner ruled that the γγ selection rule also covers the nuclear bond letters. Any number in this bean computed on the single-crossing interface letters of `atom_braid_word_3A` (`d_k`, `μ_e`, the chain law `∏(z_D + d_k)`, the `b₃` magnitudes −1.2277 / −0.7973 MeV, or a sign map on that word) is now a record of a superseded word, not a current result. Lean results stated for generic bond weights are unaffected. The redo waits on a γγ-selected word per nucleus (PR #7876). Record: `docs/audits/2026-11-15-gg-rule-rescopes-old-letter-binding.md`. The bean stays open.

## Round 69 Formalization Progress (PR #8293)
- Formalized `QOU.QBeta.AdjointIndexSetM3.pkSize_and_floorRemainder_three_knot_totals` (sorry-free, 0 advisories across all 6 static vacuity audits).
- Verified at 80-dps `mpmath` (`computations/probes/scale_mobius_adjoint_reduced_trefoil_probe.py`, `scriptHash: ae187b673714`, Commit 1 `9b139cda51963d9af6817b576a80c90bb2f74d00`, Commit 2 / Witness `474ee8c61ef5b687f244b6a129aeb23ef9956372`, PR `litlfred/qou#8293`).
