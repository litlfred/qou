# Coordination ledger — language-trap agentic QA drain

Branch `claude/q-ns-classical-gaps-9l9mj9` · PR
[#5419](https://github.com/litlfred/qou/pull/5419) · bean `qou-ujp8`

## Scope

Corpus-wide agentic audit of the ten `trap-*` categories, one full-context
read per prose-bearing content block, recorded as `reviewer.kind: "agent"`
entries in the `block-qa/v1` sidecars.

**Files touched:** `.qa.json` sidecars, content `.md` prose fixes, `.beans/`,
`.claude/skills/local/`, three `.tex` preambles.
**Files never touched:** `.lean`, `computations/`, any witness. Math-bearing
findings are reported as beans or sibling comments, never edited.

Coverage at the time of this entry: **3,037 / 3,553 blocks (85.5%)**.

## Sibling scope map — 2026-08-22

24 open PRs reviewed by title and head; four have genuine scope overlap. The
rest are Lean-only, `computations/`-only, or in unrelated chapters, and were
deliberately not commented on (AGENTS.md: *"only the genuinely-overlapping
ones, and don't make too much noise"*).

| PR | relationship | action |
|---|---|---|
| [#5367](https://github.com/litlfred/qou/pull/5367) — every content manifest loads | **file collision** on `mass-theory/atomic-q-reeb-universal-rho.{md,qa.json}` | replied: take the union either way; corrected their read of the union script's filter (it keys `field_hash.md` only, so a `.ts` rewrite does **not** degenerate it) |
| [#5371](https://github.com/litlfred/qou/pull/5371) — self-assuming projections, detector gaps | **finding handover**; no file overlap | posted 3 instances, all verified absent from the 165-entry vacuity ledger: an axiom proving `False`, three `∃ x, x = e` decls, one `:= ctx.claim_foo` projection |
| [#5407](https://github.com/litlfred/qou/pull/5407) — hyperbolic volume constants | **same surface**; no file overlap | posted the `L4a1` volume (should be 0), and the `8G/ℏ_q²` split — 749 vs 746 for the same quantity in one chapter |
| [#5430](https://github.com/litlfred/qou/pull/5430) — the three "muon q₀" values | **same surface**; no file overlap | posted two further families (`q = 111/100`, declared in a witness; `q ≈ 1.1097`) plus an old-muon + convention-C pin inside the flagship LP witness |

Classified as **no overlap** and not commented on: #5435, #5380, #5434, #5436,
#5373, #5438, #5386, #5293, #5423, #5431, #5361, #5378, #5417, #5428, #5426,
#5316, #5427, #5403 (Lean, `computations/`, witness provenance, or unrelated
chapters). #5437 edits `coordinate.md`; this branch edits
`language-trap-agent-audit.md` — same directory, different file, no conflict.

## Findings promoted out of the drain

Severe items go to their own beans rather than the `qou-3nva` ledger:
`qou-rhax` (an axiom proves `False`), `qou-etfq` (the LP-dual-stability table
does not follow from its witness), `qou-jbbk` (two Jones values unattainable by
their own polynomials), `qou-ptnp` (three vacuous decls, one load-bearing),
`qou-tol0`, `qou-vfy1`, `qou-umev`, `qou-shdw`.

## Standing discipline for this drain

Every numeric claim quoted in a drain commit or a sibling comment is
**re-derived in the coordinating session** before it is written down. The
reason is measured: across this campaign, agent *numeric* findings have
survived independent recomputation every time they were checked, and agent
claims about a file's *past or existence* have inverted three times out of
three. The clone is shallow (19 grafts), so history claims are not available
here at all — see `local/language-trap-agent-audit` §"Verify provenance claims
before repeating them".
