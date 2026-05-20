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

### 2. Bring-Bloch K-search — 4-tier consistent NEGATIVE

Extension of PR #843's Tier 0 negative result to Tier 1+2+3.
Target: $\mathrm{Vol}(K_p^{\mathrm{eff}}) = \lambda_p \cdot 8G \approx 18.026$.

| Tier | Basis size | Source                                          | Result   |
|------|-----------:|-------------------------------------------------|----------|
| 0    | 10         | atlas-named hyperbolic                          | NEGATIVE |
| 1    | 11         | + Birman-Hilden 3-braid through 8 crossings     | NEGATIVE |
| 2    | 16         | + bridge-3 8-crossing (4-braid)                 | NEGATIVE |
| 3    | 33         | + 9-crossing prime hyperbolic (KnotInfo)        | NEGATIVE |

**Open frontier:** the proton's specific Bring-decomposition either (a) needs coefficients >$10^5$, (b) needs composite/10+ crossing knots, (c) requires transcendental Bloch-Wigner ingredients beyond hyperbolic-3-manifold volumes, or (d) involves Tier 4+ knot families.

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
| ⁴He  | 4 | 12 | (H_{12} A-operator extract not in repo)              | OPEN         |

**Aggregator:** `mass-tower-operator-valued-chain.witness.json`
makes the chain visible end-to-end.

### 5. canonical-mass-table-extended regenerated through ⁵Li

Post-Vol(𝓑₃) = 8·G fix, the proton/neutron rows close to **−0.32 ppb** against CODATA (was −251 ppb pre-fix).

| atom | pred (MeV)   | ref (MeV)   | err       |
|------|--------------|-------------|-----------|
| p    | 938.272088   | 938.272088  | −0.32 ppb |
| n    | 939.565420   | 939.565421  | −0.32 ppb |
| D    |   2.248821   |   2.224566  | +1.09 %   |
| T    |   8.468598   |   8.481798  | −0.16 %   |
| ³He  |   7.488919   |   7.718043  | −2.97 %   |
| ⁴He  |  29.955677   |  28.295673  | +5.87 %   |
| ⁵Li  |  (—)         |  26.328000  | —         |

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
| #836 | claude/c5-followups                  | golden-node falsifiability (related to PR #690 C2 inflection) | hold |
| #841 | claude/fr-pullback-k1-k2-identification | FR pullback, distinct scope | hold |
| #831 | claude/post-819-ledger-update        | Δ_λ Phase 5f-5k.1 | hold |
| #845 | claude/phase-5l-disjoint-markov-trace | Phase 5l constit-factor (precursor to Move 4) | independent |
| #849 | claude/phase-5l1-tau-M-proton-closed-form | Phase 5l.1 τ_M closed forms | independent |

## Files touched (PR #852)

- **New scripts:** `bring_bloch_tier1_search_m_p.py`, `bring_bloch_tier2_search_m_p.py`, `bring_bloch_tier3_search_m_p.py`, `li2q_phiq_bar_symmetry_witness.py`, `skein_proton_canonical.py`, `mass_tower_operator_valued_chain.py`
- **New witnesses:** `bring-bloch-tier1-search-m-p.witness.json`, `bring-bloch-tier2-search-m-p.witness.json`, `bring-bloch-tier3-search-m-p.witness.json`, `li2q-phiq-bar-symmetry.witness.json`, `skein-proton-canonical.witness.json`, `mass-tower-operator-valued-chain.witness.json`
- **Updated witnesses:** `canonical-mass-table-extended.witness.json` (regenerated), `onepb-status-dashboard.witness.json` (regression fix), `witness-provenance-audit.witness.json` (refresh)
- **Updated content blocks:** `li2q-phiq-bar-symmetrization.md`, `bar-symmetric-three-layer-synthesis.md`, `q-rogers-pentagon-archimedean.md`
- **Updated compute:** `onepb_status_dashboard.py` (data-ingestion fallback)

## Next-direction recommendations

1. **H_{12} A-operator extract for ⁴He** — closes A = 4 in the operator-valued mass-tower chain (Move 4 open frontier). Estimated 30-60 min compute via numpy-Hoefsmit.
2. **Tier 4 Bring-Bloch search** — extend basis to 10+ crossing prime knots; if still negative, evidence the proton's Bring-decomposition is genuinely transcendental.
3. **Continue mass-table extension** to ⁶Li, ⁷Li (heavy compute, > 30 min each).
4. **Joint-tower SDP infrastructure** — the bigger atlas-extension task identified earlier.
