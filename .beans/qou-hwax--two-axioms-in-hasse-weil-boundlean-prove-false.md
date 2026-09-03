---
# qou-hwax
title: 'Two axioms in hasse-weil-bound.lean prove False — the qou-rhax defect class, one file over'
status: completed
type: task
priority: high
created_at: 2026-08-29T16:40:00Z
updated_at: 2026-08-29T16:40:00Z
---

Found while reviewing the whole q-Riemann-hypothesis arc for open gaps.
`content/quantum-observable-universe/q-geometric-langlands/hasse-weil-bound.lean`
carried two global axioms, each universally quantified over an arbitrary
`LocalQZetaFunction`, and **each proves `False`**.

## The derivations

```lean
axiom castelnuovo_severi_bound_axiom :
    ∀ (Z : LocalQZetaFunction) (i : Fin 8), ‖Z.eigenvalues i‖ ^ 2 ≤ Z.q

axiom eigenvalue_functional_equation_axiom :
    ∀ (Z : LocalQZetaFunction) (i : Fin 8),
      ∃ (j : Fin 8), Z.eigenvalues j = ↑Z.q / Z.eigenvalues i
```

`LocalQZetaFunction` records the **shape** of a zeta function — a real field
size `q` with `0 < q`, eight nonvanishing complex `eigenvalues`, and a degree-8
`charPoly` equal to `∏ (X - C αᵢ)`. Nothing in it says the data come from a
curve. So:

1. **Castelnuovo–Severi.** Take `q := 1`, `eigenvalues := fun _ => 2`. Every
   field is satisfied — `∏ (X - C 2)` over `Fin 8` is monic of degree 8 — and
   the axiom reads `‖(2:ℂ)‖² ≤ 1`, i.e. `4 ≤ 1`. `False`.
2. **Functional equation.** Take `q := 4`, all eigenvalues `1`. The axiom
   demands some `αⱼ = 4/1 = 4`, but every `αⱼ` is `1`. `False`.

Machine-checked by `lean`-direct (exit 0, 3.9 s). `#print axioms` on each
`False` derivation reports exactly its own axiom plus
`propext`/`Classical.choice`/`Quot.sound` — the same clean signature as the
`qou-rhax` precedent.

## Why it matters beyond the file

`thm:hasse-weil-bound` is the load-bearing local input of the whole q-RH arc.
`stochastic-mechanics/classical-riemann-hypothesis.md` reads: *"The Hasse–Weil
bound guarantees `Re(ρ) = 1/2` for each local geometry individually. The Riemann
hypothesis asserts that this alignment survives the adelic assembly."* The local
half was resting on an inconsistent pair.

**Blast radius contained**, and for the same reason as `qou-rhax`: content-block
`.lean` siblings sit outside the package globs, so no module imports this one.
`grep -rn` over `content/` and `docs/` finds one further mention, a row in
`docs/audits/2026-05-17-derivable-axioms-audit.md`. Unlike `qou-rhax`, however,
this file **does** compile — `lean`-direct exit 0 before the fix — so the
declarations were real, not merely unelaborated.

## The general shape, stated once

`qou-rhax` was `∀ a b, P a ↔ Q b` with `P` not constant in `a`. This one is the
sibling: **an external theorem asserted for every inhabitant of a structure that
does not carry the theorem's hypotheses.** The Weil results hold for the zeta
function of a smooth projective geometrically irreducible curve over `𝔽_q`;
`LocalQZetaFunction` never says its inhabitant is one. Worth scanning for
elsewhere: any `axiom : ∀ (S : SomeStructure), <classical theorem about S>`
where `SomeStructure` is a shape record.

The structure's own history is independent evidence. `eigenvalues_ne_zero` was
added on 2026-08-28 (bean `qou-lsib`) with the docstring *"Without it
`eigenvalue_norm_sq_axiom` … is not merely unproved but FALSE: the all-zeros
datum satisfies every other field."* That is this exact analysis, applied to a
third axiom in the same file, one day earlier — and it was closed by adding the
one missing field rather than by asking whether the two remaining axioms had the
same defect. They did.

---

## RESOLVED 2026-08-29 — this branch

Fixed by the §3b-cond conditional-class pattern (the `qou-rhax` option-2 route):

- The two Weil inputs become fields of `class IsWeilZeta (Z : LocalQZetaFunction) : Prop`,
  carried as an explicit `[IsWeilZeta Z]` binder.
- `eigenvalue_functional_equation`, `castelnuovo_severi_bound`,
  `eigenvalue_norm_sq` and `hasse_weil_bound` take that binder.
  `eigenvalue_norm_sq` — the step that turns `≤` into `=`, and the one piece of
  the argument the corpus proves itself — is unchanged.
- **Non-vacuity witnessed.** `weilZetaExample` (`q = 4`, all `αᵢ = 2`, the
  supersingular shape) carries an `IsWeilZeta` instance, so the class is
  *inhabited* and its fields are jointly consistent — which is exactly what the
  axioms were not. This also clears `proof-no-empty-prop-carrier`.

**Verification** (`lean`-direct, `LEAN_PATH` over the restored
`lake-cache/qou-v4-24-0` oleans):

- `hasse-weil-bound.lean` exit 0, silent.
- `#print axioms` on `hasse_weil_bound`, `eigenvalue_norm_sq` and the instance:
  `[propext, Classical.choice, Quot.sound]` on all three — no `sorryAx`, no
  corpus axiom.
- The conditional theorem **fires**: `example : ‖weilZetaExample.eigenvalues 0‖ = 2`
  proved through `hasse_weil_bound`, so it is not vacuously conditional.
- `spectral-half-line.lean` and `explicit-formula.lean` still exit 0.

The `.md` now states the theorem conditionally and says why the hypotheses are
hypotheses; the `.ts` carries the caveat as an `authorNote`.
