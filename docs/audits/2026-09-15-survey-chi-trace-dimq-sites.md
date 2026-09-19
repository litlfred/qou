# Survey: every χ / tr(id_A) / dim_q site in the corpus (2026-09-15)

**Purpose.** Input to the analysis in
[`2026-09-15-chi-as-a-component-of-the-chern-character.md`](2026-09-15-chi-as-a-component-of-the-chern-character.md)
(bean `qou-nnyn`, issue #7425): before deciding whether `χ(A) = −6` has been
treated as a bare scalar where it is one component of a graded object, list
every place the corpus defines, asserts or uses it, and say which *trace* each
site means. Produced by a read-only survey agent this session and transcribed
verbatim here (the agent could not write files); paths and quotations were
spot-checked by the session before commit. Read it as a **measurement of the
corpus on `main` at `0509e4010`**, not as an assessment — the assessment is in
the analysis doc.

Two path corrections against the brief that requested this survey: the chapter
directory is `lifting-and-descent`, not `lifting-descent`, and it has **no**
`chapter-overview.md`; the "force χ(A) = −6" sentence lives in
`introduction/chapter-overview.md`. `genus-filtration-derivation-chain` and
`chi-minus-six-chain` are both in `brings-surface/`.

## Method — greps run (repo root), file counts

| # | command (all `-rl`, `--include=*.md --include=*.ts --include=*.lean`, under `content/quantum-observable-universe`) | files |
|---|---|---|
| A | `grep -rl "tr(id" content/` | **14** |
| B | `grep -rlE "χ\|\\\\chi\|[Ee]uler characteristic"` | 847 |
| C | `grep -rlE "dim_q\|\\\\dim_q\|qdim\|quantum dimension"` | 309 |
| D | `grep -rlE "HH\^0\|HH_0\|HH\^2\|HH²\|HH⁰\|Hochschild"` | 75 |
| E | `grep -rlE "K_0\|Grothendieck group\|Chern character"` | 16 |
| F | `grep -rlE "Riemann.{1,3}Roch\|Hirzebruch"` | 10 |
| G | `grep -rlE "MarkovTrace\|tr_M\|Markov trace"` | 1134 |
| H | `grep -rlE "\-6\|−6"` | 497 |
| I | `grep -rlE "genus[- ]4\|genus[- ]four\|g = 4\|g=4\|\\\\Sigma_4\|Σ_4\|Σ₄" --include=*.md` | 121 |
| J | `grep -rlE "tr\(id\|chi\(A\)\|χ\(A\)\|dim_q\|euler" .beans/` | 120 |

Also: `find content docs -path "*<label>*"` for each named block; `grep -rn "euler_char_constant"`; `grep -rn "= -6 := \|:= -6\|= -6 := rfl"` over `*.lean`; per-file `grep -c sorry`. Zero non-comment `sorry` in every Lean file quoted below. "Chern character", "ch(A)", "K^0", "index of the Dirac", "Wenzl" ∩ χ, "categorical trace" ∩ HH: **no hits** — nothing in the corpus writes ch(A) or a Chern character at all. **Riemann–Roch appears in 10 files but never with a Todd class or a rank/degree pair beyond `(r,d) = (2,0)`.**

---

## 1. The three-values collision — the corpus already knows

`content/quantum-observable-universe/notation/notation-collisions.md:21` is a ~1400-word register entry whose own headline is the finding:

> **"$\mathrm{tr}(\mathrm{id}_A)$ names three different objects, and two corpus claims about it are in direct conflict — resolve the symbol to its object before quoting a value."**

and it records an owner decision the same day:

> **"🟧 OWNER RULING 2026-09-15 — reading (iii) is the categorical trace: $\mathrm{tr}(\mathrm{id}_A) = \dim_q(A)$, the quantum dimension, which *is* the Euler characteristic of an object in the QOU category."** Verbatim: *"i think it is $[2]_q$ ... euler characteristic of object in the QOU category"*.

Crucially, the register entry itself already names the graded-object answer as the open residue (same line):

> **"So the $-6$ needs the *Euler-characteristic-of-a-complex* sense — an alternating sum — rather than a naive $\dim_q$. Not decided here."**

and line 19 fixes notation: **"Euler characteristic is $\chi_{\mathrm{eu}}$ — never a bare $\chi$."** Note line 20 reserves a *different* −6 (the GGM/Stokes sandwich entry, `partitionEuler3_eq` = −2 × count 3) that is explicitly **"not an Euler characteristic"**.

**`notation-register.md` has no entry at all** for χ_eu, tr(id_A), or the Euler characteristic (43-line index; Table 6 = Descartes ch.9 has 5 rows, none about χ). `notation-register-table3-data.md:20` defines only `dim_q(λ) = [n]_q!/∏[h_x]_q` (hook-length, per *partition*), and :14/:17 `tr_M`, `z = q²/[2]_q`. So the collision is documented only in `notation-collisions.md`, never in the register proper.

## 2. Per-site table — which trace is meant

Codes: (a) Hom-level monoidal trace / dim_q · (b) topological χ_eu of a space · (c) alternating sum of cohomology dims · (d) HH-class / K₀-class level · (e) Markov trace on Hecke · (f) operator index · (g) unclear.

### Block triples

**`brings-surface/brings-euler-characteristic.{md,ts,lean-ref}`** — `lem:brings-euler-characteristic`, lemma. `.md:1–7`: *"The categorical Euler characteristic $\chi(A) = \mathrm{tr}(\mathrm{id}_A)$ … equals $\chi(A) = \chi(\Sigma_4) = 2 - 2g(\Sigma_4) = -6$. This value is recovered as the quantum dimension specialised at the Descartes substrate parameter $q_0$."* **Trace: (a) and (b) asserted equal in one breath — this is the primary conflation site.** `.ts:10 uses: ["prop:euler-char-stability"]`, `proofs: ["prf:brings-euler-characteristic"]`, `lean: qou:QOU.ArchimedeanUniverse.brings_euler_characteristic`. `.ts:17` authorNote (2026-09-15) carries the ruling and says the −6 here is topological, that euler-char-stability is now *"a substantive claim relating two different things"* holding *"at most on a locus in q"*, and that **"a quantum dimension of −6 is negative, while dim_q … is positive (the fundamental gives +2.0109)"**.

**`brings-surface/brings-euler-characteristic-proof.md`** — `prf:brings-euler-characteristic`, proof; `.ts:6 uses: ["lem:brings-euler-characteristic"]`. Lines 10–14: *"Equivalently, computing via the categorical trace at $\mathbf{C} = \mathrm{Rep}(\mathrm{SU}_q(2))$, the quantum dimension of $A = \mathcal{O}_q(\mathrm{SU}(2))$ specialises at the Descartes substrate parameter $q_0$ to the value $-6$, matching the topological count."* **Trace: (a) claimed ≡ (b). The "quantum dimension of $\mathcal{O}_q(SU(2))$" is the object the Lean sibling says diverges.**

**`brings-surface/archimedean-condition.{md,ts,lean}`** — `def:archimedean-condition`, definition ("Descartes condition"). **This is the K₀ site.** `.md:4` `\chi(A) = \mathrm{tr}(\mathrm{id}_A) = -6 \in R`; `.md:7`: *"This requires $6 \in R^{\times}$… **The class $[A] \in K_0(\mathbf{C})$ has rank $-6$.**"* **Trace: (d) — the only place the corpus puts −6 on a K₀ class, and it calls it a *rank*, which is a K₀→ℤ component, not the whole class.** `.ts uses: ["thm:qu-to-qou"]`. `.lean` (sorry-free): `structure ArchimedeanCondition (R) [CommRing R]` with **field** `eulerChar : R` and **field** `euler_eq : eulerChar = -6` — i.e. −6 is a *structure field constraint*, assumed; `descartes_genus_is_four` is a proved `theorem` but only `χ = −6 ∧ 2−2g = χ → g = 4`.

**`brings-surface/chi-minus-six-chain.{md,ts}`** — `ex:chi-minus-six-derivation`, example. `.md:1`: *"Step 5, which fixes the branch-point count at six, reads that count off the Weierstrass points of Bring's surface — the surface the chain then identifies at Step 7 — so the chain locates the value rather than deriving it from the axioms alone."* Step 3 (`:7–11`) is the Riemann–Roch leg: `\chi(V) = d + r(1-g) = 0 + 2(1-g) = 2-2g`. Step 6 (`:17`): *"$\chi(V) = -6$ means $h^0(V) - h^1(V) = -6$, so $h^1(V) \geq 6$."* **Trace: (c) — explicitly an alternating sum $h^0 - h^1$ of sheaf-cohomology dimensions of a rank-2 bundle. Note this is χ(V) for the *bundle*, silently identified with χ(A) for the *algebra*.** `.ts:4` `interprets: "def:archimedean-condition"`, `uses: ["def:archimedean-condition","def:motivic-substrate","prop:euler-char-stability","rem:kummer-tower","thm:motivic-perpetual-obstruction"]`, `cites: ["braden-disney-hogg-2022"]`. `.ts:21` authorNote records the Weierstrass fix (Bring has **60** points in one transitive Aut-orbit, `60 = 6 × 10`, six per transposition, degree-2 quotient genus 1) and concludes **"The step is now true; it is not a derivation."**

**`brings-surface/genus-filtration-derivation-chain.{md,ts}`** — `rem:genus-filtration-derivation-chain`, remark; `interprets: "prop:genus-filtration-ideal"`, `uses: ["prop:genus-filtration-ideal","rem:torus-evaluation-block-rank"]`. `.md:9` step 7: *"$\Sigma_4$ is the unique genus-$4$ curve with maximal symmetry ($S_5$), fixed by $\chi = -6$."* `.md:11`: **"Step 3 does not hold, so the chain does not deliver the genus"** — the evaluation matrix is block-diagonal, rank ≤ 2+2 = 4 for every q. `.md:13`: **"What the chain does establish is step 1, and independently of $\chi$"** — the volume axiom Λ²V ≅ 𝟙 forces dim V = 2 *"with no Euler characteristic, genus, or reference to Bring's surface anywhere"*. `.md:15`: **"Consequently the closing claim is withdrawn."** **Trace: (g)/none — this block is about the derivation order, not about which trace.**

**`lifting-and-descent/euler-char-stability.{md,ts,lean}`** + `-proof.md` + `-C.md` — `prop:euler-char-stability`, proposition. **This is the bridge everything else leans on.** `.md:1`: *"The categorical Euler characteristic $\chi(A_n) := \mathrm{tr}(\mathrm{id}_{A_n})$ is the rigidity trace of the identity endomorphism in $\mathbf{C}$"*; `.md:5`: *"In the archimedean realisation, $\chi(A_n) = \chi(\mathcal{S}_n)$ is the topological Euler characteristic of the total space $\mathcal{S}_n$."* `-proof.md:1` makes the trace unambiguous: `\mathrm{tr}(\mathrm{id}_{A_n}) = \mathrm{ev}_n \circ \mathrm{coev}_n`, the composite `𝟙 → A_n ⊗ A_n^∨ → 𝟙`. **Trace: (a) in the .md/-proof.md (textbook rigid monoidal trace, so literally dim_q), silently equated to (b) by the last sentence.** `-C.md` proves stability by Leray–Serre with `χ(S²) = 2` — pure (b). `.ts:7 lean: qou:QOU.Torsion.euler_char_constant`; `uses: ["def:quantum-characteristic-classes"]`, `proofs: ["prf:euler-char-stability","prf:euler-char-stability-C"]`. **This proposition proves only *stability*, never a value** — see Lean below.

**`lifting-and-descent/quantum-characteristic-classes-su2.{md,ts}`** — `ex:quantum-characteristic-classes-su2`, example; `interprets: "def:quantum-characteristic-classes"`, `uses: ["def:quantum-characteristic-classes","ex:recursive-brane-tower-su2"]`. `.md:10`: *"Under the trace map $H^2(\mathcal{S},\mathcal{B}) \to R$, the obstruction maps to the Euler characteristic: $\kappa_0 \mapsto \mathrm{tr}(\mathrm{id}_A) = \chi(\mathbb{CP}^1) = 2$."* **Trace: (b) for the value 2, but reached through a (d)-style trace map out of $H^2$.** `.ts:14` authorNote: the open residue is that this and `lem:brings-euler-characteristic` *"apply the same `prop:euler-char-stability` bridge to **different S** … so at most one describes the Descartes universe's state bundle"*.

**`predicted-spectra/knot-operator-selection-proof.{md,ts}`** — `prf:knot-operator-selection`, proof; `uses: ["prop:knot-operator-selection"]`. `.md:66` is the decisive line — *"The minimum-energy supply is the coevaluation $\mathrm{coev}_A \colon \mathbf{1} \to A \otimes A^\vee$… **Its cost is $\mathrm{tr}(\mathrm{id}_A) = [2]_q = q + q^{-1} \approx 2.011$.**"* `.md:14` also asserts the identification **`\mathrm{tr} = \mathrm{tr}_M`** ("archimedean descent"); `.md:19` `\langle a,b\rangle_F = \mathrm{tr}_M(\rho(\hat\beta_a)\rho(\hat\beta_b))`; `.md:44` records the 6×6 Gram matrix of $H_3(q)$ is singular (**convention D**, radical = the $(1^3)$ block). **Trace: (a) for the `[2]_q` value (dim_q of the *fundamental* $V_1$ — a third object, not $A$), (e) for the Frobenius pairing.** `.ts:12` authorNote: **"This block's reading is the one the owner selected."**

**`predicted-spectra/knot-operator-selection.md`** — `prop:knot-operator-selection`. `.md:4` opens with *"Let $\{\tau(r_i,s_i)\}_{i=1}^{6}$ be the embeddable torus knots on $\Sigma_4$"* — **six, taken from $\Sigma_4$, not from χ**; `.md:22–31` is `\mathcal{S}(\gamma_1,\gamma_2) = \mathrm{tr}(\Phi(\gamma_1\otimes\gamma_2)) = \sum_\lambda d_\lambda(q)\mathrm{tr}_\lambda(\cdots)`. **Trace: (a) weights × (e) block traces.**

**`fluid-dynamics/substrate-line-bundle-base-not-fibre.{md,ts}`** — `rem:substrate-line-bundle-base-not-fibre`, remark; `interprets`/`uses: "def:substrate-line-bundle"`. **Already edited to reflect the ruling.** `.md:10`: *"**The categorical trace $\mathrm{tr}(\mathrm{id}_A)$ is not on this list.** It was, until an owner ruling of 2026-09-15 identified it with the quantum dimension $\dim_q(A)$ … which is manifestly $q$-dependent ($[2]_q = q + q^{-1}$ on the fundamental)."* The four surviving q-independent bullets are `Hom_C(1, Ad(A))`, `c_1(Ad(A))`, `c_2(Ad(A))`, Euler class `e(ξ)`. **Trace: (a) — and note c_1, c_2 of Ad(A) are here, the nearest thing in the corpus to a Chern-class register, but they are never assembled into a ch(A).**

**`brings-surface/universality-general.{md,ts}`** — `rem:universality-general`, remark; `interprets`/`uses: "thm:descartes"`. Whole body (`.md:1`): *"For any admissible Euler characteristic $\chi$, the category $\mathbf{C}_{\chi}$ of $\mathbb{C}$ quantum observable universes with $\chi(\mathcal{S}) = \chi$ should admit a terminal object determined by the unique maximally symmetric Riemann surface of the corresponding genus. Bring's curve distinguishes the Descartes case $\chi = -6$…"* **Trace: (b) — indexes the whole moduli by $\chi(\mathcal{S})$, a topological integer. If the ruling makes χ(A) q-dependent this indexing is by a different object than def:archimedean-condition's.** No authorNote; **not yet touched by the 2026-09-15 pass.**

**`braids-and-knots/skein-resolution-obstruction.{md,ts,lean}`** — `def:skein-resolution-obstruction`. **This is the HH² site.** `.md:1`: *"a fourth evaluation of the universal obstruction class $\chi(A) \in HH^2 \cong k$"*; `.md:7`: `\kappa_c^{\mathrm{comp}}(L,q) = \mathrm{res}_{\mathcal{R}}(\chi(A)) \in H^2(\mathcal{R},\mathbb{G}_m)`; `.md:11`: *"**A single integer $\chi(A) = -6$** controls whether these computational problems persist"*; `.md:17`: `\kappa_c^{\mathrm{comp}} \bmod n = 0 \iff n \mid \chi(A)`. **Trace: (d) — χ(A) is a *class in HH²*, then divided by integers. "A single integer" is exactly the scalar collapse the analysis is looking for.**

**`stochastic-mechanics/qou-obstruction-millennium-specializations.md`** — same class, three evaluations. `.md:3`: *"All three obstructions are images of the same class $\chi(A) \in HH^2 \cong k$ under different evaluation maps."* `.md:8` already retracts the naive inference: *"One-dimensionality is a property of $HH^2 \cong k$, the **source** … It does not make the three images proportional to each other: they land in three different groups … with no canonical identification between them, so cross-target proportionality is not even well-typed."* `.md:10`: **"The restrictions demonstrably disagree"** — level 2 vanishes at χ = −6 (proved, `collatz_obstruction_link.lean`) while the tree residue is non-zero at non-torsion q₀. **Trace: (d).** Companions: `stochastic-mechanics/qou-obstruction-reduction-proof.md:3` *"Step 1: Observability kills $HH^0$"*, `:46` *"Therefore $HH^2 \cong k$"*; `-table1-data.md:5` `HH^2(\mathrm{Ad})` → *"= 1 (single scalar)"*; `classical-limit-obstruction-properties.md:3–6` the HH⁰/HH¹/HH² tower; `quantum-universes/poisson-hkr-connection.md:6` the HKR map out of `HH^2(A,A)`. **Nowhere is HH_0 (homology, degree 0) used — the corpus works entirely in HH^• cohomology. There is no ch(A) ∈ HH_0 anywhere.**

**`information-theory/qou-p-neq-np.md`** — `.md:33` is one of the two statements bean `qou-51l1` found in direct conflict: *"The third leg, the Riemann–Roch / branch-point chain that pins the scalar to $-6$ …, **reads its branch-point count off Bring's surface rather than deriving it, so the value is located within the axiom cone rather than forced by it**."* `.md:43`: *"The QOU obstruction reduction **conjectures** that all classical-limit obstructions map to the scalar class $\chi(A) \in HH^2$."* **Trace: (d), and note the word "scalar".**

**`introduction/chapter-overview.md:30`** (the "force" sentence; there is no `lifting-and-descent/chapter-overview.md`): *"The lifting obstructions **reduce the whole obstruction to a single scalar $\chi(A) = 2 - 2g$ with $g \geq 1$; the Descartes condition fixes its value at $-6$.**"* **This is the single clearest statement of the scalar collapse: "reduce the whole obstruction to a single scalar".** Bean `qou-51l1` quotes an older form of the same line as *"The lifting obstructions **force** the Descartes condition $\chi(A) = -6$"* — the current text says "fixes", weaker.

**`braids-and-knots/why-b3.md:1`** — the return arrow of the cycle: *"The Descartes condition $\chi(A) = -6$ forces the gauge group to be a quantum form of $\mathrm{SU}(2)$, which has rank $1$."* **Trace: (g) — uses χ as a bare integer input with no trace semantics.**

**`brings-surface/descartes-knot-eigenbasis-derivation.md:2`** — *"The Descartes condition forces $\chi(A) = -6$. This sets the genus $g = 4$ and gauge group $\mathrm{SU}_q(2)$ to rank $2$."* (rank 2 vs why-b3's rank 1 — an unrelated inconsistency in passing.) **Trace: (g).**

**`brings-surface/torus-knot-generators.{md,ts}`** — `prop:torus-knot-generators`. `.md:1`: *"The Euler characteristic $\chi(A) = -6$ forces torus knots to serve as the generators … **whose cardinality is entirely determined by $\chi$**"*; `.md:8` does the actual work from g: `g(T_{m,n}) = (m-1)(n-1)/2 \leq g(A) = 4` ⟹ *"exactly six coprime pairs … the generator set has $|\mathcal{G}| = 7$."* **Trace: (b) nominally, but the computation uses only the integer g = 4 — see §5.**

**`lifting-and-descent/motivic-perpetual-obstruction.md:11`** — *"identify $\kappa_0$ with the Euler class $e(\xi)$ of the Reeb bundle, satisfying $\mathrm{tr}(\kappa_0) = \chi(A)$"* — a **(d)→scalar trace map** again.

### Lean library files

| path | decls | −6 is | sorry-free |
|---|---|---|---|
| `content/quantum-observable-universe/lean/QOU/ArchimedeanUniverse/brings_euler_characteristic.lean` | `class BringsEulerCharacteristicContext` (fields `q0 : R`, `g : ℕ`, `genus_is_four : g = 4`); `def chi_A := 2 - 2*g`; `def qdimUnit (_q) := 1`; `def categoricalTrace q := 1*qdimUnit q - (2*g)*qdimUnit q + 1*qdimUnit q`; **theorems** `brings_euler_characteristic`, `categorical_trace_eq_euler`, `categorical_trace_q_independent`, `categorical_trace_eq_neg_six`, `quantum_dimension_recovers_chi` | **proved theorem** (`norm_num` from the field `g = 4`); −6 is *not* a field | yes (0 sorry; docstring at :212 asserts "Fully derived (no `sorry`)") |

**This file is the single most important site for the question.** It models tr(id_A) as **(c)** — an alternating sum — and says so explicitly at `:42`:
```
  tr(id_A)(q)  =  Σ_{i=0}^{2} (−1)^i · dim_q H^i(Σ_g)
```
`:38` *"`tr(id_A)` is the **super-trace** (categorical Euler characteristic) of the identity over the cohomology of the surface"*. `:63–68` is the divergence admission:
> *"**Honesty on the object.** The naive Peter–Weyl quantum dimension of the full coordinate Hopf algebra, `dim_q 𝒪_q(SU(2)) = Σ_n [n+1]_q²`, **diverges**; the finite value `−6` is the **categorical Euler characteristic / super-dimension**, not that divergent sum."*

And `:69–73` disclaims the bridge the .md blocks cite:
> *"there is **no** upstream Lean theorem asserting `tr(id_A) = 2 − 2g` — `QOU.Torsion.euler_char_constant` (`prop:euler-char-stability`) proves only *stability* of the Euler characteristic across brane-tower levels, **not its value**, so it is not cited here as establishing the value."*

`:29–36` scopes the gap: *"This file does *not* construct the category `Rep(SU_q(2))` or its objects"*; the whole q-dependence cancels because `qdimUnit ≡ 1` is **assumed** (`def qdimUnit (_q : R) : R := 1`), justified only by the motivation that `H^i(Σ₄)` are quantum-trivial. **So: the Lean carrier of the −6 works at level (c), while the .md it certifies claims level (a). The mismatch is internal to the block triple.**

| path | decls | −6 is | sorry-free |
|---|---|---|---|
| `lean/QOU/Torsion/BraneTower.lean:107–118` | `structure EulerCharStability (tower)` with fields `eulerChar : ℕ → ℤ`, `stable : ∀ n, eulerChar (n+1) = eulerChar n`; `theorem euler_char_constant` | **absent** — no value at all; `eulerChar` is an opaque field | yes |
| `lean/QOU/BringsSurface.lean:234–252` | `structure BringsQOU` with `eulerChar_eq : eulerChar = -6 := by rfl`, `branch_points_eq : num_branch_points = 6 := by rfl`, `total_ramification := 14`; `theorem is_qou` | **structure field** (auto-`rfl` against a `def eulerChar`) | yes (0) |
| `lean/QOU/BringsSurface/EulerCharacteristicSix.lean` | `def seifertRank`, `def Embeds`, `theorem genus_forced` (from `Embeds 2 9 g ∧ ¬Embeds 2 11 g`), `def eulerChar g := 2-2g`, `theorem eulerChar_forced`, `theorem finrank_H3Carrier_eq_factorial`, `theorem abs_eulerChar_eq_finrank_H3` | **proved theorem**, conditional on the two embeddability hypotheses | yes |
| `lean/QOU/BringsSurface/BranchPointSixNotForced.lean` | `def eulerChar`, `def Step34Admissible`, `theorem neg_six_admissible / neg_four_admissible / neg_eight_admissible / all_even_nonpos_admissible / step34_admissible_iff`, `def chiOverP1`, `theorem bring_weierstrass_count` (= 60), `theorem bring_weierstrass_count_ne_six`, `theorem weierstrass_split_six_by_ten`, `theorem bring_quotient_by_transposition`, `theorem chi_over_torus_is_minus_ramification` | **proved theorems, and they prove −6 is NOT forced**: Steps 3+4 admit every even non-positive χ | yes (`#print axioms`: `propext`, `Quot.sound` only, per bean `qou-qhcr`) |
| `lean/QOU/Information/ChiMinusSix.lean` | `def eulerChar`; `class QOUCohomology` (`hh0 = 0`, `hh2 = 1` as rank fields); `theorem obstruction_rank_one`; `class QOUObstruction extends QOUCohomology` (fields incl. `chi`, a Riemann–Roch field, a Bring-genus field); `theorem chi_eq_neg_six`, `theorem chi_ne_zero` | **proved theorem, conditional on the class fields** — docstring `:23–25`: *"**derives** `-6` from them by Euler-characteristic arithmetic … it never carries `-6` as a bare field"* | yes |
| `lean/QOU/ClassicalLimitObstruction.lean:36–92` | `structure ClassicalLimitObstruction (k)` with field `eulerChar : ℤ` *"which generates"* the rank-1 obstruction space; `def descartesObstruction` with `eulerChar := -6`; `theorem kummer_obstruction_divisibility` | **`def` value assignment** | yes |
| `content/.../brings-surface/archimedean-condition.lean` | `structure ArchimedeanCondition` fields `eulerChar : R`, `euler_eq : eulerChar = -6`; `def totalRamification d := 2*d+6`; `theorem descartes_genus_is_four` | **structure field constraint (assumed)** | yes |
| `content/.../brings-surface/descartes.lean` | `structure DescartesUniverse` fields `eulerChar : ℤ`, `euler_eq : eulerChar = -6`, `gauss_bonnet`; `def bringsSurface` with `eulerChar := -6`; `theorem DescartesUniverse.genus_eq_four`, `brings_euler := rfl` | **field + `def` assignment** | yes |
| `content/.../brings-surface/genus-maximal-descent.lean` | `structure GenusMaximalDescent` (`euler_eq : eulerChar = -6`); `theorem genus_eq_four`, `theorem genus_unique` | **structure field** | yes |
| `content/.../brings-surface/brings-is-qou.lean` | `structure BringsIsQOU` (field `euler_char`); `theorem brings_euler_char_neg_six`; `def standardBringsIsQOU` with `euler_char := -6`. `:25` docstring: `χ(A) = tr(id_A) = 2 − 2g = −6` | **`def` assignment**, theorem reads it back | yes |
| `content/.../lifting-and-descent/quantum-characteristic-classes.lean` | `structure QuantumCharacteristicSequence` fields `eulerChar : ObstructionSpace`, `kappa_zero_euler : kappa 0 = eulerChar`. `:13`: *"under the trace map, κ₀ ↦ χ(A) = tr(id_A)"* | **no value** | yes |
| `content/.../lifting-and-descent/qu-to-qou.lean` | `structure BranchData` (`eulerChar : ℤ`, `riemann_hurwitz : totalRamification = 2*degree + eulerChar.natAbs`), `structure QuToQou` (`trace_map : kappa_zero_obstruction = eulerChar`) | **no value** | yes |
| `content/.../lifting-and-descent/euler-char-stability.lean` | `def categoricalEulerChar`, `structure JetProlongationSystem`, `theorem euler_char_stable`, `theorem euler_char_constant`, `theorem jet_prolongation_preserves_trace` | **no value** | yes |
| `content/.../climax-volume-mass/vertex-algebra-relations.lean:236` | **`axiom descartes_trace {n} (hp : HeckeParams) : MarkovTrace hp (AlgElement.singleton []) = -6`**, over **`axiom MarkovTrace`** (`:104`); `theorem descartes_genus : (2:ℤ) - 2*4 = -6 := by norm_num` (`:232`) | **`axiom` on top of an `axiom`, for every strand count and every parameter** | file has 0 `sorry` but ~12 `axiom`s |
| `content/.../climax-volume-mass/vertex-algebra-jet-relations.lean:121–135` | `def eulerChar (_n : ℕ) : ℤ := 2 - 2*4` (level discarded by construction); `theorem euler_level_stable (n) : eulerChar n = eulerChar 0 ∧ eulerChar n = -6` | **`def` literal**, theorem is `norm_num` on it | yes |

`descartes_trace` is **trace (e)** — the Markov trace on a Hecke algebra. `notation-collisions.md:21` calls it out by name: *"asserts $\mathrm{tr}(\mathrm{id}) = -6$ as an `axiom`, over a `MarkovTrace` that is itself an `axiom`, for every strand count and every parameter — assumption on assumption … and which under this ruling is now also **wrong in $q$-dependence**."* Independent corroboration of the normalisation clash: `lean/QOU/MathlibExt/MarkovTrace.lean:41–43` states what is *not* proved — *"not the normalisation `tr_M(1) = 1` nor the Markov peel axiom"*. So `descartes_trace` asserts a value for exactly the quantity the corpus's own Markov-trace file flags as un-normalised.

`lean/QOU/BraidKnot/RegularRepBlockTrace.lean:44,121` uses a **fourth** reading: `tr(id) = finrank = |S_n| = n!` — the ordinary matrix trace of the identity on the regular representation.

## 3. Audits from 2026-09-14 / 2026-09-15

Only **two** of the 13 audits in that window touch χ at all (all 13 were grepped for `χ|chi(A)|tr(id|dim_q|Weierstrass`; 11 scored 0). **No audit in that window discusses the "three tr(id_A) values", the dim_q divergence, or Weierstrass points — those live in `notation-collisions.md`, the `.ts` authorNotes, and the beans, not in a dated audit file.**

- `docs/audits/2026-09-14-canonical-chain-condition-walk.md` (20 χ hits) — the substantive one. `:242` diagrams the cycle `why-b3: χ = −6 FORCES SU(2) ⟹ dim V = 2`; `:291` **"The corpus offers three routes to `g = 4` / `χ = −6`. All three name `SU(2)` in their own first or last sentence, so none of them breaks the cycle"** (route 1 `chi-minus-six-chain.md` step 1, route 2 `cohomological-embedding.md`, route 3 `genus-from-hecke-completeness-proof.md`, which also `uses: prop:cohomological-embedding`); `:326` the evaluation matrix `M_ij = χ_{λ_j}(T_{(r_i,s_i)})`; `:793` the full dependency chain `χ = −6 ⇄ G = SU(2) ⟹ dim V = 2 ⟹ ℓ(λ) ≤ 2 ⟹ y_(1³)=0 ⟹ z_D ⟹ α`; `:674–710` separately flags a `χ_top` name collision (motivic measure vs Euler characteristic, "two invariants with different codomains under one name").
- `docs/audits/2026-09-14-gamma-gamma-forces-the-layout-and-the-artin-band-fork.md` (3 hits) — all three are the *character* χ_λ / χ₍₂,₁₎ of the Hecke irreps (`:340,:349,:355`), **not** the Euler characteristic. Listed only to rule it out.

## 4. Beans

120 bean files match the grep; the on-topic ones:

| id | title | status | decisive line |
|---|---|---|---|
| **`qou-nnyn`** | *"chi(A)=-6 as one component of ch(A) in HH_0: locate the implicit scalar assumption and the resolution options"* | **todo** | *"Audit doc. Which corpus step turns the class into a number; which trace level (Hom-level in C vs Hochschild-level on C); options."* — `parent: qou-dgce`. This session's bean. |
| `qou-dgce` | *"Session: chi-as-term-of-ch + HH/HKR/trace exposition arc"* | in-progress (milestone) | this session. |
| `qou-2uf0` | *"FIX: tr(id_A) carries three incompatible values in the corpus (-6, [2]_q, 2) plus an independent-of-q claim"* | **completed** | Body empty; the work product is the `notation-collisions.md:21` entry and the four `.ts` authorNotes. |
| `qou-51l1` | *"GAP: is chi(A) = -6 forced or read off Bring's surface? two corpus statements disagree"* | **todo** | *"They are not two readings of one sentence: (1) asserts obstructions => chi, (2) denies it."* Quotes `introduction/chapter-overview.md:30` vs `information-theory/qou-p-neq-np.md:33`. |
| `qou-qhcr` | *"GAP: derive the branch-point count 6 from the five QOU axioms (the ONE missing step in the chi = -6 chain)"* | **todo, priority high** | **"Outcome: the 6 is still not derived. The ADE / finite-subgroup-of-SU(2) route was tested and is a negative"** — artifacts `BranchPointSixNotForced.lean` (sorry-free, axiom-clean) + `computations/chi_branch_point_count_genericity_probe.py` (18/18, exact `int`/`Fraction`). |
| `qou-r3wu` | *"FIX: genus-from-hecke-completeness claims rank 5 at g=4; measured rank 4, structurally"* | **completed** | Body empty; work product is `genus-filtration-derivation-chain.md:11–15` + `rem:torus-evaluation-block-rank`. |
| `qou-uy5c` | *"DONE: QOU⟹χ(A)=-6 conditional Lean (ChiMinusSix.lean) — cohomological grounding (HH⁰=0, HH²≅k rank1) + Bring genus 4 ⟹ χ=2-2g=-6; chi_ne_zero. §3b-cond, sorry-free"* | **completed** | Title is the content; body empty. The word **"conditional"** is load-bearing. |
| `qou-9gyk` | *"Session: chi register arc — honest wording, the false rank claim, and the three tr(id_A) values"* | **todo** (milestone) | Body empty. |
| `qou-xz89` | *"Remark interpreting 2211.08164v2.pdf at ex:chi-minus-six-derivation"* | **todo** | *"transitive + simple means one orbit of 60, not an S_3-orbit decomposition of 6"*; cite key `[reyescarocca2022]`, source Edge, J. London Math. Soc. 18 (1978) 539–545. |
| `qou-1ucq` | *"The 73x/122x tr_M contradiction is RESOLVED; the residue is six narrative chains describing a route nobody takes"* | completed | Unrelated to χ (numerical tr_M assembly); listed because it matched the grep. |

## 5. Knot-operator space and its dimension — does the count need χ or g?

**The dimension count uses g = 4 directly, through the Seifert-genus bound, never χ.** The "fixed by χ" phrasing is a later gloss.

- `brings-surface/torus-knot-generators.md:8`: `g(T_{m,n}) = \frac{(m-1)(n-1)}{2} \leq g(A) = 4`, then *"The constraint $(m-1)(n-1) \leq 8$ admits exactly six coprime pairs with $m \geq 2$. Together with the unknot $T_{1,0} = 0_1$, the generator set has $|\mathcal{G}| = 7$."* **The arithmetic input is the integer 4 on the right-hand side of an inequality. χ enters only via `:1`'s claim that the cardinality is "entirely determined by $\chi$", which is true only through `χ = 2−2g`.**
- `brings-surface/torus-embeddable-complete.md:1–7`: *"the complete list of torus knots embeddable in the genus-$4$ fiber"* = `{(2,3),(2,5),(2,7),(2,9),(3,4),(3,5)}` + unknot. **Genus only; χ not mentioned.**
- `brings-surface/embeddability-closure.md:1–3`: *"Let $(\mathbf{C},A,\tau)$ be the Descartes universe with $\chi(A) = -6$ **and** fiber genus $g(\Sigma_4) = 4$ … Then: 1. The Seifert genus of $K$ satisfies $g(K) \leq 4$."* **Both are hypothesised; only g is used.** `.ts uses: ["prop:torus-knot-generators"]`.
- `appendix-transfer-matrices/tm-interaction-completeness.md` — the "seven". `.md:1`: *"The embeddability bound on $\Sigma_4$ yields exactly seven transfer-matrix interactions: six non-trivial force operators plus the identity."* But `.md:5–7` derives the 7 from a **completely different** decomposition: *"four crossing types … four operators … two further operators … Total: $1 + 4 + 2 = 7$."* **So the corpus has two independent routes to 7 (Seifert-genus enumeration, and the crossing-alphabet count) and neither uses χ.** `.ts:20` authorNote: the closure-under-composition half is *"left to the formalisation pass"*.
- `EulerCharacteristicSix.lean:121–137`: `theorem abs_eulerChar_eq_finrank_H3` — `|χ(Σ₄)| = 6 = 3! = dim_R H_3(q)`. The file's own header (`:35`) says *"The two numbers are"* equal; it is a numerical coincidence recorded as a theorem, with `genus_forced` upstream of it.
- `molecular-construction/ilp-covalent-bond.md:13`: *"The dual space of the LP is the knot operator space: single-component braid closures."* `mass-theory/operator-selection-lp-proof.md:41` also says "operator space". **Neither cites χ or a dimension.**

## 6. Where g = 4 is load-bearing without passing through χ

121 `.md` files mention genus 4 / Σ₄. The consumers whose *statements* need g = 4 (not just the phrase):

- `brings-surface/torus-embeddable-complete.md` — the generator list is literally the solution set of `(m−1)(n−1) ≤ 8`.
- `brings-surface/embeddability-closure.md` — `g(K) ≤ 4` for every generated knot.
- `brings-surface/genus-from-hecke-completeness.md:1` — *"$g = 4$ is the least genus at which $N(g) \geq 5$"* (a count statement; `:3` **"It does not say that the evaluations available at $g = 4$ span the $5$-dimensional representation … here they provably do not"**).
- `brings-surface/torus-evaluation-block-rank.md` — the block-diagonal rank bound `≤ min(#{r=2},2) + min(#{r=3},3)`, giving 4 not 5 at g = 4. **This is the block that broke step 3.**
- `brings-surface/genus-filtration-ideal.md:1` — the ideal `𝔦_4 = (u^5)`, Chebyshev overflow at degree 5.
- `brings-surface/genus-maximal-descent.md` / `brings-riemann-hurwitz.md` / `descartes.md` — maximal symmetry: `|Aut| = 120 ≤ 84(4−1) = 252` (Hurwitz bound at g = 4). **The Hurwitz bound needs g, not χ.**
- `brings-surface/cohomological-embedding.md` — route 2 to g = 4 (`euler_char_genus_4 : (2:ℤ) - 2*4 = -6 := by decide` in the Lean sibling).
- `knots-particles-confinement/electroweak-triplet-bring-embedding.md`, `electroweak-higgs-torus-link-triplet.md`, `electroweak-triplet-far-commuting-minimal-proof.md` — embed the EW triplet in Σ₄.
- `brings-surface/fivefold-symmetry.md`, `fivefold-sheets-golden-ratio.md`, `brings-q-hyperbolic-geometry.md`, `orbital-fourier-decomposition.md`, `orbital-space-normal-bundle.md` — geometry of the genus-4 surface / its S₅ action.
- `lean/QOU/Archimedean/EmCouplingBringZeroMode.lean:206` `bringTilingEuler_eq : bringTilingEuler = -6` — a tiling Euler characteristic, **(b)**, computed from the Bring tiling combinatorics rather than from χ(A).
- `observations/w-boson-mass-discrepancy.lean:68` `chi_bring_val : chi_bring = -6 := rfl` — a `def` literal consumed numerically.

**Upshot for §5–6: every downstream *computation* found consumes the integer g = 4 (or the tiling/ramification combinatorics), not the trace. χ = −6 functions as a label on g = 4, plus one genuine use as a divisibility modulus (`n | χ(A)` in the Kummer-level obstruction, `skein-resolution-obstruction.md:17`, `ClassicalLimitObstruction.lean:77`) — and *that* use is the one that treats an HH²-class as an integer.**

## 7. What the files say about the framing question (survey verdicts, not assessment)

1. **The scalar collapse happens in the prose, and it is named.** `introduction/chapter-overview.md:30` *"reduce the whole obstruction to a single scalar $\chi(A) = 2-2g$"*; `skein-resolution-obstruction.md:11` *"A single integer $\chi(A) = -6$"*; `qou-p-neq-np.md:43` *"the scalar class $\chi(A) \in HH^2$"*. The step that turns the class into a number is the **"trace map"** `H^2(\mathcal{S},\mathcal{B}) \to R` (`quantum-characteristic-classes-su2.md:10`, `quantum-characteristic-classes.lean:13`, `motivic-perpetual-obstruction.md:11`) — an ungraded map to a ring, with **no Lean carrier and no construction anywhere**. `qou-obstruction-millennium-specializations.md:8` already retracts the one inference that was drawn from `dim HH² = 1`.
2. **No ch(A), no HH_0, no Chern character, no Todd class, no Hirzebruch–Riemann–Roch exists in the corpus.** `HH^•` cohomology appears in 75 files; `HH_0` homology in none. Riemann–Roch appears in 10 files, always as `χ(V) = d + r(1−g)` for `(r,d) = (2,0)` — no higher components. The nearest characteristic-class register is `substrate-line-bundle-base-not-fibre.md:7` (`c_1(Ad(A))`, `c_2(Ad(A))`), never assembled.
3. **The one place that does work at graded level is `brings_euler_characteristic.lean`**, which computes `Σ(−1)^i dim_q H^i` — i.e. treats −6 as the degree-alternating sum, not a bare dim_q — and admits at `:63–68` that the naive dim_q of $\mathcal{O}_q(SU(2))$ **diverges**. `notation-collisions.md:21` independently concludes *"the $-6$ needs the Euler-characteristic-of-a-complex sense — an alternating sum"*. **The corpus has already located the answer in two places; what it has not done is propagate it into the .md blocks, or reconcile it with the 2026-09-15 ruling that tr(id_A) = dim_q(A).**
4. **Genuinely ambiguous sites** (they say "trace" without fixing the object): `why-b3.md:1`, `descartes-knot-eigenbasis-derivation.md:2`, `brings-is-qou.lean:25`, `qu-to-qou.lean:43`, `quantum-characteristic-classes.lean:57`, `descartes.lean:25` — all write `χ(A) = tr(id_A)` in a docstring or a one-clause hypothesis with no evaluation and no category named.
5. **Untouched by the 2026-09-15 pass** (no authorNote, still asserting the pre-ruling reading): `brings-surface/universality-general.md` (indexes moduli by `χ(\mathcal{S})`), `braids-and-knots/skein-resolution-obstruction.md` ("a single integer"), `brings-surface/archimedean-condition.md` (the K₀-rank sentence), `brings-surface/torus-knot-generators.md` ("entirely determined by χ"), `introduction/chapter-overview.md:30` ("a single scalar"), and the `descartes_trace` axiom in `vertex-algebra-relations.lean`.
