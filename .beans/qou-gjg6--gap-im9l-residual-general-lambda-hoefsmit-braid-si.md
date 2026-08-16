---
# qou-gjg6
title: 'GAP (im9l residual): general-lambda Hoefsmit braid — size-6 S3-orbit Yang-Baxter identity'
status: in-progress
type: task
priority: normal
created_at: 2026-08-11T01:05:26Z
updated_at: 2026-08-16T14:03:02Z

updated_at: 2026-08-16T14:06:51Z

updated_at: 2026-08-16T15:28:57Z

updated_at: 2026-08-16T16:43:28Z

updated_at: 2026-08-16T18:00:00Z

updated_at: 2026-08-16T19:15:16Z

updated_at: 2026-08-16T20:28:00Z

updated_at: 2026-08-16T20:46:27Z
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


## THE RELATION IS EXACTLY WHAT CLOSES THE BRAID -- diagonal row derived and formalised

Worked the generic-orbit algebra out by hand and it lands on seminormalParam_rel with
nothing left over. That is the strongest evidence so far that the GLOBAL braid route closes
(i.e. that blocker 3, the per-orbit basis correspondence, is avoidable for the braid too).

Parameter bookkeeping is now CLOSED for an orbit. Across the six elements only p, r, p+r and
their negatives ever occur:
  axialDist_succ_swapTableau       d_{k+1}(s_k T)     = p + r
  axialDist_swapTableau_succ       d_k(s_{k+1} T)     = p + r
  axialDist_swapTableau_word_left  d_k(s_{k+1}s_k T)  = r      <- the OTHER original one
  axialDist_swapTableau_word_right d_{k+1}(s_k s_{k+1} T) = p
  axialDist_swapTableau            d(s . T)           = -d
All sorry-free. No seventh parameter appears, which is why one relation suffices.

seminormalParam_rel (new, in SeminormalParam.lean):
    a(p+r) * (a(p) + a(r) - (q - q^-1)) = a(p) * a(r)
Orbit6.seminormalParam_mul_rel stated directly on seminormalParam instead of on the
multiplicative coordinates x = q^-2p, y = q^-2r -- usable where the distances are READ OFF
TABLEAUX rather than chosen. Both Orbit6Braid and SeminormalRep can now cite it.

THE DIAGONAL ROW, derived: resolving both expansions at T' = T gives
    left   a1^2 a2 + a3 * off(-p) off(p)
    right  a1 a2^2 + a3 * off(-r) off(r)
and offDiag_mul_neg turns each off*off into 1 + a(d)(c - a(d)) via seminormalParam_add_neg.
The difference factors as

    (a1 - a2) * [ a1 a2 - a3 (a1 + a2 - c) ]

whose second factor is seminormalParam_rel. Formalised as braid_diag_identity (sorry-free).
NOTE the first factor is NOT needed -- the identity holds whether or not a1 = a2, so no
genericity assumption about the orbit enters the diagonal row.

WHAT REMAINS: wire braid_diag_identity to the tableau level (needs T != D, T != E, T != F,
each an 8-line lemma off the (c1,c2) table recorded above), then the other five rows, then
the admissibility case tree for the non-generic orbits. Mechanical now, but not small.
hoefsmit_seminormal_rep keeps its Ref'd sorry.


## ALL SIX BRAID ROWS RESOLVED ALGEBRAICALLY 2026-08-15 — only THREE carry content

Resolved both expansions against the entry rules at every row of a generic (size-6) orbit.
Writing A = s_k.T, B = s_{k+1}.T, D = s_{k+1}A, E = s_kB, F = s_kD = s_{k+1}E:

  row  left                          right                        closes by
  T    a1^2 a2 + a3 off(-p)off(p)    a1 a2^2 + a3 off(-r)off(r)   braid_diag_identity
  A    off(p)(a1a2 + a3 a(-p))       off(p) a3 a2                 braid_rowA_identity
  B    a3 off(r) a1                  off(r)(a1a2 + a3 a(-r))      braid_rowB_identity
  D    a2 off(p+r)off(p)             off(p+r)off(p) a2            ring
  E    off(p+r)off(r)a1              a1 off(p+r)off(r)            ring
  F    off(r)off(p+r)off(p)          off(p)off(p+r)off(r)         ring

THE LAST THREE ROWS ARE IDENTITIES OF THE AMBIENT RING -- the two sides are literally the
same product reordered, no parameter relation involved. And all three content-bearing rows
reduce to the SAME single relation a3(a1+a2-c) = a1a2, differing only in the multiple of it
required: (a2-a1), -off(p), +off(r). All three formalised sorry-free (braid_diag_identity,
braid_rowA_identity, braid_rowB_identity).

WHY THIS IS THE PAYOFF OF ROUTE (c), concretely. Orbit6Braid proves the same mathematics as
an explicit 6x6 matrix identity whose triple product has 1296 scalar terms and needs
maxHeartbeats 1600000 (and which timed out entirely under !![...] literals -- see the
performance note above). Indexing by SYT mu instead of Fin 6 means the zero pattern is GIVEN
by the entry rules rather than discovered by simp, so half the rows collapse to `ring` and
the other half are one linear_combination each. The tableau-indexed route is not merely
correspondence-free, it is dramatically cheaper.

The full entry table used to derive the rows (generic orbit; a1 = a(p), a2 = a(r),
a3 = a(p+r), primes = a(-d) = c - a(d)):

  rho_k  col T: [T,T]=a1  [A,T]=off1     col A: [A,A]=a1' [T,A]=off1'
         col B: [B,B]=a3  [E,B]=off3     col D: [D,D]=a2  [F,D]=off2
         col E: [E,E]=a3' [B,E]=off3'    col F: [F,F]=a2' [D,F]=off2'
  rho_l  col T: [T,T]=a2  [B,T]=off2     col A: [A,A]=a3  [D,A]=off3
         col B: [B,B]=a2' [T,B]=off2'    col E: [E,E]=a1  [F,E]=off1
         col D: [D,D]=a3' [A,D]=off3'    col F: [F,F]=a1' [E,F]=off1'

REMAINING (unchanged in kind, now smaller): wire these three row identities to the tableau
level -- needs the pairwise distinctness among {T,A,B,D,E,F} (8-line lemmas off the (c1,c2)
table recorded earlier) and the admissibility case tree for non-generic orbits, where some
of A,B,D,E,F fail to be admissible and terms drop. hoefsmit_seminormal_rep keeps its Ref'd
sorry.


## ORBIT TABLE FORMALISED 2026-08-15 -- all 15 distinctness facts are now 2 lines each

The (c1,c2) table recorded earlier is no longer prose. swapTableau_entry_cellOf is the
primitive: `s_l.T` carries `swapVal l m` where `T` carried `m`, so any word in the two swaps
evaluates at cellOf T k / cellOf T (k+1) by iterating it. Five lemmas then pin all six words:

  orbitEntries_sk        s_k.T             (k+1, k)
  orbitEntries_sl        s_{k+1}.T         (k,   k+2)
  orbitEntries_sl_sk     s_{k+1}s_k.T      (k+2, k)
  orbitEntries_sk_sl     s_k s_{k+1}.T     (k+1, k+2)
  orbitEntries_sk_sl_sk  s_k s_{k+1}s_k.T  (k+2, k+1)
  (T itself is entry_cellOf: (k, k+1))

All sorry-free, axiom-clean, every one compiled first try. With these, EVERY pairwise
distinctness among the six is `ne_of_entry_ne` + `omega` -- no tableau reasoning left in it.
Twelve of the fifteen pairs separate at c1; three need c2 (T vs s_{k+1}.T, s_k.T vs
s_k s_{k+1}.T, s_{k+1}s_k.T vs the longest word).

Re-confirming a correction made earlier in this bean, now mechanically rather than by
argument: the six values are FORCED, so the words never collide. A smaller orbit is one
where some word fails to be SwapAdmissible, never one where two words coincide.

REMAINING for the braid, and it is now only assembly: instantiate the six rows (all six
already resolved algebraically -- three by `ring`, three by braid_diag_identity /
braid_rowA_identity / braid_rowB_identity) against genMat_braid_lhs_expand /
genMat_braid_rhs_expand, using these entry lemmas for the distinctness side conditions;
then the admissibility case tree for non-generic orbits. No mathematics left, only wiring.
hoefsmit_seminormal_rep keeps its Ref'd sorry.


## TABLEAU-LEVEL BRAID PROVED 2026-08-15 -- a prerequisite I had not noticed

swapTableau_braid: s_k s_{k+1} s_k . T = s_{k+1} s_k s_{k+1} . T, sorry-free. This was NOT
on the remaining-work list and should have been: without it the sixth orbit element is not
well defined, since the LHS expansion reaches it as s_k(s_{k+1}s_k.T) and the RHS as
s_{k+1}(s_k s_{k+1}.T). The matrix braid cannot even be stated cleanly until these are known
equal.

It is the UNDEFORMED shadow of the relation being chased -- at q = 1 the seminormal matrices
degenerate to permutation matrices and the Hecke braid becomes exactly this. Worth being
explicit that the deformed statement does NOT follow from it: the matrix braid needs
seminormalParam_rel, which is invisible at the tableau level. (Recording that so a later
reader does not mistake this for the braid.)

Proof is syt_ext down to swapVal_braid, the S_3 relation on value-transpositions.

LEAN PERFORMANCE GOTCHA, second of its kind on this front and worth generalising:
`unfold swapVal; split_ifs <;> omega` proves the TWO-swap statements (swapVal_involutive,
swapVal_comm) but TIMES OUT on the three-swap nesting at the default 200000 heartbeats --
and case-splitting on x first does NOT help, because each branch still carries the full
nesting. What works is pointwise rewriting with three evaluation lemmas
(swapVal_self / swapVal_succ / swapVal_of_ne, all new), so every step is search-free.
Generalisation: for these transposition-word identities, cost grows with NESTING DEPTH, not
with the number of cases; past depth 2, rewrite rather than split. Compare the Orbit6Braid
note above, where the fix was also to make lookup a single reduction rather than a search.

Also fixed: swapVal_self/_succ cannot be proved by `simp only [swapVal]; rw [if_pos rfl]` --
simp only has already reduced `k = k` to True, so the if_pos pattern is gone. Plain
`simp [swapVal]` closes both.

REMAINING, unchanged: instantiate the six rows against the two expansions. All prerequisites
now exist -- the six rows resolved algebraically, the orbit entry table, the distinctness
route, the third parameter, seminormalParam_rel, and now the tableau-level braid.
hoefsmit_seminormal_rep keeps its Ref'd sorry.


## FIRST BRAID ROW PROVED AT THE TABLEAU LEVEL 2026-08-15

genMat_braid_apply_diag: the braid's DIAGONAL entry, sorry-free and axiom-clean. Not the
abstract identity (that was braid_diag_identity) -- this is it wired to actual genMat
entries, with the tableau distinctness and admissibility discharged. The route is now
VALIDATED end to end; the remaining five rows are the same shape.

The proof, for anyone doing the other five:
1. set A,B,D,E as the orbit elements the row touches.
2. Distinctness T != A,B,D,E,F: A,B from swapTableau_ne; D,E,F by ne_of_entry_ne against
   orbitEntries_* + entry_cellOf + omega. T != F is needed TWICE, once as s_k D and once as
   s_l E; the second follows from the first by rewriting with swapTableau_braid.
3. Off-diagonal entries via genMat_swap applied to the PARTNER column (T = s_k A, so the
   (T,A) entry is genMat_swap on column A) with swapTableau_involutive to fold it back.
4. Both expansions, then genMat_diag / genMat_apply_of_ne for every entry, then the
   axialDist rewrites.
5. linear_combination, NOT nlinarith. nlinarith failed on the final goal even with all five
   facts supplied. The exact certificate is
     (a2 - a1)*hrel + a3*a1*hsump - a3*a2*hsumr + a3*hprodp - a3*hprodr
   (hsump/hsumr = seminormalParam_add_neg, hprodp/hprodr = offDiag_mul_neg, hrel =
   seminormalParam_rel). Derived by hand from the factorisation in braid_diag_identity.

Two Lean notes:
- `(by tac : Type)` is NOT valid ascription syntax inside a rw list; hoist to a `have`.
- The six admissibility hypotheses are all load-bearing EVEN FOR THIS ONE ROW: the (T,D) and
  (T,E) entries are only known to vanish once D and E exist as tableaux, which is what hDk
  and hEl provide. So there is no cheaper "diagonal-only" version with fewer hypotheses.

REMAINING: five rows (A, B by braid_rowA/rowB_identity; D, E, F by ring), then the
admissibility case tree for non-generic orbits. hoefsmit_seminormal_rep keeps its Ref'd sorry.


## THE BRAID IS PROVED (generic orbit) 2026-08-15 — all three Hecke relations now hold

genMat_braid_generic: rho(sigma_k) rho(sigma_{k+1}) rho(sigma_k) =
rho(sigma_{k+1}) rho(sigma_k) rho(sigma_{k+1}) in column T, for any T whose
<s_k,s_{k+1}>-orbit is the full size-6 one (all six admissibilities hold). Sorry-free,
axiom-clean. With genMat_quadratic and genMat_far_comm, ALL THREE Hecke relations now hold
on all of SYT mu for arbitrary shape.

The six rows came out exactly as derived: D, E, F by `ring`; T, A, B by the single relation
with multiples (a2-a1), -off(p), +off(r).

THE ONE THING THAT COST ITERATIONS, and it was not the mathematics: getting the COLUMN MAP
right. The two expansions do not use the same column sets --
  LHS (genMat_braid_lhs_expand) reads rho_k at columns  T, B, A, D
  RHS (genMat_braid_rhs_expand) reads rho_l at columns  T, A, B, E
-- and each entry needs its own (distinctness, admissibility, partner) triple. Getting a
column wrong produces an unhelpful "rewrite failed / ring failed" rather than a type error.
The full 6x8 map is worth having written down; it is reconstructible from the two expansion
statements plus the entry table above, but reconstructing it under time pressure is where
the mistakes happen.

Partner identities needed for the side conditions (column, generator -> partner):
  (T,k)->A  (T,l)->B  (A,k)->T [bAT]  (A,l)->D  (B,k)->E  (B,l)->T [bBT]
  (D,k)->F  (E,l)->F [via hFE = swapTableau_braid]

LEAN NOTES (both cost real time):
1. `subst` on `h : T' = X` eliminates T' and ZETA-EXPANDS every `set` binding in the goal
   while leaving them folded in the context. Fix: `simp only [<- hA, <- hB, ...]` right
   after each subst to re-fold. This is the same gotcha recorded for far commutation, now
   with a general fix rather than a per-site workaround.
2. `subst` picks its direction: on `h1 : T' = T` it eliminated T (goal became T'), on
   `h2 : T' = A` with A a set-variable it eliminated T'. Do not assume; read the error.

REMAINING for hoefsmit_seminormal_rep: (a) the admissibility case tree for NON-generic
orbits (sizes 1,2,3 -- where some of A,B,D,E,F fail SwapAdmissible and terms drop; the
orbit-local identities are already proved in Orbit3Braid/Orbit6Braid), and (b) packaging
the three relations into a `Hecke ->a` algebra map via Hecke.lift. The Ref'd sorry stays
until both land.


## TWO CORRECTIONS TO MY OWN PLAN, AND THE SIZE-1 CASE 2026-08-15

CORRECTION 1 -- the packaging order I recommended last tick was BACKWARDS. I said "start
with Hecke.lift packaging, it is the one that discharges the sorry". It cannot be started
first: Hecke.lift's `hbraid` argument is `forall i, ... g i * g (i+1) * g i = ...`, a
statement about the MATRICES, so it needs the braid for EVERY column T -- i.e. for
non-generic orbits too. Packaging DEPENDS ON the case tree; it is not an alternative to it.

CORRECTION 2 -- the non-generic case tree is NOT bookkeeping either. Working the size-1
case (T fixed by both generators) turned up a genuine lemma with a genuine proof:

  axialDist_eq_of_not_admissible (sorry-free, axiom-clean):
    ¬SwapAdmissible T k → ¬SwapAdmissible T (k+1) → axialDist T k = axialDist T (k+1)

i.e. adjacent generators that both fix T fix it with the SAME scalar. WITHOUT THIS THE
BRAID IS FALSE on size-1 orbits: both sides collapse to a(d_k)^2 a(d_l) and a(d_l)^2 a(d_k),
whose difference is a(d_k)a(d_l)(a(d_k) - a(d_l)); with a(+-1) in {q, -1/q} that vanishes iff
the two distances agree, and is -(q + 1/q) != 0 when they differ. So this is load-bearing,
not a convenience.

The content is that the MIXED configurations are IMPOSSIBLE, not merely unobserved. If k,k+1
share a row and k+1,k+2 share a column, adjacency forces the cells to be (i,j), (i,j+1),
(i+1,j+1); then the corner (i+1,j) lies in mu by up-left closure and is squeezed strictly
between k and k+2, so it carries k+1 -- which (i,j+1) already carries. cellOf_unique then
equates two distinct cells. The column-then-row case is the mirror, with corner (i,j+2)...
(actually (i, c3.2)). Same shape as axialDist_ne_zero: a forced corner.

Lean note: `refine (axialDist_of_sameRow T hm2 ?_ he2 ?_).symm` cannot infer j2 (it is
determined by the LAST argument); supply it as `(j2 := ...)`. Same for _sameCol with i2.

REMAINING for hoefsmit_seminormal_rep, restated correctly:
  (1) the rest of the non-generic case tree -- sizes 2 and 3, where SOME of A,B,D,E,F are
      admissible and terms drop. Size 1 now has its key lemma; the braid identity on it
      still needs assembling.
  (2) THEN packaging into a Hecke ->a algebra map via Hecke.lift, which consumes (1).


## SIZE-1 ORBIT BRAID PROVED + the degeneracy that makes ALL smaller orbits cohere

genMat_braid_of_both_fixed (sorry-free): the braid on a size-1 orbit, i.e. when neither
generator moves T. Both columns are scalar, both triple products collapse, and the two sides
agree BECAUSE axialDist_eq_of_not_admissible identifies the scalars. This is the only place
in the whole construction where the braid rests on a GEOMETRIC fact about mu rather than on
the parameter algebra -- worth noting when reading the proof.

Then, working the size-2 case, the missing piece for ALL the smaller orbits surfaced:

  seminormalParam_mul_neg_one:  a(1) * a(-1) = -1
  offDiag_neg_one:              offDiag q (-1) = 0
  offDiag_one:                  offDiag q 1 = 1

The two size-1 eigenvalues q and -1/q multiply to -1, so `1 + a(d)a(-d)` -- the off-diagonal
factor of seminormalBlock, and the d<0 branch of offDiag -- VANISHES at d = +-1.

WHY THIS IS THE COHERENCE CONDITION, and it is worth being explicit because it is easy to
miss: genMat applies ONE uniform entry rule to every column, including the scalar ones. That
rule OFFERS a size-1 orbit an off-diagonal partner entry. The construction only works
because that entry is forced to zero. Without a(1)a(-1) = -1 the uniform rule would be
inconsistent with the size-1 blocks being genuinely 1x1 -- so this is not a convenience
lemma, it is the reason the uniform indexing (route (c)) is legitimate at all.

Concretely it is what makes the size-2 case close: there the RHS lacks the term
a3*(1 + a2*a(-a2)) that the generic diagonal row carries, and the two sides only match
because that factor is 0 when the l-distance is +-1.

REMAINING: sizes 2 and 3 assembled (the algebra is now understood -- see above), then
Hecke.lift packaging (which consumes them). hoefsmit_seminormal_rep keeps its Ref'd sorry.


## SIZE-2 ORBIT BRAID PROVED 2026-08-15 — and the smaller orbits are NOT special cases

genMat_braid_of_succ_fixed (sorry-free, axiom-clean): the braid when sigma_k moves T but
sigma_{k+1} fixes both T and s_k.T, so the orbit is exactly {T, s_k.T}.

The two non-zero rows close DIFFERENTLY, which is the finding:

  s_k.T row -- braid_rowA_identity VERBATIM. Same identity as the generic case.
  T row     -- the generic diagonal identity MINUS the term a3*(1 + a2*a(-r)), which the
               right-hand side does not produce here. The two sides match ONLY because that
               factor is 0.

So a smaller orbit is not a degenerate instance of the generic identity; it is the generic
identity WITH A TERM DELETED, and the deletion is legitimate exactly because of the scalar
degeneracy (one_add_seminormalParam_mul_neg_of_scalar, available because sigma_{k+1} fixing
T forces r = +-1 via axialDist_trichotomy). Anyone doing size 3 should expect the same
shape: not "specialise the generic proof" but "generic identity minus the terms the
non-admissible columns cannot emit, with degeneracy licensing each deletion".

Certificate for the T row (extends the generic one by one term):
  (a2-a1)*hrel + a3*a1*hsump - a3*a2*hsumr + a3*hdeg + a3*hprodp
The s_k.T row is the generic (-o1)*hrel + a3*o1*hsump unchanged.

Lean note: the (A,A) entry of rho_{k+1} needs its OWN genMat_diag + dAl even though dAl was
already applied to the COEFFICIENT in the outer peel. `rw` had consumed dAl on the
coefficient; the entry is a separate occurrence. Symptom is a `ring failed` whose goal still
shows `genMat q (k+1) hl hln A A` -- read the goal, do not re-derive the certificate.

STATUS OF THE CASE TREE: size 1 done, size 2 done (this), sizes 3 and 6 -- 6 is
genMat_braid_generic, 3 remains. Then Hecke.lift packaging.


## MIRROR SIZE-2 PROVED 2026-08-15 — and it deletes the OTHER term

genMat_braid_of_fixed_succ (sorry-free): sigma_{k+1} moves T, sigma_k fixes both T and
s_{k+1}.T, so the orbit is {T, s_{k+1}.T}.

Not a copy of genMat_braid_of_succ_fixed with names swapped -- the deletion is on the other
side. There the RIGHT-hand side lacked a3*(1 + a2*a(-r)) and the degeneracy was at r = +-1;
here the LEFT-hand side lacks a3*(1 + a1*a(-p)) and the degeneracy is at p = +-1. The moved
row is braid_rowB_identity verbatim (vs rowA in the other).

T-row certificate (note the SIGNS differ from the succ_fixed case):
  (a2-a1)*hrel + a3*a1*hsump - a3*a2*hsumr - a3*hdegp - a3*hprodr

CASE TREE STATUS: size 1 done, BOTH size-2 orientations done, size 6 done
(genMat_braid_generic). Size 3 remains, in its two orientations
  (hka, ¬hla, hAl)  and  (¬hka, hla, hBk)
plus whatever sub-cases of (hka, hla) fail to reach the full six. Then Hecke.lift.

Lean note, recurring: when a row needs BOTH diagonals (rho_k[X,X] and rho_l[X,X]), the two
`genMat_diag` applications instantiate in GOAL ORDER -- LHS first, so generator k first.
`rw [genMat_diag, dBl, genMat_diag, dBk]` fails; `rw [genMat_diag, dBk, genMat_diag, dBl]`
works. The error points at the axialDist rewrite, not at genMat_diag, so it misleads.


## SIZE-3 HAS **THREE** POSITIONS, NOT TWO — and the middle one shares the generic flags

Worked out the size-3 taxonomy before writing any of it. A size-3 orbit is a domino plus a
disjoint cell, and T can sit at any of its three positions; each gives a DIFFERENT
admissibility pattern:

  T at the sigma_k-fixed end        (¬hka,  hla,  hBk)
  T in the middle                   ( hka,  hla, ¬hAl, ¬hBk)
  T at the sigma_{k+1}-fixed end    ( hka, ¬hla,  hAl)

THE MIDDLE POSITION HAS hka AND hla -- the same leading flags as a GENERIC size-6 orbit. So
"both generators move T" does NOT imply the orbit is generic, and the final assembly must
split on hAl/hBk rather than stopping at (hka, hla). Anyone writing that assembly should read
this before assuming a 4-way split on the two leading flags suffices; it does not.

genMat_braid_of_succ_fixed_three (sorry-free, axiom-clean) does the third row of that table.
The T and s_k.T rows carry the SAME two identities as the size-2 case
genMat_braid_of_succ_fixed; what is new is the third row, which closes by `ring` alone once
axialDist_swapTableau_word_left supplies d_k(s_{k+1}s_k.T) = r.

So the deletion pattern recorded earlier holds up: the smaller orbits are the generic
identity with terms deleted, and going 2 -> 3 ADDS BACK a row rather than changing the two
that were already there.

Lean note: a column whose tableau is NOT admissible needs genMat_of_not_admissible, not
genMat_apply_of_ne -- the latter takes SwapAdmissible and rejects the negation. Symptom is
"Application type mismatch" on the admissibility argument; three sites hit it at once here.

CASE TREE: size 1 done; both size-2 done; size-3 sigma_{k+1}-fixed-end done; size 6 done.
REMAINING: size-3 middle, size-3 sigma_k-fixed end, then any (hka,hla,hAl,hBk) combinations
that are neither generic nor middle (7 and 8 in the enumeration -- possibly vacuous, but
that needs proving, not assuming). Then Hecke.lift.


## SIZE-3 MIDDLE PROVED 2026-08-15 — and it INVERTS the pattern the smaller orbits set

genMat_braid_of_middle (sorry-free, axiom-clean): both generators move T, but neither
s_k.T nor s_{k+1}.T extends, so the orbit is {s_{k+1}.T, T, s_k.T}.

THE FINDING, and it is the opposite of what sizes 1 and 2 predicted: this case needs NO
DELETION AND NO DEGENERACY. Its three rows are braid_diag_identity, braid_rowA_identity and
braid_rowB_identity UNCHANGED -- the same three the generic size-6 orbit uses.

The reason is structural: sizes 1 and 2 were "generic identity minus terms", licensed by the
scalar degeneracy 1 + a(d)a(-d) = 0, which is available only when a generator FIXES T. Here
neither generator fixes T, so no distance is +-1 and no degeneracy exists to invoke -- and
none is needed. The orbit is smaller than generic purely because the two LENGTH-2 words fail
to exist; the rows that do exist are the generic ones verbatim.

So the earlier bean note "smaller orbits are the generic identity with a term deleted" is
TRUE FOR THE ORBITS WHERE A GENERATOR FIXES T, and false in general. Corrected here rather
than left to mislead. The right statement: deletion tracks which COLUMNS are scalar, not
orbit size.

CASE TREE: size 1 done; both size-2 done; size-3 middle done; size-3 sigma_{k+1}-fixed end
done; size 6 done. REMAINING: size-3 sigma_k-fixed end (¬hka, hla, hBk) -- the mirror of the
one already done -- and then whether (hka, hla, hAl, ¬hBk) / (hka, hla, ¬hAl, hBk) can occur
at all. Then Hecke.lift.


## ALL SIX ORBIT SHAPES PROVED 2026-08-15

genMat_braid_of_fixed_succ_three (sorry-free, axiom-clean, compiled first try) closes the
last size-3 position. The braid identity now holds on EVERY orbit shape:

  size 1                          genMat_braid_of_both_fixed
  size 2, sigma_{k+1} scalar      genMat_braid_of_succ_fixed
  size 2, sigma_k scalar          genMat_braid_of_fixed_succ
  size 3, sigma_{k+1}-fixed end   genMat_braid_of_succ_fixed_three
  size 3, middle                  genMat_braid_of_middle
  size 3, sigma_k-fixed end       genMat_braid_of_fixed_succ_three
  size 6, generic                 genMat_braid_generic

The "deletion tracks which columns are scalar" rule (corrected two entries above) predicted
this one exactly: the sigma_k-fixed end deletes on the LEFT with degeneracy at p, mirroring
the sigma_{k+1}-fixed end which deletes on the right with degeneracy at r. First-try compile,
which is the rule earning its keep.

REMAINING before Hecke.lift -- and this is now the WHOLE of what stands between here and
hoefsmit_seminormal_rep:

  (a) The two unclassified flag patterns (hka, hla, hAl, ¬hBk) and (hka, hla, ¬hAl, hBk).
      By the domino/antichain picture these should be VACUOUS -- if both generators move T
      and exactly one of the length-2 words exists, there is no 3-cell configuration that
      realises it -- but that is an argument, not a proof, and it must be PROVED vacuous or
      handled. Do not assume.
  (b) genMat_braid_generic takes hDk and hEl as hypotheses. For the assembly they must be
      DERIVED from (hka, hla, hAl, hBk), or the generic case restated without them.
  (c) Then Hecke.lift: hquad from genMat_quadratic (with q*q^-1 = 1), hcomm from
      genMat_far_comm, hbraid by dispatching on the flags to the seven theorems above.

Note (a) and (b) are the same question from two sides: which flag combinations are actually
realisable. A lemma classifying the reachable patterns would close both.


## REALISABILITY CLASSIFIED 2026-08-15 — BOTH remaining gaps close, and they were one question

Three lemmas, all sorry-free, all compiled FIRST TRY (the cell analysis was done on paper
before any Lean was written, which is why):

  swapAdmissible_cross_iff       SwapAdmissible (s_k.T) (k+1)  <->  SwapAdmissible (s_{k+1}.T) k
  swapAdmissible_word_left_iff   SwapAdmissible (s_{k+1}s_k.T) k     <->  SwapAdmissible T (k+1)
  swapAdmissible_word_right_iff  SwapAdmissible (s_k s_{k+1}.T) (k+1) <->  SwapAdmissible T k

WHY: writing c1,c2,c3 for the cells holding k,k+1,k+2, EVERY admissibility anywhere in the
orbit is one of just THREE conditions -- (c1,c2), (c2,c3), (c1,c3) sharing neither row nor
column -- because each word only permutes which ENTRY sits in which of the three CELLS. The
table:

  word              its k-condition   its (k+1)-condition
  T                 (c1,c2)           (c2,c3)
  s_k.T             (c1,c2)           (c1,c3)
  s_{k+1}.T         (c1,c3)           (c2,c3)
  s_{k+1}s_k.T      (c2,c3)           --
  s_k s_{k+1}.T     --                (c1,c2)

BOTH open items fall out, and they were the same question seen from two sides, as suspected:

 (a) hAl and hBk are the SAME condition (c1,c3). So the two unclassified flag patterns
     (hka, hla, hAl, ¬hBk) and (hka, hla, ¬hAl, hBk) are VACUOUS -- now proved, not assumed.
 (b) hDk <-> hla and hEl <-> hka. So genMat_braid_generic's two extra hypotheses are DERIVED
     from the leading flags; no restatement of the generic case is needed.

This is also, essentially, the qou-7xt3 orbit-size classification: the orbit shape is
determined by which of the three pairwise conditions hold, i.e. by the comparability poset
on {c1,c2,c3}. Three conditions true -> size 6; two -> size 3 (three positions by WHICH two);
one -> size 2; none -> size 1. Worth folding back into qou-7xt3.

REMAINING: only the assembly now -- a single genMat_braid theorem dispatching on
(hka, hla, hAl) via these iffs to the seven shape theorems, then Hecke.lift. No open
mathematics.


## THE BRAID IS UNCONDITIONAL 2026-08-15 — all three Hecke relations, no orbit hypotheses

genMat_braid (sorry-free, axiom-clean, compiled first try):

    rho(sigma_k) rho(sigma_{k+1}) rho(sigma_k)
      = rho(sigma_{k+1}) rho(sigma_k) rho(sigma_{k+1})

on all of SYT mu, arbitrary shape, NO hypothesis about the orbit. It dispatches on three
flags -- does sigma_k move T, does sigma_{k+1}, does sigma_{k+1} move s_k.T -- to the seven
shape theorems, and every further admissibility those need is DERIVED via the classification
iffs rather than assumed.

With genMat_quadratic and genMat_far_comm, the three Hecke relations now hold unconditionally
for the general-lambda seminormal representation.

Note the dispatch needs only THREE flags, not four: hBk is determined by hAl
(swapAdmissible_cross_iff), which is why the tree has 7 leaves and not 9. The two patterns
that would have made it 9 are the vacuous ones.

REMAINING for hoefsmit_seminormal_rep: PACKAGING ONLY. Hecke.lift wants
  g : Fin n -> Matrix (SYT mu) (SYT mu) R
  hquad  : forall i, g i * g i = (q - qi) . g i + (q * qi) . 1     <- genMat_quadratic, qi := q^-1
  hbraid : forall i (hi : i+1 < n), ...                            <- genMat_braid
  hcomm  : forall i j, j+2 <= i -> g i * g j = g j * g i           <- genMat_far_comm
The work is the index translation between `k : N` with 1 <= k, k+1 <= |mu| here and `Fin n`
there (n = |mu| - 1, generator i <-> k = i+1), plus matching Hecke's smul normalisation.
No open mathematics.


## THE REPRESENTATION IS BUILT 2026-08-15 — but it does NOT discharge the stated sorry

seminormalRep (sorry-free, axiom-clean):

    Hecke R q q^-1 n ->a[R] Matrix (SYT mu) (SYT mu) R    for  |mu| = n+1,  0 < q,  q != 1

built from genMat_quadratic / genMat_far_comm / genMat_braid through Hecke.lift, with
seminormalRep_sigma as the computation rule. The general-lambda Hoefsmit seminormal
representation now EXISTS as an algebra map. Also hoisted instFintypeSYT / instDecEqSYT to
file level (Matrix's ring structure needs BOTH; the sections had only supplied Fintype
locally, via `open scoped Classical` for the DecidableEq).

I CHECKED WHETHER THIS CLOSES hoefsmit_seminormal_rep. IT DOES NOT. Three gaps remain, and
the third is not bookkeeping:

 (a) INDEX TYPE. The statement wants Matrix (Fin (dLambda lam)) (Fin (dLambda lam)) R; mine
     is indexed by SYT mu. Needs dLambda lam = #SYT(partitionShape lam) plus a reindex along
     an equiv (Matrix.reindexAlgEquiv). Mechanical but not written.
 (b) NON-SCALARITY. The statement's payload is `2 <= dLambda lam -> exists i, forall s,
     rho(sigma_i) != s . 1`. Nothing above proves that; it is bean SW-5. Should be reachable
     -- if dLambda >= 2 some generator has two distinct diagonal entries a(d) and a(-d), or
     a nonzero off-diagonal -- but it is a separate argument.
 (c) HYPOTHESIS MISMATCH, and this one is a real question, not a chore. The statement assumes
     only `hq : q != 0`. seminormalRep needs `0 < q` AND `q != 1`, because seminormalParam
     has a pole where q^(-2d) = 1 and zpow_ne_one is what keeps it off. At q = -1 (q^2 = 1)
     the formula degenerates -- SeminormalParam.lean already records that S1's entry is
     -1/(2q) != 0 while the formula gives 0/0. So the stated theorem is NOT a corollary of
     this construction for general q != 0, and may need either a weaker hypothesis in the
     statement or a different construction at roots of unity. DO NOT assume it follows.

So the honest status: the mathematics of the general-lambda seminormal representation is
DONE for 0 < q != 1. hoefsmit_seminormal_rep keeps its Ref'd sorry, and closing it needs (a),
(b), and a decision about (c) -- which is an owner-facing question about whether the stated
hypothesis is right, not something to quietly widen or narrow.


## HYPOTHESIS QUESTION RESOLVED 2026-08-15 — no literature needed; the sharp condition is q != 0 AND q^2 != 1

Owner asked whether resolving hoefsmit_seminormal_rep's hypotheses needs literature. It does
not -- the question is elementary over R and now settled both ways:

  OVER R:  q^m = 1 for some m != 0  <=>  |q| = 1  <=>  q = +-1  <=>  q^2 = 1

So `q != 0 AND q^2 != 1` is EXACTLY the condition for seminormalParam to stay off its pole
(denominator 1 - q^(-2d), d != 0). Consequences, both acted on:

 1. MY hypothesis was TOO STRONG. The file ran on `0 < q AND q != 1`; negative q is fine as
    long as q != -1. Weakened throughout -- 11 signatures, 36 zpow_ne_one call sites, 9
    downstream call sites. zpow_ne_one is reproved via q^2 (positive outright, and exactly
    what the hypothesis bounds) rather than via |q|, which also dodges the fact that
    `abs_zpow` / `abs_eq_one` are not the Mathlib names.
 2. THE STATED THEOREM's hypothesis is TOO WEAK, and this is the owner-facing part.
    hoefsmit_seminormal_rep assumes only `hq : q != 0`. At q = -1 the seminormal form
    genuinely degenerates -- SeminormalParam.lean already records that S1's entry is
    -1/(2q) != 0 there while the axial-distance formula gives 0/0. So the theorem as stated
    is NOT provable from this construction, and I believe it is simply missing a hypothesis.
    RECOMMENDATION: amend it to `(hq : q != 0) (hq2 : q^2 != 1)`. That is the standard
    genericity assumption -- H_n(q) is semisimple away from roots of unity -- and it is what
    [ram1997]'s axial-distance formulas presuppose. Not doing this unilaterally: it changes
    a stated theorem, so it is the owner's call.

Also landed: genMat_ne_scalar -- a generator that moves ANY tableau is not a scalar matrix,
with NO hypothesis on q. The argument is worth recording because the obvious route fails:
offDiag at the moved entry CAN vanish (offDiag q (-1) = 0). What cannot vanish is the PAIR --
the entries (s_k.T, T) and (T, s_k.T) sit at distances d and -d, and offDiag takes the plain
value 1 on the non-negative branch, so whichever sign d has, one of the two is exactly 1.

That is the substantive half of gap (2). The remaining half is combinatorial: #SYT mu >= 2
implies SOME generator moves SOME tableau (the SYT-connectivity fact -- the ledger's
"all-T connectivity" in yt-seminormal-infra). Not attempted here.


## HYPOTHESIS AMENDED 2026-08-15 (owner approved) — hoefsmit_seminormal_rep now takes q^2 != 1

Per owner go-ahead, hoefsmit_seminormal_rep's signature is now

    (q : R) (hq : q != 0) (hq2 : q^2 != 1) (lam : Partition N)

Checked before amending: NO Lean call site applies the theorem (all references are docstring
mentions), so the added hypothesis breaks nothing.

Its docstring is also rewritten. It had described the braid for arbitrary lambda as the
outstanding residual -- that is now proved (genMat_braid), so leaving the description would
have misdirected the next reader to work that is done. It now names the two ACTUAL gaps
(reindexing; the connectivity half of non-scalarity) and records why q^2 != 1 is not
decoration.


## REINDEX GAP CLOSED 2026-08-15 — and a duplicate-instance diamond removed on the way

seminormalRepFin (sorry-free, axiom-clean, first-try compile):

    Hecke R q q^-1 m ->a[R] Matrix (Fin (dLambda lam)) (Fin (dLambda lam)) R

i.e. seminormalRep transported along Fintype.equivFin. NO cardinality theorem was needed:
dLambda lam is DEFINED as Fintype.card (SYT lam), so Fin (dLambda lam) is already
Fin (Fintype.card (SYT lam)) and equivFin is the map.

THE TRAP I WALKED INTO AND BACKED OUT OF, worth recording because it would have surfaced far
from its cause: when packaging I declared

    noncomputable instance instFintypeSYT : Fintype (StandardYoungTableau mu) := Fintype.ofFinite _

But YoungTableaux.lean ALREADY declares instFintypeStandardYoungTableau by the same
Fintype.ofFinite, and it is in scope transitively (SeminormalRep -> TableauCells ->
HoefsmitRep -> YoungTableaux). Two Fintype instances on one type is a genuine DIAMOND, and
here it is load-bearing: dLambda is Fintype.card, so two instances give two cardinals and the
reindex along equivFin would not typecheck against dLambda -- or worse, would typecheck
against the wrong one. REMOVED; the file now relies on the shared instance. Only
instDecEqSYT (DecidableEq, which nothing else provides) is declared here, with a comment
saying why the Fintype deliberately is not.

Generalisable lesson: before declaring an instance for a type you did not define, grep the
import cone for an existing one. `Fintype.ofFinite` is especially prone to this because it is
the obvious thing to write and carries no hint that someone else already wrote it.

REMAINING for hoefsmit_seminormal_rep: only the connectivity half of non-scalarity --
#SYT mu >= 2 implies SOME generator moves SOME tableau. genMat_ne_scalar already converts
that into the statement's payload. Also needs (shape lam).cells.card = N to line the index
m = N - 1 up with the statement; not checked whether that is available.


## CONNECTIVITY: the route that AVOIDS the connectivity theorem, and two of its four steps

The last gap is: #SYT mu >= 2 implies SOME generator moves SOME tableau. The obvious route is
the SYT-connectivity theorem (any two SYT joined by swaps) -- that is the ledger's "all-T
connectivity" and it is a real theorem. IT IS NOT NEEDED. Contrapositive route instead:

  a tableau that NO generator moves is forced to be a single row or a single column,
  and such a shape has exactly one tableau.

So a single non-movable T already forces #SYT mu = 1; hence #SYT >= 2 makes EVERY T movable,
and picking any one finishes. This is strictly weaker than connectivity and only needs facts
about ONE tableau at a time.

STEP 1 DONE -- axialDist_eq_of_no_admissible (sorry-free, first-try compile): if every
generator fixes T then all of T's axial distances agree. Chains axialDist_eq_of_not_admissible
by induction. Since ¬adm forces d = +-1, the common value is +1 or -1.

STEP 2 DONE -- sameRow_of_not_admissible_of_one / sameCol_of_not_admissible_of_neg_one: a
fixed generator at distance +1 fixes within a ROW (¬adm leaves "same row or same column", and
same-column would force -1); mirror at -1.

STEP 3 TODO -- chain step 2 over all k: all cells of T lie in one row (resp. one column).
STEP 4 TODO -- a Young diagram all of whose cells lie in one row IS a single row (cellOf is
onto mu.cells), and a single row/column has exactly one SYT. Then #SYT mu = 1.

Then genMat_ne_scalar converts it into the statement's payload.

ALSO STILL NEEDED for hoefsmit_seminormal_rep, unrelated to the above: (shape lam).cells.card
= N, to line the generator index m up with the statement's N - 1. Not checked whether the
repo has it.


## CONNECTIVITY STEP 3 DONE — and the tempting shortcut for step 4 is BLOCKED

row_const_of_no_admissible / col_const_of_no_admissible (sorry-free, first-try): chaining
step 2 over all k, a tableau no generator moves has ALL its cells in one row (common distance
+1) or all in one column (-1).

STEP 4 REMAINS: "a Young diagram with all cells in one row has exactly one SYT".

DO NOT try to get this from the hook-length formula. It looks available --
QOU/Mathlib/SYTHookFormulaRows.lean proves dimHLF_single : dimHLF [a] = 1, i.e. HLF's
PREDICTION for a single row -- but the bridge from dimHLF to the actual tableau count is
`numSYTenum l = dimHLF l`, the Greene-Nijenhuis-Wilf theorem, and that file states plainly it
"remains open in this corpus". So dimHLF_single gives the right NUMBER on the wrong SIDE of an
open theorem. Citing it would be circular-by-omission.

The direct route needs no HLF at all and is elementary: in a single-row diagram the entry map
restricted to row 0 is strictly increasing (row_strict) and bijective onto {1..N} (bijOn), so
entry (0,j) = j+1 -- two inductions, a lower bound from monotonicity upward and an upper
bound from the top cell downward. Then cellOf T j = (0, j-1) for EVERY T, hence any two
tableaux agree, hence #SYT = 1. Estimated 40-60 lines.

Also still needed, independent of this chain: (shape lam).cells.card = N.


### Takeover assessment — the dependency graph is mis-stated, and 2 of 4 sorries are NOT blocked

Four `sorry`s on the branch. The comments say all four chain to one root
(`hoefsmit_seminormal_rep`). **Two of them do not.**

| # | site | comment says | actually |
|---|---|---|---|
| 1 | `HoefsmitRep:433` `hoefsmit_seminormal_rep` | the root GAP | **root, correct** — and blocked on a genuine owner question (below) |
| 2 | `QJucysMurphy:299` `qJM_commute` | *"Blocked on: the general seminormal rep"* | **NOT blocked** — see below |
| 3 | `QJucysMurphy:520` `barSymJMSum_block_eigenvalue` | needs root + per-element eigenvalue | correct, and **not provable as stated** (below) |
| 4 | `QJucysMurphy:530` `barSymJMSum_central` | needs `qJM_commute` | correct — so it is one step behind #2, not behind the root |

**#2 is the reroute.** `qJM` is defined by the standard multiplicative
recursion `L_{k+1} = σ_k · L_k · σ_k` (`QJucysMurphy:95`). Commutativity of the
Murphy family from *that* recursion is an **algebraic induction on the Hecke
relations** — it needs no representation at all. The comment names the
seminormal-diagonalisation proof, which is *a* sufficient route, as if it were
*the* route.

Both ingredients the induction needs are already in the tree and sorry-free, in
`SchurWeyl/HeckeAlgebra.lean`:

* `σ_braid` (`:107`) — `σ_i σ_{i+1} σ_i = σ_{i+1} σ_i σ_{i+1}`
* `σ_commute` (`:115`) — far commutation, `j + 2 ≤ i`

So the route is concretely open, not merely plausible. Closing #2 also closes
#4, taking **two of the four sorries off the hard root** — and neither needs the
general-λ construction, the index reindex, or any decision about `q`.

This matters beyond bookkeeping: an agent reading the existing comment waits for
the *harder* thing. Same shape as the mis-stated blockers found across `wpdb`
this session.

**#3 is not provable as stated, and that is the PR's own finding.** Its
signature assumes only `(hq : q ≠ 0)`, while `seminormalRep` requires `0 < q`
**and** `q ≠ 1` — `seminormalParam` has a pole where `q^{-2d} = 1`, and at
`q = -1` the formula degenerates (`SeminormalParam.lean` records `S1`'s entry as
`-1/(2q) ≠ 0` there while the formula gives `0/0`). So closing #3 needs either a
**weakened hypothesis in the statement** or a **different construction at roots
of unity**. That is an owner-facing question, correctly escalated by the
original session and left alone here.

**Next step for this branch:** prove `qJM_commute` by induction on the
recursion, then `barSymJMSum_central` from it. Do **not** wait on
`hoefsmit_seminormal_rep` for either.


### Progress + a correction to the assessment above (2026-08-16, later)

Two sorry-free, axiom-clean, **constructive** theorems landed in
`QJucysMurphy.lean` (`[propext, Quot.sound]` — no `Classical.choice`):

* **`qJM_comm_sigma`** — `σ_m` commutes with `L_k` whenever `k + 1 ≤ m`.
  Induction on `k` off `L_{k+1} = σ_k L_k σ_k`, using only `σ_commute`.
* **`qJM_commute_of_adjacent`** — **full** commutativity of the Murphy family
  follows from the adjacent case alone.

**🔻 Correcting what I wrote above.** I said the general case is "an algebraic
induction", which implied the far case routes *around* the adjacent one. **It
does not — it reduces to it.** Peeling `σ_{j-1}` off `L_j` needs `i + 1 ≤ j - 1`,
which fails exactly when `i = j - 1`. So `L_k L_{k+1} = L_{k+1} L_k` is the real
content, not a base case that falls out. Found by writing the proof, not by
reasoning about it — the far case looked free until the index arithmetic was on
screen.

**What stands:** `qJM_commute` is **not** blocked on the general seminormal rep,
and its in-file comment saying so is wrong. Everything above is proved from the
Hecke relations alone.

**The residual, now sharply localised.** One identity in the subalgebra
generated by `A = L_k` and `s = σ_k`: `A s A s = s A s A`. Available inputs:
`σ_quadratic` (`s² = (q−qi)s + qi·q`), `σ_braid`, `σ_commute`, and
`A = σ_{k-1} L_{k-1} σ_{k-1}` with `σ_k` commuting with everything in `L_{k-1}`.
That is a far smaller and better-defined target than "wait for
`hoefsmit_seminormal_rep`", and closing it closes `qJM_commute` outright via
`qJM_commute_of_adjacent`, with `barSymJMSum_central` behind it.


### Adjacent case: reduced, k=1 closed, and the obstruction named (2026-08-16, later still)

Three more sorry-free axiom-clean theorems in `QJucysMurphy.lean`:

* **`adjacent_reduce`** — both sides of `L_k L_{k+1} = L_{k+1} L_k` collapse,
  from braid + `σ_k B = B σ_k` alone, to one word conjugated by `s`. The
  adjacent case ⟺ `s` commutes with `X = t s B t s B t`.
* **`braid_pow_three`** — the residual at `B = 1` is `(ts)³ = (st)³`.
* **`qJM_one_two_commute`** — **`L_1 L_2 = L_2 L_1`, unconditional.** No
  quadratic relation, no representation. First adjacent instance closed.

**The obstruction, named.** The general residual is
`B · t s B t s = t · B t s B t` — left word starts with `B`, right with `t`.
That needs `B` to move past `t`, and `s B = B s` gives no such permission
(`L_{k-1}` and `σ_{k-1}` do **not** commute). So a general proof must use
`σ_quadratic`, or structure of `L_{k-1}` beyond its `σ_k`-commutation. This is
a fact about these hypotheses, not a claim the adjacent case is hard — `k = 1`
closes.

**Method note for whoever continues.** I first tried to settle `k = 1` in the
braid group via the `SL₂(ℤ)` representation; both sides came out `-I`, which
proves nothing — that representation's kernel is the centre of `B₃`, so it is
not faithful and cannot distinguish the two products. The pure-braid argument
(`L_1 L_2 = A₁₂A₁₃A₂₃ = Δ²`, central) is the one that actually decides it, and
the Lean proof is the direct braid rewrite, not either of those.

**Score so far on this branch:** 5 theorems, all sorry-free and axiom-clean.
Two of the four sorries (`qJM_commute`, `barSymJMSum_central`) now hang on one
explicit identity at general `k`, with `k = 1` done.


### ✅ `qJM_commute` PROVED — sorry discharged (2026-08-16)

`qJM_commute` no longer carries a sorry. Axiom-clean throughout
(`[propext, Quot.sound]`, no `sorryAx`), `lean`-direct exit 0.

* **`adjacent_step`** — the adjacent case at `k` follows from the adjacent case
  at `k-1`, using braid + `σ_k`-commutation and **nothing else**. No
  invertibility, no quadratic relation, no representation.
* **`qJM_adjacent`** — induction on `k`, base `L_0 = 1`.
* **`qJM_commute_proved`** — pairwise commutativity via
  `qJM_commute_of_adjacent`.

**🔻 Correcting my own note from earlier today.** I wrote that the general
residual "needs `B` to move past `t`, and `s B = B s` gives no such permission",
concluding a proof must use `σ_quadratic` **or** structure of `L_{k-1}` beyond
its `σ_k`-commutation. The first half was right; the answer was the *second*
disjunct — and the structure needed is simply **the previous adjacent instance**,
which any induction already holds. I had written that disjunct as a distant
possibility rather than the obvious next thing to try, and it cost a turn.

**The original GAP comment was wrong, as suspected.** It read *"requires the
seminormal diagonalisation (bean `qou-im9l` / SW-4 residual)"*. Nothing in the
proof mentions a representation. An agent trusting it would have waited on
`hoefsmit_seminormal_rep`, which is still open and much harder.

**Also learned:** `hi : i ≤ n` and `hj : j ≤ n` are unnecessary — the statement
holds for **all** `i, j`, because the recursion freezes above `n`. Left in the
public signature rather than changing it.

**Branch score: 8 theorems, all sorry-free and axiom-clean; one GAP closed.**
Remaining in the file: `barSymJMSum_block_eigenvalue` (not provable as stated —
`q ≠ 0` vs `seminormalRep`'s `0 < q ∧ q ≠ 1`; owner question) and
`barSymJMSum_central`, which named `qJM_commute` as its blocker — now available.


### `barSymJMSum_central`: the crux found, the GAP note wrong again (2026-08-16)

Two more sorry-free axiom-clean theorems:

* **`pair_comm`** — in any algebra whose quadratic relation has constant term
  `1`, `s` commutes with `A + s A s`.
* **`qJM_pair_comm`** — the instance: **`σ_i` commutes with `L_i + L_{i+1}`**,
  given `q·qi = 1`. Since `L_{i+1} = σ_i L_i σ_i`, those two terms of the sum
  are exactly `A + s A s`. **Neither summand commutes with `σ_i` alone** — this
  is why a *sum* is central when its summands are not, and it was not
  identified anywhere in the corpus.

**🔻 The GAP note names the wrong blocker — third time today.** It says
centrality needs *"`qJM_commute` plus the σ_i–L_k commutation relations"*.
`qJM_commute` is now proved and **does not bear on this at all**: it is **L–L**
commutation, centrality is a **σ–L** question. Anyone who closed `qJM_commute`
expecting this to fall out would have found nothing had moved.

What centrality actually needs, for fixed `i`:

| terms | status |
|---|---|
| `L_k`, `k ≤ i-1` | **have** — `qJM_comm_sigma` |
| `L_i + L_{i+1}` | **have** — `qJM_pair_comm` |
| `L_k`, `k ≥ i+2` | **OPEN** |

`q·qi = 1` is not incidental: the computation leaves a residue
`(1 − q·qi)(sA − As)`, so it is exactly the standard Hecke normalisation that
makes the pair work. `Hecke.σUnit` carries the same hypothesis.

**NOT claimed: that `barSymJMSum_central` is nearly done.** The third row is
real work. `L_k` for `k ≥ i+2` is built from generators *including* `σ_i`, and
at `k = i+2` the outer generator `σ_{i+1}` is **adjacent** to `σ_i`, so far
commutation does not reach it. Classically, conjugation by `s_i` permutes the
transpositions `(j,k)` with `j < k` among themselves whenever `k ≥ i+2`; the
q-analogue of that argument is what is missing. The inverse family `L_k⁻¹`
needs the same treatment with `σ⁻¹`.

**Branch score: 10 theorems, all sorry-free and axiom-clean; one GAP closed
(`qJM_commute`); one GAP reduced to a single named row.**


### All three commutation rows now proved (2026-08-16)

**`qJM_comm_sigma_high`** — `σ_i` commutes with `L_k` for every `k ≥ i+2`.
Sorry-free, axiom-clean.

| terms | status |
|---|---|
| `L_k`, `k ≤ i-1` | **have** — `qJM_comm_sigma` |
| `L_i + L_{i+1}` | **have** — `qJM_pair_comm` (needs `q·qi = 1`) |
| `L_k`, `k ≥ i+2` | **have** — `qJM_comm_sigma_high` |

The base case `k = i+2` is the whole content and is **not** far commutation:
`L_{i+2} = σ_{i+1} σ_i L_i σ_i σ_{i+1}`, and `σ_{i+1}` is **adjacent** to
`σ_i`. It closes on the **braid relation** — the two `σ_{i+1}` conjugations
absorb the adjacency — plus `σ_{i+1}` commuting with `L_i`, which
`qJM_comm_sigma` supplies at exactly that index. The step for `k ≥ i+3` is
ordinary far commutation.

**Prediction I got wrong:** I expected this row to be the harder of the two and
to need `q·qi = 1` as well. It needs **no quadratic relation at all** — it is
the *easier* row. Only the pair row needs the normalisation.

**Boundary caught while stating it:** the claim is **false** without `i+1 < n`.
At `i = n-1` the recursion has frozen, `L_{i+2} = L_{i+1} = σ_i L_i σ_i`, and
the claim would require `σ_i` to commute with `L_i` — precisely the excluded
case. Harmless for the sum (`k ≤ n` and `k ≥ i+2` force `i+1 < n`), but the
hypothesis must be present.

**What remains for `barSymJMSum_central` is no longer a missing commutation:**
(a) the `Finset` assembly splitting `range (n+1)` into `{i, i+1}` and its
complement, and (b) the **inverse family** `L_k⁻¹`, needing the same three rows
run against `qJMInv` / `σ⁻¹`.

**Branch score: 11 theorems, all sorry-free and axiom-clean; one GAP closed
(`qJM_commute`); one GAP reduced from three open commutations to assembly +
the inverse half.**


### The `L`-half of `barSymJMSum_central` is done (2026-08-16)

* **`qJM_sum_comm_sigma`** — **`Σ_{k≤n} L_k` is central.** The `Finset`
  assembly: split `range (n+1)` into `{i, i+1}` and its complement; the pair
  takes `qJM_pair_comm`, every other `k` is `≤ i-1` or `≥ i+2` and takes one of
  the other two rows.
* **`σInv_quadratic`** — `σ⁻¹` obeys the same quadratic with `d ↦ -d`, i.e.
  `(qi−q)·σ⁻¹ + 1` — exactly the shape `pair_comm` consumes.
* **`comm_σInv_iff`** — commuting with `σ_i` and with `σ_i⁻¹` are the **same
  condition**, since `σInv = σ − (q−qi)•1` is a polynomial in `σ`.

The last two turn the remaining half into a *transfer*: `qJMInv` has the same
recursion as `qJM` with `σ ↦ σInv`, so the three rows re-run against it and
then bridge back to `σ`.

**Self-inflicted bug, recorded so it is not repeated.** I "fixed" a lint warning
by rewriting `rcases … <;> simp […] <;> omega` as
`rcases … <;> (simp […]; omega)`. That **broke the proof** — `simp` closes one
of the two branches outright, leaving `omega` with no goals. The `<;>` form was
correct and the linter hint was wrong for this proof. Reverted; do not re-apply.

**Branch score: 14 theorems, all sorry-free and axiom-clean. One GAP closed
(`qJM_commute`); `barSymJMSum_central` reduced to the inverse-family transfer.**
