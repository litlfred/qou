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

3. **Jones polynomial refinement.** Classical helicity does not separate knot types. For a single thin tube of flux $\Gamma$ it equals $\Gamma^2(\mathrm{Wr} + \mathrm{Tw}) = \Gamma^2\,\mathrm{Lk}$, the flux squared times the framing number \cite{moffatt-ricca-helicity}. The value therefore depends on the framing of the tube, not on its knot type: it vanishes exactly for a zero-framed tube, and the unknot and the trefoil both admit zero-framed and non-zero-framed tubes. The Jones polynomial $J_L(q) = \mathrm{tr}_M(\rho(\beta_L))$, computed via the [Markov trace](#thm:jones-markov-trace) on the Iwahori--Hecke algebra, acts as a **finer invariant**. In the brane fluid, it evaluates to:

   $$
     J_L(q) =  \exp\!\Bigl(
       \sum_{n=1}^{\infty}
       \frac{1}{n}
       \mathrm{tr}\bigl((\check{R})^n\bigr)
       \cdot (q - q^{-1})^n
     \Bigr),
   $$

   capturing the full topological structure of the vortex tangle missed by $\mathcal{H}_q$.

   *Where the closure enters, and what is conserved.* $J_L$ is a value of the tangle's braid word
   $\beta$ only after the strands are closed: a cup below and a cap above each strand, the return
   arcs adding no crossing ([closure](#prop:closure-unseen-subword)). Closure is a trace, so it
   factors through the annular class of $\beta$ in
   $\mathrm{HH}_0 = H_n(q)/[H_n(q), H_n(q)]$, which keeps every sector character $\chi_\lambda$; the
   Markov trace then averages the sectors. Three statements follow, each proved in the Lean twin
   from the stated input.

   - *Isotopy.* A smooth ideal flow carries vortex lines with it \cite{moffatt1969}, so the closed
     vortex link at time $t$ is isotopic to the link at time $0$. By the Alexander and Markov
     theorems \cite{alexander1923,markov1936,birman1974} the two braid words are joined by
     conjugations, stabilisations $x \mapsto x\,\sigma_n^{\pm 1}$ and their inverses. Along such a
     path the Markov trace changes only by the recorded stabilisation factors, so the normalised
     value $J_L$ is conserved.
   - *Fixed axis.* If the tangle stays a closed braid on the same strands around a fixed axis, the
     path uses conjugations only. Then the whole annular class is conserved, and with it every
     sector character, which is finer than $J_L$. Under stabilisation the strand number changes and
     only the Markov-normalised value survives.
   - *Reconnection.* A reconnection replaces one crossing $\sigma$ by $\sigma^{-1}$ and breaks
     isotopy. By the skein relation $\sigma - \sigma^{-1} = q - q^{-1}$, every closure invariant
     jumps by exactly $q - q^{-1}$ times its value on the word with that crossing smoothed.

   The two inputs to the isotopy statement, frozen-in vortex lines and Markov's theorem, are cited
   and not proved here. The classical counterpart of closing the strands is the asymptotic linking
   number, where long orbit segments are closed by short paths whose contribution vanishes in the
   limit \cite{komendarczyk2008}.

4. **Classical limit.** As $q \to 1$, the representations collapse ($[j]_q[j+1]_q \to j(j+1)$), linking reduces to Gauss linking ($\mathrm{lk}_q \to \mathrm{lk}$), and $\mathcal{H}_q$ simplifies to classical Moffatt helicity $H = \int v \cdot \omega\,dV$.

**Archimedean specialisation.** What follows sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
