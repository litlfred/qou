---
name: groebner-basis
roles: [collaborator, owner]
description: >
  Compute Gröbner bases for non-commutative algebras (Hecke, braid group,
  TL category) using Singular letterplace or Python hecke_division.py.
  Reduce nuclear braid words, compute Markov traces, extract Q-values.
allowed-tools: Read Edit Bash Grep Glob Write Agent AskUserQuestion
---

# Gröbner Basis Skill

## Role

Compute non-commutative Gröbner bases and normal forms for algebraic
structures in the QOU framework: Hecke algebras, braid group algebras,
Temperley-Lieb categories. Apply to nuclear braid words for half-life
predictions.

## When to Use

- "reduce braid word" / "Gröbner reduce" / "normal form"
- "compute Hecke element" / "Markov trace"
- "nuclear braid" / "half-life from Hecke"
- "Singular computation" / "letterplace"
- "groebner basis for ..." / "division algorithm"

## Tools

### Singular (letterplace)
For exact symbolic computation over Q(q). Fastest for large A.

```bash
# Install
./scripts/setup-singular.sh

# Run
Singular computations/singular-nuclear-braid.sing
```

**Letterplace convention:**
- Ring: `(0,q), (x(1..n)), dp` then `makeLetterplaceRing(degbound)`
- Variables: `var((j-1)*ngens + i)` = generator x(i) at position j
- Multiplication: `lpMult(f, g)` (handles position shifting)
- Reduction: `reduce(f, G)` where G = `twostd(I)`
- Relations: Hecke `x(i)²=(q-q⁻¹)x(i)+1`, Yang-Baxter, far-comm

**Key functions:**
- `twostd(I)`: two-sided Gröbner basis
- `lpMult(f, g)`: letterplace multiplication
- `reduce(f, G)`: normal form modulo Gröbner basis

### Python (hecke_division.py)
For instrumented computation with step-by-step logging.

```python
from folio_assistant.computations.hecke_division import HeckeDivision, compute_nucleus
result = compute_nucleus(p=6, n=8, q_val=1.110)
```

**Key functions:**
- `HeckeDivision.nuclear_braid(p, n)`: build and reduce
- `HeckeDivision.reduce(elem)`: Gröbner reduction with logging
- `HeckeDivision.markov_trace(elem, n_strands)`: Markov trace
- `compute_nucleus(p, n)`: full computation with witness

### Python (nuclear-braid-level1.py)
Level 1 computation with 3 quark strands per nucleon.

```python
python3 computations/nuclear-braid-level1.py
```

## The Gröbner Basis

For the Hecke algebra H_A(q), the Gröbner basis G consists of:

1. **Hecke relation**: σ_i² = (q - q⁻¹)σ_i + 1
   - The ONLY energy-changing generator
   - Each application adds |c|·(q-q⁻¹) to the energy

2. **Yang-Baxter**: σ_iσ_{i+1}σ_i = σ_{i+1}σ_iσ_{i+1}
   - Energy-preserving (topological invariant)

3. **Far commutativity**: σ_iσ_j = σ_jσ_i for |i-j| ≥ 2
   - Energy-preserving (reordering)

The admissible system (B, <) uses positive braid monomials with
length-lexicographic ordering.

## Proven Results

- **Markov trace factorization**: tr(N̄) = Π_i (z·a_i + b_i) EXACT
- **Energy path-independence**: diamond lemma (confluence)
- **Only Hecke changes energy**: verified computationally
- **Generator volume decomposition**: O(A²) computation

## Witness Files

All computations produce witness JSON in `computations/`:
- `nuclear-braid-reduction.witness.json`
- `nuclear-markov-trace.witness.json`
- `nuclear-braid-level1.witness.json`
- `hecke-division.witness.json`
- `sage-nuclear-braid.witness.json` (when Sage available)

## Cross-References

- `unital-groebner-bases` paper: admissible system, division algorithm
- `prop:nuclear-groebner-reduction`: unique normal form
- `thm:groebner-shirshov-energy`: energy as invariant
- `thm:markov-trace-factorization`: exact factorization
- `prop:generator-volume-decomposition`: O(A²) computation
