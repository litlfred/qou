---
# qou-lb0f
title: 'folio-assistant lake-cache: ''restore'' cannot detect a GUTTED cache — presence check is >0, not expected-count'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-07T11:13:14Z
updated_at: 2026-10-04T15:19:13Z
parent: qou-kemt
---

Found 2026-08-07 immediately after the lake build wipe above. With the cache gutted from 7268 to 459 oleans, 'lake-cache.sh restore' returned:\n  'cache already present (459 oleans) -- nothing to do.'\n  EXIT=0\nand refused to restore. Only 'rm -rf .lake' then restore recovered the full 7268.\n\nROOT CAUSE: the presence check is 'are there any oleans at all', so any nonzero count passes. The skill doc claims this class was fixed -- its failure table says "'restored' but the build still runs cold | nothing checked that oleans actually landed | Counts .olean files and fails if zero" -- but 'fails if zero' is too weak: a gutted cache is nonzero and sails through. Exit code 0 here is actively misleading, since exit 3 ('cache found but UNUSABLE') is the state that actually obtains.\n\nSUGGESTED FIX: record the expected olean count in the cache branch (a manifest alongside the split parts) and have status/restore compare against it, returning 3 on a shortfall and re-restoring rather than no-oping. Failing that, a --force flag would at least save the rm -rf.



## Summary of Changes

Closed 2026-10-04 in the work-plan reorganisation: the work has landed on main. Evidence: [M] f-a cat-harness/scripts/lake-cache.sh now counts traces (count_traces, own_oleans_expected) and documents restore-then-build eviction (lines 260-285); lake-cache tests exist
