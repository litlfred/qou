# Coordination ledger — PR #916 `claude/lambda-scale-alts-strategy-d`

**Date:** 2026-05-22
**Branch:** `claude/lambda-scale-alts-strategy-d-2026-05-22`
**PR:** [#916](https://github.com/litlfred/qou/pull/916)
**Goal:** Enumerate alternatives to Strategy D in the 2026-05-22
q-dilog-tower brief, run cheap structural tests, fold results back
into the brief.

## Scope map (at /coordinate run, 2026-05-22 evening)

| PR | State | Classification | Relationship |
|----|--------|----------------|--------------|
| **[#916](https://github.com/litlfred/qou/pull/916)** (this) | open | **own** | Strategies F (Markov), G (Skein), H (Wedderburn V_7) + brief addendum |
| [#917](https://github.com/litlfred/qou/pull/917) | open | aligned | Post-#895 dashboard refresh: Family A predictions surfaced |
| [#909](https://github.com/litlfred/qou/pull/909) | open | **constructive sibling (framing-affected)** | Strategy D stage-1 exploration; treats `5/2 − h²·G + ...` as leading order (FRAMING-B), needs realignment per below |
| [#904](https://github.com/litlfred/qou/pull/904) | merged 2026-05-22 | aligned | `prop:lambda-scale-bring-bloch-identity → conj:` (vacuous-rfl + PSLQ tier 0-5 refuted) |
| [#892](https://github.com/litlfred/qou/pull/892) | merged 2026-05-22 | aligned | `prop:mobius-limit-from-thimble → conj:` (curve-fit CAL-4 face) |
| [#895](https://github.com/litlfred/qou/pull/895) | merged 2026-05-22 | **cluster anchor** | Rust LR adapter + `LAMBDA_PROTON_DOC` → Family A everywhere; the canonical Framing-A decision |
| [#888](https://github.com/litlfred/qou/pull/888) | merged | precursor | `LAMBDA_PROTON_DOC → LAMBDA_PROTON_FITTED_FROM_CODATA` truth-in-naming |
| [#701](https://github.com/litlfred/qou/pull/701) | open (predecessor) | source-of-truth | Family A theorem proved; `5/2 − h²·G` falsified across 5 structural routes |

## §6 Framing inconsistency surfaced + resolved

A semantic split on the symbol `λ_scale` was active across open
PRs at the time of /coordinate:

- **Framing A** (cluster — #701, #888, #892, #895 merged):
  `λ_scale := λ_A(q) = 5/2 + (3/4)·h²` (Family A theorem).
  Framework m_p prediction = 966 MeV, ~3 % off CODATA.
  The 3 % gap is honest framework state. `5/2 − h²·G` is
  **falsified** (PR #701).
- **Framing B** (#909 stage-1 + initial commits of this PR):
  `λ_scale := value closing m_p to CODATA = 2.4599527869`.
  Family A is one candidate (off by +2.96 %); `5/2 − h²·G` is
  the leading-order match (5.6 ppm), next-order open.

Per §6 escalation, the repo owner selected **Framing A**. This
PR's initial commits (`fcee22c5` + `31dc075c` + `925e3601` +
`92772aa1`) were written in Framing B; commit `36a568e8`
realigns to Framing A.

**Outstanding Framing-B holdover:** PR #909 still treats
`5/2 − h²·G` as leading-order in its stage-1 exploration. Its
findings #1 ("Leading-order ansatz confirmed: `λ_scale ≈ 5/2 −
h²·G` matches the 32-digit closure target to −5.619 ppm") and #2
("Next-order term is approximately −h⁶/6") need Framing-A
reinterpretation. Will post a coordination comment on #909.

## Headline findings (post-realignment)

### 1. Strategy F (Markov-trace identity on β_Bor) — naive form does not hold

`|tr_M((σ_1^{-1}σ_2)^3, q_0)| · ℏ_q²/Vol(𝓑_3) = 0.00134` vs
Family A 2.5328 (and vs CODATA target 2.4600), three orders of
magnitude off. The H_3 Markov trace and the H_4-Wedderburn-
derived Family A measure different invariants of the Borromean
substrate; no consequence for Family A. Strategy F closed.

**Witness:** [`lambda-scale-alt-f-markov-trace-beta-bor.witness.json`](../../computations/lambda-scale-alt-f-markov-trace-beta-bor.witness.json)

### 2. Strategy G (Skein-family polynomial direct eval) — no single-polynomial match

Best ratio-form `5/2 − ℏ_q² · ⟨𝓑_3⟩(q_0^{1/2}) = 2.4604` at
+165 ppm vs CODATA target, ~2.86 % from Family A. Lands in the
same numerical-coincidence basin as PR #701's falsified
`5/2 − h²·G` form (different structural ingredients, same
basin). Closed for single-polynomial; multi-orientation
HOMFLYPT (Strategy J) is the remaining Skein direction.

**Witness:** [`lambda-scale-alt-g-skein-polynomial-direct.witness.json`](../../computations/lambda-scale-alt-g-skein-polynomial-direct.witness.json)

### 3. Strategy H (Wedderburn variant scan) — V_3, V_4 are refinement candidates; V_7 is a coincidence

Probe `probe_family_a_variants.py` scanned 8 natural functionals
on H_4 character data:

  | variant | h² coeff | at q_0 | vs Family A | vs CODATA tgt |
  |---|---:|---:|---:|---:|
  | V_1 (Family A) | +3/4 | 2.5328 | 0 | +2.89 % |
  | **V_3** | +5/6 | 2.5364 | **+0.14 %** | +3.04 % |
  | **V_4** | +7/12 | 2.5255 | **−0.29 %** | +2.59 % |
  | V_7 (quotient) | −13/16 | 2.4652 | −2.67 % | +0.144 % |

- **V_3 and V_4** land within ±0.3 % of Family A while keeping
  substrate-pure / positive-h² / sum-form discipline. **Real
  candidates for a Family-A refinement** if a categorical
  justification picks one over the other (e.g. Frobenius-pairing
  weighting vs hook-content weighting). Recommend probing
  whether either has a natural derivation from H_4 Plancherel
  measure.
- **V_7** lands close to the CODATA target (+0.144 %) but
  disagrees with Family A by −2.67 %. Per PR #701's exhaustive
  falsification of the `5/2 - ε·h²` family hitting CODATA, V_7
  is in the same coincidence basin — not a substrate-pure
  candidate.

**Witness:** [`family-a-variants-investigation.witness.json`](../../computations/family-a-variants-investigation.witness.json)

### 4. Brief addendum (§Alternatives to Strategy D) appended

The 2026-05-22 q-dilog-tower brief now carries eight
alternative strategies (F–M) with empirical results inline and
recommended ordering. Primary direction remains the original
brief's Strategies A/B (q-dilog tower PSLQ); V_3/V_4 refinement
and Yekutieli curvature are the secondary substrate-pure paths;
Strategy D is the last resort.

## Outstanding coordination work

- [ ] Comment on [#909](https://github.com/litlfred/qou/pull/909):
      its stage-1 finding #1 ("`5/2 − h²·G` leading order")
      contradicts PR #701's falsification of that form. Suggest
      reframing as "the residual `target − Family A` lives in
      the same coincidence basin as `5/2 − h²·G`" — same
      numerical fact, Framing-A-correct interpretation.
- [ ] If V_3 / V_4 substrate justification probe lands, comment
      on #917 to update the per-observable 100× dashboard with
      the refined prediction.

## Reference

- Brief:
  [`docs/agent-briefs/2026-05-22-lambda-scale-qdilog-tower-direct.md`](../agent-briefs/2026-05-22-lambda-scale-qdilog-tower-direct.md)
  §Alternatives to Strategy D
- Family A theorem:
  [`computations/lambda_scale_all_c_i_family_a.py`](../../computations/lambda_scale_all_c_i_family_a.py)
- Family A variant scan:
  [`computations/probe_family_a_variants.py`](../../computations/probe_family_a_variants.py)
- Predecessor ledger:
  [`docs/coordination/2026-05-18-lambda-scale-falsification.md`](2026-05-18-lambda-scale-falsification.md)
- Predecessor ledger:
  [`docs/coordination/2026-05-20-lambda-p-followons-ledger.md`](2026-05-20-lambda-p-followons-ledger.md)
