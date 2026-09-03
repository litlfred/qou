# The 26 Standard-Model parameters from QOU — term-by-term status, 2026-09-03

**Bean:** `qou-65jh` (session `qou-ggdk`) · **Branch:** `claude/standard-model-terms-status-ftoejr`
**Scope:** status measurement against the live corpus, on the owner's question
*"a full term by term status update of where we are of driving the 26 terms of
the standard model from qou"*. Not a derivation of any parameter; no number
moves. Where this file and a content block disagree, the block wins and this
file is stale.

**Method.** The clone is shallow (50 commits), so currency was established by
content rather than history: every `sm-params-*` block was hashed
(`sha256(<block>.md)[:12]`) against its `.qa.json` `source_hashes.md`; audits and
beans were read by date and body; every "sorry-free" claim below was re-checked
with a word-bounded grep (`grep -c sorry` is unusable here — it counts the phrase
"sorry-free"); `FormLadderAnchorDominance.lean` was additionally verified
`lean`-direct (exit 0, axioms `[propext, Classical.choice, Quot.sound]`). Two
sub-agents ran the 2026-08-26 → 09-03 sweep and the gauge-coupling witness
verification; their measurements are cited inline. No producer was re-run.

---

## 1. Headline

**1 input, 1 proxy, 1 partial, 2 conjectural, 21 open. Zero derived to
experimental precision.** Unchanged in-paper since 2026-08-14: all eight
parameter blocks match their sidecars byte-for-byte. What has moved since the
standing cheat sheet
([`sm-eightfold-derivation-cheat-sheet.md`](../sm-eightfold-derivation-cheat-sheet.md),
last substantive edit 2026-08-25) is the structure *under* the open rows —
roughly ten new sorry-free negatives, one route-viability positive on
$\alpha_{\mathrm{EM}}$, a partial reversal of the 4-B correction, and one live
contradiction between two in-paper blocks (§8).

Counting convention: 9 charged-fermion masses + 4 CKM + 3 gauge + 2 Higgs + 1
$\theta_{\mathrm{QCD}}$ = 19, plus 7 neutrino = 26; Majorana phases not counted.

Tiers (from [`sm-params-intro.md`](../../content/quantum-observable-universe/appendix-standard-model/sm-params-intro.md)):
`input`, `proxy`, `derived`, `partial`, `conjectural`, `open`; `proved-neg` and
`standard` for the eightfold rows. *Sorry-free ≠ derived; conditional-proved ≠
premise-established.*

## 2. Charged-fermion masses (9)

| # | Parameter | Tier | What exists | What blocks it |
|---|---|---|---|---|
| 1 | $m_e$ | input | CAL-1, the MeV unit | not a prediction |
| 2 | $m_\mu$ | proxy | CAL-2 proxy `m_μ/m_e = Vol(4₁)/ℏ_q²` pins $q_0$ (CODATA-2022 since `fca08de7d29`). Owner ruling 2026-06-30: the muon *carrier* is $T(2,5)$; $4_1$ is the Higgs-mechanism knot | under the canonical proton pin it is a prediction and misses L2 100× by **963.6×** (~210 ppb) — the μ–p tension |
| 3 | $m_\tau$ | open | `prop:tau-leptonic-universality` (ratios, not a mass); direct volume reading refuted over 25 knots (scope-a); complex-volume search sharpened it (#4591, 14.5 bits) | carrier identification. **Zero τ work 2026-08-26 → 09-03** (0 hits for `m_τ`/`tau lepton`/`tau knot` over all 193 audits in that window) |
| 4–5 | $m_u, m_d$ | open | constituents of the Borromean braid; reframing #4602 — confined-quark masses are scheme-dependent renderings. $m_d - m_u$ is extractable: `δ_QCD = Δ_pn + E_EM`, `Δ_pn = 1.2933` MeV derived ([`quark-mass-extraction-stage1.witness.json`](../../computations/quark-mass-extraction-stage1.witness.json)) | `E_EM`, gating object 4-B. $m_u + m_d$ is circular ($m_\pi$ is CAL-3). **The quark charges are asserted, not derived** (`qou-a468`, 2026-08-29): `Q = w/2` is mirror-odd and ranges in $\tfrac12\mathbb{Z}$; [`QuarkBraidChargeObstruction.lean`](../../content/quantum-observable-universe/lean/QOU/StandardModel/QuarkBraidChargeObstruction.lean) closes the braid element as carrier (scope-b); the missing datum is the colour-tube environment label |
| 6 | $m_s$ | open | $(n, T_3)$ separates $s$ from $c$ ([`MesonOperatorSelectionT3.lean`](../../content/quantum-observable-universe/lean/QOU/ParticleInteractions/MesonOperatorSelectionT3.lean), sorry-free) | the content → hyperbolic-braid map (`qou-qpj9`); see §8 for the 4-C contradiction |
| 7 | $m_c$ | open | complex-mass constituent functional (class, no instance); four negatives (#4584, #4594) | as $m_s$; J/ψ-type observables are in mechanism range but no derived $\bar c c$ braid exists (#4608) |
| 8–9 | $m_b, m_t$ | open | nothing | everything |

## 3. CKM (4)

All four open and **unposed**: a mixing matrix presupposes a flavour basis and
the framework fixes no flavour degree of freedom beyond the isospin doublet.
Gated on 4-A. The adjacent derived result, $T_3 = \mathrm{sign}(\kappa)/2$
orthogonal to the generation winding
([`WeakIsospinT3Grading.lean`](../../content/quantum-observable-universe/lean/QOU/ParticleInteractions/WeakIsospinT3Grading.lean),
sorry-free, no axioms, no empirical literals), closes Gell-Mann–Nishijima at its
true width: `hyperchargeLeft_constant` and `gmn_check_has_two_distinct_rows`
prove the six-quark statement collapses to two arithmetic rows, and
`genWinding_finer_than_gmn_data` proves the relation is blind to the generation.

## 4. Gauge couplings (3)

### 4.1 $\alpha_{\mathrm{EM}}$ — `partial`, and three rival constructions

| construction | form | vs CODATA | where |
|---|---|---:|---|
| form ladder — what the appendix states | `1/α = q[9]_q[10]_q + 2g/(4π(g−1)) + αH(1−h²α) + Δ₂`, $g=4$, $H=[2]_q/(8\pi)$, $h = q - q^{-1}$ | quadratic/proton **1.6723 ppb**; cubic/proton **0.3134 ppb** (2.09 σ_α); quadratic/muon 80.51 ppb *at the retired pin A* (81.04 ppb at the live CODATA-2022 anchor) | [`alpha-em-form-ladder.witness.json`](../../computations/alpha-em-form-ladder.witness.json), [`alpha-em-schwinger-ladder.witness.json`](../../computations/alpha-em-schwinger-ladder.witness.json) — reproduced at 70 dps this session |
| Chern–Simons `.md` — what the L2 dashboard consumes via `alpha_em_inv_derived` | `q[9]_q[10]_q·(1 + δ_CS/(1−δ_CS κ))`, κ = det ratio 1.7216 | **−467.6 ppb** | `meson_em_sinh_closed_form.py`; κ graded *conjectural* (`qou-aymm`) |
| Chern–Simons `.lean` — the formalisation the paper cites | `45·[3]_q·(1 + δ + κδ²)`, κ = 8q | **+2.59 ppb** | [`em-coupling-chern-simons.lean`](../../content/quantum-observable-universe/predicted-spectra/em-coupling-chern-simons.lean); its docstring calls κ = 8q post-hoc; `qou-aymm`: ruled out (PSLQ-empirical). The smallest residual belongs to the ruled-out form |

The block's `.md` and `.lean` state formulas 470 ppb apart — a
`proof-statement-integrity` defect (`qou-aemx`, in-progress, high;
[`2026-08-28`](2026-08-28-alpha-em-lean-vs-compute-divergence.md),
[`2026-08-29`](2026-08-29-em-coupling-block-md-lean-divergence.md)). The
`partial` tier is right for the ladder: the three unproved classes are
`ArchimedeanLimit` (one instance, at $x = 0$ only), `BlochSuslinUniqueness` and
`BringZeroModeBlochClass` (zero instances); the per-loop measure $1/(8\pi)$ is
open, phase-4, owner-gated on MOC/Φ (R2 ruled not derived 2026-07-19; Φ proved
not derivable from the $E^4$ model). One advance: the EM holonomy germ is
**live** — $F_q = [\delta q_1, \delta q_2] \neq 0$ on $H_3$ where the binding
germ was sterile ([`2026-08-29`](2026-08-29-alpha-em-germ-viability-live.md));
necessary, not sufficient. Against L2 ($\sigma_\alpha/100 \approx 0.0015$ ppb)
even 0.313 ppb is 209× short. The anchor choice is the residual:
`QOU.AlphaEM.FormLadder.no_anchor_blind_affine_correction_closes_gap` proves no
anchor-blind term absorbs the 78.84 ppb μ–p spread.

Two witness-side notes. The ladder's `assertions[].source` strings are current
(proton-framed); `honest_status.not_at_target` still reads *"best ~81 ppb muon"*
and is the stale field. Both ladder producers hardcode their $q_0$ literals (no
`q_parameter` import) — the muon literal is the retired pin A — and are therefore
invisible to `q0_anchor_manifest`, `q0_anchor_consistency_audit` (filed
`Q0_ANCHOR_MISSING`) and `hardcoded_literal_audit`; their 11 residual fields are
raw float64 (baselined, PR #4677).

### 4.2 $\sin^2\theta_W$ — `conjectural`

Two constructions, different numbers, neither refutes the other. The
pure-pattern Hecke-eigenvalue ratio gives $\cot\theta_W = q_0^{-4}$; the block
[`weinberg-angle-categorical.md`](../../content/quantum-observable-universe/nuclear-interactions/weinberg-angle-categorical.md)
prints **0.6594**, but $q_0^{-4} = 0.65878$ at the live pin — a wrong digit
(the value 0.6594 needs $q = 1.10972$, five orders outside the μ–p tension); the
appendix prints 0.659 correctly and the 64 % miss is unaffected. The
$(3,2,1)$-block construction reaches 0.127 % — the best of **74** swept
candidates, missing the required 1.022386 by $1.30\times10^{-3}$, with
[`close-321-weinberg-gap.witness.json`](../../computations/close-321-weinberg-gap.witness.json)
recording `ansatz_supported_at_1e_3 = false`, `ansatz_falsified_at_1e_2 =
false`, `path_c_status = "inconclusive"`. That producer is float64 end to end
(sympy matrices cast to `np.complex128` and eigen-decomposed; 127 raw-float64
fields) under a witness declaring `engine: sympy`, `compute_dps: 70` — the
verdict is unaffected (thresholds $10^{-3}$, $10^{-2}$) but no digit past ~13 is
meaningful, and no gate in the precision family covers a sympy → numpy route.
The Lean carrier
[`weinberg-angle-categorical.lean`](../../content/quantum-observable-universe/nuclear-interactions/weinberg-angle-categorical.lean)
is **vacuous** — four `def … : Prop := True` fields and a global `trivial`
instance — duplicated in `categorical-higgs-mechanism.lean` and absent from the
vacuity ledger (fixed on this branch, bean `qou-08zf`). A third number,
$1 - ([10]_q/[11]_q)^2 = 0.22998$ (0.369 % off), lives only in
`docs/beta-decay-handoff.md`. The tractable lever is unchanged: Milnor
$\bar\mu_{123}$ separates the two $\mathrm{U}(1)$s
([`SecondCrossingInvariant.lean`](../../content/quantum-observable-universe/lean/QOU/StandardModel/SecondCrossingInvariant.lean),
[`MilnorTripleLinkingMagnus.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/MilnorTripleLinkingMagnus.lean),
sorry-free); the relative normalisation inherits the open flavour sector. The
new block
[`su5-hypercharge-n3-gate.md`](../../content/quantum-observable-universe/appendix-standard-model/su5-hypercharge-n3-gate.md)
observes that under a $2 \oplus 3$ block structure the determinant condition
*forces* $\mathrm{U}(1)_Y$, so hypercharge and the $N = 3$ problem may be one
gap — scoped honestly: nothing occupies that level.

### 4.3 $\alpha_s$ — `open`; the wording "no candidate formula" is stale

Two written expressions exist and neither determines a value.
`computations/alpha_k_selection_rule_conditional.py` writes
$1/\alpha_s = q^{p}[9]_q$ with the bracket writhe-forced and $p$ an undetermined
one-parameter family ($p + p' = 1$); only $\alpha_s \alpha_W = \alpha_{\mathrm{EM}}$
is invariant, it is conditional on `conj:e-hartree-categorical-derivation`, and
it carries no scale. `docs/beta-decay-handoff.md` (March 2026) carries a
fit-shaped $\alpha_s(M_Z) = q^{-1}/[7]_q = 0.11815$ (0.125 % from PDG) — exactly
what bean `qou-5iaz` forbids wiring. Neither appears in `content/`. The block's
substance stands: no fixed-point analogue exists for the colour sector, and the
sector is blocked on the $\mathrm{SU}(3)$ action on the framework's own state
space (`conj:sm-colour-stabilizer-action`: the stabiliser $\mathfrak{su}(3) =
\ker(\mathrm{ev}_e) \subset \mathfrak{g}_2$ has its dimension gate and bracket
closure proved; the action is open). Post-08-25: the $\lambda_a \leftrightarrow
e_a$ generator-identification route is scope-(b) excluded
([`OctonionicSu3RankObstruction.lean`](../../content/quantum-observable-universe/lean/QOU/Eightfold/OctonionicSu3RankObstruction.lean));
no object-level gate separates colour from flavour
([`FlavourColourDiscriminator.lean`](../../content/quantum-observable-universe/lean/QOU/Eightfold/FlavourColourDiscriminator.lean));
on the Brunnian configuration $\Lambda^3$ is the only non-empty channel
([`BrunnianIsotypeExclusion.lean`](../../content/quantum-observable-universe/lean/QOU/StandardModel/BrunnianIsotypeExclusion.lean));
the colour-antisymmetry input is *located* in $\bar\mu_{123}$ (sign
representation of $S_3$, established) but that the *state's* colour channel is
$(1^3)$ is not established
([`2026-08-29`](2026-08-29-colour-antisymmetry-from-milnor-mu-bar.md) §4).

## 5. Higgs sector (2)

$m_H$ — `conjectural`: $H = T(2,8)$, $W = T(2,4)$, $Z = T(2,6)$; torus links
have zero volume, so the chain is Reshetikhin–Turaev at a root of unity with two
open inputs (level selection; invariant → mass); best probes within a factor of
two. $T(2,8)$ is the boson, $4_1$ the mechanism (2026-06-30 ruling).
$v$ — `open`: nothing extracts $v$ or $G_F$; the Yukawa parameterisation and the
framework's volume–density / Hecke-energy chains are unreconciled — a missing
bridge, not a missing number.

## 6. Strong-CP (1)

$\theta_{\mathrm{QCD}}$ — `open`. Ceiling proved:
`theta_qcd_in_zero_pi [ColorSectorCPEven R]` in
[`ThetaQcdFramingCp.lean`](../../content/quantum-observable-universe/lean/QOU/StandardModel/ThetaQcdFramingCp.lean)
(sorry-free, generic base ring). Conditional on a class with no instance — a
$T(2,9)$ gluon knot has writhe $9 \neq 0$, so CP-evenness needs a colour-singlet
writhe cancellation over the $9 = 3 \times 3$ tube structure, which is the open
$\mathrm{SU}(3)$ sector. $\{0, \pi\}$ is a discrete ceiling, not the observed
smallness.

## 7. Neutrino sector (7)

$m_{\nu_{1,2,3}}$ — `open`: carrier the unknot (mirror for the antineutrino),
zero volume, zero mass at leading order, **no mechanism** for the nonzero
masses; the volume–density route is scope-(b) excluded (#4589, $\sim 10^{10}$).
PMNS angles and $\delta_{CP}$ — `open`, unposed as for CKM. Dirac versus
Majorana undistinguished. Three generations is prior to every row and `open`:
$\{3,5,7,9\} \setminus \{9\}$ by continuant harmonicity removes one of four on a
criterion unrelated to generation counting, and the $S_5$ filter gives a
different count; [`generation-completeness.lean`](../../content/quantum-observable-universe/brings-surface/generation-completeness.lean)
is vacuous (`isReachable` inhabited by $r = 0$ for every knot; `qou-0avp`).

## 8. The three gating objects

**4-A — the $N = 3$ flavour object.** Obstruction over-determined (row cap,
volume form, $\mathrm{Sym}^2$ gate); construction missing. Re-posed 2026-08-25:
the $H^1(\mathrm{base}, \mathrm{Aut}^\otimes)$ / band formulation imports
*symmetric* Tannakian duality and the braiding is provably non-symmetric
(`double_braiding_eq_one_iff`), so the question is what the reconstructed Hopf
algebra in $\mathbf{C}$ is. Since then, five sorry-free files:
`SelfDualSectorConfinement` (the required property is **non-self-duality**, a
screening test), `Sym2GateFSTrichotomy` (real and quaternionic constructions
excluded as a class), `OctonionicSu3RankObstruction` (eighth excluded route),
`TrialitySelectionRule`, `FlavourColourDiscriminator`. The live carrier
`qou-y7vg` is stalled at step 1 — naming the base is a decision, not a lookup
(three candidates, two sharing the symbol $R_q$), and both prose carriers of its
premise have no formal content (`CategoricalMordellWeil := trivial`, fixed on
this branch). Ledger: [`eightfold-n3-surface.md`](../coordination/eightfold-n3-surface.md).

**4-B — the intra-nucleon EM self-energy.** The 2026-08-25 correction
(*"cannot be the same object as the mirror front"*) is partially reversed by
channel (`qou-bn8e`, 2026-08-30, merged into `qou-o6ml`): the self channel
$A \sum q_i^2$ does not merge (it cancels in binding), the pairwise channel
$B \sum q_i q_j$ does. Derived ratio on record: $h/[2]_q = \tanh(\ln q_0) =
0.10396371\ldots$; what 4-B owes is the bond that multiplies it. The kernel is
not identified (the `H_coth` contest winner is inadmissible under the O2
zero-mean obstruction; saturation is unreachable below $A \approx 334$) and the
$\alpha \propto A^{1/3}$ separation law is a Euclidean import. New sorry-free
negative: [`ChargeQuadraticSumRule.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/ChargeQuadraticSumRule.lean)
— the quadratic-charge ansatz saturates the octet (bijection, determinant
$-1/3$), so Coleman–Glashow could not have failed; a same-branch "falls out
parameter-free" claim was retracted
([`2026-08-29`](2026-08-29-coleman-glashow-retraction-and-octet-saturation.md)).

**4-C — no third flavour grade is missing** (PR #5770): `orderedContent_injective`
(sorry-free, `by decide`) shows $\bar D^0\,(-5,+3)$ and $K^0\,(+3,-5)$ collide
only as multisets; `mass_from_graded_content_cannot_separate` quantifies over
symmetric functions of the *unordered* content. So 4-C does not reduce into 4-A;
what remains is `qou-qpj9`'s content → hyperbolic-braid map.
**Live contradiction:** [`sm-gating-objects.md`](../../content/quantum-observable-universe/appendix-standard-model/sm-gating-objects.md)
(PR #5744, 2026-08-30) restated *"the missing grade is a genuine third one …
which reduces this object into the first"* five days after #5770 struck it.
Fixed on this branch (`qou-ok51`).

## 9. What is derived, corpus-wide

1. $Q = w/2$ with $c = 1/2$ structurally fixed, and $I_3$ on the nucleon
   doublet — a two-point sign-and-ratio match on $\{p, n\}$; not $I_3$ as an
   output for general states; and per `qou-a468` not the fractional quark
   charges.
2. $T_3 = \mathrm{sign}(\kappa)/2$ orthogonal to the generation winding —
   sorry-free; GMN closure at two-row width.
3. $\alpha_{\mathrm{EM}}$ to 0.313 ppb under the proton pin — `partial`.

Everything else is `standard`, `proved-neg`, `conjectural` or `open`. The
dominant contribution remains deletion: GMO, decuplet equal spacing and
Coleman–Glashow are identities of any first-order octet breaking; the GMO
deviation is now provably under-determined at second order
([`GellMannOkuboSecondOrder.lean`](../../content/quantum-observable-universe/lean/QOU/Eightfold/GellMannOkuboSecondOrder.lean):
two equations, three unknowns, $g$ absorbable — `qou-s4h6`), so the cheat
sheet's rank-3 near-term target drops; the nonet mixing angle is the one
content-bearing eightfold target and is gated on $N = 3$.

## 10. Tower versus order zero (owner question)

Every SM-facing result is a leading-order or single-crossing statement. $Q$ and
$T_3$ are per-crossing data with no tower index — the generation winding *is*
the index, and GMN is proved blind to it. The eightfold results are first-order
octet breaking with the second order under-determined. $\alpha_{\mathrm{EM}}$ is
an order-by-order fixed-point ladder truncated at cubic with $\Delta_2$
uncomputed and the per-loop measure open; the only all-orders object on the
surface is the CS resummation $1/(1 - \delta\kappa)$ with $\kappa$ conjectural.
The central obstruction, $\dim V = 2$, is invariant along the single-fibre
tower, and `su5-hypercharge-n3-gate` proves Wenzl levels are alternatives, not
stages — one fibre occupies one level. There is no all-orders SM derivation.

**Owner ruling, 2026-09-03 (verbatim, from chat):** *"The QOU should be on the full
tower in the derivations to the standard model — should make use of the full tower
even though what is observable is only order zero."* Read here as: the derivation is
to be carried on the fibre-level categorical object in full — the Hecke tower with
the complete Frobenius pairing over all partitions, and all orders of the
fibre-level $q$-expansion — with the observable parameter its order-zero
archimedean rendering at $q_0$. Under that reading every attack in §§2–7 above is
order-zero-only except the Habiro-element route and the Magnus hook-slice result,
and the residual of an order-zero-only construction is not evidence about the
tower. Whether "full tower" means all $n$, all orders in $q$, or both is left to
the owner; this file takes both. Each per-term bean (`qou-bsu0`) carries a *tower
status* line accordingly.

## 11. Corpus defects found, and their disposition

| # | Defect | Where | Disposition |
|---|---|---|---|
| 1 | in-paper 4-C contradiction (third grade "reduces into" 4-A) | `sm-gating-objects.md` | fixed, `qou-ok51` |
| 2 | withdrawn "69 %" mirror claim live; "2/7" L2 count | `coordination/sm-26-parameter-chip-away.md` | fixed, `qou-8y7s` |
| 3 | G1 "still carries 4 of 10,000" (drained by 2026-08-19); four 2026-08-08 beans "still todo" (all completed); Phase 3 and placeholders 3, 5 "planned" (landed); chapter counts | cheat sheet | refreshed, `qou-65jh` |
| 4 | `cot θ_W ≈ 0.6594` where $q_0^{-4} = 0.65878$ | `weinberg-angle-categorical.md` | fixed, `qou-08zf` |
| 5 | vacuous `WeinbergAngleCategorical` carrier + inlined copy | `weinberg-angle-categorical.lean`, `categorical-higgs-mechanism.lean` | fixed, `qou-08zf` |
| 6 | `.md`/`.lean` formula mismatch, 470 ppb; CODATA literal as class content | `em-coupling-chern-simons.lean` | fixed, `qou-08zf` / `qou-8k2y` |
| 7 | `def CategoricalMordellWeil := trivial`; `generation-completeness.lean` vacuous; `UnifiedKnotMass` unsatisfiable | three siblings | fixed, `qou-08zf` |
| 8 | `α_s` "no candidate formula" stale as worded | `sm-params-gauge-couplings.md` | recorded here; block wording is a judgement call left to the author |
| 9 | GMO-deviation "genuine prediction" wording | `eightfold-open-problems.md` item 8 | recorded; follow-up |
| 10 | `sm-params-neutrino.md` "generation counting nowhere addressed" vs `sm-open-problems.md` row | appendix | recorded; follow-up |
| 11 | float64 route sympy → `np.complex128` uncovered by the precision family | `close_321_weinberg_gap.py` | recorded in `compute-precision-auditor` memory; producer fix is a follow-up |

## 12. Cross-references

- Standing reference: [`sm-eightfold-derivation-cheat-sheet.md`](../sm-eightfold-derivation-cheat-sheet.md) (refreshed on this branch).
- Ledgers: [`coordination/sm-26-parameter-chip-away.md`](../coordination/sm-26-parameter-chip-away.md), [`coordination/eightfold-n3-surface.md`](../coordination/eightfold-n3-surface.md).
- Reframing: [`2026-08-02-sm-observable-vs-rendering-reclassification.md`](2026-08-02-sm-observable-vs-rendering-reclassification.md).
- Lean sweep on this surface: `2026-09-03-sm-surface-lean-best-practices-sweep.md` (bean `qou-08zf`).
