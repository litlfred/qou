import Mathlib.Tactic
import QOU.BraidKnot.TwoFiltrationBridge

/-!
# QOU.Resurgence.WardFiltrationCounting — Ward↔filtration counting probe + carriers

Owner's insight (formalize-first scaffold): gauge-invariance order-by-order
(Slavnov–Taylor / Ward) gives LINEAR relations among the Stokes constants, and
these align with the **jet / Gröbner–Shirshov length filtration** better than
bare perturbative order — because the GS length carries the Hecke word-structure.
The test that decides whether this CLOSES a derivation gap (`Δ_λ`, `c_k`):

* **(B.2) Filtration-coincidence carrier** — the OPEN conjecture that the three
  ℕ-filtrations (`d_GB`, jet/iterated-integral `dII`, perturbative order)
  coincide, threaded **conditionally on `[TwoFiltrationBridge]`** (§3b-cond).
  Content-bearing (an equality of ℕ-maps), no instance — genuinely open.

* **(B.3) The counting probe** — a fully **decidable, sorry-free** `Nat`
  computation: at each body/jet order `n`, `#(Ward-free bar-invariant Stokes
  constants) = barOrbits n` vs `#(Δ_λ to fix) = deltaCount n = p(n)`.  The
  verdict `barOrbits n < deltaCount n` is **proved** (`decide`), and the
  deficit is **proved** to equal `chiralPairs n` — the SIGN degrees of freedom
  the bar-invariant trace structurally cannot see.

* **(Sign source, PROBE-4) Stokes-phase sign carrier** — the mixed-sign
  chirality (KL-positivity PROBE-4 prune: KL weights give only the magnitude)
  supplied by the imaginary Stokes phase (`±i` discontinuity ⇒ real sign that
  flips under the bar-involution).  Content-bearing carrier + a **proved**
  cancellation lemma showing the bar-invariant trace cannot see the sign.

**This closes NO derivation gap.**  The counting shows the viewpoint forces the
magnitude relations `|Δ_λ| = |Δ_{λ'}|` (over-determined), and RELOCATES the
residual gap to two categoricity questions (sign / orbit-magnitude), both open.

## References
- [leitner2026] quantum-observable-universe/mass-theory/stokes-descent-ward-filtration
- [seiberg1994] https://doi.org/10.1016/0550-3213(94)90124-4
-/

namespace QOU.Resurgence

open scoped BigOperators
open QOU.BraidKnot

/-! ## (B.3) The Ward-free vs Δ_λ counting probe — decidable, proved -/

/-- Number of partitions of `n` = **#Δ_λ at body/jet order `n`**.  Table for
`n = 0 … 8` (`interval_cases` range for the verdicts). -/
def pPart : ℕ → ℕ
  | 0 => 1 | 1 => 1 | 2 => 2 | 3 => 3 | 4 => 5
  | 5 => 7 | 6 => 11 | 7 => 15 | 8 => 22
  | _ => 0

/-- Number of **self-conjugate** partitions of `n` (= partitions into distinct
odd parts): the fixed points of the bar-involution `λ ↦ λ'`.  Table `n = 0 … 8`. -/
def scPart : ℕ → ℕ
  | 0 => 1 | 1 => 1 | 2 => 0 | 3 => 1 | 4 => 1
  | 5 => 1 | 6 => 1 | 7 => 1 | 8 => 2
  | _ => 0

/-- **#Δ_λ to fix** at order `n` = number of partitions `p(n)`. -/
def deltaCount (n : ℕ) : ℕ := pPart n

/-- **#Ward-free (bar-invariant) Stokes constants** = number of bar-orbits
`(p(n) + sc(n))/2` = (self-conjugate fixed points) + (chiral pairs).  These are
the magnitudes the gauge-invariant Markov trace `tr_M(S)` can supply. -/
def barOrbits (n : ℕ) : ℕ := (pPart n + scPart n) / 2

/-- **#chiral pairs** `{λ, λ'}` with `λ ≠ λ'` = `(p(n) − sc(n))/2` — the SIGN
degrees of freedom that the bar-invariant trace structurally cannot see. -/
def chiralPairs (n : ℕ) : ℕ := (pPart n - scPart n) / 2

/-- **Exact accounting** (proved): `p(n) = barOrbits n + chiralPairs n`.  Every
`Δ_λ` is either a self-conjugate magnitude or half of a chiral pair whose
magnitude is bar-shared and whose sign is the extra DOF. -/
theorem delta_split (n : ℕ) (hn : n ≤ 8) :
    deltaCount n = barOrbits n + chiralPairs n := by
  interval_cases n <;> decide

/-- **Counting verdict (proved).**  For every body/jet order `2 ≤ n ≤ 8`, the
number of Ward-free bar-invariant Stokes constants is strictly LESS than the
number of `Δ_λ` to fix.  The system is **over-determined** on the bar-invariant
side: the trace supplies fewer magnitudes than there are partitions, so the
`Δ_λ` are forced to satisfy relations — the magnitude pairing `|Δ_λ|=|Δ_{λ'}|`. -/
theorem overdetermined (n : ℕ) (h2 : 2 ≤ n) (h8 : n ≤ 8) :
    barOrbits n < deltaCount n := by
  interval_cases n <;> decide

/-- **Deficit = #chiral pairs (proved).**  The exact number of `Δ_λ` DOF NOT
determined by the bar-invariant trace is `chiralPairs n` — the sign/chirality
degrees of freedom (relocated, not closed). -/
theorem deficit_eq_chiralPairs (n : ℕ) (hn : n ≤ 8) :
    deltaCount n - barOrbits n = chiralPairs n := by
  interval_cases n <;> decide

/-- The deficit is **strictly positive** for `2 ≤ n ≤ 8` (proved): there is
always at least one uncaptured sign DOF, so the counting NEVER closes the full
`Δ_λ` by itself. -/
theorem chiralPairs_pos (n : ℕ) (h2 : 2 ≤ n) (h8 : n ≤ 8) :
    0 < chiralPairs n := by
  interval_cases n <;> decide

/-! ## (B.2) Ward↔filtration coincidence carrier — conditional on the bridge (§3b-cond) -/

/-- **Ward↔filtration coincidence** (OPEN conjecture carrier, §3b-cond).
Threads the (conditional) `TwoFiltrationBridge` as an instance hypothesis and
posits that the **perturbative (Ward) order** `pertOrder` coincides with the
bridge's iterated-integral / jet depth `dII` on every partition-cell.
Content-bearing (an equality of ℕ-valued maps — falsifiable), **not** `True`;
**no instance is provided** — the coincidence is genuinely open. -/
class WardFiltrationCoincidence [TwoFiltrationBridge] where
  /-- The perturbative (Ward / Slavnov–Taylor) order of a partition-cell. -/
  pertOrder : YoungDiagram → ℕ
  /-- **The conjecture**: perturbative order = jet / iterated-integral depth. -/
  coincide : ∀ μ : YoungDiagram, pertOrder μ = TwoFiltrationBridge.dII μ

/-- **Conditional consequence (proved sorry-free from the two hypotheses).**
Under the bridge + the coincidence, a self-conjugate cell's *perturbative* order
is exactly `2` (the real Bloch–Wigner depth).  This is **derived** — it composes
the bridge dichotomy (`self-conj ↦ dII = 2`) with `coincide`; it is not assumed.
(Non-degeneracy per §3b-cond item 5: the class carries the hypotheses, the
theorem derives a new conclusion from them.) -/
theorem selfconj_pertOrder_two [TwoFiltrationBridge] [W : WardFiltrationCoincidence]
    (μ : YoungDiagram) (hμ : μ.transpose = μ) :
    W.pertOrder μ = 2 := by
  rw [W.coincide μ]
  exact (TwoFiltrationBridge.bridge μ).1 hμ

/-! ## (Sign source / PROBE-4) The imaginary Stokes phase as the chirality sign -/

section SignSource

/-- **Stokes-phase sign source** (OPEN carrier, over generic `[CommRing R]`).
The mixed-sign chirality of `Δ_λ` (`n=3`: 1+/2−) is exactly what the
KL-positivity PROBE-4 prune shows the (non-negative) KL weights cannot supply —
they give only the MAGNITUDE.  The resurgent route supplies the sign via the
**imaginary Stokes phase**: the `±i` discontinuity across the Stokes line, whose
real shadow is a sign `sign μ` — encoded by `sq_one` (it *squares to `1`*; not
literal `∈ {±1}`, which is strictly stronger over a generic `[CommRing R]`) —
that **flips under the bar-involution** `λ ↦ λ'`.  (PR #4540 proves the concrete
sign is the a-function parity `(-1)^{n(λ)}`, genuinely `±1`.)
This carrier states that structure as content (**not** `True`);
whether the physics FORCES `sign` to be exactly the `±i` phase sign is the open
categoricity question (bean'd, not asserted). -/
class StokesPhaseSign (R : Type*) [CommRing R]
    (conj : YoungDiagram → YoungDiagram) where
  /-- The chirality sign carried by the Stokes phase — a real shadow of the `±i`
  phase. The carrier encodes only that it *squares to `1`* (`sq_one`), not
  literal `∈ {±1}` (which is strictly stronger over a generic `[CommRing R]`).
  PR #4540 identifies the concrete sign as the a-function parity `(-1)^{n(λ)}`,
  which is genuinely `±1`. -/
  sign : YoungDiagram → R
  /-- It is a genuine sign: `sign μ` squares to `1`. -/
  sq_one : ∀ μ, sign μ * sign μ = 1
  /-- **Chirality**: the sign flips under the bar-involution on a chiral pair. -/
  bar_flip : ∀ μ, conj μ ≠ μ → sign (conj μ) = - sign μ

/-- **The bar-invariant trace cannot see the chirality sign (proved).**  On a
chiral pair, `sign μ + sign (conj μ) = 0`: the two signs cancel, so any
bar-symmetric (conjugation-averaged) functional of the sign vanishes on the pair.
This is exactly why `tr_M(S)` supplies the MAGNITUDE (`barOrbits`) but not the
SIGN (`chiralPairs`) — matching the two counts of §B.3, and closing the loop
with the PROBE-4 mixed-sign obstruction. -/
theorem chiral_sign_cancels (R : Type*) [CommRing R]
    (conj : YoungDiagram → YoungDiagram) [S : StokesPhaseSign R conj]
    (μ : YoungDiagram) (h : conj μ ≠ μ) :
    S.sign μ + S.sign (conj μ) = 0 := by
  rw [S.bar_flip μ h]; ring

end SignSource

end QOU.Resurgence
