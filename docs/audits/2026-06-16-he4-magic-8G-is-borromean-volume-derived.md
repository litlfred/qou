# The ⁴He B_magic near-match: `8G` is DERIVED (= Vol(Borromean rings)), not fitted

**Date:** 2026-06-16
**Branch:** `claude/he4-magic-8G-provenance-2026-06-16`
**Status:** provenance assessment of the strongest low-isotope binding near-match; verified, no fit.
**Discipline:** production-vs-exploratory + critical-distance.

## Question

The low-isotope binding dashboard's single strongest hit is **⁴He** under `B_magic = ρ_F·m_e·A·8G`
(B_AME/B_magic = **0.945**, +5.7% over). Is the `8G` prefactor a derived quantity or a fitted number?

## Answer: 8G is DERIVED (verified — `scripts/he4_magic_8G_provenance.py`, exit 0)

$$8G \;=\; 8\cdot(\text{Catalan's constant}) \;=\; 7.327724753417\ldots \;=\; \mathrm{Vol}(L6a4) \;=\; \mathrm{Vol}(\text{Borromean rings}),$$

the hyperbolic volume of the Borromean-rings complement (= 2 ideal octahedra) — an **exact identity**, not a
tuned value. It matches the corpus `computations/substrate/knot_volumes.py::VOL_BORROMEAN` to 1e-9, and
`magic_A_formula.py` already documents it ("8G = Vol(L6a4) = Vol(Borromean rings), the universal residue
prefactor per the canonical chain"). So the prefactor is the **same Borromean volume** that anchors the
categorical mass formula `m(K)=m_e·Vol(K)·ρ(K)/ℏ_q²` — not numerology.

## But: the assembly is a near-match model, not a closure

`B_magic = ρ_F·m_e·A·8G` is the canonical **m_e·Vol·ρ** shape with:

| input | value | status |
|---|---|---|
| `m_e` | CAL-1 | derived |
| `8G` | Vol(Borromean rings) | **derived** (exact hyperbolic volume) |
| `Vol(⁴He) = A·8G` | 4·Vol(Borromean) | **modelled** (per-nucleon Borromean assumption) |
| `ρ_F` | 2 | **modelled** (doubly-magic density) |

`= 29.96 MeV` vs AME `28.30` → **+5.7% over**. The "fit-ness", to the extent any exists, is in the *assembly*
choices (`Vol = A·8G`, `ρ_F = 2`), **not** in `8G`. And it does **not** generalize: heavier doubly-magic nuclei
(¹⁶O, ⁴⁰Ca) use recursive-on-⁴He rather than this formula, and the binding dashboard shows every trace form
fails by ~60% at A≥6.

## Verdict

The ⁴He B_magic near-match is a **derived-prefactor near-match**: its key constant `8G` is the exact Borromean
volume (derived), within the canonical mass-formula shape — so it is **not numerology**. But the +5.7% residual,
the modelled `ρ_F=2`/`A·8G`, and the lack of generalization make it a **near-match, not a closure**. This is
consistent with the session's broader finding (only the deuteron is honestly closed, via `E₀×q⁻¹`); the A=3/A=4
near-matches are structurally grounded leads for **PROBE 2** (the A=4 interface operator, sibling cluster
#2369/#2371/#2372), not derivations.

## Cross-references

- `computations/magic_A_formula.py` — B_magic = ρ_F·m_e·A·8G; 8G = Vol(Borromean) documented
- `computations/substrate/knot_volumes.py` — `VOL_BORROMEAN`, `CATALAN_G`
- `docs/audits/2026-06-16-deuteron-closure-crosscheck-and-correction.md` — only the deuteron is honestly closed
- `scripts/he4_magic_8G_provenance.py` — this verification (exit 0)
