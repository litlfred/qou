# Stalled-PR wrap-up — verification pass on #4905, #4600, #4584, #4913, #4935

**Date:** 2026-08-10
**Branch:** `claude/stalled-prs-wrap-up-uja5th`
**Beans:** `qou-qm7f` (session), touching `qou-0hu2`, `qou-dr1c`, `qou-x64l`

This runs the gate that the sweep in #4905 named but explicitly did not run.
Its `qou-0hu2` disposition for #4600 ends *"NOT COMPILED … lean-direct pass is
the gate before landing."* That pass is done here, along with the equivalent
gate for each of the other four PRs.

**Outcome: all five merged to `main`** on the owner's explicit go-ahead, after
the gates below. Rebase-merge throughout, per the default in AGENTS.md rule 8.

| PR | merge sha |
|---|---|
| #4935 | `265b24f3` |
| #4905 | `66faf81b` |
| #4913 | `0c11a233` |
| #4584 | `52710702` |
| #4600 | `200ef38a` |

Two branch-side fixes to #4600 were pushed with the owner's approval before it
merged: the conflict resolution below, and the `qou-mpq5` fold-in. #4600 and
#4584 were also undrafted.

## Method note — the shallow clone lies about conflicts

`git merge-tree` against a shallow clone reports **CONFLICT for every branch**,
because no merge base resolves. That is an artifact, not a finding. Deepening to
1500 makes the merge bases resolve, after which four of the five merge clean and
the fifth has a single conflicting file. GitHub's own `mergeable_state` agrees
and is the cheaper authority.

This is a fourth entry for the sweep's method table in #4905: *shallow-clone
merge-tree ⇒ conflict* is unsound in the same family as the three line- and
path-counting proxies it already retired.

## Results

| PR | draft | mergeable | gate run | outcome |
|---|---|---|---|---|
| **#4905** | no | clean | none applicable — beans-only diff | ready |
| **#4913** | no | clean | `lean`-direct ×2 | **1 of 2 files unverifiable here** — see below |
| **#4935** | no | clean | independent re-check of its inherited-red claim | ready, claim confirmed |
| **#4584** | **yes** | clean | `lean`-direct + `#print axioms` + render-QA | ready — undraft |
| **#4600** | **yes** | **dirty** | `lean`-direct ×7 + render-QA ×2 | ready — conflict resolved locally, undraft |

Verification environment: toolchain v4.24.0, oleans restored from
`lake-cache/qou-v4-24-0-new` (2962 Mathlib + 870 QOU), `lean`-direct with
`LEAN_PATH` set to the restored `build/lib/lean` dirs. No `lake build`, no
`cache get`. CI is not cited — Actions auto-triggers are disabled repo-wide
(owner directive 2026-06-30), so this pass *is* the gate per AGENTS.md
§"QA is agent-owned".

### #4600 — seven modules, all check

| module | `lean`-direct | tactic `sorry` |
|---|---|---|
| `QuantumObservableUniverses/QBetaEnergyDictionary.lean` | exit 0 | 0 |
| `QuantumObservableUniverses/QExpEntire.lean` | exit 0 | 0 |
| `QuantumObservableUniverses/QSchurWeyl.lean` | exit 0 | 0 |
| `QuantumObservableUniverses/VirtualProjection.lean` | exit 0 | 0 |
| `SchurWeyl/YoungTableaux.lean` | exit 0 | 0 |
| `SchurWeyl/HeckeAlgebra.lean` | exit 0 | 0 |
| `SchurWeyl/HoefsmitRep.lean` | exit 0 | **1** |

`HoefsmitRep` needs `YoungTableaux.olean` and `HeckeAlgebra.olean` built first —
they are new on the branch, so the naive per-file pass fails on it with a
missing-object-file error that is *not* a defect. Build the two siblings with
`-o` first and it checks.

The one `sorry` is the honest state-and-queue disposition, not a placeholder: it
carries `-- Ref: [hoefsmit1974]` and `[ram1997]` (both keys resolve in
`content/schema/references.ts`) plus a six-line `GAP:` note naming the unproved
step — the braid relation for arbitrary `λ`, i.e. Hoefsmit's theorem — and
routing the residual to beans SW-4 and SW-5. **0** trivial-`True`, **0**
`native_decide` across all seven.

Render-QA grep battery on both new math-bearing `.md` blocks
(`beta-eq-ln-q-dictionary.md`, `q-exp-entire.md`): balanced `$`/`$$`/`{}`, no
`\operatorname`, no list-parser hijack inside `$$`, no align-family inline.
Clean. The pipeline render was **not** run — `folio-assistant/` is not set up in
this sandbox — so per the render-QA gate this is a hand-validated result, not a
machine-validated one.

**The merge conflict is one bean file.** `mergeable_state: dirty` resolves to a
single front-matter collision in
`.beans/qou-ahbp--lit-follow-up-fetch-read-arxiv-180609450-todorov-d.md`:
branch has `updated_at: 2026-08-02` + `parent: qou-a0gr`, `main` has
`updated_at: 2026-08-01` and no parent. The branch side is a strict superset;
resolved to it. `QOU.lean` and `quantum-observable-universes.ts` auto-merge.

### #4584 — verifies, and is merely undrafted

`complex-mass-constituent-functional.lean`: `lean`-direct **exit 0** (63 s), 0
`sorry`, and `#print axioms QOU.MassTheory.charm_block_determined` →
`[propext, Classical.choice, Quot.sound]`. Merges clean against current `main`
despite being eight days old. Nothing about it is stalled except its draft flag.

The scaffold is honest on its own terms: `ComplexMassConstituent` is a
content-bearing primary conjecture class with two parameter-quantified fields
and **no instance exhibited**, which is the correct representation of an open
primary per §3b-tax.

### #4913 — one file I could not re-verify

`IdempotentBaseChange.lean` re-verifies here: **exit 0**, 0 `sorry`.

`EndBaseChange.lean` **could not be re-verified in this sandbox.** The restored
cache is missing `Mathlib/Algebra/Module/LinearMap/Polynomial.olean`, which the
file imports directly. I checked whether the import was gratuitous by deleting
it — it is not: the file genuinely needs `Algebra.TensorProduct.basis` and
`LinearMap.toMatrix_baseChange` from that module, and without it the proof
leaves unsolved goals. Mathlib *sources* are not in the cache either, so the
module cannot be built locally.

So #4913's `EndBaseChange` rests on its own session's reported `lean`-direct
exit 0 and clean `#print axioms`, which I have **not** independently confirmed.
Stating that rather than implying a full re-verification.

### #4935 — the inherited-red claim holds

Independently confirmed: both witnesses that `precision-gates.sh --changed`
reports red — `kappa-shell8-excess-convention.witness.json` and
`a-K-via-lp-dual-full.witness.json` — are **byte-identical to `origin/main`**
and are not touched by the branch, whose diff is four bean files plus
`computations/probes/canonical-ordering-dof.witness.json`. The red is inherited
from `main`, and it is live on `main` now. Correctly beaned (`qou-mnrd`) rather
than baselined away.

## Two defects found

**1. #4600 carries a duplicate `qou-mpq5` bean.** Two files claim bean ID
`qou-mpq5`. The 3475-byte one is the real bean. The 593-byte one has a
mojibake-corrupted filename (`…dim-v-\udcce.md` where the real one ends
`…dim-v-�.md`), **no front-matter at all**, and a body that is plainly the
*continuation* of the real bean — the `## 🔥 Scope assessment (2026-08-02) — R2
is a genuine Mathlib GAP` section recording that Mathlib has no Schur–Weyl
duality, classical or quantum.

So the scope assessment is orphaned in a headerless file that no `beans`
command will surface, and the finding it records — a genuine Mathlib gap,
established by scanning all 6990 modules — is exactly the kind of negative that
must not get lost. Fix: append the fragment's body to the real bean, delete the
fragment. Not applied here; it is a change to #4600's branch.

**2. The `lake-cache/qou-v4-24-0-new` olean set is incomplete.** It is missing
at least `Mathlib/Algebra/Module/LinearMap/Polynomial.olean`, which is what
blocks #4913 above. Any agent restoring from that branch and hitting a
`does not exist` error on a Mathlib module should read it as a cache gap, not
as a broken import in the file under test — and should not conclude the file
fails to compile.

`beans check` reports 13 issues, all broken `parent:` links (`0yqu`, `krvm`).
Those beans are on `main`; the condition is pre-existing and not introduced by
any of the five PRs, and the count was unchanged by the `qou-mpq5` fold-in.

## #4600 could not be rebase-merged as it stood

GitHub rejected `merge_method: "rebase"` with **405 "This branch can't be
rebased"** — the branch carried a merge commit (the `main` merge that resolved
the `qou-ahbp` conflict).

Rule 8's documented exception would have allowed a merge commit here, but
linearizing is the better outcome and turned out to be cheap: rebasing the 17
commits onto `main` drops the merge commit, keeps every per-commit boundary
that rule 4 asks for, and leaves nothing for a reader to navigate around. The
`qou-ahbp` conflict resurfaced once during the replay and was resolved the same
way. Re-verified after the rebase — `YoungTableaux`, `HeckeAlgebra`,
`HoefsmitRep` and `QSchurWeyl` all still exit 0, no conflict markers anywhere,
zero merge commits remaining — then force-pushed with `--force-with-lease` and
rebase-merged.

Worth knowing before the next stalled PR: **resolving a conflict by merging
`main` into a branch makes that branch un-rebase-mergeable.** Rebasing the
branch onto `main` instead resolves the same conflict and keeps the default
merge method available.

## What remains open, honestly

- **`qou-0hu2`** — its named next step for #4600 is now discharged. The rest of
  the sweep's PR list is still undispositioned, and the method constraint it
  records still holds: there is no cheap screen, each PR needs its novel files
  read.
- **`qou-dr1c`** — item 1 remains open. #4913 removes two rungs and re-scopes
  it; it does not close it. The two immediately-remaining pieces are named in
  the bean and in the PR.
- **`qou-x64l`** — step 4's Lean wiring remains. The Markov weights are
  identified in closed form and cross-checked; what is missing is feeding the
  five `ρ_λ` and `hdecomp` to `gram_symm_of_rep_decomp`. The bean's cost warning
  stands and is now doubly relevant: the H4 cone is **absent** from
  `lake-cache/qou-v4-24-0-new`, so that work starts with a from-source build
  measured at >25 min per block-map file at ~6 GB RSS.

None of these three is closeable by this session, and none is claimed closed.
