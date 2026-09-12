# The UIC per-block log: it IS outside the additive class, and it still has no valley

**Date:** 2026-09-12 · **Branch:** `claude/uic-per-block-log-valley-scan-2026-09-12` · **PR:** #7230
**Bean:** `qou-zlra` (this) · `qou-brng` (class D — **stays open**) · `qou-oooq`, `qou-eqwg` (origins)
**Continues:** #7223 / [`2026-09-12-graded-binding-sign-convention.md`](2026-09-12-graded-binding-sign-convention.md) §5 item 3
**Lean:** `QOU/Mass/UICPerBlockLogPairTerm.lean` (generic, 7 declarations) +
`QOU/Mass/UICPerBlockLogSymmetryCurvature.lean` (archimedean, 2) — both sorry-free.
Split per §7c: the curvature statement is about `Real.log` and an ordering and cannot be
generic, so it lives in its own file consuming the generic one.
**Probe:** `computations/probes/uic_per_block_log_valley_scan_probe.py`

---

## 0. The claim, flatly

#7223 proved that **no product-additive functional** — `log`, `−log`, `α·log`, any sign,
any scale — carries the Vassiliev type-two pair convolution `Σ_{i<j} bᵢbⱼ`. That closed
the `+c_k / −c_k` question for the live binding law, a logarithm of the **total** trace,
and left one thing unmeasured: `hecke_core_legacy.unified_iterative_correction(Z, N)`,
whose per-block log is the only corpus functional outside that class. The #7223 agent
measured that the production call exceeded **300 s** at `(Z,N) = (2,2)` and recorded the
scan as undone rather than guess.

**Answer, in two halves that must not be collapsed into one.**

1. **The door really is open.** The UIC per-block log is genuinely outside the additive
   class: its third difference in `Z` is nonzero in **every** one of the 36 `(k_exact, A)`
   cells scanned, **gated and ungated alike**, so the non-additivity is the functional and
   **not** the Pass-2 gate. The mechanism is exact and now proved: a two-branch block
   trace has a non-multiplicativity defect `wP·wM·(x−y)²`, which under convention D's
   normalisation is exactly `wP(q)` — **independent of both bond offsets**.
2. **Nothing comes through the door.** There is still no valley of stability. The maximum
   in `Z` **does not track** `N = Z` — it coincides with it in only 3 of 36 cells and never
   at more than one truncation order per `A` (§5.2; it is *not* true that it never lands
   there, and that weaker claim is the correct one) — it sits at an endpoint in 15 of 36,
   and it has not converged in `k_exact`. The one structurally *forced* fact points the
   wrong way: the all-pairs symmetry curvature
   `L_pp + L_nn − 2·L_pn = +0.04351846501566097275` is **positive**, so the additive part
   makes the symmetric nucleus the **least** bound. That sign is forced for every `q > 1`.
   Before any of that, the functional gets the **sign of the binding itself** wrong and its
   `A`-scaling wrong (§5.3).

So the last order-zero room in class D of `qou-brng` is measured, and it is empty — but it
is empty for a different reason than the additive class, and the distinction is the
result. The additive class cannot carry a pair term *at all* (theorem). The UIC per-block
log **can** and **does**; what it carries is the wrong shape and the wrong sign.

---

## 1. The functional as the corpus actually defines it

### 1.1 The producer — what actually runs

`computations/hecke_core_legacy.py`, verified at this branch's base `origin/main` `a526f20b75d`:

| line | what it fixes |
|---|---|
| 1693 | `unified_iterative_correction(Z, N, return_per_step=False, k_max=K_PARTITION_MAX, k_exact=K_PARTITION_MAX)` — wrapper; runs the body inside `mp.workdps(COMPUTE_DPS)` |
| 1719 | `_unified_iterative_correction_exact` — the body |
| 1823-1829 | the ground-state **ordering**: alternate `p`/`n`, then fill with whichever remains |
| 1622-1630 | `_step_chain_generic`: 12 intra-nucleon crossings, then **one inter-nucleon crossing for every previous nucleon** — so the word is the **all-pairs / complete-graph** layout |
| 1908 | `L0 = _exact_log(dim)` — the `− ln d_λ` of the telescoped form |
| 1915 | `scale = e['C_lambda_resolvent_MeV']` — the weight actually used |
| 548, 564 | `C_lambda_resolvent_MeV = H_q(λ) · y_λ · ρ_λ(s_*) · m_e` |
| 538 | `y_λ = lp_shadow_price(λ) = w_λ/d_λ − 1/[k]_q!` |
| 544, 521 | `ρ_λ(s_*) = 1/(μ_λ + s_*)`, `s_* = (q₀−1)/q₀ = ℏ_q` |
| 2078-2085 | `log_cur = log_norm + _exact_log(|tr_run|)`; `raw_delta = scale · (log_cur − log_prev)` |
| 2186-2194 | **Pass 2**: `if s['final_tr_sign'] <= 0: gated_total += s['cumul_partition']` |
| 2204 | `return float(gated_total)` — the float64 cast at the public boundary |

So what runs is

```
B(Z,N) = Σ_{λ : tr M_λ(atom) ≤ 0}   m_e · H_q(λ) · y_λ · ρ_λ(ℏ_q) · ( ln|tr M_λ^{(0..A)}| − ln d_λ )
```

### 1.2 Which pieces depend on the bond content — the question the bean asked

**None of the weights do.** `H_q(λ)`, `y_λ`, `ρ_λ`, `d_λ` and the product `C_λ` are all
built by `_partition_table()` (line 523), which loops over partitions only and never
mentions `Z` or `N`. Measured rather than read off (S0.1): the five fields
`q_hook`, `shadow_price`, `dim`, `resolvent_weight_planck`, `C_lambda_resolvent_MeV` are
**byte-identical** across two different atoms. So `u_λ` is **per-partition and fixed**, not
per-atom.

The only `(Z,N)`-dependence in the whole functional is

* `ln|tr M_λ(atom)|` — the per-block log, and
* **which λ survive Pass 2** — a discrete selector.

This is worth stating because Pass 2's own comment (line 2181) says *"This is the per-atom
LP dual: each atom's braid Φ(Z,N) has a different set of tight partitions, so the
correction is atom-specific."* That is accurate about the **gate** and would be wrong about
`y_λ`, which is the same number for every atom in the corpus.

### 1.3 Producer vs content block — three divergences, reported not resolved

The content block
[`unified-iterative-correction.md`](../../content/quantum-observable-universe/mass-theory/unified-iterative-correction.md)
states

> `B_λ(Z,N) = m_e · H_q(λ) · u_λ · ( ln|tr M_λ^{(0..A)}| − ln d_λ )`,
> *"the per-partition binding corresponds directly to its Frobenius positivity LP shadow
> price `u_λ`"*, and *"The total unified correction sums these strictly over all λ."*

Against the producer that is wrong in three separate ways, and the producer is the one
that runs:

| # | content block | producer | size of the difference |
|---|---|---|---|
| 1 | `u_λ` is *"its Frobenius positivity LP shadow price"* | `lp_shadow_price`'s own docstring: *"NAMED for the LP shadow price; it is not one … This function solves no program. It evaluates a closed form."* — corrected 2026-09-05 by owner ruling, PR #6752 | a naming/epistemic claim, already settled against the block |
| 2 | weight is `m_e · H_q(λ) · u_λ` | weight is `m_e · H_q(λ) · y_λ · **ρ_λ(ℏ_q)**` — a q-Laplacian resolvent damping the block does not mention at all | `ρ_λ = 1/(μ_λ + ℏ_q)` with `μ_λ ∈ [2, 190]`, i.e. a per-partition factor spanning ~100× |
| 3 | *"sums these **strictly over all λ**"* | sums only over λ with `tr M_λ(atom) ≤ 0` | the producer's own measured note (line 2158): ungated `−0.4122` vs returned `−0.0896` at `A=2`; **3.4–4.6×**, not a rounding difference |

Divergence 3 is the serious one: read literally, the content block describes a
**different functional** from the one that runs — one with no gate. This audit scans the
producer, because the producer is what produces. **Not resolved here**: which of the two
is meant to be canonical is an owner call, and picking one would be choosing a functional.
Recorded as a finding and as a caveat on the witness.

---

## 2. Profiling: why it was 300 s, and what was done about it

`_HAS_LP_KERNEL = True` here (`pyhecke_native` 0.9.0 present), so the Rust MPFR kernel
path is live. The cost is **not** the partition table:

```
import hecke_core_legacy                    0.3 s
_PARTITION_TABLE materialised               8.9 s   (682 entries, 193 with YSN, max dim 2310)
```

and the table is cached process-wide, so it is paid once for a whole scan. The cost is the
per-call MPFR dense products, and it is governed entirely by `k_exact`:

| `k_exact` | partitions | Σ dim² at that level | UIC(1,1) | A=6 |
|---|---|---|---|---|
| 4 | 10 | 24 | 0.00 s | — |
| 5 | 17 | 120 | 0.01 s | — |
| 6 | 28 | 720 | 0.01 s | 0.04 s |
| 7 | 43 | 5,040 | 0.05 s | — |
| 8 | 65 | 40,320 | 0.30 s | 1.2 s |
| 9 | 95 | 362,880 | — | 11.2 s |
| 10 | 137 | 3,628,800 | — | ~110 s (extrapolated) |
| **11 (the default)** | 193 | 39,916,800 | — | **~1100 s (extrapolated)** |

**~10× per level, tracking `Σ dim²`.** That is the whole explanation of the 300 s wall:
at the producer's default `k_exact = 11` a single `A = 4` atom is of order 10³ s, so
#7223's `(2,2)` timeout at 300 s is exactly what this cost model predicts. It was never a
defect.

**What was made faster, without changing any number:**

1. **The table build amortises.** One process, one 8.9 s build, 39 cells — instead of a
   cold process per cell. Changes nothing computed.
2. **The float64 boundary cast is avoided.** `unified_iterative_correction` returns
   `float(gated_total)` (line 2204), but with `return_per_step=True` the *same* `gated_total`
   is available as an **`mpf`** at `per_step[-1]['gated_total_MeV']`, and the ungated total
   at `['raw_total_MeV']`. The probe reads those. Verified (S0.3) that `float()` of the mpf
   equals the producer's own float return exactly — i.e. this is strictly more precision on
   the same quantity, not a different quantity.

**What could not be made faster**, and why option (b) of the task was taken: each `(Z,N)`
has a different word — the ordering depends on `Z`, and `_step_chain_generic` cycles the
generator index `g % n_gens` with position — so there is no per-partition trajectory to
memoise across cells. The cost is irreducibly 50-dps MPFR products over YSN blocks up to
dimension 2310.

**So the scan is run at stated truncations.** `k_exact` is a first-class, documented
parameter of the producer (its own docstring, lines 1775-1789), and prior corpus work uses
it both ways — `2026-09-05-uic-sign-forced-by-gate.md` runs `k_max = 6`, #6427 runs 11.
The scan sweeps `k_exact = 4..9` over the whole grid and reports the verdict **at every
tier**, so that its stability is visible rather than assumed. Nothing cheaper is
substituted for the production functional: every cell is a real
`unified_iterative_correction` call.

**Not done, and stated as such:** `k_exact = 10` and the default `11` over the grid
(~12 h at `k = 11`). The `Δ³ ≠ 0` finding is unanimous across all six tiers run; the
argmax instability is *itself* one of the findings, so a seventh tier could move the
argmax again but could not make it retroactively stable.

---

## 3. The discriminator: why the THIRD difference, not the second

`_step_chain_generic` crosses each nucleon with **every** previous one, so the UIC's bond
census is the complete graph:

```
n_pp = C(Z,2),      n_pn = Z·(A−Z),      n_nn = C(A−Z,2).
```

`n_pn = Z(A−Z)` is already quadratic in `Z`. So **an additive functional on this layout is
already exactly quadratic**, with

```
Δ²_Z = f_pp + f_nn − 2·f_pn   (a nonzero constant),        Δ³_Z = 0.
```

Proved sorry-free as `census_secondDiff` / `census_thirdDiff`. **Therefore a nonzero second
difference on the UIC layout is not evidence of a two-bond correlation — the layout
supplies it.** The clean separator is the third difference, which vanishes identically for
every census-affine functional (`not_censusAffine_of_thirdDiff_ne_zero`).

This sharpens #7223 §S4c's own caveat — *"on the UIC's own all-pairs layout the counts are
already quadratic, so that layout does not isolate the functional"* — into a usable test.

### The chain baseline, and a boundary fact worth recording

On the **grouped** chain (`ppp…nnn`, the #7223 layout) the census is `(Z−1)` pp, one pn,
`(N−1)` nn, and the additive functional has `Δ²_Z = 0` at every **interior** centre
`2 ≤ Z ≤ A−2`, exactly as #7223 reports. It is **not** identically zero: there are exactly
two endpoint kinks, at

```
Z = 1    : Δ² = L_pp − L_pn = −0.186922208131
Z = A−1  : Δ² = L_nn − L_pn = +0.230440673147
```

for every `A = 3..8`. These are pure-species boundary effects — at `Z = 0` and `Z = A` the
single `pn` interface disappears — not a pair term. Recorded because an assertion of
"identically zero" fails on them, and the failure looks like a contradiction of #7223 when
it is not.

Separately: the **producer's** alternating ordering makes even a chain-additive functional
non-linear in `Z` (S4.1c). The all-pairs *census* is order-blind, so that does not affect
§3's argument — but the *word* is not order-blind, because the generator index cycles with
position. **This audit does not separate the per-block log's contribution to `Δ³` from the
generator-map's.** Both are non-census effects; which dominates is unmeasured.

---

## 4. The mechanism, exact

For a two-branch block — two crossing eigenvalues `x`, `y` on one generator, branch weights
`wP + wM = 1` — write the one- and two-crossing traces with bond offsets `d`:

```
T(d)       = wP(x+d)        + wM(y+d)
T₂(d₁,d₂)  = wP(x+d₁)(x+d₂) + wM(y+d₁)(y+d₂)
```

Then, sorry-free (`twoCrossing_defect`):

```
T₂(d₁,d₂) − T(d₁)·T(d₂) = wP · wM · (x − y)²
```

**and the right-hand side mentions neither offset.** Under convention D at `x = q`,
`y = −q⁻¹` we have `(x−y)² = (q + q⁻¹)² = q² + 2 + q⁻² = [3]_q + 1 = 1/wM`, so the defect
is exactly the plus-branch weight (`twoCrossing_defect_eq_wPlus`):

```
T₂(d₁,d₂) − T(d₁)·T(d₂) = wP(q) = 0.7527021132519654015937794     at q₀
```

Verified numerically to `2.08e-70` at `mp.dps = 70` over **25 offset pairs**, including two
arbitrary rationals `7/3` and `−11/5` chosen precisely to show the offset-independence is
not a coincidence of the three physical letters (S2.1).

That nonzero defect **is** the failure of `log tr_λ` to be additive over bonds — the reason
#7223's `additive_census` does not reach this functional. `twoCrossing_mul_iff` makes it an
iff: the block trace is multiplicative exactly when `wP = 0`, i.e. when one branch is dead.

For `n` crossings the same structure gives an exact factorisation through a **single
multiplicative statistic** (S3.1, four words):

```
tr_n = wP·P₊·( 1 + (wM/wP)·R ),      R = ∏ᵢ rᵢ,      rᵢ = (y + dᵢ)/(x + dᵢ)
```

so `log|tr_n|` is an additive part plus `log|1 + (wM/wP)·R|` — a **nonlinear function of an
additive statistic**. That is precisely how a per-block log leaves the additive class while
still being built from per-bond data, and why its `Z`-dependence is not polynomial.

**Scope.** This is proved for a *two-branch* block (`ChainTraceFactor.twoStrandTrace`). The
UIC's general `λ`-block spreads crossings over several generators via the cyclic map, where
the matrices do not commute and the two-branch form does not apply. §4 is the **mechanism**
by which a per-block log can escape additivity, **not** a closed form for the production
accumulator.

---

## 5. The measurement

36 cells: `A = 3..8` × `k_exact = 4..9`, every `Z` in `0..A`. Every cell is a real
`unified_iterative_correction` call. `gated` is the function's return value (Pass 2
applied); `ungated` is the same weighted sum over the **fixed** active set, which is what
isolates the functional from the selector.

### 5.1 The two functionals side by side

| functional | layout | `Δ²_Z` | `Δ³_Z` | valley? |
|---|---|---|---|---|
| **total-trace log** — the live law `E₀·log(tr_free/tr_atom)`, additive over bonds | grouped chain | **0** at every interior centre `2 ≤ Z ≤ A−2`; two endpoint kinks (§3) | 0 | no — cannot, by `additive_census` (#7223) |
| census-affine reference on the UIC's own layout | all pairs | `L_pp + L_nn − 2L_pn = +0.04351846501566097275` (constant) | **0** | no — convex, `N=Z` is the **minimum** |
| **UIC per-block log, ungated** | all pairs | nonzero, varies with `Z` | **nonzero in all 36 cells** | no — argmax does not track `N = Z` (§5.2) |
| **UIC per-block log, gated** (the production return) | all pairs | nonzero, varies with `Z` | **nonzero in all 36 cells** | no — and argmax not converged in `k_exact` |

**`Δ³_Z ≠ 0` in every cell, gated and ungated alike.** By `census_thirdDiff` that is exactly
the statement that the UIC per-block log is **not** an affine function of the bond census.
It is the first functional in the corpus of which that is true.

**And the ungated column is the decisive one.** Had `Δ³` been nonzero only after Pass 2,
the Z-structure would have been the discrete selector — an artefact of which partitions
happen to be tight — and not a correlation in the functional. It is nonzero *before* the
gate, at comparable magnitude (typically 0.3–1.4 against the gated 0.3–2.4), so the
non-additivity is the **per-block log itself**.

### 5.2 `argmax_Z` — where the maximum sits

`A//2` is where `N = Z` (the valley of stability, if there were one).

| `A` | `N=Z` at | gated argmax across `k_exact = 4,5,6,7,8,9` | ungated argmax |
|---|---|---|---|
| 3 | 1 | 0, **1**, 2, 2, 3, 3 | 3, 2, 2, 0, 0, 0 |
| 4 | 2 | 1, **2**, 4, 4, 4, 4 | 0, 4, 1, 1, 2, 2 |
| 5 | 2 | 5, 1, 5, 5, 5, 4 | 5, 4, 1, 1, 1, 4 |
| 6 | 3 | 2, 4, 4, 4, 4, **3** | 4, 1, 2, 2, 2, 2 |
| 7 | 3 | 1, 5, 1, 1, 7, 7 | 0, 0, 1, 2, 0, 0 |
| 8 | 4 | 2, 2, 0, 1, 1, 0 | 3, 2, 2, 2, 2, 2 |

Three statements, and they are different claims. **The first is deliberately weaker than
"it never lands on `N = Z`", which would be false.**

1. **It coincides with `N = Z` in 3 of the 36 cells, and never at more than one tier per
   `A`** — bolded above: `A = 3` at `k = 5`, `A = 4` at `k = 5`, `A = 6` at `k = 9`. Three
   hits out of 36, on an argmax wandering over `A+1 ∈ {4…9}` values, is what chance looks
   like; and a valley of stability is a *stable* feature of a nucleus, not a coincidence at
   one truncation order. At `A = 5, 7, 8` it never coincides at any tier. So the honest
   statement is that the argmax **does not track** `N = Z` — not that it never touches it.
2. **It is at an endpoint (`Z = 0` or `Z = A`) in 15 of 36 cells**, and the endpoint it
   reaches is usually `Z = A` — pure proton matter. That is §3's positive curvature seen
   directly: `L_pp` is the smallest of the three letters, so the maximally asymmetric
   configuration is the least penalised. It is the anti-valley, not a valley.
3. **It is not converged in the truncation order.** The gated argmax moves between adjacent
   tiers at every `A`. This is a statement about convergence, not noise: each `k_exact` is
   a *different*, larger partition set, so the sequence is a truncation sequence and it has
   not settled by `k = 9`. Given the ~10× cost per level (§2) the value at the producer's
   default `k = 11` is not predictable from below — which is the honest answer to "what
   does the production functional say about `Z`", and is why the verdict rests on `Δ³` and
   on the forced curvature rather than on any argmax.

The gated-set size `n_tight` varies with `Z` in most cells (e.g. `k=9, A=6`:
`[51, 53, 50, 48, 47, 50, 47]`), confirming Pass 2 is a live discrete selector — but, per
§5.1, not the source of the non-additivity.

### 5.3 Magnitude against AME — the honest accuracy statement

AME enters nowhere in the derivation. Post hoc, at `k_exact = 9`:

| atom | `Z` | `N` | `B_UIC` (MeV) | `B_AME` (MeV) | sign | `\|B_UIC/B_AME\|` |
|---|---|---|---|---|---|---|
| ²H | 1 | 1 | `−4.8136504934` | `2.2245662` | **wrong** | 2.164 |
| ³H | 1 | 2 | `−4.43040370717` | `8.4817962` | **wrong** | 0.522 |
| ³He | 2 | 1 | `−3.82527863882` | `7.7180413` | **wrong** | 0.496 |
| ⁴He | 2 | 2 | `−3.71158153356` | `28.295662` | **wrong** | 0.131 |

Two failures, and they are separate:

* **Wrong sign, every atom.** Not a near miss — the functional returns *negative* binding
  throughout. This reproduces
  [`2026-09-05-uic-sign-forced-by-gate.md`](2026-09-05-uic-sign-forced-by-gate.md), which
  traces it to Pass 2: `C_λ ≥ 0` for every partition by construction, the gate keeps
  exactly the partitions with `tr ≤ 0`, and a trace `≤ 0` almost never has `|tr| ≥ d`, so
  every surviving term is a non-negative scale times a negative log. Nothing here reopens
  that; it is noted so no reader takes an argmax over negative numbers for a binding
  prediction.
* **Not extensive.** `|B_UIC|` *falls* across these four — 4.81 → 4.43 → 3.83 → 3.71 —
  while AME rises 2.22 → 28.30, a factor of **12.7**. The ratio column therefore collapses
  by 16.5× across `A = 2..4` alone. This is the A-flatness #6427 measured (⁴He vs ⁶Li ratio
  0.9504 against a `C(A,2)` growth of 2.5×) seen on four atoms.

So the functional that *does* carry a two-bond correlation gets the sign wrong and the
`A`-scaling wrong before the `Z`-shape is even reached. That is the context in which §5.2's
"no valley" should be read: there is no regime here in which the `Z`-dependence is the
binding constraint.

---

## 6. Scope, per the (a)/(b) rule

**(b) structural — proved, with the invariant named.**

1. *No affine function of the all-pairs bond census has a nonzero third difference in `Z`.*
   Invariant: `census_thirdDiff` (sorry-free, any commutative ring). This is what licenses
   the discriminator; without it a nonzero `Δ²` would have been mistaken for a pair term.
2. *A two-branch block trace is multiplicative over two bonds if and only if one branch is
   dead; otherwise the defect is `wP·wM·(x−y)²`, independent of both bond offsets.*
   Invariant: `twoCrossing_defect`, `twoCrossing_mul_iff` (sorry-free). This is the
   mechanism by which a per-block log leaves the additive class of #7223.
3. *The all-pairs symmetry curvature of the additive letters is strictly positive.*
   Invariant: `symmetryCurvature_pos` / `allPairs_additive_secondDiff_pos` (sorry-free),
   given `b_pn ≥ (b_pp+b_nn)/2` — which convention D forces via
   `ChainTraceFactor.deltaPN_nonneg` — and `b_pp ≠ b_nn`. So the additive part of the UIC
   makes the symmetric nucleus a strict **minimum** of the binding, for **every** `q > 1`.
   This is an exclusion of the *ingredient*: no choice of `q` rescues it.

**(a) scope-limited — measured, constrains these constructions over this grid, not
ingredients.**

4. *The production UIC accumulator has `Δ³_Z ≠ 0` in all 36 cells, gated and ungated.*
   `A = 3..8`, `k_exact = 4..9`, proton pin, convention D. This establishes non-additivity;
   it says nothing about the *shape* of the correlation, and it does not extend to
   `k_exact = 10, 11`, which were not run.
5. *No valley: `argmax_Z` does not track `N = Z` — 3 coincidences in 36 cells, never more
   than one tier per `A`, endpoint in 15 of 36 — and is not converged in `k_exact`.*
   Same grid. A seventh tier could move the argmax again; it could not make the sequence
   retroactively convergent, and claim 3 is independent of the tier.

**Explicitly NOT claimed.** That the UIC *cannot* carry a valley. It carries a genuine
higher correlation (claims 2 and 4), and this audit measures that the correlation it
carries does not produce one on this grid. Whether the full `k_exact = 11` accumulator
does is unmeasured. What *is* structural is claim 3 — the forced sign of the additive
part — which is a reason to expect not, and is an ingredient-level exclusion rather than a
magnitude result.

**Two sources of `Δ³` are not separated.** The per-block log's non-multiplicativity
(§4) and the generator-index cycling in `_step_chain_generic`, which makes the *word*
order-dependent even though the all-pairs *census* is order-blind. Both are non-census
effects; which dominates is unmeasured.

---

## 7. What this means for the valley question, and for class D of `qou-brng`

The standing verdict has been *"no sum-over-bonds model has a valley for any `q`"*, and
#7223 sharpened it to *"the functional the corpus chose for extensivity is, by the same
theorem, the functional that cannot carry a pair term."* Row D of `qou-brng`'s escape
enumeration asked whether anything outside that class could. This audit answers it:

**The escape exists and is real — and it is empty.**

* Something in the corpus *is* outside the additive class, and it is not a technicality:
  the per-block log carries an exact, closed-form, offset-independent non-multiplicativity
  defect (§4). The #7223 theorem genuinely does not reach it.
* What comes through is not a valley. The forced component has the anti-valley sign for
  every `q > 1`, and the measured argmax does not track `N = Z`.

So the two negatives have **different characters and should not be quoted as one.** The
additive class cannot carry a pair term — a theorem. The UIC per-block log can and does —
and what it carries is the wrong shape and the wrong sign, measured. Only the second
leaves any room at all, and the room it leaves is `k_exact = 10, 11`.

**One cross-link a future agent should not have to rediscover.** The UIC word is the
**complete graph**, and `QOU.Mass.CoordinationSaturation.complete_graph_no_saturation`
(sorry-free, on `main`) already refutes complete-graph coordination on saturation grounds:
`B/A = ε·(A−1)/2` is unbounded, so it has no plateau. A valley found on this layout would
therefore have sat on a layout the corpus has already excluded for a different reason. That
does not weaken the present result; it means the remaining room is smaller than the
`k_exact` gap alone suggests.

`qou-brng` **stays open** (rule 13a): the extensive term's coefficient and mechanism are
untouched by anything here.

---

## 8. Verification

* **Lean.** `lean -DautoImplicit=false -s 65536` against the Mathlib oleans, **exit 0** on
  both files. The generic file is compiled with `-o` into a scratch shadow directory which
  is then prepended to `LEAN_PATH` for the archimedean sibling that imports it — no `lake`
  is invoked, so the restored olean cache is not evicted. Nine `#print axioms`:
  `twoCrossing_defect`, `twoCrossing_defect_offset_independent`,
  `twoCrossing_defect_eq_wPlus`, `twoCrossing_mul_iff`, `census_secondDiff`,
  `census_thirdDiff`, `not_censusAffine_of_thirdDiff_ne_zero` in the generic file, and
  `symmetryCurvature_pos`, `allPairs_additive_secondDiff_pos` in the archimedean one — all
  on `propext` / `Classical.choice` / `Quot.sound` only. **No `sorryAx`.**
* **Probe.** `computations/probes/uic_per_block_log_valley_scan_probe.py`, run with
  `python3 -u … 2>&1 | tee` per the long-compute logging discipline; witness
  `uic-per-block-log-valley-scan-probe.witness.json`.
* **Gates.** `scripts/precision-gates.sh --changed` exits 1 **tree-wide**, which is the
  pre-existing state of `main` (bean `qou-v0t8`) and not this branch. The branch-scoped
  fact is what is reported: **no file of this branch appears in any offender list** — a grep
  for `uic_per_block` / `UICPerBlockLog` across the whole gate log returns only the
  branch-name banner line — and both raw-float64 ratchets show `NEW dirty: 0`,
  `REGRESSED: 0`. The ten tree-measuring audit witnesses the runner rewrites were reverted
  with `git checkout -- computations/` before committing, per the runner's own instruction.
* **Sidecars.** `scripts/check-sidecars.sh` flagged the Lean file as **§7c MIXED generic +
  archimedean**, which was correct; the file was split rather than the flag argued with,
  and the checker now reports `no ℝ, generic OK` for the first and `ℝ justified` for the
  second. Its one remaining ⚠ is the canonical-mass status guard on
  `docs/precision-goals.md:82` — not a file of this branch.
* **Two assertions failed on the first run and were root-caused, not loosened.** S0.3
  compared different `k_exact` tiers (probe bug). S4.1 asserted the grouped chain's `Δ²_Z`
  is identically zero; it is zero only in the **interior**, with two endpoint kinks, and
  the assertion was replaced by the exact statement of both (§3).
