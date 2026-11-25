---
# qou-of4i
title: 'GAP: why the derived log binding law overshoots the deuteron by +27.4% under convention D (E_0 scale vs p-n letter weight)'
status: in-progress
type: task
priority: normal
created_at: 2026-11-25T11:23:57Z
updated_at: 2026-11-25T16:29:38Z
parent: qou-s028
---

Owner ruling 2026-11-25 ('3y sibling'), relayed by parent session. Derivation only; choosing d_pn or E_0 to hit AME is a fit and is forbidden. Two candidate loci per docs/audits/2026-08-08-binding-functional-attack-vectors-and-li2q-guard.md §10b: (a) E_0 as the nucleon-nucleon interface scale; (b) the p-n interface weight (1/2 - delta/4). Context bean qou-xj4p, PR #9421. Child session of the qou-xj4p session.

## 2026-11-25 findings (PR #9424, branch claude/deuteron-overshoot-loci-2026-11-25)
- The +27.4% is on the single-crossing letter that the 2026-11-15 gg ruling supersedes. On the ruled gg chain word the deuteron is UNBOUND (mu_pn = 1.000611191 > 1; LightNucleiGGChainSign.lean, sorry-free; audit 2026-11-22-light-nuclei-a2-a3-gg-chain). The live question is binding at all (qou-brng).
- (a) Live producer uses order-zero E0 4.18598, not the ruled tower form 4.22748 (+28.62% with it). Lean UniversalScaleMinimax: one universal scale cannot do better than (r2-r1)/(r1+r2); floors 23.93% (2H-3H), 61.17% (2H-4He). E0 as the NN scale is NOT derived (qou-91w7, qou-y3bm).
- (b) (1/2 - delta/4) is asserted. Derived alternatives overshoot more: 1/[2]_q +31.45%, T=0 mu- = 1/[2]_q^2 +162.9%. Only bare sigma undershoots (-7.82%).
Stays open: the loci are scope-(a) negatives on the old letter; the deuteron on the ruled word is open (qou-brng). Owner decision pending: align binding_log_free_energy.py to qbeta_e0.canonical()?

## 2026-11-25 locus (a) closed on the corpus premises; Lean verified
BondScaleUniversality.lean: trace-only energy forces one scale (a·log x + b·log y = G(xy) => a=b). With route T (spectator audit §8-9) the common scale is k_BT = E0 (order zero). So on those premises an NN-specific scale is excluded; the locus is mu (the bond word). UniversalScaleMinimax.lean: minimax floor (r2-r1)/(r1+r2). Both lean-direct exit 0, standard axioms. Precision gates green. PR #9424.
Still open (do not close; the deuteron on the ruled gg word is open in qou-brng): owner decision on order-zero vs tower E0 in binding_log_free_energy.py.

## 2026-11-25 owner ruling 'A ruled tower' applied (commit f1c5d61db, PR #9424)
binding_log_free_energy.py + probe_d_dressing_is_proton_net.py + probe_d_dressing_cross_a.py now use qbeta_e0.tower_summed_scaled (new). E0 4.185981 -> 4.227483 MeV (+0.9915%). Log-law binding: 2H 2.83316->2.86125 (+28.62%), 3H 6.6309->6.6967, 3He 4.8839->4.9323, 4He 8.6817->8.7677. Probe-d E0*h*net(p) ansatz 0.78365->0.79142 MeV (vs Kashiwara Q_beta 0.107%->1.10%); probe-d binding negative -75.22%->-74.98%. Baselined on_scale assertion unchanged (already false). Precision gates --changed: NEW 0. NOT switched (outside named scope): forced_link_normalisation_bond_counting, cyclic_triple_under_log_law, normalised_law_residual_shape, surface_exponent_is_dimension probes (own order-zero E0).

## RESUME STATE (session end, 2026-11-25T16:30Z)
Branch claude/deuteron-overshoot-loci-2026-11-25, head f1c5d61dbbf57475899d185cd17a0fb3f8292e7c, pushed, tree clean. Draft PR #9424 (body current).
Done: probe computations/probes/deuteron_overshoot_loci/ (RESULTS.md §0-5); Lean QOU/Nuclear/UniversalScaleMinimax.lean + BondScaleUniversality.lean (lean-direct exit 0, standard axioms); owner card 4 'A ruled tower' applied (f1c5d61db); precision gates NEW 0.
Branch is 68 commits behind main: the merge manager should merge main before /prepare-merge. Possible conflict surface: binding-log-free-energy.witness.json and probe-d witnesses if main touched them.
Open: (1) owner decision whether the four other log-law probes with their own order-zero E0 should switch (listed in RESULTS §5); (2) the deuteron on the gg-ruled word is unbound (mu_pn > 1), owned by qou-brng. Do NOT close this bean (Rule 13a: the deuteron derivation is open).

## OWNER DECISION (framed, not taken): do the four other log-law probes move to the ruled tower E0?
DECISION: card 4 ('A ruled tower') moved the log producer and both probe-d probes. Four more probes compute their own order-zero E0 = m_e/(q0(q0-1)) = 4.185981 MeV: forced_link_normalisation_bond_counting_probe, cyclic_triple_under_log_law_probe, normalised_law_residual_shape_probe, surface_exponent_is_dimension_probe (all computations/probes/). They take only M_E_MEV from the producer, so the ruling's named scope does not reach them. The question is whether it should.
FACTS: none of the four writes a witness (no WitnessBuilder, no json dump); they print only. Shape and exponent results (residual shape, surface exponent P) are ratios, so the scale cancels. One quoted number does move. The 'required factor 3.0075 against 3 strands per nucleon' (normalised_law_residual_shape, surface_exponent, quoted in docs/audits/2026-09-04-normalised-law-residual-shape.md and qbeta_strand_multiplicity_probe.py) is (max B/A)/eps with eps = E0*ln[2]_q. Under the tower E0 it becomes 2.9780 (= 3.0075/1.0099145), i.e. from +0.25% above 3 to -0.73% below it.
OPTION 1, switch all four to qbeta_e0.tower_summed_scaled. Means: one E0 across every log-law script. Cost: 4 one-line edits, no witnesses, minutes. Risk: printed MeV values move +0.99%; the 3.0075 near-match becomes 2.978, and the 2026-09-04 audit text then quotes an order-zero figure. Reversible. Commits to: the tower factor (ruled, not derived, qou-y3bm) being used everywhere on the binding surface.
OPTION 2, leave them, labelled. Means: add a comment in each saying it is order-zero by design or by history. Cost: 4 comment lines. Risk: two E0 forms stay live on the binding surface, which is the inconsistency card 4 just closed for the producer. Commits to nothing.
DEFAULT (no answer): nothing changes; the four keep order-zero; no witness is affected.
RECOMMENDATION (my judgement): option 1, since no witness depends on them and one scale on the binding surface is what card 4 asked for. Record the 3.0075 -> 2.978 move next to the audit so the 'factor 3' near-match is not quoted on the old scale.
