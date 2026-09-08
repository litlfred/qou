---
# qou-z3q9
title: Magnus Omega2 resume caches answer 'is this entry PRESENT?' not 'is it CURRENT?' w.r.t. the PRODUCER SOURCE — triton stamps q0 only, he4 stamps nothing
status: todo
type: bug
priority: high
created_at: 2026-09-08T04:55:42Z
updated_at: 2026-09-08T04:55:43Z
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
