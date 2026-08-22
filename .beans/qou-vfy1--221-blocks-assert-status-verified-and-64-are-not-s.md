---
# qou-vfy1
title: '221 blocks assert computation.status "verified"; 64 are not supported by the witness they cite'
status: in-progress
type: task
priority: normal
created_at: 2026-08-22T05:20:00Z
updated_at: 2026-08-22T07:15:00Z
---

The quantified form of class **C2** in the `qou-3nva` ledger — a block and
its witness disagreeing, with the block winning. Measured corpus-wide
2026-08-22.

## Two findings, one scan

**1. ~~The `status` field should not be in a `.ts` at all.~~ RETRACTED
2026-08-22 — see the correction section at the end. The §4 count is **1**, not
278.** What the scan actually found is **277** `.ts` carrying a `status:` key,
of which **276 sit inside `computation: { … }`** — a field describing the
computation, which §4 does not govern. Finding 2 below is unaffected and is
the real content of this bean.

| value | count |
|---|---:|
| `verified` | 221 |
| `experimental` | 52 |
| `not_run` | 4 |
| `pending` | 1 |

**2. Of the 221 `verified` claims, 64 (29 %) are not supported by the
witness they name.**

| | count |
|---|---:|
| witness `allPassed: true` **with real assertions** | 157 |
| witness `allPassed: true` but **assertions array is empty** (vacuous) | **43** |
| witness reports **`allPassed: false`** | **8** |
| cited witness **missing or unreadable** | 5 |
| **no witness cited at all** | 8 |

The 43 vacuous ones are the interesting bulk: `allPassed: true` over zero
assertions is *true* and means nothing, and it is what a block points at
when it says "verified". Related but distinct from the ~383-witness bean on
the same shape — that one is about the witnesses; this is about the blocks
that **cite them as verification**.

## Limits of the measurement, stated

- **The 157 is an upper bound on genuine support.** Passing assertions do
  not imply the assertions *cover the block's claim*. The campaign found
  several where they do not — one witness's assertions covered clause (1)
  of a three-clause proposition; another's two assertions were both about
  vanishing while the block was cited for a field-membership sentence.
- **The 5 "missing" may over-count**: witness paths were resolved with a
  basename fallback under `computations/`, which will miss anything stored
  elsewhere.
- The scan reads the **first** `status` and the **first** witness path in
  each file.

Reproduce: the script is inline in the session; the shape is
`grep '^\s*status:\s*"' content/**/*.ts` joined against the first
`*.witness.json` named in the same file.

## What would close this

The systemic fix and the cleanup are the same act: **delete the field.**
§4 already says status is derived at build time from the Lean and the
witness, so a `.ts` asserting `verified` is both forbidden and structurally
incapable of being wrong — nothing checks it against the thing it claims.
Removing it makes the 64 unsupported claims disappear by construction,
because the derived status would read the witness.

If the field is kept for any reason, it needs a checker that fails when a
block claims `verified` while its witness is absent, failing, or vacuous —
which is the 64.

Order of work, cheapest first:

1. The **8 blocks citing a witness that reports `allPassed: false`** — a
   direct contradiction, and the smallest set.
2. The **8 with no witness at all** and the **5 unresolvable** — either the
   citation is wrong or the claim is unbacked.
3. The **43 vacuous** — these need the witness fixed (assertions added) or
   the block's claim withdrawn; they are not fixable from the block side.
4. The field's removal corpus-wide, per §4.


## The 21 non-vacuous cases, enumerated (2026-08-22)

The 43 vacuous-witness blocks need the witness fixed, not the block, so
they are left for a separate pass. These 21 are actionable from the block
side. **Correction to the original scan:** it resolved witness paths by
basename under `computations/` only, so it reported 5 "unresolvable" —
**all five actually resolve**, three of them somewhere other than where the
block says. That over-count is now fixed below.

### A. Block says `verified`; witness says `allPassed: false` (8)

| block | witness | failing assertions |
|---|---|---|
| `hadron-level-knot-table` | `hadron-knot-table` | **6** — `LP_stable(c14)`, `LP_stable(o16)`, `LP_stable(ne20)`, … |
| `he4-two-row-dominance` | `he4-canonical-tr-m-block-fingerprint` | **9** — `tr_M_at_q0`, `top5_cumulative_pct`, `trivial_rep_pct`, … |
| `gs-graded-markov-trace-existence` | `markov/markov-pipeline-cross-validation` | **3** — `tr_M_at_q0_archimedean[n]`, `[p]`, `no_atoms_only_in_term6` |
| `mba-sidecar-mirror-cancellation` | `delta-lambda-z-coefficient-and-slope` | 1 — `slope_10A5_refuted_at_A_ge_5` |
| `binding-qbeta-complex-volume` | `qbeta/qbeta-ck-sseries-operator-match` | 1 — `c2_gate` |
| `q-beta-c-2-eq-neg-one-structural` | `qbeta/qbeta-symbolic-chain-alpha-b` | 1 — `alpha_q0_matches_probe_n3_witness` |
| `y-lambda-cyclotomic-factorization` | `probes/y-lambda-cyclotomic-factorization-probe` | 1 — `denominator_factors_as_cyclotomic_product` |
| `deuteron-fusion-frame` | `substrate/deuteron-tower-fusion-frame-probe` | **0** — `allPassed: false` with an empty failing set |

The last is its own oddity and is already beaned separately (`D3`:
"exits 0 while allPassed is False"). The first three are the substantive
ones: a stability table whose witness reports six instabilities, and a
"two-row dominance" claim whose witness fails on the very quantities the
dominance is about.

Note what the three `c_k`/`α`-related rows have in common: each fails a
**gate** assertion — `c2_gate`, `alpha_q0_matches_probe_n3_witness`,
`slope_…_refuted_at_A_ge_5`. The gates are doing their job and the blocks
are ignoring them.

### B. Block says `verified`; cites no witness at all (8)

`mba-sidecar-delta-lambda-closure`, `mba-sidecar-lp-sdp-dual-emission`,
`mba-sidecar-witness-json-pipeline`, `mba-step01-categorical-action`,
`mba-step06-frobenius-pairing`, `qbeta-toroidal-harmonics-basis`,
`frakD-energy-decomposition`, `toroidal-harmonics-delta-lambda`.

Five of the eight are `mba-*` appendix blocks — the maintenance-contract
appendix, where an unbacked `verified` is worse than elsewhere because the
appendix exists to bind propositions to the compute. Independently,
`agent:l01` found `mba-step06`'s cited API (`pyhecke.check_frobenius`)
checks Frobenius *positivity*, not the pairing the block describes, and
`agent:h00`/`i00` flagged `toroidal-harmonics-delta-lambda` as
convention-C-dependent.

### C. Block says `verified`; the cited path is wrong (5 — all resolve elsewhere)

| block | cites | actually at |
|---|---|---|
| `per-braid-mass-tower` | `docs/audits/2026-05-01-per-braid-tower.witness.json` | **exists as cited** (`allPassed: true`, 3 assertions) |
| `wedderburn-weight-canonical` | `docs/audits/2026-05-01-p1-3a-bw-equivalence.witness.json` | **exists as cited** (`allPassed: true`, 2 assertions) |
| `markov-trace-recursive-reducer` | `markov-trace-axiomatic-multi-atom.witness.json` | `computations/**markov/**…` |
| `rho-k-graded-expansion` | `rho-k-markov-multiplicativity.witness.json` | `computations/**_deprecated/**…` |
| `he4-channel-active-set` | `magic-shell-empirical-instantiation.witness.json` | `computations/**_deprecated/**…` |

The first two are **my scan's false positives** — witnesses under
`docs/audits/` that my basename-under-`computations/` fallback could not
see. Recorded so the count is not repeated as 5.

The last two are the real finding in this group: a `verified` block whose
evidence lives under **`_deprecated/`**. That is the same shape
`agent:g01` found citing `confinement-lp.witness.json`, and
`agent:k00` found citing a `_deprecated/` witness at the old muon pin.

### Revised totals

| | |
|---|---:|
| assert `verified` | 221 |
| **contradicted by their own witness** | **8** |
| **no witness at all** | **8** |
| **witness path wrong; 2 of those resolve as written** | 3 real + 2 false positives |
| witness `allPassed: true` over an empty assertions array | 43 |
| passing with real assertions (upper bound — coverage unchecked) | 157 |

So **62** of 221, not 64.

---

## CORRECTION (2026-08-22) — finding 1 was wrong by a factor of ~278

I wrote *"**278** content-block `.ts` files carry"* a §4-forbidden `status`
field. Re-measured by **indentation and parent key** rather than by grepping
the token:

```
3584  .ts scanned under content/quantum-observable-universe/
 277  carry a `status:` key
 276  at 4-space indent, ALL of them inside `computation: { … }`
   1  at block level  ->  mass-endomorphism/qbeta-toroidal-harmonics-basis.ts:13
```

**`computation.status` is not the field §4 forbids.** §4 governs *formalization
status* — the thing derived at build time into `proof-objects.json`. Two
independent checks agree that these are different fields:

1. **Nesting.** All 276 are a key of the `computation` object, not of the block.
2. **Vocabulary.** §4 names the formalization values explicitly:
   `not_started`, `stated`, `has_sorry`, `proved`, `mathlib_ok`. The observed
   values are `verified` / `experimental` / `not_run` / `pending` — a
   **disjoint** set. These describe whether the *computation* was run, not
   whether the *Lean* was proved.

So the §4 violation is a single file — and that file is one of the three whose
manifest does not load at all (it imports `../../ontologist`, which does not
exist), so it is already covered by the manifest-loading work in #5367.

**Finding 2 stands unchanged and is the whole value of this bean.** Whether
`computation.status: "verified"` is *honest* is a real and separate question
from whether the key is allowed, and the answer is that 64 of 221 are not
supported by the witness they name. Two sibling batches hit the same class
independently from the other end: `universal-ilp-algorithm` and the
`lp-dual-stability` family each record `verified` against witnesses whose
assertion arrays are empty, whose `expected` equals `computed` as the same
literal string, or whose LP-dual fields are all `null` with a STUB note.

**Why the error happened, since it is the campaign's own recurring shape.** I
counted a *token* and reported it as a *claim*: "a `.ts` has a `status` field"
is not "a `.ts` has the field §4 forbids". That is the `da-arity-conflation`
failure AGENTS.md §"Grep the claim SHAPE, not only the topic" describes —
resolve the symbol and check what object it belongs to before asserting a rule
is violated. One `grep -c` looked like evidence; one indentation histogram was
the actual check.
