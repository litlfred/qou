---
# qou-twnh
title: 'GAP: one witness is invalid JSON — leading + on numbers breaks every corpus-wide json.load scan'
status: completed
type: task
priority: normal
created_at: 2026-09-04T12:25:19Z
updated_at: 2026-09-04T12:25:59Z
---

FIXED 2026-09-04 (session cool-johnson). computations/_deprecated/qbeta-gb-filtration-residues.witness.json had rel_error_pct: +20.27 and ppm_error: +202689 — leading '+' on numbers is invalid JSON (RFC 8259: a number may start with '-' or a digit, never '+'). It was the SINGLE invalid-JSON witness corpus-wide, and it crashed every tool that does json.load over all witnesses (witness-schema validator, staleness triage, raw-float64 scans, my own audits). Hand-written, no producer (grep for the stem in computations/*.py is empty), deprecated — so fixed in the file directly. Removing the '+' preserves the exact numeric value. Verified: file parses, corpus-wide invalid-JSON count 1 -> 0.
