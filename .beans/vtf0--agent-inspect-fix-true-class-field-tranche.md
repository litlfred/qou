---
# vtf0
title: 'Agent-inspect + fix the 38 needs-agent vacuity candidates (true-class-field tranche + cluster-7 leftovers)'
status: open
type: task
priority: high
created_at: 2026-06-28T02:00:00Z
updated_at: 2026-06-28T02:00:00Z
---

Newly surfaced by the upgraded vacuity heuristics (PR #2881): the
`true-class-field` detector flags `class`/`structure` fields typed literally
`: True` (the field-level analogue of a `: True` conclusion — §3b-tax "the
carrier must assert something"). **36** un-annotated `: True` carrier fields
remain (16 honest opaque-markers are already exempt), plus **2 cluster-7
leftovers** deferred because compile-verification was cache-blocked this session.

**Work queue is the committed ledger:**
[`docs/audits/lean-vacuity-review-ledger.json`](docs/audits/lean-vacuity-review-ledger.json)
— every entry with `verdict: "needs-agent"`. Skill + protocol:
[`.claude/skills/local/lean-proof-vacuity-audit.md` §Agent-inspection ledger](.claude/skills/local/lean-proof-vacuity-audit.md).

**PREREQUISITE — a working Lean cache.** This session had no `lake-cache/qou-*`
orphan branch and an incomplete mathlib source (`Mathlib/Tactic/Omega.lean`
missing), so `lake env lean` could not verify edits. Restore/seed a cache first
per [`lean-environment-setup.md`](.claude/skills/local/lean-environment-setup.md);
do NOT ship unverified Lean (the cluster-7 lesson).

**Per candidate (agent inspection, then fix):**
1. **Genuine §3b-tax defect** — un-annotated `: True` field, especially a
   `Conjectures/*` carrier that a trivial `instance … := ⟨⟩` "closes"
   (e.g. `MagicNumbersBring`, `QuantumLanglandsDual`, `WeakSpectralCompleteness`,
   `ShellTransitionKnot`, `KnotFactorFrobeniusPairing`). Fix: encode the real
   property as the field type (Pattern A/B), or remove the fabricated instance
   and leave the carrier content-bearing with **no** instance (honest open state).
2. **Honest open infrastructure** Mathlib genuinely lacks (e.g. the KLR /
   Kashiwara / Hecke-`H_n(q)` scaffolds) — annotate the field `opaque marker`
   so it becomes exempt-but-tracked (do NOT fabricate content).
3. Then write the verdict into the ledger and verify `--check-ledger` passes.

**Done when:** every `needs-agent` entry has a fresh agent verdict
(`genuine`-fixed / `legit` / `advisory`-fixed) whose `.lean` sha matches, and
`bun run content/pipeline/lean-vacuity-axiom-audit.ts content/quantum-observable-universe --check-ledger docs/audits/lean-vacuity-review-ledger.json`
exits 0. Commit + push to a fresh `claude/<theme>-<ymd>` branch.

Also re-verify the 3 cache-blocked cluster-7 items once the cache is back:
`q-heat-kernel-peter-weyl.lean:82` (the pattern-C `: Prop` rewrite was reverted —
the agent edit had an unbalanced `end`; redo it), `MassGapKeystone.lean:204`
(false-premise — likely legit), `Knots/KauffmanTL3.lean:267`
(`borromean_crossing_minimal` native_decide → try `decide`).
