import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic


/-!
# QOU.AlgebraicSubstrate.QVonMangoldtFunction

The q-von Mangoldt function over maximal ideals of the coordinate ring.
LaTeX: `\label{def:q-von-mangoldt-function}`

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

set_option autoImplicit false

namespace QOU.AlgebraicSubstrate

-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
-- See `QOU.Archimedean.GroundRing` for the compiled definition.
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- A maximal ideal of the coordinate ring, carrying a norm (residue field
    cardinality) and a flag marking fundamental defects.

    **Renamed from `MaxIdeal` 2026-09-07.**  `explicit-formula.lean` declares a
    *different* `structure MaxIdeal` — over `ℝ` rather than `R_q` — in **the
    same namespace** `QOU.AlgebraicSubstrate`.  Two structures of one name in
    one namespace is a duplicate declaration; it compiles today only because
    these are content-block siblings rather than library modules, so nothing
    imports both.  The duplication itself is deliberate and documented (that
    file's docstring says "the Laurent `R_q` form lives in the sibling
    `q-von-mangoldt-function`"); sharing the name was not.  The suffix says
    which ground ring this one is over. -/
structure MaxIdealRq where
  /-- The norm N(𝔪) — cardinality of the residue field. -/
  norm : R_q
  -- norm_pos : 0 < norm  -- (archimedean; not meaningful over R_q)
  /-- Whether this ideal corresponds to a fundamental defect.

      **`Bool`, not `Prop`, since 2026-09-07.**  It was a field typed with the
      *universe* `Prop`, so the value carried a proposition and an instance
      chose it.  It is a FLAG, and the commented-out weight below consumes it
      as one (`if m.isFundamental then …`), which needs `Decidable` — free for
      `Bool` and not available for an arbitrary `Prop`.  The `ℝ` sibling in
      `explicit-formula.lean` already declares it `Bool`; this is the two
      agreeing. -/
  isFundamental : Bool

/- The q-von Mangoldt function.

    For a fundamental defect with norm N(𝔪), returns
    (N(𝔪)^ℏ_q - 1) / ℏ_q where ℏ_q = (q-1)/q is the quantum
    Planck constant. Returns 0 for non-fundamental ideals.

    NOTE: The exponentiation N(𝔪)^ℏ_q and positivity constraint
    require evaluation over ℝ. This definition is stated formally
    but deferred to the evaluation layer ι : R_q → ℝ.

    **The note is correct and the gap is real** (checked 2026-09-07): `R_q =
    LaurentPolynomial ℤ` has neither exponentiation by a ring element nor
    division, so neither `N ^ ℏ_q` nor `/ ℏ_q` is expressible here.  Carrying
    both operations as fields would state the shape and assert nothing about
    the arithmetic, which is worse than leaving the gap visible.

    **The working definition exists** — over `ℝ`, as
    `QOU.AlgebraicSubstrate.QVonMangoldtFunction` in the sibling
    `explicit-formula.lean`, together with `QChebyshevFunction`.

    🛑 **So this block's `lean.ref` names a declaration that is commented out
    HERE.**  `q-von-mangoldt-function.ts` carries
    `ref: "qou:QOU.AlgebraicSubstrate.QVonMangoldtFunction"` with
    `validation: "not_checked"`.  Under §0a resolution the sibling `.lean` is
    tried first and does not define it, so the ref reaches the grep fallback
    and lands in `explicit-formula.lean` — a *different ground ring* from the
    one this block is about.  Whether that resolution is intended is a
    judgement for the author; it is recorded rather than changed, because
    picking either answer silently would be the guess. -/
-- noncomputable def QVonMangoldtFunction (hbar_q : R_q) (hbar_pos : 0 < hbar_q)
--     (m : MaxIdealRq) : R_q :=
--   if m.isFundamental then
--     (m.norm ^ hbar_q - 1) / hbar_q
--   else
--     0

end

end QOU.AlgebraicSubstrate
