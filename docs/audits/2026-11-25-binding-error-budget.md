# Binding error budget: where the light-nucleus binding errors come from

**Date.** 2026-11-25. **Bean.** `qou-rf43` (epic `qou-s028`). **Owner request, verbatim:**
*"please do a DEEP analysis of where binding errors could be coming from."*

**Scope and method.** Light nuclei ²H, ³H, ³He, ⁴He, with ⁶Li and ⁷Li where a number exists, against
AME 2020. Owner handover the same day (token budget): no new probes and no long computation. So every
number below is either (i) read from a committed witness or a sibling PR's results, with its source, or
(ii) re-measured here in seconds with mpmath at 50 dps (scratch script, no witness, marked **[rm]**).
Nothing is tuned to AME, and AME appears only in comparison columns. Items that need heavy compute are
left as framed open entries (§5).

Owner ruling for scope, relayed 2026-11-25: *"Term-by-term, same scope as now"*. Linking neutrality
applies to each B₃ term within the 2026-11-21 scope only (γγ nucleon word plus gluon vertex); it is not
ruled for six strands or H₂.

## 0. The answer in one paragraph

On the **ruled** inputs (γγ bond, convention D, proton pin, tower E₀, log functional), the light nuclei
are not "a few percent off": they are bound by **keV, not MeV**, and on the production nucleon blocks
they are **unbound** at every q > 1. The +27 % deuteron that was quoted until this week came entirely
from a bond letter the 2026-11-15 γγ ruling superseded. The dominant error is therefore **missing binding
structure**, not a mis-set scale or a numerical defect: a γγ-admissible bond carries a trace drop of
order 10⁻³, three orders of magnitude below what AME needs, and no pairwise assembly of such bonds can
make b₃ positive. Scale, pin, convention and numerics together move the answer by about 1 %.

## 1. Ranked table

Ranked by the size of the effect on the **ruled** pipeline. "Status" is one of derived (Lean or exact
ℚ(q)), ruled (owner), conjectural, asserted, or fitted.

| # | Source | Measured effect (sign, size) | Status | Deciding artefacts |
|---|---|---|---|---|
| 1 | **Bond word (γγ selection)** | ²H moves from **+27.4 %** (superseded letter `σ_g + d_pn`) to **−99.7 %** (selected bond V(2)³, B = 6.36 keV at tower E₀). The 408 passing γγ bond words span **−0.16 to +7.67 MeV**; none within 5 % of AME. Factor ≈ 350 on ²H. | ruled (γγ rule 2026-11-15; owner card 1, cheapest pure-junction word, `FrobeniusSelected`) | `computations/probes/gg_deuteron_bond/results.md` (draft PR #9426); `docs/audits/2026-11-15-gg-rule-rescopes-old-letter-binding.md`; `QOU/Mass/GammaGammaFrobeniusSelection.lean` |
| 2 | **Missing super-pairwise / many-body term** | Needed: b₃^AME = (B(³H)+B(³He))/2 − 3B(²H) = **+1.426 MeV** [rm]. Available: b₃ < 0 for every bond triple in (0,1)³ (Ursell alternation); a two-bond chain needs a sign-mixed pair. On the superseded word the ⁴He gap is 56 % many-body even after all pairs are counted. | derived exclusions (Lean); the positive term itself is **open** (`qou-brng`) | `UrsellPartitionFunctionB3`, `B3SignOneRoot.b3corpus_chain_neg`, `AggregatorConvexity`; `docs/audits/2026-11-21-he4-binding-breakdown.md` §3; `docs/audits/2026-11-24-b3-extensive-ep-cell-carrier.md` |
| 3 | **Nucleon word (production blocks vs γγ V³)** | Sign flip of the γγ deuteron: production blocks give ratio 1.000611 (pn) / 1.001058 (np), B = **−2.6 / −4.5 keV**; γγ nucleons V³ give 0.998497, B = **+6.4 keV**. With V³ nucleons p = n, so the cell cannot tell ²H from the diproton or dineutron. | production chain sign: derived (Lean, generic ordered field, every q > 1); γγ nucleon: ruled cheapest; flavour: **open** (Phase B) | `docs/audits/2026-11-22-light-nuclei-a2-a3-gg-chain.md`; `QOU/Mass/LightNucleiGGChainSign.lean`; PR #9426 |
| 4 | **Bond topology (chain vs all pairs)** | On the superseded word, all pairs instead of A−1 neighbours closes **44 %** of the ⁴He gap (8.58 of 19.53 MeV). On the γγ bond it does not help: all-pairs ⁴He B_log = **−17.9 to −18.3 keV**, chain −9.6 keV (all four formation routes, both transports). | chain: derived (Lean); all-pairs: measured at q₀ only, not proved | `computations/probes/he4_gg_all_pairs/he4-gg-all-pairs.witness.json`; he4 breakdown §3 |
| 5 | **Energy scale E₀** | Tower vs order-zero: ×**1.00991** [rm] (+0.99 % on every B). One universal scale cannot beat the minimax floor t = (r₂−r₁)/(r₁+r₂): ²H–³H **23.9 %**, ²H–⁴He **61.2 %** (on the superseded L's). A third chart, E_osc = m_e/(q₀−1)², is **10.09 × E₀** [rm] and is what the K_A plaquette rows of `ACCURACY.md` use. | tower form ruled (2026-09-05, card 4 2026-11-25); reading E₀ as an energy **open** (`qou-91w7`, `qou-y3bm`); E_osc chart not ruled for binding | `QOU/Nuclear/UniversalScaleMinimax.lean` (PR #9424); `docs/audits/2026-11-22-energy-scale-cal-map.md`; `computations/probes/gap1b_4he_tetrahedral_k4_flux_ring/RESULTS.md` |
| 6 | **Isospin / mirror splitting** | AME B(³H) − B(³He) = **0.764 MeV** [rm]. Every γγ cell computed so far has p = n, so its mirror splitting is **0 by construction**: a 100 % miss of that observable. | **open** (needs flavoured nucleons, Phase B) | PR #9426 §Scope; `computations/probes/a3plus_gg_candidate/results.md` |
| 7 | **Coulomb E_C not subtracted** | Corpus E_C(⁴He) = 0.77 MeV, reported beside B, not subtracted. Textbook uniform-sphere sizes [rm, comparison only, not a model term]: ³He 1.00, ⁴He 0.91, ⁶Li 2.38, ⁷Li 2.26 MeV. Subtracting widens every gap. The Coulomb pair term is **not reachable** in the n = 6 braid image (α + β = 1 is an identity in ℚ(q)). | E_C: DERIVED* (Witten-κ `sorry`); unreachability: symbolic-exact n = 6 | `docs/audits/2026-11-22-coulomb-all-q-and-nucleon-writhe.md`; he4 breakdown §2 |
| 8 | **Functional** | None within its premises: B = E₀·log(tr_free/tr_atom) is forced by trace multiplicativity plus extensivity (Cauchy). The residual risk is the extensivity premise, which the dashboard tags POSITED. Raw/linear trace differences are retired. | derived (Lean) given premises | `QOU.Nuclear.LogFormUniqueness` (#9423); #9421; skill `production-vs-exploratory-discipline` Antipattern 7 |
| 9 | **Trace convention (D, z_D, y_λ two-row)** | Ruled; the only live effect is historical: the probe-d +0.29 % hit existed only under the excised convention C with the grouped word (tr_free ≈ 1 there). Under D the three-row weight vanishes identically, so there is no truncation error to budget. | ruled + derived (`ocneanuWeight_conventionD_eq_zero_of_three_rows`) | #9416, #9417; owner ruling 2026-08-15 |
| 10 | **Full tower vs order-zero (2026-09-03)** | Enters only through E₀ (row 5, +0.99 %). No binding producer evaluates the trace on the full fibre object; order-zero observables only. Effect at trace level **unmeasured**. | ruled in principle; not implemented for binding | AGENTS.md §"full tower" ruling; `qou-y3bm` |
| 11 | **q₀ pin (proton vs muon)** | μ–p shift 1.16 × 10⁻⁸ relative [rm]. Bond binding scales as y⁴–y⁵ (y = q²−1), so ΔB/B ≈ **4.9 × 10⁻⁷** [rm]. Negligible. | ruled (proton pin, CODATA 2022 muon) | `qou_substrate.constants`; owner rulings 2026-08-15, 2026-08-22 |
| 12 | **Confinement SDP reading** | Readings 1 and 2 are stricter than reading 3 (proved), so they can only remove passing bonds, never add binding. | derived | `qou-ales`; PR #9426 |
| 13 | **Comparison data** | AME 2020 vs CODATA 2022 deuteron values agree to < 1 keV; irrelevant at the keV-vs-MeV scale of rows 1–3. | — | witnesses cited above |
| 14 | **Numerics** | Closed-form chain equals the exact trace to 1.8 × 10⁻⁴⁹ MeV (⁴He); controls ≤ 2.5 × 10⁻³⁰. mpf end to end. | — | he4 breakdown §2; he4-gg-all-pairs controls |

## 2. The chain, step by step (substrate → MeV)

**(a) Word.** Nucleon block × bond letters × closure. Rows 1, 3, 4. This is where almost all the error
lives. The bond word decides the order of magnitude, the nucleon block decides the sign, and the topology
(chain vs all pairs) decides the A-dependence. Under the γγ rule the admissible bonds are those whose
words pass reading 3 at every level. The cheapest is V³, whose expansion
V³ = (2h² + h⁴)V + (1 + h²)·1 (`GammaGammaVertexOrder.lean`) is close to the identity at q₀ (h² ≈ 0.04),
so its trace ratio is 1 − O(10⁻³). That is the structural reason the binding is keV-scale: an
admissible bond is a near-identity in the Hecke algebra at q₀.

**(b) Trace.** Convention D, Ocneanu trace at z_D, proton q₀. Rows 9, 10, 11. Ruled and numerically
clean. Contributes nothing measurable except through E₀.

**(c) Functional.** log ratio. Row 8. Forced within its premises.

**(d) Scale.** E₀. Row 5. +0.99 % between the two ruled-era forms; a minimax floor means no universal
scale can repair A-dependence; the categorical-energy reading of E₀ is open.

**(e) Comparison.** Rows 6, 7, 13. The mirror splitting is not represented at all in the γγ cells, and
Coulomb is neither subtracted nor reachable in the n = 6 braid image.

## 3. What the old headline numbers were measuring

| Number in circulation | Where | What it actually rests on |
|---|---|---|
| ²H +27.4 % (log law) | #9421, probe-d | superseded single-crossing letter; record only |
| ²H +0.29 % (probe-d) | 2026-07-04 | excised convention C + grouped word; withdrawn (#9417) |
| ²H +1.81 %, ⁴He +3.65 % (K_A plaquette, `ACCURACY.md` Table 3.2a) | `gap1b_4he_tetrahedral_k4_flux_ring` | E_osc chart (10.09 × E₀), not the ruled binding pipeline; the γγ bond does not appear |
| ⁴He 3.26× low (B_sym) | 2026-11-21 dashboard | superseded interface letters, A−1 chain |
| A ≥ 5 −69 % (Q-CLT) | `ACCURACY.md` Table 3.2b | 1D symbolic proxy, not the trace pipeline |

**Critical-distance flag (judgement, not a finding).** The K_A plaquette rows are the only light-nucleus
binding numbers within a few percent, and they are read out in a different energy chart (E_osc) from
every trace-pipeline row (E₀). A factor-of-ten choice of chart with no ruling to select it is a hidden
degree of freedom in the sense of AGENTS.md §"NO FITTING": the ²H row of that table is the `#9221`
baseline, and whether E_osc was chosen because it lands ²H has not been checked here. Until it is, those
rows should not be read as evidence that the binding is understood.

## 4. Consequences

- The binding problem on ruled inputs is **"why does an admissible bond carry almost no trace drop"**,
  not "why does the deuteron overshoot". That is bean `qou-brng`, sharpened.
- A positive b₃ of +1.43 MeV must come from a term outside every pairwise or Mayer/Ursell assembly with
  bonds in (0,1): an attractive channel (bond factor > 1, sign-mixed, deuteron bound and di-nucleons
  unbound), a convex aggregator through the origin, or an unsigned cell-sum carrier
  (`B3ExtensiveCellSumCarrier`). None is derived on the γγ word.
- Scale, pin, convention, numerics and the functional together are worth about **1 %**. Effort spent
  there cannot move the answer by the factor of 10²–10³ the word-level rows require.
- The mirror splitting (0.764 MeV) and Coulomb cannot be addressed until p ≠ n in the γγ cell.

## 5. Open entries (need compute or an owner decision; nothing started here)

1. **Flavoured γγ nucleons (Phase B).** Running in sibling session `session_01EucfRmaNiqxRg52fQZeNVB`.
   Decides rows 3 and 6. Heavy: four-strand words, reading 3 per level.
2. **All-pairs γγ sign, proved.** Row 4 is measured at q₀ only. A Lean extension of
   `LightNucleiGGChainSign` to transported non-neighbour bonds would make it scope (b). Moderate.
3. **E_osc chart provenance.** Whether `#9221` selected E_osc against ²H. Cheap (read the PR), not done
   for budget reasons. If it was, Table 3.2a of `ACCURACY.md` carries a fit.
4. **Full-tower trace for binding.** Row 10 at trace level. Heavy.
5. **⁶Li, ⁷Li on the γγ word.** No γγ number exists. The chain theorem says the production-block chain
   unbinds for every A ≥ 2, so only the sign is known. Heavy (A ≥ 5 traces).
6. **Non-trace energy map.** The scope-(b) chain unbinding does not cover a non-trace energy map; the
   extensivity premise of row 8 is the place such a map would enter.

## 6. Owner decision this raises

**Decision: should `ACCURACY.md` Table 3.2a (K_A plaquette, ²H +1.81 %, ⁴He +3.65 %) carry a note that
it is not the ruled binding pipeline?**

Why it needs the owner: the scorecard's labels were ruled 2026-11-24 (*"keep the generator's labels"*),
and this would change what a reader of the paper's Accuracy dashboard takes as the binding result.

- **Option 1 — Add a scope note to the generator.** *Means:* the table states that those rows use the
  E_osc chart and production plaquettes, not the γγ bond on the trace pipeline, whose ²H is −99.7 %.
  *Costs:* one template line in `scripts/generate-accuracy-scorecard.py`, regenerate. *Risks:* none to
  numbers; the dashboard looks worse. *Commits to:* reporting the ruled pipeline's number beside it.
- **Option 2 — First check E_osc provenance (open entry 3), then decide.** *Means:* read #9221 to see
  whether the chart was chosen against ²H. *Costs:* one short session. *Risks:* none. *Commits to:*
  nothing until the check is done.
- **Option 3 — Leave it.** *Means:* the dashboard keeps showing few-percent binding. *Risks:* a referee
  compares it with the trace pipeline and finds a factor 350 between them.

**Default (no answer):** nothing changes; this audit records the discrepancy.
**Recommendation (judgement):** Option 2, then Option 1 — it is cheap and it tells us whether the only
good-looking binding numbers are a fit.

## 7. Provenance of [rm] numbers

Scratch script, mpmath 50 dps, `qou_substrate.constants.q_at()` (proton) and `q_muon_at()`:
q₀ = 1.10997858275138080759…, E₀ = 4.18598136329447589694… MeV, E₀ tower = 4.22748335562903055026…
MeV (ratio 1.00991451913…), E_osc = 42.2477681091499537704… MeV (E_osc/E₀ = 10.0926794561…),
μ–p relative shift 1.1614 × 10⁻⁸, b₃^AME = +1.4262 MeV, mirror 0.763755 MeV,
−E₀^tower·ln(0.998497160633) = 0.0063580 MeV. The Coulomb sphere values use 3/5·αħc·Z(Z−1)/(1.2 A^{1/3} fm)
with αħc = 1.44 MeV fm, as a textbook size estimate only.
