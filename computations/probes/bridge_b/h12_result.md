# H12 result: graded strand model for the folded descent (2026-11-21)

Pre-registration: `h12_preregistration.md`. Script and output: `h12_graded_descent_probe.py`, `.out.txt` (exact sympy).

**All four pre-registered criteria pass.**

| criterion | result |
|---|---|
| 1. tr(P·b^k) = q^{2k} + (−q⁻²)^k, k = 1..6 | pass |
| 2. swapped (mixed) lines are traceless | pass |
| 3. two commuting doubled letters factorise | pass |
| 4. opposite grading (q line odd) fails 1 | pass (it gives {−q², q⁻²}) |

So with the −q⁻¹ (sign) line odd and a Koszul sign on the doubled letter, the mirror-twisted trace reproduces Lusztig's folded bulk letter {q², −q⁻²}. The opposite grading gives the sign-twisted algebra instead, so Lusztig's normalisation fixes the grading.

## What this does not show

- **The test is weak.** In the one-letter and commuting cases everything is diagonal. The model was written knowing the target, so passing 1–3 mostly shows that the sign can be placed consistently, not that it is forced. Criterion 4 is the only part that discriminates.
- **The Koszul sign is a modelling choice.** It is the standard super-vector-space sign, motivated by Soergel grading. It is not derived here from Lusztig's φ_x construction (§16.4).
- **Non-commuting letters and the wall are untested.** The real test is a graded representation of the full six-strand H_6(q) (adjacent doubled letters, which do not commute, plus the middle crossing as wall), with V³, checked against reading B's D(q₀) = 0.94911520554914481986. Jimbo's Ř does not have its eigenlines on basis vectors, so that needs a super R-matrix (U_q(gl(1|1))-type) or a different construction.

## Verdict

Partial hit: a strand-level sign rule exists that turns the ruled "summed" picture into Lusztig's twisted descent for one letter and for commuting letters. No D value adopted; the ruling is unchanged.
