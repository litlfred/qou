# LEAN slice — P3 "Lean / Mathlib foundations" (read-only analysis, 2026-10-04)

Scope: 493 open LEAN-slice beans [M]. All of them are in `LEAN_mapping.tsv`, plus 13 closed or other-slice beans that matter for the structure. Lean evidence comes from a scan of all 3,992 `.lean` files on `main` @ `348e299cc` (2026-10-03). The scan strips comments and strings, then checks decl lookup and class-binder/instance status [M]. Per the owner's hard rule, every action here concerns beans only. Nothing below proposes editing or deleting a Lean declaration, statement or proof.

## Headline findings

1. **The bean store is far behind the Lean tree.** Main has **15 real `sorry` terms in 6 files** [M]: 3 in `observations/higgs-t28.lean`, 4 in `nuclear-interactions/periodic-table-demand-conjecture.lean`, 1 in a content sibling, 1 in `Fred2005/FormalGroups.lean`, and 6 in scratch or computations files. The cited-sorry catalog `qou-k1mq` still says 80 sorries in 69 files. **91 open beans are `close-evidence`** [M], mostly "Prove X" / "Sorry: X" / "PROVE(lean)" beans whose target is now sorry-free.
2. **The Hecke / Schur–Weyl programme is essentially done on the `QOU.SchurWeyl.Hecke` carrier.** Its beans still describe it as open. All of the following hold for **every n** and are sorry-free [M]:
   - `heckeWedderburn`: H_{n+1}(q) ≃ ∏_λ M_{d_λ}, in `HeckeWedderburnGeneral`.
   - `finrank_hecke_eq_factorial`.
   - `isSemisimpleRing_hecke_generic` (`HeckeSemisimpleGeneral`).
   - `wenzlCriterion_of_one_lt` and `semisimple_of_one_lt_unconditional`, which give the cited `WenzlCriterion` its first model.
   - Ocneanu/Wenzl Markov trace instances (`MarkovTraceInstance`, `WenzlMarkovTraceInstance`).
   - Uniqueness (`markovTrace_unique`), and a colimit `MarkovTrace` instance (`HeckeColimitMarkovTrace`).
   - Tower strictness (`HeckeTowerStrict`) and faithfulness (`HeckeProductInjective`).

   The S_n side was already closed: sp00 is complete, and `rskBurnsideHolds` holds for all n.
3. **The remaining P3 work on the L2 critical path is wiring, not mathematics.**
   - `class WedderburnDecomp` (`Hecke/Wedderburn.lean:115`, on the `QOU.Hecke.IwahoriHecke` carrier) still has **no instance** [M; its consumer `QBeta/WedderburnTraceDecomposition.lean:56` says so].
   - `axiom markov_trace_unique_axiom` is still at `Hecke/MarkovTrace.lean:177` [M].
   - Both are L2 mass-chain steps 3 and 5 [D, L2 audit §2 table]. Both have proved counterparts on the SchurWeyl carrier, and `SchurWeyl/HeckeCarrierEquiv.lean` already bridges the two carriers.
   - So **step 5 is unblocked by transport**. The one owner decision in the way is `qou-ar7f` (retire vs re-point the `Mathlib/HeckeAlgebra` shadows).

## Proposed epic / story tree

**P3 Lean / Mathlib foundations**: a NEW umbrella. Sub-epics, with the bean chosen to be each epic:

| key | epic bean | scope / status |
|---|---|---|
| P3.SN | `sp00` (completed; keep as parent-of-record) | Specht, SYT, hook-length, RSK, burnside. **DONE.** 50+ stragglers are close-evidence. |
| P3.HECKE | `qou-k4oq` → promote | Carriers: presentations, T_w basis, Matsumoto (06h7 completed), carrier unification `qou-img9`, `csgy`, `oyty`, `phir`. |
| P3.SW | `qou-59vq` → promote; rewrite body | Semisimplicity, Wedderburn, Markov, Schur–Weyl. Open stories: **SW-WIRE** (`hah4`, `luq7`, `h56b`, `ar7f`, `0fmb`, `ss88`, `qua1`, `yos9`), SW-5 general irreducibility (`jfr8`), SW-9 double centralizer (`us0a`), R2 (`mpq5`), Schur elements (`68e1`, `zwzd`, PR #7136). |
| P3.TL | `qou-0cyu` → promote | Temperley–Lieb, Jones, HOMFLY: `jb7k` (TL ideal = trace radical), `e6db`, `mp3m`, `7gei`, `7crn`, `f1qs`. |
| P3.CAT | NEW | Braided, ribbon and pivotal categories, RT functor: `rtrb`, `bwrt`, `rtqd`, `ga7i` (i7rq is the completed parent-of-record), `pbjv`, `bt3u`, `l25z`, `lyq2`. |
| P3.AN | `qou-c8p8` → promote | Analytic and convex Mathlib gaps. Sub-epic `qou-5gai` (hyperbolic volume) with `mlgp` + `idvt` + `7y3g` + `322e` + `m8xt` + `mame`. Stories: Hadamard (`n4pv`), argument principle (`z4jb`), conic duality (`yc05`), differential forms/Stokes (`ghc6`, `jvua`), moment problem. |
| P3.GS | `qou-1o8n` → promote | Gröbner–Shirshov for the **UGB / Fred2005 papers**; `auq3` completed. Only real Lean `sorry` here: `Fred2005/FormalGroups.lean` (`znz5`). `qSerre_is_gs_basis` is an `axiom` (`lncp`). |
| P3.HON | `qou-6qbv` → promote | Lean honesty: de-vacuify, self-assuming classes, sorry/axiom ledgers, §3b disclosure. `6awe` and the `5p7n` children become stories; `vqep` is the closed precedent; `k1mq` closes, with PR #7180 (187 conjecture classes without an instance) as its successor ledger. |
| P3.GEN | story under P3 | Generic-R §7c: `w4la`, `qreal`, `9e7p`, `tp56`. |
| P3.GAP | `08a2` keep | Research-grade tiers: geometric Langlands, motivic Galois. Tier-1/2 closed (`c8_superexp` unconditional). |

**Reclassified out of P3** (they carry a LEAN tag but are not foundations work):
- P6 (76): cache, olean and build tooling; detectors; sidecars.
- P2 (61): §3b conjecture classes such as `q_gl_*`, surreal-appendix classes, `q_ns_wellposedness`, P≠NP, volume transcendence, `bws0`/`rtep`.
- P1 (46): ParticleInteractions, confinement, nucleon and deuteron carriers.
- P5 (35): Cite / Remark / library intake.
- P4 (12): SM.

## Dependency DAG (what unblocks what)

```
P3.SN (done) ──► SW-3 Σd_λ²=n! (done) ──► P3.SW SW-6/7/8 general n (done, SchurWeyl carrier)
P3.HECKE carrier unification (img9; HeckeCarrierEquiv exists) ──┐
                                                                 ▼
                       SW-WIRE: WedderburnDecomp instance + replace markov_trace_unique_axiom use
                                 │                 └──► L2 step 3 (Markov) & step 5 (y_λ, trace decomposition)
                                 │                        └──► P1 Q_β functional under convention D (z_D weights)
                                 ▼
P3.TL TL ideal = trace radical (jb7k / PR #7481) ──► Jones/HOMFLY in Lean (e6db) ──► P2 P≠NP-in-QOU Jones leg, AJ
P3.CAT ribbon/pivotal (rtrb, ga7i, rtqd) ──► RT functor ──► bws0.bwsc ──► loc_matches (m_p·m_μ keystone)
                                                         (bwse = physics input: NEVER a Lean derivation)
P3.AN 5gai hyperbolic volume H1–H5 ──► volume-conjecture family, qou-krvm, 7y3g
P3.AN Hadamard / argument principle / elliptic ──► q-RH & elliptic-divisor carriers (P2)
P3.AN conic duality (yc05) ──► confinement SDP, operator-selection LP (P1; LP is degenerate [D])
SW-9 double centralizer (us0a) — on NO critical path [B 59vq]
```

**Critical path:**
- **For L2:** SW-WIRE is the only P3 item. P3.CAT is needed only if `loc_matches` is to be formal.
- **For the conjectures:** 5gai (volume conjecture), P3.TL Jones (P≠NP, AJ), and the Hadamard / argument-principle tier (q-RH). The last two are genuine upstream Mathlib builds [B c8p8].

## Duplicate clusters (bodies read)

| cluster | verdict |
|---|---|
| `qou-vkmt` / `qou-c8p8` | Not byte-identical. vkmt says it is the duplicate itself [B]. **Survivor c8p8.** vkmt's children are twins of c8p8's: `h8rx`→`7crn`, `nntw`→`f6bb` (both closable: Cauchy for parallelograms proved in #6491 [B]), `qk5b`→`z4jb`, `5rr4`→`yc05`. |
| `qou-lwjc` / `qou-r0jg` | Same statement, both bodies empty. **Both close-evidence**: `BurnsideDischarge.burnside_proved` + `instBurnsideContext` [M]. |
| `qou-hnhg` / `qou-otbb` / `qou-utb3` | otbb and utb3 have empty bodies. **Survivor 59vq. All three are close-evidence**: Wenzl is discharged and general-n Markov is proved [M]. |
| `qou-59vq` / `qou-k4oq` | **Not duplicates.** k4oq is carriers/foundations; 59vq is representation theory. Keep both: P3.HECKE and P3.SW. |
| `qou-0ap1` / `sp00` | 0ap1's body is empty. **dup-of sp00.** |
| `vqep` / `qou-6qbv` / `6awe` | Distinct scopes: 95 vacuity defects (done), `:True` carriers, axiomatised class fields. One epic, P3.HON = 6qbv; 6awe becomes a story. |
| `qou-k1mq` / `08a2` | Not duplicates. k1mq is a stale catalogue → close-evidence. 08a2 is tiered gap infra → keep. |

Further duplicates found: 20 more pairs, mostly the same Lean declaration filed twice, listed as `dup-of` rows in the TSV (e.g. `7t08`/`bktp` → `kyik`, `bawa`/`yabz` → `jgp2`, `idvt` → `5gai`, `ml0e` → `k4oq`).

**A caveat on "sorry-free".** Many cited sorries became §3b classes with **no instance**. Those beans are `reparent`, not `close-evidence`, because the gap moved from the term to the signature [B 08a2]. Examples: `volume_perturbation`, `shell_filling_rule`, `q_ns_wellposedness`, `confinement_*`, `q_gl_*`, `HasArgumentPrinciple`, `WedderburnDecomp`.

## Work landed, bean still open (highest-value closes)

- **Wenzl and Hecke semisimplicity:** `hnhg`, `otbb`, `8irr`, `q5bp`, `bnhe`, `101j`, `f0p8`, `kwoa`, `v32l`.
- **Markov trace and Hecke structure:** `utb3`, `o2dk`, `p8yg`, `5mrn`, `y90y`, `pk7l`.
- **S_n, Specht and RSK:** `nrex` (RSK epic; "Arc verified on main 2026-08-29"), `lwjc`, `r0jg`, `wtny` (SW-3), `b9sp`.
- **Specht stragglers:** about 35 more, all in the TSV.
- **Analytic and sorry-ledger closes:** `uyqw` (QOU/Mathlib has 0 sorry), `cxgx`, `f6bb`, `l2xx`, `v4if`, the UGB PROVE(lean) beans, and `9h6x`.
- **Scrap:** `7xay` and `tdxo` (concrete-n Wenzl ascent, superseded; PR #7481 says `WenzlTowerStep` has zero consumers).

## Stalled claims

**97 of 99 in-progress LEAN beans were last updated before 2026-09-20** [M]; each is marked `STALLED` in the TSV. Most of them are among the close-evidence set above, so they are stale rather than abandoned. Examples: `59vq` (08-19), `hnhg` (07-24), `8irr` (07-25), `lwjc` (08-01), `nrex` (08-29), `bws0`, and `c8p8`/`vkmt` (09-08).

## Open PRs that belong here

| PR | state | home |
|---|---|---|
| #7481 | dirty | TL/Hecke arc after general-n semisimplicity. P3.TL + SW-WIRE; closes `jb7k` once merged. |
| #7136 | dirty | Geck–Pfeiffer Schur elements (4 of 5 steps). P3.SW optional story, since semisimplicity already landed by the dimension squeeze. |
| #5352 | — | TL-arc proved/assumed ledger. A **do-not-merge** survey, and it holds the only copy of a sibling's commit `431def4877` [B PR body]. Owner must decide where that commit goes before anyone closes the PR. |
| #7180 | clean | 187 conjecture classes with no instance. P3.HON; successor ledger to `k1mq`. |
| #7441 | dirty | Modular involution, sorry-free (`qou-pdix`). P2 with Lean content. |
| #5338 | draft | Signed Lemma 2a (`qou-vy77`). P2. Records that a published lemma is wrong as stated. |
| #7218 | — | Uses `markovTrace_unique` to force the z_D weights. A P1 consumer of P3.SW output. |
| #7453 | — | Blueprint import. P3/P6. |

## Flags (empirical vs formal)

- `qou-adwi`: the Lean hardened a prose "~" Planck length into "=". → needs-owner.
- `4mrb` / `sv9q`: the `FourTermPairNucleonContext` instance supplies proton and neutron net values. These are empirical numbers in a Lean instance, and must not be read as a derivation.
- `6he8`: formalises an empirical deuteron "refutation".
- `bwhk` / `bwse`: Beasley–Witten = Hecke MTC is a physics identification posed as Lean work.
- `p88a`: recommends formalising identities its own check finds false.
- `citp`: a false theorem on main.

## Owner decisions needed

1. `qou-ar7f`: retire or re-point the `Mathlib/HeckeAlgebra` shadow classes. This gates SW-WIRE.
2. The `qou-luq7` / `h56b` class-field statements. Any restatement changes Lean math content, so it is owner-only.
3. `cr3v` / `x6q0` / `sekl`: these resolutions would remove Lean files or stubs, and the hard rule says no removal without the owner's say-so.
4. `fav8` / `b5w7`: how strong the QOU existence statement should be.
5. `citp`: the false theorem.
6. `adwi`: the Planck-length equality.

## Skill gaps hit

1. **No bean ↔ Lean-declaration status checker.** This analysis re-did by hand what `qou-sxyr` asks for, across about 100 beans. A generic folio-assistant skill would resolve a bean's cited declaration to {sorry / axiom / conditional on a class with or without an instance / unconditional} on demand.
2. **Instance detection by regex is unreliable.** My scan flagged `WedderburnDecomp` as having an instance; it has none. Correct answers need olean-backed `#print axioms` plus instance resolution. The `lean-formal-edges` skill exists, but the folio-assistant MCP server failed to connect, so `skill_fetch` was unavailable.
3. **No exact-title dedupe before `beans create`.** The vkmt/c8p8/bi00 trio happened despite the AGENTS.md rule.
4. **`gh` GraphQL is blocked in this environment.** PR bodies came through the REST `gh api` fallback; the PR skill should default to it.
