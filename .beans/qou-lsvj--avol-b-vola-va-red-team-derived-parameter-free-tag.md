---
# qou-lsvj
title: 'avol B_vol=a_V*A red-team: DERIVED-parameter-free tag is dishonest (contradicts own 2026-08-08 deprecation banner)'
status: todo
type: task
priority: normal
created_at: 2026-08-22T19:38:38Z
updated_at: 2026-08-22T19:38:57Z
---

Read-only adversarial audit. Doc: docs/audits/2026-08-22-avol-binding-redteam.md

FINDING: a_V = E0*ln(1/W_free) = E0*ln([3]_q!) = 7.5836 MeV/nucleon (mpmath, proton pin). No continuous fit (E0, W_free both forced), BUT >=3 discrete post-hoc knobs: (1) surprisal ln(1/W) chosen over linear (1-W) because it lands near 8 (linear=3.5); (2) unnormalized weight called a 'surprisal' though Sum W != 1; (3) x A all-knots packaging added AFTER single-partition E_gate broke at A>=24. Postdiction of the ~8 MeV/A plateau. Incoherent at A=1 (free nucleon gets 7.58 MeV binding, B_AME=0). Off the tr_M chain.

VERDICT: derived-candidate-near-match / postdiction-analogy. NOT genuine parameter-free derivation.

DASHBOARD TAG DISHONEST: mass_binding_dashboard.py line 779 tags B_vol 'DERIVED parameter-free' while lines 92-126 of the SAME file carry a 2026-08-08 deprecation banner saying B_vol 'has no basis in the derivation chain' and 'Removed from the dashboard'. Also fails the file's own DERIVED def ('through the Markov trace') and is absent from its own provenance table (line 671-679). Live self-contradiction on main.

Already assessed (in-file banner + probe's own honest verdict lines 245-254 + beans qou-78pt, qou-qlma) -> do NOT re-declare open. LIVE action = hygiene: reconcile code+legend with the 2026-08-08 deprecation (remove or demote DERIVED->EXPLORATORY). Not done here (read-only).
