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
on the free monoid; it uses only concatenation, not the quadratic or
Yang--Baxter relations.  $\square$

Neither part uses a braiding hypothesis.

**Two faces of the arrow of time.**  The braiding $c_{V,V}$
and the Reeb vector field $\xi$
(the categorical Reeb derivation, defined later in this chapter) are read
as two complementary viewpoints on one arrow of time:

- **Categorical arrow** ($c_{V,V}$): which strand crosses
  *over*.  A letter $\sigma_i \in W_n$ is a positive crossing and
  applies $c_{V,V}$.  The negative crossing $\sigma_i^{-1}$, which
  applies $\bar{c}_{V,V} := c_{V,V}^{-1}$, is not a letter of $W_n$;
  $\prec_c$ orders positive words only.  The reading is that forward
  time is Gröbner--Shirshov reduction under $\prec_c$.

- **Geometric arrow** ($\xi$): which direction the Reeb flow
  runs.

**Crossing reversal and time reversal.**  The crossing reversal
involution $\sigma \colon K \mapsto K^{\sigma}$ (mirror all
crossings) corresponds to switching the braiding:
$c_{V,V} \leftrightarrow \bar{c}_{V,V}$.  The switch exchanges which
crossing the letter $\sigma_i$ denotes, so it changes the reading of a
word, not the order: $\prec_c$ depends only on word length and the
chosen order on the letters, and is the same for both braidings.  On
the geometric side the switch is read as the reversal
$\xi \mapsto -\xi$ of the Reeb flow.  In the Feynman--Stueckelberg
interpretation, an antiparticle ($K^{\sigma}$) is its particle
($K$) with time reversed, that is, with the opposite braiding.
CPT symmetry is then read as invariance of the QOU axioms under
simultaneous
$c_{V,V} \leftrightarrow \bar{c}_{V,V}$ (T),
$K \mapsto K^{\sigma}$ (C), and
$\sigma_i \mapsto \sigma_{n-i}$ (P, strand reflection).
