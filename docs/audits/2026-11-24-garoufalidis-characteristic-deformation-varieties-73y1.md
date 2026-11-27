# Garoufalidis Characteristic vs Deformation Varieties (`characteristic.pdf` / `[garoufalidis2004]`) — Corpus Cross-Check and Two-$\rho_\infty$-Faces Synthesis (`qou-73y1`)

**Date:** 2026-11-24 · **Branch:** `claude/editorial-audit-0sq1-20d3-9rbo-73y1-20261124` · **Closes:** `qou-73y1` · **Held Source:** `library/characteristic/characteristic.pdf` (`[garoufalidis2004]`, Stavros Garoufalidis, *"On the characteristic and deformation varieties of a knot"*, *Geometry & Topology Monographs* **7** (2004), 291–309, DOI `10.2140/gtm.2004.7.291`, `arXiv:math/0306230`).

This audit cross-checks Garoufalidis's definitions, operator conventions, and explicit $3_1$ / $4_1$ calculations in `library/characteristic/characteristic.pdf` against the QOU corpus's $A$-polynomial and AJ Lean/compute carriers (`QOU.BraidKnot.AJTrefoil`, `QOU.BraidKnot.AJFigureEight`, `QOU.Mass.FourOneAPolynomialFromGluing`, `QOU.Mass.FiveTwoAPolynomialFromFareyWord`, and `stochastic-mechanics/phi-q-aj-machinery-identification`), and records the exact dimensional consequence for the two-$\rho_\infty$-faces bridge and Subgoal-2 ($q_0$ derivation).

---

## 1. Exact Operator & Variety Dictionary (`characteristic.pdf` §§1.1–2.3)

Garoufalidis (§1.1–1.2, §2.2) normalizes the zero-framed colored Jones function $J_K : \mathbb{N} \to \mathbb{Z}[q^{\pm 1}]$ of a knot $K \subset S^3$ by $J_{\mathrm{unknot}}(n) = 1$ for all $n \ge 1$ (so $J_K(1) = 1$ and $J_K(2)$ is the ordinary Jones polynomial), and acts on discrete functions $f : \mathbb{N} \to \mathbb{Q}(q)$ by the $q$-Weyl algebra

$$
  \mathcal{A} = \mathbb{Z}[q^{\pm 1}]\langle Q, E \rangle / (E Q - q Q E),
  \qquad
  (Q f)(n) = q^n f(n),
  \qquad
  (E f)(n) = f(n + 1).
$$

1. **Recursion ideal and noncommutative $A_q$-polynomial (§1.2, §2.2 Def. 2.1):**
   - Left annihilator (recursion) ideal: $I_f = \{P \in \mathcal{A} \mid P f = 0\}$. By Garoufalidis–Lê (`[garoufalidis-le-2005]`), $J_K$ is $q$-holonomic ($I_{J_K} \neq 0$) for every knot $K \subset S^3$.
   - Because $\mathcal{A}$ is not a principal ideal domain, Garoufalidis localizes in $Q$ to the Ore algebra $\mathcal{A}_{\mathrm{loc}} = \mathbb{Q}(q, Q)[E, \sigma]$ with $\sigma(g)(q, Q) = g(q, qQ)$, where every left ideal is principal, and defines $A_q(K) = \sum_{k=0}^d a_k(q, Q) E^k \in \mathcal{A}$ as the minimal-$E$-degree generator of $\mathcal{A}_{\mathrm{loc}} I_{J_K}$ cleared to coprime coefficients $a_k \in \mathbb{Z}[q, Q]$ (unique up to $\pm q^a Q^b$).
2. **Characteristic variety (§1.2 Def. 1.2) — full $q \to 1$ ideal, not top symbol:**
   - Under the evaluation map $\epsilon : \mathcal{A} \to \mathbb{Z}[E, Q]$ sending $q \mapsto 1$,
     $$
       \mathrm{ch}(K) := \bigl\{(x, y) \in (\mathbb{C}^\times)^2 \;\big|\; P(x, y) = 0 \text{ for all } P \in \epsilon(I_{J_K})\bigr\}.
     $$
   - Garoufalidis explicitly notes (§1.2, p. 2) that $\mathrm{ch}(I)$ evaluates **all** shift terms of $P$ at $q = 1$, unlike the classical $D$-module characteristic variety which retains only the principal symbol (highest $E$-power).
3. **Deformation variety & peripheral holonomy dictionary (§1.3, §2.1–2.2 Def. 2.2):**
   - Restricting the $SL_2(\mathbb{C})$ character variety $X(S^3 \setminus \mathrm{nbd}(K))$ to upper-triangular representations of $\pi_1(\partial M) \cong \mathbb{Z}^2$ with meridian and longitude upper-left eigenvalues $(M, L) \in (\mathbb{C}^\times)^2$ defines the Cooper–Culler–Gillet–Long–Shalen (CCGLS) deformation variety $D(K) \subset (\mathbb{C}^\times)^2$, whose 1-dimensional part is cut out by the classical $A$-polynomial $A_K(L, M) \in \mathbb{Z}[L, M^2]$.
   - **Meridian-squared operator identification (Def. 2.2):**
     $$
       (E,\, Q) \longleftrightarrow (L,\, M^2), \qquad \text{i.e. } E = L,\; Q = M^2\;(M = Q^{1/2}).
     $$
   - **Conjecture 2 (AJ Conjecture, §2.2):** $A_K(L, M) \doteq \epsilon(A_q(K))(L, M^2)$ up to multiplication by rational functions in $M^2$ and powers of $L$ ("essentially equal" in $\mathbb{Q}(M^2)[L]$, Lemma 2.3), which implies **Conjecture 1** ($\mathrm{ch}(K)$ and $D(K)$ have identical pure 1-dimensional components up to $M$-lines $M = \text{const}$, §1.4).

---

## 2. Line-by-Line Verification Against QOU Corpus Carriers

### A. Inhomogeneous Order vs Homogenized Abelian Factor $(L - 1)$
A crucial structural distinction between `characteristic.pdf` §3.2 and the corpus's `QDifferenceOperator` encoding (`QOU.BraidKnot.AJFigureEight`, `QOU.BraidKnot.AJTrefoil`):

- Because $J_K(n)\big|_{q=1} = 1$ for all $n$, Garoufalidis's **Lemma 3.1** (§3.2, p. 10) proves $\epsilon A_q(K)(1, 1) = 0$ for every knot, and his homogenized recursion (`MakeHomRec` in §3.2 `In[5]`, `In[11]`) eliminates the inhomogeneous right-hand side at the cost of **increasing the $E$-order by $1$** and introducing the reducible/abelian factor $(L - 1)$ in $A(K) = (L - 1) \cdot A_K^{\mathrm{nonab}}(L, M)$.
- By contrast, `QOU.BraidKnot.AJFigureEight.QDifferenceOperator` (`AJFigureEight.lean:56–70`) encodes the **inhomogeneous** operator $\sum_{j=0}^d c_j(q, q^N) J(N+j) = \mathrm{rhs}(q, q^N)$ directly, so its homogeneous part `∑ c_j(1, M²) L^j` specializes directly to the **nonabelian** CCGLS $A$-polynomial $A_K^{\mathrm{nonab}}(L, M)$ at $E$-degree $d$ (without the $(L - 1)$ factor):

| Knot $K$ | Garoufalidis Homogenized `ord_E(A_q)` (`characteristic.pdf` §3.2) | Corpus Inhomogeneous `op.order` | Abelian Factor Status |
|---|---:|---:|---|
| $3_1$ (trefoil) | $2$ (`Out[5]`, `ord_E(rec31) = 2`) | $1$ (`AJTrefoil.trefoilOperator.order = 1`) | Absorbed into `trRhs`; homogeneous part gives nonabelian degree-1 factor |
| $4_1$ (figure-eight) | $3$ (`Out[11]`, `ord_E(rec41) = 3`) | $2$ (`AJFigureEight.order_eq : op.order = 2`, matching `In[10]: qZeil[..., 2]`) | Absorbed into `rhs`; homogeneous part gives nonabelian degree-2 factor |
| $5_2$ (three-twist) | $4$ (Takata / Garoufalidis–Koutschan homogenized) | $3$ (nonabelian $L$-degree $3$ in `FiveTwoAPolynomialFromFareyWord.A`) | Nonabelian $A_{5_2}(L, M)$ has $L$-degree $3$ |

### B. Trefoil $3_1$ Cross-Check (`characteristic.pdf` §3.1 eq. (6), §3.2 `Out[8]` vs `AJTrefoil.lean`)
- **Garoufalidis (§3.1 eq. (6) & §3.2 `Out[8]`):**
  $$
    A(3_1)(L, M) = (L - 1)(L + M^6),
    \qquad
    \epsilon(\mathrm{rec31})(L, M^2) = -\frac{(L - 1)(L + M^6)}{L^2 M^2 (1 + M^2)}.
  $$
- **Corpus (`QOU.BraidKnot.AJTrefoil`, lines 108–125, sorry-free):**
  - `aPolyTrefoil L M := 1 + L * M ^ 6`, `trUnit M := (1 - M ^ 2) / M ^ 10`.
  - **Chiral convention reconciliation:** Under mirror reflection $K \mapsto \overline{K}$ ($q \mapsto q^{-1}$), Cooper–Long Proposition 4.2 (`characteristic.pdf` Remark 2.4) transforms $A_{\overline{K}}(L, M) \doteq A_K(L^{-1}, M)$, and $L \cdot \bigl((1) + L^{-1} M^6\bigr) = L + M^6$. Both `AJTrefoil` (self-anchored against $V(3_1) = -q^{-4} + q^{-3} + q^{-1}$) and Garoufalidis eq. (6) have **identical $M$-exponent $6$** (i.e. $Q^3$ under $Q = M^2$) and differ solely by $L \mapsto L^{-1}$ mirror convention plus the $(L - 1)$ homogenization factor.

### C. Figure-Eight $4_1$ Cross-Check (`characteristic.pdf` §3.1 eq. (7), §3.2 `Out[14]` vs `AJFigureEight.lean` & `FourOneAPolynomialFromGluing.lean`)
- **Garoufalidis (§3.1 eq. (7) & §3.2 `Out[14]`):**
  $$
    A(4_1)(L, M) = (L - 1)\bigl(-L + L M^2 + M^4 + 2 L M^4 + L^2 M^4 + L M^6 - L M^8\bigr),
  $$
  and `Out[14]` evaluates to
  $$
    \epsilon(\mathrm{rec41})(L, M^2)
    = \frac{(L - 1)\bigl(L - L M^2 - M^4 - 2 L M^4 - L^2 M^4 - L M^6 + L M^8\bigr)}{L^3 M^4 (1 + M^2)^2}.
  $$
- **Corpus (`AJFigureEight.aPolyFigureEight` & `FourOneAPolynomialFromGluing.A41`, sorry-free):**
  $$
    \mathrm{A41}(L, M) = M^4 L^2 - (M^8 - M^6 - 2 M^4 - M^2 + 1) L + M^4.
  $$
- **Exact algebraic identity:** Expanding Garoufalidis's nonabelian factor in eq. (7) gives
  $$
    -L + L M^2 + M^4 + 2 L M^4 + L^2 M^4 + L M^6 - L M^8
    = M^4 L^2 - (M^8 - M^6 - 2 M^4 - M^2 + 1) L + M^4
    = \mathrm{A41}(L, M)
  $$
  **identically with sign $+1$** (and the second factor of `Out[14]` is $-\mathrm{A41}(L, M) = \mathrm{A41\_routeA}(L, M)$, matching `FourOneAPolynomialFromGluing.A41_routeA_eq_neg`). All seven nonzero monomials agree coefficient-for-coefficient across `characteristic.pdf` eq. (7), Culler's census `K2_1.apoly`, the Neumann–Zagier gluing elimination (`FourOneAPolynomialFromGluing.A41_vanishes_of_nz_gluing_lift`), and the $q = 1$ specialization of the division-free qZeilberger operator (`AJFigureEightAnnihilation`). Furthermore, both Garoufalidis's denominator $L^3 M^4 (1 + M^2)^2$ and `AJFigureEight`'s `unit` factor $(M^2 - 1)^2(M^2 + 1)/M^{16}$ are pure $L$-monomial $\times$ rational functions of $M^2$ whose zeros/poles lie exclusively on the degenerate meridian lines $M^2 \in \{0, \pm 1\}$ ("essential equality" up to $y$-lines in §1.4).

### D. Twist Knot $5_2$ & Existing Monograph Citations
- **`QOU.Mass.FiveTwoAPolynomialFromFareyWord`:** Recovers the degree-3 nonabelian polynomial $A_{5_2}(L, M) = L^3 + L^2(M^{10} - M^8 + 2M^4 + 2M^2 - 1) + L(-M^{14} + 2M^{12} + 2M^{10} - M^6 + M^4) + M^{14}$ (verified chiral mirror $L^3 A(L^{-1}, M) = A_{\mathrm{census}}(L, M) \neq A(L, M)$, `A_census_eq_mirror`, `A_ne_A_census`, consistent with Remark 2.4 of `[garoufalidis2004]`). Under Definition 2.2 ($E = L$), the jump in nonabelian $L$-degree from $2$ ($4_1$, amphichiral) to $3$ ($5_2$, chiral) corresponds directly to the inhomogeneous $q$-difference order jumping from $2$ (pure bar-even Hahn–Exton $q$-Bessel kernel) to $3$ (bar-odd chiral twist channel, `qou-do3a`).
- **Existing monograph citations verified accurate:**
  - `folio/quantum-observable-universe/stochastic-mechanics/phi-q-aj-machinery-identification.{ts,md}` cites `\cite[§2.2]{garoufalidis2004}` for the quantum $A$-polynomial $\hat{A}_K \in \mathcal{A}_q$ defined from the recursion ideal of the colored Jones function — verified exact (`§2.2, Def. 2.1` is indeed where $A_q(K)$ is defined).
  - `folio/quantum-observable-universe/nuclear-interactions/q-zero-stokes-region-identification.ts` lists `garoufalidis2004` in `cites`.

---

## 3. Implications for the Two-$\rho_\infty$-Faces Bridge and Subgoal-2 ($q_0$ Derivation)

### A. The Two Faces of $\rho_\infty$ Are Connected by $\epsilon : q \mapsto 1$
In the framework's asymptotic / resurgent bridge:
1. **The algebraic ($q$-holonomic) face** is the noncommutative recursion operator $A_q(K)(E, Q; q) \in \mathcal{A}$ acting on the discrete color tower $J_K(N)$ (and its Habiro / state-integral / $q$-Bessel kernels at general $q$).
2. **The geometric ($SL_2(\mathbb{C})$ character-variety) face** is the classical curve $D(K) = \{A_K(L, M) = 0\} \subset (\mathbb{C}^\times)^2$, whose logarithmic differential $\log |M|\,d(\arg L) - \log |L|\,d(\arg M)$ governs hyperbolic volume variation under Dehn surgery (`characteristic.pdf` Remark 1.7, citing CCGLS §4.5 and Neumann–Zagier eq. (47)) and whose Newton-polygon slopes govern asymptotic growth rates (`RouteANewtonPolygonDT.lean`).

Garoufalidis's AJ bridge ($A_K(L, M) \doteq \epsilon A_q(K)(L, M^2)$, proved in-corpus for $3_1$ and $4_1$) establishes that the geometric character-variety face is literally the **$q \to 1$ commutative shadow** of the $q$-holonomic recursion ideal under $(E, Q) \mapsto (L, M^2)$.

### B. Why $D(K) = \mathrm{ch}(K)$ Alone Cannot Pin $q_0$ Without a Second Condition (Subgoal 2)
`characteristic.pdf` Lemma 4.3 (via Sabbah's $q$-analogue of Bernstein's inequality for rank $r = 1$ holonomic $\mathcal{A}$-modules) proves that for every nonzero $q$-holonomic module $M_{J_K}$,

$$
  \dim_{\mathbb{C}} \mathrm{ch}(M_{J_K}) \ge 1,
$$

and for hyperbolic and torus knots $D(K)$ is a **pure 1-dimensional complex curve** in $(\mathbb{C}^\times)^2$ (up to finite 0-dimensional components and $M$-lines). Two immediate mathematical consequences govern any non-fitted Subgoal-2 attempt to derive the substrate parameter $q_0$ from knot geometry:

1. **$q$ has already been specialized to $1$ in $\mathrm{ch}(K)$:** Passing from $A_q(K)(E, Q; q)$ to $\epsilon A_q(K)(L, M^2) \doteq A_K(L, M)$ evaluates $q = 1$ and trades the $(n, q)$ discrete scale for the continuous 1-complex-dimensional holonomy locus $(L, M) \in D(K)$ (containing, e.g., the complete hyperbolic point $(L, M) = (-1, 1)$ proved in `FourOneAPolynomialFromGluing.A41_complete_point` and `FiveTwoAPolynomialFromFareyWord.A_complete_point`, alongside a full 1-parameter family of deformed/Dehn-filling representations).
2. **Curve $\neq$ point (1 degree of freedom remains):** Because $\dim_{\mathbb{C}} D(K) = 1$, the $A$-polynomial $A_K(L, M) = 0$ defines a **locus** rather than a number. Pinning a discrete substrate value $q_0$ without fitting (`NO FITTING` discipline) requires intersecting or lifting $D(K)$ with an **independent second constraint**, such as:
   - retaining the full $q$-dependent operator $A_q(K)(E, Q; q)$ prior to $\epsilon : q \mapsto 1$ together with a meridian-holonomy / boost identification $Q = q^N$ or $M = e^{u/2}$ at a distinguished categorical fixed point, or
   - a cross-knot arithmetic / Bloch-group / quantum-modular compatibility condition across multiple saddles or Stokes sectors (`[garoufalidis-gu-marino2021]`, `[garoufalidis-zagier2023]`).

Accordingly, `[garoufalidis2004]` supplies the rigorous algebraic-to-geometric bridge $\mathcal{A}_q \xrightarrow{q \to 1} \mathbb{Z}[L, M^2]/(A_K)$ for the corpus's $3_1$, $4_1$, and $5_2$ carriers, while proving by dimension count why $A_K(L, M) = 0$ is a necessary 1-dimensional geometric constraint rather than a standalone 0-dimensional determination of $q_0$.
