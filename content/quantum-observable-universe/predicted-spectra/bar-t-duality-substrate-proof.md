*Proof.*
The substitution $q \mapsto q^{-1}$ in the Weierstrass coefficients
$p(q)$ and $r(q)$ (rational functions in $q$) yields rational
functions $p^*(q) = p(q^{-1})$ and $r^*(q) = r(q^{-1})$, defining
the curve $\mathcal{E}_{q^{-1}} : y^2 = x^3 + p^*(q)\,x + r^*(q)$.
The map $\iota_* \colon \mathcal{E}_q \to \mathcal{E}_{q^{-1}}$ is
defined by $(x, y, q) \mapsto (x, y, q^{-1})$ on the total space
$\mathcal{X} = \{(x, y, q) : y^2 = x^3 + p(q)x + r(q)\}$ and is an
involution since $\iota \circ \iota = \mathrm{id}$.

Claims (1)–(3) follow:

*(1)* $\Delta(\mathcal{E}_q) = -4p(q)^3 - 27r(q)^2 = 0$ at
$q = 1/\varphi^2$ implies $\Delta(\mathcal{E}_{1/q}) = -4p(1/q)^3
- 27r(1/q)^2 = 0$ at $1/q = 1/\varphi^2$, i.e. $q = \varphi^2$.

*(2)* $j(\mathcal{E}_q) = -1728 \cdot 64\,p(q)^3 / \Delta(q)$ pulls
back along $\iota$ to $j^*(q) := j(\mathcal{E}_{1/q}) = j(q^{-1})$,
a well-defined rational function of $q$.

*(3)* By [bar-self-dual confinement band](#prop:bar-self-dual-confinement-band)
the open interval $\mathcal{B} = (1/\varphi^2, \varphi^2)$ is the
maximal $\iota$-invariant open subset of $\mathbb{R}_{>0}$ avoiding
the golden nodes, hence the maximal locus on which both
$\mathcal{E}_q$ and $\mathcal{E}_{1/q}$ are simultaneously
non-degenerate. $\square$

**Refactoring corollary.**

Any statement of the form *"$\mathcal{E}_q$ has property $P$ for
$q \in I \subset \mathcal{B}$"* automatically yields its bar conjugate:
*"$\mathcal{E}_{1/q}$ has property $P$ for $q \in \iota(I)$."*  Thus
proofs about the elliptic family on the sub-classical wing
$(1/\varphi^2,\,1)$ extend to the super-classical wing $(1,\,\varphi^2)$
**without re-derivation** by composing with $\iota_*$.

This refactoring opportunity applies to every existing block whose
$q$-range is one-sided.  In particular, deconfinement statements
phrased as "$q < q_{\mathrm{gold}}$ $\Rightarrow$ deconfined" gain the bar
companion "$q > \varphi^2$ $\Rightarrow$ deconfined" with no additional proof
work — only an application of $\iota_*$ to the existing argument.

**Hecke-algebraic origin.**

Substrate-level bar T-duality is the geometric shadow of the
**Iwahori--Hecke bar involution** $\overline{\,\cdot\,} \colon H_n(q)
\to H_n(q^{-1})$ given on generators by $\sigma_i \mapsto
\sigma_i^{-1}$.  Since the Descartes elliptic curve $\mathcal{E}_q$
arises from the Markov trace
([Descartes elliptic curve](#prop:descartes-elliptic-curve)),
the Hecke bar involution descends to $\iota$ on the moduli
parameter — the two structures are not independent dualities but
two faces of the same algebraic involution.


Framing the standard $q \to q^{-1}$ involution as a Hecke-bar origin gives an algebraic geometry for the substrate that bridges T-duality with involution algebra and enforces algebraic parity on the substrate.
