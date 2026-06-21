---
# mig1
title: ""
status: completed
type: child
priority: normal
created_at: 2026-06-14T00:00:00Z
updated_at: 2026-06-21T19:39:07Z
parent: miga
---

# Package References & Routing

**Goal**: Update the root `qou/package.json` to delegate all testing, validation, and execution scripts (e.g. `bun run test`, `bun run lint`) strictly to the `folio-assistant` sub-modules. The root project should not manage the test orchestrators directly.
