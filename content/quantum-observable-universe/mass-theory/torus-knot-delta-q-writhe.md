*Lean sibling: a field $R$ carrying the $q$-data (AGENTS.md §7c); the identity is purely algebraic, pre-archimedean.*

**Proposition (writhe exponent of the torus-knot $\delta_q$ decoration).** *For the
torus knot $T_{m,p}$ — the closure of the standard positive braid
$(\sigma_1\cdots\sigma_{m-1})^p$, $\gcd(m,p)=1$ — the $q$-dimension decoration is the
Hecke deformation $h$ times the quantum integer at the **writhe** $w = (m-1)p$:*

$$
  \delta_q(T_{m,p}) \;:=\; q^{w} - q^{-w}
  \;=\; h\,[w]_q,
  \qquad
  w = (m-1)p,\quad h = q - q^{-1},\quad [w]_q = \frac{q^{w} - q^{-w}}{q - q^{-1}}.
$$

*an exact identity in the substrate ring $R = \mathbb{Z}[q^{\pm 1/2}, h^{-1}]$ —
**pre-archimedean, no $\pi$** — needing only $q - q^{-1} \neq 0$. Lean
`torus_deltaQ_eq_h_qbracket`, sorry-free.*

The decoration is the **bar-odd** ($\sinh$, $e_-$) part of the **trivial /
top-channel twist** $q^{(m-1)p}$: in the trivial one-dimensional block of the
Hecke algebra $H_m(q)$ every generator acts by the symmetric eigenvalue
$\sigma_i \mapsto q$, so the Coxeter word $\sigma_1\cdots\sigma_{m-1}$ acts by
$q^{m-1}$ and $(\sigma_1\cdots\sigma_{m-1})^p$ by $q^{(m-1)p}$; its bar-conjugate
($q \leftrightarrow q^{-1}$) is $q^{-(m-1)p}$, and the antisymmetric extraction is
$\delta_q = q^{w} - q^{-w}$. The writhe $w = (m-1)p$ is the number of positive
crossings of the braid.

The two-strand case $m = 2$ recovers the basis-knot decoration
[`prop:alpha-basis-knot-delta-q`](#prop:alpha-basis-knot-delta-q),
$\delta_q(T_{2,k}) = h\,[k]_q$ (writhe $w = k$). The three-strand force-carriers
then have **derived** (not assumed) exponents

$$
  \delta_q(T_{3,4}) = h\,[8]_q, \qquad \delta_q(T_{3,5}) = h\,[10]_q,
$$

the latter confirming the value used by
[`prop:alpha-em-categorical-trace-ratio`](#prop:alpha-em-categorical-trace-ratio)
in $\alpha_{EM} = h^2/\bigl(q\,\delta_q(T_{2,9})\,\delta_q(T_{3,5})\bigr)$. The
writhe exponents are rigidly tied to the leading twist $-q^{2p}$ of the Jones
polynomial of $T_{3,p}$ (cross-checked against the knot tables
$8_{19} = T_{3,4}$, $10_{124} = T_{3,5}$). Symbolic cross-check:
[`rosso_jones_three_strand_delta_q.py`](../../computations/rosso_jones_three_strand_delta_q.py).

The same writhe $w$ governs the chirality mass-factor $a_K = 1 + w\,h$ of
[`prop:chirality-writhe-ribbon-derivation`](#prop:chirality-writhe-ribbon-derivation),
but the two are distinct: that factor comes from the **ribbon full-twist**
$\varTheta\,v_\lambda = q^{2c(\lambda)}v_\lambda$ acting on *every* Wedderburn
block by its content $c(\lambda)$, whereas $\delta_q$ here is the **bar-odd part
of the single trivial-channel twist** $q^{(m-1)p}$. They share the writhe but
extract different data (a full-twist framing factor vs. an $e_-$ decoration).
