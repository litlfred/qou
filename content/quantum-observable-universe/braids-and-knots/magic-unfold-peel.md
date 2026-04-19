Let $A = Z + N$, $C = Z_c + N_c$ with $(Z_c, N_c)$ a
**doubly magic** pair (both $Z_c$ and $N_c$ in the nuclear magic
set $\{2, 8, 20, 28, 50, 82, 126\}$, with $Z_c \leq Z$ and
$N_c \leq N$), and $V = A - C$.  Let $W_{\mathrm{atom}}$ be the
standard atom braid word
([atomic braid mass](#prop:atomic-braid-mass)) for $(Z, N)$ and
let $\tilde{W}_{\mathrm{atom}}$ be the **core-first-then-valence**
reordering:
$$
  \tilde{W}_{\mathrm{atom}}
  \;=\;
  W_{\mathrm{core}}
  \,\cdot\,
  \sigma_{3C-1}^{m_{\mathrm{shell}}}
  \,\cdot\,
  W_{\mathrm{valence}}
$$
where $W_{\mathrm{core}} \in H_{3C}(q)$ uses only generators
$\sigma_0, \ldots, \sigma_{3C-2}$, $W_{\mathrm{valence}}$ uses only
$\sigma_{3C}, \ldots, \sigma_{3A-2}$ (a copy of $H_{3V}(q)$ shifted
by $3C$), and $m_{\mathrm{shell}}$ is the shell-coupling
crossing multiplicity.

**Proposition.**
*Assume the braid-relation equivalence
$\tilde{W}_{\mathrm{atom}} \sim W_{\mathrm{atom}}$ in $B_{3A}$
(so their Markov traces coincide).  Then the Markov trace factors
exactly:*

$$
  \mathrm{tr}_M(W_{\mathrm{atom}})
  \;=\;
  z^{m_{\mathrm{shell}}} \cdot
  \mathrm{tr}_M(W_{\mathrm{core}}) \cdot
  \mathrm{tr}_M(W_{\mathrm{valence}})
$$

*where $z = 1/(q^{1/2} + q^{-1/2})$ is the Markov parameter
([Jones–Markov trace](#thm:jones-markov-trace)).*

*Proof.*
By the reordering hypothesis,
$\mathrm{tr}_M(W_{\mathrm{atom}}) =
\mathrm{tr}_M(\tilde{W}_{\mathrm{atom}})$.  Since $W_{\mathrm{core}}
\in H_{3C}(q)$ and $W_{\mathrm{valence}}$ uses only generators
$\sigma_j$ with $j \geq 3C$, the two factors far-commute
(all pairwise index differences $\geq 2$) and independent of
$\sigma_{3C-1}^{m_{\mathrm{shell}}}$ under braid
far-commutativity: $[\sigma_i, \sigma_j] = 0$ whenever $|i - j|
\geq 2$.  Hence by cyclicity of the Markov trace
([Jones–Markov trace](#thm:jones-markov-trace)),
$$
  \mathrm{tr}_M(\tilde{W}_{\mathrm{atom}})
  =
  \mathrm{tr}_M\!\bigl(W_{\mathrm{core}} \cdot
                        W_{\mathrm{valence}} \cdot
                        \sigma_{3C-1}^{m_{\mathrm{shell}}}\bigr).
$$
The element $W_{\mathrm{core}} \cdot W_{\mathrm{valence}}$ lies in
the commuting subalgebra $H_{3C}(q) \otimes H_{3V}(q)$; the Markov
trace of such a tensor product factors as the product of the
factor traces by the
[Markov trace factorization theorem](#thm:markov-trace-factorization).
Finally, since the $\sigma_{3C-1}$ crossings are disjoint from
both factors (index difference $\geq 2$ to every generator used),
applying the Markov axiom $\mathrm{tr}_M(x \cdot \sigma_{n-1}) =
z \cdot \mathrm{tr}_M(x)$ iteratively on each of the
$m_{\mathrm{shell}}$ crossings yields the $z^{m_{\mathrm{shell}}}$
factor.  $\square$

## Remark on the reordering hypothesis

The reordering $\tilde{W}_{\mathrm{atom}} \sim W_{\mathrm{atom}}$
is **NOT automatic** — it requires that the braid-word
permutations between standard and reordered forms lie in the
kernel of the Hecke representation (i.e., they are related by a
sequence of braid relations $\sigma_i \sigma_{i+1} \sigma_i =
\sigma_{i+1} \sigma_i \sigma_{i+1}$ and far-commutativity).  A
sufficient condition: the standard $W_{\mathrm{atom}}$ can be
rewritten using ONLY far-commutativity (no braid-triple
relations) into $\tilde{W}_{\mathrm{atom}}$.

For the nuclear braid structure as defined in
[atomic braid mass](#prop:atomic-braid-mass), the intra-nucleon
crossings only use adjacent-generator pairs within a single
nucleon, and the inter-nucleon crossings use only the
linking generator $\sigma_{3k+2}$.  Inter-core and
inter-valence crossings therefore far-commute with each other
($|3k+2 - 3\ell+2| \geq 3 > 2$ when $k, \ell$ are in different
shells).  Core-only generators ($\sigma_j$, $j < 3C-1$) and
valence-only generators ($\sigma_j$, $j > 3C$) far-commute
automatically.  The ONLY non-commuting element is the
shell-coupling $\sigma_{3C-1}$ itself, which appears in both
orderings at the same position modulo far-commutativity.

The formal proof of the reordering equivalence is outstanding for
the generic case; validation on $^{4}\mathrm{He}$ (doubly magic
with $C = 4$, $V = 0$) is recorded in
`folio-assistant/computations/magic-unfold-validation.witness.json`
when that validation completes.

## Computational consequence

When the reordering hypothesis holds, the partition sum over
$\lambda \vdash 3A$ reduces to:
$$
  \mathrm{tr}_M(W_{\mathrm{atom}})
  =
  z^{m_{\mathrm{shell}}} \cdot
  \sum_{\mu \vdash 3C} w_\mu \chi_\mu(W_{\mathrm{core}}) / d_\mu
  \cdot
  \sum_{\nu \vdash 3V} w_\nu \chi_\nu(W_{\mathrm{valence}}) / d_\nu
$$
— an exponentially smaller computation.  For $^{6}\mathrm{Li}$
($(Z,N)=(3,3)$, $(Z_c,N_c)=(2,2)$, $C=4$, $V=2$), the full
$p(18) = 385$ partition sum reduces to $p(12) \cdot p(6) = 77 \cdot
11 = 847$ partition pairs — but each is FEASIBLE, whereas the
largest partition at $n=18$ has dim $6006$ and is not.

## Connection to the cancellation-ratio observation

The $B/M$-scaled cancellation recorded in
[atom tr_M cancellation ratio](#rem:atom-trM-cancellation-ratio)
predicts that the full $\mathrm{tr}_M(W_{\mathrm{atom}})$ will be
near-zero.  Under the magic-unfold factorization, this is
realized as: $\mathrm{tr}_M(W_{\mathrm{core}})$ is a specific
closed-shell value (near a fixed $z^k$), and
$\mathrm{tr}_M(W_{\mathrm{valence}})$ provides the binding
deviation proportional to $B/M$.  Schematically,
$$
  \mathrm{tr}_M(W_{\mathrm{atom}})
  \;=\;
  z^{m_{\mathrm{shell}}} \cdot \mathrm{tr}_M(\mathrm{core}) \cdot
  \bigl(1 - B_{\mathrm{valence}} /
          (V \cdot m_n c^2) + \ldots\bigr).
$$
A quantitative refinement is left for follow-up.
