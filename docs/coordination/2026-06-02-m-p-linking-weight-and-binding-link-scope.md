# Topics 2+3 — m_p linking_weight derivation + binding-link canonical object

**Date:** 2026-06-02
**Branch:** `claude/m-p-linking-weight-and-binding-link-2026-06-02`
**Trigger:** PR #1698 Subgoal-1 follow-up (merged `4cd808f05b`); owner directive "1 2 3" with coordinate.

PR #1698 isolated two structural targets that combine naturally on the proton + light-nuclei anchor set:

## Topic 2 — derive the proton linking_weight 2.532780 → 2.461648

PR #1698 verdict (final-audit): the +2.89 % m_p gap lives ENTIRELY in the proton's `linking_weight_family_a` value:
- Production Family A H₄ Wedderburn average: `(3q² + 4 + 3q⁻²)/4 = 2.532780` at q₀
- CODATA-implied (round-trips m_p): `2.461648`
- Gap: **+2.890 %** = +28900 ppm

Closing this gap on m_p **auto-closes** all atomic absolute-mass predictions to ~1 % (H2 magic-A extension is quasi-uniform across A=1→56). So Subgoal-1 is fundamentally a SINGLE-PARTICLE problem.

Subgoal-1 closure target: find a categorical derivation of the proton linking_weight that lands at 2.461648, not 2.532780. The 8 prior structural searches (`lambda-scale-absorbed-into-vol-density.md`) all refuted; not retracing them. Productive new attack vectors per PR #1698 Phase B/C/Vol audit:

- **Operator-valued linking_weight** (not scalar) — the Wenzl branching combiner (PR #1698 Phase C `class WenzlAOperator`) computes a per-atom value; the categorical linking_weight may not be a number but an OPERATOR on the Wedderburn decomposition.
- **q-Plancherel weights** instead of uniform `1/p(n)` — the H₄ uniform average is the unweighted partition sum; a q-Plancherel weighted sum at the same H_n level reproduces a different value.
- **Higher-rank H_n basis** with proper categorical normalization — H₄ is the smallest enclosing Wedderburn structure; H_5/H_6 with correct normalization may converge to 2.461648.

Following the α_em precedent (PR #1503): if the m_p closure lands at CAL-2 floor like α_em did, that's an analogous structural success. Note α_em precision floor is ~150 ppb; CAL-2 floor on m_p target is the genuine 100× σ_exp ratio, NOT below the substrate-derivation floor.

## Topic 3 — ²H / ³H canonical object = binding link (not whole-atom knot)

PR #1698 SDP run (cvxpy + Rust H_5 Hoefsmit, built this session):

| atom | historical knot | H_n | PSD-feasible? | failing blocks |
|---|---|---|---|---|
| ²H | 6_2 | H_3 | NO | standard (2,1) eig −0.89 |
| ³H | 8_11 | H_5 | NO | 5 of 7 (only [5], [1⁵] PSD) |
| ³He | L6a4 | H_3 | YES ✓ | none |

Only ³He's historical knot is PSD-canonical at q₀. The ²H/³H assignments are atlas-acknowledged reverse-engineered AME volume-matches (`manual-historical-volume-match` kludge tags), now rigorously confirmed to fail the single-block PSD-feasibility certificate.

Per `conj-canonical-knot-id-sdp.md §"Structural decomposition"`, the canonical T_w factors:

```
T_w(atom) = K(binding) ⊗ ⊗_i T_w(nucleon_i)
```

with the binding K = L_H (Hopf) for ²H, an 8_11-class link for ³H. The whole-atom knot is the WRONG SDP object — the binding link is what needs PSD-feasibility. Topic 3 attacks:

1. **Test PSD-feasibility of K = L_H (Hopf)** at H_3 — the deuteron binding link in its own right. If PSD-feasible, this discharges the historical-6_2 puzzle structurally: 6_2 was the AME-volume-matched proxy; L_H is the real canonical object.
2. **Test PSD-feasibility of K = 8_11-class link** at H_5 — same for tritium.
3. **Cross-link with #1709** — the volume-Wedderburn Δ_λ probe isolated q-6j saddle as the categorical-binding closure path; both directions (binding-link PSD + q-6j Vol_λ) attack the same Δ_λ gate from different angles. Coordinate to avoid duplication.

## Why combined

Topics 2 + 3 share infrastructure (per-atom Vol via SnapPy from PR #1698, per-atom tr_M via `markov_peel`, joint-tower SDP solver) and the proton anchor. Topic 2's closure (if found) fixes the absolute m_p, hence Z·m_p + N·m_n; Topic 3's closure (if found) fixes binding B(K) and hence atomic masses Z·m_p + N·m_n − B(K). Together they close the production mass-formula at categorical-derivation level.

## Coordination (siblings flagged)

- **#1521** α_em Habiro categorical ID — DEPENDENCY for Topic 1 (not this branch); same framework methodology might inform Topic 2 if linking_weight turns out to be Habiro-element-derivable.
- **#1709** volume-Wedderburn Δ_λ probe — OVERLAP+CHERRY for Topic 3; cite their q-6j-saddle isolation.
- **#1516** Option E Phase 2 — DEPENDENCY for Topic 3; parallel Δ_λ path (Kashiwara crystal vs binding-link).
- **#1503** α_em subgoal-1 closure — DEPENDENCY for Topic 2; precedent for CAL-2-floor structural-derivation closure.

Intent comments to be posted on each.

## Out of scope (forbidden per AGENTS.md)

- New ansatz fits for either linking_weight or Δ_λ (Δ_λ gate discipline — 6 ansätze refuted).
- Reintroducing `λ_scale` as a separate object (purged 2026-05-23).
- H₃ per-block trace as linking_weight (regresses m_p −56.7 %).
- Subgoal-2 absolute-precision targets below CAL-2 floor.

## Cross-references

- PR #1698 (merged): [`4cd808f05b`](https://github.com/litlfred/qou/commit/4cd808f05b)
- Final verdict: [`docs/audits/2026-06-02-subgoal-1-final-verdict.md`](../audits/2026-06-02-subgoal-1-final-verdict.md)
- SDP + multi-term + tritium: [`docs/audits/2026-06-02-subgoal-1-sdp-multiterm-and-tritium.md`](../audits/2026-06-02-subgoal-1-sdp-multiterm-and-tritium.md)
- Canonical reference (refuted routes): [`docs/lambda-scale-absorbed-into-vol-density.md`](../lambda-scale-absorbed-into-vol-density.md)
- Conjecture: [`content/quantum-observable-universe/mass-theory/conj-canonical-knot-id-sdp.md`](../../content/quantum-observable-universe/mass-theory/conj-canonical-knot-id-sdp.md)
