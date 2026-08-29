---
# qou-s7g0
title: 'GAP: lambda_scale_homflypt_skein_recursion_probe imports a module that does not exist'
status: todo
type: task
priority: normal
created_at: 2026-08-28T15:43:19Z
updated_at: 2026-08-28T15:43:19Z
parent: qou-a1lw
---

computations/probes/lambda_scale_homflypt_skein_recursion_probe.py fails with ModuleNotFoundError: No module named 'lambda_scale_alt_g_skein_polynomial_direct'. Verified: that module exists NOWHERE in the tree; the only occurrences of the name are three docstring mentions inside the failing file itself, describing it as the 'Strategy G predecessor'. Either it was deleted or it was never committed. Its witness carries the OLD-MUON value B and cannot be drained until this is resolved. Found by the B-population sweep, PR #5889.
