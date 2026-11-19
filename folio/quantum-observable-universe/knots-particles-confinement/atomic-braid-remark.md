The greedy insertion produces **ep pairs**: each electron sits immediately before its proton. The $\mathfrak{n}e = \mathrm{id}$ crossing means electrons pass through neutrons without generating Hecke generators.

The [atomic braid](#def:atomic-braid) carries the electron shell: the three electronic rows of
Table 1 — $\mathfrak{p}e$, $\mathfrak{n}e$, $ee$ — are part of the definition,
not an optional dressing. It is therefore a different object from the
electron-free nuclear core $\mathcal{B}_K \in H_{3A}(q)$, which places three
quark strands on each nucleon and carries no electron content
([notation register](../notation/notation-collisions.md)). The two are not two
conventions for one braid: $H_{A+Z}(q)$ cannot contain a word on $3A$ strands
at any $A$, since $A + Z < 3A$ whenever $Z \geq 1$. The symbol $\mathcal{A}$
denotes the atom defined here; an element of $H_{3A}(q)$ is written
$\mathcal{B}_K$.

For hydrogen the bare $[e, \mathfrak{p}]$ braid is LP-unstable, which is why the $\mathfrak{p}e$ crossing uses the $\mathcal{B}_3$-dressed eigenvalues.

**Tractability of the nuclear-ordering clause.** As written, clause 1 quantifies
over all $\binom{A}{Z}$ distinct nucleon arrangements, so it is exponential
in $A$ and is not evaluable for most of the range the mass table covers:
$\binom{12}{6} = 924$ for ${}^{12}\mathrm{C}$ but
$\binom{40}{20} \approx 1.4 \times 10^{11}$ for ${}^{40}\mathrm{Ca}$.
Clause 2 is already greedy and therefore polynomial; clause 1 is not, and
the asymmetry between them is not explained here. No polynomial rule is
substituted — that would be inventing mathematics the corpus has not
derived — so the definition stands as stated, with the cost of taking it
literally recorded. Any computation quoting a ground-state ordering for
$A \gtrsim 14$ is therefore using some unstated restriction of clause 1 and
should say which.
