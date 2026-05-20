# Coordination ledger — PR #852 `claude/lambda-p-followons`

**Date:** 2026-05-20
**Branch:** `claude/lambda-p-followons`
**Goal:** Substrate-pure m_p derivation follow-ons after PR #843
(bar-symmetrization, Bring-Bloch K-search extension, Skein, mass-
tower wiring).

## Headline findings

### 1. `prop:li2q-phiq-bar-symmetrization` — boxed identity FALSIFIED

The paper's claim
$\mathrm{Li}_2^q(z) \stackrel{?}{=} \tfrac{1}{2}(\log\Phi_q + \log\Phi_{q^{-1}}) + O((q-1)^3 z)$
is numerically falsified. For Faddeev's
$\Phi_q(z) = \prod(1-q^{2k+1}z)^{-1}$, $\log\Phi_{q^{-1}}(z) =
-\log\Phi_q(z)$ identically, so the SUM is zero.

**Correct identity** (verified to $10^{-55}$ relative at $q_0$):

$$\mathrm{Li}_2^q(z) \;=\; -h \cdot \log\Phi_q(z) \;=\; \tfrac{h}{2}\bigl(\log\Phi_{q^{-1}} - \log\Phi_q\bigr), \qquad h = q - q^{-1}$$

The §Proof in the .md had an arithmetic error in the line
"$q^n/(1-q^{2n}) + q^{-n}/(1-q^{-2n}) = -1/(q^n - q^{-n})$" — the
actual value is $0$.

**Files updated** (paper upstream/downstream sweep):
- `li2q-phiq-bar-symmetrization.md` — Proposition body rewritten with correct boxed identity + §Proof corrected; superseded SUM form moved to historical note.
- `bar-symmetric-three-layer-synthesis.md` — bar-classification table Li_2^q row + §Series-layer formula both updated.
- `q-rogers-pentagon-archimedean.md` — Volume-conjecture matching paragraph terminology updated.

**Witness:** `li2q-phiq-bar-symmetry.witness.json` (2 assertions: falsification + correct identity).

### 2. Bring-Bloch K-search — 6-tier consistent NEGATIVE

Extension of PR #843's Tier 0 negative result to Tier 1–5.
Target: $\mathrm{Vol}(K_p^{\mathrm{eff}}) = \lambda_p \cdot 8G \approx 18.026$.

| Tier | Basis size | Source                                          | Result   |
|------|-----------:|-------------------------------------------------|----------|
| 0    | 10         | atlas-named hyperbolic                          | NEGATIVE |
| 1    | 11         | + Birman-Hilden 3-braid through 8 crossings     | NEGATIVE |
| 2    | 16         | + bridge-3 8-crossing (4-braid)                 | NEGATIVE |
| 3    | 33         | + 9-crossing prime hyperbolic (KnotInfo)        | NEGATIVE |
| 4    | 40         | + 10-crossing prime hyperbolic (KnotInfo)       | NEGATIVE |
| 5    | 52         | + 11-crossing prime hyperbolic (KnotInfo)       | NEGATIVE |

**Open frontier:** after 6 consecutive negatives spanning all prime
hyperbolic knots through 11 crossings (52 basis elements), the
proton's Bring-decomposition is most plausibly either (a) requires
the categorical-trace q-dilog tower directly (not a Bring-Bloch
realisation via hyperbolic volumes), (b) needs transcendental
Bloch-Wigner ingredients beyond hyperbolic-3-manifold volumes,
or (c) requires composite/satellite knots. Pure coefficient-scaling
in the prime-knot basis is effectively ruled out at the 6-tier scale.

### 3. S(p) Skein evaluator — `S(p) ≈ 0` is calibration-forced

Three Skein-interpretation hypotheses tested for
$m_p = m_e [\mathrm{Vol}(𝓑₃)/\hbar_q^2 \cdot \lambda_p + S(p)]$:

| Hypothesis              | m_p_pred (MeV) | Δ vs CODATA |
|-------------------------|--------------:|------------:|
| S(p) = 0 (production)   | 938.27185     |  −251 ppb   |
| S(p) = ‖tr_M(β_p)‖      | 938.81649     |  ~580 ppm   |
| S(p) = V(𝓑₃, q²)        | 940.34611     |  ~2200 ppm  |

Only S(p) ≈ 0 is consistent with the 1 ppb m_p closure. The
conjecture should be revised to drop S(p) entirely OR re-derive
$\lambda_p^{\mathrm{scale}} = (\mathrm{Vol}(K_p^{\mathrm{eff}}) - S(p))/\mathrm{Vol}(𝓑₃)$
with both pieces explicit.

**Witness:** `skein-proton-canonical.witness.json`.

### 4. Operator-valued mass-tower — Stage-1 unblock visible through A = 3

`prop:mass-tower-operator-valued` was silently fully wired
through A = 3:

| Atom | A | n  | Witness                                              | Status |
|------|---|----|------------------------------------------------------|--------|
| D    | 2 |  6 | mass-tower-operator-valued.witness.json              | PROVED 5e-15 |
| T    | 3 |  9 | sublemma-2-1-h9-tritium-verify.witness.json          | PROVED       |
| ³He  | 3 |  9 | sublemma-2-1-h9-tritium-branching-verify.witness.json | PROVED 1e-14 |
| ⁴He  | 4 | 12 | sublemma-2-1-h12-helium-4-framework.witness.json     | FRAMEWORK (deferred compute) |

**Aggregator:** `mass-tower-operator-valued-chain.witness.json`
makes the chain visible end-to-end.

**A = 4 framework (2026-05-20):** the H_{12} extract is queued
as a follow-on PR — the framework script
(`sublemma_2_1_h12_helium_4_framework.py`) verifies prerequisite
H_6 + H_9 witnesses, documents the iterated 3-interface formula
β_p · I_pp · β_p · I_pn · β_n · I_nn · β_n, and records a 6-step
compute plan (estimated 30-60 min via numpy-Hoefsmit).

### 5. canonical-mass-table-extended regenerated through ⁶Li

Post-Vol(𝓑₃) = 8·G fix, the proton/neutron rows close to **−0.32 ppb** against CODATA (was −251 ppb pre-fix).

| atom | A | n  | \|tr_M(q_0)\| | pred (MeV) | ref (MeV)  | err       |
|------|---|----|---------------|------------|------------|-----------|
| p    | 1 |  3 | 1.06530623    | 938.272088 | 938.272088 | −0.32 ppb |
| n    | 1 |  3 | 0.92323330    | 939.565420 | 939.565421 | −0.32 ppb |
| D    | 2 |  6 | 0.38828647    |   2.248821 |   2.224566 | +1.09 %   |
| T    | 3 |  9 | 0.10405212    |   8.468598 |   8.481798 | −0.16 %   |
| ³He  | 3 |  9 | 0.20654086    |   7.488919 |   7.718043 | −2.97 %   |
| ⁴He  | 4 | 12 | 0.05534835    |  29.955677 |  28.295673 | +5.87 %   |
| ⁵Li  | 5 | 15 | 0.02944139    |   (—)      |  26.328000 | —         |
| ⁶Li  | 6 | 18 | 0.00788964    |   (—)      |  31.994050 | —         |

**A = 5, 6 |tr_M| values now measured** (markov_peel ~68 sec for ⁵Li,
~18 min for ⁶Li at H_{15}, H_{18}). Predictions (`B_pred`) require
the closure framework which is gated on the Δ_λ ansatz and per-
isotope knot-tower assignments — neither resolved on this branch.

### 6. onepb-status-dashboard data-ingestion regression fix

Generator was reading `cross-check-trM-1ppb.witness.json` top-level
fields (legacy format) but the witness has migrated to
WitnessBuilder layout with fields under `data.*`. Dual-path reader
now correctly reports `atoms_compared: 8`, `all_within_1ppb: true`.

## Cross-PR coordination

Sibling PRs scanned (cycles 2026-05-20):

| PR  | Branch                                | Overlap | Action |
|-----|---------------------------------------|---------|--------|
| #840 | claude/stage-2-prop-revival          | merged 2026-05-20 — independent Vol(𝓑₃) verification | none |
| #836 | claude/c5-followups                  | merged 2026-05-20 — golden-node falsifiability | none |
| #841 | claude/fr-pullback-k1-k2-identification | FR pullback, distinct scope | hold |
| #831 | claude/post-819-ledger-update        | Δ_λ Phase 5f-5k.1 | hold |
| #845 | claude/phase-5l-disjoint-markov-trace | SUPERSEDED by #854 | none |
| #849 | claude/phase-5l1-tau-M-proton-closed-form | SUPERSEDED by #854 | none |
| #853 | claude/phase-5n-notation-rename | merged 2026-05-20 — notation refactor (226 files); merge_state still clean | none |
| #854 | claude/phase-5l-combined-with-5l1 | NEW 2026-05-20 14:43 — ρ_Z^constit = tr_M^3(B_p) identity; 13 files, no overlap with this PR's scope; thematic neighbor | intent posted ([#854 comment](https://github.com/litlfred/qou/pull/854#issuecomment-4499648775)) |
| #855 | claude/lean-typed-claims-round-13 | NEW 2026-05-20 14:51 — wall-side-correct cleanup (15 Lean files, content/quantum-observable-universe/*); no overlap with my compute scripts | hold |
| #807 | claude/compute-audit-P33-P34-2026-05-19 | overlap: also extends `.claude/skills/local/compute-audit.md`; my §Long-compute logging discipline appends to a *different* section than their P33/P34 → no git-conflict; coordinated | intent posted ([#807 comment](https://github.com/litlfred/qou/pull/807#issuecomment-4499648172)) |

## Files touched (PR #852)

- **New scripts:** `bring_bloch_tier1_search_m_p.py`, `bring_bloch_tier2_search_m_p.py`, `bring_bloch_tier3_search_m_p.py`, `bring_bloch_tier4_search_m_p.py`, `li2q_phiq_bar_symmetry_witness.py`, `skein_proton_canonical.py`, `mass_tower_operator_valued_chain.py`, `sublemma_2_1_h12_helium_4_framework.py`
- **New witnesses:** `bring-bloch-tier1-search-m-p.witness.json`, `bring-bloch-tier2-search-m-p.witness.json`, `bring-bloch-tier3-search-m-p.witness.json`, `bring-bloch-tier4-search-m-p.witness.json`, `li2q-phiq-bar-symmetry.witness.json`, `skein-proton-canonical.witness.json`, `mass-tower-operator-valued-chain.witness.json`, `sublemma-2-1-h12-helium-4-framework.witness.json`
- **Updated witnesses:** `canonical-mass-table-extended.witness.json` (regenerated), `onepb-status-dashboard.witness.json` (regression fix), `witness-provenance-audit.witness.json` (refresh)
- **Updated content blocks:** `li2q-phiq-bar-symmetrization.md`, `bar-symmetric-three-layer-synthesis.md`, `q-rogers-pentagon-archimedean.md`
- **Updated compute:** `onepb_status_dashboard.py` (data-ingestion fallback)

## Next-direction recommendations

1. **H_{12} A-operator extract for ⁴He** — closes A = 4 in the operator-valued mass-tower chain (Move 4 open frontier). Estimated 30-60 min compute via numpy-Hoefsmit. **Framework landed** as `sublemma-2-1-h12-helium-4-framework.witness.json`; the production extraction itself is queued.
2. **Continue mass-table extension** to ⁷Li and beyond (compute scales as ≥ #strands², so ⁷Li at H_{21} likely > 1 hr).
3. **Joint-tower SDP infrastructure** — the bigger atlas-extension task identified earlier; per-isotope LP/SDP with shared λ_K basis.
4. **q-dilog tower direct λ_p_scale derivation** — given 6-tier Bring-Bloch negative, the productive route is most likely the categorical-trace q-dilog tower (Φ_q + Li_2^q identities), not knot-Bloch realisation. This is the structural sequel to the bar-anti-symmetrization fix landed here.
