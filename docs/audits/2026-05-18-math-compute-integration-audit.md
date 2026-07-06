# Math → compute integration audit (2026-05-18)

> Audit of all mathematical improvements that landed on `origin/main`
> over the last 10 days, with verdicts on whether each one is wired
> into the production compute chain (paper-six-term-isotope-sweep,
> derive_m_p/m_n full-tower, atomic_mass_via_rho_k).
>
> Skill driving this audit:
> [`local/compute-integration-watcher`](../../.claude/skills/local/compute-integration-watcher.md)
> (new — landed alongside this doc).
>
> Sister audit (perf/correctness inside scripts):
> [`local/compute-audit`](../../.claude/skills/local/compute-audit.md).

## 1. Scope

| Layer | Files surveyed | What we checked |
|-------|----------------|-----------------|
| Lean discharges | last-10-day commits under `content/**/*.lean` | did the proof show up? does it have a downstream consumer? |
| New propositions | `prop:flavor-split-substrate`, `prop:hopf-jones-c3-categorical`, `prop:chi-lambda-w0-sign-weighting`, `prop:kashiwara-jones-c4-categorical` | does the production chain use the derived constant? |
| Canonical-form refactors | T2/T3 Faddeev Φ_q → symmetric Li_2^q (PR #687, merged) | did all consumers migrate? |
| Mass-table sweep | `paper_six_term_isotope_sweep.py` | does it run end-to-end? what's the isotope coverage? |
| Active PRs | #683 / #689 / #679 / #690 (#686 / #688 closed) | tractable CI / review issues? |

## 2. Recent mathematical improvements (10-day window)

### 2.1 New propositions formalised on main

| Label | Landed | Status (Lean) | Probe witness | Production consumer | Verdict |
|-------|--------|---------------|---------------|---------------------|---------|
| `prop:flavor-split-substrate` | 601fc96e (`Δm to 0.52%`) + 89162ee7 (per-sheet Bring) | `.lean` exists | `probe-flavor-split-substrate.witness.json` | docstring only @ `derive_m_p_hecke_full_tower_50dps.py:58` | **I2 — PROBE-ONLY** |
| `prop:hopf-jones-c3-categorical` | merged via #672 (#664 follow-ups) | `.lean` exists | `hopf-jones-c3-categorical.witness.json` | `paper_six_term_isotope_sweep.py:972, 989` | **WIRED** ✓ |
| `prop:chi-lambda-w0-sign-weighting` | 636c7dda | `.lean` exists | (none) | (none) | **I1 — PROVEN-IN-LEAN, NO PROBE** |
| `prop:kashiwara-jones-c4-categorical` | #672 series | `.lean` exists | `kashiwara-jones-c4-categorical.witness.json` | `paper_six_term_isotope_sweep.py:990` | **WIRED** ✓ (only the c_4 substitution) |
| `prop:flavor-split-higher-order` (PR #686, **closed**) | superseded | n/a | n/a | n/a | **closed-without-merge** — skip |
| `prop:flavor-split-isobaric-delta-m` (PR #688, **closed**) | superseded | n/a | n/a | n/a | **closed-without-merge** — skip |

### 2.2 Lean discharges (axiom → theorem upgrades)

The following axioms were promoted to theorems on main in the last
10 days:

- `chirality_real` (0c89e8f9)
- `orderOf_perm_dvd_factorial` (4495fc7b)
- `photon_neutrino_requires_T35` (0a3d228d)
- `quarkAntiquarkProduction` (67f7ec30)
- `pp_eigenvalue_ratio_axiom` (74a266e1)
- `qBracket_one`, `qBracket_two`, `hParam_pos` (f774f4e4, 4ab57198, b5cadb55)
- `markovTrace_zero` (213c5fdc)
- Hoefsmit type-arg sorries → 0 (856ef457)
- `vertex-algebra-relations` 4 sorries → 0 (5ec4e963)
- `q-casimir` 6 sorries → 0 (6fabd06b)
- `y-lambda-recipe` + `habiro-expansion` Tier-3 batch (d6e0e550)
- StaircaseEW refinement + MagicShell Pattern A (b5cadb55)

**Wiring impact:** These are Lean-side proof closures; they do not by
themselves introduce a new numerical claim that needs a compute
consumer.  All discharges live inside existing structures whose
compute consumers already exist (Hoefsmit matrices, Markov trace,
q-Casimir).  **No I1–I12 hits triggered.**  Verdict: **green** — Lean
discharges are wired transitively via the existing primitives.

### 2.3 Canonical-form refactors

| Change | Commit / PR | Wiring status |
|--------|-------------|---------------|
| T2/T3 Faddeev Φ_q → symmetric Li_2^q + wire T6 | 32b717ed | **WIRED** ✓ — verified in `derive_m_p_hecke_full_tower_50dps.py:299` (`T2_single_Li2q_50dps`, `T3_pair_Li2q_50dps`) and `paper_six_term_isotope_sweep.py` `tower_mode=li2q` default |
| `compute T2/T3 locally via Li_2^q in derive_m_p/m_n consumers` | 27303e67 (PR #687) | **WIRED** ✓ — explicit comment "T2/T3 computed locally via Li_2^q since the producer (post-2026-05-17 …)" at `derive_m_n_hecke_full_tower_50dps.py:131` |
| Li_2^q helpers centralization | 08070cc4 (PR #687) | **WIRED** ✓ — single source of truth via `derived_masses.li2q_symmetric` |

### 2.4 Numerical results (probe-stage)

- **`Δm = (q-1)²(1-q^{-4})/3` → 0.10 %** (`prop:flavor-split-substrate`).  Backs into the substrate-pure flavor split.  PROBE-only.
- **`prop:flavor-split-substrate` Scheme 4 flavor-weighted: Δm = 1.295 MeV vs CODATA 1.293** (7fdf0d4d).  PROBE-only.
- **Inflection-point `d²A/da² = 0` → m_p to 0.069 %** (f827bb61). PROBE-only.
- **`A·m_avg_C2 − BE(K)` matches CODATA m_K for D, T, ³He; ρ_K substrate-match 0.07 % for nucleons** (fc310726).  PROBE-only (ρ_K consumer still on the LO tautology).
- **MILP with integer knot-operator counts — `a` invariant under ν_SDP choice** (c34fd468). PROBE-only.
- **Multilevel LP at H_3 — same `a = z_markov`** (a60ed4b8). PROBE-only.
- **H_{3A=6} multi-level SDPB — H_6 character pipeline** (8cb6d204). PROBE-only.

**Common pattern:** every one of these is a *probe* that closes a gap
in the m_p / m_n / Δm derivation, but **none has been threaded into
the production six-term mass-formula sweep**.  Most live as
`probe_*.py` siblings that emit a single witness with a `closure_ppm`
or `match_status` field; the canonical sweep does not read them.

## 3. Mass-table sweep pipeline — validation report

### 3.1 Pipeline runs?

`paper_six_term_isotope_sweep.py` ran end-to-end at `HEAD = d24a7787`
after installing `numpy`, `mpmath`, `sympy` into the session container.
(The container's default Python had none of these — flagged as an
environment issue, separate from the script.)

Outputs match the committed witness shape (rows under top-level
`rows`, not under `data`).  Exit code 0.

### 3.2 Coverage

| Atom | T1 source | Six-term run | Status |
|------|-----------|--------------|--------|
| p (¹H) | `atomic-tr-m-mpfr-50dps.witness.json` | M_pred = 28.87 MeV (E_0 = 4.19 MeV brane-legacy mode) | **runs**, err −97 % vs CODATA — calibration not at production scale |
| n (¹n) | same | M_pred = 25.82 MeV | **runs**, err −97 % |
| D (²H) | same | M_pred = 39.60 MeV | **runs**, err −97 % |
| T (³H) | same | M_pred = 46.37 MeV | **runs**, err −98 % |
| ³He | same | M_pred = 107.14 MeV | **runs**, err −96 % |
| ⁴He | fallback (`markov-peel-atomic-tr-m.witness.json` empty as of 2026-05-18) | M_pred = 73.36 MeV | **runs**, err −98 % |
| ⁵Li, ⁶Li, ⁷Li, ⁷Be, ⁸Be, ⁹Be | **partially resolved** (PR #683 merge dc0f9394, 2026-05-18) | Rust χ^λ producer wired in via `canonical_tr_m_via_rust.py`; A=5..9 atom list extension still pending in the producer | **I13** — PR #683 lands the Rust producer (scope: `{p, n, D, T, ³He}` per its PR body); A=5..9 T1 coverage still requires extending the producer's atom list.  `paper-six-term-isotope-sweep.witness.json` on this branch still reports `error_kind: "T1_witness_missing"` for ⁵Li, ⁶Li, ⁷Li, ⁷Be, ⁸Be, ⁹Be on every tower_mode.  4-way 1ppb gate currently covers D / T / ³He / ⁴He (4 atoms); A=5..9 extension is the follow-up. |

### 3.3 Structural test (T − ³He degeneracy)

| Mode | T − ³He predicted | CODATA target | Pass/fail |
|------|-------------------|---------------|-----------|
| brane-legacy | −3 918 465 MeV | +0.019 MeV | fail (calibration broken) |
| drop / q1-base / r-side-bare | −58.49 MeV | +0.019 MeV | structural |
| li2q | −61.38 MeV | +0.019 MeV | structural |
| per-partition-k | −71.19 MeV | +0.019 MeV | structural |
| combined | −71.19 MeV | +0.019 MeV | structural |

The script docstring explicitly says
> "Validates isospin symmetry (T vs ³He degeneracy modulo Coulomb + n-p mass diff)."

The structural test is **failing** at all modes — the isospin
symmetry breaking is ~60–70 MeV where CODATA says ~0.02 MeV
(modulo Coulomb).  Diagnosed in
`brane-tower-isospin-diagnosis.witness.json` (PR #524) as the Φ_q
pole-near-|V̂_i|=1 amplification.

### 3.4 Witness schema observation (I6)

`paper-six-term-isotope-sweep.witness.json` has `"data": {}` at top
level — *the rows live at top-level `rows`*, not under `data`.  This
is benign (consumers parse the right field), but trips simple
introspection scripts that walk `d["data"]["rows"]`.  Flagged as
**I6** in the new skill catalogue.

## 4. Active-PR triage

| PR | Branch | Status | Tractable issues | Recommended action |
|----|--------|--------|------------------|--------------------|
| #690 | `claude/substrate-mp-mn-no-tautology` | open / red CI | Gemini high: `atomic_mass_via_rho_k.py:115` — `c2_inflection` key missing in witness, should be `closest_to_post_hoc.m_p_pred` (one-line schema fix) | post comment, defer commit to PR owner |
| #683 | `claude/canonical-chi-rust` | open / no CI run / `dirty` | Gemini medium (outdated) | rebase first; recheck |
| #689 | `claude/post-670-story-b-mp-c5-c6` | open / red CI / `dirty` | Gemini medium ×2: Rust `hecke_canonical_chi.rs:168` f64 fallback + `:182` `unwrap_or_else` swallows errors | post comment, defer commit to PR owner |
| #679 | `claude/rho-k-wire-li-extend` | open / red CI / `dirty` | no review threads — root-cause CI failure | flag to author for investigation |
| #686 | `claude/flavor-split-higher-order` | **closed without merge** | — | unsubscribed |
| #688 | `claude/multi-nucleon-delta-m` | **closed without merge** | — | unsubscribed |

> **Branch-discipline note.** All four still-open PRs are on
> non-`claude/audit-math-compute-gRube` branches.  Per AGENTS.md and
> the per-session branch directive, this audit does **not** push
> fixes directly to them; it surfaces them for the author or each
> PR's owning agent to address.

## 5. Wiring gaps — concrete TODOs

Ranked by leverage × tractability:

1. **I2 — wire `prop:flavor-split-substrate` into the mass-table sweep.**
   - **Why:** the substrate-pure Δm formula closes to 0.10 % / 0.52 %
     on CODATA's m_n − m_p, AND it removes the implicit dependence on
     the fitted (μ_d − μ_u) input that
     `lem:nucleon-mass-splitting` carries.
   - **How:** read `probe-flavor-split-substrate.witness.json` from
     `paper_six_term_isotope_sweep.py`, use the substrate Δm as the
     primary isospin-breaking input, anchor m_avg to the CODATA
     nucleon average.  Flag the legacy CODATA m_n / m_p inputs with
     `_VALIDATION` suffix per the existing convention.
   - **Effort:** ~1 hour; cross-check against current witness rows
     for p / n / D / T / ³He / ⁴He.
   - **Verifies:** I2 fix recipe in the new skill.

2. **I1 — write probe for `prop:chi-lambda-w0-sign-weighting`.**
   - **Why:** the (1, 0, −1) sign pattern at the long element `w_0`
     fixes the sign of the c_5 and c_6 difference at H_3.  Currently
     the proof is Lean-only; no compute witness exists.
   - **How:** new script `probe_chi_lambda_w0_sign_weighting.py` reads
     `per-wedderburn-block-ck.witness.json`, computes
     `S_k^{(w_0)} = c_k^{(3)} − c_k^{(1,1,1)}`, asserts sign-agreement
     with the empirical `c_k` for k ∈ {5, 6}.  No magnitude claim
     (still open — see the prop's `.md` § "Open: magnitude closure").
   - **Effort:** ~30 min.
   - **Verifies:** I1 fix recipe in the new skill.

3. **I5 — fix `prop:atomic-mass-via-rho-k` missing-block.**
   - **Why:** `atomic_mass_via_rho_k.py`'s `contentBlock` field
     references a label that has no `.ts` / `.md` file.  This breaks
     the derivation-chain audit and produces an orphan witness.
   - **How:** repoint `contentBlock` to `prop:rho-k-h3a-refinement`
     (the canonical neighbour) **or** create a new short remark block
     wrapping the tautological LO formula `M(K) = ρ_K · m_e · |tr_M(K)|`.
   - **Effort:** ~30 min.
   - **Original surface:** 2026-05-16 mass-table-downstream audit.

4. **I5 — extend T1 source to A=5..9 atoms.**
   - **Why:** `paper_six_term_isotope_sweep` fails with KeyError for
     ⁵Li / ⁶Li / ⁷Li / ⁷Be / ⁸Be / ⁹Be.  PR #683 promises Rust χ^λ
     coverage at A=7..8.
   - **How:** wait for #683 merge; once landed, extend
     `atomic-tr-m-mpfr-50dps.witness.json` (or the Rust producer) to
     cover the missing atoms and re-run the sweep.
   - **Effort:** depends on #683 timeline; the writer side is ready.

5. **I8 audit pass — float64 leaks in `q_parameter.Q`.**
   - Per the existing `compute-audit-scan` P30 list, `hecke_core.z`
     and `hecke_core.h` are float64.  Paper-six-term lifts them with
     `mp.mpf(str(z_mark))` (good), but other consumers may use
     `float(z_mark)` directly.  Sweep needed.
   - **Effort:** ~1 hour grep + targeted patches.

6. **I11 — cross-paper `uses[]` not consumed.**
   - Sweep `content/**/*.ts` for `uses: […, "<paper-dir>:<label>", …]`
     entries and confirm the cited upstream witness is actually
     loaded by some local compute consumer.
   - **Effort:** unscoped — run the new skill's idle-sweep mode.

## 6. Recommended next steps (for the repo owner)

Numbered for easy reply:

1. Merge this audit + the new `compute-integration-watcher` skill;
   ack the I-pattern catalogue.
2. Approve item 5.1 (`prop:flavor-split-substrate` wiring) — owner
   sign-off on whether the substrate Δm should replace the
   `μ_d − μ_u` input in the production formula.
3. Approve item 5.2 (`prop:chi-lambda-w0-sign-weighting` probe) —
   this is purely additive (a new probe witness), no risk.
4. Sign off on the open-PR triage in §4 (action recommended for
   #690, #683 post-rebase, #689, #679).
5. Decide whether the idle-sweep should run nightly via a CI job
   (`.github/workflows/compute-integration-sweep.yml`).
6. Decide whether to surface the structural T − ³He failure
   (~60 MeV vs 0.02 MeV) as a first-class open question in
   `docs/coordination/1ppb.md`.

## 7. What this audit does NOT do

- Does not commit fixes to sibling-PR branches (#690, #683, #689, #679).
  Per the per-session branch directive (`claude/audit-math-compute-gRube`),
  fixes are surfaced as recommendations only.
- Does not modify protected files (`deploy/google-viewers.txt`,
  `deploy/github-collaborators.txt`, `.github/CODEOWNERS`).
- Does not run the full I1–I12 idle-sweep across all ~80
  `prop:*.ts` blocks — that is the new skill's idle-sweep mode and
  needs a CI runner or a long-running session.  Section 5.6 above
  enumerates this as a backlog item rather than completing it
  inline.

## 8. Addendum — main activity 2026-05-18 (post-audit)

The following landed on `origin/main` after this audit was first
authored.  Each entry resolves or supersedes an audit finding above:

| Commit / PR | Effect on this audit |
|-------------|----------------------|
| **PR #683** (`dc0f9394`, knot-fusion Step 2 + m_p Item A + Items C/Q6) | Partial progress on the I13 ⁵Li..⁹Be coverage gap in §3.2.  Rust χ^λ producer (`canonical_tr_m_via_rust.py`) lands with scope `{p, n, D, T, ³He}` per the PR body; A=5..9 atom list extension is the follow-up.  4-way 1ppb gate currently covers D / T / ³He / ⁴He (4 atoms). |
| `11e0cb56` (Borromean tower wired into m_p chain) | Resolves the ¹H "PROBE-ONLY" status in §2.1.  ¹H now lifts to `derived` via the conjectural Borromean tower formula. |
| **PR #695** (`y-lambda-n18-scaling`) `3d3f3833` | Extends y_λ table coverage from n=12 → n=30; orthogonal to this audit's scope. |
| `df3bfffe` / `dc3a8550` (Scale-gap §11 RESOLUTION via Borromean tower formula at 0.25 ppm) | New result not in the audit; relevant to the m_p production chain.  Did not exist at audit-author time. |
| `fd89a992` / `79548024` (Formalize + prove `conj:lambda-scale-substrate-form`) | New conjecture-class block landed.  Did not exist at audit-author time; potential I1/I2 candidate for a follow-up sweep. |
| **PR #698** (`72b0e5cc`, cite-hygiene) | Tightens `-- Ref:` placement adjacent to 2 sorries; orthogonal. |
| **PR #703** (`260522a6`, generic integration-watcher parent + refactor 3 watchers) | Refactors `compute-integration-watcher.md` (this audit's primary deliverable) into a slim ~218-line child of a generic `integration-watcher` parent.  This audit's `I1`–`I13` finding-name strings (`I1-PROVEN-IN-LEAN-NO-PROBE`, etc.) and the audit doc's I-pattern citations remain valid: the slim child preserves the I1–I13 taxonomy verbatim under Slot D. |

**Net effect on §5 TODOs (ranked by leverage × tractability):**

- Item 4 (extend T1 source to A=5..9 atoms) — **partial** via PR #683 (Rust producer landed with `{p, n, D, T, ³He}` scope); atom-list extension to A=5..9 still pending.
- All other items unchanged.  Item 5.1 (`prop:flavor-split-substrate`
  wiring) is now being delivered by PR #696 (companion to this PR
  #693); the three-phase delivery template documented in the
  refactored compute-integration-watcher Slot E was extracted from
  the PR #696 work.
