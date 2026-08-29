---
# qou-qexf
title: 'q-RH: BOTH axioms in explicit-formula.lean prove False — not merely assumed'
status: completed
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

---

## UPGRADED AND RESOLVED 2026-08-29 — I under-called this bean

The bean above says the axiom is "assumed, not derived" and that the *defect is
the caption, not the axiom*. **That was wrong, and wrong in the safe direction.**
Both axioms in the file prove `False`. Machine-checked, `#print axioms` on each
`False` reporting exactly its own axiom plus Lean's three.

### `explicit_formula_axiom` — the `qou-hwax` shape again

It quantified over `ideals` and `spectrum` **independently**. The geometric side
is determined by `ideals`, the spectral side by `spectrum`, and nothing tied
them together — so the identity was asserted for every unrelated pair. With no
ideals, no spectrum and `Ω_q = 1/(2π)` (killing the `ln_q(2πΩ_q)` term), the left
side is `0` and the right side is `2 − ½·ln_q(3/4) > 2`.

Third instance of one shape in this arc: **a claim asserted for every inhabitant
of a domain wider than the claim's subject.** `qou-hwax` was a structure lacking
its theorem's hypotheses; this is a pair of lists that are not the two faces of
one geometry.

### `qLog_tendsto_log_axiom` — false on its own definition

Captioned *"External theorem (L'Hôpital, renormalised q-log limit)"*. But
`qLog q x = log x / log q` and `log q → 0⁺` as `q → 1⁺`, so for `x ≠ 1` it
**diverges**; it does not converge to `log x`. The refutation multiplies by
`log q → 0`: since `qLog q 2 · log q` is identically `log 2`, the claimed limit
forces `log 2 = 0`.

This one needed no exotic instantiation — it contradicts the definition three
lines above it. The word *renormalised* in the caption was pointing at the true
fact (`qLog q x · log q = log x`, no limit), and what genuinely tends to `log x`
is the Tsallis q-logarithm `(x^{1−q} − 1)/(1−q)`, a different function. If the
framework needs the classical `q → 1` degeneration it needs that definition.

## Disposition — the file now has zero live axioms and zero sorries

- `qLog_mul_log` — the true renormalisation identity. **Proved.**
- `not_qLog_tendsto_log` — the limit claim refuted. **Proved**, per Strict Lean
  Discipline §10 (report honest negatives) rather than left as a caveat.
- `QZetaDatum` — bundles the ideals, spectrum and constants of *one* geometry.
  The bundling is the fix: it makes the false universal quantification
  unstatable.
- `QExplicitFormula (D : QZetaDatum)` — §3b conjecture class, **no instance**.
- `explicit_formula` — conditional on that class.
- `not_qExplicitFormula_empty` — the counterexample kept as a **theorem**, so the
  universal form cannot be reinstated without tripping over it.

Citation withdrawn: Rosen Thm 5.12 and Weil are the classical explicit formula
over `𝔽_q`, which is theirs; the q-deformation is the framework's, now
`[manuscript]`. Same disposition `qou-rhax` required.

**Verification.** `lean`-direct exit 0 (one pre-existing unused-variable
warning); `#print axioms` clean on all five declarations; the withdrawn axiom
name resolves to `Unknown constant`, confirming it survives only as prose in the
docstring. `run-validate` exit 0 `✓ Valid`, 13 issues all pre-existing elsewhere.
Render-QA battery clean on the `.md`.

## Left open deliberately — a kind question, not a defect

The block is still kind `theorem` (`thm:explicit-formula`) while its content is
an unproved conjecture and its Lean is a projection of a no-instance class —
degenerate under §3b-cond item 5. Demotion to `conj:explicit-formula` is the
honest disposition. Not done here because it renames a label cited by
`rem:yekutieli-quantum-li` and `rem:unitary-stability` and carried in the
generated definition index; recorded in the block's `authorNotes` and put to the
owner. Both consumers are remarks, so no provable-kind block would become
downstream-of-conjecture — the demotion is contained.
