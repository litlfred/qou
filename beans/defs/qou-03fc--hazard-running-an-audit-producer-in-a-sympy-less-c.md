---
# qou-03fc
title: 'HAZARD: running an audit producer in a sympy-less container silently DEGRADES its witness (two q0 witnesses are also genuinely stale on main)'
status: in-progress
type: bug
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-16T12:39:42Z
updated_at: 2026-10-04T15:15:43Z
parent: qou-5vkl
---

Found while running `scripts/precision-gates.sh --changed` as the pre-commit
preflight on PR #5205, whose diff touched only a `.lean` and `docs/audits/`.

## Two separate things, and they pull in opposite directions

**1. Two committed witnesses ARE genuinely stale on main.** Regenerating moved
real counts, not just metadata:

| witness | count that moved |
|---|---|
| `computations/q0-value-drift-audit.witness.json` | `proton-pin` **796 -> 797** (new entry: `computations/qbeta/qbeta-decay-channel-convention-status.witness.json`, a recent main landing) |
| `computations/audits/q0-anchor-consistency-audit.witness.json` | `Q0_OK` **650 -> 651**, `Q0_AMBIGUOUS` **16 -> 15** (`binding-alpha-shift-witness.witness.json` reclassified) |

By the gate's own instruction ("if a COUNT moved, the committed witness was
stale: commit the regenerated one and say which count changed") these should be
refreshed.

**2. But I could not refresh them honestly, because this container has no
sympy.** The regenerated `q0-anchor-consistency-audit.witness.json` **drops the
`"sympy": "1.14.0"` environment entry entirely** — no replacement value, the key
just disappears. Committing that would record my container's missing dependency
as a fact about the computation. That is the same failure class as widening a
baseline to make a red run green: it makes the gate pass by degrading the
evidence rather than by fixing anything.

**So I reverted both files and shipped neither.** Recording rather than
half-fixing.

## Why this is a hazard and not just a chore

The degradation is **silent and asymmetric**. The producer does not fail, warn,
or exit non-zero when sympy is absent — it emits a witness that is *correct in
its numbers* and *wrong in its provenance*, and the missing key is a deletion,
which reads in a diff as tidying rather than as loss. An agent that runs a
precision gate as a preflight, sees "modified witnesses", and follows the gate's
own advice to commit them will land the degradation without noticing.

Two aggravating factors:

- **`precision-gates.sh --changed` regenerated these even though nothing
  precision-relevant was in my diff** (a `.lean` file and two `docs/audits/`
  files). Whatever selects producers to re-run is over-broad, so the hazard
  fires on PRs that never touch `computations/`.
- **The gate reported RED after mutating the tree**, so the RED was partly about
  files its own run had just changed. A preflight that dirties the working tree
  and then grades it is hard to act on correctly.

## What to do

1. **Make the producer refuse rather than degrade.** If an environment key
   cannot be determined, exit non-zero (or write an explicit
   `"sympy": "unavailable"`) instead of dropping the key. A missing dependency
   should never be expressible as a silent deletion.
2. **Refresh the two witnesses from a container that has sympy**, and say which
   counts moved (they are recorded above, so the refresher can check the numbers
   still match rather than trusting a fresh run blind).
3. **Narrow `--changed`** so it does not re-run `computations/` producers for a
   diff that contains no `computations/` or witness file.
4. Consider whether other producers drop environment keys the same way — this
   was found by eye in a diff, not by any checker.


---

## CORRECTION (2026-08-16, same day) — I blamed the wrong thing, twice

Re-ran `precision-gates.sh --changed` after rebasing onto main. It **skipped
cleanly** — *"no witness or computations/ script touched"* — on a diff of the
same shape that had triggered the full run before. That contradiction sent me
back to the script, and both of my claims above are wrong.

### 1. `--changed` is NOT over-broad. Recommendation 3 above is refuted.

The short-circuit reads the **working tree only**:

```sh
relevant=$( { git diff --name-only HEAD;  git diff --cached --name-only
              git ls-files --others --exclude-standard; } \
            | sort -u | grep -E '(\.witness\.json$|^computations/.*\.py$)' )
```

No base, no `origin/main`, no merge-base. It cannot pick up upstream's changes,
so "it re-runs `computations/` producers for a diff that contains none" was a
mis-read. **Do not go narrow `--changed`** — it is already correctly scoped.

### 2. The real trigger was my own audit probe's witness.

The pattern is `(\.witness\.json$|^computations/.*\.py$)`. The `.py` half is
anchored to `computations/`; **the witness half is not anchored at all.** So
`docs/audits/scripts/curvature_rank_vs_gbdepth_dimension_count.witness.json` —
an audit-probe output I had just written, nowhere near `computations/` —
matched, passed the short-circuit, and the gates ran corpus-wide. That run then
executed the q0 audits (`precision-gates.sh` is the **only** file in the repo
that invokes them) and rewrote the two witnesses.

So the causal chain was: *my* untracked probe witness → short-circuit passes →
corpus-wide gates → q0 audits regenerate → sympy key dropped.

### What survives, and what to actually fix

**The hazard in the title stands, and it is the part worth keeping**: running an
audit producer in a sympy-less container silently drops the `"sympy": "1.14.0"`
environment key — a missing dependency expressible as a key *deletion*, which
reads in a diff as tidying. Recommendation 1 (make the producer refuse or write
`"sympy": "unavailable"` rather than drop the key) is unaffected and is the real
fix.

**Recommendation 2 stands**: the two witnesses are genuinely stale on main
(counts recorded above), and want a refresh from a container that has sympy.

**Recommendation 3 is withdrawn.** If anything is worth changing in the
short-circuit it is anchoring the witness half — `^computations/.*\.witness\.json$`
— so that audit-probe outputs under `docs/` stop triggering a corpus-wide gate
run. That is a papercut, not the bug I described, and it is arguably correct as
written if the intent is to catch witnesses wherever they live.


---

## 2026-09-05 — recommendation 1 CONFIRMED on a live instance, and it is one of the two witnesses this bean already names. STILL OPEN.

Not a closure: the fix is not made. This is the evidence that says it should be.

### The hazard is realised on `main`, not hypothetical

Measured over the 40 witnesses with ≥2 commits inside the last 400 commits
touching `computations/`:

    regenerations that DROPPED an environment key : 1
    regenerations that GAINED one                 : 2

The one drop is **`computations/q0-anchor-consistency-audit.witness.json` at
`c415d81fe7a`, which lost `clarabel`** — a q0 audit witness, i.e. the same
family this bean was opened on, losing a different key by the same mechanism.
So the class is not sympy-specific and not a one-off.

### The corpus-wide shape

Over the 3573 tracked witnesses on `origin/main`, **2254 carry an
`environment` dict** and their key sets are strikingly heterogeneous:

    1313  clarabel, mpmath, numpy, pyhecke_native, pyhecke_native_build, scipy, sympy
     198  mpmath, numpy, pyhecke_native, scipy, sympy
     148  mpmath, numpy, scipy, sympy
     114  mpmath, numpy, sympy
      96  clarabel, mpmath, numpy, pyhecke_native, scipy, sympy
      92  mpmath, sympy
      ...

Under the current contract (`capture_environment`: *"missing packages are
simply omitted"*, `witness.py:643-655`) **a short key set is unreadable**: it
could mean the package was absent, or that the producer predates the key. The
absence carries no information, which is the defect.

**🛑 I cannot separate those two causes from the record, and my first attempt
to was wrong.** `git log -S` on each package name returns `b831ff34c3d` for all
six, which reads as "the list was unified in one commit" — but that is a
**merge** commit and `git show b831ff34c3d^:…` finds no `for pkg in` line at
all, so the `-S` result is not evidence about when the list grew. Do not repeat
the "list-growth confound is ruled out" claim; it is not.

What *is* measurable and does not depend on that: **7 witnesses written on or
after 2026-08-29 carry `sympy` but not `numpy`**, three of them dated
2026-09-04 — `mu-p-cyclotomic-ladder-magnitude`, `mu-p-habiro-basis-order`,
`mu-p-sigma235-ohtsuki-resolution`, all carrying `pyhecke_native` and
`pyhecke_native_build` (so a well-provisioned container in that respect) with
no numpy and no scipy. Those ran somewhere numpy was not installed, and nothing
in the record says so.

### What this does NOT settle — the decision is the owner's

Recommendation 1 is *"make the producer refuse, or write `"sympy":
"unavailable"` rather than drop the key"*. The second half is a **one-function
change at `capture_environment`** — the single point every witness's
`environment` block passes through — but its blast radius is **2254 witnesses**:
each gains up to 6 `"unavailable"` keys on its next regeneration, and a witness
regenerated in a lean container would then differ from a full-container one in a
newly-recorded way. That is the intended behaviour, and it is also a contract
change on every witness in the corpus.

The **refuse** half should not be taken: a bare container is the default here
(`mpmath`/`numpy`/`scipy` are routinely absent on a fresh clone), so a producer
that refuses on a missing package would brick compute in exactly the
environments the owner declined to block on 2026-08-25.

Recommendation 2 (refresh the two genuinely-stale q0 witnesses from a
sympy-having container) is unchanged and independent of the above.

- **Round 91 (`https://github.com/litlfred/qou/pull/8413`, head `1d95d75db1b41a96e3b4987d5771f9fd945187c9`)**: Formalized theorem + 80-dps witness (`status: in-progress`).
