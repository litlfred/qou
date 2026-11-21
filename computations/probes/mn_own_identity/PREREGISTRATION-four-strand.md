# m_n by its own identity, four-strand lepton test: pre-registration (2026-11-21)

Written and committed **before any four-strand number is computed**. Follows
[`RESULT.md`](RESULT.md) (three strands: the identity forces `m_n = m_p`). Owner choice on the
thread card: "Draft PR plus lepton-strand test".

## Question

Does adding a lepton to the convention-D proton identity

  `m_p/m_e = 2 (Vol(4₁)/ℏ_q²) F_Bor(q) − 12`,  `F_Bor = tr_M(β_Bor)·[3]_q!/q³`

give a neutron identity that separates n from p, with no new constant?

## Fixed inputs (corpus, not chosen here)

- Photon `γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹`; nucleon element `V³ = (σ₁σ₂⁻¹)³` for both n and p
  (#8636 Part A, scope b).
- Electron word `σ₀σ₁σ₀ ∈ B₃`, Hopf-link closure (owner ruling 2026-11-21). Up quark = unknot strand.
- Convention-D Markov trace, `z_D = q³/(q²+1)`; whole-space weight `K^{⊗n}`, `K = q^{2T³}`.
- Jimbo Ř in the convention of `NucleonWeightSpaceTraces.lean`: `Ř(uu)=q uu`, `Ř(dd)=q dd`,
  `Ř(ud)=du`, `Ř(du)=ud + h du`, `h = q − q⁻¹`.
- Two-term trace: covariant all-pairs connected part (`BetaRoutesTwoTerm`).

## Choices this test makes (named, none selected by a number)

- **C-lep** (#8636 Part B): a fourth strand on the same `V` is the lepton doublet, `ν = u`, `e⁻ = d`.
  Then the `T³ = 0` space of `V^{⊗4}` splits as `N = n⊗ν = span(uddu, dudu, dduu)` and
  `P = p⊗e = span(duud, udud, uudd)`.
- **E-word**: the electron as its ruled `B₃` word on three strands of its own, split-unioned with the
  nucleon braid; the neutrino as one unknot strand.

## Arms and predictions

**L-A, spectator lepton strand (C-lep, element `V³ ⊗ 1`).** Sector trace of `V³⊗1` on `N` and on
`P` with weight `K^{⊗4}`. Both sectors have `K^{⊗4} = 1`, and `V³⊗1` restricts to `W_n⊗1`, `W_p⊗1`.
Prediction (certain, structural): `tr_N = tr_P`, so `m_n = m_p`, the same −1377 ppm miss. Two-term
connected part with SM charges (`u 2/3, d −1/3, ν 0, e −1`): prediction 0 for both, so no change.

**L-B, the #8636 selected four-strand word.** The γγ + reading-3 selection on four strands picks
`w ∈ {σ₁σ₃⁻¹, σ₃⁻¹σ₁}` for both states at `q₀`. Reading: replace `F_Bor` by
`F_Bor · tr_N(w)/tr_P(w)` for the neutron (ratio of compressed traces; the proton keeps `F_Bor`).
Prediction: the ratio is not 1; the isospin-½ character difference is first order in `q − 1`
(−0.2646 per #8636), so `m_n` misses by **tens of percent**, sign not predicted. Prior that it
lands within 0.1 % of CODATA m_n: < 2 %.

**L-C, electron as its ruled word (E-word).** By the Markov property the convention-D trace
factorises on a split union: `tr(V³ ⊔ X) = tr_M(V³)·tr_D(X)`. So the identity applied to the
composite gives `m(n⊗ν) = m_p` (neutrino strand trace 1) and
`m(p⊗e⁻) + 12 m_e = (m_p + 12 m_e)·tr_D(σ₀σ₁σ₀)`, `tr_D(σ₀σ₁σ₀) = q³(q⁴+1)/(q²+1)² ≈ 0.691`.
Prediction: the composite reading is **not additive**: it gives `m(p⊗e⁻) ≈ 0.69·m_p`, far from
`m_p + m_e`, about −31 %. This is a consistency test of reading the identity on a composite, not
a prediction of m_n.

## What would count

- A separation with `|m_n − CODATA| < 0.1 %` and no chosen constant: reported as a candidate, with
  every choice above listed. Not expected.
- Otherwise: L-A structural (scope b, invariant: `K^{⊗4} = 1` on both sectors plus #8636 Part A);
  L-B and L-C scope (a).

## Method

New probe `mn_four_strand_probe.py` in this directory: exact sympy over `ℚ(q)` on the 16-dim
`V^{⊗4}`, Ř checked against `A1, A2` of the three-strand probe and against #8636's
`χ^N − χ^P` on the isospin-½ block; mpmath 60 dps at the muon pin (honest test) and proton pin
(round trip). CODATA m_n, m_p only in comparison columns. Lean only if a structural statement
results (L-A).
