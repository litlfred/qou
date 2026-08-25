# q-lift literature check — Borel-kernel workplan step 1 (2026-07-20)

**Target.** q-lift the proved classical depth-2 kernel
`(n+2)·b_{n+2} = b_{n+1} + b_n` (EGF-normalized involution recurrence,
`f'(x) = (1+x)f(x)`, `QOU.Mass.QDifferenceConfluentObstruction.normalized_classical_kernel_exists`)
to a q-difference relation `[n+2]_q·b_{n+2} = b_{n+1} + c(q)·b_n` on a q-Borel
transform. Survey of the four owner-named fronts; search via WebSearch
(paper-search MCP was proxy-blocked: 403 CONNECT to api.crossref.org /
api.semanticscholar.org; arXiv MCP returned empty on all queries incl. controls).

## 1. Ramis–Zhang / RSZ q-Borel–q-Laplace summability (the analytic frame)

What exists (all verified via publisher/arXiv listings, PDFs not read except as noted):

- **Zhang 1999**, "Développements asymptotiques q-Gevrey et séries Gq-sommables",
  Ann. Inst. Fourier 49(1), 227–261 (DOI 10.5802/aif.1672). q-Gevrey order-1
  asymptotics; Gq-summability characterized by q-Borel–Laplace transforms. A power
  series solving a linear analytic q-difference equation whose Newton polygon has a
  unique slope 1 is Gq-summable of order 1.
- **Ramis–Zhang** introduced the q-Borel / q-Laplace pair (theta-kernel q-Laplace);
  see also "Sur la sommabilité des séries entières solutions formelles d'une
  équation aux q-différences, II" (C. R. Acad. Sci. / ScienceDirect S0764444298801572).
- **Marotte–Zhang 2000**, "Multisommabilité des séries entières solutions formelles
  d'une équation aux q-différences linéaire analytique", Ann. Inst. Fourier 50(6),
  1859–1890. q-analogue of Écalle–Martinet–Ramis acceleration; **every** formal power
  series solution of a linear analytic q-difference equation is Gq-multisummable.
- **Di Vizio–Zhang 2009**, "On q-summation and confluence", Ann. Inst. Fourier 59(1),
  347–392 (DOI 10.5802/aif.2433). **The confluence theorem class we need**: Borel sums
  of divergent ODE solutions are uniformly approximated on sectors by meromorphic
  solutions of q-difference deformations; compares four q-Borel sums.
- **Ramis–Sauloy–Zhang 2013**, "Local analytic classification of q-difference
  equations", Astérisque 355 (arXiv:0903.0853) — q-Stokes phenomena / local
  classification (irregular case).

**Map onto target.** This front supplies the *frame*, not the kernel: it guarantees
that if the q-deformed binding terms satisfy any linear analytic q-difference
equation (§3–§4 say the natural carrier does, order 2), then the q-Borel transform
+ Gq-(multi)summability machinery applies, and Di Vizio–Zhang-type confluence is the
right statement shape for "q-kernel → classical kernel at q→1" — i.e. for proving
the proved classical kernel is the confluent shadow of the q-lift rather than
assuming it.

## 2. q-Hermite / q-involution combinatorics (the combinatorial q-lift)

- Classical: `b_n = I(n)/n!` with I(n) the involution numbers (OEIS A000085,
  `I(n+1) = I(n) + n·I(n-1)`, EGF `e^{x+x²/2}`, = matchings of K_n, = Σ|coeffs| of
  Hermite). Our kernel is exactly this recurrence EGF-normalized.
- **Continuous q-Hermite** (Askey–Ismail; corpus keys `askey1989qhermite`,
  `ismail-masson1994`): three-term recurrence `H_{n+1}(x|q) = 2x·H_n − (1−q^n)·H_{n−1}`
  — the coefficient `(1−q^n)/(1−q) = [n]_q` is precisely the q-lift of the classical
  `n` in the involution recurrence. Second-order q-difference eigenproblem:
  Atakishiyev–Suslov 1990 (corpus `atakishiyev-suslov1990`); factorization
  arXiv:math/0602375.
- **Crossing-weighted matchings / Touchard–Riordan**: moments of continuous q-Hermite
  = matchings of [2n] weighted by q^{crossings} (Ismail–Stanton–Viennot tradition);
  generalized Touchard–Riordan formula by **Josuat-Vergès** (~2010, rook placements /
  matchings by crossings); **Cigler–Zeng**, "A curious q-analogue of Hermite
  polynomials" (arXiv:0905.0228, J. Combin. Theory A 2011).
- **Inference (not found verbatim in a single reference):** weighting involutions of
  [n] by q^{crossings} of the underlying partial matching gives q-involution numbers
  `I_q(n+1) = I_q(n) + [n]_q·I_q(n−1)`; dividing by `[n+1]_q!` yields exactly
  `[n+2]_q·b_{n+2} = b_{n+1} + b_n`, i.e. **c(q) = 1** in the naive combinatorial
  q-lift. This is a standard-technique consequence of the q-Hermite moment
  combinatorics but was NOT located as a stated theorem; treat as
  formalize-first candidate, not as literature fact.
- Ismail–Zhang, "Scaled asymptotics for q-orthogonal polynomials" (C. R. Acad. Sci.
  2006): q⁻¹-Hermite bulk asymptotics theta-function-valued — relevant later for the
  archimedean evaluation, not for the kernel.

## 3. Ohtsuki-series q-holonomy / AJ for 4₁ (the topological q-lift carrier)

- **Garoufalidis–Lê 2005** (corpus `garoufalidis-le-2005`, arXiv:math/0309214):
  colored Jones is q-holonomic — existence of the recurrence is a theorem.
- **4₁ explicitly**: the colored Jones of the figure-eight satisfies an
  **inhomogeneous q-difference recurrence of minimal order 2** (homogeneous order 3);
  stated in the Garoufalidis–Lê q-holonomy circle (verified via search snippet:
  "satisfies an inhomogeneous relation of degree 2 and does not satisfy an
  inhomogeneous relation of order less than 2"). The noncommutative A-polynomial
  Â_{4₁}(L, M, q) is explicit; AJ conjecture (Garoufalidis 2004, corpus
  `garoufalidis2004`) gives its q→1 limit as the classical A-polynomial; **strong AJ
  proved for 4₁**: Nguyen–Tran (arXiv:2006.02042, corpus `nguyen-tran-2021`).
- **Depth match**: order-2 inhomogeneous ↔ the proved classical depth-2 kernel. This
  is the natural topological home of the q-lift: the Ohtsuki/Habiro q-data of 4₁
  already satisfies an order-2 q-recurrence whose confluent limit is constrained by
  the A-polynomial.

## 4. GGM descendant q-difference equation — eq (49) VERIFIED from uploads PDF

Read directly from `library/arxiv-2012.00062v3/2012.00062v3.pdf` (pp. 14–15), Garoufalidis–Gu–Mariño,
"Peacock patterns and resurgence in complex Chern–Simons theory", arXiv:2012.00062,
Res. Math. Sci. 10 (2023) 29 (corpus `garoufalidis-gu-marino2023peacock`):

- Eq (49): `y_{m+1}(q) − (2 − q^m)·y_m(q) + y_{m−1}(q) = 0` (m ∈ ℤ) — a **linear
  order-2 q-difference equation** governing the 4₁ descendants.
- Theorem 9: fundamental solution `W_m(q)` (2×2, columns from `G⁰_m, G¹_m` q-series,
  eqs 51a/b) with `det W_m(q) = 2`, **bar symmetry** `G^j_m(q^{-1}) = (−1)^j G^j_m(q)`,
  and orthogonality/SL(2, ℤ[q^±]) pairing (eqs 52–55).
- Conjecture 10: the Stokes matrices M_R(q) in the four τ-sectors are explicit in
  `W_{−1}(q)` — this is where the SL₂ Stokes matrix `[[1,0],[−3,1]]` route
  (GGM 2021, arXiv:2007.10190, corpus `garoufalidis-gu-marino2021`) attaches.
- **Map onto target**: eq (49) has coefficients polynomial in `q^m` (q-holonomic
  normal form); the target `[n+2]_q·b_{n+2} = b_{n+1} + c(q)·b_n` is the
  `[n]_q!`-normalized (q-Borel) form of the same order-2 data. The proved bar
  symmetry of `G^j_m` is exactly the formalize-first constraint the workplan wants
  on `c(q)` before any scan.

## 5. Corpus references.ts status

Existing keys: `garoufalidis2004`, `garoufalidis-le-2005`, `le2006`,
`nguyen-tran-2021`, `garoufalidis-le-2011`, `garoufalidis-gu-marino2021`,
`garoufalidis-gu-marino2023peacock`, `garoufalidis-zagier2023`, `habiro2000/2002/
2004cyclotomic`, `askey1989qhermite`, `ismail-masson1994`, `atakishiyev-suslov1990`,
`sokal1980`, `costin1995`, Écalle (resurgence founding entry).

**Added (this branch):** Zhang 1999 (AIF 49, `zhang1999`); Marotte–Zhang 2000
(AIF 50, `marotte-zhang2000`); Di Vizio–Zhang 2009 (DOI 10.5802/aif.2433,
`divizio-zhang2009`); Ramis–Sauloy–Zhang 2013 (Astérisque 355 / arXiv:0903.0853,
`ramis-sauloy-zhang2013`); Cigler–Zeng (arXiv:0905.0228, `cigler-zeng2009`).
The optional Josuat-Vergès Touchard–Riordan generalization was not added.

## 6. Ranked shortlist

1. **GGM descendant eq (49) + AJ order-2 recurrence for 4₁** — the q-lift almost
   certainly *is* this order-2 carrier: right knot, right depth, bar symmetry
   proved, Stokes matrix `[[1,0],[−3,1]]` already the corpus's identification
   target (workplan step 3). Start here.
2. **q-Hermite / crossing-weighted involutions** — gives the concrete candidate
   `c(q) = 1` via `I_q(n+1) = I_q(n) + [n]_q·I_q(n−1)` (inferred, needs a short
   derivation or a located theorem); the combinatorial q-lift of `e^{x+x²/2}`.
   Cheap to formalize-first and to cross-check against route 1's coefficient
   `(2 − q^m)`.
3. **Ramis–Zhang / Di Vizio–Zhang summability + confluence** — not a kernel source
   but the proof frame: Gq-summability of the order-2 solution and the q→1
   confluence statement that makes "classical kernel = shadow of q-kernel" a
   theorem shape rather than an analogy.

**Honesty summary.** Verified in-sandbox: GGM eq (49)/Thm 9 (PDF read); corpus key
inventory (grep). Verified via search snippets only: AIF metadata, 4₁ order-2
inhomogeneous minimality, Marotte–Zhang and Di Vizio–Zhang statements. Inferred,
unlocated as theorem: the `c(q) = 1` q-involution recurrence of §2.
