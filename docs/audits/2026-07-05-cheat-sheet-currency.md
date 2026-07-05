# Cheat-sheet currency audit — 2026-07-05

**Scope**: Currency + derivation-chain-gap audit of
[`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md)
— the authoritative cross-link named in `AGENTS.md`. Verifies each step of the
canonical chain (substrate q₀ → **C** action → Yekutieli → Hecke → Wedderburn →
Frobenius tr_M → SDP → τ functor → MeV) still points at the correct canonical
compute script + paper reference; flags stale references, dead links, and any
claim contradicted by a more recent audit.

**Lane**: only `docs/canonical-derivation-cheat-sheet.md` + this audit doc.
Content blocks / `.qa.json` / `computations/*.py` were **not** edited.

**Verdict**: the doc is unusually current and densely cross-referenced. Three
mechanical currency defects found and fixed; **no un-tracked derivation gap
found** (the live step-9 frontier is already tracked with full corpus-grep
evidence). One content-side loss surfaced for the owner (below).

---

## Currency fixes applied

### 1. §5 item 4 — L2 100× count was stale (3/7 → 2/7)

- **Was**: *"live witness shows **3 of 7** observables pass 100× (m_p, m_e,
  m_K/m_π) … m_p PASSES (substrate anchor; 0.0004 ppb)"* (dated "2026-06-03
  reconciliation").
- **Now**: **2 of 7** (m_e, m_K/m_π); **m_p dropped 2026-07-04**.
- **Evidence** (corpus-grep, all three agree):
  1. Committed `computations/per-observable-100x-status.witness.json` →
     `"beats_100x_count": 2`.
  2. `AGENTS.md` §Precision-goals table: *"2/7 met (m_e, m_K/m_π) …
     m_p misses by ~437× since 2026-07-04"* + the STRICT q₀-anchor §rule 1
     (*"The canonical L2 count is 2/7 … since 2026-07-04 … not 3/7 or 4/7"*).
  3. [`docs/audits/2026-07-04-c4-mu-p-tension-pin-dependence.md`](2026-07-04-c4-mu-p-tension-pin-dependence.md)
     — m_p "pass" held only via a fitted Habiro tower
     `(1+46u⁴)(1+4u⁵)(1−29u⁶)` (a muon-era fit on the proton-pinned q₀,
     +242 ppb regression); tower dropped, de-fitted round-trip +1.35 ppb
     (~437× miss).

### 2. §9.2 — dead script name

- `knot_volumes.py` → `knot-volumes.py` (actual file is hyphenated;
  `computations/knot-volumes.py` exists, `knot_volumes.py` does not).

### 3. §5 item 5 — dead EW-triplet content link

- The link `../content/quantum-observable-universe/archimedean-universe/electroweak-higgs-torus-link-triplet.md`
  resolved to nothing: **neither the file nor the `archimedean-universe/`
  chapter dir exists** in the corpus (the dir was reorganized in the
  2026-05-25 chapter restructure — see
  [`docs/chapter-restructure-2026-05-25.md`](../chapter-restructure-2026-05-25.md)).
- **Corpus-grep**: `find content -iname "*electroweak*"` → empty;
  `ls content/quantum-observable-universe/ | grep -i arch` →
  `appendix-knot-operations-archimedean`, `appendix-surreals-archimedean`
  only. The surviving EW-cell content lives in `mass-theory/`
  (`hoefsmit-ew-cell-content.md`, `weak-symmetric-normalization.md`,
  `weak-spectral-completeness.md`, all verified present).
- **Fix**: repointed to the two live audit docs that document the
  T(2,8)/T(2,6)/T(2,4) triplet route —
  [`2026-05-24-sm-particle-categorical-map-rt-route.md`](2026-05-24-sm-particle-categorical-map-rt-route.md)
  (8 triplet mentions) +
  [`2026-05-24-pr1122-retraction-and-existing-canonical-adaptation.md`](2026-05-24-pr1122-retraction-and-existing-canonical-adaptation.md)
  — and named the surviving `mass-theory/` blocks. No fabricated content
  path.

---

## Verified current (no change needed)

- **All referenced compute scripts exist** (27 checked): `substrate/hecke_core.py`,
  `hecke/hecke_character_symbolic.py`, `hecke/hecke_characters.py`
  (`chi_lambda_braid` defined at line 294 — §2/§7 refs accurate),
  `canonical_mass.py`, `m_p_substrate_identity_50dps.py`, the three deprecated
  legacy vol-density scripts (`mass_table_ppb.py`,
  `m_p_borromean_verification_50dps.py`, `mass_formula_6term_mpfr_50dps.py`),
  `y_lambda_wenzl_bridge.py`, `derived_chi_catalogue{,_sweep}.py`,
  `lp_dual_solver.py`, `free-neutron-decay.py`, `derivation_chain.py`,
  `closed_form_tau_M.py`, `canonical_braid_marshalling.py`,
  `borromean_binding_recompute.py`, `binding_canonical.py`,
  `binding_depth_stratified_rust.py`, `binding_reeb_phase_decomposition.py`,
  `vol_density_per_block_wiring.py`, `reeb_flow_garside_closed_form_verification.py`,
  `probe_9b_laurent_degree_10a5.py`, `DERIVATION-CHAIN-METHODOLOGY.md`,
  `_li_2_q_util.py`, `mass_vol_density.py`. Only `knot_volumes.py` was
  wrong-named (fix 2).
- **All 14 §2 step-table paper labels resolve** in `content/`:
  `prop:braid-action-tensor`, `prop:hecke-spectral-sequence`,
  `thm:jones-markov-trace`, `prop:x5-bring-weight-identification`,
  `prop:alpha-k-derivation-procedure`, `def:frobenius-hopf-substrate`,
  `prop:chirality-writhe-ribbon-derivation`, `prop:gb-spectral-sequence`,
  `conj:jet-convergence-classical-limit`, `prop:atom-knot-mass-derivation`,
  `prop:confinement-sdp`, `prop:neutron-qvalue-symbolic`,
  `prop:geom-universality`, `prop:operator-selection-lp`.
- **All ~45 audit/coordination doc links resolve** except the one content
  dead-link fixed in fix 3.
- **Chain steps 1–11 are complete** — no missing step. The step→script→witness
  mapping in §2 and the §0 per-step status table are internally consistent and
  reflect the 2026-06-24 muon-anchor absolute-mass ruling + the 2026-07-02
  §9-consolidation restructure.

## Derivation gaps — none newly declared open

Per the `AGENTS.md` anti-flip-flop corpus-grep checklist, before declaring any
item "open" I checked `docs/audits/`, `content/`, `computations/`, and
`docs/coordination/`. **The doc already tracks its own live frontier** — the
step-9b Δ_λ / per-λ Borromean weight — with extensive, up-to-date evidence
(PROBE 1–4 verdicts through 2026-07-02, the FR-restricted-projector candidate,
the `10A−5` bookkeeping resolution, bean `ovud`). Nothing surfaced that the doc
mis-labels as settled or omits. No new "gap" is warranted.

## For the owner (content-side, NOT fixed — lane is docs-only)

- **Lost content block**: the T(2,8)/T(2,6)/T(2,4) electroweak-triplet RT-route
  had a standalone content block `electroweak-higgs-torus-link-triplet.md` that
  was **dropped in the 2026-05-25 chapter restructure** and never re-homed as a
  content block (the material survives only in the 2026-05-24 audit docs +
  scattered `mass-theory/` blocks). If the EW torus-route is meant to be a
  first-class paper block, it needs re-creating under a current chapter dir.
  The cheat-sheet link now points at the audit docs as an interim.

---

*Fixes on branch `claude/cheat-sheet-currency-2026-07-05`; see PR for blob
links.*
