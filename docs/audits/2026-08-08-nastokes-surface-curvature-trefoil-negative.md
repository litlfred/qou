# Transverse NA-Stokes surface-curvature pairing — the named discretization, BUILT; it does not close the deuteron g₂ (scope-a negative)

**Date:** 2026-08-08 · **Bean:** `qou-prjo` · **Epic:** `qou-r2nh` (Δ_λ magnitude) ·
**Tier:** builds the named-wall discretization + scope-(a) numerical negative.
**No fit, no AME inversion, nothing wired.**

## The task

`qou-prjo` named the surviving deuteron-magnitude candidate: the **transverse NA-Stokes
surface-curvature pairing** `½𝒫∮∮[𝓕,𝓕]` on the trefoil (σ₁³ = pn) Seifert surface — the
only order-2 term that survives the single-generator word (the inter-crossing Magnus tower
is proved 0 for σ₁³, `2026-07-24-eunit-magnus-order2.md §2`). The **wall** was: *"needs a
canonical discretization of the Yekutieli surface 2-form on the trefoil Seifert surface —
data the corpus lacks."* Target: derive the bar-even gap coefficient `g₂ = 1.0087` (which
would close the deuteron to −0.036%), i.e. a term of size `g₂·h²` ⇒ `c₂ := ‖Ω₂^⊥‖/h² ≈ 1`.

## The discretization, built

`computations/probes/nastokes_surface_curvature_trefoil_probe.py`:
- **Trefoil Seifert data (genus 1):** Seifert matrix `V=[[-1,1],[0,-1]]`, intersection form
  `J = V−Vᵀ = [[0,1],[-1,0]]` (`a·b=1`).
- **Germ q-curvature** `F_q=[δq₁,δq₂]` in the 2-dim Hecke rep, tested two principled ways:
  the log germ `[log σ₁, log σ₂]` (O(1)) and the **q-derivative germ** `[q ∂_q s₁·s₁⁻¹, …]`
  (O(h), the true germ-level q-increment of `germ-commutator-q-curvature.md`).
- **NA-Stokes conjugation + genus-1 collapse:** `½∮∮[𝓕,𝓕] = J_{ab}[𝓕_a,𝓕_b]`,
  `𝓕_k = U_k⁻¹ F_q U_k`, over the natural handle-holonomy choices.

## Result — c₂ is choice-dependent from 0 to 897×, never ≈ 1

| germ | handles | ‖Ω₂^⊥‖ | c₂ = ‖·‖/h² |
|---|---|---|---|
| log | s₁,s₁² | 12.87 | 294.6 |
| log | s₁,s₂ | 26.96 | 616.9 |
| log | s₂,s₁s₂ | 10.99 | 251.5 |
| q-deriv | s₁,s₁² | 2.6e-53 | **0** |
| q-deriv | s₁,s₂ | 39.19 | 896.7 |
| q-deriv | s₂,s₁s₂ | 0 | **0** |

Two structural facts: (1) the transverse term is genuinely **nonzero** on the
single-generator σ₁³ channel for off-axis handle pairs (confirming it is the surviving
candidate — it does not vanish by `[X,X]=0` like the inter-crossing tower); (2) but its
magnitude is **not canonically fixed** — with the O(h) q-derivative germ and on-axis
handles it **vanishes** (the germ commutes with the along-word holonomy), and with mixed
handles or the log germ it is **250–900×** the target. **No natural discretization lands
near `c₂ ≈ 1`.**

## Verdict (scope-a)

The named wall's "missing data" — the surface discretization — is now **built**, and the
answer is a **negative**: the transverse NA-Stokes surface-curvature pairing does **not**
supply `g₂`. The surface→scalar map carries **O(100×) gauge freedom** (germ choice: log vs
q-derivative; handle-cycle choice) that the corpus does not fix, and the natural choices
give either 0 or 250–900×, bracketing but never hitting the required unit coefficient. So
the surviving candidate, once actually computed, **joins the walled routes** — the deuteron
`g₂` (and hence the Δ_λ binding magnitude) stays open, and the na-Stokes surface-curvature
route is no longer "promising pending data" but "built and under-determined."

**Honest scope:** this is scope-(a) — a negative on the *natural* discretizations tested
(log / q-derivative germ × three handle pairs). It does not prove *no* discretization can
give `c₂=1`; it shows the corpus provides no canonical choice that does, and the freedom is
O(100×). To revive the route one would need an *independent* principle fixing (i) the germ
normalization and (ii) the two H₁ handle holonomies — absent that, `g₂` is not derivable
here. `g₂` remains NEAR-MATCH, underived (unchanged).

## References
- `computations/probes/nastokes_surface_curvature_trefoil_probe.py` (this PR)
- `.beans/qou-prjo…` (the named wall)
- `docs/audits/2026-07-24-eunit-magnus-order2.md` (§2 the σ₁³ vanishing; §3 the g₂=1.0087 gap)
- `content/quantum-observable-universe/quantum-observable-universes/germ-commutator-q-curvature.md`
