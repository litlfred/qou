---
# mig2
title: ""
status: completed
type: child
priority: normal
created_at: 2026-06-14T00:00:00Z
updated_at: 2026-06-21T19:39:07Z
parent: miga
---

# GitHub Workflows & Final Cleanup

**Goal**: Migrate GitHub workflows to the `folio-assistant/.github/workflows/` path and strip all residual testing frameworks (e.g., Playwright) and generic python scripts from the root `qou` directory.

**Constraints**: This must be executed safely to avoid breaking current CI/CD. Route the main repository workflows to trigger the folio-assistant environments.
