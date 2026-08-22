---
# qou-btvl
title: 'D3: cross-knot DT data — 6_1 + harden 5_2 (import tier; parent qou-rtec)'
status: completed
type: task
priority: normal
created_at: 2026-08-15T02:49:30Z
updated_at: 2026-08-21T21:47:54Z
---


## Handoff note (2026-08-15, post-completion)

Slope hardening landed (SnapPy normal_boundary_slopes, exact). The OTHER
half of the cross-knot data — #boundary-parabolic connections (R1's
count; 5₂ = 4 literature-recalled, 6₁ = unknown third-knot test point
for dtMax = recursionOrder+1) — is NOT hardenable in this sandbox:
snappy.ptolemy_variety(2,'all').retrieve_solutions() needs
ptolemy.unhyperbolic.org, which 403s through the proxy, and local
Groebner (magma/sage) is unavailable. A network-open or sage-equipped
environment can close it in minutes with the same probe pattern.

## 2026-08-15 update — #connections CERTIFIED after all (egress workaround)

The ptolemy-DB-firewalled handoff above is RESOLVED for 4₁/5₂: per the
owner's egress hint, the snappy WHEEL itself ships the certified Magma
primary-decomposition outputs (ptolemy/testing_files). Probe
dt_crossknot_connection_count_certified_probe.py: 4₁ = 2 irreducible
(one degree-2 orbit, x²−x+1 = ℚ(√−3)) + 1 abelian = 3; 5₂ = 3 (one
degree-3 orbit, x³+2x²+3x+1, the trace-field cubic) + 1 = 4. R1's
counts are now locally computed, not literature-recalled. Residual:
6₁ has no bundled data — the dtMax=recursionOrder+1 third-knot test
still needs the DB or magma. Pattern documented in the new
.claude/skills/local/sandbox-egress.md skill.

## 2026-08-15 THIRD-KNOT A-POLY LEG CERTIFIED (owner upload 08c56228)

Culler census tarball (uploads/A_census.tgz): 6_1 = K4_1 (snappy
identify) has geometric L-degree 4, full 5; 4_1/5_2 re-certified (2/3
geom; the K2_1 support EQUALS the Lean a41Monomials). Probe:
apoly_census_ldegree_certification_probe.py, 3/3. The 6_1 prediction
chain (DT_max = #connections = 5) is recorded as PREDICTION — the
independent resurgence DT count for 6_1 is still the missing piece of
the third-knot test (full=geom+1 is by construction, not a test).

## 2026-08-19 — a sibling used this output and got r(6₁)=4 three independent ways

PR #5293 (`qou-gz37`, `claude/gz-third-knot-rank-grading-2026-08-19`, draft)
reads BOTH this bean's census A-polynomial output and `qou-6ort`'s ki6c
extraction, and credits them. Result: `r(6₁) = 4` by three independent routes —
DG §6's algebraic number field (`x⁴−2x³+x²+3x+1`, disc 257), this bean's Newton
polygon (geometric A-poly L-degree of K4_1), and ki6c's stationary-phase gluing
quartic — with an EXACT field-equality witness between the first and third
(`γ := −α³+3α²−4α−1` satisfies `γ⁴−γ³−4γ²+4γ+8 = 0`, `γ/2` a root of the ki6c
quartic; index-2 scaling, disc 16448 = 2⁶·257).

**They independently confirmed, and improved on, this bean's two caveats.**
The `full = geom + 1` leg being definitional (not evidence) is now the Lean
theorem `plus_one_leg_is_definitional`; and "these are saddles/critical points,
the DT invariants live on the rays BETWEEN them — so none of this is a DT
count" is stated in their artifacts. My prose caveats became theorems.

**This bean's open item is NOT closed and they say so**: an independent
resurgence DT count for 6₁ is their open item 1, naming this same gap. `r` is
the R1 *shadow*, not the count.

**Also from their sweep, worth carrying**: their M3 sweep keyed on the word
"Stokes" and missed three load-bearing papers — ki6c has ZERO "Stokes" hits.
The lesson generalises the corpus-grep discipline: *a sweep keyed on the
vocabulary of the answer you expect will miss the paper that answers in
different words.* Re-sweeping on structural vocabulary matched 94/371.

Coordination posted on #5293; `r`, the field identification, and the
9₁₂ / (−2,3,9) predictions are theirs. Do not re-derive.

## 2026-08-19/21 — the 6₁ DT count is now a DISCRIMINATOR, not just a test

A third sibling (`qou-xpgq`, PR #5294) proposed indexing the Stokes constant
set by the braid index via the Wedderburn pair `(p(n), I(n))` — `(3,4)` at n=3 —
then **retracted most of it** (duplicated PR #4567; misstated 5₂ as carrying
`{3,4}` flat when it SPLITS across chirality; and #4567 had already found the
contrary result that no single scalar clones across the two knots).

What survives, at their own stated low confidence — a bare guess, not a corpus
candidate — still raises this bean's value:

    R1 (DT_max = #connections)          predicts 6₁ → {5}
    Wedderburn at the braid index       predicts 6₁ → {5, 10}   [p(4)=5, I(4)=10]

**The 10 is the discriminator**; R1 cannot produce it. So if `qou-btvl` ever
lands a 6₁ DT count it *decides between two readings*, rather than only testing
the DT correspondence. Worth the extra weight when prioritising.

**Braid-index caveat I verified for them (honest negative).** They flagged that
6₁'s braid index 4 was literature-recalled, unverified, and load-bearing for the
`{5,10}` arithmetic. I could not verify it either, and the obvious tool is a
TRAP: `snappy.Link(K).braid_word()` returns a NON-minimal representative —
5₂ gives 4 strands where the true braid index is 3. 4₁ gives 3 (coincidence),
6₁ gives 5, 9₁₂ gives 6. Morton–Franks–Williams would settle it but this SnapPy
build ships no HOMFLY (`Link` exposes only alexander/jones; spherogram exports
none). Needs KnotInfo or a HOMFLY implementation. Posted on #5293.


## 2026-08-21 — RESIDUAL CLOSED. 6_1 = 5 boundary-parabolic connections.

This bean's handoff said the 6_1 count 'is NOT hardenable in this sandbox'
because ptolemy.unhyperbolic.org 403s and magma/sage are absent, and the
certified probe repeated it ('6_1 has no bundled data'). Both were right about
the DATA and wrong about the REQUIREMENT.

Only retrieve_solutions() needs the network. Manifold.ptolemy_variety() builds
the ideal OFFLINE, and for these knots it is tiny -- 4 tetrahedra, 4 Ptolemy
coordinates, 5 equations, 2 obstruction classes. A sympy Groebner basis over QQ
settles it in seconds. No DB, no Magma, no sage.

    4_1   2 irreducible + 1 abelian = 3     reproduces the certified probe
    5_2   3 irreducible + 1 abelian = 4     reproduces the certified probe
    6_1   4 irreducible + 1 abelian = 5     <- the missing input

Producer: computations/qbeta/dt_crossknot_sixone_connection_count_groebner.py

### The trap, recorded because the wrong answer is the plausible one

SnapPy's equations_with_non_zero_condition appends the Rabinowitsch polynomial
1 = c1 c2 c3 c4 t. Without it, 6_1's obstruction class 0 contributes a spurious
rational point with c_0011_2 = 0 -> 5 irreducible, 6 connections, which would
have REFUTED R1. I ran it that way first and reported 5. The probe now computes
and prints BOTH forms so the difference is visible rather than assumed away.

### Independent gate

Each class-1 ideal is a single Galois orbit; its field must be the knot's known
trace field. Discriminants: -3, -23, 257 = Q(sqrt-3), the cubic of disc -23,
and the quartic of disc 257 -- tabulated trace fields of 4_1, 5_2, 6_1. Nothing
in the count computes a trace field, so this is a real check, not a restatement.

### What this does and does NOT settle

SUPPLIES R1's input. DT_max = #connections, so R1's 6_1 prediction is now the
definite {5}.

DOES NOT test R1. The third-knot test still needs an independent
resurgence/Borel DT count for 6_1, absent from the corpus. That is now the
ONLY missing piece.

But the test is live in a way it was not: both candidates are definite --
R1 -> {5} against Wedderburn-at-the-braid-index -> {5,10}, the latter definite
only because braid index(6_1) = 4 is now DERIVED (qou-dr8m, MFW + explicit
4-strand word) rather than recalled. This bean's own note said 'two knots of
equal braid index test a braid-index rule not at all' -- 4_1 and 5_2 are both
index 3, 6_1 is 4, so 6_1 is the first point where it is testable.


### CORRECTION to the note above (same day, before it stood)

I wrote '<- the missing input', implying the 4 was new. It is NOT. Re-reading
this bean's own 2026-08-19 entry: PR #5293 (qou-gz37) already derived
r(6_1) = 4 THREE independent ways, one of them 'DG §6's algebraic number field
(x^4-2x^3+x^2+3x+1, disc 257)'. That is character-for-character the polynomial
and discriminant my Groebner basis produced.

So the honest framing is a FOURTH route, not a first derivation:

    #5293 route 1   DG §6 algebraic number field
    #5293 route 2   Newton polygon / geometric A-poly L-degree of K4_1
    #5293 route 3   ki6c stationary-phase gluing quartic
    this            Ptolemy variety over QQ, Groebner, non-zero condition

Route 4 is genuinely independent of 1-3: it never touches the A-polynomial,
the Newton polygon, or the ki6c asymptotic. It goes through the gluing-variety
ideal itself. Getting their exact quartic out of a different construction is a
real cross-confirmation of their field identification — and cuts the other way
too, since my first (wrong) run got 5 and their 4 is what a correct run
reproduces.

What is arguably new here is small and should be stated as such: the count is
obtained WITHOUT the A-polynomial, and the '+1 abelian' step is flagged as the
same definitional move this bean already flags for 'full = geom + 1' — so the
computed content is the 4, and the 5 remains one convention away from it.

UNCHANGED: the third-knot test still needs an independent resurgence/Borel DT
count for 6_1. That is #5293's open item 1 and it is still open. r is the R1
shadow, not the count.
