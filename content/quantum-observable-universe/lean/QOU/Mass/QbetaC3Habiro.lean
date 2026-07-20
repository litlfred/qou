/-
# Q_β precision-ladder `c_k`: the FORMAL-Habiro-element route is growth-excluded

Independent parallel attack (owner directive 2026-07-17) on the `c_3` keystone
(bean `qou-1dnr`), via the **Habiro-element / fibre-level** route flagged in
AGENTS.md ("Q_β Habiro element … the intended permanent fix", parallel to the
α_EM Habiro element `[2]_q·(1−h²α)`), *distinct* from the sibling's q-lift
recursion / DM-cubic / Berezinian route.

## The route and its honest negative

The route seeks a **formal** Habiro-ring element `F(q)` whose Taylor / Ohtsuki
(`q=1`, perturbative) coefficients ARE the ladder `c_k`
(`Q_β = Q_base · ∏_{k≥2}(1 + c_k u^k)`, `u = b·ℏ_q² ≈ 0.008517`).

Two established corpus facts collide:

* **The Q_β generating function is GEOMETRIC.** `g(u) = Σ c_k u^k` has a
  **simple pole at the finite point `u = u_substrate`** (registry constraint
  **KC8** = `prop:q-beta-radius-of-convergence-gate`, PR #1713/#1727): the
  coefficient ratio `c_{k+1}/c_k → 1/u_substrate ≈ 117.409`, i.e. a **finite,
  nonzero radius of convergence**.  Geometric coefficient growth.

* **A formal Habiro element is GEVREY-1.** The `q=1` (Ohtsuki) expansion of a
  Habiro-ring element grows super-geometrically (`|c_k| ~ k!`, Borel radius
  zero) — the resurgent / quantum-modular class (Habiro 2008; Garoufalidis–
  Zagier).  This is the SAME class the *binding* ladder `D(ũ)` lives in
  (registry **KC22**: q-Gevrey, radius → 0) — but the Q_β ladder does **not**.

**Geometric growth (finite radius) and super-geometric / Gevrey-1 growth (zero
radius) are DISJOINT sequence classes.**  Hence the Q_β `c_k` cannot be the
`q=1` coefficients of any formal Habiro-ring element.  This file **proves** that
disjointness (scope-(b) *structural* exclusion, AGENTS.md §"Before declaring
refuted": a proved growth invariant forbids the ingredient), upgrading the
numerical C16 integrality-kill + the empirical KC8 gate to a Lean theorem.

## What survives (and points at the sibling / analytic route)

The correct object for `c_3` is therefore the **analytic simple-pole residue**
(the argument-principle / residue-sum picture of this branch), NOT a formal
Habiro element.  `simplePole_coeff_geometric` below exhibits the surviving
side: the Laurent coefficients of a simple pole are geometric — consistent with
KC8, inconsistent with formal-Habiro.  Its archimedean evaluation is the `c_3`
**near-match** (swings ~2.9% proton↔muon: NOT anchor-invariant ⇒ a fit, not a
derivation — registry `c_3` row).  No new `c_3` is derived here.

## Scope (honest)

`GeometricGrowth` / `SuperGeometricGrowth` and their disjointness
(`geometric_not_superGeometric`) are **proved outright** over `ℝ`.  The two
*corpus inputs* — "the Q_β ladder is geometric (KC8)" and "a formal Habiro
element's expansion is super-geometric (Gevrey-1)" — are carried as §3b-cond
**class hypotheses** (`QbetaLadderGeometric`, `FormalHabiroQOneExpansion`),
each a genuine cited fact, NOT re-derived (the first needs the SDP `c_k`
extraction; the second is literature).  The conclusion
`qbeta_ck_not_formal_habiro` derives `False` from their conjunction — the
rigorous conditional exclusion.

Base ring `ℝ` (§7c): the statements use ordering and the archimedean property
(`pow_unbounded_of_one_lt`), which is the correct home for a growth dichotomy.

-- Ref: [manuscript] docs/audits/2026-07-20-c3-habiro-route.md
-- Ref: [manuscript] docs/coordination/ck-dk-canonical-registry.md (KC8, KC22, c_3 row)
-/
import Mathlib.Algebra.Order.Archimedean.Basic
import Mathlib.Tactic

namespace QOU.Mass.QbetaC3Habiro

/-! ## Two growth classes -/

/-- **Geometric growth.** `c` is bounded by `C · L^k`.  A convergent power
series of finite radius `R = 1/L` has this (root test).  The Q_β ladder
`g(u) = Σ c_k u^k` is geometric with `L = 1/u_substrate ≈ 117.409` — the simple
pole at `u_substrate` (KC8, PR #1713/#1727). -/
def GeometricGrowth (c : ℕ → ℝ) : Prop :=
  ∃ C L : ℝ, 0 ≤ C ∧ 0 ≤ L ∧ ∀ k, |c k| ≤ C * L ^ k

/-- **Super-geometric growth** (the zero-radius / Gevrey class).  `c` eventually
dominates `M^k` for *every* rate `M`.  This is the growth of a formal
Habiro-ring element's `q=1` (Ohtsuki) expansion: Gevrey-1 (`|c_k| ~ k!`, Borel
radius 0; Habiro 2008, Garoufalidis–Zagier). -/
def SuperGeometricGrowth (c : ℕ → ℝ) : Prop :=
  ∀ M : ℝ, ∃ N, ∀ k, N ≤ k → M ^ k ≤ |c k|

/-! ## The disjointness (proved outright) -/

/-- **Growth dichotomy (the structural core).** A geometrically-growing sequence
cannot be super-geometric.  Applying super-geometry at rate `M = L + 1 > L`
forces `(L+1)^k ≤ C·L^k` for all large `k`; dividing gives `((L+1)/L)^k ≤ C`
bounded, contradicting `(L+1)/L > 1` (archimedean `pow_unbounded_of_one_lt`).
The `L = 0` corner degenerates to `1 ≤ 0`. -/
theorem geometric_not_superGeometric (c : ℕ → ℝ)
    (hg : GeometricGrowth c) : ¬ SuperGeometricGrowth c := by
  rintro hs
  obtain ⟨C, L, _hC, hL, hbound⟩ := hg
  obtain ⟨N, hN⟩ := hs (L + 1)
  -- for every k ≥ N :  (L+1)^k ≤ |c k| ≤ C · L^k
  have hkey : ∀ k, N ≤ k → (L + 1) ^ k ≤ C * L ^ k := fun k hk =>
    le_trans (hN k hk) (hbound k)
  rcases eq_or_lt_of_le hL with hL0 | hLpos
  · -- L = 0 : at k = max N 1, (0+1)^k = 1 ≤ C·0^k = 0
    have hk1 : N ≤ max N 1 := le_max_left _ _
    have hkpos : 1 ≤ max N 1 := le_max_right _ _
    have h := hkey (max N 1) hk1
    rw [← hL0] at h
    simp only [zero_pow (by omega : max N 1 ≠ 0), mul_zero] at h
    simp only [zero_add, one_pow] at h
    linarith
  · -- L > 0 : set r = (L+1)/L > 1, get r^k ≤ C for k ≥ N, contradict unbounded
    set r : ℝ := (L + 1) / L with hr
    have hr1 : 1 < r := by rw [hr]; rw [lt_div_iff₀ hLpos]; linarith
    have hrk : ∀ k, N ≤ k → r ^ k ≤ C := by
      intro k hk
      have h := hkey k hk
      have hLk : (0 : ℝ) < L ^ k := pow_pos hLpos k
      rw [hr, div_pow]
      rw [div_le_iff₀ hLk]
      linarith [h]
    -- unbounded : ∃ n, C < r^n
    obtain ⟨n, hn⟩ := pow_unbounded_of_one_lt C hr1
    -- at k = max N n : r^n ≤ r^k ≤ C < r^n
    have hnk : n ≤ max N n := le_max_right _ _
    have hmono : r ^ n ≤ r ^ (max N n) :=
      pow_le_pow_right₀ (le_of_lt hr1) hnk
    have hle : r ^ (max N n) ≤ C := hrk _ (le_max_left _ _)
    linarith

/-! ## Corpus inputs as §3b-cond class hypotheses -/

/-- **Cited input (KC8, PR #1713/#1727).** The Q_β ladder coefficients have
geometric growth (rate `1/u_substrate`, the simple pole / finite radius).  A
class hypothesis, not re-derived here (that needs the SDP `c_k` extraction);
this is the anchor-stable, proved radius/ratio gate
`prop:q-beta-radius-of-convergence-gate`. -/
class QbetaLadderGeometric (c : ℕ → ℝ) : Prop where
  geometric : GeometricGrowth c

/-- **Cited input (literature).** A formal Habiro-ring element's `q=1` (Ohtsuki)
expansion is Gevrey-1, hence super-geometric.  A class hypothesis encoding the
resurgent / quantum-modular growth (Habiro 2008; Garoufalidis–Zagier). -/
class FormalHabiroQOneExpansion (c : ℕ → ℝ) : Prop where
  superGeometric : SuperGeometricGrowth c

/-- **Main exclusion (scope-(b), conditional on the two cited inputs).** The
Q_β ladder `c_k` cannot simultaneously be geometric (KC8) and the `q=1`
coefficients of a formal Habiro-ring element (Gevrey-1): the two growth classes
are disjoint.  Hence there is **no** formal Habiro element whose Ohtsuki
expansion is the Q_β ladder — the intended "Q_β Habiro element" does not exist
as a *formal* object; the surviving object is the analytic simple-pole residue.
-/
theorem qbeta_ck_not_formal_habiro (c : ℕ → ℝ)
    [hg : QbetaLadderGeometric c] [hh : FormalHabiroQOneExpansion c] : False :=
  geometric_not_superGeometric c hg.geometric hh.superGeometric

/-! ## The surviving analytic object: simple-pole (residue) coefficients -/

/-- **Simple-pole coefficients are geometric.** The Laurent coefficients of a
simple pole `A/(u_sub − u) = Σ_k (A · u_sub^{-(k+1)}) u^k` are
`c_k = A / u_sub^{k+1}`, geometric with rate `1/u_sub`.  This is the analytic
(argument-principle / residue-sum) object that survives the exclusion above —
consistent with KC8, and NOT a formal Habiro element.  Its archimedean
evaluation is the `c_3` near-match (no real `q_0`-rational closed form). -/
theorem simplePole_coeff_geometric (A u : ℝ) (hu : 0 < u) :
    GeometricGrowth (fun k => A / u ^ (k + 1)) := by
  refine ⟨|A| / u, 1 / u, by positivity, by positivity, fun k => ?_⟩
  have hupos : (0 : ℝ) < u ^ (k + 1) := pow_pos hu _
  have hval : |A / u ^ (k + 1)| = |A| / u ^ (k + 1) := by
    rw [abs_div, abs_of_pos hupos]
  rw [hval]
  have hrhs : |A| / u * (1 / u) ^ k = |A| / u ^ (k + 1) := by
    rw [div_pow, one_pow, pow_succ]
    field_simp
  rw [hrhs]

end QOU.Mass.QbetaC3Habiro
