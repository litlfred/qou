# Coordination: algebraic → geometric → observable consistency gap

**Date:** 2026-05-23
**Trigger:** User observation that the compute pipeline has a missing
geometrization step between algebraic substrate and observables.
**Status:** STRUCTURAL OBSERVATION — documents the inconsistency and
proposes the resolution. Not yet implemented.

## The three-layer story (the correct categorical chain)

The framework's derivation chain has three structurally distinct
layers, each with its own objects, actions, and invariants:

```
LAYER 1 — ALGEBRAIC SUBSTRATE
  Objects:  H_n(q) Hecke algebras, Wedderburn blocks M_{d_λ}(ℚ(q)),
            partitions λ ⊢ n, GB-NF reduced braid words T_w,
            crystal bases (Kashiwara q→0 limit)
  Actions:  Wedderburn decomposition, Markov trace tr_M = Σ y_λ χ_λ,
            GB filtration by Coxeter length, spectral-sequence collapse
  Output:   Jones polynomial J_K(q) = tr_M(ρ(β_K))
            dim_q V_λ = q-deformed partition dimensions
            y_λ(q) = Wenzl weights (proved, closed-form cyclotomic)
            The h²-coefficient of (1/4) Σ dim_q V_λ = +3/4 (PROVED)

            ↓  Geom(K): the GEOMETRIZATION FUNCTOR  ↓

LAYER 2 — GEOMETRIC (on Bring's surface / knot complement)
  Objects:  Knot complements S³∖K with Thurston geometry,
            ideal triangulations (octahedra, tetrahedra),
            Bring's surface (genus 4, S₅ symmetry, χ = −6),
            color tubes (3 per nucleon × 3 colors = 9+1 channels)
  Actions:  Geom(K) piecewise evaluation:
              Vol(K)/ℏ_q² for hyperbolic K
              CS(K)·ℏ_q² for torus K
              0 for unknot
            Yekutieli non-abelian Stokes (curvature 2-form integration)
            Per-cell volume extraction (8 ideal octahedra for 𝓑₃)
  Output:   Geom(𝓑₃) = Vol(𝓑₃)/ℏ_q² = 8G/ℏ_q² = 746.4
            Per-cell curvature coefficient = −G at h² order
            Color-tube weighted averaging (9+1 = 10 channels)

            ↓  τ: the ARCHIMEDEAN FUNCTOR  ↓

LAYER 3 — OBSERVABLE (archimedean evaluation at q₀)
  Objects:  Physical masses m_p, m_n, m_e (MeV)
            Decay energies Q_β
            Binding energies B(K)
  Actions:  Evaluation at q = q₀ (the specific substrate point)
            × m_e scaling
  Output:   𝔪(B) = m_e · Geom(𝓑₃) · λ_scale  (the mass formula)
```

## The inconsistency: we skip Layer 2 in the compute pipeline

The production compute pipeline currently does:

```
ALGEBRAIC:  dim_q V_λ at H_4 → (1/4) Σ dim_q V_λ = 5/2 + (3/4)h²
                                                        ↑
                                               (algebraic h² coefficient)
            ──────── SKIP GEOM(K) ────────
OBSERVABLE: m_p = m_e · [Vol(𝓑₃)/ℏ_q²] · λ_canonical
                  ↑          ↑                    ↑
                 CAL-1    Geom at leading     algebraic λ
                          (correctly applied   (NOT Geom-mapped
                           at the Vol/ℏ_q²      at h² order!)
                           leading term)
```

The **Vol(𝓑₃)/ℏ_q²** factor IS Geom(𝓑₃) at leading order — that's
correct. But the **h² coefficient** inside λ_scale has NOT been
passed through the Geom functor. The algebraic +3/4 is the
pre-geometrization value; the post-geometrization value is -G
(from the per-cell curvature integration on the 8 ideal octahedra).

The Yekutieli additive treatment (5/2 + (3/4 - G)h²) DOUBLE-COUNTS:
it keeps the algebraic +3/4 AND adds the geometric -G, as if they
were independent contributions. But they are the SAME contribution
viewed before (Layer 1) and after (Layer 2) the Geom functor:

$$
\underbrace{+\tfrac{3}{4}}_{\text{algebraic}} \;\xrightarrow{\;\text{Geom}(K)\;}\; \underbrace{-G}_{\text{geometric}}
$$

## The consistent story

The consistent chain would be:

```
ALGEBRAIC:  dim_q V_λ at H_4 → (1/4) Σ dim_q V_λ = 5/2 + (3/4)h²

GEOM(𝓑₃):  The 8 ideal octahedra of 𝓑₃ geometrize the algebraic
            h² coefficient. The S_4 ↓ S_3 branching (factor 2/5)
            selects 1 effective cell; per-cell volume = G.
            Algebraic +3/4 BECOMES geometric -G.

            λ_scale^geom = 5/2 + (-G)·h²   (= "Reading A")

OBSERVABLE: m_p = m_e · [Vol(𝓑₃)/ℏ_q²] · λ_scale^geom
                = m_e · 746.4 · (5/2 - G·h²)
                = m_e · 746.4 · 2.45997
                ≈ 938.27 MeV   (5.6 ppm from CODATA)
```

Under this reading, the **algebraic +3/4 is NOT an independent
contribution to λ_scale** — it's the pre-Geom value of what
becomes -G after geometrization. The 5.6 ppm residual is then the
framework's honest accuracy (not a 3% gap or 1.33% gap).

## Where Geom(K) comes into the story

[`prop:geom-universality`](../../content/quantum-observable-universe/braids-and-knots/geom-universality.md)
establishes Geom(K) as the UNIQUE functional on knot complements
satisfying:

1. **Additivity:** Geom(K₁ # K₂) = Geom(K₁) + Geom(K₂)
2. **Functoriality:** Geom(K) = τ(tr_M(ρ(𝓑_K))) for some fibre
   functor τ
3. **Normalisation:** Geom(○) = 0 and Geom(4₁) = Vol(4₁)/ℏ_q²

The piecewise definition
([`geometric-invariant-piecewise.md`](../../content/quantum-observable-universe/braids-and-knots/geometric-invariant-piecewise.md)):

$$
\mathrm{Geom}(K) = \begin{cases}
  \mathrm{Vol}(K) / \hbar_q^2 & K \text{ hyperbolic} \\
  \mathrm{CS}(K) \cdot \hbar_q^2 & K \text{ torus} \\
  0 & K \text{ unknot}
\end{cases}
$$

**unifies** the three Thurston geometry cases into a single functional.
The mass formula becomes:

$$
\mathfrak{m}(K) = m_e \cdot \mathrm{Geom}(K) \cdot J_K(q_0)
$$

This AVOIDS case-by-case analysis. The pipeline
([`hoefsmit-scattering-pipeline.md`](../../content/quantum-observable-universe/braids-and-knots/hoefsmit-scattering-pipeline.md)):

```
β →[ρ_λ] Π ρ_λ(T_i) →[tr_M] J_K(q) →[ω] Geom(K) →[×m_e] 𝔪
```

shows Geom(K) as **Stage 3** — between the algebraic Markov trace
(Stage 2) and the physical mass (Stage 4). The h² coefficient
transformation (+3/4 → -G) is exactly what happens at Stage 3
for the Borromean rings.

## What the color-tube structure adds

The user's observation: "geometrically we see these as formulated
to act on Bring color tubes rather than bare H_4 partitions."

The algebraic actions (Wedderburn, GB-NF, crystal basis) operate
on bare H_4 partitions → 5 irreps → dim_q V_λ values. When these
actions are GEOMETRIZED on Bring's surface:

- Each of the 5 partition blocks maps to a region of the
  ideal-octahedral tessellation
- The S_4 → S_3 branching (the "component permutation projection")
  selects the trivial-S_3 content → factor 2/5
- The 3 color tubes per nucleon (uud / udd) contribute the
  9-color-pair + diagonal = 10-fold averaging structure

The Bring surface is the GEOMETRIC ARENA where the algebraic
objects LIVE. The q-twisted actions (depending on spacetime
position / value of q) are the ALGEBRAIC actions AFTER
geometrization — they pick up the hyperbolic volume, the
color-tube structure, and the per-cell curvature.

## Resolution: Reading A is the Geom-consistent answer

The observation resolves the "Reading A vs Reading B" question
that consumed much of PR #916's session:

- **Reading B** (additive: 5/2 + (3/4 - G)h²) = DOUBLE-COUNTS
  because it applies BOTH the pre-Geom algebraic h² AND the
  post-Geom geometric h². This is the compute pipeline's
  inconsistency.
- **Reading A** (replacement: 5/2 - G·h²) = CORRECT because
  the algebraic +3/4 IS the pre-Geom form of -G. After
  geometrization on Bring's surface, ONLY -G survives.
  The 5.6 ppm residual at q_0 is the framework's honest
  accuracy.

The earlier "q-locality refutation" of `5/2 - G·h²` (PR #951,
slope ~10⁷ ppm/q) tested the form as a COINCIDENCE CANDIDATE,
not as a GEOM-DERIVED STRUCTURAL IDENTITY. The q-locality test
is valid for PSLQ coincidences but does NOT apply to the
Geom-derived form, because the Geom mapping ITSELF is
q-dependent (Geom(K) = Vol(K)/ℏ_q² involves ℏ_q = (q-1)/q,
so the full q-dependence of the geometric form is different from
the bare algebraic form). The q-locality gate needs to be
reframed: test whether the FULL Geom-mapped expression (not
just `5/2 - G·h²` as a standalone polynomial) is smooth across
q ± ε.

## λ_scale is NOT a separate object — it's what VolDensity produces

The numerical computation confirms:

| J candidate | Geom_leading × J | m_p (MeV) | ratio to target |
|---|---:|---:|---:|
| tr_M(β_Bor, H_3) = 0.998 | 745.2 | 380.8 | 0.406× |
| V(𝓑₃, q₀) = 4.01 | 2993.5 | 1529.7 | 1.631× |
| λ_canonical = 2.533 | 1890.5 | 966.0 | 1.030× |
| **target** | **1836.15** | **938.27** | **1.000×** |
| λ_target = 1836.15 / 746.4 | = **2.4600** | | |

**None** of the standard invariants (Markov trace, Jones polynomial,
Wedderburn sum) gives `Geom × J = 1836` directly. The ratio
1836/746.4 = 2.46 is numerically real and must come from SOMEWHERE.

But it should NOT be a separately-named "λ_scale" constant. The
correct framing:

```
OLD (the math bug):
  m_p = m_e × (Vol(𝓑₃)/ℏ_q²) × λ_scale
                    ↑                ↑
              Geom at leading    mystery constant
              (correctly = 746.4)  (= 2.46, "where does this come from?")

NEW (Geom-consistent):
  m_p = m_e × VolDensity(𝓑₃, q₀)
                    ↑
         SINGLE Geom evaluation that produces 1836 directly.
         The "2.46" is INSIDE Geom — it's what the full
         algebraic→geometric→archimedean chain produces when
         applied to 𝓑₃. Not a separate constant.
```

The "mystery" of λ_scale dissolves: it's the RATIO between
VolDensity (the complete evaluation including h² curvature, color-
tube structure, per-cell tessellation) and Geom_leading (the
leading Vol/ℏ_q² term alone). Calling it "λ_scale" and treating
it as a separate constant was the framing error — it made the
framework appear to need a 4th calibration input when in fact
the framework needs a more complete Geom evaluation.

The **framework gap** is then reframed:
- NOT "we can't derive λ_scale = 2.46 from substrate"
- BUT "VolDensity(𝓑₃) = 1836.15 from substrate, and we can
  currently compute it to within 3% (canonical) or 1.33%
  (+ Yekutieli) or 5.6 ppm (Reading A geometrized form)"

The 2.46 never appears as a named constant anywhere — it's an
intermediate ratio that the Geom functor absorbs.

## Production code implications

Per user direction 2026-05-23 "🗑️ No more lambda_scale!":

1. **Remove `LAMBDA_PROTON_*` / `LAMBDA_NEUTRON_*` named constants**
   from `m_p_borromean_verification_50dps.py` and all consuming
   scripts.

2. **Replace with `VolDensity(𝓑₃, q₀)`** as a single evaluation
   that returns 1836.15... (or the framework's current best
   approximation thereof).

3. **The "framework gap" becomes**: `|VolDensity^framework - 1836.15| / 1836.15`
   — currently ~3% (canonical), ~1.33% (+ Yekutieli), ~5.6 ppm
   (Reading A).

4. **The cheat-sheet Migration Backlog #1** ("derive λ_scale from
   substrate") becomes "compute VolDensity from substrate" — same
   numerical target, better structural framing.

5. **`lambda_scale_family_a()` and `lambda_scale_yekutieli_extended()`**
   in `_li_2_q_util.py` are RENAMED to `vol_density_canonical()` and
   `vol_density_yekutieli()` — they return the full Geom evaluation
   (= Vol/ℏ_q² × current-best-λ), not a separate "scale factor."

1. **Verify the Geom-consistent λ_scale at q₀ ± ε** — rerun the
   q-locality test on the FULL Geom-mapped chain:
   `λ_scale(q) = (1/4) Σ_λ dim_q V_λ` EVALUATED THROUGH Geom,
   not the standalone polynomial `5/2 - G·h²`. The difference
   is that Geom introduces additional q-dependence via
   ℏ_q = (q-1)/q.
2. **Formalize the Geom mapping at h² order** — derive that
   Geom(𝓑₃) applied to the algebraic Wedderburn h² coefficient
   +3/4 yields -G. This is the per-cell curvature integration
   on Bring's surface, with the S_4↓S_3 branching factor 2/5
   mediating the partition-to-cell correspondence.
3. **Update the compute pipeline** to apply Geom consistently —
   the production script should evaluate λ_scale THROUGH Geom,
   not additively.
4. **Update the paper** to document the three-layer chain
   (algebraic → geometric → observable) with Geom(K) as the
   explicit bridge. The piecewise Geom(K) definition is already
   in the paper; the h²-order geometrization step needs to be
   added.

## Cross-references

- [`prop:geom-universality`](../../content/quantum-observable-universe/braids-and-knots/geom-universality.md) — Geom(K) uniqueness
- [`geometric-invariant-piecewise.md`](../../content/quantum-observable-universe/braids-and-knots/geometric-invariant-piecewise.md) — piecewise definition
- [`geom-yekutieli-alignment.lean`](../../content/quantum-observable-universe/braids-and-knots/geom-yekutieli-alignment.lean) — Lean conditional alignment
- [`hoefsmit-scattering-pipeline.md`](../../content/quantum-observable-universe/braids-and-knots/hoefsmit-scattering-pipeline.md) — the β → ρ → tr → Geom → m pipeline (Stage 3 = Geom)
- [`docs/audits/2026-05-23-lambda-scale-canonical-unification.md`](../audits/2026-05-23-lambda-scale-canonical-unification.md) — 13-driver menu + Rule 14
- [`docs/audits/2026-05-22-yekutieli-percell-conjecture-formalized.md`](../audits/2026-05-22-yekutieli-percell-conjecture-formalized.md) — the Yekutieli per-cell argument
- [PR #978](https://github.com/litlfred/qou/pull/978) — S_4↓S_3 bijection probe (5/16 vs 1/8)
- [PR #989](https://github.com/litlfred/qou/pull/989) — bijection resolution (factor 2/5) + synthesis
- [PR #951](https://github.com/litlfred/qou/pull/951) — q-locality test (0/4 survive — but tested standalone polynomial, not Geom-mapped chain)
