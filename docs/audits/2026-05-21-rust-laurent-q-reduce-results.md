# Tier 1.A — Rust port of LaurentQ reduce: scaffold + tests (results)

**Status:** DRAFT — scaffold complete, all Rust unit tests passing.
Empirical bench gates (⁶Li < 60 s, ⁸Be < 5 min) and bit-identical
Python cross-check (1e-25 vs `laurent_q_trace`) are explicitly
deferred to a follow-up session that can run `maturin build` and a
multi-atom sweep.

Linked roadmap: `docs/audits/2026-05-20-compute-optimization-roadmap.md`.
Linked profile: `docs/audits/2026-05-20-markov-peel-bottleneck-profile.md`.
Linked scoping: `docs/audits/2026-05-20-rust-port-scoping-markov-peel.md`.

## What landed in this PR

### Rust modules (new)

| File | Lines | Purpose |
|------|------:|---------|
| `tools/hecke-engine/src/laurent_rational_q.rs` | ~360 | `LaurentRationalQ` (BTreeMap<i32, BigRational>) with Add/Sub/Mul/Neg + FFI helpers |
| `tools/hecke-engine/src/laurent_hecke_element.rs` | ~245 | `LaurentHeckeElement` (BTreeMap<Vec<i32>, LaurentRationalQ>) with concat-mul + FFI |
| `tools/hecke-engine/src/reduce_laurent.rs` | ~330 | Port of R1 (Hecke σ²), R2 (far-comm + neg-gen commute), R3 (Yang-Baxter to lex-smaller) |
| `tools/hecke-engine/src/lib.rs` | +3 | Wire the three new modules |

### PyO3 binding (new)

| File | Change | Purpose |
|------|--------|---------|
| `tools/pyhecke-native/src/lib.rs` | +1 import, +1 binding | `incremental_reduce_rust(factors, max_iter)` |

The binding mirrors the Python `incremental_reduced_element_fast`
contract: one PyO3 call per atomic-braid reduce; identity ×
factor → reduce → × factor → reduce → ... ; returns the final
reduced element in FFI form.

### Python bridge (new)

| File | Change | Purpose |
|------|--------|---------|
| `folio-assistant/computations/markov_peel_rust_bridge.py` | +120 lines | `tr_M_atomic_rust_full(Z, N, dps)` + `_factor_to_ffi` / `_ffi_to_laurent_hecke_element` |

The Markov-trace step (`tr_M_element` on the reduced sympy-converted
element) is shared with the existing `tr_M_atomic_fast` path. Only
the reduce inner loop now runs in Rust.

### Mass-table sweep registration

| File | Change | Purpose |
|------|--------|---------|
| `folio-assistant/computations/canonical_mass_table_extended.py` | +20 lines | Registers `method="laurent_q_rust"` |

The new method is registered with a graceful `ImportError` fallback
that points the caller at "rebuild the wheel" — necessary because the
default-installed `pyhecke-native` does not yet export
`incremental_reduce_rust`.

## Test evidence

```
running 33 tests
test laurent_hecke_element::tests::accumulate_drops_zero_after_cancellation ... ok
test laurent_hecke_element::tests::add_collapses_like_terms ... ok
test laurent_hecke_element::tests::add_keeps_distinct_words ... ok
test laurent_hecke_element::tests::ffi_dedups_duplicate_words_via_sum ... ok
test laurent_hecke_element::tests::ffi_round_trip_preserves_element ... ok
test laurent_hecke_element::tests::identity_times_anything_is_anything ... ok
test laurent_hecke_element::tests::mul_concatenates_words ... ok
test laurent_hecke_element::tests::mul_distributes_over_add ... ok
test laurent_hecke_element::tests::rational_coefs_in_mul ... ok
test laurent_hecke_element::tests::zero_times_anything_is_zero ... ok
test laurent_rational_q::tests::add_cancellation_drops_zeros ... ok
test laurent_rational_q::tests::ffi_pre_simplified_rational ... ok
test laurent_rational_q::tests::ffi_zero_denominator_rejected ... ok
test laurent_rational_q::tests::ffi_round_trip ... ok
test laurent_rational_q::tests::hecke_a_squared ... ok
test laurent_rational_q::tests::hecke_a_value ... ok
test laurent_rational_q::tests::pretty_smoke ... ok
test laurent_rational_q::tests::zero_and_one ... ok
test laurent_rational_q::tests::rational_coefficients_preserved ... ok
test reduce_laurent::tests::r1_finds_adjacent_squared ... ok
test reduce_laurent::tests::r2_finds_far_comm_and_neg ... ok
test reduce_laurent::tests::r3_finds_yang_baxter_when_lex_reducing ... ok
test reduce_laurent::tests::reduce_handles_rational_coefficients_exactly ... ok
test reduce_laurent::tests::reduce_identity_is_fixpoint ... ok
test reduce_laurent::tests::reduce_iter_cap_returned_when_exceeded ... ok
test reduce_laurent::tests::reduce_lex_min_form_is_fixpoint ... ok
test reduce_laurent::tests::reduce_preserves_coefficient_linearity ... ok
test reduce_laurent::tests::reduce_r1_single_square ... ok
test reduce_laurent::tests::reduce_r1_with_prefix_suffix ... ok
test reduce_laurent::tests::reduce_r2_far_comm_reorders_to_lex_smallest ... ok
test reduce_laurent::tests::reduce_r2_neg_gen_commutes_past_pos ... ok
test reduce_laurent::tests::reduce_r3_yang_baxter_to_lex_smaller ... ok
test reduce_laurent::tests::reduce_terminates_on_proton_like_word ... ok

test result: ok. 33 passed; 0 failed; 0 ignored
```

Coverage summary:

- **LaurentRationalQ (9 tests)** — zero/one identities, hecke_a
  literal value, `(q − q⁻¹)²` expansion, add cancellation drops
  zeros, rational coefficients preserved through mul, FFI round-trip
  (including pre-simplification 2/4 → 1/2 and zero-denominator
  rejection), pretty smoke.

- **LaurentHeckeElement (10 tests)** — identity × x = x, zero × x = 0,
  mul concatenates words, mul distributes over add, accumulate drops
  zero after cancellation, add collapses like terms vs distinct, mul
  preserves rational coefficients exactly, FFI round-trip preserves
  the element, FFI deduplicates duplicate-word entries via sum.

- **reduce_laurent (14 tests)** — per-rule position-finder predicates
  (R1/R2/R3), per-rule reduce-output checks (single square; with
  prefix/suffix; far-comm reorders to lex-smallest; neg-gen
  commutes past pos-gen; Yang-Baxter to lex-smaller; lex-min as
  fixpoint), coefficient-linearity preservation, exact rational
  coefficients survive reduce, iteration cap honored, proton-like
  word terminates within cap.

## Why this is correct (proof sketch)

The three rules R1/R2/R3 are exact ports of `hecke_laurent_fast.py:
reduce_laurent_rules` (lines 119-213). The Python file is itself
load-bearing and cross-checked numerically at q₀ on proton,
deuteron, tritium, ³He, ⁴He, ⁵Li per its header comment (lines 30-32).

The Rust port preserves the structure exactly:

1. Drained-iteration outer loop (matches Python `for word, coeff in
   terms.items(): ... break`).
2. Leftmost-match per word for each rule, with `continue` after a fire
   (matches Python `reduced_this = True; break`).
3. Identical R1 rewrite: `σ_i² → h · σ_i + 1` with `h = q − q⁻¹`.
4. Identical R2 predicate: `(ig >= 0 and jg < 0) or (|ig − jg| >= 2
   and ig > jg and ig, jg >= 0)`.
5. Identical R3 predicate: `(a, b, a)` with `a, b >= 0`,
   `|a − b| = 1`, and `b < a` (the lex-comparison `(b,a,b) <
   (a,b,a)` reduces to `b < a` exactly).

The use of `BigRational` (vs `BigInt` in the existing
`laurent_poly_q.rs`) is mandated by the per-coefficient algebra of
the Markov trace — rationals like `1/2` and `1/(2(q+q⁻¹))` appear
naturally and cannot be tracked as integers. This matches the
Python `LaurentQ` which uses `fractions.Fraction`.

## What is NOT in this PR (deferred to follow-up)

1. **Maturin wheel build + install.** Requires
   `cd tools/pyhecke-native && maturin build --release` and
   `pip install --break-system-packages` of the resulting wheel.
   First-time build is ~10-20 minutes on a clean checkout.

2. **Python-side bit-identical cross-check** vs
   `laurent_q_trace.tr_M_atomic_lq.evaluate_mpf(Q_50_DIGIT_STR,
   dps=50)` on every atom in `{p, n, D, T, ³He, ⁴He, ⁵Li, ⁶Li}` to
   `1e-25` relative. PR #859 used `1e-30` and we should match.

3. **Empirical speedup gates** from §11 of the roadmap:
   - ⁶Li wall < 60 s (currently 235 s; 4× minimum)
   - ⁸Be wall < 5 min (currently infeasible)

4. **Roadmap doc update** marking Tier 1.A DONE with a link to this
   results doc. Will be done once gates (1–3) are met.

5. **CI-side validation** that the new `method="laurent_q_rust"`
   actually runs in the published wheel context.

## How to finish (next session checklist)

```bash
# 1. Build & install the wheel (10-20 min first time):
cd tools/pyhecke-native
maturin build --release
pip install --break-system-packages --force-reinstall \
    target/wheels/pyhecke_native-*.whl

# 2. Run cross-check from the Python side:
cd folio-assistant/computations
python3 -c "
from laurent_q_trace import tr_M_atomic_lq
from markov_peel_rust_bridge import tr_M_atomic_rust_full
from q_parameter import Q_50_DIGIT_STR
for Z, N, label in [(1,0,'p'), (0,1,'n'), (1,1,'D'), (1,2,'T'),
                     (2,1,'³He'), (2,2,'⁴He'), (3,2,'⁵Li'), (3,3,'⁶Li')]:
    a = abs(tr_M_atomic_lq(Z, N).evaluate_mpf(Q_50_DIGIT_STR, dps=50))
    b = abs(tr_M_atomic_rust_full(Z, N, dps=50))
    rel = abs(a - b) / max(abs(a), 1e-30)
    print(f'{label}: python={a}  rust={b}  rel={rel}  {\"OK\" if rel < 1e-25 else \"FAIL\"}')
"

# 3. Bench the sweep (verifies the ⁶Li gate):
timeout 7200 python3 -u canonical_mass_table_extended.py \
    --atoms p,n,D,T,3He,4He,5Li,6Li \
    --method laurent_q_rust \
    2>&1 | tee /tmp/sweep-laurent-q-rust.log
```

If steps 2 and 3 both pass, update this doc with the empirical
numbers and flip the status banner from DRAFT to DONE.
