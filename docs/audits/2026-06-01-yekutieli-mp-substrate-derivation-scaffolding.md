# Yekutieli substrate-derivation of m_p — scaffolding (2026-06-01)

**Date:** 2026-06-01
**Status:** SCAFFOLD ONLY — multi-session research direction, NOT a closure attempt.
**Triggered by:** user 2026-06-01 "1 2 3 4" — item 3 of session probe list.
**Queue item:** `research-yekutieli-substrate-derivation-mp` (`.beans/research-queue.json`).

## Goal

Promote (α_em/π)/dim H_3 ≈ 54 ppb m_p near-match (PR #1581) to
**tier = proved** via Yekutieli (2015) non-abelian Stokes integration
over the 8-ideal-octahedron tessellation of the 𝓑_3-complement.

This audit takes stock of prior Yekutieli work (5 audit docs +
Lean formalization + computational probes) and names the concrete
first probes for the next 3–5 session program.

## Prior art (chronological)

| Date | Audit | Verdict |
|------|-------|---------|
| 2026-05-22 | `yekutieli-percell-conjecture-formalized.md` | Conjecture stated: `Π_HS ∘ τ_q` at h² extracts curvature of ONE of 8 ideal octahedra = `−G·h²` |
| 2026-05-23 | `yekutieli-bijection-natural-reading-negative.md` | Natural-reading bijection NEGATIVE: cell ↔ H_4-partition is not the load-bearing mechanism |
| 2026-05-24 | `crystal-yekutieli-correspondence-chain.md` | Kashiwara crystal ↔ Yekutieli per-cell correspondence |
| 2026-05-24 | `yekutieli-mi-derivation-path.md` | m_i (mass per nucleon) derivation path |
| 2026-05-25 | `non-abelian-stokes-reading-a-exploration.md` | Reading-A geometrised scaffold |
| 2026-05-23 | `yekutieli-volume-join-verdict.md` (via PR #1628) | Volume-join verdict |
| 2026-06-01 | `m_p_pslq_120_dps.witness.json` (PR #1629) | 54 ppb residual is anchor-stable but its sub-coefficient is NOT a rational basis combination at 120-dps PSLQ |

## Current near-match state

```
m_p / m_e   = 1836.15267343  (CODATA)
prediction  = m_e × VolDensity(𝓑_p, q_0) × [ 1 + (α_em/π) / dim H_3 ]
            = m_e × VolDensity(𝓑_p, q_0) × [ 1 + 1/(137.036·π·6) ]
residual    = 54 ppb (anchor-stable; PR #1581)
```

The `(α_em/π)/dim H_3 = (α_em/π)/6` factor:
- Cross-anchor stable (q_proton ↔ q_muon): PR #1617 (27 alt-geometries)
- Not a rational basis combination at 120 dps PSLQ (PR #1629)
- Hypothesised structural origin: Bring-zero-mode analog (parallel m_K/m_π closure in PR #1442)

## What "promoting to proved" requires

The (α_em/π)/dim H_3 sub-coefficient needs a structural derivation
from the Yekutieli machinery, not a PSLQ-style identification.
The conjectural mechanism:

```
m_p categorical formula
  = m_e × ∫_{𝓑_p} τ_q^* curvature       [Yekutieli non-abelian Stokes]
  = m_e × Σ_{8 ideal octahedra} per-cell contribution
  = m_e × Σ_{cells} (G/π) × α_em-shaped weight × (dim H_3)⁻¹-shaped weight
```

Where:
- 𝓑_p = `𝓑_3` = Borromean rings complement, the canonical proton braid frame
- τ_q = q-deformation of the Yekutieli connection
- The Bring-zero-mode analog supplies the `α_em/π` shape; the `1/dim H_3` shape comes from the per-cell normalisation

## Concrete first probes (3–5 sessions estimated)

Each probe deliverable: one Python script + witness + audit doc, decided BEFORE running:

### Session A — per-cell α_em weight derivation
Goal: derive the α_em/π factor as the per-cell coupling weight of one of
the 8 ideal octahedra under τ_q.

Probe: `yekutieli_per_cell_alpha_em_derivation_probe.py`
  - Take the Reading-A scaffold from PR #1628's geometrised audit
  - Apply τ_q action to ONE ideal octahedron at h² order
  - Compute the coupling weight; verify it equals α_em/π at q_0
  - If yes: structural derivation half-complete
  - If no: re-examine the Bring-zero-mode analog assumption

Pre-stated failure signature: the per-cell weight comes out as a
**rational** times G (no α_em factor) ⟹ α_em is NOT the per-cell
coupling; needs a different categorical input.

### Session B — per-cell 1/dim H_3 normalisation
Goal: derive the 1/dim H_3 = 1/6 factor as the per-cell normalisation
under the half-symmetric projection Π_HS.

Probe: `yekutieli_per_cell_dim_h3_normalisation_probe.py`
  - From PR #1623 audit's NEGATIVE bijection finding (natural-reading
    fails) + PR #1624's crystal correspondence chain
  - Re-attempt Π_HS as a Kashiwara-crystal projection (not the
    natural conjugation involution that was refuted)
  - Compute the normalisation factor at H_3
  - Verify equals 1/dim H_3 = 1/6 at q_0

Pre-stated failure signature: factor comes out as 1/Σ d² = 1/14 or
some other Wedderburn-block-weighted form ⟹ the (α_em/π)/dim H_3
factor is correct numerically but NOT a per-cell Yekutieli structure.

### Session C — composition + cross-anchor verification
Goal: stitch Sessions A + B into a closed-form per-cell contribution,
verify the sum over 8 octahedra reproduces the 54 ppb correction,
and check cross-anchor stability.

Probe: `yekutieli_mp_substrate_closure_probe.py`
  - Compute Session A × Session B for each of 8 octahedra
  - Sum; compare to required 54 ppb correction
  - Evaluate at q_proton AND q_muon
  - If both match: structural derivation COMPLETE, m_p = proved
  - If only one matches: anchor-coincidence; revisit one of the
    upstream sessions

Pre-stated failure signature: closes at q_proton but not q_muon ⟹
fibre-level Habiro element required (parallel α_EM PR #1511 pattern).

### Optional Session D — Lean formalisation
If Sessions A+B+C close:
- Formalize the per-cell Yekutieli theorem in
  `content/quantum-observable-universe/lifting-and-descent/`
- Class-axiomatise the curvature integral
- Discharge in Lean modulo the class instance (§3b-cond pattern)

## Anti-pattern guards

- ❌ Do NOT search for a fitted formula matching 54 ppb numerically
  without a structural mechanism (8th-ansatz trap, see PR #1629
  PSLQ refutation)
- ❌ Do NOT re-derive the natural-reading per-cell bijection — it was
  refuted by PR #1623
- ❌ Do NOT assume the 8 octahedra contribute equally — they may
  group by Borel descent into orbits of unequal size
- ✓ DO start with Session A; do not skip ahead to Session C
- ✓ DO require cross-anchor verification at Session C

## Cross-refs

- PR #1581 — `(α_em/π)/dim H_3` 54 ppb near-match
- PR #1617 — cross-anchor stability across 27 alt-geometries
- PR #1623 — natural-reading bijection NEGATIVE
- PR #1624 — Kashiwara-crystal correspondence
- PR #1628 — Reading-A geometrised scaffold + volume-join verdict
- PR #1629 — 120 dps PSLQ refutation of rational basis fit
- PR #1442 — m_K/m_π Bring-zero-mode closure (template for Session A)
- PR #1511 — α_EM `[2]_q·(1-h²α)` Habiro element (template for Session C)
- `prop:yekutieli-non-abelian-stokes`
- `prop:bring-zero-mode-substrate`
- `conj:per-cell-curvature-extraction`
- `docs/coordination/1ppq-mass.md`
- `.beans/research-queue.json` → `research-yekutieli-substrate-derivation-mp`
