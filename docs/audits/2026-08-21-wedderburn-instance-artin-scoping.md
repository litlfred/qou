# Can Mathlib's Artin–Wedderburn + `finrank H_n(q) = n!` construct a real `WedderburnDecomp` instance?

**Status: IN PROGRESS — scoping.** Branch `claude/wedderburn-instance-artin-2026-08-21`.

## The question

Bean `qou-luq7`. `QOU.Hecke.WedderburnDecomp`
([`QOU/Hecke/Wedderburn.lean:72`](../../content/quantum-observable-universe/lean/QOU/Hecke/Wedderburn.lean))
carries the Wedderburn diagonalisation of the Markov trace as **class fields with no
instance anywhere in the tree**. So `y_lambda` and `tr_M = Σ_λ y_λ χ^λ` are *assumed*.
`#print axioms` cannot see this (bean `qou-fpjy`).

The claim to verify: Mathlib has Artin–Wedderburn, PR #4857 proved
`finrank H_n(q) = n!`, and the two halves have never been joined.

## The trap (do not rebuild it)

Three distinct objects share the `WedderburnDecomp*` name. Disambiguated below before
any construction; and bean `qou-h56b` records that one of them already has a globally
registered **trivial** instance over `PUnit`. Any construction here must pass the
delete-the-lemma / wrong-value / PUnit tests.

## Findings

_(to be filled)_
