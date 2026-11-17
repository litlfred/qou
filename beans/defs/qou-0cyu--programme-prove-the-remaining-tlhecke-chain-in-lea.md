---
# qou-0cyu
title: 'PROGRAMME: prove the remaining TL/Hecke chain in Lean -- four Mathlib gaps, one Mathlib ASSET (Artin-Wedderburn exists)'
status: in-progress
type: epic
priority: normal
created_at: 2026-08-09T18:18:27Z
updated_at: 2026-11-17T08:12:13Z
parent: qou-rtxm
---


Branch: claude/anchor-followups-2026-08-08, after merging main (462 commits,
PR #4857's Hecke tower). Owner directive: "then prove all in lean. add mathlib
infra as needed. bean up."

This bean is the CATALOGUE. Each item says what is open, whether Mathlib helps,
and what it would actually cost. Children get their own beans as they start.

## THE ASSET NOBODY HAS USED -- Mathlib HAS Artin-Wedderburn

Mathlib/RingTheory/SimpleModule/WedderburnArtin.lean, at the pinned rev, provides

    exists_algEquiv_pi_matrix_divisionRing
    exists_algEquiv_pi_matrix_divisionRing_finite   [Module.Finite R_0 R]
    exists_ringEquiv_pi_matrix_divisionRing
    exists_algEquiv_matrix_divisionRing             (simple case)
    IsSimpleRing.tfae, isSimpleRing_isArtinianRing_iff
plus Mathlib/RingTheory/SimpleModule/Isotypic.lean for the isotypic pieces.

THIS IS THE EXISTENCE HALF of the Wedderburn decomposition, and it is sitting
unused. QOU.Hecke.Wedderburn's class has NO INSTANCE (qou-luq7); the finite
version above is exactly the shape needed to build one for H_n(q) over a field,
given finite-dimensionality -- which PR #4857 already proved as
IsHeckeOfFullRank (finrank = n!). The two halves have never been put together.

HIGHEST-LEVERAGE ITEM IN THIS BEAN. It converts ten modules from
"conditional on an uninhabited class" to "conditional on nothing".

## GENUINE MATHLIB GAPS -- confirmed absent at the pinned rev

Searched Mathlib for qInt / quantumInteger / TemperleyLieb / HeckeAlgebra: the
only hit is an unrelated MeasureTheory file. So ALL of the following are real
gaps, not lookup failures:

  G1. q-INTEGERS. No [m]_q, no q-factorial, no q-binomials as a developed API.
      This repo has scattered private defs (QOU.MathlibExt.QGaussianBinomialPascal,
      wedderburn_trace_identity.qInt, my TemperleyLiebTower.qint). Consolidating
      them into one Mathlib-shaped API is a prerequisite for G2 and would retire
      several duplicates. MEDIUM cost, HIGH cleanup value.
  G2. THE q-CLEBSCH-GORDAN NORMALISATION. [2]_q^n = sum_k m_k [n-2k+1]_q with
      m_k = C(n,k) - C(n,k-1) -- the q-dimension of V^(x)n for the 2-dimensional
      V. Proved here at n = 3 and n = 4 as ring identities
      (qdim_normalisation_three / _four); the general n is open. Induction on the
      three-term recursion qint_three_term, which is already proved. MEDIUM.
  G3. TEMPERLEY-LIEB ALGEBRA. Not in Mathlib at all. Needed to state
      H_n/rad = TL_n as an isomorphism rather than as a dimension count. LARGE.
  G4. CONNES SPECTRAL DISTANCE / RIEFFEL LIP-NORMS / compact quantum metric
      spaces. Not in Mathlib. Needed to state the metric results as anything
      more than the seminorm lemmas already proved
      (lip_kernel_forces_unbounded). LARGE, and arguably a research project
      rather than a formalisation task.

## THE ONE I MIS-PRICED, and the reason is worth recording

  G5. sum_k (C(n,k) - C(n,k-1))^2 = catalan n.
      I listed this in qou-u2jg as "pure combinatorics, no q" -- as though it
      were the EASY one. It is not. By RSK it says: pairs of same-shape standard
      Young tableaux with at most two rows are counted by Catalan(n), i.e.
      321-AVOIDING PERMUTATIONS ARE CATALAN. Mathlib has `catalan` but no RSK,
      no ballot numbers, and no pattern-avoidance theory.
      Two routes: (a) formalise enough RSK -- LARGE; (b) a direct induction on
      the ballot recursion, avoiding RSK entirely -- plausibly MEDIUM and worth
      trying FIRST. Verified numerically at n = 3,4,5: 1+4 = 5, 1+9+4 = 14,
      1+16+25 = 42.

## WHAT IS ALREADY PROVED, so nobody re-does it

  TemperleyLiebTower: qint_three_term_pair, markov_branching_general,
    qdim_normalisation_three/_four, branch_four_to_three_sym/_mixed,
    catalan_three/four/five, counts_are_catalan (vs Mathlib's own `catalan`),
    y_antisym_eliminated, y_antisym_factorisation, singlet_branch_pair,
    conventionD_kills_antisymmetriser, antisym_vanishes_only_at_two_roots,
    z_eq_q_forces_trivial, conventionD_unique_nontrivial (the IFF),
    not_conventionD_of_antisym_survives, y_mixed/sym_conventionD,
    IsConventionD, loop_reciprocal (q - z = 1/[2]_q, i.e. D IS the normalised
    TL trace at delta = [2]_q), qint/yw + qint_pos/yw_pos/yw_nonneg,
    qint_three_term, yw_branching, mul_div_pow_succ,
    traceRadical_* (two-sided ideal; star radical = bilinear radical),
    vanishing_step/_dom, vanishing_all_levels/_dom, dominates_of_branching,
    terms_zero_of_sum_zero, terms_zero_of_weighted_sum_zero
  WedderburnTraceDecomposition: trace_eq_sum_blocks,
    trace_decomposition_of_blocks, trace_eq_sum_weighted_characters
  YoungDiagramThreeRowCorner: isCorner_rowEnd, isCorner_lastRow,
    exists_threeRow_corner, youngPred, threeRow_vanishing_all_levels,
    card_three_threeRow_unique, threeRow_size_three_subsingleton,
    threeRow_vanishing_of_pinning

## ORDER I RECOMMEND

  1. THE WEDDERBURN INSTANCE from Mathlib's Artin-Wedderburn + IsHeckeOfFullRank.
     Highest leverage, uses an existing asset, and unblocks ten modules.
     Coordinate first -- QOU/Hecke/** is the sibling's territory
     (docs/coordination/hecke-tower-and-trace-parameter.md).
  2. G1 q-integer API, then G2 -- G2 is nearly free once G1 exists and the
     recursion is already proved.
  3. G5 route (b), the direct induction. Abandon to route (a) only if (b) fails.
  4. G3 and G4 are large enough to need their own decision, not a default yes.

## DISCIPLINE

AGENTS.md:779 -- Lean structure FIRST for any new derivation, before Python or
prose. Every item above is already a statement, so that is satisfied; keep it
that way for children of this bean.

## UPDATE -- G1 STARTED, and G2's proof is now fully worked out on paper

QOU/Mathlib/BallotNumbers.lean (NEW, sorry-free, imported from QOU.lean).
ballot_succ_succ needs only [propext, Quot.sound]; ballot_one only [propext].

    ballot n j = C(n,j) - C(n,j-1)                    (valued in Z)
    ballot_succ_succ    m_{j+1}(n+1) = m_{j+1}(n) + m_j(n)     THE ENGINE
    ballot_boundary_zero  m_{j+1}(2j+1) = 0                    THE CRUX
    ballot_one, ballot_values_{three,four,five}
    ballot_sq_sum_catalan_small   G5 at n = 3,4,5 vs Mathlib's own `catalan`

## THE FULL G2 PROOF, worked out -- write it up next, do not re-derive it

TARGET   [2]_q^n = sum_{j=0}^{floor(n/2)} m_j(n) * [n - 2j + 1]_q

STEP. Multiply the n-case by [2] and apply qint_three_term
([m+2] + [m] = [2][m+1], already proved in TemperleyLiebTower):

    [2]^{n+1} = sum_j m_j(n) ([n-2j+2] + [n-2j])

Reindex the second half by j' = j+1, using [n-2j] = [(n+1) - 2(j+1) + 1]:

    = sum_j ( m_j(n) + m_{j-1}(n) ) [n-2j+2]        over j = 0 .. M+1, M = floor(n/2)
    = sum_j m_j(n+1) [n-2j+2]                       by ballot_succ_succ

RANGE, and this is the ONLY subtle part:
  * n ODD  -> floor((n+1)/2) = M+1. The derived range matches exactly. Done.
  * n EVEN, n = 2m -> floor((n+1)/2) = m = M, but the derived sum runs to M+1.
    The surplus term sits at j = m+1 with coefficient m_{m+1}(2m+1), which is
    ZERO by ballot_boundary_zero. So it drops and the sums coincide.

So the parity split is REAL -- not an artefact of a clumsy index choice -- and
ballot_boundary_zero is exactly what resolves it. Both halves of the machinery
now exist; what remains is Finset bookkeeping over Finset.range (n/2 + 1), which
is fiddly but has no further mathematical content.

Base case n = 0: [2]^0 = 1 = m_0(0) * [1] = 1 * 1.

## WHY I DID NOT JUST FINISH IT

Honest reason: the remaining work is Finset range manipulation with a parity
case split, which is a real chunk of Lean and I would rather land the two
mathematical lemmas verified than a half-finished induction. The pieces are
proved; the assembly is mechanical and specified above.

## STILL OPEN, unchanged in priority

  1. The WEDDERBURN INSTANCE from Mathlib's Artin-Wedderburn. Still the highest
     leverage item in this bean, and untouched. QOU/Hecke/** territory.
  2. G2 assembly, per the recipe above.
  3. G5 general -- route (b), direct induction on ballot_succ_succ, avoiding
     RSK. ballot_boundary_zero will very likely be needed there too.
  4. G3 (Temperley-Lieb) and G4 (Connes/Rieffel) still need their own decision.


## CORRECTION -- I OVER-PROMISED THE WEDDERBURN ITEM. Read this before starting it.

I listed "the Wedderburn instance from Mathlib's Artin-Wedderburn" as HIGHEST
LEVERAGE and implied it could be assembled from existing pieces. I have now
checked, and that was wrong in the way that matters.

WHAT I GOT RIGHT. Mathlib does have Artin-Wedderburn, and this tree already has
two Mathlib-gap fills around it that I had not noticed:

    QOU/MathlibExt/MatrixSemisimple.lean   isSemisimpleRing_of_nonempty --
      matrix rings over a division ring are semisimple. Fills Mathlib's own
      `proof_wanted IsSemisimpleRing.matrix`. Bean qou-5mrn.
    QOU/MathlibExt/EndSemisimple.lean      isSemisimpleRing_end -- endomorphism
      rings of finite-dimensional vector spaces are semisimple. Fills Mathlib's
      `proof_wanted IsSemisimpleRing.module_end`. Bean qou-ciun / epic qou-otbb.

WHAT I GOT WRONG, and it is the blocker. EVERY Mathlib Wedderburn theorem --
exists_algEquiv_pi_matrix_divisionRing, ..._finite, exists_ringEquiv_pi_matrix_*,
all of them -- is stated under `variable (R) [IsSemisimpleRing R]`. Mathlib gives
the STRUCTURE theorem; the SEMISIMPLICITY HYPOTHESIS is the hard part, and for
H_n(q) it is the Tits deformation / Gyoja-Uno argument. It is not in Mathlib and
it is not in this tree (grep for IsSemisimpleRing in QOU/ returns only the two
MathlibExt files above and a comment). So there is no assembly; there is a
research-grade prerequisite.

AND A PHANTOM I PROPAGATED. Commit 47c4199bd's message says "the tree already
had H3A/H4A and their Wedderburn isomorphisms". It does NOT. That commit touched
only FullRank.lean, InstanceH3.lean and InstanceH4.lean -- rank and dimension --
and grepping InstanceOnH3A/InstanceOnH4A for AlgEquiv or RingEquiv returns
NOTHING. There is no concrete algebra isomorphism to a product of matrix
algebras anywhere for H3A or H4A.

I repeated that claim to the sibling as Ask 2 on litlfred/qou#4857 ("if that
isomorphism is a usable Lean equiv, finrank = 24 follows directly"). I hedged it
there -- "not asserted, the equiv has not been read closely from this side" --
and the hedge was correct. Now it is settled: the equiv does not exist. If
anyone acts on that ask, they will be chasing something that is not there.

## THE ROUTE THAT WOULD ACTUALLY WORK, at low n only

Semisimplicity transfers along a ring equivalence, and a finite product of
matrix algebras over a field is semisimple (MatrixSemisimple gives the factor
case). So at n = 3 and n = 4 specifically:

  1. CONSTRUCT the concrete AlgEquiv H3A = M_1 x M_2 x M_1 (and H4A = M_1 x M_3
     x M_2 x M_3 x M_1, or its TL quotient M_1 x M_3 x M_2). This is the real
     work, and it does not exist yet.
  2. Semisimplicity then FOLLOWS -- no Tits deformation needed at fixed n.
  3. Mathlib's Wedderburn then applies, and the central idempotents pi_lambda
     can be read off the product decomposition.
  4. y_lambda and the block scaling still need the Markov trace's own structure;
     see qou-luq7, where the block scaling is identified as the axiom the class
     SHOULD have carried.

REVISED PRIORITY. This is no longer the cheapest item in this bean -- step 1 is
a substantial explicit construction. G2 (recipe fully specified above, both
ingredients proved) is now the cheapest real progress. Do G2 first.


## G2: THE STATEMENT IS NOW VERIFIED CORRECT BEFORE PROVING IT

Formulating a general theorem and then discovering mid-proof that it is subtly
false is the expensive failure here, so I checked first, at 40 dps, n = 0..12:

    [2]_q^n  =  sum_{j in Finset.range (n+1)} ballot n j * qint q (n + 1 - 2*j)

with NATURAL SUBTRACTION semantics on the index (clamp to 0) and qint q 0 = 0.
Residual is pure round-off throughout -- 0.0 at n = 0 rising to 4.7e-37 at
n = 12, tracking the magnitude of [2]^12 = 4371.97, not a defect.

Also swept for counterexamples to the two ingredients over the same range:
ballot_succ_succ for all n <= 12 and all j, and ballot_boundary_zero for
j <= 7. NONE.

So the exact Lean statement to prove is:

    theorem qdim_normalisation (q : R) (hq : q != 0) (h1 : q - q⁻¹ != 0) (n : N) :
        (q + q⁻¹) ^ n
          = sum j in Finset.range (n + 1),
              ((ballot n j : Z) : R) * qint q (n + 1 - 2 * j)

Base case n = 0: range 1, ballot 0 0 = 1, qint q 1 = 1 (needs h1).

Induction step, in the order the Finset lemmas want it:
  1. pow_succ, then ih, then Finset.mul_sum -- pushes (q + q⁻¹) inside.
  2. Per term: for 2j <= n the index is (n - 2j) + 1, so qint_three_term
     rewrites (q+q⁻¹) * qint(n+1-2j) = qint(n+3-2j) + qint(n-1-2j)... CAREFUL,
     write it as m = n - 2j and use qint(m+2) + qint(m) = (q+q⁻¹) qint(m+1).
     For 2j > n the factor qint(n+1-2j) is qint 0 = 0 and the term dies.
  3. Split the sum in two; reindex the lower half by j -> j+1
     (Finset.sum_range_succ' is the lemma that shifts the base, not the top).
  4. Recombine with ballot_succ_succ; the j = 0 term uses ballot_zero on both
     sides. The surplus top term is killed by ballot_boundary_zero (even n) or
     is absent (odd n) -- and with the natural-subtraction form it is killed by
     qint 0 = 0 as well, so the parity split may not even be needed. TRY WITHOUT
     IT FIRST.

That last remark is the payoff of the natural-subtraction trick and is worth
testing before writing any parity case analysis.


## 2026-08-24 — the highest-leverage item is now unobstructed

This bean's headline item is wiring Mathlib's Artin–Wedderburn into an instance
of the Wedderburn class. Measured today, that was **blocked by the class
itself**, not merely unstarted: `QOU.Hecke.WedderburnDecomp` carried a
`trace_decomp` field which, together with the *derived* `trace_exhaustive` in
the same file, forced `(1 − y_μ) · tr_M(π_μ) = 0` for every block — so no
instance with the intended nontrivial `y_λ` could exist. Machine-checked in
`9e8b712fa2`; the field is replaced by an honest `block_scaling` hypothesis in
`722761c0eb`, and `trace_decomposition` is now derived.

Also worth correcting in this catalogue: it says *"`QOU.Hecke.Wedderburn`'s
class has NO INSTANCE (qou-luq7)"* — still true — but the reason given, that
"the two halves have never been put together", was not the whole story.

Unchanged: the four Mathlib gaps G1–G4 and the mis-priced G5.


## 2026-08-24 (later) — the two halves ARE now put together; three corrections

`QOU/MathlibExt/WedderburnIdempotents.lean` (PR #5717) joins them:
`exists_central_completeOrthogonalIdempotents` turns any Artin–Wedderburn
equivalence `A ≃ₐ M₁ × ⋯ × M_N` into the idempotent/orthogonal/central/complete
system `WedderburnDecomp` asks for. Only **centrality** is new — Mathlib's
`CompleteOrthogonalIdempotents.single` + `.map` already give the other three.

**The remaining gap is the INDEXING, not the construction.** `WedderburnDecomp`
indexes by `Partition n`; Artin–Wedderburn gives an index of unconstrained size.
That the blocks of `H_n(q)` are the partitions of `n` and there are no others is
Mathas §3.43 — not in Mathlib, not here. This bean should say that rather than
"the halves have never been put together".

### Corrections to this catalogue, measured

1. **"Mathlib HAS Artin-Wedderburn" — CORRECT.** `WedderburnArtin.lean` has
   zero `proof_wanted`. Verified rather than assumed, because:
2. **`IsSemisimpleRing.matrix` / `.module_end` ARE `proof_wanted`.** A grep for
   them finds statements that read like theorems. The discriminator is
   synthesis: `failed to synthesize IsSemisimpleRing (Matrix (Fin 3) (Fin 3) ℚ)`.
   The tree's `MathlibExt/MatrixSemisimple.lean` fills the division-ring case,
   sorry-free and axiom-clean — an upstream candidate this bean does not mention.
3. **The QOU semisimplicity modules are sorry-free.** `grep -c sorry` reports
   3/6/2/1 across `HeckeGenericSemisimple`, `MatrixSemisimple`,
   `TraceFormSemisimple`, `EndSemisimple`; every one of those twelve hits is the
   phrase **"sorry-free"**. Real count: **zero**. Do not use `grep -c sorry` on
   this tree.

Also measured: `H_2(q)` at `q > 1` is concretely semisimple
(`h2_isSemisimpleRing_of_one_lt`, axiom-clean), and its Wedderburn decomposition
is already explicit in `Machinery/HeckeH2Wedderburn.lean` — so the `n = 2`
specialisation of the new bridge is redundant and was dropped rather than landed.


## 2026-08-29 — Mathlib infra: three `proof_wanted`s closed

Owner directive *"build out mathlib infra"*. `RingTheory/SimpleModule` carries
**six** of Mathlib's 29 `proof_wanted`s. Three are now proved, sorry-free and
axiom-clean, each with an acceptance test that fails to synthesise without it:

| `proof_wanted` | closed by | PR |
|---|---|---|
| `IsSemisimpleRing.matrix` (general semisimple base) | `MathlibExt/MatrixSemisimpleGeneral.lean` | #6069 |
| `IsSemisimpleRing.module_end` (any finite semisimple module) | `MathlibExt/EndSemisimpleGeneral.lean` | #6070 |
| `isSemisimpleRing_iff_pi_matrix_divisionRing` (AW as an **iff**) | `MathlibExt/WedderburnArtinCharacterisation.lean` | #6072 |

**They are siblings, not a stack** — I expected the first to be load-bearing for
the other two and it is not. #6070 goes through Schur, which lands every block
on a division ring; #6072 needs only the converse over division rings. Both rest
on `MatrixSemisimple.instIsSemisimpleRing_matrix`, which predates this session.

New general lemma worth knowing about: `matrixPiRingEquiv`,
`Matrix m m (Π i, Sᵢ) ≃+* Π i, Matrix m m (Sᵢ)`. Mathlib has
`Matrix.compRingEquiv` for matrices *of* matrices but nothing for matrices over
a `Pi`.

### The trap in that lemma, recorded because it fails silently

`Matrix m m α` is a **type synonym** for `m → m → α`. A bare `fun a b => …`
therefore elaborates with the **Pi** multiplication *even under a
`: Matrix m m (S i)` ascription*; `Matrix.mul_apply` then cannot fire while
`Pi.mul_apply` can, rewriting the product pointwise to `M a b i * N a b i`. The
result is an unprovable goal, not a type error. `Matrix.of` pins the matrix
structure. Cost: three attempts.

### Still open in that file

`IsSemisimpleRing.mulOpposite` and the two
`LinearMap.isSemisimpleModule_of_{injective,surjective}`. Not scoped.

### Measurement correction affecting this whole catalogue

`QOU/Mathlib` is **169 files, 0 real `sorry`s, 2 real `axiom`s** (both in
`ParallelogramContour.lean`). A naive `grep -c sorry` reports **30** — every one
inside a comment, mostly the phrase *"sorry-free"*, once *"the only
sorry/instance the chain depends on"*. Tree-wide there are 22 real `axiom`
declarations. Use a comment-stripping scan, not `grep -c`.

Also measured: the RSK/Burnside keystone `Σ_{λ ⊢ n} (dim SYT λ)² = n!` is
**proved** (`QOU.Mathlib.rskBurnsideHolds`, epic `qou-nrex`) and is no longer an
axiom — so the partition-indexed dimension count this bean's `Partition n` gap
sits next to has landed since 2026-08-24.


## 2026-08-30 — all six `RingTheory/SimpleModule` `proof_wanted`s now have proofs here

Three more since the 2026-08-29 entry, completing the file's list:

| statement | file (`QOU/MathlibExt/`) | PR |
|---|---|---|
| `IsSemisimpleRing.matrix` | `MatrixSemisimpleGeneral.lean` | #6069 |
| `IsSemisimpleRing.module_end` | `EndSemisimpleGeneral.lean` | #6070 |
| `isSemisimpleRing_iff_pi_matrix_divisionRing` | `WedderburnArtinCharacterisation.lean` | #6072 |
| `IsSemisimpleRing.mulOpposite` | `MulOppositeSemisimple.lean` | #6079 |
| `…_of_injective` + `…_of_surjective` (semilinear) | `SemilinearSemisimple.lean` | #6081 |

All sorry-free, `[propext, Classical.choice, Quot.sound]`, each with an
acceptance test that fails to synthesise without it.

### 🛑 Read "closed" correctly — Mathlib is untouched

#6081's body claimed *"that file's `proof_wanted` list is now empty."* **Wrong,
and corrected on the PR.** Mathlib is a **vendored dependency**; all six
`proof_wanted` declarations are still in its `Basic.lean` (re-measured on `main`
after the merges). What exists is a **proof of each statement in this tree**.
They are *upstreamable*, not *upstreamed* — that needs PRs against
`leanprover-community/mathlib4`, which have not been made.

### The two TODOs Mathlib attaches to the semilinear pair are avoidable

Each of `…_of_injective` / `…_of_surjective` carries a TODO naming an API
generalisation — *"generalize `Submodule.equivMapOfInjective` from InvPair to
RingHomSurjective"*, *"generalize `LinearMap.quotKerEquivOfSurjective` to
SemilinearMaps"*. **Neither is needed.** Both assume the proof routes through a
semilinear *equivalence*, and `≃ₛₗ` is what forces `RingHomInvPair`. But
`isSemisimpleModule_iff_of_bijective` — sitting directly above them — takes a
bijective semilinear **map**. So: `l.rangeRestrict` for the injective case, and a
*complement* of `ker l` rather than the quotient for the surjective one.

I hit the `RingHomInvPair` wall first by trying the equivalence route, which is
what showed the way round it. Mid-scoping I also called the first TODO "stale"
because `equivMapOfInjective` is already semilinear-typed; that was wrong — it is
semilinear *and* needs an inv-pair.

**Both need `[RingHomSurjective σ]`, which neither `proof_wanted` states.** Looks
like an oversight: `LinearMap.range` and `Submodule.map` are only defined for a
semilinear map under it, and the sibling theorem above them carries it. An
upstreamer needs to know this before transcribing the statements.

### And they are siblings, not a stack

Four of the six rest on `MatrixSemisimple.instIsSemisimpleRing_matrix` (the
division-ring case, predating this work) rather than on each other. #6069's
general-base result is not load-bearing for any of the others.


---

## 2026-08-30 — Wedderburn leg: the class repair landed, the degeneracy did not

The `WedderburnDecomp` item in this catalogue is now measured rather than
estimated, and the answer is negative.

- **#5710 fixed the self-assuming field** (`trace_decomp` → `block_scaling`);
  `trace_decomposition` is derived. Real progress.
- **It did not make an instance meaningful.** `chi_lambda` had to enter as a
  second free field, so only the product `y_λ · χ^λ` is constrained.
  `yLambda_not_pinned` (PR #6097) realises every nonzero rational as the weight
  at every partition. Bean `qou-luq7` carries the full record.
- **The `Partition n` / Mathas §3.43 item is NOT blocked on a decision.** It is
  blocked on two concrete formalisations: computing `χ^λ` from a matrix
  representation, and tying `SpechtDimension.dim` to its partition. Mathlib's
  Artin–Wedderburn (the asset this bean opens with) gives neither — it produces
  an unindexed existential product of matrix rings, and the whole difficulty is
  the *indexing by partitions*.
- **Cost of my own #5710 blast-radius miss:** `WedderburnRankDegeneracy.lean`
  red on main for six days. Two verification traps recorded in
  `.claude/agent-memory/lean-verifier/verification-harness.md` — a green
  `lean`-direct run against a stale dependency olean is a FALSE GREEN, and a
  hypothesis-binder grep does not find an instance.
- **Unrelated red file found by the same cone check and fixed:**
  `QOU/Mass/QIntegerBarParity.lean`, red since `1646b5d6d3` behind one stale
  `open`. PR #6097.

## 🛑 G3's PREMISE IS REFUTED, two ways — 2026-09-26 (PR #7470)

G3 reads: *"TEMPERLEY-LIEB ALGEBRA. Not in Mathlib at all. Needed to state `H_n/rad = TL_n`
as an isomorphism rather than as a dimension count. LARGE."*

**(a) "Not in Mathlib at all" is true of Mathlib and false of here.** The corpus carries
`QOU/MathlibExt/TemperleyLiebAlgebra.lean` — a `RingQuot` with a universal property
(`lift` / `hom_ext` / `exists_unique_lift`) — plus `TemperleyLiebSpanning`,
`TemperleyLiebNormalForm` and `TemperleyLiebWedderburn`. G3's wording invites the reading
that the object does not exist anywhere.

**(b) The TL algebra object is NOT needed to get past a dimension count.**
`QOU/SchurWeyl/WtraceRadicalQuotient.traceQuotEquiv` (sorry-free, every `n`, convention D)
states the quotient as an **isomorphism of algebras**:

    TraceQuot (wtrace q hq0 hq2 n) (wtrace_cyclic …) ≃ₐ[ℝ] TwoRowBlocks n

i.e. `H_n(q)/rad(wtrace) ≅ ∏_{ℓ(λ) ≤ 2} M_{f^λ}(ℝ)` — the **Wedderburn form**. That is
strictly stronger than a dimension count and it uses no TL object at all. The TL algebra is
needed only for the literal `≅ TL_n(δ)` **spelling**.

**So the remaining gap is exactly one statement:** `∏_{ℓ(λ)≤2} M_{f^λ} ≅ TL_n(δ)` in
general. Proved at `n = 2, 3` only (`TemperleyLiebWedderburn.tl2AlgEquiv`, `tl3AlgEquiv`).
G3 should be re-scoped to that, and it is smaller than LARGE — the hard half (characterising
the quotient) is done.

**What was actually missing, for the record, and it was not the mathematics.** The pinned
Mathlib has **no first-isomorphism lemma for a `RingCon` quotient**:
`Mathlib/RingTheory/Congruence/` and `Mathlib/RingTheory/TwoSidedIdeal/` carry `ker`,
`mem_ker`, `ker_eq_bot` and no `lift`, no `quotientKerEquivOfSurjective`; `Con.lift` exists
for **monoid** congruences only. PR #7470 builds `liftAlgHom` for it, which is
general-purpose and needs only `[propext, Quot.sound]`.

**A separate defect found by hitting it, recorded not fixed:** there are **two** `Algebra ℝ`
instances on this quotient type — Mathlib's `RingCon.instAlgebraQuotient` and the corpus's
`QBeta.MarkovTraceQuotient.instAlgebraTraceQuot`. They do not unify, and spelling the type
`.ringCon.Quotient` does not select Mathlib's, because `instAlgebraTraceQuot` matches
whenever the ideal is a `traceRadicalIdeal`. Changing which one the corpus uses is a
behavioural change across every `quotMk` consumer, so it was left alone.

**Nothing else in G3's neighbourhood is false.** Both other artifacts recording an open
isomorphism are **accurate**: the content block `mass-theory/hecke-radical-is-temperley-lieb.md`
("no formalised statement of `H_n(q)/rad ≅ TL_n(q)` exists" — still true, the target is the
block product) and `MathlibExt/HeckeToTemperleyLieb.lean` §"What this file does NOT claim"
(its claim is about the **relator** ideal, untouched). They are *incomplete*, not wrong. Bean
stays open: G4 and the `≅ TL_n` half are open conjectures (rule 13a).



## 🛑 STALE PARAGRAPH, measured 2026-09-27 — this bean tells a reader the prerequisite does not exist, and it does

Found while extending PR #7470. **This bean stays open** (G3 is untouched, rule
13a); only the paragraph below is wrong.

The bean currently says, of Wedderburn/Artin-Wedderburn:

> the SEMISIMPLICITY HYPOTHESIS is the hard part, and for H_n(q) it is the Tits
> deformation / Gyoja-Uno argument. It is not in Mathlib and **it is not in this
> tree** (grep for IsSemisimpleRing in QOU/ returns only the two MathlibExt files
> above and a comment). So there is no assembly; there is a research-grade
> prerequisite.

Measured on the working tree (branch claude/tl-quotient-ringcon-lift-2026-09-26,
whose only Lean additions are in SchurWeyl/ and MathlibExt/RingConLiftAlgHom):

  grep -rl "IsSemisimpleRing\|IsSemisimpleModule" --include=*.lean QOU/ | wc -l
  => 39

not "the two MathlibExt files above and a comment". And the named prerequisite is
DISCHARGED at general n, sorry-free, with no cited class:

  QOU.SchurWeyl.isSemisimpleRing_hecke_generic
    (QOU/SchurWeyl/HeckeSemisimpleGeneral.lean:88)
    {K} [Field K] [CharZero K] (q : K) (hq0 : q != 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ)
      : IsSemisimpleRing (Hecke K q q⁻¹ n)

transported along `heckeWedderburn` (HeckeWedderburnGeneral.lean:112), the
general-n Wedderburn split of H_{n+1}(q) over ALL partitions. Landed via bean
qou-kwoa; file last touched 896f82118f (2026-09-03), i.e. AFTER this bean's last
update, which is how the paragraph went stale rather than having been wrong.

Also worth recording, because it changes what is cheap: Mathlib has
`RingHom.isSemisimpleRing_of_surjective` ("any quotient of a semisimple ring is
semisimple", RingTheory/SimpleModule/Basic.lean:433). So semisimplicity of
H_n(q)/rad(tr) for ANY cyclic trace follows from the above in two lines and needs
no Wedderburn decomposition of the quotient. Proved as
`WtraceRadicalSemisimple.isSemisimpleRing_traceQuot_of_hecke` on that branch,
under hq0 and hq2 only.

**What is NOT thereby done, so this bean's own items stand:** G3 (Temperley-Lieb
as an algebra object) is untouched; TL_n(delta) semisimple at general n is still
open on all six corpus-grep paths; and the ideal equality
<U_i U_j U_i - v^2 U_i> = rad(tr_M) is still the open item HeckeToTemperleyLieb
records. Semisimplicity of the HECKE algebra and of its quotient is not
semisimplicity of TL_n -- the two carriers are only known to agree once that
ideal equality lands.

G5 note for the reader: G5 closed in 2026-08-21 via bean qou-7wf6
(ballot_sq_sum_catalan, general n). The remaining gap in that direction is the
HOOK LENGTH FORMULA at general n, not the Catalan combinatorics -- see bean
qou-7vht, which measures it.



## Reorganisation 2026-10-04

Now the epic for P3.TL under Lean / Mathlib foundations.


## Round 57 Progress (lane-e667)
- **PR:** https://github.com/litlfred/qou/pull/8254 (`e9795825b5e02ba1c5315e9cbd5d10db4bc08957`)
- **Module:** `QOU.Foundations.OcneanuTowerConventionDRibbonClebschGordan` (`folio/quantum-observable-universe/lean/QOU/Foundations/OcneanuTowerConventionDRibbonClebschGordan.lean`), wired into `QOU.lean`.
- **Theorem:** `qDim_three_term_and_cube_decomp` — proves balanced quantum-integer three-term recurrence steps `[2]_q² = [3]_q + 1`, `[2]_q · [3]_q = [4]_q + [2]_q`, and the `n = 3` tensor decomposition `[2]_q³ = [4]_q + 2 · [2]_q`, with levels `n = 1..6` and Catalan ballot-square sums verified at 80 dps in `ocneanu-tower-convention-d-ribbon-clebsch-gordan.witness.json`.
- **Status:** Kept at `in-progress` pending Merge Manager merge and full dependency verification.
