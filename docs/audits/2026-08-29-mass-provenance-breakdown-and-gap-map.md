# Mass provenance — complete breakdown and expected-gap map (2026-08-29)

Owner questions driving this audit: *is mass produced by knot operators? what are
the SDP knot operators? is there an operator intertwining the odd and even
channels? show the SDP story for hydrogen (p + e), deuterium, tritium, helium,
with predicted vs observed; where does the mass come from and where should the
gaps be?* Companion artifacts: the `/dashboard-low` run captured below (proton
pin, 2026-08-29), the Murakami citation wiring
(`rem:torus-knot-zero-volume-via-reeb`, `ex:topological-mass-trefoil`), and
[2026-07-02-torus-knot-papers-usability-analysis.md](2026-07-02-torus-knot-papers-usability-analysis.md).

## 1. Where the mass comes from — the provenance ladder

Every MeV number in the corpus descends this ladder. Provenance tags follow the
dashboard's own legend (`MEASURED` / `CAL` / `DERIVED` / `DERIVED*` / `POSITED`
/ `EXPLORATORY`).

| Rung | Object | Formula / source | Tag | Current accuracy |
|---|---|---|---|---|
| 0 | $m_e$ | CODATA input (CAL-1) — the unit | CAL | exact by construction |
| 1 | $q_0$ | **proton pin** $m_p/m_e$ (owner 2026-08-07/15); $q_0 = 1.10997858275138\ldots$ | CAL | 0.06 ppb (experimental) |
| 2 | $m_\mu$ | $m_e \cdot \mathrm{Vol}(4_1)/\hbar_q^2$ — at the proton pin this is a **prediction**, not an anchor | DERIVED | ~210 ppb (the μ–p tension) |
| 3 | $m_p$ | $2(m_\mu F_{\mathrm{Bor}} - 6m_e)$, $F_{\mathrm{Bor}} = \lvert\mathrm{tr}_M(\beta_{\mathrm{Bor}})\rvert\,[3]_q!/q^3$ | DERIVED | $-0.003$ ppb — but see §1a |
| 4 | $Q_\beta$ | Kashiwara $b^2$, parameter-free | DERIVED | +602 ppm |
| 5 | $m_n$ | $m_p + Q_\beta + m_e$ | DERIVED | **+501 ppb — FAILS its own 10 ppb witness assertion** (`allPassed: false`) |
| 6 | $B(A,Z)$ nuclear binding | production $B_{\mathrm{sym}} = \alpha\ln(\mathrm{tr}_{\mathrm{free}}/\mathrm{tr}_{\mathrm{atom}})$, $\alpha = E_0 = m_e/(q_0(q_0-1)) \approx 4.186$ MeV | **POSITED** | err 0.79× (²H) → 3.26× (⁴He) |
| 6′ | $B$ alternates | $B_{\mathrm{can}^0}$ (Borromean tower, DERIVED, wrong magnitude — the Δ_λ frontier); $B_{q\mathrm{CLT_{fac}}}$ (POSITED); $E_C$ Coulomb (DERIVED*, conditional on the Witten-κ `sorry`); $B_{\mathrm{gate}}/B_{\mathrm{vol}}$ (deprecated 2026-08-08, non-derived, still printed) | mixed | see §3 tables |
| 7 | $M_{\mathrm{nuclear}}$ | $Z\,m_{p,\mathrm{can}} + N\,m_{n,\mathrm{can}} - B$ | inherits 5+6 | ppm-scale and worse |
| 8 | $M_{\mathrm{atom}}$ | $+ Z m_e - B_{\mathrm{el}}(Z)$, $B_{\mathrm{el}}$ = AME Lunney–Pearson empirical fit | **MEASURED (imported)** | H-atom −0.91 ppb |

Standing owner rulings shaping the ladder: **ABSOLUTE MASS EXCISED**
(2026-08-11) — $m_p \approx 938.27$ MeV is an $m_e$-scaled rendering of a
dimensionless ratio, not a framework prediction; report ratios, bindings,
$Q_\beta$, $\Delta_{pn}$. The muon anchor itself was re-pinned A → C
(CODATA-2022-derived, 2026-08-22); 83 witnesses / 75 producers remain to drain
(`2026-08-29-q0-muon-anchor-repin-drain.md`).

### 1a. Honesty note on the rung-3 "0.003 ppb"

With $q_0$ on the proton pin, the $m_p$ match is the **calibration echo** —
$q_0$ was solved from $m_p/m_e$, so reproducing $m_p$ certifies only internal
consistency. The genuine predictions at the nucleon level are $m_n$ (via
$Q_\beta$; currently 501 ppb, failing its assertion) and $m_\mu$ (~210 ppb,
the 9.5σ μ–p substrate tension). Any "N ppb" claim quoted for $m_p$ without
this caveat is the CAL tautology the L2 discipline forbids.

## 2. Is mass produced by knot operators? What the SDP actually does

**No — mass is not computed by the SDP knot operators.** The division of labor:

- **Mass** comes from the muon-anchored Hecke energy (rungs 2–5): one Markov
  trace $\mathrm{tr}_M(\beta_{\mathrm{Bor}})$ of the fixed Borromean braid,
  through the single facade `computations/canonical_mass.py`, which reads the
  witness `m-p-substrate-identity-50dps.witness.json` and deliberately has no
  formula fallback. No LP/SDP anywhere in its cone.
- **The SDP layer** (`mba-step10-confinement-sdp.md`, solver
  `pyhecke.lp_dual_solver`) solves
  $\min \sum_i t_i x_i$ s.t. $\mathrm{net}(x) = n_{\mathrm{target}}$,
  $Gx \ge 0$, $x \ge 0$ with $t_i = \mathrm{tr}_M(b_i)$,
  $G_{ij} = \mathrm{tr}_M(b_i b_j)$. Its primal optimum **is** the canonical
  $T_w$ (that is what "canonical $T_w$" means operationally); its duals
  $y^*_i$ are the **binding-energy shadow prices**, and the active set
  $\{i : y^*_i > 0\}$ names the receptive sub-braids (Wedderburn channels) the
  bound state saturates. The isotope enters only through
  $n_{\mathrm{target}} = \lvert\mathrm{tr}_M(W_{\mathrm{atom}})\rvert$.
- Two structural facts bound what the SDP can ever do: (i) the full
  $H_{12}$-level Wedderburn LP is **trivial** — the central idempotents are
  orthogonal, so $\mathrm{tr}_M = \sum_\lambda y_\lambda \chi_\lambda$ is
  unique and there is no selection freedom (genuine freedom lives only in the
  non-orthogonal $H_3$ 6-element basis); (ii) the per-isotope knot-ID SDP is a
  **feasibility check with no objective** and cannot select knots — the
  assignments are an admitted AME-driven census fit
  (`2026-08-25-knot-id-is-an-admitted-fit.md`).
- The Lean uniqueness theorems (`NucleusEmptySDPUniqueness.lean`:
  `deuteron/tritium/helium3_uniqueness_closed`) certify $T_w$ uniqueness at the
  **abstract empty-constraint level only**; the real per-nucleus SDP with
  Littlewood–Richardson color-flavor constraints
  $H_{3A} \supset (H_3)^{\otimes Z} \times (H_3)^{\otimes N}$ is open work.

**Per-isotope SDP witnesses exist for exactly the chain the owner asked
about**: `nucleus-real-sdp-{proton, neutron, deuteron, tritium, he3, he4}.witness.json`.
Deuteron ($H_6$, 11 Wedderburn blocks): $\mathrm{tr}_M = 0.38836$,
$n_{\mathrm{target}} = 0.38773$, strong duality holds with gap
$8.1\times10^{-43}$; active blocks
$(2,1^4), (2,2,2), (3,3), (4,1,1), (4,2), (5,1), (6)$ — the self-conjugate
$(3,2,1)$ is the one block priced at zero, and the negative-norm blocks are
exactly the conjugates with flipped q-trace sign: the bar-involution / Type-B
fold signature showing up inside the SDP.

## 3. Predicted vs observed — H, D, T, He (the `/dashboard-low` run)

Fresh run, proton pin, 2026-08-29 (log:
`mass_binding_dashboard.py --group low`). **Hydrogen is present**: the atomic
table's $Z=1$ row **is** ¹H = p + e (electron layer $Z m_e - B_{\mathrm{el}}$).

Nuclear binding (MeV; err = $B_{\mathrm{AME}}/B$, 1.00 = perfect):

| iso | $B_{\mathrm{AME}}$ | $B_{\mathrm{sym}}$ | err sym | $B_{\mathrm{can}^0}$ | err can⁰ | $B_{q\mathrm{CLT_{fac}}}$ | $E_C$ |
|---|---:|---:|---:|---:|---:|---:|---:|
| ²H | 2.22 | 2.83 | 0.79 | 2.33 | 0.95 | 2.83 | 0.00 |
| ³H | 8.48 | 6.14 | 1.38 | 3.60 | 2.36 | 5.98 | 0.00 |
| ³He | 7.72 | 5.37 | 1.44 | 3.92 | 1.97 | 5.47 | 0.85 |
| ⁴He | 28.30 | 8.68 | **3.26** | 4.69 | **6.04** | 8.59 | 0.77 |

Atomic masses (vs raw neutral-atom AME):

| iso | $M_{\mathrm{atom}}^{\mathrm{AME}}$ | $M_{\mathrm{atom}}^{\mathrm{pred(sym)}}$ | err |
|---|---:|---:|---:|
| ¹H (p row) | 938.783 | 938.783 | **−0.91 ppb** |
| ²H | 1876.124 | 1875.516 | −324 ppm |
| ³H | 2809.432 | 2811.775 | +834 ppm |
| ⁴He | 3728.401 | 3748.017 | +5261 ppm |

Reading: the ¹H ppb-level match is **not** a binding success — it is the
proton-pin echo (§1a) plus an **imported** electron layer (§5). From ²H on,
the error is binding-dominated and grows with A; ⁴He is the catastrophic row.
The bar-involution split (dashboard Table 4) is live here too: the
entanglement-augmented $B_{\mathrm{sym+ent}}$ improves ²H (0.79 → 0.56 err
direction) and ³H (1.38 → 1.06) but leaves ⁴He at 2.57.

## 4. Fusion channels — D + T → ⁴He + n, and why the sign comes out wrong

**No reaction/channel model exists on main** (the only reaction-shaped compute,
`borromean-qvalue.py`, is deprecated). Fusion Q-values are therefore pure
bookkeeping — differences of the per-isotope bindings above (nucleon counts
balance in each channel, so constituent masses cancel exactly):

| Channel | $Q_{\mathrm{obs}}$ | via $B_{\mathrm{AME}}$ | via $B_{\mathrm{sym}}$ | via $B_{\mathrm{sym+ent}}$ | via $B_{\mathrm{can}^0}$ |
|---|---:|---:|---:|---:|---:|
| p + n → ²H + γ | +2.22 | +2.22 | +2.83 | +4.00 | +2.33 |
| D + D → ³He + n | +3.27 | +3.28 | **−0.29** | **−0.77** | **−0.74** |
| D + D → ³H + p | +4.03 | +4.04 | +0.48 | +0.00 | **−1.06** |
| **D + T → ⁴He + n** | **+17.59** | +17.60 | **−0.29** | **−0.97** | **−1.24** |

The AME column confirms the bookkeeping is exact; the model columns show the
central structural fact: **a fusion Q-value is a small difference of same-order
bindings, so it amplifies per-isotope binding error without mercy.** D+T comes
out *endothermic* in every current form because ⁴He is under-bound 3.26× —
the entire +17.6 MeV lives in the magic-closure physics the production forms
miss. Until the ⁴He row closes, every fusion channel involving it will have
the wrong sign; this is the single highest-leverage number in the light-nuclei
program. (The SU(4) occupancy form $B_{\mathrm{gate}}$ — parameter-free
$E_0\ln(1/W_\lambda)$ — fixes ⁴He specifically, err 0.94, but over-binds ²H
and is deprecated as a production form; the reconciliation of the two is the
Δ_λ frontier.)

An SDP *channel model* of fusion (initial-state vs final-state active-set
comparison, e.g. the D and T duals against the ⁴He + n duals) does not exist
and would be new research; the ingredients (per-isotope duals) are all present.

## 5. The electron layer — ¹H's 13.6 eV is imported

The dashboard's $B_{\mathrm{el}}(Z) = 1.44381\times10^{-5}Z^{2.39} +
1.55468\times10^{-12}Z^{5.35}$ MeV is the AME empirical fit — **measured, not
derived**. The framework route exists (`atom_electron_mass.py`: Hartree scale
$E_h = \alpha_{EM}^2 m_e c^2$ with the QOU-derived
$\alpha_{EM} = 1/(q[9]_q[10]_q)$, reproducing Ry ≈ 13.6 eV for Z=1) but is
diagnostic-only, emits no witness, and leaves $Z_{\mathrm{eff}}$ screening
open. So the ¹H SDP story the owner asked for splits: the **nuclear** side (p
as its own SDP subject) is witnessed; the **atomic** bound state p + e is
bookkeeping with an imported binding. Promoting `atom_electron_mass.py` to a
witnessed producer and swapping it in for the AME fit is the concrete closure
path.

## 6. The odd/even channels and their intertwiner

The channels are the bar-involution ($q \mapsto q^{-1}$) parities of the
$\sigma_i$ eigenvalue pair $q, -q^{-1}$: **bar-even** $(q+q^{-1})/2 = \cosh\lambda$
= binding / volume / retained energy; **bar-odd** $(q-q^{-1})/2 = \sinh\lambda$
= $Q_\beta$ / Chern–Simons / emitted energy
(`conj:binding-qbeta-complex-volume`: $\mathfrak{E}_{\mathrm{bind}} =
\mathrm{Re}\,\mathfrak{V}$, $\mathfrak{Q}_\beta = \mathrm{Im}\,\mathfrak{V}$).

**Yes, an intertwiner exists and is already proved sorry-free**, at three
levels in `binding-qbeta-complex-volume.lean`:

1. **`rotation_step`** — a sequence satisfies the odd-channel ($q^{-1}$-Hermite)
   recurrence at $(q,x)$ **iff** its $\iota$-rotation $n \mapsto \iota^n h_n$
   ($\iota^2 = -1$, fibre-level) satisfies the even-channel (continuous
   q-Hermite) recurrence at bar-conjugated data $(\sigma q, \iota x)$ — the
   categorical Askey / Ismail–Masson rotation
   $h_n(x|q) = i^{-n}H_n(ix|q^{-1})$. One recurrence, two channels.
2. **`invol_descent` / `recurrence_invol_descent`** — the bar involution itself
   is the intertwiner: one relation over a commutative ring with involution
   descends to both parity identities.
3. **Physically**, the bar involution is **isospin conjugation**
   (`2026-08-19-bar-involution-is-isospin-conjugation.md`): all bar parity
   lives in the braid *word* (the Wedderburn weights $y_\lambda$ are exactly
   bar-even, bit-identical under $q \mapsto 1/q$), and bar exchanges mirror
   nuclei. Inside the deuteron SDP the fold appears as the conjugate-block
   sign flip (§2).

What remains conjectural on this axis: the complex-volume **unification**
itself, the ζ₄-faithful single-$\mathfrak{V}$ assembly, the Stage-C σ₃-lift
$c_4$ rungs (blocking the decisive Casoratian $W_3$ sign test), and the map
$u(q_0)$. And one sharp negative: the bar-norm mass modulus **does not exist
as a real number** for the current atom word — both bar products are negative.

**Knot-operations table**: the operations ↔ algebra dictionary is scattered
across ~7 homes (Hecke normal-form tables 1–2, the atlas-registry closure
operators, transfer-matrix connected sum, Markov moves as cosimplicial
directions, cabling in Lean, mirror in the MBA sidecar). No single unified
block exists; **satellite** is the genuine hole — `Geom(K)` has no satellite
case (QA-flagged), and `nuclear-knot-classification.lean` hardcodes
`.satellite` to a Borromean default.

## 7. Expected-gap map — where the gaps should be, and why

Ordered by leverage; "expected" = the structure itself predicts the gap sits
here, so effort elsewhere is misallocated until these move.

| # | Gap | Why it is expected structurally | Blocking / owner-gated? |
|---|---|---|---|
| G1 | **⁴He magic closure** (err 3.26 on production; flips every fusion sign) | closure selection is the one place the trivial-LP argument does NOT apply — per-λ normalization $\Delta_\lambda$ is the admitted open frontier; $B_{\mathrm{gate}}$'s parameter-free success at exactly the magic row localizes the missing physics in $W_\lambda$ occupancy, not in the trace | Δ_λ gate (no 7th fit ansatz) |
| G2 | **$Q_\beta$ at +602 ppm → $m_n$ at 501 ppb** (witness assertion RED) | $Q_\beta$ is bar-odd — the channel whose exact ladder ($c_4$ rungs, σ₃-lift) is the named open obligation of the complex-volume conjecture | gated on s5bb Habiro keystone |
| G3 | **Binding energy-license** ($B_{\mathrm{sym}}$ POSITED) | extensivity is derived (Markov property) but nothing licenses $\alpha\ln(\cdot)$ as an energy; the licensed form ($E_0\times$ trace difference) is $B_{\mathrm{can}^0}$, which has the wrong magnitude — same Δ_λ frontier as G1 | — |
| G4 | **Electron layer imported** (13.6 eV from AME fit) | the framework has no witnessed EM bound-state producer; the α_EM-Hartree route exists but is diagnostic | small, unblocked |
| G5 | **No reaction/channel model** (fusion, capture) | corpus is static per-isotope by design; Q-values are differences — meaningful only once G1 closes | new research |
| G6 | **Knot-ID is a census fit** | the ID SDP has no objective, so it cannot select; expected until a variational principle (or the s5-so3 geometric $W_\lambda$ build) supplies one | owner-scoped (s5-so3 lane) |
| G7 | **q₀ muon-anchor drain unfinished** (83 witnesses; AGENTS.md itself stale, bean `qou-mpin`) | double re-pin (proton default 08-07, A→C 08-22) landed mid-corpus; mechanical, not conceptual | mechanical drain |
| G8 | **Satellite operation undefined** under `Geom(K)` | the operations dictionary grew per-operation; satellite was never load-bearing for A ≤ 7 — becomes load-bearing for composite/cluster nuclei | — |

The through-line: **G1 and G2 are the same two channels as §6** — G1 is the
bar-even (binding) channel's missing normalization, G2 the bar-odd channel's
missing exact ladder. The complex-volume conjecture predicts they close
together or not at all; that is the falsifiable structural bet the corpus is
currently carrying.

## 8. Actions taken with this audit

1. `murakami2004a` de-orphaned: substantive two-branch note in
   `references.ts`; cited from `rem:torus-knot-zero-volume-via-reeb` and
   `ex:topological-mass-trefoil`; ledger row backfilled
   (`bib-qa-verifications.json` id null → `murakami2004a`).
2. `ex:topological-mass-trefoil` reconciled to the 2026-06-30 owner ruling
   ($4_1$ = Higgs, not muon) and the Li₂ "interpolation of the volume" claim
   retracted per Murakami Thm 1.1 (authorNote records the change; the ≈112
   value kept as the CAL-1 natural-units rendering). Resolves the
   contradiction logged in `topological-field-ansatz-table-data.qa.json`.
3. `/dashboard-low` re-run at head (proton pin); output archived in the PR.
   Fusion bookkeeping table (§4) computed from it.
4. Follow-up beans: fusion-channel SDP comparison (research), e-layer
   promotion (G4), plus the pre-existing q₀-drain and Δ_λ tracks.

Validation note: the folio-assistant pipeline is not available in this
sandbox; the two edited `.md` blocks passed the manual render battery
(balanced delimiters, no `\operatorname`, no display-math list hijack) and the
`.ts`/JSON files parse, but the change was **not machine-validated** by the
content pipeline — CI will run it.
