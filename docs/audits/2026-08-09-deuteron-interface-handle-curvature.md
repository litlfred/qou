# The deuteron pn-interface handle holonomies, computed — the qou-prjo "absent" object grounded

**Date:** 2026-08-09 · **Bean:** `qou-prjo` / `qou-jqof` (non-abelian H₆ interface amplitude) /
`qou-dp32` (Ω₂ from Hecke commutators) · **Branch:** `claude/z-c-k-f-map-keystone-ub5yix` ·
**Tier:** compute (real H₆ Hoefsmit rep) + structural. **Scope:** the interface curvature is
computed; the deuteron MeV binding is NOT closed.

## What was missing, and what is now computed

The Yekutieli surface term `surface2Form(V_trefoil, [A_a,A_b]) = ⁅A_a,A_b⁆`
([`YekutieliTrefoilDiscretization.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/YekutieliTrefoilDiscretization.lean))
needed its two non-abelian handle holonomies `A_a, A_b` — the "non-abelian H₆ interface, absent
from the corpus" (`qou-jqof`). Grounded in the corpus deuteron H₆ word (survey 2026-08-09):

  proton block `{σ₀,σ₁}` · **interface `σ₂ = σ − h(½−δ/4)·I`** · neutron block `{σ₃,σ₄}`.

Proton `{σ₀,σ₁}` and neutron `{σ₃,σ₄}` **far-commute** (`|i−j|≥2`), so the *only* non-abelian
content is `σ₂` against its neighbours. The unique non-abelian handle pair is the
interface-straddling adjacent pair `A_a = ρ_λ(σ₂)`, `A_b = ρ_λ(σ₃)`. Because the
`bring_color_weighted` dressing `−h(½−δ/4)·I` is **central**, it drops out of the commutator
(`surface2Form_trefoil_dressing_invariant`, Lean) — the datum is δ-independent.

[`deuteron_interface_handle_curvature_probe.py`](../../computations/deltalambda/deuteron_interface_handle_curvature_probe.py)
(0-fit) computes `F_q = [σ₂,σ₃]` in the real H₆ Hoefsmit seminormal rep at q₀, all `λ⊢6`:

| finding | result |
|---|---|
| `F_q` nonzero, **exactly traceless** (`tr = 0`, all λ) | ⇒ enters binding in **quadrature** `‖F_q‖²`, never linearly (matches the A=3 Pythagorean bridge `s²`) |
| proton–neutron far-commute `[σ₀,σ₃]=0` (all λ) | only `σ₂` carries the non-abelian datum |
| color-**singlets** `(6),(1⁶)` → `F_q = 0` | no interface curvature in a singlet channel |
| bar-symmetry: conjugate pairs `λ↔λ'` have equal `‖F_q‖²` | `(5,1)&(2,1⁴)=6.09`; `(3,2,1)` self-conj `=36.52` |
| genuine q-**curvature** `dF_q = F_q(q) − F_q(1)` (F_q survives at q=1 as classical S₆ braiding) | `‖dF_q‖² ≈ 1.77·h⁴` ⇒ `dF_q ~ h²` — the **order-2 surface term** the bean predicted |

Wedderburn-weighted totals at q₀: `Σ y_λ ‖F_q‖² ≈ 1761` (raw), `Σ y_λ ‖dF_q‖² ≈ 0.175`
(q-deformation, the physical O(h²) piece).

## Honest status — what clears, what remains

- **Cleared:** the interface handle holonomies and their germ curvature `F_q` — the
  `qou-jqof`/`qou-dp32` "absent" object — are now **computed** in the real corpus H₆ rep, fed
  into the Lean `surface2Form`, and characterized (traceless, far-commutativity, singlet-null,
  bar-symmetric, `dF_q ~ h²`).
- **Confirms the bridge:** `F_q` traceless ⇒ the transverse datum contributes in **quadrature**,
  precisely the `s²` leg of the A=3 Pythagorean bridge (`A3BranchingModulusReflection`). The two
  legs of the magnitude program (A=3 amplitude, deuteron binding) share this structure.
- **Not done:** the deuteron **MeV binding**. The raw Markov trace `tr(F_q)=0`, so the binding is
  the quadrature/pairing `tr_M(ρ_deuteron·dF_q)` + the canonical λ-weighting — a further step with
  modelling choices, deliberately **not** taken here (it is where a fit could creep in). No fit;
  `μ₃`/`c₃`/`B(D)` never inverted; nothing wired; `free_parameters = 0`.

## Cross-references
- discretization + dressing-invariance: `YekutieliTrefoilDiscretization.lean`, `2026-08-09-yekutieli-trefoil-surface2form-discretization.md`
- germ `F_q`: `germ-commutator-q-curvature.lean` (`commutator_eq_curvature`)
- interface operator: `mass_at_3A_proper.py` (`atom_braid_word_3A`), `bring_color_weighted`; Hoefsmit builder: `computations/hecke/hecke_characters.py` (`build_seminormal_matrices`)
- Pythagorean quadrature: `A3BranchingModulusReflection.lean`, `BirkhoffBarOddPythagorasBridge.lean`
- remaining pairing: beans `qou-jqof`, `qou-dp32`
