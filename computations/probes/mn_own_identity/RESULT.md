# m_n by its own identity: result (2026-11-21)

Pre-registration: [`PREREGISTRATION.md`](PREREGISTRATION.md) (commit `4f0014973`, before any
number). Lean: `folio/quantum-observable-universe/lean/QOU/MassTheory/NeutronOwnIdentity.lean`.
Probe: [`mn_own_identity_probe.py`](mn_own_identity_probe.py), output
[`mn_own_identity_probe.out.json`](mn_own_identity_probe.out.json) (9/9 exact checks pass;
values at 60 dps). Disclosure: S1 below was checked once in sympy before the pre-registration
was written, to confirm the convention; every other check and every number came after.

## Short answer

**The proton identity has no neutron analogue that separates n from p.** Its trace
`tr_M(β_Bor)` is the convention-D trace of `V³` over the **whole** isospin multiplet (all
four `T³` sectors uuu, uud, udd, ddd), and it is invariant under `u ↔ d`. The γγ selection
gives the same element `V³` for n and p (#8636), and the two-term trace adds 0 on quark-only
words (`pairSum_eq_of_total_eq`). So the literal neutron identity is the proton identity, and
it gives **m_n = m_p**. The one state-sensitive reading (the nucleon's own `T³` sector) gives
`m_n/m_p ≈ q⁻²`, a 19 % miss with the neutron lighter. A single-scale m_n is not available
from the corpus readings; the n–p difference needs an ingredient outside this identity.

## Structural results (Lean, generic `[Field R]`)

| theorem | statement |
|---|---|
| `wholeTrace_eq_trM` | `tr_M(β_Bor) = (q³·1 + q·tr_{W_p}(V³) + q⁻¹·tr_{W_n}(V³) + q⁻³·1)/[2]³` |
| `wholeTrace_reflect` | the weight reflection `K ↦ K⁻¹` (`u ↔ d`) leaves it unchanged |
| `FNeutronN0_eq_FBor`, `neutron_identity_forces_equal_mass` | proton identity ∧ N0 neutron identity ⇒ `m_n = m_p` |
| `sector_ratio`, `n1_difference` | sector reading N1: `F^(n) = q⁻² F^(p)`, so `m_n − m_p = 2 m_μ F_Bor (q⁻² − 1)` |

Sector shares of `tr_M(β_Bor)` at the muon q₀: uuu 0.1684, **uud (proton) 0.4093**,
**udd (neutron) 0.3322**, ddd 0.0901. The proton identity reads 59 % of its trace from
sectors that are not the proton.

## Values (MeV; CODATA in comparison columns only)

| reading | muon pin (honest test) | vs CODATA m_n | proton pin (round trip) | vs CODATA m_n |
|---|---|---|---|---|
| proton identity, m_p | 938.271861 | (m_p: −0.244 ppm) | 938.272089 | (m_p: 0, by construction) |
| **N0** literal, m_n | **938.271861** | **−1376.8 ppm (−1.2936 MeV)** | 938.272089 | −1376.5 ppm |
| N1 own T³ sector | 760.397 | −19.07 % | 760.397 | −19.07 % |
| N2a bar mirror of F_Bor | 1760.09 | +87.3 % | 1760.09 | +87.3 % |
| N2b bar mirror of F_Bor/ℏ_q² | 1427.43 | +51.9 % | 1427.43 | +51.9 % |

q₀(muon) = 1.10997859564273904668, q₀(proton) = 1.10997858275138080759. Every pre-registered
prediction held (N0 −1377 ppm, N1 ≈ 760 MeV / −19 %, N2 tens of percent).

## Scope of the negative

- **N0 is a structural exclusion (scope b) for this functional.** The invariant is
  `wholeTrace_reflect` (`u ↔ d` symmetry of the whole-space trace) together with the
  same-element theorem of #8636. Any identity built from `tr_M(β_Bor)`, `[3]_q!`, `q`, `ℏ_q`,
  `Vol` and `m_e` alone gives the same value for n and p.
- **N1 and N2 are scope (a).** These readings, on their own, miss by 19–87 %. That does not
  exclude sector traces or the bar involution from a larger closure.
- **The −12** is the same constant in N0 (sibling item 3 owns its derivation); it does not
  affect the conclusion, which holds for any constant common to n and p.
- **Two-term trace** is cited, not re-proved: the covariant all-pairs connected part is 0 on
  every quark-only word, so one-term and two-term agree on `V³` for both nucleons.

## What would separate n from p (not done, not chosen)

1. A state-sensitive selection plus a fourth (lepton) strand: #8636 Part B shows the n⊗ν and
   p⊗e⁻ characters differ on four strands, but the selected word stays the same for q < q* =
   1.15096, and q₀ lies inside that window.
2. A flavour functional that is not `u ↔ d` symmetric, e.g. `ε_flavour(V³)`
   (`FlavourWeightSplit`), which needs the separate scale E₀ — exactly what this route set out
   to avoid.
3. Reading the identity as an isospin-multiplet (nucleon-average) observable. That is a
   relabelling, not a derivation; at the muon pin, as M_N = (m_p+m_n)/2 it would be −689 ppm.

## Four-strand lepton test (added 2026-11-21)

Pre-registration: [`PREREGISTRATION-four-strand.md`](PREREGISTRATION-four-strand.md) (commit
`ab73baa376a`, before any number). Probe [`mn_four_strand_probe.py`](mn_four_strand_probe.py),
output [`mn_four_strand_probe.out.json`](mn_four_strand_probe.out.json): 12/12 exact checks pass
(Ř reproduces the three-strand matrices, Hecke and braid relations, `tr_M(V³)` closed form,
#8636's amplitude norm `(q⁴+1)/q²`, `tr_D(σ₀σ₁σ₀) = q³(q⁴+1)/(q²+1)²`, split-union factorisation).

| arm | what it is | m_n or composite (muon pin, MeV) | vs CODATA | prediction held? |
|---|---|---|---|---|
| L-A | spectator lepton strand, `V³⊗1` on `N = n⊗ν`, `P = p⊗e` | 938.271861 | −1376.8 ppm | yes (equal, exact) |
| L-B | #8636 selected word `σ₁σ₃⁻¹` (and `σ₃⁻¹σ₁`), `F^(n) = F_Bor·tr_N(w)/tr_P(w)` | **981.43** | **+4.46 %**, neutron heavier | partly: separates, but 4.5 % not "tens of %" |
| L-C | electron word `σ₀σ₁σ₀` split-unioned with `V³` | m(p⊗e⁻) = 646.61 | −31.12 % vs m_p + m_e | yes |

Proton pin agrees within 0.25 ppm on every row.

- **L-A is structural (scope b).** Both sectors have `K^{⊗4} = 1`, `V³⊗1` restricts to `W_n` and
  `W_p`, and `tr_{W_n}(V³) = tr_{W_p}(V³)`. The two-term connected part is 0 on both sectors with
  SM charges (`ν 0, e −1`); the raw parts differ, but they are not the two-term trace.
- **L-B** is the only arm that separates n and p. Exactly, `tr_N(w) = 1` and
  `tr_P(w) = (3q² − q⁴ − 1)/q²`, so the ratio is `q²/(3q² − q⁴ − 1) = 1.0457`, first order in
  `q − 1`. The neutron comes out heavier, but by 43 MeV instead of 1.29 MeV. Scope (a): this reading,
  with these choices (C-lep, the selected word, the trace ratio as the neutron's factor), misses.
- **L-C** shows that the identity cannot be read on a split composite: the convention-D trace
  multiplies (`tr_D(σ₀σ₁σ₀) = 0.691`), while masses add. Scope (a), a consistency failure of the
  composite reading, not a value of m_n.

**Lean (formalize-first, owner rule 2026-11-21):**
`folio/quantum-observable-universe/lean/QOU/MassTheory/NeutronFourStrand.lean`, generic `[Field R]`,
`lean -DautoImplicit=false -s 65536` exit 0, `#print axioms` on all ten theorems: `propext,
Classical.choice, Quot.sound`. It puts `σ₁, σ₂, σ₃` on the six-dimensional `T³ = 0` block
(`N ⊕ P`), checks the Hecke relation for `σ₃` and the braid relations `σ₁σ₃ = σ₃σ₁`,
`σ₂σ₃σ₂ = σ₃σ₂σ₃`, and proves L-A (`trN_V3_eq_trP_V3`), L-B (`trN_w = 1`, `trP_w = 1 − h²`,
`LB_factor`: under L-B the neutron factor is `1/(1 − h²)` exactly).

**Small derivable terms, kept (owner rule 2026-11-21: do not drop a derivable correction because
a larger gap dominates).** The only derivable correction inside these arms is the two-term trace.
It is computed, not dropped: the covariant all-pairs pair charge is the same scalar on every basis
state of a sector (`−1/3` on `N`, `−1` on `P`), so its connected part is exactly 0 for **every**
element, including the selected word (`twoTerm_connected_zero`; probe agrees). The raw (unconnected)
two-term parts on `w` differ (`−1/3` on `N`, `−(1 − h²)` on `P`), but the raw part is not
the ruled two-term trace. Not derivable here, so not included: a lepton-sector constant in place of
the `−12`, and the coupling `c_em` (it multiplies 0 in any case).

## Two-term Lagrangian under a connection (added 2026-11-21; details in LITERATURE-COMPARISON §17–§27)

ℒ = 𝒟² + ψ*⊗𝒟ψ, 𝒟 = q⁻¹∇ + (1 − q⁻¹)ι_ξ∇. All results below are symbolic in q. No measured
value enters, and none is compared.

**Derived (Lean, sorry-free, standard axioms).**

| file | result |
|---|---|
| `CounitIsFrobeniusForm` | coev = η≫Δ forces ε = λ (no braiding). The scale of λ stays free. |
| `NormalisedStateScaleFree`, `NormalisedLagrangian` | a normalised state (ψ≫ψ* = 1, owner trial ruling 2026-11-21) removes λ's scale; the matter trace becomes the ∇-eigenvalue μ (Cartan-weighted: wμ). |
| `HolonomyConnectionSplit` | with ∇ = hol − 1, hol = (σ₀σ₁⁻¹)³: neutron hol = P·(proton hol)·P⁻¹, so the spectra are equal; the Cartan weights give μ_n = q⁻²μ_p; tr hol_p − 3 = −h⁴[3]_q. |
| `DeltaNPMatrixIdentity` | for any connection F with conjugate neutron block: tr(𝒟_n²) − tr(𝒟_p²) = −2q⁻¹(1 − q⁻¹)·tr F_p (cross term only). With F = hol − 1: Δ = 2q⁻¹(1 − q⁻¹)h⁴[3]_q = 3h⁵ + O(h⁶). |
| `HolonomyTLStateSum` | in the mass identity's expansion T(σ^{±1}) = q^{±1}·1 − e, hol − 1 for (σ₀σ₁⁻¹)³ is exactly the sum of the 63 states with at least one Temperley–Lieb generator (any R-algebra). |
| `TwelveNotHolonomyMultiple` | h⁴[3]_q and Δ vanish at q = 1, so no q-independent κ gives κ·f = 12. |

**Negatives (scope (a), each one pre-registered definition).**
- SU(2) calculus with flat ∇: μ = 0 on the horizontal part.
- 𝒟² leading count: N = tr(D₁²) = 3/8 (D₁ = T³/2; holonomy is O(h²)). Not 12.
- n − p of tr(𝒟²): 3h⁵. Not 12.
- The 12 in m_p = 2m_μF_Bor − 12m_e is ruled a fit (2026-11-18), and nothing here derives it.

**Open, owner's call.** The connection. The p/n conjugacy and the q⁻² split hold for every F(hol).
A nonzero Δ needs a connection with nonzero trace: hol − 1 has one, while log hol and the part odd
under hol ↦ hol⁻¹ give Δ = 0. The corpus reason for hol − 1 is `HolonomyTLStateSum`: the mass
identity consumes hol linearly, and hol − 1 is its Temperley–Lieb part. The reason against is that
a classical connection is a Lie-algebra 1-form, i.e. log hol. The corpus defines ∇ : A → A ⊗ Ω¹ as
given, so neither is forced. Also not derived: a map from the dimensionless Δ or μ to MeV.

**At q = 1 (added 2026-11-21, LITERATURE-COMPARISON §29; Lean `NucleonDiracVanishesAtOne`).**
V³(1) = 1, so the nucleon 𝒟 is 0 at q = 1 and every trace with a 𝒟 factor vanishes there for
n and p; the electron's does not (tr 𝒟_e(1)² = 4). So no ℒ term with ∇ = F(hol), F(1) = 0 and
q-independent insertions gives an n − p that survives at q = 1 (scope b, invariant V³(1) = 1).
The corpus quark-charge term (−⅓·tr V³ on n, 0 on p) does survive at q = 1, but it has degree 0
in 𝒟 and is outside ℒ as written.

**Static charge term (added 2026-11-21, LITERATURE-COMPARISON §31; Lean `StaticChargeTermNP`).**
ℒ′ = 𝒟² + QPair·hol, linear map fixed on the electron: m_n − m_p = −54.33 keV (plain) /
−48.91 keV (K-weighted) at the proton pin, limit −m_e/8 at q = 1. Pre-registered and held.
Opposite sign to CODATA and about 4 % of its size (scope (a)).
