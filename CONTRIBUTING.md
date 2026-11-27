# Contributing to QOU

Thanks for your interest in the **Quantum Observable Universe** repository (source: [github.com/litlfred/qou](https://github.com/litlfred/qou)). This repository is a mathematics paper with a Lean 4 formalisation and a compute layer. Contributions are welcome, but the bar is deliberately strict: every report must be checkable by someone who was not in your head when you wrote it.

## Contribution policy (applies to everyone except the owner, `litlfred`)

### Issues: bring evidence, or the issue is closed

An issue must carry **at least one** of the following. An issue without one is closed, without discussion, by the issue-policy check and by the maintainers.

| Evidence | What counts |
|---|---|
| **Lean counterexample** | A self-contained Lean 4 snippet that compiles against this repository's Lake workspace and proves the negation of a stated result, or shows a stated declaration is vacuous (e.g. its hypotheses are unsatisfiable, or it concludes `True`). Name the declaration (`QOU.…`). |
| **Failing Python test** | A minimal script or `pytest` test, runnable from the repository root, that fails on `main` and shows a wrong number, a precision loss, or a broken producer. Paste the command and its output. Use `mpmath`, never float64, for any numerical claim. |
| **Pinpoint mathematical citation** | A published source with **theorem/lemma/equation number and page**, plus the exact block it bears on (the `.md` path or the label, e.g. `prop:foo`). "See the literature" or a paper without a location is not a citation. |

Use the issue forms under **New issue**; each form asks for exactly one of these. Blank issues are disabled. Questions, opinions and requests for explanation go to Discussions if enabled, not to issues.

The **physics comparison points** (a model quantity set against CODATA, AME2020 or PDG) are where the empirical claims of the paper live. A report that such a comparison is wrong is welcome and still needs one of the three items above, typically a failing Python test.

### Pull requests: same bar, plus validation

A pull request must:

1. reference an issue that meets the policy above (or open one);
2. pass the validation the change touches, stated in the PR body with the commands you ran: `lean -DautoImplicit=false -s 65536 <file>` (exit 0, `#print axioms` shows no `sorryAx`) for Lean; `scripts/precision-gates.sh --changed` for compute; the content validator for `.ts`/`.md` blocks;
3. introduce no new `sorry` without a `-- Ref:` citation, no `: True` placeholder, and no fitted constant (see [`AGENTS.md`](AGENTS.md), §"NO FITTING" and §"Strict Lean Discipline").

The knowledge-graph tooling, schemas and the validation rules that content blocks must satisfy live in [**litlfred/folio-assistant-core**](https://github.com/litlfred/folio-assistant-core). Read its README before editing a content block.

### Attribution: a merged pull request earns authorship

If you are not the owner and a pull request of yours is **merged** into `main`, you will be **listed among the authors of the paper**, with the PR cited. Concretely:

- your name (as you give it in the PR, or your GitHub login) is added to the author list in [`folio/quantum-observable-universe/identity.ts`](folio/quantum-observable-universe/identity.ts) and to [`CONTRIBUTORS.md`](CONTRIBUTORS.md) in the same release;
- the authors' note of the paper describes this policy;
- a closed-unmerged PR, an issue, or a review comment does not by itself earn authorship, but issues that lead to a merged correction are acknowledged.

Tell us in the PR body how you want to be named and whether to include an affiliation or ORCID.

### License of contributions

The repository is licensed under **[Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE)**. By opening a pull request you agree that your contribution is released under the same license.

For the deeper architecture, see [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).

## TL;DR

```bash
# 1. Clone + set up
git clone https://github.com/litlfred/qou.git
cd qou

# 1b. Wire up the Folio Assistant platform (separate repo litlfred/folio-assistant).
#     Clones it as a sibling (../folio-assistant) + symlinks ./folio-assistant -> it,
#     so the content pipeline + schema imports resolve. Idempotent; re-runnable.
./scripts/setup-folio-assistant.sh

# 2. Install content-pipeline deps (TypeScript via bun)
cd content && bun install && cd ..

# 3. Install Python scientific deps (substrate compute)
pip install --user numpy sympy scipy mpmath pypdf

# 4. (Optional) Set up Lean if you'll touch .lean files
# Use the lean_setup MCP tool or:
curl -sSf https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh | sh

# 5. Validate the content pipeline
cd content && bun run validate
```

## Repo layout (high level)

| Path | What |
|---|---|
| `content/` | Authoritative content objects (`.ts` + `.md` + `.lean` triples) |
| `folio-assistant/` | **Symlink** to the external platform repo [`litlfred/folio-assistant`](https://github.com/litlfred/folio-assistant) (pipeline, schemas, viewer, compute) — created by `scripts/setup-folio-assistant.sh`; not tracked |
| `tools/` | Reusable libraries (see below) |
| `chapters/` | LaTeX rendered from content (generated; do not edit) |
| `docs/` | Design docs, audits, workplans |
| `.github/workflows/` | CI/CD pipelines |
| `.claude/` | Skill definitions, settings, decision log |

### The Folio Assistant platform (external repo)

`qou` is **content only**. The platform it consumes — content pipeline, schemas, LaTeX rendering, viewer, computations — lives in the separate repo [`litlfred/folio-assistant`](https://github.com/litlfred/folio-assistant). Local checkouts wire it through a single in-repo path, `./folio-assistant`, a symlink to a sibling clone created by `scripts/setup-folio-assistant.sh`:

| Consumer | Path it resolves through |
|---|---|
| `folio/schema/*.ts` shims + content blocks | `folio-assistant/schemas/…` |
| `package.json` scripts (`validate`, `build:content`, `export-json`, `test`, `lint`) | `folio-assistant/content/pipeline/…` (and `folio-assistant/` for tests) |
| CI ([`.github/workflows/build.yml`](.github/workflows/build.yml)) | the platform's reusable workflow on GitHub — **no local clone needed** |

Re-run the setup script any time to update the platform clone or repair the symlink. Override the source via env vars: `FOLIO_ASSISTANT_REPO`, `FOLIO_ASSISTANT_REF`, `FOLIO_ASSISTANT_DIR`.

### `tools/` packages

| Package | Language | What |
|---|---|---|
| `tools/qou-substrate/` | Python | `WitnessBuilder` + `_precision` + `q_parameter` substrate trio (not published to PyPI; install from the repo) |
| `tools/pyhecke/` | Python | Pure-Python Hecke + Gram + Wedderburn-Artin canonical surface (not published to PyPI; install from the repo) |
| `tools/pyhecke-native/` | Rust → Python (PyO3) | Native acceleration layer (not published; build with `maturin build --release`) |
| `tools/hecke-engine/` | Rust | The canonical Rust core (Gröbner-Shirshov reducer, Gram, Markov-trace, Wenzl LR, SDP backends) |
| `tools/hecke-engine-wasm/` | Rust → WASM | `wasm-bindgen` exports of the rug-free canonical surface — published as `@litlfred/hecke-engine-wasm` on npm (when stable) |
| `tools/hecke-engine-node/` | Rust → Node (napi-rs) | Server-side Node.js native binding — published as `@litlfred/hecke-engine-node` on npm (when stable) |
| `tools/witness-schema/` | JSON Schema + Pydantic + Zod | Cross-language schema for `*.witness.json` files — published as `witness-schema` on PyPI + `@litlfred/witness-schema` on npm |
| `tools/snappea-wasm/` (under `folio-assistant/`) | C → WASM | SnapPea hyperbolic 3-manifold kernel as `@snappea/kernel` on npm |

## Where to start

The easiest way in is to fork the repository and explore it with the language model of your choice. Ask it what the paper claims, how a result is proved, or where a number comes from, and let it walk you through the files.


| If you're working on… | Start here |
|---|---|
| Paper content (definitions, theorems, proofs) | [`.github/copilot-instructions.md`](.github/copilot-instructions.md) §"Content-object architecture" + [`AGENTS.md`](AGENTS.md) §"Content-object architecture" |
| A Lean formalization | [`AGENTS.md`](AGENTS.md) §"Writing `.lean` proofs — rules for agents" + [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) §"Lean workspace" |
| A new compute script | [`AGENTS.md`](AGENTS.md) §"LP / SDP duals — first-class infra" + `.claude/skills/local/compute-author.md` |
| A pyhecke / hecke-engine change | [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) §"Tools packages" |
| A CI / publish workflow change | [`docs/workplans/2026-05-24-publish-yml-parallelization-plan.md`](docs/workplans/2026-05-24-publish-yml-parallelization-plan.md) (the current plan) |

## Branching + commits

Per [`AGENTS.md`](AGENTS.md) §"Branch + PR workflow" (**STRICT**):

- **Always create a branch + PR at the start of every work tranche.** No commits direct to `main`.
- **Branch naming**: `claude/<theme>-<utc-ymd>` (e.g. `claude/lean-cache-hybrid-2026-05-24`).
- **Commit early + commit often**: small structured commits (1 logical unit per commit) so cherry-pick, bisect, and focused review work cleanly.
- **Default merge method: rebase-merge** (preserves the per-commit structure). The skill docs say "merge-commit" but `AGENTS.md` §"Branch + PR workflow" rule 7 overrides that.
- **Don't squash** unless the branch has noisy `wip` / `oops` commits the owner explicitly asks to collapse.

## CI gates

| Gate | What it checks |
|---|---|
| `validate` (witness-pipeline.yml) | 9 substrate-precision scripts pass (hyperbolic_volumes, codata_masses, …) |
| `lean_ci.yml` | Root Lake workspace builds (`lake build`) — covers all 3 paper packages (QOU, UGB, fred2005) |
| `publish.yml` | Content pipeline → LaTeX → PDF → gh-pages preview |
| `blueprint.yml` | LeanBlueprint dependency graph + axiom report |
| `paper-builder-image.yml` | Prebuilt `ghcr.io/litlfred/qou-paper-builder` Docker image used by `publish.yml` |

Run validators locally before pushing:

```bash
# Substrate-precision smoke
python3 computations/hyperbolic_volumes.py
python3 computations/codata_masses.py

# Content validation
cd content && bun run validate

# Lean build
lake build
```

## Skills (the agent-facing entry points)

The repo ships dozens of **skills** under `.claude/skills/local/` that document how to do common operations. When working on this repo via Claude Code / Cursor / GitHub Copilot, invoke skills by typing `/<skill-name>` or by asking the model to invoke them.

The high-leverage ones for contributors:

| Skill | Use for |
|---|---|
| `/prepare-merge` | Rebase + validate + request reviews + merge a PR |
| `/coordinate` | Coordinate with sibling PRs (cherry-pick, intent comments) |
| `/integration-watch` | Run the 4 integration watchers (proof / canonical / compute / detangler) |
| `/integration-backlog` | Drain a per-criterion backlog into PRs |
| `/code-review` | Review the current diff |
| `/verify` | Run the app and verify a change works |

Full routing table is in [`AGENTS.md`](AGENTS.md) §"Skill routing".

## Code style

| Language | Tool | Notes |
|---|---|---|
| Python | `ruff` (recommended), `black` style | Substrate-precision discipline: prefer `mpmath.mpf("...")` / `Decimal("...")` over bare `float` — see `.claude/skills/local/compute-author.md` |
| Rust | `cargo fmt` + `cargo clippy` | `hecke-engine`'s `mpfr` feature gates rug; default builds are mpfr-on |
| TypeScript | Bun's default (tab=2-space) | Content pipeline + assistant UI |
| Lean | `lake build` + `lake test` | Always carries `-- Ref:` citation on every `sorry`; see [`AGENTS.md`](AGENTS.md) §"Writing `.lean` proofs" |

## Questions?

- Open an issue: https://github.com/litlfred/qou/issues
- See [`docs/`](docs/) for design docs, audits, workplans
- Check [`AGENTS.md`](AGENTS.md) for the comprehensive agent / contributor guide (it's exhaustive)
