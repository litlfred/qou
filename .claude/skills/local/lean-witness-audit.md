---
name: lean-witness-audit
roles: [collaborator, owner]
description: >
  Audit Python computation scripts that produce witness statements for Lean
  formalization. Verify witnesses are complete, self-documenting, use paper
  notation, link to a content block, and emit Lean-compatible declarations.
  Detects staleness via script content hash and git commit SHA.
allowed-tools: Read Edit Bash Grep Glob
---

# Lean Witness Audit Skill

## Purpose

Audit Python computation scripts that produce witness statements
for Lean formalization. Ensure the witness output is complete,
self-documenting, uses paper notation, and maps directly to
Lean declarations.

## Unified Witness Infrastructure

### Python witness base (`witness_base.py`)

All new computation scripts should use the `WitnessBuilder` class:

```python
from witness_base import WitnessBuilder

w = WitnessBuilder("my-computation", engine="sympy")
w.set_description("Computes foo from bar")
w.set_content_block("prop:my-proposition")  # links to content block
w.add_assertion("Vol(4_1)", computed=2.0298, expected=2.0298,
                tolerance=1e-10, source="SnapPy")
w.add_parameter("q", q0)
w.add_data("extra_result", {"key": "value"})
w.save()  # → my-computation.witness.json
```

The builder automatically captures:
- **commitSha**: Git HEAD at computation time
- **scriptHash**: SHA-256 of the script file (for staleness detection)
- **scriptCommitSha**: Last commit that touched the script — provenance
  only, **not** a staleness signal (rebase-merge rewrites it; bean `qou-wsha`)
- **computedAt**: ISO 8601 timestamp
- **engine** / **engineVersion**: Computation engine info
- **assertions**: Structured pass/fail checks with tolerances
- **contentBlock**: Link to the content block this witnesses

### Staleness detection

A witness is **stale** when:
1. The script's content hash has changed since the witness was generated
2. The script's git commit SHA has changed since the witness was generated

Check staleness:
```bash
# Single witness
python3 witness_base.py check-stale my-computation.witness.json

# All witnesses
python3 witness_base.py check-all

# Unified audit (Lean + Python)
bun run scripts/witness-audit.ts
```

### Legacy witness migration

52 existing witnesses use ad-hoc JSON schemas. Only 1 uses the
structured `ComputationWitness` format. When modifying a legacy
computation script, migrate it to `witness_base.py`:

1. Replace manual `json.dump()` with `WitnessBuilder`
2. Add `w.set_content_block("label")` to link to the content block
3. Convert key results to `w.add_assertion()` calls
4. Move supplementary data to `w.add_data()`
5. Run the script to regenerate the witness with the new format

## When to invoke

- After any computation script that outputs `.witness.json` or
  `.lean.txt` files
- Before committing witness data
- When reviewing Gröbner basis computations for particle interactions

## Audit checklist

### 1. Notation compliance

- [ ] **No internal shorthand.** Every symbol must use the paper's
  notation:
  - `σ_i` not `s0`, `si`, or `sigma(0)`
  - `𝟏` not `1` or `identity` for the Hecke identity
  - `q − q⁻¹` not `HA` or `ha`
  - `s = q^½ − q^(−½)` not `S` or `S_skein`
  - `z = 1/(q^½ + q^(−½))` not `Z_m` or `z_markov`
  - `T_{r,s}` for torus knots, not `T23` or `T_29`
  - `𝔭` for proton, `𝔫` for neutron, `e⁻` for electron
  - `𝒩(Z, N)` for nucleus, `𝒜(Z, N)` for atom
  - `⋈` for Hopf link, not `bowtie` or `*`

- [ ] **Paper references.** Every formula must cite the content
  block it comes from:
  - `def:stable-nucleus` for atom definition
  - `prop:beta-decay-transfer-matrix` for crossing coefficients
  - `prop:nuclear-groebner-reduction` for Gröbner NF
  - `prop:shell-closure-normal-form` for palindromic histograms
  - `def:beta-decay-skein` for the T_{3,5} weak vertex

### 2. Completeness

- [ ] **All inputs stated.** The witness must list:
  - The substrate parameter q and all derived constants
  - The Gröbner basis (ideal I) with all three relations
  - All crossing coefficients with their pair types
  - The construction order (which particle added at which step)

- [ ] **Every reduction step shown.** For each multiplication:
  - The input crossing element (in paper notation)
  - The element BEFORE reduction (the raw product)
  - Which Gröbner rules fired (Hecke, YB, far-comm)
  - The Hecke energy cost of each step
  - The element AFTER reduction (the new normal form)

- [ ] **Final normal form.** Must include:
  - All terms with coefficients in the Hecke basis
  - The Markov trace (with strand count)
  - Total Hecke energy
  - Total reduction step count (Hecke + YB + far-comm)
  - Torus knot identification (if the NF matches a known knot)

### 3. Lean compatibility

- [ ] **Declarations.** The witness must include Lean-compatible
  output:
  - `def <name>_nf : HeckeAlgebra n q := ...`
  - `theorem <name>_is_groebner_nf : is_groebner_nf (<name>_nf) := by ...`
  - `theorem <name>_markov_trace : markov_trace n <name>_nf = <value> := by ...`

- [ ] **Types match.** The Lean declarations must use types from
  `QOU.Descartes.TransferMatrix` and `QOU.Descartes.BetaDecay`.

- [ ] **Witness JSON structure.** The `.witness.json` must have:
  - `computation`: string identifier
  - `timestamp`: ISO 8601
  - `parameters`: all q-derived constants
  - `ideal`: the Gröbner basis relations
  - `crossing_types`: all pair types with (c, d) coefficients
  - `steps`: array of step-by-step reductions
  - `normal_form`: the final NF with all metadata

### 4. Natural vs synthetic

- [ ] **Formation path.** State whether the atom is "natural"
  (stellar nucleosynthesis, Big Bang) or "synthetic" (accelerator).
  
- [ ] **q-torsion note.** For synthetic atoms, note that the
  initial braid word may differ from the natural one due to
  high-energy formation conditions, potentially giving different
  q-torsion in the Gröbner reduction.

- [ ] **Ordering dependence.** If the construction order affects
  the result (different braid words for different orderings),
  document ALL orderings tested and which one gives the minimum
  energy (= the physical atom).

### 5. Particle decomposition

- [ ] **Torus knot basis.** Decompose the normal form over the
  catalog of embeddable torus knots on Σ₄:
  - T_{2,1}, T_{2,2}, T_{2,3}, T_{2,5}, T_{2,7}, T_{2,9}
  - T_{3,1}, T_{3,2}, T_{3,3}, T_{3,4}, T_{3,5}
  - unknot (identity)

- [ ] **Physical labels.** Each torus knot coefficient must have
  a physical interpretation:
  - T_{2,1}: single Hopf crossing
  - T_{2,2}: Hopf link ℒ_H (baryon binding)
  - T_{2,3}: electron / trefoil
  - T_{2,5}: shell-2 binding
  - T_{2,7}: shell-3 binding
  - T_{2,9}: shell-5 / degree-2 binding
  - T_{3,4}: degree-2 binding
  - T_{3,5}: weak vertex (beta decay mediator)
  - unknot: vacuum / neutrino

- [ ] **Residual.** State the decomposition residual norm.
  If > 10⁻⁸, the NF has components NOT in the torus knot
  basis — these are genuinely new knot types from the
  particle interactions.

## Failure modes

- **Abbreviated notation**: Using `s0` instead of `σ₀` makes
  the witness unreadable outside the computation context.
  
- **Missing inputs**: A witness without the Gröbner basis
  stated cannot be verified independently.

- **No Lean output**: The computation is not formalized unless
  it produces Lean-compatible declarations.

- **Silent reductions**: If a Hecke step happens but isn't
  logged, the energy accounting is wrong.
