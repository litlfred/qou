---
name: sandbox-egress
description: Egress workarounds for firewalled sandboxes — github.com clones and PyPI work when a tool's own data host 403s. Route table + worked examples (mathlib, SnapPy/ptolemy). Read before declaring an external resource unreachable.
roles:
  - reader
  - collaborator
  - owner
---

# Sandbox egress — what's open, what's blocked, and the mirror route

**Rule (mirrors the AGENTS.md "route, don't give up" STRICT rule): a 403/
blocked-host error from a tool's OWN download path does NOT mean the data is
unreachable.** The sandbox proxy allowlists a few big hosts; most
project-specific data hosts are blocked. Before declaring an external
resource unavailable, walk the route table below.

## ALWAYS TRY github.com FIRST — and probe it correctly

**github.com is open for git.** Before concluding anything else, try the clone.
A public repo needs no attachment and no credentials: the session's git proxy
serves anonymous reads directly.

```sh
GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 \
    https://github.com/<owner>/<repo> /home/user/<owner>/<repo>
```

Give it a **generous timeout (~10 min)**. A large shallow pack takes 5–10
minutes through the proxy and `git index-pack` looks stalled while unpacking.
Do not interrupt it, do not re-run it, and do not run two clones at once. The
`GIT_LFS_SKIP_SMUDGE=1` prefix is load-bearing: the anonymous lane does not
serve LFS objects, so an unprefixed clone of an LFS repo ABORTS at the smudge
filter. With it, LFS files arrive as pointer stubs — say so if the real
contents are needed.

### 🛑 DO NOT probe with `curl https://github.com` — it returns 400 and means nothing

Measured 2026-08-29, in a session where cloning github.com **worked**:

| probe | result | what it means |
|---|---|---|
| `curl https://github.com` | **HTTP 400** | the PROXY refusing a pathless request — `{"message": "Request path could not be canonicalized."}`. **NOT a block.** |
| `curl https://github.com/<owner>/<repo>` | HTTP 404 | web UI is not served; says nothing about git |
| `curl https://raw.githubusercontent.com/...` | HTTP 404 | not served on this lane despite the row below |
| `curl https://github.com/<o>/<r>/info/refs?service=git-upload-pack` | **HTTP 200** | **the git protocol works — this is the correct probe** |
| `curl https://api.github.com` | **HTTP 200** | API host reachable |

An agent that probes the bare host, sees 400, and reports "github.com is
blocked" is wrong, and the clone it declined would have succeeded. Probe with
`/info/refs?service=git-upload-pack`, or simply attempt the clone — the clone
is cheap to try and is the thing you actually want.

`git ls-remote` is also a valid probe, with the caveat in route 1 below.

## If github.com is genuinely unreachable — escalate with instructions, do not just report failure

Only after the `/info/refs` probe or an actual clone attempt fails. Do not
escalate off a bare-host 400.

Tell the author (Yoon) **what to open and how**, not merely that something is
blocked. Include, concretely:

1. **The exact host and path** that failed, and the probe you ran verbatim.
2. **The observed result** — status code and body, or the git error.
3. **`curl -sS "$HTTPS_PROXY/__agentproxy/status"`** output, which reports
   `enabled`, `selective`, `toolScoped` and the `noProxy` list. `selective:
   true` means an allowlist is in force and the host must be added to it;
   `selective: false` means the block is elsewhere and the allowlist is not
   the lever.
4. **The remedy, named**: for a Claude Code on the web session the network
   policy is chosen when the ENVIRONMENT is created, so opening a host means
   editing that environment's network policy — not a per-session setting an
   agent can change. Point at
   <https://code.claude.com/docs/en/claude-code-on-the-web> and say which
   policy the work needs.
5. **What you did instead**, so the escalation is not a dead end: the route
   table below, and what you got working without the blocked host.

Never disable TLS verification, never unset `HTTPS_PROXY`, and never propose
either as the fix.

## What is open (verified, 2026-08-15; github rows re-measured 2026-08-29)

| Channel | Status | Evidence |
|---|---|---|
| `github.com` git clone / ls-remote / fetch | **OPEN** | mathlib4 shallow clone (AGENTS.md fallback); `3-manifolds/SnapPy`; `litlfred/folio-assistant` shallow clone 2026-08-29 (17 MB, `2d63a7a`) |
| `github.com` **push** to an UNATTACHED repo | **NOT available** | the anonymous lane is read-only; use `add_repo` with `access:"push"` to attach with credentials |
| `api.github.com` | **OPEN** (HTTP 200) | re-measured 2026-08-29 |
| PyPI (`pip install`) | **OPEN** | `pip install snappy` (3.3.2 + 30 deps) worked first try |
| `raw.githubusercontent.com` | **404 on this lane** — do NOT rely on it | re-measured 2026-08-29; the old "usually open" row was wrong. Clone the repo instead. |
| WebSearch (MCP) | OPEN (out-of-band) | used to locate repos |

## What is blocked (and does NOT mean "give up")

| Host | Blocked path | Working route |
|---|---|---|
| `release.lean-lang.org` | elan toolchain download | GitHub release asset (allowlisted) — see `lean-environment-setup.md` |
| Mathlib olean cache server (`lake exe cache get` 403) | prebuilt oleans | `lake-cache/*` orphan branches in THIS repo, or local mathlib clone |
| `ptolemy.unhyperbolic.org` | SnapPy `retrieve_solutions()` (403 on CONNECT) | **the snappy wheel itself ships certified magma fixtures** — see below |
| Arbitrary hosts via WebFetch (MCP) | `EGRESS_BLOCKED` | WebFetch rides the same proxy — do not assume it is out-of-band for data hosts |
| `arxiv.org` / `export.arxiv.org` | any paper fetch | **no route — escalate.** Measured 2026-09-13: `403 Host not in allowlist: arxiv.org.` |
| `www.numdam.org` (and `aif.centre-mersenne.org`) | open-access journal PDFs | **no route — escalate.** Measured 2026-09-13: `403 Host not in allowlist: www.numdam.org.` |

### 🛑 Document intake is NOT possible in this environment — and that is a statement about EVERY paper, not about one host

The two rows above were measured together on 2026-09-13, and the pair is what
matters: **`arxiv.org` is blocked as well**, so there is no such thing here as
"this particular paper's host happens to be shut." The `document-intake` /
`paper-importer` skills assume a fetch that cannot happen, and the route table
above has **no route for a journal PDF** — it is not on a git repo (route 1),
not bundled in a wheel (route 2), and the fetch has no data-URL override
(route 3). Do not spend a pass re-probing mirrors; go straight to route 5 and
escalate with the host named.

Controls measured in the same session, so this is an allowlist and not a dead
network: `github.com` git `/info/refs?service=git-upload-pack` **200**,
`pypi.org/simple/` **200**. Note the proxy reports `selective: false` while the
gateway answers with an allowlist denial naming the host — so **do not read
`selective: false` as "the allowlist is not the lever"** (the escalation
checklist above says exactly that, and on this evidence it is wrong); read the
403 body, which names the host to add.

Worked case: bean `qou-denm` (ingest Kohno 1987, Ann. Inst. Fourier 37 —
open access on NUMDAM, DOI 10.5802/aif.1075). Unobtainable here for egress
reasons, not licensing ones. The bean carries the measurement and what a
network-open environment should run.

## The route table (try in order)

1. **Is the data on a GitHub repo?** Clone it (`--depth 1`). WebSearch for
   `<project> github repository` to find the name; `git ls-remote
   https://github.com/<owner>/<repo>.git HEAD` is a cheap existence probe
   (public repos answer; remember private repos 404 unauthenticated).
2. **Is the data bundled in a pip package?** Many projects ship regression
   fixtures inside the wheel. Worked example: SnapPy's
   `snappy/ptolemy/testing_files/` contains **certified Magma
   primary-decomposition outputs for the `4_1` and `5_2` sl2 ptolemy
   varieties** — the exact data the firewalled ptolemy DB would have
   served — processable with
   `snappy.ptolemy.processMagmaFile.solutions_from_magma`. Consumed by
   `computations/qbeta/dt_crossknot_connection_count_certified_probe.py`
   (R1 connection counts 3/4, previously literature recall).
3. **Does the tool honor a data-URL env override?** SnapPy:
   `PTOLEMY_DATA_URL` (point at a local mirror / `file://` path). Lake:
   the `insteadOf` git redirect. Check the tool's source for
   `os.environ` reads before giving up.
4. **Proxy self-diagnosis**: `curl -sS "$HTTPS_PROXY/__agentproxy/status"`
   lists per-tool fixes and proxy state (see `/root/.ccr/README.md`).
   Never disable TLS verification or unset `HTTPS_PROXY`.
5. **Still blocked?** Record the residual precisely in the bean (which
   host, which path, what a network-open environment should run) — the
   qou-btvl handoff-note pattern.

## History

- 2026-08-29: the author asked that agents be told to try github.com egress
  and, when it is shut, to hand the author instructions rather than a dead
  end. Measuring it to write the rule turned up the misleading probe: bare
  `curl https://github.com` returns **400** in a session where cloning works,
  because the proxy will not canonicalize a pathless request. An agent using
  that as its reachability test concludes "blocked" and declines a clone that
  would have succeeded — the same shape as the `add_repo` tool's own warning
  not to pre-check with curl, and as `precision-gates.sh --changed` returning
  a green-looking `EXIT=0` on a clean checkout when it has actually skipped.
  Also corrected: `raw.githubusercontent.com` is **404** on this lane, not
  "usually open" as the table claimed since 2026-08-15.
- 2026-08-15: ptolemy DB 403 nearly ended the D3 connection-count
  hardening as "needs open env"; the owner's hint ("egress github.com
  clone repos") led to route 1 → route 2: the data was in the installed
  wheel all along. Counts 3 (4₁) and 4 (5₂) certified locally, trace
  fields cross-checked. Skill created from that session so the next agent
  walks the table instead of stopping at the 403.
