---
# qou-6u3n
title: '[TOOLS T13] Retire renderers and deploy into fsh-guts/ (deploy/, paper-builder-image, build-lean-mcp, docs-site.yml,…'
status: in-progress
type: feature
priority: normal
tags:
    - migration
    - tools
created_at: 2026-10-04T16:35:45Z
updated_at: 2026-10-04T18:06:44Z
parent: qou-k3er
---

From the TOOLS migration analysis (2026-10-04), story T13. Full report: docs/audits/2026-10-04-workplan-and-migration/TOOLS_report.md.

| T13 | Retire renderers and deploy into `fsh-guts/` (`deploy/`, `paper-builder-image`, `build-lean-mcp`, `docs-site.yml`, typedoc, `make-all-tables`, `split-pdf`) and move `computations/_deprecated` → `fsh-guts/` | pure renames; `convention-c-deprecated-citation-audit.py` shows 0 content citations into `_deprecated` before the move | S | owner ack on `_deprecated` |

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.



## Progress 2026-10-04

Done (commit 46af43b18): docs-site.yml and docs/_config.yml parked in fsh-guts/deprecated by pure rename. Remaining: deploy/ (needs the owner to stop the live self-updating server first; its access lists are CODEOWNERS-protected), and computations/_deprecated (owner ack). The LaTeX/PDF path is out of scope (owner: ignore, not retire).


2026-10-04 (session_01NdDGeP1SyShmoUssLuRZ91): TypeDoc retired. typedoc.json → fsh-guts/deprecated/docs-site/ (pure rename); build:docs script and typedoc devDependency removed; README points at the platform's gen-schema-docs. Still to do in T13: deploy/ (waits on the owner's server decision), paper-builder-image, build-lean-mcp.yml, make-all-tables, split-pdf, computations/_deprecated.

## 🛑 2026-10-10: the `_deprecated` half's stated EVIDENCE is false, and it cites the wrong audit

Found while re-measuring bean `qou-jyqd` (whose script is the one cited). This is
the content-parity check the "Done-when" above asks for, run on the
`computations/_deprecated` half only.

The T13 row's evidence column reads

> pure renames; `convention-c-deprecated-citation-audit.py` shows 0 content
> citations into `_deprecated` before the move

Both halves are wrong, and the second is the one that matters.

**It does not show 0.** Run on `main` `ac111c1814`, it shows **3**:

| deprecated producer | named by |
|---|---|
| `integer-lp-gluon.py` | `categorical-neutron-properties.{md,ts,qa.json}`, `categorical-proton-properties.ts`, `gluon-stabiliser-ledger.ts` |
| `protium-witness.py` | `mass-theory/binding-scale-catalan.qa.json` |
| `transfer_matrix_symbolic.py` | `mass-theory/markov-trace-factorization.md` |

**And it could not answer this question even at 0.** That audit scans only the
**139 of 568** deprecated producers *carrying a convention-C shape* — it exists
to ask *"does retired convention-C code still reach the content?"*, which is a
narrower question than *"would moving this directory break a content
reference?"*. T13 breaks on **any** reference. Measured directly:

    git grep -l 'computations/_deprecated' -- 'folio/**' | grep -v '\.lake/'
    → 27 files    (11 .json, 7 .ts, 5 .lean, 4 .md)

naming **15 distinct** deprecated producers and witnesses:
`binding-k-enumerator.witness.json`, `bw_wenzl_shadow_equivalence.py`,
`chi-lambda-w0-sign-weighting.witness.json`, `confinement-lp.witness.json`,
`integer-lp-gluon.py`, `meson-nucleon-nf.witness.json`,
`misdp_cross_channel.py`, `multi_level_sdp.py`, `positron_lifted_sdp.py`,
`protium-witness.py`, `q_variant_partition_sum.py`,
`rho-k-pair-gen-v2-wedderburn.witness.json`, `schur-weyl-mn.witness.json`,
`tau-leptonic-decay.witness.json`, `transfer_matrix_symbolic.py`.

### One of the 27 is STRUCTURAL, and it is the only one a validator reads

`folio/quantum-observable-universe/mass-theory/wedderburn-weight-canonical.ts`:

    computation: {
      engine: "python",
      script: "computations/_deprecated/bw_wenzl_shadow_equivalence.py",
      witness: "docs/audits/2026-05-01-p1-3a-bw-equivalence.witness.json",
      status: "verified",
    },

A content block declaring `computation.status: "verified"` against a producer
the corpus deprecated. That is a defect **independent of T13** — it is live on
`main` today — and it is also the single reference the move would break
mechanically rather than textually. The other 6 `.ts` hits are `authorNotes`
bodies, prose strings and comments; the `.json` hits are witness/QA sidecars;
the 4 `.md` are prose. None of those is read by a checker, but all 27 become
dangling text on a pure rename.

### What this changes for T13, and what it does not

- **The rename is still small**, and still *pure* — nothing here argues against
  it. What is wrong is the claim that it touches no content reference.
- **The honest done-when** for the `_deprecated` half is: fix
  `wedderburn-weight-canonical.ts` (its own `authorNotes` already records that
  the Wenzl-bridge field was dropped by owner ruling, so the `status:
  "verified"` is doubly stale), then rewrite the 26 textual references to the
  new path in the same commit as the move.
- **The 3-vs-27 gap is the reusable part.** A narrow detector's count quoted as
  evidence for a wider claim is the detector-blindness failure one level up —
  the detector is correct, the citation is not. Recorded on `qou-jyqd` as well,
  since it is that bean's script being mis-cited.

No change proposed here: the `_deprecated` move already waits on owner ack per
the progress notes above, and this measurement is input to that decision rather
than a reason to act.

## 2026-10-10: `computations/_deprecated` half DONE — and all of `fsh-guts/` with it (PR #7622, issue #7621)

Owner, 2026-10-10: *"_deprecated is now branch cat/cat-harness/fsh-guts (or
should be. migrate if not)"*, then **option 2, full cut-over**, chosen over a
staged cut-over and over stopping at a seed. So this went further than the
T13 row: `fsh-guts/` itself also left `main`.

- **Branch store** `cat/cat-harness/fsh-guts` seeded at `ccd00c78050`, using the
  platform's layout (`README.md`, `manifest.json` `state-manifest/v1`
  `keyedBy: tip`, `fsh-guts/**`). It holds 1944 files, verified tree-by-tree
  byte-identical to main `dc984ef780`:
  - `fsh-guts/` (122)
  - `computations/_deprecated` → `fsh-guts/deprecated/computations` (1738)
  - `docs/audits/_deprecated` → `fsh-guts/deprecated/docs/audits` (66)
  - `qou-mass/src/qou_mass/data/_deprecated` → `fsh-guts/deprecated/qou-mass/src/qou_mass/data` (18)
- **Declaration:** `qou.json` now gives `fsh-guts` a `source: {kind: branch, …}`,
  and `.gitignore` adds `/fsh-guts/**`.
- **Mounting:** `scripts/mount-fsh-guts.sh` runs at SessionStart. It uses
  `state:mount` when the platform is present, and a read-only `git archive`
  copy otherwise.
- **Readers:**
  - The `_path_bridge` last-resort fallback now looks in the mounted tree, and warns when it is unmounted.
  - 150 skip filters gain `"fsh-guts"`. Without it, a repo-root walk would read the mounted copy as live.
  - 12 hand-built paths are re-pointed.
  - 145 doc and content path references are rewritten.
- **Measured:**
  - run-validate gives 9 issues mounted (same as main) and 18, INVALID, unmounted. The 9 extra are simulator `html:` paths under `fsh-guts/deprecated/simulators/`, which pre-date this change.
  - `derived_masses.py` and `q_beta_predicted.py` exit 0 with the store mounted.
- **Open:**
  - Qou's published build (platform `publish.yml`, via `build.yml`) has no mount step, so a dispatched build would miss the parked simulators.
  - The `wedderburn-weight-canonical.ts` `verified`-against-deprecated question is unchanged: its path follows the file, and the owner decision is still pending.

**2026-10-10 (later): the simulator gap is closed.** The paper still used nine of the eleven files in the deprecated simulators folder, so they were restored to `simulators/` on main and the eleven blocks re-pointed there (two are `todo-html` stubs whose HTML never existed). `double_slit.html` and `empty.html` are unreferenced and stay on the branch store. run-validate **unmounted** now reads Valid, 9 issues, the same as main, so the platform publish workflow no longer needs a mount step.
