---
# qou-fq0f
title: 'Convention D is Wenzl level r=2 exactly: the row cap the closure block argues against'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-06T10:24:30Z
updated_at: 2026-11-16T19:27:00Z
parent: qou-rtxm
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

`folio/quantum-observable-universe/mass-endomorphism/q-hecke-seminormal-character-closure.md`,
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

---

## The 2026-06-10 no-truncation directive is satisfied — it searched the wrong factor

`docs/audits/2026-06-10-binding-active-set-compute-optimization.md` carries an
owner directive that has blocked partition-count reduction since June:

> **NO truncation — only provable exact-0.** … the precision discipline admits
> dropping a partition **only if `χ^λ(β_atom) = 0` is provable**. The exact-0
> search came back **empty**: `exact-χ-zeros = 0` … **Therefore no partitions
> are droppable.**

The search is correct and reproduces today — at tritium all **30 of 30**
partitions have `χ^λ ≠ 0`. But the summand is `y_λ · χ^λ`, and under D the
**weight** vanishes, not the character:

| tritium, n = 9 | count |
|---|---:|
| `χ^λ ≠ 0` — the audit's search | **30 of 30** |
| `y_λ · χ^λ` **exactly** 0 — the droppable set | **25 of 30** |

Not a tail: `χ_(4,3,2) = 2.384` is the **largest** character at n = 9, with
weight exactly 0.

So the carve-out the directive itself names is met, and the row cap is *more*
precise than the active-set truncation that was rejected — it drops only
provable zeros and keeps every nonzero term, including `[5,4]` (−0.00527) that
a "≲ 1 % each" reading would have dropped. The document's "legitimate
truncation path (formalize-first): prove a bound `|y_λ χ^λ| ≤ C·q₀^{−c·rows}`"
is moot; no bound is needed for an exact zero.

**The audit could not have seen this.** It is dated 2026-06-10; C → D landed
2026-08-09. Under C the level was r ≈ 2.5995, not an integer, no row cap, and
the ≥3-row tail really was nonzero at ~10⁻³–10⁻⁹ as measured there. Sound
reasoning in the frame it was written in. Audit updated in place with this
correction rather than a new document.

## Where the cap is still not taken

`tr_m_atom_via_transfer.tr_m_atom_zn` (the path `binding_canonical` actually
runs — its witness records `use_transfer: True`, so it does **not** use
`markov_trace_canonical.tr_M_element` which it imports):

    He-4 (n=12)   0.93 s   evaluating  77 partitions,  7 carry weight
    Li-6 (n=18)  12.46 s   evaluating 385 partitions, 10 carry weight

Its own comment says "ALL partitions kept, the speed is from the transfer
sweep, NOT from dropping partitions" and cites the audit above — which is now
the corrected one.

**Not done here, deliberately.** None of `chi_all_lambda_reduced_block`,
`chi_all_lambda_window` or `chi_all_lambda_general` accepts a partition
restriction, so taking the cap means threading a `shapes` parameter through
three kernels plus the dispatcher. The marginal value is also lower than it
first looks: a sibling's **window transfer** (`qou-wdij`) already removed the
`d_λ` wall that made this urgent — 963× at ⁴He (kernel 401.41 s → 0.42 s), with
⁶Li/⁷Li reachable. Worth doing, not worth rushing.


## 🟧 OWNER RULING 2026-09-07 — D7 = option 1, CHANNEL-SCOPED

Convention **D governs the decay / `Q_β` channel**; the **full tower governs
mass and binding**. This bean's Wenzl-level route (`Q^r = q⁴ ⇒ r = 2`,
Orellana's row cap) is what establishes that D *is* the two-row truncation, and
so is what makes the boundary computable: D retains **83.3333 %** of the algebra
at `n = 3` (the `Q_β` ladder's `H₃`) and **0.0434 %** at `n = 12` (⁴He). That
`n`-dependence is why the ruling is channel-scoped rather than global.

Full ruling: `docs/coordination/2026-09-05-owner-gated-bean-triage.md` §D7.

## 2026-09-08: canonical ledger for the convention-C excision family is qou-wgta (the P0 excision tracker; owner-ruling milestone qou-cdx1, S2 science blocker qou-cds2); see docs/audits/2026-09-08-l2-1ppq-research-program-gaps.md §6.3 item 2 / §7.3 C3. Nine trackers, previously linked only cds2↔8iru and htsi→t9r1, now all point there.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-08 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-10-10 — pointer

Tracked under carriers M6 and M8 of epic `qou-d8c7` "Mass endomorphism" (issue litlfred/qou#7547). Parent and status unchanged; the epic body lists what is still open for this item and where it sits in the attack-vector catalogue.

## 2026-11-16 — Convention D Wenzl Level r=2 Identity (`QOU.Foundations.ConventionDFrobeniusMarkovTower`, PR #8166)
- Formalized `wenzlLevelRTwoResidual`, `conventionD_wenzl_level_two_residual_eq_one`, `conventionD_wenzl_level_two_identity`, `threeRowFactor`, and `conventionD_three_row_factor_vanishes` in `folio/quantum-observable-universe/lean/QOU/Foundations/ConventionDFrobeniusMarkovTower.lean` (pure Lean 4 core, generic `CommRingOps R` per §7c, `0` `sorry`, `0` warnings, `0` vacuity audit hits; wired into `QOU.lean`).
- Commit: `246ab0f17af473b433e680ddc0223712e5c0d13c` | PR: `https://github.com/litlfred/qou/pull/8166`
- Kept at `status: in-progress` per merge-manager protocol.
