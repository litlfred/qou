---
# qou-zqfj
title: lake-cache.sh seed --push cannot complete for the qou package
status: completed
type: bug
priority: high
created_at: 2026-08-30T18:55:29Z
updated_at: 2026-08-31T03:03:20Z
---

Measured 2026-08-30 while reseeding `lake-cache/qou-v4-24-0`. The service script works for small
packages and CANNOT complete for the largest one -- which is the one whose cache matters. Two
independent limits, both size-dependent, neither reported as a size problem.

1. DISK. `cmd_seed` materialises the parts three times: split output in $TMP, a `git worktree add`
   checkout, `cp` of the parts into it, then `git add` into the object store. For qou that is

       parts(2.3G) + worktree(1.3G) + cp(2.3G) + objects(2.3G) ~= 7.9G

   against 7.3G free in a standard session container. It dies on ENOSPC partway.

2. PUSH SIZE. Even with the parts built, `git push` of the 2.34 GB pack gets HTTP 500 from GitHub.
   NOT a proxy abort -- `$HTTPS_PROXY/__agentproxy/status` logged ZERO github relay failures while
   it happened. A 450 MB push to the same repo succeeds, so the limit is real and size-dependent.

3. AND THE RETRY LOOP MISREADS IT. `push_retry` treats HTTP 500 as transient and burns four attempts
   over ~10 minutes on a payload the far end will never accept.

WHAT WORKS -- and it is the same artefact, byte for byte:

  * Build with `split --filter='git hash-object -w --stdin'` so no part is ever a file. Peak becomes
    objects(2.3G) + one chunk(90M) ~= 2.3G. Measured: disk 7.3G -> 5.0G, exactly as predicted.
  * Push the blobs in ~450 MB batches to a STAGING ref as a commit chain, then move the real branch.
    Staging is not optional: pushing the growing chain straight at the cache branch leaves it with an
    incomplete part set between batches, and a concurrent restore then assembles a truncated tarball
    (`gzip: not in gzip format`), indistinguishable from corruption.
  * THE FINAL COMMIT MUST BE A CHILD OF THE STAGED TIP, not an orphan. Pushed as an orphan it has no
    advertised ancestor to negotiate against, so git re-sends all 2.34 GB and 500s again -- that cost
    me four more retries and a 10-minute timeout. As a fast-forward it is one ~200-byte commit
    object and lands instantly.
  * Parents are safe: `cmd_restore` fetches --depth=1, so a consumer never sees the chain.

Working script kept at the session scratchpad; it should be folded into lake-cache.sh as the
default path, since the three-copy approach has no advantage.

LEFTOVER: `lake-cache/staging-test` still exists on origin -- ref deletes were also hitting
disconnects. Harmless (it is the parent of the published commit, hence reachable anyway) but it
shows up in `lake-cache.sh list` and should be pruned.

## Summary of Changes -- and a CORRECTION to this bean's own claim

PARTLY FIXED, and this bean was PARTLY WRONG.

WRONG: item 2 said `seed --push` sends the whole 2.34 GB in one push. That has been FALSE ON MAIN
since 428ca5c (2026-08-23), "batch seed push under GitHub's 2 GiB pack limit", which added
LAKE_CACHE_SEED_BATCH (15 parts ~ 1.35 GiB per push). I hit the single-push failure only because
this session's folio-assistant checkout was pinned at b987547374, which PREDATES that fix. I
rediscovered a solved problem and filed it as current. Checked with `git log -S` before writing
this, which is what I should have done before filing.

RIGHT, and now fixed: the DISK triple-copy. The --push loop `cp`s each part from $tmp into the
worktree, so the tarball is on disk twice for the whole loop, plus the worktree checkout, plus the
objects. Measured: 2.34 + 1.3 + 2.34 + 2.34 ~= 8.2 GB peak against 7.3 GB free. Changed to `mv`
(folio-assistant PR #159): peak ~6.0 GB, which fits. Dry path untouched.

NOT TAKEN: streaming via `split --filter='git hash-object -w --stdin'` (~2.3 GB peak, verified
end-to-end against this cache). Larger change to a CI-critical path I cannot exercise from here;
recorded in the comment and pointing at scripts/lake-cache-stage-push.sh.

SEPARATE DEFECT I INTRODUCED AND FIXED: I published the cache with subject
"(6172 oleans, 2443 own, 99% traced)". `branch_counts` parses `(<n> oleans, <m> own)` with `own)`
closing the paren, so the trailing text made it return EMPTY -- and `would_shrink` treats an
unparseable subject as "no recorded counts", i.e. IT SILENTLY DISABLES THE ANTI-SHRINK GUARD. Any
later partial seed could then have replaced a complete cache unchallenged. Corrected on
lake-cache/qou-v4-24-0 (now a2bf415e7a); the guard reads 6172/2443 off the live branch again.

The commit subject is a PARSED INTERFACE and nothing at the point of writing says so.
