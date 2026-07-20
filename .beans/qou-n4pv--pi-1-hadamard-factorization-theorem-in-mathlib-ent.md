---
# qou-n4pv
title: 'PI-1: Hadamard factorization theorem in Mathlib — entire function of finite order = (∏ over zeros, Weierstrass primary factors)·exp(poly). The theorem that pins phiBProd among its elliptic multiples. Hard multi-week complex-analysis build.'
status: in-progress
type: task
priority: normal
created_at: 2026-07-20T05:12:52Z
updated_at: 2026-07-20T06:32:43Z
---



## Verification status (2026-07-20, honest)
Compile-verification NOT completed. HadamardFactorization.lean imports the Mathlib Analysis cone (Jensen/Nevanlinna); the lake-cache oleans are algebra/combinatorics only (0 Analysis oleans). Building the cone takes >10min, exceeding BOTH the foreground tool timeout AND the detached-process lifetime (reclaimed on session idle). 4 build attempts (2 detached died mid-cone at 1587/2072 and 777/788; 2 foreground timed out at 590s/120s). The authoring agent's own run also never completed (left 'still grinding the Analysis cone'). So the file's 'compiles' status rests solely on an unverified lean-direct claim. Verification paths that WOULD work: CI (when billing clears), or seeding an Analysis-olean lake-cache branch. Do NOT mark this green until a completed build confirms it.
