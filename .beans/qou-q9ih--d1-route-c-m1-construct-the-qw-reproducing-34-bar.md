---
# qou-q9ih
title: 'D1: Route C M1 — construct the (Q,W) reproducing {3,4} + bar split (7,1); fitted quiver = candidate only (parent qou-rtec)'
status: in-progress
type: task
priority: normal
created_at: 2026-08-15T02:49:30Z
updated_at: 2026-08-22T20:24:44Z
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
