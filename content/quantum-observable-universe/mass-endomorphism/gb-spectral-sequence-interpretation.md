**What remains open after this derivation.**

*The $d \circ d = 0$ and $E_\infty$ convergence are now **derived**
from standard Hochschild-complex theory.  What remains open:*

1. *Term-by-term identification of $E_\infty^{p, *}$ with the six
   mass-formula pieces.  For $p = 0$ (descended $\mathrm{tr}_M$)
   and the Frobenius co-Casimir
   ([Frobenius universal](#thm:frobenius-codim-universal)) this
   is clear; for $p \geq 1$ the identification with $\Phi_q$ poles
   and chirality requires explicit page computation.*
2. *Explicit $E_1$ page computation for $H_3(R, q)$ —
   $\dim H^k(H_n(R, q), H_n(R, q))$ is known from
   Burciu–Scheimbauer (2019) to grow like a specific partition
   generating function, but the pairing with
   $\mathrm{tr}_M$ isolates only the cyclic part.  Matching this
   to the six terms is a **computational** task.*

*So the **existence of the spectral sequence** is derived (via
Hochschild complex standard theory); the **matching of its pages
to the six mass-formula terms** remains the open identification
problem.*

**Why this is still only a partial rigorisation.**

*A complete rigorous derivation would require:*

- *Construct the Hochschild cochain complex
  $C^*(H_n(R, q), H_n(R, q))$ equipped with the filtration induced by
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

- *Hochschild cohomology of Hecke algebras $HH^*(H_n(R, q))$ is
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

**Archimedean realisation: the $\mathbb{C}$-side of the
$E_\infty$-pairing is a Picard–Lefschetz period.**
*Strict archimedean split: the spectral sequence above lives
entirely over the categorical base ring $R$ — pairings
$\langle \mathrm{tr}_M, E_\infty^{p,*}(T_w)\rangle$ land in $R$,
not $\mathbb{C}$.  Applying the archimedean fibre functor
$\tau \colon R \hookrightarrow \mathbb{C}$ promotes the
$E_\infty$-pairing to a contour integral on the Descartes elliptic
curve $\mathcal{E}_q(\mathbb{C})$.  Specifically, the level-$p$
stratum corresponds via
(jet-GB-PL correspondence)
to the geometric jet bundle $J^p\mathcal{S}$, on which the
Seiberg–Witten differential $\lambda_{\mathrm{SW}}^{(p)}$ is the
tautological section.  The pairing's $\mathbb{C}$-realisation is
the Picard–Lefschetz thimble period $\Pi^{(p)}$
(SW-period thimble equivalence),
which equals $\tau\bigl\langle\mathrm{tr}_M,
E_\infty^{p,*}(T_w)\bigr\rangle$ up to the integer intersection
numbers $n_\sigma^{(p)}$ of the Lefschetz decomposition.  The
spectral sequence and the PL thimble decomposition are therefore
two presentations of the same data on opposite sides of $\tau$;
their agreement is the content of
(SW-period thimble equivalence).*
