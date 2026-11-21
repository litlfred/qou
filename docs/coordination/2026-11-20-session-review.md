# Review of older qou sessions (W6) — 2026-11-20

Workstream W6 of the 2026-11-20 coordinator plan (PR #8526). Data: `2026-11-20-session-review.json` (per session, per item). Supersedes the partial file at `89ba08e712`.

## Headline

- **311** session ids seen (main history + open/closed PR bodies + bean bodies). 212 HAS-OUTSTANDING-WORK, 68 COMPLETE, 30 SUPERSEDED, plus 4 ids that are not real session ids.
- Outstanding items: **109** open PRs and **1242** open beans. Of the beans, **142** are `todo` (real queued work), **510** are `in-progress` and updated since 2026-11-13, and **590** are `in-progress` but untouched since before 2026-11-13 (claims nobody is working).
- **Almost every outstanding item already lives in a bean or a PR**, so the chat sessions themselves are not needed to resume the work. That is why the SAFE TO ARCHIVE list at the end is long.
- claude.ai chats: this session has **no** `recent_chats` / `conversation_search` tool (not in the tool list, not in ToolSearch). The previous W6 run had them and they returned nothing for every query from this Project-bound session. **Plain claude.ai chats are therefore not reviewed here**; only Claude Code sessions that left commits, PR links or bean links.

## Method (reproducible)

1. `git fetch --depth=2000 origin +refs/heads/main:refs/remotes/origin/main` (main 2026-07-24 … 2026-11-19); group commits by the `Claude-Session:` trailer (15,380 of 19,713 commits carry one).
2. Open PRs (412) and PRs closed since 2026-09-15 (518) via REST; a PR belongs to a session if its body links the session id, or (for the 304 open PRs with no link) if one of its commits carries the trailer — only 2 did.
3. Beans mounted (`state-mount`, 5,779 beans). A session touched a bean if one of its commits names the bean id (`qou-xxxx`, or a backticked 4-char id that exists) or the bean body names the session.
4. **Classification.** HAS-OUTSTANDING-WORK = the session links an open PR, or it is the *last* session to touch a bean that is still `todo`/`in-progress`. SUPERSEDED-BY *x* = its only open beans were touched later by session *x*. COMPLETE = all work merged and every bean it touched is `completed`/`scrapped`.
5. **Routing** walks each bean up its `parent:` chain to a known epic (table below); open PRs are routed by the coordinator plan, else `claude/*` → W5, batch → W4. **mechanical vs research-open** is by epic, then by title keywords — a heuristic, check before acting.
6. 01Qmmkt\*/0151ZZJ\* sessions are treated as children of coordinator `01AgoHcE` (column `parent` in the JSON).

**Limits.** Commits with no trailer (4,333) are not attributed. Bean ids named only in prose without `qou-` are missed. `in-progress` does not mean anyone is working on it; the dangling-claim count is the honest reading. Nothing here verifies that a bean’s work is actually done or not done.

### Epic → workstream map

| workstream | epics |
|---|---|
| W1 mass proof (Lean) | `qou-59vq` EPIC: quantum Schur-Weyl / Hecke Wedderburn f, `qou-wp3h` Step-9a chosen joints (m_p/m_e chain), `qou-vo9t` Session: Bring obstruction coefficients + Yek, `qou-d8c7` Mass endomorphism |
| W2 mass/binding compute & precision | `qou-v2om` EPIC: close the low-isotope binding defect — , `qou-9nnz` Precision hygiene: float64, dps, gates, witne, `qou-10v9` PROGRAM: L2 at 1 ppQ (mass and binding accura, `qou-cdx1` MILESTONE: excise convention C, adopt proton , `qou-trd0` Witness, probe and QA-gate integrity, `qou-2002` Anchors, mu-p pin tension and calibration, `qou-avtq` MILESTONE: attack-vector queue (Q_beta / c3^o |
| W3 photon/QED | `qou-3l2l` alpha_em chain (and the m_K/m_pi meson leg), `qou-20sx` Weak-isospin (up/down-type) grading orthogona |
| W4 batch Lean PR triage | `qou-8lxd` EPIC: eightfold way / SM derived from QOU, `qou-rtxm` Lean / Mathlib foundations, `qou-6qbv` De-vacuify Lean :True carriers — replace with, `qou-mub3` Exposition drain and chapter work, `qou-c8p8` Mathlib infra: close class field debt, `qou-5p7n` EPIC: §3b disclosure backlog — 125 of 147 sel, `qou-1oif` S_n / Specht / SYT / RSK residuals (programme |
| W5 legacy claude PR triage & ports |  |
| W7 NEW — platform & bean hygiene (proposed) | `qou-5vkl` Platform, tooling and hygiene, `qou-n4r9` EPIC: migrate qou onto the cat-harness platfo |
| W8 NEW — open conjectures outside the mass chain (proposed) | `b9cj` UMBRELLA: open conjectures (formal mathematic, `qou-r9ih` Dilog conjecture: cusp closure + Part B toolk, `qou-frzo` EPIC: q-native alien calculus — the C1 succes, `qou-n4nr` Conjectures: volume conjecture and hyperbolic, `qou-m6dn` Conjectures: Hecke / KLR / Markov / Wenzl, `qou-qs0e` Quark state: definition on the q-tower, facto |
| OWNER owner-gated statement-correctness reports (qou-q4oa) | `qou-q4oa` Statement-correctness reports (owner-gated co |

Beans whose chain reaches none of these epics go to W7 (hygiene) by default.

## Outstanding work by workstream

| workstream | open PRs | todo beans | in-progress (recent) | in-progress (dangling) | mechanical | research-open |
|---|---|---|---|---|---|---|
| W1 | 3 | 2 | 53 | 24 | 7 | 75 |
| W2 | 6 | 18 | 201 | 222 | 163 | 284 |
| W3 | 7 | 0 | 15 | 13 | 6 | 29 |
| W4 | 52 | 34 | 135 | 87 | 130 | 178 |
| W5 | 41 | 0 | 0 | 0 | 12 | 29 |
| W7 | 0 | 66 | 23 | 142 | 215 | 16 |
| W8 | 0 | 21 | 83 | 91 | 8 | 187 |
| OWNER | 0 | 1 | 0 | 11 | 3 | 9 |

### W1 — mass proof (Lean)

Open PRs from older sessions:

- #8523 Port the core of #7551: fibre quantum trace on V^⊗3, fake instances removed — session `0151ZZJz`, updated 2026-11-19 (mechanical)
- #8522 Port #7418 onto main: the single-crossing chain factorizes — session `0151ZZJz`, updated 2026-11-19 (mechanical)
- #8365 Bring foundations: χ(A) = −6 → χ_eu(M_0), flag the five trace sites, drop two P→P tautolog — session `0151ZZJw`, updated 2026-11-19 (research-open)

Queued (`todo`) or high/critical beans (12; full list in JSON):

- `qou-ywyq` [in-progress, critical, research-open] GOAL #1: prove the trace equals the multiplicative integral (def:mass-identity) — last session `01A1cKZc`
- `qou-0xk8` [in-progress, high, research-open] T3/D2: Čech-cocycle gerbes and cocycle-level Yekutieli Thm 4.17 — last session `01CffL64`
- `qou-507c` [in-progress, high, research-open] NS follow-up: re-derive or re-scope the NS singularity chain after item 3 retraction — last session `01CffL64`
- `qou-533l` [in-progress, high, research-open] Formalize Yekutieli central-extension-of-gerbes theorem for the brane tower (tiered) — last session `01CffL64`
- `qou-5zl1` [in-progress, high, research-open] Lean: trace factorisation tr_z(W_atom) = prod_bonds (z+d_k) * P_p(z)^Z * P_n(z)^N on a concrete brai — last session `01M5GA1L`
- `qou-bvxd` [in-progress, high, research-open] T3/D1: instantiate T2b on continuous-function sheaves + Čech first Chern class infrastructure — last session `01CffL64`
- `qou-exam` [in-progress, high, research-open] Excise the notion of absolute mass (owner ruling 2026-08-11) — last session `01V8S17M`
- `qou-lx8f` [in-progress, high, research-open] Bring lifting obstruction: coefficient group (Z vs Z/2 vs O^x) and the Bring-specific vanishing clai — last session `01CffL64`
- `qou-skn4` [in-progress, high, research-open] T3: gerbes banded by an abelian sheaf; torsor gerbe; carry T2 residuals — last session `01CffL64`
- `qou-t1dx` [in-progress, high, research-open] T3/D3: genuine stacks/gerbes, minimal faithful design + first milestone — last session `01CffL64`
- `qou-d8c7` [todo, normal, research-open] Mass endomorphism — last session `014L5sFj`
- `qou-jb7k` [todo, normal, research-open] The Wedderburn input HeckeToTemperleyLieb calls missing now EXISTS — but in a different Hecke carrie — last session `01B9DD6b`

### W2 — mass/binding compute & precision

Open PRs from older sessions:

- #8521 Switch the per-generator volumes to convention D — session `0151ZZJx`, updated 2026-11-19 (research-open)
- #8100 Label production Q_β as the retired mixed base; record the D cells — session `01Qmmkt6`, updated 2026-11-16 (mechanical)
- #8098 probe(qou-cds1): derived convention-D rungs recover ~0 % of the Q_β gap — session `01Qmmkt5`, updated 2026-11-16 (research-open)
- #7610 Q_β c_k: refuse the C/D-mixed wiring producer; general-word kernel in four D-frame probes — session `014rL2No`, updated 2026-11-14 (research-open)
- #7443 qou-oiz3 + qou-5eg1: excise the float64 q_int (both definition sites) and raise _DPS_DEFAU — session `01CwN2Uy`, updated 2026-10-13 (research-open)
- #7440 qou-oiz3 stage 1: measure the float64 q_int cone (1290 files / 917 witnesses, not 124 / 24 — session `01CwN2Uy`, updated 2026-10-13 (research-open)

Queued (`todo`) or high/critical beans (61; full list in JSON):

- `qou-10v9` [in-progress, critical, research-open] PROGRAM: L2 at 1 ppQ (mass and binding accuracy) — last session `012Z68Sq`
- `qou-8vt2` [in-progress, critical, research-open] DEFINE ϑ_K: the channel has no definition for it, only a docstring phrase — last session `01AS8WGC`
- `qou-jwl8` [todo, high, research-open] The traced_volume product ∏ᵢ∏_{j>i}(σᵢ+dᵢⱼ) is not the half-twist trace — last session `01Qmmkt5`
- `qou-mc6a` [todo, high, research-open] OWNER CALL: is L_q = sqrt(hbar_q) the right q-deformed filament length? It fixes the whole E_0 tower — last session `01JBMtTn`
- `qou-q1a4` [todo, high, research-open] Trace where u and d first become distinguished in the γγ chain (photons → condensate → nucleons) — last session `01Qmmkt5`
- `qou-3e6w` [in-progress, high, research-open] EPIC: REV_n asymptotics — the upper bound on M_n (the deuteron-wall q-Borel gate) — last session `012Z68Sq`
- `qou-3ent` [in-progress, high, research-open] CORRECTION: A_omega = 3 is the OFF-DIAGONAL Stokes constant, NOT a 3d-index coefficient — eq (21) is — last session `014L5sFj`
- `qou-47nf` [in-progress, high, research-open] TRANCHE: the non-geometric Ptolemy component at n=3 — route E''s one surviving branch — last session `01NVh8DE`
- `qou-5c64` [in-progress, high, research-open] binding-single-pipeline-comparison is 3 months stale and RED when re-run — 2 assertions flip, one co — last session `01BWn4JF`
- `qou-7ylg` [in-progress, high, mechanical] BUG: main is RED on validate — alg:delta-lambda-closure cites only a remark — last session `01FsqmWK`
- `qou-9yt9` [in-progress, high, research-open] A+C: land the ConfinementLevel refactor and the DressedParticle shadowing fix — last session `01G1N9T7`
- `qou-a3lh` [in-progress, high, research-open] OWNER CALL: is a Z-clustered SnapPy pseudo-volume the right geometric input to A(K) at all? — last session `01JBMtTn`
- `qou-ales` [in-progress, high, research-open] OWNER RULING 2026-09-08: braid-word selection via gamma-gamma production + confinement SDP at q0 — n — last session `01A1NHnU`
- `qou-avtq` [in-progress, high, research-open] MILESTONE: attack-vector queue (Q_beta / c3^odd / f-map) — last session `014L5sFj`
- `qou-brfy` [in-progress, high, research-open] Does an H_4 Farey layering exist? — the one search that decides the Bring route — last session `01LDxdXe`
- `qou-brkp` [in-progress, high, mechanical] BUG (fixed) + stale witness: a dps remediation broke 2 producers, and its own gate reported them cle — last session `01S8YDwg`
- `qou-cds1` [in-progress, high, research-open] S1 (SCIENCE): re-derive the Q_beta c_k ladder under D — not a z-swap, and that is proved — last session `01B9DD6b`
- `qou-cds2` [in-progress, high, research-open] S2 (SCIENCE): pyhecke.gram.z and the Gram singularity — the ruling answers the convention, not the s — last session `01BfuBh8`
- `qou-cds5` [in-progress, high, research-open] S5 (SCIENCE): verify the r* D-frame band BEFORE re-scoring the six Delta_lambda ansaetze — last session `01Dg4i9e`
- `qou-cdx1` [in-progress, high, mechanical] MILESTONE: excise convention C, adopt proton pin + colour weighting (owner ruling 2026-08-15) — last session `01BfuBh8`
- `qou-eptr` [in-progress, high, research-open] EP/canonical decomposition as the non-pair-local extensive carrier for b_3 — aim, and the hard block — last session `01LDxdXe`
- `qou-f64g` [in-progress, high, mechanical] INFRA (gated + measured): float64 entry points in mpmath probes — 17546 hits, 4 prior beans, no gate — last session `011aZU4m`
- `qou-fxym` [in-progress, high, research-open] A3 (headline): prove REV_n = O(sqrt n) — the beta-bound is the weak step, not the (l,W) reduction — last session `01PmZzY2`
- `qou-hok7` [in-progress, high, research-open] Deuteron-wall resummation: classical Borel on q=1 period is the WRONG transform (substrate object is — last session `012Z68Sq`
- `qou-j1e5` [in-progress, high, research-open] c1: the six values are GROUPED-word — re-derive under Borromean, or scope them (blocks the probe goi — last session `01AgoHcE`
- `qou-j540` [in-progress, high, mechanical] prop:demand-stability is marked verified against a float64 witness blind at Z=82 — and its successor — last session `01BfuBh8`
- `qou-ke35` [in-progress, high, mechanical] The mpf migration of the constant modules is HALF DONE, and a consumer that never raises mp.dps now  — last session `01BfuBh8`
- `qou-lz8f` [in-progress, high, mechanical] A producer that cannot serialize an mpf DESTROYS its witness on every run — 38 candidates, and qou-g — last session `01BfuBh8`
- `qou-mgq3` [in-progress, high, research-open] Magic-number derivation: measured attack surface, and the two walls — last session `01AA8STm`
- `qou-pgdw` [in-progress, high, mechanical] precision-gates.sh runs the raw-float64 audit twice and the advisory run overwrites the gating run's — last session `01Dg4i9e`
- `qou-q0rf` [in-progress, high, mechanical] The q0-anchor refill ratchet is RED on main (NEW 147) — and the arrival rate, not the backlog, is th — last session `01BfuBh8`
- `qou-q2oa` [in-progress, high, research-open] The ladder phase alpha has no derivation from the actual Wedderburn weights — last session `01Dg4i9e`
- `qou-qb8e` [in-progress, high, research-open] HH^1 carrier: the MAGNITUDE channel — the actual open gate for c_3 — last session `01JBMtTn`
- `qou-qint` [in-progress, high, research-open] Reconcile the 8 q-integer definitions — `qInt` names two conventions — last session `01BfuBh8`
- `qou-qqm4` [in-progress, high, research-open] DERIVE c2: the second-order hbar_q coefficient of the trace difference -- and why the pairwise chain — last session `012c3Ybh`
- `qou-qrsp` [in-progress, high, mechanical] PRODUCER FIX: 37 of 45 measured producers re-pad float64 on re-run (qou-gqt5 follow-up) — last session `01NXDwc5`
- `qou-s7ld` [in-progress, high, research-open] chi scaling wall: the Rust GP minimal-length reduction is the cost, not dim — a dim-free seminormal  — last session `01QAHenv`
- `qou-sv7h` [in-progress, high, research-open] Binding compute cannot scale: sparse path unreachable, zero Rust, float64 straddle — last session `01NVh8DE`
- `qou-sw8n` [in-progress, high, research-open] def:confinement-level is a FOURTH reading of J^bullet that no audit has, and it evades both exclusio — last session `01AgoHcE`
- `qou-vr3q` [in-progress, high, research-open] Deep-dive 1: G3 monodromy/Stokes-constant keystone — derive A_ω (odd-face Q_β/Φ_b) as GGM 3d-index i — last session `01S8YDwg`
- … 21 more in JSON

### W3 — photon/QED

Open PRs from older sessions:

- #8517 Lean: switched photon, 2×2 vertex block, trace flavour no-go in H₃(q) — session `0151ZZJz`, updated 2026-11-19 (research-open)
- #8502 Lean: the Borromean braid is a product of two commuting photons in H₃(q) — session `0151ZZJz`, updated 2026-11-19 (research-open)
- #8374 Blitvić negative result, Feynman fixes, general Pieri rule in Lean — session `0151ZZJy`, updated 2026-11-18 (research-open)
- #8367 def:photon block, photon-use audit, and rescope of the #8518 two-term QED figures — session `0151ZZJz`, updated 2026-11-19 (research-open)
- #8126 γγ electron observables: V⁰/V³/V⁶ invariants — session `01Qmmkt9`, updated 2026-11-18 (research-open)
- #8064 Collider as an explicit particle: 3V energy quanta and reachable products — session `01Qmmkt4`, updated 2026-11-15 (research-open)
- #7876 gg gluon segment: derive the nucleon gluon slot by the γγ rule (qou-99qc) — session `01A1NHnU`, updated 2026-11-15 (research-open)

Queued (`todo`) or high/critical beans (1; full list in JSON):

- `qou-aemx` [in-progress, high, mechanical] The alpha_em Lean file holds TWO rival conjectures and the block cites only one; the 470 ppb figure  — last session `01BWn4JF`

### W4 — batch Lean PR triage

Open PRs from older sessions:

- 52 batch PRs carry a non-session id (`session_01E667391F74184786BF4B9D` etc.): #8510, #8505, #8500, #8497, #8492, #8487, #8481, #8474, #8471, #8469, #8463, #8455, #8451, #8446, #8441, #8437, #8433, #8430, #8422, #8414, #8409, #8402, #8399, #8394, #8390, #8385, #8382, #8377, #8356, #8346, #8340, #8331, #8323, #8320, #8310, #8303, #8299, #8291, #8276, #8254, #8241, #8237, #8234, #8227, #8223, #8214, #8166, #8162, #8157, #8148, #8144, #8141


Queued (`todo`) or high/critical beans (57; full list in JSON):

- `qou-cite` [todo, high, mechanical] 13 citations point at bibliography entries that do not exist — the check had never run — last session `01Qmmkt8`
- `qou-hkwd` [todo, high, mechanical] RENAME TRANCHE: the atomic object is a Hecke word, not a braid word — 5 mathematically-false lines,  — last session `01LDxdXe`
- `qou-m1tr` [todo, high, mechanical] Transcription audit: verify the hand-typed GGM Stokes matrices / A-polynomial / 5_2 slopes against t — last session `01S8YDwg`
- `qou-vbjg` [todo, high, mechanical] One-voice remediation: 386 blocks fail voice-branch-jargon — last session `01FsqmWK`
- `bday` [in-progress, high, mechanical] Audit what the birthday axioms actually establish — they admit a two-valued model — last session `01K4y5xE`
- `qou-6moa` [in-progress, high, mechanical] DEFECT in AGENTS.md: markovWeights_eq_jones_of_threeRow_eq_zero is cited for its own HYPOTHESIS — last session `01B9DD6b`
- `qou-6qbv` [in-progress, high, mechanical] De-vacuify Lean :True carriers — replace with real statements — last session `01Qmmkt6`
- `qou-73kb` [in-progress, high, research-open] CHAR-ZERO: audit which Specht CharZero hypotheses are load-bearing and which are proof artifacts — last session `014boi4A`
- `qou-8lxd` [in-progress, high, research-open] EPIC: eightfold way / SM derived from QOU — last session `01Qmmkt6`
- `qou-aj49` [in-progress, high, research-open] def:frobenius-hopf-substrate axiom 2 (multiplicative counit) + Frobenius relation + counit law force — last session `01A1cKZc`
- `qou-ajfl` [in-progress, high, mechanical] Add disclosure — 3 projections that assert **Theorem/Proposition** with none — last session `01XdKe1J`
- `qou-argp` [in-progress, high, mechanical] Argument principle on an annulus — the single missing lemma for the converse theta zero locus — last session `01FsqmWK`
- `qou-c46w` [in-progress, high, mechanical] prop:brings-smoothness-resolution is a PROPOSITION whose cited Lean proof was True AND True AND True — last session `016hDVVW`
- `qou-ck0g` [in-progress, high, research-open] INFRA: q-deformed Jucys-Murphy family L_k in H_n(q) + seminormal eigenvalues — last session `014boi4A`
- `qou-ep0a` [in-progress, high, research-open] Infra: general-n Markov trace stabilization in Lean — τ-functor F3 (trace realization) — last session `01VM8zyE`
- `qou-fngs` [in-progress, high, mechanical] Vacuous: instance canonical makes GBFiltrationCollapsesAtE2 free for every R — last session `01EA1MJg`
- `qou-hxzl` [in-progress, high, mechanical] Add disclosure — 24 literature-cited projections (do NOT bulk-convert to axioms) — last session `01XdKe1J`
- `qou-j3w6` [in-progress, high, research-open] DECISION (owner): condition 5 and the eightfold fundamental — keep N=2 + second object W, weaken to  — last session `01FVaNvc`
- `qou-kebu` [in-progress, high, research-open] T2b: derive per-strand twist multisets from framed braid words — last session `01FVaNvc`
- `qou-mtc9` [in-progress, high, mechanical] GAP: confinement_categorical docstring contradicts its own code (self-assuming projection) — last session `011phRdW`
- `qou-nbz9` [in-progress, high, mechanical] Adjudicate the 38 projections de-exempted by the isDefProof narrowing — last session `01XdKe1J`
- `qou-pbjv` [in-progress, high, research-open] Infra: Hecke algebra H_n(q) as braided monoidal category in Lean (n≥3) — τ-functor F1/F2 source — last session `01VM8zyE`
- `qou-qbc7` [in-progress, high, mechanical] Lean-encode the CITED RSZ assertions so a mis-citation is a type error, not prose drift — last session `01WryfLm`
- `qou-tc8y` [in-progress, high, mechanical] BUILD: give BlochWigner_unit_circle its body (Cl_2) — the opaque seal is stale and collides with the — last session `01FVaNvc`
- `qou-uq5x` [in-progress, high, research-open] The G2 frame: S6 = G2/SU(3) isotropy is viable, and what it actually costs — last session `01FVaNvc`
- `qou-z3k1` [in-progress, high, mechanical] GAP: tactic-ladder oracle finds 3 vacuous decls the vacuity audit misses (+2 definitional restatemen — last session `016hQePZ`
- `qou-z9fx` [in-progress, high, mechanical] GAP: docstring-states-a-VALUE the body does not compute — the schurElement/hookDim class — last session `01EkdWqf`
- `qou-4b6g` [todo, normal, mechanical] Atlas provenance block cites two deprecated producers; 'no entry is maintained by hand' is unenforce — last session `019qmr2E`
- `qou-6xt9` [todo, normal, mechanical] Ingest the knot-energy literature (O'Hara, Freedman-He-Wang, survey) — last session `01LDxdXe`
- `qou-7t9z` [todo, normal, mechanical] Library doc-id mis-stamp: arxiv-2111.06645/ holds 2304.09377v2.pdf — two different works whose dirs  — last session `01LDxdXe`
- `qou-a8rj` [todo, normal, mechanical] Intake: library/arxiv-1108.5286v3/1108.5286v3.pdf (Solleveld, Hochschild homology of affine Hecke al — last session `016vK8Go`
- `qou-b6ti` [todo, normal, mechanical] Library: DeTurck-Gluck (0406276v1) sectionised to 4510 chars of 40 pages — the paper defining the EM — last session `01LDxdXe`
- `qou-b9c3` [todo, normal, mechanical] 22 PDFs sit in library/ never sectioned — a third un-ingested population, invisible to every path-5  — last session `012Z68Sq`
- `qou-bbgb` [todo, normal, mechanical] Content blocks (Milnor voice): remarks/examples/definitions covering HH, HKR, distinguished triangle — last session `016Fn6V1`
- `qou-bni2` [todo, normal, mechanical] De-intensify sweep: uniform synonym-inflation register across ns-obstruction/Kummer cluster + root-o — last session `01EkdWqf`
- `qou-denm` [todo, normal, mechanical] Ingest Kohno 1987 (Ann. Inst. Fourier 37, monodromy representations of braid groups and Yang–Baxter) — last session `01HjpvdM`
- `qou-g7z6` [todo, normal, mechanical] Drain the mass-endomorphism sidecar backlog (126/126 stale) — last session `01EkdWqf`
- `qou-ghy5` [todo, normal, mechanical] 68 dangling citation keys in .lean -- Ref: and .ts cites[] — neither path is checked — last session `01Qmmkt8`
- `qou-hs0c` [todo, normal, mechanical] A library document can be fully sectioned with no ocr/ dir and still be unsearchable: O''Hara 1991 i — last session `01TovDHV`
- `qou-i229` [todo, normal, mechanical] AUDIT: 35 published figures have no computational provenance anywhere in the repo — last session `01WUnKeZ`
- … 17 more in JSON

### W5 — legacy claude PR triage & ports

Open PRs from older sessions:

- #8519 Paper PDF: LaTeX build, publish on merge, branch diff PDFs; fix bib + READMEs [topic: —] — session `01EucfRm`, updated 2026-11-19 (mechanical)
- #8139 feat(sm): formalize 3-strand Hecke colour obstruction (qou-ni4b) & full-tower CP parity (t [topic: W1] — session `01R46Ni4`, updated 2026-11-16 (research-open)
- #8134 Braid closure: what it cannot see (commutator span), two-step split, cheat-sheet §3a [topic: —] — session `01Qmmkt8`, updated 2026-11-17 (research-open)
- #8111 Bridge B: n–p mass-scale exclusions (audit, probes, Lean no-go) [topic: W2] — session `01Qmmkt5`, updated 2026-11-16 (research-open)
- #8110 Term 4: surviving-block co-Casimir C° on the radical quotient (Lean) [topic: —] — session `01Qmmkt5`, updated 2026-11-16 (research-open)
- #8102 Lean housekeeping: fix dangling computation.script paths [topic: —] — session `01Qmmkt6`, updated 2026-11-16 (mechanical)
- #8096 Binding μ_λ: Reeb-holonomy Laplacian realises Σ[c][c+1]; μ_λ carries no ħ_q² [topic: W2] — session `01Qmmkt6`, updated 2026-11-16 (research-open)
- #8054 lean-verifier memory: toolchain without elan, KZ Mathlib gap, unfold trap [topic: —] — session `01Qmmkt6`, updated 2026-11-15 (research-open)
- #7936 C-5/JC-4: scope the R-matrix obstruction against the Kummer class [topic: —] — session `01Qmmkt7`, updated 2026-11-15 (research-open)
- #7913 Lean: volume/dilog bricks (5₂ Step A + reflection, Whitehead Lemma 4 reduction, complex Li [topic: —] — session `01Qmmkt6`, updated 2026-11-15 (research-open)
- #7909 Bring's surface: colour-ratio Möbius matrix at a branch point [topic: W1] — session `01Qmmkt7`, updated 2026-11-15 (research-open)
- #7878 library: ingest Wenzl, Turaev and Proctor 1988 from the GDZ scan of Invent. Math. 92 [topic: —] — session `01Qmmkt5`, updated 2026-11-15 (research-open)
- #7874 G3.4-DJ scoping: Dipper–James / q-Schur route to image = commutant (stream 16) [topic: W2] — session `01Qmmkt8`, updated 2026-11-15 (research-open)
- #7865 p-from-braid-mirror: scope P at the Hecke-letter level [topic: W1] — session `01Qmmkt6`, updated 2026-11-15 (research-open)
- #7845 qs4c: Option I (isospin, z_D) vs Option II (colour, level 3) — impact analysis [topic: —] — session `01Qmmkt7`, updated 2026-11-15 (research-open)
- #7834 R1: Braden–Northover real structure does not fix the polarization phase λ without a choice [topic: —] — session `01Qmmkt9`, updated 2026-11-15 (mechanical)
- #7817 Convention C→D, five weeks on: the drain is finished, the accounting drifted, and the one  [topic: —] — session `01FsqmWK`, updated 2026-11-14 (mechanical)
- #7773 Molecular word on the corpus L_b: factorisation, window depth, reading 3 (qou-a1hh) [topic: —] — session `0113CzoX`, updated 2026-10-13 (research-open)
- #7769 Molecular junction window depth (CO vs N2) on the production nucleon chain [topic: W1] — session `0113CzoX`, updated 2026-10-12 (research-open)
- #7763 corpus_search reachable from agent sessions: CLI wrapper + .mcp.json entry fix (qou-q261) [topic: —] — session `0113CzoX`, updated 2026-10-12 (mechanical)
- #7590 rem-qstar: refresh figures to the CODATA-2022 muon pin [topic: —] — session `014rL2No`, updated 2026-10-10 (mechanical)
- #7481 The TL/Hecke arc after general-n semisimplicity: count↔formula, the carrier mismatch close [topic: W1] — session `01B9DD6b`, updated 2026-11-15 (mechanical)
- #7477 precision-gate triage (1 laundered float64 fixed, 2 REDs triaged as non-defects) + two AGE [topic: W2] — session `01GqUzmZ`, updated 2026-09-27 (research-open)
- #7441 lean(qou-pdix): the modular involution fixes both loci, so it cannot bridge them at any pi [topic: —] — session `01JBMtTn`, updated 2026-11-15 (research-open)
- #7406 measure(qou-5jqv): bond-order-eq-jet-degree cites a block that names a different filtratio [topic: W2] — session `01AgoHcE`, updated 2026-10-12 (mechanical)
- #7229 qou-sv7h: the end-to-end binding timing the bean's title asks for — one real row, and one  [topic: W2] — session `01EkdWqf`, updated 2026-10-12 (research-open)
- #7225 qou-ix0x: is the Habiro cyclotomic evaluation a ring homomorphism? (the hinge under #7216  [topic: —] — session `01QAHenv`, updated 2026-10-12 (research-open)
- #7218 qou-za3q/qou-gba1: the Ω₂ pairing weight family is FORCED at z_D — derived, not chosen; an [topic: —] — session `01QBqhLy`, updated 2026-10-12 (research-open)
- #7210 beans(qou-vyvt): tranche 4 merge ledger — 3 PRs replay-verified; class D dispatched [topic: —] — session `01QAHenv`, updated 2026-09-12 (research-open)
- #7205 CAL-2 proxy (Q_β) dataset: AME-2020 → CODATA-2022 registry — staged for owner decision [topic: W2] — session `01QAHenv`, updated 2026-09-12 (research-open)
- #7136 lean(qou-kwoa): four of the five classical steps to the Geck–Pfeiffer Schur element [topic: —] — session `01AN8HT6`, updated 2026-09-07 (research-open)
- #7123 probe(qou-cds1): the TL closure rule was in this corpus all along — a path-5 failure, corr [topic: W2] — session `01Y49zma`, updated 2026-11-15 (research-open)
- #6361 qou-cds1: the negative (1³) weight is an INTERVAL fact — deflating two prior claims, one o [topic: —] — session `019YaoTi`, updated 2026-08-31 (research-open)
- #6350 L2 option 3: the "0/5 unconditional" headline rests on two claims — one stale, one conflat [topic: —] — session `018xG9Uu`, updated 2026-08-31 (mechanical)
- #6342 qou-cds1 entries 9 + 15 + 16: the |c_4| threshold, a clean pinning/non-D sweep, two gates  [topic: W2] — session `01UvJAHo`, updated 2026-09-03 (mechanical)
- #6307 perf(hecke_core_symbolic): the symbolic NF fold was exponential — LaurentQ kernel takes A= [topic: W1] — session `01LuVZMz`, updated 2026-08-30 (research-open)
- #6178 Drain the AME-literal roadmap to the values registry: 176 sites, 76 producers, REVIEW reac [topic: W2] — session `01Knbv9n`, updated 2026-09-12 (mechanical)
- #6025 Add witness truncation and provenance stamping for joint-tower-sdp [topic: W2] — session `01P7iLAF`, updated 2026-09-12 (research-open)
- #5861 docs(glossary,lean): cite barrett1993 for spherical terminology; close the Barrett–Westbur [topic: —] — session `016CbWMk`, updated 2026-08-26 (mechanical)
- #5402 bean qou-j4mn: jet dependence is forced (holds), but "min degree 7" is convention-C-frame  [topic: W2] — session `01Dg4i9e`, updated 2026-08-29 (research-open)
- #5338 qou-vy77: formalize the SIGNED Lemma 2a — and a correction to my own scoping claim [topic: —] — session `01VMr1Lr`, updated 2026-11-15 (research-open)

### W7 — NEW — platform & bean hygiene (proposed)

Queued (`todo`) or high/critical beans (82; full list in JSON):

- `qou-6bla` [todo, high, research-open] One notation per object — consolidate the ℏ_q spelling family; the q-integer split is the literature — last session `01XAFFTD`
- `qou-f3mc` [todo, high, research-open] GAP: Mathas 3.7 forward half -- the source''s selection rule for the inductive step is wrong; find a — last session `01EA1MJg`
- `qou-qspu` [todo, high, research-open] Obtain and triage Kang-Lee-Lee-Oh 2002 — the q-deformed type-A GS basis qou-auq3 needs — last session `01TovDHV`
- `qou-r13s` [todo, high, mechanical] GAP: root `lake build <targets>` EVICTS a restored olean cache — 6990 to 334 measured — last session `012c3Ybh`
- `qou-sogb` [todo, high, mechanical] r5-full-canonical-knot-solver: scriptHash MATCHES and 733 fields move deterministically — the docume — last session `01BWn4JF`
- `qou-w3yy` [todo, high, mechanical] EPIC: bean tracker hygiene — off-vocabulary statuses, broken parents, and an 83% orphan rate — last session `01FsqmWK`
- `qou-4jhp` [in-progress, high, mechanical] GAP: qa-sweep cannot load at platform pin b61e856 (sci layer imports moved cat-harness/schemas); fir — last session `01Qmmkt5`
- `qou-56qy` [in-progress, high, mechanical] lean-direct exit 0 is a claim about the olean snapshot, not about the library source (305 modules st — last session `012Z68Sq`
- `qou-6cm9` [in-progress, high, mechanical] Long computes launched with setsid/nohup DIE at session boundaries; the harness's own run_in_backgro — last session `01QBqhLy`
- `qou-99fk` [in-progress, high, mechanical] qa-sweep writes block-qa attestations into the TRACKED test/attestations store -- undeclared and uni — last session `01FVaNvc`
- `qou-aawz` [in-progress, high, research-open] GAP: is there a NON-TRIVIAL FrobeniusHopfData? the corpus only exhibits A = 1 — last session `01FVaNvc`
- `qou-bg3w` [in-progress, high, mechanical] Which element is Delta? Two nucleon-word models (1-/2-crossing vs 11-crossing) both carry the name,  — last session `01FsqmWK`
- `qou-bstl` [in-progress, high, mechanical] Open beans whose work has already landed — measured, and it cost this session three times — last session `01EkdWqf`
- `qou-cvx9` [in-progress, high, mechanical] migrate-uploads-to-library keys on filename while pdf-structure keys on the arXiv stamp — divergence — last session `012Z68Sq`
- `qou-grph` [in-progress, high, mechanical] qa-staleness never computes the `graph` hash, so all 9 graph-invalidated criteria are permanently st — last session `01EkdWqf`
- `qou-lsib` [in-progress, high, mechanical] Content-block Lean siblings: 34 unverified as of 2026-08-28, and nothing in CI builds them — last session `01EkdWqf`
- `qou-n4r9` [in-progress, high, mechanical] EPIC: migrate qou onto the cat-harness platform (folio-assistant post-split) — last session `01BfuBh8`
- `qou-pz4m` [in-progress, high, mechanical] delta2-Phi magic signal is a parity artifact, and the K=10 table has no producer — last session `01AA8STm`
- `qou-rc7b` [in-progress, high, mechanical] BUILD COVERAGE: `lake build` reaches only 853 of 1618 QOU Lean modules — 47% never compiled — last session `01FsqmWK`
- `qou-sm2c` [in-progress, high, mechanical] folio.config.json carries a live-broken feedbackDir at the pinned platform — last session `01FsqmWK`
- `qou-w3dm` [in-progress, high, mechanical] MAIN-SIDE: ~508 of 2749 witnesses carry a drifted scriptHash (18%) — last session `011aZU4m`
- `qou-yf1y` [in-progress, high, mechanical] Instance declaration + config: qou.json and qou.config.json replace three retired spellings — last session `01FsqmWK`
- `fwr6` [todo, normal, research-open] forward-ref arc: what is left, and why an agent should not decide it — last session `01CSQEiZ`
- `qou-1f1w` [todo, normal, mechanical] [LEANNODES L3] First full build and known-red baseline — last session `01NdDGeP`
- `qou-36aa` [todo, normal, mechanical] [SKILLS2 S15] Turn subagents and memory into nodes — last session `01NdDGeP`
- `qou-36r3` [todo, normal, mechanical] QA: L1 KG completeness gate on per-mimetype derived content — last session `01NVh8DE`
- `qou-4rhu` [todo, normal, mechanical] S3 Conform to the folio_init layout; QA results to the cat-harness qa-reports branch — last session `01NdDGeP`
- `qou-6ccl` [todo, normal, mechanical] [CONTENT C4] Split the 3,653 sidecars — last session `01Qmmkt8`
- `qou-6u3n` [todo, normal, mechanical] [TOOLS T13] Retire renderers and deploy into fsh-guts/ (deploy/, paper-builder-image, build-lean-mcp — last session `01MAENYV`
- `qou-72py` [todo, normal, mechanical] [SKILLS2 S10] Retire the stale forks — last session `01NdDGeP`
- `qou-7br7` [todo, normal, mechanical] RETRACTED: pdf-structure.py IS present (find does not follow the folio-assistant symlink). Kept as:  — last session `01FsqmWK`
- `qou-7ko6` [todo, normal, mechanical] f-a-sci should own the math/science schemas: cat-harness holds MATH_BLOCK_KINDS and DAK_BLOCK_KINDS  — last session `01FsqmWK`
- `qou-7vht` [todo, normal, research-open] The hook length formula at general n is what blocks finrank(H_n/rad) = catalan(n+1) — NOT the Catala — last session `01B9DD6b`
- `qou-80ul` [todo, normal, mechanical] qou-gwe9 has a COUNTEREXAMPLE: Copilot reviewed #6112 (5 comments). n=5 zero-review measurement is f — last session `01TovDHV`
- `qou-8tlx` [todo, normal, mechanical] [CONTENT C9] Bibliography and references migration (plan + stories B1-B6) — last session `01NdDGeP`
- `qou-9iks` [todo, normal, mechanical] QA: round-trip translation check for semantic drift and terminology — last session `01NVh8DE`
- `qou-9olr` [todo, normal, mechanical] The rendered GitHub Pages site is deprecated, docs-site is the only workflow that has ever succeeded — last session `01FsqmWK`
- `qou-a3l1` [todo, normal, mechanical] [TOOLS T5] Wrap the 170 content-wired producers as Tool nodes (downstream = witness) — last session `01NdDGeP`
- `qou-am5t` [todo, normal, mechanical] RE-AUDIT 2026-10-10: C->D migration state measured — 3 of 4 channels DONE, one science blocker, 57 t — last session `01Qmmkt5`
- `qou-aq9i` [todo, normal, mechanical] [TOOLS T11] Reconcile and retire 8 forked scripts, 3 forked pipeline modules and lake-cache-refresh. — last session `01NdDGeP`
- … 42 more in JSON

### W8 — NEW — open conjectures outside the mass chain (proposed)

Queued (`todo`) or high/critical beans (41; full list in JSON):

- `qou-4wl1` [todo, high, research-open] A3 (leg 2): bound remainder |R|<|g''(0)| via mixed-cumulant (Sniady genus) scaling — last session `016fs7me`
- `qou-c1ln` [todo, high, research-open] LEAN: discharge the C1 connection results that are only numerical — last session `01EkdWqf`
- `qou-qexu` [todo, high, research-open] q-RH: QExplicitFormula is uninhabitable — proved for empty spectrum, general case open — last session `01FsqmWK`
- `qou-v8t7` [todo, high, research-open] ATTACK PLAN: prove Delta_lambda covariance kernel Cov(f,Sc2)<=0 — last session `016fs7me`
- `hypr` [in-progress, high, research-open] Discharge conj:surreal-limit-transfer from Mathlib Hyperreal (ℝ* is a SurrealField) — last session `011aZU4m`
- `qou-2q85` [in-progress, high, research-open] Depth-0 to depth-2 bridge - six attack routes for the convolution/volume gap — last session `01FVaNvc`
- `qou-8mtd` [in-progress, high, research-open] Define the volume of a topological 3-manifold and connect it to the triangulation volume — last session `01UsvD2y`
- `qou-b7cy` [in-progress, high, research-open] Route 9: Bloch torsion at ℚ(ζ₇)⁺ makes the 5₂ sum rule a RATIONALITY statement — last session `011aZU4m`
- `qou-ei4q` [in-progress, high, research-open] W1: the palindromic involution z -> 1/z DOES lift to Sigma, and it is the elliptic involution — last session `016hDVVW`
- `qou-gz37` [in-progress, high, research-open] Third knot found in-corpus: GZ rank grading is NOT s(x) (guard), a source erratum adjudicated, and W — last session `01S8YDwg`
- `qou-krvm` [in-progress, high, research-open] GAP: discharge optima_coincide''s hypotheses for the actual m004/L6a4 polytopes — last session `01FsqmWK`
- `qou-m1nz` [in-progress, high, research-open] Route C M1 BLOCKER — pin the Neumann-Zagier weight / charge-basis convention so the certified 3d-ind — last session `01S8YDwg`
- `qou-m3ad` [in-progress, high, mechanical] M3: H_Ad is the dtMin projection (R1 is dtMax) -- not a re-description; but support is ONE data poin — last session `0134BL9G`
- `qou-mfdq` [in-progress, high, research-open] The pole-to-cusp bijection: the .md clause is a cardinality mismatch, and the Lean named for it prov — last session `01LDxdXe`
- `qou-odh5` [in-progress, high, research-open] C1 infinity: extract the TWO Stokes multipliers via q-Borel/theta resummation (leading blocks now kn — last session `01S8YDwg`
- `qou-offl` [in-progress, high, research-open] Route 1 (parent: qnnq): off-lattice ϑ_K = cone-manifold / generalized-Dehn-filling deformation. Non- — last session `01PxWwNZ`
- `qou-ogrk` [in-progress, high, research-open] A2 (leg 1): prove Cov_Planch(ln f, omega3) <= 0 via Ivanov-Olshanski 2nd-order covariance — last session `016fs7me`
- `qou-qspc` [in-progress, high, research-open] q-RH: the spectral coordinate map alpha_i = q^rho_i has no carrier — last session `01EkdWqf`
- `qou-r91v` [in-progress, high, research-open] Phase 4: prove β=2 maximises E_β[C₂] on [2,∞) (Jack/β-Plancherel concentration or lit match) — last session `016hQePZ`
- `qou-rstq` [in-progress, high, research-open] ROAST QUEUE: every open 5₂ claim needing adversarial review, with what specifically to attack — last session `01EkdWqf`
- `qou-rtec` [in-progress, high, research-open] Route C forward — DT count as (motivic) Euler characteristic / BPS cohomology (CoHA) of the knot cha — last session `0134BL9G`
- `qou-trns` [in-progress, high, mechanical] Route 8 transport: branch integer now PINNED by the base point; envelope theorem still open — last session `011aZU4m`
- `qou-uir6` [in-progress, high, mechanical] Omega_2 pairing vs D7: report the faithful-window scan of P(z) as the result; convention-D values ar — last session `01PmZzY2`
- `qou-wgnx` [in-progress, high, research-open] GAP: theta-normalised canonical solutions for C1 — the genuine untried route to the Stokes multiplie — last session `01S8YDwg`
- `qou-0ylf` [todo, normal, research-open] PROBE C3: Kontsevich-integral tail / Vogel Lambda exotic non-Lie weight system as the residue — last session `01EXJR2e`
- `qou-2orh` [todo, deferred, research-open] BOUNDARY: connect PNeqNPInQOU to real Mathlib complexity (TM/poly-time/Cook-Levin) — last session `01EXJR2e`
- `qou-a3n3` [todo, normal, research-open] EPIC: Gevrey persistence — does the internal q-NS dynamics keep smooth data Gevrey as q→1⁺ — last session `01LDxdXe`
- `qou-b1je` [todo, normal, research-open] EPIC: P≠NP-in-QOU — conditional reframing + chip gaps to paper standard — last session `01EXJR2e`
- `qou-f9wl` [todo, normal, research-open] P≠NP-in-QOU weaker/achievable results (restrict-model + counting LB + surreal grade + GCT) — last session `01EXJR2e`
- `qou-frzo` [todo, normal, research-open] EPIC: q-native alien calculus — the C1 successor route the RSZ closure names — last session `01S8YDwg`
- `qou-gl34` [todo, normal, research-open] G3.4: V^{⊗n} = ⊕ W_λ ⊗ S_λ and ρ(H) = End_{U_q(gl_d)}(V^{⊗n}) — the hard direction — last session `01Qmmkt4`
- `qou-gld3` [todo, normal, research-open] GAP (G3): Jimbo image = full U_q(gl_d) commutant on (K^d)^{⊗n} — not provable from the tree — last session `01Qmmkt4`
- `qou-p88a` [todo, normal, mechanical] GAP: metallic_q_symbolic_galois_proofs recommends Lean-formalising two identities its own check says — last session `01PXqRGw`
- `qou-pddf` [todo, normal, research-open] Formalize citation-justified conjecture classes to Lean (published papers ≠ infallible) — last session `01HBJzj8`
- `qou-qs0e` [todo, normal, research-open] Quark state: definition on the q-tower, factor relations, SM / eightfold-way correspondence — last session `01M5GA1L`
- `qou-t5m1` [todo, normal, research-open] Phase 3 route 2: full Śniady genus expansion on (f^λ)^3-biased measure — last session `016hQePZ`
- `qou-tbmr` [todo, normal, mechanical] Prove the two GGZ obstruction hypotheses in Lean (blocked: Mathlib unimportable) — last session `01FVaNvc`
- `qou-tdp0` [todo, normal, research-open] The WITHDRAWN resurgent/Ecalle inference is still asserted live in 1ppq-qbeta.md — last session `01JBMtTn`
- `qou-usxh` [todo, None, research-open] GAP: quark-flavour extraction from the gamma-gamma NF is unformalised; chain at phi=0 yields no quar — last session `01Qmmkt6`
- `qou-wzgm` [todo, normal, research-open] Keystone-closure multi-vector attack (conj:alg-geom-dilog-equiv + conj:binding-qbeta-complex-volume) — last session `01UboXkG`
- … 1 more in JSON

### OWNER — owner-gated statement-correctness reports (qou-q4oa)

Queued (`todo`) or high/critical beans (4; full list in JSON):

- `qou-kh7e` [in-progress, high, research-open] CIRCULAR: q*_S as a ''third determination of q0'' assumes (H1) — last session `01P7iLAF`
- `qou-pwd4` [in-progress, high, mechanical] Add the missing 'free as an R-module' hypothesis to cor:pbw and cor:ugb-pbw, and cite [bokutchen2015 — last session `01WhxgtM`
- `qou-slpd` [in-progress, high, research-open] ROAST: slope ½ is a definition, not a derivation — and the two ½s are order vs level — last session `01DsEwLa`
- `qou-1xck` [todo, normal, mechanical] author intent: noether-theorem-callout assigns p_q = w as the conserved charge of the move that chan — last session `01EA1MJg`

## Sessions

`out` = open PRs / todo beans / recent in-progress / dangling in-progress it is last to touch. Children of `01AgoHcE` marked ↳.

| session | commits | first–last | class | out | archive |
|---|---|---|---|---|---|
| ↳ `0151ZZJvu1br1cXpWVcGbwWi` | 1 | 2026-11-18…2026-11-18 | COMPLETE | 0/0/0/0 | KEEP OPEN |
| ↳ `0151ZZJxLhUX4zjeYHxiouec` | 2 | 2026-11-18…2026-11-18 | HAS-OUTSTANDING-WORK | 1/1/1/0 | KEEP OPEN |
| ↳ `0151ZZJy3kmW2rejBMCzLrGv` | 1 | 2026-11-18…2026-11-18 | COMPLETE | 0/0/0/0 | KEEP OPEN |
| ↳ `0151ZZJyJhwAuRPPD7LmvV61` | 11 | 2026-11-18…2026-11-18 | HAS-OUTSTANDING-WORK | 1/0/0/0 | KEEP OPEN |
| ↳ `0151ZZJzG6TcSr2pLRtXS3ju` | 1 | 2026-11-18…2026-11-18 | COMPLETE | 0/0/0/0 | KEEP OPEN |
| ↳ `0151ZZJzLJiS5uDekZBgTvWz` | 6 | 2026-11-18…2026-11-18 | HAS-OUTSTANDING-WORK | 2/0/0/0 | KEEP OPEN |
| `01AgoHcEEG2ugBFR9pN86i8D` | 299 | 2026-08-30…2026-11-18 | HAS-OUTSTANDING-WORK | 1/1/9/11 | KEEP OPEN |
| ↳ `01Qmmkt92A9KEZW1zMfqondF` | 2 | 2026-11-18…2026-11-18 | HAS-OUTSTANDING-WORK | 0/0/0/0 | KEEP OPEN |
| ↳ `01Qmmkt9BEcDtGHY9hqeKYab` | 78 | 2026-11-15…2026-11-18 | HAS-OUTSTANDING-WORK | 1/0/1/0 | KEEP OPEN |
| ↳ `0151ZZJybg9ypA8Knv9RbJqr` | 1 | 2026-11-17…2026-11-17 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt4mgtrS6HrKFHEdJ9x` | 8 | 2026-11-15…2026-11-17 | HAS-OUTSTANDING-WORK | 0/0/1/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt5HzHX9qSCbAvbytky` | 4 | 2026-11-16…2026-11-17 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt95KQ5zgJUr1FYS2CD` | 1 | 2026-11-17…2026-11-17 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt4jJXMawHUwcyTcatJ` | 10 | 2026-11-15…2026-11-16 | HAS-OUTSTANDING-WORK | 0/0/1/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt6VpiGy4R8nSukufJF` | 15 | 2026-11-15…2026-11-16 | HAS-OUTSTANDING-WORK | 1/0/1/0 | KEEP OPEN |
| ↳ `01Qmmkt6YoJKwVeGqwyPhKKA` | 58 | 2026-11-15…2026-11-16 | HAS-OUTSTANDING-WORK | 0/1/1/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt6dCyH72NJwcLGW2sF` | 9 | 2026-11-15…2026-11-16 | HAS-OUTSTANDING-WORK | 1/0/2/2 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt6y3aQRP3f1SXsiZqC` | 85 | 2026-11-15…2026-11-16 | HAS-OUTSTANDING-WORK | 1/0/3/1 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt7miU8cGfhf4vNBtfn` | 18 | 2026-11-15…2026-11-16 | HAS-OUTSTANDING-WORK | 1/0/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt8H63qF1haVExh24Qn` | 6 | 2026-11-16…2026-11-16 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt8JHygHWRYoCryp1Tg` | 8 | 2026-11-16…2026-11-16 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt8iEPjbhwBW1UxhRQB` | 30 | 2026-11-15…2026-11-16 | HAS-OUTSTANDING-WORK | 0/1/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt8scCz9eMduxXBz7WV` | 5 | 2026-11-16…2026-11-16 | HAS-OUTSTANDING-WORK | 0/2/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt8zbeFJu1Fp1i65ZHN` | 15 | 2026-11-16…2026-11-16 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt9LMnUwdJuinPiWd2E` | 13 | 2026-11-15…2026-11-16 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt9Mq5tR3JMcGBRb2kB` | 24 | 2026-11-15…2026-11-16 | HAS-OUTSTANDING-WORK | 0/0/1/0 | SAFE TO ARCHIVE |
| `01A1NHnUY3QMcdoxDYQmLCXB` | 35 | 2026-10-12…2026-11-15 | HAS-OUTSTANDING-WORK | 1/0/4/0 | KEEP OPEN |
| `01A1cKZcfvENVLgchFAKbxC4` | 91 | 2026-10-12…2026-11-15 | HAS-OUTSTANDING-WORK | 0/0/13/0 | SAFE TO ARCHIVE |
| `01B9DD6bvfbSrQU8f24cjTX1` | 125 | 2026-09-11…2026-11-15 | HAS-OUTSTANDING-WORK | 1/2/11/4 | SAFE TO ARCHIVE |
| `01CffL64xfSNovBSYWyxPcwk` | 65 | 2026-11-15…2026-11-15 | HAS-OUTSTANDING-WORK | 0/0/6/9 | SAFE TO ARCHIVE |
| `01M5GA1LmsEf8tSMxFjMkmnn` | 90 | 2026-10-12…2026-11-15 | HAS-OUTSTANDING-WORK | 0/3/8/3 | SAFE TO ARCHIVE |
| `01MAENYVMT61pHaMddFGHYpu` | 26 | 2026-10-10…2026-11-15 | HAS-OUTSTANDING-WORK | 0/1/0/1 | SAFE TO ARCHIVE |
| `01NVh8DEvvkdp4YpSn124wwP` | 46 | 2026-09-13…2026-11-15 | HAS-OUTSTANDING-WORK | 0/5/4/3 | SAFE TO ARCHIVE |
| `01PmZzY27QHceKGXwNivRt64` | 14 | 2026-10-12…2026-11-15 | HAS-OUTSTANDING-WORK | 0/0/2/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt4mLKLR7qtdvEgCN4e` | 14 | 2026-11-15…2026-11-15 | HAS-OUTSTANDING-WORK | 0/2/4/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt4ued4gRSfmNHgYhiv` | 26 | 2026-11-15…2026-11-15 | HAS-OUTSTANDING-WORK | 1/0/0/0 | KEEP OPEN |
| ↳ `01Qmmkt5DD4bGNiS4ukfTn8T` | 5 | 2026-11-15…2026-11-15 | HAS-OUTSTANDING-WORK | 0/0/2/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt5JDBzsGke9E5vmGGK` | 6 | 2026-11-15…2026-11-15 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt5JgiCFTZPnh2BxDUP` | 14 | 2026-11-15…2026-11-15 | HAS-OUTSTANDING-WORK | 0/2/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt5LfGhWPbQCpnb61GC` | 7 | 2026-11-15…2026-11-15 | HAS-OUTSTANDING-WORK | 0/0/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt5c8TSSh1GGk4PoPDu` | 13 | 2026-11-15…2026-11-15 | HAS-OUTSTANDING-WORK | 0/1/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt5d5FkpVYuKRRHPSEJ` | 8 | 2026-11-15…2026-11-15 | HAS-OUTSTANDING-WORK | 0/0/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt5d6k1QmiTV9qcgjGF` | 1 | 2026-11-15…2026-11-15 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt5gGUwCXJoX8Y44rre` | 50 | 2026-11-15…2026-11-15 | HAS-OUTSTANDING-WORK | 1/0/2/0 | KEEP OPEN |
| ↳ `01Qmmkt5kfQxWt3uvZsEvpv8` | 18 | 2026-11-15…2026-11-15 | HAS-OUTSTANDING-WORK | 0/1/0/1 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt61jmo75kHaCvvDt6p` | 3 | 2026-11-15…2026-11-15 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt6ADWPKeSQ5Wp4kepw` | 4 | 2026-11-15…2026-11-15 | HAS-OUTSTANDING-WORK | 0/0/1/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt6KDV9jaJ1LRwuxmDp` | 5 | 2026-11-15…2026-11-15 | HAS-OUTSTANDING-WORK | 0/0/1/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt6RTXyN5gg3AQBGRy7` | 16 | 2026-11-15…2026-11-15 | HAS-OUTSTANDING-WORK | 0/0/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt6Y5QD9BjauUKx2VzC` | 1 | 2026-11-15…2026-11-15 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt6YA78a79y4cG3D5Pk` | 9 | 2026-11-15…2026-11-15 | HAS-OUTSTANDING-WORK | 0/0/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt6YuWNGS7sPqGwpD1Q` | 9 | 2026-11-15…2026-11-15 | HAS-OUTSTANDING-WORK | 1/0/2/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt6aj8pNZYJyAew2zEa` | 8 | 2026-11-15…2026-11-15 | HAS-OUTSTANDING-WORK | 0/1/3/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt6cBhDQXZbwX9Xi5ZN` | 1 | 2026-11-15…2026-11-15 | HAS-OUTSTANDING-WORK | 0/0/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt6t98xYjpUCJgxoTnK` | 6 | 2026-11-15…2026-11-15 | HAS-OUTSTANDING-WORK | 0/0/1/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt6vSoBaqsQQ4HUpUeV` | 1 | 2026-11-15…2026-11-15 | HAS-OUTSTANDING-WORK | 0/0/1/2 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt74NYKLa7QmvMkHKSG` | 1 | 2026-11-15…2026-11-15 | HAS-OUTSTANDING-WORK | 0/0/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt78z7rogMrLFoE6cfu` | 2 | 2026-11-15…2026-11-15 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt79pDG7ns1wC1h82ov` | 4 | 2026-11-15…2026-11-15 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt7FWmM2JrbDq8tkB1G` | 1 | 2026-11-15…2026-11-15 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt7R7E8ahXCV41SwRHS` | 6 | 2026-11-15…2026-11-15 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt7S5XKHyXVLPKjAMUu` | 2 | 2026-11-15…2026-11-15 | HAS-OUTSTANDING-WORK | 0/0/1/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt7arrvA9y98dYdLsLV` | 32 | 2026-11-15…2026-11-15 | HAS-OUTSTANDING-WORK | 2/0/3/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt7cFCwnBtTgUEDPHDT` | 3 | 2026-11-15…2026-11-15 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt89hom6hDCebu79b9o` | 2 | 2026-11-15…2026-11-15 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt8Fw6HhQBAKfS6DgKM` | 8 | 2026-11-15…2026-11-15 | HAS-OUTSTANDING-WORK | 0/0/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt8NobYjwox43hUw6Za` | 1 | 2026-11-15…2026-11-15 | HAS-OUTSTANDING-WORK | 0/0/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt8Pu5VWuanTHxGFmFF` | 25 | 2026-11-15…2026-11-15 | HAS-OUTSTANDING-WORK | 0/0/2/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt8RPNkJLAu7MkUPE3f` | 4 | 2026-11-15…2026-11-15 | HAS-OUTSTANDING-WORK | 0/1/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt8pE46F2YNM5QTVpHa` | 5 | 2026-11-15…2026-11-15 | HAS-OUTSTANDING-WORK | 0/0/1/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt8q6drznUXhAMdcu4P` | 1 | 2026-11-15…2026-11-15 | HAS-OUTSTANDING-WORK | 0/0/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt9G83BWVJD2uM6cPfq` | 14 | 2026-11-15…2026-11-15 | HAS-OUTSTANDING-WORK | 0/0/3/0 | SAFE TO ARCHIVE |
| `01VkVG3s1X5wRtH5rgDEBfJJ` | 11 | 2026-09-05…2026-11-15 | HAS-OUTSTANDING-WORK | 0/0/1/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt8Vi4yNrVRrtbxkAoV` | 1 | 2026-11-11…2026-11-11 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt4orcmxL7nYBUKDidm` | 1 | 2026-11-10…2026-11-10 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt5WaLSwgbVA8urteie` | 1 | 2026-10-30…2026-10-30 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt7dhGQL6nLTZKbWCxo` | 2 | 2026-10-30…2026-10-30 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `01UboXkGB32JJhxiv7omapE4` | 100 | 2026-10-10…2026-10-17 | HAS-OUTSTANDING-WORK | 0/1/3/8 | SAFE TO ARCHIVE |
| `01QHu5UpKG62GzKEgprQkzDh` | 11 | 2026-10-14…2026-10-15 | HAS-OUTSTANDING-WORK | 0/1/0/0 | SAFE TO ARCHIVE |
| `0113CzoXn3qJ6dQPNkNBtjAp` | 26 | 2026-10-12…2026-10-13 | HAS-OUTSTANDING-WORK | 3/1/2/1 | SAFE TO ARCHIVE |
| `012Z68SqSiD978gaNt1uW6Kt` | 253 | 2026-08-22…2026-10-12 | HAS-OUTSTANDING-WORK | 0/2/12/12 | SAFE TO ARCHIVE |
| `016AEU7xkxdUcw9r7adTXgyr` | 8 | 2026-10-10…2026-10-12 | HAS-OUTSTANDING-WORK | 0/0/0/1 | SAFE TO ARCHIVE |
| `018m33mMrWQvtt4G8RBJkWrN` | 41 | 2026-10-10…2026-10-12 | HAS-OUTSTANDING-WORK | 0/0/0/2 | SAFE TO ARCHIVE |
| `01BfuBh8hUrpsUuueu7ujEZj` | 205 | 2026-09-04…2026-10-12 | HAS-OUTSTANDING-WORK | 0/2/32/29 | SAFE TO ARCHIVE |
| `01D9Ty5u4CfScGxNFgQw6Dpi` | 12 | 2026-10-12…2026-10-12 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `01FVaNvcCqkAtjmwSYoECacH` | 257 | 2026-09-03…2026-10-12 | HAS-OUTSTANDING-WORK | 0/4/14/22 | SAFE TO ARCHIVE |
| `01HuCq6VC5vQRXMmjknD2dKc` | 3 | 2026-10-12…2026-10-12 | HAS-OUTSTANDING-WORK | 0/0/0/2 | SAFE TO ARCHIVE |
| `01MocQQtMQAWE9j7HgE8rpMi` | 1 | 2026-10-12…2026-10-12 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `01NoSYCkqyqvciM1u2eLW1fX` | 34 | 2026-10-10…2026-10-12 | HAS-OUTSTANDING-WORK | 0/0/1/6 | SAFE TO ARCHIVE |
| `01QPixXypRybetWKrubj2XoV` | 13 | 2026-10-12…2026-10-12 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `01RDZSaansT3gCHtnzymkVL7` | 13 | 2026-10-10…2026-10-12 | HAS-OUTSTANDING-WORK | 0/0/0/1 | SAFE TO ARCHIVE |
| `0179bgnWwSPye6YnE82mvqnC` | 1 | 2026-10-11…2026-10-11 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `01HjpvdM6z2jkKWYbBfwkCZG` | 58 | 2026-10-11…2026-10-11 | HAS-OUTSTANDING-WORK | 0/1/1/0 | SAFE TO ARCHIVE |
| `01LDxdXe6rDoi3ghQQ5oxw3t` | 161 | 2026-09-06…2026-10-11 | HAS-OUTSTANDING-WORK | 0/5/9/13 | SAFE TO ARCHIVE |
| `01LYd3kfE8WEegUyGCByxhSi` | 11 | 2026-10-11…2026-10-11 | SUPERSEDED-BY 01M5GA1L | 0/0/0/0 | SAFE TO ARCHIVE |
| `01SVz9wTyu9X4uLbfvEKADVH` | 18 | 2026-10-10…2026-10-11 | HAS-OUTSTANDING-WORK | 0/0/1/0 | SAFE TO ARCHIVE |
| `01UXsqB2nozhZ2C9oUgW4rEw` | 5 | 2026-10-11…2026-10-11 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `01V8S17MUy2ZvixUANnhFBJt` | 18 | 2026-10-11…2026-10-11 | HAS-OUTSTANDING-WORK | 0/0/0/1 | SAFE TO ARCHIVE |
| `01XWDhcZvkP6oj4vQC3jg4bF` | 13 | 2026-10-11…2026-10-11 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `01YCgjysaFWxxx4Rz7QLdsN9` | 24 | 2026-10-10…2026-10-11 | SUPERSEDED-BY 01Qmmkt6 | 0/0/0/0 | SAFE TO ARCHIVE |
| `014L5sFjSE2QEsrDNLiajn29` | 18 | 2026-09-29…2026-10-10 | HAS-OUTSTANDING-WORK | 0/2/2/0 | SAFE TO ARCHIVE |
| `014rL2NokAyPCrgZMti6jxju` | 10 | 2026-10-10…2026-10-10 | HAS-OUTSTANDING-WORK | 2/0/0/1 | KEEP OPEN |
| `01BJNRo4kh8U15HZVFDhYNJL` | 1 | 2026-10-10…2026-10-10 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `01CwDhYCb1mq4pbYyRy5WrMs` | 5 | 2026-10-10…2026-10-10 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `01NdDGeP1SyShmoUssLuRZ91` | 96 | 2026-10-04…2026-10-06 | HAS-OUTSTANDING-WORK | 0/11/0/4 | SAFE TO ARCHIVE |
| `015Q15h1fg2Hh9MJXfAqr4h7` | 1 | 2026-10-05…2026-10-05 | SUPERSEDED-BY 01M5GA1L | 0/0/0/0 | SAFE TO ARCHIVE |
| `01FsqmWKMezLw7W86Up44M8Y` | 301 | 2026-08-15…2026-09-27 | HAS-OUTSTANDING-WORK | 1/15/10/15 | SAFE TO ARCHIVE |
| `01GqUzmZ9M7v8z1Wdw9FhzuD` | 136 | 2026-08-21…2026-09-27 | HAS-OUTSTANDING-WORK | 1/1/10/8 | SAFE TO ARCHIVE |
| `01Q9N4gFJ7BcPs4WHnKdMfbz` | 2 | 2026-09-24…2026-09-24 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `01WmQ8e6wkd4dbzbe1En9znA` | 1 | 2026-09-22…2026-09-22 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `01Y4YmG1mqk9QW4ya21mLNy8` | 4 | 2026-09-20…2026-09-20 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `01SFCwxF2nePwDpnQrX66fZE` | 2 | 2026-09-19…2026-09-19 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `016Fn6V1VgQwJLVRWd6mUfos` | 42 | 2026-09-15…2026-09-16 | HAS-OUTSTANDING-WORK | 0/2/3/8 | SAFE TO ARCHIVE |
| `012c3YbhnfniXUYGKtdf36g7` | 227 | 2026-08-29…2026-09-15 | HAS-OUTSTANDING-WORK | 0/2/13/9 | SAFE TO ARCHIVE |
| `0134BL9GG95tgycYMjLVX35V` | 137 | 2026-09-05…2026-09-15 | HAS-OUTSTANDING-WORK | 0/3/7/10 | SAFE TO ARCHIVE |
| `013tqgsyqFFexSJaR7BrTZTs` | 38 | 2026-09-14…2026-09-15 | HAS-OUTSTANDING-WORK | 0/0/3/0 | SAFE TO ARCHIVE |
| `01BWn4JF2sE4kE3E7xbpK4je` | 173 | 2026-08-30…2026-09-15 | HAS-OUTSTANDING-WORK | 0/2/8/16 | SAFE TO ARCHIVE |
| `01Cb9sX3NisBDY4WN4z5wJL4` | 204 | 2026-08-10…2026-09-15 | HAS-OUTSTANDING-WORK | 0/0/5/4 | SAFE TO ARCHIVE |
| `01EA1MJgB3Vp4vnCew6Wgraw` | 303 | 2026-08-09…2026-09-15 | HAS-OUTSTANDING-WORK | 0/4/8/8 | SAFE TO ARCHIVE |
| `01Kjv1xvKvC3gAeUzmjCCWHP` | 14 | 2026-09-13…2026-09-15 | HAS-OUTSTANDING-WORK | 0/0/0/1 | SAFE TO ARCHIVE |
| `01NXDwc5gBhuaWHw4wA1L9cr` | 75 | 2026-09-05…2026-09-15 | HAS-OUTSTANDING-WORK | 0/0/4/2 | SAFE TO ARCHIVE |
| `01TJhVcVwJAnA1bGK3Sqd47B` | 42 | 2026-09-15…2026-09-15 | HAS-OUTSTANDING-WORK | 0/0/0/6 | SAFE TO ARCHIVE |
| `01UgVYVnSQgQCxEDsDso2jHN` | 107 | 2026-08-29…2026-09-15 | HAS-OUTSTANDING-WORK | 0/0/2/2 | SAFE TO ARCHIVE |
| `01WUnKeZE2YcdjGmTEcKA2Ng` | 382 | 2026-08-15…2026-09-15 | HAS-OUTSTANDING-WORK | 0/1/21/12 | SAFE TO ARCHIVE |
| `01Y49zmah825kkwu2aB8CbAY` | 353 | 2026-08-10…2026-09-15 | HAS-OUTSTANDING-WORK | 1/0/2/8 | SAFE TO ARCHIVE |
| `01G1N9T7LpyKjmkLT8MfM1bL` | 247 | 2026-08-30…2026-09-14 | HAS-OUTSTANDING-WORK | 0/0/8/7 | SAFE TO ARCHIVE |
| `01QdzbDVufzGssqqYjkw7Ykm` | 77 | 2026-09-07…2026-09-14 | HAS-OUTSTANDING-WORK | 0/0/1/6 | SAFE TO ARCHIVE |
| `01S8YDwgt8kfaWmsefTRbY5r` | 157 | 2026-08-10…2026-09-14 | HAS-OUTSTANDING-WORK | 0/2/4/10 | SAFE TO ARCHIVE |
| `01TovDHVdRcNsTBjbUWAqjWo` | 57 | 2026-09-13…2026-09-14 | HAS-OUTSTANDING-WORK | 0/4/4/8 | SAFE TO ARCHIVE |
| `016hDVVWdFKBuCmJuRT52qmx` | 160 | 2026-08-14…2026-09-13 | HAS-OUTSTANDING-WORK | 0/1/3/11 | SAFE TO ARCHIVE |
| `01CwN2Uy1xo99iLdJgrcKYbY` | 95 | 2026-09-11…2026-09-13 | HAS-OUTSTANDING-WORK | 2/0/1/6 | KEEP OPEN |
| `01FdkmYfaSg1Kha6VGTkvmjK` | 22 | 2026-09-12…2026-09-13 | HAS-OUTSTANDING-WORK | 0/0/1/0 | SAFE TO ARCHIVE |
| `01JBMtTnocTv8Yf9dNSvqCUk` | 259 | 2026-08-01…2026-09-13 | HAS-OUTSTANDING-WORK | 1/3/7/8 | SAFE TO ARCHIVE |
| `011Xe8o5r85SzhndKso9hXVK` | 216 | 2026-08-14…2026-09-12 | HAS-OUTSTANDING-WORK | 0/2/1/7 | SAFE TO ARCHIVE |
| `016fs7mezgFXdYawFXoYW81X` | 178 | 2026-07-24…2026-09-12 | HAS-OUTSTANDING-WORK | 0/2/4/7 | SAFE TO ARCHIVE |
| `01EkdWqfz4Cq7AqNPGyLb2XD` | 367 | 2026-07-24…2026-09-12 | HAS-OUTSTANDING-WORK | 1/4/7/15 | SAFE TO ARCHIVE |
| `01Megdzd2iMcm4Cka8naZ5c4` | 99 | 2026-08-21…2026-09-12 | HAS-OUTSTANDING-WORK | 0/0/3/0 | SAFE TO ARCHIVE |
| `01QAHenv5E6ytCsVcLzfyhph` | 54 | 2026-09-08…2026-09-12 | HAS-OUTSTANDING-WORK | 3/2/2/6 | SAFE TO ARCHIVE |
| `01QBqhLy3EvXcftdH7xinWHB` | 21 | 2026-09-08…2026-09-12 | HAS-OUTSTANDING-WORK | 1/0/2/2 | SAFE TO ARCHIVE |
| `01WQGiCNFNknh5SiyM6MeTru` | 73 | 2026-08-29…2026-09-08 | HAS-OUTSTANDING-WORK | 0/0/6/3 | SAFE TO ARCHIVE |
| `016hQePZH4xA7gxL5eLTP5av` | 344 | 2026-08-09…2026-09-07 | HAS-OUTSTANDING-WORK | 0/1/9/12 | SAFE TO ARCHIVE |
| `018xG9UuU6DfXN4rghMa3Dif` | 89 | 2026-08-25…2026-09-07 | HAS-OUTSTANDING-WORK | 1/0/1/4 | SAFE TO ARCHIVE |
| `01AN8HT6uJxW3z23eficJV2H` | 117 | 2026-08-29…2026-09-07 | HAS-OUTSTANDING-WORK | 1/0/3/1 | SAFE TO ARCHIVE |
| `01AWgkrPkXGZ1Hb2UmMmFMcP` | 256 | 2026-08-15…2026-09-07 | HAS-OUTSTANDING-WORK | 0/0/7/10 | SAFE TO ARCHIVE |
| `01BWXQhUZSKVXYwDzg62sg4M` | 7 | 2026-09-04…2026-09-07 | HAS-OUTSTANDING-WORK | 0/0/0/1 | SAFE TO ARCHIVE |
| `01CSQEiZrbpPxfMZEFrzbKtD` | 217 | 2026-08-30…2026-09-07 | HAS-OUTSTANDING-WORK | 0/1/4/6 | SAFE TO ARCHIVE |
| `01Af2fr1bNUn68FmdfZju1Ak` | 203 | 2026-08-10…2026-09-06 | HAS-OUTSTANDING-WORK | 0/1/5/6 | SAFE TO ARCHIVE |
| `01XAFFTDT3yusogJUdbzQ8az` | 154 | 2026-08-25…2026-09-06 | HAS-OUTSTANDING-WORK | 0/1/2/2 | SAFE TO ARCHIVE |
| `01CdeMos5ajnyPzoGCX8vo6J` | 32 | 2026-08-30…2026-09-05 | HAS-OUTSTANDING-WORK | 0/0/2/2 | SAFE TO ARCHIVE |
| `01NcoRpQDhrfCfUvwkwmzSBo` | 115 | 2026-09-03…2026-09-05 | HAS-OUTSTANDING-WORK | 0/1/4/21 | SAFE TO ARCHIVE |
| `01Prc52Z5Sct7AdeXT2TPq6J` | 133 | 2026-07-25…2026-09-05 | HAS-OUTSTANDING-WORK | 0/0/0/6 | SAFE TO ARCHIVE |
| `01ThcvAsxXUEQjFcidz1nzni` | 286 | 2026-08-15…2026-09-05 | HAS-OUTSTANDING-WORK | 0/1/3/8 | SAFE TO ARCHIVE |
| `01WQfsrwdYTJgGnUEj7ggAA9` | 3 | 2026-08-29…2026-09-05 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `018TTjfmbDpkj854S4NciBzH` | 23 | 2026-08-29…2026-09-04 | HAS-OUTSTANDING-WORK | 0/0/1/2 | SAFE TO ARCHIVE |
| `01EDA7aDAR7xu6MvWVwg6Tip` | 113 | 2026-08-14…2026-09-04 | HAS-OUTSTANDING-WORK | 0/2/0/1 | SAFE TO ARCHIVE |
| `01K4y5xEFSrp6KwheV9kpPDG` | 123 | 2026-08-30…2026-09-04 | HAS-OUTSTANDING-WORK | 0/0/3/1 | SAFE TO ARCHIVE |
| `01FqEx3eHQwtxtfVd8mXGymj` | 82 | 2026-07-24…2026-09-03 | HAS-OUTSTANDING-WORK | 0/0/1/3 | SAFE TO ARCHIVE |
| `01KYUV5jbuc1xfk3JSfmnuHW` | 10 | 2026-08-30…2026-09-03 | HAS-OUTSTANDING-WORK | 0/0/0/0 | SAFE TO ARCHIVE |
| `01PXqRGwHzMKDYznoFquR9wZ` | 49 | 2026-08-30…2026-09-03 | HAS-OUTSTANDING-WORK | 0/1/2/3 | SAFE TO ARCHIVE |
| `01UsvD2ya9FejgEiMChv1Ere` | 77 | 2026-08-10…2026-09-03 | HAS-OUTSTANDING-WORK | 0/1/1/1 | SAFE TO ARCHIVE |
| `01XznUEC5MDdAV17Day2unrA` | 1 | 2026-09-03…2026-09-03 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `011aZU4me8e8QbZSCa7TYPiV` | 370 | 2026-08-07…2026-08-31 | HAS-OUTSTANDING-WORK | 0/0/7/5 | SAFE TO ARCHIVE |
| `0134F9sY8m1nbs5FymzdoxQT` | 160 | 2026-08-25…2026-08-31 | HAS-OUTSTANDING-WORK | 0/0/2/3 | SAFE TO ARCHIVE |
| `019YaoTiLH4WC5zydwhEiQAf` | 195 | 2026-08-26…2026-08-31 | HAS-OUTSTANDING-WORK | 1/1/3/3 | SAFE TO ARCHIVE |
| `01LuVZMzzSFCStdhQPP8nUFd` | 30 | 2026-08-30…2026-08-31 | HAS-OUTSTANDING-WORK | 1/0/1/0 | SAFE TO ARCHIVE |
| `014nZEYzt7Hd7F2ZW8hTkrhJ` | 29 | 2026-08-30…2026-08-30 | HAS-OUTSTANDING-WORK | 0/0/1/4 | SAFE TO ARCHIVE |
| `015jfbZBAdcHKHsRpeBu3LgR` | 89 | 2026-08-19…2026-08-30 | HAS-OUTSTANDING-WORK | 0/0/1/0 | SAFE TO ARCHIVE |
| `01AA8STmqmqX3z5qNYVcjitx` | 17 | 2026-08-30…2026-08-30 | HAS-OUTSTANDING-WORK | 0/0/0/3 | SAFE TO ARCHIVE |
| `01Dg8mp4qbyoc98KExM2e7HG` | 39 | 2026-08-26…2026-08-30 | HAS-OUTSTANDING-WORK | 0/0/0/1 | SAFE TO ARCHIVE |
| `01MZPYBUEXxmCs9pyyof8zjz` | 22 | 2026-08-30…2026-08-30 | HAS-OUTSTANDING-WORK | 0/1/0/0 | SAFE TO ARCHIVE |
| `01TQPEQfnjRHW41uyXCbdjXq` | 105 | 2026-08-01…2026-08-30 | HAS-OUTSTANDING-WORK | 0/0/4/7 | SAFE TO ARCHIVE |
| `01UvJAHo8dfEbj7jpZdCdt2s` | 20 | 2026-08-30…2026-08-30 | HAS-OUTSTANDING-WORK | 1/0/0/0 | SAFE TO ARCHIVE |
| `01B9XTWrESNxGvxvVcizyBwE` | 10 | 2026-08-29…2026-08-29 | SUPERSEDED-BY 01Af2fr1 | 0/0/0/0 | SAFE TO ARCHIVE |
| `01P7iLAFxWg9nVCmcXDdt5zv` | 44 | 2026-08-14…2026-08-29 | HAS-OUTSTANDING-WORK | 1/0/1/1 | SAFE TO ARCHIVE |
| `01SCx49MwsQ53BuH2DK15PpZ` | 6 | 2026-08-28…2026-08-29 | HAS-OUTSTANDING-WORK | 0/0/0/1 | SAFE TO ARCHIVE |
| `01TjQbZbFQ17VAFqZukQ4DWA` | 1 | 2026-08-29…2026-08-29 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `01Unc638om1eZmqcysnLSUro` | 142 | 2026-07-25…2026-08-29 | HAS-OUTSTANDING-WORK | 0/0/2/1 | SAFE TO ARCHIVE |
| `019qmr2EGCwvCZiTnSFkqYPG` | 101 | 2026-08-25…2026-08-27 | HAS-OUTSTANDING-WORK | 0/1/1/1 | SAFE TO ARCHIVE |
| `01J2zJVvFYkbbf9ChoDRJBgL` | 104 | 2026-08-25…2026-08-26 | HAS-OUTSTANDING-WORK | 0/0/2/4 | SAFE TO ARCHIVE |
| `01K7pzr6ahL5d8nqUZdqyea9` | 40 | 2026-08-25…2026-08-26 | HAS-OUTSTANDING-WORK | 0/0/1/0 | SAFE TO ARCHIVE |
| `01KchuNBcyCDJCqh8rV5Fo9k` | 59 | 2026-08-25…2026-08-26 | SUPERSEDED-BY 01LDxdXe | 0/0/0/0 | SAFE TO ARCHIVE |
| `01Mcfw3szchAL69ZFPBgviwH` | 65 | 2026-08-25…2026-08-26 | HAS-OUTSTANDING-WORK | 0/0/4/1 | SAFE TO ARCHIVE |
| `01VYuweVNb6dk1ix3sMZEMrc` | 15 | 2026-08-25…2026-08-26 | SUPERSEDED-BY 01LDxdXe | 0/0/0/0 | SAFE TO ARCHIVE |
| `01W7ZE7c4pxzsT6E4ixpjbFH` | 68 | 2026-08-26…2026-08-26 | SUPERSEDED-BY 01BWn4JF | 0/0/0/0 | SAFE TO ARCHIVE |
| `0116BtrkrgeQS9XQ6uPtKjVa` | 4 | 2026-08-25…2026-08-25 | SUPERSEDED-BY 01FsqmWK | 0/0/0/0 | SAFE TO ARCHIVE |
| `0117vNTD7UCCPh71KJwLXR1U` | 12 | 2026-08-25…2026-08-25 | SUPERSEDED-BY 01FsqmWK | 0/0/0/0 | SAFE TO ARCHIVE |
| `011hNSEVYuVWsSUCyg1pMNVb` | 46 | 2026-08-10…2026-08-25 | HAS-OUTSTANDING-WORK | 0/0/2/2 | SAFE TO ARCHIVE |
| `014Vdmr2kJYPRZAon2gx47KR` | 60 | 2026-07-24…2026-08-25 | HAS-OUTSTANDING-WORK | 0/0/4/1 | SAFE TO ARCHIVE |
| `019sSSDJQgKpNANGonMKQugy` | 14 | 2026-08-09…2026-08-25 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `01AazBjeFyXkvth8Gyj21Ji7` | 37 | 2026-08-24…2026-08-25 | HAS-OUTSTANDING-WORK | 0/0/1/5 | SAFE TO ARCHIVE |
| `01Dg4i9eHSEHjiNURV1WuyYG` | 173 | 2026-07-24…2026-08-25 | HAS-OUTSTANDING-WORK | 1/1/16/23 | SAFE TO ARCHIVE |
| `01GwZEbnVdUNyYH1of5orquV` | 11 | 2026-08-02…2026-08-25 | HAS-OUTSTANDING-WORK | 0/0/0/0 | SAFE TO ARCHIVE |
| `01JmyvDPtRHk7oSJ7c1AaiuQ` | 17 | 2026-08-25…2026-08-25 | SUPERSEDED-BY 01EA1MJg | 0/0/0/0 | SAFE TO ARCHIVE |
| `01LL9F9XMXAvKZzjxxhMs2bQ` | 5 | 2026-08-25…2026-08-25 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `01LpF1geqPAoT5SJJLBeaExo` | 14 | 2026-08-08…2026-08-25 | HAS-OUTSTANDING-WORK | 0/0/0/0 | SAFE TO ARCHIVE |
| `01Xj4kKZqP9FwjW1MugSLGqA` | 5 | 2026-08-25…2026-08-25 | SUPERSEDED-BY 01BfuBh8 | 0/0/0/0 | SAFE TO ARCHIVE |
| `01YVe9BeRoCsWNqMQa5sWe1r` | 8 | 2026-08-25…2026-08-25 | SUPERSEDED-BY 012Z68Sq | 0/0/0/0 | SAFE TO ARCHIVE |
| `011svAVQTeiD2ED48PQMi3w8` | 10 | 2026-08-23…2026-08-24 | SUPERSEDED-BY 01UboXkG | 0/0/0/0 | SAFE TO ARCHIVE |
| `016aqu3SabqucUSGCGH1pM8w` | 72 | 2026-08-16…2026-08-24 | SUPERSEDED-BY 01BfuBh8 | 0/0/0/0 | SAFE TO ARCHIVE |
| `019iXBNML55D5ochuegPi3hf` | 48 | 2026-08-18…2026-08-24 | HAS-OUTSTANDING-WORK | 0/0/0/1 | SAFE TO ARCHIVE |
| `01Jcdnryd2YjztmqHASd6D82` | 46 | 2026-08-23…2026-08-24 | HAS-OUTSTANDING-WORK | 0/0/0/3 | SAFE TO ARCHIVE |
| `01V7UaMoA5dvHUrvAAsNFdor` | 107 | 2026-08-15…2026-08-24 | HAS-OUTSTANDING-WORK | 0/2/1/3 | SAFE TO ARCHIVE |
| `019G4N16XnuvVLzgNGvTYGKv` | 8 | 2026-08-23…2026-08-23 | HAS-OUTSTANDING-WORK | 0/0/0/2 | SAFE TO ARCHIVE |
| `01Knbv9nrezPPcwkehQA5bBx` | 143 | 2026-08-07…2026-08-23 | HAS-OUTSTANDING-WORK | 1/1/3/6 | SAFE TO ARCHIVE |
| `01XzwAzEMY8zKaxiapETTMPM` | 133 | 2026-07-26…2026-08-23 | HAS-OUTSTANDING-WORK | 0/0/1/5 | SAFE TO ARCHIVE |
| `01NAL46KWuZp4D4MwvDGWDop` | 28 | 2026-08-14…2026-08-22 | HAS-OUTSTANDING-WORK | 0/1/0/0 | SAFE TO ARCHIVE |
| `01VM8zyExssEUAtW8bMQnegm` | 86 | 2026-07-24…2026-08-22 | HAS-OUTSTANDING-WORK | 0/0/6/4 | SAFE TO ARCHIVE |
| `01WLkDyPeWZUPbLAUhHzxgDg` | 2 | 2026-08-22…2026-08-22 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `01SKyKCtdpXbsB7EP7pcyS3S` | 60 | 2026-08-14…2026-08-21 | HAS-OUTSTANDING-WORK | 0/0/2/0 | SAFE TO ARCHIVE |
| `014boi4AkMAATWvkNf9vjVTm` | 163 | 2026-08-07…2026-08-19 | HAS-OUTSTANDING-WORK | 0/0/5/4 | SAFE TO ARCHIVE |
| `01AS8WGCDJPU2qE36oS9GxjP` | 111 | 2026-08-10…2026-08-19 | HAS-OUTSTANDING-WORK | 0/1/3/0 | SAFE TO ARCHIVE |
| `01LNLMhuidjpdKLXDRRJJKbR` | 20 | 2026-08-10…2026-08-19 | SUPERSEDED-BY 01BfuBh8 | 0/0/0/0 | SAFE TO ARCHIVE |
| `01VMr1LrQjZ7wHKwyUNF6rbe` | 46 | 2026-07-25…2026-08-19 | HAS-OUTSTANDING-WORK | 1/0/0/2 | SAFE TO ARCHIVE |
| `019c3SRCWK8h5ztqpT9iJBSs` | 20 | 2026-08-10…2026-08-18 | SUPERSEDED-BY 01WQGiCN | 0/0/0/0 | SAFE TO ARCHIVE |
| `01WhxgtMTFH5XjSJTmGzVDQM` | 86 | 2026-08-07…2026-08-16 | HAS-OUTSTANDING-WORK | 0/2/4/9 | SAFE TO ARCHIVE |
| `0176YQP7w6iqoymHivoCXdoZ` | 64 | 2026-07-27…2026-08-15 | HAS-OUTSTANDING-WORK | 0/1/2/0 | SAFE TO ARCHIVE |
| `01Km78DthtvM8vywoTX7Eeb9` | 20 | 2026-08-15…2026-08-15 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `01NCeJFFUXg6oL7JzjBZPWhe` | 48 | 2026-08-11…2026-08-15 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `01NAaxzVBKiJUZUiKUEXYYQc` | 19 | 2026-08-14…2026-08-14 | HAS-OUTSTANDING-WORK | 0/0/1/1 | SAFE TO ARCHIVE |
| `01BPLWZgZqnCJzxHTQSDcrRQ` | 3 | 2026-08-11…2026-08-11 | SUPERSEDED-BY 012Z68Sq | 0/0/0/0 | SAFE TO ARCHIVE |
| `01J1r4EKbr67Kb7oQT7x7dtM` | 40 | 2026-08-08…2026-08-11 | HAS-OUTSTANDING-WORK | 0/1/2/4 | SAFE TO ARCHIVE |
| `01YEsH7dTMB4hKkYfyrd3Bw2` | 12 | 2026-08-10…2026-08-11 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `0119z496NzPkGqaSxCSBRz3g` | 77 | 2026-07-24…2026-08-10 | HAS-OUTSTANDING-WORK | 0/0/3/2 | SAFE TO ARCHIVE |
| `014RV7VX91Ajd1yfYGqfiDds` | 4 | 2026-08-10…2026-08-10 | HAS-OUTSTANDING-WORK | 0/0/0/1 | SAFE TO ARCHIVE |
| `015vToogg4QwAcz9s5ojveVn` | 44 | 2026-08-01…2026-08-10 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `016XFNEdjsPsmKMXAZsK5NFa` | 9 | 2026-08-09…2026-08-10 | HAS-OUTSTANDING-WORK | 0/0/1/0 | SAFE TO ARCHIVE |
| `0173HPdM3qvYqGpzhjWciigD` | 24 | 2026-07-24…2026-08-10 | HAS-OUTSTANDING-WORK | 0/0/1/0 | SAFE TO ARCHIVE |
| `018SG6E3ozcmJqjimgBibSpm` | 8 | 2026-08-10…2026-08-10 | SUPERSEDED-BY 01WQGiCN | 0/0/0/0 | SAFE TO ARCHIVE |
| `01942dN8o2u6JH545RhoHvpP` | 21 | 2026-08-10…2026-08-10 | HAS-OUTSTANDING-WORK | 0/0/1/2 | SAFE TO ARCHIVE |
| `01CFXBeqf6dQVAZH3MCwfd4v` | 37 | 2026-08-02…2026-08-10 | SUPERSEDED-BY 01NoSYCk | 0/0/0/0 | SAFE TO ARCHIVE |
| `01FE6RP3b9K9zoAfYQqA8PhP` | 3 | 2026-08-10…2026-08-10 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `01G2DxVm5n6Wt6keHTs94GeV` | 5 | 2026-08-10…2026-08-10 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `01G6vd1icgcxP8Tp2iZohrS4` | 19 | 2026-08-09…2026-08-10 | SUPERSEDED-BY 01BfuBh8 | 0/0/0/0 | SAFE TO ARCHIVE |
| `01RropTKWqUE49Eta6D8NVBc` | 13 | 2026-08-10…2026-08-10 | HAS-OUTSTANDING-WORK | 0/0/0/1 | SAFE TO ARCHIVE |
| `01W84nixmCVLrkhweKZDQYQ9` | 17 | 2026-08-03…2026-08-10 | HAS-OUTSTANDING-WORK | 0/1/0/0 | SAFE TO ARCHIVE |
| `01WoGPtRh8XRdsaDtD7KrvyH` | 10 | 2026-08-09…2026-08-10 | HAS-OUTSTANDING-WORK | 0/0/3/0 | SAFE TO ARCHIVE |
| `01XdKe1JhRbcdNdJAAAtxTKY` | 17 | 2026-08-09…2026-08-10 | HAS-OUTSTANDING-WORK | 0/0/4/0 | SAFE TO ARCHIVE |
| `0112ScCcnTwf93WUT43qebqo` | 7 | 2026-08-09…2026-08-09 | SUPERSEDED-BY 01BfuBh8 | 0/0/0/0 | SAFE TO ARCHIVE |
| `0165wC8EQHWzn7JCcCQwkovL` | 5 | 2026-08-01…2026-08-09 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `016vipoA3zTxqS43yfScvZw7` | 110 | 2026-07-25…2026-08-09 | HAS-OUTSTANDING-WORK | 0/0/3/3 | SAFE TO ARCHIVE |
| `018pe73GaKJwUHjVf98sWSpB` | 64 | 2026-07-24…2026-08-09 | HAS-OUTSTANDING-WORK | 0/0/0/1 | SAFE TO ARCHIVE |
| `01BfkmC7EEWCAiyKLLmydjCd` | 2 | 2026-08-09…2026-08-09 | SUPERSEDED-BY 01FVaNvc | 0/0/0/0 | SAFE TO ARCHIVE |
| `01GA8k4RwHe4AbHwy6G1hXvp` | 5 | 2026-08-09…2026-08-09 | SUPERSEDED-BY 01FVaNvc | 0/0/0/0 | SAFE TO ARCHIVE |
| `01N6FvVzzEg34dSvWNnw8vJo` | 4 | 2026-08-09…2026-08-09 | HAS-OUTSTANDING-WORK | 0/0/0/0 | SAFE TO ARCHIVE |
| `01QU4Degn3Ez2Lz1niHDWu88` | 1 | 2026-08-09…2026-08-09 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `011phRdWLnxNtYPZEBKyhEnA` | 72 | 2026-08-08…2026-08-08 | HAS-OUTSTANDING-WORK | 0/0/0/3 | SAFE TO ARCHIVE |
| `014Cn7dpPw4Yw4AgGt8fXXm7` | 16 | 2026-08-08…2026-08-08 | SUPERSEDED-BY 01Dg4i9e | 0/0/0/0 | SAFE TO ARCHIVE |
| `014PxLTMysiw7x5hyiZzrkBn` | 12 | 2026-08-07…2026-08-08 | SUPERSEDED-BY 01S8YDwg | 0/0/0/0 | SAFE TO ARCHIVE |
| `014idHY7Hc33dfZkSsv7N1D5` | 15 | 2026-08-07…2026-08-08 | HAS-OUTSTANDING-WORK | 0/0/0/2 | SAFE TO ARCHIVE |
| `01A1Ks4RKDEc4EiCw6Rbogqv` | 6 | 2026-08-08…2026-08-08 | SUPERSEDED-BY 01FsqmWK | 0/0/0/0 | SAFE TO ARCHIVE |
| `01AzvPDCt6vfpdyAwRoPXjbm` | 7 | 2026-08-07…2026-08-08 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `01B4LJ82JJt8BTcB945TVWkH` | 90 | 2026-07-25…2026-08-08 | HAS-OUTSTANDING-WORK | 0/0/1/3 | SAFE TO ARCHIVE |
| `01DsEwLaLqBdu1cNtjCqqc94` | 55 | 2026-08-08…2026-08-08 | HAS-OUTSTANDING-WORK | 0/0/2/1 | SAFE TO ARCHIVE |
| `01E3fKq6oYNZjUD28PmxrukW` | 3 | 2026-08-08…2026-08-08 | SUPERSEDED-BY 01Dg4i9e | 0/0/0/0 | SAFE TO ARCHIVE |
| `01EXJR2edZYRwyYniCTM2nvJ` | 82 | 2026-07-31…2026-08-08 | HAS-OUTSTANDING-WORK | 0/4/5/3 | SAFE TO ARCHIVE |
| `01FuoKBqnYZCRRXbuAMSKHpn` | 41 | 2026-08-02…2026-08-08 | HAS-OUTSTANDING-WORK | 0/0/3/2 | SAFE TO ARCHIVE |
| `01FvRr7yyJGFX5FGBnVnR7Tr` | 30 | 2026-08-08…2026-08-08 | HAS-OUTSTANDING-WORK | 0/0/1/1 | SAFE TO ARCHIVE |
| `01HBJzj8QHRmLoxrG8qJWkxg` | 124 | 2026-07-25…2026-08-08 | HAS-OUTSTANDING-WORK | 0/1/5/3 | SAFE TO ARCHIVE |
| `01Jd1YQmjcqq9zhAwYPYpnjS` | 7 | 2026-08-08…2026-08-08 | HAS-OUTSTANDING-WORK | 0/1/0/1 | SAFE TO ARCHIVE |
| `01NdgQh2nTPj4gJcX7WpeKpZ` | 5 | 2026-08-08…2026-08-08 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `01PxWwNZg31HiBjUhsHieu3n` | 66 | 2026-07-31…2026-08-08 | HAS-OUTSTANDING-WORK | 0/0/0/1 | SAFE TO ARCHIVE |
| `01RPZALtTLA1VjHrX2MUfAAE` | 9 | 2026-08-08…2026-08-08 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `01RvNcZe9gyZAT9HyHkwQ8EH` | 11 | 2026-08-08…2026-08-08 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `01S5hozdqULxbNtJj9qj8UJ1` | 21 | 2026-08-07…2026-08-08 | HAS-OUTSTANDING-WORK | 0/0/0/0 | SAFE TO ARCHIVE |
| `01WryfLmGkXpZfYtxrEMkfMz` | 53 | 2026-08-08…2026-08-08 | HAS-OUTSTANDING-WORK | 0/1/2/0 | SAFE TO ARCHIVE |
| `01XGXXEsXVauhhRsgzRFGfMH` | 7 | 2026-08-08…2026-08-08 | SUPERSEDED-BY 01Megdzd | 0/0/0/0 | SAFE TO ARCHIVE |
| `01YM6zj7ueQrqmKhqccDAPwm` | 3 | 2026-08-08…2026-08-08 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `01246kF351BXJyH4CMYKFPJu` | 117 | 2026-07-24…2026-08-07 | HAS-OUTSTANDING-WORK | 0/0/1/1 | SAFE TO ARCHIVE |
| `0146JaTanpn7sLdUSn1MLqsX` | 4 | 2026-08-07…2026-08-07 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `016vK8God1JGqQJfSJxitVD8` | 55 | 2026-07-31…2026-08-07 | HAS-OUTSTANDING-WORK | 0/2/1/1 | SAFE TO ARCHIVE |
| `017VoUt4bebQbJbp3NEjKjmf` | 19 | 2026-08-07…2026-08-07 | HAS-OUTSTANDING-WORK | 0/0/1/1 | SAFE TO ARCHIVE |
| `0182g6zkbEtv64rkeafR6Mxz` | 20 | 2026-08-03…2026-08-07 | SUPERSEDED-BY 01Qmmkt6 | 0/0/0/0 | SAFE TO ARCHIVE |
| `01CY6qSmTBdxdeJtMrp3tZXg` | 69 | 2026-07-25…2026-08-07 | HAS-OUTSTANDING-WORK | 0/1/1/3 | SAFE TO ARCHIVE |
| `01F1isDDFfVh8RFpmewFrtWa` | 8 | 2026-08-07…2026-08-07 | HAS-OUTSTANDING-WORK | 0/0/1/1 | SAFE TO ARCHIVE |
| `01FwtbgsYQNxC1Km7KqfNEpD` | 15 | 2026-08-07…2026-08-07 | HAS-OUTSTANDING-WORK | 0/0/0/1 | SAFE TO ARCHIVE |
| `01GahkLckN4p6s4xVgPTdT5U` | 3 | 2026-08-07…2026-08-07 | HAS-OUTSTANDING-WORK | 0/0/0/0 | SAFE TO ARCHIVE |
| `01WyfJ8SvcyP6fTpqPoRvgyG` | 12 | 2026-08-07…2026-08-07 | HAS-OUTSTANDING-WORK | 0/1/0/0 | SAFE TO ARCHIVE |
| `014oQRaNPnFLJHbhrZsiCMWt` | 66 | 2026-07-24…2026-08-02 | HAS-OUTSTANDING-WORK | 0/0/4/3 | SAFE TO ARCHIVE |
| `01JkeGT7hsPYbbukutMTLWvv` | 116 | 2026-07-24…2026-08-02 | HAS-OUTSTANDING-WORK | 0/2/9/4 | SAFE TO ARCHIVE |
| `01TQPEQfnjRHW41uyJXCbdjXq` | 1 | 2026-08-02…2026-08-02 | COMPLETE | 0/0/0/0 | n/a |
| `01AVzo6g1XhNUYKFzhXDsK9L` | 46 | 2026-07-26…2026-07-31 | HAS-OUTSTANDING-WORK | 0/0/1/0 | SAFE TO ARCHIVE |
| `01DXHDWkLt6M1926jbeFJbDY` | 6 | 2026-07-25…2026-07-26 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `01Gw5XDgy9rQFhPq9TRwT7sP` | 10 | 2026-07-26…2026-07-26 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `01RUgMGPKVV1ok1asmxjRJDf` | 9 | 2026-07-25…2026-07-26 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `01WsFkovrPXaMVSF335weDHp` | 15 | 2026-07-25…2026-07-26 | SUPERSEDED-BY 014oQRaN | 0/0/0/0 | SAFE TO ARCHIVE |
| `01X4irvqWpLuLafyqWUuvAva` | 12 | 2026-07-25…2026-07-26 | HAS-OUTSTANDING-WORK | 0/0/1/0 | SAFE TO ARCHIVE |
| `01GpJmdGMtW87sQuh31eApAR` | 12 | 2026-07-24…2026-07-25 | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `012EE90758AE4945AC814D43` | 0 | –…– | HAS-OUTSTANDING-WORK | 1/0/0/0 | n/a |
| `013WbQekVypi9A6YQbLDXMmJ` | 0 | –…– | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `013vZiHGPug7PuHoMxRS82vw` | 0 | –…– | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| ↳ `0151ZZJw2BTJf7qsMpwF9SK4` | 0 | –…– | HAS-OUTSTANDING-WORK | 1/0/0/0 | KEEP OPEN |
| ↳ `0151ZZJwtfZ8qRs8g7aipSB4` | 0 | –…– | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| ↳ `0151ZZJzC6MYcwqpYVZci9h6` | 0 | –…– | HAS-OUTSTANDING-WORK | 2/0/0/0 | KEEP OPEN |
| ↳ `0151ZZJzbbUQeB2VYFve5Fqm` | 0 | –…– | HAS-OUTSTANDING-WORK | 1/0/0/0 | KEEP OPEN |
| `0151ZZK1KpxmSJrhMGRsPSCU` | 0 | –…– | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `016CbWMkMC5bMpHtQGtqik4B` | 0 | –…– | HAS-OUTSTANDING-WORK | 1/0/0/0 | SAFE TO ARCHIVE |
| `01E667391F74184786BF4B9D` | 0 | –…– | NOT-A-SESSION | 51/0/0/0 | n/a |
| `01EucfRmMzrEARLFNgZfhwsQ` | 0 | –…– | HAS-OUTSTANDING-WORK | 1/0/0/0 | KEEP OPEN |
| ↳ `01Qmmkt5Kws3crAQ7AxccEvR` | 0 | –…– | HAS-OUTSTANDING-WORK | 1/0/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt5LxPGasHf6kgcx3iu` | 0 | –…– | HAS-OUTSTANDING-WORK | 1/0/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt5hLUvnWio7T8h6yz9` | 0 | –…– | HAS-OUTSTANDING-WORK | 1/0/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt6a8B9fgTuZMNXTipY` | 0 | –…– | HAS-OUTSTANDING-WORK | 1/0/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt6dGgS4SoUbDgSkxg6` | 0 | –…– | HAS-OUTSTANDING-WORK | 1/0/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt857yNYNbJP3mPm9Nh` | 0 | –…– | HAS-OUTSTANDING-WORK | 1/0/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt8Mmpyd1gtuFjWCYm3` | 0 | –…– | HAS-OUTSTANDING-WORK | 1/0/0/0 | SAFE TO ARCHIVE |
| ↳ `01Qmmkt9KDZu95C6usrWrMZJ` | 0 | –…– | HAS-OUTSTANDING-WORK | 1/0/0/0 | SAFE TO ARCHIVE |
| `01R46Ni4bTqcpColourTowerCP` | 0 | –…– | HAS-OUTSTANDING-WORK | 1/0/0/0 | n/a |
| `01ST9RpvTF7JHNdUNafrjf9J` | 0 | –…– | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `01TrohkM6CvNiSBiG5czmFWJ` | 0 | –…– | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `01U3pLkmf1pvM118ZT3fbYW9` | 0 | –…– | COMPLETE | 0/0/0/0 | SAFE TO ARCHIVE |
| `01VQDpPdnjTBLBcPi6D5gj61` | 0 | –…– | HAS-OUTSTANDING-WORK | 0/0/0/0 | KEEP OPEN |

Bean created for untracked work: `qou-w6tr` (dangling-claim triage, parent `qou-c20n`). No other beans were created: every open PR found is already in the W1–W5 queues (W5 covers the 41 legacy `claude/*` PRs listed under W5 above).

## Decisions for the owner

### D1. Create workstream W7 "platform & bean hygiene", whose first job is the dangling claims?

- **What it means.** 590 beans are `in-progress` but nobody has touched them since before 2026-11-13; their sessions have ended. A W7 session would read each one and propose one of: keep (still live), back to `todo` (work not started), or completed (work merged, with the commit). It would also own the platform/tooling epics `qou-5vkl` and `qou-n4r9`.
- **What it costs.** One session; mostly reading beans and `git log`. No compute, no Lean.
- **What it risks.** Closing a bean whose subject is an open conjecture is forbidden (AGENTS.md 13a), so W7 must propose, not close; you or the coordinator approve the closures. Reversible: a bean status is one line.
- **What it commits to.** The tracker becomes readable again: right now 1,814 of 5,779 beans say `in-progress`, so "in-progress" carries no information.
- **Default if you say nothing.** Nothing changes; the claims stay as they are and this review keeps counting them as outstanding.
- **Recommendation (my judgement).** Yes, but propose-only: W7 writes a table, you approve closures in batches.

### D2. Create workstream W8 "open conjectures outside the mass chain"?

- **What it means.** 195 open beans sit under the conjecture epics (`b9cj` open conjectures, `qou-r9ih` dilog, `qou-frzo` q-native alien calculus, `qou-n4nr` volume conjecture, `qou-m6dn` Hecke/KLR/Markov/Wenzl, `qou-qs0e` quark state). None of W1–W5 owns them.
- **What it costs.** Research time; these are open mathematics, not mechanical tasks.
- **What it risks.** Competes with W1–W3 for your review attention. Nothing breaks if left alone.
- **What it commits to.** Nothing beyond a queue; parallel attacks on open problems are allowed (AGENTS.md).
- **Default if you say nothing.** They stay parked; the beans keep the state.
- **Recommendation (my judgement).** Not now. Finish the mass chain (W1/W2) first; leave these as beans.

## SAFE TO ARCHIVE

Every session below has its work either merged on main or recorded in a bean or an open PR, and the outstanding items are routed above. Archiving loses only the chat transcript.

287 sessions:

- https://claude.ai/code/session_0151ZZJybg9ypA8Knv9RbJqr — COMPLETE, last 2026-11-17
- https://claude.ai/code/session_01Qmmkt4mgtrS6HrKFHEdJ9x — HAS-OUTSTANDING-WORK, last 2026-11-17
- https://claude.ai/code/session_01Qmmkt5HzHX9qSCbAvbytky — COMPLETE, last 2026-11-17
- https://claude.ai/code/session_01Qmmkt95KQ5zgJUr1FYS2CD — COMPLETE, last 2026-11-17
- https://claude.ai/code/session_01Qmmkt4jJXMawHUwcyTcatJ — HAS-OUTSTANDING-WORK, last 2026-11-16
- https://claude.ai/code/session_01Qmmkt6YoJKwVeGqwyPhKKA — HAS-OUTSTANDING-WORK, last 2026-11-16
- https://claude.ai/code/session_01Qmmkt6dCyH72NJwcLGW2sF — HAS-OUTSTANDING-WORK, last 2026-11-16
- https://claude.ai/code/session_01Qmmkt6y3aQRP3f1SXsiZqC — HAS-OUTSTANDING-WORK, last 2026-11-16
- https://claude.ai/code/session_01Qmmkt7miU8cGfhf4vNBtfn — HAS-OUTSTANDING-WORK, last 2026-11-16
- https://claude.ai/code/session_01Qmmkt8H63qF1haVExh24Qn — COMPLETE, last 2026-11-16
- https://claude.ai/code/session_01Qmmkt8JHygHWRYoCryp1Tg — COMPLETE, last 2026-11-16
- https://claude.ai/code/session_01Qmmkt8iEPjbhwBW1UxhRQB — HAS-OUTSTANDING-WORK, last 2026-11-16
- https://claude.ai/code/session_01Qmmkt8scCz9eMduxXBz7WV — HAS-OUTSTANDING-WORK, last 2026-11-16
- https://claude.ai/code/session_01Qmmkt8zbeFJu1Fp1i65ZHN — COMPLETE, last 2026-11-16
- https://claude.ai/code/session_01Qmmkt9LMnUwdJuinPiWd2E — COMPLETE, last 2026-11-16
- https://claude.ai/code/session_01Qmmkt9Mq5tR3JMcGBRb2kB — HAS-OUTSTANDING-WORK, last 2026-11-16
- https://claude.ai/code/session_01A1cKZcfvENVLgchFAKbxC4 — HAS-OUTSTANDING-WORK, last 2026-11-15
- https://claude.ai/code/session_01B9DD6bvfbSrQU8f24cjTX1 — HAS-OUTSTANDING-WORK, last 2026-11-15
- https://claude.ai/code/session_01CffL64xfSNovBSYWyxPcwk — HAS-OUTSTANDING-WORK, last 2026-11-15
- https://claude.ai/code/session_01M5GA1LmsEf8tSMxFjMkmnn — HAS-OUTSTANDING-WORK, last 2026-11-15
- https://claude.ai/code/session_01MAENYVMT61pHaMddFGHYpu — HAS-OUTSTANDING-WORK, last 2026-11-15
- https://claude.ai/code/session_01NVh8DEvvkdp4YpSn124wwP — HAS-OUTSTANDING-WORK, last 2026-11-15
- https://claude.ai/code/session_01PmZzY27QHceKGXwNivRt64 — HAS-OUTSTANDING-WORK, last 2026-11-15
- https://claude.ai/code/session_01Qmmkt4mLKLR7qtdvEgCN4e — HAS-OUTSTANDING-WORK, last 2026-11-15
- https://claude.ai/code/session_01Qmmkt5DD4bGNiS4ukfTn8T — HAS-OUTSTANDING-WORK, last 2026-11-15
- https://claude.ai/code/session_01Qmmkt5JDBzsGke9E5vmGGK — COMPLETE, last 2026-11-15
- https://claude.ai/code/session_01Qmmkt5JgiCFTZPnh2BxDUP — HAS-OUTSTANDING-WORK, last 2026-11-15
- https://claude.ai/code/session_01Qmmkt5LfGhWPbQCpnb61GC — HAS-OUTSTANDING-WORK, last 2026-11-15
- https://claude.ai/code/session_01Qmmkt5c8TSSh1GGk4PoPDu — HAS-OUTSTANDING-WORK, last 2026-11-15
- https://claude.ai/code/session_01Qmmkt5d5FkpVYuKRRHPSEJ — HAS-OUTSTANDING-WORK, last 2026-11-15
- https://claude.ai/code/session_01Qmmkt5d6k1QmiTV9qcgjGF — COMPLETE, last 2026-11-15
- https://claude.ai/code/session_01Qmmkt5kfQxWt3uvZsEvpv8 — HAS-OUTSTANDING-WORK, last 2026-11-15
- https://claude.ai/code/session_01Qmmkt61jmo75kHaCvvDt6p — COMPLETE, last 2026-11-15
- https://claude.ai/code/session_01Qmmkt6ADWPKeSQ5Wp4kepw — HAS-OUTSTANDING-WORK, last 2026-11-15
- https://claude.ai/code/session_01Qmmkt6KDV9jaJ1LRwuxmDp — HAS-OUTSTANDING-WORK, last 2026-11-15
- https://claude.ai/code/session_01Qmmkt6RTXyN5gg3AQBGRy7 — HAS-OUTSTANDING-WORK, last 2026-11-15
- https://claude.ai/code/session_01Qmmkt6Y5QD9BjauUKx2VzC — COMPLETE, last 2026-11-15
- https://claude.ai/code/session_01Qmmkt6YA78a79y4cG3D5Pk — HAS-OUTSTANDING-WORK, last 2026-11-15
- https://claude.ai/code/session_01Qmmkt6YuWNGS7sPqGwpD1Q — HAS-OUTSTANDING-WORK, last 2026-11-15
- https://claude.ai/code/session_01Qmmkt6aj8pNZYJyAew2zEa — HAS-OUTSTANDING-WORK, last 2026-11-15
- https://claude.ai/code/session_01Qmmkt6cBhDQXZbwX9Xi5ZN — HAS-OUTSTANDING-WORK, last 2026-11-15
- https://claude.ai/code/session_01Qmmkt6t98xYjpUCJgxoTnK — HAS-OUTSTANDING-WORK, last 2026-11-15
- https://claude.ai/code/session_01Qmmkt6vSoBaqsQQ4HUpUeV — HAS-OUTSTANDING-WORK, last 2026-11-15
- https://claude.ai/code/session_01Qmmkt74NYKLa7QmvMkHKSG — HAS-OUTSTANDING-WORK, last 2026-11-15
- https://claude.ai/code/session_01Qmmkt78z7rogMrLFoE6cfu — COMPLETE, last 2026-11-15
- https://claude.ai/code/session_01Qmmkt79pDG7ns1wC1h82ov — COMPLETE, last 2026-11-15
- https://claude.ai/code/session_01Qmmkt7FWmM2JrbDq8tkB1G — COMPLETE, last 2026-11-15
- https://claude.ai/code/session_01Qmmkt7R7E8ahXCV41SwRHS — COMPLETE, last 2026-11-15
- https://claude.ai/code/session_01Qmmkt7S5XKHyXVLPKjAMUu — HAS-OUTSTANDING-WORK, last 2026-11-15
- https://claude.ai/code/session_01Qmmkt7arrvA9y98dYdLsLV — HAS-OUTSTANDING-WORK, last 2026-11-15
- https://claude.ai/code/session_01Qmmkt7cFCwnBtTgUEDPHDT — COMPLETE, last 2026-11-15
- https://claude.ai/code/session_01Qmmkt89hom6hDCebu79b9o — COMPLETE, last 2026-11-15
- https://claude.ai/code/session_01Qmmkt8Fw6HhQBAKfS6DgKM — HAS-OUTSTANDING-WORK, last 2026-11-15
- https://claude.ai/code/session_01Qmmkt8NobYjwox43hUw6Za — HAS-OUTSTANDING-WORK, last 2026-11-15
- https://claude.ai/code/session_01Qmmkt8Pu5VWuanTHxGFmFF — HAS-OUTSTANDING-WORK, last 2026-11-15
- https://claude.ai/code/session_01Qmmkt8RPNkJLAu7MkUPE3f — HAS-OUTSTANDING-WORK, last 2026-11-15
- https://claude.ai/code/session_01Qmmkt8pE46F2YNM5QTVpHa — HAS-OUTSTANDING-WORK, last 2026-11-15
- https://claude.ai/code/session_01Qmmkt8q6drznUXhAMdcu4P — HAS-OUTSTANDING-WORK, last 2026-11-15
- https://claude.ai/code/session_01Qmmkt9G83BWVJD2uM6cPfq — HAS-OUTSTANDING-WORK, last 2026-11-15
- https://claude.ai/code/session_01VkVG3s1X5wRtH5rgDEBfJJ — HAS-OUTSTANDING-WORK, last 2026-11-15
- https://claude.ai/code/session_01Qmmkt8Vi4yNrVRrtbxkAoV — COMPLETE, last 2026-11-11
- https://claude.ai/code/session_01Qmmkt4orcmxL7nYBUKDidm — COMPLETE, last 2026-11-10
- https://claude.ai/code/session_01Qmmkt5WaLSwgbVA8urteie — COMPLETE, last 2026-10-30
- https://claude.ai/code/session_01Qmmkt7dhGQL6nLTZKbWCxo — COMPLETE, last 2026-10-30
- https://claude.ai/code/session_01UboXkGB32JJhxiv7omapE4 — HAS-OUTSTANDING-WORK, last 2026-10-17
- https://claude.ai/code/session_01QHu5UpKG62GzKEgprQkzDh — HAS-OUTSTANDING-WORK, last 2026-10-15
- https://claude.ai/code/session_0113CzoXn3qJ6dQPNkNBtjAp — HAS-OUTSTANDING-WORK, last 2026-10-13
- https://claude.ai/code/session_012Z68SqSiD978gaNt1uW6Kt — HAS-OUTSTANDING-WORK, last 2026-10-12
- https://claude.ai/code/session_016AEU7xkxdUcw9r7adTXgyr — HAS-OUTSTANDING-WORK, last 2026-10-12
- https://claude.ai/code/session_018m33mMrWQvtt4G8RBJkWrN — HAS-OUTSTANDING-WORK, last 2026-10-12
- https://claude.ai/code/session_01BfuBh8hUrpsUuueu7ujEZj — HAS-OUTSTANDING-WORK, last 2026-10-12
- https://claude.ai/code/session_01D9Ty5u4CfScGxNFgQw6Dpi — COMPLETE, last 2026-10-12
- https://claude.ai/code/session_01FVaNvcCqkAtjmwSYoECacH — HAS-OUTSTANDING-WORK, last 2026-10-12
- https://claude.ai/code/session_01HuCq6VC5vQRXMmjknD2dKc — HAS-OUTSTANDING-WORK, last 2026-10-12
- https://claude.ai/code/session_01MocQQtMQAWE9j7HgE8rpMi — COMPLETE, last 2026-10-12
- https://claude.ai/code/session_01NoSYCkqyqvciM1u2eLW1fX — HAS-OUTSTANDING-WORK, last 2026-10-12
- https://claude.ai/code/session_01QPixXypRybetWKrubj2XoV — COMPLETE, last 2026-10-12
- https://claude.ai/code/session_01RDZSaansT3gCHtnzymkVL7 — HAS-OUTSTANDING-WORK, last 2026-10-12
- https://claude.ai/code/session_0179bgnWwSPye6YnE82mvqnC — COMPLETE, last 2026-10-11
- https://claude.ai/code/session_01HjpvdM6z2jkKWYbBfwkCZG — HAS-OUTSTANDING-WORK, last 2026-10-11
- https://claude.ai/code/session_01LDxdXe6rDoi3ghQQ5oxw3t — HAS-OUTSTANDING-WORK, last 2026-10-11
- https://claude.ai/code/session_01LYd3kfE8WEegUyGCByxhSi — SUPERSEDED-BY 01M5GA1LmsEf8tSMxFjMkmnn, last 2026-10-11
- https://claude.ai/code/session_01SVz9wTyu9X4uLbfvEKADVH — HAS-OUTSTANDING-WORK, last 2026-10-11
- https://claude.ai/code/session_01UXsqB2nozhZ2C9oUgW4rEw — COMPLETE, last 2026-10-11
- https://claude.ai/code/session_01V8S17MUy2ZvixUANnhFBJt — HAS-OUTSTANDING-WORK, last 2026-10-11
- https://claude.ai/code/session_01XWDhcZvkP6oj4vQC3jg4bF — COMPLETE, last 2026-10-11
- https://claude.ai/code/session_01YCgjysaFWxxx4Rz7QLdsN9 — SUPERSEDED-BY 01Qmmkt6YoJKwVeGqwyPhKKA, last 2026-10-11
- https://claude.ai/code/session_014L5sFjSE2QEsrDNLiajn29 — HAS-OUTSTANDING-WORK, last 2026-10-10
- https://claude.ai/code/session_01BJNRo4kh8U15HZVFDhYNJL — COMPLETE, last 2026-10-10
- https://claude.ai/code/session_01CwDhYCb1mq4pbYyRy5WrMs — COMPLETE, last 2026-10-10
- https://claude.ai/code/session_01NdDGeP1SyShmoUssLuRZ91 — HAS-OUTSTANDING-WORK, last 2026-10-06
- https://claude.ai/code/session_015Q15h1fg2Hh9MJXfAqr4h7 — SUPERSEDED-BY 01M5GA1LmsEf8tSMxFjMkmnn, last 2026-10-05
- https://claude.ai/code/session_01FsqmWKMezLw7W86Up44M8Y — HAS-OUTSTANDING-WORK, last 2026-09-27
- https://claude.ai/code/session_01GqUzmZ9M7v8z1Wdw9FhzuD — HAS-OUTSTANDING-WORK, last 2026-09-27
- https://claude.ai/code/session_01Q9N4gFJ7BcPs4WHnKdMfbz — COMPLETE, last 2026-09-24
- https://claude.ai/code/session_01WmQ8e6wkd4dbzbe1En9znA — COMPLETE, last 2026-09-22
- https://claude.ai/code/session_01Y4YmG1mqk9QW4ya21mLNy8 — COMPLETE, last 2026-09-20
- https://claude.ai/code/session_01SFCwxF2nePwDpnQrX66fZE — COMPLETE, last 2026-09-19
- https://claude.ai/code/session_016Fn6V1VgQwJLVRWd6mUfos — HAS-OUTSTANDING-WORK, last 2026-09-16
- https://claude.ai/code/session_012c3YbhnfniXUYGKtdf36g7 — HAS-OUTSTANDING-WORK, last 2026-09-15
- https://claude.ai/code/session_0134BL9GG95tgycYMjLVX35V — HAS-OUTSTANDING-WORK, last 2026-09-15
- https://claude.ai/code/session_013tqgsyqFFexSJaR7BrTZTs — HAS-OUTSTANDING-WORK, last 2026-09-15
- https://claude.ai/code/session_01BWn4JF2sE4kE3E7xbpK4je — HAS-OUTSTANDING-WORK, last 2026-09-15
- https://claude.ai/code/session_01Cb9sX3NisBDY4WN4z5wJL4 — HAS-OUTSTANDING-WORK, last 2026-09-15
- https://claude.ai/code/session_01EA1MJgB3Vp4vnCew6Wgraw — HAS-OUTSTANDING-WORK, last 2026-09-15
- https://claude.ai/code/session_01Kjv1xvKvC3gAeUzmjCCWHP — HAS-OUTSTANDING-WORK, last 2026-09-15
- https://claude.ai/code/session_01NXDwc5gBhuaWHw4wA1L9cr — HAS-OUTSTANDING-WORK, last 2026-09-15
- https://claude.ai/code/session_01TJhVcVwJAnA1bGK3Sqd47B — HAS-OUTSTANDING-WORK, last 2026-09-15
- https://claude.ai/code/session_01UgVYVnSQgQCxEDsDso2jHN — HAS-OUTSTANDING-WORK, last 2026-09-15
- https://claude.ai/code/session_01WUnKeZE2YcdjGmTEcKA2Ng — HAS-OUTSTANDING-WORK, last 2026-09-15
- https://claude.ai/code/session_01Y49zmah825kkwu2aB8CbAY — HAS-OUTSTANDING-WORK, last 2026-09-15
- https://claude.ai/code/session_01G1N9T7LpyKjmkLT8MfM1bL — HAS-OUTSTANDING-WORK, last 2026-09-14
- https://claude.ai/code/session_01QdzbDVufzGssqqYjkw7Ykm — HAS-OUTSTANDING-WORK, last 2026-09-14
- https://claude.ai/code/session_01S8YDwgt8kfaWmsefTRbY5r — HAS-OUTSTANDING-WORK, last 2026-09-14
- https://claude.ai/code/session_01TovDHVdRcNsTBjbUWAqjWo — HAS-OUTSTANDING-WORK, last 2026-09-14
- https://claude.ai/code/session_016hDVVWdFKBuCmJuRT52qmx — HAS-OUTSTANDING-WORK, last 2026-09-13
- https://claude.ai/code/session_01FdkmYfaSg1Kha6VGTkvmjK — HAS-OUTSTANDING-WORK, last 2026-09-13
- https://claude.ai/code/session_01JBMtTnocTv8Yf9dNSvqCUk — HAS-OUTSTANDING-WORK, last 2026-09-13
- https://claude.ai/code/session_011Xe8o5r85SzhndKso9hXVK — HAS-OUTSTANDING-WORK, last 2026-09-12
- https://claude.ai/code/session_016fs7mezgFXdYawFXoYW81X — HAS-OUTSTANDING-WORK, last 2026-09-12
- https://claude.ai/code/session_01EkdWqfz4Cq7AqNPGyLb2XD — HAS-OUTSTANDING-WORK, last 2026-09-12
- https://claude.ai/code/session_01Megdzd2iMcm4Cka8naZ5c4 — HAS-OUTSTANDING-WORK, last 2026-09-12
- https://claude.ai/code/session_01QAHenv5E6ytCsVcLzfyhph — HAS-OUTSTANDING-WORK, last 2026-09-12
- https://claude.ai/code/session_01QBqhLy3EvXcftdH7xinWHB — HAS-OUTSTANDING-WORK, last 2026-09-12
- https://claude.ai/code/session_01WQGiCNFNknh5SiyM6MeTru — HAS-OUTSTANDING-WORK, last 2026-09-08
- https://claude.ai/code/session_016hQePZH4xA7gxL5eLTP5av — HAS-OUTSTANDING-WORK, last 2026-09-07
- https://claude.ai/code/session_018xG9UuU6DfXN4rghMa3Dif — HAS-OUTSTANDING-WORK, last 2026-09-07
- https://claude.ai/code/session_01AN8HT6uJxW3z23eficJV2H — HAS-OUTSTANDING-WORK, last 2026-09-07
- https://claude.ai/code/session_01AWgkrPkXGZ1Hb2UmMmFMcP — HAS-OUTSTANDING-WORK, last 2026-09-07
- https://claude.ai/code/session_01BWXQhUZSKVXYwDzg62sg4M — HAS-OUTSTANDING-WORK, last 2026-09-07
- https://claude.ai/code/session_01CSQEiZrbpPxfMZEFrzbKtD — HAS-OUTSTANDING-WORK, last 2026-09-07
- https://claude.ai/code/session_01Af2fr1bNUn68FmdfZju1Ak — HAS-OUTSTANDING-WORK, last 2026-09-06
- https://claude.ai/code/session_01XAFFTDT3yusogJUdbzQ8az — HAS-OUTSTANDING-WORK, last 2026-09-06
- https://claude.ai/code/session_01CdeMos5ajnyPzoGCX8vo6J — HAS-OUTSTANDING-WORK, last 2026-09-05
- https://claude.ai/code/session_01NcoRpQDhrfCfUvwkwmzSBo — HAS-OUTSTANDING-WORK, last 2026-09-05
- https://claude.ai/code/session_01Prc52Z5Sct7AdeXT2TPq6J — HAS-OUTSTANDING-WORK, last 2026-09-05
- https://claude.ai/code/session_01ThcvAsxXUEQjFcidz1nzni — HAS-OUTSTANDING-WORK, last 2026-09-05
- https://claude.ai/code/session_01WQfsrwdYTJgGnUEj7ggAA9 — COMPLETE, last 2026-09-05
- https://claude.ai/code/session_018TTjfmbDpkj854S4NciBzH — HAS-OUTSTANDING-WORK, last 2026-09-04
- https://claude.ai/code/session_01EDA7aDAR7xu6MvWVwg6Tip — HAS-OUTSTANDING-WORK, last 2026-09-04
- https://claude.ai/code/session_01K4y5xEFSrp6KwheV9kpPDG — HAS-OUTSTANDING-WORK, last 2026-09-04
- https://claude.ai/code/session_01FqEx3eHQwtxtfVd8mXGymj — HAS-OUTSTANDING-WORK, last 2026-09-03
- https://claude.ai/code/session_01KYUV5jbuc1xfk3JSfmnuHW — HAS-OUTSTANDING-WORK, last 2026-09-03
- https://claude.ai/code/session_01PXqRGwHzMKDYznoFquR9wZ — HAS-OUTSTANDING-WORK, last 2026-09-03
- https://claude.ai/code/session_01UsvD2ya9FejgEiMChv1Ere — HAS-OUTSTANDING-WORK, last 2026-09-03
- https://claude.ai/code/session_01XznUEC5MDdAV17Day2unrA — COMPLETE, last 2026-09-03
- https://claude.ai/code/session_011aZU4me8e8QbZSCa7TYPiV — HAS-OUTSTANDING-WORK, last 2026-08-31
- https://claude.ai/code/session_0134F9sY8m1nbs5FymzdoxQT — HAS-OUTSTANDING-WORK, last 2026-08-31
- https://claude.ai/code/session_019YaoTiLH4WC5zydwhEiQAf — HAS-OUTSTANDING-WORK, last 2026-08-31
- https://claude.ai/code/session_01LuVZMzzSFCStdhQPP8nUFd — HAS-OUTSTANDING-WORK, last 2026-08-31
- https://claude.ai/code/session_014nZEYzt7Hd7F2ZW8hTkrhJ — HAS-OUTSTANDING-WORK, last 2026-08-30
- https://claude.ai/code/session_015jfbZBAdcHKHsRpeBu3LgR — HAS-OUTSTANDING-WORK, last 2026-08-30
- https://claude.ai/code/session_01AA8STmqmqX3z5qNYVcjitx — HAS-OUTSTANDING-WORK, last 2026-08-30
- https://claude.ai/code/session_01Dg8mp4qbyoc98KExM2e7HG — HAS-OUTSTANDING-WORK, last 2026-08-30
- https://claude.ai/code/session_01MZPYBUEXxmCs9pyyof8zjz — HAS-OUTSTANDING-WORK, last 2026-08-30
- https://claude.ai/code/session_01TQPEQfnjRHW41uyXCbdjXq — HAS-OUTSTANDING-WORK, last 2026-08-30
- https://claude.ai/code/session_01UvJAHo8dfEbj7jpZdCdt2s — HAS-OUTSTANDING-WORK, last 2026-08-30
- https://claude.ai/code/session_01B9XTWrESNxGvxvVcizyBwE — SUPERSEDED-BY 01Af2fr1bNUn68FmdfZju1Ak, last 2026-08-29
- https://claude.ai/code/session_01P7iLAFxWg9nVCmcXDdt5zv — HAS-OUTSTANDING-WORK, last 2026-08-29
- https://claude.ai/code/session_01SCx49MwsQ53BuH2DK15PpZ — HAS-OUTSTANDING-WORK, last 2026-08-29
- https://claude.ai/code/session_01TjQbZbFQ17VAFqZukQ4DWA — COMPLETE, last 2026-08-29
- https://claude.ai/code/session_01Unc638om1eZmqcysnLSUro — HAS-OUTSTANDING-WORK, last 2026-08-29
- https://claude.ai/code/session_019qmr2EGCwvCZiTnSFkqYPG — HAS-OUTSTANDING-WORK, last 2026-08-27
- https://claude.ai/code/session_01J2zJVvFYkbbf9ChoDRJBgL — HAS-OUTSTANDING-WORK, last 2026-08-26
- https://claude.ai/code/session_01K7pzr6ahL5d8nqUZdqyea9 — HAS-OUTSTANDING-WORK, last 2026-08-26
- https://claude.ai/code/session_01KchuNBcyCDJCqh8rV5Fo9k — SUPERSEDED-BY 01LDxdXe6rDoi3ghQQ5oxw3t, last 2026-08-26
- https://claude.ai/code/session_01Mcfw3szchAL69ZFPBgviwH — HAS-OUTSTANDING-WORK, last 2026-08-26
- https://claude.ai/code/session_01VYuweVNb6dk1ix3sMZEMrc — SUPERSEDED-BY 01LDxdXe6rDoi3ghQQ5oxw3t, last 2026-08-26
- https://claude.ai/code/session_01W7ZE7c4pxzsT6E4ixpjbFH — SUPERSEDED-BY 01BWn4JF2sE4kE3E7xbpK4je, last 2026-08-26
- https://claude.ai/code/session_0116BtrkrgeQS9XQ6uPtKjVa — SUPERSEDED-BY 01FsqmWKMezLw7W86Up44M8Y, last 2026-08-25
- https://claude.ai/code/session_0117vNTD7UCCPh71KJwLXR1U — SUPERSEDED-BY 01FsqmWKMezLw7W86Up44M8Y, last 2026-08-25
- https://claude.ai/code/session_011hNSEVYuVWsSUCyg1pMNVb — HAS-OUTSTANDING-WORK, last 2026-08-25
- https://claude.ai/code/session_014Vdmr2kJYPRZAon2gx47KR — HAS-OUTSTANDING-WORK, last 2026-08-25
- https://claude.ai/code/session_019sSSDJQgKpNANGonMKQugy — COMPLETE, last 2026-08-25
- https://claude.ai/code/session_01AazBjeFyXkvth8Gyj21Ji7 — HAS-OUTSTANDING-WORK, last 2026-08-25
- https://claude.ai/code/session_01Dg4i9eHSEHjiNURV1WuyYG — HAS-OUTSTANDING-WORK, last 2026-08-25
- https://claude.ai/code/session_01GwZEbnVdUNyYH1of5orquV — HAS-OUTSTANDING-WORK, last 2026-08-25
- https://claude.ai/code/session_01JmyvDPtRHk7oSJ7c1AaiuQ — SUPERSEDED-BY 01EA1MJgB3Vp4vnCew6Wgraw, last 2026-08-25
- https://claude.ai/code/session_01LL9F9XMXAvKZzjxxhMs2bQ — COMPLETE, last 2026-08-25
- https://claude.ai/code/session_01LpF1geqPAoT5SJJLBeaExo — HAS-OUTSTANDING-WORK, last 2026-08-25
- https://claude.ai/code/session_01Xj4kKZqP9FwjW1MugSLGqA — SUPERSEDED-BY 01BfuBh8hUrpsUuueu7ujEZj, last 2026-08-25
- https://claude.ai/code/session_01YVe9BeRoCsWNqMQa5sWe1r — SUPERSEDED-BY 012Z68SqSiD978gaNt1uW6Kt, last 2026-08-25
- https://claude.ai/code/session_011svAVQTeiD2ED48PQMi3w8 — SUPERSEDED-BY 01UboXkGB32JJhxiv7omapE4, last 2026-08-24
- https://claude.ai/code/session_016aqu3SabqucUSGCGH1pM8w — SUPERSEDED-BY 01BfuBh8hUrpsUuueu7ujEZj, last 2026-08-24
- https://claude.ai/code/session_019iXBNML55D5ochuegPi3hf — HAS-OUTSTANDING-WORK, last 2026-08-24
- https://claude.ai/code/session_01Jcdnryd2YjztmqHASd6D82 — HAS-OUTSTANDING-WORK, last 2026-08-24
- https://claude.ai/code/session_01V7UaMoA5dvHUrvAAsNFdor — HAS-OUTSTANDING-WORK, last 2026-08-24
- https://claude.ai/code/session_019G4N16XnuvVLzgNGvTYGKv — HAS-OUTSTANDING-WORK, last 2026-08-23
- https://claude.ai/code/session_01Knbv9nrezPPcwkehQA5bBx — HAS-OUTSTANDING-WORK, last 2026-08-23
- https://claude.ai/code/session_01XzwAzEMY8zKaxiapETTMPM — HAS-OUTSTANDING-WORK, last 2026-08-23
- https://claude.ai/code/session_01NAL46KWuZp4D4MwvDGWDop — HAS-OUTSTANDING-WORK, last 2026-08-22
- https://claude.ai/code/session_01VM8zyExssEUAtW8bMQnegm — HAS-OUTSTANDING-WORK, last 2026-08-22
- https://claude.ai/code/session_01WLkDyPeWZUPbLAUhHzxgDg — COMPLETE, last 2026-08-22
- https://claude.ai/code/session_01SKyKCtdpXbsB7EP7pcyS3S — HAS-OUTSTANDING-WORK, last 2026-08-21
- https://claude.ai/code/session_014boi4AkMAATWvkNf9vjVTm — HAS-OUTSTANDING-WORK, last 2026-08-19
- https://claude.ai/code/session_01AS8WGCDJPU2qE36oS9GxjP — HAS-OUTSTANDING-WORK, last 2026-08-19
- https://claude.ai/code/session_01LNLMhuidjpdKLXDRRJJKbR — SUPERSEDED-BY 01BfuBh8hUrpsUuueu7ujEZj, last 2026-08-19
- https://claude.ai/code/session_01VMr1LrQjZ7wHKwyUNF6rbe — HAS-OUTSTANDING-WORK, last 2026-08-19
- https://claude.ai/code/session_019c3SRCWK8h5ztqpT9iJBSs — SUPERSEDED-BY 01WQGiCNFNknh5SiyM6MeTru, last 2026-08-18
- https://claude.ai/code/session_01WhxgtMTFH5XjSJTmGzVDQM — HAS-OUTSTANDING-WORK, last 2026-08-16
- https://claude.ai/code/session_0176YQP7w6iqoymHivoCXdoZ — HAS-OUTSTANDING-WORK, last 2026-08-15
- https://claude.ai/code/session_01Km78DthtvM8vywoTX7Eeb9 — COMPLETE, last 2026-08-15
- https://claude.ai/code/session_01NCeJFFUXg6oL7JzjBZPWhe — COMPLETE, last 2026-08-15
- https://claude.ai/code/session_01NAaxzVBKiJUZUiKUEXYYQc — HAS-OUTSTANDING-WORK, last 2026-08-14
- https://claude.ai/code/session_01BPLWZgZqnCJzxHTQSDcrRQ — SUPERSEDED-BY 012Z68SqSiD978gaNt1uW6Kt, last 2026-08-11
- https://claude.ai/code/session_01J1r4EKbr67Kb7oQT7x7dtM — HAS-OUTSTANDING-WORK, last 2026-08-11
- https://claude.ai/code/session_01YEsH7dTMB4hKkYfyrd3Bw2 — COMPLETE, last 2026-08-11
- https://claude.ai/code/session_0119z496NzPkGqaSxCSBRz3g — HAS-OUTSTANDING-WORK, last 2026-08-10
- https://claude.ai/code/session_014RV7VX91Ajd1yfYGqfiDds — HAS-OUTSTANDING-WORK, last 2026-08-10
- https://claude.ai/code/session_015vToogg4QwAcz9s5ojveVn — COMPLETE, last 2026-08-10
- https://claude.ai/code/session_016XFNEdjsPsmKMXAZsK5NFa — HAS-OUTSTANDING-WORK, last 2026-08-10
- https://claude.ai/code/session_0173HPdM3qvYqGpzhjWciigD — HAS-OUTSTANDING-WORK, last 2026-08-10
- https://claude.ai/code/session_018SG6E3ozcmJqjimgBibSpm — SUPERSEDED-BY 01WQGiCNFNknh5SiyM6MeTru, last 2026-08-10
- https://claude.ai/code/session_01942dN8o2u6JH545RhoHvpP — HAS-OUTSTANDING-WORK, last 2026-08-10
- https://claude.ai/code/session_01CFXBeqf6dQVAZH3MCwfd4v — SUPERSEDED-BY 01NoSYCkqyqvciM1u2eLW1fX, last 2026-08-10
- https://claude.ai/code/session_01FE6RP3b9K9zoAfYQqA8PhP — COMPLETE, last 2026-08-10
- https://claude.ai/code/session_01G2DxVm5n6Wt6keHTs94GeV — COMPLETE, last 2026-08-10
- https://claude.ai/code/session_01G6vd1icgcxP8Tp2iZohrS4 — SUPERSEDED-BY 01BfuBh8hUrpsUuueu7ujEZj, last 2026-08-10
- https://claude.ai/code/session_01RropTKWqUE49Eta6D8NVBc — HAS-OUTSTANDING-WORK, last 2026-08-10
- https://claude.ai/code/session_01W84nixmCVLrkhweKZDQYQ9 — HAS-OUTSTANDING-WORK, last 2026-08-10
- https://claude.ai/code/session_01WoGPtRh8XRdsaDtD7KrvyH — HAS-OUTSTANDING-WORK, last 2026-08-10
- https://claude.ai/code/session_01XdKe1JhRbcdNdJAAAtxTKY — HAS-OUTSTANDING-WORK, last 2026-08-10
- https://claude.ai/code/session_0112ScCcnTwf93WUT43qebqo — SUPERSEDED-BY 01BfuBh8hUrpsUuueu7ujEZj, last 2026-08-09
- https://claude.ai/code/session_0165wC8EQHWzn7JCcCQwkovL — COMPLETE, last 2026-08-09
- https://claude.ai/code/session_016vipoA3zTxqS43yfScvZw7 — HAS-OUTSTANDING-WORK, last 2026-08-09
- https://claude.ai/code/session_018pe73GaKJwUHjVf98sWSpB — HAS-OUTSTANDING-WORK, last 2026-08-09
- https://claude.ai/code/session_01BfkmC7EEWCAiyKLLmydjCd — SUPERSEDED-BY 01FVaNvcCqkAtjmwSYoECacH, last 2026-08-09
- https://claude.ai/code/session_01GA8k4RwHe4AbHwy6G1hXvp — SUPERSEDED-BY 01FVaNvcCqkAtjmwSYoECacH, last 2026-08-09
- https://claude.ai/code/session_01N6FvVzzEg34dSvWNnw8vJo — HAS-OUTSTANDING-WORK, last 2026-08-09
- https://claude.ai/code/session_01QU4Degn3Ez2Lz1niHDWu88 — COMPLETE, last 2026-08-09
- https://claude.ai/code/session_011phRdWLnxNtYPZEBKyhEnA — HAS-OUTSTANDING-WORK, last 2026-08-08
- https://claude.ai/code/session_014Cn7dpPw4Yw4AgGt8fXXm7 — SUPERSEDED-BY 01Dg4i9eHSEHjiNURV1WuyYG, last 2026-08-08
- https://claude.ai/code/session_014PxLTMysiw7x5hyiZzrkBn — SUPERSEDED-BY 01S8YDwgt8kfaWmsefTRbY5r, last 2026-08-08
- https://claude.ai/code/session_014idHY7Hc33dfZkSsv7N1D5 — HAS-OUTSTANDING-WORK, last 2026-08-08
- https://claude.ai/code/session_01A1Ks4RKDEc4EiCw6Rbogqv — SUPERSEDED-BY 01FsqmWKMezLw7W86Up44M8Y, last 2026-08-08
- https://claude.ai/code/session_01AzvPDCt6vfpdyAwRoPXjbm — COMPLETE, last 2026-08-08
- https://claude.ai/code/session_01B4LJ82JJt8BTcB945TVWkH — HAS-OUTSTANDING-WORK, last 2026-08-08
- https://claude.ai/code/session_01DsEwLaLqBdu1cNtjCqqc94 — HAS-OUTSTANDING-WORK, last 2026-08-08
- https://claude.ai/code/session_01E3fKq6oYNZjUD28PmxrukW — SUPERSEDED-BY 01Dg4i9eHSEHjiNURV1WuyYG, last 2026-08-08
- https://claude.ai/code/session_01EXJR2edZYRwyYniCTM2nvJ — HAS-OUTSTANDING-WORK, last 2026-08-08
- https://claude.ai/code/session_01FuoKBqnYZCRRXbuAMSKHpn — HAS-OUTSTANDING-WORK, last 2026-08-08
- https://claude.ai/code/session_01FvRr7yyJGFX5FGBnVnR7Tr — HAS-OUTSTANDING-WORK, last 2026-08-08
- https://claude.ai/code/session_01HBJzj8QHRmLoxrG8qJWkxg — HAS-OUTSTANDING-WORK, last 2026-08-08
- https://claude.ai/code/session_01Jd1YQmjcqq9zhAwYPYpnjS — HAS-OUTSTANDING-WORK, last 2026-08-08
- https://claude.ai/code/session_01NdgQh2nTPj4gJcX7WpeKpZ — COMPLETE, last 2026-08-08
- https://claude.ai/code/session_01PxWwNZg31HiBjUhsHieu3n — HAS-OUTSTANDING-WORK, last 2026-08-08
- https://claude.ai/code/session_01RPZALtTLA1VjHrX2MUfAAE — COMPLETE, last 2026-08-08
- https://claude.ai/code/session_01RvNcZe9gyZAT9HyHkwQ8EH — COMPLETE, last 2026-08-08
- https://claude.ai/code/session_01S5hozdqULxbNtJj9qj8UJ1 — HAS-OUTSTANDING-WORK, last 2026-08-08
- https://claude.ai/code/session_01WryfLmGkXpZfYtxrEMkfMz — HAS-OUTSTANDING-WORK, last 2026-08-08
- https://claude.ai/code/session_01XGXXEsXVauhhRsgzRFGfMH — SUPERSEDED-BY 01Megdzd2iMcm4Cka8naZ5c4, last 2026-08-08
- https://claude.ai/code/session_01YM6zj7ueQrqmKhqccDAPwm — COMPLETE, last 2026-08-08
- https://claude.ai/code/session_01246kF351BXJyH4CMYKFPJu — HAS-OUTSTANDING-WORK, last 2026-08-07
- https://claude.ai/code/session_0146JaTanpn7sLdUSn1MLqsX — COMPLETE, last 2026-08-07
- https://claude.ai/code/session_016vK8God1JGqQJfSJxitVD8 — HAS-OUTSTANDING-WORK, last 2026-08-07
- https://claude.ai/code/session_017VoUt4bebQbJbp3NEjKjmf — HAS-OUTSTANDING-WORK, last 2026-08-07
- https://claude.ai/code/session_0182g6zkbEtv64rkeafR6Mxz — SUPERSEDED-BY 01Qmmkt6KDV9jaJ1LRwuxmDp, last 2026-08-07
- https://claude.ai/code/session_01CY6qSmTBdxdeJtMrp3tZXg — HAS-OUTSTANDING-WORK, last 2026-08-07
- https://claude.ai/code/session_01F1isDDFfVh8RFpmewFrtWa — HAS-OUTSTANDING-WORK, last 2026-08-07
- https://claude.ai/code/session_01FwtbgsYQNxC1Km7KqfNEpD — HAS-OUTSTANDING-WORK, last 2026-08-07
- https://claude.ai/code/session_01GahkLckN4p6s4xVgPTdT5U — HAS-OUTSTANDING-WORK, last 2026-08-07
- https://claude.ai/code/session_01WyfJ8SvcyP6fTpqPoRvgyG — HAS-OUTSTANDING-WORK, last 2026-08-07
- https://claude.ai/code/session_014oQRaNPnFLJHbhrZsiCMWt — HAS-OUTSTANDING-WORK, last 2026-08-02
- https://claude.ai/code/session_01JkeGT7hsPYbbukutMTLWvv — HAS-OUTSTANDING-WORK, last 2026-08-02
- https://claude.ai/code/session_01AVzo6g1XhNUYKFzhXDsK9L — HAS-OUTSTANDING-WORK, last 2026-07-31
- https://claude.ai/code/session_01DXHDWkLt6M1926jbeFJbDY — COMPLETE, last 2026-07-26
- https://claude.ai/code/session_01Gw5XDgy9rQFhPq9TRwT7sP — COMPLETE, last 2026-07-26
- https://claude.ai/code/session_01RUgMGPKVV1ok1asmxjRJDf — COMPLETE, last 2026-07-26
- https://claude.ai/code/session_01WsFkovrPXaMVSF335weDHp — SUPERSEDED-BY 014oQRaNPnFLJHbhrZsiCMWt, last 2026-07-26
- https://claude.ai/code/session_01X4irvqWpLuLafyqWUuvAva — HAS-OUTSTANDING-WORK, last 2026-07-26
- https://claude.ai/code/session_01GpJmdGMtW87sQuh31eApAR — COMPLETE, last 2026-07-25
- https://claude.ai/code/session_013WbQekVypi9A6YQbLDXMmJ — COMPLETE, last PR-only
- https://claude.ai/code/session_013vZiHGPug7PuHoMxRS82vw — COMPLETE, last PR-only
- https://claude.ai/code/session_0151ZZJwtfZ8qRs8g7aipSB4 — COMPLETE, last PR-only
- https://claude.ai/code/session_0151ZZK1KpxmSJrhMGRsPSCU — COMPLETE, last PR-only
- https://claude.ai/code/session_016CbWMkMC5bMpHtQGtqik4B — HAS-OUTSTANDING-WORK, last PR-only
- https://claude.ai/code/session_01Qmmkt5Kws3crAQ7AxccEvR — HAS-OUTSTANDING-WORK, last PR-only
- https://claude.ai/code/session_01Qmmkt5LxPGasHf6kgcx3iu — HAS-OUTSTANDING-WORK, last PR-only
- https://claude.ai/code/session_01Qmmkt5hLUvnWio7T8h6yz9 — HAS-OUTSTANDING-WORK, last PR-only
- https://claude.ai/code/session_01Qmmkt6a8B9fgTuZMNXTipY — HAS-OUTSTANDING-WORK, last PR-only
- https://claude.ai/code/session_01Qmmkt6dGgS4SoUbDgSkxg6 — HAS-OUTSTANDING-WORK, last PR-only
- https://claude.ai/code/session_01Qmmkt857yNYNbJP3mPm9Nh — HAS-OUTSTANDING-WORK, last PR-only
- https://claude.ai/code/session_01Qmmkt8Mmpyd1gtuFjWCYm3 — HAS-OUTSTANDING-WORK, last PR-only
- https://claude.ai/code/session_01Qmmkt9KDZu95C6usrWrMZJ — HAS-OUTSTANDING-WORK, last PR-only
- https://claude.ai/code/session_01ST9RpvTF7JHNdUNafrjf9J — COMPLETE, last PR-only
- https://claude.ai/code/session_01TrohkM6CvNiSBiG5czmFWJ — COMPLETE, last PR-only
- https://claude.ai/code/session_01U3pLkmf1pvM118ZT3fbYW9 — COMPLETE, last PR-only

## KEEP OPEN

- https://claude.ai/code/session_014rL2NokAyPCrgZMti6jxju — authored open PR(s) in the coordinator merge queue: #7610 — keep until merged or closed
- https://claude.ai/code/session_0151ZZJvu1br1cXpWVcGbwWi — last commit on main 2026-11-18 — may still be running
- https://claude.ai/code/session_0151ZZJw2BTJf7qsMpwF9SK4 — authored open PR(s) in the coordinator merge queue: #8365 — keep until merged or closed
- https://claude.ai/code/session_0151ZZJxLhUX4zjeYHxiouec — authored open PR(s) in the coordinator merge queue: #8521 — keep until merged or closed
- https://claude.ai/code/session_0151ZZJy3kmW2rejBMCzLrGv — last commit on main 2026-11-18 — may still be running
- https://claude.ai/code/session_0151ZZJyJhwAuRPPD7LmvV61 — authored open PR(s) in the coordinator merge queue: #8374 — keep until merged or closed
- https://claude.ai/code/session_0151ZZJzC6MYcwqpYVZci9h6 — authored open PR(s) in the coordinator merge queue: #8522, #8523 — keep until merged or closed
- https://claude.ai/code/session_0151ZZJzG6TcSr2pLRtXS3ju — last commit on main 2026-11-18 — may still be running
- https://claude.ai/code/session_0151ZZJzLJiS5uDekZBgTvWz — authored open PR(s) in the coordinator merge queue: #8502, #8517 — keep until merged or closed
- https://claude.ai/code/session_0151ZZJzbbUQeB2VYFve5Fqm — authored open PR(s) in the coordinator merge queue: #8367 — keep until merged or closed
- https://claude.ai/code/session_01A1NHnUY3QMcdoxDYQmLCXB — authored open PR(s) in the coordinator merge queue: #7876 — keep until merged or closed
- https://claude.ai/code/session_01AgoHcEEG2ugBFR9pN86i8D — previous coordinator (299 commits, last 2026-11-18); archive once the 2026-11-20 coordinator confirms it holds its queue
- https://claude.ai/code/session_01CwN2Uy1xo99iLdJgrcKYbY — authored open PR(s) in the coordinator merge queue: #7440, #7443 — keep until merged or closed
- https://claude.ai/code/session_01EucfRmMzrEARLFNgZfhwsQ — #8519 (paper PDF build) is the one live legacy merge candidate (W5)
- https://claude.ai/code/session_01Qmmkt4ued4gRSfmNHgYhiv — authored open PR(s) in the coordinator merge queue: #8064 — keep until merged or closed
- https://claude.ai/code/session_01Qmmkt5gGUwCXJoX8Y44rre — authored open PR(s) in the coordinator merge queue: #8098 — keep until merged or closed
- https://claude.ai/code/session_01Qmmkt6VpiGy4R8nSukufJF — authored open PR(s) in the coordinator merge queue: #8100 — keep until merged or closed
- https://claude.ai/code/session_01Qmmkt92A9KEZW1zMfqondF — last commit on main 2026-11-18 — may still be running
- https://claude.ai/code/session_01Qmmkt9BEcDtGHY9hqeKYab — authored open PR(s) in the coordinator merge queue: #8126 — keep until merged or closed
- https://claude.ai/code/session_01VQDpPdnjTBLBcPi6D5gj61 — current coordinator / merge manager (2026-11-20)

Also keep the six 2026-11-20 workstream sessions (W1–W6) and this one until the coordinator closes the plan.

Not session ids (do not try to open): `session_012EE90758AE4945AC814D43`, `session_01E667391F74184786BF4B9D`, `session_01R46Ni4bTqcpColourTowerCP`, `session_01TQPEQfnjRHW41uyJXCbdjXq`. The first one is on 51 batch PRs (W4).
