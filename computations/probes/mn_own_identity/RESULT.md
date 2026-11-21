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
