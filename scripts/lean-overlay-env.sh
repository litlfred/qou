#!/usr/bin/env bash
# lean-overlay-env.sh — `lean`-direct verification with a PRIVATE WRITE OVERLAY.
#
# `lean-direct-env.sh` gives you a read-only LEAN_PATH over the restored olean
# tree.  That is enough to CHECK a file, but not to check anything that IMPORTS
# a module you just edited: the importer would load the stale shared olean and
# appear to compile.  Rebuilding into the shared tree is not an option either —
# it corrupts the restore for every other agent and every later run.
#
# This script adds the missing piece: an overlay directory you own, placed FIRST
# on LEAN_PATH, holding your rebuilt oleans.
#
# ─────────────────────────────────────────────────────────────────────────────
# THE TRAP THIS SCRIPT EXISTS TO AVOID (measured 2026-08-24, twice, by two
# independent agents):
#
#   An overlay is NOT a shadowing layer.  Lean resolves a module by taking the
#   FIRST LEAN_PATH root that contains the matching directory, and then looking
#   ONLY there.  It does not fall through to later roots.
#
#   So an overlay holding ONE rebuilt file breaks EVERY sibling import:
#
#     $ mkdir -p $OVL/QOU/SchurWeyl                     # one file rebuilt here
#     $ LEAN_PATH=$OVL:<shared> lean t.lean
#     error: object file '$OVL/QOU/SchurWeyl/WenzlMarkovCorner.olean' of module
#            QOU.SchurWeyl.WenzlMarkovCorner does not exist
#
#   ...even though that olean is present in the shared root.  An EMPTY overlay
#   is harmless; a PARTIAL one is worse than none.
#
# The fix is to make the overlay COMPLETE: a symlink farm mirroring every module
# in the shared roots, with real files only where you rebuilt.  `init` does that.
#
# And when you rebuild, the symlink MUST be removed first — otherwise `lean -o`
# follows it and writes THROUGH the link into the shared cache, which is the
# corruption the overlay was there to prevent.  `build` does that.
# ─────────────────────────────────────────────────────────────────────────────
#
# Usage:
#   scripts/lean-overlay-env.sh init [--overlay DIR]
#       (Re)build the symlink farm.  Idempotent; safe to re-run.
#
#   scripts/lean-overlay-env.sh check <file.lean> [--overlay DIR]
#       Type-check one file against the overlay.  Exit 0 = checks.
#
#   scripts/lean-overlay-env.sh build <Module/Path.lean> [--overlay DIR]
#       Rebuild a module INTO the overlay (breaking the symlink first), so that
#       later `check`s of its importers see your version.  Module path is
#       relative to the Lean package root, e.g. QOU/SchurWeyl/Foo.lean.
#
#   scripts/lean-overlay-env.sh env [--overlay DIR]
#       Print the LEAN_PATH, for use in your own command lines.
#
# Overlay defaults to $LEAN_OVERLAY, else a per-user temp dir.
# Never runs `lake`.  See AGENTS.md §"VERIFY a single file with lean-direct".
set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")/.." && pwd)"
PKG="$ROOT/folio/quantum-observable-universe/lean"

cmd="${1:-}"; shift || true
OVL="${LEAN_OVERLAY:-${TMPDIR:-/tmp}/lean-overlay-$(id -u)}"
args=()
while [ "$#" -gt 0 ]; do
  case "$1" in
    --overlay) OVL="$2"; shift 2 ;;
    *) args+=("$1"); shift ;;
  esac
done

# shellcheck source=/dev/null
source "$ROOT/scripts/lean-direct-env.sh" || exit 1
BASE_LEAN_PATH="$LEAN_PATH"

# Extra read-only olean roots (e.g. a session-local overlay from an earlier
# build) may be supplied via LEAN_EXTRA_ROOTS, colon-separated.
BASE_LEAN_PATH="${LEAN_EXTRA_ROOTS:+$LEAN_EXTRA_ROOTS:}$BASE_LEAN_PATH"

# LOAD-BEARING newline: `printf '%s'` emits no trailing newline, so `read`
# hits EOF on the final field and bash DISCARDS it.  That silently dropped the
# LAST LEAN_PATH root — which is the QOU package's own build directory — so the
# farm was built from Mathlib alone and every `check` of a file importing
# another QOU module died with "object file ... does not exist".  The failure
# reads like a real Lean error, and the natural workaround (point
# LEAN_EXTRA_ROOTS at some other agent's QOU overlay) reintroduces exactly the
# partial-overlay trap this script exists to prevent.
roots() { printf '%s\n' "$BASE_LEAN_PATH" | tr ':' '\n' | while read -r r; do [ -n "$r" ] && [ -d "$r" ] && printf '%s\n' "$r"; done; }

farm_init() {
  mkdir -p "$OVL"
  local n=0 skipped=0
  # First root wins, matching Lean's own resolution order.
  while read -r r; do
    local rn=0 rs=0
    while IFS= read -r -d '' f; do
      local dst="$OVL/${f#"$r"/}"
      if [ -e "$dst" ] || [ -L "$dst" ]; then rs=$((rs+1)); continue; fi
      mkdir -p "$(dirname "$dst")"
      ln -s "$f" "$dst" && rn=$((rn+1))
    done < <(find "$r" -name '*.olean' -print0 2>/dev/null)
    # PER-ROOT, not just the total.  "9429" and "7268" look alike enough that
    # two readers missed an entire package by eye; a root contributing 0 is
    # the dropped-root / shadowed-root failure and must be obvious at a glance.
    printf 'lean-overlay:   %6d linked %6d present  %s\n' "$rn" "$rs" "$r"
    n=$((n+rn)); skipped=$((skipped+rs))
  done < <(roots)
  echo "lean-overlay: farm at $OVL — $n linked, $skipped already present"
}

farm_check() {
  [ -d "$OVL" ] || { echo "lean-overlay: no overlay at $OVL — run 'init' first" >&2; return 1; }
  local any
  any=$(find "$OVL" -name '*.olean' -print -quit 2>/dev/null)
  [ -n "$any" ] || { echo "lean-overlay: overlay $OVL is empty — run 'init' first" >&2; return 1; }
}

case "$cmd" in
  init)
    farm_init
    ;;
  env)
    printf '%s\n' "$OVL:$BASE_LEAN_PATH"
    ;;
  check)
    [ "${#args[@]}" -ge 1 ] || { echo "usage: $0 check <file.lean>" >&2; exit 2; }
    farm_check || exit 1
    export LEAN_PATH="$OVL:$BASE_LEAN_PATH"
    ( cd "$PKG" && lean "${args[@]}" )
    ;;
  build)
    [ "${#args[@]}" -eq 1 ] || { echo "usage: $0 build <Module/Path.lean>" >&2; exit 2; }
    farm_check || exit 1
    src="${args[0]}"
    case "$src" in
      /*) echo "lean-overlay: build takes a package-relative path (e.g. QOU/SchurWeyl/Foo.lean)" >&2; exit 2 ;;
    esac
    [ -f "$PKG/$src" ] || { echo "lean-overlay: no such file $PKG/$src" >&2; exit 2; }
    out="$OVL/${src%.lean}.olean"
    mkdir -p "$(dirname "$out")"
    # LOAD-BEARING: drop the symlink so `lean -o` cannot write through it into
    # the shared cache.  Without this, a rebuild silently corrupts the restore.
    if [ -L "$out" ]; then
      rm -f "$out"
    elif [ -e "$out" ]; then
      rm -f "$out"          # our own earlier real build; replacing it is fine
    fi
    export LEAN_PATH="$OVL:$BASE_LEAN_PATH"
    ( cd "$PKG" && lean -o "$out" "$src" ) || exit $?
    [ -L "$out" ] && { echo "lean-overlay: BUG — $out is still a symlink after build" >&2; exit 1; }
    echo "lean-overlay: built $src -> $out"
    ;;
  selftest)
    # Locks in the invariant this script exists for.  A fix that stops
    # reproducing the failure it prevents is a fix nobody can trust.
    farm_check || exit 1
    probe="${TMPDIR:-/tmp}/lean-overlay-selftest.$$"
    mkdir -p "$probe/partial"
    mod=$(cd "$PKG" && find QOU -name '*.lean' -path '*SchurWeyl*' | head -1)
    [ -n "$mod" ] || { echo "selftest: no QOU module found" >&2; exit 1; }
    modname=$(printf '%s' "${mod%.lean}" | tr '/' '.')
    printf 'import %s\n' "$modname" > "$probe/t.lean"
    mkdir -p "$probe/partial/$(dirname "$mod")"
    rc=0
    # (1) a PARTIAL overlay must FAIL — this is the trap.
    if ( cd "$PKG" && LEAN_PATH="$probe/partial:$BASE_LEAN_PATH" lean "$probe/t.lean" ) >/dev/null 2>&1; then
      echo "selftest: FAIL — partial overlay resolved; the trap no longer reproduces" >&2
      rc=1
    else
      echo "selftest: ok — partial overlay breaks resolution (trap reproduces)"
    fi
    # (2) the farm overlay must SUCCEED.
    if ( cd "$PKG" && LEAN_PATH="$OVL:$BASE_LEAN_PATH" lean "$probe/t.lean" ) >/dev/null 2>&1; then
      echo "selftest: ok — farm overlay resolves"
    else
      echo "selftest: FAIL — farm overlay does not resolve $modname" >&2
      rc=1
    fi
    # ─────────────────────────────────────────────────────────────────────
    # (1) and (2) check SHADOWING.  Neither can ever catch a MISSING root, and
    # (2) is worth spelling out because it looks like it should: it runs lean
    # with LEAN_PATH="$OVL:$BASE_LEAN_PATH", so when the farm lacks a module
    # Lean simply falls through to the real root still sitting in
    # BASE_LEAN_PATH behind it.  Measured: under the dropped-root bug, with no
    # LEAN_EXTRA_ROOTS at all, (2) still printed "ok — farm overlay resolves"
    # while the farm held 0 of 2161 QOU oleans.  The base path silently repairs
    # exactly the omission the check is supposed to expose.
    #
    # So (3) and (4) assert COVERAGE, and both iterate a root list built by a
    # DIFFERENT mechanism (IFS array split) from the one roots() uses
    # (printf | tr | read) — otherwise a dropped root is invisible to the very
    # checks meant to find it, since it never appears in roots() output.
    # ─────────────────────────────────────────────────────────────────────
    st_expected=0
    st_roots=()
    IFS=':' read -r -a st_fields <<< "$BASE_LEAN_PATH"
    for st_f in "${st_fields[@]:-}"; do
      if [ -n "$st_f" ] && [ -d "$st_f" ]; then
        st_expected=$((st_expected+1)); st_roots+=("$st_f")
      fi
    done
    # (3) ROOT COMPLETENESS — roots() must not drop any existing root.
    st_actual=$(roots | wc -l)
    if [ "$st_expected" -eq "$st_actual" ]; then
      echo "selftest: ok — roots() emits all $st_expected existing LEAN_PATH roots"
    else
      echo "selftest: FAIL — roots() emits $st_actual of $st_expected existing LEAN_PATH roots" >&2
      echo "          (the dropped one is the LAST: 'printf %s' ends without a newline," >&2
      echo "           so 'read' hits EOF on the final field and bash discards it)" >&2
      rc=1
    fi
    # (4) PER-ROOT COVERAGE — the farm must reach into EVERY root, not merely
    #     be globally non-empty.  Under the bug the farm held 7268 links and
    #     zero QOU modules, so farm_check's global non-empty test passed while
    #     the modules under test were absent.  A link supplied by an earlier
    #     root counts: the invariant is reachability, which is what Lean needs.
    for st_r in "${st_roots[@]:-}"; do
      [ -n "$st_r" ] || continue
      st_olean=$(find "$st_r" -name '*.olean' 2>/dev/null | sort | head -1)
      [ -n "$st_olean" ] || continue          # root carries no oleans at all
      st_rel="${st_olean#"$st_r"/}"
      if [ -e "$OVL/$st_rel" ]; then
        echo "selftest: ok — farm covers $st_r"
      else
        echo "selftest: FAIL — farm has no link for $st_rel (root $st_r)" >&2
        rc=1
      fi
    done
    rm -rf "$probe"
    exit $rc
    ;;
  *)
    sed -n '1,50p' "$0" >&2
    exit 2
    ;;
esac
