The route from the axioms to a number that can be compared with
experiment passes through a short sequence of steps, each of them a
standard construction applied to the structure above. They are stated
here in words; the mass-analysis chapter records each step with its
algorithm ([derivation chain](#prose:pre-archimedean-derivation-chain)).

1. **From processes to braids.** A configuration of strands followed
   through the internal time-flow traces out a braid, and composing
   processes composes braids. The braiding of the category therefore
   gives a representation of the braid group, and integrating it over
   surfaces lands in the Iwahori–Hecke algebra $H_n(q)$.

2. **From braids to knots.** Joining the ends of a braid closes it
   into a knot or link. A theorem of Jones and Ocneanu gives a unique
   normalised trace on $H_n(q)$ compatible with closing, the *Markov
   trace* $\mathrm{tr}_M$, and evaluated on a closed braid it is the
   Jones polynomial $J_K(q)$ ([Markov trace](#thm:jones-markov-trace)).
   Each knot thus receives a rational function of $q$.

3. **From one trace to finitely many pieces.** The algebra $H_n(q)$
   splits into matrix blocks indexed by the partitions $\lambda$ of
   $n$, exactly as $\mathbb{C}[S_n]$ does at $q = 1$. On each block
   the trace is an ordinary matrix trace, the character $\chi_\lambda$,
   so the Markov trace becomes a finite weighted sum
   $\mathrm{tr}_M = \sum_\lambda y_\lambda \chi_\lambda$ — the Fourier
   decomposition of the trace over the irreducible blocks
   ([Wedderburn decomposition](#prop:wedderburn-as-noncomm-fourier)).

4. **From many candidates to one element.** Which element of the
   algebra represents a given composite is not chosen by hand.
   Candidates are built by pair production from photons, and a
   semidefinite program over the Frobenius pairing selects among them;
   its dual variables record which blocks the selected state saturates
   ([confinement program](#prop:confinement-sdp)). Where this selection
   is complete and where it is still open is recorded composite by
   composite in the nuclear and mass chapters.

5. **From rational functions to numbers.** Everything up to this point
   is algebra in the variable $q$. The last step is the archimedean
   realisation: substitute the measured value $q_0$ and multiply by a
   single unit of scale ([archimedean functor](#def:archimedean-realization-functor)).

> **A worked miniature.** Write $h = q - q^{-1}$, so that the quadratic
> relation reads $\sigma_i^2 = h\sigma_i + 1$ and
> $\sigma_i^{-1} = \sigma_i - h$, and let $z = q^3/(q^2+1)$ be the Markov
> parameter. Take the three-strand word $V^3 = (\sigma_0\sigma_1^{-1})^3$,
> the core of the Borromean rings, and follow it along the route above.
>
> 1. *Braid to algebra.* Replacing each $\sigma_1^{-1}$ by $\sigma_1 - h$
>    and reducing with $\sigma_i^2 = h\sigma_i + 1$ leaves a combination of
>    the six basis elements $1, \sigma_0, \sigma_1, \sigma_0\sigma_1,
>    \sigma_1\sigma_0, \sigma_0\sigma_1\sigma_0$ of $H_3(q)$ with
>    coefficients in $\mathbb{Z}[q, q^{-1}]$.
> 2. *Trace.* The Markov trace sends these six elements to
>    $1, z, z, z^2, z^2, z(hz+1)$, and the sum collapses to
>    $$\mathrm{tr}_M(V^3) = \frac{4 + h^2 - 3h^4 - h^6}{h^2 + 4}.$$
> 3. *Blocks.* The same rational function is
>    $\sum_\lambda y_\lambda\chi_\lambda$ over
>    $\lambda = (3), (2,1), (1^3)$, with
>    $y_{(3)} = \frac{q^4+1}{(q^2+1)^2}$,
>    $y_{(2,1)} = \frac{q^2}{(q^2+1)^2}$ and $y_{(1^3)} = 0$. The sign
>    block carries no weight: this is the trace radical of $H_3(q)$
>    ([Gram degeneracy](#prop:gram-degeneracy-blocks-connes)) seen in one
>    line.
> 4. *Number.* Substituting $q_0$ gives $0.998562\ldots$. This is the
>    rational function through which the proton-to-electron ratio pins
>    $q_0$ ([which pin the numbers use](#rem:epistemic-status-of-calibrations)).
>
> The first three steps of the miniature are identities in $\mathbb{Q}(q)$ and involve no measurement.
> The figure-eight word $V^2$ gives $(h^4 + 3h^2 + 1)/(h^2+4)$ by the same
> route. Every value above is computed exactly by
> `computations/intro/intro_worked_miniature_h3.py`.

The order matters. The categorical steps fix *shapes* — which knots,
which blocks, which weights — without reference to any measurement;
the measured world enters only at step five, in the three numbers
described next.
