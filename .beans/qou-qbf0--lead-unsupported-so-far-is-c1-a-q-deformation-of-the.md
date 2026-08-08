---
# qou-qbf0
title: 'LEAD (unsupported so far): is C1 a q-deformation of the polylog connection on P1 minus {0,1,inf}? The map is MISSING'
status: todo
type: task
priority: normal
created_at: 2026-08-08T10:55:00Z
updated_at: 2026-08-08T10:55:00Z
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
