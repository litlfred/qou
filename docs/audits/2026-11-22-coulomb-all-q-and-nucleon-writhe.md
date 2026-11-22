# The two measured Coulomb negatives hold over Q(q); the nucleon writhe is 0 (2026-11-22)

Owner ruling 2026-11-22, verbatim *"Do all"* on the #9103 card: prove the two items that
`docs/audits/2026-11-21-neutron-heavier-sign.md` §27A and §28 record as measured at a few q only,
and settle which nucleon writhe is current. Issue #9102, PR #9103.

## 1. Both items are identities in Q(q) at n = 6

Pre-registration: `computations/probes/np_splitting/np_all_q_symbolic_preregistration.md`
(commit `78924a752b9`, before the probe). Probe and output: `np_all_q_symbolic_probe.py`, `.out.txt`.
Every entry is an exact element of the rational function field Q(q), held as a numerator and a
denominator in Q[q] (python-flint `fmpq_poly`, reduced by gcd). No float and no numeric q are used in
the computation. The readout is the one in §26–§28: ΔE_X = T_X/T_1,
T_X(a, b) = Tr(K^{⊗6} Π_{a,b} V_A³ V_B³ X), V = σ_lo σ_{lo+1}⁻¹, Jimbo Ř.

**§27A, the whole braid image.** Over Q(q):

- The 720 sector vectors span a space of dimension 10 of 16. Each of the 720 reduces to zero
  against the basis, so the span is exactly that space, not merely at least that space.
- T_1 is in the span, so the constant c is free.
- The affine-bilinear system for (κ, κα, κβ) has rank 2: the reachable pair terms with κ ≠ 0 form
  one ray, with

      α(q) = q²(q¹² − 3q¹⁰ + q⁸ − 5q⁶ + 3q⁴ − 2q² + 1) / P(q),
      β(q) = (q¹² − 2q¹⁰ + 3q⁸ − 5q⁶ + q⁴ − 3q² + 1) / P(q),
      P(q) = q¹⁴ − 2q¹² − q¹⁰ − 2q⁸ − 2q⁶ − q⁴ − 2q² + 1.

- **α + β = 1 is an identity in Q(q).** So is β(q) = α(q⁻¹): the bar involution exchanges the two
  centres. Coulomb (α = β = 0 with κ ≠ 0) is not reachable for any q at which the computation is
  defined.
- Cross-check: α(111/100) = 0.656124… and α(7/5) = 1.053685…, the values §27A measured.

**§28, invariant couplings.** Over Q(q):

- Ř-compatible U_q pair Casimir (G-q, coproduct Δe = e⊗K + 1⊗e, Δf = f⊗1 + K⁻¹⊗f):
  **pp − nn = 0**, and pp − pn − np + nn = q + q⁻¹.
- KZ monodromy M = β_AB²: **pp − nn = 0**.
- Control, the opposite coproduct: pp − nn ≠ 0 (a degree-18 numerator), as registered.

**Where the identities hold.** An identity in Q(q) holds at every q where the rational functions
used are defined. The probe lists the excluded points: the zeros of P(q) (positive real roots
≈ 0.60286 and ≈ 1.65875, reciprocal to each other) and the zeros of the elimination pivots.
None of them is q = 111/100, 7/5, 2, or the proton q₀. At the roots of P the normalisation κ = 1 of
the ray fails; there the reachable term has no Q_aQ_b part at all, which is still not Coulomb.

**Tier.** Symbolic-exact (computer algebra over Q(q)) at n = 6. This is not a Lean proof, and it
says nothing about n ≠ 6. Lean already covers the parts with a structural reason: the Weyl-symmetric
classical forms (`WeylSymmetricPairNotCoulomb.lean`), the zero sector trace of weight-shifting
insertions and the Cartan readout for every q (`WeightShiftZeroTrace.lean`), and the single crossing
to all orders (`HeckeSeriesCollapse.lean`). The symmetry behind α + β = 1 is now in Lean as well; see
the next paragraph.

**The structural reason for α + β = 1 (added the same day, issue #9124).** Flipping every strand
(u ↔ d) and reversing the strand order is conjugation by a permutation matrix J with
J Ř_i J = Ř_{4−i}. It sends the core to its inverse, J C J = C⁻¹, and sector (a, b) to
(3 − b, 3 − a), that is Q_A ↦ 1 − Q_B, Q_B ↦ 1 − Q_A. The earlier draft of this section stopped
there and called the inverse core an obstruction. It is not one: the half twist Δ = σ_lo σ_{lo+1} σ_lo
satisfies Δ V Δ⁻¹ = V⁻¹ by the braid relation, so D = Δ_A Δ_B gives D C D⁻¹ = C⁻¹, and D acts inside
each block, so it commutes with the sector projectors. Hence

    T_X(Q_A, Q_B) = T_{X'}(1 − Q_B, 1 − Q_A),   X' = D⁻¹ J X J D,

and the set of reachable pair shifts is closed under the sector involution. That involution sends
c + κ(Q_A − β)(Q_B − α) to c + κ(Q_A − (1 − α))(Q_B − (1 − β)). Since the reachable terms with κ ≠ 0
form one ray, (1 − α, 1 − β) = (β, α), which is α + β = 1.

- Lean, sorry-free (axioms propext, Quot.sound, Classical.choice):
  `QOU.QBeta.PairTermSectorSymmetry` —
  - `halfTwist_conj_core_pow` (the braid identity, in any group);
  - `readout_sectorSymm` (the readout symmetry, for any ring with a trace and an automorphism with
    the stated relations);
  - `alpha_add_beta_eq_one_of_unique_ray`;
  - `not_coulomb_of_unique_ray`.
- The 64 × 64 instances of the relations (J Ř_i J = Ř_{4−i}, J C J = C⁻¹, D C D⁻¹ = C⁻¹, D preserves
  sectors) are checked exactly over Q(q) by `np_pair_term_sector_symmetry_check.py` (output in
  `.out.txt`), not in Lean.
- The uniqueness of the ray (rank 2) stays a computer-algebra fact over Q(q) at n = 6, and is a
  named hypothesis of the Lean theorems.

The same symmetry explains §28. The Ř-compatible pair Casimir and the KZ monodromy M = β_AB² are
fixed by X ↦ D⁻¹ J X J D (check 6), and the sector involution sends the proton pair (1, 1) to the
neutron pair (0, 0), so pp = nn for both (`readout_eq_of_fixed`). The opposite-coproduct Casimir
is not fixed, which is why the control gives pp ≠ nn.

So of the two inputs to the Coulomb exclusion, the symmetry is now structural and the rank is
computed. The symmetry argument uses the braid relation, the shape of the Jimbo Ř-matrix, and
one more fact: K^{⊗6} is a scalar on each sector, so it cancels in ΔE. That last fact needs every
strand to sit in a block. With spectator strands between the blocks it fails, and so does the
symmetry (§3).

## 2. The nucleon writhe under the ruled word is 0, for both nucleons

**What the corpus fixes.** The nucleon word is β_Bor = (σ₀σ₁⁻¹)³ (owner rulings 2026-11-21, γγ
word by whole-word linking neutrality, and 2026-11-22, energy minimisation as a selection rule).
The proton and the neutron carry the same word. They differ in which strands are u and d, which is
the sector label the readout uses, not in the braid. Its writhe is 0
(`QOU.Mass.GammaGammaWordSelection.borromean_writhe`, sorry-free).

**The other readings in the corpus.** Three nucleon writhe readings predate the ruled word, and
none of them is the writhe of β_Bor:

| reading | values | source | what it is |
|---|---|---|---|
| inter-nucleon arc | w(p) = +1, w(n) = −1 | `2026-06-02-u1-hypercharge-assignment.md` §2 | the writhe of the bond, linking-number normalisation |
| Hopf-link pair framing | pp = +2, nn = −2 | same, from `2026-06-01-inter-nucleon-linked-channel.md` | the framing of a two-nucleon pair, not of a nucleon |
| intra-block | p = +3, n = +1 | `mba-sidecar-mirror-cancellation.md`; `computations/delta_lambda_exponent_from_crossings.py` | older nine-crossing nucleon words: proton 6σ − 3σ⁻¹, neutron 5σ − 4σ⁻¹ |

The `WritheIndependenceCriterion.lean` docstring quotes the second row as "the derived framing
writhes w(p) = +2, w(n) = −2"; those are pair framings. `SecondCrossingInvariant.lean` uses
writhe 0 for the Borromean baryon, which is the ruled-word reading.

**Consequence for `def:coulomb-charge`.** With w(p) = w(n) = 0 and charges 1 and 0, the electric
charge is not a function of the nucleon-word writhe. Lean:
`QOU.StandardModel.WritheChargeHypercharge.charge_not_writhe_of_equal_writhe` (abstract) and
`QOU.StandardModel.NucleonWritheCharge.charge_not_writhe_on_nucleons` (on β_Bor), sorry-free. The
halved writhe gives the proton charge 0
(`halved_writhe_proton_charge_zero`). This is a second, direct refutation of Q = w/2 as the electric
charge, independent of the quark argument already in the block.

**Consequence for the hypercharge premise.** Several blocks state that "the proton and neutron share
Y = +1 while their writhes differ". Under the ruled word their writhes do not differ. The conclusion
those blocks draw, that Y needs a second invariant, still stands, but by a different route:
the baryon and the vacuum share writhe 0 and differ in baryon number
(`SecondCrossingInvariant.baryon_vacuum_separating`), and the electric charge separates p and n at
equal writhe (above). Blocks carrying the old premise:
`eightfold-way/flavor-charge-assignments.md`, `eightfold-way/eightfold-open-problems.md`,
`appendix-standard-model/sm-gauge-truncation.md`, `appendix-standard-model/sm-hypercharge-invariant.md`,
`appendix-standard-model/sm-lagrangian-selection-rules.md`.

## 3. More strands: spectators (issue #9124, item 3)

Pre-registration: `computations/probes/np_splitting/np_more_strands_preregistration.md` (commit
`e3c781b9f0e`, before the probe). Probe and output: `np_more_strands_probe.py`, `.out.txt`. Same
readout, with X over the whole N-strand Hecke image and the spectator strands summed over in the
sector projector. Exact rationals (python-flint fmpq) at q = 111/100 and q = 7/5. These are exact at
those q, not identities in q.

| layout | N | spectators | ΔE span | rank of (κ, κα, κβ) | reachable pair terms | Coulomb |
|---|---|---|---|---|---|---|
| L6 | 6 | none | 10 / 16 | 2 | one ray, α + β = 1 | no |
| L7e | 7 | one, after block B | 10 / 16 | 2 | the same ray as L6 | no |
| L7s | 7 | one, between the blocks | 14 / 16 | 1 | α = α₆(q), β free | no |
| L8s | 8 | two, between the blocks | 14 / 16 | 1 | α = α₆(q), β free | no |

α₆(q) is the six-strand value (111/100: 0.656124…, 7/5: 1.053685…). The Coulomb form needs α = 0,
so it is excluded in every layout at both q.

**P1 failed, and why.** The prediction was that the symmetric layouts (L7s, L8s) keep the sector
involution. They do not. The argument of §1 needs K^{⊗N} to be a scalar on each sector, so that it
cancels in ΔE. A spectator between the blocks carries its own K factor, which varies inside a sector,
and the flip-and-reverse map sends K to K⁻¹. With the spectator at the end (L7e) nothing changes
from N = 6.

**The K weight is what excludes Coulomb.** A diagnostic run with the plain trace (no K^{⊗N},
`QOU_NO_K=1`) gives the same result as the K-weighted run at N = 6, where K cancels. With any
spectator (L7s, L7e, L8s) the plain trace reaches all 16 sectors, and the Coulomb form becomes
reachable. The readout of §26 is the K-weighted (quantum) trace. So the exclusion with spectators
rests on that weighting, not on the braid alone.

**Scope.** Two values of q and N ≤ 8 with two blocks; §4 lifts the K-weighted rows to identities
in q. Not a statement about three or more blocks.

## 4. Identities in q, and the bar symmetry (issue #9124)

Probe and output: `np_more_strands_symbolic_probe.py`, `.out.txt`. Every entry is a polynomial in q
(python-flint `fmpz_poly`, after scaling by powers of q), the span is computed over Q(q) by
fraction-free elimination, and α, β are rational functions of q. The words are the fully
commutative elements of S_N (132, 429, 1430 for N = 6, 7, 8), whose Hecke images span the
Temperley–Lieb quotient that the words generate on V^{⊗N} (Fan; Graham). That reduction is checked,
not assumed, at N = 6 and N = 7, where the probe also runs all of S_N and gets the same span.

Over Q(q), every row of the §3 table holds as stated, with

    α₆(q) = q²(q⁶ − q⁵ − q⁴ − q³ + q² − 1)(q⁶ + q⁵ − q⁴ + q³ + q² − 1)
            / ((q² + 1)(q¹² − 3q¹⁰ + 2q⁸ − 4q⁶ + 2q⁴ − 3q² + 1)),

β₆(q) = 1 − α₆(q) = α₆(q⁻¹). In L7s and L8s the relation pins α = α₆(q) exactly and leaves β free.
The Coulomb form is not reachable in any layout, as an identity in q.

**The bar symmetry.** `ψ = transpose ∘ Ad F ∘ bar` (F flips u ↔ d on every strand, bar : q ↦ q⁻¹)
reverses products, sends σ_i to σ_i⁻¹ and fixes K^{⊗N}
(`np_pair_term_bar_symmetry_check.py`, ALL PASS). It sends V = σ_a σ_b⁻¹ to σ_b σ_a⁻¹, which the
half twist conjugates back to V, so ψ(C) = E C E⁻¹ with E = Δ_A Δ_B. Unlike the sector involution
of §1, this needs nothing about how K sits on a sector, so it holds with spectators. On pair
terms it acts by (Q_A, Q_B) ↦ (1 − Q_A, 1 − Q_B) and q ↦ q⁻¹, sending (α, β) to
(1 − ᾱ, 1 − β̄). The probe confirms the reachable span is closed under it in all four layouts.

Lean (`QOU.QBeta.PairTermSectorSymmetry`, sorry-free, axioms propext and Quot.sound):
`readout_barSymm` is the abstract readout statement; `alpha_add_bar_eq_one_of_pinned_alpha` gives
α₀(q) + α₀(q⁻¹) = 1 whenever α is pinned; `not_coulomb_of_pinned_alpha` excludes Coulomb from that
alone; `beta_eq_bar_alpha_of_unique_ray` gives β(q) = α(q⁻¹) when the ray is unique. So with
spectators the exclusion of Coulomb reduces to one computed fact, that α is pinned. That fact is
established for N ≤ 8; it is not proved for general N.

## Scope

No empirical input enters a proof. The nucleon charges 1 and 0 are hypotheses of the Lean lemma, as
comparison data. Part 1 is scope-(b) for n = 6 within the readout of §26 (all q, both identities
exact). The tower in n is open. Part 2 is derived from the ruled word.
