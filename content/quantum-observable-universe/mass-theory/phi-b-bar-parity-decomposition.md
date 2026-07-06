# Bar-parity (sinh/cosh) decomposition of the modular double

**Proposition.** *Let $R$ be a commutative ring and $\sigma\colon R\to R$ a
ring involution (the modular double $b\mapsto b^{-1}$, equivalently the bar
$q\mapsto q^{-1}$). For every $f\in R$,*

$$
2f \;=\; \underbrace{(f+\sigma f)}_{\text{bar-even}} \;+\; \underbrace{(f-\sigma f)}_{\text{bar-odd}},
\qquad
\sigma(f+\sigma f)=f+\sigma f,\qquad \sigma(f-\sigma f)=-(f-\sigma f).
$$

*The bar-even part is fixed by $\sigma$; the bar-odd part is negated. The
decomposition is unique and holds over any commutative ring.*

## Interpretation

This is the algebraic core of the **sinh/cosh split** on the Faddeev
modular double. The Faddeev non-compact quantum dilogarithm $\Phi_b$ is
modular-invariant, $\Phi_b=\Phi_{b^{-1}}$, so its logarithm decomposes under
$\sigma$ into a bar-even ($\cosh$) part and a bar-odd ($\sinh$) part.

Conditional on the complex-volume conjecture `conj:binding-qbeta-complex-volume`,
the two parts are the two faces of the complex volume
$\mathfrak V=\mathrm{Vol}+i\,\mathrm{CS}$:

- **bar-even ($\cosh$)** $=\ \mathrm{Re}\,\mathfrak V$ — the hyperbolic
  volume / **mass** face, evaluated on the real-$q$ (Rogers) saddle;
- **bar-odd ($\sinh$)** $=\ \mathrm{Im}\,\mathfrak V$ — the Chern–Simons /
  **decay** ($\mathfrak Q_\beta$) face, carried on the root-of-unity
  (Faddeev) saddle.

The mathematical statement above is **unconditional**; only this physical
identification of the two parts invokes the conjecture.

## Consequence for the $c_k$ ladder

Because the two parts live on the two archimedean saddles, a coefficient's
**bar-parity predicts its anchor-behaviour**: bar-even coefficients are
real-$q$ and **anchor-stable**, bar-odd coefficients are root-of-unity and
**anchor-dependent**. This is confirmed on both available rungs —
$c_2=-1$ (bar-even) is Taylor-exact, $c_3$ (bar-odd) swings $\approx 2.375\%$
between the proton and muon anchors — so the ladder element factors as
$F(q)=F_{\text{even}}(q)\cdot F_{\text{odd}}(q)$ with $F_{\text{odd}}$ the
modular-double ($\Phi_b$) factor. (Scan:
`computations/qbeta/qbeta_fmap_parity_stability_probe.py`; accuracy audit:
`docs/audits/2026-07-06-qbeta-faddeev-phi-b-modular-double-accuracy.md`.)
