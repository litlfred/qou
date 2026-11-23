---
# qou-h6ef
title: 'Layer-2 ChamberGS architecture: explicit nuclear motif conservation matrix A, universal Grobner / Graver basis, odd-even monomer staggering & capacitated Mayer-Jensen shell flips'
status: in-progress
type: feature
priority: high
tags:
    - sturmfels-thomas
    - grobner
    - nuclear-binding
    - compute-closure
created_at: 2026-11-23T19:37:30Z
updated_at: 2026-11-23T20:54:29Z
parent: qou-qzvs
---

## Summary & Purpose

Formalize and compute the **Layer-1 vs. Layer-2 architectural split** for QOU nuclear & atomic assembly using **Bernd Sturmfels & Rekha R. Thomas (1997)** parametric integer programming, toric ideals $I_A$, Graver / universal Gröbner test sets, and capacitated Mayer–Jensen shell slack variables:

- **Layer 1 (`HeckeGS` — Microscopic Noncommutative Braid Layer):** Confluent Bokut–Shiao / Kang–Lee–Lee–Oh Gröbner–Shirshov reduction in $H_n(q) \twoheadrightarrow TL_n(q)$ computes exact rational trace polynomials $\mathrm{tr}_D(w)(q)$ of elementary motifs (unchanged, already sorry-free).
- **Layer 2 (`ChamberGS` — Macroscopic Motif & Capacitated-Shell Integer Program):** Assembling $(Z, N)$ out of elementary motifs $u \in \mathbb{N}^m$ (nucleons, deuteron/triton/helion/$\alpha$ clusters, pair bonds, plus Mayer–Jensen shell-capacity slack variables $u_s + w_s = C_s$ for $C_s \in \{2, 6, 12, 8, 22, 32, 44\}$) under linear conservation $A u = b(Z, N)$ is a **parametric integer program $\mathrm{IP}_{A, c(Z,N,q_0)}(b)$**:
  1. Replaces per-isotope `clarabel-mpfr` `.witness.json` crutches in prose/Lean with **chamber-wide algebraic Gröbner test-set theorems** (`c \cdot (g^+ - g^-) > 0` on finite $\mathcal{G}_k$).
  2. Automatically generates **odd–even nuclear pairing staggering** and Wigner $N=Z$ cusps via exact integer remainder monomers ($u \in \mathbb{N}^m$, avoiding half-$\alpha$ continuous LP relaxation artifacts).
  3. Unifies ordering switches ($A < 4 \leftrightarrow A \ge 4$), magic-shell separation-energy kinks ($w_s = 0$ wall in $\Gamma(A)$), and $\alpha$-fission/decay thresholds ($Q_\alpha = 0$ facet flipping $x_{\mathrm{dau}} x_\alpha \leftrightarrow x_{\mathrm{par}}$) as **Sturmfels–Thomas Gröbner flips**.

---

## Additional Attributions Required
- **Pasquale Conti & Patrizia Gianni (1991)** (*AAECC-9*, LNCS 539, 130–139: toric Buchberger algorithm for integer programming).
- **Jack E. Graver (1975)** (*Math. Programming* 9, 207–226: universal Graver test sets $\mathrm{Gr}_A$).
- **Bernd Sturmfels & Rekha R. Thomas (1997)** (*Math. Programming* 77, 357–387) & **Rekha R. Thomas (1995, 2006)** (Gröbner fans, state polytope $\mathrm{St}(A)$ edge directions = universal Gröbner basis, local wall-ideal Gröbner flips).
- **Louis J. Billera, Israel M. Gel'fand & Bernd Sturmfels (1990)** and **Israel M. Gel'fand, Mikhail M. Kapranov & Andrei V. Zelevinsky (1994)** (secondary polytopes, Gale-dual regular triangulations, bistellar flips).

## Verified Symbolic Enumeration & Owner Decision (`2026-11-23`, Options 1 + 2 + 3 Approved)

1. **Exact Symbolic Enumeration of `A_0 = [[1,0,1,1,2,2],[0,1,1,2,1,2]]` (`p, n, d, t, h, alpha`):**
   - Graver basis `|Gr_{A_0}| = 28` unsigned primitive binomials (`56` signed vectors); `17` unsigned circuits (`34` signed).
   - Universal Gröbner Basis `|U_{A_0}| = 27` unsigned binomials (`54` signed; sole non-UGB Graver element: `x_alpha - x_p x_n x_d`).
   - Exact Gröbner fan: **`73` full-dimensional chambers** in `R^6 / row(A_0) ~= R^4`.
   - **Exact Physical Chamber Coincidence:** `QOU bare q_0`, `QOU tower q_0`, and experimental `AME2020` ALL lie strictly inside the **same chamber `C_phys`**, bounded by 5 irredundant facet walls (`B_alpha - 2 B_h >= 0` [+9.750 MeV QOU vs +12.860 MeV AME], `B_alpha - 2 B_t >= 0` [+8.055 vs +11.332 MeV], `B_t - B_d >= 0` [+7.134 vs +6.257 MeV], `B_h - B_d >= 0` [+6.287 vs +5.493 MeV], `B_d >= 0` [+2.051 vs +2.225 MeV]), with an **11-rule minimal reduced Gröbner basis `G_phys`**.
2. **Two-Stage Confinement Architecture (Owner Approved Options 1 + 2 + 3, Dispatched to Worker 11 on `claude/lp-bootstrap-prior-art-dual-gaps-20261123`):**
   - **Layer 1 (`HeckeGS`, §3.3, §9.5, §12.1):** Enforces colour confinement as the column-alphabet filter (`SU(3)_c` singlets only; `q_local -> q_gold = 1/phi^2` modifies the alphabet at QGP deconfinement).
   - **Layer 2 (`ChamberGS`, §12.2, §12.4-12.5, §15.14-15.15):** Enforces nuclear confinement / stability selection via Sturmfels-Thomas binomial arrow orientation (`x_A x_B -> x_{AB}` bound vs `x_{AB} -> x_A x_B` at drip lines `^5He -> alpha + n`, `^8Be -> 2 alpha` paired with degree-3 Hoyle `x_alpha^3 -> x_{12C}`, and `Z >= 84` alpha-fission), refining `periodic-table-demand-conjecture.md:40`.


Claimed by claude/lp-bootstrap-prior-art-dual-gaps-20261123 (2026-11-23)
PR #9210 opened on claude/lp-bootstrap-prior-art-dual-gaps-20261123 (f89375881ae6)
