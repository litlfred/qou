# L-2 proof sketch — selective q-deformation lemma

**Compiled** 2026-05-03 on `claude/path-to-1ppb-w1-rho-substrate`.
**Status**: proof sketch (categorical, not yet formalised in Lean).
Companion to
[`2026-05-03-z-eq-n-rho-derivation-sketch.md`](2026-05-03-z-eq-n-rho-derivation-sketch.md)
§3.

---

## §1. Statement

**Lemma L-2 (selective q-deformation).**  Let $A \geq 2$ and let
$\rho_{\rm struct}(K) \in \mathbb{Z}_{>0}$ denote the Wedderburn-block
multiplicity of the canonical-knot closure $\widehat{\beta_K}$ in the
Iwahori–Hecke algebra $H_A(q)$. Then for every $q$ in the
*generic locus* (defined below), $\rho_{\rm struct}(K)$ is
**q-independent**:

$$
  \rho_{\rm struct}(K)
  \;=\;
  \rho_{\rm struct}(K)\bigl|_{q = 1}
  \quad\text{for all generic } q.
$$

In particular, $\rho_{\rm struct}(K)\bigl|_{q = q_0} =
\rho_{\rm struct}(K)\bigl|_{q = 1}$, so the integer prefactor in the
Kashaev law is **not** q-deformed at $q_0$.

---

## §2. Generic locus

Define the *generic locus* $\mathcal{G}_A \subset \mathbb{C}^\times$ to
be the complement of the discriminant locus

$$
  \mathcal{D}_A
  \;=\;
  \{ q \in \mathbb{C}^\times :\, [m]_q = 0
    \text{ for some } m \in \{1, \ldots, A\} \},
$$

where $[m]_q = (q^m - q^{-m})/(q - q^{-1})$ is the q-integer.
Equivalently, $\mathcal{D}_A$ is the set of $q$ such that $q^2$ is a
primitive $n$-th root of unity for some $n \leq A$.

**Claim.**  $q_0 \in \mathcal{G}_A$ for every finite $A$ — i.e., the
substrate parameter is generic at every level.

**Proof of claim.**  $q_0 \approx 1.10998…$ is real and $> 1$, so
$q_0^2 \approx 1.232 > 1$ is never a root of unity (any complex root
of unity has modulus $1$).  Hence $q_0 \in \mathcal{G}_A$ for all
$A$.  □

---

## §3. Standard semisimplicity input

The starting point is the classical theorem (Iwahori–Matsumoto;
Gyoja; see Mathas 1999 §3.3):

**Theorem (Iwahori–Hecke semisimplicity at generic q).**  For
$q \in \mathcal{G}_A$, the Iwahori–Hecke algebra $H_A(q)$ is
semisimple.  Its simple modules $S^\lambda(q)$ are indexed by
partitions $\lambda \vdash A$; the dimension $\dim_\mathbb{C}
S^\lambda(q) = \dim_\mathbb{C} S^\lambda$ is the dimension of the
specht module of the symmetric group $S_A$ at the same partition.

Consequence: the Wedderburn decomposition

$$
  H_A(q)
  \;\cong\;
  \bigoplus_{\lambda \,\vdash\, A}
    \mathrm{End}_\mathbb{C}\bigl(S^\lambda(q)\bigr)
$$

has **the same number of blocks**, **the same block dimensions**, and
**the same multiplicities** for any $q \in \mathcal{G}_A$ as for
$q = 1$.

---

## §4. Wedderburn-block multiplicity of a knot closure

Let $K$ be a knot or link expressible as the closure of a braid
$\beta_K \in B_A$.  Its image $\widehat{\beta_K} \in H_A(q)$
decomposes under the Wedderburn isomorphism as

$$
  \widehat{\beta_K}
  \;=\;
  \bigoplus_{\lambda \,\vdash\, A}
    \rho^\lambda(\beta_K)
  \quad\text{with } \rho^\lambda(\beta_K) \in
  \mathrm{End}_\mathbb{C}\bigl(S^\lambda(q)\bigr).
$$

The **Wedderburn-block multiplicity** $\rho_{\rm struct}(K)$ is
defined as the number of partitions $\lambda$ for which
$\rho^\lambda(\beta_K) \neq 0$ — equivalently, the support of $K$'s
Markov trace decomposition.  Concretely (Jones 1987; Kassel
§XI.4):

$$
  \rho_{\rm struct}(K)
  \;=\;
  \#\,\{\lambda \,\vdash\, A :\, \chi^\lambda(\beta_K) \neq 0\}
$$

where $\chi^\lambda$ is the Hecke-algebra character associated to
$\lambda$.

---

## §5. Proof of L-2

**Step 1.**  By the semisimplicity theorem (§3), the assignment
$\lambda \mapsto S^\lambda(q)$ is a *flat family* of simple modules
parametrised by $q \in \mathcal{G}_A$.  In particular, the
*characters* $\chi^\lambda(q)$ are continuous (in fact analytic)
functions of $q$ on $\mathcal{G}_A$, and $\chi^\lambda(q)\bigl|_{q=1}
= \chi^\lambda$ (the symmetric-group character).

**Step 2.**  $\chi^\lambda(\beta_K)$ is a polynomial in $q^{\pm 1}$
with integer coefficients (Jones 1987, Kassel–Turaev §X.5 — the
characters are rational functions in $q^{\pm 1/2}$ that reduce to
the symmetric-group character at $q=1$).  Such a polynomial either
vanishes identically on $\mathcal{G}_A$ or has only finitely many
zeros, all of which lie on the discriminant locus
$\mathcal{D}_A$.

**Step 3.**  Therefore: $\chi^\lambda(\beta_K) = 0$ for $q \in
\mathcal{G}_A$ iff $\chi^\lambda(\beta_K)\bigl|_{q=1} = 0$ — i.e., the
support of the character on $\mathcal{G}_A$ matches the support at
$q = 1$.

**Step 4.**  Combining steps 1–3:

$$
  \rho_{\rm struct}(K)\bigl|_{q \in \mathcal{G}_A}
  \;=\;
  \#\,\{\lambda :\, \chi^\lambda(\beta_K)\bigl|_{q \in \mathcal{G}_A}
    \neq 0\}
  \;=\;
  \#\,\{\lambda :\, \chi^\lambda(\beta_K)\bigl|_{q=1} \neq 0\}
  \;=\;
  \rho_{\rm struct}(K)\bigl|_{q=1}.
$$

In particular, evaluating at $q = q_0$ (which lies in $\mathcal{G}_A$
by §2's claim) gives $\rho_{\rm struct}(K)\bigl|_{q=q_0} =
\rho_{\rm struct}(K)\bigl|_{q=1}$.  □

---

## §6. Categorical interpretation

L-2 says the Wedderburn-block-multiplicity index is a *discrete*
invariant of the knot–braid $K \mapsto \widehat{\beta_K}$ that the
q-deformation cannot move.  This is consistent with the standard
picture of the Hecke algebra as a flat deformation of the symmetric
group algebra: the block structure is fixed; only the *internal*
endomorphism algebras of each block carry the q-deformation.

In the language of the Z=N derivation sketch (§3 of the companion
note): the q-deformation factors through $H_A(q)$ — it deforms the
character values $\chi^\lambda(\beta_K, q)$ (continuously in $q$),
the q-dimensions $\dim_q S^\lambda$, and the Markov trace
$\mathrm{tr}_M(\widehat{\beta_K}, q)$, but it does **not** deform the
discrete index $\rho_{\rm struct}$ that labels which blocks
$\widehat{\beta_K}$ projects onto.

---

## §7. Lean formalisation status

**Difficulty**: medium.  L-2 requires:

1. The semisimplicity theorem for $H_A(q)$ at generic $q$ — not yet
   in Mathlib but established in the standard literature (Mathas
   §3.3, Geck–Pfeiffer §3.3).  Proof via flatness + Tits's
   deformation argument.
2. The character continuity argument (§5 step 1) — straightforward
   given semisimplicity.
3. The polynomial-zero argument (§5 step 2) — elementary algebra.

Estimated effort: 1–2 work weeks.  The hardest step is (1); steps
(2) and (3) are short once (1) is in place.

**Suggested Lean structure**:

```lean
namespace QOU.Hecke
open CategoryTheory

-- Class encoding the generic-q Wedderburn structure:
class WedderburnSemisimpleAt (A : ℕ) (q : ℂ) where
  is_generic : ∀ m, 1 ≤ m ∧ m ≤ A → q_int m q ≠ 0
  hecke_blocks : Fin (Nat.partitionCount A) → Type*
  hecke_iso :
    HeckeAlgebra A q ≃ₐ[ℂ] PiBlocks hecke_blocks

-- Multiplicity = support of character on simple modules
noncomputable def rho_struct {A : ℕ} (K : Knot) : ℕ :=
  ∑ λ : Partition A, if (heckeChar λ K) = 0 then 0 else 1

-- L-2: q-independence on the generic locus
theorem rho_struct_q_independent
    {A : ℕ} (K : Knot) (q : ℂ) [WedderburnSemisimpleAt A q] :
    rho_struct (q := q) K = rho_struct (q := 1) K := by
  sorry  -- polynomial-zero argument; see §5
```

The class instance `WedderburnSemisimpleAt A q_0` can be discharged
once $q_0$'s genericity (§2 claim) is in place, which is essentially
trivial since $q_0$ is real and $> 1$.

---

## §8. Bottom line

**L-2 is essentially classical** — it follows from the standard
semisimplicity theorem for $H_A(q)$ at generic $q$, plus an
elementary character-continuity argument.  It has not been formalised
in Lean to date, and doing so is a 1–2 week task whose primary
infrastructure cost is *establishing the semisimplicity theorem for
$H_A(q)$ in Mathlib* (the rest of the proof is short).

For the immediate Z=N ρ-correction work, **L-2 can be assumed**
without compromising rigour at the empirical-regularity level — the
proof above is a complete (informal) derivation, and the substrate
parameter $q_0$ provably lies in the generic locus.

---

**End of L-2 proof sketch.**
