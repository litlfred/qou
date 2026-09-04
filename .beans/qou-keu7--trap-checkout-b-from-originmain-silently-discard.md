
## Guarded 2026-09-04 — the detection is now a hook, not a paragraph

This bean recorded a sharp detection rule and nothing ran it. That is the same
finding [`precommit-bean-id-warn.sh`](../scripts/precommit-bean-id-warn.sh)
states one directory over about `check-beans.sh`: **a gate nobody invokes is
documentation.** Six PreToolUse warn hooks now exist; this is the sixth.

[`scripts/prebranch-bean-loss-warn.sh`](../scripts/prebranch-bean-loss-warn.sh)
fires on a branch-creation tool call that names an explicit base, and prints the
beans that would vanish, the beans that would revert, and the recovery command
with the current sha already filled in.

### Two design choices worth keeping

**It matches `-b` as well as `-B`.** This bean names `checkout -B`, but `-B` is
not what does the damage — *moving the worktree to a commit lacking files HEAD
has* is. Plain `git checkout -b <new> origin/main` from a branch carrying
unmerged beans loses them identically, and that is the far more common shape in
practice: this session alone created five branches that way. A branch created
with **no** explicit base cannot lose anything and is ignored.

**It reports ADDED and MODIFIED separately.** An added bean *vanishes*; a
modified one silently *reverts to the base's version*, which is the subtler half
and is exactly what happened to `qou-jr5r` — main kept the stale `todo` body
while the retraction sat unmerged. A guard that only counted deletions would
have missed it.

### Verified four ways

- `--selftest` builds a throwaway repo and asserts all four behaviours: added
  bean reported, modified bean reported as a revert, silent on a branch with no
  bean delta, silent (not erroring) on an unknown base ref.
- Argument parsing checked on five realistic command strings, including the two
  that must **not** fire (`checkout -b` with no base, `git commit`).
- Fired against a real branch of this session and correctly named the single
  bean that would vanish, with the recovery sha.
- Silent on a control branch carrying no bean delta.

### It demonstrated the trap on itself

While testing, checking out another branch to reach a bean-carrying HEAD
**removed the guard script from the worktree** — it was committed on its own
branch and absent from the target — so the real-world case had to be re-run from
a copy outside the repo. Exactly the mechanism this bean documents, met while
building the thing that warns about it.

### What it does NOT do

It warns; it never blocks (always exits 0), per the posture the owner chose for
the precision hook on 2026-08-25 — warn-on-commit, push-side block offered and
declined. Do not upgrade it without asking. And it covers `.beans/` only:
**any** tracked file committed on an unmerged branch is lost the same way by the
same checkout. Beans are singled out because they are the case that has actually
cost this repo, and because a lost bean is silent in a way lost code is not — a
missing source file breaks a build.

### Follow-up the same session — the first matcher had a false positive

Re-reading the guard's own diff adversarially turned up a defect in it. The
matcher was a **substring** test, so a command that merely *quotes* the
invocation fired it. Measured:

    git commit -m 'docs: explains git checkout -b claude/foo origin/main and why'
    -> WARNED

and the commit documenting this very guard is exactly such a message. **A guard
that cries on the commit describing it is noise, and noise is what gets guards
ignored** — which would have reproduced this bean's own root failure (a check
that exists and is not heeded) by a different route.

Fixed by matching at a **command position**: split the string on separators
(`;`, `&&`, `||`, `|`, backtick, `$(`) and require the fragment to *begin* with
`git checkout|switch`. A quoted mention sits mid-fragment and is skipped. A base
ref that does not resolve now exits early too, so a prose placeholder like
`origin/<default>` cannot reach the git layer.

**The matcher is now covered by `--selftest`**, which previously exercised only
the diff logic. Nine rows: four true positives (`-b`, `-B`, `switch -C`, and a
compound `git fetch … && git checkout -b …`) and five that must stay silent
(no explicit base; the quoted-in-a-commit-message case; a `grep` for the string;
an `echo` of it; a plain `git commit`). A new class whose selftest does not cover
it is the trap this session kept finding elsewhere.

### Clarification: git DOES protect uncommitted work

While testing, `git checkout` **refused** to switch branches because the guard
script had uncommitted edits. That is the boundary of this trap and is worth
stating plainly: git blocks a checkout that would overwrite *uncommitted*
changes. The silent loss happens only for work that is **committed on the branch
and absent from the target** — which is why it is invisible, and why `git status`
is clean afterwards.
