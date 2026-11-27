# Covariance kernel: the square-law inverse and the large-tilt obstruction

**Date:** 2026-11-27 · **Branch:** `claude/kernel-square-law-inverse-2026-11-27` · **Beans:** `qou-v8t7`
(attack plan), `qou-x631` (kernel), epic `qou-7igi` · **Scope:** one exact reformulation (proved),
one structural exclusion of a proof class (machine-checked counterexample). Neither proves or
refutes the kernel. No fit, nothing wired, no measured value enters.

Notation as in the [complete synthesis](2026-11-24-covariance-kernel-x631-complete-synthesis-9rbo.md):
`f^λ` the hook-length dimension, `ω₃(λ) = Σ_□ c(□)² − C(n,2)`, `σ` a 3-cycle,
`T(g) := Σ_{λ⊢n} (f^λ)² χ^λ(g)`, kernel `cov(n) = Σ_λ (f^λ)³ ω₃(λ) ≤ 0 ⇔ T(σ) ≤ 0`.

## 1. The kernel is a coefficient of the inverse of the square law

Let `Q := (1/n!) Σ_{x∈S_n} x²` in the centre of `ℚ[S_n]`: the law of `X²` for `X` uniform on `S_n`.

**Proposition.** `Q` acts on the irreducible `V^λ` by the scalar `1/f^λ`. Hence `Q` is invertible,
`Q^{-1} = Σ_λ f^λ e_λ = (1/n!) Σ_g T(g)·g`, and

> `cov(n) ≤ 0  ⇔  [σ] Q^{-1} ≤ 0`:
> the convolution inverse of the square law puts non-positive mass on 3-cycles.

*Proof.* A central element acts on `V^λ` by `(1/f^λ)·χ^λ(z)`. For `z = Q` this is
`(1/f^λ)·(1/n!)Σ_x χ^λ(x²) = ν(λ)/f^λ`, where `ν(λ)` is the Frobenius–Schur indicator, and
`ν(λ) = 1` for every irreducible of `S_n` (all are realised over `ℚ`). Expanding
`e_λ = (f^λ/n!) Σ_g χ^λ(g^{-1}) g` gives the coefficient formula. ∎

The identity coefficient is `[e]Q^{-1} = Σ_λ (f^λ)³/n! > 0`. The transposition coefficient is `0`
(conjugation symmetry), so the 3-cycle class is the first class where the sign is in question.

**Why it is worth having.** The 2026-07-18 frontier note says `T(σ)` "is not a connection-coefficient
count ⇒ no manifestly-nonnegative model". This gives it a model, though a signed one: a
coefficient of the inverse of a probability measure. The same object carries the whole tilt family.
For a central `F` with eigenvalue `F(λ)`, `Cov_Planch(F, ω₃) = |C₃|·[σ]F̂`, so with
`φ(s) := [σ]Q^{-s}`:

- `φ(1) ∝ cov(n)` (the kernel),
- `φ'(0) ∝ A2 = Cov_Planch(ln f, ω₃)` (pincer leg 1, `qou-ogrk`),
- `φ(θ) ∝ Z_{2+θ}·g(θ)`, so the pincer's interpolation `g(θ) = E_{2+θ}[ω₃]` has the sign of `φ`.

Since `e − Q` has spectrum in `[0, 1)`, `Q^{-s} = Σ_{m≥0} C(s+m−1, m)(e − Q)^m` converges, with
non-negative weights for `s > 0`.

**Check (zero shared code).** `wlambda_covariance_kernel_square_law_inverse.py` builds `Q` as a class
function by squaring every `x ∈ S_n`, inverts it in the class algebra by solving the convolution
system over `ℚ`, and compares with the hook-formula side. Exact agreement for `n = 3..7`, e.g.
`n = 7`: `[σ]Q^{-1} = −146/315 = T₃/7!` and `[e]Q^{-1} = 8152/315 = Σf³/7!`.

## 2. The natural sufficient condition is false, and why

The expansion above suggests the sufficient condition

> (AM) `a_m := [σ](e − Q)^m ≤ 0` for every `m ≥ 1`,

which would give `φ(s) ≤ 0` for **every** `s > 0`, hence the kernel and A2 together.
Up to the positive factor `|C₃|^{-1}`, `a_m = (1/n!)Σ_λ (f^λ)² ω₃(λ) (1 − 1/f^λ)^m`.

**(AM) is false at `n = 18`.** As `m → ∞` (and likewise for `f^s`, `s → ∞`) the sum is dominated
by the shapes of maximal dimension, so the limiting sign is the sign of `ω₃` summed over them.
Exact table, `n ≤ 40` (probe check B):

| `n` | max-dim shapes | `Σ ω₃` on them |
|---|---|---|
| 18 | `(7,4,3,2,1,1)` and transpose, `f = 16336320` | **+6** |
| 26 | `(8,6,4,3,2,1,1,1)`, `(8,5,4,3,2,2,1,1)`, `f = 2474843571200` | **+2** |
| 4, 5, 8, 14, 21 | | 0 |
| all other `3 ≤ n ≤ 40` | | < 0 |

The tilted covariance `Cov(ω₃, f^s)` therefore turns positive for large `s`: the first crossing is
`s* ≈ 362.94` at `n = 18` and `s* ≈ 144.13` at `n = 26` (mpmath, 60 digits, exact integer inputs).

**Lean (sorry-free, `decide`).** `HeckeTemperleyLieb/YoungDiagramKernelLargeTilt.lean`:
`omega3_maxdim_eighteen`, `sytDim_le_maxdim_eighteen` (no partition of 18 exceeds `16336320`),
`tiltedSum_eighteen_one_neg`, `tiltedSum_eighteen_363_pos`, and
`not_forall_tiltedSum_nonpos : ¬ ∀ k s, 1 ≤ s → tiltedSum k s ≤ 0`.
Axioms: `propext`, `Classical.choice`, `Quot.sound` only.

**Classification.** This is a (b)-type exclusion of a **proof class**, with the computation as the
invariant: no argument valid for every increasing `ψ(f)`, every power `f^s` with `s ≥ 1`, or every
absolutely monotone function of `1 − 1/f` can prove the kernel, because each of those statements
is false at `n = 18`. It explains route 2 of the synthesis (β-monotonicity of `E_β[C₂]` fails) at
the level of mechanism: the large-β limit reads off `ω₃` at the top shape, and that sign is not
fixed. It says nothing against the kernel at `s = 1`, which holds at `n = 18` with a large margin.

**What a proof must therefore use.** The exponent `s = 1` (or a bounded window of `s`). In the
`(e − Q)^m` expansion, the positive `a_m` occur only for `m` of the order of `f_max`
(`m ≳ 10^{10}` at `n = 18`), where `(1 − 1/f)^m` has already killed every shape except the top few.
A proof via this expansion would have to show the early negative terms dominate that tail, a
quantitative statement rather than a sign pattern.

## 3. Overlap check

Threads "Find the missing half of strong binding" (PR #9721) and "Derive the extensive binding term"
(bean `qou-brng`) work on braid-word merge counts and the reading-3 ceiling. Neither touches the
`S_n` Plancherel kernel, `T₃`, or the `Δ_λ` growth chain, so there is no overlap.

## 4. Provenance

- Probe: [`computations/deltalambda/wlambda_covariance_kernel_square_law_inverse.py`](../../computations/deltalambda/wlambda_covariance_kernel_square_law_inverse.py)
  (exact `Fraction` for checks A and B; mpmath 60 dps for the `s*` brackets only), witness beside it.
- Lean: [`YoungDiagramKernelLargeTilt.lean`](../../folio/quantum-observable-universe/lean/HeckeTemperleyLieb/YoungDiagramKernelLargeTilt.lean),
  `lean`-direct exit 0.
- Corpus grep before writing: no prior use of Frobenius–Schur, the Gelfand model, a convolution
  inverse, or the max-dimension shape's `ω₃` in `docs/audits/*covariance*`, `*delta-lambda*` or the
  beans.
