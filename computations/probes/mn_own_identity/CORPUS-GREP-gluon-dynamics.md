# Corpus-grep: QCD gluon DYNAMICS in qou (2026-11-22)

memory: MEMORY.md (336 lines, 845e2f82001) + library-and-staleness-traps.md, resolved-topics.md (grepped for gluon/colour/Casimir only)

Question: does the corpus already hold any of the following? Running α_s(Q²),
β₀ / beta function, asymptotic freedom, antiscreening, three- and four-gluon
vertices, gluon self-coupling, f^{abc}, Casimir scaling C_A/C_F = 9/4,
colour octet/singlet, a string-tension value, flux tube, Λ_QCD, 't Hooft
double-line, Drinfeld–Kohno / infinitesimal braid relations, Faddeev–Popov ghosts.

Branch `claude/mn-own-identity-2026-11-21`. Read-only search. The two files in
this directory, `PREREGISTRATION-three-gluon-vertex.md` and
`PREREGISTRATION-quark-gluon-vertex.md`, are the originating work and are left
out of every count below.

## Commands run

```sh
# step 0 (CLI; it works, and emptyRoots = [] for every query)
bun scripts/corpus-search.ts "<topic>" --limit 200
#   topics: gluon | strong coupling | asymptotic freedom | string tension |
#           Casimir | structure constants | Drinfeld-Kohno
# paths 1-4 and 6: count per path, with ripgrep
EX='--no-ignore --glob=!**/.lake/** --glob=!**/__pycache__/** --glob=!**/*.pyc'
rg -l -i $EX -e "<regex>" docs/audits folio computations docs/coordination library beans/defs
# path 5, library tiers
grep -i -n -E 'QCD|gluon|Yang.?Mills|confin|Kohno|Faddeev|...' library/INDEX.md
rg -l -i -e "<regex>" library/*/sections     # tier 3
rg -l -i -e "<regex>" library/*/ocr          # tier 4
ls uploads | wc -l                           # 0: no un-ingested PDFs
```

**Trap found during this run.** Without `--no-ignore`, ripgrep obeys
`.gitignore`. `beans/` is gitignored on main (it is branch-mounted), so
`rg -l gluon beans/defs` returns **0** and `rg -l --no-ignore gluon beans/defs`
returns **73**. Every beans count here uses `--no-ignore`. Plain `grep -r` is
not affected. (`content/` is now `folio/`, and `.beans/` is now `beans/defs/`;
the mount holds 5875 beans.)

Raw per-path file counts, with `--no-ignore`, `.lake/` excluded:

| topic regex (abridged) | audits | folio | computations | coord | library | beans |
|---|---|---|---|---|---|---|
| α_s / running coupling | 59 | 55 | 133 | 4 | 77 | 32 |
| β₀ / beta function | 12 | 8 | 48 | 2 | 80 | 12 |
| asymptotic freedom | 2 | 6 | 0 | 0 | 64 | 3 |
| antiscreening | 2 | 2 | 0 | 0 | 0 | 1 |
| three-gluon | 0 | 0 | 5 | 0 | 1 | 1 |
| four-gluon | 0 | 3 | 2 | 0 | 0 | 1 |
| gluon self-coupling | 3 | 1 | 16 | 0 | 4 | 3 |
| f^{abc} / structure constants | 35 | 83 | 49 | 1 | 238 | 17 |
| C_A / C_F / 9/4 | 168 | 209 | 952 | 15 | 250 | 155 |
| colour octet/singlet | 15 | 23 | 20 | 4 | 13 | 10 |
| string tension | 3 | 3 | 0 | 0 | 4 | 2 |
| flux tube | 9 | 3 | 6 | 3 | 133 | 7 |
| Λ_QCD | 0 | 0 | 0 | 0 | 5 | 2 |
| 't Hooft / double-line / large-N | 12 | 12 | 19 | 0 | 187 | 7 |
| Drinfeld–Kohno / infinitesimal braid / KZ | 32 | 105 | 41 | 4 | 283 | 24 |
| Faddeev–Popov / BRST | 2 | 1 | 1 | 0 | 30 | 1 |

These counts mostly measure homonyms: `alpha_shift`, `9/4` in unrelated
fractions, `structure constant` of Stokes data, `singlet` in Hecke blocks,
`Faddeev` in the quantum dilogarithm. The verdicts below come from reading the
hits.

## Overview: one assessment covers most of the list

Bean **`qou-pa2f`** ("Assess: is the QCD claim SU(3) gauge theory or a 3-label
colour index", `in-progress`) records a subagent measurement: *"NO SU(3) …
'LieAlgebra' occurs ONCE in QOU code and it is sl(Fin 2) C; no gauge
connection, no Yang-Mills functional … NO beta function, NO running coupling,
NO asymptotic freedom, NO Wilson loop, NO area law, NO string-tension value."*
It also records that `ColourObstruction.lean` proves that the tetraplectic
SU(2) cannot be colour. Its verdict is *"QCD is a vocabulary map"*. This run
confirms that reading for the dynamical items. **The bean is a secondary
source.** I checked its claims against the files listed below, not taken them
on trust.

**A second trap: resolutions that are not on disk.** Several beans state
"Resolution (2026-11-19) … proved in X.lean (0 sorry)" for exactly these
topics. The files do not exist: `git ls-files | grep -c <stem>` returns 0 for
`RibbonPantBernKosowerGluonVertex` (bean `qou-t3zb`: f^{abc}, Jacobi, Fierz,
ghost-free three-gluon vertex), `FourLoopQCDRunningAndWeinbergRGE` (bean
`qou-n1ks`, scrapped: β₀..β₃), `InfraredQFTSubsumptionAndPartonMoments` (bean
`qou-bgq9`: α_s, 4T relations), `BringThetaBruhatAndMesonH3` (bean `qou-3ttt`:
Casimir 4/3 → 8/3) and `ColorVsCharmAdditiveSector` (bean `qou-pa2f`
cross-reference). The 2026-11-21 physics-scope re-check, recorded in each of
those beans (issue #8810, gap bean `qou-w12g`), says the same. **Do not cite
any of these as held.**

## Per topic

| # | topic | verdict | where, and what it actually is |
|---|---|---|---|
| 1 | running α_s(Q²) | **not found** (gap beaned); literature held as background | The corpus has no map from a trace to α_s. Gap bean `qou-5iaz` is `in-progress` ("no coupling extraction; blocked on SU(3) action", blocked by `qou-ni4b`). `folio/.../appendix-standard-model/sm-params-gauge-couplings.md`: *"α_s \| open"*. Two candidate formulas circulate, and `docs/audits/2026-09-03-sm-26-term-status.md` §4.3 labels both scale-free and conditional: `1/α_s = q^p[9]_q` with p undetermined (`computations/alpha_k_selection_rule_conditional.py`, invariant α_s·α_W = α_EM) and the fit-shaped `α_s(M_Z) = q⁻¹/[7]_q`. Neither runs with Q². `docs/audits/2026-10-10-level3-su3-channel-test.md` row 2 records α_s as untestable. |
| 2 | β₀ / beta function | **not found as QCD β₀**. One sign-rule label exists | `lean/QOU/StandardModel/ElectroweakVevGaps.lean:210`: *"Sign rule: anti-screening (b₀ < 0) gives s = −1"* takes b₀ as an **input** for the EW-vev loop sign; nothing computes it (bean `qou-myxi`). β₀ = 11 − 2n_f/3 is stated nowhere in folio/computations/docs. The β₀..β₃ "proof" (`qou-n1ks`) is scrapped and its file is absent. Library: `arxiv-alg-geom-9705010v1` §4 defines a beta function and asymptotic freedom in general terms. No held source states QCD's β₀ (the explicit-coefficient grep is empty). |
| 3 | asymptotic freedom | **prose only, no derivation**; library: background mentions | `folio/.../predicted-spectra/force-knot-identification.md:48` ("strands of T_{2,9} locally parallel … This yields asymptotic freedom"); `mass-endomorphism/categorical-chain-convergence-mechanisms.md:59` ("categorical analog"); `observations/color-confinement-observation.md:22` ("effective q flows"). `knots-particles-confinement/confinement-universality.ts:25` **withdraws** the earlier "categorical expression of asymptotic freedom" framing. Beans `qou-5iaz` option 3 and `qou-jsx5` treat it as OPEN research (q-CLT flow). Library: mentioned in passing in `klein-few-body-systems-…`, `s10052-020-08615-2`, `physrevd111094513`, `arxiv-hep-th-9408099v1` (Seiberg–Witten, N=2). Hits on `arxiv-math-0405258v2` are Voiculescu "asymptotic freeness", a homonym. |
| 4 | antiscreening | **not found** (label only) | Only the label "broken non-abelian anti-screening" in `lean/QOU/Archimedean/BringSchwingerNormalizationDerivation.lean:60,352` and `docs/audits/2026-11-20-ew-vev-gaps.md:128`, which states *"No corpus result derives it"*. Library: 0 docs (sections and ocr). |
| 5 | three-gluon vertex (f^{abc} ggg) | **not found** (homonym) | Every hit is the braid crossing count: "the MINIMUM is three gluon crossings" (`computations/qbeta/qbeta_adjunction_ilp_probe.py`, `qbeta_crossing_budget_gluon_parity_probe.py`). There is no f^{abc}-type vertex. The `qou-t3zb` resolution is absent from disk. Library: one passing mention ("gluon self-interaction", Klein, few-body lattice EFT, sec-001). |
| 6 | four-gluon vertex | **not found** (homonym) | "the four gluon candidates" means four candidate braid letters: `lean/QOU/QBeta/ECatBlockDecomposition.lean:221`, `LetterSumBlindness.lean:199`, `computations/qbeta/qbeta_ecat_pair_kernel_probe.py:4`, `computations/probes/ohara_link_energy/README.md:26`. Library: 0. |
| 7 | gluon self-coupling | **held, but the corpus uses the name for something else** | In the corpus, "gluon self-coupling" = **2·σ₀ crossings appended to each nucleon word** (9 → 11 letters, "ILP-derived"): `computations/substrate/hecke_core_symbolic.py:234`, `build_atomic_braid_recipe_{p,n}_chain.py`, `computations/qbeta/integer_lp_gluon_convention_d.py`, `docs/audits/2026-08-08-borromean-trace-convention-forcing.md:55`. The one Lean statement about it, `lean/QOU/QBeta/GluonVertexPsdParity.lean` (0 sorry), proves that the H₂ vertex σ₀^k is PSD ⇔ k even. It is **not** a non-abelian A³/A⁴ self-interaction. |
| 8 | f^{abc}, su(3) structure constants | **not found** in folio/computations; library only | No Lean or Python defines Gell-Mann f^{abc}. Bean `qou-t3zb` (`todo`, re-scoped to math only) is the target, and its claimed proof is absent. Octonion route: `lean/QOU/Eightfold/OctonionicSu3RankObstruction.lean` (λ_a ↔ e_a, a rank obstruction) and `docs/audits/2026-08-26-octonionic-su3-two-routes.md`. `ColourObstruction.lean` is sorry-free (its one `sorry` match is the word "sorry-free" in a docstring). Library: `arxiv-0908.3425v1` (ChPT), `arxiv-1105.2919v1`, `arxiv-1205.4619v1`, `arxiv-math-ph-0012035v3`, `arxiv-hep-ph-0601023v3`, `arxiv-1107.1559v1` (the last was triaged *not relevant* in `docs/audits/2026-08-25-octonion-division-algebra-upload-triage.md:63`). |
| 9 | Casimir scaling C_A/C_F = 9/4 | **partially held**: C_F is held, the 9/4 ratio is not found | `folio/.../eightfold-way/sl-n-color-framing.md:8,17` defines `C_F = (N²−1)/2N` and the one-gluon colour factor `c_R = ½(C₂(R) − 2C_F)`. `lean/QOU/Braiding/SlNFramingColourFactor.lean` (0 sorry) proves that SU(N) framing q^{-1/N} gives the ratio `\|C(3̄)/C(6)\| = (N+1)/(N−1) = 2`. Probe: `computations/probes/sl_n_framing_colour_factor_probe.py`. Bean `qou-sl3f` (`in-progress`, owner decision open). The level-3 audit (`2026-10-10-level3-su3-channel-test.md` row 4) says C_F = 4/3 and C_A = 3 are "pure group theory, no corpus formula reading them off a Markov trace". No file states C_A/C_F = 9/4 (the grep for `C_A/C_F` and `Casimir scaling` matches only the absent-file bean `qou-3ttt` and the parent's preregistration). The sl₂ split Casimir Ω appears in KZ: `mass-endomorphism/kz-connection-sl2.md`, `lean/QOU/KZ/Drinfeld/Casimir.lean`. |
| 10 | colour octet / singlet | **partially held**: singlet structure is held, there is no adjoint/octet gluon | Singlet: `lean/QOU/Eightfold/TrialitySelectionRule.lean:55` (0 sorry: a two-quark object has no colour singlet at any q); `SlNFramingColourFactor.lean` (Λ^N V singlet braids trivially); `appendix-knot-operations/borromean-gluon-content.md` (the Borromean NF as a colour singlet, prose); `computations/probes/level_three_colour_channel_probe.py`. "Octet" in `eightfold-way/` is the **flavour** octet, a homonym. No colour-octet gluon representation exists. `ColourObstruction.lean` and `qou-pa2f` record that the framework's SU(2) is not colour. |
| 11 | string tension (value) | **not found** (dictionary only) | `observations/confinement-curvature-rank.md:9` ("String tension = curvature 2-cocycle"); `mass-theory/confinement-categorical-proof.md:34` and `.lean:21` ("plays the role of"); `docs/audits/2026-09-04-depth-one-is-empty.md:111`. No value anywhere: `2026-10-10-level3-su3-channel-test.md` row 7, *"needs a scale and a map; none in corpus"*, and `qou-pa2f`. Library: Sine-Gordon "string tension" in `symmetry-04-00039-v3` (Knots on a Torus model), `arxiv-2502.02662v1` (2D Yang–Mills string dual), `arxiv-1508.01458v1`. No lattice σ value. |
| 12 | flux tube | **held as topology and obstruction, no dynamics** | `lean/QOU/ParticleInteractions/MesonFluxTubeReduction.lean` (0 sorry: two structural obstructions to a canonical D-meson flux-tube braid); `computations/meson_fluxtube_topology_probe.py`, `jpsi_boundstate_mass_probe.py`; `docs/coordination/sm-26-parameter-chip-away.md:35,60,120`. Gap bean `qou-qpj9` (`todo`) and its children `qou-3ttt`, `qou-k4l2`, `qou-886m` (all `todo`). Bean `sdcb` (`completed`: pion "snapping energy" vs the SDP, a Lean sense-check). Library: helicity/linking flux-tube papers (`1992evansberger` ocr, `procrsoclondona92` ocr, `arxiv-0808.1533v3`, `arxiv-1012.5432v4`), not QCD. |
| 13 | Λ_QCD | **not found** in authored corpus; library only, as an input | folio uses Λ_QCD only as a denominator: `observations/deconfinement-golden-threshold.md:42` (k_B T_c/Λ_QCD), `observations/observables-algebraic-independence.md:11` ("cannot be expressed algebraically in ℚ(q₀)"). Beans `qou-5iaz` (Λ_QCD before α_s, "neither before `qou-ni4b`") and `qou-jsx5`. Library: lattice and Cottingham n–p papers (`arxiv-hep-lat-0003021v3`, `arxiv-hep-lat-9912004v2`, `s10052-020-08615-2`, `arxiv-2008.05806v2`, `arxiv-1506.06747v3`, `arxiv-1704.06561v2`, `arxiv-2608.15898v1`, `arxiv-0811.1338v1`, `lattice2021-543`) use Λ_QCD as a phenomenological input. |
| 14 | 't Hooft double-line / large-N_c | **not found** (homonym) | Every 't Hooft hit is the Cellular Automaton Interpretation (`information-theory/observable-beable-correspondence.md`, `substrate-computation.md`, `q-game-of-life-interpretation.md`, bean `qou-nmqd`). One volume-asymptotics "q→1 't Hooft" limit appears in `docs/audits/2026-07-25-borromean-jones-asymptotics-volume-and-1loop.md:15`. "Ribbon graph" = RT tangles (bean `rttg`). Library: `arxiv-0710.4405v1` ("Large-N_C and QCD asymptotics") and many generic large-N matrix-model papers. No double-line propagator anywhere in the authored corpus. |
| 15 | Drinfeld–Kohno / infinitesimal braid relations | **HELD** (sl₂ and gl_n; the n-strand theorem is partly open) | `folio/.../mass-endomorphism/kz-connection-sl2.{md,lean}` (Arnold relation, flatness ⇔ infinitesimal pure braid relations). `lean/QOU/KZ/GLnResidues.lean` ("gl_n residues … infinitesimal braid relations", 0 sorry, 0 axiom), `GLnKZ.lean`, `KZ4.lean`, `DrinfeldAssociator.lean` (pentagon on residues satisfying the infinitesimal braid relations, 0 sorry), and `KZ/Drinfeld/*` (Casimir, Hexagon, Braiding, HeckeStrands). `docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md` assembles an argument for sl₂ at ℏ ∉ ℚ; it is not refereed, and only its Hecke half is in Lean. Probes: `computations/probes/kz_pullback_monodromy_exact_probe.py`, `computations/kz_real_q0_pure_braid_monodromy_probe.py`, `bridge_b/h2_kz_isospin_blind_probe.py`. Open: `qou-9634` (Lean n-strand DK, `in-progress`) and `qou-zoyv` (D_ℏ ribbon, `in-progress`). Library: **`kohno1987-aif`** is held (sec-003, infinitesimal pure braid relations), so bean `qou-denm` ("Ingest Kohno 1987", `todo`) is **stale**. Also held: `arxiv-q-alg-9707006v1` §3 (the Drinfeld–Kohno theorem), `drinfeld1991-quasitriangular` (ocr), `schechtman-varchenko1991-arrangements`. The gl_n Casimir Ω = Σ T^a⊗T^a is therefore already in the corpus for N = 3 via gl_3. Its link to an f^{abc} vertex is not made anywhere. |
| 16 | Faddeev–Popov ghosts | **not found** in authored corpus; library only | Lean hits (`PhiBSArgumentIdentification`, `EkParitySplit`, `MathlibExt/FaddeevQuantumDilogarithm`) are the Faddeev **quantum dilogarithm**, a homonym. `docs/audits/2026-07-18-bring-s4-elliptic-factor-genus-and-period-block.md:109` mentions an "analytic torsion + Faddeev–Popov" in passing. Bean `qou-t3zb` ("without Faddeev–Popov ghosts") is a target with no file. Library: `arxiv-hep-ph-9306237v1` (FP determinant, ChPT with ρ), `67-6-1860` (ocr), plus BRST in string/TQFT papers. |

## Verdict

- **Already held:** Drinfeld–Kohno / infinitesimal braid relations (#15), for
  sl₂ and for the gl_n residues (so gl₃ is included), sorry-free in
  `QOU/KZ/`. The full n-strand theorem is still open (`qou-9634`).
- **Partially covered:** Casimir structure (#9: C_F and the one-gluon colour
  factor ratio 2 in the SU(N) frame; the C_A/C_F = 9/4 ratio is not in the
  corpus). Colour singlet (#10: singlet selection is held; a colour octet /
  adjoint gluon is not). Flux tube (#12: topology and an obstruction, no
  energy).
- **Closed but mis-scoped by name:** "gluon self-coupling", "three gluon" and
  "four gluon" (#5–#7) are braid-crossing counts and letter candidates, not
  QCD vertices. A topic grep reports them as held. They are not the QCD
  objects.
- **Not found across all six paths in the authored corpus** (folio,
  computations, docs, coordination, beans as artifacts): running α_s(Q²), QCD
  β₀, a derivation of asymptotic freedom, a derivation of antiscreening,
  f^{abc}, a string-tension value, Λ_QCD as a derived object, 't Hooft
  double-line, Faddeev–Popov ghosts. For α_s, Λ_QCD, f^{abc} and asymptotic
  freedom there are **open gap beans** (`qou-5iaz`, `qou-ni4b`, `qou-jsx5`,
  `qou-t3zb`), so they count as known open targets rather than unnoticed
  ones. The library holds the standard physics only as background (ChPT,
  lattice n–p, Seiberg–Witten). No held source states QCD β₀ explicitly.
- **Absence-of-evidence scope.** "Not found" means no match in the regexes
  above, read against hits, on this checkout. It does not mean the subject
  cannot be constructed. The seven `corpus_search` queries had empty
  `emptyRoots`. For "asymptotic freedom" and "string tension" `corpus_search`
  returned no seeds at all, while grep found prose hits, because those phrases
  sit only in block bodies, not in labels or titles.
