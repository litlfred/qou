---
# qou-vyvt
title: 'Session: agent-consolidation-binding 2026-09-07 — stalled-agent takeover (round 2), merge sweep, chi scaling, Q_β elements, binding SHAPE toward L2'
status: in-progress
type: epic
priority: normal
created_at: 2026-09-07T18:25:01Z
updated_at: 2026-09-12T07:52:49Z
---

Branch claude/agent-consolidation-binding-1jtf80. Owner instruction 2026-09-07 (round 2 of the stalled-agent takeover; sibling round 1 is #7121 / qou-6g7j with fronts observable C, #7092 coboundary, Z-resolved b3, REV Σβ, SandwichReduces — NOT duplicated here). This session: merge every clean open PR; take over the fronts #7121 left: the chi producer scaling wall (#7083), the Q_β ℚ(q)-coefficient leg (#7118), and the binding SHAPE residual (symmetry-energy term of the additive log law), which the owner names as where most of the binding gap sits. Goal statement: L2 toward 1 ppQ; binding is not an L2 row and must not be quoted as one (1ppQ reanalysis §5 item 3).

## 2026-09-08 ~04:25Z status
- qou-kvgn merge sweep: DONE (10 merged, replay-verified; see bean).
- qou-zunl chi scaling wall: DONE on PR #7160 (carrier bean on that branch is qou-s7ld). ⁵Li 2.5 s / ⁶Li 8.5 s all partitions via level-local seminormal path-sum; five matrix-m caches were on the grouped word and are regenerated on borromean. Four deltalambda/ consumers NOT re-run.
- qou-0e2p Q_β ℚ(q) leg: DONE on PR #7164 (that branch carries the superset copy of the bean; on rebase keep it). Over ℚ(q) the bar-odd criterion is vacuous; over the bar-fixed field F=ℚ(q+1/q) Δ_L has exactly one bar-odd line and it is NOT a Markov trace (ab(q−z_D)²=0 obstruction); Δ_S bar-odd on the whole span in every row. The 'Q_BETA_MEV truncation' premise was inverted: the registry value is σ-limited; the 8.8e-10 was the witness's own float64 M_N rounding. OWNER DECISION raised in #7164 §4: CAL-3 Q_β from AME-2020 (0.78233341(61), default) or from the CODATA-2022 registry m_n−m_p−m_e (0.78233355931(38), +191 ppb, 116 consumer files, Δc₃≈+0.309).
- qou-qve5 binding SHAPE: still running (branch claude/binding-shape-symmetry-term-edge-set-2026-09-07, BondCutSymmetry.lean in progress).
- Agents CAN push and open PRs (create_pull_request reached them via the hook); the earlier 'mcp__github__* not exposed to subagents' TRAP applies to the merge-coordinator agent type's tool list, not to general-purpose dispatches.

## 2026-09-08 ~04:30Z — all four fronts landed
- qou-qve5 binding SHAPE: PR #7165 (2 commits, 20 sorry-free theorems in QOU/Hecke/BondCutSymmetry.lean + BondCutSymmetryLogBound.lean, axioms propext/choice/Quot.sound only; probe 14/14). HONEST NEGATIVE, scope-(b): cut identity B = (e_pp d_P + e_nn d_N)/2 + δ·n_pn, δ = e_pn − (e_pp+e_nn)/2 — all layout dependence is the p–n cut times δ. Segregated layouts (corpus chain, constant cut) ⇒ affine in (Z,N), no (N−Z)² at all; well-mixed ⇒ one symmetry term E₀δk/4 with SEMF sign iff δ>0; corpus δ = −0.02176 (wrong sign); convex interface bounds δ ≤ 2 ln q₀ = 0.2087 so max a_A^eff = 2.65 MeV at k=12 vs 23.7 target; positivity forbids neutron-matter unbinding on any graph/interface. The symmetry energy needs a term OUTSIDE positive pair-additive bond counts = the qou-brng extensive object. Bean qou-qve5 stays OPEN (rule 13a; positive target unclosed). The branch carries the superset copy of the qou-qve5 bean; on rebase keep it.
- Agent notes: SessionStart lake-build-bg had filled the disk twice (killed by agents; 875M partial .lake left in main checkout); q_at() in qou_substrate.constants returns float64 — precision item for that module's arc.
- Open PRs from this session: #7129 (ledger), #7160, #7164, #7165 — all non-draft, mergeable, agent-verified; merge awaits owner permission (rule 7).

## Tranche 2 (2026-09-08 ~08:00Z) — after 'merge and continue': #7160 43e3e1b305a, #7164 d32f83379f5, #7165 e928329504d, #7129 5566ddffd69 all rebase-merged, replay-verified. Held merges #6178/#6025 NOT merged (recommended against; the generic 'merge' is read as the four session PRs). CAL-3 dataset decision (#7164 §4) still open. Dispatched: qou-nmuz (deltalambda consumer re-runs), qou-hxz4 (binding-word level-locality), qou-v8ct (E₀ factor 2.656).

- 08:11Z qou-nmuz DONE → PR #7172 (all four deltalambda consumers moved on borromean Li; saturation probe stays 3-red with a rotated set; re-pin of two Li assertions is an owner option). bind-local (qou-hxz4) and e0-scale (qou-v8ct) still running.

- 08:20Z qou-hxz4 DONE → PR #7173 (honest negative: binding words not level-local, obstruction is the fixed-H_k embedding; re-embedding on 3A strands is an owner-level re-derivation, option 2). e0-scale (qou-v8ct) still running.

- 08:25Z qou-v8ct DONE → PR #7174 (scope-(a) negative: uniform factor is 98.6 % of the log-residual and undecidable vs bond factors at fixed law; scale is downstream of shape). TRANCHE 2 COMPLETE: #7172 #7173 #7174 open, mergeable, awaiting owner merge permission; ledger #7168.

## Tranche 2 MERGED 2026-09-11 ~14:35Z (owner: 'merge. and continue / ok to overlap')
All four rebase-merged and replay-verified by patch-id, every commit replayed: #7172 92d5cd579a5 (6/6) · #7173 463668610c1 (4/4) · #7174 fe8fd214c73 (3/3) · #7168 ledger 438df617985 (5/5).
Phase-4 gate evidence (no CI exists; agent-owned verification IS the gate): precision-gates.sh --changed on all three substantive PRs — exit 1 on the standing corpus-wide ratchets, ZERO red lines naming any branch file (grepped per-branch stem). #7174 Lean QOU/Hecke/BindingScaleCandidates.lean compiled FROM SOURCE against the pinned Mathlib olean tree, lean -DautoImplicit=false -s 65536 exit 0 (154 s), and #print axioms on ALL 18 theorem/lemma declarations = [propext, Classical.choice, Quot.sound], no sorryAx. NOTE: the PR body says '15 decls / 12 theorems'; the file actually carries 18 theorem+lemma decls and all 18 are axiom-clean — the body UNDERSTATES its own coverage. mirror-drift-audit --baseline clean (no new live shadows). #7172 and #7173 touch no Lean. Copilot requested on all three; none arrived in ~18 min and again after 3 days idle (0 reviews, 0 threads) — merged on agent verification per the zero-live-external-gates rule.
Re-verified before merging that main had moved only 1 commit (ef2e7d9d710 -> 61d93c97ff0) touching 1 file, no overlap with any PR and no .lean, so the 3-day-old gate results still described what was merged.
Session branch restarted from main at 438df617985. Worktrees reclaimed; disk 9.2 GB free.
STILL OPEN FOR THE OWNER (all default to no-op): repin li on the two carrier_saturation_mechanism_probe Li assertions; CAL-3 dataset AME-2020 vs CODATA-2022 registry (#7164 §4); held merges #6178 / #6025; 3A-strand re-embedding of the binding producer (#7173 option 2).
TRANCHE 3 dispatched: qou-brng (extensive-term route) with owner-authorised overlap on #7155.

## Tranche 3 (qou-brng) MERGED 2026-09-11 ~15:20Z — PR #7181, 653eae78a5a, replay 3/3.
Result: scope-(b) structural exclusion of the MULTIPLICITY sub-channel of the trace/spectral class. A trace sum Σ_λ y_λ χ^λ Δ_λ can be large two ways — one summand large, or many summands. The second is capped by the triangle inequality at log(card), one-sided in the deciding direction; with card = p(3A) and Hardy–Ramanujan (carried as an explicit _of_ hypothesis, NOT proved) that is O(√A). ⁵⁶Fe would need 10^50.6 summands against p(168) = 10^11.4 (short 39.2 orders); ²³⁸U short 159.0. Scale-free headline (E₀ cancels, which matters because #7174 made the scale undecidable): normalised at ¹²C the binding ratio outruns the multiplicity ratio 1.140 (¹⁶O) → 3.191 (²³⁸U), GROWING — a constant mismatch would be a scale error, a growing one is a shape error. Honestly recorded non-bite: at A=2 the cap EXCEEDS the binding 4.56×, exactly as the explicit threshold A > (c/a)² predicts; the exclusion bites from ⁴He up.
The reusable part is the ENUMERATION: four classes outside #7165, each against a NAMED hypothesis of bondSum_nonneg / bondSum_ne_semf_neutronMatter — A 3-body (already blocked 3 ways: MayerThreeBodySign, BrunnianTripleExhaustion, BodyOrderRecurrenceDepth), B non-sign-definite bond energy (LIVE, smallest escape, what the physics wants — a repulsive bond is what unbinds neutron matter; qou-ib3g measured b>1 at m=2), C trace/spectral (escapes on BOTH hypotheses; multiplicity sub-channel now excluded), D fibre-level/higher order in q (LIVE, and the 2026-09-03 full-tower ruling makes it non-optional long-term).
Live remainder, sharper: an extensive term in the trace sum must live in the DOMINANT SUMMAND's log-weight log|y_λ χ^λ(β_A)| — the 3A-strand word has length Θ(A), the right growth class. This is an unconditional counting reason for the concentration BindingConcentration.lean argues from LP sparsity: there it is a property of the chosen LP, here it holds whatever LP is written.
PARENT-SESSION INDEPENDENT VERIFICATION (not taken on the agent's report): both Lean files compiled FROM SOURCE in import order against the pinned Mathlib tree, lean -DautoImplicit=false -s 65536 exit 0 (3 s + 4 s); #print axioms on all 11 declarations = [propext, Classical.choice, Quot.sound], 0 sorryAx, 0 errors. check-sidecars exit 0 and CONFIRMS the §7c split (generic file 'no ℝ, generic OK'; ℝ file 'archimedean construct present, ℝ justified'). precision-gates --changed exit 1, and a grep for all four branch stems across the full log returns ZERO lines. mirror-drift --baseline clean. (Minor: the PR body says '11 RED gates', my run counted 9 RED headings — a grep-shape difference, not a disagreement; both agree zero reds name a branch file.)
Bean qou-brng STAYS OPEN (rule 13a). The 0.95·ℏ_q² match was not used, wired, or forced, and no route was ranked by residual.


## Tranche 4 (2026-09-12, owner: 'do all') — the five open decisions

Branch restarted at main 396baaeb4ea (41 commits behind). Three fronts dispatched
in parallel; two settled locally.

- **repin li — DONE, PR #7206.** Three pins, not two: li6_amplification_reproduced
  82.85481->164.35298, anchor_kappa5Li_reproduced 64.10282->143.39659, and
  carrier_band_ratio_pinned 1.50250->4.83238 (NOT in the owner option; flagged as
  such in its source note — it is max/min of m_e.S and both moving entries are the
  two Li rows, so leaving it red is a false red). Cause: 07d6584d94e (#7160)
  regenerated the 5Li/6Li matrix-m ATOM chi caches onto the borromean word. NOT a
  goalpost move: main's COMMITTED independent-route witness
  (carrier-table-convention-d-rederivation, Frobenius/MN, shares no path) already
  carried 143.39658.../164.35298..., so main was internally inconsistent; re-running
  that route leaves its witness byte-identical. Two-route agreement 6.8e-50 (5Li),
  3.1e-49 (6Li). Band ratio corroborated only to 1.6e-11 REL, gap carried entirely
  by 4He the minimum (1.55e-11 rel, pre-existing LR-vs-Frobenius); stated in the note.
  Probe 7/10 -> 10/10. Gates exit 1 on standing ratchets, ZERO reds naming either file.

- **CAL dataset — PR #7205 (agent), NOT merged.** Q_beta is the CAL-2 proxy, not
  CAL-3 (label corrected). AME-2020 0.78233341(61) vs CODATA-2022 registry
  0.78233355931(38), +190.85 ppb = 0.208 sigma. c_3 -2.0693 -> -1.7605 (-14.93 %);
  the |-2-c_3|/2 near-match DEGRADES 3.47 % -> 11.98 %. **L2 Q_beta miss 164.0 ->
  223.9x, WORSE** — the agent's own correction of a figure #7164 sec4 and its first
  two commits had as 139.5x/'closer': that holds the target at the AME sigma, but the
  dashboard scores each determination against 1/100 of ITS OWN sigma and the registry
  is more precise, so the target tightens faster than the residual improves. Exactly
  one dashboard row moves; headline stays 1/6 scoreable. Blast radius re-measured:
  187 tracked files (NOT 116) — 120 live .py consumers, 126 .json carrying the
  literal, 19 dated audit docs deliberately left. New cost found: under the registry
  codata_constants' own m_n-m_p-m_e cross-check becomes CIRCULAR (7.4e-17 by
  construction) where under AME it was a real 0.22-sigma comparison. Separate
  exemption-1 commit: CodataEntry.value is ALREADY mpf so float() was an active
  downcast; Q_NEUTRON_MEV error 9.15e-14 -> 4.24e-59 MeV (the 9.15e-14 is 117x the
  L1 1-ppQ target). Prior claim corrected: q_at() returns mpf, not float64.

- **class B — DONE, PR #7204 (agent).** Class B escapes bondSum_nonneg and NOT the
  cap: BondCutSymmetryLogBound.energySlope_convex_le never takes b <= 1, so
  delta <= 2 ln q was never a consequence of positivity. Of #7165's 20 declarations
  exactly two carry an energy sign hypothesis. 20 new sorry-free declarations,
  sec7c split, lean -DautoImplicit=false -s 65536 exit 0, #print axioms clean on all
  20. Derived bond factors (convention D, proton pin, exact Fraction):
  b_pp = 0.6126880371 = z_D EXACTLY; all three energies POSITIVE, so the corpus's own
  law is not in class B at all. a_A^eff <= 2.647 MeV at k=12 with NO sign hypothesis
  (9.0x short of 23.7). Sweeping m=1..12 DOES flip the sign from m=2 and still reaches
  only 5.963 MeV, 4.0x short. Three scope-(b) + one scope-(a). Class B's exclusion is
  WEAKER than the positive class's — it runs through the magnitude cap, not layout.
  Open question sharpened: what derived object puts b_pn more than 5x below both
  like-species bonds? Also: qou-ib3g's '0.335/0.984/1.709' are ENERGY RATIOS
  L(m)/L(1), not bond factors (b(3) = 0.8485/0.5139/0.2122).

- **reembed 3A — running** (agent, branch claude/binding-word-3a-reembedding-2026-09-12).

- **held merges — BOTH measured; my earlier recommendation on #6025 was WRONG.**
  #6025 does NOT widen raw-float64-baseline.json: it DRAINS it (files 1100->1098,
  fields 46467->35400) via the sanctioned deprecated-f64 carve-out, both required
  fields present, reported by name. But it is fully SUPERSEDED: 10 of its 12 files are
  byte-identical on main (Rust sources, the 429,020-line witness, the stamping script),
  main's audit witness already lists joint-tower-sdp-rust 11057 in
  deprecated_f64_carved_out_by_file, and the only 2 differing files are ones where the
  branch is BEHIND (1098/35400 vs main's 1004/30990). Merging would re-inflate the
  baseline ~94 files. Recommend CLOSE as already-landed; comment posted.
  #6178: 3,881 commits of main since its merge-base, 238 conflicts INCLUDING .py
  sources, 0 of 404 files matching main. Its central claim ('every witness compared
  against a fresh run of the same producer in the same container') is void on a
  resolved tree. Re-execution, not a rebase. Comment posted recommending extraction
  of its live findings instead.

- **Extracted from #6178 and FIXED — PR #7206 commit 2.**
  probe_chirality_delta_lambda_the3_diagnostic has raised TypeError on every run
  since c86e55ec9; reproduced on main. The other two producers #6178 named were
  repaired independently since. ALSO A PRECISION FIX: Q0_PROTON is
  qou_substrate.constants.Q, the float64 constant, so passing it injected binary64
  into a 50-dps computation; the closure's q0 comes from the witness at full
  precision and is the same anchor (q0Anchor 'proton', q0Value == Q_50_DIGIT_STR to
  22 digits). Redundancy now CHECKED by assertion at rel_eps 1e-15, so a muon-pinned
  witness fails loudly instead of straddling. Probe exit 0, 1/1, witness regenerated
  for the first time since the breakage.


### Tranche 4 closeout (2026-09-12)

- **reembed 3A — DONE, PR #7202.** The obstruction is NOT what #7173 named. #7173 blamed
  the fixed-H_k embedding; measured, the decider is the COUPLING GRAPH, which changing the
  embedding does not touch. _step_chain_generic emits one inter-nucleon letter per previous
  nucleon = C(A,2), the COMPLETE graph K_A; atom_braid_word_3A bonds only consecutive
  nucleons = A-1, the PATH P_A (measured A=2..6: 1/3/6/10/15 vs 1/2/3/4/5). Exhaustive over
  all A! orderings A=2..7: contiguity implies path, K_A reachable iff A<=2. Dropping
  contiguity does not rescue it — K_A is layout-realisable iff A<=6, but over EVERY
  K_A-realising layout the max contiguous nucleon triples is 2/3 at A=3 and ZERO at A=4,5
  (234 / 5736 / 64986 layouts). A=2 is the sole exception and IS level-local (~8x faster),
  and the value MOVES: same H_6, same 23 letters, chi^lambda differs on 9 of 11 partitions
  of 6, max rel 1.43, lambda=[5,1] going -0.827 -> +3.216. So option 2 is a re-derivation,
  as the owner was told. Probe 18/18, 70 dps, cross-checked <1e-45; ContiguousCouplingGraph.lean
  7 decls sorry-free. Corpus defect found and fixed: hecke_core_legacy.py:1040-1042 asserted
  'chi_lambda(sigma_k) is independent of k (class function), so any embedding ... yields the
  same trace' — premise true, conclusion FALSE (chi is a class function on the GROUP, not of
  the multiset of letters); that one sentence answers this PR's question wrongly. Note the
  sibling site at :1004 is TRUE (in (2,2), rho(sigma_1) and rho(sigma_3) are the same matrix)
  — the agent caught its own misattribution before it landed. Bean qou-w6x3 completed;
  residual owner decision framed in qou-8274 (default: do nothing).

- **PARENT-SESSION INDEPENDENT VERIFICATION of class B (#7204), not taken on the agent's
  report.** The agent verified inside its own worktree, which was reclaimed, so this was
  re-done from scratch in the main checkout. Built the 4-module cone from source with
  lean-direct against the restored Mathlib tree (3480 oleans; NO lake build):
  BondCutSymmetry 8s, BondCutSymmetryLogBound 4s, BondCutSymmetryNoSignDefinite 5s,
  BondCutSymmetryNoSignDefiniteLogBound 4s — all exit 0 under
  'lean -DautoImplicit=false -s 65536'. #print axioms on all 20 declarations by
  fully-qualified name: 20 checked, 0 sorryAx, 0 errors, 19 on
  [propext, Classical.choice, Quot.sound] and bondSum_energyShift alone on [propext] —
  reproducing the agent's report EXACTLY, including that one strictly-weaker outlier.
  (Note for the next agent: scripts/lean-library-sweep.py needs --package QOU here and
  still bails — this container has no QOU olean tree at all, only dependency packages, so
  the 4-module lean-direct cone is the route that works.)

- **#7204 was left as a DRAFT by its agent although the work was complete** — undrafted
  here. #7202 likewise ready. Both awaiting owner merge permission (rule 7).
