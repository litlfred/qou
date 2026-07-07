<!-- FILE_START: vortex-spectrum-intro.md -->
The $q$-deformation of brane hydrodynamics forces vortex
circulation onto a discrete ladder and pins helicity to a
topological invariant. We collect the modes that the braided
monoidal structure produces and the conservation law it enforces.

We open with Remark: Vortex intensity modes: from classical fluids to $q$-deformation, which contrasts four classical mechanisms
for discrete vortex spectra with the $q$-deformed mechanism and
fixes the comparison. We then prove Proposition: Discrete vortex mode spectrum — the eigenvalues of the $q$-Laplacian on a
filament are $[k]_q^2 \cdot \hbar_q / L_q^2$ — and interpret
the resulting levels in Remark: Vortex intensity levels as fluid-dynamical orbitals. The central structural result
is Proposition: Categorical helicity conservation: helicity is a
topological invariant of the braided monoidal structure, with
Remark: Helicity as quantised topological charge reading the
invariant as a charge. We close with Remark: Vortex reconnection as divisor surgery, the birational picture of filament
recombination that the next section, **Turbulence and acoustics**,
consumes when it builds the $q$-deformed energy cascade on tangles
of these filaments.

_(draft.)_
<!-- FILE_END: vortex-spectrum-intro.md -->

<!-- FILE_START: vortex-intensity-modes.md -->
The [substrate parameter](#def:substrate-parameter) $q$ imposes
algebraic discreteness on vortex circulation that classical
Navier--Stokes cannot provide.  Four classical mechanisms exhibit
discrete modes but continuous intensity; the $q$-deformation
closes this gap.

**1. Kelvin waves on vortex filaments.**
A classical vortex filament supports standing-wave perturbations
(Kelvin modes) with discrete wavelengths $\lambda_k = L/k$,
$k = 1, 2, 3, \ldots$, where $L$ is the filament length.  The
dispersion relation is

$$
  \omega_k =  \frac{\Gamma}{4\pi a^2}k^2
  \bigl(\ln(L/a) - \text{const}\bigr),
$$

with vortex core radius $a$ and circulation $\Gamma$.  These
modes are discrete in wave number but the circulation $\Gamma$
itself is a free continuous parameter.  In the $q$-deformed
setting the filament lives in the 1-jet bundle $J^1 \mathcal{S}_n$,
and the $q$-Laplacian $\Delta_q$ replaces the classical
Laplacian.  Its eigenvalues are the $q$-integers
$[k]_q = (q^k - q^{-k})/(q - q^{-1})$, producing a spectrum
that is discrete in **both** wave number and intensity:

$$
  \omega_k^{(q)} = 
  \frac{\Gamma_q}{4\pi a_q^2}[k]_q^2
  \bigl(\ln_q(L/a_q) - c_q\bigr).
$$

As $q \to 1$ the $q$-integers collapse to ordinary integers and
the classical Kelvin spectrum is recovered.

**2. Superfluid vortex quantisation.**
In superfluid helium and Bose--Einstein condensates, the
macroscopic wave function $\psi = |\psi|e^{i\varTheta}$
forces circulation to be quantised:
$\Gamma_n = n \cdot h/m$, $n \in \mathbb{Z}$.  This is a
topological constraint — the phase must be single-valued around
any closed loop.  The QOU analogue is the holonomy of the
$\mathrm{SU}(2)$ connection around a vortex filament.  The
[primordial vortex](#rem:primordial-vortex) carries topological
charge because the $\mathrm{SU}(2)$ holonomy is quantised by
the representation theory of $\mathrm{SU}_q(2)$: the
Casimir eigenvalue $[j]_q[j+1]_q$ with $j \in \frac{1}{2}\mathbb{Z}_{\geq 0}$
replaces the continuous $\Gamma$.

**3. Vortex breakdown states.**
In confined swirling flows (pipe flow, combustion chambers),
vortices transition between topologically distinct stable
configurations — columnar, bubble breakdown, spiral breakdown —
separated by finite energy barriers.  These are discrete
**states**, not modes.  In the brane fluid, the analogous
transitions are the [geodesic vortex](#rem:geodesic-vortices)
fixed points of the $q$-deformed energy functional: each fixed
point is a stable vortex configuration, and passage between
them requires crossing a barrier set by $q$.

**4. Stability eigenvalues.**
The Lamb--Oseen vortex and other smooth classical vortex
profiles have discrete eigenvalues in their linear stability
spectrum.  Perturbations grow or decay at specific discrete
rates.  For the $q$-deformed vortex, these eigenvalues are
governed by the weight-space decomposition of the adjoint
bundle: the **longitudinal modes** (Cartan subalgebra) give
the stable eigenvalues (laminar, decaying), while the
**ladder modes** ($E_\pm$) give the unstable eigenvalues
(entangling, growing).  The separation between these two
families is not a coincidence of initial conditions but an
algebraic consequence of the $\mathrm{SU}_q(2)$ structure.

The correspondence is summarised in
[Table: Classical fluid concepts and their $q$-deformed analogues](#tbl:vortex-intensity-modes-table-data).

<!-- FILE_END: vortex-intensity-modes.md -->

<!-- FILE_START: discrete-vortex-spectrum.md -->
Let $\varrho$ be a stable vortex filament of length $L$ in the
brane fluid with [substrate parameter](#def:substrate-parameter)
$q > 1$, and let $\Delta_q$ be the $q$-Laplacian acting on
sections of the normal bundle $N_\varrho$.

Then:

1. The eigenvalues of $\Delta_q$ restricted to $\varrho$ form a
   discrete spectrum $\{\lambda_k^{(q)}\}_{k \geq 1}$ with

   $$
     \lambda_k^{(q)} = 
     [k]_q^2 \cdot \frac{\hbar_q}{L_q^2},
   $$

   where $[k]_q = (q^k - q^{-k})/(q - q^{-1})$ is the
   $q$-integer and $L_q$ is the $q$-deformed filament length.

2. The **intensity levels** of the vortex are indexed by the
   spin label $j \in \frac{1}{2}\mathbb{Z}_{\geq 0}$ of the
   $\mathrm{SU}_q(2)$ representation carried by the holonomy
   around $\varrho$.  The vortex energy at level $j$ is

   $$
     E_j^{(q)} = 
     \frac{\hbar_q}{2I_q}[j]_q[j+1]_q,
   $$

   where $I_q$ is the $q$-deformed moment of inertia of the
   filament cross-section.

3. Transitions between intensity levels $j \to j'$ are
   mediated by the ladder modes $E_\pm$ of the weight-space
   decomposition, with selection rule $|j - j'| = 1$.  The
   energy released or absorbed is

   $$
     \Delta E_{j \to j'} = 
     \frac{\hbar_q}{2I_q}
     \bigl([j']_q[j'+1]_q - [j]_q[j+1]_q\bigr).
   $$

4. In the classical limit $q \to 1$:
   - $[k]_q \to k$ and the Kelvin-wave spectrum is recovered.
   - $[j]_q[j+1]_q \to j(j+1)$ and the energy levels reduce to
     the rigid-rotor spectrum of angular momentum theory.
   - The selection rule $\Delta j = \pm 1$ reduces to the
     standard dipole selection rule.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: discrete-vortex-spectrum.md -->

<!-- FILE_START: discrete-vortex-spectrum-novelty.md -->
While the spectral theory of rigid rotors and Kelvin waves is standard, the mathematical novelty is formally unifying these classical phenomena as evaluations of representations of the quantum group $\mathrm{SU}_q(2)$ over the $q$-Laplacian. This specific reframing rigorously anchors vortex intensity levels and selection rules to the discrete topology of the $q$-integer spectrum, replacing heuristic classical angular momentum derivations with exact categorical constraints.
<!-- FILE_END: discrete-vortex-spectrum-novelty.md -->

<!-- FILE_START: discrete-vortex-physical.md -->
The [discrete vortex spectrum](#prop:discrete-vortex-spectrum)
has a direct physical reading: a stable vortex in the brane fluid
does not smoothly increase its circulation but jumps between
discrete intensity states.  The transitions are governed by the
same $\mathrm{SU}_q(2)$ ladder operators that produce fermionic
matter in the weight-space decomposition.  The vortex intensity
levels $E_j^{(q)}$ are the fluid-dynamical analogue of atomic
energy levels.
<!-- FILE_END: discrete-vortex-physical.md -->

<!-- FILE_START: helicity-conservation.md -->
Let $(\mathbf{C}, \varTheta, G, \mathcal{S})$ be a
[QOU](#def:quantum-observable-universe) with brane fluid velocity
$v = \nabla_A S$ and vorticity
$\omega = \mathrm{curl}_Av = \nabla_A \times v$.  Define the
**categorical helicity** of a vortex configuration
$\{\varrho_1, \ldots, \varrho_n\}$ as

$$
  \mathcal{H}_q
  = 
  \sum_{i} \oint_{\varrho_i}
  v \cdot \omegads
  + 
  2\sum_{i < j}
  \mathrm{lk}_q(\varrho_i, \varrho_j)
  \Gamma_i^{(q)}\Gamma_j^{(q)},
$$

where $\mathrm{lk}_q(\varrho_i, \varrho_j)$ is the $q$-deformed
linking number and
$\Gamma_i^{(q)} = [j_i]_q[j_i + 1]_q$ is the quantised
circulation of filament $\varrho_i$ at intensity level $j_i$.
Then:

1. **Conservation.**  Under the
   [quantum Euler equation](#rem:madelung-fluid),
   $\mathcal{H}_q$ is conserved:
   $d\mathcal{H}_q/dt = 0$.

2. **Decomposition.**  The categorical helicity splits into three
   topological invariants:

   $$
     \mathcal{H}_q
     = 
     \underbrace{\sum_i \mathrm{Wr}_q(\varrho_i)
       (\Gamma_i^{(q)})^2}_{\text{writhe}}
     + 
     \underbrace{\sum_i \mathrm{Tw}_q(\varrho_i)
       (\Gamma_i^{(q)})^2}_{\text{twist}}
     + 
     \underbrace{2\sum_{i<j}
       \mathrm{lk}_q(\varrho_i,\varrho_j)
       \Gamma_i^{(q)}\Gamma_j^{(q)}}_{\text{linking}},
   $$

   where $\mathrm{Wr}_q$ and $\mathrm{Tw}_q$ are the $q$-deformed
   writhe and twist satisfying the Călugăreanu--White--Fuller
   relation $\mathrm{Wr}_q + \mathrm{Tw}_q = \mathrm{Lk}_q$
   (self-linking).

3. **Jones polynomial refinement.**  Classical helicity assigns the
   same value to the unknot and the trefoil (both can have
   $\mathcal{H} = 0$).  The Jones polynomial
   $J_L(q) = \mathrm{tr}_M(\rho(\beta_L))$, computed as the
   [Markov trace](#thm:jones-markov-trace) on the Iwahori--Hecke algebra,
   is a **finer invariant** that separates these cases.  In the
   brane fluid,

   $$
     J_L(q) =  \exp\!\Bigl(
       \sum_{n=1}^{\infty}
       \frac{1}{n}
       \mathrm{tr}\bigl((\check{R})^n\bigr)
       \cdot (q - q^{-1})^n
     \Bigr),
   $$

   encoding the full topological content of the vortex tangle
   beyond what $\mathcal{H}_q$ alone captures.

4. **Classical limit.**  As $q \to 1$:
   $[j]_q[j+1]_q \to j(j+1)$,
   $\mathrm{lk}_q \to \mathrm{lk}$ (Gauss linking number), and
   $\mathcal{H}_q$ reduces to the classical Moffatt helicity
   $H = \int v \cdot \omegadV$.


**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: helicity-conservation.md -->

<!-- FILE_START: helicity-physical.md -->
The [conservation of categorical helicity](#prop:helicity-conservation)
is the fluid-dynamical expression of topological charge conservation.
A vortex configuration cannot change its total helicity by smooth
evolution — helicity redistributes between writhe, twist, and linking,
as observed in [trefoil chirality flips](#rem:trefoil-vortex-chirality-flip).

The quantisation of $\Gamma_i^{(q)} = [j_i]_q[j_i+1]_q$ ensures
that each term in the helicity sum is individually quantised.
Helicity takes values in a discrete lattice determined by the
$\mathrm{SU}_q(2)$ representation labels $\{j_i\}$, not only
a continuous conserved quantity.
<!-- FILE_END: helicity-physical.md -->

<!-- FILE_START: vortex-reconnection.md -->
When two vortex filaments approach, the divisor
$\{\psi = 0\}$ undergoes surgery.  The quantum pressure $Q_q$
regularises the classical reconnection singularity.  Let $D = \sum_i n_i\varrho_i$ be the effective
divisor encoding the vortex configuration, where $\varrho_i$ are
the filament components and $n_i \in \frac{1}{2}\mathbb{Z}$ are
their intensity levels.  Reconnection is a **birational
transformation** of the divisor:

$$
  D =  \cdots + \varrho_i + \varrho_j + \cdots
  \quad\xrightarrow{\text{surgery}}\quad
  D' =  \cdots + \varrho_i' + \varrho_j' + \cdots,
$$

where $\varrho_i'$ and $\varrho_j'$ are the reconnected filaments.
The surgery preserves:

- **Total circulation**: $\Gamma_i^{(q)} + \Gamma_j^{(q)} =
  \Gamma_{i'}^{(q)} + \Gamma_{j'}^{(q)}$ (conservation of
  $\mathrm{SU}_q(2)$ Casimir).
- **Categorical helicity**: $\mathcal{H}_q[D] = \mathcal{H}_q[D']$
  ([helicity conservation](#prop:helicity-conservation)), though
  writhe and twist may redistribute.
- **Total homology class**: $[D] = [D']$ in $H_1(\mathcal{S})$.

**Three types of divisor surgery.**

| Surgery type | Divisor operation | Physical process | Hecke eigenvalue |
|---|---|---|---|
| **Pass-through** | $\varrho_i, \varrho_j \to \varrho_i, \varrho_j$ | Elastic scattering | $q$ (symmetric) |
| **Strand exchange** | $\varrho_i, \varrho_j \to \varrho_i', \varrho_j'$ | Reconnection | $-q^{-1}$ (antisymmetric) |
| **Annihilation** | $\varrho_i, \bar\varrho_i \to E_0$ | Pair annihilation $\to$ exceptional divisor | — |

The first two types correspond to the two eigenvalues of the
[Hecke relation](#rem:braid-fluid) $(T - q)(T + q^{-1}) = 0$,
confirming the [braid--fluid correspondence](#rem:braid-fluid).
The third type — annihilation — occurs when a filament meets its
orientation-reversed partner $\bar\varrho_i$.  The pair collapses
to an exceptional divisor $E_0 \cong \mathbb{CP}^1$, releasing
energy $2\mathcal{E}_q[\varrho_i]$ as radiation (Kelvin waves
propagating along neighbouring filaments).

**Blowup and pair creation.**
The reverse process — **blowup** of an exceptional divisor — is
pair creation.  A sufficiently energetic Kelvin wave on a filament
$\varrho_k$ concentrates energy at a point; when the local energy
density exceeds $2\mathcal{E}_q[\varrho_{\min}]$ (twice the
[geodesic vortex](#rem:geodesic-vortices) energy of the
fundamental mode), the exceptional divisor inflates into a
filament--anti-filament pair:

$$
  E_0  \to  \varrho_{\mathrm{new}} + \bar\varrho_{\mathrm{new}},
$$

with the new filaments inheriting the minimum intensity level
$j = \frac{1}{2}$.  This is the fluid-dynamical realisation of
pair production: a photon (Kelvin wave) creates an
electron--positron pair (vortex--antivortex pair).

**Selection rules.**
Not all reconnections are allowed.  The
$\mathrm{SU}_q(2)$ representation theory imposes **fusion rules**
on divisor surgery: the reconnection
$\varrho_i + \varrho_j \to \varrho_{i'} + \varrho_{j'}$ is
permitted only if the Clebsch--Gordan decomposition

$$
  V_{j_i} \otimes V_{j_j}
  = 
  \bigoplus_{J = |j_i - j_j|}^{j_i + j_j} V_J
$$

contains the representation $V_{j_{i'}} \otimes V_{j_{j'}}$
as a summand.  This connects vortex reconnection to the
Clebsch--Gordan coefficients of the
quantum group.

**Connection to chirality.**
The [trefoil chirality flip](#rem:trefoil-vortex-chirality-flip)
identified three routes for chirality reversal.  In the divisor
language:

1. **Passage through exceptional divisor**: the vortex momentarily
   collapses to $E_0$ and re-inflates with reversed orientation —
   a pair annihilation followed by pair creation with opposite
   chirality.
2. **Complex substrate rotation**: the divisor rotates through a
   path in the complexified state bundle that is homotopically
   non-trivial — no surgery needed, but the ambient space must
   be complexified.
3. **Reidemeister reconnection**: a sequence of strand exchanges
   (Reidemeister moves) that changes the knot type — this is a
   shell transition, not a particle-type change.
<!-- FILE_END: vortex-reconnection.md -->

