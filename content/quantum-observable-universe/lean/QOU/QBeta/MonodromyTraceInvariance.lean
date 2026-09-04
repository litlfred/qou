/-
# Why branch 3's monodromy reading closes: conjugation preserves the trace

Bean `qou-pdix`. Computed in
`computations/qbeta/qbeta_kd_monodromy_reading_closed_probe.py` (4/4).

That bean's entry 5 defines its one contentful branch as

> `M` = exponential/holonomy of an independently-defined connection **whose
> monodromy reproduces the Hecke braiding**

and says it escapes the rationality exclusion *"because a holonomy is
transcendental"*. For the **monodromy** reading that escape does not work, and
the reason is the theorem below.

Kohno–Drinfeld gives, for any such connection, holonomy matrices **gauge-
conjugate** to the Hecke braid-image matrices. `trace_conj_of_mul_eq_one` says
conjugation preserves the trace — and the carrier condition
(`TransferMatrixSpectrum`: `M.trace = 2 cos (eigenphase q)`) is a condition **on
the trace**. So such a monodromy's trace is exactly some `tr ρ(w)`.

The probe measures what those are, in the `(2,1)` block and exactly in `q`:

* every generator has `det ρ(σ) = −1`, so an **even-length** word has `det = +1`
  exactly — the carrier's *second* field is automatic and free, and was never the
  obstruction (`det_even_word`);
* every word trace lies in `ℤ[q,q⁻¹]` — the seminormal radical
  `√(q⁴+q²+1)` cancels identically, as characters must;
* `(σ₀σ₁)³ = I` exactly for every `q`, so the representation factors through
  `B₃/⟨Δ²⟩ ≅ PSL(2,ℤ)` and the achievable traces are indexed by conjugacy
  classes there — a countable set of Laurent polynomials.

Since `2 cos((z−1)h/2)` is transcendental over `ℚ(q,z)` (that bean's entry 4),
the trace field is impossible. **Branch 3 as worded is closed**, with no Drinfeld
associator and no `ζ(3)` computation — superseding the `ζ(3)` milestone proposed
earlier the same day, which targeted exactly this reading.

## What survives

The **open-path / non-abelian Stokes** reading. An open-path holonomy is not a
monodromy — not a closed loop, not a braid-group image — so it is not
trace-pinned, and it is gauge-**dependent**: it transforms by the endpoint frames
rather than by conjugation, which is precisely the hypothesis
`trace_conj_of_mul_eq_one` needs and does not get. Entry 5 cites "Yekutieli
non-abelian Stokes", so that is the corpus's intended shape; its own wording
just does not capture it.
-/
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum

namespace QOU.QBeta

open Matrix

/-- **Conjugation preserves the trace.** Stated with a one-sided inverse so it
needs no `Invertible` instance: `Q * P = 1` is all the gauge equivalence
supplies, and all the argument uses.

This is the whole of why branch 3's monodromy reading closes. A connection whose
monodromy reproduces the Hecke braiding has holonomies of the form `P * ρ(w) * Q`
with `Q * P = 1`; their traces are therefore *exactly* `tr ρ(w)`, which the probe
measures to be Laurent polynomials in `q`. The carrier needs a transcendental
trace, so no such monodromy is a carrier. -/
theorem trace_conj_of_mul_eq_one {n : Type*} [Fintype n] [DecidableEq n]
    {R : Type*} [CommRing R] (P Q M : Matrix n n R) (h : Q * P = 1) :
    Matrix.trace (P * M * Q) = Matrix.trace M := by
  rw [Matrix.trace_mul_comm, ← mul_assoc, h, one_mul]

/-- Every generator of the braid image has `det = −1` in the `(2,1)` block
(measured in the probe), so an **even-length** word has `det = +1` exactly. The
carrier's `M.det = 1` field is automatic on the braid image — it was never the
obstruction; the trace field is. -/
theorem det_even_word (k : ℕ) : ((-1 : ℝ)) ^ (2 * k) = 1 := by
  rw [pow_mul]
  norm_num

/-- And an odd-length word has `det = −1`, so it cannot meet the `det = 1` field
at all — the braid image splits cleanly by parity. -/
theorem det_odd_word (k : ℕ) : ((-1 : ℝ)) ^ (2 * k + 1) = -1 := by
  rw [pow_succ, det_even_word]
  norm_num

end QOU.QBeta
