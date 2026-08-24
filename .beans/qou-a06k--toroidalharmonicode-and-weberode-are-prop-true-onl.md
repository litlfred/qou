---
# qou-a06k
title: ToroidalHarmonicODE and WeberODE are Prop := True — only an in-body comment discloses it
status: completed
type: bug
priority: normal
created_at: 2026-08-24T19:40:57Z
updated_at: 2026-08-24T19:45:55Z
---

`QOU/QBeta/ToroidalHarmonicsBasis.lean:89-105`.

## Not an instance — two `def ... : Prop := True`

```
/-- The exact Toroidal Harmonic ODE parameterised by degree n and order m. -/
def ToroidalHarmonicODE (n m : R) (_F : R -> R) (eta : R) : Prop :=
  let V := n^2 - 1/4 + (m^2 - 1/4) / (Real.sinh eta)^2
  True

/-- The local Parabolic Cylinder (Weber) limit in coordinate u. -/
def WeberODE (A B C : R) (_F : R -> R) (u : R) : Prop :=
  True
```

Both ignore every argument. `ToroidalHarmonicODE` even computes the potential
`V` and then discards it. So they are the same proposition as each other and as
every other tautology, and

```
theorem liouville_green_weber_limit (n m A B C : R) (hA : A = 2) (hC : C = -22) :
    exists T, forall _F eta, ToroidalHarmonicODE n m _F eta <-> WeberODE A B C (_F o T) eta
```

is `True <-> True`, closed by `Iff.rfl` with `T := id`. `hA` and `hC` are unused,
which is the quickest way to see that nothing asymptotic is happening: the
"phenomenological constants map to A=2, B~12.13, C=-22" is decoration on a
statement that holds for every `A`, `B`, `C`.

## The defect being fixed here is disclosure, not the stub

The stub itself is legitimate and already tracked: **`qou-p3pl`** carries
`liouville_green_weber_limit` as a cited sorry, tier P, "blocked on in-repo
scaffolding (not Mathlib) ... do NOT weaken the statement". That bean stays
open and this one does not replace it.

What was wrong is that the *disclosure lived only in the theorem's proof body*:

```
  -- `WeberODE` above is the opaque operator stub pending the Mathlib
  --   ODE-formalism bridge, so this asymptotic limit is stated, not yet
  --   derived in Lean.
```

An in-body comment is invisible to `#print axioms`, to the generated docs, to
hover, and to anyone reading the module header — where the two defs are
advertised as *"`ToroidalHarmonicODE`: The exact ODE in the toroidal coordinate
eta"* and *"`WeberODE`: The local Parabolic Cylinder ODE limit"*. Both docstrings
said "the ... ODE" with no hint that the body is `True`.

## Fixed 2026-08-24 (branch `claude/mt7r-archimedean-eval-2026-08-24`)

Docstrings on `ToroidalHarmonicODE`, `WeberODE` and `liouville_green_weber_limit`
now state that the bodies are `True`, that the equivalence is `Iff.rfl`, that
`hA`/`hC` are unused, and that `qou-p3pl` carries the real obligation. **No code
changed** — the stubs, the theorem statement and the proof are untouched, so
`qou-p3pl` is unaffected and the statement was not weakened.

Gates: `scripts/lean-direct-cone.sh QOU.QBeta.ToroidalHarmonicsBasis` exit 0;
`bun run scripts/run-validate.ts` **Valid — 26 issues, 0 errors** (baseline,
unchanged).

## Left alone deliberately

The unused `let V` binding is a real smell (it is the only trace of the intended
potential) but removing it is a code change to a stub whose replacement is
`qou-p3pl`'s job, and the unused-variable sweep `qou-tb7c` already lists this
file. Left for whoever does either.
