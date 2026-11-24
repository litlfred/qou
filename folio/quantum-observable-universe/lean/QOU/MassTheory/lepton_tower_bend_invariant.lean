import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# QOU.Archimedean.lepton_tower_bend_invariant — the screening invariant for any generation bridge

Companion to `lepton_continuant_binet` / `lepton_continuant_positivity`,
serving bean `qou-htk4` (the successor to `qou-lsp9`).  Numerical twin:
[`lepton_tower_bend_screening.py`](../../../../../computations/lepton_tower_bend_screening.py).

## The problem this solves

`qou-lsp9` closed one candidate bridge at a time — first `net`, then every
positive linear readout of `H₂(q)`.  Candidate-by-candidate refutation
does not scale, and worse, it invites fitting: a candidate `f` plugged
into `m_w = C · g^w · f(w)^p` always has three free parameters against the
two observed lepton ratios, so *something* can always be made to fit.

The fix is to work with a quantity the free parameters cannot touch.

## The bend

For a tower `x` sampled at three consecutive generation windings, define

```
  bend x w = x(w+2)² / (x(w) · x(w+4)).
```

`bend_of_scaled_geometric_pow` is the point of the whole file:

```
  m_w = C · g^w · f(w)^p     ⟹     bend m w = (bend f w)^p
```

**`C` and `g` cancel exactly.**  The overall mass scale and the
per-generation geometric factor — the two knobs that make every candidate
look adjustable — drop out of the bend identically.  Only the exponent
survives, so a candidate readout is screened by a *single* number with a
*single* free parameter, not three.

## What it buys immediately

`bend_of_geometric`: a readout that is exactly geometric in the winding
has `bend = 1`.  Combined with the transport law, `geometric_readout_forces_unit_bend`
says any such readout forces `bend m = 1` **for every `C`, `g` and `p`
simultaneously** — so a tower whose measured bend is not `1` excludes that
entire three-parameter class outright, with no fine-tuning argument and no
appeal to how large `p` would have to be.

The measured lepton bend is `m_μ² / (m_e · m_τ) ≈ 12.295`, nowhere near
`1`.  That single number is what kills every exponential-type invariant of
`T(2,n)` at once — the Jones polynomial and the Markov trace included,
since in the two-dimensional `H₂(q)` those are linear readouts and hence
geometric up to `O(q⁻²ⁿ)` by `linFunctionalK_two_step`.

`bend_of_linear` covers the other standard family: a readout linear in the
winding has `bend = (w+2)²/(w(w+4))`, which at the lepton windings
`(3,5,7)` is `25/21 ≈ 1.19` — also nowhere near `12.295`.  Between them
these two lemmas cover essentially every classical knot invariant of
`T(2,n)`: each is either polynomial in the winding (bend near `1` from
below) or exponential in it (bend exactly `1`).

## How to use it

Screen a candidate bridge by computing one number.  A viable
parameter-free bridge needs `bend f ≈ 12.295` at `p = 1`, or `≈ 3.51` at
`p = 2`, or `≈ 2.31` at `p = 3`.  Anything with `bend` near `1` requires a
large exponent and is a fit, not a derivation.

-- Ref: [leitner2026] quantum-observable-universe/predicted-spectra/lepton-continuant-recurrence.md
-/

namespace QOU.Archimedean

variable {K : Type*} [Field K]

/-- The three-point **bend** of a tower at windings `w`, `w+2`, `w+4`:

```
  bend x w = x(w+2)² / (x(w) · x(w+4)).
```

Multiplicatively this is the log-concavity of the tower — `bend > 1` means
the log-increments are decreasing.  For the charged leptons at windings
`(3, 5, 7)` it is `m_μ² / (m_e · m_τ) ≈ 12.295`. -/
def bend (x : ℕ → K) (w : ℕ) : K := (x (w + 2)) ^ 2 / (x w * x (w + 4))

/-- **The bend transports through the whole bridge class, and the two
fitting knobs cancel.**

If `m_w = C · g^w · f(w)^p` then `bend m = (bend f)^p`: the overall scale
`C` and the geometric factor `g` drop out *identically*, leaving the
exponent as the only surviving freedom.

This is what makes the bend a screening tool rather than one more quantity
to fit.  A candidate readout `f` is tested by comparing `bend f` against
the measured `bend m`, with two of the three free parameters already
eliminated. -/
theorem bend_of_scaled_geometric_pow {w : ℕ} (C g : K) (p : ℕ) (f m : ℕ → K)
    (hm : ∀ k, m k = C * g ^ k * (f k) ^ p)
    (hC : C ≠ 0) (hg : g ≠ 0) (h0 : f w ≠ 0) (h4 : f (w + 4) ≠ 0) :
    bend m w = (bend f w) ^ p := by
  have hC2 : C ^ 2 ≠ 0 := pow_ne_zero _ hC
  have hgw : g ^ w ≠ 0 := pow_ne_zero _ hg
  have hg4 : g ^ 4 ≠ 0 := pow_ne_zero _ hg
  have h0p : (f w) ^ p ≠ 0 := pow_ne_zero _ h0
  have h4p : (f (w + 4)) ^ p ≠ 0 := pow_ne_zero _ h4
  simp only [bend, hm, div_pow, ← pow_mul, pow_add]
  field_simp
  ring

/-- **A readout that is exactly geometric in the winding has bend `1`.**

`x(w) = a · r^w` gives `bend x w = 1` for every `w`: the numerator
`a² r^(2w+4)` and the denominator `a² r^(2w+4)` agree identically. -/
theorem bend_of_geometric (a r : K) (ha : a ≠ 0) (hr : r ≠ 0) (w : ℕ) :
    bend (fun k => a * r ^ k) w = 1 := by
  have ha2 : a ^ 2 ≠ 0 := pow_ne_zero _ ha
  have hrw : r ^ w ≠ 0 := pow_ne_zero _ hr
  simp only [bend, pow_add]
  field_simp

/-- **The screening theorem.**

A geometric readout forces `bend m = 1` for *every* `C`, `g` and `p` at
once.  Hence a tower with any measured bend other than `1` is incompatible
with the entire three-parameter class built on a geometric readout — no
fine-tuning argument required, and no need to ask how large `p` would have
to be.

Applied to the leptons: the measured bend is `≈ 12.295`, so every
exponential-type invariant of `T(2,n)` is excluded in one step. By
`linFunctionalK_two_step` that includes every linear readout of `H₂(q)`
up to its `O(q⁻ⁿ)` remainder — the Markov trace and the Jones polynomial
among them. -/
theorem geometric_readout_forces_unit_bend {w : ℕ} (C g a r : K) (p : ℕ)
    (m : ℕ → K) (hm : ∀ k, m k = C * g ^ k * (a * r ^ k) ^ p)
    (hC : C ≠ 0) (hg : g ≠ 0) (ha : a ≠ 0) (hr : r ≠ 0) :
    bend m w = 1 := by
  have h0 : a * r ^ w ≠ 0 := mul_ne_zero ha (pow_ne_zero _ hr)
  have h4 : a * r ^ (w + 4) ≠ 0 := mul_ne_zero ha (pow_ne_zero _ hr)
  rw [bend_of_scaled_geometric_pow C g p (fun k => a * r ^ k) m hm hC hg h0 h4,
    bend_of_geometric a r ha hr w, one_pow]

/-- **A readout linear in the winding has bend `(w+2)²/(w(w+4))`.**

At the lepton windings `(3, 5, 7)` this is `25/21 ≈ 1.190`, independent of
the constant `c`.  Together with `bend_of_geometric` this covers the two
families every classical `T(2,n)` invariant falls into: the polynomial
ones (crossing number, determinant `= n`, genus, signature) land near
`1.19`, the exponential ones land exactly on `1`, and the measured lepton
bend is `12.295`. -/
theorem bend_of_linear (c : K) (hc : c ≠ 0) (w : ℕ)
    (hw : (w : K) ≠ 0) (hw4 : ((w : K) + 4) ≠ 0) :
    bend (fun k => c * (k : K)) w
      = ((w : K) + 2) ^ 2 / ((w : K) * ((w : K) + 4)) := by
  simp only [bend, Nat.cast_add, Nat.cast_ofNat]
  field_simp

end QOU.Archimedean
