Closing a braid adds a coevaluation (cup) below each strand and an evaluation (cap) above it.
It adds no crossing. An observation in this framework inserts a crossing
([observation braid](#rem:observation-braid)), so closure is not an observation.

**Cups and caps as entangled pairs.** The coevaluation of $V$ is the maximally entangled vector
$\Omega$ of [the proposition](#prop:closure-unseen-subword), item 3. With the pivotal weight
$K = \mathrm{diag}(q, q^{-1})$ on $V = R^2$ it becomes the $q$-weighted vector $\Omega_K$, and
the quantum trace of a braid $\beta$ on $V^{\otimes n}$ is
$\langle \Omega_K, (\beta \otimes 1)\,\Omega_K \rangle$. Read: the cups prepare $n$ entangled
pairs, $\beta$ acts on one half of each pair, and the caps project back onto the pairs. Each
return arc is the entangled partner of its strand.

**Two steps.** The word *closure* covers two different maps.

1. *Annular closure* keeps the closure axis. It is the map $H_n(q) \to \mathrm{HH}_0(H_n(q))$
   of item 1 of [the proposition](#prop:closure-unseen-subword), and it keeps every character
   $\chi_\lambda$ separately.
2. *Forgetting the axis* sends each block to its quantum dimension. The result is the Markov
   trace at $z_D$ ([categorical trace](#rem:categorical-trace-is-the-markov-trace)), which
   averages the blocks.

**What an unseen intermediate is.** A process that emits $u$, runs $w$, and reabsorbs $u^{-1}$
has the same value as $w$ under every closure (item 2): $u$ passes round the return arc and
cancels. More generally, a subword is invisible to every closure exactly when removing it
changes the element by a commutator (item 1). This gives a precise meaning to an intermediate
that is produced and not seen, without a virtual particle.

**Fluid dynamics.** The [helicity](#prop:helicity-conservation) of a vortex tangle is a closure
invariant. Its classical counterpart is the asymptotic linking number, in which long orbit
segments are closed by short paths whose contribution vanishes in the limit
\cite{komendarczyk2008}; the closing arcs are again unseen.

Which physical object the closure axis is (a photon loop, a periodic direction, or nothing) is
an interpretation and is not derived here.
