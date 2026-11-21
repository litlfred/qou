*Proof that $\prec_c$ is well-founded on $W_n$.*
Let $S \subseteq W_n$ be non-empty.

(a) **Degree is bounded below.**  Every $w \in W_n$ has
$\ell(w) \geq 0$.  Let $d = \min\{\ell(w) : w \in S\}$.
The set $S_d = \{w \in S : \ell(w) = d\}$ is non-empty.

(b) **Finite alphabet at each degree.**  Each $w \in S_d$
is a word of length $d$ over the finite alphabet
$\{1, \ldots, n-1\}$.  There are at most $(n-1)^d$ such
words, a finite set.  Every finite totally ordered set
has a minimum.  Let $w_0$ be the lex-minimum of $S_d$.

(c) **$w_0$ is the minimum of $S$.**  For any $w \in S$:
if $\ell(w) > d$ then $w_0 \prec_c w$ (shorter words
first); if $\ell(w) = d$ then $w_0 \leq_{\mathrm{lex}} w$
by construction.  $\square$

*Compatibility with concatenation.*  Let $w \prec_c w'$ and
$u, v \in W_n$.  If $\ell(w) < \ell(w')$ then
$\ell(u\,w\,v) < \ell(u\,w'\,v)$, since length is additive.
If $\ell(w) = \ell(w')$ and $w <_{\mathrm{lex}} w'$, a common
prefix $u$ leaves the first differing letter unchanged, and so
does a common suffix $v$, because $w$ and $w'$ have equal length
and their first difference occurs before $v$ begins.  Hence
$u\,w\,v \prec_c u\,w'\,v$.  This is the admissibility
condition of an
([admissible system](#unital-groebner-bases:def:admissible-system))
on the free monoid; it uses only concatenation, not the Hecke or
Yang--Baxter relations.  $\square$

Neither part uses a braiding hypothesis.
