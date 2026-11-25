#!/usr/bin/env bash
# qa-publish-local — run the QA writers qou.json declares and publish them to
# this repository's qa-reports branch, from an agent's checkout.
#
# The same steps as the platform's layer-qa-publish.yml (which
# .github/workflows/compute-qa.yml calls), for when Actions is not enabled
# (owner, 2026-11-23: agents rebuild after a merge). publish-main-local.sh
# runs it, so a merge publishes the site AND the QA the integrated QA page
# reads.
#
#   1. the knowledge-graph audit for this instance, when the platform carries
#      it (kg-audit.ts); reported, never fatal, as in the workflow
#   2. every `qa.writers[].run` in qou.json, in order, from qou's root, with
#      QA_HOME=test/results and INSTANCE unset (scripts/qa-writer.sh resolves
#      both layouts); a writer that fails stops the run, so a partial record
#      is never published
#   3. qa:publish --ref main/<HEAD>, to origin's qa-reports branch, with the
#      entry laid out as the workflow lays it out: `<name>/test/results/...`,
#      because the workflow publishes from the INDEX checkout, where qou sits
#      at ./<name>, and the integrated QA page reads `<name>/<qa path>`. The
#      home is copied into a throwaway git checkout at that path and published
#      from there; nothing in this checkout is written.
#
# Usage:
#   bash scripts/qa-publish-local.sh                # writers + publish main/<HEAD>
#   bash scripts/qa-publish-local.sh --no-publish   # writers only
set -euo pipefail
ROOT=$(git rev-parse --show-toplevel)
cd "$ROOT"
PLAT=${PLATFORM_DIR:-folio-assistant}
PUBLISH=1; [ "${1:-}" = "--no-publish" ] && PUBLISH=0
export QA_HOME=test/results
unset INSTANCE
SHA=$(git rev-parse HEAD)

echo "== qa-publish-local: knowledge-graph audit"
if [ -f "$PLAT/cat-harness-tools/scripts/kg-audit.ts" ]; then
  bun run "$PLAT/cat-harness-tools/scripts/kg-audit.ts" --instance . 2>&1 | tail -5 \
    || echo "qa-publish-local: kg-audit did not complete; the kg axis reads unknown"
else
  echo "qa-publish-local: no kg-audit.ts in $PLAT; the kg axis reads unknown"
fi

python3 -c '
import json, sys
for w in json.load(open(sys.argv[1], encoding="utf-8")).get("qa", {}).get("writers", []):
    print(w["id"] + "\t" + w["run"].replace("\n", " "))
' qou.json | while IFS=$'\t' read -r id cmd; do
  echo "== qa-publish-local: writer $id"
  bash -c "$cmd"
done

if [ "$PUBLISH" = 0 ]; then echo "qa-publish-local: written under $QA_HOME, NOT published (--no-publish)"; exit 0; fi
NAME=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1], encoding="utf-8"))["name"])' qou.json)
REMOTE=${QA_STORE_REMOTE:-$(git remote get-url origin)}
STORE=$(cd "$PLAT/cat-harness-tools/scripts" && pwd)/qa-store.ts
STAGE=$(mktemp -d)
trap 'rm -rf "$STAGE"' EXIT
git -C "$STAGE" init -q
git -C "$STAGE" -c user.email=qa@localhost -c user.name=qa-publish-local commit -q --allow-empty -m stage
mkdir -p "$STAGE/$NAME/$QA_HOME"
cp -a "$QA_HOME/." "$STAGE/$NAME/$QA_HOME/"
echo "== qa-publish-local: qa:publish main/$SHA ($NAME/$QA_HOME)"
(cd "$STAGE" && QA_STORE_REMOTE=$REMOTE bun run "$STORE" publish --ref "main/$SHA" --root "$NAME/$QA_HOME")
