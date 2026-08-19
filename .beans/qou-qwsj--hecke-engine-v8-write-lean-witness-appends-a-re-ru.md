---
# qou-qwsj
title: hecke-engine v8 write_lean_witness APPENDS — a re-run duplicates Lean decls into a non-compiling witness
status: todo
type: task
priority: normal
created_at: 2026-08-19T21:12:37Z
updated_at: 2026-08-19T21:13:07Z
---

FOUND 2026-08-19 while running the hecke-engine binaries for the qou-8q0u
before/after output verification (PR #5344). Not fixed there -- out of that
PR's scope (it is an anchor change, this is an IO bug).

DEFECT. tools/hecke-engine/src/bin/v8.rs:749-750 --

    let mut file = std::fs::OpenOptions::new()
        .create(true).append(true).open(&filename).unwrap();

write_lean_witness APPENDS unconditionally and dedups on nothing. So running
the same nucleus twice writes a SECOND copy of every declaration into the
committed witness-<nuc>.lean. Observed concretely: one `hecke-engine 2 2` run appended 50 lines to tools/hecke-engine/witness-4he.lean, re-declaring
tr_alt_4he / net_4he / observable_4he / color_4he which were already there.
Duplicate declarations in one Lean file do not compile -- so the emitted
witness is broken by the second run, silently, with exit 0.

The committed witness-4he.lean is currently CLEAN (the accidental append was
reverted, not committed). The bug is latent, not live in the tree.

RELATED, same run, possibly a separate issue: `hecke-engine 2 2` also rewrote
checkpoint-4he.json with materially different content -- n_words 12 -> 10,
tr_alt_n_terms 22 -> 5, wholly different coefficient lists. Those are INTEGER
Laurent coefficients, so they cannot move with the q0 anchor; the committed
checkpoint must have come from a different invocation or an older version.
Worth establishing which invocation is canonical before trusting either.

FIX SKETCH. Either truncate (.write(true).truncate(true)) so a re-run replaces,
or read-then-skip-if-present so the file accumulates one block per nucleus as
the append presumably intended. Decide which behaviour is wanted first -- the
filename is per-nucleus (witness-4he.lean), which argues for truncate.
