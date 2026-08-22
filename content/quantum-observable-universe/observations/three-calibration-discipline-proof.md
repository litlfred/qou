## Proof sketch

Induction along the 19-link derivation chain. At each step:

* **Base.** The categorical action $\mathfrak{S} = \mathrm{tr}(\Phi)$
  is a $\mathbb{Q}(q)$-valued endomorphism trace
  ([categorical-action](#def:categorical-action)) — dimensionless,
  living in $H^1$.
* **Frobenius pairing.** Preserves $\mathbb{Q}(q)$-rationality
  ([frobenius-pairing](#def:frobenius-pairing)); identifies
  $A \cong A^\vee$ in $H^0 \oplus H^1$.
* **Mass identity.** Introduces the *Frobenius norm* $\|\cdot\|$
  on $A$ ([mass-identity](#def:mass-identity)) — the norm is
  itself a $\mathbb{Q}(q)$-valued Markov-trace expression in
  $H^0$, not an Archimedean absolute value. The single $H^0$
  insertion is multiplied by $m_e$ at the reporting step.
* **Hecke :refterm[descent]{#descent}.** $\Phi_{\mathrm{mass}}(\beta) \in H_n(q)$ is a
  $\mathbb{Q}(q)$-element of the Hecke algebra
  ([hecke-mass-element](#def:hecke-mass-element)).
* **Markov trace.** $\mathrm{tr}_M : H_n(q) \to \mathbb{Q}(q)$
  ([jones-markov-trace](#thm:jones-markov-trace)).
* **Tower.** The mass-tower formula
  ([mass-endomorphism-tower](#prop:mass-endomorphism-tower)) is
  built from Markov-trace expressions, $\Phi_q$-tower terms, and
  rational coefficients in $z$ — all in $\mathbb{Q}(q)$.
* **Meson sector.** The orthogonal $\mathrm{Vol}(\mathrm{Hopf}) = 0$
  class supplies the single meson scale $m_\pi$, independent of
  $(m_e, q_0)$ (the Hopf-link complement has zero hyperbolic volume).
  $\mathfrak{Q}_\beta$, the CAL-2 proxy, is itself reproduced from $m_e$ and
  the already-pinned $q_0$ via the
  substrate identity
  $$
    \mathfrak{Q}_\beta \;=\; m_e\,\frac{\lvert q_0^2 - 2q_0 - 1\rvert\,(q_0+1)}{2\,q_0^{3}}
    \;\approx\; 0.784\ \text{MeV}\quad(0.17\%\text{ vs CODATA}),
  $$
  the bar-odd ($\sinh$) partner of the bar-even ($\cosh$) meson scale
  $m_\pi$: the :refterm[descent]{#descent} obstruction
  class
  ([motivic perpetual obstruction theorem](#thm:motivic-perpetual-obstruction))
  is normalised by the already-fixed scales, not by a fourth input.

The dimensional factors $m_e$ and $m_\pi$ enter only at the final
reporting step
([tower-binding-energy](#prop:tower-binding-energy)),
multiplying the dimensionless tower expression to give a value in
energy units. The composite functional is therefore
$\mathfrak{m}(X) = m_e^a m_\pi^c \cdot Q_X(q_0)$ with
$Q_X \in \mathbb{Q}(q_0)$ and $a, c \in \mathbb{Z}_{\geq 0}$.

The proposition is **conditional** on the chain being realised.
Remaining open conjectures along the chain
([mass-endomorphism](#conj:mass-endomorphism),
[phi-q-tower-jsj-bridge](#rem:phi-q-tower-jsj-bridge))
do not affect the dimensional-discipline statement: every step
that *is* realised respects $m_e^a m_\pi^c \cdot \mathbb{Q}(q_0)$
homogeneity, and any future closure of the chain inherits this.

∎
