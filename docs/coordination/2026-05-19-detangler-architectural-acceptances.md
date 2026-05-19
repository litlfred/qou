# Detangler mega-tranche — architectural-accept rationale for remaining items

Closes the 3 remaining detangler `needs-author` queue items as
`wontfix:architectural`, after the 16-commit structural-cleanup tranche
on `claude/detangler-quick-wins-section-splits-2026-05-18` resolved 12
others (5 section splits / 2 table extractions / 1 fold / 2 fwd-ref
reorders / 1 prop→prf FP filter / 1 chapter-level split). The 3 below
are not addressed by mechanical reorganisation; their resolutions are
architectural-accept decisions.

## 1. Ch 17 (`app:knot-operations`) — 100% cross-section ratio

**Finding.** All 5 inter-block edges in `appendix-knot-operations`
cross section boundaries (5/5 = 100% cross-section ratio).

**Architectural rationale.** Ch 17 is a 5-section reference appendix
for the Hecke-algebra operations dictionary. Each section is a
self-contained operation reference (particle NFs / Hecke-algebra ops
/ gluon-model comparison / knot-operator basis table / hadron-level
knot decomposition). The 100% ratio reflects the natural structure
of a reference appendix: every inter-block edge crosses sections by
design, because each section is one named entry-point for the reader.

**Decision.** Reference appendix is exempt from R1-R3 density band.
The reader-navigation affordance (5 named sections vs 1 flat section)
outweighs the cross-section finding.

## 2. Braids→Descartes 29 cross-wall forward edges

**Finding.** 29 forward edges Ch 5 (braids, pre-wall) → Ch 7 (descartes,
post-wall). Crosses the categorical/archimedean wall.

**Architectural rationale.** The archimedean wall is the paper's
substrate-to-numerical-evaluation cut. Pre-wall content stays in
generic-R substrate (categorical); post-wall content specialises to R
for numerical evaluation. The wall's purpose IS that forward direction:
substrate → consumer.

The detangler skill's `archimedean-wall-violation` rule is only about
edges crossing the wall in the WRONG direction (post-wall → pre-wall
edges silently consuming categorical machinery without an
`archimedean-bridge` tag). All 29 edges here flow in the CORRECT
direction (substrate → numerical consumer).

**Decision.** Accept the 29 forward edges as canonical reading
direction. Wall-direction-respecting forward edges are by-design,
not a finding.

## 3. `prop:sw-3root-rational-integrand` → `rem:color-tube-cubic`

**Finding.** New proposition in Ch 5 (braids-and-knots) uses a remark
in Ch 7 (descartes-universe) for its defining cubic. H2 cross-chapter
forward edge.

**Architectural rationale.** The color-tube cubic
`F(z, c) = c^3 + (4z+1)c^2 + (6z^2+3z+1)c + (4z^3+3z^2+2z+1)` is
fundamentally a descartes-universe geometric object — it parametrises
the color tube in the Brings-surface coordinates that descartes-universe
defines. The SW-3-root product is the Ch 5 categorical-action consumer
of that cubic (the integrand `lambda_SW^(1)(z) = ∏_k dc_k/dz` is the
categorical mass-formula amplitude).

Moving `rem:color-tube-cubic` upstream to Ch 5 would mix categorical
and geometric content in a way that obscures both. Keeping the
forward edge preserves the substrate (geometric) → consumer
(categorical action) narrative.

**Decision.** Accept the forward edge. The remark stays in
descartes-universe; the prop stays in braids-and-knots; the cross-
chapter use is canonical.

## Cumulative detangler tranche state (2026-05-19)

After this acceptance commit:

| Status | Count |
|---|--:|
| resolved | 9 |
| wontfix (architectural / preview-chapter / false-positive / volume) | 9 |
| needs-author | 0 |
| **total** | **18** |

Detangler queue is fully drained. The 16-commit mega-tranche on
`claude/detangler-quick-wins-section-splits-2026-05-18` represents
the paper's structural-cleanup deliverable; this ledger entry caps
the queue by recording the 3 architectural acceptances that don't
need a code change.
