# 2026-06-09 — Binding-energy compute audit: depth-stratified is canonical default

## TL;DR for agents

**Default binding-energy compute** is the depth-stratified canonical chain via:

- `folio-assistant/computations/binding_depth_stratified_rust.py` (preferred — Rust kernel for n ≥ 9)
- `folio-assistant/computations/binding_depth_stratified_lr.py` (LR combiner — for A ≥ 4 via per-nucleon H_3 → H_{3A})
- `folio-assistant/computations/binding_depth_stratified.py` (Python fallback)

Witness JSONs (all on `main`):
- [`binding-depth-stratified-rust.witness.json`](../../folio-assistant/computations/binding-depth-stratified-rust.witness.json) (6 atoms: D, T, ³He, ⁴He, ⁶Li, ⁷Li)
- [`binding-depth-stratified-lr.witness.json`](../../folio-assistant/computations/binding-depth-stratified-lr.witness.json)
- [`binding-depth-stratified.witness.json`](../../folio-assistant/computations/binding-depth-stratified.witness.json) (⁴He deferred)
- [`binding-depth-stratified-selfconj.witness.json`](../../folio-assistant/computations/binding-depth-stratified-selfconj.witness.json)
- [`binding-depth-stratified-knot-weighted.witness.json`](../../folio-assistant/computations/binding-depth-stratified-knot-weighted.witness.json)

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
[`binding_depth_stratified_rust.py:62-70`](../../folio-assistant/computations/binding_depth_stratified_rust.py)):

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

## Numerical state (per witnesses 2026-06-09)

| atom | depth-stratified B_pred | B_AME | ratio | gap |
|---|---:|---:|---:|---:|
| D (²H) | 0.607 MeV | 2.225 | 0.273 | **−73 %** |
| T (³H) | 2.808 MeV | 8.482 | 0.331 | **−67 %** |
| ³He | 2.653 MeV | 7.718 | 0.344 | **−66 %** |
| ⁴He (Rust) | 14.063 MeV | 28.296 | 0.497 | **−50 %** |
| ⁴He (LR) | 59.114 MeV | 28.296 | 2.089 | **+109 %** |

**The canonical depth-stratified compute does NOT close binding at the
10 % threshold.** D / T / ³He under-bind by ~67-73 %; ⁴He LR vs Rust
disagree by a factor 4× on the sign of the deviation — signalling the
per-depth α_k assignment rule is not yet substrate-derived (cf. cheat
sheet "open Barrier-1").

**Compare against the flat magic-A formula** `B(⁴He) = 2·m_e·A·Vol(L6a4)
= 2·m_e·4·8G = 29.96 MeV` (+5.87 %, no per-depth structure): the flat
formula BEATS the depth-stratified tower sum on ⁴He (50 % undershoot
Rust, 109 % overshoot LR). This says the tower sum is over-/under-
weighting depth bands rather than monotonically refining the magic-A
result. The unclosed structural gap is **not** at low depth (where the
magic-A flat result lives) but in the α_2 / α_3 / α_{k≥4} assignment
choices.

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
   field** when reporting binding numbers — this flags that α_k is
   empirical, not derived.
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
`2·m_e·A·8G` (+5.87 %) on ⁴He (-50 % Rust, +109 % LR). Four
structural reasons:

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

### (iii) Compute-path "instability" Rust vs LR — actually an artifact

| atom | LR n_atom | LR n_free | Rust n | LR/AME | Rust/AME |
|---|---:|---:|---:|---:|---:|
| D | 11 | 11 | 11 | 0.273 | **0.273** |
| T | 30 | 30 | 30 | 0.331 | **0.331** |
| ³He | 30 | 30 | 30 | 0.344 | **0.344** |
| ⁴He | **24** | 77 | 77 | 2.089 | 0.497 |

**LR ratio = Rust ratio EXACTLY for D, T, ³He** (to 3 dp). The 4×
⁴He LR vs Rust disagreement (2.089 vs 0.497) is **entirely an
artifact** of the partial cached ⁴He atom chi witness — 24 of 77
H_12 partitions only.

`binding_depth_stratified_lr.py:188-191` treats missing partitions
as 0 in Φ_atom:

```python
chi_atom_for_phi = {lam: chi_atom.get(lam, mp.mpf(0))
                     for lam in chi_free.keys()}
```

The 53 missing partitions push `Φ_atom` artificially low ⇒
`Φ_free − Φ_atom` over-counts ⇒ `B_LR` inflates from ~14 MeV
(true value matching Rust direct) to 59 MeV.

**LR is mathematically EXACT for the free config** in the
parabolic subalgebra H_3^A ⊂ H_{3A}:

$$\chi^\lambda(\beta_p\cdot\beta_n\cdots) = \sum_{\mu_1,\ldots,\mu_A\vdash 3} c^\lambda_{\mu_1\cdots\mu_A}\,\chi^{\mu_1}(\beta_p)\cdots$$

(Mathas (1999) §3 branching rule). LR is a compute optimization,
not a different formula. It does NOT "factorize interface crossings
away" — it only computes the FREE config (disjoint Hecke product);
the ATOM config chi comes from a cached H_{3A} witness produced by
the SAME `chi_q_atomic` Rust kernel as the Rust direct path, WITH
interface crossings included.

**Fix**: complete the ⁴He cached atom chi witness to 77/77 partitions
(via `compute_atom_chi_rust.py 4He`). Once done, LR will agree with
Rust within numerical precision; the 2.089 vs 0.497 spread collapses.

This means the only genuine compute-path question is "is Rust direct
H_{3A} canonical?" — yes, that's the default per the LR docstring
(line 21-26) and the witness consistency check above.

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

### (iii-bis) Per-depth Rust vs LR breakdown (⁴He)

| depth | α_k | Rust δΦ | LR δΦ | LR/Rust |
|---|---:|---:|---:|---:|
| 0 | 1 | 0 | 0 | — |
| 1 | 1 | 0.00128 | 0.00128 | **1.00 ←identical** |
| 2 | 0.249 | 0.357 | 0.599 | 1.68 |
| 3 | 1 | 2.28 | 7.42 | **3.25** |
| 4 | 3.74 | 2.54 | **9.65** | 3.80 |
| 5 | 3.74 | 0.43 | 3.39 | 7.96 |
| 6 | 3.74 | 0.15 | 0.68 | 4.45 |
| 7 | 3.74 | 0.0073 | 0.052 | 7.10 |
| 8 | 3.74 | 0.0004 | 0.0026 | 6.50 |
| **TOTAL** | — | **14.06** | **59.11** | **4.20** |

**Same α_k assignment.** Same Φ_k formula. The 4× total divergence
is entirely driven by **different χ values**:

- **Rust**: `compute_atom_chi_rust.py` runs `chi_q_atomic` Rust kernel
  directly on the full H_{3A} = H_{12} braid word — exact χ for each
  of the 77 partitions of 12 via Geck-Pfeiffer + Hoefsmit.
- **LR**: `binding_depth_stratified_lr.py` builds H_{12} characters
  from per-nucleon H_3 building blocks via Littlewood-Richardson
  tensor product:
  $\chi^\lambda_{\rm LR}(\beta_{\rm 4He}) = \sum_{\mu\nu\rho\sigma\vdash 3} c^\lambda_{\mu\nu\rho\sigma}\,\chi^\mu\chi^\nu\chi^\rho\chi^\sigma$
  using `prop:block-multiplicativity-v-free`. H_3 has only 3 partitions
  ({[3],[2,1],[1³]}), so all 77 H_12 χ are built from this tiny basis ×
  LR multiplicities.

**Why depth 1 agrees exactly**: at a single generator, no LR
multiplicity is invoked — both methods compute the same thing.

**Why depth ≥ 3 diverges 3-8×**: long partition shapes have many
LR decompositions into H_3 factors, and the LR sum
`Σ c^λ_{μνρσ}` over-counts compared to the exact Rust χ on the
H_{12} braid word.

**Why depth 4 dominates**: 68 % of Rust total / 61 % of LR total. LR
depth-4 contribution (36.13 MeV) alone EXCEEDS the AME 28.30 — the
inflation is concentrated exactly where α_k = m_e·8G is large.

**Physical interpretation:**
- **LR ≡ "⁴He as 4 independent nucleons + tensor multiplicities"** —
  assumes nucleon factorization (`prop:block-multiplicativity-v-free`);
  over-counts because tensor multiplicities double-count entangled
  channels.
- **Rust ≡ "⁴He as the H_{12} braid word with interface-knot crossings"**
  — honors interface structure that LR factorizes away; under-counts
  because chi-differences at high depth nearly cancel (atom and free
  share H_{12} structure).

**AME sits between**:

```
Rust 14.06 ←──── AME 28.30 ────→ LR 59.11
    (0.50×)        (1.00×)        (2.09×)
```

Geometric mean √(Rust · LR) = **28.83 MeV** (+1.9 % vs AME 28.30) — a
suggestive but unmotivated coincidence (no proposition predicts the
geometric mean). The TRUE ⁴He χ is neither fully factorized (LR) nor
fully captured by the canonical H_{12} braid word's chi-differences
(Rust). Resolving this is what the **operator-valued combiner**
(PR #1698 track) is meant to deliver — a per-bond magnitude carrier
that interpolates between LR's free tensor and Rust's fully-coupled
H_{3A}.

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
tuning ([`binding_ladder_catalog.py:63`](../../folio-assistant/computations/binding_ladder_catalog.py)
warning: α-ladder is fitted; per-isotope inconsistency was the
falsification of the fitted route).

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
- [`binding_factor_f_decomposition.py`](../../folio-assistant/computations/binding_factor_f_decomposition.py)
  — extracted f(Z, N) values + pairwise-bond model falsification
