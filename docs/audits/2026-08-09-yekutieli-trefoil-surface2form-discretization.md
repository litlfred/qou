# A canonical discretization of the Yekutieli surface 2-form on the trefoil Seifert surface (qou-prjo)

**Date:** 2026-08-09 · **Bean:** `qou-prjo` (deuteron transverse surface-curvature) / `qou-yczy`
(Yekutieli 2-form discretization) / `qou-dp32` (Ω₂ from Hecke commutators) · **Branch:**
`claude/z-c-k-f-map-keystone-ub5yix` · **Tier:** formalize-first (Lean sorry-free) + scope-(a)
validation. **Scope:** builds the named-absent object; deuteron number NOT closed.

## The wall this clears

Bean `qou-prjo`'s surviving object is the transverse non-abelian-Stokes surface-curvature
pairing `½P∮∮[F_q,F_q]` on the deuteron pn braid `σ₁³ = trefoil`, over the trefoil's genus-1
Seifert surface. Because `σ₁³` is a **single generator** (abelian), all path/Magnus corrections
vanish beyond order 1 (`TrefoilSurfaceStateSum.commutator_zero`, Lean), so the entire order-2
binding datum is this surface term. The stated wall: *"a canonical discretization of the
Yekutieli surface 2-form on the trefoil Seifert surface — data the corpus lacks."*

## What is built (Lean, sorry-free)

[`QOU/QBeta/YekutieliTrefoilDiscretization.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/YekutieliTrefoilDiscretization.lean),
`lean`-direct EXIT 0. The discretized (doubled, integral) surface 2-form on a genus-1 Seifert
surface with Seifert form `V` and handle holonomies `A : Fin 2 → R` (`Ring R`):

  `surface2Form V A = ∑_{i,j} V_{ij} · ⁅A_i, A_j⁆`.

| Theorem | Content |
|---|---|
| `surface2Form_eq_skew` | **only the skew (intersection) part of `V` survives**: `= (V₀₁ − V₁₀)·⁅A₀,A₁⁆` (self-linking `Vᵢᵢ` cancels because `⁅Aᵢ,Aᵢ⁆ = 0` and the bracket is antisymmetric) |
| `surface2Form_trefoil` | trefoil `V=[[-1,1],[0,-1]]` ⇒ `= ⁅A_a,A_b⁆` (unit intersection) |
| `surface2Form_trefoil_eq_germ_curvature` | `= (1+A₀)(1+A₁) − (1+A₁)(1+A₀)` — **exactly the corpus germ `F_q`** (`germ-commutator-q-curvature.lean`, `commutator_eq_curvature`). The discretized `½P∮∮[F_q,F_q]` on the trefoil is a **single germ q-curvature**. |
| `surface2Form_trefoil_eq_zero_iff` | `= 0 ⇔ ⁅A_a,A_b⁆ = 0` — the transverse bridge: abelian handles ⇒ 0; nonzero requires non-commutative handles |

**The structural payoff:** the discretization is **framing-independent** (self-linking drops)
and reduces to the non-abelian **intersection** of the two Seifert handles — one germ `F_q`. This
is the object `qou-prjo`/`qou-yczy`/`qou-dp32` all needed, now grounded in the corpus's own
sorry-free `F_q`.

## Validation (probe, 0-fit)

[`yekutieli_trefoil_surface2form_discretization_probe.py`](../../computations/deltalambda/yekutieli_trefoil_surface2form_discretization_probe.py)
(pure 2×2, 0 free params):

- **(A) abelian handles** (the deuteron's *own* trefoil in `H₂`, single generator `σ₁` ⇒
  commuting) → `surface2Form = 0` **exactly**, reproducing `commutator_zero`. The
  isolated-trefoil transverse term is **null** — the deuteron binding is not here.
- **(B) non-abelian germ** (reduced Burau of `B₃`, `σ₁,σ₂` non-commuting) → nonzero
  (`‖·‖ = 3.52`; magnitude convention-dependent — this toy has `O(1)` increments; the canonical
  small `q`-germ `δq ~ h` would scale as `h²`). `surface2Form_trefoil = ⁅A₀,A₁⁆` numerically
  confirmed (skew-only).

## Honest status — what clears, what remains

- **Cleared (wall #1):** the canonical Yekutieli-2-form discretization on the trefoil Seifert
  surface now **exists** as a sorry-free Lean object, grounded in the corpus `F_q`, with its
  defining structure (skew-only, single germ curvature) proved. This is the qou-prjo "missing
  data."
- **Sharpened (wall #2):** the discretization proves the deuteron's *isolated* `σ₁³` trefoil
  gives **exactly 0** (abelian handles). The nonzero transverse datum requires **non-abelian
  interface handle holonomies** (the "non-abelian `H₆` interface," absent from the corpus,
  `qou-jqof`/`qou-dp32`). The remaining gap is precisely *those handle holonomies*, not the
  discretization.
- **Not done:** the deuteron binding number. No fit; the reduced-Burau germ is a toy; `μ₃`/`c₃`/
  `g₂` never inverted; nothing wired; `free_parameters = 0`.

## Cross-references
- `F_q`: `quantum-observable-universes/germ-commutator-q-curvature.lean` (`commutator_eq_curvature`, `curvature_antisymm`)
- single-generator vanishing: `computations/deltalambda/TrefoilSurfaceStateSum.lean` (`commutator_zero`); `docs/audits/2026-07-24-eunit-magnus-order2.md` §2
- Yekutieli plaquette/strip layer: `QOU/MathlibExt/YekutieliIntegration.lean`
- τ-shadow abelian-collapse lesson: `docs/audits/2026-07-26-nastokes-curvature-yekutieli-coefficient.md` (`qou-tw5z`)
- remaining input (interface handles): beans `qou-jqof`, `qou-dp32`
