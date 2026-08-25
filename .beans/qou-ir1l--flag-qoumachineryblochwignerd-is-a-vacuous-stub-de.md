---
# qou-ir1l
title: 'FLAG: QOU.Machinery.blochWignerD is a vacuous stub — def := 0 with a rfl ''theorem'' and an unused hypothesis'
status: completed
type: bug
priority: normal
created_at: 2026-08-07T08:45:09Z
updated_at: 2026-08-07T09:56:04Z
---

content/quantum-observable-universe/lean/QOU/Machinery/QDilogarithm.lean:78

    noncomputable def blochWignerD (_q : ℝ) (_n : ℕ) : ℝ := 0
    theorem blochWignerD_real_pos (q : ℝ) (n : ℕ) (_hq : 0 < q) :
        blochWignerD q n = 0 := rfl

This is the banned pattern under AGENTS.md Strict Lean Discipline §5:
the conclusion is a tautology (rfl on a definitional 0) and the
hypothesis 0 < q is never used. It asserts nothing falsifiable.

It is also now actively MISLEADING. The docstring reads it as 'Bloch-Wigner
does not transfer to the substrate (Chain 1 beta NEGATIVE, PR #1768)'. But
this session measured a genuine, sharp, 51-digit Bloch-Wigner value in the
QOU corpus: D(y_+) = Vol(5_2)/3 at the 5_2 saddle shape (bean qou-ma3u).
The negative verdict was about D(q^n) for REAL positive q — where D
vanishes for the trivial reason that D vanishes on the reals. Naming the
symbol blochWignerD and defining it as the constant 0 encodes a
special-case vanishing as if it were the function.

Honest dispositions (§1a): delete it, or rename to make the restriction
explicit (blochWignerD_at_real_powers) and state the real reason
(D vanishes on ℝ), or demote to a documented conjecture carrier.
Do NOT leave a global-looking name bound to 0.
