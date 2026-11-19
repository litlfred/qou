**Conjecture.**
*The Higgs boson is the torus link $T(2,8)$ — the unique genus-$3$ link on the Bring's surface whose Seifert surface spans all three exceptional divisors simultaneously.*

**The three exceptional divisors.**

The Bring's surface ($\chi = -6$, genus $4$) has three color tubes $(r, g, b)$ ([color tube coordinates](#def:color-tube-coordinates)). The brane tower blow-up produces three exceptional divisors $D_r, D_g, D_b$, one for each color fiber. The Borromean link $\mathcal{B}_3$ ([Borromean quark](#conj:borromean-quark)) lies at the intersection of these three divisors.

The torus links $T(2, 2k)$ on the Bring's surface have genus $k - 1$ and interact with the exceptional divisors by genus:

| Link | Genus | Divisors spanned | Role |
|------|------:|:----------------:|------|
| $T(2,2)$ | 0 | 0 (trivial Seifert) | Gluon |
| $T(2,4)$ | 1 | 1 ($D_r$ or $D_g$ or $D_b$) | $W$ boson |
| $T(2,6)$ | 2 | 2 ($D_r \cup D_g$ etc.) | $Z$ boson |
| $T(2,8)$ | 3 | **all 3** ($D_r \cup D_g \cup D_b$) | **Higgs** |

The torus link $T(2,8)$ is the first and only link with a Seifert surface genus large enough to span all three exceptional divisors. Its genus ($3$) exactly matches the number of color tubes.

**Scalar (spin $0$) character of $T(2,8)$.**

The two components of $T(2,8)$ each wind $4$ times around the torus longitude and $1$ time around the meridian. The fermion--boson correspondence ([fermion--boson knot--link](#prop:fermion-boson-knot-link)) identifies even-$n$ links as bosons, with components related by the fiber adjoint involution.

For $T(2,8)$, the linking number is $4$. The two components cross each other $8$ times, contributing $4$ crossings each. The Reeb winding of the two components cancels exactly: one winds $+4$ and the other $-4$ around the Reeb direction. The total angular momentum vanishes:

$$
  J =  J_1 + J_2 =  +4 + (-4) =  0.
$$

The torus link $T(2,8)$ is therefore a scalar (spin-$0$) boson. It is the only member of the $T(2,n)$ family where Reeb windings cancel exactly due to genus-$3$ symmetry.

**The Higgs mechanism as linking with $T(2,8)$.**

A particle (knot or link) acquires mass by crossing with $T(2,8)$. The crossing energy ([crossing energy](#def:crossing-energy)) of the interaction is proportional to the number of crossings between the particle and the Higgs link:

$$
  m_{\mathrm{Higgs}}  \propto 
  N_{\mathrm{cross}}(T(2,8))
   \times  \frac{q - q^{-1}}{q + q^{-1}}
$$

where $N_{\mathrm{cross}}(L)$ counts crossings between the particle braid and the link $L$.

Particles that cross all three exceptional divisors (heavy quarks, $W$, $Z$) interact strongly with $T(2,8)$ and acquire large masses. Particles confined to fewer divisors interact less. The photon ($\mathbf{1}_{B_4}$, the 4-strand identity, knot-trivial under Markov closure; see [confined-particle](#def:confined-particle)) has zero crossings with $T(2, 8)$ and remains massless.

**Mass of the Higgs.**

The torus link $T(2,8)$ has genus $3$. Its Seifert surface area is proportional to the product of the three exceptional divisor volumes. The self-crossing energy of $T(2,8)$ determines its mass ($\sim 125$ GeV) via the Skein polynomial evaluated at $q = q_0$:

$$
  m_H =  \frac{\mathrm{Vol}(\text{Seifert}(T(2,8)))}{\hbar_q^2}
  \cdot c_{\mathcal{B}}
$$

Here $c_{\mathcal{B}}$ is the historical common-scale factor of the [Borromean baryon mass formula](#conj:borromean-baryon-mass-formula) (the purged $\lambda_{\mathrm{scale}}$ literal, since re-expressed there as the common Borromean term $\mathfrak{m}_{\mathcal{B}_3}(q_0)$). It is recorded as a near-form resting on an acknowledged calibration input. The canonical production mass shape absorbs it into the per-block density, $m = m_e\,\mathrm{Vol}(K)\,\varrho(K)/\hbar_q^2$ (no standalone scale factor). This $\sim 125$ GeV heuristic estimate remains exploratory, conditional on that open closure.

The Higgs mass stems from the genus-$3$ Seifert surface volume, determined by the three color tube volumes of the Bring's surface. In the 2-strand torus-link Plancherel trace hierarchy $P_m(h) = \sum_{j=0}^m \tfrac{1}{2}\binom{m+j}{2j}h^{2j}$ ($h = q - q^{-1}$, satisfying $(q+q^{-1})\cdot 2P_m(h) = q^{2m+1}+q^{-(2m+1)}$), dressing the $W \to Z$ step by $([2]_q/2)^2 = 1 + h^2/4$ reconciles the $W$-anchored and $Z$-anchored categorical mass ratios:
$$
  m_H^{(W)} \;=\; m_W\,\frac{P_4(h_0)}{P_2(h_0)}\,\frac{6}{5}\,\frac{[2]_{q_0}}{2}\,C_{\mathrm{loop}},
  \qquad
  m_H^{(Z)} \;=\; m_Z\,\frac{P_4(h_0)}{P_3(h_0)}\,\frac{6}{5}\,\frac{2}{[2]_{q_0}}\,C_{\mathrm{loop}},
$$
so the $W$-anchor and $Z$-anchor evaluations agree to within $21.9\;\mathrm{MeV}$ ($174.7\;\mathrm{ppm}$) and land inside the PDG $125.20 \pm 0.11\;\mathrm{GeV}$ window under the parameter-free 1-loop / Bring zero-mode factors ($125.230\;\mathrm{GeV}$ from $W$ and $125.208\;\mathrm{GeV}$ from $Z$ with $C_{\mathrm{loop}} = 1 - \tfrac{2}{3\pi}\hbar_q^2$; $125.200\;\mathrm{GeV}$ from $W$ and $125.178\;\mathrm{GeV}$ from $Z$ with $C_{\mathrm{loop}} = 1 - \alpha_{\mathrm{EM}}/\pi$; or $125.052\;\mathrm{GeV}$ / $125.030\;\mathrm{GeV}$ with $C_{\mathrm{loop}} = 1 - 2G h_0^4$). Which 1-loop factor is canonical remains open alongside the C1/C$_{\text{sector}}$ torus-link identification.

**Uniqueness of the Higgs.**

On the genus-$4$ Bring's surface, the Seifert surface of $T(2,8)$ has genus $3$, filling $3$ of the $4$ available handles. Up to isotopy, there is exactly one way to embed a genus-$3$ surface into a genus-$4$ surface leaving one handle free. The next link $T(2,10)$ would require genus $4$ (all handles), saturating the surface and precluding the coexistence of Borromean and knot structures. Therefore, $T(2,8)$ is the unique Higgs candidate.
