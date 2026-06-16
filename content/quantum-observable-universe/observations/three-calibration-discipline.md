**Proposition (Three-calibration discipline).**
*The QOU framework admits **categorically exactly three** external
calibration inputs, aligning to three distinct (co)homological
degrees of the substrate:*

| Cohomological datum ($H^1 = 2W$) | Calibration                        | Role                                                       | Source                  |
| -------------------------------: | ---------------------------------- | ---------------------------------------------------------- | ----------------------- |
|       $W$-plane **scale** ($H^0$) | $m_e$ (electron mass)              | Sets the dimensional unit                                  | CODATA                  |
|     $W$-plane **modulus** ($H^1$) | $m_p / m_e \approx 1836.153$       | Fixes the substrate parameter $q_0$                        | CODATA (proton ratio)   |
| meson-sector **scale** (orthog.) | $m_\pi \approx 139.57\;\text{MeV}$ | Sets the $\mathrm{Vol}(\mathrm{Hopf})=0$ meson scale       | PDG (charged-pion mass) |

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
in the baryon sector), and $q_0$ is fixed by the proton ratio (the
$H^1$ $W$-plane modulus). $Q_\beta$ is **derived** from $m_e$ and
$q_0$, not a primitive calibration factor.*

## Discussion

This proposition crystallises a discipline that is implicit
elsewhere in the paper:

1. **Three calibration inputs, no more, no less.** The QOU
   framework reads three CODATA / PDG values ($m_e$, the proton
   ratio $m_p/m_e$, and $m_\pi$) and spends them on three distinct
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
   the proton ratio). The meson sector — whose Hopf-link complement
   has $\mathrm{Vol}(\mathrm{Hopf}) = 0$, hence no geometric scale
   derivable from $(m_e, q_0)$ — contributes a third, **orthogonal**
   scale, pinned by $m_\pi$. The count $2 + 1 = 3$ matches the three
   calibrations exactly.
3. **Overdetermination.** The $H^1$ modulus is itself
   overdetermined: $q_0$ is pinned canonically by the proton ratio
   $m_p/m_e$ (the most precise anchor; re-pinned 2026-05-28), and
   can equally be fixed by $\alpha_{\mathrm{EM}}^{-1}$ or by tritium
   $t_{1/2}$, which agree on $q_0$ to within 0.3% (per
   [substrate-consistency window](#prop\:substrate-consistency-window)).
   The muon ratio $m_\mu/m_e$ — the pre-2026-05-28 anchor — is now a
   $9.5\sigma$ cross-check *prediction*, not a calibration. These all
   re-determine the **same** $H^1$ datum: they are consistency
   cross-checks, not additional calibrations.
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
  substrate identity: the :refterm[descent]{#descent} obstruction
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
