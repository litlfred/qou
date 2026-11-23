# Pre-Registration Addendum: Layer-2 Sturmfels–Thomas ChamberGS (`A_0` & `A_shell`)

## Scope & Anti-Fit Discipline

This pre-registration fixes the exact integer matrices `A_0` and `A_shell`, Graver/Gröbner enumeration algorithms, `workdps = 80`, `q0Anchor = "proton"`, and chamber-coincidence assertions (`qou-h6ef` Approved Options 1 + 2 + 3) prior to writing `chamber_gs_model_a_b_probe.py`:

1. **Model A (`A_0` Core 1s Cluster Matrix):**
   $$A_0 = \begin{pmatrix} 1 & 0 & 1 & 1 & 2 & 2 \\ 0 & 1 & 1 & 2 & 1 & 2 \end{pmatrix}$$
   on $(x_p, x_n, x_d, x_t, x_h, x_\alpha)$.
   - Compute exact $\mathrm{Gr}_{A_0}$ by both Pottier S-pair completion and exhaustive $[-6,6]^4$ kernel box search, verifying $|\mathrm{Gr}_{A_0}| = 28$ unsigned ($56$ signed) and $17$ unsigned circuits.
   - Enumerate the complete Gröbner fan $\mathrm{GF}(I_{A_0})$ in $\mathbb{Q}^4$ via exact rational facet-flipping BFS and cross-check against `sympy.groebner`, verifying $|\mathrm{GF}(I_{A_0})| = 73$ full-dimensional chambers and $|\mathcal{U}_{A_0}| = 27$ unsigned Universal Gröbner Basis binomials (sole non-UGB Graver element: $x_\alpha - x_p x_n x_d$).
   - Verify whether parameter-free QOU bare $q_0$, QOU tower $q_0$, and experimental AME2020 cluster binding energies all sit strictly inside the **exact same** 5-wall physical chamber $\mathcal{C}_{\mathrm{phys}}$ with the 11-rule minimal reduced Gröbner basis $\mathcal{G}_{\mathrm{phys}}$.
   - Verify exact normal-form reductions modulo $\mathcal{G}_{\mathrm{phys}}$, including ${}^5\mathrm{He}$ ($x_p^2 x_n^3 \to x_\alpha x_n$ neutron-drip monomer) and odd–even / $N=Z$ remainder monomers.

2. **Model B (`A_shell` Capacitated Mayer–Jensen Shell Matrix):**
   - For $S = 7$ Mayer–Jensen shell capacities $C_s = [2, 6, 12, 8, 22, 32, 44]$ (cumulative magic closures $[2, 8, 20, 28, 50, 82, 126]$), verify $|\mathrm{Gr}_{B_{\mathrm{shell}}}| = \binom{S}{2}$ unsigned per species and 100% confluence of the $S - 1$ adjacent single-shell promotion rules $u_{s+1} w_s \to u_s w_{s+1}$ across all valid integer fiber states $u_s + w_s = C_s \ge 1$.
