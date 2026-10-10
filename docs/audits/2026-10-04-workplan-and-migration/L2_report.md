# L2 — "PROGRAM — L2 at 1 ppQ": proposed epic tree (analyst KEY = L2)

**Scope:** every bean with slice = L2: 555 open and 525 closed `[M]`. **No bean, file or content was changed.** Every proposal is about beans, epics or PRs only (owner hard rule: no math or physics content is changed). Where a bean is marked `scrap`, only the bean is closed. Content stays.
**Anchor:** `docs/audits/2026-09-08-l2-1ppq-research-program-gaps.md` (§0–§8), the 09-07 reanalysis (amended 09-13), and the 09-12/09-13 audits on z_D, b₃, γγ and cds1 `[D]`.
**Mapping:** `out/L2_mapping.tsv` has 563 rows `[M]`.

## 1. Proposed tree

The P1 root is **NEW** ("PROGRAM — L2 at 1 ppQ"). Its body should state the 09-08 frame:
- L1 (compute precision) is met. L2 is 1/6 scoreable and 0/6 unconditional.
- Four un-derived objects remain: the Q_β functional under D, the extensive binding term, the m_μ/pin tension, and the α_em conditional classes.
- It should cite the six predecessor articulations, which are 1qug, vibo, m2ay, ggdk/65jh, `qou-37j2` (completed) and tonv `[D]`.

| epic (key) | bean that becomes the epic | stories (story bean) | open members `[M]` |
|---|---|---|---|
| **QB**: Q_β on the ruled z_D base (R1) | **`qou-avtq`** (promote and retitle; a queue milestone, stale since 08-26) | phase `qou-pdix` · D-frame ladder `qou-cds1` (+ re-score `qou-iagg`) · f-map `qou-i2ir` · c₃ front `qou-dvlt` · element/ε `qou-99qc` (EXPO slice) · A_ω/odd-channel `qou-esx7` (demote from epic, pre-D, needs re-scope) | 61 |
| **BIND**: the extensive many-body term (R2) | **`qou-v2om`** (already titled EPIC, owner-picked 08-26) | kernel `qou-brng` · γγ word selection `qou-ales` (OTHER slice; owner ruling 09-08) · two-body/deuteron `qou-8274` (owner decision) · Δ_λ magnitude, parked per §7.4: `qou-6snb` · census retirement `qou-sa60` · compute `qou-sv7h` · Lean 9b `b9ms` | 120 |
| **9A**: step-9a chosen joints (R3) | **NEW** | joints red-team `qou-n04i` · absolute-mass excision `qou-exam` (demote from epic) · TL-vs-H₃ fibre `qou-n1dj` | 30 |
| **ANCHOR**: pins, μ–p tension, calibration | **NEW** | q₀-gate ledger `qou-1c4y` · muon-pin edition `qou-tekx` · μ–p structural `qou-6gf9` (OTHER) · CAL layer `qou-mkgt` (paused by owner) · CODATA/AME vintage `qou-cgbd` | 38 |
| **AEM**: α_em chain + meson leg (R4) | **`qou-6ufi`** (low confidence: its body is empty and its scope is narrower, B2 τ only, so it must be retitled or replaced by a NEW epic) | reconcile the two α_em `qou-aemx` (CONJ) · per-loop measure `qou-rgiz` · B2 τ `qou-6ufi` children · m_K/m_π `qou-dhck` | 18 |
| **CONV**: convention-C excision | **`qou-cdx1`** (owner-ruling milestone 08-15) | ledger `qou-wgta` (canonical per §8.4 C3) · witness regeneration `qou-eea0` · Gram singularity `qou-cds2` (LEAN slice) | 47 |
| **PREC**: precision hygiene (float64, dps, gates, witness currency) | **NEW** (the owner may prefer to move it to P6) | `qou-f64g` · `qou-p77d` · `qou-fl9i` · red-on-main ledger `qou-z23u` (successor of completed `qou-sknx`) · NEW "witness currency" story | 89 |

**Out of P1** (reparent; detail is left to the sibling analysts):
- P5 (citations, remarks, cross-checks, prose): 58
- P3 (Markov trace, Wenzl, TL, cited-sorry Lean): 51
- P4 (SM, leptons, OBS): 23
- P2 (`qou-x631`, a *formal* combinatorial conjecture; 5₂; wzgm children): 10
- P6 (qou-mass vendor, platform): 8
- logs: 5

`qou-x631` stays an epic, but under P2, with a cross-link to BIND, because its result feeds k(A)=O(log A).

Candidates that should not become epics:
- **t7qv** is a 126 KB session log, so `demote-log`.
- **kehn** (CONJ slice) is a 06-24 pre-D near-match milestone. Make it a history story under QB.
- **r2bf** and **qou-93jy** are empty milestones, so mark them `dup-of`.
- **qou-ch8w** and **dgap** are not in the L2 slice. They are cross-links only.
- **qou-janm** and **qou-mu5i** are session beans that belong under CONV as logs.

## 2. Duplicate clusters (read from bodies, not only titles)

| survivor | duplicates | basis |
|---|---|---|
| `qou-exam` | `qou-9uto` | 9uto is an empty-body EPIC from 08-04; exam is the owner-ruled successor from 08-11. The 08-04 tasks (loqn, n4u6, g937, tknh, v266) move under exam. |
| `qou-wgta` | `qou-nsih`, `qou-emyt` | Owner-authorised C sweeps on 08-09 and 08-30, re-measured by the canonical ledger. `qou-janm` (session) is a log. |
| `qou-eea0` | `qou-cdh3`, `qou-q0zk` | One task (regenerate C-frame witnesses) counted three ways: 14, 99 and 84. |
| `qou-y6h7` | `qou-ondw` | Both re-pose the LP/SDP on TL_n = H_n/rad. |
| `qou-1c4y` | `qou-cds3` | The same muon→proton witness migration (870 vs ~840 witnesses). |
| `qou-tekx` | `qou-2361`, `qou-2zw0`, `qou-khac`, `qou-58sa` | One defect: two muon pins (CODATA-2018 vs 2022) in circulation. |
| `qou-fl9i` | `qou-yh08` | Sub-canonical dps (838 vs 952 sites). |
| `qou-4pmk` | `qou-dqhd` | Identical event: he-nu-sdp float64 went 5→11 (fcc65c1380). |
| `qou-xbh4` | `qou-nc5h` | Identical: VOL_6_1 built at dps 15. |
| `qou-rgiz` | `qou-5et6` | The same α_em per-loop-measure lever. |
| `qou-v6wz` | `qou-u6cz` | The same qbeta-ck-basis-constrained-pslq witness. |
| `qou-dvlt` / `qou-i2ir` | `qou-93jy` / `r2bf` | Empty milestones. |
| `qou-kr8a` / `qou-zko1` / `qou-0w3s` | `mass_categorical_descent` / `skein_mass_from_linking` / `qou-wfhf`, `50p7` | The same Lean targets (these belong to P3). |
| `qou-a0j7` | `qou-9rlz`, `qou-78bm` | Recurring observations of qou-mass vendor drift (P6). |
| `qou-bhrx`, `qou-cc97`, `qou-juz3` | `qou-0vsu`, `qou-nkzs`, `qou-ja0k` | Markov-trace infrastructure (P3). |

**Related but not duplicates** (cross-reference them, keep both):
- `qou-hytc` vs `qou-p77d`: tolerance fields vs computed/expected fields.
- `qou-5ipv` vs `qou-dhck`: different m_K/m_π defects.
- `qou-u14x`/`qou-pzzl`: both have empty bodies and are only probable duplicates (low confidence).

The **ratchet-red event family** has 10 open beans (7kq3, hlp5, 6ixs, ah1m, ldwx, 58zq, 5sg8, nwhg, kn46, 4pmk). Put them under `qou-z23u`, as §6.3 item 6 found.

## 3. Work landed on main whose bean is still open (`close-evidence`; 18 proposals, all `[M]` from `git log origin/main`)

- `qou-06wh` 84489c2f56
- `qou-qgtk` 73c2db9b41 (18→0)
- `qou-mnrd` 8f32d1fac5 ("CLOSE — main is GREEN")
- `qou-ishr` 832635a1c8 (43,901→0)
- `qou-gqt5` bdba6f731e
- `qou-gzs0` 22affaed24 (the body itself recommends closing)
- `qou-212w` 0d7261f40f
- `qou-brg3` 1d30ba8736
- `qou-wlaf` ac5d45bbb8
- `qou-9ies` 4d7f192bad
- `qou-xwet` 74e7bdb5cc
- `qou-txru` 1c4cc27775
- `qou-uujo` 2b8206e504
- `qou-qflp` b89969ad1d
- `qou-tbk7` ede90ce982 (answered negative)
- `qou-6tcn` 860bf06333
- `qou-rbdi` 33ccc1895b
- `neutron_proton_splitting` 1be9bf9ec0

**Do not auto-close:** `qou-7vm4`, `qou-8xb1`, `qou-ftuv` and `qou-s2gm`. Each was closed on main and then reopened by the §13a sweep (a61496dbc). `qou-1jw9`, `qou-36i2`, `qou-7e1t`, `qou-bmz8` and `qou-prjo` carry a closing commit but their bodies say "stays open". All nine are `needs-owner`.

## 4. Stalled claims

- 130 L2 beans are `in-progress`. **122 have had no bean update and no main commit since 2026-09-20**, and 63 since 2026-09-04 `[M]` (date = max of front-matter `updated_at` and last main commit naming the id).
- Only 8 were active after 09-20: cds1, 7xa5, 840k, p77d, 301d, 8iru, epxx, s7z2.
- Heavily worked claims that went quiet: `qou-brng` (187 commits, last 09-14), `qou-pdix` (89, 09-14), `qou-sv7h` (52, 09-12), `qou-1c4y` (46, 09-11), `qou-x631` (38, 09-11), `z2bn` (68, 08-23), `t7qv` (67, 09-07).
- Every candidate epic is stale: avtq and v2om since 08-26, 6ufi since 07-24.
- **104 of 555 open L2 beans have an empty body** `[M]`. They cannot be triaged without the commit log.
- Only 60 of 555 have a parent `[M]`.

## 5. Open PRs that belong to L2 epics `[M]` (open_prs.txt plus branch head subjects)

- **QB:** #7441 (pdix), #7123, #6361, #6342 (cds1)
- **BIND:** #7407, #7216, #6358 (brng); #7225 (ix0x); #7229 and #6307 (compute); #6357 (vbyi); #7418 (u5qs, bond product); #7419 (hok7); #7210 (vyvt merge ledger); #6359 (Milnor route 3)
- **P2, cross-link to BIND:** #7218 (za3q/gba1 → x631)
- **ANCHOR:** #7205 (CAL-2 Q_β dataset AME→CODATA, *staged for owner decision*); #6178 (AME registry)
- **AEM:** #6350 (m_K/m_π conditionality); #7402 (oots)
- **PREC:** #7443, #7440 (oiz3); #7318; #6025; #7477 (precision-gate triage)
- **CONV:** #5402 (j4mn C-frame jet)
- **Not L2:** #7481 and #5352 (P3, TL arc); #5338 (P2, Whitehead volume conjecture); #7401 (unclear: pole-to-cusp)

## 6. Decisions only the owner can make

1. **Epic owners for AEM and for the NEW epics.** I recommend promoting `qou-6ufi` only if it is retitled to the R4 scope. Otherwise make AEM a NEW epic, with 6ufi as the B2 story.
2. **The Δ_λ magnitude family (22 beans).** §7.4 says "do not re-open". The options are to park them under the `qou-6snb` story (recommended), or to scrap the beans (bookkeeping only; content stays).
3. **The pre-ruling "wire X into canonical_mass" beans** (`qou-1tne`, `qou-8du0`, `qou-59i6`, `idt1`, `qou-qb9e`, `qou-s077`). Most have empty bodies and predate the anti-fit and no-census rulings. Each is a scrap candidate.
4. **`qou-8274`** (is the level-local H₆ deuteron word the binding object?). This is explicitly an owner decision.
5. **Whether PREC belongs in P1 or P6.**
6. **The nine re-close or keep cases in §3.**

## 7. Flags: an empirical value inside a formal statement (no content change proposed)

- **`qou-4paj`:** Lean axioms assert |m_n(q₀) − 939.565| < 1.
- **`neutron_proton_splitting`:** the closing commit 1be9bf9ec0 *adds a `codata_agreement` field* to a Lean class.
- **`qou-4zu7`:** `single_calibration_framework`.
- **`qou-nzi9`:** `GapA4MuonBranching.target_correction_constraint`.
- **`qou-kx92`:** classes that conclude `:True`.
- **Two classes in §5.2 of the anchor doc:** `QbetaCkTruncationCanonicalClass` (its field c₃ = J_Hopf(1) axiomatises a 3.47 % near-match) and `QOU.Borromean.MassFormula` (its class fields compare to CODATA).

Each of these mixes a measured number into a Lean statement. They should be separated as empirical claims and kept apart from the conjecture umbrella.

## 8. Skill gaps a generic folio-assistant skill would have solved

1. **A per-bean evidence tool** listing the commits, PRs and branches for each bean, and flagging open beans that have closing-language commits. Here it had to be done by grepping commit subjects; such a tool would have produced §3 directly.
2. **A dedupe guard on `beans create`.** It would have prevented the families counted three ways (C witnesses 14/99/84; dps 838/952; muon pin ×5).
3. **A stalled-claim sweep** that uses commit dates. `updated_at` under-reports activity.
4. **An empty-body lint.** 104 open beans have no body.
5. **A `session-log` bean type.** "Session:" beans are typed `epic` and pollute every epic query.
6. **A check of prose parenthood against front matter.** The 09-08 doc's "parented to qou-cds1" has no front-matter parent behind it.
7. **The folio-assistant MCP server did not connect in this session**, so `skill_list` and `work_plan_prime` were unavailable.
