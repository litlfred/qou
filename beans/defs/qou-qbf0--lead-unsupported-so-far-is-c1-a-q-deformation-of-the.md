---
# qou-qbf0
title: 'LEAD (unsupported so far): is C1 a q-deformation of the polylog connection on P1 minus {0,1,inf}? The map is MISSING'
status: in-progress
pr: 8195
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T10:55:00Z
updated_at: 2026-10-04T15:13:12Z
parent: qou-frzo
---

## Where the lead came from

C1's singular locus is `{0, [1], infinity}` on `E_q = C*/q^Z` (`qou-qbe9x`), where
`0` and `infinity` are the two FIXED POINTS of the dilation `x -> qx` and the third
site is the ORBIT OF THE IDENTITY. Owner asked whether that aligns with a corpus
`P^1` with three marked points.

**Corpus check (done, and it corrects the premise).** Bring's spacetime `P^1` does
NOT have three marked points: it carries **SIX** branch points (degree-4 covering
`pi: S -> P^1`, `R_tot = 14` by Riemann-Hurwitz), grouped in **three CONJUGATE
PAIRS** -- and it is the pairs that carry the three lepton generations
(`archimedean-yekutieli.md`). Counts: "six/6 branch points" 9 hits, "three branch
points" 0 hits. `|chi(A)| = 6` is load-bearing in `chi-minus-six-chain.md`.
**So the C1 triple does not align with Bring's spacetime.** Do not record that.

The corpus's ONLY `{0,1,infinity}` is Goncharov's motivic fundamental groupoid of
`P^1 \ {0,1,infinity}`, in `mass-theory/cl3-zeta5-geometric-realization.md` as
Candidate 3 for realising a depth-3 period. That is a better-targeted home for a
three-site configuration -- hence this lead.

## Status: PLAUSIBLE, NOT SUPPORTED

Owner uploaded the lit (commit 9a6d8f4b); all now registered in `references.ts`:

  brown-motivic-p1-three-points   Brown, "Motivic periods and P^1 minus 3 points"
  deligne-goncharov2005           "Groupes fondamentaux motiviques de Tate mixte"
  schlesinger2001                 "Some remarks on q-deformed multiple polylogarithms"
  zhao2008-mpl-roots-of-unity     MPL values at roots of unity
  zhao2010-standard-relations     Standard relations of MPL values at roots of unity

**Reading them does NOT close the lead**, and the reason is specific:

* The CLASSICAL side (Brown, Deligne-Goncharov) is `pi_1^mot(P^1 - {0,1,inf})`:
  iterated integrals of a KZ-TYPE CONNECTION whose singularities are exactly
  `0, 1, infinity`. That is the structure C1 would have to match.
* The Q-SIDE in hand (Schlesinger) defines q-deformed multiple polylogarithms as
  **q-SERIES**, e.g. `Li_{1,1}(z1,z2,q) = sum_{0<j<k} z1^j z2^k /((1-q^j)(1-q^k))`,
  and studies their algebra / Hopf structure and a link to a quantum
  Grothendieck-Teichmuller group. **It contains no q-difference module and no
  singular locus at all.**

So nothing in hand exhibits **a q-difference equation on `C*/q^Z` (or `P^1`) whose
solutions are q-polylogarithms and whose singularities sit at `0, [1], infinity`**.
That object is precisely the missing map. Without it the "match" is three sites
against three sites -- and even that is weak, because **two of C1's three sites
(`0`, `infinity`) are FORCED by the dilation symmetry** and carry no information.
Only the third site is a real datum.

## What would actually settle it

1. **Find or construct the q-KZ / q-difference connection whose horizontal
   sections are q-polylogs.** The natural candidate name is the q-KZ equation
   (Frenkel-Reshetikhin). NOTE: a corpus grep for `qKZ` returns only binary pack
   files and one patch -- **there is no qKZ content in the corpus**. If that
   equation is the bridge, it has to be brought in.
2. **Compare singular loci and local exponents**, not counts. C1 at `0` is
   Fuchsian; at `infinity` irregular of slope 1/2; at `[1]` the leading coefficient
   has a simple zero (genuine, `qou-qbe9x`). A KZ-type connection on
   `P^1 - {0,1,inf}` is regular-singular at ALL THREE points. **C1's slope-1/2
   irregularity at infinity is already a structural MISMATCH with a
   regular-singular KZ picture** -- this should be checked first, because it is
   cheap and it may kill the lead outright.
3. Only if (2) survives: look for a morphism `E_q -> P^1 - {0,1,inf}`.

## Discipline

Item 2 is the formalize-first prune for this lead: an irregular singularity cannot
be matched to a regular-singular one, so if C1's slope-1/2 at infinity is genuine
(it is -- proved this session) then any claimed identification with a KZ-type
connection must explain it. Run that BEFORE chasing q-KZ literature. Do not record
the three-site coincidence as evidence in any durable artifact.

**Lit ask if pursued:** a source giving a q-difference/q-KZ equation with
q-polylogarithm solutions and an explicit singular locus. Not among the seven
uploaded.

## PRUNE RUN 2026-08-08 — the KZ identification FAILS, on two independent tests

**Test 1 — local types.** A KZ-type connection on `P^1 - {0,1,inf}` is
REGULAR-SINGULAR at all three points (every Newton slope 0). C1:

    x = 0        all ord_0 a_i = 0   -> slope 0    -> Fuchsian    MATCHES
    x = [1]      simple zero of a_2                -> genuine site (qou-qbe9x)
    x = infinity single edge slope 1/2 -> IRREGULAR              MISMATCH

**Test 2 — the classical limit (the sharper one).** Irregularity at finite `q` is
not by itself fatal: a q-deformation may confluence to a regular-singular ODE. So
does C1 have a finite rank-2 limit as `q -> 1`?

    a_1 = a_0 = -(q-1) -> 0,   while  a_2 = q^2 x - 1 -> x - 1 != 0

so `L1 -> (x-1) sigma^2`, and `(x-1) y(q^2 x) = 0` is **not rank 2** -- the limit
is DEGENERATE. Rescaling does not save it: `L1/(q-1)` has leading coefficient
`(q^2 x - 1)/(q-1) -> infinity` for `x != 1` (checked at eps = 1e-1 ... 1e-6:
26.3, 206.0, 2006.0, 2000006.0 -- diverging as 2/eps).

**Verdict, scope-(a):** C1 is not a q-deformation of the KZ/polylog connection on
`P^1 - {0,1,inf}` in the naive sense. It is irregular where that picture is
regular-singular, and it has no finite rank-2 classical limit to confluence to.
The three-site coincidence is not evidence, and this bean should not be cited as
support for one. What is NOT excluded: some non-naive correspondence at the level
of periods/values rather than connections -- but no one should chase that without
a concrete map.

## The right tool is ALIEN CALCULUS — and it dodges the obstruction that killed RSZ

Owner asked. **Corpus first:** resurgence is not new here -- 239 files mention it,
27 alien derivations, 25 the bridge equation, 95 Ecalle. Per
`docs/audits/2026-08-01-uq0-map-resurgence-surreal-tool-assessment.md` §2, the
alien-calculus attack **already exists**: `OneInstantonNormalization.lean`
(PR #4246) + `2026-07-25-aomega-one-instanton-magnitude-probe.md` -- structurally
done, quantitatively open. That audit also maps `C1` into the same single open
object as every other angle (the Q_beta Habiro element / resurgent trans-series
normalisation).

**Why this matters for the present thread.** The RSZ route died because
`F(P1,...,Pk)` is built on the SLOPE FILTRATION and needs `k >= 2` distinct slopes
(`qou-qbp5`); C1 has one. **Alien calculus has no such requirement.** Alien
derivations `Delta_omega` act on the resurgent function itself and measure
singularities in the Borel plane; they do not need a two-slope filtration, and
they are the natural home for exactly the irregular, q-Gevrey-divergent object
that `deg_q(c_n) = n^2` (proved this session) certifies C1 to be.

So the correct statement is not "RSZ almost worked" but: **RSZ was never the right
tool for a pure-isoclinic point, and the tool the corpus already uses -- alien
calculus -- is.** That reframes S3 (`qou-qbs4`) away from "extract U in C^2 via
Birkhoff-Guenther" and toward the existing one-instanton/alien route.

**Open caveat, honestly:** classical alien calculus is well developed; the
q-analogue is less standard, and Test 2 shows we cannot confluence C1 to the
classical setting and apply Ecalle there. Whatever is used must be q-native.

## Also noted

Owner identified `library/ant-v14-n7-s/ant-v14-n7-s.pdf` as ANT **13**:7 and pointed at its TOC:
the relevant article is **Jarossay, "Pro-unipotent harmonic actions and dynamical
properties of p-adic cyclotomic multiple zeta values"** (p. 1711) -- the p-adic
cyclotomic-MZV side of the same `{0,1,inf}` story. Not yet read; noted for whoever
picks up the periods/values angle left open above.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-08 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress (PR #8195)
- [x] Formalized in `folio/quantum-observable-universe/lean/QOU/MassTheory/C1SingularLocusAndSlopeLevelBridge.lean` (`0` `sorry`, `0` `axiom`, `0 CRITICAL, 0 advisory` across all 7 static vacuity/borrowed-name audits) and wired into `QOU.lean`.
- [x] Verified exact rational witness in `computations/probes/c1-singular-locus-and-slope-level-bridge.witness.json` (`scriptHash: fc315c730706`, `scriptCommitSha: 17c1b41227b6c499979110fb6c31637514935ccf`, `allPassed: true`, `0` raw `float64` fields).
- [ ] Awaiting Merge Manager merge of PR #8195 (`4d59250dbada4070a6545f88b8d6f14fb94d89f6`).
