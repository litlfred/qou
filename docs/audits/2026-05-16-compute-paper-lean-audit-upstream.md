# Compute / Paper / Lean Coverage Audit

**Date:** 2026-05-16
**Scope:** Three compute scripts in `computations/`.
**Method:** Read each script in full, enumerate math claims, search
`content/quantum-observable-universe/` for backing content blocks,
inspect sibling `.lean` files for proof status.

Files audited (all paths absolute):

- `/home/user/qou/computations/bw_chirality_isotopes.py` (305 lines)
- `/home/user/qou/computations/gb_filtration_jet_tracker.py` (545 lines)
- `/home/user/qou/computations/term5_v2_chirality.py` (153 lines)

---

## 1. `bw_chirality_isotopes.py`

### (A) Math claims inventory

1. **BW volume coefficient** `λ_V = 2·[2]_q·[7]_q · m_e`
   (line 72, `module-level constants`).
2. **BW surface coefficient** `λ_S = 2·[4]_q² · m_e` (line 73).
3. **BW Coulomb coefficient** `λ_C = (q − q⁻¹)·[6]_q · m_e` (line 74).
4. **BW asymmetry coefficient** `a_asym = 3·[2]_q·[7]_q · m_e`
   (line 75); equivalently `a_asym = (3/2)·λ_V`.
5. **BW pairing coefficient** `δ_P = [3]_q·[7]_q · m_e` (line 76).
6. **BW exchange-Coulomb coefficient** `λ_ex = [3]_q/[2]_q · m_e`
   (line 77).
7. **BW shell coefficient** `δ_S = [2]_q²·[3]_q · m_e` (line 78).
8. **Magic-proximity function** `f(x) = Σ_m exp(−(x−m)²/(2·[2]_q²))`
   over magic numbers `{2,8,20,28,50,82,126}` with width `σ = [2]_q`
   (function `magic_proximity`, lines 88–95).
9. **Seven-term BW formula** for the binding `B_bulk + B_Z + B_shell`
   (functions `B_bulk`, `B_Zdep`, `B_shell`, `predict_binding_vanilla`,
   lines 98–181). Sign convention for pairing follows §128–131.
10. **Chirality factor classification** for the bulk:
    - `D` (A=2, satellite, chiral+): `1 + h`
    - `T`, `³He` (A=3, figure-8, amphi): `1 − h²`
    - `⁴He` (A=4, Borromean, 2 amphi): `(1 − h²)²`
    - A ≥ 5: limit factor → `1`
    (lines 81–84, used in `chirality_map` lines 222–233).
11. **Z-dependent chirality factor** `f_Zdep_scale = h·[2]_q = q² − q⁻²`
    (line 85), used in `predict_binding`.
12. **Chirality-modified binding formula**
    `B_K = (chirality_factor)·B_bulk + (h·[2]_q)·B_Z + B_shell`
    (function `predict_binding`, lines 134–167).

### (B) Paper content-block backing

| # | Claim | Backing |
|---|-------|---------|
| 1 | `λ_V = 2[2]_q[7]_q · m_e` | **BACKED:** `conj:q-integer-mass-formula` at `/home/user/qou/content/quantum-observable-universe/particle-interactions/q-integer-mass-formula.md` (line 11 of table). |
| 2 | `λ_S = 2[4]_q² · m_e` | **BACKED:** same conjecture, row 2. |
| 3 | `λ_C = (q−q⁻¹)[6]_q · m_e` | **BACKED:** same conjecture, row 3. |
| 4 | `a_asym = 3[2]_q[7]_q · m_e` | **BACKED:** same conjecture, row 4; relation `a_asym = (3/2)λ_V` stated lines 63–67. |
| 5 | `δ_P = [3]_q[7]_q · m_e` | **BACKED:** same conjecture, row 5. |
| 6 | `λ_ex = [3]_q/[2]_q · m_e` | **BACKED:** same conjecture, row 6 (Hecke-extra terms). |
| 7 | `δ_S = [2]_q²[3]_q · m_e` | **BACKED:** same conjecture, row 7. |
| 8 | Magic-proximity Gaussian `f(x)`, width `σ = [2]_q` | **BACKED:** same conjecture, lines 37–40. Formula spelled out identically. |
| 9 | Seven-term BW formula | **BACKED:** same conjecture, displayed formula lines 26–35. |
| 10 | Chirality factors `{1+h, 1−h², (1−h²)²}` per A∈{2,3,4} | **BACKED:** `prop:figure-eight-bw-coefficients` at `/home/user/qou/content/quantum-observable-universe/braids-and-knots/figure-eight-bw-coefficients.md`. The classification table at lines 114–119 lists exactly the three values used here. Also interpretively covered by `prop:chirality-from-frobenius-self-pairing` (`chirality-from-frobenius-self-pairing.md`). |
| 11 | `f_Zdep = h·[2]_q = q² − q⁻²` | **BACKED:** `prop:figure-eight-bw-coefficients`, line 38 of the `.md` (factor `h[2]_q = q²−q⁻²`). |
| 12 | Chirality-modified composite formula `B_K = (·)B_bulk + (h[2]_q)B_Z` | **BACKED:** `prop:figure-eight-bw-coefficients`, displayed formula lines 6–10 (matches exactly with `B_bulk + B_Z` decomposition). The "A≥5 → factor → 1" limiting behaviour is documented in the .md table (line 119) but is not derived; it is asserted as the limit. |

### (C) Lean proof coverage

Lean siblings: `q-integer-mass-formula.lean`, `figure-eight-bw-coefficients.lean`.

| # | Claim | Lean status |
|---|-------|------|
| 1 | `λ_V` | **LEAN_PROVED:** `QOU.Interactions.lambda_V` (def, q-integer-mass-formula.lean L33). |
| 2 | `λ_S` | **LEAN_PROVED:** `lambda_S` (L37). |
| 3 | `λ_C` | **LEAN_PROVED:** `lambda_C` (L41). |
| 4 | `a_asym` and the relation `a_asym = (3/2)λ_V` | **LEAN_PROVED:** `a_asym` def (L45); `asym_volume_relation` theorem (L75, ring-proved, sorry-free). |
| 5 | `δ_P` | **LEAN_PROVED:** `delta_P` (L49). |
| 6 | `λ_ex` and exchange–Coulomb relation | **LEAN_PROVED:** `lambda_ex` (L57); `exchange_coulomb_relation` theorem (L84, field_simp/ring, sorry-free). |
| 7 | `δ_S` | **LEAN_PROVED:** `delta_S` (L63). |
| 8 | Magic-proximity Gaussian | **LEAN_MISSING:** abstracted as parameters `f_Z f_N : ℝ` in `binding_energy_bw` (L94) and as a class field `f_magic : ℕ → ℝ` (L121). No constructive Lean definition. |
| 9 | Seven-term BW formula | **LEAN_PROVED (as a def, not a theorem):** `binding_energy_bw` (L94) packages the algebraic formula. The accuracy claim (this formula matches AME to within tolerance) is **LEAN_HAS_SORRY** as the conjecture class field `QIntegerMassFormula.fits_AME` (L149); marked conjectural per CLAUDE.md §3b-cond. The `-- Ref:` lines (L43, L73 etc.) cite `[manuscript] Ch 11 §8`. |
| 10 | Chirality factors per A class | **LEAN_PROVED (partial):** `fig8BulkFactor` (L24) and `fig8ZdepFactor` (L29) defined; `figure_eight_bw_coefficients` theorem exists (L84) but states existence only for `A = 3` (the figure-eight case). The satellite (`1+h`) and Borromean (`(1−h²)²`) factors are NOT formalised. |
| 11 | `f_Zdep = h·[2]_q = q²−q⁻²` | **LEAN_PROVED:** `fig8ZdepFactor` def (L29); `fig8ZdepFactor_pos` (L64) proves positivity of this factor when `q > 1`. The algebraic identity `h·[2]_q = q²−q⁻²` is implicit in the def. The `figure_eight_std_character` theorem (L38) proves the character identity `2 − [3]_q = −1 − h²` that yields the factor. |
| 12 | Composite formula `B_K = (·)B_bulk + (h[2]_q)B_Z` | **LEAN_MISSING:** Lean has only the existential statement that `a, f` exist with the right values for A=3 (`figure_eight_bw_coefficients` L84); the full composite binding formula is not assembled at theorem level. |

---

## 2. `gb_filtration_jet_tracker.py`

### (A) Math claims inventory

1. **Iwahori-Hecke algebra presentation**: `T_i^2 = (q − q⁻¹)T_i + 1`,
   braid relations `T_i T_{i+1} T_i = T_{i+1} T_i T_{i+1}`,
   far commutativity `T_i T_j = T_j T_i` for `|i−j|≥2`
   (docstring lines 22–26; encoded in `right_mul_T`, lines 182–218).
2. **σ-inverse identity**: `T_i⁻¹ = T_i − (q − q⁻¹)`
   (docstring L27; method `right_mul_T_inv` lines 220–225).
3. **GS-NF right-action rule**: `T_w · T_i = T_{ws_i}` if `ℓ(ws_i) > ℓ(w)`;
   `T_w · T_i = (q − q⁻¹)T_w + T_{ws_i}` if `ℓ(ws_i) < ℓ(w)`
   (docstring lines 28–30; method `right_mul_T` cases at L191 and L201).
   This is the core math claim of the script.
4. **Coxeter length = inversion count** for symmetric group elements
   (function `coxeter_length`, lines 91–94).
5. **GS-filtration certificate**: grading of an element `E ∈ H_n(q)`
   by Coxeter length of its support `T_w` terms
   (function `filtration_certificate`, lines 227–233).
6. **Jet-order data model**: ordered sequence of reduction events
   `(step, T_i, w_before, w_after, ℓ_before, ℓ_after, relation_fired)`
   (class `JetEvent` lines 131–141; emission in `right_mul_T`).
7. **Closed-form reduction of σ_1³ in H_2**:
   `σ_1³ = ((q−q⁻¹)² + 1) T_{s_1} + (q − q⁻¹) T_e`,
   filtration shape `{0:1, 1:1}` (asserted as test case at L324–330).
8. **Verification of expected filtration shapes** for ascending words:
   `σ_1 σ_2 σ_3 σ_4` in H_5 has shape `{4: 1}`;
   `σ_1 σ_2 σ_1` in H_3 has shape `{3: 1}` (lines 401–424).

### (B) Paper content-block backing

| # | Claim | Backing |
|---|-------|---------|
| 1 | Hecke relations (T_i² + braid + far commut.) | **BACKED:** CLAUDE.md §7a "Hecke-Skein convention" gives the relation `(σ_i − q)(σ_i + q⁻¹) = 0` equivalent to `T_i² = (q−q⁻¹)T_i + 1`. Multiple paper blocks reference `H_n(q)` (e.g., `figure-eight-bw-coefficients.md` L48–51 cites the Wedderburn decomposition of `H_3(q)`). No single dedicated paper block defines the Hecke relations themselves — the script's docstring relations are the canonical Iwahori-Hecke presentation, treated as standard background. **Marginally BACKED via convention** but no `def:hecke-algebra` or `prop:hecke-relations` block exists. |
| 2 | `T_i⁻¹ = T_i − (q − q⁻¹)` | **BACKED:** CLAUDE.md §7a explicitly derives this from the Hecke quadratic relation. Not formalised as a paper proposition. |
| 3 | GS-NF right-action rule | **UNBACKED as a stand-alone proposition.** The rule is a direct consequence of (1) and is standard knot-theory folklore (Geck–Pfeiffer, Mathas). Papers reference *that* the GS normal form exists (e.g., `prop:atomic-mass-gb-nf` cites `unital-groebner-bases:cor:pbw`; `gs-graded-markov-trace-existence.md`, `graded-markov-trace-from-gs-filtration.md` reference the GS filtration), but the **explicit Hecke right-multiplication rule** the script implements is not the content of any QOU paper block. It is encoded only in the script's docstring. |
| 4 | Coxeter length = inversion count | **UNBACKED:** standard combinatorics; the script implements it as helper code. No paper block. |
| 5 | GS-filtration certificate | **BACKED (indirectly):** `prop:graded-markov-trace-from-gs-filtration` at `/home/user/qou/content/quantum-observable-universe/braids-and-knots/graded-markov-trace-from-gs-filtration.md` defines the GS filtration `J^•(q)`, the associated-graded algebra, and the descent of the Markov trace. The script's `filtration_certificate` is a concrete data structure realising the abstract `J^ℓ / J^{ℓ+1}` strata. Companion `conj:gs-graded-markov-trace-existence` at `gs-graded-markov-trace-existence.md` axiomatises the existence. |
| 6 | Jet-order data model | **UNBACKED:** the script's JetEvent log is infrastructure for the future joint-tower SDP confinement solver. The closest paper block, `prop:jet-prefix-gb-filtration` at `jet-prefix-gb-filtration.md`, introduces the *concept* of GS-filtration-indexed prefixes (β_k^GS = projection onto J^{k-3}/J^{k-2}) but does NOT define the ordered-reduction-event format. The jet-order data shape is purely a script-side convention. |
| 7 | σ_1³ = ((q−q⁻¹)² + 1) T_{s_1} + (q − q⁻¹) T_e | **UNBACKED:** specific Hecke computation, used as ground-truth test in the script. Not a paper-stated identity. |
| 8 | Expected filtration shapes for ascending words | **UNBACKED:** test-case assertions, not paper-stated. |

### (C) Lean proof coverage

| # | Claim | Lean status |
|---|-------|------|
| 1 | Hecke relations | **LEAN_PROVED (as definition):** `QOU.HeckeAlgebra.*` Lean modules (e.g., `/home/user/qou/content/quantum-observable-universe/lean/QOU/HeckeAlgebra.lean` umbrella; `Common`, `Hoefsmit`, `Wedderburn`, `MarkovTrace`, `Formal`, `Realification`). Algebra exists in Lean. The quadratic relation is not exposed as a stand-alone theorem with a `-- Ref:` line that matches CLAUDE.md §7a, but the underlying definitions are present. |
| 2 | `T_i⁻¹ = T_i − (q − q⁻¹)` | **LEAN_MISSING** as a stand-alone theorem. Implicit in any concrete realisation of the algebra. |
| 3 | GS-NF right-action rule | **LEAN_MISSING.** No `right_mul_T` theorem in the QOU Lean tree that proves the case split (ascending = `T_{ws_i}`, descending = `(q−q⁻¹)T_w + T_{ws_i}`). |
| 4 | Coxeter length | **LEAN_MISSING** in QOU. (Mathlib has `Coxeter.Length`; not wrapped in QOU.) |
| 5 | GS-filtration certificate | **LEAN_HAS_SORRY (class-axiomatised, no sorry literal):** `QOU.BraidKnot.GradedMarkovTraceFromGSFiltration` class at `/home/user/qou/content/quantum-observable-universe/lean/QOU/BraidKnot/GradedMarkovTraceFromGSFiltration.lean` (L45) wraps the existence as a class with `gradedTrace`, `markovValue`, `descends_from_markov`. The class records only the level-0 descent identity (L56–57); the per-level descent is NOT axiomatised. The downstream theorem `graded_markov_trace_from_gs_filtration` (L63) proves only the level-0 identity. Citation: `-- Ref: [manuscript] prop:graded-markov-trace-from-gs-filtration` (L62). |
| 6 | Jet-order data model | **LEAN_MISSING.** No Lean type corresponds to `JetEvent`. |
| 7 | σ_1³ closed form in H_2 | **LEAN_MISSING.** |
| 8 | Ascending-word filtration shapes | **LEAN_MISSING.** |

---

## 3. `term5_v2_chirality.py`

### (A) Math claims inventory

1. **V2 chirality identity** (the conjecture proper):
   `a_K = G_{β, β*} / G_{1, 1} = τ(β · β*⁻¹)`
   with `β* = β_mirror` (geometric mirror knot)
   (module docstring lines 11–16). The script computes
   `a_K = τ(β · β_mirror⁻¹)` via the Wedderburn partition sum.
2. **Mirror-word identity for pure-crossing atom braids**:
   `β_mirror⁻¹ = reverse-word(β)` for words of the form
   `[(strand-tuple, ε) ...]` where ε ∈ {0, −h} encodes σ_i vs σ_i⁻¹
   (function `v2_composite_word`, lines 62–69). The docstring cites
   `probe_term5_aK_v2_mirror_chirality.py` for derivation.
3. **Composite-word V2 evaluation**:
   `a_K = Σ_{λ ⊢ 3A} y_λ(q_0) · χ^λ_q(composite_word)`
   over partitions of `3A`, with `y_λ` the canonical Wenzl–Schur weight
   and `χ^λ_q` the Hoefsmit q-character (function `_aK_v2_cached`,
   lines 72–110).
4. **3A-strand atomic-braid convention**: a braid of an atom (Z, N)
   lives in `H_{3A}` where `A = Z + N` (line 80, calling
   `atom_braid_word_3A(Z, N, include_inter=True)`).
5. **V1 informationless claim**: the legacy V1 `β* = β⁻¹`
   (multiplicative inverse) gives `τ(β · β⁻¹) = τ(1_n)` depending
   only on strand count, hence "informationless" — motivating V2
   (docstring lines 15–18). This is a *meta-claim* about which
   chirality measure carries braid information.

### (B) Paper content-block backing

| # | Claim | Backing |
|---|-------|---------|
| 1 | `a_K = G_{β,β*}/G_{1,1} = τ(β · β*⁻¹)` (conjecture proper) | **BACKED:** `conj:knot-factor-frobenius-pairing` at `/home/user/qou/content/quantum-observable-universe/braids-and-knots/knot-factor-frobenius-pairing.md`. Lines 18–26 give the boxed identity `B_bulk = E_0 (\|tr_M(W_free)\| − \|tr_M(W_atom)\|)` and lines 96–101 explicitly define the knot-factor ratio as `a(N) = \|tr_M(W_atom)\|/\|tr_M(W_free)\|`. The Frobenius-pairing form is the abstract restatement (the conjecture title in the `.ts` is literally "Knot factor as Frobenius self-pairing ratio"). Also `prop:chirality-from-frobenius-self-pairing` at `chirality-from-frobenius-self-pairing.md` defines `a_K(β) := τ(β · β*) / τ(1·1)` (lines 19–23), exactly the script's formula. |
| 2 | `β_mirror⁻¹ = reverse-word(β)` for pure-crossing atom words | **UNBACKED:** the script docstring cites `probe_term5_aK_v2_mirror_chirality.py` as the derivation source. No paper block formalises this word-level identity. The geometric content (mirror knot = each crossing flipped) is alluded to by `chirality-from-frobenius-self-pairing.md` ("the antipode σ_i ↦ σ_i⁻¹, reverse word order", lines 14–16), which captures the same operation, but does NOT spell out the per-tuple ε encoding the script uses. |
| 3 | Wedderburn partition sum for V2 a_K | **BACKED:** `rem:recomputed-low-isotope-mass-table` at `recomputed-low-isotope-mass-table.md` (lines 36–47) gives the formula `tr_M = Σ_λ y_λ χ^λ` with `β_K = atom_braid_word_3A(Z, N)` and per-block `Δ_λ` correction. The V2 evaluation in `term5_v2_chirality.py` is exactly this sum applied to the composite mirror word. The `y_λ` Wenzl weight is backed by `prop:wedderburn-weight-canonical` (`wedderburn-weight-canonical.md`); the Hoefsmit `χ^λ_q` by `prop:q-hecke-seminormal-character-closure` (`q-hecke-seminormal-character-closure.md`). |
| 4 | Atomic-braid 3A-strand convention | **BACKED:** `prop:atomic-mass-gb-nf` at `/home/user/qou/content/quantum-observable-universe/braids-and-knots/atomic-mass-gb-nf.md` (line 6) states `n = 3A + Z`. The script uses `n = 3A` only; this is a script-side variant of the paper's atomic-braid layout (paper's def:atomic-braid is what the script's `atom_braid_word_3A` implements; the `+ Z` electron strands are handled separately or absorbed). |
| 5 | V1 informationless claim | **UNBACKED:** this is a script-side methodological argument explaining the V1→V2 transition. No paper block states "the multiplicative inverse `β⁻¹` gives an `a_K` that depends only on strand count". |

### (C) Lean proof coverage

`term5_v2_chirality.py` is a Python library — it has no `.lean` sibling.
The backing content blocks have these Lean coverage states:

| # | Claim | Lean status (via backing block) |
|---|-------|------|
| 1 | `a_K = τ(β · β*)` | **LEAN_HAS_SORRY (conjecture class):** `QOU.BraidKnot.KnotFactorFrobeniusPairing` at `/home/user/qou/content/quantum-observable-universe/lean/QOU/BraidKnot/KnotFactorFrobeniusPairing.lean`. The class (L47) carries fields `markov_trace_q`, `frobenius_pairing_q`, `knot_factor`, `factorisation_holds`. The conjectural content is the `factorisation_holds` field. A `canonical` instance (L82) discharges it tautologically (both functions are `0`, equality is `rfl`), which is **trivially Lean-verified but encodes none of the conjectural content** (per the instance docstring L78–81). Citation: `-- Ref: [manuscript] conj:knot-factor-frobenius-pairing` (L81). The companion `prop:chirality-from-frobenius-self-pairing` declares `lean.ref = qou:QOU.BraidKnot.chirality_frobenius_self_pairing` but **no such Lean declaration exists in the QOU tree** (grep returns no match). So this is effectively **LEAN_MISSING** for the `chirality_frobenius_self_pairing` ref. |
| 2 | Mirror-word identity | **LEAN_MISSING.** |
| 3 | Wedderburn partition sum | **LEAN_PROVED (definition):** `QOU.HeckeAlgebra.Wedderburn`, `Hoefsmit`, `JonesMarkovWenzl` files exist (`/home/user/qou/content/quantum-observable-universe/lean/QOU/HeckeAlgebra/`). The sum `Σ_λ y_λ χ^λ` exists as a Lean def in those modules. Whether a *theorem* equating this to `tr_M(β)` (Wenzl's theorem) carries a sorry was not verified line-by-line in this audit. **LEAN_PROVED (defn level)**; theorem-level status not confirmed. |
| 4 | 3A-strand atomic braid | **LEAN_MISSING.** No `atom_braid_word_3A` analogue in QOU Lean tree. The `atomic-mass-gb-nf.lean` file abstracts the braid as an arbitrary element `β_K : A` (L86). |
| 5 | V1 informationless claim | **LEAN_MISSING (and not appropriate for Lean — methodological).** |

---

## Summary Table

| File | Total claims | BACKED | LEAN_PROVED (sorry-free) | LEAN_HAS_SORRY / class-conditional | LEAN_MISSING |
|------|:----:|:------:|:--------:|:-----:|:-------:|
| `bw_chirality_isotopes.py` | 12 | 12 | 7 (λ_V, λ_S, λ_C, a_asym + relation, δ_P, λ_ex + relation, δ_S) + 2 (fig8 def + positivity) = **9** | 1 (`fits_AME` conjecture class) | 2 (magic-Gaussian def, composite chirality formula for A≠3 cases) |
| `gb_filtration_jet_tracker.py` | 8 | 2 fully (GS-filtration, Hecke relations via convention) + 1 marginal | 0 (no theorem-level Lean for the script's mathematical core) | 1 (GS graded-trace class with level-0 only) | 7 |
| `term5_v2_chirality.py` | 5 | 3 (V2 a_K identity, Wedderburn partition sum, 3A-strand convention modulo +Z) | 0 sorry-free theorem-level | 1 (`KnotFactorFrobeniusPairing` class with tautological skeleton instance — encodes none of the conjectural content) | 4 |

**Aggregate:**
- **25 distinct math claims** across the three files.
- **17 BACKED** by a content block in `content/quantum-observable-universe/`.
- **9 LEAN_PROVED (sorry-free, theorem-level)** — all from `q-integer-mass-formula.lean` and `figure-eight-bw-coefficients.lean`.
- **3 LEAN_HAS_SORRY** in conjecture-class form (`fits_AME`, `gradedTrace` per-level descent, `factorisation_holds`) — formally per CLAUDE.md §3b-cond, the class fields are *not* `sorry` literals but the discharging instances are tautological / level-0-only.
- **13 LEAN_MISSING** — the GS right-action rule, the explicit Hecke quadratic / inverse identities at theorem level, the mirror-word `β_mirror⁻¹ = reverse-word(β)` identity, the magic-proximity Gaussian, and most of `gb_filtration_jet_tracker.py`'s mathematical infrastructure.

## Notable findings

1. **`bw_chirality_isotopes.py` is the best-supported of the three.**
   Every coefficient definition has a corresponding Lean `def` with
   a `-- Ref:` comment, and the two algebraic relations
   (`a_asym = (3/2)λ_V` and the exchange–Coulomb identity) are proved
   sorry-free in Lean. The accuracy claim against AME data is correctly
   class-axiomatised (CLAUDE.md §3b-cond).

2. **`gb_filtration_jet_tracker.py`'s core right-action rule is
   formally unbacked.** The Hecke quadratic identity, the σ-inverse
   rule, and the ascending/descending case split for `T_w · T_i`
   are all standard but appear only in CLAUDE.md §7a and in script
   docstrings — there is no `prop:hecke-right-action-rule` block,
   and no Lean theorem proving the case split. The `JetEvent` data
   model is purely a script-side convention.

3. **`term5_v2_chirality.py` relies on a tautological Lean skeleton.**
   The `KnotFactorFrobeniusPairing` class has a `canonical` instance
   (L82–87) whose `factorisation_holds = rfl` is trivially true
   because both `markov_trace_q` and `frobenius_pairing_q` are
   constant zero. This satisfies the §3b-cond hypothesis at the type
   level but encodes none of the conjectural content. The script
   computes the actual Markov trace via the Wedderburn sum, which is
   independent of any Lean instance.

4. **One broken Lean ref.** `chirality-from-frobenius-self-pairing.ts`
   declares `lean.ref = "qou:QOU.BraidKnot.chirality_frobenius_self_pairing"`
   but no such declaration exists in the QOU Lean tree. This is a
   `validation: "not_checked"` block; the validator would flag this
   on a strict run.

5. **Mirror-word identity needs a content block.** The identity
   `β_mirror⁻¹ = reverse-word(β)` (used in `v2_composite_word`,
   lines 62–69 of `term5_v2_chirality.py`) is the entire algebraic
   content of the V2 derivation, but is documented only in a sibling
   probe script's docstring. A short proposition in
   `braids-and-knots/` (e.g. `prop:atom-braid-mirror-reverse`) would
   close this gap.
