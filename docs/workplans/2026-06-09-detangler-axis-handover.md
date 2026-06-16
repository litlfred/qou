# Detangler cross-chapter axis — handover (2026-06-09)

Handover for the next agent picking up the **detangler integration-watch**
axis (cross-chapter forward references). Written after the quark-sector move
([#2021](https://github.com/litlfred/qou/pull/2021)) landed on `main`.

## State

- **Quark move merged** (rebase, [#2021](https://github.com/litlfred/qou/pull/2021)):
  the 5-block quark sector (`up-quark`, `up-quark-properties`, `down-quark`,
  `down-quark-properties`, `quark-antiquark-production`) moved Ch13
  `predicted-spectra` → Ch9 `particle-interactions`, before
  `prop:four-term-pair-nucleon`. Three flagged Ch9→Ch13 edges are now
  intra-chapter.
- **Detangler: 62 actionable** cross-chapter forward edges remain
  (`forward_ref_classifier.py --actionable-only`).
- **CI billing-stalled** the whole session (0 check runs). Local gate:
  `cd content && bun run validate quantum-observable-universe` — currently
  green (1 pre-existing Lean-stub warning on `prop:proton-mass-substrate-identity`,
  untouched).
- **Lean** sandbox network-blocks `release.lean-lang.org`; restore prebuilt
  oleans from the `lake-cache/qou-v4-24-0` orphan branch
  (CLAUDE.md §"Mathlib cache 403 fallback"). The quark move is Lean-safe
  regardless (`.lean` siblings travelled; QOU Lake package is independent of
  chapter dirs, so `lean.ref` sibling-resolution holds).

## Key references

| Artifact | Path |
|---|---|
| Triage doc (Tables A/B = waive inventory) | [`docs/audits/2026-06-09-cross-chapter-forward-ref-triage.md`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-06-09-cross-chapter-forward-ref-triage.md) |
| Classifier | [`computations/forward_ref_classifier.py`](https://github.com/litlfred/qou/blob/main/computations/forward_ref_classifier.py) (`:94` `WAIVED_CHAPTERS`, `:170` structural waivers) |
| Waiver policy | [`docs/forward-ref-waiver-policy.md`](https://github.com/litlfred/qou/blob/main/docs/forward-ref-waiver-policy.md) |
| H2 cross-chapter heuristic | `content/pipeline/content-graph-analysis.py --json` |

Re-run the actionable list:
```bash
python3 computations/forward_ref_classifier.py --json --actionable-only
```

## Next steps — prioritized

### P1 — finish the detangler axis (the in-flight tranche)

1. **Record the ~60 legit couplings as waives** (mechanical, no content
   moves). The classifier flags *any* logical forward ref; ~47
   prop/lemma-target callbacks + ~11 def-subject-matches-chapter are
   deliberate, not mis-homes. Edit the classifier waive logic per the waiver
   policy. This drops "62 actionable" → near-zero so the watcher stops
   reporting legitimate couplings as defects. Tables A/B in the triage doc
   are the inventory.

2. **3 genuine author-call `def→def` edges** — surface with evidence; do
   **not** auto-move (the `su2-generators` near-miss this session shows a
   usage-heuristic move can reverse a deliberate prior decision):
   - `lifting-and-descent::def:motivic-galois-character → mass-theory::def:adelic-substrate` — which is foundational?
   - `braids-and-knots::def:skein-resolution-obstruction → information-theory::def:computational-horizon` (+2 downstream edges to stochastic-mechanics `thm:qou-obstruction-reduction` and fluid-dynamics `prop:ns-obstruction-tower`) — does a braids def genuinely depend on an info-theory horizon, or should the edge drop?
   - `mass-theory::def:adelic-substrate → stochastic-mechanics::def:classical-limit-functor`

3. **The 1 edge the quark move surfaced**:
   `quark-antiquark-production (Ch9) → breit-wheeler-pair-production (Ch13)`.
   Either **waive** (Breit–Wheeler is a non-quark γγ→ℓ⁺ℓ⁻ process template;
   subject = the spectrum chapter) **or** also move
   `breit-wheeler-pair-production` to Ch9 for a tighter pair-production
   grouping. Author call. Was hidden before the move (both in Ch13).

### P2 — #1998 leftovers (noted open all session, unstarted)

4. Orphan re-homing · the two within-band advisory sections · compound base
   titles. (Section-title arc itself shipped: #1998, #2007, #2010; the CI
   hard-gate is in.)

### P3 — verify / deferred

5. **Sibling [#2020](https://github.com/litlfred/qou/pull/2020)**
   (predicted-spectra particle slice — `categorical-proton-unique`,
   `categorical-neutron-unique`, `antiparticle-crossing-reversal`,
   `integer-stability`, `baryon-product-from-alt`; disjoint from the quark
   blocks). A rebase heads-up was posted; `predicted-spectra.ts` changed
   under it. Confirm it rebases clean.
6. **Corpus QA staleness** — ~1071 stale blocks
   (`bun run content/pipeline/qa-staleness.ts content/quantum-observable-universe`),
   Lean-gated, owned by qa-drains #1918/#1941. Deferred.
