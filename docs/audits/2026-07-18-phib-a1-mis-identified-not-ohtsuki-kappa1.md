# Self-review correction: the merged Φ_b 2-loop A₁ is exact but MIS-IDENTIFIED — it is not the 4₁ Ohtsuki κ₁

**Date:** 2026-07-18 · **Branch:** `claude/phib-a1-kappa-correspondence-2026-07-17` ·
**Tier:** exact-arithmetic self-review correction · **Discipline:** scope-(a); re-scope not delete;
no `c_k` wired; L2 unchanged (2/7). **Corrects (in scope):** the merged #3854 / #3859.

## Why this note

No external reviewer remains (Gemini Code Assist sunset 2026-07-17), so the standing
red-team duty is ours. Chasing the A₁↔d_k question from #3859, I ran the sufficiency check
#3854 omitted — and it fails. This retires the "Φ_b 2-loop b-dictionary" line honestly.

## What #3854 did, and the gap

#3854 derived `A₁` = the 2-loop of the potential `V(z) = Li₂(z) − Li₂(1/z)` at the saddle
`z* = e^{iπ/3}`, gated on **G1** (Vol(4₁)), **G2** (torsion √3), **G3** (formula). Those
gates are **necessary but not sufficient** to identify the potential: the *true* 4₁ state
integral has the **same** Vol and the **same** torsion, yet its 2-loop invariant is the
known **Ohtsuki κ₁ = 11√3π/108** (corpus #3571/#3606, fit directly from the Kashaev
invariant `⟨4₁⟩_N`). #3854 never checked A₁ against κ₁.

## Findings (exact, 50+ dps — probe `qbeta_phib_a1_vs_ohtsuki_kappa1.py`)

1. **A₁ is exact and clean:** `A₁ = 1/3 + (17√3/108)·i` (both parts to `1e-48`). The #3854
   saddle computation is internally correct — the *number* stands.
2. **A₁ ≠ κ₁.** `κ₁ = 11√3π/108 = 0.5542165` is **real**; `A₁` is complex and π-free. Under
   the `ℏ = 2πi/N` dictionary the state-integral 2-loop maps to the 1/N coefficient,
   `A₁·2πi = −1.713 + 2.094i` — not the real κ₁; the best single-factor conversion misses by
   **63%**. No clean match exists.
3. **⇒ V = Li₂(z) − Li₂(1/z) is not the 4₁ state integral.** The Ohtsuki series, the
   perturbative Chern–Simons series, and the state-integral loop expansion are the **same**
   invariants; a correct 4₁ state integral's 2-loop **would** equal κ₁. Mine does not, so my
   potential — while matching Vol and torsion — **diverges at 2-loop**. It is a Vol+torsion
   reconstruction, not the physical integral.

## Correction (scope-(a); re-scope, do not delete)

The merged #3854 `A₁` is a **clean, correctly-computed** 2-loop of a Vol+torsion-matched
potential, **mis-identified** as "the 4₁ Φ_b 2-loop b-dictionary". The *number* is not
retracted (per the over-claim discipline: the numerical result stands, only the scope was
wrong); the **identification** is. The physical loop invariants / b-dictionary are the
corpus **κ-tower** (`κ₁ = 11√3π/108`, `κ₃ = (1081/21870)√3π³`, `κ₄ = (98/729)π⁴`) — already
derived, independently, from the Kashaev fit.

**This also resolves the A₁↔d_k question of #3859** (definitively, negatively): A₁ is not a
loop invariant of the *physical* 4₁ integral, so it is neither the prefactor normalization
nor a ladder coefficient of the right object. The κ-tower is that object. The "does the Φ_b
2-loop feed F1" line is therefore closed: the correct object (κ-tower) was already in hand,
and the odd-channel resummation's open piece remains what the merged F1 work found — more
D-ladder rungs, not a new normalization.

## Lesson (recorded)

Vol + torsion are two constraints; a state-integral potential has more content than that.
Matching a leading invariant and its 1-loop torsion does **not** identify the potential — the
2-loop (κ₁) is the discriminating check, and it must be run before claiming "the state
integral". The `Re A₁ = 1/3` cleanliness was seductive but not evidence of physical identity.

## Compute

- Probe: [`computations/qbeta/qbeta_phib_a1_vs_ohtsuki_kappa1.py`](../../computations/qbeta/qbeta_phib_a1_vs_ohtsuki_kappa1.py) (exit 0)
- Witness: `computations/qbeta/qbeta-phib-a1-vs-ohtsuki-kappa1.witness.json`

## Cross-references

- Corrected: [`2026-07-17-phib-2loop-bdictionary.md`](2026-07-17-phib-2loop-bdictionary.md) (#3854), [`2026-07-17-phib-2loop-deformed-gluing-f1-feed.md`](2026-07-17-phib-2loop-deformed-gluing-f1-feed.md) (#3859)
- Ohtsuki κ-tower (the physical object): [`2026-07-12-bar-odd-s-three-routes.md`](2026-07-12-bar-odd-s-three-routes.md)
- κ₁ producer: `computations/qbeta/qbeta_c3_kashaev_invariant_grounding.py`
