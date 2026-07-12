# α_EM heat-kernel coupling conjecture — literature check + outside-view referee forecast

**Date:** 2026-07-12 · **Axis:** α_EM (`prop:em-coupling-bring-zero-mode`) · **Tier:** external research
(100-agent deep-research sweep: 5 search angles → 15 sources → 3-vote adversarial verification per claim).
**Scope-(a) throughout; no c_k wired; critical-distance license.**

Stress-tests the coupling conjecture — *"the zero-mode `2/(3π) = dim H¹/Area` enters `1/α_EM`
via the heat-kernel `a₁` (Seeley–DeWitt) / conformal-anomaly coefficient"* — against the
physics literature, and forecasts referee reception of the Bring's-surface α derivation.

## Verified findings (3-0 adversarial votes except where noted)

1. **No precedent exists** for a `1/α` contribution of the form `dim H¹(surface)/Area`
   (Betti number over hyperbolic area). Where mainstream QFT runs the exact apparatus
   (U(1) on compact 2-surfaces), the topological output is the **Chern number** — an
   area-independent integer via Atiyah–Singer — never a Betti/area ratio, and never a
   finite shift to a dimensionless EM coupling.
   [arXiv:hep-th/9608103; PRD 101, 054507]
2. **The heat-kernel/Seeley–DeWitt machinery is genuinely calculable on compact hyperbolic
   surfaces** — but when actually applied it produces a **gravitational (Liouville/Polyakov)**
   effective action with curvature-valued coefficients, not a gauge-coupling shift.
   [arXiv:2308.05802]
3. **Adjacent legitimate constructions exist** (U(1) flux on Γ₀(N) hyperbolic quotients;
   heat-kernel topological terms in black-hole entropy) — but they target flavor structure
   and entropy **log-coefficients**; the topological piece is a *fixed anomaly coefficient*,
   not a tunable additive shift landing on 137.036. [arXiv:2007.11497; 2008.11461]
4. **Wyler 1969 — the canonical precedent — is discredited on two independent grounds**:
   (a) an *arbitrary radius = 1 normalization* (hidden DOF, unforced by the scale-independent
   O(n,2) group) [Robertson, PRL 27, 1545 (1971)]; (b) an outright **math error** in the
   Poisson-kernel coefficient of Cartan's third/fourth domain [Pease, IJTP 1977].
   Community verdict: *"a number in search of a theory"* (Adler) — intriguing numerology,
   never fraud, never a derivation.
5. **Digit-matching carries near-zero evidential weight**: a π-and-137 closed form
   reproduces α to the last digit with no physical content [Dattoli, arXiv:1009.1711].
6. **Dimensional-analysis objection**: in 2D the gauge coupling is *dimensionful*
   (QED₂ photon mass `e/√π`) — there is no dimensionless fine-structure analog *on the
   surface itself*. Whatever maps the 2-surface quantity to the 4D dimensionless α is
   doing all the work; in QOU that is the archimedean functor — i.e. **the conjecture**.

## What was NOT established (important — the door is not closed)

The adversarial verification **refuted (0-3) the sharper negative claims**: that the
Seeley–DeWitt coefficient decomposes into a Gauss–Bonnet coupling shift (so my earlier
`a₁ ∝ ∫R` framing is *unsupported*, not merely unprecedented), that it yields only
log-coefficients, and that 2D θ-independence rules the term out. **No source proves a
`b₁/Area` coupling term cannot be constructed.** The case against is "no precedent +
strong disanalogy + numerology history" — scope-(a), not a theorem. And **no source
examined Bring's surface or `2/(3π)` specifically**.

## Where QOU is genuinely better-positioned than Wyler — and where it is not

| Wyler failure mode | QOU status |
|---|---|
| arbitrary radius = 1 normalization (hidden DOF) | **better**: `2/(3π)` is genus-determined, Lean-proved (`bringZeroMode_genus_determined`); `g = 4` from `prop:force-carrier-bring-uniqueness`; `q₀` calibrated elsewhere, not fitted to α |
| math error in the coefficient | **better**: the value identity is machine-checked |
| the *identification* of the geometric ratio with `1/α` is unforced | **same gap**: why `b₁/Area` enters `1/α` is exactly as unforced as Wyler's coset-volume identification — this is THE referee pivot |

## Referee forecast (unsoftened, per the critical-distance license)

**Default reception: numerology** — the construction would be read as Wyler-class until the
coupling identification is *forced* (derived from a zeta-determinant / index / anomaly
computation on Bring's surface), not chosen. The proved genus-determination of the *value*
and the proton-anchor cross-check (48×) are real differentiators a referee would note —
they answer Wyler's normalization objection — but they do not answer the identification
objection. The +0.313 ppb agreement, by itself, carries near-zero evidential weight
(finding 5). Publishability of the α claim rests entirely on deriving the coupling.

### Owner clarification (2026-07-12): comparison-only posture — issue relocates, not dissolves

The owner's standing epistemic posture is **comparison to observed, no ontological
claims**: the framework reports a parameter-free structural value and compares it to
`1/α`; no mechanism is asserted. This is cleaner than Wyler (who claimed a derivation)
and reframes the outside-view issue honestly:

- **What dissolves:** the burden to prove a coupling mechanism. A `near-match`-tier
  observation claim carries no such burden, and the corpus tier discipline states it
  correctly.
- **What relocates:** the referee question becomes **assembly-selection** — *why this
  combination* of Bring invariants (`q[9]_q[10]_q + b₁/Area + Schwinger`) rather than
  any other — Wyler's radius=1 was also a selection, not an ontology. The defense is
  the **documented attempt ledger** (failed alternatives, PSLQ refutations), which
  converts "picked the winner" into "reported the survivor of a recorded search."
  This is a statistics (look-elsewhere) question, answerable, not metaphysics.
- **The stated cost:** without a mechanism the `O(α²)` coefficient is **permanently
  observational** — it can never be computed, only read off the residual (and the
  entropy rule forbids fitting it). So under this posture **+0.313 ppb (2× σ) is a
  floor, not a waypoint**; closing to 1× σ would require exactly the mechanism the
  posture declines to claim.
- **The payoff:** falsifiability — the match sharpens or breaks with improved σ_α and
  q₀, and the 48× proton-anchor preference was not free to vary.

## Action taken

- Re-scoped the coupling framing in `alpha_em_two_loop_structure_probe.py`: the
  heat-kernel `a₁` identification is a **candidate framing with no literature precedent**
  (and the `a₁`→Gauss–Bonnet decomposition claim was adversarially refuted), not an
  identified mechanism.
- The two open questions the literature could not answer — (i) can a U(1) `a₁` on a
  compact hyperbolic surface produce a finite dimensionless additive coupling shift at
  all, and (ii) what maps the 2-surface quantity to 4D α — are the precise formalize-first
  targets for any future coupling work.

## Sources
Primary: PRL 27, 1545 (Robertson 1971) · IJTP (Pease 1977) · arXiv:hep-th/9608103 ·
PRD 101, 054507 · arXiv:2308.05802 · arXiv:2007.11497 · arXiv:2008.11461 · arXiv:1009.1711.
Full verified-claim ledger: 100-agent workflow `wf_9ed467b3-100` (session artifact).
