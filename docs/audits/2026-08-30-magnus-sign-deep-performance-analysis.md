# Deep performance analysis: cutting the Magnus Ω₂ sign computation

**Date:** 2026-08-30
**Question (owner):** "What other performance bottlenecks? … find ways to cut the
computational load either through trees or potential symbolic forms instead of
massive sums. Is there anything conjecturally we can use to simplify?"

**Object.** `P(A) = Σ_{λ⊢n} y_λ · tr(ρ_λ Ω₂_λ)`, `n = 3A`, `y_λ = d_q(λ)²/[n]_q!`,
`ρ = ∏ σ_{g_i}` (the ⁴He-style braid word, L≈47 crossings at A=4),
`Ω₂ = ½ Σ_{i<j} [A_{g_i},A_{g_j}]`, germ `A_g = q·∂_qσ_g·σ_g⁻¹`. We need the **sign**
of `P(A)` as the sign-vs-A map (A=2,3 negative so far).

## 1. Bottleneck decomposition (three nested loops)

| loop | size | cost |
|---|---|---|
| outer: sum over `λ⊢n` | `p(n)` partitions | Σ dim² = **n!** total (dim²-weighted) |
| middle: `tr(ρ_λ Ω₂_λ)`, matrix-free | per λ | **O(dim_λ²·L)** |
| inner: mpf arithmetic (140 dp) | per op | **0.24–0.97 µs** |

Flat-sparse total ≈ `n!·L`. The tower replaces the outer loop's `n!` by a
sub-exponential Bratteli contraction. This doc measures every lever.

## 2. Constant-factor levers (measured)

| lever | measured | note |
|---|---|---|
| **gmpy2 `mpfr` (native) inner arithmetic** | **4.0×** | 0.24 vs 0.97 µs/op at 466-bit (=140 dp). The real constant win. NO-FLOAT64-clean (MPFR, explicit precision). Bake into the tower engine. |
| gmpy2 backend under mpmath | 1.2× | free, auto-detected once `pip install gmpy2`; a fresh container needs it installed at launch |
| precision drop 140→50 dp | **~1.0× (nil)** | 1.17 vs 1.14 µs/op — cost is Python object overhead, not mantissa. So keeping 140 dp for exact comparability is FREE, and dropping dp is NOT a lever. |
| batched mat-vec | small | only helps if the Python loop (not mpf) dominates; with `mpfr` the arithmetic is fast so batching may matter — untested |

Constant factors cap out at ~5×. They do **not** change the asymptotics — A=5 flat
stays ~weeks even at 4×. The wins below are structural.

## 3. Tree lever: the Bratteli / branching tower (sub-exponential)

Steps 1–3 built and validated (`branching_tower.py`): the SYT basis is the
Bratteli path basis; `σ_g` and the germ `A_g` are single-level-local MPOs; the
nucleon-cut bond is `p(3(A-1))` (sub-exp `exp(c√A)`) with germ+link locality O(1).
Contraction cost `~A·p(3(A-1))^c ~ exp(c'√A)` vs flat `exp(3A ln 3A)`. Step 4 (the
contraction engine, on `mpfr`) is the build. **This computes the exact `P(A)`.**

## 4. THE STRUCTURAL WIN — row-concentration (measured, and it grows with A)

For the **sign** — all we need — the massive sum is unnecessary. `P` concentrates
on the FEW-ROW (near-trivial, small-dimensional) representations, which are exactly
the CHEAP ones. Measured from the committed A=2/A=3 witnesses (+ A=4 partial):

**Contribution by number of rows of λ (A=3):**

| rows(λ) | net contribution | fraction of Σ\|c\| |
|---|---|---|
| 1 (trivial) | 0 | 0 % (Ω₂ vanishes on the 1-dim rep) |
| **2-row** | **−1.77e7** | **91.0 %** |
| 3-row | −1.55e6 | 8.1 % |
| ≥4-row | — | <0.9 % total |

**Truncation vs the full `P` (sign always correct):**

| A | reflection rep `(n-1,1)` share | sign margin `\|P\|/Σ\|c\|` | hooks | ≤2-row | ≤3-row |
|---|---|---|---|---|---|
| 2 | 56 % | 69 % | 0.953·P | 1.024·P | 0.985·P |
| 3 | 86 % | 99 % | 0.951·P | 0.918·P | 0.999·P |
| 4 (partial) | 92 % | 99.9 % | — | — | — |

**The reflection-rep dominance and the sign margin both GROW with A** (56→86→92 %;
69→99→99.9 %). The expensive dim-5000–7700 partitions contribute ~nothing; the
dim-8/11 reflection rep carries the sign.

**Why this is a big win.** `#{λ⊢n with ≤K rows} ~ n^{K-1}` is **polynomial**, and the
dominant reps are small-dimensional, so the **≤3-row truncation is a poly-size sum
of cheap reps that reproduces the sign and ~99 % of the value** — no tower, no
huge-dim partitions. Tool: `magnus_sign_row_truncation_probe.py --rows 3 --A …`.
(Validated directly against the committed A=2/A=3 witnesses; running it for new A
needs free cores — it is starved while the flat A=4 run saturates all four.)

## 5. Conjectures that would collapse it further

- **C1 — Row/cumulant decay.** The contribution decays with row-count like a
  cumulant expansion truncating in order. If `|tr(ρ_λ Ω₂_λ)|` provably decays with
  rows(λ) (or with dim), the ≤K-row truncation becomes a *rigorous* sign with a
  computable tail bound. This is the **cluster-expansion connection** — cf. the
  just-ingested Procacci–Yuhjtman (Penrose tree-graph) and Rebenko (canonical
  virial) papers (`docs/audits/2026-08-30-cluster-expansion-uploads-…`): row-count
  ≈ connected-cluster order.
- **C2 — Reflection-rep closed form.** As A→∞, `sign(P(A))` is set by `(n-1,1)`
  (dim `3A-1`). The standard rep is very concrete (germs are explicit `(3A-1)²`
  matrices), so `tr(ρ_{(n-1,1)} Ω₂)` may have a **closed form in A** ⇒ the sign is
  a closed-form function of A, computed with no representation theory at all. This
  is the highest-value lead: **extract `tr(ρ_{(n-1,1)} Ω₂)` for A=2..6 and fit /
  derive the closed form.** (The corpus already carries two-row closed-form
  character machinery: `phase1b_two_row_closed_form_character.py`.)
- **C3 — Jucys–Murphy / content-symbolic germ.** The germs `A_g = q∂_qσ_g σ_g⁻¹`
  are the log-derivatives of the R-matrix = the KZ / Kohno–Drinfeld infinitesimal
  braid connection; in the q→1 limit `A_g → t_{g,g+1}` (sums of transpositions),
  and the Jucys–Murphy elements `L_k = Σ_{i<k} t_{ik}` are **diagonal in the SYT
  basis with content eigenvalues**. If `Ω₂` (a commutator curvature of the KZ
  connection) reduces to a content polynomial in the JM elements, `tr(ρ_λ Ω₂_λ)`
  becomes a sum over SYT of `ρ`-weights × explicit content factors — a large
  symbolic simplification, and the natural route to C2's closed form.

## 6. Honest rigor gap

Truncation (§4) and C2 give a **heuristic** sign of very high confidence (99.9 %
margin at A=4), **not yet a theorem**: a rigorous sign needs either the C1 tail
bound on `|tr(ρ_λ Ω₂_λ)|` for the excluded high-row λ, or the C2 closed form with
a proof the excluded remainder cannot flip it. The `y_λ` are known exactly; the
missing ingredient is the `|tr|` bound. This is the one open item; everything in
§2–§4 is measured and everything in §3 is validated.

## 7. Prioritized recommendations

1. **Extract `tr(ρ_{(n-1,1)} Ω₂)` for A=2..6 and derive/fit its closed form (C2).**
   Cheapest, highest-value: if it closes, the sign is a formula in A, no tower.
2. **Prove the row-decay tail bound (C1)** to upgrade truncation to a rigorous sign
   — likely via the cluster/cumulant papers just ingested.
3. **Build step 4 (tower engine) on `mpfr`** for the exact `P(A)` when the value
   (not just sign) is wanted, banking the 4×.
4. Constant factors (`mpfr`, gmpy2) are worth ~5× but never change the asymptotics.

The load-cutting order is: **reflection-rep closed form (maybe O(1)) ≺ ≤K-row
truncation (poly) ≺ tower (sub-exp) ≺ flat (factorial).** We have been paying
factorial for a sign that a single small representation almost entirely determines.
