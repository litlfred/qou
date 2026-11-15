---
# qou-ttb1
title: witness environment guard treats pyhecke_native_build as ORDERED, but a .so content hash is not
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-24T20:06:56Z
updated_at: 2026-11-15T13:40:00Z
parent: qou-5vkl
---

OBSERVED 2026-08-24 on branch claude/excise-convention-c-2026-08-24.

qou_substrate.witness._pyhecke_native_build_hash() is a sha256 prefix of the
compiled .so. WitnessBuilder's environment guard compares it like a VERSION —
a change is reported as a downgrade and the on-disk value is kept:

  ⚠ environment: q0-anchor-consistency-audit.witness.json: this container would
    record LESS than the witness on disk — downgraded pyhecke_native_build
    909e02527c90e773 -> b843d058d29dcec6. The file was NOT modified and its
    stronger environment block was kept.

But a content hash of a build artifact is NOT ordered. Neither value is
'stronger'; they are different builds. The guard's advice ('install the missing
libraries') does not apply — pyhecke_native 0.9.0 is installed either way.

Measured here, the guard preserved the WRONG one. b843d058d29dcec6 is this
container's actual and original build (live: one .so at
/root/.local/lib/python3.11/site-packages/pyhecke_native/, hashing to b843).
909e02527c90e773 was TRANSIENT — it appeared mid-session during a pip install
and vanished when the container restarted. So two audit witnesses
(q0-anchor-consistency, witness-provenance) are pinned to a build hash that no
longer exists anywhere, and re-running them cannot fix it: the guard refuses
the write. The other two audits carry no environment block and are unaffected.

Not fixed here: the guard is shared infrastructure that every producer writes
through, and changing its comparison semantics is not in scope for a
convention-C branch. Recording so the next agent does not repeat my mistake of
filing 'regenerate these' as a to-do — the regeneration is a no-op by design.

Suggested shape if picked up: compare version-like fields (mpmath, numpy,
python) by ordering as now, but treat hash-like fields (pyhecke_native_build) as
INCOMPARABLE — prefer the current container's value, or record both, rather than
pinning whichever container wrote first.

DUPLICATE — a sibling found this first and diagnosed it better. Corrected 2026-08-24.

PR #5683 (branch claude/stalled-agent-prs-ir8t3p, bean qou-orb6) already carries
the diagnosis AND the fix. Their account, which is more precise than mine:

  pyhecke_native_build is sha256(.so)[:16] ordered by _version_tuple, so
  _version_tuple('30fd920c…')==(30,) vs _version_tuple('b843d058…')==() makes
  ()<(30,) a false 'DOWNGRADE', and a false downgrade sends save() down the
  preserve path and stamps a build hash the container does not have; six
  distinct values exist in the corpus because a Rust release build is not
  byte-reproducible.

I wrote 'a content hash is not ordered', which is true but stops short. The
actual mechanism is that _version_tuple PARSES the hex: a hash whose leading
characters are digits yields a tuple, one starting with a letter yields (), and
() compares less than anything. Verified independently on this branch:

    909e02527c90e773 -> (909,)
    b843d058d29dcec6 -> ()
    30fd920c241a54fa -> (30,)
    () < (909,)      -> True

So it is not merely unordered — it is ordered WRONGLY and asymmetrically, and
which of two builds 'wins' depends on nothing but whether its hash happens to
start with a digit. That also explains why my case preserved the transient
value: 909… leads with digits, b843… does not.

Two facts of theirs I did not have: SIX distinct values exist corpus-wide, and
the reason is that a Rust release build is not byte-reproducible — so this is
not container drift, it is expected churn the guard mishandles.

Their fix is a _NON_ORDINAL_ENV_KEYS guard, i.e. exactly the 'treat hash-like
fields as incomparable' shape I suggested, already implemented and gate-green.
PR #5683 is blocked on a GitHub rate limit, not on review.

ACTION: do not fix this here. My contribution is an independent confirmation
from a different route (I hit it as an anomalous preserved build hash on
convention-C work; they hit it auditing witness provenance). Two independent
observations of the same defect strengthen it. Close this as duplicate when
#5683 merges.

## Closed 2026-11-15 (owner tap, E1 bean triage)

Its own instruction was "close as duplicate when #5683 merges". #5683 merged on 2026-08-24.
