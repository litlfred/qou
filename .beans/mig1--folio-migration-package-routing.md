---
id: mig1
parent: miga
type: child
status: pending
created_at: 2026-06-14
updated_at: 2026-06-14
---

# Package References & Routing

**Goal**: Update the root `qou/package.json` to delegate all testing, validation, and execution scripts (e.g. `bun run test`, `bun run lint`) strictly to the `folio-assistant` sub-modules. The root project should not manage the test orchestrators directly.
