# Metallic-regime follow-ups — S(4), q↔ρ calibration, φ² literature, nova cascade

**Date:** 2026-06-09
**Branch:** `claude/wizardly-fermat-amvizc`
**Owner directive:** follow-ups to the merged metallic-q / SDP-regime thread
(#1999 → #2047 → #2049 → #2071 → #2074 → #2076), per the four-option reply
(1 y · 2 pick up stalled S(4) · 3 y · 4 check) + the nova-cascade question.

## Task list

1. **Δ_λ feed** — DONE upstream: #2076 (merged) showed the gate is a *scale*
   gate (`log₁₀|tr_M|` quadratic in A, R²=0.9999; no constant Δ_λ closes).
   Live continuations are sibling PRs #2078 (atom→V_hyp→Δ_λ workplan) and
   #2080 (operator-combiner extension). This session: coordinate, do not
   duplicate.
2. **S(4) probe** — pick up the stalled thread (synthesis §7.4 recorded the
   H₄ infra wall and stopped). Unlock: #2057 proved `pyhecke_native` builds
   from source in-sandbox (cargo ships). Build it, extract H₄(q) Markov-trace
   cost data, sweep the n=4 LP active set across the metallic ladder, test
   `S(4) ⊆ {δ_1..δ_4}`.
3. **q↔ρ calibration** — pin the q-density map using the EOS blocks
   (`prop:eos-borromean-cfl`) + nuclear saturation anchor `q₀ ↔ ρ₀`;
   predict ρ(δ_silver), ρ(φ²), ρ(δ_bronze); make the NICER kink prediction
   quantitative.
4. **φ² literature check** — gCFL/CCS transition constraints from
   neutron-star observations vs the bar-mirror prediction q = φ² ≈ 2.618.
5. **Nova / supernova cascade** (owner question) — model core collapse as a
   cascading traversal of metallic phase boundaries; simplest pre/post
   composition + energy budget; compare to observed SN energies
   (SN 1987A neutrino burst ~3×10⁵³ erg / ~10 s, then steady release).

## Status

- [ ] 2. S(4): pyhecke_native build → H₄ data → LP sweep
- [ ] 3. q↔ρ calibration compute + audit doc
- [ ] 4. φ² literature section
- [ ] 5. nova cascade model + data comparison
- [ ] 1. coordination comments on #2078 / #2080
