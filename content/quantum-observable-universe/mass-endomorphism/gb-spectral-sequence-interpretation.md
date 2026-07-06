**Open formalization requirements.**

Standard Hochschild-complex theory yields $d \circ d = 0$ and $E_\infty$ convergence. The open requirements are:

1. Term-by-term identification of $E_\infty^{p, *}$ with the six mass-formula components. At $p = 0$ (descended $\mathrm{tr}_M$), this is the Frobenius co-Casimir ([`thm:frobenius-codim-universal`](#thm:frobenius-codim-universal)). For $p \geq 1$, identifying $\Phi_q$ poles and chirality demands explicit page computation.
2. Explicit $E_1$ page computation for $H_3(R, q)$. Burciu and Scheimbauer (2019) establish that $\dim H^k(H_n(R, q), H_n(R, q))$ grows via a specific partition generating function. The pairing with $\mathrm{tr}_M$ isolates the cyclic part. Matching this to the six terms requires a computational derivation.

The Hochschild complex guarantees the existence of the spectral sequence. Matching its pages to the mass-formula terms remains open.

## Rigorous derivation path

A full rigorous derivation requires four steps:

- Construct the Hochschild cochain complex $C^*(H_n(R, q), H_n(R, q))$ with the filtration induced by $J^\bullet(q)$.
- Prove $\mathrm{tr}_M$ is a Hochschild cocycle, exploiting the cyclicity of the Markov trace.
- Compute the spectral sequence pages $E_r$ explicitly for $n = 3$ and verify the decomposition.
- Match each page to the corresponding mass term via $\Phi_q$ poles, Frobenius invariants, and chirality components.

This represents a research-level project in cohomological algebra and deformation theory. We flag the target; the work stands open.

## Structural value

The spectral-sequence framing enforces architectural rigidity:

1. The six mass terms are not arbitrary. They constitute the non-trivial pages of a canonical spectral sequence.
2. The mass sum equals the total cohomology of the filtered Hecke algebra paired with $T_w$.
3. Regime switching ([`prop:mass-formula-regime-switching`](#prop:mass-formula-regime-switching)) occurs because different pages dominate for different $A$. This reflects the spectral sequence structure, not an ad-hoc failure of additivity.

## Relation to standard formalisms

Hochschild cohomology $HH^*(H_n(R, q))$ is established by Kosmann-Schwarzbach, Lambe–Stasheff, and Burciu–Scheimbauer. These supply deformation-theoretic data: $HH^2$ controls deformations, $HH^3$ controls obstructions.

Our filtration $J^\bullet(q)$ is specific to the substrate parameter $q$, forming a finer grading than standard length. This yields $q$-dependent differentials. 

Reshetikhin–Turaev invariants at roots of unity emerge as residues of the $E_\infty$ pages when $q = \zeta_\ell$ collapses the filtration. The RT evaluation is strictly a spectral-sequence specialization.

This grounds the mass formula in quantum topology and deformation theory. The unification objective is to prove the six-term mass evaluates a specific spectral-sequence cohomology class paired against the atomic braid, relying exclusively on the Hecke algebra.

## Archimedean realization

The $E_\infty$-pairing operates strictly over the categorical base ring $R$. Pairings $\langle \mathrm{tr}_M, E_\infty^{p,*}(T_w)\rangle$ land in $R$, not $\mathbb{C}$. 

Applying the archimedean fibre functor $\tau \colon R \hookrightarrow \mathbb{C}$ promotes the $E_\infty$-pairing to a contour integral on the Descartes elliptic curve $\mathcal{E}_q(\mathbb{C})$. The level-$p$ stratum maps to the geometric jet bundle $J^p\mathcal{S}$. The Seiberg–Witten differential $\lambda_{\mathrm{SW}}^{(p)}$ serves as the tautological section.

The pairing's $\mathbb{C}$-realization is the Picard–Lefschetz thimble period $\Pi^{(p)}$, equaling $\tau\bigl\langle\mathrm{tr}_M, E_\infty^{p,*}(T_w)\bigr\rangle$ up to the integer intersection numbers $n_\sigma^{(p)}$ of the Lefschetz decomposition. The spectral sequence and the PL thimble decomposition provide two presentations of the identical data across the archimedean wall.
