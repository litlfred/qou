---
# qou-fq0f
title: 'Convention D is Wenzl level r=2 exactly: the row cap the closure block argues against'
status: in-progress
type: task
priority: normal
created_at: 2026-09-06T10:24:30Z
updated_at: 2026-09-06T10:39:23Z
---

## The measurement

The Wenzl level is fixed by the Markov parameter via `Q^r = z_W/(1 - Q + z_W)`,
`Q = q²`, `z_W = q·z` (`computations/markov/markov_weights_symbolic.py`). At the
proton pin:

| convention | z | Q^r | r |
|---|---:|---:|---:|
| C (excised 2026-08-09) | 0.499320334184 | 1.72025175121 | **2.59951553640** |
| **D (production)** | 0.612688037146 | 1.51795324982 | **2.00000000000** |

Under D, `Q^r = q⁴ = Q²` **exactly** — algebraically, not numerically:
`1 - q² + q⁴/(q²+1) = 1/(q²+1)`, so `Q^r = q⁴`. Convention D *is* the r = 2
locus. Under C the level was not an integer at all.

Wenzl's row cap (`s_{α,r} = 0` when `ℓ(α) > r`; Orellana, *Crelle* 508 (1999)
157–178, p. 5) therefore bites at **two rows** under production:

    H_3 :  y_(1,1,1) = 0                      1 of 3 partitions killed
    H_4 :  y_(2,1,1) = y_(1,1,1,1) = 0        2 of 5 partitions killed

Verified two independent ways that agree exactly: `y_lambda_symbolic` (Wenzl
principal specialisation) and the H₄ closed forms in
`h4_markov_weights_closed_form.py` substituted at `z = q³/(q²+1)`. Both give

    w_λ^D  =  s_λ(q, q⁻¹) / [2]_q⁴        (λ with ≤ 2 rows)
    w_λ^D  =  0                            (λ with ≥ 3 rows)

with `Σ_λ w_λ d_λ = 1` exactly. The vanishing is not a limit or a small
residual: the closed forms carry a literal factor `(A z − q³)`, `A = q²+1`, and
`z_D = q³/A` is its root.

## Why this is a finding and not a rediscovery

The *mathematics* is already correct and documented — `markov_weights_symbolic
.schur_principal_symbolic` states the r = 2 collapse in its own docstring, and
`WenzlWeightVanishing.lean` certifies the cap. Nothing computed is wrong.

What is wrong is a **content block that argues the opposite**, in prose the
C→D migration never touched.

`content/quantum-observable-universe/mass-endomorphism/q-hecke-seminormal-character-closure.md`,
"Two layers have to be got right", bullet 1:

> **Weight layer.** The two-variable Schur function s_λ(q, q⁻¹)/H_q(λ) vanishes
> for partitions with three or more rows and so cannot serve as the weight. The
> correct weight is y_λ(q), the Wenzl Schur principal specialisation.

Under production D, `y_λ(q)` **is** the two-variable specialisation and **does**
vanish for ≥ 3 rows. The property the bullet offers as disqualifying is a
property of the weight it endorses. The contrast was true in the C frame
(r ≈ 2.5995, no integral cap) and became vacuous at the migration.

Same block, the displayed formula sums `Σ_{λ ⊢ 3A}` over all partitions without
noting that under D only the ≤2-row λ contribute — for the five-atom table
that is 2 of 3 terms at H₃.

## Decision needed

1. **Rewrite the Weight-layer bullet** so it discriminates on something true
   under D. The real distinction is *normalisation*, not vanishing:
   `s_λ/H_q(λ)` divides by the hook polynomial, `y_λ` by
   `Z = Σ_μ s_μ f^μ`. Both vanish above two rows.
2. **State the row cap where the partition-sum is introduced**, so a reader is
   not left to infer that three of five H₄ blocks are absent.
3. **Owner question, derivation-side:** that D lands on an *integral* Wenzl
   level while C does not is an argument FOR D that has never been written
   down. r = 2 means the Markov trace factors through the two-row
   (Temperley–Lieb) quotient. Is that intended structure or an accepted
   consequence? It bears on the TL-kernel item already flagged as
   grouped-specific under `qou-hu1f`.

## Producer defect found alongside (fix landed with this bean)

`computations/h4_markov_weights_closed_form.py`:

- **:346** `cfc = closed_forms(sympify(canonical_q0), z0)` evaluated the
  **canonical proton-pin** weights with `z0 = XCHECK_Z`, the convention-**C**
  constant, and published them in the witness as
  `anchor.weights_at_canonical_q0` — a field whose surrounding note explains at
  length how carefully the *pin* was chosen while the *convention* input was
  stale. It printed `(2,1,1) = 0.0236` and `(1,1,1,1) = -0.00084` where D gives
  exactly 0.
- **:152** the comment claims "`XCHECK_Z` is transcribed, so a CONVENTION
  change breaks loudly". It did not break: C→D landed 2026-08-09 and this
  producer still exits 0, because *both* sides of that cross-check are frozen
  in C. The cross-check is a historical reproduction of a C-era artifact —
  correct as such, and C is the right constant for it — but it is not a
  tripwire on the live convention, and describing it as one is why the :346
  defect survived the migration.

Method note: a text sweep of the C signature returns 177 hits / 106 "live"
under a keyword classifier. The executable surface is **8 bindings in 7 files**
(AST, not grep), and of those, 6 are correct — named `z_c`, `zC`, `REG_ZC`, or
inside a probe whose subject is the C/D difference. The one real defect sits in
a file where the *same constant is right in one arm and wrong in the other*. A
sweep would have broken the good arm and missed the point of the bad one.


---

## The row cap is worth ~100x, and nobody was taking it

Recorded 2026-09-06, same pass. This is the consequence of r = 2 that matters
operationally, and it lands on `qou-sv7h` ("binding compute cannot scale").

`tr_M_via_wenzl_bridge_mpfr` sums `y_λ · χ_λ` over **every** partition of n. Under
D, `y_λ = 0` for `ℓ(λ) > 2`, so most of those terms are identically zero — but χ_λ
was built for all of them anyway, at full seminormal-matrix cost:

| | shapes | carry weight | Σ d_λ | max d_λ |
|---|---:|---:|---:|---:|
| H_9 (A=3) | 30 | 5 | 2620 → 126 (4.8 %) | 216 → 48 |
| H_12 (A=4) | 77 | 7 | 140152 → 924 (0.7 %) | 7700 → 297 |

**Measured, with bit-identical output** (`strip(before) == strip(after)` on the
five-atom witness, and `|Δ| = 0` on a direct tritium comparison):

    tritium   (H_9)   30.407 s -> 0.337 s     90.3x
    helium-3  (H_9)   35.003 s -> 0.305 s    114.6x
    deuteron  (H_6)    0.049 s -> 0.012 s      4.2x
    TOTAL             65.46 s  -> 0.66 s      99.5x

    helium-4  (H_12)  >1200 s TIMEOUT -> 19.37 s

The last line is the point: `atomic_tr_m_helium4.py` was one of the four
producers the `qou-hu1f` regeneration pass could not run at all. It is not a
scalability *problem* at A=4; it was 91 % waste.

### Why it wasn't already free

The skip is `y_lam == 0`, and the witness does not store zeros — it stores
**~1e-73 rounding residues**, because the path that produced them cancels
numerically rather than symbolically. 71 orders below the smallest live weight,
so harmless to the sum and invisible to every consumer, but enough to defeat an
exact-zero test. `y_lambda_at_q0_mpmath` (the live closed form) *does* return
exact zeros; the cached witness does not. So the optimisation was available in
one code path and not in the one production uses.

`_apply_wenzl_row_cap` now snaps them, having first **verified** they are
negligible (raises if any capped weight exceeds 1e-40 of the largest live one —
so if the mathematics ever moves this fails loudly instead of zeroing something
real). That applies a theorem; it does not threshold.

### A trap I walked into, worth recording

The first version of `_wenzl_level` recovered `q` from `z` by solving
`z = q³/(q²+1)` — which *assumes convention D* and is therefore circular. Fed
convention C's `z = 0.4993203342` it returned **r = 2**, precisely the answer the
function existed to be able to refuse. It would have capped rows under a
convention that caps nothing.

Caught by testing the guard against the case it must reject, not the case it
must accept. `q` is now read from the same witness table as `z`; C yields None,
a table with no `q` yields None, and the cap has to be earned.
