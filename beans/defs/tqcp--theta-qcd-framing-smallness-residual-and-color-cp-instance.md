---
# tqcp
title: 'GAP: θ_QCD framing route — <10⁻¹⁰ smallness residual + ColorSectorCPEven instance (needs SU(3) 3×3 writhe cancellation)'
status: todo
type: task
priority: normal
tags:
    - sm-26
    - reorg-2026-10-04
    - 8f-colour
created_at: 2026-08-02T00:00:00Z
updated_at: 2026-10-10T07:15:42Z
parent: qou-8lxd
blocked_by:
    - qou-ni4b
---

Framing-phase route to the strong-CP angle θ_QCD
(branch `claude/theta-qcd-framing-phase-2026-08-02`,
`content/quantum-observable-universe/appendix-standard-model/theta-qcd-framing-cp.lean`,
audit `docs/audits/2026-08-02-theta-qcd-framing-phase-cp-route.md`).

PROVED sorry-free: bar-symmetry (CP-even) ∧ pure-phase ⟹ Θ²=1 ⟹ θ∈{0,π}
(`framingPhase_eq_pm_one`); q-power framing phases are automatically pure
phases (`purePhase_qpow`); CP-even(qⁿ) ⟺ q^{2n}=1 (`cpEven_qpow_iff`, at real
q₀>1 ⟹ n=0 ⟹ θ=0).

TWO OPEN PIECES (this bean):

1. **ColorSectorCPEven instance.** Whether the QCD colour-sector TOTAL framing
   phase is CP-even is undischarged (content-bearing class, no instance). A
   single T(2,9) gluon knot has writhe 9≠0 (maximally chiral). An instance
   needs a colour-singlet writhe cancellation over the 9=3×3 tube structure
   (three tubes ↔ anti-tubes, total writhe 0), which requires the OPEN SU(3)
   colour sector. Do NOT supply an axiom/class asserting θ=0 (anti-laundering).

2. **Smallness residual.** Even granting (1), {0,π} (or θ=0 at real q₀) is a
   DISCRETE prediction, not the observed |θ_QCD|<10⁻¹⁰ smallness. Deriving the
   small nonzero residual (or an exact-zero + its correction) is open.

Next honest step: derive the SU(3) colour-singlet projection and check whether
it forces the summed writhe over the three tubes to zero (⟹ instance of the
class ⟹ θ∈{0,π}). Gated on the open SU(3) sector.

## 🔥 Roast (2026-09-03, qou-bsu0)

(i) Needs an instance of `ColorSectorCPEven` — a colour-singlet writhe cancellation over the 9 = 3×3 tubes, since one T(2,9) gluon knot has writhe 9 — after which θ ∈ {0, π} follows (`framingPhase_eq_pm_one`, `ThetaQcdFramingCp.lean`, sorry-free); and, separately, the smallness |θ| < 10⁻¹⁰, which {0, π} does not address.
(ii) Excluded: nothing beyond the discrete ceiling; no route to smallness is even proposed anywhere in the corpus.
(iii) Trap: supplying `instance : ColorSectorCPEven` by fiat (anti-laundering); reading θ = 0 at real q₀ (`cpEven_qpow_iff` forces n = 0) as a solution of strong CP — it is the hypothesis restated; an axion-like field added by hand.
(iv) Next: derive the SU(3) colour-singlet projection and check whether it forces the summed writhe to zero (`qou-ni4b`). Not near-term.
(v) Forecast: one algebraic step done, no foothold on smallness; the hardest open problem in this sector.
Tower status [reading: qou-ggdk]: ORDER-ZERO-ONLY — the framing phase q^{w·c} is a per-crossing datum; the bar involution is fibre-level (Habiro), so CP-evenness is naturally a bar-parity statement about the full colour-sector Markov trace over all partitions — not formulated.
