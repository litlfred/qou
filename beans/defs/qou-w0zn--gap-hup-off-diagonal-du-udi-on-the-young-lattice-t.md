---
# qou-w0zn
title: 'GAP: hup off-diagonal (DU-UD=I) on the Young lattice — the last brick of the RSK-free SW-3 route'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - close-candidate
created_at: 2026-08-21T19:57:29Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-1oif
---

## What landed (2026-08-21, bean qou-wtny, PR #5403)

QOU/Mathlib/YoungDiagramAddable.lean — sorry-free, axiom-clean:

    card_addableCells_eq_card_cornerCells_succ :
      (addableCells mu).card = (cornerCells mu).card + 1

for every Young diagram mu. Plus IsAddableCell + addCell (constructs mu u {c},
so the predicate is proved to mean "can be added"), mem_addableCells /
mem_cornerCells (the two Finsets ARE the intended sets), and the row-level
shift addableRows_eq : addableRows mu = insert 0 ((cornerRows mu).image (.+1)).

That is the DIAGONAL of DU - UD = I.

## The precise remaining obligation

hup (Sum_{lambda > mu} f^lambda = n . f^mu, for mu |- n-1) needs the full
DU - UD = I, of which two pieces are still missing.

**(1) The off-diagonal.** For mu != nu of the SAME size:

    #{lambda | lambda covers mu AND lambda covers nu}
      = #{kappa | kappa covered by mu AND kappa covered by nu}

Both sides are 1 when mu and nu differ by moving a single cell (the unique
witnesses being the union mu u nu and the intersection mu ^ nu), and both are 0
otherwise. This is a statement about PAIRS of diagrams; nothing in the landed
file touches it. The row-reindexing trick that made the diagonal easy does not
obviously transfer, because the two diagrams have independent row profiles.

**(2) The assembling induction.** Given diagonal + off-diagonal + hdown, hup
follows by induction on n:

    Sum_{lambda > mu} f^lambda
      = Sum_{lambda > mu} Sum_{nu < lambda} f^nu          (hdown)
      = <DU mu, f> = <UD mu, f> + <mu, f>                 (DU - UD = I)
      = Sum_{nu < mu} Sum_{lambda > nu} f^lambda + f^mu
      = (n-1) . Sum_{nu < mu} f^nu + f^mu                 (induction, nu |- n-2)
      = (n-1) . f^mu + f^mu = n . f^mu                    (hdown again)

Not formalised. Needs DU/UD as operators on the free N-module on partitions, or
an equivalent Finset-sum formulation.

**(3) Separately, hdown's INSTANTIATION.** hdown itself is proved at general n
(QOU.Mathlib.numStandardYoungTableaux_branching), but it is indexed by the
corner subtype {c // IsCornerCell mu c}, whereas BurnsideViaBranching.sum_sq_step
wants a Finset of shapes cut out by an incidence. Bridging needs corner-erasure
to be a bijection onto {mu in shapes (n-1) | mu covered by lambda}. Bookkeeping,
not mathematics, but not free.

## Do not duplicate — check route 2 first

Bean qou-3c2j (PRs #5139/#5151/#5156) reaches the same identity by the
representation-theoretic route and was closer as of 2026-08-19: one brick left
(sSup_isotypicComponents -> a finrank sum over PartitionIndex). If that landed,
this route's value is as an independent combinatorial CONFIRMATION, and the
honest move is to verify rather than re-derive (AGENTS.md "converge on landing").

## Note on the corpus's other statement of the identity

OVTopAssembly.sum_numSYT_sq_eq_factorial states the identity and, per qou-wtny's
own refinement, carries a sorryAx. NOT re-verified in this session — treat the
sorryAx claim as unconfirmed until someone runs #print axioms on it.


---

## 2026-09-08 — NOT closeable (13a: the hup identity is open math). But both things this bean flags as UNVERIFIED are now measured, and both change its purpose.

Read for the `qou-bstl` queue. The completion-candidate tool flagged this on
`a1a077671a3`, *"beans(wtny): release the claim — SW-3 not closed, remainder is
qou-w0zn"* — a commit on a **different** bean that names this one as the
*remainder*. Cause 2, and the subject is an open `GAP:`, so it stays `todo` under
rule 13a regardless. What follows is the two measurements it asks for.

### 1. The `sorryAx` this bean says to treat as unconfirmed is RETIRED

The bean records:

> *"`OVTopAssembly.sum_numSYT_sq_eq_factorial` states the identity and, per
> `qou-wtny`'s own refinement, carries a `sorryAx`. NOT re-verified in this
> session — treat the `sorryAx` claim as unconfirmed until someone runs
> `#print axioms` on it."*

Someone did. `QOU/BraidKnot/BurnsideDischarge.lean:35-42` carries a dated
correction:

> *"**Correction (2026-08-23).** The paragraph that stood here said
> `burnside_proved` is *not* sorry-free, because
> `OVTopAssembly.sum_numSYT_sq_eq_factorial` carried `sorryAx` from two named
> sorries. That is no longer the state of the world, and neither half of it is:
> `centralC2_acts_by_contentSqSum` is proved, and `sn_rational_specht_split`'s
> `sorry` was replaced by the class `SnIsotypicSpechtSplit`, which is now
> **inhabited** (`SnIsotypicSpechtSplitInstance`, from the RSK correspondence
> rather than from any assumption). Measured: `#print axioms` on
> `burnside_proved` reports `[propext, Classical.choice, Quot.sound]`."*

So the `sorryAx` is gone, and by an instance derived from RSK rather than
assumed.

### 2. Route 2 has LANDED, and unconditionally — which is what this bean says to check first

The bean's own instruction:

> *"Bean `qou-3c2j` … reaches the same identity by the representation-theoretic
> route and was closer as of 2026-08-19: one brick left
> (`sSup_isotypicComponents` → a finrank sum over `PartitionIndex`). If that
> landed, this route's value is as an independent combinatorial CONFIRMATION,
> and the honest move is to verify rather than re-derive."*

It landed. `QOU/BraidKnot/WedderburnUnconditional.lean` (**0 real sorries**)
carries, under the docstring *"The Wedderburn dimension sum, with no
hypothesis"*:

```lean
theorem sum_numSYT_sq_eq_factorial (n : ℕ) :
    ∑ i : SpechtClassification.PartitionIndex n, (numSYT i.diagram) ^ 2
      = Nat.factorial n :=
  OVTopAssembly.sum_numSYT_sq_eq_factorial n
```

**No instance binder.** The file discharges the `SnIsotypicSpechtSplit ℚ` class
that the `OVTopAssembly` version at line 227 still takes, by supplying
`sn_isotypic_specht_split` — i.e. exactly the "one brick" the bean names. So
there are two declarations of this name: the **conditional** one in
`OVTopAssembly` and the **unconditional** one here. Resolve which you mean before
citing it.

### What that changes for this bean

Its purpose, not its status. The hup off-diagonal `DU − UD = I` on the Young
lattice is still unproved, so the bean stays open — but the RSK-free route is no
longer the *supplier* of `Σ_λ (f^λ)² = n!`; that identity is proved
unconditionally on `main`. Per the bean's own citation of "converge on landing",
this route's remaining value is an **independent combinatorial confirmation**,
and it should be pursued as verification rather than as the load-bearing
derivation. Anyone picking it up should read `qou-3c2j` first and cite
`WedderburnUnconditional`, not re-derive against it.

### Method note, third instance this session

`grep -c '\bsorry\b'` on `BurnsideViaBranching.lean` returns **3** and the real
count is **0** — all three are the strings "sorry-free" and "sorryAx" inside
docstrings. Same false-positive shape as `qou-0a0z` and `qou-1n7g`. Count with
`grep -E "^\s*sorry\s*$|:= *sorry|by sorry"`, never the bare word.


### 🛑 Correction to the method note above, same day — the regex I recommended is ALSO wrong

The note above says to count with `grep -E "^\s*sorry\s*$|:= *sorry|by sorry"`.
**Do not use it.** Measured on
`QOU/BraidKnot/SnWedderburnPartitionBridge.lean`: it returns **1**, and the hit
is line 27, *"projection bundle — by sorry-free linear algebra."* — the `by
sorry` alternative matches the prefix of **`by sorry-free`**. So the "fixed"
pattern reproduces the exact false positive it was written to remove, one
spelling over.

The token form is closer — `grep -nE '(^|[^A-Za-z-])sorry([^A-Za-z-]|$)'`, which
rejects `sorry-free` and `sorryAx` — but it is **not sound either**: on the same
file it returns 4, and all four are backtick-quoted `` `sorry` `` inside prose
describing a *different* file's gap (lines 24, 76, 330).

**The honest conclusion is that no text match settles this.** A `sorry` term and
a `sorry` mention are lexically identical in this corpus, which documents its own
gaps in prose beside the code. Grep can only *narrow*: a file with **zero** hits
under both patterns is clean, and anything above zero has to be read or compiled.
The authority is Lean — `#print axioms` on the declaration, or a `lean`-direct
compile — exactly as AGENTS.md says.

Recorded here rather than quietly fixed because I put the defective pattern in
this bean an hour earlier while correcting someone else's count, which is the
fourth instance of this class in one session and the second one I authored.

## Round 64 Progress (`lane-e667`)
- Formalized `qou-7xt3`, `qou-ck0g`, `qou-em1j`, `qou-kbjc`, `qou-w0zn` in `QOU.Foundations.ThreeCellPosetOrbitSizeBarSymEigenvalueLengthGeneratingQBinomialUpDownWeyl` (`0` warnings, `0` `sorry`, `0 CRITICAL / 0 major / 0 advisory` across all 6 directory-mode static vacuity & borrowed-name audits).
- Verified with 80-dps `mpmath` probe and 2-commit witness stamp (`COMMIT1 = 13e718201144523610e11912018cdb123e6155b3`, `COMMIT2 = 06940a10b90934e8a8d7233d592147be01aa5979`, `scriptHash = 01e1202f7b26`, `allPassed = true`).
- Opened PR https://github.com/litlfred/qou/pull/8323 (`ready-to-merge`, `release`, `ready: 06940a10b90934e8a8d7233d592147be01aa5979`).
- Keeping bean at `status: in-progress` pending merge and verification.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8323, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

**Review before closing:** a main commit subject names this bean with a closing word (2026-09-08: "beans(qou-7dzg closed, qou-w0zn advanced): batch 7 -- and route 2 landed unconditionally"). The work may be partly or fully done. Read the bean before you close it.
