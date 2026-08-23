---
# qou-uer7
title: 'SW-8 general: the Ocneanu Markov weights w_lam(q,z) at every n'
status: in-progress
type: task
priority: normal
created_at: 2026-08-23T16:51:49Z
updated_at: 2026-08-23T20:39:45Z
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
