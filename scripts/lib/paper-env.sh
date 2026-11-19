# paper-env.sh — where this repository lives and which paper to build, derived
# rather than written in. Sourced by build-paper-pdf.sh, publish-paper-pdf.sh
# and paper-diff-pdf.sh, so none of them names an owner, a repository or a
# paper (owner, 2026-11-19).
#
# Sets:
#   REPO_SLUG   <owner>/<repo>: $GITHUB_REPOSITORY in Actions, else the origin
#               remote (https, ssh, or a proxied .../git/<owner>/<repo> URL)
#   REPO_OWNER, REPO_NAME
#   REPO_BASE   https://github.com/<owner>/<repo>
#   PAGES_BASE  https://<owner>.github.io/<repo>
#   GHPAGES_BLOB  $REPO_BASE/blob/gh-pages
#   DEFAULT_PAPER the first `dir:` listed in folio/folio.ts
# Expects ROOT (the repository root) to be set.
REPO_SLUG="${GITHUB_REPOSITORY:-}"
if [ -z "$REPO_SLUG" ]; then
  REPO_SLUG=$(git -C "$ROOT" remote get-url origin 2>/dev/null \
    | sed -E 's#\.git$##; s#.*[/:]([^/:]+/[^/:]+)$#\1#')
fi
[ -n "$REPO_SLUG" ] && [ "${REPO_SLUG#*/}" != "$REPO_SLUG" ] \
  || { echo "paper-env: cannot work out <owner>/<repo> (no GITHUB_REPOSITORY, no origin remote)" >&2; return 2 2>/dev/null || exit 2; }
REPO_OWNER=${REPO_SLUG%%/*}
REPO_NAME=${REPO_SLUG#*/}
REPO_BASE="https://github.com/$REPO_SLUG"
PAGES_BASE="https://$REPO_OWNER.github.io/$REPO_NAME"
GHPAGES_BLOB="$REPO_BASE/blob/gh-pages"
DEFAULT_PAPER=$(grep -oE "dir:[[:space:]]*\"[^\"]+\"" "$ROOT/folio/folio.ts" 2>/dev/null \
  | head -1 | sed -E 's/.*"([^"]+)"/\1/')
# The default branch, for source links: origin's HEAD, else "main".
DEFAULT_BRANCH=$(git -C "$ROOT" symbolic-ref --quiet --short refs/remotes/origin/HEAD 2>/dev/null | sed 's#^origin/##')
DEFAULT_BRANCH=${DEFAULT_BRANCH:-main}
