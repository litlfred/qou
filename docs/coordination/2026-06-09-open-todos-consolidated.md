# Consolidated open-todo ledger — 2026-06-09 (7-PR sweep)

**Author of sweep:** session `claude/hopeful-feynman-y0zsyy` (PR #2064).
**Why:** @litlfred (away ~1 week) asked, while sweeping the day's open PRs, to
"review all their workplan to see what's still open and consolidate todos."

**Scope swept:** PRs #2043, #2054, #2030, #2055, #2039, #2059, #2034 + 9
workplan/handover docs. **Merged during the sweep:** #2039, #2034, #2055,
#2054 (their recommended *work* stays open below; only the *docs* are now on
main). **Still open:** #2043, #2059 (Lean, dirty), #2030 (dirty — carries a
merge commit; needs cherry-pick not rebase).

> This is a coordination ledger, not paper content. Items are grouped by
> theme and deduped across the source docs. Each carries its source +
> rough size. Author-decision-gated items are flagged for @litlfred's return.

---

## A. Lean / proof gaps
| # | Todo | Source | Size |
|---|------|--------|------|
| A1 | 3 UGB well-foundedness sorries (`AlgOps.mkDegLexOrder.wf`, `NormalForms.lexLt_wf`, `JetOrder.degLexNat_wf`) — need Mathlib `List.Shortlex` | #2059 | substantive |
| A2 | 33 QOU content-block sibling sorries — survey + close where possible | #2059 | per-block |
| A3 | Lean v4.24.0 corpus-green verification (restore lake-cache; verify `LRCoefficientHecke`/`WenzlAOperator`/`MagicABindingFormula`/`IwahoriHecke`) | #2034 §1; week-review T2 | ~½ session, IMMEDIATE |
| A4 | Residual v4.24.0 timeouts: `Witness12C`, `HeckeEngine`, `PauliWitness A≥8` | week-review T2 | ~½ session |
| A5 | Cross-validate 2026-06-02 rapid-merge cluster (#1545/#1551/#1562/#1569/#1571) | #2039 §6-3 | ~½ session |
| A6 | `adelic-reeb-restricted-product.lean` `not_checked` → real `lake build` to flip `checked` | #2043 | small, CI-gated |
| A7 | Mathlib oleans cache-restore protocol verification | #2039 §6-2; #2034 §4 | ~1 session |
| A8 | `AvgCrossingPreservesGradeHolds` discharge — HARD-BLOCKED 20–40+ sessions; only `T_avg_squares_to_scalar` landed (#1569) | #2039 §4 | research; do NOT attempt blind |
| A9 | #2059 "Phase 1/2/4" — ⚠ cited `docs/workplans/2026-06-09-overall-strategy-update.md` **does not exist** anywhere (dangling) | #2059 | blocked/undefined |

## B. Bibliography
| # | Todo | Source | Size |
|---|------|--------|------|
| B1 | `freedman1994` borderline tier-3 — issue vs source-in-repo (author call) | session-handover §2; #2043 | trivial |
| B2 | Bib workflow phases 3–4 (photo-ingestion watcher; agent-sourced backfill over `uploads/`) | session-handover §3 | multi-session |
| B3 | Triage 333 unreviewed refs by availability (one issue per *physical*-access ref only; do NOT mass-seed) | session-handover §2 | ongoing |
| B4 | Triage fresh HUMAN-REVIEW refs `domagala-lewandowski-2004`, `meissner2004`, `ashtekar-baez-corichi-krasnov-1998` | session-handover §3 | small |

## C. Detangler / forward-refs
| # | Todo | Source | Size |
|---|------|--------|------|
| C1 | **4 author-call `def→def` edges** (surface, do NOT auto-move): skein-resolution-obstruction→computational-horizon; motivic-galois-character→adelic-substrate; adelic-substrate→classical-limit-functor; quark-antiquark-production→breit-wheeler-pair-production | #2030; detangler-handover; forward-ref-triage | author decision |
| C2 | #1998 leftovers: orphan re-homing · 2 within-band advisory sections · compound base titles | detangler-handover P2 | small |
| C3 | Confirm sibling #2020 rebases clean (`predicted-spectra.ts` churn) | detangler-handover P3-5 | verify |
| C4 | Corpus QA staleness ~1071 stale blocks — Lean-gated, sibling-owned (#1918/#1941) | detangler-handover P3-6 | deferred |

## D. Organic-chem / H₂O molecular
| # | Todo | Source | Size |
|---|------|--------|------|
| D1 | WS-A4: backing computes+witnesses for `ch4`/`co2`/`ilp-covalent` (theory-only .md) | organic-chem-redo WS-A | medium |
| D2 | WS-A5: run `lp_dual_witness_validator.py`; chemistry witnesses green | WS-A | small |
| D3 | WS-A3 (deferred): route chem scripts through `pyhecke.molecular` once #1062 lands | WS-A | blocked on #1062 |
| D4 | **WS-B de-hardcode** ~25 bare literals → `:val{witness=…}` (LP-dual B1; Alexander/barrier B2; benzene 1.40/1.54/1.34 Å) | WS-B; affectionate-hopper Item 4 | medium |
| D5 | WS-C general molecular projector + Lean (C1 strand-partition, C2 parabolic-Hecke, C3 `prop:assembly-projector-exists`, C4 benzene, C5 CH₄/CO₂) | WS-C | large |
| D6 | WS-D leftovers (mostly DONE in #2003 — confirm residual) | WS-D | mostly done |
| D7 | WS-E active-set=bond order: E1 CO/CO₂ probe; E2 SDP closed-shell→magic numbers | WS-E | medium-research |
| D8 | WS-F2: **correct `co-lp-dual-binding.md`** (single-chain triple-bond FALSIFIED → orthogonal-channel) — partly addressed by #2003; confirm .md rewrite landed | WS-F | medium |
| D9 | WS-G heat-as-probability (Markov-trace partition fn; catalyst = lowers peak-birthday) | WS-G | research |
| D10 | **Migrate ~55 `lean.validation: "not_started"` → `"not_checked"`** (enum dropped `not_started`) | affectionate-hopper Item 4 | mechanical |
| D11 | Item 4 branch hosts D4+D10 (**THIS session is doing it** — branch hopeful-feynman) | affectionate-hopper §0,§3 | — |

## E. Phase transitions / H₂O lattice  *(H₂O build itself DONE on main)*
| # | Todo | Source | Size |
|---|------|--------|------|
| E1 | Molecular chapter currency/wiring fix (purge λ_scale/Geom_full/scalar ρ_q; canonical pkgs + LP duals + witnesses) | phase-transitions step 0; `2026-06-08-molecular-chapter-currency-wiring-audit.md` | medium-large |
| E2 | Phase-ratio fixed point: running-q `T_boil/T_freeze = [n_K]_q` (integer-crossing REFUTED; needs `T_q=ℏ_q` fixed point) | phase-transitions step 2 | research |
| E3 | Knot-symmetry hierarchy of matter — promote to prop on `cor:knot-factor-borromean-composite` | phase-transitions step 3 | medium |
| E4 | Ice lattice symmetry (genuine GAP — no space-group content): lattice space-group × internal H₂O symmetry; `ex:ice-Ih-from-h2o` | phase-transitions step 4 | large, new structure |
| E5 | Electron shells in lattice (Hopf-trefoil shell model under lattice bonding) | phase-transitions step 5 | medium |
| E6 | Owner pre-build questions: qualitative ordering vs quantitative temps? fix q₀ or sweep q to anyonic bound? | phase-transitions §open | author decision |

## F. CI / infra
| # | Todo | Source | Size |
|---|------|--------|------|
| F1 | ~~Merge #2054~~ **DONE this sweep** (code-quality-gates on main) | #2054 | ✅ |
| F2 | Python ruff cleanup (un-ratchet): `universal-ilp.py`, substrate facade re-exports → `__all__`/`# noqa: F403` | #2054 | small |
| F3 | Rust clippy wildcard cleanup (~27–58 hits, mostly `use super::*` in tests) — ratchet new | #2054 | ongoing |
| F4 | Sidecar staleness sweep (≤10/commit per AGENTS.md idle rule) | #2034 §3; week-review | ½ session idle |
| F5 | STATUS.md housekeeping: bump "Last updated"→2026-06-09; clear stale Active-sessions rows | week-review | trivial |
| F6 | Stale-branch cleanup on origin (merged `claude/*` whose follow-up landed) | week-review | trivial |

## G. Q_β / precision
| # | Todo | Source | Size |
|---|------|--------|------|
| G1 | Q_β bridge experiment #3 — multi-block eigenphase in **fundamental rep** (not H₃ block sum); pass⟹formalise, fail⟹document floor-limited | qbeta-thread §3-1 | ~1 day, decisive |
| G2 | L1 1 ppb→1 ppQ: route `markov_peel` fast path through exact-mpf (drop `float()` cast, ~2.7e-16) | qbeta-thread §3-2 | concrete L1 win |
| G3 | Verify `canonical-no-negative-result-in-paper` checker catches new offenders; triage falsified-probe blocks → `docs/audits/` | qbeta-thread §3-4 | small sweep |
| G4 | m_μ 100× gap (209.8 ppb, ≈9.5σ) — ⚠ priority CONTRADICTION (week-review T1 vs #2039/qbeta HARD-BLOCKED); resolve before spending a session | week-review T1; #2039 §4 | research; see §contradictions |
| G5 | A≥3 binding −13% uniform bond under-strength — GAP-A-4/#1778/#1789/#1784 | qbeta-thread §4 | research, sibling-owned |
| G6 | Option-E Phase 2 KL enumeration — extend `kazhdan_lusztig.py` n≤4→S_6, re-run `n^w_λ` (#1516) | #2034 §2; #2039 §6-4 | ½–full session |

## H. Surreal / transcendental / LQG
| # | Todo | Source | Size |
|---|------|--------|------|
| H1 | `Σm=0 ⟺ 𝒪(ℙ(V))=A^{coT}` proposition — needs Lean weight-grading on `ℙ(V)=G_q/T_q` | session-handover §3 | medium |
| H2 | Conjecture-consumer triage on 13 newly-tagged `conj:*` blocks (commit `a54f1f8b`) — which open conjectures unblock most downstream | #2039 §6-1 | ≤1 session, high-leverage |

## I. Research-grade parked probes
I1 Δ_λ step-9b SW-residue/q-difference (preflight done) · I2 ζ₅ Goncharov depth-3 via Markov-trace (scaffold) · I3 Mass=Vol×Density+δ from non-abelian Stokes · I4 Mass-sweep A>12 (gated on H_{3A}) · I5 Yekutieli substrate m_p (Bring-zero-mode; 54 ppb residual) · I6 Flavor-split m_n/Δ_pn Habiro X(q) · I7 Casimir ξ_{even≥2} (parked, gated on N_⊙) · I8 Optical-fibre 1D QOU · I9 QA-backlog proof-braids.

---

## Cross-PR overlaps (deduped above)
1. Lean v4.24.0 corpus-green/cache-restore = A3+A5+A7 (in #2034, #2039, week-review).
2. Option-E Phase 2 KL = G6 (in #2034, #2039, week-review).
3. Sidecar staleness sweep = F4 (in #2034, week-review).
4. m_μ 210 ppb = G4 (Tier-1 in week-review BUT HARD-BLOCKED in #2039/qbeta — contradiction).
5. WS-B de-hardcode + `not_started`→`not_checked` = D4+D10+D11 (organic-chem-redo + affectionate-hopper).
6. `co-lp-dual-binding.md` correction = D8 (organic-chem WS-F2 + #2003 finding).
7. H₂O build = step-1 of phase-transitions AND h2o-molecular-braid-build — **DONE on main**.
8. Conjecture-consumer triage = H2 (#2039 + week-of-2026-06-01).

## Already done / closeable
- session-handover §1 (#2024 + #2011): **merged**.
- ohara1991 tier-3 seed + `prop:adelic-reeb-restricted-product`: **done in #2043** (open; lands on merge).
- surreal-rescope execution: **done** (#2024 territory).
- Quark sector Ch13→Ch9 (#2021), `def:commutative-qou` Ch9→Ch3 (#2016): **merged**.
- Detangler waive 61→4: **done in #2030** (open, needs cherry-pick).
- H₂O molecular build (4 blocks): **done on main** (#2014+#2013).
- #2003 molecular-bonds/WS-D + EmbeddableKnotOperator (Lean sorry-free) + benzene spine: **done** (`8eb7386b`).
- #1543 disciplines (corpus-grep-before-open etc.): **live on main**.

## Stale / contradictory (for author attention)
1. `2026-06-09-overall-strategy-update.md` **dangling** — #2059's "Phase 1/2/4" has no backing doc.
2. **m_μ priority contradiction** — week-review Tier-1 vs #2039/qbeta HARD-BLOCKED (`MuOverDetermination` Lean-proved over-determination). HARD-BLOCKED is newer/more specific.
3. Commit-count drift (~150 vs ~2481 vs ~2802) — different bucketing, cosmetic.
4. "3/7 vs 4/7 L2 met" — authoritative is **3/7** (m_μ demoted post-2026-05-28 re-pin).
5. Option-E "0.11% near-match" closure-claim **retracted** (main `d7f9749470`, CAL-4 violation) but week-review STATUS still lists it.
6. STATUS.md "Active sessions" stale (last 2026-06-01).

---

**Highest-leverage cheap wins:** C1 (4 author-call edges — owner decisions), H2 (conjecture triage ≤1 sess), G2 (L1→1ppQ mpf cast), A3 (Lean corpus-green ½ sess).
**Queue for @litlfred's return (author-decision-gated):** C1, E6, G4-contradiction, B1, D-chapter direction.
