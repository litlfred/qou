# Triton far-commutativity port — interim verification (8/14 partitions)

Beans `qou-5mxd` (the port), `qou-z3q9` (the resume-cache bug found doing it).

## Status: PARTIALLY VERIFIED, and by a stronger test than was planned

The plan was witness equality against the committed run. What is being used
instead is a **direct per-partition comparison at H₉, both sides computed this
session**, which is stronger: it compares the same partitions under the two code
versions rather than comparing an output against a file of unknown vintage.

Measured 2026-09-08, patched run still in flight:

```
unpatched rows 14, patched rows 8, overlapping 8
fields compared: dim, y_lambda, tr_rho_Omega2, tr_Omega2_ctrl
VERDICT: all overlapping partitions IDENTICAL
control (perturbed row): caught — comparison is live
```

The control matters: the same script re-run against a deliberately perturbed copy
of one row reports the difference, so "IDENTICAL" is a result and not a broken
comparator. That check exists because an earlier verification in this same arc
returned a false IDENTICAL — it invoked `/usr/bin/time`, absent in this
container, so the probe never ran and the committed file was compared to itself.

## Where the two sides come from

- **unpatched (14 rows)** — the baseline run of the pre-patch producer, which hit
  its 1800 s timeout and never wrote a witness, but had banked 14 partitions to
  `.triton_magnus_omega2_progress.jsonl`. Saved before anything else touched it.
- **patched (growing)** — a fresh run of the patched producer from an **empty**
  cache.

The emptied cache is load-bearing. The patched producer, launched over the
existing progress file, printed `resumed 14/30 partitions` and would have served
the unpatched rows as its own output — see `qou-z3q9`. Any comparison built on
that run would have been circular.

## What is NOT established

- The remaining 6 of 14, and the 16 partitions no baseline exists for.
- **Any speedup.** Not measured at H₉, and the deuteron measurement found none at
  all at H₆ (BEFORE 1367/1264/1291 ms vs AFTER 1212/1339/1166 ms, overlapping).
  Whether the larger H₉ dims change that is exactly the open question; do not
  assume they do.
- The final witness comparison, which needs the run to reach 30/30.
