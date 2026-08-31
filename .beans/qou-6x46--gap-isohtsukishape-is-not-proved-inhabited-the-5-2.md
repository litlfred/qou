---
# qou-6x46
title: 'GAP: IsOhtsukiShape is not proved inhabited -- the 5_2 chain has no shape witness'
status: todo
type: task
priority: normal
created_at: 2026-08-31T03:46:07Z
updated_at: 2026-08-31T03:46:07Z
---


## What is missing

`QOU/Archimedean/FiveTwoOhtsukiBridge.lean` defines

    def IsOhtsukiShape (y : ℂ) : Prop :=
      y ^ 3 - 3 * y ^ 2 + 2 * y - 1 = 0 ∧ 0 < y.im

and every theorem in the `5₂` volume-conjecture chain takes it as a hypothesis
(directly, or as the `shape` field of `OhtsukiAsymptotic`). **Nothing in the
corpus proves it is inhabited.** Probed 2026-08-31:

    example : ∃ y : ℂ, IsOhtsukiShape y := by exact?
    -- `exact?` could not close the goal

Mathematically it is true — `y³ − 3y² + 2y − 1` has one real root
(`2.3247179572…`) and a conjugate non-real pair, `y₀ = 0.33764102137762698702 +
0.5622795120623012439i`. Formally it is an open hole, and a small one.

## Why it is worth closing even though a bigger gate sits above it

`OhtsukiAsymptotic` has no instance and never will here (it is Ohtsuki's
steepest-descent analysis), so the top-level theorem is conditional either way.
But "conditional on a published theorem" and "conditional on a hypothesis nobody
has shown is satisfiable" are different kinds of conditional, and the corpus's
vacuity audits exist to keep them apart. Closing this turns the second into the
first.

## Suggested attack

Not Cardano. The cheap route is the derivative test: `p′(y) = 3y² − 6y + 2` has
real roots `1 ± 1/√3` (`0.4226497…`, `1.5773502…`), and

    p(1 − 1/√3) = −0.6151…      p(1 + 1/√3) = −1.3848…

are **both negative**, so `p` is strictly monotone across its only sign change
and has exactly one real root. `ℂ` is algebraically closed, so the other two
roots are a non-real conjugate pair, and conjugation gives one with `Im > 0`.
Both bracket values are rational-arithmetic checks after clearing `√3`.

## Related probe, recorded here because it belongs to the same audit

`FiveTwoTriangulation` — the *other* class the bridge is conditional on — **is**
satisfiable at a derived `vol`. This typechecks (probe only; deliberately NOT
committed as an instance, per AGENTS.md §3b-tax on fabricated witnesses):

    example {y : ℂ} (hy : IsOhtsukiShape y) :
        FiveTwoTriangulation ((starRingEnd ℂ) (1 / y))
          (3 * BlochWigner_lob ((starRingEnd ℂ) (1 / y))) where
      shape_im_pos   := (conj_inv_is_five_two_shape hy).2
      shape_root     := (conj_inv_is_five_two_shape hy).1
      vol_eq_three_D := rfl

So the two classes are **not** instance-free for the same reason.
`OhtsukiAsymptotic` carries genuine unproved analysis. `FiveTwoTriangulation`'s
first two fields are already theorems here, and its third *defines* `vol`; its
instance-free status is a deliberate refusal to launder the name `vol`, since
Lean has no definition of hyperbolic volume to tie it to. An instance would make
the conclusion read `Tendsto … (nhds (3·D(y₊)))`, which is true content modulo
(A) but no longer says "the hyperbolic volume of the `5₂` complement".

Worth stating plainly in `BlochWignerLobachevsky.lean` where the class is
declared — the current docstring says `vol_eq_three_D` "is the geometric input,
and it is the whole content", which is right, but a reader can miss that the
class is satisfiable and conclude the gate is stronger than it is.
