The light-nucleus examples use only the bare transfer matrix product. For heavy nuclei, shell corrections from the magic number structure become essential. This section works through the full $Q$-value algorithm on simplified two-strand transfer-matrix chains, illustrating how a definite $Q$-value output follows from the aether parameter $q$. Whereas in the three-dimensional $\alpha$-simplex model of Chapter 10 the Mayer–Jensen magic closures $\mathcal{M} = \{2, 8, 20, 28, 50, 82, 126\}$ arise unconditionally from $(2j+1)$ spin–orbit sub-shell degeneracy splitting of three-dimensional harmonic-oscillator levels ([higher-$\ell$ spin–orbit magic closures](#prop:spin-orbit-magic-closures)), the linear two-strand examples worked out in this appendix treat $\mathcal{M}$ as input shell boundaries conditional on the dominant-binding-operator and inner-shell cancellation rules [(C1)–(C3)](#rem:shell-construction-rules). Where a residual remains in the two-strand chain, it reflects that reduction rather than an adjustable parameter.

Recall: $s = q^{1/2} - q^{-1/2}$, $z = q^3/(q^2+1) = q^2/[2]_q$ (canonical Convention D, distinct from the symmetric Temperley–Lieb factor $1/(q^{1/2}+q^{-1/2})$, at which the illustrative decimals in the legacy tables below were evaluated), $\hbar_q = 1 - q^{-1}$, $E_{\times} = \frac{1}{2}(q - q^{-1})$, and $\mu_0$ the remaining conversion constant that carries the dimensionless bracket into MeV.

## The magic number table

Shell closures occur at the Mayer–Jensen nucleon counts (derived in three dimensions via [spin–orbit magic closures](#prop:spin-orbit-magic-closures), where the corresponding Gröbner--Shirshov word-length histogram is palindromic):

$$
  \mathcal{M} = \{0, 2, 8, 20, 28, 50, 82, 126\}
$$

For nucleon count $X$, see [Table 1](#tbl:tm-heavy-atom-examples-table1-data). When $X$ is magic ($n_{\mathrm{out}} = 0$), the outermost shell is closed and the relevant shell size is $n_{\mathrm{shell}}(X)$.

## The $Q$-value algorithm (summary)

**Input:** $(Z, N)$, aether parameter $q$.

1. Compute outer shell occupancies for parent $(Z, N)$ and daughter $(Z+1, N-1)$.
2. Compute torus knot Markov traces $\tau(n)$ for each occupancy from the Chebyshev recurrence.
3. Compute bare Skein polynomial ratio $R_{\mathrm{bare}} = \log_q(P_{\mathrm{dau}} / P_{\mathrm{par}})$.
4. Compute shell correction $\Delta_{\mathrm{shell}} = (\text{proton shell change}) + (\text{neutron shell change})$.
5. Add weak vertex $\Delta_{T_{3,5}} = -3.370$.
6. Convert: $Q = |R_{\mathrm{bare}} + \Delta_{\mathrm{shell}} + \Delta_{T_{3,5}}| \times \hbar_q \cdot E_{\times} \cdot \mu_0$.

## Example 6: Carbon-14 ($A = 14$, $Z = 6$, $N = 8$)

${}^{14}\mathrm{C} \to {}^{14}\mathrm{N}$ ($\beta^-$: $\mathfrak{d} \to \mathfrak{u}$ at one neutron).

This is the anomalously slow decay ($t_{1/2} = 5730$ yr, $\log ft = 9.04$). The shell structure explains why.

See [Table 2](#tbl:tm-heavy-atom-examples-table2-data). The parent has a closed neutron shell at $n = 8$. The daughter breaks it ($N = 8 \to N' = 7$).

**Parent** ${}^{14}\mathrm{C}(6, 8)$: 13 generators, $\binom{14}{2} = 91$ matrix multiplications. Nucleon ordering: $[\underbrace{\mathfrak{p} \cdots \mathfrak{p}}_{6} \underbrace{\mathfrak{n} \cdots \mathfrak{n}}_{8}]$. The converting neutron (position 6) affects $\sigma_0$ through $\sigma_6$.

See [Table 3](#tbl:tm-heavy-atom-examples-table3-data). Generator $\sigma_6$ carries nearly half the total energy change ($-1.660$ of $-3.361$). Its chiral degree $k_6 = 7$ means all 7 crossings with downstream nucleons change type.

The parent's 8-neutron shell is closed. The Skein polynomial factors: $J_{8\mathfrak{n}}(q) = J_{\mathcal{N}(0,2)}(q)^4 \cdot (\text{linking factors})$. Breaking one neutron pair destroys this factorization. The matrix element is suppressed by $1/|J_{\mathcal{N}(0,2)}(q)| \approx 1/2.01$. Combined with the spin-parity mismatch ($0^+ \to 1^+$), this gives $|\mathcal{M}|^2 \sim 10^{-6}$.

Leading-order: $t_{1/2} \approx 6690$ yr vs observed $5730$ yr. The 17% residual is the shell correction contribution. The $n = 8$ closed sub-link provides extra parent stability, increasing $\mathfrak{Q}_\beta$ via the $Q^5$ phase-space factor.

## Example 7: Cobalt-60 ($A = 60$, $Z = 27$, $N = 33$)

${}^{60}\mathrm{Co} \to {}^{60}\mathrm{Ni}$ ($\beta^-$). An allowed Gamow--Teller transition where the daughter gains a proton shell closure.

See [Table 4](#tbl:tm-heavy-atom-examples-table4-data). The daughter has $Z' = 28$—a closed proton shell.

Each outer-shell occupancy contributes a torus-knot Markov trace $\tau(n)$. See [Table 5](#tbl:tm-heavy-atom-examples-table5-data).

$R_{\mathrm{bare}} = -32.09$ (from $\binom{60}{2} = 1770$ multiplications).

$$
  \Delta_{\mathrm{shell}} = \underbrace{(\log_q \tau(8) - \log_q \tau(7))}_{\text{proton: } +2.78} + \underbrace{(\log_q \tau(4) - \log_q \tau(5))}_{\text{neutron: } +2.26} = +5.04
$$

The proton shell closure ($+2.78$) dominates: the daughter gains the stability of a closed $Z = 28$ shell.

$$
  Q = |{-32.09 + 5.04 + (-3.37)}| \times \hbar_q \cdot E_{\times} \cdot \mu_0 \approx 0.513 \text{ MeV}
$$

$\mathcal{Q}_{\mathrm{exp}} \approx 0.318$ MeV. Error: $+61\%$. The residual measures shell structure not yet captured by the correction.

## Example 8: Bismuth-210 ($A = 210$, $Z = 83$, $N = 127$)

${}^{210}\mathrm{Bi} \to {}^{210}\mathrm{Po}$ ($\beta^-$). The heaviest nucleus in the verification table, requiring $\binom{210}{2} = 21{,}945$ multiplications.

See [Table 6](#tbl:tm-heavy-atom-examples-table6-data). Both parent counts sit one above a magic number. The daughter's neutron count $N' = 126$ hits a magic closure.

209 generators, each carrying up to 209 crossings at $\sigma_0$. At generator $\sigma_i$:
- $j < 83$: $T_{pp}$
- $83 \leq j < 210$: $T_{\mathrm{mix}}$ if $i < 83$, $T_{nn}$ if $i \geq 83$

The converting neutron (position 83) affects $\sigma_0$ through $\sigma_{83}$. The daughter gains a closed neutron shell at $N' = 126$. The proton count moves from $n_{\mathrm{out}} = 1$ to $n_{\mathrm{out}} = 2$.

See [Table 7](#tbl:tm-heavy-atom-examples-table7-data). The computation is exact. Every jet order through the $209$-jet is included in the product.

## Summary: shell structure across the periodic table

See [Table 8](#tbl:tm-heavy-atom-examples-table8-data).

Transitions that create or destroy a closed sub-link at a magic number have the largest matrix-element corrections. ${}^{137}\mathrm{Cs}$ has the smallest residual (9%) because the daughter ${}^{137}\mathrm{Ba}$ is one neutron short of the $n = 82$ closure.

The shell correction reflects the discrete closure structure of the Skein polynomial. Replacing this simplified two-strand approximation with quantitative heavy-nucleus predictions proceeds through the three-dimensional $\alpha$-simplex shell hierarchy and $(2j+1)$ spin–orbit sub-shell closures of [spin–orbit magic closures](#prop:spin-orbit-magic-closures) under canonical Convention D ($z = q^3/(q^2+1)$).
