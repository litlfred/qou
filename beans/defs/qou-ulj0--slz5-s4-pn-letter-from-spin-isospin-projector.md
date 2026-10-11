---
# qou-ulj0
title: 'slz5 S4: pn letter from a spin x isospin projector (S=1, T=0)'
status: todo
type: task
priority: normal
created_at: 2026-10-10T15:10:00Z
updated_at: 2026-10-10T18:30:00Z
parent: qou-slz5
---

Stepping stone 4. OPEN. Builds on qou-kj4v (T, not content, selects the channel) and qou-q8vl (escape needs d_pn outside [d_nn, d_pp] or a non-monotone law).

**Idea (judgement, untested).** Build the pn bond from the spin x isospin projector on a doubled strand: S=1, T=0 for the deuteron, S=0, T=1 for pp/nn/pn singlet. This leaves the one-letter H_2 family {sigma + d}, so neither the averaging bar nor the monotone bar applies, and it targets the Pauli-lock degeneracy directly. Required: letters valid on the faithful window 0 <= z <= h, derived, not chosen against AME.

Test: the two-nucleon ordering pn bound, pp and nn unbound (= the sign-mixed chain pattern that gives b3 > 0, qou-q8vl). No path in the six-path grep shows this attempted.

## 2026-10-10 — narrowed by a structural exclusion (PR #7612, bc7606cf6f4)

`QOU.Hecke.ChannelSwapSplitting.tr_swap_sub` (sorry-free, generic CommRing): for any trace and degree-one letters a + b·c on carriers c1 (isospin), c2 (spin),
tr(f(c1) g(c2)) - tr(g(c1) f(c2)) = (a1 b2 - a2 b1)(tr c2 - tr c1).
A Markov trace has tr sigma_i = z for every i, so the deuteron (S=1,T=0) and singlet (S=0,T=1) are EXACTLY degenerate when spin and isospin each ride on one generator, adjacent or far. Scope (b), invariant tr c1 = tr c2; converse over a domain. Exact H_4 check: (s1,s2) and (s1,s3) give 0; (s1, s2 s3 s2) gives h z^2 (a1 b2 - a2 b1).

Surviving door: carriers with UNEQUAL traces (e.g. a crossing over a third strand, tr(s2 s3 s2) = z + h z^2). Open: a derived (not chosen) reason spin and isospin ride on carriers of different length, or the 3S1-3D1 tensor/space index of qou-kj4v. Stays open.

## 2026-10-10 — option 1 (derive a carrier asymmetry from the 3-quark geometry): scope (a) negative

In six-quark Schur–Weyl language a two-nucleon spin S is the two-row diagram (3+S, 3−S), and the same holds for isospin T. So the deuteron is spin (4,2) ⊗ isospin (3,3), and the singlet is spin (3,3) ⊗ isospin (4,2). Within one nucleon both spin and isospin are the mixed (2,1) block on the SAME three quark strands. The geometry therefore gives spin and isospin identical data: both are SU(2) doublets on identical strands. If each factor is weighted by a Markov trace, the deuteron/singlet weight ratio is r(z_spin)/r(z_iso), where

r(z) = w(4,2)/w(3,3) = (q²−q+1)²(q²+q+1)²(q⁵z+q³z+qz+1) / [q²(qz+1)(q⁴−q³+q²−q+1)(q⁴+q³+q²+q+1)]

(sympy, from the Ocneanu closed form). r is increasing in z: 1.4404 at 0, 1.8522 at h/2, 2.1864 at h, 3.0437 at z_D. A split therefore needs z_spin ≠ z_iso. Nothing in the 3-strand geometry supplies that difference, and choosing it would be a fit.

Physics reading: this is Wigner SU(4) spin–isospin symmetry. The S-wave pair lies in the SU(4) antisymmetric 6, which contains (S,T) = (1,0) and (0,1). The letters respect SU(4), so they cannot split the deuteron from the singlet. In nature that splitting is SU(4)-breaking, and the tensor force (spin coupled to orbital angular momentum, not to isospin) supplies it. Corpus: folio/.../nuclear-interactions/audit/wigner-su4-alpha-cluster-probe.md already uses SU(4) as the shell organiser.

Next door (judgement): the space/tensor index of qou-kj4v, i.e. the ³S₁–³D₁ mixing. It distinguishes spin from isospin by construction. This bean stays open.

## 2026-10-10 — framing twist (commit 7c4a10f55e2, PR #7612)

Result: a central twist acting by scalars s, s' (spin, on blocks (4,2),(3,3)) and i, i' (isospin) gives
D − S = (s·i' − s'·i)·tr p·tr p'.
- Symmetric twist (same on both factors, as the ribbon axioms give inside one category): D = S exactly. Scope (b), invariant s·i' = s'·i.
- Spin-only ribbon twist θ_λ = q^{c(λ)}: D − S = (q⁵ − q³)·w₄₂·w₃₃, zero iff q² = 1; D/S = q₀² = 1.2321 (full twist q₀⁴ = 1.5180), z-independent. Two-row law c = S(S+1) + n(n−4)/4 makes the ratio parameter-free.
- ASSUMED, not derived: that the twist acts on spin and not isospin (Lean hypothesis θ_iso = 1 in `spin_only_twist_split`). No corpus or library source derives it; Finkelstein–Rubinstein needs Lorentz invariance as input.
- Open: sign of the energy splitting (trace→energy map, Δ² vs Δ⁻²) and exponent normalisation (k = 1 vs 2).
Files: QOU/Hecke/TwistedChannelSplitting.lean (exit 0, no sorry); computations/deltalambda/framing_twist_channel_split_probe.py (6/6).
Status stays todo: the spin/isospin asymmetry is still underived.

## 2026-10-11 — is theta_iso = 1 derivable? Mostly NO (commit 8e8c2fdeb94, PR #7612)

Lean QOU/Hecke/IsospinTwistFromBalancing.lean (exit 0; axioms propext/Classical.choice/Quot.sound). Balancing theta_{X⊗Y} = c_{Y,X}c_{X,Y}(theta_X⊗theta_Y) fixes the isospin twist from the isospin braiding; the block-level form theta|_lambda = tau^n f_lambda is carried as a hypothesis [bakalovkirillov2001, turaev2010].
- Spin Hecke-braided at q, isospin at t: D − S = sigma^6 tau^6 q^6 t^6 (q^4 − t^4) tr p tr p' (hecke_balanced_split; needs JucysMurphySpectrum for (4,2), (3,3)).
- The corpus grades isospin by the P± of the SAME H_n(q0) (audit 2026-08-16 §4), so t = q and D = S. In the corpus's own structure theta_iso = 1 contradicts balancing. Scope (b) for that structure; the invariant is balancing + q^4 = t^4.
- The spin-only form follows iff isospin is transparent (Müger centre), which under Hecke braiding is iff t^2 = 1 (classical). No corpus structure makes isospin classical. That would need C_spin ⊠ Rep(SU(2)), which also breaks the shared-trace Pauli lock.
- Convention correction: with Delta^2 = theta^2 (fullTwist_eq_theta_sq) the balancing ratio is q^4, so spin-only D/S = q0^4 = 1.517953. The earlier q0^2 used theta = q^c, half the balancing twist. TwistedChannelSplitting must say which twist it means.
Verdict: the spin/isospin split is NOT derivable from the present structure. Status stays todo.

## 2026-10-11 — sign of the split: NOT fixed by the corpus (commit c7c36cf576b, PR #7612)

sign(D − S) = sign(s − s') (block traces positive at z_D). Two unfixed signs multiply:
- Twist orientation: Delta^2 = (sigma_1…sigma_5)^6 acts by q^{+2c} (fixed), but whether a spin-only insertion is Delta^2 or Delta^-2 is free; strand-twist-datum's framing t ∈ Z is a free label.
- Trace→energy map: all working forms (−alpha ln mu, B_sym, m ∝ |tr_M|) are antitone and POSITED (dashboard tag: "no block licenses alpha ln(ratio) as an energy"). m_e Σ y chi Delta_lambda is not monotone here (Delta_(4,2) = +9, Delta_(3,3) = −5).
Four cells proved conditional in Lean (TwistSplitSignDictionary.lean). Log form: B_D − B_S = −2·orient·k·alpha·ln q0 = ∓0.8735 MeV (ribbon) / ∓1.7471 MeV (full twist). Nature agrees with (θ^-1, antitone) or (θ, monotone): labelled comparison only, not a selection.
Moot while theta_iso = 1 is underivable (entry above).
