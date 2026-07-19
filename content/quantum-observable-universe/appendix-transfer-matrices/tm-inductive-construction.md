Given a nucleus with $A$ nucleons and transfer matrix chains $\{M_i\}_{i=0}^{A-2}$, we describe how adding one nucleon produces the $A+1$ nucleus. This inductive step is the engine behind every Skein polynomial computation. 

## The inductive step: $A \to A+1$

Given nucleus $\mathcal{N}(Z, N)$ with $A$ nucleons ordered $[\tau_0, \ldots, \tau_{A-1}]$ where $\tau_k \in \{\mathfrak{p}, \mathfrak{n}\}$. The braid has generators $\sigma_0, \ldots, \sigma_{A-2}$ with transfer matrix products $M_i$ and traced volumes $\hat{V}_i$.
Add nucleon $\tau_A$ at position $A$.
Result: Nucleus $\mathcal{N}'$ with $A+1$ nucleons, generators $\sigma_0, \ldots, \sigma_{A-1}$, and updated products $M_i'$.

**Rule 1: Existing generators gain one crossing.** Every existing generator $\sigma_i$ acquires one crossing between nucleon $i$ and nucleon $A$. The transfer matrix product appends one new factor on the left:

$$
  M_i'(q) = T_{\tau_i, \tau_A}(q) \cdot M_i(q)
$$

where $T_{\tau_i, \tau_A}$ is $T_{pp}$, $T_{nn}$, or $T_{\mathrm{mix}}$.

**Rule 2: One new generator is created.** A new generator $\sigma_{A-1}$ appears with a single crossing:

$$
  M_{A-1}'(q) = T_{\tau_{A-1}, \tau_A}(q)
$$

**Rule 3: Skein polynomial update.** The new polynomial factors as:

$$
  P_{\mathcal{N}'}(q) = \left( \prod_{i=0}^{A-2} \hat{V}_i'(q) \right) \cdot \hat{V}_{A-1}'(q)
$$

where $\hat{V}_i'(q) = z \cdot (M_i')_{11} + (M_i')_{21}$.

**Rule 4: Crossing count grows by $A$.** Adding the $(A+1)$-th nucleon creates $A$ new crossings. The total crossing count goes from $\binom{A}{2}$ to $\binom{A+1}{2}$.

## The recurrence at each generator

At generator $\sigma_i$, the coefficients $(a_i, b_i)$ in $M_i = \bigl(\begin{smallmatrix} a_i \\ b_i \end{smallmatrix}\bigr)$ satisfy the transfer matrix recurrence. Starting from $(a, b) = (0, 1)$, each new crossing with nucleon $j$ updates:

$$
  \begin{pmatrix} a' \\ b' \end{pmatrix} = T(c_j, d_j) \cdot \begin{pmatrix} a \\ b \end{pmatrix}
$$

Explicitly: $a' = ac_j(q - q^{-1}) + ad_j + bc_j$ and $b' = ac_j + bd_j$.

## Jet expansion interpretation

The crossing product stratifies into jet orders. Jet order $r$ is the $(r+1)$-body correlation, present with multiplicity $\binom{k_i}{r}$. Adding nucleon $A$ increases the chiral degree at every existing generator by 1. Single beta decay is a 1-jet variation. The $Q$-value sums only over generators $\sigma_i$ with $i \leq p$, where $p$ is the converting nucleon's position. Unaffected generators cancel exactly.

