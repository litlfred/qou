**Proposition (Three-calibration discipline).**
*The QOU framework admits **categorically exactly three** external
calibration inputs, aligning to three distinct (co)homological
degrees of the substrate:*

| Cohomological datum ($H^1 = 2W$) | Measured input | What it fixes | Source |
| -------------------------------: | -------------- | ------------- | ------ |
|       $W$-plane **scale** ($H^0$) | $m_e$          | the dimensional unit (scale) | CODATA (electron mass) |
|     $W$-plane **modulus** ($H^1$) | $m_\mu$        | $q_0$ via $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$ | CODATA (muon mass) |
|        orthogonal class (no $H$-degree) | $m_\pi$  | the $\mathrm{Vol}(\mathrm{Hopf})=0$ meson scale (independent of $m_e, q_0$) | PDG (charged-pion mass) |

The three measured inputs are **three masses** $(m_e, m_\mu, m_\pi)$.
$m_e$ sets the unit; since $q_0$ is dimensionless it is fixed by $m_\mu$
*relative to that unit* — i.e. by the ratio $m_\mu/m_e$ through the
figure-eight identity $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$ with
$\hbar_q = 1 - q_0^{-1}$ (inverted for $q_0 \approx 1.10998$); $m_\pi$
sets the orthogonal meson scale. $Q_\beta$ is **derived** from
$m_e, q_0$ (see below), not a fourth input.

*For every confined hadronic state $X$ the mass functional defined
by the algebraic-side chain
([categorical action](#def\:categorical-action),
[Frobenius pairing](#def\:frobenius-pairing),
[mass identity](#def\:mass-identity),
[mass-endomorphism tower](#prop\:mass-endomorphism-tower),
[Jones–Markov trace](#thm\:jones-markov-trace))
factors as*

$$
  \mathfrak{m}(X) \;=\;
  m_e^{\,a(X)}\;m_\pi^{\,c(X)}\;Q_X(q_0),
  \qquad
  Q_X(q) \in \mathbb{Q}(q),
$$

*with non-negative integer exponents $a(X), c(X)$ determined by the
(co)homological grading the observable $X$ supplies. Concretely:
$a$ counts mass-scale insertions ($H^0$ — the $W$-plane scale), $c$
counts meson-sector insertions (the orthogonal $m_\pi$ class; $c = 0$
in the baryon sector), and $q_0$ is fixed by the lepton ratio
$m_\mu/m_e$ (the $H^1$ $W$-plane modulus). $Q_\beta$ is **derived**
from $m_e$ and $q_0$ — it is the bar-odd ($\sinh$) partner of the
bar-even ($\cosh$) meson scale $m_\pi$ under the bar-involution
$q \mapsto q^{-1}$
([substrate cohomology calibration story](../mass-theory/substrate-cohomology-calibration-story.md)),
not a primitive calibration factor.*

## Discussion

This proposition crystallises a discipline that is implicit
elsewhere in the paper:

1. **Three calibration inputs, no more, no less.** The QOU
   framework reads three CODATA / PDG values ($m_e$, the lepton
   ratio $m_\mu/m_e$, and $m_\pi$) and spends them on three distinct
   (co)homological data of the substrate. Every other physical
   prediction in the paper is the product of these three with a
   $\mathbb{Q}(q_0)$-valued algebraic expression — a Markov trace,
   a Wedderburn-block sum, a $\Phi_q$-tower contribution, etc.
2. **(Co)homological alignment.** The three calibrations are not
   interchangeable: they are precisely the three real degrees of
   freedom of the Bring Hodge structure $H^1 = 2W$
   ([calibration-cohomology-alignment](../mass-theory/calibration-cohomology-alignment.md)).
   The rank-2 $W$-Hodge plane carries two invariants — a **scale**
   (the $H^0$ prefactor, pinned by $m_e$) and a **modulus** (the
   $\mathrm{SL}_2$ trace $\tau = 2\cosh\theta$, pinned by $q_0$ via
   the lepton ratio $m_\mu/m_e$). The meson sector — whose Hopf-link complement
   has $\mathrm{Vol}(\mathrm{Hopf}) = 0$, hence no geometric scale
   derivable from $(m_e, q_0)$ — contributes a third, **orthogonal**
   scale, pinned by $m_\pi$. The count $2 + 1 = 3$ matches the three
   calibrations exactly.
3. **Overdetermination (and the physical-observations anchor).** The
   canonical $H^1$ modulus is pinned by the lepton ratio $m_\mu/m_e$
   through the figure-eight volume identity

   $$
     \frac{m_\mu}{m_e} \;=\; \frac{\mathrm{Vol}(4_1)}{\hbar_q^2},
     \qquad \hbar_q = 1 - q_0^{-1},
     \qquad \mathrm{Vol}(4_1) = 2\Lambda(\pi/3) \approx 2.0299,
   $$

   inverted for $q_0$ — so CAL-1 and CAL-2 together *coordinatize* the
   single modulus $q_0$ one-to-one (the ratio **determines** $q_0$; note
   $q_0 \approx 1.110$ while $m_\mu/m_e \approx 206.77$, so $q_0$ is the
   *root* of the identity, not the ratio itself). This is why CAL-1 +
   CAL-2 are **one** dimensionless $H^1$ datum, not two. The modulus is
   itself overdetermined: it can equally be
   fixed by $\alpha_{\mathrm{EM}}^{-1}$ or by tritium $t_{1/2}$, which
   agree on $q_0$ to within 0.3% (per
   [substrate-consistency window](#prop\:substrate-consistency-window)).
   In the **Physical-Observations** chapter one may instead anchor
   $q_0$ on a *derived* quantity with smaller experimental error —
   the proton ratio $m_p/m_e$ (0.06 ppb vs the muon ratio's 22 ppb;
   the re-pin of 2026-05-28). This is a precision substitution within
   the same overdetermined $H^1$ datum, **not** a change to the
   canonical calibration: $m_\mu/m_e$ remains CAL-2; $m_p/m_e$ is the
   numerical anchor, with $m_\mu/m_e$ then a $9.5\sigma$ cross-check
   prediction (the $\mu$–$p$ substrate tension). They re-determine the
   **same** $H^1$ datum — consistency cross-checks, not additional
   calibrations.
4. **Audit consequence.** Any content block or compute output that
   quotes a numerical mass / binding energy / Q-value not of the
   form $m_e^a m_\pi^c \cdot \text{rational}(q_0)$ has either (a)
   introduced a fourth calibration — a discipline violation that
   must be flagged and either derived or named — or (b) is
   reporting a $\tau$-image quantity from the Archimedean side
   (volume, length, etc.), which is an honest cross-domain
   comparison but does not participate in algebraic-side
   derivations.

## Proof sketch

Induction along the 19-link derivation chain (compiled in
[derivation-audit-](../../../docs/derivation-audit-.md)
and refreshed in
[-math-framework-deep-audit](../../../docs/audits/-math-framework-deep-audit.md)).
At each step:

* **Base.** The categorical action $\mathfrak{S} = \mathrm{tr}(\Phi)$
  is a $\mathbb{Q}(q)$-valued endomorphism trace
  ([categorical-action](#def\:categorical-action)) — dimensionless,
  living in $H^1$.
* **Frobenius pairing.** Preserves $\mathbb{Q}(q)$-rationality
  ([frobenius-pairing](#def\:frobenius-pairing)); identifies
  $A \cong A^\vee$ in $H^0 \oplus H^1$.
* **Mass identity.** Introduces the *Frobenius norm* $\|\cdot\|$
  on $A$ ([mass-identity](#def\:mass-identity)) — the norm is
  itself a $\mathbb{Q}(q)$-valued Markov-trace expression in
  $H^0$, not an Archimedean absolute value. The single $H^0$
  insertion is multiplied by $m_e$ at the reporting step.
* **Hecke :refterm[descent]{#descent}.** $\Phi_{\mathrm{mass}}(\beta) \in H_n(q)$ is a
  $\mathbb{Q}(q)$-element of the Hecke algebra
  ([hecke-mass-element](#def\:hecke-mass-element)).
* **Markov trace.** $\mathrm{tr}_M : H_n(q) \to \mathbb{Q}(q)$
  ([jones-markov-trace](#thm\:jones-markov-trace)).
* **Tower.** The mass-tower formula
  ([mass-endomorphism-tower](#prop\:mass-endomorphism-tower)) is
  built from Markov-trace expressions, $\Phi_q$-tower terms, and
  rational coefficients in $z$ — all in $\mathbb{Q}(q)$.
* **Meson sector.** The orthogonal $\mathrm{Vol}(\mathrm{Hopf}) = 0$
  class supplies the single meson scale $m_\pi$, independent of
  $(m_e, q_0)$ (the Hopf-link complement has zero hyperbolic volume).
  $Q_\beta$, by contrast, is **derived** from $m_e$ and $q_0$ via the
  substrate identity
  $$
    Q_\beta \;=\; m_e\,\frac{\lvert q_0^2 - 2q_0 - 1\rvert\,(q_0+1)}{2\,q_0^{3}}
    \;\approx\; 0.784\ \text{MeV}\quad(0.17\%\text{ vs CODATA}),
  $$
  the bar-odd ($\sinh$) partner of the bar-even ($\cosh$) meson scale
  $m_\pi$: the :refterm[descent]{#descent} obstruction
  class
  ([motivic-perpetual-obstruction](#conj\:motivic-perpetual-obstruction))
  is normalised by the already-fixed scales, not by a fourth input.

The dimensional factors $m_e$ and $m_\pi$ enter only at the final
reporting step
([tower-binding-energy](#prop\:tower-binding-energy)),
multiplying the dimensionless tower expression to give a value in
energy units. The composite functional is therefore
$\mathfrak{m}(X) = m_e^a m_\pi^c \cdot Q_X(q_0)$ with
$Q_X \in \mathbb{Q}(q_0)$ and $a, c \in \mathbb{Z}_{\geq 0}$.

The proposition is **conditional** on the chain being realised.
Open conjectures along the chain
([motivic-perpetual-obstruction](#conj\:motivic-perpetual-obstruction),
[mass-endomorphism](#conj\:mass-endomorphism),
[phi-q-tower-jsj-bridge](#conj\:phi-q-tower-jsj-bridge))
do not affect the dimensional-discipline statement: every step
that *is* realised respects $m_e^a m_\pi^c \cdot \mathbb{Q}(q_0)$
homogeneity, and any future closure of the chain inherits this.

∎

## Audit hook

This proposition serves as the **calibration-discipline hook** for
audits. Companion task **P1.5** in the
[ math-framework workplan](../../../docs/audits/-math-framework-workplan.md)
sweeps the paper for blocks that violate this discipline (e.g.
compound-shell calibration, atlas base cases). Companion task
**P0.1** sweeps proof blocks for Archimedean-side derivation
inputs (Vol(K), hyperbolic, Mostow, $\ldots$) — the
$\mathbb{Q}(q_0)$-rationality clause forbids such inputs in
algebraic-side derivations.

A **fourth** dimensional input anywhere in the paper is a hard
audit failure. The three calibrations are categorical: they sit in
distinct cohomological degrees and cannot be replaced by other
choices without violating the (co)homological alignment.
