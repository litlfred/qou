---
# qou-mt4n
title: 'S2 follow-up: make the hecke-gram schema contract actually execute'
status: in-progress
pr: 8248
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-16T11:39:42Z
updated_at: 2026-11-17T07:18:00Z
parent: qou-5vkl
---

Follow-up to `qou-cds2` (S2). Related: `qou-m7py` (the Rust/Python
convention split this contract is supposed to catch).

## The finding, as relayed — and what re-measurement changed

Relayed: *"three tests covering the Rust/Python Gram contract skip in every
environment, and a live schema break (Rust renamed `inverse` →
`quotient_inverse` while `gram.schema.json` still required `inverse`)
survived the entire C→D migration because of it. Two of the three also
assert `G @ G_inv == I`, which convention D makes false."*

**Re-measured 2026-08-16 before filing. Two of the three claims are already
repaired; the mechanism that hid them is not.** Recording the correction
here rather than filing the relayed text as-is:

| claim | state today |
|---|---|
| schema still requires `inverse` | **FIXED.** `tools/hecke-engine/schemas/gram.schema.json` requires `quotient_inverse`; the property doc records the rename as deliberate *"so a consumer keyed on the old name fails loudly"*. |
| two tests assert `G @ G_inv == I` | **FIXED.** Both were rewritten — `test_rust_gram.py:65` and `test_native.py:85` — and each docstring names the assertion it replaced. |
| the tests skip in every environment | **LIVE.** Unchanged. |

So do **not** write this up as a live schema break. The live item is the
third row, and it is the one that matters: it is *why* the first two
survived a whole migration.

## The live mechanism

Three test modules are skipped at **module level**, so every test in them
disappears when the Rust binary / native wheel is absent:

    tools/pyhecke/tests/test_rust_gram.py:22   pytestmark = pytest.mark.skipif(not _rust_gram_available(), ...)
    tools/pyhecke/tests/test_native.py
    tools/pyhecke/tests/test_hecke_cli.py

`test_rust_gram.py` alone carries **5** tests behind that one mark,
including `test_rust_gram_validates_against_schema` — the check that would
have caught the rename the day it landed. Its sibling `test_native.py:89`
says so in as many words: *"skips when the Rust binary is not built, so it
never ran to fail."*

The skip is defensible in isolation (`qou-m7py` records a container where
`pyhecke_native` was simply not installed, and the package must work without
it). What is not defensible is that this leaves the **entire** Rust/Python
contract surface unverified in the default environment, so a contract break
is invisible until someone builds the engine by hand.

## What to do

1. Decide what the contract test is *for*. If it is meant to gate the
   contract, it cannot be conditional on an optional build — build the
   engine in the environment that runs it, or check in a recorded
   certificate fixture and validate **that** against the schema
   unconditionally.
2. At minimum, split the module: schema-shape assertions can run against a
   committed sample certificate with no binary present; only the
   Rust-vs-Python numerical agreement genuinely needs the build.
3. Make a skipped contract test **visible** rather than silent — a skip that
   is structural (never runs anywhere) should not look like a skip that is
   incidental (runs in CI, not locally).
4. Re-check the two repaired claims above before assuming they are still
   repaired; both were repaired only on 2026-08-15.

## Provenance

Filed 2026-08-16 from an agent that could not reach the `beans` CLI.
Relayed text corrected against the tree at merge `36080a4e21`; the
correction is deliberate — filing the stale version would have sent the next
agent to fix a schema that is already right.

## Progress (2026-11-17, PR #8248)

- [x] Scope the `hecke-gram` binary skip mark to subprocess-invoking tests in `tools/pyhecke/tests/test_rust_gram.py` and add 3 unconditional contract tests (`test_gram_schema_is_valid_and_requires_convention_d_keys`, `test_rust_gram_struct_fields_match_schema_contract`, `test_python_gram_certificate_validates_against_schema`) (PR #8248, Commit 1 `d3dcd4c4757a988299ad0246ed502bd2358a90e4`).
- [ ] Merge PR #8248 (`claude/round53-trd0-9nnz-fixes`, HEAD `b4185f1dac70a76b08299e291f3137fb9b60fe3c`)
