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

## Status

This **sharpens** the residual to a single, well-posed differential-geometry /
resolvent identity — and guards against the coaxial trap — but does **not**
close it; constructing the `η ↔ w` intertwiner is the owner-authorized G1
(research-DG) step. Scope unchanged: this is the `V_λ`/geometry side; it does
**not** produce the Hecke-dual `W_λ`.
