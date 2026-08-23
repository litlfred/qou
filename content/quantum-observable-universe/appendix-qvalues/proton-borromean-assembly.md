**Conjecture (proton Borromean mass assembly).**
*The proton mass assembles from the Borromean categorical observable
$F_{\mathrm{Bor}}$ ([`def:f-bor-borromean-observable`](../braids-and-knots/f-bor-borromean-observable.md))
according to*

$$
  m_p \;=\; \mathrm{mult} \cdot \bigl(m_\mu \cdot F_{\mathrm{Bor}}(q_0) \;-\; \mathrm{bind} \cdot m_e\bigr),
$$

*where the two structural integers are the categorical invariants of $H_3(q)$:*

- *the **constituent multiplicity** $\mathrm{mult} = \dim V_{(2,1)} = 2$, the dimension of the trace-dominant Hecke irrep, and*
- *the **per-constituent electron-binding count** $\mathrm{bind} = |S_3| = 6$ (so $12 = \mathrm{mult}\cdot\mathrm{bind} = 2\cdot 6 = |S_3|\cdot\dim V_{(2,1)}$).*

## Status: open categorical bridge

The numerical identity $m_p = 2\,m_\mu F_{\mathrm{Bor}}(q_0) - 12\,m_e$ is verified to $0.24\,\mathrm{ppm}$ at 50-dps MPFR, and each factor has an established categorical *identification*:

- $F_{\mathrm{Bor}}(q) = |\mathrm{tr}_M(\beta_{\mathrm{Bor}}, q)| \cdot [3]_q!/q^3$ is the Borromean Markov-trace observable (categorical, [`def:f-bor-borromean-observable`](../braids-and-knots/f-bor-borromean-observable.md));
- the transpose-pair identity $y_{(3)}(q)\cdot y_{(1,1,1)}(q) = 1/[3]_q!^2$ is Lean-proved;
- the integer $12 = 2\cdot 6 = \mathrm{mult}\cdot\mathrm{bind}$ is a categorical count ($|S_3|\cdot\dim V_{(2,1)}$). An earlier identification of it as the inverse of an Ocneanu leading-pole coefficient $-\tfrac{1}{12}$ was **refuted for $\beta_{\mathrm{Bor}}$** — whose Markov trace has a $q^{-4}$ pole of coefficient $1$, not the $q^{-10}\cdot(-\tfrac{1}{12})$ of the measured no-interface braid (retracted 2026-05-25; re-confirmed in the 2026-08-22 F_Bor red-team audit) — and is not part of the derivation.

What remains **conjectural** is the *bridge* from these identifications to the assembly law above — specifically why the trace-dominant irrep's dimension $\dim V_{(2,1)}$ enters as a **linear** multiplier and $|S_3|$ as the electron-binding count. The Wedderburn block expansion of the Markov trace (the $(2,1)$ block carries $\approx 49\%$ of the proton's $T_1$ contribution) is the natural framework, but the formal categorical statement is pending.

The conjecture is axiomatised as the Lean class `QOU.AppendixQValues.ProtonBorromeanAssembly`: its fields are exactly these hypotheses (the two structural integers and the factored assembly law), and [`prop:proton-mass-substrate-identity`](proton-mass-substrate-identity.md) derives the published flat identity from them, sorry-free modulo the class instance.
