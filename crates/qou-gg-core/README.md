# `qou-gg-core`

Lightweight, pure-Rust (`#![forbid(unsafe_code)]`, zero C-FFI, `wasm32`-compatible) foundational algebra crate built on [`gs-basis`](../gs-basis) for the ruled $\gamma\gamma$ interaction model and $(Z, N)$ atomic-chart construction.

## Scope & Layering

`qou-gg-core` provides **only** the exact algebraic and combinatorial primitives (no numerical floating-point evaluation, no C-FFI solvers, and no exploratory probe censuses, which layer cleanly on top of this crate):

1. **Ruled 4-Term Photon & $k$-Photon Collision Engine (`photon`)**
   - `Photon4Term<R>`: $\gamma^{(s)}(\phi_0, \phi_1, \phi_{01}) = \mathbf{1} + \phi_0\sigma_s + \phi_1\sigma_{s+1} + \phi_{01}\sigma_s\sigma_{s+1}^{-1}$ at any strand offset $s \ge 0$, with chiral eigen-photons $\gamma_+^{(s)} = \gamma^{(s)}(0, 0, qh)$ and $\gamma_-^{(s)} = \gamma^{(s)}(0, 0, -q^{-1}h)$ satisfying $\gamma_+^{(0)}\gamma_-^{(0)} = V_0^3 = \beta_{\mathrm{Bor}}$ in $H_3(q)$ ($h = q - q^{-1}$).
   - `k_photon_product` & `four_photon_product`: exact $4^k$ signed-braid expansion and streaming Gröbner–Shirshov reduction through 4-photon ($4^4 = 256$ monomials), plus whole-word linking-neutral projection.

2. **Whole-Word Linking-Neutrality Cut (`u1_neutral`)**
   - Exact port of `QOU/StandardModel/PhotonU1NeutralCut.lean` generalized to $n \ge 2$ strands (`closure_components`, `self_writhes`, `pairwise_linkings_twice`, `writhe`, `is_linking_neutral` / `is_u1_neutral`).

3. **Hadron Words & Crossing-Local Quark-Charge Dressings (`hadron`)**
   - Bare Borromean baryon $\beta_{\mathrm{Bor}} = V^3$, typed `uud` ($\mathfrak{p}$) and `udd` ($\mathfrak{n}$) flavour assignments, charged pion $\pi^\pm = \sigma_0^2 \in H_2(q)$, electron Hopf word $\sigma_0\sigma_1\sigma_0 \in B_3$, and exact symbolic $3\times 3$ weight-space matrices $L_p, L_n, M_p, M_n$ (`QOU/Nuclear/NucleonChargeDressedWords.lean`).

4. **Deterministic $Z = 0\ldots 118$ `T3` + Hopf Atomic-Chart Generator (`atomic_chart`)**
   - Exact $O(A)$ Class-1 proper 3-edge-coloured inter-nucleon bond graph constructor matching `QOU/MassTheory/NucleusBondValence.lean` ($M_{\mathrm{T3}}(A) = \min(\binom{A}{2}, 3\lfloor A/2 \rfloor)$ for $A \ge 3$ and $1$ at $A = 2$), intra-nucleon $V^3$ placements on $3A$ quark strands, and $Z$-electron Madelung `2n²` Hopf shell placements, serializable to JSON via `AtomicDatum`.
   - Anchor note: numerical evaluations built downstream of `qou-gg-core` pin the aether parameter $q_0$ strictly at the physical proton anchor (muon pin on hold per 2026-11-28 owner ruling).
