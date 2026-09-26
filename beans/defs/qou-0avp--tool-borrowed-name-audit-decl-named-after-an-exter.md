---
# qou-0avp
title: 'TOOL: borrowed-name audit — decl named after an external theory whose statement is all local defs'
status: completed
type: task
priority: normal
created_at: 2026-08-26T18:58:13Z
updated_at: 2026-08-30T07:14:17Z
---

## The gap this fills (measured, not assumed)

Sibling tool bean: `qou-k9yt` — [`scripts/lean-definition-collapsed-audit.py`](../scripts/lean-definition-collapsed-audit.py),
which detects theorems made true by a local `def` rather than by an argument.
That detector requires **two** signals:

- **A. COLLAPSED** — proof is `rfl` / `by rfl` / `simp`/`unfold` over a same-file `def`.
- **B. OPEN-CLAIM** — the docstring *admits* the statement is open ("open input",
  "body is `sorry`", "not in Mathlib", "unproved").

**The laundering shape this bean targets escapes BOTH signals**, because it is the
mirror image of B: the docstring *over*-claims rather than admitting openness.

### Worked instance — `QOU.BraidsAndKnots.dtEuler_eq_deltaLambdaG`

Cited corpus-wide (AGENTS.md, `STATUS.md`, `qou-f0ny`) as *"the per-partition Δ_λ
value is PROVED, sorry-free, general-n"*. Unfolded:

```lean
def gradedDimG   (N d k : ℕ) : ℕ := if k = N then d else 0   -- one-hot
def dtEulerG     (N d : ℕ) : ℤ := Σ_{k ≤ N} (-1)^k * gradedDimG N d k
def deltaLambdaG (N d : ℕ) : ℤ := (-1)^N * d
theorem dtEulerG_eq_deltaLambdaG : dtEulerG N d = deltaLambdaG N d := by
  rw [dtEulerG_collapse]; rfl
```

The "DT / 3d-index graded Euler characteristic" is the alternating sum of a list
that is zero except in one slot. There is no moduli space, no Behrend function,
no perverse sheaf — `(-1)^N` is *named* the Behrend sign by the docstring. The
one piece of genuine content is the *other* leg,
`aStat_eq_sumChoose2_conjugate` (`n(λ) = Σ_i C(λ'_i, 2)`), which is classical:
Macdonald, *Symmetric Functions and Hall Polynomials*, I.1 Ex. 2.

**Why `lean-definition-collapsed-audit.py` reports 0 on it** — verified by running it:

- **Signal B never fires.** `DOC_OPEN` matches admissions of openness. This
  docstring says *"THE GENERAL-`n` UNIFICATION"* and *"the real content"*.
- **Signal A never fires either.** `TRIVIAL_TAIL` matches `:= rfl` / `:= by rfl`;
  this is `:= by rw [dtEulerG_collapse]; rfl`. `SIMP_ARGS` looks for a same-file
  plain `def` among the rewrite arguments; `dtEulerG_collapse` is a *theorem*.

So the shape is invisible to every checker in the tree, exactly as `qou-k9yt`
records for its own shape and AGENTS.md §3b-tax records for empty Prop carriers.

## The proposed signal

**BORROWED NAME** — the decl name or docstring invokes an external named theory
(Donaldson–Thomas, Behrend, Springer, Seifert, Verlinde, Peter–Weyl, Kazhdan–Lusztig,
Chebyshev, Yang–Baxter, Schur, Hoefsmit, Wedderburn, …) while **every** non-Mathlib
symbol occurring in the *statement* resolves to a `def`/`abbrev` in the same file,
and the proof cites no external theorem.

`BORROWED ∧ COLLAPSED-ish` ⇒ the theorem is about the file's own definitions and
is named after somebody else's theorem. That is not automatically a defect — a
definitional restatement that *says so* is legitimate — so this is a high-recall
candidate generator like every other vacuity criterion, and the genuine/legit
verdict stays an agent call per the review-ledger discipline.

## Prior art in this corpus — do NOT re-derive

- `qou-k9yt` — the definition-collapsed detector (sibling axis; A ∧ B).
- `qou-wcff` — **completed**; found the same shape in
  `brings-surface/genus-filtration-ideal.lean` (`seifertGenus_T2p p := (p-1)/2`
  and `torusEmbeddable m n g := (m-1)*(n-1) ≤ 2*g` entered as definitions, so the
  knot theory is typed in rather than proved). Its *instance* half is discharged;
  its **checker** half — *"extend the vacuity detector to flag `theorem X : A = B`
  where A and B are definitionally equal after unfolding the file's own defs"* —
  is the other half of this bean.
- `qou-yifx` — **todo**; the "signed Springer dimension" has no T.A. Springer
  citation registered anywhere in `references.ts`. Same defect class, caught by
  hand from the bibliography side rather than the Lean side.

## How this bean was reached

An owner question — *"any genuinely new significant results not dependent on
internal conjecture?"* — measured over all 3,530 content blocks: 744 provable,
576 with no `conj:` in the transitive `uses[]` cone, 460 resolving to Lean,
**353** sorry-free / axiom-free / no conjecture-class hypothesis / no `: True`.
Ranked by proof depth the set collapses immediately; the deepest item corpus-wide
(`prop:polynomial-bar-involution`, 339 lines) proves that `X ↦ -X` is a ring
involution on `R[X]` with fixed subring `R[X²]`.



## Built and swept (2026-08-26)

[`scripts/lean-borrowed-name-audit.py`](../scripts/lean-borrowed-name-audit.py),
witness [`docs/audits/2026-08-26-borrowed-name-audit.witness.json`](../docs/audits/2026-08-26-borrowed-name-audit.witness.json).

**The two signals in the plan above were not enough**, and this is the part
worth carrying forward: `BORROWED and LOCAL-ONLY` fires **1121** times, about a
third of the provable decls in the tree. A generator that flags a third of the
corpus is noise. Two further signals were needed — OVERCLAIM (docstring asserts
the decl carries the external theory's content) and CHEAP (<=4 restate-only
tactic steps, no cross-file lemma):

    CRITICAL  BORROWED + LOCAL-ONLY + OVERCLAIM + CHEAP     12
    major     BORROWED + LOCAL-ONLY + CHEAP                197
    advisory  BORROWED + LOCAL-ONLY                        939

**Best independent catch** (not designed for): `seifert_euler_relation` in
`QOU/BraidKnot/Sigma1CubedSeifertTessellation.lean`. `seifertDisks := 2`,
`seifertBands := 3`, `boundaryComponents := 1`, `seifertGenus := 1` are all
hand-entered, so `-1 = 2 - 2*1 - 1` by `decide` cannot fail — while the
docstring says *"This is the genuine check (had the cell count been wrong, this
would fail)"*. The falsifiability claim is exactly backwards.

Spot-checked 4 of 12: 3 genuine, 1 (`hecke_n3_frobenius_codim`) arguably
legitimate — a real symbolic identity that merely happens to be named after
Frobenius. **Sample of four; not a precision rate.**

## Next (NOT done here)

- Agent-adjudicate the 12 into `docs/audits/lean-vacuity-review-ledger.json`.
- Triage the 197 `major`.
- Decide whether this becomes a `qa-sweep` criterion or stays a standalone
  script like its sibling `lean-definition-collapsed-audit.py`.



## CORRECTION — the kernel overturned one of my own claims (2026-08-26)

Asked whether this was AST-based, the answer was no: the tool above is
line/regex. So a kernel companion was built —
[`scripts/lean/BorrowedNameKernel.lean`](../scripts/lean/BorrowedNameKernel.lean)
+ [`scripts/lean/audit-driver.sh`](../scripts/lean/audit-driver.sh) — which
reads the ENVIRONMENT rather than the source text: `Expr.getUsedConstants` on
the type and on the proof term, resolved through `Environment.getModuleIdxFor?`,
plus `Meta.isDefEq` on the two sides of the statement under `forallTelescope`.
That last check is the one bean `qou-wcff` asked for and the one no text
scanner can approximate: definitional equality is decided by the kernel, not
by the shape of the tactic block.

**It immediately contradicted me.** I described `dtEulerG_eq_deltaLambdaG` as
"rfl-level arithmetic". The kernel says `defeq_collapse = false`,
`value_is_rfl = false`: with `N` free, `List.range (N+1)` does not reduce, so
`dtEulerG_collapse` is a real (elementary) induction, not a `rfl`.

**What survives unchanged** is the naming/scope claim, which the kernel
independently confirms: `local_only = true`, `value_foreign = 0` — the
statement quantifies over nothing but this file's own `def`s and the proof
cites nothing outside the file. Calling the alternating sum of a one-hot list
"the DT/3d-index graded Euler characteristic" with a "Behrend sign" is
nomenclature, not geometry. But "proved by rfl" was wrong and is retracted.

The kernel pass also found a definitional collapse the regex missed:
`PartitionOf5.dtEuler_eq_dtEulerG` is `defeq_collapse = true` AND
`value_is_rfl = true`. Regex flagged neither. **The two tools are
complementary, not redundant** — text sees names and docstrings, the kernel
sees reduction.

Environment note for whoever runs this: the olean cache restores the ROOT
workspace, so LEAN_PATH must be anchored at `$ROOT/.lake/packages/*`, not at
`content/<paper>/lean/.lake/packages/*` (the latter has batteries but no
Mathlib, and fails as "unknown module prefix 'Mathlib'", which reads like a
missing cache). Both traps are documented in the driver header.



## Adjudicated 2026-08-26 — all 19 CRITICAL into the vacuity ledger

11 genuine / 1 advisory / 7 legit. **Measured precision 63%**, against the 75%
a sample of four suggested. The 7 false positives are one characterisable
class — real symbolic or finite computations merely *named* after a
mathematician — which is the expected LOCAL-ONLY failure mode and the lead
for refinement. The 197 `major` remain untriaged.



## `major` tier triaged 2026-08-26 (197 -> 115), sample-adjudicated

**Two principled exclusions**, both demoting to advisory rather than dropping:
1. `@[simp]` unfolding of a local def — definitional BY DESIGN. **All 62** of
   the one-file cluster were these.
2. Proof discharges via a binder FIELD (`tau.commutator`) — a genuine
   conditional derivation. Ported from the sibling detector `qou-k9yt`.

The 62-in-one-file concentration was the **per-item-counting trap** AGENTS.md
records for the witness queue. After the exclusions, file concentration among
survivors is flat (max 5), so a rate over them is no longer dominated by one file.

CRITICAL unchanged at 19 — the exclusions do not reach that tier.

**Sampled 8 at random (seed 7); 5 resolved by reading the definitions:**
2 genuine, 3 legit ⇒ **~40% on a sample of five**, against 63% at CRITICAL.
Lower is expected: `major` is exactly CRITICAL minus the OVERCLAIM gate.
**Do not quote 40% as the tier rate** — n=5.

Sharpest `major` catch: `kl_eigenvalue_at_one_eq_pairCount` —
`klEigenvalueAtOne : Int := 2` and `pairCount : Int := 2` are two
independently hand-entered literals, so the theorem is `2 = 2 := rfl`, while
its docstring calls it *"the q->1 one-loop restores the doubled total"*.

**Still open:** 110 of the 115 unadjudicated. The kernel pass is the scalable
route (`defeq_collapse` decides table-lookup vs real content without reading
each file), but it is SLOW — 8 modules exceeded 10 minutes — and only 23 of
the 56 library modules involved have oleans in the restored cache.



## Kernel scaling measured; BringsSurface cluster adjudicated (2026-08-26, post-merge)

**Batch at ~8 modules.** Two separate limits bite on longer lists and both are
now set in the driver: `maxRecDepth` (fine at 8, fails at 15 building the list
literal) and the **command's own 200000-heartbeat budget**, which is separate
from the 20000 cap `defeqCollapse` puts around each `isDefEq`. Even with both
lifted, throughput binds: 8 modules ≈ 2m40s consistently, 15 in one command
exceeds 9m40s, and one 6-module batch of heavier files times out.

**Cumulative: 16 modules, 221 theorems, 39 defeq collapses.**

**Largest cluster — `QOU/BringsSurface.lean`, 8 collapses.** Every input is a
hand-entered literal (`genus := 4`, `eulerChar := -6`, `covering_degree := 4`,
`num_branch_points := 6`, `automorphism_order := 120`). The **values are
correct** for Bring's surface and are standard citable facts — the defect is not
a wrong number, it is that nothing derives them, so a relation between them
cannot fail.

Sharpest: `theorem is_qou (_bq : BringsQOU) : eulerChar = (covering_degree : ℤ)
* 2 - 14 := riemann_hurwitz_check` — takes a `BringsQOU` and **discards it**,
returning constant arithmetic. The name asserts the framework's central
identification; the statement says `-6 = -6` with the QOU structure unused.

Also `riemann_hurwitz_check` (R-H not applied; its conclusion is typed in) and
`euler_genus_relation` — the `seifert_euler_relation` shape exactly. All three
adjudicated **genuine**; ledger now 182.



## Sharpest catch of the audit — `quantum_peter_weyl_completeness` (2026-08-27)

```lean
def eigenspace_dim (twice_j : ℕ) : ℕ := (twice_j + 1) ^ 2

/-- **Quantum Peter–Weyl completeness.** The matrix coefficients {D^j_{mn}}
    form a complete orthonormal basis of L²(A).
    This is an axiom of the formalization. … Tannaka–Krein reconstruction …
    Ref: [woronowicz1987] https://doi.org/10.1007/BF01219077 -/
theorem quantum_peter_weyl_completeness :
    ∀ (twice_j : ℕ), eigenspace_dim twice_j = (twice_j + 1) ^ 2 := by
  intro twice_j; rfl
```

The theorem unfolds its own definition — literally `x = x`. Kernel-confirmed
`defeq_collapse=true`, `value_is_rfl=true`, `local_only=true`.

**It is the AGENTS.md §1a audit-dodge shape by its own words.** The docstring
says *"This is an axiom of the formalization"* while the declaration is a
`theorem`. §1a: a docstring saying "stated as an opaque axiom" beside a
`theorem … := by rfl` is **strictly worse than an `axiom`, because an axiom is
visible to `#print axioms` and this is not.** Same shape `qou-wcff` recorded
for genus-filtration-ideal. Adjudicated **genuine**; ledger 183.

Honest dispositions per §1a: prove the real completeness statement; or state it
with `sorry` + `-- Ref: [woronowicz1987]`; or declare it an `axiom` so the
axiom audit can see it.

## Kernel scaling, follow-up measurement

The 7 modules that timed out as one batch were retried at **batch size 3**:
3 completed in 4m14s, the remaining 4 still time out at 560s. **Batch size
alone does not rescue the heaviest modules** — those need their own budget.
Cumulative: 19 modules, 352 theorems, 56 defeq collapses.


---

## 2026-08-27 — the four "impossible" modules, resolved 3–1

Ran solo (2400 s each) after the batch-5 finding that PermutationEnumeration
completes alone:

    PermutationEnumeration          73 thms /  58 collapses   79 %
    MassEndomorphism.ZHabiroCauchy       38 /   7             18 %
    Mathlib.NonAbelianStokes             48 /   7             14 %
    Knots.KauffmanTL3               TIMED OUT at 2400 s

**Corrects a claim in the merged PR #5875**, which said "the constraint was the
BATCH, not the module". True for three of four. KauffmanTL3 is genuinely too
heavy: its own docstring records the 8_19 `decide` as ~70 s of kernel reduction
on its own, and the pass then runs isDefEq over every theorem in the module,
several carrying those same bracket reductions. A batch budget was never its
problem.

Corrected: solo running recovers a module the batch STARVED; it does not
recover one whose own reductions exceed the budget.

Recorded in `docs/audits/2026-08-26-kernel-defeq-sample.witness.json`
(batch6_note), landed on branch
`claude/lean-vacuity-detector-shared-machinery-2026-08-27` / PR #5880 rather
than a third PR — it corrects the PR that spawned that branch and touches no
detector code.

Kernel sample now 53 modules / 994 theorems / 252 collapses — still 2.3 % of
the 2257-module QOU tree. The collapse range across the sample is now 14–79 %,
which strengthens rather than weakens batch 5's conclusion that the rate is not
a quality signal: the two new low-end modules and the 79 % high-end one are all
substantially legitimate.

Remaining on this bean: 34 unadjudicated `major` candidates (expected yield near
zero — §6a of #5875 measures the genuine findings as concentrated 16-of-18 in
the mass/binding files, and the remainder sit outside them), and 741 QOU modules
with no olean, two of which are known compile failures.


---

## 2026-08-30 — both tiers drained; the kernel pass gained a second predicate

**Adjudication complete: 177 of 177 borrowed-name findings** (27 CRITICAL, 150
major). Verdicts: 104 legit, 41 advisory, 37 genuine. Ledger 346 entries,
0 stale. PR #6093.

**Ledger staleness backlog cleared, and it produced the first measured
remediations.** 15 entries stale after the rebase (I first reported 4 — my gate
checked only my own 152). Two were *fixed declarations*: `q_ns_wellposedness`
genuine → legit (was `ctx.wellposedness_holds`, now composes assumed hypotheses
with in-file proofs, and its module docstring cites the finding by name), and
`traceInner_nonneg_of_posSemidef` advisory → legit (axiom → full spectral
proof). `toffoli_transfer_matrix` is partially remediated with a *stronger*
finding: two of five conjuncts removed as FALSE, not merely self-assuming, so
the class was uninhabitable in its intended model.

**The kernel finding is the durable one: `defeqCollapse` is structurally blind
to `proof-no-self-assuming-projection`,** which is 111 of the 168 genuine
verdicts. Measured on 117 theorems in 10 modules chosen for that family: 1
collapse total, and 0 of the 5 targets it could see. The reason is not sample
size — `defeqCollapse` asks about the STATEMENT, and a projection's statement
is two opaque class-field applications with nothing to reduce; the defect is
entirely in the VALUE.

**Implemented the fix.** `BorrowedNameKernel.valueOnlyProjects` /
`value_only_projects`: every own-module constant in the proof term is a field
projection, at least one is. Same 117 theorems — `defeq_collapse` 1 (0.85 %),
`value_only_projects` 21 (17.9 %). Recall 6/6 on targets. Precision validated
on the one case that can decide it: `q_ns_wellposedness` does NOT fire, so the
predicate separates the pre- and post-remediation forms of the same
declaration, i.e. the §3b-cond forbidden pattern from the sanctioned one.

**Two follow-ups, both named and neither done:**
1. False-positive class: it reads only own-module constants, so a proof doing
   real work through Mathlib alone is indistinguishable from a projection
   (measured: `langlands_dual_pos`, and the two `q_ns` conjuncts). Fix is a
   non-local non-packaging constant count; needs its own recall measurement.
2. The pass enumerates THEOREMS, so a `def` carrying a proposition — the
   AGENTS.md §1a def-disguise, the whole reason that rule exists — is invisible
   to it. `toffoli_transfer_matrix` is one, adjudicated genuine, and its module
   reports 0 of 3.

**Trap for the next agent:** the first version of `valueOnlyProjects` returned
ZERO across five modules chosen for containing the defect. Field access leaves
BOTH the projection AND the structure in `getUsedConstants`, so
`all isFieldProjection` is false exactly when the structure is local. A detector
returning zero on its own designed-for population is a bug until proved
otherwise.


---

## CLOSED 2026-08-30 — merged as 1f6538d38 (PR #6093)

Both borrowed-name tiers drained: **27 CRITICAL + 150 major = 177 of 177
adjudicated**. Verdicts 104 legit / 41 advisory / 37 genuine. Ledger 368 entries
(mine ∪ 22 that landed on main mid-verification), 0 stale, and
`lean-vacuity-axiom-audit.ts --check-ledger` exits 0 on the merged state.

The durable result is not the drain, it is what the drain revealed about the
detector: **`defeqCollapse` is structurally blind to
`proof-no-self-assuming-projection`**, which is 111 of 168 genuine verdicts. It
asks about the STATEMENT; that family's statement is two opaque class-field
applications with nothing to reduce, and the defect is entirely in the VALUE.
Measured 0 collapses on 7 such verdicts. Fixed by `valueOnlyProjects`
(21/117 vs defeq's 1/117 on the same theorems; 6/6 recall on targets; correctly
does NOT fire on `q_ns_wellposedness` post-remediation, so it separates the
§3b-cond forbidden pattern from the sanctioned one). `isAuthoredClaim` also now
analyses Prop-typed `def`s, so the §1a def-disguise is visible for the first
time.

Two corrections published rather than buried: the "17 collapse / 2 not" figure
was wrong twice over (bare-decl-name join across files — the arity conflation
AGENTS.md warns about, committed inside the tooling that measures the audit that
exists to catch it; correct split is 12/18 on the def-arm family, 0/7 on the
projection family), and I first reported 4 stale ledger entries when the true
figure was 15.

**Successors:** `qou-qcy6` (third detector — class-field-graph shape, raised by
a sibling on #6097 and verified here). Still open and unclaimed: the
`valueOnlyProjects` Mathlib false-positive class — it reads only own-module
constants, so a proof doing real work through Mathlib alone is indistinguishable
from a pure projection; the fix is a non-local non-packaging constant count and
it needs its own recall measurement.
