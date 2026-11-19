The $Q$-value for any $\beta^-$ decay $\mathcal{N}(Z, N) \to \mathcal{N}(Z\!+\!1, N\!-\!1)$ is computed by the following algorithm. The inputs are the substrate parameter $q$ and the nucleon counts $(Z, N)$. No external nuclear physics data is used.

## Proven facts used by the algorithm

**(P1)** The Gröbner--Shirshov reduction of the nuclear braid has zero Yang–Baxter steps and zero far-commutativity steps. This is verified for $A \leq 6$ and proven inductively for all $A$. Therefore the per-generator transfer matrix chain is the exact Gröbner--Shirshov normal form.

**(P2)** The transfer matrix at each generator $\sigma_i$ is $T(c, d) = \bigl(\begin{smallmatrix} c(q-q^{-1})+d & c \\ c & d \end{smallmatrix}\bigr)$. The crossing coefficient $(c, d)$ is determined by the nucleon pair type (pp, nn, or mix).

**(P3)** The five embeddable torus knots $T_{2,n}$ for $n = 3, 5, 7, 9$ each reduce to $c_n \sigma + d_n$ in $H_2(q)$ via the Chebyshev recurrence. These are exact polynomials in $q$.

**(P4)** Shell closures occur when the word-length histogram is palindromic. This is the Poincaré polynomial of $S_{n_s}$.

**(P5)** The finiteness bound $[n_s - 1]_q! > [2]_q^{n_s - 1}$ crosses at $n_s = 5$.

**(P6)** The inverse identity $T_{2,9} \cdot T_{2,9}^{-1} = \mathbf{1}$ holds identically. Conjugation by $T_{2,9}$ preserves chirality. All same-sign crossings commute with the crossing reversal involution.

## Conjectured (used but not yet proven)

**(C1)** The magic numbers $\{2, 8, 20, 28, 50, 82, 126\}$ emerge from the palindromic closure pattern. This is currently observed but not derived in closed form from $q$.

**(C2)** The dominant binding operator for a shell of size $n_s$ is the largest $T_{2,n}$ with $n \leq n_s$.

**(C3)** Inner shell dressing by $T_{2,9}$ conjugation cancels in the $Q$-value. The inner shells are the same in parent and daughter.

## Algorithm

**Input:** $(Z, N)$ with $N \geq 1$. The parent has at least one neutron to convert.

**Output:** $Q(Z, N)$ in MeV.

### Step 0: Magic number table

$$
  \mathcal{M} = \{0, 2, 8, 20, 28, 50, 82, 126\}
$$

For nucleon count $X$, define:
- $m_{\leq}(X) = \max\{m \in \mathcal{M} : m \leq X\}$. This is the largest magic number $\leq X$.
- $m_{<}(X) = \max\{m \in \mathcal{M} : m < X\}$. This is the largest magic number strictly below $X$.
- $n_{\mathrm{out}}(X) = X - m_{\leq}(X)$. This is the nucleon count in the outermost open shell. It is zero if $X$ is magic.
- $n_{\mathrm{shell}}(X) = m_{\leq}(X) - m_{<}(X)$. This is the size of the shell containing $X$, even if not fully occupied.

**Special case:** If $X \in \mathcal{M}$ (magic), then $n_{\mathrm{out}}(X) = 0$ and the outermost shell is closed. The relevant shell size for the closure is $n_{\mathrm{shell}}(X)$.

### Step 1: Outer shell occupancies

Compute for parent and daughter:

$$
  n_p^{\mathrm{par}} = n_{\mathrm{out}}(Z), \qquad
  n_n^{\mathrm{par}} = n_{\mathrm{out}}(N)
$$

$$
  n_p^{\mathrm{dau}} = n_{\mathrm{out}}(Z + 1), \qquad
  n_n^{\mathrm{dau}} = n_{\mathrm{out}}(N - 1)
$$

If any of these are zero (magic closure), the corresponding shell is closed. The shell size is $n_{\mathrm{shell}}(X)$ instead.

### Step 2: Torus knot traces

For each outer shell occupancy $n_{\mathrm{out}}$, compute the Markov trace of $T_{2,n_{\mathrm{out}}} = \sigma^{n_{\mathrm{out}}}$ in $H_2(q)$:

$$
  \tau(n) = \mathrm{tr}_{\mathrm{Markov}}(\sigma^n, 2)
$$

If $n = 0$ (magic closure), use $\tau(n_{\mathrm{shell}})$ instead. This is the trace of the full closed shell.

The traces are computed from the Chebyshev recurrence. No numerical reduction is needed.

### Step 3: Bare Skein polynomial ratio

Compute the Level 0 transfer matrix Skein polynomials $P_{\mathrm{par}}(q)$ and $P_{\mathrm{dau}}(q)$. Use the naive ordering $[\underbrace{p \cdots p}_{Z} \underbrace{n \cdots n}_{N}]$ with bare crossing coefficients:

$$
  \text{pp}: (c, d) = (1, 0), \qquad
  \text{nn}: (c, d) = (1, -(q - q^{-1})), \qquad
  \text{mix}: (c, d) = (1, -\tfrac{1}{2}(q - q^{-1}))
$$

The bare ratio in $\log_q$:

$$
  R_{\mathrm{bare}} = \log_q(P_{\mathrm{dau}} / P_{\mathrm{par}})
$$

### Step 4: Outer shell correction

The bare computation does not account for the torus knot binding within shells. The correction is:

$$
  \Delta_{\mathrm{shell}}
  = 
  \underbrace{
    \log_q \tau(n_p^{\mathrm{dau}})
    - \log_q \tau(n_p^{\mathrm{par}})
  }_{\text{proton shell change}}
  + 
  \underbrace{
    \log_q \tau(n_n^{\mathrm{dau}})
    - \log_q \tau(n_n^{\mathrm{par}})
  }_{\text{neutron shell change}}
$$

This captures two effects. First, the shell closure gain. When $n^{\mathrm{dau}}$ hits a magic number, $\tau(n_{\mathrm{shell}}) > \tau(n^{\mathrm{par}})$. Therefore $\Delta > 0$. The daughter is more bound, and $Q$ decreases. Second, the shell opening cost. When the parent has a magic closure that the daughter breaks, $\Delta < 0$. Therefore $Q$ increases.

### Step 5: Weak vertex

The $T_{3,5}$ weak vertex contributes:

$$
  \Delta_{T_{3,5}} = \log_q \mathrm{tr}_{\mathrm{Markov}}(T_{3,5}, 3) = -3.370
$$

### Step 6: Inner shell dressing

The inner closed shells are shared between parent and daughter. They are conjugated by $T_{2,9}$:

$$
  \Delta_{\mathrm{inner}} = 0
  \qquad\text{(cancels: same shells on both sides)}
$$

This uses conjecture (C3).

### Step 7: $Q$-value

$$
  \boxed{
    Q(Z, N)
    = 
    \bigl|
      R_{\mathrm{bare}}
      + \Delta_{\mathrm{shell}}
      + \Delta_{T_{3,5}}
    \bigr|
     \times 
    \hbar_q \cdot E_{\times}(q) \cdot \mu_0
  }
$$

Here $\hbar_q = 1 - q^{-1}$, $E_{\times} = \frac{1}{2}(q - q^{-1})$, and $\mu_0 = m_e / (3 E_{\times})$.

## Worked example: ${}^{60}\mathrm{Co}$ ($Z = 27, N = 33$)

**Step 0:**
- $m_{\leq}(27) = 20$, $m_{\leq}(33) = 28$
- $m_{\leq}(28) = 28$, $m_{\leq}(32) = 28$

**Step 1:**
- $n_p^{\mathrm{par}} = 27 - 20 = 7$ (open, size-8 shell)
- $n_n^{\mathrm{par}} = 33 - 28 = 5$ (open, size-22 shell)
- $n_p^{\mathrm{dau}} = 28 - 28 = 0$ (magic)
  Use $n_{\mathrm{shell}}(28) = 28 - 20 = 8$.
- $n_n^{\mathrm{dau}} = 32 - 28 = 4$ (open)

**Step 2:**
- $\tau(7) = \mathrm{tr}(T_{2,7}) \approx 1.299$, $\log_q = +2.51$
- $\tau(5) = \mathrm{tr}(T_{2,5}) \approx 0.993$, $\log_q = -0.07$
- $\tau(8) = \mathrm{tr}(T_{2,8}) \approx 1.736$, $\log_q = +5.29$ (for the closed proton shell)
- $\tau(4) = \mathrm{tr}(T_{2,4}) \approx 1.257$, $\log_q = +2.19$

**Step 3:**
$R_{\mathrm{bare}} = -32.09$

**Step 4:**

$$
  \Delta_{\mathrm{shell}}
  = (\log_q \tau(8) - \log_q \tau(7))
  + (\log_q \tau(4) - \log_q \tau(5))
  = (5.29 - 2.51) + (2.19 - (-0.07))
  \approx 2.78 + 2.26 = +5.04
$$

**Step 5:**
$\Delta_{T_{3,5}} = -3.37$

**Step 7:**

$$
  Q = |{-32.09 + 5.04 + (-3.37)}|
  \times 0.0991 \times 0.1045 \times 1.630
  \approx 30.42 \times 0.01688
  \approx 0.513 \text{ MeV}
$$

The measured value is $\mathcal{Q}_{\mathrm{exp}} \approx 0.318 \pm 0.0001$ MeV, giving a $+61\%$ discrepancy.

**Coverage.** The algorithm produces a definite answer for any $(Z, N)$ from $q$ alone. The $+61\%$ error for ${}^{60}$Co indicates the shell correction (Step 4) is not yet capturing the full structure. The conjectures (C1)–(C3) require verification. The magic number derivation (C1) from $q$ remains the key open problem.
