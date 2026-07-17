# Colour `𝔰𝔲(3) ⊂ 𝔤₂ = Der(𝕆)`: the stabilizer of a unit imaginary octonion has dim 8 (`S⁶ = G₂/SU(3)`)

**Date:** 2026-07-17
**Branch:** `claude/octonion-su3-stabilizer-2026-07-17`
**Scope:** exact-arithmetic result; cross-checks the landed `dim Der(𝕆)=14`; realises the colour-`SU(3)` piece the octonion-recovery audit flagged as present-but-unbuilt. No fit, no tier change.

## Result

On the octonions `𝕆` (Baez structure constants — the **same `octMul`** as the
landed `QOU/MathlibExt/OctonionDerivations`), let `𝔤₂ = Der(𝕆)` (the derivation
algebra, `dim = 14`, proved on `main`). Fix a unit imaginary octonion `e` and let

`ev_e : Der(𝕆) → 𝕆,  D ↦ D(e)`,   `𝔰𝔲(3) := ker(ev_e) = { D ∈ Der(𝕆) : D(e) = 0 }`.

Exact rational linear algebra
([`octonion_su3_stabilizer_probe.py`](../../computations/octonion_su3_stabilizer_probe.py),
witness `octonion-su3-stabilizer.witness.json`) gives:

| quantity | value |
|---|---|
| `dim Der(𝕆)` | **14** (independent cross-check of the sibling Lean `dim=14`, #3717/#3734) |
| `rank(ev_e)` | **6** |
| `dim ker(ev_e) = dim 𝔰𝔲(3)` | **8** |
| `14 − 8` | **6 `= dim S⁶ = dim G₂/SU(3)`** |

verified orbit-independently for `e ∈ {e₁, e₂, e₄}` (equal, as `G₂` acts
transitively on `S⁶`).

## Why this is the colour `SU(3)`

`dim 𝔰𝔲(3) = 8 = dim SU(3)`. The subalgebra of derivations fixing a preferred
imaginary unit **is** the **Günaydin–Gürsey colour `SU(3) ⊂ G₂ = Aut(𝕆)`** — the
"fix an imaginary direction" step by which `Im 𝕆` branches `7 = 1 ⊕ 3 ⊕ 3̄`. The
octonion-recovery analysis
([`2026-07-12-octonion-recovery-from-genus4-analysis.md`](2026-07-12-octonion-recovery-from-genus4-analysis.md))
established that QOU's three colour `S₃` sectors carry this colour `SU(3)` but
left the `𝔰𝔲(3) ⊂ 𝔤₂` embedding **unbuilt**; this closes that gap at the
Lie-algebra level, directly on the corpus's own `Der(𝕆)`.

## Mechanism (why `rank = 6`, structurally)

`im(ev_e)` lands in `⟨e₀, e⟩^⊥` (the `6`-dimensional tangent to `S⁶` at `e`):

- `D(1) = 0` for every derivation (`derivation_annihilates_one`, on `main`), and a
  derivation preserves the norm, so `⟨D(e), e⟩ = 0` — hence `D(e) ⊥ e`;
- `D` maps `Im 𝕆 → Im 𝕆`, so `D(e) ⊥ e₀ = 1`.

The probe confirms both projections vanish exactly (`im_perp(e₀, e) = True`), so
`rank(ev_e) ≤ 6`; an explicit `6×6` minor gives equality. Thus `dim 𝔰𝔲(3) =
14 − 6 = 8`, and the `6`-dimensional image is precisely `T_e S⁶` — the orbit
`G₂·e = S⁶ = G₂/SU(3)`, recovered as a **dimension count**, not extrinsic
Lie-group theory.

## Lean formalisation (follow-up)

This is the exact-arithmetic establishment. The Lean version — `ev_e` as a
`LinearMap` on the landed `Der𝕆`, `rank = 6` via the same explicit-basis / rank
machinery the sibling used for `rank = 50`, hence `finrank 𝔰𝔲(3) = 8` — is a
clean follow-up on `OctonionDerivations` (deferred here only because that file's
`decide`-heavy compile makes the iterate loop slow; the computation itself is
settled). Tracked for the octonion `MathlibExt` tree.

## Scope discipline

Exact rational linear algebra on the standard Baez octonions — a **cross-check +
a new dimension count**, not a fit and not a numerical near-match. `dim 𝔰𝔲(3)=8`
and `dim S⁶=6` are integers, computed exactly. No `c_k`, no observable wired, no
tier change. Anti-laundering: nothing here is tuned to data.

-- Ref: [manuscript] docs/audits/2026-07-12-octonion-recovery-from-genus4-analysis.md
