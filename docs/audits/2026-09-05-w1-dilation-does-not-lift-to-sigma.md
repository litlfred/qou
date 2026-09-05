# No nontrivial base dilation lifts to Σ — the branch sextic settles it in two coefficients

**Date:** 2026-09-05 · **Bean:** `qou-lmnq` · follows `qou-7fnr` (#6738), `qou-1z28` (#6695), `qou-an6y` (#6652), `qou-col1` (#6628)
**Lean:** [`QOU/Mass/DilationBranchLocusRigidity.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/DilationBranchLocusRigidity.lean) — sorry-free, generic `[Field K] [CharZero K]`, `lean`-direct exit 0, axioms `propext / Classical.choice / Quot.sound` on all four declarations
**Probe:** [`w1_dilation_no_lift_to_sigma_probe.py`](../../computations/probes/w1_dilation_no_lift_to_sigma_probe.py) — exact sympy over `ℚ`; the substrate read-out is mpmath at 60 dps; no float64; no witness by design
**Cited, not re-derived:** [`c3_w1_cover_monodromy.py`](../../computations/qbeta/c3_w1_cover_monodromy.py) — the S₃ covering monodromy

## What was asked

W1 (`qou-d8de`) asks for a q-difference prolongation `D_q` built from the colour
spectral curve Σ, and its first named route is a **q-shift on the base**,
`z ↦ q²z`. Two tranches have excluded that route by constraining the
**coefficient field**:

| PR | excludes |
|---|---|
| #6695 | a rational q-connection on the `z`-line with the sheets as flat sections |
| #6738 | the same, after localising at a ramification point (`z = z_c + t²`) |

#6738 closed by naming what those leave standing: *"coefficients not rational in
a coordinate, or an operator on Σ"*. This tranche settles the second, and it
constrains no coefficient field at all.

## The argument

Let `π : Σ → P¹` be the 3-sheeted cover and `m_λ(z) = λz`. Suppose
`σ : Σ → Σ` is an automorphism with `π ∘ σ = m_λ ∘ π`.

1. **σ permutes the branch locus.** σ and `m_λ` are isomorphisms, so
   `e_{σ(p)}(π) = e_p(π)`: a point is ramified exactly when its image is.
   Branch points are the images of ramification points, so `m_λ` maps the branch
   locus to itself. `m_λ` fixes `0` and `∞`, and `D(0) = 16 ≠ 0` puts `0`
   outside the locus, so `m_λ` permutes the **six finite** branch points — the
   zeros of the branch sextic
   `D(z) = 16z⁶+24z⁵+35z⁴+50z³+35z²+24z+16`, `= −disc_X P`
   (`QOU.Mass.ColorSpectralCubicGeometry.color_cubic_discriminant`).
2. **Equal root multisets means proportional polynomials.** `D` is squarefree
   (probe §1), so `D(λz)` and `D(z)` share a root multiset iff
   `D(λz) = c·D(z)` for a constant `c`.
3. **Two coefficients finish it.** The constant term gives `16 = 16c`, hence
   `c = 1`; the linear term then gives `24λ = 24`, hence `λ = 1`.
   `QOU.Mass.DilationBranchLocusRigidity.dilation_scaling_rigid`, sorry-free.

**Conclusion (scope (b); the invariant is the sextic's own coefficients).** The
only dilation of the base admitting a lift to Σ is the identity — for **every**
`λ`, at **every** `q`. So the surviving "operator on Σ" alternative is not
available to the dilation route.

Step 1 is stated in prose and is **not formalised**; the Lean carries the
algebraic core (step 3) that it reduces to, and the file header says so.

## Why this is complementary to Bézivin–Ramis, not a corollary of it

The rationality theorem #6695 and #6738 lean on requires **`λ` not a root of
unity** and **rational coefficients**. This argument needs neither: it is a
statement about which self-maps of the `z`-line the curve admits, so it covers
the root-of-unity case the theorem explicitly does not, and it says nothing
about, and needs nothing from, the coefficient field.

## What the probe measured

| § | check | result |
|---|---|---|
| 1 | `D = −disc_X P`; matches the corpus's `branchSextic`; squarefree; `D(0) = 16`; degree 6; product of roots `= 1`; palindromic | all true |
| 2 | exact solve of `D(λz) = c·D(z)` over `ℚ̄` | the single solution `(λ, c) = (1, 1)` |
| 3 | **control** — the same solve on `z⁶ − 1` | six solutions, exactly the sixth roots of unity |
| 4 | S₃ premises reproduced (irreducible; `disc` not a square) | `S3`, attributed to the cited probe |
| 5 | `λ = q₀²` at the canonical proton pin | `1.232052454166763931269805`; fails `λ = 1` and `λ⁶ = 1` |

**§3 is the section that makes §2 mean something.** A solve returning only the
trivial answer is worth nothing unless the same machinery can return a
nontrivial one, and on `z⁶ − 1` it returns all six roots of unity. So §2 is a
property of the branch sextic — specifically of its nonzero **constant and
linear** coefficients — and not an artefact of the searcher.

§2 also records the weaker bound that survives if those coefficients ever
change: `λ·B = B` alone gives `∏(λz_c) = ∏ z_c`, and the product of the roots is
`16/16 = 1`, so `λ⁶ = 1`. The substrate value fails that too.

## How this composes with what the corpus already held

`c3_w1_cover_monodromy.py` establishes full S₃ covering monodromy and concludes
that `D_q` *"cannot be a single-valued algebraic operator on the base — it lives
on the 3-sheeted cover."* That is what makes the present result load-bearing
rather than incidental: the prior probe pushes `D_q` onto Σ, and this one says
**the dilation cannot follow it there**. Neither result is interesting without
the other.

The dilation route is now closed in all three places it could have lived:

| where | closed by |
|---|---|
| the base coordinate `z` | #6695 |
| the ramified local coordinate `t` | #6738 |
| Σ itself | this tranche |

## Scope — what is not excluded

- **A q-difference operator whose base map is not a dilation.** Every statement
  here is about `z ↦ λz`. A base map of another shape is untouched.
- **Route 2 of `qou-d8de`, the root-of-unity fibre monodromy.** That datum acts
  on the *fibre*, and no statement about self-maps of the `z`-line bears on it.
  It is now the live route.
- **Route 3, the Ramis–Sauloy–Zhang / Sauloy local framework import.** Untouched,
  and after three chart-based exclusions it is the natural next step.
- `D_q` is **not constructed**. This tranche removes a route.

## Reproduce

```bash
PYTHONPATH=computations:tools/qou-substrate/python \
  python3 -u computations/probes/w1_dilation_no_lift_to_sigma_probe.py
# Lean (lean-direct against the restored olean cache):
lean content/quantum-observable-universe/lean/QOU/Mass/DilationBranchLocusRigidity.lean
```
