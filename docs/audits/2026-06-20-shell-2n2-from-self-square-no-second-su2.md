# 2n² shell capacity = self-square of one cosh-parity element (no second SU(2))

**Date:** 2026-06-20
**Branch:** `claude/zealous-hypatia-05xyp9` (PR #2348, bean `e2nf`)
**Compute:** [`computations/shell_capacity_chebyshev_bridge.py`](../../computations/shell_capacity_chebyshev_bridge.py)
(exact sympy). **Class:** formalize-first construction.

## Result (owner's "no second SU(2)" vindicated, with one residual conjecture)

The 2n² orbital degeneracy is the **self-square of a single bar-even (cosh)
element** — the q-Clebsch–Gordan of one `SU(2)_q` irrep with itself — not two
independent compact `SU(2)`s.

**Proven exactly (n = 1…8):**

| # | identity | meaning |
|---|---|---|
| II | `[n]_q = U_{n-1}((q+q⁻¹)/2)` | the angular q-dimension is the **cosh / bar-even** Chebyshev of the shell element `U_{n-1}` (the n-dim `SU(2)_q` irrep `V_{(n-1)/2}`) |
| III | `[n]_q² = Σ_{ℓ=0}^{n-1} [2ℓ+1]_q` | the **self-square** `dim_q(V⊗V) = ⊕_{ℓ=0}^{n-1} V_ℓ` (q-Clebsch–Gordan) |
| IV | `2[n]_q²\|_{q=1} = 2n²` | `= 2,8,18,32,…` — the shell capacities |

So `2n² = 2·[n]_q²|_{q=1} = 2·Σ_{ℓ=0}^{n-1}(2ℓ+1)`. The `(j,j)` "doubling" that
standard physics gets from `SO(4)=SU(2)×SU(2)` is here the **self-fusion `V⊗V`
of ONE element** — the second factor is a *copy* of the first, tied by the
coproduct, not an independent symmetry.

**The unification (one element, two parities).** The shell-`n` object is the one
Chebyshev `U_{n-1}`. Its **bar-even (cosh, `(q+q⁻¹)/2`)** evaluation is the
*angular* q-dimension `[n]_q` (degeneracy); its **bar-odd (sinh, `(q−q⁻¹)/2`)**
evaluation is the *radial* σ-tower side (shell index / energy). cosh ⊕ i·sinh =
the complex volume `𝔙` ([`bar-parity-split`](../../content/quantum-observable-universe/mass-theory/bar-parity-split.md)).
**This is the `SU(1,1)↔SU(2)` two-real-forms picture, no second compact group.**

**Residual conjecture (single step):** that the shell state space *is* the
self-square `[n]_q²` of the angular element (the `V⊗V` coproduct). Everything
else is exact. This replaces the `SO(4)/Runge–Lenz` *symmetry input* with a
*self-square* internal to the one `sl(2,ℂ)/𝔙` — a clean categorical operation,
not a symmetry to discover.

## Side-correction (content bug found)

[`shell-structure-eigenvalues.md`](../../content/quantum-observable-universe/predicted-spectra/shell-structure-eigenvalues.md)
claims `(T_γe^n)_{21} = U_{n-1}((q−q⁻¹)/2)` (Chebyshev-U at the sinh argument).
**Refuted exactly for n ≥ 3** — e.g. `(T³)₂₁ = q²−1+q⁻²` but
`U_2((q−q⁻¹)/2) = q²−3+q⁻²`. `T_γe` has `det = −1`, so its entries follow
`p_n = (q−q⁻¹)p_{n−1} + p_{n−2}` (plus sign), not the standard Chebyshev
recurrence (minus). The radial entries are the det = −1 ("Fibonacci–Chebyshev")
variant. To flag/fix in `shell-structure-eigenvalues.md` (does not affect the
2n² result, which lives on the cosh/angular side).

## Still separate — Gap 2 (Madelung)

The noble-gas *ordering* beyond 2n² (pure-2n² closes at `[2,10,28,60]`, not the
noble `[2,10,18,36]`) needs the screening / `n+ℓ` step. Open question (owner,
2026-06-20): how much of this falls out of the confinement-SDP optimal
active-set dressing sequence (the SDP *is* the many-body optimiser) — tracked
separately.
