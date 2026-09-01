# The tower is not elliptic — the decay operator's spectral curve, exactly in `q`

**Date:** 2026-08-31 · **Bean:** `qou-cds1` (Step 26) · **Scope:** (a).

**Artifacts.**
[`QOU/QBeta/DiscriminantCurveInQ.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/DiscriminantCurveInQ.lean)
(15 theorems, sorry-free, axioms `[propext, Classical.choice, Quot.sound]`) ·
[`qbeta_discriminant_curve_in_q_probe.py`](../../computations/qbeta/qbeta_discriminant_curve_in_q_probe.py)
(8/8). Corrects
[the elliptic-spectrum finding](./2026-08-31-qbeta-imq-elliptic-generator-refutation.md)'s
successor steps 21–25.

---

## The correction this file exists for

Steps 21–25 of `qou-cds1` each evaluated a spectrum at the **single numerical
point** `q = q₀ = 1.1099785827513808`. One sample cannot tell a discriminant that
is a perfect square from one that is an irreducible degree-18 polynomial, so no
step in that range could have decided anything about the tower — and each of them
asserted tower-level conclusions anyway. The owner's diagnosis ("perhaps you are
collapsing to order zero and not seeing the twisting as we go out the tower") was
right about the method, and this step redoes the question with `q` carried
symbolically throughout.

**A second, factual correction, also mine.** Step 25's write-up said `Δ_L`
"cannot be asked this question" because `build_nucleon_nf` takes no `q`. That is
wrong. `hecke_core_symbolic.hm_sym` is the symbolic-`q` twin of `hm`; mirroring
`pyhecke.atom.build_nucleon_nf`'s 11-crossing word through it gives the nucleon
normal form as an exact element of `ℚ(q)`. It agrees with the canonical numeric
builder to `9·10⁻¹⁷` in all twelve coordinates. There was no gap — there was a
function I did not look for.

> **A trap worth writing down.**
> `shift_from_nf_basis.build_nucleon_nf_sym_atomic` looks like the mirror and is
> not. It agrees on the crossing **counts** and the 7/4 per-generator split — its
> docstring says so — but applies all gen-0 crossings before all gen-1, i.e. the
> **monotone re-sort** of `B₃`, where the canonical builder alternates.
> `nucleon_braid_word`'s own docstring measures that re-sort at **82 %** on
> `tr_M`. Using it here would have silently answered a different question, and
> the disagreement shows up as `L₊ = e⁻ = 0` — a signature, not a rounding error.

---

## 1 · There is no twisting to be missed

For `Δ_L = NF(neutron) − NF(proton)` in the `(2,1)` block, as exact identities in
`ℚ(q)`:

| invariant | bar parity | |
|---|---|---|
| `tr(1/q)` | `= −tr(q)` | bar-**odd** |
| `det(1/q)` | `= +det(q)` | bar-**even** |
| `disc(1/q)` | `= +disc(q)` | bar-**even** |

So the bar involution acts trivially on the spectral geometry: there is **no
`q⁻ⁿ` twist anywhere**, and `disc` is forced to be a polynomial in the
bar-invariant coordinate `x = q + 1/q`. That is the twisting question, answered
by an identity rather than by a sample.

It has a payoff on the unit circle. Bar-odd `tr` means `tr` is **purely
imaginary** for `|q| = 1` and bar-even `det` means `det` is **real** there —
confirmed to 40 digits (`|Re tr| < 1.5·10⁻⁴⁰`, `|Im det| < 4.0·10⁻⁴²`). Every
root of unity therefore carries a real discriminant and a well-defined
eigenphase; see §5.

## 2 · The two spectral curves

**Short model** (`Δ_S`, the ladder's closed forms):

```
disc_S(q) = h(q)²                    a perfect square in q
disc_S(x) = (x − 2)(x + 2) = x² − 4  a conic in x
```

`y² = disc_S` has **genus 0** either way. And `x = q + 1/q ≥ 2` for every real
`q > 0`, so `disc_S ≥ 0` **identically**: `Δ_S` is hyperbolic at every real `q`,
degenerate only at `q = 1`. The short model is closed for all `q`, not merely at
`q₀` — the statement the point evaluations could not make.
(`shortModelDisc_eq_hSq`, `shortModel_not_elliptic`, `two_le_add_inv_of_pos`.)

**Long model** (`Δ_L`, what production runs on):

```
disc_L(x) = (x − 2)(x + 2) · G₋(x) · G₊(x) / 16
G∓(x)     = 2x⁸ − 21x⁶ + 77x⁴ − 115x² ∓ 2x + 58
```

Degree 18, **squarefree**, four irreducible factors over `ℚ`. So `y² = disc_L(x)`
is hyperelliptic of **genus 8**; being even in `x` it covers `y² = R(w)`,
`w = x²`, of degree 9 — **genus 4**.

**Neither is genus 1.** There is no elliptic curve here, and therefore no tower
of elliptic curves indexed by anything. (`discLong_factor`, `discLong_even`,
`discLong_eq_quotient`; the probe checks its own polynomial against the Lean
literals so the two cannot drift apart.)

## 3 · The Hecke tower adds nothing, by branching

`Res^{H_n}_{H_{n−1}} S^λ = ⊕_μ S^μ` over `μ = λ` minus a box. Every corpus object
is `H₃`-valued (Step 25), so its spectrum in any `H_n` irrep is a union with
multiplicity of its three `H₃` spectra — **no new eigenvalue, hence no new
discriminant, at any level `n`**. Verified on all five `H₄` shapes at three
different `q`: `(2,2) = (2,1)`, `(3,1) = (3) + (2,1)`, `(2,1,1) = (1³) + (2,1)`,
`(4) = (3)`, `(1⁴) = (1³)`.

## 4 · The classical limit is exactly `2π/3` — and the trefoil is second-order

Every NF coordinate of `Δ_L` carries a factor `(q−1)(q+1)`, so `Δ_L → 0` at
`q = 1`: the nucleons are degenerate classically and the whole difference is a
deformation effect. The **direction** it vanishes along is not degenerate. Orders
of vanishing in `ε = q − 1`:

| `γ` | `σ₀` | `σ₁` | `L₊` | `L₋` | `e⁻` |
|---|---|---|---|---|---|
| **1** | 2 | 2 | 3 | **1** | 2 |

so the leading direction is `−(γ + L₋) = −(1 + T₁T₀)`, and `T₁T₀` is the `S₃`
three-cycle, whose standard-rep eigenvalues are the primitive cube roots of
unity. Hence modulus 1, `tr = −1`, `det = 1`, `disc = −3`, and eigenphase
**exactly `2π/3`**. (`classical_charpoly`, `classical_cube_root`,
`classical_order_three`, `classical_cos_eigenphase`.)

Note where the trefoil sits in that expansion. The corpus's electron word
`e⁻ = T₀T₁T₀` — the longest element — enters only at **second** order. The thing
that does the decay is `1 + L₋` at leading order; the trefoil is its first
correction, not its leading term.

## 5 · Two towers, and the phase in both

**The real branch.** `disc_L` has exactly two real roots with `x ≥ 2` (the range
of `x = q + 1/q`): `x = 2` and `x = 2.104510749293091`. So

> `Δ_L` is **elliptic exactly for `q ∈ (1, 1.379732661603278)`**, and
> `q₀ = 1.1099785827513808` sits **29.0 %** of the way up that window.

Its eigenphase sweeps monotonically from `2π/3` at `q → 1⁺` down to `0` at the
upper wall, where the spectrum degenerates. `θ(q₀) = 2.02044502` — reproducing
the `2.0204` measured numerically in Step 22 and carried through Step 25, from a
completely independent construction.

Because `θ` sweeps continuously to zero, the required ladder phase **is**
attained. This step locates where, precisely so the avenue closes on data rather
than on taste:

| convention | `θ` required at `q₀` | `q*` where `θ_L = θ_req` | `(q* − q₀)/σ_q₀` | `q_hi − q*` |
|---|---|---|---|---|
| `z_C` | `0.0565947375` | `1.37812464914` | **`2.91·10¹¹`** | `0.0016` |
| `z_D` | `0.0447443946` | `1.37956231361` | **`2.93·10¹¹`** | `0.00017` |

with `σ_q₀ = 9.2116·10⁻¹³`, the substrate pin's uncertainty propagated from
CODATA `m_p/m_e`. Both crossings land inside the last 0.2 % of the window, hard
against the degeneracy wall: **the phase is only small where `Δ_L` is about to
stop being elliptic at all.** And both are excluded by the calibration at three
hundred billion σ.

This is a falsification test, not a search. The curve was derived first, the
crossing was located afterwards, and the distance was measured. `q*` is recorded
as a fact **about the curve** and is never a candidate `q`.

**The cyclotomic branch — `q = ζ_N`, `N` the degree.** The one reading of
"indexed by the degree of `q`" that is a genuine tower, and it does move:

| `N` | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 13 | 20 | 29 | 60 | 120 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `φ_N` | `2π/3` | sing. | deg. | `2π/3` | `1.4042` | `π` | `2.1664` | `2.9211` | `2.0344` | `1.8116` | `1.9775` | `2.0622` |

`N = 3` and `N = 6` hit the classical `2π/3` exactly (`disc = 9/16` at both),
`N = 8` gives exactly `π`, `N = 4` is singular (`det = 0`, `tr = 29i`), `N = 5`
degenerate, and `φ_N → 2π/3` as `N → ∞`. The minimum over every non-degenerate
`N ≤ 120` is `φ₇ = 1.4042283` — still **24.8×** the required phase.

---

## What changed, and what did not

**Changed.** The short model is closed for all `q`, not just `q₀`. The long model
has a named curve of genus 8 instead of a number. The classical limit is an exact
`2π/3` with an identified mechanism, and the trefoil's place in it is pinned at
second order. The ladder-phase identification is excluded **quantitatively by the
substrate pin** rather than by inspection.

**Not changed.** No `c_k` value is asserted, no convention adjudicated, nothing
proposed, wired or readmitted.

## What is deliberately not in Lean

The bar-parity identities for the long model and the location of `disc_L`'s real
roots. Both are in the witness with their exact expressions; carrying the
degree-36 numerator into Lean would add weight without adding confidence, since
`ring` on the factored form already pins the polynomial everything else is read
off. The ellipticity window and the `3·10¹¹ σ` exclusion are **measurements**,
not identities, and belong in the witness rather than in a theorem.
