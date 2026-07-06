# Bar-symmetric / antisymmetric decomposition of `B_pp` — the per-crossing-vs-per-block gap

**Date:** 2026-06-04
**Probe:** [`computations/probes/c2_bpp_variants_routes_abc.py`](../../computations/probes/c2_bpp_variants_routes_abc.py)
**Witness:** `route-abc-bpp-derivation.witness.json`
**Branch:** `claude/habiro-per-knot-lambda-derivation-2026-06-03` (PR #1765 follow-up to PR #1777)
**Status:** EXPLORATORY. **Reframes** the PR #1777 c=2 candidate chain.

## Prompt that drove this

User question 2026-06-04: *"why throw `Re`/`Im` away prematurely... maybe there is some interesting info"*

Sharp question. At real q₀, `Im(χ^λ(q₀)) = 0` algebraically (Hoefsmit characters live in `ℚ(q^{1/2})`, real at q > 0; `lusztig_q_0_imaginary_part_zero` invariant). So *literal* `Im(χ)` is just mpc roundoff noise at q₀. But **richer information IS being thrown away** — by the `|·|` step in `Σ_λ y_λ |Re χ^λ|`, which discards the bar-involution symmetric/antisymmetric structure.

## The bar-involution sym/anti decomposition

`def:coulomb-charge` decomposes the crossing energy as:

```
E_cross = ½(n₊+n₋)·(q + q⁻¹)    ← bar-symmetric (strong)
        +    Q     ·(q − q⁻¹)    ← bar-antisymmetric (Coulomb)
```

The **categorical analog at the partition-sum (block) level** is:

```
χ_sym(q)  := (χ(q) + χ(q⁻¹)) / 2     ← maps to STRONG piece structurally
χ_anti(q) := (χ(q) − χ(q⁻¹)) / 2     ← maps to COULOMB piece structurally

B_sym  := E₀ · Σ_λ y_λ_sym · (χ_sym_free  − χ_sym_atom)     ← block-strong
B_anti := E₀ · Σ_λ y_λ_sym · (χ_anti_free − χ_anti_atom)    ← block-Coulomb
```

This is the no-information-loss replacement for the source's `Σ_λ y_λ |Re χ^λ|`.

## Numerical result on the H_6 diproton at q₀ (50 dps, native MPFR)

| variant | value (MeV) | notes |
|---|---|---|
| **B_sym** (bar-symmetric → strong) | **1.0810** | true bar-symmetric strong piece |
| **B_anti** (bar-antisymmetric → Coulomb) | **0.9960** | direct block-Coulomb, no tanh multiplier needed |
| ratio `B_anti / B_sym` (block-level) | **0.9214** | |
| per-crossing `tanh(ln q₀) = (q−q⁻¹)/(q+q⁻¹)` | **0.1040** | |
| **mismatch factor** | **8.86 ×** | block ratio ≠ per-crossing ratio |
| source `B_pp = Σ y_λ \|Re χ\|` | 2.286 | sign-mixed `\|χ_sym + χ_anti\|`-style |

## The structural finding

**The per-crossing identity `Coulomb/strong = tanh(ln q₀)` from `def:coulomb-charge` does NOT carry through to per-block partition sums.** At the per-crossing (algebraic, q-rational) level the ratio is 0.10. At the per-block (Σ_λ y_λ-weighted summed) level the ratio is 0.92 — almost 9× larger.

So the source's formula

```
dHe = tanh(ln q₀) · B_pp
```

multiplies a *per-crossing* analytic factor by a *per-block* total — a **structural inconsistency**. The 3.21× residual factor in PR #1777's open slot is largely the accumulated translation between per-crossing and per-block levels — NOT primarily a "missing categorical multiplier" the c=2 selection rule could supply.

## What this means for the c=2 candidate chain

My prior PR #1777 comment proposed:

```
predicted_split = dHe · lw_c2(q₀) · (12/5)
                = 0.2377 · 1.337 · 2.4
                = 0.7625 MeV    vs AME 0.7638    →  −0.155 % off
```

The 0.155 % match was using the **source's chained-approximation value** of `dHe = 0.2377` (which is itself the per-crossing-times-per-block inconsistency). With the bar-symmetric/antisymmetric decomposition replacing the source's formula, **the chain's anchor shifts**:

- B_anti directly as Coulomb piece (no tanh factor): **0.996 MeV**, **+30.4 %** vs AME (not 0.155 %)
- B_anti · lw_c2(q₀) · (12/5) = 3.196 MeV (+318 % over AME — far)

So my 0.155 % match was a **coincidence of two approximation errors canceling** in the source formula, not a clean signature of a categorical chain that includes the c=2 selection rule.

## Honest reframing of the open question

The c=2 selection rule itself (PR #1765 main result) is unaffected — it's an exact symbolic identity at the link/Wedderburn level. What **is** affected is its proposed *application* to PR #1777's pp-Coulomb slot. The right derivation of the EM-linking invariant should:

1. Use the bar-symmetric/antisymmetric decomposition at the block level (B_anti directly, no per-crossing tanh translation), OR
2. Derive the per-block tanh-analog from a higher-rank categorical structure, OR
3. Reframe the diproton sub-link differently entirely.

The c=2 selection rule's natural slot in any such chain is still defensible — but it doesn't combine cleanly with the source's `tanh(ln q₀) · B_pp` formula, and the 0.155 % match was misleading.

## Open derivation routes (revised)

- **R1 — Replace `dHe`** with the direct `B_anti` (= 0.996 MeV) and re-derive what categorical scaling closes to AME 0.7638. Cleanest categorical foundation; doesn't have the per-crossing-vs-per-block flaw.
- **R2 — Derive the BLOCK-level Coulomb/strong ratio** as a separate q-rational from the partition-weighted sum (NOT the per-crossing tanh). Could be a closed form like `Σ y_λ_sym · χ_anti / Σ y_λ_sym · χ_sym` evaluated symbolically.
- **R3 — Reframe pp-Coulomb via the Hopf-link tr_M structure** (Route B from this probe): the Lean-proved closed form `tr_M(σ²) = 1 + (q−1)/√q` at H_2 is categorically cleaner than a per-block sum at H_6. The needed `m_e` scale identification stays open.

## Verdict

The user's question revealed a genuine structural gap in PR #1775's `dHe` formula — the per-crossing-vs-per-block translation is the deeper open derivation step. My c=2 chain matched an approximation artifact, not a clean signature. **PR #1777's open slot is now reframed:** the categorical question isn't "what multiplies tanh(ln q₀)·B_pp by 3.21×?" but "what's the correct per-block Coulomb/strong ratio that replaces tanh(ln q₀) at the block level?"

This is honest progress — it kills a false lead (the 0.155 % near-match) while opening a sharper question about the bar-involution structure at the block level.

## Q-usage discipline check

All sym/anti decomposition is **fibre-level** (`χ(q) ± χ(q⁻¹))/2` is a Laurent-polynomial-level construction over `R_q = ℤ[q, q⁻¹]`). At real q₀ both pieces are REAL (no |q|=1 step). `Im(χ(q₀)) = 0` invariant respected throughout. The "sym vs anti" terminology IS the categorical analog of "Re vs Im" but at the FIBRE level under the bar-involution `q ↔ q⁻¹`, not at the archimedean level.
