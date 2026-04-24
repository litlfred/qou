The unified knot mass formula
([unified knot mass](#thm:knot-mass-formula-unified)) has six
structural terms.  Earlier commentary suggested these emerge as
pages of a **spectral sequence** associated with the Gröbner–Shirshov
filtration $J^\bullet(q)$ on $H_n(q)$.  This proposition makes the
spectral-sequence structure precise and states the $E_\infty$
convergence target.

**Definition (filtered differential algebra).**
*The Hecke algebra $H_n(q)$ with the confinement filtration
$J^\bullet(q)$
([confinement level](#def:confinement-level)) carries a natural
differential $d$ induced by the three Gröbner–Shirshov rewriting
rules
([Hecke normal form](#def:hecke-normal-form)):*

1. *Hecke relation: $d_{\mathrm{H}}(\sigma_i^2) = (q - q^{-1})\sigma_i + \mathbf{1}$.*
2. *Far commutativity: $d_{\mathrm{F}}(\sigma_i \sigma_j) = \sigma_j \sigma_i$ for $|i - j| \geq 2$.*
3. *Yang–Baxter: $d_{\mathrm{YB}}(\sigma_i \sigma_{i+1} \sigma_i) = \sigma_{i+1} \sigma_i \sigma_{i+1}$.*

*Each rule lowers filtration degree (the RHS sits in the same or
lower stratum than the LHS).  The direct sum $d = d_H + d_F + d_{YB}$
satisfies $d \circ d = 0$ on the filtered complex (after
normalisation), making $(H_n(q), J^\bullet, d)$ a **filtered
differential algebra**.*

**Proposition (GB spectral sequence).**
*The filtered differential algebra $(H_n(q), J^\bullet, d)$ has an
associated spectral sequence $(E_r^{\ell, *}, d_r)$ with:*

$$
  E_0^{\ell, *} \;=\; J^\ell(q) / J^{\ell+1}(q)
  \qquad \text{(associated graded)},
$$

$$
  E_1^{\ell, *} \;=\; H^*\bigl(J^\ell / J^{\ell+1},\ d\bigr)
  \qquad \text{(Hochschild-type cohomology of each stratum)},
$$

*and higher pages $E_r^{\ell, *}$ obtained by successive
homology of the $d_r$ differential.*

*Convergence:*

$$
  E_\infty^{\ell, *}
  \;\Longrightarrow\;
  \mathrm{gr}^\ell\bigl(H_n(q)\bigr).
$$

*The Markov trace $\mathrm{tr}_M: H_n(q) \to \mathbb{C}$ is a
$d$-closed linear functional (by cyclicity) and therefore descends
to $E_\infty$.*

**Identification of the six mass terms with spectral-sequence pages.**

*Pairing $\mathrm{tr}_M$ against the braid word $T_w$ decomposes
over the spectral sequence pages as:*

| page | contribution | mass term |
|---|---|---|
| $E_\infty^{0, *}$ | $\mathrm{tr}_M$ on associated-graded filtration-$0$ part of $T_w$ | descended $\|\mathrm{tr}_M(T_w)\|$ (Term 1) |
| $E_\infty^{1, *}$ | single-generator residue at $\zeta_1 = 1$ pole | single-gen tower $\sum \Phi_q(\|\hat V_i\|)$ (Term 2) |
| $E_\infty^{2, *}$ | pair-generator residue at $\zeta_1$ | pair-gen tower $z^2 \sum \Phi_q$ (Term 3) |
| full $E_\infty$ pairing | $\sum_\lambda 1/\dim_q(\lambda)$ (Frobenius co-Casimir) | Term 4 (universal) |
| braid-closure ribbon | self-pairing $\tau(\beta \beta^*)$ | chirality $a_K$ (Term 5) |
| $E_\infty^{\ell \geq 3, *}$ | higher-stratum prefix corrections | jet-level prefix (Term 6, open) |

**Why this is a rigorisation target, not a proof.**

*The proposition states the spectral-sequence structure but **does
not prove**:*

1. *$d \circ d = 0$ on the filtered complex (requires detailed
   Gröbner–Shirshov confluence analysis).*
2. *Convergence $E_\infty \Rightarrow \mathrm{gr}\,H_n(q)$
   (requires a regularity condition on the filtration — essentially
   bounded below and exhaustive, which $J^\bullet$ is).*
3. *The identification of $E_\infty$ pages with the six mass terms
   is **assertion, not theorem**.  Term 1 is clearly $E_\infty^{0, *}$
   by construction; Terms 2, 3 follow from the pole structure of
   $\Phi_q$; Term 4 is the character-theoretic identity
   ([Frobenius universal](#thm:frobenius-codim-universal)); Terms 5,
   6 are open.*

*A complete rigorous derivation would require:*

- *Construct the Hochschild cochain complex
  $C^*(H_n(q), H_n(q))$ equipped with the filtration induced by
  $J^\bullet(q)$.*
- *Show $\mathrm{tr}_M$ is a Hochschild cocycle (follows from
  cyclicity of Markov trace).*
- *Compute the spectral sequence pages $E_r$ explicitly for small
  $n$ (say $n = 3$) and verify the decomposition.*
- *Match each page to the corresponding mass term via the
  $\Phi_q$/Frobenius/chirality identifications above.*

*This is a **research-level formalisation task** — likely a
multi-week project in cohomological algebra / deformation theory.
The proposition flags the target; the work is open.*

**Structural value.**

*Even as a conjecture, the spectral-sequence framing clarifies:*

1. *The **six terms are not arbitrary** — they are the non-trivial
   pages of a canonical spectral sequence.*
2. *The **sum is total cohomology** of the filtered Hecke algebra
   paired with $T_w$ — a well-defined algebraic invariant.*
3. *The **regime switching**
   ([mass formula regime switching](#prop:mass-formula-regime-switching))
   is not ad-hoc but reflects **which pages dominate** for different
   $A$ — a feature of the spectral sequence, not a failure of
   additivity.*

**Relation to other formalisations.**

- *Hochschild cohomology of Hecke algebras $HH^*(H_n(q))$ is
  computed in Kosmann-Schwarzbach, Lambe–Stasheff, and extended
  by Burciu–Scheimbauer.  These give **deformation-theoretic**
  input: $HH^2$ controls deformations, $HH^3$ controls obstructions.*
- *Our filtration $J^\bullet(q)$ is **specific to the substrate
  parameter $q$** and finer than the standard length filtration;
  the resulting spectral sequence has $q$-dependent differentials.*
- *Reshetikhin–Turaev invariants at roots of unity are the
  **residues** of the $E_\infty$ pages at filtration-collapsing
  $q = \zeta_\ell$ — the RT evaluation is the spectral-sequence
  specialisation.*

*This connects the paper's mass formula to the broader machinery
of quantum topology and deformation theory — the unification
target is to show that the six-term mass is a specific
**spectral-sequence cohomology class** paired with the atomic
braid, computable from the Hecke algebra alone.*
