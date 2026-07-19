# The Δ_λ "bar-odd sector re-check" is already closed by the proved ℓ¹-ceiling invariant — corpus-grep catch, no new probe warranted

**Date:** 2026-07-19 · **Branch:** `claude/agent-pickup-stalled-rtugin` ·
**Axis:** Δ_λ binding closure / Option-E · **Tier:** corpus-grep resolution of a
proposed "un-done" item · **Discipline:** no fit, no new ansatz, nothing wired,
no tier change.

## The proposed item

The PR #4064 c₃⟺q₀ synthesis flagged a "clean, cheap, un-done byproduct":

> the Δ_λ bar-involution search covered the **bar-even** sector, but the derived
> sign is **bar-odd** on conjugate pairs (n=3,6); re-run Option-E min-norm in
> the right (bar-odd) sector.

Per the corpus-grep discipline (AGENTS.md §Before declaring "open"), an item
proposed as un-done must be checked against the corpus before any probe is run.
It resolves in the corpus — the item is **already closed by a proved invariant**.

## Why it is already closed

The Δ_λ *sign* is not a search target — it is **proved exact**:
`Δ_λ = sgn(w_0^{S_{λ'}})·dim_λ = (−1)^{n(λ)}·dim_λ`
([`delta_lambda_sign_rule_proof.py`](../../computations/delta_lambda_sign_rule_proof.py),
2712 partitions through S₂₀, all match; Lean sorry-free `PartitionOf5.deltaSign_mixed`,
`S5SO3FiberAction.lean`, PR #2416). It is mixed-sign on conjugate pairs exactly as
the synthesis notes (n=3: 1+/2−; n=6: 6+/5−).

"Re-run min-norm in the bar-odd sector" is therefore a **sign/chirality-only
re-derivation**: keep `{y_λ, χ^λ}` and the magnitude `|Δ_λ| = dim_λ` fixed, vary
only the per-block sign `s_λ ∈ {±1}` (bar-even → bar-odd). This exact class is the
subject of a **proved scope-(b) structural exclusion**
([`delta_lambda_l1_ceiling_sign_prune.py`](../../computations/delta_lambda_l1_ceiling_sign_prune.py),
the magnitude-side analogue of the PROBE-4 KL-positivity prune):

> By the triangle inequality, for **every** sign assignment `{s_λ}`,
> `|Σ_λ s_λ (y_λ χ^λ dim_λ)| ≤ Σ_λ |y_λ χ^λ dim_λ| =: ‖c‖₁`.
> The measured ceiling `‖c‖₁ / |target|` is **0.358–0.592 < 1** for all of
> D / T / ³He / ⁴He (refreshed 2026-07-19, exit 0):
>
> | iso | net/tgt | ‖c‖₁/tgt |
> |-----|---------|----------|
> | D   | 0.171   | 0.516    |
> | T   | 0.225   | 0.358    |
> | ³He | 0.304   | 0.592    |
> | ⁴He | 0.107   | 0.406    |

So **no** sign- or chirality-only re-derivation — including any bar-odd-sector
min-norm that keeps `|Δ_λ| = dim_λ` — can reach the binding target; the ℓ¹
ceiling caps it at 36–59 %. The invariant cited (ℓ¹/triangle bound) is what
licenses the scope-(b) phrasing.

## What is actually open (and what running a probe would/wouldn't buy)

The ℓ¹ prune states the necessary condition explicitly: a **magnitude-adding**
ingredient is required — (i) a re-derived block magnitude `|Δ_λ| ≠ dim_λ`,
(ii) re-weighted `y_λ`, or (iii) an added term. A bar-odd-restricted min-norm
solve over *magnitudes* (reading (i), not sign-only) is not pruned — but solving
it against the AME binding energies **inverts the anchors**, which is a **fit**
by the Δ_λ-gate anti-laundering rule, informative only as a diagnostic and
**never** wireable to production as canonical. The per-atom magnitude deficit it
would report is already characterised by the multi-isotope residual probes
(`option_e_multi_isotope_delta_lambda_probe_v3.py`, "what would f need to
provide"). So no new probe is warranted here: the sign-sector reading is
proved-closed, and the magnitude reading reduces to the already-known
"magnitude-adding ingredient necessary" conclusion.

## Disposition

Item **closed** as already-resolved, not pursued as open. This is the
anti-rework / "OK to duplicate effort, not to re-declare a closed item open"
discipline (AGENTS.md) operating as intended: the synthesis's byproduct was
proposed in good faith across a context boundary, and the corpus check catches
that a proved invariant already answers it. The genuinely-open Δ_λ direction
remains the **magnitude** closure (Subgoal-2, owner-un-gated 2026-07-11/07-13),
pursued via derivation — not a sign-sector re-search and not an AME-inversion fit.
