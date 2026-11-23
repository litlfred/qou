# Bridge B: what can and cannot split the neutron from the proton (2026-11-15/16)

Issue #8101. This is the second "bridge" of the 2026-11-15 derivation-chain audit (Lagrangian → trace → non-abelian
Stokes → weight-space decomposition → mass formula): the step from weight-space data to an MeV mass, tested on the
neutron–proton difference. It records negatives and two structural exclusions. **No content block is changed.**
The model terms "proton", "neutron", "u", "d" follow the repo's model-by-default ruling; physics enters only where a
number is set against CODATA, and those comparisons are marked.

Setting throughout: Jimbo braiding Ř on `(C²)^{⊗n}`, `h = q − q⁻¹`, convention-D pivot `K = diag(q, q⁻¹)`
(forced, `MarkovOrientationForced.lean`), γγ nucleon word `V³ = (σ₁σ₂⁻¹)³` (owner ruling, qou-ales), proton =
weight `+1` space of `(C²)^{⊗3}` (two u, one d; u = `T³ = +½`, merged #7971), neutron = weight `−1` space.
Values at the proton pin `q₀ = 1.1099785827513808`.

## Summary

| object tested | proton/neutron difference it produces | status |
|---|---|---|
| one scalar λ × Markov trace for every mass (B1) | Δm ≈ 0.039 MeV, and m_p/m_e ≈ 1 (vs 1836) | refuted, scope (a) |
| 𝒟² weight ratios as the source of the mass dressings | none (weights are pure powers of q) | refuted, scope (a) |
| KZ connection, every direction (Reeb, translation, transverse) | none | excluded, scope (b) |
| braid action, any signed word | none in the plain trace | **Lean**, scope (b) |
| any operator commuting with the total lowering operator `F₃` | none beyond the pivot `q²` | **Lean**, scope (b) |
| quantum trace restricted to the weight spaces | `T_p = q²·T_n`, the same for every word | **Lean** |
| any rule seeing only "same / different quark" | none (`u ↔ d` symmetric) | **Lean**, scope (b) |
| per-strand twist datum (hypercharge candidate) | constant `θ_V^{ΔT}`, ΔT assigned | scope (a) |
| any diagonal single-strand datum `a + b·h` | first order: exactly `−2b`, word-independent (an input) | scope (b) |
| one-photon exchange between tracked quarks (Y imported) | classical charge sums + `O(h⁴)` word-dependent term | probe, conditional |

**Bottom line.** Everything in the chain is built from braids, Hecke elements and the KZ connection, and these all
commute with the quantum-group symmetry (Schur–Weyl duality). Inside that class, proton and neutron can differ
only by the trace's own pivot weight (the fixed factor `q^{∓2}`) or by a datum imported by hand. A derived,
word-dependent n − p splitting needs an object that breaks that symmetry, and the corpus does not contain one.

## 1. B1: one scalar times a trace (scope a)

The action `𝔖 = λ·tr(ℒ)` has one scalar. Pre-registered reading: every mass is `λ ×` its trace, with the electron
word in `{V⁰, V³, V⁶}`. Exact result (`b1_electron_normalised_probe.py`): `Δm ≈ 0.039 MeV` (−97 %) and
`m_p/m_e ≈ 1` against CODATA 1836.15. Every Markov trace here is `1 + O(h²)`, so a linear trace → MeV map cannot
produce the lepton–hadron hierarchy. The restricted traces are `T(p) = 0.4087`, `T(n) = 0.3317`.

## 2. The mass dressings are not 𝒟² weight ratios (scope a; a proposal of this work, retracted)

The corpus uses three underived q-dressings: `c_q² = 1/(q−1)²` (mass–energy block), `1/ℏ_q² = q²/(q−1)²` (CAL-2
muon anchor) and `q⁻²/ℏ_q = 1/(q(q−1))` (hadronic `E₀`). A proposal made during this work read all three as ratios
of the weights of `𝒟²`, using `𝒟 = q⁻¹∇ + ℏ_q ι_ξ∇` with weights `q⁻¹` and `ℏ_q`. **That reading double-counted
the ξ-component.** Bridge A2 (`LagrangianKZIdentification.lean`, branch `claude/bridge-a-lagrangian-kz-2026-11-15`)
shows `𝒟 = P∘∇` with `P = q⁻¹` transverse to ξ and `P = q⁻¹ + ℏ_q = 1` on ξ. So the 𝒟² weights are `q⁻²`, `q⁻¹`, `1`:
pure powers of q, with no pole at `q = 1`, whereas every dressing has one. The proposal is refuted. The dressings
remain underived.

Recorded while checking this (not changed here): the Lean of `thm:mass-energy-equivalence` is definitional
(`categoricalMass q E := E·(q−1)²`), and Step 1 of its proof sketch is false as stated: with the Jimbo Ř and
`K = diag(q, 1/q)`, `Tr((K⊗K)Ř) = q(q²+1)`, not `q`. These go to the owner as a separate content question.

## 3. The KZ connection is isospin-blind (scope b; invariant: diagonal-sl₂ equivariance)

Each `Ω_ij = (C_ij − C_i − C_j)/2` is built from Casimirs, so it commutes with the total `E, F, H`
(`h2_kz_isospin_blind_probe.py`, exact at n = 3). Hence `ω(u) = Σ Ω_ij u_ij` is equivariant for every direction.
The characteristic polynomials of a generic `a·Ω₀₁ + b·Ω₀₂ + c·Ω₁₂` agree on the two weight spaces. The Reeb
contraction `ι_E ω = Σ Ω_ij` (Bridge A, `InfinitesimalPureBraid.lean`, `connForm_euler`) has spectrum
`{3/2, −3/2, −3/2}` on both. By A2, `𝒟` is exactly as blind as `∇`.

## 4. Lean: the plain trace is the same for every signed word, and the pivot is the whole split

`QOU/BraidsAndKnots/NucleonIsospinExclusions.lean` (generic `[Field R]`, `q ≠ 0`, `q² + 1 ≠ 0`):
- `trace_sword_eq`: for every **signed** braid word, the plain trace on the proton-type and neutron-type weight
  spaces agree. This extends `NucleonWeightSpaceTraces.trace_word_eq` (positive words only, np-splitting §17) via
  the Hecke relation `σ⁻¹ = σ − h` (`intertwine_inv`, with `A_i · inv(A_i) = 1` proved for each generator).
- `restrictedTrace_ratio`: `T_p = q²·T_n` for every signed word. `V3_ratio` instantiates it at the γγ word.

- **General form** (`commutant_trace_eq`, `commutant_restrictedTrace_ratio`): `P` is not ad hoc. With
  `Δ(F) = F⊗1 + K⁻¹⊗F` (the coproduct commuting with Ř), the block of `F₃` from the proton-type to the
  neutron-type weight space is `q·P` (`lowerBlock_eq`; `h3_lowering_block_probe.py`, exact). So **any**
  weight-preserving operator commuting with the total lowering operator has equal plain traces on the
  two spaces and restricted quantum traces in ratio `q²`. Braid words are one instance
  (`lowerBlock_intertwine_sword`). All declarations use only `propext`, `Classical.choice`, `Quot.sound`.

So the B1 split is entirely the pivot weight. Numerically `T(p)/T(n) = 1.232052454166767` against
`q₀² = 1.232052454166764`. The relative split is `1 − q⁻²` whatever the word. The same result was found
independently by the n–p thread (`2026-11-15` np-splitting audit §13, "n/p = q^{∓2} exactly").

## 5. Lean: same/different-quark rules cannot see `u ↔ d` (scope b; invariant: label complement)

Pre-registered rule "labelled V³": keep the γγ word, label the strands, keep the letter on a same-quark crossing
and use the derived weak element `W = (2/(q²+1))·½(σ+σ⁻¹)` on a u–d crossing. Exact result
(`a2_labelled_v3_probe.py`): for all three placements of the odd quark,
`t_p = t_n = (3q⁴ + 2q² + 3)²/(q²(q²+1)⁶)`, so Δm = 0.

The reason is general and is proved (`decorate_proton_eq_neutron`): uud and udd are label complements, and a rule
that sees only `l_a = l_b` gives the same decorated word for a labelling and its complement. The coloured-strand
(Yokonuma–Hecke) route reached the same conclusion through the colour flip (np-splitting audit §12).

## 6. Intrinsic u/d data on one strand (scope b; invariant: dim V = 2)

Every weight-preserving single-strand operator on `V = C²` is `a + b·h`. Summed over the quarks at one time slot it
equals `3a + b·H_total`, which commutes with Ř (checked exactly). So at first order any such datum (a mass term
`diag(m_u, m_d)`, a charge, a twist read as an operator) gives **n − p = −2b = m_d − m_u exactly, for every word**:
the braid contributes nothing, and the number is an input. The per-strand twist of `def:strand-twist-datum` acts on the
irreducible V by a scalar, so it gives a word-independent constant `θ_V^{ΔT}` with assigned ΔT. Off-diagonal
single-strand operators (E, F) vanish at first order in a diagonal trace; at second order they give the FE/EF terms
(q⁻² for the symmetric combination, np-splitting §20). The weak-vertex thread confirms the same structure from the
decay side: its emission asymmetry is exactly `2Y`, independent of q and of the word (ε-EM1).

## 7. One-photon exchange (probe; conditional on imported `Y = 1/3`)

The one object found that does depend on the word is a photon exchanged between two **tracked** quarks at two
different points of the braid. The braiding does not just carry a quark's charge to its new strand:
`Ř(h⊗1)Ř⁻¹ = 1⊗h − 2h·|↓↑⟩⟨↑↓|`. Rule (pre-registered): quark charge `Q = h/2 + 1/6` (SM hypercharge, **imported**),
ordered pairs of distinct quarks, uniform weight over the 21 slot pairs of the word, restricted traces as above
(`em1_photon_exchange_probe.py`). Equal-time symmetric Coulomb sums are excluded in advance, since
`Σ_{a<b} Q_aQ_b` is a function of totals.

| word | E(n) − E(p) at q₀ | at q = 1 |
|---|---|---|
| V³ | −0.6663932 | −2/3 |
| V⁶ | −0.6660752 | −2/3 |

At `q = 1` it reproduces the classical sums (p 0, n −2/3). The braid correction starts at `O(h⁴)` and depends on the
word (+0.042 % on V³, +0.089 % on V⁶). Comparison point (physics): the classical sign makes the proton heavier from
EM, which is the expected sign of the EM part; the measured total has the neutron heavier, so the larger non-EM term
is still missing. No MeV scale was chosen for E.

## 8. Corpus tension (reported, not edited)

`appendix-standard-model/sm-params-quark-masses.md` says the framework "derives both Δ_pn *and* its own
electromagnetic–strong decomposition", so `m_d − m_u` is "well-posed with no new inputs". Neither holds yet:
Δ_pn has several incompatible values with an asserted scale (`ScaleHypothesis`, no instance), and
`def:coulomb-charge` itself marks its EM reading open. Changing the sentence is a content change and waits on the owner.

## 9. What breaks the symmetry (search, pre-registered)

Criterion: an object counts only if it does not commute with `F₃` **and** has a framework-fixed size
other than the pivot. No hit.

- The pivot `K` breaks `u ↔ d`, with derived size `q^{∓2}`. That is the B1 split.
- The weak-vertex family (`L± = Ř₁^{±1}Ř₂^{±1}`, `P_L`, `P_R`, `J`, `Δ_S`) is built from polynomials in Ř,
  so it commutes with `F₃` and is excluded by `commutant_trace_eq`. This agrees with the weak-vertex
  thread's measurements ε-L1 and ε-TR1 (draft PR #8104).
- The corpus Higgs vacuum (`conj:g-action-on-substrate`, G-3/G-4) is a rank-1 projector on one weight
  line of the doublet, so it breaks the symmetry. Its direction comes from an assigned hypercharge
  `y = 1/2`, its norm from the measured VEV, and its coupling to quarks is not specified.
- The Coulomb insertion breaks the symmetry with asymmetry `2Y`, where Y is an input (§7).

Two tensions in `conj:g-action-on-substrate`, reported and not edited:
1. G-3 asks for a non-zero morphism `𝟏 → A^{(H)}` with `A^{(H)}` the spin-½ irrep. By Schur that
   Hom-space is zero in `Rep(SU_q(2))`, so a VEV cannot be a module map. It has to be adjoined from
   outside the equivariant category, which is the categorical form of the no-go above.
2. G-2/G-4 give `dim_q = [2]_q` for a rank-1 projector. A weight line has quantum dimension `q^{±1}`.

## 10. A type-B boundary picks a direction, not a size (2026-11-21)

This search was pre-registered in `h5_boundary_datum_preregistration.md`. The computations are exact, in `h5_boundary_sweep_probe.py` and `h5_ruled_photon_probe.py`.

A braid with a wall carries a boundary generator on an end strand. It acts by a 2×2 matrix `𝒦` that must solve the reflection equation `Ř𝒦Ř𝒦 = 𝒦Ř𝒦Ř`. For the Jimbo Ř, the only non-scalar solutions have one diagonal entry forced to zero: the `d` entry when the wall is at strand 1, and the `u` entry when it is at strand 3. In either case `𝒦` does not commute with `F₃`.

Only the diagonal of `𝒦` enters the restricted traces, so the type-B eigenvalues cancel from `T_p/T_n`. For the special pair V³ the ratio does not depend on where the boundary is inserted:

| wall | V³: `T_p/T_n` | at `q = 1` |
|---|---|---|
| strand 1 | `−q⁶(q⁶ − 3q⁴ + 3q² − 3)/(q⁶ − 2q⁴ + 3q² − 1)`, which is `2.4287166711934…` at `q₀` | 2 |
| strand 3 | `q⁸(q² − 2)(q⁴ − q² + 1)/(q¹² − 4q¹⁰ + 6q⁸ − 7q⁶ + 4q⁴ − 3q² + 1)` | 1/2 |

Check against the ruled photon `γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹`. V³ is the pair `γ(0,0,qh)·γ(0,0,−q⁻¹h)`. For a general pair `γ(φ)γ(φ′)`, the ratio depends on the photon parameters and on where the boundary is inserted. The general formula reduces exactly to the V³ row above.

This computes only the `M_QCD` term of the two-term trace. The `M_QED` charge term on a boundary would need `Y` and is not computed.

Verdict, scope (a). The boundary fixes the direction up to one binary choice, namely which end carries the wall. It does not fix the size of an n − p splitting, that is, the coupling between the boundary and the bulk.

### 10a. What fixes the coupling and the end: no hit (H6, 2026-11-21)

Pre-registered in `computations/probes/bridge_b/h6_boundary_coupling_preregistration.md`; result
in `h6_result.md`. Six candidates were checked, and none fixes `ε` or the end:
- the Stokes boundary term: the corpus has no forms (`qou-20bk`), and the surface-term coefficient is not derived;
- the type-B Markov value `q²(x+y)/(q²+1)`: still free;
- the XXZ surface term: restricted traces 0 on both spaces;
- folding, the Markov orientation, the over-strand rule, Reeb.

One exact fact sharpens the gap. Strand reversal composed with the flavour swap fixes the Jimbo
`Ř` and inverts the pivot `K`. So the end choice is the same bit as the sign of n − p. It is not a
second unknown. Scope (a).

### 10b. Forms for a Stokes boundary, and the M_QED wall term (H7, 2026-11-21)

Result in `computations/probes/bridge_b/h7_result.md`.

- **Forms.** Generic Lie-valued forms now exist (`QOU/Mathlib/LieValuedForms.lean`, rewired into
  `NonAbelianStokes.lean` today). No specific α, β is defined on the form side. A categorical connection `∇ : A → A ⊗ Ω¹(A)` does exist, but the categorical action `ev ∘ ℒ_q ∘ coev` is a closed trace with no boundary datum. Stokes is still an assumed class whose
  only model is trivial, and no wall sits on `cellBoundary`. No hit.
- **M_QED, carried all-pairs insertion.** It is constant on each weight space, so it factors out of
  the wall trace: n − p = −Y with or without the wall.
- **Slot-averaged exchange.** It is a virtual-photon model, which is not admissible (no virtual
  photons); comparison only.

### 10c. An open categorical trace with a boundary object (H8, 2026-11-21)

Result in `computations/probes/bridge_b/h8_result.md`. If the boundary inherits the action's λ, the
wall's effect beyond the pivot is set by `s = x + y` alone. No corpus statement fixes `s`.

- Folding (`s = h`, conditional on `conj:type-b-folding-cpt` plus an eigenvalue-matching reading)
  gives an order-`h` effect that vanishes at q = 1: `D(q₀) = 0.93996`.
- The Markov and quantum-dimension conventions give order-1 effects (5/7 at q = 1).

No hit.

### 10d. The folded wall (H9, 2026-11-21)

Result in `computations/probes/bridge_b/h9_result.md`. In the six-strand folded model the wall is the
middle crossing, so its size is fixed with no free number. Its effect beyond the pivot:
- is 1 at q = 1;
- at q₀ is `D = 0.958360` (mirror strands summed) or `0.957145` (mirror pinned to the ι-image).

It is not a hit. It is conditional on `conj:type-b-folding-cpt`, on the boundary sharing the bulk λ,
and on the choice of mirror reading.

### 10e. Folding breaks the bulk Hecke relation (H9b, 2026-11-21)

Result in `computations/probes/bridge_b/h9b_result.md`.

- A folded bulk generator is a product of two commuting crossings. It satisfies the cubic
  `(σ̂ − q²)(σ̂ + 1)(σ̂ − q⁻²) = 0`, not the Hecke quadratic. So braid-level folding derives the wall's
  Hecke relation but leaves `H₃(q)`, where the photon lives. `V³ ≠ γγ` after folding: 0.958360 against
  0.958055.
- For a general photon pair, `D = 1` at q = 1 for every φ, and `D` depends on φ at q₀.
- The Hecke-level reading (type B with equal parameters: the H5 wall with eigenvalues `{q, −q⁻¹}`, H8
  N1, `D(q₀) = 0.939957`) keeps the bulk Hecke.

### 10f. The wall's Hecke parameter from folding (H10, 2026-11-21)

Result in `computations/probes/bridge_b/h10_result.md`. In the folding, the bulk type-B generator is a
length-2 pair and the wall has length 1. With Lusztig's weight function `L = ℓ` restricted to the
fixed-point group, the wall's parameter is the square root of the bulk's: `Q = q^{1/2}`. That gives
`D(q₀) = 0.968071` on V³ and `D = 1` at q = 1.

It is a conditional derivation: it rests on `conj:type-b-folding-cpt`, on the boundary sharing λ, and on
the Lusztig monograph, which is not held. Equal parameters (`0.939957`) has no corpus support. A
Markov condition fixes a trace value, not `Q`.

### 10g. Lusztig's monograph read: normalisation corrected (H10b, 2026-11-21)

The source is now held (`uploads/0208154v2.pdf`, commit `f5d31c46b93`). §16.2 confirms the folding rule: the fixed group is Coxeter on the orbit longest elements, with the weight function L equal to the restricted ambient length. So the wall has L = 1 and the bulk L = 2. §16.7(b) fixes the quadratic relations with the **ambient** v. `conj:type-b-folding-cpt` folds the physical H_n(q), so v = q: the folded bulk is at q² and the wall at q. H10 had set the folded bulk to q (v = q^{1/2}), which does not match the conjecture's ambient. On V³ the supported reading gives D(q₀) = 0.94911520554914481986 (H10 as written: 0.96807142877888556063); D(1) = 1 in both. Whether the photon words live in the folded bulk (q²) or the ambient (q) is a new open input. D is a trace ratio, not a mass. Details: `computations/probes/bridge_b/h10_result.md` and `h10b_lusztig_normalisation_probe.py`.

### 10h. Where the photon word lives (H11, 2026-11-21)

The corpus fixes the home: `conj:type-b-folding-cpt` folds the physical H_n(q), and the owner ruling of 2026-11-21 writes the nucleon word in the ambient six-strand H_6(q), mirrors summed. So the words live in the ambient at q. What is open is the descent to the type-B algebra: Lusztig §16 uses the ι-twisted K♯ trace (traceless swapped pairs vanish), while the ruling uses a plain trace. A one-letter toy check gives plain {q², −1, −1, q⁻²}, naive swap trace {q², q⁻²}, Lusztig {q², −q⁻²}; the naive model has the wrong sign on the q⁻² line. Reading B (0.949115) is the K♯-level descent and has no strand-level model in the corpus. Details: `computations/probes/bridge_b/h11_result.md`.

### 10i. Graded strand model for the descent (H12, 2026-11-21)

Grading the σ eigenlines with the −q⁻¹ line odd and putting a Koszul sign on the doubled letter makes the mirror-twisted trace reproduce Lusztig's folded letter {q², −q⁻²} for one letter and for two commuting letters; the opposite grading fails. The test is weak (diagonal, target known in advance), the Koszul sign is a modelling choice, and non-commuting letters, the wall and V³ are untested. Details: `computations/probes/bridge_b/h12_result.md`.

### 10j. The graded six-strand test fails (H13, 2026-11-21)

Written inside H₆(q), H12's per-letter Koszul sign (bᵢ = σ̂ᵢ − 2q⁻²E₃₊ᵢE₃₋ᵢ, mirror ι = reversal with basis flip) is ι-equivariant. But the folded quadratic holds under the twisted trace only for F ∈ {1, b₁}, and the graded letters break the type-B braid relations as operators (exact, q = 3/2 and 2). Scope (a): this construction is not a model of Lusztig's descent. His sign lives on the per-element structures φ_x (§16.4), not per letter. D was not computed. Details: `computations/probes/bridge_b/h13_result.md`.

### 10k. Whole-word KL signs reproduce Lusztig's descent (H14, 2026-11-21)

The KL bases of S₆ (equal parameters) and of its ι-fixed B₃ with L = (1, 2, 2) were computed independently. For all 847 pairs y ≤ x in W, every folded coefficient is ≡ the ambient one mod 2 and no larger in absolute value, as Lusztig §16.6 predicts. The equal-parameter control fails. The two differ at 188 positions, 90 of them negative: the sign lives on whole words, which is why H13's per-crossing sign failed. This gives a strand-level model of reading B (bulk q², wall q). Necessary-condition check, not a proof. Details: `computations/probes/bridge_b/h14_result.md`.

### 10l. Folding rule for all n, and the V³ word through the descent (H15, H16, 2026-11-21)

H15: the KL-level check of §10k passes for n = 3..7. Even n folds to B_{n/2} with wall weight 1. Odd n folds to B_{(n−1)/2} with the middle generator s_m s_{m+1} s_m, of weight 3 (A₁ at n = 3). Details: `h15_result.md`.

H16: the six-strand V³ word (H9), folded by Lusztig's descent and traced by the H8 functional, gives D = 0.94911520554914481986 at q₀, i.e. reading B to 20 digits. The naive untwisted projection agrees only mod 2 and gives D = 0.93900102455152553557; the two agree at q → 1. D is a trace ratio, not a mass. Necessary-condition check, not a proof. Details: `computations/probes/bridge_b/h16_result.md`.

### 10m. The descent at n = 4 and n = 5 (H17, 2026-11-21)

Both cases fold to B₂: bulk b of weight 2, and wall w of weight 1 at n = 4 or 3 at n = 5. On the stand-in word (T_b T_w⁻¹)³, Lusztig's descent and the naive projection agree mod 2 and differ as Laurent polynomials at both n. This matches H16 at n = 6, so the weight-3 wall added to conj:type-b-folding-cpt passes the same necessary check. The two-strand trace model satisfies the B₂ relation for every wall parameter, so it cannot test the weight. B₂ has no second bulk letter, so this is not the photon vertex. Details: `computations/probes/bridge_b/h17_result.md`.

### 10n. A model that forces the weight: even n passes, odd n untested (H18, 2026-11-21)

The ambient Jimbo module (C²)^{⊗n} is used with ι realised as J = (spin flip)·(strand reversal). The twisted power sums tr(J A^k) of each orbit generator then fix its weight from the ambient operator alone. At n = 4 and 6 the weight is forced, to 1 for the fixed root and 2 for swapped pairs, and every wrong weight fails. The swapped pairs carry the sign +v⁻² rather than Lusztig's −v⁻², a sign-normalisation question (§16.4) that is left open. At n = 5 and 7 every twisted power sum vanishes, because the module has zero twisted character at odd n. The weight-3 wall is therefore neither tested nor refuted. A spin-1 module would test it. Details: `computations/probes/bridge_b/h18_result.md`.

### 10o. The weight-3 wall on a three-state module (H19, 2026-11-21)

H18's test was re-run on the three-state Hecke module (C³)^{⊗n} with the gl₃ Jimbo Ř. The spin-1 sl₂ R-matrix has three eigenvalues and is not a Hecke representation, so this gl₃ module stands in for it. The N = 2 control reproduces H18 exactly. At n = 4..7 every orbit's weight is forced to its ambient length: 1 for the fixed root, 2 for swapped pairs, and 3 for the middle orbit s_m s_{m+1} s_m at n = 5 and 7, whose twisted power sums are now non-zero. The weight-3 wall carries Lusztig's sign −v⁻³. The swapped pairs still carry +v⁻² against Lusztig's −v⁻², the same open normalisation question as H18. Necessary-condition check, not a proof. Details: `computations/probes/bridge_b/h19_result.md`.

### 10p. Why the swapped pairs carry +v⁻² (H20, 2026-11-21)

On every swapped-pair orbit of (C^N)^{⊗n} (N = 2, 3; n = 4..7), the twisted power sums are exactly c₊ v^{2k} + c₋ v^{−2k}, and the mixed joint eigenspaces contribute 0. Reason: J swaps the commuting generators T_i and T_{n−i}, so it moves every joint eigenspace with unequal eigenvalues, and only the squares v² and (−v⁻¹)² = +v⁻² survive. So the +v⁻² of §10n and §10o is forced for any module in which J swaps two commuting generators, and a J-twisted trace of the ambient pair product cannot give Lusztig's −v⁻². Whether another twist does is not tested. Details: `computations/probes/bridge_b/h20_result.md`.

## 11. What remains open

- A symmetry-breaking object (a vacuum or boundary choice in the Higgs role) that distinguishes u from d inside the
  framework. Without it, `m_d − m_u` is an input.
- The MeV scale of any trace-level n − p quantity (`H_α` is asserted, `E₀` is linear in traces, neither is derived for
  this use).
- The hierarchy factor `1/ℏ_q²` (muon anchor) and its siblings: underived.

Probes: `computations/probes/bridge_b/` (exact sympy; numbers at `q₀` by mpmath or exact rationals; outputs in
`*.out.txt`). Project-file copies with pre-registrations: `qou-derivation-chain/bridge-b/`.
