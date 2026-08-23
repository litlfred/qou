---
# qou-0h5k
title: 'SW-7 (=R2c): Wedderburn iso H_n(q) ≅ ⊕_{λ⊢n} M_{d_λ}(K)'
status: in-progress
type: task
priority: normal
created_at: 2026-08-02T19:33:07Z
updated_at: 2026-08-23T13:39:07Z
parent: qou-59vq
blocked_by:
    - qou-j377
    - qou-wtny
---

Assemble ⊕_λ ρ_λ : H_n(q) → ⊕_λ M_{d_λ}(K); injective (SW-5/6) + dim both sides = n! (SW-3) ⇒ AlgEquiv. This is the  field of HeckeWedderburnData.

## Refine (recon): Mathlib Wedderburn-Artin is EXISTENCE only (exists_algEquiv_pi_matrix_of_isAlgClosed) — block set/dims existential. Route to the partition-INDEXED iso: assemble ⊕_λ ρ_λ (SW-4) + injective (SW-5) + dim match Σd_λ²=n! (SW-3) ⇒ AlgEquiv directly, rather than extracting from the existential form. Does NOT need Jacobson density (SW-9).

## ⏩ Spanning half of dim H_3(q)=6 PROVED (2026-08-10) — sorry-free

[`QOU/SchurWeyl/HeckeDim3.lean`](https://github.com/litlfred/qou/blob/claude/schur-weyl-sw5-irreducibility-2026-08-10/content/quantum-observable-universe/lean/QOU/SchurWeyl/HeckeDim3.lean):
`span_sixWords_eq_top` — the six words `{1,σ₀,σ₁,σ₀σ₁,σ₁σ₀,σ₀σ₁σ₀}` span
H_3(q) = Hecke K q qi 2, i.e. **dim_K H_3(q) ≤ 6**. Generic [CommRing K].
Proof: `adjoin{σ₀,σ₁}=⊤` (mk surjective + FreeAlgebra.induction) + closure
span = adjoin (`Algebra.adjoin_eq_span`) + closure_induction_left with the 12
explicit quadratic/braid left-mult reductions. Axiom-clean; wired into QOU.lean;
lean-direct exit 0. On PR #4942.

**Remaining for full SW-7 (Wedderburn iso / dim=6):** the matching lower bound
`dim ≥ 6` (the six words linearly INDEPENDENT), via ρ=(triv,sign,seminormalRep21):
either the 6×6 independence of ρ(sixWords) in ℝ×ℝ×M₂, or ρ surjective (then
dim≥6 from spanning ⇒ dim=6 ⇒ ρ iso = R2-inst). That is the next increment.

## Independence (dim ≥ 6) — reductions VERIFIED, messy 4×4 tail remains (2026-08-10)

WIP saved (compiles, one Ref'd GAP sorry): scratchpad `HeckeDim3Indep.WIP.lean`.
Route: specialize K=ℝ, qi=q⁻¹; apply the three reps to a linear relation
Σcᵢwᵢ=0 and read off 6 equations (et=triv, es=sign, m00/m01/m10/m11=seminormal
M₂ entries). **VERIFIED sorry-free reductions:**
- `hqi := mul_inv_cancel₀ hq` (q·q⁻¹=1); `hqi_ne : q+q⁻¹≠0`; `hK : K≠0` (K=(q⁴+q²+1)/(q²+1)²).
- `hD : c₃ - c₄q⁻¹ + c₅q - c₆ = 0` — from `m10 = K·(…)`, factor K≠0.
  (`linear_combination m10 + c₆*K*hqi` — the c₆ term needs the q·q⁻¹=1 correction.)
- `hC : c₃ + c₄q - c₅q⁻¹ - c₆ = 0` — `linear_combination m01 + c₆*hqi`.
- `h45 : c₄ = c₅` — from `hC - hD = (c₄-c₅)(q+q⁻¹)=0`, q+q⁻¹≠0.
- `h36 : c₃ = c₆ - c₄(q-q⁻¹)` — `linear_combination hC - q⁻¹*h45`.

**Remaining (the GAP):** close `c₁=c₂=c₄=c₆=0` (then c₃=c₅=0 via h45,h36) from the
2 DIAGONAL seminormal entries `m00` (coeff c00=-1/(q³+q)) and `m11` (coeff
c11=q³/(q²+1)) together with `et`, `es`. After substituting c₅=c₄ and
c₃=c₆-c₄(q-q⁻¹), this is a 4×4 in (c₁,c₂,c₄,c₆); clear denominators
(×(q³+q), ×(q²+1)) to a polynomial identity in q and finish with
`linear_combination`/`nlinarith`. The coefficients are the only thing left to
compute. This closure gives dim H_3(q)=6 AND, since the 3 reps then biject,
the SW-7 Wedderburn iso H_3(q)≅ℝ×ℝ×M₂ = R2-inst at n=3.

## ✅ dim H_3(q) = 6 — BOTH BOUNDS PROVEN (2026-08-10)
- dim ≤ 6: HeckeDim3.span_sixWords_eq_top (sorry-free).
- dim ≥ 6: HeckeDim3Indep.sixWords_indep (sorry-free, qou-pymd closed).
Next for the SW-7 Wedderburn ISO (R2-inst at n=3): assemble the six words into a
Basis (finrank=6) and package ρ=(triv,sign,seminormalRep21) as the iso H_3(q)≅ℝ×ℝ×M₂.
The hard dimension theorem is done; remaining is finrank/Basis + iso plumbing.


## Measured 2026-08-19 — n = 3 only; the general assembly is gated on SW-3 + SW-5

Landed and sorry-free on main: `HeckeDim3Dim` (finrank H_3(q) = 6),
`HeckeWedderburn3.rho_bijective` -> H_3(q) ~= R x R x M_2(R), `HeckeWedderburnData3`.
General n has the SPANNING half only: `HeckeCoset.finrank_le_factorial`
(dim <= (n+1)!, generic CommRing, sorry-free — qou-uoal).

The missing half is the lower bound, and it has exactly two routes:
- **rep-theoretic**: rho_lambda jointly injective (SW-5 `qou-jfr8`) + sum d_lambda^2 = n!
  (SW-3 `qou-wtny`) => dim >= n!. Both open; SW-5 just became reachable via Ram 4.1.
- **GS normal forms**: `qou-auq3` (sibling, ACTIVELY OWNED — do not duplicate),
  proving `hecke_is_gs_basis` gives normal forms and the basis directly.

So SW-7-general is downstream of one of those two landing, not independently
attackable right now.


## TAKEOVER 2026-08-23T13:35Z (owner-authorised, > 4h staleness rule)

Last commit anywhere in the SchurWeyl area: `ace79127c` at 2026-08-22 19:24 UTC
— **18.2 hours** before takeover, against the owner's 4-hour threshold. No open
PR and no branch updated today carries SW-7 scope. Continuing from `main`
(`9f11db11d`); no sibling branch touched.

## Why SW-7 is NOW assemblable — both blockers cleared while I was away

- **SW-3 landed**: `QOU.Mathlib.rskBurnsideHolds n` for EVERY n (e877f7755 /
  1b5f4751c), not just n <= 12. `Sum d_lambda^2 = n!` is available.
- **SW-5 landed**: `seminormalRep_range_eq_top` (each block SURJECTIVE) and
  `seminormalRep_not_matRepEquiv_of_ne` (pairwise inequivalent, UNCONDITIONAL).

## The route — and note it is NOT the classical file's route

`SpechtWedderburnGeneral` (q=1, sorry-free) goes **injectivity + equal finrank**.
That does not transfer: on the q-side we have `finrank H_n(q) <= n!`
(`HeckeCoset.finrank_le_factorial`) but NOT the lower bound — that is the open
GS-basis item `qou-auq3`. Injective + `dim source <= dim target` proves nothing.

**Go through SURJECTIVITY instead**, which is what the q-side actually has:

1. Product map Phi = (+)_lambda rho_lambda : H_n(q) -> Prod_lambda M_{d_lambda}(R).
2. Each block surjective (SW-5) + blocks separated by central scalars (SW-5's
   inequivalence machinery) => **Phi surjective**. THIS IS THE MISSING STEP.
3. Surjective + `finrank H_n <= n!` + `finrank target = Sum d_lambda^2 = n!`
   => bijective.
4. **Corollary worth naming: `finrank H_n(q) = n!`** — the Iwahori-Hecke basis
   theorem's LOWER bound, obtained without the GS route. If this lands it
   partially obviates `qou-auq3`'s motivation (not its content).

## Step 2's crux, and why it needs no Jacobson density

Mathlib has no density / bicommutant, and none is needed. Let A = range Phi.
- The central elements give A a family of block-scalar tuples that SEPARATE the
  partitions. Lagrange interpolation over a finite index set (the same argument
  as `DiagonalSeparation.single_self_mem_of_separating`, which I proved for the
  single-block case) puts every **block idempotent** `Pi.single lambda 1` in A.
- Then for any target x, `x = sum_lambda (Pi.single lambda 1) * a_lambda` where
  `a_lambda` is any preimage of `x_lambda` in block lambda. Each summand is in A.
So A = top, elementarily.

Implementation order: (i) the abstract Pi-algebra lemma (no Hecke content, so it
checks on its own terms); (ii) instantiate with the seminormal blocks; (iii) the
finrank count; (iv) `HeckeWedderburnData` instance
(`QSchurWeyl.lean:62`, the n=3 case is `HeckeWedderburnData3`).
