# Survey: HH / HKR / ch / K_0 / FM–Orlov / S¹ / DG–Čech–de Rham sites in the corpus (2026-09-15)

**Purpose.** Input to the analysis in [`2026-09-15-chi-as-a-component-of-the-chern-character.md`](2026-09-15-chi-as-a-component-of-the-chern-character.md) (issue #7425, session milestone `qou-dgce`). Produced by a read-only survey agent this session and transcribed here unchanged apart from this preface and the removal of the agent's note that it could not write the file; paths were spot-checked by the session before commit. Read it as a **measurement of the corpus on `main` at `0509e4010`** (and, where stated, of the #7420 head `607d3874a`), not as an assessment — the assessment is in the analysis doc.

---

## 0. Method — exact greps and counts

Surface A: `content/` over `*.ts *.md *.lean`, `/.lake/` excluded (3 740 `.ts`, ~3 700 `.md`, 2 908 `.lean` under `content/quantum-observable-universe/lean/QOU/`).
Surface B: `library/INDEX.md` (700 lines / ~700 doc dirs), `library/*/sections/*.md`, `library/*/ocr/*.txt`.
Surface C: `docs/audits/` (2 639 entries), `docs/coordination/`, `.beans/`.

| pattern (`grep -rniE`, content/) | hits |
|---|---|
| `Hochschild` | 140 |
| `HH\^` | 65 · `HH\^2` 30 · `HH_1` 15 |
| `HH_0\|HH₀\|HH_\{0\}\|HH\^0\|HH⁰` | 31 |
| `HH_\*` / `HH\*` | 0 / 0 |
| `cyclic homology` | 1 |
| `Hochschild[-–—]+Kostant[-–—]+Rosenberg` | 11 (in 10 files) |
| `\bHKR\b` | 56 (many are unrelated Lean identifiers in `SchurWeyl/TableauCells.lean`, `Mathlib/Roth*.lean`, `Knot/Kashaev*.lean`) |
| `Chern character` | **1** |
| `Chern class` 32 · `c_1` 131 · `c_2` 289 | |
| `Todd` | 9 (all Michael J. Todd, SDP) · `Todd class` **0** |
| `Riemann[-–—]+Roch` | 19 · `Hirzebruch` **0** |
| `\bMukai\b\|Fourier[-–— ]+Mukai` | **0** |
| `Orlov\|Bondal\|C[aă]ld[aă]r[aă]ru` | **0** |
| `Willerton\|Vezzosi\|Hoyois\|Scherotzke\|Sibilla` | **0** each |
| `Ben.Zvi` | 6 (all `content/schema/references.ts`) |
| `Van den Bergh` | 19 · `Calabi.?Yau` 13 |
| `K_0` 24 · `K\^0` 5 · `Grothendieck group` 1 · `Grothendieck` 43 · `K-theory` 40 |
| `distinguished triangle\|exact triangle\|triangulated categor` | **2** (both in `references.ts`) · `triangulated` 6 · `D\^b` **0** · `pretriangulated` **0** |
| `derived categor` | 8 · `dg.categor\|DG categor` **0** · `A_\\infty` 14 (all are the direct-limit algebra $A_\infty$, unrelated to $A_\infty$-algebras) |
| `integral transform` 4 · `exact equivalence` **0** · `representability` 24 |
| `S\^1` 73 · `S¹` 25 · `circle action` **0** · `loop space` **1** · `free loop space` **0** · `S\^1.equivariant` **0** · `mixed complex` **0** · `Connes` 63 (all Connes *distance*/spectral triple) |
| `Yekutieli` **1 051** · `non.abelian Stokes` 86 · `gerbe` 125 · `Cech\|Čech` 87 · `Čech[-–—]de Rham` **0** · `cosimplicial` 158 · `crossed groupoid` 43 · `twisted deformation` 17 · `Maurer.Cartan\|MC element` 5 · `descent data` 5 |
| `base manifold` 29 · `smooth manifold` 8 · `algebraic variety` 3 · `complex manifold` 1 · `scheme` 91 · `M_0` 50 · `varTheta` 261 · `archimedean tuple` 3 |
| `1409.1198` (whole repo, incl. `.bib/.tex/.json`) | **0** |
| `2106.07444` (whole repo) | **1** |

Surface C counts: `S^1` audits 13 / beans 21 / coordination 2; `S¹` 81 / 3 / 7; `circle action` 1 / 1 / 0; `loop space` 0 / 0 / 0; `mixed complex` 0 / 0 / 0.

---

## 1. Hochschild homology / cohomology, Van den Bergh, Calabi–Yau

### The defining block
**`content/quantum-observable-universe/stochastic-mechanics/classical-limit-obstruction.{ts,md}`** — `definition`, `def:classical-limit-obstruction`, chapter `stochastic-mechanics` (Ch 19). **This is the corpus's only content block that defines anything Hochschild.** It defines *one group* by fiat, not the theory:
> `classical-limit-obstruction.md:3-9`: "The **classical limit obstruction** of the quantum universe is the Hochschild cohomology group $$\mathrm{Obs}(\mathbf{C}, q \to 1) := HH^2(\mathcal{U}_q(\mathfrak{g}), \mathrm{Ad})$$"

**Status: DEFINED (narrowly).** `HH^2(\mathcal{U}_q,\mathrm{Ad})` is named and given a role; the Hochschild complex, $HH^*$, $HH_*$, the bar resolution and the cup/Gerstenhaber product are nowhere constructed. Lean sibling `lean/QOU/ClassicalLimitObstruction.lean` — **0 sorry**, but it carries dimensions as `ℕ` class fields, not cohomology.

### Blocks that ASSUME it
- **`stochastic-mechanics/qou-obstruction-reduction.{ts,md}`** + `-proof.md` — `theorem`, `thm:qou-obstruction-reduction` — asserts $\dim_k HH^2 = 1$. **ASSUMED from the axioms** in the strongest sense in the corpus. Decisive lines:
  > `qou-obstruction-reduction-proof.md:3-9`: "**Step 1: Observability kills $HH^0$.** The QOU axiom $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ … is the statement $$HH^0(\mathcal{U}_q, \mathrm{Ad}) = \mathrm{Ad}^G = 0.$$"
  > `:14-30`: "**Step 2: Frobenius duality relates $HH^0$ and $HH^d$.** The Frobenius--Hopf self-duality $A \cong A^\vee$ … induces a Poincaré duality on Hochschild cohomology \cite{yekutieli2010}: $$HH^n \cong HH^{d-n\vee}, \qquad d = \dim G.$$ This is the Van den Bergh duality for Frobenius algebras: the dualizing bimodule is trivialized by the Frobenius form $\lambda : A \to \mathbf{1}$."
  > `:46-47`: "Therefore $HH^2 \cong k$: the obstruction space is one-dimensional. $\square$"
  Lean `lean/QOU/AlgebraicSubstrate/qou_obstruction_reduction.lean` — **6 sorry**; `vdb_duality` and `drinfeld_rigidity` are explicitly labelled `INPUT`:
  > `:57-60`: "/-- INPUT — **Van den Bergh / Calabi–Yau duality of dimension 3** for `U_q(su₂)`: `HH^i(U_q,Ad) ≅ HH_{3-i}(U_q,Ad)`, hence equal dimension. (A literature theorem; the class instance is the §3b-cond conditional hypothesis.) -/"
- **`stochastic-mechanics/classical-limit-obstruction-properties.{ts,md}`** — `remark`, `rem:classical-limit-obstruction-properties` — the only place the corpus gives the deformation-theoretic *meaning*. **ASSUMED.**
  > `:11`: "**Control of the classical limit by $HH^2$.** … the first-order deformation $\phi_1$ is a Hochschild 2-cocycle. The second-order term $\phi_2$ exists iff $[\phi_1] \cup [\phi_1] = 0$ in $HH^3$. The total obstruction … $\mathrm{obs}_\infty = \sum_{n \geq 1} (q-1)^n [\phi_n] \in HH^2(\mathrm{Ad})[[q-1]]$."
- **`information-theory/qou-p-neq-np.md`** — `conjecture`, `conj:qou-p-neq-np`. **ASSUMED, and here the corpus states exactly what the axioms are taken to imply** — this is the single best sentence for the "what do the axioms imply" pass:
  > `:33`: "Two of its three legs come from the axioms: the observability axiom kills $HH^0$, and the Frobenius--Hopf self-duality induces the Yekutieli--Van den Bergh Poincaré duality on Hochschild cohomology so that $HH^2 \cong (HH^1)^\vee \cong k$"
- **`stochastic-mechanics/qou-obstruction-millennium-specializations.md`** — `remark` — a *correction* block that narrows the claim. **MENTIONED + correction.**
  > `:8`: "**Proportionality is conjectural, not a consequence of one-dimensionality.** … One-dimensionality is a property of $HH^2 \cong k$, the *source* … It does not make the three images proportional *to each other*"
- **`braids-and-knots/skein-resolution-obstruction.md:1`** — `definition`, `def:skein-resolution-obstruction` — "a fourth evaluation of the universal obstruction class $\chi(A) \in HH^2 \cong k$." **ASSUMED.**
- **`mass-theory/spectral-sequence-collapse.{ts,md}`** — `proposition`, `prop:spectral-sequence-collapse`. The corpus's *positive* Hochschild claim. **ASSUMED, and the block itself flags the gap:**
  > `.md:1`: "*For semisimple $A = H_n(R, q)$, Hochschild cohomology vanishes in positive degrees $\mathrm{HH}^k(A,\, A) = 0$.*"
  > `.ts:16-27` authorNote: "**The Lean does not prove this block's statement.** … What is missing is a Lean *statement*, and two things block writing one — Mathlib has no Hochschild-cohomology framework, and there is no defined filtration to collapse"
- **`mass-endomorphism/gb-spectral-sequence-interpretation.md:31`** — `remark` — "$HH^2$ controls deformations, $HH^3$ controls obstructions." **MENTIONED.**
- **`mass-theory/terms-2-6-higher-operations.ts:15`** + `-table1-data.md:3-4` — records a **CLOSED** route: "$HH^1(H_3(R, q)) = 0$ at generic $q$"; "$HH^2(\mathbb{R}[S_3]) = 0$ by Burghelea's theorem". **MENTIONED (negative result).**
- **`quantum-observable-universes/rigid-dualizing-complex.{ts,md}`** (`definition`, `def:rigid-dualizing-complex`) and **`rigid-dualizing-brings.{ts,md}`** (`example`, `ex:rigid-dualizing-brings`) — the corpus's Van den Bergh duality statement in `Ext`/`Tor` form. **DEFINED (the rigid dualizing complex) / ASSUMED (the duality).**
  > `rigid-dualizing-complex.md:5`: "3. **Van den Bergh duality:** For any finitely generated $A$-bimodule $M$, the rigid dualizing complex induces a duality $\mathrm{Ext}^i_A(M, \omega_A^\bullet) \cong H^{d-i}(M)^\vee$"
- `q-geometric-langlands/q-flat-connection.{md,ts}` (`definition`), `q-gl-obstruction-calc.{md,ts}` (`proposition`), `q-flat-connection-remark.md` (`remark`) — all identify the $q$-curvature with $HH^2$ **via HKR**; see §2.
- `lifting-and-descent/hochschild-kummer-connection.{ts,md}` — `remark`, `rem:hochschild-kummer-connection`; `lifting-and-descent/motivic-galois-character.md`; `lifting-and-descent/motivic-perpetual-obstruction.md`. **ASSUMED.**

### Lean library
| file | sorry | note |
|---|---|---|
| `lean/QOU/Information/CocenterTraceFactor.lean` | 7 | **The only place in the repo where $HH_0$ is DEFINED.** `:57`: "/-- The **cocenter** `HH₀(A) = A / [A,A]` — the target of every trace functional. -/" and `:6` "the trace factors through `HH₀ = A/[A,A]`". |
| `lean/QOU/Information/HochschildH1.lean` | 8 | **The only place $HH^1$ is DEFINED.** `:16`: "`HH1 R A := Der(A) ⧸ Inn(A)` — the first Hochschild cohomology, as an `R`-module." Header claims "All sorry-free" — **that claim is false, the file has 8 `sorry`.** |
| `lean/QOU/Information/OuterDerivationResidue.lean` | 4 | P-vs-NP residue as a class in `HH₀`/`HH₁`. |
| `lean/QOU/Information/ChiMinusSix.lean` | 3 | `QOUCohomology` class encodes the assumption as ranks. **Contains a mathematical slip:** `:44` "duality collapses `HH²(A) ≅ (HH⁰)^∨ ≅ k`, so `HH²` is rank one" — with `observability : hh0 = 0` (`:51`) this would give `HH² = 0`, contradicting `hh2 = 1`. The `.md` has it right (`HH² ≅ (HH¹)^∨`). Worth a fix. `chi_eq_neg_six` and `chi_ne_zero` themselves are sorry-free but conditional on `[QOUObstruction]`. |
| `lean/QOU/AlgebraicSubstrate/qou_obstruction_reduction.lean` | 6 | See above; also carries the K₀→HH₀ trace and "Chern character" fields (§3, §4). |
| `lean/QOU/AlgebraicSubstrate/obstruction_residual_gap.lean` | 1 | `:112` "/-- Van den Bergh / Calabi–Yau duality in dimension 3. -/"; `:106` "/-- `dim_k HH_i(U_q, Ad)`. -/" |
| `lean/QOU/Hecke/H2KaehlerDegrees.lean` | **0** | The corpus's one genuinely proved Hochschild-adjacent result; see §2. |
| `lean/QOU/BraidKnot/MassGapObstruction.lean`, `.../GBSpectralSequence.lean`, `lean/QOU/QGeometricLanglands.lean` (1 sorry), `lean/QOU/q_gl_obstruction_calc.lean` (7 sorry) | | consumers |

### Verdict
- $HH^2$ **has** a defining content block (`def:classical-limit-obstruction`), but only as one group of one algebra.
- $HH_*$ / $HH^*$ as graded theories, $HH_0$, $HH_1$, **cyclic homology $HC$** — **NO defining content block.** `cyclic homology` appears exactly once in all of `content/`, in a Lean docstring (`lean/QOU/Hecke/H2KaehlerDegrees.lean:27`, a Loday citation).
- **Van den Bergh duality**: stated in `def:rigid-dualizing-complex` and `ex:rigid-dualizing-brings`; used as an axiom-level input everywhere else. Never proved. The Lean marks it `INPUT`.
- **Calabi–Yau**: `models-of-qous/calabi-yau.ts` is `ex:calabi-yau` = "Real hypersurface in a Calabi--Yau $2$-fold" (`index-of-definitions/definition-index.md:1303`) — a *geometric* CY, **unrelated to CY algebras**. "Calabi–Yau algebra" in the Ginzburg sense: **not found on the surface searched** (`content/**/*.{ts,md,lean}`); it appears only inside Lean docstrings as a synonym for Van den Bergh duality.

---

## 2. The HKR theorem

**HKR is invoked 11 times by name, in 10 files, and is never stated.** No content block defines it, states its hypotheses, or names its conclusion $HH_n(X) \cong \bigoplus_i H^i(X, \Omega^{i+n})$. The affine form $HH_*(A) \cong \Omega^*_A$ appears only in degree one, and only in a Lean docstring.

Invocations, all **ASSUMED** (used as a black-box isomorphism):
- **`quantum-universes/poisson-hkr-connection.{ts,md}`** — `remark`, `rem:poisson-hkr-connection`, title "HKR and skew-Poisson integration", `interprets: "def:poisson-object"`, chapter `quantum-universes`. **The closest thing to an HKR block, and it states only degree 2 for a bimodule:**
  > `.md:3-12`: "**From Hochschild to bivectors.** The first-order deformation $\phi_1 \in HH^2(\mathcal{U}_q, \mathrm{Ad})$ … maps under the Hochschild--Kostant--Rosenberg isomorphism to a bivector field: $$\mathrm{HKR} \colon HH^2(A, A) \xrightarrow{\sim} \Gamma\!\bigl(\Lambda^2 T_A\bigr) = \mathrm{Hom}_{\mathbf{C}}\!\bigl(\mathbf{1}, \Lambda^2(\Omega^1(A)^{\vee})\bigr).$$"
  > `.md:16`: "**Internal vs. external.** The classical approach defines the Poisson bracket by passing through $\tau$ to the vector-space level and invoking HKR. The internal definition avoids this detour."
- **`q-geometric-langlands/q-gl-obstruction-calc-proof.md:2`** — "The Hochschild--Kostant--Rosenberg comparison identifies this space with $HH^2(\mathcal{U}_q, \mathrm{Ad})$. The image under $\mathrm{HKR}$ is the gerbe-theoretic obstruction class $\kappa_0 = e(\xi)$."
- **`q-geometric-langlands/q-flat-connection-remark.md:3`** — same identification; `:11-14` "obstruction $HH^2$ and the gerbe class in … $HH^2$ measuring $n$-divisibility of the $q$-curvature."
- **`stochastic-mechanics/qou-obstruction-reduction-proof.md:50`** — "The HKR comparison map sends the generator of $HH^2$ to the Euler class $\kappa_0 = e(\xi) \in H^2(\mathcal{S}, \mathcal{B})$, whose trace is $\chi(A)$." **This is the load-bearing use: HKR is what carries the $\chi(A)$ value into $HH^2$.**
- **`lifting-and-descent/hochschild-kummer-connection.md:9`** — "The HKR comparison bridges the gerbe (geometric) and Hochschild (deformation) realizations of this single motivic class."
- Also: `quantum-universes/qu-structures-intro.md`, `quantum-universes/outro-quantum-universes.md`, `q-geometric-langlands/q-flat-connection.md`, `lifting-and-descent/motivic-perpetual-obstruction.md`, `predicted-spectra/yekutieli-transcendence-shadow.md`.

### Is it ever stated as an assumption or hypothesis class? — Yes, once, in Lean, and honestly.
**`lean/QOU/Hecke/H2KaehlerDegrees.lean` — 0 sorry.** This is the only place in the corpus where HKR is declared a *cited hypothesis* with a named scope:
> `:24-27`: "the first Hochschild homology is the module of Kähler differentials, `HH_1(A_h/R) ≅ Ω¹_{A_h/R}` (Hochschild–Kostant–Rosenberg degree one; for a commutative algebra this is the elementary identification `HH_1 = Ω¹`, Weibel … Prop. 9.4.3 / Loday *Cyclic Homology* 1.1.10)"
> `:33-34`: "**Those two identifications are cited, not proved here** — Mathlib's `KaehlerDifferential` API for a quotient of a polynomial ring was not exercised in this session, and no Hochschild framework exists."
> `:53-55` "## What this does NOT claim * Nothing about `n ≥ 3` (`H_n` is non-commutative there; `HH_1 ≠ Ω¹` and the corpus has no instance)."
What it *does* prove sorry-free: `kaehlerIdeal_eq_top_of_isUnit` (the semisimple fibre has no $HH_1$ when $[2]_q^2$ is a unit) and `kaehlerIdeal_ne_top_of_hom` ($HH_1(H_2/\mathbb{Z}[q^{\pm1}]) \neq 0$ at $q = i$). **This is the corpus's only PROVED HKR-adjacent statement, and it is at $n=2$ only.**

Restated in `docs/audits/2026-09-05-binding-gap-groupoids-derived-categories-full-tower.md:817`: "**Cited, not proved:** `HH_1(A/R) ≅ Ω¹_{A/R}` for commutative `A` (HKR in degree one; Weibel 9.4.3)".

### Verdict
**No content block defines or states HKR.** It is invoked as a named isomorphism in 5 content blocks and is the bridge on which `thm:qou-obstruction-reduction` part (b) rests. Nothing in Lean states the general theorem; `H2KaehlerDegrees.lean` states degree one for one commutative algebra and marks it cited.

---

## 3. Chern character, Chern classes, Todd, HRR, Mukai

### `ch(F)` / "Chern character as a trace" / "generalized trace into $HH_0$"
**Not found on the surface searched** (`content/**/*.{ts,md,lean}` and `docs/audits/`, `.beans/`) as a *mathematical object*. `Chern character` has exactly **one** hit in the whole of `content/`, and it is a Lean class-field docstring:
> `lean/QOU/AlgebraicSubstrate/qou_obstruction_reduction.lean:84`: "/-- Chern character map property identifying the trace image of the HH² generator with χ(A) via trace pairing -/  chern_character : phi_1_image = trace_pairing chi_A"
**Status: ASSUMED** (a class field, i.e. a hypothesis; 6 sorry in file). Its companion field is the one place the $K_0 \to HH_0$ trace exists anywhere in the corpus:
> `:78`: "/-- Structural trace evaluation map from algebraic K-theory K₀(A) to Hochschild homology HH₀(A) -/  trace_pairing : ℤ → ℝ"
> `:80`: "/-- Hattori-Stallings trace property relating the primitive Kummer obstruction κ₀ to the Euler characteristic χ(A) -/"
> `:115` comment: "-- Ref: [yekutieli2010] Van den Bergh duality for Hochschild (co)homology; Euler/trace class computation"
> `:112-118` docstring: "This is the explicit Connes / Hattori–Stallings pairing computation … which is NOT derivable from the two structural inputs (`vdb_duality`, `drinfeld_rigidity`) and is left as the honest domain gap."

**This is precisely the finding the owner ask (`qou-dgce`) anticipated:** the corpus already has $\chi(A)$ sitting at the end of a $K_0 \to HH_0$ trace map named `chern_character`, with no block anywhere explaining what a Chern character is, and with the Hattori–Stallings step flagged as a gap. **$ch(A) \in HH_0$ is nowhere constructed; only its value on one class is hypothesised.**

### Chern *classes* — these the corpus does have, as an axiom
**`quantum-observable-universes/quantum-observable-universe.md:6`** — the QOU axiom itself:
> "4. *(Measurability)* The categorical Chern classes of the adjoint object vanish: $c_1(\mathrm{Ad}(A)) = 0$ and $c_2(\mathrm{Ad}(A)) = 0$."
- **`quantum-observable-universes/qou-exists-axiom-3.{ts,md}`** — `lemma`, `lem:qou-exists-axiom-3`, "Axiom 3 — vanishing categorical Chern classes for the adjoint bundle", Ch 2, Lean `qou:QOU.QuantumObservableUniverse.exists_axiom_3_chern`. **ASSUMED under a structural hypothesis:** `.md:3` "Under the structural hypothesis that the classical principal bundle $P$ satisfies $c_1(\mathrm{Ad}(P)) = c_2(\mathrm{Ad}(P)) = 0$, the corresponding categorical Chern classes … must also vanish". `qou-exists-axiom-3-proof.md:2`: "Categorical Chern classes are defined via $\tau$" — **the nearest the corpus comes to defining a categorical characteristic class, in one clause of a proof.**
- `quantum-observable-universes/qou-axioms-physical-reading.md:11` (physical reading: "Vanishing Chern classes are an anomaly-freedom condition… Together these satisfy the hypotheses of the non-abelian Stokes theorem"), `q-geometric-langlands/geometric-rh-exposition.md:21`, `climax-volume-mass/vertex-algebra-relations.md:267-281` (QUO-3a/3b translation), `quantum-observable-universes/categorical-instanton-unique{-proof}.{md,lean}` ($c_2$ classifies instantons), `lifting-and-descent/quantum-characteristic-classes-su2.md:5`, `yekutieli-lifting-condition-su2.md:13` ($\kappa(L) = c_1(L)$).
- `lifting-and-descent/hochschild-kummer-connection.md:9` — "projects at each finite place $p$ to a motivic Chern class $\rho_p(\kappa) \in H^1_{\mathrm{Gal}}(\ldots)$". **ASSUMED.**

### Riemann–Roch — used, classical, degree-1 only
Not Hirzebruch–RR (`Hirzebruch` = 0 hits). It is the classical curve RR, used to convert $\chi = -6$ into $g = 4$:
- **`brings-surface/genus-maximal-descent.{ts,md}`** + `-proof.md` — `proposition`, `prop:genus-maximal-descent`, Ch 6. **ASSUMED (RR cited, conclusion derived):**
  > `genus-maximal-descent-proof.md:2`: "By Riemann--Roch on the compact Riemann surface $M_0$: $\chi(V) = \deg(V) + \mathrm{rank}(V)(1-g) = 2(1-g)$. Setting $2(1-g) = -6$ gives $g = 4$."
  Lean `lean/QOU/Archimedean/genus_maximal_descent.lean:24` "/-- Riemann–Roch on the descent curve `M₀`: `χ = 2(1 − g)` … -/" — carried as an **explicit hypothesis**, `:16` "Riemann–Roch identity itself, carried as an explicit hypothesis on the".
- `brings-surface/chi-minus-six-chain.md:7` (`example`, `ex:chi-minus-six-derivation`) "**Step 3: Apply Riemann--Roch.**"; `brings-surface/brings-surface-example.md:17`; `lean/QOU/BringsSurface/BranchPointSixNotForced.lean:54`; `lean/QOU/Information/ChiMinusSix.lean:67,78`; `q-geometric-langlands/hasse-weil-bound-proof.md:100` (function-field RR).

### Absent
**Todd class, Hirzebruch–Riemann–Roch, Mukai vector, Mukai pairing, Cǎldǎraru, Cǎldǎraru–Willerton, Toën–Vezzosi, Hoyois–Scherotzke–Sibilla — none found on the surface searched** (`content/**/*.{ts,md,lean}`; `Todd` hits are all Michael J. Todd's SDP text). Ben-Zvi–Nadler *Nonlinear Traces* (arXiv:1305.7175) **is registered** in `content/schema/references.ts:1786-1806` with `stage: "candidates"` and the note "Traces and dimensions of dualizable objects in higher algebra identified with derived loop spaces / fixed-point loci in correspondence categories; nonlinear GRR, Atiyah–Bott–Lefschetz" — and is **cited by zero content blocks** (grep of `content/**/*.ts` for `ben-zvi-nadler2013-nonlinear-traces` returns only the `references.ts` definition). Same for `ben-zvi-nadler2009-character-theory` (arXiv:0904.1247).

### Verdict
**No content block defines the Chern character.** Chern *classes* are an axiom of the theory and are used without a definition (`qou-exists-axiom-3-proof.md:2` "defined via $\tau$" is the whole of it). This is the largest single exposition gap in the list.

---

## 4. K-theory: $K_0$, Grothendieck group, $\chi: K_0 \to \mathbb{Z}$

### $K_0$ of the QOU category — used exactly once, in the definition of the Descartes condition
> **`brings-surface/archimedean-condition.md:7`** (`definition`, `def:archimedean-condition`, title "Descartes condition", Ch 6, Lean `qou:QOU.ArchimedeanCondition`, `validation: "not_checked"`): "The class $[A] \in K_0(\mathbf{C})$ has rank $-6$."

**Status: ASSUMED.** $K_0(\mathbf{C})$ is never defined; "rank" of a class in it is never defined; and the relation between "rank $-6$" and $\chi(A) = \mathrm{tr}(\mathrm{id}_A) = -6$ is never stated. This is the corpus's only $K_0$-of-a-category usage and it is load-bearing for the whole Descartes chain.

### $K_0(\mathrm{Var}_k)$ — this one *is* defined
> **`lifting-and-descent/motivic-substrate.md:11`** (`definition`, `def:motivic-substrate`, Ch 4): "1. the **Grothendieck ring of varieties** $K_0(\mathrm{Var}_k)$ over the base field $k$. It is the free abelian group on isomorphism classes $[X]$ of $k$-varieties modulo the scissor relations $[X] = [Z] + [X \setminus Z]$ for closed $Z \subseteq X$, with product $[X] \cdot [Y] = [X \times_k Y]$."
> `:15`: "The motivic substrate is taken axiomatically: the ring $K_0(\mathrm{Var}_k)$, the Lefschetz class $\mathbb{L}$, the localization $\widehat{\mathcal{M}}$, and the realization functors are posited as given data"

**Status: DEFINED** (and declared axiomatic). Also `mass-theory/motivic-mass-measure.{md,lean}:2`; Lean `lean/QOU/MotivesArchimedean.lean:39` "/-- Abstract Grothendieck ring of varieties `K_0(Var_k)`."

### $\chi$ as a functional out of $K_0$
- `mass-theory/archimedean-realization-functor.md:9-14` (`definition`) — "$\widehat{\mathcal{M}} \otimes_{K_0(\mathrm{Var})} \mathbb{Z}$", "sending the motivic class $[X]$ to its topological Euler characteristic $\chi_{\mathrm{top}}(X)$".
- `mass-theory/archimedean-realization-functor-interpretation.md:5` (`remark`) — "$\chi_{\mathrm{top}} \colon K_0(\mathrm{Var}) \to \mathbb{Z}$ is a *ring homomorphism* — a **motivic measure** in the sense of Denef–Loeser". **DEFINED for $K_0(\mathrm{Var})$.**
- `lean/QOU/AlgebraicSubstrate/qou_obstruction_reduction.lean:78` — the $K_0(A) \to HH_0(A)$ trace, see §3. **ASSUMED.**
- `prop:euler-char-stability` (`lifting-and-descent/euler-char-stability-C.md`, Lean `qou:QOU.Torsion.euler_char_constant`) — $\chi(A_n)$ constant along the tower.

### Absent
`\chi(\mathcal{F})` and `[\mathcal{F}]` for a *sheaf/perfect complex*, and $K^0(X)$ as topological K-theory: **not found on the surface searched.** All 5 `K^0` hits are the neutral kaon $K^0$ (`eightfold-way/meson-octet-decomposition.md:31` etc.). `Grothendieck group` has 1 hit and it is not a definition (`mass-theory/gb-residue-spectral-sum.md:22`, "an identity in the Grothendieck group of the filtered algebra").

### Verdict
**$K_0(\mathrm{Var}_k)$ has a defining content block. $K_0(\mathbf{C})$ / $K_0(A)$ — NO defining content block**, despite being the source of `def:archimedean-condition`'s "rank $-6$" and of the Lean `trace_pairing`. No block states $\chi: K_0 \to \mathbb{Z}$ for the QOU category.

---

## 5. Triangulated / derived categories, DG categories, $A_\infty$

**Essentially absent. The corpus uses $D(A^e)$ as a place for objects to live and never introduces triangulated structure.**

- `distinguished triangle`, `exact triangle`, `pretriangulated`, `cone` (in the mapping-cone sense), `D^b(X)`, `dg category`, `dg-enhancement`, `A_∞-algebra`: **none found on the surface searched** (`content/**/*.{ts,md,lean}`). The 2 hits for `triangulated categor` are both bibliography (`content/schema/references.ts:15415,15419`, Bridgeland 2007 "Stability conditions on triangulated categories" — registered, **cited by zero content blocks**). The other 4 `triangulated` hits mean *ideally triangulated 3-manifolds* (`mass-theory/stokes-dt-bps-bridge.md:24`, `hyperbolic-knot-shape-fields.md:21`, `lean/QOU/Brings/HeckeMapFaceSize.lean:10,114`). The 532 hits for `cone` are light cones, Bring cones, knot cones. The 14 `A_\infty` hits are all the *direct-limit algebra* $A_\infty = \varinjlim A_n$ (`lifting-and-descent/direct-limit-algebra-su2.md`, `def:direct-limit-algebra`) — a genuine notation collision with $A_\infty$-algebras that no block flags.

- `derived category` — 8 hits, all "where $\omega_A^\bullet$ lives", never a definition:
  > **`quantum-observable-universes/rigid-dualizing-complex.md:1`** (`definition`, `def:rigid-dualizing-complex`, Ch 2): "Let $A$ be the Frobenius--Hopf substrate algebra and let $D(A)$ denote its derived category of bimodules." **ASSUMED** — $D(A)$ introduced by fiat in the first clause of the definition it is needed for.
  > `rigid-dualizing-brings.md:16`: "The rigid dualizing complex must satisfy $\omega_A^\bullet \simeq R\mathrm{Hom}_{A^e}(A, A^e)$ in $D(A^e)$."
  > `mass-theory/geom-yekutieli-alignment.md:48` and `lean/QOU/BraidKnot/geom_yekutieli_alignment.lean:154`: "in the derived category $D(A^e)$."
  > `brings-surface/local-cohomology-group.md:1`: "the derived category framework generalizes the commutative concept of principal parts supported at the singularity." **MENTIONED.**
  > `quantum-observable-universes/substrate-self-duality.lean:8`: "a quasi-isomorphism `A ≃ ω_A•` in the derived category."
  > `mass-theory/q-beta-categorical-precision-ladder-context.md:151`: "Kashiwara mixing has no derived categorical proof yet." **CONJECTURED/open.**

- The only sustained *discussion* of the derived route is an audit, not content: **`docs/audits/2026-09-05-binding-gap-groupoids-derived-categories-full-tower.md`** (1 394 lines). It contains the corpus's only prose on $HH_0$ as a universal object:
  > `:195-197`: "`HH_0(A) = A/[A,A]` is the universal receiver of traces; for a semisimple `A` it is spanned by the primitive central idempotents, i.e. by `{e_λ}` — which is exactly why the corpus's every trace is `Σ_λ y_λ χ_λ`. The higher `HH_k(A)` of a semisimple algebra vanish."
  > `:248`: "this is the informal statement that `tr_M` is `HH_0` of a simplicial object; the derived route is literally 'take its higher homology'"
  > `:738`: "A referee at a mathematics venue will accept 'the Markov trace is `HH_0`; …"
  This audit mentions `Fourier`/`Orlov`/`Bondal`/`triangle` **zero times**.

### Verdict
**NO defining content block for triangulated categories, distinguished triangles, derived categories, DG categories, or $A_\infty$.** $D(A)$/$D(A^e)$ are used in three definitions/examples without introduction. The $A_\infty$ notation collision is unflagged.

---

## 6. Fourier–Mukai, Orlov, Bondal, exact equivalence

**Not found on the surface searched.** Zero hits for `Fourier-Mukai` (any dash), `Mukai`, `Orlov`, `Bondal`, `exact equivalence` across `content/**/*.{ts,md,lean}` — and zero in `docs/audits/` and `.beans/`. No kernel, no integral-transform-as-functor, no representability theorem.

Closest surviving material:
- `integral transform` — 4 hits, all analytic (Fourier/Laplace transforms), not $\Phi_K$.
- `representability` — 24 hits; **all are `q-geometric-langlands` Langlands-side or SDP-side**, none is Orlov representability.
- The corpus's own "these two categories are the same" statements are **Tannakian, not derived**: `quantum-observable-universes/tannaka-krein-reconstruction.md:1` "This provides the monoidal equivalence $\mathbf{C} \simeq \mathrm{Rep}(H)$"; `quantum-universes/tannaka-krein-overview.md:4` "**Equivalence.** The functor $\tau$ establishes a monoidal equivalence $\mathbf{C} \simeq \mathrm{Rep}(G)$"; `q-geometric-langlands/tannaka-krein-isomorphism.md:7` "an equivalence of categories lying over the fibre functor $\tau$"; `q-geometric-langlands/q-gl-conjecture.md:35` "equivalence of categories."

### Verdict
**NO content block mentions, let alone defines, the Fourier–Mukai transform or Orlov/Bondal–Orlov.** Complete absence; the notion has no foothold in the corpus at all.

---

## 7. $S^1$-action, loop space, Connes $B$, mixed complex, cyclic

**The $S^1$/cyclic side is the emptiest topic after FM–Orlov, but unlike FM–Orlov it has a *recorded owner-gated open question*.**

- `circle action`, `free loop space`, `S^1-equivariant`, `mixed complex`, Connes' operator $B$, $\mathcal{L}X$: **none found on the surface searched** (`content/**/*.{ts,md,lean}`). `loop space` has exactly 1 hit in `content/` and it is not a free loop space.
- All 98 `S^1`/`S¹` hits in `content/` are geometric circles: knot embeddings $\varrho: S^1 \to \mathcal{S}$ (`brings-surface/orbital-fourier-decomposition.md:1`, `fluid-dynamics/geodesic-vortices.md:4`, `berry-vortex-moduli.md:7`, `observations/trefoil-vortex-chirality-flip.md:27`), the Hopf fibration $S^1 \hookrightarrow S^3_q \to S^2$ (`information-theory/phase-transition-boundary.md:3`, `quantum-volume-interpretation.md:7`), Möbius-energy domains $S^1 \times S^1$ (`climax-volume-mass/mobius-energy-proof.md:19`), the U(1) phase circle (`quantum-observable-universes/u1-equivariant-reduction-proof.md:8-19`), roots of unity on $S^1$, and electron-shell labels like `1s^1`.
- All 63 `Connes` hits are the **Connes distance / spectral triple**, not cyclic homology: `information-theory/connes-distance-not-reeb-step-count.{ts,md}` (`remark`, `rem:connes-distance-not-reeb-step-count`), `prop:gram-degeneracy-blocks-connes`, `cor:finite-connes-forces-trivial-kernel`. Also `lean/QOU/AlgebraicSubstrate/qou_obstruction_reduction.lean:112` "the explicit Connes / Hattori–Stallings pairing computation" — Connes' *pairing*, in a `sorry`-bearing gap note.

### The recorded open question (beans + audits)
There **is** an owner-gated $S^1$-equivariant item, and it is about a geometric realisation of the Markov weights, not about cyclic homology:
- **`docs/audits/2026-08-21-webster-williamson-molien-lead-for-equivariant-index.md`** — "**Status:** LEAD — nothing derived, nothing wired. Four open verification items below." Decisive:
  > "The corpus carries an owner-gated open item: an **S¹-equivariant (Reeb-graded) index reproducing the partition weights geometrically, with a conjugation symmetry coming from a Hodge-★ / Poincaré duality**. That is a description of a geometrically-constructed trace on the Hecke algebra whose character expansion is graded."
  Source: `library/arxiv-0911.4494v2` (Webster–Williamson, *The geometry of Markov traces*), bib id `webster-williamson-2014-markov`.
- **`.beans/qou-sf1t--qplancherel-constructed-partition-function-total-m.md:65`** — "library/arxiv-0911.4494v2 (Webster-Williamson, "The geometry of Markov traces") constructs a geometrically-defined trace whose character expansion is given by MOLIEN SERIES via B_Δ-equivariant intersection cohomology -- the shape of the owner-gated S^1-equivariant-index item. Needs a lead doc, with the Tr_Γ vs Jones-Ocneanu identification flagged as OPEN verification".
- `docs/audits/scripts/keystone_wlambda_Z_defect_n_scaling.py:177` and `keystone_wlambda_C_n_closed_form.py:192` — "falsifiable target -- any S^1-equivariant index realizing W_lambda".
- `docs/audits/2026-08-01-ksel1-singularity-selection.md:79` — "**Free transitive circle action.** The class map $u \mapsto …" (the only "circle action" in `docs/`; a singularity-selection argument, not a cyclic structure).
- **`.beans/qou-siin--pull-through-solleveld-affine-hecke-hh-is-nonzero.md`** — the corpus's most careful Hochschild bean. Records that `library/arxiv-1108.5286v3` (Solleveld) is registered as `solleveld2022` and "**cited by zero content blocks**"; that its §3.1 gives `HH_*(H ⊗ Γ) ≅ ⊕_w Ω^*(t_{ρ_w})^{G_{ρ_w}}` "by Morita invariance + Hochschild-Kostant-Rosenberg"; and, on the homology/cohomology bridge:
  > "## Gate (iii) CHECKED — not closed, and it SPLITS the lead (2026-08-25) … Read §3, §3.1, §3.3 for a bridge between homology and cohomology. **There is none.** `HH^` never appears; no duality or Poincare statement anywhere; the sole "cohomology" occurrence is about CYCLIC homology of smooth commutative algebras. … **The cohomological statement is not a transport — it is a separate piece of work.**"
  This matters for §1: it says the corpus's $HH^{\ge1} = 0$ claim and the Van den Bergh transport are scope-bounded to the *finite* Hecke algebra.

### Verdict
**NO content block defines an $S^1$-action, a loop space, the Connes operator $B$, a mixed complex, or cyclic homology.** The one open $S^1$ question in the corpus (audits + bean `qou-sf1t`) is an *equivariant index for the Markov weights*, deliberately gated, with a named library source and four unverified items — not an $S^1$-action on Hochschild chains.

---

## 8. Non-abelian Stokes / Yekutieli / gerbes / Čech / MC elements / crossed groupoids

**This is the topic the corpus is richest in — 1 051 `Yekutieli` hits — and it is the one place the corpus explicitly places the QOU inside a named external framework. It spells out the cosimplicial / crossed-groupoid / Čech machinery in substance; it does NOT spell out the DG-category or Čech–de Rham side.**

### Where the QOU is explicitly placed in Yekutieli's setting
- **`lifting-and-descent/yekutieli-lifting-intro.md:1`** — the placement sentence: "We measure this obstruction, identify it as a quantum characteristic class, and use it to upgrade a quantum universe to a quantum observable universe. **We use Yekutieli's framework for central extensions of gerbes.**"
- **`lifting-and-descent/cosimplicial-intro.md:1`** — "The recursive brane tower carries a higher-categorical structure organising the transitions between levels into a cosimplicial crossed groupoid. **Yekutieli's framework for central extensions of gerbes \cite{yekutieli2010} supplies exactly the triples $(x, g, a)$ required to define the face and degeneracy maps.**"
- **`lifting-and-descent/yekutieli-mapping-table.{ts,md}`** — `prose`, `sec:yekutieli-mapping-table`, `cites: ["yekutieli2008","yekutieli2009","yekutieli2010","yekutieli2015","yekutieli2015-twisted-dq"]`, Ch 4. **This is the single most important block for topic 8: a 12-row concept-by-concept dictionary.** Verbatim rows:
  > `:14-18` "Recursive Brane Tower $\{\mathcal{S}_n\}$ … & Central extension of gerbes $\mathfrak{G}_{n+1} \to \mathfrak{G}_n$ & \cite[Thm.~3.13, \S6]{yekutieli2010}"
  > `:19-22` "Quantum Characteristic Classes $\kappa_n \in H^2(M, \mathcal{O}_M^{\times})$ … & Obstruction classes for lifting objects in central extensions & \cite[\S4, Def.~4.15]{yekutieli2010}"
  > `:35-38` "Vacuum State $\tau$ … & Unique MC element in the pronilpotent DG Lie algebra & \cite{yekutieli2009}"
  > `:39-41` "Mass Identity … & Nonabelian multiplicative integral; 2D nonabelian Stokes theorem & \cite[Ch.~5--6]{yekutieli2015}"
  > `:42-45` "Substrate field $q(p)$ … & Local twisted deformation parameter; MC element varying over $M$ & \cite{yekutieli2008, yekutieli2009}"
  > `:56-59` "Cosimplicial crossed groupoid … & Cosimplicial object in crossed groupoids; \v{C}ech nerve of a gerbe & \cite[\S1--2]{yekutieli2010}"
  > `:60-63` "Twisted $2$-cocycle $d(g_{ijk}) = a \cdot g \cdot a^{-1}$ … & Twisted \v{C}ech cocycle in $H^2(M, \mathcal{O}_M^\times)$ & \cite[Def.~4.15, Thm.~4.17]{yekutieli2010}"
  **Status: ASSUMED throughout — every row is a citation, not a derivation.** `yekutieli-lifting-proof.md:32`: "**Conclusion.** Theorem 4.17 of yekutieli2010 applies with".

### The machinery that IS spelled out
- **`lifting-and-descent/cosimplicial-crossed-groupoid.{ts,md}`** — `proposition`, `prop:cosimplicial-crossed-groupoid`, tags `["cosimplicial","crossed-groupoid","gerbe","yekutieli"]`, Lean `qou:QOU.LiftingDescent.cosimplicial_crossed_groupoid_exists`, `validation: "not_checked"`. **DEFINED/PROVED-conditionally:** `.md:7-9` "from the simplex category $\Delta$ to the $2$-category of gerbes on $M$ extends to a *cosimplicial crossed groupoid*… 1. The coface maps $\delta^i \colon \mathfrak{G}_{n} \to \mathfrak{G}_{n+1}$ are given by jet prolongation acting on objects (inserting the $i$-th face in the Čech nerve)."
- **`lifting-and-descent/ccg-cosimplicial-identities.{md,lean}`** — `definition`, `def:ccg-cosimplicial-identities`, Ch 4. `.md:1`: "*The coface maps $\delta^i$ (composites of jet prolongation with Čech face maps) and codegeneracy maps $\sigma^j$ (composites of :refterm[descent]{#descent} with Čech degeneracy maps) satisfy the cosimplicial identities:*" **DEFINED.**
- **`lifting-and-descent/descent-cocycle-deviation.{ts,md}`** — `lemma`, `lem:descent-cocycle-deviation`, "Cocycle deviation at level $n+1$ as a twisted Čech 2-cocycle", tags include `cech-cohomology`. **PROVED-conditionally** (`-proof.md:22-30`, ends `$\square$`).
- **`lifting-and-descent/descent-condition.md:11`** — the explicit cocycle: "$g_{ijk}^{(n)} = g_{ij}^{(n)} \cdot g_{jk}^{(n)} \cdot (g_{ik}^{(n)})^{-1}$ is the Čech $1$-cocycle deviation at level $n$".
- `lifting-and-descent/yekutieli-lifting-condition.md:14`, `quantum-characteristic-classes-unique{-proof}.md`, `quantum-characteristic-classes-exists-proof.md:13`, `weak-equiv-invariance.ts`, `def:yekutieli-triple`, `prop:yekutieli-lifting`, `prop:blowup-yekutieli`, `climax-volume-mass/vertex-algebra-relations.md:608-610` ("### C-10: \v{C}ech--Yekutieli descent cocycle"), `vertex-algebra-jet-relations.md:354` ("### JC-8: \v{C}ech cocycle at level $n$"), `lean/QOU/LiftingDescent/ccg_cosimplicial_identities.lean:42-57`, `lean/QOU/Torsion/DescentCondition.lean:37`.
- Non-abelian Stokes (86 hits) is load-bearing for the mass identity and for the Chern-class axiom: `quantum-observable-universes/qou-axioms-physical-reading.md:11` "Together these satisfy the hypotheses of the non-abelian Stokes theorem, which is what makes the integral well defined"; `q-geometric-langlands/geometric-rh-exposition.md:21` "The nonabelian Stokes theorem dictates that if the curvature $F_\nabla$ … were nonzero, different triangulations of a bounding surface would yield different path-ordered products."

### What is only cited, never spelled out
- **Čech–de Rham: `Čech[-–—]de Rham` returns 0 across `content/`, `docs/audits/`, `.beans/`.** The bicomplex is nowhere. **Not found on the surface searched.**
- **DG categories / DG Lie algebra machinery:** `dg categor` = 0 hits. `MC element` appears in exactly 2 places, both single table rows (`yekutieli-mapping-table.md:37,44`); the pronilpotent DG Lie algebra, its gauge group, and the MC equation are never set up. `mass-theory/archimedean-functor-uniqueness.md:24` says only "the cosimplicial / Yekutieli triple machinery".
- **Twisted deformation quantization:** 17 hits, all citational.
- **Rigid dualizing complexes:** substantive (`def:rigid-dualizing-complex`, `ex:rigid-dualizing-brings`, `conj:geom-yekutieli-alignment`), but the derived-category ambient is assumed (§5).

### Verdict
The corpus **does** have defining blocks for the cosimplicial crossed groupoid, the Čech cocycle deviation, the cosimplicial identities, and the Yekutieli triple, plus a full concept dictionary in `sec:yekutieli-mapping-table`. It has **NO block** for Čech–de Rham, for the DG-category/DG-Lie side, or for MC elements beyond two table cells.

---

## 9. The base manifold $M$ / $M_0$

**Yes — there is a block asserting the classical-analogue base is an ordinary smooth manifold, and it asserts it rather than deriving it.**

> **`content/quantum-observable-universe/models-of-qous/spatial-realization-functor.{ts,md}`** — `definition`, `def:spatial-realization-functor`, title "Spatial realization functor", tags `["spectrum","functor","contact-geometry"]`, Lean `qou:QOU.SpatialRealizationFunctor`, `validation: "not_checked"`, chapter `models-of-qous`.
> `.md:1-6`: "Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe. The **spatial realization** of $A$ is the space $$M = \mathrm{Spec}(A) = \{ p \colon \mathbf{1} \to A \mid p \text{ is a categorical point} \}.$$"
> **`.md:8` — the decisive line:** "This functor realises the algebra $A$ as a contact manifold. It sends the Frobenius form to the global contact $1$-form and the torus generator to the Reeb field. **The target $M$ is an ordinary smooth manifold—the classical space whose function algebra $C^\infty(M)$ the fibre functor $\tau$ recovers from $A$.**"
> `.md:18`: "2. **Kähler differentials.** The module $\Omega^1(A)$ of Kähler differentials **exists in $\mathbf{C}$ by hypothesis.** Under the fibre functor, $\tau(\Omega^1(A))$ maps to sections of the cotangent bundle $\Gamma(T^* M)$."
> `.md:43`: "Non-degeneracy of $\int_A$ guarantees that $d\varTheta$ is maximally non-degenerate on $\ker\varTheta$, which defines a contact manifold."

**Status: ASSUMED.** $M$ being a smooth manifold is asserted in the definition (no smoothness/Hausdorff/second-countability argument, no representability of $\mathrm{Spec}$), and $\Omega^1(A)$ is admitted "by hypothesis". This is the corpus's answer to "under the axioms the classical-analogue base behaves like a smooth manifold", and it is a definition, not a remark or example.

The **algebraic-variety** side is separate and about the *fibre*, not the base:
> `brings-surface/brings-smoothness.md:1`: "Bring's surface $\mathcal{S}$ … is a *smooth* algebraic variety. The three power-sum constraints intersect transversely in $\mathbb{P}^4$, ensuring no singular points exist." **PROVED (transversality argument given).**
> `brings-surface/brings-surface-def.md:1`: "**Bring's surface** is the algebraic variety" — `definition`, `def:brings-surface`. **DEFINED.**

The **archimedean tuple** $(\mathbf{C}, \varTheta, G, \mathcal{S})$:
> `introduction/chapter-overview.md:10`: "The QOU manifests as the archimedean tuple"
> `brings-surface/approach-to-exceptional-divisor.md:3`: "In the QOU archimedean tuple $(\mathbf{C}, \varTheta, G, \mathcal{S})$, the base manifold $M$ carries the smooth metric in which two free vortices propagate. … **"Below Planck scale" in QOU is a categorical statement, not a metric one.** The relevant geometry switches from the base $M$ to the fibre $\mathcal{S}_p$"
> `models-of-qous/p-adic-realisation.md:1`: "we realise the archimedean tuple over a $p$-adic base" — the block that shows the tuple is *not* tied to an archimedean base field. **DEFINED/EXEMPLIFIED.**

$M_0$ specifically:
> `brings-surface/genus-maximal-descent.md:3`: "the categorical Euler characteristic $\mathrm{tr}(\mathrm{id}_A) = -6$ determines the topological type of the base curve. Under the fibre functor $\tau$ of any archimedean realisation, **Riemann--Roch on $M_0$ forces $2(1 - g) = -6$, hence $g = 4$.**"
> `lifting-and-descent/euler-char-stability-C.md:9`: "**the base manifold $M_0$ remains invariant under jet prolongation.** Therefore, $\chi(M_0)$ persists unaltered at every level."
> `lifting-and-descent/descent-reduction-zero.md:1`: "When $\dim M_k = 0$, the base manifold is a discrete set of points".
> `notation/notation-collisions.md:35` — register ruling: "plain $M$ is the **(deprecated)** base manifold and appears as $\chi_{\mathrm{eu}}(M)$". **Note for the exposition pass: $M$ as base manifold is marked deprecated in the notation register.**

`complex manifold` has 1 hit and it is in a `references.ts` note, not content. `scheme` (91 hits) is never used of the QOU base.

### Verdict
**Yes, `def:spatial-realization-functor` is the block, and `.md:8` is the quote.** It is a *definition asserting* smooth-manifold behaviour, not a remark/example deriving it from the axioms — so it is exactly the place a "what the axioms are assumed to imply" statement should attach.

---

## 10. The two arXiv papers

Surfaces searched: `library/INDEX.md`, all `library/*/structure.json`, all of `library/`, `content/schema/references.ts`, `content/bib-qa-verifications.json`, `references.bib`, `main.tex`, and then the **whole repo excluding `.git`**.

### `1409.1198` — **NOT held and NOT cited. Zero hits anywhere in the repository.**
`grep -rn "1409\.1198" .` (all files, `.git` excluded) returns nothing. Not in `library/INDEX.md`, not in any `library/*/structure.json`, not in `content/schema/references.ts`, not in `content/bib-qa-verifications.json`, not in `references.bib`. **Not found on the surface searched.** I could not infer its title from the corpus, since no trace of it exists; the owner will need to supply the title.

### `2106.07444` — **NOT held and NOT cited. One incidental hit, inside someone else's bibliography.**
> `library/arxiv-2303.08330v2/sections/sec-010-the-colored-jones-polynomial-of-a-cable-knot.md:236`: "[24] Trinh M., From the Hecke Category to the Unipotent Locus , arXiv:2106.07444."

So the title is **Minh-Tâm Quang Trinh, "From the Hecke Category to the Unipotent Locus"**, and the corpus knows of it *only* because it appears as reference [24] in the ingested colored-Jones-of-a-cable-knot paper `arxiv-2303.08330v2`. There is **no `library/arxiv-2106.07444*` directory**, no `INDEX.md` row, and no `references.ts` entry. Given the corpus's heavy Hecke-category/Markov-trace/Molien investment (§7), this is a plausible acquisition target, but as of today: **not held, not cited.**

---

## Library holdings that are on-point (Surface B)

Doc-ids with `library/INDEX.md` titles. "cited?" = whether any `content/**/*.ts` block lists the bib id in `cites`.

### Hochschild / cyclic / HKR
| doc-id | title (INDEX.md) | note |
|---|---|---|
| `arxiv-1108.5286v3` | *Hochschild homology of affine Hecke algebras* (Solleveld) | bib `solleveld2022`; **cited by zero content blocks** — see bean `qou-siin`, which read §3/§3.1/§3.3 and found no HH↔HH^ bridge |
| `arxiv-0707.2003v2` | *A geometric model for Hochschild homology of Soergel bimodules* (Webster–Williamson) | `references.ts:1452` "HH_* of Soergel bimodules as equivariant intersection homology of B×B-orbit closures" |
| `arxiv-math-0510265v3` | *Triply-graded link homology and Hochschild homology of Soergel bimodules* (Khovanov) | `references.ts:1430` "the Markov trace is its Euler characteristic" — **directly on-point for §3/§4** |
| `arxiv-1011.6483v3` | *Derived Higher Hochschild Homology, Topological Chiral Homology and Factorization Algebras* | `references.ts:1497` "the bridge between the categorified-trace and factorization-homology routes"; also matches HKR + Chern character + cyclic homology + Hirzebruch greps |
| `arxiv-1202.5547v1` | *Markov property and Khovanov-Rozansky homology: Coxeter Case* (Lasy) | |
| `generalised-markov-traces-and-jucys-murphy-element` | (Hochschild cohomology hit) | |
| `centsim` | Geck–Rouquier, *Centers and simple modules for Iwahori–Hecke algebras* | per the 2026-09-05 audit: "**98 % of its text is in `ocr/` only**; a `sections/` grep cannot see it | the centre = `HH_0`" |
| HKR-by-name also in: | `arxiv-0801.3233v4`, `arxiv-1006.1099v3`, `arxiv-1304.3481v1`, `arxiv-1305.7175v4` | |
| cyclic homology in: | `arxiv-0811.2435v1`, `arxiv-0904.1247v3`, `arxiv-1011.0679v2`, `arxiv-1011.6483v3`, `arxiv-1108.5286v3`, `arxiv-1305.7175v4`, `arxiv-1412.4229v4`, `arxiv-2607.03827v1`, `arxiv-math-0510265v3` | |

### Chern character / traces / Mukai / HRR
| doc-id | title | note |
|---|---|---|
| **`arxiv-1305.7175v4`** | ***Nonlinear Traces*** **(Ben-Zvi–Nadler)** | **the single most on-point holding for topic 3.** `references.ts:1786` id `ben-zvi-nadler2013-nonlinear-traces`, `stage: "candidates"`, 37 pp / 18 sections, note: "Traces and dimensions of dualizable objects in higher algebra identified with derived loop spaces / fixed-point loci in correspondence categories; nonlinear GRR, Atiyah–Bott–Lefschetz." Hits **every** grep: HKR, Fourier–Mukai, Chern character, cyclic homology, dg category, Mukai pairing, Hirzebruch, Hochschild cohomology. **Cited by zero content blocks.** |
| `arxiv-0904.1247v3` | *The Character Theory of a Complex Group* (Ben-Zvi–Nadler) | id `ben-zvi-nadler2009-character-theory`; hits Orlov, cyclic homology, dg category, Hochschild cohomology, Bondal. **Cited by zero content blocks.** |
| `arxiv-1504.07260v3` | (Mukai vector/pairing hit) | |
| `arxiv-0707.3682v2` | *On the p-adic Beilinson conjecture for number fields* | higher K-groups; Chern character |
| `arxiv-0811.2435v1` | Kontsevich–Soibelman, *Stability structures, motivic Donaldson-Thomas invariants and cluster transformations* | hits Van den Bergh, **Calabi–Yau algebra**, cyclic homology, dg category, Bondal, Grothendieck group |
| `acsv231201` | (only `Todd class` hit in the entire library) | |
| `arxiv-1611.03697v5`, `arxiv-2406.05311v1`, `arxiv-2507.12454v1`, `arxiv-hep-th-0206161v1`, `arxiv-0707.3682v2`, `arxiv-0811.2435v1` | further Chern-character holdings | |

### Derived / triangulated / DG / Fourier–Mukai / Orlov
| doc-id | title | note |
|---|---|---|
| **`arxiv-1610.09640v4`** | ***Derived Categories*** **(Yekutieli, 459 pp book)** | `references.ts:1931`: "459-page foundational text: derived categories, DG modules, dualizing complexes (commutative and noncommutative), perfect and tilting DG bimodules." Hits Fourier–Mukai, Orlov, Bondal, distinguished triangle, dg category, Van den Bergh, Calabi–Yau algebra. **The obvious source for topics 5 and 6, and it is already held and already registered.** |
| `arxiv-1312.6411v4` | *Duality and Tilting for Commutative DG Rings* (Yekutieli) | id `yekutieli2013-duality-tilting-dg`; hits distinguished triangle, dg category, Van den Bergh, Bondal, Hochschild cohomology |
| `arxiv-1109.3255v2` | *Floer cohomology in the mirror of the projective (plane)* | Fourier–Mukai, Orlov, dg category |
| `arxiv-1006.1099v3` | *Floer cohomology and pencils of quadrics* (Smith) | Orlov, HKR, Bondal, dg category, Hirzebruch, Hochschild cohomology |
| `disssubmission` | *Tannakian categories of perverse sheaves on abelian varieties* | Fourier–Mukai, distinguished triangle, Hirzebruch — **and Tannakian, i.e. the corpus's own idiom** |
| `arxiv-1901.08945v2` | *Decompositions of derived categories of gerbes* | Orlov + gerbes — sits exactly at the §5/§8 junction |
| `arxiv-1608.03227v4`, `arxiv-1608.07308v1` | Gorsky–Negut-type braid/flag-Hilbert-scheme categorifications | Orlov, Bondal, dg category, Grothendieck group, Hirzebruch |
| `arxiv-1112.0030v2` | *Homological algebra of knots and BPS states* | Orlov |
| `ant-v14-n7-s{,-p05}`, `arxiv-1010.4386v5`, `arxiv-1601.02479v5`, `arxiv-1606.01832v3`, `arxiv-2002.04901v5`, `arxiv-math-0409593v1` | distinguished-triangle holdings | |

### Yekutieli / gerbes / MC / cosimplicial (topic 8 — already well mined)
`arxiv-0801.0083v4` *Central Extensions of Gerbes*; `arxiv-0905.0488v5` *Twisted Deformation Quantization of Algebraic Varieties*; `arxiv-0801.3233v4` same, survey; `arxiv-1109.1919v3` *Combinatorial Descent Data for Gerbes* ("descent data in cosimplicial crossed groupoids", `references.ts:1369` cites Thm 0.1/2.4); `arxiv-1103.1035v4` *MC Elements in Pronilpotent DG Lie Algebras*; `arxiv-1412.4229v4` *The Squaring Operation for Commutative DG Rings* (`references.ts:1844` "making Van den Bergh rigidity definable"); `arxiv-2102.00255v1` *Rigidity, Residues and Duality*; `arxiv-1103.4815v3` *Four Equivalent Versions of Non-Abelian Gerbes* ("ˇCech cocycles, classifying maps, bundle gerbes, and principal…"); `arxiv-0808.1923v3` *Connections on Non-Abelian Gerbes and their Holonomy*; `arxiv-math-0505170v2` *An Averaging Process for Unipotent Group Actions*; `arxiv-1606.01832v3` *Flatness and Completion Revisited*.

### $S^1$-equivariant index (topic 7)
`arxiv-0911.4494v2` — *The geometry of Markov traces* (Webster–Williamson), bib `webster-williamson-2014-markov`. "We give a geometric interpretation of the Jones-Ocneanu trace on the Hecke algebra, using the equivariant cohomology of sheaves". The named source of the owner-gated $S^1$-equivariant-index item; lead doc `docs/audits/2026-08-21-webster-williamson-molien-lead-for-equivariant-index.md`, four open verification items.

---

## Gaps — notions with NO defining content block

Ordered by how load-bearing the undefined notion already is.

1. **Chern character $ch$, and the generalized trace $K_0 \to HH_0$.** No block. Yet `lean/QOU/AlgebraicSubstrate/qou_obstruction_reduction.lean:78,84` already carries `trace_pairing : ℤ → ℝ` documented as "Structural trace evaluation map from algebraic K-theory K₀(A) to Hochschild homology HH₀(A)" and `chern_character : phi_1_image = trace_pairing chi_A`, with `:112-118` conceding the Hattori–Stallings step "is NOT derivable from the two structural inputs … and is left as the honest domain gap". **The owner's hypothesis in `qou-dgce` — that $\chi(A)=-6$ is one component of $ch(A) \in HH_0$ with a vanishing implicitly assumed — is consistent with everything found: the corpus writes $\chi(A)$ as a scalar and nowhere says what the other components of $ch$ are or that they vanish.**
2. **$HH_*$ and $HH^*$ as graded theories; $HH_0$; $HH_1$; cyclic homology $HC$; the Connes operator $B$; mixed complexes.** $HH_0$ and $HH_1$ are defined only in Lean (`CocenterTraceFactor.lean:57`, `HochschildH1.lean:16`), both files `sorry`-bearing, neither with a content sibling. `cyclic homology` appears once in all of `content/`, in a citation.
3. **HKR.** Invoked by name in 5 content blocks, load-bearing for `thm:qou-obstruction-reduction`(b), never stated. Degree-1 affine case cited (not proved) in one sorry-free Lean file at $n=2$ only.
4. **Fourier–Mukai transform, kernels, Orlov / Bondal–Orlov representability.** Complete absence: **zero hits** in `content/`, `docs/audits/`, `.beans/`. The corpus's only "same category" statements are Tannakian.
5. **Triangulated categories, distinguished triangles, cones, $D^b(X)$, DG categories, dg-enhancements, $A_\infty$-algebras.** No block. Yet `def:rigid-dualizing-complex` opens with "let $D(A)$ denote its derived category of bimodules". Also: the corpus's $A_\infty$ = direct-limit algebra collides with $A_\infty$-algebras and no block flags it (the notation register `notation/notation-collisions.md` covers $\mathbb{M}$, $\mathcal{M}$, $M$, $HH^2$ but not $A_\infty$).
6. **$S^1$-actions, circle actions, free loop spaces, $S^1$-equivariance, $\mathcal{L}X$.** No block. The one live $S^1$ question is owner-gated and about an equivariant index for Markov weights (bean `qou-sf1t`, audit 2026-08-21), not about a circle action on Hochschild chains.
7. **Čech–de Rham bicomplex.** Zero hits anywhere. The Čech side alone is well developed (`lem:descent-cocycle-deviation`, `def:ccg-cosimplicial-identities`); the de Rham pairing with it is absent.
8. **The DG-Lie / MC-element side of Yekutieli.** `MC element` exists only as two cells of `yekutieli-mapping-table.md` (`:37`, `:44`); the pronilpotent DG Lie algebra, its gauge action, and the MC equation are never set up, though `arxiv-1103.1035v4` is held and registered.
9. **Todd class, Hirzebruch–Riemann–Roch, Mukai vector, Mukai pairing.** Zero hits. (Classical curve RR *is* used and is carried as an explicit Lean hypothesis.)
10. **$K_0(\mathbf{C})$ / $K_0(A)$ and $\chi: K_0 \to \mathbb{Z}$ for the QOU category.** No block, although `def:archimedean-condition` (the Descartes condition, Ch 6) turns on "The class $[A] \in K_0(\mathbf{C})$ has rank $-6$" (`brings-surface/archimedean-condition.md:7`). $K_0(\mathrm{Var}_k)$, by contrast, **is** properly defined in `def:motivic-substrate`.
11. **Calabi–Yau *algebra*** (Ginzburg sense). `ex:calabi-yau` is a geometric CY 2-fold; "Calabi–Yau duality" appears only inside Lean docstrings as a synonym for Van den Bergh duality.
12. **Categorical Chern classes.** $c_1, c_2$ are a QOU *axiom* (`quantum-observable-universe.md:6`) but the only definitional text is the half-sentence `qou-exists-axiom-3-proof.md:2`: "Categorical Chern classes are defined via $\tau$".

### Two defects found in passing (not gaps — errors)
- **`lean/QOU/Information/ChiMinusSix.lean:44`** states "duality collapses `HH²(A) ≅ (HH⁰)^∨ ≅ k`, so `HH²` is rank one", but the same class asserts `observability : hh0 = 0` (`:51`) — as written this gives `HH² = 0`, contradicting `frobeniusHopf_duality : hh2 = 1` (`:55`). The `.md` chain has it right: `HH² ≅ (HH¹)^∨` (`information-theory/qou-p-neq-np.md:33`, `qou-obstruction-reduction-proof.md:37`). A docstring-level slip in the file that carries `chi_eq_neg_six`.
- **`lean/QOU/Information/HochschildH1.lean:21`** header claims "All sorry-free, generic `{R : CommRing} {A : Ring} [Algebra R A]`", but the file contains **8 `sorry`**.

### Where an exposition arc has the least to fight
Topics 1 (Hochschild), 2 (HKR), 3 (ch), 4 ($K_0$) all converge on one already-written object: `chern_character : phi_1_image = trace_pairing chi_A` in `qou_obstruction_reduction.lean`. A block defining $ch: K_0(\mathbf{C}) \to HH_0$, one defining $HH_*$/$HH^*$, one stating HKR with hypotheses, and one connecting `[A] ∈ K_0(\mathbf{C})` (`archimedean-condition.md:7`) to `tr(id_A) = -6` would retire gaps 1–4 and 10 together and give `def:archimedean-condition` the foundation it currently assumes. `library/arxiv-1305.7175v4` (*Nonlinear Traces*) and `library/arxiv-1610.09640v4` (Yekutieli, *Derived Categories*) are already held and registered and cover topics 3, 5, and 6 between them; neither is cited by any content block yet.
