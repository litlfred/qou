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

## Honest §3b chips LANDED (move B — extend the conditional cone, no fabricated instance)

Both landed with the real Mathlib lemmas — no artifact shortcuts.

1. **`FollowsRogersSzego` even-sector tower** (`Mass/BindingQHermiteOscillator.lean`,
   `rogers_szego_even_at_neg_one`) — the file already proved the ODD sector vanishes
   at `t=−1` (bar-odd/sinh collapse); added the EVEN closed form
   `H_{2j}(−1;q) = ∏_{i<j}(1−q^{2i+1})·H_0` (bar-even/cosh tower), completing the
   q-Hermite even/odd parity. Direct application of this session's bar-parity insight.
   Verified lean-direct sorry-free (`#print axioms` = propext/Classical/Quot only). ✓

### Second round — the two proven levers applied to sibling files (2026-07-14)

Survey confirmed the bar-parity and growth levers bite in siblings. Landed, all
verified lean-direct sorry-free (axioms = propext/Classical/Quot only):

3. **`QWeberInterpolation.interp_even_at_neg_one`** (bar-parity lever) — the q-Weber
   interpolant transferred odd-vanishing but never the even tower; added it reusing the
   new `rogers_szego_even_at_neg_one`. Completes the q-Weber even/odd parity. ✓
4. **`LevelSelection.no_superlinear_selection`** (growth lever) — generalises
   `no_linear_selection` to eventually-super-linear rules (`A ≤ kA A`, `A ≥ A₀`);
   discharges the "bond-count `A(A−1)/2` a fortiori excluded" claim that was prose-only
   (bond-count qualifies with `A₀ = 3`). ✓
5. **Paper formalization** — `conj:tower-geometric-lower-bound` + `prop:level-selection-
   not-linear` content blocks (lean.ref → the class / `no_linear_selection`), A≥1
   nuance now in corpus. ✓

**Deferred (honest):** `BindingGevreyHalf.involution_not_exponentially_bounded` — a
formal `¬∃ C r, I(n) ≤ C·r^n` capstone. The *content* is already proved (the sandwich
lower bound `factorial_le_four_pow_mul_involution_sq`: `I(n) ≥ √(n!/4ⁿ)` already leaves
every exponential class); the `¬∃` repackaging needs `Real.summable_pow_div_factorial`,
whose heavy analysis import exceeds the sandbox 2-min compile budget. Not an open gap —
a nicety blocked by environment friction.

### Ruled out (already complete / wrong-shape / anti-fit-gated)

`BindingHyperbolicRecurrence`, `BindingQBesselKernel`, `NaStokesKeystone`,
`RogersSzegoInhabited`, `BarParityExclusion`, `KeystoneC8SuperExpBound` — surveyed, not
genuine one-lever chips (already symmetric, no vanishing sector, or need cross-file √(k!)).

### Forward path (not yet done)

`conj:tower-geometric-lower-bound`'s faithful proof needs SYT/skew-tableau/Plancherel
infra — and **main just landed YT seminormal-weight infra** (`χ_λ(σ)=c_λ·h`, several
commits 2026-07-14). Rebasing onto that may unblock the growth conjecture's combinatorial
core. Remaining beans qou-8t34 (cyclotomic, anti-fit-gated), qou-x3nt (pairing / narrow a
class), qou-g020 (2-adic, speculative for binding) are lower-confidence.

---

#### First-round detail

2. **`TowerGeometricLowerBound.no_linear_selection`** (`Mass/LevelSelectionLogarithmic.lean`)
   — converts the file's "linear selection excluded" prose into a `: False` theorem, the
   **honest** way: extensivity required only for `A ≥ 1` (the `A = 0` boundary artifact —
   `w 0 ≥ c > 0` vs `M·0 = 0` — deliberately excluded), and the contradiction genuinely
   uses the Mathlib exponential-beats-linear lemma `isLittleO_coe_const_pow_of_one_lt`
   (`(A:ℝ) =o[atTop] r^A`), not the boundary. Verified lean-direct sorry-free
   (`#print axioms` = propext/Classical/Quot only). ✓ **LANDED** — done with the real
   growth lemma as requested, no artifact shortcut.
