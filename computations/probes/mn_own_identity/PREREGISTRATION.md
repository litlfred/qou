# Pre-registration: m_n by its own identity (2026-11-21)

Written and committed before any number below was computed. Repo main `845e2f820`.

## The question

The production proton identity (convention D) is

    m_p/m_e = 2 (Vol(4₁)/ℏ_q²) F_Bor(q) − 12,   F_Bor = |tr_M(β_Bor)| [3]_q! / q³,

with tr_M(β_Bor) = (4 + h² − 3h⁴ − h⁶)/(h² + 4), h = q − q⁻¹. Goal: state the neutron's
own identity of this shape, evaluate it at q₀ (muon pin = the honest test; proton pin = a
round trip), and report m_n directly, not as m_p + Q_β + m_e. Framework (owner rulings,
`docs/coordination/owner-rulings.md`): photon γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹; electron
σ₀σ₁σ₀ ∈ B₃ (Hopf closure); up quark = unknot strand; two-term Lagrangian trace.

## Corpus facts used (cited, not re-derived)

- β_Bor = V³ = (σ₁σ₂⁻¹)³ = γ(0,0,qh)·γ(0,0,−q⁻¹h) (`borromeanV3A_eq_switched_photon_product`).
- p and n are the T³ = +½ and −½ weight spaces W_p, W_n of (C²)^⊗3, with u = e₁
  (`docs/audits/2026-11-20-qbeta-flavour-weight-split.md`).
- The γγ + reading-3 selection gives the SAME element for n and p on three strands (#8636,
  scope b, `isoChar_eq`), and tr_{W_p}(V³) = tr_{W_n}(V³) (`trace_borromeanV3A/B`).
- The covariant all-pairs two-term connected part vanishes on every quark-only word
  (`pairSum_eq_of_total_eq`, `QOU.QBeta.BetaRoutesTwoTerm`; scored value 0 on V³).
- Pivot: T_p = q² T_n (#8734).

## Structural claim to prove in Lean first (prediction)

S1. tr_M(β_Bor) is the whole-space convention-D quantum trace
    Tr(K^{⊗3} V³)/[2]³ = (q³ + q⁻³ + [2]_q · tr_W(V³)) / [2]_q³,
    i.e. a sum over all four T³ sectors (uuu, uud, udd, ddd). Prior: 90 %.
S2. It is invariant under the weight reflection K ↦ K⁻¹ (which exchanges the uud and udd
    sectors). Prior: 95 % given S1.
S3. Hence the literal neutron identity (same element, same trace, two-term adds 0) has
    F^(n) = F_Bor exactly, and the two identities together force m_n = m_p. Prior: 90 %.

## Candidate neutron identities and predicted outcomes

| id | reading | predicted value |
|---|---|---|
| N0 | literal: same word V³, same whole-space (two-term) trace | m_n = m_p exactly. Muon pin: m_n ≈ 938.2719 MeV, ≈ −1377 ppm vs CODATA m_n (i.e. misses by ≈ −1.29 MeV). Proton pin: m_n = CODATA m_p, ≈ −1376 ppm. |
| N1 | sector-resolved: leading term ∝ the nucleon's own T³ component ε_N(V³) = q^{±1} tr_W/[2]³, so F^(n) = q⁻² F^(p) | m_n/m_e = 2(Vol/ℏ²)F_Bor q⁻² − 12: m_n ≈ 760 MeV, ≈ −19 %; neutron LIGHTER (consistent with sibling (1)'s sign question). |
| N2 | bar mirror of the whole identity (q ↦ q⁻¹ in F_Bor and ℏ_q, #8734 "bar = mirror") | F ratio q⁶ on F_Bor alone (m_n ≈ 1.87 × tower), q⁴ with ℏ_q included: off by tens of percent. Scope-(a) negative. |

Prior that ANY of N0–N2 lands within 100 ppm of CODATA m_n: < 2 %.
Prior that the honest outcome is "no single-scale neutron identity among the corpus readings
separates n from p": ~85 %.

## Discipline

Exact arithmetic (sympy ℚ(q)) for identities; mpmath ≥ 50 dps for values; no float64.
CODATA m_n, m_p, m_μ appear in comparison rows only (and m_μ/m_e in the muon pin, CAL-2).
Nothing is fitted; no candidate is selected by accuracy. Every candidate is reported.
