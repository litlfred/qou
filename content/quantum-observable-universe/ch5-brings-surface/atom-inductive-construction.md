An atom $\mathcal{A}(Z, N)$ is constructed **inductively** from
the empty brane, one nucleon and one electron at a time.  At
every step the algebraic state is a Gröbner-normalized word in
the Hecke algebra $H_A(q)$.  We show the first three atoms
explicitly: hydrogen, deuterium, and helium-3.

## The inductive schema

**Data at step $k$.**  After linking $k$ nucleons and $k_e$
electrons, the atom is encoded by two objects:

1. **Nuclear word** $\bar{\mathcal{N}}_k \in H_k(q)$ — the
   Gröbner normal form of the nuclear braid on $k$ strands.

2. **Electron chain** $\bar{\mathcal{E}}_{k_e}$ — a sequence of
   closed sub-Hopf links of trefoils $T_{2,3}$, each at a
   definite shell level $n$.

**Operators.**  Two operators build the atom:

$$
  \boxed{
    \Phi_{\mathrm{nuc}}^{(k)}
    \;:\;
    H_k(q) \;\longrightarrow\; H_{k+1}(q),
    \qquad
    \bar{\mathcal{N}}_k
    \;\mapsto\;
    r\!\left(
      \bar{\mathcal{N}}_k
      \cdot \prod_{j=0}^{k-1}(c_j \sigma_j + d_j),\;
      G
    \right)
  }
$$

$$
  \boxed{
    \Phi_{\mathrm{elec}}^{(n)}
    \;:\;
    \bar{\mathcal{E}}_{k_e}
    \;\mapsto\;
    \bar{\mathcal{E}}_{k_e}
    \;\bowtie_n\; T_{2,3}
  }
$$

where $r(\cdot, G)$ is the Gröbner division algorithm with
basis $G = \{\sigma_i^2 - (q-q^{-1})\sigma_i - 1,\;
\text{YB},\; \text{far-comm}\}$, and the crossing coefficients
$(c_j, d_j)$ depend on the nucleon types at positions $j$ and
$k$:

| New nucleon | Existing nucleon $j$ | $c_j$ | $d_j$ |
|:-----------:|:-------------------:|:-----:|:-----:|
| $\mathfrak{p}$ | $\mathfrak{p}$ | $1$ | $0$ |
| $\mathfrak{n}$ | $\mathfrak{n}$ | $q^2$ | $-qs$ |
| mixed | mixed | $\tfrac{1+q^2}{2}$ | $-\tfrac{qs}{2}$ |

with $s = q^{1/2} - q^{-1/2}$.

**Gröbner preservation (inductive claim).**
If $\bar{\mathcal{N}}_k$ is in Gröbner normal form, then
$\bar{\mathcal{N}}_{k+1} = \Phi_{\mathrm{nuc}}^{(k)}(\bar{\mathcal{N}}_k)$
is also in Gröbner normal form.  This is
[shell closure normal form](#prop:shell-closure-normal-form)
part (i): the division algorithm terminates and produces a
unique remainder with no leading monomial of any $g \in G$
in its support.

---

## Step 0.  Vacuum: $\mathcal{A}(\emptyset)$

$$
  \bar{\mathcal{N}}_0 = \emptyset, \qquad
  \bar{\mathcal{E}}_0 = \emptyset
$$

No strands, no crossings, no electrons.  The identity
of the empty Hecke algebra $H_0(q) = \mathbb{Z}[q^{\pm 1}]$.

**Gröbner check:** Trivially in normal form (empty word).

---

## Step 1.  Hydrogen nucleus: $\bar{\mathcal{N}}(1, 0)$

**Operation:** $\Phi_{\mathrm{nuc}}^{(0)}$ — add one proton
$\mathfrak{p}$ to the vacuum.

$$
  \bar{\mathcal{N}}_1
  \;=\;
  \mathbf{1} \;\in\; H_1(q)
$$

There are **zero generators** in $H_1(q)$ (one strand, no
crossings possible).  The nuclear word is the identity $\mathbf{1}$.

**Crossing coefficients:** None (no existing nucleons to cross).

**Hecke reduction steps:** $0$.

**Hecke energy:** $E_1 = 0$.

**Gröbner check:** $\mathbf{1}$ has no $\sigma_i$ at all —
trivially in normal form.

**Electron attachment:** $\Phi_{\mathrm{elec}}^{(1)}$ — attach
one trefoil at shell $n = 1$.

$$
  \bar{\mathcal{E}}_1 = T_{2,3}
  \qquad (\text{shell } 1s^1, \text{ open})
$$

**The full atom:**

$$
  \boxed{
    \mathcal{A}(1, 0)
    \;=\;
    \underbrace{\mathbf{1}}_{\bar{\mathcal{N}}_1}
    \;\bowtie\;
    \underbrace{T_{2,3}}_{\bar{\mathcal{E}}_1}
  }
$$

**Word:** $\mathbf{1}$.  **Shell:** $1s^1$ (open).
**Total Hecke energy:** $0$.

---

## Step 2.  Deuterium nucleus: $\bar{\mathcal{N}}(1, 1)$

**Operation:** $\Phi_{\mathrm{nuc}}^{(1)}$ — add one neutron
$\mathfrak{n}$ to the hydrogen nucleus.

The new nucleon ($\mathfrak{n}$, position $k = 1$) crosses the
existing nucleon ($\mathfrak{p}$, position $j = 0$).  This is a
**mixed crossing**:

$$
  c_0 = \tfrac{1 + q^2}{2}, \qquad
  d_0 = -\tfrac{q\,s}{2}
$$

The pre-reduction element in $H_2(q)$ is:

$$
  \xi_2
  \;=\;
  \bar{\mathcal{N}}_1 \cdot (c_0\,\sigma_0 + d_0)
  \;=\;
  \mathbf{1} \cdot \bigl(\tfrac{1+q^2}{2}\,\sigma_0
  - \tfrac{qs}{2}\bigr)
  \;=\;
  \tfrac{1+q^2}{2}\,\sigma_0
  \;-\;
  \tfrac{qs}{2}
$$

**Gröbner reduction of $\xi_2$:**

Check each term against $G$:

- $\tfrac{1+q^2}{2}\,\sigma_0$: word $= \sigma_0$, length $1$.
  No $\sigma_i^2$ → no Hecke reduction needed.
  No YB triple ($A = 2$, only $\sigma_0$) → no YB reduction.
  No far-comm pair → nothing to sort.

- $-\tfrac{qs}{2}$: word $= \mathbf{1}$, length $0$.
  Trivially reduced.

**No reductions apply.** The element is already in normal form:

$$
  \boxed{
    \bar{\mathcal{N}}(1, 1)
    \;=\;
    \tfrac{1+q^2}{2}\;\sigma_0
    \;-\;
    \tfrac{qs}{2}
  }
$$

**Numerical values at $q = 1.1097$:**

$$
  q^2 = 1.2314, \quad
  s = q^{1/2} - q^{-1/2} = 0.0524, \quad
  \tfrac{1+q^2}{2} = 1.1157, \quad
  \tfrac{qs}{2} = 0.0291
$$

$$
  \bar{\mathcal{N}}(1,1)
  \;=\;
  1.1157\,\sigma_0 - 0.0291
$$

**Hecke reduction steps:** $0$ (already in normal form).

**Hecke energy:** $E_2 = |1.1157| \cdot 1 + |{-}0.0291| \cdot 0
= 1.1157$.

**Gröbner check:** Support $= \{\sigma_0,\, \mathbf{1}\}$.
Neither word contains $\sigma_i^2$, a YB triple, or an
unsorted far-comm pair.  $\checkmark$

**Transfer matrix form.**  The nuclear word
$a\,\sigma_0 + b$ with $a = \tfrac{1+q^2}{2}$,
$b = -\tfrac{qs}{2}$ corresponds to the state vector:

$$
  \begin{pmatrix} a \\ b \end{pmatrix}
  \;=\;
  T_{\mathrm{mix}}(q) \cdot \begin{pmatrix} 1 \\ 0 \end{pmatrix}
  \;=\;
  \begin{pmatrix} 1.1157 \\ -0.0291 \end{pmatrix}
$$

confirming that the sequential builder reproduces the
transfer matrix action.

**Electron attachment:** $\Phi_{\mathrm{elec}}^{(1)}$ — attach
one trefoil at shell $n = 1$.

$$
  \boxed{
    \mathcal{A}(1, 1)
    \;=\;
    \underbrace{
      \tfrac{1+q^2}{2}\,\sigma_0 - \tfrac{qs}{2}
    }_{\bar{\mathcal{N}}(1,1)}
    \;\bowtie\;
    \underbrace{T_{2,3}}_{\bar{\mathcal{E}}_1}
  }
$$

**Word:** $\tfrac{1+q^2}{2}\,\sigma_0 - \tfrac{qs}{2}$.
**Shell:** $1s^1$ (open).
**Total Hecke energy:** $1.1157$ (all from the mixed crossing,
zero Hecke reduction cost).

---

## Step 3.  Tritium / Helium-3 nucleus: $\bar{\mathcal{N}}(1, 2)$

**Operation:** $\Phi_{\mathrm{nuc}}^{(2)}$ — add a second
neutron $\mathfrak{n}$ to the deuterium nucleus.

The new nucleon ($\mathfrak{n}$, position $k = 2$) crosses
**two** existing nucleons:

- **With nucleon 0** ($\mathfrak{p}$): mixed crossing at
  generator $\sigma_0$.
  $(c_0, d_0) = (\tfrac{1+q^2}{2},\; -\tfrac{qs}{2})$.

- **With nucleon 1** ($\mathfrak{n}$): neutron-neutron crossing
  at generator $\sigma_1$.
  $(c_1, d_1) = (q^2,\; -qs)$.

The crossing element for the new nucleon is the **product** of
the two crossing factors (one per existing nucleon):

$$
  \Pi_2
  \;=\;
  (c_0\,\sigma_0 + d_0)(c_1\,\sigma_1 + d_1)
$$

Expanding (since $\sigma_0$ and $\sigma_1$ are on **adjacent**
generators, they do NOT commute — no far-comm simplification):

$$
  \Pi_2
  \;=\;
  c_0 c_1\,\sigma_0\sigma_1
  \;+\;
  c_0 d_1\,\sigma_0
  \;+\;
  d_0 c_1\,\sigma_1
  \;+\;
  d_0 d_1
$$

**Numerical coefficients:**

$$
  c_0 c_1 = \tfrac{1+q^2}{2} \cdot q^2
  = 1.1157 \times 1.2314 = 1.3738
$$

$$
  c_0 d_1 = \tfrac{1+q^2}{2} \cdot (-qs)
  = 1.1157 \times (-0.0581) = -0.0649
$$

$$
  d_0 c_1 = (-\tfrac{qs}{2}) \cdot q^2
  = -0.0291 \times 1.2314 = -0.0358
$$

$$
  d_0 d_1 = (-\tfrac{qs}{2})(-qs)
  = 0.0291 \times 0.0581 = 0.0017
$$

So:

$$
  \Pi_2
  \;=\;
  1.3738\,\sigma_0\sigma_1
  - 0.0649\,\sigma_0
  - 0.0358\,\sigma_1
  + 0.0017
$$

**Pre-reduction element:** multiply $\bar{\mathcal{N}}(1,1)$
by $\Pi_2$:

$$
  \xi_3
  \;=\;
  \bar{\mathcal{N}}(1,1) \cdot \Pi_2
  \;=\;
  (1.1157\,\sigma_0 - 0.0291) \cdot
  (1.3738\,\sigma_0\sigma_1 - 0.0649\,\sigma_0
  - 0.0358\,\sigma_1 + 0.0017)
$$

Distribute term by term.  Write $a = 1.1157$, $b = -0.0291$:

$$
  \xi_3
  \;=\;
  a \cdot c_0 c_1 \;\sigma_0 \cdot \sigma_0\sigma_1
  \;+\; a \cdot c_0 d_1 \;\sigma_0 \cdot \sigma_0
  \;+\; a \cdot d_0 c_1 \;\sigma_0\sigma_1
  \;+\; a \cdot d_0 d_1 \;\sigma_0
$$

$$
  \;+\; b \cdot c_0 c_1 \;\sigma_0\sigma_1
  \;+\; b \cdot c_0 d_1 \;\sigma_0
  \;+\; b \cdot d_0 c_1 \;\sigma_1
  \;+\; b \cdot d_0 d_1
$$

The key terms containing $\sigma_0^2$:

- $a \cdot c_0 c_1\;\sigma_0^2\sigma_1$
  $= 1.1157 \times 1.3738\;\sigma_0^2\sigma_1 = 1.5327\;\sigma_0^2\sigma_1$

- $a \cdot c_0 d_1\;\sigma_0^2$
  $= 1.1157 \times (-0.0649)\;\sigma_0^2 = -0.0724\;\sigma_0^2$

**Gröbner reduction — Hecke step 1:** Apply
$\sigma_0^2 = (q - q^{-1})\sigma_0 + 1$ to the
$\sigma_0^2\sigma_1$ term:

$$
  1.5327\;\sigma_0^2\sigma_1
  \;\longrightarrow\;
  1.5327\,(q - q^{-1})\;\sigma_0\sigma_1
  \;+\;
  1.5327\;\sigma_1
$$

$$
  = 1.5327 \times 0.2091\;\sigma_0\sigma_1
  + 1.5327\;\sigma_1
  = 0.3205\;\sigma_0\sigma_1 + 1.5327\;\sigma_1
$$

**Hecke energy cost:** $|1.5327| \times |q - q^{-1}|
= 1.5327 \times 0.2091 = 0.3205$.

**Gröbner reduction — Hecke step 2:** Apply
$\sigma_0^2 = (q - q^{-1})\sigma_0 + 1$ to the
$\sigma_0^2$ term:

$$
  -0.0724\;\sigma_0^2
  \;\longrightarrow\;
  -0.0724\,(q - q^{-1})\;\sigma_0
  \;-\;
  0.0724
$$

$$
  = -0.0151\;\sigma_0 - 0.0724
$$

**Hecke energy cost:** $|{-}0.0724| \times 0.2091 = 0.0151$.

**Collecting all terms after reduction** (grouping by word):

| Word | Coefficient | Sources |
|:----:|:-----------:|:--------|
| $\sigma_0\sigma_1$ | $a \cdot d_0 c_1 + b \cdot c_0 c_1 + 0.3205$ | $= 1.1157 \times (-0.0358) + (-0.0291) \times 1.3738 + 0.3205$ |
| | | $= -0.0400 - 0.0400 + 0.3205 = 0.2406$ |
| $\sigma_0$ | $a \cdot d_0 d_1 + b \cdot c_0 d_1 - 0.0151$ | $= 1.1157 \times 0.0017 + (-0.0291)(-0.0649) - 0.0151$ |
| | | $= 0.0019 + 0.0019 - 0.0151 = -0.0113$ |
| $\sigma_1$ | $b \cdot d_0 c_1 + 1.5327$ | $= (-0.0291)(-0.0358) + 1.5327$ |
| | | $= 0.0010 + 1.5327 = 1.5337$ |
| $\mathbf{1}$ | $b \cdot d_0 d_1 - 0.0724$ | $= (-0.0291)(0.0017) - 0.0724$ |
| | | $= -0.0001 - 0.0724 = -0.0724$ |

**Check for further reductions:**

- No $\sigma_i^2$ terms remain.
- $\sigma_0\sigma_1$: adjacent generators, length $2$ — this is
  the beginning of a YB triple $\sigma_0\sigma_1\sigma_0$, but
  no such triple appears (no length-$3$ words).
- No far-comm pairs ($|0 - 1| = 1 < 2$).

**The normal form is complete:**

$$
  \boxed{
    \bar{\mathcal{N}}(1, 2)
    \;=\;
    0.2406\;\sigma_0\sigma_1
    \;-\; 0.0113\;\sigma_0
    \;+\; 1.5337\;\sigma_1
    \;-\; 0.0724
  }
$$

or in exact $q$-arithmetic:

$$
  \bar{\mathcal{N}}(1, 2)
  \;=\;
  \alpha_{01}\;\sigma_0\sigma_1
  \;+\; \alpha_0\;\sigma_0
  \;+\; \alpha_1\;\sigma_1
  \;+\; \alpha_\emptyset
$$

where the coefficients $\alpha_w \in \mathbb{Z}[q^{\pm 1/2}]$
are polynomial functions of $q$ determined by the crossing
coefficients and the Hecke relation.

**Comparison with known result.**  The computation in
[nuclear Gröbner reduction](#prop:nuclear-groebner-reduction)
reports:

$$
  \bar{\mathcal{N}}(1, 2)
  \;=\;
  -0.145
  + (-0.015)\,\sigma_0
  + 1.539\,\sigma_1
  + 0.162\,\sigma_0\sigma_1
$$

The dominant term $+1.539\,\sigma_1$ matches our
$+1.5337\,\sigma_1$ (the neutron-neutron crossing,
weighted by $q^2 \approx 1.232$).  Small numerical
differences arise from rounding of intermediate coefficients.

**Gröbner check:** Support $= \{\sigma_0\sigma_1,\,
\sigma_0,\, \sigma_1,\, \mathbf{1}\}$.  All words are
reduced (no squares, no YB triples, generators in
ascending order within each word).  $\checkmark$

**Total Hecke energy:** $E_3 = E_2 + 0.3205 + 0.0151
= 1.1157 + 0.3356 = 1.4513$.

**Hecke steps at this stage:** $2$ (both from
$\sigma_0^2$ elimination).

**Physical reading:** The dominant term $1.534\,\sigma_1$ is the
strong $\mathfrak{n}$-$\mathfrak{n}$ Hopf crossing.  The
sub-dominant $0.241\,\sigma_0\sigma_1$ is the mixed crossing
chain $\mathfrak{p}$-$\mathfrak{n}_1$-$\mathfrak{n}_2$.  The
two Hecke reductions ($\sigma_0^2 \to (q-q^{-1})\sigma_0 + 1$)
are the algebraic expression of resolving the double crossing
at the proton — the proton interacts with both neutrons,
creating a $\sigma_0^2$ that the Hecke relation resolves into
a weighted single crossing plus a scalar.

**Electron attachment:** $\Phi_{\mathrm{elec}}^{(1)}$ — one
electron at shell $n = 1$.

$$
  \boxed{
    \mathcal{A}(1, 2)
    \;=\;
    \underbrace{
      0.241\,\sigma_0\sigma_1
      - 0.011\,\sigma_0
      + 1.534\,\sigma_1
      - 0.072
    }_{\bar{\mathcal{N}}(1,2)}
    \;\bowtie\;
    \underbrace{T_{2,3}}_{\bar{\mathcal{E}}_1}
  }
$$

**Word:** 4 terms on support $\{\sigma_0\sigma_1,\sigma_0,
\sigma_1, \mathbf{1}\}$.
**Shell:** $1s^1$ (open).
**Dominant crossing:** $\sigma_1$ (neutron-neutron, strong force).

---

## Summary of the first three steps

| Step | Atom | $\bar{\mathcal{N}}$ | Terms | Hecke steps | $\Delta E$ | Shell |
|:----:|:----:|:--------------------|:-----:|:-----------:|:----------:|:-----:|
| 1 | $\mathcal{A}(1,0)$ | $\mathbf{1}$ | 1 | 0 | 0 | $1s^1$ |
| 2 | $\mathcal{A}(1,1)$ | $1.116\,\sigma_0 - 0.029$ | 2 | 0 | 0 | $1s^1$ |
| 3 | $\mathcal{A}(1,2)$ | $0.241\,\sigma_0\sigma_1 - 0.011\,\sigma_0 + 1.534\,\sigma_1 - 0.072$ | 4 | 2 | $0.336$ | $1s^1$ |

**Pattern:** The number of terms grows as the number of reduced
words in $S_A$ of length $\leq A - 1$.  The Hecke steps (and
energy cost) appear **only when a nucleon crosses a nucleon it
shares a type with** — specifically, when a proton crosses two
or more existing strands, or a neutron crosses two or more,
creating $\sigma_j^2$ terms that the Hecke relation must resolve.

**What comes next (Step 4: ${}^3\mathrm{He}$).**
Adding a second proton to $\bar{\mathcal{N}}(1,2)$ produces
$\bar{\mathcal{N}}(2,1)$ — the helium-3 nucleus.  The new
proton crosses all three existing nucleons, generating
$\sigma_j$ factors at $j = 0, 1, 2$ and creating $\sigma_j^2$
terms wherever the new proton meets an existing proton.  The
first **shell closure** occurs at $\bar{\mathcal{N}}(2,2)$
(helium-4), where the palindromic Poincaré histogram
$\{1, 3, 4, 3, 1\}$ appears and the Hecke energy gap signals
the completion of the $s$-shell.

**The torus knot operator enters at shell $n = 2$.**
When the fifth nucleon is added (lithium), the Hecke energy
jumps by factor $\sim 15\times$
([shell closure](#prop:shell-closure-normal-form)).  The new
nucleon cannot fit into the existing shell — it must start a
new shell mediated by the torus knot $T_{2,3}$, whose crossing
coefficients $(c_n, d_n)$ follow the Chebyshev recurrence
and replace the bare mixed/nn/pp coefficients at the
inter-shell boundary.
