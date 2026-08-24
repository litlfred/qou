#!/usr/bin/env bash
# check-sidecars.sh — PRE-COMMIT preflight: map changed files → the QA sidecars /
# criteria that apply to them, so agents check the RELEVANT sidecars instead of
# relying on the reactive post-commit qa-sweep (which does not cover everything).
#
# Motivation (2026-06-25): a gratuitous `(q : ℝ)` / `SL₂(ℝ)` landed on a purely
# algebraic statement in a STANDALONE library Lean file. The §7c rule is documented
# and doubly-tooled (`q-usage-*`, `wall-side-correct`/`checkWallSide`), but both
# checkers run per content-block `<block>.qa.json` — a library file with no `.md`/`.ts`
# sibling has no sidecar and escapes the sweep. This script closes that gap: it tells
# you, for exactly the files you touched, which sidecar criteria apply and runs the
# §7c base-ring check on un-sidecar'd library Lean by hand.
#
# Usage:
#   scripts/check-sidecars.sh [file ...]     # explicit files
#   scripts/check-sidecars.sh                # default: staged + unstaged vs HEAD
#
# Exit code: 0 always (advisory). Look for ⚠ lines — they need agent action.

set -uo pipefail
ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "not a git repo"; exit 0; }
cd "$ROOT"

# Shared changed-file collection. ONE definition, so the fifth gate script
# cannot repeat the defect the first four shared (bean qou-pt9b).
. "$ROOT/scripts/lib/changed-files.sh"

# Collect target files.
if [ "$#" -gt 0 ]; then
  files=("$@")
else
  # THE MERGE-BASE DIFF IS NOT OPTIONAL -- same defect as precision-gates.sh
  # --changed (bean qou-s2gm, defect 1), found here by running this script on
  # a branch with three commits and being told "no changed files".
  #
  # Both `git diff HEAD` and `--cached` see only UNCOMMITTED work, so once a
  # change is committed this exits 0 having examined nothing. It is worse here
  # than there: AGENTS.md names this script the pre-commit preflight AND the
  # merge-time verification gate for content blocks ("Content blocks changed ->
  # check-sidecars.sh clean"), and at merge time the changes are ALWAYS
  # committed -- so as the merge gate it has been reading an empty set and
  # reporting success.
  #
  # On `main` the merge-base IS HEAD, so this adds nothing on a clean checkout.
  mapfile -t files < <(changed_files)
fi
mapfile -t files < <(printf '%s\n' "${files[@]:-}" | sort -u | grep -v '^$' || true)
if [ "${#files[@]}" -eq 0 ]; then
  # A SKIP IS NOT A PASS (#5495, requested by the sibling on #5453). "0 files
  # considered" and "N considered, none relevant" were the same sentence, and
  # they are not the same fact: the first means this gate examined NOTHING.
  # The scope line says what was compared, so a caller can tell a genuine skip
  # from the merge-base half having been dropped.
  echo "check-sidecars: 0 changed file(s) — this check examined NOTHING."
  echo "  scope: $(changed_files_scope)"
  exit 0
fi

# Code-level archimedean markers (the §7c wall). Prose in /- -/ docstrings is ignored
# by stripping comment lines first; we scan the CODE body only.
# NOTE (bean qou-akb4, class 1): the former `ARCH` marker regex lived here and
# listed `\bnorm_num\b` as an archimedean marker.  It was wrong — `norm_num`
# discharges a concrete numeric goal over ANY semiring, and closing `2 + 2 = 4`
# in ℕ does not cross the substrate→archimedean wall, so it produced §7c
# advisories that were routinely dispositioned "not a defect".
#
# It was ALSO already dead: the §7c checks below use `JUST`, which correctly
# omits `norm_num`, and `ARCH` was referenced nowhere (verified: one occurrence
# in the file, its own definition, with no `eval`/indirect expansion).  Removed
# rather than repaired, so it cannot be wired back in and silently reintroduce
# the false positive.  `linarith`/`positivity`/`nlinarith` remain defensible
# markers in `JUST` — they want an order; `norm_num` alone does not.

action=0
echo "check-sidecars: ${#files[@]} changed file(s)"
echo

for f in "${files[@]}"; do
  [ -f "$f" ] || continue
  case "$f" in
    # ANY .lean under content/ — the branch below already distinguishes a
    # content-block sibling (has .md/.ts) from standalone library Lean, so
    # the path pattern must not pre-filter.
    #
    # It used to read `content/*/lean/*.lean|content/*lean*/*.lean`, which
    # requires the literal path component `lean/`. Content-block Lean does
    # NOT live under one — it sits beside its .md/.ts, e.g.
    # `content/<paper>/braids-and-knots/bar-involution.lean`. Those matched
    # no branch at all (there is no default `*.lean` case), so a .lean-only
    # edit to a content block silently escaped the sidecar-staleness gate:
    # 941 sidecar-carrying blocks were invisible to it. Caught when a
    # 53-file swarm reported "0 blocks needing refresh" while every one of
    # those 53 sidecars was in fact stale on source_hashes.lean.
    content/*.lean)
      base="${f%.lean}"
      if [ -f "$base.md" ] || [ -f "$base.ts" ]; then
        # Content-block Lean — has (or should have) a .qa.json sidecar.
        qa="$base.qa.json"
        echo "▸ $f  [content-block Lean]"
        if [ -f "$qa" ]; then
          crits=$(grep -oE '"(q-usage-[a-z0-9-]+|wall-side-correct|[a-z-]+-statement-integrity|da-[a-z0-9-]+|one-voice-[a-z0-9-]+)"' "$qa" 2>/dev/null | tr -d '"' | sort -u | paste -sd', ' -)
          echo "    sidecar: $qa"
          echo "    criteria: ${crits:-<none cached>}"
        else
          echo "    ⚠ NO sidecar yet"; action=1
        fi
        echo "    → refresh: bun run folio-assistant/content/pipeline/qa-sweep.ts $base"
      else
        # STANDALONE library Lean — covered by the per-block checker ONLY if some content
        # block's `lean.ref` resolves here (candidate-2); a library file referenced by NO
        # block is an ORPHAN and escapes the block-driven sweep (the real §7c hole —
        # folio-assistant's q-usage-audit now sweeps orphans content-based). This authoring
        # gate mirrors that with CONTENT-BASED checks (NOT a path heuristic — a path heuristic
        # over-fires on catch-all dirs like BraidKnot/; see the audit). Strip /- -/ + -- first.
        # Comment stripping, in three passes. The FIRST pass is load-bearing and
        # was missing (bean qou-akb4, class 3 — the dominant defect):
        #
        # `sed '\#/-#,\#-/#d'` is a RANGE delete. Given a complete one-line
        # docstring `/-- Archimedean shim of markovZ. -/` it opens the range on
        # that line and then searches the FOLLOWING lines for `-/` — the closer
        # on the same line does not end it. So everything from a one-line
        # docstring to the next block-comment terminator was deleted AS IF IT
        # WERE COMMENT, including the declarations in between.
        #
        # Measured over the 3037 `.lean` files under `content/`: 1578 of them
        # (52%) lost at least one declaration, 5723 declarations and 54213 code
        # lines in total, invisible to every §7c check below. Worked case:
        # `BraidKnot/HoefsmitV21CosSymmetrization.lean` (329 lines -> 161) lost
        # `noncomputable def markovZ_real (q : ℝ) (_hq : 0 < q)`, so the file
        # read as archimedean-only and flagged §7c MIXED while in fact carrying
        # the prescribed generic + `_real` pair the branch below now recognises.
        #
        # Pass 1 removes complete one-line `/- ... -/` blocks; pass 2 is the
        # range delete, now seeing only genuinely multi-line comments; pass 3
        # takes `--` line comments. `@` is the delimiter because the pattern
        # contains `|`.
        body=$(sed -E 's@/-([^-]|-+[^-/])*-+/@@g' "$f" \
               | sed '\#/-#,\#-/#d' | sed 's|--.*||')
        GEN='(\{R\s*:\s*Type|\[CommRing|\[Field\b|\[GroupWithZero|\(R\s*:=)'
        RTYPE='(:\s*ℝ|\(ℝ\)|→\s*ℝ|ℝ\s*\))'      # ℝ used as a type
        # Genuine archimedean JUSTIFICATION (a statement that actually needs ℝ):
        JUST='(Real\.(sqrt|rpow|log|exp|cos|sin|pi|tan|arctan)|0\s*<|<\s*1|≤|≥|\blinarith\b|\bpositivity\b|\bnlinarith\b|LinearOrdered|CODATA|MeV)'
        printf '%s\n' "$body" | grep -qE "$RTYPE" && hasR=1   || hasR=0
        printf '%s\n' "$body" | grep -qE "$JUST"  && hasJ=1   || hasJ=0
        printf '%s\n' "$body" | grep -qE "$GEN"   && hasGen=1 || hasGen=0
        # §7c `_real`-suffix convention (bean qou-akb4, class 2): a generic
        # declaration `foo` sitting beside its archimedean specialisation
        # `foo_real` is the PRESCRIBED §7c pattern — the generic result and the
        # ℝ-instantiation that consumes it — not a file that needs splitting.
        # Detect the pair and downgrade to informational.  The undiscriminated
        # MIXED flag stays for every other file: the discrimination is the
        # useful half, so this narrows the branch rather than silencing it.
        decls=$(printf '%s\n' "$body" \
          | grep -oE '^[[:space:]]*(noncomputable[[:space:]]+)?(theorem|lemma|def|abbrev|instance)[[:space:]]+[A-Za-z_][A-Za-z0-9_'"'"'.]*' \
          | awk '{print $NF}' | sort -u)
        pairedReal=0
        for d in $decls; do
          case "$d" in
            *_real)
              if printf '%s\n' "$decls" | grep -qx "${d%_real}"; then pairedReal=1; break; fi
              ;;
          esac
        done
        if [ "$hasGen" = 1 ] && { [ "$hasR" = 1 ] || [ "$hasJ" = 1 ]; } && [ "$pairedReal" = 1 ]; then
          echo "▸ $f  [§7c generic + _real specialisation — prescribed pattern, informational]"
        elif [ "$hasGen" = 1 ] && { [ "$hasR" = 1 ] || [ "$hasJ" = 1 ]; }; then
          echo "▸ $f  [⚠ §7c MIXED generic + archimedean → split into two files per §7c]"
          printf '%s\n' "$body" | grep -nE "$RTYPE|$JUST" | head -6 | sed 's/^/         /'
          action=1
        elif [ "$hasR" = 1 ] && [ "$hasJ" = 0 ]; then
          echo "▸ $f  [⚠ §7c base-ring-minimal: ℝ in type but NO archimedean construct → likely gratuitous; generalize to {R}/[Field R]]"
          printf '%s\n' "$body" | grep -nE "$RTYPE" | head -6 | sed 's/^/         ℝ: /'
          action=1
        elif [ "$hasR" = 1 ] || [ "$hasJ" = 1 ]; then
          echo "▸ $f  [library Lean — archimedean construct present, ℝ justified (no sidecar; confirm if referenced by a block)]"
        else
          echo "▸ $f  [library Lean — no ℝ, generic OK]"
        fi
      fi
      ;;
    # Pipeline / schema code under content/ is not a content block — it has no
    # .md sibling and no sidecar, so the arm below would print a bogus
    # "(no sidecar yet)" and a qa-sweep line that cannot do anything.
    content/pipeline/*|content/schema/*|content/values/*)
      echo "▸ $f  [content-tree code — not a block, no sidecar applies]"
      ;;
    content/*.md|content/*.ts)
      base="${f%.*}"
      qa="$base.qa.json"
      # A chapter/paper MANIFEST is `<dir>/<dir>.ts` with no `.md` sibling — it
      # lists blocks, it is not one. 47 of them exist, and without this the arm
      # below reports "(no sidecar yet)" and prints a qa-sweep line that cannot
      # do anything. Same misclassification as the content-tree code arm above.
      if [ ! -f "$base.md" ] && [ "$(basename "$base")" = "$(basename "$(dirname "$base")")" ]; then
        echo "▸ $f  [chapter/paper manifest — lists blocks, is not one; no sidecar applies]"
        continue
      fi
      echo "▸ $f  [content block]"
      if [ -f "$qa" ]; then
        crits=$(grep -oE '"(q-usage-[a-z0-9-]+|wall-side-correct|one-voice-[a-z0-9-]+|da-[a-z0-9-]+|[a-z-]+-integrity|remark-[a-z-]+)"' "$qa" 2>/dev/null | tr -d '"' | sort -u | paste -sd', ' -)
        echo "    sidecar criteria: ${crits:-<none cached>}"
      else
        echo "    (no sidecar yet)"
      fi
      echo "    → bun run folio-assistant/content/pipeline/qa-sweep.ts $base   (refresh stale criteria)"
      ;;
    computations/*.py)
      echo "▸ $f  [compute producer]"
      echo "    → LP/SDP? run python computations/lp_dual_witness_validator.py ; re-run producer to refresh *.witness.json"
      # P30 raw-emit guard (bean cmiy): a producer that writes a *.witness.json via a
      # raw json.dump / write_text but never routes through WitnessBuilder emits a witness
      # with NO provenance (engine/scriptFile/commitSha) — it lands as PROV_MISSING in the
      # witness_provenance_audit and defeats staleness detection. Flag it so new raw emits
      # are caught at authoring time instead of being drained batch-by-batch after the fact.
      pybody=$(sed 's|#.*||' "$f")
      emits_witness=$(printf '%s\n' "$pybody" | grep -qE '(json\.dump[s]?\(|\.write_text\()' \
        && printf '%s\n' "$pybody" | grep -qE '\.witness\.json' && echo 1 || echo 0)
      uses_builder=$(printf '%s\n' "$pybody" | grep -qE '(WitnessBuilder|wrap_legacy|stamp_staleness_metadata|witness_base)' && echo 1 || echo 0)
      if [ "$emits_witness" = 1 ] && [ "$uses_builder" = 0 ]; then
        echo "    ⚠ P30: writes a *.witness.json via raw json.dump/write_text with NO WitnessBuilder →"
        echo "         emitted witness will be PROV_MISSING (no engine/scriptFile/commitSha)."
        echo "         Route through WitnessBuilder.wrap_legacy(...).save() (assertion-free payloads)"
        echo "         or WitnessBuilder.stamp_staleness_metadata(payload, script_path=__file__, engine=…)"
        echo "         (payloads carrying a flat 'assertions'/'allPassed'). See bean cmiy / AGENTS.md."
        action=1
      fi
      ;;
    computations/*.witness.json|*/*.witness.json)
      echo "▸ $f  [witness]"
      echo "    → check scriptHash drift (NOT scriptCommitSha — rebase-merge rewrites it; bean qou-wsha)"
      echo "      LP/SDP duals via lp_dual_witness_validator.py"
      ;;
    *) : ;;  # no known sidecar axis
  esac
done

echo
# Author-note Lean-coverage freshness (drift gate; PR #3490 mechanism).
# The advertised proved-counts drift whenever a proof or conjecture
# lands; refresh-authors-note.ts --check recomputes from the live tree.
# Soft-skip when bun or the folio-assistant platform link is missing.
if command -v bun >/dev/null 2>&1 && [ -e "$(dirname "$0")/../folio-assistant" ]; then
  if ! bun run "$(dirname "$0")/refresh-authors-note.ts" --check >/dev/null 2>&1; then
    action=1
    echo "▸ authors-note Lean-coverage stats STALE (proved-counts drifted)"
    echo "    → bun run scripts/refresh-authors-note.ts   (rewrites note + lean-coverage.json; commit both)"
  fi
else
  echo "  (authors-note drift check skipped: bun or folio-assistant/ missing — scripts/setup-folio-assistant.sh)"
fi

echo
# Soundness / vacuity of quantified statements (bean qou-7t1n).
#
# `#print axioms` reports which axioms a proof DEPENDS ON, not whether they
# are jointly SATISFIABLE — nothing else in this repo checks the latter. On
# 2026-08-08 that gap was hiding four axioms that each proved `False`
# (b1_hyperbolic_rows, schrijver_strong_duality,
# schrijver_complementary_slackness, dressed_mass_split_substrate_closed_form),
# every one behind clean-looking audits, in files whose citations were apt.
#
# Run here rather than only in CI because CI is workflow_dispatch-only
# (owner directive 2026-06-30), so a script nobody invokes catches nothing.
if command -v python3 >/dev/null 2>&1; then
  audit="$(dirname "$0")/lean-one-sided-binder-audit.py"
  if [ -f "$audit" ]; then
    audit_out=$(python3 "$audit" 2>/dev/null || true)
    # Print the whole report rather than a sed slice: the findings sit below
    # a blank line after each section header, so a `/^UNSOUND/,/^$/` range
    # shows the header and drops the actual file list — which is the only
    # part worth reading.
    if printf '%s\n' "$audit_out" | grep -qE "^(UNSOUND|ADVISORY)"; then
      action=1
      if printf '%s\n' "$audit_out" | grep -q "^UNSOUND"; then
        echo "🛑 UNSOUND quantified statement(s) — these prove False. Fix before commit."
      else
        echo "▸ soundness audit: unconditional claim(s) over an arbitrary structure."
        echo "  Fatal iff the related fields are independent — read the structure."
      fi
      printf '%s\n' "$audit_out" | sed 's/^/    /'
    fi
  fi
fi

# ── canonical-mass status guard ───────────────────────────────────────────────
# Runs when the change touches a surface the guard covers: production compute
# docstrings (computations/**.py), the authoritative paper (content/**.md), or a
# live reference doc (docs/**.md).
#
# Hosted HERE rather than in CI on purpose. Every workflow in .github/workflows
# is `workflow_dispatch`-only (auto-triggers disabled repo-wide, 2026-06-30,
# Actions billing), so a CI job for this guard would never fire on a push and
# would only look like coverage. This script is the path agents actually walk
# before committing — AGENTS.md §"QA is agent-owned; CI is a backup".
#
# The guard is stdlib-only (ast/re/hashlib), so it adds no dependency to the
# preflight. Its two regression suites need mpmath and are NOT run here; run
# them directly when touching the guard itself:
#   python3 computations/canonical_mass_status_guard_test.py
#   python3 computations/canonical_mass_table_nucleon_rows_test.py
if printf '%s\n' "${files[@]}" | grep -qE '^(computations/.*\.py|(content|docs)/.*\.md)$'; then
  guard="computations/canonical_mass_status_guard.py"
  if [ -f "$guard" ]; then
    if ! guard_out=$(python3 "$guard" --strict 2>&1); then
      action=1
      echo "⚠ canonical-mass status guard: a DEPRECATED absolute-mass figure is cited as live status."
      echo "  Live m_p is CODATA +1.35 ppb via the canonical_mass facade; 2.89%/966/406/−57% are the"
      echo "  Vol(𝓑₃)·ρ forms. See docs/canonical-mass-formula-guardrail.md."
      printf '%s\n' "$guard_out" | sed 's/^/    /'
    fi
  fi
fi

# Block-manifest load check (block-manifest-audit).
#
# `run-validate` walks the CHAPTER manifests' block lists, never the filesystem,
# so a `<block>.ts` that fails to import, exports no `default`, or carries a
# label the schema rejects is not a validation error — the block is simply
# invisible. It is absent from the rendered paper AND skipped by every
# per-block QA checker, with validation still green. Five blocks were in that
# state on 2026-08-15, three of them since June/July, each announced as landed
# by its commit message. This is the gate that catches the sixth.
if printf '%s\n' "${files[@]}" | grep -qE '^content/.*\.(md|ts)$'; then
  mapfile -t blockfiles < <(printf '%s\n' "${files[@]}" | grep -E '^content/.*\.(md|ts)$')
  if ! bma_out=$(bun run --preload "$ROOT/scripts/preload-registry.ts" \
        "$ROOT/content/pipeline/block-manifest-audit.ts" --diff "${blockfiles[@]}" 2>&1); then
    action=1
    echo "⚠ block-manifest-audit: a changed block's manifest does not load."
    printf '%s\n' "$bma_out" | sed 's/^/    /'
  fi
fi

echo
if [ "$action" -eq 1 ]; then
  echo "⚠ check-sidecars: action needed above. Resolve §7c markers / refresh sidecars BEFORE commit."
else
  echo "check-sidecars: no un-sidecar'd §7c flags. Still run qa-sweep on any content blocks listed."
fi
exit 0
