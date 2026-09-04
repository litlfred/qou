# lean-verifier — cache restore: shortcuts and hazards

Companion to `MEMORY.md`'s restore section. Everything here was measured;
re-measure before quoting a number.

## STABLE — before fetching 1.6G, check whether a LEAKED tarball already is it

The leak below has an upside. Measured 2026-09-04 on `/tmp/tmp.1qCCxhNguJ`
(dated 2026-08-16): `tar tzf` listed **11 786** entries, `tar xzf -C "$ROOT"`
succeeded, the tree went to 9721 oleans with `Mathlib.Tactic` present — the whole
fetch saved. Take two numbers first, because 5.14 GB does not always fit:
`gzip -dc "$f" | wc -c` (~2 min, no disk) and `df -h /`. Net growth that day was
only ~400 MB because most entries already existed; budget for the full figure.
Then **still reap it** — the trap below is unchanged.

**And the restore itself has a concurrency hazard:** the parts are resolved
through the global `FETCH_HEAD`, so a second `git fetch` (a background job, a
parallel agent) repoints it mid-loop, the assembled tarball is truncated, and
`tar` fails looking exactly like a corrupt cache (cost a session 2026-06-22).
Run it serially, or fetch into a private ref
(`git fetch --depth=1 origin "$BR:refs/restore-tmp"`) and read from that.

**A partial restore is normal:** `lake-cache/qou-v4-24-0-new` carries 2970 of
Mathlib's 6996 modules — 58 % absent. Outside that cone, `object file … does not
exist` is a cache gap, not a defect in the file under test.
