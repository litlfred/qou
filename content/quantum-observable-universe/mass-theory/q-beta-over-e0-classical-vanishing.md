**Proposition.** *Let* $\mathfrak{Q}_\beta(q)$ *and* $E_0^{(N{=}0)}(q)$ *be the
substrate closed forms of* [`prop:neutron-qvalue-symbolic`](neutron-qvalue-symbolic.md)
*and* [`rem:beta-decay-energy-scale`](beta-decay-energy-scale.md):*

$$
\mathfrak{Q}_\beta(q) \;=\; m_e \cdot \frac{(2q + 1 - q^2)(q+1)}{2q^3},
\qquad
E_0^{(N=0)}(q) \;=\; \frac{m_e}{q(q-1)}.
$$

*Then the ratio*

$$
S(q) \;\coloneqq\; \frac{\mathfrak{Q}_\beta(q)}{E_0^{(N{=}0)}(q)}
\;=\; \frac{(2q + 1 - q^2)\,(q^2 - 1)}{2 q^2}
$$

*satisfies* $S(q = 1) = 0$ *as an algebraic identity over any
commutative ring.*

## Proof

Direct evaluation:

$$
S(1) \;=\; \frac{(2\cdot 1 + 1 - 1)\,(1 - 1)}{2\cdot 1}
\;=\; \frac{2 \cdot 0}{2} \;=\; 0. \qquad\blacksquare
$$

The substantive content is the algebraic *structure* of the
numerator: $\mathfrak{Q}_\beta$ carries a $(q+1)$ factor, $E_0^{(N=0)}$ carries a
$1/[q(q-1)]$ pole, and their product picks up the $(q^2 - 1) = (q+1)(q-1)$
in the simplified form — so the ratio inherits a $(q-1)$ zero at $q = 1$
that no rearrangement can cancel.

## Consequence for the $c_k$ precision ladder

The shape-collapse audit
[`docs/audits/2026-06-03-qbeta-markov-trace-shape-collapse.md`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-06-03-qbeta-markov-trace-shape-collapse.md)
states *"$c_k$ come from $u_{\text{ladder}}$ Taylor of $S(q) = \mathfrak{Q}_\beta(q)/E_0(q)$"*.
Taken literally, this recipe is **degenerate**: the Taylor expansion of
$S/S(1)$ around $q = 1$ is $0/0$, and the proved $c_2 = -1$ cannot be
recovered.

The resolution is interpretive:

- The $S = \mathfrak{Q}_\beta / E_0$ in the audit doc is the **SDP-constraint
  scalar** (numerical at $q_0$ — the affine target $n_{\text{target}} = S(q_0) \approx 0.18689$
  that the operator-selection program solves for).
- The **$c_k$ ladder normalization** is a different object,
  namely $\mathfrak{Q}_\beta / [Q_A \cdot \cos(\alpha_{\text{eff}})]$, with
  $Q_A$ and $\alpha$ read from the operator-valued $N{=}3$ witness
  (see [`qbeta_1ppq_achieved.py`](https://github.com/litlfred/qou/blob/main/computations/qbeta/qbeta_1ppq_achieved.py)).

This proposition is therefore the algebraic obstruction that pins the
gap and identifies the missing categorical input
($Q_A(q)$ and $\alpha(q)$ symbolic closed forms).

## Two independent routes to the same conclusion

The vanishing $S(1) = 0$ is the *direct-algebraic* witness. An
*operator-theoretic* witness arrives from the SDP strict-complementarity
analysis:

| Route | Diagnostic | Numerics |
|---|---|---|
| **Taylor expansion** ([PR #1769](https://github.com/litlfred/qou/pull/1769)) | $S(1) = 0$; the Taylor series in $u_{\text{ladder}}$ degenerates | $S_{N=0}(q_0) - S_{\text{target}} = 0.168\%$ |
| **SDP strict complementarity** ([PR #1752](https://github.com/litlfred/qou/pull/1752)) | Frobenius Gram indefinite (eigenvalues include $-0.855$); LP min-trace $\neq T_\beta$ selection; selector direction $S$-independent | $Q_A(q_0) = m_e \cdot \lvert q^2 - 2q - 1\rvert (q+1)/(2q^3) = 0.78365\;\text{MeV}$, $\equiv$ CODATA $\mathfrak{Q}_\beta$ to $0.168\%$ with zero CODATA-$\mathfrak{Q}_\beta$ input |

Both routes converge on the same structural conclusion: the bare
substrate scale $Q_A$ predicts $\mathfrak{Q}_\beta$ to $0.168\%$ CODATA-free, and
the remaining sub-ppb correction is the $c_k$ ladder whose
normalization is *not* the SDP-constraint scalar $S = \mathfrak{Q}_\beta/E_0$.
