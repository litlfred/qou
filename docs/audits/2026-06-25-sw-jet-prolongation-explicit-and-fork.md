# Explicit λ_SW^(n) jet-prolongation + the depth-2-vs-super-exponential fork

**Date:** 2026-06-25
**Branch:** `claude/sw-lambda-jet-prolongation-2026-06-25`
**Probe:** [`computations/sw_period_growth_probe.py`](../../computations/sw_period_growth_probe.py)
**Coordinates with:** bean `z2bn` (Lever-1, the binding-τ keystone)

## The explicit prolongation (candidate) and its grounding

**Upstream — corpus-stated** ([`mi-sw-abelianisation-proof.md`](../../content/quantum-observable-universe/brings-surface/mi-sw-abelianisation-proof.md) Step 3, [`jet-prolongation.md`](../../content/quantum-observable-universe/lifting-and-descent/jet-prolongation.md)):
- `λ_SW^(0) = X dz` (X = root of the color cubic `X³+(z+1)X²+(z²+z+1)X+(z³+z²+z+1)=0`)
- `λ_SW^(1) = dX` ("the implicit derivative of the color tube cubic")
- `λ_SW^(n≥2)` = **"higher jets follow by induction"** via `J^n = J^1(J^{n-1})`, `J^1(A)=A⊗Ω^1(A)`

**Inference (this session).** Reading the jet induction as iteration of the
implicit/total derivative `D = ∂_z + X'·∂_X` (it cannot be exterior `d`, since
`d²X=0`):

$$\boxed{\;\lambda_{\rm SW}^{(n)} = X^{(n)}(z)\,dz = D^n(X)\,dz\;}$$

— a **computable** rule to any order, filling the "by induction" gap.
Substrate jets: `X(z₀)=−1.0525`, `X'=−0.5095`, `X''=−0.1744`.

**Caveat (the one unverified step).** `n=0,1` are corpus-stated; `λ_SW^(n)=X^(n)dz`
for `n≥2` is the natural reading, but the n-jet object `A⊗Ω^1⊗…` could be a
fuller tensor than its top 1-form. Confirming "top component vs full Kähler-jet"
is the open point for z2bn.

**Downstream — consumers of `a_D^(n)=∮_{S_c}λ_SW^(n)`:**
- `mi-sw-abelianisation`: `‖MI∫_{S_c}‖_{J^n}=|a_D^(n)|` (n-th jet of the Yekutieli MI∫)
- `binding-manybody-jet-filtration`: `B(K)=Σ_{n≥2} m_e·a_D^(n)` (n=2 deuteron, n=4 magic-shell ⁴He)
- `sl2-prolongation-recurrence`: `a_D^(n+2)=τ a_D^(n+1)−a_D^(n)`, `τ=(a_D^(2)+a_D^(4))/a_D^(3)`
- `electron-period-base`: `a_D^(2)=τ a_D^(1)−m_e`, `a_D^(0)=m_e`

## The fork — settled structurally

Two corpus claims for the same `a_D^(n)`:
- **(i) SL₂ depth-2** `a_D^(n+2)=τa_D^(n+1)−a_D^(n)` → **geometric**, ratio → λ₊≈2.18.
- **(ii) #1765** `a_D^(n)=lw(n−1)=(1/n)Σ_{λ⊢n}dim_q` → **super-exponential** (measured).

They agree at n=2,3,4 (τ is *fit* to those 3 anchors) and through n=5, then split.

**Resolution.** `γ` encircles branch points where `disc_X=0` ⇒ two sheets collide
⇒ **square-root branch** (verified: sheet-gap → 4.5e-16). Then `X^(n)~(z−z_k)^{1/2−n}`,
so the period coefficient `|(1/2)_n^{fall}|` has ratio `(n−½)` = 1.5, 2.5, 3.5, …
— **growing without bound ⇒ super-exponential**. This also dissolves the apparent
paradox that the *pointwise* jets `X^(n)(z₀)` shrink: z₀ is inside the convergence
disk; the *period* is dominated by the branch-point singularity.

| n | lw/#1765 (ratio) | depth-2/SL₂ (ratio) |
|--:|---:|---:|
| 4 | 2.533 (1.894) | 2.533 (1.894) |
| 5 | 5.376 (2.123) | 5.356 (2.115) |
| 6 | **13.560** (2.522) | **11.619** (2.169) |
| 8 | 115.83 (3.100) | 55.35 (2.184) |

**Verdict:** `a_D^(n)` grows super-exponentially ⇒ **lw/#1765 is the true
prolongation; the depth-2 SL₂ τ is an n≤4 effective fit** (it cannot produce
factorial growth). The q-difference kernel for the super-exp `a_D^(n)` is the
**q-Bessel** class (`jackson-q-bessel-contiguity`, `QBesselContiguityRecurrence.lean`)
— the natural fast production engine.

## Compute wire-up after Lean formalization

1. **Producer** `sw_prolongation_periods.py`: explicit `λ_SW^(n)=X^(n)dz` jets + periods `a_D^(n)`; witness. Replaces the SL₂ effective-fit `sw_prolongation_symbol.py`.
2. **Binding consumer** `B(atom)=Σ_{n=2}^{A} m_e·a_D^(n)·w_n(K)` (body-order series, truncated at nucleon count A) — **sidesteps the Δ_λ gate** (jet-filtration replaces per-block Δ_λ).
3. **Fast engine:** the q-Bessel contiguity recurrence (already Lean-formalized) as the compute kernel for `a_D^(n)`.
4. **Cross-checks:** `a_D^(n)` period ≡ `lw(n−1)` (#1765); ≡ q-Bessel recurrence.
5. **Downstream:** `B(atom)→m(atom)` into the mass-table sweep + L2 dashboard; MBA-appendix `alg:` block.

## Reproduce

```bash
cd computations && python3 -u sw_period_growth_probe.py
```
