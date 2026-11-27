# Forward-ref logical-defect triage + workplan (2026-06-01)

**Source:** `forward_ref_classifier.py` reports **56 logical defects**
(was 60; recent main churn). All are **cross-chapter** — no within-
chapter defects, so section reordering alone won't help; the fixes are
either edge reclassification or chapter-level reorders.

## Buckets

| Bucket | Count | Category | Action | Effort |
|--------|------|----------|--------|--------|
| **A** | 9 | MISLABELED (mass-endomorphism → mass-theory) | edge review / invert / `uses`→`interprets` | 2-4 h |
| **B1** | 8 | REORDERABLE Δ≤2 (adjacent) | move target earlier / source later | 4-8 h |
| **B2** | 15 | REORDERABLE Δ3-8 | medium reorders | 8-16 h |
| **B3** | 15 | REORDERABLE Δ≥9 | long-range (defer) | 16+ h |
| **C** | 9 | ACCEPTED-ARCHITECTURAL | none (archimedean-wall direction) | — |

## Bucket C — already accepted (no action)
Per `2026-05-19-detangler-architectural-acceptances.md`:
- **particle-interactions → mass-theory (6):** the archimedean-wall
  direction (categorical pre-wall → numerical post-wall) is canonical.
- **brings-surface → particle-interactions (3):** geometry is the
  upstream producer of the categorical action.

## Bucket A — mislabeled (Phase 1, quick wins)
The mass-endomorphism chapter is a pedagogical opener; mass-theory is
the analysis chapter. Many `uses[]` edges are either backwards or merely
narrative. Candidates to review (read block prose, then invert edge OR
change `uses`→`interprets` OR extract a foundational piece):
1. `conj:mass-endomorphism` → `prop:hecke-mass-trace`, `conj:brane-tower-z-habiro`
2. `prop:explicit-central-idempotent` → `prop:jucys-murphy-central-elements-qou`, `prop:bring-figure-eight-depth-2-witness`
3. `prop:tau-M-asymptotic-rep-theory` → `prop:hoefsmit-V21-cos-symmetrization`, `prop:habiro-residue-sum-equivalence`
4. `prop:homological-shell-condensation` → `prop:graded-trace-residue-split`
5. `prop:categorical-chain-convergence-mechanisms` → `prop:q-beta-categorical-precision-ladder`
6. `prop:atomic-mass-gb-nf` → `prop:alpha-shift-torus-knot`

## Bucket B1 — adjacent reorders (Phase 2, Δ≤2)
1. `braids-and-knots/def:so3-generators` → `brings-surface/def:su2-generators` (move su2 earlier — foundational)
2. `braids-and-knots/prop:lagrange-resolvent-transform` → `brings-surface/def:brings-surface`
3. `lifting-and-descent/cor:quantum-dilogarithm` → `mass-endomorphism/thm:topological-mass`
4. `mass-theory/prop:transfer-matrix-level-independence` → `measurement-observation/def:bundle-isotopy-equivalence`
5. `particle-interactions/def:categorical-meson` → `predicted-spectra/def:quark-antiquark-production`
6. `particle-interactions/def:categorical-proton` → `predicted-spectra/def:down-quark`
7. `particle-interactions/prop:four-term-pair-nucleon` → `predicted-spectra/def:quark-antiquark-production`
8. `lifting-and-descent/def:motivic-galois-character` → `mass-theory/def:adelic-base-ring` (Δ2)

## High-fanout targets (move-once-fix-many)
- `observations/prop:flavor-split-aether` — 3 sources
- `predicted-spectra` defs (`quark-antiquark-production`, `down-quark`) — 2-3 sources each → **predicted-spectra may want foundational extraction / earlier placement**

## Phased plan
1. **Phase 1 (A):** verify + fix the 9 mislabeled. LOW risk. ~5-8 fixed.
2. **Phase 2 (B1):** the 8 Δ≤2 reorders. ~10-15 cumulative.
3. **Phase 3 (B2):** medium reorders; cluster on `predicted-spectra`.
4. **Phase 4:** confirm + record Bucket C (no code change).
5. **Phase 5 (B3):** defer; many may promote to C.

**Floor:** ~21 irreducible defects (Bucket C + intrinsic cross-chapter)
per `forward-ref-logical-analysis.md`. Target: 56 → ~21 (≈ 60% cut).

**Discipline:** each reorder must not create NEW logical defects (run
`forward_ref_classifier.py` before/after; net logical count must fall).
Edge reclassification (`uses`→`interprets`) only when block A genuinely
*mentions* rather than *relies on* block B — verified by reading prose.

---

## B1 feasibility check (2026-06-01) — the "easy wins" do NOT survive

After the Bucket-A reclassification (60→57 on main), each Bucket-B1
target was checked for **(deps that block an earlier move)** and
**(same-chapter consumers that would become NEW backward edges)**:

| B1 target | own deps | same-chapter consumers | verdict |
|---|---|---|---|
| `def:su2-generators` | `def:su2-basis` (same ch) | 1 | CLUSTER, +1 new edge |
| `def:brings-surface` | none | **13** | RISKY — up to 13 new backward edges |
| `thm:topological-mass` | 3 | 4 | RISKY |
| `def:bundle-isotopy-equivalence` | `def:bundle-initial-conditions` | 1 | CLUSTER |
| `def:adelic-base-ring` | `def:classical-limit-functor` | 3 | RISKY |
| quark cluster (`up`/`down`/`qq̄`/`breit-wheeler`) | `up-quark`→`conj:borromean-quark` **in observations (LATER)** | up=3, breit=2, … | **RISKY — net negative** |

**Conclusion.** *No* B1 defect is a clean single/cluster move: every
target is a foundational block with multiple same-chapter consumers, so
moving it earlier **creates more backward edges than it removes**. The
quark cluster additionally depends on `conj:borromean-quark` which lives
*later* (observations) — moving the cluster earlier would *worsen* that
edge.

This empirically confirms the **~21 irreducible floor**: the
particle-interactions→predicted-spectra and ↔mass-theory edges are the
intrinsic categorical→numerical (archimedean-wall) flow, not
misplacements. They belong with Bucket C (accept), not B (reorder).

**Recommendation:** the cheap, safe wins are exhausted at 60→57 (Bucket-A
narrative reclassifications). Further reduction requires either (a) the
author's editorial decision to relocate a heavily-consumed foundational
block (large, multi-PR), or (b) accepting the remaining cross-chapter
edges as architectural. Do NOT execute net-negative reorders to chase
the count.
