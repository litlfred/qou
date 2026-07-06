# 2026-07-03 — Deuteron (D) canonical mass + binding from scratch: per-stage error ledger

**Date:** 2026-07-03 · **Branch:** `claude/d-mass-binding-canonical-aj98ux` · **PR:** [#3266](https://github.com/litlfred/qou/pull/3266) · **Bean:** `cexx` (session milestone)

## Goal (owner request, 2026-07-03)

Rebuild the deuteron mass and binding **from scratch** along the canonical
chain — from the substrate / γγ (pair-production) entry point through the
Hecke/Markov trace, the confinement SDP, to the archimedean MeV numbers —
**fully witnessed, no fitted constants, no hardcoded literals**, and with a
**per-stage error ledger**: at every stage of the chain, record the error the
stage introduces against the corresponding experimental anchor, so the owner
can see *where each error is coming from*.

Then, for the D case specifically, assess symbolic-answer prospects for the
four open A≥3-binding items (Δ_λ per-λ weight; α_k assignment rule; many-body
series closed form; mirror-pair magnitude), restricted to what D can decide.

## Status

**COMPLETE** — all seven stages run, symbolic prospects assessed, follow-up
landed. This doc is the ledger of record; see §Findings and §Verdict.

## Planned stage decomposition (γγ → D)

| Stage | Object | Canonical source | Anchor compared | Error recorded |
|---|---|---|---|---|
| S0 | q₀ pin (CAL-2 via m_μ/m_e = Vol(4₁)/ℏ_q²) | `q_parameter.Q_50_DIGIT_STR` / `constants.q_at` | m_μ/m_e (muon) vs m_p/m_e (proton) | μ–p tension (anchor-choice error) |
| S1 | γγ / pair-production entry: photon = crossing operator; e⁺e⁻ / nucleon-pair thresholds | corpus survey (crossing energy E_H, brane crossings) | — | structural (no fit) |
| S2 | Nucleon masses m_p, m_n (muon-anchored Hecke energy, `F_Bor`) | `canonical_mass.py` facade | CODATA m_p, m_n | per-nucleon mass error |
| S3 | Deuteron braid `atom_braid_word_3A(1,1)` → tr_M in H₆; Wedderburn per-λ decomposition | `closed_form_tau_M.py`, Wenzl bridge | — (exact ℚ(q) identity checks) | cross-method L1 error |
| S4 | Confinement SDP / operator selection at A=2, full primal+dual | `lp_dual_solver.py` | — | duality gap |
| S5 | Binding B_D — every non-fitted route: trace-canonical `E₀·Δtr`, depth-stratified tower, Vol(6₂), μ₀·ℏ_q·J_q², Borromean Li₂^q tower | `binding_canonical.py`, `binding_depth_stratified*.py`, `borromean_binding_recompute.py`, `per_braid_tower.py` | AME2020 B_D = 2.2246 MeV | per-route binding error |
| S6 | Deuteron mass m_D = m_p + m_n − B_D | composition | AME2020 m_D | end-to-end error |

## Symbolic-prospect targets (D case)

1. **Δ_λ(D) ≈ 1/h(q₀)** (h(q₀) = q₀^(−15.0002), PROBE-1 observation tier) — exact or near-match?
2. **FR-restricted projector** `χ^λ·χ^λ(e_{K*})` at D (brane-tower plan §7).
3. **α_k at A=2**: the k=3 break is DERIVED (`χ^{(2,1)}(Δ)=0`); the D tower only reaches depth 5 — what does the D-restricted assignment look like symbolically?
4. **Many-body series at A=2**: trivially one bond — D is the base case; what D fixes vs cannot decide.

## Findings

Producers: [`computations/deuteron_from_scratch_ledger.py`](../../computations/deuteron_from_scratch_ledger.py)
→ `deuteron-from-scratch-ledger.witness.json` (4/4 assertions) and
[`computations/probes/probe_d_symbolic_prospects.py`](../../computations/probes/probe_d_symbolic_prospects.py)
→ `probes/probe-d-symbolic-prospects.witness.json` (audit-only, 2/2).
All numbers at 50 dps, q₀ solved live, CODATA/AME comparison-only.

### Where each error comes from (the ledger)

| Stage | Error source | Size | Notes |
|---|---|---|---|
| S0 anchor choice | μ–p anchor tension in q-space | **11.53 ppb** | the proton pin (`q_at`) solves the RAW identity `m_p/m_e = 2·(Vol(4₁)/ℏ_q²)·F_Bor − 12` (owner ruling 2026-07-03: the fitted habiro tower that briefly dressed the pin was stripped). The ~11.5 ppb μ–p tension is the documented substrate floor (≈×21 → ~242 ppb on masses); the AGENTS "m_μ prediction" narrative is CURRENT. PR #3280 proved the exact habiro c₄ is linear in the pin offset, i.e. a dressed pin merely reparametrizes this tension rather than closing it |
| S1 γγ entry | none (topological) | 0 | γγ spans the 6-operator H₃ basis (Lean `gamma_gamma_chirality_surjective`); crossing energy `𝔈_×(q₀) = ½(q−q⁻¹) > 0`. **Flags:** (i) `nucleon-from-photons-summary.md` cites `four-term-photon-to-atoms.witness.json` which does not exist anywhere in the repo (dangling citation); (ii) the absolute-mass normaliser does not yet come from this chain (bean `ovud`) |
| S2 nucleon masses (RAW pin) | bare F_Bor identity, m_p ratio | **+1.35 ppb** | at the proton-pinned q₀ the BARE identity round-trips m_p/m_e by construction (ratio-space exact, 1e-40); the residual +1.35 ppb is the CODATA-internal MeV-conversion inconsistency (m_p[MeV] vs m_e[MeV]·(m_p/m_e)), not a framework error |
| S2 fit-tier diagnostic | Habiro-dressed m_p at the RAW pin | **+242 ppb** | applying either habiro c₄ (46 or 4143/90) at the raw pin OVERSHOOTS CODATA m_p by ~242 ppb — this IS the μ–p tension reparametrized (PR #3280). The dressing is fit-tier, not canonical; owner reconcile pending (bean `2i8g`) |
| S2 hygiene | producer `m_p_substrate_identity_50dps.py` still applies the fit-tier habiro dressing (its committed witness was computed at the old dressed pin) | producer m_p stale vs raw pin | flagged to #3280, not churned on this PR |
| S3 trace | transfer (fine-Bratteli) vs closed-form (colour-weighted Wenzl/χ_λ) atom/free ratio | **2.6e-1** | different canonical word families/normalizations, each exact on its own reference (Phase-5q closed form is exact-ℚ); finer Jones-vs-Wenzl convention-D spread is 1.955e-4 |
| S4 SDP | full-space real SDP unbounded (Frobenius Gram indefinite) | structural | bounded positive-norm subspace: duality gap 0.0; canonical LR-branching encoding does not reproduce B_D — that IS the Δ_λ gate |
| S5 binding | **the dominant error of the whole chain** | −79% … +33% route spread | see table below |
| S6 composed m_D | binding stage ≫ nucleon stage | nucleons ±0.0000 MeV, binding −0.74…+1.76 MeV | best composed m_D: −12.9 ppm (R3) |

### Binding routes at D (all non-fitted; B_AME = 2.2245662 MeV)

| Route | B (MeV) | err | error source |
|---|---:|---:|---|
| R1 tower level-0 `E₀·Δtr` | 2.4914 | **+11.99%** | uniform E₀ where the per-λ weight belongs |
| R1b + Li₂^q pair term | 2.9667 | +33.4% | tower adds binding — gap is not a truncation error |
| R2 Borromean level-0 | 2.0898 | −6.06% | same missing per-λ weight on the Borromean τ |
| R2b Borromean tower | 2.4803 | +11.5% | as R2 |
| R3 `m_e·Vol(6₂)` | 2.2488 | **+1.09%** | Kashaev linearization + underived ρ-scale rule |
| R4 diagnostic `Q_β·Δtr` | 0.4656 | −79.1% | scale mismatch — the Δ_λ(D) residual lives here |
| R5 rotational `μ₀·ℏ_q·J_q²(3)` | 2.0196 | −9.21% | highest-weight collapse of the per-λ Reeb phase |

### Symbolic prospects at D (probe, all near-match tier, nothing wired)

1. **Δ_λ(D) vs 1/h(q₀) — sharpened.** `Δ_λ(D)·h − 1 = −1.19e-3` (0.12%);
   q₀-exponent 14.9888 (−0.011 from 15). The candidate closed form
   `B_D = Q_β·Δtr/h` lands **+0.119% of AME with zero fits** — the sharpest
   D-specific target in this session. Scope (a): no invariant currently
   forces the 1/h; formalize-first question = *what forces the binding scale
   to be Q_β/h instead of E₀?*
2. **NEW cross-coincidence: `Q_β/h` vs `m_e·8G` = −6.2e-4** (0.06%). The
   "Δ_λ(D) ≈ 1/h" observation and the tower plateau constant `α_{k≥4} =
   m_e·8G` are (to 0.06%) the *same* statement: `Q_β ≈ m_e·8G·h`. Also
   `Q_β/h = 0.894·E₀` — exactly the R1 +11.99% overbind factor
   (1/0.894 = 1.119), i.e. R1 and R4 differ *only* by the E₀-vs-Q_β/h scale
   choice on the same Δtr. Observation tier; connects CAL-2 (𝔇_β), the
   Borromean/Catalan volume 8G, and the Hecke h on one line.
3. **α_k at A=2.** χ^{(2,1)}(σ₁σ₂σ₁) = 0 reproduced **symbolically** from
   the repo's own Hoefsmit seminormal matrices (sympy-exact) ⇒ the z^k
   break at k=3 is derived, not assigned. The collapsed weight is exactly
   `1 + q^{1/2} − q^{−1/2}` (= 1.1044 at q₀ — α₃ = 1 is a 10.4%
   near-match). The D depth-stratified tower gap 3.6656 has q₀-exponent
   12.449 — NOT near-integer: no q₀-power bookkeeping closes the D tower.
4. **Per-λ weight (Δ_λ / FR projector) — under-determination result.** At
   A=2 the scalar binding gives ONE equation against ELEVEN per-λ unknowns
   (λ ⊢ 6): the solution space is 10-dimensional, so **no unique symbolic
   Δ_λ is derivable from D data, and no collapse-last candidate preserving
   the scalar sum is falsifiable at A=2** — the structural reason PROBE-4's
   per-λ towers reproduced the scalar tower to ≤6.6e-7. The FR-restricted
   projector `χ^λ·χ^λ(e_{K*})` (brane-tower plan §7) is falsifiable only
   cross-A; D pins its scalar normalization. The probe emits the D per-λ
   atom vector (y_λ, χ^λ, contributions, 11 blocks) as the carrier the
   projector must weight.
5. **Q_β form spread.** Production Kashiwara-b² Q_β vs the symbolic CAL-2
   proxy `m_e|q²−2q−1|(q+1)/(2q³)`: 0.17% — matches the known CAL-2
   cross-check figure; recorded as the Q_β-form component of any
   trace-canonical binding number.
6. **Scope statements.** The many-body series (ρ·A rule, 2-body/4-body
   reconciliation) and the mirror-pair magnitude are NOT decidable at A=2:
   D is the exact 2-body base case and is silent on both.

### Follow-up (2026-07-04, owner picks 1+2) — formalize-first on the 1/h scale + facade fix

Producer: [`probes/probe_d_qbeta_h_invariant.py`](../../computations/probes/probe_d_qbeta_h_invariant.py)
→ `probes/probe-d-qbeta-h-invariant.witness.json` (audit-only, 3/3).

1. **EXACT reduction (sympy-proved in ℚ(q)):** with the CAL-2 proxy
   `Q_β = m_e·|q²−2q−1|(q+1)/(2q³)` and `E₀ = m_e/(q(q−1))`,
   `Q_β = E₀·h·(2−h)/2` **exactly** — so the "1/h" scale is not a new
   object: **`Δ_λ(D) = 1/h ⟺ B_D = E₀·(1−h/2)·Δtr`**, i.e. the canonical
   E₀ route dressed by `(1−h/2)` = the bar-average of the smoothed
   crossing pair `{1, 1−h}` (`σ⁻¹ = σ−h`; the same `−h/2` shift as the
   averaged p-n interface `σ_avg = σ−h/2`, and D has exactly one p-n
   interface). Numbers: undressed +11.99% → dressed **+0.29%** (proxy
   Q_β) / **+0.12%** (Kashiwara Q_β). Lean target filed (generic
   `[Field R]`, §7c — `field_simp; ring`).
2. **`Q_β = m_e·8G·h` REFUTED-as-exact** (scope (b) for the exact claim
   only; invariant = the 50-dps precision floor: gap 6.2e-4 vs required
   ~1e-45). The 0.06% near-match survives as an observation of the
   Weinberg-cosh class: `E₀·(2−h)/2 ≈ m_e·8G` at q₀,
   algebraic-vs-Catalan.
3. **Sharpened open question (the wiring gate):** derive from the
   binding functional that the trace-canonical scale is E₀ dressed by
   the smoothed bar-average of the single interface crossing. Until
   derived, the +0.12% candidate stays observation-tier (Δ_λ gate).
4. **Facade correctness (revised after main's raw-pin ruling):** the
   canonical pin (`q_at`) solves the RAW identity — main stripped the
   fitted habiro tower on 2026-07-03 (`7b95577aae`). So
   `canonical_mass.py::_from_formula` correctly uses the **bare** form
   `2·(m_μ·F_Bor − 6·m_e)` (no habiro), matching the raw pin to the
   ratio-space floor. `habiro_ratio_s5bb()`/`C4_S5BB` remain exposed at
   module level in `m_p_substrate_identity_50dps.py` **relabeled
   fit-tier** — the single edit point for the owner reconcile. (An
   earlier revision of this PR dressed the fallback with habiro; that
   was wrong against the raw pin and has been reverted.)
5. **c₄ history verdict (2026-07-04, owner-directed investigation;
   coordinated with PR #3280):** the pin's `46` entered with
   `d27b002745` (2026-06-15) as the then-fitted c₄; `58ba1c6800`
   (2026-06-28, bean `ovud`) *"replace fitted c_4 with exact geometric
   index 4143/90"* upgraded the **producer only** (zero q_parameter
   files touched) — and the "derived geometrically" label entered via
   that commit message alone. Sibling
   [PR #3280](https://github.com/litlfred/qou/pull/3280) independently
   shows: (i) the exact c₄ needed is **linear in the q₀ pin offset**
   (slope ≈ 3.99/ppb — c₄ = 46 *is* the muon-calibration convention,
   i.e. the μ–p tension reparametrized, not resolved), (ii) `4143` has
   **no derivation trail** in the corpus and the cited s5bb
   Reeb-resonance route is an explicit honest-negative, (iii) 4143/90
   overshoots vs naked 46. Combined verdict:
   BOTH values are fit-tier; my earlier "re-pin to 4143/90" direction
   is **withdrawn** — the reconcile is among #3280's owner options
   (relabel honestly / revert to 46 / drop to the 240 ppb floor). Since
   main independently stripped the habiro tower from the pin, the
   canonical pin is now RAW and the S0 tension is the honest ~11.5 ppb
   substrate floor — no c₄-absorption, and the AGENTS m_μ-prediction
   narrative is CURRENT. Bean `2i8g` re-scoped to the producer-label
   reconcile only. This label question is now owned by #3280; this PR
   only relabels `C4_S5BB` fit-tier so the producer's in-code comment
   matches.
6. **Cross-A discriminator (owner pick #1 follow-through):** the
   (1−h/2) dressing is a **D-specific scale fix** — fixed a-priori
   candidates (flat, per-interface) leave A≥3 at −59%…−90% while D
   closes to +0.29%; the A≥3 gap is the saturating-Δtr extensive
   deficit, a separate mechanism (jet-filtration channel, PR #3270).
   Scope (a). Producer:
   [`probes/probe_d_dressing_cross_a.py`](../../computations/probes/probe_d_dressing_cross_a.py).

### Verdict

The deuteron's from-scratch chain error is **entirely a binding-scale
question**: nucleon masses contribute +0.0000 MeV (proton anchor) to the
composed m_D while the binding routes span −79%…+33%. The single sharpest
D-specific symbolic lead is the two-sided near-coincidence
`Q_β ≈ m_e·8G·h` (0.06%) ⟺ `Δ_λ(D) ≈ 1/h` (0.12%): if the Q_β/h scale
were *derived* (formalize-first target), the trace-canonical route would
land at +0.12% with zero fits. Per the Δ_λ gate this is NOT wired — it is
recorded as an observation-tier candidate with its invariant question
stated.
