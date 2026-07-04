The Euler characteristic is stable along the tower, but it aggregates Hodge-theoretic data we now want to expose. This section refines the count into Betti numbers, fixes a $q$-harmonic basis, and uses the curvature commutator to sort the basis into fermionic and bosonic sectors.

**Betti numbers of the brane tower** (rem) records the dimensions $b_k(A_n)$ that the Euler characteristic packages. **$q$-Harmonic basis of the brane tower** (rem) chooses representatives compatible with the substrate parameter, and **Weight-space decomposition of the harmonic basis** (rem) splits the basis by $\mathrm{SU}(2)$ weight. **Fermion--boson classification by commutator with curvature** (prop) is the structural result: the algebraic filter $[\text{--}, F]$ sorts the harmonic basis into commuting (bosonic) and anti-commuting (fermionic) parts, and the proof in the Lean file is a Frobenius-trace computation. **The algebraic filter** (rem) interprets the projector, and **Distributional connection at the limit** (rem) states the resulting connection in the form the next section requires.

The next section, *Descent*, takes the fermion--boson split and the eigenspace data and uses them to project the brane tower onto its physically realised stratum.

_(draft.)_
