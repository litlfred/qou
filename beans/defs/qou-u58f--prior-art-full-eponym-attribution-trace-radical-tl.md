---
# qou-u58f
title: 'Prior art & full-eponym attribution: trace-radical TL_n(q) quotient (Orellana, Geck-Lambropoulou, Jones, BHMV, Barrett-Westbury), Leibniz PII / GNS null ideal, and Rieffel-Connes-Kantorovich-Rubinstein metric finiteness'
status: completed
type: task
priority: high
tags:
    - prior-art
    - attribution
    - connes-distance
    - temperley-lieb
created_at: 2026-11-23T18:30:19Z
updated_at: 2026-11-24T09:20:47Z
---

## Summary & Purpose

Prior-art and full-eponym attribution sweep for QOU's three-part structural bridge connecting:
1. **Quotienting the Hecke algebra by the Convention-D Markov trace radical** ($H_n(q)/\mathrm{rad}(\tau) \cong TL_n(q)$ at $z_D = q^3/(q^2+1)$),
2. **Gottfried Wilhelm Leibniz's Principle of the Identity of Indiscernibles (PII)** as operational GNS / presymplectic null-radical quotienting, and
3. **Gram degeneracy ($\det G = 0 \implies \ker L \supsetneq \mathbb{C}\cdot 1$) driving the Connes–Kantorovich–Rubinstein spectral distance to $+\infty$** until quotiented to the faithful Temperley–Lieb algebra $TL_n(q)$ (`gram-degeneracy-blocks-connes.md`, `connes-distance-not-reeb-step-count.md`, `intro.md`, `references.bib`).

Bundles cleanly onto queued branch `claude/leibniz-relational-scales-20261123` alongside Chapter 0 Leibniz relational-space framing (`intro.md`, avoiding `introduction.ts` touched by `#9194`) and beans `qou-adwi` + `qou-5uj7`.

---

## 1. Lineage A — Trace-Radical Quotient ($H_n(q)/\mathrm{rad}(\tau) \cong TL_n(q)$) & Negligible Morphisms

1. **Subfactor & Hecke–Temperley–Lieb GNS Quotient:**
   - **Harold Neville Vazeille Temperley & Elliott H. Lieb (1971)**, *Proc. R. Soc. Lond. A* 322, 251–280 (diagram algebra $TL_n$).
   - **Vaughan F. R. Jones (1983, 1985, 1987)** (*Invent. Math.* 72, 1–25; *Ann. of Math.* 126, 335–388) & **Adrian Ocneanu**: GNS inner product $\langle x, y\rangle = \mathrm{tr}(x^* y)$ on $H_n(q)$; at two-row Markov weight $z_D = q^3/(q^2+1)$, vanishing on $\ell(\lambda) \ge 3$ (`[1^3]` at $n=3$, $\dim 6 \to C_3 = 5$) yields $H_n(q)/\mathcal{N}_\tau \cong TL_n(q)$.
   - **Hans Wenzl (1987, 1988)** (*C. R. Math. Rep. Acad. Sci. Canada* 9; *Invent. Math.* 92, 349–383) & **Paul P. Martin (1991)** (*Potts Models and Related Problems in Statistical Mechanics*): explicit Gram determinants and Jones–Wenzl idempotents.
   - **Rosa C. Orellana (1999)**, *"Weights of Markov traces on Hecke algebras"*, *J. Reine Angew. Math.* (Crelle's Journal) 508, 157–178, and **Meinolf Geck & Sofia Lambropoulou (1997)**, *"Markov traces and knot invariants related to Iwahori–Hecke algebras of type B"*, *J. Reine Angew. Math.* 482, 191–213: explicit Young-diagram Markov trace weight formulas on Iwahori–Hecke algebras and exact characterization of weight-vanishing trace radicals (essential citations in Ch. 5, Ch. 11, and `gram-degeneracy-blocks-connes.md`).

2. **Universal Skein & Categorical Semisimplification ($\overline{\mathcal{C}} = \mathcal{C}/\mathcal{N}$):**
   - **Christian Blanchet, Nathan Habegger, Gregor Masbaum & Pierre Vogel (1992, 1995)** (*Topology* 31, 685–699; 34, 883–927 — spell out all four BHMV authors on first mention) and **Vladimir G. Turaev (1994)** (*Quantum Invariants of Knots and 3-Manifolds*): operational universal skein quotient identifying tangle combinations indistinguishable across all closed pairings.
   - **John W. Barrett & Bruce W. Westbury (1996, 1999)** (*Trans. Amer. Math. Soc.* 348, 3997–4022; *Adv. Math.* 143, 357–375): tensor ideal $\mathcal{N}$ of negligible morphisms ($\mathrm{tr}(f\circ g)=0\;\forall g$) and semisimplified quotient $\mathcal{C}/\mathcal{N}$.
   - **Pavel Etingof, Shlomo Gelaki, Dmitri Nikshych & Victor Ostrik (2015)** (*Tensor Categories*, AMS): modern categorical semisimplification.
   - **QOU-Distinctive Contrast to State Explicitly:** Standard TQFT semisimplifies at *roots of unity* $q = e^{i\pi/r}$ to kill quantum-dimension-zero tilting modules; QOU takes the trace-radical quotient at **real hyperbolic $q_0 > 1$** (where $U_q(\mathfrak{sl}_2)$ is semisimple) purely from the **two-row $SU_q(2)$ Schur–Weyl rank cap** (**Michio Jimbo 1986**) making $y_\lambda = 0$ for $\ell(\lambda) \ge 3$ under Convention D.

---

## 2. Lineage B — Leibniz's Identity of Indiscernibles as GNS / Null-Radical Quotient

1. **Relational Space & Identity of Indiscernibles:**
   - **Gottfried Wilhelm Leibniz & Samuel Clarke (1717)** (*Correspondence*, 1715–1716, Third Letter §4): space as the order of coexistences ($\otimes, \sigma$), time as the order of successions ($\circ$), and PII disallowing distinct mathematical states with identical observable relations.
2. **Operational GNS Null Ideal & Gauge Null Radical:**
   - **Israel M. Gelfand & Mark A. Naimark (1943)** and **Irving E. Segal (1947)** (*Ann. of Math.* 48, 930–948 — credit all three on GNS): quotienting $A$ by $\mathcal{N}_\tau = \{a \in A : \tau(a^*a)=0\}$ as operational identification of empirically indiscernible elements; extended to physical equivalence by **Rudolf Haag & Daniel Kastler (1964)** (*J. Math. Phys.* 5, 848–861).
   - **Paul A. M. Dirac** and **Marc Henneaux & Claudio Teitelboim (1992)** (*Quantization of Gauge Systems*, Ch. 1–2): gauge equivalences as the null radical $\ker(\omega)$ of a degenerate bilinear/presymplectic form, requiring quotienting before a non-degenerate metric/symplectic form exists; analogous to Andrey N. Kolmogorov's pseudometric quotient $X/\{d=0\}$.
   - Philosophical analyses (optional scholarly context): **Hermann Weyl (1949)**, **Simon Saunders (2003)**, **Steven French & Décio Krause (2006)**, **Klaas Landsman (2017)**.

---

## 3. Lineage C — Gram Degeneracy Blocking Connes–Kantorovich–Rubinstein Distance

1. **Connes–Kantorovich–Rubinstein Spectral Metric:**
   - **Leonid V. Kantorovich (1940, 1942)** & **Gennady Sh. Rubinstein (1957–1958)** (primal-dual optimal transport metric, prior to Vasershtein 1969) and **Alain Connes (1989, 1994)** (*Ergodic Theory Dynam. Systems* 9, 207–220; *Noncommutative Geometry*): $d_D(\phi,\psi) = \sup\{|\phi(a)-\psi(a)| : \|[D,\pi_\tau(a)]\| \le 1\}$.
   - Two distinct failure modes under $\det G = 0$ on unquotiented $H_n(q)$ ($n \ge 3$, Convention D): (A) $r \in \mathrm{rad}(\tau) \implies \pi_\tau(r)=0 \implies L(r)=0$, sending $d_D(\phi,\psi) \to +\infty$ whenever $\phi(r) \neq \psi(r)$; (B) kinetic/Hodge $G^{-1}$ singularity.
2. **Lip-Norm Kernel / Faithfulness Criterion & Degenerate Spectral Triples:**
   - **Marc A. Rieffel (1998, 1999, 2004)** (*Doc. Math.* 4, 559–600; *Mem. Amer. Math. Soc.* 168) and **Hanfeng Li (2005)**: $d_L$ defines a finite topology-generating state-space metric iff $\ker(L) = \mathbb{C}\cdot 1_{\mathcal{A}}$ (forcing $\pi_\tau$ faithful, i.e., quotienting $\mathrm{rad}(\tau)$ first) and the unit $L$-ball is compact in $\mathcal{A}/\mathbb{C}1$.
   - **Frédéric Latrémolière (2015, 2016)** (*J. Funct. Anal.*): coincidence/faithfulness property — non-trivial representation kernel $I = \mathrm{rad}(\tau)$ forces $d_D = +\infty$ outside states factoring through $\mathcal{A}/I \cong TL_n(q)$.
   - **Bruno Iochum, Thomas Krajewski & Pierre Martinetti (2001)** (*J. Geom. Phys.* 37, 100–121 — note: **Bruno** Iochum, verify exact given name in `.bib`!) and **Francesco D'Andrea & Pierre Martinetti (2010)**: explicit characterization of infinite-distance walls when $\ker([D,\pi(\cdot)]) \supsetneq \mathbb{C}1$ and recovery of finite distance on the quotient modulo the null ideal.
   - **QOU-Distinctive Synthesis to State Explicitly:** Unlike Chamseddine–Connes spectral Standard Models (which postulate a semisimple finite algebra $\mathcal{A}_F = \mathbb{C}\oplus\mathbb{H}\oplus M_3(\mathbb{C})$ with faithful trace by hand), QOU starts with $H_n(q)$ at real $q_0 > 1$, proves Convention-D observability forces $\det G = 0$ for $n \ge 3$, and uses Rieffel's Lip-norm kernel theorem to show **state-space metric finiteness dynamically forces $H_n(q) \twoheadrightarrow TL_n(q)$**.

---

## Acceptance Criteria / Deliverables

- [ ] Add verified primary BibTeX entries (`leibniz-clarke1717`, `orellana1999`, `geck-lambropoulou1997`, `barrett-westbury1999`, `bhmv1995`, `segal1947`, `haag-kastler1964`, `henneaux-teitelboim1992`, `kantorovich1942`, `rubinstein1957`, `rieffel1999`, `rieffel2004`, `latremoliere2016`, `iochum-krajewski-martinetti2001`, `dandrea-martinetti2010` — reusing any keys already in `folio/quantum-observable-universe/references.bib` without duplicates, and verifying exact first names such as *Bruno* Iochum).
- [ ] Add/update prior-art remarks & full-eponym attributions in:
  1. `folio/quantum-observable-universe/mass-theory/gram-degeneracy-blocks-connes.{md,ts}` (citing Rieffel 1999/2004, Kantorovich 1942, Rubinstein 1957, Latrémolière 2016, Iochum–Krajewski–Martinetti 2001, Orellana 1999, Geck–Lambropoulou 1997, Jones 1987, Wenzl 1988, Barrett–Westbury 1999, BHMV 1995, Gelfand–Naimark–Segal, and stating both QOU-distinctive contrasts cleanly in Milnor voice).
  2. Chapter 5 Hecke/Temperley–Lieb radical block (`hecke-radical-is-temperley-lieb` or adjacent remark, crediting Rosa C. Orellana 1999 & Meinolf Geck and Sofia Lambropoulou 1997 alongside Vaughan F. R. Jones 1987, Hans Wenzl 1988, Harold Neville Vazeille Temperley & Elliott H. Lieb 1971).
  3. Chapter 0 Overview (`introduction/intro.md`, paired with Leibniz relational-space framing, avoiding `introduction.ts` touched by `#9194`).
- [ ] Pass `voice-leak-ratchet.ts`, `run-validate.ts`, and `run-validate-references.ts` (`0` errors).

Closed via post-merge reconciliation: landed on origin/main in PR #9207 (5a350c1a535).
