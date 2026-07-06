**Proposition (the self-dual Higgs has a real complex volume).**
*The figure-eight knot $4_1$ — the Higgs (mass mechanism) — is **amphichiral**. It equals its own mirror, so its colored Jones polynomial is fixed under the bar-involution $\sigma\colon q \mapsto q^{-1}$*:

$$
  J_N(4_1; q) = J_N(4_1; q^{-1}) \qquad (\forall N).
$$

*Consequently, its Neumann–Zagier complex volume $\mathbb{V}(4_1) = \mathrm{Vol}(4_1) + i\,\mathrm{CS}(4_1)$ is **real**:*

$$
  \mathrm{CS}(4_1) = \mathrm{Im}\,\mathbb{V}(4_1) = 0,
  \qquad
  \mathrm{Re}\,\mathbb{V}(4_1) = \mathrm{Vol}(4_1) \approx 2.0299.
$$

*The bare Higgs knot therefore contributes **only the real (volume / mass) face** — the muon mass scale $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$ — and its imaginary (decay) face vanishes. Thus, $\mathfrak{Q}_\beta$ is **not** a property of the lone Higgs knot.*

Where the decay face does live is conjectural: per [`conj:binding-qbeta-complex-volume`](../mass-endomorphism/binding-qbeta-complex-volume.md), $\mathfrak{Q}_\beta$ is the imaginary part of the many-body **binding defect** $\mathfrak{V} = E_0\,\mathrm{tr}_M((\Pi_{\text{free}}-\mathbf{1})\circ\mathcal{M})$. That identification is not part of this proposition.

## The Askey two-saddle structure

Torus knots and hyperbolic knots form the two archimedean saddles of one quantum A-polynomial $\hat A_K$ (the AJ machinery, [`phi-q-aj-machinery-identification`](../stochastic-mechanics/phi-q-aj-machinery-identification.md); the strong AJ conjecture holds for $4_1$ \cite{nguyen-tran-2021}):

| | torus knots (leptons) | hyperbolic knots (Higgs $4_1$) |
|---|---|---|
| Askey object | Rogers $q$-ultraspherical | non-compact Askey-Wilson \cite{koelink-stokman-2003} |
| dilog regulator | Rogers $\mathrm{Li}_2^q$ | Faddeev $\Phi_q$ |
| archimedean saddle | real $q\in(0,1)$ | root of unity $q=e^{2\pi i/N}$ |
| bar-parity | bar-even ($\cosh$) | bar-odd ($\sinh$) recovered only when chiral |

For the amphichiral $4_1$, both saddles collapse onto the real axis (the bar-odd part vanishes). This explains why the volume-conjecture sum $\langle 4_1\rangle_N$ is real and grows at the rate $\mathrm{Vol}(4_1)$ (Kashaev \cite{kashaev1997}, Murakami–Murakami \cite{murakami-murakami2001}), with no Chern–Simons phase.

## What is proved, and over which ring

The self-duality $\Rightarrow$ vanishing-imaginary-face implication is an **algebraic identity over any commutative ring with a bar-involution** $\sigma$. It is not restricted to $\mathbb{C}$ (the archimedean instance is $\sigma =$ complex conjugation). It is Lean-formalised sorry-free (`QOU.Knot.SelfDuality.higgs_complex_volume_real`): a $\sigma$-fixed element has a zero bar-odd part and a bar-even part $2V$. The same file proves the **recurrence descent** — one three-term recurrence with a bar-even multiplier yields both parity ladders (the $c_k$ engine).

The hyperbolic-volume value $\mathrm{Vol}(4_1)$ itself (the saddle limit) is the volume conjecture, proved in the literature but not in Mathlib. It is carried as the conditional class `QOU.Knot.FigureEightVolume.VolumeConjecture41`. The Kashaev sum's non-vanishing floor ($\langle 4_1\rangle_N \ge 1$) is proved sorry-free.
