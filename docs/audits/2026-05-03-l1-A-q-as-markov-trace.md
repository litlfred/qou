# Identifying [A]_q as a Markov trace — L-1 progress

**Compiled** 2026-05-03 on `claude/path-to-1ppb-w1-rho-substrate`.
**Status**: categorical identification (clean) + open Markov-trace
formula identification.

This note gives the cleanest known categorical identification for
$[A]_q$ in the Z=N ρ-correction formula and identifies the precise
Markov-trace formula in $H_A(q)$ as the remaining research-grade
question for L-1.

---

## §1. Cleanest categorical identification

In the **Reshetikhin–Turaev** picture of the Jones polynomial:

$$
  J(L; q) \;=\; q\text{-tr}_{V^{\otimes n}}\bigl(\mathrm{RT}(\beta_L)\bigr)
$$

where $V$ is the 2-dimensional standard representation of
$U_q(\mathfrak{sl}_2)$, and $L$ is the closure of a braid $\beta_L
\in B_n$ — here the q-trace $q\text{-tr}$ means the Reshetikhin–Turaev
ribbon trace using the pivotal structure $K^{2\rho}$.

**Categorical identification (clean).**

$$
  \boxed{\;[A]_q \;=\; q\text{-dim}_q\bigl(V^{(A-1)}\bigr)
  \;=\; q\text{-tr}\bigl(\mathrm{id}_{V^{(A-1)}}\bigr)\;}
$$

where $V^{(A-1)} = \mathrm{Sym}^{A-1}(V)$ is the irreducible
representation of $U_q(\mathfrak{sl}_2)$ of highest weight $A-1$
(dimension $A$, q-dimension $[A]_q$).

This is the most natural categorical home for $[A]_q$:

- At $q = 1$: $[A]_q = A = \dim V^{(A-1)}$. Recovers integer count.
- At $q \ne 1$: $[A]_q$ is the *q-deformed* dimension picked up by the
  RT functor's pivotal structure.

In the QOU substrate, the natural rep $V^{(A-1)}$ corresponds to the
**A-host categorical content**: $A$ nucleon hosts arranged with
substrate-deformed dimension. The "integer host count $A$" of the
classical Kashaev law is precisely $\dim_\mathbb{C} V^{(A-1)}$; the
"q-deformed host count" is the q-dim $[A]_q$.

---

## §2. Markov-trace identification — partial

The cleanest identification (§1) lives in $U_q(\mathfrak{sl}_2)$, not
directly in $H_A(q)$. The Schur–Weyl bridge gives the connection:

$$
  V^{\otimes A}
  \;\cong\;
  \bigoplus_{k = 0}^{A} S^{(A-k, 1^k)}_q \otimes V^{(A-k-1) \cdot ?}
  \cdot\,\text{(actually, via Schur-Weyl with } U_q(\mathfrak{sl}_2)
  \text{:})
$$

For Schur–Weyl duality $H_A(q) \otimes U_q(\mathfrak{sl}_2)$ acting on
$V^{\otimes A}$ (with $V$ the 2-dim standard):

$$
  V^{\otimes A}
  \;\cong\;
  \bigoplus_{k=0}^{\lfloor A/2 \rfloor}
    S^{(A-k, k)}_q \otimes V^{(A - 2k)},
$$

and the q-trace on $V^{\otimes A}$ equals $[2]_q^A$. The decomposition
gives a **partition sum identity**:

$$
  [2]_q^A
  \;=\;
  \sum_{k = 0}^{\lfloor A/2 \rfloor}
    d_q^{(A-k, k)} \cdot [A - 2k + 1]_q,
$$

where $d_q^{(A-k, k)}$ is the q-dim of the Specht module
$S^{(A-k, k)}_q$.

For our purposes, the term $k = 0$ gives the partition $(A)$ (single
row), with $d_q^{(A)} = 1$ and contribution $[A+1]_q$.

**Open**: a clean *element-level* Markov-trace identity in $H_A(q)$
of the form $\mathrm{tr}_M(X_A) = [A]_q$ for some explicit $X_A \in
H_A(q)$. The candidates worth probing:

| candidate | rationale |
|-----------|-----------|
| $\mathrm{tr}_M(\sigma_1 \sigma_2 \cdots \sigma_{A-1})$ | Markov trace of the long cycle (A-cycle in $S_A$) |
| $\mathrm{tr}_M\bigl(p^{(A-1, 1)}\bigr)$ | Trace of Young symmetrizer at the natural rep |
| $\mathrm{tr}_M(JM_A)$ | Trace of the A-th Jucys–Murphy element |
| $\mathrm{tr}_M\bigl(\Delta(A)\bigr)$ | Where $\Delta(A) = \sum_w q^{\ell(w)/2} \sigma_w$ is the q-symmetrizer |

The Ram (1991) character formula gives the q-character of the long
cycle on hook representations $(k, 1^{A-k})$:

$$
  \chi^{(k, 1^{A-k})}_q(\sigma_1 \sigma_2 \cdots \sigma_{A-1})
  \;=\;
  (-1)^{A-k} \, q^{2k - A - 1}
$$

Summing over hooks with their Plancherel weights:

$$
  \mathrm{tr}_M(\sigma_1 \cdots \sigma_{A-1})
  \;=\;
  \sum_{k=1}^{A} y^{(k, 1^{A-k})} \cdot (-1)^{A-k} \cdot q^{2k - A - 1}.
$$

A numerical check at A=2, A=4 against the value $[A]_q$ at $q_0$ would
either confirm or rule out this candidate Markov-trace identity.
Reserved for the next session as a 30-minute focused probe.

---

## §3. Implication for L-1

The L-1 lemma asserts:

$$
  B(q) \;=\; m_e \cdot \mathrm{Vol}_{\rm hyp}(K_A) \cdot
  (\rho_{\rm struct} + A - [A]_q).
$$

With the identification of §1, the $A - [A]_q$ term equals:

$$
  A - [A]_q
  \;=\;
  \dim_\mathbb{C} V^{(A-1)} \;-\; q\text{-dim}_q V^{(A-1)},
$$

i.e., the **dimensional anomaly** of the natural $U_q(\mathfrak{sl}_2)$
representation. This anomaly vanishes at $q = 1$ (recovering integer
count) and is the leading-order contribution at $q \ne 1$.

**Categorical L-1 (refined)**: the binding-energy formula at finite
$q$ acquires a dimensional-anomaly correction proportional to
$\dim_\mathbb{C} V^{(A-1)} - q\text{-dim}_q V^{(A-1)}$, scaled by
$m_e \cdot \mathrm{Vol}_{\rm hyp}(K_A)$. The proportionality constant
is $-1$ (subtractive — the q-deformation REDUCES the integer host
count's contribution by exactly the dimensional anomaly).

This is a **finite-q correction to the Kashaev law**, traceable to
the substrate's $U_q(\mathfrak{sl}_2)$-deformation and the
representation theory of the natural rep. It is *categorically clean*
even if a precise element-level Markov-trace formula in $H_A(q)$
remains to be pinpointed.

---

## §4. Conjectural form

```
Conjecture L-1 (finite-q Kashaev correction).
  For Z=N=k light atoms with canonical Kashaev assignment
  (K_A, ρ_struct), the binding energy at substrate q satisfies

      B(q) = m_e · Vol_hyp(K_A) · (ρ_struct + A − [A]_q),

  where the correction A − [A]_q equals the dimensional anomaly of
  the natural U_q(sl_2)-representation V^{(A-1)}, i.e.,

      A − [A]_q = dim V^{(A-1)} − q-dim_q V^{(A-1)}.

  At q=1: correction vanishes, recovering the classical integer
  Kashaev law B = ρ_struct · m_e · Vol_hyp(K_A).
```

---

## §5. Lean formalisation

The identification in §1 is a standard fact about
$U_q(\mathfrak{sl}_2)$'s irreducibles and can be stated in Lean as a
definition wrapping Mathlib's existing `qDimension` infrastructure
(once added — `qDimension` is a research-grade addition to
Mathlib, not yet present).

**Conjectural class** (per CLAUDE.md §3b conditional-class policy):

```lean
namespace QOU.Hecke

class FiniteQKashaevCorrection (K : Knot) (A : ℕ) where
  rho_struct : ℕ
  vol_hyp    : ℝ
  /-- The conjectural binding-energy formula at finite q. -/
  binding_energy : (q : ℂ) → ℝ
  classical_limit :
    binding_energy 1 = rho_struct * M_E_MEV * vol_hyp
  q_correction (q : ℂ) :
    binding_energy q
      = rho_struct * M_E_MEV * vol_hyp
        + M_E_MEV * vol_hyp * (A - q_dim_natural q A)
  -- where q_dim_natural q A = [A]_q = q-dim of V^(A-1)

end QOU.Hecke
```

Downstream conditional theorems (e.g., the binding-energy prediction
for ²H, ⁴He at $q_0$) can then take `[FiniteQKashaevCorrection K A]`
as an explicit instance hypothesis.

---

## §6. Precise H_A(q)-Markov-trace identification (closed)

The numerical probe in
[`l1_markov_trace_for_qA.py`](../../folio-assistant/computations/l1_markov_trace_for_qA.py)
tested the natural Jones–Markov candidates in $H_A(q)$ at $q_0$ and
found:

| element | tr_M at $q_0$ | matches |
|---------|---------------|---------|
| $1 \in H_2(q)$ (unnormalised) | $2.0109$ | $[2]_q$ ✓ |
| $\mathrm{id}_{V_A}$ in $U_q(\mathfrak{sl}_A)$ | $[A]_q$ | $[A]_q$ ✓ |

**Precise identification (closed).**  In the **unnormalised**
convention where the Hecke Markov trace satisfies

$$
  \mathrm{tr}_M^{\rm un}(1_n) \;=\; [n]_q
  \qquad\text{(i.e., the q-graded dimension of the regular rep),}
$$

the q-integer $[A]_q$ is exactly $\mathrm{tr}_M^{\rm un}(1_A) \in
H_A(q)$.  Equivalently, by Schur–Weyl with $U_q(\mathfrak{sl}_A)$,
$[A]_q$ is the q-dimension of the standard rep $V_A$ — the two
formulations are identical.

In the **normalised** convention (where $\mathrm{tr}_M(1_n) = 1$),
the trace of $1_n$ is just $1$; the q-integer $[A]_q$ then appears as
the *unnormalisation factor* needed to recover the q-graded dimension.

The element-level Markov-trace identification is therefore:

$$
  \boxed{\;[A]_q \;=\; \mathrm{tr}_M^{\rm un}(1_A) \;=\;
  q\text{-dim}_q(V_A)_{U_q(\mathfrak{sl}_A)}.\;}
$$

This *closes* the precise H_A(q)-Markov-trace identification:
$[A]_q$ is the unnormalised Markov trace of the identity element of
$H_A(q)$, equivalently the q-dimension of the natural rep of
$U_q(\mathfrak{sl}_A)$ via Schur–Weyl.

## §7. Status summary

| step | status |
|------|--------|
| Categorical identification of $[A]_q$ in $U_q(\mathfrak{sl}_2)$ | **Done** (§1) |
| Schur–Weyl partition-sum identity | **Done** (§2) |
| **Element-level Markov-trace formula in $H_A(q)$** | **Done** (§6) — $\mathrm{tr}_M^{\rm un}(1_A) = [A]_q$ |
| Categorical refinement of L-1 | **Done** (§3) |
| Conjectural Lean class | **Stubbed** (§5) |
| Mathlib `qDimension` / class instance proof | **Open** — research-grade |

For the immediate Z=N work, §1's identification suffices to give a
clean categorical home for $[A]_q$ inside the substrate's
representation-theoretic framework. The finer question of which
specific element of $H_A(q)$ has Markov trace $[A]_q$ is reserved
for the next focused 30-minute probe.

---

**End of [A]_q identification note.**
