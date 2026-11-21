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
