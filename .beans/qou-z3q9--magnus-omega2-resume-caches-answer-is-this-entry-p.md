---
# qou-z3q9
title: Magnus Omega2 resume caches answer 'is this entry PRESENT?' not 'is it CURRENT?' w.r.t. the PRODUCER SOURCE — triton stamps q0 only, he4 stamps nothing
status: completed
type: bug
priority: high
created_at: 2026-09-08T04:55:42Z
updated_at: 2026-09-12T03:27:06Z
parent: qou-9c80
---

## Measured 2026-09-08

`triton_magnus_omega2_sign_probe.py:244`

    _stamp = hashlib.sha256(f"{Q0}|9".encode()).hexdigest()[:12]

The resume key is q0 and the strand count. It does NOT include the producer's
own source. Four lines above it the file states the intent it fails to meet:

    # STAMPED, not just keyed on the partition. A cache entry records the q it
    # was computed at, and a mismatch DISCARDS rather than silently serving a
    # stale block. That is the qou-5ovu lesson: a gate that answers "is this
    # entry PRESENT?" when the question is "is this entry CURRENT?" is how two
    # witnesses sat at a superseded convention for three weeks.

So the guard exists for a stale *q* and is absent for stale *code*.

`he4_magnus_omega2_sign_sparse_probe.py:516-527` is worse: the `--checkpoint`
resume keys on `rec["lambda"]` alone, with no stamp of any kind — neither q0
nor source.

## How it was found — it nearly manufactured a false verdict

While verifying the far-commutativity port (`qou-5mxd`), the PATCHED triton was
launched and printed

    resumed 14/30 partitions from .triton_magnus_omega2_progress.jsonl

Those 14 rows were computed by the UNPATCHED code in the timed-out baseline run.
The witness would have been a pre/post mixture, and the "is the patched output
identical?" check would have come back identical PARTLY BECAUSE 14 OF 30 ROWS
WERE LITERALLY THE OLD CODE'S OUTPUT. Caught by reading the resume line rather
than by any gate. The run was killed before it banked a mixed row (progress file
verified still at 14 pure-unpatched rows), those rows saved as a genuine partial
baseline, and the patched run restarted from an empty cache.

## Fix

Fold the producer's source hash into the stamp, e.g.

    _src = hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()
    _stamp = hashlib.sha256(f"{Q0}|9|{_src}".encode()).hexdigest()[:12]

and give the he4 checkpoint a stamp at all. Note this makes a comment-only edit
invalidate the cache, which for an expensive producer is a real cost — the
alternative is to hash only the Omega2/germ construction, which is narrower but
fragile. Deliberately NOT applied while a verification run is in flight: editing
the file mid-run would invalidate the rows that run is banking.


## RESOLVED 2026-09-11 (PR #7179, merged `77c88fb60`) — both halves applied

Verified on `main` `5408f53d2`:

**triton** `triton_magnus_omega2_sign_probe.py:257-258` — the producer's own
source hash is now folded into the resume stamp, exactly as the Fix section
above proposed:

    _src_sha = hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()
    _stamp   = hashlib.sha256(f"{Q0}|9|{_src_sha}".encode()).hexdigest()[:12]

**he4** `he4_magnus_omega2_sign_sparse_probe.py:541-578` — the checkpoint had
no stamp of any kind; it now has one, and the discard is on the read path:

    _ck_src   = hashlib.sha256(open(__file__, "rb").read()).hexdigest()
    _ck_stamp = hashlib.sha256(f"{_Q0_RESOLVED}|12|{_ck_src}".encode()).hexdigest()[:12]
    if rec.get("_st") != _ck_stamp:   # line 556 — drop, do not serve
    ckpt_fh.write(json.dumps({**row, "_st": _ck_stamp}) + "\n")   # line 578

So a row written by one source version is dropped rather than served by
another, which is the PRESENT-vs-CURRENT distinction this bean is about.

**The cost named in the Fix section is real and was accepted deliberately.** A
comment-only edit to either producer now invalidates its whole cache. For he4
that is an 8.0 h recompute. The narrower alternative (hash only the
Omega2/germ construction) was rejected as fragile: it needs a human to keep the
hashed region in step with what actually affects the numbers, which is the same
class of assumption that produced this bug.

**The he4 run that followed used the new stamp end to end** — emptied cache,
77/77 partitions, 8.0 h, no resume. So the stamp is not merely present; the
A=4 result was produced under it.

Closing: this is mechanical infrastructure, no open conjecture (AGENTS.md §13a).
