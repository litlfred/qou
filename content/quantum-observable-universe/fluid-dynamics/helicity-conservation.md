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
