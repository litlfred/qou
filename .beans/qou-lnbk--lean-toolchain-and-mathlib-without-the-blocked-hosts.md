---
# qou-lnbk
title: 'INFRA: build Lean + Mathlib in a sandbox where release.lean-lang.org and the olean cache are blocked'
status: completed
type: task
priority: normal
tags:
    - lean
    - infra
    - mathlib
    - sandbox
created_at: 2026-08-07T18:40:00Z
updated_at: 2026-08-07T18:40:00Z
---


## Problem

Agent sandboxes for this repo often have an egress policy that **denies**:

* `release.lean-lang.org:443` — so `elan` cannot install a toolchain
  (`error during download … CONNECT tunnel failed, response 403`)
* `mathlib4.blob.core.windows.net` — so `lake exe cache get` downloads **0 of
  7335** files and every attempt fails

`github.com` **is** reachable (it is how the repo itself is cloned). That is the
whole opening. Earlier beans (`qou-clx8`) recorded "Lean unavailable here" and
that conclusion was **wrong** — it was a missing workaround, not a hard block.

## Recipe (verified end-to-end 2026-08-07)

**1. Toolchain from the GitHub mirror.** `lean-toolchain` pins
`leanprover/lean4:v4.24.0`; the same build is a GitHub release asset.

```sh
curl -sS -L -o lean.tar.zst \
  https://github.com/leanprover/lean4/releases/download/v4.24.0/lean-4.24.0-linux.tar.zst
```

⚠ Only `.tar.zst` exists (`.tar.gz` 404s), and **there is no `zstd` binary and
no `tar --zstd` support** on the image. Decompress in Python:

```sh
python3 -m pip install zstandard
python3 - <<'PY'
import zstandard, tarfile
with open('lean.tar.zst','rb') as f:
    with zstandard.ZstdDecompressor().stream_reader(f) as r:
        tarfile.open(fileobj=r, mode='r|').extractall('toolchain')
PY
export PATH="$PWD/toolchain/lean-4.24.0-linux/bin:$PATH"
lean --version     # 4.24.0
```

**2. Mathlib source from GitHub, then a TARGETED build.** `lake update` fetches
sources fine (the cache step inside it fails noisily — ignore it, or kill the
`cache get` child, it retries 7335 times).

**Do not run `lake build` bare** — that builds the world. Build the module you
need:

```sh
lake build Mathlib.Tactic.LinearCombination     # 708 jobs, minutes
```

**3. Reuse the build across projects.** The scratch project and this repo pin the
*same* Mathlib rev (`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`, checked in both
`lakefile.toml` and `lake-manifest.json`), so the packages hardlink straight in:

```sh
cp -al /path/to/scratch/.lake/packages content/quantum-observable-universe/lean/.lake/packages
```

`content/*/lean/.lake/` is gitignored (`.gitignore:64`) — confirm with
`git check-ignore -v <path>/.lake/` **and note it only reports correctly once the
directory exists**, which is an easy way to scare yourself into thinking it is
untracked.

## Result

`lake build QOU.QBeta.FiveTwoCyclotomicBloch` — **707 jobs, success, in-tree**,
with `#print axioms` clean. So a sandbox agent *can* write and verify Lean here.

## Known snag

The in-tree build stops to clone `doc-gen4` because the lakefile's `[[require]]`
for it is active despite its comment saying otherwise. Costly but not fatal.
**Tracked separately as `qou-dg4x`, which also explains why the obvious fix
breaks the docs CI.**

## What this does NOT solve

Only *targeted* builds are practical. A full `lake build` of `QOU` still means
compiling Mathlib from source with no cache — hours. If a session needs the whole
library, it needs the cache host unblocked, not this recipe.

## Refs

* corrects `qou-clx8`'s "Lean is blocked here" note
* `qou-dg4x` (doc-gen4 lakefile/CI bug), PR #4658
