import QOU.QBeta.QBesselContiguityRecurrence

/-!
# QOU.Mass.BindingQBesselKernel — Layer 2: the super-exponential q-Bessel kernel

**The genuine global layer of the binding prolongation `a_D^(n)`.** Sibling PR #2795 settled,
via the √-branch of the color spectral curve (`X^(n) ~ (z−z_k)^{1/2−n}`, falling-factorial
coefficient `(1/2)_n`), that `a_D^(n) = lw(n−1)` (#1765) grows **super-exponentially** — and that
its natural fast kernel is the **q-Bessel** class (`jackson-q-bessel-contiguity`). This file wires
that verdict to the existing q-Bessel infrastructure
(`QOU.QBeta.QBesselContiguityRecurrence`) at the level of the *binding period sequence*.

## The two layers are one recurrence with two ratio regimes

Both layers are `first_order_solution` (`c_n = c_0 · ∏_{j<n} r_j`) with different ratio `r`:

| Layer | ratio `r_k` | sequence | regime |
|---|---|---|---|
| **1 (`BindingHyperbolicRecurrence`)** | **constant** `ρ = λ₊ = e^{θ_binding}` | `a_D^(n) = a_D^(0)·ρⁿ` (geometric, C-finite) | depth-2 SL₂, **n ≤ 4 fit** |
| **2 (this file)** | **`q^k`-dependent** `qbesselRatio q a k` | `a_D^(n) = a_D^(0)·∏ qbesselRatio` (q-holonomic) | super-exp, **true global** |

Layer 1 is exactly the **constant-ratio degeneration** (`q → 1`) of Layer 2
(`geometric_of_constant_ratio` in the imported file) — which is precisely *why* the SL₂ trace
`τ` is an effective fit that breaks at `n = 6`: a `q^k`-dependent ratio admits no low-order
constant-coefficient (C-finite) recurrence (#1839).

## `BindingFollowsQBessel` — the §3b conjecture (bean `z2bn`)

The conjectural input is that the **binding generating-function coefficients** `a_D^(n)` satisfy
the Hahn–Exton q-Bessel contiguity `(★)`. This is the fibre q-difference kernel `R(q,x)` that
bean `z2bn` is chasing, in its q-Bessel realization. Granting it (class instance), the closed
form and the second-order q-difference equation `(☆)` follow unconditionally from the imported
theorems. The class axiomatises the *recurrence* (a hypothesis on `a_D`); the closed form is
**derived**, not carried — §3b-cond non-degenerate.

Ground ring: a generic field (the q-Bessel layer is **fibre-level / q-formal**, AGENTS.md
"Im(q) at fibre vs observable" — no archimedean evaluation here), matching the imported file. -/

namespace QOU.Mass.BindingQBesselKernel

open QOU.QBeta

variable {K : Type*} [Field K]

/-- **The binding prolongation follows the q-Bessel contiguity — `conj` (bean `z2bn`).**
The binding generating-function coefficients `aD n = a_D^(n)` satisfy the Hahn–Exton q-Bessel
first-order q-recurrence `(★)`: `aD (k+1)·(1−q^{k+1})(1−a q^k) = −q^k · aD k` (with `a = q^{ν+1}`).
This is the §3b conjecture that the super-exponential binding period (= `lw(n−1)`, #1765) is the
q-holonomic q-Bessel sequence — the fibre q-difference kernel `R(q,x)`. The single conjectural
input; the consequences below are derived. -/
class BindingFollowsQBessel (aD : ℕ → K) (q a : K) : Prop where
  /-- The Hahn–Exton q-Bessel contiguity `(★)` for the binding coefficients. -/
  contiguity : ∀ k, aD (k + 1) * ((1 - q ^ (k + 1)) * (1 - a * q ^ k)) = -q ^ k * aD k

/-- **Layer 2 — q-holonomic closed form (conditional on `BindingFollowsQBessel`).** The binding
period is the q-hypergeometric product `a_D^(n) = a_D^(0) · ∏_{j<n} qbesselRatio q a j` — the
super-exponential sequence, derived from the q-Bessel contiguity via `qbessel_coeff_closed_form`.
The product of `q^k`-dependent ratios is what produces the factorial `(1/2)_n` growth (PR #2795). -/
theorem binding_qbessel_closed_form (aD : ℕ → K) (q a : K)
    [B : BindingFollowsQBessel aD q a]
    (hD : ∀ k, (1 - q ^ (k + 1)) * (1 - a * q ^ k) ≠ 0) (n : ℕ) :
    aD n = aD 0 * ∏ j ∈ Finset.range n, qbesselRatio q a j :=
  qbessel_coeff_closed_form q a aD hD B.contiguity n

/-- **Layer 2 — second-order q-difference equation `(☆)` (conditional).** The same binding
coefficients satisfy the function-level q-Bessel q-difference equation's coefficient form,
`(a q^{2k+1} − q^{k+1} − a q^k + 1)·a_D^(k+1) + q^k·a_D^(k) = 0`, via
`qbessel_second_order_recurrence`. This is the explicit `q`-difference operator annihilating the
binding generating function — the Layer-2 analogue of the depth-2 SL₂ operator. -/
theorem binding_qbessel_second_order (aD : ℕ → K) (q a : K)
    [B : BindingFollowsQBessel aD q a] (k : ℕ) :
    (a * q ^ (2 * k + 1) - q ^ (k + 1) - a * q ^ k + 1) * aD (k + 1) + q ^ k * aD k = 0 :=
  qbessel_second_order_recurrence q a aD B.contiguity k

/-- **Layer 1 as the constant-ratio degeneration of Layer 2.** If instead the binding ratio is a
*constant* `ρ` (the `q → 1` limit, `ρ = λ₊ = e^{θ_binding}` the SL₂ eigenvalue), the period is
geometric `a_D^(n) = a_D^(0)·ρⁿ` — the C-finite depth-2 SL₂ effective fit
(`BindingHyperbolicRecurrence`). This is the honest statement of "the SL₂ τ is the `n ≤ 4`
degeneration": same `first_order_solution`, ratio collapsed to a constant. -/
theorem binding_sl2_constant_ratio_degeneration (aD : ℕ → K) (ρ : K)
    (hrec : ∀ k, aD (k + 1) = ρ * aD k) (n : ℕ) :
    aD n = aD 0 * ρ ^ n :=
  geometric_of_constant_ratio (fun _ => ρ) aD ρ (fun _ => rfl) hrec n

end QOU.Mass.BindingQBesselKernel
