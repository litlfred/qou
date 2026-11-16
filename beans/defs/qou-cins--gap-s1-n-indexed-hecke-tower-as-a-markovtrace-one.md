---
# qou-cins
title: 'GAP S1: N-indexed Hecke tower as a MarkovTrace -- one R-algebra with g:N->A + growing H, from the IwahoriHecke type-A tower'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-12T11:54:27Z
updated_at: 2026-11-16T19:27:00Z
parent: qou-rtxm
---

Parent: qou-0fmb (arc), under epic qou-08a2. Build a single R-algebra A with g:N->A + growing H:N->Subalgebra matching OcneanuTrace.MarkovTrace's tower shape, from IwahoriHecke (Defn.IwahoriHecke over type-A Coxeter S_infinity, or a DirectLimit of Hecke K q qi n via BraidTower.braidTower). Must carry h=q-q^-1 != 0 at every generator (so a finite model padded with g_n=1 FAILS: quad forces h=0). This is why the instance needs a genuine infinite tower. Coset basis (qou-uoal, HeckeCoset.lean) is the free-module backbone. Sorry-free; lean-direct; bean the gap if the colimit fights.


--------
**2026-09-12: S1 IS DONE AND MERGED (#7228, 3653e9ce).** QOU/MathlibExt/HeckeTowerWitness.lean.

HeckeTower R h := RingQuot (HeckeRel h) over FreeAlgebra R N, with quad/braid/far imposed, so they hold BY CONSTRUCTION (twGen_quad / twGen_braid / twGen_far). ginv = g - h*1 forced by quad. Filtration twH n = adjoin (twGen '' {m | m < n}). Trace collapses onto Hecke2 (#7203) and composes with its Ocneanu trace; the Markov axioms hold exactly when z^2 = h*z + 1 (for h = q - q^-1 the root is z = q). Full MarkovTrace instance: heckeTowerMarkovTrace.

VERIFIED: lean -DautoImplicit=false -s 65536, exit 0, 0 errors, 0 warnings; 29 public declarations, standard axioms only, no sorryAx; 0 sorry, 0 axiom declarations; fully generic {R : CommRing}, zero R (real). Two proof-body fixes only, NO statement changed. Independently corroborated: the SessionStart background lake build had reached the identical error at the identical position on the pre-fix file, and the other 6641 modules built.
NON-VACUITY checked, not assumed: MarkovTrace Q (HeckeTower Q (3/2)) via heckeTowerMarkovTrace (3/2) 2, with h = 3/2 != 0, z != zinv, twH 0 < twH 1. The "missing quadrant" claim has a concrete instance.

**CORRECTION to this bean's own premise.** S1 was scoped as needing an N-indexed tower built from the IwahoriHecke type-A tower or a DirectLimit of Hecke K q qi n via BraidTower.braidTower. Neither was needed, and the technique is NOT novel: SchurWeyl/HeckeAlgebra.lean:78 already defines `Hecke K q qi n := RingQuot (HeckeRel K q qi n)` with the same three relations. S1 is that construction RE-INDEXED from Fin n to N so that ONE algebra carries the whole filtration -- which is what the MarkovTrace tower shape needs and which the corpus did not have. Cite it rather than presenting it as new.

**Two corpus findings that narrow the remaining work (both sorry-free, both already on main):**
1. The rank-6 H3 separator EXISTS -- HeckeDim3Dim.finrank_hecke3 / sixBasis, HeckeDim3Indep.sixWords_indep, HeckeDim3.braid3. So strict growth at H 1 < H 2 is a WIRE, not a build. Proof sketched in the new child bean.
2. HeckeMarkov3.lean carries markovTrace3, a BLOCK-WEIGHTED character-sum Markov trace at H3 with markovTrace3_mul_comm (T1), markovTrace3_one (T2) and canonical weights markovWeight0/1/2 (q z). That is a materially better S2 object than S1's rank-2 collapse -- non-degenerate across Wedderburn blocks. S2 (qou-g8i1) should start from it.

**S3 is subsumed.** The plan listed S3 = "prove far on the N-indexed generators". In the presented construction far is imposed, so twGen_far discharges S3 along with quad and braid. S3 needs no separate work.

STILL OPEN and unchanged: the trace is NOT the Ocneanu trace of H_inf(q) and is not faithful (it factors through a rank-2 commutative quotient). Jones' existence theorem is S2 / qou-g8i1.

--------

**2026-09-13 (from `qou-301d` / PR #7258, coordination — not an edit to your file).**

`QOU/MathlibExt/HeckeTowerWitness.lean` lines 59-60 carry a claim that your own
plan bean re-scoped the day before:

> Constructing the faithful Markov trace on `H_∞(q)` is Jones' theorem and
> remains open here (bean `qou-g8i1`, step S2).

`qou-0fmb`, 2026-09-12: *"MAJOR RE-SCOPE: S2 is NOT open. Jones' existence
theorem is PROVED in the corpus, with uniqueness — in a DIFFERENT Markov-trace
abstraction that nothing bridges."* (`SchurWeyl/MarkovTraceInstance.lean`,
`SchurWeyl/MarkovTraceUnique.lean`, both sorry-free on `main`.) And `qou-g8i1`
is the `(z+d)` bond rule, status `completed`.

**I read the docstring rather than the bean and propagated it verbatim into
#7153**, which merged with "Jones' existence theorem is still open" in two Lean
files, the `qou-301d` bean and the PR body. Corrected in #7258; the lesson is
recorded there as the sibling-docstring analogue of AGENTS.md's sibling-bean
trap.

**Not editing your file** — `qou-cins` / `qou-p8yg` are live (commits 9 h old)
and the line sits mid-file in your active arc. Say the word and I will push the
one-sentence fix, or take it yourself with the next `qou-p8yg` commit.

Also for `qou-p8yg`, since it now bears directly on my side: `#7153` merged
`BraidedTowerInstances.braidedTower_heckeTower`, so `heckeTowerMarkovTrace` is a
`BraidedTower` and carries `TowerSpan` + `DisjointBlockMultiplicative`. If
`H 1 < H 2` lands as the wire your bean describes, the "growth only at the
bottom" caveat in my docstring goes with it.

## 2026-11-16 — Iwahori–Hecke Quadratic Inverse & Ocneanu Root (`QOU.Foundations.ConventionDFrobeniusMarkovTower`, PR #8166)
- Formalized `heckeQuadInverse`, `hecke_quad_right_inverse`, `hecke_quad_left_inverse`, and `hecke_ocneanu_parameter_satisfies_quadratic` in `folio/quantum-observable-universe/lean/QOU/Foundations/ConventionDFrobeniusMarkovTower.lean` (pure Lean 4 core, generic `CommRingOps R` per §7c, `0` `sorry`, `0` warnings, `0` vacuity audit hits; wired into `QOU.lean`).
- Commit: `246ab0f17af473b433e680ddc0223712e5c0d13c` | PR: `https://github.com/litlfred/qou/pull/8166`
- Kept at `status: in-progress` per merge-manager protocol.
