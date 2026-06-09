# Cross-chapter forward-reference triage (2026-06-09)

**Axis:** detangler integration-watch (`content-graph-analysis.py` H2 +
`forward_ref_classifier.py`). Read-only; no sidecar writes.
**Scope:** quantum-observable-universe paper, `origin/main` @ #2016.

## TL;DR — the "64 defects" right-sizes to ~4 real questions

The classifier reports **64 logical-defect** cross-chapter forward edges
(of 244 raw: 131 storytelling + 43 structural + 5 already-waived are
correctly excluded). On per-edge triage, **almost all 64 are legitimate
forward couplings, not mis-homes**:

| Bucket | Count | Disposition |
|---|---|---|
| Target is a **prop / lemma / cor** (deliberate forward callback) | 47 | **waive** |
| Target is a **definition whose subject = its own chapter** | ~11 | **waive** (def belongs there) |
| **Genuine mis-home** (def subject ≠ chapter) | 1 | **moved** — `def:commutative-qou`, [PR #2016] |
| **Documented prior decision** (don't reverse) | 1 | **waive** — `def:su2-generators` (PR #823) |
| **Genuinely ambiguous** — needs author call | ~2–4 | **author triage** (quark placement) |

So the actionable surface is **~2–4 edges**, not 64. The detangler's
"logical defect" label flags *any* logical forward reference; it does not
distinguish "the def is mis-homed" from "the def belongs in its later
chapter and is referenced forward on purpose."

## Triage rule used

For each `src_chapter :: src_block → tgt_chapter :: tgt_block` (src earlier
than tgt):

1. **Target is not a `definition`** (prop/lemma/cor) → **waive**. A
   proposition/lemma is proved where it lives; an earlier block citing it
   forward is a deliberate narrative callback, not a placement error.
2. **Target is a `definition`** → candidate move, but first:
   - **Does the def's *subject* match its current (later) chapter?**
     (`briggs-klein-chart` ↔ brings-surface; `adelic-substrate` ↔
     mass-theory; `operational-entropy` ↔ information-theory;
     `yekutieli-lifting-condition` ↔ lifting-and-descent). If yes →
     **waive** (it belongs there; the earlier user forward-references it).
   - **Check for a prior relocation decision** (grep the manifests for a
     `// <block> relocated … (PR #NNN …)` comment). If present → **waive**
     (do not reverse a considered placement). *This caught `su2-generators`,
     deliberately relocated by PR #823's fit-section-chapter audit.*
   - **Else** (def subject ≠ chapter, no prior decision) → **move** the
     block triple earlier (the `commutative-qou` case).

## Table A — the 17 definition-target edges (move-candidates)

| src chapter :: block | → tgt chapter :: **def** | verdict |
|---|---|---|
| braids-and-knots :: def:so3-generators | brings-surface :: **def:su2-generators** | **waive** — PR #823 prior decision |
| braids-and-knots :: prop:lagrange-resolvent-transform | brings-surface :: **def:brings-surface** | **waive** — the Bring's-surface def belongs in brings-surface |
| braids-and-knots :: def:skein-resolution-obstruction | information-theory :: **def:computational-horizon** | **author** — does a braids def depend on an info-theory horizon, or should the dep drop? |
| brings-surface :: prop:mi-sw-abelianisation | mass-endomorphism :: **def:mass-identity** | **waive** — mass-identity belongs in the mass chapter |
| brings-surface :: prop:torus-knot-generators | particle-interactions :: **def:knot-particle-generation** | **waive** — belongs in particle-interactions |
| lifting-and-descent :: cor:quantum-dilogarithm | brings-surface :: **def:briggs-klein-chart** | **waive** — Bring's-surface chart belongs in brings-surface |
| lifting-and-descent :: prop:blowup-yekutieli | brings-surface :: **def:local-cohomology-group** | **waive** — cohomological-defect concept belongs in brings-surface |
| lifting-and-descent :: def:motivic-galois-character | mass-theory :: **def:adelic-substrate** | **author** — def→def across chapters; check which is foundational |
| mass-theory :: def:categorical-transfer-matrix | information-theory :: **def:operational-entropy** | **waive** — entropy belongs in info-theory |
| mass-theory :: prop:transfer-matrix-level-independence | measurement-observation :: **def:bundle-isotopy-equivalence** | **waive** — belongs in measurement-observation |
| mass-theory :: def:adelic-substrate | stochastic-mechanics :: **def:classical-limit-functor** | **waive** — classical-limit belongs in stochastic-mechanics |
| particle-interactions :: def:confinement-level | climax-volume-mass :: **def:knot-operator-energy** | **waive** — energy belongs in q-hyperbolic geometry |
| particle-interactions :: prop:confinement-level-unique | climax-volume-mass :: **def:local-shadow-ordering** | **waive** — belongs in climax-volume-mass |
| particle-interactions :: def:categorical-proton | predicted-spectra :: **def:down-quark** | **author** — quark placement (see below) |
| particle-interactions :: def:categorical-meson | predicted-spectra :: **def:quark-antiquark-production** | **author** — quark placement |
| particle-interactions :: prop:four-term-pair-nucleon | predicted-spectra :: **def:quark-antiquark-production** | **author** — quark placement |
| quantum-observable-universes :: prop:qou-canonical-action | lifting-and-descent :: **def:yekutieli-lifting-condition** | **waive** — Yekutieli-lifting belongs in lifting-and-descent |

### The one genuinely-structural question: quark placement
`particle-interactions` (Ch9, nucleons) defines protons/mesons that depend
on `def:down-quark` / `def:quark-antiquark-production` in `predicted-spectra`
(Ch13). A proton is *built from* quarks, so the quark definitions are
logically prior — yet predicted-spectra is the framework's "particle
spectrum" chapter where they currently live. **Author call:** either the
quark definitions move to a shared earlier location (before nucleons), or
this is an accepted forward pointer to the spectrum chapter. This is the
only cluster where the move-vs-waive answer is non-obvious.

## Table B — the 47 prop/lemma-target edges → waive

All have a non-definition target (a proven result cited forward). Grouped
by chapter pair (count): mass-endomorphism→mass-theory (9),
particle-interactions→mass-theory (6), mass-theory→observations (5),
braids-and-knots→mass-theory (3), brings-surface→particle-interactions (3),
mass-theory→predicted-spectra (3), predicted-spectra→molecular-construction
(2), + 16 single-edge pairs. These are deliberate forward callbacks to
later *results* (consumption coupling — e.g. mass-theory "consumes
particles"), not placement errors.

## Worked precedents (this session)

- **Move (done):** `def:commutative-qou` — a QOU-axioms definition
  ("a QOU is strictly commutative when μ∘c = μ…") mis-homed in
  particle-interactions's varying-Euler section, used by `prop:u1-equivariant-reduction`
  in the QOU chapter. Moved Ch9→Ch3 ([PR #2016]); classifier 65→64.
- **Waive (not moved):** `def:su2-generators` — usage (4× braids-and-knots
  vs 1× brings-surface) *looked* like a mis-home, but the braids manifest
  documents `// su2-generators relocated to archimedean-universe/ (PR #823
  fit-section-chapter audit)`. Reversing that is wrong → waive.

## Recommendation

1. **Waive the ~60 legitimate couplings** (Tables A-waive + B). If desired,
   record them in the detangler waive-list so the axis stops reporting
   them as logical defects (one mechanical pass; no content moves).
2. **Author triages the quark-placement cluster** (3 edges) +
   `motivic-galois-character→adelic-substrate` + `skein-resolution-obstruction
   →computational-horizon` (2 edges) — the only genuine move-vs-waive calls.
3. **The detangler integration-watcher handles new cross-chapter edges
   incrementally** going forward (it already gates them on PRs).
4. **Do not grind blind cross-chapter moves** — `su2-generators` shows a
   usage-heuristic move can reverse a deliberate prior decision. Always
   check the def's subject-vs-chapter and prior-relocation comments first.

## Copilot review

Requested on the carrying PR; reviewer feedback + any reclassification will
be appended here.
