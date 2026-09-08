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

