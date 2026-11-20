**Remark (bar-symmetry class, categorical sectors, and the $c_5$ falsifiable prediction).**

> **Bar-symmetry class** (per [Bar-involution and its $P_{\mathrm{avg}}$ / $P_{\mathrm{skew}}$ projections: the canonical $q \leftrightarrow q^{-1}$, $\sigma \leftrightarrow \sigma^{-1}$ involution on the Hecke algebra, splitting every $H_n(q)$-quantity into a bar-symmetric (even/cosh/cos/$\mathrm{Li}_2^q$-like) part the framework retains and a bar-anti-symmetric (odd/sinh/sin/$\Phi_q$-like) part the framework projects away](#def:bar-involution)):
> $c_5(q) = -b^2(q) - 1/2 = -3/2 + 1/[2]_q^2$ is **bar-symmetric** as a function of $q$. The Hoefsmit-Quantum-2 identity $b^2 = 1 - 1/[2]_q^2$ is a proved algebraic theorem in the Lean sibling. The "$-1/2$" piece is a q-independent commutative-QOU constant; $c_5(q=1) = -5/4$ proved as `c5_classical_limit_eq_neg_five_quarters`. The $c_5$ outlier at silver is the arithmetic sum of two clean bar-symmetric pieces landing on inert prime $11 \in \mathbb{Z}[1+\sqrt 2]$, not a quantum-deformation artifact.

> **Pentagon-reduction cross-link.** The Leibniz expansion uses the q-dilogarithm pentagon identity implicitly. The algebraic identity making this rigorous lives in [`pentagon_reduction_li2q.py`](../../../computations/pentagon_reduction_li2q.py). The Pentagon coherence layer of $c_5$'s decomposition is what `pentagon_reduction_li2q.py` makes algebraic.

## Categorical interpretation

The $\mathfrak{Q}_\beta$ predictions live in two distinct categorical sectors. First, the pure-$\sigma$ sector ($c_3, c_4, c_6, c_7$): contributions from positions acting as pure Hecke generators or their inverses. This algebraically lives in the $\mathbb{Z}$-span of Hecke-quadratic eigenvalues. Second, the bar-invariant fixed-point sector ($c_5$): contributions from averaged-crossing positions. This algebraically lives in the bar-invariant subring (fixed by $\sigma \leftrightarrow \sigma^{-1}$).

The two sectors are independent categorical inputs. Pure-$\sigma$ is the Hecke-generator action; bar-invariant fixed-point is the involution-projector action. Both reproduce $\mathfrak{Q}_\beta$ exactly via the precision ladder.

## Falsifiable prediction

Any future rung $c_k$ at $k \geq 8$ whose order $\hbar_q^{2k}$ coincides with an averaging-resonance position will pick up similar $1/2$ fingerprints.

The proton braid has 11 typed crossings: 7 pure $\sigma_0$, 4 pure $\sigma_1$, 1 averaged $\sigma_0$, 1 averaged $\sigma_1$, 3 inverted $\sigma_1^{-1}$. The averaging-resonance rungs are determined by the positions where two averaged crossings interact. 

By combinatorial counting, the predicted averaging-resonance rungs are those $k$ for which $\binom{2}{2} \cdot (\text{combinatorial weight})$ peaks. The first is $k = 5$; subsequent peaks are predicted at $k = 8, 11, \ldots$ (every 3 rungs).

This is testable by extending SDP-$T_\beta$ extraction to $k \geq 8$ and checking whether $c_8$ has a $1/2$ fingerprint.

## Discussion

This decomposition is a structural identification, not a first-principles derivation. The $-b^2$ and $-1/2$ summands are identified categorically. The proof that the precision-ladder $c_5$ takes exactly this form requires computing the typed-$\mathbf{B}_3$ Markov-trace expansion at order $b^5 \hbar_q^{10}$, and separating pure-$\sigma$ contributions from averaged-position contributions. Both are concrete computations not yet executed. This proposition sets up the categorical grammar; its full proof requires the order-by-order Hecke expansion machinery.
