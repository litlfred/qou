The full sublimation criterion
([shell-filling criterion](#prop:composite-crossing-parity))
uses the Hecke representation structure, not just crossing
parity.  The key variable is the **valence electron count**
$\ell_v$ relative to the shell capacity $\ell_{\max}$.

**Test against observed sublimation at 1 atm.**

See [Table](#tbl:crossing-parity-test-table-data).

**Score: 11/12 (92%).**

The full representation-theoretic criterion resolves all
three counterexamples from the crude parity rule:

- **H** ($\ell_v = 1$ of $\ell_{\max} = 2$): near-closed
  shell, extension splits via the trivializing section.
  Liquid H exists at 20 K.  $\checkmark$

- **Na** ($\ell_v = 1$ of $\ell_{\max} = 2$): near-closed
  shell, plus metallic band delocalization.  Melts normally.
  $\checkmark$

- **Cu** ($3d^{10}4s^1$): the $3d$ subshell is fully closed,
  and the single $4s$ valence electron is near-closed plus
  metallic.  Melts normally.  $\checkmark$

**The one remaining miss: iodine.**
Iodine ($\ell_v = 5$ of $\ell_{\max} = 6$) is classified
as "near-closed" by the criterion, predicting a stable
liquid.  Yet iodine sublimes at 1 atm.  The resolution may
lie in iodine's molecular structure: $I_2$ dimers form a
van der Waals solid, and the weak inter-molecular
(not inter-atomic) binding makes sublimation favorable.
The single-atom Hecke module is the wrong unit — the
$I_2$ dimer has crossing number $n_K(I_2) \equiv 0 \pmod{2}$
but the inter-dimer linking (van der Waals) is too weak
to sustain a liquid.  This is a **molecular** sublimation,
not an atomic one.

**Connection to magic numbers.**
The same decomposition $V^{\otimes n} \cong \bigoplus_\lambda
V_\lambda \otimes S_\lambda$ that produces the nuclear magic
numbers (2, 8, 20, 28, 50, 82, 126) via palindromic
Poincaré polynomials in the Bruhat lattice also produces
the sublimation criterion via Ext groups between the
irreducible summands $S_\lambda$.  Magic shell closures
trivialize the extension; half-filled shells maximize it.
