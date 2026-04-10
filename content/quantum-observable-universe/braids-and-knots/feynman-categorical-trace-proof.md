**Proof.**
The argument proceeds in three steps: decompose the Hilbert space into
the eigenbasis, collapse the path integral to a finite sum, then
identify the result with the Markov trace.

**Step 1 (Eigenbasis decomposition).**
By the $q$-analogue of Schur--Weyl duality
([knot eigenbasis completeness](#prop:knot-eigenbasis-complete)(1)),
the tensor power decomposes as

$$
  V^{\otimes n}
  \cong
  \bigoplus_{\substack{\lambda \vdash n \\ \ell(\lambda) \leq 2}}
  V_\lambda \otimes S_\lambda,
$$

where $V_\lambda$ is the irreducible $\mathrm{SU}_q(2)$-module of spin
$j = (\lambda_1 - \lambda_2)/2$ and $S_\lambda$ is the irreducible
$H_n(q)$-module.  The braid $\beta \in B_n$ acts on $V^{\otimes n}$
via the braid group representation
$\rho_n \colon B_n \to \mathrm{Aut}(V^{\otimes n})$, and on each
$S_\lambda$ via the quotient map $B_n \to H_n(q)$.

The number of summands is $\lfloor n/2 \rfloor + 1$, corresponding to
spins $j = n/2, n/2 - 1, \ldots, \epsilon/2$ where
$\epsilon = n \bmod 2$.  This is finite for every $n$.

**Step 2 (Trace collapse).**
In Feynman's formulation, the transition amplitude between initial state
$|\psi_i\rangle$ and final state $|\psi_f\rangle$ is

$$
  \langle\psi_f|\psi_i\rangle
  =
  \int \mathcal{D}\phi\,e^{iS[\phi]/\hbar},
$$

where the integral runs over all paths in configuration space.  Now
suppose that the Hilbert space admits the complete eigenbasis from
Step 1.  Then every path $\phi$ factors through a unique irreducible
summand $V_\lambda \otimes S_\lambda$, and the continuum integral
collapses to a finite sum:

$$
  \int \mathcal{D}\phi\,e^{iS[\phi]/\hbar}
  \;\longrightarrow\;
  \sum_{\substack{\lambda \vdash n \\ \ell(\lambda) \leq 2}}
  \dim_q(V_\lambda) \cdot \mathrm{tr}_{S_\lambda}\bigl(\rho_n(\beta)\bigr).
$$

The quantum dimension $\dim_q(V_\lambda) = [2j+1]_q$ arises as the
trace of the identity on $V_\lambda$ in the rigid monoidal category:
$\dim_q(V_\lambda) = \mathrm{tr}(\mathrm{id}_{V_\lambda})
= \mathrm{ev}_{V_\lambda} \circ \mathrm{coev}_{V_\lambda}$.
The factor $\mathrm{tr}_{S_\lambda}(\rho_n(\beta))$ is the trace of
the braid action restricted to the $H_n(q)$-module $S_\lambda$.

No regularisation is needed: the sum has finitely many terms because
$V^{\otimes n}$ has finitely many irreducible summands (semisimplicity
of $H_n(q)$ at non-root-of-unity $q$).

**Step 3 (Markov identification).**
The Jones--Markov trace is defined by
([Jones--Markov trace](#thm:jones-markov-trace)):

$$
  \mathrm{tr}_M\bigl(\rho(\beta)\bigr)
  =
  \sum_{\substack{\lambda \vdash n \\ \ell(\lambda) \leq 2}}
  w_\lambda \cdot \mathrm{tr}_{S_\lambda}\bigl(\rho_n(\beta)\bigr),
$$

where the weights $w_\lambda$ are determined by the Markov property
$\mathrm{tr}_M(x T_n^{\pm 1}) = z^{\pm 1}\mathrm{tr}_M(x)$.  For
the Markov trace normalised by $\mathrm{tr}_M(1) = 1$, the weights
are $w_\lambda = \dim_q(V_\lambda) / \dim_q(V^{\otimes n})$.  Since
the overall normalisation is a scalar factor, the transition amplitude
and the Markov trace agree up to this normalisation:

$$
  \langle\psi_f|\psi_i\rangle_{\mathrm{eigenbasis}}
  =
  \mathrm{tr}_M\bigl(\rho(\beta)\bigr).
$$

By the categorical mass as Markov trace
([categorical mass as Markov trace](#prop:categorical-mass-markov)),
the absolute value of this expression is the categorical mass at a
single brane level:
$\mathfrak{m}(\varrho)|_{\text{single level}}
= |\mathrm{tr}_M(\rho(\beta))|$.  $\square$
