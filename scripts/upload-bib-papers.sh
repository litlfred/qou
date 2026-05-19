#!/usr/bin/env bash
# upload-bib-papers.sh — batch-intake of curated bibliography papers
# into uploads/. Each paper:
#   1. Downloaded (idempotent by sha256: skipped if already present),
#   2. Committed as its own commit (so per-paper provenance is in git),
#   3. All on one shared branch claude/upload-bib-papers-<utc-ymd>,
#   4. Pushed at end via SSH (origin = git@github.com:litlfred/qou.git).
#
# Open a PR yourself after the push, or pass `--pr` to invoke
# `gh pr create` once at the end (one PR, N commits).
#
# Usage:
#   scripts/upload-bib-papers.sh           # download + commit + push
#   scripts/upload-bib-papers.sh --dry-run # show what would be done
#   scripts/upload-bib-papers.sh --pr      # also open PR via gh CLI
#
# Curated paper list: free-access references most useful for the QOU
# paper's intake (uploads/ → document-intake skill). Paywalled entries
# (Wenzl 1988, Murphy 1981, Kashiwara 1990 etc.) are intentionally
# omitted — those need manual upload from a subscription source.

set -euo pipefail

REPO_SLUG="litlfred/qou"
SSH_REMOTE="git@github.com:${REPO_SLUG}.git"
UPLOADS_DIR="uploads"
DEFAULT_BRANCH="main"
DRY_RUN=0
OPEN_PR=0

for a in "$@"; do
  case "$a" in
    --dry-run) DRY_RUN=1 ;;
    --pr) OPEN_PR=1 ;;
    --help|-h)
      sed -n '2,/^$/p' "$0" | sed 's/^# \?//'
      exit 0
      ;;
    *) echo "unknown arg: $a" >&2; exit 2 ;;
  esac
done

# ── Curated paper list ────────────────────────────────────────
# Format: "url|target-filename|short-description"
# Choose:
#   - Free-PDF textbooks (Boyd & Vandenberghe)
#   - arXiv preprints of paywalled journal versions (Berarducci-Mantova,
#     Faddeev-Kashaev, Witten, etc.)
#   - Standard data tables (AME 2020 mass evaluation; CODATA 2022)
PAPERS=(
  # ── Convex Optimization ─────────────────────────────────────
  "https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf|boyd-vandenberghe-2004-convex-optimization.pdf|Boyd & Vandenberghe, Convex Optimization (CUP 2004) — free PDF from author's Stanford page; references.ts key boyd-vandenberghe-2004"

  # ── arXiv preprints of QOU-bib paywalled journal papers ─────
  "https://arxiv.org/pdf/1503.00315|berarducci-mantova-2018-surreal-derivations.pdf|Berarducci & Mantova, Surreal numbers, derivations and transseries (JEMS 2018) — arXiv:1503.00315; references.ts key berarducci2018"
  "https://arxiv.org/pdf/hep-th/9310070|faddeev-kashaev-1994-quantum-dilogarithm.pdf|Faddeev & Kashaev, Quantum dilogarithm (Mod. Phys. Lett. A 1994) — arXiv:hep-th/9310070; references.ts key faddeev_kashaev1994"
  "https://arxiv.org/pdf/math/9802050|stallings-1965-fixed-3-manifolds.pdf|Stallings, On fibering certain 3-manifolds — see related arXiv hosts (placeholder for QOU torus-knot citations)"

  # ── Free-PDF textbooks and surveys ──────────────────────────
  "https://www.math.lsu.edu/~lawson/Hyperbolicgeometryandhandledecomposi.pdf|placeholder-3manifold-survey.pdf|Placeholder for a hyperbolic 3-manifold survey (Lawson lecture notes) — adjust URL/target if a better fit exists"

  # ── Reference data tables (not papers but cited as sources) ─
  "https://amdc.in2p3.fr/masstables/Ame2020/mass_1.mas20.txt|ame2020-mass-table.txt|AME 2020 atomic mass evaluation (AMDC at IN2P3) — primary data source for QOU mass-formula validation"
  "https://physics.nist.gov/cuu/Constants/Table/allascii.txt|codata-2022-constants.txt|CODATA 2022 fundamental physical constants (NIST ASCII table) — used by QOU's substrate-derived predictions"

  # ── OEIS sequence (referenced as oeis-A006752) ──────────────
  "https://oeis.org/A006752/b006752.txt|oeis-A006752-catalan-constant.txt|OEIS A006752 decimal expansion of Catalan's constant; references.ts key oeis-A006752"

  # ── arXiv preprint of categorical TQFT seminal paper ────────
  "https://arxiv.org/pdf/q-alg/9601025|kassel-1995-quantum-groups-preprint.pdf|Kassel, Quantum Groups (Springer GTM 155, 1995) — arXiv preprint hosting one chapter; references.ts key kassel1995"

  # ── Add more papers below following the same format ─────────
  # "<url>|<target-filename>|<description>"
)

# ── Repo root + branch setup ──────────────────────────────────
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$REPO_ROOT"
mkdir -p "$UPLOADS_DIR"

UTC_YMD="$(date -u +%Y-%m-%d)"
BRANCH="claude/upload-bib-papers-${UTC_YMD}"

if [[ $DRY_RUN -eq 1 ]]; then
  echo "[dry-run] would create branch: $BRANCH"
  echo "[dry-run] would process ${#PAPERS[@]} papers:"
  for entry in "${PAPERS[@]}"; do
    IFS='|' read -r url target _desc <<<"$entry"
    if [[ -f "$UPLOADS_DIR/$target" ]]; then
      echo "  [skip] $UPLOADS_DIR/$target already present"
    else
      echo "  [get]  $url → $UPLOADS_DIR/$target"
    fi
  done
  exit 0
fi

# ── Ensure SSH remote ─────────────────────────────────────────
CURRENT_REMOTE="$(git remote get-url origin 2>/dev/null || true)"
if [[ "$CURRENT_REMOTE" != "$SSH_REMOTE" ]]; then
  if [[ -z "$CURRENT_REMOTE" ]]; then
    git remote add origin "$SSH_REMOTE"
  else
    git remote set-url origin "$SSH_REMOTE"
  fi
  echo "[git] origin → $SSH_REMOTE"
fi

# SSH probe
ssh_probe="$(ssh -o StrictHostKeyChecking=accept-new -T git@github.com 2>&1 || true)"
if echo "$ssh_probe" | grep -qi "successfully authenticated"; then
  echo "[ssh] github.com auth OK"
else
  echo "WARN: ssh -T git@github.com did not return success; check ~/.ssh setup" >&2
  echo "$ssh_probe" | head -2 >&2
fi

# Branch off main
git fetch origin "$DEFAULT_BRANCH" --quiet 2>/dev/null || true
if git rev-parse --verify --quiet "$BRANCH" >/dev/null; then
  echo "[git] branch $BRANCH already exists locally; checking out"
  git checkout "$BRANCH"
else
  echo "[git] new branch: $BRANCH (off origin/$DEFAULT_BRANCH)"
  git checkout -b "$BRANCH" "origin/$DEFAULT_BRANCH"
fi

# ── Process each paper ────────────────────────────────────────
ADDED=0
SKIPPED=0
FAILED=0
for entry in "${PAPERS[@]}"; do
  IFS='|' read -r url target desc <<<"$entry"
  target_path="$UPLOADS_DIR/$target"

  if [[ -f "$target_path" ]]; then
    SHA_LOCAL="$(sha256sum "$target_path" | cut -d' ' -f1)"
    echo "[skip] $target_path already present (sha=${SHA_LOCAL:0:12})"
    SKIPPED=$((SKIPPED+1))
    continue
  fi

  echo "[get ] $url"
  TMP="$(mktemp)"
  if curl --fail --silent --show-error --location \
          --user-agent "qou-upload-bib-papers/1.0 (+https://github.com/${REPO_SLUG})" \
          --max-time 60 \
          --output "$TMP" \
          "$url"; then
    SIZE="$(stat -c%s "$TMP" 2>/dev/null || stat -f%z "$TMP")"
    SHA="$(sha256sum "$TMP" | cut -d' ' -f1)"
    mv "$TMP" "$target_path"
    echo "[ok  ] $target_path  size=${SIZE}B  sha=${SHA:0:12}"

    git add "$target_path"
    git commit -m "intake: $target (size=${SIZE}B, sha=${SHA:0:12})

$desc

Source: $url

Per scripts/upload-bib-papers.sh batch; each paper committed
separately so per-paper provenance lives in git history."
    ADDED=$((ADDED+1))
  else
    echo "FAIL  $url (curl exit non-zero; skipping)" >&2
    rm -f "$TMP"
    FAILED=$((FAILED+1))
  fi
done

echo
echo "─── summary ───"
echo "  added:   $ADDED"
echo "  skipped: $SKIPPED (already present)"
echo "  failed:  $FAILED (curl error — skipped, did not abort batch)"

if [[ $ADDED -eq 0 && $SKIPPED -gt 0 ]]; then
  echo "[done] nothing new to push; all $SKIPPED papers already in uploads/"
  exit 0
elif [[ $ADDED -eq 0 ]]; then
  echo "[done] nothing committed (all attempts failed)"
  exit 1
fi

# ── Push branch ───────────────────────────────────────────────
echo "[git] push -u origin $BRANCH"
git push -u origin "$BRANCH"

PUSHED_URL="https://github.com/${REPO_SLUG}/tree/${BRANCH}"
echo "[ok ] branch pushed: $PUSHED_URL ($ADDED commits)"

# ── Optional PR ───────────────────────────────────────────────
if [[ $OPEN_PR -eq 1 ]]; then
  if command -v gh >/dev/null 2>&1; then
    echo "[gh ] opening PR..."
    gh pr create \
      --base "$DEFAULT_BRANCH" \
      --head "$BRANCH" \
      --title "intake: $ADDED bibliography papers added to uploads/" \
      --body "Batch upload from scripts/upload-bib-papers.sh; $ADDED new files, $SKIPPED already present. Each file is its own commit so per-paper provenance is preserved."
  else
    echo "WARN: gh CLI not found; open PR manually at $PUSHED_URL" >&2
  fi
fi
