---
name: build-docs
roles: [collaborator, owner]
user_invocable: true
description: >
  Builds the Lean HTML documentation (doc-gen4) locally in the workspace.
allowed-tools: Bash AskUserQuestion run_command
---

# /build-docs

This command builds the Lean HTML documentation using `doc-gen4` locally in the workspace to save GitHub CI minutes.

## Behavior
1. Navigate to the Lean directory: `cd folio/quantum-observable-universe/lean`
2. Uncomment the `doc-gen4` dependencies in `lakefile.toml` (which are commented out by default to avoid slow builds).
   ```bash
   sed -i '' 's/# \[\[require\]\]/[[require]]/' lakefile.toml
   sed -i '' 's/# name = "doc-gen4"/name = "doc-gen4"/' lakefile.toml
   sed -i '' 's|# git = "https://github.com/leanprover/doc-gen4"|git = "https://github.com/leanprover/doc-gen4"|' lakefile.toml
   sed -i '' 's/# rev = "1cd7a1113090e216703e323e8fdcdf099f0a9c8a"/rev = "1cd7a1113090e216703e323e8fdcdf099f0a9c8a"/' lakefile.toml
   ```
   *(Note: The `sed -i ''` syntax is used because the agent environment is macOS).*
3. Update `doc-gen4` and run the build:
   ```bash
   lake update doc-gen4
   lake -R -Kenv=dev build QOU:docs
   ```
4. Restore `lakefile.toml` to avoid committing the `doc-gen4` dependency:
   ```bash
   git checkout lakefile.toml
   ```
5. Confirm to the user that the documentation has been generated in `folio/quantum-observable-universe/lean/.lake/build/doc`.
