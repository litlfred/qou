---
# qou-0avp
title: 'TOOL: borrowed-name audit — decl named after an external theory whose statement is all local defs'
status: in-progress
type: task
priority: normal
created_at: 2026-08-26T18:58:13Z
updated_at: 2026-08-26T19:29:31Z
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
