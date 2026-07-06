---
name: compute-author
roles: [collaborator, owner]
description: >
  Pre-work briefing + durable patterns for anyone writing or modifying
  compute scripts under `computations/` or the Rust
  crates under `tools/`. Read this BEFORE you write or change compute
  code — it covers precision discipline, Rust↔Python boundary cost,
  exact-arithmetic choices (BigInt vs BigRational vs sympy.Rational),
  algebraic-preflight requirements before optimization shortcuts, and
  the canonical references for every load-bearing convention. Sibling
  to `compute-audit` (which is post-hoc); this skill is pre-work.
allowed-tools: Read Bash Grep Glob Edit Write Skill
---

# Compute-author skill — read before writing compute code

## Role

When a user (or you) is about to **author new compute** under
`computations/` (Python) or `tools/hecke-engine/`,
`tools/pyhecke-native/` (Rust), or modify existing compute scripts in
a way that touches precision, performance, or canonical-derivation
discipline — run this skill **before** any code change.

This is the pre-work counterpart to `local/compute-audit` (post-hoc
script review). Both share a vocabulary; this one gates entry, that
one gates exit.

**Workflow precondition** (AGENTS.md §Branch + PR workflow, STRICT):
before writing the first line of compute, create a branch
(`claude/<theme>-<utc-ymd>`) and open a PR. Commit early + commit
often; small structured commits cherry-pick cleanly. This is a
standing authorization for ALWAYS-PR — agents do not need to wait
for explicit "open a PR" from the user. Exception: integration-
watcher batch sweeps may bulk-commit.

## When to use this skill

Use this skill whenever a request mentions any of:

**Authoring intent:**
- "write new compute" / "optimize" / "optimise" / "port" / "rewrite"
- "make this faster" / "speed up" / "speedup"

**Precision / numerics vocabulary:**
- "precision" / "1 ppb" / "1ppb" / "tolerance"
- "float" / "float64" / "f64" / "double" — almost always means
  "STOP and use mpmath / BigRational instead"
- "symbolic" / "exact" / "Rational" / "BigInt" / "BigRational"
- "mpf" / "mpmath" / "mpfr" / "rug" / "dps" / "50 digits"
- "witness" (any new witness emission)

**Cross-language / build vocabulary:**
- "python" / "py" / "rust" — the very mention of crossing the
  language boundary triggers the boundary-cost decision rule (§2.1)
- "pyo3" / "maturin" / "cargo" / "wheel" / "extension module"
- "round-trip" / "boundary" / "FFI"

**Performance / resource vocabulary:**
- "memory" / "storage" / "OOM" / "leak" / "cache"
- "speed" / "fast" / "wall" / "elapsed" / "ETA"
- "bottleneck" / "hotspot" / "profile"

**Correctness / verification vocabulary:**
- "cross-check" / "agree to" / "matches" / "identity"
- "error" / "diff" / "residual" / "drift"
- "orbit-sum" / "preflight" / "verify the identity"

**Specific algorithmic touchpoints:**
- "BigInt vs BigRational" / "sympy.Rational vs LaurentQ"
- "LP/SDP" / "primal/dual" / "shadow price"
- "Markov trace" / "Hoefsmit" / "Wenzl" / "LR bridge" / "chi^λ"
- "atomic braid" / "Hecke" / "H_n(q)" / "q-deformation"
- Anything in `hecke_*.py`, `markov_*.py`, `laurent_*`,
  `tools/hecke-engine/`, `tools/pyhecke-native/`

**Pre-work questions:**
- "Should I use X here?" — the type / precision / boundary choices
- "How do I integrate Python and Rust?" — granularity rule (§2.1)
- "What's the precision target?" — L1 / L2 (§0)
- "I want to claim this trace is exactly zero" — algebraic preflight (§3)
- "I'm about to skip / amortize / cache something" — preflight (§3)

If your task touches LP/SDP duals, mass-table compute, Markov trace,
Hoefsmit / Wenzl / LR-bridge characters, atomic-braid construction,
or anything in the `hecke_*.py` / `markov_*.py` / `laurent_*.py`
family — this skill applies.

**Anything performance-related is in-scope for this skill, even if
the request looks small.** A one-line "use float64 here" change can
break the precision floor; the skill exists to catch that before the
code lands.

## §0. Canonical cheat-sheet pointers (read these first)

| Source | What it gives you | Read time |
|--------|-------------------|----------:|
| [`docs/precision-goals.md`](../../docs/precision-goals.md) | **L1 (compute precision) vs L2 (per-observable accuracy)** — what "1 ppb" means in QOU; substrate q_0 conventions; subgoals; CAL-2 floor | 15 min |
| [`AGENTS.md` §Precision goals (STRICT)](../../AGENTS.md) | three-calibration discipline (three masses CAL-1 m_e, CAL-2 m_μ, CAL-3 m_π; q₀ via m_μ/m_e; Q_β derived); no fitting; Δ_λ gate (no 7th ansatz) | 10 min |
| [`AGENTS.md` §LP/SDP duals — first-class infra](../../AGENTS.md) | every LP/SDP must emit `y0_star`, `y_star`, `active_set`, `primal_obj`, `dual_obj`, `duality_gap`; `lp_dual_solver.py` is the canonical entry | 5 min |
| [`.claude/skills/local/production-vs-exploratory-discipline.md`](production-vs-exploratory-discipline.md) | **CAL-4 / empirical-fit / numerology bright-line** — 3-category framework (production / exploratory / numerology), 13-driver canonical menu, Rule 14 escalation, q-locality gate, pre-promotion 7-step checklist. Read BEFORE deciding whether a candidate goes into a `*_50dps.py` production script or stays in a `probe_*.py` exploratory file. | 15 min |
| [`docs/audits/2026-05-20-compute-optimization-roadmap.md`](../../docs/audits/2026-05-20-compute-optimization-roadmap.md) | current optimization roadmap — Tier 1.A through 1.F | 10 min |
| [`docs/audits/2026-05-20-next-agent-handover.md`](../../docs/audits/2026-05-20-next-agent-handover.md) | step-by-step Tier 1.A starter (Rust LaurentQ port) | 30 min if working that tier |
| [`docs/audits/2026-05-20-markov-peel-bottleneck-profile.md`](../../docs/audits/2026-05-20-markov-peel-bottleneck-profile.md) | cProfile data + 4-strategy ranking that motivated #859 | 5 min |
| [`docs/audits/2026-05-20-rust-port-scoping-markov-peel.md`](../../docs/audits/2026-05-20-rust-port-scoping-markov-peel.md) | Rust port scoping; Phase-1+2 already done | 10 min |

For the algorithmic side:

| Source | What it gives you |
|--------|-------------------|
| `computations/_precision.py` | `COMPUTE_DPS_DEFAULT = 50`, `OUTPUT_DPS_DEFAULT = 40`, `PRECISION_GUARD = 10` — the production precision floor |
| `computations/q_parameter.py` | `Q_50_DIGIT_STR` — the canonical 50-dps substrate value (always pass as STRING; never round to float) |
| `computations/codata_constants.py` | CAL-1 / CAL-2 / CAL-3 anchors; **never inline a CODATA literal** (P31) |
| `computations/lp_dual_solver.py` | canonical LP/SDP entry point — always route LP/SDP through this |
| `computations/markov_trace_canonical.py` | reference `tr_M_word` implementation (the sympy baseline) |
| `computations/laurent_q_trace.py` | reference Python LaurentQ implementation (PR #859) — match bit-for-bit when porting |
| `tools/hecke-engine/src/laurent_poly_q.rs` | existing Rust LaurentPoly (BigInt) — template for new types |
| `tools/hecke-engine/src/tr_m_word_lq.rs` | Phase-2 Rust port style + PyO3 pattern (PR #859) |
| `tools/pyhecke-native/src/lib.rs` | 20+ PyO3 bindings as reference patterns |

### §0.1 Sandbox / fresh-container bootstrap (deps + native wheel)

A fresh cloud container often ships **neither** the Python deps **nor**
the compiled native wheel. Do **not** declare a compute "blocked (no
`pyhecke_native`)" — it is almost always buildable in-place. Bootstrap
order:

```bash
# 1. Core scientific deps (base python3 may lack them).
python3 -m pip install numpy mpmath sympy

# 2. In-repo pure-Python packages (Layer 2a/2b), editable.
python3 -m pip install -e tools/qou-substrate -e tools/pyhecke -e tools/witness-schema

# 3. pyhecke_native — NOT on PyPI yet (alpha), and the prebuilt wheel
#    is usually NOT shipped. BUT the container ships the Rust toolchain
#    (`cargo`, `rustc`) and the crate source (tools/pyhecke-native +
#    tools/hecke-engine), so build it from source via maturin (~1 min):
python3 -m pip install maturin
python3 -m pip install ./tools/pyhecke-native    # compiles + installs pyhecke_native
python3 -c "import pyhecke_native; print('native OK')"
```

Key facts (so agents stop mis-reporting the blocker):

- **The Rust toolchain ships in the web/cloud sandbox** (unlike the Lean
  `elan` host, which is firewalled — see
  [`lean-environment-setup.md`](lean-environment-setup.md)). `cargo build`
  works; only crates.io fetches need network (usually allowed).
- **The pure-sympy compute paths do NOT need native.** `markov_peel`,
  `markov_trace_canonical`, `char_fast`, and the symbolic `tr_M_atomic`
  (`use_fast=False`) run on numpy/sympy alone — D/T/³He/⁴He are all
  tractable without the wheel. Native is only needed for (a) speed and
  (b) large-A chi (H_18 ⁶Li / H_21 ⁷Li) where the sympy GS reducer
  scales ~10×/A unit and becomes infeasible.
- So "no `pyhecke_native`" blocks **only** the large-A Rust-kernel
  producers (e.g. `compute_atom_chi_rust.py 6Li 7Li`) *until you build
  the wheel* — after the `pip install ./tools/pyhecke-native` above, even
  those are unblocked. Corpus-grep / formalize-first discipline: build
  it before reporting a capability as unavailable.

## §1. Precision discipline (STRICT, no f64 in production)

**L1 floor: 50-dps compute / 40-dps output**, configurable via
`QOU_COMPUTE_DPS`. Every production path obeys this.

### §1.1 Numeric-type decision table

When choosing the coefficient / scalar type for a new compute:

| You need to represent… | Use | Rationale |
|------------------------|-----|-----------|
| Exact integer (q^k exponent, hook-length count) | Python `int`, Rust `i32`/`i64`/`BigInt` | exact, no precision issue |
| Exact rational (sympy.Rational, half-integer, q^{1/2} coefficient with denominator) | Python `sympy.Rational` or Rust `num_rational::BigRational` | exact, required for Markov-trace identities at q_0 |
| Real at 50-dps (substrate value, trace evaluation at q_0) | Python `mpmath.mpf` (always pass `q_str` as string), Rust `rug::Float` (MPFR) via decimal-string FFI | matches L1 floor |
| Floating-point f64 | **only for cross-checking** — clearly marked LOSSY in docstring | NEVER on the production critical path |

**Cross-check tolerance at 50-dps: `1e-25` minimum.** Not `1e-15`.
At 50-dps you have 50 significant digits; allowing a 1e-15 tolerance
defeats the precision floor. PR #859 uses 1e-30 as the bar.

**No `float(some_sympy_expr)` in production paths.** Convert via
`mpmath.mpf(str(sympy.N(expr, dps + 5)))` (decimal-string round-trip;
exact at the requested precision) or via `Rational.p / Rational.q`
when the value is rational.

### §1.2 Three-calibration discipline (STRICT)

Only three calibration anchors:

| # | Anchor | Source |
|---|--------|--------|
| CAL-1 | electron mass `m_e` | `codata_constants.M_E_MEV` |
| CAL-2 | muon mass `m_μ` (→ `q_0` via `m_μ/m_e`) | CODATA (phys-obs may anchor `q_0` on `m_p/m_e` for precision) |
| CAL-3 | charged-pion mass `m_π` (meson scale) | PDG (`Q_β` is *derived* from CAL-1+CAL-2, not a calibration) |

A **fourth calibration is forbidden.** Any compute that introduces a new
free parameter calibrated against an experimental observable will be
caught by the canonical-watcher (`.claude/skills/local/canonical-watcher.md`)
and rejected. The Δ_λ gate (per `AGENTS.md`) specifically forbids a
seventh ansatz for per-partition Δ_λ values — six have already failed.

### §1.3 No fitting / numerology

If your compute pattern-matches a numerical agreement (e.g. "this
trace equals 2q − 1 at q_0"), that's NOT a derivation. Either:

- (a) derive the structural identity from the categorical machinery
- (b) document the match as a **falsifiability probe** with explicit
  `_fit` / `_probe` suffix in the script name + audit-only witness
- (c) demote to a `remark` block (interpretation, not claim)

See `compute-audit.md §Anti-patterns this skill explicitly rejects`
for the "numerology" / "three-route convergence" / "universal-from-one-atom"
patterns to avoid.

## §2. Rust ↔ Python boundary cost (when to cross)

PyO3 boundary cost is **~50 ns per call**. This makes per-fine-grained
calls a loss: ⁵Li tr_M_atomic has ~37 M sympy compares; crossing the
boundary 37 M times costs 1.85 s of pure overhead, dwarfing any
algorithmic savings.

### §2.1 Granularity decision rule

| Call frequency per atom | PyO3 boundary cost | Net effect |
|------------------------:|-------------------:|-----------|
| 1 (whole-atom compute returns a structured result) | ~50 ns | trivial — go for it |
| 10s–100s (per-reduced-word trace) | ~5 μs | acceptable — boundary amortized |
| 1000s–10K (per-sub-step in a recursion) | ~500 μs–5 ms | borderline — must measure |
| 1M+ (per-coefficient arithmetic op) | seconds | **FORBIDDEN — boundary dominates** |

**The right Rust port granularity:** port the WHOLE COMPUTE (atomic word,
reduce, trace) as a single PyO3 call. Python builds the input + reads
the output; Rust does everything in between.

PR #859's Phase-2 follows this: `pyhecke_native.tr_m_word_lq(word, n_strands)`
is called per reduced σ-word (hundreds per atom, not millions of times),
not per-coefficient-multiplication.

### §2.2 What NOT to do

```python
# BAD — per-call boundary cost dominates
for word, coef in reduced_element.terms.items():
    for q_exp, sym_coef in coef.coefs.items():
        # millions of crossings — STOP
        result = pyhecke_native.bigrational_mul(c_num, c_den, ...)
```

```python
# GOOD — one boundary crossing per atom
reduced_bytes = pyhecke_native.incremental_reduce_rust(word, max_iter)
trace_bytes   = pyhecke_native.tr_m_atomic_rust(Z, N, dps)
# decode/evaluate in Python
```

### §2.3 FFI marshalling format

For complex objects (LaurentQ polynomials, ZHLaurent traces) across
the boundary: serialize as **flat structured Python lists** (no
custom Python objects on the Rust side; no bincode/msgpack unless
you've measured the alternative). PyO3 ferries `Vec<(i32, String)>`
easily; the decimal-string representation of BigInt/BigRational
preserves arbitrary precision.

See `tools/pyhecke-native/src/lib.rs` `chi_lambda_all_partitions_mpfr`
for the established pattern.

## §3. Algebraic-preflight discipline

Before optimizing via symmetry / orbit-sum / shortcut identities,
**prove (or numerically falsify) the identity on the smallest
non-trivial case first.** Do NOT ship the shortcut until the identity
is established.

### §3.1 Preflight protocol

```
Decide which symmetry / shortcut you want to exploit
    │
    ├── Step 1: write down the identity in narrative
    │           (e.g. "tr_M(β_{Z,N}) = |S_Z × S_N| · tr_M(orbit_rep)")
    │
    ├── Step 2: pick the smallest atom where it's non-trivial
    │           (orbit size ≥ 4; usually ⁴He)
    │
    ├── Step 3: compute BOTH sides at 50-dps via the existing
    │           (slow but correct) path
    │
    ├── Step 4: check rel.diff < 1e-25
    │           │
    │           ├── PASSES → repeat on next smallest atom (⁵Li, ⁶Li)
    │           │           If all pass → implement
    │           │
    │           └── FAILS → STOP. Document the failure in
    │                       docs/audits/<date>-<identity-name>-falsified.md
    │                       with the numerical witness. Investigate
    │                       sign convention / orbit structure. Do NOT
    │                       ship the shortcut.
```

### §3.2 Common false identities (don't ship without proof)

| Claim | Trap |
|-------|------|
| "Markov trace is invariant under nucleon permutation" | TRUE only if the permutation is a CONJUGATION in H_{3A}; mixed-species permutations involve I_pp / I_pn / I_nn interface swaps that are NOT pure conjugations |
| "tr_M(reversed word) = tr_M(word)" | FALSE — Markov trace is cyclic, not reversal-symmetric |
| "tr_M(σ ⊗ σ') = tr_M(σ) · tr_M(σ')" | FALSE for inter-strand-coupled braids; only true for disjoint tensor factors per Wenzl 1988 §1.7 |
| "λ_p_scale derivable from N-tier Bring-Bloch search at coeff bound K" | NEGATIVE through K = 10⁸ across 6 tiers (PR #843 + #852) — don't keep retrying the same shape |
| "Trace cyclic rotation does not affect cache identity" | TRUE — but the rotation must affect ONLY the cache key, NOT the recursion behavior |

### <a id="formalize-first"></a>§3.3 Formalize-first probe discipline (STRICT — narrow the search BEFORE running it)

**Too much time is lost chasing numerical rainbows that a one-line
structural argument — or a small Lean lemma — would have eliminated up
front.** Before launching a numerical search/scan over a *hypothesis
class* (a family of candidate closed forms, a PSLQ basis, a partition /
character / root-of-unity enumeration, a recursion-kernel fit), STOP and
ask whether a **formalizable structural claim prunes the class first**.

**Protocol — one step at a time:**

1. **State the hypothesis class** you would probe
   (e.g. "c_3 = f(q) for some *real-q* closed form"; "A = ℚ-combo of these
   12 periods"; "the residue is a partition invariant for λ ⊢ n ≤ 5").
2. **Find the structural invariant the whole class must satisfy** — parity,
   bar-symmetry, a degree / anchor bound, cross-anchor rigidity, search-
   space entropy vs available precision, a Lean-provable constraint.
3. **Formalize it** — a Lean lemma (even *conditional* / `sorry` + a
   `-- Ref:` citation per the §3b-cond pattern), or a rigorous symbolic
   argument — that the class provably satisfies or violates.
4. **Let the result narrow the probe:**
   - class REFUTED structurally → **do not run the numerical scan at all**;
   - a structural property CONSTRAINS the class → probe only the surviving
     sub-class;
   - brute-enumerate **only** what formalization cannot prune.

**Worked precedents (each cost a probe cycle that a formalize-first step
would have saved):**

| structural argument (cheap) | killed (expensive) |
|---|---|
| `dc_3/dq ≈ 4.6e6` is impossible for a smooth real `f` ([PR #1821](https://github.com/litlfred/qou/pull/1821)) | the entire **real-q `c_3 = f(q)`** family — incl. the 4-session c_3 flip-flop + sl_6 / residual numerical scans |
| entropy bound `precision > n_terms·log10(2·height)` ([PR #1805](https://github.com/litlfred/qou/pull/1805)) | the **12-constant PSLQ** search — at A's ~11 digits ANY relation found is spurious |
| A is asymptotically ~4 sig figs from `c_2..c_10` ([PR #1805](https://github.com/litlfred/qou/pull/1805)) | **high-precision identifications** of A — pointless until canonical c_11+ exists |
| finite linear-algebra rank check ([commit `eca145ca`](https://github.com/litlfred/qou/commit/eca145ca)) | the **constant-kernel recursion** — refuted through depth 4 before any fit |

**Lean granularity for pruning.** The formalized claim may be a
*conditional / scaffolding* lemma (sorry-free machinery, or `sorry` +
`-- Ref:`). Per the c_k/d_k registry §1, *machinery-proved ≠ values-
derived* — but a sorry-free **conditional** still narrows the search and
makes the pruning auditable. The point is to bound the search, not to
claim a closure.

**When NOT to formalize-first.** If the formalization is harder than the
probe AND the probe is cheap and decisive, just run the probe. This rule
targets **wide / expensive** searches that a cheap structural argument
would prune — not every one-off check. Use judgment: formalize-first when
the hypothesis class is large and a structural invariant is plausible.

Cross-ref: `production-vs-exploratory-discipline.md` (which probes are
exploratory), `proof-gap-audit.md` §K (declaring "open"), and the
"Before declaring open math" corpus-grep checklist in AGENTS.md (the
complement: formalize-first prunes *forward*; corpus-grep prunes
*backward* against already-known results).

### <a id="formalize-the-refutation"></a>§3.4 Formalize-the-refutation (turn a dead ansatz into a Lean disproof)

Formalize-first (§3.3) prunes a class *before* the scan. Its mirror prunes
*after*: when a numerical probe **refutes** a candidate closed form, do not
let the refutation live only in prose + a witness JSON — **formalize the
disproof** so the dead ansatz cannot be silently re-proposed. Adopted from
AlphaProof Nexus's disproof path (numeric counterexample → formalized →
proved it refutes the conjecture; arXiv:2605.22763, Green #57; see
[`docs/audits/2026-06-06-alphaproof-nexus-comparative-assessment.md`](../../../docs/audits/2026-06-06-alphaproof-nexus-comparative-assessment.md)).

**When to use.** A hypothesis-class member (a Δ_λ closure ansatz, a c_k
closed form, a recursion kernel) has been refuted at a concrete anchor by a
witnessed computation, and "do not re-propose this" is currently enforced
only by reviewer vigilance (e.g. the Δ_λ "no 7th ansatz" rule).

**Pattern.** State the ansatz and its refuting evaluation as a Lean lemma
whose conclusion is the **inequality** at the witnessed anchor:

```lean
-- The ansatz: a proposed closed form for the deferred quantity.
def ansatzΔ (lam : Partition) : ℝ := …   -- e.g. a Frobenius co-Casimir form

-- The refutation: at the witnessed anchor the ansatz misses the required
-- value by more than tolerance. requiredΔ_deuteron, the residual, and tol
-- are :leanval-pinned to a witness, so the numbers cannot drift.
theorem ansatzΔ_refuted_deuteron :
    tol_deuteron < |ansatzΔ deuteronPartition - requiredΔ_deuteron| := by
  -- unfold; norm_num / native_decide against the :leanval-pinned literals
  -- Ref: <witness JSON producing requiredΔ_deuteron + residual>
  sorry  -- replace with the discharged numeric inequality
```

**Discipline:**
- The literals are `:leanval[…]`-pinned to the producing witness
  (`witnessed-values.md`) — the disproof is only as current as its witness;
  refresh per the witness-staleness rules.
- The lemma's `-- Ref:` cites the **witness JSON**, not "we checked once".
- File the disproof beside the conjecture it kills; the conjecture's `.md`
  links to it, so a future agent grepping the ansatz finds the refutation
  (the backward complement of formalize-first).
- This **operationalises** the `production-vs-exploratory-discipline.md`
  "no Nth fit" rules: a refuted ansatz becomes a machine-checked `≠`, not a
  prose warning.

**Worked exemplar — Frobenius co-Casimir Δ_λ, refuted at the deuteron.**
Numbers pinned from
[`rho-k-h3a-co-casimir.witness.json`](../../../computations/rho-k-h3a-co-casimir.witness.json)
(`allPassed: true`, 50 dps; Option B of
[`docs/audits/2026-05-18-delta-lambda-gating-context.md`](../../../docs/audits/2026-05-18-delta-lambda-gating-context.md)).
The ansatz predicts a binding-density sum `+0.144959…` (m_e units); the
empirical target `−B_D/m_e` is `−4.353367…` — wrong sign, magnitude off by
≈30.03× (closure gap `4.498326…`, matching the witness). Stated as a decidable
rational inequality so it compiles with no `sorry`:

```lean
namespace QOU.BraidKnot.DeltaLambdaRefutation

/-- Frobenius co-Casimir predicted Σ_λ y_λ χ^λ Δ_λ at the deuteron (m_e units);
    12 sig figs from `/data/co_casimir_prediction/sum_contributions_signed`. -/
def coCasimirSum : ℚ :=  144959224127 / 1000000000000   -- ≈ +0.144959224127

/-- Empirical −B_D/m_e (m_e units), from `/data/target_signed`. -/
def targetSigned : ℚ := -4353367281870 / 1000000000000   -- ≈ −4.353367281870

/-- Viability tolerance (the ansatz misses by > 4, with the wrong sign). -/
def tol : ℚ := 1

/-- **Refutation.** The Frobenius co-Casimir ansatz misses the deuteron target
    by more than tolerance (gap ≈ 4.498 m_e units).
    -- Ref: [manuscript] rho-k-h3a-co-casimir.witness.json -/
theorem coCasimir_refuted_deuteron : tol < |coCasimirSum - targetSigned| := by
  unfold tol coCasimirSum targetSigned
  norm_num  -- norm_num handles |·| on ℚ natively

end QOU.BraidKnot.DeltaLambdaRefutation
```

*Status (illustrative — not compiled; verify in CI):* the inequality's
arithmetic is verified exactly — the gap `4498326505997/10^12` equals the
witness `closure_gap`. The Lean proof is the standard rational form but is
**not** compiled in this session (the Mathlib
cache is unavailable in the sandbox; AGENTS.md "Mathlib cache 403 fallback"),
so build it in CI / a warmed env before citing it as machine-checked. Promoting
it to a committed content-object `lem:frobenius-cocasimir-refuted-deuteron`
beside
[`conj:rho-prefactor-structural`](../../../content/quantum-observable-universe/braids-and-knots/conj-rho-prefactor-structural.md)
(GAP-A-4) is the natural follow-up (`.ts`/`.md`/`.lean` triple + green build).

## §4. Rust-port patterns (when porting Python to Rust)

### §4.1 Type-mapping cheat-sheet

| Python (LaurentQ) | Rust target | Notes |
|-------------------|-------------|-------|
| `sympy.Rational` | `num_rational::BigRational` | exact rational; pure-Rust no system deps |
| `sympy.Integer` | `num_bigint::BigInt` | exact integer |
| `dict[int, sympy.Rational]` (LaurentQ.coefs) | `BTreeMap<i32, BigRational>` | deterministic iteration order; lookup O(log n) |
| `tuple[int, ...]` (Hecke word) | `Vec<u32>` | 0-based generator indices throughout |
| `mpmath.mpf` | `rug::Float` (MPFR) | for boundary numerical evaluations only |
| `LaurentHeckeElement.terms: dict[tuple, LaurentQ]` | `BTreeMap<Vec<u32>, LaurentRationalQ>` | the "sparse Hecke element" |

### §4.2 Cargo features — what to enable

Default `cargo build` in `tools/hecke-engine/` does NOT enable:

- `clarabel-sdp` — pulls in OpenBLAS / netlib / gfortran (system deps)
- `clarabel-bigrational` — pulls in clarabel + rationals
- `clarabel-mpfr` — pulls in clarabel + rug MPFR

**Don't enable these features unless you specifically need them.**
The default build covers LaurentPolyQ, Wenzl, seminormal, and the
new Markov-axiom recursion — all without Clarabel.

### §4.3 Maturin build workflow

```bash
# Build (no virtualenv required if you use `build` not `develop`)
cd tools/pyhecke-native
maturin build --release
# Install the wheel
pip install --break-system-packages --force-reinstall \
    target/wheels/pyhecke_native-*-cp311-*-x86_64.whl
# Smoke test
python3 -c "import pyhecke_native; print(pyhecke_native.__version__)"
```

**`maturin develop` requires a virtualenv** — if you're in a venvless
session, use `maturin build` + `pip install` instead.

### §4.4 Long-compute logging discipline (from compute-audit.md)

Any compute > 5 min wall: launch with `python3 -u` + tee to `/tmp/<name>.log`.
Emit progress lines every ~10 s with wall + ETA. If a BG script ends
silently with 0-byte output and no completion notification, assume
crashed — re-launch with stricter logging.

See `compute-audit.md §Long-compute logging discipline` for the full
rules.

## §5. Witness-emission discipline

Every compute script ships with a `*.witness.json` (per
`witness_base.py`). The witness must include:

| Field | Source | Notes |
|-------|--------|-------|
| `name`, `description`, `computation` | author | match the docstring |
| `engine` | author | `"python"`, `"mpmath"`, `"numpy"`, `"sympy"`, `"rust"` |
| `scriptFile`, `scriptHash`, `scriptCommitSha` | `WitnessBuilder` | auto-populated |
| `computedAt`, `durationMs` | `WitnessBuilder` | auto-populated |
| `parameters` | author | `compute_dps`, `target_dps`, etc. |
| `data` | author | the actual results |
| `assertions` | author (via `add_assertion`) | every claim is a structured assertion with computed/expected/tolerance/source |
| `auditOnly` or full pipeline | author | `set_audit_only(doc_path)` if this is research-grade |

For LP/SDP witnesses specifically: also emit `y0_star`, `y_star`,
`active_set`, `primal_obj`, `dual_obj`, `duality_gap` per AGENTS.md
§LP/SDP duals.

## §6. CI / merge etiquette

- **CI is billing.** Don't churn commits. Squash where possible.
- **Combine related PRs** per AGENTS.md "minimize PR creation".
- **Branch naming:** `claude/<theme>-<utc-ymd>`. Pattern is load-bearing
  for `coordinate.md` + upload-branch idempotency.
- **/prepare-merge** at the end. Address Gemini + Copilot review
  comments mechanically; don't argue cosmetic findings.
- **Cross-check tolerance 1e-25 at 50-dps.** Never claim "passes at 1e-15".

## §7. Quick gotchas table

| Symptom | Cause | Fix |
|---------|-------|-----|
| Result drifts by ~1e-7 between two methods | one path uses f64 internally | switch to mpmath / BigRational |
| Cross-check passes at 1e-15 but fails at 1e-25 | tolerance set too loose | tighten — the 50-dps precision floor demands 1e-25 minimum |
| `maturin develop` fails: "no virtualenv" | maturin requires venv for develop | use `maturin build --release` + `pip install` |
| Cargo build pulls in OpenBLAS | accidentally enabled `clarabel-sdp` feature | remove the feature flag |
| Per-call PyO3 boundary cost dominates | granularity too fine | port the WHOLE compute, one PyO3 call per atom |
| Symbol drift after rebase: q^{1/2} vs q | LaurentPolyQ vs LaurentRationalQ key convention | check the encoding (`q_half_exp = 2 * q_exp` in `laurent_poly_q.rs`) |
| Witness fails drift detector | self-emitting audit witnesses bumped `files_scanned` | regenerate the 4 audit witnesses; commit as "post-rebase drift refresh" |
| `tr_m_word_lq` raises `RuntimeError: Case C` | atomic braid hit multi-top-1 segment | caller falls back to sympy ocneanu — don't implement Case C in Rust |
| Compute crashes silently with 0-byte BG output | sympy stack overflow or OOM | re-launch with `python -u` + tee + progress lines |
| Sympy round-trip dominates ⁵Li+ profile | reduce path still in Python | port `incremental_reduce_rust` to Rust (Tier 1.A roadmap) |
| Orbit-sum identity gives wrong tr_M | claimed symmetry isn't a conjugation | do §3 preflight before shipping orbit shortcuts |

## §8. Pre-work checklist (use before every compute change)

- [ ] I have read `docs/precision-goals.md`
- [ ] I have read `AGENTS.md §Precision goals` and `§LP/SDP duals`
- [ ] I have identified which **calibration anchor** my new compute touches (CAL-1 / 2 / 3, or none)
- [ ] My coefficient types are **exact** (BigInt / BigRational / sympy.Rational) — no `float`/`f64` in production paths
- [ ] Cross-check at 1e-25 vs the existing reference path is planned
- [ ] If exploiting a symmetry / orbit / shortcut: §3 algebraic preflight is run on the smallest non-trivial atom
- [ ] If porting to Rust: granularity is **whole-compute per PyO3 call** (§2.1)
- [ ] Witness emission plan: includes `parameters`, `assertions`, LP/SDP duals if applicable
- [ ] Long-compute scripts launch with `python -u` + tee
- [ ] Branch name follows `claude/<theme>-<utc-ymd>`
- [ ] Combined with related work on one PR (per AGENTS.md "minimize PR creation")
- [ ] **MBA-appendix sync.** If the script realises a step of the canonical chain (Steps 1–11 per [`docs/canonical-derivation-cheat-sheet.md §0`](../../../docs/canonical-derivation-cheat-sheet.md)) or one of the sidecar algorithms (Δ_λ closure, c_k truncation ladder, LP/SDP dual emission, witness-JSON pipeline), the matching `alg:`-block under [`content/quantum-observable-universe/appendix-mass-binding-algorithms/`](../../../content/quantum-observable-universe/appendix-mass-binding-algorithms/) must be updated in the **same commit** (or at the latest in the same PR): `uses[]` cites the upstream provables you used, `computation.script` / `computation.witness` point at the new files, and the .md body's *Algorithm* / *Correctness* / *Python API* sections reflect the new signature. Reviewers will check the appendix diff against the compute diff.

If any box is unchecked, **stop and resolve before writing code**.

## §9. Sibling skills

- [`local/compute-audit`](compute-audit.md) — post-hoc review of compute
  scripts (30 P-patterns P1–P30). This skill (compute-author) is
  pre-work; compute-audit is post-hoc.
- [`local/canonical-watcher`](canonical-watcher.md) — catches four-cal /
  numerology / fits violations on incoming compute.
- [`local/compute-integration-watcher`](compute-integration-watcher.md) —
  cross-layer wiring check (is a paper claim actually consumed by
  production compute?).
- [`local/prepare-merge`](prepare-merge.md) — merge workflow when your
  compute work is ready to ship.

## Anti-patterns this skill explicitly rejects

- **Writing compute without reading the cheat sheet** (§0 references).
  Every gotcha in §7 has a precedent — almost certainly already
  documented.
- **Optimizing without a profile** — per P29 of compute-audit, profile
  first to identify the actual bottleneck. Don't guess.
- **Per-call PyO3 crossings** — the boundary cost dominates (§2.1).
  Always port whole computes.
- **f64 in production** — the L1 floor is 50-dps; f64 truncates at 1e-15.
- **Shortcut identities without algebraic preflight** — orbit-sums,
  cyclic invariance, tensor-factorization claims must be verified
  numerically at 50-dps on the smallest non-trivial case before
  shipping.
- **Inline CODATA literals** — always route through `codata_constants.py`
  (P31).
- **A fourth calibration anchor** — only CAL-1 / 2 / 3 exist; any new
  free parameter calibrated against experimental data is rejected.
