Three mathematically distinct constructions share the name *Markov*
in this work.  They arise from the same combinatorial source (the
braid group $B_n$) but operate at different levels of the
Cat$\to$Alg$\to$Geom$\to$Arch$\to$Phys arc.

1. **Markov trace** (Jones--Wenzl).  The unique trace functional
   $\mathrm{tr}_M \colon H_n(R,q) \to R$ satisfying cyclicity, the
   Markov axiom $\mathrm{tr}_M^{(n)}(x\sigma_{n-1})
   = z \cdot \mathrm{tr}_M^{(n-1)}(x)$, and $\mathrm{tr}_M(1)=1$.
   This is the **algebraic** object that feeds the mass formula:
   $\mathfrak{m}(\varrho) = m_e \cdot
   |\mathrm{tr}_M(\rho(\beta))| \cdot \mathrm{Geom}_{\mathrm{full}}(K,q_0)$.
   Symbol: $\mathrm{tr}_M$.

2. **Markov chain** (stochastic dynamics).  The random walk on
   braid words induced by Hecke--Markov transition probabilities
   $p_{w \to w'} = \mathrm{tr}_M(\rho(w')) \cdot \overline{\mathrm{tr}_M(\rho(w'))} /
   \sum \mathrm{tr}_M(\rho(w'')) \cdot \overline{\mathrm{tr}_M(\rho(w''))}$
   (bar denotes the Hecke bar-involution $q \leftrightarrow q^{-1}$;
   at real $q_0$ the form reduces to $|\mathrm{tr}_M|^2$).
   This is the **stochastic**
   object that gives error bounds on the mass formula via
   Perron--Frobenius dominant-eigenvalue convergence.  See
   Chapter Stochastic Mechanics.

3. **Markov moves** (topological equivalence).  Stabilisation
   $\beta \mapsto \beta\sigma_n^{\pm 1}$ and conjugation
   $\beta \mapsto \gamma\beta\gamma^{-1}$ on $B_n$.  Two braids
   represent the same link iff they are related by a finite
   sequence of Markov moves (Markov's theorem, 1935).  This is
   the **topological** input that makes the Jones polynomial a
   knot invariant.

These three uses are separated: (1) is an algebraic
functional, (2) is a probability measure, (3) is an equivalence
relation.  Context always disambiguates, but when precision matters
we write $\mathrm{tr}_M$ for (1), "Markov chain" for (2), and
"Markov move" for (3).
