# λ-coloured WRT(S³/2I): colour-resolved decomposition + the Schur–Weyl index obstruction

**Date:** 2026-06-22
**Branch:** `claude/keystone-wrt-color-schurweyl-2026-06-22`
**Status:** Positive/structural — the colour-resolution is computed (well-anchored) and the precise
obstruction to a direct `colour ↔ W_λ` identity is established (an index-counting + Schur–Weyl fact).
No fit; no component↔W_λ match asserted.
**Bean:** [`s5bb`](../../.beans/s5bb--s5-so3-keystone.md)
**Follows:** [`2026-06-22-keystone-habiro-wrt-s3-2i.md`](2026-06-22-keystone-habiro-wrt-s3-2i.md)
**Script:** [`scripts/keystone_wrt_color_schurweyl_probe.py`](scripts/keystone_wrt_color_schurweyl_probe.py)
**Witness:** [`computations/keystone-wrt-color-schurweyl.witness.json`](../../computations/keystone-wrt-color-schurweyl.witness.json)

## The colour-resolved decomposition (well-anchored)

The bare Σ(2,3,5) invariant already splits over its four false-theta components, one per support
residue `a ∈ {1,11,19,29}` (the icosahedral/E₈ data). Evaluated at the bar image `1/q₀` (50 dps):

| `a` | `Ψ̃₃₀^{(a)}(1/q₀)` |
|-----|-------------------|
| 1 | 0.98999965222313 |
| 11 | 0.78861465023608 |
| 19 | 0.50299993214087 |
| 29 | 0.04796281223285 |
| **sum** | **2.32957704683293** (= `Ψ(1/q₀)`, cross-check 1.4×10⁻¹⁵) |

These four components are the colour-resolution intrinsic to the closed manifold — the SU(2)
integrable / flat-connection structure of Σ(2,3,5). (Σ(2,3,5) has exactly two irreducible SU(2) flat
connections; with the trivial and the reflection structure these organise the four false-theta
residues.)

## The obstruction to a direct `colour ↔ W_λ` identity (stated, not forced)

| index set | size | meaning |
|-----------|------|---------|
| WRT colour components of Σ(2,3,5) | **4** | residues {1,11,19,29}; SU(2)-spin / flat-connection index |
| partitions `λ ⊢ 5` | **7** | S₅ Wedderburn blocks of `H₅(q)` |
| "physical" blocks | **3** | (3,1,1), (3,2), (2,2,1) |

`4 ≠ 7` and `4 ≠ 3`: there is **no naive bijection** between the WRT colour components and the `W_λ`
family, so a direct numerical `component = W_λ` equality is **impossible by counting** (and was not
sought — forcing one would be numerology).

**The reason is representation-theoretic and precise.** The WRT colour index is **SU(2)-spin** (the
Wilson-line rep / the Seifert-fibre colour); the `W_λ` index is **S₅-partitions**. SU(2)-spin and
Sₙ-partitions are related by **Schur–Weyl duality**, *not* by the identity. So the λ-resolution of the
`W_λ` family from the (SU(2)-coloured) WRT data **requires the explicit Schur–Weyl functor**
`SU(2)-colours → S₅-blocks` — the very same colour-ℂ³ vs spin-ℂ² Schur–Weyl bridge the framework
already uses (#2364).

## The frontier, now at the representation-theoretic core

The keystone's open object has been driven, this session, through a strictly-narrowing chain:

1. finite Sasakian + equivariant index *(arena ruled out)*;
2. modular block weights `d²/D²` *(reframe)*;
3. non-compact `E_q(2)` contraction at real `q₀` *(identification)*;
4. Habiro-WRT(Σ(2,3,5)) at the bar image `1/q₀` *(q-series operational)*;
5. **here:** the colour components are computed, and the residual map is pinned to the **Schur–Weyl
   functor** SU(2)-colour → S₅-block.

That functor is **well-understood mathematics, finitely stated** — the genuine remaining step is to
push the SU(2)-coloured WRT data through Schur–Weyl and check the resulting S₅-resolved weights
against `W_λ` (with the bar/Habiro bridge for the `q₀ > 1` regime). This is the representation-theoretic
core, not differential geometry; it is a clean handoff point.

No fit; nothing wired; `c_k`/`Δ_λ` cal-anchored.

## Cross-references

- [`2026-06-22-keystone-habiro-wrt-s3-2i.md`](2026-06-22-keystone-habiro-wrt-s3-2i.md) — the bare invariant + bar/Habiro bridge this resolves.
- [`2026-06-22-keystone-modular-category-identification.md`](2026-06-22-keystone-modular-category-identification.md) — the non-compact `E_q(2)` home.
- Sources: Hikami, arXiv:math/0604091, math-ph/0504082; Andersen–Mistegård (resurgence), Wiley jlms.12506.
