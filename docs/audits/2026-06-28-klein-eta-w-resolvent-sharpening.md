# η↔w resolvent — sharpening the last open step of the Klein bridge (with an obstruction guard)

**Date:** 2026-06-28
**Branch:** `claude/klein-eta-w-resolvent-2026-06-28`
**Status:** Sharpening + obstruction guard. Advances (does not close) the sole
residual of `conj:klein-bring-icosahedral-bridge` (merged PR #2928).
**Check:** [`scripts/keystone_eta_w_resolvent_probe.py`](../../scripts/keystone_eta_w_resolvent_probe.py) (parameter-free, exit 0).
**Keystone bean:** `s5bb`; ledger [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md).

## Where the bridge stands (merged)

`conj:klein-bring-icosahedral-bridge` (PR #2928) settled three layers, all
`lean`-direct verified (`leanok`):

1. **Group** — `⟨ζ₅ pentad, colour trefoil⟩ = A₅` (canonical alternating
   subgroup; EM involution is the odd coset).
2. **Orbifold** — `ℙ(V)/A₅ = S²(2,3,5)` (cone orders `(5,3,2)`, `χ_orb=1/30`)
   = the Poincaré-sphere Seifert base.
3. **Möbius realization** — Klein forms `f₁₂,H₂₀,T₃₀`, syzygy
   `T²+H³=1728f⁵`, quotient map `I=H³/1728f⁵`, pentad-anchored.

The **sole residual** is the *single-`ℙ(V)` realization*: the ζ₅ pentad acts on
the base ratio `z`, the colour trefoil acts on the spectral ratios `η`; Klein's
resolvent must identify them so both act as one icosahedral Möbius `A₅` on a
single `ℙ(V)`.

## The obstruction (a trap the resolvent must avoid)

The `so3-generators` realization of the order-3 trefoil is `α = ` rotation by
`2π/3` about `e₃` — the **same axis** as the pentad `S` (`w↦εw`, `2π/5` about
the Hopf polar axis `e₃`). Coaxial rotations commute, so

$$
  \langle\, \alpha(e_3),\ \text{pentad}(e_3)\,\rangle \;=\; C_{15}\ (\text{abelian})
  \quad\neq\quad A_5 .
$$

(Verified: order `15`, `αS = Sα`.) So the icosahedral 3-fold is **not** the
`so3` `α`-about-`e₃`. A naive "reuse the existing geometric 3-fold" assembly
fails for the same structural reason the EM 2-fold failed (dihedral, PR #2928):
the geometric generator is in the wrong position relative to the pentad axis.

## The target (what the resolvent must hit)

Placing the order-3 at the **icosahedral vertex→face angle** from `e₃`
(non-coaxial — concretely Klein's `ST`, order 3) and pairing it with the pentad
`S` **does** generate `A₅`:

$$
  \langle\, S,\ ST\,\rangle \;=\; A_5\ (\text{order } 60).
$$

(Verified in `PSL(2,\mathbb{C})`.) So the open step is precise: **Klein's
resolvent must transport the trefoil's spectral-`η` 3-fold onto the non-coaxial
icosahedral-angle axis** (the `ST` position), not the coaxial `e₃` axis the
`so3` holonomy `α` occupies. Concretely, the Lagrange-resolvent map
`η = η(z,w_k)` ([`rem:braid-group-action`](../../content/quantum-observable-universe/brings-surface/braid-group-action.md))
must intertwine the trefoil's `(η₁,η₂) ↦ (η₁, ζ^j η₂)` action with the Möbius
order-3 `ST` on the base `ℙ(V)`.

## Localization in the corpus's own resolvent coordinates (2026-06-28 follow-up)

The original obstruction (above) used abstract `so3` rotations. Re-deriving it
in the **corpus's** spectral ratios `η₁ = w₁/w₂`, `η₂ = w₃/w₄`
([`rem:braid-group-action`](../../content/quantum-observable-universe/brings-surface/braid-group-action.md))
pinpoints the obstruction more sharply
([`scripts/keystone_eta_w_resolvent_corpus_coords.py`](../../scripts/keystone_eta_w_resolvent_corpus_coords.py),
parameter-free, exit 0):

- The pentad `P` (the `ζ₅` 5-cycle `x_j↦x_{j+1}`, i.e. `w_k↦ζ₅^{-k}w_k`) acts
  on `(η₁,η₂)` as the **scalar** `ζ₅·I`.
- The trefoil `τ` acts as `diag(1, ω)`, `ω = e^{2πi/3}`.

Both are diagonal, so `⟨P, τ⟩ = C₁₅` (order 15, verified) — the same abelian
collapse as the `so3` probe, now intrinsic to the coordinates.

The decisive new fact: **a scalar pentad acts trivially on the projective
ratio `η₁/η₂`** (verified: `η₁/η₂` is fixed by `P`). So in these coordinates
the pentad's icosahedral order-5 rotation is *invisible* on any single `ℙ¹`.
The only generator that fails to commute with `P` is the off-diagonal
reflection `σ₂` `(η₁,η₂)↦(η₂⁻¹,η₁⁻¹)`, and it does so merely as an
**inversion** `σ₂Pσ₂ = P⁻¹` (dihedral) — it does *not* supply the missing
5-fold. By contrast Klein's genuine non-scalar order-5 Möbius `S` with the
2-fold `T` gives `⟨S,T⟩ = A₅` (order 60, verified projectively).

**Refined open step.** The resolvent must collapse the 2-torus `(η₁,η₂)` to a
single icosahedral parameter on which the *scalar* `ζ₅` becomes Klein's
*non-scalar* order-5 Möbius `S`; only then is `A₅` realized on one `ℙ(V)`.
This is a one-line, checkable requirement on the `η ↔ w` map — but
constructing the collapse remains the open G1 work.

## Status

This **sharpens** the residual to a single, well-posed differential-geometry /
resolvent identity — and guards against the coaxial trap (now localized to the
scalar-pentad degeneracy in corpus coordinates) — but does **not** close it;
constructing the `η ↔ w` intertwiner is the owner-authorized G1
(research-DG) step. Scope unchanged: this is the `V_λ`/geometry side; it does
**not** produce the Hecke-dual `W_λ`.
