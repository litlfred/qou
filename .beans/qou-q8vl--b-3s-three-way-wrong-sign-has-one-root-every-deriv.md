---
# qou-q8vl
title: 'b_3''s three-way wrong sign has ONE root: every derived bond scalar is confined to (0,1), and uniform attraction does not escape it'
status: in-progress
type: task
priority: normal
created_at: 2026-09-12T12:28:23Z
updated_at: 2026-09-12T18:20:33Z
---

## Resolved as far as it goes: ONE root, and the stated escape is insufficient

Branch `claude/b3-sign-one-root-2026-09-12`, PR #7226.
Lean `QOU/MassTheory/B3SignOneRoot.lean` (13 decls, sorry-free, `lake build` exit 0).
Probe `computations/probes/b3_sign_one_root_probe.py` (10/10, exit 0, 60 dps).
Audit `docs/audits/2026-09-12-b3-sign-one-root-and-the-insufficient-escape.md`.

### The finding

The three wrong-sign routes (#7193 count channel, #7198 Ursell, #7200 dominant
summand) are ONE failure. Every production interface letter is `σ + d·1` with
`d ≤ 0` — `pp = (1,0)` bare σ, `nn = (1,−h)` which IS σ⁻¹ (`μ_nn = 1/(q(q²+1))`,
`|dev| 0.0` at 50 dps), `pn` colour-weighted between them — so every bond factor
is confined to `(0,1)`, and that decides the sign in all three settings.

### 🛑 The correction to the escape hatch

The Ursell audit §4 and the AGENTS.md extensive-term bullet say a positive term
"needs a bond factor above 1". **Necessary, not sufficient.** The production
`A=3` word is a CHAIN, so `φᵀ₃ = g₀₁·g₁₂` — a PRODUCT — whose sign is invariant
under flipping BOTH bonds. Measured: reflecting every live bond to attractive
leaves `b₃` byte-identical (`−0.293278112721` ³H, `−0.190468485549` ³He).
A two-bond chain needs **exactly one** bond above 1.

Also: the chain is covered by NEITHER standing theorem. `b3corpus_neg` needs all
three bonds strictly inside `(0,1)` and the absent bond sits at exactly 1;
`wMult_b3_nonpos` is the equal-bond case and the chain bonds differ by ~0.105.

### The required pattern is the two-nucleon spectrum

Exactly the two SIGN-MIXED assignments make both chains positive: `g_pn` opposite
to both like-pair bonds. Since `B = −α·log μ > 0` iff `μ < 1`, that is "unlike
pair binds, like pairs do not" — deuteron bound, diproton and dineutron unbound.
The live model binds all three, dineutron most. **`b₃ > 0` and the correct
two-body isospin structure are ONE condition.**

Both derived families excluded: production letters by `d ≤ 0`; isospin projectors
by an IDENTITY, `μ₊ + μ₋ = 1` (symbolic residual 0, any `z`, any `q`), so an
attractive channel forces its partner to `μ < 0` where the log is not real.

### Two claims of mine the probe refuted

* **"even powers attract, odd repel" is FALSE.** Measured `m = −2…+8`: `μ > 1` at
  `m = 2,4,5,6,7,8` — **+5 and +7 are odd**. A two-data-point extrapolation from
  `μ(σ²) > 1 > μ(σ³)`. Reproduces the corpus's stacked-bond table independently.
* **"a bond above 1 is the only escape" is FALSE.** `b3Agg_nonneg_of_convexOn`
  (`qou-82mc`) gives `b₃ ≥ 0` with every bond still inside `(0,1)`.

### Status: this bean stays OPEN, and `qou-brng` is untouched

σ² is NOT proposed — `qou-kj4v` records that the topological argument selecting it
runs backwards (binds the diproton, unbinds the deuteron), and adopting it because
it yields `b₃ > 0` is selection against the target. Magnitude is untouched. What
is open: a THIRD bond family that supplies the sign-mixed pattern by derivation,
and the convexity route, which is unanalysed here.
