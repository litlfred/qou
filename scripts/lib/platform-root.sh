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
