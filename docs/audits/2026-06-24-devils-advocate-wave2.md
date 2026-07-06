# Devil's-advocate audit — Wave 2 (canonical-chain core)

**Watcher:** [`local/devils-advocate-watcher`](../../.claude/skills/local/devils-advocate-watcher.md)
**Date:** 2026-06-24 · **Branch:** `claude/lucid-gates-92e98s`
**Model:** claude-opus-4-8 · L1 formalist + L2 skeptical physicist + L3 algebraist + L4 reproducibility/citation + adjudicator.

Wave 2 attacks the core of the derivation chain: q₀ determination, the tr_M Frobenius pairing, the confinement SDP, the F_Bor observable, and the magic-A binding formula. As in wave 1, `da-*` findings persist in each block's `.qa.json`; a `da-referee-verdict` of `open-objection` means *a referee argument survived rebuttal*, not that the block is proven false.

## Results

| Block | Verdict | Strongest objection |
|-------|---------|---------------------|
| [`knot-factor-frobenius-pairing`](../../content/quantum-observable-universe/mass-theory/knot-factor-frobenius-pairing.md) | **🔴 open-objection** | `.ts` title + **both** `.lean` siblings encode the **retracted** ratio form `a(N)=\|tr_M(W_atom)\|/\|tr_M(W_free)\|` (the `.md` itself calls it 6–17× wrong), and **neither Lean file compiles** (import-after-decls + duplicate-class collision) — so nothing is verified. |
| [`magic-A-binding-formula`](../../content/quantum-observable-universe/mass-theory/magic-A-binding-formula.md) | 🟡 survivable | Tagged `"no-fitting"` / "closed form" while two of four inputs (`ρ_F=2`, `Vol=A·8G`) are *modelled* (corpus's own 2026-06-16 audit: "near-match, not a closure") and the +5.9% ⁴He miss is real. |
| [`confinement-sdp`](../../content/quantum-observable-universe/mass-theory/confinement-sdp.md) | 🟡 survivable | `lean.ref` (`QOU.ParticleInteractions.ConfinementSDP`) resolves to no decl (sibling is a `sorry`-stub; the real file is namespace `QOU.Interactions`); 2 of 3 cited compute scripts missing. |
| [`local-substrate-q`](../../content/quantum-observable-universe/observations/local-substrate-q.md) | 🟡 survivable | Body states q₀ as muon-determined, but the live pin (and the block's own witness) is the proton ratio — a cross-check identity stated as the determination; Lean one re-pin behind. |
| [`f-bor-borromean-observable`](../../content/quantum-observable-universe/braids-and-knots/f-bor-borromean-observable.md) | 🟢 clean | Only a citation-key typo (`chlouveraki2016hdr` → `chlouveraki2016-hdr`) + a placeholder DOI. The `[3]_q!/q³` normalization is `1/y_{(3)}`, Lean-proved forced, not tuned (predicts m_n as a second observable). |

## Highlights

- **`knot-factor-frobenius-pairing` (open, critical).** The most serious wave-2 find. The durable artifacts (`.ts` title + both `.lean` siblings) carry a formulation the block's own `.md` body explicitly *retracts* as historical and 6–17× off the Skein values, and the Lean does not compile at all (`lean.validation: not_checked` confirms it was never built; the broken sibling *shadows* the library file under §0a sibling-first resolution). The `da-false-claim` is scoped `structural` and cites a proved invariant (Lean-4 grammar — imports-after-declarations + duplicate-name collision make it un-typecheckable). → **Author-assist:** decide the canonical claim (Skein-product `a_K`, per the `.md`), then rewrite/repair the Lean to it and delete the retracted ratio encoding.

- **`magic-A-binding-formula` (survivable).** The math is honest about its +5.9% miss, but the `"no-fitting"` tag + "closed form" vocabulary on a formula with two *modelled* inputs and a single in-domain data point (⁴He) is a surviving `da-overclaim`. `ρ_F=2` is a disclosed (not concealed) hidden DOF. → **Author-assist:** re-tag / soften framing to "near-match" per the corpus's own provenance audit.

- **`confinement-sdp` (survivable).** Math is standard Boyd–Vandenberghe SDP duality and the witness correctly emits the full LP/SDP dual (no historical primal-only gap). Defects are wiring: a dangling/mis-namespaced `lean.ref` and two cited compute scripts that don't exist. The Lean conditional-class projection is a *sanctioned* Pattern-4 stub (registered in `conditional-class-instances.md`), so `partial`, not surviving.

- **`local-substrate-q` (survivable).** The `unique_q_solution` Lean theorem genuinely derives ∃! (sorry-free) — not vacuous. The surviving issue is purely the muon-vs-proton anchor staleness, disclosed elsewhere in the corpus but not in this block's prose/Lean.

- **`f-bor-borromean-observable` (clean).** Adversary confirms the normalization is structurally forced (`1/y_{(3)}`, content-sum `c((3))=3` → `q³`, Lean-proved) and falsifiably predicts m_n — a fitted normalization could not. Only pre-publication citation hygiene remains (auto-dischargeable).

## Disposition

- **Author-assist (queued):** `knot-factor-frobenius-pairing` (Lean repair + retracted-form removal, critical); `magic-A-binding-formula` (re-tag overclaim, major); `confinement-sdp` (fix dangling `lean.ref` + missing-script references, major/minor).
- **Auto-discharge (hygiene, separate commit):** `f-bor-borromean-observable` citation-key typo.
- **Defer (rebutted-as-known):** the disclosed muon-vs-proton anchor staleness, the sanctioned Pattern-4 SDP stub.

## Running tally (waves 1–2, 9 blocks)

2 open-objection · 5 survivable-objection · 2 clean. The adversary has now flagged **two** durable-artifact-vs-narrative divergences where a block's `.lean`/`.ts` encodes a claim the `.md` itself disavows or the corpus has purged (`borromean-baryon-mass-formula` λ_scale revival; `knot-factor-frobenius-pairing` retracted ratio form) — a recurring failure class worth a targeted sweep.
