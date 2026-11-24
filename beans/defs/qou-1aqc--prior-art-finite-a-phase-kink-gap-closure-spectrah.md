---
# qou-1aqc
title: 'Prior art & finite-A phase-kink gap closure: spectrahedral collapse, Sturmfels-Thomas Grobner chambers, Laurent-Bachoc-Vinzant rank drops & Perdew-Parr magic-shell shadow-price jumps'
status: completed
type: task
priority: high
tags:
    - prior-art
    - attribution
    - spectrahedron
    - magic-numbers
created_at: 2026-11-23T19:29:24Z
updated_at: 2026-11-24T09:20:46Z
parent: qou-qzvs
---

## Summary & Purpose

1. **Prior-art & equitable attribution** for QOU's finite-$A$ phase transitions, nuclear magic-number kinks (§12.4), **Spectrahedral Phase Collapse** (§14.20), $k=12$ / deconfinement regime walls (§15.12, §15.15), and computational phase transitions (Ch. 20) as **LP/SDP facet jumps, Sturmfels–Thomas normal-fan chamber crossings, and dual shadow-price ($u_\lambda$) discontinuities**—explaining sharp phase boundaries at finite $A$ without invoking a Lee–Yang $N \to \infty$ thermodynamic limit.
2. **Formal + Compute Gap Closure**:
   - **Lean 4 (`SymmetryReducedDualCertificate.lean`, Worker 11):** Prove `piecewise_linear_concave_of_parametric_lp` & `dual_shadow_price_jump_at_kink` (a finite-dimensional variational minimum over a polyhedron/spectrahedron exhibits exact non-analytic derivative/shadow-price jumps $u^- > u^+$ at exposed ridges/vertices where the normal cone has dimension $\ge 2$, bypassing the smooth canonical partition-function $N \to \infty$ obstruction of Lee & Yang 1952).
   - **Compute (`qou-i2jl` in Worker 9):** Test the parameter-free **Perdew–Parr / Goeppert-Mayer shell-kink shadow-price jump** $\Delta\mu_{2n}(N=126)$ at the $N=126$ vertex kink as the internal cluster-formation barrier $\exp(-2\sqrt{2\mu_\alpha \Delta\mu_{2n}(126)}\, r_\pi / \hbar)$ explaining magic ${}^{210}\mathrm{Po}$'s $S_\alpha \approx 0.055$ $\alpha$-tunneling hindrance!

---

## Five Literatures & Mandatory Full-Eponym Attributions

1. **Derivative Discontinuities, Magic-Shell Shadow-Price Kinks & RDM Spectrahedral Faces:**
   - **John P. Perdew, Robert G. Parr, Mel Levy & Jose L. Balduz Jr. (1982)** (*Phys. Rev. Lett.* 49, 1691): piecewise linearity of $E(N)$ and exact chemical-potential (shadow-price) jumps at shell closures.
   - **Maria Goeppert Mayer (1948, 1949)** & **Otto Haxel, J. Hans D. Jensen & Hans E. Suess (1949)**: nuclear magic shell closures $N, Z \in \{2,8,20,28,50,82,126\}$ via two-nucleon separation-energy kinks.
   - **Arthur J. Coleman & Vyacheslav I. Yukalov (2000)** and **Valentin Zauner, David Draxler, Laurens Vanderstraeten, Jutho Haegeman & Frank Verstraete (2016)** (*New J. Phys.* 18, 113033): 1st-order transitions = flat exposed facets of the RDM spectrahedron; 2nd-order/shell kinks = non-smooth vertices/ridges with multi-dimensional normal cones.
   - **Gergely Gidofalvi & David A. Mazziotti (2008)** and **Brecht Verstichel, Helen van Aggelen, Dimitri Van Neck, Paul W. Ayers & Patrick Bultinck (2009–2013)**: active-set switches and rank drops in nuclear/fermionic 2-RDM SDPs.

2. **Bootstrap Kinks & Gram Rank-Drop Deconfinement:**
   - **Sheer El-Showk, Miguel F. Paulos, David Poland, Slava Rychkov, David Simmons-Duffin & Alessandro Vichi (2012, 2014)** and **Dalimil Mazáč (2017)**: critical phase transitions at LP/SDP bound kinks via extremal-functional zero rearrangement.
   - **Vladimir Kazakov & Zechuan Zheng (2023)** and **Minjae Cho, Barak Gabai, Ying-Hsuan Lin, Victor A. Rodriguez, Joshua Sandor & Xi Yin (2022)**: Gross–Witten–Wadia and confinement–deconfinement transitions as Gram rank-drop boundary faces.

3. **Parametric LP Chambers, Gröbner Flips, Spectrahedral Shadows & Tropical Phase Loci:**
   - **Saul I. Gass & Thomas L. Saaty (1955)** (parametric LP), **Bernd Sturmfels & Rekha R. Thomas (1997)** (*Math. Programming* 77, 357–387), **Rekha R. Thomas (2006)** (*Lectures in Geometric Combinatorics*), and **João Gouveia, Pablo A. Parrilo & Rekha R. Thomas (2010, 2013)**: normal-fan chambers, Gröbner flips across chamber walls (bridging §12.1 GS normal forms to §12.4 binding regimes!), and spectrahedral facial collapses (§14.20).
   - **Cynthia Vinzant (2014)** (*Notices Amer. Math. Soc.* 61, algebraic boundaries and rank-drop singularities of spectrahedra).
   - **Monique Laurent (2003, 2009)** and **Christine Bachoc & Frank Vallentin (2008)** (*J. Amer. Math. Soc.* 21, 909–942): symmetry-reduced SDP hierarchies and rank-deficient moment/Gram cones.
   - **Victor P. Maslov (1987)**, **Mikhail Kapranov, Bernd Sturmfels & Andrei Zelevinsky (1991)**, **Oleg Viro (2001)**, **Grigory Mikhalkin (2005)**, and **Jacek Miękisz (1993)**: Maslov dequantization / tropical corner loci and $T=0$ ground-state motif polytopes, contrasted with **Tsung-Dao Lee & Chen-Ning Yang (1952)** smooth thermal partition functions.

4. **Conic Intrinsic-Volume Phase Transitions (Ch. 20 Computational Complexity):**
   - **David L. Donoho & Jared Tanner (2005, 2009)** (*PNAS* 102; *J. Amer. Math. Soc.* 22) and **Dennis Amelunxen, Martin Lotz, Michael B. McCoy & Joel A. Tropp (2014)** (*Information and Inference* 3, 224–294).


Claimed by claude/lp-bootstrap-prior-art-dual-gaps-20261123 (2026-11-23)
PR #9210 opened on claude/lp-bootstrap-prior-art-dual-gaps-20261123 (f89375881ae6)

Closed via post-merge reconciliation: landed on origin/main in PR #9210 (9ce8d04d27a).
