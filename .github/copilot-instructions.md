# Copilot Instructions for QOU
This repository delegates to the shared Copilot instructions from the folio-assistant sub-repository.
Please read: `folio-assistant/.github/copilot-instructions.md`

Repo-specific rules that apply on top of the shared instructions:

## Contribution POLICY AND ATTRIBUTION (owner directive 2026-11-23) — STRICT

The repository is being prepared for public release. The policy is in
[`CONTRIBUTING.md`](../CONTRIBUTING.md) §"Contribution policy"; agents enforce it
and must not weaken it.

- **Issues need evidence.** From anyone other than the owner (`litlfred`), an
  issue must carry a Lean counterexample, a failing Python test, or a pinpoint
  citation (theorem/equation number and page). Otherwise it is closed
  (`issue-policy.yml` does this automatically). Do not open evidence-free
  issues on behalf of others, and do not reopen one the check closed.
- **A non-owner's merged PR earns authorship.** When an agent merges (or
  prepares the merge of) a PR whose author is not `litlfred`, it must, in the
  same PR or an immediate follow-up: add the contributor to
  `paperIdentity.authors` in
  [`folio/quantum-observable-universe/identity.ts`](../folio/quantum-observable-universe/identity.ts)
  and a row to [`CONTRIBUTORS.md`](../CONTRIBUTORS.md) naming the PR. Ask the
  contributor how they want to be named; default to their GitHub login.
- **Agent attribution is not authorship.** Commits and PRs written by agents
  carry their `Co-Authored-By` / session trailers as now; an agent is never
  added to the paper's author list. The authors' note records the use of
  language models.
- **License.** Everything in the repository is CC BY 4.0 ([`LICENSE`](../LICENSE)).
  Do not add files under another license without asking the owner, and keep
  third-party code's own notice beside it.
- **KG validation** rules and tooling are documented in
  [litlfred/folio-assistant-core](https://github.com/litlfred/folio-assistant-core);
  point contributors there rather than restating its rules.

