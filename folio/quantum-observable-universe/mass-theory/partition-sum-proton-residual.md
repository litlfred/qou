*Let $\mathfrak{m}^{\mathrm{tower}}(\mathfrak{p}, q_0)$ be the pure-tower proton mass. The proton tower residual equals the electron mass times the inverse-quantum-dimension sum over partitions of $3$:*

$$
    \Delta m_{\mathfrak{p}}
    \;:=\;
    m_{\mathfrak{p}}^{\mathrm{CODATA}} - \mathfrak{m}^{\mathrm{tower}}(\mathfrak{p}, q_0)
    \;\overset{?}{=}\;
    m_e\sum_{\lambda\vdash3}\frac{1}{\dim_q\lambda}
    \;=\;
    m_e\Bigl(2 + \frac{1}{[2]_q}\Bigr).
$$

The second equality is proved, as a formal sum, in [`prop:h3-frobenius-casimir-markov-trace`](#prop:h3-frobenius-casimir-markov-trace) (item 4). The same proposition shows that this sum is not the Markov trace of the Frobenius Casimir of $H_3(q)$: under convention D that trace is $(q^4+q^2+1)(q^6+q^4+q^2+5)/(q^2+1)^2$, which is $6$ at $q=1$ where the sum is $5/2$. The element $C_{\dim_q}$ whose trace is the sum is built to have that trace, and under convention D it is undefined because the $(1^3)$ block has Markov weight $0$; the sum over the surviving blocks is $1+1/[2]_q$. The earlier statement that "the Markov trace of the co-Casimir element analytically simplifies to the sum over partitions of inverse quantum dimensions" is therefore withdrawn.

**Comparison (empirical; not part of any proved statement).** At $q_0$, $m_e(2+1/[2]_{q_0})=1.2761$ MeV, and the classical value $(5/2)\,m_e=1.2775$ MeV.

The tower that production uses is fixed by the proton identity

$$
  \frac{m_{\mathfrak p}}{m_e} \;=\; 2\,\frac{\mathrm{Vol}(4_1)}{\hbar_q^2}\,F_{\mathrm{Bor}}(q) \;-\; 12,
  \qquad
  F_{\mathrm{Bor}}(q) = \frac{|\mathrm{tr}_M(\beta_{\mathrm{Bor}})|\,[3]_q!}{q^3},
$$

whose Borromean weight $y_{(2,1)} = 1/[2]_q^2$ forces $z = q^3/(q^2+1)$, so it is convention D. Its tower term is $\mathfrak{m}^{\mathrm{tower}} = 2\,m_e\,(\mathrm{Vol}(4_1)/\hbar_q^2)\,F_{\mathrm{Bor}}$, and the residual against it is:

| pin | $q_0$ from | $\mathfrak{m}^{\mathrm{tower}}$ (MeV) | $\Delta m_{\mathfrak p}/m_e$ | $m_{\mathfrak p}$ (MeV) |
|---|---|---|---|---|
| proton | the identity above, solved with CODATA $m_{\mathfrak p}/m_e$ | $944.404$ | $-12$ (by construction) | $938.272089$ (round trip) |
| muon | $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$, CODATA 2022 | $944.404$ | $-11.99955$ | $938.271861$ ($-244$ ppb) |

At the proton pin the residual is $-12\,m_e$ exactly, because $q_0$ is defined by the identity. It is not a measurement. The muon pin is the only one at which $m_{\mathfrak p}$ is tested. The residual is negative, and its size is set by the constant $12$ in the identity rather than by a partition sum. The integer $12$ is fitted. It was selected because $2\,m_\mu F_{\mathrm{Bor}}(q_0)$ exceeds the measured $m_{\mathfrak p}$ by about $12\,m_e$, and no derivation of a $-12\,m_e$ term is on record. It is one discrete parameter chosen against the target. The factorisations $12 = \dim V_{(2,1)}\cdot|S_3| = 2\cdot 6$ and $12 = 2F_{\mathrm{Bor}}(1)$ are readings of the integer, not derivations of it. Because integer multiples of $m_e$ are spaced about $545$ ppm of $m_{\mathfrak p}$ apart, the nearest integer always lies within about $272$ ppm. A miss of $244$ ppb at the muon pin is therefore about $10^{-3}$ likely by chance alone, before the choice of the formula's other factors is counted.

Two earlier residuals were measured against towers that no live producer reproduces. These are the archived corrected tower $936.994$ MeV (Table 4), giving $+1.278$ MeV, and the literal $938.7228$ MeV, held only in Lean files, giving $-0.451$ MeV. Neither tower is the convention-D tower above. The near-match of $+1.278$ MeV with $m_e(2+1/[2]_{q_0})$ exists only against the archived value, and there the classical $(5/2)\,m_e$ is closer ($0.03\%$) than the $q$-form ($0.14\%$). Against the live tower, neither sum is close to the residual.
