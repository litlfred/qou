import QOU.Interactions.QIntegerMassFormula

open QOU.Interactions

-- Q1. Does the global instance resolve? If it does, every downstream
--     `[QIntegerMassFormula]` binder is silently satisfied by it.
#synth QIntegerMassFormula

-- Q2. Is f_magic globally the zero function? The `fun _ => 0` is what makes
--     `binding_energy_bw … (f_magic Z) (f_magic N)` line up definitionally
--     with `IsAMEValue.fits_bound`'s `… 0 0`.
example : (inferInstance : QIntegerMassFormula).f_magic = fun _ => 0 := rfl
example : (inferInstance : QIntegerMassFormula).tolerance = 1 / 100 := rfl

-- Q3. Does the "conjectural" theorem carry a sorry? The class docstring says
--     "`sorry` in any concrete instance is understood as conjecture" and the
--     instance docstring says "Carries the conjecture as an explicit sorry".
#print axioms fits_AME_conditional
#print axioms QOU.Interactions.canonical

-- Q4. THE TEST. If `fits_AME_conditional` had content, it could not be proved
--     for an ARBITRARY real number in place of the AME binding energy. Here
--     `IsAMEValue` is the only gate -- and its third field `fits_bound` already
--     asserts the 1% bound at f_magic = 0. So the "theorem" should follow from
--     that field alone, with the conclusion never touching the formula.
example (B : ℝ) [inst : IsAMEValue 26 30 B] (q m_e : ℝ) :
    ∃ δ : ℝ, |δ| ≤ (1 : ℝ) / 100 ∧
      B = (1 + δ) * binding_energy_bw q m_e 26 30 0 0 :=
  inst.fits_bound q m_e

-- Q5. Sharper: is `IsAMEValue` inhabited for a value that is NOT an AME entry?
--     If the class is satisfiable at an arbitrary B by supplying `fits_bound`
--     from nothing, then "B_AME is an AME database entry" restricts nothing
--     that the conjecture then leans on -- the bound is assumed, not measured.
--     Left as an explicit `sorry` so the probe reports what it needs.
example : True := trivial
