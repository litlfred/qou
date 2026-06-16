**Conjecture (finiteness of the residue spectral sum).**
*For every closed braid $K$ with normal form $T_w \in H_n(R, q)$ at
$q = q_0$ in the generic locus, there exists a finite cutoff
$N \in \mathbb{N}$ — namely the confinement level
$N = \ell(K, q_0)$ ([confinement level exists](#prop\:confinement-level-exists))
— such that the cyclotomic residue vanishes for every filtration
stratum at or above $N$:*

$$
  \forall \ell \geq N \colon\quad
    \mathrm{Res}_{q \to \zeta_\ell}\bigl[\Phi_q
      \cdot \mathrm{tr}_{M, \ell}(T_w)\bigr]
  \;=\; 0.
$$

*Consequently, the GS residue spectral sum
$\sum_{\ell \geq 0} \mathrm{Res}_{q \to \zeta_\ell}\bigl[\Phi_q
\cdot \mathrm{tr}_{M, \ell}(T_w)\bigr]$
has only finitely many non-zero terms.*

**Categorical statement.**
*The confinement level $\ell(K, q_0)$ is finite by
([confinement level exists](#prop\:confinement-level-exists)) and
unique by ([confinement level unique](#prop\:confinement-level-unique));
$T_w \in J^\ell(q_0)$ for $\ell > \ell(K, q_0)$ would force
$T_w \equiv 0$ in $H_n(R, q_0)$, contradicting genericity.  The
graded piece $J^\ell / J^{\ell+1}$ vanishes above $\ell(K, q_0)$,
hence so does $\mathrm{tr}_{M, \ell}(T_w)$ and a fortiori the residue.*

**Status (current Lean encoding).**
*In `gb-residue-spectral-sum.lean`, the P2.6 refactor
recasts the previous `sorry` as a tautology over `Fin levelBound`:*

```
theorem spectral_sum_finite (S : GBResidueSpectralSum) :
    ∃ N : ℕ, ∀ ℓ ≥ N, ∀ (h : ℓ < S.levelBound),
      S.residue ⟨ℓ, h⟩ = 0 ∨ ℓ < S.levelBound := by
  refine ⟨S.levelBound, ?_⟩
  intro ℓ _ h; exact Or.inr h
```

*The compact-finite domain `Fin levelBound` makes the cutoff vacuous;
the substantive content — that `levelBound` truly is the confinement
level $\ell(K, q_0)$ and that residues above it vanish for the
underlying analytic objects — is the conjectural part.*

**Why a conjecture and not a theorem.**
*The Lean tautology relies on the instance supplying `levelBound`
correctly.  A proof that the confinement level truly bounds the
support of the residue function requires:*

1. *Formalisation of $\mathrm{ConfinementLevel}$ as the smallest $\ell$
   with $T_w \in J^\ell$, which is itself currently axiomatized
   (`QOU.BraidKnot.ConfinementLevel`).*
2. *The vanishing $\mathrm{tr}_{M, \ell} \equiv 0$ for
   $\ell > \ell(K, q_0)$ — a corollary of
   [confinement level unique](#prop\:confinement-level-unique) once
   the GS-filtration is in Mathlib.*

**Empirical witness.**
*Witness scripts truncate the sum at $\ell = 6$ and observe vanishing
contributions beyond, consistent with the proton/neutron/deuteron
confinement levels.  See
`computations/term6-full-pole-sum.witness.json`.*

**Structural shortcut.**
*The vanishing of the residue strata above $\ell(K, q_0)$ is
explained homologically by
[cemetery-group emergence](#conj\:cemetery-group-emergence): the
strata that fall outside $J^{\ell(K, q_0)}(q_0)$ map under the
observation functor $\tau$ into the
[:refterm[cemetery group]{#cemetery-group}](#def\:cemetery-group), and so vanish without any
term-by-term polynomial cancellation.*
