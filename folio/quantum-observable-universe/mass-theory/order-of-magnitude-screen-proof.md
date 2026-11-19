**Item 1.** Multiply $\lambda\le\lambda'$ by $|x|\ge0$ and by $t\ge0$. Reflexivity: $t\le\lambda t$ for $\lambda\ge1$, $t\ge0$. The predicate depends on $x$ only through $|x|$, and with $|t|=t$ the two conjuncts swap under $t\leftrightarrow|x|$. Transitivity: $a\le\lambda b\le\lambda\mu|c|$ and $|c|\le\mu b\le\mu\lambda a$. Products: multiply the inequalities, all factors being nonnegative.

**Item 2.** If $x=x^\ast$, item 1 lifts $\mathrm{Scr}_\mu(t,x^\ast)$ to $\mathrm{Scr}_\lambda(t,x)$.

**Item 3.** For $y=|a|\le\tfrac12$: $1+a\ge1-y\ge\tfrac12$, $1+a\le1+2y$, and $(1+2y)(1+a)\ge(1+2y)(1-y)=1+y(1-2y)\ge1$. So $\mathrm{Scr}_{1+2y}(1,1+a)$, and the product rule of item 1 gives the finite product, the empty product being $\mathrm{Scr}_1(1,1)$.

**Item 4.** $0\le z^m\le1$, so $Bz^m\le B<t$.

**Item 5.** $z^m\le z^n$ for $m\ge n$, so $t\le\lambda Bz^m$ would give $t\le\lambda Bz^n<t$. In the Archimedean case choose $n$ with $z^n<t/(\lambda B+1)$; then $\lambda Bz^n\le(\lambda B+1)z^n<t$.

**Item 6.** $|x-t|\le\lambda t$ is $x-t\le\lambda t$ and $t-x\le\lambda t$; the second holds automatically for $x\ge0$, $\lambda\ge1$. For the counterexample, $|-19/2|=19/2$ lies in $[1/10,10]$, while $|-19/2-1|=21/2>10$.

All six items hold over any linearly ordered field (with the Archimedean property used for the eventual power exit in item 4).

The passage from item 3 to the infinite ladder $\prod_{k\ge2}(1+c_ku_0^k)$ needs $1+y\le e^y$ (analysis) and the convergence of $\sum_k|c_k|u_0^k$, which is not proved. $\blacksquare$
