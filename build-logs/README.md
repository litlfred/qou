# build-logs/

Structured output from [`scripts/lean-build-all.sh`](../scripts/lean-build-all.sh)
(root Lake-workspace build of every paper).

| File | Committable? | Purpose |
|------|-------------|---------|
| `lean-build-status.json` | **yes** | Per-paper pass/fail, failing modules, extracted compile errors (`file:line:col` + message) and `sorry` locations. |
| `<paper>.log` | no (gitignored) | Raw full build output per paper. |
| `_status.tsv` | no (gitignored) | Per-run scratch table consumed by the sidecar generator. |

## Sharing a build failure (no copy-paste)

Lean builds are slow and verbose. Instead of pasting terminal output, commit
the JSON sidecar and let an agent read it straight from the branch:

```bash
./scripts/lean-build-all.sh --cache          # build all papers from root
git add build-logs/lean-build-status.json
git commit -m "build: failure sidecar" && git push
```

Or let the script commit + push the sidecar for you (commits only that one
file, via your configured git remote — e.g. SSH):

```bash
./scripts/lean-build-all.sh --cache --commit-sidecar
```

The agent reads `build-logs/lean-build-status.json` and acts on the extracted
errors directly — no terminal copy-paste, and the slow build runs once on your
machine (or in CI).
