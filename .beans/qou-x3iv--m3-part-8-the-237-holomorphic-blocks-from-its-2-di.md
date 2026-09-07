---
# qou-x3iv
title: 'M3 Part 8: the (-2,3,7) holomorphic blocks from its 2-dim state integral (GK q-series route) — the tranche that answers item 1'
status: in-progress
type: task
priority: normal
tags:
    - g3-aomega
    - route-c
created_at: 2026-09-07T19:24:33Z
updated_at: 2026-09-07T19:31:36Z
---

Owner 'Merge and go' 2026-09-07. Sibling of qou-m3ad / qou-rtec (both are tasks; a task cannot parent a task). Goal: the pretzel's holomorphic blocks B^alpha(x;q) (7 of them, level 2) from the m016 state integral, evaluated as q-series by the Garoufalidis-Kashaev residue method (held: arxiv-1304.2705v1 — 1-dim I_{A,B} family proved, multi-dim stated as 'well known to experts' without a general theorem; arxiv-1411.6062v2), CERTIFIED against the derived rotated-index family (aomega_m3_rotated_index_three_knots_probe) via GGM eq 19. Then S^+(x;0) in GGM's normalisation and item 1 runs. Inputs on hand: SnapPy m016 NZ data (3 tets, 2 obstruction classes, Ptolemy fields c^3-c-1 and c^3+4c^2+3c-1). Honest boundary: the 4_1 corpus instance is 1-dim; the pretzel is 2-dim and level 2 — GZ §4.2 declined it. Do not transcribe; derive and certify.

SOURCE SURVEY 2026-09-07 (before any computation). Held: GK 1304.2705 (Theorem 1.1: the 1-dim family I_{A,B}(b) = int Phi_b(x)^B e^{-A pi i x^2} dx, B > A > 0, as q-series F_{A,B}(q,x) = sum_m (-1)^{Am} q^{A m(m+1)/2} x^m/(q;q)_m^B with F~_{A,B} = F_{B-A,B}; multi-dim case stated as known to experts, NO general theorem), GK 1411.6062, Dimofte-Garoufalidis 1202.6268 (quantum content of the gluing equations), Nimershiem 2108.09349 (geometric triangulations of (-2,3,n) pretzel complements), GGM 2012.00062 §7 (1-dim state integrals and descendants), GGMW-type 2312.00624 (wave functions; examples 4_1 and 5_2 only). NOT held: Andersen-Kashaev TQFT, BDP14 holomorphic blocks, Garoufalidis-Koutschan pretzel A-hat. GZ 2111.06645 §8.2 worked the pretzel only at roots of unity (units, prefactors S_K(alpha)), not q-series blocks.

HYPOTHESIS H-I23 (unverified; do NOT upgrade without the certification below): the 5_2 state integral is I_{1,3} (GK §3), whose q-series are F_{1,3} (= GGM's H^- tower, (-1)^n q^{n(n+1)/2}/(q)_n^3) and F~_{1,3} = F_{2,3} (= GGM's H^+ tower, q^{n(n+1)}/(q)_n^3). The (-2,3,7) pretzel is the 5_2 SISTER (same volume 2.8281, same trace field c^3-c-1); the natural candidate is I_{2,3} = int Phi_b^3 e^{-2 pi i x^2} (B=3 > A=2 > 0, in GK's family), i.e. the SAME two towers with the q and q~ roles swapped. If true, GK Theorem 1.1 gives the pretzel's blocks EXPLICITLY (F_{2,3} on the q side, F_{1,3} on the q~ side) with the operator P_{2,3}, and GZ §4.2's 'no explicit formula' concerns a different object. CERTIFICATION (the only admissible upgrade): the blocks so obtained must reproduce the DERIVED rotated-index family Ind^rot_{m016}(m,zeta;q) (aomega_m3_rotated_index_three_knots_probe, exact to q^3) through GGM eq 19. A memory-reconstructed prescription is not evidence; the index is.

LABEL CORRECTION (same hour): GK 1304.2705 §1.3 states I_{1,2} = I_{4_1} and I_{2,3} = I_{5_2}; GGM 2007.10190 App. A writes the 5_2 state integral as I_{2,3,lambda,mu}. So 5_2 is (A,B) = (2,3), NOT (1,3) as H-I23 said; the q~-partner is F~_{2,3} = F_{1,3}. The sister candidate for (-2,3,7) is therefore the OTHER member, (A,B) = (1,3): int Phi_b^3 e^{-pi i x^2} (B=3 > A=1 > 0), i.e. the same two towers with q and q~ swapped — still a HYPOTHESIS, to be DERIVED from m016's NZ datum via the held DG 1202.6268 state-integral prescription and certified against the index. GGM 2012.00062 §7 gives the general 1-dim family Z_{A,r}(u,t;tau) = int prod_{j<=r} Phi_b(v+u_j) e^{-A pi i v^2 + 2 pi i v t} dv with its factorisation in G_{A,r}(y,z;q); 5_2 is (A,r)=(2,3), u=(0,u,-u). If m016 reduces to (A,r)=(1,3) with some u-configuration, its blocks are explicit and held.
