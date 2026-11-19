## Homogeneity of the chain

Induction along the 19-link derivation chain. At each step:

* **Base.** The categorical action $\mathfrak{S} = \mathrm{tr}(\Phi)$
  is a $\mathbb{Q}(q)$-valued endomorphism trace
  ([categorical action](#def:categorical-action)) — dimensionless,
  living in $H^1$.
* **Frobenius pairing.** Preserves $\mathbb{Q}(q)$-rationality
  ([Frobenius pairing](#def:frobenius-pairing)); identifies
  $A \cong A^\vee$ in $H^0 \oplus H^1$.
* **Mass identity.** Introduces the *Frobenius norm* $\|\cdot\|$
  on $A$ ([Frobenius mass identity](#def:mass-identity)) — the norm is
  itself a $\mathbb{Q}(q)$-valued Markov-trace expression in
  $H^0$ rather than an Archimedean absolute value. The single $H^0$
  insertion is multiplied by $m_e$ at the reporting step.
* **Hecke :refterm[descent]{#descent}.** $\Phi_{\mathrm{mass}}(\beta) \in H_n(q)$ is a
  $\mathbb{Q}(q)$-element of the Hecke algebra
  ([Hecke mass element](#def:hecke-mass-element)).
* **Markov trace.** $\mathrm{tr}_M : H_n(q) \to \mathbb{Q}(q)$
  ([Jones–Markov trace theorem](#thm:jones-markov-trace)).
* **Tower.** The mass-tower formula
  ([mass-endomorphism tower](#prop:mass-endomorphism-tower)) is
  built from Markov-trace expressions, $\Phi_q$-tower terms, and
  rational coefficients in $z$ — all in $\mathbb{Q}(q)$.
* **Meson sector.** The orthogonal $\mathrm{Vol}(\mathrm{Hopf}) = 0$
  class supplies the single meson scale $m_\pi$, independent of
  $(m_e, q_0)$ (the Hopf-link complement has zero hyperbolic volume).
  $\mathfrak{Q}_\beta$, the CAL-2 proxy, is itself computed from $m_e$ and
  the already-pinned $q_0$ via the ruled convention-D base
  ($\varepsilon$ evaluated as the canonical Convention-D Markov trace at $z_D = q^3/(q^2+1)$)
  $$
    \mathfrak{Q}_\beta^{z_D} \;=\; \Bigl\lvert \tfrac{h^2}{2} - h\,z_D \Bigr\rvert\,\frac{m_e}{q_0(q_0-1)(1-\hbar_q^2)}
    \;\approx\; 0.4491\ \text{MeV}\quad(-42.59\%\text{ vs CODATA}),
  $$
  with $h = q_0 - q_0^{-1}$ and $\hbar_q = 1 - q_0^{-1}$ (tower-summed $E_0$; the order-zero form gives $0.4447$ MeV, and $\{V, V^{-1}, L_+, L_-\}$ reselection gives $0.6515$ MeV, $-16.72\%$). The retired Form A,
  $m_e\lvert q_0^2-2q_0-1\rvert(q_0+1)/(2q_0^3) \approx 0.784$ MeV ($+0.17\%$),
  is kept only as a historical cross-check
  ([cos-resummation](#prop:q-beta-cos-resummation)). The all-order Convention-D generating function $\mathcal{G}_D(u; q)$ and cumulants $c_2^{(D)} = -1$, $c_3^{(D)}(q) = -\frac{3q^2-1}{2q(q^2+1)}$, and $c_4^{(D)}(q)$ are derived in closed form ($\mathbb{Q}(q)$-rational functions converging with radius $R_u \approx 0.369$), while the deficit of the bare trace $\mathrm{tr}_{z_D}(\Delta)$ reflects the vanishing bare weight $y_{(1^3)}(z_D) = 0$ on the antisymmetric baryon sign block $(1^3)$ rather than a missing fourth scale. Every step uses only fixed scales in $\mathbb{Q}(q_0)$,
  so the :refterm[descent]{#descent} obstruction
  class
  ([motivic perpetual obstruction theorem](#thm:motivic-perpetual-obstruction))
  is normalised by the already-fixed scales rather than by a fourth input.

The dimensional factors $m_e$ and $m_\pi$ enter only at the final
reporting step
([three-channel brane-tower binding](#prop:tower-binding-energy)),
multiplying the dimensionless tower expression to give a value in
energy units. The composite functional is therefore
$\mathfrak{m}(X) = m_e^a m_\pi^c \cdot Q_X(q_0)$ with
$Q_X \in \mathbb{Q}(q_0)$ and $a, c \in \mathbb{Z}_{\geq 0}$.

The discipline enters as an explicit **structural assumption** rather than a derived theorem; what the induction above shows is that the assumption is **consistent with** the derivation chain as far as the chain is realised.
Remaining open conjectures along the chain
([mass endomorphism conjecture](#conj:mass-endomorphism),
[$\Phi_q$ JSJ-volume bridge](#rem:phi-q-tower-jsj-bridge))
do not affect the dimensional-discipline statement: every step
that *is* realised respects $m_e^a m_\pi^c \cdot \mathbb{Q}(q_0)$
homogeneity, and any future closure of the chain inherits this.
