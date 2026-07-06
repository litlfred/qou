This appendix collects the transfer-matrix changes induced by the
elementary nuclear and electromagnetic processes. Each such process
is, at bottom, a local rewrite of crossing type, and the quantity we
care about is the difference between the transfer matrix after the
rewrite and the transfer matrix before it. Concretely, an
**interaction** that changes the crossing type from
$(K_1, K_2)$ to $(K_1', K_2')$ is encoded by the
$\Delta$ operator:

$$
  \Delta_{K_1 K_2 \to K_1' K_2'}(q)
  = 
  T_{K_1', K_2'}(q) - T_{K_1, K_2}(q)
$$

The sections below work this out process by process. Beta decay
(§1) is the worked instance from which the others are built: every
subsequent case is either the same matrix, its negation, or a
composition of copies of it.

## 1. The universal beta decay matrix

The step from any nuclear crossing type to the next is
**always the same matrix**:

$$
  \Delta_\beta(q)
  = 
  T_{\mathrm{mix}}(q) - T_{nn}(q)
  = 
  T_{pp}(q) - T_{\mathrm{mix}}(q)
$$

In closed form:

$$
  \boxed{
    \Delta_\beta(q)
    = 
    \tfrac{1}{2}(q - q^{-1}) \mathbb{I}
  }
$$

**Explicit entries:**

$$
  \Delta_\beta(q) = 
  \begin{pmatrix}
    \dfrac{q - q^{-1}}{2} & 0 \\[6pt]
    0 & \dfrac{q - q^{-1}}{2}
  \end{pmatrix}
$$

See [Table 1](#tbl:tm-interactions-table1-data).

**Properties:**

- $\Delta_\beta$ is **scalar** (proportional to $\mathbb{I}$): it commutes with every transfer matrix.
- At $q = 1$: $q - q^{-1} = 0$ and $\Delta_\beta = 0$ (no parity violation classically).
- **Universality**: the same $\Delta_\beta$ applies to every nucleus, for
 every converting nucleon, regardless of the partner.

## 2. Reverse beta decay ($\beta^+$)

Positron emission runs $\beta^-$ backwards, so it undoes exactly the
crossing-type change of §1. Its transfer-matrix difference is
therefore the same operator with the opposite sign:

$$
  \boxed{
    \Delta_{\beta^+}(q) =  -\Delta_\beta(q)
  }
$$

$\beta^+$ decay is $\mathfrak{u} \to \mathfrak{d}$, the reverse
of $\beta^-$ ($\mathfrak{d} \to \mathfrak{u}$). The matrix is
 negated.

## 3. Photon absorption (Reidemeister I move)

Photon absorption does not change a crossing type — it
**appends** a new transfer matrix factor $T_{\gamma e}$ to
the chain at the absorbing generator:

$$
  \boxed{
    M_i^{(n+1)}(q) =  T_{\gamma e}(q) \cdot M_i^{(n)}(q)
    =  T_{pp}(q) \cdot M_i^{(n)}(q)
  }
$$

The energy change for shell $n \to n+1$:

$$
  \Delta E_{n \to n+1}
  = 
  \hat{V}(M_i^{(n+1)}) - \hat{V}(M_i^{(n)})
$$

For hydrogen (single generator), the transfer matrix at
shell $n$ is $T_{pp}^n$ (the $n$-th matrix power), and
the energy scales as $\lambda_+^n$ where $\lambda_+$ is
the larger eigenvalue of $T_{pp}$.

## 4. Pair creation ($\gamma\gamma \to e^- e^+$)

Pair creation is a chirality-changing crossing replacement of the
same form as $\beta^+$, so its transfer-matrix difference lands on
the same operator as §2:

$$
  \boxed{
    \Delta_{\mathrm{pair}}(q)
    = 
    T_{e^- e^+}(q) - T_{\gamma\gamma}(q)
    = 
    T_{\mathrm{mix}}(q) - T_{pp}(q)
    = 
    -\Delta_\beta(q)
  }
$$

Pair creation consumes a **two-photon crossing** (empty–empty)
and produces a **particle–antiparticle crossing** (trefoil–mirror
trefoil). A single photon cannot pair-produce in vacuum
(momentum conservation requires either a second photon or a
nearby nucleus to absorb recoil). The transfer matrix change
is the same as $\beta^+$ decay: a chirality-changing crossing
replacement.

## 5. Double beta decay ($2\beta$)

At a generator $\sigma_i$ affected by both converting
nucleons at positions $p_1$ and $p_2$:

$$
  \Delta M_i^{(2\beta)}
  = 
  L_i \cdot \Delta_\beta \cdot C_i \cdot \Delta_\beta \cdot R_i
  + 
  L_i \cdot \Delta_\beta \cdot R_i'
  + 
  L_i' \cdot \Delta_\beta \cdot R_i
$$

where $C_i$ is the product of unchanged transfer matrices
between the two converting positions, and $L_i, R_i$ are
the products to the left and right. The **quadratic term**
$\Delta_\beta \cdot C_i \cdot \Delta_\beta$ is the nuclear
matrix element of double beta decay.

## 6. Toffoli transfer matrix (information-theoretic)

On $3$ strands with nucleon types
$[\mathfrak{p}, \mathfrak{p}, \mathfrak{n}]$, the Toffoli
gate selects the target strand whose control--control pair
has unit crossing coefficient ($c = 1$).

The target-flip amplitude factors as:

$$
  P_{\mathrm{flip}}(q; k_1, k_2) =  c_{k_1 k_2}(q) \cdot \Phi(q)
$$

where $c_{k_1 k_2}$ is the control--control crossing
coefficient and:

$$
  \boxed{
    \Phi(q) = 
    \frac{(q-1)(q^{3/2} + q^{1/2} - 1)(q^{3/2} + q + 1)}{2(q+1)^2}
  }
$$

The full $2 \times 2$ Toffoli transfer matrix $\mathbf{M}(q)$:

See [Table 2](#tbl:tm-interactions-table2-data).

**Single-crossing type-blindness:** at generator $\sigma_1$
(one crossing), $\hat{V}_1 = z$ regardless of crossing
type. A single crossing carries no type information.

## 7. Catalogue of all $\Delta$ operators

See [Table 3](#tbl:tm-interactions-table3-data).
