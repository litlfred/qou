---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-034-324-directional-importance-sampling
section_title: "Directional Importance Sampling"
section_number: 3.2.4
pages: 80-87
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.912
latex_coverage_ratio: 1.0
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
[]{#secimpsampling label="secimpsampling"}

In this section, we discuss a special case of the importance sampling method. Sometimes, the proposed transition probability $T(s\rightarrow s')$ has a certain symmetry along $n$ directions in the state space, so there are always $n$ unique states $s'_1,s'_2,...,s'_n$ which share the same proposed transition probability $T(s\rightarrow s'_i)$, $$T(s\rightarrow s'_1) = T(s\rightarrow s'_2) = ... =T(s\rightarrow s'_n).
 \label{Timpnew}$$ So, from the current state $s$, there is the same chance of proposing any of the states from $s'_1$ to $s'_n$. Similarly, for a given state $s'$, there can be several states $s_1,...,s_n$ which have the same proposed transition probability $T(s'\rightarrow s_i)$. For the reverse proposed transition probability we have, $$T(s'\rightarrow s_1) = T(s'\rightarrow s_2) = ... = T(s'\rightarrow s_n).
 \label{Timprev}$$ The summation of the proposed transition probability alone each direction is the same, $$\sum_{s_i'}T(s\rightarrow s'_i) = \sum_{s_i}T(s'\rightarrow s_i)
= \frac{1}{n}.
 \label{T1on}$$ The total summation of the proposed transition probability is, $$\!\!\!
\sum_{s'}T(s\rightarrow s') = \sum_i \sum_{s_i'}T(s\rightarrow s'_i) =\sum_{s}T(s'\rightarrow s) = \sum_i \sum_{s_i}T(s'\rightarrow s_i)= 1.
 \label{sumT1on}$$

<figure id="FigImpnsample">
<embed src="Figures/PIMCImpSampling.eps" />
<figcaption>Illustration of a state space with 8-direction symmetry. </figcaption>
</figure>

For example, Fig. [1](#FigImpnsample){reference-type="ref" reference="FigImpnsample"} is an illustration for $n=8$ case. In this case, in the configuration space, a particle located at $\bm r=(x,y,z)$ can be described as in state $s$. We can propose to move it to a new state $s'$ with $r'=(x',y',z')$ according to, $$T(s \rightarrow s') = \left(\frac{1}{\sqrt{2\pi \sigma^2}}\right)^3
e^{ - \frac{( x' - x )^2 }{2 \sigma^2} }
e^{ - \frac{( y' - y )^2 }{2 \sigma^2} }
e^{ - \frac{( z' - z )^2 }{2 \sigma^2} }.
 \label{}$$ On each axis there are 2 choices which correspond to the same value of $T(s \rightarrow s')$. They are $x'$ and $x''=2x-x'$, $y'$ and $y''=2y-y'$, $z'$ and $z''=2z-z'$. That means there are in total $n=2^3=8$ directions and unique states correspond to the same $T(s \rightarrow s')$. We can label these 8 states from $s'_1$ to $s'_8$. E.g., set $s'_1$ as the $(x',y',z')$ state, and if $x'>x$, $y'>y$ and $z'>z$, we can simply denote $s'_1 \equiv (+++)$. Set $s'_2$ as the $(x'',y',z')$ state, we can denote $s'_2 \equiv (-++)$, etc. Finally set $s'_8$ as the $(x'',y'',z'')$ state, we can denote $s'_8 \equiv (---)$. So now, $s'_1$ to $s'_8$ simply mean the $n=8$ unique directions in the state space. Similarly, for each of the 8 possible $s'$ with $r'=(x',y',z')$, there are 8 possible $s$ (denoted by the light circles for each $s'$). Their coordinates are $x$ and $x_-=2x'-x$, $y$ and $y_-=2y'-y$, $z$ and $z_-=2z'-z$.

For the summations over $s'_i$, we have $\sum_{s_i'}T(s\rightarrow s'_i)=1/8$. For example, the summation over all the $s'_1=(+++)$ states is,

::: flalign
\_s_1'T(ss'\_1) = ()\^3 = . []{#sumpppimp label="sumpppimp"}
:::

The summation over all the $s'_2=(-++)$ states is $\sum_{s_2'}T(s\rightarrow s'_2)$ which has the same integrand as Eq.([\[sumpppimp\]](#sumpppimp){reference-type="ref" reference="sumpppimp"}) but with a different integral range $\int_{-\infty}^{x} dx
\int_{y}^{+\infty} dy
\int_{z}^{+\infty} dz$, and $\sum_{s_2'}T(s\rightarrow s'_2)$ is also $1/8$. The summation over all the $s'_8=(---)$ states is $\sum_{s_8'}T(s\rightarrow s'_8)$ which has the same integrand as Eq.([\[sumpppimp\]](#sumpppimp){reference-type="ref" reference="sumpppimp"}) and again with a different integral range $\int_{-\infty}^{x} dx
\int_{-\infty}^{y} dy
\int_{-\infty}^{z} dz$, and $\sum_{s_8'}T(s\rightarrow s'_8)$ is $1/8$, too. The summation for all the other states are similar and $\sum_{s_i'}T(s\rightarrow s'_i)$ are all $1/8$. Therefore Eq.([\[T1on\]](#T1on){reference-type="ref" reference="T1on"}) and Eq.([\[sumT1on\]](#sumT1on){reference-type="ref" reference="sumT1on"}) are valid.

If $T(s\rightarrow s')$ has directional symmetry, we can mark the current state $s$ as $s_i$ because it implicitly carries the directional notation $i$. When we proposed a new state $s'$ from such a $T(s\rightarrow s')$, then we can temporarily mark $s'$ as $s'_1$. However, we do not immediately pick this state $s'_1$ as the new trial state. Because from $T(s\rightarrow s')$, each of the $s'_1$ to $s'_n$ states has the same chance to be picked, we want to further pick the 'best' state from $s'_1$ to $s'_n$. We can pick a state $s'_j$ according to $\tilde{\pi}(s'_j)$ such that, $$\tilde{\pi}(s'_j)=\frac{\pi(s'_j)}{\sum_{k=1}^n \pi(s'_k)} .
\label{imppinewdist}$$

This can be called directional importance sampling. In this way, the correspondingly proposed transition probability for directional importance sampling $T^{\textrm{imp}}(s_i\rightarrow s'_j)$ can be written as, $$T^{\textrm{imp}}(s_i\rightarrow s'_j)
= \left[ \sum_{j=1}^n T(s_i\rightarrow s'_j)  \right] \tilde{\pi}(s'_j)
= \frac{ n T(s_i\rightarrow s'_j) \pi(s'_j)}{\sum_{k=1}^n \pi(s'_k)}.
 \label{Timpnewsi}$$ The reverse directional importance sampling transition probability $T^{\textrm{imp}}(s'_j\rightarrow s_i)$ can be similarly written as, $$T^{\textrm{imp}}(s'_j\rightarrow s_i)
= \frac{ n T(s'_j\rightarrow s_i) \pi(s_i)}{\sum_{i=1}^n \pi(s_i)},
\label{Timpreverse}$$ where states $s_1$ to $s_n$ all have the same proposed transition probability $T(s'_j\rightarrow s_i)$[^1].

Therefore after picking $s'_1$ from $T(s\rightarrow s')$ we further pick $s'_j$ by Eq.([\[imppinewdist\]](#imppinewdist){reference-type="ref" reference="imppinewdist"}). Finally we judge if $s'_j$ is accepted or not by the acceptance probability $A(s_i\rightarrow s'_j)$, $$\!\!\!\!\!\!\!\!
A(s_i \rightarrow s'_j)=
\min \left[  1, \frac{\pi(s'_j)T^{\textrm{imp}}(s'_j\rightarrow s_i)}{\pi(s_i) T^{\textrm{imp}}(s_i \rightarrow s'_j)} \right]
=  \min \left[  1, \frac{ T(s'_j\rightarrow s_i) \sum \limits_{k=1}^n \pi(s'_k)  }{ T(s_i\rightarrow s'_j) \sum \limits_{j=1}^n \pi(s_j)  } \right] .
\label{Accptequationimp}$$ If $T(s_i\rightarrow s'_j) =T(s'_j\rightarrow s_i)$, Eq.([\[Accptequationimp\]](#Accptequationimp){reference-type="ref" reference="Accptequationimp"}) simply becomes, $$A(s_i\rightarrow s'_j)
=  \min \left[  1, \frac{\sum_{j=1}^n \pi(s'_j)}{\sum_{i=1}^n \pi(s_i)} \right] .
\label{Accptequationimp2}$$

If there are $s'_j$ with bigger $\pi(s'_j)$ than the $\pi(s'_1)$ from the initially chosen $s'_1$ by $T(s_i\rightarrow s'_1)$, then the directional importance sampling acceptance rate of Eq.([\[Accptequationimp2\]](#Accptequationimp2){reference-type="ref" reference="Accptequationimp2"}) can be higher than acceptance rate from gaussian sampling of Eq.([\[Accptequationsimp\]](#Accptequationsimp){reference-type="ref" reference="Accptequationsimp"}) or regular sample of Eq.([\[Accptequationsimp2\]](#Accptequationsimp2){reference-type="ref" reference="Accptequationsimp2"}). In other words, with this additional importance sampling, we can move more beads in gaussian sampling with a larger step size in regular sampling than those without importance sampling, with the same acceptance rate as without importance sampling. Adding importance sampling can enable us to explore the configuration space more efficiently. The tradeoff is that we need to evaluate all the relevant $\pi(s'_j)$ and $\pi(s_i)$ which can be time-consuming.

As long as the number $n$ is an even number, and each state $s'_i$ can find its opposite direction among the $n$ directions, it can be reduced to a simple 2-directional case. We can pick $n/2$ directions and combine them into one generalized direction, and combine the rest $n/2$ opposite directions into the other generalized direction. Once we picked $s'_1$ from one direction, there is always a state $s'_2$ in exactly the opposite direction. For example, in the $n=8$ case illustrated by Fig. [1](#FigImpnsample){reference-type="ref" reference="FigImpnsample"}, as indicated by the red arrows and lines, we can denote $s$ as $s_1$, and we group $s'_1$ to $s'_4$ into one generalized direction. And, since $s'_5$ is at the opposite direction of $s'_4$, $s'_6$ is the opposite of $s'_3$, $s'_7$ is the opposite of $s'_2$, and $s'_8$ is the opposite of $s'_1$, so we group $s'_5$ to $s'_8$ into the other generalized direction. By doing this, we reduced the $n=8$ case into an $n=2$ case. Every time we proposed $s'_1$, we take $s'_2$ in the opposite direction of $s'_1$ as the only alternative state. We can just mark $s'_2$ as ${s'_1}_{-}$. For the chosen $s'_1$ or $s'_2$, there is a corresponding $s_2$ such that $T(s'_i\rightarrow s_1)=T(s'_i\rightarrow s_2)$. In our PIMC, usually one can find an 'opposite direction' of $\mathcal{R}'$ which can be marked as $\mathcal{R}''$ such that $T_{l'r'}(\mathcal{R} \rightarrow \mathcal{R}')=T_{l'r'}(\mathcal{R} \rightarrow \mathcal{R}'')$, and then we can use directional importance sampling to further pick either $\mathcal{R}'$ or $\mathcal{R}''$.

As a concrete example, we can apply the $n=2$ importance sampling to the single bead sampling in Sections [\[Sample1bead\]](#Sample1bead){reference-type="ref" reference="Sample1bead"}. The algorithm is described as follows.

Step 1

:   For the current state $s$, randomly pick bead $K$, we propose to move its configuration from $R_K$ to $R'_K$ according to Eq.([\[Tlrnew\]](#Tlrnew){reference-type="ref" reference="Tlrnew"}).

Step 2

:   It is 3 dimensional space and the particle number is $A$, each particle along one dimension has 2 different choices of coordinates, so there are $2^{3A}$ different $R'_K$ which give the same value of Eq.([\[Tlrnew\]](#Tlrnew){reference-type="ref" reference="Tlrnew"}). For any proposed $R'_K=\frac{R_{K-1}+R_{K+1}}{2}+\Delta R$, we only pick ${R'_K}_{-}=\frac{R_{K-1}+R_{K+1}}{2}-\Delta R=R_{K-1}+R_{K+1}-R'_K$, because it not only corresponds to the same value of Eq.([\[Tlrnew\]](#Tlrnew){reference-type="ref" reference="Tlrnew"}) but also the opposite direction of $R'_K$. Call the state with total configuration $\mathcal{R'}=\{R_1,..,R'_K,...,R_N\}$ as $s'_1$, and call the state with $\mathcal{R'}_{-}=\{R_1,..,{R'_K}_{-},...,R_N\}$ as $s'_2$ or ${s'_1}_{-}$. We now calculate,

    ::: flalign
    & =\
    & = . []{#imp1beadexample label="imp1beadexample"}
    :::

    Generate a random number $a$ ranging uniformly from 0 to 1. If $a \leq$ Eq.([\[imp1beadexample\]](#imp1beadexample){reference-type="ref" reference="imp1beadexample"}) we choose $R'_K$ which means $s'_1$, otherwise we choose ${R'_K}_{-}$ which means $s'_2$.

Step 3

:   Denote the original state $s$ as $s_1$. According to Eq.([\[Tlrold\]](#Tlrold){reference-type="ref" reference="Tlrold"}), no matter which $s'_i$ is selected, there are only two choices for $s_1$ and $s_2$. Since we denote the original state $s$ with $R_K$ as $s_1$, $s_2$ must include a another choice of $R_K$ call it ${R_K}_{-}$ such that $\left({R_{K}}-\frac{R_{K\!-\!1}+R_{K\!+\!1}}{2} \right)^2=\left({R_{K-}}-\frac{R_{K\!-\!1}+R_{K\!+\!1}}{2} \right)^2$. Similar with ${R'_K}_{-}$, we have $R_K-\frac{R_{K-1}+R_{K+1}}{2}$ = $\frac{R_{K-1}+R_{K+1}}{2}-{R_K}_{-}$ for ${R_K}_{-}$. We denote ${R_K}_{-}=R_{K-1}+R_{K+1}-R_K$ as the opposite position of $R_K$, and we denote $\mathcal{R}_{-}=\{R_1,..,{R_K}_{-},...,R_N\}$ as $s_2$ or ${s_1}_{-}$. The left part of Fig. [2](#FigImpnsample2D){reference-type="ref" reference="FigImpnsample2D"} illustrates the $R_K$, $R_{K-}$, $R'_{K-}$, and $R'_{K-}$. For the picked new state $s'_i$, use Eq.([\[Accptequationimp\]](#Accptequationimp){reference-type="ref" reference="Accptequationimp"}) to calculate the acceptance probability $A(s_i\rightarrow s'_i)$ and we find that

    ::: flalign
    A(s_1s'\_i) &=\
    &= { , e\^ - }\
    &= { 1, } .
    :::

Step 4

:   Generate a uniform random number $b$ which ranges from 0 to 1. If $b \leq A(s_1\rightarrow s'_i)$, the new state $s'_i$ is accepted, so set it as the current state $s$, namely $s = s'_i$, then go to step 1 and continue. Else, the new state $s'_i$ is rejected (in other words the new state $s'_i$ is just the current state $s$), then go to step 1 and continue.

<figure id="FigImpnsample2D">
<embed src="Figures/PIMCImpSampling2D.eps" />
<figcaption>Illustration of 2-direction importance samplings. The left one is for single bead sampling plus 2-direction importance sampling. The right one is for regular sampling plus 2-direction importance sampling.</figcaption>
</figure>

The importance sampling can also be applied on the regular single bead sampling in sections [\[secregularsampling\]](#secregularsampling){reference-type="ref" reference="secregularsampling"}. The algorithm is very similar. The difference is that, in step 1, we propose a move for the selected bead $K$ according to Eq.([\[regsampling1\]](#regsampling1){reference-type="ref" reference="regsampling1"}). In step 2, $R'_K-R_K=R_K-{R'_K}_{-}$ so ${R'_K}_{-}=2R_{K}-R'_K$, and denote the new state with $R'_K$ as $s'_1$, with ${R'_K}_{-}$ as $s'_2$. In step 3, denote the current state as $s_1$, if $s'_1$ is chosen, $R_K-R'_K=R'_K-{R_K}_{-}$ so ${R_K}_{-}=2R'_{K}-R_K$. If $s'_2$ is chosen, $R_K-{R'_K}_{-}={R'_K}_{-}-{R_K}_{-}$ so ${R_K}_{-}=2{R'_{K}}_{-}-R_K$. Based on the chosen $s'_1$ or $s'_2$, denote the corresponding ${R_K}_{-}$ as $s_2$. The right part of Fig. [2](#FigImpnsample2D){reference-type="ref" reference="FigImpnsample2D"} illustrates the relevant states and the coordinates. Since $T(s_1\rightarrow s'_i) =T(s'_i\rightarrow s_1)$, the $A(s_1\rightarrow s'_i)$ is simply Eq.([\[Accptequationimp2\]](#Accptequationimp2){reference-type="ref" reference="Accptequationimp2"}) and we have, $$\begin{aligned}
\!\!\!\!\!\!\!\! A(s_1\rightarrow s'_i) \!\!\!\! &=& \!\!\!\! \min \left[
 1,
 \frac{ \sum \limits_{j=1}^2 \pi(s'_j)  }{  \sum \limits_{j=1}^2 \pi(s_j)  }
 \right]  \nonumber \\
 &=& \!\!\!\! \min \left \{
 1,
 \frac{ f^V_{l'r'}(\mathcal{R}') g^F(\mathcal{R}') + f^V_{l'r'}(\mathcal{R}'_{-}) g^F(\mathcal{R}'_{-}) }
 { f^V_{lr}(\mathcal{R}) g^F(\mathcal{R}) + f^V_{lr}(\mathcal{R}_{-}) g^F(\mathcal{R}_{-})  }
 \right \} \nonumber \\
&=& \!\!\!\! \min \left \{
 1,
 \frac{f^V_{l'r'}(\mathcal{R}') G^f_{K-1, K'} G^f_{K', K+1}
 + f^V_{l'r'}(\mathcal{R}'_{-}) G^f_{K-1, K'_{-}} G^f_{K'_{-}, K+1}  }
 {f^V_{lr}(\mathcal{R}) G^f_{K-1, K} G^f_{K, K+1}
 +f^V_{lr}(\mathcal{R}_{-}) G^f_{K-1, K_{-}} G^f_{K_{-}, K+1}  }
 \right \} . ~~~
\end{aligned}$$ The $K_{-}$ or $K'_{-}$ appear at the $I$ or $J$ subscript in $G^f_{I,J}$ means ${R_K}_{-}$ or ${R_K}'_{-}$ in the corresponding place in Eq.([\[Gfij\]](#Gfij){reference-type="ref" reference="Gfij"}).

[^1]: Note that $T^{\textrm{imp}}(s\rightarrow s'_i)$ is a valid proposed transition probability. Because for Eq.([\[Timpreverse\]](#Timpreverse){reference-type="ref" reference="Timpreverse"}), with the help of Eq.([\[Timpnew\]](#Timpnew){reference-type="ref" reference="Timpnew"}) and Eq.([\[T1on\]](#T1on){reference-type="ref" reference="T1on"}), we can see that, $$\begin{aligned}
    \sum_{s'} T^{\textrm{imp}}(s\rightarrow s') &=  \sum_{i=1}^n \sum_{s'_i} T^{\textrm{imp}}(s\rightarrow s'_i) \nonumber \\
    &= n \sum_{i=1}^n \sum_{s'_i}  \frac{T(s\rightarrow s'_i) \pi(s'_i)}{\sum_{j=1}^n \pi(s'_j)} \nonumber \\
    &= n  \sum_{s'_i} T(s\rightarrow s'_i) \frac{\sum_{i=1}^n \pi(s'_i)}{\sum_{j=1}^n \pi(s'_j)} \nonumber \\
    &= n \sum_{s'_i} T(s \rightarrow s'_i) \nonumber \\
    &= 1 . \label{Timpnewnorm}
    \end{aligned}$$ So $T^{\textrm{imp}}(s\rightarrow s'_i)$ based on the importance sampling algorithm is a valid proposed transition probability because it is non-negative and its summation over all the possible states is 1. Actually Eq.([\[Timpnewnorm\]](#Timpnewnorm){reference-type="ref" reference="Timpnewnorm"}) may not really need to be required. As long as the normalization factors of $T^{\textrm{imp}}$ can be canceled in acceptance rate $A(s \rightarrow s')$ it will be correct.
