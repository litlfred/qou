**Conjecture ($q$-Collatz).**
Let $(\mathbf{C}, A, \tau)$ be a quantum universe with
Frobenius--Hopf substrate $A$
([substrate](#def:frobenius-hopf-substrate)),
categorical Reeb derivation $\xi_q \colon A \to A$
([Reeb derivation](#def:categorical-reeb-derivation)),
$q$-Reeb flow $\phi_t^q \in \mathrm{Aut}(A)$
([categorical $q$-Reeb flow](#def:categorical-q-reeb-flow)),
and substrate parameter $q \in \mathbb{G}_m^{\mathrm{nt}}(k)$
([torsion avoidance](#rem:substrate-gm-torsion)).

### The Reeb-rotated Hecke--Collatz endomorphism

The Hecke--Reeb idempotents
$e_+(\xi_q), e_-(\xi_q) \colon A \to A$
project onto the symmetric (weight-$0$) and antisymmetric
(weight-$1$) eigenspaces of $\xi_q$
([skein generation](#prop:skein-generation)).
Define the **single-step Collatz endomorphism**:

$$
  \widetilde{C}_q
  \;=\;
  e_+(\xi_q)\,\circ\,\mu^{-1}_{[2]_q}
  \;+\;
  e_-(\xi_q)\,\circ\,\mu^{-1}_{[2]_q}
  \,\circ\,\bigl(\mu_{[3]_q} + \eta\bigr),
$$

where both branches include division by $[2]_q$ — the
accelerated form encoding the classical identity that
$3n+1$ is always even for odd $n$.

The **Reeb-rotated Hecke--Collatz map** is the
composition of $\widetilde{C}_q$ with one Reeb advance:

$$
  C_q \;:=\; \phi^q_{t_P}\,\circ\,\widetilde{C}_q,
$$

where $\phi^q_{t_P}$ is the Reeb flow over one Planck
time $t_P = \hbar_q = (q-1)/q$
([operations per Planck](#prop:reeb-operations-per-planck)).
The Reeb advance **rotates the eigendecomposition**:
after each Collatz step, the element's projection onto
$A_H \oplus A_V$ is re-evaluated in the rotated frame.
This models the classical phenomenon that parity changes
under arithmetic operations.

### The contraction estimate

**Algebraic identity.**
For all $q > 0$:

$$
  [2]_q^2 - [3]_q \;=\; q.
$$

*Proof.* $[2]_q^2 = (q+1)^2 = q^2 + 2q + 1$ and
$[3]_q = q^2 + q + 1$; the difference is $q$.  $\square$

**Consequence:** $[3]_q / [2]_q^2 < 1$ for all $q > 0$.

Over one Reeb period $\Omega_q$, an element $a \in A$
spends a fraction $f_+$ of the time in the symmetric
eigenspace $A_H$ (where $\widetilde{C}_q$ contracts by
$1/[2]_q$) and $f_- = 1 - f_+$ in the antisymmetric
eigenspace $A_V$ (where $\widetilde{C}_q$ has ratio
$[3]_q/[2]_q$).  The **Reeb-averaged Lyapunov exponent**
is

$$
  \log\lambda_q(f_+)
  \;=\;
  f_+ \log\frac{1}{[2]_q}
  \;+\;
  f_- \log\frac{[3]_q}{[2]_q}.
$$

The orbit contracts ($\lambda_q < 1$) iff

$$
  f_+ \;>\; f_+^*(q)
  \;:=\;
  \frac{\log\bigl([3]_q / [2]_q\bigr)}
       {\log [3]_q}.
$$

At equal distribution $f_+ = 1/2$:

$$
  \lambda_q({\textstyle\frac{1}{2}})
  \;=\;
  \sqrt{\frac{[3]_q}{[2]_q^2}}
  \;<\; 1
  \qquad(\text{by } [3]_q < [2]_q^2).
$$

Since $f_+^*(q) < 1/2$ for all $q > 0$, equal
distribution always lies in the contractive regime.

### The Collatz horizon

Define the **Collatz convergent subcategory**

$$
  A^{\mathrm{conv}}_q
  \;:=\;
  \bigl\{\,a \in A \;:\;
  \langle f_+ \rangle_{\mathrm{Reeb}}(a) > f_+^*(q)
  \,\bigr\},
$$

where $\langle f_+ \rangle_{\mathrm{Reeb}}(a)$ is the
time-averaged fraction that the $C_q$-orbit of $a$
spends in $A_H$ over a Reeb period.

The **Collatz horizon** is

$$
  \mathcal{H}_{Col}(q)
  \;:=\;
  \overline{A^{\mathrm{conv}}_q}
  \;\setminus\;
  A^{\mathrm{conv}}_q
  \;=\;
  \bigl\{\,a \in A \;:\;
  \langle f_+ \rangle_{\mathrm{Reeb}}(a) = f_+^*(q)
  \,\bigr\}.
$$

This is the codimension-$1$ locus where the
Reeb-averaged Lyapunov exponent changes sign — the
exact analog of the computational boundary
$\mathcal{H}_c$ in the P $\neq$ NP conjecture
([P vs NP boundary](#conj:p-vs-np-boundary)).

### The conjecture

**In a QOU** $(\mathbf{C}, \theta, G, \mathcal{S})$:
the Collatz obstruction $\kappa_C :=
\mathrm{res}_{C_q}(\kappa_0)$ satisfies

$$
  \boxed{\kappa_C = 0
  \quad\Longleftrightarrow\quad
  \mathcal{H}_{Col}(q) = \varnothing
  \quad\text{for all } q > 1.}
$$

Equivalently: the Reeb flow distributes every element
$a \in A$ with $\langle f_+ \rangle > f_+^*(q)$, and
the entire positive cone converges to the fixed point
$a^* = \eta(\mathbf{1}) / (1 - \lambda_q)$.

### Size boundary

The Collatz horizon (if non-empty) has explicit size:

| Quantity | Formula | At $q = q_0$ |
|----------|---------|--------------|
| Critical fraction | $f_+^*(q) = \frac{\log([3]_q/[2]_q)}{\log [3]_q}$ | $0.381$ |
| Contraction at $f_+ = 1/2$ | $\lambda_q = \sqrt{[3]_q/[2]_q^2}$ | $0.866$ |
| Gap | $[2]_q^2 - [3]_q = q$ | $1.110$ |
| Fixed point | $a^* \approx (1/[2]_q)/(1 - \lambda_q)$ | $\approx 3.5$ |

At $q \to 1$: $f_+^* \to \log_3(3/2) \approx 0.369$ and
$\lambda_q \to \sqrt{3/4} \approx 0.866$.  Since the Reeb
flow gives $\langle f_+ \rangle = 1/2 > 0.369$, the
contraction margin is $1/2 - f_+^* \approx 0.131$ — a
$13\%$ excess beyond the critical threshold.

### Classical limit

At $q = 1$: $[2]_1 = 2$, $[3]_1 = 3$, the Reeb rotation
degenerates to the parity alternation, and the accelerated
$\widetilde{C}_1$ recovers the Syracuse map:

$$
  \widetilde{C}_1(n)
  = \begin{cases}
      n/2 & n \text{ even},\\
      (3n + 1)/2 & n \text{ odd}.
    \end{cases}
$$

The classical Collatz conjecture is: the horizon
$\mathcal{H}_{Col}(1) = \varnothing$.  The classical
heuristic (even steps occur with frequency $\approx 1/2$)
matches the QOU prediction: $1/2 > f_+^*(1) \approx 0.369$.
