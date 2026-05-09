*The binding energy of $H_2$ is:*

$$
  \mathbf{E}_{\mathrm{bind}}(H_2)
  = \alpha \cdot y_{\mathrm{cov}}^*
  = \alpha \cdot \bigl(2\Phi_1^H - \Phi_1^{H_2}\bigr)
$$

*where $\alpha = m_e \times 8G \approx 0.511 \times 7.328
\approx 3.744 \;\mathrm{MeV}$ is the universal binding scale
from the [Wedderburn mass formula](#thm\:wedderburn-mass-formula).*

*The optimal binding from the LP dual encodes:*

1. **Attractive contribution**: each shared electron creates
   two $\sigma^{-1}$ crossings (one to each proton), reducing
   $\Phi_1$ by the covalent channel eigenvalue ratio.

2. **Repulsive penalty**: the $\mathfrak{p}_1\mathfrak{p}_2$
   crossing ($\sigma$, eigenvalue $q$) and the $e_1 e_2$
   crossing ($\sigma$, eigenvalue $q$) increase $\Phi_1$.

3. **Net binding**: the two attractive crossings per shared
   electron outweigh the one repulsive crossing between
   protons, giving net positive binding.

*The LP dual shadow price $y_{\mathrm{cov}}^*$ directly gives
the **bond dissociation energy** — the energy required to
separate $H_2$ into two H atoms.  The :refterm[observed value]{#observed-value} is
$D_0(H_2) \approx 4.478 \;\mathrm{eV}$.*

*Computationally, the $H_2$ braid is small enough ($H_4(q)$,
dimension $4! = 24$) to enumerate all orderings exactly.
The witness computation should be committed as
`h2-molecular-binding.witness.json`.*
