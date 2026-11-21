import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Ring.Int.Defs
import Mathlib.Data.Prod.Basic
import Mathlib.Logic.Embedding.Basic
import Mathlib.Tactic.Ring

/-!
# QOU.BraidsAndKnots.YoungDiagramTranspose — the transpose-parity no-go for the Δ_λ kernel sign

The Δ_λ super-exponential growth bound (#3939) reduces (#3959) to the covariance kernel

    T₃ = Σ_{λ⊢k} (f^λ)² χ^λ(3-cycle) ≤ 0
       ⇔ cov(k) := Σ_{λ⊢k} (f^λ)³ (Σ_□ c(□)² − C(k,2)) ≤ 0,   c(i,j) = j − i.

The kernel is **OPEN** (`YoungDiagramKernel.covariance_kernel_conjecture`, an honest §3b `sorry`).
A tempting scope-(b) route is the **conjugation involution** `λ ↔ λ'` (transpose), which the
reduction already exploits to prove the *linear* content moment vanishes (`T₂ = 0`). This file
formalizes the precise statement that this route **cannot sign `T₃`**: the transpose involution kills
the **odd** content moment `T₂` but is a pointwise **symmetry** of the **even** content-square moment,
so it contributes zero information about the sign of `T₃`.

The content parities are realized on a **cell model** of a Young diagram as a `Finset (ℕ × ℕ)` of
cells `(i,j)`, with transpose = coordinate swap `(i,j) ↦ (j,i)`:

  * `csum` (linear content `Σ (j − i)`) is transpose-**odd**  (`csum_transpose`) ⇒ kills `T₂`;
  * `csq`  (content square `Σ (j − i)²`) is transpose-**even** (`csq_transpose`) — squares kill the
    sign ⇒ the whole `cov` summand is transpose-invariant (`kernel_summand_transpose_invariant`).

The coordinate-swap cell model is the representation-free heart of the classical conjugation
bijection; on the weakly-decreasing `List ℕ` encoding of `YoungDiagramKernel` the swap is realized by
`YoungDiagramKernel.conj` (the cell-level bijection there is the standard transpose correspondence).

Together with the FKG-on-dominance no-go (`fl_kernel_sign_structure.py`, NARROWING A) this pins the
kernel sign as an **order-blind, parity-blind** concentration effect: no correlation inequality on
the dominance lattice and no parity/involution argument can produce it — a large-deviation /
tilted-limit-shape bound is required. **This file does not close the kernel.**

Base ring: `ℤ` for the concrete content (contents are integers); the abstract summand-parity lemmas
are generic over `{R : Type*} [CommRing R]`. This is a standalone library file (no `.ts`/`.md`
sibling), imported by no `QOU` module — like `YoungDiagramKernel` / `DeltaLambdaDReduction`, it is
verified per-file by `lean`-direct. It contains **no `sorry`** (grep-confirmed).

> **Verification note (2026-07-19; RESOLVED 2026-07-25).** This file was authored and hand-audited
> but not machine-compiled in its originating session (toolchain egress-blocked). A follow-up
> session has since verified it `lean`-direct (restored `lake-cache` oleans + `LEAN_PATH`):
> **exit 0, sorry-free — the claim is now machine-checked.**

-- Ref: [leitner2026] docs/audits/2026-07-19-deltalambda-kernel-sign-structural-narrowing.md
-/

namespace QOU.BraidsAndKnots.YoungDiagramTranspose

open Finset

/-! ## Abstract summand parity (generic commutative ring)

An involution on the index set fixes each summand of an **even** quantity but flips the sign of each
summand of an **odd** one. This is the abstract reason the transpose route can only close `T₂` (odd
content moment), never `T₃` (even content-square moment). -/

variable {ι : Type*} {R : Type*} [CommRing R]

/-- **Even moment is fixed pointwise.** If the weight `g` and the quantity `a` are both invariant
under `σ` at `i`, the weighted summand `g · a` is fixed by `σ`. So an involution gives **no** sign
information about an even moment — the crux of the transpose no-go for `T₃`. -/
theorem even_summand_involution_invariant (g a : ι → R) (σ : ι → ι) (i : ι)
    (hg : g (σ i) = g i) (ha : a (σ i) = a i) :
    g (σ i) * a (σ i) = g i * a i := by
  rw [hg, ha]

/-- **Odd summands cancel in pairs.** If the weight is invariant (`g (σ i) = g i`) and the quantity
is odd (`a (σ i) = − a i`), the paired summands `g i · a i` and `g (σ i) · a (σ i)` cancel. Summing
this pairing over the transpose involution is exactly why the odd content moment vanishes:
`T₂ = Σ_λ (f^λ)³ Σ_□ c(□) = 0`. -/
theorem odd_summand_involution_cancels (g a : ι → R) (σ : ι → ι) (i : ι)
    (hg : g (σ i) = g i) (ha : a (σ i) = - a i) :
    g i * a i + g (σ i) * a (σ i) = 0 := by
  rw [hg, ha]; ring

/-! ## Concrete cell model: contents under coordinate swap (transpose)

A Young diagram is modeled by its set of cells `D : Finset (ℕ × ℕ)`; the content of a cell `(i,j)`
is `c = j − i ∈ ℤ`. Transpose is the coordinate swap `(i,j) ↦ (j,i)`, realized as a `Finset.map`
along the injective `Prod.swap`. -/

/-- Transpose of a diagram: swap the coordinates of every cell. -/
def transpose (D : Finset (ℕ × ℕ)) : Finset (ℕ × ℕ) :=
  D.map ⟨Prod.swap, Prod.swap_injective⟩

/-- Linear content `Σ_□ (j − i)` of a diagram (in `ℤ`). -/
def csum (D : Finset (ℕ × ℕ)) : ℤ :=
  ∑ p ∈ D, ((p.2 : ℤ) - (p.1 : ℤ))

/-- Content square `Σ_□ (j − i)²` of a diagram (in `ℤ`). -/
def csq (D : Finset (ℕ × ℕ)) : ℤ :=
  ∑ p ∈ D, ((p.2 : ℤ) - (p.1 : ℤ)) ^ 2

/-- **Content square is transpose-EVEN.** `(j − i)² = (i − j)²`, so `Σ_□ c(□)²` is fixed by
transpose. This is the fact that makes the transpose involution a *symmetry* of the `cov` summand —
it cannot sign `T₃`. -/
theorem csq_transpose (D : Finset (ℕ × ℕ)) : csq (transpose D) = csq D := by
  unfold csq transpose
  rw [Finset.sum_map]
  refine Finset.sum_congr rfl (fun p _ => ?_)
  simp only [Function.Embedding.coeFn_mk, Prod.fst_swap, Prod.snd_swap]
  ring

/-- **Linear content is transpose-ODD.** `(j − i) + (i − j) = 0`, so `Σ_□ c(□)` negates under
transpose. This is the mechanism behind `T₂ = 0`. -/
theorem csum_transpose (D : Finset (ℕ × ℕ)) : csum (transpose D) = - csum D := by
  refine eq_neg_of_add_eq_zero_left ?_
  unfold csum transpose
  rw [Finset.sum_map, ← Finset.sum_add_distrib]
  refine Finset.sum_eq_zero (fun p _ => ?_)
  simp only [Function.Embedding.coeFn_mk, Prod.fst_swap, Prod.snd_swap]
  ring

/-- **The `cov(k)` summand is transpose-invariant.** Given a transpose-invariant weight `g` (the SYT
dimension `f^λ = f^{λ'}`, classical) and `csq` transpose-even, the whole summand `g · (csq − C)` is
fixed by transpose. Hence the transpose involution contributes **zero** information about the sign of
`cov(k)` — the route-(b) no-go. -/
theorem kernel_summand_transpose_invariant (D : Finset (ℕ × ℕ)) (g : Finset (ℕ × ℕ) → ℤ) (C : ℤ)
    (hg : g (transpose D) = g D) :
    g (transpose D) * (csq (transpose D) - C) = g D * (csq D - C) := by
  rw [hg, csq_transpose]

end QOU.BraidsAndKnots.YoungDiagramTranspose
