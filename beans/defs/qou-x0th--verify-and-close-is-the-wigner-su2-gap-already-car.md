---
# qou-x0th
title: 'OPEN (not a verify-and-close): the SU(2) -> SO(3) architectural gap is D10, the WignerSU4 files are D11 and cannot carry it, and the Lean does not derive the falsification'
status: todo
pr: 8192
type: task
priority: normal
tags:
    - 8f-open
    - 8f-lean
    - reorg-2026-10-04
    - split-from-nmib
created_at: 2026-10-10T08:27:45Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-8lxd
---

Split out of `qou-nmib` on 2026-10-10. **Probably a verify-and-close, not a
formalisation** — read the two files below before writing any Lean.

`qou-nmib` asked, in one title, for "H3 Delta baryon map **and** Wigner SU(2)
gap resolution". The second half appears already carried. Two substantive
sorry-free Lean files exist on the live tree, neither a stub:

**1. `folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/WignerSU4FromSpinIsospin.lean`**
The D11 carrier for `conj:wigner-su4-from-spin-isospin` — `SU(4) = SU(2)_S ×
SU(2)_I` as the combined classical limit of the spin `SO(3)` fibre action (D10)
and the canonical isospin `ℤ/2` swap (D9).

- `class WignerSU4FromSpinIsospin` (line 100), **no instance provided** — the
  honest open state for a conjecture per §3b.
- `wignerSU4_occupancy_via_plancherel` (127).
- `wignerSU4FromSpinIsospin_refutable` (139) / `_satisfiable` (152). **This pair
  is the part worth not losing**: without it, a conjecture class is
  indistinguishable from one that is vacuously unsatisfiable, and this file's own
  history is exactly that failure — see below.

**2. `folio/quantum-observable-universe/lean/QOU/Mass/WignerSU4RowBoundInactive.lean`**
The row-cap side: `rows`, `rows_le`, `SU4Admissible p := rows p ≤ 4`,
`su4_inactive_of_le_four`, `su4_filter_eq_univ`, `su4_restricted_sum_eq`,
`su4_no_magic_enhancement`, and `su4_active_at_five` as the non-vacuity witness
(the bound bites only from `n = 5`, so the earlier theorems are applicable rather
than conditionally empty).

## The trap this file already fell into, recorded so it is not re-introduced

Per that file's own docstring: its two content-bearing fields once read

```lean
dynamic_capacity_from_plancherel_weight (A Z N : ℕ) (S W_lam E_gate E_0 : ℝ) :
  E_gate = E_0 * Real.log (1 / W_lam)
```

— an equation between **four unrelated reals with no hypothesis linking them**.
Instantiating `E_gate := 1`, `E_0 := 0` gives `1 = 0`, so
`¬ Nonempty WignerSU4FromSpinIsospin` was **provable**: the class had no instance
*and could not have one*. Repaired on an owner ruling, together with a `.ts` ref
that resolved to a **different**, vacuous `holds : Prop` stub — so the block was
reading a carrier that asserted nothing while the one asserting something had no
reader.

## What this bean actually needs

1. **State what "the gap" was.** `qou-nmib` never said; its title is the only
   record. Candidates: the `SU(2)_S × SU(2)_I` factorisation itself, the
   `su4_inactive_of_le_four` vacuity window (`n ≤ 4`), or the occupancy weight.
   Corpus-grep `conj:wigner-su4-from-spin-isospin`'s consumers first.
2. **Check it against the two files**, including `#print axioms` on the named
   declarations.
3. **Close with evidence, or re-scope to whatever is genuinely missing.**

**Default if unanswered: nothing happens** — the two files stay as they are and
remain correct; only the ledger stays unclear about whether the item is done.

**Blast radius:** read-only unless step 3 finds a gap. No compute, no witness.


## 2026-10-10 — NOT a verify-and-close. Re-scoped, stays open.

Worked as step 1 of the bean's own plan ("state what the gap was; check it
against the two files"). Both steps done. The answer to the title's question is
**no**, and identifying the gap turned out to be the valuable part.

### Step 1 — what "the gap" is, and the title's phrase is not the corpus's

**The phrase "SU(2) gap" occurs in exactly two places in the repo: this bean,
and one migration mapping TSV.** It is not corpus vocabulary; it came from
`qou-nmib`'s title. What the corpus names is the **SU(2) → SO(3) architectural
gap** — `docs/audits/2026-05-24-h4-coefficient-source-trace-and-so3-gap.md`,
whose own title carries it, triggered by the author's observation *"there was
supposed to be h⁴ terms … but related to full SO(3) action. SU(2) picked up
quadratic terms."*

In the duality tracker it is **D10** (spin `SU(2)_S`), whose row reads
`⏳ scaffold` with *"full SO(3) gap flagged in …"*. So `qou-nmib` compressed
"Wigner SU(4) = SU(2)_S × SU(2)_I" (D11) and "the SO(3) gap" (D10) into one
phrase.

### Step 2 — the two files are D11, so they CANNOT carry it

`WignerSU4FromSpinIsospin.lean` and `WignerSU4RowBoundInactive.lean` are the
**D11** carrier. The tracker's D11 row states its own precondition:
*"requires D9 + D10 both ✅ first"*. D10 **is** the gap. A carrier downstream of
a gap does not close it, and this one is honest about its state — the class has
**no instance**, which is the correct open representation.

### The gap is OPEN, and its original mechanism is REFUTED

`docs/audits/2026-06-01-s5-so3-su2-u1-fiber-action.md` supersedes the 2026-05-24
doc (which now opens with a correction banner pointing at it). Its VERDICT,
quoted because it is the live state:

> The geometric fiber map is **NOT derivable** from the current structure. …
> the conjecture's load-bearing premise — "the S₃ truncation sees only ℓ≤1, so
> ℓ=2 is the NEW thing the full SO(3) opens" — **is FALSE**: the (2,1)/std irrep
> that carries h⁴ already appears at BOTH ℓ=1 and ℓ=2 (multiplicities 1 and 2)
> … The three correspondences FACTOR — they do not unify into one fiber action.
> This is a CLEAN NEGATIVE.

Per-correspondence: **SO(3)/h⁴ OPEN**, **SU(2)/spin PARTIALLY DERIVED**,
**U(1)/hypercharge OPEN**.

### 🛑 NEW FINDING — the Lean that audit calls "DERIVED, sorry-free" does not derive the falsification

`folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean`
— 885 lines, 37 theorems, **sorry-free** (its only `sorry` match is a docstring
heading). Measured:

- **Zero `import` lines.** No Mathlib. No `Subgroup`, `Perfect`, `commutator`
  or `Equiv.Perm` anywhere outside docstrings.
- **The only proof tactic in the file is `decide`** (5 occurrences, plus
  `cases p <;> decide` and one `rfl`). Everything is a finite exhaustive check
  over hand-encoded `List ℕ` data.

**That is legitimate in itself** — AGENTS.md item 6 permits `decide` on a
genuinely decidable finite computation, and the file is better engineered than a
first read suggests: `s3rot_branching_dim_check` constrains
`s3RotBranchingMult` at every `ℓ ≤ 4` to satisfy
`Σ_μ mult(μ) · dim(μ) = 2ℓ+1`, `s5_to_s3_restriction_dim_consistent` does the
same for the S₅→S₃ table, both guard `List.zipWith` against silent truncation
(citing #2431), and a sibling script
`scripts/s5so3_branching_backbone_verify.py` cross-checks embedding-independence.
**My first reading was "it derives nothing", and that was too strong.**

**The correct, narrower claim: the guards constrain the tables but do not PIN
them, and the falsification lives in exactly the unpinned coordinate.** With
`s3IrrepDims = [1, 1, 2]`, the level-`ℓ` constraint is `a + b + 2c = 2ℓ+1`,
which leaves the std multiplicity `c` free. Constructed and checked:

| ℓ | committed | std mult | an alternative passing every guard | std mult |
|---|---|---:|---|---:|
| 0 | `[1,0,0]` | 0 | `[1,0,0]` | 0 |
| 1 | `[0,1,1]` | **1** | `[3,0,0]` | **0** |
| 2 | `[1,0,2]` | **2** | `[3,0,1]` | **1** |
| 3 | `[1,2,2]` | 2 | `[5,0,1]` | 1 |
| 4 | `[2,1,3]` | 3 | `[7,0,1]` | 1 |

The right-hand table satisfies `s3rot_branching_dim_check` at all five levels —
and under it the std irrep appears at `ℓ = 2` and **not** at `ℓ = 1`, i.e. it
**restores the very premise the audit reports as falsified.** So the Lean does
not establish the falsification; it restates a table whose correctness rests on
standard character theory checked in Python. (A second, milder degeneracy: the
trivial and sign multiplicities both have dimension 1, so swapping them at every
level also passes every guard and leaves the std spot-check untouched — which
matters, because this same file carries a Δ_λ **chirality** section where
triv-vs-sign is the distinction.)

**And one theorem is the item-8 case outright.** `spin_Z2_ne_sign_Z2`, which the
audit names as the arc's *"genuine derived structural result"*, is:

```lean
theorem spin_Z2_ne_sign_Z2 :
    let binaryIcosahedralAbelianizationOrder : ℕ := 1   -- 2I is perfect
    let s5AbelianizationOrder : ℕ := 2                  -- sign character
    binaryIcosahedralAbelianizationOrder ≠ s5AbelianizationOrder := by
  decide
```

It proves `1 ≠ 2`. Both numerals are `let`-bound and the mathematics — that `2I`
is perfect and that `S₅`'s abelianisation is `ℤ₂` — is in **comments**. Unlike
the branching tables, nothing constrains these two numerals at all. AGENTS.md
Strict Lean Discipline item 8: *"if the statement doesn't say something
falsifiable about the domain, it is not a theorem."*

**None of this says the mathematics is wrong.** The branching multiplicities and
`2I`-perfect are standard and are almost certainly right. The claim is the
"sorry-free ≠ derived" one: the Lean restates them rather than establishing
them, so citing this file as having *derived* the falsification over-states it.
**This is the second instance of that class in one session** — the first was
`λ_C` / `a_asym` on `qou-opjb`, where the only two theorems are `unfold; ring`
identities over `noncomputable def`s.

**Minor correction of the audit**: its Lean section says the facts were added
*"with `native_decide` / explicit data"*. There is **zero** `native_decide` in
the file. So the anti-laundering concern item 6 raises about that tactic does not
arise here.

### Two stale pointers, found en route

- `docs/duality-tracker.md:40` links D11 at
  `folio/quantum-observable-universe/braids-and-knots/wigner-su4-from-spin-isospin.md`.
  **That file does not exist**; the block is under `nuclear-interactions/`.
- The 2026-06-01 audit's Lean section cites
  `folio/quantum-observable-universe/lean/...` — the **pre-rename** path
  (`content/` → `folio/`).

Neither fixed here: both are one-line edits in another arc's documents, and
under the ask-first rule a doc-path sweep is not mine to start.

### Disposition

**Stays `todo`.** Re-titled to name the gap the corpus names. What would close it
is D10 — a derived map from the 5-strand `A₅ ⊂ S₅` fibre data to the 3-strand
`S₃/H₃` Borromean trace — which the 2026-06-01 audit reports as not derivable
from the current structure. **Do not pick this up expecting a repair**, and do
not cite `S5SO3FiberAction.lean` as having derived the falsification.


## Progress Checklist (Round 56 — PR #8192)
- [x] Non-vacuous Lean 4 formalization in `QOU.Eightfold.CPBarParityLevel3ChannelAndWignerS3Pinning` (`0` `sorry`, `0` vacuity audit findings)
- [x] 50-dps `mpmath` probe `computations/probes/cp_bar_parity_level3_channel_and_wigner_s3_pinning_probe.py` and stamped witness `computations/probes/cp-bar-parity-level3-channel-and-wigner-s3-pinning.witness.json` (`allPassed: true`, `scriptHash: d2a06f0c494a`, `scriptCommitSha: c0214e17e49e615dc65e266a92be3d79589d2874`)
- [x] Opened PR `litlfred/qou#8192` (`82fe2aa092fb7be41555f2084a2891bcea71c295`)
- [ ] Awaiting merge and final closure verification

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8192, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
