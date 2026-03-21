#!/usr/bin/env bash
# Test runner for MCP setup scripts.
#
# Tests are added as we hit failure points.
# Each test function returns 0 (pass) or 1 (fail).
#
# Usage:
#   ./scripts/tests/run-tests.sh

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
PASS=0
FAIL=0

# ── Helpers ──────────────────────────────────────────────────────
run_test() {
    local name="$1"
    local func="$2"
    if "$func" 2>/dev/null; then
        echo "  PASS  $name"
        PASS=$((PASS + 1))
    else
        echo "  FAIL  $name"
        FAIL=$((FAIL + 1))
    fi
}

# ── Tests ────────────────────────────────────────────────────────

test_check_lean_outputs_valid_json() {
    # Failure point: check-lean.sh must always output parseable JSON,
    # even when lean is not installed.
    OUTPUT=$("$REPO_ROOT/scripts/check-lean.sh" 2>/dev/null)
    echo "$OUTPUT" | python3 -c "import json,sys; json.load(sys.stdin)" 2>/dev/null
}

test_check_lean_has_mode_field() {
    # Failure point: editor skill reads "mode" field to decide
    # local vs remote vs none. Must always be present.
    OUTPUT=$("$REPO_ROOT/scripts/check-lean.sh" 2>/dev/null)
    MODE=$(echo "$OUTPUT" | python3 -c "import json,sys; print(json.load(sys.stdin)['mode'])" 2>/dev/null)
    [ -n "$MODE" ]
}

test_check_lean_mode_is_valid() {
    # Mode must be one of: local, remote, local-degraded, none
    OUTPUT=$("$REPO_ROOT/scripts/check-lean.sh" 2>/dev/null)
    MODE=$(echo "$OUTPUT" | python3 -c "import json,sys; print(json.load(sys.stdin)['mode'])" 2>/dev/null)
    case "$MODE" in
        local|remote|local-degraded|none) return 0 ;;
        *) return 1 ;;
    esac
}

test_check_lean_reads_remote_from_config() {
    # Failure point: remote_url must come from lean-mcp.config.json
    OUTPUT=$("$REPO_ROOT/scripts/check-lean.sh" 2>/dev/null)
    REMOTE_URL=$(echo "$OUTPUT" | python3 -c "import json,sys; print(json.load(sys.stdin).get('remote_url',''))" 2>/dev/null)
    EXPECTED_DOMAIN=$(python3 -c "import json; print(json.load(open('$REPO_ROOT/lean-mcp.config.json')).get('domain',''))" 2>/dev/null)
    echo "$REMOTE_URL" | grep -q "$EXPECTED_DOMAIN"
}

test_check_no_artifacts_passes_clean() {
    # With nothing staged, the pre-commit hook should pass
    cd "$REPO_ROOT"
    "$REPO_ROOT/scripts/check-no-lean-artifacts.sh"
}

test_config_json_is_valid() {
    python3 -c "import json; json.load(open('$REPO_ROOT/lean-mcp.config.json'))"
}

test_config_has_required_fields() {
    python3 -c "
import json, sys
d = json.load(open('$REPO_ROOT/lean-mcp.config.json'))
required = ['domain', 'image', 'mcp_internal_port', 'authorized_emails']
missing = [f for f in required if f not in d]
if missing:
    print(f'Missing: {missing}', file=sys.stderr)
    sys.exit(1)
"
}

test_mcp_json_is_valid() {
    python3 -c "import json; json.load(open('$REPO_ROOT/.mcp.json'))"
}

test_mcp_json_has_lean_lsp() {
    python3 -c "
import json, sys
d = json.load(open('$REPO_ROOT/.mcp.json'))
if 'lean-lsp' not in d.get('mcpServers', {}):
    sys.exit(1)
"
}

test_caddyfile_template_has_domain_var() {
    grep -q '${LEAN_MCP_DOMAIN}' "$REPO_ROOT/deploy/Caddyfile.template"
}

test_gitignore_blocks_env() {
    grep -q 'deploy/.env' "$REPO_ROOT/.gitignore"
}

test_gitignore_blocks_lake() {
    grep -q 'lean/.lake/' "$REPO_ROOT/.gitignore"
}

test_self_update_preserves_env() {
    # The self-updater must exclude deploy/.env from git clean
    grep -q "exclude='deploy/.env'" "$REPO_ROOT/deploy/self-update.sh"
}

# ── Run ──────────────────────────────────────────────────────────
echo "=== MCP Setup Tests ==="
echo ""

run_test "check-lean.sh outputs valid JSON"         test_check_lean_outputs_valid_json
run_test "check-lean.sh has mode field"              test_check_lean_has_mode_field
run_test "check-lean.sh mode is valid enum"          test_check_lean_mode_is_valid
run_test "check-lean.sh reads remote from config"    test_check_lean_reads_remote_from_config
run_test "check-no-artifacts passes when clean"      test_check_no_artifacts_passes_clean
run_test "lean-mcp.config.json is valid JSON"        test_config_json_is_valid
run_test "lean-mcp.config.json has required fields"  test_config_has_required_fields
run_test ".mcp.json is valid JSON"                   test_mcp_json_is_valid
run_test ".mcp.json has lean-lsp server"             test_mcp_json_has_lean_lsp
run_test "Caddyfile.template uses domain variable"   test_caddyfile_template_has_domain_var
run_test ".gitignore blocks deploy/.env"             test_gitignore_blocks_env
run_test ".gitignore blocks lean/.lake/"             test_gitignore_blocks_lake
run_test "self-update.sh preserves .env"             test_self_update_preserves_env

echo ""
echo "Results: $PASS passed, $FAIL failed"
[ "$FAIL" -eq 0 ]
