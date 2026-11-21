## Proof

**Withdrawn (owner ruling 2026-11-21).** The shell-size rule used here, that a closing shell of size $n_s$ is bound by the torus knot $T_{2,n_s}$, is withdrawn. Its basis was a mislabel: $(\sigma_0\sigma_1)^2\sigma_0$ closes to $T(2,4)$, not to the cinquefoil $T(2,5)$. The rule stays withdrawn until it is derived. Steps (i) and (v) use the rule directly, so this argument does not establish the [proposition](#prop:torus-knot-shell-binding).

The construction proceeds by induction on nucleon count, with shell closures detected by palindromic word-length histograms.

**(i) Shell closure triggers the inter-shell operator.**
When the word-length histogram of $\bar{\mathcal{N}}(p, n)$ is palindromic at nucleon count $A = A_{\mathrm{close}}$, the next nucleon crosses the closed shell via $\Phi_{\mathrm{shell}}^{(\ell)}$ with the torus knot $T_{2, n_s}$, where $n_s = A_{\mathrm{close}} - A_{\mathrm{prev}}$ is the size of the closing shell.

**(ii) Normalization is preserved across shell boundaries.**
The inter-shell operator $\Phi_{\mathrm{shell}}^{(\ell)}$ produces a Gröbner--Shirshov normal form. As in the intra-shell step, the Chebyshev crossing element $(c_{n_s}\sigma + d_{n_s})$ is linear in $\sigma$, and the division algorithm produces a unique normal form remainder. The palindromic structure of the previous shell is preserved: the new nucleon's generators act on strands $A, A+1, \ldots$, which are disjoint from the closed shell's generators $0, \ldots, A_{\mathrm{close}} - 1$.

**(iii) Shell capacities from the six embeddable torus knots.**
The embeddable torus knots on the Bring surface assign shell sizes via their $r \times s$ products.

See [Table 2](#tbl:torus-knot-shell-binding-table2-data).

The shell capacity is the number of nucleon pairs that the torus knot can bind. Each torus knot $T_{r,s}$ mediates a shell of size $r \times s$ nucleon crossings. The actual shell occupancy is the number of nucleon pairs (proton + neutron) that fill the shell before palindromic closure.

The degree-1 knots ($T_{2,n}$, single-strand meridional winding) establish the primary shell sequence. The degree-2 knots ($T_{2,9}$, $T_{3,4}$) provide sub-shell splittings that refine the primary shells.

**(iv) The cumulative magic number sequence.**
The magic numbers are the cumulative sums of shell occupancies. Each shell closes when same-type nucleons fill all available crossings:

See [Table 3](#tbl:torus-knot-shell-binding-table3-data).

This construction is **proposed** to reproduce the experimental magic numbers $\{2, 8, 20, 28, 50, 82, 126\}$; a closed from-$q$ derivation of the full sequence — reconciling the Table-2 $r\times s$ capacities with the Table-3 occupancies — remains the **key open problem** and is not established by the induction above.

**(v) Energy gap at shell boundaries.**
The Hecke energy $\Delta E$ jumps by a factor $\sim |\lambda_+(T_{2,n_s})/\lambda_-(T_{2,n_s})|$ at each shell boundary. For the first shell closure (He-4 $\to$ Li-5):

$$
  \frac{\Delta E_5}{\Delta E_4} \approx \frac{1.409}{0.095} = 14.8
$$

This ratio defines the shell gap, the algebraic signature of the transition from intra-shell (bare crossings) to inter-shell (torus knot crossings). The gap grows with shell size because the torus knot eigenvalue ratio $|\lambda_+/\lambda_-| = q^{2n_s}$ increases exponentially.

## Gröbner--Shirshov preservation across all shells (inductive summary)

The full inductive argument for the construction of any nucleus $\mathcal{A}(Z, N)$ proceeds as follows:

1. **Base.** $\bar{\mathcal{N}}(1, 0) = \mathbf{1}$, which is in normal form by definition.
2. **Intra-shell step.** Given $\bar{\mathcal{N}}_A$ in normal form within shell $\ell$, the next nucleon crosses via the bare transfer matrix $(c_j\sigma_j + d_j)$. Gröbner--Shirshov division ensures the result is in normal form.
3. **Shell closure detection.** After each step, the word-length histogram is checked. If it is palindromic, the shell is closed.
4. **Inter-shell step.** After a shell closure, the next nucleon crosses the closed shell via the Chebyshev crossing element $(c_{n_s}\sigma + d_{n_s})$ of $T_{2, n_s}$. Because this element is linear in $\sigma$, it enters the Gröbner--Shirshov division exactly like an intra-shell crossing. The algorithm produces a normal form.
5. **Repeat** until $A = Z + N$ nucleons are linked.

At every step, the Gröbner--Shirshov division algorithm produces a unique normal form. The inter-shell step differs only in the magnitude of the crossing coefficients, not in algebraic structure. Normalization preservation follows from the same theorem used for intra-shell steps.
