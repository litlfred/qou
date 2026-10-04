# OTH slice report: OTHER + SESSION open beans (analyst KEY = OTH)

Scope: 613 open beans [M] (540 OTHER, 73 SESSION), all mapped in `OTH_mapping.tsv`. The method was a regex first pass (`OTH_classify.py`), then about 190 manual overrides made after reading titles and bodies (`OTH_build.py`, `OTH_sess.py`). Owner hard rule applied: every proposal touches beans and epics only. Beans whose *work* is a content edit (P5.CORRECT, the §7 proposals) are marked owner-gated.

Actions [M]: reparent 461 · demote-log 73 · keep 32 · dup-of 14 · close-evidence 12 · needs-owner 11 · scrap 6 · promote-epic 4. Confidence: 13 rows are `l` and the rest are `h` or `m`. Each row in the auto-routed P1.BIND bucket is a title-level judgement.

## Proposed tree for this area (the bean that IS each epic, or NEW)

**P1: L2 at 1 ppQ**
- **P1.BIND, extensive many-body binding term (9b): NEW** (121 of my beans). `b9ms` becomes its Lean sub-epic. The story column already splits it:
  - light-nucleus magnitudes (13)
  - bond-scalar / b_3 sign and Ursell (12)
  - Magnus/χ compute engine (11)
  - ħ_q trace-difference expansion c0/c1/c2 (11)
  - production-chain / atom-NF structure (10)
  - Route C groupoid / triangulation (8). Proposal: **qou-2akx (session) is converted into this story**. Its 1 kB charter body is not a log, and it has 13 open kids.
  - braid-word selection via γγ + confinement SDP (7, owner ruling 2026-09-08, `qou-ales`)
  - canonical nucleon ordering / grouped-era (6+3)
  - framing/writhe (4)
  - composition / Möbius-energy program (4)
  - NN interface scale α (2; this is *not* α_em)
- **P1.QB, Q_β / c_k / f-map under convention D: NEW.** It absorbs `qou-avtq`, `kehn`, `r2bf`, `qou-93jy` and `qou-dvlt`, with `qou-esx7` (A_ω odd-channel Stokes) as a sub-epic. 24 beans, including the A_ω/GGM cluster and the θ_K/T-series.
- **P1.DLAM = qou-x631**, with `qou-h315` (M1>0 CS-margin machinery) as a sub-epic. The 4 `qou-v8t7` children move to x631, because the feature `qou-v8t7` restates x631's Cov≤0 statement. Note that x631 is a **formal** inequality consumed by L2. It could sit in P2 with a "consumed-by P1" link: owner choice.
- **P1.HYG, convention-C excision & precision hygiene: NEW.** `qou-cdx1` is the ruling and `qou-wgta` the tracker. Stories: float64/LAUNDERED drain, q0-anchor gates, q-integer convention split (PR #7077), OLD-MUON witness drain (ex `qou-a1lw`).
- **P1.ALPHA = qou-6ufi** (with `qou-rgiz`). **P1.MU: NEW**, covering m_μ/m_e, F_Bor normalisation and the Vol(6_2) literal. **P1.MESON: NEW** (`qou-v6oz` only). **P1.MU0 = qou-ch8w** (na-Stokes / Yekutieli multiplicative integral).

**P2: Conjectures umbrella**
- Families: DILOG/volume = `qou-r9ih` (30, incl. Rivin/angle structures, 5₂ saddle sum rule, KVC anchors, vdV L4), RES/alien-C1-Stokes = `qou-frzo` (19, incl. R2-core → `qou-q04o`), KEY = `qou-wzgm`, PNP = `qou-b1je`, COLLATZ = `qcz6`, AJ = `c7vs`, §3b = `b9cj`.
- DEPTH = `qou-2q85` (transcendence-depth bridge). Promote it to a P2 family and **remove it from under qou-8lxd**: its own body [B] says it targets volume, not flavour.

**P3: Lean / Mathlib**
- `qou-6qbv` de-vacuify (17, incl. the 11 "missing hypotheses" carriers and the swarm leftovers `vvcw`/`1c24`)
- `08a2` (15: GS/jet-order, LP/SDP infra, fibration LES)
- `qou-0ap1` S_n (13, incl. Jucys–Murphy)
- `qou-utb3` Markov/TL (7)
- `rtep`, `qou-ec5z` (D2–D5), `qou-59vq`, `qou-vkmt`, `qou-5gai`, `qou-lbth`, `qou-k4oq`

**P4**
- `qou-8lxd` (19), keeping its parented children.
- **P4.SCOPE: NEW**, physics-claim scope audits (13): CCC/TQFT/QG assessments, HasAction rank-2, χ(A)=−6, matter/antimatter, dark matter, Planck length.

**P5**
- **P5.CITE: NEW** (56, the Cite/Remark-interpreting/Cross-check backlog)
- **P5.FWD: NEW** (11; promote `dtg7`)
- **P5.CORRECT: NEW** (17, statement-correctness defects; every one is an owner-gated content change)
- **P5.NOTATION: NEW** (4)

**P6**
- **P6.PROBE: NEW**, probe/witness/QA-gate integrity (37; `dgap` and `qou-v6so` as sub-epics)
- **P6.OPS: NEW**, agent-ops traps (7). These are better moved into skills than kept as beans.
- `qou-p7z5`, `qou-ty42`, `qou-j34j`

## SESSION / HANDOFF / Arc-review beans (73 open)

No session bean, open or closed epic, contains a `- [ ]` item [M]. Only 73 files in the whole store carry one, and none of them is a session bean. Handoffs list open work as prose with bean ids instead. I resolved every referenced id. **All 73 → demote-log + close.** 18 of them first need their open children reparented, per the mapping. 41 have empty bodies (len ≤ 2) [M].

Unbeaned real work found in session prose, proposed as new stories:
1. **qou-3ul5**: owner review of the "four content proposals" in §7 of `docs/audits/2026-09-07-substrate-branch-and-the-q-eq-1-interface.md` → P4.SCOPE, needs-owner (content).
2. **qou-vyvt** (owner items, defaults to no-op):
   - re-pin Li on two `carrier_saturation_mechanism_probe` assertions → P1.BIND
   - CAL-3 dataset AME-2020 vs CODATA-2022 → under `qou-mkgt`
   - held merges #6178/#6025 → P6.OPS
3. **qou-psjm**:
   - 232 class-D NARROW witness-copy findings, each needing a read
   - ~70 stale scriptHashes
   - 23 parse-guard-skipped files
   - audits scan only `computations/`, not `tools/` or `qou-mass/`
   - reference-literal fix in `qou_mass/api.py` and `_internal/y_lambda_su_n.py`

   All five → P1.HYG.
4. **qou-7r6d**: four cosmology/C-symmetry follow-ups (mirror vs C antiparticle; a Vol(mirror) lemma for `bare_mass_invariance`; density bar-parity; C-equivariance of γγ production) → P4.SCOPE.
5. **qou-9ot5**:
   - habiro drift → P1.QB
   - seminormal-matrix route at n=9 → P1.BIND
   - manifest-vs-witness anchor vocabulary → P6.PROBE
6. **qou-m6sp**:
   - 3–4 cite/compute-check actions → P5.CITE. Check sibling #6962 first.
   - JSON-LD nodes for 8 docs → P6/migration. The generator is absent at pin 428ca5c.
7. **qou-janm**: qa-sweep/render of the 3 content blocks → P1.HYG.
8. **qou-0ubf**: "TL_n: A_n presents S_n" as a Mathlib contribution → P3.SN.
9. **qou-2z9j**: a 3-batch drain plan for 159 self-assuming/trivial Lean defects → under `qou-6qbv`, unless its committed ledger already serves as the tracker.

The other referenced follow-ups are already beaned. Seven named in handoffs are already **completed** [M] (e.g. qou-hv27, qou-t9r1, qou-z0pr).

## Duplicate clusters (dup-of → survivor)

| Duplicate | Survivor |
|---|---|
| qou-0xmm | qou-9552 (completed; body says "twin") |
| qou-uts1 | qou-ml55 (completed, identical title) |
| qou-63lc | qou-b7cf (LAUNDERED 0→34) |
| qou-dygk | qou-h0ou (HasAction scalar) |
| qou-csdp | qou-ii3w |
| qou-qqzm | qou-d2s7 (same cite + block) |
| qou-c0yc | qou-07vh (atom-NF q-degree) |
| qou-ff5g | qou-8mmq (He4 two-row zero) |
| qou-ebcn | qou-zezz (A_ω GGM 3d-index, #3805; qou-ledr joins the same cluster) |
| qou-q377 | qou-qvpl (hypercharge) |
| htw2 | qou-kebu (strand-twist) |
| qou-6e88 | qou-0z7n (cauchyMul_order) |
| qou-6rmz | qou-50a7 (SDP feasibility) |
| qou-rp5f | qou-cons (body: "REDUCED TO qou-cons") |

Related but not duplicates:
- `qou-vkmt` and `qou-c8p8` both carry the title "Mathlib infra: close class field debt". This pair is outside my slice, so someone should check it.
- qou-t5m1 overlaps the completed qou-joi7 (Śniady).
- qou-wxmm overlaps qou-50a7.

## Work landed but bean still open (close-evidence, mostly m)

- **qou-pdg9**: "DERIVED both ways".
- **qou-x4zl**: closes via the telescope at X=0.
- **qou-18r3** and **qou-71ma**: the crux was answered NEGATIVE.
- **qou-qiw9**: answered.
- **qou-q3np**: literature search done.
- **qou-o1dh**: RESULT.
- **qou-n9qf**: headline withdrawn.
- **qou-i6bn** and **qou-p68e**: RETAINED adjudications.
- **qou-9rbo** (handoff) and **qou-p2d5** (prepare-merge #4657): low confidence; check whether the PR merged.
- Four in-progress beans whose only referenced branch is already an ancestor of `main` [M] (`branches.tsv`), so the work likely landed: qou-ggdk, qou-bn8e, qou-gmfz, qou-9ohz.
- **Do not close** qou-fi93 or qou-brng. (rule 13a [B]).

## Stalled claims

- 202 of 205 in-progress beans have no update for more than 14 days, i.e. since before 2026-09-20 [M]. By last-update month: June 3, July 24, August 86, September 89. The only live ones are qou-krvm, qou-0yqu and qou-weeq (all 2026-09-26).
- Oldest: thb7 (06-23), ovud (06-24), i5p0 (06-30), 8we6 (07-03), vvcw/1c24 (07-05, under the *scrapped* session uudc), qou-3lsb (07-12), qou-zezz (07-17).
- Proposal: reset all 202 to `todo`.
- "Claimed by branch" notes in my slice: only 3 [M].
  - qou-tonv → `claude/l2-1-ppq-gaps-c9zuwt`: the branch exists.
  - qou-xblo → `claude/fivetwo-level7-ladder-numerators`: the branch exists.
  - qou-jfr8 → "this session": no branch named, so the claim is unverifiable.
- No claim note in my slice names a branch that is missing from `heads.txt`.

## Owner decisions needed

1. Should **P1.DLAM (qou-x631)** sit in P1 or in P2 as a formal conjecture family?
2. **qou-2q85**: the parent move off qou-8lxd, given the scope correction in its body.
3. **qou-dap4**: its epic premise ("symbol calculus absent") is contradicted by qou-p6m1 ("PRESENT").
4. **qou-gl58**: a per-file q-integer basis determination; the handoff gates it on the owner.
5. **qou-izu7** (E_x normalisation), **qou-mc6a** (L_q), **qou-a3lh** (SnapPy pseudo-volume), **qou-ocal** (bk-crossing re-scope), **qou-7p7d**, **qou-mp5u**, **qou-1xck**: each needs an owner call.
6. **dtg7 / fwr6**: a ruling on uses[] semantics.
7. All 17 **P5.CORRECT** beans. They propose changes to math statements, which the new hard rule forbids without the owner.

## Formal vs empirical flags

- **qou-c9fh**: CS(Hopf) as the gate for `conj:binding-qbeta-complex-volume`. The P2 keystone conjecture `qou-wzgm` couples a nuclear-binding observable to complex volume. Its empirical leg must not enter a formal proof.
- **qou-fi93** and **qou-v1jg** (matter/antimatter 7.88%) and **qou-qjh8** (dark matter) are physics-scope claims. I put them in P4.SCOPE, not P2.
- The P1.BIND magnitude beans (e.g. **qou-3wvl**, **qou-2row** "derive ρ_F≈1.889") target measured values. Keep them out of the P2 conjecture carriers.

## Hygiene findings

- 18 bean files have a front-matter `# id` that differs from the filename stem [M]: e.g. `confinement_categorical.md` → `cnca`, `integration-audit-ledger.md` → `integration`. 11 of the "missing hypotheses" beans in my slice are of this kind.

## Skill gaps (where a generic folio-assistant skill would have helped)

1. **Session-log detection and close-out.** No skill turns a "Session:"/HANDOFF bean into (children reparented, prose follow-ups extracted, log closed). Handoffs carry follow-ups as prose instead of `- [ ]` items, so the store has no unchecked items to query, and the work is invisible to `beans list`.
2. **Duplicate detection at `beans create`.** Here that means similar-title plus same-target checks.
3. **Stale-claim sweep.** The 202 stalled in-progress beans show that in-progress has no expiry and no holder in practice.
4. **Epic-membership enforcement.** 534 of my 613 have no parent [M]; a gate should require one for new beans.
5. **Filename/front-matter id consistency check.**
6. **A formal-vs-empirical tag on beans and conjecture carriers**, so that P2 cannot silently absorb an empirical prediction.
