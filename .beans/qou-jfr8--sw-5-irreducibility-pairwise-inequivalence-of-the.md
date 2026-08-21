---
# qou-jfr8
title: 'SW-5: irreducibility + pairwise inequivalence of the ρ_λ'
status: in-progress
type: task
priority: normal
created_at: 2026-08-02T19:33:07Z
updated_at: 2026-08-21T16:25:11Z
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


## TAKEOVER 2026-08-21 — stalled claim, pairwise inequivalence (q-DEFORMED)

Claiming under the stalled-claim policy. Prior holder's last commit on the
backing work was **aab0901121** (`lean(qou-jfr8): admissible-swap connectivity
transported`), 2026-08-19 19:39 UTC — **~44 h** stale, against a 3 h threshold.
Confirmed genuinely idle rather than merely paused: `main` has moved 18 commits
since, **none** touching `SchurWeyl/` or mentioning `jfr8`, and there is no open
PR for it. (My previous turn read the same silence as a fleet-wide pause; that
reading is retired — the fleet is demonstrably active again.)

Continuing from `main`, not from any sibling branch. Nothing force-pushed.

**Scope taken: pairwise inequivalence only.** Irreducibility (range form) is
landed; I am not reopening it.

### Corpus-grep before declaring it open (the step I skipped on `qou-gjg6`)

`BraidKnot/SpechtClassification.specht_pairwise_noniso` **does** prove pairwise
non-isomorphism — but for a **different object**: Specht modules over `k[S_n]`
at **q = 1**, as `Representation k (Perm (Fin n))`, via the dominance-order
route (`dom_of_intertwiner` / `spechtIso_imp_dom_both`). The q-deformed
`ρ_λ : Hecke ℝ q q⁻¹ n →ₐ[ℝ] Matrix (SYT λ) (SYT λ) ℝ` is not covered by it, and
nothing in `SchurWeyl/` states it. Genuinely open — and the owner has confirmed
the q-deformed case is the target.

The q=1 file is still useful as a **precedent for the Lean shape**: it declares
its own `IsRepIso` intertwiner predicate rather than reaching for `FDRep`,
explicitly to avoid `Module.Finite` plumbing. I am mirroring that choice on the
algebra-hom side.

### Route, and an honest split between what is cheap and what is true

The JM diagonalisation makes the dominance-order argument unnecessary here.
`ρ_λ(L_k)` is diagonal with entry `q^{2·cellContent (cellOf T k)}` at `T`
(`seminormalRep_qJM`), so similarity invariants read off contents directly.

**Stage 1 (cheap, conditional).** `Θ = barSymJMSum` is central and
`ρ_λ(Θ) = cellContentCoshSum λ q · 1` (`seminormalRep_barSymJMSum`, proved). A
scalar is a similarity invariant, so
`cellContentCoshSum λ q ≠ cellContentCoshSum ν q ⟹ ρ_λ ≇ ρ_ν`.

**Stage 1 does NOT give the unconditional statement, and I will not dress it up
as if it did.** At a *fixed real* q the cosh-sum is one number, and two distinct
shapes could collide numerically. As Laurent polynomials in q the two sums
differ (the content multisets differ, and the coefficients are positive), so
they agree for at most finitely many q — but "at most finitely many" is not
"not at q₀", and this file evaluates at a fixed q.

**Stage 2 (the real content).** Unconditional separation needs the eigenvalue
**multiset**, not a sum. From an intertwiner, `ρ_λ(L_k) ~ ρ_ν(L_k)` for each k;
both are diagonal, so the diagonal multisets agree; `zpow_injective_of_not_
root_of_unity` (already landed) turns equal eigenvalues into equal contents; and
the disjoint union over k is `d_λ` copies of the content multiset of λ. With
`d_λ = d_ν` forced by equal matrix size, the content multisets agree — and the
content multiset determines the partition.

**The unconditional statement is TRUE**, so Stage 2 is not chasing a mirage:
`H_n(q)` over ℝ is semisimple whenever q is not a root of unity of order ≤ n,
which `q ≠ 0 ∧ q² ≠ 1` gives here, and the ρ_λ are then the full list of
irreducibles. What is open is only the Lean.

**Anticipated residual:** *"the content multiset determines the Young diagram"*
is classical but I have not found it in the corpus. If it turns out to be the
expensive piece, it gets its own bean rather than a `sorry`.


## Stage 1 + 2 LANDED (PR #5370) — and the route that removes the condition

`QOU/SchurWeyl/SeminormalInequivalence.lean`, 7 theorems, all sorry-free and
axiom-clean `[propext, Classical.choice, Quot.sound]`, wired into `QOU.lean`.

**Stage 1** — `MatRepEquiv`, `MatRepEquiv.scalar_eq`,
`seminormalRep_not_matRepEquiv_of_contentCoshSum_ne`. Conditional, as scoped.

**Stage 2** — `conj_eq`, `trace_eq`, `card_eq`, `seminormalRep_jmPowSum`,
`contentPowSum_eq_of_matRepEquiv`.

### Correcting my own plan in the takeover note above

I wrote that stage 2 needs *"the eigenvalue multiset of each `ρ(L_k)`"*, and
budgeted for either Newton's identities or `charpoly` similarity-invariance.
**Neither is needed, and the multiset never has to be handled as a multiset.**

Sum over `k` FIRST. `Σ_k L_k^m` has a *constant* diagonal — the cell sweep
(`sum_cellOf_range`) makes every tableau give the same value — so it acts by a
**scalar**, and `scalar_eq` (already proved for stage 1) applies verbatim at
every `m`. No per-`k` multiset, no charpoly, no power-sum-to-multiset lemma.
`seminormalRep_jmPowSum` is `seminormalRep_barSymJMSum` with the bar-symmetrised
`m = ±1` combination replaced by an arbitrary power, and the proof is the same
four lines plus `Matrix.diagonal_pow`.

### The genericity hypothesis does a second job

Writing `t = q^{2m}`, the family says the content generating functions
`Σ_{c∈μ} t^c` and `Σ_{c∈ν} t^c` agree at every point of `{q², q⁴, q⁶, …}`.
`q ≠ 0` and `q² ≠ 1` make `q²` positive and `≠ 1`, so its powers are strictly
monotone and those points are **pairwise distinct** — infinitely many. A Laurent
polynomial with infinitely many roots vanishes.

Worth noting because elsewhere in this arc `q² ≠ 1` is used only for `zpow`
injectivity (`zpow_injective_of_not_root_of_unity`). Here it buys something
different: an infinite supply of distinct evaluation points. Same hypothesis,
unrelated mechanism.

### Genuinely open — two steps, neither hidden as a `sorry`

1. **Infinitely many roots ⟹ coefficient equality.** Clear `t^{-K}` by
   multiplying through by `t^K` (`K = max |content|`), then
   `Polynomial.eq_zero_of_infinite_isRoot`. The infinitude comes from strict
   monotonicity of `m ↦ (q²)^m`.
2. **Content multiset determines the Young diagram.** Classical; corpus-grepped
   and **not found** — `SchurWeyl/`, `BraidKnot/`, `Mathlib/` all negative. This
   is the one I would budget for. If it is expensive it gets its own bean.

The file states both in its stage-2 docstring and proves neither. It proves what
it says and no more; nothing in it is a placeholder.

### Scope check on what is claimed

`seminormalRep_not_matRepEquiv_of_contentCoshSum_ne` is **not** `μ ≠ ν ⟹
ρ_μ ≇ ρ_ν` and must not be cited as if it were. Scope-(a): it separates exactly
those pairs whose content-cosh sums differ *at this q*. The unconditional
statement is **true** (`H_n(q)/ℝ` is semisimple away from roots of unity of
order ≤ n, and the ρ_λ are then the complete pairwise-inequivalent family) — the
gap is formalisation, not mathematics.


## CORRECTION 2026-08-21 — item 1 of "Remaining" is CLOSED, and its prescribed route was wrong

The "Remaining" list above says **two** steps are open. Only **one** is.

**Item 1 (infinitely many roots ⟹ coefficient equality) is DONE** — landed in
this branch, sorry-free: `poly_eq_zero_of_eval_pow`, `coeff_sum_X_pow`,
`card_filter_eq_of_powSum_eq`, and the assembled
`contentCount_eq_of_matRepEquiv`. An equivalence now forces the two shapes to
have the same number of cells of **every** content.

**And the route I wrote into that item is not the one that worked.** It said:

> *Clear `t^{-K}` by multiplying through by `t^K` (`K = max |content|`), then
> `Polynomial.eq_zero_of_infinite_isRoot`.*

The `t^K` clearing does **not** belong in the general lemma.
`card_filter_eq_of_powSum_eq` is stated with **`ℕ` exponents**, so it never sees
a shift at all — the ℤ-valued contents are moved into `ℕ` at the *call site*
(`shiftedContent`, `pow_shiftedContent`), where the row bound
`row_lt_card` supplies the lower bound. Putting the shift inside the lemma would
have coupled a general fact about power sums to Young-diagram specifics for no
reason. Only `Polynomial.eq_zero_of_infinite_isRoot` survives from that sketch.

Two things found along the way that the sketch did not anticipate:

* **`q² ≠ 1` does a second, unrelated job.** Elsewhere in this arc it gives
  injectivity of `c ↦ q^{2c}`. In the roots argument it makes `q²` positive and
  `≠ 1`, hence its powers strictly monotone, hence the evaluation points
  pairwise distinct. Same hypothesis, different mechanism — do not conflate them
  when re-scoping the genericity.
* **The `d + n < 0` branch is not bookkeeping.** There the shifted filter can be
  nonempty while the content filter is empty, so the translation iff genuinely
  *fails*; both sides are shown empty directly instead.

**Item 2 (content multiset ⟹ Young diagram) now has its own bean: `qou-tho9`**,
with the corpus-grep and one real lead (`TLContentStratification` already gives
the *support* half — `numCols` and `length` — sorry-free, on `Partition` rather
than `YoungDiagram`).

**This entry exists because the list above was stale within one commit of being
written.** Same failure class as the `qou-gjg6` HLF note: a plan recorded as
"open" that a later commit closed, left sitting where the next agent would trust
it. Read the "Remaining" list above only through this correction.


## SECOND HALF CLOSED 2026-08-21 — pairwise inequivalence is unconditional

`seminormalRep_not_matRepEquiv_of_ne` (PR #5370), sorry-free and axiom-clean:
`μ ≠ ν → ¬ MatRepEquiv (seminormalRep … μ) (seminormalRep … ν)`, with no
hypothesis beyond `μ ≠ ν` and the genericity `seminormalRep` already carries.

Both residuals listed under "Remaining" are now closed:

1. **Infinitely many roots ⟹ coefficient equality** — closed earlier this
   session (see the CORRECTION entry above; the route I prescribed was not the
   one used).
2. **Content multiset ⟹ Young diagram** — closed as `qou-tho9`, in the same
   session it was opened. Its own route sketch was also wrong: diagonals of a
   Young diagram are downward-closed, so the diagonal *length* decides
   membership outright — no greedy row recovery, no Frobenius coordinates, no
   `Partition`↔`YoungDiagram` bridge.

**Calibration note.** I sized these two backwards. The roots step, called the
cheaper half, took several iterations; the content-multiset step, the one I said
I would budget for, compiled first try in ~90 lines. I had read "classical, not
in the corpus" as a difficulty signal — it is not one, when the object carries as
much structure as a Young diagram.

**What is left on this bean.** The `AlgHom.range = ⊤` irreducibility half was
already landed by the prior holder before the takeover. With inequivalence now
closed, check whether anything in the bean's own "Remaining" list from the
irreducibility side still stands before marking `qou-jfr8` complete — I have not
re-verified that half and am not claiming it.


## Re-verified the IRREDUCIBILITY half 2026-08-21 — it is NOT closed, and its plan has a hole

I said I would check this before anyone marks `qou-jfr8` complete. Measured:

**`AlgHom.range (seminormalRep …) = ⊤` does not exist anywhere.** The phrase
occurs exactly once in the tree — in `SeminormalRange.lean`'s header, as the
*target* ("Toward SW-5 in the range form"). `DiagonalSeparation.eq_top_of_single_mem`
is the abstract "all matrix units ⟹ ⊤"; nothing instantiates it at
`seminormalRep`. So the bean's "THE ONE REMAINING GAP" is still open, and
connectivity landing (`syt_swapStep_connected`, #5321) did **not** close it.

**The plan for that gap has an unverified premise.** It reads:

> a chain `T = T_0, …, T_m = T'` where each step is an admissible swap, **so
> that genMat's off-diagonal entry offDiag is nonzero at each step**

That "so that" does not follow. `offDiag q (-1) = 0` is a `@[simp]` lemma in
`SeminormalRep.lean` — the entry genuinely vanishes — and `genMat_ne_scalar`'s
own docstring already flags it: *"this does not go through `offDiag ≠ 0` at the
moved entry: that can genuinely vanish."* `genMat_ne_scalar` survives by reading
the **partner** column instead, which is available to it because it only needs
*one* nonzero entry. The chain argument needs a **direction**, and that is a
strictly stronger demand.

**The crux, stated precisely.** `offDiag_mul_neg` gives
`offDiag q d · offDiag q (-d) = 1 + a(d)·a(-d)`, so *both* entries of a pair are
nonzero iff `1 + a(d)a(-d) ≠ 0`. At `d = ±1` that is exactly `0`
(`seminormalParam_mul_neg_one`). So the gap needs **two** lemmas, neither in the
corpus:

1. **`SwapAdmissible T k → 2 ≤ |axialDist T k|`.** Grepped: no bound on
   `|axialDist|` for admissible swaps exists (`natAbs`/`abs`/`2 ≤` searches all
   negative). Note `axialDist_trichotomy` does *not* give this — it says same-row
   ⟹ `+1` and same-column ⟹ `−1`, not the converse.
2. **`1 + a(d)a(-d) ≠ 0` for `|d| ≥ 2`.**

**Why this matters beyond bookkeeping.** Without (1), each swap-adjacent pair
supplies only **one** guaranteed directed edge — the direction out of the
tableau whose `axialDist` is `≥ 0`, since the other entry is `offDiag` of a
negative distance. Exactly one of the pair has `d ≥ 0` (`axialDist_ne_zero`
rules out the tie), so the induced digraph has one arc per undirected edge and
is not strongly connected in general. Matrix units compose along *directed*
paths (`single a b · single b c = single a c`), so one-way arcs do not deliver
every `single T' T 1`. The undirected connectivity that landed is genuinely not
enough by itself.

I believe (1) is true — a hand-check of `d = -1` with distinct rows and columns
runs into a cell squeezed between `k` and `k+1` — but I have **not** proved it
and am not asserting it. It is the next concrete step on this half.

**So: do not mark `qou-jfr8` complete.** The inequivalence half is closed; the
irreducibility half is one named lemma-pair short of it, and the shortfall is in
the *plan*, not merely in the typing.
