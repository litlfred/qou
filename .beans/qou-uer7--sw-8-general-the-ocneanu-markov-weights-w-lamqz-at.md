---
# qou-uer7
title: 'SW-8 general: the Ocneanu Markov weights w_lam(q,z) at every n'
status: in-progress
type: task
priority: normal
created_at: 2026-08-23T16:51:49Z
updated_at: 2026-08-23T18:42:40Z
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
