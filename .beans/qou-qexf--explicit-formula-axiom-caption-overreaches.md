---
# qou-qexf
title: 'q-RH: explicit_formula_axiom assumes the whole identity, and its citation does not cover the q-deformation'
status: todo
type: task
priority: high
created_at: 2026-08-29T17:00:00Z
updated_at: 2026-08-29T17:00:00Z
---

`q-geometric-langlands/explicit-formula.lean`. `thm:explicit-formula` is
`explicit_formula_axiom` restated as a theorem — the entire identity assumed,
nothing derived:

```
ψ_q(X) = X − Σ_ρ X^ρ/[ρ]_q − ln_q(2πΩ_q) − ½ ln_q(1 − X^{−2})
```

Under Strict Lean Discipline §7 this is the named pattern: an `axiom` consumed
downstream is not a proof of its statement.

## The specific defect is the caption, not the axiom

Assuming a hard analytic input is a legitimate disposition. What is not is the
caption: *"External theorem (Rosen 2002 Ch 5 Thm 5.12; Weil 1948;
Reshetikhin–Turaev 1991)."* Rosen Thm 5.12 is the explicit formula for the zeta
function of a **curve over 𝔽_q**. The identity above is its **q-deformation** —
`[ρ]_q`, `ln_q`, and the `Ω_q` term are the framework's own constructions and
appear in none of the three cited works. The citation makes an assumed
framework claim read as a settled classical one.

This is `qou-rhax`'s finding in milder form (*"the caption attributes it to a
paper that does not say it … the citation is what makes the axiom look
load-bearing rather than arbitrary"*), and its sibling `qou-hwax` is the same
family. Three in one chapter cluster.

## Disposition

Split it. The classical explicit formula for a curve over 𝔽_q **can** be cited
to Rosen honestly; state that one with its real citation. State the
q-deformation separately, cited to `[manuscript]`, and — since it is the
framework's own claim and is not proved — as a `conjecture` carrier per §3b
rather than an axiom, or as a hypothesis class in the `IsWeilZeta` style if a
downstream result is to be made conditional on it.

`qLog_tendsto_log_axiom` in the same file is a second assumed analytic fact. It
is honestly cited to `[manuscript]` and is a much smaller item, but it is
probably provable from Mathlib (`Real.log` continuity plus L'Hôpital at `q → 1⁺`)
and would be a clean win.

**Corpus-grep run (all six paths):** no derivation of the q-explicit formula
exists. 7 audit hits are mass-theory or the rhax audit; 6 `computations/` hits
are λ-scale / h4-drivers / figure-eight; 3 `library/INDEX.md` hits are
Reidemeister torsion, holonomy R-matrix, Ohtsuki. The item is open.
