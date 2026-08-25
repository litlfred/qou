# Nguyen–Tran strong-AJ (4₁) → Lean brick decomposition — NT-T1 workplan

Bean `qou-a9xy` (epic `qou-iiz4`), branch `claude/qlift-borel-kernel-derivation-2026-07-20`.
Source read in full: `library/arxiv-2006.02042v1/2006.02042v1.pdf` (11 pp; text extracted via pdfminer —
the PDF was absent from the worktree at session start and arXiv is proxy-blocked in
this sandbox; it was checked out from `origin/main` mid-session and then read directly).

## 0. Scope verification

**Title (verbatim): "THE STRONG AJ CONJECTURE FOR THE FIGURE EIGHT KNOT",
Hoang-An Nguyen and Anh T. Tran** (Acta Math. Vietnamica 46 (2021), corpus key
`nguyen-tran-2021`). The scope **is exactly 4₁** — no adjustment needed. (The
"cables of torus knots" title guess in the task belongs to Tran's earlier
[Tr4] = arXiv:1404.0331, cited by this paper for its transfer Lemmas 3.1–3.3.)

## 1. Exact statements proved (theorem numbers from the PDF)

- **Conjecture 1 (AJ, Garoufalidis).** ε(α_K) = A_K(M,L) up to an M-only polynomial
  factor, where ε reduces t = −1 and α_K generates the localized recurrence ideal
  Ã_K = T̃·A_K. Quantum torus T := R⟨L^±1,M^±1⟩/(LM − t²ML), R = C[t^±1];
  A_K := {P ∈ T | P·J_K = 0} (left ideal; nonzero by [GL] = `garoufalidis-le-2005`).
- **Conjecture 2 (Strong AJ, Sikora [Si]).** √(ε(A^σ_K)) = p, where σ(M^kL^l) =
  M^−kL^−l, A^σ_K is the σ-invariant part of A_K (ideal of T^σ), and the A-ideal
  p := ker(θ : t^σ → C[χ(π₁X)]) with p = (A_K·t)^σ [FGL].
- **Theorem 1.** The strong AJ conjecture holds for the figure eight knot E = 4₁.
- **Lemma 2.1.** If ∃ P ∈ R[M^±1,L^±1] with P·J_K ∈ R[M^±1], σ(P) = P, and
  ε(P) = M^k L^l (A′_K)^{2m}, then p_K ⊂ √(ε(A^σ_K)). Proof leans on **[Tr4,
  Lemmas 3.1–3.3]** (cited, not re-proved).
- **Lemma 2.2.** Explicit L^{±1}, L^{±2} action on the Charles–Marché basis ⟨1⟩, ⟨x⟩
  mod C[t,M], from [CM, Prop 4.5]; J_E = ⟨1⟩ with
  ⟨Q⟩(n) = [n]·Σ_{k=0}^{n−1} Q(t,t^{2n},t^{4k})·∏_{l=1}^k (t^{4n}+t^{−4n}−t^{4l}−t^{−4l}).
- **Construction (§2.1–§2.7, eqs (2.1)–(2.14)).** P = B·α′_E with α′_E = a₁L +
  a₋₁L^−1 + a₀ the known inhomogeneous order-2 recurrence [CM, Prop 4.4];
  symmetric conditions (2.1)–(2.3), initial conditions (2.4)–(2.8) [ε(P)=(A′_E)²],
  polynomiality. Reduces to the commutative Diophantine equation **(2.13)**
  A₁p₀ + B₁p₁ = C₁ in R[M^±1] (solved by a Mathematica Gröbner basis + conversion
  matrix), then the σ-symmetry functional equation **(2.14)**
  M^14t^8 f(t,M) + M²t^8 f(t,M^−1) = (explicit RHS), solved by the palindrome-halving
  ansatz f = f(1,M) + (t²−1)h, h = t^8M^−6k. Output: explicit b₀, p₁, p₋₁, p₀ (§2.7).
- Forward inclusion √(ε(A^σ_E)) ⊂ p_E: AJ known for 4₁ [Ga] + A′_E =
  L + L^−1 − M⁴ − M^−4 + M² + M^−2 + 2 has no nontrivial M-only factors +
  [Tr4, Lemma 3.1].

**Honest mapping to what QOU needs.** The "4₁ order-2 recurrence certificate +
annihilator generation" is **already sorry-free in the corpus** and is NOT what this
paper adds: `QOU.BraidKnot.AJFigureEightAnnihilation.figureEightOperator_annihilates`
(division-free qZeilberger telescope, all q ≠ 0 incl. roots of unity) +
`AJFigureEight.StrongAJFigureEight` instance (order-2 op, nontriviality, q=1
specialization to A_{4₁}, meridian-squared convention). Conventions differ: paper
t with q ≈ t⁴, M = t^{2n}, [n]-normalized J vs corpus q, m = q^N — a translation
lemma is a brick below, not a wall. What the paper adds over the corpus Lean is the
**ideal-theoretic layer**: T, A_K, σ, localization T̃, radical, A-ideal, and the
σ-symmetric certificate P with ε(P) = (A′_E)². For the epic's real goal (reusable
q-Weyl / q-difference infra for the keystone q-lift), the payload is bricks B1–B4/B8–B9,
not the ideal equality itself.

## 2. Proof-skeleton → Lean bricks

Classes: (a) pure algebra doable now; (b) needs NT-T2 q-Weyl infra; (c) genuine
Mathlib gap; (d) honest wall (research-grade).

| # | Brick | Paper locus | Class | Notes |
|---|---|---|---|---|
| B1 | Quantum torus T as skew-Laurent ring R[M^±][L^±;σ], σ(M)=t²M | §1.1 | **(b)** — the NT-T2 core | Build on Mathlib `Algebra.SkewMonoidAlgebra` (exists: Basic/Single/Support — early-stage) with G = Multiplicative ℤ acting on R[M^±]; or hand-roll finitely-supported ℤ-indexed Laurent coeffs with twisted mul (the corpus already hand-rolls the *function model*: `QDifferenceOperator` + `Annihilates` in `AJFigureEight.lean` — B1 is the abstract-ring upgrade, only where genuinely needed) |
| B2 | Recurrence ideal A_K = left annihilator of J_K; nonzero for 4₁ | §1.1 | (b) | Nonzeroness is free from the proved corpus annihilation once translated (B12); general-knot nonzeroness [GL] stays cited |
| B3 | T̃ = Laurent L-polys over R(M); left-Euclidean division ⇒ principal left ideals | §1.2 | **(c)** | Mathlib `RingTheory.OreLocalization.*` exists (ring-level Ore localization) but NO skew polynomial / Ore-extension ring, NO noncommutative Euclidean/PID theory. Hand-build skew division by degree (analog of `Polynomial.divByMonic` with σ-twist) — hard engineering, not research |
| B4 | σ-involution on T and t; invariant subrings T^σ, t^σ | §1.3 | (a)/(b) | Pure algebra once B1 exists; on the commutative t it is doable now |
| B5 | A-ideal p: χ(π₁X), θ, p = ker θ; identification p = (A_K·t)^σ | §1.3 | **(d)** | SL₂(ℂ)-character varieties of knot groups are nowhere near Mathlib. Honest route: *define* p := ((L−1)A′_E·t)^σ on the Lean side citing [FGL], flag the geometric identification as a cited input (§3b-cond class if a provable kind needs it) |
| B6 | Forward inclusion: A′_E has no M-only factors; [Tr4, L3.1] transfer | §2 opening | (a) + (d) | The no-M-factor check is pure algebra (A′_E is monic-in-L of L-degree 1 after (L−1) split — contentless factor argument), doable now; the [Tr4] lemma itself is an un-reproved dependency |
| B7 | Lemma 2.1 (certificate ⇒ reverse inclusion), via [Tr4, L3.2/3.3] | §2, L2.1 | **(d)** | Depends on Tr4's R ∈ R[L^±] with ε(R)=(L+L^−1−2)^r construction — formalizing means importing a second paper; wall unless Tr4 is also decomposed (out of NT-T1 scope, name it in the epic) |
| B8 | The explicit certificate P: transcribe p₁, p₋₁, p₀, b₀; prove σ(P)=P and ε(P)=(A′_E)² | §2.7 | **(a)** | Mechanical `field_simp; ring` over a generic field — same technology as `figureEightOperator_specializes`. Doable NOW with zero new infra |
| B9 | P·J_E ∈ R[M^±1] (the inhomogeneous annihilation of P) | §2.8, L2.2 | (a)/(b) | Two routes: (i) redo Lemma 2.2 by extending `HabiroNewtonLadder` — the ⟨Q⟩ basis IS the corpus's Newton ladder up to [n]-normalization and q = t⁴; (ii) **cheaper**: derive P-annihilation by operator algebra from the PROVED `figureEightOperator_annihilates` (P = B·α′_E; α′_E is a T̃-unit multiple of the corpus operator — clear denominators, reuse the telescope). Route (ii) needs only B12 + fraction bookkeeping |
| B10 | Eq (2.13) verification | §2.3–2.4 | (a) | Lean does NOT need Gröbner search: the paper used Mathematica to *find* (p̃₀,p̃₁); checking A₁p̃₀+B₁p̃₁=C₁ is one `ring`. (Formalize-first: verify certificates, don't port searches. Mathlib `RingTheory.MvPolynomial.Groebner` exists — monomial-order division — if ever wanted; cross-paper link: UGB) |
| B11 | Radical ideals in t^σ | Conj. 2 | (a) | `Ideal.radical` exists (commutative — t^σ is commutative ✓, verified in `RingTheory/Ideal/Operations`) |
| B12 | Convention translation lemma: paper (t, M=t^{2n}, [n]-normalized J) ↔ corpus (q, m=q^N, `coloredJones41`) | throughout | (a) | Small but load-bearing; pin q = t⁴ and the normalization ratio once, reuse everywhere |

## 3. Mathlib gap analysis (verified against the pinned toolchain's olean tree, v4.24.0)

- **HAS**: `Mathlib.RingTheory.OreLocalization.{OreSet,Basic,Ring,NonZeroDivisors}`;
  `Mathlib.Algebra.SkewMonoidAlgebra.{Basic,Single,Support}` (early-stage);
  `Mathlib.RingTheory.MvPolynomial.Groebner`; `Ideal.radical` (commutative);
  `Mathlib.Algebra.Polynomial.Laurent`.
- **DOES NOT HAVE** (binary string-scan of every olean — decl names are stored as
  strings, so absence is strong): `Nat.qFactorial` / `qBinomial` / `gaussBinomial`
  — **the task's "Mathlib HAS Nat.qFactorial?" hint is FALSE at this pin**;
  no Ore/skew *polynomial* extension R[x;σ,δ], no skew Laurent ring, no
  noncommutative PID/Euclidean theory, no Newton polygon for q-difference
  operators, no character varieties.
- Consequence: B1 is buildable on SkewMonoidAlgebra or hand-rolled; B3 is the one
  genuine build-from-scratch (c); B5 stays a cited definition.

## 4. Ordered brick queue (NT-T2..T4)

| Tranche | Bricks (order) | Effort | Reused by |
|---|---|---|---|
| **NT-T2** (q-Weyl infra) | B12 → B1 → B4 → B2 | medium | keystone Borel-kernel module (`QOU.Mass.QDifferenceConfluentObstruction` — its order-2 kernel carrier), GGM eq-49 descendant equation (qlift-literature-check §4: same order-2 shape, `y_{m+1}−(2−q^m)y_m+y_{m−1}=0`), `phi-q-aj-machinery-identification` (its `QuantumAPolynomial` degree-placeholder gets a real backing), `ColoredJonesRecurrence`/`KnotOperatorRecurrence` (their trace recurrences become elements of A_K) |
| **NT-T3** (certificate layer) | B8 → B10 → B6(a-part) → B9 route (ii) | medium (B8/B10 are cheap; B9 is the bulk) | AJ tranche files (`AJFigureEight*`, `AJTrefoil*`); Habiro ladder consumers |
| **NT-T4** (ideal layer — gated) | B3 → B11 → B5(def) → B7 → Theorem 1 assembly | high; B7/B5 are (d) walls without a Tr4 side-tranche | RSZ classification (Ramis–Sauloy–Zhang slope/Newton-polygon work needs exactly B3's skew Laurent ring + division), any future strong-AJ statement for 𝓑₃ (currently OPEN, `phi-q-aj-machinery-identification.lean`) |

**Most reusable piece: B1** (quantum torus / skew-Laurent q-Weyl ring + σ) — five
named consumers above. **Hardest three: B3, B5, B7.** NT-T4's Theorem-1 assembly is
honest only as §3b-cond conditional on named [Tr4]/[FGL] classes until those are
formalized — per the anti-laundering rule, that conditional instance must NOT be
reported as "strong AJ proved in Lean".

## 4a. NT-T2 build status (B1, B2, B3 landed 2026-07-20)

Branch `claude/qlift-borel-kernel-derivation-2026-07-20`, bean `qou-s9ap`.

- **B1 — `QOU.Machinery.QuantumTorus` (sorry-free).** The quantum torus
  realised as the skew-Laurent ring on Mathlib `SkewMonoidAlgebra A
  (Multiplicative ℤ)`: `sigma` (σ-twist), `emb : A →+* T`, `Lgen`/`Linv` +
  `LUnit` (L a unit), the q-Weyl commutation `Lgen_mul_emb` (`L·a = σ(a)·L`)
  and `qWeyl_eigen_commutation` (`LM = c·ML`), coeff/support basics, the
  `ℕ→K` function-model operators `shiftFwd`/`mulPow` + `funcModel_qWeyl`
  (interoperates with `QOU.BraidKnot.AJFigureEight`), and the universal
  ring-hom evaluation `torusEval` (via `liftNCRingHom`). Generic
  `{A}[CommRing A]`; no ℝ (§7c).
- **B2 — degree/basis layer (sorry-free, same file).** `monomial` (`L^n·a`),
  `monomial_mul_monomial` (twisted product), `expSupport`/`coeffAt`/`topDeg`
  (top L-degree, ⊥ for 0) + `coeffAt_eq_zero_of_topDeg_lt`.
- **B3 — `QOU.Machinery.QuantumTorusDivision` (scaffold + honest wall).** The
  reduction **engine is proved sorry-free**: `reductionQuotient`,
  `reduction_leading_coeff_match` (product's `L^e` coeff = `f`'s, via
  `coeff_single_mul` + `Ring.inverse_mul_cancel` on the σ-image unit),
  `reduction_top_coeff_cancel` (one step kills the `L^e` term),
  `isUnit_smul_of_isUnit`, `coeffAt_sub`. **Honest wall (two cited
  `sorry`s, NOT vacuous):** `skew_right_division_degree_drop` (the
  `topDeg`-monotonicity calculus over `WithBot ℤ` that upgrades the proved
  top-coeff cancellation to a strict degree drop) and
  `exists_skew_right_division` (`f = q·g + r`, assembled by well-founded
  recursion on `topDeg`). Both are the **genuine v4.24.0 Mathlib gap**: no
  Ore/skew-polynomial extension, no skew-Laurent Euclidean algorithm, no
  noncommutative PID/Euclidean theory. Per the anti-laundering rule, B3 does
  **not** claim skew-Euclidean division is proved in Lean — only the reduction
  step is; the recursion assembly and the degree-calculus remain open (NT-T4
  gate, class (c)/(d)).

## 5. What is NOT claimed

- No Lean was written in NT-T1; classifications (a)–(d) are assessments, not builds.
- [Tr4, Lemmas 3.1–3.3], [CM, Props 4.4/4.5], [GL] q-holonomicity, and the [FGL]
  p = (A_K·t)^σ identification are inputs the paper cites — formalizing Theorem 1
  unconditionally requires them (B5/B7 walls name them explicitly).
- Mathlib absence claims are name-scans at the pinned toolchain, not source greps
  (source tree not present in the sandbox; oleans only).
