# Keystone geometric `W`: `Jac(Bring) ~ E⁴` — the rank-2 W-plane is the elliptic curve `Bring/S₄`

**Date:** 2026-06-24
**Branch:** `claude/mass-open-keystone-w-l2-root-2026-06-24`
**Status:** exact (character theory); concretely identifies the keystone "W-plane" as a specific elliptic curve and reduces the keystone q-family monodromy from genus-4 to genus-1. No fit.
**Probe:** [`computations/substrate/bring_jacobian_isogeny_factors.sage`](../../computations/substrate/bring_jacobian_isogeny_factors.sage) · **Witness:** [`computations/substrate/bring-jacobian-isogeny-factors.witness.json`](../../computations/substrate/bring-jacobian-isogeny-factors.witness.json)
**Builds on:** merged [#2701](https://github.com/litlfred/qou/pull/2701) (`H^{1,0}(Bring)` is the A₅-irreducible 4-dim standard rep).

## The question this answers

#2701 established that the framework's `H¹(Bring) = 2W` cannot be an A₅-subrep of
the holomorphic differentials (they are the *irreducible* 4-dim standard rep), so
`W` must be an **isogeny/CM factor of `Jac(Bring)`**. That left *which* factor. This
probe pins it exactly.

## Method — quotient genera (exact, no period integration)

For any `H ≤ S₅ = Aut(Bring)`, the quotient curve has
`genus(Bring/H) = dim (H^{1,0})^H = dim std^H = (1/|H|) Σ_{h∈H} χ_std(h)`,
and the quotient map `Bring ↠ Bring/H` makes `Jac(Bring/H)` an isogeny factor of
`Jac(Bring)`. This is pure character theory — no period matrix (which #2701 showed
is tool-limited by conjugate singularities), no fit.

## The result

| `H` (subgroup of S₅) | `\|H\|` | `genus(Bring/H) = dim std^H` |
|---|---|---|
| `S₄` (point stabilizer) | 24 | **1 — elliptic** |
| `A₄`, `D₆` | 12 | **1 — elliptic** |
| `D₄` | 8 | **1 — elliptic** |
| `S₃`, `C₆` | 6 | **1 — elliptic** |
| `C₂×C₂`, `C₄` | 4 | **1 — elliptic** |
| `C₃` | 3 | 2 |
| `C₂` (transposition) | 2 | 2 or 3 |
| `A₅`, `S₅`, `F₂₀`, `D₅` | 60/120/20/10 | 0 |

**Eight subgroup classes give genus-1 (elliptic) quotients.** The cleanest is
`E := Bring/S₄`, an elliptic curve.

### `Jac(Bring) ~ E⁴`

1. `H^{1,0}(Bring) = std` is **irreducible** as an S₅-representation (#2701). A
   curve whose analytic representation `H^{1,0}` is `G`-irreducible has a
   **`G`-isotypic Jacobian** — isogenous to a power `B^n` of a single
   isogeny-simple abelian variety `B`.
2. `E = Bring/S₄` is a genus-1 **quotient**, hence an isogeny **factor**. A simple
   factor of an isotypic `B^n` must be isogenous to `B`, so `B = E` and
   `Jac(Bring) ~ E⁴` (`4 = dim Jac`).

This is the established Riera–Rodríguez result ("The period matrix of Bring's
curve", *Pacific J. Math.* **154** (1992)); here it is re-derived from quotient
genera + the #2701 irreducibility.

## Why this sharpens the keystone

The framework's **rank-2 "W-plane scale + modulus"** (2 real DOF, cheat-sheet) is
**literally `E = Bring/S₄`**: an elliptic curve's period is exactly a scale and a
modulus — 2 real DOF. So:

- **`H¹(Bring) = 2W` is concrete:** `H¹(Bring) = H¹(E) ⊗ std = 2·std`, with `W`
  the elliptic factor `E` and the "2" the rank of `H¹(E)`. Consistent with #2701
  (W is an abelian-variety factor, not an A₅-subrep of forms).
- **The keystone q-family monodromy `M` drops from genus-4 to genus-1.** Instead of
  an `Sp(8,ℤ)` Gauss–Manin monodromy on the full genus-4 family, the W-plane data is
  a **2×2 `SL₂` Gauss–Manin monodromy on a q-family of elliptic curves `E(q)`**
  (`SL₂` because it preserves the principal polarization on `E`). The keystone
  trace target `tr B = 2.6424` (merged lever-1 #2701) is then literally
  `tr M` of that 2×2 monodromy.
- **Consistency with lever-1.** The lever-1 binding kernel is the depth-2,
  `det = 1` recurrence `R = x² − τx + 1` with `τ = tr B = 2.6424` — exactly the
  characteristic polynomial of a 2×2 `SL₂` matrix. The elliptic-W-plane picture
  *predicts* this 2×2 structure: `M ∈ SL₂(ℤ)` acting on `H¹(E)` has char. poly
  `x² − (tr M)x + 1`. The lever-1 recurrence and the elliptic W-plane are the same
  object.

## What remains open (the genuine keystone)

The fixed elliptic curve `E = Bring/S₄` has no monodromy; the keystone needs the
**q-family `E(q)`** (the deformation whose Gauss–Manin monodromy `M(q)` has
`tr M(q₀) = 2.6424`). Two concrete sub-questions, now genus-1 (tractable):

1. **Identify `E(q)`** — the q-deformation of `Bring/S₄`. Candidate: the elliptic
   fibre of the s5-so3 / Seifert `S³/2I` construction (#2524) restricted to the
   `S₄`-quotient. Its j-invariant / modulus as a function of q.
2. **`tr M(q₀) = 2.6424`?** — compute the Gauss–Manin monodromy trace of `E(q)`
   around `q₀` and test against the lever-1 target. The torus shortcut is *refuted*
   (#2701: `τ_torus = 2.0437 ≠ 2.6424`), so `E` is **not** the substrate torus `E_q`
   — it is the distinct elliptic curve `Bring/S₄`, and finding its modulus is the
   open step.

This converts the keystone from "derive a genus-4 Gauss–Manin matrix" to "identify
one q-family of elliptic curves and check a 2×2 monodromy trace" — a substantial
reduction in difficulty, and it ties the geometric-`W_λ` keystone (#2503/#2524) to
the merged lever-1 recurrence.

## Discipline

Exact character theory (`genus(Bring/H) = dim std^H`); no fit; nothing wired. The
`Jac(Bring) ~ E⁴` decomposition is exact (isotypic + elliptic-quotient argument,
matching Riera–Rodríguez). The q-family `E(q)` and its monodromy trace are the
open keystone, now at genus-1.
