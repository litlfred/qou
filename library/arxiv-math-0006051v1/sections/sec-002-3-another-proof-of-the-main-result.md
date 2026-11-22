---
doc_id: arxiv-math-0006051v1
doc_title: "Finite and p-adic polylogarithms"
section_id: sec-002-3-another-proof-of-the-main-result
section_title: "Another proof of the main result"
section_number: 3
pages: 5-8
source_pdf: 0006051v1.pdf
source_sha256: 10483e75bd3655ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.849
doc_brief: "Finite and p-adic polylogarithms — 4 sections: Front matter; Introduction; The proof"
---
[]{#sec:another label="sec:another"}

In this section we sketch another proof of the main result. This proof has two interesting features: First of all, it proves directly the formula for $F_n$ in terms of the functions $L_n(z)$ defined at the end of the last section. This formula is of course simpler than the original formula. The other feature is that the key ingredient in the proof is a formula, discovered by Rob de Jeu and the author, which seems to be of some further importance. This formula shows up in the computation of syntomic regulators. These two features suggest that the proof to be described below may in some way be more "correct" than the first one, although it is if anything slightly more complicated.

The formula alluded to above is the content of the following

::: proposition
We define a sequence of functions $f_k(z,S)$ inductively as follows: $$f_0(z,S) = \frac{S}{1-S},\quad f_{k+1}(z,S)= \int_z^S
    f_k(z,t)d\log t\;.$$ Then, when $z,S\in W$ and $z\equiv S \pmod{p}$ the following formula holds: $$\label{Delprop}
    -\sum _{k=0}^{n}(-1)^{k}k!\cdot \binom{n}{k}f_{k+1}(z,S)\log
    ^{n-k}(S)
    = (-1)^{n} n! \left( L_{n+1}(z) - L_{n+1}(S) \right)\;.$$
:::

We would like to remark on the potential importance of this formula. The construction of $p$-adic polylogarithms by Coleman is an inductive procedure. At each step the degree $n$ polylogarithm $\operatorname{Li}_n$ is constructed as a locally analytic function satisfying the differential equation $d \operatorname{Li}_n(z) = \operatorname{Li}_{n-1}(z) d\log z$. This determines $\operatorname{Li}_n$ up to a locally constant function and a Frobenius condition replaces this by a globally constant function ambiguity. As remarked by Kontsevich the distribution relation removes the ambiguity completely. The formula above allows for a different approach: The functions $f_n$ have no ambiguity in their definitions and are in fact given by converging power series in $S$ and $z-S$. Once the $f_n$ are given, the formula determines $L_n$ up to a locally constant function and the distribution relation determines it completely. The functions $\operatorname{Li}_n$ can be determined from the $L_n$.

For our purposes, the formula is also useful because it allows us to relate the values of $L_n$ at two congruent points.

::: lemma
Suppose $z\in X$ and $w\in W$. Then $$p^{-n}f_n(z,z(1+pw))\equiv \frac{z}{1-z}\frac{w^n}{n!} \pmod{p}\;.$$
:::

The proof is a direct computation similar to the proof of proposition [\[maincong\]](#maincong){reference-type="ref" reference="maincong"}. Suppose now that $z$ is a root of unity. Then $\log(z(1+pw))\equiv pw \pmod{p^2}$. Thus, using [\[Delprop\]](#Delprop){reference-type="eqref" reference="Delprop"} we immediately obtain $$p^{-n-1}(-1)^n n! (L_{n+1}(z(1+pw))-L_{n+1}(z))\equiv
  c_{n+1} \frac{z}{1-z}w^{n+1}\pmod{p}$$ with $$c_{n+1}=\sum_{k=0}^{n} (-1)^k \frac{k!}{(k+1)!}\binom{n}{k}=
  \frac{1}{n+1}\sum_{k=0}^{n} (-1)^k \binom{n+1}{k+1}=\frac{1}{n+1}\;.$$ so $$p^{-n} (L_n(z(1+pw))-L_n(z))\equiv -(-1)^n \frac{1}{n!}
    \frac{z}{1-z}w^n\pmod{p}\;.$$ We can define the derivation $D$ on functions of two variables as $D=S(1-S)\partial/\partial S+ z(1-z)\partial/\partial z$. One easily obtains the following

::: lemma
If $z,S\in X$ and $z\equiv S\pmod{p}$ then $p^k | Df_k(z,S)$.
:::

Differentiating the key formula we find, with $S=z(1+pw)$, $$\begin{gathered}
  p^{-n}(-1)^n n! (DL_{n+1}(S)-DL_{n+1}(z))\\=
  p^{-n} \sum_{k=0}^n k! \binom{n}{k}\left[Df_{k+1}(z,S)\log^{n-k}(S)+(n-k)
  f_{k+1}(z,S)\log^{n-k-1}(S) \right](1-S)\\ \equiv
  \sum_{k=0}^n k! \binom{n}{k}(n-k) f_{k+1}(z,S)\log^{n-k-1}(S) (1-z)
\equiv
  d_{n+1}zw^{n}\pmod{p}\; ,
\end{gathered}$$ where $$d_{n+1}=\sum_{k=0}^{n} (-1)^k \frac{k!}{(k+1)!}\binom{n}{k}(n-k)=
  -\sum_{l=1}^{n} (-1)^l \binom{n}{l}=1 \;.$$ Let $z$ be a root of unity. Since $\log(z)=0$ we have $$\begin{aligned}
  DL_n(z)&=
  z(1-z)\Big[
             \operatorname{Li}_{n-1}(z)\frac{1}{z}\\
             &+\sum_{m=1}^{n-1} \frac{(-1)^m}{m!}
               \left(
                     \operatorname{Li}_{n-m-1}(z) \frac{1}{z} \log^m(z)
                      + m \operatorname{Li}_{n-m}(z) \log^{m-1}(z) \frac{1}{z}
              \right)
       \Big]\\
       &=(1-z) (\operatorname{Li}_{n-1}(z)-\operatorname{Li}_{n-1}(z))=0\;.
\end{aligned}$$ Thus we find $$p^{-n} DL_n(S)\equiv -(-1)^n \frac{n}{n!} zw^{n-1}\pmod{p}\;.$$ Suppose now that we let $F(z)=\sum_{m=1}^n e_m L_m(z)\log^{n-m}(z)$. Substituting first of all a root of unity in $X$ we find $DF(z)=e_{n-1} (1-z) L_{n-1}(z)$ so we should have $e_{n-1}=-1$. Then $$\begin{aligned}
  p^{1-n}DF(S)&= \sum_{m=1}^n  e_m\Big(DL_m(S)\log^{n-m}(S)
  \\&\phantom{=} \phantom{\sum_{m=1}^n 
    e_m}+(n-m)L_m(S)\log^{n-m-1}(S)(1-S) \Big) p^{1-n}
  \\ &\equiv
  \sum_{m=1}^n e_m\Big(-(-1)^m \frac{m}{m!} zw^{m-1}\cdot
  w^{n-m}\\&\phantom{=} \phantom{\sum_{m=1}^n
    e_m} +
  (n-m)(p^{-m}L_m(z)-(-1)^m \frac{1}{m!}\frac{z}{1-z}w^m)w^{n-m-1}(1-z)\Big)
  \\ &=
  -zw^{n-1}\sum_{m=1}^n ((-1)^m e_m (\frac{m}{m!} + (n-m)\frac{1}{m!}))\\
  &\phantom{=} \phantom{-zw^{n-1}}+\sum_{m=1}^n e_m (n-m) p^{-m}L_m(z)
  \pmod{p} \;. 
\end{aligned}$$ We wish to choose the coefficients $e_m$ in such a way that this expression is independent of $w$. Since in the second sum we know by corollary [\[reduction\]](#reduction){reference-type="ref" reference="reduction"} that $p^{-m}L_m(z)$ is not congruent to $0$ modulo $p$ (as a function of $z$) we see that the only non zero coefficients can be $e_n$ and $e_{n-1}$. By fixing $e_{n-1}=-1$ we get the equation $$(-1)^n e_n \frac{n}{n!}+(-1)^{n}
  \left(\frac{n-1}{(n-1)!}+\frac{1}{(n-1)!}\right)=0$$ from which we can recover $e_{n}=-n$.
