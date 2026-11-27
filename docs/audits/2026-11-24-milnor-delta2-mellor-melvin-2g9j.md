# Mellor–Melvin Geometric $\bmod\,\Delta$ Cross-Check for $\Delta = 2$ Milnor Triples (`qou-2g9j`)

**Date:** 2026-11-24  
**Held Primary Reference:** B. Mellor and P. Melvin, *A geometric interpretation of Milnor's triple linking numbers*, *Alg. Geom. Topol.* **3** (2003), 557–568 (`library/0110001v3/`).  
**Probe & Witness:** `computations/probes/milnor_mubar_delta2_mellor_melvin_probe.py` $\to$ `computations/probes/milnor-mubar-delta2-mellor-melvin.witness.json`.

---

## 1. Purpose and Mathematical Formulation

For a 3-component sublink $L_i \cup L_j \cup L_k \subset S^3$ with pairwise linking numbers $\mu_{pq} = \operatorname{lk}(L_p, L_q)$ and indeterminacy $\Delta_{ijk} = \gcd(|\mu_{ij}|, |\mu_{jk}|, |\mu_{ik}|)$, Milnor's triple linking number $\bar{\mu}_{ijk}(L) \in \mathbb{Z}/\Delta_{ijk}\mathbb{Z}$ retains one non-trivial parity bit at $\Delta_{ijk} = 2$.

Mellor and Melvin (2003, Theorem 1, `library/0110001v3/sections/sec-000-1-introduction.md` pp. 560–562 and `sec-001-3-proof-of-the-theorem.md` pp. 562–567) establish that for **any** family $F = (F_i, F_j, F_k)$ of oriented Seifert surfaces in general position,
$$\bar{\mu}_{ijk}(L) \equiv m_{ijk}(F) - t_{ijk}(F) \pmod{\Delta_{ijk}},$$
where:
- $t_{ijk}(F) = \#(F_i \cap F_j \cap F_k) \in \mathbb{Z}$ is the signed count of triple intersection points (oriented by $\operatorname{sign}\det(n_i, n_j, n_k)$), and
- $m_{ijk}(F) = e_{ijk}(F) + e_{jki}(F) + e_{kij}(F)$ with $e_{pqr}(F) = \epsilon_{pq}(w_r)$, the degree-2 Magnus coefficient of $h_p h_q$ in the boundary piercing word $w_r$ read off as $L_r = \partial F_r$ intersects $F_p$ and $F_q$.

Bean `qou-2g9j` previously closed the $\Delta = 2$ carrier residual via direct longitude readout (`milnor_mubar_vanishes_on_every_triple_probe.py`) while leaving Mellor–Melvin's surface formula — and specifically the conjecture that the canonical carrier's $(2, \text{odd})$-torus-knot Seifert surfaces satisfy $t_{ijk}(F) = 0$ on $\Delta = 2$ chain triples — unverified. In addition, an independent verification was needed because `milnor_mubar_vanishes_on_every_triple_probe.py`'s simplified undercrossing reader did not reverse over/under strand positions on $\sigma_g^{-1}$ or conjugate Wirtinger meridians $w^{-1} m_p w$ (causing it to return a nonzero artifact `2` on the Reidemeister-III / Yang–Baxter unlink word $\sigma_0 \sigma_1 \sigma_0 \sigma_1^{-1} \sigma_0^{-1} \sigma_1^{-1} = 1 \in B_3$, although on monotone words no non-monotone conjugation arises).

---

## 2. Two Independent Exact Implementations Cross-Checked

`computations/probes/milnor_mubar_delta2_mellor_melvin_probe.py` implements both formulations in exact integer/rational arithmetic (`int` and `fractions.Fraction`, zero `float64`):

1. **Algorithm 1 — Mellor–Melvin Triangulated Seifert Surfaces in $\mathbb{Q}^3$:**
   - Applies Seifert's algorithm to each component $L_c$ of an $n$-strand closed braid $\widehat{\beta}$ (smoothing intra-component self-crossings into concentric Seifert circles with 6-triangle half-twisted saddle bands, so positive-genus $(2, \text{odd})$-torus knot components are triangulated directly).
   - Verifies $\partial F_c = L_c$ as an exact oriented 1-chain on every component before any intersection query.
   - Computes piercing words $w_r$ by exact rational segment–triangle intersection, checks Mellor–Melvin §2 Remark 2 ($\epsilon_{pq}(w_r) + \epsilon_{qp}(w_r) = \mu_{pr}\mu_{qr}$) and Remark 1 (basepoint cyclic-shift invariance $\bmod\,\Delta$) on every triple, and computes $t_{ijk}(F)$ via exact $3 \times 3$ rational Cramer's rule with strict interior barycentric checks.
2. **Algorithm 2 — Exact Artin / Wirtinger Nilpotent-Class-2 Longitude Magnus Expansion:**
   - Evaluates $\bar{\mu}_{ijk} \equiv \epsilon_{ij}(l_k^{(3)}) \pmod{\Delta_{ijk}}$ in $F(m_0, \dots, m_{\mu-1})/\gamma_3$, tracking exact Wirtinger meridian conjugators $w^{-1} m_p w = 1 + h_p + \sum_q \alpha_q (h_p h_q - h_q h_p) \pmod{h^3}$ and exact inverse $\sigma_g^{-1}$ crossings, verifying cyclic symmetry and antisymmetry $\bmod\,\Delta$ on every triple.

---

## 3. Measured Results

| Test Suite | Braid / Carrier Family | $\Delta$ | Mellor–Melvin $(m_{ijk}, t_{ijk}, m-t \bmod \Delta)$ | Wirtinger $\epsilon_{ij}(l_k^{(3)}) \bmod \Delta$ | Result |
|---|---|---:|---|---|---|
| **Control A.1** (Theorem (3) Type-2 surface) | Borromean $(\sigma_0 \sigma_1^{-1})^3 \in B_3$, heights $(-,-,-)$ | $0$ | $(m = 0,\; t = +1,\; m - t = -1)$ | $-1$ | **EXACT MATCH** |
| **Control A.2** (Theorem (2) Type-1 surface) | Borromean $(\sigma_0 \sigma_1^{-1})^3 \in B_3$, heights $(+,-,-)$ | $0$ | $(m = -1,\; t = 0,\; m - t = -1)$ | $-1$ | **EXACT MATCH** |
| **Control B** (Yang–Baxter unlink guard) | $\sigma_0 \sigma_1 \sigma_0 \sigma_1^{-1} \sigma_0^{-1} \sigma_1^{-1} = 1 \in B_3$ | $0$ | $(m = +1,\; t = +1,\; m - t = 0)$ | $0$ | **EXACT MATCH** |
| **Control C.1** ($B_3$ $\Delta = 2$ non-zero, both heights) | $(\sigma_0 \sigma_1^{-1})^3 \sigma_0^4 \in B_3$ ($\operatorname{lk}=(2,0,0)$) | $2$ | $(-,-,-): (0, 1, 1)$; $(+,-,-): (-1, 0, 1)$ | $1 \pmod 2$ | **EXACT MATCH** |
| **Control C.2** ($12$-strand ${}^4\text{He}$ cyclic-square non-zero) | ${}^4\text{He}$ base (`neg_branch`) + $(+1,-1,+1,-1)$ at `pos=0, m=1`, triple `(1,2,3)` | $2$ | $m - t \equiv 1 \pmod 2$ | $1 \pmod 2$ | **EXACT MATCH** |
| **Control C.3** ($12$-strand ${}^4\text{He}$ cyclic-square null) | ${}^4\text{He}$ base (`neg_branch`) + $(-1,+1,+1,-1)$ at `pos=20, m=4`, triple `(2,3,4)` | $2$ | $m - t \equiv 0 \pmod 2$ | $0 \pmod 2$ | **EXACT MATCH** |
| **Canonical Carrier Sweep** | `2H, 3H, 3He, 4He, 6Li, 8Be, 10B` (`pos_branch` + `neg_branch`, **606 triples**: 343 at $\Delta=0$, 90 at $\Delta=1$, **173 at $\Delta=2$**) | $0, 1, 2$ | **0** nonzero $\bar{\mu}$; **0** of 173 $\Delta=2$ triples have $t_{ijk}(F) \neq 0$ | **0** nonzero $\bar{\mu}$; **0** mismatches vs Mellor–Melvin | **606 / 606 MATCH (`0` nonzero)** |

### Key Conclusions
1. **Unperturbed Carrier Vanishing Confirmed by Two Exact Reidemeister-Invariant Routes:** Across all 606 triples (and specifically all 173 $\Delta = 2$ one-bit residual triples) of `2H..10B` in both crossing-resolution branches, both Mellor–Melvin's Seifert-surface formula and the exact Wirtinger nilpotent-class-2 longitude expansion yield $\bar{\mu}_{ijk} \equiv 0 \pmod{\Delta}$ with `0` discrepancies.
2. **Geometric Chain-Disjointness Sketch Verified:** Every one of the 173 $\Delta = 2$ triples of the canonical carrier has $t_{ijk}(F) = 0$ on the canonical Seifert surfaces of its $(2, \text{odd})$-torus-knot components, and $m_{ijk}(F) \equiv 0 \pmod 2$.
