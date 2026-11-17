---
# qou-0y6l
title: Sweep L6a4 obstruction classes 2-13 with the saturated msolve pipeline
status: in-progress
pr: 8240
updated_at: 2026-11-17T07:03:07Z
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-06T03:41:37Z
updated_at: 2026-10-04T15:14:01Z
parent: qou-r9ih
---

## 2026-09-06 — why three class-2 attempts produced no verdict, and the fourth is running

**None of the three failures was mathematical.** Each died when the filesystem
filled; the third took its own log with it, so its outcome is unknowable.

**Root cause (not the solve).** `scripts/setup-lean-toolchain.sh` runs as a
SessionStart hook and re-stages **5.0 GB** of Lean on every resume — a 697 MB zip
it never deletes plus a 4.3 GB extract, into `/tmp`, which does not survive a
container. Quota ~38 GB, resident repo ~33 GB: **33 + 5 = 38.** One resume fills
the container with no compute running. Fixed in `1432473982` (drop the zip after
extract; refuse to stage below ~6 GB free). Verified on the next resume — no
re-stage, disk held at 5.0 GB.

**A full disk is not a degraded session, it is a dead one:** the harness cannot
write a child's stdout, so every command fails including the `rm` that would fix
it. Reached <100 KB free twice.

**Caps for the fourth attempt are asymmetric on purpose** (15 GB RAM / 13 free,
5.0 GB disk): `ulimit -v` 10 GB generous — an OOM kill is survivable;
`ulimit -f` 1 GB tight — a runaway `.res` is not. Capping memory tightly was my
first draft and is the wrong instinct: it constrains the plentiful resource.

**Two corrections of my own.**
1. Class 2 keeps **11 variables** vs class 1's 12 — my original figure. My
   "correction" to 12/13 was wrong: that is the `.ms` header, which also counts
   msolve's linear form `u`. Two conventions, not a discrepancy. Confirmed live by
   the run: `eliminated 16 -> 11 vars, 17 eqs, maxdeg 12, 129.6s`. Better size
   signal: **59,475 bytes vs 10,225 — 5.8x the polynomial data.**
2. The sibling branch's class-1 result is **not** independent confirmation. Both
   result commits are patch-identical across the branches
   (`c6622b885874`, `359769e26b60`) — same patches, different SHAs after rebase.
   One computation, not two. Class 1's real evidence stays its **round trip**.

**Whatever class 2 returns is PROVISIONAL.** The driver lets elimination consume
`t` and re-imposes the non-zero condition only on surviving variables, so it does
not restore it by construction — eliminated coordinates' denominators can still
vanish at a solution. No dimension/degree may be reported until
`ptolemy_exact_character.py` round-trips a point against snappy's original
equations. That gap is exactly what forced the class-1 retraction in #6815.

## 2026-09-06 10:26 — the staircase route is CALIBRATED on a real corpus system

`gb_staircase.py` reproduces **L6a4 class 1 = dim 0, degree 4** from the Groebner
basis ALONE — no RUR, no parametrisation — matching the independently established
result (over Q, round-tripped witness, #6815 as corrected). Five hand-checked toy
ideals also pass. The tool can now be trusted on class 2.

**Timing, and it is informative.** GB only, 1 thread: **286 s** (10:21:22 →
10:26:08). Full RUR for the same class: 373 s. So for class 1 the Groebner basis is
most of the cost and the FGLM change-of-order is cheap — unsurprising at degree 4,
where the linear algebra is tiny.

**That sharpens what a class-2 timeout would mean.** My stated rationale for the
probe was that FGLM is 'routinely dominant' for a high-degree ideal. Class 1 does not
exhibit that, because its degree is 4. So if the class-2 GB also times out, the cost
is in the Groebner basis itself and no RUR budget helps; if the GB lands quickly, the
degree is large and FGLM was indeed the wall. Either outcome is diagnostic — which is
the property a blind longer run does not have.

**The verdict remains ASYMMETRIC** (recorded in the tool's own output): the FKR
reduction clears denominators via `numer(q.subs(x,-B/A))`, ADDING the locus {A=0},
so genuine solutions inject into the reduced system but not conversely. EMPTY would
be conclusive; NON-EMPTY is an upper bound only, and — the limitation I missed when
launching — a Groebner basis supplies no POINT, so a non-empty GB-only verdict cannot
be round-tripped at all without the RUR.

## 2026-09-06 10:43 — the class-2 GROEBNER BASIS also times out: the direct route is CLOSED

`msolve -g 2`, 2700 s, 3 threads: **exit 124, zero bytes.** With the calibration this
settles which half of msolve is expensive, and therefore closes the route:

| | |
|---|---|
| class 1, GB only, 1 thread | **286 s** |
| class 1, full RUR | 373 s (so FGLM is ~23%) |
| class 2, GB only, 3 threads | **> 2700 s** (>9x wall on 3x threads) |

For class 2 the **Groebner basis itself is the wall**. No RUR budget helps; a longer
run of the same shape cannot succeed.

**This corrects my own rationale.** I launched the probe saying FGLM is 'routinely
dominant for a high-degree ideal'. Class 1 does not exhibit that — at degree 4 its
linear algebra is trivial. The probe was still right (diagnostic either way) but the
reason I gave was unsupported by the single data point I had.

**The presentations are IDENTICAL**, which sharpens everything: asked directly, every
class 1–13 presents as **27 vars / 33 eqs** (class 0 differs at 26/32, being the
trivial class carrying the geometric rep). So class 1 settles in 373 s and classes
2/3/4 exceed 900 s *from the same size of presentation*. The ideal's SHAPE does all
the work.

**A negative I will not dress up:** I tried to detect symmetry orbits among the 14
classes with a cheap signature, hoping the order-48 symmetry group (Z/2 × octahedral)
would collapse the sweep. My invariant was broken — it counted '+'-separated terms and
returned (1,1,1,1,1,1) for every class, i.e. no information. The orbit question is
untouched and open.

## The unlock is probably NOT more compute — it is a 403

`V.retrieve_solutions()` for class 2 resolves to a real file in the Ptolemy database:
`ptolemy.unhyperbolic.org/data/pgl3/HTLinkExteriors/08_tetrahedra/L6a4__sl3_c2.magma_out.gz`
— **the exact object we have failed three times to compute.** The agent proxy denies
that host (CONNECT 403, policy denial, same class as release.lean-lang.org). This is an
egress limit, not a mathematical one, and it is the single highest-value unblock
available: if that host is allowed, classes 2–13 may be answerable by retrieval rather
than re-derivation.

## 2026-09-06 11:00 — literature search for the duality step: NOT FOUND, and the near-miss is instructive

The conditional needs one antecedent: **duality negates the obstruction class**. Corpus-grep
path 5 over the 576 held documents does NOT supply it. What it does supply is two traps.

**Trap 1 — the section titled 'Duality' is a different duality.** `arxiv-1207.6711v1`
(*Gluing equations for PGL(n,C)-representations*, the paper defining our varieties) has
§12 'Duality'. It is Ptolemy-coordinates ↔ shape-coordinates (Fock–Goncharov A ↔ X), a
COORDINATE duality. It is not representation duality ρ ↦ ρ*. Citing it for the antecedent
would be a textbook conflation. That paper mentions 'obstruction' exactly ONCE, about ±I
for EVEN n — not our case.

**Trap 2 — the paper that defines obstruction cocycles does so over Z/2, not Z/3.**
`arxiv-1111.2828v2` (*The complex volume of SL(n,C)-representations*) §9.1 'Obstruction
cocycles and the pSL(n,C)-Ptolemy varieties' defines σ ∈ **Z²(K; Z/2Z)** — the pSL case,
where the centre is ±I. Ours is **Z/3**, the centre μ₃ of SL(3), via snappy's
`PtolemyGeneralizedObstructionClass`. Same word, different group; the Z/2 statement does
not transfer, and 2c=0 in Z/2 is vacuous whereas 2c=0 in Z/3 forces c=0 — the whole
argument turns on exactly that difference.

**Status: the antecedent is UNVERIFIED and the measured structure stands on its own.**
H²=(Z/3)³ and the ±involution are measured facts (`obstruction_gerbe_involution.py`,
6/6 checks). The Sym² consequence remains conditional and must not be reported as a
result. Next: find the generalized (Z/N) obstruction-class definition — Garoufalidis–
Goerner–Zickert is the likely source and does not appear to be held — and check how ρ ↦ ρ*
acts on it. That single step converts a 12-class compute problem into a theorem.

## 2026-09-06 12:50 — the Sym² question is CLOSED; the group theory behind it is formalised

**Result.** L6a4 obstruction classes 1–13 cannot carry a self-dual representation, hence
cannot contain Sym² of an SL(2,ℂ) rep. The gate passes for all thirteen **with no Gröbner
basis**. The 12-class sweep is unnecessary for the gate's purpose.

Two halves, both established here rather than cited:
1. **Derived:** `c* = c^{-1}` from the obstruction cocycle — inverse-transpose is a
   *homomorphism* ((AB)^{-T} = A^{-T}B^{-T}), and it inverts the centre. With
   `c = -c ⇒ 2c = 0 ⇒ c = 0` (2 invertible mod 3), only the trivial class can be self-dual.
2. **Measured (the relative gap):** negating the cocycle acts on the Ptolemy variety as
   `u → u²`. P^c and P^-c differ in 10 of 33 equations; substituting u→u² through P^c
   reproduces P^-c exactly as polynomial sets, classes 1/2/3.

**Formalised, sorry-free, lean-direct EXIT 0** (`ObstructionClassForcesComplexType.lean`):
`cocycle_map`, `cocycle_dual` (=obs_dual), `cocycle_conj`, `cocycle_conj_of_comm`
(=obs_congr), `obs_neg_of_inv` (the μ₃≅ZMod 3 bridge). Axioms: [propext] / [propext,
Quot.sound]. **Still not an instance** — needs H² (cocycle→class) and the relative step,
neither of which is algebra.

**Compute route closed, with a measured reason.** Class-2 GB alone > 2700 s; calibration
put FGLM at only ~23 % of class 1's cost, so the Gröbner basis IS the wall and no RUR
budget helps. All classes 1–13 present as 27 vars/33 eqs, so shape decides cost, not size.

**Three broken detectors of my own this session, all the same class:**
- `Mathlib*.olean` glob → reported 4 oleans, true count 3471. Made me decline the Lean
  work as impossible when the cache was there all along.
- String comparison of polynomials → false NEGATIVE on the true u→u² statement.
- `pdftotext` absent → reported 8 PDFs as "no text layer", a property of my toolchain.

**Lean binary was missing by my own hand** — both elan toolchains are symlinks into /tmp
and I deleted the targets clearing disk. Re-staged from the GitHub release asset
(allowlisted; release.lean-lang.org is not). Extract is 2.44 GB, not 4.3 GB.
`git repack -d` freed only **54 MB** — loose objects were already efficient; packing moved
bytes. Do not reach for it as a space fix.

## 2026-09-06 13:00 — snappy's own saturation route ALSO times out: three routes, three negatives

Full 27-var system, saturate by every variable, over ℚ, in Singular (Sage's Gröbner
engine, so this is what `compute_solutions(engine='sage')` runs). **exit=124 at the full
5400 s** (11:30:11Z → 13:00:11Z — ran to the wall, not an early failure).

**The class-2 compute picture is complete, and every route is a measured negative:**

| route | engine | result |
|---|---|---|
| FKR-reduced, RUR | msolve | > 3000 s |
| FKR-reduced, GB only | `msolve -g 2` | > 2700 s |
| full system + saturation | Singular | > 5400 s |

These are **not three attempts at one thing**. The first two are the corpus's custom
reduction (11 vars, fast for class 1, *provisional* — clearing denominators adds {A=0});
the third is snappy's own route (27 vars, *sound by construction* — saturation removes the
degenerate components). Small-and-provisional and large-and-sound both fail, so the
difficulty is in the ideal, not in a choice of formulation.

**No fourth attempt.** Each route answered something the previous could not; none was a
longer run of the same shape. Nothing available here differs in kind: Magma absent, Sage
absent (Singular is its engine — that is why it was the right proxy), and the Ptolemy
database holds no pgl3 data for this manifold.

**Open:** non-emptiness, dimension, degree, irreducibility of classes 2–13.
**NOT open:** the Sym² gate — settled structurally for all 13, needs no variety
decomposition, unaffected by this negative. That separation is the session's point: the
expensive question turned out not to be the one that had to be answered.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-06 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress Update (PR #8240)
- **Status**: `in-progress` (awaiting Merge Manager merge of `litlfred/qou#8240` at `cb076a625e5995208490115a8926f02d958314a7`).
- **Lean Formalization**: `QOU.QBeta.AnglePolytopeFeasibilityAndClausenUnitCircleBrick.fkr_denominator_clearing_spurious_locus_split` (Torus saturation A_denom * u_sat = 1 eliminates the spurious denominator locus A_denom = 0 from the cleared FKR polynomial P_cleared = A_denom * Q_true.)
- **80-dps Witness**: `computations/probes/angle-polytope-feasibility-and-clausen-unit-circle-brick.witness.json` (`scriptHash: 2cbc25827af3`, `scriptCommitSha: ec2c1b177f9eff729f315a26ddbb5ea7edbf540d`).
