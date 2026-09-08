# L2 / 1 ppQ — the research program, its gaps, and where each is being closed (2026-09-08)

**Tier:** coordination + audit (no new mathematics). Written on
`claude/l2-1-ppq-gaps-c9zuwt` (PR #7159) at the owner's request: *"what do we need to
do to get to L2 1 ppQ? Walk through the canonical derivation of mass and binding. List
exactly what the gaps are and where we are trying to close them … what is the status of
Q_β, c₃ or the f-map? What are the open conjectures? … articulate the research program
cohesively and see what are the priority gaps to close."*

**Provenance key used throughout.** `[W]` carried from a committed witness on
`origin/main` (with `computedAt`); `[M]` measured this session (git / grep / exact
arithmetic on witness fields); `[D]` carried from a cited audit doc or Lean file;
`[PR]` an open sibling PR not yet on `main`. No producer was re-run: `mpmath` is absent
from this container, so every number is the committed witness, not a fresh run.

---

## 0. The headline, and what "L2 1 ppQ" actually means

**"L2 1 ppQ" conflates two targets, and the distinction changes what has to be done.**

| leg | target | live status |
|---|---|---|
| **L1 — compute precision** | cross-method agreement ≤ 1 ppQ (10⁻¹⁵) at the substrate q₀ | **met**: 6 atoms, peel-vs-χ agreement 6e-50 … 1.2e-49 `[W]` (`onepb-status-dashboard`, 2026-08-30; `cross-check-trM-1ppb`, 2026-09-07). Two caveats in §5. |
| **L2 — per-observable accuracy** | for each predicted observable O, σ_theory(O) ≤ σ_exp(O)/100 | **1 of 6 scoreable (m_K/m_π), 0 of 6 unconditional** `[W]` 2026-09-07. |
| **σ_theory at 1 ppQ** (the owner's underlying goal, precision-goals.md §"reframe") | every residual becomes calibration-limited | residuals are 10⁴–10⁹ above 1 ppQ, and **every one traces to an un-derived object, not to compute** (§1.2). |

So L2 is never "1 ppQ": the tightest per-observable target is 1.5 ppt (α_em⁻¹) and the
loosest 264 ppb (m_K/m_π). What the owner is really asking is *which un-derived objects
stand between the chain and calibration-limited residuals*. That is the list in §6.

**The count moved on 2026-09-07 and the docs have not caught up.** Commit `d626761a34`
(bean `qou-37j2`) added `alpha_em_inv` to the L2 dashboard; `scoreable_total` went 5 → 6.
`docs/precision-goals.md` (lines 38, 240, 256, 265–267, 588) and `AGENTS.md` (lines
2373, 2421, 3112) still say 1/5. The unconditional count stays **0/6** under the
2026-08-22 red-team (`m_K/m_π` clears only through an α_em term resting on an open
`sorry`).

### Lineage — this is the sixth programme articulation in 25 days; the other five are

| date | bean | document | what it settled | what this doc adds over it |
|---|---|---|---|---|
| 08-14 | `1qug` | `sm-eightfold-derivation-cheat-sheet.md` | SM-26 parameter status | — (different scope) |
| 08-18 | — | `2026-08-18-mass-binding-accuracy-what-is-closeable.md` | 1/5 scoreable recount; ℓ¹ ceiling on Δ_λ re-weighting | superseded by 09-07 as status |
| 08-29 | `vibo` | `2026-08-29-mass-provenance-breakdown-and-gap-map.md` | the provenance ladder; expected-gap map G1–G8 | §2 here maps the *chosen joints* the ladder passes over |
| 08-30 | `m2ay` | canonical-derivation magnitude cheat sheet | magnitude table | — |
| 09-03 | `ggdk`/`65jh` | `2026-09-03-sm-26-term-status.md` | 1 input / 1 proxy / 1 partial / 21 open; the three gating objects | — (SM scope) |
| 09-07 | `37j2` | `2026-09-07-1ppq-reanalysis-what-moved-and-what-to-attack.md` | the three walls W1–W3; ranked attack list; α_em on the dashboard | this doc **agrees with its walls and ranking** and adds: the per-step proved/chosen map of the mass chain (§2), the binding structural status (§3), the conjecture / assumed-form inventory (§5), and the thread-level coordination analysis (§6) |

None of the five cites a predecessor (§6.3 item 4). This one does, and its §7 ranking is stated
as a *delta* against the 09-07 list rather than a fresh list.


---

## 1. Live L2 status and where each residual comes from

### 1.1 The dashboard `[W]` — `per-observable-100x-status.witness.json`

`computedAt 2026-09-07T12:39:23Z`, `scriptHash 66f1e9466de8`, proton pin
`q₀ = 1.10997858275138080759…`, 70/60 dps. Q_β rows are stamped `INHERITED_C`
(canonical convention is D) and `INADMISSIBLE_FUNCTIONAL` (`z = 1`).

| obs | pred | CODATA/PDG | err (ppb) | σ_exp (ppb) | target σ/100 (ppb) | miss | scored? |
|---|---|---|---:|---:|---:|---:|---|
| m_p | 938.272089427 | 938.272089430 | 0.0029 | 0.309 | 0.0031 | N/A | no — anchor round-trip |
| m_e | 0.510998950690 | same | 0 (defined) | 0.313 | 0.0031 | N/A | no — CAL-1 input |
| m_μ | 105.658397811 | 105.658375496 | **211.2** | 21.77 | 0.2177 | **970.2×** | yes |
| Q_β | 0.782334410278 | 0.782333410 | **1279** | 779.7 | 7.797 | **164.0×** | yes |
| m_n | 939.565422788 | 939.565421940 | **0.903** | 0.511 | 0.0051 | **176.7×** | yes |
| Δ_pn | 1.29333336097 | 1.29333251 | **658.0** | 433.6 | 4.336 | **151.7×** | yes |
| α_em⁻¹ | 137.035999127 | 137.035999177 | **0.365** | 0.153 | 0.0015 | **238.3×** | yes (added 2026-09-07) |
| m_K/m_π | 3.53711862102 | 3.53711843895 | 51.5 | 26 364 | 263.6 | 0.195× (meets, 5.1× margin) | yes |

Quote `beats_100x_scoreable = 1 / scoreable_total = 6`. `beats_100x_count = 2` counts the
two inputs and must not be quoted (AGENTS.md STRICT). There are **no binding-energy rows**:
the per-isotope 100× targets (D 4.5, T 1.2, ³He 1.3, ⁴He 0.35 ppb) are unscored because
the extensive magnitude term is open (§3).

### 1.2 Residual → un-derived object → chain step

This is the table that answers "what do we need to do". Each residual is a framework
quantity; calibration noise is negligible against all of them (q₀'s own σ contributes
0.045 ppb to Q_β and 0.317 ppb to m_μ `[M]`).

| obs | residual | the un-derived object it traces to | chain step | owner bean |
|---|---:|---|---|---|
| m_μ | 211.2 ppb | **The μ–p substrate tension, exactly.** The CODATA-2022 muon pin and the proton pin differ by 11.614 ppb in q₀ `[M]`; m_μ = m_e·Vol(4₁)/ℏ_q² has lever `d ln m_μ / d ln q = −2/(q−1) = −18.185`, and 11.614 × 18.185 = **211.21 ppb** `[M]`, reproducing the witness to four digits. Every *ratio* observable has ℏ-exponent 0 and is blind to it (`PinRobustnessOfRatios.lean`). Re-pinning moves it, never shrinks it; deriving q₀ is forever gated. So this residual is **structural** — it can only close if the framework produces two pins that agree, i.e. if the archimedean evaluation of ℏ_q⁻² is refined, not if any anchor is chosen better. | 9 (archimedean functor at q₀) | none open — recorded as the two-way tension |
| Q_β | 1279 ppb | **Two stacked defects, one number.** (a) The scored value is the `Q_N2` rung of the c_k ladder in **convention C**; `qbeta_ck_cache.py` refuses under D, so no D-frame value exists (`qou-cds1`). (b) The closed form it sits on solves to Markov parameter `z = 1`, inadmissible under D (`ConventionDAdmissibleRoots.lean`, sorry-free); admissible alternatives give +12.47 % (`z = q`) and −43.16 % (`z_D`), and choosing by residual is forbidden (`qou-99qc`). | 11 (β-decay functional) — via 6 (Markov trace) | `qou-99qc`, `qou-cds1` |
| m_n | 0.903 ppb | **Pure Q_β propagation** via Path C `m_n = m_p + Q_β + m_e`: absolute offsets are Q_β +1.000 µeV, m_n +0.848 µeV, Δ_pn +0.851 µeV `[M]` — one number. Path C bypasses the flavour split, so the p/n colour-weighting convention (R3, `bring_color_weighted`) does **not** enter this row. | same as Q_β | same |
| Δ_pn | 658.0 ppb | same 0.85 µeV over a 1.29 MeV denominator | same | same |
| α_em⁻¹ | 0.365 ppb | Schwinger-ladder cubic form conditional on three unproved classes (`ArchimedeanLimit`, `BlochSuslinUniqueness`, `BringZeroModeBlochClass`) `[W]`; the residual's sign flips with the CODATA edition. | separate α_em chain | see §4 |
| m_K/m_π | 51.5 ppb (meets) | `√([3]_q[4]_q)` core is scan-selected (two discrete indices) and misses 385× on its own; clears only via the EM term `(α_em/π)(1+log(1+ℏ_q))` whose α_em rests on the Witten-κ `sorry`. Truncation knob removed 2026-08-22 (PR #5467); two selection knobs remain. | meson leg | `2026-08-22-mK-mpi-l2-red-team.md` |
| B(K), all A ≥ 2 | unscored | the **extensive (many-body) binding term** — a separate additive object, not a per-block weight (§3) | 9b | `qou-brng`, `qou-edt7` |

**Consequence for priorities.** Four of the six scoreable misses (Q_β, m_n, Δ_pn, and
the binding rows behind ⁴He) are downstream of **two** un-derived objects: the Q_β
functional under convention D, and the extensive binding term. m_μ is a third, structural
one. α_em and m_K/m_π share a fourth (the α_em conditional classes). That is the whole
L2 frontier: four objects.

### 1.3 The CAL-2 floor, restated

The "780 ppb CAL-2 floor" quoted in precision-goals.md is σ_exp(Q_β)/Q_β = 779.7 ppb
`[M]` (PDG 2024), the precision of the *ideal* CAL-2 datum. Under the proton
precision-substitution it is **not** the operative floor: q₀ is pinned from m_p/m_e at
0.0174 ppb, which propagates to 0.045 ppb in Q_β and **0.317 ppb in m_μ**. Every 100×
target in the table sits below 780 ppb, so "Subgoal-1 = targets ≥ 780 ppb" is satisfied by
nothing except the two anchors. And one target is unreachable at the proton pin by
*any* theory: **m_μ's target (0.2177 ppb) is below its calibration-propagated floor
(0.317 ppb)**. Only a tighter m_p/m_e measurement, or re-pinning to the muon (which makes
m_μ the tautological anchor and moves the 211 ppb onto m_p), changes that.

---

## 2. The mass chain, steps 1–9a: what is proved, what is chosen

The owner's suspicion — *"starting from the categorical action everything seems to be
defined … except the word; guessing some symbolic forms somewhere"* — is **confirmed with
one sharpening**: it is not only the word. **Every joint between the Lean-proved pieces of
step 9a is a selection**, and the word itself is chosen at three levels. The proved pieces
are real; what is not derived is how they are joined.

### 2.1 Per-step status `[M]` (grep of the named files this session)

| step | proved (sorry-free Lean) | derived, not formalised | asserted / chosen | bean |
|---|---|---|---|---|
| 1 categorical action | `braid-action-tensor.lean` (`BraidActionTensor`, `braiding_is_iso`; 0 sorry) | — | the Hecke quadratic is **definitional** in `def:categorical-action` | — |
| 2 Stokes → Hecke | `stokes_curvature_factors` (a `field_simp; ring` identity); `HeckeQuadraticClassicalShadow.lean` (the q = 1 shadow is an involution) | Picard–Lefschetz monodromy of the colour cubic is S₃ (`colour_cubic_branch_monodromy_probe.py`) — derives only the q = 1 shadow | **the geometry is a §3b conjecture class** `HeckeMonodromy` (`Mass/HeckeMonodromy.lean:55–63`); the deformation `1 ↦ q` is stipulated; KZ realisation pruned at real q₀ | `qou-0jcd`, `qou-d0qq` in-progress; `qou-denm` |
| 3 Alexander + Markov | `borromean_markov_trace_closed_form` (0 sorry) — **given** the Borromean Jones polynomial cited `[murasugi1996]`, not computed | y_λ closed forms at n = 3 | **two external axioms**: `markov_trace_unique_axiom` (`Hecke/MarkovTrace.lean:177`, whose own docstring says the class "is too weak"), `jones_markov_trace_exists` (`jones-markov-trace.lean:193`). `MarkovTrace.lean:131` docstring still writes convention C | `qou-juz3`, `qou-ar7f` |
| 4 Bring χ = −6 | χ = −6 as data; `seifert_genus_bound` for 7 torus-knot generators | — | "dim H₃(q) = 6 = # embeddable torus knots" is **not a Lean statement**: `prop:spectral-sequence-h3-explicit` has no `.lean` sibling; `embeddability-closure.lean` lists **7** generators; the particle ↔ knot dictionary is a hard-coded list | `qou-k8ek`, `qou-i229` |
| 5 Wedderburn / y_λ | `blockDim_eq_numSYT`; `trace_decomposition`, `yLambda_unique`, per-λ Frobenius orthogonality — **all conditional on `class WedderburnDecomp`** | Wenzl bridge numeric n = 3, 4, 5 | central-idempotent orthogonality and Schur orthogonality are **class axioms** (cheat-sheet §9.4 L-1/L-2, Mathas §3.43, not in Mathlib) | `qou-juz3`, `qou-mpq5` |
| 6 Frobenius pairing | the pairing is a **structure** (data); per-λ block orthogonality is step 5's conditional theorem | chirality `a_K = 1 + w(K)h + …` (no `.lean` sibling) | `Ψ = S² = id` is recorded "✅ proved (D3/D23)" in the cheat sheet; grep of `lean/QOU` for `antipode_sq` / `S_sq` / `Ψ = ` found **no theorem** — the "proof" is the structure declaration | none |
| 7 GB filtration | `centralIdempotent_idem` | `derivation_chain.py` tracker | `prop:gb-spectral-sequence` has no `.lean`; collapse at E₂ is a class field; `atom-knot-mass-derivation.lean:94–104` defines `gbSpectralCollapsePage := 2` and `GbSpectralSequenceCollapseAtE2 := (2 = 2)` — **true by definition** | `wpdb` |
| 8 jet order | `SkewSYT.lean` C1/C2 proved | jet-order log | `conj:jet-convergence-classical-limit` is a conjecture with no `.lean`; and the corpus now says production **has no tower** (`qou-tower`: H₃ GS reduction after every crossing ⇒ 6 dims for every nucleus) | `qou-tower`, `qou-hu1f` |
| 9a m_p/m_e | `dim V_(2,1) = 2`; Borromean closed form; `[3]_q!`; `proton_mass_substrate_identity` — a `rw; ring` from **class fields** | Vol(4₁) = 2·Cl₂(π/3) (KVC for 4₁ is a literature theorem); convention D forced by fibre N = 2 | **everything joining the proved pieces is chosen** — §2.2 | `qou-n04i`, `qou-24w9`, `qou-mrel`, `ovud`, `qou-6gf9`, `qou-4paj`, `qou-7loj` |

### 2.2 The chosen symbolic forms, in order of leverage on m_p/m_e

1. **The nucleon word `β_Bor = (σ₀σ₁⁻¹)³`.** Stated by definition in
   `def:categorical-proton`; hard-coded as `borromeanBraid` in
   `kashaev-volume-conjecture.lean:133`; labelled SELECTED / CONJECTURAL by the 2026-08-22
   red-team (`conj:proton-borromean-assembly`). The cheat sheet's "per-knot answer to why
   Bor" is prose; no Lean or content proposition derives the word from the categorical
   action of steps 1–2.
2. **The quark → crossing template.** `pyhecke/atom.py:462–530`: `uu → σ`, `dd → σ⁻¹`,
   `ud → averaged (σ − h/2)`, plus the confinement block. The p/n distinction is
   **assigned** by quark content; `thm:averaging-resonance-rule` proves arithmetic on the
   recipe (`kRes n w = n/2 + w` by `decide`), not the recipe. The intra-nucleon ordering was
   changed by owner ruling on 2026-09-05 (grouped → alternating), moving absolute traces by
   3.8–14× — a quantity a ruling can move is a chosen one.
3. **The atom word and the colour-weighted p–n interface.** `atom_braid_word_3A` with
   `pn_convention = "bring_color_weighted"`: interface factor `z − h(1/2 − δ/4)`. Two
   facts: (a) the object is **not a braid word** — the `2A+1` averaged letters lie outside
   `ρ(B_n)` (`qou-hkwd`); (b) δ = `(q−1)²(1−q⁻⁴)/3` is `prop:flavor-split-substrate`, which
   has no `.lean` and is fixed by matching `(m_n − m_p)/M_N` to −0.10 %. And `qou-nlw5`:
   the live interface value implies a q₀ matching **neither** pin (7.2e-5 off both).
4. **`F_Bor = |tr_M(β_Bor)|·[3]_q!/q³`.** A `def`; the producer's own `## Status` says
   *"F_Bor identification as natural categorical observable — open"*. `[3]_q!` is already
   bar-symmetric and `/q³` **breaks** bar-symmetry; removing it moves m_p by **+37 %**; the
   writhe of β_Bor is 0 so there is no `q^writhe` source; with one instance any exponent
   rationalises as f(3) (`qou-24w9`).
5. **The integers 2 and 6 in `m_p = 2(m_μ F_Bor − 6 m_e)`.** `ProtonBorromeanAssembly.lean:56–64`
   carries `multiplicity_eq_two`, `bindingCount_eq_six` and the assembly law as **class
   fields**; the "theorem" distributes them. This is AGENTS.md §3b-cond item 5 territory
   (a class carrying its own conclusion). The red-team probe: `2·m_μ·F_Bor = 1848.1527 m_e`
   and the subtraction reaching `m_p/m_e` is `12.0 m_e` to the last digit — i.e. 12 is the
   residual the pre-normalised F_Bor leaves, re-labelled `dim V_(2,1)·|S₃|`. The earlier
   `1/(−1/12)` Ocneanu provenance was refuted and scrubbed (`qou-mrel` records the owner's
   own question on the `−6 m_e` term).
6. **The muon anchor `m_μ = m_e·Vol(4₁)/ℏ_q²` and `ℏ_q = 1 − 1/q`.**
   `figure-8-muon-mass-cross-check.lean:44–47` proves `cal2_identity_pinned` **from the
   hypothesis that is its conclusion**; `vol_4_1` is a hard-coded literal (:19); `hbarQ` is
   a `def` with no derivation of `1 − q⁻¹` from steps 1–8. Vol(4₁) itself is a theorem
   (KVC for 4₁ in the literature). *Why the muon is 4₁* is the `skeinDescendants` list entry
   `"figure-eight (4₁)"` — a dictionary, not a theorem. `qou-6gf9` treats the relation as the
   leading term of an unknown series.
7. **Two kernel-false axioms still on `main`** (`qou-4paj`): `categorical-proton.lean` /
   `categorical-neutron.lean:71` assert `|neutron_mass q₀ − 939.565| < 1` while the
   definition evaluates to ≈ 746; the negations are provable. No consumers, but they are the
   `lean.ref` targets of `def:categorical-proton/neutron`.

**Reading.** Steps 1, 3 (closed form), 5 (block dimensions), 9a (the algebra of the
assembly) are genuinely proved. Steps 2, 4, 6, 7, 8 are proved *conditionally on classes
or definitions that carry the content*, and the m_p/m_e assembly is an exact identity
whose ingredients (word, template, interface, `/q³`, 2, 6, ℏ_q, the 4₁ dictionary) are each
chosen. Because q₀ is pinned by inverting this very identity against m_p/m_e, none of
those choices is *tested* by m_p — the ratio reproduces by construction. The only step-9a
predictions are m_μ (structural, §1.2) and m_n/Δ_pn, and those are Q_β propagation.

**What the m_n / Δ_pn rows inherit from steps 1–9a: only the m_p round-trip.** Both
production routes are Path C, `m_n = m_p + Q_β + m_e`. Two different m_n are live on
`main`: the facade witness (2026-08-29) carries `Q_β = 0.78280469` (**+602 ppm**, the
Kashiwara-N2 form evaluated at `z_D`) and `m_n` at **+501 ppb**; the L2 dashboard carries
the c_k-ladder `Q_β` (1279 ppb, convention C) and m_n at 0.903 ppb / 176.7×. A factor
~550 apart, and the dashboard's own note says
`reproducible_under_canonical_convention: false`. So the quoted 176.7× / 151.7× are
C-frame numbers with no canonical replacement yet (`qou-khue`, `qou-cds1`).

---

## 3. The binding chain, steps 9b–10: what is proved, what is chosen, what the numbers are

### 3.1 Status `[M]` (every Lean file grepped for `sorry` / `axiom` this session)

| sub-step | proved (sorry-free) | derived (no fit) | fitted / open | bean |
|---|---|---|---|---|
| Δ_λ per-partition **value** | `dtEuler_eq_deltaLambda_unconditional` — `Δ_λ = (−1)^{n(λ)}·dim V_λ`, all n (`BraidsAndKnots/DeltaLambdaGeneralNUnconditional.lean:41`) | wired to `delta-lambda-witness.json` (`value_only: true`) | the witness's own caveat: "needs `y_λ·χ^λ` weighting and a separate super-pairwise extensive term" | `qou-f0ny` |
| the extensive term — four prunes | `CoordinationSaturation` (`complete_graph_no_saturation`, `bounded_degree_saturates`); `ChainBondOrderDependence.orderIndependent_iff`; `BodyOrderRecurrenceDepth.three_le_depth`; `MayerThreeBodySign.lt_of_b3_pos` — all 0 sorry / 0 axiom | — | the **magnitude / mechanism** | `qou-brng` (todo), `qou-edt7` (in-progress) |
| deuteron | `BlochVolumeLeg` (volume leg ≡ 0); `ClosureComponentsSignInvariant` | owner ruling A 2026-08-29: canonical braid closure, Vol = 0 | Gram + SDP route is a scope-(a) negative (0 of 6 encodings; the one non-zero is AME fed back in); the +0.19 % `m_e·Vol(𝓑₃)·Δtr` route is dead twice over (Vol(𝓑₃) substituted for Vol(Hopf), and the `Δtr` law refuted) | `qou-e5jf` (todo; superseded by the ruling, not closed) |
| the cheat-sheet "honest derived core" `B = m_e Σ_n (n−1) Vol_n(K)` | `LinearChainBondCount.linear_chain_cluster_measure` — **the multiplicity `M_n = n − 1` only**; its own docstring: the magnitude "is empirical … NOT a Lean claim" | — | **the volumes are census-selected**: the producer's ³H 8.4686 / ³He 7.4889 are byte-identical to the `2·m_e·Vol(8₁₁)` / `2·m_e·Vol(L6a4)` census rows, which the 2026-09-05 ruling *"no knot-selection routes"* retires. **Cheat-sheet §0 row 9b is stale on its own terms** | `qou-fcn8` |
| the live derived functional `B = E₀·ln(tr_M(β_free)/tr_M(β_atom))` | `BindingExtensivity`, `SymmetrySignAmGm`, `BoundedDegreeCoulomb`, … (7 files) | bond factors `b_pp = z_D`, `b_nn`, `b_pn` closed-form in q, exact to 1e-35; `E₀ = m_e/(q(q−1))` derived; **log is the unique multiplicative→additive map**, so the functional is forced, not chosen — the one unambiguously good result of the window (a ~1300× residual-band gain over `B = scale·Δtr`, which is refuted algebraically: `Δtr/tr_free → 1` by A = 11) | the identification `α·ln(·)` = *energy* is `POSITED` (dashboard tag); the coefficient is not derived; the shape residual 22.5 % is 22.7× the total scale freedom 0.99 % | `qou-mkm8`, `qou-0c19` |
| step 10 — operator-selection LP | `operator_selection_lp.lean` (feasibility, optimality, strong duality; 0 sorry) | `lp_dual_solver` emits every dual field | the LP is **degenerate**: optimum ≡ 0, `y₀* = 0`, the minimiser set is a positive-dimensional mirror-closed face — "not a selection principle" (`operator-selection-lp.md:28–56`) | — |
| step 10 — `T_w` / knot identification | — | — | **an admitted fit**: `T_w` and the knot are hard-coded inputs; the census search selects on `B_AME/(ρ m_e)` (`2026-08-25-knot-id-is-an-admitted-fit.md`; `mass_table_ppb.py:11–22`); owner ruled 2026-09-05 no knot-selection routes | `qou-8ms1`, `qou-9ot5` |

### 3.2 The numbers

**A. What production publishes `[W]`** — `canonical-mass-table-extended.witness.json` (2026-09-07,
proton pin) copies `B_pred` from `mass-table-ppb.witness.json` (2026-08-23):

| nuclide | B_pred | B_AME | err | origin, verbatim from the witness |
|---|---:|---:|---:|---|
| ²H | 2.24882 | 2.22457 | +1.09 % | `1·m_e·Vol(6₂)` — "census-assigned (EXPLORATORY)" — **retired by ruling A** |
| ³H | 8.46860 | 8.48180 | −0.16 % | `2·m_e·Vol(8₁₁)` — census-assigned |
| ³He | 7.48892 | 7.71804 | −2.97 % | `2·m_e·Vol(L6a4)` — census-assigned |
| ⁴He | 29.95568 | 28.29566 | +5.87 % | `2·m_e·4·8G` — "magic rule (ν_SDP = 2 extrapolated)" |
| A = 5, 6, 7 | none | | | "no census knot with Vol ≈ B_AME/m_e found" — the selection signature AGENTS.md names |

These are the selected-against-target numbers, and the 2026-09-07 witness still publishes all four
labelled `prediction_method: canonical-trace`. **They are not predictions and should not be
quoted as such.**

**B. What the derived functional gives `[M]`** — `mass_binding_dashboard.py --group low`, run this
session (no witness emitted; float64 per `qou-4ohh`; proton pin; α = E₀^(N=0) = 4.186 MeV; D-frame
bond factors `pp = 0.607, pn = 0.677, nn = 0.790`). `err X = B_AME / B_X`:

| iso | B_AME | B_sym (log law) | err | B_can⁰ (`E₀·Δtr`, refuted) | err | E_C |
|---|---:|---:|---:|---:|---:|---:|
| ²H | 2.22 | 2.83 | 0.79 | 0.62 | 3.61 | 0.00 |
| ³H | 8.48 | 6.14 | 1.38 | 0.46 | 18.5 | 0.00 |
| ³He | 7.72 | 5.37 | 1.44 | 0.57 | 13.6 | 0.85 |
| ⁴He | 28.30 | 8.68 | **3.26** | 0.33 | 86.5 | 0.77 |

Two quiet inconsistencies: the dashboard's α (4.186) is not the ruled `E₀^full = 4.227483` MeV
(under which the log law is an upper bound for 2547 of 2548 nuclides, ⁴He the sole exception);
and the first end-to-end run of the step-10 `binding_energy` path gives the deuteron at
**−7.271 MeV — wrong sign** (`2026-09-02-binding-energy-first-corrected-value.md`), with ³H, ³He,
⁴He likewise negative and nearly constant in A: the accumulator carries no extensive term.

**C. The 3-body cumulant is where the defect lives** (`2026-08-29-he4-magnitude-shortfall-location.md`,
convention D, proton pin): AME `b₃ = +1.426`, model `b₃ = −2.744`; the held-out ³He−³H splitting
is right-signed and short by 2–6×. **Both corpus assemblies are proved incapable of `b₃ > 0`**:
multiplicative `W = 1 − ∏f` forces `b₃ < 0` whenever `f_pn ≤ 2/3` (every measured value is;
`MayerThreeBodySign`), and pairwise-additive log forces `b₃ = 0`. Sibling PR #7148 `[PR]` adds
that the already-derived kind-dependent bond weight is real but far too weak (`ρ_pp` 0.72–1.21
against a required 1.641); PR #7155 `[PR]` adds that **every edge set `atom_braid_word_3A` can
express is a linear layout and has no bulk** (Lean, sorry-free) — so a surface term cannot come
from any expressible coordination graph.

### 3.3 What is structurally excluded (scope b) vs merely unsuccessful (scope a)

**Scope (b), invariant named, Lean sorry-free — do not re-run:** complete-graph coordination
(no saturation); the linear chain as a well-defined functional at q ≠ 1 (arrangement-dependent
unless `L_pp = L_pn = L_nn`); the multiplicative assembly with `f_pn ≤ 2/3` (`b₃ < 0`); the
pairwise-additive log (`b₃ = 0`); body-order recurrence depth < 3 (and a 3-term ratio is
unfalsifiable — first prediction at body order ≥ 6); any count-channel carrier (`b₃/b₂ = M − 3 ∈ ℤ`
vs measured ∈ (0,1)); a scalar q-difference kernel on the q-Borel carrier at any depth; the
`B = scale·Δtr` law; any expressible edge set carrying a bulk (PR #7155).

**Scope (a), unsuccessful, ingredient not excluded:** the six Δ_λ magnitude ansätze (never
re-scored under D, `qou-6snb`); the deuteron Gram/SDP (six encodings); `m_e·Vol(𝓑₃)·Δtr`; the
volume-defect `ℏ_q²` route; the Milnor-μ̄ exclusion (re-scoped b → a on 2026-08-30 because the
canonical word fixes the interfaces non-uniformly); PROBE 3/4 per-λ towers; the kind-dependent
bond weight (PR #7148).

### 3.4 The one real open problem

The **extensive many-body term** — the assembly functional and its coefficient. Upstream of it
everything is settled: the form is the extensive log family on the Lean-forced chain, the scale
freedom is 0.99 %, the shape residual 22.5 %, and the defect sits at 3-body. What `qou-brng`
reduces it to: *why the mutual (coordination) channel enters as a bare integer count while the
self channel carries the quantum-dimension sum `lw`* — a ribbon-category statement
(`2026-09-03-brng-subq2…`) that Mathlib lacks. Sibling PR #7153 `[PR]` (TowerSpan proved from
the braid relations; the disjoint-block trace law discharged) is the infrastructure this needs.

The bean's own recommendation, marked as judgement: not another carrier / weight search but (i)
the quantum-trace / connected-sum multiplicativity formalisation (`qou-301d`), and — ranked above
it by the arc's "signs before digits" rule — (ii) **un-bind the diproton / dineutron**
(`QOU.QBeta.single_crossing_binds`, route `qou-vbyi`), since no magnitude work reaches L2 while a
predicted observable has the wrong sign.

---

## 4. Q_β, the c_k ladder / c₃, and the f-map — status under convention D

Short version: **the Q_β channel has no derived number on the canonical convention.** The
functional is inadmissible, the ladder above `c₂` is extracted from the measurement it
predicts, the phase the ladder needs has no derivation in either convention, and the
fibre-level "permanent fix" (a Habiro element) has no candidate. What *is* settled is a
set of sorry-free exclusions that fence the problem sharply.

### 4.1 Q_β itself — the functional is the open decision

| fact | tier | evidence |
|---|---|---|
| the published form `Q_β = m_e·\|q²−2q−1\|(q+1)/(2q³)` (0.17 %) equals `\|tr_M^z(Δ_S)\|·E₀` at Markov parameter **z = 1** (the coordinate sum) | derived, exact over ℚ(q) | `qbeta_published_form_is_the_inadmissible_z1_probe.py` 15/15 |
| admissible convention-D roots are `z = q` (augmentation) and `z_D = q³/(q²+1)`; `z = 1` is not one | **proved**, sorry-free | `QBeta/ConventionDAdmissibleRoots.lean` (8 theorems) |
| option B, augmentation `σ ↦ q`: **0.8798906 MeV, +12.470 %** | derived, admissible | `2026-09-05-qbeta-functional-decision-options.md` §6 |
| option C, `tr_M` at `z_D`: **0.4447004 MeV, −43.157 %** | derived, admissible | same |
| B and C are proportional: `tr_M(z_D)(Δ_S) = α·aug(Δ_S)`, `α = (q⁴+1)/(q²+1)² ≈ 0.5054` | **proved** | `AdmissibleAgreementDeterminesClass.lean` (5 theorems, 0 sorry) |
| the admissible trace space is 2-dimensional and `net` (z = 1) lies outside it | proved (rank computation) | `qbeta_admissible_span_prune_probe` 8/8 |
| a convex weight `w*` between B and C exists but fails on 3 of 6 basis elements | **fitted → excluded** | `qou-99qc` 2026-08-28 |
| option E (a different element): requires `χ_(2,1) = 2χ_(3)`; both `Δ_S` and `Δ_L` fail for every q > 1 | scope-(b) exclusion of both candidates | `qbeta-option-e-forced-class` 9/9 |

**The decision that is pending is what ε *means*** in `Q_β = |ε(Δ)|·E₀`: the augmentation
(an algebra map that descends to the TL quotient `H₃/rad`, where `prf:algebraic-gns-embedding`
puts the theory) or the coordinate sum (not an algebra map unless h = 0 —
`CounitSigmaOne.h_eq_zero_of_image_one`, sorry-free — and does not descend). Choosing by
residual is selection against the target and forbidden. **Owner bean `qou-99qc` (todo).**
The default if nothing is decided is unstable: the published 0.17 % keeps being read as live
(PR #5893 already re-derived the mismatch once).

The L2 row is scored on `Q_N2` from the c_k cache — the z = 1 base times the `c₂ = −1` rung,
**convention C**, proton pin — and the producer refuses to run under D. The facade witness
carries a *different* Q_β (the same form evaluated at `z_D`, **+602 ppm**). So the 164× /
176.7× / 151.7× trio are C-frame numbers with no canonical replacement.

### 4.2 The c_k ladder and c₃

| rung | value | tier | frame |
|---|---|---|---|
| c₂ | −1 | **structural** — the `u²` coefficient of the explicit-factor product `Π_{k≥2}(1 + c_k u^k)` (trivially, no k = 1 factor); for the normalised `Φ(u)/Φ(0)` it is `c̃₂ = −9/8` (`normalisedQuadCoeff_eq`, sorry-free). Not "proved": `N2_factor` is a bare `def` | C; a D re-extraction gives c₂ ≈ −9.30 |
| c₃ | −2.06934258 (proton) / −2.01986031 (muon, CODATA 2022) vs candidate −2 = J_Hopf(1); gap 3.47 %; cross-anchor swing 2.39 % | **extracted from CODATA Q_β** (cache tier `cal-anchored`); refuted as a real-q fibre element | C; D re-extraction gives **−974** (a sensitivity measurement, not a value) |
| c₄ | ≡ 0 once c₃ is extracted (`greedy_later_rungs_vanish`, sorry-free) | artifact | C |
| c₅ | `−(b² + ½) = −1.2527` current; `3c₃² + b = +12.87` superseded, still at 2 sites | near-match | C (`qou-54g5` todo: block says −6.6 ppb at the muon pin, code gives +7.34) |
| c₆, c₇ | imposed in the extraction | self-consistent, not independent | C |
| c₈–c₁₀ | rational at the silver ratio q = 1 + √2, `norm_num` | proved at one point, no cross-anchor test | — |
| N = 4 → 5 | \|residual\| 6.1698 → 6.2260 ppb (+0.91 %) under the live c₅ | signature holds, margin small | C |

**The ladder has not been re-derived under D, and it is proved that it cannot be by
substitution.** `decayLadder_zC_threeRow_ne_zero` (`MarkovZFullBarCondition.lean:214`,
sorry-free): the C ladder and the two-row (D) forcing are mutually exclusive. C and D are
*different algebras* — `TL_n = H_n/⟨antisym⟩`, `y_(1³) = 0` exactly; at n = 3 D retains
83 % of C's content, at ⁴He 0.043 % (`qbeta-c-vs-d-are-different-algebras`, scope-(b)).
Owner ruling D7 (2026-09-07): convention D governs the decay channel; the full tower governs
mass/binding.

**The blocker underneath is the phase.** The ladder's N = 1 factor carries an eigenphase
`α = (z − 1)h/2` whose cited source (`prop:q-beta-spectral-bridge`) produces a ratio
coefficient, not a phase (5.35 % C / 4.12 % D off), and the cosine carrier
`TransferMatrixEigenphase` is **proved vacuous** (`EigenphaseCarrierVacuity.lean`, 0 sorry).
"Re-derive under D" therefore means *supply a phase*, bean `qou-pdix` (in-progress, the S1
blocker). Routes already closed and not to be re-run: bar-even rescaling
`z̃_D = z_D/q²`; the derived projection `α − h²/4` (c₂ −9.30 → −1.73, still 73 % off);
the three D-frame gates on a Habiro generator (all vacuous, `…is_exhausted_probe` 10/10);
Hoefsmit eigenphase supply; Route-5 projection N-selection (predicts nothing).

What `qou-cds1` has actually been building (PRs #6965 … #7111, merged 2026-09-07) is
**foundations, not the ladder**: `heckeToTL`, the presentation-level `TL_n ≅ H_n/⟨…⟩`
(sorry-free), Wedderburn at n = 2, 3, TL freeness, the δ-half of the closure rule. Open:
`⟨relators⟩ = traceRadical tr_M`, `dim TL_n = Catalan(n)`. Sibling PR #7149 `[PR]` adds
that the "N question" on |q| = 1 (whether a root of unity supplies the eigenphase) reduces
to the **algebraicity of Vol(4₁)**: rational and transcendental q₀ are both excluded by
Niven and algebraic-integrality (Mathlib), so a root of unity exists only if Vol(4₁) is
algebraic — a named open problem, not an unanswerable one.

### 4.3 The f-map (z → c_k)

The f-map is the assembly taking the proved z-side data — the Markov parameter's exact
3-term recursion `4(n+1)a_{n+1} + 6n a_n + (2n−1)a_{n−1} = 0` (`MarkovParameterRecursion.lean`),
the ℏ-Taylor coefficients of Δtr_M — into the ladder rungs c_k
(`docs/coordination/z-ck-fmap-keystone.md`). The root of every flip-flop: Δtr_M is O(√u)
while c₃ is O(u³), and the shared −2 was a five-order coincidence (PR #1593).

Registry (`ck-dk-canonical-registry.md` §9, KC1–KC22): KC1 depth ≥ 2 *proved*; KC2/3/4
(`a₂ = c₂`, `a₁ = −c₃`, `a₁ = √2Φ₂`) *conditional* on a depth-2 recursion never established;
KC13 z bar-even / κ bar-odd *proved for C only* — `bar(z_D) = q⁻⁴ z_D` (`ZBarParity.zD_bar_twist`,
20 theorems) so it does not transfer; KC20–22 the c₃ bar-odd carrier, all C-conditional.

**Under D the f-map is fenced in four directions**: `c₃ = J_Hopf(1) = −2` is not forceable
from the two-row trace in the bar-odd channel (**scope-(b)**, `FMapC3ParityExclusion.lean`,
7 theorems: any bar-odd part vanishes at q = 1, and −2 is bar-even nonzero), nor bar-even
(q = 1 genericity), nor from the Φ_b amplitude leg (Route C, `qou-i2ir`: the one-scale gate
needs `4λ₂³ + λ₃² = 0`, measures 6.088), and three transport routes closed 2026-08-26. The
live residue is a **form clash**: the evaluation map is affine in the loop weight, the ladder
asserts a cosine, and the cosine carrier is vacuous. Bean `22ie` was scrapped as a dead
session milestone; its content lives in `qou-avt4` (completed), `qou-avtq` (the attack-vector
queue, in-progress) and `qou-i2ir`, all parented to `qou-cds1`.

### 4.4 The Habiro element and q*

- **Habiro / fibre-level programme:** `qbeta-habiro-taylor-investigation` re-run 2026-09-07
  reports `allPassed = False` with `missing_categorical_formula = "Q_β = m_e × f(Δtr_M(q), q)"`.
  Generator rigidity is proved (single generator ⟹ Hankel `c₂c₄ = c₃²`, `c3_not_free`;
  `QBetaHabiroGeneratorRigidity.lean`, 10 theorems); the D-frame generator gates are
  exhausted. Twenty-five `*Habiro*` Lean files, none deriving a c_k. **No candidate element;
  no live bean owns "find it"** — `qou-avtq` is the nearest queue.
- **q\* (the decay-sector point):** root of `S(q) = c₃(q) + Vol(4₁)`, C-frame; under a bare
  z-swap it leaves the anchor interval by ≈ 20 000 gaps. Its premise (H1)
  `c₃^even = −Vol(4₁)` is **motivated, not derived** (the bar-split needs q ≈ 0.901, which no
  anchor supplies); "third determination of q₀" is withdrawn as circular; `σ(c₃) ≈ ±1.26`
  (61 % of |c₃|) so the proximity to −Vol(4₁) is 0.03σ — no evidence either way. `qou-avt3`
  is blocked by design until H1 is derived or dropped; no bean owns deriving H1.

**Absences, stated as absences:** no D-frame c_k exists (the producer refuses); no derived
phase in any convention; no admissible functional reproduces Q_β; no Habiro element; no
derivation of H1. The only unconditional proved items in the arc are exclusions and the
TL/Hecke infrastructure.

---

## 5. The open conjectures, the assumed forms, and the formal surface

### 5.1 Population `[M]`

**181** blocks use the `conjecture(…)` builder (mass-theory 64, appendix-surreals 17,
nuclear-interactions 15, observations 12, …). **117** are cited in some `uses[]`; **75** are cited
by a block in the mass / nuclear / braids / observations / q-values chapters (graph-adjacent to
the chain, which is a structural filter, not a judgement of importance); **7** have no `lean.ref`.
Of the ones on the m_p / B(K) / Q_β chain proper, **none has a Lean instance** — every §3b class
below is content-bearing and open, which is the honest state.

### 5.2 The conjectures that carry the chain

| label | what it asserts | Lean carrier | note |
|---|---|---|---|
| `conj:proton-borromean-assembly` | `m_p = mult·(m_μ F_Bor − bind·m_e)`, `mult = dim V_(2,1) = 2`, `bind = \|S₃\| = 6`; the *bridge* (why dim enters linearly, why \|S₃\| is the binding count) is the conjecture | `ProtonBorromeanAssembly` (fields `multiplicity_eq_two`, `bindingCount_eq_six`) | load-bearing for the m_p/m_e identity (§2.2 item 5) |
| `conj:borromean-baryon-mass-formula` | common Borromean term for baryon masses; **its class fields compare to CODATA ratios** (`\|m_p/m_e − 1836.152673426\| ≤ residual`) | `QOU.Borromean.MassFormula` | a comparison inside a class, not a derivation |
| `conj:binding-manybody-eq-jet-filtration` | `B(K) = Σ_n m_e·a_D^(n)`: the binding series is the jet-order filtration; the block's own body records that an unconstrained recursion "constrains nothing" | `BindingManyBodyJetFiltration` (7 fields) | 7 users |
| `conj:kashaev-volume-conjecture` | Kashaev limit → hyperbolic volume; the Vol(K) input | `VolumeConjecture (q : ℝ)` | proved for 4₁ in the literature; used conditionally elsewhere |
| `conj:inter-nucleon-channel-color-tube` | the pn channel is the colour-tube-weighted refinement of `(σ + σ⁻¹)/2` — the source of `bring_color_weighted` | `InterNucleonChannelColorTube [BringFiberAction]` | **conditional on `conj:s5-so3-fiber-action`, which has no block**: grep of every `label:` finds nothing; three `.ts` cite it as "PR #1081 Task 3"; the ledger `docs/coordination/s5-so3-keystone.md` exists |
| `conj:reeb-linking-cwf-normalization` | the pn-bond amplitude is unit-normalised exchange, `a²(1 + z²) = z²`; "B(²H) = 5g remains a near-match, unit anchor open" | `ReebLinkingCWF` | feeds step 9b |
| `conj:qbeta-ck-truncation-canonical` | ∀ k ≥ 3 ∃ canonical anchor-free closed form for `c_k`; fields `c₂ = −1`, `c₃ = J_Hopf(1)` | `QbetaCkTruncationCanonicalClass : Prop` | **the second field axiomatises the 3.47 % near-match** |
| `conj:crystal-graph-realization` | Hecke normal forms realise crystal highest-weight vectors | `CrystalGraphRealization` — **three different declarations** in three files | most-used (12) |
| `conj:rho-prefactor-structural` | `ρ(𝔥) ≈ dim_q(λ*(T_w))` | `RhoPrefactorStructural` | the λ_A replacement candidate |
| `conj:stokes-dt-bps-bridge` | Stokes constants = DT/BPS degeneracies | `StokesDTBPSBridge` | `qou-q3np`: 4₁ Stokes constants are integers, the targets are small opposite-signed reals — a structural obstruction, no literature precedent |
| `conj:binding-qbeta-complex-volume` | binding and β-decay unified by complex volume | **no `lean.ref`** | 7 users; the structural bet in the gap map's G1/G2 "close together or not at all" |
| `conj:canonical-knot-id-sdp` | ²H/³H/³He knots from the confinement SDP | **no `lean.ref`** | `qou-vd7j`: the SDP admits 0 of 3558; owner ruled 2026-09-05 "no knot-selection routes" |
| `conj:im-q-physical-role` | observables factor through \|q\| | `ImQPhysicalRole : Prop` | the q\* block depends on it |

### 5.3 Where a symbolic form is *assumed* rather than derived (the owner's "guessing some symbolic forms")

Keyword counts on chain-chapter `.md` `[M]`: `ansatz` 40, `near-match` 44, `by fiat` 12,
`stipulat` 11, `postulat` 3; in `computations/`: `ansatz` 546, `near-match` 489. The load-bearing
instances, with the corpus's own words:

| quantity | form assumed | where it says so | status |
|---|---|---|---|
| **Q_β** | `Q_β = \|Δ(net)\|·𝔈₀` | `epistemic-status-of-calibrations.md:56` "We postulate…"; `calibration-inputs.md:91` "constitutes an ansatz"; `qbeta_net_trace_invariance_probe.py:11` "**STEP 8 IS THE CHAIN'S ONE POSTULATE**" | reduced to the step-4 presentation postulate, not eliminated; under D `z = 1` inadmissible (§4.1) |
| **ℏ_q** | `ℏ_q := 1 − q⁻¹` | `quantum-planck-constant.md:1` — a one-line definition | no derivation found (the substrate chapters were not searched exhaustively, so "there is none" is not established) |
| **𝔈₀** | `𝔈₀ = m_e c_q² ℏ_q = m_e/(q(q−1))` | `energy-scale-planck.md` "Derived form" | derived from the *definitions* of `c_q` and `ℏ_q`, i.e. from two definitional choices; a tower-summed variant `𝔈₀/(1 − ℏ_q²)` is 1 % away; the `kT` assignment conflicts (`qou-892m`) |
| **m_μ/m_e** | `= Vol(4₁)/ℏ_q²` | `epistemic-status-of-calibrations.md:26` "structurally tautological. We defined q₀ to enforce it" | the CAL-2 definition |
| **F_Bor normaliser** | `[3]_q!/q³ = 1/y_(3)` | `f-bor-borromean-observable.md:1–8` "the natural … combination" | why the trivial-partition Markov weight is the right normaliser is not argued (`qou-24w9`, `qou-n1dj`) |
| **brane-tower functional** | Rogers `Li₂^q`, not Faddeev `Φ_q` | `mass-endomorphism-tower.md:16–20` "the Faddeev form was **empirically incompatible with isospin symmetry** at q₀" | chosen by outcome — selection against the target |
| **bar-even channel** | `g(x) = −Li₂^q(−x)`, `x > 0` branch | `_li_2_q_util.py:140–150` | justified by convergence, not structure |
| **Markov z** | `z = q³/(q²+1)` | `markov-trace-frobenius-selection.md:71` "derived in step 3b"; `markov-axioms-primitive.md:40` "stipulated"; `h3-markov-wenzl-weights-context.md:67–74` records that the two blocks disagree | forced in the mass channel by the two-row cap; transfer to the decay channel forbidden by its own source |
| **pn interface** | `σ_pn = (σ + σ⁻¹)/2`, `α = ½` | `pn_alpha_lp_dual.py:15–18` "postulated … no algebraic derivation of α = ½" | uniqueness proved *given* bar-invariance + `σ_pn = z`; the colour-weighted form lies outside those hypotheses |
| **colour weight ε** | `ε = δ/4` | `closed_form_tau_M.py:75–84` "IS derived"; `interface-knot-markov-z-proof.md:119–136`: misses bar-oddness by `q²`, the repair `ε = qδE/4` leaves a **free bar-even E**, "no particular E is asserted" | parity forced, magnitude not |
| **ρ(q)** (λ_A) | `5/2 + 3h²/4` | `mass_vol_density.py:17` | a CODATA-implied fit; deprecated for absolute mass; replacement `ρ ≈ dim_q(λ*)` conjectural |
| **c₃** | `−2 = J_Hopf(1)` | `qbeta-ck-truncation-canonical.md:15`; `q-beta-c3-hopf…md:65` "near-match, not Taylor-exact" | 3.47 % off; the class field axiomatises it |
| **α_em Habiro element** | `H(q) = [2]_q(1 − h²α)` | `alpha-em-habiro-bar-involution.md:1` "Let H(q) = … be" | bar-invariance proved *of* the form; the form posited; `1/(4π)` "remains a near-match fit"; the `[10]_q` linchpin `δ_q(T_{3,5}) = q¹⁰ − q⁻¹⁰` asserted (`qou-15sj`) |
| **Plancherel weight in Φ_k** | `dim_q²` | `2026-09-05-phi-k-weight-family.md` | `y_λ` and `d_q²/[n]_q!` pruned in Lean; **ruled 2026-09-05: Molien canonical**, `d_q²/D²` a labelled comparison arm (`qou-oots`; the audit first listed this as open — corrected in §8) |
| **4-body weight** | `w₄ ≈ 15.6016` from a depth-2 q-difference operator | `universal-binding-architecture.md:21–27` "Organizing ansatz" | matches ⁴He to 1.2e-4 — flagged in-block as a substrate-value match, not a derivation |
| **deuteron binding** | `B(²H) ≈ 5g·E_unit` | `reeb-linking-cwf-normalization.md:36` | near-match, unit anchor open (`qou-i4pz`) |

### 5.4 The formal surface `[M]` (comment-stripped scan; `lean`/`lake` not run)

- **The `QOU/` library is sorry-free.** Raw `grep sorry` hits 28 / 52 / 112 / 26 / 30 files in
  `Mass` / `MassTheory` / `QBeta` / `Hecke` / `BraidsAndKnots`, and **every one is prose**
  ("sorry-free", docstrings). Non-comment `sorry`: **0**. (My own first-pass grep this session
  counted those prose hits as sorries; that figure is withdrawn.)
- **Five axioms**: `Hecke/MarkovTrace.lean:177` `markov_trace_unique_axiom` (the step-3
  uniqueness); `BraidKnot/IwahoriHeckeAPI.lean:313/333/372` central-idempotent centrality,
  orthogonality, bar-transpose (the step-5 Wedderburn content, Mathas §3.43);
  `BraidKnot/PSDFeasibilityProxy.lean:90`.
- **Eight content-sibling `sorry`s on the chain, in three files** — the one that matters is
  `mass-theory/gram-determinant-plancherel-ratio.lean:164` `gram_kappa_numerical_value`
  (`\|κ − 1.722\| < 0.001`, hypothesis `IsTorusPairAtQ0` with no constructor): the **Witten-κ
  Gram determinant that α_em, and hence the m_K/m_π pass, is conditional on**.
- **§3b classes without instances** carry the rest of the open state: `HeckeMonodromy` (step 2),
  `IsHeckeOfFullRank` (needed before any `WedderburnDecomp` instance, `qou-hah4`),
  `ZToCkMappingClass` (the f-map; named in AGENTS.md's anti-laundering rule),
  `TransferMatrixEigenphase` (the ladder phase, proved vacuous), `StokesDTBPSBridge`,
  `CovarianceKernelConjecture` / `KernelPincerLegs` (the W_λ kernel),
  `BindingFollowsQBessel`, `ProlongationPeriodMeanQuantumDim` (the NA-Stokes keystone), the
  Milnor order/sign classes (`qou-v7ro`). `FMapStructuralPaths.lean:32–60` declares three f-map
  route classes that may be field-less — flag for `proof-no-empty-prop-carrier`.

### 5.5 Open research beans that name mathematics (not hygiene)

| bean | status | what is open |
|---|---|---|
| `qou-brng` | todo | prove the saturated binding fraction `B/(A m_N) = ℏ_q²` exactly; the map `n₊ + n₋ → z`; why mutual linking enters as a bare integer while self-linking keeps `lw` |
| `qou-edt7` | in-progress | what replaces the multiplicative assembly `W = 1 − ∏f`: both corpus assemblies proved incapable of `b₃ > 0` |
| `qou-99qc` | todo | **owner call**: what ε means in `Q_β = \|ε(Δ)\|·E₀` |
| `qou-cds1` / `qou-pdix` | in-progress | the D-frame ladder; the phase it needs has no derivation |
| `qou-cds2` | in-progress | the Gram singularity under D; `G_PINV` pseudoinverse still live in `gram.py` / `gram.rs` / `confinement-operator-selection.py` |
| `qou-oots` | in-progress | ruled Molien 2026-09-05; remaining scope is the α_em-axis triage |
| `qou-e5jf` | todo | three inconsistent deuteron knots; owner ruling A picked braid closure; bean body not updated since 08-21 |
| `qou-q3np` | todo (high) | `A_ω → S(μ)/S(p)` has no precedent and a structural obstruction (do not close: rule 13a) |
| `qou-n1dj` | todo | does the mass fibre functor land in `Rep(SU_q(2)) ≅ TL` or full `H₃(q)`? corpus self-contradiction, 197 ppm on m_p |
| `qou-rm47` | todo | which fibre dimension N does the binding channel trace (`N_eff = 2.5995`) |
| `qou-892m` | todo | two unreconciled `kT` assignments (`ℏ_q` vs `E₀`) |
| `qou-15sj` / `qou-gwio` / `qou-gbsa` / `aemx` | todo | α_em: `[10]_q` linchpin asserted; −468 ppb structural residual; **two α_em derivations 470 ppb apart** |
| `qou-v8qx` | todo | `w₃` second base case via the ramified double cover — the one route nothing excludes |
| `08a2` / `60iz` / `qou-dyij` | in-progress | keystone de-abstraction; Mathlib knot-theory gap blocks the general `jet_filtered_knot_factor` layer |
| `qou-9nq9` … `qou-u8w5` (8 beans) | todo / in-progress | the Δ_λ **magnitude** family — surviving object is the bare first-order per-bond amplitude |

---

## 6. The last four weeks of `main`, clustered — where the effort went and where it did not join up

**Scale `[M]`** (`origin/main` deepened to 2026-07-18): **12,184 commits** since 2026-08-10
(562 merges), **635** audit docs dated in the window, **6,016** `claude/*` branches, **1,961
beans created** in the window, **519 in-progress** (463 with `qou-` ids). The thread clustering
keys on the bean id in each commit subject; 20 % of commits (2,437, in ≤15-commit beans) fall in
an unclassified tail and are not in the rows below.

### 6.1 Threads

| # | thread | key beans (commits) | commits | moved a chain step? | what landed |
|---|---|---|---|---|---|
| T5 | **binding magnitude / extensive term / deuteron / Gram-SDP** | brng(133) sv7h(28) wlaf(26) 6tcn(23) hok7(21) yaig(19) edt7(15) | 1,335 | **9b** | four sorry-free structural *negatives* (saturation, chain-order, body-order depth, Mayer sign); the derived log functional (§3); owner rulings (deuteron non-hyperbolic 08-29; no knot-selection routes 09-05); no positive closure |
| T10 | precision gates, float64 ratchets, witness assertions | srvu(40) p77d(37) 26f2(27) | 1,228 | none | infra |
| T4 | **Hecke / Schur–Weyl / GS foundations in Lean** | auq3(182) phir(103) j7ln(58) gjg6(57) uer7(40) kwoa(34) k4oq(22) | 1,131 | foundations of 3/5/7 | proved, sizeable — and **cited nowhere in the cheat sheet** |
| T6 | **mass channel: Δ / ε(Δ), tr_M h-tower c₁/c₂, χ carriers, Φ_k weights, full tower** | k5r5(95) o6ov(95) w4gn(38) 9yt9(35) oots(23) 99qc(22) hu1f(18) qqm4(27) pdg9(13) | 873 | **9a** (m_n side) | c₁ of the trace difference derived (`pdg9`) then **staled** by the 09-05 atom-word reordering; many negatives; one retraction-of-a-retraction |
| T3 | q₀ anchor migration, CODATA 2022, anchor gates | 1c4y(38) y98b(34) 9ugp(32) aj91(29) | 871 | none (moves no residual) | infra |
| T1 | **Q_β c_k ladder / eigenphase α under D** | cds1(287) pdix(37) | 661 | **11** | mostly negatives (§4); three self-retractions in `cds1` alone |
| T11 | Lean hygiene: vacuity ledger, self-assuming projections, false axioms | z9ws(56) lsib(20) i6u4(16) | 619 | none | infra + one real soundness find (4 SDP-uniqueness axioms prove `False`) |
| T12 | QA / content hygiene | ujp8(106) 3nva(49) | 545 | none | infra |
| T2 | convention C → D excision / Gram z | cds2(24) t9r1(19) cxjq(16) | 544 | prerequisite of 11 | detector-blindness taxonomy at 39 rows; C surface still "unmeasured" |
| T13 | process / meta | gwe9(32) | 372 | none | infra |
| T9 | hyperbolic volume, 4₁ / 5₂, two-bridge | f8li(22) 52ch(20) yvyd(16) | 230 | **off path since 08-29** (deuteron Vol = 0) | proved + literal fixes |
| T7 | Δ_pn / mirror / E_EM / Milnor linking | 768r(24) dg07(23) o6ml(17) bn8e(16) 17mq(14) | 226 | **9a** (Δ_pn) | negatives + one route |
| T14 | trajectory / arithmetic (Roth, surreals, q-NS) | br3w(10) | 183 | none | proved, off-programme |
| T8 | **α_em / m_K/m_π / Witten κ** | aemx(8) qpj9 pb1w | **72** | 9 (α_em `sorry`) | **two α_em derivations 470 ppb apart** (`aemx`, open since 08-28); α_em put on the dashboard 09-07 |
| T16 | particle / knot tables | knot(12) | 64 | none | fixes |

**The share that is mathematics `[M]`:** infra threads 3,866 commits (31.7 %), merges 562,
bookkeeping kinds inside math threads 2,353 — **55.6 % non-mathematics**; `fix/audit/retract`
inside math threads 10.4 %; `lean/probe/feat/derive` inside math threads **18.9 %**. Inside T5,
`beans:` is the most common commit prefix (290) against 128 `probe` and 85 `lean`.

### 6.2 Corrections of corrections — the signature of uncoordinated work

1,773 of 11,622 non-merge commits (**15.3 %**) carry self-correction language; 147 of 635 audit
docs do, 28 of them outright retractions. The cases where a correction itself needed correcting:

- **the M₁ / Magnus kernel** (`k5r5`, `o6ov`, `x631`): `2026-09-03-covariance-kernel-M1-k5r5-weight-bug-retraction-retracted.md`; 42 `covariance-kernel-M1-*` docs in the window; **13 `magnus-*` docs on 2026-09-05 alone**, the arc recomputed after `wdij` found the canonical atom word non-monotone and its producer dead on `main`; `2026-09-06-c1-is-stale-on-the-reordered-atom-word.md` then stales `pdg9`'s derived c₁.
- **`cds1`**: `0b7d4f8b04` "the projection is PARTIAL — RETRACTS my own merged #6875"; `39228bfbf1` the wrong Pochhammer in Lean, 507 % off.
- **c₂** (`qqm4`/`yaig`): "c₂ has nothing to predict from — WRONG"; "my retraction of that mechanism was wrong"; "k(A) form REFUTED at A = 5 — and my prediction was wrong too".
- **false axioms**: four SDP-uniqueness axioms prove `False` (`i6u4`, 09-05); a second family the next day; two false nucleon-mass axioms (09-04, still on `main`, `qou-4paj`).
- **duplicated derivations retracted**: `2026-08-19-qou-shrp-duplicated-corpus-euler-maclaurin.md`; `2026-08-25-4b-corrections-duplication-and-two-fronts.md` (a Lean file re-deriving `binding_mn_milnor_linking.py` "in the same words").
- `a61496dbc` (09-08) **reopens 18 beans whose own body says they are open**.

### 6.3 Duplicated / uncoordinated pairs (same target, no cross-citation between the bean bodies)

1. **`k5r5` (99 commits, 08-21 → 09-08) vs `o6ov` (99 commits, 08-30 → 09-05)** — both on the odd-moment / Magnus `tr(ρ_λ ω²)` kernel; **zero cross-citations** among `k5r5`/`o6ov`/`x631`/`za3q`/`omr7`.
2. **Convention-C excision: nine trackers** (`wgta`, `janm`, `htsi`, `t9r1`, `eea0`, `okkz`, `jyqd`, `fq0f`, `47sx`), linked only `cds2↔8iru` and `htsi→t9r1`; no canonical ledger.
3. **q₀ gates: sixteen beans**, cross-reference density ~10 %; `3f7a`'s own finding is that the two red q₀ gates are *one* unfinished migration.
4. **Programme-articulation sessions: five in 25 days, none citing a predecessor** — `1qug` (08-14, SM-26 cheat sheet), `vibo` (08-29, m_n(K) magnitude gap), `m2ay` (08-30, canonical-derivation magnitude cheat sheet), `ggdk`/`65jh` (09-03, SM-26 status), `37j2` (09-07, the 1 ppQ reanalysis). This document is the sixth; §0 names all five and states what it adds.
5. **Trace-tower c₁/c₂ vs the χ-carrier caches**: `hu1f`, `9yt9`, `eddc`, `k54t`, `92u9` do not cite `pdg9`/`qqm4`, and `92u9`/`eddc`'s intra-ordering change is what staled `pdg9`'s c₁.
6. **Duplicate beans** — **corrected 2026-09-08 (C7 pass, front-matter-stripped `diff`)**: only `yh08`/`zo4i` is byte-identical (`zo4i` scrapped); `rcgi`/`1lh4` and `9552`/`0xmm` are an empty stub beside the landed record, `vkmt`/`c8p8` and `ifot`/`wxg1` already self-declare the duplication, `82ur`/`5380` are different findings — cross-referenced, not scrapped. The thread-clustering pass over-stated this item. Plus **seven "raw-float64 ratchet is red on main" beans** (08-11 … 09-06) for one recurring event, each with its own offender list — now cross-referenced to `qou-sknx`.
7. `edt7` vs `bhzt` ("what replaces the multiplicative assembly", both 08-30, no cross-reference).
8. Fourteen beans with a byte-identical "Infra-blocked" next-step, 13 created in six seconds (`2026-08-30-infra-blocked-is-one-verdict-stamped-fourteen-times.md`).

### 6.4 The primary coordination document does not record the work

`docs/canonical-derivation-cheat-sheet.md` (last touched 09-06) contains **zero** occurrences of
`brng`, `k5r5`, `o6ov`, `magnus`, `phir`, `kwoa`, `k4oq`, `auq3`, `pdg9`, `qqm4`, `yaig`, `99qc`,
`aemx`, `dg07`, `768r`, `17mq`, `bn8e`, `hu1f`, `full tower`, `CoordinationSaturation`,
`ConventionDAdmissibleRoots` `[M]`. Its §0 row 11 still reads "🟢 derived; `c_k` truncation" while
AGENTS.md (09-05) scopes the functional as inadmissible and the 09-07 reanalysis says the ladder
does not converge under D. Row 9b still leads with "bond-count × hyperbolic volume" and a
2026-07-20 keystone; the 08-29 deuteron ruling, the 08-30 saturation lemma, the 09-05 log
functional and the "no knot-selection" ruling are absent. Of sixteen threads, only step 2 and one
line of the deuteron ruling reached it.

### 6.5 What is currently claimed (`in-progress`, 463 `qou-*` beans), by thread `[M]`

Numbers in brackets are claims **not updated since before 08-25**:
unclassified tail **220 [116]**; T5 binding 42 [10] — three of them (`0c19`, `eptr`, `dk8a`) are
the same open problem as `brng`, which is `todo`; T10 precision 33 [13]; T13 process 25 [16];
T4 Hecke/Lean 22 [12]; T11 17 [8]; T3 q₀ 17 [3]; T6 mass channel 16 [4]; T9 volume 14 [10, ten
stale]; T2 convention 12 [5]; T1 Q_β 10 [2]; T7 Δ_pn 9 [2].

**Blunt reading.** Four weeks produced one derived coefficient (c₁, already stale), one derived
binding functional, a large set of sorry-free structural exclusions, and a substantial Hecke
foundation in Lean that the programme document does not reference. The hardest kernel was
attacked by two ~100-commit beans that never cite each other; convention-C excision and q₀ gating
are tracked in 9 and 16 uncross-referenced beans; the programme was re-articulated five times
without lineage; and the lever the corpus itself ranks cheapest — the Q_β functional decision
(`qou-99qc`, an owner call, still `todo`) and α_em — received the least effort.

---

## 7. The priority gaps, ranked by derivational cleanliness — stated as a delta against the 2026-09-07 list

The 09-07 reanalysis ranked five attacks: (1) α_em on the dashboard — **done 09-07**; (2) a
non-ladder Q_β derivation; (3) the binding shape residual as an edge-set question; (4) say the
μ–p residual is structural; (5) do **not** extend the c_k ladder or consolidate onto the most
accurate α_em. This audit agrees with all five and changes the list in three ways: it separates
the *owner decisions* that are cheap and gating from the *research* that is not; it adds the
step-9a joints (§2.2), which the 09-07 list did not see because it audited numbers rather than
derivations; and it adds the coordination repairs (§6), because the measured 15 % correction
rate is itself the largest single drag on the programme.

### 7.1 Owner decisions — cheap, gating, and currently `todo`

| # | decision | bean | what it unblocks | default if nothing is decided |
|---|---|---|---|---|
| D1 | **what ε means** in `Q_β = \|ε(Δ)\|·E₀` (augmentation `σ ↦ q`, or a non-trace element, or retract Q_β as a prediction) | `qou-99qc` | the only lever on **three of six** L2 rows; `qou-cds1`'s ladder cannot start without a base | the published 0.17 % keeps being read as live and re-derived (it has been once) |
| D2 | ~~the **Plancherel weight family** in Φ_k~~ — **ALREADY RULED (owner, 2026-09-05, `qou-oots`): Molien `f^λ q^{−κ} dim_q/[n]_q!` is canonical, `d_q²/D²` kept as a labelled comparison arm.** This row was written as open by mistake; corrected 2026-09-08 (§8). Re-affirmed by the owner the same day. | `qou-oots` | the α_em-axis triage (PR #6840) is what remains in the bean | — |
| D3 | **close or re-scope `qou-e5jf`** against ruling A, and retire the census rows from the production table (`prediction_method: canonical-trace` on selected numbers) | `qou-e5jf`, `qou-fcn8` | stops the retired ²H `Vol(6₂)` number and the census A = 3 rows being republished as derived | the 2026-09-07 witness keeps publishing them |

### 7.2 Research — the four un-derived objects, in order

| # | object | what "closing" means | live front | cost / risk |
|---|---|---|---|---|
| R1 | **the Q_β functional on an admissible base, then its ladder** — W1 of the 09-07 list | a derived phase (or a non-phase mechanism) for the N = 1 factor on the base D1 selects; then a D-frame ladder with structural `c₂ = −1` as the self-consistency check | `qou-pdix` → `qou-cds1`; PR #7149 reduces the |q| = 1 route to the algebraicity of Vol(4₁) | sessions, not turns; the honest outcome may be "no D-frame derivation", turning three rows *undefined* rather than inaccurate |
| R2 | **the extensive binding term** — the 3-body cumulant sign | a mechanism giving `b₃ > 0` that is not pairwise-additive, not multiplicative with `f_pn ≤ 2/3`, not a count channel, not an expressible edge set; per `qou-brng`, the ribbon-category fact behind mutual-vs-self linking | `qou-brng`, `qou-edt7`; infrastructure `qou-301d` (PR #7153 landed TowerSpan); **signs first**: `qou-vbyi` diproton | binding is not an L2 row, so this moves no scored number; it is the framework's main *structural* gap |
| R3 | **the step-9a joints** (§2.2): `/q³`, the integers 2 and 6, the F_Bor normaliser, `ℏ_q = 1 − q⁻¹`, muon = 4₁ | formalize-first — a Lean statement of what would *force* each, or an honest demotion of `conj:proton-borromean-assembly`'s class fields from "identified" to "chosen" | `qou-24w9` (`/q³`), `qou-mrel` (−6 m_e), `qou-n1dj` (TL vs H₃), `qou-6gf9` (m_μ as leading term), `qou-4paj` (two false axioms — a one-commit fix) | m_p cannot test any of these (q₀ is pinned on the same identity); the payoff is a derivation, not a number |
| R4 | **α_em**: reconcile the two derivations 470 ppb apart and discharge the Witten-κ `sorry` | one α_em, with `gram_kappa_numerical_value` proved or the dependence made an explicit §3b class | `aemx`, `qou-15sj`, `qou-gwio`; content sibling `gram-determinant-plancherel-ratio.lean:164` | cheap to *measure* (72 commits in four weeks — the least-worked critical item); the `[10]_q` linchpin is asserted |

The μ–p residual (W2) stays where the 09-07 list put it: **no attack**; state it as structural on
the dashboard. It is plausibly the same object as whatever replaces the Q_β base, and its target
is below the calibration floor at the proton pin in any case (§1.3).

### 7.3 Coordination repairs — the drag on everything above

| # | repair | evidence |
|---|---|---|
| C1 | **update the cheat sheet §0 rows 9b and 11** (and §9.3) to the 09-05 log functional, the deuteron ruling, the saturation lemma, and the inadmissible-functional scoping; cite the T4 Hecke foundations | §6.4: zero occurrences of any four-week bean in the primary coordination document |
| C2 | **merge the M₁ / Magnus fronts** (`k5r5`, `o6ov`, `x631`, `za3q`, `omr7`) under one bean with a shared ledger | two ~100-commit beans, zero cross-citation, a retraction-retracted |
| C3 | **one ledger each for convention-C excision (9 beans) and the q₀ gates (16 beans)** | §6.3 items 2–3 |
| C4 | **fix the two m_n values on `main`** (facade +501 ppb vs dashboard 0.9 ppb) — stamp both with their functional and frame, or drop one | §2, `qou-khue` |
| C5 | **tighten the L1 assertion tolerance 1e-9 → 1e-15** so the gate matches the claim; correct the `cross-check-trM-1ppb` prose ("~1.8e-4") that is four orders stale against its own data | §1 / L1 caveats |
| C6 | **refresh `docs/precision-goals.md`** (≈ 20 stale figures, Appendix A) and the 1/5 → 1/6 count in AGENTS.md | §0 |
| C7 | the **duplicate and stale claims**: six byte-identical bean pairs, seven "ratchet red" beans, 116 unclassified `in-progress` claims untouched for two weeks | §6.3, §6.5 |

### 7.4 Do not

- extend the c_k ladder, or z-swap it (proved invalid by `decayLadder_zC_threeRow_ne_zero`);
- choose between `z = q` and `z_D` by residual, or between the three α_em constructions by residual;
- re-open knot selection, per-λ re-weighting, scale-rule probes, the Δ_λ magnitude ansätze, or any
  scope-(b)-excluded assembly in §3.3;
- quote the 1300× binding-functional gain, the 0.17 % Q_β, or the census A ≤ 4 rows as L2 progress;
- close a bean whose subject is an open conjecture (rule 13a) — `qou-q3np`, `qou-e5jf` and the
  §5.2 classes stay open until the mathematics closes.

---

## Appendix A — stale figures in `docs/precision-goals.md` `[M]`

| line | says | live |
|---|---|---|
| 11–12, 105, 127, 606 | 50 / 40 dps; `COMPUTE_DPS_DEFAULT = 50` | 70 / 60 / guard 10 (`qou_substrate.precision`) |
| 38, 240, 256, 265–267, 588–590 | 1/5 scoreable, `scoreable_total = 5` | **1/6**, α_em⁻¹ added 2026-09-07 |
| 65 | σ_theory "m_p: 242 ppb; m_avg 2.89 %" | absolute-mass rows excised 2026-08-11 |
| 66, 248 | m_e σ 0.29 ppb | 0.313 ppb (CODATA 2022) |
| 108–114 | "gate must be tightened 1 ppb → 1 ppQ … still gates at 1 ppb" | float path fixed 2026-06-29; the assertion tolerance is *still* 1e-9 |
| 185–189, 300–305 | "Q_β at 0 ppQ (exact) … Habiro-exact 5.744 ppb" | 1279 ppb, convention C, z = 1 inadmissible; contradicted by L238 |
| 201–203, 586 | 8 atoms, `max_rel_delta = 0.0`, 92.79 ppb structural floor | 6 atoms, 1.2e-49, 2.78e-8 ppb |
| 251, 294 | Q_β "CAL-3 cross-check" | CAL-2 proxy (ruling 2026-06-26) |
| 290–292, 361–364, 464–465, 470, 546 | Q_β 1.25 ppm / 160×; m_n 1.04 ppb / 416×; Δ_pn 755 ppb / 159×; 437×; 964×; 1248 ppb | 1279 ppb / 164.0×; 0.903 / 176.7×; 658 / 151.7×; N/A; 970.2×; 1279 |
| 358–359 | "Met: m_e, m_p" | m_p not scored (anchor round-trip); contradicts L249 |
| 372–378 | Subgoal-2 "requires q₀ derivation" | q₀ route forever gated |
| 154, 538–541 | μ–p separation 11.537 ppb | 11.614 ppb at the CODATA-2022 pin |

## Appendix B — method and limits

- No producer was re-run except `mass_binding_dashboard.py --group low` (no witness; float64,
  `qou-4ohh`); `mpmath` ≥ 1.4 was installed for it. The working tree was left clean.
- The four-week clustering keys on bean ids in commit subjects; 20 % of commits fall in an
  unclassified tail. "Load-bearing" for conjectures is `uses[]` adjacency to chain chapters.
- The Lean sorry count is a comment-stripped scan cross-checked by raw grep; `lake` / `lean` were
  not run. Instance absence for §3b classes was checked by grep for the word `instance` and every
  hit was prose; instances declared in other files were not ruled out.
- Six sub-agents produced the front reports (mass chain, binding chain, Q_β / c_k / f-map, L1/L2
  dashboards, conjecture inventory, thread clustering); every figure they carried from a witness
  or audit doc is marked `[W]` / `[D]`, and the ones re-measured here `[M]`.
- Session beans: milestone `qou-tonv`; tasks `qou-zw8t`, `qou-tatx`, `qou-xyqh`, `qou-xzo8`,
  `qou-b9xt`, `qou-lxdq`, `qou-z024`.

---

## 8. Owner response and rulings (2026-09-08) — recorded, with what changed in this document

The owner answered the §7 option list the same day. All four items were selected, with one
ruling added. Verbatim, from the structured reply:

> *"All selection of great words should be done through gamma gamma production and the
> semi-definite product solutions at q_0. Shouldn't use census."*

Reading (agent's, marked as a reading): *braid* words. Every canonical braid word is to be
**selected** by the γγ (Breit–Wheeler pair-production) construction — words assembled from
pair-production vertices, the `σ₀σ₁⁻¹ = γγ̄` reading already in
`gamma_gamma_pair_production_decomposition.py` and `breit-wheeler-pair-production-derivation.md`
— with the **confinement SDP at q₀** (PSD Wedderburn projections; `sdp_gamma_gamma_to_qqbar.py`,
`nucleus_operator_selection_sdp.py`, `prop:confinement-sdp`) picking the canonical `T_w`. Census
volume-matching is excluded as a selection mechanism. **Carrier bean: `qou-ales`.**

### 8.1 What the ruling bears on in this document

- §2.2 items 1–3 — the nucleon word, the quark → crossing template and the colour-weighted atom
  word — are exactly the *chosen* joints the ruling says are to be *selected*. Under the ruling
  they stop being template assignments and become outputs of step 10.
- §3.1 knot-id "admitted fit" and `conj:canonical-knot-id-sdp`: the SDP route is the one named.
- §3.4 / `qou-vbyi` (the diproton sign): every in-algebra direction is closed and the bean asks
  for a "structural change"; a pp word *selected* by γγ + SDP rather than *assigned* by
  `uu → σ` is that candidate. R2 "signs first" therefore runs through `qou-ales`.

### 8.2 Corpus state of the named route `[M]`

| piece | state |
|---|---|
| `sdp_gamma_gamma_to_qqbar.py` | a **starter scaffold** (witness 2026-08-29): the H₂ γγ → e⁺e⁻ demo only (`σ₀³` has `tr_M ≈ 0.73` at q₀); the H₃ skeleton is outlined; "full SDP solve deferred". Its own discipline line already reads "NO Vol_hyp. NO census." |
| `nucleus_operator_selection_sdp.py` | sweeps `n_target = \|tr_M(W_atom)\|` taken **from the existing atom word** — circular as a selector; and the LP it solves is proved degenerate (§3.1) |
| `qou-vd7j` | the 0/3558 admissibility result is an **over-determination artifact** — the net row `1ᵀx = A` is inconsistent with the six Frobenius rows for every nucleus; the cheap fix (drop the redundant row or use the consistent net) was named 2026-08-02 and never done; heavy-A f64 overflow is separate |
| `breit-wheeler-pair-production-derivation.md` | bare `γγ = σ₀²` lands 1.6 % short of `2m_e`; the "colored photon" admixture carries parameters `φ₀, φ₁, φ₀₁` that must be **derived**, not fitted to `2m_e` |

**What closing means, formalize-first:** (1) state in Lean what makes a word γγ-produced and
what the SDP selects, before any search; (2) fix the `qou-vd7j` net-row over-determination and
re-run admissibility, reporting per nucleus which words survive **without reading AME**; (3) only
then compare the surviving words for p, n, ²H, pp, nn against the template — the diproton sign is
the first falsifiable output. Default if nothing is done: words stay template-assigned and §2.2
stays "chosen".

### 8.3 The three decisions

| # | decision | recorded where | consequence |
|---|---|---|---|
| D1 | **ε(Δ) := the Markov trace at `z_D = q³/(q²+1)` (option C), by owner ruling the same day, following D7.** Sequence: the owner first selected the augmentation (on an option carrying the agent's recommendation); `13bb8243d8` on `main` then showed the augmentation *is* the Markov trace at `z = q`, so the question is which Markov parameter and D7 (convention D governs the decay channel) selects `z_D`; put back with both options framed (§8.5), **the owner chose `z_D`** | `qou-99qc` (2026-09-08 appends); AGENTS.md scoping note | Q_β base = 0.4447004 MeV (−43.157 %); the published 0.17 % is retired as the base and kept as the C-frame / z = 1 historical cross-check; the augmentation (+12.470 %) is the other admissible point, proportional to it; `qou-cds1` has its base and S1 reduces to the phase (`qou-pdix`); dashboard rows Q_β / m_n / Δ_pn to be re-scored on the `z_D` base — **not done here** |
| D2 | **Molien** — not a new decision: ruled 2026-09-05, re-affirmed today | `qou-oots` | this document's §5.3, §5.5, §7.1 said the choice was open; **that was my error**, corrected above |
| D3 | not selected as such; the owner's ruling above supersedes it — the census rows are retired by the ruling, not by a bookkeeping close of `qou-e5jf` | `qou-ales` | `qou-e5jf` stays open (rule 13a) with a cross-reference |

### 8.4 Coordination repairs authorised (C1–C7) — what landed on this branch

Recorded in the commit log of PR #7159 as they land; the bean-hygiene items (C2, C3, C7) and
the document refreshes (C1, C6) were run as two parallel tranches and are itemised in the PR
body. C4 (the two live m_n values) and C5 (the L1 assertion tolerance) are noted below.

- **C2 / C3 / C7 — landed.** Magnus fronts `k5r5`, `o6ov`, `za3q`, `omr7` parented to the epic
  `qou-x631` with cross-references (zero existed); convention-C family (9 beans + `cds2`) cross-
  referenced to the canonical ledger `qou-wgta` (not `cds2`, whose own body names `wgta` as its
  predecessor); q₀-gate family (16) to `qou-1c4y`; ratchet-red beans (7) to `qou-sknx`; one
  byte-identical duplicate scrapped (`zo4i`). 49 bean files, one status change, four parent
  changes. Three empty-stub duplicates (`0xmm`, `vkmt`, `1lh4`) are left open with a note — the
  owner may scrap them.
- **C4 — the two live m_n values.** Recorded on `qou-khue`: neither is canonical until both
  witnesses are re-scored on the augmentation base (D1) and stamped with functional + frame. Not
  a witness edit in this PR (producer re-run under D; ask-before-change).
- **C5 — the L1 gate now gates at the 1 ppQ it claims.** `onepb_status_dashboard.py`'s two
  assertions tightened `1e-9 → 1e-15` (tightened, never widened); producer re-run with `clarabel`
  restored to the environment so the provenance block does not degrade; both assertions pass at
  `7.3e-50` and `1.2e-49` `[M]`. The only other fields that moved are `computedAt` / `commitSha` /
  `scriptHash`. The `raw-float64` warning on `structural_max_non_anchor_delta_ppb` is
  pre-existing on `main` (same `float` type there) and is not introduced here.

### 8.5 Open on the owner: which Markov parameter is ε — the augmentation or `z_D`

Commit `13bb8243d8` (bean `qou-99qc`, on `main` after this branch diverged) removes the dichotomy
the D1 option was written on. Both admissible candidates are points of one Markov family
(`ε = tr_M^z`, `z ∈ {q, z_D}`), so the decision is a *convention* question, and the owner's D7
ruling (2026-09-07) already assigns convention D to the decay channel. Under D7 the consistent
choice is `z_D` (Q_β = 0.4447004 MeV, −43.157 %); the augmentation (`z = q`, +12.470 %) is the
strictly finer one-row truncation and is not convention D. The owner selected the augmentation
on an option that did not carry this fact. Neither base is wired; the question is put in chat
with both options framed, and this row records the outcome when it arrives.

**Outcome (owner, 2026-09-08, same session): A — `z_D`, follow D7.** Recorded on `qou-99qc`, in the AGENTS.md scoping note, in `docs/precision-goals.md` and in the cheat sheet row 11. The residual the framework now carries for Q_β on its canonical base is **−43.157 %**; that number is a documented honest miss, not a fit, and is the starting point for the D-frame ladder.
