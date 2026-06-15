**Proposition (Three-calibration discipline).**
*The QOU framework admits **categorically exactly three** external
calibration inputs, aligning to three distinct (co)homological
degrees of the substrate:*

|        (Co)homology degree | Calibration                   | Role                                      | Source                         |
| -------------------------: | ----------------------------- | ----------------------------------------- | ------------------------------ |
|       $H^0$ — *mass scale* | $m_e$ (electron mass)         | Sets the dimensional unit                 | CODATA                         |
|  $H^1$ — *substrate ratio* | $m_\mu / m_e \approx 206.768$ | Fixes the substrate parameter $q_0$       | CODATA (lepton ratio)          |
| $H^2$ — *weak/decay scale* | $Q_\beta$                     | Fixes the beta-decay sector normalisation | PDG (representative $Q$-value) |

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
  m_e^{\,a(X)}\;Q_\beta^{\,c(X)}\;Q_X(q_0),
  \qquad
  Q_X(q) \in \mathbb{Q}(q),
$$

*with non-negative integer exponents $a(X), c(X)$ determined by the
(co)homological grading of the observable $X$ supplies. Concretely:
$a$ counts mass-scale insertions ($H^0$), $c$ counts beta-decay
insertions ($H^2$), and $q_0$ is fixed by the lepton ratio ($H^1$).*

## Discussion

This proposition crystallises a discipline that is implicit
elsewhere in the paper:

1. **Three calibration inputs, no more, no less.** The QOU
   framework reads three CODATA / PDG values (lepton ratio, $m_e$,
   $Q_\beta$) and spends them on three distinct
   (co)homological degrees of the substrate. Every other physical
   prediction in the paper is the product of these three with a
   $\mathbb{Q}(q_0)$-valued algebraic expression — a Markov trace,
   a Wedderburn-block sum, a $\Phi_q$-tower contribution, etc.
2. **(Co)homological alignment.** The three calibrations are not
   interchangeable: they pin distinct cohomological data of the
   substrate sheaf. $H^0$ supplies a single dimensional scale
   (length / mass / time become inter-convertible only after the
   $H^0$ choice is made). $H^1$ supplies the local Frobenius
   eigenvalue spectrum (the substrate parameter $q$ — a single
   $\mathbb{Q}_p$-period for each prime $p$). $H^2$ supplies the
   normalisation of the :refterm[descent]{#descent} obstruction class — the weak
   sector's overall scale.
3. **Overdetermination.** Within each cohomological degree, the
   choice of input is itself overdetermined: $H^1$ can equally well
   be fixed by $\alpha_{\mathrm{EM}}^{-1}$ or by tritium
   $t_{1/2}$, which agree on $q_0$ to within 0.3% (per
   [substrate-consistency window](#prop\:substrate-consistency-window)).
   The three sectors (strong / EM / weak) supply consistency
   cross-checks but are *not* additional calibrations: they
   re-determine the same $H^1$ datum.
4. **Audit consequence.** Any content block or compute output that
   quotes a numerical mass / binding energy / Q-value not of the
   form $m_e^a Q_\beta^c \cdot \text{rational}(q_0)$ has either (a)
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
* **Beta-decay sector.** Q-values enter via the :refterm[descent]{#descent}
  obstruction class
  ([motivic-perpetual-obstruction](#conj\:motivic-perpetual-obstruction))
  whose normalisation supplies the single $H^2$ scale.

The dimensional factors $m_e$ and $Q_\beta$ enter only at the final
reporting step
([tower-binding-energy](#prop\:tower-binding-energy)),
multiplying the dimensionless tower expression to give a value in
energy units. The composite functional is therefore
$\mathfrak{m}(X) = m_e^a Q_\beta^c \cdot Q_X(q_0)$ with
$Q_X \in \mathbb{Q}(q_0)$ and $a, c \in \mathbb{Z}_{\geq 0}$.

The proposition is **conditional** on the chain being realised.
Open conjectures along the chain
([motivic-perpetual-obstruction](#conj\:motivic-perpetual-obstruction),
[mass-endomorphism](#conj\:mass-endomorphism),
[phi-q-tower-jsj-bridge](#conj\:phi-q-tower-jsj-bridge))
do not affect the dimensional-discipline statement: every step
that *is* realised respects $m_e^a Q_\beta^c \cdot \mathbb{Q}(q_0)$
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
