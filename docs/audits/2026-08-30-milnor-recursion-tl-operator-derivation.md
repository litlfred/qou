# The −h²(h²+2) deficit recursion, derived at the operator level in the spin-½ rep (bean qou-v7ro)

**Date:** 2026-08-30 · **PR:** #6077 ·
**Probe:** [`milnor_recursion_tl_derivation_probe.py`](../../computations/deltalambda/milnor_recursion_tl_derivation_probe.py)
(+ witness) · **Scope:** (a); exact ℚ(q); no float64; no Lean instance created.

## What this establishes

The convention-D Brunnian trace-deficit obeys `D_{A+1}(h) = −h²(h²+2)·D_A(h)`, verified exactly
at A=3,4,5,6 (full rational function). This note **derives the mechanism** of that recursion in
the concrete spin-½ (2-dim `U_q(sl₂)`) rep — the concrete form of convention D — replacing the
opaque "why" with an explicit Temperley–Lieb operator computation.

All four claims verified exactly (sympy over ℚ(q)); A=3 for the operator-level claims (A=4 needs
a 32-dim symbolic matrix inverse, intractable in sympy), and the recursion itself at A=3..6.

## The derivation

**Frame (C0, verified).** Convention D = spin-½: `V = ℚ(q)²`, `R` the Hecke R-matrix
(`R² = (q−1/q)R + 1`), quantum trace `qtr_n(X) = tr(μ^⊗n·X)`, `μ = diag(q,1/q)`. Then
`τ_D(β) = qtr(ρ(β))/[2]^n` and `D_A = 1 − τ_D(w_A) = qtr(Δ_A)/[2]^A`, `Δ_A = 1 − ρ(w_A)`.
Because `V` is 2-dimensional, `ρ` factors through the TL quotient (≥3-row diagrams vanish) — so
this **is** convention D. The probe confirms `1 − τ_D(w_A)` equals the convention-D h-forms
(A=3: `h⁴(h²+3)/(h²+4)`, A=4: `−h⁶(h²+2)(h²+3)/(h²+4)`).

**TL data (C1, verified).** `e_A := q − R_A` satisfies `e_A² = [2]e_A` (`[2] = q+1/q`); the band
generator `σ_A² = q²·1 − h·e_A` and `σ_A^{−2} = q^{−2}·1 + h·e_A`, with `h = q − 1/q`.

**The operator expansion (C2, verified as matrices).** With `w_{A+1} = [w_A, σ_A²]` and
`W = ρ(w_A)⊗1`:

    ρ(w_{A+1}) = 1 + q²h·e_A − h q^{−2}·W e_A W^{−1} − h²·W e_A W^{−1} e_A.

The **sole `w_A`-dependent term** is the last, with coefficient exactly **`−h²`**. This is where
the recursion's `−h²` comes from. (Scalar check, independent of the rep:
`ββ' = (q^{−2}−1)(q²−1) = 2 − (q²+q^{−2}) = −h²`.)

**Assembling the trace (C3/C4, verified).** Taking `qtr` of the expansion, the two abelian terms
are `w_A`-independent constants — `qtr(e_A) = qtr(W e_A W^{−1}) = [2]^A` — and the
deficit-dependence lives entirely in `qtr(W e_A W^{−1} e_A)`. The four terms assemble to
`D_{A+1} = −h²(h²+2)·D_A` exactly (the `h²+2 = q²+q^{−2}` enters through the trace assembly).

## Honest correction and the remaining step

**A clean-reduction guess of mine was wrong, and is retracted.** I initially conjectured that
the `W e_A W^{−1} e_A` term reduces, via a conditional-expectation identity, to a single affine
function of `qtr(W_0)`:
`qtr(W_0·E_A(W_0^{−1})) = [2]^{A+1}(1−u) + [2]u·qtr(W_0)`. **The probe refutes this** — the
relevant ratio is a messy rational function, not that affine form. The recursion is a property
of the **full 4-term assembly**, not a one-line conditional-expectation identity. (Caught before
it reached any durable artifact; the Lean reduction and the PR never asserted it.)

**What is proved vs. open:**

- **Proved (this note):** at A=3, the operator expansion (C2) holds as matrices, and its quantum
  trace reproduces `D_{A+1} = −h²(h²+2)D_A`; the `−h²` is the coefficient of the unique
  `w_A`-dependent operator term. The recursion holds at A=3..6 (full function).
- **Open (∀A):** a general-A proof that the C2 expansion + its trace assembly yield the recursion
  for every A — a Brunnian induction on `w_A = [w_{A−1}, σ_{A−1}²]`, now a concrete TL statement
  rather than the Bar-Natan / Habegger–Masbaum weight-system bridge.

So the structural picture is now: **the `−h²` is derived at the operator level; the `(h²+2)` and
the ∀A closure are the remaining trace-assembly / induction step.** This is a genuine narrowing
of the open problem, not a proof of it.

## Cross-references

- Recursion + closed form (4 exact points): [`2026-08-29-... (milnor_a5_a6_recursion_test)`](../../computations/deltalambda/milnor-a5-a6-recursion-test.witness.json)
- Lean reduction (recursion ⟹ ∀A tight slice): `content/quantum-observable-universe/lean/QOU/MassTheory/BrunnianDeficitRecursion.lean`
- A=4 proved slice: `BorromeanA4TightSlice.lean`
