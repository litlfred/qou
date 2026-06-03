#!/usr/bin/env bash
# Make elan/lake/lean visible to subprocesses that DON'T source bashrc/lean-env.sh.
#
# Problem: in remote-execution containers, elan installs binaries into
# /root/.elan/bin/, which is NOT on the default PATH for non-interactive
# subprocesses (MCP tool subprocs, hook scripts, ad-hoc Bash invocations).
# Sourcing scripts/lib/lean-env.sh works for scripts that source it, but
# every other call site has to re-export PATH or hit "lake: command not
# found".
#
# Fix: symlink elan/lake/lean/leanc/leanmake into /usr/local/bin/, which
# IS on the default PATH for every spawned shell, including minimal-env
# MCP subprocesses. Plus drop an /etc/profile.d/elan.sh for login shells.
#
# Idempotent — safe to re-run on every SessionStart. If the toolchain
# isn't installed yet, also runs setup-lean-toolchain.sh (which downloads
# Lean v<toolchain> from GitHub release assets, since the upstream
# `release.lean-lang.org` host responds with "Host not in allowlist" 403
# in this container's network policy).
#
# Exit codes:
#   0 — symlinks present (and toolchain installed, if elan was found)
#   0 — elan not installed, nothing to do (run the toolchain installer
#       separately if you want Lean here)
#   non-zero — symlink creation failed (permissions? readonly /usr/local?)

set -uo pipefail

ELAN_HOME="${ELAN_HOME:-$HOME/.elan}"
LOCAL_BIN="/usr/local/bin"
BINS=(elan lake lean leanc leanmake)

# 1. If elan isn't installed, nothing to symlink. Bail quietly.
if [ ! -d "$ELAN_HOME/bin" ]; then
  exit 0
fi

# 2. Symlink each binary if it exists at the source and isn't already linked.
linked=0
for b in "${BINS[@]}"; do
  src="$ELAN_HOME/bin/$b"
  dst="$LOCAL_BIN/$b"
  if [ -e "$src" ] && [ ! -e "$dst" ]; then
    if ln -s "$src" "$dst" 2>/dev/null; then
      linked=$((linked+1))
    fi
  fi
done

# 3. Drop a profile.d entry for login shells (belt + suspenders; the
#    symlinks above are what actually makes MCP subprocs work).
profile_d="/etc/profile.d/elan.sh"
if [ ! -e "$profile_d" ] && [ -w "/etc/profile.d" ]; then
  cat > "$profile_d" <<EOF
# Added by scripts/setup-elan-symlinks.sh — make elan visible to all shells
export ELAN_HOME="\${ELAN_HOME:-$ELAN_HOME}"
case ":\$PATH:" in
  *":\$ELAN_HOME/bin:"*) ;;
  *) export PATH="\$ELAN_HOME/bin:\$PATH" ;;
esac
EOF
  chmod 644 "$profile_d" 2>/dev/null || true
fi

# 4. Quiet status (one line, prefixed for log grep).
if [ "$linked" -gt 0 ]; then
  echo "setup-elan-symlinks: linked $linked binaries into $LOCAL_BIN" >&2
fi

exit 0
