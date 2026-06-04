#!/usr/bin/env bash
# scripts/lean-closure-orchestrator.sh — drive the 3-gate Lean-closure pipeline
#
# Per docs/audits/2026-06-03-proof-axis-629-fails-stale-diagnostics.md +
# todos/lean-discharge-queue.json `lean-compile-diagnostics-regen`.
#
# Pipeline:
#   Phase A — `lake build QOU` (from-source if no cache; 1-3 hrs first time)
#   Phase B — agent walks .lean files and calls
#             `mcp__lean-lsp__lean_diagnostic_messages` per file, emitting
#             JSONL to /tmp/lean-diagnostics-<DATE>.jsonl  [AGENT-DRIVEN]
#   Phase C — `bun run content/pipeline/lean-compile-audit.ts --ingest <jsonl>`
#             then qa-sweep proof-lean-compiles to refresh 629 stale sidecars
#
# Resume-safe: each phase is independent. If the container restarts mid-build,
# re-run Phase A (lake build is incremental — picks up where it left off).
#
# Usage:
#   ./scripts/lean-closure-orchestrator.sh build       # Phase A only (background safe)
#   ./scripts/lean-closure-orchestrator.sh status      # show build progress
#   ./scripts/lean-closure-orchestrator.sh ingest <jsonl>  # Phase C: ingest + sweep
#   ./scripts/lean-closure-orchestrator.sh             # show this help

set -uo pipefail
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOG="/tmp/lean-closure-build.log"
TODAY="$(date -u +%Y-%m-%d)"

cmd="${1:-help}"

case "$cmd" in
  build)
    echo "Phase A: lake build QOU"
    echo "  log: $LOG"
    echo "  background-safe: launching with nohup"
    cd "$REPO_ROOT"
    nohup lake build QOU > "$LOG" 2>&1 &
    pid=$!
    echo "  PID: $pid"
    echo "  Tail with: tail -f $LOG"
    echo "  Status with: $0 status"
    ;;

  status)
    if [ ! -f "$LOG" ]; then
      echo "No build log at $LOG. Run '$0 build' first."
      exit 1
    fi
    echo "=== Build log tail ==="
    tail -5 "$LOG"
    echo ""
    echo "=== Stats ==="
    built=$(grep -c '^✔' "$LOG" 2>/dev/null || echo 0)
    err=$(grep -c '^✖\|^error:' "$LOG" 2>/dev/null || echo 0)
    echo "  Modules built: $built"
    echo "  Errors: $err"
    if pgrep -f "lake build QOU" > /dev/null; then
      echo "  Build status: RUNNING"
    else
      if grep -q 'Build completed successfully\|Build successful' "$LOG"; then
        echo "  Build status: COMPLETE ✓"
      elif grep -q 'error:' "$LOG"; then
        echo "  Build status: FAILED"
      else
        echo "  Build status: STOPPED (no completion marker)"
      fi
    fi
    echo "  .lake/ disk: $(du -sh "$REPO_ROOT/.lake/" 2>/dev/null | awk '{print $1}')"
    ;;

  ingest)
    jsonl="${2:-}"
    if [ -z "$jsonl" ] || [ ! -f "$jsonl" ]; then
      echo "Usage: $0 ingest <path-to-diagnostics.jsonl>"
      echo "  JSONL must have one {\"file\":..., \"diagnostics\":[...]} per line"
      echo "  per content/pipeline/lean-compile-audit.ts --ingest format."
      exit 1
    fi
    echo "Phase C.1: ingest $jsonl into lean-compile-diagnostics.json"
    cd "$REPO_ROOT"
    bun run content/pipeline/lean-compile-audit.ts --ingest "$jsonl"
    echo ""
    echo "Phase C.2: qa-sweep proof-lean-compiles to refresh sidecars"
    bun run content/pipeline/qa-sweep.ts content/quantum-observable-universe \
      --only proof-lean-compiles
    echo ""
    echo "Done. Stale sidecar count should drop from 629."
    ;;

  help|--help|-h|"")
    cat <<EOF
Lean-closure orchestrator — drives the 3-gate pipeline.

Phases:
  A. lake build QOU                      (~1-3 hrs; sources Mathlib from local clone)
  B. per-file mcp__lean-lsp__lean_diagnostic_messages [AGENT-DRIVEN]
     Emit JSONL per content/pipeline/lean-compile-audit.ts --ingest format:
       {"file": "<repo-rel-path>", "diagnostics": [<LSP-style>]}
     One line per .lean file under content/quantum-observable-universe/.
  C. ingest JSONL + qa-sweep to clear 629 stale sidecars

Usage:
  $0 build                Phase A: launch lake build in background
  $0 status               Phase A: check progress
  $0 ingest <jsonl>       Phase C: ingest diagnostics + sweep sidecars

Phase B must be agent-driven (MCP tools require an agent harness). See
.claude/skills/local/lean-completeness-audit.md §6 'lean-compile-
diagnostics.json staleness warning' for the agent invocation pattern.

Resume-safe: each phase is independent. lake build is incremental
across container restarts.
EOF
    ;;

  *)
    echo "Unknown command: $cmd"
    echo "Run '$0 help' for usage."
    exit 1
    ;;
esac
