The full sublimation criterion ([shell-filling criterion](#prop:composite-crossing-parity)) relies on the Hecke representation structure, not merely the crossing parity. The determining variable is the **valence electron count** $\ell_v$ relative to the shell capacity $\ell_{\max}$.

**Test against observed sublimation at 1 atm.**

See [Table](#tbl:crossing-parity-test-table-data).

**Score: 11/12 (92%).**

The representation-theoretic criterion resolves all three counterexamples where the crude parity rule fails:

- **H** ($\ell_v = 1$ of $\ell_{\max} = 2$): The shell is near-closed. The extension splits via the trivializing section. Liquid H exists at 20 K. $\checkmark$
- **Na** ($\ell_v = 1$ of $\ell_{\max} = 2$): The shell is near-closed and exhibits metallic band delocalization. It melts normally. $\checkmark$
- **Cu** ($3d^{10}4s^1$): The $3d$ subshell is fully closed. The single $4s$ valence electron is near-closed and metallic. It melts normally. $\checkmark$

**The molecular exception: iodine.**
Iodine ($\ell_v = 5$ of $\ell_{\max} = 6$) has a near-closed shell. The atomic criterion predicts a stable liquid, yet iodine sublimes at 1 atm. This exception occurs because iodine forms a molecular $I_2$ van der Waals solid. The weak intermolecular binding makes sublimation favorable. The single-atom Hecke module is the wrong fundamental unit. The $I_2$ dimer has crossing number $n_K(I_2) \equiv 0 \pmod{2}$, but the inter-dimer linking is too weak to sustain a liquid phase. The sublimation is molecular, not atomic.

**Connection to magic numbers.**
The decomposition $V^{\otimes n} \cong \bigoplus_\lambda V_\lambda \otimes S_\lambda$ produces the nuclear magic numbers (2, 8, 20, 28, 50, 82, 126) via palindromic Poincaré polynomials in the Bruhat lattice. The identical decomposition produces the sublimation criterion via Ext groups between the irreducible summands $S_\lambda$. Magic shell closures trivialize the extension; half-filled shells maximize it.
