---
id: mig2
parent: miga
type: child
status: pending
created_at: 2026-06-14
updated_at: 2026-06-14
---

# GitHub Workflows & Final Cleanup

**Goal**: Migrate GitHub workflows to the `folio-assistant/.github/workflows/` path and strip all residual testing frameworks (e.g., Playwright) and generic python scripts from the root `qou` directory.

**Constraints**: This must be executed safely to avoid breaking current CI/CD. Route the main repository workflows to trigger the folio-assistant environments.
