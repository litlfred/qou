# Deuteron knot/link assignment — adjudicated (bean `qou-e5jf`, wall W3 of #5242)

**Date:** 2026-08-21 · **Branch:** `claude/deuteron-knot-adjudication-2026-08-21` ·
**PR:** #5350 · **Bean:** `qou-e5jf` · **Tier:** audit-only, nothing wired.

## 0. BLUF

**The disagreement is a CATEGORY disagreement, and it is worse than the bean
recorded — but it is also almost entirely harmless downstream.**

1. There are **not three assignments to one object.** There are **four
   distinct objects** wearing the name "the deuteron's knot", plus a fifth
   number that is simply a wrong literal. Two of them (`6₂`, Hopf `L2a1`) are
   named side by side *in the same registry record* as different fields.
2. **No assignment is the closure of the deuteron's canonical braid word,
   and none can be.** Measured here: every live construction of the deuteron
   mass word closes to a **3-component link**. `6₂` and the trefoil are
   **knots** (1 component); Hopf is a **2-component** link. Component count is
   fixed by the underlying permutation, so this holds for **every** resolution
   of the averaged crossings and every crossing convention — it is not a
   numerical near-miss, it is an arity mismatch.
3. **The canonical mass word is not a braid word at all.** 5 of its 23 letters
   are averaged crossings `σ − h/2` and `σ − h(½ − δ/4)`, which are genuine
   ℂ-linear combinations in `H₆(q)`, not braid-group elements. The one live
   converter resolves them "to σ (positive) **per F1 convention**" — the
   corpus's own word. So "closure is a computation, not a choice" **fails at
   the deuteron**: the choice is upstream of the computation.
4. **`6₂` is AME-inverted and the corpus already says so, in the production
   source.** `mass_table_ppb.py` L19–22: *"that IS a form of AME-driven fitting
   (we picked the knot whose volume is closest to `B_AME/ρ`)."* Under the
   owner's ruling this is inadmissible as a ground.
5. **Verdict: UNDETERMINED**, and the honest statement is stronger than
   "we cannot choose" — **none of the three candidates is admissible**. Two are
   excluded structurally (arity), one is excluded by provenance (inversion).
6. **Blast radius is small.** The `Vol(6₂)` and `Vol(Hopf)` legs land in
   scripts already labelled hypothesis/exploratory or already reporting honest
   negatives. Under W1 (`deuteron_volume_leg_eq_zero`, sorry-free) the volume
   leg vanishes at the deuteron on any real-shape triangulation, so the
   extended-Bloch consumers are insensitive either way. **Nothing that is
   claimed as a derived result changes.**

---

## 1. Inventory (re-derived from `main` @ `8ba73cc915`, not from the bean)

### A. `σ₁³` → trefoil `T(2,3)`, `Vol = 0` — the **pn channel / per-bond** word

| | |
|---|---|
| **Named** | trefoil `3₁` = `T(2,3)` torus knot, **non-hyperbolic** |
| **Braid word** | `σ₁³` in `B₂` (2 strands, 3 crossings) |
| **Volume as used** | `0` (SnapPy: 2 flat tetrahedra, shapes `{1/2, 2}`, `solution_type = "contains flat tetrahedra"`) |
| **Primary site** | [`computations/deltalambda/deuteron-octahedral-gluing.witness.json`](../../computations/deltalambda/deuteron-octahedral-gluing.witness.json) (SnapPy 3.3.2, 70 dps), producer [`deuteron_octahedral_gluing_probe.py:7`](../../computations/deltalambda/deuteron_octahedral_gluing_probe.py) |
| **What it actually is** | the **pn channel** word, not the atom: *"deuteron pn channel = trefoil σ₁³: s=2, c=3 ⇒ b₁ = 2 (the anchor unit)"* — [`probes/nastokes_transverse_curvature_seifert_probe.py:39`](../../computations/probes/nastokes_transverse_curvature_seifert_probe.py) |
| **Consumers** | `MassTheory/TrefoilColoringBarEven.lean:4`, `MassTheory/PinchedOctahedronDegenerate.lean:17`, `MassTheory/RogersDilogInflection.lean:4`, `MassTheory/TransverseSurfaceCurvature.lean:70`, `MassTheory/GermRootVectorGaugeFixing.lean:34,58,101,290`, `probes/eunit_magnus_order2_probe.py:40,207`, `probes/eunit_g2_derivation_probe.py:48`, `probes/nastokes_germ_root_vector_gauge_probe.py:272,286`, `deltalambda/deuteron_trefoil_qinvariant_closed_form_probe.py`, `deltalambda/coloring_hq0_g2_derivation_probe.py:11` |

**Note.** `σ₁³` is literally a **subword** of the `6₂` word in B (below):
`[1,−2, 1,1,1, −2]` = `σ₁σ₂⁻¹ · σ₁³ · σ₂⁻¹`. The two are not rival answers;
one sits inside the other.

**Note 2 (crossing count).** The pn channel is `3` crossings here but `m_pn = 1`
in [`mass_at_3A_proper.atom_braid_word_3A`](../../computations/mass_at_3A_proper.py#L297).
The corpus carries both a 1-crossing and a 3-crossing pn interface.

### B. `6₂`, `Vol = 4.40083251612304610144…` — the **atom knot** `K(²H)`

| | |
|---|---|
| **Named** | knot `6₂`, hyperbolic |
| **Braid word** | `[1, −2, 1, 1, 1, −2]` = `σ₁σ₂⁻¹σ₁³σ₂⁻¹` on **3 strands** — [`binding-k-solver.witness.json`](../../computations/binding-k-solver.witness.json) `data.registry[0].atom_braid_word` (`n_braid: 3`, `n_0: 6`); repeated at [`probes/he_nu_sdp_psd_count_test.py:63`](../../computations/probes/he_nu_sdp_psd_count_test.py) |
| **Volume as used** | `4.40083251612304610144120386564092803398348541851650` — [`computations/substrate/knot_volumes.py:144`](../../computations/substrate/knot_volumes.py) (`_SNAPPY_HP_50`), docstring L139: *"used as the canonical 2H (deuteron) knot closure"* |
| **Consumers** | [`substrate/binding_manybody_series.py:11`](../../computations/substrate/binding_manybody_series.py) (`B_2 = m_e · Vol(6_2)`), [`binding_ladder_catalog.py:31,92`](../../computations/binding_ladder_catalog.py), [`family_1_kashaev.py:9,79`](../../computations/family_1_kashaev.py), [`mass_table_ppb.py:144`](../../computations/mass_table_ppb.py), [`per_atom_rho_deviation.py:66`](../../computations/per_atom_rho_deviation.py), [`vol_density_deuteron_perknot_probe.py`](../../computations/vol_density_deuteron_perknot_probe.py), [`deuteron_from_scratch_ledger.py:381`](../../computations/deuteron_from_scratch_ledger.py), [`probes/rho_f_vol_binding_dashboard.py:32`](../../computations/probes/rho_f_vol_binding_dashboard.py), [`probes/gap_a4_T2_per_knot_vol_probe.py:72`](../../computations/probes/gap_a4_T2_per_knot_vol_probe.py), [`probes/torsion_nu_sdp_probe.py:197`](../../computations/probes/torsion_nu_sdp_probe.py) |
| **Content layer** | [`kashaev-density-equals-sdp-multiplicity.md:34`](../../content/quantum-observable-universe/mass-theory/kashaev-density-equals-sdp-multiplicity.md) (`²H (D) \| knot 6₂ \| 1 \| 1`); [`conj-canonical-knot-id-sdp.md:4`](../../content/quantum-observable-universe/mass-theory/conj-canonical-knot-id-sdp.md) |

**Verified here (measured, exact).** The registry word does close to `6₂`.
Kauffman-bracket state sum over `TL₃` (exact, sympy, no floats):

```
[1,−2,1,1,1,−2] on 3 strands → 1 component, writhe +2
V(t) = t⁻¹ − 1 + 2t − 2t² + 2t³ − 2t⁴ + t⁵      det = |V(−1)| = 11
```

which is the mirror of the tabulated `V(6₂) = t⁻⁵ − 2t⁻⁴ + 2t⁻³ − 2t⁻² + 2t⁻¹ − 1 + t`,
`det(6₂) = 11`, span 6 = crossing number (alternating). Calibrated in the same
convention against the unknot (det 1), `σ₁³` (det 3), `σ₁²` (Hopf, det 2, 2
components) and `4₁` (det 5). So **B is internally consistent** — the name
matches the word. The question is whether the *word* is the deuteron's.

### C. Hopf link `L2a1`, `Vol = 0` — the **binding link** `K_bind(²H)`

| | |
|---|---|
| **Named** | Hopf link `L2a1`, Seifert-fibred, `Vol = 0` exactly |
| **Braid word** | `σ₃²` in the inter-nucleon generator subset of `H₆` — [`_deprecated/binding_k_enumerator.py:37`](../../computations/_deprecated/binding_k_enumerator.py): *"For ²H, this confirms K = σ₃² (Hopf, length 2) is the unique PSD-feasible inter-nucleon binding of length ≤ L_K_max"* |
| **Volume as used** | `0` |
| **Primary sites** | [`binding_link_volumes.py:8,118`](../../computations/binding_link_volumes.py), [`binding-k-solver.witness.json`](../../computations/binding-k-solver.witness.json) `registry[0].binding_link_name = "L_H (Hopf)"`, [`theta_wn_jetfilt_linkvolume.py:78`](../../computations/theta_wn_jetfilt_linkvolume.py), [`volume-binding-four-point.witness.json`](../../computations/volume-binding-four-point.witness.json), [`deltalambda/vol_t_he3_snappy_probe.py:80`](../../computations/deltalambda/vol_t_he3_snappy_probe.py), [`bk_crossing_coordination.py:86,91`](../../computations/bk_crossing_coordination.py) |
| **Content layer** | [`bk-coordination-multiplicity.md:30`](../../content/quantum-observable-universe/mass-theory/bk-coordination-multiplicity.md): *"The deuteron sits on the Seifert-fibred Hopf link"*; [`linear-chain-bond-count.md:32`](../../content/quantum-observable-universe/mass-theory/linear-chain-bond-count.md) |

**B and C are the same record.** `binding-k-solver.witness.json`'s deuteron
row carries **both**: `"knot_name": "6_2"` *and* `"binding_link_name": "L_H (Hopf)"`.
They are different fields for different objects — the atom's own knot and the
inter-nucleon binding operator. **The registry is not self-contradictory.**
What *is* contradictory is the consumer layer putting them in the same slot
(§2 below).

### D. The canonical **mass word** at `n = 3A = 6` — no determinate closure

| | |
|---|---|
| **Named** | nothing — this is Reading 1, *"the literal mass-braid `H₉` closures"* of [`docs/coordination/2026-08-07-l2-volume-binding-cluster.md:55`](../coordination/2026-08-07-l2-volume-binding-cluster.md) |
| **Word** | [`computations/mass_at_3A_proper.py:257 atom_braid_word_3A(1, 1)`](../../computations/mass_at_3A_proper.py) — **23 letters** `(c, d, gen)` in `H₆(q)` |
| **Volume as used** | Reading 1 reports `0` under all three averaged-crossing conventions |
| **Consumers** | the entire mass/trace chain (`markov_trace_3A`, `chi_lambda_of_word`, `tr_m_atom_zn`) — i.e. *the* canonical object |

Measured letter classification (exact, at `q₀` 50-dps, `h = q − q⁻¹`,
`δ = flavor_split_leading(q)`):

| generator | `σ` | `σ⁻¹ = σ − h` | averaged `σ − h/2` | colour-weighted `σ − h(½ − δ/4)` |
|---|---|---|---|---|
| `σ₀` | 6 | — | 1 | — |
| `σ₁` | — | 3 | 1 | — |
| `σ₂` (pn interface) | — | — | — | 1 |
| `σ₃` | 5 | — | 2 | — |
| `σ₄` | — | 4 | — | — |
| **total** | 11 | 7 | 4 | 1 |

**18 braid letters, 5 non-braid letters.** The averaged crossings are
`(σ + σ⁻¹)/2` up to normalisation — genuine linear combinations, with no
closure.

### E. Numbers that are simply wrong (not knot-identity questions)

| site | value | canonical | note |
|---|---|---|---|
| [`m_tau_knot_prediction.py:91`](../../computations/m_tau_knot_prediction.py) | `"6_2": "4.0597664956578801590"` | `4.40083251612…` | **7.75 % low**; agrees to 8 digits with `2·Vol(4₁) = 4.05976642…`. Bean `qou-r0dn`. |
| [`vol_density_deuteron_perknot_probe.py:39`](../../computations/vol_density_deuteron_perknot_probe.py) | `4.40083298054544839393` | `4.40083251612…` | diverges at the **8th** significant digit. Bean `qou-r0dn`. |
| [`gap_a3_overshoot_robustness_check.py:68`](../../computations/gap_a3_overshoot_robustness_check.py) | `VOL = {"D": 12.776}` | — | a per-atom back-out, **not** a named-knot volume; convention-C, muon-anchored, already labelled as such in the file. Listed so a future grep does not mistake it for a fourth knot assignment. |

---

## 2. Category verdict

**The prior in the task brief is confirmed and then some.**

`σ₁³` **is** recorded as the deuteron word at ~15 sites, its closure **is** the
trefoil `T(2,3)`, it **is** non-hyperbolic with `Vol = 0`, and this **is**
consistent with W1. The `Vol(6₂)` discrepancy **is** a category disagreement:
`6₂` is genuinely hyperbolic (`4.400833`), the trefoil and Hopf are genuinely
not (`0`). So this is **not** three hyperbolic knots differing numerically.

But the sharper statement is about **arity**, and it is convention-free:

> The number of components of a braid closure depends only on the underlying
> permutation. Replacing `σᵢ` by `σᵢ⁻¹` does not change that permutation.
> Therefore **every** resolution of the averaged crossings — and every
> crossing convention — gives the **same component count**.

Measured (exact, `braid_closure_id.py` + `mass_word_closures.py`, scratchpad):

| object | strands | components | det | note |
|---|---|---|---|---|
| `atom_braid_word_3A(1,1)`, all 32 resolutions | 6 | **3** (all 32) | 120 … 784 | **10 distinct Jones polynomials** among 32 resolutions |
| `load_atom_braids()["D"]` as-coded | 6 | **3** | 0 | carries bean `qou-yaqm` sign bug |
| `load_atom_braids()["D"]` sign-corrected | 6 | **3** | 3472 | |
| `6₂` (registry word) | 3 | **1** | 11 | |
| trefoil `σ₁³` | 2 | **1** | 3 | |
| Hopf `σ₁²` | 2 | **2** | 2 | |

So:

- **`6₂` cannot be the closure of the deuteron mass word** (1 vs 3 components).
- **The trefoil cannot be** (1 vs 3).
- **The Hopf link cannot be** (2 vs 3).
- **The mass word has no determinate closure anyway**: 32 resolutions,
  **10 distinct link types**. `hecke_word_to_braid_word`
  ([`atom_braid_words.py:44`](../../computations/atom_braid_words.py)) picks one
  of them by fiat — *"averaged — convert to σ (positive) per F1 convention"* —
  and the colour-weighted pn letter (`|d + h/2| ≈ 7.2e-5 < 0.01`) silently
  falls into the same branch.

**Additional structural mismatch, same tier (measured).** The mass word's
*nucleon* sub-closure has **2** components, while the framework's nucleon is
the Borromean link `𝓑₃ = (σ₁σ₂⁻¹)³` with **3**. So the mass-word frame does not
reproduce the framework's own nucleon as a link either. Recorded as an
observation; it may simply mean the nucleon is not intended to be read as a
closure.

### Where the real live contradiction is

Not in the registry — in the **consumer layer**, where the atom knot's volume
and the binding link's volume occupy the same slot:

| script | slot | deuteron value |
|---|---|---|
| [`substrate/binding_manybody_series.py:11`](../../computations/substrate/binding_manybody_series.py) | `B_2` = per-bond binding | `m_e · Vol(6_2)` = **4.400833** |
| [`theta_wn_jetfilt_linkvolume.py:78`](../../computations/theta_wn_jetfilt_linkvolume.py) | "whole-atom hyperbolic link volume" | **0.0** (Hopf) |
| [`binding_ladder_catalog.py:92`](../../computations/binding_ladder_catalog.py) | `B(D)` | `1·m_e·Vol(6_2)` = **4.400833** |
| [`binding_link_volumes.py:118`](../../computations/binding_link_volumes.py) | `Vol(K_bind)` | **0** (Hopf) |

Two scripts fill "the deuteron's volume" with `4.400833`; two fill it with `0`.
The content layer carries both too — `kashaev-density-equals-sdp-multiplicity.md:34`
says `6₂`, `bk-coordination-multiplicity.md:30` says Hopf.

---

## 3. Adjudication

**I cannot adjudicate in favour of any of the three, and this is not a tie —
each is excluded on its own grounds.**

Walking the task brief's grounds in decreasing strength:

### Ground 1 — derivation from the braid word actually used by the mass chain

**Fails, and rules out all three.** The word is `atom_braid_word_3A(1,1)`; it is
not a braid word (5 non-braid letters); every resolution closes to a
3-component link; and the 32 resolutions give 10 distinct link types. Closure is
a computation *only after* a choice that is currently made by an undocumented
convention. **Scope-(b) structural exclusion**, on the proved invariant that
component count is a permutation invariant: `6₂` (1 comp), `3₁` (1 comp) and
Hopf (2 comp) are **excluded** as the closure of the canonical deuteron mass
word, under any crossing convention and any resolution. That invariant is
elementary and convention-free; it does not depend on my bracket normalisation.

### Ground 2 — consistency with the proved two-row / `TL₂` structure

**Does not discriminate.** `conventionD_weight_eq_zero_iff`
([`QOU/QBeta/WenzlWeightVanishing.lean:241`](../../content/quantum-observable-universe/lean/QOU/QBeta/WenzlWeightVanishing.lean))
kills every partition with `> 2` rows, so the deuteron's Hecke content at
`n = 3A = 6` is `{(6), (5,1), (4,2), (3,3)}`. Two-row content is exactly the
Temperley–Lieb / Jones level, which any of these closures possesses. It
constrains the *representation content*, not the *link type*. It does note
that the deuteron's canonical home is `H₆`, which is one more strike against
the `6₂` word (a 3-braid embedded in `H₆` — the registry's own
`constituent_product_word` is a 6-braid, so the factorisation compares objects
at two different strand counts).

### Ground 3 — consistency with what the binding formula's other factors assume

**Discriminates against `6₂`, but only by exposing the inversion.** The `6₂`
assignment's provenance is a census search that minimises
`|B_AME − ρ_F · m_e · Vol(K)|`, with `ρ_F ∈ {m_e, 2m_e}` a free binary also
picked to match. The corpus states this itself, twice:

- [`computations/mass_table_ppb.py:19-22`](../../computations/mass_table_ppb.py):
  *"The atom→knot assignments for D, T, ³He were obtained by census search in
  `jsj_verification.py` — that IS a form of AME-driven fitting (we picked the
  knot whose volume is closest to `B_AME/ρ`). Flagged here as 'hyp: by-census'."*
- [`docs/audits/2026-05-24-rule14-atom-knot-census.md:24`](2026-05-24-rule14-atom-knot-census.md):
  *"**This is empirical fitting** … a coefficient selected by minimising a
  CODATA residual, with no substrate-derived rule producing the same answer"*,
  and L61: *"the framework has … **no canonical `(Z, N) ↦ K_census` functor** …
  the census assignments are scaffolding."*

The 2026-06-12 adjudication ([`2026-06-12-knot-id-volume-match-adjudication.md`](2026-06-12-knot-id-volume-match-adjudication.md))
ranked `6₂` (+1.09 %) over `6₁` (−27.3 %) — again **by agreement with AME**. It
settles that the *printed digits* were stale and that the named set beats the
orphan set; it does **not** supply a derivation, and it does not claim to
(§Verdict: *"the SDP-uniqueness claim of `conj:canonical-knot-id-sdp` itself
remains open"*). The producer `jsj_verification.py` now lives in
`computations/_deprecated/`.

Under the owner's ruling — *"Δ_λ from inverted CODATA = NOT ALLOWED"* — an
assignment selected by which volume reproduces `B_AME` is **inadmissible as a
ground**, whatever its numerical merit.

### What survives

**Hopf `L2a1` is the one candidate with a non-inverted derivation** —
`binding_k_enumerator.py` obtains `K = σ₃²` as the unique PSD-feasible
inter-nucleon binding of length ≤ `L_K_max`, a structural criterion with no AME
input. But (i) that producer is **deprecated**, (ii) it is a claim about the
**binding operator**, not the atom knot, and (iii) it does not license writing
`Vol(Hopf) = 0` into a slot that `6₂`'s consumers fill with `4.400833` — those
are different objects.

**Conclusion: UNDETERMINED.** Precisely:

> The corpus contains no derivation of a deuteron knot type. `6₂` is
> AME-inverted (self-declared). The trefoil is a per-bond channel word, not the
> atom. Hopf is the binding operator, not the atom. And the atom's own
> canonical word admits no determinate closure — it is not a braid.

---

## 4. Blast radius

**(b) — unaffected.** The largest class, and the relief worth stating.

- **Every extended-Bloch / flattening consumer.**
  `QOU.MassTheory.BlochVolumeLegFlatVanishing` (sorry-free, `#print axioms`
  clean) proves `∑ D(zᵢ) = 0` over real shapes **for every tetrahedron count**,
  so the volume leg is `0` at the deuteron on any real-shape triangulation.
  Under the trefoil and Hopf frames alike the leg is zero, so W1's conclusion
  is insensitive to the trefoil-vs-Hopf question. It is *not* insensitive to
  the `6₂` frame — but `6₂` is inadmissible, so nothing is lost.
- **The `σ₁³` Lean cone** — `TrefoilColoringBarEven`, `PinchedOctahedronDegenerate`,
  `RogersDilogInflection`, `TransverseSurfaceCurvature`, `GermRootVectorGaugeFixing`.
  These state facts **about the trefoil / about the single-generator word
  `σ₁³`** (e.g. `Ω_k = 0` for `k ≥ 2` because all letters commute). They are true
  of `σ₁³` regardless of whether `σ₁³` is the deuteron. What becomes uncertain
  is only their *physical interpretation*, which is class (c).
- **The Markov-trace mass chain.** `markov_trace_3A` / `chi_lambda_of_word`
  consume the **Hecke word**, never a closure. The Markov trace of a Hecke
  element is well defined whether or not the element is a braid. `tr_M`, `χ_λ`,
  `y_λ`, `Δ_λ` values, `conventionD_weight_eq_zero_iff`, the two-row cap — all
  untouched.
- **`volume-binding-four-point.witness.json`.** Already excludes the deuteron as
  a data point and says why; its verdict (*"the four-point falsification cannot
  be run"*) stands unchanged and is if anything strengthened.
- **`binding_link_volumes.py`.** Its own witness records
  `deuteron_endomorphism_holds: passed = false`, `err_pct = −6.31 %`. Already an
  honest negative; unchanged.

**(a) — wrong.**

- **`Vol(6₂)` as a deuteron binding term.** `substrate/binding_manybody_series.py`
  `B_2 = m_e · Vol(6_2) = 2.2489 MeV` (+1.09 % vs AME 2.224566). The `+1.09 %`
  is not a prediction — it is the residual of the fit that *chose* `6₂`. Same for
  `binding_ladder_catalog.py:92` and `family_1_kashaev.py:9`. These should carry
  the `hyp: census-assigned / AME-inverted` label that `mass_table_ppb.py`
  already carries.
- **`m_tau_knot_prediction.py:91`** — `Vol(6₂) = 4.0598` is wrong by 7.75 %
  independent of everything above. Bean `qou-r0dn`.
- **`delta_lambda_jsj_phase3.load_atom_braids()`** — the sign-dropping offset
  bug (bean `qou-yaqm`) corrupts every closure this producer hands to SnapPy.
  Component count is unaffected (3 either way), so **the verdict above does not
  depend on the fix**.

**(c) — status becomes *unknown*.**

- **The physical reading of the `σ₁³` results.** "The deuteron's NA-Stokes
  surface-curvature term vanishes" is now "the *pn channel word* `σ₁³`'s term
  vanishes, and whether that word is the deuteron's is undetermined." The
  mathematics stands; the identification does not.
- **`conj:canonical-knot-id-sdp`** — already a `conjecture`, already stating the
  SDP-uniqueness claim as an open verification requirement. Its status is
  unchanged; what this audit adds is that its `²H` row is **also** arity-blocked
  from being the mass word's closure, not merely unverified.
- **`kashaev-density-equals-sdp-multiplicity.md:34`** (`²H → 6₂`) and
  **`bk-coordination-multiplicity.md:30`** (`²H → Hopf`) — the content layer
  asserts both. At most one can be "the deuteron's knot"; on this analysis
  neither is.
- **The 1-vs-3 crossing pn interface** (`m_pn = 1` in `atom_braid_word_3A`
  vs `c = 3` in the `σ₁³` channel probes) — a separate undetermined convention.

---

## 5. What would determine it — cheapest first

1. **Decide what "the deuteron's knot" is supposed to *be*, and say so once.**
   Zero compute. The registry already distinguishes `knot_name` from
   `binding_link_name`; the consumers do not. Three named slots — atom knot,
   binding link, per-bond channel word — with one owner each would dissolve the
   consumer-layer contradiction (§2) *without settling the mathematics*. This is
   the cheapest real gain and it is a documentation act.

2. **Derive the resolution of the averaged crossings — or prove none exists.**
   ~1 day. This is the actual blocker and it is upstream of every knot
   candidate. `σ − h/2 = (σ + σ⁻¹)/2` is not a braid; the F1 "treat as positive"
   convention is a choice made in a 4-line converter. Two honest outcomes:
   - a substrate-level rule fixing each averaged letter (then the closure *is* a
     computation, and one runs it — the answer will be a 3-component link, so
     the census must be searched over **3-component links**, not knots); or
   - a proof that the Hecke element's invariants (Markov trace, `HOMFLY` via the
     Ocneanu trace) are **all** the deuteron has, and that no single link type is
     assigned — which is a perfectly good structural answer and would close
     `qou-e5jf` as "the question was malformed".

   **Formalize-first note:** step 2 is exactly the AGENTS.md §formalize-first
   pattern. The invariant *"component count is a permutation invariant, hence
   resolution-independent"* is one Lean lemma and it already prunes the entire
   knot-valued candidate class. Prove it before searching any census.

3. **Search the 3-component census.** ~hours *given* step 2. If the deuteron's
   closure is a 3-component link, then `6₂`, `3₁` and `L2a1` were never
   candidates and the right census slice is `L6*`, `L7*`, … 3-component links —
   which is where `L6a4 = 𝓑₃` already lives. Note the suggestive coincidence:
   the framework's nucleon `𝓑₃` is itself 3-component. **Do not rank candidates
   by `|B_AME − ρ·m_e·Vol|`** — that is the move that produced `6₂`.

4. **Only if 2 and 3 both fail:** the R5-full SDP solver, which
   `2026-05-24-rule14-atom-knot-census.md:61` names as the thing that would make
   the assignment derived (*"the resulting knot is then derived (Markov closure
   of the SDP solution), not census-fitted"*). Expensive, long-deferred, and the
   `A = 4` Hoefsmit/Clarabel gap (`conj #604` / GAP-A-1) is upstream of it.

**Explicitly NOT a determining experiment:** any procedure that scores
candidates by agreement with `B_AME`. That is the forbidden inversion, it is how
`6₂` got here, and re-running it at higher precision would only produce a
better-fitting wrong answer.

---

## 6. Reproduction

Exact/symbolic throughout (sympy `TL_n` state sum, mpmath at 60 dps for the
letter classification). No floats entered any conclusion; no witness was
written or regenerated. Scripts:
`braid_closure_id.py` (Kauffman bracket → Jones → determinant, calibrated
against unknot/`3₁`/Hopf/`4₁`) and `mass_word_closures.py` (32-resolution
enumeration), scratchpad-local — not committed, since this audit records the
results and nothing downstream consumes them.

## 7. Beans

- `qou-e5jf` — **adjudicated here**: undetermined, with all three candidates
  excluded on independent grounds. Ready for owner ruling on §5 item 1.
- `qou-yaqm` — **new**: sign-dropping generator offset in
  `delta_lambda_jsj_phase3.load_atom_braids()`.
- `qou-r0dn` — **new**: `Vol(6₂)` literal wrong by 7.75 % in
  `m_tau_knot_prediction.py`; 8th-digit divergence in
  `vol_density_deuteron_perknot_probe.py`.

---

## 8. Amendments after independent re-verification (2026-08-21, second agent)

This section was added on `claude/deuteron-knot-adjudication-redo-2026-08-21`
after the commit above was rescued by cherry-pick. The rescue was needed
because the commit had landed on an unrelated sibling branch
(`claude/tl-arc-lean-infra-2026-08-21`) — two agents were sharing one
checkout, so `HEAD` was the sibling's when this doc was committed. It existed
in exactly one place until the cherry-pick.

Everything above is **unchanged**. A second agent re-derived the findings from
the tree rather than inheriting them; the results below either **confirm**,
**sharpen**, or **add to** §§1–7. **The `UNDETERMINED` verdict of §3 is
unchanged, and is now supported by a second, independent computation.**

### 8.1 Independent confirmation of the `6₂` identification (§1B)

§1B identified the registry word `[1, −2, 1, 1, 1, −2]` as `6₂` using a
Kauffman-bracket state sum over `TL₃`. That was re-done by a **different**
route — the reduced Burau representation over `ℤ[t, t⁻¹]`, giving the
Alexander polynomial rather than the Jones polynomial:

```
[1,−2,1,1,1,−2] on 3 strands → 1 component, writhe +2
Δ(t) = −t² + 3t − 3 + 3t⁻¹ − t⁻²        det = |Δ(−1)| = 11
```

`Δ` is the tabulated Alexander polynomial of `6₂` and `det = 11` agrees with
§1B's bracket computation. **Two independent invariants, computed by two
independent methods, give the same identification.** §1B stands.

The script is committed as
[`computations/probes/deuteron_braid_closure_identification.py`](../../computations/probes/deuteron_braid_closure_identification.py)
— §6 recorded its scratchpad scripts as uncommitted, so this supplies a
reproducible artifact for the arity argument that §3 Ground 1 rests on. It
emits no witness. Its five textbook reference rows (unknot 1, Hopf 2, trefoil
3, figure-eight 5, `6₂` 11) are load-bearing: the first version mapped
`σᵢ⁻¹` by substituting `t → 1/t`, which coincides with the matrix inverse only
in `B₂`, and it silently returned `3` for the figure-eight and `5` for `6₂`.
Anyone re-deriving this should calibrate before trusting a corpus row.

### 8.2 New — a **fourth** name/word mismatch, in `gb-filtration-jet-order-reader`

Not in the §1 inventory, and a different defect class from §1E (which is
wrong *numbers* under right names): here the **word does not close to the
knot it is named for**.

[`computations/gb-filtration-jet-order-reader.witness.json:41`](../../computations/gb-filtration-jet-order-reader.witness.json)
names a row `"deuteron 6_2 σ_1^{-1} σ_2 σ_1^{-1} σ_2^2 in H_3"`. Measured:

| row as written | components | det | the named knot |
|---|---|---|---|
| `4_1`: `(σ₁σ₂⁻¹)²` | 1 | 5 | `4₁`: knot, det 5 — **correct** |
| `6_2`: `σ₁⁻¹σ₂σ₁⁻¹σ₂²` | **2** | **8** | `6₂`: **knot**, det **11** — **mismatch** |
| `8_11`: `σ₁⁻¹σ₂σ₁⁻²σ₂³` | **2** | 18 | `8₁₁`: **knot** — **mismatch** |

The figure-eight row is correct, so the file's notation convention is the
standard one and these two rows are genuinely wrong rather than
differently-conventioned.

For the deuteron row the repair looks like a single exponent:
`σ₁⁻¹σ₂σ₁⁻¹σ₂³` (one more `σ₂`) gives **1 component, det 11** — exactly `6₂`.
**No repair is proposed for the tritium row**: two nearest-neighbour
candidates (`σ₂⁴`, `σ₁⁻³`) do restore a knot (det 23, det 25) but neither is
identifiable as `8₁₁` from what was computed here, so only the arity mismatch
is claimed.

**Scope-(b) structural exclusion**, on the *same* proved invariant §2 already
uses — the number of components of a braid closure is a permutation
invariant, so it is independent of every crossing sign and every convention.
A 2-component closure cannot be a knot. This needs no determinant table.

**Blast radius: (c), status unknown, small.** The row's `max_grade` and
`filtered_basis_size` are computed *from the word*, so they are correct facts
about the word; what is wrong is the **name**. The risk is a reader taking
"`max_grade = 3`" as a jet-order fact about `6₂`. Bean `qou-w8kb`.

### 8.3 Correction to bean `qou-yaqm` — the doc is right, the bean over-generalises

§4(a) states the sign-drop's component count is "3 either way" and scopes that
to the deuteron. **That is correct** — re-measured by exact cycle count of the
induced permutation, the deuteron goes 3 → 3. The verdict's independence from
the fix holds.

Bean `qou-yaqm` states it **unscoped** ("Component count is unchanged (3)")
while also naming the T / ³He / ⁴He rows. Off the deuteron row that is
**false**:

| row | as-coded | sign-corrected |
|---|---|---|
| `D` | 3 | 3 |
| `T` | 4 | 4 |
| **`³He`** | **2** | **4** |

So the bug *does* change the topology of the ³He closure. The bean has been
corrected; §4(a) needs no change.

Two further sharpenings of the bean, both measured:

- **Line numbers are 73 / 75 / 77**, not 69–76.
- **The as-coded deuteron closure is split.** The as-coded word reaches only
  `max|gen| = 4` on 6 strands, so **strand 6 is never touched** and the
  closure is (something on 5 strands) ⊔ unknot. This *explains* the `det = 0`
  §2 records — a split link has vanishing Alexander polynomial. The
  sign-corrected word reaches `σ₅`. Determinant 0 is therefore not an
  incidental number but the signature of the defect.
- **The same `[g + k for g in …]` pattern appears 8 more times** in
  [`computations/atom_braid_words.py`](../../computations/atom_braid_words.py)
  (lines 101, 103, 105, 110, 111, 114, 115, 157), and the **proton** word
  `p = [1, −2, 1, −2, 1, −2, 1, 1, 2, 1, 1]` carries negative letters too — so
  `[g + 3 for g in p]` is affected as well. The defect is not confined to one
  producer.

### 8.4 Sharpening of §1E — the `2·Vol(4₁)` reading is a hypothesis, not an identity

§1E says the `m_tau_knot_prediction.py:91` literal "agrees to 8 digits with
`2·Vol(4₁)`". That wording is exact and is **not** being corrected. Adding the
measurement, so a later reader does not upgrade it to an identity:

```
literal                4.059766495657880159
2·Vol(4₁)              4.0597664256386145
difference             7.00193e-8            relative 1.72471e-8
literal vs census      −7.75003 %
probe literal vs census  4.64422e-7           relative 1.05531e-7
```

The literal is **not** `2·Vol(4₁)`; it differs in the 9th significant figure.
"Doubled figure-eight" remains a **hypothesis** about how the wrong number got
there, tiered as such — the provenance is undetermined. What is **measured**
is only the −7.75 % disagreement with the census value, and that alone is
what bean `qou-r0dn` needs to be actionable.

### 8.5 Prior art check on §3 Ground 3

Independently corpus-grepped and found the same thing §3 cites, plus one item
worth naming explicitly:
[`computations/probes/knot_id_volume_match_adjudication.py`](../../computations/probes/knot_id_volume_match_adjudication.py)
is a **live, non-deprecated** probe whose stated purpose is to adjudicate this
exact fork, and whose method is scoring `ρ · m_e · Vol(K)` against `B_AME`
(docstring: *"named set {6_2, 8_11, L6a4}: errors ≈ +1.1 %, −0.16 %, −3.0 %"*).
Its verdict — *"the names are right"* — rests entirely on AME agreement.

Under the owner's ruling that is the forbidden inversion, so **the corpus's
existing adjudication of `6₂` is not admissible as a ground**, exactly as §3
concludes. Its docstring's *"no fit: the law has zero free parameters"* is
true of the **law** and not of the **selection**: the knot name is itself a
discrete parameter chosen from a census by AME agreement. Recording this so a
later agent who finds that probe does not read it as settling the question.

### 8.6 Environment note

SnapPy is **not installed** in this container (`ModuleNotFoundError: No module
named 'snappy'`), so nothing here was re-checked against the census
programmatically. Every claim in §8 is exact integer or symbolic arithmetic
(`sympy`) over the braid words themselves, or a permutation cycle count — no
float64 entered any conclusion, and no witness was written or regenerated.
