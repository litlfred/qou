*The [chain form](#prop:canonical-closure-torus-chain) has an algebraic
consequence that is stronger than the topological one. Write the canonical
Hecke word as $\prod_i p_i(\sigma_i)$, one polynomial per generator in Coxeter
order -- the averaged letters sit inside the power of their own generator, so
this needs no branch to be chosen. Then the normalised Markov trace on
$H_{3A}$ is the product of two-strand traces,*

$$
  \mathrm{tr}_M\Bigl(\prod_i p_i(\sigma_i)\Bigr)
  \;=\;
  \prod_i \bigl[\,w_+\,p_i(q) + w_-\,p_i(-q^{-1})\,\bigr],
  \qquad
  w_+ = \frac{[3]_q}{[3]_q+1},\quad w_- = \frac{1}{[3]_q+1},
$$

*because a closed braid whose word is a product of sub-words on strand sets
overlapping in one strand is a connected sum, and the Markov trace -- like
every multiplicative link invariant -- is multiplicative under connected sum,
not only under the split union of
[the KS shortcut](#rem:ks-multiplicativity-via-markov). Each interface
generator carries the single letter $\sigma + d$, whose two-strand trace is*

$$
  w_+(q + d) + w_-(-q^{-1} + d) \;=\; z + d,
  \qquad z = \frac{q^3}{q^2+1},
$$

*so the free-minus-atom log-ratio is exactly a sum over the $A-1$ interfaces:*

$$
  L(Z,N) \;=\; \sum_{\text{interfaces}} -\log(z + d_i),
  \qquad
  L_{pp} = -\log z,\quad
  L_{nn} = -\log(z - h) = \log\bigl(q(q^2+1)\bigr),\quad
  L_{pn} = -\log(z + d_{pn}).
$$

## Measured

At 200 bits, with $q$ from the fifty-digit substrate value, the full
$H_{3A}$ Markov trace of the canonical word against the product of two-strand
factors: $^2$H ($n=6$) $2.3\times10^{-59}$, $^3$H and $^3$He ($n=9$)
$3.1\times10^{-59}$, $^4$He ($n=12$) $4.0\times10^{-59}$; the Jones
polynomial of the closure equals $\prod_i V(T(2,e_i))$ exactly on both
classical branches for $A \le 4$. The three constants $-\log(z+d)$ reproduce
the binding arc's bond constants -- measured there in $H_6$ -- to all sixty
digits.

## What it means for the binding gap

The [linear-chain closed form](#thm:markov-trace-factorization)
$B_{\mathrm{sym}} = a\,[(Z-1)L_{pp} + L_{pn} + (N-1)L_{nn}]$, which the proof
of that result took as its *named structural input*, is a
corollary of the topology: connected sum $\Rightarrow$ multiplicative trace
$\Rightarrow$ additive $L$. The canonical closure therefore carries **no
many-body binding at all** -- not by measurement, by theorem. The many-body
cumulants the binding arc found ($c_3 < 0$, $c_4 < 0$, $c_5 > 0$, the
order-six datum) belong to the *all-pairs* bond model, whose band-routed
bonds interleave generators across blocks and destroy the chain form. With
$\alpha = m_e/(q_0(q_0-1)) = 4.185981$ MeV the chain gives $^4$He
$8.6817$ MeV against $B_{\mathrm{AME}} = 28.2957$, namely $31\,\%$; the missing
$69\,\%$ is absent from the canonical closure because a connected sum has
nothing to put there. Any closure that carries genuinely many-body binding
must fail to be composite -- non-split, prime, with the kind of irreducibly
multi-component linking the Borromean rings have and this chain does not. That
is the precise form of "the missing binding is not in the bond graph", and it
says which topology the search has to move to.

The affine law also disposes of the obvious repair. Any modification acting as
an interface offset -- a convention change, a fractional twist insertion
$q^{2c(\lambda)/n}$ -- has bond constant $-\log(z+d)$ with no trace to run, so
invert it: closing $^4$He on the chain with a common offset needs
$-\log(z+d) = 2.253212$, i.e. $d = -0.507627 = -2.4281\,h$. The algebra's
letters supply $d \in \{0, -h/2, d_{pn}, -h\}$, so $d/h \in [-1, 0]$: the
required offset is $2.43\times$ more negative than the most negative letter
that exists. No interface offset can close the gap.

The quantity $L$ itself is a free-energy difference over the Markov state
sum; that it is the binding energy is a separate and open claim, recorded in
[the free-energy reading](#rem:bond-log-ratio-is-a-free-energy).

## The stated form assumes the grouped intra ordering; the conclusion does not

Writing the word as $\prod_i p_i(\sigma_i)$ — one polynomial per generator —
requires each generator's letters to be **contiguous**. That is a property of
how the word is assembled, not of the chain topology. The canonical atom
word is assembled that way (all of the $\sigma_0$ chain,
then all of the $\sigma_1$ chain), which is why the identity measures exact
above. In contrast, the alternating Borromean builder lays each nucleon's six
**confinement letters** down alternating, as the $(\sigma_0\sigma_1^{-1})^3$ its
own source comment always named — the Borromean braid $\beta_{\mathrm{Bor}}$,
identified against its closed form to $5\times10^{-60}$. Same letter
multiset, different order, and it does **not** satisfy the per-generator form:
that fails by $2.8\times$ at $A = 2$, rising to $13.3\times$ at $A = 4$.

*A distinction worth keeping.* Grouped and
alternating describe the arrangement of six letters **inside** the eleven-letter
intra block, not the block itself. That block is not $\beta_{\mathrm{Bor}}$
under either arrangement and cannot be: two of its eleven letters are averaged,
$\sigma - (h/2)\cdot 1$, which is outside the image of
$\rho : B_n \to H_n(q)$, so it is not a braid at all and has no single closure to
name. One proton: $1.145759692457300870$ grouped, $0.629328402202921918$
alternating, against $0.998562163836787266$ for the bare six-letter
$\beta_{\mathrm{Bor}}$ — three distinct objects.

**The factorisation survives this.** The load-bearing step is connected-sum
multiplicativity, which is blind to letter order inside a summand, and it is
measured to survive the reordering exactly:
$\mathrm{tr}_M(\text{chain}) = \prod_k \mathrm{tr}_M(\text{intra}_k)\prod_i(z+d_i)$.
So the interface factors, the three bond constants and $L$ itself are
**identical under both orderings** — to $\sim 10^{-60}$ at $A = 2, 3, 4$ — and
the "no many-body binding" conclusion holds for either word. What is
ordering-specific is the stronger per-generator statement.

The same caveat applies one level up, to the [chain
form](#prop:canonical-closure-torus-chain): "every generator occurs in exactly
one contiguous run", so that the closure is a linear connected sum of $(2,k)$
torus links, is again a property of the assembly. With the confinement core
alternating, a nucleon's letters no longer form two runs, so that reading of the
block lapses. It is tempting to go further and say the block therefore satisfies
this arc's own criterion for where many-body binding could live — "a closure
that fails to be composite, non-split, prime, with the kind of irreducibly
multi-component linking the Borromean rings have" — but that would be
unsupported twice over: the block is a weighted sum of branch closures rather
than one link, and containing $\beta_{\mathrm{Bor}}$ as a subword is not the
same as being prime. What is actually measured is only that
$L$ is unchanged to $\sim 10^{-60}$: the reordering happens **inside** each
nucleon, the nucleons remain strung on a chain, and no many-body binding
appears anywhere.

What *moves* is every
**absolute** trace: the intra factor falls by $3.8\times$ at $^2$H to
$14.3\times$ at $^4$He when the confinement core is relaid alternating,
carrying the difference-based
$B = Q_\beta\bigl(\mathrm{tr}_M(W_{\text{free}}) - \mathrm{tr}_M(W_{\text{atom}})\bigr)$
route with it by the same factor.

The split is proved. Given the
connected-sum input — $\mathrm{tr}_M(W_{\text{atom}}) = F \prod_i (z + d_i)$ and
$\mathrm{tr}_M(W_{\text{free}}) = F$ — the ratio is
$\prod_i (z+d_i)$ for **any** intra factor $F \neq 0$, so two orderings with
factors $F_1, F_2$ give the same ratio with *no hypothesis relating them*
, and hence the same $L$
. The invariance is
cancellation, not coincidence. The difference route instead satisfies
$F_1(1-P) = (F_1/F_2)\,F_2(1-P)$ and genuinely differs
whenever $F_1 \neq F_2$ and $P \neq 1$. And the two
confinement words are different objects: at $q = 1$, where both are elementary,
the per-generator product is $1/4$ and the Borromean closed form is $1$
, so the $82\,\%$ gap at $q_0$ is not a deformation
artefact. The connected-sum multiplicativity itself is taken as input
(classical, cited below), not proved here. The effect of the reordering on the
absolute traces, and which word is $\beta_{\mathrm{Bor}}$, are numerical
measurements.

## What is proved, what is checked, what is cited

The factor algebra is proved: the
affine law $\mathrm{tr}_2(\sigma + d) = z + d$ from the level-2 Wenzl weights;
the mirror factor $z - h = 1/(q(q^2+1))$ and
$\mathrm{tr}_2(\sigma)\,\mathrm{tr}_2(\sigma^{-1}) = 1/[2]_q^2$, hence
$L_{pp} + L_{nn} = 2\log(q + q^{-1})$; positivity of all three factors for
$q \ge 1$; and that $-\log$ of a product of positive factors is the sum of the
$-\log$s. The factorisation of the $H_{3A}$ trace is checked at $A \le 4$ and
rests on the chain form (verified through $A = 12$) plus the connected-sum
multiplicativity of the Markov trace, which is classical \cite{birman1974}
and is cited rather than proved here. Nothing here says which prime closure would carry
many-body binding, or that one exists in the framework.
