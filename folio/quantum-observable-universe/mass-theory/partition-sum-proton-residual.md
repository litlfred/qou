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

**Comparison (empirical; not part of any proved statement).** At $q_0$, $m_e(2+1/[2]_{q_0})=1.2761$ MeV, and the classical value $(5/2)\,m_e=1.2775$ MeV. The residual depends on which tower mass is used, and the recorded tower values do not agree:

| tower value used | $\mathfrak m^{\mathrm{tower}}$ (MeV) | $\Delta m_{\mathfrak p}$ (MeV) |
|---|---|---|
| archived corrected tower (Table 4) | $936.994$ | $+1.278$ |
| current Lean pin `protonTowerMass` | $938.7228$ | $-0.451$ |

Only the archived value gives a residual near $+1.28$ MeV; the current pin gives the opposite sign. Against the archived value the classical $(5/2)\,m_e$ is closer ($0.03\%$) than the $q$-form ($0.14\%$), so the comparison does not single out the $q$-deformed sum. The relation is a comparison against one recorded number, not a derived equality.
