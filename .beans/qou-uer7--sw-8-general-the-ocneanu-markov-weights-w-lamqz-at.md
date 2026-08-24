---
# qou-uer7
title: 'SW-8 general: the Ocneanu Markov weights w_lam(q,z) at every n'
status: in-progress
type: task
priority: normal
created_at: 2026-08-23T16:51:49Z
updated_at: 2026-08-24T00:02:03Z
parent: qou-59vq
---

## What SW-7 left, and what it did not

`heckeWedderburnDataOfWeights` (PR to follow) builds `HeckeWedderburnData` at
EVERY n from `heckeWedderburn` (SW-7, merged c18a357142). But the weight family
`w : Partition (n+1) -> R` is a **parameter of that construction, not a result of
it**. `markov_eq` holds by `rfl` because `markov` is DEFINED as
`sum_lam w_lam chi_lam`. So the structural half is done and the content is not.

## The actual open item

Which `w` makes the functional a genuine MARKOV TRACE. Two properties single it
out:

- trace property: `tr(xy) = tr(yx)`;
- Markov condition: `tr(x . sigma_n) = z . tr(x)`.

At n=3 both are proved — `HeckeMarkov3.markovWeight0/1/2 (q z)` with
`markovWeights_markov_sigma1`. At general n they are open. The classical answer is
Ocneanu's weight, a ratio of q-hook products over the diagram, and getting it
will want the branching rule rather than more linear algebra.

## Do not read the structure instance as delivering this

`heckeWedderburnDataOfWeights` will happily accept ANY `w`, including nonsense,
and the resulting term is still a well-typed `HeckeWedderburnData`. A downstream
consumer could therefore call `markov` a Markov trace without it being one. The
naming keeps `weight` visibly an input and the module docstring says so; anyone
wiring this into an R2 result should supply a `w` with the two properties PROVED,
not merely chosen.


## Attempted 2026-08-23 — NOT closed; the corpus's candidate formula FAILS validation

Went to formalise the general weight and validated the existing candidate first.
It does not hold up.

### Established exactly (sympy over Q(q,z), no floats)

1. **The normalisation is `sum_lam d_lam . w_lam = 1`, not `sum_lam w_lam = 1`.**
   Verified against the Lean-proved n=3 weights. This is what `markovTrace3_one`
   encodes (trace of the identity in block lam is d_lam) and what
   `HeckeWedderburnData.markov_eq` expects. Landing exactly on 1 also
   cross-checks that the weights were transcribed correctly.
2. **The denominator of every proved weight IS the q-hook product**
   `prod_x [h(x)]_{q^2}`: (3) and (1^3) give [2]_{q^2}[3]_{q^2}, (2,1) gives
   [3]_{q^2}. The Ocneanu SHAPE is right at n=3.

### What fails

`computations/mass_at_3A_proper.py::jones_wenzl_weight` implements

    omega_lam = z^(n-1) prod_x (1 - z q^{2c(x)}) / (1 - q^{2h(x)})

and its docstring claims `sum_lam omega_lam = 1`. Across **160 convention
combinations** — exponent in {1,2}, q -> {q, q^2, -q, 1/q}, ten z-substitutions,
both plausible targets (w_lam and d_lam.w_lam) — it NEVER reproduces the proved
n=3 weights and NEVER sums to 1.

Probe: `computations/schurweyl/ocneanu_weight_validation.py` (exact arithmetic).

### Why nothing was formalised

The candidate is the only general formula in the corpus and it fails the one case
that is Lean-proved. Formalising it would launder a fit. This area already
produced a correction cycle (`qou-2tuv`) — a reason for more care, not less.

### Next honest step

DERIVE rather than recall: solve the defining conditions (trace property,
`tr(x.sigma_n) = z tr(x)`, normalisation) at n=4 in exact arithmetic, read the
numerator structure off against the hook-product denominator that IS confirmed,
and only then formalise.

**Separable finding:** the `jones_wenzl_weight` defect is a live bug in a
production compute path, independent of SW-8.


## Status 2026-08-23 — the weights at general n are DERIVED and partly Lean-proved (PR #5575)

Closed form, derived in exact Q(q,z) rather than recalled:

    W_lam(q,z) = prod_{(i,j) in lam} [ q^{2i}(q^2 - 1 - qz) + q^{2j+1} z ]
                 / prod_{(i,j) in lam} [ q^{2h(i,j)} - 1 ]

Lean (sorry-free, axiom-clean): `QOU/SchurWeyl/OcneanuWeight.lean` (generic `[Field R]`,
no R) + `OcneanuWeightMarkov3.lean` (the R comparisons). Reproduces `markovWeight0/1/2`
exactly; `Sum_lam d_lam W_lam = 1` at n=3 AND n=4 — the n=4 identity being the
out-of-sample one, since n<=3 cannot constrain the framing monomial at all.

Also proved: at convention D's `z = q^3/(q^2+1)`, every partition with >=3 rows has
weight ZERO. That z is the k=2 member of the family `z = q^{2k+1}/(1+q^2+...+q^{2k})`
killing content `-k`; convention C's `sqrt(q)/(q+1)` is not a member at any integer
content.

### The trap, for whoever picks this up

**Every partition of n <= 3 has distinct cell contents.** The first repeat is the two
content-0 cells of (2,2). So a weight formula fitted to n<=3 is off by a monomial and
looks correct — mine was, by q^2 on exactly (2,2), (3,2), (2,2,1). Any future work on
this must check at n >= 4.

### STILL OPEN — the reason this bean is not closed

The **Markov property at general n**: `tr(xy) = tr(yx)` and `tr(x sigma_n) = z tr(x)`
for the functional `Sum_lam W_lam chi_lam` built from this closed form. Verified
numerically (exactly, in Q(q,z)) through n=6, and cross-checked against the corpus's
independent linear-solve inversion at n=2..5 — but **not proved**.

Until it is proved, `heckeWedderburnDataOfWeights` is deliberately NOT instantiated with
`ocneanuWeight`. Doing so would let a consumer read the functional as a Markov trace on
the strength of a numerical check, which is what `HeckeWedderburnDataGeneral`'s own
docstring warns against. That instantiation is the next real deliverable and it needs the
theorem, not the probe.

Likely route: the branching identity `W_mu^(n) = Sum_{lam = mu+box} W_lam^(n+1)` is a
clean statement about the closed form alone (a hook-length/content telescoping) and
implies trace-consistency across the tower; combined with the q-JM diagonal action
(`seminormalRep_qJM_diag`, already proved) it should give the Markov condition without
ever assembling a seminormal matrix.

### Defects surfaced, beaned not fixed

- `qou-bsec` — `jones_wenzl_weight` is wrong and LIVE (mass_at_3A_proper.py:592).
- `qou-pc7l` — `ocneanu_weights.py` docstring declares convention C, code runs D.


## Update — the bridge to `schurPrincipal` is proved (same PR #5575)

`OcneanuWeightWenzl.lean`, sorry-free, axiom-clean, generic `[Field R]`:

    ocneanuWeight q (q^3/(q^2+1)) mu = schurPrincipal 2 (q^2) mu / (q^2+1)^|mu|

Why it matters: `QOU/QBeta/WenzlWeightVanishing.lean` names ONE external citation —
*"Wenzl's theorem, the external input and the only one, is that these ARE the
Ocneanu/Markov trace weights"* — and `docs/audits/2026-08-16-two-row-cap-proved-and-
deltalambda-magnitude.md` records that the two-row cap and everything built on it are proved
ABOUT `schurPrincipal`, so reading them as statements about the mass channel is that citation,
invisible to `#print axioms`.

The bridge **relocates** that citation (it does not discharge it) onto the single statement

    ocneanuWeight satisfies tr(x sigma_n) = z tr(x) at general n

about a formula that was derived from the Markov conditions and is Lean-proved to reproduce
the corpus's own proved n=3 weights. **Proving that one statement would discharge the corpus's
only external input here outright.** That makes it the highest-value open item on this bean,
not merely the next one.

## Discipline failure to record

I proved `ocneanuWeight_conventionD_eq_zero_of_three_rows` and grepped the corpus
**afterwards**. `schurPrincipal_eq_zero_iff` had been there since 2026-08-16, sorry-free and
more general (any level r), together with `wenzlLevel_conventionD`. Wrong order; the
corpus-grep checklist exists for exactly this. The duplicate is retained only because its
hypotheses are strictly weaker (no root-of-unity condition), and its docstring says all of
this. The sharper iff is now the corpus theorem transported along the bridge, not a second
proof.

## Convention D, restated cleanly

At `z_D`, `W_lam = s_lam(1, q^2) / [2]_{q^2}^n` — the normalised 2-variable principal Schur
specialisation. Verified against three mutually independent routes through n=8 (hook-content,
bialternant determinant, SSYT sum over entries in {1,2}); all identical. Consequences that then
stop being coincidences: the >=3-row vanishing is "s_lam in 2 variables is 0 for l(lam) > 2";
the normalisation `Sum_lam f^lam W_lam = 1` is the Schur expansion `p_1^n = Sum_lam f^lam
s_lam` at (1, q^2); and the branching identity is the **Pieri rule** `s_mu * e_1 = Sum_{lam =
mu + box} s_lam`.

That last point supersedes the "next step" recorded above. Proving branching directly as a
rational-function identity over addable corners is the hard road; it is Pieri in disguise, and
at convention D it collapses further to a 2-term identity over <=2-row partitions, since the
third addable corner (2,0) contributes zero.


## Update — branching at convention D is PROVED (same PR #5575)

`OcneanuWeightBranching.lean`, sorry-free, axiom-clean, generic `[Field R]`:

    ocneanuWeight q z_D (twoRow m k)
      = ocneanuWeight q z_D (twoRow (m+1) k) + ocneanuWeight q z_D (twoRow m (k+1))

plus the diagonal case k = m (where `twoRow m (m+1)` is not a partition, so only one term
survives). The third addable corner (2,0) contributes zero by
`ocneanuWeight_conventionD_eq_zero_of_three_rows`.

The Pieri reframing recorded in the previous update was right and it paid: the general-corner
route was never needed.

- `schurPrincipal_twoRow` — the hook-content product over a two-row diagram TELESCOPES:
  `schurPrincipal 2 Q (twoRow m k) = Q^k (1 + Q + ... + Q^{m-k})`. Row-1's numerator and
  denominator cancel outright (one `prod_range_reflect`); the rest collapses to a single ratio.
- `qBracket_pieri` — branching then reduces to `[d+1](1+Q) = [d+2] + Q[d]`, which is
  `s_mu * e_1 = Sum_{lam = mu+box} s_lam` in two variables. d=0 needs no case split in the
  ARITHMETIC (empty sum kills the term); only at the diagram level.
- `markovWeight2_conventionD` — a real cross-check, not decoration: it chains the n=3 theorem
  through the bridge and the new general two-row formula to `q^2/(q^2+1)^2`. Uses both the
  independently-proved n=3 weight and the new telescoping, so an off-by-one in the latter would
  fail there.

### This is ONE of the two halves, and the other is still open

Branching is **consistency of the weight family under restriction** `H_{n+1} -> H_n`. It is NOT
the Markov condition `tr(x sigma_n) = z tr(x)`, and it does not imply it. That remains the open
item, and it is still the highest-value one on this bean: per `OcneanuWeightWenzl`, proving it
would discharge the corpus's only external citation (Wenzl) outright.

### Scope note

Everything here is at convention D and on <=2-row diagrams. That is not a limitation of the proof
technique so much as the whole content of convention D — the >=3-row weights vanish, so <=2 rows
IS the trace. A general-convention branching identity would need the full corner sum and the
hook-ratio-in-corner-contents identity; not attempted, and not needed for the canonical convention.


## Update — the Markov condition has a route, and its arithmetic core is proved (PR #5575)

Last update I recorded that I had no route to the general-n Markov condition I would defend.
I have one now, and it changes the shape of what is left.

### The reduction

For x in H_n, decompose V_lam over its removals and set A_mu = P_mu sigma_n P_mu. A_mu commutes
with H_{n-1}; Hecke branching is multiplicity-free, so the commutant of H_{n-1} in End(V_mu) is
the Gelfand-Tsetlin algebra and A_mu is DIAGONAL in the seminormal basis, with (T,T) entry the
Hoefsmit parameter a(c(lam/mu) - c_T(n)). Since H_n = (+)_mu End(V_mu) the diagonal entries x_TT
range freely, so coefficients match pointwise; and n being T's largest entry, its cell is a
REMOVABLE corner of mu. Hence

    for every mu |- n and every removable corner r of mu:
      sum_{s addable corner of mu} w_{mu+s} a(c(s) - c(r)) = z w_mu

— a finite identity in the corner contents of ONE partition. Tested exactly at SYMBOLIC z (not
just convention D) for every partition of n = 1..6 and every removable corner:
`computations/schurweyl/ocneanu_markov_corner_reduction.py`.

### What is now proved in Lean

`OcneanuWeightMarkovCorner.lean`, sorry-free, axiom-clean: `markov_corner_row0`,
`markov_corner_row1`, `markov_corner_row1_diag`. At convention D the identity is two equations
with at most two terms each (the third addable corner (2,0) has weight zero), and against
`schurPrincipal_twoRow` both collapse to elementary geometric-sum facts —
[d+2] - 1 = x[d+1] and [d+1] = [d] + x^d.

### 🛑 What is NOT proved, and it is the whole remaining gap

**The reduction is not formalised.** Steps (i) A_mu diagonal and (ii) the Hoefsmit entry are what
`seminormalRep` encodes, but neither is proved in Lean. So the three theorems above do NOT prove
the Markov condition. They prove its arithmetic core.

**This is still progress worth naming:** the open item has changed from "prove the Markov
condition" — a statement about an algebra, its trace, and an arbitrary element x — to "prove that
P_mu sigma_n P_mu is diagonal in the seminormal basis, with the Hoefsmit entry". That is a
statement about the explicit matrices `seminormalRep` already defines, and the corpus already has
`seminormalRep_qJM_diag` (Ram 4.1) which is the same flavour of result. Different shape, and a
more tractable-looking one.

### Next

Formalise the reduction: (i) the diagonality of A_mu, (ii) its entry. Then the Markov condition
follows from the corner identities already proved — and that discharges the corpus's only external
citation (Wenzl), per `OcneanuWeightWenzl`.


## Update — the reduction's STRUCTURAL half is now Lean, and my justification for it was heavier than needed

`SeminormalBlockTrace.lean`, sorry-free, axiom-clean:

- `genMat_eq_zero_of_cellOf_succ_eq` — sigma_k's off-diagonal entries cross blocks.
- `cellOf_eq_of_genMat_ne_zero` — earlier generators preserve blocks.
- `trace_mul_genMat` — hence for any block-preserving X,
      tr(X . sigma_k) = sum_T X_TT * seminormalParam q (axialDist T k).

That third one is exactly the step the corner reduction runs on: it is what turns
chi^lam(x . sigma_n) into a sum of diagonal entries weighted by Hoefsmit parameters.

### CORRECTION to the justification recorded in this bean

The update above justified the diagonality by *"A_mu commutes with H_{n-1}; branching is
multiplicity-free, so the commutant is the Gelfand-Tsetlin algebra"* — Okounkov-Vershik. That is
**correct but far heavier than necessary**, and it is not what the Lean does.

`genMat` is defined with exactly two nonzero entries per column: the diagonal, and the swap partner
`swapTableau T k`. The swap partner moves `k+1` into the cell that held `k`
(`cellOf_swapTableau_succ`), and that is a different cell (`cellOf_ne`). Twelve lines, no
representation theory. Fact 2 is the same argument against `cellOf_swapTableau_of_ne`.

Recording rather than quietly switching: the OV justification is what this bean and
`OcneanuWeightMarkovCorner`'s docstring claim, so a reader comparing them should be able to see
which route the Lean actually takes. Both files now carry the note.

### What remains — and it is now a different, smaller thing

`trace_mul_genMat` is about **one** `V_lam`. The Markov condition is about the weighted sum over all
`lam |- n+1`. What is missing is the **assembly**: the lam-indexed decomposition (`heckeWedderburn`)
plus the weights (`ocneanuWeight`), combined with the corner identities already proved in
`OcneanuWeightMarkovCorner`. No new mathematics is identified as missing — the three pieces exist;
they have not been put together.

State of the arc:

| piece | status |
|---|---|
| closed-form weight, derived + checked vs proved n=3 | **Lean** |
| bridge to `schurPrincipal` at convention D | **Lean** |
| branching (trace-tower consistency) | **Lean** |
| Markov corner identities (the arithmetic core) | **Lean** |
| block structure + trace identity (the structural half of the reduction) | **Lean** |
| **assembly into the Markov condition** | **OPEN — the only remaining gap** |

Proving that assembly discharges the corpus's only external citation (Wenzl), per
`OcneanuWeightWenzl`.


## Update — block-preservation lifted to the subalgebra, and a gap I had not named

`SeminormalBlockTrace.lean` extended, sorry-free, axiom-clean: `BlockPreserving` (closed under
zero/one/add/neg/smul/mul), `blockSubalgebra`, generator membership, hence

    adjoin_earlyGens_le_blockSubalgebra : Algebra.adjoin R (earlyGens q N) <= blockSubalgebra N
    trace_mul_genMat_of_adjoin : X in adjoin -> (X * genMat q k).trace
                                   = sum_T X_TT * seminormalParam q (axialDist T k)

### CORRECTION — "only the assembly remains" was one gap short

The previous update's table listed the assembly as **the only remaining gap**. That was wrong, and
the missing item is on the structural side, not the assembly side:

**Identifying `Algebra.adjoin R (earlyGens q N)` with the image of the Hecke inclusion
`H_{N-1} -> H_N` under `seminormalRep`.** Without it, `trace_mul_genMat_of_adjoin` applies only to
matrices already known to lie in that adjoin — there is no route from an actual `x in H_{N-1}` to
the hypothesis. I did not notice this until writing the theorem's statement down, which is the
usual way: the gap was invisible while the result was prose.

Corrected state of the arc:

| piece | status |
|---|---|
| closed-form weight, derived + checked vs proved n=3 | **Lean** |
| bridge to `schurPrincipal` at convention D | **Lean** |
| branching (trace-tower consistency) | **Lean** |
| Markov corner identities (arithmetic core) | **Lean** |
| block structure + trace identity, for one V_lam | **Lean** |
| `adjoin(earlyGens)` = image of the Hecke inclusion | **OPEN** |
| assembly: lam-indexed sum with weights | **OPEN** |

Two gaps, not one. Neither has been shown to need new mathematics; both are work.


## Update — the inclusion gap is CLOSED; back to one remaining gap

The second gap I named one update ago is shut. `heckeIncl` is an `AlgHom` and
`adjoin_range_sigma_eq_top` says the sigma generate, so the composite's image lands in the block
subalgebra:

    seminormalRep_heckeIncl_mem_blockSubalgebra :
      seminormalRep q _ _ (m+1) hN (heckeIncl R q q^-1 m y) in blockSubalgebra (m+2)

and hence for every y in H_m(q),

    trace_heckeIncl_mul_lastGen :
      tr(rho(iota y) . rho(sigma_{m+1})) = sum_T rho(iota y)_TT * seminormalParam q (axialDist T (m+1))

That is chi^lam(x . sigma_n) = sum_T x_TT a(c(lam/mu) - c_T(n)) for a single V_lam, with the
hypothesis **discharged for a genuine Hecke element** rather than assumed of a matrix.

Worth noting for whoever picks this up: everything needed was already in the corpus — `heckeIncl`,
`heckeIncl_sigma`, `adjoin_range_sigma_eq_top`, `seminormalRep_sigma`, `seminormalGen`. It wanted
wiring, not new mathematics. The gap looked larger than it was.

| piece | status |
|---|---|
| closed-form weight, derived + checked vs proved n=3 | **Lean** |
| bridge to `schurPrincipal` at convention D | **Lean** |
| branching (trace-tower consistency) | **Lean** |
| Markov corner identities (arithmetic core) | **Lean** |
| block structure + trace identity, one V_lam | **Lean** |
| `adjoin(earlyGens)` contains the Hecke-inclusion image | **Lean** |
| assembly: lam-indexed sum with weights | **OPEN — the only gap** |

The assembly needs `heckeWedderburn` (the lam-indexed decomposition) and `ocneanuWeight` (the
weights) combined with `OcneanuWeightMarkovCorner`'s corner identities. No new mathematics is
identified as missing there either — but I said that about the inclusion gap too, and it still took
a session's work, so read "no new mathematics" as a claim about difficulty class, not about effort.


## Update — the tableau side of the branching compatibility (ingredients only)

`SytInsertMaxTransport.lean`, sorry-free, axiom-clean, no ring at all:

  cellOf_insertMax, axialDist_insertMax, swapAdmissible_insertMax_iff,
  swapTableau_insertMax, insertMax_injective

`genMat`'s entry rules read exactly four things about a tableau — cellOf, axialDist, SwapAdmissible,
swapTableau — so "the seminormal rep of lam restricted to a corner's block IS the seminormal rep of
mu" reduces to their compatibility with `insertMax`. These are those four, plus injectivity.

**Corpus-grep paid.** I was about to build the branching bijection from scratch;
`QOU.Mathlib.SYTBranchingRule` already has it — `branchInv`, surjective AND injective — along with
`insertMax`, `eraseCorner`, `IsCornerCell`, `card_eraseCorner`, `syt_ext`. Only the five transport
lemmas were genuinely absent. Anyone continuing this should grep `QOU/Mathlib/SYT*` before writing
anything about tableaux.

**These are ingredients, not the conclusion.** Still unwritten:

1. the block equality `genMat_lam q k (insertMax S'') (insertMax S') = genMat_mu q k S'' S'` — a
   case analysis over genMat's three branches using the five lemmas;
2. the outer reindexing `{(lam, corner)} <-> {(mu, addable corner)}` — `branchInv` gives the inner
   half (fixing lam), not the exchange of the outer index;
3. the lam-sum with weights, where the corner identities of `OcneanuWeightMarkovCorner` get used.

So the "assembly" I have been calling one gap is really these three steps. Item 1 looks
mechanical given the transport lemmas; items 2 and 3 are where the remaining thought is.

Note on `check-sidecars.sh`: it labels this file "archimedean construct present, ℝ justified". The
file contains no ℝ and no ring — the flag comes from `≤` inside `Set.Icc`, the same weak-marker
false positive measured under `qou-9e7p`.


## Update — step 1 done, step 2's first half done

`SeminormalBlockEquality.lean`, sorry-free, axiom-clean.

**Step 1** — `genMat_insertMax`: a generator avoiding the top entry has, on the block of the corner
`c`, exactly the matrix it has downstairs on `mu \ c`. Case analysis over genMat's three branches,
each discharged by one of the transport lemmas plus injectivity.

Plus the image characterisation, which turned out nearly free (`insertMax_eraseMax` repackaged):
`cellOf_insertMax_top` and `exists_insertMax_of_cellOf_top` — the block of `c` is EXACTLY
insertMax's image.

**Step 2, first half** — `compress_seminormalRep_heckeIncl`:

    compress c hc (rho_mu (iota y)) = rho_{mu\c} y     for EVERY y in H_{m+1}(q)

via `compress_mul` (compression is multiplicative on block-preserving matrices: the sum over SYT mu
collapses to the block, and the block IS insertMax's image, so it becomes a sum over SYT (mu\c))
plus an adjoin-induction over `adjoin_range_sigma_eq_top`.

The image characterisation is what makes `compress_mul` work — that is why it was worth landing in
the same pass.

### Remaining

| step | status |
|---|---|
| 1. block equality at a generator | **Lean** |
| 2a. lift to every Hecke element | **Lean** |
| 2b. outer reindexing `{(lam, corner)} <-> {(mu, addable corner)}` | **OPEN** |
| 3. the lam-sum with weights, consuming the corner identities | **OPEN** |

2b is combinatorial bookkeeping over `Nat.Partition`/`YoungDiagram` — `branchInv` gives the inner
half (lam fixed, corner varying) but not the exchange of the outer index. 3 is where
`ocneanuWeight` and `OcneanuWeightMarkovCorner` finally meet. Neither is written, and I have not
attempted either, so I am not going to estimate them.


## Update — step 2b: the missing `addCell`, and why it was missing

`QOU/Mathlib/YoungDiagramAddCell.lean`, sorry-free, axiom-clean, pure combinatorics:

    IsAddableCell, addCell, card_addCell, isCornerCell_addCell,
    isAddableCell_eraseCorner, eraseCorner_addCell, addCell_eraseCorner

**Why the corpus did not already have it.** `eraseCorner` exists; there was no inverse. That is fine
for `branchInv`, which fixes `lam` and varies the corner — it only ever REMOVES. Step 2b needs the
OUTER exchange, `{(lam, removable corner)} <-> {(mu, addable corner)}`, and the backwards direction
has to BUILD `lam` from `(mu, s)`. Nothing in the corpus could do that.

**Not assembled: the equivalence itself.** The dependent `Sigma` packaging — the second component's
type depends on the first — is its own piece of work, and I stopped before it rather than half-do
it. What is landed is the construction plus both round-trips, which is what that packaging consumes.

Also worth noting for whoever does the packaging: `Finset.sum_nbij'` may be the better route than an
`Equiv`, since the assembly wants a sum reindexing and the dependent-Sigma `Equiv` is the painful
form of the same content.

| step | status |
|---|---|
| 1. block equality at a generator | **Lean** |
| 2a. lift to every Hecke element | **Lean** |
| 2b. `addCell` + round-trips | **Lean** |
| 2b. the reindexing equivalence / sum-reindex | **OPEN** |
| 3. the lam-sum with weights | **OPEN** |


## Update — step 2b is CLOSED

`cornerAddEquiv n : CornerPair n ≃ AddPair n`, sorry-free, axiom-clean:
`(lam, removable corner) <-> (lam \ c, that corner, now addable)`.

**The phrasing is the whole trick, and it cost me an attempt.** The natural spelling is a `Sigma`
over the diagram, `Sigma L : {mu // |mu| = n+1}, {c // IsCornerCell L.1 c}`. Don't. The second
component's type then depends on the first, so `left_inv` lands on a `HEq` between corner-proofs
over two diagrams that are equal but not syntactically so, and discharging it needs a transport
whose motive does not typecheck — the card-proof inside the diagram depends on the diagram. I hit
that, backed out, and rephrased **both sides as subtypes of one product type**. The dependency
disappears and the round-trips become plain `Subtype.ext` on a pair. Same content, no HEq.

Recorded in the file's docstring too, because the `Sigma` spelling is the one anyone would reach
for first.

| step | status |
|---|---|
| 1. block equality at a generator | **Lean** |
| 2a. lift to every Hecke element | **Lean** |
| 2b. `addCell` + round-trips + the exchange equivalence | **Lean** |
| 3. the lam-sum with weights | **OPEN — the only gap** |

Step 3 is where `ocneanuWeight` and `OcneanuWeightMarkovCorner`'s corner identities finally meet.
It will also want Fintype instances on `CornerPair`/`AddPair`, transportable from `Nat.Partition`
via `partitionShapeEquiv`, to turn `cornerAddEquiv` into a sum reindexing.

I have said "only one gap left" twice this session and been wrong once. This time the remaining
item is a single named theorem rather than a category of work, but I have not attempted it.


## Update — the sum reindexing is landed

`QOU/Mathlib/YoungDiagramCornerReindex.lean`, sorry-free, axiom-clean:

- `fintypeDiagramsOfCard n` — diagrams of size `n`, transported from `Nat.Partition n`
  via `partitionShapeEquiv`.
- `fintypeCornerPair n` — via `cornerPairEquivSigma`, an all-`rfl` repackaging into the
  Sigma form. The Sigma spelling is painful for the *bijection* (HEq, see above) but
  harmless for this, because nothing moves.
- `fintypeAddPair n` — transported along `cornerAddEquiv` itself. This is the part worth
  keeping: nothing ever has to bound the addable cells of a diagram directly; the
  removable side already did that work.
- `sum_cornerPair_eq_sum_addPair` — the exchange under a sum.

One correction to my own note above: I suggested `Finset.sum_nbij'` might beat an `Equiv`
here. It doesn't — once the phrasing is subtype-of-a-product the `Equiv` is three `rfl`s
and the reindexing is one `Fintype.sum_equiv`. The `Equiv` was the painful form only in
the Sigma spelling.

Separate file rather than appended to `YoungDiagramAddCell`: finiteness is the one part
of this that is not pure ℕ × ℕ combinatorics (it comes off the RSK/Schensted cone, and
the corner-set `Fintype` comes from `SYTBranchingRule`), so `AddCell` stays importable by
callers that only want `addCell` and the round-trips.

| step | status |
|---|---|
| 1. block equality at a generator | **Lean** |
| 2a. lift to every Hecke element | **Lean** |
| 2b. the exchange + its sum reindexing | **Lean** |
| 3. the λ-sum with weights | **OPEN — the only gap** |


## Step 3 is CLOSED — the assembly is formalised

`QOU/SchurWeyl/MarkovAssembly.lean`, `markov_of_corner_identity`, sorry-free and axiom-clean:

    ∑_{|λ| = m+2} w_λ · tr(ρ_λ(ι y) · σ_{m+1}) = z · ∑_{|ν| = m+1} w_ν · tr(ρ_ν(y))

for every `y ∈ H_{m+1}(q)` and **every** weight function `w`, with the per-corner identity
as an explicit hypothesis — not an axiom, not a `sorry`.

**What that is worth, stated precisely.** What is proved is the *reduction*: the Markov
condition for the weighted seminormal trace **is** that finite arithmetic identity in the
corner contents of one partition. Everything representation-theoretic is now discharged in
Lean — branching, the block structure of the last generator, the Hoefsmit entry, the
reindexing. `OcneanuWeightMarkovCorner` proves the hypothesis at convention D for the ≤2-row
diagrams the trace lives on; the general-`n` statement is what
`ocneanu_markov_corner_reduction.py` tests exactly at symbolic `z` through `n = 6`.

**So the standing caveat has moved, and I have narrowed it in the two files that carry it.**
`OcneanuWeightMarkovCorner` and `SeminormalBlockEquality` both said the λ-sum was paper-only;
both now say what is actually still outside Lean, which is the corner identity at general `n`.

Two bricks landed on the way, both in `SeminormalCornerTrace` / `YoungDiagramCornerReindex`:

- `trace_heckeIncl_mul_lastGen_corner` — the block trace as a sum over corners, with
  `branchEquiv` (packaging `branchInv`'s two bijectivity halves, which `SYTBranchingRule`
  proved separately because it only needed the cardinality) and `axialDist_insertMax_top`.
- `sum_corner_eq_sum_addable` — the exchange as a **double**-sum reindexing, which is the form
  the block trace actually needs. The summand is a function of the erased diagram *as a
  subtype element carrying its card proof*; that is what lets the two sides' card proofs meet
  without transport (both are proofs of a Prop, hence definitionally equal), and the last step
  of that proof is `rfl`.

Plus `addCellOrSelf` (`addCell` made total, so it can appear in a summand quantified over all
cells) and `isCornerCell_cellOf_card`, which is what lets the corner identity apply at
`r = ` the cell carrying each downstairs tableau's top entry.

| step | status |
|---|---|
| 1. block equality at a generator | **Lean** |
| 2a. lift to every Hecke element | **Lean** |
| 2b. the exchange + its double-sum reindexing | **Lean** |
| 3. the λ-sum with weights | **Lean** |
| the corner identity at general `n` | **open** — proved at convention D for ≤2 rows; tested exactly through n=6 |

Two mechanical notes worth keeping. `Equiv.sum_comp` times out at `whnf` on these sums — it
wants the two `Fintype` instances definitionally equal and they are noncomputable
(`Set.Finite.fintype`); `Fintype.sum_equiv`, which asks only for a pointwise equality, goes
through instantly. And a Sigma-valued intermediate function needs a `set F : … := … with hF`
binding: written inline it has no inferable type and its projections do not resolve.


## The general-`n` corner identity at convention D may be MUCH closer than the PR says

Noticed while replying to the two sibling coordination comments. `markov_of_corner_identity`
quantifies its hypothesis over **all** `ν` of size `m+1`, and I had been reading that as
"needs the general-`n` identity". It may not, at convention D, because of the vanishing:

- **`ν` with ≥3 rows.** `w_ν = 0`, so the RHS is `z·0 = 0`. Adding a cell cannot *reduce* the
  row count, so every `ν+s` also has ≥3 rows and every `w_{ν+s} = 0` — the LHS is `0` too.
  The hypothesis holds **trivially**, not by any corner arithmetic.
- **`ν` with ≤2 rows.** Its addable cells are `(0,m)`, `(1,k)` and `(2,0)`; the third makes a
  3-row diagram, weight `0`. So the sum has exactly the **two** surviving terms that
  `markov_corner_row0` / `markov_corner_row1` / `markov_corner_row1_diag` already prove.

If that holds up, `ocneanuWeight` at convention D satisfies the Markov property **at general
`n`, unconditionally** — which is the open item the PR headline names, and the last external
citation the whole tranche was aimed at.

**Not attempted, and I am not claiming it.** Two things have to be built and either could be
harder than the sketch: a classification putting every `ν` in one of the two buckets, and an
enumeration of the addable cells of `twoRow m k` as the subtype the hypothesis sums over
(with `(2,0)` shown to contribute zero). The second is the fiddly one. Also worth checking
before starting: whether `markov_corner_row1`'s statement without `0 < k` lines up with the
`k = 0` (single-row `ν`) case, where row 1 has no removable corner — the file's own docstring
flags that the identity there "corresponds to no corner and carries no Markov content", which
is about the *removable* side but is the kind of edge the enumeration will hit.

This supersedes my previous "next step" note, which said to attack the corner identity at
general `n` directly from `schurPrincipal`'s hook-content form. That is the right move for
**arbitrary** `z`; at convention D specifically, the vanishing may do the work.


## The convention-D shortcut WORKED — the Markov condition is unconditional at every `n`

`QOU/SchurWeyl/MarkovConventionD.lean`, `SeminormalRep.markov_conventionD`, sorry-free,
axioms `[propext, Classical.choice, Quot.sound]`:

    ∑_{|λ|=m+2} W_λ · tr(ρ_λ(ι y) · σ_{m+1}) = z_D · ∑_{|ν|=m+1} W_ν · tr(ρ_ν(y))

for every `y ∈ H_{m+1}(q)`, `W = ocneanuWeight q z_D`, `z_D = q³/(q²+1)`. The per-corner
identity that `MarkovAssembly` took as a hypothesis is **discharged**, for every diagram and
every removable corner, with no general-`n` arithmetic — exactly as the sketch predicted:

- **≥3 rows**: both sides zero, no corner arithmetic at all.
- **≤2 rows**: the diagram *is* a `twoRow`; of its ≤3 addable cells, `(2,0)` makes three rows
  and drops out; what survives is the two-term statement already proved.

The two pieces the sketch said had to be built are `TwoRowCorners.lean` (addable/removable
characterisations, the addable-cell sum as ≤3 explicit terms, and the `addCell` identities) and
`eq_twoRow_of_rowLen_two_eq_zero`. The `k = 0` edge I flagged did not bite: `markov_corner_row0`
covers it as `k < m`, and the `k = m` diagonal is `markov_corner_row1_diag`.

**What this closes, stated exactly.** Wenzl's theorem — this tranche's one external input — says
these *are* the Ocneanu/Markov weights, which is **two** legs: the Markov property and the
normalisation `tr(1) = 1`.

- **Markov property: proved** at convention D, every `n`.
- **Normalisation: NOT proved** at general `n`. Lean has `∑_λ f^λ W_λ = 1` at `n = 3` and
  `n = 4` only; it is verified numerically through `n = 9`, which is not a proof.
- **Arbitrary `z`**: the per-corner identity remains open;
  `ocneanu_markov_corner_reduction.py` tests it symbolically through `n = 6`.

So do **not** write "Wenzl's theorem is discharged". Write "the Markov-property leg is discharged
at convention D; the normalisation leg at general `n` is open." That second leg is the next item,
and it is a different shape — an identity in `f^λ` and the weights, not a corner recursion.


## The normalisation leg is closed too — both defining properties now hold at every `n`

`QOU/SchurWeyl/MarkovNormalisation.lean`, `sum_dim_weight_eq_one`, sorry-free, axiom-clean:

    ∑_{|λ| = n} f^λ · W_λ = 1   for every n,  W = ocneanuWeight q z_D

which is `tr(1) = 1`, since `tr(1) = ∑_λ W_λ · dim V_λ` and `dim V_λ = f^λ`.

**I said in the last note that this was "a different shape — an identity in `f^λ` and the weights,
not a corner recursion". That was wrong, and being wrong about it is why it landed quickly:** it
is the *same* exchange, run without the Hoefsmit factor. `ocneanuWeight_addable_sum` gives
`∑_{s addable} W_{ν+s} = W_ν` for every diagram (same ≥3-rows / `twoRow` split, `(2,0)` dropping
out), `numStandardYoungTableaux_branching` expands `f^λ`, and `sum_corner_eq_sum_addable` closes
it — so the sum is *constant in `n`* and equals its value at `n = 0`. The base case is `⊥` with
`f = 1` (`numStandardYoungTableaux_bot`, **already in the corpus**) and `W = 1`.

Complement, not replacement: `OcneanuWeightMarkov3`'s normalisation lemmas do the same identity at
`n = 3, 4` for **arbitrary** `z`. Neither subsumes the other.

### Status of the external input

| | |
|---|---|
| Markov property `tr(x·σ_n) = z·tr(x)` | **Lean**, convention D, every `n` |
| Normalisation `tr(1) = 1` | **Lean**, convention D, every `n` |
| Uniqueness — that a Markov trace with a given `z` is *the* one | **not proved** |
| Both properties at **arbitrary** `z` | **not proved**; symbolic tests to `n = 6` |

So Wenzl's theorem is no longer an input *for the two properties the downstream mass channel
actually uses*. It is still an input for the word "**the**". Do not compress this to "Wenzl
discharged" — the uniqueness step is a real statement and nobody has written it here.

The natural next item is that uniqueness: a Markov trace is determined on `H_n` by the two
properties plus cyclicity, by induction on reduced words. #5592's coset recursion
(`pyhecke.tl.markov_trace_basis`, `w = u·d` with `d` minimal in `S_{n-1}w`) is exactly that
induction done computationally, and is the obvious thing to formalise against.


## Scoping the uniqueness leg — two findings, one of them a trap

Corpus-grepped before starting, and the picture is better than I assumed in the last note.

**1. The spanning family already exists.** `HeckeCoset.span_cosetFam_eq_top (m) : Submodule.span K
(Set.range (cosetFam m)) = ⊤`, with `cosetFam (m+1) (b, j) = ι(cosetFam m b) · descProd m j` and
`descProd m j = σ_m σ_{m-1} ⋯ σ_{m-j+1}`. That is exactly the induction skeleton uniqueness needs:

- `j = 0` — `T_{m+1}(ι x) = T_m x` by consistency.
- `j ≥ 1` — `descProd m j` has the top generator `σ_m` on the left and the rest inside `ι(H_m)`,
  so cyclicity moves the tail across and the Markov property collapses it to `z · T_m(…)`.

Then extend off the family by `Submodule.span_induction`. So the hard structural half — the coset
decomposition — is **not** work I would have to do; #5592's `w = u·d` coset recursion is the same
induction done computationally, and is the obvious cross-check.

**2. `MarkovTraceTower` is NOT the axiomatisation its name suggests — do not build on it.**
`QOU/Braiding/HnMarkovTrace.lean:45` declares `class MarkovTraceTower (q : ℝ)` carrying **only**
`z`, `z_pos`, and `trM_sigma1_sq : ℕ → ℝ` with a stabilisation property. It is a statement about
the trace of the **single element `σ₁²`**, not a trace functional on `H_n` at all. A uniqueness
theorem needs a real structure — a family of linear maps with cyclicity, normalisation, Markov and
consistency — which does not exist in the corpus yet. I nearly targeted `MarkovTraceTower` on the
strength of the name.

**Estimate, stated as an estimate:** the structure plus the induction plus the `descProd`
manipulation. Not a five-line bridge, but not the multi-session job I implied either, given (1).
Where it should live is a real question — this PR is already 26 files, so a follow-up branch may
serve the reviewer better than the combine-into-one-branch default.


## Uniqueness is proved — but read what it does and does not give

`QOU/SchurWeyl/MarkovTraceUnique.lean`, `markovTrace_unique`, sorry-free, **generic
`[CommRing K]`** (no ordering, nothing archimedean):

> any two Markov traces on the Hecke tower with the same `z` agree, on every `H_n(q)`.

The scoping note two entries up was right: `HeckeCoset.span_cosetFam_eq_top` does the structural
work, and the proof is one induction over that family. `descProd_eq_last_mul_incl` is the only new
ingredient — `r_j = σ_m · ι(t)` for `1 ≤ j ≤ m+1` — after which cyclicity moves the tail and the
Markov property collapses the rest.

**The `j ≤ m+1` bound is load-bearing.** The factorisation is *false* past it: `descProd 0 2 =
σ₀·σ₀`, and `σ₀ ∉ ι(H_0) = K·1`. `cosetIndex` only ever supplies `j : Fin (m+2)`, so the family
stays in range — but a future generalisation that drops the bound will break here, not obviously.

**It does NOT identify the Ocneanu weight with anything yet, and I want that recorded before
someone reads the theorem name.** It is a statement *about* `MarkovTraceFamily`, and **no instance
is built**. The identification needs the weighted seminormal trace packaged as one, which needs two
properties not yet proved for it:

- **cyclicity** `tr(xy) = tr(yx)` — blockwise from `Matrix.trace_mul_comm`; `seminormalRep` is an
  `AlgHom`, so this should be short.
- **consistency** `tr_{n+1}(ι x) = tr_n x` — the corner decomposition *without* the `σ` factor.
  Needs a small new lemma ("trace of a block-preserving matrix = sum of the compressed block
  traces"), then `compress_seminormalRep_heckeIncl` and `ocneanuWeight_addable_sum` close it.

Index conventions will need care there: this file's `tr (n+1)` is on `Hecke K q qi (n+1) =
H_{n+2}(q)`, while `markov_conventionD` is indexed by diagram size.

| | |
|---|---|
| Markov property | **Lean**, convention D, every `n` |
| Normalisation | **Lean**, convention D, every `n` |
| Uniqueness (abstract) | **Lean**, generic `CommRing` |
| The seminormal trace **as** a `MarkovTraceFamily` | **open** — cyclicity + consistency + packaging |
| Either property at arbitrary `z` | **open**; symbolic tests to `n = 6` |


## CLOSED — the Ocneanu weight *is* the Markov trace, and Wenzl is no longer an input at convention D

`QOU/SchurWeyl/MarkovTraceInstance.lean`, sorry-free, axiom-clean:

    ocneanuMarkovTrace  : MarkovTraceFamily ℝ q q⁻¹ (q³/(q²+1))
    eq_wtrace_of_markov : ∀ T : MarkovTraceFamily ℝ q q⁻¹ (q³/(q²+1)), ∀ n x,
                            T.tr n x = wtrace … n x

Every Markov trace on the Hecke tower with parameter `z_D` **is** the Ocneanu-weighted seminormal
trace. That is exactly what `QBeta/WenzlWeightVanishing.lean` calls *"the external input, and the
only one"*.

**Building the instance also retires my own caveat from two entries up.** I flagged uniqueness as
possibly vacuous — a theorem about a structure nobody had inhabited. It is inhabited now, so the
uniqueness statement has content and the identification follows from it.

The two fields that were missing:

- **cyclicity** — `seminormalRep` is an `AlgHom`, so `Matrix.trace_mul_comm` blockwise. Short, as
  predicted.
- **consistency** — the corner decomposition again, minus the `σ` factor. `trace_eq_sum_compress`
  needs **no** block-preserving hypothesis, which I had assumed it would: the trace is a sum over
  `SYT μ` and `branchEquiv` is a bijection onto it, so the split is unconditional.

### Final status

| | |
|---|---|
| Markov property | **Lean**, convention D, every `n` |
| Normalisation | **Lean**, convention D, every `n` |
| Uniqueness | **Lean**, generic `[CommRing K]` |
| The instance, and the identification | **Lean**, convention D |
| Either property at **arbitrary `z`** | **open** — symbolic tests to `n = 6` |
| Root-of-unity regime | **out of scope by construction** — `H_n(q)` is not semisimple there and partitions stop indexing the irreducibles; needs a different statement, not a better proof (cf. `qou-4lft`) |

**Do not quote this as "Wenzl's theorem is proved".** It is proved *at convention D*, under
`q ≠ 0`, `q² ≠ 1`, `q² + 1 ≠ 0`, and `q²` not a root of unity. Convention D is canonical per the
2026-08-15 owner ruling, so that is the case the corpus needs — but the qualifier is real.

Follow-on work, none of it blocking: arbitrary `z` (the per-corner identity is the whole gap);
instantiating `HeckeWedderburnData` with `ocneanuWeight` (sibling `sw8` is on the structure side);
and re-reading the downstream two-row-cap audit now that the identification is not a citation.
