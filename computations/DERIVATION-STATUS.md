# BW Mass Formula + 1/α: Derivation Status

## Architecture

All observables derive from the **Hoefsmit scattering pipeline**
(prop:hoefsmit-scattering-pipeline):

```
braid β  →[Hoefsmit ρ_λ]→  Π R-matrices  →[tr_M]→  J_K(q)  →[ω]→  Geom(K)  →[×m_e]→  𝔪
```

Each stage is functorial. The Hecke algebra H_k(q) decomposes via the
Wedderburn-Artin theorem into irreducible blocks indexed by partitions
λ ⊢ k. The Hoefsmit seminormal form gives explicit R-matrix evaluations
for each crossing.

## Core engines

| File | Purpose | Status |
|------|---------|--------|
| `hecke_core.py` | H₃(q) NF multiplication, BW formula, atom construction | **Active** — single source of truth |
| `hecke_characters.py` | Hoefsmit seminormal matrices for any partition at any k | **Active** — sparse matrices for k≤12+ |
| `hoefsmit_witness.py` | Load pre-computed character tables from JSON | **Active** — branching rule, k=3..15 |
| `hoefsmit_witness.json` | Pre-computed character tables | **Active** — 191→1000+ partitions |
| `q_parameter.py` | Substrate parameter q₀ | **Active** — single source of truth |
| `hecke_h4.py` | H₄(q) 24-dim NF multiplication | **Superseded** by hecke_characters.py |
| `youngs_lattice_mass.py` | Young's lattice beam search | **Superseded** by branching rule |

## Proved theorems (this session)

| Proposition | Statement | Proof method |
|------------|-----------|-------------|
| prop:hoefsmit-seminormal-form | T_i acts via a_ρ=h/(1-q^{-2ρ}) | Hecke relation + det=-1 |
| prop:figure-eight-branching-rule | χ(4₁,λ) = (f³+f¹¹¹-f²¹) - f²¹·h² | SymPy symbolic + induction |
| prop:universal-braid-branching | χ(K,λ) = Σ f^{λ/μ}·χ_K^μ for any K,λ | Induction on k + Pieri |
| prop:eigenvalue-product-expansion | ln\|Λ_sym\| = ℓ₂A²/4 + ℓTA - ℓT - ℓ₂T² | Direct eigenvalue algebra |
| prop:geom-yekutieli-alignment | Geom(K) = ⟨ω_A•, S³∖K⟩_Frob | Yekutieli rigidity |
| prop:geom-universality | Geom(K) is unique (additivity+functoriality+normalisation) | Neumann-Zagier + Yekutieli |
| prop:six-term-mass-formula-complete | B_{4₁} = (1-h²)B_bulk + z²[3]/[2]·B_C + z·B_ex | Wedderburn-Artin channels |

## BW Mass Formula: 11 terms at k=5

| # | Term | Coefficient | Scaling | Partition | Status |
|---|------|-------------|---------|-----------|--------|
| 1 | Volume | 2[2][7]m_e | +A | [2,1] h⁰ | DERIVED |
| 2 | Surface | 2[4]²m_e | -A^{2/3} | [2,1] h² boundary | DERIVED |
| 3 | Coulomb | h[6]m_e | -Z(Z-1)/A^{1/3} | [2,1] pp excess | DERIVED |
| 4 | Asymmetry | 3[2][7]m_e | -(N-Z)²/(4A) | [2,1] h¹ Casimir | DERIVED |
| 5 | Pairing | [3][7]m_e | ±1/√A | [3]+[1,1,1] descent | DERIVED |
| 6 | Exchange | [3]/[2]m_e | -Z^{4/3}/A^{1/3} | [2,1] h³ boundary | DERIVED |
| 7 | Shell | [2]²[3]m_e | +f_magic/A^{2/3} | [3,1] branching | DERIVED |
| 8 | Hook | [3]·[2]²·m_e | -(1-f_Z)(1-f_N)A^{1/3} | [2,2] self-conj | DERIVED (q-hook product H_q((2,2)) = [3]·[2]² via prop:wigner-np-pairing; numerically equal to the previous |β₄|·|lnλ| ad-hoc form at q₀ ≈ 6.29 MeV) |
| 9 | Wigner | [5]!·m_e | -T(T+1)/A | [3,1,1] Frob reciprocity | DERIVED |
| 10 | Form factor | h[5]m_e | -Z²/A | [3,2]⊕[2,2,1] conj pair | DERIVED |
| 11 | pn corr | (y_{(4,1)}+y_{(2,1,1,1)})·m_e via Wenzl-bridge n=5 | +ZN/A^{4/3} | [4,1]⊕[2,1,1,1] conj pair | DERIVED (Wenzl-bridge symbolic in ℤ[q^{±1}] via prop:y-lambda-recipe-from-partition; previous "approx" tag obsolete — closed form available at n ≤ 12 per y_lambda_wenzl_bridge_extended.py) |

### Figure-eight modification (A=3 nuclei)

For A=3 (figure-eight topology), three algebraic factors modify the BW:

| Factor | Expression | Value | Scales |
|--------|-----------|-------|--------|
| a | 1-h² = 4-[3]_q | 0.956 | bulk (vol, surf, asym) |
| f_C | z²[3]/[2] | 0.377 | Coulomb |
| f_ex | z = 1/(√q+1/√q) | 0.499 | exchange |

### q-integer coefficient origins

The q-integer [c+1] in each coefficient counts the geometric sum
of eigenvalue powers over c crossings:

  [c+1]_q = Σ_{j=0}^c q^{c-2j}

For Borromean (c=6): [7]. For figure-eight (c=4): [5].

The content sum c(λ) = Σ(j-i) determines the BW scaling:
- c > 0 → A-type (ρ > 0, a_ρ → q)
- c < 0 → Z-type (ρ < 0, a_ρ → -q⁻¹)
- c = 0 → isospin (balanced)

## Fine Structure Constant

> **🛑 CORRECTED 2026-08-21 — the two entries below were the wrong way
> round.** This section labelled the PSLQ-empirical form "Live closed form"
> and the CS tower "Legacy … superseded". The corpus says the opposite:
> `archimedean-functor-uniqueness-context` rules the 45·[3]_q form out
> **structurally** as "a legacy PSLQ-empirical conjecture", while the CS
> tower is what `pyhecke.constants.ALPHA_EM_INV_DERIVED` actually computes
> today. See item 5 of the open-items list below for the full record.

**Best derived form** — the CS tower, exactly resummed
(`pyhecke.constants.ALPHA_EM_INV_DERIVED`; the geometric tower sums in
closed form, so there is no truncation order to choose):

```
1/α = q·[9]_q·[10]_q · (1 + c₁/(1 − c₁κ))
    = 137.0359350939756          (proton pin, the production default)
CODATA-2022: 137.035999177
Residual: −468 ppb — STRUCTURAL (the tower is converged; no further
                     orders can close it)
```

**Ruled out** — not merely superseded:

```
1/α = 45 · [3]_q · (1 + δ_CS + 8q·δ_CS²)   where δ_CS = ℏ_q⁴ · [5]_q
Residual: −2.6 ppb at the proton pin vs CODATA-2022
```

Its residual is the *smallest* of any form here. That is the signature of a
fit, not evidence for it: `archimedean-functor-uniqueness-context` excludes
it structurally for requiring "arbitrary integer ratios … from a
non-pentagon source", and the live table in
`electroweak-higgs-torus-link-triplet-table1-data` still marks it
`open: N_v = ?`.

**Superseding derived form** — bare + the photon IR zero-mode
(`prop:em-coupling-bring-zero-mode`), for completeness:

```
1/α = q·[9]_q·[10]_q + 2/(3π)
    = 137.0354154444              (proton pin)
Residual: −4260 ppb
```

## Current Results (k=5)

```
Mass MAE:      0.006% (45 isotopes, H through U)
³H mass:       0.00001% (figure-eight BW)
³He mass:      0.00000% (figure-eight BW)
Q(³H→³He):     18.23 keV (exp 18.59, 2.0%)
1/α:           137.035998166 (6.7 ppb, within CODATA 21 ppb)
H-H bond:      4.469 eV (0.2%)
```

## Convergence (derived levels k=3..5)

```
k=3: MAE 0.035% (6 terms)
k=4: MAE 0.023% (8 terms) — ÷1.5
k=5: MAE 0.006% (11 terms) — ÷3.6
```

Bound: MAE(k) ≤ 0.035% × [2]²^{-(k-3)}, rate ~4× per level.
k≥6: requires exact Hoefsmit corrections (witness tables ready, k=3..15).
k=13: substrate uncertainty floor (δq from CODATA m_μ/m_e).

## New proposition: BW coefficients as LP shadow prices

**prop:mass-coefficient-shadow-price** (braids-and-knots chapter)

Each BW coefficient is the shadow price (LP dual variable) of the
corresponding partition's Frobenius positivity constraint in the
nuclear operator selection LP.  This closes the derivation loop:

  operator-selection-lp → shadow prices → BW coefficients
  mass-categorical-descent → partition structure → scaling functions
  wedderburn-trace-identity → normalization → trace budget

Corollary: **branching rule for coefficients** — the branching
Res^{H_{k+1}}_{H_k} V_μ = ⊕ V_λ induces a constraint on
level-(k+1) shadow prices via Frobenius reciprocity:

  C_μ = Σ_{λ↗μ} [dim_q(μ) / Σ_{μ':λ↗μ'} dim_q(μ')] · C_λ

This propagates known coefficients from level k to k+1 without fitting.

### Branching-derived k=6 coefficients

Applying the branching rule to the 11 known k=5 coefficients gives
ALL k=6 partition coefficients (in q-integer units, ×m_e for MeV):

| Partition | dim_q | w | c(λ) | C_μ | C_μ·m_e |
|-----------|-------|---|------|-----|---------|
| [3,2,1] (Wigner-2) | 17.35 | 0.359 | 0 | 60.04 | 30.68 MeV |
| [4,1,1]+[3,1,1,1] | 10.67 | 0.136 | ±3 | 38.72 | 19.79 MeV |
| [4,2]+[2,2,1,1] | 9.67 | 0.111 | ±5 | 2.59 | 1.32 MeV |
| [3,3]+[2,2,2] | 5.45 | 0.035 | ±3 | 0.18 | 0.09 MeV |
| others | — | <0.033 | — | <1.3 | <0.6 MeV |

The [3,2,1] coefficient decomposes as:
  C_{321} = 0.448 × [5]! + 0.534 × h[5] + 0.534 × h[5]
          = 58.88 + 0.58 + 0.58
          = 60.04  (98% from Wigner branching)

### Marginal correction (frontier)

The branching gives ABSOLUTE k=6 coefficients, but k=5 already
accounts for 98% of the isospin physics via [5]!.  The NET
correction from k=5→k=6 is the MARGINAL:

  δB_{k6} = Σ_μ C_μ·S_μ - Σ_λ C_λ·S_λ

where S_μ(Z,N,A) and S_λ(Z,N,A) are the k=6 and k=5 scaling
functions respectively.  Since the branching approximately preserves
the total: Σ C_μ·S_μ ≈ Σ C_λ·S_λ, the marginal is sub-MeV —
determined by the scaling-function MISMATCH between levels.

Computing this marginal requires the full spectral LP at H_6(q)
(not just the branching rule), because the scaling functions at
different levels interact non-trivially.

## Calibration discipline (post-2026-05-01 audit)

The framework has **categorically exactly three** external
calibration inputs (per
[`prop:three-calibration-discipline`](../../content/quantum-observable-universe/observations/three-calibration-discipline.md)):

| ID | Calibration | (Co)homology | Role |
|----|-------------|--------------|------|
| **CAL-0** | $m_e$ (CODATA) | $H^0$ | Mass scale |
| **CAL-1** | $m_\mu / m_e$ (CODATA) | $H^1$ | Fixes substrate parameter $q_0$ |
| **CAL-2** | $Q_\beta$ (PDG) | $H^2$ | Weak / β-decay sector ($E_0$ above) |

The substrate parameter $q_0$ is **not** a fitted parameter beyond
this budget; it is the $H^1$ calibration. Any **fourth** external
input is a hard audit failure. The earlier "Energy scale $E_0$:
calibrated, not independently derived" entry is now correctly framed
as the $H^2$ calibration — not an additional fit.

## Open questions (ranked)

1. **k=6 scaling function**: coefficient DERIVED (C_{321}=w·h/2),
   reconciled (shadow price × A(A-1)/2 crossings = branching coeff:
   0.0375 × 1540 = 57.7 ≈ 60.04 for Fe-56).  MAE improved ~1%
   (0.01038% → 0.01030%).  BUT: scaling is NOT T(T+1)/A^{4/3} —
   character data shows N=Z nuclei also contribute (m_{321} ≠ 0
   for ⁴He, ¹²C, ⁴⁰Ca).  Correct scaling requires the full
   character polynomial in Z,N,A from the symbolic computation.
2. **Q-values for A≥4**: BW at k=5 gives keV-scale errors in mass DIFFERENCES.
   Needs k≥7 exact corrections.
3. **Magic numbers**: {2,8,20,28,50,82,126} from Bring's surface
   — algebraic claim now stated as
   [`conj:magic-numbers-bring`](../../content/quantum-observable-universe/algebraic-substrate/magic-numbers-bring.md)
   (P1.4 path-(b)): the seven values are conjectured to be the
   ranks of distinguished $S_5 \times \langle\hat\tau\rangle$-stable
   period sub-lattices on Bring's surface. Path-(a) proof
   (concrete period-lattice construction + bijection) remains
   open. Equivalent under Yekutieli rigidity to
   `conj:categorical-neutrality-saturated-shells` and
   `conj:homological-shell-condensation`; the three are three
   models of the same conjectural surface.
4. **Molecular binding beyond H-H**: vertex-volume method fails for multi-electron atoms.
5. **1/α residual**: **OPEN.** The best *derived* form sits at
   **−468 ppb** against CODATA-2022 at the proton pin.

   > **🛑 CORRECTED 2026-08-21.** This item previously read
   > *"~~399 ppb~~ — **resolved at 6.7 ppb** … no further derivation
   > required"*, citing the closed form
   > $1/\alpha_{EM} = 45 \cdot [3]_q \cdot (1 + \delta_{CS} + 8q\delta_{CS}^2)$,
   > $\delta_{CS} = \hbar_q^4[5]_q$. **That form is structurally ruled out
   > by the corpus itself**, and the entry mis-attributed it besides:
   >
   > - [`archimedean-functor-uniqueness-context`](../content/quantum-observable-universe/mass-theory/archimedean-functor-uniqueness-context.md)
   >   calls it *"a legacy PSLQ-empirical conjecture, since superseded by
   >   `prop:em-coupling-bring-zero-mode`"*, requiring *"arbitrary integer
   >   ratios … that would have to come from a non-pentagon source"*, and
   >   *"ruled out **structurally** in addition to the existing PSLQ
   >   ruling."*
   > - The live table in
   >   [`electroweak-higgs-torus-link-triplet-table1-data`](../content/quantum-observable-universe/knots-particles-confinement/electroweak-higgs-torus-link-triplet-table1-data.md)
   >   carries the same form marked **`open: N_v = ?`**.
   > - `prop:alpha-em-categorical-trace`, the label cited as its source,
   >   contains **no such formula**. That proposition is an *identity* —
   >   $\alpha_{EM} = h^2/(q\,\delta_q(T_{2,9})\,\delta_q(T_{3,5}))$ —
   >   decomposing the **bare** coupling $q[9]_q[10]_q$, which is 0.155 %
   >   from CODATA. Its "match to $10^{-12}$" is the identity closing, not
   >   a prediction of the measured $\alpha$.
   > - Every *"✅ resolved"* corroboration lives under
   >   `docs/audits/_deprecated/`.
   > - The quoted 6.7 ppb is muon-pinned **and** measured against CODATA-
   >   **2018** (`137.035999084`; 2022 is `137.035999177`).
   >
   > The residual being *smallest* for the ruled-out form is the expected
   > signature of a fit, not evidence for it — which is why "resolved …
   > no further derivation required" was the damaging phrasing.

   Measured at the proton pin (the production default) against
   CODATA-2022 `137.035999177`:

   | form | status | residual |
   |---|---|---|
   | bare $q[9]_q[10]_q$ | derived | −0.155 % |
   | bare $+\,2/(3\pi)$ photon IR zero-mode (`prop:em-coupling-bring-zero-mode`, the superseding form) | derived | **−4260 ppb** |
   | CS tower, exactly resummed (`pyhecke.constants.ALPHA_EM_INV_DERIVED`) | derived | **−468 ppb** |
   | $45[3]_q(1+\delta_{CS}+8q\delta_{CS}^2)$ | **ruled out** (PSLQ-empirical) | −2.6 ppb |

   `pyhecke/constants.py` describes its −468 ppb as **structural**: the CS
   tower is geometric with ratio $c_1\kappa \approx 2.7\times10^{-3}$ and
   sums in closed form, so no further orders can close the gap. That is the
   honest state of this item — and it contradicted this entry's "resolved"
   for as long as both were live.
6. **Energy scale E₀**: calibrated as the $H^2$ input (CAL-2 = $Q_\beta$).
7. **Neutrino mass**: ν = unknot ($K_{0_1}$); $J_\nu(q)=1$; bare-knot
   mass = 0. The framework predicts $m_\nu \sim \mu_0\cdot(q-1)$
   (vacuum drag, not knot topology — see
   `content/.../archimedean-universe/neutrino-knot.md`). The earlier
   "wrong by 10⁶" claim was a neutron/neutrino confusion (comparing
   neutrino against neutron mass) and is **withdrawn**.

## Audit closures (2026-05-01 / 2026-05-02)

| ID | Status | Notes |
|----|--------|-------|
| **CAL-0/1/2** | 🟢 declared | Three-calibration discipline (P0.4 landed) |
| **SUB-1** ($q_0$) | 🟢 = CAL-1 | $H^1$ calibration; `q_parameter.py` + `q_pinning_50_digit.py` derive $q_0$ from a single CODATA $m_\mu/m_e$ input — no separate fit-against-mass-tower step exists. P1.1(b) confirmed in place. |
| **NU-1** | 🟢 withdrawn | Neutrino = unknot; bare mass = 0 (P1.6 audit) |
| **SHELL-1** | 🟢 cleared | Compound-shell calibration *is* CAL-2 (P1.5 audit) |
| **JSJ-link 8** | 🟢 algebraic recast landed | Hecke $J^\bullet$-stratification (P0.3) |
| **BW-8** | 🟢 closed | Wenzl-bridge q-hook product; live derivation in `wigner-np-pairing`. |
| **BW-11** | 🟢 closed | Wenzl-bridge closed form $(y_{(4,1)} + y_{(2,1,1,1)})\,m_e$ at $n=5$. |
| **MAG-1** | 🟢 6/7 derived/verified | Hoefsmit $\{2,8,20,28\}$ + PR #499 self-conjugate witness $\{50,82\}$ + PR #500 homological framework; only $Z=126$ pending (cron compute). The "only on the magic ladder" claim is `conj:homological-shell-condensation`. |
| **ALPHA-2** (1/α residual) | 🔴 OPEN | **Corrected 2026-08-21** (was "🟢 closed at 6.7 ppb … no further derivation required"). The 6.7 ppb belonged to the `45[3]_q(1+δ_CS+8qδ_CS²)` form, which the corpus rules out **structurally** as PSLQ-empirical; it was also muon-pinned and scored against CODATA-2018. Best derived form is −468 ppb (CS tower, structural). See item 5. |

See [`docs/audits/2026-05-01-math-framework-deep-audit.md`](../../docs/audits/2026-05-01-math-framework-deep-audit.md)
for the full audit and
[`docs/audits/2026-05-01-math-framework-workplan.md`](../../docs/audits/2026-05-01-math-framework-workplan.md)
for the priority queue.  Open conjectures and their downstream cones
are tracked in
[`docs/audits/conjecture-cones.md`](../../docs/audits/conjecture-cones.md).
