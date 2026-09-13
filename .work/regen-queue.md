# Regeneration queue — rewritten 2026-09-13 after the 702-commit merge

The previous contents are obsolete. Main's `qou-sv7h` arc made the kernel
EXACT — the accumulator had been multiplying 167-bit inputs at ambient dps 15
and the log layer was float64 on top — so **everything downstream of
`hecke_core_legacy` computed before this merge is superseded by construction**,
not merely stale. That is a much wider statement than the old queue's, and it
replaces it.

## 1. The nuclide table — RUNNING

`hadron-knot-table.witness.json` completed 19/19 on 2026-09-07 and is committed
(`ee2c9c278f2`), but under the PRE-sv7h kernel. Re-running now from zero; the
old checkpoint was deleted rather than re-stamped.

**That is the opposite call from 2026-09-07, and deliberately so.** That merge
changed a key file by a pure RENAME, so the cached atoms were provably still
valid and re-stamping was right. This one changes the arithmetic, so the cache
is wrong and discarding is right. The key did its job both times; what differs
is what the diff said.

Early signal: proton / neutron / protium reproduce byte-identically
(0.629328 / 0.475134 / 1.146338), as expected — sv7h bites on the
accumulation, so divergence should appear at compounds, not at A=1.

Cheaper than the 7 h it took last time: main replaced the factorial SYT
enumeration with an exact closed form (`qou-r4w5`), and the witness now
checkpoints per atom, so a killed container publishes the rows it reached.

## 2. `qou-3uvs` — re-confirm, but the conclusion should hold

The si28 / ca40 / fe56 Frobenius verdicts (all FAIL) came from the old kernel.
They need re-confirming from this run. The conclusion is expected to survive:
the violations are **10 %–84 % of the scale** and ~1e9 x the tolerance, and
sv7h moves values at ~1e-15. Nothing at that size flips a verdict at that
margin — but it should be read off the new witness, not assumed.

## 3. The kernel memo — DELETED, re-port only with a wider key

38 MB discarded, not ported. `_memo_build_id()` hashed ONLY the compiled
native module, and sv7h is a **Python** change, so the old cache would have
been served unchanged against a numeric path that had moved — a stale-value
failure, which is worse than no cache.

Re-port it against a key that hashes the Python numeric path too. Main already
uses that idiom: `he4_magnus_omega2_sign_sparse_probe.py` stamps
`_ck_src = sha256(open(__file__,'rb').read())` into every cached row and drops
rows that do not match. Same fix as the `_ckpt_key` widening.

`scripts/hkt-resume.sh` still sets `QOU_KERNEL_MEMO`; it is inert and says so.

## 4. Everything else — RE-CHECK against the merged tree first

The old queue's entries were measured before 702 commits landed. Do not act on
them as written. In particular main independently fixed several things this
branch was carrying:

* the `mp.mpf(repr(<mpf>))` trap (`qou-gxsd`) in at least three more places,
  and better — dividing directly rather than round-tripping through a string;
* the witness truncation window, by building the payload BEFORE `open(...,"w")`
  rather than by writing to a sibling temp (`qou-m549`; this file had been
  committed to main at **0 bytes**);
* `scriptFile` in `stamp_staleness_metadata` (`qou-4383`).

Re-measure before re-doing.
