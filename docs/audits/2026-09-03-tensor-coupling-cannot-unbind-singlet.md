# The (S, L) tensor coupling cannot fix the two-nucleon sign defect — qou-vbyi route 1 is a dead end for both A = 2 defects

**Date:** 2026-09-03 · **Beans:** `qou-s42j` (session), `qou-vbyi` (target), `qou-7nwg` (cited) ·
**Arc:** two-nucleon sector / "signs before digits" · **Scope:** a scope-(b) structural exclusion
with the invariants named, formalize-first (Lean, sorry-free). **Nothing is fitted, nothing is
wired, no number moves.**

## The defect, restated

`computations/probes/two_nucleon_sector_sign_probe.py`:

| system | framework | nature | |
|---|---:|---|---|
| pn (deuteron, ³S₁) | **+2.8328** MeV | `+2.2246` — BOUND | 27.3 % over |
| pp (diproton, ¹S₀) | **+2.5416** MeV | `a = −17.3 fm` — **UNBOUND** | **wrong sign** |
| nn (dineutron, ¹S₀) | **+3.3069** MeV | `a = −18.9 fm` — **UNBOUND** | **wrong sign** |

By Pauli, in a relative S-wave spin and isospin symmetries are opposite, so `pp` and `nn`
(`T = 1`) are **pure spin singlets** (`S = 0`). The sign defect *lives in the singlet*.

## What was already excluded (all Lean, sorry-free, on `main`)

| route | invariant | declaration |
|---|---|---|
| any single-crossing interface | `μ ≤ z < 1 ⟺ q³ < q²+1` | `QOU.QBeta.single_crossing_binds` |
| `T₃`-graded writhe on `pp` | non-negative exponent on a base in `(0,1)` | `t3_grading_cannot_unbind_pp` |
| Hecke spectral projectors | `μ₊ + μ₋ = 1` | `InterfaceScalar.mu_sum_eq_one` |
| any T-odd rescaling, any framing | total `−α log(μ₊μ₋)` invariant, floored at `α log 4` | `TwoChannelTotalBindingFloor` |
| any **separable** space factor `fSpin·fIso·fSpace` | both channels are S-wave (same `L`) | `InterfaceScalar.separable_interface_degenerate` |

The eight-closures audit (2026-08-16) closed the sector with the sign standing as a structural
defect. Bean `qou-vbyi` (2026-08-25/31) then named **one surviving shape**: a
**non-separable (S, L) coupling — the ³S₁–³D₁ tensor force** — "untouched by the above and the
live shape", because "a product of a spin function and a space function is exactly what a
coupling is not."

## The prune — two invariants, both proved

`content/quantum-observable-universe/lean/QOU/QBeta/TensorCouplingCannotUnbindSinglet.lean`
(namespace `QOU.QBeta.TensorCouplingSinglet`).

### (A) The tensor operator acts as a scalar on the singlet, and the scalar is 0

On two spin-½ particles with `|s⟩ = |↑↓⟩ − |↓↑⟩` and the tensor operator
`S₁₂(n) = 3(σ₁·n)(σ₂·n) − σ₁·σ₂`, exact `4×4` matrix algebra over `ℂ` gives

| statement | declaration |
|---|---|
| `σ₁·σ₂ \|s⟩ = −3 \|s⟩` | `sigmaDot_mulVec_singlet` |
| `(σ₁·n)(σ₂·n) \|s⟩ = −\|n\|² \|s⟩`, **every** `n` | `nDotProd_mulVec_singlet` |
| `S₁₂(n) \|s⟩ = 3(1 − \|n\|²) \|s⟩` | `tensorOp_mulVec_singlet` |
| `\|n\|² = 1 ⟹ S₁₂(n) \|s⟩ = 0` | `tensorOp_annihilates_singlet` |

The singlet is an **eigenvector of both generators for every direction**. So any coupling built
from `σ₁·σ₂` and `(σ₁·n)(σ₂·n)` has **no off-diagonal element out of `S = 0`**: there is nothing
to mix the singlet with (in angular-momentum language, at `J = 0` the `S = 0` channel has no
`L = 2` partner — `L = 2, S = 0` gives `J = 2`). The `pp` / `nn` channels are untouched by the
tensor coupling, at any strength, in any direction. **The sign defect cannot be reached by this
route.**

### (B) Off-diagonal coupling only lowers the ground state

Where the tensor force *does* act — the triplet, mixing `³S₁` with `³D₁` — the coupled block
`[[E_S, t], [t, E_D]]` has lower eigenvalue `λ₋ = (E_S+E_D)/2 − √(((E_S−E_D)/2)² + t²)`:

| statement | declaration |
|---|---|
| `λ₋` is a root of `(a−λ)(b−λ) − t² = 0` | `lowerEigen_is_eigenvalue` |
| `λ₋ ≤ a` | `lowerEigen_le_left` |
| `t ≠ 0 ⟹ λ₋ < a` (and `< b`) | `lowerEigen_lt_left_of_ne`, `lowerEigen_lt_right_of_ne` |

Any nonzero coupling puts the coupled ground level **strictly below** the uncoupled `³S₁` level:
tensor mixing binds the deuteron *harder*. The uncoupled channel is already **27.3 % over-bound**.
The coupling moves it the wrong way.

### Verdict

**Scope-(b) exclusion.** The non-separable (S, L) tensor coupling — `qou-vbyi` route 1 — is a
dead end for **both** `A = 2` defects: identically zero on the singlet where `pp`/`nn` live
(invariant A), and strictly deepening on the triplet where the deuteron is already over-bound
(invariant B). This closes the "live shape" the bean left open.

## What this does NOT exclude (honest scope)

- **Unbinding as such.** The writhe-normalised even-negative stacked words `σ^{−2k}` do give
  `μ_eff > 1` (`SingleCrossingAlwaysBinds` §scope; `stacked_interface_writhe_normalised_probe.py`)
  — at 6–9× nature's magnitude. A repair *direction*, not a repair; not a single crossing, not a
  spin-space coupling, so outside both this file and `single_crossing_binds`.
- **A change to the binding law** `B = −α log μ` itself. The `qou-y0mc` `S`-vs-`H` ambiguity is
  open — but the eight-closures audit already notes neither form fixes the *sign*
  (`−α·μ·log μ > 0` always).
- **Whether `pp` / `nn` are single-clasp bonds at all** (the carrier / bond-type assignment) — a
  different question from the interface value.
- **The `T`-projector route** is not what this file is about: `qou-7nwg` correctly notes the
  `T = 1 / T = 0` split is available in the Hecke algebra via `P±` with no spin at all — and the
  corpus already proves those scalars *both bind* (`mu_sum_eq_one`). This file closes the
  complementary spin-space route.

## What sharpens, for the next agent

The sign defect is now boxed from every interface-side direction: scalar (single crossing,
projectors, gradings, T-odd), separable space factor, **and** non-separable spin-space coupling.
Every surviving direction is *outside the interface value*: the stacked-word class (wrong
magnitude), the binding law, or the bond/carrier assignment for `pp`/`nn`. "Signs before digits"
still gates the L2 binding claim; this narrows where the sign can come from, it does not supply it.

## Verification

`lean`-direct, sorry-free; `#print axioms` on all eight declarations =
`{propext, Classical.choice, Quot.sound}` (no `sorryAx`). The four (A) matrix identities were
independently exact-verified in sympy (`computations/probes/tensor_coupling_singlet_check_probe.py`, 13/13: explicit `4×4` forms match
the Kronecker construction; eigenvalues `−3`, `−|n|²`, `3(1−|n|²)`). Repo CI is
`workflow_dispatch`-only; the agent verification above is the gate.
