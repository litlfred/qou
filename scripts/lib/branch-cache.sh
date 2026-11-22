# shellcheck shell=bash
# Common infrastructure for qou's branch caches: the cat-harness `family`
# storage keying that `lake-cache`, `wheel-cache`, `trace-cache` and the caches
# migrated after them share.
#
# SOURCE IT; do not run it. `scripts/branch-cache.sh` is the command-line face
# of the same functions, and `computations/_branch_cache.py` is the Python twin
# (it calls that CLI, so there is one implementation of every rule below).
#
# THE RULES, one place:
#   * The family prefix is READ from qou.json: the `directories[]` entry whose
#     `graphTypologies` names the kind and whose `storage.keyedBy` is "family".
#     No fallback: a family nobody declared is not a cache.
#   * A member is one orphan branch `<branchPrefix><member>`. Its name is the
#     caller's key; the caller decides what goes in it.
#   * A SOURCE KEY is the first 12 hex of sha256 over the lines
#     "<dir> <git tree id at HEAD>\n", in the order given. A dirty source tree
#     has no key ("undetermined: ..."), so it never restores a value built from
#     other sources and never seeds one.
#   * Git objects live in a PRIVATE bare repository,
#     `<git-common-dir>/<kind>.git`, never in the checkout's object store.
#   * A push is NEVER forced. A member is never deleted (AGENTS.md rule 9).
#   * Every member carries `manifest.json` whose `$schema` is
#     `<kind>-member/v1` and whose `member` is the branch's own member name,
#     and every stored file is listed there with its sha256, checked on restore.
#
# Two member layouts:
#   single   one blob plus manifest.json and README.md, written once
#            (bc_seed_single; used by wheel-cache).
#   sharded  manifest.json lists content-addressed `shards/<sha256>.jsonl`; a
#            seed ADDS a shard as a new commit on the tip and, if another
#            writer moved the tip first, refetches and re-applies
#            (bc_shard_restore / bc_shard_seed; used by trace-cache and the
#            Python twin).
#
# Exit codes every caller inherits:
#   0 hit / seeded / already present   1 miss   2 usage or environment
#   3 undetermined or corrupt or unreachable — never a hit.

[ -n "${BC_LIB_LOADED:-}" ] && return 0
BC_LIB_LOADED=1

bc_die() { echo "${BC_KIND:-branch-cache}: $1" >&2; exit "${2:-2}"; }

bc_root() { git -C "$(dirname "${BASH_SOURCE[0]}")/../.." rev-parse --show-toplevel; }

# bc_prefix <kind>  -> prints the declared branchPrefix; returns 1 if undeclared.
bc_prefix() {
  local p
  p="$(python3 - "$(bc_root)/qou.json" "$1" <<'PY' 2>/dev/null
import json, sys
for e in json.load(open(sys.argv[1])).get("directories", []):
    st = e.get("storage") or {}
    if sys.argv[2] in (e.get("graphTypologies") or []) and st.get("keyedBy") == "family":
        print(st["branchPrefix"]); break
PY
)"
  [ -n "$p" ] || return 1
  echo "$p"
}

# bc_init <kind> — sets BC_KIND and BC_PREFIX, or dies.
bc_init() {
  BC_KIND="$1"
  BC_PREFIX="$(bc_prefix "$1")" || bc_die "qou.json declares no $1 family"
}

bc_remote_url() { git remote get-url origin; }

bc_bare() {
  local b; b="$(git rev-parse --path-format=absolute --git-common-dir)/${BC_KIND}.git"
  [ -d "$b" ] || git init -q --bare "$b" || return 1
  echo "$b"
}

# bc_source_key <label> <dir>... -> 12 hex, or "undetermined: <label> differ
# from HEAD" and return 3.
bc_source_key() {
  local label="$1" dirty d trees=""; shift
  dirty="$(git status --porcelain -- "$@")"
  if [ -n "$dirty" ]; then echo "undetermined: $label differ from HEAD"; return 3; fi
  for d in "$@"; do trees+="$d $(git rev-parse "HEAD:$d")"$'\n'; done
  printf '%s' "$trees" | sha256sum | cut -c1-12
}

# bc_source_trees_json <dir>... -> {"dir": "<tree id>", ...} on one line.
bc_source_trees_json() {
  python3 - "$@" <<'PY'
import json, subprocess, sys
print(json.dumps({s: subprocess.check_output(["git", "rev-parse", f"HEAD:{s}"], text=True).strip()
                  for s in sys.argv[1:]}))
PY
}

bc_list() {
  git ls-remote --heads "$(bc_remote_url)" "${BC_PREFIX}*" | sed "s#.*refs/heads/${BC_PREFIX}##"
}

# bc_present <branch> -> 0 present, 1 absent, 3 unreachable.
bc_present() {
  local ls
  ls="$(git ls-remote --heads "$(bc_remote_url)" "$1" 2>/dev/null)" || return 3
  [ -n "$ls" ]
}

# bc_fetch_member <branch> -> prints the commit; 1 absent, 3 unreachable.
bc_fetch_member() {
  local br="$1" B rc
  bc_present "$br"; rc=$?
  [ $rc -eq 3 ] && { echo "$BC_KIND: could not reach origin (unknown, not a miss)" >&2; return 3; }
  [ $rc -eq 0 ] || return 1
  B="$(bc_bare)" || return 2
  git -C "$B" fetch -q --depth=1 "$(bc_remote_url)" "refs/heads/$br" 2>/dev/null \
    || { echo "$BC_KIND: fetch of $br failed (unknown, not a miss)" >&2; return 3; }
  git -C "$B" rev-parse FETCH_HEAD
}

bc_commit_tree() {   # bc_commit_tree <tree> <subject> <body> [parent]
  local B; B="$(bc_bare)" || return 2
  local pflag=(); [ -n "${4:-}" ] && pflag=(-p "$4")
  git -C "$B" -c user.name="${GIT_AUTHOR_NAME:-qou $BC_KIND}" \
      -c user.email="${GIT_AUTHOR_EMAIL:-noreply@anthropic.com}" \
      commit-tree "$1" "${pflag[@]}" -m "$2" -m "$3"
}

bc_push() {   # bc_push <commit> <branch>  — never forced
  local B; B="$(bc_bare)" || return 2
  git -C "$B" push -q "$(bc_remote_url)" "$1:refs/heads/$2"
}

# ── single layout ────────────────────────────────────────────────────────

# bc_seed_single <member> <file> <manifest-json> <readme> <subject> <body>
# The member must not exist yet (the caller checks; a race loses cleanly).
bc_seed_single() {
  local m="$1" file="$2" man="$3" readme="$4" subj="$5" body="$6" B hw hm hr tree commit name
  B="$(bc_bare)" || return 2
  name="$(basename "$file")"
  hw="$(git -C "$B" hash-object -w "$file")" || return 2
  hm="$(printf '%s\n' "$man" | git -C "$B" hash-object -w --stdin)" || return 2
  hr="$(printf '%s\n' "$readme" | git -C "$B" hash-object -w --stdin)" || return 2
  tree="$(printf '100644 blob %s\tREADME.md\n100644 blob %s\tmanifest.json\n100644 blob %s\t%s\n' \
           "$hr" "$hm" "$hw" "$name" | git -C "$B" mktree)" || return 2
  commit="$(bc_commit_tree "$tree" "$subj" "$body")" || return 2
  bc_push "$commit" "$BC_PREFIX$m" \
    || { echo "$BC_KIND: push of $BC_PREFIX$m refused (another seed may have won; that is fine)" >&2; return 3; }
  echo "$BC_KIND: seeded $BC_PREFIX$m" >&2
}

# ── sharded layout ───────────────────────────────────────────────────────

# bc_shard_restore <member> <outdir> -> writes <outdir>/manifest.json and
# <outdir>/shards/*.jsonl, every shard sha256-checked.
bc_shard_restore() {
  local m="$1" out="$2" br C rc B
  br="$BC_PREFIX$m"
  C="$(bc_fetch_member "$br")"; rc=$?
  [ $rc -eq 1 ] && { echo "$BC_KIND: miss $br" >&2; return 1; }
  [ $rc -eq 0 ] || return "$rc"
  B="$(bc_bare)" || return 2
  git -C "$B" show "$C:manifest.json" > "$out.manifest.tmp" 2>/dev/null \
    || { echo "$BC_KIND: corrupt $br: no manifest.json" >&2; rm -f "$out.manifest.tmp"; return 3; }
  mkdir -p "$out/shards" || return 2
  python3 - "$BC_KIND" "$m" "$out.manifest.tmp" "$B" "$C" "$out/shards" <<'PY' || { rm -f "$out.manifest.tmp"; return 3; }
import hashlib, json, os, subprocess, sys
kind, member, man, bare, commit, outdir = sys.argv[1:]
d = json.load(open(man))
if d.get("$schema") != f"{kind}-member/v1" or d.get("member") != member:
    sys.exit(f"{kind}: corrupt: manifest names {d.get('member')!r}")
for s in d.get("shards", []):
    name = s["file"]
    if "/" in name or name.startswith(".") or not name.endswith(".jsonl"):
        sys.exit(f"{kind}: corrupt: bad shard name {name!r}")
    blob = subprocess.run(["git", "-C", bare, "cat-file", "blob", f"{commit}:shards/{name}"],
                          capture_output=True, check=False).stdout
    if hashlib.sha256(blob).hexdigest() != s["sha256"]:
        sys.exit(f"{kind}: corrupt: sha256 of {name} does not match")
    with open(os.path.join(outdir, name), "wb") as f:
        f.write(blob)
print(f"{kind}: restored {len(d.get('shards', []))} shard(s)", file=sys.stderr)
PY
  mv "$out.manifest.tmp" "$out/manifest.json"
  echo "$BC_KIND: hit $br" >&2
}

# bc_shard_seed <member> <shard.jsonl> <meta-json> <readme>
#   meta-json: a JSON object of the kind's own manifest fields, placed after
#   `$schema` and `member` and before `shards`, in the order given.
# Adds the shard (if not already listed) as a new commit on the member's tip.
bc_shard_seed() {
  local m="$1" shard="$2" meta="$3" readme="$4" br B sha name hs attempt C rc parent oldf man hm hr stree tree commit
  br="$BC_PREFIX$m"; B="$(bc_bare)" || return 2
  sha="$(sha256sum "$shard" | cut -d' ' -f1)"; name="$sha.jsonl"
  hs="$(git -C "$B" hash-object -w "$shard")" || return 2
  for attempt in 1 2 3 4 5; do
    C="$(bc_fetch_member "$br")"; rc=$?
    case $rc in 0) parent="$C" ;; 1) parent="" ;; *) return "$rc" ;; esac
    oldf="$(mktemp)"; echo '{}' > "$oldf"
    [ -n "$parent" ] && git -C "$B" show "$parent:manifest.json" > "$oldf"
    man="$(python3 - "$BC_KIND" "$m" "$name" "$sha" "$shard" "$oldf" "$meta" <<'PY'
import json, subprocess, sys, datetime
kind, m, name, sha, shard, oldf, meta = sys.argv[1:]
old = json.load(open(oldf))
shards = old.get("shards", [])
if any(s["file"] == name for s in shards):
    print("PRESENT"); sys.exit(0)
entries = sum(1 for line in open(shard) if '"v":' in line)
shards.append({"file": name, "sha256": sha, "entries": entries,
               "addedAt": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
               "addedFrom": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()})
out = {"$schema": f"{kind}-member/v1", "member": m}
out.update(json.loads(meta))
out["shards"] = shards
print(json.dumps(out, indent=2))
PY
)"; rc=$?; rm -f "$oldf"
    [ $rc -eq 0 ] || { echo "$BC_KIND: could not write the manifest" >&2; return 2; }
    if [ "$man" = "PRESENT" ]; then echo "$BC_KIND: $name already in $br" >&2; return 0; fi
    hm="$(printf '%s\n' "$man" | git -C "$B" hash-object -w --stdin)" || return 2
    hr="$(printf '%s\n' "$readme" | git -C "$B" hash-object -w --stdin)" || return 2
    stree="$( { [ -n "$parent" ] && git -C "$B" ls-tree "$parent:shards"; \
                printf '100644 blob %s\t%s\n' "$hs" "$name"; } | git -C "$B" mktree)" || return 2
    tree="$(printf '100644 blob %s\tREADME.md\n100644 blob %s\tmanifest.json\n040000 tree %s\tshards\n' \
             "$hr" "$hm" "$stree" | git -C "$B" mktree)" || return 2
    commit="$(bc_commit_tree "$tree" "$BC_KIND: add shard $name to $m" \
             "From qou $(git rev-parse HEAD)." "$parent")" || return 2
    if bc_push "$commit" "$br" 2>/dev/null; then
      echo "$BC_KIND: seeded $name into $br" >&2; return 0
    fi
    echo "$BC_KIND: push of $br refused (attempt $attempt); refetching" >&2
    sleep "$attempt"
  done
  echo "$BC_KIND: gave up seeding $br after 5 attempts" >&2; return 3
}
