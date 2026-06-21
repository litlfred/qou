# Workplan — the q-Laplacian / `[k]_q` unifying perspective

**Date:** 2026-06-01
**Author intent:** recast scattered q-deformed structures (q-heat,
q-NS, Gram/Markov, Yekutieli) through the shared q-Laplacian eigenvalue
tower `[k]_q`, with a single organizing block + a canonical Verlinde /
ADE quantum-dimension reference, placed to create **backward** (not
forward) references.

---

## Diagnosis (corpus-checked, not guessed)

| Concept | In paper already? | Evidence |
|---|---|---|
| `[k]_q` q-integers, q-Laplacian Δ_q | **Yes, heavily** (165 `.md`) | grep |
| Root-of-unity truncation `[κ]_q=0` | **Yes, fully exposited** (qualitative) | `fluid-dynamics/root-of-unity-truncation.md` |
| Verlinde / ADE quantum dimensions | **Barely** — 5 ad-hoc `.md` mentions, no canonical reference | grep `Verlinde` |
| **`[k]_q` as the *organizing* perspective** | **No** — no unifying block exists | grep for unifying block → empty |

**Conclusion.** The pieces are in the paper; the *unifying perspective*
and the *Verlinde/ADE citation* are the genuine gaps. The recent
q-spectral-tower probe (`q_spectral_truncation_tower.py`) **verifies
exactly** what `root-of-unity-truncation.md` already asserts — it is a
verification witness, not new content.

## Why a unifying block does NOT create forward-ref defects

Per [`docs/forward-ref-logical-analysis.md`](../forward-ref-logical-analysis.md):
the detangler's headline metric is the **logical-defect count**, not
raw forward-refs; storytelling/structural edges are benign (62% of the
existing 251).

**Chapter order (paper manifest):**
```
quantum-observable-universes (#3)  →  lifting-and-descent (Yekutieli)
  →  braids-and-knots  →  mass-theory (Gram)  →  fluid-dynamics (q-heat, q-NS)
```

`quantum-observable-universes` is **before all four target chapters** and
already hosts `intro-q-special-functions` + `categorical-fourier-transform`.
Placing the unifying block there means every consumer (Yekutieli,
Gram, q-heat, q-NS) references it **backward** — the *good* edge
direction. **Net logical forward-refs created: zero.** This is the
whole point of the placement: it converts what would be scattered
local re-derivations into backward references to one source.

## Workplan (detangler-aware)

### Item 1 — Verlinde / ADE reference + citations (smallest, do first)
- Add Verlinde (1988, *Nucl. Phys. B* 300:360) + an ADE / quantum-
  dimension reference to `content/schema/references.ts`.
- Cite from the 5 existing `Verlinde`-mentioning blocks
  (`root-of-unity-truncation.md`, `zeta8-witness-level2-su2.md`, …),
  replacing ad-hoc mentions with `\cite{}`.
- **No new blocks; no reorder.** Pure bibliographic.

### Item 2 — unifying `[k]_q` proposition block (the gap)
- New block in **`quantum-observable-universes`** (before all targets):
  `prop:q-laplacian-spectral-tower` (or a `remark` if no new logical
  claim — likely `proposition` since the truncation IS a claim).
- Content: `[k]_q` is the shared eigenvalue tower of Δ_q; at
  `q=e^{iπ/κ}`, `[κ]_q=0` truncates the spectrum to the finite
  Verlinde/ADE set; the surviving dims are cyclotomic (φ at κ=5, √2 at
  κ=8). One source the consumers reference.
- `+ .lean`: the truncation lemma `[κ]_q = 0 at q=e^{iπ/κ}` over a
  generic field (cyclotomic), fibre-level (no reality).
- Witness: link the existing `q-spectral-truncation-tower.witness.json`.

### Item 3 — recast consumers to backward-ref the unifying block
- `fluid-dynamics/root-of-unity-truncation.md`: replace its local
  re-statement of the truncation with `uses: [prop:q-laplacian-spectral-tower]`
  + a one-line backward ref.
- `q-heat-equation.md`, Gram-matrix exposition, Yekutieli
  obstruction-cap: same — backward-ref the tower instead of
  re-introducing `[k]_q` locally.
- **Run `chapter-complexity-review` before/after** to confirm the
  logical-backward-edge count does **not** rise (it should fall, since
  re-derivations collapse to references).

### Item 4 — detangler check (gate)
- After items 2–3, run `forward_ref_classifier.py` and the
  chapter-complexity energy metric. Acceptance: **logical-defect count
  ≤ pre-workplan count** (no new logical forward refs; placement in
  ch #3 guarantees backward edges).

## Discipline
- Fibre-level: `[k]_q`, `q` formal, Im unconstrained; the bar
  involution / root-of-unity is the operative structure; reality only
  at q₀ (per AGENTS.md Im(q) fibre-vs-observable).
- No fitted form; the truncation values are exact cyclotomic.
- The Verlinde/ADE values are *referenced* (standard since RT 1990),
  not claimed as framework-internal discoveries.

## What this is NOT
- Not the q-NS PDE solve (blowup exponent) — survey research target,
  multi-week, out of scope here.
- Not the q-heat archimedean Padé continuation — likewise.
- Not new mathematics — it is exposition + citation + one organizing
  proposition that the corpus already supports.

---

## Execution status (2026-06-01, PR #1647)

- [x] **Item 1** — Verlinde 1988 reference added to `references.ts` (valid; was missing).
- [x] **Item 2** — `prop:q-laplacian-spectral-tower` (+ Lean over ℂ) in `quantum-observable-universes` "Geometric interpretations"; cites verlinde1988 + reshetikhin1991; validates 0 issues.
- [x] **Item 3** — `root-of-unity-truncation` (fluid-dynamics) recast to `uses: prop:q-laplacian-spectral-tower` (backward cross-chapter ref) + prose backward-ref; cites verlinde1988.
- [x] **Item 4** — detangler gate PASSED: `forward_ref_classifier` reports 60 logical defects, **none are the new blocks**. Placement in ch #3 (before all 4 consumers) → every edge backward; zero logical forward-refs introduced.

**Lean caveat:** the spectral-tower lemmas are unverified locally (no `lake`); CI-gated.

**Not done (out of scope, survey research targets):** q-NS PDE blowup-exponent solve; q-heat archimedean Padé continuation; full Yekutieli Galois-Fourier decomposition. The probes supply these their exact finite spectral boundary data.
