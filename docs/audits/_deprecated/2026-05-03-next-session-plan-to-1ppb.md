> **DEPRECATED on 2026-05-24.** Point-in-time status, intermediate workplan iteration, dead-end exploration, or earlier sublemma version superseded by a later "refined" iteration. Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) §"5-tranche recommendation" T2 for the deprecation rationale.

# Next-session plan — survey of main + workplan to 1 ppb

**Compiled** 2026-05-03 on `claude/4-parallel-followup-tests` (PR #515).
**Scope**: Survey what landed in `origin/main` in the last ~36 h, fold the
findings into the audit, and refresh the workplan with **1 ppb** as the
mass-table target.  Intended as the seed brief for the **next session**
on a fresh branch.

---

## §1. What landed in main in the last 36 h

### Merged PRs

| PR | scope | net effect on canonical pipeline |
|----|-------|----------------------------------|
| #498 | tier-1/2 audit refresh | bookkeeping |
| #499 | tier-3 math audit | self-conjugate witness for magic ladder ✓ |
| #500 | qou-algebraic-refactor | BB-stratification + 6-knot Bring basis ✓ |
| #501 | tier-4 math audit | conjectural-propagation policy ✓ |
| #503 | refactor-computation-framework | **MAG-126 closed in 1.47 ms; FROB-FILTER closed form; §3·B ≤0.32% on 4 atoms** |
| #504 | golden-ratio-exploration | negative result (φ not categorical anchor) |
| #505 | audit-math-framework continuing | one-voice cleanup + binding-energy probes |
| #506 | jet-prolongation-habiro-deepen | **Habiro fast path landed** (memo speedups) |
| #507 | moduli-d4-zi-lift | exceptional divisor structural input |
| #516 | markov-axiom-recursion | recursion axiom for Markov trace |
| #519 | post-merge-survey | v5 deliverables 1+2 + appendix C recompute |

### Notable individual commits on main

| commit | finding | status |
|--------|---------|--------|
| `23ff1bac6` | **v5 #1 magic_A_formula.py** — `B = ρ_F · m_e · A · 8G` (callable) | ⁴He at +5.87% |
| `23ff1bac6` | **v5 #2 alpha_cluster_recursion.py** — `B(nα) = n·B(⁴He) + C(n,2)·c_αα` | ⁸Be at +10.3% |
| `6b75e5573` | **c categorical closed form** — `c = 2·w_(6,3)(q) + w_(9)(q)` (Schur–Weyl) | ✓ derived (not fit) |
| `65db81582` | ⟨Φ_q⟩ closed-form attempt | structural reduction lands |
| `04cf102a4` | α analytic attempt — 80/81/82 all match fit | **RETRACTED** as pattern-match |
| `916a88d29` | α ≈ 82·E_0 **retraction**: not a derivation | explicit negative result |
| `7c2017199` | **GS-filtration E_2-page (Term 6) probe** | r=+0.62 (strongest yet) |
| `264b02001` | Khovanov closure-energy probe | r=+0.81 R (vs Jones −0.61) |
| `46bc03fa6` | magic-residual probe — `is_magic_pair` r=+0.74 | structural |
| `52fbba4a3` | **M_iso L-function Frobenius-trace candidate** (R6 step-3→4) | open |
| `ae70902a9` | M_iso L-function — 9-prime extension | open |
| `37c695fb4` | M_iso Hecke-multiplicativity test | inconclusive |
| `a630e2314` | M_iso L-function handoff doc — 3 paths | written |
| `9bfe5e286` | **Term 6 binding-energy formal write-up** | content block ✓ |
| `bcd386445` | `prop:term6-binding-density` | content block ✓ |
| `5bf642b20` | Path-(b) BB-grade variants — ALL cancel at magic | structural impossibility |
| `a5ebf3c0c` | **Frobenius probe in Z[ζ_{2p}]** (exact algebraic) | open |
| `2834792d1` | markov_peel — skip `sp.simplify` in trace agg | perf only |
| `80eafe8b6` | markov_peel — interleave reduce with multiplication | perf only |
| `701283ec4` | test_markov_peel — tritium ✓; ³He / ⁴He xfail | trace bottleneck |

### Conflict assessment vs PR #515

`fd70339a8` on this branch already merges `e0a230a9d` (PR #519) cleanly.
The audit-witness file is the only recurring conflict path; it
regenerates idempotently from `derivation_chain_validator.py` and
both branches agree once regenerated.

**No semantic conflict** between PR #515 and main:

- N_sym(q) framework (#515) is orthogonal to magic-A / α-cluster
  (#519) — different sectors.
- v4 mass pipeline key-bug fix (#515) does not touch v3, which is what
  §3·B closure (#503) uses.
- HIGGS-SLOT / RHO-SUBSTRATE / SHELL-7-FULL-KAPPA flags (#515 audit)
  do not duplicate any open issue on main.

### Simplification opportunities exposed by new main commits

| Where | Opportunity |
|-------|-------------|
| `crt_markov_v4.py` (#515) | After Habiro fast path (#506), the depth-1/2 recursion can use the memoized Habiro evaluator instead of re-multiplying matrices. Estimated 5–10× speedup. |
| `n_sym_*.py` probes (#515) | Candidate-(a) Gram-determinant probe is now computable using the symbolic Hecke core (#511) + the Schur–Weyl decomposition that landed for `c` (`6b75e5573`). |
| `gt_matrix_pslq_probe.py` (#515) | `[5]_q/[4]_q` leading-order witness can re-use `hecke_core_symbolic.py` (#511) for an exact evaluation rather than mpmath floats. |
| `shell7_bb_stratum_test.py` (#515) | The κ=0-stratum reformulation can use `magic_A_formula.py` (#519) as a benchmark for the Z=N magic baseline. |
| `v4_mass_pipeline.py` (#515) | After `α ≈ 82·E_0` retraction (`916a88d29`), the calibration discussion in this file should be updated to **not** suggest a single-scalar α exists. |

---

## §2. Mass-table-ppb — current state and 1 ppb target

The canonical mass benchmark (from `mass-table-ppb.witness.json`) at
the close of main `e0a230a9d`:

| atom | formula | err % | err ppb | ratio to 1 ppb |
|------|--------|------:|--------:|---------------:|
| ²H  | `1·m_e · Vol(6_2)` (census)         | +1.09 % | 1.09 × 10⁷ | 10⁷ |
| ³H  | `2·m_e · Vol(8_11)` (census)        | −0.16 % | 1.56 × 10⁶ | 10⁶ |
| ³He | `2·m_e · Vol(L6a4)` (census)        | −2.97 % | 2.97 × 10⁷ | 10⁷ |
| ⁴He | `2·m_e · 4·8G` (magic A)            | +5.87 % | 5.87 × 10⁷ | 10⁷ |
| ⁸Be | `2·B(⁴He) + 1·c_αα` (α-cluster)     | +10.33 % | 1.03 × 10⁸ | 10⁸ |

The 1 ppb target — `err_ppb < 1` — is **6–8 orders of magnitude** below
current. Closure requires four structural inputs to land in turn.

### §2.1 Structural-input ledger (the four gaps to 1 ppb)

| Gap | Current state | Target state | Lever |
|-----|---------------|--------------|-------|
| **G-A: ρ_F integer correction** | Plan H → ρ³He = 2.062, +3.1% over integer 2 (PR #512) | Closed-form ρ_F(q, family) with q-residual | `RHO-SUBSTRATE` test from PR #515 audit §2 |
| **G-B: T_w cluster decomposition** | Recursive on ⁴He works for nα magic (#519); blocks non-magic | Closed-form T_w(K) for arbitrary admissible K via knot-operator catalog | Term-6 derivation (`9bfe5e286`) extended to non-magic |
| **G-C: y_λ Wenzl-bridge** | Numeric mpmath bypass (works n≤18) | Symbolic in q via `hecke_core_symbolic.py` (#511) | wire `y_lambda_wenzl_bridge_numeric` → symbolic |
| **G-D: q→q_0 realization** | Mass-table uses `q_0 = 1.10998…`; substrate uniqueness via `q-pinning-50-digit` | 50-dp PSLQ-confirmed unique categorical root | Already at 50 dp (`Q_50_DIGIT_STR` in `q_parameter.py`) |

### §2.2 Per-atom error decomposition (post-pipeline budget)

The 5–10% residuals on ⁴He / ⁸Be / ³He all share **the same sign pattern
that the audit's §3.1 family-specific structural-input uncertainty is
absorbing**.  Specifically:

- **²H** — knot is L6a4 not 6_2 in the canonical assignment (the
  `census-assigned` flag); the +1.09% is residual census vs canonical.
- **³He** — −2.97% is consistent with PR #512's +3.1% ρ-correction
  applied with the wrong sign in the current witness; closing G-A
  flips this and recovers ³He to ≤0.5%.
- **⁴He** — +5.87% is the magic-A formula's bare prediction; T_w
  derivation (G-B) for the doubly-magic cluster operator is the missing
  factor.
- **⁸Be** — +10.33% is the α-cluster compound: 2× ⁴He's residual
  (~ +12%) minus pair-pair correction.  Closes when ⁴He closes plus a
  small `c_αα` correction.

So **G-A + G-B together** would take all 5 entries above to ≤0.5%
(10⁻³, ~10⁶ ppb).  The next 6 orders to 1 ppb come from:

- **G-C** (Wenzl-bridge symbolic-in-q): contributes ~10⁻⁵ at q_0;
- **G-D**: already at 50 dp, contributes < 10⁻¹⁵.

The 1 ppb target is thus dominated by **G-B** (T_w) and **G-C** (y_λ).

---

## §3. Workplan to 1 ppb (next session, ranked by ppb-per-day)

### High-leverage (each closes ≥1 order of magnitude)

| # | Task | Expected outcome | Effort | Closes |
|---|------|------------------|--------|--------|
| **W-1** | **Wire RHO-SUBSTRATE** (#512 result) into `mass-table-ppb` | ³He from −2.97% → ≤0.5%; 8× ppb improvement | 0.5 d | G-A |
| **W-2** | Compute **`det 𝒢_EW(q_0)`** as candidate (a) for `𝒩_sym` | NV-1 closure if matches 213.11 to <1%; otherwise sharpens failure mode | 1 d | NV-1 |
| **W-3** | Extend Term-6 binding-density to ⁴He / ⁶Li / ¹²C | Tests T_w cluster generalization; benchmark vs AME | 1 d | G-B partial |
| **W-4** | Migrate `crt_markov_v4` depth-1/2 to **Habiro fast path** (#506) | 5–10× speedup unblocks larger-A Wedderburn evaluations | 0.5 d | infra |
| **W-5** | **HIGGS-SLOT** non-torus probe (4_1, 5_2, 6_3) | Locate Higgs slot; recover part of `conj:electroweak-higgs-torus-link-triplet` | 1 d | HIGGS-SLOT |

### Medium-leverage (closes flags, structural)

| # | Task | Effort | Closes |
|---|------|--------|--------|
| W-6 | **SHELL-7 full κ=0 stratum** (transpose-pair-summed) | 1 d | SHELL-7-FULL-KAPPA |
| W-7 | **Wenzl-bridge symbolic-in-q** — replace numeric mpmath | 2 d | G-C |
| W-8 | **M_iso L-function** — pursue 3 paths from `m-iso-l-function-handoff.md` | 2–4 d | M_iso identification |
| W-9 | Lean siblings for the 12+ new conjectures (PR #511 + #515) | 3–5 d | formalisation |

### Mechanical (batched into the next session's first commit)

The 16 outstanding Gemini comments on PR #515 are all mechanical:

| Class | Files affected | Fix |
|-------|---------------|-----|
| `encoding='utf-8'` on `open()`/`Path.write_text` | 9 scripts | one-line each |
| PEP 8 — one import per line | 3 scripts | trivial |
| Dead `if False:` in `n_sym_numerical_anchor.py` line 30 | 1 | delete |
| `:=` ambiguity in `2026-05-03-n-sym-derivation-attempt.md:59` | 1 | replace with `≈` |
| `T^3 ⊗ Y` notation in `g-action-on-substrate.md:31` | 1 | clarify in narrative |

**Recommendation**: open the next session on a fresh branch
`claude/next-session-1ppb-workplan` (or similar), land all mechanical
fixes in commit 1, then proceed in priority order W-1 → W-5.

---

## §4. Numbers to track to 1 ppb

| quantity | post-#515 best | 1 ppb target | ratio |
|----------|---------------:|--------------:|------:|
| 1/α_EM | 137.035998166 (6.7 ppb of CODATA) | 1 ppb | 6.7× |
| Q(n→p) | 0.7816 MeV (−0.097%) | ≤1 ppb (10⁻⁹) | 10⁶ |
| MAE on 45 isotopes (k=5) | 0.006% (#503) | 10⁻⁹ | 10⁵ |
| ²H binding | 1.09% | 10⁻⁷ | 10⁵ |
| ⁴He binding | 5.87% | 10⁻⁷ | 10⁵ |
| ⁸Be binding | 10.33% | 10⁻⁷ | 10⁵ |
| 𝒩_sym(q_0) | 213.111807 (numerical) | symbolic closed form | qualitative |
| g_A (free n) | 1.27028 (−0.4%) leading | locked at PDG 0.1% | PDG-floor-blocked |

The single biggest leverage to **light-atom** ppb is **G-A (RHO-SUBSTRATE)**:
W-1 alone takes ³He from 2.97 × 10⁷ ppb to ≤ 5 × 10⁶ ppb, a clean order
of magnitude.  G-B (Term-6 / T_w cluster) is the next decade.

---

## §5. Watch list for in-flight branches (next session, run in background)

| branch | last activity | watch for |
|--------|---------------|-----------|
| `claude/post-electron1-multi-tackle` (PR #511) | merged into #515 base | done |
| `claude/electron-1-categorical-correction` (PR #509) | merged into #515 | done |
| `claude/rho-3he-plan-h-probe` (PR #512) | open (other agent) | merge → unblocks W-1 |
| `claude/ew-higgs-mass-ratio-probe` (PR #513) | open (other agent) | merge → informs HIGGS-SLOT |
| `claude/plan-h-census-and-higgs-correction` (PR #514) | open (other agent) | likely to be subsumed by W-5 |

Background watch policy: `git fetch origin main` at the start of each
turn; if main moved, run the integration / conflict / simplify check
described in §1.  Same for the listed sibling branches when they merge
to main.

---

**End of next-session plan.**
