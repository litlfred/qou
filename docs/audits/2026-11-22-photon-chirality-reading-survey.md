# Chirality of the off-(0,1) vertex: reading A vs reading B — corpus survey

memory: MEMORY.md (336 lines, 2c6aaeab200) + resolved-topics.md not needed (no row on this topic)
Read-only survey, main, 2026-11-22. Photon used throughout: γ = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹. No computation was run on any other form.

## Verdict

**Open on every path searched. No owner ruling and no Lean theorem decides A vs B.** But the corpus has, in practice, implemented **reading A everywhere it places a vertex off (0,1)**. B-type words (σ_i⁻¹σ_{i+1}, σ_{i+1}σ_i⁻¹) appear only as labelled comparison arms. Two documents attribute the generalisation σ_iσ_{i+1}⁻¹ to the owner ruling. That ruling, verbatim, names only σ₀σ₁⁻¹.

A second bit also matters: under A alone the ⁴He/pn sign still reverses with the bond's **side**, meaning which nucleon it borrows a generator from. A fixes the chirality and does not fix the sign.

## 1. Statements that fix orientation

| what | file:line | quote |
|---|---|---|
| over/under, Lean | `lean/QOU/Knot/BraidClosure.lean:424-430` | `stepOver c (loIdx c.gen) = some c.positive` (σ_i positive ⇒ lower strand over) |
| over/under, prose | `introduction/intro-particles-as-knots.md:21-22` | "Its generator $\sigma_i$ crosses strand $i$ over strand $i+1$" |
| σ_i = L₊ | AGENTS.md §7a | "$\sigma_i$ = positive crossing $L_+$" |
| "u passes over" | `knots-particles-confinement/down-quark.md:8` | "the down quark strand passes under where the up quark passes over" |
| up quark | `knots-particles-confinement/up-quark.md:2` | "an unknot … with **positive crossing orientation** within … $\mathcal{B}_3$" |
| u = K=q vector | `lean/QOU/QuarkState/OverStrandWeight.lean:10-12,124` | "for σ_i (positive) the strand at the lower position i passes OVER"; `over_e1_iff_pure` |
| #8800 §21 (open PR, REST) | `docs/audits/2026-11-21-neutron-heavier-sign.md` §21 | "the Markov weight moves with the letter order … What is still an input: the definition 'u passes over'" |
| Markov at top | `mass-endomorphism/markov-trace-hecke-functional.md:6` | "$\mathrm{tr}_M(x\,\sigma_m) = z\,\mathrm{tr}_M(x)$ for $x \in H_m$" |
| P-invariance | same `.md:81`; `.lean:2229` `towerTr_reflect` | "replacing each $\sigma_a$ with $\sigma_{n-1-a}$. Then $\mathrm{tr}_M(w^{P}) = \mathrm{tr}_M(w)$" (stated for positive words; inverses follow by σ⁻¹ = σ − h) |
| letter order is a choice | `quantum-observable-universes/braiding-induced-ordering.md:3` | "the order on the letters is a choice, so $\prec_c$ is not canonical" |
| P as CPT reading | `…/braiding-induced-ordering-interpretation.md` | "$\sigma_i \mapsto \sigma_{n-i}$ (P, strand reflection)", a remark, not a theorem |
| tower growth | `lifting-and-descent/ordering-jet-compatibility-proof.md:9-10` | "new generators $\omega_i$ are ordered after all level-$n$ generators". These are jet directions, **not** strand generators, so this does not fix A/B. |
| photon pinned | `brings-surface/photon.md:7` | "one positive crossing on the strands $(0,1)$ and one negative crossing on the strands $(1,2)$" |
| β_Bor | `braids-and-knots/borromean-word-minimal.md:1` | "$\beta_{\mathrm{Bor}} = (\sigma_0\sigma_1^{-1})^3$"; 1-indexed twin `fundamental-knots-operator-basis.md:9` $(\sigma_1\sigma_2^{-1})^3$ |
| electron | `docs/coordination/owner-rulings.md:34` | "The electron is σ₀σ₁σ₀ ∈ B₃" (P-fixed: σ₁σ₀σ₁ = σ₀σ₁σ₀) |

## 2. Off-(0,1) vertices in Lean and compute

| site | word | inverts | reading |
|---|---|---|---|
| `lean/QOU/Mass/GammaGammaWordSelection.lean:92` | `vertex i := [⟨i,true⟩,⟨i+1,false⟩]` | larger | **A** |
| `lean/QOU/Molecular/H2BondMirror.lean:95` | `σ i * (σ (i+1))⁻¹` | larger | A |
| `markov-trace-hecke-functional.lean:1168-1185` | ggTail: `shift 1 N * vertexCube`; `ggBondFactor = tr(V³ · N↑¹)` | larger, left entry | A |
| `mass-theory/pieri-photon-shift.md:2` (prop) | "$\varphi_{01}\,\sigma_a\sigma_b^{-1}$ on consecutive generators $a$, $b=a+1$" | larger | A |
| `docs/audits/2026-11-21-magic-shells-gamma-gamma-model.md:19-22` | "the owner-ruled fourth term `σ_iσ_{i+1}⁻¹`", `0 ≤ i ≤ Z−2` | larger | A, **misattributed to the ruling** |
| `docs/audits/2026-11-17-photon-usage-audit.md:44` | "the γγ vertex $\sigma_i\sigma_{i+1}^{-1}$" | larger | A |
| `computations/probes/he4_gg_all_pairs/he4_gg_all_pairs_probe.py:144` | "G^3 = (s_{3j-1} s_{3j}^-1)^3" (production) | larger, left | A |
| `probes/he4_closed_form/hecke_exact.py:84-92` | `V3(k)=[S(k),I(k+1)]*3`; proton(k), neutron(k) | larger | A |
| `probes/gamma_gamma_bond_is_pair_independent_probe.py:112`, `gamma_gamma_h3_psd_selector_probe.py:121`, `gamma_gamma_bond_markov_crosscheck_probe.py:116` | σ_iσ_{i+1}⁻¹ | larger | A |
| `probes/qbeta_gg_lepton_pair/qbeta_gg_lepton_pair_probe.py:35` | `[(i,+1),(i+1,-1)]` | larger | A |
| `qbeta/qbeta_gamma_gamma_submonoid_h4_probe.py:174` | "`vertex i = sigma_i sigma_{i+1}^{-1}`" | larger | A |
| `probes/two_nucleon_bond_response_arity_probe.py:99-104` | V1=σ₂σ₃⁻¹, V3=σ₁σ₂⁻¹ (A); V2=σ₃σ₂⁻¹, V4=σ₂σ₁⁻¹ (B) | both | enumerated; "V1 is the canonical one … Nothing in the arc derives the choice" |
| `probes/n4_weak_vertex_decay_probe.py:90`, `n4_left_doublet_flavour_probe.py:78`, `qbeta_delta_doublet/delta_doublet_candidates_probe.py:145` | `mirror` flag gives σ_a⁻¹σ_b | both | A default, B (ι) as an arm |
| `probes/he4_sign_conventions/he4_sign_conventions_probe.py:38` | "ruled" vs "iota" | both | labelled arms |

No producer was found that uses B as its default. No pair of producers with opposite defaults was found.

## 3. Consequences (A vs B), from the sign table and probes

| observable | dependence | A (production placement) | B / other side | source |
|---|---|---|---|---|
| ⁴He chain | chirality × side | −0.862 keV (unbinds) | ι-left +3.642; ruled-right +16.02 keV | sign-table §2 |
| pn bond (²H) | side within A | V1: −4.469 keV | V3 (A, other side): +56.6 keV | arity probe, `qou-ales` step 11 |
| ³H/³He, Δ_pp | bond writhe/side | open | open | sign-table C5, `qou-fi1p` |
| hydrogen S, capture S | chirality × side | not re-checked | C2: cancels between placements (unmerged Lean) | #8804 §42–46 |
| α_em sectors | ι | open | open | `2026-11-21-alpha-em-which-form-is-canonical.md` §13 |
| n−p (A1–A6) | p/n bit = letter order | n lighter (wrong) under every reading | — | #8800 |
| GMO | flavour order = strand reflection | +0.01854 (Ξ−N units) | −0.01839 | `flavour_order_letter_order_probe.py:124-140` |
| single objects (β_Bor, electron, photon) | none | P-invariant trace | same | `towerTr_reflect`; `H2BondMirror` `mirror_vPow_three_conj` |

Every binding row misses observed values by about three orders of magnitude under either reading (+28.3 MeV for ⁴He). The data cannot decide the question, and per directive they are not a reason.

**Internal-consistency flags.**
1. `ggBondFactor` / `towerTr_ggChain` hard-code A with left entry in the definition. The factorisation proof uses only `towerTr_disjoint`, so it holds for any H₂ bond. The theorem assumes A in its statement but does not need it.
2. A has a structural argument in its favour (my reading, not a theorem). It equals "transport the vertex by the same shift y ↦ y^{↑k} that places nucleons" (`ggTail`, `hecke_exact.proton(k)`). Under B the nucleons would move by shift and the bonds by reflected shift.
3. Two audit docs describe σ_iσ_{i+1}⁻¹ as owner-ruled. The ruling ledger (`owner-rulings.md`, photon row) says only σ₀σ₁⁻¹.

## 4. Rulings / Lean that decide it
None found. Searched `owner-rulings.md` for larger/letter order/reflection/chirality (no hit). Searched Lean for any theorem quantifying over vertex chirality at position i (none; `towerTr_reflect` gives invariance and does not choose).

## Paths run
0. `bun scripts/corpus-search.ts`, `--limit 200`: "strand reflection", "letter order", "braiding-induced ordering" returned 0 seeds (emptyRoots []); "chiral vertex" hit def-photon → prop-pieri-photon-shift; "photon" returned 66 seeds.
1. docs/audits: hits are the sign table, photon-usage audit, magic-shells audit, and neutron-heavier-sign (#8800, via `gh api`).
2. folio/ (excl. `.lake`): the blocks above.
3. computations/: the 15 sites above.
4. docs/coordination/owner-rulings.md: no decision.
5. library/INDEX.md: no hit for amphichiral/strand reflection/chirality. sections/: one unrelated hit. uploads/: 1 file, not checked.
6. beans/defs (mounted): `qou-ales` (in-progress) step 11, "the bond response is ONE-BODY and its SIGN is an underived placement artifact". No bean decides A/B.
