---
# qou-a2q5
title: 'Witness staleness blind spot: imported-module drift (neither SELF nor UPSTREAM catches it)'
status: todo
type: task
priority: normal
created_at: 2026-08-10T17:48:14Z
updated_at: 2026-08-10T17:48:15Z
parent: qou-1nvh
---

Found by hitting it THREE TIMES in one session (PR #4939). witness_dependency_drift.py checks exactly two directions: SELF (producer scriptHash) and UPSTREAM (recorded upstream_witness_hashes, i.e. other WITNESS files). Neither hashes the producer's IMPORTED-MODULE cone. So a change to an upstream .py module leaves the producer byte-identical (SELF passes) with no upstream witness changed (UPSTREAM passes or is undeclared) while the committed numbers no longer reproduce. Worked cases: (1) bsym-residual-shell-structure - _bond_type_L/tr_m_atom_via_transfer changed 2026-08-08, H2 flipped true->FALSE on refresh; (2) gap2-borromean-triple-count - coulomb_energy.py changed 2026-08-09 (qou-usft), triple/binding ratios 1.132/1.197/1.240 -> 1.148/1.210/1.250 on refresh; (3) coulomb-mirror-killswitch - same qou-usft change, plus stale verdict prose. Neither (1) nor (2) declares upstream_witness_hashes at all. Measured adoption of that mechanism repo-wide: 222 witnesses = 7.7%. So the declared-edge path cannot cover this even in principle at current adoption. Proposed fix: hash the producer's first-party import cone (resolve local imports transitively, skip stdlib/third-party) into a new witness field, and add it as a third direction in the validator. Cheaper interim: have WitnessBuilder auto-record hashes of first-party modules already in sys.modules at save() time.
