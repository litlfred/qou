---
# qb5s
title: 'Record the Bring-quintic / EW-twist interpretation of the Δ_λ exponent (5 per chain-site) in the audit'
status: open
type: task
priority: normal
created_at: 2026-06-15T01:27:00Z
updated_at: 2026-06-15T01:27:00Z
parent: v3po
---

Follow-up to the Δ_λ second-kind / crossing derivation merged in PR #2311
(`85d7e738`, audit `docs/audits/2026-06-14-qlommel-delta-lambda-second-kind-derived-b.md`).

**Finding to record** (interpretive — observation, not yet a proof):

- The Δ_λ q₀-exponent factors as `5·(2A−1) = 5 × (A nucleons + (A−1) bonds)`,
  i.e. **5 per chain-SITE** (nucleon or inter-nucleon bond), with NO −3 offset
  (the −3 was an artifact of using the crossing count `10A−2` as the unit).
- The per-site q-power **5 = the degree of the Bring quintic** (`𝒳₅`; genus 4,
  χ=−6, Aut = S₅, `g²=5`).
- The same odd integers recur: the Δ_λ sites give `2A−1 ∈ {3,5,7}`, and the
  categorical Weinberg angle is `cosh(5η₀)/cosh(7η₀)` — the same `5,7` as the
  EW torus-LINK twist counts `2m+1` for the W=T(2,4)/Z=T(2,6) triplet
  (`electroweak-higgs-torus-link-triplet.md`; cheat-sheet:266,271 — T(2,2m) are
  2-component links, gcd=2, and 2m+1 is the q-power of the trace polynomial
  P_m, not the second torus parameter). Cross-observable thread:
  Δ_λ chain-sites and electroweak twists draw on one odd-integer/quintic
  structure.

**Action**: add a short interpretation paragraph to the audit (or a `remark`
block) recording the quintic/EW-twist reading, clearly marked as an
*observation* pending the `q₀^5`-per-site mechanism (bean: jet-order derivation,
see sibling). New branch + PR (do NOT reopen #2311).
