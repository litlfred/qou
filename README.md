# qou-v4-24-0-lean-direct-refresh — addon over `qou-v4-24-0`

Seeded 2026-11-19 by the `lean-verifier` agent from qou `c4a0c309a`
(branch `claude/modest-heisenberg-k201yv`, source = that tree).
**Lean-direct output: plain oleans, NO fresh `.trace`.** Restore with `tar`,
verify with `lean`-direct / `scripts/lean-direct-cone.sh`. **Never `lake build`
over it** — Lake would consult the base seed's (now stale) traces.

## What it holds (paths relative to the repo root, already `folio/…`)

- 3251 `.olean`: 3223 QOU + 28 UGB rebuilt lean-direct from current source
  (`-DautoImplicit=false -s 65536`), i.e. every library module whose olean in
  the base seed `a792c46` did not match its current source, plus its import
  closure (and modules the cone builder's dep-mtime rule re-ran).
- 28 `.ilean` (UGB only; the QOU cone builder writes none — QOU ileans in the
  base seed are stale for rebuilt modules; they only matter to the LSP).
- 3324 `.srcsha` stamps (sha256 of the source each olean was built from), read
  by `scripts/lean_freshness.py`, so `lean-direct-cone.sh` and
  `lean-axiom-guard.py` decide freshness by content. 312 of them stamp base-seed
  oleans whose Lake `.trace` source hash equals the current source hash.

Not included: the QOU root aggregator `QOU.olean` — `QOU.lean` is red at
`c4a0c309a` (`QOU.Tetraplectic.unitJ` declared in both
`QOU/BringConeGauge.lean:60` and `QOU/BringConeIcosahedral.lean:45`).

## Restore (after the base seed)

```sh
ROOT=$(git rev-parse --show-toplevel)
scripts/lean-cache-restore.sh                 # base seed qou-v4-24-0 (a792c46)
scripts/lean-restore-gap-oleans.sh            # Mathlib gap addon (>= bcadf92: 158 oleans)
T=/tmp/addonfetch; rm -rf $T; git init -q $T
git -C $T remote add origin https://github.com/litlfred/qou
git -C $T fetch --depth=1 -q origin cat/folio-assistant-sci/lake-cache/qou-v4-24-0-lean-direct-refresh
C=$(git -C $T rev-parse FETCH_HEAD)
( for p in $(git -C $T ls-tree --name-only $C | grep '^lake-oleans\.tgz\.part' | sort); do
    git -C $T show "$C:$p"; done ) | tar xzf - -C "$ROOT" --unlink-first
echo "PIPESTATUS=${PIPESTATUS[*]}"; rm -rf $T
```

Staleness after restore is decided by the stamps: anything changed on `main`
since `c4a0c309a` is rebuilt by `scripts/lean-direct-cone.sh <Module>`.
