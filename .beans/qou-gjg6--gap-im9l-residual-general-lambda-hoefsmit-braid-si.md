---
# qou-gjg6
title: 'GAP (im9l residual): general-lambda Hoefsmit braid — size-6 S3-orbit Yang-Baxter identity'
status: in-progress
type: task
priority: normal
created_at: 2026-08-11T01:05:26Z
updated_at: 2026-08-16T14:03:02Z
parent: qou-59vq
---

## Residual after SW-4-gen scaffolding pass (2026-08-11)

`hoefsmit_seminormal_rep` in
`content/quantum-observable-universe/lean/QOU/SchurWeyl/HoefsmitRep.lean`
still carries ONE `-- Ref:`-cited `sorry` (the general `∀ λ ⊢ N` statement).
Everything else in the file is sorry-free (`#print axioms` →
`[propext, Classical.choice, Quot.sound]`, no `sorryAx`).

### What landed sorry-free this pass (reusable for the general build)
- `seminormalBlock q a` — the generic axial-distance 2×2 orbit block
  (top-right 1, trace q−q⁻¹, det −1, one free param `a`).
- `seminormalBlock_quadratic` — Hecke quadratic relation, ALL q≠0, ALL a.
- `seminormalBlock_ne_scalar` — non-degeneracy (off-diagonal 1≠0).
- `S1_eq_seminormalBlock` — `S1 q = seminormalBlock q (-1/(q³+q))`.
- `S1_ne_scalar`.
- `seminormalRep22 : Hecke ℝ q q⁻¹ 3 →ₐ[ℝ] M₂(ℝ)` (λ=(2,2), N=4) with
  σ0/σ1/σ2 lemmas + `seminormalRep22_nonScalar`. First 4-strand rep;
  first NON-VACUOUS far-commutation σ0σ2=σ2σ0. All relations reduce to
  the (2,1) lemmas `S0_quadratic`/`S1_quadratic`/`S0_S1_braid`.

### What remains open (the hard core)
1. Enumerate the `s_i`-orbits of `SYT λ` (Lean: SYT type is
   `QOU.Mathlib.StandardYoungTableau`; `dLambda`=Fintype.card). Each orbit
   has size 1 (entries i+1,i+2 same row → scalar q; same column → −q⁻¹) or
   size 2 (both s_i·T standard → a `seminormalBlock` with `a` the axial-
   distance rational function). Need a Lean map `Fin (dLambda λ) → SYT λ`
   and the orbit trichotomy as a decidable case split.
2. Assemble the block-diagonal generator matrix `ρ_λ(σ_i)` from the orbits.
3. **BRAID for arbitrary λ** — the Yang-Baxter / axial-distance identity
   across the S₃-orbit of three consecutive entries i,i+1,i+2. Orbit sizes
   1/2/3 reduce to the (2,1)/(2,2)-style 2×2 identities (already have the
   template `S0_S1_braid`); the GENERIC size-6 orbit is a real
   6-dimensional identity NOT reducible to 2×2 blocks. This is Hoefsmit's
   thesis theorem. Refs: [hoefsmit1974], [ram1997] (axial-distance formulas).

### Suggested next step
Formalize the size-6 braid as a standalone lemma over ℝ: given the three
axial distances of an S₃-orbit, the two 6×6 generator matrices (each two
`seminormalBlock`s + two scalars, in the seminormal basis ordering) satisfy
`ρ(σ_i)ρ(σ_{i+1})ρ(σ_i) = ρ(σ_{i+1})ρ(σ_i)ρ(σ_{i+1})`. If that single
`field_simp;ring` 6×6 identity closes, the general theorem is within reach
(the orbit bookkeeping is then plumbing). If it does NOT close as one ring
identity, that is the true blocker to report.

Env: lean-direct against main-repo oleans (worktree has none); NEVER
`lake build`. Restore recipe in AGENTS.md / lean-environment-setup.md.


## PROGRESS 2026-08-14 (PR #5020): step (i)/(ii) parameter IDENTIFIED and verified; step (iii) still open

New sorry-free file QOU/SchurWeyl/SeminormalParam.lean.

The axial-distance rational function the general construction needs is

    a(d) = (q - q^-1) / (1 - q^(-2d))          [seminormalParam]

This is ANCHORED, not asserted: S1 in HoefsmitRep.lean was built by hand to satisfy
the braid relation with S0, independently of any axial-distance formula, and its (0,0)
entry is -1/(q^3+q). In [[1,2],[3]] the entry 2 has content 1 and 3 has content -1, so
sigma_1 acts with axial distance d = -2, and a(-2) = (q-q^-1)/(1-q^4) = -1/(q^3+q).
Recorded as S1_eq_seminormalParam.

Consequences that simplify the remaining build:
- a(1) = q and a(-1) = -q^-1 (seminormalParam_one / _neg_one). So the SIZE-1 orbit
  eigenvalues are the SAME formula as the size-2 blocks. The orbit trichotomy of step (i)
  is a case split on the BLOCK SIZE only, not on the parameter — one formula throughout.
- a(d) + a(-d) = q - q^-1 (seminormalParam_add_neg), matching seminormalBlock's trace,
  so a size-2 orbit is exactly seminormalBlock q (a d) with lower-right entry a(-d) read
  from the partner tableau. Step (ii) assembly needs no extra choice.

CAVEAT worth carrying: q^2 != 1 is a REAL hypothesis, not cosmetic. At q = +-1 both
q - q^-1 and 1 - q^4 vanish, so a(-2) evaluates to 0 (Lean 0/0) while S1's entry is
-1/(2q) != 0. The Hecke algebra degenerates to the group algebra there and the seminormal
form is not given by this formula. Any general-lambda statement must carry it.

STILL OPEN (the hard core, unchanged): step (iii), the braid relation for arbitrary
lambda -- the generic size-6 S_3-orbit identity. The suggested probe is now UNBLOCKED:
with a(d) pinned, parametrise an S_3 orbit by the three cell contents c1,c2,c3, set
u = q^(-2(c2-c1)), v = q^(-2(c3-c2)); all six axial distances are +-(c2-c1), +-(c3-c2),
+-(c3-c1), so every entry is rational in (q,u,v) with denominators 1-u, 1-v, 1-uv and
their inverse partners. The 6x6 braid identity is then a rational-function identity in
three variables. Remaining design step before the probe: fix the basis ordering and the
two DIFFERENT pairings (sigma_i pairs the 6 tableaux one way, sigma_{i+1} another) -- that
is what makes it irreducible to 2x2 blocks, and getting it wrong makes the identity false
rather than hard, so it must be derived, not guessed.


## STEP (iii) CLOSED 2026-08-14 (PR #5020) — the size-6 orbit braid is PROVED

New sorry-free file QOU/SchurWeyl/Orbit6Braid.lean: genA_genB_braid proves
ABA = BAB on a generic size-6 S_3-orbit. Axiom-clean.

Two things made it tractable:

1. THE STATEMENT IS POLYNOMIAL, not rational. The three parameters a1 = a(p),
   a2 = a(r), a3 = a(p+r) are not independent; eliminating u,v gives ONE relation

       a3 * (a1 + a2 - c) = a1 * a2        (c = q - 1/q)

   and that relation is exactly what the braid needs. Verified sufficient (free
   random a1,a2,c) and necessary (perturbing a3 breaks it). So the theorem carries
   no q, no u/v, no integer distances. seminormalParam_mul_rel ties it back to the
   real seminormal parameters.

2. THE ORIENTATION CONVENTION IS A REAL CONSTRAINT, and it was identified by
   exhaustive exact-rational search over the four orientation combinations rather
   than guessed. Both-negative and both-positive HOLD; both mixed combinations FAIL
   (6/36 nonzero entries in ABA-BAB). Only the consistent case is formalised; the
   mixed negative is recorded in the docstring as numerical, not formal.

PERFORMANCE NOTE for anyone doing 6x6 matrix identities in Lean: do NOT define the
matrices as !![...] literals. simp must chase vecCons chains and the triple product
(1296 scalar terms) times out even at 2M heartbeats on a pure-ring goal. Defining
via Matrix.of fun i j => match (i:N),(j:N) with ... makes entry lookup a single iota
reduction: same theorem, 100 seconds.

STILL OPEN (what actually remains of gjg6): steps (i) and (ii) -- enumerate the
s_i-orbits of SYT lambda (Lean type QOU.Mathlib.StandardYoungTableau; need a map
Fin (dLambda lam) -> SYT lam and the orbit trichotomy as a decidable case split),
and assemble the block-diagonal generator matrices from the orbits. This is
bookkeeping over the tableau combinatorics, not new mathematics: the size-1 and
size-2 orbit blocks are seminormalBlock (already proved), the size-6 braid is now
proved, and the parameter is seminormalParam. hoefsmit_seminormal_rep is still a
Ref'd sorry until that plumbing lands.


## STEP (i) PARTIAL 2026-08-14 (PR #5020): entry->cell inverse + the two scalar cases

New sorry-free file QOU/SchurWeyl/TableauCells.lean, axiom-clean.

The StandardYoungTableau structure carries bijOn (the entry map is a bijection from
cells onto {1..|mu|}) but does not EXPOSE the inverse, and the whole construction needs
to go backwards: given entry k, which cell holds it. Now:

- cellOf T k  -- the cell holding entry k; total (off-range k |-> (0,0)) so no subtype
  bookkeeping leaks into the construction. With cellOf_spec, cellOf_mem, entry_cellOf
  (round trip on entries) and cellOf_unique (round trip on cells -- this is the one that
  lets you COMPUTE cellOf from an explicit tableau).
- axialDist T k = axialDistance (cellOf T k) (cellOf T (k+1)) -- the seminormalParam
  argument for the generator sigma_k.
- axialDist_of_sameRow = +1 and axialDist_of_sameCol = -1: the two SIZE-1 orbit cases.
  Composed with seminormalParam_one / _neg_one these are exactly the scalar eigenvalues
  q and -q^-1.

Worth noting where the content is: sameRow_adjacent / sameCol_adjacent prove that
CONSECUTIVE entries sharing a row (resp. column) sit in ADJACENT cells -- any cell
strictly between them would carry an entry strictly between two consecutive integers.
That is the step where standardness (bijection onto an interval) is used rather than
mere semistandardness, and it is why the distance is exactly +-1 and not merely signed.

STILL OPEN for step (i): the s_k action on tableaux (swap the entries k, k+1) plus the
proof that it lands back in SYT lambda exactly in the non-adjacent case -- i.e. the
size-2 orbit case, which is the remaining substance. Then step (ii), assembling the
block-diagonal generator from the orbits, and only then does hoefsmit_seminormal_rep
lose its Ref'd sorry.


## STEP (i) ESSENTIALLY DONE 2026-08-14 (PR #5020): the s_k action lands

TableauCells.lean extended, still sorry-free and axiom-clean:

- swapVal k -- the transposition of the VALUES k, k+1, an involution.
- SwapAdmissible T k -- cells of k and k+1 share neither row nor column. By
  sameRow_adjacent / sameCol_adjacent this is exactly the complement of the two
  size-1 cases, i.e. THE size-2 orbit condition.
- not_sameRow_of_admissible / not_sameCol_of_admissible -- the usable form.
- swapSsyt -- row_weak' and col_strict' survive the swap. Proof shape: the swap can
  only disturb order at the two swapped values, and the single bad configuration (k and
  k+1 in a common row/column) is exactly what admissibility rules out; feeding that
  negation to omega closes all split_ifs branches at once.
- bijOn_swapVal -- the value-swap is a bijection of {1..n} (involution + MapsTo, via
  Set.InvOn.bijOn), so the filling of the swapped tableau is still a bijection.
- swapTableau -- s_k . T as a StandardYoungTableau. THE SIZE-2 ORBIT PARTNER.
- swapTableau_involutive -- s_k applied twice is the identity.

CAVEAT recorded in the file: swapTableau_involutive takes admissibility of the SWAPPED
tableau as a hypothesis rather than deriving it from hadm. It is true (the swap exchanges
the two cells, so the condition is symmetric) but proving it needs cellOf of the swapped
tableau, which is not done. Anyone completing step (ii) should close that first -- it is
small and it removes a hypothesis from every downstream use.

Two Lean gotchas that cost time and will recur:
1. T.entry vs the SSYT coercion are defeq but NOT syntactically equal, so a `have :=`
   without a type ascription hands omega two different atoms. Always ascribe.
2. omega would not use a split_ifs branch hypothesis `0 = k` in the zeros' obligation;
   discharging the branch explicitly with if_neg was the fix.

STILL OPEN: step (ii) only -- assemble the block-diagonal generator matrix from the
orbits (map Fin (dLambda lam) -> SYT lam, the orbit trichotomy as a decidable case split,
and the block-diagonal assembly), then hoefsmit_seminormal_rep loses its Ref'd sorry.


## CAVEAT CLOSED 2026-08-15 (PR #5020): admissibility of the swapped tableau is DERIVED

The hypothesis flagged in the previous entry is gone. cellOf_swapTableau_self and
cellOf_swapTableau_succ compute cellOf of the swapped tableau (the swap exchanges the
cells of k and k+1, both by cellOf_unique), so swapAdmissible_swapTableau derives
admissibility of s_k.T from admissibility of T, and swapTableau_involutive now carries
NO side hypothesis. {T, s_k.T} is a two-element orbit outright.

STEP (i) IS NOW COMPLETE. Everything the block assembly needs about individual tableaux
is proved: cellOf + its round trips, axialDist, the two size-1 cases (+1 / -1 forcing
the scalars q and -q^-1), the size-2 orbit partner swapTableau, its involutivity, and
the derived symmetry of admissibility.

STILL OPEN: step (ii) ONLY -- an enumeration Fin (dLambda lam) -> SYT lam, the orbit
trichotomy as a decidable case split (same row / same column / admissible), and the
block-diagonal assembly of the generator matrix. Then hoefsmit_seminormal_rep loses its
Ref'd sorry. Note the assembly can now cite: seminormalParam for the entry values,
seminormalBlock for the size-2 blocks, axialDist_of_sameRow/_sameCol for the size-1
scalars, and Orbit6.genA_genB_braid for the braid relation on the generic orbit.


## STEP (ii) RE-SCOPED 2026-08-15 — it is NOT just bookkeeping (correcting my own earlier note)

Earlier entries in this bean called step (ii) "bookkeeping over tableau combinatorics,
not new mathematics". Having scoped it against the actual API, that is too optimistic and
is corrected here.

### What IS fully determined now (the generator matrix)

Pick e : SYT lam ~= Fin (dLambda lam) (Fintype.equivFin; noncomputable, arbitrary order --
the ordering does not matter, only the per-pair orientation does). Write a(d) =
seminormalParam q d and d_T = axialDist T k. Then rho_lam(sigma_k) has entries, in the
convention anchored by S1 and used in Orbit6Braid:

    M[T][T]   = a(d_T)                                  -- uniform; covers the scalar
                                                           cases too, since a(1) = q and
                                                           a(-1) = -q^-1
    M[s_k.T][T] = if d_T < 0 then 1 + a(d_T)*a(-d_T)    -- T is the "first" member
                  else 1
    M[T'][T]  = 0                                        for T' not in {T, s_k.T}

with s_k.T = swapTableau (defined only when SwapAdmissible; in the size-1 cases the row
is just the diagonal entry). Every ingredient of that formula is proved: seminormalParam
(+ its values at +-1), axialDist, axialDist_of_sameRow/_sameCol, swapTableau,
swapTableau_involutive, swapAdmissible_swapTableau.

### What is NOT bookkeeping (the honest blocker)

Proving the Hecke relations for that matrix at general lambda needs:

1. FAR COMMUTATION (|k-l| >= 2): that the s_k and s_l ACTIONS on tableaux commute, and
   that admissibility is preserved across them. Not proved; needs its own lemma.
2. BRAID: an orbit classification for <s_k, s_{k+1}> acting on SYT lam -- each orbit has
   size 1, 2, 3 or 6 -- AND, for each orbit, a basis correspondence identifying the
   restriction of rho with the proved matrices. Orbit6Braid proves the generic case in an
   EXPLICIT basis ordering (indices 0..5 with fixed pairings); matching an arbitrary orbit
   to it is the missing step, not a rewrite.
3. The size-3 orbit case is not covered by anything proved so far (sizes 1 and 2 are; 6 is).

So the remaining work is: an s_k action-commutes lemma, an orbit-size classification, a
per-orbit basis correspondence, and the size-3 case. That is a session or more of genuine
development, not assembly. Anyone picking this up should not expect the Orbit6Braid result
to drop straight in.


## STEP (ii) BLOCKER 1 of 4 CLOSED 2026-08-15: far commutation of the s_k actions

TableauCells.lean extended, sorry-free and axiom-clean:

- swapVal_comm -- disjoint value-transpositions {k,k+1} and {l,l+1} commute (|k-l| >= 2).
- cellOf_swapTableau_of_ne -- applying s_l does not move the cell of any entry outside
  {l, l+1}. This is the workhorse: it is why a far swap cannot disturb anything about k.
- swapAdmissible_of_far -- admissibility at k survives a far swap at l. DERIVED, so it is
  supplied automatically at the use site rather than being carried as a hypothesis.
- swapTableau_comm -- s_k s_l . T = s_l s_k . T for |k-l| >= 2. The tableau-level form of
  the generator relation sigma_k sigma_l = sigma_l sigma_k.

Remaining step-(ii) blockers, now 3 of 4:
2. orbit-size classification for <s_k, s_{k+1}> acting on SYT lam (sizes 1,2,3,6);
3. per-orbit basis correspondence matching Orbit6Braid's explicit index ordering;
4. the size-3 orbit case, which nothing proved so far covers.


## SIZE-3 ORBIT IDENTIFIED (numerical, NOT yet formalised) 2026-08-15

What a size-3 orbit IS: the standard fillings of a DOMINO + a disjoint cell. The domino's
two cells are adjacent, which forces their relative order, so the count is 3!/2! = 3.
(Sizes: 3 cells in a row or column -> 1; domino + disjoint cell -> 3; three mutually
non-adjacent cells -> 6.)

Concretely, with cells A, B adjacent (row-domino: content(B) = content(A)+1; column-domino:
content(A)-1) and C disjoint from both, the three fillings of {k,k+1,k+2} with
entry(A) < entry(B) are

  1: A=k,   B=k+1, C=k+2      2: A=k,   B=k+2, C=k+1      3: A=k+1, B=k+2, C=k

and the generators act as

  sigma_k    : fixes filling 1 with the SCALAR a(+-1)  (+1 row-domino -> q; -1 column-domino
               -> -q^-1); 2x2 block on {2,3}
  sigma_{k+1}: 2x2 block on {1,2}; fixes filling 3 with the same scalar

so each generator is (scalar) (+) (2x2 block) -- but on DIFFERENT summands, which is why
the orbit is 3-dimensional and irreducible to the 2x2 case, exactly as at size 6.

STATUS: exact-rational check over 8 random (q, contents) pairs, both row- and
column-dominoes: the Hecke quadratic relation holds for both generators and the BRAID
relation holds, under the same negative-distance-first orientation convention used in
Orbit6Braid. This is NUMERICAL EVIDENCE ONLY -- there is no Lean theorem for the size-3
orbit yet, and the corresponding blocker in the step-(ii) list stays OPEN.

Formalising it should follow Orbit6Braid exactly: 3x3 matrices via Matrix.of + match on
the index values (NOT !![...] literals), parameters as free reals subject to whatever
single relation the elimination gives, then ext + fin_cases + field_simp + ring. Expect
it to be cheaper than the 6x6.


## SIZE-3 ORBIT PROVED 2026-08-15 (branch orbit3-braid) — blocker 4 of 4 closed

Orbit3Braid.lean, sorry-free and axiom-clean: genA_genB_braid proves ABA = BAB on a
size-3 orbit (domino + disjoint cell), and genA_quadratic the Hecke relation.

TWO hypotheses, both necessary:
  hsc  : sc * sc = c * sc + 1      -- the SCALAR satisfies the Hecke quadratic, i.e. sc is
                                      a root of X^2 - cX - 1, so sc in {q, -1/q}
  hrel : a2 * (sc * (sc - a1)) = a1 -- the two block parameters are a(d) and a(d -+ 1) for
                                      the same axial distance; eliminating d leaves this

Finding worth recording: my first probe left c and sc INDEPENDENT and everything failed --
including the QUADRATIC, which is what exposed the omission. sc is not free: the scalar
block must itself satisfy sigma^2 = c sigma + 1. Once tied, 26/26 exact-rational cases hold
across both domino orientations, and the hrel form above is uniform in sc (the q-only form
a2*q*(q-a1) = a1 works for the row-domino but NOT the column one).

Lean note: the proof eliminates both c and a2 by substitution (c = (sc^2-1)/sc, a2 =
a1/(sc(sc-a1))) and closes with field_simp; ring. genA_quadratic needs the hypothesis
pre-normalised as sc^2 - c*sc - 1 = 0 -- linear_combination cannot serve both branches
because they need different multiples (1x and 2x), while linarith on the normalised form
handles the scaling.

STEP (ii) BLOCKERS REMAINING: 2 of 4 --
  2. orbit-size classification for <s_k, s_{k+1}> acting on SYT lam;
  3. per-orbit basis correspondence matching the explicit index orderings of
     Orbit3Braid / Orbit6Braid.
Every ORBIT-LOCAL identity is now proved: size 1 (scalars), size 2 (seminormalBlock),
size 3 (this file), size 6 (Orbit6Braid).


## SIZE-3 HYPOTHESES NOW DERIVED (same branch/PR #5062)

The two hypotheses of genA_genB_braid are no longer merely stated -- Orbit3Braid.lean now
discharges both for the actual seminormal parameters, the role seminormalParam_mul_rel
plays for Orbit6Braid:

  hsc_row / hsc_col   -- the scalars q and -q^-1 each satisfy sc^2 = c*sc + 1
  hrel_row / hrel_col -- with a1 = a(d) at x = q^-2d, a2 = a(d-1) at q^2 x (row-domino)
                         or a(d+1) at x/q^2 (column), the relation
                         a2 * sc * (sc - a1) = a1 holds identically

This is also the concrete reason genA_genB_braid is stated through sc rather than q: the
q-only form of the relation covers the row-domino only, and hrel_col is what shows the
sc-form is the right generalisation rather than a cosmetic rewrite.

So the size-3 orbit is now a statement about the Hoefsmit matrices end-to-end, not about
abstract 3x3 arrays.


## ORBIT TRICHOTOMY PROVED 2026-08-15 — the step-(ii) case split

TableauCells.lean gains axialDist_trichotomy (+ cellOf_ne), sorry-free and axiom-clean:
for consecutive entries k, k+1 in range,

    axialDist T k = 1  \/  axialDist T k = -1  \/  SwapAdmissible T k

i.e. the two cells share a row (size-1 orbit, scalar q), share a column (size-1, scalar
-q^-1), or share neither (size-2, a seminormalBlock). No fourth case and no overlap: the
cells are distinct because the entries are (cellOf_ne), so they cannot agree in BOTH
coordinates.

This is the decidable case split the generator assembly runs on, and it is the first
genuinely step-(ii) result rather than step-(i) infrastructure.

STEP (ii) REMAINING after this:
  - orbit-SIZE classification (this is the per-generator trichotomy, not yet the
    <s_k, s_{k+1}>-orbit sizes 1/2/3/6 -- those need both generators considered together);
  - per-orbit basis correspondence onto the explicit index orderings of Orbit3Braid /
    Orbit6Braid;
  - the block-diagonal assembly itself.


## THE QUADRATIC RELATION IS PROVED GLOBALLY 2026-08-15 (route (c))

SeminormalRep.lean now carries genMat_quadratic: for ARBITRARY shape mu and every
generator sigma_k,

    rho(sigma_k)^2 = (q - q^-1) * rho(sigma_k) + 1

on all of SYT mu at once. Sorry-free, axiom-clean. This is the first Hecke relation
established for the general-lambda representation rather than one orbit at a time.

WHY ROUTE (c) MADE IT POSSIBLE. The matrix is indexed by StandardYoungTableau mu on BOTH
sides, so there is no per-orbit basis correspondence to build -- blocker 3 of the step-(ii)
list is bypassed for this relation, not solved. The proof never constructs a block
decomposition; it reads one off the entry rules, column by column.

THE TWO NEW FACTS IT RESTS ON (both were missing, both now in TableauCells):
- axialDist_ne_zero -- consecutive entries never share a diagonal. If they did, the cell
  completing their rectangle would lie in mu by up-left closure and would carry an entry
  strictly between k and k+1. NOTE the trichotomy does NOT give this: SwapAdmissible only
  says the cells differ in both coordinates, not that their CONTENTS differ. Without it
  seminormalParam sits on its pole at d = 0.
- axialDist_swapTableau -- the swap negates the distance, so {T, s_k.T} carries d and -d.
  That is what makes the pair's diagonal sum to q - q^-1 via seminormalParam_add_neg.
Plus axialDistance_antisymm (added next to the definition in HoefsmitRep), zpow_ne_one
(a real q > 0, q != 1 is not a root of unity -- the archimedean half of axialDist_ne_zero)
and swapTableau_ne.

THE SHAPE OF THE ARGUMENT: sum_mul_genMat_column shows column T has support in
{T, s_k.T} and nothing else, so (M^2) restricted to that column is a 2x2 Cayley-Hamilton:
trace a(d) + a(-d) = q - q^-1, determinant a(d)a(-d) - (1 + a(d)a(-d)) = -1 by
offDiag_mul_neg (whichever of the two off-diagonal entries carries the factor, the product
is the same). On the fixed columns the trichotomy gives d = +-1, where seminormalParam
evaluates to q resp. -q^-1 -- the two roots of X^2 - (q - q^-1)X - 1.

WHY THIS DOES NOT CLOSE gjg6, stated plainly: the quadratic is COLUMN-LOCAL. Each column
sees at most two tableaux, so the relation never leaves a 2x2. The braid is NOT
column-local -- it mixes sigma_k and sigma_{k+1}, whose supports differ, and that
difference is exactly the content of Orbit3Braid / Orbit6Braid. Far commutation is
likewise still open (swapTableau_comm gives it at the level of TABLEAUX; lifting that to
the matrices is not done). hoefsmit_seminormal_rep keeps its Ref'd sorry.

STEP (ii) REMAINING: far commutation of the matrices; the <s_k, s_{k+1}>-orbit size
classification; the braid relation globally (or, failing that, the per-orbit basis
correspondence after all). Anyone continuing should try far commutation next -- like the
quadratic it is likely column-local, since a far swap moves no cell the other generator
looks at (cellOf_swapTableau_of_ne).

---

## 2026-08-16 — TAKEOVER of the branch backing PR #5076 (stalled-claim protocol)

Owner instruction: *"take over 5076"*.

**Staleness confirmed** per AGENTS.md §2 stalled-claim takeover:

| check | value |
|---|---|
| branch | `claude/seminormal-quadratic-2026-08-15` |
| last commit SHA | `3a50fd4e7d6134ee9a2303fd2734f475a124b8b3` |
| last commit | *"lean(qou-gjg6): connectivity step 3 — and the hook-length shortcut for step 4 is blocked"* |
| age | **16 h** (threshold is 3 h) |
| newer PR activity | none since 2026-08-15T21:51Z |
| in-flight CI | none possible — CI is `workflow_dispatch`-only repo-wide, so a long build cannot be mistaken for a stall |

**Will continue from that branch's tip. Will NOT force-push over it** — the one
rule the protocol is emphatic about.

**This bean was at `todo`, not `in-progress`** — so the branch was doing 29
commits of work against an unclaimed bean. Claiming it now.

**Note on scope drift between bean and PR.** This bean's title is the *size-6
S₃-orbit Yang–Baxter identity*, described as the residual after the SW-4-gen
pass. PR #5076 states that identity is **done** — the braid relation holds
unconditionally via three admissibility flags dispatching to seven shape
theorems, sorry-free. So the bean title understates what the branch achieved,
and the residual it names may already be closed. First task of the takeover is
to establish what is actually left, rather than to resume against a stale
description.

**Downstream consumer, for whoever reads this next.** #5205 added
`QOU.BraidKnot.SeminormalEigenvalue`, a §3b-cond class with no instance,
carrying the seminormal eigenvalue statement as hypotheses. Discharging it is
`qou-ck0g` item 2, and its substrate is this branch's `seminormalRep`. So this
work has a named dependent now.


## FAR COMMUTATION PROVED GLOBALLY 2026-08-15 — two of three relations now hold

genMat_far_comm: rho(sigma_k) rho(sigma_l) = rho(sigma_l) rho(sigma_k) for |k-l| >= 2, all
of SYT mu, arbitrary shape. Sorry-free, axiom-clean. Blocker 1 of the step-(ii) list is now
closed at the MATRIX level, not just the tableau level (swapTableau_comm was the latter).

NO HYPOTHESIS ON q -- not even q > 0 or q != 1. Worth contrasting with the quadratic, which
needed both (via seminormalParam_add_neg, and via zpow_ne_one to stay off the pole): far
commutation never COMBINES two parameters, it only observes that the two products pair the
same four entries. So it holds for every real q, degenerate cases included.

SHAPE: both products are supported on {T, s_k.T, s_l.T, s_k s_l.T} and pair them identically,
because a far swap changes nothing the other generator reads --
axialDist_swapTableau_of_far (the parameter), swapAdmissible_far_iff (the admissibility,
BOTH directions), cellOf_swapTableau_of_ne (the partner) -- and swapTableau_comm makes the
fourth corner well defined. Four admissibility cases x up to five row cases; every one closes
by `ring` after the entry rewrites.

SUPPORTING (new): sum_mul_genMat_column_of_not_admissible (the scalar-column analogue of
sum_mul_genMat_column) and swapTableau_far_ne -- s_k.T and s_l.T differ at the cell holding
k, where the first carries k+1 and the second still carries k. That one is what the
four-element support rests on: T != s_k s_l.T follows from it by applying s_k.

LEAN GOTCHA THAT COST FOUR ITERATIONS, worth recording since it will recur in the braid:
`subst` ZETA-EXPANDS a `set` binding in the goal while leaving it folded in the context, so
a term-mode argument like `Ne.symm hAB : B != A` fails to elaborate against an expected type
displaying as `swapTableau T l ... != A` even though the two are defeq. Unification assigns
the metavariables before the defeq check. Fixes that work: use the by_cases hypothesis
directly when it already has the right shape (h2 : not (B = A)), or wrap in `by exact`.
Fix that does NOT work: `rw [<- hB]` to re-fold -- it just moves the unfolding to the other
argument.

REMAINING: the BRAID only. It is the one relation that is not column-local -- sigma_k and
sigma_{k+1} have different supports, so no column argument reaches it, and that is precisely
the content of Orbit3Braid / Orbit6Braid. Either lift those per-orbit identities via the
basis correspondence (blocker 3, still open), or find a global argument. hoefsmit_seminormal_rep
keeps its Ref'd sorry until then.


## BRAID REDUCED TO PURE ORBIT ALGEBRA 2026-08-15 — the third parameter is NOT a new unknown

Not the braid itself. What landed is the bridge that turns it into algebra, plus the one
structural fact that makes the algebra finite.

THE STRUCTURAL FACT (axialDist_succ_swapTableau / axialDist_swapTableau_succ, sorry-free):
an ADJACENT swap shifts the other generator's distance by the current one --

    d_{k+1}(s_k . T) = d_k(T) + d_{k+1}(T)       and the mirror
    d_k(s_{k+1} . T) = d_k(T) + d_{k+1}(T)

With cell contents x,y,z at entries k,k+1,k+2 the two distances are y-x and z-y; either
generator applied produces the third, z-x. So a <s_k,s_{k+1}>-orbit is governed by THREE
parameters a(p), a(r), a(p+r) satisfying ONE relation -- and that relation is exactly
Orbit6Braid.seminormalParam_mul_rel, a3(a1+a2-c) = a1 a2. The third parameter was never a
free unknown; contrast this with far commutation, where the other generator's distance is
UNCHANGED (axialDist_swapTableau_of_far) and no third parameter appears at all. That
contrast is the precise sense in which the braid is harder.

THE BRIDGE (genMat_braid_lhs_expand / genMat_braid_rhs_expand, sorry-free, axiom-clean):
two applications of the new genMat_mul_apply carry each triple product down to four entries
at NAMED tableaux of the orbit. Writing p = d_k(T), r = d_{k+1}(T), the braid becomes,
for every row T':

  rho_k[T',T] a(r) a(p) + rho_k[T',s_{k+1}T] off(r) a(p)
    + rho_k[T',s_kT] a(p+r) off(p) + rho_k[T',s_{k+1}s_kT] off(p+r) off(p)
  =
  rho_{k+1}[T',T] a(p) a(r) + rho_{k+1}[T',s_kT] off(p) a(r)
    + rho_{k+1}[T',s_{k+1}T] a(p+r) off(r) + rho_{k+1}[T',s_ks_{k+1}T] off(p+r) off(r)

This is Orbit6Braid's 6x6 identity re-derived in TABLEAU indices -- which is the point:
there is no basis correspondence to justify, so blocker 3 may be avoidable for the braid
too, exactly as route (c) avoided it for the quadratic and far commutation.

WHAT IS ACTUALLY BLOCKING, stated precisely: the ORBIT-SIZE CLASSIFICATION (bean qou-7xt3).
The row cases turn on which of s_kT, s_{k+1}T, s_{k+1}s_kT, s_ks_{k+1}T exist (each needs
its own admissibility) and which COINCIDE. In particular s_{k+1}s_kT != s_ks_{k+1}T is
precisely what makes an orbit size 6 rather than smaller, and the smaller orbits are the
cases where terms merge. Both expansions above also carry admissibility of the intermediate
tableau as an explicit hypothesis (hAl / hBk) -- discharging or case-splitting those is part
of the same classification.

So the honest state: the braid is no longer a search for a mechanism, it is a finite case
analysis waiting on the orbit classification. hoefsmit_seminormal_rep keeps its Ref'd sorry.


## SIZE-6 DISTINGUISHER PROVED + the method for every remaining orbit fact 2026-08-15

swapTableau_adj_words_ne (sorry-free): s_{k+1}s_k.T != s_k s_{k+1}.T. This single
inequality is what separates a generic <s_k,s_{k+1}>-orbit from a smaller one -- the two
length-2 words land apart exactly when all six words do. Contrast swapTableau_comm, where
the FAR generators commute outright; here they do not, and that failure IS the braid.

Also swapTableau_adj_ne (s_k.T != s_{k+1}.T) and the helper ne_of_entry_ne.

THE METHOD, which makes every remaining orbit fact an 8-line lemma. Every element of the
orbit is determined by its entries at the two cells c1 = cellOf T k and c2 = cellOf T (k+1)
(the third cell is forced). swapTableau_entry turns each into a swapVal word applied to
T.entry, so the whole computation is `rw [swapTableau_entry, ..., he]; simp only [swapVal];
split_ifs <;> omega`. With A = s_k.T, B = s_{k+1}.T, D = s_{k+1}A, E = s_kB, F = s_kD
(= s_{k+1}E, the braid element), the table is

           c1      c2
    T      k       k+1
    A      k+1     k
    B      k       k+2
    D      k+2     k
    E      k+1     k+2
    F      k+2     k+1

All six pairs are distinct, so any of the 15 pairwise distinctness facts follows by reading
off a column where the two rows differ and running the four-line tactic above. NOT
pre-built here: build them as the braid case analysis demands, rather than 15 lemmas most
of which may go unused.

Note the table also EXPLAINS the smaller orbits: they arise when some of A, B, D, E, F fail
to be admissible (not when they collide -- the entry values above are forced), which is why
both braid expansion lemmas carry intermediate admissibility as an explicit hypothesis.
That is the shape the remaining case analysis has to take.
