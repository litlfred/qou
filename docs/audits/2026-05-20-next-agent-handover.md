# Next-agent handover — compute optimization implementation

**Date:** 2026-05-20
**Author session:** post-#859 + #865 merge
**Reading time:** 30 min for orientation; 1 hr including referenced docs

---

## §0. TL;DR (60 seconds)

You are picking up the compute-optimization track for the **Quantum Observable Universe** (QOU) paper.

- PR #859 (merged): Python LaurentQ + Phase-2 Rust port → ⁶Li 4.4× faster
- PR #865 (merged): roadmap doc — defines Tiers 1.A → 1.F
- **Your job:** implement Tier 1.A (Rust LaurentQ.__mul__ + reduce loop), then 1.B (orbit reduction), then 1.C + 1.D (quick wins)
- **Goal:** unlock heavy atoms (A ≥ 8) and organic chemistry (¹²C, ¹⁴N, ¹⁶O)
- **Floor:** ⁶Li wall < 60 s, ⁸Be < 5 min, cross-check at 1e-25 vs Python LaurentQ

---

## §1. Orientation — read in order

| # | File | Time | Why |
|---|------|-----:|-----|
| 1 | [`CLAUDE.md`](../../CLAUDE.md) | 15 min | repo conventions, **precision goals (L1 = 50-dps)**, three-calibration discipline (STRICT — read this) |
| 2 | [`2026-05-20-compute-optimization-roadmap.md`](2026-05-20-compute-optimization-roadmap.md) | 10 min | the master plan (PR #865) — tiers, projections, attack order |
| 3 | [`2026-05-20-markov-peel-bottleneck-profile.md`](2026-05-20-markov-peel-bottleneck-profile.md) | 5 min | cProfile data + 4-strategy ranking that motivated #859 |
| 4 | [`2026-05-20-rust-port-scoping-markov-peel.md`](2026-05-20-rust-port-scoping-markov-peel.md) | 10 min | initial scoping (Phase-1+2 done; you're doing Phase-3) |
| 5 | [`laurent_q_trace.py`](../../computations/laurent_q_trace.py) | 15 min | **reference implementation** you must match bit-for-bit |
| 6 | [`hecke_laurent_fast.py`](../../computations/hecke/hecke_laurent_fast.py) | 20 min | **THE FILE YOU'RE PORTING** for Tier 1.A — read every line |
| 7 | [`tools/hecke-engine/src/tr_m_word_lq.rs`](../../tools/hecke-engine/src/tr_m_word_lq.rs) | 10 min | Phase-2 Rust template (style + PyO3 pattern) |
| 8 | [`tools/hecke-engine/src/laurent_poly_q.rs`](../../tools/hecke-engine/src/laurent_poly_q.rs) | 10 min | existing BigInt LaurentPoly — your starting template (extend to BigRational) |

**Do not write code until you have read 1, 2, 5, 6.**

---

## §2. Story so far

| PR | What landed | Speedup |
|----|-------------|---------|
| #843 | Borromean fix `Vol(𝓑₃) = 8·G` | m_p → −0.32 ppb |
| #852 | bar-anti-sym + 6-tier Bring-Bloch NEG + mass-table to ⁶Li | foundational |
| **#859** | LaurentQ Python + Phase-2 Rust port (`tr_m_word_lq` recursion) | **⁶Li 4.4×** |
| **#865** | roadmap (this track) | planning |

### §2.1 Empirical state (post #859)

| atom | sympy wall | LaurentQ wall | your target |
|------|----------:|--------------:|------------:|
| ⁴He  | 11.14 s | 3.8 s | < 1 s |
| ⁵Li  | 67 s | 22.8 s | < 5 s |
| ⁶Li  | 1036 s | 235 s | **< 60 s** |
| ⁷Li  | ~5 hr (proj) | ~17-20 min | < 5 min |
| ⁸Be  | infeasible | infeasible | **< 5 min** |
| ¹²C  | infeasible | infeasible | < 90 min |

### §2.2 Why the current path is slow

cProfile on ⁵Li (248 s wall under profiler):

| Function | Wall | % |
|----------|-----:|--:|
| `sympy/core/basic.py:compare` | 66 s | 27% |
| `sympy/core/sympify.py:sympify` | 21 s | 8.5% |
| `sympy/core/add.py:flatten` | 13.8 s (146 s cumulative) | 5-60% |
| `sympy/core/cache.py:wrapper` | 10.8 s (171 s cumulative) | 4-70% |
| `laurent_q.py:__mul__` (the "fast" path) | 6.5 s | **3%** |

The Phase-2 Rust port (`tr_m_word_lq`) attacks the trace-assembly downstream. But the upstream **reduce step** (`incremental_reduced_element_fast`) is **still Python LaurentQ** — 60-70% of post-#859 wall. That's your target.

**User's verbatim directive:** *"sympy Rational arithmetic inside LaurentQ.__mul__ → rust? that would be large but worth it"*

---

## §3. Tier 1.A — Rust LaurentQ.__mul__ + reduce loop

**Effort:** 1-2 weeks focused
**Priority:** ★★★ (the user's #1)
**Unlock:** A ≥ 8 / organic chemistry (combined with Tier 1.B)

### §3.1 Files you'll touch

| Side | File | Action |
|------|------|--------|
| Rust (NEW) | `tools/hecke-engine/src/laurent_rational_q.rs` | LaurentPoly in q with `BigRational` coefs |
| Rust (NEW) | `tools/hecke-engine/src/laurent_hecke_element.rs` | `BTreeMap<Vec<u32>, LaurentRationalQ>` |
| Rust (NEW) | `tools/hecke-engine/src/reduce_laurent.rs` | R1+R2+R3 fixpoint reducer |
| Rust (MOD) | `tools/hecke-engine/src/lib.rs` | add three `pub mod` lines |
| PyO3 (MOD) | `tools/pyhecke-native/src/lib.rs` | add `incremental_reduce_rust` binding |
| Python (MOD) | `computations/markov/markov_peel_rust_bridge.py` | add `tr_M_atomic_rust_full(Z, N, dps)` |
| Python (MOD) | `computations/canonical_mass_table_extended.py` | add `method="laurent_q_rust"` |
| Audit (NEW) | `docs/audits/2026-05-21-rust-laurent-q-reduce-results.md` | empirical results |

### §3.2 Algorithm — the three reduce rules

Read `hecke_laurent_fast.py:119-216` for the source-of-truth implementation. The rules are:

**R1. Hecke quadratic.** For any word containing adjacent identical generators `(..., σ_i, σ_i, ...)`:
```
σ_i² → h · σ_i + 1     where h = q - q⁻¹
```
Translates one word into two words (coefficients `h` and `1`).

**R2. Braid relations.** For adjacent generators differing by 1, `(..., σ_i, σ_{i+1}, σ_i, ...)`:
```
σ_i · σ_{i+1} · σ_i = σ_{i+1} · σ_i · σ_{i+1}
```
Pure word rewrite — coefficient unchanged.

**R3. Far commutativity.** For `|i - j| ≥ 2`, `σ_i · σ_j = σ_j · σ_i`. Used to canonicalize word order for cache hits.

**Fixpoint loop.** Apply R1 + R2 + R3 repeatedly until no rule fires. Bounded by `max_iterations_per_step = 5000` (matches Python).

### §3.3 BigRational vs BigInt — why you need rationals

Python LaurentQ stores `coefs: dict[int, sympy.Rational]`. The Markov-axiom recursion generates fractions like `1/2`, `1/(2·(q + q⁻¹))`, etc. Pure `BigInt` (as in the existing `laurent_poly_q.rs`) cannot represent these.

Use `num_rational::BigRational` from the `num-rational = "0.4"` crate (already in `hecke-engine/Cargo.toml`).

```rust
// in tools/hecke-engine/src/laurent_rational_q.rs
use num_bigint::BigInt;
use num_rational::BigRational;
use num_traits::{One, Zero};
use std::collections::BTreeMap;

#[derive(Clone, Debug, Default)]
pub struct LaurentRationalQ {
    /// q^k coefficient at exponent k. Sparse — only non-zero terms.
    pub terms: BTreeMap<i32, BigRational>,
}

impl LaurentRationalQ {
    pub fn zero() -> Self { Self { terms: BTreeMap::new() } }
    pub fn one() -> Self {
        let mut t = BTreeMap::new();
        t.insert(0, BigRational::one());
        Self { terms: t }
    }
    // ... Add, Mul, Neg, etc. — mirror laurent_poly_q.rs style
}
```

### §3.4 PyO3 binding pattern

Add to `tools/pyhecke-native/src/lib.rs`:

```rust
/// Reduce a Hecke-word product to canonical NF. Mirrors
/// `computations/hecke_laurent_fast.incremental_reduced_element_fast`.
///
/// `word`: `Vec<(i32, i32, u32)>` triples `(c_num, c_den, gen)` —
///   the rational coefficient `(c_num/c_den)` times σ_gen.
/// Returns: `Vec<(Vec<u32>, Vec<(i32, i32, i32)>)>` — list of
///   (reduced_word, [(q_exp, num, den), ...]) pairs.
#[pyfunction]
fn incremental_reduce_rust(
    word: Vec<(i32, i32, u32)>,
    max_iter: usize,
) -> PyResult<Vec<(Vec<u32>, Vec<(i32, String, String)>)>> {
    // BigRational → decimal string at the boundary (PyO3 can't
    // ferry BigInt directly; string is exact + cheap).
    ...
}
```

**Boundary cost:** ONE PyO3 call per atomic-braid reduction. The reduced element has hundreds of σ-only terms; flat marshalling cost is < 1 ms.

### §3.5 Cross-check pattern (REQUIRED before merge)

```python
# computations/markov/markov_peel_rust_bridge.py — new function
def tr_M_atomic_rust_full(Z: int, N: int, dps: int = 50):
    """Full Rust path: Rust reduce → Rust tr_m_word_lq → mpmath eval."""
    from mass_at_3A_proper import atom_braid_word_3A
    word = atom_braid_word_3A(Z, N, include_inter=True)
    # Translate to Rust-friendly (c_num, c_den, gen) form
    rust_word = [(int(c * 1000), 1000, gen) for c, _, gen in word]  # placeholder
    # Call Rust reduce → returns flat list of (word, coef_q_terms)
    reduced = pyhecke_native.incremental_reduce_rust(rust_word, 10000)
    # For each reduced (word, q_coef), call Rust tr_m_word_lq on the word,
    # multiply by q_coef, accumulate in ZHLaurent.
    # Then evaluate at q₀ to mpmath.mpf at dps.
    ...
```

Cross-check vs `laurent_q_trace.tr_M_atomic_lq.evaluate_mpf` on every atom in `{p, n, D, T, ³He, ⁴He, ⁵Li, ⁶Li}` to **1e-25 relative** (not 1e-15 — at 50-dps you have 50 digits of precision; 1e-15 defeats the point).

### §3.6 Acceptance criteria

All of the following must pass before opening the PR:

- [ ] `cargo test --release --lib` in `tools/hecke-engine` → all new tests pass
- [ ] `cargo test --release --lib reduce_laurent` → fixpoint terminates on the proton, deuteron, tritium, ⁴He atomic words
- [ ] `maturin build --release` in `tools/pyhecke-native` → wheel builds
- [ ] PyO3 binding callable: `import pyhecke_native; pyhecke_native.incremental_reduce_rust(...)`
- [ ] Cross-check bit-identical at 50-dps vs `laurent_q_trace.tr_M_atomic_lq.evaluate_mpf` on **every** atom in `{p, n, D, T, ³He, ⁴He, ⁵Li, ⁶Li}` — abs(rel.diff) < 1e-25
- [ ] **⁶Li wall < 60 s** (4× the current 235 s; **mandatory gate**)
- [ ] ⁸Be wall < 5 min (currently infeasible — this is the empirical proof of unlock)
- [ ] No regression: existing `markov_peel.tr_M_atomic` tests still pass
- [ ] CI `validate` green on the PR

---

## §4. Tier 1.B — orbit reduction (3-5 days; **algebraic proof first**)

### §4.1 The risk

The claim is `tr_M(β_{Z,N}) = |S_Z × S_N| · tr_M(orbit_representative)`. **This may be false.** Markov trace is conjugation-invariant in H_{3A}, but nucleon permutations are NOT pure conjugations when species are mixed (the I_pp / I_pn / I_nn interfaces transform differently).

### §4.2 Required preflight (DO NOT SKIP)

Before writing the orbit-representative code, prove or numerically falsify the orbit-trace identity on ⁴He:

```python
# Test in a fresh script — DO NOT commit until passing
from laurent_q_trace import tr_M_atomic_lq
from q_parameter import Q_50_DIGIT_STR
import mpmath as mp
mp.mp.dps = 50

# Full atomic braid (canonical ordering: p, p, n, n)
full = tr_M_atomic_lq(2, 2).evaluate_mpf(Q_50_DIGIT_STR, 50)

# Orbit representative: build by hand — only one (p, n) interface
# instead of all 4 cross-pairs
orbit_repr = ...  # YOU CONSTRUCT THIS — see §4.3
orbit_val = 4 * tr_M_atomic_orbit_lq(orbit_repr).evaluate_mpf(...)

rel_err = abs(full - orbit_val) / abs(full)
print(f"orbit identity rel.err: {rel_err}")
assert rel_err < mp.mpf("1e-25"), "ORBIT IDENTITY FALSE — STOP"
```

### §4.3 Decision tree

```
Run the ⁴He preflight (§4.2)
│
├── Identity holds (rel.err < 1e-25)
│   │
│   ├── YES → proceed to §4.4 (implementation)
│   │
│   └── NO  → STOP. Document the failure in
│             docs/audits/2026-05-21-orbit-identity-falsified.md
│             with the numerical witness. Escalate to author —
│             do NOT ship orbit code.
│
└── Identity holds only with sign correction
    │
    └── Investigate `tr_M(β) = Σ_{g ∈ S_Z × S_N} sign(g) · tr_M(g·rep)`?
        Check on ⁴He, ⁵Li, ³He. Document findings.
```

### §4.4 Implementation (only if §4.2 passes)

| Step | File | Action |
|------|------|--------|
| 1 | `computations/mass_at_3A_proper.py` | new `atom_braid_orbit_representative(Z, N)` |
| 2 | `computations/laurent_q_trace.py` | new `tr_M_atomic_orbit_lq(Z, N)` that calls the representative + multiplies by orbit size |
| 3 | `computations/canonical_mass_table_extended.py` | new `method="laurent_q_orbit"` or `--use-orbit` flag |
| 4 | Cross-check | every benched atom: orbit-path vs full-path agree to 1e-25 |

### §4.5 Orbit sizes (for sanity-check)

| atom | (Z, N) | orbit |
|------|--------|-------|
| ⁴He | (2,2) | 4 |
| ⁵Li | (3,2) | 12 |
| ⁶Li | (3,3) | 36 |
| ⁷Li | (3,4) | 144 |
| ⁸Be | (4,4) | 576 |
| ¹²C | (6,6) | ~520 K |

### §4.6 Acceptance criteria

- [ ] §4.2 preflight passes on ⁴He AND ⁵Li AND ⁶Li (three independent atoms)
- [ ] Implementation cross-checks against full-path on every catalogued atom to 1e-25
- [ ] ⁸Be wall reduction is at least 100× vs Tier 1.A alone (orbit 576 should give ~500× in theory; settling for 100× allows for overhead)
- [ ] CI green

---

## §5. Tier 1.C — cyclic canonical form (1-2 hours)

### §5.1 Change

In `tools/hecke-engine/src/tr_m_word_lq.rs`, replace the cache key:

```rust
// BEFORE
type CacheKey = (Vec<u32>, usize, u32);

fn cache_key(word: &[u32], n_strands: usize, max_depth: u32) -> CacheKey {
    (word.to_vec(), n_strands, max_depth)
}

// AFTER
fn canonical_cyclic(word: &[u32]) -> Vec<u32> {
    let n = word.len();
    if n == 0 { return vec![]; }
    let mut best: Vec<u32> = word.to_vec();
    for i in 1..n {
        let rot: Vec<u32> = word[i..].iter()
            .chain(word[..i].iter())
            .copied()
            .collect();
        if rot < best { best = rot; }
    }
    best
}

fn cache_key(word: &[u32], n_strands: usize, max_depth: u32) -> CacheKey {
    (canonical_cyclic(word), n_strands, max_depth)
}
```

### §5.2 Pitfall

The cyclic canonicalization must ONLY affect the cache key — NOT the recursion behavior. The recursion still operates on the original word (its rotations are part of the algorithm).

### §5.3 Acceptance

- [ ] `cargo test` — existing tests still pass
- [ ] New test: `tr_M([0, 1])` and `tr_M([1, 0])` both compute correctly AND cache-hit on the second call (assert via cache stats)
- [ ] No regression in ⁶Li wall

---

## §6. Tier 1.D — sweep cache (1 day; may already be done)

### §6.1 Verify first

```bash
cd computations
python3 -c "
import markov_peel
from markov_peel import _shifted_nucleon_nf
for Z, N in [(1,0), (0,1), (1,1), (1,2), (2,1), (2,2), (3,2), (3,3)]:
    _ = markov_peel.tr_M_atomic(Z, N)
print(_shifted_nucleon_nf.cache_info())
"
```

| `hits` value | action |
|-------------|--------|
| > 0 | **Tier 1.D is already done** (#859 scaffolding sufficient) |
| = 0 | wire `_shifted_nucleon_nf` into `tr_M_atomic_fast` path (currently slow-path only — see audit doc footnote ⚠️) |

### §6.2 Acceptance

- [ ] `cache_info().hits > 0` after sweep
- [ ] Mass-table sweep wall reduced ≥ 20%

---

## §7. Build / test environment

### §7.1 Prerequisites

```bash
# Rust toolchain — version pinned via rust-toolchain.toml; should be 1.94+
rustc --version
cargo --version

# maturin (Python ↔ Rust binding builder)
pip install --break-system-packages maturin
maturin --version
```

### §7.2 Build cycle

```bash
# 1. Build hecke-engine (Rust lib)
cd tools/hecke-engine
cargo build --release
cargo test --release --lib   # runs all unit tests

# 2. Build pyhecke-native (PyO3 wheel) + install
cd ../pyhecke-native
maturin build --release
pip install --break-system-packages --force-reinstall \
    target/wheels/pyhecke_native-*-cp311-*.whl

# 3. Python smoke test
cd ../../computations
python3 laurent_q_trace.py             # 6/6 self-check
python3 markov_peel_rust_bridge.py     # cross-check

# 4. Mass-table bench (with the laurent_q method from #859)
timeout 7200 python3 -u canonical_mass_table_extended.py \
    --atoms p,n,D,T,3He,4He,5Li,6Li --method laurent_q \
    2>&1 | tee /tmp/bench.log
```

### §7.3 Gotchas

| Symptom | Cause | Fix |
|---------|-------|-----|
| `maturin develop` fails: "no virtualenv" | maturin requires venv for `develop` | Use `maturin build --release` + `pip install` instead |
| `pyhecke_native` not found in Python | not installed after rebuild | `pip install --force-reinstall target/wheels/*.whl` |
| Cargo pulls in OpenBLAS / gfortran | feature flag `clarabel-sdp` accidentally on | Default build only; do NOT enable Clarabel features unless needed |
| Cross-check fails at 1e-15 (passes at 1e-25) | tolerance too tight | At 50-dps, 1e-25 is the floor; 1e-15 will spuriously fail |
| CI fails with `witness drift` | self-emitting audit witnesses bumped | Run validators per `/prepare-merge` §1·a; commit the drift |
| `tr_m_word_lq` raises `RuntimeError: Case C` | atomic braid hit Case C (multiple top-1) | Caller falls back to sympy ocneanu — **don't implement Case C in Rust** |

---

## §8. Strict rules (from CLAUDE.md)

| Rule | Consequence of violating |
|------|--------------------------|
| **No f64 in production paths** (L1: 50-dps compute) | review-rejected; ⁴He wall regression to ~10s |
| **Three-calibration discipline** (CAL-1 = m_e, CAL-2 = 𝔇_β, CAL-3 = 𝔇_π) | any fourth-cal violation auto-rejected |
| **No fitting / numerology** | review-rejected (PR #843 / #852 audit) |
| **Combine related PRs** | 1.A + 1.C together; 1.B separate |
| **Structured branch names** `claude/<theme>-<utc-ymd>` | naming convention; coordinate.md relies on it |
| **CI is billing** | don't churn commits; squash where possible |
| **Cross-check tolerance 1e-25 minimum at 50-dps** | precision-floor must be respected |
| **NEVER edit `deploy/google-viewers.txt` / `github-collaborators.txt` / `.github/CODEOWNERS`** | protected files; owner-only |

---

## §9. Coordination checklist before opening your PR

- [ ] `git fetch origin main && git rebase origin/main` clean
- [ ] Run `/prepare-merge` per `.claude/skills/local/prepare-merge.md`
- [ ] Run witness-drift validators (4 of them; see §1·a of prepare-merge)
- [ ] Lean-ref migration check (`cd content && bun run migrate-lean-refs:dry`)
- [ ] Content validation (`bun run validate quantum-observable-universe`) if any .md touched
- [ ] One-voice audit on touched .md (if any)
- [ ] Cross-check vs Python LaurentQ on every atom in canonical set
- [ ] Bench results in `docs/audits/2026-05-21-rust-laurent-q-reduce-results.md`
- [ ] Update [`2026-05-20-compute-optimization-roadmap.md`](2026-05-20-compute-optimization-roadmap.md) to mark Tier 1.A as DONE
- [ ] Coordinate intent on any sibling PRs (see `local/coordinate` skill)

---

## §10. When you can say "done"

Tier 1.A is **done** when ALL six criteria are met:

| # | Criterion | Measurement |
|---|-----------|:------------|
| 1 | ⁶Li wall < 60 s | `python3 canonical_mass_table_extended.py --atoms 6Li --method laurent_q_rust` |
| 2 | ⁸Be wall < 5 min | same command, atom 8Be |
| 3 | Cross-check vs Python LaurentQ at 1e-25 | `tr_M_atomic_rust_full vs tr_M_atomic_lq.evaluate_mpf` on p..⁶Li |
| 4 | All cargo + python tests pass | `cargo test --release --lib && python3 laurent_q_trace.py` |
| 5 | CI `validate` green | GitHub Actions on the PR |
| 6 | Audit doc committed | `2026-05-21-rust-laurent-q-reduce-results.md` |

When these pass, **¹²C / organic chemistry is unlocked** (combined with Tier 1.B which you also ship).

---

## §11. After Tier 1.A

| Next | Why | Effort |
|------|-----|--------|
| Tier 1.C (cyclic cache canonical form) | quick win; ships on the 1.A PR | 1-2 hr |
| Tier 1.B (orbit reduction) | **gates ¹²C / organic chem** when combined with 1.A | 3-5 days |
| Tier 1.D (sweep cache verify) | already done? — verify first | 1 day max |
| Tier 4.E / 4.F (Bring S₅) | research-grade; separate PR; only if A=5 specifically becomes a bottleneck | weeks |

After Tier 1.B lands, organic-chemistry compute (¹²C, ¹⁴N, ¹⁶O) becomes routine. That's the real prize.

---

## §12. Standing requests from author

These are durable preferences (not session-specific):

1. **No f64 in production.** MPFR via `mpmath.mpf` at `dps=50+`.
2. **Heavy atoms + organic chem are the use cases.** Optimize for A ≥ 8, not for ⁴He.
3. **Rust where it helps; Python where it doesn't.** The roundtrip Python ↔ Rust costs ~50ns per call — only worth crossing for amortizable work (whole-atom compute, not per-multiplication).
4. **One PR, combined commits.** Per CLAUDE.md "Combine related work into one branch / one PR. Minimize their creation."
5. **Show benches in commit messages.** Concrete numbers, not "should be faster".

---

## §13. Pointers if you get stuck

| If you're stuck on… | Read | Or skill |
|---------------------|------|----------|
| Rust BigRational arithmetic | `tools/hecke-engine/src/laurent_poly_q.rs` (BigInt template) + `num-rational` docs | n/a |
| PyO3 patterns | `tools/pyhecke-native/src/lib.rs` (20+ existing fns) | n/a |
| Markov-axiom recursion | `markov_trace_canonical.py:_tr_M_word_impl` + `laurent_q_trace.py:_tr_M_word_lq_cached` | `compute-audit` skill |
| Hecke algebra background | `hecke_symbolic.py` + papers cited in `CLAUDE.md §7a` | n/a |
| Cross-PR coordination | `coordinate.md` | `coordinate` skill |
| /prepare-merge | `.claude/skills/local/prepare-merge.md` | `prepare-merge` skill |
| Witness-pipeline drift | `compute_audit_scan.py`, `derivation_chain_validator.py`, etc. | `compute-audit` skill |

---

## §14. Final reminder

The point isn't speedup-for-its-own-sake. The point is **unlocking ¹²C / ¹⁴N / ¹⁶O** so the framework can predict organic-chemistry observables. Tier 1.A is the gate. Tier 1.B compounds on it. Once both land, A ≤ 16 becomes routine and the QOU framework reaches the actual application target.

You have the full bottleneck audit, the full implementation template (#859), and a clear go-decision from the author. Good luck.

— previous agent
