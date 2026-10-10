# Content-sibling `.lean` standalone-compile repair — tranche 2026-07-27

Draining the `cscb` epic backlog: content-block `.lean` siblings
(`folio/quantum-observable-universe/**/*.lean` **outside** the `lean/`
Lake package) that fail to compile standalone. These live outside the
CI-built `lake build QOU` target, so breakage accumulated silently across
many PRs. PR #2964 gates *new* breakage (diff-scoped content-sibling-compile
CI); this epic remediates the existing set (~57% of 929 files at epic open).

## Scope of this tranche

Cluster: **`folio/quantum-observable-universe/braids-and-knots/`** (35
content-sibling `.lean` files). One directory, file-disjoint from sibling
agents, completable in a single session.

## Method (per the `cscb` epic)

1. **Sweep** — `lean <file>` (lean-direct against the restored Mathlib +
   QOU oleans; **not** `lake build` — cache is intact) over every
   content-sibling in the cluster; record PASS / FAIL + first error.
2. **Categorize** each FAIL:
   - `missing-import` / `unknown-decl` — add the needed `import` (e.g.
     `Mathlib.Data.Nat.Factorial.Basic` for `Nat.factorial`).
   - `renamed-import` — module split/moved at the pinned Mathlib rev
     (e.g. `Mathlib.LinearAlgebra.Dimension` → `.Dimension.Finrank`;
     `Mathlib.Tactic.Omega` removed — `omega` is core).
   - `orphaned-body` / `syntax` — a prior head-only comment-out left a live
     proof body / stacked docstring; restore or fence.
   - `needs-noncomputable` — IR check failed (e.g. `LaurentPolynomial.T`);
     mark `noncomputable`.
   - `proof`/`type-error` — genuine unsolved goal / mismatch.
3. **Fix + verify** — apply the fix, re-run `lean <file>` to **exit 0**
   before committing. One commit per file (or per tight category cluster).
4. **Anti-laundering** — never `head`-comment-out a live proof or swap a
   real statement for `True` to force a pass; a genuine `proof`/`type-error`
   gets a real fix or an honest `sorry` + `-- Ref:` (per AGENTS.md §1),
   never a vacuity dodge.

## Status

- [ ] Sweep `braids-and-knots` → categorized FAIL list
- [ ] Fix cluster, one commit per file, each verified `lean` exit 0
- [ ] Re-sweep to confirm 0 FAIL in the cluster
