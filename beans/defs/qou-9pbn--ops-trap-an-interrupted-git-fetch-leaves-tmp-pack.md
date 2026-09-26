---
# qou-9pbn
title: 'OPS TRAP: an interrupted git fetch leaves tmp_pack_* in .git/objects/pack and NOTHING reaps it — 9.4 GB here, and it bricks the session'
status: completed
type: bug
priority: normal
created_at: 2026-09-13T16:32:36Z
updated_at: 2026-09-13T16:33:11Z
---

## MEASURED 2026-09-13, on this container, mid-session

The Bash harness stopped being able to write its own stdout capture:

    the temp filesystem at .../tasks is full (0MB free)

At that point EVERY command fails, including the `df` that would diagnose it and
the `rm` that would fix it. Commands whose output is empty still succeed, which
is the only lever left.

## THE CAUSE, AND IT IS NOT WHAT THE DOCUMENTED ONES SAY

    .git                        13 G
    .git/objects/pack           11 G
    sum of all *.pack files    1.2 G     <- so the packs are NOT the problem
    .git/objects/pack/tmp_pack_tYweVv   7.6 G
    .git/objects/pack/tmp_pack_ZNS0a3   1.8 G

9.4 GB in two abandoned temp packs. `git fetch` streams a pack into
`tmp_pack_<random>` and renames it on success; killed or failed mid-transfer it
leaves the file, and **nothing ever reaps it** -- not `git gc`, not
`git prune`, not a later successful fetch. Deleting both took `/` from 100 %
(2.1 M free) to 76 % (9.3 G free) in one `rm`, with `.git` 13 G -> 3.6 G.

    rm -f .git/objects/pack/tmp_pack_*      # safe when no git process is running

Almost certainly from the `lake-cache/qou-v4-24-0` fetches: that branch is ~1.7 GB
of tarball parts, and AGENTS.md's own recipe fetches it repeatedly.

## WHY THE EXISTING GUIDANCE DOES NOT CATCH IT

AGENTS.md's disk material names two hazards and this is neither:

1. the leaked `/tmp/tmp.*` tarball the cache-restore recipe streams parts into
   (its `trap` fixes that one);
2. "a fetch into .git does NOT reclaim; fetch into a throwaway repo instead".

(2) is about *reachable* objects in *packs*. This is unreachable bytes in a
**temp file that is not a pack at all**, so every instruction that reasons about
packs, refs or gc misses it -- including `du -sh .git/objects/pack` followed by
`ls -S *.pack`, which is what I did first and which reported 1.2 GB against a
directory holding 11 GB. **The 10x discrepancy between the directory total and
the sum of its packs IS the signature.**

## THE DIAGNOSTIC, for whoever hits this next

    du -sh .git/objects/pack
    ls -la .git/objects/pack/ | grep -v -E '\.pack$|\.idx$|\.rev$'

If the second command lists a `tmp_pack_*`, that is the whole of it.

## SECOND-ORDER: A CONCURRENT `lake build` MAKES IT WORSE AND HIDES ITSELF

`scripts/lean-build-bg.sh` re-fires on compaction, and it was running: writing
oleans into the paper mathlib tree while I was measuring, so the free-space
figure moved between commands and `lean-shadow-verify.sh` warned its counts
were "a snapshot of a MOVING target". Kill it by PID before measuring --
`pkill -9 -f "lake build"` matches the pkill's OWN command line and kills the
shell that issued it (exit 1, command truncated mid-way; observed here).

## NOT CLAIMED

That the temp packs came from a specific fetch. Their mtimes were not recorded
before deletion, which was the wrong order to do it in -- the space was needed
to run the command that would have told me. If you hit this again, `ls -la`
first, then delete.
