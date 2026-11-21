# m_n by its own identity: where the error comes from, against the literature (2026-11-21)

Scope: the compute of this directory (the convention-D proton identity read for the neutron,
three-strand readings N0/N1/N2 and four-strand arms L-A/L-B/L-C). The Q_β route (`Q_β = m_e·R(q)`,
`R ≤ 3/4`) belongs to another thread and is not redone here. CODATA and the literature values
below are comparison points only; none enters a proof or a fit. Numbers of this framework are
recomputed with mpmath at 50 dps at the muon pin (CAL-2, CODATA 2022 `m_μ/m_e`).

## 1. The literature split of m_n − m_p = 1.29333 MeV (n − p)

| source | QCD part (m_d − m_u) | QED part | total | in library |
|---|---|---|---|---|
| Borsanyi et al. (BMW) 2015, lattice QCD+QED | +2.52(17)(24) | −1.00(07)(14) | 1.51(16)(23) | `arxiv-1406.4088v2` |
| Walker-Loud, Carlson, Miller 2012, Cottingham | (+2.53(40) lattice input) | −1.30(03)(47) (elastic −1.39(02)) | | `arxiv-1210.7777v1` |
| Gasser, Leutwyler 1975 Cottingham | | −0.76(30) | | cited in `arxiv-1210.7777v1` |
| Gasser, Leutwyler, Rusetsky 2020, Compton sum rule | +1.87(16) | −0.58(16) | | `arxiv-2008.05806v2` |

(Signs converted to n − p; the papers quote p − n.) Two facts are common to all of them:
the splitting is a **difference of two terms of opposite sign**, a strong one (`m_d > m_u` makes
the neutron heavier, ≈ +2.0 to +2.5 MeV, i.e. 2.0–2.7 × 10⁻³ of m_N) and an electromagnetic one
(the proton's charge makes it heavier, ≈ −0.6 to −1.3 MeV, i.e. 0.6–1.4 × 10⁻³). And both
**vanish in the isospin limit** `m_u = m_d`, `α = 0`, where `m_n = m_p` exactly.

## 2. Where each piece of this compute sits against that split

**(a) The proton side is not the source.** Muon pin: m_p = 938.271861 MeV, −243.86 ppb. The
calibration error propagated from σ(m_μ/m_e) = 22 ppb is 25.7 ppb (sensitivity
d ln m_p / d ln(m_μ/m_e) = 1.155), so this is the known 9.5σ μ–p tension. It is 5600× smaller
than the n–p gap (1376.5 ppm of m_n).

**(b) N0 (m_n = m_p) is exactly the isospin limit.** The functional is `u ↔ d` symmetric
(`wholeTrace_reflect`) and the two-term connected part is 0. In literature terms it contains
neither the QCD term nor the QED term, so its −1.2933 MeV miss is the whole of both. This is not
a numerical error in the compute; it is the absence of both isospin-breaking sources.

**(c) A consequence that the literature makes sharp: the identity hits the wrong mass.** An
isospin-symmetric functional should land near the isospin-symmetric nucleon mass, which to first
order in the breaking is the doublet average (m_p + m_n)/2 = 938.9188 MeV. The identity lands on
m_p to 0.24 ppm instead. The offset is (m_p+m_n)/2 − m_p = 0.6467 MeV = **1.2655 m_e**. So, if the
identity is the isospin-limit mass, a proton-specific −1.27 m_e is sitting inside the constant −12
(or the scale). The "−12" is owned by sibling item 3; this is passed to it as a measured
constraint, not a correction.

**(d) The framework's u/d asymmetry is too large by an order of magnitude.** The only place u and
d differ in this compute is the T³ weight `K = q^{±1}` and the crossing structure. The sizes it
produces, against the literature's breaking fractions:

| quantity | size | vs (m_n−m_p)/m_n = 1.3765 × 10⁻³ |
|---|---|---|
| N1 own-sector ratio, 1 − q⁻² | 0.1883 (neutron lighter) | ×137, wrong sign |
| L-B selected word, h²/(1−h²), h = q − q⁻¹ | 0.04570 (neutron heavier) | ×33, right sign |
| BMW QCD part alone | 2.68 × 10⁻³ | ×1.95 |
| BMW QED part alone | −1.06 × 10⁻³ | ×−0.77 |

In QCD the strong breaking is first order in (m_d − m_u)/Λ ≈ 2.5 MeV / m_N. Here the breaking
enters through q itself (2 ln q = 0.209, h² = 0.0437), with no separate small parameter for
m_d − m_u. The flavour grading is the same q that sets the masses, so any reading that lets K or a
u–d crossing see the state gives a splitting of order q − 1 or h², 30–140× too big. A
neutron-heavier result of the right size needs a breaking parameter of order 10⁻³ that the
current objects do not contain. (h⁴ = 1.91 × 10⁻³ is of that order; that is an observation of
magnitude only, not a derivation, and nothing here proposes it.)

> **Correction (2026-11-21, later the same day).** "Needs a breaking parameter of order 10⁻³ that
> the current objects do not contain" was wrong. The identity itself contains one: the ratio of its
> constant term to its volume term, 12 mₑ / m_p = 6.5 × 10⁻³. If the Cartan weight sits on the
> constant term instead of the volume term, the split is h · 12 mₑ ≈ 1.28 MeV, with the neutron
> heavier. See §2(g). I also missed two corpus results in the first pass:
> `prop:flavor-split-substrate` already gives (m_n − m_p)/M_N ≈ (q−1)²(1−q⁻⁴)/3 to −0.1 %, but its
> own proof (Step 2) labels the input a phenomenological ansatz chosen to agree with experiment,
> and it is convention C. `NucleonIsospinExclusions` (`trace_sword_eq`, `restrictedTrace_ratio`)
> already proves, for every braid word, equal bare sector traces and quantum-trace ratio q².

**(e) The two-term trace removes exactly the term that carries the EM splitting.** On a
nucleon, the pair charge Σ_{i<j} Q_iQ_j is a scalar on each weight space: 0 on uud, −1/3 on udd.
The ruled (connected) two-term trace subtracts that scalar, so it is 0 for both nucleons
(`pairSum_eq_of_total_eq`; four strands `twoTerm_connected_zero`). In the Cottingham analysis the
dominant EM piece is the elastic (Born) term, ≈ −1.39 MeV (WLCM 2012), which is set by the nucleon
charge form factors, i.e. by the total charge squared Q_N² = ΣQ_i² + 2Σ_{i<j}Q_iQ_j (p 1, n 0). That
is the scalar part the connected trace removes. The corpus already proves the raw part has the
literature's sign: with a repulsive like-charge coupling w_N > 0, s_q ≥ 0 the neutron comes out
lighter (`PairwiseChargeEnergyBeta.nucleon_em_split_neg`, split −w_N/3 − s_q/3). So the EM half of
the literature split is not missing from the algebra; it is removed by the connected subtraction,
and its coupling w_N (c_em) is not derived. Whether the ruled two-term trace should keep the
scalar charge part for an EM self-energy is a question for the owner; nothing is changed here.

**(f) L-C is a structural mismatch, not a size error.** The convention-D trace multiplies over a
split union (tr_D(σ₀σ₁σ₀) = 0.691), masses add. Nothing in the literature corresponds.

**(g) Which term of the mass formula can carry the split (added 2026-11-21).** Pre-registration
[`PREREGISTRATION-cartan-constant.md`](PREREGISTRATION-cartan-constant.md); probe
[`mn_cartan_constant_probe.py`](mn_cartan_constant_probe.py) (8/8 exact checks); Lean
`QOU/MassTheory/NeutronCartanConstant.lean` (sorry-free, axioms `propext, Classical.choice,
Quot.sound`).

The production identity has two terms, +2 m_μ F_Bor and −12 mₑ. The volume term is a braid-class
function and the γγ word is the same for p and n, so it is isospin-blind. On the nucleon weight
spaces the only state-sensitive factor is the Cartan weight, q on uud and q⁻¹ on udd. Proved
(`split`, `neutron_heavier_iff`): for any assembly of bare and Cartan-weighted terms,
m_n − m_p = −s(q − q⁻¹) × (net weighted coefficient), so for q > 1 **the neutron is heavier
exactly when the weighted part is net negative**. Weighting the volume term gives the neutron
lighter (`volume_weighted_neutron_lighter`, this is N1). Weighting the −12 mₑ term gives the neutron
heavier (`const_weighted_neutron_heavier`).

| reading | m_n − m_p (muon pin) | vs 1.29333 | m_p | m_n |
|---|---|---|---|---|
| volume weighted (N1) | −177.87 MeV | wrong sign | −0.24 ppm | −19 % |
| constant weighted, proton-normalised (s = q⁻¹): 12(1 − q⁻²) mₑ | **1.15494 MeV** | −10.70 % | −0.24 ppm | −147.5 ppm |
| constant weighted, plain K^⊗3 (s = 1): 12 h mₑ | **1.28196 MeV** | −0.88 % | −719 ppm | −730 ppm |

The proton pin agrees to the shown digits. Against the literature, this is the shape QCD has: an
isospin-blind gluon energy plus a small flavour-sensitive term. The literature total is
1.29 (experiment), 1.51(16)(23) (BMW 2015), 1.35(18)(8) (QCDSF-UKQCD 2015). Both readings land
inside or near those error bars. The sign and the size h · 12 mₑ do not depend on which reading is
taken. What is **not derived**: that the −12 mₑ term carries a Cartan weight at all, and the
normalisation s. The −12 itself is underived (#8809). The proton-normalised reading keeps m_p but
needs an extra q⁻¹. The plain K^⊗3 reading has no extra factor, but it moves m_p by
−12(q − 1) mₑ = −0.67 MeV, which breaks the proton round trip. Choosing between them by residual
would be selection against the target, so neither is adopted.

*Narrowing (same day), using only the proton test.* The −12 audit
(`docs/audits/2026-11-21-proton-minus-twelve-origin.md`) found that at the muon pin the proton's
constant must be q-independent to about 1 % of h²: a count or a dimension, not a trace evaluated
at q₀. The plain K^⊗3 reading gives the proton −12q = −13.32. That moves m_p by −719 ppm, where the
measured precision is at the ppb level. So that reading is **falsified by the proton**. This is the
honest m_p prediction at the muon pin; it is not a choice made against n − p. The proton-normalised
reading survives: the constant is 12 mₑ on the highest-weight member (p) and 12 q⁻² mₑ on the
lowered member (n). That is the Cartan weight measured relative to the doublet's highest weight.
Its split is 12(1 − q⁻²) mₑ = 1.15494 MeV, 10.7 % below experiment and below the lattice totals.
The derivation target is therefore precise: a q-independent count, 12, on the proton weight space,
and a reason why a lowered state carries q⁻² relative to it. Neither is derived. The rest of the
gap (0.138 MeV) is the size of the EM pieces in §2(e). That is a magnitude comparison, not a
closure.

## 3. Summary of the error, term by term

| literature term (n − p) | this compute | status |
|---|---|---|
| QCD, m_d − m_u: ≈ +1.9 to +2.5 MeV | weighting the volume term gives the wrong sign (×137); weighting the −12 mₑ term gives the neutron heavier, 1.15–1.28 MeV in total (§2g) | candidate term identified; that it carries a weight, and the normalisation, are not derived |
| QED, mainly elastic: ≈ −0.6 to −1.3 MeV | present in the raw two-term part with the right sign; removed by the connected subtraction; coupling not derived | removed by a ruling, size underived |
| isospin-symmetric mass ≈ (m_p+m_n)/2 | identity gives m_p to 0.24 ppm; 1.27 m_e offset sits in the −12 | constant carries a proton-specific piece |
| proton calibration | −244 ppb, 9.5σ μ–p tension | not the source (5600× smaller) |

Every derivable term in these arms is included; the two terms above that are absent (a
m_d − m_u parameter and c_em) are absent because nothing in the corpus derives them.

## 4. The two open pieces: why q⁻², why 12 (2026-11-21, coordinator relay of the owner's "keep deriving")

**The q⁻² is now derived from one premise.** Lean `QOU/MassTheory/NeutronSectorQTraceConstant.lean`
(sorry-free, `lean -DautoImplicit=false -s 65536` exit 0, axioms `propext, Classical.choice,
Quot.sound`). Premise: the constant term is the convention-D quantum trace of some braid element,
taken on the nucleon's **own** weight space, with a normalisation κ that is the same for p and n.
(The volume term is the whole-space Markov trace and stays blind.) Then, **for every signed braid
word and every κ**, the neutron's constant is q⁻² times the proton's (`neutron_constant_ratio`).
This comes from `restrictedTrace_ratio` (T_p = q² T_n, via the intertwiner P) and is not a choice.
Fixing the proton at 12 mₑ gives 12 q⁻² mₑ for the neutron, m_n − m_p = 12(1 − q⁻²) mₑ =
1.15494 MeV (`split_of_sector_qtrace`), and the neutron is heavier for q > 1
(`neutron_heavier_of_sector_qtrace`). With the bare sector trace there is no split
(`bare_sector_constant_no_split`). So the proton-normalised reading of §2(g) is not an extra
normalisation choice: it is what any own-sector quantum trace gives once the proton value is
fixed. What remains assumed is the premise itself: that the constant is an own-sector trace while
the volume term is a whole-space trace.

**The 12 is not derived.** Under the premise the proton constant is κ·q·tr_{W_p}(w). The −12 audit
requires it to be independent of q. A search of all 1457 reduced signed words in σ₁^{±1}, σ₂^{±1}
up to length 6 (`mn_sector_count_probe.py`, pre-registered in its docstring, exact sympy) finds
**no** word with q·tr_{W_p}(w) independent of q. On W_p the trace is q^{e(w)} + χ_(2,1)(w), where
e is the exponent sum: one copy of the quartet and one copy of the doublet. So a pure number κ
would need a specific linear combination of words, and nothing in the corpus names one. Scope (a):
words up to length 6, single words only. The 12 stays a count with several readings
(2·F_Bor(1) = 4·F_e(1) = 2·|S₃| = dim V_(2,1)·dim H₃), none of them selected by the framework
(issue #8809).

## 5. Sums of words, and whether the own-sector premise follows from the QOU axioms (2026-11-21)

Pre-registered in `PREREGISTRATION-sums-and-premise.md` (with a disclosure of an exploratory run).

**Sums of words (`mn_sector_sums_probe.py`, 7/7).** Over all 1457 reduced signed words of
length ≤ 6, the integer span of the own-sector traces `T_p = q·tr_{W_p}` reaches exactly the
constants `3ℤ`. The minimum is `σ₁ + 2σ₁⁻¹` (`T_p = 3`); `σ₂ + 2σ₂⁻¹` gives the same value; and
`4σ₁ + 8σ₁⁻¹` gives 12. Within this class every multiple of 3 is reachable, so the class does
not single out 12, and choosing multiplicities to hit 12 would be selection against the target.
This is a statement about the searched class only; it does **not** show that 12 is unforced. No
canonical element of `H_3` (symmetriser, `Σ T_w`, `Σ q^{-ℓ} T_w`, full twist, Jucys–Murphy
sum) has a q-independent nonzero `T_p`; the antisymmetriser gives 0, as `W_p` has no `(1³)`
part. The three `S_3` sums give `6 = |S_3|` at `q = 1`, so `12 = 2|S_3|` is suggested at the
classical point only. Scope (a): words of length ≤ 6.

**The premise (`OwnSectorFromWeightGrading.lean`, sorry-free).**

- *Forced.* The maximal torus (`def:maximal-torus`) acts diagonally on weight spaces. With a
  torus pivotal element `K = Σ λ_N π_N`, the quantum trace is the `λ`-weighted sum of sector
  traces (`qtrace_eq_sum_sectors`), and for a weight-preserving `x` each sector trace is the
  trace on the sector (`sector_trace_eq_restriction`). For `K^{⊗3}`, `λ_p = q`, `λ_n = q⁻¹`.
  So *if* a term is read sector by sector, its weights and the `q²` ratio are forced.
- *Proved, and narrower than it first read.* A rule that treats the volume and constant terms
  alike cannot make the neutron heavier once the proton mass is positive
  (`uniform_rule_neutron_not_heavier`). So a heavier neutron needs a rule that separates the
  two terms. The sector decomposition by itself does not separate them.
- *Not found.* I have not found where in the axioms the separation comes from. That is a gap
  in this search, **not** a proof that the axioms cannot supply it (correction 2026-11-21,
  owner: "You just haven't proven that it's not forced"). The first version of this section
  said "not derivable from the QOU axioms"; that over-claimed and is withdrawn.
- *Normalisation.* The plain sector trace gives `s = 1` (K2), which the proton test falsified.
  K1 needs an extra `q⁻¹`, whose source is likewise not found.

## 6. Where the 12 and the term separation could come from (candidates)

`NucleonSectorBurnsideCount.lean` (sorry-free) and `mn_twelve_candidates_probe.py`.

The proton identity factors as `m_p/m_e = 2((m_μ/m_e) F_Bor − 6)`, and `6 = F_Bor(1) = [3]_1!`.
The candidate that ties the count to a sector: the classical `S_3` fixed-point count on the
flavour labellings of `V^{⊗3}` is `6` on the proton sector, `6` on the neutron sector, `12` on
both nucleon sectors, and `24` on the whole space (`burnside_*`, by `decide`). At `q = 1` the
six `S_3` traces on `W_p` also sum to `6` (`own_sector_count_q1`); for general `q` they do not
(`own_sector_sum_q`). So **if** the constant is a classical `S_3` count, it is `12` only when
restricted to a nucleon sector, and the whole-space reading gives `24`. That is a link between
the count and a sector restriction. It does not choose between "2 × own sector" and
"1 × both nucleon sectors", and it does not show the constant is such a count.

Other candidates that equal 12 numerically are listed in the probe output with no mechanism
attached (`3 colours × 4 weights of V^{⊗3}`, `|A_4|`, `dim H_4 / 2`, `2|χ(Bring)|`). Equal
values with no mechanism are not evidence, and none is selected.

## 7. Flavour-labelled closure (`mn_labelled_closure_probe.py` 7/7, `NucleonSectorBurnsideCount.lean`)

A labelled closure keeps each closed component's `u/d` label: a labelling counts only if it is
constant on the cycles of the braid's permutation. Computed with the full 8-dim Jimbo R-matrix.

1. **It does not separate the volume term by itself.** `V³` is a pure braid, so every labelling
   of a sector is consistent, and its labelled closure equals the sector trace on every sector.
   Labelling therefore resolves the volume term as much as the constant, and by
   `uniform_rule_neutron_not_heavier` that alone gives a lighter neutron. (Scope: this one
   mechanism, applied uniformly.)
2. **It gives a q-independent count of 6 exactly on the nucleon sectors.** On the six positive
   permutation braids with closure weight `q^{c(σ) − 3}`, the labelled count is `6` on the
   proton sector and `6` on the neutron sector for every `q` (`labelled_count_proton`,
   `labelled_count_neutron`), and `5 + q²` on `uuu` and `ddd`. So the q-independence the `−12`
   audit requires holds on the nucleon sectors and fails on the others.
   Disclosure: the weight `q^{c − n}` was chosen by inspecting the proton entries; the neutron
   value and the `uuu`/`ddd` failure are out of sample.

What this does and does not give: a mechanism under which a q-independent `6` per nucleon
sector appears, which would make the proton constant `2 × 6` and keeps it off the whole space.
It does not give the neutron's `q⁻²` (the labelled count is `6` on both sectors; the `q⁻²`
still needs the `K^{⊗3}` weight with the extra `q⁻¹`), it does not explain the factor 2, and it
does not show the constant term is this count. Those stay open.

## 8. The closure weight from the Ocneanu trace; the factor 2 (`mn_closure_weight_ocneanu_probe.py` 4/4)

**Weight.** The weight `q^{c − n}` of §7 is `1/τ_z(T_{w_C})`, where `τ_z` is the Ocneanu trace
and `w_C` the minimal-length element of `σ`'s conjugacy class, for which `τ_z(T_{w_C}) = z^{n−c}`.
With a general Markov parameter the class-normalised labelled count on a nucleon sector is
`3 + 3q/z`, and it equals `6 = |S_3|` **iff `z = q`** (`labelled_count_eq_six_iff`, sorry-free).
At the canonical `z_D = q³/(q² + 1)` it is `6 + 3/q²` (`labelled_count_zD`), and no extra factor
`q^{k(n−c)}` (k = −6…6) makes the `z_D` count q-independent. So the weight is no longer a free
choice: it is the Ocneanu normalisation, and it needs `z = q` (the other admissible point under
convention D, the augmentation), not `z_D`. Normalising by the full trace `τ_z(T_σ)` instead of
the class representative gives no constant at either point. Which Markov parameter governs the
mass channel is a framework question this probe does not settle.

**Factor 2.** The production identity already reads
`m_p/m_e = dim V_(2,1) · ((m_μ/m_e) F_Bor − |S_3|)` with `dim V_(2,1) = 2`. The 2 multiplies the
volume term as well, so the constant inside the bracket is `6`, which is the labelled count. The
factor 2 is the identity's overall prefactor, not a separate piece of the constant. (Its own
origin, `dim V_(2,1)`, belongs to the volume-term derivation, not to this thread.)

**Still open.** The neutron's `q⁻²`: the labelled count is 6 on both sectors, so the split still
needs the `K^{⊗3}` weight with the extra `q⁻¹` (K1). And why the constant term is the labelled
count of the `S_3` permutation braids at all.

## 9. The neutron's q⁻² from the Markov condition at z_D (`MarkovPivotalNucleonWeights.lean`, sorry-free)

Earlier the `q²` ratio came from assuming the symmetric weight `K = diag(q, q⁻¹)`. Here nothing
is assumed about `K` except that it is diagonal, `K = diag(a, b)`. Jimbo's `Ř` and the Markov
condition (weighted partial trace over the closed strand is a scalar) give:

- `markov_forces_ratio`: the condition holds iff `b = a q⁻²`, for every scale `a`;
- `markov_z_eq_zD`: the Markov parameter is then `z_D = q³/(q² + 1)`, for every scale;
- `nucleon_weight_ratio`: proton sector weight `a²b`, neutron `ab²`, so neutron = `q⁻²` × proton.

So the neutron's `q⁻²` relative to the proton follows from convention D's Markov condition. It
is no longer an assumption about `K`.

What it does not fix is the overall scale. With the trace normalised (`a + b = 1`) and the
framing factor `(1 + q²)³ q⁻³` from `def:mass-identity`, the weights are exactly `q` and `q⁻¹`
(`framed_unit_scale`). That is the K2 reading, which the proton test falsified. The surviving K1
reading (proton weight 1, neutron `q⁻²`) needs a further overall `q⁻¹`, still not found.

Two consequences for §7–8. (i) A diagonal pivotal trace on `V^{⊗n}` always gives `z = z_D`, so the
`z = q` normalisation the labelled count needs is not a pivotal trace on `V`; it is the trivial
(one-row) channel, which is the only channel the labelled closure of a permutation braid sees,
since consistent labellings only meet same-label crossings where `Ř` acts by `q`. (ii) The `z = q`
count is therefore not the scoreboard's trace.

**Correction (2026-11-21, owner: "We have two term trace....it is derived. What other trace do you
mean?").** An earlier version of (ii) said the ratio `q⁻²` and the count `6` "come from two different
traces" and asked whether one mass functional can use both. That framing was wrong. There is one
derived trace, the two-term Lagrangian trace (owner ruling 2026-11-21), and §10 works inside it. The
`z = q` closure of §7–8 is a probe of the count, not a second mass functional.

## 10. Inside the two-term Lagrangian trace (`TwoTermMatterOwnSector.lean`, sorry-free)

The two-term Lagrangian is `ℒ = 𝒟² + ψ*·𝒟ψ`, `𝒟 = q⁻¹∇ + (1 − q⁻¹)Reeb`
(`CategoricalLagrangianTwoTermBridge.lean`).

- **Separation of the terms.** `𝒟²` contains no nucleon state, so with a shared `𝒟` it cancels in
  `n − p` (`trace_lagrangian_diff_shared_dirac`, already on `main`). The matter term `ψ*·𝒟ψ` contains
  the nucleon's own state, so it is the own-sector piece. This is the structural reason the volume
  term is shared while the constant is own-sector.
- **The extra `q⁻¹`.** The horizontal coefficient of the matter term is `q⁻¹`. If the horizontal
  matter trace is the own-sector trace of a common `c` (Cartan weight `q` on the proton sector,
  `q⁻¹` on the neutron, as `Kp`/`Kn`), the horizontal contribution is `c` for the proton and
  `q⁻² · c` for the neutron (`horizontal_matter_proton_of_own_sector`,
  `horizontal_matter_neutron_of_own_sector`). That is exactly K1, the reading that survived the
  proton test. `nucleon_diff_of_own_sector_horizontal` gives the whole difference:
  `(q⁻² − 1)·c + (1 − q⁻¹)·(Reeb matter difference)`.

What is assumed, and stated as Lean hypotheses (`hHorizP`, `hHorizN`): that the horizontal matter
trace is the own-sector trace of one common `c`.

**That hypothesis reduces to two checkable facts (`MatterTraceWeightVector.lean`, sorry-free).**
`ψ* ≫ ψ` factors through the unit, so in a matrix model it is rank one, `ψ φ`. For the quantum
trace `τ(X) = tr(K X)`:

- `qtrace_rank_one`: if `K ψ = w ψ`, then `tr(K ψ φ M) = w · (φ M ψ)`. The sector weight is the
  `K`-eigenvalue of the state, by cyclicity alone.
- `matrix_element_eq_of_intertwiner`: if the up/down flip `P` sends the proton state to the
  neutron state and intertwines the connections (`P Mp = Mn P`, the shape of `P A₁ = B₁ P`), the two
  matrix elements are equal.

So `hHorizP`/`hHorizN` hold once (a) the nucleon state is a `K`-weight vector, of weight `q`
(proton) or `q⁻¹` (neutron), and (b) the flip intertwines the two horizontal connections. Fact (a)
is what "proton sector" means. Fact (b) is not yet checked against the corpus's `nablaEndo`.

**This also corrects the count framing.** An earlier version of this section said the identity on
the 3-dimensional weight space gives `3`, not `12`. That treated `c` as a trace over the sector. It
is not: `c = φ ∇ ψ` is one matrix element. If `∇` acts as the identity, `c = φ ψ`, the
normalisation of the nucleon state. So the open question is now: what fixes `φ ∇ ψ = 12`? Either
`∇` on the nucleon state, or the state's normalisation, or both. Neither is fixed by the corpus
yet. Searching for a `∇` or a normalisation that gives `12` would be selection against the target,
so it has not been done.

Note that the bridge on `main` already puts the pairwise Coulomb charge in the Reeb matter piece
(`trace_matter_diff_coulomb_specialization`), so the horizontal piece is not otherwise occupied.

## 11. Checking (b) and the state's normalisation against the corpus (2026-11-21)

**(b), the connection.** `nablaEndo` is never instantiated in the Lean tree. It appears only as a
field of `CategoricalDiracOperator` and in hypotheses of `CategoricalLagrangianTwoTermBridge`. So
there is no corpus `∇` to check (b) against. What can be said: if `∇` on the weight space is built
from braid generators, (b) holds automatically, because the corpus flip `P` already satisfies
`P A₁ = B₁ P` and `P A₂ = B₂ P` (`NucleonWeightSpaceTraces.intertwine₁/₂`). On the bridge's weight
spaces `Kp = q • 1` and `Kn = q⁻¹ • 1`, so (a) holds for every state too.

**A conflict with the bridge.** The concrete bridge theorem
`trace_lagrangian_diff_concrete_borromean_weight_space` assumes `hHoriz`: equal horizontal matter
traces for proton and neutron. Under (a) and (b) the two traces are `q·m` and `q⁻¹·m`, so
`matrix_element_zero_of_equal_traces` (sorry-free) proves `hHoriz` forces `m = 0` when `q² ≠ 1`.
So the bridge's concrete theorem, as stated, carries no horizontal own-sector constant at all. One
of the two has to give: either `hHoriz` (and then the horizontal piece is the K1 constant) or the
K1 lead. This is not resolved here.

A related inconsistency inside the bridge: the bosonic Reeb² hypotheses carry the Cartan weight
(`hReebP : … = q * trace V³_A`), but the matter Reeb hypotheses do not
(`hMatReebP : … = trace ((Q₁₂ + Q₂₃) V³_A)`). By `qtrace_rank_one`, a matter trace on a weight-`q`
state carries the weight `q` too. The Coulomb piece of the bridge should be re-checked for that.

**The normalisation.** `categorical-lagrangian.md` defines `ψ* = λ ∘ S(ψ)` with `λ` the Frobenius
form. In `FrobeniusHopfData` the form `λ` is constrained only by the two snake identities with the
coevaluation. Those are unchanged under `λ ↦ sλ`, `coev ↦ s⁻¹ coev`, so the axioms do not fix the
scale of `ψ* ψ`. (Now a Lean theorem: `FrobeniusFormScaleFree.lean`, §12.) So the corpus does not currently
fix `φ ψ`, and therefore does not fix `c = 12` through the normalisation either. A normalisation
law for `λ` (for instance the Markov `τ(1) = 1`, which fixes a trace, not `λ`) would have to be added
or derived.

## 12. The weighted bridge and the free Frobenius scale (2026-11-21, owner: "1 3")

**The bridge with Cartan weights (`WeightedTwoTermBridge.lean`, sorry-free).**
`trace_lagrangian_diff_weighted_borromean` restates the concrete bridge theorem with two changes. It
drops `hHoriz` and uses horizontal matter traces `q·c` (proton) and `q⁻¹·c` (neutron). It also gives
the Coulomb (matter-Reeb) traces their Cartan weights, `q·tr((Q₁₂+Q₂₃)V³_A)` and
`q⁻¹·tr((Q₁₂+Q₂₃)V³_B)`. The bosonic hypotheses are unchanged. Result:

    τℒ_n − τℒ_p = (1−q⁻¹)²(q⁻¹−q)·tr V³   (unchanged bosonic term)
                 + (q⁻² − 1)·c              (horizontal own-sector constant, K1)
                 + (1−q⁻¹)·W(q),
    W(q) = (2q¹⁴ − 2q¹² − 9q¹⁰ + 20q⁸ − 26q⁶ + 18q⁴ − 13q² + 4)/(9q⁷).

`W` replaces the bridge's unweighted Coulomb function `U(q) = (2q¹² − 7q¹⁰ + … + 2)/(3q⁶)`. Both
equal `−2/3` at `q = 1`, so the classical limit is unchanged. At the CODATA-2022 muon pin (40-digit
mpmath, model evaluation, not a comparison) `W = −0.597423649217` against `U = −0.663427284748`;
after the factor `(1 − q⁻¹)`, `−0.0591937666` against `−0.0657335208`, about 10 % smaller. The value
of `c`, and the units in which these traces become MeV, are not fixed here.

**The free scale (`FrobeniusFormScaleFree.lean`, sorry-free).** `snake_left_rescale` and
`snake_right_rescale`: both snake identities survive `λ ↦ s•λ`, `coev ↦ s⁻¹•coev` for any `s ≠ 0`.
`pairing_rescale`: the pairing then scales by `s`. So the axioms as written do not fix the
normalisation of `ψ*ψ`, and the constant `c = φ∇ψ` inherits that freedom. Fixing `c = 12` needs a
normalisation law for `λ` that the current `FrobeniusHopfData` does not contain. Adding one is an
axiom change and is an owner decision; nothing here proposes a value.

## 13. Does existing structure already pin λ? (2026-11-21, owner: "1")

Read `FrobeniusHopfData` (`CategoricalFoundations.lean`) law by law. Only three laws mention `λ`:
the two snake identities and `antipode_frobeniusForm : S ≫ λ = λ`. The last is linear in `λ`, so
it is invariant under `λ ↦ sλ` as well. None of the unit, counit, (co)associativity, Frobenius or
other antipode laws mentions `λ`. So **no axiom pins the scale of λ**. With §12 this is now a
complete check of the structure, not a sample.

Two things the structure does pin, and why they matter:

- **The categorical trace is scale-free** (`leftTrace_rescale`, sorry-free). `leftTrace f =
  coev ≫ (f ▷ A) ≫ μ ≫ λ` is unchanged by `λ ↦ sλ`, `coev ↦ s⁻¹coev`, because the closed loop
  contains one of each. So any constant that is a *closed* trace has a fixed value. The open
  pairing `ψ* ψ` contains `λ` but not `coev`, so it is not fixed. This sharpens the question: the
  constant `c` is fixed by the current axioms if and only if it can be written as a closed trace
  rather than as `φ ∇ ψ` with a free normalisation of `ψ`.
- **The counit `ε` is pinned** by the counit laws (a comonoid has a unique counit; standard, not
  re-proved here). The corpus already uses the hypothesis `λ = ε` in
  `MassTraceIdentity.massTrace_eq_functional_hol_of_frobeniusForm_eq_counit` and in the bridge's
  `reeb_holonomy_leftTrace_eq_functional_hol`. Under that hypothesis the scale of `λ` is fixed. It is
  a hypothesis of those theorems, not an axiom. Whether `λ = ε` is compatible with the snake
  identities on the intended models has not been checked here, and the value it gives `ψ* ψ`
  also depends on `ψ`, which is still free.

The Markov normalisation `τ(1) = 1` fixes a trace on the Hecke tower, not `λ`; by
`leftTrace_rescale` the categorical trace is already scale-free, so it adds nothing to `λ` either.

## 14. λ = ε against the snakes; the matter constant as a closed trace (2026-11-21, owner: "3")

`CounitFrobeniusForm.lean`, sorry-free:

- `counit_snake_right`: with evaluation `μ ≫ ε` and coevaluation `η ≫ Δ`, the right snake identity
  holds in every `FrobeniusHopfData`, from the stated Frobenius relation, `one_mul` and
  `comul_counit` alone. So `λ = ε` is compatible with the right snake identity. The left snake would
  need the mirror Frobenius relation `μ ≫ Δ = (A ◁ Δ) ≫ α⁻¹ ≫ (μ ▷ A)`, which is not an axiom of
  `FrobeniusHopfData`; not checked. (Note: `FrobeniusHopfModelDichotomy` shows models collapse
  under the convolution condition, which is no longer an axiom; it does not apply here.)
- `matter_leftTrace_rescale`: the costate is `ψ* = λ ∘ S(ψ)`, so it carries its own `λ`. A closed
  trace of the matter term cancels one `λ` against `coev` and keeps the costate's: it scales by `s`.
  So **the matter constant cannot be made scale-free by writing it as a closed trace.** Its
  normalisation is the normalisation of `λ`.

What does remove the scale is a **ratio of two open pairings that share `λ`**: both scale by `s`.
The production identity writes the constant in units of `m_e` (`12 m_e`). If the electron's own mass
is the matter pairing of the electron state in the same Lagrangian, then CAL-1 fixes `s`, and the
nucleon/electron ratio of matter pairings is scale-free. That is not a fourth calibration. Whether
the electron's mass is such a pairing is not yet established.

## 15. Pairing ratio and the mirror Frobenius relation (2026-11-21, owner: "3")

Pre-registered in `PREREGISTRATION-pairing-ratio-and-mirror.md` before running.

**A. Nucleon/electron ratio** (`mn_pairing_ratio_probe.py`, exact `ℚ(q)`). Mixed-state expectation
`⟨X⟩ = tr(K X)/tr(K)` (a ratio of closed traces, so scale-free), Jimbo `Ř` on `V^{⊗3}`, electron
`σ₀σ₁σ₀`, nucleon `(σ₀σ₁⁻¹)³`.

| sector | ratio `⟨X_N⟩/⟨X_e⟩` | at `q = 1` |
|---|---|---|
| E1 whole space | `−(q¹² − 3q¹⁰ + 2q⁸ − 4q⁶ + 2q⁴ − 3q² + 1)/(q⁷(q⁴+1))` | `2` |
| E2 proton sector | `−(q²+1)²(q¹² − 3q¹⁰ + 3q⁸ − 5q⁶ + 3q⁴ − 3q² + 1)/(3q⁹(q⁴+1))` | `2` |
| E2 neutron sector | same as proton | `2` |

Pass criterion was `12` identically. **Scope-(a) negative for this class only**: the ratio is
`q`-dependent and equals `2` at `q = 1`, not `12`. The proton and neutron sector expectations of
`V³` are equal, so this class does not produce the `q⁻²` split either (that comes from the weight
of a pure state, §10–11, which the mixed average divides out). Observation, not a claim: at
`q = 1` the ratio is `2 = dim V_(2,1)`, the factor already present in the production identity; the
missing factor is `6 = |S₃|`.

**B. Mirror Frobenius relation.** In the pre-registered commutative class (`ℚ[x]/(x²)`, `S = id`)
every solution satisfies the mirror relation; no counterexample. Element-level argument that it
holds more generally in a **symmetric** category: apply `antipode_anti_comul` to the stated
relation `Δ(ab) = Δ(a)(1⊗b)`. With `antipode_anti_mul` this gives
`Δ(S b · S a) = (S b ⊗ 1) Δ(S a)`, and `S` is bijective (`antipode_involutive`), so
`Δ(cd) = (c ⊗ 1)Δ(d)`: the mirror relation. Not formalised; the braided (non-symmetric) case is
not checked. `counit_snake_left_of_mirror` (sorry-free) then gives the left snake identity for
`λ = ε`, `coev = η ≫ Δ`. So in the symmetric case `λ = ε` satisfies both snake identities.

## 16. Mirror relation in Lean; second ratio class (2026-11-21, owner: "1 2")

**Mirror relation, now proved** (`MirrorFrobeniusFromAntipode.lean`, sorry-free, axioms `propext`,
`Quot.sound`). `mirror_of_antipode`: for an algebra `A` over a commutative ring with the flip
braiding on `A ⊗ A`, the stated relation `Δ(ab) = Δ(a)(1⊗b)` plus `S` anti-multiplicative,
`Δ ∘ S = flip ∘ (S⊗S) ∘ Δ` and `S ∘ S = id` give `Δ(ab) = (a⊗1)Δ(b)`. With
`counit_snake_left_of_mirror` and `counit_snake_right`, **`λ = ε` with `coev = η ≫ Δ` satisfies both
snake identities in the symmetric case.** Scope: element level, flip braiding; the braided
non-symmetric case is still unchecked, and the bridge from `FrobeniusHopfData` morphisms in
`ModuleCat` to these element statements is not written.

**Second ratio class** (pre-registered and committed at `9ced266afbb` before the run;
`mn_pairing_ratio_class2_probe.py`). Pass criterion `12` identically in `q`:

| variant | proton | neutron | at `q = 1` |
|---|---|---|---|
| P1 pure weight states (each basis vector) | six different functions of `q` | | `2` each |
| P2 unnormalised sector traces `tr_sec(K X_N)/tr(K X_e)` | `−P(q)/(q⁵(q²+1)(q⁴+1))` | `−P(q)/(q⁷(q²+1)(q⁴+1))` | `3/4` |
| P3 Hecke symmetriser `X_N Σ_w T_w` | equal for p and n | | `4` |

(`P(q) = q¹² − 3q¹⁰ + 3q⁸ − 5q⁶ + 3q⁴ − 3q² + 1`.) **Scope-(a) negative**: no variant gives `12`.
Observation: in P2 the neutron is exactly `q⁻²` times the proton, which matches the Markov result
(§9) and is the only variant with the right split. Its value at `q = 1` is `3/4`, a factor `16`
short of `12`. Not pursued, since adjusting toward `12` would be selection.

## 17. λ = ε is forced, and it does not fix the scale (2026-11-21)

Pre-registered in `PREREGISTRATION-counit-pairing.md` (commit 2a1e36cc3c9, before the run).

**Correction of my own earlier claim.** In §16 I wrote that λ = ε is "the first route where
λ's scale is actually fixed". That is wrong. What was shown there was that λ = ε is *consistent*
with both snakes. Neither that nor anything below fixes the scale.

**Lean, sorry-free** (`QOU/MassTheory/CounitIsFrobeniusForm.lean`,
`counit_eq_frobeniusForm_of_coev`, `lean -DautoImplicit=false -s 65536` exit 0, axioms
`propext, Classical.choice, Quot.sound`). In every `FrobeniusHopfData`, `coevaluation = η ≫ Δ`
forces `ε = λ`. It uses the left snake, the right counit law, the right unit law and coherence.
It does not use the braiding, so it settles the braided case asked about in §16. It also does not
need the mirror relation, so `mirror_of_antipode` (§16) is no longer on this route's critical path.

**Scale, exact (probe part A, H₂(q), generic Frobenius form λ(1) = a, λ(σ) = b).** The counit
solved from the counit law is exactly (a, b), for every (a, b) with Gram determinant
(a + bq)(aq − b)/q ≠ 0. So ε = λ holds on the whole family and no normalisation is forced:
`(λ, coev) ↦ (sλ, s⁻¹coev)` moves `(Δ, ε) ↦ (s⁻¹Δ, sε)` and keeps both `coev = η ≫ Δ` and `ε = λ`.
The matter constant `ψ*·𝒟ψ = λ(S(ψ)·𝒟ψ)` therefore still scales by s, as in §13.

**Ratio, exact (probe part B, H₃(q) regular representation).** Frobenius form: the canonical
symmetrising trace τ(T_w) = δ_{w,e}. S(T_w) = T_{w⁻¹}. P(X) = τ(S(X)X), which is scale-free as a
ratio.
- P(X_e) = 1 for X_e = σ₀σ₁σ₀ (a basis element, so this is exact for every q).
- P(X_N) = (q⁴ − q² + 1)(q¹⁶ − 5q¹⁴ + 11q¹² − 16q¹⁰ + 19q⁸ − 16q⁶ + 11q⁴ − 5q² + 1)/q¹⁰ for
  X_N = (σ₀σ₁⁻¹)³.
- Ratio 1 at q = 1, 1.000348711784543 at the CODATA-2022 muon pin (mpmath, 30 digits).
Not 12: scope-(a) negative for this class. Checks passed: Hecke relation, braid relation,
τ symmetric on the basis.

**Structural context, not new here.** `FrobeniusHopfModelDichotomy.lean` (corpus, sorry-free)
already proves that in any monoidal-preadditive category whose scalars form a field, every
`FrobeniusHopfData` has A a zero object or a retract of the unit. So the full structure has no
non-trivial linear model, and any matter-pairing computation must be done in a Frobenius algebra
(as above) that does not satisfy all the antipode axioms. Part B's S preserves τ and reverses
products, but H₃(q) with its Frobenius coproduct is not a `FrobeniusHopfData`.

**Status of the 12.** Not found in the searched classes, now including λ = ε pairings in H₃(q).

## 18. What fixes λ's scale: a normalised state, not CAL-1 (2026-11-21)

No numerical test here, so no pre-registration.

**Corpus check.** In `CategoricalLagrangian` (`QDifferentialGeometry.lean`) the `costate` and
`state` are independent fields. Neither it nor `categorical-lagrangian.md` normalises the state.
CAL-1 enters as the base of the period tower (`electron-period-base.md`: `a_D^{(e)} = m_e`). It is
not stated anywhere as the electron's matter pairing (searched `quantum-observable-universes/` and
`mass-theory/`). So the CAL-1 route has no corpus anchor.

**Lean, sorry-free** (`QOU/MassTheory/NormalisedStateScaleFree.lean`, lean-direct exit 0, axioms
`propext, Classical.choice, Quot.sound`):
- `matter_rescale`: `(a•ψ*) ≫ (b•ψ) ≫ 𝒟 = (ab)•(ψ* ≫ ψ ≫ 𝒟)`;
- `norm_rescale`: `(b•ψ) ≫ (a•ψ*) = (ab)•(ψ ≫ ψ*)`;
- `matter_invariant_of_normalised`: if `ψ ≫ ψ* = 𝟙` both before and after, the matter term is
  unchanged.

Since `ψ* = λ∘S(ψ)` is linear in `λ`, a rescaling of `λ` is a rescaling of `ψ*`. Under the
normalisation `ψ ≫ ψ* = 𝟙`, the state absorbs it and the matter term does not move. The bosonic
term `𝒟²` never depended on `λ`. So with normalised states, the scale of `λ` is not a parameter of
`ℒ`. The only remaining scale is the overall unit, which is CAL-1's job anyway.

**What this does not settle.** The normalisation is a hypothesis, not in the corpus definition.
Adding it changes `def:categorical-lagrangian`, so it is the owner's decision.

**Bearing on §17 part B.** The quantity tested there, `τ(S(X)X)`, is exactly `ψ ≫ ψ*`. Under this
normalisation it is 1 for every state, so that ratio stops being a candidate for the 12. The
normalised matter constant is `ψ*(𝒟ψ)/ψ*(ψ)`. It needs a concrete `∇` on the state space, and
the corpus `nablaEndo` is still never instantiated (§10).

## 19. Trial: normalised states, downstream (2026-11-21)

Owner: *"Try 1 for now, see if it helps downsteam"*. Logged as a trial in
`docs/coordination/owner-rulings.md`. `def:categorical-lagrangian` is unchanged; the trial is the
separate structure `NormalisedCategoricalLagrangian` (`QOU/MassTheory/NormalisedLagrangian.lean`,
sorry-free, lean-direct exit 0, axioms `propext, Classical.choice, Quot.sound`).

**What it gives.**
- `matter_projector_idempotent`: `ψ* ≫ ψ` is idempotent, so the matter term is `𝒟` compressed
  onto the state's line.
- `matter_trace_eq_eigenvalue`: in the matrix model, `φψ = 1` and `Dψ = μψ` give `tr(Dψφ) = μ`.
- `weighted_matter_trace_eq_eigenvalue`: with `Kψ = wψ`, `tr(Kψφ D) = wμ`.
- So the own-sector constant `c` of §10 becomes the `∇`-eigenvalue `μ` of the normalised nucleon
  state (its expectation value when the state is not an eigenvector), with no scale attached. The
  neutron/proton horizontal split is `q⁻¹(q⁻¹ − q)μ` (`nucleon_horizontal_split`).

**What it does not give.**
- No number. The corpus has no concrete `∇` on the nucleon state space: `nablaEndo` is a free
  field, and the nucleon weight-space files (`NucleonWeightSpaceTwoTerm` and siblings) supply braid
  generators and charge operators, not a connection. Choosing one would be a new modelling choice,
  so I did not.
- It sharpens, not removes, the §10 conflict: with normalisation, the bridge's `hHoriz` plus the
  weight-vector and intertwiner conditions give `μ = 0` (`matrix_element_zero_of_equal_traces`),
  i.e. a vanishing own-sector constant.
- No 12. The 12 would now have to be the `∇`-eigenvalue of the nucleon state (in units where the
  overall scale is CAL-1), which makes the open question spectral and scale-free.

## 20. ∇ from the corpus SU(2) calculus: μ = 0 under the flat connection (2026-11-21)

Pre-registered in `PREREGISTRATION-su2-calculus-nabla.md` (commit 87ff912a34b, before the run).

**Corpus search.** The only concrete connection is on `O(SU(2))` with the left-invariant calculus
(`connection-su2.md`, `reeb-su2.md`): Reeb `ξ = ½ diag(1, −1)`, horizontal = no `ω₃` component.
Lean `nablaEndo` is never instantiated; the nucleon weight-space files define braid generators and
charge operators only. The connection 1-form `𝒜` is free data.

**Identification (mine, can be rejected).** On `(C²)^{⊗3}`, Reeb = Cartan `ξ_tot` and horizontal =
root vectors `E, F`, acting through the U_q(sl₂) coproduct; flat connection `𝒜 = 0`. The U_q
relations `KE = q²EK`, `KF = q⁻²FK`, `[E,F] = (K − K⁻¹)/(q − q⁻¹)` all check exactly.

**Results, exact, for every normalised state in each weight space (generic symbolic state):**

| | ⟨E⟩, ⟨F⟩ | ⟨ξ⟩ | K-weight | tr(Kψφ ξ) |
|---|---|---|---|---|
| proton `W(2,1)` | 0, 0 | +1/2 | q | q/2 |
| neutron `W(1,2)` | 0, 0 | −1/2 | q⁻¹ | −1/(2q) |

- Horizontal: `μ = 0`. Under the flat connection the own-sector constant `c` vanishes for every
  normalised weight state, because `E, F` shift weight. This agrees with the §19 route (the bridge's
  `hHoriz` forces `μ = 0`) and reaches it independently.
- Reeb: `ξ_tot` is the isospin `T³`. The K-weighted Reeb matter difference is
  `n − p = −(q² + 1)/(2q) = −[2]_q/2`, so the matter term contributes `−(1 − q⁻¹)[2]_q/2` to
  `τℒ_n − τℒ_p`. This is a model quantity; its sign is not compared to the mass splitting here,
  because the map from the sign of a trace of `ℒ` to a mass has not been derived.
- The 12: not attainable in this class.

**What would change this.** A non-zero own-sector constant needs a connection 1-form `𝒜` with a
weight-zero horizontal component. The corpus leaves `𝒜` free, so supplying one is a modelling
choice for the owner.

## 21. Horizontal connection from the braid holonomy: μ ≠ 0, exact q⁻² split, no 12 (2026-11-21)

Pre-registered in `PREREGISTRATION-holonomy-connection.md` (commit 9f63c356908, before the run).

**Corpus basis.** `MassTraceIdentity.lean`: the discrete multiplicative integral of a cycle is the
ordered product of its transports, and the mass trace is a functional of it. The canonical chain
turns non-abelian Stokes into the Hecke relation, so the nucleon holonomy is `B₃ = (σ₀σ₁⁻¹)³`.
Braid operators commute with U_q(sl₂), so they are weight-zero, which §20 showed is what `μ ≠ 0`
needs. **Identification (mine):** `∇_hol = hol − 1` (lattice convention). States: the normalised
eigenvectors of `B₃` itself, so no state is chosen against a target.

**Results, exact.**
- Spectrum of `B₃` is the **same** on `W_p` and `W_n`: `(t − 1)·(t² + c₁t + 1)` with
  `c₁ = (q¹² − 3q¹⁰ + 3q⁸ − 4q⁶ + 3q⁴ − 3q² + 1)/q⁶`. The eigenvalue 1 is the symmetric branch
  (`μ = 0`). The other two form the (2,1) block.
- So `μ` is identical for proton and neutron on each branch: the flip-intertwiner condition (b)
  holds automatically for this connection. With the K-weights, `q⁻¹·w·μ` gives
  **neutron = q⁻² × proton on every branch, exactly**: the own-sector split of §10 is reproduced
  with a non-zero constant.
- The two (2,1) eigenvalues are a complex-conjugate pair at the muon pin:
  `μ ≈ −0.0029070948 ± 0.0761953964 i`. Their sum is real:
  `Σμ = −(q² − 1)⁴(q⁴ + q² + 1)/q⁶`, ≈ −0.0058141896 at the pin, and `0` at `q = 1`
  (each `μ` vanishes to order `(q − 1)²`).
- Electron reference (`X_e = σ₀σ₁σ₀`, same convention): eigenvalues `1, −1, q³`, so
  `hol − 1 ∈ {0, −2, q³ − 1}` on both weight spaces.
- The 12: no `μ`, no n/p ratio and no nucleon/electron ratio equals 12 identically
  (`twelve_hits = []`). Scope-(a) negative.

**What this changes.** This is the first connection in the thread that gives a non-zero own-sector
constant and produces the q⁻² split, rather than assuming it. It rests on one identification
(`∇ = hol − 1`) that the corpus does not rule. A single eigenstate gives a complex `μ` at the pin;
only the block trace is real. Which of these (single state, or block trace) is the physical matter
constant is open.

**Side note (Lean, existing).** `massIntegrand_eq_id_of_frobeniusForm_eq_counit` needs
`frobeniusForm = counit`. §17's `counit_eq_frobeniusForm_of_coev` supplies it whenever
`coevaluation = η ≫ Δ`, so that hypothesis is now discharged from a structural one.

## 22. Complex geometry of the holonomy eigenvalue, and the Lean form of §21 (2026-11-21)

Owner: *"fall back to block, but try complex first .. look at complex Geom"*. Pre-registered in
`PREREGISTRATION-holonomy-complex-geometry.md` (commit a978cc01bf2, before the run).
Probe `mn_holonomy_complex_geometry_probe.py`, exact sympy, mpmath at the CODATA-2022 muon pin.

**The eigenvalue is a pure phase.** The non-trivial pair satisfies `t² + c₁t + 1 = 0`, so
`λ+λ− = 1`, and for `1/φ < q < φ` (φ the golden ratio) `|c₁| < 2`: the pair is `e^{±iθ}` on the
unit circle (elliptic). The boundary is exact: `c₁ − 2 = (q⁴ + 1)²(q² − q − 1)(q² + q − 1)/q⁶`,
which vanishes at `q = φ` and `q = 1/φ`. Outside that range the pair is real (loxodromic). The pin
`q₀ ≈ 1.10998` is elliptic: `θ = 0.0762693181392606636463`, `|λ| = 1`, complex length
`log λ = iθ` (real part zero to working precision): a pure rotation, no hyperbolic translation.

**Closed form of the complex μ.**
- `|μ|² = 2 + c₁ = h⁴[3]_q` exactly, with `h = q − q⁻¹`, `[3]_q = q² + 1 + q⁻²`.
- So `|μ| = 2 sin(θ/2) = h²√[3]_q` and `arg μ = (π + θ)/2`:
  `μ = h²√[3]_q · e^{i(π+θ)/2}`.
- At the pin: `|μ| = 0.0762508336791316063538`, `arg μ = 1.60893098586452695105`.
- Near `q = 1`: `θ = 4√3 ε² − 4√3 ε³ + O(ε⁴)` for `q = 1 + ε`, i.e. `θ ≈ √3 h²`.
- **Block fallback:** `μ + μ̄ = 2 Re μ = −h⁴[3]_q = −(q² − 1)⁴(q⁴ + q² + 1)/q⁶`.

No comparison with a hyperbolic volume, Chern–Simons invariant or measured number was made.

**Lean, sorry-free** (`QOU/MassTheory/HolonomyConnectionSplit.lean`, lean-direct exit 0, axioms
`propext, Classical.choice, Quot.sound`), over any field, built on the corpus intertwiner `P(q)`:
- `intertwine_Vpow`, `intertwine_V3`: `P Vpⁿ = Vnⁿ P`.
- `Vn3_conj`: `Vn³ = P Vp³ P⁻¹` (needs `q ≠ 0`, `q² + 1 ≠ 0`): same spectrum.
- `eigen_transfer`: `Vp³ψ = λψ` gives `Vn³(Pψ) = λ(Pψ)`, so `μ` is the same for p and n.
- `trace_Vp3_sub_three`: `tr(Vp³) − 3 = −(q² − 1)⁴(q⁴ + q² + 1)/q⁶` (agrees with §21's probe,
  which used the 8-dimensional tensor representation: an independent convention check).
- `two_add_c1_eq`: `2 + c₁ = h⁴[3]_q`; `c1_sub_two_eq`: the golden-ratio boundary.
