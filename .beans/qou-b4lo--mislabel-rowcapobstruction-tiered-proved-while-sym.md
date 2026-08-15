---
# qou-b4lo
title: 'MISLABEL: RowCapObstruction tiered ''proved'' while Sym2Gate/WeylInvariance get the arithmetic-vs-rep-theory caveat'
status: completed
type: task
priority: normal
created_at: 2026-08-08T13:03:35Z
updated_at: 2026-08-15T04:42:03Z
---

Found by the SM/eightfold epistemic accounting,
`docs/audits/2026-08-08-sm-eightfold-epistemic-accounting.md` §3.1
(Finding 2, material/tier).

**The inconsistency.** The eightfold chapter applies the
arithmetic-vs-representation-theory caveat in 2 of 3 places and omits it in
the third — the one place where it is load-bearing for the chapter's central
open problem (`N = 3`):

- `Sym2Gate.lean` gets it: *"What that file proves is only the arithmetic —
  its declarations reduce to identities such as `6 = 6 ∧ 0 = 0`, with the
  representation-theoretic content supplied by hand in the statement names,
  not by the proofs. … the file should not be cited as [a machine-checked
  pass]."* (`schur-weyl-eightfold.md:114-121`)
- `WeylInvarianceQDeformation.lean` gets it: a section headed **"What the
  Lean does not establish"** — *"What is machine-checked is the arithmetic of
  the separation on the `A₂` datum, which is a weaker statement and should
  not be cited for the stronger one."* (`q-deformation-weight-lattice.md:52-58`)
- `RowCapObstruction.lean` does **not**: *"**The obstruction is proved.**
  This is not an observation but a theorem, machine-checked sorry-free"*
  (`schur-weyl-eightfold.md:75-77`); ledger row
  `eightfold-open-problems.md:17` *"**proved** (Lean, sorry-free)"*.

**Evidence that the `Sym2Gate` sentence describes `RowCapObstruction`
verbatim.** Read in full (189 lines): every proof is `Nat.choose`
arithmetic. The headline theorem is

```lean
def weylDimAlt (N : ℕ) : ℕ := N.choose 3                    -- :92
theorem weyl_dim_alt_eq_zero_iff (N : ℕ) : weylDimAlt N = 0 ↔ N < 3 := by
  unfold weylDimAlt
  exact Nat.choose_eq_zero_iff                              -- :101-103
```

The rest are `by decide` / `omega` / `Nat.choose_le_choose`. The
representation theory — that `dim V_{(1³)}^{gl_N} = C(N,3)` (hook-content
formula) and the Schur–Weyl row cap `ℓ(λ) ≤ N` — is carried by the `def`
names and docstrings, not proved. The file's own docstring concedes the
boundary (:131-134, Worpitzky's identity "is **not** formalised here").

**Verification state:** `scripts/lean-verify.sh` → `✓ exit 0`, word-bounded
`sorry` count 0. So "sorry-free" is factually correct; the defect is purely
the tier word "proved" for what is a ℕ-arithmetic instance of a standard fact.

**Not wrong, just over-tiered.** The conclusion (`N = 2` cannot host the
eightfold decomposition) is true — hook-content and the row cap are textbook.
The scope-(b) discipline is also correctly observed: `schur-weyl:93-94` and
the file's :61-68 both name the invariant, as AGENTS.md requires.

**Suggested fix (content edit, needs sidecar + render-QA):** apply the same
caveat paragraph used for `Sym2Gate`/`WeylInvariance` — e.g. "what is
machine-checked is the arithmetic of the row cap on the `A₂`/`gl_N` channel
dimensions; the hook-content formula supplying `dim V_λ` is standard and
cited, not formalised here." Retier the ledger row from `proved` to
`standard + machine-checked arithmetic instance`.

**Secondary note for whoever picks this up.** `decuplet_forces_three` and
`singlet_forces_three` run in the direction the framework does not need
(observing a decuplet ⇒ `N = 3`); the framework needs `N = 3` *supplied*,
which is the open half the ledger correctly records at row :18. Worth saying
so if the paragraph is rewritten.

---

**Update (2026-08-08, post-commit).** The colour-row Lean cone was rebuilt with
`scripts/lean-direct-cone.sh QOU.MathlibExt.OctonionColourActionBaseModule -k -j4`:
`done: ok=9 in 923s`, `err=0`, `blocked=0`. So the audit's total is **20 Lean
files verified green and sorry-free, zero red** across both chapters' citation
graph. This does not change this bean: `RowCapObstruction.lean` was already
green and sorry-free from the start — the finding was never about compilation,
it is about the tier word "proved" attached to a ℕ-arithmetic instance of a
standard fact while two sibling files get an explicit caveat for the same
construction.
