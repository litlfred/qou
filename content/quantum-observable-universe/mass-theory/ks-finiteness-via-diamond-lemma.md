To put a motivic measure on the moduli stack of objects,
Kontsevich--Soibelman *assume* their categories are
**ind-constructible** \cite{kontsevich-soibelman-2008} — countable
inductive limits of constructible sets (their Lemma 1, Corollary 1).
For a general $3$-Calabi--Yau category there is no other way to make
"the number of objects of class $\gamma$" well defined; the hypothesis
is the load-bearing tameness input.

In the QOU setting this finiteness is **not assumed but proved**, in
two lines, by the Gröbner--Shirshov / Diamond Lemma — the same move by
which Poincaré--Birkhoff--Witt becomes an algebraic triviality (the
unital Gröbner-bases route to PBW).

**Setup (one definition).** The Gröbner--Shirshov normal form gives
$H_n(q)$ a basis of **standard monomials** $\{T_w : w \in S_n\}$
indexed by the finite Coxeter group $S_n$ — confluence of the braid +
Hecke rewriting system (Bergman's Diamond Lemma \cite{bergman1978};
Bokut \cite{bokut2005}).

**Two-line proof.** The standard monomials of Coxeter length
$\ell(w) = k$ form a **finite** set — at most
$|\{w \in S_n : \ell(w) = k\}| \le |S_n|$ of them — so each length-$k$
slice of $H_n(q)$ is a finite-dimensional scheme, *constructible by
theorem*, and the curvature-rank stratification ([GB
stratification](#prop:curvature-rank-gb-stratification)) refines it
into finitely many strata. No tameness hypothesis is needed:
confluence delivers the finite slice. $\square$

So where KS *assume* ind-constructibility to buy finiteness, QOU
*earns* it from the Diamond Lemma — a known structural input given a
prior abstract assumption, recovered here as an algebraic theorem. The
price is specificity: QOU commits to the semisimple Hecke/braid
category rather than an arbitrary $3$CY, which is exactly the trade
that lets the partition decomposition replace the motivic Hall
algebra.
