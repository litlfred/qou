The previous section delivered the $q$-deformed
operators in coordinate form on $M$; we now build heat-flow,
Laplace, Fourier, and resolvent calculus on top of them. The
whole package is organised around the $q$-shuffle Hopf algebra
$\mathcal{H}_q$ and its grouplikes $\exp_q, \log_q,
\mathrm{Li}_2^q$ — purely Hopf-algebraic objects whose
archimedean Taylor representations are an additional fact about
the $\mathbb{C}$-realisation, not the defining property.

**$q$-heat equation** (def) introduces $\partial_t u = -\Delta_q
u$ along the Reeb flow $\phi_t^q$ on a fixed substrate slice;
**existence of the $q$-heat equation** (prop) and **uniqueness
of the $q$-heat equation** (prop), with their proofs, fix the
construction. Substituting the three-term expansion of
$\Delta_q$ splits the right-hand side into classical diffusion,
Reeb-spin diffusion, and Coriolis cross-coupling.
**Categorical Laplace transform** (def) defines $\mathcal{L}$ as
the monoidal functor pairing against the real grouplike
$\exp_q(-s \cdot) \in G(\mathcal{H}_q)$; existence and uniqueness
propositions (with proofs) follow. **Categorical Fourier
transform** (def), with its existence and uniqueness blocks,
pairs against the imaginary-spectral grouplike $\exp_q(i\xi
\cdot)$.

**$q$-resolvent** (def) is $R_q(s) = (s +
\widehat{\Delta_q})^{-1}$, characterised as the Laplace
transform of the $q$-heat semigroup and diagonalised over
irreducibles by Peter--Weyl. Existence and uniqueness blocks
(with proofs) deliver $R_q$. **Categorical Wick rotation: real
forms of $\exp_q$** (rem) identifies $\mathcal{F}[f](\xi) =
\mathcal{L}[f](i\xi)$: the Laplace and Fourier transforms are
the two real slices of a single complex pairing against
$\exp_q$, and the $q$-heat and $q$-Schrödinger equations are
sibling dynamics under $t \mapsto it$. **$q$-exponential**
(def), with its existence and uniqueness blocks, is the unique
grouplike of $\mathcal{H}_q$ satisfying $D_q \exp_q = \exp_q$.

**Finite-field obstruction to the $\exp_q$ Taylor series** (rem)
records that the Hopf-algebraic content of $\exp_q$ survives in
characteristic $p$ even when the Jackson factorials $[n]_q!$
vanish, with the truncated $\exp_q^{(p)}$ and the Witt-vector
lift to $\mathbb{Q}_p, \mathbb{C}_p$ as substitutes;
**$p$-adic realisations** (rem) gives the convergence radii.
**$q$-logarithm** (def), with its existence and uniqueness
propositions, is the unique primitive of $\mathcal{H}_q$
inverting $\exp_q$ — the Hopf-algebraic shadow of the Lie
exponential. **$q$-dilogarithm** (def), with its existence and
uniqueness propositions, is the unique level-$2$ primitive of
$\mathcal{H}_q$ normalised by the pentagon identity — the
potential whose derivative recovers the universal $R$-matrix. The next section, **Braiding
conventions**, returns to the algebraic origin of the
substrate parameter and pins down the orientation choices
behind $q$, $i$, and the ribbon twist.

_(draft.)_
