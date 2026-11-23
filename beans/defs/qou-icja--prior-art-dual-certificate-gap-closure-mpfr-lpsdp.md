---
# qou-icja
title: 'Prior art & dual-certificate gap closure: MPFR LP/SDP bootstrap (Kantorovich, Gatermann-Parrilo, Viazovska, van Aggelen, Boldo-Mahboubi, Goulart-Chen, Dvorak-Kolmogorov) + extremal-functional uniqueness in Lean'
status: in-progress
type: task
priority: high
tags:
    - prior-art
    - attribution
    - lp-duality
    - compute-closure
created_at: 2026-11-23T19:27:02Z
updated_at: 2026-11-23T20:54:28Z
parent: qou-qzvs
---

## Summary & Purpose

1. **Prior-art & equitable multi-author attribution** for QOU's symmetry-reduced arbitrary-precision LP/SDP (`clarabel-mpfr`), Schrijver/Gatermann–Parrilo Young-diagram shadow prices ($u_\lambda, u_0$), complementary-slackness operator selection, and `.witness.json` $\to$ `sorry`-free Lean 4 dual-certificate verification pipeline.
2. **Methodological gap-closure application**: apply (a) **Dvořák–Kolmogorov / Farkas / Viazovska strict complementary-slackness uniqueness** (`unique_primal_of_strict_dual_slack`), (b) **Gatermann–Parrilo / Schrijver centralizer block reduction**, and (c) **Verstichel–van Aggelen–Mazziotti $(D,Q,G)$ positivity + Kazakov–Zheng inhomogeneous skein-loop equations** to attack QOU's open discrete-selection and normalization gaps (`g_A(q_0)` colour-spin expectation in `hadron-half-life-verification.md`, discrete scan-index uniqueness on `m_K/m_pi`, and `A=4` normal-form uniqueness).

---

## Five Prior-Art Pillars & Mandatory Full-Eponym Attributions

1. **MPFR Conformal / S-Matrix / Sphere-Packing Bootstrap & Extremal Functionals:**
   - **Riccardo Rattazzi, Vyacheslav S. Rychkov, Erik Tonni & Alessandro Vichi (2008)** (*JHEP* 12, 031): LP primal operator weights vs dual shadow-price exclusion certificates.
   - **Sheer El-Showk, Miguel F. Paulos, David Poland, Slava Rychkov, David Simmons-Duffin & Alessandro Vichi (2012, 2014)**: extremal functional method (physical states locked at zeros of optimal dual slack).
   - **David Simmons-Duffin (2015)** (*JHEP* 06, 174) & **Walter Landry & David Simmons-Duffin (2019)** (`SDPB` native GNU MPFR primal-dual interior-point solver for ill-conditioned polynomial blocks), alongside **Paul J. Goulart & Yuwen Chen (2024)** (*arXiv:2405.12762*, Clarabel interior-point conic algorithm).
   - **Henry Cohn & Noam Elkies (2003)** (*Ann. of Math.* 157, 689–714), **Maryna S. Viazovska (2017)** (*Ann. of Math.* 185, 991–1016), and **Henry Cohn, Abhinav Kumar, Stephen D. Miller, Danylo Radchenko & Maryna Viazovska (2017)**: zero-gap complementary slackness pinning unique algebraic structures ($E_8$, Leech lattice).

2. **Symmetry-Reduced Representation-Theoretic Block LP/SDP (`u_λ` Shadow Prices):**
   - **Philippe Delsarte (1973)** (*Philips Res. Rep. Suppl.* 10): association-scheme character reduction to LP.
   - **Alexander Schrijver (1979, 2005)** (*IEEE Trans. Inform. Theory* 51, 2859–2866) & **Dion Gijswijt, Alexander Schrijver & Hajime Tanaka (2006)** (*J. Combin. Theory Ser. A* 113, 1719–1731): noncommutative centralizer $*$-algebra block-diagonalization.
   - **Karin Gatermann & Pablo A. Parrilo (2004)** (*J. Pure Appl. Algebra* 192, 95–128): general isotypic Peter–Weyl / Young-diagram decomposition of invariant conic/SOS programs.

3. **Nuclear v2RDM & Noncommutative Trace / Wilson-Loop Bootstrap:**
   - **A. John Coleman (1963)**, **Claude Garrod & Jerome K. Percus (1964)**, **Maho Nakata, Hiroshi Nakatsuji, Mitsuhiro Fukuda, Katsuki Fujisawa & Masakazu Kojima (2001)**, **David A. Mazziotti (2004, 2012)**.
   - **Brecht Verstichel, Helen van Aggelen, Dimitri Van Neck, Paul W. Ayers & Patrick Bultinck (2009)** (*Phys. Rev. C* 80, 034308): $(J,T)$-coupled SDP positivity directly in nuclear pairing and shell-model binding.
   - **Miguel Navascués, Stefano Pironio & Antonio Acín (2007, 2008)** (NPA noncommutative trace Gram hierarchy $\tau(b_i^* b_j) \succeq 0$), **Xizhi Han, Sean A. Hartnoll & Jorrit Kruthoff (2020)**, **Scott Lawrence (2021–2023)**, and **Vladimir Kazakov & Zechuan Zheng (2022–2024)** (*JHEP*, Wilson-loop skein/Makeenko–Migdal equations + Gram positivity).

4. **Certified Rational LP/SDP Dual Certificates in Proof Assistants (`.witness.json` $\to$ Lean 4):**
   - **Gyula Farkas (1902)**, **Leonid Vitaliyevich Kantorovich (1939)** (*resolving multipliers / shadow prices*), **Tjalling C. Koopmans**, **John von Neumann (1947)**, **George B. Dantzig (1951)**.
   - **Thomas C. Hales et al. (2017)** & **Alexey Solovyev (2011)** (Flyspeck external LP $\to$ formal HOL Light dual verification), **Xavier Allamigeon & Ricardo D. Katz (2019)**, **Sylvie Boldo, Catherine Lelay, Guillaume Melquiond, Assia Mahboubi & Pierre Roux** (Coq certified SDP/positivity witnesses), and **Martin Dvořák & Vladimir Kolmogorov (2024/2026)** (*arXiv:2409.08119*, Lean 4 linear optimization duality).

5. **QOU-Distinctive Synthesis:** Unlike continuum CFT/QCD bootstraps that bound infinite-dimensional correlator islands, QOU solves MPFR conic programs on finite-dimensional Hecke/Temperley–Lieb Young-diagram strata (`Delsarte–Schrijver` + `Gatermann–Parrilo`) to select minimum-action normal forms and verify exact rational dual certificates in Lean 4 (`Hales–Solovyev` + `Dvořák–Kolmogorov`).


Claimed by claude/lp-bootstrap-prior-art-dual-gaps-20261123 (2026-11-23)
PR #9210 opened on claude/lp-bootstrap-prior-art-dual-gaps-20261123 (f89375881ae6)
