# Devil's-advocate audit — Wave 1 (seed targets)

**Watcher:** [`local/devils-advocate-watcher`](../../.claude/skills/local/devils-advocate-watcher.md)
**Date:** 2026-06-24 · **Branch:** `claude/lucid-gates-92e98s` · **HEAD:** `43dc406c`
**Model:** claude-opus-4-8 · **Lenses per block:** L1 formalist + L2 skeptical physicist + L3 algebraist + L4 reproducibility/citation + adjudicator.

This is the first wave of the adversarial axis: for each block we constructed the strongest referee objection, then let the block's own text / Lean / cited refs / corpus-grep rebut it. Findings persist as `da-*` entries in each block's `.qa.json`. A `da-referee-verdict` of `open-objection` means *a referee argument survived rebuttal in this audit* — **not** that the block is proven false.

## Seed-target selection (Slot H)

Wave 1 = the four most load-bearing, most-attackable claims on the canonical derivation chain: the headline m_p mass derivation, the central anti-numerology discipline, the Δ_λ binding gate, and the Q_β c_k precision ladder.

## Results

| Block | Verdict | Strongest surviving / open objection | Disposition |
|-------|---------|--------------------------------------|-------------|
| [`conj:borromean-baryon-mass-formula`](../../content/quantum-observable-universe/mass-theory/borromean-baryon-mass-formula.md) | **open-objection** | Revives `λ_scale` as a live "conjectural common scale" with "open R&D", contradicting its own sibling (`structurally falsified … Do not revive`), its witness (`RESOLVED post-PR #1080`), and the AGENTS.md standing purge. | **Author-assist** (queue, critical) |
| [`prop:three-calibration-discipline`](../../content/quantum-observable-universe/observations/three-calibration-discipline.md) | survivable-objection | Lean proves a tautological factorisation, not the "exactly three" count; Q_β is asserted "derived" where the corpus labels its key link "POSTULATED, NOT DERIVED". | **Author-assist** (queue, major) |
| [`prop:qbeta-ck-truncation-canonical`](../../content/quantum-observable-universe/appendix-qvalues/qbeta-ck-truncation-canonical.md) | survivable-objection | Ships a stale/false witness assertion (`N3_beats_100x … passed:false`); "near-match" framing trails the 2026-06-04 registry that REFUTED real-q `c_3`. | **Author-assist** (queue, major — likely a witness refresh + cite update) |
| [`alg:per-isotope-binding-delta-lambda-closure`](../../content/quantum-observable-universe/appendix-mass-binding-algorithms/mba-sidecar-delta-lambda-closure.md) | **clean** | (only a stale "current direction" wording vs the post-PROBE-4 frontier; honest open-gate record) | **Defer** (rebutted-as-known) |

## Per-block detail

### 1. `conj:borromean-baryon-mass-formula` — **open-objection** (critical)

The most damaging find of the wave. The block presents `λ_scale` (the per-baryon "conjectural common scale") as a live object with an "open R&D" programme to derive a closed form matching `2.4599…`. But:

- its **sibling** `lambda-scale-substrate-form.md` states `λ_scale` was *structurally falsified*, the CAL-4 framing *purged*, and `λ_scale` *absorbed into VolDensity* (Family A, PR #1080) — "**Do not revive**";
- the block's **own witness** records `open_R_and_D.substrate_linking_weight = "RESOLVED post-PR #1080"`;
- **AGENTS.md:660** carries the standing purge ("do not reintroduce `λ_scale`").

Compounding (independent, surviving): the Lean class fields `proton_matches_codata : True` / `neutron_matches_codata : True` are vacuous (§1a audit-dodge), and the backing witness has `assertions:[]` while `.ts` reports `status:"verified"` (an empty assertion set verifies nothing). `da-hidden-dof` (per-baryon λ_scale fit) is partial — the block honestly isolates the substrate-derived ΔS (1015 ppm) as the testable claim.

→ **Author ask:** is the `λ_scale` revival intended, or should this block be re-scoped to the absorbed-into-VolDensity / ΔS-only framing (and the `: True` Lean fields + empty-assertion "verified" status fixed)?

### 2. `prop:three-calibration-discipline` — survivable-objection

The framework's central anti-numerology defense. Two surviving objections, both conceded *in siblings* but not in this block's assertive prose: (a) the Lean theorem `:= c.mass_factorisation X` projects the conclusion it should derive (self-assuming projection, §3b-cond non-degenerate / proof-statement-integrity) — it encodes neither "exactly three" nor "no fourth"; (b) the corpus carries ≥3 mutually inconsistent calibration triples, so "exactly three" survives relabeling (the L3 worry). The Q_β "derived" claim is a partial overclaim (corpus: "POSTULATED, NOT DERIVED"). `da-hidden-dof` (m_p re-pin) and `da-citation-misuse` are rebutted.

### 3. `prop:qbeta-ck-truncation-canonical` — survivable-objection

Honest tiering (the discipline AGENTS.md demands) — so the *tiering* is not the objection. The defects are staleness: the headline witness assertion `N3_beats_100x_experimental_target` is `passed:false` (computed 38.61 ppb vs expected 6.02 — a frozen pre-re-pin number), and the block predates / does not cite the 2026-06-04 registry that REFUTED real-q `c_3`. `c_2 = -1` is genuinely proved (sibling Lean); the Lean sibling is an honest §3b conjecture, not vacuous.

### 4. `alg:per-isotope-binding-delta-lambda-closure` — **clean**

A model honest open-gate record: enumerates only the six *failed* ansätze, restates the no-7th-ansatz ban, names the PROBE 4 KL-positivity prune, and carries `status:experimental` / "No verified witness yet". The only blemish is the "current direction" wording trailing the post-prune frontier by ~5 weeks — a `partial`, rebutted-as-known. Demonstrates the adversary does **not** cry wolf on a block that honestly reports its own open status.

## Calibration note (adversary held to its own discipline)

Per the (a)/(b) refutation-scope rule, only finding #1's `da-overclaim` is scoped `structural` — and it cites a concrete corpus closure (the Family A absorption proof, PR #1080) as the invariant. Every other "wrong" finding is scoped `limited`. No "open gap" was written `surviving` without the corpus-grep checklist (the Δ_λ and c_k status were both found already-documented, hence rebutted-as-known / staleness rather than fresh gaps).

## Next waves (queued)

Backlog = 1047 auditable blocks. Priority per Slot H: remaining canonical-chain + headline-observable blocks (q_0 inversion, tr_M Frobenius pairing, SDP confinement, F_Bor, the binding-magic A blocks), then by downstream-dependent count. Surviving objections from this wave are in `.beans/devils-advocate-watcher-queue.json`.
