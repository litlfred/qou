---
# qou-t1kv
title: 'GAP: HeckeGenerators is H_infinity — Schur cascade (PROVED, #5766) blocks stdRep3; dim>1 IsJMWeight witness needs a bounded-index class variant'
status: todo
type: task
priority: normal
created_at: 2026-08-25T10:48:07Z
updated_at: 2026-08-25T16:33:12Z
---

## The defect

`QOU.BraidKnot.Hecke.HeckeGenerators` (HeckeJucysMurphyElements.lean:63) quantifies its
relations over **all** `i : ℕ`:

    hecke : ∀ i, σ i * σ i = algebraMap R A (q - q⁻¹) * σ i + 1
    braid : ∀ i, σ i * σ (i+1) * σ i = σ (i+1) * σ i * σ (i+1)
    far   : ∀ i j, i + 1 < j → σ i * σ j = σ j * σ i

That is the STABLE algebra H_∞(q). H_∞ has no nontrivial finite-dimensional
representations, so **no finite-dimensional rep can be an instance** — and therefore
`IsJMWeight` (HeckeSeminormalWeight.lean) cannot be discharged at `dim V_λ > 1`.

This is why the non-vacuity witness that shipped with #5746 is the ONE-DIMENSIONAL
`scalarGenerators`. That was not a choice of convenience; it is the only shape the class
admits.

## Padding does not work — checked, not assumed

The obvious workaround is to embed H_3 ⊂ H_∞ by padding σ_i for i ≥ 2 with a scalar `s`.
It fails at the boundary. Braid at i = 1 with σ_2 = s:

    LHS = σ_1 · s · σ_1 = s·σ_1²        RHS = s · σ_1 · s = s²·σ_1

so it needs `σ_1² = s·σ_1`. With the Hecke relation `σ_1² = (q−q⁻¹)σ_1 + 1` that becomes
`1 = (s − q + q⁻¹)·σ_1`, i.e. **σ_1 must be a scalar**. False in any rep of dim > 1.
So padding is not merely inelegant; it is inconsistent.

## What is already sitting there unused

`QOU/Archimedean/HeckeH3.lean` has **`stdRep3 : HeckeRep 3 2`** — the (2,1) representation
of H_3(q), dimension 2, with `stdRep3_hecke0`, `stdRep3_hecke1`, `stdRep3_braid` all PROVED
and packaged with `hecke_rel` / `braid_adj` / `braid_far`. It is exactly the multi-dimensional
instance needed, and it cannot be used because of the arity above.

Expected eigenvalues for λ = [2,1] at n = 3 (contents of (0,0),(0,1),(1,0) are 0, 1, −1;
two SYT): `L_0 = 1`; `L_1 = σ_0²` with the two Hecke roots squared, `q²` and `q⁻²`, matching
`q^{2·(+1)}` and `q^{2·(−1)}`. So the check is concrete and falsifiable.

## The fix

A bounded-index variant — relations required only for indices `< n−1`. `jmRaw H k` for
`k < n` touches only `σ_0 … σ_{n−2}`, so every theorem in the chain (`jmRaw_comm`,
`jmProd_eq_delta_pow`, `IsJMWeight`, `fullTwist_smul_eq_theta_sq`) goes through unchanged
on the bounded class. Then `stdRep3` instantiates it directly and the `dim > 1` gap closes
at n = 3 without any seminormal construction.

Estimated small: a class variant plus re-parameterising the existing proofs by the bound.

## Do NOT start a parallel Hecke seminormal form

See bean `sv8b` (priority HIGH) and `QOU/BraidKnot/JucysMurphy.lean` (830 lines, "brick 5
of the Okounkov–Vershik tower"): the corpus already has the CLASSICAL (q = 1) seminormal /
Gelfand–Zetlin construction with Specht modules, SYT adjacent-swap and entry-monotonicity
infrastructure, and three honestly-stubbed `sorry` + `-- Ref:` cores. `sv8b` has a
division of labour agreed on PR #4702. Building a second one from scratch would duplicate
mechanical, settled work — which the AGENTS.md overlap rule permits only for open-outcome
research, not for this.


---

## RETRACTED, same day, by me — "no finite-dim rep can instantiate it" is FALSE

The claim above is wrong and machine-refuted. Two counterexamples, the first of which was
already merged and axiom-checked **in the very file this bean cites**:

1. **`scalarGenerators : HeckeGenerators R R q`** (HeckeSeminormalWeight.lean). `A = R` is a
   finite-dimensional algebra — dimension 1. So a finite-dimensional instance not only can
   exist, one already shipped.
2. **Constant-σ, in ANY ring.** Take any `X` with `X * X = algebraMap (q − q⁻¹) * X + 1` and
   set `σ i = X` for every `i`. Braid degenerates to `X³ = X³` and far to `X² = X²`, both
   `rfl`. Verified: `constGenerators` compiles, `lean`-direct **exit 0**. So
   `Matrix (Fin 2) (Fin 2) R` carries an instance too.

I reasoned "H_∞ has no finite-dim reps" and did not check it against the instance I had
written myself an hour earlier. The estimate that followed from it — "hours, not
Wenzl-scale" — is retracted with it.

## The ACTUAL obstruction, stated correctly

It is not finite-dimensionality. It is that **`stdRep3` specifically does not extend to
H_∞**, and the mechanism is Schur, not dimension:

- `σ_0`, `σ_1` in the (2,1) rep are irreducible on `R²`, so together they generate all of
  `M_2(R)`.
- `far` forces `σ_3` to commute with **both** `σ_0` and `σ_1` (`0+1 < 3`, `1+1 < 3`), so by
  Schur `σ_3` is **scalar**, say `s`.
- `braid` at `i = 2` then gives `s·σ_2² = s²·σ_2`, so `σ_2² = s·σ_2`; with the Hecke
  relation that forces `σ_2` scalar too, say `t`.
- `braid` at `i = 1` then gives `t·σ_1² = t²·σ_1`, forcing **`σ_1` scalar** — contradicting
  2-dimensionality.

So the cascade runs downward from `σ_3` and kills the rep. That IS a real obstruction and it
does block using `stdRep3`. **This argument is reasoning, not machine-checked** — unlike the
refutation above. It should be Lean-proved before anyone relies on it, and it is a good
candidate for the formalize-first rule: prove the exclusion, then stop searching for the
instance.

## Revised estimate — NOT hours

The bounded-index class variant is still the right fix, but the cost was understated. Bounds
must be threaded through every lemma in the chain (~700 lines across eight files), and the
inductions in `run_push` / `delta_pow_run` carry indices up to `b + j + 1`, so the bound
bookkeeping is not mechanical. Call it a day of careful work with real risk of the bounds
failing to line up — not an afternoon.

Whether that is worth it for one `dim = 2` witness at `n = 3` is now a genuine question, and
I do not think the answer is obviously yes. `sv8b` may be the better use of the same effort.


---

## The Schur cascade is now MACHINE-CHECKED (2026-08-25, PR #5766)

The caveat above — *"This argument is reasoning, not machine-checked ... It should be
Lean-proved before anyone relies on it"* — is discharged. New library file
`QOU/BraidKnot/HeckeStableScalarCascade.lean`, 13 declarations, no `sorry`:

    sigma_eq_of_succ_scalar   sigma (i+1) = algebraMap s  ->  sigma i = THAT SAME s
    sigma_eq_of_le_of_scalar  downward propagation to every i <= j
    sigma_scalar_of_schur     Schur on {sigma 0, sigma 1}  ->  sigma 1 is scalar
    stdTwo_no_stable_extension   no HeckeGenerators restricts to the seminormal pair

`far` puts `sigma 3` in the centralizer of `sigma 0` and `sigma 1` (0+1<3, 1+1<3), Schur
makes it scalar, and the braid relation cascades down. **The obstruction is Schur, not
finite-dimensionality** — the retraction above stands and nothing in the proof leans on it.

Non-vacuity is carried, not assumed: the 2x2 Young seminormal pair is PROVED to satisfy
the Hecke and braid relations over any field with q != 0, and restated in the class's own
`algebraMap` vocabulary (`stdTwo_hecke0_algebraMap` / `stdTwo_hecke1_algebraMap`) so the
claim is literally the relation `HeckeGenerators.hecke` demands, not a `smul` lookalike.
Their joint centralizer is proved to be exactly the scalars.

Verified: `lean`-direct exit 0 against a cone built FROM SOURCE (8 QOU modules), and
`#print axioms` on all 13 declarations = [propext, Classical.choice, Quot.sound] — no
`sorryAx`. The container's root Mathlib cache is restored (oleans=6990, traces=0), the
state that yields phantom `sorryAx`, so `lake build` was never run.

### What this settles, and what it does NOT

SETTLED: the bounded-index class variant is not merely the tidier route to a `dim > 1`
witness — it is the ONLY one. This is a scope-(b) structural exclusion with a proved
invariant, so no cheaper instantiation exists to be found and nobody should look for one.

STILL OPEN — this bean stays open for it: the bounded-index refactor itself (~700 lines
across eight files, bounds threaded through `run_push` / `delta_pow_run`). The revised
"about a day, with real risk" estimate above is UNCHANGED; proving the exclusion does not
shrink the refactor, it only removes the possibility of avoiding it.

The cost question above — *"whether that is worth it for one dim=2 witness at n=3"* — is
now a cleaner decision: the alternative of finding some other instantiation is provably
empty, so the choice is the refactor or no `dim > 1` witness at all.
