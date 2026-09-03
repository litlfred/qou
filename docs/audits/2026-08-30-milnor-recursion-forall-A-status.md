# The ∀A Milnor deficit recursion: reduced to one identity, not yet proved (bean qou-v7ro)

**Date:** 2026-08-30 · **Bean:** `qou-v7ro` · **Merged:** PR #6077 (`f50bd72b03`) ·
**Probes:** `milnor_recursion_tl_derivation_probe.py`, `milnor_recursion_forall_A_reduction_probe.py` ·
**Scope:** (a); exact ℚ(q); no float64; no conjecture instance fabricated.

## What is established

The convention-D Brunnian trace-deficit `D_A = 1 − τ_A` (spin-½ / Temperley–Lieb Markov
trace; `τ_D(w) = qtr(ρ(w))/[2]^A`) satisfies, verified **exactly at A = 3, 4, 5, 6** on the full
rational function:

    D_{A+1}(h) = −h²(h²+2)·D_A(h),   h = q − 1/q,   u := q²+q⁻² = h²+2.

Lean (merged, sorry-free, axiom-clean): the A=3 and A=4 tight slices are proved
(`borromean_tight_slice`, `borromean4_tight_slice`), and **`tight_slice_of_recursion`** proves
`[BrunnianDeficitRecursion D] ⇒` the exact-order tight slice for **all A ≥ 3** — so proving the
recursion ∀A closes the ∀A nonvanishing of `MilnorExactOrderConjecture`.

## The ∀A reduction (this is the new content)

With `W = ρ(w_A)⊗1`, the operator expansion (verified as matrices) is

    ρ(w_{A+1}) = 1 + q²h·e_A − hq⁻²·We_AW⁻¹ − h²·We_AW⁻¹e_A,   e_A = q − R (TL generator).

Taking `qtr` over `V^⊗(A+1)`, **three of the four terms are A-independent and provable ∀A**:

| term | value | why (∀A) |
|---|---|---|
| `qtr(e_A)` | `[2]^A` | loop closure: e_A caps 2 strands (one loop = [2]) × [2]^{A−1} free strands |
| `qtr(We_AW⁻¹)` | `[2]^A` | `ρ(braid)` commutes with `μ^⊗n` (`[R, μ⊗μ]=0`) ⇒ conjugation drops out of the quantum trace ⇒ `= qtr(e_A)` |
| scalar | `q²h − hq⁻² = h²[2]` | `(q²−q⁻²)h = (q−q⁻¹)(q+q⁻¹)h = h²[2]`, exact |

So the entire recursion collapses to a **single identity** in the one `w_A`-dependent term:

    (★★)   qtr_{A+1}(W e_A W⁻¹ e_A) = [2]^{A+1}(1−u) + u[2]·qtr_A(ρ(w_A)).

`(★★)` is verified exactly at A = 3, 4. **Proving `(★★)` for all A is the single remaining
step** — and it is a concrete TL statement, replacing the opaque Bar-Natan/Habegger–Masbaum
weight-system bridge the bean originally named as the blocker.

## The remaining step, precisely (for the next agent)

`(★★)`'s LHS reduces, by the TL cap-cup identity `e_A X e_A = ⟨∩_A|X|∪_A⟩·e_A` and the Markov
property `qtr_{A+1}(Y e_A) = qtr_A(Y)`, to

    qtr_A( ρ(w_A) · (F⊗1) ),   F = ⟨∩_A| ρ(w_A)⁻¹ |∪_A⟩   (the cap-cup contraction of strand A).

**The cap-cup contraction is the μ⁻¹-weighted partial trace, and it lives at trace level, not
matrix level** (probe `milnor_recursion_capcup_weight_probe.py`, verified A=3,4):

- **Cap-cup weight is μ⁻¹, not μ.** The clean TL sub-lemma is `ptr_{μ⁻¹}(e) = 1` (identity);
  `ptr_μ(e) = diag(q⁻², q²)` is a nontrivial diagonal. Contracting strand A of `ρ(w_A)⁻¹` uses the
  cup `|∪⟩ = q^{-1/2}|01⟩ − q^{1/2}|10⟩`, whose weight is `μ⁻¹ = diag(1/q, q)` — the **inverse** of the
  quantum-trace weight. Using `μ` (last session's error) makes `(★★)` fail.
- **∀A index reduction** (pure linear algebra, holds ∀A):
  `qtr_A(W₀·(F⊗1)) = qtr_{A-1}(P·F)` with `P := ptr_μ(W₀)`, `F := ptr_{μ⁻¹}(W₀⁻¹)`, `W₀ = ρ(w_A)`.
- **Equivalent trace identity** `(†'')` (verified A=3,4):

      qtr_{A-1}(P·F) = [2]^{A+1}(1−u) + u[2]·qtr_{A-1}(P),   P = ptr_μ(ρ(w_A)),  F = ptr_{μ⁻¹}(ρ(w_A)⁻¹).

- **It is a genuine trace identity.** The tempting **matrix** form `P·F = [2]²(1−u)·1 + u[2]·P` is
  **FALSE** at A=3,4 — the equality appears only after `qtr_{A-1}`. So the ∀A proof must be a
  trace / Brunnian argument, **not** linear algebra on `P·F`.
- **No affine collapse.** `P = ptr_μ(ρ(w_A))` is **not** in `span{1, ρ(w_{A-1}), ρ(w_{A-1})⁻¹}` (A=4):
  the one-strand partial closure of a Brunnian braid does not reduce to a scalar × identity. This is
  precisely why `(†'')` is Brunnian-specific yet still open — the Brunnian structure constrains the
  closures without collapsing them.

The recursive handle `E_A(w_A⁻¹) = E_A(b·w_{A-1}·b⁻¹)·w_{A-1}⁻¹` (`b = A_{A-1,A}`, verified A=4)
gives an induction skeleton; the induction must be run against `(†'')` at **trace level** with the
**μ⁻¹** cap-cup, not the diagonal μ-weighted partial trace.

## Two honest corrections made this session (verification caught both)

1. An "operator-level C3" was first stated as a *single conditional-expectation identity*
   `qtr(W₀·E_A(W₀⁻¹)) = …`; the direct matrix check FAILED. The verified statement is the
   **direct** 4th-term qtr `(★★)` above.
2. In the ∀A reduction, `(★★)`'s LHS was again reduced to the **diagonal** partial trace
   `E_A` (`ptr_last` with `μ = diag(q,q⁻¹)`); that also FAILED at A=3,4. The correct contraction
   `F` is the **TL cap-cup** `⟨∩|·|∪⟩` (off-diagonal cup/cap structure), NOT the diagonal
   quantum partial trace. This is the specific trap for the next attempt.

## Status

- Recursion: **verified exact A=3–6**; **reduced ∀A to `(★★)`** (3 of 4 qtr-terms proved ∀A).
- Clean algebra `(★★) ⟹ D_{A+1}=−h²(h²+2)D_A` is rigorous ∀A: with `G_A := qtr(ρ(w_A))`, the
  A-independent terms give `G_A = [2]^A(1+h²) − h²Q_A` and `(★★)` gives `Q_A = [2]^A(1−u)+u[2]G_{A-1}`;
  eliminating `Q_A` yields `1−D_A = 1 + h²u·D_{A-1}`, i.e. `D_A = −h²(h²+2)D_{A-1}`, exactly.
- `(★★)` ⟺ the trace identity `(†'')` `qtr_{A-1}(P·F)=[2]^{A+1}(1−u)+u[2]qtr_{A-1}(P)`,
  `P=ptr_μ(ρ(w_A))`, `F=ptr_{μ⁻¹}(ρ(w_A)⁻¹)`: **verified A=3,4**; **NOT proved ∀A**. The cap-cup weight
  is `μ⁻¹` (clean sub-lemma `ptr_{μ⁻¹}(e)=1`); the identity is **trace-level only** (matrix form FALSE);
  `P` has **no affine collapse**. This is the open crux.
- No `BrunnianDeficitRecursion` instance exists — the honest open state is preserved.
