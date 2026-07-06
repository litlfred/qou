---
# 3t8p
title: CI live lake build to score proof-build-green/no-axiom-growth/lean-compiles
status: todo
type: task
priority: normal
tags:
    - lightning-followup
created_at: 2026-07-06T04:11:12Z
updated_at: 2026-07-06T10:54:05Z
---

3 CI-only Lean criteria n/a on path (214/118/191). Need proof-objects.json+axiom-report.txt from full lake build. Run in lean_ci.yml.


## Update 2026-07-06
Local `lake build QOU` FAILS on `proofwidgets/widgetJsAll` (JS-widget target needs npm/node, absent in sandbox) even with github egress + `cache get`. Genuinely CI-only: run in lean_ci.yml (has node) to produce proof-objects.json + axiom-report.txt for proof-build-green / proof-no-axiom-growth.
