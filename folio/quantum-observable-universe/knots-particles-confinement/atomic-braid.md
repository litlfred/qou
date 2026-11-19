**Definition.**
*The **atomic braid** of a neutral atom $(Z, N)$ is the element of $H_{A+Z}(q)$ obtained by assembling $Z$ protons, $N$ neutrons, and $Z$ electrons into a single Hecke algebra with $A + Z$ strands, where $A = Z + N$. The crossing coefficients are:*

See [Table 1](#tbl:atomic-braid-table1-data).

*The **ground-state ordering** is determined by:*

1. *Nuclear ordering: minimize $\Phi_1$ over all permutations of $Z$ protons and $N$ neutrons.*
2. *Electron insertion: greedily insert each of $Z$ electrons at the position minimizing $\Phi_1$.*

**Combinatorial complexity of clause 1.** Clause 1 quantifies over all $\binom{A}{Z}$ distinct nucleon arrangements, so its full enumeration grows exponentially in $A$ ($\binom{12}{6} = 924$ for ${}^{12}\mathrm{C}$, whereas $\binom{40}{20} \approx 1.4 \times 10^{11}$ for ${}^{40}\mathrm{Ca}$). Clause 2 is greedy and therefore polynomial in $Z$, whereas clause 1 is not. No heuristic polynomial restriction is substituted into the definition itself; any computation evaluating a ground-state ordering for $A \gtrsim 14$ restricts the search space of clause 1 and specifies the chosen restriction explicitly.

*The greedy insertion produces **ep pairs**: each electron sits immediately before its proton. The $\mathfrak{n}e = \mathrm{id}$ crossing means electrons pass through neutrons without generating Hecke generators.*

*The atomic braid carries the electron shell: the three electronic rows of
Table 1 — $\mathfrak{p}e$, $\mathfrak{n}e$, $ee$ — are part of the definition,
not an optional dressing. It is therefore a different object from the
electron-free nuclear core $\mathcal{B}_K \in H_{3A}(q)$, which places three
quark strands on each nucleon and carries no electron content
([notation register](../notation/notation-collisions.md)). The two are not two
conventions for one braid: $H_{A+Z}(q)$ cannot contain a word on $3A$ strands
at any $A$, since $A + Z < 3A$ whenever $Z \geq 1$. The symbol $\mathcal{A}$
denotes the atom defined here; an element of $H_{3A}(q)$ is written
$\mathcal{B}_K$.*

*For hydrogen ($A = 1$): the bare $[e, \mathfrak{p}]$ braid is LP-unstable. The $\mathfrak{p}e$ crossing uses the $\mathcal{B}_3$-dressed eigenvalues $(q^5, -q^{-5})$ instead of the bare $(q^{-1}, -q)$.*
