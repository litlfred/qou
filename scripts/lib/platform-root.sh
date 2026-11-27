# platform-root.sh — where this checkout reaches the platform layers.
#
#   . scripts/lib/platform-root.sh; plat=$(qou_platform_root "$ROOT")
#
# qou is a platform layer (owner ruling 2026-11-24, "1 qou is platform later"):
# index.config.json pins the layers it runs on and index.lock.json mounts them
# at the repository root (cat-harness/, cat-harness-tools/,
# folio-assistant-core/, folio-assistant-sci/, bootstrap*/). Those mounts are
# the platform. Until every hook and script has moved to them, the older
# `folio-assistant/` link (scripts/setup-folio-assistant.sh,
# .folio-assistant-pin) is the compatibility path, used when the root mounts
# are absent. Prints the directory that holds `cat-harness-tools/` and
# `folio-assistant-sci/`; prints nothing and returns 1 when neither is there.
qou_platform_root() {
  local root=${1:?root}
  if [ -f "$root/cat-harness-tools/package.json" ] && [ -d "$root/folio-assistant-sci" ]; then
    printf '%s\n' "$root"
  elif [ -d "$root/folio-assistant/cat-harness-tools" ]; then
    printf '%s\n' "$root/folio-assistant"
  else
    return 1
  fi
}

# qou_platform_shim <root> — make the compatibility path name the root mounts.
#
# When the layers are mounted at the root, `folio-assistant/` must reach THEM,
# not a second platform: the platform's typology registry scans every layer in
# the checkout, so an older clone behind `folio-assistant/` reading the newer
# root mounts fails outright (measured 2026-11-24: run-validate through a
# 42bd8d6 clone crashed on the root cat-harness-tools' validators, "validates
# family qa-attestations/v1, which kind attestations does not list"). So the
# link becomes a directory of relative links to the root mounts, and every
# script that still names `folio-assistant/<layer>/...` runs the one platform
# index.lock.json pins.
#
# Touches only a SYMLINK (the clone it pointed to is left where it is, and its
# target recorded in folio-assistant/.previous-link) or an absent path. A real
# directory that is not this shim (an in-place clone) is left alone, with a
# warning. No-op when the root mounts are absent.
qou_platform_shim() {
  local root=${1:?root} fa l
  fa="$root/folio-assistant"
  [ -f "$root/cat-harness-tools/package.json" ] && [ -d "$root/folio-assistant-sci" ] || return 0
  [ -f "$fa/.qou-platform-shim" ] && return 0
  if [ -L "$fa" ]; then
    local prev; prev=$(readlink "$fa")
    rm "$fa"
    mkdir "$fa"
    printf '%s\n' "$prev" > "$fa/.previous-link"
  elif [ -e "$fa" ]; then
    echo "platform-root: $fa is a directory, not the shim; left as is. It is a second platform beside the root mounts; move it aside to use them." >&2
    return 0
  else
    mkdir "$fa"
  fi
  for l in cat-harness cat-harness-tools folio-assistant-core folio-assistant-sci bootstrap bootstrap-tools node_modules; do
    ln -sfn "../$l" "$fa/$l"
  done
  printf 'folio-assistant/ -> the root-mounted layers (scripts/lib/platform-root.sh)\n' > "$fa/.qou-platform-shim"
  echo "platform-root: folio-assistant/ now names the root-mounted layers"
}
