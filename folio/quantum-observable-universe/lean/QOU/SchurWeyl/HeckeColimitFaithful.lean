/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.SchurWeyl.HeckeInclInjective
import QOU.SchurWeyl.HeckeColimit
import QOU.SchurWeyl.HeckeWedderburnGeneral

/-!
# The Hecke colimit is faithful, and its filtration grows strictly

`HeckeColimit`'s own docstrings say, three times, that `H n` is "the image, not an isomorphic copy
of `Hecke K q qi n` — those coincide exactly when `ofLim n` is injective, which is the open question
of bean `qou-ejde` and is not assumed anywhere here."

That question is settled here. `ofLim n` **is** injective at generic `q`, so the colimit contains
each level of the tower faithfully and the range filtration `H` is strictly increasing.

## The route, and why it is short now

`Mathlib.DirectLimit.mk_injective` says the canonical map into a direct limit is injective as soon
as **every transition map** is. So the whole content is lifting one-step injectivity to all steps:

1. `heckeIncl_injective` (bean `qou-ejde`, one step) — already proved;
2. `heckeInclLE_injective` (this file) — every step, by `Nat.le_induction` over
   `heckeInclLE_succ`, since a composition of injections is an injection;
3. `ofLim_injective` (this file) — `DirectLimit.mk_injective` applied to 2.

🛑 **`Ring.DirectLimit.of_injective` does not exist**, under that name, in the pinned Mathlib
v4.24.0 — bean `qou-ejde`'s original route cites it and that citation is dead. The live lemma is
`DirectLimit.mk_injective`, whose hypothesis is exactly "all transitions injective"; the two
injectivity lemmas that do exist under the old spelling are `lift_injective` and `mk_injective`.

## What this closes, and what it does not

**Closes:** `ofLim` faithfulness, hence `finrank (H n) = (n+1)!` and `H n < H (n+1)` — strict growth
of the *colimit's* filtration, which is the level `HeckeTowerWitness` could not reach and which
`qou-p8yg` asks for.

**Does not close:** `trLim` faithfulness. That is a different statement — whether the *trace* on the
colimit separates points — and nothing here bears on it. `HeckeColimitMarkovTrace`'s "What is NOT
proved here" lists both; only the first is discharged.

Nor does this transfer to `twH` in `MathlibExt/HeckeTowerWitness`, whose separator is a rank-2
collapse. This is the colimit carrier, not that one.

## Scope

`ℝ`, `q ≠ 0`, `NotRootOfUnity q` — generic `q`, inherited from `heckeIncl_injective` (whose step 2
is stated over `ℝ`) and from `finrank_hecke_eq_factorial` (which needs semisimplicity). At a root of
unity every step of this fails, not merely weakens.

-- Ref: [leitner2026] beans qou-ejde, qou-p8yg, qou-0fmb.
-/

namespace QOU.SchurWeyl.HeckeColimit

open QOU.SchurWeyl QOU.SchurWeyl.HeckeInclusion QOU.SchurWeyl.HeckeDirectedSystem

variable {K : Type*} [Field K] [CharZero K] {q : K}

/-- **Every transition map of the tower is injective**, not just the one-step inclusion. Induction
on the upper index; the successor step is a composition of two injections. -/
theorem heckeInclLE_injective (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (i j : ℕ) (hij : i ≤ j) : Function.Injective (heckeInclLE K q q⁻¹ i j hij) := by
  induction j, hij using Nat.le_induction with
  | base =>
      rw [heckeInclLE_self]
      exact fun _ _ h => h
  | succ n hn ih =>
      rw [heckeInclLE_succ K q q⁻¹ i n hn]
      exact (SeminormalRep.heckeIncl_injective hq0 hq2 n).comp ih

/-- **Faithfulness.** The canonical map from level `n` into the colimit is injective, so `H n` is an
isomorphic copy of `Hecke ℝ q q⁻¹ n` rather than merely its image. This is the question
`HeckeColimit` and `HeckeColimitMarkovTrace` both flag as open. -/
theorem ofLim_injective (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) :
    Function.Injective (ofLim K q q⁻¹ n) :=
  DirectLimit.mk_injective (heckeF K q q⁻¹)
    (fun i j hij => heckeInclLE_injective hq0 hq2 i j hij) n

/-- The algebra map into the colimit is injective. -/
theorem ofLimₐ_injective (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) :
    Function.Injective (ofLimₐ K q q⁻¹ n) :=
  ofLim_injective hq0 hq2 n

omit [CharZero K] in
/-- The filtration step, as a submodule, is the range of the linear map into the colimit. -/
theorem toSubmodule_H (n : ℕ) :
    (H K q q⁻¹ n).toSubmodule = LinearMap.range (ofLimₗ K q q⁻¹ n) := rfl

/-- **Each level sits in the colimit with its full dimension** `(n+1)!`. -/
theorem finrank_H (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) :
    Module.finrank K (H K q q⁻¹ n).toSubmodule = (n + 1).factorial := by
  haveI := finiteDimensional_hecke (K := K) q q⁻¹ n
  rw [toSubmodule_H, LinearMap.finrank_range_of_inj
    (f := ofLimₗ K q q⁻¹ n) (ofLim_injective hq0 hq2 n),
    finrank_hecke_eq_factorial q hq0 hq2 n]

/-- **Strict growth of the colimit filtration.** `H n < H (n+1)` for every `n` — the level
`HeckeTowerWitness`'s rank-2 collapse cannot reach, and what bean `qou-p8yg` asks for. -/
theorem H_lt_succ (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) :
    H K q q⁻¹ n < H K q q⁻¹ (n + 1) := by
  refine lt_of_le_of_ne (H_mono K q q⁻¹ (Nat.le_succ n)) fun heq => ?_
  have hf : Module.finrank K (H K q q⁻¹ n).toSubmodule
      = Module.finrank K (H K q q⁻¹ (n + 1)).toSubmodule := by rw [heq]
  rw [finrank_H hq0 hq2 n, finrank_H hq0 hq2 (n + 1)] at hf
  have hlt : (n + 1).factorial < (n + 1 + 1).factorial := by
    have hs := Nat.factorial_succ (n + 1)
    have hp := Nat.factorial_pos (n + 1)
    nlinarith [hs, hp]
  omega

end QOU.SchurWeyl.HeckeColimit
