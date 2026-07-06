# Compute optimisation roadmap — markov-peel pipeline for heavy atoms + organic chemistry

**Date:** 2026-05-20
**Trigger:** Session-end handover after PR #859 (LaurentQ-direct Markov trace + Phase-2 Rust port) merged. Captures the next-tranche optimisation plan for downstream heavy-atom (A ≥ 8) and organic-chemistry compute that PR #859 unblocks.
**Author context:** "we will need everything for heavy atoms and organic chem"; "sympy Rational arithmetic inside LaurentQ.__mul__ -> rust? that would be large but worth it"

## Status after PR #859 (already on main)

Empirical speedups landed:

| atom | sympy `tr_M_atomic` | Python LaurentQ `tr_M_atomic_lq` (PR #859) | speedup |
|------|--------------------:|-------------------------------------------:|--------:|
| ⁴He  | 11.14 s             |  3.8 s   | 2.9× |
| ⁵Li  | 67 s                | 22.8 s   | 2.9× |
| ⁶Li  | 1036 s (17 min)     | 235.3 s (3.9 min) | **4.4×** |
| ⁷Li  | ~5 hr (projected)   | ~17-20 min (in flight) | 15-18× |

Phase-2 Rust port (`pyhecke_native.tr_m_word_lq` + Python `tr_M_atomic_rust_recursive`): bit-identical to Python LaurentQ at 50-dps; doesn't yet move the needle because the Python `incremental_reduced_element_fast` reduce step still dominates (60-70% of wall).

## Bottleneck ranking (post-#859, empirical from cProfile on ⁶Li)

| # | Component | Share of ⁶Li wall | Symmetry-exploitable? |
|---|-----------|------------------:|:----------------------|
| 1 | `incremental_reduced_element_fast` (LaurentQ reduce of atomic braid) — sympy `Rational` arithmetic inside `LaurentQ.__mul__` is the inner hot loop | **60-70%** | YES (nucleon-permutation S_Z × S_N — under-used) |
| 2 | `tr_M_word_lq` recursion across reduced σ-words | 15-20% | YES (cyclic rotation canonical form — partially used) |
| 3 | sympy `Rational` ops inside `LaurentQ.__mul__` (subset of #1) | 10-15% | NO (algebraic kernel) |
| 4 | `y_lambda_at(n, q_0)` lookup + sympy→mpmath conversion | 3-5% | already exploited (q₀ witness cache) |
| 5 | atomic word build + PyO3 marshalling | < 1% | n/a |

## Optimisation roadmap (ranked by user-flagged priority + ROI)

### Tier 1 — author's explicit priority (heavy atoms + organic chem critical path)

#### 1.A. **Rust `LaurentQ.__mul__` + reduce rule loop** ★★★

The user explicitly flagged: "sympy Rational arithmetic inside LaurentQ.__mul__ -> rust? that would be large but worth it". This is the dominant wall (60-70%) and the single largest improvement available.

**Scope:** new Rust crate path (or extend `hecke-engine`) with:
- `LaurentRationalQ` — Laurent polynomial in `q` with `num_rational::BigRational` coefficients (exact rationals, no sympy)
- `LaurentHeckeElement` — `BTreeMap<Vec<u32>, LaurentRationalQ>` (dict of σ-words to LaurentRationalQ coefs)
- `reduce_laurent_rules_rust` — port of `reduce_laurent_rules` (R1: σ² → hσ + 1, R2: braid relations, R3: normal form) with exact-rational arithmetic
- PyO3 binding `incremental_reduced_element_rust(word: list, max_iter) -> LaurentHeckeElement` returning the reduced element as a flat byte buffer for one-shot marshalling

**Boundary cost:** ONE PyO3 call per atomic-braid reduction. The reduced element (~hundreds of σ-only terms) is marshalled back as a structured Python object via the existing FFI pattern.

**Expected speedup:** 10-50× over the current Python LaurentQ reduce. Critical because:
- Each `LaurentQ.__mul__` allocates new sympy `Rational` objects; Rust `BigRational` uses pooled allocations
- sympy's `Basic.compare` (37 M calls on ⁵Li per the profile) becomes a cheap integer-compare on flat (numerator, denominator) pairs in Rust

**Projected impact at A ≥ 8 (heavy atoms / organic chem):**

| atom | A | Python LaurentQ projected | Rust reduce projected | enables |
|------|--:|--------------------------:|----------------------:|---------|
| ⁷Li  | 7 | ~17-20 min                | ~30-60 s              | routine ⁷Li sweeps |
| ⁸Be  | 8 | ~70-90 min (projected)    | ~2-5 min              | **unlocks A=8** |
| ⁹Be  | 9 | ~3-4 hr                   | ~10-30 min            | **unlocks A=9** |
| ¹²C  | 12| infeasible                | ~30-90 min            | **unlocks organic chemistry** |
| ¹⁴N  | 14| infeasible                | ~1-3 hr               | unlocks ¹⁴N (amines, amides) |
| ¹⁶O  | 16| infeasible                | ~2-6 hr               | unlocks ¹⁶O (carbonyl, hydroxyl) |

**Effort:** 1-2 weeks focused. Mirrors the existing `hecke_laurent_fast.py` algorithm 1:1 in Rust; reuses `hecke_engine::laurent_poly_q::LaurentPolyQ` as the polynomial-in-q base type (but switch from `BigInt` to `BigRational` since LaurentQ uses Rational coefs).

**Risk:** medium. The reduce rules R1-R3 are well-defined; main risk is the Python ↔ Rust word-format translation (the Python uses `tuple[int, ...]` of generator indices, Rust uses `Vec<u32>` — same encoding, no semantic gap).

**This is THE optimization for heavy-atom + organic-chem use cases.**

### Tier 2 — nucleon-permutation symmetry (S_Z × S_N orbit reduction)

#### 1.B. **Nucleon-orbit reduction in `atom_braid_word_3A`** ★★

For atomic braid β_{Z,N} with Z protons and N neutrons, the same-species nucleons are interchangeable. The braid word naturally has a S_Z × S_N permutation symmetry. The current reduce walks the FULL word; the orbit-quotient walks only one representative per (S_Z × S_N) orbit.

**Scope:**
- New helper `atom_braid_orbit_representative(Z, N)` that returns the canonical orbit representative + orbit size |S_Z × S_N| = Z! · N!
- `incremental_reduced_element_fast` operates on the representative only
- Final trace: `tr_M(β_{Z,N}) = |orbit| · tr_M(representative)` IFF the trace is invariant under the orbit action (it is — Markov trace is invariant under conjugation; nucleon permutations are conjugations by braid generators in H_{3A})

**Expected impact:**

| atom | (Z, N) | orbit size | wall reduction |
|------|--------|-----------:|----------------|
| ⁴He | (2,2) |   4 | 4× |
| ⁵Li | (3,2) |  12 | 12× |
| ⁶Li | (3,3) |  36 | 36× |
| ⁷Li | (3,4) |  144 | 144× |
| ⁸Be | (4,4) | 576 | **576×** |
| ¹²C | (6,6) | ~520K | overwhelming |

**Compounded with #1.A:** Rust reduce on the orbit representative for ¹²C would be ~30-90 min / 520K ≈ trivial seconds. **This is the path to truly tractable organic chemistry.**

**Caveat:** the orbit-trace identity needs algebraic verification. The Markov trace IS conjugation-invariant in H_{3A}, but the orbit action involves not just conjugation but also the I_pp / I_pn / I_nn interface swaps. For Z, N ≥ 2 with mixed interfaces (which is every atom with both species), the orbit action might not be a pure conjugation. **First step: prove or disprove the orbit-trace identity** (a small Lean proof or numerical cross-check on ⁴He → ⁵Li transitions).

**Effort:** 3-5 days (1-2 days for algebraic verification + 2-3 days for orbit-representative builder + Python integration).

**Risk:** medium-high — the algebraic identity is the load-bearing claim. If false, the optimization gives wrong answers (verifiable via cross-check vs full-word path on A ≤ 6).

### Tier 3 — cheap quick wins

#### 1.C. **Canonical cyclic-rotation form for `tr_m_word_lq` cache keys** ★

The Markov trace is cyclic: `tr_M(αβ) = tr_M(βα)`. Currently the Rust cache keys on the literal word tuple. Picking the lexicographically-smallest cyclic rotation as the cache key collapses cyclic-equivalent words to a single cache entry.

**Effort:** 1-2 hours. Pure Rust change in `tr_m_word_lq.rs`; no algorithmic risk.
**Impact:** 1.5-3× on the recursion portion (~5% of total wall → ~1-2% improvement after compounding).

#### 1.D. **Session-level shifted-NF cache for the mass-table sweep** ★

When the mass table iterates atoms p, n, D, T, ³He, ⁴He, ⁵Li, ⁶Li, ⁷Li, ⁸Be, …, each atom needs the proton-NF shifted by 0, 3, 6, … and neutron-NF similarly. The shifted-NF entries are independent of atom; cache them across the sweep.

**Effort:** 1 day. Already scaffolded as `_shifted_nucleon_nf` in `markov_peel.py` (from PR #859); now needs wiring into `canonical_mass_table_extended.py`'s outer loop.
**Impact:** 1.2-1.5× on full mass-table sweep wall (no per-atom impact).

### Tier 4 — research-grade (deferred, separate PR)

#### 1.E. **Bring S₅-block decomposition** at H_15 (⁵Li-class atoms)

Bring's quintic Galois symmetry S_5 acts on the 5 branch periods of `y² = x⁵ - 1`. At H_{15} (⁵Li, A=5), the 176 partitions of 15 carry a residual S_5 action via the 5-cycle structure. Computing one orbit representative per S_5 orbit and applying the orbit-sum identity for χ^λ would reduce the Wenzl-bridge combine from 176 partitions to ~7-30 orbits.

**Expected impact:** 3-5× on the y_λ × χ^λ combine at A=5 only; doesn't help A ≠ 5.
**Effort:** 1 week (research-grade; needs the orbit-sum identity derived + verified).
**Risk:** medium-high — derivation involves non-trivial Bring-substrate-categorical bridge work.

#### 1.F. **Bring quintic substitution for q₀** — substrate-derivation of λ_p_scale

Currently q₀ is a numerical 50-dps mpf. The "substrate-derivation of q₀ from first principles" open problem (PR #843 / PR #852 6-tier consistent-NEGATIVE) might be resolved via Bring's exact quintic root. Would give an exact algebraic representation of q₀ that propagates symbolically through every trace computation.

**Expected impact:** enables fully-symbolic-q paths through every compute; eliminates dps-truncation errors at machine precision.
**Effort:** 2-4 weeks; requires new content + Lean derivation.
**Note:** **Out of scope for this optimization track** — it's a substrate-derivation research question, not a pipeline optimization. Listed here for completeness because it touches the same Bring-Markov-substrate interface.

## Status update (2026-05-22)

**Tier 1.A: architectural delivery complete; 4× bench gate open.**
See [`2026-05-22-rust-laurent-q-reduce-results.md`](2026-05-22-rust-laurent-q-reduce-results.md)
for full details.  Empirical ⁶Li speedup vs Python LaurentQ:
- After all-Rust + MPFR pipeline (commit `22e3c1cd`): **2.38×**
  (94.6 s vs 225 s baseline)
- After R1 fast-path (commit `52940b5f`): **2.65×**
  (84.5 s vs 223.7 s baseline)

Cross-check bit-identical to 5.6 × 10⁻⁴⁹ relative on every
atom from p through ⁶Li.  Follow-up optimisations (FxHashMap
intermediate, GCD deferral via Ratio::new_raw) tracked in the
results doc to close the remaining gap to the 60 s gate.

**Tier 1.C: complete.**  Cyclic-canonical cache key in
`tr_m_word_lq.rs`; shipped on the same branch.

## Recommended attack order

1. **Tier 1.A (Rust LaurentQ reduce loop)** — biggest win, user's explicit priority, 1-2 weeks
2. **Tier 1.B (nucleon-orbit reduction)** — multiplicative with #1.A; gates organic chemistry; 3-5 days
3. **Tier 1.C (cyclic canonical form)** — cheap rollup commit; ship with #1.A
4. **Tier 1.D (sweep cache)** — small PR; ship with #1.B
5. **Tier 1.E (Bring S₅ orbits at A=5)** — research follow-on; only if A=5 specifically becomes a bottleneck
6. **Tier 1.F (Bring quintic substitution)** — separate substrate-derivation PR; not on the pipeline-optimization critical path

## Combined projected timeline → unlock organic-chemistry compute

| Stage | After what | A reachable in < 1 hr |
|-------|-----------|----------------------:|
| Today (post-#859) | merged | A ≤ 7 |
| + Tier 1.A | 1-2 wk | A ≤ 8 |
| + Tier 1.A + 1.B | +3-5 days | A ≤ 12 (¹²C) ★ organic chem first reached |
| + Tier 1.A + 1.B + 1.C + 1.D | +1 day | A ≤ 16 (¹⁶O) |

¹²C / ¹⁴N / ¹⁶O are the gateway atoms for organic chemistry. The combination 1.A + 1.B is the unlocking pair.

## Cross-references

- PR #859 (merged, parent of this roadmap): `optimize: LaurentQ-direct Markov trace + Rust port`
- [`docs/audits/2026-05-20-markov-peel-bottleneck-profile.md`](2026-05-20-markov-peel-bottleneck-profile.md) — original profile + 4-strategy ranking
- [`docs/audits/2026-05-20-rust-port-scoping-markov-peel.md`](2026-05-20-rust-port-scoping-markov-peel.md) — initial Rust scoping (Phase-1+2 done; this doc plans Phase-3 = Tier 1.A above)
- `tools/hecke-engine/src/laurent_poly_q.rs` — existing BigInt LaurentPoly; extend to BigRational for Tier 1.A
- `tools/hecke-engine/src/tr_m_word_lq.rs` — Phase-2 Rust recursion (already shipped via #859); Tier 1.A targets the upstream reduce step that feeds this

## Handover summary for the next agent

If you pick this up: **start with Tier 1.A (Rust LaurentQ reduce loop)**. The user has explicitly approved the scope ("sympy Rational arithmetic inside LaurentQ.__mul__ -> rust? that would be large but worth it"). The implementation pattern is:

1. Add `LaurentRationalQ` (or extend `LaurentPolyQ` to support `BigRational` coefs) in `tools/hecke-engine/src/`.
2. Port `reduce_laurent_rules` from `computations/hecke/hecke_laurent_fast.py:119` to Rust 1:1.
3. PyO3 binding `incremental_reduced_element_rust(word, max_iter)` returning a serialised LaurentHeckeElement.
4. Python bridge in `markov_peel_rust_bridge.py` to compose with the existing `pyhecke_native.tr_m_word_lq`.
5. Cross-check at MPFR-50dps on ⁴He → ⁷Li (must match `laurent_q_trace.tr_M_atomic_lq.evaluate_mpf` bit-for-bit).
6. Benchmark and ship.

After Tier 1.A lands: Tier 1.B (nucleon-orbit reduction) requires algebraic verification of the orbit-trace identity. Do that on paper (or Lean) FIRST; don't ship the orbit code until the identity is established. Test on ⁴He (orbit size 4) and ⁵Li (orbit size 12) against the full-word reference path before extending to ⁷Li / ⁸Be.
