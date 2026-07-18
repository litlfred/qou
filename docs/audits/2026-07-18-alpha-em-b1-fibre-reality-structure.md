# α_EM τ-correspondence, bean B1 — the fibre reality structure ρ (obstruction re-typed)

**Date:** 2026-07-18 · **Axis:** the `1/π` correspondence wall (milestone `qou-b5qg`, bean
`qou-qcz1`) · **Tier:** symbolic-exact analytic bookkeeping · **Derives no clause; no fit;
nothing wired; `1/(8π)` stays phase-4.**

Probe [`alpha_em_b1_fibre_reality_structure_probe.py`](../../computations/alpha_em/alpha_em_b1_fibre_reality_structure_probe.py)
→ [witness](../../computations/alpha_em/alpha-em-b1-fibre-reality-structure.witness.json) (4/4).

## Result

The anti-holomorphic ingredient the τ-obstruction (`a6d522e0a`) demanded is the **fibre
parameter conjugation `ρ: q ↦ q̄`** — an involution *not in the q-algebra*:

- **(R1)** Through the nome, `ρ` **is** `τ ↦ −τ̄` — exactly the Hodge-conjugation analytic
  type. The pairing **{ρ ↔ Hodge conjugation} has no type obstruction.**
- **(R2)** On the fibre circle `|q|=1`, `ρ` coincides *pointwise* with bar (`q⁻¹=q̄`) while
  differing globally (bar holomorphic, ρ anti-holomorphic) — resolving why brick 3 saw
  "bar exchanging the degenerate points": that exchange *is* ρ, seen through its circle
  restriction; its geometric shadow is the Lean-locked vertex-family swap (#3942).
- **(R3)** `ρ` **fixes the archimedean point** (`q₀∈ℝ`): the reality structure is unbroken
  at the observable point — the conjugation doubling is **fibre-only** (consistent with the
  Im(q) fibre-vs-observable discipline and real masses at `q₀`).
- **(R4)** The full dictionary now **types consistently**:
  `bar ↔ τ↦−τ` (holo=holo) · `transpose ↔ τ↦½−τ` (holo=holo) · `ρ ↔ τ↦−τ̄` (anti=anti).
  The obstruction barred only the mis-typed `{transpose ↔ conjugation}`; on `{±i}`, ρ
  exchanges the points and the transpose fixes them — the two-strata role-swap, correctly
  typed.

## What remains (B2, `qou-tq20`)

The functorial statement: τ intertwines `ρ` with the actual Hodge conjugation of
`H¹(Bring)` (whose degenerate-locus shadow is already Lean-verified). B1 supplies the
type-consistent dictionary; it does not derive the functor.

## Scope guard (STRICT)

Exact bookkeeping; derives no clause; no fit; nothing wired. Composes with (not
duplicating): the merged obstruction audit (`a6d522e0a`), merged #3933/#3942, the merged
conjecture statement (#3921).

## Cross-references

- Proof plan: milestone `qou-b5qg` (B1–B5) — `.beans/`
- Obstruction: `2026-07-18-alpha-em-tau-correspondence.md` (main)
- Geometric shadow: `2026-07-18-alpha-em-sigmaJ-geometric-carrier.md` + `QOU/Archimedean/SigmaJGeometricCarrier.lean` (#3942, merged)
