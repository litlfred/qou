**Proposition (spectral form of $F_{\mathrm{Pauli}}$).**
*Working over $R = \mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$, the
Pauli statistical weight appearing in nuclear $Q$-value formulas
([mass-formula validation](#rem:mass-formula-validation)) is the ratio
of Wedderburn-block traces*

$$
  F_{\mathrm{Pauli}}(\beta)
  \;=\;
  \frac{\mathrm{tr}_{\mathrm{alt}}(\beta)}
       {\mathrm{tr}_{\mathrm{sym}}(\beta)}
  \;=\;
  \frac{c_{(1^n)}(\beta) \cdot \dim_q V_{(1^n)}}
       {c_{(n)}(\beta) \cdot \dim_q V_{(n)}}
  \,\in\, R,
$$

*where $c_{(1^n)}(\beta) = \chi_{(1^n)}(\beta)$ is the
alternating-irrep character and $c_{(n)}(\beta) = \chi_{(n)}(\beta)$
the symmetric-irrep character.  In particular,
$F_{\mathrm{Pauli}}$ vanishes when $\beta$ has no alternating-block
content (bosonic configurations) and is a unit when $\beta$ saturates
the alternating block (fully fermionic configurations).*

*Proof.* The regular representation of $H_n(q)$ decomposes as
$\bigoplus_\lambda V_\lambda^{\oplus \dim V_\lambda}$ (Wedderburn).
The Markov trace projects onto each irrep block as
$\mathrm{tr}_\lambda(\beta) = c_\lambda(\beta) \cdot \dim_q V_\lambda
/ [n]_q!$
([Wedderburn trace](#prop:wedderburn-trace-identity)).  Restricting
to the two extremal partitions $\lambda = (1^n)$ (alternating, fully
antisymmetric) and $\lambda = (n)$ (trivial, fully symmetric), the
$[n]_q!$ factor cancels in the ratio.  $\square$

**Specialisation to $H_3(q)$.**
*The three irreps of $H_3(q)$ are $V_{(3)}$ (sym, dim $1$),
$V_{(2,1)}$ (std, dim $2$), $V_{(1,1,1)}$ (alt, dim $1$).  For a
nuclear braid $\beta \in B_3$:*

$$
  F_{\mathrm{Pauli}}(\beta)
  \;=\;
  \frac{c_{(1,1,1)}(\beta) \cdot \dim_q V_{(1,1,1)}}
       {c_{(3)}(\beta) \cdot \dim_q V_{(3)}}.
$$

*Both extremal $q$-dimensions equal $1$, so $F_{\mathrm{Pauli}}$
reduces to the ratio of central-idempotent characters
$c_{(1,1,1)}/c_{(3)}$.  This recovers the working definition of
$F_{\mathrm{Pauli}}$ in the certificate engine
([mass-formula validation](#rem:mass-formula-validation)) but now
identifies it as a Wedderburn-block trace ratio rather than a
posited "statistical weight".*
