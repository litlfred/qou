# Witness Architecture: Lean Integration + Binary Release

## Design goals

1. **Any isotope queryable**: given (Z, N), retrieve exact NF in q
2. **Lean-verified**: correctness checked by Lean, not trusted from Rust
3. **Scalable**: works for A=3 (tritium) through A=294 (oganesson)
4. **Content-integrated**: each witness is a content block triple

## Architecture

```
                    ┌─────────────────┐
                    │  hecke-engine    │  Rust: fast computation
                    │  (v8/v9/modular)│  Produces witness + certificate
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │  Certificate    │  JSON: NF polynomials +
                    │  (per isotope)  │  strand-by-strand trace
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
     ┌────────▼───────┐ ┌───▼────┐ ┌───────▼───────┐
     │ .lean witness  │ │ .ts    │ │ .md           │
     │ (Lean 4 defs + │ │ block  │ │ human-readable│
     │  verification) │ │ manifest│ │ polynomial    │
     └────────────────┘ └────────┘ └───────────────┘
```

## Certificate format

Each isotope produces a certificate with:

```json
{
  "isotope": { "Z": 27, "N": 33, "A": 60, "symbol": "Co" },
  "engine": { "version": "0.9.0", "commit": "abc1234" },
  "polynomials": {
    "tr_alt": [[exp, "coeff"], ...],
    "net":    [[exp, "coeff"], ...],
    "observable": [[exp, "coeff"], ...],
    "color":  [[exp, "coeff"], ...]
  },
  "strand_trace": [
    { "strand": 1, "n_words": 1, "checksum": "sha256..." },
    { "strand": 2, "n_words": 2, "checksum": "sha256..." },
    ...
  ],
  "pn_count": 792,
  "f_pauli_f64": 0.0042,
  "computed_at": "2026-04-05T01:00:00Z"
}
```

## Lean verification strategy

### Tier 1: Full verification (A ≤ 12)

The witness Lean files define exact `LaurentPolynomial ℤ` values.
Lean can verify by direct computation:

```lean
-- Already exists in PauliWitness/witness-8be.lean
def tr_alt_8Be : LaurentPolynomial ℤ := C 93 * T^54 + ...
def net_8Be : LaurentPolynomial ℤ := C 127 * T^111 + ...
```

Lean compilation checks the polynomial is well-formed.
`#eval` can evaluate at any q.

### Tier 2: Strand-by-strand verification (12 < A ≤ 60)

The full polynomial is too large for Lean source. Instead:

```lean
import QOU.Descartes.GroundRing
import QOU.Descartes.TransferMatrix

namespace QOU.Descartes.PauliWitness

-- The witness is loaded from a binary file (Lean FFI or #eval)
-- Verification: replay the strand construction one strand at a time

/-- Verify that extending NF at strand k by crossing (i,k+1) and
    reducing gives the claimed NF at strand k+1.
    This is a finite check on bounded data. -/
def verifyStrand (nf_k : List (HeckeWord × LaurentPolynomial ℤ))
    (crossing : VertexType)
    (nf_k1 : List (HeckeWord × LaurentPolynomial ℤ)) : Bool :=
  let extended := extendAndReduce nf_k crossing
  let stripped := applyQuotientIdeals extended
  stripped == nf_k1

/-- Full verification: check all strands sequentially. -/
def verifyWitness (config : NuclearConfig)
    (strands : List (List (HeckeWord × LaurentPolynomial ℤ))) : Bool :=
  strands.zip (strands.tail).all fun (nf_k, nf_k1) =>
    verifyStrand nf_k (nextCrossing config) nf_k1

end QOU.Descartes.PauliWitness
```

Key insight: each strand verification is independent and bounded.
For A=60 with 59 strands, each strand check involves ~A words.
Total verification: O(A²) — minutes in Lean.

### Tier 3: Checksum verification (A > 60)

For very heavy isotopes, even strand-by-strand is slow. Use:

```lean
/-- The witness polynomial matches the claimed SHA-256 checksum.
    The checksum was verified by running the Rust engine twice
    with different random seeds (probabilistic verification). -/
axiom witness_checksum_verified :
  sha256 (serialize witness_210Bi) = "a1b2c3..." 
  -- Ref: [hecke-engine v0.9.0, commit abc1234]
```

This is honest: the axiom says "this data was computed by the engine
and checksummed". The engine itself is verified on small cases.

## Content block structure

Each witness is a content block triple:

```
content/quantum-observable-universe/appendix-witnesses/
  witness-<isotope>.ts     ← Manifest: label, engine ref, uses
  witness-<isotope>.md     ← Human-readable polynomial display
  witness-<isotope>.lean   ← Lean definitions + verification tier
```

### Manifest (.ts)

```typescript
import { definition } from "../../schema/builders";

export default definition({
  label: "def:witness-8be",
  title: "Pauli witness for ${}^8\\mathrm{Be}$ (exact in $q$)",
  tags: ["pauli-witness", "beryllium-8", "exact-polynomial"],
  lean: {
    decl: "QOU.Descartes.PauliWitness.witness_8Be",
    file: "witness-8be.lean",
  },
  witness: {
    engine: "hecke-engine",
    version: "0.8.0",
    commit: "abc1234",
    a: 8, z: 4, n: 4,
    f_pauli: 0.3677,
    verification: "full",  // "full" | "strand" | "checksum"
  },
  uses: [
    "def:hecke-normal-form",
    "prop:shell-closure-normal-form",
  ],
});
```

### Narrative (.md)

```markdown
The Pauli witness for ${}^8\mathrm{Be}$ (Z=4, N=4, A=8) is the
exact Gröbner normal form in $H_8(q)$ after quotient ideals $I_8 + I_9$.

$$
  F_{\mathrm{Pauli}}^{(8)} = \frac{|\mathrm{tr}_{\mathrm{alt}}|}{|\mathrm{net}|}
  \approx 0.3677
$$

The polynomial $\mathrm{net}(t)$ has 127 terms in $\mathbb{Z}[t, t^{-1}]$
with maximum coefficient $\sim 10^8$.
```

## Binary release structure

```
witness-database-v1.tar.zst
├── index.json              ← All isotopes: Z, N, A, F_Pauli, tier
├── certificates/
│   ├── H-002.cert.json     ← Full certificate with strand trace
│   ├── H-003.cert.json
│   ├── He-004.cert.json
│   ├── ...
│   └── Og-294.cert.json
├── polynomials/
│   ├── H-002.poly.bin      ← Compact binary: sparse (exp, bigint) pairs
│   ├── ...
│   └── Og-294.poly.bin
└── checksums.sha256         ← Reproducibility verification
```

## Query interface

### From Lean

```lean
-- Import the witness library
import QOU.Descartes.PauliWitness.Database

-- Query by (Z, N)
#eval PauliWitness.lookup 27 33  -- ⁶⁰Co
-- Returns: { f_pauli := 0.0042, tr_alt := ..., net := ... }

-- Verify the witness
#eval PauliWitness.verify 27 33  -- runs strand-by-strand check
```

### From MCP server

The paper-assistant MCP server serves witness data at:
- `/api/witness/:z/:n` → JSON certificate
- `/api/witness/:z/:n/lean` → Lean source file
- `/api/witness/:z/:n/verify` → run verification, return result

### From CLI

```bash
hecke-engine witness 27 33       # compute
hecke-engine verify 27 33        # verify existing certificate
hecke-engine lookup 27 33        # query from database
```

## Verification tiers by A

| A range | Tier | Method | Lean trust | Time |
|---------|------|--------|------------|------|
| 2-12 | Full | Polynomial literals in Lean | Verified | <1s |
| 13-20 | Full | Strand-by-strand `native_decide` | Verified | <1min |
| 21-60 | Strand | Strand checksums + spot checks | High | ~10min |
| 61-294 | Checksum | SHA-256 of binary certificate | Moderate | <1s |

## Computation plan

| Phase | Isotopes | Method | Time (parallel) | Storage |
|-------|----------|--------|-----------------|---------|
| 1 | A≤12 (done) | v8 i128 | minutes | 0.1 MB |
| 2 | A=13-20 | v8 i128 + mid-strip | hours | 1 MB |
| 3 | A=21-60 | v9 BigInt or modular | days | 30 MB |
| 4 | A=61-120 | modular CRT | weeks | 600 MB |
| 5 | A=121-294 | modular CRT | months | 7 GB |

Phases 1-3 are feasible on a single machine.
Phases 4-5 need distributed computation (GitHub Actions, HPC).
