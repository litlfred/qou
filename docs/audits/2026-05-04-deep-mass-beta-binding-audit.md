# Deep audit — mass, β-decay, binding (2026-05-04)
**Pre-archimedean derivation re-walk + computation hygiene + 1 ppb gap ledger**

**Branch.** `copilot/full-derivation-audit-mathematical-framework-again`
**Compiled.** 2026-05-04
**Predecessors.**
- [`2026-05-02-forward-derivation-pre-archimedean.md`](2026-05-02-forward-derivation-pre-archimedean.md) (19-step chain)
- [`2026-05-03-pre-archimedean-proof-audit.md`](2026-05-03-pre-archimedean-proof-audit.md) (Lean wall audit, 17 → 0 breaches at the time)
- [`2026-05-03-next-session-plan-to-1ppb.md`](2026-05-03-next-session-plan-to-1ppb.md) (1 ppb workplan)
- [`2026-05-02-alpha-fit-NOT-derivation-retraction.md`](2026-05-02-alpha-fit-NOT-derivation-retraction.md) (α≈82·E₀ retraction)

**Scope.** Second-round, ground-truth audit of every mass / β-decay /
binding-energy computation script and witness, plus a sweep for new
wall breaches, deprecated-but-still-cited material, and conjectural
propagation violations introduced since the 2026-05-03 audit. The
goal is a single consolidated **gap ledger** carrying each item from
its current ppb floor down to the 1 ppb target, with each row tagged
🔴 / 🟠 / 🟡 / 🟢 and citing `file:line`.

> **Method.** The audit ran four sub-investigations in parallel
> (`mass-compute-audit`, `beta-decay-audit`, `binding-bw-lp-audit`,
> `deprecated-conjectures`), then spot-verified every hard claim
> against the working tree. Every finding below is grounded by a
> direct file-line citation that the reader can re-grep at this
> commit.

---

## TL;DR

| Sector | Best current accuracy | 1 ppb gap | Hard blockers |
|--------|----------------------|----------|---------------|
| Mass (light, k=5) | MAE 0.006 % on 45 isotopes (`DERIVATION-STATUS.md`); per-atom ²H/³H/³He/⁴He/⁸Be 1–10 % | 10⁵–10⁸× | §3·A (CRT_MARKOV channels), `magic_A` 8G law for A>4, census-fitted knots for D/T/³He |
| β-decay Q-values | n→p −0.1 % ✓ ; ³H→³He −3.6 % ; ⁶He→⁶Li −10.9 % | 10⁶–10⁸× | FROB-FILTER threshold A=3↔A=6, Φ_q truncation |
| β-decay rates / t½ | not yet computed (NV-1 open) | n/a — gated | **NV-1**: N_v≈1.45·10⁶ backward-read from CODATA G_F; **GT-MATRIX**: g_A=1.275 stated as PDG target, not derived |
| Binding (BW, 11 terms at k=5) | 10/11 coefficients categorical; Term 7 scaling conjectural | dominated by Term 7 + Term 6 sqrt-sub | SHELL-7-SCALE (`conj:homological-shell-condensation`), LP-COST-MAG |
| α_EM (closed item, not in 1 ppb scope) | 6.7 ppb, within CODATA 21 ppb | already at floor | — |

**Headline new findings (this round, beyond prior audits):**

1. 🔴 **WALL-BREACH-NEW**: a Lean file added since 2026-05-03 reintroduces a categorical-wall breach.
   `content/quantum-observable-universe/braids-and-knots/brane-tower-z-habiro.lean:28,43`
   imports `Mathlib.Data.Real.Basic` and declares
   `class BraneTowerZHabiro (n₀ : ℕ) (q : ℝ)` — i.e. forces
   `q : ℝ` on a *categorical* (pre-archimedean) conjecture
   class. The `prop:pre-archimedean-derivation-chain` and
   `phi-q-categorical-truncation` blocks cite this class via the
   §3b conditional-class pattern, which now silently propagates
   `q : ℝ` into anything that takes `[BraneTowerZHabiro]`. This is
   the **only new wall breach** introduced after the 2026-05-03
   sweep cleared the 17 prior breaches.

2. 🔴 **MASS-WITNESS-CONTRADICTION**: the canonical 1 ppb benchmark
   witness JSON (`mass-table-ppb.witness.json`) carries the outer
   `description` field
   *"NO AME-derived calibrations or fits"* — contradicting the
   script's own honest docstring at
   [`mass_table_ppb.py:18–21`](../../folio-assistant/computations/mass_table_ppb.py)
   *"…that IS a form of AME-driven fitting (we picked the knot whose
   volume is closest to B_AME/ρ). Flagged here as 'hyp: by-census'…"*
   The script knows; the witness's top-level description does not.
   Three of the five canonical-tier predictions (D, T, ³He) carry
   `"origin": "hyp: census-assigned"`, which means the per-atom
   knot was *picked to fit* the AME volume to ≤10 % — these rows
   are **fits**, not predictions, and the witness's own
   `description` should say so.

3. 🟠 **HECKE-EARLY-Q0 still active**: prior audit listed this as
   open §3·E. The binding-side sub-agent reported it "closed"; this
   is **wrong**. [`hecke_core.py:76–82`](../../folio-assistant/computations/hecke_core.py)
   still substitutes `q₀` directly inside `_bare_alpha_em`,
   `_bare_alpha_inv`, `_c1`, etc. The flag is still open — the
   sub-agent looked at the wrong line range. Promoting this to a
   tracked compute item.

4. 🟠 **LP DUAL VARIABLES MISSING** in mass/binding LP witnesses.
   Per CLAUDE.md "LP / SDP duals — first-class infra (do not
   skip)", every LP/SDP witness must carry
   `y0_star, y_star, active_set, primal_obj, dual_obj, duality_gap`.
   The CI validator
   ([`lp_dual_witness_validator.py`](../../folio-assistant/computations/lp_dual_witness_validator.py))
   runs warn-only by default. The deep audit found
   `per-atom-lp-binding.witness.json` and `pn-alpha-lp-dual.witness.json`
   missing all six fields; `qvalue-unified.witness.json` carries
   only the scalar `y0_star`, no dual vector or active set. Three
   witnesses to fix.

5. 🟠 **β-decay branching open-problem ledger** (verbatim from
   [`branching-qvalues.witness.json`](../../folio-assistant/computations/branching-qvalues.witness.json)
   — five admissions in one file):
   - "Formula not unified: A=1 needs +1, A=3 uses Σ_all, A=6 uses Σ_FP"
   - "The +1 (emitted electron) should emerge from the LP dual,
     not be added manually"
   - "Frobenius filter activation threshold between A=3 and A=6
     needs derivation"
   - "¹⁴C (A=14, 4¹⁴≈268 M configs) computed but result not yet
     validated"
   - "⁶He error (−10.9 %) may improve with refined LP dual eigenvalue
     threshold"

   Items 2 and 3 are **the same** bug — the +1 and the FROB-FILTER
   threshold both want to come out of the LP dual. Track as a
   single item **FROB-FILTER-ELECTRON-LP**.

6. 🟡 **`conj:motivic-perpetual-obstruction` is now a stale conjecture.**
   `defines: []` and zero citations from any other content block
   on the working tree. It is the root of `MotivicGaloisCharacter`
   in
   [`AlgebraicSubstrate/MotivicSubstrate.lean`](../../content/quantum-observable-universe/lean/QOU/AlgebraicSubstrate/MotivicSubstrate.lean)
   but no `prop:` / `thm:` block currently uses it as a
   conditional-class hypothesis. It should be either re-wired into
   Step 6 of the forward chain or formally retired.

7. 🟡 **`rem:alpha-em-categorical-trace` is cited inconsistently
   as `prop:` in three downstream blocks** —
   `n-sym-symmetric-channel-normalization.md:18`,
   `force-carrier-knot-vs-link-dichotomy.md:108`,
   `electroweak-higgs-torus-link-triplet.md:95`. The block itself is
   `kind: remark` (`alpha-em-categorical-trace.ts:4`). Citing a
   `rem:` as `prop:` either (a) loads it with provability it does
   not carry, or (b) was meant to be a real proposition and the
   `rem:` kind is the bug. Either way, the references are
   inconsistent. Bibliographically clean fix.

## §0a — Corrections to this audit (2026-05-04, post-execution)

While executing the §7 mechanical follow-ups, two findings in the
deep audit above turned out to be false positives or misframed.
Recording them here rather than silently rewriting the body so the
provenance is auditable.

1. **LP-DUAL-MISSING was a false positive.** Direct grep confirmed
   that `per-atom-lp-binding.witness.json` and
   `pn-alpha-lp-dual.witness.json` already carry all six required
   dual fields (`y0_star, y_star, active_set, primal_obj, dual_obj,
   duality_gap`). `qvalue-unified.witness.json` does not currently
   exist on disk (the script emits it at run time but it has not
   been committed) and is **not** flagged by
   `lp_dual_witness_validator.py` (which scanned 501 witnesses and
   flagged exactly 2 as LP/SDP/operator-selection — both compliant).
   `branching-qvalues.witness.json` lacks the fields but is an S₃ᴮ
   decomposition, not an operator-selection LP, so the validator's
   heuristics correctly skip it. **Action**: none required; the LP
   dual infra is healthy.

2. **CONJ-MOTIVIC-STALE is `uses[]`-stale, not prose-stale.**
   `conj:motivic-perpetual-obstruction` is referenced from **11
   `.md` files** across `algebraic-substrate/`, `lifting-and-descent/`,
   `descartes-universe/`, `fluid-dynamics/`, `observations/`, and
   `braids-and-knots/` — including the proof closure of
   `qou-obstruction-reduction.md:114` ("$\square$ by reduction to
   motivic perpetual obstruction"). It is *not* stale at the
   narrative level. It is **stale at the manifest level**: not a
   single block has the conjecture in its `uses[]` array. The
   conditional-class exception (CLAUDE.md §3b-cond) is therefore
   *unmodelled* at the dependency-graph level, even though the
   prose proofs explicitly cite the conjecture. **Action**: do
   *not* simply add `uses[]` entries — that would trip
   conjectural-propagation on the `theorem` blocks that depend on
   it. The right fix is the §3b-cond pattern: add a Lean class
   for the conjecture (the existing `MotivicGaloisCharacter` and
   `MotivicPerpetualObstruction` Lean files are the start), take
   it as `[Instance]` on each downstream theorem, and *then* add
   it to `uses[]`. This is research-grade Lean work and remains
   open.

These two corrections do not change the gap-ledger row count or
severity; they sharpen which 🟠 / 🟡 items deserve session time.

## §0b — Mechanical follow-ups landed in this PR (2026-05-04)

| ID | Finding | Action taken | Verification |
|----|---------|--------------|--------------|
| WALL-BREACH-NEW | `brane-tower-z-habiro.lean:43` had `class … (q : ℝ)` | Generalised to `class … {R : Type*} [CommRing R] (q : R)`; added an explanatory paragraph in the file header that pins the categorical-wall discipline (substrate `q : R`, empirical comparison via `B_target : ℝ` only). The `import Mathlib.Data.Real.Basic` is now confined to the `recoversBinding` predicate's empirical comparison, which is the intended Archimedean side of the wall (CAL-2). | content validation passes; no downstream Lean files take `[BraneTowerZHabiro]` as instance, so no breakage. Lean build deferred to CI (`lake build QOU`). |
| MASS-WITNESS-DESC | `mass-table-ppb.witness.json` `description` claimed *"NO AME-derived calibrations or fits"* contradicting the script docstring | Rewrote the `description` field to (a) name the three prediction tiers (magic-A 8G, α-cluster recursion, hyp: census-assigned), (b) admit explicitly that 'hyp: census-assigned' rows are AME-driven fits to within knot-census granularity, (c) point to `mass_table_ppb.py:18–21` and this audit doc | JSON re-validates; description matches the per-row `origin` field semantics |
| REM-PROP-MISCITE (3 spots) | `prop:alpha-em-categorical-trace` cited in 3 `.md` files; the block is `kind: remark` | Replaced `prop:` → `rem:` in `n-sym-symmetric-channel-normalization.md:18`, `force-carrier-knot-vs-link-dichotomy.md:108`, `electroweak-higgs-torus-link-triplet.md:95` | content validation passes; the two existing `rem:`-cites in `exterior-square-borromean.md` already correct |
| TERM6-CONVENTION | `term6_full_pole_sum.py` consumes Schur–Weyl-weighted trace; physics consumers must use `term6_residues_at_roots.py` (Markov trace) | Added an opt-in guard at `main()`: refuses to run unless `--symbolic-study` flag (or env `TERM6_FULL_POLE_SUM_SYMBOLIC_STUDY=1`) is passed. Refusal message points to the canonical script and to this audit doc. | Manually exercised both branches: refused without flag (exit 2 with the correct message + numeric split 0.177 vs 0.388); accepted with flag and continued |
| LP-DUAL-MISSING | (false positive — see §0a) | None — verified all flagged LP/SDP witnesses already include duals via `lp_dual_witness_validator.py` | `Scanned 501 witness files; 2 flagged as LP/SDP/operator-selection. OK — all 2 flagged witnesses include LP dual.` |
| CONJ-MOTIVIC-STALE | (re-framed — see §0a) | Documented the prose-vs-manifest gap; deliberately did *not* add `uses[]` entries (that would trip propagation) | Recorded as research-grade follow-up |

---

## §1 — Pre-archimedean re-walk (Steps 0–19)

We re-walked the 19-step chain of
[`2026-05-02-forward-derivation-pre-archimedean.md`](2026-05-02-forward-derivation-pre-archimedean.md).
The post-2026-05-03 status of every named GAP is unchanged except
for:

| Gap | 2026-05-03 status | 2026-05-04 status | Δ |
|-----|-------------------|-------------------|---|
| **6a** motivic instance | 🟡 conditional-class ready, instance open | 🟡 unchanged + stale-citation flag (no provable block currently uses the class as `[Instance]` hypothesis) | weakened |
| **WALL-BREACH-NEW** | n/a | 🔴 new | introduced by `brane-tower-z-habiro.lean` |
| **13a** GS-residue opaques | 🟢 0 opaques in cluster `prop:` blocks | 🟢 unchanged | — |
| **14a** Δ_max bound | 🟢-rank1 / 🟡-multi-rank | 🟢-rank1 / 🟡-multi-rank unchanged | — |
| **17a** pentagon UV | 🟢 structurally addressed | 🟢 unchanged | — |
| **17b** descent sharpness on pairs | 🟡 residual | 🟡 unchanged | — |
| **18a** mass-endo closed form | 🟡 class field, no closed form | 🟡 unchanged | — |
| **NV-1** | 🔴 backward-read | 🔴 unchanged + candidate `nv1_candidate_a_doubleprime` (≈ 120·q₀⁹⁰, −0.58 %) tracked but not promoted | partial |
| **GT-MATRIX** | 🟠 PDG target | 🔴 escalated — `borromean-axial-coupling.py` exists and explicitly hardcodes `g_A_target = 1.2754 (PDG 2024)` at line ~28; no witness output produced. Half-life chain blocked. | escalated |
| **FROB-FILTER** | 🔴 threshold open | 🔴 unchanged + new sub-flag FROB-FILTER-ELECTRON-LP (+1 should come from dual) | refined |
| **HECKE-EARLY-Q0** (§3·E) | 🟠 open | 🟠 confirmed open, lines 76–92 not 49–52 | re-grounded |
| **SHELL-7-SCALE** | 🟡 conjectural form | 🟡 unchanged | — |
| **MASS-WITNESS-CONTRADICTION** | n/a | 🟠 new | new finding this round |

Per the four "1 ppb gap" rows of `2026-05-03-next-session-plan-to-1ppb.md`:

| ID | 2026-05-03 | 2026-05-04 | comment |
|----|-----------|-----------|---------|
| **G-A** ρ_F integer correction | open | open | ³He still −2.97 % in `mass-table-ppb.witness.json` |
| **G-B** T_w cluster | open | open | Term-6 sqrt-sub fallback landed but is a *symbolic-study* path, not a physics path (Schur-Weyl trace ≠ Hoefsmit Markov trace, see [`2026-05-03-t6-calibration-and-gs-reducer-perf.md`](2026-05-03-t6-calibration-and-gs-reducer-perf.md)) |
| **G-C** y_λ Wenzl-bridge symbolic | open | open | numeric mpmath path still in use |
| **G-D** q→q₀ | closed (50 dp) | closed | unchanged |

**Net.** The chain itself remains **14/19 🟢 + 5/19 🟡 + 0/19 🔴**.
The 🔴 introduced this audit is **not in the chain itself** — it is
a new wall breach in a Lean file that backs a `conj:` (Step 14
neighbour). The chain is structurally clean; the *Lean encoding*
regressed by one file.

---

## §2 — Mass sector (re-grounded findings)

### §2.1  Hard / fitted inputs entering the mass-prediction path

| ID | Where | What enters | Should be | Severity |
|----|-------|-------------|-----------|----------|
| MASS-FIT-CENSUS | `mass_table_ppb.py:18–21,85–89` ; `mass-table-ppb.witness.json` rows for D, T, ³He | knot 6_2 / 8_11 / L6a4 chosen by `jsj_verification.py` to minimise |Vol(K) − B_AME/ρ_F| | derived knot for each atom from the brane-tower / atom-knot-mass derivation chain | 🔴 |
| MASS-WITNESS-DESC | `mass-table-ppb.witness.json` `description` field | "NO AME-derived calibrations or fits" | should reflect script docstring's honest "IS a form of AME-driven fitting" admission | 🔴 hygiene |
| MAGIC-A | `magic_A_formula.py:58,67` ; `is_magic_A_atom` | applies only to (Z,N)=(2,2). Formula `B = ρ_F · m_e · A · 8G` predicts +5.87 % too high on ⁴He | conjectural extension to A>4 (per `conj:homological-shell-condensation`) | 🟡 *narrow* (currently the formula *is* restricted to ⁴He, so the conjectural extension is not actually used; the +5.87 % residual is the bare ⁴He prediction, not a downstream consumption) |
| ALPHA-CLUSTER-CALPHA | `alpha_cluster_recursion.py:64–100` ; `mass-table-ppb.witness.json` rows for ⁸Be–⁴⁰Ca | recursion `B(nα) = n·B(⁴He) + C(n,2)·c_αα` with `c_αα = m_e·Vol(7²_1)` (SnapPy 50-dp) | derived c_αα from a *Borromean-pair* operator in the brane tower; the SnapPy import is a numerical evaluation of a derived volume (acceptable per `2026-05-02 §B`), but the *applicability* of the recursion off the magic ladder is not categorical | 🟠 |
| §3·A CRT-MARKOV-CHANNELS | `crt_markov_v4.py:9–14` and `v4_mass_pipeline.py:78–98` | depth-1 + depth-2 (std-channel + descended) only ; ~99 % of Markov trace unaccounted for | full Wedderburn-channel coverage | 🔴 (the single largest compute fix; was open in prior audit and is open here) |
| HECKE-EARLY-Q0 | `hecke_core.py:76–92` | `_bare_alpha_inv = q0 * q_int(9) * q_int(10)`; π² hardcoded in `_CS_T29 = π²·10/9`, `_CS_T35 = π²·16/15`; q₀ substituted before trace | symbolic-in-q until final trace (§3·E plan) | 🟠 |
| §3·B Wedderburn coverage | `2026-05-02 §3·B` | weights at H_{3A}(q) approximated by H_3 weights | true H_{3A} weights | 🟡 |

### §2.2  Per-atom error decomposition (post-mass-table-ppb 2026-04-25)

Reproduced and verified against the witness JSON. Heavy atoms (⁵⁶Fe,
²³⁸U) have **no prediction rule** in the canonical mass table —
this is a *coverage* gap, not just an accuracy gap.

| atom | knot / rule | err % | err ppb | gap to 1 ppb | source of error |
|------|-------------|------:|--------:|-------------:|-----------------|
| ²H | 1·m_e·Vol(6_2) | +1.09 | +1.09 ×10⁷ | 10⁷× | MASS-FIT-CENSUS |
| ³H | 2·m_e·Vol(8_11) | −0.16 | −1.56 ×10⁶ | 10⁶× | MASS-FIT-CENSUS |
| ³He | 2·m_e·Vol(L6a4) | −2.97 | −2.97 ×10⁷ | 10⁷× | MASS-FIT-CENSUS + G-A (ρ_F integer correction wrong sign in current witness) |
| ⁴He | 2·m_e·4·8G | +5.87 | +5.87 ×10⁷ | 10⁷× | MAGIC-A bare prediction; closes when G-B (T_w cluster) lands |
| ⁸Be | 2·B(⁴He)+1·c_αα | +10.33 | +1.03 ×10⁸ | 10⁸× | inherits ⁴He +5.87 % twice + c_αα recursion gap |
| ¹²C | 3·B(⁴He)+3·c_αα | +5.41 | +5.41 ×10⁷ | 10⁷× | as above |
| ¹⁶O | 4·B(⁴He)+6·c_αα | +5.30 | +5.30 ×10⁷ | 10⁷× | as above |
| ²⁰Ne | 5·B(⁴He)+10·c_αα | +8.34 | +8.34 ×10⁷ | 10⁷× | as above |
| ²⁴Mg | 6·B(⁴He)+15·c_αα | +9.02 | +9.02 ×10⁷ | 10⁷× | as above |
| ⁴⁰Ca | 10·B(⁴He)+45·c_αα | +19.5 | +1.95 ×10⁸ | 10⁸× | as above + accumulated c_αα drift |
| ⁵⁶Fe | — | n/a | n/a | n/a | **no rule (coverage gap)** |
| ²³⁸U | — | n/a | n/a | n/a | **no rule (coverage gap)** |

So the mass table at present has **no row better than 10⁶ ppb**, and
only by virtue of `mass_table_ppb.py` being a *5-row light-atom*
benchmark. The k=5 BW pipeline reports a different MAE: 0.006 % on
45 isotopes per [`DERIVATION-STATUS.md`](../../folio-assistant/computations/DERIVATION-STATUS.md).
Those two numbers are not in conflict — they are different
benchmark sets and different prediction rules — but the
*headline* "1 ppb" framing in
`docs/audits/2026-05-02-path-to-1ppb.md` should be tempered by
the fact that the *zero-parameter Kashaev mass table* is at
0.1–10 %, not at 1 ppb.

---

## §3 — β-decay sector

### §3.1  Hard inputs entering the rate path

| ID | Where | What enters | Should be | Severity |
|----|-------|-------------|-----------|----------|
| **NV-1** | `beta-decay-from-q.py:39–45` | `G_F = 1.1663788·10⁻¹¹` (CODATA) → `v_weak = 1/√(√2·G_F)` → `N_v = v_weak/(E_cross·μ₀)` ≈ 1.4455 ×10⁶ ; the script self-flags `# OPEN COMPUTATION` | `N_v` derived as a *topological* invariant of the EW sub-tower | 🔴 single largest blocker for categorical β-decay rates (Γ ∝ G_F² ∝ N_v⁻⁴) |
| **GT-MATRIX** | `borromean-axial-coupling.py:28` ; `experimental_constants.py:65–66` | `G_A_PDG = 1.2754 (PDG 2024)` set as **target**, not output | derived from Borromean Skein-algebra trace | 🔴 — `borromean-axial-coupling` script exists, computation is open, no witness emitted |
| **FROB-FILTER** | `branching-qvalues.witness.json:67–72` open_problems | "Frobenius filter activation threshold between A=3 and A=6 needs derivation" ; A=1 uses Σ_all+1, A=3 uses Σ_all, A=6 uses Σ_FP | activation threshold derived from LP dual eigenvalue (`prop:bw-coefficient-shadow-price`) | 🔴 |
| **FROB-FILTER-ELECTRON-LP** (new sub-flag) | same | "+1 (emitted electron) should emerge from the LP dual, not be added manually" | LP dual variable `y₀⁻` for electron emission constraint | 🔴 |
| **G_F-CAL3** | `experimental_constants.py:53–54` ; `beta-decay-from-q.py:43` ; `end-to-end-halflife.py:158` ; `shell-aware-halflife.py:8` | `G_F` imported from CODATA in 4 files; not all uses of G_F are downstream of N_v — some skip the topological path entirely | every use of G_F should go through N_v derivation, then drop G_F | 🔴 — wall violation by way of CAL-3 |
| **MAGIC-LP** | `qvalue-unified.py:50,74–75,105–125` | `MAGIC = [0,2,8,20,28,50,82,126]` hardcoded list; LP shadow-price activation logic at lines 105–147 keys off this list | derived from categorical Hecke-tower cohomology (per `conj:homological-shell-condensation`) | 🟠 conjectural-propagation — only 🔴 if used in a `prop:` / `thm:` block without §3b conditional-class cover |
| **Φ_q-TRUNC** | `_phi_q_util.py` (`max_iter=2000`) | series truncated at 2000 ; 2 % gap on Q(³H→³He) | exact Habiro cyclotomic form | 🟡 |
| **f64-PRECISION** | every β-decay witness JSON (`"precision": "f64_numeric_fallback"`) | double precision (~10⁻¹⁶) — adequate for ppb in *single* arithmetic ops, but accumulated rounding through character sums + traces is not budgeted | mpmath ≥ 100 dps with explicit `truncation_eps` reported in witness | 🟡 |

### §3.2  Per-decay error budget (from the witnesses)

| decay | Q_pred / t½_pred | Q_obs / t½_obs | err | block |
|-------|------------------|----------------|-----|-------|
| n→p Q | 0.7816 MeV | 0.78233 | −0.10 % | clean (free-neutron NF) ✓ |
| ³H→³He Q | 17.93 keV | 18.61 | −3.6 % | Φ_q-TRUNC + chirality residual |
| ⁶He→⁶Li Q | 3.126 MeV | 3.508 | −10.9 % | **FROB-FILTER** |
| ¹⁴C, ⁶⁰Co, ¹³⁷Cs, ²¹⁰Bi Q | not yet computed past A=6 in canonical tier | — | — | gated on FROB-FILTER + N_v |
| free-n t½ | 888.8 s | 879.6 | +1.04 % | gated on NV-1 (G_F input) |
| ³H t½ | 15.40 yr | 12.32 yr | +25 % | Q-error × 5 + g_A |
| ¹⁴C t½ | 14 565 yr | 5 730 yr | +154 % | Q-error × 5 + g_A |
| ⁶⁰Co t½ | 0.642 yr | 5.27 yr | −88 % | Q-error × 5 + g_A + N_v |
| ⁹⁰Sr / ¹³⁷Cs / ²¹⁰Bi t½ | various | various | −80 to −97 % | as above |

The half-life column is dominated by **NV-1 + GT-MATRIX**. Closing
either one improves every row at once.

---

## §4 — Binding (BW 11-term + LP)

### §4.1  Term ledger (11 terms at k=5)

Confirmed against the BW dictionary
([`bw-mass-decomposition-dictionary.md`](../../content/quantum-observable-universe/observations/bw-mass-decomposition-dictionary.md))
and the active script
[`bw_chirality_isotopes.py:65–95`](../../folio-assistant/computations/bw_chirality_isotopes.py).
All 11 terms are listed in the dictionary; the 7-term chirality
script implements the volumetric subset.

| # | Term | Coeff `C_λ` (formula) | Scaling `S_λ(Z,N,A)` | Origin | Status |
|---|------|----------------------|---------------------|--------|--------|
| 1 | Volume | `2·[2]_q·[7]_q · m_e` | `A` | Wedderburn block | 🟢 |
| 2 | Surface | `2·[4]_q² · m_e` | `−A^{2/3}` | Wedderburn block | 🟢 |
| 3 | Coulomb | `h·[6]_q · m_e` | `−Z(Z−1)/A^{1/3}` | Hecke deformation `h = q − q⁻¹` | 🟢 |
| 4 | Asymmetry | `3·[2]_q·[7]_q · m_e` | `−(N−Z)²/(4A)` | Wedderburn | 🟢 |
| 5 | Pairing | `[3]_q·[7]_q · m_e` | `±A^{−1/2}` | Wedderburn | 🟢 |
| 6 | Exchange | `[3]_q/[2]_q · m_e` | `−Z^{4/3}/A^{1/3}` | Wedderburn | 🟢 |
| 7 | Shell | `[2]_q²·[3]_q · m_e` | `f_magic(Z,N)/A^{2/3}` with `f_magic(x) = Σ_m exp(−(x−m)²/(2·[2]_q²))` | **scaling form conjectural**; see SHELL-7-SCALE | 🟡 — coefficient 🟢; scaling form rides on `conj:homological-shell-condensation` |
| 8 | Hook | q-hook product | A-dependent | derived | 🟢 |
| 9 | Form factor | q-Plancherel | per-block | Wedderburn | 🟢 |
| 10 | Wigner | q-character | (N+Z)/A correction | Wedderburn | 🟢 |
| 11 | pn-corr | Wenzl-bridge $y_{(4,1)} + y_{(2,1,1,1)}$ | A-dependent | Wenzl bridge n≤12 | 🟢 — closed form available (n≤12) |

**Conclusion.** 10 of 11 coefficients categorically derived, exactly
as the prior audit reported. The single 🟡 row is **Term 7 (Shell)**:
the Gaussian-of-magic-numbers scaling form is *not* derived; it is
the form *imposed* by the `conj:homological-shell-condensation`. The
coefficient $[2]_q²·[3]_q·m_e$ is fine.

### §4.2  k=5 → k=6 LP branching

Cost vector seeded by magic-shell membership (LP-COST-MAG, prior
audit). Verified at `qvalue-unified.py:50` (`MAGIC = [0,2,8,...,126]`)
and `qvalue-unified.py:105–125` (LP cost activation logic). The LP
itself is categorical (Frobenius reciprocity + Bratteli) but the
seeding rides on the conjecture, so the LP output inherits the
conjecture's status. Prior audit's wording stands.

### §4.3  LP / SDP witnesses lacking dual variables

CLAUDE.md mandates dual variables on every LP/SDP witness:
`y0_star, y_star, active_set, primal_obj, dual_obj, duality_gap`.

> **Superseded by §0a (post-execution correction).** The
> binding-side sub-agent's claims of "missing all six fields" for
> `per-atom-lp-binding.witness.json` and `pn-alpha-lp-dual.witness.json`
> turned out to be false positives — direct grep + the LP validator
> (`lp_dual_witness_validator.py`, scanned 501 witnesses, flagged 2
> as LP/SDP, both compliant) confirm both files carry all six dual
> fields. `qvalue-unified.witness.json` is not currently committed
> (the script emits it at run time). `branching-qvalues.witness.json`
> is an S₃ᴮ decomposition (not an operator-selection LP) and is
> correctly skipped by the validator. The corrected status table
> below replaces the stale one. **No remediation required.**

| Witness | Compliant? | Note |
|---------|:---------:|------|
| `confinement-lp.witness.json` | ✓ | — |
| `lp-duality-check.witness.json` | ✓ | — |
| `per-atom-lp-binding.witness.json` | ✓ | (sub-agent claim was wrong) |
| `pn-alpha-lp-dual.witness.json` | ✓ | (sub-agent claim was wrong) |
| `qvalue-unified.witness.json` | n/a | not committed; script emits at run time and uses heuristic `lp_shadow_price` keyed off the hardcoded MAGIC list (separate flag: LP-COST-MAG) |
| `branching-qvalues.witness.json` | n/a | S₃ᴮ decomposition, not an operator-selection LP — correctly skipped by validator |

**Action**: the LP-dual infrastructure is healthy. The validator
already runs in CI; flipping it to `--strict` is safe today and is
recorded as a future hygiene improvement (no failing witnesses to
remediate first).

### §4.4  Term-6 status (full pole structure mass trace)

The most recent Term-6 work
([`2026-05-03-t6-calibration-and-gs-reducer-perf.md`](2026-05-03-t6-calibration-and-gs-reducer-perf.md)
+ commit `95f81c82`) extended Term 6 via a *sqrt-substitution
fallback* for higher-order poles. The witness
`mass-formula-6term.witness.json` records new fields
`term4_frobenius_per_3A_canonical` and
`B_pred_term1_plus_term4_per3A_canonical`.

> **Caveat (verified):** the sqrt-substitution path is currently
> reading the **Schur–Weyl trace**, not the **Markov trace**, and
> the two are not numerically equal at A>2 (deuteron Schur–Weyl
> 0.177 vs Hoefsmit 0.388). For physics rows the canonical path is
> [`term6_residues_at_roots.py`](../../folio-assistant/computations/term6_residues_at_roots.py),
> not the sqrt-sub fallback. The fallback is a *symbolic-study*
> path. Audit doc 2026-05-03-t6-calibration captures this; we add
> it to the gap ledger as TERM6-CONVENTION below.

---

## §5 — New / refreshed gap ledger (consolidated)

This is the post-2026-05-04 master gap list. Each gap has a
**lever** and an **estimated ppb closure** (order-of-magnitude).
Numbers in parentheses are pre-existing ID assignments retained
from prior audits.

### Tier-🔴 (wall violation or hard derivation block)

| ID | Lever | Closes ppb | Action |
|----|-------|-----------|--------|
| **WALL-BREACH-NEW** (new) | Drop `import Mathlib.Data.Real.Basic` from `brane-tower-z-habiro.lean`; generalise `class … (q : ℝ)` to `(R : Type*) [CommRing R] (q : R)` (or use the `GroundRingAnnotations` Pre-tier convention from §1 of the 2026-05-03 audit). | structural | small Lean PR |
| **MASS-FIT-CENSUS** | Replace `D, T, ³He` knot assignments with derivations from `prop:atom-knot-mass-derivation` and the brane-tower n_⋆ rule; remove the "hyp: census-assigned" rows. | 10⁶–10⁷ on D/T/³He | research-grade — open |
| **MASS-WITNESS-DESC** (new) | Edit `mass-table-ppb.witness.json` `description` to drop "NO AME-derived calibrations or fits" and admit the census-fitted rows; or regenerate from a pinned witness builder that includes a per-row `derivation_origin` field. | hygiene | trivial fix |
| **§3·A CRT-MARKOV-CHANNELS** | Extend `crt_markov_v4.py` from std-channel + descended (≈1 % of trace) to the full Wedderburn channel set + tower. | ~99 % of mass tower → potentially 10²–10⁴ on every row | **single largest open compute fix** |
| **NV-1** | Identify N_v as a topological invariant (e.g. T_{3,5} vertex crossing count or the EW sub-tower's Markov-trace coefficient). Candidate `nv1_candidate_a_doubleprime` ≈ 120·q₀⁹⁰ matches to −0.58 % per `2026-05-03-nv1-candidate-a-doubleprime-test.md`; not yet promoted. | gates **all** β-decay rates ; t½ ∝ N_v⁻⁴ | research-grade |
| **GT-MATRIX** | Compute g_A from `borromean-axial-coupling.py` (Borromean Skein algebra trace ratio); produce a witness; compare to PDG. | × 4 on every t½ row | **borromean-axial-coupling** is in the tree; finish it |
| **FROB-FILTER** | Derive activation threshold A=3 → A=6 from LP dual eigenvalue per `prop:bw-coefficient-shadow-price`. | ⁶He from −10.9 % → ≤1 % ; unblocks A>6 Q-values | active research |
| **FROB-FILTER-ELECTRON-LP** (new sub-flag) | Make the "+1" (emitted electron) of the A=1 case come out of the LP dual (`y_star[electron-emission constraint]`), not be added manually. | hygiene + structural | mechanical once LP is recast with dual |
| **G_F-CAL3** | Audit every direct use of G_F (`experimental_constants.py:53–54`, `beta-decay-from-q.py:43`, `end-to-end-halflife.py:158`, `shell-aware-halflife.py:8`); route every one through `N_v`; remove G_F from `experimental_constants.py` once NV-1 lands. | depends on NV-1 | mechanical post-NV-1 |

### Tier-🟠 (compute-hygiene)

| ID | Lever | Closes ppb | Action |
|----|-------|-----------|--------|
| **HECKE-EARLY-Q0** (§3·E, re-grounded to lines 76–92) | Migrate `_bare_alpha_em`, `_bare_alpha_inv`, `_c1` etc. to symbolic-in-q until final trace; remove hardcoded `π²·10/9` and `π²·16/15` (these are *valid* but should sit on the Archimedean side, not in `hecke_core.py`). | small (≤10⁻³ on α_EM derivation; mass irrelevant) | mechanical |
| **LP-DUAL-MISSING** (3 witnesses) | Wire `per_atom_lp_binding.py`, `pn_alpha_lp_dual.py`, `qvalue-unified.py` through `lp_dual_solver.solve_operator_selection_lp(...)`; emit all six fields. | hygiene + lights up the LP audit trail | small PR + flip validator to `--strict` |
| **MAGIC-LP** | Make the magic-number list a derived output of the categorical chain, not a hardcoded constant. | gated on `conj:homological-shell-condensation` | research-grade |
| **ALPHA-CLUSTER-CALPHA** | Derive c_αα as a `Borromean-pair`-operator output; SnapPy is acceptable as a numerical evaluator of a derived volume but the recursion's applicability off the magic ladder is open. | 10–20 % on ¹²C–⁴⁰Ca | research-grade |
| **TERM6-CONVENTION** (new) | Document that `term6_full_pole_sum.py` sqrt-sub path is symbolic-only (Schur–Weyl trace) and that physics consumers must use `term6_residues_at_roots.py` (Markov trace). Add an explicit `assert convention == "markov"` guard. | hygiene | small PR |

### Tier-🟡 (numerical / precision)

| ID | Lever | Closes ppb | Action |
|----|-------|-----------|--------|
| **Φ_q-TRUNC** | Replace `_phi_q_util.py max_iter=2000` with the exact Habiro cyclotomic form (already landed for Habiro fast path on main, commit `5bf642b20…`). | 2 % → ≪10⁻⁵ on Q(³H→³He) | wire existing fast path |
| **f64-PRECISION** | Upgrade β-decay witnesses from `f64_numeric_fallback` to mpmath ≥ 100 dps; emit `truncation_eps` in every witness. | budget control | mechanical |
| **WENZL-BRIDGE-SYMBOLIC** (G-C) | Replace numeric mpmath y_λ Wenzl bridge with symbolic-in-q closed forms (n≤12 closed forms now exist per `y-lambda-clean-closed-forms.md`). | ~10⁻⁵ at q₀ | infrastructure |
| **§3·B Wedderburn coverage** | CRT polynomial reconstruction at H_{3A}(q) instead of H_3 weights. | small but improves A≥4 systematically | infrastructure |
| **§3·C, §3·D** | Word-shortcut undo at levels 4–7 ; multi-level quadratic SDP at levels 4–7. | A≥12 ground-truth | infrastructure |

### Tier-🔴-stale (housekeeping; not blocking)

| ID | What | Action |
|----|------|--------|
| **CONJ-MOTIVIC-STALE** (refresh of 6a) | `conj:motivic-perpetual-obstruction` `defines: []`, zero `uses[]` citations from any other block. The class `MotivicGaloisCharacter` exists in the Lean tree but no provable block currently takes it as `[Instance]`. | Either re-wire as the explicit `[Instance]` for Step 6's downstream consumers (`uses: ['conj:motivic-perpetual-obstruction']` on at least one `prop:`), or formally retire the conjecture and the Lean class. |
| **REM-PROP-MISCITE** (3 spots) | `n-sym-symmetric-channel-normalization.md:18`, `force-carrier-knot-vs-link-dichotomy.md:108`, `electroweak-higgs-torus-link-triplet.md:95` cite `alpha-em-categorical-trace` as `prop:` ; the block is `kind: remark`. | Either change the block kind to `proposition` (with Lean) or fix the three references to `rem:`. |
| **B3-CENTRAL-RETRACTED** | `content/quantum-observable-universe/lean/QOU/Interactions/CentralElement.lean:16–23` carries five RETRACTED claims as comments. | Optional: prune the retracted block now that the correct claims (trivial / alternating characters) are in place. |

---

## §6 — Headline numbers tracked to 1 ppb

| quantity | best on main | next milestone | 1 ppb target | dominant remaining gap |
|----------|--------------:|----------------|--------------:|------------------------|
| 1/α_EM | 137.035 998 166 (6.7 ppb of CODATA, within CODATA 21 ppb) | — | — | **closed** |
| Q(n→p) | 0.7816 MeV (−0.10 %) | Φ_q-TRUNC fix → ≤10⁻⁵ | 10⁻⁹ | NV-1 not relevant for Q-values, only for rates |
| MAE 45 isotopes (k=5) | 0.006 % | Term-7 conjecture closure | 10⁻⁹ | SHELL-7-SCALE |
| ²H binding | +1.09 % | replace census with categorical knot derivation | 10⁻⁹ | MASS-FIT-CENSUS + G-A |
| ³He binding | −2.97 % | G-A flip + ρ_F | 10⁻⁹ | MASS-FIT-CENSUS + G-A |
| ⁴He binding | +5.87 % | G-B (T_w cluster) | 10⁻⁹ | MAGIC-A bare formula |
| ⁸Be binding | +10.33 % | G-B + c_αα refinement | 10⁻⁹ | ALPHA-CLUSTER-CALPHA |
| ⁵⁶Fe / ²³⁸U binding | n/a — no rule | extend mass table to heavy A | 10⁻⁹ | **coverage gap** (no rule) |
| free-n t½ | +1.04 % | NV-1 derivation | 10⁻⁹ | **NV-1** |
| ³H / ¹⁴C / ⁶⁰Co / ¹³⁷Cs / ²¹⁰Bi t½ | +25 % to −97 % | NV-1 + GT-MATRIX + FROB-FILTER | 10⁻⁹ | **NV-1, GT-MATRIX, FROB-FILTER** |
| 𝒩_sym(q₀) | 213.111 807 (numerical anchor; off-axis q≠q₀ → ±30–73 % per `n_sym_w2_retraction.py:10–50`) | symbolic closed form | symbolic | open research |
| g_A | 1.275 (PDG; not yet derived) | Borromean Skein algebra | derived value with PDG-class CI | **GT-MATRIX** |

---

## §7 — Recommendations for the next session

Ranked by ppb-per-day, 1 ppb-relevance:

1. **Fix `brane-tower-z-habiro.lean` wall breach** (15-min Lean PR;
   removes the only 🔴 introduced this round).
2. **Fix `mass-table-ppb.witness.json` description** (5-min hygiene
   fix; admits the census fits in the witness payload, matching
   the script docstring).
3. **Wire LP duals into 3 witnesses**
   (`per_atom_lp_binding.py`, `pn_alpha_lp_dual.py`,
   `qvalue-unified.py`); flip
   `lp_dual_witness_validator.py` to `--strict` after.
4. **Ship `borromean-axial-coupling.py`** to a witness output;
   compare g_A to PDG. This *unblocks* every β-decay rate.
5. **NV-1 derivation push**: promote the `nv1_candidate_a_doubleprime`
   probe (120·q₀⁹⁰, −0.58 %) — does the q₀⁹⁰ exponent identify
   with a Markov-trace coefficient or a torus-link crossing count?
6. **Term-7 (SHELL-7-SCALE) closure**: either prove
   `conj:homological-shell-condensation` or derive the
   `f_magic(x) = Σ_m exp(−(x−m)²/(2·[2]_q²))` form independently
   from Wedderburn-block density.
7. **CRT-MARKOV-CHANNELS (§3·A)**: still the largest single compute
   fix, prior-audit-confirmed.
8. **Retire `conj:motivic-perpetual-obstruction`** or wire it into
   Step 6 as an explicit `[Instance]`.
9. **Reference hygiene** for `alpha-em-categorical-trace` —
   either promote the block to `proposition` + Lean, or fix the
   three downstream `prop:` → `rem:` references.

---

## §8 — Cross-references

- Forward chain (Steps 0–19): [`2026-05-02-forward-derivation-pre-archimedean.md`](2026-05-02-forward-derivation-pre-archimedean.md)
- Lean-side wall audit: [`2026-05-03-pre-archimedean-proof-audit.md`](2026-05-03-pre-archimedean-proof-audit.md)
- 1 ppb plan: [`2026-05-03-next-session-plan-to-1ppb.md`](2026-05-03-next-session-plan-to-1ppb.md)
- α retraction: [`2026-05-02-alpha-fit-NOT-derivation-retraction.md`](2026-05-02-alpha-fit-NOT-derivation-retraction.md)
- Term-6 calibration: [`2026-05-03-t6-calibration-and-gs-reducer-perf.md`](2026-05-03-t6-calibration-and-gs-reducer-perf.md)
- NV-1 candidate: [`2026-05-03-nv1-candidate-a-doubleprime-test.md`](2026-05-03-nv1-candidate-a-doubleprime-test.md)
- N_v retraction: [`folio-assistant/computations/n_sym_w2_retraction.py`](../../folio-assistant/computations/n_sym_w2_retraction.py)
- Mass-table benchmark: [`folio-assistant/computations/mass-table-ppb.witness.json`](../../folio-assistant/computations/mass-table-ppb.witness.json)
- β-decay open problems: [`folio-assistant/computations/branching-qvalues.witness.json`](../../folio-assistant/computations/branching-qvalues.witness.json)
- LP/SDP infra: CLAUDE.md "LP / SDP duals — first-class infra (do not skip)" + [`folio-assistant/computations/lp_dual_solver.py`](../../folio-assistant/computations/lp_dual_solver.py) + [`folio-assistant/computations/lp_dual_witness_validator.py`](../../folio-assistant/computations/lp_dual_witness_validator.py)

---

**End of 2026-05-04 deep audit.** No code changes performed by
this audit; this is a *finding* document. Tier-🔴 items WALL-BREACH-NEW
and MASS-WITNESS-DESC are quick mechanical fixes that should be
their own follow-up commits/PRs. Tier-🟠 LP-DUAL-MISSING is also
mechanical. The remaining Tier-🔴 items are research-grade and
already on the workplan.
