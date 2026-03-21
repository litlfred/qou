# Test Engineer Skill

## Role

Write and maintain unit tests for the QOU formalization pipeline.
Tests are TypeScript using Bun's built-in test runner (`bun:test`).

## Test infrastructure

| Path | Purpose |
|------|---------|
| `scripts/tests/*.test.ts` | Test files (bun discovers `*.test.ts`) |
| `scripts/tests/helpers.ts` | Shared helpers: paths, Lean project discovery, LaTeX parsing |
| `scripts/tests/report.ts` | Test report generator (outputs `TestReport` JSON) |
| `scripts/tests/run-tests.sh` | Shell entry point (delegates to `bun test`) |
| `schemas/qou-types.ts` | TypeScript types for test definitions, results, reports, coverage |

## When to write a test

1. **A bug was found** — write a regression test before fixing.
2. **A new script or config file is added** — test its contract.
3. **A LaTeX macro is changed** — test extraction still works.
4. **A Lean project is added** — auto-discovered, but verify.
5. **The editor skill detects a potential error** — it will ask the user
   whether to write a test. If yes, this skill writes it.

## How to write a test

```typescript
// In scripts/tests/<suite>.test.ts
import { describe, test, expect } from "bun:test";
import { REPO_ROOT, LEAN_DIR, ... } from "./helpers";

describe("Feature under test", () => {
  test("specific behavior", () => {
    // Arrange
    // Act
    // Assert
    expect(result).toBe(expected);
  });
});
```

### Conventions

- **One test file per concern**: `lean-projects.test.ts`, `latex-lean-coverage.test.ts`,
  `infrastructure.test.ts`. Create new files for new concerns.
- **Use helpers.ts**: Don't hardcode paths or re-implement discovery.
- **Informational vs. blocking**: Tests that report data quality (sorry count,
  coverage gaps, label mismatches) should log and pass. Tests that verify
  contracts (JSON validity, required fields, file existence) should fail.
- **Comment the failure point**: Each test should document what bug or
  failure it prevents.
- **Types from schemas/qou-types.ts**: Use `TestResult`, `TestReport`,
  `CoverageEntry` etc. when generating structured output.

### Adding a new Lean project

When a new Lean library is added to `lakefile.toml` (e.g., `Unital`):
- `discoverLeanProjects()` in `helpers.ts` auto-discovers it
- `lean-projects.test.ts` automatically tests it (directory, files, sorry audit)
- No manual test registration needed

### Test categories (from `TestCategory` type)

| Category | What it tests |
|----------|---------------|
| `lean-compile` | .lean files exist, have imports, are non-empty |
| `lean-library` | Toolchain, lakefile, dependencies declared |
| `lean-sorry` | Sorry count per project/file |
| `latex-lean-coverage` | \\lean{} tags resolve, theorem coverage, \\leanok consistency |
| `latex-structure` | Labels, cross-refs, environments |
| `schema-validity` | JSON manifests match their schemas |
| `infrastructure` | MCP config, scripts, deploy, .gitignore |

## Running tests

```bash
# All tests
bun test                              # from scripts/tests/
./scripts/tests/run-tests.sh          # from repo root

# By suite
./scripts/tests/run-tests.sh lean     # Lean project tests
./scripts/tests/run-tests.sh coverage # LaTeX↔Lean coverage
./scripts/tests/run-tests.sh infra    # Infrastructure

# JSON report (TestReport schema)
./scripts/tests/run-tests.sh --json
bun run report.ts --out test-report.json
```

## Report output

`bun run report.ts` outputs JSON conforming to `TestReport` in
`schemas/qou-types.ts`. This report is consumed by:

1. **CI pipeline** — build status, pass/fail gates
2. **Publication pipeline** — proof coverage statistics for PDF/HTML
3. **Blueprint** — formalization status overlay

The report includes `by_category` breakdown so each pipeline stage
can extract just the tests relevant to it.
