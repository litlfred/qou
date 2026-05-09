# Proton 544k ppb defect — `m_e` anomaly audit

**Status:** documentation-only; **no fix applied.**
**Goal:** explain why `proton-mass-50dps.derivation.json` predicts
`m_p = 937.7615 MeV` and propose resolution options without algebraic fitting.

## 1 — The empirical anomaly

```
predicted m_p   = 937.7615319093 MeV   (proton-mass-50dps.derivation.json)
CODATA m_p      = 938.27208816   MeV
m_p − m_e       = 937.7610892100 MeV
predicted − (m_p − m_e) = +443 eV  (i.e. +472 ppb of m_p)
```

The predicted value is **m_p − m_e to within 472 ppb**. Equivalently, the
predicted dimensionless ratio is

```
m_p_Hecke / m_e_Hecke      = 1835.1535397662    (this chain)
CODATA m_p / m_e           = 1836.1526732506
diff                        = 0.9991 ≈ exactly 1.000
```

The Hecke ratio sits at `m_p/m_e − 1` to 3 decimal places.

## 2 — The mechanism: magic literals

`folio-assistant/computations/derivation_chain.py:73-76`:

```python
M_HECKE_PIPELINE_AT_Q0: dict[str, float] = {
    "e": 0.0007783,  # electron, atomic 2-strand braid
    "p": 1.4283,     # proton, T1+T2+T3+T4 mass-endomorphism tower
}
```

These literals are **placeholders** declared by their own docstring: "When the
full-precision 50 dps tower-derivation chain lands these summaries should be
regenerated together with their consumers." Origin: commit `1861df6` /
`03ec39c` (Apr 29 / May 2 2026), described as "rounded summary of the upstream
`proton_mass_tower_derivation.py` output."

`build_proton_mass_50dps_chain.py:62`:

```python
M_P_PRED_MEV = (M_P_HECKE_PIPELINE / M_E_HECKE_PIPELINE) * M_E_MEV_CODATA
            = (1.4283 / 0.0007783) * 0.51099895
            = 937.7615 MeV
```

The "predicted m_p" is **algebraic re-expression of the two literals** — not a
computation from any of the six unified-mass-formula terms.

## 3 — What the literals do NOT come from

### 3.1 Not from `mass_endomorphism.py`
Running the f64 mass-endomorphism tower at q_0 (per-Phase-1 diagnostic
`proton-residual-rootcause.witness.json`):
- m_p_Hecke (f64) = 1,178,995.5254
- m_e_Hecke (f64) = 630.5293
- ratio          = 1869.85

Different by ~6 orders of magnitude in absolute scale. The literals 1.4283 /
0.0007783 are **not** rounded summaries of `mass_endomorphism.py` output.

### 3.2 Not from `mass-formula-6term-mpfr-50dps.witness.json`
Naive sum of six terms for the proton (from
`mass-formula-6term-mpfr-50dps.witness.json`, last refresh 2026-04-29):

| Term | Value | Source |
|------|-------|--------|
| T1 (descended trace `\|tr_M(T_w)\|`) | +1.0653 | dimensionless |
| T2 (single-gen brane Φ_q) | **0.0** | KeyError: A=1 not in brane-tower witness (PR #533: A=1 tower is structurally empty) |
| T3 (pair-gen brane Φ_q) | **0.0** | same |
| T4 (Frobenius co-Casimir, m_e·tr_M(C)) | +1.2761 | MeV (via explicit m_e prefactor) |
| T5 (chirality-BW, a_K · B_bulk) | **−7.7918** | sign and magnitude both anomalous for proton |
| T6 (Habiro residue tail) | +0.6807 | unitless? |
| **naive sum** | **−4.7697** | dimensionally heterogeneous |

The 6-term sum is **dimensionally inconsistent** (T1 dimensionless, T4 in MeV,
T5 in MeV, T2/T3 zero by missing-witness, T6 mixed). It cannot be assembled
into an m_p value without additional structure.

### 3.3 Comparison
| Quantity | Value |
|----------|-------|
| `mass_endomorphism.py` ratio (f64) | **1869.85** (1.83% high) |
| `M_HECKE_PIPELINE_AT_Q0` ratio (placeholder) | **1835.15** (0.054% low; missing exactly +1) |
| 6-term naive sum (50 dps) | **−4.77** (sign-wrong, dimensionally heterogeneous) |
| CODATA m_p/m_e | 1836.15 |

The three numerical paths give different answers. The chain consumes the
**placeholder**, not either real computation.

## 4 — Why this is suspicious (and why a `+1` patch is wrong)

A `+1` correction in the Hecke ratio would make
`(1.4283/0.0007783 + 1)·M_E_MEV ≈ 938.272 MeV ≈ CODATA m_p (within 472 ppb)`.
**This is exactly the algebraic-cancellation-hides-a-fitting pattern.** Three
reasons not to apply it:

1. **No structural justification.** A `+1` in the ratio means "add the
   electron rest mass back to the predicted m_p". For the proton (no bound
   electron) there is no physical reason to do so. Adding `+1` is what one
   would do to match CODATA, not what the framework predicts.

2. **It would break the electron case.** For X = electron itself,
   `(m_e_Hecke / m_e_Hecke + 1) · m_e = 2 m_e`. Wrong.

3. **It hides the real defect.** The literals are placeholders flagged by
   their own author. A `+1` patch would freeze them as canonical values
   instead of regenerating from a real chain.

The empirical observation is a **diagnostic signal**: it says the placeholder
literals were calibrated against `(m_p − m_e)/m_e` rather than `m_p/m_e`,
either by direct numerology (someone tuned them to give 937.76 MeV by mistake)
or by an upstream computation that is itself missing the rest-mass anchor.
Either way, the defect lives upstream of `derivation_chain.py`, not in the
chain step itself.

## 5 — Resolution options (NO fix applied; these are the choices)

### Option A — Honest relabel (immediate, ~1h)
Demote `proton-mass-50dps.derivation.json` predicted-m_p from `DERIVED +
COMPUTATIONAL` to **`PLACEHOLDER`**. Update `M_HECKE_PIPELINE_AT_Q0` docstring
to flag the `m_p/m_e − 1` anomaly explicitly. Add a per-step note that the
chain's "m_p_pred_MeV" is the algebraic expression of two unverified literals,
not a derivation.

- **Pros:** honest about the actual state; agents know not to trust the value;
  no math change.
- **Cons:** does not fix the ppb gap; the chain remains a scaffold.
- **Risk:** none.

### Option B — Recompute m_p from the 6-term witness (real fix, ~1–2 days)
Build a script that consumes `mass-formula-6term-mpfr-50dps.witness.json` and
assembles the six terms into m_p. Required prerequisites:

1. **Unit reconciliation.** Identify the unit of each term (T1 dimensionless,
   T4 MeV, T5 MeV, T6 ?). Apply the right prefactors so they combine
   additively into MeV.
2. **A=1 brane-tower extension.** Extend
   `terms_2_3_atom_per_gen_mpfr_50dps.py` to emit per-generator volumes for
   (Z=1, N=0). PR #533 says A=1 tower is structurally empty — confirm or
   refute the T2=T3=0 assumption.
3. **T5 sign / scale audit.** The proton chirality-BW term is −7.79 MeV;
   for a "none" knot type with `chirality_map["none"] = 1`, this means
   `B_bulk + B_Zdep + B_shell` is negative for the proton. Trace through
   `bw_chirality_isotopes.py`.
4. **T6 unit clarification.** Habiro residue values look dimensionless;
   confirm the residue-to-MeV conversion is applied somewhere.

After 1–4, replace `M_HECKE_PIPELINE_AT_Q0["p"]` and `["e"]` with computed
values; rerun the chain.

- **Pros:** principled; gives a real m_p prediction.
- **Cons:** several open questions (units, A=1 tower, T5 sign); each
  resolution is itself a research step, not a one-line fix.
- **Risk:** intermediate result may be far worse than 544k ppb until each
  layer is sanity-checked.

### Option C — Audit the upstream "summary" claim (~1–2 sessions)
The literals' docstring claims they are "rounded summaries of `proton_mass_
tower_derivation.py` output". They are not. **Either** find the actual
upstream that emitted 1.4283 / 0.0007783 (possibly a deleted branch or a
preprocessing step that scaled by an unknown factor), **or** confirm no such
upstream exists and the literals were hand-typed during a calibration session.

- **Pros:** establishes the truth about provenance before any further math
  work; also resolves the question "where did the +1 anomaly originate".
- **Cons:** archaeology; may be inconclusive.
- **Risk:** finding a missing scaling step would rehabilitate the literals;
  finding nothing confirms hand-tuning to a (probably wrong) target.

### Option D — Combine A + B as a two-PR sequence
Land Option A first as a single-commit PR (relabel + flag, no math). Then
land Option B as a multi-step fix on top of the relabel. This avoids
freezing the placeholder into "DERIVED" status while the principled fix is
in progress.

- **Pros:** unblocks the audit + makes the actual state visible to agents;
  Option B then proceeds against accurate baseline.
- **Cons:** still requires Option B's research work.
- **Risk:** lowest of the four.

### Option E — Defer; treat 544k ppb as known-floor
Document the placeholder behavior in CLAUDE.md and the precision dashboard,
then focus 1ppb work on chains that don't depend on the placeholder
(e.g. T1 / T3 / T2 in the action queue, which improve binding-energy
predictions for A ≥ 2 nuclei without touching `M_HECKE_PIPELINE_AT_Q0`).

- **Pros:** zero risk; preserves momentum on parallel improvements.
- **Cons:** the 544k ppb proton defect remains; structurally limits the
  precision dashboard.
- **Risk:** none.

## 6 — Recommendation

**Option D (A then B)**, in that order. Option A is risk-free and
immediately makes the actual state of the chain auditable. Option B is the
real fix but has open prerequisites that need their own scoping. Option E is
viable as a fallback if Option B's prerequisites turn out to be deeper than
expected.

**Explicitly NOT recommended:** patching the chain with `+1` to algebraically
match CODATA. That would freeze the wrong placeholder into the canonical
chain and disguise the underlying placeholder-vs-derivation gap.

## 7 — Where else this pattern may exist

`grep` for the same `(m_X_Hecke / m_e_Hecke) * M_E_MEV` pattern:

| File:line | Pattern | Affected? |
|-----------|---------|-----------|
| `build_proton_mass_50dps_chain.py:62` | `M_P_PRED_MEV = ...` | **YES** (this audit's target) |
| `proton_mass_tower_derivation.py:249-250` | `m_p_MeV = ratio_p_e * M_E_MEV` | uses f64 mass-endomorphism, gives +1.84% (different defect) |
| `level1_vhat_brane_tower.py:164,177,235` | same pattern | needs audit |
| `markov_convention_parallel.py:160-161` | `to_MeV(m_Hecke, m_e_Hecke)` | needs audit |
| `hbar_vs_q_parametrization.py:181` | `m_p_MeV = (m_p_Hecke / m_e_Hecke) * M_E_MEV` | needs audit |

For each: confirm whether the input Hecke values are derived or
placeholder-magic, and whether the ratio matches CODATA m_p/m_e or
(m_p − m_e)/m_e.

## 8 — Provenance archaeology (post-blame)

A detailed `git log -S` and blob-hash audit of every commit that
mentions `1.4283` was performed after the initial Phase 1.5 audit.
Findings:

### 8.1 Only two commits are real edits

| Commit | Date (UTC) | Stat | What it did |
|--------|-----------|------|-------------|
| **`1861df6`** | 2026-04-29 20:34 | 6,578 files / 1,436,765 ins | **Root squash.** Hand-types `M_P_HECKE_PIPELINE = 1.4283` and `M_E_HECKE_PIPELINE = 0.0007783` into `build_proton_mass_50dps_chain.py:60-61`. Comment: `# rounded summary; see note above`. `derivation_chain.py` exists but does NOT contain the literal at this point. |
| **`0312a1e`** | 2026-04-29 21:38 | 3 files / 28 ins / 16 del | **Centralization.** Moves the literal from the builder into a new `M_HECKE_PIPELINE_AT_Q0` registry in `derivation_chain.py`. Value is copied verbatim, not recomputed. |

### 8.2 The other 8 "matching" commits are squash-rebase artefacts

`git log --all -S '1.4283'` returns 10 commits (excluding my own), but
blob-hash equality reveals that 6 of them share the **identical**
`derivation_chain.py` blob `bd31a3ee19fd…`:

| Commit | derivation_chain.py blob |
|--------|--------------------------|
| `0312a1e` Apr 29 21:38 | `bd31a3ee…` (created here) |
| `c69f66a` May 1 | `bd31a3ee…` (unchanged) |
| `20e428e` May 1 | `bd31a3ee…` |
| `03ec39c` May 2 | `bd31a3ee…` |
| `0866254` May 2 | `bd31a3ee…` |
| `0a53e1e` May 2 | `bd31a3ee…` |
| `bb61068` May 2 | `bd31a3ee…` |
| `9e50eb5` May 2 | `99e6a3f9…` (unrelated edit) |
| `a43d7f1` May 3 | `99e6a3f9…` (unrelated edit) |

`9e50eb5` and `a43d7f1` change the blob but do NOT modify
`M_HECKE_PIPELINE_AT_Q0["p"]` — they edit other parts of the file
(q-Hecke probe / Kashaev integrand variables).

The 6 commits with identical blobs are **omnibus rebase merges**
(each touches 6,600+ files and 1.4M+ lines per commit-stat).
Confirmed by the existence of `51efa18` `squash: rebase onto
origin/main + resolve all conflicts (conflicts resolved in 8 files)`
on the branch's main path. `git log -S` matches them because each
rebase re-emits the registry block as `+` in its merge diff.

### 8.3 No commit computes `1.4283` programmatically

```bash
git show 1861df6:folio-assistant/computations/mass_endomorphism.py | grep -c '1\.4283'
# -> 0

git show 1861df6:folio-assistant/computations/proton_mass_tower_derivation.py | grep -c '1\.4283'
# -> 0
```

The docstring at `1861df6`'s `build_proton_mass_50dps_chain.py:53-57` claims
the literal is a "rounded summary of the upstream
`proton_mass_tower_derivation.py` output". That script's actual output is
`m_p_Hecke ≈ 1,178,995` (f64) — verified by re-running it post-squash and by
inspecting the script's body at `1861df6`. It has **never** produced `1.4283`
in any committed code path.

### 8.4 The literal sits at the wrong CODATA target

`1.4283 / 0.0007783 = 1835.1535`. CODATA values:

```
(m_p − m_e) / m_e = 1835.1527    ← matches to ~1 ppm
m_p / m_e         = 1836.1527    ← differs by exactly +1.000
```

Whoever typed the literal pre-squash was matching `(m_p − m_e)/m_e`,
not `m_p/m_e`. Either deliberately (subtracting the bound electron
of atomic hydrogen and forgetting to add it back), or as a mistaken
calibration target.

### 8.5 Implication for the audit

This archaeology **rules out Option C** ("audit upstream provenance"):
there is no committed upstream computation to find or refute. The
literal is a placeholder hand-typed at the root squash, calibrated to
the wrong target, with a docstring claiming a provenance that no
committed code supports.

The viable resolutions reduce to **A / B / D / E** as enumerated
in §5. Recommendation remains **D** (relabel-then-derive).

## 9 — Cross-reference

- Phase 0 audit: `docs/audits/2026-05-09-mass-table-1ppb-audit.md`
- Phase 1 diagnostic witness: `folio-assistant/computations/proton-residual-rootcause.witness.json`
- Phase 1.5 audit witness: `folio-assistant/computations/proton-m_e-anomaly-audit.witness.json`
- Plan: `/root/.claude/plans/lots-of-new-math-parallel-lagoon.md`
- Real edit commits for the literal: `1861df6` (root squash, Apr 29 20:34),
  `0312a1e` (centralization, Apr 29 21:38). All other matches are
  squash-rebase artefacts (verified by blob-hash equality).
