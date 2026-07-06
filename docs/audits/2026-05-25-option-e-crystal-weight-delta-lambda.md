# 2026-05-25 — Option E: Kashiwara crystal weight → Δ_λ(K) closure

## TL;DR

Single-session probes (1, 2, 3, 4) have mapped the Δ_λ(K) landscape but cannot close it without categorical input. **Option E** proposes that the framework's canonical Δ_λ(K) is determined by the **Kashiwara crystal weight** of the partition λ at the atomic braid word β_K:

$$
  \Delta_\lambda(K) \;=\; \sum_{w \in \mathcal{B}_\lambda(\mathcal{B}_K)} n^w_\lambda \cdot \rho_w(K)
$$

where:
- $\mathcal{B}_\lambda(\mathcal{B}_K)$ — crystal vertices in the Wedderburn-$\lambda$ block reachable from $\mathcal{B}_K$ in the crystal graph;
- $n^w_\lambda$ — Kazhdan–Lusztig multiplicities (integer);
- $\rho_w(K)$ — canonical-basis trace at crystal vertex $w$, evaluated at q_0.

The conjecture is open: `conj:crystal-graph-realization` + `conj:kazhdan-lusztig-classical-limit`.

This branch (`claude/kashiwara-crystal-option-e-scaffolding-2026-05-25`) is the **scaffolding** — Lean stubs + audit framing + infrastructure planning. **Not** the closure proof; that's weeks-scale work.

## Why now

Probes 1+3+4 ([PR #1229](https://github.com/litlfred/qou/pull/1229), **merged 2026-05-25**) mapped the per-atom Δ_λ(K) landscape:

| atom | A | dominant λ*(K) | shape | max |Δ_λ(K)| |
|------|---|---------------|-------|---:|
| D    | 2 | (2,1,1,1,1)    | hook (transpose of (5,1)) | 15.7 |
| T    | 3 | (2,2,2,1,1,1)  | (transpose of (6,3))      | 212.9 |
| ³He  | 3 | (2,2,2,1,1,1)  | (transpose of (6,3))      | 104.6 |
| ⁴He* | 4 | (9,3)          | two-row                   | 1573 (truncated) |

**T and ³He share dominant λ*** = (2,2,2,1,1,1) — a structural fingerprint of the A=3 family. **D's dominant** = (2,1,1,1,1) is the hook. These are **categorical patterns** that the crystal-weight hypothesis must predict.

Probe-2 (joint multi-atom) falsified the counter-framework "global Δ_λ" hypothesis (max |Δ| = 431.7 across atoms). The framework's K-dependence is canonical; Option E provides the categorical mechanism.

## What exists (survey 2026-05-25)

| Component | Location | State | Option E need |
|---|---|---|---|
| Δ_λ(K) formula | [`rho-k-h3a-refinement.lean`](../../content/quantum-observable-universe/braids-and-knots/rho-k-h3a-refinement.lean) L49-66 | ✓ defined as `class RhoKH3ARefinement` axiomatising identity | crystal-weight instantiation |
| Crystal graph | [`crystal-graph-realization.md`](../../content/quantum-observable-universe/braids-and-knots/crystal-graph-realization.md) | ✓ conjecture, empirically verified | Lean formalisation |
| KL classical limit | [`kazhdan-lusztig-classical-limit.md`](../../content/quantum-observable-universe/archimedean-universe/kazhdan-lusztig-classical-limit.md) | ✓ conjecture, unproven | Lean classical limit theorem |
| KL canonical basis at q=1 | [`lusztig-canonical-basis-q-eq-1.lean`](../../content/quantum-observable-universe/braids-and-knots/lusztig-canonical-basis-q-eq-1.lean) | ✓ Lean stub | extend to q ≠ 1 |
| Kashiwara Jones c_4 | [`kashiwara-jones-c4-categorical.lean`](../../content/quantum-observable-universe/braids-and-knots/kashiwara-jones-c4-categorical.lean) | ✓ Lean stub | extend to general level |
| Crystal-basis path | [`crystal-bases-path-a.md`](../../content/quantum-observable-universe/braids-and-knots/crystal-bases-path-a.md) | ✓ computational path | tie to Δ_λ(K) extraction |
| Crystal vertex enumeration | [`crystal-basis-resolves-mass-tower-open-problems.lean`](../../content/quantum-observable-universe/archimedean-universe/crystal-basis-resolves-mass-tower-open-problems.lean) L70-94 | ✓ finite graph traversal stub | extend to per-atom Δ_λ |
| Frobenius Gram matrix | [`gram-matrix-dual.py`](../../computations/gram-matrix-dual.py) (pyhecke) | ✓ computed (numpy 6×6) | Lean formalisation |
| Frobenius Gram matrix (Lean, content-block sibling) | [`particle-interactions/gram-matrix-h3-symbolic.lean`](../../content/quantum-observable-universe/particle-interactions/gram-matrix-h3-symbolic.lean) | ✓ **landed on main** — full symbolic 6×6, all 21 upper-triangle entries as Laurent polynomials in `u = √q`, sympy-computed, verified to 1e-16 against `gram-matrix-dual.witness.json` at q_0 | wiring to `gram_matrix q = 0` stub is the only remaining sub-task (see row below) |
| Frobenius Gram matrix (Lake-built production) | [`lean/QOU/Archimedean/frobenius_gram_matrix.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/frobenius_gram_matrix.lean) | ✓ **landed on main** — full 6×6 over generic ring `R` (AGENTS.md §7c compliant), with explicit Hoefsmit-seminormal entries `g₁₅, g₃₄, g₃₅, g₅₅` and symmetry/positivity theorems | use directly in Phase 2 |
| Wire `gram_matrix q = 0` stub | [`universal-ilp-algorithm.lean`](../../content/quantum-observable-universe/particle-interactions/universal-ilp-algorithm.lean) L28-29 | ✗ still `= 0`; the production `gram_matrix` lives in `frobenius_gram_matrix.lean` so this content-block stub is mostly cosmetic | low-priority wiring; not blocking Phase 2 |
| `gram_matrix(q)` PyO3 | [`pyhecke-native/src/lib.rs`](../../tools/pyhecke-native/src/lib.rs) | ✓ hardwired to H_3 (6×6) | generalise to H_n |
| `gram_inverse(q)` PyO3 | [`pyhecke-native/src/lib.rs`](../../tools/pyhecke-native/src/lib.rs) | ✓ hardwired to H_3 | generalise to H_n |
| `chi_lambda_braid(shape, word, q)` PyO3 | [`pyhecke-native/src/lib.rs`](../../tools/pyhecke-native/src/lib.rs) | ✓ n-strand (f64) | mpfr variant for substrate precision |
| Per-atom χ caches | `computations/chi-{D,T,³He,⁴He}-h{n}-at-q0-50dps.witness.json` | ✓ D, T, ³He complete | use directly for Phase 2 |
| ⁴He full 77-partition χ table | [`chi-lambda-he4-full-partition-table.witness.json`](../../computations/chi-lambda-he4-full-partition-table.witness.json) | ✓ landed on main (`30d5f19a1`, 2026-05-25) | re-run probe-4 ⁴He with full table |
| Jones-Markov atlas (general H_n y_λ) | [`jones-markov-atlas`](../../computations/) | ✓ landed on main (`814a7545b`, 2026-05-25); generic H_n y_λ solver via cycle-type Schur-orthogonality; verified Σ y_λ · dim_λ = 1 for A ≤ 4 | reuse for Phase 2 Wedderburn projection |
| H_4 Wedderburn atlas + H_3 vs H_{3A} legacy bug audit | [`c70707397`](https://github.com/litlfred/qou/commit/c70707397) (2026-05-24) | ✓ landed on main; bug is root cause of the 5.87% ⁴He gap | Phase 1 must NOT inherit the H_3-vs-H_{3A} legacy |
| pyhecke-native multi-block χ_λ | [`8bb47b448`](https://github.com/litlfred/qou/commit/8bb47b448) (2026-05-25) | ✓ FIRST multi-block χ_λ measurement via tier-3 wiring | reuse for Phase 1 instead of authoring `chi_lambda_eval.py` from scratch |
| pyhecke M3 public API | [`134c04fe5`](https://github.com/litlfred/qou/commit/134c04fe5) (2026-05-25) | ✓ atom/molecular/constants lazy-loaded | Phase 1 wrapper imports from public API |
| Crystal vertex weights ρ_w | (NOT EXIST) | ✗ no Lean / pyhecke implementation | **author this in Phase 1** |

## Workplan (weeks-scale, NOT this session)

This branch ships ONLY the scaffolding + framing. Full Option E is multi-PR over weeks.

### Phase 0 — scaffolding (this session, this branch)

- [x] Audit doc framing (this file)
- [ ] `kashiwara-crystal-delta-lambda.ts/md/lean` — conjecture block stating the crystal-weight formula for Δ_λ(K)
- [ ] PR opened for visibility + coordination

### Phase 1 — categorical infrastructure (follow-on PRs)

**Status update (2026-05-30, PR #1509 retrospective).** A misdirected
attempt at the first Phase 1 item revealed that the symbolic
Hoefsmit-seminormal 6×6 Gram matrix is **already done in main**, in
two independent forms:

  * [`particle-interactions/gram-matrix-h3-symbolic.lean`](../../content/quantum-observable-universe/particle-interactions/gram-matrix-h3-symbolic.lean)
    — full 21-entry symbolic matrix in `u = √q`, content-block sibling.
  * [`lean/QOU/Archimedean/frobenius_gram_matrix.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/frobenius_gram_matrix.lean)
    — full 6×6 over generic ring `R`, Lake-built production formalisation.

The first checkbox in this section ("Replace `gram_matrix q = 0`
stub") is therefore re-scoped from "implement the matrix" to "wire
the existing matrix into the content-block sibling" — a low-priority
cosmetic change since `frobenius_gram_matrix.lean` is already the
production form. Crossed out below.

**H_3 vs H_n=6 scope note.** Both existing Gram matrices are for
H_3(q). The deuteron mass formula requires H_6(q) and the larger
atomic nuclei H_n for n ≥ 9. Phase 1 still needs the **general H_n
Gram matrix** generalisation (next checkbox below); the H_3 case is
the entry-point sanity check.

- [x] ~~Replace `gram_matrix q = 0` stub in [`universal-ilp-algorithm.lean`](../../content/quantum-observable-universe/particle-interactions/universal-ilp-algorithm.lean) with computed Hoefsmit-seminormal 6×6 entries~~ **already done in `gram-matrix-h3-symbolic.lean` + `frobenius_gram_matrix.lean`**; the stub wiring is a separate cosmetic follow-up.
- [ ] **Generalise the H_3 Gram matrix to H_n for n ≥ 4** — required for the deuteron (H_6) and larger atomic nuclei. The existing 21-entry symbolic 6×6 does not lift directly; the Hoefsmit-seminormal closed form for `tr_M(b_i · b_j)` at general n is the actual Phase 1 deliverable.
- [ ] Formalise the canonical-basis trace ρ_w in Lean (extend [`lusztig-canonical-basis-q-eq-1.lean`](../../content/quantum-observable-universe/braids-and-knots/lusztig-canonical-basis-q-eq-1.lean) to q ≠ 1)
- [ ] Build a Lean enumerator for crystal vertices at level n=6 (deuteron weight)
- [ ] **Reuse**: Jones-Markov atlas (`814a7545b`) provides generic H_n y_λ solver — extends pyhecke-native's hardwired H_3 case. **No need to author from scratch**; reuse + cite.
- [ ] Generalise `gram_matrix(q)` / `gram_inverse(q)` in pyhecke-native from hardwired H_3 to general H_n (still open after `814a7545b`; atlas covers y_λ but not the basis matrix)
- [ ] **Reuse**: pyhecke-native multi-block χ_λ tier-3 wiring (`8bb47b448`) supersedes the `chi_lambda_eval.py` wrapper plan — direct PyO3 import from the lazy-loaded M3 API (`134c04fe5`).

#### Phase 1' design note — H_n Gram generalisation (2026-05-30)

**New primitive available** (commit `6964850fe`,
`sprint3-4(iwahori): TypeA + MarkovTrace`):
[`lean/QOU/IwahoriHecke/TypeA.lean`](../../content/quantum-observable-universe/lean/QOU/IwahoriHecke/TypeA.lean)
defines `IwahoriHeckeOfSn R q n` over generic `[Field R]`, which
is the right ambient type for an abstract H_n Gram matrix.

**Hardcoded entries do not scale.** The H_3 case has `3! = 6`
basis elements and `21` distinct upper-triangle Gram entries; this
is hand-tractable. At H_6 (deuteron) the count jumps to `6! = 720`
basis elements with `720·721/2 = 259 560` distinct entries — far
beyond hand-symbolic encoding. The Phase 1' deliverable therefore
must **compute** `G_{ij} = tr_M(b_i^* · b_j)` from primitives,
not list entries.

**Recommended Phase 1' design:**

1. Extend
   [`braids-and-knots/markov-axioms-primitive.lean`](../../content/quantum-observable-universe/braids-and-knots/markov-axioms-primitive.lean)'s
   `MarkovTraceAxioms` class to a uniform family
   `MarkovTraceHn (R : Type*) [Field R] (n : ℕ) (q : R)` providing
   `trM : IwahoriHeckeOfSn R q n → R` satisfying M1–M4.
2. Author
   `lean/QOU/IwahoriHecke/GramMatrix.lean` with
   `noncomputable def gramHn (R) [Field R] (n : ℕ) (q : R)
     (b : Fin n.factorial → IwahoriHeckeOfSn R q n) :
     Matrix (Fin n.factorial) (Fin n.factorial) R`
   defined as `Matrix.of (fun i j => trM (bar (b i) * b j))`.
3. Prove abstract structural properties at the `gramHn` level:
   `gramHn_isSymm` (symmetric), `gramHn_pos_semidefinite_at_q_pos`
   (positivity for `q > 0` from M3 stability), etc. These are
   independent of `n` and reusable.
4. Specialise to `H_3` and verify the result matches the existing
   `gram-matrix-h3-symbolic.lean` entries — closes the loop on the
   "already done at H_3" finding without re-encoding the 21
   entries.
5. Specialise to `H_6` and feed into Phase 2 crystal-weight
   tabulation `ρ_w(D) = (gramH6_inv u) · χ^•(D)`.

**Scope estimate.** Items 1–3 are the abstract scaffolding pass:
typeclass design + structural theorems, no per-entry symbolic
work. ~1-2 sessions of focused Lean work. Items 4–5 (specialisation
+ verification) are Phase 2 deliverables that depend on item 3
landing.

**Anti-pattern.** Do NOT author a separate per-`n` hardcoded entry
table (e.g., `gram-matrix-h6-symbolic.lean` mirroring
`gram-matrix-h3-symbolic.lean`). That pattern stalled at H_3 for a
reason — the entry count grows super-exponentially. The abstract
`gramHn` over the Iwahori-Hecke primitive is the only scalable
design.

### Phase 2 — crystal-weight formula verification (research-grade)

- [x] ~~Tabulate canonical-basis-trace ρ_w(K) for K ∈ {D, T, ³He, ⁴He}~~ **(partial, w = w_0 only)**: H_6 ρ_λ(w_0) diagonal per partition landed via PR #1697 + #1516 (`probe-option-e-h6-entry-point.witness.json`).  Multi-vertex enumeration (w ≠ w_0) blocked on `kazhdan_lusztig.py` n ≤ 4 cap.
- [ ] Identify the Brundan–Kleshchev image of each crystal vertex w in the KLR algebra R^Λ_α
- [ ] ~~Verify Δ_λ(D) = Σ_w n^w_λ · ρ_w(D) against probe-1's empirical D solution from `delta-lambda-bar-invariance-probe.witness.json` (PR #1229 merged)~~ **single-vertex (w = w_0) shortcut REFUTED — see PROBE 4 cheap-pass verdict below**
- [ ] Extend to T, ³He, ⁴He using the full atomic χ caches; cross-check shape patterns
- [ ] **⁴He upgrade**: re-run the per-atom sweep (probe-4 logic) with the full 77-partition `chi-lambda-he4-full-partition-table.witness.json` (now on main) — supersedes probe-4's provisional 24/77 truncation

#### PROBE 4 cheap-pass verdict (2026-06-02, PR #1516)

**Upstream context.** [`rho_w_crystal_vertex_trace.py`](../../computations/rho_w_crystal_vertex_trace.py)
(on main; design doc [`2026-05-31-rho-w-crystal-vertex-trace-design.md`](2026-05-31-rho-w-crystal-vertex-trace-design.md)) already established the genuine
per-vertex ρ_w := ⟨v_T|ρ_λ(β_K)|v_T⟩ via Hoefsmit/Young seminormal,
and showed that the regular-multiplicity sum `Σ_w ρ_w(K) = χ^λ(β_K)`
(trace identity) does **not close** the deuteron
(`closure_status: does_not_close`).

This PR's PROBE 4 cheap-pass is **orthogonal scope**: tests four
ad-hoc closed-form variants of Δ_λ that are NOT the regular-
multiplicity Σ_w ρ_w. Following PR #1709's "cheap proxy first"
strategy.  **All four candidates refuted (miss ≥ 66%):**

| Candidate                       | S_candidate | rel_err |
|---------------------------------|-------------|---------|
| A: χ^λ(w_0)                     | −0.0074     | 99.83%  |
| B: \|χ^λ(w_0)\|                 | +0.9024     | 120.73% |
| C: sgn(χ^λ(w_0)) · dim_λ        | −1.4596     |  66.47% |
| D: max-abs ρ_λ(w_0) diag        | +0.7600     | 117.46% |

Target_signed = −4.35337 per `delta-lambda-empirical-tabulation.witness.json`.

**Combined implication.**  With `rho_w_crystal_vertex_trace.py`
(regular-multiplicity sum, refuted) AND this probe (four ad-hoc
closed-form variants, all refuted), the Kashiwara/KL approach
cannot close Δ_λ via any single-vertex or trivial-multiplicity
shortcut.  The remaining live paths are:

1. **Full Kazhdan-Lusztig multiplicity machinery** with NON-trivial
   `n^w_λ` (KL polynomials, not `n^w_λ = 1`) summed across multiple
   vertices `w` (extend `kazhdan_lusztig.py` past the n ≤ 4 cap to
   S_6, ~hours of recursion-implementation work).
2. **Pivot to GAP-A-3 / GAP-A-4** per AGENTS.md §L2 (categorical
   brane-tower level selection / ρ general rule).

Witness: `probe-option-e-phase2-crystal-vertex-candidates.witness.json`
(PR #1516).  Symmetric refutation to PR #1709's geometric Vol_λ
result — both single-vertex KL shortcuts AND content/hook-angle
Vol_λ proxies fail at deuteron; q-6j saddle (#1709) and full
n^w_λ enumeration (this PR) remain the live in-Option-E directions.

### Phase 3 — closure proof (Lean, research-grade)

- [ ] Prove `theorem delta_lambda_crystal_realisation : Δ_λ(K) = Σ_w n^w_λ · ρ_w(K)` modulo `conj:crystal-graph-realization`
- [ ] Discharge `conj:crystal-graph-realization` via Brundan–Kleshchev + Lecouvey bijection
- [ ] Discharge `conj:kazhdan-lusztig-classical-limit` for the deuteron (and atom family)

### Phase 4 — full per-atom closure

- [ ] Re-run probe-4 with crystal-predicted Δ_λ(K); verify per-atom match to ≤ 1 ppb on target_signed
- [ ] Extend to A=5,6,7 (⁵Li, ⁶Li, ⁷Li wiring GAP); verify B(K) prediction
- [ ] Wire to `mass_table_ppb.py` production path (PR #1228 §10 action #4)

## Coordination (siblings)

| sibling | scope | overlap | action |
|---|---|---|---|
| **#1229** (probes 1-4, this session) | Δ_λ(K) empirical landscape | parent | reference data for Phase 2 |
| **#1224** (synthesis doc) | 14-ansatz audit + 3 probes recommendation | parent | Option E sequence reactivated post-probe-4 |
| **#1228** (vol-density-derivation audit) | §10 action #1 (chi_lambda_eval.py wrapper) + alpha-cluster recursion | dependency | Phase 1 `gram_matrix` generalisation converges with their wrapper |
| **#1127** (Q_β fitting finding) | GAP-A-4 `conj:rho-prefactor-structural` | adjacent | Option E may provide the correct ρ_K form |
| **#1246** (CAL-2 cohomological audit) | substrate q_0 framing | upstream | Phase 3's KL classical limit needs q_0 framing |

Posted intent on all five branches (next commit on this branch).

## Anti-patterns avoided

- Not a 7th fit-based ansatz (per AGENTS.md): the crystal-weight formula is a STRUCTURAL identity derivable from categorical primitives, not an optimisation criterion.
- Not dropping CAL-3 (per `1ppb-compute-tranche-queue.md` invariant).
- Not introducing free per-knot parameters: every quantity (n^w_λ, ρ_w) is derived from the framework's categorical structure.
- Not assuming q_0 specific value: the crystal-weight formula holds over generic R (AGENTS.md §7c); q_0 enters only at the archimedean evaluation step.

## What this PR does NOT do

- Does NOT close Δ_λ(K) — only scaffolds the categorical machinery.
- Does NOT modify any production compute (`mass_table_ppb.py` untouched).
- Does NOT replace `gram_matrix q = 0` stub in this commit — Phase 1 follow-up.
- Does NOT introduce a numerical verification — Phase 2 follow-up.
