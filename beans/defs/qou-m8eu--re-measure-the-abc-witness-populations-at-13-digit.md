---
# qou-m8eu
title: Re-measure the A/B/C witness populations at >=13-digit prefix and publish the LIST
status: completed
type: task
priority: normal
created_at: 2026-08-28T15:07:52Z
updated_at: 2026-08-28T15:48:33Z
parent: qou-jeb1
---

Measured at >=13-digit prefixes on the rebased branch: A=139 (+4 also carrying C), B=260, C=50, rounded=14. Two findings. (1) 50 witnesses ALREADY carry C on main -- invisible to q0_muon_population_partition.py, whose loose prefix 1.1099785955 structurally cannot match 1.1099785956. They derive q0 from the live CODATA-2022 ratio rather than reading the anchor. (2) The stamped-only criterion misses 65: A is carried by 139 but only 74 are stamped muon. Three scopes give 78 / 139 / 160; the old '53' was the narrowest and stale by ~2984 commits. Tool extended with --list/--value/--stamp/--json and a stamp x value cross-tab.
