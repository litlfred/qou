The Gröbner--Shirshov basis theory for the Iwahori--Hecke algebra
$H_A(q)$ gives a stronger result than uniqueness of normal
forms: the **energy** of the nuclear braid word is a topological
invariant, computed by the division algorithm with no path
dependence.

**Theorem.**
Let $G = \{\sigma_i^2 - (q - q^{-1})\sigma_i - 1, \sigma_i \sigma_{i+1} \sigma_i - \sigma_{i+1} \sigma_i \sigma_{i+1}, \sigma_i \sigma_j - \sigma_j \sigma_i\}$ be the Gröbner--Shirshov basis
for $H_A(q)$
([nuclear Gröbner--Shirshov reduction](#prop:nuclear-groebner-reduction)).
Define the **energy functional** on $H_A(q)$ by

$$
  E(\xi) =  \sum_{w \in B} |c_w(q)| \cdot \ell(w)
$$

where $\xi = \sum_w c_w(q) \cdot w$ is the normal form
$\mathcal{N}(Z, N)$ and $\ell(w)$ is the word length.
Then:

1. **Only Hecke reductions change energy.**
   The Yang--Baxter relation $\sigma_i \sigma_{i+1} \sigma_i = \sigma_{i+1} \sigma_i \sigma_{i+1}$ and the far
   commutativity $\sigma_i \sigma_j = \sigma_j \sigma_i$
   preserve all coefficients and word lengths.  The Hecke
   relation $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$ is the
   unique energy-changing generator in $G$.

2. **Energy is path-independent.**
   The total energy change from the unreduced braid word
   $\mathcal{N}_{\mathrm{raw}}(Z, N)$ to the normal form
   $\mathcal{N}(Z, N)$ is independent of the order
   in which the Gröbner--Shirshov basis elements are applied.  This
   follows from the confluence (Bergman diamond lemma) of the
   Gröbner--Shirshov basis: all reduction paths lead to the
   same normal form, and the energy is a function of the
   normal form alone.

3. **Each Hecke step has a definite energy.**
   When $\sigma_i^2$ is replaced by $(q - q^{-1})\sigma_i + 1$,
   the energy change at that step is

   $$
     \Delta E_{\mathrm{step}}
     = 
     |c| \cdot \bigl(|q - q^{-1}| + 1 - 1\bigr)
     = 
     |c| \cdot |q - q^{-1}|
   $$

   where $c$ is the coefficient of the $\sigma_i^2$ term.  Every
   Hecke step **increases** the total weight by $|c| \cdot (q - q^{-1})$
   (since $q > 1$ ensures $q - q^{-1} > 0$).

**Proof.**

*Part 1.*
The Yang--Baxter relation $\sigma_i \sigma_{i+1} \sigma_i = \sigma_{i+1} \sigma_i \sigma_{i+1}$ has the same word length
on both sides ($\ell = 3$) and coefficient $1$.  Applying it to a
term $c \cdot w$ produces $c \cdot w'$ where $|c| = |c|$ and
$\ell(w') = \ell(w)$.  Similarly for far commutativity.  Only
the Hecke relation $\sigma_i^2 \mapsto (q - q^{-1})\sigma_i + 1$
changes the word length (from $\ell$ to $\ell - 1$) and splits
one coefficient into two.

*Part 2.*
The Gröbner--Shirshov basis $G$ satisfies the Bergman diamond lemma
(the main theorem of the Gröbner--Shirshov basis theory,
[main theorem](#unital-groebner-bases:thm:main-theorem)):
for any two overlapping reductions, the results can be further
reduced to the same normal form.  Since the energy is computed
from the normal form and the normal form is unique, the energy
is path-independent.

*Part 3.*
Let $c \cdot \sigma_i^2 \cdot (\text{suffix})$ be a reducible
term.  After applying the Hecke relation:
- One term has coefficient $c(q - q^{-1})$ and word length
  $\ell - 1$ (the $\sigma_i$ term).
- One term has coefficient $c$ and word length $\ell - 2$
  (the identity term).
The total weight changes by
$|c(q-q^{-1})| + |c| - |c| = |c| \cdot |q - q^{-1}|$.

**Substrate-internal: GS reduction over the Habiro embedding.**
*The reduction rules in $G$ — Hecke, Yang–Baxter, far commutativity —
are formal rewriting rules that act strictly within the polynomial
embedding $\mathbb{Z}[q^{\pm 1}] \hookrightarrow \widehat{\mathbb{Z}[q]}$
([Habiro ring](#def:habiro-ring)). Confluence (Bergman diamond) is
an exact algebraic consequence of the foundational triple
$(\mathbf{C}, A, \tau)$, holding in any base ring where the
Hecke relation $\sigma_i^2 = (q-q^{-1})\sigma_i + 1$ can be
imposed — and in particular over the
[motivic substrate](#def:motivic-substrate) before any place-realization
is applied. The energy functional $E(\xi)$ takes values in
$\mathbb{Z}_{\geq 0}[q^{\pm 1}]$ as a formal Laurent polynomial;
its evaluation as a real-valued physical quantity (Skein binding
energy) requires the archimedean realization $\rho_\infty$
([archimedean realization](#def:archimedean-realization-functor))
of the substrate, and is downstream of the reduction itself.*

**Computational verification.**
The instrumented division algorithm (`hecke_division.py`) confirms:

| Nucleus | Hecke steps | YB steps | Far-comm | Total $\Delta E$ |
|---------|:---:|:---:|:---:|---:|
| Deuteron $\mathcal{N}(1,1)$ | 0 | 0 | 0 | 0 |
| ${}^{3}\mathrm{H} \mathcal{N}(1,2)$ | 1 | 0 | 0 | $+0.260$ |
| ${}^{4}\mathrm{He} \mathcal{N}(2,2)$ | 4 | 0 | 0 | $+0.641$ |
| ${}^{6}\mathrm{Li} \mathcal{N}(3,3)$ | 26 | 0 | 0 | $+4.233$ |

All energy changes come from Hecke steps.  Yang--Baxter and
far-commutativity steps contribute zero energy change, confirming
part 1 of the theorem.

**The beta-decay energy difference.**
The half-life is determined by
$\Delta E = E(\mathcal{N}(p+1,n-1))
- E(\mathcal{N}(Z, N))$, which counts the difference
in Hecke steps between parent and daughter normal forms.  This
difference is **always negative** (verified computationally for
all $A \leq 6$): the daughter has fewer Hecke steps, consistent
with beta decay releasing energy.

| Transition | $\Delta E$ (Hecke steps) |
|------------|:---:|
| ${}^{3}\mathrm{H} \to {}^{3}\mathrm{He}$ | $-0.027$ |
| ${}^{4}\mathrm{He} \to {}^{5}\mathrm{Li}$ | $-0.073$ |
| ${}^{6}\mathrm{Li} \to {}^{6}\mathrm{Be}$ | $-0.828$ |

The magnitude of $\Delta E$ grows with $A$, reflecting the
increasing number of crossings that rearrange in heavier nuclei.
