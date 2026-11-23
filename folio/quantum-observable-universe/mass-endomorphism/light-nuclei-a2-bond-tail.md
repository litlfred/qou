**Proposition.** *Let $K$ be a field with $2 \neq 0$, and let $z, h \in K$. Write
$\mathrm{tr}$ for the Markov trace on $H_4$ with parameter $z$ and $h = q - q^{-1}$, and use the
letters $S_i = \sigma_i$, $I_i = \sigma_i - h = \sigma_i^{-1}$ and $A_i = \sigma_i - h/2$. Let*

$$
V^3_k = (S_k I_{k+1})^3, \qquad
p = V^3_1\, S_1 A_1 A_2 S_1 S_1, \qquad
n = V^3_1\, A_1 A_1 I_2 S_1 S_1 .
$$

*Then*

$$
4\,\mathrm{tr}(p) = -\bigl(-h^{10}z + h^9z^2 - h^9 - 5h^8z + 5h^7z^2 - 5h^7 - 9h^6z + 9h^5z^2 - 9h^5 - 5h^4z + 4h^3z^2 - 5h^3 + h^2z - 6hz^2 + 2h - 4z\bigr),
$$

$$
4\,\mathrm{tr}(n) = -(h^2+4)\bigl(-h^8z + h^7z^2 - h^7 - 3h^6z + 3h^5z^2 - 3h^5 - 2h^4z + 2h^3z^2 - 2h^3 + h^2z - hz^2 + h - z\bigr),
$$

$$
4\bigl(\mathrm{tr}(p\,V^3_0) - \mathrm{tr}(p)\bigr) = h^4 (z^2 - hz - 1)(-h^7 + h^6z - 4h^5 + 3h^4z - 6h^3 + 2h^2z - 3h - 2z),
$$

$$
4\bigl(\mathrm{tr}(n\,V^3_0) - \mathrm{tr}(n)\bigr) = h^5 (h^2+1)(h^2+4)(hz - h^2 - 1)(z^2 - hz - 1).
$$

*In particular both bond terms vanish when $z^2 - hz - 1 = 0$, that is at $z = q$ and
$z = -q^{-1}$.*

**Setting.** In the $A = 2$ $\gamma\gamma$ chain the first nucleon's block factors out of the
trace (`towerTr_disjoint` in `prop:markov-trace-hecke-functional`), so the bond from nucleon $0$
into nucleon $1$ acts on a four-strand tail: the receiving block's word on $\sigma_1, \sigma_2$,
followed by $V^3_0 = (\sigma_0\sigma_1^{-1})^3$. The words $p$ and $n$ above are the production
proton and neutron blocks on that tail.

**Consequence.** At $h = 0$ both free traces equal $z$. Dividing the bond terms by the free
traces, the relative change starts at order $h^4$ for a bond into a proton, with coefficient
$(1 - z^2)/2$, and at order $h^5$ for a bond into a neutron, with coefficient $(1 - z^2)/z$.
At $z = 1/2$ these are $3/8$ and $3/2$. This step is elementary algebra on the identities and
is not part of the Lean statement.

**Lean.** The sibling file proves the four identities and the two vanishing statements over
any field with $2 \neq 0$. The trace is computed by a merging evaluator `ME`, proved equal to
the plain expansion (`ME_eq_P`) and to a sum of the word evaluator `trWord` over the
positive-word expansion of the letters (`tail_eq_trWord`); `trWord` equals every Markov trace
by `isMarkovTrace_eq_trWord`. The reduction in **Setting** is also proved (`a2_reduce`): for any
first nucleon $N_0 \in H_3$ the full chain `ggChain` and the free product `freeTail` have traces
$\mathrm{tr}(N_0)$ times the bonded and free tails, so `a2_bond_into_proton` and
`a2_bond_into_neutron` state the two identities on the full $A = 2$ words.

**The $h^2$ step.** The file also proves `towerTr_shift_commutator`: for every $Y$ on strands
$\geq 1$, $\mathrm{tr}\bigl(Y^{\uparrow}(\sigma_0\sigma_1 - \sigma_1\sigma_0)\bigr) = 0$, over any
commutative ring and for every $z$ and $h$. Since $\sigma_1$ is the shift of $\sigma_0$,
cyclicity and the Markov factorisation at the first strand reduce the two terms to
$\mathrm{tr}(\sigma_0)\,\mathrm{tr}(\sigma_0 Y)$ and $\mathrm{tr}(\sigma_0)\,\mathrm{tr}(Y\sigma_0)$,
which are equal. The $h^2$ part of $V^3 - 1$ is this commutator, so it never contributes to the
trace of a bond, whatever the receiving word.
