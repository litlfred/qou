<!-- FILE_START: vortex-spectrum-intro.md -->
The $q$-deformation of brane hydrodynamics forces vortex circulation onto a discrete ladder and pins helicity to a topological invariant. We collect the modes produced by the braided monoidal structure and the conservation laws it enforces.

We open with Remark: Vortex intensity modes: from classical fluids to $q$-deformation, which contrasts four classical mechanisms for discrete vortex spectra with the $q$-deformed mechanism to anchor the comparison. We then prove Proposition: Discrete vortex mode spectrum — the eigenvalues of the $q$-Laplacian on a filament are $[k]_q^2 \cdot \hbar_q / L_q^2$ — and interpret the resulting levels in Remark: Vortex intensity levels as fluid-dynamical orbitals. The central structural result is Proposition: Categorical helicity conservation: helicity operates as a topological invariant of the braided monoidal structure. Remark: Helicity as quantised topological charge reads this invariant as a discrete charge. We close with Remark: Vortex reconnection as divisor surgery, establishing the birational picture of filament recombination. The subsequent section, **Turbulence and acoustics**, uses this to build the $q$-deformed energy cascade on tangles of these filaments.
<!-- FILE_END: vortex-spectrum-intro.md -->

<!-- FILE_START: vortex-intensity-modes.md -->
The [substrate parameter](#def:substrate-parameter) $q$ imposes an algebraic discreteness on vortex circulation absent in classical Navier--Stokes. Four classical mechanisms exhibit discrete modes but continuous intensity; the $q$-deformation closes this gap.

**1. Kelvin waves on vortex filaments.**
A classical vortex filament supports standing-wave perturbations (Kelvin modes) at discrete wavelengths $\lambda_k = L/k$, for integers $k \geq 1$ and filament length $L$. The dispersion relation reads

$$
  \omega_k =  \frac{\Gamma}{4\pi a^2}k^2
  \bigl(\ln(L/a) - \text{const}\bigr),
$$

with vortex core radius $a$ and circulation $\Gamma$. These modes are discrete in wave number, yet the circulation $\Gamma$ remains a free continuous parameter. Under $q$-deformation, the filament inhabits the 1-jet bundle $J^1 \mathcal{S}_n$, and the $q$-Laplacian $\Delta_q$ replaces the classical Laplacian. Its eigenvalues correspond to the $q$-integers $[k]_q = (q^k - q^{-k})/(q - q^{-1})$, yielding a spectrum discrete in **both** wave number and intensity:

$$
  \omega_k^{(q)} = 
  \frac{\Gamma_q}{4\pi a_q^2}[k]_q^2
  \bigl(\ln_q(L/a_q) - c_q\bigr).
$$

As $q \to 1$, the $q$-integers collapse to classical integers, recovering the standard Kelvin spectrum.

**2. Superfluid vortex quantisation.**
In superfluid helium and Bose--Einstein condensates, the macroscopic wave function $\psi = |\psi|e^{i\varTheta}$ forces circulation to quantise as $\Gamma_n = n \cdot h/m$ for $n \in \mathbb{Z}$. This constitutes a topological constraint: the phase must remain single-valued around any closed loop. The QOU analogue is the holonomy of the $\mathrm{SU}(2)$ connection around a vortex filament. The [primordial vortex](#rem:primordial-vortex) carries topological charge because the representation theory of $\mathrm{SU}_q(2)$ quantises the $\mathrm{SU}(2)$ holonomy: the Casimir eigenvalue $[j]_q[j+1]_q$ with $j \in \frac{1}{2}\mathbb{Z}_{\geq 0}$ replaces the continuous $\Gamma$.

**3. Vortex breakdown states.**
In confined swirling flows (e.g., pipe flow), vortices transition between topologically distinct stable configurations — columnar, bubble breakdown, spiral breakdown — separated by finite energy barriers. These act as discrete **states**, not modes. In the brane fluid, the [geodesic vortex](#rem:geodesic-vortices) fixed points of the $q$-deformed energy functional supply the analogous transitions: each fixed point forms a stable vortex configuration, and transitioning between them requires crossing an energy barrier set by $q$.

**4. Stability eigenvalues.**
Smooth classical vortex profiles like the Lamb--Oseen vortex possess discrete eigenvalues in their linear stability spectrum. Perturbations grow or decay at specific discrete rates. For the $q$-deformed vortex, the weight-space decomposition of the adjoint bundle governs these eigenvalues. The **longitudinal modes** (Cartan subalgebra) define the stable, decaying eigenvalues, while the **ladder modes** ($E_\pm$) define the unstable, entangling eigenvalues. This separation is an algebraic consequence of the $\mathrm{SU}_q(2)$ structure, not an artefact of initial conditions.

The correspondence is mapped in [Table: Classical fluid concepts and their $q$-deformed analogues](#tbl:vortex-intensity-modes-table-data).
<!-- FILE_END: vortex-intensity-modes.md -->

<!-- FILE_START: discrete-vortex-spectrum.md -->
Let $\varrho$ denote a stable vortex filament of length $L$ in the brane fluid with [substrate parameter](#def:substrate-parameter) $q > 1$. Let $\Delta_q$ denote the $q$-Laplacian acting on sections of the normal bundle $N_\varrho$.

Then:

1. The eigenvalues of $\Delta_q$ restricted to $\varrho$ form a discrete spectrum $\{\lambda_k^{(q)}\}_{k \geq 1}$ scaling as

   $$
     \lambda_k^{(q)} = 
     [k]_q^2 \cdot \frac{\hbar_q}{L_q^2},
   $$

   where $[k]_q = (q^k - q^{-k})/(q - q^{-1})$ is the $q$-integer and $L_q$ is the $q$-deformed filament length.

2. The spin label $j \in \frac{1}{2}\mathbb{Z}_{\geq 0}$ of the $\mathrm{SU}_q(2)$ representation carried by the holonomy around $\varrho$ indexes the **intensity levels** of the vortex. The vortex energy at level $j$ equals

   $$
     E_j^{(q)} = 
     \frac{\hbar_q}{2I_q}[j]_q[j+1]_q,
   $$

   where $I_q$ represents the $q$-deformed moment of inertia of the filament cross-section.

3. The ladder modes $E_\pm$ of the weight-space decomposition mediate transitions between intensity levels $j \to j'$ under the strict selection rule $|j - j'| = 1$. The energy exchanged evaluates to

   $$
     \Delta E_{j \to j'} = 
     \frac{\hbar_q}{2I_q}
     \bigl([j']_q[j'+1]_q - [j]_q[j+1]_q\bigr).
   $$

4. In the classical limit $q \to 1$:
   - $[k]_q \to k$, returning the classical Kelvin-wave spectrum.
   - $[j]_q[j+1]_q \to j(j+1)$, reducing the energy levels to the rigid-rotor spectrum of standard angular momentum.
   - The selection rule $\Delta j = \pm 1$ reduces to the classical dipole selection rule.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: discrete-vortex-spectrum.md -->

<!-- FILE_START: discrete-vortex-spectrum-novelty.md -->
While the spectral theory of rigid rotors and Kelvin waves is established, the mathematical synthesis lies in uniting these classical phenomena as evaluations of $\mathrm{SU}_q(2)$ representations over the $q$-Laplacian. This reframing formally derives vortex intensity levels and selection rules directly from the discrete topology of the $q$-integer spectrum. It replaces heuristic angular momentum models with exact categorical constraints.
<!-- FILE_END: discrete-vortex-spectrum-novelty.md -->

<!-- FILE_START: discrete-vortex-physical.md -->
The [discrete vortex spectrum](#prop:discrete-vortex-spectrum) supports a direct physical interpretation. A stable vortex in the brane fluid cannot smoothly escalate its circulation; it must transition sharply between discrete intensity states. The $\mathrm{SU}_q(2)$ ladder operators that yield fermionic matter in the weight-space decomposition govern these transitions. The resulting vortex intensity levels $E_j^{(q)}$ serve as the fluid-dynamical analogue of atomic electron orbitals.
<!-- FILE_END: discrete-vortex-physical.md -->

<!-- FILE_START: helicity-conservation.md -->
Let $(\mathbf{C}, \varTheta, G, \mathcal{S})$ be a [QOU](#def:quantum-observable-universe) governed by brane fluid velocity $v = \nabla_A S$ and vorticity $\omega = \mathrm{curl}_Av = \nabla_A \times v$. Define the **categorical helicity** of a vortex configuration $\{\varrho_1, \ldots, \varrho_n\}$ as

$$
  \mathcal{H}_q
  = 
  \sum_{i} \oint_{\varrho_i}
  v \cdot \omega\,ds
  + 
  2\sum_{i < j}
  \mathrm{lk}_q(\varrho_i, \varrho_j)
  \Gamma_i^{(q)}\Gamma_j^{(q)},
$$

where $\mathrm{lk}_q(\varrho_i, \varrho_j)$ specifies the $q$-deformed linking number and $\Gamma_i^{(q)} = [j_i]_q[j_i + 1]_q$ indicates the quantised circulation of filament $\varrho_i$ at intensity level $j_i$.

Then:

1. **Conservation.** The [quantum Euler equation](#rem:madelung-fluid) strictly conserves $\mathcal{H}_q$: $d\mathcal{H}_q/dt = 0$.
2. **Decomposition.** The categorical helicity resolves into three distinct topological invariants:

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

   where $\mathrm{Wr}_q$ and $\mathrm{Tw}_q$ denote the $q$-deformed writhe and twist obeying the Călugăreanu--White--Fuller relation $\mathrm{Wr}_q + \mathrm{Tw}_q = \mathrm{Lk}_q$.

3. **Jones polynomial refinement.** Classical helicity $\mathcal{H}$ assigns zero to both the unknot and the trefoil, failing to separate them. The Jones polynomial $J_L(q) = \mathrm{tr}_M(\rho(\beta_L))$, computed via the [Markov trace](#thm:jones-markov-trace) on the Iwahori--Hecke algebra, acts as a **finer invariant**. In the brane fluid, it evaluates to:

   $$
     J_L(q) =  \exp\!\Bigl(
       \sum_{n=1}^{\infty}
       \frac{1}{n}
       \mathrm{tr}\bigl((\check{R})^n\bigr)
       \cdot (q - q^{-1})^n
     \Bigr),
   $$

   capturing the full topological structure of the vortex tangle missed by $\mathcal{H}_q$.

4. **Classical limit.** As $q \to 1$, the representations collapse ($[j]_q[j+1]_q \to j(j+1)$), linking reduces to Gauss linking ($\mathrm{lk}_q \to \mathrm{lk}$), and $\mathcal{H}_q$ simplifies to classical Moffatt helicity $H = \int v \cdot \omega\,dV$.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: helicity-conservation.md -->

<!-- FILE_START: helicity-physical.md -->
The [conservation of categorical helicity](#prop:helicity-conservation) physically manifests topological charge conservation within the fluid. Smooth evolution cannot alter the total helicity of a vortex configuration. It merely redistributes helicity among writhe, twist, and linking, as demonstrated by [trefoil chirality flips](#rem:trefoil-vortex-chirality-flip).

The exact quantisation of $\Gamma_i^{(q)} = [j_i]_q[j_i+1]_q$ mandates that each term in the helicity sum remains individually quantised. Consequently, helicity is restricted to a discrete lattice structured by the $\mathrm{SU}_q(2)$ representation labels $\{j_i\}$. It is not a continuous conserved variable.
<!-- FILE_END: helicity-physical.md -->

<!-- FILE_START: vortex-reconnection.md -->
When two vortex filaments approach, the divisor $\{\psi = 0\}$ undergoes surgery. The quantum pressure $Q_q$ acts to regularise the classical reconnection singularity. Let $D = \sum_i n_i\varrho_i$ denote the effective divisor framing the vortex configuration, where $\varrho_i$ represent the filament components and $n_i \in \frac{1}{2}\mathbb{Z}$ identify their intensity levels. Reconnection constitutes a **birational transformation** on the divisor:

$$
  D =  \cdots + \varrho_i + \varrho_j + \cdots
  \quad\xrightarrow{\text{surgery}}\quad
  D' =  \cdots + \varrho_i' + \varrho_j' + \cdots,
$$

where $\varrho_i'$ and $\varrho_j'$ designate the reconnected filaments. The surgery preserves three quantities:

- **Total circulation**: $\Gamma_i^{(q)} + \Gamma_j^{(q)} = \Gamma_{i'}^{(q)} + \Gamma_{j'}^{(q)}$ (enforcing conservation of the $\mathrm{SU}_q(2)$ Casimir).
- **Categorical helicity**: $\mathcal{H}_q[D] = \mathcal{H}_q[D']$ ([helicity conservation](#prop:helicity-conservation)), although writhe and twist are free to redistribute.
- **Total homology class**: $[D] = [D']$ evaluated in $H_1(\mathcal{S})$.

**Three types of divisor surgery.**

| Surgery type | Divisor operation | Physical process | Hecke eigenvalue |
|---|---|---|---|
| **Pass-through** | $\varrho_i, \varrho_j \to \varrho_i, \varrho_j$ | Elastic scattering | $q$ (symmetric) |
| **Strand exchange** | $\varrho_i, \varrho_j \to \varrho_i', \varrho_j'$ | Reconnection | $-q^{-1}$ (antisymmetric) |
| **Annihilation** | $\varrho_i, \bar\varrho_i \to E_0$ | Pair annihilation $\to$ exceptional divisor | — |

The first two classes map exactly to the two eigenvalues of the [Hecke relation](#rem:braid-fluid) $(T - q)(T + q^{-1}) = 0$, explicitly verifying the [braid--fluid correspondence](#rem:braid-fluid). The third class, annihilation, triggers when a filament encounters its orientation-reversed partner $\bar\varrho_i$. The pair physically collapses into an exceptional divisor $E_0 \cong \mathbb{CP}^1$, jettisoning energy $2\mathcal{E}_q[\varrho_i]$ as Kelvin-wave radiation along adjacent filaments.

**Blowup and pair creation.**
The inverse mechanism — the **blowup** of an exceptional divisor — constitutes pair creation. When an intense Kelvin wave on a filament $\varrho_k$ concentrates energy locally, and that density breaches $2\mathcal{E}_q[\varrho_{\min}]$ (twice the fundamental [geodesic vortex](#rem:geodesic-vortices) energy), the exceptional divisor forcefully inflates into a filament--anti-filament pair:

$$
  E_0  \to  \varrho_{\mathrm{new}} + \bar\varrho_{\mathrm{new}}.
$$

These newly spawned filaments adopt the absolute minimum intensity level $j = \frac{1}{2}$. This serves as the precise fluid-dynamical mapping of pair production: a photon (the Kelvin wave) generates an electron--positron pair (the vortex--antivortex pair).

**Selection rules.**
Reconnections are strictly filtered. The $\mathrm{SU}_q(2)$ representation theory issues rigid **fusion rules** controlling divisor surgery. The specific reconnection $\varrho_i + \varrho_j \to \varrho_{i'} + \varrho_{j'}$ proceeds if and only if the Clebsch--Gordan decomposition

$$
  V_{j_i} \otimes V_{j_j}
  = 
  \bigoplus_{J = |j_i - j_j|}^{j_i + j_j} V_J
$$

incorporates the target representation $V_{j_{i'}} \otimes V_{j_{j'}}$ as a viable summand. This binds vortex reconnection entirely to the structural Clebsch--Gordan coefficients of the quantum group.

**Connection to chirality.**
The [trefoil chirality flip](#rem:trefoil-vortex-chirality-flip) defines three avenues for chirality reversal. Translated to divisor terms:

1. **Passage through exceptional divisor**: The vortex collapses briefly to $E_0$ and re-inflates bearing reversed orientation. This is effectively pair annihilation paired directly with opposite-chirality pair creation.
2. **Complex substrate rotation**: The divisor sweeps through a homotopically non-trivial path mapped inside the complexified state bundle. No surgery occurs, but the ambient manifold must accommodate complexification.
3. **Reidemeister reconnection**: A structural series of strand exchanges (Reidemeister moves) explicitly alters the core knot type. This denotes a shell transition, not a modification of particle identity.
<!-- FILE_END: vortex-reconnection.md -->

