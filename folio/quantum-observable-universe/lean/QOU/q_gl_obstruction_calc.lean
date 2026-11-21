import QOU.QGeometricLanglands

/-!
# QOU.q_gl_obstruction_calc

Canonical declaration for content block
[`prop:q-gl-obstruction-calc`](../../../quantum-observable-universe/q-geometric-langlands/q-gl-obstruction-calc.md): *Obstruction to $q$-flatness*.

The four-part claim is now **asserted as a theorem** (no longer a bare
`def : Prop`).  Its arithmetic core is composed from the proved results
in `QOU.QGeometricLanglands`:

* part 3 (Kummer divisibility, `κ₀ mod n = 0 ↔ n ∣ χ(A)`) composes the
  proved `kummer_divisibility_criterion` with the geometric bridge
  (`κ₀ mod n = 0 ↔ χ(A) ≡ 0 (mod n)`, the Kummer exact-sequence
  computation), which is now carried as the **explicit conditional-class
  hypothesis** `QOU.QGlObstructionCalcContext.kappa_kummer_bridge`
  (AGENTS.md §3b-cond) rather than an internal `sorry` — the geometric
  input is thereby visible in the theorem's signature and part 3 is a
  genuine conditional derivation;
* part 4 (perpetual obstruction at arbitrarily large Kummer levels)
  is derived from the proved `obstruction_cofinite_persistence`
  together with part 3 — no additional geometric input.

Parts 1 (intrinsic curvature nonzero when `κ₀ ≠ 0`, via HKR) and
2 (q-flatness ↔ vanishing connection-dependent curvature) are genuinely
geometric and are **not** covered by the arithmetic core. They are
**assumed**, as the class fields `intrinsic_curvature_nonzero` and
`q_flatness_equiv`, and the theorem discharges each by returning the
field — `exact ctx.intrinsic_curvature_nonzero` / `exact ctx.q_flatness_equiv`.

Read the two halves differently, because they are not the same kind of
thing. Part 3's `kappa_kummer_bridge` is an *input*: the theorem composes
it with the proved `kummer_divisibility_criterion` to reach a conclusion
neither one states, which is the §3b-cond pattern working as intended.
Parts 1 and 2 have no such composition — each field's type is its
conjunct of the conclusion verbatim, so for those two the theorem asserts
exactly what it assumes. The mathematical content of this declaration is
parts 3 and 4.

**Docstring corrected 2026-08-24.** Until now this paragraph, and the
per-part list below, said parts 1 and 2 "carry honest `sorry`s with the
manuscript citation per AGENTS.md §1". That stopped being true at
`b67ee924e84`, which replaced both `sorry`s with the class fields above
and left the prose describing the previous state. The change is a
legitimate move — a `sorry` and a hypothesis-carrying field are both
honest ways to record an unproved input, and `QGlObstructionCalcContext`
has no instance anywhere, so nothing is silently discharged — but a
reader trusting the docstring would have looked for two `sorry`s that are
not there and missed that two of the four parts are now assumptions.

## Base ring (§7c)

The arithmetic core runs in `ℤ` (`χ(A)`, Kummer levels, divisibility). The two
curvature values `F^{intr}_q` and `R(∇)` are only ever tested against zero
(`≠ 0`, `= 0`) -- they are never ordered, normed or approximated -- so they take
values in a generic commutative ring rather than `ℝ`. The archimedean
realisation is the instantiation `R := ℝ`.
-/

namespace QOU

variable {R : Type*} [CommRing R]

/-- Abstract context for the `q_gl_obstruction_calc` claim — manuscript-themed
    typed fields standing in for the geometric objects of
    `prop:q-gl-obstruction-calc`. -/
class QGlObstructionCalcContext (R : Type*) [CommRing R] where
  /-- The categorical object / monoidal structure. -/
  CategoricalObj : Type
  /-- Euler characteristic `χ(A)`. -/
  chi_A : ℤ
  chi_A_nonzero : chi_A ≠ 0
  /-- Intrinsic q-curvature `F^{intr}_q` of a q-flat connection. -/
  F_intr : R
  /-- Predicate: `∇_q` is q-flat. -/
  q_flat : Prop
  /-- The connection-dependent curvature `R(∇)`. -/
  R_connection : R
  /-- Predicate: `κ_0 mod n` vanishes at Kummer level `n`. -/
  kappa_vanishes : ℕ → Prop
  /-- Predicate: the obstruction class `κ₀ = e(ξ) ∈ H²(𝒮, 𝔾_m)` vanishes. -/
  kappa_zero : Prop
  /-- **Geometric Kummer bridge** (class-axiomatised geometric input, per
      AGENTS.md §3b-cond). At Kummer level `n ≥ 1`, the mod-`n` reduction of
      the obstruction class `κ₀ ∈ H²(𝒮, 𝔾_m)` — the connecting map of the
      Kummer exact sequence `0 → μ_n → 𝔾_m --(·)ⁿ--> 𝔾_m → 0` in sheaf
      cohomology — vanishes iff the Euler characteristic satisfies
      `χ(A) ≡ 0 (mod n)`.  This is the genuinely *geometric* half of part 3:
      it computes `κ₀ mod n` by `χ(A) mod n` (the Yekutieli central-extension
      computation `H²(𝒮, 𝔾_m) ≅ ℤ` with `κ₀ ↔ χ(A)`), a fact not derivable
      from Mathlib.  It is an **input** to the theorem — *not* part 3's
      conclusion (`κ₀ mod n = 0 ↔ n ∣ χ(A)`), which is *derived* by composing
      this bridge with the proved arithmetic
      `QGeometricLanglands.kummer_divisibility_criterion`.  Encoding it as a
      named field (rather than an internal `sorry`) makes the conditional
      dependency explicit in the theorem's signature and auditable from the
      context. -/
  -- Ref: [yekutieli2010] Yekutieli, "Central Extensions of Gerbes," Adv. Math. 225 (2010), arXiv:0801.0083
  kappa_kummer_bridge : ∀ n : ℕ, 1 ≤ n →
    (kappa_vanishes n ↔ chi_A % (n : ℤ) = 0)
  /-- External theorem / missing input: intrinsic curvature is nonzero when κ₀ ≠ 0 -/
  intrinsic_curvature_nonzero : ¬ kappa_zero → F_intr ≠ 0
  /-- External theorem / missing input: q-flatness is equivalent to vanishing connection-dependent curvature -/
  q_flatness_equiv : q_flat ↔ R_connection = 0

/-- **Obstruction to q-flatness** (`prop:q-gl-obstruction-calc`).

Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
$\chi(A) \neq 0$ and obstruction class
$\kappa_0 = e(\xi) \in H^2(\mathcal{S}, \mathbb{G}_m)$.  Then:

1. the intrinsic q-curvature `F^{intr}_q = HKR⁻¹(κ₀)` is nonzero
   whenever `κ₀ ≠ 0` — **assumed**, as `ctx.intrinsic_curvature_nonzero`
   (geometric, manuscript);
2. `∇_q` is q-flat iff its connection-dependent curvature vanishes —
   **assumed**, as `ctx.q_flatness_equiv` (geometric, manuscript);
3. at Kummer level `n ≥ 1`, `κ₀ mod n = 0` iff `n ∣ χ(A)` — **derived**
   by composing the geometric bridge to `χ(A) mod n` (the explicit
   conditional-class hypothesis `kappa_kummer_bridge`) with the **proved**
   arithmetic half `kummer_divisibility_criterion`;
4. for `χ(A) ≠ 0` the obstruction persists at arbitrarily large Kummer
   levels — **proved** from `obstruction_cofinite_persistence` + (3). -/
-- Ref: [leitner2026] quantum-observable-universe/q-geometric-langlands/q-gl-obstruction-calc.ts
theorem q_gl_obstruction_calc (ctx : QGlObstructionCalcContext R) :
    (¬ ctx.kappa_zero → ctx.F_intr ≠ 0) ∧
    (ctx.q_flat ↔ ctx.R_connection = 0) ∧
    (∀ n : ℕ, 1 ≤ n → (ctx.kappa_vanishes n ↔ (n : ℤ) ∣ ctx.chi_A)) ∧
    (∀ N : ℕ, ∃ n : ℕ, N < n ∧ ¬ ((n : ℤ) ∣ ctx.chi_A) ∧
                       ¬ ctx.kappa_vanishes n) := by
  -- Geometric bridge (Kummer exact sequence, Yekutieli): the mod-n
  -- vanishing of κ₀ is computed by the Euler characteristic mod n.
  -- Class-axiomatised geometric input (AGENTS.md §3b-cond) — no longer an
  -- internal `sorry`; the theorem is conditional on `ctx.kappa_kummer_bridge`.
  have h_bridge : ∀ n : ℕ, 1 ≤ n →
      (ctx.kappa_vanishes n ↔ ctx.chi_A % (n : ℤ) = 0) :=
    ctx.kappa_kummer_bridge
  -- Part 3: geometric bridge ∘ PROVED kummer_divisibility_criterion.
  have h_crit : ∀ n : ℕ, 1 ≤ n →
      (ctx.kappa_vanishes n ↔ (n : ℤ) ∣ ctx.chi_A) := fun n hn =>
    (h_bridge n hn).trans
      (QGeometricLanglands.kummer_divisibility_criterion ctx.chi_A n hn).symm
  refine ⟨?_, ?_, h_crit, ?_⟩
  · -- Part 1: F^{intr}_q = HKR⁻¹(κ₀) ≠ 0 when κ₀ ≠ 0.  Geometric
    -- (Hochschild–Kostant–Rosenberg comparison); not covered by the
    -- arithmetic core.
    -- Ref: [leitner2026] prop:q-gl-obstruction-calc
    exact ctx.intrinsic_curvature_nonzero
  · -- Part 2: q-flatness ↔ vanishing connection-dependent curvature.
    -- Geometric (def:q-flat-connection); not covered by the
    -- arithmetic core.
    -- Ref: [leitner2026] prop:q-gl-obstruction-calc
    exact ctx.q_flatness_equiv
  · -- Part 4: PROVED from obstruction_cofinite_persistence + part 3.
    intro N
    obtain ⟨n, hn_mem, hNn⟩ :=
      (QGeometricLanglands.obstruction_cofinite_persistence ctx.chi_A
        ctx.chi_A_nonzero).exists_gt N
    exact ⟨n, hNn, hn_mem.2, fun hk => hn_mem.2 ((h_crit n hn_mem.1).mp hk)⟩

end QOU
