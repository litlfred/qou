# Proposal — collapse mass-binding & β-decay into the one complex-volume story

**Date:** 2026-06-16 · **PR:** #2346 · **Status:** PROPOSAL (not executed)
**Driver:** `conj:binding-qbeta-complex-volume` —
`𝔙(K) = E₀·tr_M((Π_free−1)∘𝓜) ∈ ℂ`, `Re 𝔙 = 𝔈_bind` (binding),
`Im 𝔙 = 𝔔_β` (β-decay Q-value). Binding and decay are **two real shadows
of one complex object**, not two stories. The block's authorNote flags
this reorg as a tracked follow-up.

## The "two disjoint stories" defect (evidence)

The paper currently treats binding and β-decay as **parallel narratives**:

- **`mass-theory`** has a standalone subsection **"The `𝔔_β` precision
  ladder"** (`sec:mass-algebraic-qbeta-ladder`) — Q_β as its own artifact;
  binding lives separately in the physical-face "tower binding energy".
- **`observations`** has standalone sections **"Beta decay: mechanism,
  half-life, tritium"** and **"Beta decay: magic-shell consequences"** —
  no link to binding or to a shared object.
- **`appendix-qvalues`** ("Q-Value Predictions from q") is a separate
  appendix from `appendix-mass-binding-algorithms`.
- The unification `conj:binding-qbeta-complex-volume` sits in
  `mass-endomorphism` but is **not woven into the narrative** — stated, not
  used to reframe the two channels as one.

Nowhere does the paper say: *compute `𝔙(K)` once; binding = Re, Q_β = Im.*

## Proposed reorganization (before → after, high level)

| Locus | Before | After |
|---|---|---|
| `mass-endomorphism` | `conj:binding-qbeta-complex-volume` stated in isolation | **New section** "The complex volume `𝔙`: binding and decay as Re/Im" — introduces `𝔙`, the bar-parity→Re/Im split, the fibre-level caveat, the Stage-B Re/Im corroboration |
| `mass-theory` algebraic face | subsec "The `𝔔_β` precision ladder" | **rename** → "Complex-volume precision ladder: Re(`𝔙`) & Im(`𝔙`)" + a 1-block intro framing Q_β as Im(`𝔙`) (blocks unchanged) |
| `mass-theory` physical face | "Physical face: mass formulas and predictions" (binding only) | **rename** → "…complex-volume observables (Re and Im)"; note Im(`𝔙`)=Q_β alongside binding |
| `observations` | two "Beta decay: …" sections | **reframe** section intros to "Q-values as Im(`𝔙`)" / "magic-shell structure & complex-volume consequences" (blocks unchanged) |
| `appendix-qvalues` | standalone "Q-Value Predictions" | **rename** → "Imaginary part of the complex volume — Q-values from q" (intro added; content unchanged) |

The `bar-parity-split` block + `substrate-cohomology-calibration-story`
get a narrative **inversion**: cosh/sinh become *derivative* of Re/Im `𝔙`
(currently the parities are assigned to observables after the fact; the
"pinning one constrains the other" line becomes a direct consequence of
complex structure).

## Ranked edit list

**Cheap / low-risk (renames + new intro prose; no block moves, no Lean):**
1. New `mass-endomorphism` section + intro block introducing `𝔙` (Re/Im).
2. Rename the `mass-theory` `𝔔_β`-ladder subsection → complex-volume ladder + 1-block intro.
3. Rename `mass-theory` physical-face section title + 1-block intro.
4. Reframe the two `observations` β-decay section titles + intros.
5. Rename `appendix-qvalues` → `appendix-im-complex-volume` (`git mv` + manifest title + intro).

**Medium (prose bridges; still no derivation changes):**
6. `bar-parity-split` + `substrate-cohomology-calibration-story` narrative inversion (cosh/sinh ← Re/Im `𝔙`).
7. Optional 3-column reference table: nucleus | Re `𝔙` (binding) | Im `𝔙` (Q_β).

**Must NOT change:** the proven Lean (`ComplexVolumeMatch`, sorry-free); the
three-calibration discipline placement; the transfer-matrix/Markov machinery;
the witness-backed observation tables; `mba-step11-q-beta-truncation` (compute
bridge — needs a compute-pipeline audit before any move).

## Risk / scope

- Mostly **prose + renames** → low risk; the value is narrative coherence, not
  new math. No derivation rewrites.
- **Label renames** (`sec:…`) ripple to cross-refs (Lean `lean.ref` is
  unaffected — only section URIs change). Run the detangler after to catch
  forward-ref breaks; record renames in a reorganization map.
- Estimate: a focused 1–2 session pass (renames + ~6–10 new intro blocks +
  a one-voice sweep), gated on owner go.

## Decisions on the adjacent `𝔙`-simplification items (this session)

- **Stage-B "two c₂" reframe (HIGH):** done — net-route = Re `𝔙`, brane-tower
  = Im `𝔙`; expected, not anomalous. Two keystones (`R`, `F`) collapse to one
  complex `𝔙` search. (`2026-06-16-hoefsmit-stage-b-attempt-verdict.md` §reframe;
  `2026-06-10-…-synthesis.md` §8.)
- **Lean `ComplexVolumeMatch` unification (HIGH):** done — one `measured_volume`
  + one `volume_match`; binding/Q_β derived as Re/Im.
- **Reeb sinh/cosh recurrence "dedup" (MED): DECLINED.** The two theorems
  (`reeb_tower_sinh_three_term`, `…_cosh_…` in `QOU/QBeta/ReebTowerJacobiAnger.lean`)
  are **1-line proofs each** (`rw [sinh_add, sinh_sub]; ring`), and the file's
  docstring **already** states the unification ("the rotation tower and the
  growth tower solve one operator `p_{k+1}=2t·p_k−p_{k−1}`"). Parameterising
  over the function would add typeclass overhead for ~zero line savings and risk
  a sorry-free proof — not worth it. Already clear.
- **#5 narrative inversion + LOW cross-refs:** folded into this reorg (items 6
  above) rather than scattered now — piecemeal edits would be re-done by the
  reorg.

## Open questions for the owner

- Keep `appendix-qvalues` as a renamed "Im(`𝔙`)" appendix vs merge into
  `mass-theory` physical face? (Proposal: rename — lower risk.)
- "Complex volume" only in section titles; keep "binding"/"Q-value" in block
  titles for clarity? (Proposal: yes.)
- Greenlight to execute (and on which branch)?
