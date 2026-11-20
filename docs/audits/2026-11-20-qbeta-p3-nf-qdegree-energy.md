# P3: β-decay energy as a change of normal-form q-degree / Bruhat length

Bean `qou-99qc`. Owner (Carl, 2026-11-20 20:52): β-decay is an interaction and a
Gröbner–Shirshov calculation; is one side "at a higher q power"? P3 (owner-selected cheap
diagnostic): read an energy off the change of a normal-form q-degree or Bruhat length between
the initial and final states of n → p e⁻ ν̄. PR #8682. Nothing is wired; CODATA and the scored
0.3254 MeV cell (#8586) appear only as comparison rows.

Pre-registration: `computations/probes/qbeta_nf_qdegree/PREREGISTRATION.md` (committed first,
`7f9016bf4e`). Lean: `QOU/QBeta/NormalFormLengthInvariants.lean`. Probe and witness:
`computations/probes/qbeta_nf_qdegree/` (10/10, sympy exact in ℚ(q), mpmath 70 dps, proton q₀).

## 1. Answer

- **Yes, the proton sits two q-powers above the neutron**, under the index character
  χ(x) = Σ_w c_w q^{ℓ(w)} (the length-weighted functional T_w ↦ q^{ℓ(w)}): χ(p) = q²·χ(n) in
  both typed-crossing models (`lenWeighted_nucP_eq_sq_mul`, sorry-free; probe for the 11-letter
  model). A typed crossing contributes χ = q (σ), (q+q⁻¹)/2 (the averaged σ − h/2) or q⁻¹
  (σ⁻¹ = σ − h); the proton and neutron words differ by one σ against one σ⁻¹, so the ratio is q². This is the same +2 as the Cartan charge of T⁺ found by #8661.
- **On the γγ base V³ = (σ₁σ₂⁻¹)³, which is the same element for p and n, every invariant gives
  Δ = 0** for the nucleons (`lenWeighted_V3`: χ(V³) = 1). Any non-zero Δ is then the lepton's.
- **Leading Bruhat length never separates n from p** (2 and 2 short; 3 and 3 long; 2 and 2 on V³).
  Δℓ_lead for the decay is the electron's own length: 1 (trefoil σ₁³ in H₂) or 3 (σ₁σ₂σ₁).
- **No invariant gives Q_β without a chosen scale**, and the χ-degree cannot be an energy with one
  linear scale: the proton has the higher degree but is lighter, and the electron has positive
  degree (+3) and is massive. E = κ·deg would need κ < 0 for the nucleons and κ > 0 for the
  electron. This is a sign argument on these element assignments (scope (a) for the route; the
  invariant is the sign of Δdeg).

## 2. Why these invariants, and the contrast with the step count

`beta-decay-skein-properties` reads Q off the count of rewrite steps. R3 (#8632) measured 25
(leftmost-first) against 30 (rightmost-first) quadratic steps on (σ₁σ₂)⁵, with one normal form.
The probe reproduces both counts and checks the normal form against the Lean operators.

The Lean file proves (generic `CommRing`): the right actions of σ₁, σ₂ on T_w coefficient vectors
satisfy the quadratic and braid relations (`act_quad`, `act_braid`), so a rewrite at any position
of a word leaves the coefficient vector unchanged (`eval_quad`, `eval_braid`), and the reduced
words give the basis (`eval_reduced`). Every invariant below is a function of that vector, so it is
rewrite-order independent. For the corpus energy of `thm:groebner-shirshov-energy`,
E(ξ) = Σ_w |c_w|ℓ(w), this is the H₃ case of the statement bean `qou-n2un` records as open
("paths are reductions of the same element"); `gsEnergy_quad` states it.

χ is the index character: appending σ multiplies it by q, σ⁻¹ by q⁻¹ (`lenWeighted_act`,
`lenWeighted_actInv`), so on a braid word χ = q^{writhe} (`lenWeighted_eval_signed`).

## 3. Δ (final p ⊗ e⁻ ⊗ ν̄ minus initial n; ν̄ = 1; disjoint strands)

| nucleon model | lepton | Δℓ_lead | Δ log_q χ | Δ log_q N | ΔE_gs (q₀) | ΔE_gs nucleon only |
|---|---|---|---|---|---|---|
| short typed | σ₁³ (H₂) | 1 | 5 | 1.3462 | 1.4757 | −0.20906 |
| short typed | σ₁σ₂σ₁ | 3 | 5 | 1.3462 | 3.1045 | −0.20906 |
| 11-letter typed | σ₁³ | 1 | 5 | 2.7102 | 1.9993 | +0.06389 |
| 11-letter typed | σ₁σ₂σ₁ | 3 | 5 | 2.7102 | 4.3872 | +0.06389 |
| V³ (both) | σ₁³ | 1 | 3 | 3 | 1.2043 | 0 |
| V³ (both) | σ₁σ₂σ₁ | 3 | 3 | 3 | 3.3183 | 0 |

N = Σ|c_w(q₀)| q₀^{ℓ(w)}. Its Δ log_q is not an integer for the typed models, so N is not a
q-degree. The coefficient q-degree span of the nucleon normal forms is [−1,1]/[−2,2] (short p/n),
[−10,10] (both 11-letter), [−5,5] (V³).

**E_gs side finding.** `groebner-shirshov-energy.lean` records `beta_decay_energy_negative`
("daughter lower energy than parent, verified for A ≤ 6"); the Lean statement is vacuous and the
intended content is open (`qou-n2un`). On the nucleon alone the sign depends on the model: the
daughter is lower in the short model (−0.209) and higher in the 11-letter model (+0.064), and
equal on V³. So the claim holds in one of the three corpus nucleon models.

## 4. Required scale per unit (comparison only; not tuned, not wired)

κ = Q / |Δ|, as a ratio to m_e. Q_exp = 0.78233341 MeV, Q_scored = 0.325433929 MeV (#8586).

| Δ used | κ/m_e (Q_exp) | κ/m_e (Q_scored) |
|---|---|---|
| Δℓ_lead = 1 (trefoil) | 1.53099 | 0.63686 |
| Δℓ_lead = 3 (σ₁σ₂σ₁) | 0.51033 | 0.21229 |
| Δ log_q χ = 5 (typed) | 0.30620 | 0.12737 |
| Δ log_q χ = 3 (V³) | 0.51033 | 0.21229 |

No corpus-derived scale per unit q-degree or per unit length exists (grep of `folio/`,
`computations/`, `docs/audits/`, beans; corpus_search on "Bruhat", "crossing budget",
"beta-decay", "Kazhdan-Lusztig"). E₀ = m_e/(q₀(q₀−1)) ≈ 4.186 MeV is a different object (the
scale of `beta-decay-energy-scale` for |Δ(net)|); the κ/E₀ ratios are in the witness.

## 5. Status

Scope (a) for the route "energy = scale × Δ(normal-form invariant)": with the corpus elements, no
invariant gives Q_β without a chosen scale, and the one invariant that separates n from p
(χ-degree) carries the wrong relative sign against the lepton under one linear scale. The
rewrite-order independence of normal-form invariants is proved (H₃); the step-count reading of
`beta-decay-skein-properties` is not a function of the element.

Not established: a lepton element derived from the interaction (the P1/P2 sibling words were not
published when this ran; the branches `claude/beta-gs-reduction-n-gammagamma-2026-11-20` and
`claude/beta-entangled-lepton-pair-2026-11-20` did not exist); the general-n Lean statement.
