import QOU.Infra.Polylogarithm

/-!
# Im Li_3(ζ_n) closed form at every root of unity

Compiled formalisation of
`prop:cyclotomic-trilog-imaginary-closed-form`.
Sibling docstub at
`braids-and-knots/cyclotomic-trilog-imaginary-closed-form.lean`.

The closed form `Im Li_3(ζ_n) = (n - 1)(n - 2) π³ / (3 n³)`
is the substantive Theorem A content; identification with the
analytic polylog value lives in
`QOU.Infra.Polylogarithm.TheoremA`.
-/

namespace QOU.BraidKnot.CyclotomicTrilogImaginary

open QOU.Infra.Polylogarithm

/-! ### `closed_form_holds` — REMOVED 2026-08-21

    It read `∀ n, 2 ≤ n → imLi3ZetaPredicted n = imLi3ZetaPredicted n`,
    closed by `rfl` (vacuity ledger, `proof-no-trivial-true` /
    `reflexive-tautology`, verdict genuine).  A name asserting that a
    closed form *holds* is exactly the claim a reflexive equality cannot
    make: a closed-form statement needs the predicted value on one side
    and the closed form on the other.  That makes it worse than a merely
    empty theorem — a reader grepping for whether the `Im Li₃` closed form
    is established would have found a green `theorem` and stopped.

    It was **dropped rather than restated** because both halves of the
    real content already exist upstream, and duplicating either here would
    add nothing:

    - the verified `n = 4` row is
      `QOU.Infra.Polylogarithm.beta3_from_jonquiere :
      imLi3ZetaPredicted 4 = beta3`, proved from the definitions;
    - the **general-`n`** identification with the analytic
      `Im Li₃(exp(2πi/n))` is conditional content, carried by
      `TheoremA.agrees_at`, and remains unproved.

    Nothing referenced this declaration. -/

end QOU.BraidKnot.CyclotomicTrilogImaginary
