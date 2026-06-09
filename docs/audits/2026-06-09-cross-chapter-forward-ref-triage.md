# Cross-chapter forward-reference triage (2026-06-09)

**Axis:** detangler integration-watch (`content-graph-analysis.py` H2 +
`forward_ref_classifier.py`). Read-only; no sidecar writes.
**Scope:** quantum-observable-universe paper, `origin/main` @ [PR #2016].

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
| **Documented prior decision** (don't reverse) | 1 | **waive** — `def:su2-generators` ([PR #823]) |
| **Logically-prior dep** (nucleon built-from quark) | 3 | **moved** — quark sector → particle-interactions, [PR #2021] |

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
     deliberately relocated by [PR #823]'s fit-section-chapter audit.*
   - **Else** (def subject ≠ chapter, no prior decision) → **move** the
     block triple earlier (the `commutative-qou` case).

## Table A — the 17 definition-target edges (move-candidates)

| src chapter :: block | → tgt chapter :: **def** | verdict |
|---|---|---|
| braids-and-knots :: def:so3-generators | brings-surface :: **def:su2-generators** | **waive** — [PR #823] prior decision |
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
| particle-interactions :: def:categorical-proton | predicted-spectra :: **def:down-quark** | **moved** — quark sector → particle-interactions (now intra-chapter) |
| particle-interactions :: def:categorical-meson | predicted-spectra :: **def:quark-antiquark-production** | **moved** — now intra-chapter |
| particle-interactions :: prop:four-term-pair-nucleon | predicted-spectra :: **def:quark-antiquark-production** | **moved** — now intra-chapter |
| quantum-observable-universes :: prop:qou-canonical-action | lifting-and-descent :: **def:yekutieli-lifting-condition** | **waive** — Yekutieli-lifting belongs in lifting-and-descent |

### The one genuinely-structural question: quark placement — RESOLVED (moved)
`particle-interactions` (Ch9, nucleons) defined protons/mesons that depended
on `def:down-quark` / `def:quark-antiquark-production` in `predicted-spectra`
(Ch13). A proton is *built from* quarks, so the quark definitions are
logically prior — yet predicted-spectra is the framework's "particle
spectrum" chapter where they lived. **Author decision (2026-06-09): move the
quark sector before the protons.** The 5-block quark sector — `up-quark`,
`up-quark-properties`, `down-quark`, `down-quark-properties`,
`quark-antiquark-production` — was relocated Ch13 → Ch9
(`particle-interactions/`, section *Nucleon derivation from pair production*,
inserted before `prop:four-term-pair-nucleon`). The three flagged edges are
now **intra-chapter** (no longer cross-chapter forward refs). See
*Resolution* below for the post-move detangler delta.

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

## Resolution — quark move + post-move detangler (2026-06-09)

**Done ([PR #2021]):** the 5-block quark sector moved Ch13
(`predicted-spectra`) → Ch9 (`particle-interactions`, *Nucleon derivation
from pair production*), placed before `prop:four-term-pair-nucleon` and the
proton/meson defs that consume it. `bun run validate` green (1 pre-existing
issue, unchanged).

**Detangler delta (`forward_ref_classifier.py --actionable-only`): 64 → 62.**

| edge | before | after |
|---|---|---|
| `categorical-proton → down-quark` | Ch9→Ch13 forward (flagged) | **intra-Ch9** ✓ resolved |
| `categorical-meson → quark-antiquark-production` | Ch9→Ch13 forward (flagged) | **intra-Ch9** ✓ resolved |
| `four-term-pair-nucleon → quark-antiquark-production` | Ch9→Ch13 forward (flagged) | **intra-Ch9** ✓ resolved |
| `quark-antiquark-production → breit-wheeler-pair-production` | hidden (both Ch13) | **Ch9→Ch13 forward (new, visible)** |
| `up-quark → conj:borromean-quark` | Ch13→Ch14 forward | Ch9→Ch14 forward (target is a *conjecture* → waive) |

Net −3 resolved, +1 surfaced ⇒ −2 (64→62). The one surfaced edge,
`quark-antiquark-production → breit-wheeler-pair-production`, is a
**waive-class** dependency: `breit-wheeler-pair-production` is the
general Breit–Wheeler γγ→ℓ⁺ℓ⁻ pair-production *template* (an electron-pair
process), not a quark block, and its subject belongs with the
spectrum/process material — same pattern as the ~11 def-subject-matches-
chapter waives in Table A. It was previously invisible because both blocks
sat in Ch13; the move makes the genuine quark→template dependency explicit.
**Left in place** (not auto-moved): the author's instruction was "move quark
before protons," and Breit–Wheeler is a distinct, non-quark process block.
Flag for a future call if a tighter pair-production grouping is wanted.

## Copilot review

**Copilot (2026-06-09):** low-confidence comments on PR-link rendering — the
reference-style `[PR #2016]` link was undefined, and several bare in-text
mentions (`@ #2016`, `(PR #823)`, `PR #823's`, `PR #823 prior decision`)
were not links. Fixed: reference definitions for `[PR #2016]`, `[PR #2021]`,
`[PR #823]` added below, and the bare in-text mentions converted to the
reference-style form. No reclassification of the triage verdicts (the review
accepted the classification and the isolated author-decision set).

[PR #2016]: https://github.com/litlfred/qou/pull/2016
[PR #2021]: https://github.com/litlfred/qou/pull/2021
[PR #823]: https://github.com/litlfred/qou/pull/823
