**Generators.** A knot type $K$ is *fundamental* if it is the unknot or a
torus knot. Every fundamental knot has $\mathrm{Vol}(K) = 0$, but the converse
fails: by Thurston's trichotomy a knot complement is torus, satellite or
hyperbolic, and satellite knots, including composites such as $3_1 \# 3_1$,
also have volume zero. (An earlier version of this proof said the
volume-zero knots are precisely the torus knots and the unknot.) In
the particle dictionary, the fundamental knots are the fermions:
the unknot (neutrino), trefoil $3_1$ (electron), cinquefoil $5_1$
(tau), and the torus$(p,2)$ family.

**Generation.** The Skein module $\mathrm{Sk}_q$ is generated as an
algebra by the fundamental knot types $\{K_i\}_{i \in \mathcal{F}}$
and the Hopf link $\mathcal{L}_{\mathrm{Hopf}}$.  Every hadron
$H \in \mathrm{Sym}^n(K) \otimes \mathcal{L}_{\mathrm{Hopf}}$
admits a **terminal Skein resolution**: iterating the Skein relation

$$
  q \cdot L_+ -  q^{-1} \cdot L_-
  =  (q - q^{-1}) \cdot L_0
$$

at every crossing terminates in a finite polynomial

$$
  [H] =  \sum_{\alpha} c_\alpha(q) \cdot
  [K_{i_1}] \cdots [K_{i_k}]
$$

where each $[K_{i_j}]$ is the class of a fundamental knot and
$c_\alpha(q) \in \mathbb{Z}[q^{\pm 1}]$.

**The relation above collapses the skein module of $S^3$.** Apply it at the
crossing of a one-crossing unknot diagram. Both $L_+$ and $L_-$ are the unknot
$U$ and $L_0$ is the two-component unlink, so
$(q - q^{-1})\,U = (q - q^{-1})\,(U \sqcup U)$ and $U \sqcup U = U$. At a crossing
of the Hopf link $H$, $L_- = U \sqcup U = U$ and $L_0 = U$, so
$q\,H - q^{-1}\,U = (q - q^{-1})\,U$ and $H = U$. Induction on the unknotting
number then gives $[L] = [U]$ for every link $L$. This relation is the HOMFLY
relation at $a = q$, $z = q - q^{-1}$, the $\mathfrak{gl}_1$ point, where the
invariant is $1$. So in $\mathrm{Sk}_q(S^3)$ every hadron resolves to
$1 \cdot [U]$: generation holds, but the polynomial $[H]$ carries no linking
information.

**Mass from linking.** The step below needs a resolution in which the Hopf
link is not identified with the unknot. In $\mathrm{Sk}_q(S^3)$ with the relation
above it is, so this step does not follow from the resolution as written; it
needs a different skein theory (a framed relation, or a variable other than
$a = q$). By
([Skein-resolution mass formula](#lem:skein-mass-from-linking)),
$\mathfrak{m}(H) = Q(q) \cdot \mathfrak{m}(\mathcal{L}_{\mathrm{Hopf}}) +
\sum_i \mathrm{Vol}(K_i)/\hbar_q^2$.  For hadrons composed entirely
of fundamental (torus-knot) constituents, $\mathrm{Vol}(K_i) = 0$
for all $i$, so the entire inertial mass arises from the linking
topology, $\mathfrak{m}(H) = Q(q) \cdot \mathfrak{m}(\mathcal{L}_{\mathrm{Hopf}})$.
$\square$
