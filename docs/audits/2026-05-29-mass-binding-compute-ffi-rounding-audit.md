# Mass + binding compute audit — bottlenecks, Rust coverage, FFI rounding, library replacement

**Date:** 2026-05-29
**Trigger:** Repo-owner question — "is mass and binding calculations, where
are performance bottlenecks? has everything been moved over to rust that
would make sense? double check rounding tripping rust→python→rust. any
python libraries need to be replaced with rust?"
**Skills:** [`local/compute-audit`](../../.claude/skills/local/compute-audit.md)
+ [`local/ffi-roundtrip-audit`](../../.claude/skills/local/ffi-roundtrip-audit.md).
**Environment constraint:** this audit ran in a container with `cargo`
available but **no `mpmath` and no pip network** — so the Python compute
scripts could not be executed and no q₀ cross-check / re-bench was run.
Empirical numbers below are cited from the prior audit docs (which carry
the benches); all *static* findings (call-site shapes, import graphs,
doc-vs-code drift) were verified by reading the current tree.

---

## TL;DR — answers to the four questions

1. **Bottleneck.** The whole mass/binding pipeline bottoms out in one
   place: `markov_peel.tr_M_atomic` (Markov trace of the atomic braid
   `β_{Z,N}` in `H_{3A}`). Within it the **reduce loop** dominates — on
   ⁶Li it is ~80% of wall (~80 s of ~95 s), now running in Rust
   (`reduce_laurent`) over exact `BigRational` coefficients. The
   downstream trace recursion + MPFR substitution is the remaining ~20%.

2. **Rust coverage.** The hot path *is* in Rust (Tier 1.A: reduce + trace
   + MPFR, single PyO3 call; Tier 1.C: cyclic cache key). What is **not**
   moved and would make sense:
   - **Tier 1.B nucleon-orbit reduction** — the single biggest remaining
     lever (36× ⁶Li, 576× ⁸Be), never built; gated on an unproven
     orbit-trace identity.
   - **`hecke-mass`** Rust binary already computes a full Z=1..20 mass
     table but is **not wired** into the canonical pipeline (1-strand vs
     3-strand-per-nucleon convention mismatch).
   - **Binding scripts** are almost entirely pure-mpmath; they consume
     trace *witnesses* rather than recomputing, so this is mostly fine —
     except the f64 cross-check variant (see §3).

3. **FFI rounding (rust→python→rust).** **No precision-tripping found on
   the production path.** `tr_M_atomic_rust_full` is a *single* PyO3
   crossing returning one MPFR decimal string; cross-checks bit-identical
   to `5.6×10⁻⁴⁹` relative. The only multi-crossing paths
   (`_rust_recursive`, the prefix-cache `_with_state`) shuttle **exact
   integers / exact `BigRational` state**, not rounded floats — so they
   are lossless by construction, and neither is the production path
   anyway. The one genuine precision *ceiling* is the **f64** atom-chi
   witness path feeding `binding_depth_stratified_rust.py` (see §3).

4. **Python libraries to replace.** `sympy` has already been displaced on
   the hot trace path (→ Rust `BigRational`); the ~161 remaining sympy
   importers are mostly symbolic-derivation / probe scripts where it is
   the right tool. `mpmath` (466 files) is the correct final-evaluation
   kernel and should stay. The two concrete replacement candidates are
   **`scipy.optimize.linprog` / SDP solves → the existing Rust Clarabel
   binary** (`clarabel_certify.rs`), and **eliminating the residual
   `sympy.Rational` arithmetic inside any LaurentQ Python fallback** (the
   Rust path already does this). Full detail in §4.

---

## 1. Where are the performance bottlenecks?

### Critical path

Every mass and binding observable flows through the Markov trace of an
atomic braid:

```
canonical_mass_table_extended.py            (sweep driver)
  → markov_peel_rust_bridge.tr_M_atomic_rust_full   (--method laurent_q_rust)
      → pyhecke_native.tr_m_atomic_mpfr[_cached]     (ONE PyO3 call)
          → reduce_laurent  (R1+R2+R3, BigRational)   ← BOTTLENECK (~80%)
          → tr_m_word_lq    (Markov-axiom recursion)  ← ~15%
          → MPFR substitution at q₀                   ← ~5%
```

### Empirical bottleneck ranking (⁶Li, from the prior profiles)

| Component | Share of ⁶Li wall | In Rust? | Symmetry-exploitable? |
|-----------|------------------:|:--------:|:----------------------|
| `reduce_laurent` fixpoint (BigRational `__mul__` + BTreeMap insert + word clone per R1 fire) | **~80%** | yes | **YES — nucleon S_Z×S_N orbit (unused, Tier 1.B)** |
| `tr_m_word_lq` recursion across reduced σ-words | ~15% | yes | partly (cyclic canonical key — done) |
| MPFR substitution at q₀ | ~5% | yes | n/a |

Source: [`2026-05-22-rust-laurent-q-reduce-results.md`](2026-05-22-rust-laurent-q-reduce-results.md)
§"Why we're at 2.4×, not 4×" and
[`2026-05-20-markov-peel-bottleneck-profile.md`](2026-05-20-markov-peel-bottleneck-profile.md).

**Historical note.** Pre-Rust, the dominant cost was *sympy machinery*
(`Basic.compare` 37 M calls, `sympify`, `add.flatten` = ~46% of wall in
trace assembly). That has been eliminated by the Tier 1.A port — the
sympy round-trip in trace assembly is gone on the `laurent_q_rust` path.

### Current state of the 4× gate

⁶Li: **84.5 s** (rust) vs 60 s target — **gate still open** at ~2.65×
over the Python LaurentQ baseline. The residual is pure BigRational
arithmetic inside the reduce fixpoint (≈4000 reduced terms × ~40
q-exponents × ~50 passes). The three landed micro-opts (R1 fast-path,
FxHashMap intermediate, GCD deferral) net ~2.4×→3.0× on small atoms but
are flat on ⁶Li. **Algorithmic reduction of the input word length
(Tier 1.B) is the only lever that changes the asymptotics.**

---

## 2. Has everything been moved to Rust that would make sense?

### Already in Rust (production)

| Layer | File | Status |
|-------|------|:------:|
| `LaurentRationalQ` (q-Laurent, BigRational coefs) | `tools/hecke-engine/src/laurent_rational_q.rs` | ✅ |
| `LaurentHeckeElement` | `tools/hecke-engine/src/laurent_hecke_element.rs` | ✅ |
| `reduce_laurent` (R1+R2+R3) | `tools/hecke-engine/src/reduce_laurent.rs` | ✅ |
| `tr_m_atomic_mpfr` (end-to-end + MPFR) | `tools/hecke-engine/src/tr_m_atomic_mpfr.rs` | ✅ |
| cyclic-canonical cache key (Tier 1.C) | `tools/hecke-engine/src/tr_m_word_lq.rs` | ✅ |
| χ^λ batch APIs (rayon) `chi_lambda(s)_braid`, `chi_q_atomic_all_partitions`, `chi_lambda_all_partitions_{f64,mpfr}` | `tools/pyhecke-native/src/lib.rs` | ✅ |

### NOT moved — ranked by ROI

1. **Tier 1.B — nucleon-orbit reduction `(S_Z × S_N)`.** ★★★ The atomic
   braid `β_{Z,N}` is invariant under permuting like nucleons; quotienting
   the word by its `S_Z × S_N` orbit shrinks the reduce *input* by `Z!·N!`
   (⁶Li 36×, ⁸Be 576×, ¹²C ~520K×). This compounds multiplicatively with
   the Rust reduce and is **the gateway to A≥8 / organic chemistry**.
   *Blocker:* the orbit-trace identity is unproven — the orbit action mixes
   conjugation with `I_pp/I_pn/I_nn` interface swaps, so it is **not**
   obviously a pure conjugation. Must be proven (Lean or numeric on
   ⁴He→⁵Li) **before** the optimization can be trusted. This is a
   research step, not a mechanical port.

2. **`hecke-mass` binary wiring.** ★★ `target/release/hecke-mass` already
   emits a full Z=1..20 binding/mass table (0.5–0.85% error) but uses a
   1-strand-per-nucleon convention vs the canonical 3-strand color-tube
   framing. Needs a convention adapter + A≤6 cross-check before it can be
   added as an L1.5 predictor track. Est. 1–2 days.
   Source: [`2026-05-19-rust-l1-wiring-status.md`](2026-05-19-rust-l1-wiring-status.md).

3. **LP / SDP conic solves → Clarabel (Rust).** ★ See §4 — 4 callers use
   `scipy.optimize.linprog`; the Rust `clarabel_certify.rs` binary exists
   but Python LP/SDP callers do not route through it.

### Should stay in Python (deliberately)

- **Binding scripts** (`binding_*.py`) are mostly pure mpmath and consume
  precomputed trace witnesses. The Σ_λ combine and the
  `B = E_0·(|tr_M(W_free)| − |tr_M(W_atom)|)` arithmetic is cheap (≤ ~200
  partitions). No Rust port warranted; the cost is upstream in the trace.
- **Symbolic-derivation / probe scripts** (the ~161 sympy importers) —
  sympy is the right tool for closed-form algebra; not a hot path.

---

## 3. Rounding: rust → python → rust

**Verdict: no precision-tripping on the production path.** Detail:

### Production path — clean single crossing

`tr_M_atomic_rust_full` (`markov_peel_rust_bridge.py:290`) makes **one**
PyO3 call to `tr_m_atomic_mpfr`, which does the entire reduce → trace →
MPFR-substitution chain inside Rust and returns **one** decimal string.
Python does `mp.mpf(result_str)` once. There is no Rust→Python→Rust
shuttle. Cross-check vs `tr_M_atomic_lq.evaluate_mpf` is **5.6×10⁻⁴⁹**
worst-case relative across p…⁶Li (per the Tier 1.A results doc) — i.e.
exact to working precision. The only rounding event is the final
MPFR→string at `dps` (default 50), done once, ~10 orders below the
40/50-dps serialization floor and ~35 orders below the ppt research need.

### Multi-crossing paths exist but are lossless

- `tr_M_atomic_rust_recursive` (same file) does python→rust→python *per
  reduced word*, returning ZHLaurent coefficients as **BigInt decimal
  strings**. Integers round-trip exactly; the q^exp powers are then
  accumulated in mpmath at `dps`. No rounding loss — but it is **not** the
  production path (only `markov_peel_rust_bridge.py`'s own smoke test
  calls it; `canonical_mass_table_extended.py` uses `_rust_full`). It is
  effectively superseded and could be marked deprecated.
- The prefix-cache path `tr_m_atomic_mpfr_with_state` ships the reduced
  Hecke **state** (exact `BigRational` numerator/denominator string pairs)
  back into Rust. Also exact. And it is documented as a net-loss
  experiment, off by default.

### The one real precision *ceiling* (flag, not a bug)

`binding_depth_stratified_rust.py` reads `atom-chi-rust-{atom}.witness.json`
at **f64** precision (the docstring says so explicitly) and forms the
binding **difference** `free − atom`. A difference of two ~0.05-magnitude
traces that cancels 2–3 leading digits leaves ~12–13 significant digits
out of f64's ~15–16 — **below the 50-dps L1 compute floor**. This is
acceptable for that script's role (an exploratory f64 cross-check) and the
**production** binding path (`binding_canonical.py`) instead uses the
closed-form `tr_M(𝓑_K)` via `tr_m_wenzl_bridge_mpfr` (MPFR, line ~197), so
production binding is *not* f64-capped. Recommendation: regenerate the
`atom-chi-rust-*` witnesses via the MPFR batch API
(`chi_lambda_all_partitions_mpfr`) if those f64 witnesses are ever
promoted into a precision-sensitive consumer. **Requires an mpmath+wheel
environment to regenerate + cross-check — deferred.**

---

## 4. Python libraries needing Rust replacement

| Library | Files | Verdict |
|---------|------:|---------|
| `sympy` | 161 | **Mostly keep.** Already displaced on the hot trace path (→ Rust BigRational). Remaining users are symbolic-derivation / closed-form / probe scripts where sympy is correct. 373 `simplify`/`cancel` sites exist but P16 (the production trace) already opts out via `simplify=False`. No bulk port warranted. |
| `mpmath` | 466 | **Keep.** Correct arbitrary-precision *final-evaluation* kernel. The Rust side already uses MPFR (`rug`) for the hot path; mpmath is the Python-side combine + the binding arithmetic, which is cheap. |
| `numpy` | 121 | **Keep** (f64 linear algebra, Gram matrices, witnesses). Not a wall. |
| `scipy` | 18 | **One real candidate:** `scipy.optimize.linprog` (4 callers) + the sparse `eigsh`/`LinearOperator` SDP feasibility solves. The Rust **Clarabel** binary (`tools/hecke-engine/src/bin/clarabel_certify.rs`) already exists for exactly this. Routing the LP/SDP operator-selection solves through it would give a Rust conic solver with the dual variables the LP/SDP-dual CI rule requires. Est. medium effort; needs the per-witness cross-check. |

**Bottom line:** the high-value library replacement already happened
(sympy→BigRational on the trace path). The remaining net-positive port is
**scipy LP/SDP → Clarabel**, and it is modest. There is no case for a
wholesale mpmath/numpy→Rust migration — those are the right tools where
they are used, and they are not the bottleneck.

---

## Issues fixed in this session (doc-currency, verifiable by inspection)

1. **`precision-goals.md` precision constants were stale.** Doc said
   `COMPUTE_DPS_DEFAULT = 50 / OUTPUT_DPS_DEFAULT = 40 / GUARD = 10`; the
   live code `tools/qou-substrate/python/qou_substrate/precision.py`
   (re-exported by the `_precision.py` shim) is **65 / 50 / 15**. Synced
   the doc to the code.
2. **CLAUDE.md L1 row** carried the same stale "50 dps compute / 40 dps
   serialization" parenthetical — synced to 65/50 for consistency with its
   own cited authoritative reference (`precision-goals.md`).
3. **`ffi-roundtrip-audit.md` offender catalogue was stale.** 5 of the 7
   "open" offenders (`delta_lambda_fr_identity_phase5c`,
   `chirality_avg_content_chiral`, `chirality_avg_content_atomic`,
   `constit_factor_varying_q_phase5k2`, `compute_atom_chi_rust`) have since
   been migrated to the batch `chi_lambdas_braid` / `chi_q_atomic_all_partitions`
   APIs (F-A / F-B applied, visible `# F-A:` comments). 1 was superseded by
   the single-call `tr_M_atomic_rust_full` (F-C). Only the N=3
   `chirality_braid_average.py` per-shape loop remains, which is correctly
   F-D-exempt. Marked the catalogue RESOLVED with current status.

---

## Greenlight-ready roadmap (needs an mpmath + pyhecke_native env to verify)

None of these were landed this session because the container cannot run
the mandatory q₀ cross-check (no mpmath / no wheel). In priority order:

1. **Tier 1.B nucleon-orbit reduction** — first *prove* the orbit-trace
   identity (Lean or numeric ⁴He→⁵Li), then build
   `atom_braid_orbit_representative(Z,N)`. Single biggest lever; unlocks
   A≥8 + organic chem. (Research + ~3–5 days impl.)
2. **scipy LP/SDP → Clarabel** — route operator-selection solves through
   `clarabel_certify.rs`; emit primal+dual per the LP-dual CI rule. When
   porting, preserve the objective under any variable transformation: if
   the solver operates on contribution variables
   $x_\lambda' = y_\lambda \chi^\lambda \Delta_\lambda$ (rather than the raw
   $x_\lambda$), the cost vector must be rescaled by
   $1/|y_\lambda \chi^\lambda|$ so the minimised weighted L1 norm still
   targets the intended objective.
3. **`hecke-mass` wiring** — convention adapter + A≤6 cross-check, then add
   as an L1.5 predictor track.
4. **Deprecate `tr_M_atomic_rust_recursive`** — superseded by `_rust_full`;
   keep one cross-check test, drop it from the live menu.
5. **Regenerate f64 atom-chi witnesses at MPFR** if/when any
   precision-sensitive consumer reads them.

## Implementation update (2026-05-29) — LP + SDP → Clarabel

Roadmap item 2 was implemented this session (PR #1440):

- **LP (done, verified).** `tools/hecke-engine/src/operator_selection_lp.rs`
  solves the operator-selection LP over the `litlfred/Clarabel.rs` **MPFR**
  backend (167 bits ≈ 50 dps), replacing scipy HiGHS f64. The dual
  sign-mapping is proven by 5 cargo tests (strong duality, KKT,
  complementary slackness, dual nonnegativity, feasibility). A JSON CLI
  (`clarabel-operator-selection-lp`) bridges to Python via decimal
  strings; `pyhecke.lp_dual_solver.solve_operator_selection_lp` gains a
  non-regressing `backend="clarabel"` opt-in (default stays scipy).

- **SDP (done for the diagonal lift; genuine dense-PSD blocked on
  LAPACK).** The existing `solve_psd_operator_selection_sdp` enforces
  `M(x) = diag(Gx) ⪰ 0`, which is *exactly* the LP's componentwise
  `Gx ≥ 0`. So `backend="clarabel"` there faithfully delegates to the
  verified MPFR LP and repackages as `SdpDualResult` — exact for the
  diagonal lift, no cvxpy/SCS. A **genuine dense-PSD** Clarabel solve
  (off-diagonal / moment-matrix lift) needs Clarabel's PSD cone, which
  requires either `clarabel-sdp` (f64; its `sdp-netlib` build **fails in
  this container with `cmake::fail`** — no CMake/gfortran/OpenBLAS
  toolchain) or an MPFR PSD eigensolver. Tracked as a follow-up; it needs
  a LAPACK-capable build env.

- **Verification gate.** `computations/clarabel_lp_crosscheck.py`
  compares scipy LP, clarabel LP, and clarabel SDP on the dummy + random
  SPD-Gram LPs (objective, active set, strong duality). Run it in a
  scipy+numpy env before flipping any default backend.

## Cross-references

- [`2026-05-20-compute-optimization-roadmap.md`](2026-05-20-compute-optimization-roadmap.md) — Tier menu + projected A-reach.
- [`2026-05-22-rust-laurent-q-reduce-results.md`](2026-05-22-rust-laurent-q-reduce-results.md) — Tier 1.A benches + 4× gate.
- [`2026-05-20-markov-peel-bottleneck-profile.md`](2026-05-20-markov-peel-bottleneck-profile.md) — original cProfile.
- [`2026-05-19-rust-l1-wiring-status.md`](2026-05-19-rust-l1-wiring-status.md) — hecke-mass / convention mismatch.
