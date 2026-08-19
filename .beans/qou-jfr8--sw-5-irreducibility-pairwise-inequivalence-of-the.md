---
# qou-jfr8
title: 'SW-5: irreducibility + pairwise inequivalence of the ρ_λ'
status: in-progress
type: task
priority: normal
created_at: 2026-08-02T19:33:07Z
updated_at: 2026-08-19T20:29:53Z
parent: qou-59vq
blocked_by:
    - qou-u86i
---

Each Hoefsmit rep is irreducible and ρ_λ ≇ ρ_μ for λ≠μ (distinct central characters). Ref: [wenzl1988].

## ✅ Concrete (2,1) case PROVED (2026-08-10) — sorry-free, axiom-clean

[`QOU/SchurWeyl/Irreducibility.lean`](https://github.com/litlfred/qou/blob/claude/agent-task-662242-vag458/content/quantum-observable-universe/lean/QOU/SchurWeyl/Irreducibility.lean):
`seminormal21_no_common_eigenvector` (q≠0) — S0, S1 have no common eigenvector,
hence no common 1-dim invariant subspace, hence the 2-dim shape-(2,1) rep is
IRREDUCIBLE. Proof: an S0-eigenvector is axis-aligned (distinct eigenvalues
q≠-q⁻¹ via q+q⁻¹≠0), but S1 fixes neither axis (c₀₁=1, c₁₀=(q⁴+q²+1)/(q²+1)²>0).
lean-direct EXIT=0; axioms [propext, Classical.choice, Quot.sound]; wired into QOU.lean.

General-λ irreducibility depends on the general seminormal construction — stays
with residual bean qou-im9l (needs SW-4-gen first).


## Re-scoped 2026-08-19 — the general case is now REACHABLE, and the enabling input just landed

Prior state: only the concrete shape-(2,1) case
(`Irreducibility.seminormal21_no_common_eigenvector`, q != 0). The general case
looked blocked on the general seminormal rep. **It no longer is.** Two things
landed since:

- `hoefsmit_seminormal_rep` for all lambda (#5279, qou-im9l) — the reps exist.
- `seminormalRep_qJM` (#5290, qou-t8qh) — **Ram Thm 4.1**: the q-Jucys-Murphy
  element L_k acts DIAGONALLY on the SYT basis with entry q^{2.cellContent} at
  the cell holding k+1.

Ram 4.1 is exactly the classical engine for general irreducibility, and it is now
available as a proved lemma rather than a plan:

1. The JM family {L_1..L_n} acts diagonally, so it generates a commutative
   subalgebra whose joint eigenspaces are spanned by subsets of the SYT basis.
2. **Separation**: distinct SYT of the same shape have distinct content
   *sequences* (c(T,1),...,c(T,n)) — a standard tableau is determined by its
   content vector. Hence the joint eigenvalue sequences (q^{2c(T,k)})_k are
   pairwise distinct at generic q, so each joint eigenspace is ONE line.
   => every H_n(q)-invariant subspace is a span of a SUBSET of the SYT basis.
3. **Connectivity**: an invariant subspace containing T also contains s_k.T
   whenever the swap is admissible, since genMat's off-diagonal entry is nonzero
   (`offDiag`, and `genMat_ne_scalar`). SYT of a fixed shape are connected under
   admissible swaps.
   => the only invariant subspaces are 0 and everything. IRREDUCIBLE.

Step 2 is the one with real content and is where the work is: *content vector
determines the tableau*, plus the genericity that q^{2a} = q^{2b} implies a = b
(which is exactly the q^2 not a root of unity hypothesis already carried by
`seminormalRep`). Step 3 needs SYT connectivity under admissible swaps — check
`SytRowSuperstandard.syt_all_connect_to_some` and
`SytAdmissible.exists_swapAdmissible_of_one_lt_card` before building it.

Pairwise inequivalence rho_lambda !=~ rho_mu for lambda != mu is the second half and
falls out of the same separation: the L_k eigenvalue MULTISET is the multiset of
cell contents of lambda, which determines lambda.

CLAIMED by this session 2026-08-19.


## Progress 2026-08-19 (PR #5307) — separation half LANDED sorry-free

**Corpus-grep finding that changed the plan:** step 2 (content tuple determines
the tableau) was ALREADY PROVED in the corpus as
`BraidKnot.JucysMurphy.syt_content_tuple_injective` — the Okounkov-Vershik stack
under BraidKnot/, sorry-free, 950 lines. I nearly rebuilt it. What was actually
missing is the TRANSLATION between the repo's two StandardYoungTableau types
(QOU.Mathlib.* used by SchurWeyl vs QOU.BraidKnot.* used by OV), which differ by
an off-by-one label convention.

Landed:
- `SytContentTuple.lean`: `cellOf_eq_tableauCellEquiv` (the label
  correspondence across the existing type bridge) + `syt_eq_of_cellContent_eq`
  (separation in the cellOf API).
- `SeminormalSimpleSpectrum.lean`: `zpow_injective_of_not_root_of_unity`,
  `seminormalRep_qJM_diag`, and `seminormalRep_qJM_spectrum_injective` — the
  joint L_k eigenvalue tuple determines T.

All sorry-free, axioms [propext, Classical.choice, Quot.sound].

**Sharpening of the plan:** 'Ram 4.1 gives diagonal' is NOT the separation. A
diagonal matrix with a repeated entry has a plane of eigenvectors. Diagonal +
simple spectrum is what forces joint eigenspaces to be single coordinate lines.
The bean's step 1/step 2 split above was right but the writeup blurred them.

## Remaining

1. **Connectivity transport.** `syt_adjacentSwap_connected` /
   `syt_all_connect_to_some` exist sorry-free on the BraidKnot side; transport
   them the same way `SytContentTuple` transported separation.
2. **The invariant-subspace step.** T in an invariant subspace => s_k.T in it,
   because genMat's off-diagonal entry `offDiag` is nonzero.
3. **DESIGN QUESTION, not yet settled:** what should 'irreducible' BE in Lean
   here? `AlgHom.range (seminormalRep ...) = top` is the form SW-7 actually
   consumes and avoids setting up a Module-over-the-algebra structure. Reaching
   it needs Lagrange interpolation on the simple spectrum to build the diagonal
   matrix units E_TT from the L_k images, then connectivity to get the
   off-diagonal units. That interpolation is the largest single remaining piece.
4. Pairwise inequivalence rho_lambda !=~ rho_mu — the eigenvalue MULTISET is the
   content multiset of lambda, which determines lambda. Not started.

## Do not duplicate

The five `cellContent` definitions in the corpus (SchurWeyl/HoefsmitRep,
BraidKnot/JucysMurphy, MathlibExt/QPartitionCombinatorics,
MathlibExt/WenzlSchurElement, HeckeAlgebra/JonesMarkovWenzl) are a real
consolidation target but are NOT part of this bean. Filed as an observation
only.


## Range form chosen (owner, 2026-08-19) — skeleton closed at both ends

Target settled as `AlgHom.range (seminormalRep ...) = top`. Landed sorry-free,
axiom-clean:

- `DiagonalSeparation.single_self_mem_of_separating` — abstract: a subalgebra
  containing a DIAGONAL family whose entry-tuples SEPARATE the index set
  contains every diagonal matrix unit. Finite-set Lagrange interpolation as a
  product. No Hecke or tableau content, so it checks on its own terms.
- `DiagonalSeparation.eq_top_of_single_mem` — matrix units generate everything.
- `SeminormalRange.diagonal_seminormalRep_qJM` — rho(L_k) is its own diagonal.
- `SeminormalRange.single_self_mem_range` — every DIAGONAL unit is in the image.
- `SeminormalRange.single_mem_range_of_entry_ne_zero` — a nonzero (T',T) entry
  anywhere in the image promotes to the off-diagonal unit single T' T 1.

**Lean shape note worth keeping:** matrices are NOT a `CommMonoid`, so
`Finset.prod` cannot be taken over them even when the particular matrices commute.
The interpolation product is taken in the function ring (iota -> R) with
`diagonal` applied once, and membership recovered by induction on the index set
through diagonal's multiplicativity. First attempt failed on exactly this.

## THE ONE REMAINING GAP

Supplying a nonzero (T', T) entry for EVERY pair. Concretely:

  for T != T', a chain T = T_0, T_1, ..., T_m = T' where each step is an
  admissible swap, so that genMat's off-diagonal entry offDiag is nonzero at
  each step; then compose the units (single T'' T' 1 * single T' T 1 =
  single T'' T 1).

`QOU.BraidKnot.JucysMurphy.syt_adjacentSwap_connected` proves the connectivity
sorry-free. Transport is HARDER than SytContentTuple was: that one only had to
match LABEL conventions (off-by-one), this one has to match the SWAP notions --
BraidKnot's `AdjacentSwapStep` / `swapCellsSYT` against SchurWeyl's
`SwapAdmissible` / `swapTableau`. Budget accordingly; do not assume the same
5-line bridge works.

Pairwise inequivalence (rho_lambda !=~ rho_mu) still not started.


## Connectivity LANDED (PR #5321) — and my cost estimate was wrong in the good direction

`SytSwapTransport.lean`, sorry-free: `swapAdmissible_of_sq_axialDist_ne_one`,
`SwapStep`, `swapStep_of_adjacentSwapStep`, `syt_swapStep_connected`.

**Retracting the estimate in the previous entry.** I wrote that this transport
would be 'strictly larger' than SytContentTuple because the SWAP CONSTRUCTIONS
would have to be matched. They do not. `AdjacentSwapStep` is defined purely in
terms of CONTENT VECTORS and never mentions how the stepped-to tableau is built,
so the transport needs only swapTableau's content profile plus separation. The
lesson generalises: check whether the upstream definition is stated
extensionally before budgeting for a structural match.

## NEW OBSTRUCTION — the plan in this bean was wrong about the last step

Step 3 above says 'an invariant subspace containing T also contains s_k.T since
genMat's off-diagonal entry is nonzero (offDiag)'. **That is not automatic.**

    offDiag q d = if d < 0 then 1 + a(d).a(-d) else 1

so the entry is the plain 1 only on the NON-NEGATIVE branch, and
`offDiag q (-1) = 0`. SeminormalRep's own `genMat_ne_scalar` docstring flags
this: *'this does not go through offDiag != 0 at the moved entry: that can
genuinely vanish'*. Since axialDist (s_k.T) k = -axialDist T k, each admissible
pair yields exactly ONE oriented edge for free -- and one orientation per edge
does not give all ordered pairs single U V 1.

**The missing lemma: `offDiag q d != 0` for |d| >= 2, real q != 0, q^2 != 1.**

Derivation (do not re-derive): with y = q^2 > 0, the vanishing condition
1 + a(d)a(-d) = 0 is equivalent to (y-1)^2 . y^(e-1) = (y^e - 1)^2 with e = |d|.
Factoring y^e - 1 = (y-1)(1 + y + ... + y^(e-1)) reduces it to
y^(e-1) = (1 + y + ... + y^(e-1))^2, and for y > 0 the sum exceeds y^((e-1)/2) --
term-by-term when e is odd (the middle power IS a term and the others are
positive), by AM-GM on the two middle terms when e is even. Only e = 1 solves it,
which is exactly the NON-admissible distance.

**Checked in EXACT RATIONALS, not floats** (121 rationals q x 12 distances):
0 mismatches between the direct form and the reduction, 0 vanishings at |d| >= 2,
and the driving inequality strictly positive throughout.

This is load-bearing mathematics, not plumbing: if offDiag DID vanish at an
admissible distance, the tableaux reachable in one direction would span an
invariant subspace and the representation would not be irreducible.

Formalising it is real analysis over zpow (the geometric-sum factorisation plus
the AM-GM step), not a bookkeeping lemma. It is the single remaining gap between
the current branch and range = top.


## SW-5 RANGE FORM PROVED (2026-08-19)

`seminormalRep_range_eq_top`: for every shape mu of size n+1 and every real q
with q != 0, q^2 != 1, the seminormal representation SURJECTS onto the full
matrix algebra M_{#SYT mu}(R). Sorry-free, axiom-clean. Children qou-qyy0 and
qou-x10g both closed.

This is Burnside-equivalent to irreducibility, in the form SW-7 (`qou-0h5k`)
consumes -- and it avoids standing up a module-over-the-algebra structure just to
state 'irreducible'.

**Still open in this bean:** pairwise inequivalence rho_lambda !=~ rho_mu for
lambda != mu. Not started. The route is the same separation: the L_k eigenvalue
MULTISET is the multiset of cell contents of lambda, which determines lambda.


## Inequivalence half — the corpus's central element is DISPROVED for this purpose

`SeminormalInequivalence.lean` (PR #5331), sorry-free:

- `coshSum_transpose` — **`barSymJMSum` / `cellContentCoshSum` is TRANSPOSE-INVARIANT.**
  Transposing negates every content and q^{2c}+q^{-2c} is even in c, so the
  bar-symmetrised sum takes the same value on lambda and lambda' at EVERY q.
  It therefore cannot be the separating central character. Now a theorem, not
  an observation. Measured in exact rationals: at n=7 the 15 partitions give 8
  distinct values and every collision is exactly a transpose pair.
- `seminormalRep_jmSum` — the UNSYMMETRISED Murphy power sum acts by
  sum_c q^{2c}. Central under the same hypothesis via `qJM_sum_comm_sigma'`
  (already on main, sorry-free). Not even in c, so not transpose-blind.
- `contentSum_eq_of_intertwiner` — any intertwining algebra isomorphism forces
  the two content sums to agree. Contrapositive: differing content sums =>
  inequivalent.

## What is deliberately NOT claimed

That distinct partitions of n have distinct `sum_c q^{2c}` **at a given real q**.
The sums are distinct Laurent polynomials in q^2 (the content multiset
determines the partition), but a nonzero integer Laurent polynomial CAN vanish
at a real q that is not a root of unity, so `q != 0 and q^2 != 1` do not suffice.
Separation held at every sampled q up to n=9 in exact arithmetic. That is
evidence, not proof, and the file says so in those words.

**This is the honest residual of SW-5.** The structural half (range = top) is
proved; the arithmetic half is a separate question about when an integer Laurent
polynomial vanishes at a real point, and it should not be waved through.
