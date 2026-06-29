# e5tn — cross-chapter-forward triage (detangler watcher), 2026-06-29

**Bean:** `e5tn` — *Integration: detangler watcher — cross-chapter-forward (12 items).*
**Verdict:** all 12 chapter-pair aggregates → `wontfix: architectural`; the 2 genuine
corpus-wide logical forward-ref defects are fixed (subject-matched waive of
`def:q-flat-connection`), bringing actionable logical forward-refs to **0**.

## What the 12 items are

Each of the 12 `cross-chapter-forward` queue items is an **H2 chapter-pair aggregate**
(severity `minor`, "baseline architectural coupling existing on main"), not an individual
defect. They are the highest forward-edge-count chapter pairs:

| id | chapter pair | fwd edges | class |
|----|--------------|-----------|-------|
| 69cc59f87d2e | Ch 9 (Particle Interactions) → Ch 11 (Mass Analysis) | 23 | result-callback (mass cluster) |
| db3f8eac3c34 | Ch 11 (Mass Analysis) → Ch 13 (Predicted Spectra) | 17 | result-callback (mass cluster) |
| 728a488af21a | Ch 8 (Mass Endomorphism) → Ch 11 (Mass Analysis) | 15 | result-callback (mass cluster) |
| 3f7f29d8d96c | Ch 3 (QOUs) → Ch 4 (Models of QOUs) | 10 | framing chapter (`models-of-qous` waived wholesale) |
| 711efc620558 | Ch 6 (Braids and Knots) → Ch 7 (Bring) | 8 | foundational coupling (Bring) |
| de869f9e2c76 | Ch 11 (Mass Analysis) → Ch 14 (Physical Observations) | 8 | result-callback (mass cluster) |
| ef5f939989b5 | Ch 7 (Bring) → Ch 13 (Predicted Spectra) | 7 | result-callback (mass cluster) |
| 0f47a0f27c0b | Ch 7 (Bring) → Ch 9 (Particle Interactions) | 5 | foundational coupling (Bring) |
| 799edb7a3f23 | Ch 3 (QOUs) → Ch 7 (Bring) | 5 | foundational coupling (Bring) |
| eb05151e5a9e | Ch 14 (Physical Observations) → Ch 17 (Fluid Dynamics) | 5 | result-callback |
| 1c7d0900bd45 | Ch 9 (Particle Interactions) → Ch 14 (Physical Observations) | 4 | result-callback (mass cluster) |
| 50a557937fdd | Ch 7 (Bring) → Ch 10 (q-Hyperbolic Geometry) | 4 | foundational coupling (Bring) |

## Grounding: `forward_ref_classifier.py` over the whole corpus

```
Forward references: 313 total
  LOGICAL DEFECT     2  (actionable — reader must rely on future content)
  logical-waived    68  (surreal lift / FOUNDATIONAL_LATE — sanctioned)
  storytelling     195  (motivation / interpretation / cite — benign)
  structural        48  (appendix / framing chapter — benign)
```

The 12 aggregates are dominated by `storytelling` (`T-narrative`/`T-cite`) and `structural`
(`S-framing`/`S-appendix`) edges:

- **Mass cluster** (Ch 8/9/11/13/14/17): a derivation in an early mass chapter forward-
  references where its *consequence* is computed (`L-result-callback` / `T-narrative`) — the
  deliberate, sanctioned coupling pattern the detangler skill records as
  `wontfix: architectural` (a paper legitimately says "we will use this in the mass analysis").
- **Bring foundational coupling** (Ch 6/7 → later): the Bring's-surface chapter is a
  foundational object referenced forward into the physics chapters — peer of the existing
  `brings-surface::*` subject-matched waivers.
- **Framing chapter** (Ch 3 → Ch 4): `models-of-qous` is a `FRAMING_CHAPTER`, waived wholesale.

None of the 12 chapter pairs is the home of an actionable defect — the 2 `LOGICAL DEFECT`
edges live in a different pair (Ch 3 → q-geometric-langlands, below). So **all 12 →
`wontfix: architectural`** stands on the classifier evidence.

## The 2 actionable logical defects — fixed

Both target `q-geometric-langlands/def:q-flat-connection`:

- `quantum-observable-universes/conj:q-harmonic-flow` → `def:q-flat-connection`
- `quantum-observable-universes/prop:germ-commutator-q-curvature` → `def:q-flat-connection`

**Resolution: subject-matched waive** (`SUBJECT_MATCHED_DEFS`), not a mis-home:

- `def:q-flat-connection`'s subject — the flat connection / local system — is the core object
  of geometric Langlands, so it belongs in its `q-geometric-langlands` home chapter (the
  documented `SUBJECT_MATCHED_DEFS` test: "does the definition's subject match its home?").
- Corroborated by `germ-commutator-q-curvature`'s own `authorNote`: the identity
  `[δq₁,δq₂]=F_q` is verified **independently** over an abstract ring; the
  `F_q ↔ q-flat-connection` identification is *"narrative"* (the def-cone is conjecture-free,
  def↔def with `q-local-system`). The early `uses[]` edge is a deliberate narrative coupling.
- It is **not** among the 3 edges the classifier deliberately leaves actionable for an author
  call (`skein→computational-horizon`, `embeddable-knot-operator→covalent-bond-types`,
  `quark-antiquark→breit-wheeler`).

After the waive: `LOGICAL DEFECT 2 → 0`, `L-subject-matched 12 → 14`. The author's `uses[]`
edge is **preserved** — only the classifier finding is waived.

## Disposition

- 12 queue items: already `status=wontfix, reason="converted to bean: e5tn"`; this audit is
  the recorded triage decision → all `wontfix: architectural`.
- `computations/forward_ref_classifier.py`: `def:q-flat-connection` added to
  `SUBJECT_MATCHED_DEFS`.
- Bean `e5tn` ready to close (human-only, §4a).
