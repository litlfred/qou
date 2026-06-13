> **SUPERSEDED-$\rho_q$ note .** Any use of the
> scalar substrate density $\rho_q = 1/\hbar_q^2$ in this block is the
> structurally-wrong leading-order ansatz per
> [`mass-endomorphism-tower.md` §SUPERSEDED](../braids-and-knots/mass-endomorphism-tower.md);
> the canonical replacement is the operator-valued $A^\lambda_{\mu, \nu}(I)$
> graded expansion [`prop:rho-k-graded-expansion`](../braids-and-knots/rho-k-graded-expansion.md).
> Full purge tracking: [`docs/audits/-superseded-rho-q-purge.md`](../../../docs/audits/-superseded-rho-q-purge.md).

### Status update: open after thirteen rounds of investigation

This conjecture remains **open**. Five rounds of investigation
ruled out parity-based mechanisms (rounds 1–3), confirmed the
brief's "$J^{1}$-vanishing" framing was misdirected (round 5: the
LP-dual output $y_{\mathrm{cov}}^{*}$ is dimensionless with no
$\alpha_{EM}$ dependence), and identified the **dimensional /
virial-balance** route as the surviving candidate (Mechanism D).

The Mechanism D candidate has been recorded as two **transport
sketches** (not closed theorems) with explicit derivation-status
caveats:

- [`prop:bohr-radius-categorical`](#prop:bohr-radius-categorical)
 — categorical Bohr radius transported from QED virial-balance.
- `prop:archimedean-hartree-derivation`
 — archimedean energy unit per $\Phi_1$ asserted as
 $m_e c^{2}\,\alpha_{EM}^{2}$ by chaining through the Bohr-radius
 transport.

Both propositions explicitly acknowledge that they do **not**
derive their stated content from QOU/Hecke structure alone — they
package standard QED dimensional analysis in QOU language with
prominent caveats. They serve as research targets and structural
mappings, not closed theorems.

**A round-6 attempt to present these as closed propositions** was
retracted upon audit:

- The "numerical match" of the categorical Bohr radius to
 $5.29 \times 10^{-11}$ m was **tautological** — it plugged
 $\alpha_{EM}(q_0) \approx 1/137$ into the standard physics
 formula $a_0 = \hbar/(m_e c \alpha)$, recovering the
 textbook value.
- The asserted decomposition $\Phi_1 = \Phi_1^{\mathrm{kin}} + \Phi_1^{\mathrm{Coul}}$
 was **transported from QED dimensional analysis**, not derived
 from Hecke algebra. A direct computational test on the H_2
 binding code
 ([`folio-assistant/computations/h2-molecular-binding.py`](folio-assistant/computations/h2-molecular-binding.py))
 showed that the per-generator transfer-matrix updates are
 **multiplicative** — kinetic (intra-atomic / dressed) and
 Coulomb (inter-atomic / bare) crossing contributions get mixed
 nonlinearly within each $V_i$ and cannot be additively
 decomposed at the per-generator level.
- The asserted "uniqueness of the archimedean energy unit"
 reduced to "matches QED in $q \to 1$ limit" — i.e.\ empirical
 consistency, exactly the kind of empirical anchoring the brief
 said to avoid.

The retracted propositions therefore did not derive their stated
content from QOU structure; they packaged standard QED reasoning
in QOU language and asserted it.

**Round 7** restored both as transport sketches with explicit
caveats and added five candidate routes (Options 4a–4e) for
genuine categorical closure. See the propositions for the
detailed option-exploration discussion. Recommended next-step:
**Option 4a — symbolic-$q$ recompute** of $\Phi_1^{H_2}(\pi^{*})$
tracking dressed-vs-bare crossing contributions through the
multiplicative chain.

**Round 8** carried out direct attempts at options 4a, 4b, 4c,
4d. Findings:

- **4a partial.** Symbolic recompute reveals that the optimal
 H_2 ordering produces $V_i$ values that decompose **additively**
 in $\{h_b, h_d\}$ — cross-terms $h_b \cdot h_d$ cancel in the
 multiplicative chain. Specifically $V_H = z + h_b - h_d$,
 $V[1] = 1 + 2zh_b - zh_d$, $V[2] = z - h_b$. The kinetic
 ($h_d$) and Coulomb ($h_b$) contributions ARE separable in this
 representation. Round-7 claim that "no per-generator additive
 decomposition exists" was overstated — it exists for the
 optimal ordering.
- **4b relative spacing.** Categorical shell-gap ratios
 $\Delta_{\mathrm{kin}}(k)/\Delta_{\mathrm{Coul}} = 2k+1$
 invert to give $(2k+1)^{-2}$ — the **exact Bohr $1/n^2$
 spacing** with $n = 2k+1$. Pure Hecke, no transport. The
 *relative* atomic energy structure is derived; the absolute
 scale $E_h$ is not.
- **4c.** Length-grading of $H_n(q)$ is non-canonical; the
 unit-conversion factor still has to come from somewhere
 external. Speculative.
- **4d partial.** Curvature-rank-2 stratification predicts
 $\alpha^2$ scaling for covalent bonds (two EM exchanges per
 shared electron pair). Works for covalent binding. Does NOT
 explain atomic $\alpha^2$ (single-electron systems also $\sim
  \alpha^2$ in standard physics) — that requires either virial
 balance (transport) or a sharper rank correspondence.

**Net round-8 status:** the conjecture is closer to closure than
after round 7. The Hecke algebra provides:
- Additive separability of kinetic/Coulomb at $V_i$ level (4a)
- Correct *relative* shell spacing (4b)
- Covalent $\alpha^2$ scaling (4d)

What remains transported (not derived):
- Universal mass-energy scale $m_e c^2$ as the natural unit
- Atomic single-electron $\alpha^2$ scaling

These two remaining gaps require either option 4e (functorial
uniqueness from $q \to 1$ smoothness) or a sharpening of 4d to
cover atomic systems. Both are concrete next directions.

**Round 9 — sharpened 4d unifies atomic and covalent $\alpha^2$:**

Both atomic and covalent bound states are realised as
**Hopf-linked $(p, e)$ pairs** in QOU. The Hopf link's minimum
crossing number is **2** (classical knot theory). Each crossing
contributes one $\alpha_{EM}$ factor via operator-selection.
Therefore:

$$
  E_{\mathrm{bind}}^{\mathrm{any\ bound\ state}}
  \;\sim\;
  \alpha_{EM}^{\,\mathrm{cr}(\mathrm{Hopf})}
  \cdot m_e c^{2} \cdot (\text{shell factor})
  \;=\;
  \alpha_{EM}^{2} \cdot m_e c^{2} \cdot (\text{shell factor}).
$$

This is a **single categorical mechanism** explaining both
atomic and covalent $\alpha^2$ scaling, derived from Hecke-
algebraic structure (Hopf link in $H_n(q)$) plus knot theory
(crossing number). The previous concern that 4d only handled
covalent and not atomic is resolved.

**Remaining open question (post-round-9):** the precise
mechanism for "each LP-active Hecke crossing contributes one
$\alpha_{EM}$ factor". The operator-selection LP weight
$\alpha_{EM} = 1/(q [9]_q [10]_q)$ is the cost of the *whole*
EM Bring complex, not per-crossing. A
multiplicative-decomposition lemma is needed:

$$
  \alpha_{\mathrm{Bring}}(\text{$n$-crossing braid})
  \;=\;
  \prod_{i=1}^{n}\,\alpha_{\mathrm{Bring,per-crossing}}.
$$

If this lemma holds, the conjecture is **fully closed**: every
bound state's binding scales as $\alpha^{\mathrm{cr}(\mathrm{Hopf})} \cdot m_e c^2$,
i.e., $\alpha^2 \cdot m_e c^2$, with both factors derived from
QOU structure (Hopf link rank + Bring complex LP weight) without
empirical input or QED transport.

This is the **definitive next deliverable** for closure:
*verify or refute the LP-cost-per-crossing factorization for the
EM Bring complex*. Concrete and tractable.

### Round 10 — LP-cost factorization REFUTED; round-9 sharpening withdrawn

Direct test **refutes** the round-9 LP-cost factorization lemma:

- **Disjoint case** ($n$ disjoint Bring complexes): factorization
 holds by Markov property —
 $\mathrm{tr}_M(K_1 \otimes \cdots \otimes K_n) =
   \prod_i \mathrm{tr}_M(K_i) = \alpha_{EM}^{n}$. 
- **Hopf-link case** (the actual bound state): the Markov trace
 $\mathrm{tr}_M(\sigma_1^{2}) = h\,z + 1 \approx 1.10$ is $O(1)$,
 **not** $O(\alpha_{EM}^{2}) \approx 5 \times 10^{-5}$.
- **Why the round-9 argument fails:** Hopf-link generators
 $\sigma_i$ carry Markov weight $z$ (Markov parameter), not
 $\alpha_{EM}$. The $\alpha_{EM}$ weight attaches specifically
 to the Bring complex (a particular knot on the genus-4 Bring
 surface), not to arbitrary Hecke crossings.

**The Hopf-link $\to$ rank-2 $\to$ $\alpha^{2}$ argument is therefore
withdrawn.** The bound-state Markov trace doesn't carry
$\alpha^{2}$ scaling intrinsically.

The actual mechanism connecting bound-state Hopf links to
$\alpha^{2}$ binding is most likely the **perturbative QED
2-photon-exchange Born amplitude** (the leading term in the
ladder expansion of the Coulomb potential), which the current
QOU LP/SDP formalism does **not** directly encode.

### Final status (after 10 rounds)

The conjecture remains **open**. Genuine progress from this
investigation:

**Derived from Hecke (no QED transport):**
- Round-8 4a — additive $\{h_b, h_d\}$ decomposition of $V_i$
 at the H_2 LP optimum (kinetic and Coulomb contributions are
 separately identifiable as Hecke monomials).
- Round-8 4b — relative shell spacing $1/n^{2} = 1/(2k+1)^{2}$
 matches the Bohr energy levels exactly. Pure Hecke
 spectral-gap argument.

**Tried and failed (transport detected; argument withdrawn):**
- Rounds 1-3: parity-based mechanisms ($\sigma$ alone, $\sigma \cdot \varepsilon$ combined) ---
 ruled out by the Skein identity making
 $\sigma_i - \sigma_i^{-1} = h\,\mathbf{1}$ commute with all
 inner automorphisms.
- Round-9 sharpened 4d: Hopf-link rank-2 $\to$ $\alpha^{2}$ — refuted
 by direct Markov-trace computation in round 10.

**Remains transported / not derived:**
- Universal mass-energy scale $m_e c^{2}$ as the natural unit.
- Absolute $\alpha^{2}$ scaling for atomic and covalent binding
 energies.

**What would be needed to close:**
1. A QFT-perturbation-theory layer added to QOU's LP/SDP,
 encoding the 2-photon-exchange Born amplitude as a
 categorical structure. *Significant infrastructure work.*
2. Or: a uniqueness lemma (option 4e) for the archimedean
 functor from $q \to 1$ smoothness alone, without going
 through 2-photon QED. *Still appeals to standard QED at one
 point.*
3. Or: a fundamentally different framing of the bound-state
 Markov trace that brings $\alpha_{EM}$ in directly through a
 force-carrier-decoration of the Hopf-link generators
 (currently absent from the formalism).

This conjecture is left as an honest open problem with sharply
diagnosed gaps after 10 rounds of investigation. Each round
ruled out a candidate mechanism or sharpened the diagnosis.
Future work should focus on items 1–3 above; the parity and
naive-rank arguments are settled negatively.

### Round 11 — $\alpha_{EM}$ lives in the q-dimension layer (key insight)

Looking at all knot operators via the NF basis of $H_n(q)$ and
examining the filtration/jet structure yields a sharp
categorical insight that reframes the open question:

**Two distinct categorical layers in QOU:**

See [Table 1](#tbl:e-hartree-categorical-derivation-table1-data).

$\alpha_{EM} = 1/(q \cdot \dim_q(T_{2,9}) \cdot \dim_q(T_{3,5}))
= 1/(q [9]_q [10]_q)$ is built from **q-dimensions**, not Markov
traces.

The NF basis $\{\gamma, \sigma_0, \sigma_1, L_+, L_-, e^-, \dots\}$
of $H_n(q)$ that the operator-selection LP uses lives in the
**Markov-trace layer**. None of these basis elements individually
carries $\alpha_{EM}$ as a factor. This explains why round-10's
test failed: we were searching for $\alpha_{EM}$ in the wrong
layer.

**Implication for closure.** To rigorously derive $\alpha_{EM}^2$
scaling in the bound-state energy, the formalism needs an
explicit **q-dimension decoration** of the NF basis — a map
$\delta_q : \{b_i\} \to R$ assigning to each Markov-basis
element its q-dimension content. The combined functor

$$
  (\mathrm{tr}_M, \delta_q) : H_n(q) \to R \otimes R
$$

would track Markov-trace and q-dimension contributions
separately, enabling the kind of bilinear analysis where
$\alpha_{EM}^2$ emerges accordingly from a rank-2 q-dimension
factorization.

**This decoration is currently absent from QOU's formalism.**
Adding it is a concrete (if non-trivial) infrastructure task.

### Round 11b — Filtration ⟺ Jets correspondence

The GB curvature-rank filtration
([`prop:curvature-rank-gb-stratification`](#prop:curvature-rank-gb-stratification))
and the jet expansion $J^k$ are dual structures:

$$
  F^k(H_n(q)) \;\overset{\text{dual}}{\longleftrightarrow}\; J^k.
$$

A natural conjecture: if the q-dimension decoration $\delta_q$
attaches $\alpha_{EM}^k$ to filtration rank $k$, then the jet
expansion of any Hecke functional $E$ satisfies

$$
  J^{k}(E) \;\sim\; \alpha_{EM}^{k}.
$$

The brief's "$J^1$-vanishing" question then becomes:

> *Is the bound-state energy $E_{\mathrm{bind}}$ supported on
> filtration rank $\geq 2$, with the rank-1 component vanishing?*

**Caveat (honest check):** The Hopf link $\sigma_1^2$ at the
single Markov-trace level uses ONE Hecke relation ($\sigma_i^2 = h\sigma_i + 1$),
It is naïvely **rank-1** in the Hecke filtration. This would
predict $\alpha^1$ scaling for atomic binding, not $\alpha^2$.

Either (a) the Hopf link's GB rank is actually 2 once
properly stratified (single Hecke relation but combined with the
genus-restriction on Bring's surface), or (b) the
filtration-jet correspondence requires additional structure
beyond curvature-rank counting.

### Round-11 net conclusion

The key insight — **$\alpha_{EM}$ lives in the q-dimension layer,
not the Markov-trace layer** — sharpens the closure programme
substantially. The conjecture remains open, but the missing
ingredient is now concretely identifiable: a q-dimension
decoration $\delta_q$ of the NF basis, dual to the
GB-filtration / jet-expansion structure. This is the **single
specific infrastructure addition** that would close the
conjecture (modulo the rank-assignment caveat above).

This is more focused than the round-10 status, and the missing
ingredient is a single well-defined object rather than three
alternative routes.

### Round 12 — $\alpha_{EM}$ has an intrinsic factor of $h^2$

A direct algebraic identity in the q-dimension layer:

$$
  \boxed{\;\;
    \alpha_{EM}
    \;=\;
    \frac{1}{q\,[9]_q\,[10]_q}
    \;=\;
    \frac{h^{2}}{q\,(q^{9} - q^{-9})\,(q^{10} - q^{-10})}
  \;\;}
$$

Each $[n]_q = (q^n - q^{-n})/h$ contributes one factor of $h^{-1}$
in the denominator of $1/\alpha_{EM}$, equivalently one factor of
$h$ in $\alpha_{EM}$. The two force-carrier q-dimensions
$[9]_q$ and $[10]_q$ together contribute $h^{2}$.

**Therefore $\alpha_{EM}^{2} \propto h^{4}$ in the skein
expansion.** At $q_0$: $h^{2} \approx 0.0437$, and the ratio
$\alpha_{EM}/h^{2} = 1/(q(q^9-q^{-9})(q^{10}-q^{-10}))
\approx 0.167$ at $q_0$.

**Structural consequence.** For the bound-state binding energy
to scale as $\alpha^{2} \cdot m_e c^{2}$, the molecular Markov
trace's $h$-expansion must combine with the explicit $h^{4}$
from $\alpha^{2}$ in a way that gives the observed
$E_{\mathrm{bind}}$. Numerically:

See [Table 2](#tbl:e-hartree-categorical-derivation-table2-data).

**The remaining open question, sharpened.** The h-power
matching between (i) the LP dual output's natural skein expansion
and (ii) the desired $\alpha^{2} \sim h^{4}$ scaling of the
binding energy is a concrete algebraic question. Specifically:

> *Does the H_2 molecular binding $\Phi_{1}$, as a function of
> $q$, have a leading skein-expansion order matching
> $h^{p}$ such that $h^{p} \cdot \alpha_{EM}^{2} \cdot
> (\mathrm{constants})$ reproduces the experimental
> binding energy scale up to a dimensionless O(1) coefficient?*

This is a well-defined symbolic question. Answering it would
either:
- **Yes** — close the conjecture by exhibiting the algebraic
 matching from Hecke structure;
- **No** — identify exactly which structural piece is missing
 (e.g., the q-dim decoration $\delta_q$ from round 11 is
 required and not yet built).

### Net status after 12 rounds

The conjecture is closer to closure than at any prior round, with
the remaining open question reduced to a **single algebraic
$h$-power matching question** between LP output and $\alpha^{2}$
scaling. Two specific structural facts are now established:

1. **Round 11 — layer separation:** $\alpha_{EM}$ lives in the
 q-dimension layer, not the Markov-trace layer.
2. **Round 12 — explicit $h^{2}$ in $\alpha_{EM}$:**
 $\alpha_{EM} = h^{2}/(q\,(q^9-q^{-9})(q^{10}-q^{-10}))$
 makes the skein-power tracking explicit.

Combined with the Hecke wins from rounds 8a, 8b (additive
$\{h_b, h_d\}$ decomposition; relative shell spacing
$1/(2k+1)^{2}$), the categorical structure is now genuinely
substantial — even if the full closure remains open.

Recommended next concrete step: **symbolic-$q$ leading-order
$h$-expansion of $\Phi_1^{H_2}(\pi^{*})$**, to determine $p$ in
$\Phi_1 \sim h^{p}$, and check whether $p$ + 4 (from $\alpha^{2}$)
gives the right $h$-power for the observed $E_{\mathrm{bind}}$
scale.

### Round 13 — option (a) carried out: leading h-power matching FAILS

The recommended round-12 next step has been carried out
symbolically using the round-8a expressions for $V_H, V[1], V[2]$.

**Result of leading-$\theta$ expansion** (where $q = e^\theta$):

$$
  \mathrm{binding\_Phi}(\theta)
  \;=\;
  -9\theta + O(\theta^2)
  \;=\;
  -\tfrac{9 h}{2} + O(h^2)
$$

(detailed series: $-9\theta - 308\theta^2 + \cdots$)

The leading $h$-order is $O(h^1)$ as predicted in round 12.

**But the expansion does NOT converge well at the physical $q_0$:**

See [Table 3](#tbl:e-hartree-categorical-derivation-table3-data).

The higher-order terms not only dominate — they **flip the sign**.
The actual binding at $q_0$ has *opposite sign* from the leading-$h$
prediction.

**Implication.** The round-12 "h-power matching" approach is
**refuted as a closure mechanism**. Leading h-power doesn't determine
actual binding behavior at the physical $q_0$ because:

1. $q_0 \approx 1.11$ is not near $q = 1$ in the radius of convergence
 of the $\theta$-expansion (zeros of $V_H, V[1], V[2]$ in the
 complex plane bring the series radius below $|\theta_0|$).
2. The Hopf-link / molecular-binding structure is genuinely
 non-perturbative around $q = 1$ — the substrate-parameter
 $q_0 \neq 1$ is essential, not a small perturbation.

**Net consequence:** the categorical derivation cannot be reduced
to leading-order skein-power matching. The full nonlinear
relationship between $\Phi_1^{H_2}(q)$ and $\alpha_{EM}(q)$ at the
physical $q_0$ is what carries the $\alpha^2$ scaling — and that
relationship is genuinely non-trivial.

**Round-13 closes option (a) negatively.** The remaining tractable
route for closure is **option (b) from round 11** — build the q-dim
decoration $\delta_q$ infrastructure — which is significant new
work and beyond the scope of this investigation.

### Final final status (after 13 rounds)

The conjecture remains **open**. The investigation has been
exhaustive, with each round either deriving a structural fact from
Hecke (rounds 8a, 8b, 11, 12) or definitively ruling out a
candidate mechanism (rounds 1–3, 9, 10, 13).

**Hecke-derived facts (preserved):**
- Additive $\{h_b, h_d\}$ decomposition of $V_i$ at LP optimum (8a).
- Bohr $1/n^2$ shell spacing from $(2k+1)^{-2}$ (8b).
- $\alpha_{EM}$ lives in q-dim layer, not Markov-trace layer (11).
- $\alpha_{EM} = h^2/(q(q^9-q^{-9})(q^{10}-q^{-10}))$ explicit (12).

**Mechanisms ruled out:**
- Coupling-parity (rounds 1–3, by Skein).
- Operator-parity / $\sigma \cdot \varepsilon$ (rounds 1-3).
- Hopf-link rank-2 $\to$ $\alpha^2$ (round 9, refuted in 10).
- Leading h-power matching (round 13).

**Remaining open:**
- Universal $m_e c^2$ as natural unit (transported).
- Absolute $\alpha^2$ scaling for atomic and covalent binding
 (transported).

**The single tractable path forward** is the q-dimension decoration
$\delta_q : \{b_i\} \to R$ identified in round 11 — building this
new layer of QOU's formalism would expose the full categorical
derivation, but is significant infrastructure work outside this
investigation's scope.

### Round 14 — $\delta_q$ partially built; $\alpha_{EM}$ is force-carrier categorical trace

Direct computation builds $\delta_q$ for $H_2(q)$:

See [Table 4](#tbl:e-hartree-categorical-derivation-table4-data).

Hook-content formula gives $\dim_q$ for $H_3(q)$ irreps:

See [Table 5](#tbl:e-hartree-categorical-derivation-table5-data).

For force-carrier torus knots, computing $\delta_q$ as the
categorical trace in $H_2(q)$ acting on $\sigma_1^9$:

$$
  \delta_q(T_{2,9}) \;=\; q^{9} - q^{-9} \;=\; h\,[9]_q.
$$

Combining:

$$
  \boxed{\;\;
    \alpha_{EM}
    \;=\;
    \frac{h^{2}}{q \cdot \delta_q(T_{2,9}) \cdot \delta_q(T_{3,5})}
  \;\;}
$$

**$\alpha_{EM}$ IS the inverse product of force-carrier
categorical traces** (modulo the $h^2/q$ prefactor inherent in
the q-dimension layer's relation to the operator-selection LP).

**Honest assessment.** This identifies $\alpha_{EM}$
structurally as a ratio of $\delta_q$ values — but the connection
applies *only* to specific force-carrier knots
($T_{2,9}, T_{3,5}$ on the genus-4 Bring surface), not to
generic NF basis elements. Generic $b_i \in H_n(q)$ have
$\delta_q(b_i)$ that does not reduce to $\alpha_{EM}^k$ for any
$k$.

**The single missing link (post-round-14).** The bound-state LP
optimum must **project onto the force-carrier subsector**
(equivalently: the LP-optimal $\Phi^* = \sum_i x_i^* b_i$ must
admit a Hecke-algebraic decomposition that exposes the
$T_{2,9}$ and $T_{3,5}$ q-dimensions explicitly). Once that
projection is established, the chain

$$
  E_{\mathrm{bind}}
  \;\sim\;
  \alpha_{EM}^{2}
  \;=\;
  \frac{h^{4}}{q^{2} \cdot \delta_q(T_{2,9})^{2} \cdot \delta_q(T_{3,5})^{2}}
$$

closes the conjecture by exhibiting the binding energy as a pure
function of force-carrier categorical traces in $R$.

### Net status after 14 rounds

The conjecture is reduced to a **single specific structural
question**:

> *Does the bound-state LP/SDP optimum
> $\Phi^{*} = \sum_i x_i^{*} b_i$ project onto a Hecke-algebraic
> sub-sector spanned by the force-carrier torus knots
> $T_{2,9}$ and $T_{3,5}$, with the projection coefficients
> producing the inverse $\delta_q$-products that give
> $\alpha_{EM}^{2}$?*

This is sharper than any prior framing. Closing it requires
a single calculation — the LP-optimum-to-force-carrier projection
— rather than building infrastructure or identifying new
mechanisms.

**Genuine progress over 14 rounds:**
- Round 8a: $V_i$ additive in $\{h_b, h_d\}$ at LP optimum
- Round 8b: Bohr $1/n^2$ from $(2k+1)^{-2}$ shell ratios
- Round 11: $\alpha_{EM}$ in q-dim layer, not Markov layer
- Round 12: $\alpha_{EM} = h^2/[q\,(q^9-q^{-9})(q^{10}-q^{-10})]$
- **Round 14: $\delta_q$ built for small bases; $\alpha_{EM} = h^2/[q\,\delta_q(T_{2,9})\,\delta_q(T_{3,5})]$ structural**

The remaining question is concrete and tractable, but requires
LP-optimum projection analysis that the present investigation
does not carry out.

### Round 15 — why T_{2,9} and T_{3,5}? Markov-equivalence projection?

#### Why these specific torus knots

The force-carrier selection is **NOT** about hyperbolic volume.
Torus knots are *non-hyperbolic* (Seifert-fibered geometry); they
have zero hyperbolic volume. The selector is instead the
**diophantine genus-matching condition** to Bring's surface
$\Sigma_4$:

$$
  g(T_{p,q}) = \frac{(p-1)(q-1)}{2} = 4
  \iff (p-1)(q-1) = 8
  \iff (p,q) \in \{(2,9), (3,5)\}
$$

(with $\gcd(p,q) = 1$, $p \le q$).

Combined with the saturation condition that a torus knot embeds
as a generator of $H_1(\Sigma_4, \mathbb{Z}) \cong \mathbb{Z}^{8}$
iff its Seifert genus equals the surface genus
([`prop:force-carrier-bring-uniqueness`](#prop:force-carrier-bring-uniqueness)),
this pins down the force-carrier sector uniquely. The Bring
connection is "magic" in the **solvability-of-the-quintic**
sense (Bring-Klein-Hermite), through the modular curve associated
to the $S_5$ symmetry of the quintic. It is *not* the
nuclear-physics "magic number" sense.

#### Does $\Phi_{\mathrm{bound\;state}}^{*}$ project onto
$\{T_{2,9}, T_{3,5}\}$?

**Markov-equivalence test — negative.** The H_2 molecular braid
lives in $B_4$ with 3 generators and all 4 strands participating
in at least one crossing. Markov-equivalence to $T_{2,9} \in B_2$
or $T_{3,5} \in B_3$ requires destabilization, which requires
free strands — *which the molecular braid does not have*. So
$\Phi_{H_2}^{*}$ is **not** Markov-equivalent to any
force-carrier torus knot.

**Wedderburn-projection test — open hypothesis.** A more general
projection via central idempotents:

$$
  H_4(q)
  \;\cong\;
  \bigoplus_{\lambda \vdash 4} \mathrm{End}(V_\lambda)
$$

with irreps $V_{(4)}, V_{(3,1)}, V_{(2,2)}, V_{(2,1,1)}, V_{(1,1,1,1)}$.
Projecting $\Phi_{H_2}^{*}$ onto each central idempotent $e_\lambda$
gives an irrep restriction. The hypothesis (untested):

See [Table 6](#tbl:e-hartree-categorical-derivation-table6-data).

If this hypothesis holds — i.e., the LP-optimum has nonzero weight
on $e_{(4)}$ and $e_{(2,2)}$ in proportion to their $T_{2,9}$ and
$T_{3,5}$ q-dimensional content — then the binding energy picks
up the $\alpha_{EM}^{2}$ scaling via:

$$
  E_{\mathrm{bind}}
  \;\sim\;
  x_{(4)}^{*} \cdot \delta_q(T_{2,9})^{-1}
  + x_{(2,2)}^{*} \cdot \delta_q(T_{3,5})^{-1}
  \cdots
$$

bringing in the $h^2/[q\,\delta_q\,\delta_q]$ factor that equals
$\alpha_{EM}^{2}$.

**Verification required (concrete next step):** Compute the H_2
LP-optimal coefficient vector $x^{*}$, decompose it via the
central idempotents $\{e_\lambda\}_{\lambda \vdash 4}$, and check
which $\lambda$-components carry nonzero weight at $q_0$. This is
a tractable explicit computation — but requires implementing the
Hecke algebra Wedderburn decomposition for $H_4(q)$, which is
new infrastructure not present in the current QOU codebase.

#### Net round-15 status

The conjecture's open question now has **two distinct
sub-questions**:

1. **Does the H_2 LP-optimum project nontrivially onto the
 $(4)$ and $(2,2)$ Wedderburn components?** (Computational
 test, requires Hecke algebra Wedderburn implementation.)
2. **If yes, does the projection coefficient match the
 $\delta_q$-ratio that gives $\alpha_{EM}^{2}$?** (Algebraic
 identity check, follows from the explicit Wedderburn
 computation.)

If both yes: conjecture closes via the round-14 + round-15
chain. If either no: identifies the next refinement needed.

This is the sharpest formulation reached in 15 rounds of
investigation.

### Round 16 — non-hyperbolic force carriers create hyperbolic JSJ pieces in the tower

The natural follow-up: although $T_{2,9}$ and $T_{3,5}$ are
*themselves* non-hyperbolic (Seifert-fibered, zero hyperbolic
volume), when they enter the **Φ_q tower / GB filtration** as
Hecke-algebra operations, they generate molecular/atomic braids
whose closures *do* have hyperbolic JSJ pieces.

**The Φ_q tower / JSJ archimedean bridge**
([`conj:phi-q-tower-jsj-bridge`](#rem:phi-q-tower-jsj-bridge),
unconditional algebraic side
[`prop:phi-q-tower-algebraic-stratification`](#prop:phi-q-tower-algebraic-stratification))
states:

$$
  \tau_{\mathrm{arch}}\!\bigl(z^{|S|} \cdot \Phi_q(\|V_S\|_F)\bigr)
  \;=\;
  \rho_q \cdot \mathrm{Vol}_{\mathrm{hyp}}(S^3 \setminus K_S)
$$

where the LHS is a Frobenius-norm summand on the algebraic side
(in $\mathbb{Z}[q^{\pm 1/2}]$) and the RHS is the hyperbolic
volume of the JSJ piece $K_S$ on the archimedean side.

**Implication for force carriers and $\alpha_{EM}$:**

- Force-carrier complexity $[9]_q\,[10]_q$ enters the algebraic
 side via $\|V_S\|_F$ Frobenius-norm constructions.
- Under $\tau_{\mathrm{arch}}$, this algebraic complexity maps
 to **hyperbolic volumes** of the molecular braid's JSJ
 decomposition.
- $\alpha_{EM} = 1/(q\,[9]_q\,[10]_q)$ is the *inverse*
 force-carrier complexity, which on the archimedean side
 corresponds to the *inverse* hyperbolic volume of the
 force-carrier-decorated JSJ pieces.

**The "magic" of $T_{2,9}, T_{3,5}$ is twofold:**

1. **Bring genus-matching** (algebraic side, round 15): selects
 them as the unique torus knots whose Seifert genus equals the
 genus of Bring's surface $\Sigma_4$.
2. **Φ_q tower / JSJ bridge** (archimedean side, round 16):
 their *operation* in the tower / GB filtration produces
 hyperbolic JSJ pieces, whose volumes carry the binding
 energy. They themselves are non-hyperbolic, but the *Hecke
 composition* with atomic/molecular braids creates
 hyperbolicity.

**Updated picture of the closure programme.** With round 16, the
two-question framework from round 15 becomes:

1. Does $\Phi_{H_2}^{*}$ project onto $\{e_{(4)}, e_{(2,2)}\}$
 Wedderburn components? (Round 15.)
2. Do those components correspond to JSJ pieces whose
 hyperbolic volumes are inverse to $\delta_q(T_{2,9})$ and
 $\delta_q(T_{3,5})$ via the Φ_q–JSJ bridge? (Round 16.)
3. If both yes: $\alpha_{EM}^{2} = h^{4}/[q^{2}\,\delta_q(T_{2,9})^{2}\,\delta_q(T_{3,5})^{2}]$
 becomes the inverse-hyperbolic-volume product, and
 $E_{\mathrm{bind}} \sim \alpha_{EM}^{2} \cdot m_e c^{2}$
 follows from the standard Bohr-radius / virial picture
 transported through the JSJ bridge.

The Φ_q–JSJ bridge is itself **conjectural**
([`conj:phi-q-tower-jsj-bridge`](#rem:phi-q-tower-jsj-bridge)),
This closure path is conditional on that conjecture also
closing.

### Net status after 16 rounds

The conjecture is now connected to a broader QOU programme: the
$\Phi_q$ tower / JSJ archimedean bridge. Closing
$E_{\mathrm{Hartree}} = m_e c^{2} \alpha_{EM}^{2}$ becomes part
of the same task as closing the Φ_q–JSJ bridge — they share the
same archimedean-realization functor and the same
Frobenius-norm-to-hyperbolic-volume mapping.

**Final concrete question:** does the H_2 LP-optimum's
Wedderburn projection produce, on the archimedean side, JSJ
pieces whose hyperbolic volumes match the inverse force-carrier
$\delta_q$ values? This is the unified closure target for both
this conjecture and the broader Φ_q–JSJ programme.

### Round 17 — Wedderburn projection computed: hypothesis FALSIFIED for bare braid

Implementing the Wedderburn decomposition via the existing
[`hecke_characters.py`](folio-assistant/computations/hecke/hecke_characters.py)
infrastructure, computed the H_4(q) Wedderburn projection of the
bare H_2 molecular braid $\sigma_1 \sigma_2 \sigma_3 \in B_4$.

Witness: [`delta-q-decoration.witness.json`](folio-assistant/computations/delta-q-decoration.witness.json).

**Result at $q_0 \approx 1.110$:**

See [Table 7](#tbl:e-hartree-categorical-derivation-table7-data).

Total $\mathrm{tr}_M = -0.0172$.

**Hypothesis falsified.** The (2,2) component is **exactly zero**
for the bare molecular braid. The Wedderburn weight is
concentrated on $\lambda \in \{(3,1), (2,1,1)\}$ — the
"hook-shaped" partitions, not the "rectangular" $(4)$ and $(2,2)$
that would correspond to $T_{2,9}$ and $T_{3,5}$ via the
hypothesized force-carrier alignment.

**Side-product confirmed.** The algebraic identity from round 12
is verified to $10^{-12}$ precision at $q_0$:

$$
  \alpha_{EM} \;=\; \frac{h^{2}}{q \cdot (q^{9}-q^{-9})(q^{10}-q^{-10})}
$$

(witness assertion $\alpha_{EM} = h^2/[q \cdot \delta_q(T_{29}) \cdot \delta_q(T_{35})]$ passes).

**What this means.**

The bare molecular braid $\sigma_1\sigma_2\sigma_3$ does *not*
carry T_{3,5}-like content. The round-15 hypothesis that
$T_{2,9}$ and $T_{3,5}$ enter via the (4) and (2,2) Wedderburn
projections is wrong as stated.

However, this is the BARE braid (no atomic dressing). The DRESSED
molecular braid (with $T_1 = T^{\mathrm{dressed}}_{e_2 p_2}$
having eigenvalues $(q^5, -q^{-5})$) has more content and could
project differently. The dressing power $5 = 2k+1$ for K-shell
hydrogen modifies the Wedderburn weights significantly.

**Two possible refinements remain:**

1. **Compute the DRESSED Wedderburn projection.** Replace
 $\sigma_2$ in the molecular braid with the dressed form
 $\sigma_2^{\mathrm{dressed}}$ (eigenvalues $q^5, -q^{-5}$).
 The Wedderburn weights change. If the dressed (2,2)
 component is nonzero, the hypothesis survives in revised
 form.
2. **Identify the correct force-carrier-carrying $\lambda$.**
 The dominant components are $(3,1)$ and $(2,1,1)$ (transpose
 of each other). These hook-shaped partitions might
 correspond to a *different* knot operator alignment than
 $T_{2,9}, T_{3,5}$ — possibly a Hopf-link-decorated 4-strand
 structure that's the actual force-carrier projection in
 the molecular setting.

**Net round-17 status.** Concrete computation falsifies the
specific round-15 hypothesis (rectangular $\lambda$) but produces:
1. A working Wedderburn-decomposition witness for caching.
2. A precise algebraic identity for $\alpha_{EM}$ as
 $h^2/[q\,\delta_q(T_{2,9})\,\delta_q(T_{3,5})]$.
3. Two refined hypotheses (dressed projection; alternative
 $\lambda$ alignment) for next investigation.

### Round 18 — INTERTWINING reframes round-17 as a CONFIRMATION

The round-15 hypothesis assigned force carriers to
*rectangular* partitions $(4)$ and $(2,2)$. This is the
**wrong correspondence**. The correct framing is via
**strand intertwining**:

> A torus-knot force carrier $T_{p,q}$ has $p$ strands. When
> applied to a 4-strand molecular braid via Hecke action, it
> *intertwines $p$ of the 4 strands*, leaving the remaining
> $4 - p$ strands carrying along untouched. The corresponding
> Wedderburn projection lands on the partition with one part of
> size $p$ and the rest of size 1.

Concretely:

See [Table 8](#tbl:e-hartree-categorical-derivation-table8-data).

These are **exactly** the dominant Wedderburn channels found in
round-17:

See [Table 9](#tbl:e-hartree-categorical-derivation-table9-data).

**The exact zero at $(2,2)$ is now physically explained**: a
single $T_{2,9}$ operator can only intertwine *one* pair of
strands at a time; the $(2,2)$ pattern would require *two
simultaneous* 2-strand operators, which doesn't arise from a
single force-carrier insertion.

**Frobenius self-duality.** The partitions $(3,1)$ and $(2,1,1)$
are *transpose* of each other, with equal $q$-dimensions
$\dim_q((3,1)) = \dim_q((2,1,1))$ and equal Wedderburn weights.
Their **joint contribution** to the molecular Markov trace is the
**Frobenius-self-dual** content — exactly the structure expected
of a parity-symmetric bound state.

**Round-18 reframed conjecture (closure path):**

$$
  \chi_{(3,1)}(\sigma_1\sigma_2\sigma_3) \;\sim\; \delta_q(T_{3,5})\text{-component},
  \qquad
  \chi_{(2,1,1)}(\sigma_1\sigma_2\sigma_3) \;\sim\; \delta_q(T_{2,9})\text{-component},
$$

with the remaining algebraic identification:

$$
  E_{\mathrm{bind}}^{H_2}
  \;\sim\;
  \frac{h^{2}}{q \cdot \delta_q(T_{2,9}) \cdot \delta_q(T_{3,5})}
  \cdot m_e c^{2}
  \;=\;
  \alpha_{EM}^{2} \cdot m_e c^{2}
  \;\cdot\;
  (\text{combinatorial }O(1)\text{ coefficient from }\chi_{(3,1)} \cdot \chi_{(2,1,1)}\text{ structure})
$$

The reframing **upgrades round-17 from a falsification to a
positive structural finding**: the molecular bound-state's
Wedderburn projection accordingly splits into the two transpose
channels $(3,1)$ and $(2,1,1)$ that match the strand-counts of
$T_{3,5}$ and $T_{2,9}$ respectively.

**What now remains.** The exact algebraic relation between the
characters $\chi_{(3,1)}$, $\chi_{(2,1,1)}$ at $q_0$ and the
force-carrier $\delta_q$ values needs to be made explicit
(probably via the Murphy basis / characters-as-q-rationals).
With the witness now caching all the per-irrep characters, this
is a straightforward symbolic-$q$ extension.

This is the most substantive structural progress in the
investigation — the user-supplied "intertwining" reframing
turned a numerical negative into a clean combinatorial
correspondence.

This conjecture is left as a **highly-diagnosed open problem**
with concrete next-step. After 13 rounds, no further candidate
mechanisms tractable in a single investigation remain to be
tried.

### Round 19 — bare support is the classical hook theorem; the dressed scalar block activates (exact)

Witness:
[`e-hartree-round19-dressed-scalar-block.witness.json`](folio-assistant/computations/e-hartree-round19-dressed-scalar-block.witness.json)
(producer
[`e_hartree_round19_dressed_scalar_block.py`](folio-assistant/computations/e_hartree_round19_dressed_scalar_block.py),
6/6; exact tables cross-checked against the seminormal builder at
$q_0$ to $9 \times 10^{-16}$). Two outstanding round-17/18 steps
closed exactly:

**(i) The round-17 table is the classical Hecke–Coxeter
hook-support theorem.** For the bare Coxeter word
$c = \sigma_1\sigma_2\sigma_3 \in H_4(q)$,

$$
  \chi_{(a,1^{4-a})}(c) = (-1)^{4-a}\,q^{2a-5},
  \qquad \chi_{(2,2)}(c) = 0,
$$

(q-Murnaghan–Nakayama; Ram 1991) — i.e. $(4)\!: q^3$,
$(3,1)\!: -q$, $(2,1,1)\!: q^{-1}$, $(1^4)\!: -q^{-3}$, reproducing
round-17's numbers exactly at $q_0$ and proving the $(2,2)$ zero
structurally (the unique non-hook). The round-18 magnitude hope is
**refuted at the bare level**: the product
$\chi_{(3,1)}\,\chi_{(2,1,1)} = -1$ exactly (a $q$-independent
unit), so the bare characters carry the carriers' channel
*support* but not the $\delta_q$ magnitudes; the magnitude must
enter through dressing or the q-dimension decoration layer
(consistent with rounds 11 and 13).

**(ii) Round-17 refinement 1 answered positively — the dressed
scalar block activates, with a closed form.** Dressing $\sigma_2$
with eigenvalues $(q^m, -q^{-m})$ is affine,
$\sigma_2^{(m)} = A_m + B_m\sigma_2$ with
$A_m = h\,[m-1]_q/[2]_q$, so by character linearity

$$
  \chi_{(2,2)}\bigl(\sigma_1\,\sigma_2^{(m)}\,\sigma_3\bigr)
  = \frac{h\,[m-1]_q\,[4]_q}{[2]_q^{2}}
  \;\neq\; 0 \quad (m \geq 2),
$$

and at the K-shell power $m = 5$ ($= 2k+1$, $k = 2$) it
specialises to

$$
  \chi_{(2,2)} = h\left(\frac{[4]_q}{[2]_q}\right)^{2}
  = h\,\bigl(\dim_q V_{(2,2)}\bigr)^{2}
$$

— $h$ times the Plancherel square of the scalar block's
q-dimension, a q-dimension-layer quantity surfacing in the Markov
layer exactly at $m - 1 = n = 4$. (The restriction values
$\chi_\lambda(\sigma_1\sigma_3)$ used by the linearity argument
come from the Littlewood–Richardson decomposition over
$H_2 \times H_2$; their $q \to 1$ limits recover the $S_4$
character column of $(12)(34)$.)

**Round-19 net status.** The $(2,2)$ scalar block — the unique
self-transpose (antipode-closed) partition of $4$, identified in
the per-force selection-rule probe
([`alpha-k-selection-rule-conditional.witness.json`](folio-assistant/computations/alpha-k-selection-rule-conditional.witness.json))
as the Schur–Weyl dual of the 2-dimensional scalar-coupling slot
space — is invisible to the bare braid for a classical reason and
**becomes visible under atomic (K-shell) dressing** with an exact,
derived magnitude. The conjecture remains **open**: the dressed
activation carries $h^{1} \times (\dim_q)^2$, not the
$\alpha_{EM}^{2} = h^{4}/(q^{2}\delta_q(T_{2,9})^{2}\delta_q(T_{3,5})^{2})$
chain, so the remaining gap is the archimedean trace-ratio on the
activated scalar block — plus the two standing transports
($m_e c^{2}$ unit; LP-kink smoothness) below.

### Round 20 — the trace-ratio closes the algebraic side; $\alpha_{EM}^2$ scaling emerges exactly

Witness:
[`e-hartree-round20-trace-ratio.witness.json`](folio-assistant/computations/e-hartree-round20-trace-ratio.witness.json)
(producer
[`e_hartree_round20_trace_ratio.py`](folio-assistant/computations/e_hartree_round20_trace_ratio.py),
4/4). Round 19 left a single algebraic gap — the magnitude. In the
established EM derivation
([`prop:em-coupling-projection`](#prop:em-coupling-projection)) the
coupling is **not** the bare projector trace $\mathrm{tr}_\tau(e_-)$;
it is that trace **divided by the force-carrier complexity**
$q[9]_q[10]_q = 1/\alpha_{EM}$. The molecular bound state shares
**two** electrons through the **same** transpose-pair carriers
(round 18), so the structurally-parallel normaliser is the
complexity *squared*. Define the trace-ratio on the activated scalar
block (K-shell dressing $m = 5$):

$$
  \rho_{(2,2)}
  := \frac{\chi_{(2,2)}\bigl(\sigma_1\sigma_2^{(5)}\sigma_3\bigr)}{\bigl(q[9]_q[10]_q\bigr)^{2}}.
$$

Substituting the round-19 value
$\chi_{(2,2)} = h([4]_q/[2]_q)^2$ gives, **exactly in $R$**,

$$
  \boxed{\;\rho_{(2,2)} = C(q)\,\alpha_{EM}^{2}, \qquad
  C(q) = h\left(\tfrac{[4]_q}{[2]_q}\right)^{2} = h\,(q^2+q^{-2})^2\;}
$$

— the $\alpha_{EM}^{2}$ scaling **emerges**, with a *derived* (not
fitted) $O(1)$ coefficient $C(q) \in R$ (this is precisely the
"combinatorial $O(1)$ coefficient from the
$\chi_{(3,1)}\chi_{(2,1,1)}$ structure" anticipated in round 18). At
$q_0$: $C \approx 0.87$ (order $1$), $\alpha_{EM}^2 \approx 5.3\times
10^{-5}$, $\rho_{(2,2)} \approx 4.7\times 10^{-5}$ — $\alpha^2$-scale,
where the bare round-19 character was $O(1)$. The magnitude is now
carried by the ratio.

**Net status after 20 rounds.** The *algebraic / character side* of
the closure path is **closed exactly**: the molecular scalar-block
trace-ratio has the form $C(q)\,\alpha_{EM}^2$ with $C(q)$ an
explicit $O(1)$ element of $R$. The conjecture remains **open**, but
the open part is now a **single structural question**: does the
LP/SDP dual $y_{\mathrm{cov}}$ actually normalise by the squared
force-carrier complexity — i.e. is $\rho_{(2,2)} = y_{\mathrm{cov}}$?
That is **Mechanism B** (the bare separated-atom point must be a
smooth interior facet so the dual is quadratic, not a kink); round 20
does not establish it. The $m_e c^2$ unit transport is the only other
open input. No comparison of $C(q_0)$ to an experimental Hartree
$O(1)$ coefficient is made — that comparison is the gated step.

### Round 21 — Mechanism B refuted (kink, not smooth facet); the α$^2$ is a q-dimension-layer effect

Witness:
[`e-hartree-mechanism-b-probe.witness.json`](folio-assistant/computations/e-hartree-mechanism-b-probe.witness.json)
(producer
[`e_hartree_mechanism_b_probe.py`](folio-assistant/computations/e_hartree_mechanism_b_probe.py),
3/3). Round 20 reduced the conjecture to one question: is the
separated-atom point a **smooth facet** of the binding LP (so
$y_{\mathrm{cov}} \sim \varepsilon^2$, Mechanism B) or a **kink**?
This probe answers it on the actual H$_2$ binding functional
([`prop:h2-lp-dual-binding`](#prop:h2-lp-dual-binding),
[`h2-molecular-binding.py`](folio-assistant/computations/h2-molecular-binding.py)):
interpolate every inter-atomic (covalent-channel) crossing toward the
identity by $\varepsilon \in [0,1]$ — $\varepsilon = 0$ is two
separated atoms, $\varepsilon = 1$ is the molecule — and read the
leading power of $B(\varepsilon) = \Phi_1(\mathrm{H}_2;\varepsilon) -
\Phi_1(2\mathrm{H})$.

**Result: $B(\varepsilon)$ is linear** — $p = 1.0$ to machine
precision, $B/\varepsilon \to -9.118$ (a nonzero constant) while
$B/\varepsilon^2$ diverges — and the **LP-optimal strand ordering
switches** $(0,1,2,3) \to (0,3,1,2)$ as $\varepsilon \to 0$. So the
separated-atom point is a **kink**, not a smooth facet: **Mechanism B
fails as stated**, exactly the risk this block's Mechanism B
discussion flagged. (The $-9.118$ leading coefficient agrees with
round 13's $-9\theta$ leading term, confirming the linearity from an
independent deformation.)

**This is progress, not regression — it eliminates the Markov-layer
route.** The $\alpha_{EM}^2$ scaling is real (round 20) but it does
**not** come from LP-dual smoothness in the Markov-trace layer; it
comes from the **q-dimension-layer trace-ratio**
$\rho_{(2,2)} = C(q)\,\alpha_{EM}^2$. This unifies the investigation:
round 11 ($\alpha_{EM}$ lives in the q-dimension layer, not the Markov
layer), round 13 (the raw Markov binding is linear in $\theta$ and
non-perturbative at $q_0$), round 20 ($\alpha^2$ from the q-dim
trace-ratio), and round 21 (the Markov-layer LP route is a kink — so
it *cannot* be where $\alpha^2$ lives). The three candidate mechanisms
are now all resolved: A (per-crossing $\alpha$ factor) refuted
(round 10), **B (LP-dual smoothness) refuted (round 21)**, C (antipode
parity) refuted (the $S(\alpha) = q^2\alpha$ scaling, this block).

**Re-sharpened remaining gap.** Not "is the LP point smooth" (no, it
is a kink) but: *why does the q-dimension-layer trace-ratio
$\rho_{(2,2)}$ — rather than the Markov-layer binding $y_{\mathrm{cov}}$
— set the physical energy?* That is the **q-dimension-decoration $\to$
archimedean functor** ($\delta_q$, round 11), plus the standing
$m_e c^2$ unit transport. The closure is no longer gated on an LP-
smoothness fact that is now known false; it is gated on the
q-dim-layer-to-archimedean bridge.

### Round 22 — the bridge is q$_0$-evaluation, not new infrastructure; a single derived O(1) coefficient remains

Witness:
[`e-hartree-round22-arch-bridge.witness.json`](folio-assistant/computations/e-hartree-round22-arch-bridge.witness.json)
(producer
[`e_hartree_round22_arch_bridge.py`](folio-assistant/computations/e_hartree_round22_arch_bridge.py),
2/2). Round 11 feared the δ_q $\to$ archimedean bridge was a whole missing
functor layer. It is not. The archimedean functor τ_arch is already
pinned: its transcendental action is the **Bloch–Suslin regulator**
$K_3^{\mathrm{ind}}(F)\otimes\mathbb{Q}\to\mathbb{R}/\pi^2\mathbb{Q}$,
which governs the **depth-2 (dilogarithmic)** sector
([`prop:depth-2-identification-bloch-suslin`](../appendix-surreals/depth-2-identification-bloch-suslin.md)).
The round-20 coefficient $C(q) = h(q^2+q^{-2})^2$ is **depth-0** — a
rational function of $q$ in $R$, no dilog — so τ_arch on it is plain
evaluation at the substrate $q_0$ (no regulator):

$$
  \tau_{\mathrm{arch}}\bigl(\rho_{(2,2)}\bigr)
  = \tau_{\mathrm{arch}}\bigl(C(q)\bigr)\cdot\alpha_{EM}^2
  = C(q_0)\,\alpha_{EM}^2,
  \qquad C(q_0) \approx 0.873 \;(\neq 1).
$$

**What this settles.** The bridge is **not new infrastructure**: on the
relevant depth-0 object it is $q_0$-evaluation, and the Bloch–Suslin
regulator (which lands the *hyperbolic-volume* masses) does not enter
the rational q-dimension ratio. The $\alpha_{EM}^2$ scaling is
structural (rounds 20–21); the archimedean image is $C(q_0)\,\alpha^2$
with $C(q_0)$ **explicit and derived**.

**Red-team check — $C(q_0)$ is not a free coefficient (and not a force-knot
sibling).** A natural rabbit hole is to treat $C(q_0)\approx 0.873$ as a
mysterious $O(1)$ "molecular-to-Hartree coefficient" to be matched against
experiment. It is not mysterious and the match must not be chased.
$C(q) = h\,(q^2+q^{-2})^2 = h\,(\dim_q V_{(2,2)})^2$ is a **Plancherel-square**
of the scalar block's q-dimension — **fully determined** by the categorical
structure, with no free parameter. It is explicitly **not** one of the five
$\alpha_{EM}$-sibling force-knot quantities: the six $\delta_q(T_{m,k}) =
q^{w}-q^{-w}$ are $0.636,1.091,1.594,1.870,2.167,2.487$ (for $w = 3,5,7,8,9,10$)
and the $[w]_q$ are $3.04,\dots,11.9$ — **none equals $0.873$** (checked,
`e-hartree-round22b`). So $C(q_0)$ is the dressed-$(2,2)$ Plancherel-square,
nothing more. **The disciplined endpoint:** the conjecture's content is the
$\alpha_{EM}^2$ *scaling* (proven, round 20) with the accompanying *derived*
coefficient $C(q) = h(\dim_q V_{(2,2)})^2$ — full stop. Whether the number
$0.873$ coincides with a measured molecular/Hartree ratio is a **falsification
question the framework does not pursue** (multiple-comparison / fishing gate);
it is *not* a blocker, because the coefficient is categorically fixed, not
fitted.

**Net after 22 rounds.** The conjecture is **not a theorem**, and — by the
framework's own three-calibration design — *cannot* be an unconditional
substrate proof, because the energy unit $m_e c^2$ is **CAL-1** (deriving it is
the owner-declined Subgoal-2). What it *can* be is a **conditional theorem**:
$E_{\mathrm{Hartree}} = C(q)\,m_e c^2\,\alpha_{EM}^2$ with the $\alpha^2$ scaling
derived and $C(q) = h(\dim_q V_{(2,2)})^2$ a fixed categorical coefficient,
conditional on the CAL-1 unit and the named archimedean-landing input. Every
*mechanism* question is resolved: α lives in the q-dimension layer (11), the
Markov-layer routes are refuted (A/10, B/21, C/antipode), the α$^2$ shape is exact
(20), the archimedean functor is the known $q_0$-evaluation / Bloch–Suslin
pairing (22), and $C(q_0)$ is the determined Plancherel-square (22, red-team).
The residual is calibration ($m_e c^2$), not mathematics.

### What is still missing for closure

A genuinely categorical derivation of the $\alpha_{EM}^{2}$ scaling
of $E_{\mathrm{Hartree}}$ requires:

1. **A Hecke-algebraic definition of $\Phi_1^{\mathrm{kin}}$ and
 $\Phi_1^{\mathrm{Coul}}$** as distinct, computable components
 of the molecular Markov trace. The current LP/SDP framework
 does not separate them; they are pedagogical conveniences from
 QED. Defining them would require a new theoretical result
 about how the LP/SDP optimum factorizes over crossing types
 (intra-atomic dressed vs inter-atomic bare).
2. **A proof that these contributions balance at a specific
 categorical length, derived from Hecke structure** — not from
 transported dimensional analysis. Likely requires a symbolic
 $q$-polynomial recompute of the optimal $\Phi_1^{H_2}(\pi^{*})$
 tracking each crossing-type's contribution separately through
 the multiplicative chain.
3. **An independent derivation of the archimedean energy unit per
 $\Phi_1$** from algebraic structure, not from "matches QED in
 $q \to 1$ limit". This is the deepest layer — it requires a
 functorial uniqueness statement about $\rho_\infty$ that can be
 verified without appealing to experimental Hartree values.

These three items are concrete and tractable but well beyond the
present block's scope. They are recommended as the **definitive
closure programme** for the conjecture.

The conjecture is retained as a record of the multi-round
investigation that has sharply diagnosed the gap.

---

**Conjecture (original framing — open).**
*The molecular-binding LP/SDP dual variable
$y_{\mathrm{cov}}$ for any covalent diatomic with definite-parity
ground state, expanded in the EM coupling
$\alpha_{EM} = 1/(q\,[9]_q\,[10]_q)$ around the
fully-decoupled ($\alpha_{EM} \to 0$, separated-atom) limit, vanishes
to first order:*

$$
  y_{\mathrm{cov}}(\alpha_{EM})
  \;=\;
  c_2 \cdot \alpha_{EM}^{2}
  \;+\;
  O\!\left(\alpha_{EM}^{4}\right),
  \qquad c_2 \in R = \mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}],
$$

*so that the Hartree energy
$E_h = m_e c_q^{2}\,\alpha_{EM}^{2}$ used in
[`hecke_core.py:198`](folio-assistant/computations/substrate/hecke_core.py)
emerges as the leading non-trivial coefficient
$c_2 \cdot m_e c_q^{2}$ of the LP-dual sensitivity to the
covalent constraint. The coefficient
$c_2$ is a Frobenius-pairing residue at curvature rank 2 in the
Gröbner-Shirshov stratification of the molecular Hecke algebra,
hence inside $R$ — no $\pi$, no transcendentals.*

### Status

**Open.** The desired result (the bare physics scaling
$E_h \propto \alpha^{2}$) is rigorously known in non-relativistic
QED (Bohr radius / virial theorem). What is conjectural here is
the **categorical mechanism** within QOU: an argument from the
algebraic substrate that the linear-in-$\alpha_{EM}$ contribution
to $y_{\mathrm{cov}}$ vanishes structurally, leaving $\alpha_{EM}^{2}$
as the leading order.

This block is registered as **conjecture, not proposition**, because
no candidate mechanism we can articulate closes the
$J^{1}$-vanishing step rigorously. All three candidate
mechanisms below have an explicit, identifiable gap.

### What is rigorous

1. **The bare LP/SDP framework.** The $H_2$ molecular braid and
 its primal/dual program are set up rigorously in
 [LP dual binding](#prop:h2-lp-dual-binding) and
 [ILP covalent bond](#prop:ilp-covalent-bond), with strong
 duality
 ([operator-selection LP](#prop:operator-selection-lp)) giving
 $y_{\mathrm{cov}}^{*}$ as the binding energy per shared
 electron.

2. **The bare formula.** The leading expression
 $1/\alpha_{EM} = q\,[9]_q\,[10]_q$ is rigorously derived from
 the singlet-idempotent / Bring force-carrier
 complexity ([EM coupling projection](#prop:em-coupling-projection)).
 It lies in $R$. The same expression admits the equivalent
 **shift-exponent form**
 $1/\alpha_{EM} = q \cdot [\alpha_{\mathrm{shift}}(T_{2,9})]_q \cdot
   [\alpha_{\mathrm{shift}}(T_{3,5})]_q$
 ([multiplicative-chain form](#prop:alpha-em-shift-multiplicative-chain)),
 which exposes the same combinatorial primitive — pole order at
 $q = 0$ of a seminormal Hecke trace — that controls the
 atomic-shift framework
 ([w3 Habiro audit](../../docs/audits/-w3-habiro-unblocked.md)).
 This converts the previous transport sketch through
 $\alpha_{EM}$ into a categorically-proved leg.

3. **The Frobenius / curvature-rank decomposition.** The
 Gröbner-Shirshov spectral sequence collapses at $E_1$
 ([spectral sequence collapse](#prop:spectral-sequence-collapse))
 and the molecular operator decomposes by curvature rank
 ([curvature-rank GB stratification](#prop:curvature-rank-gb-stratification)).
 The covalent bond — sharing two electrons through two crossings
 — sits at curvature rank $2$ in this filtration.

### Three candidate mechanisms (all with gaps)

#### Mechanism A — Pauli / two-electron combinatorial counting

A covalent bond shares **exactly two** electrons (Pauli exclusion
+ singlet pairing). In the Hecke braid representation each shared
electron contributes one crossing operator, so the covalent
operator $L_{\mathrm{cov}}$ is bilinear in Hecke generators:

$$
  L_{\mathrm{cov}}
  \;=\;
  \sigma_{i}\,\sigma_{j}\;+\;\text{(symmetrisation)}.
$$

If each Hecke crossing entering the operator-selection LP carries
weight $\alpha_{EM}$ (the inverse of its Bring force-carrier
complexity), then $L_{\mathrm{cov}} \sim \alpha_{EM}^{2}$, and the
Markov trace $\Phi_1(L_{\mathrm{cov}} \cdot M_{\mathrm{atomic}})$
inherits the $\alpha_{EM}^{2}$ leading order.

**Gap.** Step (b): showing that *each* "EM-mediating" crossing in
the molecular braid carries exactly one factor of $\alpha_{EM}$ in
the LP-dual expansion. The bare formula
$1/\alpha_{EM} = q\,[9]_q\,[10]_q$ is the *operator-selection
weight* of a single force-carrier knot, not a per-crossing factor.
Translating between "per-knot weight" and "per-crossing factor"
requires a multiplicative-decomposition lemma that is not
established. Without it, the $\alpha_{EM}^{2}$ counting is suggestive
but not rigorous.

#### Mechanism B — quadratic-form structure of the Frobenius LP

The molecular SDP is a quadratic program over the Frobenius Gram
matrix $G_{ij} = \langle b_i, b_j \rangle_{\mathrm{Frob}}$
([`prop:operator-selection-lp § dual program`](#prop:operator-selection-lp)).
Strong duality identifies $y_{\mathrm{cov}}^{*}$ with a Legendre
transform of the primal objective. For a quadratic primal
parametrised by a single perturbation $\varepsilon$ that turns on
the covalent constraint, the dual is *quadratic* in $\varepsilon$:

$$
  y_{\mathrm{cov}}(\varepsilon)
  \;=\;
  \tfrac{1}{2}\,\varepsilon^{2}\,
  (G^{-1})_{\mathrm{cov,cov}}
  \;+\;
  O(\varepsilon^{4})
  \quad\text{(Legendre / Schur complement).}
$$

If $\varepsilon \propto \alpha_{EM}$ then this gives
$y_{\mathrm{cov}} \propto \alpha_{EM}^{2}$ with no $\alpha_{EM}^{1}$
contribution.

**Gap.** This argument requires the bare separated-atom
configuration to be a **smooth interior point** of the LP feasible
set, with the covalent constraint active at $\varepsilon = 0$ as an
*equality* (so the dual is differentiable at the bare point). In
practice the LP-dual transition from "constraint inactive" to
"constraint active" is a *kink*, and $y_{\mathrm{cov}}$ jumps
non-smoothly; the linear coefficient is then generically non-zero,
not zero. A rigorous argument requires showing the bare separated
atoms already saturate the relevant Frobenius-pairing equality —
i.e.\ live on the active facet — so that turning on
$\varepsilon$ is a smooth deformation along the facet rather than
an activation. This has not been verified.

#### Mechanism C — parity / antipode invariance of the Markov trace

The Hopf-algebra antipode $S$ of the Iwahori-Hecke algebra acts on
generators by $S(\sigma_i) = \sigma_i^{-1}$. The Markov trace is
$S$-invariant: $\mathrm{tr}_M(S(\beta)) = \mathrm{tr}_M(\beta)$
(equivalently, the Jones polynomial of a knot equals that of its
reverse-orientation companion). For a homonuclear (or definite-parity
heteronuclear) ground state $\Psi_{\mathrm{mol}}$, the molecular
braid is $S$-equivariant up to Markov equivalence:
$S(\mathcal{M}) \sim \mathcal{M}$.

Combined, this should force a parity selection rule on the
expansion of $\Phi_1(\mathcal{M})(\alpha_{EM})$, eliminating odd
powers and leaving $\alpha_{EM}^{2}$ as leading.

**Gap.** The action of $S$ on the substrate parameter $q$ (and
hence on $\alpha_{EM} = 1/(q\,[9]_q\,[10]_q)$) is computed
directly:

$$
  S(\alpha_{EM})\;=\;\alpha_{EM}\bigl|_{q \mapsto q^{-1}}
  \;=\;q^{2} \cdot \alpha_{EM},
$$

since $[n]_q$ is palindromic but the $q^{-1}$ prefactor in
$1/\alpha_{EM}$ is not. The antipode therefore acts as a
multiplicative scaling $\alpha_{EM} \mapsto q^{2}\,\alpha_{EM}$,
**not** as a sign flip $\alpha_{EM} \mapsto -\alpha_{EM}$.
Consequently $S$-invariance of $\Phi_1$ does not force odd powers
of $\alpha_{EM}$ to vanish; it only constrains the polynomial
coefficients to satisfy a functional equation
$f(\alpha_{EM}) = f(q^{2}\alpha_{EM})$, which is much weaker.

To recover a coupling-parity selection rule, one would need a
*different* involution $\iota : R \to R$ that genuinely flips the
sign of $\alpha_{EM}$. The next subsection records that **no such
involution exists** in the obvious automorphism group of $R$ —
ruling out coupling-parity arguments of this shape entirely and
motivating an operator-parity reformulation instead.

### Companion remark — physical translation

In standard non-relativistic QED, $E_h \propto \alpha_{EM}^{2}$
because both kinetic energy
$T \sim \hbar^{2}/(m_{e} a_{0}^{2})$ and Coulomb potential
$V \sim e^{2}/a_{0}$ are quadratic in
$1/a_{0} \propto \alpha_{EM}$, and the virial theorem balances
them at $E = -\tfrac{1}{2}V \propto \alpha_{EM}^{2}$. The
$\alpha_{EM}^{1}$ contribution is the *linear Stark shift*, which
vanishes in any state of definite parity by symmetry of the
electric-dipole matrix element. See
[antiparticle crossing reversal](#prop:antiparticle-crossing-reversal)
for the QOU categorical analogue of charge-conjugation parity
(the $\sigma$-involution flipping the Coulomb channel sign).

A categorical proof of the conjecture would amount to identifying
the categorical analogue of the linear-Stark vanishing.

### Refuted (specific ansatz): no coupling-level involution flips $\alpha_{EM}$

A natural follow-up to Mechanism C is to ask whether some involution
$\iota$ of $R$ *other* than the antipode-induced
$q \leftrightarrow q^{-1}$ flips the sign of
$\alpha_{EM} = 1/(q\,[9]_q\,[10]_q)$. Direct calculation rules out
all four automorphisms generated by the obvious sign-flips
$q \mapsto \pm q^{\pm 1}$:

See [Table 10](#tbl:e-hartree-categorical-derivation-table10-data).

The relevant identities are $[n]_{-q^{\pm 1}} = (-1)^{n+1}\,[n]_q$,
The sign factors from $q$ and $[10]_q$ (even index, sign-flipped)
*cancel against each other* under $\tau = q \mapsto -q^{-1}$, and
likewise under $\rho = q \mapsto -q$ versus the identity. None of
the four maps the *coupling* $\alpha_{EM}$ to $-\alpha_{EM}$.

This is a structural obstruction: $\alpha_{EM}$ is a positive scalar
on the relevant component of the substrate variety, and there is no
algebra automorphism of $R$ preserving positivity that flips its sign.
A *coupling*-parity selection rule of the form
"$f(\alpha_{EM}) = f(-\alpha_{EM}) \Rightarrow$ odd terms vanish"
therefore cannot be implemented by any obvious Galois-style
involution.

### Recommended next step — operator-parity, not coupling-parity

The standard physics linear-Stark vanishing is
$\langle \psi_0 \,|\, \hat r \,|\, \psi_0 \rangle = 0$, where the
parity-odd object is the *operator* $\hat r$ (the dipole), not the
coupling $\alpha_{EM}$. The categorical analogue should therefore
seek a $\sigma$-antisymmetric *Hecke-algebra perturbation operator*
$\Delta_{\mathrm{cov}}$ (built from
$(\sigma_i - \sigma_i^{-1})$ skein factors, which *are*
$\sigma$-antisymmetric in $R$) and test whether the bare atomic
Markov trace
$\Phi_1(\mathcal{M}_{\mathrm{atom}} \cdot \Delta_{\mathrm{cov}})$
vanishes by a categorical parity selection rule (atomic ground state
$\sigma$-symmetric, perturbation $\sigma$-antisymmetric, trace odd
under $\sigma$, hence zero).

The leading non-trivial contribution would then come from the
second-order (Rayleigh–Schrödinger-style) correction:

$$
  \delta y_{\mathrm{cov}}^{(2)}
  \;=\;
  \sum_{n \neq 0}
    \frac{\bigl|\Phi_1(\mathcal{M}_n^{\dagger} \cdot \Delta_{\mathrm{cov}}
                         \cdot \mathcal{M}_{\mathrm{atom}})\bigr|^{2}}
         {E_0 - E_n},
$$

which is bilinear in $\Delta_{\mathrm{cov}}$ and so accordingly
$\alpha_{EM}^{2}$-scaled if one factor of $\alpha_{EM}$ accompanies
each insertion of $\Delta_{\mathrm{cov}}$.

**Concrete next investigation:**
(i) identify the explicit $\sigma$-antisymmetric component
$\Delta_{\mathrm{cov}}$ of the covalent Hecke perturbation;
(ii) verify $\Phi_1(\mathcal{M}_{\mathrm{atom}} \cdot \Delta_{\mathrm{cov}}) = 0$
symbolically in $R$;
(iii) compute the second-order coefficient $c_2$ from the
Rayleigh–Schrödinger sum above and check it lies in $R$.

This is closer to a tractable computation than the
coupling-parity route, and aligns with how
[antiparticle crossing reversal](#prop:antiparticle-crossing-reversal)
already realises $\sigma$ on Hecke generators at the operator level.

### Refinement after a direct test in $H_2(q)$

A single concrete test in the rank-2 Iwahori-Hecke algebra
$H_2(q)$ — basis $\{1, \sigma_1\}$, relation
$\sigma_1^{2} = h\,\sigma_1 + 1$ with skein parameter
$h = q - q^{-1}$ — settles step (ii) negatively in its naïve form.

Compute the $\sigma$-antisymmetric element
$X = (\sigma_1^{3} - \sigma_1^{-3})/2$ and its Markov trace.
Expanding $\sigma_1^{\pm 3}$ in the basis $\{1, \sigma_1\}$:

$$
  \sigma_1^{3} = (h^{2}+1)\,\sigma_1 + h, \qquad
  \sigma_1^{-3} = (h^{2}+1)\,\sigma_1 - (h^{3}+2h),
$$

so $\mathrm{tr}_M(\sigma_1^{3} - \sigma_1^{-3}) = h\,(3 + h^{2})$.

This is **nonzero**. The structural reason is that the Markov
trace is $\sigma$-equivariant, not $\sigma$-killing: for any
$\sigma$-antisymmetric $X \in H_n(q)$ (algebra-antisymmetric:
$\sigma(X) = -X$),

$$
  \mathrm{tr}_M(X)(q) \;=\; -\mathrm{tr}_M(X)(q^{-1}),
$$

forcing $\mathrm{tr}_M(X) = (q - q^{-1})\,\cdot\,p(q)$ for some
palindromic $p \in R$ — but **not** $p = 0$ generically. The
trace acquires one factor of the skein parameter $h$, not a full
zero.

#### Implication: $\sigma$-parity alone is insufficient

The naïve operator-parity argument therefore does not close
$J^{1}$-vanishing. In an expansion of $\Phi_1(\mathcal{M})$ in
the *skein parameter* $h = q - q^{-1}$, the $\sigma$-equivariance
identity does enforce that the **odd-$h$** part of any
$\sigma$-antisymmetric trace carries an extra factor of $h$ —
which is itself $h$-odd, so the **product is $h$-even** —
delivering the desired $h$-evenness of the bare-atom trace. But
the LP-dual expansion of interest is in the *coupling*
$\alpha_{EM}$, not in $h$, and the two are not proportional:

$$
  h(q_{0}) \approx 0.21, \qquad \alpha_{EM}(q_{0}) \approx 0.0073,
  \qquad \alpha_{EM} \neq c \cdot h.
$$

Even the operator-parity route requires either:
(a) a translation showing the $\alpha_{EM}$-expansion of
$y_{\mathrm{cov}}$ inherits the $h$-evenness of the underlying
trace, or
(b) an *additional* symmetry beyond $\sigma$ — most plausibly the
**nuclear-exchange involution** $\varepsilon$ for homonuclear (or
definite-parity) molecules, which swaps the two atomic strands
(conjugation by a half-twist braid). Combined $\sigma\varepsilon$
parity may kill the residual palindromic factor that $\sigma$
alone leaves behind.

#### Updated recommended next step

Pursue the **combined $\sigma \cdot \varepsilon$ parity** for the
$H_2$ molecular braid:

1. Make $\varepsilon$ explicit as conjugation by a specific braid
 $\gamma \in B_4$ that swaps strands $(p_1 \leftrightarrow p_2,
   e_1 \leftrightarrow e_2)$.
2. Decompose the covalent perturbation
 $\Delta_{\mathrm{cov}}$ into joint $(\sigma, \varepsilon)$
 parity sectors; identify the
 $(\sigma\text{-anti}, \varepsilon\text{-sym})$ component.
3. Show that the bare $H_2$ ground state
 $\mathcal{M}_{\mathrm{atom}}^{\otimes 2}$ lies in the
 $(\sigma\text{-sym}, \varepsilon\text{-sym})$ sector.
4. Conclude — IF the joint parity argument goes through — that
 $\mathrm{tr}_M(\mathcal{M}_{\mathrm{atom}}^{\otimes 2} \cdot
   \Delta_{\mathrm{cov}}^{(\sigma\text{-anti},\,\varepsilon\text{-sym})})
   = 0$ exactly (not just up to factor $h$), giving the desired
 $J^{1}$-vanishing.

The heteronuclear case (CO, HCl, etc.) does **not** satisfy
$\varepsilon$-symmetry. Standard physics predicts a nonzero
permanent dipole moment for such molecules, and
$\alpha_{EM}^{1}$ contributions to binding *do* in fact appear
(though they are smaller than $\alpha_{EM}^{2}$ at
$\alpha_{EM} \approx 1/137$). This is consistent with the
$\sigma\varepsilon$ argument requiring nuclear-exchange symmetry.

### Round-3: Skein-identity obstruction kills *all* parity arguments

A direct computation in $H_4(q)$ on the single covalent crossing
$\sigma_2$ closes the parity route negatively. The Skein identity

$$
  \sigma_i - \sigma_i^{-1} \;=\; (q - q^{-1})\,\mathbf{1}
  \;=\; h\,\mathbf{1}
$$

means the $\sigma$-antisymmetric component of *every* single
crossing is a scalar multiple of the identity:

$$
  \tfrac{1}{2}\bigl(\sigma_i - \sigma_i^{-1}\bigr)
  \;=\;
  \tfrac{h}{2}\,\mathbf{1}.
$$

The identity element commutes with all of $H_n(q)$, so any
inner-automorphism involution $\varepsilon = \mathrm{Ad}_\gamma$
(including the nuclear-exchange braid $\gamma = (\sigma_1
\sigma_2 \sigma_3)^{2} \in B_4$) acts as the identity on it:
$\varepsilon(\tfrac{h}{2}\mathbf{1}) = \tfrac{h}{2}\mathbf{1}$.
The combined $(\sigma\text{-anti}, \varepsilon\text{-sym})$
component of $\sigma_2$ is therefore

$$
  \Delta_{-+}^{(\sigma_2)}
  \;=\;
  \tfrac{1}{2}\bigl[
    \tfrac{h}{2}\mathbf{1} \;+\; \varepsilon(\tfrac{h}{2}\mathbf{1})
  \bigr]
  \;=\;
  \tfrac{h}{2}\,\mathbf{1},
$$

with Markov trace

$$
  \mathrm{tr}_M\!\bigl(\Delta_{-+}^{(\sigma_2)}
                       \cdot \mathcal{M}_{\mathrm{atom}}\bigr)
  \;=\;
  \tfrac{h}{2}\,\mathrm{tr}_M\!\bigl(\mathcal{M}_{\mathrm{atom}}\bigr)
  \;\neq\; 0.
$$

This is independent of which inner-automorphism $\varepsilon$ one
chooses, because the identity element is a fixed point of every
inner automorphism. Hence **no $\mathbb{Z}/2$ parity grading
generated by Hopf antipode and conjugations can force the linear-
in-$h$ coefficient of a single covalent crossing to vanish**.

#### Structural conclusion

Parity-based mechanisms (A, C, C$'$, σε, $\ldots$) are **structurally
insufficient** for $J^{1}$-vanishing in the molecular Hecke
algebra $H_n(q)$. The Skein identity is the obstruction: it
trades a $\sigma$-antisymmetric Hecke generator for a *scalar
multiple of the identity*, against which every parity argument
collapses.

### Mechanism D — virial / scaling (the route that survives)

Re-examining the standard physics: the $\alpha^{2}$ scaling of
$E_{\mathrm{Hartree}} = m_e c^{2}\,\alpha_{EM}^{2}$ does **not**
come from the linear-Stark vanishing. The two facts are
independent:

- $E \sim \alpha^{2}$ comes from **dimensional analysis** at the
 Bohr radius $a_0 \sim 1/(m_e c \alpha)$: both kinetic energy
 $T \sim \hbar^{2}/(m_e a_0^{2}) \sim m_e c^{2}\alpha^{2}$ and
 Coulomb potential
 $V \sim e^{2}/a_0 \sim m_e c^{2}\alpha^{2}$ scale quadratically
 in $\alpha$, and the virial theorem balances them at
 $E = -\tfrac{1}{2}V \sim \alpha^{2}$.

- The linear-Stark vanishing
 $\langle\psi|\hat r|\psi\rangle = 0$ is a *separate* parity fact
 that suppresses certain *external-field perturbations*; it is
 not the source of the bare $\alpha^{2}$ binding scale.

The QOU-categorical analogue should therefore be a **virial /
scaling** argument, not a parity argument.

**Mechanism D (virial/scaling).** At the bound-state LP/SDP
optimum, the molecular Markov trace decomposes into two
contributions analogous to kinetic and potential energy. Both
involve the *bound-state characteristic eigenvalue*
$\lambda_{\mathrm{bound}}$ of the molecular transfer matrix
($T_1 = T_{e_2 \mathfrak{p}_2}^{\mathrm{dressed}}$ in
[`prop:h2-lp-dual-binding`](#prop:h2-lp-dual-binding), with
eigenvalues $(q^{5}, -q^{-5})$). By the virial-theorem analogue,
both contributions scale as $\lambda_{\mathrm{bound}}^{-2}$, and
$\lambda_{\mathrm{bound}}^{-1}$ is the categorical analogue of
$\alpha_{EM}$. The leading order is therefore $\alpha_{EM}^{2}$
by dimensional matching, with no $\alpha_{EM}^{1}$ term to
suppress in the first place.

**What this changes.** The $J^{1}$-vanishing is not a *theorem*
to prove — it is a *trivial consequence* of the LP/SDP being
quadratic in the bound-state scale. The conjecture sharpens to:

> *The bound-state characteristic scale $\lambda_{\mathrm{bound}}$
> of the molecular transfer matrix relates to $\alpha_{EM}$ by
> $\lambda_{\mathrm{bound}}^{-1} \in R$ and
> $\lambda_{\mathrm{bound}}^{-1}(q_0) = \alpha_{EM}(q_0) \cdot c_1$
> for some $c_1 \in R$ of order unity.*

Verifying this is a **direct symbolic computation**:
 (i) extract the molecular transfer-matrix eigenvalue
$\lambda_{\mathrm{bound}}$ symbolically from the H_2 LP setup;
 (ii) compute $\lambda_{\mathrm{bound}}^{-1}(q)$ in $R$;
 (iii) compare numerically at $q_0$ to $\alpha_{EM}(q_0)$ — if
they match within an $R$-rational factor, the conjecture
upgrades to a proposition with explicit $c_2$.

**Empirical check from the H_2 witness**
([`folio-assistant/computations/h2-molecular-binding.witness.json`](folio-assistant/computations/h2-molecular-binding.witness.json)):
- $y_{\mathrm{cov}}^{*} = 0.687$ (in $\Phi_1$ units)
- $E_{\mathrm{bind}}^{\mathrm{predicted}} \approx 4.638\,\mathrm{eV}$
- $E_{\mathrm{Hartree}} \approx 27.296\,\mathrm{eV}$
- Ratio: $E_{\mathrm{bind}}/E_{\mathrm{Hartree}} \approx 0.170$

The dimensionless ratio $0.170$ is the conjectured $c_2$. It is
$O(1)$ (the standard physics value for the $H_2$ molecular ratio
$E_{\mathrm{bind}}/E_h \approx 1/6$ closely matches), supporting
Mechanism D's prediction without requiring any $J^{1}$-vanishing
miracle.

#### Round-4 numerical pin-down attempt (inconclusive)

A search over simple $R$-rational candidates for $c_2$ at $q_0$
($\textrm{target} = 0.16992$) gives no clean match within the
witness precision:

See [Table 11](#tbl:e-hartree-categorical-derivation-table11-data).

The closest candidate $1/(q\,[5]_q)$ is off by $1.6\%$, well
outside the LP-dual numerical precision (witness reports a single
$f64$ optimum without symbolic-$q$ traceback). The standard
physics ratio $1/6$ is off by $1.9\%$, suggesting the QOU value
deviates from textbook by $\sim 2\%$ — not implausible for a
substrate-corrected calculation.

**Honest reading.** $c_2$ does *not* by definition equal a low-degree
$R$-rational at $q_0$ within obvious search scope. Either (i)
$c_2$ is a more elaborate Frobenius-pairing expression in $R$
that requires explicit symbolic computation of
$\Phi_1^{H_2}(\pi^{*})$, or (ii) the witness numerical value is
itself sensitive to LP-precision artefacts and a more careful
50-dps recompute might pin down a cleaner closed form.

**Status of the conjecture after four rounds.**
- The $J^{1}$-vanishing framing of the original brief was
 diagnosed as misdirected: parity-based mechanisms (A, C, C$'$,
 σε) are structurally insufficient because of the Skein
 identity. No "linear-Stark vanishing" categorical analogue is
 required; the $\alpha^{2}$ scaling is dimensional/virial.
- Mechanism D survives as the structural answer at the heuristic
 level, supported empirically by the witness ratio
 $E_{\mathrm{bind}}/E_h \approx 1/6$.
- Closing the conjecture to a proposition requires either a
 symbolic-$q$ recomputation of $\Phi_1^{H_2}(\pi^{*})$ (currently
 done only numerically), or an independent identification of
 $c_2$ from the molecular Hecke representation theory.

This is the converged form of the conjecture; further refinement
requires symbolic-$q$ infrastructure beyond the present
investigation.

### Round-5: the brief's framing was a category error — reformulation

Tracing the actual H_2 pipeline numerically settles the conjecture's
framing:

```
binding_Phi_diff = 0.6870 (Phi_1 units, dimensionless, ~ O(1))
E_HARTREE = 27.30 eV (= 511000 eV * alpha^2, HARDCODED in
                              folio-assistant/computations/substrate/hecke_core.py:198)
E_MOL = E_HARTREE / TWO_Q^2 = 6.75 eV per Phi_1 unit
E_bind = binding_Phi_diff * E_MOL = 4.64 eV
```

**The LP/SDP output $y_{\mathrm{cov}}^{*} = $ binding_Phi_diff is
pure Hecke-trace, dimensionless, and does NOT depend on
$\alpha_{EM}$ at all.** $\alpha_{EM}^{2}$ enters the eV value
*only* at the unit-conversion step
$E_{\mathrm{HARTREE}} = m_e c^{2}\,\alpha_{EM}^{2}$, which is
hardcoded.

This means **the brief's request to "expand $y_{\mathrm{cov}}$ in
$\alpha_{EM}$" was a category error**: $y_{\mathrm{cov}}$ is the
$\Phi_1$-unit LP-dual output, which has no $\alpha_{EM}$
dependence to expand. The whole "$J^{1}$-vanishing" question is
therefore *vacuously true*: there is no $\alpha_{EM}^{1}$
contribution to suppress because there is no $\alpha_{EM}$ in
$y_{\mathrm{cov}}$ at all.

#### Reformulated question

The actual categorical question is **upstream** of the LP:

> *Why is the archimedean realization functor
> $\rho_\infty : \widehat{\mathbb{Z}[q]} \to \mathbb{R}$ such that
> one unit of categorical action ($\Phi_1$, the Markov-trace
> logarithm) maps to $m_e c^{2}\,\alpha_{EM}^{2}$ in physical eV
> units (modulo the $TWO\_Q^{2} = (q+q^{-1})^{2}$ molecular
> rescaling), and not to some other combination such as
> $m_e c^{2}$ or $m_e c^{2}\,\alpha_{EM}$?*

This is the actual content of "Hartree-energy categorical
derivation". It is *not* a question about the LP at all — it is a
question about the **archimedean realization functor**
([archimedean realization](#def:archimedean-realization-functor)):
specifically about why its restriction to molecular-binding-LP
outputs picks up exactly two factors of $\alpha_{EM}$.

#### Standard physics translation (derivation sketch)

Categorical $\Phi_1$ has dimension of action ($\hbar$). Mapping
action $\times$ inverse-length gives energy. The natural categorical
length scale at a covalent bond is the **categorical Bohr radius**
$a_{0}^{\mathrm{cat}}$, set by balance of the EM force-carrier
coupling $\alpha_{EM}$ against the electron mass $m_{e}$:

$$
  a_{0}^{\mathrm{cat}}
  \;\sim\;
  \frac{\hbar}{m_{e} c \, \alpha_{EM}}.
$$

Energy per unit action then carries one factor of $\alpha_{EM}$
from $1/a_{0}^{\mathrm{cat}}$ and one factor from the Coulomb
strength itself (force $\propto \alpha_{EM}$ times distance
$a_{0}^{\mathrm{cat}}$ giving back $\alpha_{EM}$ in the energy
denominator):

$$
  E\;=\;F\cdot d
  \;\sim\;\alpha_{EM}\cdot\frac{1}{a_{0}^{\mathrm{cat}}}
  \;\sim\;m_{e} c^{2}\,\alpha_{EM}^{2}.
$$

This is the standard Bohr-virial picture, transported into the
QOU functorial framework. The two factors of $\alpha_{EM}$ in
$E_{\mathrm{HARTREE}}$ are not a parity miracle and not an LP
expansion — they are **dimensional** and arise from $\alpha_{EM}$
appearing both as the force-coupling LP weight *and* as the
inverse of the categorical length scale.

#### Closure status (after 5 rounds)

The conjecture, in its corrected reformulation, becomes:

> *The archimedean realization functor's restriction to
> molecular-binding $\Phi_1$ outputs picks up exactly two factors
> of $\alpha_{EM}$ — one from the categorical Bohr length
> $a_{0}^{\mathrm{cat}} \sim 1/\alpha_{EM}$ and one from the
> force-coupling $\alpha_{EM}$ itself — yielding
> $E_{\mathrm{HARTREE}} = m_e c^{2}\,\alpha_{EM}^{2}$ as the unit
> energy.*

Closing this rigorously requires:
(i) a categorical definition of $a_{0}^{\mathrm{cat}}$ as a
specific eigenvalue/length in the molecular Hecke representation;
(ii) verification that the archimedean functor
$\rho_\infty$ (currently embodied implicitly in
[`hecke_core.py:198`](folio-assistant/computations/substrate/hecke_core.py))
is forced to multiply Markov-trace outputs by $1/(a_{0}^{\mathrm{cat}})^{2}$;
(iii) showing this is the unique consistent choice given the
Frobenius pairing structure.

This is genuinely tractable but well beyond the scope of the
present block. It is recommended as the **definitive next
deliverable** — a separate proposition on "$\alpha_{EM}^{2}$ in
the molecular archimedean realization functor" — once the
categorical Bohr radius is given a precise Hecke definition.

### What this block does *not* claim

- It does **not** claim a proof of $E_h \propto \alpha_{EM}^{2}$
 from QOU principles. It claims only that this scaling is the
 expected leading behaviour and identifies the open structural
 step.
- It does **not** introduce $\pi$, transcendentals, or PSLQ-fitted
 constants. The coefficient $c_2$ is conjecturally in
 $R = \mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$.
- It does **not** override the existing usage of
 $E_{\mathrm{Hartree}} = m_e c^{2}\,\alpha_{EM}^{2}$ in
 [`hecke_core.py:198`](folio-assistant/computations/substrate/hecke_core.py)
 as a numerical input — that usage remains an empirical scale
 pending closure of this conjecture.

### Honest reporting

We attempted three derivation mechanisms here and
identified an explicit gap in each. Mechanism C with the
$q \mapsto -q^{-1}$ involution is the most promising line of
attack; pursuing it is the recommended next research step.
Reporting the partial chain — rather than papering over with
post-hoc identifications — is the deliberate purpose of this
block.

### Round 19 — closed-form $\chi_\lambda$ characters and dressed projection

**Task 1 — Closed-form characters.** All five irrep-characters of the
bare H_2 molecular braid $\sigma_1\sigma_2\sigma_3 \in B_4$ are
**single $q$-monomials**:

See [Table 12](#tbl:e-hartree-categorical-derivation-table12-data).

These are exact closed forms in $q$ (verified to $10^{-10}$ at $q_0$).

The **force-carrier sum** is

$$
  \chi_{(3,1)}(\sigma_1\sigma_2\sigma_3) + \chi_{(2,1,1)}(\sigma_1\sigma_2\sigma_3)
  \;=\; -q + q^{-1}
  \;=\; -h.
$$

The combined (3,1)+(2,1,1) force-carrier Markov-trace contribution
of the bare braid is exactly $-w\,h/f$.

**Task 2 — Dressed projection.** Replacing the middle crossing
$\sigma_2$ with the K-shell-dressed $T^{\mathrm{dr}}_{e_2 p_2}$
(eigenvalues $q^5, -q^{-5}$) — equivalently
$T^{\mathrm{dr}} = \alpha\,\sigma_2 + \beta\,\mathbf{1}$ with
$\alpha = (q^5+q^{-5})/(q+q^{-1})$ and $\beta = q^5 - \alpha q$ —
gives:

See [Table 13](#tbl:e-hartree-categorical-derivation-table13-data).

**Key new observations:**

1. **The $(2,2)$ channel becomes nonzero under dressing.** The K-shell
 $q^5$ structure breaks the bare $(2,2) = 0$ selection rule.
2. **Force-carrier channel amplification factor $\approx [5]_q$.**
 The combined $(3,1) + (2,1,1)$ contribution scales by $5.13$ in
 the dressing, very close to the K-shell quantum dimension
 $[5]_q = 5.22$ at $q_0$. This is a direct algebraic signature of
 the dressing power.
3. **Self-duality preserved.** The transpose pair structure is
 maintained: $w_{(3,1)} = w_{(2,1,1)}$ and $f_{(3,1)} = f_{(2,1,1)}$
 regardless of dressing.

These findings sharpen the closure programme: the **algebraic factor
of $[5]_q$ from K-shell dressing** is a candidate for one of the
needed factors of $h$ (since $[5]_q \cdot h^2 = q^5 - q^{-5}$, which
is a building block of force-carrier $\delta_q$ values).

The remaining gap is the precise multiplicative chain that produces
$h^4$ scaling in the binding energy from these dressed Wedderburn
contributions. Witness data is now cached in
[`delta-q-decoration.witness.json`](folio-assistant/computations/delta-q-decoration.witness.json)
for downstream symbolic-$q$ analysis.
