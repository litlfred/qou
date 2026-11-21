---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-032-322-multi-level-sampling
section_title: "Multi-level Sampling"
section_number: 3.2.2
pages: 69-77
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.913
latex_coverage_ratio: 1.0
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
[]{#secMultibeadSample label="secMultibeadSample"}

Due to the disadvantage of single bead sampling, for a given amount of computation time, we have to sample multiple beads at a time instead of just one in order to make the sampling efficient. For example, if we propose to move $u$ portion of the $N$ beads, so about $uN$ beads will be proposed to move at a time, and the acceptance rate is $a$. Then in order for all the $N$ beads to be moved, we need at least $1/(ua)$ trials. For each trial, in order to calculate acceptance rate $A(s\rightarrow s')$, we need to do $uN$ updates for either $\phi^r_{M}(\mathcal{R},S)$ in Eq.([\[phirMR\]](#phirMR){reference-type="ref" reference="phirMR"}) or $\phi^l_{M}(\mathcal{R},S)$ in Eq.([\[philMR\]](#philMR){reference-type="ref" reference="philMR"}) with accordingly range of $M$. So for the proposed moves there are $uN/(ua)=N/a$ updates. Besides, among all the $1/(ua)$ trials, only about $a/(ua)=1/u$ are accepted, for those accepted moves, we need to update some beads for the $\phi^r_{M}(\mathcal{R},S)$ and some for the $\phi^l_{M}(\mathcal{R},S)$. This will actually results in updating about $N$ beads. So for the accepted moved, there will be $N/u$ updates. So totally, there will be $N/u+N/a=N(1/u+1/a)$ updates. And the factor $(1/u+1/a)$ is usually much smaller than $N$, for example, N=500, when $u=1/3$, $a$ could be around 0.1 so $10\%$, so $(1/u+1/a) \approx 13$ which is much smaller than $N=500$. So $N(1/u+1/a)$ updates much more cheaper than $N^2$ updates needed for the single beads sampling.

In order to find some ways to sample multiple beads at a time, we need to make full use of Eq.([\[Rdiffadd1\]](#Rdiffadd1){reference-type="ref" reference="Rdiffadd1"}). From the total $N+1$ beads on the time line from bead $0$ to bead $N$, we randomly pick $2^n+1$ contingent beads from bead $I$ to bead $I+2^n$, where $n$ is a positive integer. To make the notations easier, here we temporarily mark the configurations from bead $I$ to bead $I+2^n$ as $R_0$ to $R_{2^n}$, and we mark their configurations as, $$\mathcal{R}=\{R_0, R_1, R_2, ..., R_{2^n-1}, R_{2^n} \}. \label{mathcalRmulbeads}$$ The configurations $R_0$ to $R_{2^n}$ in Eq.([\[mathcalRmulbeads\]](#mathcalRmulbeads){reference-type="ref" reference="mathcalRmulbeads"}) are just the relabeling of the original $R_I$ to $R_{I+2^n}$ among the total $N+1$ beads on the path.

The product of the free particle propagators $g^F(\mathcal{R})$ can be written as, $$g^F(\mathcal{R}) = \prod_{I=0}^{2^n-1} G^f_{I, I+1}.  \label{gF2n}$$ We can group the $2^n+1$ beads $\{R_0, R_1, ..., R_{2^n} \}$ in $\mathcal{R}$ into $n$ levels as the following,

::: empheq
align

::: array
cccc [Level]{.roman} 0 :& R_0, R\_2\^n . & ([2 beads]{.roman}) & L\^n_0()\
[Level]{.roman} 1 :& R\_2\^n . & ([1 bead]{.roman}) & L\^n_1()\
[Level]{.roman} 2 :& R\_ 2\^n , R\_ 2\^n . & ([2 beads]{.roman}) & L\^n_2()\
⋮& ⋮& ⋮& ⋮\
[Level]{.roman} k :& R\_ 2\^n , R\_ 2\^n, R\_ 2\^n, \..., R\_ 2\^n . & ([$2^{k-1}$ beads]{.roman}) & L\^n_k()\
⋮& ⋮& ⋮& ⋮\
[Level]{.roman} n :& R\_1, R\_3, R\_5, R\_7, \..., R\_2\^n-1 . & ([$2^{n-1}$ beads]{.roman}) & L\^n_n()
:::
:::

We can then use Eq.([\[GKm1KpKpkp1\]](#GKm1KpKpkp1){reference-type="ref" reference="GKm1KpKpkp1"}) to rearrange Eq.([\[gF2n\]](#gF2n){reference-type="ref" reference="gF2n"}) level by level and Eq.([\[gF2n\]](#gF2n){reference-type="ref" reference="gF2n"}) becomes, $$g^F(\mathcal{R}) = \prod_{k=0}^{n} L^n_k(\mathcal{R}) ,
\label{gFRplevels}$$ where $L^n_k(\mathcal{R})$ is defined as the product of gaussian functions at level $k$,

$$L^n_k(\mathcal{R}) =
\begin{cases}
G^f_{0, 2^n},  &  k = 0. \\
 \prod\limits_{I=1}^{2^{k-1}}  G^f_{\frac{2I-1}{2^k}2^{n}; \frac{2I-2}{2^k}2^{n}, \frac{2I}{2^k}2^{n}}  , & k \neq 0
.\end{cases} \label{Lfkn}$$ For any non negative integer $J$, $K$, $L$, $M$, $N$, the $G^f_{J, K}$ is calculated by Eq.([\[Gfij\]](#Gfij){reference-type="ref" reference="Gfij"}), and the $G^f_{M;L,N}$ in Eq.([\[Lfkn\]](#Lfkn){reference-type="ref" reference="Lfkn"}) is, $$\begin{aligned}
& G^f_{M;L,N} =
\left( \frac{2m}{\pi |N-L| \Delta \tau \hbar^2} \right)^{\frac{3A}{2}}
 e^{  -   \frac{ \left(  R_{M}  - \frac{ R_{L} + R_{N}   }{2}   \right)^2   }   {2\times \frac{|N-L|}{2}\Delta \tau \frac{\hbar^2}{2m}   }    }.
\label{gFRplevels}
\end{aligned}$$ Given Eqs.([\[Lfkn\]](#Lfkn){reference-type="ref" reference="Lfkn"}) and ([\[gFRplevels\]](#gFRplevels){reference-type="ref" reference="gFRplevels"}), we can propose to move multiple beads, from bead $1$ to $2^n-1$ such that the new configuration is $$\mathcal{R}'=\{R'_0, R'_1, R'_2, ..., R'_{2^n-1}, R'_{2^n} \},  \label{mathcalRpmulbeads}$$ where $R_0$ and $R_{2^n}$ remain the same although they are marked as $R'_0$ and $R'_{2^n}$ in Eq.([\[mathcalRpmulbeads\]](#mathcalRpmulbeads){reference-type="ref" reference="mathcalRpmulbeads"}). The product of the new free particle propagators $g^F(\mathcal{R}')$ can be written as, $$g^F(\mathcal{R}') = \prod_{k=0}^{n} L^n_k(\mathcal{R}') . \label{gFRp}$$

We can set the proposed transition probability $T_{l'r'}(\mathcal{R} \rightarrow \mathcal{R}')$ as, $$T_{l'r'}(\mathcal{R} \rightarrow \mathcal{R}') = g^F(\mathcal{R}') = \prod_{k=0}^{n} L^n_k(\mathcal{R}').
 \label{Tlrnewmbeads}$$ Eq.([\[Tlrnewmbeads\]](#Tlrnewmbeads){reference-type="ref" reference="Tlrnewmbeads"}) means that we can set the proposed transition probability at each level $k$ as $T^n_k(\mathcal{R}')$ such that $$T^n_k(\mathcal{R}') =  L^n_k(\mathcal{R}'),
 \label{Tlrnewmbeadslevelk}$$ and $T_{l'r'}(\mathcal{R} \rightarrow \mathcal{R}')$ can be just written as $$T_{l'r'}(\mathcal{R} \rightarrow \mathcal{R}') = \prod_{k=0}^{n} T^n_k(\mathcal{R}').
 \label{Tlrnewmbeadslbl}$$ The reverse transition probability $T_{lr}(\mathcal{R}' \rightarrow \mathcal{R})$ can be written as, $$T_{lr}(\mathcal{R}' \rightarrow \mathcal{R}) =
\prod_{k=0}^{n} T^n_k(\mathcal{R}) .
 \label{Tlroldmbeadslbl}$$

We can call this multi-level or n-level sampling, because we can propose to move the beads level by level from level 0 to level $n$, by using $T^n_k(\mathcal{R}')$ at each level. By doing proposed moves in this way, we implement Eq.([\[Tlrnewmbeadslbl\]](#Tlrnewmbeadslbl){reference-type="ref" reference="Tlrnewmbeadslbl"}). This makes $g^F(\mathcal{R}')  T_{lr}(\mathcal{R}' \! \rightarrow \! \mathcal{R}) = g^F(\mathcal{R}) T_{l'r'}(\mathcal{R} \! \rightarrow \! \mathcal{R}')$ and it enables Eq.([\[Acc2\]](#Acc2){reference-type="ref" reference="Acc2"}) to become Eq.([\[acc2simp\]](#acc2simp){reference-type="ref" reference="acc2simp"}), and we can use Eq.([\[Accptequationsimp\]](#Accptequationsimp){reference-type="ref" reference="Accptequationsimp"}) to judge if accept $\mathcal{R}'$ or not. Fig. [1](#PIMCBisection){reference-type="ref" reference="PIMCBisection"} is the illustration of 3-level sampling.

<figure id="PIMCBisection">
<embed src="Figures/PIMCBisection.eps" />
<figcaption>Illustration of a 3-level sampling algorithm. </figcaption>
</figure>

The algorithm can be described as follows.

Step 1

:   For the total $N+1$ beads on the time line as shown in Fig. [\[PIMCbeads\]](#PIMCbeads){reference-type="ref" reference="PIMCbeads"}, select a proper integer $n$, randomly pick $2^n+1$ contingent beads from $R_I$ to $R_{I+2^n}$ (note that in the program, $n$ does not need to be a fixed number, we can pick different $n$ each time when we are at step 1). For notational convenience, temporarily call them $R_0$ to $R_{2^n}$ instead of $R_I$ to $R_{I+2^n}$, and we use $\mathcal{R}$ to denote the group, $\mathcal{R}=\{R_0, R_1, R_2, ..., R_{2^n-1}, R_{2^n} \}$.

    For example, in Fig. [1](#PIMCBisection){reference-type="ref" reference="PIMCBisection"}, it is $n=3$ so $2^n=8$. We randomly pick $R_I$ to $R_{I+8}$ beads from the total $N+1$ beads, we temporarily mark them as $R_0$ to $R_8$.

Step 2

:   1.  If we keep $R_0$ and $R_{2^n}$ unchanged, this can be taken as a 'fake' level 0 move, so $R'_0=R_0$ and $R'_{2^n}=R_{2^n}$. In this case, $L^n_0(\mathcal{R}') = L^n_0(\mathcal{R})$, we set $$T_{l'r'}(\mathcal{R} \rightarrow \mathcal{R}') = \prod_{k=1}^{n} L^n_k(\mathcal{R}') ,
         \label{Tlrnewmbeadsf1}$$ and it can still make Eq.([\[Acc2\]](#Acc2){reference-type="ref" reference="Acc2"}) become Eq.([\[acc2simp\]](#acc2simp){reference-type="ref" reference="acc2simp"}). And we go to step 3.

    2.  Else, if we keep $R_{2^n}$ unchanged and just propose $R'_0$ (so $R'_{2^n}=R_{2^n}$), then according to Eq.([\[Lfkn\]](#Lfkn){reference-type="ref" reference="Lfkn"}), $L^n_0(\mathcal{R}')=\exp \left[ - \frac{(R'_0-R_{2^n})^2}{2\times 2^n \Delta \tau \frac{\hbar^2}{m}  } \right]$, we propose $${\bm{r}'}_i^0 =
           {\bm{r}}_i^{2^n}
          + \bm{g}_i \sqrt{ 2^n\Delta \tau \frac{\hbar^2}{m}} ,
         \label{}$$ for $i$ from 1 to $A$, and we have $R_0'$ and go to step 3 for the rest $L^n_k(\mathcal{R}')$.

    3.  Else, if we keep $R_{0}$ unchanged and just propose $R'_{2^n}$ (so $R'_0=R_0$), then according to Eq.([\[Lfkn\]](#Lfkn){reference-type="ref" reference="Lfkn"}), $L^n_0(\mathcal{R}')=\exp\ \Big[ - \frac{(R_0-R'_{2^n})^2}{2\times 2^n \Delta \tau \frac{\hbar^2}{m}  } \Big]$, we propose $${\bm{r}'}_i^{2^n} =
           {\bm{r}}_i^{0}
          + \bm{g}_i \sqrt{ 2^n\Delta \tau \frac{\hbar^2}{m}} ,
         \label{}$$ for $i$ from 1 to $A$, and we have $R_{2^n}'$ and go to step 3 for the rest $L^n_k(\mathcal{R}')$.

    4.  Else, we can also use the one bead sampling algorithm described in section [\[Sample1bead\]](#Sample1bead){reference-type="ref" reference="Sample1bead"}, propose $R'_0$ according to $R_1$ and $R'_{2^n}$ according to $R_{2^n-1}$ and then judge and go to step 1.

    For example, in Fig. [1](#PIMCBisection){reference-type="ref" reference="PIMCBisection"}, we keep $R_0$ and $R_8$ unchanged, so $R_0'=R_0$ and $R_8'=R_8$.

Step 3

:   According to the product of gaussian functions of $L^n_k(\mathcal{R})$ in Eq.([\[Lfkn\]](#Lfkn){reference-type="ref" reference="Lfkn"}), we propose the moves level by level, so $k$ from $1$ to $n$. At level $k$, $2^{k-1}$ beads need be to moved, which means from $I=1$ to $2^{k-1}$, each $R_{\frac{2I-1}{2^k}{2^{n}}}$ need to be proposed to a new configuration $R'_{\frac{2I-1}{2^k}{2^{n}}}$. And we propose $R'_{\frac{2I-1}{2^k}{2^{n}}}$ according to the $G^f_{\left(\frac{2I-1}{2^k}2^{n}\right)'; \left(\frac{2I-2}{2^k}2^{n}\right)', \left(\frac{2I}{2^k}2^{n}\right)'}$ in $L^n_k(\mathcal{R}')$ in Eq.([\[Tlrnewmbeads\]](#Tlrnewmbeads){reference-type="ref" reference="Tlrnewmbeads"}), such that ${\bm{r}'}_i^{{(2I-1){2^{n-k}}}}$ (the new coordinates of particle $i$) in $R_{\frac{2I-1}{2^k}{2^{n}}}$ is proposed according to, $${\bm{r}'}_i^{{\frac{2I-1}{2^{k}}{2^{n}}}} \!\!=
      \frac{ {\bm{r}'}_i^{\frac{2I-2}{2^{k}}{2^{n}}} \!\! + {\bm{r}'}_i^{\frac{2I}{2^{k}}{2^{n}}}      }{2}
      + \bm{g}_i \sqrt{ \frac{2^n}{2^k}\Delta \tau \frac{\hbar^2}{2m}} .
     \label{Lfknp}
    \hspace{-1em}$$ For $i$ from 1 to $A$, we propose to move particle $i$ according to Eq.([\[Lfknp\]](#Lfknp){reference-type="ref" reference="Lfknp"}) in each configuration in each level.

    Note that the level $k$ beads are only proposed based on the beads of previous levels, so this allow us to propose the new beads level by level. After we propose the new configurations level by level, we have $\mathcal{R}'=\{R'_0, R'_1, R'_2, ..., R'_{2^n-1}, R'_{2^n} \}$. For example, in Fig. [1](#PIMCBisection){reference-type="ref" reference="PIMCBisection"}, level 1, 2 and 3 are,

    Level 1

    :   $k=1$, $2^{1-1}=1$, $I=1$, each $[{(2I-1){2^{3-1}}}]^{\text{th}}$ bead needs to be moved, so $R_4$ is the only bead that needs to be moved, and we propose $R_4'$ based on $R'_0$ and $R'_8$ according to Eq.([\[Lfknp\]](#Lfknp){reference-type="ref" reference="Lfknp"}), and each particle is moved as $${\bm{r}'}_i^{4} =
          \frac{ {\bm{r}'}_i^{0}  + {\bm{r}'}_i^{8}      }{2}
          + \bm{g}_i \sqrt{ 4 \Delta \tau \frac{\hbar^2}{2m}} .$$ After looping over all the particles, go to level 2.

    Level 2

    :   $k=2$, $2^{2-1}=2$, so $I=1,2$, each $[(2I-1){2^{3-2}}]^{\text{th}}$ bead needs to be moved, so $R_2$ and $R_6$ are the two beads that need to be moved, and according to Eq.([\[Lfknp\]](#Lfknp){reference-type="ref" reference="Lfknp"}), we propose $R'_2$ based on $R'_0$ $R'_4$, and $R'_6$ based on $R'_4$ and $R'_8$. E.g., each particle in $R'_2$ is moved as $${\bm{r}'}_i^{2} =
          \frac{ {\bm{r}'}_i^{0}  + {\bm{r}'}_i^{4}      }{2}
          + \bm{g}_i \sqrt{ 2 \Delta \tau \frac{\hbar^2}{2m}} ,$$ and that in $R'_6$ is moved as $${\bm{r}'}_i^{6} =
          \frac{ {\bm{r}'}_i^{4}  + {\bm{r}'}_i^{8}      }{2}
          + \bm{g}_i \sqrt{ 2 \Delta \tau \frac{\hbar^2}{2m}}.$$ After looping over all the particles, go to level 3.

    Level 3

    :   $k=3$, $2^{3-1}=4$, so $I=1,2,3,4$, each $[(2I-1){2^{3-3}}]^{\text{th}}$ beads need to be moved, and so $R'_1$, $R'_3$,$R'_5$, $R'_7$ need to be proposed according to Eq.([\[Lfknp\]](#Lfknp){reference-type="ref" reference="Lfknp"}) similarly as described before.

Step 4

:   Now we need to look at the whole set of $N+1$ beads on the time line, and use consistent notations in the work. The $\{R'_0, R'_1, R'_2, ..., R'_{2^n-1}, R'_{2^n} \}$ in step 3 are in fact as mentioned in step 1, really $\{R'_I, R'_{I+1}, R'_{I+2}, ..., R'_{I+2^n-1}, R'_{I+2^n} \}$ on the time line. So overall, the proposed configuration $\mathcal{R}'$ is, $$\mathcal{R}'=\{R_0,R_1,...,R'_I, R'_{I+1}, ..., R'_{I+2^n}, ..., R_N \}.$$ The original configuration $\mathcal{R}$ is just Eq.([\[defmathcalR\]](#defmathcalR){reference-type="ref" reference="defmathcalR"}) for the whole $N+1$ original beads.

    For example, in Fig. [1](#PIMCBisection){reference-type="ref" reference="PIMCBisection"}, once we have the new $\{R'_0, R'_1, ..., R'_{8} \}$, we change their labels to the original ones $\{R'_I, R'_{I+1}, ..., R'_{I+8} \}$. So finally $\mathcal{R}'$ is the same as $\mathcal{R}$ except that $R_I$ to $R_{I+8}$ are replaced by $R'_I$ to $R'_{I+8}$.

Step 5

:   Use Eq.([\[Accptequationsimp\]](#Accptequationsimp){reference-type="ref" reference="Accptequationsimp"}) to judge if we accept the proposed configurations $\mathcal{R}'$ or not. Then go to step 1 and continue.

    For example, in Fig. [1](#PIMCBisection){reference-type="ref" reference="PIMCBisection"}, we use Eq.([\[Accptequationsimp\]](#Accptequationsimp){reference-type="ref" reference="Accptequationsimp"}) to judge if we accept the proposed configurations $\mathcal{R}'$ or not.

It should be pointed out that, the proposed trial moves at each level in the multi-level sampling are the same as in the bisection method ([@Ceperley95a]). But the two are not the same. We propose all the n-level new configurations and then do an overall acceptance or rejection. However in the bisection method, we accept or reject at each level, and if the proposed configuration is rejected at level $k$, then the whole proposed configurations from level 1 to $k$ will be completely rejected and discarded.

In the bisection method, the lower the level, the less time consuming it is to do the rejection. In other words, 'if you want to reject, reject early.' It works best if the first level's acceptance rate is highly distinct from the rest levels'.

For example, consider a 3-level bisection, if the first level acceptance rate is $30\%$, the second and third levels' are $80\%$ and $90\%$, then the total acceptance rate is $21.6\%$. But since the first level acceptance rate is significantly lower than the rest, actually most trial moves are quickly rejected at the first level and there is no need to spend time to go to and level, and those trial moves which get to the and level are mostly be accepted. Therefore, not much time is wasted at the and levels. In this case, bisection method will be faster than multi-level sampling simply because it can reject early. Bisection works well for systems with potentials with highly repulsive cores where core overlap can be deleted early and rejected.

However, if the three levels' acceptance rate are similar, then the bisection method does not have an advantage over multi-level sampling. If the , and level's acceptance rate are $50\%$, $60\%$ and $70\%$, then the total acceptance is still similarly $21\%$. Nonetheless, more moves will go to level 2 and 3 and be judged and then be rejected. This slows down the bisection method. We have tested the bisection method and find it lack of efficiency in our calculations. In the bisection method we need to accept or reject using an effective Eq.([\[Accptequationsimp\]](#Accptequationsimp){reference-type="ref" reference="Accptequationsimp"}) at each level which involves the calculation of an effective $f^V_{l'r'}(\mathcal{R}')$ and $f^V_{lr}(\mathcal{R})$. They contain the sum over all the spin and isospin states. This is different from the situations in most bisection method calculations which mostly deal with central interaction which does not have spin isospin structure. This spin and isospin sum makes each level's acceptance rate not too much different from each other, just like the $50\%$, $60\%$ and $70\%$ example above.

Therefore, we find the bisection method does not have a computational advantage over multi-level sampling. As expected, multi-level sampling has a slightly higher acceptance rate than bisection method. This is because the bisection method can reject early. For example, say the total acceptance rate is $a=20\%$ for a 2-level sampling. In bisection method it decomposes the acceptance rate $a$ in to $a_1$ for level 1 and $a_2$ for level 2, and theoretically $a=a_1a_2$. If $a_1$ and $a_2$ are both less than $100\%$ then the acceptance rate of bisection and 2-level sampling are the same, both are $a=20\%$. But, in bisection it sometimes happens that $a_1=10\%$ and $a_2=200\%$ (when it is bigger than $100\%$ it simply means always accepting the moves), so theoretically $a_1a_2$ is still $20\%$, but actually since $a_1=10\%$, $90\%$ of the moves have already been rejected at the level. The real total acceptance is around $10\%$ instead of the $20\%$ for 2-level sampling. We use multi-level sampling in our calculations, because it allows us to take more samples of new configurations per unit time.
