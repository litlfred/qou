# 2026-06-09 — Binding-energy compute audit: depth-stratified is canonical default

## TL;DR for agents

**Default binding-energy compute** is the depth-stratified canonical chain via:

- `computations/binding_depth_stratified_rust.py` (preferred — Rust kernel for n ≥ 9)
- `computations/binding_depth_stratified_lr.py` (LR combiner — for A ≥ 4 via per-nucleon H_3 → H_{3A})
- `computations/binding_depth_stratified.py` (Python fallback)

Witness JSONs (all on `main`):
- [`binding-depth-stratified-rust.witness.json`](../../computations/binding-depth-stratified-rust.witness.json) (6 atoms: D, T, ³He, ⁴He, ⁶Li, ⁷Li)
- [`binding-depth-stratified-lr.witness.json`](../../computations/binding-depth-stratified-lr.witness.json)
- [`binding-depth-stratified.witness.json`](../../computations/binding-depth-stratified.witness.json) (⁴He deferred)
- [`binding-depth-stratified-selfconj.witness.json`](../../computations/binding-depth-stratified-selfconj.witness.json)
- [`binding-depth-stratified-knot-weighted.witness.json`](../../computations/binding-depth-stratified-knot-weighted.witness.json)

## What "canonical" means here

The depth-stratified compute implements the framework's canonical chain
Steps 5-8 (Wedderburn → Frobenius pairing → GB filtration → jet tower):

```
H_n(q) → ⊕ M_{d_λ}(ℚ(q))           ← Step 5 Wedderburn
tr_M  = Σ y_λ χ_λ                   ← Step 6 Frobenius pairing
J^•(q) by Coxeter length            ← Step 7 GB filtration
E_∞ collapses at E_2 (claim)        ← Step 8 jet order
```

The binding-energy contribution is the **depth-graded sum** over the
GB filtration tower:

$$B(K) \;=\; m_e \cdot \sum_{k \geq 0} \alpha_k \cdot \sum_{w \in J^k / J^{k+1}}
   y_w \cdot (\chi^\lambda_{\text{free}}(w) - \chi^\lambda_{\text{atom}}(w))$$

with `α_k` the per-depth dimensional coefficient (1 at depth 0-1, q-corrected at higher k).

## ⚠ Honest status

`canonical_status` field in **all** depth-stratified witnesses reads:

```
canonical-with-empirical-assignment
```

**Correction (2026-06-09 within this session):** the `α_k`
coefficients are **NOT empirical fits** — they are structurally
defined constants (see
[`binding_depth_stratified_rust.py:62-70`](../../computations/binding_depth_stratified_rust.py)):

```python
def alpha_k(k: int) -> mp.mpf:
    z_mark = 1 / (mp.sqrt(Q0) + 1 / mp.sqrt(Q0))   # Markov braid-trace marker
    G = mp.catalan                                  # Catalan's constant
    if k in (0, 1, 3):  return 1                    # trivial layers
    if k == 2:          return z_mark ** 2          # ≈ 0.2493
    return M_E_MEV * 8 * G                          # ≈ 3.7445 = m_e · Vol(L6a4)
```

| k | α_k | source |
|---|---:|---|
| 0 | 1 | identity layer |
| 1 | 1 | depth-1 trivial |
| 2 | z² ≈ 0.2493 | Markov braid-trace marker² at q = q₀ |
| 3 | 1 | center of H_3 (special) |
| ≥ 4 | m_e · 8G ≈ 3.7445 | ⁴He magic-A `Vol(L6a4) = 8G` plateau |

What "canonical-with-empirical-assignment" actually means is the
**per-depth ASSIGNMENT rule** — which constant goes to which k,
with α_3 = 1 special-cased back to trivial instead of continuing
the Markov-marker series, and α_{k≥4} = m_e · 8G extended as a
flat plateau from the ⁴He magic-A formula. It is NOT a recursion
`α_k = f(α_{k-1})`, and it is NOT derived from a single substrate
principle. That is the unclosed gap.

## Numerical state (per witnesses 2026-06-09, post-regen)

| atom | depth-stratified B_pred | B_AME | ratio | gap |
|---|---:|---:|---:|---:|
| D (²H) | 0.607 MeV | 2.225 | 0.273 | **−73 %** |
| T (³H) | 2.808 MeV | 8.482 | 0.331 | **−67 %** |
| ³He | 2.653 MeV | 7.718 | 0.344 | **−66 %** |
| ⁴He | 14.063 MeV | 28.296 | 0.497 | **−50 %** |

LR and Rust direct now agree to 3 dp for every atom (verified by
re-running both against the now-complete 77/77 ⁴He cached atom chi
witness on 2026-06-09). The 2.089 "LR overshoot" reported earlier
was 100 % an artifact of a stale binding witness consuming a 24/77
partial cached chi witness — corrected. See "Prevention" §below.

**The canonical depth-stratified compute does NOT close binding at the
10 % threshold.** D / T / ³He under-bind by ~67-73 %; ⁴He under-binds by
50 %. The per-depth α_k assignment rule is not yet substrate-derived
(cf. cheat sheet "open Barrier-1"). LR and Rust direct now agree
exactly across all four atoms (verified post-regen 2026-06-09).

**Compare against the flat magic-A formula** `B(⁴He) = 2·m_e·A·Vol(L6a4)
= 2·m_e·4·8G = 29.96 MeV` (+5.87 %, no per-depth structure): the flat
formula BEATS the depth-stratified tower sum on ⁴He (50 % undershoot).
This says the tower sum is under-weighting some depth bands rather than
monotonically refining the magic-A result. The unclosed structural gap
is **not** at low depth (where the magic-A flat result lives) but in
the α_2 / α_3 / α_{k≥4} assignment choices.

## Lean status

There IS Lean infrastructure for the depth-stratified framework, but
not a closure-grade proof:

- `content/quantum-observable-universe/lean/QOU/BraidKnot/DepthStratifiedFrobeniusReciprocity.lean`
  — `conj:depth-stratified-frobenius-reciprocity` (§3b-cond class)
- `content/quantum-observable-universe/lean/QOU/BraidKnot/BlockMultiplicativityVFree.lean`
  — `prop:block-multiplicativity-v-free` (used by LR combiner)

These provide the structural framework. The individual α_k constants
(`z² = (1/(√q+1/√q))²` and `m_e · 8G`) have structural origin in
the Markov braid-trace and the L6a4 Borromean link complement volume,
but the **per-depth assignment rule** mapping k to constant is NOT
Lean-proved — that's the §3b-cond gap.

## What this means for agents

### DO

1. **Use `binding_depth_stratified_rust.py`** (or LR variant for A ≥ 4)
   as the default binding-energy compute. Cite the witness JSON.
2. **Cite the `canonical_status = canonical-with-empirical-assignment`
   field** when reporting binding numbers — this flags that the
   PER-DEPTH ASSIGNMENT RULE for α_k is empirical, not derived (the
   individual α_k constants themselves are structural, see §Honest
   status above).
3. **Report the ratio `B_pred / B_AME`** alongside any binding number
   so the unclosed structural gap is visible.

### DO NOT

1. **Do NOT** invent new closure formulas (Coulomb correction, cross-
   isotope bar-symmetric, etc.) without first checking the framework's
   existing decompositions. The Δ_λ gate is mis-framed (cheat sheet §9.3
   2026-06-02 update); single-multiplicative ansätze are forbidden by
   the three-calibration discipline.
2. **Do NOT** treat the +5.87 % magic-A `2·m_e·A·8G` formula as a
   universal binding formula. It applies only to ⁴He's doubly-magic
   shell, and even there overshoots by 5.87 % structurally (see
   `binding_factor_f_decomposition.py` for the factorisation
   `Vol(K_bind) = 8G · f(Z, N) · Δtr` where `f` is currently
   AME-extracted, not derived).
3. **Do NOT** chase the Option E v9 cross-isotope `(1+q)/2` 0.11 %
   "closure" — retracted as CAL-4 numerology (cheat sheet §9.3 +
   [`docs/audits/2026-05-31-isospin-mirror-v9-discipline-assessment.md`](2026-05-31-isospin-mirror-v9-discipline-assessment.md)).

## The 6-knot multiplicative-closure interpretation (cheat-sheet
update target)

Per cheat sheet Step 4 ("Bring χ = −6 → 6 basis elements ↔ 6 torus
knots ↔ particle content fixed"), the 6 are the basis-element
generators of `H_3(q)` — NOT 6 independent SM-equivalent operators.
The full binding spectrum is the **multiplicative closure** of those
6 generators climbing the GB filtration / jet tower:

- **Depth 0**: identity (1 generator)
- **Depth 1**: σ_1, σ_2 (2 generators)
- **Depth 2**: σ_1 σ_2, σ_2 σ_1 (2 products)
- **Depth 3**: σ_1 σ_2 σ_1 = σ_2 σ_1 σ_2 (center, 1)

Total: **6 H_3 basis elements**. Each contributes binding at its depth
order via the depth-stratified compute.

The user's observation "we need ALL knot operators not just 6 generators"
is correct — and the framework's depth-stratified compute already
implements this (the tower sum). The remaining gap (67-73 % undershoot
for D / T / ³He) is the per-depth α_k assignment being empirical.

## Why the tower undershoots — structural diagnosis

The depth-stratified tower under-performs the flat magic-A formula
`2·m_e·A·8G` (+5.87 %) on ⁴He (-50 % undershoot, both Rust direct and
LR variant after the 2026-06-09 partial-witness fix). Four structural
reasons:

### (i) Dimensional mismatch within α_k

| k | α_k | dimension |
|---|---|---|
| 0, 1, 3 | 1 | dimensionless |
| 2 | z² = (1/(√q+1/√q))² ≈ 0.249 | dimensionless (Markov braid-trace marker²) |
| ≥ 4 | m_e · 8G ≈ 3.74 | **MeV** |

Φ_k is dimensionless (Σ_{depth=k} (dim_q²/qfact)·log|χ·dim_q|), so
the contribution `α_k · Φ_k`:

- at low depth (k ≤ 3) is dimensionless but is added to MeV totals as if MeV;
- at high depth (k ≥ 4) is genuinely MeV.

The formula is dimensionally inhomogeneous — the low-depth terms
are numerically small enough that the answer looks MeV-scaled, but
the categorical justification for adding dimensionless and MeV
contributions is missing.

### (ii) Chi-difference concentration vs α_k weighting are anti-correlated

`Φ_atom` and `Φ_free` use the **same** `chi_q_atomic` on the **same**
H_{3A} braid word, only toggling interface-knot crossings at gens
`3k+2`. Interface crossings are length-1 elements ⇒ the chi
DIFFERENCE (the relevant quantity) concentrates at **low depth**.

- At low depth (k ≤ 3): chi-differences are large; α_k = 1
  (dimensionless) → small dimensionless contribution.
- At high depth (k ≥ 4): chi structures nearly coincide (atom and
  free share H_{3A} content); chi-differences are small; α_k = m_e·8G
  (MeV) → small MeV contribution.

The depth where weight is largest is exactly where the chi-difference
is smallest. By construction, the tower can never deliver the full
magic-A binding through this sum.

### (iii) Compute-path consistency — verified (post-2026-06-09 regen)

LR and Rust direct now agree exactly per atom (the earlier "4× spread"
was a stale-witness artifact; see (iii-bis) below).

### (iv) No slot for the `A` scale factor

Magic-A is `B(⁴He) = 2·m_e·A·Vol(L6a4) = 2·m_e·4·8G`. The `A`
factor (nucleon count) is essential to the +5.87 % match. **No
single `α_k · Φ_k` term in the tower carries an `A` factor** — α_k
depends on k alone; Φ_k is a sum over partitions of fixed total `3A`
(implicit A but only via partition shapes, not as a scale multiplier).

A per-depth additive sum is structurally incapable of producing the
magic-A scaling rule. To do so would require either an explicit `A·`
prefactor on the whole tower (breaking the per-depth decomposition)
or an `A`-dependent α_k recursion (not what the current formula
provides).

### (iii-bis) The earlier "LR ≠ Rust" reading was wrong — stale-witness artifact

An earlier version of this audit claimed LR over-counted via tensor
multiplicities. That was incorrect. The reason:

`binding_depth_stratified_lr.py:21-26` docstring says LR computes
**only the FREE config** (the disjoint Hecke product
`β_p·β_n·…` in the parabolic subalgebra H_3^A ⊂ H_{3A}, the q-shuffle
convolution structure of `markov_trace_3A(include_inter=False)`).
The ATOM config chi comes from a CACHED witness produced by the same
`chi_q_atomic` Rust kernel as the direct path. LR does not
"factorize away" interface crossings — it never sees them.

The LR branching formula

$$\chi^\lambda(\beta_p\cdot\beta_n\cdots) = \sum_{\mu_1,\ldots,\mu_A\vdash 3} c^\lambda_{\mu_1\cdots\mu_A}\,\chi^{\mu_1}(\beta_p)\cdots$$

is the Mathas (1999) §3 LR rule, **mathematically exact** for elements
in the parabolic. Verification: re-running LR + Rust on 2026-06-09
gives identical ratios (0.273 / 0.331 / 0.344 / 0.497) for all four
of D / T / ³He / ⁴He.

The earlier "LR 2.089" reading came from a stale binding witness
that captured a 24/77 partial cached ⁴He atom chi witness; the chi
witness was upgraded to 77/77 after, but
`binding-depth-stratified-lr.witness.json` was never regenerated
until this audit forced it. See "Prevention" §below.

### Synthesis

Magic-A succeeds by **not decomposing** — it identifies ⁴He with the
whole-nucleus Vol(L6a4) and multiplies by `2·A` as a structural
scale rule. The depth-stratified tower **decomposes too far**, asking
the chi-differences to do work they cannot (they concentrate at the
wrong depth, the formula has no `A` slot, and compute paths
disagree).

The remaining open question is whether a different decomposition —
e.g. a **multiplicative tower** `B = m_e·Π_k(1 + α_k·Φ_k)` rather
than additive, or an `A`-scaled outer factor — could reconcile the
tower with magic-A. This is the natural follow-up to the per-depth
α_k assignment-rule problem.

## Prevention: avoid future "partial cached witness → inflated binding" bugs

The ⁴He LR vs Rust 4× spread reported in earlier sessions was
**100 % an artifact** of a stale binding witness that captured a
24/77 partial cached ⁴He atom chi witness; the chi witness was later
upgraded to 77/77 but the binding witness was not regenerated.
Re-running `binding_depth_stratified_lr.py` on 2026-06-09 against
the current chi witness gives `B(⁴He)/AME = 0.497` — identical to
Rust direct.

Discipline to prevent recurrence:

### 1. Witness-completeness gate at the consumer

`binding_depth_stratified_lr.py` now checks every cached atom chi
witness against `PARTITION_COUNTS = {3:3, 6:11, 9:30, 12:77, 15:176,
18:385, 21:792}` (the p(n) values for relevant strand counts) and:

- prints a `⚠ {atom} cached atom chi PARTIAL: X/expected partitions`
  warning at run time;
- records `partition_completeness_warnings` and
  `all_atom_chi_witnesses_complete` fields in the output witness JSON
  so downstream consumers see the partial state.

Missing partitions still get substituted as 0 (unchanged behaviour),
but the substitution is **surfaced**, not silent.

### 2. Standalone audit

[`chi_witness_completeness_audit.py`](../../computations/chi_witness_completeness_audit.py)
walks every `chi-*-at-q0-*.witness.json` in
`computations/`, compares `len(by_partition)` to
`p(n_strands)` from `PARTITION_COUNTS`, and produces
`chi-witness-completeness-audit.witness.json` with an assertion
that the incomplete count is 0. Run as part of the canonical /
compute integration watchers.

### 3. Routine to refresh stale binding witnesses

Any binding-energy compute that consumes cached chi witnesses
records the `n_partitions_atom` it observed at run time. If
`n_partitions_atom < p(n_strands)` for any atom in the latest
binding witness, regenerate the binding witness as follows:

1. Re-run `compute_atom_chi_rust.py {atom}` (or the producer that
   wrote the cached chi witness) until `n_cached = p(n_strands)`.
2. Re-run all consumer binding scripts
   (`binding_depth_stratified_rust.py`,
   `binding_depth_stratified_lr.py`,
   `binding_depth_stratified.py`,
   `binding_depth_stratified_selfconj.py`,
   `binding_depth_stratified_knot_weighted.py`).
3. Diff the resulting binding witnesses — any |ratio_LR / ratio_Rust − 1|
   > 0.01 signals a residual mismatch worth investigating.

### 4. Cross-path consistency assertion

LR and Rust direct should agree to floating-point tolerance for every
atom once cached witnesses are complete (verified on 2026-06-09 for
D, T, ³He, ⁴He: all agree to 3 dp). Treat any future LR vs Rust
disagreement as a partial-witness symptom first, not a structural
finding.

### 5. Extend to atoms beyond cache

`compute_atom_chi_rust.py 6Li` (H_18, 385 partitions) and `7Li`
(H_21, 792 partitions) have not been run. The depth-stratified
witnesses report `deferred` for those atoms. Generating their
cached chi witnesses + then their binding witnesses extends the
canonical default compute beyond A=4.

## Open compute lever

**Substrate-derive the per-depth ASSIGNMENT rule.** The constants
themselves are structural (z² Markov braid-trace marker; 8G = Vol(L6a4)
Borromean volume) — what's missing is the **rule that picks which
constant lives at each depth k**, including:

1. Why does α_2 take the Markov z² (and not, say, z·dim_q or z⁴)?
2. Why does α_3 = 1 break the series back to trivial (the H_3 center
   element) — does the GB filtration genuinely give α_3 = 1 or is
   that a leftover convention?
3. Why is α_{k≥4} the m_e · 8G ⁴He magic-A constant, and why does it
   plateau rather than continue some Markov-marker recursion?

A genuine recursion `α_k = f(α_{k-1}, q, k)` derivable from the
Wedderburn → Frobenius → GB filtration chain would CLOSE the
remaining gap. The framework explicitly forbids per-isotope α_k
tuning ([`binding_ladder_catalog.py:63`](../../computations/binding_ladder_catalog.py)
warning: α-ladder is fitted; per-isotope inconsistency was the
falsification of the fitted route).

## Option 4 (operator-valued combiner) status — already on main, blocked at A ≥ 3

Per the synthesis recommendation, the structural fix for the per-depth
α_k assignment problem is the operator-valued combiner, NOT α_k
retuning. The infrastructure is already on main:

| Component | File | State |
|---|---|---|
| Combiner | [`canonical_tr_m_via_branching.py`](../../computations/canonical_tr_m_via_branching.py) | A=2 end-to-end; A ≥ 3 returns `None` with diagnostic |
| A-operator extracts | `sublemma_2_1_A_operator_extract*.py` (H_6, H_9, H_12) | ✅ partial coverage; H_15 / H_18 missing |
| Q-value chain | `branching-qvalue-chain.py` | ✅ |
| Atom-level branching | `sublemma_2_1_deuteron_branching.py`, `sublemma_2_1_h12_he4_branching.py` | ✅ scripted |
| Interface-knot binding | `binding_via_interface_knot.py` | T1+T2 finite; T3 divergent for A ≥ 2 |

**Documented blocker (`canonical_tr_m_via_branching.py:218-252`):**
the H_9+ A-operator extracts are **rank-deficient** (least-squares
fits over the H_3 inner-test family, NOT universal). Empirically:
- A=2 deuteron matches `markov_peel` at 7e-15 (H_6 extract IS full-rank)
- A=3 tritium / ³He differ from `markov_peel` by 21-42 % (H_9 extracts under-fitted)
- A ≥ 3 returns `None` rather than silently-wrong values

**Three closure paths documented in code:**
1. Regenerate H_9 / H_12 / H_15 / H_18 extracts with test-word set
   large enough to make rank ≥ n_unknowns for every λ — explodes at H_18
   (e.g. [4,3,1,1] needs ≥ 3390 test words).
2. Build truly recursive ρ_ξ via matrix-form Wenzl branching identity
   (requires operator-form A^λ reconstruction, not just trace form).
3. Fall back to canonical `markov_peel.tr_M_atomic` for the inner — gives
   the correct |tr_M| symbolically at any q, at the cost of bypassing
   the combiner's speedup.

**Recommended next concrete step**: rather than writing a new
`binding_via_operator_combiner.py` from scratch (which would just
re-cover the existing A=2 work), pick one of:

- **path 3 follow-up** ✅ **DONE (this PR)**: see
  [`binding_combiner_markov_peel_fallback.py`](../../computations/binding_combiner_markov_peel_fallback.py)
  + [`binding-combiner-markov-peel-fallback.witness.json`](../../computations/binding-combiner-markov-peel-fallback.witness.json).
  Forms `B = E_0·(|tr_M^free| − |tr_M^atom|)` from the canonical
  markov_peel trace; succeeds for **every** A (D, T, ³He, ⁴He), with
  the A ≥ 3 atoms — the exact ones `canonical_tr_m_via_branching.py`
  returns `None` for — passing a machine-checkable
  `a3plus_atoms_bypass_rank_deficiency_blocker` assertion. Results
  below.
- **path 1 follow-up** ✅ **DONE for A=3 / nn (this PR)**: the H_9
  extract regenerated over the full S_6×S_3 permutation basis (native
  chi) is full-rank for all 30 λ⊢9, and tritium Path A vs Path B agrees
  at machine ε (max rel res 1.22e-13). The "larger test-word family" the
  audit anticipated is specifically the **permutation basis** (the
  bare-σ family was degenerate). See §"Path 1 CLOSED at A=3" below.

### Path 3 result (markov_peel trace difference) — blocker-free but does NOT close

Run 2026-06-09 (50 dps, 81 s wall for D/T/³He/⁴He):

| atom | A | \|tr_M^free\| | \|tr_M^atom\| | B_dim | B (E_0) MeV | B (m_e) MeV | B_AME | ratio (E_0) | tower ratio |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| D | 2 | 0.9835 | 0.3883 | 0.5952 | 0.466 | 0.304 | 2.225 | **0.209** | 0.273 |
| T | 3 | 0.9080 | 0.1041 | 0.8040 | 0.629 | 0.411 | 8.482 | **0.074** | 0.331 |
| ³He | 3 | 1.0478 | 0.2065 | 0.8412 | 0.658 | 0.430 | 7.718 | **0.085** | 0.344 |
| ⁴He | 4 | 0.9673 | 0.0553 | 0.9120 | 0.713 | 0.466 | 28.296 | **0.025** | 0.497 |

`E_0 = E_0_CALIBRATION_MEV` (Q_β CAL-3 ≈ 0.7823 MeV); the `m_e` column
re-scales by CAL-1 (≈ 0.654×) for cross-comparison. "tower ratio" is
the depth-stratified default from the table above.

Two conclusions:

1. **Path 3 is blocker-free.** It computes A ≥ 3 binding via the exact-
   symbolic canonical trace with no A-operator extracts at all — the
   rank-deficiency wall that stops `canonical_tr_m_via_branching.py` at
   A ≥ 3 never arises. This is now a baseline the operator-valued
   combiner (PR #1698 track) must beat once its extracts are full-rank.
2. **The trace difference does NOT close binding** — and is *worse* than
   the depth-stratified tower at every atom, with the gap widening as A
   grows (ratio falls 0.209 → 0.025 D → ⁴He). This is the direct
   numerical confirmation of §"Why the tower undershoots" (iv): a
   per-atom `|tr_M|` difference carries **no A-scale ("magic-A")
   factor**, so it structurally cannot reproduce `2·m_e·A·8G`. Path 3 is
   thereby closed off as a *closure* mechanism.

**Convention finding (corrects the path-3 sketch above).** The sketch
said "uses `markov_peel.tr_M_atomic`". In fact `tr_M_atomic` hardcodes
the canonical default `pn_convention="bring_color_weighted"`, whose p-n
interface crossing `σ − h·(½ − δ/4)` carries a **numeric**
`δ = flavor_split_subleading(q₀)`. The markov_peel trace path is
exact-symbolic in the *formal* variable q (`crossing_from_cd` maps each
crossing to an exact element of ℚ(q)·H_n(q)), and a numeric δ cannot be
a polynomial in formal q — so `tr_M_atomic(include_inter=True)` raises
`unknown (c, d) crossing` for every atom. The implemented script
therefore builds the bound word with `pn_convention="strict_averaged"`
(color-blind `σ − h/2`) and traces via the markov_peel primitives
directly. The color weighting it drops is a sub-0.1 % perturbation on
one crossing coefficient (δ ≈ 1.4e-3) — negligible against the 5–40×
binding shortfall, and the free config has no interface crossing at all,
so the binding *difference* stays convention-consistent.

## Path 1 CLOSED at A=3 (2026-06-09 follow-up) — the H_9 rank deficiency was a degenerate test-word set, not a structural wall

The audit's path-1 ("regenerate H_9 extracts with a larger test-word
family") is now done, and it **closes the operator-valued branching
combiner at A=3** (tritium) at machine ε. The earlier "rank-deficient ⇒
under-fitted ⇒ 21–42% A=3 mismatch" was a symptom; the **root cause is
the degenerate test-word family**, not a structural limit of the
branching ansatz.

### Diagnosis (formalize-first)

The Phase-1 H_9 extract used a hand-picked 12-word H_6 family (bare-σ
products, length ≤ 3). Probed directly, that family's `ρ_ξ` image spans
only a fraction of `End(V_ξ)`:

| ξ ⊢ 6 | d_ξ² | bare-σ span (≤len 4, 791 words) | S_6 perm basis (720 words) |
|---|---:|---:|---:|
| (3,2,1) | 256 | **97** (partial) | **256** (FULL) |
| (4,2) | 81 | 69 | 81 (FULL) |
| (4,1,1) | 100 | 78 | 100 (FULL) |

By the double-centralizer theorem `ρ_ξ(H_6) = End(V_ξ)`, so the **full
S_6 permutation basis** (the 720 reduced words `T_w`, w ∈ S_6) spans
`End(V_ξ)` exactly — verified above. The bilinear interface system is
`χ^λ(W6·I_2·W3) = Σ c^λ_{ξν} Tr(A^λ_{ξν}·(ρ_ξ(W6)⊗ρ_ν(W3)))`; once the
test data spans `End(V_ξ)⊗End(V_ν)` there is **no gauge freedom** in
`A^λ_{ξν}`, so the extracted operator is the true intertwiner (Schur /
double-centralizer) and generalizes to the deuteron-inner — which is
exactly what the A=3 case needs.

### Result (regenerated witnesses on this branch)

`sublemma_2_1_A_operator_extract_h9.py --interface nn --full-basis
--native` → **all 30/30 λ ⊢ 9 over-determined and consistent at
~1e-14** (was rank 14/30 for (8,1), 66/3390 for (4,3,1,1)).

`sublemma_2_1_h9_tritium_verify.py --atom tritium` → **Path A (direct
χ^λ via Hoefsmit) vs Path B (iterated Sub-lemma 2.1 with the full-basis
A): all 30/30 λ agree, max rel residual 1.22e-13.** The 21–42% mismatch
is gone.

⇒ The operator-valued branching combiner (Sub-lemma 2.1) is
**mathematically correct at A=3**; the prior failure was 100% the
degenerate test words. This reconciles with the audit's path-b
(matrix-form Wenzl): the full-basis extraction realizes the same
intertwiner determinacy empirically.

### What made it tractable: native chi + S_n symmetry

- **S_n symmetry** supplies the spanning set: the S_6×S_3 permutation
  basis (720×6 words) is the minimal guaranteed-full-span test family.
- **`pyhecke_native`** (built from source in-container — see
  [`compute-author.md §0.1`](../../.claude/skills/local/compute-author.md))
  evaluates χ^λ via `chi_lambdas_braid` (rayon-batch) at **4475/s vs
  ~5/s** pure-Python — the full 129,600-eval basis runs in **8.2 s** vs
  ~7 h. The `nn` interface is `σ⁻¹` (pure braid), so it maps directly to
  a native braid word.

### Scope and scaling (honest)

- **Closed: nn (tritium).** ³He needs the **pn** interface, whose
  averaged crossing `σ − (h/2)·1` is a Hecke combination, not a braid
  generator. Route it through native via **linearity**:
  `χ(W·(σ−h/2)·W') = χ(W·σ·W') − (h/2)·χ(W·W')` (two braid evals). Then
  the same closure applies. Follow-up.
- **Combiner None-gate** (`canonical_tr_m_via_branching.py:252`) can now
  be lifted for the nn-closable atoms; H_12 (A=4) is tractable the same
  way.
- **H_18 (⁶Li) and beyond do not scale**: the full S_n basis is `n!`
  (17! at H_18) — infeasible. There the direct `markov_peel` path, or a
  **multiplicity-space (intertwiner) parametrization** of `A^λ_{ξν}`
  (dimension `c^λ_{ξν}` ≪ `(d_ξ d_ν)²`, the categorical/Schur reduction),
  is the route. This is the natural next research step beyond path 1.
- **Binding physics unchanged.** This closes a *compute-wiring* gap (the
  combiner now works at A=3), NOT the binding-closure gap — binding
  still under-binds (magic-A scale factor missing; see the markov_peel
  trace-difference result above). The combiner gives correct per-λ χ
  decompositions, not new binding.

## See also

- [`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md)
  §9 (Bind row + §9.3) — authoritative framing of the Δ_λ gate's
  mis-framing + bond-sum / many-body re-direction
- [`docs/audits/2026-05-31-isospin-mirror-v9-discipline-assessment.md`](2026-05-31-isospin-mirror-v9-discipline-assessment.md)
  — retraction of Option E v9 (1+q)/2 0.11 % claim
- [`docs/audits/2026-06-02-binding-many-body-ceiling.md`](2026-06-02-binding-many-body-ceiling.md)
  — pairwise chain-sum captures 26 % of ⁴He
- [`docs/audits/2026-06-02-he4-binding-canonical-vs-full-theta-design.md`](2026-06-02-he4-binding-canonical-vs-full-theta-design.md)
  — canonical magic-A `2·m_e·A·Vol(L6a4)` analysis + +5.87 % residual
- [`binding_factor_f_decomposition.py`](../../computations/binding_factor_f_decomposition.py)
  — extracted f(Z, N) values + pairwise-bond model falsification
