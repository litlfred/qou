# Coordination — dilog/pentagon algebraic layer → mass & binding

**Goal:** land the pentagon↔dilogarithm algebraic infra (the "QOU axioms → dilog
naturally" spine) and use it to close genuine gaps in the canonical derivation of
mass and binding, without laundering the genuinely-open pieces.

**Owner branch:** `claude/faddeev-phi-b-construction-wp7xau` (PR #3779).

## Scope map (2026-07-13)

| PR | Branch | Relationship | Action |
|----|--------|-------------|--------|
| **#3779** (this) | faddeev-phi-b | dilog/pentagon algebraic layer + Φ_b dialog critique | own |
| #3773 | conj-alg-geom-dilog-equiv | **overlap** — bar-even keystone (`conj:alg-geom-dilog-equiv`) consumes `pentagon_iff_isDilog`; also `conj:binding-qbeta-com` | intent posted ([#3773 comment](https://github.com/litlfred/qou/pull/3773#issuecomment-4962536003)) |
| #3683 | borel-alien-calculus | **dependency** — resurgent monodromy datum (G3); my Moiré critique affirms their program is necessary, not shortcut-able | intent posted ([#3683 comment](https://github.com/litlfred/qou/pull/3683#issuecomment-4962262945)) |
| #3778 | mass-binding-errors | **merged** — binding frontier round 3 (packing exponent pruned as empirical import; carrier-saturation mechanism derived; a5+ lower bound). Integrated by rebase. | rebased in |
| #3769 | canonical-derivation-c_k | adjacent — `w(q)←Φ_b`, c_k registry | watch |

## Landed this branch

- `prop:dilog-pentagon-is-associator` / `pentagon_iff_isDilog` — pentagon ⟺
  q-dilogarithm, **sorry-free + axiom-free** (`#print axioms` = none).
- Expanded `rem:q-dilogarithm-pentagon-associator` (pentagon = associator; two
  faces; analytic×algebraic *pairing*, not product).
- Critical assessment: Moiré/resonance framing rejected; "A_ω falls out
  algebraically" rejected — **G3 stays open** (not laundered).

## Honest boundary for "close mass/binding gaps"

The mass/binding canonical chain is extensively worked; the remaining gaps are
mostly **genuine open math** carried honestly as §3b conjecture classes
(Mathlib-gaps: `deriv Li₂ = −log(1−x)/x` term-by-term for the analytic five-term;
level-selection faithful proof; the packing exponent "empirical import" per merged
#3778) or **anti-fit-gated**. Per the STRICT anti-laundering rule these are NOT to
be closed by axiom/vacuous-proof. Only genuinely-derivable bridges get closed.

## Survey result (2026-07-13) — no honest dilog→binding lever exists

A read-only survey of the pentagon/dilog/Rogers/h⁴ material in `Mass/`,
`MassTheory/`, `Braiding/`, `BraidsAndKnots/`, `BringsSurface/` found **no §3b
conjecture class the new `pentagon_iff_isDilog` (or Rogers/PentagonTwist) infra
can honestly chip at**:

1. **No sorries touch pentagon/dilog** in those four trees — already sorry-free.
2. **`PachnerPentagonBorromean`** (field `4·h4_stateSum_coeff = -3`, the pentagon
   residual → Borromean −3/4 bridge) is **witnessed-negative**, not merely open:
   `borromeanH4BestSpec_misses_target_by_more_than_1pct` proves the best natural
   `(u,v)` specialisation gives h⁴ ≈ +2.49e-7 (positive) vs target −3/4 — ~100%
   miss, wrong sign. Intentionally instance-free per the negative-scope discipline.
   Its consumers already exist sorry-free. Not chippable.
3. **`QRogersAnalyticContinuation`** — q=1 five-term already discharged sorry-free
   (default instance + `rogersLogCorrection_eq_log_sub`, `rogersAlphaBeta_complement`);
   q≠1 analytic `Li₂` five-term is the genuine **Mathlib-`Li₂` gap** (`deriv Li₂ =
   −log(1−x)/x` term-by-term). The scalar `pentagon_iff_isDilog` cannot supply it.
4. **`CyclicDilogPentagon`** (`PentagonRigidity`/`PentagonClosure`) — open field is
   the **operator** pentagon `Φ(𝗉)Φ(𝗊)=Φ(𝗊)Φ(𝗉+𝗊)Φ(𝗉)` + a Liouville step; the file
   states a scalar/commutative pentagon "would be *false*." `FiveTerm` is scalar/
   additive ⇒ applying it here would be **laundering**.

The only real sorries in the vicinity are RSK/Specht combinatorics in `BraidKnot/`
(`burnside : Σ_λ (f^λ)² = n!`, SYT/character-table) — genuine Mathlib gaps, unrelated
to the pentagon insight.

**Honest conclusion:** the session's dilog/pentagon insights are an upstream
*consolidation* (real, sorry-free, axiom-free), not a lever that discharges pending
mass/binding conjecture classes. The remaining §3b classes are open for good reasons
(Mathlib-`Li₂` gap; witnessed-negative Pachner; RSK gap) and must stay honestly open.
Genuine (large) paths to actually chip them: build `Real.dilog` + the analytic
five-term (⇒ discharges `QRogersAnalyticContinuation`); build RSK / `Σ(f^λ)²=n!`
(⇒ discharges the `burnside` sorry + Specht chain). Neither is faked here.
