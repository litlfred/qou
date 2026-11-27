# α_EM CS tower: the Seifert κ at the corpus's own Alexander variable (2026-11-27)

Bean `qou-gwio` (α_EM structural residual, −467.6 ppb); epic `qou-myts`, brief C4.
Probe [`alpha_em_kappa_alexander_variable_probe.py`](../../computations/alpha/alpha_em_kappa_alexander_variable_probe.py),
witness `alpha-em-kappa-alexander-variable.witness.json`. Mathematics first; CODATA
enters only in the comparison table.

## Question

The resummed Chern–Simons tower is
`1/α = bare·(1 + c₁/(1 − c₁κ))`, `bare = q[9]_q[10]_q`. With the shipped Witten
Gram ratio `κ_W = 1.7216` it misses by −467.6 ppb (proton pin). Two results were
already in the corpus and are **not** recorded on `qou-gwio`:

- `alpha_em_kappa_qdeformation_family_probe.py`: all 16 readings of "replace m, n by
  [m]_q, [n]_q" in the Witten 2×2 Gram miss the window; κ is basis-independent
  (`QOU.Archimedean.gramDetRatio_congr_invariant`).
- `alpha_em_seifert_kappa_pairing_probe.py` (2026-11-24): the 8×8 Seifert pairing on
  `H₁(Σ₄) = ℤ⁸` gives `κ(u) = 1/(u⁸ Δ_{T(2,9)}(u) Δ_{T(3,5)}(u))` and, **at u = q⁻¹**,
  −24.53 ppb (proton) / +55.16 ppb (muon).

Is `u = q⁻¹` derived, or picked?

## What the corpus fixes

Convention D (owner ruling 2026-08-15) fixes the Hecke generator by
`(T − q)(T + q⁻¹) = 0`. The eigenvalue ratio is `−q⁻²`, and the Burau representation
(eigenvalues `1, −t`) is the Hecke `(n−1,1)` representation at `t = q^{∓2}`. The
corpus already uses that variable for the same carrier:
`QOU/StandardModel/AlphaEmT35Linchpin.lean` proves
`Δ_{T(3,5)}(q²) = (q − q⁻¹)(q¹⁵ − q⁻¹⁵)/((q³ − q⁻³)(q⁵ − q⁻⁵))` and ties it to the bare
factor. The variable `t = q^{±1}` would need eigenvalue ratio `−q^{∓1}`, i.e.
generators with eigenvalues `q^{1/2}, −q^{−1/2}`; convention D does not supply it.

Proved symbolically in the probe (sympy, difference = 0):

- `det(V₂₉ − V₂₉ᵀ)det(V₃₅ − V₃₅ᵀ) / det(V₂₉ − uV₂₉ᵀ)det(V₃₅ − uV₃₅ᵀ) = 1/(u⁸Δ₂₉(u)Δ₃₅(u))` for all `u`;
- `Δ_{T(p,r)}(q²) = [pr]_q/([p]_q[r]_q)` for `(2,9)` and `(3,5)`;
- hence the convention-D member has the closed form
  `κ_D(q) = κ(q⁻²) = q¹⁶ [2]_q[9]_q[3]_q[5]_q / ([18]_q[15]_q)`.

`u = q⁻²` was pre-registered (in the probe docstring) before evaluation, keeping the
existing probe's orientation and squaring the variable.

## Comparison (80 dps)

| member | κ | proton pin (ppb) | muon pin (ppb) |
|---|---|---|---|
| **u = q⁻² (convention D, pre-registered)** | 2.62955 | **+1726.8** | **+1806.5** |
| u = q⁻¹ (existing Seifert probe) | 1.90516 | −24.5 | +55.2 |
| u = q | 0.35884 | −3749.7 | −3670.1 |
| u = q² | 0.09329 | −4387.7 | −4308.0 |
| Witten Gram (shipped) | 1.7216 | −467.6 | −387.9 |
| κ that would close (diagnostic only) | 1.9153 / 1.8823 | 0 | 0 |

## Reading

1. **Scope-limited negative (a).** The Seifert-pairing κ at the Alexander variable
   that convention D fixes overshoots, +1727 ppb: 3.7× the shipped miss, opposite
   sign. It does not close the residual.
2. **The −24.5 ppb figure is a selection, not a derivation, as it stands.** It is one
   of four members `u ∈ {q^{±1}, q^{±2}}` and is the only one near the target; its
   variable is not the one the corpus's Hecke algebra gives. It should be labelled
   *selected* on the dashboard and in `rem:em-coupling-chern-simons` until a reason
   for `t = q` (a half-twist / framing argument that halves the Burau exponent) is
   derived. This is recorded, not changed: the block edit waits for the owner.
3. **No member is excluded structurally (b).** Nothing here proves the Seifert
   pairing is the wrong object; it proves the corpus-variable member misses.
4. **Pin floor.** The needed κ moves from 1.9153 (proton) to 1.8823 (muon), and every
   member's residual moves by ≈ 80 ppb between pins. So no α_EM residual below about
   80 ppb is meaningful until the proton/muon pin tension (`qou-2002`) is settled;
   "closing" the residual to the ppb level is blocked on that, whatever κ is.

## Not done here

- The two-loop coefficient (`qou-l4t2`) stays NEEDS-OWNER: the canonical α_EM form is
  open (`qou-aemx`), so "the" coefficient is not one object.
- No Lean. The identities are exact sympy cancellations; a `[Field K]` port of
  `κ_D` closed form is straightforward if wanted.
