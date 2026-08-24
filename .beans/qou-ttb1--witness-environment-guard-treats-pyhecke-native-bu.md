---
# qou-ttb1
title: witness environment guard treats pyhecke_native_build as ORDERED, but a .so content hash is not
status: todo
type: task
priority: normal
created_at: 2026-08-24T20:06:56Z
updated_at: 2026-08-24T20:07:32Z
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
