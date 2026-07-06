# U(1) / SU(2) / SO(3) symmetry-loss audit (2026-06-04)

**Question (owner).** In the M = Vol × Density mass/binding chain, where have
the U(1), SU(2), and SO(3) symmetries been *lost* — collapsed to a scalar,
projected to an abelian shadow, or stubbed out? Which losses are legitimate
(archimedean projection) vs lossy shortcuts/stubs to be restored?

**Verdict (one line).** U(1) loss is **legitimate** (the τ-functor forces a
real observable); SU(2) is **collapsed by a lossy shortcut** (the global
H₄ scalar `linking_weight` replaces the per-knot per-block Markov trace —
verified ~2.38× discrepancy); SO(3) is an **unimplemented stub**
(`chirality_sign = 0`; the S₅↔SO(3) fibre action is conjectural).

## Verdict table

| Symmetry | Lives in | Lost where (file:line) | Loss type | Verdict |
|---|---|---|---|---|
| **U(1)** (writhe/framing phase `q^{w·c}`, Im(q) at the \|q\|=1 fibre) | categorical/fibre, pre-τ | `\|·\|` / `Re[·]` at the archimedean projection: `vhat_tower_im_cancellation.py:22-26`, `paper_modulus_audit_nonarchimedean.py:50-56`; constraint `lusztig_q_0_imaginary_part_zero` (`four_unwired_theorems_regression.py:119`, Im(q₀)=0 to 1e-40) | archimedean projection | ✅ **LEGITIMATE** — the MeV observable must be real (`def:archimedean-realization-functor`); Im(q) is preserved at the fibre level. Only a notation cleanup (some `\|·\|` in non-archimedean sections should be signed) remains. |
| **SU(2)_q** (per-block Wedderburn tower `Σ_λ y_λ χ^λ`; the q-characters `[n]_q = sinh(nη)/sinh η`) | the **Density** ρ(q) of M=Vol×Density | production uses the **global H₄ scalar** `linking_weight_family_a = (3q²+4+3q⁻²)/4` (`_li_2_q_util.py:172-197`) instead of the per-knot per-block `tr_M`; the discipline gate is **RED** (`vol_density_per_block_wiring.py:103-190`) | numerical shortcut | ❌ **LOSSY** — **verified 2026-06-04**: global `linking_weight(q₀)` = **2.5328** vs per-block `tr_M(proton)` = **1.0653**, ratio **2.378×**. The global scalar discards the per-block SU(2) selectivity. **Primary restoration target.** |
| **SO(3)** (spin ℤ₂ double-cover of SU(2); S₅↔SO(3) fibre; chirality/CPT) | should set the inter-nucleon color-pair weighting + spin structure | `chirality_sign (_p) : Int := 0` stub (`brings-surface/inter-nucleon-channel-color-tube.lean:74-82`); the `S5SO3Fiber`/`InterNucleonChannelColorTube` class is `sorry`/conjectural (`…color-tube.md:39,127-143`); `s5_so3_su2_u1_fiber_action.py:172-196` partially maps it | unimplemented stub | ❌ **BLOCKED** — empirically load-bearing (per-sheet scheme → Δm_{n-p} to 0.14% vs uniform 305 ppm), but awaits the conjectural fibre action. Long-term frontier, NOT a quick fix. |

## The hyperbolic bridge (why SU(2) and U(1) are the same η)

With `q = e^η` (η = log q): `h = q−q⁻¹ = 2 sinh η` (U(1) odd) and
`[2]_q = q+q⁻¹ = 2 cosh η = 2.0109` (U(1) even) **are the j=½ SU(2)_q Weyl
character** `[2j+1]_q = sinh((2j+1)η)/sinh η`. So the cosh/sinh (U(1)
flavour rapidity, the p-n / mirror-binding split) and the SU(2) character
tower share one rapidity; the U(1) split is the abelian/Cartan shadow of
SU(2). Formalised in `QOU/Mass/MassVolDensity.lean` §3 (parity) + §5
(`su2_fundamental_eq_two_cosh`). SO(3) sits one level up (SU(2)/ℤ₂); its
ℤ₂ (spin) is **not** the S₅/A₅ sign ℤ₂ (`s5_so3_su2_u1_fiber_action.py:172-196`).

## Recommendations (by tractability)

1. **SU(2) — RESTORE (primary, medium-risk).** Phase production from the
   global `linking_weight_family_a(q)` to the per-knot per-block density
   `vol_density_per_block(vol_K, tr_M_K, q)`. The discipline gate is currently
   RED (2.38× global-vs-per-block); this is the open per-block-vs-global
   question, *not* a silent swap — first expose both side-by-side in the
   M=Vol×Density compute (`mass_vol_density.py`), then resolve which is
   canonical (the paper's per-block Σ_λ is the authoritative form; the
   global scalar was the exploratory shortcut). Coupled to the per-knot-Vol
   question (#1762/#1816) and the VolDensity purge (Stage 2).
2. **U(1) — documentational only (low-risk).** Reconcile `|·|` notation in
   non-archimedean sections per `paper_modulus_audit_nonarchimedean.py`.
   The physics is sound (legitimate τ-projection).
3. **SO(3) — research frontier (high-effort).** Formalise the S₅↔SO(3)
   fibre action → derive `chirality_sign` / the color-pair weight matrix.
   Empirically expected to improve Δm_{n-p} ~3×, but conditional on the
   `conj:s5-so3-fiber-action` class. Sharpen on paper first.

## Key files
- `computations/_li_2_q_util.py:172-197` — global linking_weight (SU(2) collapse site)
- `computations/vol_density_per_block_wiring.py` — RED discipline gate (per-block ≠ global)
- `computations/s5_so3_su2_u1_fiber_action.py` — the U(1)/SU(2)/SO(3)/S₅ fibre map
- `content/quantum-observable-universe/brings-surface/inter-nucleon-channel-color-tube.{md,lean}` — SO(3) stub (`chirality_sign=0`)
- `content/quantum-observable-universe/lean/QOU/Mass/MassVolDensity.lean` §3/§5 — the U(1)↔SU(2) hyperbolic bridge (this session)
- `computations/vhat_tower_im_cancellation.py`, `four_unwired_theorems_regression.py:119` — U(1) Im(q)=0 archimedean projection (legitimate)
