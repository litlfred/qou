import Mathlib.Tactic

/-!
# QOU.AppendixSurreals.DiophantineBirthday — conjectural class (placeholder)

**§3b-cond class axiomatisation** for content block
[`conj:diophantine-birthday`](../../../quantum-observable-universe/appendix-surreals/diophantine-birthday.md): *Algebraic vs transcendental numbers are separated by birthday trajectory*.

This is a **conjecture**: the class `DiophantineBirthday` carries a placeholder
field; the `noncomputable instance` is the conjectural witness whose
`sorry` represents the open conjecture itself (per AGENTS.md §3b),
NOT a missing proof.  Downstream theorems may take
`[DiophantineBirthday]` as an explicit `[Instance]` hypothesis to derive
unconditional Lean theorems modulo this single conjectural input
(per §3b-cond).

The field schema below is a structural placeholder; refine the
fields to match the conjecture's actual content as the
formalisation matures.

## ⚠ RELABELLED 2026-08-10 — a PLACEHOLDER, not an open conjecture

Bean `qou-bday`.  The paragraphs above, and the "no instance is provided — that is the
honest open state" note further down, **claim an epistemic status this file does not
have**, in two independent ways.  Both are established, not suspected.

**1. Withholding the instance encodes nothing.**  The fields are `residual : ℝ` and
`residual_eq_zero : residual = 0`, so `⟨0, rfl⟩` inhabits the class — verified in Lean.
Any downstream result taking `[DiophantineBirthday]` is therefore **unconditional in
disguise**: the hypothesis discharges in one line.  The history note below records that
an `axiom`-asserted global instance was removed as dishonest; removing it did not
achieve what that note claims, because the class was trivially satisfiable either way.
This is the "stipulates the answer" degeneracy catalogued in
`docs/audits/2026-08-09-inhabitation-is-a-weak-discriminator.md` — the useful test is
not *"is the carrier inhabited?"* but *"is the instance non-degenerate?"*.

**2. The separation, as stated, is IMPOSSIBLE.**  See
`QOU/AppendixSurreals/DiophantineBirthdayScope.lean`.  The `SurrealField` axiom
`birthday_ofReal_le_omega` puts every real at birthday `≤ ω`, and in Conway's surreals
every non-dyadic real is born exactly on day `ω` — so `birthday(√2) = ω = birthday(π)`.
`no_birthday_only_separation` proves that **no** predicate on the birthday can then
distinguish them.  A separation by birthday-of-the-number cannot exist.

**Where the conjecture must actually live.**  Its own gloss says "birthday
**trajectory**", and that word is load-bearing: Liouville and Roth are about how fast
rationals approximate `α`, which in surreal terms is the shape of the **sign
expansion** — the path `SignSequence.gonshor` traces — not the ordinal it terminates at.
A faithful statement compares *prefixes* against the Liouville exponent.  That statement
is not written, here or anywhere in the corpus.

**Until it is, treat this file as a placeholder rather than a formalised conjecture, and
do not cite `[DiophantineBirthday]` as conditional support for anything.**  It supports
nothing.
-/

namespace QOU.AppendixSurreals

/-- Algebraic vs transcendental numbers are separated by birthday trajectory

    Conjectural class — see [`conj:diophantine-birthday`](../../../quantum-observable-universe/appendix-surreals/diophantine-birthday.md). -/
class DiophantineBirthday where
  /-- **Content statement** (from manuscript):

      Liouville's theorem and Roth's theorem bound the approximability
of an algebraic irrational by rationals: if $\alpha$ is algebraic of
degree $d$, then $|\alpha - p/q| > c/q^d$ for sufficiently large
$q$ (Liouville), and Roth improves the exponent to $2 + \delta$ for
any $\delta > 0$.  We use $\delta$ rather than $\varepsilon$ here
to avoid collision with the surreal infinitesimal $\varepsilon =
1/\omega$ used elsewhere
  -- Witness: computations/none in this appendix.

      Field schema below is a structural placeholder; refine per §3b
      to match the conjecture's actual content. The single sorry on
      the `noncomputable instance` is the conjecture itself. -/
  residual : ℝ
  /-- The residual vanishes (the conjecture is the assertion that
      this holds). -/
  residual_eq_zero : residual = 0


-- The conjecture itself.  The `sorry` represents the **open
-- conjecture** per §3b — not a missing proof.
-- Ref: [manuscript] quantum-observable-universe/appendix-surreals/diophantine-birthday.ts
-- ⚠ **No instance is provided.** This was recorded as "the honest open state"
-- (AGENTS.md §3b-tax); it is NOT. `⟨0, rfl⟩` inhabits this class, so withholding
-- the instance encodes nothing and every downstream `[DiophantineBirthday]`
-- hypothesis is dischargeable in one line. See the RELABELLED note in the header.
-- History: this file previously carried
--     axiom conj_diophantine_birthday : DiophantineBirthday
--     noncomputable instance : DiophantineBirthday := conj_diophantine_birthday
-- i.e. the conjecture was asserted by `axiom` and installed as a global instance, so
-- every downstream `[DiophantineBirthday]` resolved for free.  Removed, not completed — downstream
-- results must take `[DiophantineBirthday]` as an explicit hypothesis.

end QOU.AppendixSurreals
