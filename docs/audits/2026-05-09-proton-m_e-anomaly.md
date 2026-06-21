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

`computations/derivation_chain.py:73-76`:

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
Document the placeholder behavior in AGENTS.md and the precision dashboard,
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
mentions `1.4283` was performed after the initial m_e anomaly audit.
Findings:

### 8.1 Only two commits are real edits

| Commit | Date (UTC) | Stat | What it did |
|--------|-----------|------|-------------|
| **`1861df6`** | 2026-04-29 20:34 | 6,578 files / 1,436,765 ins | **Root squash.** Hand-types `M_P_HECKE_PIPELINE = 1.4283` and `M_E_HECKE_PIPELINE = 0.0007783` into `build_proton_mass_50dps_chain.py:60-61`. Comment: `# rounded summary; see note above`. `derivation_chain.py` exists but does NOT contain the literal at this point. |
| **`0312a1e`** | 2026-04-29 21:38 | 3 files / 28 ins / 16 del | **Centralization.** Moves the literal from the builder into a new `M_HECKE_PIPELINE_AT_Q0` registry in `derivation_chain.py`. Value is copied verbatim, not recomputed. |

### 8.2 The other 8 "matching" commits are squash-rebase artefacts

`git log --all -S `\.1.4283.` returns 10 commits (excluding the audit's own), but
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
git show 1861df6:computations/mass_endomorphism.py | grep -c '1\.4283'
# -> 0

git show 1861df6:computations/proton_mass_tower_derivation.py | grep -c '1\.4283'
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

## 9 — Addendum (2026-05-09 evening): Items 1–4 already resolved by Strategy-3

After this audit was written, a closer reading of the 10-day commit
window revealed that the Option B prerequisites listed in §5 had
**already been resolved upstream** in commits `5c3919b` (May 5),
`dbaf2aa` / `57a6f2f` (May 6), and the `atomic_braid_mass_table.py`
"Strategy-3" mass table.  The `proton-mass-50dps.derivation.json`
chain is therefore a **stale scaffold** that no longer represents the
canonical mass derivation.  The 544k ppb "defect" is an artefact of
that staleness, not of the framework.

### 9.1 What Strategy-3 actually computes

`atomic_braid_mass_table.py` (canonical mass-table chain, anchored in
`atomic_braid_mass_terms.py`) implements the unit-reconciled formula

```
total_hecke = T1 + T2 + T3 + T4         (cat units)
M_pred      = E_0 · total_hecke + T6_MeV (MeV; T5 multiplicative on T1)
E_0         = (M_p − T6_MeV[p]) / total_hecke[p]   (proton-calibrated)
```

with documented unit conventions in
[`atomic_braid_mass_terms.py`](../../computations/atomic_braid_mass_terms.py):

> **Dimensionality conventions:**
> - Hecke-unit terms (T1, T2, T3, T4) are returned in cat units —
>   they get scaled by `E_0` (MeV/cat-unit) at the assembly site.
> - T6 is returned in MeV directly; **do not** multiply by `E_0`
>   again at the assembly site.

### 9.2 Verification at q_0 (this session)

Running `atomic_braid_mass_table.py` produces:

```
|tr_M(p)|_atomic     = 1.6331535640481      (matches the closed-form derivation to 14 digits)
total_hecke[p]       = 4.6912 cat units
T2[p]=0.4986   T3[p]=0.0622   T4[p]=2.4973   T6[p]=0.6807 MeV
E_0                  = 199.859751695 MeV / cat-unit
M_pred[p]            = 938.2721 MeV          (= CODATA, by calibration)
```

The placeholder literal `M_HECKE_PIPELINE_AT_Q0["p"] = 1.4283` matches
**neither** `total_hecke[p] = 4.6912` **nor** `|tr_M(p)| = 1.6332`.
It is a dead literal that does not correspond to any quantity in the
canonical chain.

### 9.3 Status of the Option B prerequisites (Items 1–4)

| Item | Status | Resolution |
|------|--------|-----------|
| **1.** Unit reconciliation across T1–T6 | **RESOLVED** | `atomic_braid_mass_terms.py` documents the conventions; `atomic_braid_mass_table.py:322` does the assembly `M_pred = E_0 · total_hecke + T6_MeV` |
| **2.** A=1 brane-tower extension | **RESOLVED** | Strategy-3 populates A=1 (proton, neutron) with T2=0.4986, T3=0.0622; uses `t2_markov` / `t3_markov` (not the `terms-2-3-atom-per-gen-mpfr-50dps.witness.json` which was A≥2 only) |
| **3.** T5 sign / scale audit | **RESOLVED** | Strategy-3 uses T5 = (a_K − 1)·T1·E_{0,β}; for proton a_K=1 ⇒ T5=0. The −7.79 MeV from `mass_formula_6term_mpfr_50dps.py` was a different (structurally inequivalent) T5 formulation; that script is not on the canonical chain. |
| **4.** Replace `M_HECKE_PIPELINE_AT_Q0["p"]` | **REFRAMED** | The literal does not correspond to any quantity in Strategy-3. Right action is **deprecate the registry + the legacy chain**, not "replace with derived value". |

### 9.4 Δ_n² and Δ_I — the full-twist + knot-operator scalars

The user's mention of "δ and δ²" refers to two distinct scalars that
the Strategy-3 chain consumes explicitly:

**Δ_n² — full-twist saturated-shell scalar** (per
`conj:categorical-neutrality-saturated-shells` and
`full_twist_delta_n2_verification.py`):
the full twist Δ_n² ∈ Z(B_n) ↪ Z(H_n(q)) acts on each Wedderburn block
V_λ as the central scalar `q^{c(λ)}` where `c(λ) = Σ_{(i,j)∈λ} (j−i)`
is the partition's content sum.  At magic n ∈ {2,8,20,28,50,82,126}
the categorical mass endomorphism Φ_n is invariant under this action.

**Δ_I — knot-operator quotient-braid Jones factor** (per
`atomic_braid_mass_table.py:T1`):
the per-atom multiplicative coupling `a(Z, N)` derived from the
canonical-knot-id-SDP solver (when available; falls back to
`jones_quotient_fallback` otherwise).  Embeds into T1 as

```
|tr_M_atomic(K)| = |tr_M(p)|^Z · |tr_M(n)|^N · |a(Z,N)| · Δ_n²-scalar
```

These were both upgraded in the May 6 PR #548 work to preserve 50-dps
precision (`57a6f2f`) and to disambiguate dim-irrep from |S_n|
(`dbaf2aa`). The earlier m_e anomaly audit did not catch them because it focused
on the legacy `proton-mass-50dps.derivation.json` chain that doesn't
consume them.

### 9.5 Strategy-3 prediction errors (the new bottleneck)

The proton sits at 0% error by construction (E_0 is calibrated
against M_p).  The actual 1 ppb work has shifted to closing the
**other-atom** errors:

| Atom | Strategy-3 M_pred | M_codata | Error |
|------|-------------------|----------|-------|
| p    | 938.272 MeV       | 938.272  | 0.000% (calibration anchor) |
| n    | 861.345           | 939.565  | **−8.325%** |
| D    | 1420.831          | 1875.613 | **−24.247%** |
| T    | 1287.884          | 2808.921 | **−54.150%** |
| ³He  | 1391.177          | 2808.392 | **−50.464%** |
| ⁴He  | 2243.587          | 3727.379 | **−39.808%** |

The 8% neutron error and 24+% nucleon-binding errors at A ≥ 2 are
the **real precision frontier**.  These trace primarily to:
- The `canonical_a_k(jet-knot)` values for A=3,4 atoms (T, ³He, ⁴He)
- The T2 / T3 brane-tower computations at A ≥ 2 (Markov-cumulant form)
- Δ_n² coupling for higher A (n=6, 9, 12 partitions)

### 9.6 Recommended next steps (revised from §5)

1. **Deprecate the legacy chain.** Update
   `M_HECKE_PIPELINE_AT_Q0` and `build_proton_mass_50dps_chain.py`
   docstrings to mark them DEPRECATED and point to
   `atomic_braid_mass_table.py` as the canonical chain.

2. **Re-anchor 1ppb work on Strategy-3.** The mass-table-1ppb-audit
   (Phase 0) and the subsequent T1 / T3 / T2 / T5 / T4 / T6 queue
   should be rescoped against Strategy-3's actual prediction errors,
   not the legacy chain's `544k ppb` artefact.

3. **Investigate the −8% neutron error.** The neutron has the same
   T2/T3/T4/T6 and a(Z,N)=1 as the proton, differing only in
   |tr_M(n)| = 1.2482 vs |tr_M(p)| = 1.6332.  But the Strategy-3
   prediction is 861 MeV vs CODATA 939.6 — an 8.3% gap.  This
   localises the unit-conversion bug somewhere in the proton-only
   calibration of E_0.

4. **Audit the canonical_a_k jet-knot invariants.** A=3,4 errors
   are −54%, −50%, −40%; these are dominated by `a(Z,N)` for T,
   ³He, ⁴He.  Either the canonical-a_k values are wrong, or the
   product structure `|tr_M(p)|^Z · |tr_M(n)|^N · a(Z,N)` is
   missing a piece.

### 9.7 Cross-references

- Categorical chain γγ → 6-term derivation:
  `docs/audits/2026-05-05-categorical-chain-gamma-to-six-term.md`
  (commit `5c3919b`)
- Six-term per-weight derivation:
  `docs/audits/2026-05-04-six-term-per-weight-derivation.md`
- Δ_n² verification:
  `computations/full_twist_delta_n2_verification.py`
- Strategy-3 canonical chain:
  `computations/atomic_braid_mass_table.py`
- Shared term utilities:
  `computations/atomic_braid_mass_terms.py`
