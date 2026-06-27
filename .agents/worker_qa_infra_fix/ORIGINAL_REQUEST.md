## 2026-06-27T12:04:21Z

Fix the relative import paths in `folio-assistant/src/qa-agent-write.ts` and `folio-assistant/src/qa-agent-drain-queue.ts`.

Specifically:
1. In `folio-assistant/src/qa-agent-write.ts`:
   - Replace import from `"../../content/pipeline/qa-utils"` with `"../content/pipeline/qa-utils"`
   - Replace import from `"../../schemas/block-qa"` with `"../schemas/block-qa"`
2. In `folio-assistant/src/qa-agent-drain-queue.ts`:
   - Replace import from `"./qa-utils"` with `"../content/pipeline/qa-utils"`
   - Replace import from `"./qa-criteria-registry"` with `"../content/pipeline/qa-criteria-registry"`

Verification:
Run `bun run folio-assistant/src/qa-agent-write.ts` and `bun run folio-assistant/src/qa-agent-drain-queue.ts` using bun to verify they load and compile (they will print argument validation errors or run successfully, but they should NOT fail with "Cannot find module").

When verified, commit these changes as `fix(qa-infra): correct relative import paths in folio-assistant scripts` and push the commit. Return a report detailing what changes were made and verification output.

## 2026-06-27T12:06:18Z

Correct the repo root detection logic in `folio-assistant/src/qa-agent-write.ts` and `folio-assistant/src/qa-agent-drain-queue.ts` to properly resolve paths when run from the `qou` repository root.

Specifically:
1. In `folio-assistant/src/qa-agent-drain-queue.ts`:
   Replace `process.chdir(resolve(import.meta.dir, "..", ".."));` on line 35 with a check that uses `process.cwd()` if `content/quantum-observable-universe` exists there, so it chdirs to the `qou` repository root instead of the `folio-assistant` directory.
   Example:
   ```typescript
   const initialCwd = process.cwd();
   const repoRoot = existsSync(resolve(initialCwd, "content/quantum-observable-universe"))
     ? initialCwd
     : resolve(import.meta.dir, "..", "--");
   process.chdir(repoRoot);
   ```
2. In `folio-assistant/src/qa-agent-write.ts`:
   Replace `const REPO_ROOT = resolve(import.meta.dir, "../..");` on line 48 with a similar dynamic resolution for `REPO_ROOT`.
   Example:
   ```typescript
   const initialCwd = process.cwd();
   const REPO_ROOT = existsSync(resolve(initialCwd, "content/quantum-observable-universe"))
     ? initialCwd
     : resolve(import.meta.dir, "../..");
   ```

Verification:
Run `bun run folio-assistant/src/qa-agent-drain-queue.ts content/quantum-observable-universe --out /tmp/current-drain-queue.json` from the `qou` root and verify that the output JSON `/tmp/current-drain-queue.json` has correct chapter slugs (e.g. "appendix-knot-periodic-table" rather than "litlfred" or "?").

When verified, commit and push the changes. Report back with the verification results and commit info.

