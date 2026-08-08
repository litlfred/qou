Let $R$ be a commutative ring and $q \in R^{\times}$ an invertible element with a chosen square root $q^{1/2}$. The Markov trace $\mathrm{tr}_M$ on the Iwahori-Hecke algebra $H_n(R, q)$ is the unique linear functional satisfying:

1. **Normalisation:** $\mathrm{tr}_M(1) = 1$.
2. **Cyclicity:** $\mathrm{tr}_M(xy) = \mathrm{tr}_M(yx)$ for all $x, y$.
3. **Stabilisation by $\sigma_n$:** $\mathrm{tr}_M(x \sigma_n) = z \cdot \mathrm{tr}_M(x)$ for $x \in H_n(R, q)$, where $z = 1/(q^{1/2} + q^{-1/2})$ is the Markov-trace loop value.

Stabilisation by $\sigma_n^{-1}$ — often listed as a fourth axiom — is not an independent condition. Substituting the Hecke quadratic relation $\sigma_n^{-1} = \sigma_n - (q - q^{-1})$ into axiom 3 and using linearity of the trace (with $x \cdot 1 = x$) forces
$$
  \mathrm{tr}_M(x \sigma_n^{-1}) \;=\; z_{-} \cdot \mathrm{tr}_M(x),
  \qquad
  z_{-} \;:=\; z - (q - q^{-1}),
$$
so the negative-crossing loop value $z_{-}$ differs from $z$ whenever $q \neq \pm 1$. No choice of trace parameter makes the two stabilisations scale by mutually inverse factors either: $z \cdot z_{-} = 1$ has the sole solutions $z = q$ and $z = -q^{-1}$, the one-dimensional characters of $H_n(R, q)$, both of which are degenerate. Link invariance of the closure invariant is instead restored by the writhe prefactor outside the trace ([Markov trace](#thm:jones-markov-trace)).

Each of the three consequences above — the derivation of $z_{-} = z - (q - q^{-1})$, the root pair $z \in \{q,\, -q^{-1}\}$ of $z \cdot z_{-} = 1$, and the $z^k$ factor recorded below — follows from axiom 3 for an *arbitrary* stabilisation parameter. None of them uses the particular value of $z$ stipulated in axiom 3: the first substitutes the Hecke quadratic, the second depends only on $h = q - q^{-1}$, and the third only counts applications of axiom 3. Substituting a different member of the family changes the numerical values these expressions take, not the identities themselves.

Axioms 1–3 determine $\mathrm{tr}_M$ uniquely and non-degenerately, but they do so only once $z$ is fixed, and the value of $z$ above is a stipulation of this definition rather than a consequence of it: axioms 1–2 with an unspecified stabilisation parameter admit a one-parameter family (the Ocneanu family), and fixing $z = 1/(q^{1/2}+q^{-1/2})$ selects one member of it. That member is the **full-Hecke Ocneanu**, or **Wenzl $z$-**, trace, recorded as **convention C** in the [trace-convention registry](../../../docs/coordination/trace-convention-registry.md). Its three-row weight satisfies $y_{(1^3)}(q) \neq 0$ for $q \neq 1$, so its braid closure is **not** the Jones polynomial: that is a different member, convention D with $z = q^3/(q^2+1)$, carried by the two-dimensional $\mathrm{SU}_q(2)$ fibre and equivalently characterised by $y_{(1^3)} = 0$. The name *Jones–Markov trace*, used for the generic construction throughout, accordingly does not by itself fix $z$, and a statement about "the Markov trace" is comparable across sources only when it names its convention.

A likely provenance for the stipulated value, offered as an observation rather than an established finding: it is the Temperley–Lieb loop reciprocal read at the wrong exponent, hence applied to the wrong generator. With loop parameter $\delta = q^{1/2} + q^{-1/2}$ one has $1/(q^{1/2} + q^{-1/2}) = q^{1/2}/(q+1) = \delta^{-1}$. On the Temperley–Lieb side the stabilisation is carried by the *projection* $e_n$, not by the Hecke generator $\sigma_n$ of axiom 3, and its value is $\delta^{-1}$ or $\delta^{-2}$ according to the normalisation of $e_n$: for idempotent generators $e_n^2 = e_n$ it is $\mathrm{tr}(x e_n) = \delta^{-2}\,\mathrm{tr}(x)$ (Jones 1985, relation (V), where $t/(1+t)^2 = \delta^{-2}$), and rescaling to $e_n^2 = \delta e_n$ multiplies it by $\delta$ to give $\delta^{-1}$. Either way the parameter belongs to $e_n$; axiom 3 attaches it to $\sigma_n$. The shapes coincide, which is what makes the substitution easy to make and worth recording; that it is what in fact happened is not established here.

Because $\mathrm{tr}_M$ is compatible with the tower inclusions and evaluates disjoint generators by iterated application of axiom 3, the joint Markov trace of two braids acting on disjoint strand sets is strictly multiplicative:
$$
  \mathrm{tr}_M(K_1 \sqcup K_2) \;=\; \mathrm{tr}_M(K_1) \cdot \mathrm{tr}_M(K_2).
$$
Appending $k$ further strands, each stabilised by one positive crossing, multiplies this value by $z^k$ (one factor of $z$ per application of axiom 3). This derives the inter-knot decoupling theorem from primitive Markov axioms.
