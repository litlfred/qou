**Remark (physical interpretation).**
The observable modular tensor category
$\mathbf{C}_{\mathrm{any}}(N)$ of
[def:observable-mtc](#def:observable-mtc) packages three pieces of
anyonic data that can be read off directly from its structure:

1.  **Anyonic objects.**  Each non-trivial simple
    $\mathbf{V}_i \in \mathbf{C}_{\mathrm{any}}(N)$ is an anyon:
    a topological excitation labelled by the truncated integrable
    highest weight $i \in \{0, 1, \ldots, N-2\}$.  These are the same
    filaments that appear as vortex moduli in
    [rem:berry-vortex-moduli](#rem:berry-vortex-moduli); at
    $q = \zeta_N$ the Berry phase around such a filament is a
    *rational* fraction of $2\pi$, selecting a finite set of
    allowed topological charges.

2.  **Fusion rules.**  Tensor decomposition in
    $\mathbf{C}_{\mathrm{any}}(N)$ takes the form

    $$
      \mathbf{V}_i  \otimes  \mathbf{V}_j
        =  \bigoplus_{k} N_{ij}^{\,k}\, \mathbf{V}_k,
    $$

    with non-negative integer multiplicities $N_{ij}^{\,k}$ determined
    by the Verlinde formula from the modular $S$-matrix [@mooreSeiberg1989].
    These are the combinatorial rules governing composite-particle
    formation from anyonic constituents.

3.  **Ribbon twist and fractional spin.**  Each simple carries a
    ribbon twist $\theta_{\mathbf{V}_i} \colon \mathbf{V}_i
    \xrightarrow{\sim} \mathbf{V}_i$ satisfying

    $$
      \theta_{\mathbf{V}_i}  =  e^{2\pi i s_i}\, \mathrm{id}_{\mathbf{V}_i},
    $$

    where $s_i \in \mathbb{Q}$ is the *fractional spin* of the anyon.
    For $N \geq 3$ and $i \neq 0$, $s_i$ is strictly outside
    $\frac{1}{2}\mathbb{Z}$; the topological excitation is neither
    bosonic nor fermionic.

**Non-commutative vs.\ commutative.**  At $q = \zeta_N$ these three
features coexist consistently because the braiding is non-symmetric
(see [prop:bn-mtc-action](#prop:bn-mtc-action)). In the commutative
limit of [def:commutative-qou](#def:commutative-qou) the braiding
trivialises, the MTC expands to the full symmetric classical
$\mathrm{Rep}(\mathrm{SU}(2))$, ribbon twists on simples reduce to
$\pm 1$, and fractional statistics are absent.  The anyonic regime
and the commutative regime are disjoint: the fifth-roots-of-unity
data that appear in both appear for different reasons ---
geometric branch points in the commutative limit, deformation
parameter in the MTC.
