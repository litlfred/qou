# q₀ two-layer migration — scope for owner review (bean `z5vu`)

**Status:** scoping only — no compute changed. Owner decision required.
**Context:** follow-up to the q₀-convention codification (PR #2731) + the
m_e reconcile (PR #2725). The convention itself is settled (see AGENTS.md
§"q₀ anchor convention" + `three-calibration-discipline.md` §3).

## The convention (settled)

| Layer | q₀ pin | m_μ status |
|---|---|---|
| Ideal / canonical 3-CAL | CAL-2 = m_μ/m_e (`Vol(4₁)/ℏ_q²`) | calibration input — exact by construction |
| Experimental / Physical-Obs | m_p/m_e (0.06 ppb re-pin) | 9.5σ prediction, ~210 ppb (963.6× the L2 target) |

## What is inconsistent (the L2-dashboard symptom)

`per_observable_100x_status.py` reads m_μ from
`m-p-borromean-verification-50dps.witness.json` → `muon_check.m_mu_pred_MeV`.
That witness (and `q-pinning-50-digit.witness.json`, which feeds **~72
producers / ~840 witnesses**) carries q₀ = `1.1099785955573347`, which
reproduces the CODATA muon ratio to ~0.05 ppb. So a fresh dashboard run
reports m_μ ≈ met, while the committed witness + the authoritative
`precision-goals.md` report the proton-anchored **963.6× miss**.

## ⚠ Decisive open question (verify in the FULL compute env FIRST)

The migration's size depends on a fact I **could not verify in a minimal
sandbox** (`import qou_substrate.constants` without the F_Bor / Hecke
compute):

- In-sandbox, `constants.q_at(50)` (the "proton solve") returned
  `1.1099785955573347` and `q_muon_at(50)` returned `1.1099785955541806`
  — differing by only **~0.0028 ppb**, with **both** giving m_μ/m_e to
  ~0.05 ppb (i.e. both muon-behaving).
- The authoritative docs say the proton and muon q₀ differ by **~11.5 ppb**
  and m_μ misses **~210 ppb**.

These cannot both hold. Most likely `q_at()` fell back to a cached
muon-ish value because the proton Newton solve needs F_Bor (tr_M of the
Borromean braid), which the bare import did not execute. **Step 0 of z5vu
is to run `q_at(50)` in the full env and confirm it returns the true
proton q₀ (~1.10997858…, 11.5 ppb from muon, m_μ → ~210 ppb).** If it
does NOT — i.e. the package's exported canonical q₀ is itself
muon-behaving — then the "963.6×" framing (and the just-merged AGENTS.md
rule) would itself be the stale artifact, and the whole picture inverts.
Do not start the migration until Step 0 settles which value is canonical.

## Options (contingent on Step 0 = "proton q₀ is real, m_μ misses 210 ppb")

**Option A — full computations-layer migration to proton q₀.**
Regenerate `q-pinning-50-digit.witness.json` on the proton q₀, then the
~72 producers / ~840 downstream witnesses (the same scope as the
"143-producer canonical regen", commit `768d9ddf`). Coordinated,
long-compute (`… 2>&1 | tee` per the logging discipline), owner-gated.
- Pro: every witness becomes proton-canonical; the dashboard reads correct
  values natively; one source of truth.
- Con: largest blast radius; risks if the computations layer is *meant* to
  stay muon-canonical (3-CAL mathematical layer) while only the
  precision/package layer is proton.

**Option B — bounded dashboard fix (recommended if Step 0 confirms).**
Leave the ~840 muon-q₀ witnesses as the canonical *mathematical* (3-CAL)
layer; make only the **precision dashboard** evaluate predictions at the
**proton** q₀ (from `qou_substrate.constants`), so m_μ (and m_n, Δ_pn) are
scored as proton-anchored predictions and m_p as the anchor.
- Pro: no 840-witness churn; matches the two-layer convention exactly
  (canonical math = muon, physical-obs precision = proton).
- Con: the dashboard then mixes its data source (computations witnesses
  for structure, package q₀ for the precision evaluation) — must be done
  for ALL rows coherently, not m_μ alone, or the dashboard is half-muon
  half-proton.

## Recommendation

1. **Step 0 (cheap, full env):** confirm `q_at(50)` returns the true
   proton q₀ and that m_μ misses ~210 ppb. This also resolves whether the
   merged AGENTS.md rule / `observable-sector-tracker.md` edit are correct
   — if Step 0 inverts, revert those.
2. If confirmed → **Option B** (bounded dashboard fix), owner-reviewed,
   leaving the muon-canonical computations layer intact.
3. Option A only if the owner wants the entire computations layer
   proton-canonical (much larger; coordinate with the canonical-watcher /
   the `768d9ddf`-style regen tooling).
