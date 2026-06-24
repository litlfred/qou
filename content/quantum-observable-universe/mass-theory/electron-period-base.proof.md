**Proof.** The prolonged Seiberg--Witten periods obey the one-parameter
recurrence
$$
a_D^{(n+2)} = \tau\,a_D^{(n+1)} - a_D^{(n)}
$$
([`prop:sl2-prolongation-recurrence`](#prop:sl2-prolongation-recurrence)),
a second-order linear recursion with constant coefficient $\tau$. Such a
recursion is determined by its two lowest terms together with $\tau$:
every $a_D^{(n)}$ with $n \geq 2$ is a $\mathbb{Z}[\tau]$-linear
combination of $a_D^{(0)}$ and $a_D^{(1)}$, obtained by iterating the
recurrence.

The $n = 0$ term $a_D^{(0)}$ is the *unprolonged* period — the **electron
period** $a_D^{(e)}$ — by
[`prop:jet-sw-tau-decomposition`](#prop:jet-sw-tau-decomposition) ("the
$n=0$ term is the electron period"). Calibration CAL-1 identifies it with
the leptonic scale, $a_D^{(e)} = m_e$. Hence the entire tower is generated
from the triple $(m_e,\,a_D^{(1)},\,\tau)$, with $m_e$ entering as the
**base** term of the recursion; this is the Lean witness
`QOU.Mass.electron_period_is_base`.

That $m_e$ propagates into *every* higher period — rather than sitting as
an external multiplicative prefactor — is seen already at $n = 2$. Setting
$n = 0$ in the recurrence gives
$$
a_D^{(2)} = \tau\,a_D^{(1)} - a_D^{(0)} = \tau\,a_D^{(1)} - m_e ,
$$
in which the electron scale appears explicitly and additively; this is the
Lean witness `QOU.Mass.second_period_contains_me`. By induction on the
recurrence the same dependence carries to all $n \geq 2$. Thus $m_e$ is the
base period of the tower, which is the cohomological content of CAL-1 as
the scale ($h^0$ datum) of the rank-2 $W$-Hodge plane. $\blacksquare$
