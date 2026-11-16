---
# tqcp
title: 'GAP: θ_QCD framing route — <10⁻¹⁰ smallness residual + ColorSectorCPEven instance (needs SU(3) 3×3 writhe cancellation)'
status: in-progress
type: task
priority: normal
tags:
    - sm-26
    - reorg-2026-10-04
    - 8f-colour
created_at: 2026-08-02T00:00:00Z
updated_at: 2026-11-16T17:48:00Z
parent: qou-8lxd
blocked_by:
    - qou-ni4b
---

Framing-phase route to the strong-CP angle θ_QCD
(branch `claude/theta-qcd-framing-phase-2026-08-02`,
`folio/quantum-observable-universe/appendix-standard-model/theta-qcd-framing-cp.lean`,
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

## Progress update 2026-11-16 (PR #8139, `0435e799b9eb320f989c979717153b33245cefc1`)

Upgraded the strong-CP framing route from `ORDER-ZERO-ONLY` to the full-tower 3-strand Wedderburn Markov trace $\Theta_{\mathrm{tower}}(w; q) = \sum_{\lambda \vdash 3} y_\lambda(q)\chi_\lambda(T_w; q)$ in `folio/quantum-observable-universe/lean/QOU/StandardModel/ThreeStrandColourTowerCP.lean` (wired into `QOU.lean`, `0` `sorry`, `0` custom axioms) and verified at 50 dps in `computations/probes/three_strand_colour_tower_cp_probe.py`:
- `SingletTubeConfig`, `mirrorConfig`, `totalWrithe_mirror_eq_self_iff`, `totalWrithe_eq_zero_of_balanced`, `mirrorConfig_eq_self_of_balanced`: proves that a $3$-tube + $3$-antitube configuration has bar-symmetric total writhe iff $\sum_{a=1}^3 (w_a + \bar{w}_a) = 0$.
- `contentSum3_transpose`, `towerChiralMoment_eq`, `towerChiralMoment_eq_zero_iff`: across $\lambda \in \{(3), (2,1), (1^3)\}$, the Young content sums $(+3, 0, -3)$ satisfy $c_{\lambda'} = -c_\lambda$ and factor the full-tower chiral moment as $3w(y_{(3)} - y_{(1^3)})$, which vanishes for $y_{(3)} \ne y_{(1^3)}$ iff $w = 0$.
- `cpEvenSingletWitness_of_balanced` & `balancedT29Singlet_cpEven` vs `gluonT29_not_cpEven` & `gluonT29_qpow_ne_one`: discharges the division-free CP-even framing witness conditionally on any balanced $3 \times \bar{3}$ singlet tube configuration without supplying a fake unconditional `ColorSectorCPEven` instance by fiat. The $|\theta_{\mathrm{QCD}}| < 10^{-10}$ smallness residual remains open; kept `in-progress`.
