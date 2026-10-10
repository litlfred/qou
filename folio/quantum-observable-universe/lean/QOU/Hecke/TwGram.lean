import QOU.Hecke.TwBasisField
import QOU.MathlibExt.RegTraceGram

/-!
# QOU.Hecke.TwGram — the regular-trace Gram matrix of `H_n(q)` in the `T_w` basis

First brick of bean `qou-0y6h` (Geck–Pfeiffer `det(Gram) = ∏ Schur`), and the
immediate consequence of the `T_w` basis landing.

`QOU.MathlibExt.RegTraceGram.isSemisimpleRing_of_regTraceGram_det_ne_zero` has
been waiting for a basis since it was written; its own docstring says so:

> *"This is the exact hook a `T_w`-basis Gram computation plugs into: supply the
> basis `b` (brick `qou-lrz1`) and the determinant value `det = [n]_q!` (brick
> `qou-twwf`), and semisimplicity of `H_n(q)` follows — no further Hecke input."*

`QOU.Hecke.TwBasis.basisTwOfField` is that basis. This file plugs it in.

## What is proved

* `twGram` — the Gram matrix of the regular trace form in the `T_w` basis,
  indexed by `Equiv.Perm (Fin (n+1)) × Equiv.Perm (Fin (n+1))`.
* `twGram_apply` — its `(v, w)` entry is `tr(L_{T_v T_w})`, an observable.
* `isSemisimpleRing_of_twGram_det_ne_zero` — **`det ≠ 0 ⟹ H_n(q) is
  semisimple**, at every `n`.

## What this does NOT do

It does not compute the determinant. That is the remaining content of
`qou-0y6h` — Geck–Pfeiffer 7.2.6, `det(Gram) = ∏_λ (Schur_λ)^{f^λ}` — and it is
the hard half. What changed is only that the statement can now be *made*: before
the basis there was no finite index set to take a determinant over, which is why
the 2026-08-29 gap inventory recorded `det(Gram)` as not even stateable.

Nothing here bears on the P≠NP wall; semisimplicity is a magnitude-axis fact.
-/

namespace QOU.Hecke.TwBasis

open QOU.MathlibExt LinearMap

variable (K : Type*) [Field K] (q : K) (n : ℕ)

/-- **The regular-trace Gram matrix of `H_n(q)` in the `T_w` basis.**
    Rows and columns are indexed by `S_{n+1}`, so it is `(n+1)! × (n+1)!`. -/
noncomputable def twGram :
    Matrix (Equiv.Perm (Fin (n + 1))) (Equiv.Perm (Fin (n + 1))) K :=
  BilinForm.toMatrix (basisTwOfField K q n)
    (regTraceBilin K (QOU.Hecke.IwahoriHecke K q n))

/-- **The Gram entries are observables**: the `(v, w)` entry is the trace of
    left multiplication by `T_v T_w`. -/
@[simp] theorem twGram_apply (v w : Equiv.Perm (Fin (n + 1))) :
    twGram K q n v w
      = regTraceForm K (QOU.Hecke.IwahoriHecke K q n) (Tw K q n v) (Tw K q n w) := by
  rw [twGram, regTraceGram_toMatrix_apply, coe_basisTwOfField]

/-- **`det(Gram) ≠ 0 ⟹ `H_n(q)` is semisimple**, at every rank.

    This is the composition the `RegTraceGram` hook was written for, and it
    could not be stated before `basisTwOfField`: without a basis there is no
    finite index set to take the determinant over. -/
theorem isSemisimpleRing_of_twGram_det_ne_zero
    (h : (twGram K q n).det ≠ 0) :
    IsSemisimpleRing (QOU.Hecke.IwahoriHecke K q n) :=
  isSemisimpleRing_of_regTraceGram_det_ne_zero (basisTwOfField K q n) h

end QOU.Hecke.TwBasis
