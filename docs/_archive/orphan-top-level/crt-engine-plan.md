# Plan: CRT Engine + u128 Storage for Binary Release

## Identity-Simplified Computation

From `transfer-matrix-identities.md`:
- T_pp × T_nn = I (pp-nn pairs cancel)
- T_pn² = [2]_q²/4 × I (pn pairs give scalar)

For nucleus (Z, N) with ground-state ordering:
1. Count: n_pp = C(Z,2), n_nn = C(N,2), n_pn = Z×N
2. Cancel: min(n_pp, n_nn) pp-nn pairs
3. Pair: n_pn // 2 pn pairs → each gives scalar [2]_q²/4
4. Effective: |n_pp - n_nn| leftover same-type + n_pn % 2 unpaired pn

For Z=N nuclei: **zero effective crossings** — mass is pure scalar.

## CRT Engine Design

Replace BigInt with modular arithmetic:
- Choose K primes p₁, ..., p_K with ∏p_i > max_coefficient
- Compute NF mod each p_i independently (u64 arithmetic)
- Reconstruct exact integer coefficients via Chinese Remainder Theorem
- K = 4 primes (each ~2⁶⁰) gives 240-bit range, sufficient for A ≤ 40

### Primes for CRT
```rust
const CRT_PRIMES: [u64; 4] = [
    1_000_000_007,      // 10^9 + 7
    1_000_000_009,      // 10^9 + 9
    998_244_353,        // NTT-friendly prime
    985_661_441,        // another NTT-friendly
];
```

Product ≈ 10^{36} — sufficient for coefficients up to ~10^{36}.
For A > 30 (coefficients ~10^{100}), use K = 8 primes.

### u128 Storage for Binary Release

Certificate format for GitHub binary release:
```json
{
  "isotope": {"z": 11, "n": 12, "a": 23},
  "tr_alt": {
    "terms": [[power, "coeff_hex_u128"], ...],
    "sign_bits": "hex_bitmap"
  },
  "net": { ... },
  "f_pauli_f64": 1.234567,
  "crt_primes": [1000000007, 1000000009, ...],
  "crt_residues": {
    "tr_alt": [[power, [r1, r2, r3, r4]], ...],
    "net": [[power, [r1, r2, r3, r4]], ...]
  }
}
```

The CRT residues are u64 values — compact and portable.
The exact BigInt coefficients can be reconstructed from the residues.
f_pauli_f64 is the pre-computed float for immediate use.

## Implementation Steps

### Phase 1: Identity simplification in Python
- Implement the pp-nn cancellation + pn pairing
- Compute Φ_q from scalars + effective crossings only
- Test against current results (should match exactly)

### Phase 2: CRT engine in Rust
- Add `--crt` flag to hecke-bigint
- Compute NF mod each prime independently (4 parallel passes)
- Each pass uses u64 arithmetic — no BigInt
- Merge results via CRT at the end

### Phase 3: u128 binary certificate format
- Compact binary format for GitHub release
- Include CRT residues for exact reconstruction
- Include f_pauli_f64 for immediate use

### Phase 4: Generate all certificates
- Run CRT engine for all missing atoms (Na-K)
- Run for Z=21-40 (Sc-Zr)
- Benchmark: expect ~10× speedup from CRT vs BigInt
