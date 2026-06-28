# Compute-integration sweep — resolution of the UNVERIFIED 8 (2026-06-28)

Branch: `claude/compute-integration-wiring-2026-06-28`
Follow-up to: [`docs/audits/2026-06-28-compute-integration-sweep.md`](2026-06-28-compute-integration-sweep.md)
(sibling branch `claude/compute-integration-sweep-2026-06-28`).
Skill: `local/compute-integration-watcher` (verification checklist §385–397).

## Purpose

The parent sweep marked 8 labels **UNVERIFIED**: the label string appears
inside a genuine probe witness under a *non*-`contentBlock` field
(`reference_blocks`, `design_spec`, nested `uses`), so a probe very likely
exists, but the sweep could not confidently classify WIRED vs I2 (probe-only)
vs genuine I1 without opening each witness and grepping the production
consumers. This doc records the per-label resolution with evidence.

## Method

- **Production consumer set (25 scripts):** `derive_*.py`,
  `build_*_chain*.py`, `paper_six_term*.py`, `atomic_mass_via_rho_k.py`,
  `mass_table_ppb.py`, `canonical_mass.py` (the same set the parent sweep used).
- **WIRED** if a consumer references the label string **or** a witness
  filename that carries the label, **and** that reference is load-bearing
  (the code implements / consumes the claim, not a bare mention in a
  docstring bibliography).
- **I2 (probe-only)** if a probe witness carries the label (in any field) but
  **no** consumer references the label or its witness file. Per AGENTS.md
  *"Before declaring refuted / ruled out"* this is a **scope-(a)** finding:
  "no *direct* production consumer found" — **not** a structural claim that
  the prop is excluded from production. The witness still validates the claim.
- **I1** only if no probe witness carries the label at all (none of the 8
  fell here — all 8 have a probe witness; the parent sweep was right to not
  promote them to I1).

## Resolution table

| # | label | carrying probe witness (field) | production consumer? | verdict | evidence |
|---|---|---|---|---|---|
| 1 | `thm:frobenius-codim-universal` | `mass-formula-6term.witness.json` (`reference_blocks`) | **yes** | **WIRED** | `derive_m_p_hecke_path_a.py:137` computes the codim field *"per thm:frobenius-codim-universal"*; the sibling production witness `mass-formula-6term-mpfr-50dps.witness.json` is consumed by `build_proton_mass_50dps_chain.py`, `derive_m_{e,n,p}_hecke_path_a.py`. The theorem's claim is implemented in the m_p production code. |
| 2 | `thm:markov-trace-product` | `vhat-per-crossing-chain.witness.json` (nested `reference_blocks`) | **yes** | **WIRED** | `derive_m_p_hecke_full_tower_50dps.py:250,256,352` — the canonical m_p production chain uses the theorem's per-generator factor `∏ V̂ᵢ = tr_M` in its CHANNEL-SELECTION step (cross-checked to 4e-6, audit `2026-06-01-vhat-per-crossing-transfer-chain.md`). |
| 3 | `prop:joint-tower-sdp-confinement` | `joint-tower-sdp-h6-h9.witness.json`, `joint-tower-sdp-rust.witness.json` (`design_spec`) | no | **I2 (probe-only)** | Two named SDP confinement witnesses carry it as their `design_spec`; also `binding-k-solver`, `rho-prefactor-structural-verifier`. No consumer references the label or those witness files. Probe-only confinement SDP. |
| 4 | `prop:categorical-mass-markov` | `canonical-isospin-pyhecke.witness.json` (`reference_blocks`) + the Δ_λ family | no | **I2 (probe-only)** | Carried in `reference_blocks` of `canonical-isospin-pyhecke` and the `delta-lambda-*` tabulation/sweep witnesses + `e0-calibration-audit`. No consumer references them. Part of the Δ_λ-gated probe family (Track-A blocker) — probe-only is the expected state. |
| 5 | `prop:schur-weyl-mass-decomposition` | `atom-level-wedderburn-tower.witness.json` (`reference_blocks`) | no | **I2 (probe-only)** | `reference_blocks` of `atom-level-wedderburn-tower`; that witness is not referenced by any consumer (filename grep over the 25 scripts is empty). |
| 6 | `thm:wedderburn-mass-formula` | `atomic-braid-gb-filtration-extension.witness.json` (nested `reference_blocks`) | no | **I2 (probe-only)** | Carried in the GB-filtration-extension probe witness; not consumed by any production chain. |
| 7 | `prop:magic-numbers-from-q` | `per-pair-wedderburn-enumeration.witness.json` (`reference_blocks`) | no | **I2 (probe-only, intentional)** | The carrying witness self-describes as *"Empirical step — NOT a new closed form (per AGENTS.md Track A discipline)"* — it is an intentional probe, not a wiring candidate. No consumer references it. |
| 8 | `prop:categorical-neutrality-saturated-shells` | `per-pair-wedderburn-enumeration` (`reference_blocks`), `delta-n2-lp-dual-extraction` + `full-twist-delta-n2-verification` (`contentBlock`) | no | **I2 (probe-only)** | Has a dedicated probe (`delta-n2-lp-dual-extraction` carries it as `contentBlock`) plus the per-pair enumeration. No production consumer references the label or those witnesses. |

## Summary

- **2 of 8 → WIRED** (`thm:frobenius-codim-universal`, `thm:markov-trace-product`)
  — both load-bearing in the m_p production chains.
- **6 of 8 → I2 (probe-only)**, scope-(a): "no direct production consumer
  found". None promote to I1 (all carry a probe witness). Four of the six
  (`categorical-mass-markov`, `magic-numbers-from-q`,
  `categorical-neutrality-saturated-shells`, plus the SDP / Wedderburn
  structural pair) are Δ_λ / Track-A / SDP-confinement probes where
  probe-only is the *expected* state given the Track-A gate, not a wiring
  defect.
- **0 of 8 → genuine I1.**

No (b)-scope structural-exclusion claims are made: every I2 row means the
witness exists and validates its prop; only a *direct* production consumer is
absent. Wiring any of the six into production is gated on the corresponding
Track-A / SDP / Δ_λ decision, not on this audit.

## Incidental finding (out of scope, flagged for follow-up)

While wiring the c_k witnesses (Task A of this PR), the existing
`c-k-beta-decay-bound.witness.json` was found to carry
`contentBlock: "conj:archimedean-remainder-exponential-decay"` — but **no
block file defines that label** in `content/` (it appears only inside a
`uses[]` / prose reference in
`particle-interactions/q-beta-spectral-bridge`). This is an **I5 dangling
`contentBlock` reference**. Resolution options (not taken here): author the
`conj:archimedean-remainder-exponential-decay` conjecture block, or repoint
the witness to `prop:per-braid-mass-tower` (the proved prop the exponential
remainder bound is derived from). Filed as follow-up.
