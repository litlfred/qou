The light-nucleus examples (Section B.5) use only the bare
transfer matrix product.  For heavy nuclei, **shell corrections**
from the magic number structure become essential.  This section
works through the full $Q$-value algorithm for
nuclei spanning the periodic table.

Recall: $s = q^{1/2} - q^{-1/2}$,
$z = 1/(q^{1/2} + q^{-1/2})$,
$\hbar_q = 1 - q^{-1}$,
$E_{\times} = \frac{1}{2}(q - q^{-1})$.

---

## The magic number table

Shell closures occur at specific nucleon counts where the
Gröbner--Shirshov normal form word-length histogram is palindromic:

$$
  \mathcal{M} = \{0, 2, 8, 20, 28, 50, 82, 126\}
$$

For nucleon count $X$, define:

See [Table 1](#tbl:tm-heavy-atom-examples-table1-data).

When $X$ is magic ($n_{\mathrm{out}} = 0$), the outermost
shell is **closed** and the relevant shell size is
$n_{\mathrm{shell}}(X)$.

---

## The $Q$-value algorithm (summary)

**Input:** $(Z, N)$, substrate parameter $q$.

1. Compute outer shell occupancies for parent $(Z, N)$ and
   daughter $(Z+1, N-1)$.
2. Compute torus knot Markov traces $\tau(n)$ for each
   occupancy (from Chebyshev recurrence).
3. Compute bare Skein polynomial ratio
   $R_{\mathrm{bare}} = \log_q(P_{\mathrm{dau}} / P_{\mathrm{par}})$.
4. Compute shell correction
   $\Delta_{\mathrm{shell}} = (\text{proton shell change}) +
   (\text{neutron shell change})$.
5. Add weak vertex $\Delta_{T_{3,5}} = -3.370$.
6. Convert: $Q = |R_{\mathrm{bare}} +
   \Delta_{\mathrm{shell}} + \Delta_{T_{3,5}}| \times
   \hbar_q \cdot E_{\times} \cdot \mu_0$.

---

## Example 6: Carbon-14 ($A = 14$, $Z = 6$, $N = 8$)

${}^{14}\mathrm{C} \to {}^{14}\mathrm{N}$ ($\beta^-$:
$\mathfrak{d} \to \mathfrak{u}$ at one neutron).

This is the **anomalously slow** decay ($t_{1/2} = 5730$ yr,
$\log ft = 9.04$) — six orders of magnitude slower than
tritium.  The shell structure explains why.

### Step 0: Magic number lookup

See [Table 2](#tbl:tm-heavy-atom-examples-table2-data).

The parent has a **closed neutron shell** at $n = 8$.  The
daughter breaks it: $N = 8 \to N' = 7$.

### Step 1: Transfer matrix structure

**Parent** ${}^{14}\mathrm{C}(6, 8)$: 13 generators,
$\binom{14}{2} = 91$ transfer matrix multiplications.

Nucleon ordering: $[\underbrace{\mathfrak{p} \cdots \mathfrak{p}}_{6}
\underbrace{\mathfrak{n} \cdots \mathfrak{n}}_{8}]$.

At each generator $\sigma_i$, the crossings decompose into
pp, nn, and mix types.  The converting neutron (position 6)
affects generators $\sigma_0$ through $\sigma_6$.

**Generator volume profile** (${}^{14}\mathrm{C}$ vs
${}^{14}\mathrm{N}$):

See [Table 3](#tbl:tm-heavy-atom-examples-table3-data).

Generator $\sigma_6$ — the converting nucleon's own
generator — carries nearly **half** the total energy change
($-1.660$ of $-3.361$).  Its chiral degree $k_6 = 7$ means
all 7 crossings with downstream nucleons change type.

### Step 2: Shell correction

The parent's 8-neutron shell is closed.  The Skein polynomial
**factors**:

$$
  J_{8\mathfrak{n}}(q)
  = 
  J_{\mathcal{N}(0,2)}(q)^4 \cdot (\text{linking factors})
$$

Breaking one neutron pair destroys this factorization.  The
matrix element is suppressed by:

$$
  |\mathcal{M}|^2
   \propto 
  \frac{1}{|J_{\mathcal{N}(0,2)}(q)|}
   \approx 
  \frac{1}{q + q^{-1}}
   \approx 
  \frac{1}{2.01}
$$

Combined with the spin-parity mismatch ($0^+ \to 1^+$),
this gives $|\mathcal{M}|^2 \sim 10^{-6}$ — explaining the
$\log ft = 9.04$.

### Step 3: Result

Leading-order: $t_{1/2} \approx 6690$ yr vs observed
$5730$ yr (ratio 1.17).  The 17% residual is the
**shell correction contribution**:

$$
  \frac{\Delta t_{1/2}}{t_{1/2}}
   \approx 
  -5 \cdot \frac{\delta E_{\mathrm{shell}}}{Q_0}
   \approx  -17\%
$$

The $n = 8$ closed sub-link provides extra parent stability,
increasing $\mathfrak{Q}_\beta$ via the $Q^5$ phase-space factor.

---

## Example 7: Cobalt-60 ($A = 60$, $Z = 27$, $N = 33$)

${}^{60}\mathrm{Co} \to {}^{60}\mathrm{Ni}$ ($\beta^-$).
An allowed Gamow--Teller transition where the daughter
**gains** a proton shell closure.

### Step 0: Magic number lookup

See [Table 4](#tbl:tm-heavy-atom-examples-table4-data).

The daughter has $Z' = 28$ — a **closed proton shell**.  This
transition creates a shell closure.

### Step 1: Torus knot traces

See [Table 5](#tbl:tm-heavy-atom-examples-table5-data).

### Step 2: Bare ratio

$R_{\mathrm{bare}} = -32.09$ (from the $\binom{60}{2} = 1770$
transfer matrix multiplications).

### Step 3: Shell correction

$$
  \Delta_{\mathrm{shell}}
  = 
  \underbrace{(\log_q \tau(8) - \log_q \tau(7))}_{\text{proton: } 5.29 - 2.51 = +2.78}
  + 
  \underbrace{(\log_q \tau(4) - \log_q \tau(5))}_{\text{neutron: } 2.19 - (-0.07) = +2.26}
  =  +5.04
$$

The proton shell closure ($+2.78$) is the dominant correction:
the daughter gains the stability of a closed $Z = 28$ shell.

### Step 4: Weak vertex and final answer

$$
  Q
  = 
  |{-32.09 + 5.04 + (-3.37)}|
   \times 
  \hbar_q \cdot E_{\times} \cdot \mu_0
$$

$$
  = 
  30.42 \times 0.0991 \times 0.1045 \times 1.630
   \approx 
  0.513  \text{MeV}
$$

$\mathcal{Q}_{\mathrm{exp}} \approx 0.318$ MeV.  Error:
$+61\%$.  The algorithm produces a definite answer from $q$
alone; the residual indicates the shell correction is not
yet capturing the full structure (conjectures C1--C3 need
verification).

---

## Example 8: Bismuth-210 ($A = 210$, $Z = 83$, $N = 127$)

${}^{210}\mathrm{Bi} \to {}^{210}\mathrm{Po}$ ($\beta^-$).
The heaviest nucleus in the verification table, with
$\binom{210}{2} = 21{,}945$ transfer matrix multiplications
(all computable in milliseconds).

### Step 0: Magic number lookup

See [Table 6](#tbl:tm-heavy-atom-examples-table6-data).

Both parent nucleon counts sit **one above** a magic number.
The daughter's neutron count $N' = 126$ hits a magic closure —
the highest known magic number.

### Step 1: Structure

**209 generators**, each carrying up to 209 crossings at
$\sigma_0$.  The nucleon ordering has 83 protons followed by
127 neutrons.  At generator $\sigma_i$:

- Crossings $j < 83$: pp type ($T_{pp}$)
- Crossings $83 \leq j < 210$: mix type ($T_{\mathrm{mix}}$) if
  $i < 83$, nn type ($T_{nn}$) if $i \geq 83$

The converting neutron (position 83) affects generators
$\sigma_0$ through $\sigma_{83}$.

### Step 2: Shell correction

The daughter gains a **closed neutron shell** at $N' = 126$.
This is the largest magic number and contributes the
strongest shell correction.  Simultaneously, the proton
count moves from $n_{\mathrm{out}} = 1$ to
$n_{\mathrm{out}} = 2$, a modest open-shell change.

### Step 3: Computation count

See [Table 7](#tbl:tm-heavy-atom-examples-table7-data).

The computation is **exact** — no approximations, no
truncations.  Every jet order through the $209$-jet is
included in the transfer matrix product.

---

## Summary: shell structure across the periodic table

See [Table 8](#tbl:tm-heavy-atom-examples-table8-data).

**Pattern:** Transitions that create or destroy a closed
sub-link at a magic number have the largest matrix-element
corrections.  ${}^{137}\mathrm{Cs}$ has the smallest residual
(9%) because the daughter ${}^{137}\mathrm{Ba}$ is one neutron
short of the $n = 82$ closure — the transition into a
near-magic daughter is slightly favoured.

The shell correction is not an external fix — it is the
**discrete structure of the Skein polynomial** already present
in the framework.  The full quantitative computation requires:
(1) deriving the magic numbers from $q$ (conjecture C1), and
(2) determining the shell energy scale $\lambda_{\mathrm{shell}}$
(conjecture C2).
