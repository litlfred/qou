#!/usr/bin/env bash
# site:lean — the qou site build's Lean step (index.config.json site.build.siteSteps).
#
# Publishes the Lean render at the route qou.json's `lean-docs` declaration
# names (process lean-docs-publish.bpmn, folio-assistant-sci). The render is
# READ from the mounted branch store, never from a Lake build, so the site build
# needs no Lean toolchain. Everything is read from the declarations: the mount
# path and route from qou.json, the module roots from each paper's lakefile.
#
# THE visualiser is the KG route (owner, 2026-11-19: "use thin html and dynamic
# loading"): lean-kg-publish's viewer page and its data/ shards, which the
# store holds under lean/; they are copied as they are. A store that still holds
# doc-gen4's static HTML instead is staged by lean-render.ts (its bookkeeping
# left out, its iframe pages rail-declined, its layout shim added), the
# non-default fallback. Either way the platform's own rail pass, which the site
# build runs after every site step, puts the harness rail on the pages, so the
# rail's assets are the site's and nothing extra lands at the site root.
#
set -euo pipefail
SITE="${1:?usage: site:lean <built site>}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
read -r MOUNT ROUTE < <(python3 -I - "$ROOT/qou.json" <<'PY'
import json, re, sys
for d in json.load(open(sys.argv[1]))["directories"]:
    if "lean" not in d.get("graphTypologies", []):
        continue
    v = d.get("coverage", {}).get("visualiser", [])
    refs = [v] if isinstance(v, str) else [x if isinstance(x, str) else x.get("ref", "") for x in v]
    for r in refs:
        m = re.match(r"^_site/(.+?)/(?:index\.html)?$", r)
        if m:
            print(d["path"].rstrip("/"), m.group(1)); sys.exit(0)
sys.exit("qou.json declares no `lean` graph with a _site/<route>/ visualiser")
PY
)
DOCS="$ROOT/$MOUNT"
if [ ! -f "$DOCS/index.html" ]; then
  echo "✗ site:lean: the Lean store is not mounted at $MOUNT/ (run: bun run cat state:mount). No Lean pages staged, and that is not a pass." >&2
  exit 1
fi
DEST="$SITE/$ROUTE"
if [ -f "$DOCS/data/index.json" ]; then
  rm -rf "$DEST"; mkdir -p "$DEST"
  cp -R "$DOCS/." "$DEST/"
  rm -f "$DEST/manifest.json" "$DEST/README.md"
  echo "✓ site:lean: the Lean graph viewer ($MOUNT/, KG route) staged at $ROUTE/; railed by the site build's rail pass"
  exit 0
fi
MODULES=$(sed -n '/^\[\[lean_lib\]\]/,/^name/ s/^name *= *"\(.*\)"/\1/p' "$ROOT"/folio/*/lean/lakefile.toml | paste -sd, -)
echo "⚠ site:lean: $MOUNT/ holds doc-gen4's static HTML, not the KG viewer: staging the fallback" >&2
exec bun run "$ROOT/folio-assistant/folio-assistant-sci/adapters/paper/lean/lean-render.ts" \
  --docs "$DOCS" --site "$SITE" --route "$ROUTE" --modules "$MODULES" --no-rail
