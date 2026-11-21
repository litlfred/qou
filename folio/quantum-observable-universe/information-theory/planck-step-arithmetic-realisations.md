The Planck step $t_P(q) = q/(q-1)$ ([discrete Planck step](#rem:discrete-planck-step)) is a rational function of $q$. Both $t_P(q)$ and the iteration $f_q(z) = z^2 + c(q)$ realise over any field. One records the finite-field and $p$-adic incarnations of the Planck dynamics.

**Finite-field dynamics.**
Over $k = \mathbb{F}_\pp$ with $q \in \mathbb{F}_\pp^\times$, the iteration $f_q \colon \mathbb{F}_\pp \to \mathbb{F}_\pp$ acts on a finite set. Every orbit is eventually periodic. This orbit structure encodes the Planck dynamics of the finite-field QOU:

- **Orbit length** $|O_x|$ counts the Planck steps before state $x$ recurs. This provides the finite-field analogue of Poincaré recurrence time.
- **Fixed points** of $f_q$ satisfy $z^2 - z + c(q) = 0$. They exist in $\mathbb{F}_\pp$ if and only if $1 - 4c(q)$ is a quadratic residue modulo $\pp$.
- **Period-$n$ orbits** are roots of $f_q^{\circ n}(z) = z$ not fixed by any $f_q^{\circ d}$ for $d \mid n$. The Weil zeta function of the curve $w^2 = z^2 + c(q)$ over $\mathbb{F}_\pp$ governs their count.

The Julia set $J(f_q)$ over $\mathbb{C}$ complexifies this finite orbit structure. The boundary between escaping and bounded orbits provides the continuous analogue to partitioning $\mathbb{F}_\pp$ into short-period and long-period orbits.

**$p$-Adic Planck step.**
Over $\mathbb{Q}_\pp$, the substrate parameter $q$ carries a $\pp$-adic valuation. The Planck time $t_P = q/(q-1)$ has valuation $v_\pp(t_P) = v_\pp(q) - v_\pp(q-1)$. When $q \equiv 1 \pmod{\pp^n}$, $q$ approaches the classical limit in the $\pp$-adic topology. Here $v_\pp(q-1) \geq n$. The Planck time becomes $\pp$-adically large, dictating slow dynamics. When $v_\pp(q-1) = 0$, $q$ occupies the Big Bang regime. The Planck time reaches minimal valuation, dictating maximally fast dynamics.

The Witt vector lift ([Witt vector lift](#rem:witt-lift-qou)) promotes the $\mathbb{F}_\pp$ orbit structure to a $\mathbb{Z}_\pp$-lattice. The finite orbits of $f_q$ over $\mathbb{F}_\pp$ lift to Teichmüller representatives in $\mathbb{Z}_\pp$. The $\pp$-adic Planck step acts on these lifts via the Frobenius endomorphism. The passage $\mathbb{F}_\pp \to \mathbb{Q}_\pp \to \mathbb{C}$ forms the arithmetic analogue of cosmological progression, moving from the discrete Big Bang to the continuous classical limit.
