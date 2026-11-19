**Algorithm (Parameter-free multi-scale nuclear binding energy).**
*Evaluate the total nuclear binding energy $B(Z, N)$ of an isotope of proton number $Z$, neutron number $N$, and mass number $A = Z + N$ from $(q_{2t}, m_e, \alpha_{\mathrm{EM}}^{\mathrm{corr}})$ with zero empirical liquid-drop or recurrence fit parameters.*

### Input

- *Proton count $Z \in \mathbb{N}$, neutron count $N \in \mathbb{N}$ ($A = Z + N \ge 2$), aether parameter $q = q_{2t} > 1$, electron mass scale $m_e$, and Form-B electromagnetic coupling $\alpha_{\mathrm{EM}}^{\mathrm{corr}}(q)$ (from [Step 9a](#alg:mass-identity)).*

### Output

- *Total nuclear binding energy $B(Z, N) = B_{\mathrm{cell/simp}}(A) - \Delta E_{\mathrm{shell/sym}}(Z, N) + \delta_{\mathrm{pair}}(Z, N) - E_C(Z, A)$ and multi-$\alpha$ breakup thresholds $\Delta B(n_\alpha)$.*

### Algorithm

1. **Intra-cluster $H_4(q)$ full-twist $\alpha$-cell ($A \le 4$ and multi-$\alpha$ breakup thresholds):**
   - Decompose the central 4-strand full twist $\Delta_4^2 = (\sigma_1\sigma_2\sigma_3)^4 \in Z(H_4(q))$ over the five Specht modules $\lambda \in \{(4), (3,1), (2,2), (2,1^2), (1^4)\}$ of dimensions $(1, 3, 2, 3, 1)$ with exact framing eigenvalues $q^{2c(\lambda)} \in \{q^{12}, q^4, 1, q^{-4}, q^{-12}\}$.
   - Evaluate the two-row Convention-D Casimir $\mathrm{Cas}_D(q) = \frac{12(q^4 + 1)}{(q^2 + 1)^2}$ together with the GPMT-renormalised row-$3$/row-$4$ full-twist and Casimir functionals on $(2,1^2)$ and the Wigner-$\mathrm{SU}(4)$ singlet $(1^4)$ (from [Step 5](#alg:wedderburn-decomposition)).
   - For $A = 4 n_\alpha$ $\alpha$-conjugate nuclei, intra-$\alpha$ cell energies cancel identically in breakup thresholds $\Delta B(n_\alpha) = \binom{n_\alpha}{2}(v_{2\alpha} - c_{\mathrm{EM}}) + \binom{n_\alpha}{3} w_{3\alpha} + \binom{n_\alpha}{4} w_{4\alpha}$: because $0 < c_{\mathrm{EM}} - v_{2\alpha} < \tfrac{1}{3} w_{3\alpha}$, the $2\alpha$ dimer $^8\mathrm{Be}$ ($1$ edge, $0$ triangles) has $\Delta B_{2\alpha} < 0$ (unbound), whereas $^{12}\mathrm{C}$ ($3$ edges, $1$ Borromean triangle, $\Delta B_{3\alpha} > 0$) and $^{16}\mathrm{O}$ ($6$ edges, $4$ triangles, $1$ tetrahedron) are strictly bound.
2. **3D simplicial compact-ball triangulation ($A \ge 4$):**
   - Construct the coordinate-verified 3D Euclidean close-packed / Freudenthal–Kuhn shell ball $\mathcal{T}_A$ of $f_0 = A$ vertices with $f_3$ tetrahedra and $f_{0,\partial}$ boundary vertices ($\chi(\mathcal{T}_A) = 1$, $\chi(\partial\mathcal{T}_A) = 2$). Compute the remaining face counts by exact **Dehn–Sommerville elimination**:
     $$
       f_{1,\partial} = 3 f_{0,\partial} - 6,
       \quad
       f_{2,\partial} = 2 f_{0,\partial} - 4,
       \quad
       f_2 = 2 f_3 + f_{0,\partial} - 2,
       \quad
       f_1 = A + f_3 + f_{0,\partial} - 3,
     $$
     capturing both the interior tetrahedral edge-cycle excess $c = f_3 - (A - 3) \ge 0$ ($2 \to 3$ Pachner closures above the minimal 3-tree) and buried interior nucleons $A_{\mathrm{int}} = A - f_{0,\partial}$ ($f_{0,\partial} = O(A^{2/3})$).
   - Weight edges, triangles, and tetrahedra by the Convention-D two-body bonds ($b_{2,\log D}, b_{2,\mathrm{Bor},D}$) and $H_3(q)/H_4(q)$ GPMT Mayer cluster cumulants ($w_3 > 0$, $w_4 < 0$):
     $$
       B_{\mathrm{simp}}(\mathcal{T}_A)
       \;=\;
       f_1\,b_2(q) \;+\; f_2\,w_3(q) \;+\; f_3\,w_4(q).
     $$
3. **3D Pauli/Fermi harmonic-oscillator and Mayer–Jensen spin–orbit shell filling:**
   - Order single-particle subshells $(n_r, \ell, j = \ell \pm \tfrac{1}{2})$ ($N_{\mathrm{osc}} = 2n_r + \ell$) at the Compton oscillator scale and spin–orbit coupling
     $$
       \hbar\omega_q(A) \;=\; \frac{m_e}{(q - 1)^2}\,A^{-1/3},
       \qquad
       \varepsilon(n_r, \ell, j) \;=\; \hbar\omega_q(A)\Bigl(N_{\mathrm{osc}} + \tfrac{3}{2} - \kappa_{\mathrm{SO}}(q)\,\langle \ell \cdot s \rangle_j\Bigr).
     $$
   - Fill $Z$ protons and $N$ neutrons independently into subshells of exact Pauli capacity $2j + 1$ ($g_+(\ell) = 2\ell + 2$, $g_-(\ell) = 2\ell$). Cumulative oscillator closures $C_{\mathrm{osc}}(K) = \frac{(K+1)(K+2)(K+3)}{3}$ plus the depressed stretched intruder $j = K + \tfrac{3}{2}$ ($g_+(K+1) = 2K + 4$) generate both the $1p_{3/2}$ subshell closure at $6$ ($^{12}\mathrm{C}$) and the magic closures $2, 8, 20, 28, 50, 82, 126$, while neutron–proton Fermi promotion ($N - Z = 2d$) produces the quadratic Pauli symmetry energy $\Delta E_{\mathrm{Pauli}}(Z, N) \propto \frac{(N - Z)^2}{A}$.
4. **Temperley–Lieb seniority pairing and simplicial FCC Coulomb repulsion:**
   - Within the valence subshell of each species, evaluate the seniority-$0$ Kramers pair projector $e_{\mathrm{pair}}^2 = [2]_q\,e_{\mathrm{pair}}$ with pairing gap $\Delta_{\mathrm{TL}}(q) = \tfrac{1}{2} g_{\mathrm{pair}}\,[2]_q$, adding $+\Delta_{\mathrm{pair}}$ for even–even ($v_p = v_n = 0$), $0$ for odd-$A$ ($v_p + v_n = 1$), and $-\Delta_{\mathrm{pair}}$ for odd–odd ($v_p = v_n = 1$) nuclei.
   - Subtract the electrostatic proton-pair energy $E_C(Z, A)$: on $\mathcal{T}_A$ ($A \le 4$ and $\alpha$-clusters), sum exact inverse vertex distances $E_C^{\mathrm{disc}} = \frac{\alpha_{\mathrm{EM}}^{\mathrm{corr}}\,\hbar c}{2}\sum_{u \neq v} p_u p_v\,d(u, v)^{-1}$ at bond length $\ell_{\mathrm{bond}} = \tfrac{3}{2}\bar\lambda_\pi$ (yielding $\binom{Z}{2}\frac{\alpha_{\mathrm{EM}}^{\mathrm{corr}}\,\hbar c}{\ell_{\mathrm{bond}}}$ on a regular simplex with zero continuum $3/5$ distortion), and for bulk close-packed shells transport the 3D FCC packing radius scale $r_{0,\mathrm{FCC}} = \left(\tfrac{3}{16\pi}\right)^{1/3}\ell_{\mathrm{bond}}$.

### Termination and Complexity

Dehn–Sommerville face elimination and seniority/magic-shell occupancy run in $O(A)$ exact integer operations; explicit pairwise vertex summation on $\mathcal{T}_A$ requires $O(Z^2)$ operations in $\ge 80$-digit ball arithmetic.

### Mathematical Justification

1. **Per-partition Springer/DT index and $H_4(q)$ weights:** The signed block index $\Delta_\lambda = (-1)^{n(\lambda)}\dim V_\lambda$ is proved in [Donaldson–Thomas index unification](#prop:delta-lambda-dt-index-unification) (with density context in [the binding-density remark](#rem:term6-binding-density)), and the explicit $H_4(q)$ orthogonal weights follow [explicit $H_4(q)$ Wedderburn weights](#prop:explicit-alpha-k-h4).
2. **Spin–orbit magic closures and quadratic Pauli promotion:** Subshell capacities $2j + 1$, the Mayer–Jensen sequence $M_K = \frac{(K+1)(K+2)(K+3)}{3} + (2K + 4)$, and the quadratic $(N - Z)^2$ Fermi promotion identity are proved in [spin–orbit magic closures](#prop:spin-orbit-magic-closures). Remaining open coarse-graining and heavy-actinide deformation items are recorded in [the $\Delta_\lambda$ structural sidecar](#alg:delta-lambda-closure).
