---
id: miga
type: parent
status: completed
created_at: 2026-06-14
updated_at: 2026-06-14
---

# Folio-Assistant Infrastructure Migration (Parent)

**Goal**: Decouple generic agent infrastructure, LLM configurations, and CI/CD operations from the quantum-observable-universe (`qou`) repository and isolate them within the `folio-assistant` sub-repository. The final state of `qou` must strictly contain only physics content, compute substrate, and math simulators.

## Work Breakdown
- **Phase 1 & 2 (Completed)**: Copilot/Claude skills moved. Docker files and MCP servers moved.
- **Phase 3**: Package routing (delegate test/lint from root to folio-assistant).
- **Phase 4**: GitHub Workflows migration and final repository cleanup.
